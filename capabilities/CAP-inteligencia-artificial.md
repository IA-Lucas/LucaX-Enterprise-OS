---
id: CAP-inteligencia-artificial
titulo: Inteligencia Artificial
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
classe: nucleo
maturidade: experimental
custodio: DEP-ENG
exercentes: [DEP-ENG]
depende_de: [CAP-dados, CAP-arquitetura, CAP-integracao]
consumida_por: [CAP-engenharia-de-agentes]
especializa: null
---

# Inteligencia Artificial (CAP-inteligencia-artificial)

## Proposito
Aplicar modelos de linguagem e sistemas de IA como substrato de trabalho da organizacao —
sabendo escolher, instruir, avaliar e limitar o que eles produzem. E a competencia sem a
qual uma empresa operada por IA nao passa de intencao.

## Escopo
A competencia de selecionar modelo adequado a tarefa, instruir com precisao, avaliar saida
de forma objetiva, reconhecer alucinacao e limite, e decidir quando **nao** usar IA.

| Item | Definicao |
|---|---|
| Dominio | `REA` — Realizacao |
| Classe estrategica | `nucleo` |
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
| ID | `CAP-inteligencia-artificial` |
| Nome | Inteligencia Artificial |
| Dominio | REA |
| Classe | nucleo |
| Maturidade | experimental |
| Especializa | nenhuma |

## 2. Missao (A-03)
> Garantir que a organizacao obtenha de sistemas de IA resultado confiavel e avaliavel — e
> que reconheca, antes de depender dele, quando o resultado nao e confiavel.

## 3. Limites (A-05)
| **Nao** abrange | Pertence a |
|---|---|
| Projetar e operar a forca de trabalho de agentes | `CAP-engenharia-de-agentes` |
| Modelar e qualificar o dado que alimenta os modelos | `CAP-dados` |
| Decidir a estrutura do sistema em que a IA se insere | `CAP-arquitetura` |
| Contratar e manter provedores de modelo | `CAP-integracao` |
| Verificar a entrega final de forma independente | `CAP-qualidade` |
| Avaliar risco legal do uso de IA | `CAP-juridico` |

> **Fronteira com `CAP-engenharia-de-agentes`:** esta Capability trata do **modelo como
> ferramenta** — escolha, instrucao, avaliacao. Aquela trata do **agente como trabalhador**
> — papel, escopo, autonomia, coordenacao. Um bom prompt e desta; uma boa Carta de agente e
> daquela.

## 4. Responsabilidades (A-06)
| # | A organizacao e capaz de... |
|---|---|
| R1 | Escolher modelo proporcional a tarefa, sem sub nem superdimensionar |
| R2 | Instruir com precisao suficiente para tornar a saida previsivel |
| R3 | Avaliar saida por criterio objetivo, nao por impressao |
| R4 | Reconhecer alucinacao, excesso de confianca e limite de competencia do modelo |
| R5 | Decidir quando **nao** usar IA, e justificar |
| R6 | Reduzir o contexto necessario sem degradar o resultado (PI-14) |
| R7 | Estimar e controlar o custo de inferencia como restricao declarada (PI-11) |

## 5. Entradas (A-07)
| Entrada | Origem | Obrigatoria? |
|---|---|---|
| Dado qualificado e com linhagem | `CAP-dados` | Sim |
| Estrutura tecnica e fronteiras | `CAP-arquitetura` | Sim |
| Contexto curado | `CAP-conhecimento` | Sim |
| Provedores e limites de uso | `CAP-integracao` | Sim |
| Calibracao do que produziu bom resultado | `CAP-aprendizado-organizacional` | Nao |

## 6. Saidas (A-08)
| Saida | Consumida por |
|---|---|
| Criterio de escolha de modelo por tarefa | `CAP-engenharia-de-agentes` |
| Metodo de avaliacao de saida | `CAP-qualidade`, `CAP-engenharia-de-agentes` |
| Limites conhecidos e modos de falha | `CAP-qualidade`, `CAP-arquitetura` |
| Custo de inferencia estimado | `CAP-financeiro` |

## 7. Artefatos produzidos (A-09)
| Tipo de artefato | Exemplo |
|---|---|
| ADR | Escolha de modelo, decisao de nao usar IA |
| Memoria (`MEM-TEC`) | Limites do modelo, modos de falha, tecnica que funcionou |
| Skill (`SKL`) | Procedimento de avaliacao de saida |

## 8. Dependencias (A-10)
| Capability | Relacao | Por que |
|---|---|---|
| `CAP-dados` | depende-de | Modelo alimentado por dado nao qualificado produz saida nao confiavel |
| `CAP-arquitetura` | depende-de | IA fora da estrutura decidida cria acoplamento nao previsto |
| `CAP-integracao` | depende-de | Sem provedor de modelo contratado e limitado, nao ha substrato para operar |

## 9. Consumidores (A-11)
| Capability | Relacao | O que consome |
|---|---|---|
| `CAP-engenharia-de-agentes` | depende-de | O substrato sobre o qual os agentes operam |
| `CAP-qualidade` | consome-saida-de | Metodo de avaliacao e limites conhecidos |
| `CAP-financeiro` | consome-saida-de | Custo de inferencia |

## 10. Indicadores (A-12)
| # | Indicador | Direcao | Como se mede | Estado |
|---|---|---|---|---|
| I1 | Saidas de IA aceitas sem avaliacao objetiva | → 0 | Verificacao em QG-3 | nao medido |
| I2 | Alucinacoes detectadas antes do consumo, nao depois | ↑ | Comparacao deteccao × incidente | nao medido |
| I3 | Contexto necessario por tarefa | ↓ | Volume de entrada por execucao | nao medido |
| I4 | Decisoes registradas de **nao** usar IA | ↑ | ADRs com essa conclusao | nao medido |
| I5 | Desvio entre custo de inferencia estimado e real | → 0 | Comparacao registrada | nao medido |

## 11. Criterios de evolucao (A-13)
| Movimento | Gatilho | Ganho PI-14 |
|---|---|---|
| Especializar | Avaliacao de saida virar disciplina propria, com metodo e cadencia distintos | Organizacao |
| Especializar | Engenharia de contexto divergir de engenharia de instrucao | Reducao de contexto |
| Fundir | Deixar de ser distinguivel de `CAP-engenharia-de-agentes` na pratica | Organizacao |
| Depreciar | **Nunca sem emenda C3** — classe `nucleo` (CL-05) |

## 12. Historico de maturidade
| Data | De | Para | Evidencia | Instrumento |
|---|---|---|---|---|
| 2026-07-28 | proposta | experimental | Catalogo aprovado; competencia ainda nao exercida sob metodo registrado | ADR-0002 |

## 13. Rastreabilidade
| Campo | Conteudo |
|---|---|
| ADR de criacao | ADR-0002 |
| RFC de origem | RFC-0001 |
| Normas que exerce | [FND-01 PI-11](../foundation/01-constituicao.md) — qualidade antes de custo |
| Componentes vinculados | nenhum ainda |
