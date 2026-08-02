---
id: CAP-marketing
titulo: Marketing
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
depende_de: [CAP-produto, CAP-estrategia]
consumida_por: [CAP-comercial]
especializa: null
---

# Marketing (CAP-marketing)

## Proposito
Fazer com que quem tem o problema descubra que existe solucao: posicionar, narrar e
distribuir a mensagem certa pelo canal certo, sem prometer o que o produto nao entrega.

## Escopo
A competencia de posicionar, construir narrativa, escolher canal, produzir conteudo e medir
aquisicao — sempre dentro do que o produto de fato faz.

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
| ID | `CAP-marketing` |
| Nome | Marketing |
| Dominio | MER |
| Classe | habilitadora |
| Maturidade | experimental |
| Especializa | nenhuma |

## 2. Missao (A-03)
> Garantir que a solucao chegue a quem tem o problema, descrita de forma que a expectativa
> criada seja a que o produto cumpre.

## 3. Limites (A-05)
| **Nao** abrange | Pertence a |
|---|---|
| Definir o que o produto e | `CAP-produto` |
| Definir posicionamento estrategico da organizacao | `CAP-estrategia` |
| Comunicacao **interna** entre partes | `CAP-comunicacao` |
| Negociar, contratar e reter cliente | `CAP-comercial` |
| Autorizar exposicao externa | **SOBERANO** (LV-08) |
| Desenhar a experiencia do produto | `CAP-design` |
| Avaliar conformidade da mensagem com norma externa | `CAP-juridico` |

> **Limite duro (LV-08, EX-02):** nenhuma saida desta Capability vai ao publico sem
> autorizacao explicita do Soberano. Nao ha delegacao — e a razao pela qual DEP-GRW opera
> em autonomia A1.
>
> **Fronteira com `CAP-comunicacao`:** esta comunica **para fora**; aquela, **para dentro**.

## 4. Responsabilidades (A-06)
| # | A organizacao e capaz de... |
|---|---|
| R1 | Posicionar a solucao em relacao a alternativa que o publico usa hoje |
| R2 | Construir narrativa fiel ao que o produto entrega |
| R3 | Escolher canal proporcional ao publico e ao custo |
| R4 | Produzir conteudo que sustente a mensagem |
| R5 | Medir aquisicao e reconhecer canal que nao funciona |
| R6 | **Recusar promessa que o produto nao cumpre**, mesmo que converta melhor |

## 5. Entradas (A-07)
| Entrada | Origem | Obrigatoria? |
|---|---|---|
| O que o produto e e nao e | `CAP-produto` | Sim |
| Posicionamento estrategico | `CAP-estrategia` | Sim |
| Panorama de publico e concorrencia | `CAP-pesquisa` | Nao |
| Linguagem e identidade da experiencia | `CAP-design` | Nao |
| Requisitos de conformidade externa | `CAP-juridico` | Sim |
| Autorizacao de exposicao | SOBERANO | **Sim** |

## 6. Saidas (A-08)
| Saida | Consumida por |
|---|---|
| Posicionamento e narrativa | `CAP-comercial` |
| Plano de canal e conteudo | `CAP-comercial`, `CAP-coordenacao` |
| Metricas de aquisicao | `CAP-estrategia`, `CAP-financeiro` |
| Sinal de mercado observado | `CAP-produto`, `CAP-pesquisa` |

## 7. Artefatos produzidos (A-09)
| Tipo de artefato | Exemplo |
|---|---|
| Relatorio | Plano de canal, resultado de aquisicao |
| Memoria (`MEM-PRD`) | Posicionamento, mensagem que funcionou |
| ADR | Decisao de posicionamento ou de canal |

## 8. Dependencias (A-10)
| Capability | Relacao | Por que |
|---|---|---|
| `CAP-produto` | depende-de | Comunicar sem saber o que o produto e produz promessa falsa |
| `CAP-estrategia` | depende-de | Mensagem fora da direcao confunde o mercado |

## 9. Consumidores (A-11)
| Capability | Relacao | O que consome |
|---|---|---|
| `CAP-comercial` | depende-de | Posicionamento e narrativa para converter |
| `CAP-produto` | consome-saida-de | Sinal de mercado |
| `CAP-financeiro` | consome-saida-de | Custo de aquisicao |

## 10. Indicadores (A-12)
| # | Indicador | Direcao | Como se mede | Estado |
|---|---|---|---|---|
| I1 | Promessas externas que o produto nao cumpriu | → 0 | Comparacao mensagem × entrega | **0** (nenhuma comunicacao emitida) |
| I2 | Publicacoes sem autorizacao explicita do Soberano | → 0 | Registro de autorizacao (LV-08) | **0** |
| I3 | Custo de aquisicao por canal | ↓ | Metrica por canal | nao medido |
| I4 | Canais mantidos apesar de resultado nulo | → 0 | Revisao de plano de canal | nao medido |

## 11. Criterios de evolucao (A-13)
| Movimento | Gatilho | Ganho PI-14 |
|---|---|---|
| Especializar | Producao de conteudo e gestao de canal divergirem em cadencia | Organizacao |
| Especializar | Marca e aquisicao exigirem metodos distintos | Organizacao |
| Fundir | Deixar de ser distinguivel de `CAP-comercial` na pratica | Organizacao |
| Depreciar | Se a organizacao passar a operar sem publico externo | — |

## 12. Historico de maturidade
| Data | De | Para | Evidencia | Instrumento |
|---|---|---|---|---|
| 2026-07-28 | proposta | experimental | Catalogo aprovado; nenhum produto e nenhuma comunicacao externa | ADR-0002 |

## 13. Rastreabilidade
| Campo | Conteudo |
|---|---|
| ADR de criacao | ADR-0002 |
| RFC de origem | RFC-0001 |
| Normas que exerce | [FND-05 §10](../foundation/05-framework-comunicacao.md) |
| Componentes vinculados | nenhum ainda |
