---
id: CAP-estrategia
titulo: Estrategia
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
classe: nucleo
maturidade: emergente
custodio: DEP-EXE
exercentes: [DEP-EXE]
depende_de: [CAP-conhecimento, CAP-governanca]
consumida_por: [CAP-coordenacao, CAP-produto, CAP-marketing]
especializa: null
---

# Estrategia (CAP-estrategia)

## Proposito
Definir e manter viva a direcao da organizacao: onde apostar, o que recusar, e sob quais
criterios um caminho e melhor que outro. E a competencia que transforma a intencao do
Soberano em direcao acionavel sem microgestao (Visao V1).

## Escopo
A competencia de formular direcao de longo prazo, decidir portfolio, estabelecer criterios
de sucesso organizacional e recusar oportunidades que nao servem a direcao.

| Item | Definicao |
|---|---|
| Dominio | `DIR` — Direcao |
| Classe estrategica | `nucleo` |
| Maturidade | `emergente` |
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
| ID | `CAP-estrategia` |
| Nome | Estrategia |
| Dominio | DIR |
| Classe | nucleo |
| Maturidade | emergente |
| Especializa | nenhuma |

## 2. Missao (A-03)
> Garantir que cada esforco da organizacao sirva a uma direcao declarada, e que a recusa
> do que nao serve seja tao explicita quanto a escolha do que serve.

## 3. Limites (A-05)
| **Nao** abrange | Pertence a |
|---|---|
| Priorizar a fila de trabalho e alocar capacidade | `CAP-coordenacao` |
| Definir o escopo de um produto especifico | `CAP-produto` |
| Verificar conformidade da decisao com a norma | `CAP-governanca` |
| Descobrir fatos sobre mercado, publico ou tecnologia | `CAP-pesquisa` |
| Posicionar e comunicar a mensagem ao publico | `CAP-marketing` |
| Gerir custo e recursos | `CAP-financeiro` |

> **Fronteira com `CAP-coordenacao`:** estrategia decide **para onde**; coordenacao decide
> **o que primeiro e com quem**. Confundir as duas produz plano sem execucao ou execucao
> sem rumo.

## 4. Responsabilidades (A-06)
| # | A organizacao e capaz de... |
|---|---|
| R1 | Formular direcao de longo prazo em horizontes com criterio de conclusao |
| R2 | Decidir o que entra e o que sai do portfolio, com justificativa registrada |
| R3 | Declarar o que a organizacao **nao** fara, e por que |
| R4 | Estabelecer criterios de sucesso organizacional verificaveis |
| R5 | Reconhecer quando a direcao deixou de servir e propor sua revisao |
| R6 | Traduzir determinacao do Soberano em direcao operavel sem distorce-la |

## 5. Entradas (A-07)
| Entrada | Origem | Obrigatoria? |
|---|---|---|
| Determinacao e intencao do Soberano | externa (Soberano) | Sim |
| Historico de decisoes e apostas anteriores | `CAP-conhecimento` | Sim |
| Rito e instrumento de decisao | `CAP-governanca` | Sim |
| Sinais de mercado e de contexto | `CAP-pesquisa` | Nao |
| Resultado observado dos produtos | `CAP-produto` | Nao |

## 6. Saidas (A-08)
| Saida | Consumida por |
|---|---|
| Direcao vigente e horizontes | `CAP-coordenacao`, todas |
| Decisao de portfolio | `CAP-produto` |
| Criterios de sucesso organizacional | `CAP-coordenacao`, `CAP-qualidade` |
| Escopo negativo da organizacao | todas |
| Posicionamento estrategico | `CAP-marketing` |

## 7. Artefatos produzidos (A-09)
| Tipo de artefato | Exemplo |
|---|---|
| ADR | Decisao de portfolio, mudanca de direcao |
| Documento fundacional (`FND`) | Missao, visao, objetivos de longo prazo |
| Memoria (`MEM-EST`) | Aposta registrada e seu resultado |

## 8. Dependencias (A-10)
| Capability | Relacao | Por que |
|---|---|---|
| `CAP-conhecimento` | depende-de | Decidir sem historico repete analise ja feita |
| `CAP-governanca` | depende-de | Decisao estrategica sem rito nao vincula (PI-04) |

## 9. Consumidores (A-11)
| Capability | Relacao | O que consome |
|---|---|---|
| `CAP-coordenacao` | depende-de | A direcao que a prioridade deve servir |
| `CAP-produto` | depende-de | Decisao de portfolio e criterios de sucesso |
| `CAP-marketing` | depende-de | Posicionamento estrategico |

## 10. Indicadores (A-12)
| # | Indicador | Direcao | Como se mede | Estado |
|---|---|---|---|---|
| I1 | Esforcos ativos rastreaveis a um objetivo declarado | → 100% | Vinculo trabalho × horizonte | nao medido |
| I2 | Apostas com resultado avaliado apos o prazo | → 100% | Revisao de ADRs de portfolio | nao medido |
| I3 | Recusas registradas (escopo negativo explicito) | ↑ | Contagem de "nao faremos" documentados | 1 (H1: nenhum agente antes da fundacao) |
| I4 | Mudancas de direcao sem decisao registrada | → 0 | Auditoria de coerencia | **0** |
| I5 | Tempo entre determinacao do Soberano e direcao operavel | ↓ | Data da instrucao × data da prioridade | nao medido |

## 11. Criterios de evolucao (A-13)
| Movimento | Gatilho | Ganho PI-14 |
|---|---|---|
| Especializar | Portfolio crescer a ponto de exigir gestao propria, separada da formulacao de direcao | Organizacao |
| Especializar | Direcao de longo prazo e apostas de curto prazo exigirem cadencias incompativeis | Organizacao |
| Fundir | Deixar de ser distinguivel de `CAP-coordenacao` na pratica | Organizacao |
| Depreciar | **Nunca** — sem direcao, a organizacao nao tem por que existir |

## 12. Historico de maturidade
| Data | De | Para | Evidencia | Instrumento |
|---|---|---|---|---|
| 2026-07-28 | proposta | experimental | Catalogo aprovado | ADR-0002 |
| 2026-07-28 | experimental | emergente | Exercida com resultado registrado: missao, visao, valores, 3 horizontes com criterio de conclusao e escopo negativo declarado, em FND-01 | ADR-0002 |

## 13. Rastreabilidade
| Campo | Conteudo |
|---|---|
| ADR de criacao | ADR-0002 |
| RFC de origem | RFC-0001 |
| Normas que exerce | [FND-01 §1–§5](../foundation/01-constituicao.md) |
| Componentes vinculados | nenhum ainda |
