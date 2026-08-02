---
id: CAP-comercial
titulo: Comercial
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
classe: habilitadora
maturidade: experimental
custodio: DEP-GRW
exercentes: [DEP-GRW]
depende_de: [CAP-marketing, CAP-produto, CAP-juridico]
consumida_por: [CAP-financeiro]
especializa: null
---

# Comercial (CAP-comercial)

## Proposito
Converter interesse em relacao sustentavel: transformar quem descobriu a solucao em quem a
usa e permanece usando, sob termos que a organizacao consegue honrar.

## Escopo
A competencia de converter, precificar, contratar, reter e reconhecer quando um cliente ou
um modelo de receita nao serve a organizacao.

| Item | Definicao |
|---|---|
| Dominio | `MER` — Mercado e Recursos |
| Classe estrategica | `habilitadora` |
| Maturidade | `experimental` |
| Custodio | DEP-GRW |
| Exercentes | DEP-GRW |

## Responsaveis
| Papel | Quem |
|---|---|
| Custodio (unico) | DEP-GRW |
| Exercentes | DEP-GRW |
| Autoridade de evolucao | DEP-GRW, com parecer de DEP-GOV |
| Ratificador | SOBERANO |

---

## 1. Identidade (A-01)
| Campo | Valor |
|---|---|
| ID | `CAP-comercial` |
| Nome | Comercial |
| Dominio | MER |
| Classe | habilitadora |
| Maturidade | experimental |
| Especializa | nenhuma |

## 2. Missao (A-03)
> Garantir que a organizacao so assuma compromissos com o publico que ela e capaz de
> cumprir, e que os cumpra de forma economicamente sustentavel.

## 3. Limites (A-05)
| **Nao** abrange | Pertence a |
|---|---|
| Posicionar e comunicar ao mercado | `CAP-marketing` |
| Definir o que o produto entrega | `CAP-produto` |
| Avaliar validade juridica do contrato | `CAP-juridico` |
| Controlar custo e resultado financeiro | `CAP-financeiro` |
| Operar e sustentar o que foi vendido | `CAP-operacoes` |
| Autorizar compromisso publico | **SOBERANO** (LV-08) |

> **Limite duro:** compromisso externo em nome da organizacao exige autorizacao explicita do
> Soberano. Prometer prazo, escopo ou capacidade sem confirmar com `CAP-produto` e
> `CAP-coordenacao` viola PI-10.

## 4. Responsabilidades (A-06)
| # | A organizacao e capaz de... |
|---|---|
| R1 | Converter interesse em uso, sem prometer alem do entregavel |
| R2 | Precificar de forma que o valor entregue sustente o custo |
| R3 | Estruturar termos que a organizacao consegue honrar |
| R4 | Reter por resultado entregue, nao por friccao de saida |
| R5 | Reconhecer cliente ou modelo que nao serve, e recusar |
| R6 | Devolver ao produto o sinal do que faltou para converter |

## 5. Entradas (A-07)
| Entrada | Origem | Obrigatoria? |
|---|---|---|
| Posicionamento e narrativa | `CAP-marketing` | Sim |
| Proposta de valor e escopo real | `CAP-produto` | Sim |
| Limites contratuais e obrigacoes | `CAP-juridico` | Sim |
| Capacidade de entrega disponivel | `CAP-coordenacao` | Sim |
| Custo por cliente atendido | `CAP-financeiro` | Nao |

## 6. Saidas (A-08)
| Saida | Consumida por |
|---|---|
| Receita e retencao | `CAP-financeiro` |
| Compromissos assumidos | `CAP-coordenacao`, `CAP-operacoes` |
| Sinal de objecao e de perda | `CAP-produto`, `CAP-marketing` |
| Modelo de monetizacao | `CAP-estrategia`, `CAP-financeiro` |

## 7. Artefatos produzidos (A-09)
| Tipo de artefato | Exemplo |
|---|---|
| Relatorio | Resultado de conversao e retencao |
| Memoria (`MEM-PRD`) | Objecao recorrente, motivo de perda |
| ADR | Decisao de modelo de monetizacao |

## 8. Dependencias (A-10)
| Capability | Relacao | Por que |
|---|---|---|
| `CAP-marketing` | depende-de | Converter sem posicionamento e negociacao no vazio |
| `CAP-produto` | depende-de | Vender sem saber o escopo real gera promessa falsa |
| `CAP-juridico` | depende-de | Contratar sem limites conhecidos cria obrigacao nao avaliada |

## 9. Consumidores (A-11)
| Capability | Relacao | O que consome |
|---|---|---|
| `CAP-financeiro` | depende-de | Receita e compromissos que sustentam o planejamento |
| `CAP-produto` | consome-saida-de | Sinal de objecao e de perda |
| `CAP-operacoes` | consome-saida-de | Compromissos a sustentar |

## 10. Indicadores (A-12)
| # | Indicador | Direcao | Como se mede | Estado |
|---|---|---|---|---|
| I1 | Compromissos assumidos e nao cumpridos | → 0 | Comparacao promessa × entrega | **0** (nenhum compromisso) |
| I2 | Retencao por resultado versus por friccao de saida | ↑ | Motivo declarado de permanencia | nao medido |
| I3 | Clientes recusados por nao servirem a organizacao | ↑ | Registro de recusa | nao medido |
| I4 | Margem entre valor entregue e custo de atendimento | ↑ | Comparacao com `CAP-financeiro` | nao medido |

## 11. Criterios de evolucao (A-13)
| Movimento | Gatilho | Ganho PI-14 |
|---|---|---|
| Especializar | Aquisicao e retencao divergirem em metodo e cadencia | Organizacao |
| Especializar | Suporte a cliente surgir como responsabilidade propria | Organizacao |
| Fundir | Deixar de ser distinguivel de `CAP-marketing` na pratica | Organizacao |
| Depreciar | Se a organizacao passar a operar sem contraparte externa | — |

## 12. Historico de maturidade
| Data | De | Para | Evidencia | Instrumento |
|---|---|---|---|---|
| 2026-07-28 | proposta | experimental | Catalogo aprovado; nenhum cliente, produto ou compromisso | ADR-0002 |

## 13. Rastreabilidade
| Campo | Conteudo |
|---|---|
| ADR de criacao | ADR-0002 |
| RFC de origem | RFC-0001 |
| Componentes vinculados | nenhum ainda |
