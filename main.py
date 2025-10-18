import streamlit as st
from PyPDF2 import PdfReader

st.set_page_config(page_title="ClassRoom AI", page_icon="🎓")

st.title("ClassRoom AI")
st.header("Your AI Revision Coach 🎓")
st.write("Upload your notes and past papers to get AI-powered analysis and quizzes.")

uploaded_notes = st.file_uploader("📘 Upload Notes (PDF)", type="pdf")
uploaded_papers = st.file_uploader("📄 Upload Past Papers (PDF)", type="pdf")

if uploaded_notes and uploaded_papers:
    st.success("✅ Files uploaded successfully! Day 2 we’ll start analyzing them.")
else:
    st.info("Please upload both files to continue.")



def extract_text(pdf):
    reader = PdfReader(pdf)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

