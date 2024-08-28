from sqlalchemy import create_engine
from sqlalchemy import inspect
from config.env import DB_NAME, DB_HOST, DB_PASSWORD, DB_USER, DB_PORT
import pandas as pd
import streamlit as st

def get_sqlalchemy_engine():
    """
    Cria uma engine SQLAlchemy para conexão com o banco de dados MySQL.
    
    Returns:
        sqlalchemy.engine.Engine: Objeto de engine SQLAlchemy.
    """
    try:
        engine = create_engine(f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
        return engine
    except Exception as e:
        print(f"Erro ao criar engine SQLAlchemy: {e}")
        return None

def execute_query(query: str) -> pd.DataFrame:
    """
    Executa uma query no banco de dados MySQL e retorna os resultados em um DataFrame.
    
    Args:
        query (str): A query SQL a ser executada.
        
    Returns:
        pd.DataFrame: DataFrame contendo os resultados da query.
    """
    engine = get_sqlalchemy_engine()
    if engine is None:
        return None

    try:
        df = pd.read_sql(query, engine)

        return df
    except Exception as e:
        st.error(f"Erro ao executar a query: {e}")
        return None
    finally:
        engine.dispose()

def get_db_structure() -> str:
    """
    Obtém a estrutura do banco de dados (nomes das tabelas e colunas) para ser usada no prompt da IA.

    Returns:
        str: Estrutura do banco de dados formatada como texto.
    """
    engine = get_sqlalchemy_engine()
    if engine is None:
        st.error("Erro ao conectar ao banco de dados.")
        return None

    try:
        inspector = inspect(engine)
        tables = inspector.get_table_names()

        db_structure = f"Estrutura do Banco de Dados '{DB_NAME}':\n\n"

        if len(tables) == 0:
            st.error("Nenhuma tabela encontrada.")
            return None

        for table_name in tables:
            db_structure += f"Tabela: {table_name}\n"
            columns = inspector.get_columns(table_name)
            for column in columns:
                field = column['name']
                column_type = str(column['type'])
                db_structure += f"- {field} ({column_type})\n"
            db_structure += "\n"

        return db_structure

    except Exception as e:
        st.error(f"Erro ao obter a estrutura do banco de dados")
        return None

    finally:
        engine.dispose()

def close_connection(engine):
    """
    Fecha a engine do SQLAlchemy.
    
    Args:
        engine: Objeto de engine SQLAlchemy.
    """
    if engine:
        engine.dispose()
