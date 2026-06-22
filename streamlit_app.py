import os
import streamlit as st
from utils.pdf_loader import extract_text
from utils.text_splitter import split_text
from utils.embeddings import get_embeddings
from utils.qa_chain import get_qa_chain

from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI

# --- Get API Key from environment only (hidden from user) ---
openai_api_key = os.environ.get("OPENAI_API_KEY")

if not openai_api_key:
    st.error("⚠️ API Key not configured. Please set OPENAI_API_KEY environment variable.")
    st.stop()

# --- UI ---
st.title("📄 AI PDF Chat Assistant")
st.write("Upload a PDF and ask questions about it!")

uploaded_files = st.file_uploader(
    "Upload PDFs",
    type="pdf",
    accept_multiple_files=True
)

if uploaded_files:
    with st.spinner("Processing your PDF..."):
        text = extract_text(uploaded_files)
        chunks = split_text(text)
        vectorstore = FAISS.from_texts(
            chunks,
            embedding=get_embeddings()
        )
        llm = ChatOpenAI(
            model="gpt-4o-mini",
            api_key=openai_api_key
        )
        qa = get_qa_chain(llm, vectorstore)

    st.success("✅ PDF processed! Ask your question below.")

    question = st.text_input("💬 Ask a question about your PDF")

    if question:
        with st.spinner("Thinking..."):
            answer = qa.run(question)
        st.write("### Answer:")
        st.write(answer)
