import os
from typing import List
from pypdf import PdfReader

from .embeddings import get_embeddings


# -----------------------------
# 1. Extract text from PDF
# -----------------------------
def extract_text_from_pdf(file_path: str) -> str:
    text = ""
    reader = PdfReader(file_path)

    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content + "\n"

    return text


# -----------------------------
# 2. Chunk text into small parts
# -----------------------------
def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    words = text.split()
    chunks = []

    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = words[start:end]
        chunks.append(" ".join(chunk))
        start += chunk_size - overlap

    return chunks


# -----------------------------
# 3. Full ingestion pipeline
# -----------------------------
def ingest_document(file_path: str):
    """
    Full pipeline:
    PDF -> Text -> Chunks -> Embeddings
    Returns:
        chunks: List[str]
        embeddings: numpy array
    """

    print("Extracting text from PDF...")
    text = extract_text_from_pdf(file_path)

    if not text.strip():
        raise ValueError("No text found in document")

    print("Chunking text...")
    chunks = chunk_text(text)

    print(f"Generated {len(chunks)} chunks")

    print("Generating embeddings...")
    embeddings = get_embeddings(chunks)

    return chunks, embeddings
