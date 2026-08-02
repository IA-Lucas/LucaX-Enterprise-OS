---
id: CAP-coordenacao
titulo: Coordenacao Organizacional
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
dominio: DIR
classe: habilitadora
maturidade: experimental
custodio: DEP-EXE
exercentes: [DEP-EXE]
depende_de: [CAP-estrategia, CAP-comunicacao]
consumida_por: [CAP-financeiro]
especializa: null
---

# Coordenacao Organizacional (CAP-coordenacao)

## Proposito
Converter direcao em trabalho efetivamente executado: priorizar, alocar capacidade,
sequenciar, arbitrar conflitos entre areas e cobrar resultado. E a competencia que impede
que a organizacao saiba para onde ir e mesmo assim nao chegue.

## Escopo
A competencia de decidir **o que primeiro, com quem e ate quando**, e de resolver disputas
de escopo, prioridade e recurso entre areas.

| Item | Definicao |
|---|---|
| Dominio | `DIR` — Direcao |
| Classe estrategica | `habilitadora` |
| Maturidade | `experimental` |
| Custodio | DEP-EXE |
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
| ID | `CAP-coordenacao` |
| Nome | Coordenacao Organizacional |
| Dominio | DIR |
| Classe | habilitadora |
| Maturidade | experimental |
| Especializa | nenhuma |

## 2. Missao (A-03)
> Garantir que a capacidade disponivel esteja sempre aplicada ao trabalho de maior valor
> segundo a direcao vigente, e que nenhum trabalho fique sem dono.

## 3. Limites (A-05)
| **Nao** abrange | Pertence a |
|---|---|
| Definir a direcao a ser servida | `CAP-estrategia` |
| Definir o conteudo tecnico do trabalho | `CAP-arquitetura` / `CAP-engenharia` |
| Definir o escopo do produto | `CAP-produto` |
| Julgar se a entrega passa | `CAP-qualidade` |
| Operar rotina recorrente ja definida | `CAP-operacoes` |
| Projetar quem executa (forca de trabalho de agentes) | `CAP-engenharia-de-agentes` |

> **Fronteira com `CAP-operacoes`:** coordenacao decide **o que sera feito e por quem**;
> operacoes **executa o que ja e rotina**. Coordenacao aloca; operacoes mantem.

## 4. Responsabilidades (A-06)
| # | A organizacao e capaz de... |
|---|---|
| R1 | Ordenar a fila de trabalho por valor conforme a direcao vigente |
| R2 | Alocar capacidade a esforcos concorrentes, com criterio explicito |
| R3 | Abrir e fechar ciclos de trabalho com cadencia previsivel |
| R4 | Arbitrar conflito de escopo, prioridade ou recurso entre areas |
| R5 | Cobrar resultado e identificar trabalho sem dono |
| R6 | Consolidar o estado da organizacao para o Soberano |

## 5. Entradas (A-07)
| Entrada | Origem | Obrigatoria? |
|---|---|---|
| Direcao vigente e criterios de sucesso | `CAP-estrategia` | Sim |
| Estado do trabalho em curso | `CAP-operacoes` | Sim |
| Protocolo de troca e escalonamento | `CAP-comunicacao` | Sim |
| Custo e limites de recurso | `CAP-financeiro` | Nao |
| Pedidos e propostas das areas | todas | Sim |

## 6. Saidas (A-08)
| Saida | Consumida por |
|---|---|
| Prioridade vigente | todas |
| Alocacao de capacidade | todas |
| Decisao de arbitragem | as areas em conflito |
| Briefing de trabalho | as areas executoras |
| Reporte consolidado | Soberano |

## 7. Artefatos produzidos (A-09)
| Tipo de artefato | Exemplo |
|---|---|
| Carta de projeto (`PRJ`) | Esforco temporario com criterio de encerramento |
| Relatorio | Reporte consolidado, estado de ciclo |
| Nota de Decisao | Arbitragem, mudanca de prioridade |

## 8. Dependencias (A-10)
| Capability | Relacao | Por que |
|---|---|---|
| `CAP-estrategia` | depende-de | Priorizar sem direcao e arbitrariedade |
| `CAP-comunicacao` | depende-de | Coordenar sem protocolo de troca produz trabalho orfao |

## 9. Consumidores (A-11)
| Capability | Relacao | O que consome |
|---|---|---|
| `CAP-financeiro` | depende-de | Alocacao contra a qual mede consumo |
| todas | coordena *(inversa)* | Esta Capability coordena todas as demais |

## 10. Indicadores (A-12)
| # | Indicador | Direcao | Como se mede | Estado |
|---|---|---|---|---|
| I1 | Trabalho ativo sem dono nomeado | → 0 | Varredura da camada OPR | nao medido |
| I2 | Ciclos fechados com portao pendente sem excecao | → 0 | Auditoria de fechamento | nao medido |
| I3 | Conflitos entre as mesmas duas areas, recorrentes | → 0 | Registro de arbitragem | nao medido |
| I4 | Tempo entre bloqueio detectado e desbloqueio decidido | ↓ | Registro de escalonamento | nao medido |
| I5 | Retrabalho por prioridade revertida no meio do ciclo | ↓ | Mudancas de fila apos abertura | nao medido |

## 11. Criterios de evolucao (A-13)
| Movimento | Gatilho | Ganho PI-14 |
|---|---|---|
| Especializar | Gestao de portfolio e alocacao de capacidade exigirem cadencias distintas | Organizacao |
| Especializar | Arbitragem virar volume proprio, separado da priorizacao | Organizacao |
| Fundir | Deixar de ser distinguivel de `CAP-estrategia` | Organizacao |
| Depreciar | Se a organizacao passar a operar com um unico fluxo, sem concorrencia por capacidade | — |
| Promover a `nucleo` | Se a coordenacao de multiplos produtos em paralelo se tornar o gargalo estrategico (H3) | — |

## 12. Historico de maturidade
| Data | De | Para | Evidencia | Instrumento |
|---|---|---|---|---|
| 2026-07-28 | proposta | experimental | Catalogo aprovado; nenhum ciclo de trabalho aberto ainda | ADR-0002 |

## 13. Rastreabilidade
| Campo | Conteudo |
|---|---|
| ADR de criacao | ADR-0002 |
| RFC de origem | RFC-0001 |
| Normas que exerce | [FND-02 §5](../foundation/02-estrutura-organizacional.md), [FND-05 §8](../foundation/05-framework-comunicacao.md) |
| Componentes vinculados | nenhum ainda |
