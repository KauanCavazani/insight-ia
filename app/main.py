import streamlit as st
from interface.layout import render_layout
from services.ai_generator import generate_query
from services.database import execute_query
from utils.validators import validate_query
from utils.plot import generate_plot

def main():
    st.title("Consulta Analítica com IA Generativa")
    
    # Renderiza a interface de entrada e outras partes do layout
    user_input = render_layout()

    # Processa a entrada do usuário
    if user_input:
        with st.spinner('Gerando query...'):
            # Gera a query a partir do prompt do usuário usando a IA
            generated_query, chart_config = generate_query(user_input)

        if generate_query:
            st.subheader("Query Gerada")
            st.code(generated_query, language='sql')
            
            # Valida a query gerada
            if validate_query(generated_query):
                # Executa a query no banco de dados
                results = execute_query(generated_query)
                plot = generate_plot(results, chart_config)
                
                # Exibe os resultados
                st.subheader("Resultados")
                st.write(results)
                if plot:
                    st.pyplot(plot)
            else:
                st.error("A query gerada não é válida. Tente reformular a pergunta.")
    
if __name__ == "__main__":
    main()
