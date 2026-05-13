from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

def ask_question(question):

    # Embedding model
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Load FAISS DB
    db = FAISS.load_local(
        "db/faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    # Search similar docs
    docs = db.similarity_search(question)

    # Combine document text
    context = "\n\n".join([doc.page_content for doc in docs])

    # Gemini model
    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.3,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    # Prompt
    prompt = f"""
    Answer the question based only on the context below.

    Context:
    {context}

    Question:
    {question}
    """

    # Generate response
    response = model.invoke(prompt)

    return response.content