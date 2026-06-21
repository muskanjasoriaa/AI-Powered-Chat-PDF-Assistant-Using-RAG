import streamlit as st
from utils.pdf_loader import extract_text
from utils.text_splitter import split_text
from utils.embeddings import get_embeddings
from utils.qa_chain import get_qa_chain

from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI

st.title("AI PDF Chat Assistant")

# Retrieve API Key from sidebar or Secrets
openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
if not openai_api_key:
    # Try to load from Streamlit Secrets
    try:
        openai_api_key = st.secrets["OPENAI_API_KEY"]
    except Exception:
        pass

if not openai_api_key:
    st.info("Please enter your OpenAI API Key in the sidebar to proceed.")
    st.stop()

uploaded_files = st.file_uploader(
    "Upload PDFs",
    type="pdf",
    accept_multiple_files=True
)

if uploaded_files:

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

    question = st.text_input("Ask a question")

    if question:

        answer = qa.run(question)

        st.write(answer)