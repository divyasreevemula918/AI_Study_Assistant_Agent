from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def create_vector_store(chunks):

    # Check if chunks are empty
    if not chunks or len(chunks) == 0:
        raise ValueError("No text chunks found. PDF may be empty.")

    # Create embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Create FAISS vector store
    vector_store = FAISS.from_texts(
        texts=chunks,
        embedding=embeddings
    )

    # Save vector store
    vector_store.save_local("faiss_index")

    return vector_store