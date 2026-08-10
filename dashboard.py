import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from groq import Groq

#cria uma variável para armazenar a URL de conexão com o banco de dados Supabase
DATABASE_URL = st.secrets["DATABASE_URL"]
CHAVE_API_GROQ = st.secrets["CHAVE_API_GROQ"]

#Config da página web do Stramlit
st.set_page_config(
    page_title="E-commerce Analytics",
    page_icon="📊",
    layout="wide"
)

# O @st.cache_data diz ao Streamlit para não ir ao banco de dados 
# toda a vez que a pessoa clicar num botão, deixando o site muito mais rápido!
@st.cache_data(ttl=300) #ttl = time to live, a cada 5 min busca os dados atualizados no banco de dados

def carregar_dados():
    engine = create_engine(DATABASE_URL)
    df_faturamento = pd.read_sql("SELECT * FROM vw_faturamento_por_categoria", engine)
    df_logistica = pd.read_sql("SELECT * FROM vw_status_entrega", engine)
    return df_faturamento, df_logistica

df_faturamento, df_logistica = carregar_dados()

#Interface visual
st.title("📊 Smart Insights Dashboard - E-commerce")
st.markdown("Um painel gerencial automatizado com Inteligência Artificial.")

st.divider() #cria linha horizontal para separar as seções

#Barra lateral de FILTROS
st.sidebar.header("Filtros")

#lista de categorias disponíveis para o usuário selecionar
categorias_disponiveis = df_faturamento['categoria'].unique().tolist()

#caixa de seleção na barra lateral
categoria_selecionada = st.sidebar.multiselect(
    "Selecione as Categorias",
    options=categorias_disponiveis,
    default=categorias_disponiveis #seleciona todas as categorias por padrão
)

#Filtra os dados com base na categoria selecionada pelo usuário
if categoria_selecionada:
    df_faturamento_filtrado = df_faturamento[df_faturamento['categoria'].isin(categoria_selecionada)]
else:
    df_faturamento_filtrado = df_faturamento.iloc[0:0]

#CÁLCULO E EXIBIÇÃO DE KPIS
faturamento_global = df_faturamento["faturamento_total"].sum()
total_pedidos_logistica = df_logistica["total_pedidos"].sum()
#Ticket Médio = Faturamento Global / Total de Pedidos
ticket_medio = faturamento_global / total_pedidos_logistica if total_pedidos_logistica > 0 else 0

# Criamos colunas para dispor os cartões de métrica lado a lado
col_kpi1, col_kpi2, col_kpi3, col_kpi4 = st.columns(4)

with col_kpi1:
    st.metric(label="💰 Faturamento Total", value=f"R$ {faturamento_global:,.2f}")
with col_kpi2:
    st.metric(label="📦 Total de Pedidos", value=f"{total_pedidos_logistica:,}")
with col_kpi3:
    st.metric(label="🎟️ Ticket Médio", value=f"R$ {ticket_medio:,.2f}")
with col_kpi4:
    st.metric(label="🤖 Status da IA", value="Ativo & Online", delta="Gemini 3.5")

st.divider()

#Cria duas colunas na tela
col1, col2 = st.columns(2)

with col1:
    st.subheader("💰 Faturamento por Categoria")
    st.bar_chart(df_faturamento_filtrado.set_index('categoria')['faturamento_total'], color="#1f77b4")
                 #data=df_faturamento.head(10), x="categoria", y="faturamento_total", color="#1f77b4"

with col2:
    st.subheader("📦 Status Global de Entregas")
    st.bar_chart(data=df_logistica, x="status_entrega", y="total_pedidos", color="#ff7f0e")

#Integração com IA
st.divider() #cria linha horizontal para separar as seções
st.subheader("🧠 Cérebro Analítico")

if st.button("Gerar Relatório Estratégico com IA"):

    #exibe uma animação de carregamento enquanto a IA pensa
    with st.spinner("Lendo os dados e preparando o relatório..."):
        try:
            texto_faturamento = df_faturamento_filtrado.head(10).to_string(index=False)
            texto_logistica = df_logistica.to_string(index=False)

            prompt = f"""
            Atue como um Diretor de E-commerce Sênior. O utilizador selecionou especificamente as seguintes categorias para análise: {categoria_selecionada}.
            
            Analise estes dados consolidados destas categorias:
            
            FATURAMENTO GLOBAL DAS CATEGORIAS SELECIONADAS: R$ {df_faturamento_filtrado['faturamento_total'].sum():,.2f}
            
            TABELA DE FATURAMENTO:
            {texto_faturamento}
            
            TABELA DE LOGÍSTICA (Panorama Geral):
            {texto_logistica}
            
            Escreva um relatório executivo curto e em tópicos focado estritamente nas categorias selecionadas, apontando:
            1. O desempenho comercial destas categorias específicas e qual se destaca mais.
            2. Uma avaliação crítica conectando com o cenário operacional.
            3. Uma recomendação estratégica direcionada para este grupo de produtos.
            """
            api_key = st.secrets["CHAVE_API_GROQ"]
            client = Groq(api_key=api_key)
            
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model="llama-3.1-8b-instant",
            )
            
            resposta = chat_completion.choices[0].message.content

            resposta_formatada = resposta.replace("$", "\$") #substitui o sifrão simples para evitar problemas de formatação
            
            st.success("Análise Estratégica Concluída!")
            st.write(resposta_formatada)
                
        except Exception as e:
            st.error(f"Erro detalhado na IA: {e}")