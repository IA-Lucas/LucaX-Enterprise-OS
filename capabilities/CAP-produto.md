---
id: CAP-produto
titulo: Produto
tipo: capability
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-EXE
proprietario: DEP-EXE
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0002]
substitui: []
substituido_por: null
dominio: VAL
classe: nucleo
maturidade: experimental
custodio: DEP-PRD
exercentes: [DEP-PRD]
depende_de: [CAP-pesquisa, CAP-estrategia]
consumida_por: [CAP-design, CAP-arquitetura, CAP-marketing, CAP-comercial]
especializa: null
---

# Produto (CAP-produto)

## Proposito
Definir **o que deve existir e por que**, transformando intencao em problema bem formulado
e resultado verificavel. E a competencia que realiza a Visao V1: converter direcao em algo
entregavel sem microgestao.

## Escopo
A competencia de enquadrar problema, definir publico, estabelecer criterios de aceite
verificaveis, declarar escopo negativo e ordenar valor dentro de um produto.

| Item | Definicao |
|---|---|
| Dominio | `VAL` — Descoberta e Valor |
| Classe estrategica | `nucleo` |
| Maturidade | `experimental` |
| Custodio | DEP-PRD |
| Exercentes | DEP-PRD |

## Responsaveis
| Papel | Quem |
|---|---|
| Custodio (unico) | DEP-PRD |
| Exercentes | DEP-PRD |
| Autoridade de evolucao | DEP-PRD, com parecer de DEP-GOV |
| Ratificador | SOBERANO |

---

## 1. Identidade (A-01)
| Campo | Valor |
|---|---|
| ID | `CAP-produto` |
| Nome | Produto |
| Dominio | VAL |
| Classe | nucleo |
| Maturidade | experimental |
| Especializa | nenhuma |

## 2. Missao (A-03)
> Garantir que a organizacao construa a coisa certa: que o problema esteja bem formulado e
> que exista criterio objetivo para saber se foi resolvido.

## 3. Limites (A-05)
| **Nao** abrange | Pertence a |
|---|---|
| Decidir **como** construir | `CAP-arquitetura` / `CAP-engenharia` |
| Decidir se o produto entra no portfolio | `CAP-estrategia` |
| Priorizar entre produtos concorrentes | `CAP-coordenacao` |
| Verificar se a entrega atende o criterio | `CAP-qualidade` |
| Desenhar a forma e a interacao | `CAP-design` |
| Descobrir os fatos que fundamentam a definicao | `CAP-pesquisa` |
| Comunicar o produto ao publico | `CAP-marketing` |

> **Fronteira com `CAP-estrategia`:** estrategia decide **se um produto deve existir**;
> produto decide **o que ele e e o que nao e**.

## 4. Responsabilidades (A-06)
| # | A organizacao e capaz de... |
|---|---|
| R1 | Enquadrar problema de forma que a solucao nao esteja embutida no enunciado |
| R2 | Definir publico e contexto de uso com precisao suficiente para decidir |
| R3 | Escrever criterio de aceite verificavel por terceiro sem consultar o autor |
| R4 | Declarar escopo negativo — o que o produto deliberadamente nao fara |
| R5 | Ordenar valor dentro do produto, com justificativa do que foi despriorizado |
| R6 | Formular hipotese com o teste que a confirmaria, e registrar sua refutacao |
| R7 | Definir o criterio de encerramento do produto na sua criacao |

## 5. Entradas (A-07)
| Entrada | Origem | Obrigatoria? |
|---|---|---|
| Decisao de portfolio e criterios de sucesso | `CAP-estrategia` | Sim |
| Evidencia sobre problema e publico | `CAP-pesquisa` | Sim |
| Hipoteses invalidadas e padroes de uso | `CAP-aprendizado-organizacional` | Nao |
| Viabilidade e custo tecnico | `CAP-arquitetura` | Nao |
| Sinal de uso e feedback | `CAP-operacoes`, `CAP-comercial` | Nao |

## 6. Saidas (A-08)
| Saida | Consumida por |
|---|---|
| Spec com criterios de aceite | `CAP-arquitetura`, `CAP-engenharia`, `CAP-qualidade` |
| Carta de produto | `CAP-coordenacao`, `CAP-marketing` |
| Escopo negativo | todas as Capabilities de realizacao |
| Roadmap e justificativa de despriorizacao | `CAP-coordenacao` |
| Definicao de sucesso do produto | `CAP-qualidade`, `CAP-comercial` |

## 7. Artefatos produzidos (A-09)
| Tipo de artefato | Exemplo |
|---|---|
| Spec (`SPC`) | Definicao do que deve existir e como verificar |
| Carta de produto (`PRO`) | Problema, publico, criterio de sucesso e de encerramento |
| Memoria (`MEM-PRD`) | Persona, hipotese, feedback, escopo negativo |
| ADR | Decisao de escopo |

## 8. Dependencias (A-10)
| Capability | Relacao | Por que |
|---|---|---|
| `CAP-pesquisa` | depende-de | Definir sem evidencia produz suposicao formalizada |
| `CAP-estrategia` | depende-de | Produto fora da direcao e esforco desperdicado |

## 9. Consumidores (A-11)
| Capability | Relacao | O que consome |
|---|---|---|
| `CAP-design` | depende-de | Problema e publico a partir dos quais desenha |
| `CAP-arquitetura` | depende-de | Spec e criterios de aceite |
| `CAP-marketing` | depende-de | O que o produto e, para comunicar sem prometer errado |
| `CAP-comercial` | depende-de | Proposta de valor |
| `CAP-qualidade` | consome-saida-de | Criterios contra os quais verifica |

## 10. Indicadores (A-12)
| # | Indicador | Direcao | Como se mede | Estado |
|---|---|---|---|---|
| I1 | Specs cujo criterio de aceite foi verificavel sem consultar o autor | → 100% | Verificacao em QG-1 | nao medido |
| I2 | Retrabalho causado por defeito de spec | ↓ | Devolucoes em QG-3 com causa "spec" | nao medido |
| I3 | Specs com escopo negativo declarado | → 100% | Auditoria de spec | nao medido |
| I4 | Hipoteses testadas antes da construcao | ↑ | Registro em `MEM-PRD` | nao medido |
| I5 | Reuso de spec ou criterio entre produtos | ↑ | Referencia cruzada | nao medido |

## 11. Criterios de evolucao (A-13)
| Movimento | Gatilho | Ganho PI-14 |
|---|---|---|
| Especializar | Descoberta e definicao exigirem cadencias incompativeis | Organizacao |
| Especializar | Portfolio de multiplos produtos tornar a gestao transversal distinta da definicao | Organizacao |
| Fundir | Deixar de ser distinguivel de `CAP-design` na pratica | Organizacao |
| Depreciar | **Nunca** — sem esta competencia a organizacao constroi a coisa errada com eficiencia |

## 12. Historico de maturidade
| Data | De | Para | Evidencia | Instrumento |
|---|---|---|---|---|
| 2026-07-28 | proposta | experimental | Catalogo aprovado; nenhum produto criado, nenhuma spec escrita | ADR-0002 |

## 13. Rastreabilidade
| Campo | Conteudo |
|---|---|
| ADR de criacao | ADR-0002 |
| RFC de origem | RFC-0001 |
| Normas que exerce | [FND-03 §3.6](../foundation/03-taxonomia.md), [FND-01 §6.2 QG-1](../foundation/01-constituicao.md) |
| Componentes vinculados | nenhum ainda |
