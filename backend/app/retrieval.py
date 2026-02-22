from typing import List, Tuple
import numpy as np

from .embeddings import get_embeddings
from .faiss_store import search_index


# -----------------------------
# Retrieve relevant chunks
# -----------------------------
def retrieve_context(query: str, top_k: int = 2) -> Tuple[List[str], List[float]]:
    """
    Convert query -> embedding -> FAISS search -> return top chunks.

    Args:
        query: user question
        top_k: number of relevant chunks to retrieve

    Returns:
        (chunks, scores)
    """

    if not query.strip():
        raise ValueError("Query cannot be empty")

    # Generate embedding for query
    query_embedding = get_embeddings([query])

    # FAISS search
    chunks, scores = search_index(query_embedding, top_k=top_k)

    return chunks, scores


# -----------------------------
# Build context string for LLM
# -----------------------------
def build_context(chunks: List[str]) -> str:
    """
    Combine retrieved chunks into single context string.
    """

    context = "\n\n".join(chunks)
    return context
