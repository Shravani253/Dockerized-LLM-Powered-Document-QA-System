Dockerized LLM-Powered Document QA System

A containerized Retrieval-Augmented Generation (RAG) system that enables users to upload PDF documents and ask natural language questions. The system retrieves relevant document context using vector search (FAISS) and generates grounded answers using a locally hosted Large Language Model via Ollama.

🚀 Overview

This project implements an end-to-end RAG pipeline including:

PDF ingestion

Text chunking

Embedding generation

Vector similarity search using FAISS

Context retrieval

LLM-based answer generation

Dockerized backend deployment

React-based frontend interface

The system ensures responses are grounded in uploaded documents rather than relying solely on the LLM’s pre-trained knowledge.

🏗️ Architecture

User → React Frontend → FastAPI Backend →
PDF Ingestion → Embeddings → FAISS Vector Store →
Top-K Retrieval → Local LLM (Ollama) → Generated Answer

🛠️ Tech Stack
Backend

FastAPI (async API framework)

FAISS (vector similarity search)

Sentence Transformers (all-MiniLM-L6-v2 for embeddings)

Ollama (local LLM inference)

Docker & Docker Compose (containerization)

Frontend

React.js

Fetch API for backend communication

Models Used

Embedding Model:

sentence-transformers/all-MiniLM-L6-v2

Used to convert text chunks into dense vector embeddings.

LLM Model (via Ollama):

phi3 (or any locally available Ollama model)

Used for grounded response generation.

You can switch models by changing the model name in the backend configuration.

📂 Project Structure
Dockerized-LLM-Powered-Document-QA-System/
│
├── backend/
│   ├── app/
│   │   ├── ingestion.py
│   │   ├── embeddings.py
│   │   ├── faiss_store.py
│   │   ├── retrieval.py
│   │   ├── llm.py
│   │   ├── main.py
│   │   └── utils.py
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── requirements.txt
│
├── frontend/
│   └── rag-ui/
│
└── README.md
⚙️ How It Works
1️⃣ Document Upload

User uploads a PDF.

Text is extracted and split into manageable chunks.

2️⃣ Embedding Generation

Each chunk is converted into vector embeddings using all-MiniLM-L6-v2.

3️⃣ Vector Storage

Embeddings are stored in FAISS for fast similarity search.

4️⃣ Question Answering

User asks a question.

Question is embedded.

Top-k similar chunks are retrieved.

Retrieved context is sent to the local LLM.

LLM generates a grounded answer.

🐳 Running with Docker (Recommended)
Step 1: Start Backend
cd backend
docker compose up --build

Backend will run at:

http://localhost:8000

Swagger Docs:

http://localhost:8000/docs
Step 2: Start Frontend

In a separate terminal:

cd frontend/rag-ui
npm install
npm start

Frontend runs at:

http://localhost:3000
🖥️ Running Without Docker (Optional)
Backend
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
Frontend
cd frontend/rag-ui
npm install
npm start
📌 Requirements

Python 3.10+

Node.js

Docker Desktop

Ollama installed locally

Install Ollama:
https://ollama.com

Pull model:

ollama pull phi4:latest

Start Ollama:

ollama run phi4:latest


✨ Key Features

Full Retrieval-Augmented Generation pipeline

Vector-based semantic search

Local LLM inference (no external API dependency)

Dockerized backend deployment

Async FastAPI architecture

Interactive React frontend

🎯 Use Cases

Internal document QA systems

Enterprise knowledge assistants

Resume document analysis tools

Local AI assistants without cloud dependency

📈 Future Improvements

Streaming responses

Multi-document support

Persistent vector database

Authentication & role-based access

Cloud deployment (AWS/GCP)

👩‍💻 Author

Shravani Vanalkar
Full-stack AI & Backend Developer