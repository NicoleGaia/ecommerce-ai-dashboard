 #importa as bibliotecas pandas(análise de dados) 
 # e sqlalchemy(conversa com banco de dados)
import streamlit as st

import pandas as pd
from sqlalchemy import create_engine #crete_engine (criar motor) que vai ligar Python ao Supabase
from google import genai

DATABASE_URL = st.secrets["DATABASE_URL"]
CHAVE_API_GEMINI = st.secrets["CHAVE_API_GEMINI"]

#def -> define uma função
def gerar_insights_com_ia():
    print("A tentar ligar à base de dados...")

    #cria o "motor" de ligação
    engine = create_engine(DATABASE_URL)

    #Ler a View que você criou diretamente para o Python
    query_faturamento = "SELECT * FROM vw_faturamento_por_categoria"
    query_logistica = "SELECT * FROM vw_status_entrega"
    #try/except -> tenta executar o código e, se houver um erro, captura a exceção
    try:
        #Ler a View do Supabase e aramazena o resultado em um DataFrame do pandas
        df_faturamento = pd.read_sql(query_faturamento, engine) #lê a query e armazena o resultado em um DataFrame do pandas
        df_logistica = pd.read_sql(query_logistica, engine) #lê a query e armazena o resultado em um DataFrame do pandas

        print("✅ Dados recolhidos! A enviar para a IA analisar...\n")

        #Trasforma a tabela numa string de texto para a IA conseguir ler
        dados_em_texto_faturamento = df_faturamento.to_string(index=False) #significa que não queremmos o índice das linhas da tabela
        dados_em_texto_logistica = df_logistica.to_string(index=False)

        prompt = f"""
        Atue como um Analista de Dados Sénior de um E-commerce. 
        Analise as seguintes tabelas que mostram a quantidade vendida e o faturamento total por categoria , bem como os status das entregas dos produtos vendidos:
        
        TABELA 1: Faturamento por Categoria
        {dados_em_texto_faturamento}
        
        TABELA 2: Status das Entregas
        {dados_em_texto_logistica}

        Escreva um relatório curto (máximo de 2 parágrafos) com:
        1. O maior destaque positivo (o que deu mais dinheiro).
        2. Uma recomendação estratégica de marketing para aproveitar estes números.
        3. Verificar se há um problema de logística (entregas atrasadas) e sugerir uma ação para melhorar a experiência do cliente.
        """

        # Chama a IA para gerar insights com base nos dados fornecidos
        client = genai.Client(api_key=CHAVE_API_GEMINI) #autenticação com a chave da API do Gemini
        resposta = client.models.generate_content( # gera conteúdo com base no prompt fornecido
            model='gemini-3.5-flash',
            contents=prompt # conteúdo que será enviado para a IA analisar e gerar insights
        )

        #Imprime o resultado da IA
        print("="*50)
        print("🤖 INSIGHTS AUTOMÁTICOS DA IA:")
        print(resposta.text)
        print("="*50)

    except Exception as e:
        print("❌ Ocorreu um erro:", e)

#Executa a função para testar a conexão com o banco de dados
gerar_insights_com_ia()
