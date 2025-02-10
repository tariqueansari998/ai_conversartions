### 🔥 Learn AI concepts in my blog [Building AI Applications: A Beginner's Guide to RAG, Agents, and Tools](https://medium.com/@tariqueansari998/building-ai-applications-a-beginners-guide-to-rag-agents-and-tools-19788848bd4f) 

## Table of Contents
- [About](#-about)
- [Content](#-content)
- [How to Build](#-how-to-build)
- [Documentation](#-documentation)

## 🚀 About

Learning new technology can be intimidating specially with all the complexities of the topic randomly being served on internet.

The goal of this repository is to help build AI applications starting with simple chatbots and gradually adding complexities along the way.

## 📑 Content

### Beginner
1. Simple chatbot using **Chainlit**. [**Refer: ai_conversation.py**](beginner/ai_conversation.py)
2. Explore **RAG** by creating vector store using custom knowledge base. Use this vector store in chat application. [**Refer: ai_rag_conversation.py**](beginner/ai_rag_conversation.py)
3. Give more power to AI applications by creating **Agents** and giving it **Tools** to produce desired result. [**Refer: ai_agent_conversation.py**](beginner/ai_agent_conversation.py)

## 📝 How to run applications

### Pre-requisites
* Python [Installation Guide](https://www.python.org/downloads/)
* Poetry [Installation Guide](https://python-poetry.org/docs/#installation)
* Docker

### Using LLM
LLM can be used one of the following ways:
1. APIs from one of the platforms like [HuggingFace](https://huggingface.co/models), [Anthropic](https://console.anthropic.com/dashboard), [OpenAI](https://platform.openai.com/docs/api-reference/introduction) etc

OR
2. Run LLM locally using Docker
```shell
# Open a terminal (Command Prompt or PowerShell for Windows, Terminal for macOS or Linux)
# Pull docker image for Ollama. Check for latest version https://hub.docker.com/r/ollama/ollama
docker pull ollama/ollama:0.3.6

#Run Ollama server in detach mode with Docker
# without GPU
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama:0.3.6 
# with GPU
docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama:0.3.6


```



## 📚 Documentation

### Getting Started
Explore the [Getting Started Guide]().

