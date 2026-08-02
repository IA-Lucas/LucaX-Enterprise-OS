---
id: CAP-arquitetura
titulo: Arquitetura
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
depende_de: [CAP-produto]
consumida_por: [CAP-engenharia, CAP-dados, CAP-inteligencia-artificial, CAP-infraestrutura, CAP-integracao]
especializa: null
---

# Arquitetura (CAP-arquitetura)

## Proposito
Decidir a estrutura do sistema e sustentar essa decisao no tempo: escolher fronteiras,
padroes e tradeoffs de forma que a proxima mudanca seja barata e que o raciocinio original
permaneca recuperavel.

## Escopo
A competencia de definir componentes e suas fronteiras, escolher padroes tecnicos, avaliar
viabilidade, assumir divida conscientemente e registrar o porque de cada escolha.

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
| ID | `CAP-arquitetura` |
| Nome | Arquitetura |
| Dominio | REA |
| Classe | habilitadora |
| Maturidade | experimental |
| Especializa | nenhuma |

## 2. Missao (A-03)
> Garantir que a estrutura escolhida hoje nao impeca a mudanca de amanha, e que o motivo
> de cada escolha continue disponivel quando ninguem lembrar dele.

## 3. Limites (A-05)
| **Nao** abrange | Pertence a |
|---|---|
| Definir o que construir | `CAP-produto` |
| Construir a solucao | `CAP-engenharia` |
| Desenhar a estrutura **organizacional** | `CAP-governanca` |
| Modelar dados de dominio e sua semantica | `CAP-dados` |
| Prover e operar ambientes de execucao | `CAP-infraestrutura` |
| Verificar se o resultado atende ao criterio | `CAP-qualidade` |
| Escolher e contratar capacidade externa | `CAP-integracao` |

> **Fronteira com `CAP-engenharia`:** arquitetura decide **a estrutura e o porque**;
> engenharia **constroi dentro dela**. Uma decisao que so afeta um trecho isolado nao e
> arquitetural.
>
> **Fronteira com `CAP-governanca`:** esta Capability arquiteta **sistemas**; aquela,
> **a organizacao**.

## 4. Responsabilidades (A-06)
| # | A organizacao e capaz de... |
|---|---|
| R1 | Definir componentes e fronteiras que sustentem mudanca sem reescrita |
| R2 | Escolher padroes tecnicos e declarar quais sao proibidos |
| R3 | Avaliar viabilidade e estimar custo estrutural antes de comprometer |
| R4 | Registrar o raciocinio: alternativa descartada, criterio e tradeoff aceito |
| R5 | Assumir divida tecnica de forma consciente, com custo declarado |
| R6 | Identificar quando uma decisao e irreversivel e trata-la como Tipo 1 |
| R7 | Preferir a solucao mais simples defensavel entre as que satisfazem o criterio |

## 5. Entradas (A-07)
| Entrada | Origem | Obrigatoria? |
|---|---|---|
| Spec e criterios de aceite | `CAP-produto` | Sim |
| Restricoes de forma e interacao | `CAP-design` | Nao |
| Historico tecnico e caminhos descartados | `CAP-conhecimento` | Sim |
| Antipadroes conhecidos | `CAP-aprendizado-organizacional` | Nao |
| Catalogo de capacidades externas | `CAP-integracao` | Nao |

## 6. Saidas (A-08)
| Saida | Consumida por |
|---|---|
| Decisao arquitetural registrada (ADR) | `CAP-engenharia`, `CAP-dados`, `CAP-infraestrutura` |
| Desenho de componentes e fronteiras | `CAP-engenharia` |
| Padroes adotados e proibidos | `CAP-engenharia`, `CAP-qualidade` |
| Avaliacao de viabilidade e custo | `CAP-produto`, `CAP-coordenacao` |
| Registro de divida tecnica | `CAP-coordenacao`, `CAP-qualidade` |

## 7. Artefatos produzidos (A-09)
| Tipo de artefato | Exemplo |
|---|---|
| ADR | Decisao arquitetural com alternativas e tradeoff |
| Memoria (`MEM-TEC`) | Arquitetura vigente, divida, caminho descartado |
| RFC | Proposta de mudanca estrutural |

## 8. Dependencias (A-10)
| Capability | Relacao | Por que |
|---|---|---|
| `CAP-produto` | depende-de | Arquitetar sem spec produz estrutura sem proposito |

## 9. Consumidores (A-11)
| Capability | Relacao | O que consome |
|---|---|---|
| `CAP-engenharia` | depende-de | Estrutura e padroes dentro dos quais constroi |
| `CAP-dados` | depende-de | Fronteiras e contratos de integracao |
| `CAP-inteligencia-artificial` | depende-de | Estrutura em que os modelos se encaixam |
| `CAP-infraestrutura` | depende-de | Requisitos estruturais de execucao |
| `CAP-integracao` | depende-de | Contratos que a capacidade externa deve atender |

## 10. Indicadores (A-12)
| # | Indicador | Direcao | Como se mede | Estado |
|---|---|---|---|---|
| I1 | Decisoes arquiteturais com alternativas reais registradas | → 100% | Auditoria de ADR (VD-01) | nao medido |
| I2 | Mudancas que exigiram reescrita estrutural nao prevista | ↓ | Registro de retrabalho | nao medido |
| I3 | Divida tecnica com custo declarado no momento de assumi-la | → 100% | Registro em `MEM-TEC` | nao medido |
| I4 | Decisoes reabertas por falta do registro do porque | → 0 | Consulta previa a memoria TEC | nao medido |
| I5 | Decisoes Tipo 1 classificadas corretamente na origem | → 100% | Comparacao com reversao real | nao medido |

## 11. Criterios de evolucao (A-13)
| Movimento | Gatilho | Ganho PI-14 |
|---|---|---|
| Especializar | Arquitetura de dados e arquitetura de aplicacao divergirem em metodo | Organizacao |
| Especializar | Arquitetura de sistemas com agentes exigir raciocinio proprio | Reducao de contexto |
| Fundir | Deixar de ser distinguivel de `CAP-engenharia` na pratica | Organizacao |
| Promover a `nucleo` | Se a estrutura tecnica passar a ser o fator dominante de velocidade da organizacao | — |

## 12. Historico de maturidade
| Data | De | Para | Evidencia | Instrumento |
|---|---|---|---|---|
| 2026-07-28 | proposta | experimental | Catalogo aprovado; nenhum sistema arquitetado — a arquitetura produzida ate aqui e organizacional, e pertence a `CAP-governanca` | ADR-0002 |

## 13. Rastreabilidade
| Campo | Conteudo |
|---|---|
| ADR de criacao | ADR-0002 |
| RFC de origem | RFC-0001 |
| Normas que exerce | [FND-01 §6.2 QG-2](../foundation/01-constituicao.md), [FND-07](../foundation/07-framework-decisoes.md) |
| Componentes vinculados | nenhum ainda |
