# Base de Conhecimento



> [!TIP]
> **Prompt usado para esta etapa:**
> 

> [cole ou anexe o template `02-base-conhecimento.md` pra contexto]

## Dados Utilizados


| `acao.csv` | CSV | sera baixado atraves do **yfinance** . |

sites para buscas:
https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/cotacoes/
https://statusinvest.com.br/acoes
https://investidor10.com.br/
https://br.investing.com/
https://www.fundamentus.com.br/
https://www.moneytimes.com.br/
https://www.infomoney.com.br/

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

caso não encontrado fazer uma varredura na **web** e procurar sobre a acao necessaria

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

apos o usuario fazer uma requesicao sobre uma acao o agente baixara os  dados atraves do yfinance

```python
import pandas as pd
import yfinance as yf
from datetime import date, timedelta
import matplotlib.pyplot as plt
import sklearn

df_ibovespa = yyf.download('^BVSP', period='2y', interval='1d')
print(df.head())
data_1 = input('data inicial')
data_2 =input('data final')
acao = inpunt('digite uma acao')
df_acao = yf.download(tickers=self.acao, start=data_1,end=data_2,interval='1d')

info = acacao_info = acao.info
print("P/L:", acao_info.get("trailingPE"))
print("ROE:", acao_info.get("returnOnEquity"))
print("Dividend Yield:", acao_info.get("dividendYield"))

```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados serao baixaidos atraves do **df_acao = yf.download(tickers=self.acao, start=data_1,end=data_2,interval='1d')** em formato CSV, atraves dos dados baixados inicia as analises e tratamentos dos dados. Apos a limpeza começa a analise utilizando a biblioteca do **sklearn**, caso necessario aprensenta graficos.

A análise fundamentalista de ações avalia o valor real de uma empresa por meio de seus indicadores financeiros, balanços e dados econômicos, focando em P/L, ROE e Dividend Yield.

Principais IndicadoresP/L (Preço sobre Lucro): Mostra o tempo de retorno do investimento.
P/VP (Preço sobre Valor Patrimonial): Compara o preço da ação com o patrimônio da empresa.
ROE (Retorno sobre o Patrimônio): Mede a eficiência no ganho de lucro.
Dividend Yield: Aponta o rendimento em dividendos pagos ao acionista.



## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.
acao ="PETR4.SA"
data_1='2026-02-05'
data_2='2020-02-05'
dados = yf.download(f"{acao}, start={d},end={d},interval='1d'")

