import ollama
from utils.files import read_file
from services.database import get_db_structure
import re
import unidecode
import streamlit as st

# Configurações da API
MODEL_NAME = 'codellama' 

def generate_query(user_input: str) -> str:
    """
    Gera uma query SQL a partir da entrada do usuário usando IA generativa.
    
    Args:
        user_input (str): A consulta em linguagem natural fornecida pelo usuário.
        
    Returns:
        str: A query SQL gerada pelo modelo de IA.
    """
    try:
        isCorrect = False
        prompt_template = read_file("app/prompts/prompt_template.txt")
        db_structure = get_db_structure()
        prompt = prompt_template.format(
            instruction=user_input,
            db_structure=db_structure
        )
        
        while not isCorrect:
            # Chama a API do modelo de IA para gerar a query
            response = ollama.generate(
                model=MODEL_NAME,
                prompt=prompt,
            )

            print(response.get('response'))

            query, chart_type, y_chart_value, x_chart_value = extract_values(response.get('response'))
            chart_config = {
                "chart_type": chart_type, 
                "y_chart_value": y_chart_value,
                "x_chart_value": x_chart_value
            }

            if query:
                isCorrect = True

            print(chart_config)
        
        return query, chart_config
    
    except Exception as e:
        st.error(f"Erro ao gerar a query: {e}")
        return ""
    
def extract_values(response: str):
    # Usar expressões regulares para capturar os valores
    query_pattern = re.compile(r"query:\s*(.*?);", re.IGNORECASE)
    chart_type_pattern = re.compile(r"chart type:\s*(.*?)(?:\s|;|$)", re.IGNORECASE)
    y_chart_value_pattern = re.compile(r"y value:\s*(.*?)(?:\s|;|$)", re.IGNORECASE)
    x_chart_value_pattern = re.compile(r"x value:\s*(.*?)(?:\s|;|$)", re.IGNORECASE)

    # Função para retornar None se o valor for "" ou "none"
    def clean_value(value):
        value = remove_acentos_e_pontuacao(value.strip())
        if not value or value.strip().lower() == "none":
            return None
        return value
    
    # Captura valores ou define como None se não encontrado
    query_match = query_pattern.search(response)
    chart_type_match = chart_type_pattern.search(response)
    y_chart_value_match = y_chart_value_pattern.search(response)
    x_chart_value_match = x_chart_value_pattern.search(response)
    
    # Checa se a busca retornou resultado e usa .group(1) se sim
    query = query_match.group(1) if query_match else None
    chart_type = clean_value(chart_type_match.group(1)) if chart_type_match else None
    y_chart_value = clean_value(y_chart_value_match.group(1)) if y_chart_value_match else None
    x_chart_value = clean_value(x_chart_value_match.group(1)) if x_chart_value_match else None
    
    return query, chart_type, y_chart_value, x_chart_value

def remove_acentos_e_pontuacao(text):
    text = unidecode.unidecode(text)
    text = text.translate(str.maketrans('', '', '".;'))
    return text