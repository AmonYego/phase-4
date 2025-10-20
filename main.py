import streamlit as st
from PyPDF2 import PdfReader
import google.generativeai as genai
import time

st.set_page_config(page_title="ClassRoom AI", page_icon="🎓")
st.title("ClassRoom AI")
st.header("Ace your exams — Revise Like a Pro with AI")
st.write("Upload your class notes and past papers for AI-powered topic analysis, simple explanations, and smart practice questions — or chat directly with the AI to get instant help, explanations, and revision support.")
genai.configure(api_key="AIzaSyARKbi8gr-3sLsw5KOEsZMUsudHA53sxBA")
model = genai.GenerativeModel("gemini-2.5-flash")
mode = st.radio("Choose a mode:", ["📄 Analyze Notes/Past Papers", "💬 Ask AI a Question"])

if mode == "📄 Analyze Notes/Past Papers":
   lecture_file = st.file_uploader("📘 Upload Lecture Notes (PDF)", type="pdf")
   pastpaper_file = st.file_uploader("📄 Upload Past Papers/Exams (PDF)", type="pdf")
   def extract_text(pdf):
       reader = PdfReader(pdf)
       text = ""
       for page in reader.pages:
           text += page.extract_text() + "\n"
       return text
   def extract_study_topics(lecture_text, pastpaper_text):
       prompt = f"""
   You are an educational AI assistant. Compare the following documents (lecture notes and past papers) and perform the following:

   1. Identify the **top 5 most frequently tested or emphasized concepts** based on past papers vs lecture content.
   2. For each concept, provide a **short, simple, and student-friendly explanation**.
   3. Be concise, clear, and avoid unnecessary jargon.
   4. Format the response using the structure below:

   **📌 KEY CONCEPTS:**
   - List the 5 concepts clearly in bullet form.

   **📘 EXPLANATIONS:**
   For each key concept, provide:
   Concept Name:
   Short Explanation (2–3 sentences max).

   Ensure the formatting is clean and easy for students to read and revise.
   Lecture Notes:
       {lecture_text[:]}

       Past Paper:
       {pastpaper_text[:]}
       """

       response = model.generate_content(prompt)
       return response.text

   def simplify(lecture_text, pastpaper_text):
       prompt = f"""
          You are a patient tutor who explains concepts in the simplest way possible using real-life analogies, examples, and step-by-step breakdowns. Assume the learner is a slow learner.

          Using the results below, explain each concept clearly in everyday language:

          RESULTS:
          {result}

          Now, based on the context in the lecture notes and past papers, further clarify using relatable analogies:

          LECTURE NOTES:
          {lecture_text}

          PAST PAPERS:
          {pastpaper_text}

          ✅ Your task:
          1. For each concept in the results, explain it as if teaching a slow learner.
          2. Use at least one everyday analogy for each concept.
          3. Break complex concepts into smaller steps.
          4. Give an easy example a high school student can understand.
          5. Keep explanations short, friendly, and encouraging.

          📘 Format like this:

          **Concept Name:**
          🔹 Simple Explanation:
          🔹 Analogy (real-life comparison):
          🔹 Example:
          🔹 Why it matters:

          Make it feel like a supportive tutor is guiding the student gently.
          """

       response = model.generate_content(prompt)
       return response.text


   def generate_practice_questions(lecture_text, pastpaper_text):
       prompt = f"""
       You are an expert academic examiner and educational AI. Carefully analyze and compare the concepts that appear in BOTH the lecture notes and past papers provided below. From the overlapping or recurring concepts:

       ✅ Generate exactly **30 well-structured, high-quality exam-style questions**.
       ✅ Use a natural mix of question types, such as:
          - Short-answer questions
          - Structured/descriptive questions
          - Calculation or problem-solving questions (ONLY if applicable to the subject)
       ✅ Include a natural progression of difficulty (a blend of easier, moderately challenging, and advanced questions), but do NOT label or categorize difficulty levels.
       ✅ Ensure conceptual coverage is broad yet focused on repeated topics.
       ✅ Questions should feel professionally set, as in a formal college/university exam.
       ✅ DO NOT include multiple-choice questions.
       ✅ DO NOT provide any answers.

       📘 Format your response clearly as:

       **📚 EXAM QUESTION SET (30 Questions):**

       1. ...
       2. ...
       3. ...
       ...
       30. ...

       ---

       Here are the lecture notes:
       {lecture_text[:]}

       Here are the past papers:
       {pastpaper_text[:]}
       """

       response = model.generate_content(prompt)
       return response.text

   if lecture_file and pastpaper_file:
           with st.spinner("🤖 AI is thinking... hang tight!"):
               st.success("✅Files received")
               st.subheader("I’m now carefully analyzing your content—this may take a few seconds. ⏳")
               lecture_text = extract_text(lecture_file)
               pastpaper_text = extract_text(pastpaper_file)
               practice_questions = generate_practice_questions(lecture_text, pastpaper_text)
               with st.spinner("🚀 Powering up your success... analyzing now!"):
                       result = extract_study_topics(lecture_text, pastpaper_text)
                       st.success("🚀 Your AI-powered revision pack is ready!🔥")
                       st.balloons()
                       st.subheader("Your personalized study guide is now ready - time to grow smarter")
                       st.write(result)

               if st.button("Simplify explanation"):
                           explanation=simplify(lecture_text, pastpaper_text)
                           st.write(explanation)
               st.download_button(
                           label="📥 Download Practice Questions",
                           data=practice_questions,
                           file_name="practice_questions.txt",
                           mime="text/plain"
                       )


   else:
           st.info("Please upload both files to continue.")
elif mode == "💬 Ask AI a Question":

    # Step 1: Ask for user input
    user_question = st.text_input("Ask a question:")

    # Step 2: Define the function (outside of button)
    def generate_answer(user_question):
        prompt = f"""
        You are an expert educational AI tutor who explains academic questions clearly and simply.
        The student asked:

        "{user_question}"

        Please respond with:
        📘 Explanation: Explain in a clear and simple way using an analogy if helpful.
        📍 Summary: Give a quick summary in 2 bullet points.
        📝 Practice Question: Provide 1 similar question for practice (without the answer).
        """

        response = model.generate_content(prompt)  # Your Gemini/OpenAI call
        return response.text  # Adjust if using OpenAI

    # Step 3: Show button and call function
    if st.button("Get Answer"):
        if user_question:
            answer = generate_answer(user_question)
            st.success(answer)
        else:
            st.warning("Please enter a question first.")

st.markdown("""
<div style='text-align: center; padding-top: 30px; color: gray; font-size: 14px;'>
    🛠️ Built by <b>Papa Yego</b>
</div>
""", unsafe_allow_html=True)




