# from langchain.chains import ConversationalRetrievalChain
# from langchain_openai import ChatOpenAI
# from app.chat.vector_stores.pinecone import build_retriever
# from app.chat.llms.chatopenai import build_llm
# from app.chat.memories.sql_memory import build_memory

# def build_llm(chat_args):
#     retriever = build_retriever(chat_args)
#     llm = build_llm(chat_args)
#     memory = build_memory(chat_args)
#     return ConversationalRetrievalChain.from_llm(
#         llm=llm,
#         retriever=retriever,
#         memory=memory
#     ) 

from langchain.chat_models import ChatOpenAI

def build_llm(chat_args):
    return ChatOpenAI()