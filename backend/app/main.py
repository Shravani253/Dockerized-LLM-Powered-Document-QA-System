import os
import shutil
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .ingestion import ingest_document
from .faiss_store import create_faiss_index
from .retrieval import retrieve_context, build_context
from .llm import generate_answer


app = FastAPI(title="RAG FAISS API")


# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # change later for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


UPLOAD_DIR = "data"
os.makedirs(UPLOAD_DIR, exist_ok=True)


# -----------------------------
# Health check
# -----------------------------
@app.get("/")
async def root():
    return {"message": "RAG API running"}


# -----------------------------
# Upload & Index Document
# -----------------------------
@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    try:
        if not file.filename.endswith(".pdf"):
            raise HTTPException(status_code=400, detail="Only PDF files allowed")

        file_path = os.path.join(UPLOAD_DIR, file.filename)

        # Save uploaded file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Run ingestion pipeline
        chunks, embeddings = ingest_document(file_path)

        # Create FAISS index
        create_faiss_index(embeddings, chunks)

        return {"status": "Document indexed successfully", "chunks": len(chunks)}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -----------------------------
# Ask Question
# -----------------------------
@app.post("/ask")
async def ask_question(query: dict):
    try:
        user_query = query.get("query")

        if not user_query:
            raise HTTPException(status_code=400, detail="Query missing")

        print("User query:", user_query)

        chunks, scores = retrieve_context(user_query)
        print("Chunks retrieved:", len(chunks))

        context = build_context(chunks)
        print("Context length:", len(context))

        if not context.strip():
            return {"answer": "No relevant context found in document."}

        answer = generate_answer(user_query, context)

        return {
            "query": user_query,
            "answer": answer,
            "sources_found": len(chunks)
        }

    except Exception as e:
        print("\n🔥 FULL ERROR TRACEBACK:")
        traceback.print_exc()
        return {"error": str(e)}
