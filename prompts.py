"""
Prompts module.
Stores all the prompt templates used for LangChain chains and Gemini interactions.
"""

from langchain_core.prompts import PromptTemplate

ANSWER_EVALUATION_PROMPT = PromptTemplate.from_template(
    """You are an expert technical interviewer evaluating a candidate's answer.
Your evaluation must be based strictly on the provided knowledge base context whenever possible.

Interview Question:
{question}

Candidate's Answer:
{user_answer}

Knowledge Base Context:
{context}

Evaluate the candidate's answer based on the following criteria. Score each category independently from 0 to 10 (decimals allowed):
- technical_accuracy: How factually correct is the answer compared to the context?
- completeness: Did the answer cover all necessary parts of the question?
- clarity: Is the explanation easy to understand and well-structured?
- examples: Did the candidate provide appropriate examples or use cases?

Rules:
1. Provide constructive feedback outlining technical strengths, missing concepts, and incorrect statements (if any).
2. Write an ideal answer based on the context.
3. Determine a confidence level (e.g., High, Medium, Low) for your evaluation based on how much the context covers the question.
4. Calculate an overall_score (0-10) as an average or weighted representation of the above scores.
5. IF the overall_score is strictly below 6.0, you MUST provide exactly one realistic follow-up interview question based on the missing concepts to help the candidate improve. Do not repeat the original question. IF the overall_score is 6.0 or higher, leave follow_up_question empty/null.
6. Return the evaluation strictly in the requested JSON structure.
"""
)

QUESTION_GENERATION_PROMPT = """
Generate an interview question for the following topic: {topic}
"""

INTERVIEW_GENERATION_PROMPT = PromptTemplate.from_template(
    """You are an expert technical interviewer conducting an interview for the role of {role}.
Your task is to generate EXACTLY 5 unique interview questions based on the provided knowledge base context.

Difficulty Level: {difficulty}

Rules for Question Generation:
1. Generate exactly 5 unique questions. DO NOT repeat questions.
2. The questions must accurately match the requested difficulty ({difficulty}). 
3. Maintain the tone of a highly experienced and professional interviewer.
4. Focus strictly on concepts and deep understanding. NO trivia questions.
5. Coding/programming tasks are ALLOWED ONLY for 'Medium' and 'Hard' difficulties. For 'Easy', stick to conceptual questions.
6. Under no circumstances should you ask HR or behavioral questions in this technical interview.
7. Ensure a good, broad coverage of topics based on the context.

Context from Knowledge Base:
{context}

Generate the 5 interview questions following the structured format exactly.
"""
)
