from pypdf import PdfReader

def extract_text(pdf_files):
    text = ""

    for pdf in pdf_files:
        reader = PdfReader(pdf)

        for page in reader.pages:
            text += page.extract_text()

    return text