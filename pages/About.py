import streamlit as st

with open('copy/about.md', 'r') as f:
    body = f.read()

st.image('assets/header_icon.png', width=150)

st.markdown(body, unsafe_allow_html=False, help=None)

