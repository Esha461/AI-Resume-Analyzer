from PyPDF2 import PdfReader
from docx import Document


def extract_text(uploaded_file):
    filename = uploaded_file.name.lower()

    if filename.endswith(".pdf"):
        reader = PdfReader(uploaded_file)
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        return text

    elif filename.endswith(".docx"):
        doc = Document(uploaded_file)
        text = ""

        for para in doc.paragraphs:
            text += para.text + "\n"

        return text

    return ""
