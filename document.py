from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

# Initialize FAISS
vector_store = FAISS.load_local("health_guidelines_index", OpenAIEmbeddings())
# Adding fitness tips
documents = [
    {"content": "Walk at least 10,000 steps daily for a healthy heart.", "category": "steps"},
    {"content": "Sleep at least 7 hours a day for optimal health.", "category": "sleep"},
]
vector_store.add_documents(documents)

