from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from resume_vertor_store import get_retriever
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain_community.llms import Ollama

llm = Ollama(model="llama3")
retriever = get_retriever()
contextualize_q_system_prompt = (
    "Given a chat history and the latest user question "
    "which might reference context in the chat history, "
    "formulate a standalone question which can be understood "
    "without the chat history. Do NOT answer the question, just "
    "reformulate it if needed and otherwise return it as is."
)
# Create a prompt template for contextualizing questions
contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", contextualize_q_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)

history_aware_retriever = create_history_aware_retriever(llm, retriever, contextualize_q_prompt)