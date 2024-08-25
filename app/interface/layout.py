import streamlit as st

def render_layout():
    """
    Renderiza o layout da interface do usuário e retorna a entrada do usuário.
    """
    
    # Caixa de texto para o usuário inserir a consulta em linguagem natural
    st.subheader("Digite sua consulta")
    user_input = st.text_area(
        "O que você gostaria de consultar?", 
        placeholder="Exemplo: Quantos usuários têm mais de 65 anos?"
    )
    
    # Botão para confirmar a consulta
    if st.button("Consultar"):
        return user_input
    
    return None
