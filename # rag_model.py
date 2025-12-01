# rag_model.py

# Import necessary modules
from langchain.document_loaders import TextLoader, PyPDFLoader  # Use PyPDFLoader if it's a PDF
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Step 2: Load the document
loader = TextLoader('/Users/alireza/University Courses/NLP/Rag-Model', encoding='utf-8')  
documents = loader.load()

# Print to verify (optional)
print(f"Loaded {len(documents)} document(s). First 100 chars: {documents[0].page_content[:100]}")