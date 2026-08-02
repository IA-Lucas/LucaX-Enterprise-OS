---
id: CAP-dados
titulo: Dados
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
depende_de: [CAP-arquitetura, CAP-seguranca]
consumida_por: [CAP-inteligencia-artificial]
especializa: null
---

# Dados (CAP-dados)

## Proposito
Fazer com que a organizacao consiga confiar nos proprios numeros: modelar, coletar,
qualificar e disponibilizar dados de forma que uma pergunta tenha sempre a mesma resposta,
com origem conhecida.

## Escopo
A competencia de modelar dominio em dados, garantir integridade e linhagem, disponibilizar
para consumo e produzir analise com significado inequivoco.

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
| ID | `CAP-dados` |
| Nome | Dados |
| Dominio | REA |
| Classe | habilitadora |
| Maturidade | experimental |
| Especializa | nenhuma |

## 2. Missao (A-03)
> Garantir que toda afirmacao quantitativa feita pela organizacao possa ser rastreada ate
> sua origem e reproduzida por outro.

## 3. Limites (A-05)
| **Nao** abrange | Pertence a |
|---|---|
| Memoria organizacional e conhecimento textual | `CAP-conhecimento` |
| Definir a estrutura tecnica que hospeda os dados | `CAP-arquitetura` |
| Prover armazenamento e ambiente de execucao | `CAP-infraestrutura` |
| Treinar, avaliar e operar modelos | `CAP-inteligencia-artificial` |
| Proteger dado sensivel e controlar acesso | `CAP-seguranca` |
| Definir a base legal de tratamento de dado pessoal | `CAP-juridico` |
| Investigar o mundo externo | `CAP-pesquisa` |

> **Fronteira com `CAP-conhecimento`:** esta Capability cuida de **dado estruturado do
> dominio**; aquela, de **conhecimento organizacional**. Um numero de uso e dado; a licao
> extraida dele e conhecimento.

## 4. Responsabilidades (A-06)
| # | A organizacao e capaz de... |
|---|---|
| R1 | Modelar dominio em dados com semantica inequivoca |
| R2 | Garantir integridade, linhagem e reprodutibilidade |
| R3 | Definir a metrica de forma que ela signifique sempre a mesma coisa |
| R4 | Disponibilizar dado para consumo sem duplicar a fonte de verdade |
| R5 | Detectar dado inconsistente, faltante ou enviesado |
| R6 | Distinguir fato medido de estimativa derivada |

## 5. Entradas (A-07)
| Entrada | Origem | Obrigatoria? |
|---|---|---|
| Contratos e fronteiras tecnicas | `CAP-arquitetura` | Sim |
| Definicao de metrica de produto | `CAP-produto` | Nao |
| Sinal operacional e de uso | `CAP-operacoes` | Nao |
| Requisitos de protecao e acesso | `CAP-seguranca` | Sim |

## 6. Saidas (A-08)
| Saida | Consumida por |
|---|---|
| Modelo de dados e semantica | `CAP-engenharia`, `CAP-inteligencia-artificial` |
| Dado qualificado com linhagem | `CAP-inteligencia-artificial`, `CAP-produto` |
| Analise e metrica confiavel | `CAP-estrategia`, `CAP-produto`, `CAP-comercial` |
| Alerta de inconsistencia ou vies | `CAP-qualidade` |

## 7. Artefatos produzidos (A-09)
| Tipo de artefato | Exemplo |
|---|---|
| Memoria (`MEM-TEC`) | Modelo de dados, linhagem, definicao de metrica |
| ADR | Decisao de modelagem |
| Relatorio | Analise com fonte e metodo |

## 8. Dependencias (A-10)
| Capability | Relacao | Por que |
|---|---|---|
| `CAP-arquitetura` | depende-de | Modelagem fora da estrutura decidida cria fonte paralela |
| `CAP-seguranca` | depende-de | Modelar dado sem requisito de protecao e acesso cria exposicao |

## 9. Consumidores (A-11)
| Capability | Relacao | O que consome |
|---|---|---|
| `CAP-inteligencia-artificial` | depende-de | Dado qualificado para alimentar e avaliar modelos |
| `CAP-produto` | consome-saida-de | Metricas de uso e resultado |
| `CAP-estrategia` | consome-saida-de | Evidencia quantitativa para decidir |
| `CAP-seguranca` | verifica *(inversa)* | Verifica protecao e acesso ao dado |

## 10. Indicadores (A-12)
| # | Indicador | Direcao | Como se mede | Estado |
|---|---|---|---|---|
| I1 | Metricas com definicao unica e documentada | → 100% | Catalogo de metricas | nao medido |
| I2 | Mesma pergunta respondida de forma divergente por fontes distintas | → 0 | Comparacao de fontes | nao medido |
| I3 | Dados com linhagem rastreavel ate a origem | → 100% | Auditoria de linhagem | nao medido |
| I4 | Analises que distinguem fato medido de estimativa | → 100% | Auditoria de relatorio | nao medido |

## 11. Criterios de evolucao (A-13)
| Movimento | Gatilho | Ganho PI-14 |
|---|---|---|
| Especializar | Engenharia de dados e analise divergirem em metodo e cadencia | Organizacao |
| Especializar | Governanca de dado pessoal virar volume proprio | Organizacao |
| Fundir | Deixar de ser distinguivel de `CAP-engenharia` na pratica | Organizacao |
| Promover a `nucleo` | Se produtos orientados a dado se tornarem a aposta central | — |

## 12. Historico de maturidade
| Data | De | Para | Evidencia | Instrumento |
|---|---|---|---|---|
| 2026-07-28 | proposta | experimental | Catalogo aprovado; nenhum dado modelado — a fase de fundacao proibiu banco de dados | ADR-0002 |

## 13. Rastreabilidade
| Campo | Conteudo |
|---|---|
| ADR de criacao | ADR-0002 |
| RFC de origem | RFC-0001 |
| Componentes vinculados | nenhum ainda |
