# AI Conversations

---

In this repository we will explore AI libraries & concepts like RAG & AI Agents by building our own AI chatbots using Python, LangChain & HuggingFace

LangChain is an open source framework for building applications based on large language models (LLMs). It provides standardized interface for chaining together different components like document loaders, text splitters, embeddings, vector stores, and prompting mechanisms.
Hugging Face is a company and community platform that provides state-of-the-art open-source machine learning models and tools for natural language processing and other AI tasks.

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

## Contents
---
1. Simple chatbot [ai_conversation.py](ai_conversation.py)
2. Build a chatbot RAG
3. Build a chatbot using AI Agents

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
```