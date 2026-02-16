from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from llm.llm import get_embeddings

def build_vectorstore(pdf_path="data/sample.pdf", vectorstore_path="vectorstore/faiss_index"):
    # Load the PDF document
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # Split the document into smaller chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)

    # Get the embedding model
    embedding_model = get_embeddings()

    # Create the FAISS vector store
    vectorstore = FAISS.from_documents(texts, embedding_model)

    # Save the vector store to disk
    vectorstore.save_local(vectorstore_path)

    return vectorstore