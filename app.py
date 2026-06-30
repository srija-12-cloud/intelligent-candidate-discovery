import streamlit as st

st.set_page_config(page_title="Intelligent Candidate Discovery")

st.title("🤖 Intelligent Candidate Discovery")

job_description = st.text_area("Enter Job Description")

uploaded_files = st.file_uploader(
    "Upload Candidate Resumes",
    accept_multiple_files=True,
    type=["pdf", "txt"]
)

if st.button("Find Best Candidates"):
    st.success("Candidate matching process started!")
    st.write("This is the prototype version of the application.")
