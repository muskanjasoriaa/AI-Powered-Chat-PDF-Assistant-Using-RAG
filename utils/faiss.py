from langchain_community.vectorstores import FAISS
from utils.embeddings import get_embeddings

def create_vectorstore(chunks):
    vectorstore = FAISS.from_texts(
        texts=chunks,
        embedding=get_embeddings()
    )

    return vectorstore