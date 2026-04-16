# 📄 AI PDF Chatbot (RAG System)

An intelligent **AI-powered PDF chatbot** that allows users to upload PDF documents and ask questions about their content.
The system uses **Retrieval-Augmented Generation (RAG)** with modern LLMs to provide accurate answers based on document context.

---

# 🚀 Features

* 📂 **Multiple PDF Upload**
* 💬 **ChatGPT-style conversational interface**
* 🧠 **Conversation Memory**
* ⚡ **Fast Semantic Search using Vector Database**
* 📚 **Source Citations (Page Numbers)**
* 🔍 **Context-aware responses using RAG**
* 🌐 **Groq LLM integration (LLaMA-3.3-70B)**
* 🎯 **Accurate answers from document content**
* 🖥️ **Beautiful Streamlit UI**

---

# 🧠 Architecture

User Question →
Retriever (Vector Search) →
Relevant PDF Chunks →
LLM (Groq LLaMA Model) →
Context-Aware Answer

The system follows the **Retrieval-Augmented Generation (RAG)** architecture used in modern AI assistants.

---

# 🛠️ Tech Stack

**Frontend**

* Streamlit

**Backend / AI**

* LangChain
* Groq LLM API
* HuggingFace Embeddings

**Vector Database**

* ChromaDB

**Document Processing**

* PyPDF
* Recursive Text Splitting

---

# 📂 Project Structure

```
AI_PDF_Chatbot
│
├── app.py
├── requirements.txt
├── README.md
├── .env
└── vector_db (auto created)
```

---

# ⚙️ Installation

Clone the repository:

```
git clone https://github.com/yourusername/ai-pdf-chatbot.git
cd ai-pdf-chatbot
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_groq_api_key
HF_TOKEN=your_huggingface_token
```

---

# ▶ Running the Application

Start the Streamlit app:

```
streamlit run app.py
```

Then open your browser:

```
http://localhost:8501
```

---

# 📚 How It Works

1. User uploads PDF documents
2. Text is extracted and split into chunks
3. Embeddings are generated using HuggingFace models
4. Chunks are stored in a **Chroma Vector Database**
5. When a user asks a question:

   * Relevant chunks are retrieved
   * LLM generates an answer using context
6. The chatbot returns the answer with **source references**

---

# 📊 Example Use Cases

* 📖 Research Paper Assistant
* 📚 Study Helper
* 📑 Legal Document Analysis
* 🏢 Business Report Q&A
* 📄 Contract Understanding

---

# 🔮 Future Improvements

* FAISS vector database for faster retrieval
* Hybrid search (BM25 + vector search)
* Reranker models for improved accuracy
* PDF text highlighting
* Multi-document reasoning
* LangGraph AI agents

---

# 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss the changes.

---

# 📜 License

MIT License

---

# 👨‍💻 Author

**Ikbal Singh**

AI / Machine Learning Engineer

LinkedIn: https://www.linkedin.com/in/ikbal-rajvansh

---
