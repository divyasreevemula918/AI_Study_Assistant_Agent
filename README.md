# 📚 AI Study Assistant Agent 🤖

An AI-powered Study Assistant that can analyze PDF documents, answer questions, generate summaries, and create quizzes using Gemini AI, HuggingFace Embeddings, FAISS, and Streamlit.

---

# 📂 Complete Project Structure

```text
AI_Study_Assistant_Agent/
│
├── app.py
├── requirements.txt
├── runtime.txt
├── .gitignore
├── README.md
├── .env
│
├── modules/
│   └── vector_store.py
│
├── data/
│
└── db/
```

---

# 🚀 Features

- Upload PDF documents
- Extract text from PDFs
- Analyze PDF content using AI
- Ask questions from uploaded PDFs
- Generate summaries automatically
- Generate MCQ quizzes with answers
- Semantic search using vector embeddings
- Retrieval-Augmented Generation (RAG) pipeline
- Interactive Streamlit UI

---

# 🛠 Tech Stack

- Python
- Streamlit
- Gemini AI
- HuggingFace Embeddings
- FAISS
- PyPDF2
- LangChain

---

# ⚙️ Installation

## Clone Repository

```bash
git clone <your-github-repository-link>
cd AI_Study_Assistant_Agent
```

## Create Virtual Environment

```bash
py -3.11 -m venv venv
```

## Activate Virtual Environment

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Setup API Key

Create `.env`

```env
GOOGLE_API_KEY=your_api_key_here
```

---

# ▶️ Run Project

```bash
streamlit run app.py
```

---

# 📦 requirements.txt

```txt
streamlit==1.45.1
langchain==0.3.25
langchain-community==0.3.24
langchain-google-genai==2.1.4
langchain-text-splitters==0.3.8
google-generativeai==0.8.5
faiss-cpu==1.7.4
sentence-transformers==4.1.0
PyPDF2==3.0.1
python-dotenv==1.1.0
pydantic==2.11.4
```

---

# 📝 runtime.txt

```txt
python-3.11
```

---

# 📝 .gitignore

```gitignore
__pycache__/
*.pyc
venv/
.env
.vscode/
db/
data/
.cache/
```

---

# 🧠 Workflow

```text
PDF Upload
   ↓
Text Extraction
   ↓
Chunking
   ↓
HuggingFace Embeddings
   ↓
FAISS Vector Database
   ↓
Similarity Search
   ↓
Gemini AI Response
```

---

# 📌 Future Improvements

- Voice assistant
- OCR for scanned PDFs
- Multi-PDF support
- Flashcards generation
- Chat history memory
- AWS deployment
- Multi-agent workflows

---

# 👨‍💻 Author

Developed using Python, Streamlit, Gemini AI, HuggingFace Embeddings, and FAISS.
