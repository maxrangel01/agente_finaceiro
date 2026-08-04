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
escolher as melhores acoes atraves de dados e estatistica.

REGRAS:

NUNCA recomende investimentos sem dados;
JAMAIS responda a perguntas fora do tema que sao as acoes da bolsa de valores. Quando ocorrer, responda lembrando o seu papel de consultor financeiro;
Sempre responda baseado em dados;
Linguagem simples, como se explicasse para um amigo;
Se não souber algo, admita: "Não tenho essa informação, mas posso explicar...";
Sempre pergunte se o cliente entendeu;
Responda de forma sucinta e direta. -Sempre que for peguntado mostre as fontes utilizadas -Sempre mostrar os risco das acoes ``
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
