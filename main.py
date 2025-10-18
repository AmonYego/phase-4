import streamlit as st
from PyPDF2 import PdfReader
import google.generativeai as genai

st.set_page_config(page_title="ClassRoom AI", page_icon="🎓")

st.title("ClassRoom AI")
st.header("Your AI Revision Coach 🎓")
st.write("Upload your notes and past papers to get AI-powered analysis and quizzes.")

lecture_file = st.file_uploader("📘 Upload Notes (PDF)", type="pdf")
pastpaper_file = st.file_uploader("📄 Upload Past Papers (PDF)", type="pdf")

if lecture_file and pastpaper_file:
    st.success("✅ Files uploaded successfully! Day 2 we’ll start analyzing them.")
else:
    st.info("Please upload both files to continue.")



def extract_text(pdf):
    reader = PdfReader(pdf)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

if lecture_file and pastpaper_file:
    lecture_text = extract_text(lecture_file)
    pastpaper_text = extract_text(pastpaper_file)

    st.write("### Extracted Lecture Notes:")
    st.write(lecture_text[:1000])  # preview first 1000 chars

    GEMINI_API_KEY="AIzaSyARKbi8gr-3sLsw5KOEsZMUsudHA53sxBA"
    import google.generativeai as genai

    genai.configure(api_key="AIzaSyARKbi8gr-3sLsw5KOEsZMUsudHA53sxBA")

    #model = genai.GenerativeModel("gemini-1.5-flash")
    #model = genai.GenerativeModel("gemini-1.0-pro")
    model = genai.GenerativeModel("gemini-2.5-flash")


    def compare_texts(lecture_text, past_paper_text):
        prompt = f"""
        Compare the following two documents:
        1. Lecture Notes:
        {lecture_text[:2000]}

        2. Past Paper:
        {past_paper_text[:2000]}

        Identify the most repeated and important concepts for students to study.
        Then explain each concept simply.
        """
        response = model.generate_content(prompt)
        return response.text


if lecture_file and pastpaper_file:
    lecture_text = extract_text(lecture_file)
    pastpaper_text = extract_text(pastpaper_file)
    st.write("### Analyzing with Gemini AI...")
    result = compare_texts(lecture_text, pastpaper_text)
    st.write(result)

