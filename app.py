import mimetypes
mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('text/css', '.css')

import streamlit as st
import json
import pandas as pd
from dotenv import load_dotenv

from rag import load_vectorstore
from engine import generate_interview
from evaluator import evaluate_answer

def init_app():
    load_dotenv()
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'landing'
    if 'vector_store' not in st.session_state:
        st.session_state.vector_store = None
    if 'interview' not in st.session_state:
        st.session_state.interview = None
    if 'current_q_index' not in st.session_state:
        st.session_state.current_q_index = 0
    if 'evaluations' not in st.session_state:
        st.session_state.evaluations = []
    if 'follow_up_active' not in st.session_state:
        st.session_state.follow_up_active = False
    if 'follow_up_question' not in st.session_state:
        st.session_state.follow_up_question = None

def restart_interview():
    st.session_state.current_page = 'landing'
    st.session_state.interview = None
    st.session_state.current_q_index = 0
    st.session_state.evaluations = []
    st.session_state.follow_up_active = False
    st.session_state.follow_up_question = None
    st.rerun()

def render_sidebar():
    with st.sidebar:
        st.header("Interview Status")
        if st.session_state.interview:
            st.write(f"**Role:** {st.session_state.role}")
            st.write(f"**Difficulty:** {st.session_state.difficulty}")
            st.progress(st.session_state.current_q_index / 5.0)
            st.write(f"**Question:** {min(st.session_state.current_q_index + 1, 5)} / 5")
        if st.button("Restart Interview"):
            restart_interview()

def show_landing():
    st.title("InterviewAce AI 🎯")
    st.markdown("### Your Professional AI Interview Coach")
    st.write("Welcome to InterviewAce AI. Experience a realistic, dynamic technical interview tailored to your desired role and difficulty level. Get real-time, actionable feedback driven by our advanced Knowledge Base.")
    if st.button("Start Interview", type="primary"):
        st.session_state.current_page = 'config'
        st.rerun()

def show_config():
    st.title("Configure Your Interview")
    
    col1, col2 = st.columns(2)
    with col1:
        role = st.selectbox("Select Role", ["Python Developer", "Java Developer", "Frontend Developer", "Backend Developer", "AI/ML Engineer", "Data Analyst"])
    with col2:
        difficulty = st.selectbox("Select Difficulty", ["Easy", "Medium", "Hard"])
        
    if st.button("Generate Interview", type="primary"):
        with st.spinner("Initializing Knowledge Base and Generating Questions... (this may take a minute)"):
            if not st.session_state.vector_store:
                st.session_state.vector_store = load_vectorstore(force_rebuild=False)
            
            if not st.session_state.vector_store:
                st.error("Failed to load Knowledge Base. Ensure documents are present in 'knowledge' directory and your API key is valid.")
                return
                
            interview = generate_interview(role, difficulty, st.session_state.vector_store)
            if interview and interview.questions:
                st.session_state.interview = interview
                st.session_state.role = role
                st.session_state.difficulty = difficulty
                st.session_state.current_page = 'interview'
                st.rerun()
            else:
                st.error("Failed to generate interview. Please check your API key and try again.")

def render_evaluation_card(eval_result):
    st.markdown("### Evaluation Feedback")
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Overall", f"{eval_result.overall_score}/10")
    col2.metric("Technical", f"{eval_result.technical_accuracy}/10")
    col3.metric("Completeness", f"{eval_result.completeness}/10")
    col4.metric("Clarity", f"{eval_result.clarity}/10")
    col5.metric("Examples", f"{eval_result.examples}/10")
    
    with st.expander("Strengths"):
        if eval_result.strengths:
            for s in eval_result.strengths:
                st.write(f"- {s}")
        else:
            st.write("No specific strengths noted.")
            
    with st.expander("Missing Concepts & Incorrect Statements"):
        if eval_result.missing_concepts:
            st.markdown("**Missing Concepts:**")
            for m in eval_result.missing_concepts:
                st.write(f"- {m}")
        if eval_result.incorrect_statements:
            st.markdown("**Incorrect Statements:**")
            for inc in eval_result.incorrect_statements:
                st.write(f"- {inc}")
                
    with st.expander("Ideal Answer & Suggestions"):
        st.write(eval_result.ideal_answer)
        
    with st.expander("Retrieved Sources & Confidence"):
        st.write(f"**Confidence:** {eval_result.confidence}")
        st.write(f"**Sources:** {', '.join(eval_result.retrieved_sources) if eval_result.retrieved_sources else 'None'}")

def show_interview():
    idx = st.session_state.current_q_index
    questions = st.session_state.interview.questions
    
    if idx >= len(questions):
        st.session_state.current_page = 'report'
        st.rerun()
        
    q = questions[idx]
    
    st.subheader(f"Question {idx + 1} of 5")
    st.caption(f"Topic: {q.topic} | Difficulty: {q.difficulty}")
    
    st.markdown(f"**{q.question}**")
    
    has_been_evaluated = len(st.session_state.evaluations) > idx
    
    if not has_been_evaluated:
        user_answer = st.text_area("Your Answer:", key=f"ans_{idx}", height=150)
        if st.button("Submit Answer", type="primary"):
            if user_answer.strip():
                with st.spinner("Evaluating your answer..."):
                    eval_result = evaluate_answer(q.question, user_answer, st.session_state.role, st.session_state.vector_store)
                    if eval_result:
                        st.session_state.evaluations.append(eval_result)
                        if eval_result.overall_score < 6.0 and eval_result.follow_up_question:
                            st.session_state.follow_up_active = True
                            st.session_state.follow_up_question = eval_result.follow_up_question
                        st.rerun()
                    else:
                        st.error("Evaluation failed. Please try again.")
            else:
                st.warning("Please provide an answer before submitting.")
    else:
        eval_result = st.session_state.evaluations[idx]
        render_evaluation_card(eval_result)
        
        if st.session_state.follow_up_active:
            st.warning("Your score was below 6.0. Let's try to improve it with a follow-up!")
            st.markdown(f"**Follow-up Question:** {st.session_state.follow_up_question}")
            follow_up_answer = st.text_area("Your Follow-up Answer:", key=f"fu_ans_{idx}", height=150)
            
            if st.button("Submit Follow-up"):
                if follow_up_answer.strip():
                    with st.spinner("Re-evaluating..."):
                        combined_question = f"{q.question}\nFollow-up: {st.session_state.follow_up_question}"
                        new_eval = evaluate_answer(combined_question, follow_up_answer, st.session_state.role, st.session_state.vector_store)
                        if new_eval:
                            st.session_state.evaluations[idx] = new_eval
                            st.session_state.follow_up_active = False
                            st.session_state.follow_up_question = None
                            st.rerun()
                else:
                    st.warning("Please provide an answer.")
        else:
            if st.button("Next Question" if idx < 4 else "Finish Interview", type="primary"):
                st.session_state.current_q_index += 1
                st.rerun()

def show_report():
    st.title("Final Interview Report 📊")
    evals = st.session_state.evaluations
    if not evals:
        st.warning("No evaluations found.")
        return
        
    avg_overall = sum(e.overall_score for e in evals) / len(evals)
    avg_tech = sum(e.technical_accuracy for e in evals) / len(evals)
    avg_comp = sum(e.completeness for e in evals) / len(evals)
    avg_clarity = sum(e.clarity for e in evals) / len(evals)
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Avg Overall Score", f"{avg_overall:.1f}/10")
    col2.metric("Avg Technical", f"{avg_tech:.1f}/10")
    col3.metric("Avg Completeness", f"{avg_comp:.1f}/10")
    col4.metric("Avg Clarity", f"{avg_clarity:.1f}/10")
    
    st.markdown("### Performance Summary")
    questions = st.session_state.interview.questions
    
    report_data = []
    strong_topics = []
    weak_topics = []
    
    for i, (q, e) in enumerate(zip(questions, evals)):
        report_data.append({
            "Question": f"Q{i+1}",
            "Topic": q.topic,
            "Score": e.overall_score
        })
        if e.overall_score >= 7.0:
            strong_topics.append(q.topic)
        else:
            weak_topics.append(q.topic)
            
    df = pd.DataFrame(report_data)
    st.table(df)
    
    colA, colB = st.columns(2)
    with colA:
        st.success("**Strong Topics:**\n" + ("\n".join([f"- {t}" for t in set(strong_topics)]) if strong_topics else "None"))
    with colB:
        st.error("**Weak Topics (Needs Improvement):**\n" + ("\n".join([f"- {t}" for t in set(weak_topics)]) if weak_topics else "None"))
        
    st.markdown("### AI Recommendations")
    if weak_topics:
        st.info("Focus your upcoming study sessions on your weak topics. Review the ideal answers provided during the interview.")
    else:
        st.info("Great job! Keep practicing to maintain this level of performance.")
        
    full_trace = {
        "role": st.session_state.role,
        "difficulty": st.session_state.difficulty,
        "average_score": avg_overall,
        "interview": [
            {
                "question": q.model_dump(),
                "evaluation": e.model_dump()
            } for q, e in zip(questions, evals)
        ]
    }
    st.download_button(
        label="Download Full Report (JSON)",
        data=json.dumps(full_trace, indent=2),
        file_name="interview_report.json",
        mime="application/json"
    )

def main():
    st.set_page_config(page_title="InterviewAce AI", page_icon="🎯", layout="wide")
    init_app()
    render_sidebar()
    
    if st.session_state.current_page == 'landing':
        show_landing()
    elif st.session_state.current_page == 'config':
        show_config()
    elif st.session_state.current_page == 'interview':
        show_interview()
    elif st.session_state.current_page == 'report':
        show_report()

if __name__ == "__main__":
    main()
