# 📄 RAG Document Chatbot

An end-to-end **Retrieval-Augmented Generation (RAG) chatbot** that allows users to upload PDF documents and ask questions based specifically on the document's content.

The system combines **Gemini**, **FAISS vector search**, and text embeddings to retrieve relevant document context before generating an answer.

---

## 🎯 Objective

The objective of this project is to build a document question-answering system using Retrieval-Augmented Generation.

Instead of relying only on an LLM's existing knowledge, the chatbot retrieves relevant information from an uploaded PDF and provides that information to the language model as context.

---

## ✨ Features

- Upload PDF documents
- Extract text automatically
- Split documents into overlapping chunks
- Generate semantic embeddings
- Store embeddings in a FAISS vector database
- Retrieve relevant document sections
- Generate context-aware answers using Gemini
- Reject questions whose answers are not available in the document
- Simple Flask-based web interface

---

## 🧠 RAG Architecture

```text
PDF Document
     │
     ▼
Text Extraction
     │
     ▼
Text Chunking
     │
     ▼
Gemini Embeddings
     │
     ▼
FAISS Vector Database
     │
     │
     ├──────── User Question
     │               │
     │               ▼
     │        Query Embedding
     │               │
     ▼               ▼
   Semantic Similarity Search
             │
             ▼
      Relevant Chunks
             │
             ▼
         Gemini LLM
             │
             ▼
      Grounded Answer
```

---

## 🛠️ Technologies Used

- Python
- Flask
- Google Gemini API
- Gemini Embeddings
- FAISS
- NumPy
- PyPDF
- HTML
- CSS

---

## 🔍 How It Works

### 1. Document Processing

The uploaded PDF is processed using PyPDF and its text is extracted.

### 2. Text Chunking

The extracted text is divided into smaller overlapping chunks.

### 3. Embeddings

Each text chunk is converted into a numerical embedding using the Gemini Embedding model.

### 4. Vector Storage

The embeddings are stored in a FAISS vector index.

### 5. Retrieval

When the user asks a question, the question is embedded and compared with the stored document vectors.

### 6. Generation

The most relevant document chunks are supplied to Gemini along with the user's question.

Gemini then generates an answer grounded in the retrieved document context.

---

## 📂 Project Structure

```text
09-RAG-Chatbot/
│
├── data/
│   └── sample.pdf
│
├── templates/
│   └── index.html
│
├── static/
│
├── vectorstore/
│   ├── index.faiss
│   └── chunks.pkl
│
├── screenshots/
│   ├── pdf_uploaded.png
│   ├── rag_answer.png
│   └── grounded_response.png
│
├── app.py
├── rag.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository and navigate to this project.

Create a virtual environment:

```bash
python3.11 -m venv rag_env
source rag_env/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Gemini API Key

Create a `.env` file:

```text
GOOGLE_API_KEY=your_api_key_here
```

The `.env` file is excluded from Git using `.gitignore`.

Never commit API credentials to the repository.

---

## ▶️ Run the Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

Upload a PDF, process the document, and ask questions about its contents.

---

## 💬 Example Questions

For the included AI/ML sample document:

```text
What is Retrieval-Augmented Generation?

How are embeddings used in a RAG system?

What are the benefits of RAG?
```

---

## 📊 Key Concepts Demonstrated

- Generative AI
- Large Language Models
- Retrieval-Augmented Generation
- Semantic Search
- Text Embeddings
- Vector Databases
- Cosine Similarity
- Prompt Grounding
- Document Question Answering

---

## 🚀 Future Improvements

- Support multiple PDF documents
- Add conversational chat history
- Display retrieved sources/pages
- Support DOCX and TXT documents
- Add user authentication
- Add streaming LLM responses
- Deploy the chatbot to a cloud platform

---

## 👩‍💻 Author

**Khushie Brahma**
