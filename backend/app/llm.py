import os
import requests

OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://localhost:11434/api/generate"
)
MODEL_NAME = "phi4:latest"  



def generate_answer(query: str, context: str) -> str:
    """
    Generate grounded answer using Phi-4 via Ollama
    """

    prompt = f"""
You are a helpful AI assistant.
Answer ONLY using the provided context.
If the answer is not in the context, say: "Not found in document."

Context:
{context}

Question:
{query}
"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            },
            timeout=300
        )

        if response.status_code != 200:
            return f"Ollama error: {response.text}"

        data = response.json()
        return data.get("response", "").strip()

    except Exception as e:
        return f"LLM Error: {str(e)}"
 