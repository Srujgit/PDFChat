'''
PDF chat with RAG.
Database - Chroma
Embedding Model - Linq Mistral
Local LLM - Mistral 7B
GUI - streamlit

Flow-
1. User drops/ uploads files to query to.
2. A text splitter splits the text into chunks. Chunks are then passed to an embedding model.
3. Embeddings are then stored in ChromaDB.
4. Embeddings are retrieved as per user queries. 
'''
import streamlit as st

st.title("Welcome to RAGChat")