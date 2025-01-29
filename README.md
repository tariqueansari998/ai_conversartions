# AI Conversations

---
**AI Chatbot Development with LangChain & HuggingFace**

Build context-aware AI chatbots using Python, diving into RAG (Retrieval Augmented Generation) and AI Agents. We'll explore how to create conversational AI that maintains context and conversation history using LangChain for LLM applications and HuggingFace for NLP models.

# Getting started

---
## Pre-requisites
* Python 3.10 or above
* Poetry

## Installation

---
### Python
* Download & install python from [python website](https://www.python.org/downloads/)
* Select _Add to path_ option while installation
### Poetry
* https://python-poetry.org/docs/#installation

## Run the program
### Install dependencies required by project from [pyproject.toml](pyproject.toml)
```commandline
poetry install
```
### Refresh poetry file
```commandline
poetry lock --no-update
```
### Run a program
```commandline
poetry run chainlit run .\ai_conversation.py -w --port 8080
poetry run python .\ai_rag_conversation.py
```

## Contents
---
1. Simple chatbot using chainlit [ai_conversation.py](ai_conversation.py)
2. Explore RAG [ai_rag_conversation.py](ai_rag_conversation.py)
3. Build a chatbot using AI Agents



