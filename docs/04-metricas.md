# Avaliação e Métricas

> [!TIP]
> **Prompt usado para esta etapa:**
> Crie o system prompt do agente "Max".
> REGRAS:
- NUNCA recomende investimentos sem dados;
- JAMAIS responda a perguntas fora do tema que sao as acoes da bolsa de valores. 
  Quando ocorrer, responda lembrando o seu papel de consultor financeiro;
- Sempre responda baseado em dados;
- Linguagem simples, como se explicasse para um amigo;
- Se não souber algo, admita: "Não tenho essa informação, mas posso explicar...";
- Sempre pergunte se o cliente entendeu;
- Responda de forma sucinta e direta.
-Sempre que for peguntado mostre as fontes utilizadas
-Sempre mostrar os risco das acoes 
> [03-prompts.md]
> Crie um plano de avaliação pro agente "Max" com 3 métricas: assertividade das tecomendacoes, segurança e coerência. Inclua 4 cenários de teste e um formulário simples de feedback. Preencha o template abaixo.
>
[ 04-metricas.md]


## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | As acoes recomendasdas fazem sentido? | Sugerir acoes baseada em dados |

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de setores na bolsa de valores
- **Pergunta:** "Quais os setores da bolsa de valores?"
- **Resposta esperada:** agente faz pesquisa (https://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/renda-variavel/acoes/consultas/classificacao-setorial/)
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 2: Recomendação de produto
- **Pergunta:** "Qual acao você recomenda para mim?"
- **Resposta esperada:** a gente procura acoes com o menor risco
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:**  So respondo sobre acoes da bolsa de valores
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Qual outro investimento voce me indica?"
- **Resposta esperada:** So respondo sobre acoes da bolsa de valores
- **Resultado:** [X] Correto  [ ] Incorreto

---

## Formulário de Feedback (Sugestão)

Use com os participantes do teste:

| Métrica | Pergunta | Nota (1-5) |
|---------|----------|------------|
| Assertividade | "As respostas responderam suas perguntas?" | ___ |
| Segurança | "As informações pareceram confiáveis?" | ___ |
| Coerência | "A linguagem foi clara e fácil de entender?" | ___ |

**Comentário aberto:** O que você achou desta experiência e o que poderia melhorar?

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- [Liste aqui]

**O que pode melhorar:**
- [Liste aqui]
