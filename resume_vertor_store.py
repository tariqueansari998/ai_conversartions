"""
steps
1. Define source data directory & persistent db directory
2. Check if vector store already exists, if not
3. Load the file data using langchain loaders(TextLoader in our case)
4. Define embedding model
5. Create vector store using Chroma from langchain_community.vectorstores
"""
import os
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

current_directory = os.path.dirname(os.path.abspath(__file__))
datasource_directory = os.path.join(current_directory, "resume")
db_directory = os.path.join(datasource_directory, "db", "chroma_resume_db")

hf_embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


def load_resume_vector_store():
    print(f"Current directory {current_directory} \n datasource_directory {datasource_directory} \n db_directory {db_directory}")

    if not os.path.exists(db_directory):
        print("Initializing vector store")

        if not os.path.exists(datasource_directory):
            print(f"No datasource directory named {datasource_directory}")

        resumes = [f for f in os.listdir(datasource_directory) if f.endswith('.txt')]

        documents = []
        for resume_file in resumes:
            loader = TextLoader(os.path.join(datasource_directory, resume_file))
            resume_docs = loader.load()
            for doc in resume_docs:
                # Add metadata to each document indicating its source
                doc.metadata = {'source': resume_file}
                documents.append(doc)

        print(f"Documents: {documents}")

        # split the document into chunks
        text_splitter = CharacterTextSplitter(chunk_overlap=0, chunk_size=100)
        docs = text_splitter.split_documents(documents)

        # Display information about the split documents
        print("\n--- Document Chunks Information ---")
        print(f"Number of document chunks: {len(docs)}")

        db = Chroma.from_documents(docs, hf_embedding_model, persist_directory=db_directory,
                                   collection_metadata={"hnsw:space": "cosine"})
        print("\n--- Finished creating and persisting vector store ---")
    else:
        print("Vector store already exists")


def query_resume_vector_store(query):
    print(f"Current directory {current_directory} \n db_directory {db_directory} \n {query}")

    # Load the existing vector store with the same embedding function with which the vector store was created
    db = Chroma(persist_directory=db_directory,embedding_function=hf_embedding_model,
                collection_metadata={"hnsw:space": "cosine"})

    retriever = db.as_retriever(search_type="similarity_score_threshold",
                                search_kwargs={"k": 3, "score_threshold": 0.1})

    relevant_docs = retriever.invoke(query)

    # Display the relevant results with metadata
    print("\n--- Relevant Documents ---")
    for i, doc in enumerate(relevant_docs, 1):
        print(f"Document {i}:\n{doc.page_content}\n")
        print(f"Source : {doc.metadata['source']}\n")