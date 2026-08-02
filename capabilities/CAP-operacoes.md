---
id: CAP-operacoes
titulo: Operacoes
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
dominio: SUS
classe: habilitadora
maturidade: experimental
custodio: DEP-OPS
exercentes: [DEP-OPS]
depende_de: [CAP-infraestrutura, CAP-engenharia]
consumida_por: []
especializa: null
---

# Operacoes (CAP-operacoes)

## Proposito
Manter funcionando o que ja existe, com previsibilidade: executar rotina, detectar
anomalia, responder a incidente e garantir continuidade. E a competencia que faz o
construido continuar valendo depois da entrega.

## Escopo
A competencia de transformar procedimento em rotina confiavel, monitorar estado, agir sobre
desvio, conduzir incidente ate a causa e assegurar continuidade.

| Item | Definicao |
|---|---|
| Dominio | `SUS` — Sustentacao |
| Classe estrategica | `habilitadora` |
| Maturidade | `experimental` |
| Custodio | DEP-OPS |
| Exercentes | DEP-OPS |

## Responsaveis
| Papel | Quem |
|---|---|
| Custodio (unico) | DEP-OPS |
| Exercentes | DEP-OPS |
| Autoridade de evolucao | DEP-OPS, com parecer de DEP-GOV |
| Ratificador | SOBERANO |

---

## 1. Identidade (A-01)
| Campo | Valor |
|---|---|
| ID | `CAP-operacoes` |
| Nome | Operacoes |
| Dominio | SUS |
| Classe | habilitadora |
| Maturidade | experimental |
| Especializa | nenhuma |

## 2. Missao (A-03)
> Garantir que o que ja existe continue funcionando, e que quando parar de funcionar a
> organizacao saiba antes do usuario.

## 3. Limites (A-05)
| **Nao** abrange | Pertence a |
|---|---|
| Construir ou alterar estruturalmente o que opera | `CAP-engenharia` |
| Prover e dimensionar o ambiente de execucao | `CAP-infraestrutura` |
| Priorizar e alocar o trabalho | `CAP-coordenacao` |
| **Verificar** que o backup e integro e restauravel | `CAP-seguranca` (PI-05) |
| Extrair a licao do incidente | `CAP-aprendizado-organizacional` |
| Verificar se a entrega esta correta | `CAP-qualidade` |

> **Fronteira com `CAP-infraestrutura`:** aquela **prove a plataforma**; esta **opera o que
> roda sobre ela**. Provisionar ambiente e daquela; executar a rotina diaria e desta.
>
> **Fronteira com `CAP-seguranca`:** esta **executa** o backup; aquela **verifica** que ele
> serve. Executar e verificar nao se concentram no mesmo papel.

## 4. Responsabilidades (A-06)
| # | A organizacao e capaz de... |
|---|---|
| R1 | Transformar procedimento em rotina reproduzivel por quem nao a criou |
| R2 | Monitorar estado e detectar anomalia antes do impacto |
| R3 | Conduzir incidente: conter, corrigir efeito e identificar causa |
| R4 | Executar backup e registrar sua execucao |
| R5 | Manter continuidade diante de falha parcial |
| R6 | Reconhecer quando o desvio exige mudanca estrutural, e escalar em vez de remediar |
| R7 | Reportar estado corrente de forma que a coordenacao possa decidir |

## 5. Entradas (A-07)
| Entrada | Origem | Obrigatoria? |
|---|---|---|
| Artefato construido e pronto para operar | `CAP-engenharia` | Sim |
| Ambiente de execucao | `CAP-infraestrutura` | Sim |
| Prioridade e alocacao | `CAP-coordenacao` | Sim |
| Requisitos de protecao e backup | `CAP-seguranca` | Sim |

## 6. Saidas (A-08)
| Saida | Consumida por |
|---|---|
| Estado operacional corrente | `CAP-coordenacao` |
| Runbook de rotina | proprios exercentes, futuros agentes |
| Registro e conducao de incidente | `CAP-aprendizado-organizacional`, `CAP-governanca` |
| Registro de execucao de backup | `CAP-seguranca` |
| Sinal de uso real | `CAP-produto`, `CAP-dados` |

## 7. Artefatos produzidos (A-09)
| Tipo de artefato | Exemplo |
|---|---|
| Memoria (`MEM-OPR`) | Runbook, estado corrente, registro de backup |
| Workflow (`WFL`) | Rotina recorrente formalizada |
| Relatorio | Status operacional, postmortem |

## 8. Dependencias (A-10)
| Capability | Relacao | Por que |
|---|---|---|
| `CAP-infraestrutura` | depende-de | Nao se opera o que nao tem onde rodar |
| `CAP-engenharia` | depende-de | Nao se opera o que nao foi construido |

## 9. Consumidores (A-11)
| Capability | Relacao | O que consome |
|---|---|---|
| `CAP-coordenacao` | consome-saida-de | Estado do trabalho e bloqueios |
| `CAP-produto` | consome-saida-de | Sinal de uso real |
| `CAP-aprendizado-organizacional` | consome-saida-de | Incidentes e sua conducao |
| `CAP-seguranca` | verifica *(inversa)* | Verifica backup e continuidade |

## 10. Indicadores (A-12)
| # | Indicador | Direcao | Como se mede | Estado |
|---|---|---|---|---|
| I1 | Anomalias detectadas pela organizacao antes do usuario | → 100% | Origem da deteccao | nao medido |
| I2 | Incidentes fechados com causa corrigida, nao so efeito | → 100% | Verificacao de fechamento | sem ocorrencia |
| I3 | Rotinas executaveis por quem nao as criou | → 100% | Teste de runbook | nao medido |
| I4 | Backups executados e registrados conforme previsto | → 100% | Registro em `MEM-OPR` | nao medido |
| I5 | Desvios remediados repetidamente sem escalar a mudanca estrutural | → 0 | Recorrencia do mesmo remedio | nao medido |

## 11. Criterios de evolucao (A-13)
| Movimento | Gatilho | Ganho PI-14 |
|---|---|---|
| Especializar | Resposta a incidente e rotina programada divergirem em cadencia | Organizacao |
| Especializar | Suporte a usuario surgir como responsabilidade propria | Organizacao |
| Fundir | Deixar de ser distinguivel de `CAP-infraestrutura` na pratica | Organizacao |
| Promover a `nucleo` | Se a continuidade se tornar a promessa central ao publico | — |

## 12. Historico de maturidade
| Data | De | Para | Evidencia | Instrumento |
|---|---|---|---|---|
| 2026-07-28 | proposta | experimental | Catalogo aprovado; nada em operacao | ADR-0002 |

## 13. Rastreabilidade
| Campo | Conteudo |
|---|---|
| ADR de criacao | ADR-0002 |
| RFC de origem | RFC-0001 |
| Normas que exerce | [FND-06 §3.4](../foundation/06-arquitetura-memoria.md) |
| Componentes vinculados | nenhum ainda |
