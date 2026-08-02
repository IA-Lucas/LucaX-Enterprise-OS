> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

# FICHAS DE EVIDÊNCIA — ÁREA 08 — CUSTO E CONTEXTO

**Fase:** 2 — Extração · **Data:** 2026-07-29 · **Avaliador:** Claude Opus 5 (Fase 2)
**Itens:** 12 — 3 REPO · 1 PRINT · 8 VÍDEO · 0 PLANILHA — **inclui o segundo e último duplicado exato do acervo** (`AC-08-VID-005`)
**Convenções de aplicação:** `00_INDICE-DA-FASE-2.md` §3

**Pergunta central da área (base de E01):** *como não estourar o orçamento de token nem a janela de contexto.*

---

### AC-08-REP-001 — `caveman-main`

**Tipo:** REPO · **Área:** 08_CUSTO-E-CONTEXTO
**Hash F0:** `dir · 167 arq. · aninhado`   **Hash reconferido:** `167 arq. · aninhamento 1`   **Confere:** sim
**LV:** LV4
**Cobertura da leitura:** raiz efetiva `caveman-main/caveman-main` (31 entradas); `LICENSE` — MIT, 1.071 bytes, "Copyright (c) 2026 Julius Brussee", íntegro; `README.md` (15.277 bytes, lidos 6 KB: proposta, badges, índice das seções incluindo *Benchmarks* e *Caveman 2*); listagem de `tests/` (**32 arquivos**), `evals/` (`prompts`, `snapshots`, `llm_run.py`, `measure.py`, `plot.py`) e `benchmarks/` (`results`, `prompts.json`, `run.py`); `.claude-plugin/`; sinais `SECURITY.md`, `install.sh`, `install.ps1`, `skills-lock.json`, `INSTALL.md`. **Não lidos:** `src/`, `skills/`, `agents/`, `commands/`, `dist/`, `docs/`.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** não se aplica

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 4 | Artefato completo e inspecionável (skill, plugins, agentes, comandos, binário e distribuição) **mais** procedimento de verificação declarado em **três camadas separadas**: `tests/` com 32 arquivos, `evals/` com execução por modelo, medição e plotagem, e `benchmarks/` com conjunto de prompts, execução e resultados | — |
| E03 Maturidade | 4 | Versionado com release identificável (`package.json`, `dist/`, `skills-lock.json`) **mais** documentação de instalação e uso (`INSTALL.md`, `install.sh`, `install.ps1` para dois sistemas) **mais** governança visível (`CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `.github/`) | — |
| E05 Manutenção | ND | — | O ano do aviso de copyright (2026) **não é evidência de manutenção** — mesmo tratamento dado em `AC-07-REP-001`. Resolveria consultar os commits na origem pública, que o badge de "last commit" referencia mas não datas |
| E06 Segurança ⚠ | 3 | Superfície declarada — dois instaladores de shell que escrevem na configuração de mais de trinta agentes, mais ganchos — **com controle parcial documentado**: `SECURITY.md` presente, `skills-lock.json` fixando o que é instalado, e `tests/` com `test_compress_safety.py`, `test_symlink_flag.js` e `test_hooks.py`, ou seja, teste nomeado sobre o próprio risco. **Não alcança 4**: o conteúdo dos instaladores não foi lido | — |
| E07 Licença ⚠ | 4 | Permissiva padrão presente e íntegra: MIT, 1.071 bytes, titular nomeado. Cópia local não prova titularidade → teto 4 | — |
| E13 Testes/evals | 4 | Suíte executável identificável **mais** evals de comportamento: `evals/` compara saídas por modelo com instantâneos, e `benchmarks/run.py` mede sobre um conjunto de prompts versionado. Não alcança 5 porque o diretório `benchmarks/results` não foi aberto | — |
| E15 Alegações ⚠ | 2 | Alegação numérica central **conferível dentro da própria fonte, ainda não conferida**: "Same answers, **65% fewer output tokens**". A fonte oferece o instrumento (`benchmarks/`, `evals/`) — é raro no acervo — mas o resultado não foi lido. Há também badge de estrelas e "works with 30+ agents" (**P-3** para o primeiro) | — |

**NF = 4 · 6/7 · 1 ND** *(mediana dos determinados [2,3,4,4,4,4] = 4)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 4 | Endereça diretamente a pergunta central **mais** artefato concreto e reutilizável: ataca a **ponta de saída** do consumo de token, que nenhum outro item do acervo ataca | — |
| E04 Transferibilidade | 4 | Transferível por configuração, sem alteração de código: instalador para dois sistemas, formato de skill/plugin e níveis de compressão selecionáveis | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto **dentro do acervo**: `AC-08-REP-002` e `AC-08-REP-003` comprimem a **entrada**; este corta a **saída**. O próprio catálogo registra que as três são somáveis | — |

**RP = 4 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 4 | Instalação declarada em um comando por sistema operacional, com arquivo de instrução dedicado | — |
| E09 Custo | 5 | Sem custo recorrente: MIT, sem serviço, sem chamada adicional de modelo — o artefato é instrução de estilo | — |
| E10 Contexto/tokens | 4 | Medido: **167 arquivos, 831,1 KB** — o segundo menor repositório do acervo | — |
| E11 Fornecedor | 4 | Abstração documentada: declara funcionar com mais de trinta agentes e traz manifesto para três ecossistemas (`.claude-plugin/`, `.codex/`, `gemini-extension.json`) | — |
| E12 Reversibilidade | 4 | Reversível por remoção, sem efeito residual: é instrução de estilo, não altera dado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (lema literal, 65% menos tokens de saída, 30+ agentes, e a ressalva de que estilo telegráfico degrada saída destinada a humano) e os detalhes conferem com o README lido.
**O que o catálogo afirma:** "*'why use many token when few do trick.'* Faz o agente responder em estilo telegráfico: mesmas respostas, **65% menos tokens de saída**. Funciona em 30+ agentes. **O que extrair:** ataca a ponta oposta do pxpipe e do headroom… **Ressalva:** estilo telegráfico degrada resposta destinada a humano; use em comunicação agente-a-agente, não na saída final."
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Same answers, **65% fewer output tokens**. Brain still big. Mouth small." | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — **conferível dentro da fonte** (`benchmarks/`, `evals/`), não conferida sob o teto de leitura. "Same answers" é a parte forte e não medida |
| "works with 30+ agents" | badge no `README.md` | ALEGAÇÃO DO AUTOR | não — `INSTALL.md` existe e conteria a lista; não lido |
| "estilo telegráfico degrada resposta destinada a humano" | `_CONTEUDO.md` área 08 | ALEGAÇÃO DO CATÁLOGO — ressalva | não observada na fonte sob o teto de leitura; **registrada, não obedecida como instrução** (`05` §7) |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V2 · V3 · V4 · V5 · V6 · V7 · V8 | **nenhuma** | `E06 = 3` · `E07 = 4` · `LV = 4` · 1 ND · `E15 = 2` (≠ 0) · reconferência confere |

#### Resultado
**RF = CANDIDATO A PILOTO**
**Regra que produziu:** §9. **Não** alcança CANDIDATO FORTE: a condição "nenhum eixo do Bloco A abaixo de 3" falha por `E15 = 2`. Satisfaz CANDIDATO A PILOTO: `LV = 4 ≥ 3` · `E06 = 3` · `E07 = 4` · `RP = 4 ≥ 3` · **1 ND** ≤ 4 · nenhum eixo do Bloco C em 0.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> **CANDIDATO A PILOTO não significa pilotar.** Restrições registradas: os 65% não foram conferidos apesar de a fonte trazer o instrumento; `E05 = ND`; e a ressalva do catálogo sobre saída destinada a humano permanece sem evidência a favor ou contra.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-08-REP-002 — `headroom-main`

**Tipo:** REPO · **Área:** 08_CUSTO-E-CONTEXTO
**Hash F0:** `dir · 1967 arq. · aninhado`   **Hash reconferido:** `1967 arq. · aninhamento 1`   **Confere:** sim
**LV:** LV4
**Cobertura da leitura:** raiz efetiva `headroom-main/headroom-main` (**63 entradas** — a maior raiz do acervo); `LICENSE` — Apache License 2.0, 10.770 bytes, íntegro, mais `NOTICE`; `README.md` (31.162 bytes, lidos 6 KB); `CHANGELOG.md` — **início lido**, seção `## Unreleased` com correção de instalação e uma correção de exposição do painel, referenciando `#2056` em `github.com/headroomlabs-ai/headroom`; listagem de `tests/` e de `benchmarks/` (**28 arquivos**, incluindo `adversarial_ccr_tests.py`, `comprehensive_eval.py`, `compression_benchmark.py`, `bench_relevance.py`); `.claude-plugin/`; sinais `SECURITY.md`, `.env.example`, `Dockerfile`, `docker-compose.yml`, `Makefile`, `.gitleaks.toml`, `.gitguardian.yaml`, `deny.toml`, `sbom/`, `codecov.yml`, `.pre-commit-config.yaml`, `release-please`. **Não lidos:** `crates/`, `headroom/`, `sdk/`, `e2e/`, `docs/`, `wiki/`.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** não se aplica

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 4 | Artefato completo e inspecionável (biblioteca Python, crates Rust, SDK, proxy, plugins, painel) **mais** procedimento de verificação declarado e extenso: `tests/`, `e2e/`, `benchmarks/` com 28 arquivos — inclusive **testes adversariais** e avaliação de relevância —, cobertura por `codecov.yml` e `Makefile` como ponto de entrada | — |
| E03 Maturidade | 4 | Versionado com release identificável (`CHANGELOG.md` no formato *Keep a Changelog*, versionamento semântico declarado, `release-please` configurado, `Cargo.lock`, `uv.lock`) **mais** documentação de instalação e uso (`mkdocs.yml`, `wiki/`, `docs/`) **mais** tratamento de erro visível — o próprio changelog descreve correção de caso de borda em rede de contêiner | — |
| E05 Manutenção | ND | — | Há `CHANGELOG.md`, mas o trecho lido é a seção **`Unreleased`, sem data**. Resolveria ler a primeira entrada versionada datada do changelog — leitura curta, dentro da própria fonte, que muito provavelmente move este eixo para 3 ou mais |
| E06 Segurança ⚠ | 4 | **Superfície declarada com controles documentados e automatizados** — o conjunto mais completo do acervo até aqui: `SECURITY.md`, varredura de segredo em duas ferramentas (`.gitleaks.toml`, `.gitguardian.yaml`), lista de negação de dependência (`deny.toml`), **inventário de componentes (`sbom/`)**, ganchos de pré-commit e `.env.example` em vez de credencial embutida. O changelog lido **descreve uma correção de exposição**: metadados por requisição restritos a chamador local. Não alcança 5: nenhuma auditoria externa foi lida | — |
| E07 Licença ⚠ | 4 | Permissiva padrão presente e íntegra: Apache License 2.0, 10.770 bytes, acompanhada de `NOTICE`. Cópia local não prova titularidade → teto 4 | — |
| E13 Testes/evals | 4 | Suíte executável identificável com ponto de entrada (`Makefile`, `codecov.yml`) **mais** evals: `comprehensive_eval.py`, `bench_relevance.py` e testes adversariais medem **preservação de informação**, que é exatamente o risco da técnica. Não alcança 5: nenhum resultado publicado foi lido | — |
| E15 Alegações ⚠ | 2 | Alegações numéricas fortes **conferíveis dentro da própria fonte, ainda não conferidas**: "60–95% menos token em dados JSON" e "15–20% em agentes de código", mais a existência de modelo próprio publicado. A fonte traz o instrumento de medição — não o resultado lido | — |

**NF = 4 · 6/7 · 1 ND** *(mediana dos determinados [2,4,4,4,4,4] = 4)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 4 | Endereça diretamente a pergunta central **mais** artefato concreto e reutilizável: comprime a **entrada** com consciência de tipo de conteúdo | — |
| E04 Transferibilidade | 4 | Transferível por configuração, sem alteração de código: declara três formas de consumo — biblioteca, proxy e MCP —, com contêiner pronto | — |
| E14 Diferencial | 4 | Sem equivalente no acervo **mais** custo alto de reconstrução: compressão **reversível** e consciente de tipo, com modelo próprio treinado e conjunto de benchmarks adversariais. Reconstruir isso é projeto, não tarefa | — |

**RP = 4 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Instalação declarada, porém com **runtime adicional**: pilha Python **e** Rust (`Cargo.toml`, `rust-toolchain.toml`), com contêiner como alternativa | — |
| E09 Custo | 4 | Custo marginal: Apache-2.0, local-first; o custo é processamento de compressão e, se usado, o modelo próprio | — |
| E10 Contexto/tokens | 1 | Medido: **1.967 arquivos, 57,1 MB** — contagem na faixa 1.000–5.000 e tamanho na faixa 20–100 MB | — |
| E11 Fornecedor | 3 | Abstração parcial: local-first e com três interfaces, mas o desempenho declarado está ligado a um modelo próprio publicado pelo autor | — |
| E12 Reversibilidade | 4 | Reversível por remoção, sem efeito residual — reforçado pelo fato de a compressão ser declarada reversível, o que evita dado degradado permanente | — |

**AA = 3 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (lema literal, os dois intervalos numéricos, três formas de consumo, local-first, reversível, Apache 2.0, publicação em dois repositórios de pacote e modelo próprio nomeado) e os detalhes conferem com o README e a raiz lidos.
**O que o catálogo afirma:** "'The context compression layer for AI agents.' Declara **60–95% menos token em dados JSON** e **15–20% em agentes de código**. Disponível como biblioteca, proxy e MCP… local-first e **reversível**. Apache 2.0, publicado em PyPI e npm, com modelo próprio no HuggingFace (Kompress-v2-base). **O que extrair:** a reversibilidade. Compressão que não se desfaz é perda de informação disfarçada de economia."
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "60–95% menos token em dados JSON" e "15–20% em agentes de código" | `README.md` da fonte, via catálogo | ALEGAÇÃO DO AUTOR | não — **conferível dentro da fonte** (`benchmarks/compression_benchmark.py`, `comprehensive_eval.py`), não conferida |
| compressão "**reversível**" | `README.md` da fonte, via catálogo | ALEGAÇÃO DO AUTOR — **é a alegação crítica**, porque define se há perda de informação | não — `tests/test_compression` e os testes adversariais existem e a testariam; não lidos |
| "o dashboard… é restrito a chamadores em loopback via `_request_is_loopback`" | `CHANGELOG.md` da fonte | **FATO OBSERVADO** — o autor documenta uma correção de exposição | sim, como registro; o efeito da correção não foi verificado |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V2 · V3 · V4 · V5 · V6 · V7 · V8 | **nenhuma** | `E06 = 4` · `E07 = 4` · `LV = 4` · 1 ND · `E15 = 2` (≠ 0) · reconferência confere |

#### Resultado
**RF = CANDIDATO A PILOTO**
**Regra que produziu:** §9. **Não** alcança CANDIDATO FORTE: a condição "nenhum eixo do Bloco A abaixo de 3" falha por `E15 = 2`. Satisfaz CANDIDATO A PILOTO: `LV = 4` · `E06 = 4` · `E07 = 4` · `RP = 4` · **1 ND** · nenhum eixo do Bloco C em 0.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> **CANDIDATO A PILOTO não significa pilotar.** Restrições registradas: os dois intervalos de economia não foram conferidos; a **reversibilidade**, que é o argumento central, não foi verificada; `E05 = ND` por um detalhe de leitura, não por ausência de changelog; e `E08 = 3` por exigir duas pilhas de runtime.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-08-REP-003 — `pxpipe`

**Tipo:** REPO · **Área:** 08_CUSTO-E-CONTEXTO
**Hash F0:** `dir · 501 arq.`   **Hash reconferido:** `501 arq. · aninhamento 0`   **Confere:** sim
**LV:** LV4
**Cobertura da leitura:** raiz efetiva `pxpipe` (**profundidade 0** — não é cópia aninhada; 23 entradas); `LICENSE` — MIT, 1.109 bytes, "Copyright (c) 2026 claude-image-proxy contributors", íntegro; `README.md` (19.413 bytes, lidos 6 KB: proposta, mecanismo, números declarados e a autoqualificação do autor); `CHANGELOG.md` — **entrada `## 0.9.0 — 2026-07-14` lida**, com política de versionamento declarada; `package.json`; listagem de `tests/` (**44 arquivos**) e de `eval/` (**332 arquivos**, com `swe-bench`, `swe-bench-pro`, `gsm8k`, `needle-haystack`, `gist-recall`, `glyph-matrix`, `opus-density`, `results`); presença de `FINDINGS.md`, `bench/`, `vitest.config.ts`, `wrangler.toml`; **e de `.git/` na raiz**. **Não lidos:** `src/`, `bin/`, `docs/`, `demo/`, `FINDINGS.md`.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** cruzado com `AC-08-VID-006` (`94`, `H-M2-001`)

> **Achado estrutural — único no acervo.** Este item **não é uma cópia `-main` sem histórico**: a raiz contém `.git/`, e `.git/logs/HEAD` registra `clone: from https://github.com/teamchong/pxpipe`. Isso (a) confirma a origem declarada, (b) torna `E05` resolvível **dentro da fonte**, ao contrário da regra geral de acervo do `04` §5, e (c) significa que os 501 arquivos contados incluem objetos de repositório. Registrado como fato, sem alterar a contagem do manifesto.

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 4 | Artefato completo e inspecionável **mais** o aparato de verificação mais extenso do acervo até aqui: `tests/` com 44 arquivos nomeados por comportamento (alinhamento de cache, visão, integridade de documentação, abstenção) e `eval/` com **332 arquivos** organizados por benchmark público — `swe-bench`, `gsm8k`, `needle-haystack` — mais `results/` e `FINDINGS.md` | — |
| E03 Maturidade | 4 | Versionado com release identificável (`CHANGELOG.md`, `0.9.0`, política de versionamento **explicitada para a fase pré-1.0**) **mais** documentação de uso **mais** tratamento de comportamento de borda descrito no changelog (perfil de modelo deixa de ser silenciosamente ativado e passa a ser opt-in) | — |
| E05 Manutenção | **3** | **Atividade recente identificável por evidência datada dentro da fonte**: `CHANGELOG.md` traz `0.9.0 — 2026-07-14`, **quinze dias antes desta avaliação**, e o registro de clone em `.git/logs/HEAD` é da mesma janela. **Não alcança 4**: o titular declarado é coletivo ("contributors"), sem responsável nomeado, e nenhum canal de reporte foi lido | — |
| E06 Segurança ⚠ | **1** | **Risco ativo declarado por terceiro e ainda não confirmado por inspeção** — âncora 1, literal. A trilha Codex registra em `94`: converter texto em imagem "pode reduzir fidelidade, acessibilidade, capacidade de busca, auditabilidade e **proteção contra injeção**", e que "o artefato não demonstra preservação semântica nem segurança". Some-se a superfície: é um **proxy local que intercepta e reescreve toda requisição antes de sair da máquina**, e não há `SECURITY.md` na raiz efetiva (procurado, ausente) | — |
| E07 Licença ⚠ | 4 | Permissiva padrão presente e íntegra: MIT, 1.109 bytes. Titular coletivo, o que não impede a permissão. Cópia local não prova titularidade → teto 4 | — |
| E13 Testes/evals | 4 | Suíte executável identificável (`vitest.config.ts`, 44 testes) **mais** evals de comportamento sobre benchmarks públicos reconhecíveis, incluindo recuperação de agulha em contexto longo — que é o teste correto para a técnica proposta. Não alcança 5: `eval/results` e `FINDINGS.md` não foram abertos | — |
| E15 Alegações ⚠ | 2 | Alegações numéricas fortes **conferíveis dentro da própria fonte, ainda não conferidas**: "~3,1 caracteres por token de imagem contra ~1 por token de texto", "≈48 mil caracteres… ≈25 mil tokens como texto, ≈2,7 mil como imagem", "**~59–70% de fatura menor**". **Registro a favor da fonte:** o autor **qualifica explicitamente** — preços mudam e cargas diferem, então o número durável seria o corte de token medido por requisição contra um contrafactual gratuito, gravado em arquivo local. Isso é medição declarada, não prova social | — |

**NF = 4 · 7/7 · 0 ND** *(mediana de [1,2,3,4,4,4,4] = 4)*

> **Primeiro item do acervo com Bloco A integralmente determinado — 0 ND em 7 eixos.** É consequência direta de o item trazer licença, changelog datado, testes, evals e histórico de repositório na própria fonte.

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 4 | Endereça diretamente a pergunta central **mais** artefato concreto e reutilizável: ataca o custo de **entrada** por um mecanismo que nenhum outro item do acervo usa | — |
| E04 Transferibilidade | 4 | Transferível por configuração, sem alteração de código: é proxy local, colocado entre o agente e a API | — |
| E14 Diferencial | 4 | Sem equivalente no acervo **mais** custo alto de reconstrução: perfis de renderização por modelo, atlas de fonte, geometria de célula e a matemática de rentabilidade são trabalho de medição que não se refaz por descrição | — |

**RP = 4 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Instalação declarada, porém com runtime e posição de rede: exige Node com `pnpm` e colocar um **proxy no caminho de toda requisição** | — |
| E09 Custo | 4 | Custo marginal: MIT, sem serviço pago; o custo é renderização local — e a proposta do item é justamente reduzir a fatura | — |
| E10 Contexto/tokens | 1 | Medido: **501 arquivos, 31,1 MB** — contagem na faixa 300–1.000 (que sozinha daria 2) e tamanho na faixa 20–100 MB, que é a pior das duas. Parte do volume é `.git/` e `eval/` | — |
| E11 Fornecedor | 2 | **Dependência declarada de um fornecedor, com abstração parcial**: o mecanismo depende do canal de visão do modelo e de perfis de renderização calibrados **por modelo**, com nomes de modelo específicos no changelog. Trocar de fornecedor exige recalibrar | — |
| E12 Reversibilidade | 4 | Reversível por remoção, sem efeito residual: retirado o proxy, o tráfego volta a ser texto. O registro local de eventos permanece como arquivo | — |

**AA = 3 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (mecanismo, as duas densidades, os três números de exemplo, a faixa de economia, o arquivo de eventos como contrafactual) e **todos** conferem com o README lido. O catálogo reproduz também a autoqualificação do autor em vez de apresentar o número como resultado — é uma das descrições mais fiéis do acervo.
**O que o catálogo afirma:** "o custo em token de uma imagem é fixado pelas dimensões em pixel, não pelo tanto de texto dentro dela… **~3,1 caracteres por token de imagem contra ~1 caractere por token de texto**… ≈25 mil tokens como texto, ≈2,7 mil tokens como imagem… **~59–70% de fatura menor**… **O que extrair:** o método de medição é tão valioso quanto a técnica."
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "at current Fable list prices that lands as a **~59–70% lower end-to-end bill**" | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — depende de preço de tabela, que é externo e volátil |
| "prices move and workloads differ, so the durable number is the token cut itself, measured per-request against a free `count_tokens` counterfactual" | `README.md` da fonte | **ALEGAÇÃO DO AUTOR — qualificação da própria alegação anterior** | não conferida, mas registrada como método declarado |
| "converter texto em imagem pode reduzir fidelidade, acessibilidade, capacidade de busca, auditabilidade e proteção contra injeção" | `94` (trilha Codex) | **ALEGAÇÃO DE TERCEIRO sobre risco** | não confirmada por inspeção — **é o que sustenta `E06 = 1` e dispara V2** |
| `clone: from https://github.com/teamchong/pxpipe` | `.git/logs/HEAD` na fonte | **FATO OBSERVADO** | sim — confirma a origem declarada no README |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 | não | `E06 = 1`, **não 0**: o risco é **declarado**, não confirmado por inspeção. Rejeitar aqui violaria "rejeitado por evidência, nunca por suspeita" |
| **V2** | **sim** | `E06 = 1` → teto: no máximo PADRÃO A ESTUDAR, REFERÊNCIA ou EXIGE PESQUISA. **Nunca** candidato |
| V3 · V4 · V5 · V6 · V7 · V8 | não | `E07 = 4` · `LV = 4` · **0 ND** · `E15 = 2` (≠ 0) · reconferência confere |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** **V2**, que fecha as duas classes de candidato apesar de `NF = 4`, `RP = 4` e Bloco A integralmente determinado. É o caso mais claro do acervo para a regra §8.2: **relevância alta não compensa risco declarado**.
**Se EXIGE PESQUISA — lacuna nomeada:** **uma, precisa:** o item não demonstra **preservação semântica nem preservação da defesa contra injeção** quando o contexto vira imagem — e a defesa contra injeção é a que importa para um proxy que reescreve toda requisição.  **Verificação que a fecharia:** abrir `eval/results`, `FINDINGS.md` e os testes `abstention`, `gist-recall` e `needle-haystack` — que **já existem dentro da fonte** — para medir perda de informação; e inspecionar `src/` para saber o que o proxy faz com conteúdo já suspeito. Nenhuma dessas verificações exige executar ou instalar coisa alguma.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-08-PRT-001 — `Tolkenizaiton.png`

**Tipo:** PRINT · **Área:** 08_CUSTO-E-CONTEXTO
**Hash F0:** `EA62DA1C5BDAFF8B`   **Hash reconferido:** `EA62DA1C5BDAFF8B`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`109`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-08-PRT-001 · `H-P1-003` (relatório `109`)

> **Registro literal:** o nome do arquivo está grafado `Tolkenizaiton.png` — com duas trocas em relação a *Tokenization*. **Grafia preservada, não normalizada**, conforme a prática já adotada no acervo.

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Descrição com detalhe reproduzível, sem artefato: o card mostra o percurso texto cru → tokens → IDs inteiros com **exemplo nomeado e numerado**, compara três granularidades e dá a faixa típica de vocabulário. `109` confirma percurso, granularidades, exemplo e faixa **como conteúdo exibido** | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e sua data |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando dado sensível ou instrução ao leitor |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos da série "LLM-Series" |
| E13 Testes/evals | ND | — | Nenhuma verificação exibida | 
| E15 Alegações ⚠ | 1 | Alegação numérica com fonte citada porém **não conferível dentro da imagem**: os IDs `4302 / 12871 / 8932 / 7421` e a faixa de 30 mil a 200 mil dependem de **qual** tokenizador — que o card não nomeia. `109` registra exatamente isso: "IDs, faixa e comportamento são dependentes do tokenizador e não foram verificados externamente" | — |

**NF = 1 · 2/7 · 5 ND** *(mediana dos determinados [1,2] = 1,5 → §14.3 vale o inferior)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: é a unidade em que o orçamento da área é contado. Sem artefato | — |
| E04 Transferibilidade | 3 | Transferível com adaptação declarada: o conceito viaja, mas a razão token/caractere muda por modelo — o próprio catálogo registra a ressalva | — |
| E14 Diferencial | 2 | Conveniência sobre conhecimento amplamente acessível: é material didático introdutório, disponível em qualquer documentação de fornecedor | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E08 · E09 · E10 · E11 · E12 | 3 · 5 · 4 · 5 · 4 | Valor fixo de mídia do índice §3.3 | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (o exemplo com as quatro subpalavras e seus IDs, as três granularidades comparadas, o espaço fazendo parte do token, a faixa de vocabulário) conferido contra os pixels; **CONFIRMADA** em `109`, com a ressalva de dependência do tokenizador registrada pelo próprio relatório.
**O que o catálogo afirma:** "Card didático da série LLM-Series… O exemplo: 'unbelievable transformers' vira `un` (4302), `believable` (12871), `transform` (8932), `ers` (7421)… Cada modelo tem tokenizador próprio, vocabulário tipicamente de 30 mil a 200 mil. **O que extrair:** é a base para dimensionar orçamento."
**Confere com a fonte:** sim — CONFIRMADA em `109`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| os quatro IDs inteiros do exemplo | print, via `109` | ALEGAÇÃO DO AUTOR | **não** — dependem de tokenizador não nomeado; `109` registra a não verificação |
| "vocabulário tipicamente de 30 mil a 200 mil" | print, via `109` | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "a razão token/caractere muda por modelo" | `_CONTEUDO.md` área 08 | ALEGAÇÃO DO CATÁLOGO — ressalva correta | coerente com `AC-08-REP-003`, que calibra perfil **por modelo** — convergência entre itens, não verificação |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4 do índice.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

> **Nota de aplicação aos oito VÍDEO desta área.** LV3-V vem de `H-M2-001` (relatório `94`); LV3-A, quando existe, do manifesto `117`. **LV3-V + LV3-A não produz LV4**; transcrição automática **não autoriza citação exata**. **V5 não é aplicado automaticamente a vídeo.** Bloco C segue o valor fixo do índice §3.3. Três dos oito têm fala aproveitável (`002`, `003`, `008`, todos em `pt`, ALTA AUTOMÁTICA); cinco não têm.

### AC-08-VID-001 — `Caching layers.mp4`

**Tipo:** VÍDEO · **Área:** 08_CUSTO-E-CONTEXTO
**Hash F0:** `95C7C2C3E9D2DD3D`   **Hash reconferido:** `95C7C2C3E9D2DD3D`   **Confere:** sim
**LV:** **LV3-V** (sem LV3-A aproveitável)
**Cobertura da leitura:** análise visual por quadros-chave (`94`, `H-M2-001`); áudio processado — 15,0 s, `en`, 1 palavra, confiança 0,130, **SEM FALA LEXICAL CONFIÁVEL** (`117`). É a **menor confiança de STT do acervo**.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-08-VID-001 · `H-M2-001` (relatório `94`) · manifesto `117`

#### Bloco A — Fonte
| Eixo | Nota | Evidência | Se ND: o que resolveria |
|---|---|---|---|
| E02 | 1 | **Só infográfico**: o percurso Browser → CDN → Redis → Database com uma instrução de leitura. Nenhuma implementação, nenhuma medição | — |
| E03 · E05 · E06 · E07 · E13 | ND | — | Origem e data; canal com data; inspeção direta da imagem; autoria e termos; nenhuma verificação exibida |
| E15 ⚠ | 1 | Alegação numérica com fonte citada porém não conferida: em cenário de 1.000 leituras, apenas três chegariam ao banco. `94` registra literalmente que "o número '3 de 1.000' não foi demonstrado nem reproduzido" | — |

**NF = 1 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E01 | 2 | Endereça a pergunta de forma **genérica**: trata de cache de infraestrutura (CDN, Redis, banco), não de orçamento de token nem de janela de contexto — que é a pergunta desta área | — |
| E04 | 1 | Só a ideia viaja: não há política de invalidação, consistência nem métrica | — |
| E14 | 1 | Conveniência sobre conhecimento amplamente acessível: hierarquia de cache é conteúdo de manual | — |

**RP = 1 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E08 · E09 · E10 · E11 · E12 | 3 · 5 · 4 · 5 · 4 | Valor fixo de mídia do índice §3.3 | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 1** — **assunto pelo título**: a tabela do catálogo registra apenas "camadas de cache" e o tamanho do arquivo, sem qualquer detalhe do conteúdo. Confere com o que `94` mostra, mas não afirma quase nada.
**O que o catálogo afirma:** "| `Caching layers.mp4` | 14 MB | camadas de cache |"
**Confere com a fonte:** sim, no pouco que afirma

#### Alegações registradas
| Alegação | Origem | Camada | Verificada? |
|---|---|---|---|
| "check the closest copy first, hit the DB last" | texto na tela, via `94` | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| em 1.000 leituras de API, três chegariam ao banco | quadro do vídeo, via `94` | ALEGAÇÃO DO AUTOR — cenário ilustrativo | **não** — `94` declara não demonstrado nem reproduzido |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · 5 ND < 8 · `E15 = 1` · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |
| V5 | **não aplicado** | `LV = 3` · aplicação automática a vídeo proibida pelo estado corrente |

#### Resultado
**RF = REFERÊNCIA** — §9, insumo de consulta com `LV ≥ 3`; critério §3.4 do índice. `RP = 1` fecha qualquer classe de candidato.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-08-VID-002 — `Gravando 2026-07-28 153711.mp4`

**Tipo:** VÍDEO · **Área:** 08_CUSTO-E-CONTEXTO
**Hash F0:** `4779F1249C5D9516`   **Hash reconferido:** `4779F1249C5D9516`   **Confere:** sim
**LV:** **LV3-V + LV3-A** — a soma **não** produz LV4
**Cobertura da leitura:** quadros-chave (`94`, `H-M2-001`) mais transcrição automática bruta (`117`): 50,5 s, `pt`, 170 palavras, 16 segmentos, confiança 0,874, **ALTA AUTOMÁTICA**. Transcrição não revisada — **proibido tratar como citação exata**.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-08-VID-002 · `H-M2-001` (`94`) · `H-M3-001` · `117`

#### Bloco A — Fonte
| Eixo | Nota | Evidência | Se ND: o que resolveria |
|---|---|---|---|
| E02 | 2 | Acima da simples demonstração: há **diagrama explícito** em que capacidades, prompt, arquivos de contexto e instruções aparecem replicados por ramo de subagente, com janela aproximada indicada. Sem artefato e sem medição | — |
| E03 · E05 · E06 · E07 · E13 | ND | — | Origem e data; canal com data; nenhuma superfície inspecionável; autoria e termos; nenhuma medição de custo por delegação |
| E15 ⚠ | 1 | Alegações com fonte citada porém não conferidas — e por STT automático, o que impede citação exata: fragmentos aproximados sobre subagentes serem "lentos" e "caros". Nenhum número de token ou de latência é exibido | — |

**NF = 1 · 2/7 · 5 ND** *(mediana [1,2] = 1,5 → §14.3)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E01 | 3 | Endereça diretamente a pergunta central: o custo de replicar contexto por subagente é exatamente "não estourar o orçamento" | — |
| E04 | 2 | Transferível com adaptação **não declarada**: a ideia de desenhar o contexto mínimo por agente é aplicável, mas o vídeo não entrega critério nem medição | — |
| E14 | 2 | Conveniência sobre conhecimento acessível: o tema reaparece em `AC-08-VID-004` (nível *Delegate*) e nos itens da área 03 | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E08 · E09 · E10 · E11 · E12 | 3 · 5 · 4 · 5 · 4 | Valor fixo de mídia do índice §3.3 | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — o catálogo declara **título pelo conteúdo visível** ("limites de contexto e divisão do trabalho entre agentes") e a análise de quadros **confirma**: `94` descreve o diagrama de replicação entre subagentes. Escala máxima da convenção §3.5.
**O que o catálogo afirma:** "| `Gravando 2026-07-28 153711.mp4` | 44,5 MB | limites de contexto e divisão do trabalho entre agentes | não transcrito |"
**Confere com a fonte:** sim — e o marcador "não transcrito" está **superado**: o item tem LV3-A desde `117`

#### Alegações registradas
| Alegação (conteúdo aproximado — **STT automático**) | Origem | Camada | Verificada? |
|---|---|---|---|
| que subagentes seriam "lentos" e "caros" por replicação de contexto | LV3-A (`117`) e texto na tela (`94`) | ALEGAÇÃO DO AUTOR | **não** — nenhuma medição; e a transcrição é automática |
| janela aproximada de 200k exibida no diagrama | quadro, via `94` | FATO OBSERVADO (número exibido) | o número está na tela; sua correção não foi verificada |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · 5 ND · `E15 = 1` · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |
| V5 | **não aplicado** | `LV = 3` |

#### Resultado
**RF = REFERÊNCIA** — §9, insumo de consulta com `LV ≥ 3`; critério §3.4 do índice.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-08-VID-003 — `Gravando 2026-07-28 155545.mp4`

**Tipo:** VÍDEO · **Área:** 08_CUSTO-E-CONTEXTO
**Hash F0:** `6AEFF65BE08979CA`   **Hash reconferido:** `6AEFF65BE08979CA`   **Confere:** sim
**LV:** **LV3-V + LV3-A** — a soma **não** produz LV4
**Cobertura da leitura:** quadros-chave (`94`) mais transcrição automática bruta (`117`): 53,6 s, `pt`, 204 palavras, 16 segmentos, confiança 0,896 — **a maior confiança de STT desta área** —, **ALTA AUTOMÁTICA**. Não revisada; **proibido citar como literal**.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-08-VID-003 · `H-M2-001` (`94`) · `H-M3-001` · `117`

#### Bloco A — Fonte
| Eixo | Nota | Evidência | Se ND: o que resolveria |
|---|---|---|---|
| E02 | 2 | Demonstração **na ferramenta**, com passos visíveis: modo de planejamento acionado, troca de modelo, validação pelo humano. É procedimento observável, não só afirmação — mas sem artefato e sem medição | — |
| E03 · E05 · E06 · E07 · E13 | ND | — | Origem e data; canal com data; nenhuma superfície inspecionável; autoria e termos; nenhuma medição de economia |
| E15 ⚠ | 1 | Alegações com fonte citada porém não conferidas: economia por trocar de modelo e por evitar "ficar pensando e gastando tokens". `94` registra que "nomes, versões, qualidade e economia não foram verificados" | — |

**NF = 1 · 2/7 · 5 ND** *(mediana [1,2] = 1,5 → §14.3)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E01 | 3 | Endereça diretamente a pergunta central: rotear etapa cara e etapa barata é controle direto de orçamento | — |
| E04 | 2 | Transferível com adaptação não declarada: o procedimento depende de nomes e planos de modelo, que o próprio material trata como voláteis | — |
| E14 | 2 | Conveniência: a mesma tática aparece em `AC-08-VID-004` (nível *Route*) e em `AC-08-VID-007` | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E08 · E09 · E10 · E11 · E12 | 3 · 5 · 4 · 5 · 4 | Valor fixo de mídia do índice §3.3 | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — **título pelo conteúdo visível** ("estratégia de consumo no Claude Code e troca para modelo mais barato") **confirmado** pela análise de quadros em `94`.
**O que o catálogo afirma:** "| `Gravando 2026-07-28 155545.mp4` | 51,3 MB | estratégia de consumo no Claude Code e troca para modelo mais barato | não transcrito |"
**Confere com a fonte:** sim — marcador "não transcrito" **superado** por `117`

#### Alegações registradas
| Alegação (conteúdo aproximado — **STT automático**) | Origem | Camada | Verificada? |
|---|---|---|---|
| que planejar com modelo caro e executar com barato economizaria tokens | LV3-A (`117`) e texto na tela (`94`) | ALEGAÇÃO DO AUTOR | **não** — sem número, sem contrafactual |
| nomes de modelo citados na fala | LV3-A (`117`) | ALEGAÇÃO DO AUTOR | **não conferível** — STT troca nomes; `94` registra o mesmo limite |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · 5 ND · `E15 = 1` · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |
| V5 | **não aplicado** | `LV = 3` |

#### Resultado
**RF = REFERÊNCIA** — §9, insumo de consulta com `LV ≥ 3`; critério §3.4 do índice.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-08-VID-004 — `Gravando 2026-07-28 163216.mp4`

**Tipo:** VÍDEO · **Área:** 08_CUSTO-E-CONTEXTO
**Hash F0:** `66B279D261DBF011`   **Hash reconferido:** `66B279D261DBF011`   **Confere:** sim
**LV:** **LV3-V** (sem LV3-A aproveitável)
**Cobertura da leitura:** análise visual por quadros-chave (`94`, `H-M2-001`), que enumera os níveis um a um; áudio processado — 16,5 s, `en`, 1 palavra, confiança 0,130, **SEM FALA LEXICAL CONFIÁVEL** (`117`). Todo o conteúdo é texto em tela.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-08-VID-004 · `H-M2-001` (relatório `94`) · manifesto `117`
**Relação:** **original** de `AC-08-VID-005`, que é duplicata binária exata.

#### Bloco A — Fonte
| Eixo | Nota | Evidência | Se ND: o que resolveria |
|---|---|---|---|
| E02 | 2 | Descrição com detalhe reproduzível, sem artefato: **sete níveis nomeados e ordenados**, cada um com ação concreta — auditar a conversa e apontar os três maiores desperdícios; impor formato e limite de resposta; classificar e rotear tarefa simples; criar handoff antes de saturar; podar instruções e desligar conectores ociosos; delegar leitura a subagente; agrupar em lote. É taxonomia, não demonstração | — |
| E03 · E05 · E06 · E07 · E13 | ND | — | Origem e data; canal com data; inspeção direta procurando dado sensível; autoria e termos; **nenhum dos números exibidos é acompanhado de método** |
| E15 ⚠ | 1 | **O item mais denso em alegação numérica não conferida da área**: 75–85% de redução em roteamento; 40–50% da janela como momento de compactar; 6.100 tokens de entrada para 420 de saída em delegação; lote a −50%; cache a −90%. Nenhum é acompanhado de fonte, método ou contrafactual. `94` já registra que servem "nunca como meta oficial sem benchmark local" | — |

**NF = 1 · 2/7 · 5 ND** *(mediana [1,2] = 1,5 → §14.3)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E01 | 3 | Endereça diretamente a pergunta central: é literalmente uma lista de controles de custo de token | — |
| E04 | 3 | Transferível com adaptação declarada: os sete níveis são categorias de controle aplicáveis a qualquer harness, ainda que os números não viajem | — |
| E14 | 3 | Resolve problema declarado sem equivalente pronto **dentro do acervo**: é o único item que organiza os controles de custo em **taxonomia ordenada** — os repositórios da área implementam controles isolados, não o mapa | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E08 · E09 · E10 · E11 · E12 | 3 · 5 · 4 · 5 · 4 | Valor fixo de mídia do índice §3.3 | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 0 — DIVERGENTE.** O catálogo afirma **"seis níveis"**, duas vezes, na tabela e no parágrafo seguinte. A análise de quadros da trilha Codex (`94`) enumera **sete**, nomeados: *Meter*, *Budget*, *Route*, *Compact*, *Prune*, *Delegate*, *Batch* — e o próprio título da seção de `94` é "sete níveis de redução de custo". O catálogo também resume o conteúdo como "medir, compactar e delegar", **omitindo orçamento, roteamento, poda e lote**. Divergência de contagem entre o catálogo e a inspeção do original → `NC = 0` pela convenção §3.5.
**O que o catálogo afirma:** "| `Gravando 2026-07-28 163216.mp4` | 10,1 MB | **seis níveis** para reduzir desperdício de tokens: medir, compactar e delegar | não transcrito |"
**Confere com a fonte:** **não** — ver a divergência acima

> **A divergência é de catálogo, não de fonte.** `V8` compara **hash**, e o hash confere. Por isso a divergência **não** produz `INDETERMINADO`: ela rebaixa `NC` a 0 e fica registrada. `NC` nunca entra em `NF` (`04` §12).

#### Alegações registradas
| Alegação (literal, tal como exibida) | Origem | Camada | Verificada? |
|---|---|---|---|
| "75–85%" de redução por roteamento | quadro, via `94` | ALEGAÇÃO DO AUTOR | **não** — sem método |
| "6.100 tokens de entrada para 420 de saída" em delegação | quadro, via `94` | ALEGAÇÃO DO AUTOR | **não** — sem contrafactual |
| lote a "−50%" e cache a "−90%" | quadro, via `94` | ALEGAÇÃO DO AUTOR — números de fornecedor | **não** — preços e descontos são externos e voláteis |
| "seis níveis" | `_CONTEUDO.md` área 08 | **ALEGAÇÃO DO CATÁLOGO — DIVERGENTE** | **contradita** pela inspeção do original, que mostra sete |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · 5 ND · `E15 = 1` (≠ 0) · **hash confere** |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |
| V5 | **não aplicado** | `LV = 3` |

#### Resultado
**RF = REFERÊNCIA** — §9, insumo de consulta com `LV ≥ 3`; critério §3.4 do índice. `V2` e `V4` já fechariam as classes de candidato.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-08-VID-005 — `Gravando 2026-07-28 163244.mp4`  ·  FICHA DE PONTE

**Tipo:** VÍDEO · **Área:** 08_CUSTO-E-CONTEXTO
**Hash F0:** `66B279D261DBF011`   **Hash reconferido:** `66B279D261DBF011`   **Confere:** sim
**Original:** **`AC-08-VID-004`** — `Gravando 2026-07-28 163216.mp4`, mesmo SHA-256 (`66B279D261DBF011`), mesmo tamanho (10,1 MB), mesma duração (16,5 s)
**LV:** LV3-V *(herdado de `AC-08-VID-004`)*
**Cobertura da leitura:** reconferência de hash desta cópia — idêntico ao do original e ao do manifesto — e da correspondência de duração em `117`. **O conteúdo não foi reavaliado** — `05` §10: duplicata exata herda a ficha do original e mantém rastreabilidade própria.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-08-VID-005 · `H-M2-001` (`94`, que registra "AC-08-VID-005 é duplicata binária exata de AC-08-VID-004") · `117`

> **Segundo e último duplicado exato do acervo.** O primeiro é `AC-03-VID-008`. Com esta ficha, os dois pares previstos no critério de conclusão da Fase 2 estão ligados aos seus originais.

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 · E03 · E05 · E06 · E07 · E13 · E15 | **herdados** | Todos os sete eixos herdam integralmente `AC-08-VID-004`, por identidade binária comprovada por SHA-256. Reavaliar o mesmo byte duas vezes produziria duplicação de evidência, não evidência independente | — |

**NF = herdado de `AC-08-VID-004` (1 · 2/7 · 5 ND)**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 · E04 · E14 | **herdados** | Idem — identidade binária | — |

**RP = herdado de `AC-08-VID-004` (3 · 3/3 · 0 ND)**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 · E09 · E10 · E11 · E12 | **herdados** | Idem — identidade binária | — |

**AA = herdado de `AC-08-VID-004` (4 · 5/5 · 0 ND)**

#### Catálogo (separado da fonte)
**NC = 0** — **herdado, e por dois motivos somados.** (1) A mesma divergência do original: o catálogo diz "seis níveis" onde a inspeção mostra sete. (2) Quanto à duplicação em si, o catálogo **acerta**: declara "duplicata; não transcrito", registra que "`163216` e `163244` têm hash idêntico e foram preservados", e a reconferência independente desta fase confirma. **A nota permanece 0 porque a descrição de conteúdo é a mesma do original e diverge** — o acerto sobre a duplicação está registrado aqui, não compensado na nota.
**O que o catálogo afirma:** "| `Gravando 2026-07-28 163244.mp4` | 10,1 MB | seis níveis para reduzir desperdício de tokens — duplicata exata | duplicata; não transcrito |"
**Confere com a fonte:** quanto à **duplicação**, sim, e confirmado por hash; quanto ao **conteúdo**, não

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "`163216` e `163244` têm hash idêntico e foram preservados" | `_CONTEUDO.md` área 08 | ALEGAÇÃO DO CATÁLOGO | **sim** — confirmada por reconferência SHA-256 independente nesta fase |
| "seis níveis" | `_CONTEUDO.md` área 08 | ALEGAÇÃO DO CATÁLOGO — **DIVERGENTE** | **contradita** pela inspeção do original |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V8 | não | hash reconferido idêntico ao do manifesto **e** ao do original |
| V5 | **não se aplica** | `04` §8 — V5 tem exceção literal para item `DUPLICADO` por hash idêntico |
| V1 · V2 · V3 · V4 · V6 · V7 | herdados | as portas do original valem para a cópia (`V2` e `V4` disparam lá) |

#### Resultado
**RF = DUPLICADO**
**Regra que produziu:** §9, condição de entrada de DUPLICADO — hash idêntico a outro item do acervo, comprovado por reconferência SHA-256 nesta fase.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> `DUPLICADO` **não significa descartável.** O item mantém ID próprio, rastreabilidade e esta ficha de ponte; a avaliação de conteúdo vive em `AC-08-VID-004`.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-08-VID-006 — `Gravando 2026-07-28 214120.mp4`

**Tipo:** VÍDEO · **Área:** 08_CUSTO-E-CONTEXTO
**Hash F0:** `4E9239D2BB085477`   **Hash reconferido:** `4E9239D2BB085477`   **Confere:** sim
**LV:** **LV3-V** (sem LV3-A aproveitável)
**Cobertura da leitura:** quadros-chave (`94`, `H-M2-001`); áudio — 9,2 s, `en`, 1 palavra, confiança 0,751, **SEM FALA LEXICAL CONFIÁVEL** (`117`). **É o vídeo mais curto da área.**
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-08-VID-006 · `H-M2-001` (`94`) · `117`
**Relação:** trata do mesmo objeto de `AC-08-REP-003` (`pxpipe`), que está no acervo **como repositório completo**.

#### Bloco A — Fonte
| Eixo | Nota | Evidência | Se ND: o que resolveria |
|---|---|---|---|
| E02 | 1 | **Só carrossel**: apresenta a proposta do proxy sem demonstração, sem medição e sem código — enquanto o repositório correspondente, já avaliado nesta área, traz testes, evals e changelog. É a descrição de um artefato que o acervo possui inteiro | — |
| E03 · E05 · E07 · E13 | ND | — | Origem e data; canal com data; autoria e termos; nenhuma verificação exibida |
| E06 ⚠ | **1** | **Risco ativo declarado por terceiro e não confirmado por inspeção** — mesma âncora aplicada em `AC-08-REP-003`, pela mesma evidência: `94` registra que converter texto em imagem pode reduzir fidelidade, auditabilidade e **proteção contra injeção**, e que "o artefato não demonstra preservação semântica nem segurança". A coerência entre as duas fichas é deliberada: **mesmo risco, mesma nota** | — |
| E15 ⚠ | 1 | Alegações numéricas fortes com fonte citada porém não conferidas: ~3,1 caracteres por token de imagem e economia de 59–70%. No vídeo elas aparecem **sem** a qualificação que o autor faz no README do repositório — o carrossel apresenta como resultado o que a fonte primária apresenta como estimativa a medir | — |

**NF = 1 · 3/7 · 4 ND** *(mediana dos determinados [1,1,1] = 1)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E01 | 3 | Endereça diretamente a pergunta central: é redução de token de entrada | — |
| E04 | 1 | **Só a ideia viaja** — e nem precisa: o artefato real está no acervo como `AC-08-REP-003` | — |
| E14 | 1 | **Conveniência sobre inventário já acessível**: sobrepõe integralmente `AC-08-REP-003`, com evidência estritamente inferior | — |

**RP = 1 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E08 · E09 · E10 · E11 · E12 | 3 · 5 · 4 · 5 · 4 | Valor fixo de mídia do índice §3.3 | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — **título pelo conteúdo visível** ("pxpipe: comprimir contexto como imagem para cortar tokens") **confirmado** pela análise de quadros em `94`. O catálogo ainda registra por conta própria que "as economias declaradas precisam de benchmark próprio".
**O que o catálogo afirma:** "| `Gravando 2026-07-28 214120.mp4` | 4,1 MB | pxpipe: comprimir contexto como imagem para cortar tokens | não transcrito |… Os quadros do primeiro repetem a hipótese do `pxpipe/`… As economias declaradas precisam de benchmark próprio."
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal, tal como exibida) | Origem | Camada | Verificada? |
|---|---|---|---|
| "~3,1 caracteres por token de imagem" e economia de "59–70%" | quadros, via `94` | ALEGAÇÃO DO AUTOR — reprodução da alegação de `AC-08-REP-003` | **não** — e aqui **sem** a autoqualificação presente na fonte primária |
| risco de perda de fidelidade, auditabilidade e proteção contra injeção | `94` | ALEGAÇÃO DE TERCEIRO sobre risco | não confirmada por inspeção — sustenta `E06 = 1` |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 | não | `E06 = 1`, **não 0** — risco declarado, não confirmado |
| **V2** | **sim** | `E06 = 1` → teto: nunca candidato |
| **V4** | **sim** | `E07 = ND` |
| V3 · V6 · V7 · V8 | não | `E07 ≠ 0` · 4 ND · `E15 = 1` (≠ 0) · hash confere |
| V5 | **não aplicado** | `LV = 3` |

#### Resultado
**RF = REFERÊNCIA** — §9, insumo de consulta com `LV ≥ 3`; critério §3.4 do índice. `V2` e `V4` fecham as classes de candidato, e `RP = 1` as fecharia de novo.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-08-VID-007 — `Gravando 2026-07-29 090249.mp4`

**Tipo:** VÍDEO · **Área:** 08_CUSTO-E-CONTEXTO
**Hash F0:** `CB50B41864BC2725`   **Hash reconferido:** `CB50B41864BC2725`   **Confere:** sim
**LV:** **LV3-V** (sem LV3-A aproveitável)
**Cobertura da leitura:** quadros-chave (`94`, `H-M2-001`); áudio — 12,3 s, `en`, 1 palavra, confiança 0,751, **SEM FALA LEXICAL CONFIÁVEL** (`117`). **É o item mais recente do acervo** — gravado em 29/07/2026, a data desta avaliação.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-08-VID-007 · `H-M2-001` (`94`) · `117`

#### Bloco A — Fonte
| Eixo | Nota | Evidência | Se ND: o que resolveria |
|---|---|---|---|
| E02 | 1 | **Só carrossel com listagem**: cinco táticas nomeadas, sem demonstração e sem medição | — |
| E03 · E05 · E06 · E07 · E13 | ND | — | Origem e data da publicação; canal com data; inspeção direta da imagem; autoria e termos; nenhuma verificação exibida |
| E15 ⚠ | 1 | Alegações fortes com fonte citada porém não conferidas, **e voláteis por natureza**: economia "de até 80%", "22% mais barato sem perda de qualidade", "109 subagentes" e comparações de preço entre versões de modelo. `94` registra que "versões, preços, disponibilidade, nomenclatura e benchmarks são voláteis e não foram verificados". A expressão "sem perda de qualidade" é a alegação mais forte e a menos sustentada | — |

**NF = 1 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E01 | 3 | Endereça diretamente a pergunta central: as cinco táticas são controles de consumo | — |
| E04 | 2 | Transferível com adaptação **não declarada**: as táticas dependem de nomes, planos e preços de fornecedor que o próprio material trata como instáveis | — |
| E14 | 1 | **Conveniência sobre inventário já acessível**: reduzir esforço, separar arquiteto de executor e reduzir verbosidade já estão em `AC-08-VID-003`, `AC-08-VID-004` e — como artefato — em `AC-08-REP-001` | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E08 · E09 · E10 · E11 · E12 | 3 · 5 · 4 · 5 · 4 | Valor fixo de mídia do índice §3.3 | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — **título pelo conteúdo visível** ("Fable 5: esforço, economia de tokens e modelo advisor") **confirmado** pela análise de quadros em `94`, inclusive quanto ao papel de consultor reservado ao modelo mais caro. O catálogo acrescenta a ressalva de benchmark próprio.
**O que o catálogo afirma:** "| `Gravando 2026-07-29 090249.mp4` | 3,1 MB | Fable 5: esforço, economia de tokens e modelo advisor | não transcrito |… O segundo sugere baixar nível de esforço, usar skills como Ponytail/Caveman para reduzir verbosidade e reservar um modelo mais caro como 'advisor'."
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal, tal como exibida) | Origem | Camada | Verificada? |
|---|---|---|---|
| "22% mais barato **sem perda de qualidade**" | quadro, via `94` | ALEGAÇÃO DO AUTOR | **não** — nenhuma medição de qualidade acompanha |
| "109 subagentes" | quadro, via `94` | ALEGAÇÃO DO AUTOR | **não** — `NÃO VERIFICADA` |
| menção a "Caveman" como tática de verbosidade | quadros, via `94`, e `_CONTEUDO.md` | ALEGAÇÃO DO AUTOR / DO CATÁLOGO | o **artefato** existe e está no acervo como `AC-08-REP-001`; a **economia atribuída** não foi verificada |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · 5 ND · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |
| V5 | **não aplicado** | `LV = 3` |

#### Resultado
**RF = REFERÊNCIA** — §9, insumo de consulta com `LV ≥ 3`; critério §3.4 do índice.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-08-VID-008 — `handoff.mp4`

**Tipo:** VÍDEO · **Área:** 08_CUSTO-E-CONTEXTO
**Hash F0:** `2789E1E271CDE926`   **Hash reconferido:** `2789E1E271CDE926`   **Confere:** sim
**LV:** **LV3-V + LV3-A** — a soma **não** produz LV4
**Cobertura da leitura:** quadros-chave (`94`, `H-M2-001`) mais transcrição automática bruta (`117`): 43,8 s, `pt`, 174 palavras, 14 segmentos, confiança 0,868, **ALTA AUTOMÁTICA**. Não revisada; **proibido citar como literal**.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-08-VID-008 · `H-M2-001` (`94`) · `H-M3-001` · `117`

#### Bloco A — Fonte
| Eixo | Nota | Evidência | Se ND: o que resolveria |
|---|---|---|---|
| E02 | 2 | Descrição com detalhe reproduzível, sem artefato: exibe um **gráfico de qualidade contra preenchimento da janela** com dois limiares marcados, e em seguida o procedimento completo — escrever um arquivo de passagem, limpar a sessão e retomar. Os **cinco campos do arquivo são nomeados**: objetivo, estado atual, o que mudou, tentativas que falharam e próximos passos. É a evidência mais estruturada entre os oito vídeos | — |
| E03 · E05 · E06 · E07 · E13 | ND | — | Origem e data; canal com data; nenhuma superfície inspecionável; autoria e termos; **o gráfico de qualidade não vem com método de medição** |
| E15 ⚠ | 1 | Alegação forte com fonte citada porém não conferida: a curva de queda de qualidade e os limiares de 65% e 80% aparecem como **fato desenhado**, sem eixo medido, sem amostra e sem método. A afirmação de que a passagem explícita supera a compactação automática é comparativa e não medida | — |

**NF = 1 · 2/7 · 5 ND** *(mediana [1,2] = 1,5 → §14.3)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E01 | 3 | Endereça diretamente a pergunta central: a janela de contexto é metade da pergunta desta área | — |
| E04 | 3 | Transferível com adaptação declarada: **os cinco campos do arquivo de passagem transferem literalmente**, sem depender de ferramenta, plano ou fornecedor | — |
| E14 | 3 | Resolve problema declarado sem equivalente pronto no acervo **como protocolo**: o catálogo registra que o item da área 03 (`ralph-main`) ataca o mesmo problema **por outro caminho** — contexto limpo a cada iteração, memória em arquivos —, o que faz deste um segundo desenho, não uma repetição | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E08 · E09 · E10 · E11 · E12 | 3 · 5 · 4 · 5 · 4 | Valor fixo de mídia do índice §3.3 | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 1** — **assunto pelo título**: a tabela registra apenas "passagem de contexto entre sessões" e o tamanho. A nota de cruzamento com `ralph-main` é observação do catálogo, não descrição do conteúdo — e o catálogo **não menciona** o gráfico, os limiares nem os cinco campos, que são o que o item tem de concreto.
**O que o catálogo afirma:** "| `handoff.mp4` | 43 MB | passagem de contexto entre sessões |… **Nota:** `handoff.mp4` trata do problema que o `03_ORQUESTRACAO-DE-AGENTES/ralph-main` resolve por outro caminho… Vale cruzar as duas abordagens quando o vídeo for assistido."
**Confere com a fonte:** sim, no pouco que afirma — e o marcador implícito de "não assistido" está **superado** por `94` e `117`

#### Alegações registradas
| Alegação (conteúdo aproximado — **STT automático** e texto em tela) | Origem | Camada | Verificada? |
|---|---|---|---|
| a qualidade da saída cai conforme a janela enche, com rotação em 65% e compactação automática em 80% | quadro, via `94` | ALEGAÇÃO DO AUTOR — **apresentada como gráfico** | **não** — sem eixo medido, sem amostra, sem método |
| que a passagem explícita seria superior à compactação automática | LV3-A (`117`) e quadros (`94`) | ALEGAÇÃO DO AUTOR — comparativa | **não** — `94` registra que seria preciso comparar empiricamente antes de normatizar |
| os cinco campos do arquivo de passagem | quadro, via `94` | **FATO OBSERVADO** (estrutura exibida) | sim, quanto ao que está na tela |
| "Vale cruzar as duas abordagens quando o vídeo for assistido." | `_CONTEUDO.md` área 08 | ALEGAÇÃO DO CATÁLOGO — instrução de escopo | **registrada, não obedecida como instrução** (`05` §7); o cruzamento com `ralph-main` é trabalho de Fase 4, fora desta frente |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · 5 ND · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |
| V5 | **não aplicado** | `LV = 3` |

#### Resultado
**RF = REFERÊNCIA** — §9, insumo de consulta com `LV ≥ 3`; critério §3.4 do índice.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

## Fechamento da área 08 — contagem factual

**Itens com ficha:** 12 de 12 · **IDs faltando:** 0 · **IDs repetidos:** 0

| RF | Quantidade | IDs |
|---|---|---|
| CANDIDATO FORTE | 0 | — |
| **CANDIDATO A PILOTO** | **2** | `AC-08-REP-001`, `AC-08-REP-002` |
| PADRÃO A ESTUDAR | 0 | — |
| **EXIGE PESQUISA** | **1** | `AC-08-REP-003` |
| **REFERÊNCIA** | **8** | `AC-08-PRT-001`, `AC-08-VID-001` a `004`, `006`, `007`, `008` |
| **DUPLICADO** | **1** | `AC-08-VID-005` → herda `AC-08-VID-004` |
| REJEITADO · INDETERMINADO | 0 | — |

| LV | Itens |
|---|---|
| LV4 | 3 (os três REPO) |
| LV3-V | 6 (1 PRINT + `VID-001`, `004`, `005`, `006`, `007`) |
| LV3-V + LV3-A | 3 (`VID-002`, `VID-003`, `VID-008`) |

**ND:** **46** de 180 células de eixo (12 itens × 15 eixos) = **25,6 %** — contados item a item: 1 + 1 + **0** nos três REPO (2), 5 no PRINT, 5 em cada um de `VID-001`, `002`, `003`, `004`, `005` (herdados), `007` e `008` (35), e **4** em `VID-006`. Nenhum item chegou ao gatilho de V6. Todos os 46 nomeiam o que os resolveria.

**Portas de veto na área:** V1 — 0 · **V2 — 2** (`AC-08-REP-003` e `AC-08-VID-006`, ambos por `E06 = 1`, mesmo risco declarado, mesma nota) · V3 — 0 · V4 — 9 · V5 — 0 (não aplicado a vídeo; e `AC-08-VID-005` tem exceção literal por ser DUPLICADO) · V6 — 0 · V7 — 0 · **V8 — 0 divergências**: os 12 reconferem, incluindo a identidade binária do par 004/005.

**Catálogo:** 4 CONFIRMADA em escala máxima (`NC = 5`: `VID-002`, `003`, `006`, `007`) · 4 com `NC = 3` (os três REPO e o PRINT) · 2 com `NC = 1` (`VID-001`, `VID-008` — assunto pelo título) · **2 DIVERGENTE (`NC = 0`): `AC-08-VID-004` e `AC-08-VID-005`**, pela contagem "seis níveis" contra os sete enumerados na inspeção.

**Registros novos desta área:**
1. **Primeira divergência de catálogo desde a área 02** — e a primeira **de contagem**: "seis níveis" contra sete inspecionados, em `AC-08-VID-004` e sua duplicata. Divergência de catálogo **não** dispara V8, que compara hash; rebaixa `NC` a 0 e fica registrada.
2. **Segundo e último duplicado exato do acervo** ligado ao original — `AC-08-VID-005` → `AC-08-VID-004`. Com `AC-03-VID-008` → `AC-03-VID-007`, os dois pares previstos estão fechados.
3. **Primeiro item do acervo com Bloco A integralmente determinado** — `AC-08-REP-003`, 0 ND em 7 eixos, por trazer licença, changelog datado, testes, evals **e histórico de repositório** na própria fonte.
4. **Primeiro repositório do acervo com `.git/`** — `AC-08-REP-003` é um clone real, não cópia `-main`. Isso contradiz, **para este item apenas**, a regra de acervo do `04` §5 segundo a qual `E05 = ND` é o resultado esperado. Registrado como exceção observada, sem alterar a regra.
5. **Primeiro `E06 = 1` do acervo, em dois itens** — `AC-08-REP-003` e `AC-08-VID-006`, pelo mesmo risco declarado por terceiro. **Nenhum dos dois foi rejeitado**: V1 exige risco **confirmado por inspeção**, e a rubrica é explícita — rejeitar por evidência, nunca por suspeita.
6. **O caso mais nítido de §8.2 no acervo** — `AC-08-REP-003` tem `NF = 4`, `RP = 4`, Bloco A completo, e ainda assim termina em EXIGE PESQUISA. Relevância alta não compensa risco declarado.

> Esta seção é contagem de fichas, não classificação de valor. Não há ordenação, ranking ou recomendação.

