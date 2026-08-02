---
id: CAP-aprendizado-organizacional
titulo: Aprendizado Organizacional
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
dominio: COG
classe: nucleo
maturidade: experimental
custodio: DEP-KMS
exercentes: [DEP-KMS]
depende_de: [CAP-conhecimento]
consumida_por: [CAP-qualidade, CAP-engenharia-de-agentes]
especializa: null
---

# Aprendizado Organizacional (CAP-aprendizado-organizacional)

## Proposito
Converter experiencia vivida em capacidade futura: extrair causa, generalizar licao,
declarar quando ela se aplica e quando nao, e fazer com que a proxima ocorrencia seja
mensuravelmente melhor. E a competencia que realiza a Visao V2.

## Escopo
A competencia de transformar o que aconteceu — sucesso, falha, incidente, surpresa — em
conhecimento acionavel e calibracao, com condicoes de aplicabilidade explicitas.

| Item | Definicao |
|---|---|
| Dominio | `COG` — Cognicao Organizacional |
| Classe estrategica | `nucleo` |
| Maturidade | `experimental` |
| Custodio | DEP-KMS |
| Exercentes | DEP-KMS; todos contribuem materia-prima |

## Responsaveis
| Papel | Quem |
|---|---|
| Custodio (unico) | DEP-KMS |
| Exercentes | DEP-KMS |
| Autoridade de evolucao | DEP-KMS, com parecer de DEP-GOV |
| Ratificador | SOBERANO |

---

## 1. Identidade (A-01)
| Campo | Valor |
|---|---|
| ID | `CAP-aprendizado-organizacional` |
| Nome | Aprendizado Organizacional |
| Dominio | COG |
| Classe | nucleo |
| Maturidade | experimental |
| Especializa | nenhuma |

## 2. Missao (A-03)
> Garantir que a organizacao nunca pague duas vezes pelo mesmo erro, e que o que funcionou
> seja reproduzivel por quem nao estava presente.

## 3. Limites (A-05)
| **Nao** abrange | Pertence a |
|---|---|
| Persistir, indexar e recuperar registros | `CAP-conhecimento` |
| Verificar se uma entrega esta correta | `CAP-qualidade` |
| Registrar violacao de norma e sua correcao | `CAP-governanca` |
| Descobrir fatos novos sobre o mundo externo | `CAP-pesquisa` |
| Calibrar o comportamento de agentes especificos | `CAP-engenharia-de-agentes` |

> **Fronteira com `CAP-pesquisa`:** esta Capability aprende com o que a organizacao
> **viveu**; aquela descobre o que a organizacao **ainda nao sabe** sobre o mundo.
>
> **Fronteira com `CAP-conhecimento`:** aquela guarda e devolve; esta **produz a licao** que
> sera guardada.

## 4. Responsabilidades (A-06)
| # | A organizacao e capaz de... |
|---|---|
| R1 | Identificar causa, e nao sintoma, do que ocorreu |
| R2 | Generalizar a licao sem transformar caso unico em regra universal |
| R3 | Declarar as condicoes em que a licao se aplica **e em que nao se aplica** |
| R4 | Definir a acao que decorre da licao, com dono |
| R5 | Calibrar heuristicas de estimativa e de risco pela experiencia |
| R6 | Refutar licao anterior diante de evidencia nova, preservando o historico |
| R7 | Reconhecer quando um ganho previsto (PI-14) nao se confirmou |

## 5. Entradas (A-07)
| Entrada | Origem | Obrigatoria? |
|---|---|---|
| Reportes de trabalho concluido | todas as Capabilities | Sim |
| Incidentes e sua analise de causa | `CAP-governanca`, `CAP-operacoes` | Sim |
| Resultado observado de decisoes | `CAP-conhecimento` | Sim |
| Vereditos de revisao independente | `CAP-qualidade` | Sim |

## 6. Saidas (A-08)
| Saida | Consumida por |
|---|---|
| Licao com condicoes e acao | todas |
| Antipadrao identificado | `CAP-qualidade`, `CAP-arquitetura` |
| Heuristica calibrada | `CAP-estrategia`, `CAP-coordenacao` |
| Calibracao de execucao | `CAP-engenharia-de-agentes` |
| Sinal de ganho PI-14 nao confirmado | `CAP-governanca` |

## 7. Artefatos produzidos (A-09)
| Tipo de artefato | Exemplo |
|---|---|
| Memoria (`MEM-APR`) | Licao com situacao, causa, condicoes e acao |
| Relatorio | Postmortem, retrospectiva de ciclo |

## 8. Dependencias (A-10)
| Capability | Relacao | Por que |
|---|---|---|
| `CAP-conhecimento` | depende-de | Licao sem registro recuperavel nao produz efeito |

## 9. Consumidores (A-11)
| Capability | Relacao | O que consome |
|---|---|---|
| `CAP-estrategia` | consome-saida-de | Heuristicas e apostas que nao funcionaram |
| `CAP-qualidade` | depende-de | Antipadroes e falhas conhecidas |
| `CAP-engenharia-de-agentes` | depende-de | Calibracao do que produz bom resultado |
| `CAP-produto` | consome-saida-de | Hipoteses invalidadas e padroes de uso |

## 10. Indicadores (A-12)
| # | Indicador | Direcao | Como se mede | Estado |
|---|---|---|---|---|
| I1 | Trabalhos encerrados com licao registrada | → 100% | Verificacao em QG-5 | nao medido |
| I2 | Latencia entre evento e licao gravada | ↓ | Data do evento × data do registro | nao medido |
| I3 | Licoes recuperadas antes de trabalho semelhante | ↑ | Consulta registrada em QG-0 | nao medido |
| I4 | Reincidencia da mesma causa raiz | → 0 | Comparacao entre incidentes | nao medido |
| I5 | Licoes sem secao de condicoes ou de acao | → 0 | Auditoria de registro APR | nao medido |

## 11. Criterios de evolucao (A-13)
| Movimento | Gatilho | Ganho PI-14 |
|---|---|---|
| Especializar | Aprendizado sobre execucao de agentes divergir do aprendizado sobre negocio | Reuso |
| Especializar | Postmortem de incidente virar volume proprio, distinto de retrospectiva | Organizacao |
| Fundir | Deixar de ser distinguivel de `CAP-conhecimento` na pratica | Organizacao |
| Depreciar | **Nunca** — a competencia sustenta a Visao V2 |

## 12. Historico de maturidade
| Data | De | Para | Evidencia | Instrumento |
|---|---|---|---|---|
| 2026-07-28 | proposta | experimental | Catalogo aprovado; nenhum ciclo operacional concluido, logo nenhuma licao extraida | ADR-0002 |

## 13. Rastreabilidade
| Campo | Conteudo |
|---|---|
| ADR de criacao | ADR-0002 |
| RFC de origem | RFC-0001 |
| Normas que exerce | [FND-06 §3.5](../foundation/06-arquitetura-memoria.md) |
| Componentes vinculados | nenhum ainda |
