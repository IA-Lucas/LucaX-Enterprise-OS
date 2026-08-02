---
id: RFC-0001-camada-de-capabilities
titulo: Introduzir uma camada de Capabilities entre a Constituicao e a estrutura operacional
tipo: rfc
versao: 1.0.0
status: aprovado
camada_memoria: nao-aplicavel
autor: DEP-EXE
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: null
decisoes_relacionadas: [ADR-0002]
substitui: []
substituido_por: null
classe_mudanca: C3
prazo_analise: 2026-07-28
---

# RFC-0001: Camada de Capabilities

## Proposito
Propor a criacao de uma camada normativa de **Capabilities** — competencias permanentes da
organizacao — situada entre a Constituicao e a futura estrutura operacional.

## Escopo
Abrange a definicao do conceito, sua taxonomia, ciclo de vida, relacoes, propriedade e
regras de evolucao, alem da regra de vinculacao obrigatoria de componentes. Nao abrange a
criacao de departamentos, agentes, skills ou workflows.

## Responsaveis
| Papel | Quem |
|---|---|
| Proponente | DEP-EXE |
| Areas que devem se manifestar | DEP-GOV (conformidade), DEP-QAR (sobreposicao e lacuna), DEP-KMS (custodia do catalogo) |
| Aprovador | SOBERANO |
| Prazo de manifestacao | 2026-07-28 |

---

## 1. Situacao atual

A Fundacao (FND-01 a FND-07, ratificada por ADR-0001) definiu **quem responde por que**
(departamentos), **como algo muda** (governanca), **como se nomeia** (taxonomia), **como se
comunica**, **como se lembra** e **como se decide**.

Nao definiu **o que a organizacao sabe fazer**. Hoje, a competencia so existe implicitamente,
diluida na missao de cada departamento.

## 2. Problema

Sem uma camada explicita de competencia, tres defeitos surgem assim que a estrutura
operacional comecar a ser construida:

| # | Defeito | Consequencia |
|---|---|---|
| P1 | **Competencia amarrada a estrutura.** O que a empresa sabe fazer so existe descrito dentro da Carta de um departamento. | Reorganizar um departamento apaga ou fragmenta o registro da competencia. A empresa "esquece" o que sabe ao se reorganizar. |
| P2 | **Sem eixo de rastreabilidade transversal.** Agentes, skills e workflows nascerao ligados a departamentos, nao a competencias. | Impossivel responder "o que exatamente a organizacao sabe fazer?" e "o que exerce esta competencia?" sem varrer todo o repositorio. |
| P3 | **Lacunas invisiveis.** Nao havendo catalogo do que se deve saber fazer, a ausencia de uma competencia so aparece quando um trabalho falha por falta dela. | Descoberta de lacuna sempre reativa, sempre cara. |

Evidencia do problema: a estrutura de FND-02 descreve nove dominios de responsabilidade,
mas nenhum documento vigente permite listar as competencias da organizacao nem verificar se
elas cobrem o que a missao exige.

## 3. Pergunta de decisao

O LucaX deve adotar uma camada normativa de Capabilities, com catalogo proprio e vinculacao
obrigatoria de todos os componentes, antes de construir a estrutura operacional?

## 4. Criterios de avaliacao

| # | Criterio | Peso | Como se mede |
|---|---|---|---|
| C1 | Sobrevive a reorganizacao estrutural | Alto | A competencia continua descrita apos mudanca de departamento |
| C2 | Torna lacunas detectaveis antes da falha | Alto | Ha catalogo comparavel com a missao |
| C3 | Cria rastreabilidade transversal | Alto | De componente a competencia, e de competencia a componentes |
| C4 | Nao duplica definicao ja existente na Fundacao | **Bloqueante** | Nenhuma secao repete FND-01 a FND-07 |
| C5 | Custo de manutencao proporcional | Medio | Numero de artefatos gerido pelos ritos ja existentes |

## 5. Opcoes

### Opcao A — Camada de Capabilities com catalogo proprio e vinculacao obrigatoria
| Campo | Conteudo |
|---|---|
| Descricao | Novo tipo de componente (`CAP`), documento normativo proprio (FND-08), catalogo em `capabilities/`, vinculo obrigatorio de todo componente a ao menos uma Capability |
| A favor | Resolve P1, P2 e P3; competencia torna-se independente da estrutura; catalogo permite revisao de cobertura; vinculo cria a espinha dorsal de rastreabilidade |
| Contra | Acrescenta um documento fundacional e um tipo de componente; exige emenda C3 a hierarquia normativa; custo de manter as Cartas |
| Custo | Um documento normativo, um template, N Cartas de Capability, emendas em cascata |
| Quem e afetado | Todos os departamentos; todo componente futuro |

### Opcao B — Descrever competencias dentro das Cartas de departamento
| Campo | Conteudo |
|---|---|
| Descricao | Cada Carta de departamento lista as competencias que exerce; nao ha catalogo separado |
| A favor | Custo quase nulo; nenhum tipo novo; nenhuma emenda C3 |
| Contra | **Nao resolve P1** — a competencia continua morrendo com a reorganizacao; **nao resolve P3** — lacuna nao aparece porque nao ha visao de conjunto; competencia exercida por duas areas seria descrita duas vezes, violando MM-01 |
| Custo | Baixo agora, alto na primeira reorganizacao |
| Quem e afetado | Departamentos |

### Opcao C — Catalogo descritivo sem vinculacao obrigatoria
| Campo | Conteudo |
|---|---|
| Descricao | Catalogo de Capabilities existe como referencia, mas componentes nao precisam se vincular |
| A favor | Resolve P1 e parcialmente P3; custo menor que A; nao exige vinculo em cada componente |
| Contra | **Nao resolve P2** — sem vinculo, nao ha rastreabilidade nos dois sentidos; catalogo sem vinculo tende a desatualizar, porque nada o obriga a acompanhar a realidade; vira documento decorativo |
| Custo | Medio |
| Quem e afetado | Quem consultar o catalogo, se consultar |

### Opcao Z — Nao fazer nada
| Campo | Conteudo |
|---|---|
| Consequencia | A estrutura operacional e construida sem camada de competencia; P1, P2 e P3 se materializam |
| Custo da inacao | Cresce com cada componente criado sem vinculo — o mesmo padrao de assimetria de custo ja reconhecido em ADR-0001 §6 |

## 6. Recomendacao do proponente

**Opcao A.** E a unica que satisfaz C1, C2 e C3 simultaneamente. A Opcao C falha no ponto
decisivo: catalogo que nada obriga a manter atualizado deixa de refletir a realidade e passa
a enganar quem o consulta — pior que nao existir. A Opcao B falha no problema que motivou a
proposta: acopla competencia a estrutura, exatamente o que se quer evitar.

Sobre C4 (bloqueante): a camada de Capabilities **nao duplica** a Fundacao porque responde a
uma pergunta que nenhum documento vigente responde. Departamento responde "quem"; Capability
responde "o que se sabe fazer". Onde houvesse risco de duplicacao — governanca, comunicacao,
memoria — as Capabilities correspondentes **referenciam** as normas existentes em vez de
reescreve-las (MM-01, FND-03 §7.1).

## 7. Impacto previsto

| Dimensao | Impacto |
|---|---|
| Departamentos | Todos passam a ser custodios ou exercentes de Capabilities |
| Componentes | Todo componente futuro declara `capabilities:` no frontmatter |
| Normas afetadas | FND-01 §10 e §11 (hierarquia e glossario), FND-02 (relacao estrutura×competencia), FND-03 (§2, §3, §4, §7), FND-04 (§6), FND-06 (§3.1) |
| Camadas de memoria | EST — o catalogo e conhecimento estrategico |
| Ganho PI-14 pretendido | **Organizacao:** competencia deixa de ser implicita. **Reuso:** catalogo reutilizavel por qualquer produto futuro. **Reducao de contexto:** vinculo permite carregar so a competencia pertinente a tarefa, em vez de varrer a estrutura inteira. |
| Sinal que comprovara o ganho | Primeira reorganizacao estrutural em que nenhuma competencia se perde; primeira lacuna detectada por revisao de catalogo, e nao por falha |

## 8. Riscos

| # | Risco | Impacto | Mitigacao |
|---|---|---|---|
| R1 | Capabilities viram copia dos departamentos, com outro nome | Alto | Testes TC-1 a TC-6; revisao arquitetural obrigatoria de sobreposicao |
| R2 | Catalogo inflado por antecipacao | Medio | Antipadroes de criacao (FND-08 §7.1); maturidade `experimental` para o nao exercido |
| R3 | Cartas viram burocracia sem uso | Medio | Vinculacao obrigatoria (§8) faz o catalogo ser consultado em QG-0 |
| R4 | Duplicacao com normas da Fundacao | **Alto** | C4 bloqueante; Capabilities referenciam normas, nao as reescrevem |
| R5 | Emenda C3 a hierarquia sem necessidade real | Medio | Esta RFC e a analise de impacto exigidas pelo rito C3 |

## 9. Perguntas em aberto

| Pergunta | Dono da resposta | Bloqueia? |
|---|---|---|
| Quantas Capabilities o catalogo inicial deve ter? | DEP-EXE, na revisao arquitetural | Nao — resolvido no ADR |
| Departamentos serao redesenhados para espelhar Capabilities? | SOBERANO | **Nao** — e explicitamente rejeitado: CI-01 separa as camadas |
| Produtos existentes precisarao ser revinculados? | — | Nao — nao ha produtos nesta data |

## 10. Manifestacoes

| Area | Posicao | Fundamento | Data |
|---|---|---|---|
| DEP-GOV | Apoia com ressalva | Exige que a mudanca seja tratada como **C3**, por alterar a hierarquia normativa (FND-01 §10) e a propria Fundacao. Sem isso, a adocao seria irregular. | 2026-07-28 |
| DEP-QAR | Apoia | Risco R1 e R4 sao reais mas mitigaveis por revisao arquitetural obrigatoria ao fim da fase. | 2026-07-28 |
| DEP-KMS | Apoia | Catalogo pertence a camada EST; custodia compativel com o papel de curadoria. | 2026-07-28 |

## 11. Resultado

| Campo | Conteudo |
|---|---|
| Decisao | **aceita** |
| ADR gerado | [ADR-0002](../decisions/ADR-0002-adocao-da-camada-de-capabilities.md) |
| Ressalva incorporada | Classificada como **C3, Tipo 1**, conforme exigido por DEP-GOV |
| Data | 2026-07-28 |
| Responsavel | DEP-EXE |
