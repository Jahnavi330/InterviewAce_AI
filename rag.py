import os
import logging
from typing import List, Optional

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def load_documents(knowledge_dir: str) -> List[Document]:
    """
    Recursively scans the knowledge directory, detects supported file types,
    and loads them with appropriate loaders while preserving metadata.
    """
    documents = []
    
    if not os.path.exists(knowledge_dir):
        logger.warning(f"Knowledge directory '{knowledge_dir}' does not exist.")
        return documents

    for root, _, files in os.walk(knowledge_dir):
        for file in files:
            file_path = os.path.join(root, file)
            # Derive role from folder name (relative to knowledge_dir)
            rel_path = os.path.relpath(root, knowledge_dir)
            role = rel_path if rel_path != "." else "general"
            
            try:
                if file.lower().endswith(".pdf"):
                    loader = PyPDFLoader(file_path)
                    docs = loader.load()
                    for doc in docs:
                        doc.metadata["role"] = role
                        doc.metadata["file_name"] = file
                    documents.extend(docs)
                elif file.lower().endswith((".md", ".txt")):
                    loader = TextLoader(file_path, encoding='utf-8')
                    docs = loader.load()
                    for doc in docs:
                        doc.metadata["role"] = role
                        doc.metadata["file_name"] = file
                    documents.extend(docs)
                else:
                    logger.debug(f"Skipping unsupported file type: {file_path}")
            except Exception as e:
                logger.error(f"Error loading {file_path}: {e}")
                
    logger.info(f"Loaded {len(documents)} document pages/files.")
    return documents

def split_documents(documents: List[Document]) -> List[Document]:
    """
    Splits documents into smaller chunks suitable for embedding and retrieval.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        is_separator_regex=False,
    )
    chunks = text_splitter.split_documents(documents)
    logger.info(f"Split documents into {len(chunks)} chunks.")
    return chunks

def create_vectorstore(chunks: List[Document], persist_dir: str = "vectorstore") -> FAISS:
    """
    Creates a FAISS vector database from document chunks and saves it locally.
    """
    if not chunks:
        raise ValueError("No document chunks provided to create vectorstore.")
        
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    logger.info("Initializing vector store and computing embeddings...")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    
    os.makedirs(persist_dir, exist_ok=True)
    vectorstore.save_local(persist_dir)
    logger.info(f"Vector store saved to '{persist_dir}'.")
    return vectorstore

def load_vectorstore(persist_dir: str = "vectorstore", force_rebuild: bool = False, knowledge_dir: str = "knowledge") -> Optional[FAISS]:
    """
    Loads an existing FAISS database, or optionally rebuilds it if force_rebuild=True 
    or if it doesn't exist.
    """
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    if not force_rebuild and os.path.exists(persist_dir) and os.path.exists(os.path.join(persist_dir, "index.faiss")):
        logger.info(f"Loading existing vector store from '{persist_dir}'.")
        try:
            # allow_dangerous_deserialization=True is required for loading FAISS index in newer versions
            vectorstore = FAISS.load_local(persist_dir, embeddings, allow_dangerous_deserialization=True)
            return vectorstore
        except Exception as e:
            logger.error(f"Error loading vector store: {e}. Rebuilding...")
            # Fall through to rebuild
            
    logger.info("Rebuilding vector store...")
    documents = load_documents(knowledge_dir)
    if not documents:
        logger.warning("No documents found. Cannot build vector store.")
        return None
        
    chunks = split_documents(documents)
    return create_vectorstore(chunks, persist_dir)

def retrieve_context(query: str, vector_store: FAISS, role: Optional[str] = None, k: int = 5) -> List[Document]:
    """
    Retrieves the most relevant context from the FAISS vector store for a given query.
    Optionally filters by role.
    """
    if not vector_store:
        logger.error("Vector store is not initialized.")
        return []
        
    logger.info(f"Retrieving context for query: '{query}', role: {role}")
    
    try:
        filter_dict = {"role": role} if role else None
        
        # FAISS implementation in LangChain supports filtering via metadata
        if filter_dict:
            docs = vector_store.similarity_search(query, k=k, filter=filter_dict)
        else:
            docs = vector_store.similarity_search(query, k=k)
            
        return docs
    except Exception as e:
        logger.error(f"Error retrieving context: {e}")
        return []
