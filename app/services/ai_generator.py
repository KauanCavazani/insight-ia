from config.env import DOC_PATH
from utils.files import read_file
from services.database import get_db_structure
import re
import unidecode
import streamlit as st
import os
from langchain_community.llms import Ollama
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains.retrieval_qa.base import RetrievalQA
import json
from langchain_community.document_loaders import TextLoader

class IaGenerator:
    def __init__(self):
        self.ollama = Ollama(model="codellama")
        self.oembed = OllamaEmbeddings(model="nomic-embed-text")
        self.vector_store = self._process_document()

    def _process_document(self):
        """Processa os documentos de apoio"""
        all_docs = []

        for filename in os.listdir(DOC_PATH):
            if filename.endswith(".txt"):
                file_path = os.path.join(DOC_PATH, filename)
                loader = TextLoader(file_path)
                loaded_text = loader.load() 
                all_docs.extend([doc for doc in loaded_text])

        text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0)
        all_docs_splitter = text_splitter.split_documents(all_docs)
        
        if all_docs:
            return Chroma.from_documents(documents=all_docs_splitter, embedding=self.oembed, persist_directory='docs/chroma/')
        else:
            print("Nenhum documento encontrado.")

    def generate_query(self, user_input: str) -> str:
        """
        Gera uma query SQL a partir da entrada do usuário usando IA generativa.
        
        Args:
            user_input (str): A consulta em linguagem natural fornecida pelo usuário.
            
        Returns:
            str: A query SQL gerada pelo modelo de IA.
        """
        prompt_template = read_file("app/prompts/prompt_template.txt")

        prompt = prompt_template.format(
            instruction=user_input
        )

        qachain = RetrievalQA.from_chain_type(self.ollama, retriever=self.vector_store.as_retriever())
        res = qachain.invoke({"query": prompt})

        try:
            print(res["result"])
            res_json = json.loads(res["result"])["query"]
        except Exception as ex:
            res_json = {"error": "A resposta não estava no formato JSON", "response": ex}

        return res_json