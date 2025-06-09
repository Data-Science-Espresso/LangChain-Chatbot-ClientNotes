# chatbot_core.py: Core logic for chatbot based on OneNote notes in a txt file

from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOllama
from langchain.chains import ConversationalRetrievalChain

def build_qa_chain(txt_path="notes.txt"):
    loader = TextLoader(txt_path, encoding="utf-8")  # Loads a plain text file
    documents = loader.load()

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)  # Split into chunks
    docs = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.from_documents(docs, embeddings)
    retriever = db.as_retriever()
    
    llm = ChatOllama(model="mistral")  # You can change this to another model (e.g., llama3)
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    return qa_chain
