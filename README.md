# LangChain App – Your Local LLM Chat Assistant for your Notes
This is a simple LangChain-based Streamlit app that connects to local or cloud LLMs (e.g. OpenLLaMA, GPT) and lets you chat with your own data using vector search (FAISS + Sentence Transformers).

Features
- Chat interface with context memory
- Local embedding & vector store (FAISS)
- Easy integration with HuggingFace models

## Run it locally
pip install -r requirements.txt
streamlit run app.py

☕ Comparison to Langflow: https://medium.com/data-science-collective/langchain-vs-langflow-build-a-simple-llm-app-with-code-or-drag-drop-cbace40c12b1?sk=b5e4970bff791c8e1d80a22bc221a74b
☕ Installation Guide for LangChain and Ollama: https://sarahleaschrch.substack.com/p/step-by-step-guide-to-install-langchain
