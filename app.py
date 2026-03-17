from fastapi import FastAPI
from sentence_transformers import SentenceTransformer
import numpy as np

app = FastAPI()

# ✅ NEW ROUTE (fixes 404)
@app.get("/")
def home():
    return {"message": "API is running successfully 🚀"}

model = SentenceTransformer("all-MiniLM-L6-v2")

docs = [
    "Machine learning is used in artificial intelligence.",
    "Vector databases store embeddings for similarity search.",
    "Retrieval augmented generation improves AI responses."
]

embeddings = model.encode(docs)

@app.get("/search")
def search(query: str):
    query_vector = model.encode(query)
    similarities = np.dot(embeddings, query_vector)
    best_index = np.argmax(similarities)

    return {
        "query": query,
        "result": docs[best_index]
    }