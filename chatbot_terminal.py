# chatbot_terminal.py: Terminal interface

from chatbot_core_onenote import build_qa_chain

qa_chain = build_qa_chain("customer_xy_notes.txt")
chat_history = []

print("OneNote-Chatbot started! Type 'exit' to quit.")

while True:
    query = input("\n❓ Your question: ")
    if query.lower() in ["exit", "quit"]:
        print("👋 Chat ended.")
        break

    result = qa_chain({"question": query, "chat_history": chat_history})
    print("\n🤖 Answer:", result["answer"])
    chat_history.append((query, result["answer"]))
    print("\n🔍 Source snippet:")
    print(result["source_documents"][0].page_content[:300])