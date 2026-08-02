---
id: TPL-workflow
titulo: Template de Workflow
tipo: template
versao: 1.0.0
status: ativo
camada_memoria: nao-aplicavel
autor: DEP-GOV
proprietario: DEP-EXE
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0001]
substitui: []
substituido_por: null
---

# Template — Workflow

## Proposito
Padronizar sequencias definidas de etapas para produzir um resultado recorrente, conforme
[FND-03 §3.10](../03-taxonomia.md).

## Escopo
Trabalho recorrente com etapas, responsaveis e portoes definidos.

> **Nesta fase da fundacao nenhum workflow pode ser criado.** Este template existe para que
> a fase seguinte comece com o padrao pronto.

## Responsaveis
Proprietario: DEP-EXE · Conformidade: DEP-GOV · Verificacao: DEP-QAR.

## Instrucoes de uso
1. Grave em `workflows/WFL-<DEP>-<slug>.md`.
2. Workflow que atravessa departamentos declara o **dono do resultado final** (FND-02 §6).
3. Etapa que apenas transporta, sem transformar, e candidata a remocao (HO-05).

---
---
id: WFL-<DEP>-<slug>
titulo: <o resultado que este workflow produz>
tipo: workflow
versao: 1.0.0
status: rascunho
camada_memoria: nao-aplicavel
autor: <DEP-xxx>
proprietario: <DEP-xxx>
aprovador: DEP-EXE
criado_em: <AAAA-MM-DD>
atualizado_em: <AAAA-MM-DD>
revisao_prevista: <AAAA-MM-DD>
decisoes_relacionadas: [<ADR de criacao>]
substitui: []
substituido_por: null
gatilho: <o que dispara este workflow>
portoes: [<QG-x>, ...]
---

# <Nome do Workflow>

## Proposito
<Que resultado recorrente este workflow produz. Ate 3 frases.>

## Escopo
| Item | Definicao |
|---|---|
| Aplica-se a | |
| **Nao** se aplica a | |
| Dono do resultado final | <DEP-xxx> |

## Responsaveis
| Papel | Quem |
|---|---|
| Proprietario | |
| Dono do resultado final | |
| Verificacao | DEP-QAR |

## 1. Gatilho
| O que dispara | Quem dispara | Pre-condicoes |
|---|---|---|

## 2. Entradas
| Entrada | Origem | Obrigatoria? |
|---|---|---|

## 3. Etapas
| # | Etapa | Responsavel | Entrada | Saida | Portao |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |

## 4. Portoes
| Portao | Momento | Quem libera | Criterio |
|---|---|---|---|

## 5. Saidas
| Saida | Destinatario | Formato |
|---|---|---|

## 6. Criterio de conclusao
<Como se sabe que o workflow terminou com sucesso.>

## 7. Criterio de falha
| Falha | Como reconhecer | Onde retorna | Quem e acionado |
|---|---|---|---|

## 8. Handoffs internos
| De | Para | O que transfere | Criterio de aceite |
|---|---|---|---|

## 9. Memoria
| Etapa | Camada alimentada | O que grava |
|---|---|---|

## 10. Ganho PI-14
| Campo | Conteudo |
|---|---|
| Ganho declarado | |
| Sinal que motivou a criacao | |
| Data de reavaliacao | |

## 11. Criterio de descontinuacao
<Quando este workflow deixa de valer a pena, ou deve ser consolidado (FND-02 §9.3).>
