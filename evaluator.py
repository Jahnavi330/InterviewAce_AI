import logging
from typing import List, Optional
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq

from rag import retrieve_context
from prompts import ANSWER_EVALUATION_PROMPT

# Configure logging
logger = logging.getLogger(__name__)

class EvaluationResult(BaseModel):
    """Pydantic model representing the structured feedback for a candidate's answer."""
    overall_score: float = Field(description="Overall score from 0 to 10")
    technical_accuracy: float = Field(description="Technical accuracy score from 0 to 10")
    completeness: float = Field(description="Completeness score from 0 to 10")
    clarity: float = Field(description="Clarity score from 0 to 10")
    examples: float = Field(description="Examples score from 0 to 10")
    strengths: List[str] = Field(description="List of technical strengths in the answer")
    missing_concepts: List[str] = Field(description="List of missing concepts or omitted information")
    incorrect_statements: List[str] = Field(description="List of incorrect statements made by the candidate")
    ideal_answer: str = Field(description="The ideal answer based on the retrieved context")
    follow_up_question: Optional[str] = Field(None, description="A follow-up question if overall_score < 6.0, else None")
    confidence: str = Field(description="Confidence level of the evaluation (e.g., High, Medium, Low)")
    retrieved_sources: List[str] = Field(description="List of sources or file names used for the evaluation")

def evaluate_answer(question: str, user_answer: str, role: str, vector_store) -> Optional[EvaluationResult]:
    """
    Evaluates the candidate's answer using the RAG pipeline.
    """
    logger.info(f"Evaluating answer for role: {role}")
    
    role_mapping = {
        "Python Developer": "python",
        "Java Developer": "java",
        "Frontend Developer": "frontend",
        "Backend Developer": "backend",
        "AI/ML Engineer": "aiml",
        "Data Analyst": "data_analyst"
    }
    kb_role = role_mapping.get(role, role.lower().replace(" ", "_"))
    
    # 1. Retrieve the top 5 most relevant chunks
    docs = retrieve_context(query=question, vector_store=vector_store, role=kb_role, k=5)
    
    sources = set()
    if not docs:
        logger.warning(f"No context found in vector store for role: {role}.")
        context_str = "No specific context available."
    else:
        context_str = "\n\n".join([doc.page_content for doc in docs])
        for doc in docs:
            file_name = doc.metadata.get("file_name", "Unknown Source")
            sources.add(file_name)
            
    # 2. Use Groq through LangChain
    llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0.3)
    structured_llm = llm.with_structured_output(EvaluationResult)
    
    chain = ANSWER_EVALUATION_PROMPT | structured_llm
    
    try:
        # 3. Compare and evaluate
        result = chain.invoke({
            "question": question,
            "user_answer": user_answer,
            "context": context_str
        })
        
        if result:
            # Inject retrieved sources
            result.retrieved_sources = list(sources)
            logger.info(f"Evaluation complete. Overall score: {result.overall_score}")
            return result
        else:
            logger.error("Failed to parse LLM structured output.")
            return None
    except Exception as e:
        logger.error(f"Error during answer evaluation: {e}")
        return None

def calculate_scores(evaluation_result: EvaluationResult) -> dict:
    """
    Helper function to extract scores.
    """
    if not evaluation_result:
        return {}
    return {
        "overall_score": evaluation_result.overall_score,
        "technical_accuracy": evaluation_result.technical_accuracy,
        "completeness": evaluation_result.completeness,
        "clarity": evaluation_result.clarity,
        "examples": evaluation_result.examples
    }

def generate_followup(missing_concepts: List[str]) -> Optional[str]:
    """
    Independent helper to generate a follow-up question dynamically outside of the main evaluation.
    """
    if not missing_concepts:
        return None
        
    from langchain_core.prompts import PromptTemplate
    prompt = PromptTemplate.from_template(
        "Based on the following missing concepts from a candidate's answer, generate exactly one realistic follow-up interview question to help them improve. Do not provide the answer.\nMissing concepts: {concepts}"
    )
    llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0.7)
    chain = prompt | llm
    
    try:
        response = chain.invoke({"concepts": ", ".join(missing_concepts)})
        return response.content.strip()
    except Exception as e:
        logger.error(f"Error generating follow up: {e}")
        return None

def generate_ideal_answer(question: str, context: str) -> str:
    """
    Independent helper to generate an ideal answer given a question and context.
    """
    from langchain_core.prompts import PromptTemplate
    prompt = PromptTemplate.from_template(
        "Using only the following context, provide a complete, clear, and technically accurate ideal answer to the interview question.\n\nContext:\n{context}\n\nQuestion:\n{question}"
    )
    llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0.3)
    chain = prompt | llm
    
    try:
        response = chain.invoke({"context": context, "question": question})
        return response.content.strip()
    except Exception as e:
        logger.error(f"Error generating ideal answer: {e}")
        return "Could not generate ideal answer."
