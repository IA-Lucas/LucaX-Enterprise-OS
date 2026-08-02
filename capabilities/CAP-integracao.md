---
id: CAP-integracao
titulo: Integracao e Ferramental
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
custodio: DEP-TLS
exercentes: [DEP-TLS]
depende_de: [CAP-arquitetura, CAP-seguranca]
consumida_por: [CAP-inteligencia-artificial]
especializa: null
---

# Integracao e Ferramental (CAP-integracao)

## Proposito
Incorporar capacidade externa sem que a organizacao perca o controle sobre si: avaliar,
adotar, limitar e descartar servicos, APIs e ferramentas de terceiros de forma consciente.

## Escopo
A competencia de decidir o que a organizacao **nao** vai construir, escolher de quem
depender, declarar o que trafega, impor limites e planejar a saida antes da entrada.

| Item | Definicao |
|---|---|
| Dominio | `SUS` — Sustentacao |
| Classe estrategica | `habilitadora` |
| Maturidade | `experimental` |
| Custodio | DEP-TLS |
| Exercentes | DEP-TLS |

## Responsaveis
| Papel | Quem |
|---|---|
| Custodio (unico) | DEP-TLS |
| Exercentes | DEP-TLS |
| Autoridade de evolucao | DEP-TLS, com parecer de DEP-GOV |
| Ratificador | SOBERANO |

---

## 1. Identidade (A-01)
| Campo | Valor |
|---|---|
| ID | `CAP-integracao` |
| Nome | Integracao e Ferramental |
| Dominio | SUS |
| Classe | habilitadora |
| Maturidade | experimental |
| Especializa | nenhuma |

## 2. Missao (A-03)
> Garantir que toda dependencia externa seja escolhida com criterio, limitada com clareza e
> abandonavel sem catastrofe.

## 3. Limites (A-05)
| **Nao** abrange | Pertence a |
|---|---|
| Prover substrato que a organizacao controla | `CAP-infraestrutura` |
| Decidir a estrutura em que a ferramenta se encaixa | `CAP-arquitetura` |
| Avaliar risco de exposicao e proteger segredo | `CAP-seguranca` |
| Avaliar termos e licenca sob a otica juridica | `CAP-juridico` |
| Aprovar o custo recorrente | `CAP-financeiro` |
| Usar a ferramenta no dominio do produto | a Capability que a consome |

> **Fronteira com `CAP-infraestrutura`:** aquela cuida do que a organizacao **provisiona e
> controla**; esta, do que ela **contrata e do qual passa a depender**.
>
> **Fronteira com `CAP-seguranca`:** esta escolhe **de quem depender**; aquela avalia **o
> risco de faze-lo**. A adocao exige o parecer daquela — por isso a dependencia dura.

## 4. Responsabilidades (A-06)
| # | A organizacao e capaz de... |
|---|---|
| R1 | Avaliar capacidade externa por resultado para a tarefa, nao por custo primeiro (PI-11) |
| R2 | Declarar o que trafega para fora antes de qualquer adocao |
| R3 | Manter catalogo unico do que e oficial para cada finalidade |
| R4 | Impor e monitorar limites de uso |
| R5 | Definir criterio de descarte **antes** de adotar |
| R6 | Manter alternativa avaliada para dependencia critica |
| R7 | Referenciar credencial apenas por variavel de ambiente, nunca por valor (PI-08) |

## 5. Entradas (A-07)
| Entrada | Origem | Obrigatoria? |
|---|---|---|
| Contratos e requisitos estruturais | `CAP-arquitetura` | Sim |
| Parecer de risco e exposicao | `CAP-seguranca` | Sim |
| Sintese de termos e licenca | `CAP-juridico` | Sim |
| Limite de custo aprovado | `CAP-financeiro` | Sim |
| Necessidade de capacidade | qualquer Capability | Sim |

## 6. Saidas (A-08)
| Saida | Consumida por |
|---|---|
| Catalogo de ferramentas oficiais | todas |
| Ficha de ferramenta com dado trafegado e custo | `CAP-seguranca`, `CAP-financeiro` |
| Limites de uso | `CAP-inteligencia-artificial`, `CAP-operacoes` |
| Mapa de dependencia externa e risco | `CAP-arquitetura`, `CAP-coordenacao` |
| Criterio de descarte e alternativa | `CAP-arquitetura` |

## 7. Artefatos produzidos (A-09)
| Tipo de artefato | Exemplo |
|---|---|
| Ferramenta (`TOL`) | Ficha com finalidade, dado, custo, criticidade, descarte |
| ADR | Decisao de adocao ou de descarte |
| Memoria (`MEM-TEC`) | Risco de dependencia, lock-in conhecido |

## 8. Dependencias (A-10)
| Capability | Relacao | Por que |
|---|---|---|
| `CAP-arquitetura` | depende-de | Adotar sem contrato estrutural cria acoplamento nao previsto |
| `CAP-seguranca` | depende-de | Adotar sem parecer de risco expoe a organizacao |

## 9. Consumidores (A-11)
| Capability | Relacao | O que consome |
|---|---|---|
| `CAP-inteligencia-artificial` | depende-de | Provedores de modelo e seus limites |
| `CAP-infraestrutura` | consome-saida-de | Capacidades externas disponiveis |
| `CAP-financeiro` | consome-saida-de | Custo recorrente por dependencia |
| `CAP-juridico` | consome-saida-de | Termos aceitos ao contratar |

## 10. Indicadores (A-12)
| # | Indicador | Direcao | Como se mede | Estado |
|---|---|---|---|---|
| I1 | Ferramentas adotadas sem criterio de descarte definido | → 0 | Auditoria de ficha (DP-05) | **0** (nenhuma adotada) |
| I2 | Dependencias criticas sem alternativa avaliada | → 0 | Mapa de dependencia | **0** |
| I3 | Credenciais registradas por valor em vez de referencia | → 0 | Varredura (PI-08) | **0** |
| I4 | Adocoes decididas por custo em vez de resultado | → 0 | Secao de avaliacao PI-11 na ficha | **0** |
| I5 | Ferramentas oficiais duplicadas para a mesma finalidade | → 0 | Catalogo | **0** |

## 11. Criterios de evolucao (A-13)
| Movimento | Gatilho | Ganho PI-14 |
|---|---|---|
| Especializar | Provedores de modelo e ferramentas de trabalho divergirem em criterio de avaliacao | Organizacao |
| Especializar | Gestao de acesso e segredo virar volume proprio | Organizacao |
| Fundir | Deixar de ser distinguivel de `CAP-infraestrutura` na pratica | Organizacao |
| Promover a `nucleo` | Se a composicao de capacidades externas se tornar o diferencial da organizacao | — |

## 12. Historico de maturidade
| Data | De | Para | Evidencia | Instrumento |
|---|---|---|---|---|
| 2026-07-28 | proposta | experimental | Catalogo aprovado; nenhuma ferramenta adotada oficialmente | ADR-0002 |

## 13. Rastreabilidade
| Campo | Conteudo |
|---|---|
| ADR de criacao | ADR-0002 |
| RFC de origem | RFC-0001 |
| Normas que exerce | [FND-03 §3.12](../foundation/03-taxonomia.md), [FND-04 §11](../foundation/04-governanca.md), [FND-01 PI-11](../foundation/01-constituicao.md) |
| Componentes vinculados | nenhum ainda |
