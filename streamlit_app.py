"""
Gemini-Based Curriculum Generator – Prototype
"""

import streamlit as st

st.title("AI Curriculum Generator (Demo)")
topic = st.text_input("Enter a topic you want to learn")

if st.button("Generate"):
    st.success(f"Stub curriculum for: {topic}")
    st.write("- Lesson 1: Intro")
    st.write("- Lesson 2: Key Concepts")
    st.write("- Lesson 3: Practice Tasks")
