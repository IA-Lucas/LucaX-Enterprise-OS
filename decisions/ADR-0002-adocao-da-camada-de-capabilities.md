---
id: ADR-0002-adocao-da-camada-de-capabilities
titulo: Adotar a camada de Capabilities como camada intermediaria entre a Constituicao e a estrutura operacional
tipo: adr
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-EXE
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0001]
substitui: []
substituido_por: null
classe_mudanca: C3
tipo_decisao: 1
supera: []
superado_por: null
---

# ADR-0002: Adotar a camada de Capabilities

## Proposito

Registrar a decisao de criar a camada de Capabilities do LucaX Enterprise OS — o documento
normativo FND-08, o tipo de componente `CAP`, o catalogo inicial e a regra de vinculacao
obrigatoria — e as emendas em cascata que ela exige na Fundacao.

## Escopo

Aplica-se a toda a arquitetura organizacional. Nao cria departamento, agente, skill,
workflow, produto, codigo nem infraestrutura.

## Responsaveis

| Papel | Quem |
|---|---|
| Proponente | DEP-EXE |
| Revisor independente | DEP-QAR |
| Guardiao (classe e conformidade) | DEP-GOV |
| Aprovador | SOBERANO |
| Ratificador | **SOBERANO** (C3 e Tipo 1) |
| Executor | DEP-GOV |

---

## 1. Contexto

ADR-0001 estabeleceu a Fundacao: sete documentos que definem por que a organizacao existe,
quem responde por que, como as coisas se chamam, como mudam, como se comunicam, como se
lembram e como se decide.

Nenhum desses documentos responde **o que a organizacao sabe fazer**. A competencia existe
hoje apenas implicitamente, dissolvida na missao de cada departamento — e portanto acoplada
a estrutura que a hospeda.

O momento importa: a fase seguinte criara Cartas de departamento e, depois, agentes. Se
esses componentes nascerem ligados apenas a estrutura, a competencia permanecera invisivel
como entidade propria, e o custo de extrai-la depois crescera com cada componente criado.

## 2. Problema / Pergunta de decisao

O LucaX deve adotar uma camada normativa de Capabilities, com catalogo proprio e vinculacao
obrigatoria de componentes, antes de construir a estrutura operacional?

## 3. Criterios de decisao

> Definidos antes do exame das alternativas (CD-01). Herdados de [RFC-0001 §4](../rfcs/RFC-0001-camada-de-capabilities.md).

| # | Criterio | Peso | Como se mede |
|---|---|---|---|
| C1 | Sobrevive a reorganizacao estrutural | Alto | Competencia continua descrita apos mudanca de departamento |
| C2 | Torna lacunas detectaveis antes da falha | Alto | Existe catalogo comparavel com a missao |
| C3 | Cria rastreabilidade transversal nos dois sentidos | Alto | De componente a competencia e vice-versa |
| C4 | Nao duplica definicao existente na Fundacao | **Bloqueante** | Nenhuma secao reescreve FND-01 a FND-07 |
| C5 | Custo de manutencao proporcional | Medio | Gerido pelos ritos ja existentes, sem instrumento novo |

## 4. Alternativas consideradas

### Alternativa A — Camada de Capabilities com catalogo e vinculacao obrigatoria
| Campo | Conteudo |
|---|---|
| Descricao | FND-08 + tipo `CAP` + catalogo em `capabilities/` + vinculo obrigatorio |
| A favor | Unica que satisfaz C1, C2 e C3 juntos; competencia deixa de depender da estrutura |
| Contra | Exige emenda C3; acrescenta tipo de componente e custo de manutencao das Cartas |
| Custo | 1 documento normativo, 1 template, 23 Cartas, 6 emendas em cascata |
| Risco | Capabilities virarem copia dos departamentos (R1) |
| Avaliacao | C1 alto · C2 alto · C3 alto · C4 satisfeito · C5 medio |

### Alternativa B — Competencias descritas dentro das Cartas de departamento
| Campo | Conteudo |
|---|---|
| Descricao | Cada departamento lista o que sabe fazer; sem catalogo separado |
| A favor | Custo quase nulo; sem emenda C3; sem tipo novo |
| Contra | Nao resolve C1 — competencia morre com a reorganizacao. Nao resolve C2 — sem visao de conjunto, lacuna so aparece na falha. Competencia exercida por duas areas seria descrita duas vezes, violando MM-01 |
| Custo | Baixo agora; alto na primeira reorganizacao |
| Risco | Alto — reproduz exatamente o defeito que se quer evitar |
| Avaliacao | C1 baixo · C2 baixo · C3 baixo · C4 satisfeito · C5 alto |

### Alternativa C — Catalogo descritivo, sem vinculacao obrigatoria
| Campo | Conteudo |
|---|---|
| Descricao | Catalogo existe como referencia; componentes nao precisam se vincular |
| A favor | Resolve C1 e parcialmente C2; custo menor que A |
| Contra | Nao resolve C3 — sem vinculo nao ha rastreabilidade nos dois sentidos. Pior: nada obriga o catalogo a acompanhar a realidade, e catalogo desatualizado engana quem o consulta |
| Custo | Medio |
| Risco | Medio-alto — vira documento decorativo |
| Avaliacao | C1 alto · C2 medio · C3 **baixo** · C4 satisfeito · C5 medio |

### Alternativa Z — Nao fazer nada
| Campo | Conteudo |
|---|---|
| O que acontece | A estrutura operacional e construida sem camada de competencia |
| Custo real da inacao | Cresce com cada componente criado sem vinculo — mesma assimetria reconhecida em ADR-0001 §6. Extrair a camada depois exige revisitar todo componente ja criado |
| Por que nao venceu | O custo de adiar e estritamente crescente, e a fase seguinte ja comecaria a acumula-lo |

## 5. Decisao

**Decidimos adotar a camada de Capabilities do LucaX Enterprise OS**, composta de:

1. **FND-08 — Enterprise Capability Framework**, incorporado a Fundacao;
2. o tipo de componente **`CAP`**, com prefixo, localizacao e template proprios;
3. o **catalogo inicial de 23 Capabilities**, em `capabilities/`, distribuidas em 7 dominios;
4. a **regra de vinculacao obrigatoria**: nenhum Departamento, Agente, Subagente, Skill,
   Workflow ou Produto pode existir sem vinculo a ao menos uma Capability;
5. as **emendas em cascata** em FND-01, FND-02, FND-03, FND-04 e FND-06 (§7).

## 6. Justificativa

A Alternativa A vence pelos tres criterios de maior peso. O ponto decisivo esta em C3, onde
A e C divergem: **um catalogo sem vinculo obrigatorio nao tem mecanismo que o force a
acompanhar a realidade.** Documento que ninguem e obrigado a manter desatualiza, e catalogo
de competencias desatualizado e pior que ausente — afirma que a organizacao sabe fazer algo
que talvez ja nao saiba, violando o espirito de PI-10.

A vinculacao obrigatoria e o que transforma o catalogo de descricao em **estrutura viva**:
como todo componente precisa se vincular, e como o vinculo e verificado em QG-0 e na
auditoria de integridade referencial, o catalogo e consultado por necessidade, nao por
disciplina.

Sobre C4 (bloqueante), o teste foi aplicado explicitamente: Capability responde "o que a
organizacao sabe fazer"; departamento responde "quem responde por isso". Sao perguntas
diferentes com respostas diferentes. Onde havia risco real de duplicacao — governanca,
comunicacao, memoria, qualidade — as Cartas correspondentes **referenciam** as normas
vigentes por ID em vez de reescreve-las (MM-01, FND-03 §7.1).

**Tradeoff aceito:** a organizacao passa a manter 23 artefatos adicionais e a exigir um
campo a mais em todo componente futuro. Aceita-se esse custo permanente de manutencao em
troca de que a competencia sobreviva a qualquer reorganizacao e de que lacunas sejam
detectaveis antes de causarem falha.

**Ressalva de DEP-GOV incorporada:** a mudanca foi classificada como **C3**, e nao C2, por
alterar a hierarquia normativa (FND-01 §10) e a propria Fundacao. Tratar como C2 teria sido
irregular — a ressalva esta registrada em RFC-0001 §10 e foi acatada integralmente.

## 7. Impacto

| Dimensao | Impacto |
|---|---|
| Departamentos afetados | Os nove — cada um passa a ser custodio e/ou exercente de Capabilities |
| Componentes afetados | Todo componente futuro passa a declarar `capabilities:` |
| Camadas de memoria a atualizar | **EST** — o catalogo e conhecimento estrategico permanente |
| Decisoes superadas | Nenhuma. ADR-0001 e **complementado**, nao superado |
| Documentos a atualizar | FND-01 (§10 hierarquia, §11 glossario), FND-02 (§9.1 escada, §10 restricoes), FND-03 (§2 IDs, §3 componentes, §4 frontmatter, §7 diretorios, §8 vocabulario), FND-04 (§6 pre-condicoes), FND-06 (§3.1 conteudo da camada EST) |
| Artefatos criados | FND-08; TPL-capability; 23 Cartas `CAP-*`; `capabilities/README.md`; revisao arquitetural |
| Custo e dependencia criados | Manutencao de 23 Cartas + campo obrigatorio em todo componente. **Nenhuma dependencia externa.** |
| Ganho PI-14 | **Organizacao:** competencia deixa de ser implicita e ganha fronteira nomeada. **Reuso:** catalogo aplicavel a qualquer produto futuro sem adaptacao. **Reducao de contexto:** o vinculo permite carregar apenas a competencia pertinente, em vez de varrer a estrutura. |

## 8. Evidencias

| # | Evidencia | Origem | Confianca | O que discrimina |
|---|---|---|---|---|
| E1 | Nenhum documento da Fundacao responde "o que a organizacao sabe fazer" | Leitura de FND-01 a FND-07, 2026-07-28 | Alta | Elimina Z; confirma que a camada nao duplica |
| E2 | FND-02 descreve 9 dominios de responsabilidade, mas nao permite verificar cobertura de competencia contra a missao | FND-02 §3 | Alta | Sustenta o problema P3 (lacunas invisiveis) |
| E3 | A assimetria de custo por adiamento ja foi reconhecida e aceita como argumento em ADR-0001 §6 | ADR-0001 | Alta | Sustenta decidir agora, nao depois |
| E4 | Diretriz do Soberano de que nenhum componente exista sem vinculo a Capability | Instrucao direta, 2026-07-28 | Alta | Elimina a Alternativa C |
| E5 | Diretriz do Soberano de que a arquitetura se especialize por ganho (PI-14) | ADR-0001 E3 | Alta | Sustenta os criterios de evolucao de FND-08 §7 |

**Evidencia ausente, declarada (VD-05):** nao ha, nesta data, nenhuma reorganizacao
estrutural ocorrida no LucaX que comprove empiricamente o beneficio C1, nem lacuna detectada
por catalogo que comprove C2. **Os ganhos declarados sao previstos, nao observados.** Esta
e a mesma fragilidade de ADR-0001 e a razao pela qual §12 fixa gatilhos de confirmacao.

## 9. Riscos e mitigacao

| # | Risco | Probabilidade | Impacto | Mitigacao |
|---|---|---|---|---|
| R1 | Capabilities viram espelho dos departamentos com outro nome | **Alta** | Alto | Testes TC-1 a TC-6 (FND-08 §1.1); invariante CI-01; revisao arquitetural obrigatoria; o catalogo adotado tem 23 Capabilities contra 9 departamentos, e nenhuma correspondencia 1:1 |
| R2 | Catalogo inflado por antecipacao | Media | Medio | Antipadroes de criacao (FND-08 §7.1); maturidade `experimental` marca o que ainda nao e exercido |
| R3 | Cartas viram burocracia nao consultada | Media | Alto | Vinculacao obrigatoria + verificacao em QG-0 (VC-04) |
| R4 | Duplicacao com normas da Fundacao | Media | **Alto** | C4 bloqueante; Cartas referenciam normas por ID; verificado na revisao arquitetural |
| R5 | Sobreposicao entre Capabilities vizinhas | **Alta** | Medio | Atributo Limites (A-05) obrigatorio, nomeando a Capability dona de cada exclusao |
| R6 | **Esta decisao estar errada** — a camada ser peso sem retorno | Media | Alto | Gatilhos de §12; consolidacao e prevista e legitima (FND-08 §7.3); reversao detalhada em §10 |

## 10. Plano de reversao

| Campo | Conteudo |
|---|---|
| Como desfazer | ADR de revogacao superando este; remocao da regra de vinculacao (§8 de FND-08); FND-08 passa a `revogado`; emendas em cascata reverteis por nova versao MAIOR de cada documento afetado |
| Custo da reversao | **Baixo nesta data** — nenhum departamento, agente, skill, workflow ou produto foi criado ainda, logo nenhum componente possui vinculo a desfazer |
| Janela em que ainda e possivel | A reversao encarece a cada componente vinculado. Enquanto o catalogo nao tiver consumidores, e barata |
| Reversao parcial | Preferivel e possivel: manter o catalogo como referencia e remover apenas a vinculacao obrigatoria — equivale a recuar da Alternativa A para a C |
| Quem executa | DEP-GOV, sob ratificacao do Soberano |
| Backup necessario (PI-07) | Copia datada de `foundation/` e `capabilities/` antes de qualquer revogacao |

## 11. Classificacao

| Campo | Valor |
|---|---|
| Classe de mudanca | **C3** — altera a hierarquia normativa e a propria Fundacao |
| Tipo de reversibilidade | **Tipo 1** — cria regra vinculante para todo componente futuro |
| Decisor | SOBERANO |
| Ratificador | SOBERANO |
| Data da decisao | 2026-07-28 |
| Data de vigencia | 2026-07-28 |

## 12. Revisao

| Campo | Conteudo |
|---|---|
| Gatilho temporal | 2027-01-28 — revisao semestral da Fundacao (FND-04 §8) |
| Gatilho por evento | Primeira reorganizacao estrutural: verificar se **nenhuma competencia se perdeu** (confirma C1) |
| Gatilho por evento | Primeira lacuna detectada por revisao de catalogo em vez de por falha (confirma C2) |
| Gatilho por confirmacao de ganho PI-14 | Na revisao estrutural, medir se o vinculo reduziu o contexto necessario para iniciar trabalho |
| Sinal de que esta decisao deu errado | Cartas de Capability nao sao consultadas em QG-0; vinculos declarados de forma generica so para cumprir a regra; catalogo desatualizado por mais de um horizonte |
| Responsavel pela revisao | DEP-EXE com DEP-QAR; DEP-GOV verifica conformidade |

## 13. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Origem | [RFC-0001](../rfcs/RFC-0001-camada-de-capabilities.md), aceita em 2026-07-28 |
| Decisoes superadas | Nenhuma |
| Decisoes relacionadas | [ADR-0001](ADR-0001-adocao-da-fundacao-organizacional.md) — complementada, nao superada |
| Artefatos criados | FND-08; TPL-capability; 23 Cartas de Capability; catalogo e mapa de dependencias; revisao arquitetural |
| Emendas em cascata | FND-01 v1.1.0 · FND-02 v1.1.0 · FND-03 v1.1.0 · FND-04 v1.1.0 · FND-06 v1.1.0 |
| Registros de memoria | Camada EST — o catalogo integralmente |

---

## Checklist de validade (FND-07 §4.1)
- [x] VD-01 — 3 alternativas reais + "nao fazer nada"
- [x] VD-02 — criterios declarados antes da escolha (herdados da RFC)
- [x] VD-03 — nenhuma alternativa de palha (B e C sao praticas correntes e defensaveis)
- [x] VD-04 — tradeoff aceito explicito (§6)
- [x] VD-05 — ausencia de evidencia empirica declarada (§8)
- [x] VD-06 — plano de reversao presente, com reversao parcial (Tipo 1)
- [x] VD-07 — impacto em cascata mapeado e executado (§7)
- [x] VD-08 — data e responsavel presentes
- [x] VD-09 — gatilhos de revisao definidos (§12)

---

## Ratificacao do Soberano

Esta decisao e C3 e Tipo 1: exige ato explicito do Soberano (PI-01, PI-06).

| Campo | Conteudo |
|---|---|
| Ratificado por | SOBERANO (Lucas) |
| Data | 2026-07-28 |
| Forma | Determinacao direta e escrita, na abertura desta fase |
| Texto invocado | *"Nenhum Departamento, Agente, Skill, Workflow ou Produto podera existir sem estar vinculado a pelo menos uma Capability."* |

### Observacao de conformidade (DEP-GOV)

A determinacao invocada e ato soberano real e datado, e ela propria estabelece a regra de
vinculacao — nucleo desta decisao. Mas antecede o texto final aqui ratificado.

Vale a mesma ressalva de ADR-0001: discordando o Soberano de qualquer definicao adotada,
esta ADR deve ser **superada** pelo rito de FND-07 §7, nunca editada (LV-04). Ate la, a
camada de Capabilities vigora integralmente.

| Campo | Conteudo |
|---|---|
| Confirmado apos leitura? | |
| Data | |
| Ajustes solicitados | |
