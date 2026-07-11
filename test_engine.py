import os
import sys

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from rag import load_vectorstore
from engine import generate_interview

def test_engine():
    print("Loading Vector Store...")
    # Make sure to set GROQ_API_KEY in your .env before running this
    vector_store = load_vectorstore(force_rebuild=False)
    
    if not vector_store:
        print("Vector store not found. Please ensure the knowledge base is built first.")
        return
        
    print("\nGenerating Python Developer Interview (Medium)...")
    interview = generate_interview("Python Developer", "Medium", vector_store)
    
    if interview:
        print("\n--- Generated Interview ---")
        for q in interview.questions:
            print(f"\nQ{q.question_number}: {q.question}")
            print(f"Topic: {q.topic} | Difficulty: {q.difficulty}")
            print(f"Expected Answer: {q.expected_answer_summary}")
            if q.follow_up_question:
                print(f"Follow-up: {q.follow_up_question}")
    else:
        print("\nFailed to generate interview.")

if __name__ == "__main__":
    test_engine()
