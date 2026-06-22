# 📄 AI-Powered Chat PDF Assistant Using RAG

An AI-powered application that lets you upload PDF documents and ask questions about their content using Retrieval-Augmented Generation (RAG) technology.

---

## 🚀 Live Demo
> Coming soon after deployment

---

## ✨ Features

- 📄 Upload single or multiple PDF files
- 💬 Ask natural language questions about your PDFs
- 🤖 AI-powered answers using GPT-4o-mini
- 🔍 Smart context retrieval using FAISS vector search
- ⚡ Fast and accurate responses using RAG architecture

---

## 🧠 Tech Stack

| Technology | Purpose |
|------------|---------|
| **Streamlit** | Frontend UI |
| **LangChain** | RAG pipeline & LLM chaining |
| **OpenAI GPT-4o-mini** | Language model for answers |
| **FAISS** | Vector store for semantic search |
| **HuggingFace Embeddings** | Text embeddings (`all-MiniLM-L6-v2`) |
| **PyPDF** | PDF text extraction |
| **Python 3.11+** | Core language |

---

## 🏗️ Project Structure

```
AI-Powered-Chat-PDF-Assistant-Using-RAG/
│
├── streamlit_app.py          # Main Streamlit application
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore rules
├── render.yaml              # Render deployment config
│
└── utils/
    ├── pdf_loader.py        # PDF text extraction
    ├── text_splitter.py     # Text chunking
    ├── embeddings.py        # HuggingFace embeddings
    ├── faiss.py             # FAISS vector store
    └── qa_chain.py          # QA retrieval chain
```

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.11+
- OpenAI API Key → [Get one here](https://platform.openai.com/api-keys)

### 1. Clone the repository
```bash
git clone https://github.com/muskanjasoriaa/AI-Powered-Chat-PDF-Assistant-Using-RAG.git
cd AI-Powered-Chat-PDF-Assistant-Using-RAG
```

### 2. Create a virtual environment
```bash
python -m venv venv
```

Activate it:
- **Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```
- **Mac/Linux:**
```bash
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set your OpenAI API Key

**Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY="sk-your-api-key-here"
```

**Mac/Linux:**
```bash
export OPENAI_API_KEY="sk-your-api-key-here"
```

### 5. Run the app
```bash
streamlit run streamlit_app.py
```

Open your browser at **http://localhost:8501** 🎉

---

## 📦 Requirements

```
streamlit
langchain
langchain-community
langchain-openai
pypdf
faiss-cpu
sentence-transformers
huggingface_hub
```

---

## 🔒 Environment Variables

| Variable | Description |
|----------|-------------|
| `OPENAI_API_KEY` | Your OpenAI API key (required) |

---

## 🤖 How It Works

```
1. Upload PDF
      ↓
2. Extract text (PyPDF)
      ↓
3. Split into chunks (LangChain Text Splitter)
      ↓
4. Generate embeddings (HuggingFace)
      ↓
5. Store in FAISS vector store
      ↓
6. User asks a question
      ↓
7. Retrieve relevant chunks (FAISS similarity search)
      ↓
8. Generate answer (GPT-4o-mini)
      ↓
9. Display answer to user ✅
```

---

## 👩‍💻 Author

**Muskan Jasoria**
- GitHub: [@muskanjasoriaa](https://github.com/muskanjasoriaa)

---

## 📄 License

This project is licensed under the MIT License.
