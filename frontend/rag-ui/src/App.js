import React, { useState } from "react";
import axios from "axios";

const API_BASE = "http://127.0.0.1:8000";

function App() {
  const [file, setFile] = useState(null);
  const [uploadStatus, setUploadStatus] = useState("");
  const [query, setQuery] = useState("");
  const [answer, setAnswer] = useState("");

  // -----------------------------
  // Upload PDF
  // -----------------------------
  const handleUpload = async () => {
    if (!file) {
      alert("Select a PDF first");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    setUploadStatus("Indexing document...");

    try {
      const res = await axios.post(`${API_BASE}/upload`, formData);
      setUploadStatus(res.data.status || "Indexed successfully");
    } catch (err) {
      setUploadStatus("Upload failed");
    }
  };

  // -----------------------------
  // Ask Question
  // -----------------------------
  const handleAsk = async () => {
    if (!query.trim()) return;

    setAnswer("Thinking...");

    try {
      const res = await axios.post(`${API_BASE}/ask`, {
        query: query,
      });

      setAnswer(res.data.answer);
    } catch (err) {
      setAnswer("Error fetching answer");
    }
  };

  return (
    <div style={{ maxWidth: 700, margin: "40px auto", fontFamily: "Arial" }}>
      <h1>📄 RAG Knowledge Assistant</h1>

      <div style={card}>
        <h3>Upload PDF</h3>
        <input type="file" accept=".pdf" onChange={(e) => setFile(e.target.files[0])} />
        <br /><br />
        <button onClick={handleUpload}>Upload</button>
        <p>{uploadStatus}</p>
      </div>

      <div style={card}>
        <h3>Ask Question</h3>
        <textarea
          rows="4"
          style={{ width: "100%" }}
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Ask something about the document..."
        />
        <br /><br />
        <button onClick={handleAsk}>Ask</button>
        <p><strong>Answer:</strong></p>
        <div style={answerBox}>{answer}</div>
      </div>
    </div>
  );
}

const card = {
  background: "#fff",
  padding: 20,
  marginBottom: 20,
  borderRadius: 10,
  boxShadow: "0 2px 10px rgba(0,0,0,0.1)"
};

const answerBox = {
  background: "#f4f4f4",
  padding: 10,
  borderRadius: 5
};

export default App;
