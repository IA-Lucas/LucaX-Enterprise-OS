---
name: rq-3-e-do-acervo-mas-os-57-sao-lacuna-do-juiz-py
description: "RQ-3 e norma do acervo e nao alcanca o lucaX; os vetos sem fundamento nao sao juiz omitindo, sao o juiz.py descartando — e sao 74, nao 57."
metadata: 
  node_type: memory
  type: project
  originSessionId: 0e7536bb-e3c1-40fb-b929-913247fe963c
  modified: 2026-08-09T11:44:35.271Z
---

Medido em 2026-08-08 (M-03A), respondendo se os 74 vetos do lucaX violam `RQ-3`.

**`RQ-3` e do acervo.** `departments/qar/carta.md:276`, registro de riscos de DEP-QAR:
*"**Veto usado como poder de merito** — barrar por discordar do conteudo · Todo veto cita
o item de DoD ou o risco nao mitigado que o fundamenta; veto sem fundamento e devolvido"*.
**Zero ocorrencias de `RQ-3` em toda a arvore do lucaX.**

**Mas nao ha violacao**, por dois motivos medidos:

1. Nenhum dos 74 reprovados e veto de DEP-QAR. `RQ-3` vincula o veto do **orgao** dentro
   do acervo; o `critico` do lucaX nao e o orgao. Norma do acervo nao alcanca ato de fora
   dele — mesma armadilha da F22 (CAP-financeiro despachando para porta que nao recebe),
   no sentido inverso.
2. Os 57 sem fundamento **nao sao juiz omitindo, sao codigo descartando**.
   `scripts/juiz.py:150-151`: para `critico`, chama `registrar_veredito(agent_type, ...)`
   **sem passar `motivo`**; so `coo-critico` passa (linha 159). O contrato de saida do
   `critico` (`.claude/agents/critico.md:45`) **exige** `Motivo (1 linha)`. O fundamento e
   emitido no texto e perdido a caminho do log. Por isso os 57 sem motivo sao exatamente
   os 57 do `critico`, e os 17 do `coo-critico` tem todos.

**Achado mais duro que o da F37: em fundamento gravado o log tem 0 de 74, nao 17.** O
campo `motivo` dos 17 nao e fundamento no sentido de `RQ-3` — e uma **tag de armadilha**
de conjunto fechado (`ARMADILHAS_VALIDAS`, `juiz.py:88-92`): `pareceu-razoavel` 9,
`nenhuma` 5, `sem-busca-acervo` 1, `ressalva-como-alibi` 1, `mudanca-pequena` 1. Cinco
dizem literalmente `nenhuma`. Os 90 aprovados tem 0 motivo por desenho.

**Dono: lucaX.** E lacuna de fidelidade do log em `scripts/juiz.py`, materia de la — nao
vira achado com dono e gatilho no acervo.

**Why:** a pergunta "de quem e a norma" decide quem responde, e a resposta obvia (o texto
de `RQ-3` descreve exatamente o sintoma) estava errada nas duas pontas: a norma nao
alcanca, e o sintoma tem outra causa. Ler o call site desfez as duas.

**How to apply:** antes de transformar numero da fabrica em violacao de norma do acervo,
conferir (a) se a norma alcanca o ator e (b) se o dado ausente foi omitido pelo ator ou
descartado pelo instrumento que grava. Ver [[veredictos-lucax-25-de-164-sao-juiz-1]].
