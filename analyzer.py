import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

st.write("GROQ_API_KEY found:", os.getenv("GROQ_API_KEY") is not None)

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)



# -------------------------------
# Resume Analyzer Function
# -------------------------------

def analyze_resume(resume_text, job_description):
    import streamlit as st

    prompt = f"""
You are an expert ATS Resume Analyzer.

Analyze the candidate resume according to the job description.

Resume:
{resume_text}


Job Description:
{job_description}


Provide the analysis in this format:

## 1. Resume Match Score
Give a score out of 100.

## 2. Skills Found
List the skills present in the resume.

## 3. Missing Skills
List important skills missing according to the job description.

## 4. Strengths
Mention strong points of the resume.

## 5. Weaknesses
Mention areas that need improvement.

## 6. Suggestions
Give practical suggestions to improve the resume.

## 7. Interview Questions
Generate 5 technical and HR interview questions.

Use headings and bullet points.
"""


    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.3
    )


    return response.choices[0].message.content





# -------------------------------
# AI Cover Letter Generator
# -------------------------------
print("generate_cover_letter loaded")
def generate_cover_letter(resume_text, job_description):

    prompt = f"""
You are a professional career coach.

Create a personalized cover letter for the candidate using the resume
and job description provided below.


Resume:

{resume_text}


Job Description:

{job_description}


Instructions:

- Write a professional cover letter.
- Mention relevant skills from the resume.
- Match the job requirements.
- Keep it between 250-350 words.
- Use a formal business tone.
- Include opening, body paragraphs, and closing.
- Make it ATS friendly.
"""


    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.5
    )


    return response.choices[0].message.content

   
  