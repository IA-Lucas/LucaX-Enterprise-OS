---
id: CAP-engenharia-de-agentes
titulo: Engenharia de Agentes
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
depende_de: [CAP-inteligencia-artificial, CAP-conhecimento, CAP-comunicacao, CAP-aprendizado-organizacional]
consumida_por: []
especializa: null
---

# Engenharia de Agentes (CAP-engenharia-de-agentes)

## Proposito
Projetar, calibrar e operar a **forca de trabalho de agentes** da organizacao: definir
papeis, escopos, limites de autonomia e coordenacao entre executores de IA. E a competencia
que distingue o LucaX de uma empresa que apenas usa IA.

## Escopo
A competencia de decidir que papel deve existir, o que ele **nao** pode fazer, quanto
contexto precisa, como se coordena com outros papeis e como sua qualidade e mantida ao
longo do tempo.

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
| ID | `CAP-engenharia-de-agentes` |
| Nome | Engenharia de Agentes |
| Dominio | REA |
| Classe | nucleo |
| Maturidade | experimental |
| Especializa | nenhuma |

## 2. Missao (A-03)
> Garantir que o trabalho da organizacao possa ser executado por agentes com resultado
> previsivel, escopo respeitado e autonomia que nunca excede a concedida.

## 3. Limites (A-05)
| **Nao** abrange | Pertence a |
|---|---|
| Escolher, instruir e avaliar o modelo subjacente | `CAP-inteligencia-artificial` |
| Curar o conhecimento que alimenta os agentes | `CAP-conhecimento` |
| Definir o protocolo de troca entre partes | `CAP-comunicacao` |
| Priorizar e alocar o trabalho que os agentes farao | `CAP-coordenacao` |
| Verificar de forma independente o que os agentes produzem | `CAP-qualidade` |
| Conceder autoridade acima da prevista em norma | **ninguem** — PI-01, LV-07 |
| Prover ambiente de execucao | `CAP-infraestrutura` |

> **Fronteira com `CAP-inteligencia-artificial`:** aquela responde "que modelo, com que
> instrucao, avaliado como?"; esta responde "que papel deve existir, com que escopo, que
> limite e que coordenacao?".
>
> **Fronteira com `CAP-coordenacao`:** esta projeta **quem pode executar**; aquela decide
> **o que sera executado e quando**.

## 4. Responsabilidades (A-06)
| # | A organizacao e capaz de... |
|---|---|
| R1 | Decidir que papel de execucao deve existir, e qual nao deve |
| R2 | Declarar o escopo de um agente **e o que nao lhe compete** |
| R3 | Atribuir nivel de autonomia proporcional ao risco, nunca acima do departamento |
| R4 | Determinar o contexto minimo que um papel precisa para agir corretamente |
| R5 | Coordenar multiplos agentes sem que a responsabilidade fique orfa |
| R6 | Calibrar comportamento a partir de resultado observado |
| R7 | Reconhecer quando um papel deve ser dividido, fundido ou aposentado |
| R8 | Garantir que nenhum agente amplie a propria autoridade (PI-01, LV-07) |

## 5. Entradas (A-07)
| Entrada | Origem | Obrigatoria? |
|---|---|---|
| Criterio de escolha de modelo e metodo de avaliacao | `CAP-inteligencia-artificial` | Sim |
| Pacote de contexto curado | `CAP-conhecimento` | Sim |
| Protocolo de canal, handoff e escalonamento | `CAP-comunicacao` | Sim |
| Calibracao do que produz bom resultado | `CAP-aprendizado-organizacional` | Sim |
| Norma de autonomia e separacao de poderes | `CAP-governanca` | Sim |

## 6. Saidas (A-08)
| Saida | Consumida por |
|---|---|
| Carta de agente e de subagente | `CAP-coordenacao`, `CAP-governanca` |
| Definicao de contexto minimo por papel | `CAP-conhecimento` |
| Arranjo de coordenacao entre papeis | `CAP-coordenacao` |
| Calibracao aplicada | `CAP-aprendizado-organizacional` |

## 7. Artefatos produzidos (A-09)
| Tipo de artefato | Exemplo |
|---|---|
| Carta de agente (`AGT`) / subagente (`SUB`) | Papel com escopo, limites e autonomia |
| Workflow (`WFL`) | Sequencia que encadeia papeis |
| Skill (`SKL`) | Procedimento reutilizavel entre papeis |
| ADR | Decisao de criar, dividir ou aposentar papel |

## 8. Dependencias (A-10)
| Capability | Relacao | Por que |
|---|---|---|
| `CAP-inteligencia-artificial` | depende-de | Sem dominio do substrato, o papel projetado nao se sustenta |
| `CAP-conhecimento` | depende-de | Agente sem contexto curado improvisa |
| `CAP-comunicacao` | depende-de | Agente sem protocolo produz trabalho orfao |
| `CAP-aprendizado-organizacional` | depende-de | Sem calibracao pelo resultado observado, o papel nao melhora |

## 9. Consumidores (A-11)
| Capability | Relacao | O que consome |
|---|---|---|
| `CAP-coordenacao` | consome-saida-de | Papeis disponiveis para alocacao |
| `CAP-qualidade` | verifica *(inversa)* | Verifica a saida dos agentes projetados |
| `CAP-governanca` | verifica *(inversa)* | Verifica que nenhum papel excede autoridade |

> Nenhuma Capability **depende** desta ainda: e a competencia mais nova do catalogo e
> nenhum papel foi criado. Espera-se que se torne dependencia de quase toda realizacao
> conforme H2 avance.

## 10. Indicadores (A-12)
| # | Indicador | Direcao | Como se mede | Estado |
|---|---|---|---|---|
| I1 | Agentes que atuaram fora do escopo declarado | → 0 | Auditoria de execucao vs. Carta | nao medido |
| I2 | Tentativas de operar acima da autonomia concedida | → 0 | Registro de incidente (LV-07) | nao medido |
| I3 | Contexto necessario por papel | ↓ | Volume do pacote por execucao (PI-14) | nao medido |
| I4 | Trabalho orfao apos handoff entre agentes | → 0 | Verificacao de aceite (HO-01) | nao medido |
| I5 | Reuso de papel entre produtos distintos | ↑ | Vinculo agente × produto | nao medido |
| I6 | Devolucoes em QG-3 de saida produzida por agente | ↓ | Registro de revisao | nao medido |

## 11. Criterios de evolucao (A-13)
| Movimento | Gatilho | Ganho PI-14 |
|---|---|---|
| Especializar | Projeto de papel e orquestracao de multiplos papeis divergirem em metodo | Organizacao |
| Especializar | Calibracao continua virar volume proprio, distinto do projeto | Organizacao |
| Especializar | Contexto por papel crescer a ponto de exigir engenharia de contexto propria | Reducao de contexto |
| Fundir | Deixar de ser distinguivel de `CAP-inteligencia-artificial` na pratica | Organizacao |
| Depreciar | **Nunca sem emenda C3** — classe `nucleo` e distintiva (CL-05) |

## 12. Historico de maturidade
| Data | De | Para | Evidencia | Instrumento |
|---|---|---|---|---|
| 2026-07-28 | proposta | experimental | Catalogo aprovado; **nenhum agente criado** — a fase de fundacao e esta o proibiram expressamente | ADR-0002 |

## 13. Rastreabilidade
| Campo | Conteudo |
|---|---|
| ADR de criacao | ADR-0002 |
| RFC de origem | RFC-0001 |
| Normas que exerce | [FND-03 §3.3–§3.4](../foundation/03-taxonomia.md), [FND-01 §7.2](../foundation/01-constituicao.md), [FND-05 §11](../foundation/05-framework-comunicacao.md) |
| Componentes vinculados | nenhum ainda |
