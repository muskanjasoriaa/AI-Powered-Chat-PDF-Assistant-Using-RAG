from langchain_classic.chains import RetrievalQA

def get_qa_chain(llm, vectorstore):

    retriever = vectorstore.as_retriever()

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever
    )

    return qa