import faiss
import os
import pickle
import numpy as np
from typing import List, Tuple


INDEX_PATH = "faiss_index/index.bin"
CHUNKS_PATH = "faiss_index/chunks.pkl"


# -----------------------------
# 1️⃣ Create & Save Index
# -----------------------------
def create_faiss_index(embeddings: np.ndarray, chunks: List[str]):
    """
    Create FAISS index and save it with chunk metadata.
    """

    os.makedirs("faiss_index", exist_ok=True)

    dimension = embeddings.shape[1]

    # Using L2 distance index
    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    # Save index
    faiss.write_index(index, INDEX_PATH)

    # Save chunk text separately
    with open(CHUNKS_PATH, "wb") as f:
        pickle.dump(chunks, f)

    print("FAISS index created and saved.")


# -----------------------------
# 2️⃣ Load Index
# -----------------------------
def load_faiss_index():
    if not os.path.exists(INDEX_PATH):
        raise FileNotFoundError("FAISS index not found.")

    index = faiss.read_index(INDEX_PATH)

    with open(CHUNKS_PATH, "rb") as f:
        chunks = pickle.load(f)

    return index, chunks


# -----------------------------
# 3️⃣ Search Index
# -----------------------------
def search_index(query_embedding: np.ndarray, top_k: int = 3) -> Tuple[List[str], List[float]]:
    """
    Search FAISS index and return top_k relevant chunks.
    """

    index, chunks = load_faiss_index()

    distances, indices = index.search(query_embedding, top_k)

    results = []
    scores = []

    for idx, dist in zip(indices[0], distances[0]):
        results.append(chunks[idx])
        scores.append(float(dist))

    return results, scores
