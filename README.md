# 🛒 E-commerce AI Analytics Dashboard

> Um dashboard analítico interativo e inteligente para gestão de e-commerce, construído com Python, Streamlit, PostgreSQL (Supabase) e Inteligência Artificial generativa (Llama 3 via Groq).

---

## 🚀 Sobre o Projeto
Este projeto foi desenvolvido com o objetivo de centralizar e analisar dados de faturamento e logística de um e-commerce. A aplicação não se limita a exibir gráficos estáticos: ela conta com **filtros interativos dinâmicos** e um **Cérebro Analítico integrado com IA**, capaz de redigir relatórios estratégicos e executivos sob demanda com base nos recortes de dados selecionados pelo usuário.

---

## 🛠️ Tecnologias e Ferramentas Utilizadas
* **Linguagem:** Python 3.10+
* **Interface Web:** Streamlit
* **Manipulação de Dados:** Pandas
* **Banco de Dados Relacional:** PostgreSQL (hospedado no Supabase)
* **Conexão com Banco:** SQLAlchemy & Psycopg2
* **Inteligência Artificial:** Llama 3 (via API da Groq)
* **Controle de Versão & Deploy:** Git, GitHub e Streamlit Cloud

---

## 📊 Principais Funcionalidades
1. **Conexão em Nuvem Segura:** Integração direta com banco de dados PostgreSQL (hospedado no Supabase).
2. **Filtros Dinâmicos na Barra Lateral:** Seleção múltipla de categorias que atualizam instantaneamente os gráficos e métricas da tela.
3. **Análise Estratégica com IA (LLM):** Botão inteligente que lê o estado atual dos dados filtrados e gera *insights* comerciais e recomendações operacionais em segundos.
4. **Otimização de Performance:** Utilização de cache (`st.cache_data`) para garantir navegação fluida e economizar requisições ao banco.

---

## ⚙️ Como Executar o Projeto Localmente

Se você deseja clonar e rodar esta aplicação na sua máquina, siga os passos abaixo:

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/NicoleGaia/ecommerce-ai-dashboard](https://github.com/NicoleGaia/ecommerce-ai-dashboard)
   cd ecommerce-ai-dashboard

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt

3. **Configure as credenciais locais:**
   ```Ini,TOML
   DATABASE_URL = "sua_string_de_conexao_do_supabase"
   CHAVE_API_GROQ = "sua_chave_da_api_groq"

4. **Execute a aplicação:**
   ```bash
   streamlit run dashboard.py

---

## 🌐 Acesso em Produção

Você pode testar a aplicação diretamente na nuvem através do link abaixo:
👉 [Acessar E-commerce AI Dashboard na Web](https://ecommerce-ai-dashboard.streamlit.app/)

---

## 👤 Autora
Desenvolvido por **Nicole** 🚀  
[LinkedIn](https://www.linkedin.com/in/nicole-gaia/) | [GitHub](https://github.com/NicoleGaia)