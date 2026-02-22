from typing import List
import numpy as np
from sentence_transformers import SentenceTransformer

# Load model once (global, efficient)
model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embeddings(texts: List[str]) -> np.ndarray:
    """
    Generate embeddings for a list of text chunks.
    
    Args:
        texts: List of text strings
    
    Returns:
        numpy array of embeddings (float32)
    """
    embeddings = model.encode(
        texts,
        convert_to_numpy=True,
        show_progress_bar=True
    )

    # FAISS requires float32
    return embeddings.astype("float32")
