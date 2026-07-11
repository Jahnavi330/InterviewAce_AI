import os
import sys
import json

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from rag import load_vectorstore
from evaluator import evaluate_answer, calculate_scores

def test_evaluation():
    print("Loading Vector Store...")
    # Ensure GROQ_API_KEY is in .env before running
    vector_store = load_vectorstore(force_rebuild=False)
    
    if not vector_store:
        print("Vector store not found. Please ensure the knowledge base is built first.")
        return
        
    question = "Explain the difference between a list and a tuple in Python."
    # A partially correct answer to see if it generates missing concepts and follow ups
    user_answer = "A list is mutable, which means you can change it. A tuple is immutable. Both can store multiple items."
    role = "Python Developer"
    
    print(f"\nEvaluating Question: {question}")
    print(f"User Answer: {user_answer}\n")
    
    result = evaluate_answer(question, user_answer, role, vector_store)
    
    if result:
        print("--- Evaluation Result ---")
        # Convert to dictionary and print as formatted JSON
        print(json.dumps(result.model_dump(), indent=2))
        
        scores = calculate_scores(result)
        print("\n--- Extracted Scores ---")
        print(json.dumps(scores, indent=2))
    else:
        print("\nFailed to evaluate answer.")

if __name__ == "__main__":
    test_evaluation()
