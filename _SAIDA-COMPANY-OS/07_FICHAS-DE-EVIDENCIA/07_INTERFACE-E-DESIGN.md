> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

# FICHAS DE EVIDÊNCIA — ÁREA 07 — INTERFACE E DESIGN

**Fase:** 2 — Extração · **Data:** 2026-07-29 · **Avaliador:** Claude Opus 5 (Fase 2)
**Itens:** 13 — 5 REPO · 5 PRINT · 3 VÍDEO · 0 PLANILHA
**Convenções de aplicação:** `00_INDICE-DA-FASE-2.md` §3

**Pergunta central da área (base de E01):** *como o humano vê e comanda o sistema.*

---

### AC-07-REP-001 — `excalidraw-master`

**Tipo:** REPO · **Área:** 07_INTERFACE-E-DESIGN
**Hash F0:** `dir · 1243 arq. · aninhado`   **Hash reconferido:** `1243 arq. · aninhamento 1`   **Confere:** sim
**LV:** LV4
**Cobertura da leitura:** raiz efetiva `excalidraw-master/excalidraw-master` (37 entradas); `LICENSE` — MIT, 1.067 bytes, "Copyright (c) 2020 Excalidraw", íntegro; `README.md` (7.774 bytes, lidos 6 KB: proposta, badges, links de documentação); `package.json`; `vitest.config.mts` e `setupTests.ts` presentes na raiz; **busca por `SECURITY.md` e `CHANGELOG` na raiz efetiva — ausentes**; sinais `Dockerfile`, `docker-compose.yml`, `.husky/`, `crowdin.yml`, `firebase-project/`. **Não lidos:** `packages/`, `excalidraw-app/`, `dev-docs/`.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** não se aplica

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 4 | Artefato completo e inspecionável (monorepo com aplicativo, pacotes publicáveis, exemplos, documentação de desenvolvimento) **mais** procedimento de verificação declarado na raiz: `vitest.config.mts`, `setupTests.ts` e ganchos de pré-commit em `.husky/` | — |
| E03 Maturidade | 3 | Versionado com release identificável: pacote publicado em npm com badge de download mensal e `packages/` como origem. **Não alcança 4**: nenhum `CHANGELOG` na raiz efetiva e nenhum tratamento de erro observado no material lido | — |
| E05 Manutenção | ND | — | Nenhuma evidência datada dentro da fonte. Resolveria consultar releases e commits na origem pública |
| E06 Segurança ⚠ | 3 | Superfície declarada (aplicativo web colaborativo, backend de sincronização em `firebase-project/`, três arquivos de ambiente versionados como modelo) **com controle parcial documentado**: o README declara o produto "**end-to-end encrypted**", e `Dockerfile`/`docker-compose.yml` permitem execução isolada. A criptografia é **declarada**, não verificada | — |
| E07 Licença ⚠ | 4 | Permissiva padrão presente e íntegra: MIT, 1.067 bytes, titular nomeado, com badge correspondente. Cópia local não prova titularidade → teto 4 | — |
| E13 Testes/evals | 3 | Suíte executável identificável com ponto de entrada declarado: `vitest.config.mts` na raiz mais `setupTests.ts`. Nenhum eval de comportamento de agente — e não faria sentido aqui | — |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas ("virtual hand-drawn style whiteboard, collaborative and end-to-end encrypted"); os números presentes são badges de download, que não sustentam a proposta. **P-3** | — |

**NF = 3 · 6/7 · 1 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça a pergunta de forma genérica: é editor de desenho, não interface de comando do sistema. O próprio catálogo delimita — "**não é ferramenta de agente** — é o editor de diagramas" | — |
| E04 Transferibilidade | 4 | Transferível por configuração, sem alteração de código: o pacote `@excalidraw/excalidraw` é embutível, e há `docker-compose.yml` para execução própria | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto **dentro do acervo**: é o único item que entrega superfície de desenho colaborativo embutível | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 4 | Instalação declarada por pacote npm ou `docker-compose`; configuração por variável de ambiente (três arquivos de exemplo na raiz) | — |
| E09 Custo | 5 | Sem custo recorrente: roda sobre recurso já existente, sem chamada de modelo — é editor, não agente | — |
| E10 Contexto/tokens | 1 | Medido: **1.243 arquivos, 52,5 MB** — contagem na faixa 1.000–5.000 e tamanho na faixa 20–100 MB | — |
| E11 Fornecedor | 5 | Sem dependência de fornecedor: MIT, auto-hospedável por contêiner, com formato de arquivo próprio e aberto | — |
| E12 Reversibilidade | 4 | Reversível por remoção, sem efeito residual: o dado do usuário fica em arquivo exportável | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (whiteboard open source, colaborativo, criptografado ponta a ponta, pacote embutível) e o detalhe **confere** com o README e o `package.json`. O catálogo acerta ainda ao delimitar o que o item **não** é.
**O que o catálogo afirma:** "Editor de desenho à mão livre, colaborativo e criptografado ponta a ponta. **Não é ferramenta de agente** — é o editor de diagramas… O pacote `@excalidraw/excalidraw` é embutível."
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "An open source virtual hand-drawn style whiteboard. Collaborative and **end-to-end encrypted**." | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — código não lido; sustenta `E06 = 3` como controle **declarado** |
| "provável uso pretendido é gerar/editar diagrama de arquitetura programaticamente" | `_CONTEUDO.md` área 07 | `INFERÊNCIA` do catálogo — marcada como tal pelo próprio catálogo ("provável") | não |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V2 · V3 · V4 · V5 · V6 · V7 · V8 | **nenhuma** | `E06 = 3` · `E07 = 4` · `LV = 4` · 1 ND · `E15 = 3` · reconferência confere |

#### Resultado
**RF = CANDIDATO A PILOTO**
**Regra que produziu:** §9. **Não** alcança CANDIDATO FORTE: exige `RP ≥ 4`, e `RP = 3` — o item é excelente no que faz, mas endereça a pergunta da área apenas de forma genérica. Satisfaz CANDIDATO A PILOTO: `LV ≥ 3` · `E06 = 3` · `E07 = 4` · `RP = 3 ≥ 3` · **1 ND** ≤ 4 · nenhum eixo do Bloco C em 0.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> **CANDIDATO A PILOTO não significa pilotar.** Restrições registradas: `E10 = 1` (1.243 arquivos) e `E05 = ND`.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-07-REP-002 — `frontend-design-main`

**Tipo:** REPO · **Área:** 07_INTERFACE-E-DESIGN
**Hash F0:** `dir · 3 arq.`   **Hash reconferido:** `3 arq. · aninhamento 0`   **Confere:** sim
**LV:** LV4
**Cobertura da leitura:** raiz efetiva `frontend-design-main` — **listagem completa: 3 entradas** (`.claude-plugin/`, `skills/`, `README.md`); **busca por `LICENSE`/`COPYING`/`LICENCE` — ausente**; `README.md` **integral** (977 bytes); `.claude-plugin/` (`plugin.json`). **Não lido:** o conteúdo de `skills/`. **É o menor repositório do acervo.**
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** não se aplica

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 3 | Artefato completo e inspecionável correspondente à afirmação — uma skill empacotada como plugin, com manifesto e três exemplos de invocação no README —, **sem** procedimento de verificação declarado | — |
| E03 Maturidade | 2 | Funciona no cenário demonstrado, mas **sem versionamento, sem release e sem tag** observáveis: a listagem completa da raiz tem três entradas e nenhuma delas é `VERSION` ou `CHANGELOG` | — |
| E05 Manutenção | ND | — | Nenhuma evidência datada dentro da fonte. Resolveria consultar a origem pública |
| E06 Segurança ⚠ | ND | — | Item documental (§14.1): exige **leitura integral**. O conteúdo de `skills/` não foi lido. Superfície declarada é baixa — a skill gera código de interface, não executa nem acessa rede |
| E07 Licença ⚠ | ND | — | **Não há arquivo de licença na raiz efetiva** (procurado e não encontrado). Resolveria ler a licença na origem pública. **Quarto e último caso I-04 / bloqueio B-02 do acervo** |
| E13 Testes/evals | 0 | **Inspecionada a listagem completa da raiz efetiva: nenhum teste, eval ou verificação de qualquer natureza** entre as três entradas | — |
| E15 Alegações ⚠ | 1 | Alegação forte com fonte citada porém não conferida: "Generates distinctive, **production-grade** frontend interfaces that avoid generic AI aesthetics" — afirmação de qualidade sem medição, num domínio (estética) que o próprio material trata como avaliável. Os autores estão nomeados com endereço institucional, o que torna a **origem** conferível | — |

**NF = 1 · 4/7 · 3 ND** *(mediana dos determinados [0,1,2,3] = 1,5 → §14.3 vale o inferior)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 4 | Endereça diretamente a pergunta central — como o humano vê o sistema — **mais** artefato concreto e reutilizável (§14.2): uma skill instalável que dirige a geração de interface | — |
| E04 Transferibilidade | 4 | Transferível por configuração, sem alteração de código: instala como plugin e é acionada automaticamente para trabalho de front-end, conforme o próprio README | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto no acervo **como ponto de partida**: `AC-07-REP-004` declara, no próprio README, que "**Impeccable started from there**" — a derivação é fato observado, não alegação do catálogo | — |

**RP = 4 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 5 | Item documental (§14.1): não requer instalação de runtime **e** o artefato declara como é consumido — plugin, acionamento automático em trabalho de front-end, com exemplos de invocação | — |
| E09 Custo | 4 | Custo marginal: apenas as chamadas de modelo já previstas; nenhum serviço externo | — |
| E10 Contexto/tokens | 5 | Medido: **3 arquivos, 9,3 KB** — a menor superfície do acervo inteiro. Manifesto único mais skill, com o restante carregável sob demanda | — |
| E11 Fornecedor | 4 | Abstração documentada: é conteúdo de skill em formato comum; o acionamento é do harness hospedeiro | — |
| E12 Reversibilidade | 4 | Reversível por remoção, sem efeito residual: três arquivos, sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 2** — **PARCIAL.** O conteúdo confere (evita estética genérica, escolhas ousadas, tipografia e paleta distintivas, animação, autores nomeados, ponteiro para o cookbook), mas o catálogo afirma "**a skill oficial da Anthropic**", e o README **não usa a palavra oficial** — traz apenas dois autores com endereço institucional. Atribuição de oficialidade **não observável na fonte** → teto 2 (§14.4).
**O que o catálogo afirma:** "`frontend-design-main/` — **a skill oficial da Anthropic**… **O que extrair:** é o ponto de partida canônico. Leia antes do Impeccable, que se declara derivado dele."
**Confere com a fonte:** parcialmente — a **derivação** afirmada pelo catálogo **confere**, e está no README de `AC-07-REP-004`; a **oficialidade**, não

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Generates distinctive, **production-grade** frontend interfaces that avoid generic AI aesthetics." | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "a skill **oficial** da Anthropic" | `_CONTEUDO.md` área 07 | ALEGAÇÃO DO CATÁLOGO | **não observável na fonte** → sustenta `NC = 2`. O README nomeia dois autores com endereço `@anthropic.com`, o que é indício de origem, não declaração de oficialidade |
| "Anthropic's frontend-design was the first widely-used design skill for Claude. **Impeccable started from there.**" | `README.md` de `AC-07-REP-004` | ALEGAÇÃO DO AUTOR (de outro item do acervo) | **confere como declaração de derivação**, lida na fonte derivada |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 4` · 3 ND · `E15 = 1` (≠ 0) · reconferência confere |
| **V2** | **sim** | `E06 = ND` |
| **V4** | **sim** | `E07 = ND` — licença ausente na raiz efetiva |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** V2 e V4 (§8), que fecham as duas classificações de candidato; §9, condição de entrada de EXIGE PESQUISA.
**Se EXIGE PESQUISA — lacuna nomeada:** duas: (1) **licença e titularidade**, ausentes na raiz efetiva — o quarto e último caso I-04 do acervo; (2) `E06` — o conteúdo de `skills/` não foi lido por inteiro, e é o artefato inteiro do item.  **Verificação que a fecharia:** ler a licença na origem pública e ler `skills/` por completo — leitura mínima, com três arquivos no total.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-07-REP-003 — `hyperframes-main`

**Tipo:** REPO · **Área:** 07_INTERFACE-E-DESIGN
**Hash F0:** `dir · 4185 arq. · aninhado`   **Hash reconferido:** `4185 arq. · aninhamento 1`   **Confere:** sim
**LV:** LV4
**Cobertura da leitura:** raiz efetiva `hyperframes-main/hyperframes-main` (40 entradas); `LICENSE` — Apache License 2.0, 10.763 bytes, íntegro; `README.md` (24.760 bytes, lidos 6 KB: proposta, badges de versão e download, links de documentação); `package.json` (scripts de teste e verificação); `.claude-plugin/`; sinais `SECURITY.md`, `.env.example`, `DESIGN.md`, `ADOPTERS.md`, `CREDITS.md`, `skills-manifest.json`, `Dockerfile.test`, `lefthook.yml`, `commitlint.config.js`, diretórios `registry/`, `releases/` e `updates/`. **Não lidos:** `packages/`, `skills/`, `docs/`, `examples/`.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** não se aplica

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 4 | Artefato completo e inspecionável (monorepo com pacotes, registro de blocos, exemplos, skills e plugins para três harnesses) **mais** procedimento de verificação declarado: `"test": "bun run test:unit"`, testes por pacote, `check:tracked-artifacts`, `check:workspace-contracts` e `Dockerfile.test` | — |
| E03 Maturidade | 4 | Versionado com release identificável (badge de versão npm, diretórios `releases/` e `updates/`) **mais** documentação de instalação e uso (quickstart, catálogo, playground, docs) **mais** tratamento de erro visível na configuração (`lefthook.yml`, `commitlint.config.js`, `knip.config.ts`, verificações de contrato de workspace) | — |
| E05 Manutenção | ND | — | Nenhuma data observada no material lido; `releases/` existe mas não foi enumerado. Resolveria listar `releases/` ou consultar as releases publicadas |
| E06 Segurança ⚠ | 3 | Superfície declarada (renderização de HTML para vídeo, execução em contêiner, plugins de harness) **com controles parciais documentados**: `SECURITY.md`, `.env.example`, ganchos de pré-commit e `Dockerfile.test` para execução isolada | — |
| E07 Licença ⚠ | 4 | Permissiva padrão presente e íntegra: Apache License 2.0, 10.763 bytes, com badge correspondente. Cópia local não prova titularidade → teto 4 | — |
| E13 Testes/evals | 3 | Suíte executável identificável com ponto de entrada declarado (`test`, `test:unit`, testes por pacote, mais uma suíte nomeada de classificação no pacote produtor). Nenhum eval de comportamento de agente identificado | — |
| E15 Alegações ⚠ | 1 | Alegações com fonte citada porém não conferidas: badge de downloads mensais, `ADOPTERS.md` como prova social e o lema "Built for agents". **P-3** aplicado | — |

**NF = 3 · 6/7 · 1 ND** *(mediana dos determinados [1,3,3,4,4,4] = 3,5 → §14.3 vale o inferior)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central pelo lado da **saída**: transformar marcação em vídeo é como o sistema se mostra ao humano, ainda que não seja superfície de comando | — |
| E04 Transferibilidade | 4 | Transferível por configuração: pacote npm, manifesto de skills, plugins para três harnesses e catálogo de blocos prontos | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto **dentro do acervo**: é o único item que produz vídeo a partir de marcação, sem editor | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 4 | Instalação declarada por pacote npm com quickstart documentado; configuração por arquivo. Não alcança 5: exige Node ≥ 22 e cadeia de renderização | — |
| E09 Custo | 4 | Custo marginal: Apache-2.0, sem licença paga; o custo é de processamento local de renderização | — |
| E10 Contexto/tokens | **0** | Medido: **4.185 arquivos, 110,4 MB** — tamanho **acima de 100 MB**; a contagem sozinha fecharia a âncora 1, mas vale a pior das duas | — |
| E11 Fornecedor | 4 | Abstração documentada: três harnesses com plugin próprio, formato de entrada é HTML padrão, saída é vídeo | — |
| E12 Reversibilidade | 4 | Reversível por remoção, sem efeito residual: a entrada é marcação e a saída é arquivo | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (lema literal, requisito de Node ≥ 22, licença Apache 2.0, mantenedor) e **todos** os detalhes conferem com o README e o `LICENSE` lidos.
**O que o catálogo afirma:** "“Write HTML. Render video. Built for agents.” Node ≥22, Apache 2.0, mantido pela HeyGen. **O que extrair:** camada de saída em vídeo sem editor."
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Write HTML. Render video. **Built for agents.**" | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| Badge de downloads mensais e `ADOPTERS.md` | `README.md` e raiz da fonte | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA`; **P-3** |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V2 · V3 · V4 · V5 · V6 · V7 · V8 | **nenhuma** | `E06 = 3` · `E07 = 4` · `LV = 4` · 1 ND · `E15 = 1` (≠ 0) · reconferência confere |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** §9, por eliminação escrita — CANDIDATO FORTE exige `RP ≥ 4` e `RP = 3`; CANDIDATO A PILOTO exige nenhum eixo do Bloco C em 0 e `E10 = 0`; PADRÃO A ESTUDAR exige `E03`, `E05` ou `E08` baixos ou ND, e satisfaz por `E05 = ND` — **nova ocorrência de DEF-13**. Prevaleceu EXIGE PESQUISA pelo critério §3.4: o valor está no artefato e há verificação nomeada.
**Se EXIGE PESQUISA — lacuna nomeada:** (1) `E05 = ND` — nenhuma data de manutenção observada, apesar de existir `releases/`; (2) a superfície de 4.185 arquivos e 110,4 MB não é delimitável a partir do que foi lido.  **Verificação que a fecharia:** listar `releases/` para datar a manutenção e identificar, por `package.json` `files[]` e pelo pacote npm publicado, qual é a superfície efetivamente distribuída — **sem instalar**.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-07-REP-004 — `impeccable-main`

**Tipo:** REPO · **Área:** 07_INTERFACE-E-DESIGN
**Hash F0:** `dir · 2201 arq. · aninhado`   **Hash reconferido:** `2201 arq. · aninhamento 1`   **Confere:** sim
**LV:** LV4
**Cobertura da leitura:** raiz efetiva `impeccable-main/impeccable-main` (38 entradas); `LICENSE` — Apache License 2.0, 10.766 bytes, íntegro, mais `NOTICE.md`; `README.md` (17.418 bytes, lidos 6 KB: proposta, derivação declarada, quick start, o que está incluído, comandos); `package.json` (exportações e scripts); `.claude-plugin/`; `tests/` — **394 arquivos**, com subdiretórios `fixtures`, `framework-fixtures`, `lib`, **`live-e2e`** e **`skill-behavior`**; presença de `PRODUCT.md`, `DESIGN.md`, `skills-lock.json`, `wrangler.toml`, `extension/`, `functions/`; **busca por `SECURITY.md` na raiz efetiva — ausente**. **Não lidos:** `cli/`, `skill/`, `site/`, `docs/`.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** não se aplica

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 4 | Artefato completo e inspecionável (skill, CLI, extensão de navegador, funções, site) **mais** procedimento de verificação declarado e robusto: `tests/` com **394 arquivos**, incluindo `live-e2e/` e `skill-behavior/`, mais `skills-lock.json` e exportação explícita do motor de detecção (`./cli/engine/detect-antipatterns.mjs`, `./browser`) | — |
| E03 Maturidade | 4 | Versionado com release identificável (pacote npm com `README.npm.md` próprio, `skills-lock.json`, scripts de build de release) **mais** documentação de instalação e uso (`npx impeccable install`, `/impeccable init`, site de documentação) **mais** tratamento de erro visível na configuração (`biome.json`, `cli-ignores`, verificações no diretório de testes) | — |
| E05 Manutenção | ND | — | Nenhuma evidência datada dentro da fonte. Resolveria consultar releases e commits na origem pública |
| E06 Segurança ⚠ | 3 | Superfície declarada (CLI, extensão de navegador, funções em borda com `wrangler.toml`) **com controle parcial documentado e relevante**: o README declara que "The CLI and browser extension run the deterministic rules **with no LLM and no API key**" — ou seja, a verificação principal **não envia dado a lugar nenhum**. **Não alcança 4**: não há `SECURITY.md` nem escopo de permissão da extensão no material lido | — |
| E07 Licença ⚠ | 4 | Permissiva padrão presente e íntegra: Apache License 2.0, 10.766 bytes, acompanhada de `NOTICE.md`. Cópia local não prova titularidade → teto 4 | — |
| E13 Testes/evals | 4 | Suíte executável identificável com ponto de entrada **mais** evals de comportamento: o diretório `tests/skill-behavior/` é, pelo nome e pela posição, verificação de comportamento do artefato de instrução, e `live-e2e/` cobre iteração em navegador real. Não alcança 5: nenhum resultado publicado foi lido | — |
| E15 Alegações ⚠ | 2 | Alegações numéricas fortes **com fonte citada e conferível dentro da própria fonte, ainda não conferidas**: "1 skill, **23 commands**, live browser iteration, and **46 deterministic detector rules**" — contáveis em `cli/engine/` e no diretório da skill, não contados sob o teto de leitura | — |

**NF = 4 · 6/7 · 1 ND** *(mediana dos determinados [2,3,4,4,4,4] = 4)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 4 | Endereça diretamente a pergunta central — como o humano vê o sistema — **mais** artefato concreto e reutilizável: o par `PRODUCT.md` + `DESIGN.md` escrito por `init` e lido por todos os comandos seguintes, mais 23 comandos com vocabulário compartilhado | — |
| E04 Transferibilidade | 4 | Transferível por configuração, sem alteração de código: `npx impeccable install` e diretórios de plugin para **onze** harnesses distintos na raiz | — |
| E14 Diferencial | 4 | Sem equivalente pronto no acervo **mais** custo alto de reconstrução: **46 regras determinísticas de detecção que rodam sem modelo e sem chave** — verificação barata e reprodutível de um domínio que todo o resto do acervo trata por opinião | — |

**RP = 4 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 4 | Instalação declarada em um comando (`npx impeccable install`), configuração por `/impeccable init` que escreve os dois arquivos de contexto | — |
| E09 Custo | 4 | Custo marginal: Apache-2.0; as 46 regras determinísticas **não consomem modelo**, e só a crítica por LLM tem custo — o que é declarado explicitamente | — |
| E10 Contexto/tokens | 1 | Medido: **2.201 arquivos, 76,1 MB** — contagem na faixa 1.000–5.000 e tamanho na faixa 20–100 MB | — |
| E11 Fornecedor | 4 | Abstração de fornecedor documentada: onze diretórios de harness na raiz, motor de detecção exportado como módulo independente | — |
| E12 Reversibilidade | 4 | Reversível por remoção, sem efeito residual: os arquivos de contexto ficam no projeto do usuário e são legíveis; a extensão é removível à parte | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (1 skill, 23 comandos, iteração ao vivo, 46 regras determinísticas, os vícios nomeados, o que `init` escreve, a lista de comandos, e a observação de que as regras rodam sem LLM e sem chave) e **todos** os detalhes conferem com o README lido — inclusive a citação literal dos vícios combatidos.
**O que o catálogo afirma:** "1 skill, 23 comandos, iteração ao vivo no navegador e **46 regras determinísticas** de detecção… **O que extrair:** duas coisas. (1) O par `PRODUCT.md` + `DESIGN.md` como fonte da verdade… (2) As 46 regras rodam **sem LLM e sem chave de API**. Verificação determinística é mais barata e mais confiável que pedir opinião ao modelo."
**Confere com a fonte:** sim — é uma das descrições mais precisas do acervo

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "**46 deterministic detector rules** plus LLM-only critique checks. The CLI and browser extension run the deterministic rules with no LLM and no API key." | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — **conferível dentro da fonte** (`cli/engine/detect-antipatterns.mjs`), não conferida sob o teto de leitura |
| "Anthropic's frontend-design was the first widely-used design skill for Claude. **Impeccable started from there.**" | `README.md` da fonte | ALEGAÇÃO DO AUTOR | **fato observado sobre a derivação declarada** — o item de origem está no acervo como `AC-07-REP-002` |
| "Every model trained on the same SaaS templates… Inter for everything, purple-to-blue gradients, cards nested in cards…" | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA`; é o diagnóstico que motiva as 46 regras |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V2 · V3 · V4 · V5 · V6 · V7 · V8 | **nenhuma** | `E06 = 3` · `E07 = 4` · `LV = 4` · 1 ND · `E15 = 2` (≠ 0) · reconferência confere |

#### Resultado
**RF = CANDIDATO A PILOTO**
**Regra que produziu:** §9. **Não** alcança CANDIDATO FORTE: `E15 = 2` está abaixo de 3 no Bloco A. Satisfaz CANDIDATO A PILOTO: `LV ≥ 3` · `E06 = 3` · `E07 = 4` · `RP = 4 ≥ 3` · **1 ND** ≤ 4 · nenhum eixo do Bloco C em 0.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> **CANDIDATO A PILOTO não significa pilotar.** Restrições registradas: `E10 = 1` (2.201 arquivos), `E05 = ND`, ausência de `SECURITY.md` para uma extensão de navegador, e as três contagens do README ainda não conferidas.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-07-REP-005 — `ui-ux-pro-max-skill-main`

**Tipo:** REPO · **Área:** 07_INTERFACE-E-DESIGN
**Hash F0:** `dir · 484 arq. · aninhado`   **Hash reconferido:** `484 arq. · aninhamento 1`   **Confere:** sim
**LV:** LV4
**Cobertura da leitura:** raiz efetiva `ui-ux-pro-max-skill-main/ui-ux-pro-max-skill-main` (18 entradas); `LICENSE` — MIT, 1.075 bytes, "Copyright (c) 2024 Next Level Builder", íntegro; `README.md` (**31.020 bytes**, lidos 6 KB: badges de regras e estilos, CLI npm, e um exemplo de ficha de estilo com fonte, humor, uso recomendado e efeitos); `skill.json` presente; `.releaserc.json` presente; `.claude-plugin/`; **busca por diretório de teste na raiz efetiva — ausente**; **busca por `SECURITY.md` — ausente**. **Não lidos:** `src/`, `cli/`, `projects/`, `preview/`, `screenshots/`, `docs/`.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** não se aplica

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 3 | Artefato completo e inspecionável (skill com manifesto próprio, CLI publicada, catálogo de estilos com tokens concretos — tipografia, humor, uso recomendado, efeitos e tempos de transição), **sem** procedimento de verificação declarado na raiz | — |
| E03 Maturidade | 4 | Versionado com release identificável (badge de release, `.releaserc.json` — automação de versionamento semântico —, pacote CLI publicado em npm) **mais** documentação de instalação e uso (README de 31 KB em duas línguas, `CONTRIBUTING.md`) **mais** tratamento de erro visível na configuração (automação de release com regras declaradas) | — |
| E05 Manutenção | ND | — | Nenhuma evidência datada dentro da fonte. Resolveria consultar as releases na origem pública |
| E06 Segurança ⚠ | 2 | **Superfície ampla sem controle documentado na raiz efetiva**: CLI publicada em npm, badge de Python 3.x indicando execução adicional, diretórios `projects/`, `preview/` e `screenshots/` que sugerem captura e escrita local. **Procurado e não encontrado**: `SECURITY.md`, escopo de permissão, política de dados | — |
| E07 Licença ⚠ | 4 | Permissiva padrão presente e íntegra: MIT, 1.075 bytes, titular nomeado, com badge correspondente. Cópia local não prova titularidade → teto 4 | — |
| E13 Testes/evals | ND | — | **Procurado na listagem da raiz efetiva: não há diretório de teste no topo**, e nenhum script de teste foi observado. Resolveria listar `src/` e `cli/` procurando suíte |
| E15 Alegações ⚠ | 2 | Alegações numéricas fortes **com fonte citada e conferível dentro da própria fonte, ainda não conferidas**: "**161 reasoning rules**" e "**67 UI styles**", ambos como badge. Contáveis em `src/`, não contados sob o teto de leitura. Há ainda badge de estrelas — **P-3** | — |

**NF = 3 · 5/7 · 2 ND** *(mediana dos determinados [2,2,3,4,4] = 3)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 4 | Endereça diretamente a pergunta central **mais** artefato concreto e reutilizável: cada estilo do catálogo vem com tipografia, paleta, humor, uso recomendado e parâmetros de movimento — material diretamente transportável para um documento de design | — |
| E04 Transferibilidade | 4 | Transferível por configuração, sem alteração de código: CLI publicada, `skill.json` e plugin de marketplace | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto **dentro do acervo** pela **amplitude**: 67 estilos com tokens é a maior biblioteca de direção visual do acervo; `AC-07-REP-004` cobre detecção de vício, este cobre escolha de estilo | — |

**RP = 4 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 4 | Instalação declarada por CLI npm publicada, com plugin de marketplace como alternativa | — |
| E09 Custo | 4 | Custo marginal: MIT, sem licença paga; o consumo é o das chamadas de modelo já previstas. **Registrado**: o README traz botão de apoio financeiro voluntário, que não é custo obrigatório | — |
| E10 Contexto/tokens | 2 | Medido: **484 arquivos, 12,8 MB** — contagem na faixa 300–1.000 e tamanho na faixa 5–20 MB | — |
| E11 Fornecedor | 4 | Abstração documentada: skill em formato comum, CLI independente, plugin de marketplace | — |
| E12 Reversibilidade | 4 | Reversível por remoção, sem efeito residual: skill e CLI, sem estado persistente próprio observado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (161 regras de raciocínio, 67 estilos, CLI própria em npm, presença de `preview/`, `screenshots/` e `projects/`) e o detalhe **confere** com os badges e a listagem da raiz — a menos das contagens, que são reproduzidas do README e não foram conferidas por esta frente.
**O que o catálogo afirma:** "Skill com CLI própria em npm. Traz `preview/`, `screenshots/` e `projects/`."
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "**161 reasoning rules**" e "**67 UI styles**" | `README.md` da fonte (badges) | ALEGAÇÃO DO AUTOR | não — **conferíveis dentro da fonte**, não conferidas |
| Badge de estrelas no GitHub | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA`; **P-3** |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V2 · V3 · V4 · V5 · V6 · V7 · V8 | **nenhuma** | `E06 = 2` (≠ 0 e ≠ ND) · `E07 = 4` · `LV = 4` · 2 ND · `E15 = 2` (≠ 0) · reconferência confere |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** §9 — as duas classificações de candidato exigem `E06 ≥ 3`, e aqui `E06 = 2`. **PADRÃO A ESTUDAR** também satisfaz sua condição (`E04 = 4` com `E05 = ND` e `E13 = ND`) — **nova ocorrência de DEF-13**; prevaleceu EXIGE PESQUISA pelo critério §3.4.
**Se EXIGE PESQUISA — lacuna nomeada:** três: (1) a superfície de execução — CLI npm mais Python, sem `SECURITY.md` nem escopo declarado, num artefato que captura telas; (2) `E13` — nenhuma suíte de testes localizada; (3) as duas contagens de badge, conferíveis dentro da fonte.  **Verificação que a fecharia:** ler `cli/` e `src/` para delimitar o que é executado e o que é escrito em disco, localizar a suíte de testes e contar regras e estilos — leitura adicional que estoura o teto de `05` §8 e precisa de autorização.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

> **Nota de aplicação aos cinco PRINT desta área.** Os cinco (`dashboard1.png` … `dashboard5.png`) são um **conjunto**: o próprio catálogo os fecha com um parágrafo único ("O que extrair das cinco juntas"). Todos foram **inspecionados visualmente pela trilha Codex** no relatório `109` e os cinco voltaram **CONFIRMADA** — nenhuma divergência na área. Bloco C dos cinco segue o valor fixo de mídia do índice §3.3. `V2` e `V4` disparam nos cinco: autoria, licença e superfície de segurança de um print não são determináveis por inspeção de pixel.

### AC-07-PRT-001 — `dashboard1.png`

**Tipo:** PRINT · **Área:** 07_INTERFACE-E-DESIGN
**Hash F0:** `AAB6EE531951487E`   **Hash reconferido:** `AAB6EE531951487E`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`109`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-07-PRT-001 · `H-P1-003` (relatório `109`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Descrição com detalhe **reproduzível** e comparativo lado a lado, sem artefato: valor de cor literal `#F7F5F2`, uso de card com sombra suave, e um painel executivo com cinco KPIs nomeados mais linha, rosca e barras por região. `109` confirma fundo, cards, sombra e painel | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e sua data |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Os valores exibidos (Receita R$ 8,72M etc.) parecem dado de demonstração; resolveria confirmar se são dado real de alguma organização |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos de uso da imagem |
| E13 Testes/evals | ND | — | Nenhum critério de verificação exibido: a regra é apresentada, não medida |
| E15 Alegações ⚠ | 2 | Alegação estética com **referência conferível dentro da própria imagem** — o comparativo antes/depois — porém não medida: "fundo branco puro com gráfico solto parece padrão de fábrica" é juízo, não resultado | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central da área — como o humano vê o sistema — sem artefato que a acompanhe | — |
| E04 Transferibilidade | 3 | Transferível com adaptação declarada: um valor hexadecimal e uma regra de card cabem em documento de design sem tradução, mas exigem decisão de quem adota | — |
| E14 Diferencial | 2 | Conveniência sobre conhecimento amplamente acessível: paleta off-white com card é prática comum; o valor está no token concreto | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E08 · E09 · E10 · E11 · E12 | 3 · 5 · 4 · 5 · 4 | Valor fixo de mídia do índice §3.3: item documental sem instalação; sem custo recorrente; evidência derivada curta; PNG, formato aberto; consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (valor de cor literal, card com sombra, painel executivo com KPIs nomeados) conferido contra os pixels; **CONFIRMADA** em `109`.
**O que o catálogo afirma:** "**MATE O BRANCO CHAPADO** — … Troque por off-white (**#F7F5F2**) e coloque cada visual num card com sombra suave. O comparativo usa um painel 'Visão Executiva' com KPIs (Receita Total R$ 8,72M, Lucro Líquido, Margem, Ticket Médio, Clientes Ativos) mais linha, donut e barras por região."
**Confere com a fonte:** sim — CONFIRMADA em `109`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Fundo branco puro com gráfico solto parece padrão de fábrica." | print, via `109` | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA`; juízo estético |
| "Fundo `#F7F5F2`, cards, sombra suave e painel executivo conferem." | `109` | FATO OBSERVADO (por inspeção da trilha Codex) | sim, quanto ao que está na imagem |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 2` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4 do índice (não há verificação nomeada que mude a classe: é imagem, e o que ela mostra já foi conferido).
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-07-PRT-002 — `dashboard2.png`

**Tipo:** PRINT · **Área:** 07_INTERFACE-E-DESIGN
**Hash F0:** `E8CAEB562E422E3B`   **Hash reconferido:** `E8CAEB562E422E3B`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`109`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-07-PRT-002 · `H-P1-003` (relatório `109`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Descrição com detalhe reproduzível e **demonstração na própria imagem**: tudo em cinza com um único destaque em dourado sobre "Ticket Médio". `109` confirma "um accent e o restante em cinza" | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e sua data |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando dado sensível ou instrução ao leitor |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos de uso da imagem |
| E13 Testes/evals | ND | — | Nenhuma medição: a alegação de acessibilidade é feita, não testada |
| E15 Alegações ⚠ | 1 | Alegação com fonte citada porém não conferida, inclusive uma **alegação técnica**: "melhora acessibilidade de quebra" — afirmação sobre contraste que nenhum número na imagem sustenta | — |

**NF = 1 · 2/7 · 5 ND** *(mediana dos determinados [1,2] = 1,5 → §14.3 vale o inferior)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: é regra de hierarquia visual — o que o humano enxerga primeiro | — |
| E04 Transferibilidade | 3 | Transferível com adaptação declarada: "uma cor de destaque, o resto em cinza" vira token de tema com uma decisão de qual é o destaque | — |
| E14 Diferencial | 2 | Conveniência sobre conhecimento amplamente acessível: hierarquia por cor única é regra clássica de visualização | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E08 · E09 · E10 · E11 · E12 | 3 · 5 · 4 · 5 · 4 | Valor fixo de mídia do índice §3.3 | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (tudo cinza, um único destaque em dourado, aplicado a "Ticket Médio") conferido contra os pixels; **CONFIRMADA** em `109`.
**O que o catálogo afirma:** "**UMA COR MANDA, O RESTO OBEDECE** — … A regra: uma cor de destaque, todo o resto em cinza — *o dado importante grita e o contexto sussurra*. No exemplo, tudo cinza com apenas 'Ticket Médio' e uma barra em dourado. **O que extrair:** simplifica tokens de tema e melhora acessibilidade de quebra."
**Confere com a fonte:** sim — CONFIRMADA em `109`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "melhora acessibilidade de quebra" | `_CONTEUDO.md` área 07 | ALEGAÇÃO DO CATÁLOGO | **não** — nenhuma razão de contraste medida; `NÃO VERIFICADA` |
| "*o dado importante grita e o contexto sussurra*" | print, via `109` | ALEGAÇÃO DO AUTOR | não — figura de linguagem |

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

### AC-07-PRT-003 — `dashboard3.png`

**Tipo:** PRINT · **Área:** 07_INTERFACE-E-DESIGN
**Hash F0:** `DC4547447569E197`   **Hash reconferido:** `DC4547447569E197`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`109`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-07-PRT-003 · `H-P1-003` (relatório `109`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | O mais reproduzível dos cinco: proporção numérica declarada (**rótulo 3× menor que o valor**), caixa alta, cor cinza, e **anatomia completa de componente** — ícone, valor dominante, rótulo secundário, variação percentual com cor de direção e o texto de comparação. `109` confirma proporção, caixa alta, variação e comparação mensal "como regra exibida" | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e sua data |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando dado sensível ou instrução ao leitor |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos de uso da imagem |
| E13 Testes/evals | ND | — | Nenhuma medição de legibilidade: a proporção é prescrita, não testada | 
| E15 Alegações ⚠ | 2 | Alegação numérica **conferível dentro da própria imagem e conferida**: `109` registra que a proporção 3× está de fato exibida. Não alcança 3 porque nada mede que a proporção produza o efeito afirmado | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: define como um indicador é lido pelo humano | — |
| E04 Transferibilidade | 3 | Transferível com adaptação declarada: a anatomia do cartão de indicador vira especificação de componente quase sem tradução | — |
| E14 Diferencial | 2 | Conveniência sobre conhecimento amplamente acessível, com um ganho concreto: a razão numérica e a cor de direção economizam a decisão | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E08 · E09 · E10 · E11 · E12 | 3 · 5 · 4 · 5 · 4 | Valor fixo de mídia do índice §3.3 | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (proporção 3×, caixa alta e cinza, anatomia de cinco partes, texto literal "vs. mês anterior") conferido contra os pixels; **CONFIRMADA** em `109`.
**O que o catálogo afirma:** "**NÚMERO GIGANTE, RÓTULO PEQUENO** — O número deve ser **3× maior** que o rótulo… A anatomia do card de KPI: ícone + valor dominante + rótulo secundário + variação percentual com cor de direção (verde alta, vermelho queda) e o texto 'vs. mês anterior'."
**Confere com a fonte:** sim — CONFIRMADA em `109`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "O número deve ser **3× maior** que o rótulo" | print, via `109` | ALEGAÇÃO DO AUTOR — **prescrição**, não medição | a **exibição** da proporção confere (`109`); o **efeito** afirmado, não |
| "verde alta, vermelho queda" | print, via `109` | FATO OBSERVADO | sim — registrado também como convenção que ignora daltonismo, não tratada pela fonte |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 2` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4 do índice.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-07-PRT-004 — `dashboard4.png`

**Tipo:** PRINT · **Área:** 07_INTERFACE-E-DESIGN
**Hash F0:** `EB6F073D81DC2538`   **Hash reconferido:** `EB6F073D81DC2538`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`109`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-07-PRT-004 · `H-P1-003` (relatório `109`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | **Só descrição qualitativa**: "mesmas margens, mesmo respiro entre cards, bordas casadas" — nenhum valor, nenhuma unidade, nenhuma escala de espaçamento. `109` confirma que margens e alinhamentos **são consistentes na imagem**, mas a regra exibida não é quantificada. É o menos reproduzível dos cinco | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e sua data |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando dado sensível ou instrução ao leitor |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos de uso da imagem |
| E13 Testes/evals | ND | — | Nenhuma verificação exibida | 
| E15 Alegações ⚠ | 1 | Alegação com fonte citada porém não conferida: "algo que ninguém aponta mas todo mundo sente" — afirmação sobre percepção humana, sem qualquer medição | — |

**NF = 1 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: alinhamento é condição de leitura | — |
| E04 Transferibilidade | 3 | Transferível com adaptação declarada — mas a adaptação é grande: sem escala numérica, quem adota precisa inventar os valores | — |
| E14 Diferencial | 1 | **Conveniência sobre conhecimento amplamente acessível**: grade e espaçamento consistente é o primeiro item de qualquer manual de layout, inclusive dos repositórios desta mesma área | — |

**RP = 3 · 3/3 · 0 ND** *(mediana de [1,3,3] = 3)*

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E08 · E09 · E10 · E11 · E12 | 3 · 5 · 4 · 5 · 4 | Valor fixo de mídia do índice §3.3 | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — o detalhe afirmado (margens iguais, respiro igual, bordas casadas) foi **conferido contra os pixels** e voltou consistente; **CONFIRMADA** em `109`. A descrição não afirma nada além do que a imagem mostra.
**O que o catálogo afirma:** "**A GRADE INVISÍVEL** — Visual meio torto e espaçamento diferente em cada canto é algo que ninguém aponta mas todo mundo sente. Mesmas margens, mesmo respiro entre cards, bordas casadas."
**Confere com a fonte:** sim — CONFIRMADA em `109`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "algo que ninguém aponta mas todo mundo sente" | print, via `109` | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA`; afirmação sobre percepção |
| "Margens, respiros e alinhamentos consistentes conferem." | `109` | FATO OBSERVADO | sim, quanto ao que está na imagem |

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

### AC-07-PRT-005 — `dashboard5.png`

**Tipo:** PRINT · **Área:** 07_INTERFACE-E-DESIGN
**Hash F0:** `518DCF3E32385DA8`   **Hash reconferido:** `518DCF3E32385DA8`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`109`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-07-PRT-005 · `H-P1-003` (relatório `109`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Descrição com detalhe reproduzível na forma de **ações concretas de remoção** — apagar bordas, eliminar linhas de grade, deixar o espaço separar — e `109` confirma que a remoção e o uso de espaço em branco estão de fato na imagem | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e sua data |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando dado sensível ou instrução ao leitor |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos de uso da imagem |
| E13 Testes/evals | ND | — | Nenhuma verificação exibida | 
| E15 Alegações ⚠ | 1 | Alegações com fonte citada porém não conferidas, duas delas fortes: "cara de Excel 2007" e "*dashboard caro não é o que tem mais, é o que teve coragem de tirar*" — a segunda associa densidade visual a valor percebido, sem qualquer medição | — |

**NF = 1 · 2/7 · 5 ND** *(mediana dos determinados [1,2] = 1,5 → §14.3 vale o inferior)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: densidade e ruído determinam o que o humano consegue ler | — |
| E04 Transferibilidade | 3 | Transferível com adaptação declarada: são três ações de remoção, aplicáveis a qualquer biblioteca de gráfico | — |
| E14 Diferencial | 2 | Conveniência sobre conhecimento amplamente acessível: redução de ruído gráfico é princípio clássico; o ganho está na forma acionável | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E08 · E09 · E10 · E11 · E12 | 3 · 5 · 4 · 5 · 4 | Valor fixo de mídia do índice §3.3 | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (bordas apagadas, linhas de grade eliminadas, espaço em branco como separador) conferido contra os pixels; **CONFIRMADA** em `109`.
**O que o catálogo afirma:** "**MENOS CAIXA, MAIS RESPIRO** — Borda em tudo, linha de grade e fundo em cada visual dão 'cara de Excel 2007'. Apague as bordas, elimine as gridlines, deixe o espaço separar. A frase-síntese: *dashboard caro não é o que tem mais, é o que teve coragem de tirar*."
**Confere com a fonte:** sim — CONFIRMADA em `109`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "*dashboard caro não é o que tem mais, é o que teve coragem de tirar*" | print, via `109` | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "são especificação de design system, não dica solta… Cabem num `DESIGN.md` quase sem tradução." | `_CONTEUDO.md` área 07, fechando os cinco | ALEGAÇÃO DO CATÁLOGO | **parcialmente** — os cinco de fato dão paleta, regra de cor, anatomia de componente, grade e densidade; "quase sem tradução" é juízo do catálogo, não fato |

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

> **Nota de aplicação aos três VÍDEO desta área.** LV3-V vem de `H-M2-003` (relatório `97`); LV3-A, quando existe, vem do manifesto `117`. **A soma LV3-V + LV3-A não produz LV4** e a transcrição automática **não autoriza citação exata** — as falas abaixo entram como conteúdo aproximado, nunca como literal. Conforme o estado corrente da multimídia, **V5 não é aplicado automaticamente a vídeo**: pontuam-se apenas os eixos destravados e o resto é ND. Bloco C segue o valor fixo do índice §3.3.

### AC-07-VID-001 — `exemplo .mp4`

**Tipo:** VÍDEO · **Área:** 07_INTERFACE-E-DESIGN
**Hash F0:** `D3CCFF036EC70356`   **Hash reconferido:** `D3CCFF036EC70356`   **Confere:** sim
**LV:** **LV3-V** (sem LV3-A aproveitável)
**Cobertura da leitura:** análise visual por quadros-chave da trilha Codex (`97`, `H-M2-003`); áudio processado — 15,7 s, idioma detectado `en`, 21 palavras, 3 segmentos, confiança 0,894, classificado em `117` como **LETRA/TRILHA MUSICAL — NÃO É NARRAÇÃO**. **Não há narração a aproveitar**: o áudio é trilha, e por isso este item não recebe LV3-A.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-07-VID-001 · `H-M2-003` (relatório `97`) · manifesto `117`

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | **Só demonstração de resultado**: gravação de um site escuro, editorial e cinematográfico. `97` registra explicitamente que **não há processo, prompts nem evidência de qual ferramenta produziu qual parte** | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e sua data |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Não há superfície de execução a avaliar; resolveria obter os artefatos-fonte que `97` diz serem necessários |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos do vídeo e do site exibido |
| E13 Testes/evals | ND | — | Nenhuma verificação exibida | 
| E15 Alegações ⚠ | 1 | Alegações fortes com fonte citada porém não conferidas, **exibidas na própria tela**: a atribuição a "Antigravity + Nano Banana 2 + Claude Design" e a chamada "Just Copy My Prompts" — nenhum prompt é mostrado no material analisado | — |

**NF = 1 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central pelo lado da direção visual — o que o humano vê —, sem artefato | — |
| E04 Transferibilidade | 1 | **Só a ideia viaja**: sem prompt, sem código e sem atribuição causal, nada é reexecutável | — |
| E14 Diferencial | 1 | Conveniência sobre conhecimento amplamente acessível: é uma referência estética entre muitas | — |

**RP = 1 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E08 · E09 · E10 · E11 · E12 | 3 · 5 · 4 · 5 · 4 | Valor fixo de mídia do índice §3.3 | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (site escuro editorial, atribuição exibida na tela, chamada "Just Copy My Prompts") conferida por análise visual em `97`, que **acrescenta** a ausência de processo em vez de escondê-la.
**O que o catálogo afirma:** "demonstração visual de site arquitetônico… atribuído na tela a 'Antigravity + Nano Banana 2 + Claude Design'… **Valor:** referência de direção visual e composição. Não há processo, prompts nem evidência de qual ferramenta produziu qual parte."
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal, tal como exibida) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Antigravity + Nano Banana 2 + Claude Design" | texto na tela do vídeo, via `97` | ALEGAÇÃO DO AUTOR — atribuição de ferramenta | **não** — nenhuma evidência de qual ferramenta produziu qual parte |
| "Just Copy My Prompts" | texto na tela do vídeo, via `97` | ALEGAÇÃO DO AUTOR | **não** — nenhum prompt é exibido |
| Áudio classificado como "LETRA/TRILHA MUSICAL — NÃO É NARRAÇÃO" | `117` | FATO OBSERVADO (classificação da trilha Codex) | sim — sustenta a ausência de LV3-A |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · 5 ND < 8 · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |
| **V5** | **não aplicado** | `LV = 3` (LV3-V), acima do gatilho; e o estado corrente da multimídia proíbe aplicação automática de V5 a vídeo |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4 do índice. `RP = 1` fecha qualquer classe de candidato.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-07-VID-002 — `Gravando 2026-07-28 163723.mp4`

**Tipo:** VÍDEO · **Área:** 07_INTERFACE-E-DESIGN
**Hash F0:** `0D72EF229FB5B1FF`   **Hash reconferido:** `0D72EF229FB5B1FF`   **Confere:** sim
**LV:** **LV3-V + LV3-A** — e, conforme o estado corrente, **a soma não produz LV4**
**Cobertura da leitura:** análise visual por quadros-chave (`97`, `H-M2-003`) **mais** transcrição automática bruta integral (`117`, ficha `AC-07-VID-002`): 56,7 s, idioma `pt`, 234 palavras, 20 segmentos, confiança média de token 0,855, estado **ALTA AUTOMÁTICA**, 26 de 331 tokens abaixo de 0,50. É o **único item da área com fala narrativa aproveitável**. Transcrição não revisada por humano — **proibido tratar como citação exata**.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-07-VID-002 · `H-M2-003` (relatório `97`) · `H-M3-001` · manifesto `117`

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Acima da simples demonstração: o vídeo mostra o **resultado** (painel de anúncios e analytics), o **meio** (código em HTML/JavaScript, menção a API em Python) e o **método declarado** (páginas de sistema de design com cor, superfície, componente, movimento e interação). Ainda assim **não há artefato**: nenhum arquivo, repositório ou prompt é entregue | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e sua data |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Nenhuma superfície inspecionável; resolveria obter o código exibido |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos do vídeo e do código exibido |
| E13 Testes/evals | ND | — | Nenhuma verificação exibida; o critério de "consistência" é afirmado, não medido | 
| E15 Alegações ⚠ | 1 | Alegações fortes com fonte citada porém não conferidas, e **por STT automático**, o que impede citação exata: conteúdo aproximado de ganho de velocidade ("dashboards muito mais rápidos"), de qualidade ("designs absurdos") e de flexibilidade ("100% customizáveis"), além de versão de modelo mencionada. Nenhum número, nenhuma medição | — |

**NF = 1 · 2/7 · 5 ND** *(mediana dos determinados [1,2] = 1,5 → §14.3 vale o inferior)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: descreve uma divisão de trabalho entre humano e modelo na produção da interface — quem escreve o quê | — |
| E04 Transferibilidade | 2 | Transferível com adaptação **não declarada**: o achado — especificar tokens, componentes e movimento **antes** de gerar — é reutilizável, mas o vídeo não entrega as páginas do sistema de design que exibe | — |
| E14 Diferencial | 2 | Conveniência sobre conhecimento amplamente acessível: a mesma prática está, em forma de artefato, em `AC-07-REP-004` (par `PRODUCT.md` + `DESIGN.md`) e em `AC-07-REP-005` (catálogo de estilos) — que **entregam** o que este vídeo apenas mostra | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E08 · E09 · E10 · E11 · E12 | 3 · 5 · 4 · 5 · 4 | Valor fixo de mídia do índice §3.3 | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (painel de anúncios/analytics, código em HTML/JavaScript, menção a FastAPI e a uma versão de modelo, seguidos de páginas de sistema de design com cor, superfície, componente, movimento e interação) conferida por análise visual em `97`. O catálogo **marca por conta própria** o que permanece alegação — versão do modelo, técnica e contribuição causal.
**O que o catálogo afirma:** "dashboard guiado por design system… **Achado:** especificar tokens, componentes e movimento antes de gerar/tornar consistente a interface. Versão do modelo, técnica e contribuição causal permanecem alegações."
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (conteúdo aproximado — **STT automático, não é citação exata**) | Origem | Camada | Verificada? |
|---|---|---|---|
| que a nova forma permitiria "dashboards muito mais rápidos, com designs absurdos e 100% customizáveis" | LV3-A, `117` | ALEGAÇÃO DO AUTOR | **não** — nenhuma medição; e a transcrição é automática |
| que o autor divide o trabalho: o modelo monta o front em HTML/JavaScript/CSS e o humano fica com a API em Python | LV3-A, `117` | ALEGAÇÃO DO AUTOR — descrição de método | **não** — o método é descrito, não demonstrado ponta a ponta |
| menção a FastAPI e a uma versão de modelo | LV3-V (`97`) e LV3-A (`117`) | ALEGAÇÃO DO AUTOR | **não** — `97` registra que a versão do modelo permanece alegação; **STT troca nomes e números** |
| "vibe design" como nome dado pelo autor à prática | LV3-A, `117` | ALEGAÇÃO DO AUTOR — termo do autor | grafia **não confirmável** por STT |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · 5 ND < 8 · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |
| **V5** | **não aplicado** | `LV = 3` · aplicação automática a vídeo proibida pelo estado corrente |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4 do índice. `RP = 2` fecha as classes de candidato.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-07-VID-003 — `Gravando 2026-07-29 092040.mp4`

**Tipo:** VÍDEO · **Área:** 07_INTERFACE-E-DESIGN
**Hash F0:** `7C4E279C5FF3E0E6`   **Hash reconferido:** `7C4E279C5FF3E0E6`   **Confere:** sim
**LV:** **LV3-V** (sem LV3-A aproveitável)
**Cobertura da leitura:** análise visual por quadros-chave (`97`, `H-M2-003`); áudio processado — 10,4 s, idioma detectado `en`, **1 palavra**, 1 segmento, confiança 0,751, classificado em `117` como **SEM FALA LEXICAL CONFIÁVEL**. Todo o conteúdo é texto na tela.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-07-VID-003 · `H-M2-003` (relatório `97`) · manifesto `117`

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | **Só listagem**: cinco repositórios nomeados com uma linha de função cada, sem demonstração, sem comparação e sem critério de escolha. `97` registra que nomes, licenças, números e segurança **precisam ser confirmados antes de baixar** | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e sua data |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Item que **instrui a baixar repositórios de terceiros**; resolveria inspecionar cada um dos cinco alvos — dois dos quais já estão no acervo e foram avaliados aqui |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos do vídeo | 
| E13 Testes/evals | ND | — | Nenhuma verificação exibida | 
| E15 Alegações ⚠ | 1 | Alegações de capacidade por repositório, com **fonte citada e conferível** — os nomes são endereços de origem —, porém não conferidas no vídeo. Duas delas **são conferíveis dentro do próprio acervo**: `nextlevelbuilder/ui-ux-pro-max-skill` bate com o titular "Next Level Builder" da licença MIT de `AC-07-REP-005`, e `impeccable` bate com `AC-07-REP-004`. A atribuição de propriedade `pbakaus/impeccable` **não foi conferida** | — |

**NF = 1 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: organiza o problema em três frentes — direção visual, sistema de design e retorno visual para o agente | — |
| E04 Transferibilidade | 1 | **Só a ideia viaja**: é uma lista de nomes; nada é executável a partir do vídeo | — |
| E14 Diferencial | 2 | Conveniência sobre inventário já acessível: **dois dos cinco itens que ele indica já estão no acervo** como repositório completo (`AC-07-REP-004`, `AC-07-REP-005`); o valor residual são os três nomes restantes, que o acervo não contém | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E08 · E09 · E10 · E11 · E12 | 3 · 5 · 4 · 5 · 4 | Valor fixo de mídia do índice §3.3 | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (os cinco nomes de repositório e a função atribuída a cada um) conferida por análise visual em `97`; a grafia dos nomes foi preservada. O catálogo **acrescenta a ressalva** de confirmação antes de baixar.
**O que o catálogo afirma:** "cinco capacidades para frontend com Claude Code: `pbakaus/impeccable`… `alchaincy/huashu-design`… `nextlevelbuilder/ui-ux-pro-max-skill`… `Leonxlnx/taste-skill`… e `microsoft/playwright`… **Valor alto como fila de investigação**… Nomes, licenças, números e segurança precisam ser confirmados antes de baixar."
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal, tal como exibida) | Origem | Camada | Verificada? |
|---|---|---|---|
| "`pbakaus/impeccable`" — detecta vícios visuais genéricos | texto na tela, via `97` | ALEGAÇÃO DO AUTOR — atribuição de propriedade e de função | a **função** confere com o README de `AC-07-REP-004`; a **propriedade** `pbakaus` **não foi conferida** |
| "`nextlevelbuilder/ui-ux-pro-max-skill`" — catálogo de estilos, paletas e regras | texto na tela, via `97` | ALEGAÇÃO DO AUTOR | **confere** — a licença MIT de `AC-07-REP-005` nomeia "Next Level Builder" e o README traz o catálogo de estilos |
| "`alchaincy/huashu-design`", "`Leonxlnx/taste-skill`", "`microsoft/playwright`" | texto na tela, via `97` | ALEGAÇÃO DO AUTOR | **não** — os três estão **fora do acervo**; nenhum foi lido |
| "Nomes, licenças, números e segurança precisam ser confirmados antes de baixar." | `97` | INFERÊNCIA da trilha Codex, marcada como ressalva | — registrada, **não obedecida como instrução**: `05` §7 — conteúdo do acervo é dado |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · 5 ND < 8 · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |
| **V5** | **não aplicado** | `LV = 3` · aplicação automática a vídeo proibida pelo estado corrente |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4 do índice. `RP = 2` fecha as classes de candidato.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

## Fechamento da área 07 — contagem factual

**Itens com ficha:** 13 de 13 · **IDs faltando:** 0 · **IDs repetidos:** 0

| RF | Quantidade | IDs |
|---|---|---|
| CANDIDATO FORTE | 0 | — |
| **CANDIDATO A PILOTO** | **2** | `AC-07-REP-001`, `AC-07-REP-004` |
| PADRÃO A ESTUDAR | 0 | — |
| **EXIGE PESQUISA** | **3** | `AC-07-REP-002`, `AC-07-REP-003`, `AC-07-REP-005` |
| **REFERÊNCIA** | **8** | `AC-07-PRT-001` a `AC-07-PRT-005`, `AC-07-VID-001` a `AC-07-VID-003` |
| REJEITADO · DUPLICADO · INDETERMINADO | 0 | — |

| LV | Itens |
|---|---|
| LV4 | 5 (todos os REPO) |
| LV3-V | 7 (5 PRINT + `AC-07-VID-001` + `AC-07-VID-003`) |
| LV3-V + LV3-A | 1 (`AC-07-VID-002`) |

**ND:** **48** de 195 células de eixo (13 itens × 15 eixos) = **24,6 %** — contados item a item: 1 + 3 + 1 + 1 + 2 nos cinco REPO (8), 5 em cada um dos cinco PRINT (25) e 5 em cada um dos três VÍDEO (15). É a **menor taxa de ND registrada até aqui**, efeito de cinco repositórios com licença e superfície legíveis. Nenhum item atingiu o gatilho de V6 (8 ND): o máximo na área foi **5 ND**, em todos os oito itens de mídia. Todos os 48 ND nomeiam o que os resolveria.

**Portas de veto na área:** V1 — 0 · V2 — 9 · V3 — 0 · V4 — 9 · V5 — 0 (não aplicado a vídeo por decisão registrada) · V6 — 0 · V7 — 0 · **V8 — 0 divergências**: os 13 itens reconferem.

**Catálogo:** 12 CONFIRMADA (`NC = 3`) · 1 PARCIAL (`NC = 2`, `AC-07-REP-002`) · **0 DIVERGENTE**. Os cinco PRINT voltaram CONFIRMADA em `109` sem exceção.

**Registros novos desta área:**
1. **Quarto e último caso I-04 / B-02** — `AC-07-REP-002` sem arquivo de licença na raiz efetiva. Fecha a lista de repositórios sem licença do acervo.
2. **Derivação declarada entre itens do acervo** — o README de `AC-07-REP-004` afirma literalmente que o projeto partiu de `AC-07-REP-002`. É a primeira relação de linhagem **observada na fonte**, não afirmada pelo catálogo.
3. **Cruzamento de mídia com repositório** — `AC-07-VID-003` indica cinco repositórios, e **dois deles são itens desta mesma área**; um dos nomes (`nextlevelbuilder`) confere com o titular da licença de `AC-07-REP-005`. Três dos cinco estão fora do acervo.
4. **DEF-13 reincidente** — duas novas ocorrências (`AC-07-REP-003`, `AC-07-REP-005`) em que PADRÃO A ESTUDAR e EXIGE PESQUISA são simultaneamente satisfeitas e a rubrica não declara precedência.
5. **`E10 = 0` pela segunda vez no acervo** — `AC-07-REP-003`, por 110,4 MB.

> Esta seção é contagem de fichas, não classificação de valor. Não há ordenação, ranking ou recomendação.

