---
name: veredictos-lucax-25-de-164-sao-juiz-1
description: "O log de vereditos do lucaX mistura Juiz 1 e Juiz 2 — a taxa real de reprovacao do Juiz 2 e 53,2%, nao os 45,1% que a F37 publicou."
metadata: 
  node_type: memory
  type: project
  originSessionId: 0e7536bb-e3c1-40fb-b929-913247fe963c
  modified: 2026-08-09T11:44:20.303Z
---

Medido em 2026-08-08 (M-03A) sobre `E:\lucaX\nucleo\reforco\veredictos.jsonl`,
164 linhas, janela 2026-07-14 a 2026-07-29.

**25 das 164 linhas nao sao de Juiz 2.** Entram por `scripts/juiz.py:474`, que e o
caminho do **Juiz 1** (validacao contra `specs/saida.schema.json`) e registra veredito
de *qualquer* agente cuja resposta seja JSON. Sao `coo-executor` (24) e
`webtoon-contador` (1), **todas `aprovado`**. O conjunto Juiz 2 real e
`JUIZES_TEXTO = {critico, coo-critico}` (`juiz.py:97`) — `critico` 106 + `coo-critico` 33.

| conjunto | total | reprovados | taxa |
|---|---|---|---|
| log inteiro (o que a F37 publicou) | 164 | 74 | 45,1% |
| **so Juiz 2** (correto) | **139** | **74** | **53,2%** |

Os 25 diluiam a taxa por serem todos aprovados. O `README.md` da pasta afirma que o log
e "de todo veredito real de Juiz 2" — **a afirmacao esta vencida**: e mais um caso da
familia `RD-101`, artefato que afirma propriedade que ja nao vale.

**Why:** a F37 leu o log pela afirmacao do README em vez de pelos call sites de
`registrar_veredito`, e por isso contou quatro agentes sem notar que dois deles nao
julgam nada. Numero publicado com denominador contaminado vira lastro de decisao errada.

**How to apply:** ao reusar esse log, filtrar por `agente in {critico, coo-critico}`
antes de qualquer razao. E antes de citar qualquer numero da fabrica, conferir o call
site que grava, nao o README que descreve. Contexto: a M-03A concluiu que **QG-3 do
acervo e Juiz 2 do lucaX NAO sao o mesmo** — objeto diferente (artefato x mensagem de
subagente), criterio diferente (9 itens de DoD com evidencia por item x 6 fases
PASS/FAIL/N/A), orgao diferente (DEP-QAR x agente `critico`) — e a linha JSONL nem
identifica **o que** foi julgado, entao o denominador "submetidos" do `KQ-8` e
impreenchivel a partir dela. **`KQ-8` segue `definido, sem valor`, e isso esta correto.**
Nada a somar, nada de tarefa para a principal. Ver [[rq-3-e-do-acervo-mas-os-57-sao-lacuna-do-juiz-py]].
