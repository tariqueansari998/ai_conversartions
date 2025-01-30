from dotenv import load_dotenv
from langchain.chains.retrieval import create_retrieval_chain
from resume_vertor_store import load_resume_vector_store
from langchain_core.messages import HumanMessage, SystemMessage
from retrievers import history_aware_retriever
from document_chain import doc_chain

def ai_conversation():
    print("Start conversation with AI")
    chat_history = []
    rag_chain = create_retrieval_chain(history_aware_retriever, doc_chain)
    while True:
        query = input("You:")
        if query.lower() == 'exit':
            break
        result = rag_chain.invoke({"input": query, "chat_history": chat_history})
        print(f"AI: {result['answer']}")
        chat_history.append(HumanMessage(content=query))
        chat_history.append(SystemMessage(content=result['answer']))


if __name__ == '__main__':
    load_dotenv()
    load_resume_vector_store()
    ai_conversation()
