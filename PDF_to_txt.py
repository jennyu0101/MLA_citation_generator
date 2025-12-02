# app.py
import streamlit as st
from cite_master import CiteMaster   # CiteMaster 패키지 필요

st.title("MLA Citation Generator")

input_type = st.radio("Input type:", ["Paper title", "DOI"])
if input_type == "Paper title":
    paper_title = st.text_input("Enter the paper title")
    user_input = paper_title.strip()
elif input_type == "DOI":
    doi = st.text_input("Enter the DOI (e.g. 10.1016/j.rser.2020.109984)")
    user_input = doi.strip()

if st.button("Generate MLA citation"):
    if not user_input:
        st.warning("Please enter a paper title or DOI.")
    else:
        try:
            cm = CiteMaster()  # create instance
            # 예: format = 'mla', include_bibtex False
            citation = cm.format_citation(user_input, style="mla")
            st.text_area("MLA Citation", citation, height=150)
        except Exception as e:
            st.error(f"Error generating citation: {e}")
