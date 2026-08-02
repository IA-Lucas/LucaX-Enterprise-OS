---
id: CAP-engenharia
titulo: Engenharia
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
dominio: REA
classe: habilitadora
maturidade: experimental
custodio: DEP-ENG
exercentes: [DEP-ENG]
depende_de: [CAP-arquitetura]
consumida_por: [CAP-operacoes]
especializa: null
---

# Engenharia (CAP-engenharia)

## Proposito
Construir o que foi especificado, dentro da estrutura decidida, de modo que funcione, seja
verificavel e possa ser mantido por quem nao o escreveu.

## Escopo
A competencia de transformar spec e arquitetura em artefato que funciona, com verificacao
propria, legibilidade e sustentabilidade ao longo do tempo.

| Item | Definicao |
|---|---|
| Dominio | `REA` — Realizacao |
| Classe estrategica | `habilitadora` |
| Maturidade | `experimental` |
| Custodio | DEP-ENG |
| Exercentes | DEP-ENG |

## Responsaveis
| Papel | Quem |
|---|---|
| Custodio (unico) | DEP-ENG |
| Exercentes | DEP-ENG |
| Autoridade de evolucao | DEP-ENG, com parecer de DEP-GOV |
| Ratificador | SOBERANO |

---

## 1. Identidade (A-01)
| Campo | Valor |
|---|---|
| ID | `CAP-engenharia` |
| Nome | Engenharia |
| Dominio | REA |
| Classe | habilitadora |
| Maturidade | experimental |
| Especializa | nenhuma |

## 2. Missao (A-03)
> Garantir que o que a organizacao decide construir passe a existir, funcionando, com prova
> de que funciona.

## 3. Limites (A-05)
| **Nao** abrange | Pertence a |
|---|---|
| Decidir a estrutura e os padroes | `CAP-arquitetura` |
| Decidir o que construir | `CAP-produto` |
| **Aprovar a propria entrega** | `CAP-qualidade` (PI-05) |
| Modelar dados de dominio | `CAP-dados` |
| Operar o que foi construido | `CAP-operacoes` |
| Prover ambiente de execucao | `CAP-infraestrutura` |
| Construir e calibrar agentes | `CAP-engenharia-de-agentes` |

> **Fronteira intransponivel:** esta Capability **nunca** verifica a propria saida. A
> verificacao independente e de `CAP-qualidade` (PI-05, LV-03). Autoverificacao interna
> existe, mas nao substitui nem dispensa o portao QG-3.

## 4. Responsabilidades (A-06)
| # | A organizacao e capaz de... |
|---|---|
| R1 | Implementar spec dentro da estrutura arquitetural decidida |
| R2 | Produzir verificacao junto com a construcao, nao depois |
| R3 | Escrever de modo legivel por quem nao participou |
| R4 | Estimar com base em heuristica calibrada, nao em otimismo |
| R5 | Reconhecer e declarar quando a spec e insuficiente, em vez de adivinhar |
| R6 | Manter o construido funcionando ao longo de mudancas sucessivas |
| R7 | Registrar divida assumida durante a construcao |

## 5. Entradas (A-07)
| Entrada | Origem | Obrigatoria? |
|---|---|---|
| Estrutura, padroes e decisoes arquiteturais | `CAP-arquitetura` | Sim |
| Spec e criterios de aceite | `CAP-produto` | Sim |
| Definicao de forma e comportamento | `CAP-design` | Nao |
| Modelo de dados | `CAP-dados` | Nao |
| Antipadroes e falhas conhecidas | `CAP-aprendizado-organizacional` | Nao |

## 6. Saidas (A-08)
| Saida | Consumida por |
|---|---|
| Artefato construido e funcionando | `CAP-qualidade`, `CAP-operacoes` |
| Verificacao propria e sua evidencia | `CAP-qualidade` |
| Registro de divida assumida | `CAP-arquitetura`, `CAP-coordenacao` |
| Estimativa e viabilidade de execucao | `CAP-coordenacao` |

## 7. Artefatos produzidos (A-09)
| Tipo de artefato | Exemplo |
|---|---|
| Memoria (`MEM-TEC`) | Divida assumida, armadilha encontrada |
| ADR | Decisao de implementacao com precedente |
| Relatorio | Reporte de entrega com evidencia |

## 8. Dependencias (A-10)
| Capability | Relacao | Por que |
|---|---|---|
| `CAP-arquitetura` | depende-de | Construir sem estrutura decidida produz sistema irreconciliavel |

## 9. Consumidores (A-11)
| Capability | Relacao | O que consome |
|---|---|---|
| `CAP-operacoes` | depende-de | O que sera operado e mantido |
| `CAP-qualidade` | verifica *(inversa)* | Verifica a saida desta Capability |
| `CAP-seguranca` | verifica *(inversa)* | Verifica risco na saida desta Capability |

## 10. Indicadores (A-12)
| # | Indicador | Direcao | Como se mede | Estado |
|---|---|---|---|---|
| I1 | Entregas aprovadas em QG-3 sem devolucao | ↑ | Registro de revisao | nao medido |
| I2 | Entregas com evidencia de verificacao propria | → 100% | Secao Evidencia do reporte | nao medido |
| I3 | Desvio entre estimativa e execucao real | → 0 | Comparacao registrada | nao medido |
| I4 | Divida assumida e registrada no momento | → 100% | `MEM-TEC` vs. achados posteriores | nao medido |
| I5 | Defeitos encontrados em producao que a verificacao propria deveria pegar | ↓ | Postmortem | nao medido |

## 11. Criterios de evolucao (A-13)
| Movimento | Gatilho | Ganho PI-14 |
|---|---|---|
| Especializar | Construcao de superficie e de nucleo exigirem competencias distintas | Organizacao |
| Especializar | Construcao assistida por agentes divergir estruturalmente da construcao direta | Reducao de contexto |
| Fundir | Deixar de ser distinguivel de `CAP-arquitetura` na pratica | Organizacao |
| Depreciar | Se toda construcao passar a ser feita por `CAP-engenharia-de-agentes` sem intervencao direta | — |

## 12. Historico de maturidade
| Data | De | Para | Evidencia | Instrumento |
|---|---|---|---|---|
| 2026-07-28 | proposta | experimental | Catalogo aprovado; nenhum artefato construido — a fase de fundacao proibiu codigo | ADR-0002 |

## 13. Rastreabilidade
| Campo | Conteudo |
|---|---|
| ADR de criacao | ADR-0002 |
| RFC de origem | RFC-0001 |
| Normas que exerce | [FND-01 §6.1 DoD](../foundation/01-constituicao.md) |
| Componentes vinculados | nenhum ainda |
