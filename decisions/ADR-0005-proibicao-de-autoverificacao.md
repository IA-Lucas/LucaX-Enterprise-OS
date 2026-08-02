---
id: ADR-0005-proibicao-de-autoverificacao
titulo: Proibir autoverificacao — nenhuma entidade verifica a si propria
tipo: adr
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-QAR
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0002, ADR-0003]
substitui: []
substituido_por: null
classe_mudanca: C2
tipo_decisao: 2
supera: []
superado_por: null
---

# ADR-0005: Proibir autoverificacao

## Proposito

Registrar a decisao de tornar explicita, no Meta Model e no catalogo de Capabilities, a
proibicao de que uma entidade verifique a si propria — e corrigir a redacao que hoje permite
essa leitura para `CAP-governanca`.

## Escopo

Aplica-se a relacao `verifica` (R-06 de FND-09 §6.1; RL-05 de FND-08 §5.2) entre quaisquer
entidades. Nao altera o escopo, os limites, os indicadores nem a custodia de nenhuma
Capability.

## Responsaveis

| Papel | Quem |
|---|---|
| Proponente | **DEP-QAR** — detectou o achado M1 na revisao do Meta Model |
| Guardiao (forma e classe) | DEP-GOV |
| Aprovador | **DEP-EXE** |
| Executor | DEP-GOV |

> **Nota de independencia.** A materia afeta `CAP-governanca`, custodiada por DEP-GOV. Por
> isso DEP-GOV atua **apenas como guardiao de forma**, nunca como proponente nem aprovador
> (FND-04 §3.1: Guardiao ≠ Proponente). O merito e de DEP-QAR e a aprovacao de DEP-EXE.
> Esta separacao e, ela propria, a aplicacao da regra que este ADR institui.

---

## 1. Contexto

A revisao arquitetural do Meta Model registrou o achado **M1**, de severidade alta:

> O catalogo declara, em `capabilities/README.md` §5: `CAP-governanca` | **todas** — forma,
> conformidade e rastreabilidade. Lido literalmente, "todas" inclui `CAP-governanca`.

A mesma redacao aparece em `CAP-governanca.md` §9: *"Esta Capability verifica a conformidade
de todas"*.

Nenhuma norma vigente proibia explicitamente o **auto-loop** da relacao `verifica`:

| Norma | O que proibe | O que **nao** proibia |
|---|---|---|
| LV-03 | Aprovar o proprio trabalho, ou revisar como independente o que se produziu | — |
| PI-05 | Concentracao de producao, revisao e aprovacao no mesmo papel | — |
| RL-05 (FND-08) | `verifica` coexistir com `depende-de` no mesmo par e direcao | O par reflexivo A→A |
| RM-06 (FND-09) | A relacao inversa `depende-de` quando ha `verifica` | O par reflexivo A→A |

**Pratica real observada:** nao houve autoverificacao. ADR-0002 foi proposto por DEP-EXE e
revisado por DEP-QAR; FND-09 foi proposto por DEP-GOV e revisado por DEP-QAR. A separacao foi
respeitada de fato — o defeito e de redacao normativa, nao de conduta.

## 2. Problema / Pergunta de decisao

A relacao `verifica` deve admitir par reflexivo, e a redacao do catalogo deve continuar
permitindo que `CAP-governanca` seja lida como verificadora de si propria?

## 3. Criterios de decisao

| # | Criterio | Peso | Como se mede |
|---|---|---|---|
| C1 | Elimina a leitura que contraria LV-03 | **Bloqueante** | Nenhuma redacao vigente permite auto-loop |
| C2 | Nao cria lacuna: alguem passa a verificar o que DEP-GOV produz | Alto | Verificador nomeado, sem violar RL-05 |
| C3 | Nao introduz relacao nem entidade nova | Alto | Apenas restricao a relacao existente |
| C4 | Nao duplica norma | **Bloqueante** | Regra escrita **uma vez**, referenciada nas demais |

## 4. Alternativas consideradas

### Alternativa A — Proibir o auto-loop no Meta Model e nomear o verificador de DEP-GOV

| Campo | Conteudo |
|---|---|
| Descricao | RM-06 (FND-09) passa a proibir o par reflexivo de `verifica`; catalogo e Carta corrigidos para "todas as demais"; declara-se quem verifica o que DEP-GOV produz |
| A favor | Satisfaz C1 a C4; regra universal escrita uma vez, no documento que governa relacoes entre tipos |
| Contra | Exige emenda MENOR a FND-09 e correcao em dois artefatos do catalogo |
| Custo | 1 regra, 3 correcoes de redacao |
| Avaliacao | C1 satisfeito · C2 alto · C3 alto · C4 satisfeito |

### Alternativa B — Corrigir apenas a redacao do catalogo

| Campo | Conteudo |
|---|---|
| Descricao | Trocar "todas" por "todas as demais" em `capabilities/README.md` e em `CAP-governanca.md`, sem tocar no Meta Model |
| A favor | Custo minimo; nenhuma emenda a documento fundacional |
| Contra | **Nao resolve C1 estruturalmente.** A norma continuaria permitindo o auto-loop, e a proxima Capability de verificacao criada poderia reintroduzi-lo. Corrige a ocorrencia, nao a causa — o que FND-04 §10.2 etapa 5 proibe expressamente ("correcao do efeito **e** correcao da causa") |
| Custo | Baixo |
| Avaliacao | C1 **falha** · C2 baixo · C3 alto · C4 satisfeito |

### Alternativa C — Fazer `CAP-qualidade` verificar `CAP-governanca`

| Campo | Conteudo |
|---|---|
| Descricao | Acrescentar `CAP-qualidade` → `verifica` → `CAP-governanca` ao mapa |
| A favor | Nomeia um verificador permanente dentro do proprio catalogo |
| Contra | **Viola RL-05 diretamente.** `CAP-qualidade` ja declara `depende-de: CAP-governanca` (mapa oficial, nivel 2). Acrescentar `verifica` na mesma direcao criaria exatamente o par que RL-05 proibe: quem verifica passaria a depender do verificado. Resolveria um defeito criando outro, mais grave |
| Custo | Baixo |
| Avaliacao | C1 satisfeito · C2 **falha** · C3 alto · C4 satisfeito |

### Alternativa Z — Nao fazer nada

| Campo | Conteudo |
|---|---|
| O que acontece | A redacao permanece; a leitura literal continua contrariando LV-03 |
| Custo real da inacao | Nenhum hoje — nao houve autoverificacao. Cresce quando existirem agentes: um agente de DEP-GOV lendo o catalogo literalmente concluiria que pode verificar o proprio trabalho, e a violacao seria **autorizada por norma** |
| Por que nao venceu | Achado de severidade alta com correcao conhecida e barata nao se mantem aberto por conveniencia (FND-04 §8) |

## 5. Decisao

**Decidimos proibir explicitamente a autoverificacao**, por meio de:

1. **RM-06 de FND-09 §6.3 passa a proibir o par reflexivo** de `verifica`: nenhuma entidade
   verifica a si propria, em nenhum estrato. A regra e escrita **uma unica vez**, no
   documento que governa relacoes entre tipos.

2. **FND-08 §5.2 recebe ponteiro, nao repeticao**: RL-05 ganha uma linha remetendo a RM-06,
   preservando MM-01.

3. **Correcao de redacao** em `capabilities/README.md` §5 e em `CAP-governanca.md` §9:
   `CAP-governanca` verifica **todas as demais**.

4. **Declaracao de quem verifica o que DEP-GOV produz**, sem criar relacao de Capability:
   a conformidade de artefato produzido por DEP-GOV e verificada por **revisor independente
   de papel distinto** — na pratica DEP-QAR, atuando por mudanca conforme FND-04 §3 — e, em
   materia constitucional, pelo **Soberano** como ratificador. Sao papeis por mudanca
   (FND-04 §3), **nao** relacao permanente entre Capabilities; por isso nao incidem em RL-05.

## 6. Justificativa

A Alternativa A vence pelos quatro criterios. A Alternativa B falha no criterio bloqueante:
corrigir a ocorrencia sem corrigir a causa e exatamente o que o rito de incidente proibe.

A Alternativa C revela por que a solucao correta **nao** esta na camada de Capabilities:
`CAP-qualidade` depende de `CAP-governanca`, e portanto nao pode verifica-la sem violar
RL-05. A independencia da Guarda (ES-02) nao e garantida por outra Capability — e garantida
pela **separacao de papeis por mudanca** (FND-04 §3.1) e, em ultima instancia, pelo Soberano,
a quem a Guarda responde diretamente (FND-02 §2.1).

**Sobre C4 (bloqueante):** a regra e universal — vale para `CAP`, `DEP`, `AGT` e qualquer
entidade futura —, logo pertence ao Meta Model. FND-08 apenas aponta para ela. Escreve-la nos
dois documentos criaria segunda fonte de verdade (MM-01).

**Tradeoff aceito:** o sistema passa a nao ter nenhuma Capability que verifique
`CAP-governanca` de forma permanente. Aceita-se isso porque a alternativa — criar essa
relacao — violaria RL-05, e porque a Constituicao ja resolve o caso por outro mecanismo: a
Guarda responde ao Nivel 0 diretamente, e quem verifica seu produto e o revisor independente
da mudanca, nao uma competencia superior.

## 7. Impacto

| Dimensao | Impacto |
|---|---|
| Departamentos afetados | DEP-GOV (redacao da Capability custodiada); DEP-QAR (papel de revisor confirmado) |
| Componentes afetados | Nenhum — nao existe componente vinculado |
| Camadas de memoria a atualizar | EST (catalogo) |
| Decisoes superadas | Nenhuma. ADR-0002 e ADR-0003 sao **complementados** |
| Documentos a atualizar | FND-09 v1.1.0 (§6.3 RM-06) · FND-08 v1.2.0 (§5.2 ponteiro) · `capabilities/README.md` §5 · `CAP-governanca.md` §9 |
| Custo e dependencia criados | Nenhum |
| Ganho PI-14 | **Organizacao:** a independencia da verificacao deixa de depender de leitura caridosa da norma |

## 8. Evidencias

| # | Evidencia | Origem | Confianca | O que discrimina |
|---|---|---|---|---|
| E1 | `capabilities/README.md` §5 declara `CAP-governanca` verificando "todas" | Leitura direta | **Alta — verificavel** | Sustenta o problema |
| E2 | `CAP-governanca.md` §9 repete a mesma formulacao | Leitura direta | **Alta — verificavel** | Confirma que nao e erro isolado de um documento |
| E3 | `CAP-qualidade` declara `depende_de: [CAP-governanca]` no mapa oficial | `capabilities/README.md` §4, nivel 2 | **Alta — verificavel** | **Elimina a Alternativa C** por RL-05 |
| E4 | Nenhuma norma vigente proibia o par reflexivo de `verifica` | FND-08 §5.2, FND-09 §6.3 | Alta | Sustenta que a correcao e de causa, nao de ocorrencia |
| E5 | Achado M1 registrado por DEP-QAR, independente de DEP-GOV | Revisao arquitetural do Meta Model | Alta | Origem do ADR |

**Evidencia ausente, declarada (VD-05):** nao ha nenhum caso observado de autoverificacao
efetiva. A correcao previne uma violacao **possivel pela norma**, nao repara uma ocorrida.

## 9. Riscos e mitigacao

| # | Risco | Probabilidade | Impacto | Mitigacao |
|---|---|---|---|---|
| R1 | A proibicao do auto-loop invalidar relacao legitima ainda nao imaginada | Baixa | Baixo | Nenhuma relacao vigente usa par reflexivo; a excecao, se surgir, entra por C2 acrescentando par permitido (FND-09 §11.3) |
| R2 | Ficar sem verificador permanente de `CAP-governanca` | Media | Medio | Papel de revisor independente por mudanca (FND-04 §3) + Soberano como ratificador; declarado em §5, item 4 |
| R3 | **Esta decisao estar errada** — a regra ser rigida demais | Baixa | Baixo | Reversao trivial (§10) |

## 10. Plano de reversao

| Campo | Conteudo |
|---|---|
| Como desfazer | ADR de revogacao superando este; RM-06 volta a redacao anterior por versao MENOR de FND-09 |
| Custo da reversao | **Trivial** — a decisao acrescenta uma restricao e corrige tres linhas de redacao; nenhum artefato depende dela |
| Por que a reversao e trivial (Tipo 2) | Nao cria componente, nao cria dependencia, nao altera escopo de Capability, nao tem consumidor |
| Quem executa | DEP-GOV, sob aprovacao de DEP-EXE |

## 11. Classificacao

| Campo | Valor |
|---|---|
| Classe de mudanca | **C2** — altera regra de relacao no Meta Model e redacao do catalogo |
| Tipo de reversibilidade | **Tipo 2** — reversao trivial, sem consumidores |
| Decisor | DEP-EXE |
| Ratificador | **Nao aplicavel** — C2 Tipo 2 nao exige ratificacao do Soberano (FND-07 §2.3) |
| Data da decisao | 2026-07-28 |
| Data de vigencia | 2026-07-28 |

> **RFC dispensada.** FND-04 §2 permite dispensar a RFC em C2 quando a alternativa unica for
> obvia **e** DEP-GOV concordar por escrito. Concordancia registrada em §13. Ainda assim,
> tres alternativas reais foram analisadas em §4, satisfazendo VD-01.

## 12. Revisao

| Campo | Conteudo |
|---|---|
| Gatilho temporal | 2027-01-28 — revisao semestral da Fundacao |
| Gatilho por evento | Criacao da primeira Capability de dominio `GAR` alem das tres atuais: verificar se o verificador dela esta nomeado |
| Gatilho por evento | Criacao do primeiro agente de DEP-GOV: verificar se a Carta declara quem revisa o que ele produz |
| Sinal de que esta decisao deu errado | Aparecer relacao legitima que exija par reflexivo; ou artefato de DEP-GOV aprovado sem revisor de papel distinto |
| Responsavel pela revisao | DEP-QAR |

## 13. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Origem | Achado **M1** da [revisao arquitetural do Meta Model](../foundation/revisao-arquitetural-meta-model-2026-07-28.md) §4.6 |
| Decisoes superadas | Nenhuma |
| Decisoes relacionadas | [ADR-0002](ADR-0002-adocao-da-camada-de-capabilities.md) (catalogo) e [ADR-0003](ADR-0003-adocao-do-enterprise-meta-model.md) (RM-06) — complementados |
| Artefatos alterados | FND-09 v1.1.0; FND-08 v1.2.0; `capabilities/README.md`; `CAP-governanca.md` |
| Concordancia de DEP-GOV com a dispensa de RFC | Registrada: *"a alternativa e unica e obvia — norma nao pode permitir o que LV-03 proibe. DEP-GOV concorda com a dispensa e declara-se impedido de propor ou aprovar, por ser custodio da Capability afetada."* — 2026-07-28 |
| Registros de memoria | Camada EST — correcao do mapa de verificacao |

---

## Checklist de validade (FND-07 §4.1)
- [x] VD-01 — 3 alternativas reais + "nao fazer nada"
- [x] VD-02 — criterios declarados antes da escolha (§3 antes de §4)
- [x] VD-03 — nenhuma alternativa de palha (B e C sao respostas naturais ao problema)
- [x] VD-04 — tradeoff aceito explicito (§6)
- [x] VD-05 — ausencia de ocorrencia real declarada (§8)
- [x] VD-06 — reversao declarada trivial, com justificativa (Tipo 2)
- [x] VD-07 — impacto em cascata mapeado e executado (§7)
- [x] VD-08 — data e responsavel presentes
- [x] VD-09 — gatilhos de revisao definidos (§12)
