from sentence_transformers import SentenceTransformer

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Sample documents
docs = [
    "Machine learning is used in artificial intelligence.",
    "Vector databases store embeddings for similarity search.",
    "Retrieval augmented generation improves AI responses."
]

# Convert to embeddings
embeddings = model.encode(docs)

# Store locally (simulate DB)
data_store = []

for doc, emb in zip(docs, embeddings):
    data_store.append({
        "text": doc,
        "vector": emb
    })

print("✅ Data processed and stored successfully!")