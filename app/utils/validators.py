import re
import streamlit as st

def validate_query(query: str) -> bool:
    """
    Valida a query SQL gerada para garantir que seja segura e bem formada.
    
    Args:
        query (str): A query SQL a ser validada.
        
    Returns:
        bool: True se a query for válida, False caso contrário.
    """
    # Verifica se a query não está vazia
    if not query.strip():
        st.error("A query está vazia.")
        return False
    
    # Verifica se a query contém palavras-chave perigosas (ex: DROP, DELETE) para evitar SQL Injection
    dangerous_keywords = ['drop', 'delete', 'truncate', 'alter', 'insert', 'update']
    if any(keyword in query.lower() for keyword in dangerous_keywords):
        st.error("A query contém palavras-chave perigosas.")
        return False
    
    # Verifica se a query tem uma estrutura básica válida (por exemplo, contém SELECT)
    if not re.search(r'\bselect\b', query, re.IGNORECASE):
        st.error("A query não parece ser uma consulta SELECT.")
        return False
    
    return True

