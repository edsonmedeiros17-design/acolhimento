import streamlit as st

st.set_page_config(page_title="Edson Medeiros", layout="centered")

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

st.components.v1.html(html, height=900, scrolling=True)
