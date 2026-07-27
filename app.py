import streamlit as st
import re
import time
import plotly.graph_objects as go

from parser import extract_text
from analyzer import analyze_resume


st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


# Sidebar
with st.sidebar:
    st.title("🤖 AI Resume Analyzer")

    st.markdown("---")

    st.write("### 🚀 Powered By")
    st.write("Groq + Llama 3.3")

    st.markdown("---")

    st.write("### ✨ Features")

    st.write("✅ ATS Score")
    st.write("✅ Resume Analysis")
    st.write("✅ Skill Gap Detection")
    st.write("✅ Interview Questions")
    st.write("✅ Resume Text Extraction")
    st.write("✅ Download Report")

    st.markdown("---")

    st.info("🎓 College Project")


# Main page
st.title("📄 AI Resume Analyzer")

st.write("Upload your resume and paste the job description below.")


resume = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)


job_description = st.text_area(
    "Paste Job Description",
    height=250
)


if st.button("Analyze Resume"):

    if resume is None:
        st.error("Please upload a resume.")

    elif job_description.strip() == "":
        st.error("Please enter a job description.")

    else:

        with st.spinner("Analyzing Resume..."):

            start = time.time()

            # Extract resume text
            resume_text = extract_text(resume)


            # Analyze resume
            result = analyze_resume(
                resume_text,
                job_description
            )


            end = time.time()


        st.success("Analysis Complete!")

        st.info(
            f"⏱ Analysis completed in {round(end-start,2)} seconds"
        )


        # Resume Details

        st.write("### 📄 Uploaded Resume")


        col1, col2 = st.columns(2)


        with col1:
            st.metric(
                "Resume Name",
                resume.name
            )


        with col2:
            st.metric(
                "File Size (KB)",
                round(resume.size/1024,2)
            )



        # ATS Score

        st.subheader("🎯 ATS Score")


        score_match = re.search(
            r'(\d+)\s*out of\s*100',
            result,
            re.IGNORECASE
        )


        if score_match:

            score = int(score_match.group(1))


            if score >= 80:
                st.success(
                    f"ATS Score: {score}/100"
                )

            elif score >= 60:
                st.warning(
                    f"ATS Score: {score}/100"
                )

            else:
                st.error(
                    f"ATS Score: {score}/100"
                )


            st.progress(score/100)


            fig = go.Figure(
                go.Indicator(
                    mode="gauge+number",
                    value=score,
                    title={"text":"ATS Score"},
                    gauge={
                        "axis":{"range":[0,100]},
                        "steps":[
                            {
                                "range":[0,50],
                                "color":"#ffcccc"
                            },
                            {
                                "range":[50,80],
                                "color":"#fff3cd"
                            },
                            {
                                "range":[80,100],
                                "color":"#d4edda"
                            }
                        ]
                    }
                )
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )


        # Tabs

        tab1, tab2 = st.tabs(
            [
                "📊 Analysis",
                "📄 Resume Text"
            ]
        )


        with tab1:
            st.markdown(result)


        with tab2:
            st.text_area(
                "Extracted Resume Text",
                resume_text,
                height=500
            )


        # Download Report

        st.markdown("---")

st.subheader("✉️ AI Cover Letter Generator")

if st.button("Generate Cover Letter"):

    cover_letter = generate_cover_letter(
        resume_text,
        job_description
    )

    st.write(cover_letter)

    st.download_button(
        label="📥 Download Cover Letter",
        data=cover_letter,
        file_name="cover_letter.txt",
        mime="text/plain"
    )