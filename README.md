# LangChain App – Your Local LLM Chat Assistant for your Notes
This is a simple LangChain-based Streamlit app that connects to local or cloud LLMs (e.g. OpenLLaMA, GPT) and lets you chat with your own data using vector search (FAISS + Sentence Transformers).

Features
- Chat interface with context memory
- Local embedding & vector store (FAISS)
- Easy integration with HuggingFace models

## Run it locally
pip install -r requirements.txt
streamlit run app.py
