import os
import sys

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from rag import load_documents, split_documents

def test_rag_pipeline():
    print("Testing document loading...")
    docs = load_documents("knowledge")
    print(f"Loaded {len(docs)} document chunks/pages.")
    
    if docs:
        print(f"Sample document metadata: {docs[0].metadata}")
        
    print("\nTesting document splitting...")
    chunks = split_documents(docs)
    print(f"Created {len(chunks)} chunks.")
    
    if chunks:
        print(f"Sample chunk metadata: {chunks[0].metadata}")
        print(f"Sample chunk content (first 100 chars): {chunks[0].page_content[:100]}...")

if __name__ == "__main__":
    test_rag_pipeline()
