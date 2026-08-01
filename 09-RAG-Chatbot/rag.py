import os
import pickle
import faiss
import numpy as np

from dotenv import load_dotenv
from pypdf import PdfReader
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

INDEX_PATH = "vectorstore/index.faiss"
CHUNKS_PATH = "vectorstore/chunks.pkl"


def extract_pdf_text(pdf_path):
    reader = PdfReader(pdf_path)

    pages = []

    for page in reader.pages:
        text = page.extract_text()

        if text:
            pages.append(text)

    return "\n".join(pages)


def create_chunks(text, chunk_size=1000, overlap=150):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])

        start += chunk_size - overlap

    return chunks


def get_embeddings(texts, task_type="RETRIEVAL_DOCUMENT"):

    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=texts,
        config=types.EmbedContentConfig(
            task_type=task_type,
            output_dimensionality=768
        )
    )

    return np.array(
        [embedding.values for embedding in response.embeddings],
        dtype="float32"
    )


def create_vector_store(pdf_path):

    print("Reading PDF...")

    text = extract_pdf_text(pdf_path)

    if not text.strip():
        raise ValueError("No readable text was found in the PDF.")

    print("Creating text chunks...")

    chunks = create_chunks(text)

    print("Creating Gemini embeddings...")

    embeddings = get_embeddings(
        chunks,
        task_type="RETRIEVAL_DOCUMENT"
    )

    # Normalize vectors for cosine similarity
    faiss.normalize_L2(embeddings)

    index = faiss.IndexFlatIP(embeddings.shape[1])
    index.add(embeddings)

    os.makedirs("vectorstore", exist_ok=True)

    faiss.write_index(index, INDEX_PATH)

    with open(CHUNKS_PATH, "wb") as file:
        pickle.dump(chunks, file)

    print(f"Created {len(chunks)} chunks.")
    print("Vector database created successfully!")


def retrieve(question, k=4):

    index = faiss.read_index(INDEX_PATH)

    with open(CHUNKS_PATH, "rb") as file:
        chunks = pickle.load(file)

    query_embedding = get_embeddings(
        [question],
        task_type="RETRIEVAL_QUERY"
    )

    faiss.normalize_L2(query_embedding)

    _, indices = index.search(query_embedding, k)

    retrieved_chunks = []

    for index_value in indices[0]:
        if index_value != -1:
            retrieved_chunks.append(chunks[index_value])

    return retrieved_chunks


def ask_question(question):

    retrieved_chunks = retrieve(question)

    context = "\n\n---\n\n".join(retrieved_chunks)

    prompt = f"""
You are a document question-answering assistant.

Answer the user's question using ONLY the document context provided below.

If the answer cannot be found in the context, say:
"I could not find that information in the document."

DOCUMENT CONTEXT:
{context}

USER QUESTION:
{question}

ANSWER:
"""

    response = client.models.generate_content(
     model="gemini-flash-latest",
     contents=prompt
    )

    return response.text