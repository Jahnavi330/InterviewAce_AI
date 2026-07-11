import logging
from typing import List, Optional
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq

from rag import retrieve_context
from prompts import INTERVIEW_GENERATION_PROMPT

# Configure logging
logger = logging.getLogger(__name__)

class Question(BaseModel):
    """Pydantic model representing a single interview question."""
    question_number: int = Field(description="The sequential number of the question (1 to 5)")
    question: str = Field(description="The interview question text")
    topic: str = Field(description="The specific topic or concept being tested")
    difficulty: str = Field(description="The difficulty level of the question (Easy, Medium, Hard)")
    expected_answer_summary: str = Field(description="A concise 2-4 line summary of what a good answer should include")
    follow_up_question: Optional[str] = Field(None, description="An optional follow-up question to dig deeper into the candidate's knowledge")

class Interview(BaseModel):
    """Pydantic model representing a complete interview session with exactly 5 questions."""
    questions: List[Question] = Field(description="A list of exactly 5 interview questions")

def generate_interview(role: str, difficulty: str, vector_store) -> Optional[Interview]:
    """
    Generates a realistic 5-question interview based on the selected role and difficulty.
    Uses the RAG pipeline to retrieve relevant context.
    """
    logger.info(f"Generating interview for role: {role}, difficulty: {difficulty}")
    
    # Map role strings to directory names used in the knowledge base if necessary
    role_mapping = {
        "Python Developer": "python",
        "Java Developer": "java",
        "Frontend Developer": "frontend",
        "Backend Developer": "backend",
        "AI/ML Engineer": "aiml",
        "Data Analyst": "data_analyst"
    }
    kb_role = role_mapping.get(role, role.lower().replace(" ", "_"))
    
    # 1. Retrieve context using RAG
    query = f"Interview questions and concepts for {role} at {difficulty} difficulty"
    docs = retrieve_context(query=query, vector_store=vector_store, role=kb_role, k=10)
    
    if not docs:
        logger.warning(f"No context found in vector store for role: {role}. Proceeding without detailed context.")
        context_str = "No specific context available. Use general industry knowledge."
    else:
        context_str = "\n\n".join([doc.page_content for doc in docs])
        
    # 2. Use Gemini through LangChain
    llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0.7)
    
    # 3. Request Structured Output
    structured_llm = llm.with_structured_output(Interview)
    
    chain = INTERVIEW_GENERATION_PROMPT | structured_llm
    
    try:
        result = chain.invoke({
            "role": role,
            "difficulty": difficulty,
            "context": context_str
        })
        
        # Validate the output
        if validate_questions(result, difficulty):
            return result
        else:
            logger.error("Generated interview failed validation.")
            return None
            
    except Exception as e:
        logger.error(f"Error during interview generation: {e}")
        return None

def validate_questions(interview: Interview, expected_difficulty: str) -> bool:
    """
    Validates the generated interview questions based on rules.
    """
    if not interview or not interview.questions:
        logger.error("No questions generated.")
        return False
        
    if len(interview.questions) != 5:
        logger.error(f"Expected 5 questions, but got {len(interview.questions)}.")
        return False
        
    # Ensure no duplicates
    question_texts = set()
    for q in interview.questions:
        if q.question in question_texts:
            logger.error(f"Duplicate question detected: {q.question}")
            return False
        question_texts.add(q.question)
        
    return True

def generate_question(topic: str, difficulty: str) -> Optional[Question]:
    """
    Generates a single interview question for a specific topic.
    This can be used for dynamic follow-ups or single question generation.
    """
    from prompts import QUESTION_GENERATION_PROMPT
    from langchain_core.prompts import PromptTemplate
    
    logger.info(f"Generating single question for topic: {topic}, difficulty: {difficulty}")
    
    prompt = PromptTemplate.from_template(
        "Generate one {difficulty} interview question about {topic}. Provide the output strictly as structured JSON."
    )
    
    llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0.7)
    structured_llm = llm.with_structured_output(Question)
    chain = prompt | structured_llm
    
    try:
        result = chain.invoke({"topic": topic, "difficulty": difficulty})
        return result
    except Exception as e:
        logger.error(f"Error generating single question: {e}")
        return None
