---
id: CAP-financeiro
titulo: Financeiro
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
dominio: MER
classe: suporte
maturidade: experimental
custodio: DEP-EXE
exercentes: [DEP-EXE]
depende_de: [CAP-coordenacao, CAP-comercial]
consumida_por: []
especializa: null
---

# Financeiro (CAP-financeiro)

## Proposito
Manter a organizacao economicamente viavel: saber quanto custa operar, quanto entra, e
onde o recurso esta sendo consumido — para que a restricao de custo seja **declarada**, e
nunca decida em silencio.

## Escopo
A competencia de prever, acompanhar e limitar consumo de recurso; medir custo por unidade
de valor; e sustentar decisao de investimento com numero, nao com impressao.

| Item | Definicao |
|---|---|
| Dominio | `MER` — Mercado e Recursos |
| Classe estrategica | `suporte` |
| Maturidade | `experimental` |
| Custodio | DEP-EXE *(funcao Recursos/FIN, conforme FND-02)* |
| Exercentes | DEP-EXE |

## Responsaveis
| Papel | Quem |
|---|---|
| Custodio (unico) | DEP-EXE |
| Exercentes | DEP-EXE |
| Autoridade de evolucao | DEP-EXE, com parecer de DEP-GOV |
| Ratificador | SOBERANO |

---

## 1. Identidade (A-01)
| Campo | Valor |
|---|---|
| ID | `CAP-financeiro` |
| Nome | Financeiro |
| Dominio | MER |
| Classe | suporte |
| Maturidade | experimental |
| Especializa | nenhuma |

## 2. Missao (A-03)
> Garantir que a organizacao saiba o custo do que faz antes de comprometer, e que nenhuma
> escolha seja tomada por custo sem que isso esteja declarado.

## 3. Limites (A-05)
| **Nao** abrange | Pertence a |
|---|---|
| Decidir prioridade e alocacao de trabalho | `CAP-coordenacao` |
| Decidir direcao e portfolio | `CAP-estrategia` |
| Precificar e contratar | `CAP-comercial` |
| Escolher a ferramenta a adotar | `CAP-integracao` |
| Obrigacao fiscal e contabil formal | `CAP-juridico` + assessoria humana |
| **Vetar por custo uma escolha de qualidade** | ninguem — PI-11 |

> **Limite constitucional (PI-11):** esta Capability **informa e restringe**, mas nao
> substitui o criterio de qualidade. Custo e restricao declarada, nunca o criterio de
> decisao dominante. Uma escolha pode ser cara e ainda assim correta — cabe a esta
> Capability tornar o preco visivel, nao decidir por ele.

## 4. Responsabilidades (A-06)
| # | A organizacao e capaz de... |
|---|---|
| R1 | Prever o custo de um esforco antes de comprometer capacidade |
| R2 | Acompanhar consumo real contra o previsto |
| R3 | Definir e monitorar limites de gasto por finalidade |
| R4 | Medir custo por unidade de valor entregue |
| R5 | Tornar visivel o custo marginal de cada novo produto (OB-H3.1) |
| R6 | Declarar a restricao de custo em vez de deixa-la decidir em silencio (PI-11) |

## 5. Entradas (A-07)
| Entrada | Origem | Obrigatoria? |
|---|---|---|
| Alocacao de capacidade e prioridades | `CAP-coordenacao` | Sim |
| Receita e compromissos | `CAP-comercial` | Sim |
| Custo recorrente de dependencias | `CAP-integracao` | Sim |
| Custo de substrato | `CAP-infraestrutura` | Sim |
| Custo de inferencia | `CAP-inteligencia-artificial` | Sim |

## 6. Saidas (A-08)
| Saida | Consumida por |
|---|---|
| Previsao e limite de custo | `CAP-coordenacao`, `CAP-integracao`, `CAP-infraestrutura` |
| Consumo real contra previsto | `CAP-coordenacao`, Soberano |
| Custo por unidade de valor | `CAP-estrategia`, `CAP-produto` |
| Custo marginal por produto | `CAP-estrategia` |

## 7. Artefatos produzidos (A-09)
| Tipo de artefato | Exemplo |
|---|---|
| Relatorio | Consumo do ciclo, previsao, custo marginal |
| Memoria (`MEM-OPR`) | Consumo e limites do ciclo corrente |
| ADR | Decisao de limite de gasto |

## 8. Dependencias (A-10)
| Capability | Relacao | Por que |
|---|---|---|
| `CAP-coordenacao` | depende-de | Sem alocacao, nao ha contra o que medir consumo |
| `CAP-comercial` | depende-de | Sem receita e compromissos, a viabilidade nao se calcula |

## 9. Consumidores (A-11)
| Capability | Relacao | O que consome |
|---|---|---|
| `CAP-coordenacao` | consome-saida-de | Limites e consumo para priorizar |
| `CAP-estrategia` | consome-saida-de | Custo marginal e viabilidade |
| `CAP-integracao` | consome-saida-de | Limite aprovado antes de adotar |
| `CAP-infraestrutura` | consome-saida-de | Limite aprovado antes de provisionar |

## 10. Indicadores (A-12)
| # | Indicador | Direcao | Como se mede | Estado |
|---|---|---|---|---|
| I1 | Compromissos assumidos sem custo previsto | → 0 | Auditoria de decisao | **0** |
| I2 | Desvio entre custo previsto e real | → 0 | Comparacao por ciclo | nao medido |
| I3 | Custo marginal do enesimo produto | ↓ | Comparacao entre produtos (OB-H3.1) | nao medido |
| I4 | Escolhas em que o custo decidiu sem estar declarado | → 0 | Auditoria de ADR (PI-11) | **0** |
| I5 | Limites ultrapassados sem decisao registrada | → 0 | Monitoramento de limite | **0** |

## 11. Criterios de evolucao (A-13)
| Movimento | Gatilho | Ganho PI-14 |
|---|---|---|
| Promover a `habilitadora` | Quando houver receita recorrente ou custo operacional material | — |
| Especializar | Contabilidade formal e gestao de consumo divergirem em metodo | Organizacao |
| Especializar | Promocao da funcao FIN a departamento proprio (FND-02 §8.4) | Organizacao |
| Fundir | Deixar de ser distinguivel de `CAP-coordenacao` na pratica | Organizacao |

## 12. Historico de maturidade
| Data | De | Para | Evidencia | Instrumento |
|---|---|---|---|---|
| 2026-07-28 | proposta | experimental | Catalogo aprovado; nenhuma receita, nenhum custo recorrente contratado | ADR-0002 |

## 13. Rastreabilidade
| Campo | Conteudo |
|---|---|
| ADR de criacao | ADR-0002 |
| RFC de origem | RFC-0001 |
| Normas que exerce | [FND-01 PI-11](../foundation/01-constituicao.md), [FND-02 DEP-EXE funcao FIN](../foundation/02-estrutura-organizacional.md) |
| Componentes vinculados | nenhum ainda |
