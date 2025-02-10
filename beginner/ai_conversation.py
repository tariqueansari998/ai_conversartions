import chainlit as cl
from dotenv import load_dotenv
from langchain_community.llms import HuggingFaceEndpoint
from langchain import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts.prompt import PromptTemplate

load_dotenv()

template = """You are an AI assistant that provides helpful responses to user queries

Current conversation:
{history}
Human: {input}
AI:"""

prompt = PromptTemplate(input_variables=["history", "input"], template=template)

@cl.on_chat_start
def main():
    model_id = "Qwen/Qwen2.5-Coder-32B-Instruct"
    llm = HuggingFaceEndpoint(
        repo_id=model_id,
        max_length=2000,
        temperature=0.5,
    )
    llm_chain = ConversationChain(
        llm=llm,
        prompt=prompt,
        verbose=True,
        memory=ConversationBufferMemory()
    )
    cl.user_session.set("llm_chain", llm_chain)

@cl.on_message
async def main(message: cl.Message):
    llm_chain = cl.user_session.get("llm_chain")
    res = await llm_chain.acall(message.content, callbacks=[cl.AsyncLangchainCallbackHandler()])
    print(f"Response: {res}")
    await cl.Message(content=res["response"]).send()