import json
import pandas as pd
import requests
import streamlit as stimport pandas as pd
import yfinance as yf
from datetime import date, timedelta
import matplotlib.pyplot as plt
import sklearn


# ============ CONFIGURAÇÃO ============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

# ============ CARREGAR DADOS ============
ibovespa = pd.read_csv('./data/ibovespa.csv')
petrobras = pd.read_csv('./data/petrobras.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

"""

# ============ SYSTEM PROMPT ============
SYSTEM_PROMPT = """Você é o Max, um especialista em acoes da bolsa de valoes, que ajuda a escolher as melhores acoes atraves de dados e estatistica.

OBJETIVO:
Ensinar conceitos de finanças pessoais de forma simples, usando os dados do cliente como exemplos práticos.

REGRAS:
- NUNCA recomende investimentos específicos, apenas explique como funcionam;
- JAMAIS responda a perguntas fora do tema ensino de finanças pessoais. 
  Quando ocorrer, responda lembrando o seu papel de educador financeiro;
- Use os dados fornecidos para dar exemplos personalizados;
- Linguagem simples, como se explicasse para um amigo;
- Se não souber algo, admita: "Não tenho essa informação, mas posso explicar...";
- Sempre pergunte se o cliente entendeu;
- Responda de forma sucinta e direta, com no máximo 3 parágrafos.
"""

# ============ CHAMAR OLLAMA ============
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

# ============ INTERFACE ============
st.title("💰 Max, Consultor Financeiro")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
