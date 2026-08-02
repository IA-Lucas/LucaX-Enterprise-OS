> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

# FICHAS DE EVIDÊNCIA — ÁREA 01 — DECIDIR MODELO E ESCOPO

**Fase:** 2 — Extração · **Data:** 2026-07-29 · **Avaliador:** Claude Opus 5 (Fase 2)
**Itens:** 11 — 0 REPO · 5 PRINT · 6 VÍDEO · 0 PLANILHA
**Instrumento:** `04_RUBRICA-DE-AVALIACAO.md` (inclusive §14) · `05_GUIA-DE-APLICACAO-DA-RUBRICA.md`
**Convenções de aplicação:** `07_FICHAS-DE-EVIDENCIA/00_INDICE-DA-FASE-2.md` §3

**Pergunta central da área (base de E01):** *que modelo usar para cada tipo de tarefa, e até onde levar o sistema.*

---

### AC-01-PRT-001 — `Captura de tela 2026-07-28 155729.png`

**Tipo:** PRINT
**Área:** 01_DECIDIR-MODELO-E-ESCOPO
**Hash F0:** `DC4365C3885D4F35`   **Hash reconferido:** `DC4365C3885D4F35`   **Confere:** sim
**LV:** LV3-V
**Cobertura da leitura:** inspeção visual do original registrada em `109`/`105` (lote 07, H-P1-001); descrição do `_CONTEUDO.md` da área 01 confrontada com os pixels pela trilha Codex. Esta frente não abriu a imagem.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** AC-01-PRT-001 · `H-P1-001` (relatório `105`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Infográfico “How AI is perceived”: exemplo isolado, não reprodutível; nenhum insumo ou procedimento acompanha a imagem (`105`, área 01) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem do infográfico e inspecionar seu versionamento/atualização |
| E05 Manutenção | ND | — | Localizar canal de publicação original com data e cadência |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial visível ou instrução dirigida ao leitor |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos de uso da imagem de terceiro |
| E13 Testes/evals | ND | — | Não há artefato testável associado; resolveria identificar a fonte primária do modelo apresentado |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas (camadas de maturidade, nomes de ferramentas); nenhum número decisivo em jogo (`105`) | — |

**NF = 2 · 2/7 · 5 ND** *(mediana de [2,3] = 2,5 → §14.3 vale o inferior)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a segunda pergunta central da área — “até onde levar o sistema” — decompondo maturidade em capacidades (`105`: superfície → combinação por função → sistemas que substituem workflows) | — |
| E04 Transferibilidade | 2 | O padrão (decompor trabalho em capacidades) é transferível; a lista de produtos é do contexto do autor | — |
| E14 Diferencial | 2 | Agregação de material público amplamente conhecido; nomes reaparecem em AC-01-PRT-004 e AC-02-PRT-004 | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): não requer instalação; o formato de consumo não está declarado no artefato | — |
| E09 Custo | 5 | Sem custo recorrente; arquivo PNG local de 833,7 KB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = uma entrada descritiva em `105` (< 1 MB, < 50 arquivos), superfície delimitada pelo relatório | — |
| E11 Fornecedor | 5 | PNG, formato aberto; consumo não depende de fornecedor | — |
| E12 Reversibilidade | 4 | Consulta não produz estado; remoção sem efeito residual | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável, conferida contra os pixels pela trilha Codex e classificada CONFIRMADA (`105`). Não chega a 4 porque o `_CONTEUDO.md` não declara o método pelo qual obteve a descrição desta imagem.
**O que o catálogo afirma:** "Infográfico “How AI is perceived”. Na ponta visível, iniciantes “usam ChatGPT para tudo”. Abaixo da linha d’água, o praticante combina ferramentas por função… A base termina em “sistemas de IA que substituem workflows”."
**Confere com a fonte:** sim — CONFIRMADA em `105`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "maturidade não é trocar um chatbot por outro; é decompor o trabalho em capacidades e montar uma pilha" | `_CONTEUDO.md` área 01 | ALEGAÇÃO DO CATÁLOGO | não |
| "sistemas de IA que substituem workflows" | print (texto observado) | ALEGAÇÃO DO AUTOR | não |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 | não | `E06 ≠ 0` |
| V2 | **sim** | `E06 = ND` → teto: PADRÃO A ESTUDAR / REFERÊNCIA / EXIGE PESQUISA |
| V3 | não | `E07 ≠ 0` |
| V4 | **sim** | `E07 = ND` → nunca CANDIDATO FORTE nem CANDIDATO A PILOTO |
| V5 | não | `LV = 3` |
| V6 | não | 5 ND de 15 (< 8) |
| V7 | não | `E15 = 3` |
| V8 | não | hash reconferido confere |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta, não candidato a componente, com `LV ≥ 3`; dentro do teto imposto por V2 e V4.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-01-PRT-002 — `Captura de tela 2026-07-28 163806.png`

**Tipo:** PRINT
**Área:** 01_DECIDIR-MODELO-E-ESCOPO
**Hash F0:** `F4E903F49157D1A6`   **Hash reconferido:** `F4E903F49157D1A6`   **Confere:** sim
**LV:** LV3-V
**Cobertura da leitura:** inspeção visual do original pela trilha Codex (`105`, lote 07); descrição do `_CONTEUDO.md` confrontada com os pixels. Esta frente não abriu a imagem.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** AC-01-PRT-002 · `H-P1-001` (relatório `105`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só imagem de opinião: meme sem eixos, escala, fonte ou critério declarado (`_CONTEUDO.md`; CONFIRMADA em `105`). Nenhum artefato inspecionável corresponde à afirmação | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e seu estágio |
| E05 Manutenção | ND | — | Localizar canal de origem com data |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial ou instrução ao leitor |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos do meme |
| E13 Testes/evals | ND | — | Nenhum artefato testável associado |
| E15 Alegações ⚠ | 3 | Nenhum número em jogo; a única afirmação é qualitativa (“respeito”), sem métrica (`105`: "Humor não constitui evidência sobre comportamento do modelo") | — |

**NF = 1 · 2/7 · 5 ND** *(mediana de [1,3] = 2 → §14.3 vale o inferior: 1)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 1 | Tangencia a área — cita modelos —, mas o núcleo é percepção social, não critério de escolha por tarefa | — |
| E04 Transferibilidade | 1 | Só a ideia (“há percepção social diferente da técnica”) viaja; nada da implementação | — |
| E14 Diferencial | 1 | Conveniência sobre algo já acessível; nenhuma capacidade nova | — |

**RP = 1 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação; formato de consumo não declarado | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 212,6 KB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = uma entrada em `105`, superfície delimitada | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado; remoção sem resíduo | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — o catálogo descreve o item com detalhe verificável (divisória, logotipos de cada lado, ausência de eixos) e o detalhe confere na inspeção visual (`105`, CONFIRMADA).
**O que o catálogo afirma:** "Meme sem eixos, escala, fonte ou critério declarado. Uma linha vertical divide os logotipos… **O que extrair:** nada quantitativo. É percepção social do autor, não benchmark."
**Confere com a fonte:** sim — CONFIRMADA em `105`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "É percepção social do autor, não benchmark. Pode sugerir modelos a investigar, mas não deve orientar roteamento nem compra." | `_CONTEUDO.md` área 01 | ALEGAÇÃO DO CATÁLOGO | não |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 | não | `E06 ≠ 0` |
| V2 | **sim** | `E06 = ND` |
| V3 | não | `E07 ≠ 0` |
| V4 | **sim** | `E07 = ND` |
| V5 | não | `LV = 3` |
| V6 | não | 5 ND de 15 |
| V7 | não | `E15 = 3` |
| V8 | não | hash confere |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; `E01 = 1` (≠ 0), portanto **não** cabe REJEITADO.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-01-PRT-003 — `frontend ranking.png`

**Tipo:** PRINT
**Área:** 01_DECIDIR-MODELO-E-ESCOPO
**Hash F0:** `D97296B446732B44`   **Hash reconferido:** `D97296B446732B44`   **Confere:** sim
**LV:** LV3-V
**Cobertura da leitura:** inspeção visual do original pela trilha Codex (`105`, lote 07), com conferência linha a linha do ranking contra o `_CONTEUDO.md`. Esta frente não abriu a imagem.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** AC-01-PRT-003 · `H-P1-001` (relatório `105`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Captura isolada de um placar (Code Arena / Arena.ai): exemplo não reprodutível — a imagem exibe posições e Elo, sem insumo, data ou procedimento (`105`) | — |
| E03 Maturidade | ND | — | Acessar a fonte Arena.ai e verificar versionamento/metodologia do ranking |
| E05 Manutenção | ND | — | Verificar a cadência de atualização do placar na origem |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial ou instrução ao leitor |
| E07 Licença ⚠ | ND | — | Identificar termos de uso do conteúdo da Arena.ai |
| E13 Testes/evals | ND | — | Obter a metodologia e os dados do placar na origem |
| E15 Alegações ⚠ | 1 | Alegações numéricas fortes (Elo 1.654 a 1.506; 15 posições) com fonte citada — Code Arena/Arena.ai — porém não conferida e não conferível com o material disponível. O próprio catálogo registra barra hachurada e ausência de data | — |

**NF = 1 · 2/7 · 5 ND** *(mediana de [1,2] = 1,5 → §14.3 vale o inferior)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: comparação de modelos por tipo de tarefa (geração de frontend) | — |
| E04 Transferibilidade | 2 | O padrão — escolher modelo por tarefa medindo distância de desempenho — é transferível; os números são do contexto e da data do autor | — |
| E14 Diferencial | 2 | Agregação de material público; sobrepõe AC-01-PRT-005 na função de comparar modelos | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação; formato de consumo não declarado | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 1,2 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `105` + tabela do `_CONTEUDO.md`, < 1 MB | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 2** — **PARCIAL** em `105`: o catálogo captura líderes e famílias posteriores mas **omite as posições intermediárias 6–8, 11 e 14** (Claude Opus 4.6 Thinking, Opus 4.8, Opus 4.6, Sonnet 4.6, Muse Spark) e simplifica a ordem ao escrever “seguem GLM/Qwen/Kimi/MiniMax/Gemini”. Detalhe verificável presente, mas parte dele **não confere** → não alcança 3 (§14.4 e §6, âncora 3).
**O que o catálogo afirma:** "Top 5: 1º Claude Fable 5 (High) 1.654, 2º GLM-5.2 (Max) 1.595, 3º Claude Opus 4.7 Thinking 1.566, 4º Claude Opus 4.8 Thinking 1.561, 5º Claude Opus 4.7 1.556. Seguem GLM-5.1, Qwen-3.7 Max, Kimi-K2.6, MiniMax-M3, Gemini-3.5 Flash — todos entre 1.506 e 1.531."
**Confere com a fonte:** parcialmente — enumeração incompleta, correção material registrada em `105` §“Quatro correções materiais”, item 1

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "a diferença entre o 2º e o 15º lugar é de ~90 pontos Elo" | `_CONTEUDO.md` área 01 | ALEGAÇÃO DO CATÁLOGO | não — `NÃO VERIFICADA` |
| "a fonte marca Claude Fable 5 como não amostrado no momento (barra hachurada) e não traz data explícita" | `_CONTEUDO.md` área 01 | ALEGAÇÃO DO CATÁLOGO | não |
| Elo 1.654 (1º) … 1.506–1.531 (posições seguintes) | print (texto observado) | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 | não | `E06 ≠ 0` |
| V2 | **sim** | `E06 = ND` |
| V3 | não | `E07 ≠ 0` |
| V4 | **sim** | `E07 = ND` |
| V5 | não | `LV = 3` |
| V6 | não | 5 ND de 15 |
| V7 | não | `E15 = 1` (≠ 0) |
| V8 | não | hash confere |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** §9 — relevância aparente (`E01 = 3`) somada a lacuna nomeada e endereçável; teto respeitado (V2/V4).
**Se EXIGE PESQUISA — lacuna nomeada:** data, versão, amostragem e metodologia do placar Code Arena, mais as posições 6–8, 11 e 14 omitidas pelo catálogo.  **Verificação que a fecharia:** consultar a página Arena.ai/Code Arena na origem, registrar data e critério de amostragem, e recuperar a ordem completa do print.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-01-PRT-004 — `melhroes iA 2026.png`

**Tipo:** PRINT
**Área:** 01_DECIDIR-MODELO-E-ESCOPO
**Hash F0:** `C17746D57845EACE`   **Hash reconferido:** `C17746D57845EACE`   **Confere:** sim
**LV:** LV3-V
**Cobertura da leitura:** inspeção visual do original pela trilha Codex (`105`, lote 07). Esta frente não abriu a imagem. Grafia do nome preservada como está no disco (`05` §10).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** AC-01-PRT-004 · `H-P1-001` (relatório `105`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só listagem: pirâmide de nomes por categoria, sem critério, pontuação, insumo ou artefato inspecionável (`_CONTEUDO.md`: "é uma lista sem pontuação nem critério") | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e seu estágio |
| E05 Manutenção | ND | — | Localizar canal de origem com data |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial ou instrução ao leitor |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos do infográfico |
| E13 Testes/evals | ND | — | Nenhum artefato testável associado |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas (“melhores IAs de 2026” por categoria); nenhum número decisivo. `105`: "Ano, atualidade e superioridade permanecem alegações não verificadas" | — |

**NF = 1 · 2/7 · 5 ND** *(mediana de [1,3] = 2 → §14.3 vale o inferior: 1)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça a pergunta de forma genérica: mapeia categorias de ferramenta sem particularizar critério de escolha | — |
| E04 Transferibilidade | 2 | O padrão (inventário por categoria) transfere; a seleção de produtos é do autor e datada | — |
| E14 Diferencial | 1 | Conveniência sobre inventário já acessível; sobrepõe AC-01-PRT-001 e AC-06-PRT-001 | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 1,7 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `105` + parágrafo do `_CONTEUDO.md` | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (seis faixas e os produtos de cada uma) conferida contra os pixels e classificada CONFIRMADA (`105`).
**O que o catálogo afirma:** "Pirâmide em português, seis faixas: Assistentes (ChatGPT, Claude, Gemini, Perplexity) · Pesquisa (NotebookLM, Perplexity) · Programação (Cursor, Claude Code, Bolt.new, Replit) · Design (Canva, Figma AI, Gamma) · Vídeo (Google Veo, Runway, Higgsfield, HeyGen, OpusClip, Descript) · Automação (n8n, Make, Zapier, Lindy, Chatbase)."
**Confere com a fonte:** sim — CONFIRMADA em `105`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "serve para mapear candidatos a integrar em vez de construir, não para decidir. Trate como inventário, não como ranking." | `_CONTEUDO.md` área 01 | ALEGAÇÃO DO CATÁLOGO | não |
| "melhores IAs de 2026" (título do print) | print (texto observado) | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 | não | `E06 ≠ 0` |
| V2 | **sim** | `E06 = ND` |
| V3 | não | `E07 ≠ 0` |
| V4 | **sim** | `E07 = ND` |
| V5 | não | `LV = 3` |
| V6 | não | 5 ND de 15 |
| V7 | não | `E15 = 3` |
| V8 | não | hash confere |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`, dentro do teto de V2/V4.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-01-PRT-005 — `ops 5 cenchmark.png`

**Tipo:** PRINT
**Área:** 01_DECIDIR-MODELO-E-ESCOPO
**Hash F0:** `D8E3DB6B322C68A5`   **Hash reconferido:** `D8E3DB6B322C68A5`   **Confere:** sim
**LV:** LV3-V
**Cobertura da leitura:** inspeção visual do original pela trilha Codex (`105`, lote 07), com conferência linha a linha da tabela contra o `_CONTEUDO.md`. Esta frente não abriu a imagem.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** AC-01-PRT-005 · `H-P1-001` (relatório `105`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Captura isolada de uma tabela de benchmarks: exemplo não reprodutível; os benchmarks são nomeados (Frontier-Bench v0.1, GDPval-AA v2, ARC-AGI-3, BrowseComp, OSWorld 2.0, DeepSWE v1.1, FrontierCode v1.1, AutomationBench, HealthBench Professional) mas nenhum insumo ou script acompanha | — |
| E03 Maturidade | ND | — | Acessar a fonte primária de cada benchmark e verificar versão/estabilidade |
| E05 Manutenção | ND | — | Verificar cadência de publicação das tabelas na origem |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial ou instrução ao leitor |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos de uso da tabela |
| E13 Testes/evals | ND | — | Obter dados, critérios e execução reprodutível dos benchmarks citados |
| E15 Alegações ⚠ | 1 | Alegações numéricas fortes (43,3% · 1861 · 30,2% · 90,8% · 70,6% · 68,8% · 72,7% · 66,0% …) com fonte citada — nomes e versões de benchmark — porém não conferidas e não conferíveis com o material disponível. `105` registra ainda que a célula vencedora em Health e Biology exibe **“Mythos 5” sob a coluna Fable 5** | — |

**NF = 1 · 2/7 · 5 ND** *(mediana de [1,2] = 1,5 → §14.3 vale o inferior)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central da área — desempenho comparado por tipo de tarefa, base para roteamento de modelo | — |
| E04 Transferibilidade | 2 | O padrão (matriz benchmark × modelo para decidir roteamento) transfere; os números são datados e do contexto do autor | — |
| E14 Diferencial | 2 | Agregação de material público; concorre com AC-01-PRT-003 na mesma função | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 566,8 KB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `105` + tabela transcrita no `_CONTEUDO.md` | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 2** — **PARCIAL** em `105`: o catálogo afirma 13 linhas mas transcreve 10, **omitindo linhas de reasoning multidisciplinar (sem/com ferramentas) e Biology**; além disso normaliza para “Fable 5” uma célula cujo texto observado é **“Mythos 5”**. Detalhe verificável presente e parcialmente não conferido → teto 2 (§14.4).
**O que o catálogo afirma:** "Tabela de quatro colunas: **Opus 5**, **Fable 5**, **Opus 4.8** e **GPT-5.6 Sol**, em treze linhas de benchmark." (seguida de tabela com 10 linhas)
**Confere com a fonte:** parcialmente — correção material 2 de `105`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Opus 5 lidera na maioria, mas **perde em DeepSWE (GPT-5.6), Legal e Health (Fable 5)**" | `_CONTEUDO.md` área 01 | ALEGAÇÃO DO CATÁLOGO | não |
| "Isso é argumento direto contra escolher um modelo único para tudo — a arquitetura deve prever **roteamento de modelo por tipo de tarefa**" | `_CONTEUDO.md` área 01 | ALEGAÇÃO DO CATÁLOGO + `DECISÃO DE ESCOPO DE TERCEIRO` (prescreve arquitetura) | não — instrução não obedecida (§14.5) |
| Percentuais e pontuações por benchmark (43,3% · 1861 · 72,7% · 66,0% …) | print (texto observado) | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 | não | `E06 ≠ 0` |
| V2 | **sim** | `E06 = ND` |
| V3 | não | `E07 ≠ 0` |
| V4 | **sim** | `E07 = ND` |
| V5 | não | `LV = 3` |
| V6 | não | 5 ND de 15 |
| V7 | não | `E15 = 1` (≠ 0) |
| V8 | não | hash confere |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** §9 — relevância aparente (`E01 = 3`) com lacuna nomeada e endereçável; teto de V2/V4 respeitado.
**Se EXIGE PESQUISA — lacuna nomeada:** origem, data, versão e metodologia das nove famílias de benchmark exibidas; identidade de “Mythos 5”; as três linhas omitidas pelo catálogo.  **Verificação que a fecharia:** localizar a publicação primária de cada benchmark citado, registrar data e protocolo, e recuperar a tabela completa do print.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-01-VID-001 — `Free Claude Code.mp4`

**Tipo:** VÍDEO
**Área:** 01_DECIDIR-MODELO-E-ESCOPO
**Hash F0:** `8E00C68D6B3B30B5`   **Hash reconferido:** `8E00C68D6B3B30B5`   **Confere:** sim
**LV:** LV3-V + LV3-A *(a combinação não produz LV4 — `04` §10.2.1)*
**Cobertura da leitura:** ficha visual de 9 quadros (4%–92% da duração) em `95` sob `H-M2-002`; transcrição automática bruta integral (59,5 s, `en`, 14 segmentos, p = 0,925) em `TRANSCRICOES-BRUTAS-STT/01_.../AC-01-VID-001`. Nenhuma revisão humana da fala. Binário não aberto por esta frente.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** AC-01-VID-001 · `H-M2-002` (visual, relatório `95`) · `H-M3-001` (áudio, manifesto `117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Demonstração isolada e não reprodutível: os quadros mostram a instalação (`npm install -g omniroute`), o painel e a lista de provedores, mas nenhum insumo, configuração ou procedimento acompanha o vídeo (`95`) | — |
| E03 Maturidade | ND | — | Localizar o repositório/produto OmniRoute e inspecionar versão, release e estabilidade de interface |
| E05 Manutenção | ND | — | Localizar o repositório de origem e verificar atividade datada |
| E06 Segurança ⚠ | ND | — | Inspecionar diretamente o pacote `omniroute`: custódia de chave de API, destino do tráfego e escopo de permissão. O material demonstra colar chave de agregador em painel de terceiro — superfície declarada, não inspecionada |
| E07 Licença ⚠ | ND | — | Identificar o repositório do produto e ler o texto da licença na origem |
| E13 Testes/evals | ND | — | Localizar o repositório e inspecionar diretório de testes |
| E15 Alegações ⚠ | 0 | A proposta central (“gateway gratuito”) **depende** de números fortes sem fonte: “over 460 models” (LV3-A, 00:00:13–18), “39 provedores” e “≈1,4 bilhão de tokens/mês” (LV3-V, `95`), “number one repo of the day” (LV3-A, 00:00:18–21). Nenhum é verificável com o material disponível | — |

**NF = 1 · 2/7 · 5 ND** *(mediana de [0,2] = 1)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: acesso e troca de modelo por provedor, com efeito direto em custo e escopo do sistema | — |
| E04 Transferibilidade | 2 | O **padrão** (camada de roteamento entre agente e provedores) é transferível; a implementação demonstrada depende de conta, chave e painel de terceiro | — |
| E14 Diferencial | 2 | Agregação de capacidade pública já conhecida (agregadores de modelo); o próprio material remete a OpenRouter como alternativa equivalente | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental para efeitos de consumo (§14.1): o vídeo não requer instalação e não declara formato de consumo. *A ferramenta que ele retrata não foi pontuada aqui* | — |
| E09 Custo | 5 | Sem custo recorrente para consultar; MP4 local de 57,1 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual em `95` + ficha STT de 47 linhas; < 1 MB, superfície delimitada | — |
| E11 Fornecedor | 5 | MP4 em container aberto; consulta não depende de fornecedor | — |
| E12 Reversibilidade | 4 | Consulta sem estado; remoção sem resíduo | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 1** — o próprio `_CONTEUDO.md` classifica o item sob "Vídeos (NÃO são legíveis por IA — catalogados por título)" e rotula a coluna como "Assunto pelo título": descrição declaradamente derivada do nome do arquivo, sem indício de inspeção. O conteúdo observado (gateway OmniRoute) é compatível com “usar Claude Code sem custo”, mas a compatibilidade não eleva a nota (§6, âncora 1).
**O que o catálogo afirma:** "`Free Claude Code.mp4` | 60 MB | como usar Claude Code sem custo / plano gratuito | não transcrito"
**Confere com a fonte:** sim, em nível genérico — o conteúdo é sobre acesso gratuito a modelos via gateway, não sobre plano gratuito do produto. Divergência de tamanho (60 MB × 57,1 MB) já resolvida como D-09 (conversão MiB→MB), não reaberta.

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "you have access to over 460 models when using Cloud Code" | LV3-A bruto, 00:00:13,400–00:00:18,040 — **fala provável, não citação exata** | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "it's rightfully placed as the number one repo of the day" | LV3-A bruto, 00:00:18,040–00:00:21,880 — fala provável | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "Alega agregar tiers gratuitos de 39 provedores/460+ modelos e cerca de 1,4 bilhão de tokens/mês" | `95` (texto visual observado) | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "Just became completely free… unlimited usage in one install" | LV3-A bruto, 00:00:00–00:00:05 — fala provável | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |

> O motor de STT grafou "OmniRoot" e "Cloud Code"; o material visual grafa "OmniRoute" e "Claude Code". Registrado como divergência de transcrição automática, não corrigido no texto bruto (`117`, regra de uso).

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 | não | `E06 ≠ 0` — injeção/credencial não confirmadas por inspeção |
| V2 | **sim** | `E06 = ND` |
| V3 | não | `E07 ≠ 0` |
| V4 | **sim** | `E07 = ND` |
| V5 | não | `LV = 3` (LV3-V + LV3-A) |
| V6 | não | 5 ND de 15 |
| V7 | **sim** | `E15 = 0` e a relevância do item depende dessa alegação → teto EXIGE PESQUISA |
| V8 | não | hash confere (reconferido também pela trilha STT) |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** V7 (§8) — teto EXIGE PESQUISA; compatível com V2 e V4.
**Se EXIGE PESQUISA — lacuna nomeada:** identidade, repositório, licença, modelo de custódia de chave de API e termos de serviço do produto “OmniRoute”, mais a verificação dos números 460 modelos / 39 provedores / 1,4 bi de tokens.  **Verificação que a fecharia:** localizar o repositório público do produto, ler licença e política de tratamento de credenciais, e conferir os números na documentação primária — sem instalar nem executar.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-01-VID-002 — `Gravando 2026-07-28 153846.mp4`

**Tipo:** VÍDEO
**Área:** 01_DECIDIR-MODELO-E-ESCOPO
**Hash F0:** `A1B951B8AE062FB6`   **Hash reconferido:** `A1B951B8AE062FB6`   **Confere:** sim
**LV:** LV3-V *(LV3-A bruto existe e resultou `SEM FALA LEXICAL CONFIÁVEL` — 1 palavra, p = 0,751)*
**Cobertura da leitura:** ficha visual de 9 quadros em `95` sob `H-M2-002`; ficha STT em `TRANSCRICOES-BRUTAS-STT/01_.../AC-01-VID-002` (18,1 s, sem fala aproveitável). Binário não aberto por esta frente.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** AC-01-VID-002 · `H-M2-002` (visual, relatório `95`) · `H-M3-001` (áudio, manifesto `117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só narrativa visual: carrossel com o padrão “orquestrador caro + executores baratos”, sem artefato inspecionável (configuração, roteador, medição) que corresponda ao que afirma (`95`) | — |
| E03 Maturidade | ND | — | Identificar o artefato/produto que implementa o padrão e inspecionar seu estágio |
| E05 Manutenção | ND | — | Localizar a publicação de origem com data e cadência |
| E06 Segurança ⚠ | ND | — | Nenhuma superfície de risco inspecionada; resolveria inspecionar a implementação concreta do roteamento, se existir |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos do carrossel |
| E13 Testes/evals | ND | — | Obter o experimento que sustenta os percentuais exibidos |
| E15 Alegações ⚠ | 0 | A proposta central depende de dois números fortes sem fonte: **“54% de economia” e “96% de desempenho”** (`95`). Não verificáveis com o material disponível | — |

**NF = 0 · 2/7 · 5 ND** *(mediana de [0,1] = 0,5 → §14.3 vale o inferior)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: qual modelo para qual papel, com o padrão inverso (executor barato + consultor sob demanda) explicitado nos quadros | — |
| E04 Transferibilidade | 3 | Padrão transferível com adaptação declarada e delimitada — a separação planejador/executor não depende de ambiente do autor; os nomes de modelo, sim | — |
| E14 Diferencial | 2 | Agregação de material público; o mesmo padrão reaparece em AC-08-VID-003, AC-08-VID-007 e AC-03-VID-005 dentro do próprio acervo | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação; formato de consumo não declarado | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 7,9 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual em `95` + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — o `_CONTEUDO.md` rotula a coluna como "Título pelo conteúdo visível" (**método declarado**) e os quadros entregues pelo Codex **confirmam o método**: o assunto catalogado corresponde ao conteúdo visual, não ao nome do arquivo (que é apenas `Gravando 2026-07-28 153846.mp4`). Condição de `NC = 5` de `04` §6.1.5 satisfeita.
**O que o catálogo afirma:** "`Gravando 2026-07-28 153846.mp4` | 7,9 MB | Fable 5 líder + Sonnet 5 operários: roteamento por custo e desempenho | não transcrito"
**Confere com a fonte:** sim — `95`: "carrossel com orquestrador “Fable 5”, workers “Sonnet 5” e padrão inverso de executor barato com consultor sob demanda"

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Alega 54% de economia e 96% de desempenho" | `95` (texto visual observado) | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "os três vídeos trazem rankings ou economia declarada por seus autores. Confirmar fonte, data, preço e metodologia antes de transformar qualquer posição em regra de roteamento." | `_CONTEUDO.md` área 01 | ALEGAÇÃO DO CATÁLOGO | não |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 | não | `E06 ≠ 0` |
| V2 | **sim** | `E06 = ND` |
| V3 | não | `E07 ≠ 0` |
| V4 | **sim** | `E07 = ND` |
| V5 | não | `LV = 3` |
| V6 | não | 5 ND de 15 |
| V7 | **sim** | `E15 = 0` e a proposta depende dos percentuais → teto EXIGE PESQUISA |
| V8 | não | hash confere |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** V7 (§8) — teto EXIGE PESQUISA; compatível com V2 e V4.
**Se EXIGE PESQUISA — lacuna nomeada:** procedência e método dos números “54% de economia” e “96% de desempenho”, e identidade/versão dos modelos nomeados no carrossel.  **Verificação que a fecharia:** benchmark local próprio comparando planejador caro + executor barato contra modelo único, com tarefas e critérios definidos por esta casa — e não a repetição do número do autor.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-01-VID-003 — `Gravando 2026-07-28 160504.mp4`

**Tipo:** VÍDEO
**Área:** 01_DECIDIR-MODELO-E-ESCOPO
**Hash F0:** `654D7FBD89519866`   **Hash reconferido:** `654D7FBD89519866`   **Confere:** sim
**LV:** LV3-V *(LV3-A bruto = `SEM FALA LEXICAL CONFIÁVEL`, 1 palavra, p = 0,751)*
**Cobertura da leitura:** ficha visual de 9 quadros em `95` sob `H-M2-002`; ficha STT em `TRANSCRICOES-BRUTAS-STT/01_.../AC-01-VID-003` (12,5 s). Binário não aberto por esta frente.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** AC-01-VID-003 · `H-M2-002` (relatório `95`) · `H-M3-001` (manifesto `117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só opinião visual: rankings de ferramentas por categoria sem rubrica, teste ou artefato (`95`: "o ranking não tem rubrica nem teste reproduzível") | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e seu estágio |
| E05 Manutenção | ND | — | Localizar canal de origem com data |
| E06 Segurança ⚠ | ND | — | Nenhuma superfície inspecionada; resolveria inspecionar as ferramentas citadas |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Obter o critério e o teste que sustentam o ranking |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas — posições relativas por categoria, sem número decisivo em jogo (`95`) | — |

**NF = 1 · 2/7 · 5 ND** *(mediana de [1,3] = 2 → §14.3 vale o inferior: 1)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça a pergunta de forma genérica: separa categorias (pesquisa, criação de sistemas, automação, imagens) sem particularizar critério | — |
| E04 Transferibilidade | 1 | Só a ideia (“escolher por categoria de trabalho”) viaja; a seleção é preferência do autor | — |
| E14 Diferencial | 1 | Conveniência sobre inventário já acessível; sobrepõe AC-01-VID-006 e AC-06-VID-014 | — |

**RP = 1 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 7,6 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado ("Título pelo conteúdo visível") **e confirmado** pelos quadros: o assunto catalogado corresponde ao conteúdo visual, não ao nome do arquivo (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 160504.mp4` | 7,6 MB | ranking de ferramentas por tarefa: pesquisa, criação de sistemas e imagens | não transcrito"
**Confere com a fonte:** sim — `95`: "pesquisa de mercado (Gemini, Perplexity, ChatGPT), criação de sistemas (Claude Code, Cursor, Lovable), automação (Zapier, Make, Shortcuts) e imagens (Higgsfield, Gemini, Canva)"

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "ranking de ferramentas por tarefa: pesquisa, criação de sistemas e imagens" | `_CONTEUDO.md` área 01 | ALEGAÇÃO DO CATÁLOGO | conferida contra os quadros — confere |
| Posições relativas entre Gemini/Perplexity/ChatGPT, Claude Code/Cursor/Lovable, Zapier/Make/Shortcuts, Higgsfield/Gemini/Canva | `95` (texto visual observado) | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 | não | `E06 ≠ 0` |
| V2 | **sim** | `E06 = ND` |
| V3 | não | `E07 ≠ 0` |
| V4 | **sim** | `E07 = ND` |
| V5 | não | `LV = 3` |
| V6 | não | 5 ND de 15 |
| V7 | não | `E15 = 3` |
| V8 | não | hash confere |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; sem lacuna endereçável que altere a natureza opinativa do item.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-01-VID-004 — `Gravando 2026-07-28 162512.mp4`

**Tipo:** VÍDEO
**Área:** 01_DECIDIR-MODELO-E-ESCOPO
**Hash F0:** `1671949B009E4C96`   **Hash reconferido:** `1671949B009E4C96`   **Confere:** sim
**LV:** LV3-V *(LV3-A bruto = `SEM FALA LEXICAL CONFIÁVEL`, 1 palavra, p = 0,130)*
**Cobertura da leitura:** ficha visual de 9 quadros em `95` sob `H-M2-002`; ficha STT em `TRANSCRICOES-BRUTAS-STT/01_.../AC-01-VID-004` (10,0 s). Binário não aberto por esta frente.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** AC-01-VID-004 · `H-M2-002` (relatório `95`) · `H-M3-001` (manifesto `117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só divulgação: anuncia um modelo aberto e sua posição em arenas, sem artefato, insumo ou procedimento inspecionável (`95`) | — |
| E03 Maturidade | ND | — | Localizar o modelo/repositório na origem e verificar release, pesos e estabilidade |
| E05 Manutenção | ND | — | Verificar atividade datada no repositório de origem |
| E06 Segurança ⚠ | ND | — | Inspecionar o modelo na origem: procedência dos pesos, telemetria, termos |
| E07 Licença ⚠ | ND | — | Ler a licença de pesos e de uso do modelo divulgado |
| E13 Testes/evals | ND | — | Obter os benchmarks citados com dados e critérios |
| E15 Alegações ⚠ | 1 | Alegações numéricas fortes (posição em arenas/benchmarks contra “Fable/Sol”) com fonte citada genericamente — “arenas” e “benchmarks” — porém não conferidas e não conferíveis com o material disponível | — |

**NF = 1 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça a pergunta de forma genérica: apresenta um candidato a modelo sem critério de roteamento por tarefa | — |
| E04 Transferibilidade | 1 | Só a ideia (“avaliar modelo aberto como alternativa”) viaja | — |
| E14 Diferencial | 2 | Agregação de material público; a informação de posição em arena sobrepõe AC-01-PRT-003 | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 6,4 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado ("Título pelo conteúdo visível") **e confirmado** pelos quadros; o nome do arquivo não contém informação de assunto (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 162512.mp4` | 6,4 MB | Kimi K3 no topo da Frontend Code Arena e comparação de benchmarks | não transcrito"
**Confere com a fonte:** sim — `95`: "divulga modelo aberto/gratuito e posição em arenas/benchmarks contra modelos “Fable/Sol”"

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Kimi K3 no topo da Frontend Code Arena" | `_CONTEUDO.md` área 01 | ALEGAÇÃO DO CATÁLOGO | não — `NÃO VERIFICADA` |
| Posição do modelo em arenas e comparação de benchmarks contra “Fable/Sol” | `95` (texto visual observado) | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 | não | `E06 ≠ 0` |
| V2 | **sim** | `E06 = ND` |
| V3 | não | `E07 ≠ 0` |
| V4 | **sim** | `E07 = ND` |
| V5 | não | `LV = 3` |
| V6 | não | 5 ND de 15 |
| V7 | não | `E15 = 1` (≠ 0) |
| V8 | não | hash confere |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** §9 — relevância aparente com lacuna nomeada e endereçável; teto de V2/V4 respeitado.
**Se EXIGE PESQUISA — lacuna nomeada:** identidade, procedência dos pesos, licença de uso comercial e requisitos de hardware do modelo divulgado; data e metodologia da arena citada.  **Verificação que a fecharia:** localizar a publicação primária do modelo, ler a licença de pesos e registrar data/metodologia do placar — sem baixar pesos nem executar.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-01-VID-005 — `Gravando 2026-07-28 180226.mp4`

**Tipo:** VÍDEO
**Área:** 01_DECIDIR-MODELO-E-ESCOPO
**Hash F0:** `234C8B7B9B3319A1`   **Hash reconferido:** `234C8B7B9B3319A1`   **Confere:** sim
**LV:** LV3-V + LV3-A *(a combinação não produz LV4)*
**Cobertura da leitura:** ficha visual de 9 quadros em `95` sob `H-M2-002`; transcrição automática bruta integral (68,9 s, `pt`, 18 segmentos, p = 0,814, **MÉDIA AUTOMÁTICA**, 46 de 348 tokens abaixo de 0,50) em `TRANSCRICOES-BRUTAS-STT/01_.../AC-01-VID-005`. Sem revisão humana. Binário não aberto por esta frente.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** AC-01-VID-005 · `H-M2-002` (relatório `95`) · `H-M3-001` (manifesto `117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só narrativa: classificação por faixas subjetivas, sem artefato nem critério. A fala provável confirma a natureza opinativa (“Foda, bom, dá pra usar, [perda de] tempo”, 00:00:00–00:00:03) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e seu estágio |
| E05 Manutenção | ND | — | Localizar canal de origem com data |
| E06 Segurança ⚠ | ND | — | Nenhuma superfície inspecionada |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Obter critério e teste que sustentem as faixas |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas; nenhum número decisivo em jogo — a fala provável é inteiramente adjetival | — |

**NF = 1 · 2/7 · 5 ND** *(mediana de [1,3] = 2 → §14.3 vale o inferior: 1)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça a pergunta de forma genérica: preferência por ferramenta e por tarefa (transcrição/reunião, audiovisual, referências), sem critério declarado | — |
| E04 Transferibilidade | 1 | Só a ideia viaja; a classificação é preferência pessoal do autor e datada | — |
| E14 Diferencial | 1 | Conveniência sobre inventário já acessível; sobrepõe AC-01-VID-003, AC-01-VID-006 e AC-06-VID-014 | — |

**RP = 1 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 58,8 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT de 51 linhas; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado ("Título pelo conteúdo visível") **e confirmado** por duas evidências independentes: os quadros (`95`) e a fala provável, que reproduz exatamente as quatro faixas descritas pelo catálogo (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 180226.mp4` | 58,8 MB | ranking em tiers de ferramentas e modelos de IA | não transcrito" e "O vídeo mostra uma avaliação opinativa em faixas (“foda”, “bom”, “dá para usar”, “perda de tempo”)."
**Confere com a fonte:** sim — LV3-A bruto 00:00:00–00:00:03 registra as mesmas faixas

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "A posição de cada ferramenta precisa ser tratada como preferência do autor, não benchmark reproduzível." | `_CONTEUDO.md` área 01 | ALEGAÇÃO DO CATÁLOGO | não |
| "um modelo pra áudio visual mais foda do mundo, e tem todos os modelos de todos os LMS lá dentro" | LV3-A bruto, 00:00:09,380–00:00:14,720 — **fala provável, não citação exata** | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "Siri. Pô, bicho. Esquece. É muito ruim. É péssimo." | LV3-A bruto, 00:00:38,600–00:00:42,160 — fala provável | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |

> O motor grafou "Chate a PT", "X-Filge", "Manos", "notebook LLM" e "BigView"; nomes de produto **não** foram normalizados (`117`, regra de uso). Identificação inequívoca das ferramentas citadas depende de revisão do áudio.

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 | não | `E06 ≠ 0` |
| V2 | **sim** | `E06 = ND` |
| V3 | não | `E07 ≠ 0` |
| V4 | **sim** | `E07 = ND` |
| V5 | não | `LV = 3` |
| V6 | não | 5 ND de 15 |
| V7 | não | `E15 = 3` |
| V8 | não | hash confere |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; conteúdo declaradamente opinativo, sem lacuna que o converta em candidato a componente.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-01-VID-006 — `llms para usar.mp4`

**Tipo:** VÍDEO
**Área:** 01_DECIDIR-MODELO-E-ESCOPO
**Hash F0:** `2C903B644BF6F5E3`   **Hash reconferido:** `2C903B644BF6F5E3`   **Confere:** sim
**LV:** LV3-V + LV3-A *(a combinação não produz LV4)*
**Cobertura da leitura:** ficha visual de 9 quadros em `95` sob `H-M2-002`; transcrição automática bruta integral (27,6 s, `pt`, 7 segmentos, p = 0,927, **ALTA AUTOMÁTICA**) em `TRANSCRICOES-BRUTAS-STT/01_.../AC-01-VID-006`. Sem revisão humana. Binário não aberto por esta frente.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** AC-01-VID-006 · `H-M2-002` (relatório `95`) · `H-M3-001` (manifesto `117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só narrativa: a fala provável qualifica ferramentas por tarefa em adjetivos (“ruim”, “maneiro”, “elite”, “fantástico”) sem nenhum artefato inspecionável | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e seu estágio |
| E05 Manutenção | ND | — | Localizar canal de origem com data |
| E06 Segurança ⚠ | ND | — | Nenhuma superfície inspecionada |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Obter critério e teste por trás das qualificações |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas; nenhum número decisivo em jogo (fala provável integral, 7 segmentos, sem cifras) | — |

**NF = 1 · 2/7 · 5 ND** *(mediana de [1,3] = 2 → §14.3 vale o inferior: 1)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça a pergunta de forma genérica: seis categorias de tarefa (pesquisa, programação, automação, imagens, apps/sites, brainstorming) com preferência declarada, sem critério | — |
| E04 Transferibilidade | 1 | Só a ideia (“ferramenta por caso de uso”) viaja | — |
| E14 Diferencial | 1 | Conveniência sobre inventário já acessível; sobrepõe AC-01-VID-003 e AC-01-VID-005 | — |

**RP = 1 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 26,7 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT de 40 linhas; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 1** — o item está na tabela "Vídeos (NÃO são legíveis por IA — catalogados por título)", com a coluna rotulada "Assunto pelo título": descrição declaradamente derivada do nome do arquivo (`llms para usar.mp4` → "quais LLMs escolher"), sem indício de inspeção. Compatível com o conteúdo, mas compatibilidade não eleva a nota.
**O que o catálogo afirma:** "`llms para usar.mp4` | 28 MB | quais LLMs escolher | não transcrito"
**Confere com a fonte:** sim, em nível genérico — o conteúdo observado é ranking de ferramentas por tarefa, mais amplo do que “quais LLMs”

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Pra programação, esse aqui é mais ou menos, esse aqui é bom, mas esse aqui é elite." | LV3-A bruto, 00:00:07,500–00:00:11,900 — **fala provável, não citação exata** | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "Lacuna conhecida: se uma decisão de custo ou de escolha de modelo depender destes dois vídeos, marque como pendente de revisão humana." | `_CONTEUDO.md` área 01 | ALEGAÇÃO DO CATÁLOGO | não |

> A fala provável **não nomeia** as ferramentas (“esse aqui”); a identificação depende dos quadros e permanece parcial. Nenhum nome foi inferido.

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 | não | `E06 ≠ 0` |
| V2 | **sim** | `E06 = ND` |
| V3 | não | `E07 ≠ 0` |
| V4 | **sim** | `E07 = ND` |
| V5 | não | `LV = 3` |
| V6 | não | 5 ND de 15 |
| V7 | não | `E15 = 3` |
| V8 | não | hash confere |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; conteúdo opinativo sem artefato associado.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

## Fechamento da área 01

| Métrica | Valor |
|---|---:|
| Itens representados | 11 / 11 |
| Fichas válidas contra `04` §13 | 11 |
| Hashes reconferidos / divergentes | 11 / **0** |
| `RF = REFERÊNCIA` | 6 |
| `RF = EXIGE PESQUISA` | 5 |
| `RF = INDETERMINADO` | 0 |
| Total de eixos possíveis (11 × 15) | 165 |
| Eixos determinados | 110 |
| Eixos em `ND` | **55 (33,3%)** |
| Divergências catálogo × fonte | 2 parciais (AC-01-PRT-003, AC-01-PRT-005) · 0 divergentes |

Nenhuma fonte foi modificada. Nenhum item foi adotado, ordenado, priorizado ou recomendado.
