---
id: CAP-infraestrutura
titulo: Infraestrutura
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
depende_de: [CAP-arquitetura]
consumida_por: [CAP-operacoes]
especializa: null
---

# Infraestrutura (CAP-infraestrutura)

## Proposito
Prover o substrato onde as coisas rodam: ambientes, execucao, armazenamento e o caminho
entre o que foi construido e o que esta disponivel. E a competencia que torna o trabalho
utilizavel fora da maquina de quem o fez.

## Escopo
A competencia de provisionar e dimensionar ambientes, definir o caminho de publicacao,
garantir reprodutibilidade de execucao e prever o custo do substrato.

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
| ID | `CAP-infraestrutura` |
| Nome | Infraestrutura |
| Dominio | SUS |
| Classe | habilitadora |
| Maturidade | experimental |
| Especializa | nenhuma |

## 2. Missao (A-03)
> Garantir que o que a organizacao constroi tenha onde existir de forma reproduzivel, e
> que o caminho ate la seja previsivel e reversivel.

## 3. Limites (A-05)
| **Nao** abrange | Pertence a |
|---|---|
| Decidir a estrutura do sistema | `CAP-arquitetura` |
| Operar a rotina do que roda sobre o ambiente | `CAP-operacoes` |
| Adotar e contratar capacidade externa de terceiro | `CAP-integracao` |
| Verificar protecao, acesso e exposicao | `CAP-seguranca` |
| Modelar os dados armazenados | `CAP-dados` |
| Aprovar o custo recorrente | `CAP-financeiro` |

> **Fronteira com `CAP-integracao`:** esta Capability cuida do substrato que a organizacao
> **provisiona e controla**; aquela, das capacidades **de terceiros** das quais a
> organizacao passa a depender.

## 4. Responsabilidades (A-06)
| # | A organizacao e capaz de... |
|---|---|
| R1 | Provisionar ambiente reproduzivel, nao artesanal |
| R2 | Definir o caminho entre construido e disponivel, com reversao |
| R3 | Dimensionar recurso proporcional a necessidade real |
| R4 | Isolar ambientes de modo que falha em um nao contamine outro |
| R5 | Prever o custo do substrato antes de comprometer |
| R6 | Garantir que a execucao produza o mesmo resultado em qualquer ambiente valido |

## 5. Entradas (A-07)
| Entrada | Origem | Obrigatoria? |
|---|---|---|
| Requisitos estruturais de execucao | `CAP-arquitetura` | Sim |
| Requisitos de protecao e isolamento | `CAP-seguranca` | Sim |
| Capacidades externas disponiveis | `CAP-integracao` | Nao |
| Limite de custo aprovado | `CAP-financeiro` | Sim |

## 6. Saidas (A-08)
| Saida | Consumida por |
|---|---|
| Ambiente de execucao provisionado | `CAP-operacoes`, `CAP-engenharia` |
| Caminho de publicacao e reversao | `CAP-operacoes` |
| Custo previsto do substrato | `CAP-financeiro` |
| Limites de capacidade | `CAP-coordenacao` |

## 7. Artefatos produzidos (A-09)
| Tipo de artefato | Exemplo |
|---|---|
| Memoria (`MEM-TEC`) | Topologia de ambiente, limites conhecidos |
| ADR | Decisao de plataforma ou de topologia |
| Workflow (`WFL`) | Caminho de publicacao formalizado |

## 8. Dependencias (A-10)
| Capability | Relacao | Por que |
|---|---|---|
| `CAP-arquitetura` | depende-de | Provisionar sem requisito estrutural produz ambiente inadequado |

## 9. Consumidores (A-11)
| Capability | Relacao | O que consome |
|---|---|---|
| `CAP-operacoes` | depende-de | O ambiente onde a rotina roda |
| `CAP-engenharia` | consome-saida-de | Ambiente de construcao e verificacao |
| `CAP-financeiro` | consome-saida-de | Custo previsto do substrato |
| `CAP-seguranca` | verifica *(inversa)* | Verifica isolamento, acesso e exposicao |

## 10. Indicadores (A-12)
| # | Indicador | Direcao | Como se mede | Estado |
|---|---|---|---|---|
| I1 | Ambientes reproduziveis a partir de definicao, nao de memoria | → 100% | Teste de recriacao | nao medido |
| I2 | Publicacoes revertidas com sucesso quando necessario | → 100% | Registro de reversao | nao medido |
| I3 | Desvio entre custo previsto e real do substrato | → 0 | Comparacao registrada | nao medido |
| I4 | Falhas que atravessaram o isolamento entre ambientes | → 0 | Postmortem | nao medido |

## 11. Criterios de evolucao (A-13)
| Movimento | Gatilho | Ganho PI-14 |
|---|---|---|
| Especializar | Ambiente de execucao de agentes divergir do ambiente de produtos | Organizacao |
| Especializar | Caminho de publicacao virar disciplina propria | Organizacao |
| Fundir | Deixar de ser distinguivel de `CAP-operacoes` na pratica | Organizacao |
| Depreciar | Se toda execucao passar a ocorrer em capacidade de terceiro, sob `CAP-integracao` | — |

## 12. Historico de maturidade
| Data | De | Para | Evidencia | Instrumento |
|---|---|---|---|---|
| 2026-07-28 | proposta | experimental | Catalogo aprovado; nenhuma infraestrutura provisionada — a fase de fundacao a proibiu | ADR-0002 |

## 13. Rastreabilidade
| Campo | Conteudo |
|---|---|
| ADR de criacao | ADR-0002 |
| RFC de origem | RFC-0001 |
| Componentes vinculados | nenhum ainda |
