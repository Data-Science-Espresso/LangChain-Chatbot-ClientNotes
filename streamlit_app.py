# streamlit_app.py: Web app with Streamlit
import streamlit as st
from chatbot_core_onenote import build_qa_chain

st.set_page_config(page_title="🗒️ OneNote-Chatbot", layout="wide")
st.title("🗒️ Chat with your OneNote Notes")

qa_chain = build_qa_chain("customer_xy_notes.txt")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

question = st.text_input("What would you like to know about your customer notes?", key="input")

if question:
    result = qa_chain({
        "question": question,
        "chat_history": st.session_state.chat_history
    })

    st.session_state.chat_history.append((question, result["answer"]))

    for i, (q, a) in enumerate(st.session_state.chat_history[::-1]):
        st.markdown(f"**❓ Question {len(st.session_state.chat_history) - i}:** {q}")
        st.markdown(f"**🤖 Answer:** {a}")