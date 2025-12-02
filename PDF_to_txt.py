import streamlit as st
import requests

st.title("MLA Citation Generator (DOI-based)")

doi = st.text_input("Enter DOI (e.g. 10.1038/nphys1170)")

def generate_mla(doi):
    url = f"https://api.crossref.org/works/{doi}"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()["message"]

    authors = data.get("author", [])
    if authors:
        first_author = authors[0]
        last = first_author.get("family", "")
        first = first_author.get("given", "")
        author_part = f"{last}, {first}, "
    else:
        author_part = ""

    title = data.get("title", [""])[0]
    container = data.get("container-title", [""])[0]
    year = data.get("published-print", {}).get("date-parts", [[None]])[0][0]

    doi_link = f"https://doi.org/{doi}"

    mla = f'{author_part}"{title}." {container}, {year}, {doi_link}.'
    return mla


if st.button("Generate MLA Citation"):
    if not doi:
        st.warning("Please enter a DOI.")
    else:
        mla = generate_mla(doi)
        if mla:
            st.text_area("MLA Citation", mla, height=200)
        else:
            st.e
