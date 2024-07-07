from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.chat.vector_stores.pinecone import vector_store

def create_embeddings_for_pdf(pdf_id: str, pdf_path: str):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    loader = PyPDFLoader(file_path=pdf_path)
    documents = loader.load_and_split(text_splitter)

    # for doc in documents:
    #     try:
    #         print(doc)
    #     except UnicodeEncodeError:
    #         print("UnicodeEncodeError")

    for doc in documents:
        doc.metadata = {
            "page": doc.metadata["page"],
            "text": doc.page_content,
            "pdf_id": pdf_id
        }

    vector_store.add_documents(documents)
