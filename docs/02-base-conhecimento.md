# Base de Conhecimento

```python
import pandas as pd
import yfinance as yf
from datetime import date, timedelta
import matplotlib.pyplot as plt
import sklearn
'''

> [!TIP]
> **Prompt usado para esta etapa:**
> 

> [cole ou anexe o template `02-base-conhecimento.md` pra contexto]

## Dados Utilizados


| `acao.csv` | CSV | sera baixado atraves do **yfinance** . |

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

caso não encontrado o pode fazer uma varredura na rede e procurar sobre a acao necessaria

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

```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados serao baixaidos atraves do **df_acao = yf.download(tickers=self.acao, start=data_1,end=data_2,interval='1d')** em formato CSV, atraves dos dados baixados inicia as analises e tratamentos dos dados. Apos a limpeza começa a analise utilizando a biblioteca do **sklearn**, caso necessario aprensenta graficos.



## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.
acao ="PETR4.SA"
data_1='2026-02-05'
data_2='2020-02-05'
dados = yf.download(f"{acao}, start={d},end={d},interval='1d'")

