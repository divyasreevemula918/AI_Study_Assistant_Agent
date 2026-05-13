# import streamlit as st
# from modules.vector_store import create_vector_store
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from PyPDF2 import PdfReader

# st.title("AI Agent Assistant")

# uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

# if uploaded_file is not None:

#     # Step 1: Read PDF
#     pdf_reader = PdfReader(uploaded_file)
#     text = ""

#     for page in pdf_reader.pages:
#         page_text = page.extract_text()
#         if page_text:
#             text += page_text

#     # Debug: show extracted text length
#     st.write("Extracted text length:", len(text))

#     if not text.strip():
#         st.error("No readable text found in this PDF (it may be scanned or image-based).")
#         st.stop()

#     # Step 2: Split text into chunks
#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size=1000,
#         chunk_overlap=200
#     )

#     chunks = text_splitter.split_text(text)

#     st.write("Number of chunks:", len(chunks))

#     if not chunks:
#         st.error("Text splitting failed. No chunks generated.")
#         st.stop()

#     # Step 3: Create vector store safely
#     try:
#         vector_store = create_vector_store(chunks)
#         st.success("Vector store created successfully!")
#     except Exception as e:
#         st.error(f"Error creating vector store: {str(e)}")
import streamlit as st
from modules.vector_store import create_vector_store
from langchain_text_splitters import RecursiveCharacterTextSplitter
from PyPDF2 import PdfReader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# =========================================
# Load Environment Variables
# =========================================

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# =========================================
# Streamlit UI
# =========================================

st.set_page_config(
    page_title="AI Study Assistant Agent",
    page_icon="📚",
    layout="wide"
)

st.title("📚 AI Study Assistant Agent")

st.write(
    "Upload a PDF and interact with it using AI 🤖"
)

# =========================================
# Upload PDF
# =========================================

uploaded_file = st.file_uploader(
    "Upload your PDF",
    type="pdf"
)

# =========================================
# Process PDF
# =========================================

if uploaded_file is not None:

    # Step 1: Read PDF
    pdf_reader = PdfReader(uploaded_file)

    text = ""

    for page in pdf_reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text

    # Debug
    st.write("📄 Extracted text length:", len(text))

    # Empty text check
    if not text.strip():

        st.error(
            "No readable text found in this PDF."
        )

        st.stop()

    # =========================================
    # Step 2: Split Text into Chunks
    # =========================================

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_text(text)

    st.write("✂ Number of chunks:", len(chunks))

    if not chunks:

        st.error(
            "Text splitting failed."
        )

        st.stop()

    # =========================================
    # Step 3: Create Vector Store
    # =========================================

    try:

        vector_store = create_vector_store(chunks)

        st.success(
            "✅ Vector store created successfully!"
        )

    except Exception as e:

        st.error(
            f"Error creating vector store: {str(e)}"
        )

        st.stop()

    # =========================================
    # Step 4: Gemini Model
    # =========================================

    model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=st.secrets["GOOGLE_API_KEY"],
    temperature=0.3
)

    # =========================================
    # Sidebar Features
    # =========================================

    st.sidebar.title("📌 AI Features")

    option = st.sidebar.radio(
        "Choose Feature",
        [
            "Ask Questions",
            "Generate Summary",
            "Generate Quiz"
        ]
    )

    # =========================================
    # 1. Ask Questions
    # =========================================

    if option == "Ask Questions":

        st.subheader("💬 Ask Questions from PDF")

        user_question = st.text_input(
            "Enter your question"
        )

        if st.button("Get Answer"):

            docs = vector_store.similarity_search(
                user_question,
                k=3
            )

            context = ""

            for doc in docs:
                context += doc.page_content + "\n"

            prompt = f"""
            Answer the question based on the context below.

            Context:
            {context}

            Question:
            {user_question}

            Give a clear and detailed answer.
            """

            response = model.invoke(prompt)

            st.success("✅ Answer Generated")

            st.write(response.content)

    # =========================================
    # 2. Generate Summary
    # =========================================

    elif option == "Generate Summary":

        st.subheader("📝 PDF Summary")

        if st.button("Generate Summary"):

            summary_prompt = f"""
            Summarize the following content
            in simple understandable points.

            Content:
            {text[:10000]}
            """

            response = model.invoke(
                summary_prompt
            )

            st.success("✅ Summary Generated")

            st.write(response.content)

    # =========================================
    # 3. Generate Quiz
    # =========================================

    elif option == "Generate Quiz":

        st.subheader("🧠 Quiz Generator")

        if st.button("Generate Quiz"):

            quiz_prompt = f"""
            Generate 10 multiple choice questions
            from the following content.

            Also provide correct answers.

            Content:
            {text[:10000]}
            """

            response = model.invoke(
                quiz_prompt
            )

            st.success("✅ Quiz Generated")

            st.write(response.content)