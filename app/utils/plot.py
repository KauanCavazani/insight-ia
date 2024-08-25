import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import streamlit as st


def generate_plot(df: pd.DataFrame, chart_config: dict):
    """
    Plota um gráfico com base no DataFrame e no tipo de gráfico sugerido pela IA.
    
    Args:
        df (pd.DataFrame): DataFrame contendo os dados da query.
        chart_config (dict): Configurações do gráfico.
    """
    plot = None

    # Configurações do gráfico
    chart_type = chart_config['chart_type']
    x_value = chart_config['x_chart_value']
    y_value = chart_config['y_chart_value']

    if not x_value or not y_value:
        return None
    
    if x_value not in df.columns or y_value not in df.columns:
        return None

    x_is_numeric = pd.to_numeric(df[x_value], errors='coerce').notna().all()
    y_is_numeric = pd.to_numeric(df[y_value], errors='coerce').notna().all()

    if not x_is_numeric and not y_is_numeric:
        return None

    # Ajusta o gráfico baseado na quantidade de registros
    sample_size = 1000 
    if len(df) > sample_size:
        df = df.sample(sample_size)

    num_columns = df.shape[1]

    if chart_type and num_columns > 1:
        # Define o tamanho da figura
        plt.figure(figsize=(12, 8))

        # Gera o gráfico baseado no tipo
        if chart_type == "bar":
            if len(df) > 50:
                st.warning("Número de categorias é muito grande. Exibindo uma amostra.")
                df = df.sample(50)  
            ax = sns.barplot(data=df, x=df[x_value], y=df[y_value])
            plt.xticks(rotation=45)  
        elif chart_type == "line":
            sns.lineplot(data=df, x=df[x_value], y=df[y_value])
        elif chart_type == "pie":
            if len(df) <= 10: 
                df.plot.pie(y=df[y_value], autopct='%1.1f%%')
            else:
                st.warning("Número de categorias para o gráfico de pizza é muito grande. Exibindo uma amostra.")
                df = df.head(10)  
                df.plot.pie(y=df[y_value], autopct='%1.1f%%')
        elif chart_type == "scatter":
            sns.scatterplot(data=df, x=df[x_value], y=df[y_value])
        else:
            st.error(f"Tipo de gráfico '{chart_type}' não reconhecido. Mostrando histograma.")
            sns.histplot(data=df, x=df[x_value], kde=True)

        plt.title(f"{chart_type.capitalize()} plot for {x_value} vs {y_value}")
        plt.xlabel(x_value)
        plt.ylabel(y_value)

        plot = plt

    return plot