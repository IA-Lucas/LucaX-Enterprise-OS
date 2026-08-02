---
id: CAP-pesquisa
titulo: Pesquisa
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
depende_de: [CAP-conhecimento]
consumida_por: [CAP-produto]
especializa: null
---

# Pesquisa (CAP-pesquisa)

## Proposito
Reduzir incerteza antes de gastar: descobrir o que a organizacao ainda nao sabe sobre
publico, problema, mercado, concorrencia ou tecnologia, e devolver isso como evidencia
utilizavel em decisao.

## Escopo
A competencia de formular pergunta investigavel, escolher metodo proporcional a duvida,
coletar evidencia com proveniencia e concluir com grau de confianca declarado.

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
| ID | `CAP-pesquisa` |
| Nome | Pesquisa |
| Dominio | VAL |
| Classe | habilitadora |
| Maturidade | experimental |
| Especializa | nenhuma |

## 2. Missao (A-03)
> Garantir que decisoes caras sejam tomadas com evidencia proporcional ao seu custo, e que
> a incerteza remanescente seja declarada, nunca escondida.

## 3. Limites (A-05)
| **Nao** abrange | Pertence a |
|---|---|
| Decidir o que construir a partir do achado | `CAP-produto` |
| Aprender com a propria experiencia da organizacao | `CAP-aprendizado-organizacional` |
| Guardar e recuperar o que ja foi descoberto | `CAP-conhecimento` |
| Avaliar viabilidade tecnica de uma solucao | `CAP-arquitetura` |
| Testar mensagem e canal junto ao publico | `CAP-marketing` |
| Modelar e analisar dados operacionais proprios | `CAP-dados` |

> **Fronteira com `CAP-aprendizado-organizacional`:** esta Capability investiga o **mundo
> externo**; aquela extrai licao da **experiencia interna**.

## 4. Responsabilidades (A-06)
| # | A organizacao e capaz de... |
|---|---|
| R1 | Transformar duvida difusa em pergunta investigavel |
| R2 | Escolher metodo proporcional ao custo da decisao que depende dele |
| R3 | Coletar evidencia com proveniencia rastreavel |
| R4 | Distinguir fato observado de interpretacao |
| R5 | Concluir com grau de confianca declarado, incluindo "nao sabemos" |
| R6 | Reconhecer quando a pergunta ja foi respondida antes (consulta previa a memoria) |

## 5. Entradas (A-07)
| Entrada | Origem | Obrigatoria? |
|---|---|---|
| Pergunta ou incerteza a reduzir | `CAP-produto`, `CAP-estrategia` | Sim |
| O que ja se sabe | `CAP-conhecimento` | Sim |
| Fontes externas | externa | Sim |

## 6. Saidas (A-08)
| Saida | Consumida por |
|---|---|
| Achado com evidencia e confianca | `CAP-produto`, `CAP-estrategia` |
| Mapa de publico e de problema | `CAP-produto`, `CAP-design` |
| Panorama de concorrencia e mercado | `CAP-marketing`, `CAP-estrategia` |
| Declaracao de incerteza remanescente | quem decidir |

## 7. Artefatos produzidos (A-09)
| Tipo de artefato | Exemplo |
|---|---|
| Relatorio | Achado de pesquisa com fontes e confianca |
| Memoria (`MEM-PRD`) | Persona, contexto de uso, sinal de mercado |

## 8. Dependencias (A-10)
| Capability | Relacao | Por que |
|---|---|---|
| `CAP-conhecimento` | depende-de | Pesquisar o que ja se sabe e desperdicio (MM-04) |

## 9. Consumidores (A-11)
| Capability | Relacao | O que consome |
|---|---|---|
| `CAP-produto` | depende-de | Evidencia sobre problema e publico |
| `CAP-estrategia` | consome-saida-de | Sinais de mercado e contexto |
| `CAP-design` | consome-saida-de | Contexto de uso e jornada |
| `CAP-marketing` | consome-saida-de | Panorama de publico e concorrencia |

## 10. Indicadores (A-12)
| # | Indicador | Direcao | Como se mede | Estado |
|---|---|---|---|---|
| I1 | Decisoes C2/C3 com evidencia de pesquisa anexada | ↑ | Secao 8 dos ADRs | nao medido |
| I2 | Achados com proveniencia e confianca declaradas | → 100% | Auditoria de relatorio | nao medido |
| I3 | Pesquisas que repetiram investigacao ja registrada | → 0 | Consulta previa a memoria | nao medido |
| I4 | Hipoteses de produto refutadas antes da construcao | ↑ | Registro em `MEM-PRD` | nao medido |
| I5 | Custo da pesquisa × custo da decisao que a exigiu | proporcional | Comparacao registrada | nao medido |

## 11. Criterios de evolucao (A-13)
| Movimento | Gatilho | Ganho PI-14 |
|---|---|---|
| Especializar | Pesquisa de publico e pesquisa tecnica exigirem metodos incompativeis | Organizacao |
| Especializar | Vigilancia continua de mercado virar rotina propria | Organizacao |
| Fundir | Deixar de ser distinguivel de `CAP-produto` na pratica | Organizacao |
| Depreciar | Se toda decisao passar a ser tomada com evidencia ja disponivel internamente | — |

## 12. Historico de maturidade
| Data | De | Para | Evidencia | Instrumento |
|---|---|---|---|---|
| 2026-07-28 | proposta | experimental | Catalogo aprovado; nenhuma pesquisa conduzida | ADR-0002 |

## 13. Rastreabilidade
| Campo | Conteudo |
|---|---|
| ADR de criacao | ADR-0002 |
| RFC de origem | RFC-0001 |
| Normas que exerce | [FND-07 §4 secao 8](../foundation/07-framework-decisoes.md) |
| Componentes vinculados | nenhum ainda |
