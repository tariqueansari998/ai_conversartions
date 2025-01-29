from dotenv import load_dotenv
from resume_vertor_store import load_resume_vector_store,query_resume_vector_store

load_dotenv()
load_resume_vector_store()
query_resume_vector_store(query="Who is tarique ansari")