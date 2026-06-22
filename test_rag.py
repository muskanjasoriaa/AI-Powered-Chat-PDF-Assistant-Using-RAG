import os
import ssl

# Globally disable SSL certificate verification in Python standard library
ssl._create_default_https_context = ssl._create_unverified_context

# Disable warnings about unverified HTTPS requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Patch httpx to disable SSL verification
import httpx
original_httpx_init = httpx.Client.__init__
def patched_httpx_init(self, *args, **kwargs):
    kwargs['verify'] = False
    original_httpx_init(self, *args, **kwargs)
httpx.Client.__init__ = patched_httpx_init

# Patch requests to disable SSL verification
import requests
original_requests_init = requests.Session.__init__
def patched_requests_init(self, *args, **kwargs):
    original_requests_init(self, *args, **kwargs)
    self.verify = False
requests.Session.__init__ = patched_requests_init

os.environ["HF_HUB_DISABLE_SSL_VERIFICATION"] = "1"
os.environ["CURL_CA_BUNDLE"] = ""
os.environ["PYTHONHTTPSVERIFY"] = "0"

from utils.embeddings import get_embeddings
from utils.faiss import create_vectorstore
from utils.qa_chain import get_qa_chain

print("Loading embeddings model...")
embeddings = get_embeddings()
print("Embeddings loaded!")

print("Creating vectorstore...")
chunks = ["This is a test document about Python programming.", "LangChain is a framework for building LLM applications."]
vectorstore = create_vectorstore(chunks)
print("Vectorstore created!")

print("Creating fake LLM...")
from langchain_community.llms.fake import FakeListLLM
llm = FakeListLLM(responses=["This is a mock answer about Python."])

print("Creating QA chain...")
qa = get_qa_chain(llm, vectorstore)
print("QA chain created!")

print("Running QA chain query...")
try:
    res = qa.run("What is Python?")
    print("qa.run output:", res)
except Exception as e:
    print("qa.run failed:", e)

try:
    res_inv = qa.invoke({"query": "What is Python?"})
    print("qa.invoke output:", res_inv)
except Exception as e:
    print("qa.invoke failed:", e)
