import streamlit as st
import nlu

st.page_link("streamlit_app.py", label="Home", icon="🕌")

st.title("Chat")
prompt = st.chat_input("What's your mood?")
if prompt:
    sentiment = nlu.load('sentiment').predict(prompt)
    st.chat_message(f'sentiment {sentiment}')