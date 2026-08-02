---
id: CAP-design
titulo: Design
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
classe: habilitadora
maturidade: experimental
custodio: DEP-PRD
exercentes: [DEP-PRD]
depende_de: [CAP-produto]
consumida_por: []
especializa: null
---

# Design (CAP-design)

## Proposito
Dar forma ao que foi definido: decidir como o problema se apresenta a quem o vive, de modo
que a solucao seja compreensivel, usavel e coerente entre contextos.

## Escopo
A competencia de traduzir problema e criterio em forma, fluxo, linguagem e interacao —
incluindo a coerencia visual e verbal entre produtos.

| Item | Definicao |
|---|---|
| Dominio | `VAL` — Descoberta e Valor |
| Classe estrategica | `habilitadora` |
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
| ID | `CAP-design` |
| Nome | Design |
| Dominio | VAL |
| Classe | habilitadora |
| Maturidade | experimental |
| Especializa | nenhuma |

## 2. Missao (A-03)
> Garantir que a solucao correta tambem seja compreensivel e usavel por quem tem o problema,
> sem exigir que a pessoa entenda como o sistema funciona por dentro.

## 3. Limites (A-05)
| **Nao** abrange | Pertence a |
|---|---|
| Definir qual problema resolver e para quem | `CAP-produto` |
| Decidir a estrutura tecnica que sustenta a forma | `CAP-arquitetura` |
| Implementar a interface | `CAP-engenharia` |
| Descobrir contexto de uso e jornada | `CAP-pesquisa` |
| Definir mensagem e narrativa de mercado | `CAP-marketing` |
| Verificar se a forma atende ao criterio de aceite | `CAP-qualidade` |

> **Fronteira com `CAP-marketing`:** design cuida da coerencia **na experiencia do produto**;
> marketing, da coerencia **na mensagem ao mercado**. A identidade e compartilhada; o uso
> nao.

## 4. Responsabilidades (A-06)
| # | A organizacao e capaz de... |
|---|---|
| R1 | Traduzir problema e criterio em forma e fluxo compreensiveis |
| R2 | Manter coerencia de linguagem e interacao entre contextos e produtos |
| R3 | Reduzir o esforco cognitivo exigido de quem usa |
| R4 | Antecipar caso de borda, erro e estado vazio na propria forma |
| R5 | Justificar decisao de forma por criterio, nao por preferencia |
| R6 | Reaproveitar padroes de interacao ja validados |

## 5. Entradas (A-07)
| Entrada | Origem | Obrigatoria? |
|---|---|---|
| Spec, problema e criterios de aceite | `CAP-produto` | Sim |
| Contexto de uso e jornada | `CAP-pesquisa` | Nao |
| Restricoes tecnicas e viabilidade | `CAP-arquitetura` | Nao |
| Identidade e narrativa | `CAP-marketing` | Nao |

## 6. Saidas (A-08)
| Saida | Consumida por |
|---|---|
| Definicao de forma, fluxo e interacao | `CAP-engenharia` |
| Padroes de interacao reutilizaveis | `CAP-engenharia`, futuros produtos |
| Linguagem de interface | `CAP-marketing` |
| Tratamento de erro e estado limite | `CAP-engenharia`, `CAP-qualidade` |

## 7. Artefatos produzidos (A-09)
| Tipo de artefato | Exemplo |
|---|---|
| Spec (`SPC`) | Especificacao de forma e comportamento de interface |
| Memoria (`MEM-PRD`) | Padrao de interacao validado |
| ADR | Decisao de padrao de design |

## 8. Dependencias (A-10)
| Capability | Relacao | Por que |
|---|---|---|
| `CAP-produto` | depende-de | Desenhar sem problema definido produz forma sem funcao |

## 9. Consumidores (A-11)
| Capability | Relacao | O que consome |
|---|---|---|
| `CAP-engenharia` | consome-saida-de | Definicao de forma e comportamento a implementar |
| `CAP-marketing` | consome-saida-de | Linguagem e identidade da experiencia |

> **Nenhuma Capability depende **estruturalmente** desta.** Isso e deliberado: engenharia
> constroi sem superficie quando nao ha superficie. Por RL-06, a ausencia de consumidor
> **duro** por um horizonte inteiro tornaria esta Capability candidata a depreciacao — o
> gatilho a observar e a existencia de produto com superficie de interacao propria.

## 10. Indicadores (A-12)
| # | Indicador | Direcao | Como se mede | Estado |
|---|---|---|---|---|
| I1 | Reuso de padroes de interacao entre produtos | ↑ | Referencia a padrao existente | nao medido |
| I2 | Retrabalho de implementacao por forma mal definida | ↓ | Devolucoes com causa "design" | nao medido |
| I3 | Casos de borda previstos no design, nao descobertos na revisao | ↑ | Comparacao design × achados de QG-3 | nao medido |
| I4 | Decisoes de forma com criterio registrado | → 100% | Auditoria de ADR de design | nao medido |

## 11. Criterios de evolucao (A-13)
| Movimento | Gatilho | Ganho PI-14 |
|---|---|---|
| Especializar | Interface e sistema de identidade exigirem competencias distintas | Organizacao |
| Especializar | Design de interacao com agentes divergir do design de interface humana | Reuso |
| Fundir | Deixar de ser distinguivel de `CAP-produto` na pratica | Organizacao |
| Depreciar | Se todos os produtos passarem a nao ter superficie de interacao propria | — |

## 12. Historico de maturidade
| Data | De | Para | Evidencia | Instrumento |
|---|---|---|---|---|
| 2026-07-28 | proposta | experimental | Catalogo aprovado; nenhuma superficie desenhada | ADR-0002 |

## 13. Rastreabilidade
| Campo | Conteudo |
|---|---|
| ADR de criacao | ADR-0002 |
| RFC de origem | RFC-0001 |
| Componentes vinculados | nenhum ainda |
