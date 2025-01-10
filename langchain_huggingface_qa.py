import chainlit as cl
from dotenv import load_dotenv
from langchain_community.llms import HuggingFaceEndpoint
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate

load_dotenv()

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","""
        You are an AI assistant that provides helpful responses to user queries
        """),
        ("user", "{question}\n"),
    ]
)

@cl.on_chat_start
def main():
    model_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"
    llm = HuggingFaceEndpoint(
        repo_id=model_id,
        max_length=200,
        temperature=0.5,
    )
    llm_chain = LLMChain(llm=llm, prompt=prompt, verbose=True)
    cl.user_session.set("llm_chain", llm_chain)

@cl.on_message
async def main(message: cl.Message):
    llm_chain = cl.user_session.get("llm_chain")
    res = await llm_chain.acall(message.content, callbacks=[cl.AsyncLangchainCallbackHandler()])
    await cl.Message(content=res["text"]).send()