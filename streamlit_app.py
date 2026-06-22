import os
import ssl

# Globally disable SSL certificate verification in Python standard library
try:
    ssl._create_default_https_context = ssl._create_unverified_context
except Exception:
    pass

# Disable warnings about unverified HTTPS requests
import urllib3
try:
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
except Exception:
    pass

# Patch httpx to disable SSL verification
try:
    import httpx
    original_httpx_init = httpx.Client.__init__
    def patched_httpx_init(self, *args, **kwargs):
        kwargs['verify'] = False
        original_httpx_init(self, *args, **kwargs)
    httpx.Client.__init__ = patched_httpx_init
except Exception:
    pass

# Patch requests to disable SSL verification
try:
    import requests
    original_requests_init = requests.Session.__init__
    def patched_requests_init(self, *args, **kwargs):
        original_requests_init(self, *args, **kwargs)
        self.verify = False
    requests.Session.__init__ = patched_requests_init
except Exception:
    pass

os.environ["HF_HUB_DISABLE_SSL_VERIFICATION"] = "1"
os.environ["CURL_CA_BUNDLE"] = ""
os.environ["PYTHONHTTPSVERIFY"] = "0"

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