---
id: CAP-comunicacao
titulo: Comunicacao Organizacional
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
classe: habilitadora
maturidade: experimental
custodio: DEP-EXE
exercentes: [DEP-EXE, DEP-KMS]
depende_de: [CAP-conhecimento]
consumida_por: [CAP-coordenacao, CAP-engenharia-de-agentes]
especializa: null
---

# Comunicacao Organizacional (CAP-comunicacao)

## Proposito
Transferir trabalho, contexto e resultado entre partes da organizacao **sem perda e sem
ambiguidade**. E a competencia que impede que o handoff seja o ponto onde a informacao
morre e a responsabilidade fica orfa.

## Escopo
A competencia de enderecar, enquadrar e transferir: escolher canal, formular pedido com
criterio de aceite, transferir responsabilidade com aceite explicito, reportar com evidencia
e escalar quando cabe.

| Item | Definicao |
|---|---|
| Dominio | `COG` — Cognicao Organizacional |
| Classe estrategica | `habilitadora` |
| Maturidade | `experimental` |
| Custodio | DEP-EXE |
| Exercentes | DEP-EXE (protocolo), DEP-KMS (curadoria do pacote) |

## Responsaveis
| Papel | Quem |
|---|---|
| Custodio (unico) | DEP-EXE |
| Exercentes | DEP-EXE, DEP-KMS |
| Autoridade de evolucao | DEP-EXE, com parecer de DEP-GOV |
| Ratificador | SOBERANO |

---

## 1. Identidade (A-01)
| Campo | Valor |
|---|---|
| ID | `CAP-comunicacao` |
| Nome | Comunicacao Organizacional |
| Dominio | COG |
| Classe | habilitadora |
| Maturidade | experimental |
| Especializa | nenhuma |

## 2. Missao (A-03)
> Garantir que quem recebe um trabalho consiga agir corretamente sem reconstruir o que
> quem enviou ja sabia.

## 3. Limites (A-05)
| **Nao** abrange | Pertence a |
|---|---|
| Persistir, curar e recuperar conhecimento | `CAP-conhecimento` |
| Decidir o que sera transferido e a quem | `CAP-coordenacao` |
| Comunicar ao publico externo | `CAP-marketing` |
| Extrair licao do que foi comunicado | `CAP-aprendizado-organizacional` |
| Definir a norma sobre o que deve ser registrado | `CAP-governanca` |

> **Fronteira com `CAP-conhecimento`:** aquela **monta e cura** o Pacote de Contexto; esta
> o **transporta** com envelope, aceite e prova de recebimento. Persistencia versus
> transferencia.
>
> **Fronteira com `CAP-marketing`:** esta Capability comunica **para dentro**; aquela,
> **para fora**.

## 4. Responsabilidades (A-06)
| # | A organizacao e capaz de... |
|---|---|
| R1 | Escolher o canal certo para a natureza da mensagem |
| R2 | Formular pedido unico, com criterio de aceite e escopo negativo |
| R3 | Transferir responsabilidade por contrato, com aceite explicito |
| R4 | Reportar resultado com evidencia, desvios e o que **nao** foi entregue |
| R5 | Escalar no nivel certo, com opcoes e recomendacao |
| R6 | Devolver trabalho mal formado em vez de improvisar sobre ele |
| R7 | Enviar contexto minimo suficiente, nao contexto maximo disponivel |

## 5. Entradas (A-07)
| Entrada | Origem | Obrigatoria? |
|---|---|---|
| Conteudo curado do pacote de contexto | `CAP-conhecimento` | Sim |
| Trabalho a ser transferido | qualquer Capability | Sim |
| Prioridade e destinatario | `CAP-coordenacao` | Sim |

## 6. Saidas (A-08)
| Saida | Consumida por |
|---|---|
| Handoff com contrato e aceite | Capability receptora |
| Reporte com evidencia | `CAP-coordenacao`, Soberano |
| Escalonamento fundamentado | nivel competente |
| Registro da troca | `CAP-conhecimento` |

## 7. Artefatos produzidos (A-09)
| Tipo de artefato | Exemplo |
|---|---|
| Handoff (`MSG`) | Transferencia com contrato de 11 clausulas |
| Reporte (`MSG`) | Estado, evidencia, nao entregue, aprendizado |
| Memoria (`MEM-OPR`) | Registro da comunicacao relevante |

## 8. Dependencias (A-10)
| Capability | Relacao | Por que |
|---|---|---|
| `CAP-conhecimento` | depende-de | Sem curadoria, transfere-se contexto demais ou de menos |

## 9. Consumidores (A-11)
| Capability | Relacao | O que consome |
|---|---|---|
| `CAP-coordenacao` | depende-de | Protocolo de troca e escalonamento |
| `CAP-engenharia-de-agentes` | depende-de | Formato de instrucao e de reporte dos executores |
| todas | fornece-para | Canal formal de troca |

## 10. Indicadores (A-12)
| # | Indicador | Direcao | Como se mede | Estado |
|---|---|---|---|---|
| I1 | Handoffs devolvidos por contexto insuficiente | ↓ | Motivo de devolucao (HO-02) | nao medido |
| I2 | Handoffs devolvidos duas vezes pelo mesmo motivo | → 0 | Registro de devolucao (HO-03) | nao medido |
| I3 | Reportes sem secao de evidencia ou de nao-entregue | → 0 | Auditoria de reporte (RP-01, RP-02) | nao medido |
| I4 | Responsabilidade assumida por silencio | → 0 | Verificacao de aceite explicito (HO-01) | nao medido |
| I5 | Tamanho do nucleo do pacote de contexto | ↓ | Volume por handoff | nao medido |

## 11. Criterios de evolucao (A-13)
| Movimento | Gatilho | Ganho PI-14 |
|---|---|---|
| Especializar | Comunicacao entre agentes divergir estruturalmente da comunicacao entre departamentos | Reducao de contexto |
| Especializar | Curadoria de contexto virar volume proprio, distinto do protocolo | Reducao de contexto |
| Fundir | Deixar de ser distinguivel de `CAP-conhecimento` na pratica | Organizacao |
| Promover a `nucleo` | Se a curadoria de contexto se confirmar como o fator dominante de qualidade dos agentes | — |

## 12. Historico de maturidade
| Data | De | Para | Evidencia | Instrumento |
|---|---|---|---|---|
| 2026-07-28 | proposta | experimental | Catalogo aprovado; protocolo definido em FND-05, ainda nao exercido em troca real | ADR-0002 |

## 13. Rastreabilidade
| Campo | Conteudo |
|---|---|
| ADR de criacao | ADR-0002 |
| RFC de origem | RFC-0001 |
| Normas que exerce | [FND-05](../foundation/05-framework-comunicacao.md) |
| Componentes vinculados | nenhum ainda |
