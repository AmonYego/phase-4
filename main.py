import streamlit as st

st.set_page_config(page_title="AI Revision Coach", page_icon="🎓")

st.title("🎓 AI Revision Coach (MVP)")
st.write("Upload your notes and past papers to get AI-powered analysis and quizzes.")

uploaded_notes = st.file_uploader("📘 Upload Notes (PDF)", type="pdf")
uploaded_papers = st.file_uploader("📄 Upload Past Papers (PDF)", type="pdf")

if uploaded_notes and uploaded_papers:
    st.success("✅ Files uploaded successfully! Day 2 we’ll start analyzing them.")
else:
    st.info("Please upload both files to continue.")
