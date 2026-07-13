# 🎯 InterviewAce AI

**InterviewAce AI** is your professional AI Interview Coach, designed to provide realistic, dynamic technical interviews tailored to your desired role and difficulty level. Built with a modern tech stack, it uses RAG (Retrieval-Augmented Generation) to give you actionable feedback based on a curated Knowledge Base.

🌐 **[Try the Live Demo Here!](https://interviewaceai.streamlit.app/)**

## 🚀 Features

- **Tailored Interviews**: Choose from various roles (Python Developer, Java Developer, Frontend/Backend Developer, AI/ML Engineer, Data Analyst) and difficulties (Easy, Medium, Hard).
- **Dynamic Question Generation**: Leverages LangChain and Groq's fast LLMs to generate contextual interview questions based on the selected role and topic.
- **Real-time Evaluation**: Get instant feedback on your answers, scored on Technical Accuracy, Completeness, Clarity, and Examples.
- **Adaptive Follow-ups**: If you struggle with a question (scoring below 6.0), the AI coach will dynamically ask targeted follow-up questions to give you a chance to improve.
- **Comprehensive Feedback**: Review your strengths, missing concepts, incorrect statements, and the ideal answer for each question.
- **Detailed Final Report**: Get a comprehensive summary of your strong and weak topics. Download the full interview report in JSON format for further review.

## 🛠️ Technology Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **LLM Orchestration**: [LangChain](https://langchain.com/)
- **Vector Database (RAG)**: [FAISS](https://faiss.ai/)
- **Embeddings**: HuggingFace Sentence Transformers
- **LLM API**: [Groq](https://groq.com/) (using the Llama 3.3 70B model)

## ⚙️ Setup and Installation

### Prerequisites
- Python 3.11+
- A [Groq API Key](https://console.groq.com/keys)

### Local Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "InterviewAce AI"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**
   Copy the example environment file and add your Groq API key:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` to include your `GROQ_API_KEY`.

4. **Run the Application**
   ```bash
   streamlit run app.py
   ```
   *(On Windows, you can alternatively use the provided `run_app.bat` script).*

### Docker Setup

You can also run InterviewAce AI using Docker:

1. **Build the image**
   ```bash
   docker build -t interviewace-ai .
   ```

2. **Run the container**
   ```bash
   docker run -p 8501:8501 --env-file .env interviewace-ai
   ```

## 📂 Project Structure

- `app.py`: Main Streamlit application entry point and UI layout.
- `engine.py`: Core logic for generating structured interview questions.
- `evaluator.py`: Logic for evaluating candidate answers and providing granular feedback.
- `rag.py`: RAG pipeline using FAISS to retrieve relevant context from the knowledge base.
- `prompts.py`: LangChain prompt templates for generation and evaluation tasks.
- `knowledge/`: Directory containing the Markdown documents used as the vector store's context.
