import streamlit as st

st.page_link("pages/chat.py", label="Chat", icon="🌀")
st.title("🎈 Streamlit PoC")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.divider()

# README
st.title("👀 README.md")
with open('README.md', 'r') as f:
    content = f.read()

st.markdown(content)
st.divider()

# CODE
st.title("💾 CODE")
code = """
# README
st.title("👀 README.md")
with open('README.md', 'r') as f:
    content = f.read()

st.markdown(content)
"""

st.code(code)
st.divider()
