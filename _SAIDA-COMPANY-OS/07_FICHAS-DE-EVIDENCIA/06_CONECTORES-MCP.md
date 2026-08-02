> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

# FICHAS DE EVIDÊNCIA — ÁREA 06 — CONECTORES E MCP

**Fase:** 2 — Extração · **Data:** 2026-07-29 · **Avaliador:** Claude Opus 5 (Fase 2)
**Itens:** 40 — 4 REPO · 13 PRINT · 23 VÍDEO · 0 PLANILHA
**Convenções de aplicação:** `00_INDICE-DA-FASE-2.md` §3

**Pergunta central da área (base de E01):** *como o sistema alcança o mundo externo.*

> **Observação de método para esta área.** Conector é fronteira de autoridade: identidade, credencial, dados alcançáveis, operações permitidas e efeitos externos. `E06` foi pontuado sobre a **superfície declarada na fonte** — nunca sobre a promessa de segurança. Onde a fonte declara contornar controle de plataforma de terceiro, isso é registrado como **risco ativo declarado** (`E06 = 1`), pelo mesmo critério aplicado a `AC-04-REP-005`.

---

### AC-06-REP-001 — `agent-browser-main`

**Tipo:** REPO · **Área:** 06_CONECTORES-MCP
**Hash F0:** `dir · 413 arq. · aninhado`   **Hash reconferido:** `413 arq. · aninhamento 1`   **Confere:** sim
**LV:** LV4
**Cobertura da leitura:** raiz efetiva `agent-browser-main/agent-browser-main` (25 entradas); `LICENSE` — Apache License 2.0, 10.931 bytes, íntegro; `README.md` (**73.453 bytes**, lidos 6 KB: instalação em quatro métodos, requisitos, início rápido, catálogo de comandos); `package.json` integral; `evals/` — 18 arquivos (`cases`, `lib`, `run.ts`, `context-footprint.ts`); `benchmarks/` — 8 arquivos (`bench.ts`, `scenarios.ts`); `CHANGELOG.md` (entrada `0.31.1`); `agent-browser.schema.json`; **busca por `SECURITY.md` na raiz efetiva — ausente**. **Não lidos:** `cli/`, `packages/`, `skills/`, `docs/`.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** não se aplica

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 4 | Artefato completo e inspecionável (binário Rust, CLI, esquema JSON, skills empacotadas) **mais** procedimento de verificação declarado: `evals/` com ponto de entrada `run.ts` e `benchmarks/` com `bench.ts` e `scenarios.ts` | — |
| E03 Maturidade | 4 | Versionado com release identificável (`"version": "0.31.1"`, `CHANGELOG.md` com marcadores de release, publicação em npm, Homebrew e Cargo) **mais** documentação de instalação e uso (quatro métodos, comando `upgrade` que detecta o método) **mais** tratamento de erro visível: o README declara que `install --with-deps` "exits nonzero if the package manager cannot install every required browser library" e que cliques falham cedo quando outro elemento cobre o alvo | — |
| E05 Manutenção | ND | — | O `CHANGELOG` traz a versão e correções nominais, mas **nenhuma data** foi observada. Resolveria consultar a página de releases na origem pública |
| E06 Segurança ⚠ | 2 | **Superfície ampla sem controle documentado na raiz efetiva**: o catálogo de comandos inclui `eval <js>` (execução de JavaScript arbitrário na página), `connect <port>` (conexão a navegador por protocolo de depuração), `stream enable` (WebSocket de streaming em porta), `upload`, `pdf` e `screenshot`. **Procurado e não encontrado**: `SECURITY.md`, política de permissão, escopo de origem permitida | — |
| E07 Licença ⚠ | 4 | Permissiva padrão presente e íntegra: Apache License 2.0, 10.931 bytes; `"license": "Apache-2.0"` no `package.json`. Cópia local não prova titularidade → teto 4 | — |
| E13 Testes/evals | 4 | `evals/` inspecionado: 18 arquivos com `cases/`, ponto de entrada `run.ts` e `package.json` próprio — suíte executável identificável — **mais** eval de comportamento de agente explicitamente nomeado (`context-footprint.ts`), além de `benchmarks/` separado. Não alcança 5: nenhum resultado publicado e reprodutível foi lido | — |
| E15 Alegações ⚠ | 1 | Alegações fortes com fonte citada porém não conferidas: "**Fast** native Rust CLI" sem número no trecho lido, mais badge de diretório externo. O repositório **tem** `benchmarks/`, o que torna a alegação conferível na fonte, mas nenhum resultado foi lido | — |

**NF = 4 · 6/7 · 1 ND** *(mediana dos determinados [1,2,4,4,4,4] = 4)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 4 | Endereça diretamente a pergunta central — alcançar a web — **mais** artefato concreto: comandos que devolvem **árvore de acessibilidade com referências** (`snapshot`, `click @e2`), desenhados para consumo por agente em vez de seletor CSS frágil | — |
| E04 Transferibilidade | 4 | Transferível por configuração: quatro caminhos de instalação, detecção automática de navegador já instalado, esquema JSON de configuração e skills empacotadas no próprio pacote | — |
| E14 Diferencial | 4 | Sem equivalente pronto no acervo **mais** custo alto de reconstrução: binário nativo com protocolo de acessibilidade próprio para agentes; os demais itens da área **citam** automação de navegador, este a entrega | — |

**RP = 4 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 4 | Instalação declarada em um comando (`npm install -g agent-browser`), configuração por esquema. Não alcança 5: exige download de navegador dedicado | — |
| E09 Custo | 4 | Custo marginal: Apache-2.0, sem licença paga; o custo é o do navegador local e das chamadas já previstas | — |
| E10 Contexto/tokens | 2 | Medido: **413 arquivos, 6,6 MB** — contagem na faixa 300–1.000 e tamanho na faixa 5–20 MB | — |
| E11 Fornecedor | 4 | Abstração documentada: detecta instalações existentes de quatro navegadores/ferramentas e opera sobre protocolo de depuração padrão | — |
| E12 Reversibilidade | 4 | Reversível por remoção, sem efeito residual no repositório do usuário; o navegador baixado é artefato separado e removível | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (CLI em Rust nativo, autoria, presença de `benchmarks/`, `evals/` e `skills/`) e **todos** os detalhes conferem com a listagem da raiz efetiva e o `package.json`.
**O que o catálogo afirma:** "CLI em Rust nativo, feito pela Vercel Labs. Rápido. Traz `benchmarks/`, `evals/` e `skills/`."
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Browser automation CLI for AI agents. **Fast** native Rust CLI." | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — **conferível dentro da fonte** (`benchmarks/`), não conferida |
| "Existing Chrome, Brave, Playwright, and Puppeteer installations are detected automatically." | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — código não lido |
| "Rápido." | `_CONTEUDO.md` área 06 | ALEGAÇÃO DO CATÁLOGO | não — `NÃO VERIFICADA` |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V2 · V3 · V4 · V5 · V6 · V7 · V8 | **nenhuma** | `E06 = 2` (≠ 0 e ≠ ND, logo V2 **não** dispara) · `E07 = 4` · `LV = 4` · 1 ND · `E15 = 1` (≠ 0) · reconferência confere |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** §9 — as duas classificações de candidato exigem `E06 ≥ 3`, e aqui `E06 = 2`. **Registra-se que PADRÃO A ESTUDAR também satisfaz sua condição** (`E04 = 4` com `E05 = ND`) — nova ocorrência de **DEF-13**. Prevaleceu EXIGE PESQUISA pelo critério §3.4 do índice: neste item **o valor está no artefato**, não no padrão, e existe verificação nomeada que muda o que ele vale. *(Distinção declarada em relação a `AC-03-REP-007`, onde a própria fonte e o catálogo situam o valor no padrão.)*
**Se EXIGE PESQUISA — lacuna nomeada:** a superfície de segurança — execução de JavaScript arbitrário, conexão por protocolo de depuração e streaming em porta —, **sem `SECURITY.md` nem política de permissão na raiz efetiva**; e `E05 = ND`.  **Verificação que a fecharia:** ler `cli/` e `packages/` procurando confinamento, allowlist de origem e escopo de `eval`; e consultar a página de releases para datar a manutenção — **sem executar**.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-06-REP-002 — `Agent-Reach-main`  ·  ⚠ contorno de controle de plataforma declarado

**Tipo:** REPO · **Área:** 06_CONECTORES-MCP
**Hash F0:** `dir · 93 arq. · aninhado`   **Hash reconferido:** `93 arq. · aninhamento 1`   **Confere:** sim
**LV:** LV4
**Cobertura da leitura:** raiz efetiva `Agent-Reach-main/Agent-Reach-main` (18 entradas); `LICENSE` — MIT, 1.067 bytes, "Copyright (c) 2025 Agent Eyes", íntegro; `README.md` (19.368 bytes, em chinês, lidos 6 KB: motivação, tabela de plataformas suportadas, instalação, limites de capacidade); `pyproject.toml` (metadados, `version = "1.5.0"`, dependências e extras); `CHANGELOG.md` (entrada `[1.3.1] - 2026-03-27`); `tests/` — 16 arquivos, nomes listados; sinais `.env.example`, `SECURITY.md`, `test.sh`, `constraints.txt`, `llms.txt`. **Não lidos:** `agent_reach/`, `config/`, `docs/`, `scripts/`.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** não se aplica

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 4 | Artefato completo e inspecionável (CLI Python, canais por plataforma, `config/`, `skills`) **mais** procedimento de verificação declarado: `tests/` com 16 arquivos nomeados por contrato (`test_channel_contracts.py`, `test_probe.py`, `test_doctor.py`, `test_cookie_extract_perms.py`) e um `test.sh` na raiz | — |
| E03 Maturidade | 4 | Versionado com changelog presente (`version = "1.5.0"`, `CHANGELOG.md`) **mais** documentação de instalação e uso (`CONFIGURATION`, `docs/` em quatro idiomas, `llms.txt`) **mais** tratamento de erro visível: comando `doctor` que reporta canal a canal o que funciona e como corrigir, e roteamento com backend alternativo por plataforma | — |
| E05 Manutenção | 3 | Atividade identificável por evidência datada dentro da fonte: `CHANGELOG.md` com `[1.3.1] - 2026-03-27`, descrevendo correção de quebra em uma plataforma específica. **Não alcança 4** pela inconsistência observada: o `pyproject.toml` declara `1.5.0` e a entrada mais recente do changelog é `1.3.1` — as duas versões não se reconciliam com o que foi lido | — |
| E06 Segurança ⚠ | **1** | **Risco ativo declarado pela própria fonte e não confirmado por inspeção de código.** O README declara, como funcionalidade, o roteamento em torno de bloqueios de plataforma — "2026-06 实例：yt-dlp 被 B站风控封死 → 已切换 bili-cli，用户零操作" (o mecanismo de controle de uma plataforma bloqueou a ferramenta; trocou-se o backend, sem ação do usuário) — e o reúso de **estado de login e cookies** de Twitter, Reddit, Facebook, Instagram e Xiaohongshu. A instalação recomendada é colar uma frase com **URL remota para o agente buscar e seguir**. **Contrapesos declarados e registrados**: `SECURITY.md` presente, `.env.example`, modo `--safe` que não instala pacotes de sistema, cookies declaradamente locais, e um teste nomeado `test_cookie_extract_perms.py` | — |
| E07 Licença ⚠ | 4 | Permissiva padrão presente e íntegra: MIT, 1.067 bytes; `license = {text = "MIT"}` no `pyproject.toml`. Cópia local não prova titularidade → teto 4 | — |
| E13 Testes/evals | 3 | `tests/` inspecionado: 16 arquivos com ponto de entrada declarado (`test.sh`, pytest em `dev`), cobrindo contratos de canal, sondagem, diagnóstico e permissões de cookie. Nenhum eval de comportamento de agente | — |
| E15 Alegações ⚠ | 1 | Alegações fortes com fonte citada porém não conferidas: "**完全免费** — 所有工具开源、所有 API 免费" (tudo gratuito), "$1/月" de proxy, badge de "Trending #1 Repository of the Day" e contagem de estrelas. **P-3** aplicado | — |

**NF = 3 · 7/7 · 0 ND** *(mediana de [1,1,3,3,4,4,4] = 3)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 4 | Endereça diretamente a pergunta central — alcançar o mundo externo — **mais** artefato concreto: tabela de 15 plataformas com estado "funciona sem configuração" × "desbloqueia após configurar", e um comando de diagnóstico por canal | — |
| E04 Transferibilidade | 3 | Transferível com adaptação declarada e delimitada: exige permissão de execução de shell no agente, configuração por plataforma e, em vários canais, estado de login do usuário | — |
| E14 Diferencial | 4 | Sem equivalente pronto no acervo **mais** custo alto de reconstrução: é o único item que trata **degradação de canal como problema de engenharia** — cada plataforma tem backend preferencial e alternativo, com troca declarada quando um quebra | — |

**RP = 4 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Runtime já presente e instalação documentada com passos: o processo instala CLI, Node.js, `gh`, `mcporter`, configura busca por MCP, detecta ambiente e registra um arquivo de skill. Extenso demais para as âncoras superiores | — |
| E09 Custo | 4 | Custo marginal declarado: ferramentas abertas e APIs gratuitas, com custo recorrente apenas de proxy em servidor (~US$ 1/mês), explicitamente dispensável em máquina local | — |
| E10 Contexto/tokens | 3 | Medido: **93 arquivos, 826,9 KB**. Tamanho fecharia a âncora 4 (< 1 MB), contagem fecha a âncora 3 (50–300); vale a pior das duas | — |
| E11 Fornecedor | 4 | Abstração de fornecedor documentada e **central ao produto**: cada plataforma tem "首选 + 备选" (preferencial + alternativo), com troca declarada por configuração | — |
| E12 Reversibilidade | 3 | Reversível por remoção, com efeitos colaterais documentados: instala pacotes de sistema, registra arquivo de skill no diretório do agente e armazena estado de login | — |

**AA = 3 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (projeto chinês com traduções em `docs/`, proposta de manter a forma de conexão mais estável do momento, Python 3.10+, MIT) e **todos** os detalhes conferem: o README está em chinês, `docs/` traz traduções, `pyproject.toml` declara `requires-python = ">=3.10"` e a licença é MIT.
**O que o catálogo afirma:** "Projeto chinês (README em chinês, com traduções em `docs/`). A proposta: instalar acesso à internet no agente de uma vez, escolhendo e mantendo a forma de conexão mais estável do momento… Python 3.10+, MIT."
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "2026-06 实例：yt-dlp 被 B站风控封死 → 已切换 bili-cli，用户零操作" | `README.md` da fonte | **FATO DECLARADO PELO AUTOR** sobre o desenho do produto | não verificado por inspeção — **sustenta `E06 = 1`**: o contorno de controle de plataforma é apresentado como funcionalidade |
| "🔒 **隐私安全** \| Cookie 只存在你本地，不上传不外传。" (cookies só existem localmente, não são enviados) | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — `agent_reach/` não lido; existe um teste nomeado sobre permissões de cookie, não lido |
| "💰 **完全免费** \| 所有工具开源、所有 API 免费。" (tudo gratuito) | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "帮我安装 Agent Reach：https://raw.githubusercontent.com/…/install.md" | `README.md` da fonte | **FATO OBSERVADO** — método de instalação por instrução remota | registrado como achado de cadeia de suprimentos: o agente é instruído a **buscar e seguir** um documento remoto (`05` §7.1: conteúdo externo é dado, nunca instrução) |
| Inconsistência `version = "1.5.0"` × `CHANGELOG [1.3.1]` | `pyproject.toml` e `CHANGELOG.md` da fonte | **FATO OBSERVADO** | inconsistência interna confirmada |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V4 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` (declarado, **não confirmado por inspeção de código**) · `E07 = 4` · `LV = 4` · 0 ND · `E15 = 1` (≠ 0) · reconferência confere |
| **V2** | **sim** | `E06 = 1` → teto PADRÃO A ESTUDAR / REFERÊNCIA / EXIGE PESQUISA |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** V2 (§8) fecha as duas classificações de candidato; §9, condição de entrada de EXIGE PESQUISA.
**Se EXIGE PESQUISA — lacuna nomeada:** três, todas endereçáveis: (1) a **consequência jurídica e contratual** de contornar o controle de acesso de plataformas de terceiros e reutilizar estado de login; (2) o que exatamente o documento remoto de instalação manda o agente executar; (3) a inconsistência de versão entre manifesto e changelog.  **Verificação que a fecharia:** ler `docs/install.md` e `agent_reach/` para enumerar comandos executados e dados armazenados; e submeter a questão de termos de serviço a avaliação jurídica **antes** de qualquer piloto — esta frente não a resolve.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-06-REP-003 — `context7-master`

**Tipo:** REPO · **Área:** 06_CONECTORES-MCP
**Hash F0:** `dir · 375 arq. · aninhado`   **Hash reconferido:** `375 arq. · aninhamento 1`   **Confere:** sim
**LV:** LV4
**Cobertura da leitura:** raiz efetiva `context7-master/context7-master` (25 entradas); `LICENSE` — MIT, 1.079 bytes, "Copyright (c) 2021 Upstash, Inc.", íntegro; `README.md` (9.887 bytes, lidos 6 KB: problema declarado, dois modos de operação, instalação, remoção, dicas de uso, ferramentas expostas); `package.json` (monorepo, scripts, licença); `server.json`; `.changeset/`; **busca por diretório de teste na raiz efetiva — ausente**; sinais `SECURITY.md`, `.env.example`, `gemini-extension.json`. **Não lidos:** `packages/`, `plugins/`, `skills/`, `rules/`, `docs/`.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** não se aplica

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 4 | Artefato completo e inspecionável (monorepo com SDK, servidor MCP, CLI, skills, regras, `server.json`) **mais** procedimento de verificação declarado: `"test": "pnpm -r run test"`, `typecheck`, `lint:check` e `format:check` em `package.json`, mais fluxo de release por changesets | — |
| E03 Maturidade | 4 | Versionado com release identificável (pacotes publicados em npm com badge de versão, `.changeset/` como processo declarado, `release` e `release:snapshot` em scripts) **mais** documentação de instalação e uso (setup em um comando, modo manual, clientes alternativos) **mais** tratamento de erro visível: caminho de **remoção** documentado (`npx ctx7 remove`, mais desinstalação global separada) | — |
| E05 Manutenção | ND | — | Nenhuma data observada no material lido; o diretório `.changeset/` existe mas não foi enumerado. Resolveria listar `.changeset/` ou consultar as releases dos pacotes publicados |
| E06 Segurança ⚠ | 3 | Superfície declarada (servidor MCP **remoto** em `mcp.context7.com`, chave de API por cabeçalho, CLI que escreve configuração no agente, skill instalada automaticamente) **com controles parciais documentados**: `SECURITY.md`, `.env.example`, autenticação por OAuth com geração de chave, e caminho de remoção explícito. **Não alcança 4**: nenhum escopo de permissão nem política de retenção do serviço remoto foi lido | — |
| E07 Licença ⚠ | 4 | Permissiva padrão presente e íntegra: MIT, 1.079 bytes, titular corporativo nomeado; `"license": "MIT"` no `package.json`. Cópia local não prova titularidade → teto 4 | — |
| E13 Testes/evals | ND | — | **Procurado na listagem da raiz efetiva: não há diretório de teste no topo.** O script `test` delega a cada pacote (`pnpm -r run test`), o que sugere suítes em `packages/*`. Resolveria listar `packages/*/test` — leitura adicional que estoura o teto de `05` §8 |
| E15 Alegações ⚠ | 1 | Alegações funcionais fortes com fonte citada implicitamente porém **não conferidas**: "no **hallucinated APIs** that don't exist", "up-to-date, **version-specific** documentation… straight from the source". São exatamente as afirmações que exigiriam eval, e nenhum foi lido | — |

**NF = 4 · 5/7 · 2 ND** *(mediana dos determinados [1,3,4,4,4] = 4)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 4 | Endereça diretamente a pergunta central — trazer informação externa para dentro do contexto — **mais** artefato concreto: duas ferramentas MCP nomeadas com contrato (`resolve-library-id`, e a recuperação por identificador de biblioteca e versão) | — |
| E04 Transferibilidade | 4 | Transferível por configuração, sem alteração de código: `npx ctx7 setup` com alvo por agente, ou registro manual do endereço do servidor MCP em qualquer cliente | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto **dentro do acervo**: recuperação de documentação **por versão** no momento da geração. Nenhum outro item ataca a defasagem de documentação como problema de conector | — |

**RP = 4 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 4 | Instalação declarada em um comando (`npx ctx7 setup`), com autenticação e escolha de modo; configuração manual documentada como alternativa | — |
| E09 Custo | 3 | Custo variável por uso, com limite ou controle possível: o README declara chave de API **gratuita** com "higher rate limits" — ou seja, há limite de taxa no uso sem chave, e o serviço é hospedado por terceiro | — |
| E10 Contexto/tokens | 2 | Medido: **375 arquivos, 19,3 MB** — contagem na faixa 300–1.000 e tamanho na faixa 5–20 MB | — |
| E11 Fornecedor | 2 | **Fornecedor único, porém com formato de dados aberto**: o valor depende do índice hospedado em `context7.com`; o transporte é MCP, padrão aberto, e a saída é texto de documentação | — |
| E12 Reversibilidade | 5 | Reversível por remoção, sem efeito residual, **e a reversão está documentada pelo próprio autor**: "To remove the generated setup later, run `npx ctx7 remove`", com a ressalva explícita de desinstalar o pacote global separadamente | — |

**AA = 3 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (o problema atacado — documentação desatualizada e API alucinada — e o mecanismo de injetar documentação da versão correta no prompt) e o detalhe **confere** quase literalmente com a seção "❌ Without Context7 / ✅ With Context7" do README.
**O que o catálogo afirma:** "Resolve um problema específico e caro: o modelo trabalha com documentação de biblioteca desatualizada, gera exemplo velho e **alucina API que não existe**. O Context7 puxa documentação da versão correta direto da fonte e injeta no prompt. **O que extrair:** é a peça que mais reduz erro em código gerado. Considere obrigatório em qualquer sistema que escreva código."
**Confere com a fonte:** sim quanto à descrição

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "no tab-switching, **no hallucinated APIs that don't exist**, no outdated code generation" | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA`; nenhum eval foi lido |
| "**Considere obrigatório** em qualquer sistema que escreva código." | `_CONTEUDO.md` área 06 | ALEGAÇÃO DO CATÁLOGO + `DECISÃO DE ESCOPO DE TERCEIRO` — prescreve obrigatoriedade | **instrução não obedecida** (`04` §14.5): nenhum item é obrigatório por decisão do catálogo |
| "é a peça que **mais reduz erro** em código gerado" | `_CONTEUDO.md` área 06 | ALEGAÇÃO DO CATÁLOGO | não — `NÃO VERIFICADA`, comparação sem medida |
| "**API Key Recommended**: Get a free API key… for higher rate limits." | `README.md` da fonte | ALEGAÇÃO DO AUTOR | **fato observado no README** — sustenta `E09 = 3` |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V2 · V3 · V4 · V5 · V6 · V7 · V8 | **nenhuma** | `E06 = 3` · `E07 = 4` · `LV = 4` · 2 ND (no limite) · `E15 = 1` (≠ 0) · reconferência confere |

#### Resultado
**RF = CANDIDATO A PILOTO**
**Regra que produziu:** §9. **Não** alcança CANDIDATO FORTE: `E15 = 1` está abaixo de 3 no Bloco A. Satisfaz CANDIDATO A PILOTO: `LV ≥ 3` · `E06 = 3 ≥ 3` · `E07 = 4 ≥ 3` · `RP = 4 ≥ 3` · **2 ND** ≤ 4 · nenhum eixo do Bloco C em 0.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> **CANDIDATO A PILOTO não significa pilotar.** Restrições registradas na própria ficha: `E11 = 2` (o valor depende de um índice hospedado por terceiro), `E13 = ND` (suíte não localizada sob o teto de leitura) e `E15 = 1` (a alegação central — eliminar API alucinada — não tem eval).

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-06-REP-004 — `last30days-skill-main`

**Tipo:** REPO · **Área:** 06_CONECTORES-MCP
**Hash F0:** `dir · 153 arq. · aninhado`   **Hash reconferido:** `153 arq. · aninhamento 1`   **Confere:** sim
**LV:** LV4
**Cobertura da leitura:** raiz efetiva `last30days-skill-main/last30days-skill-main` (18 entradas); `LICENSE` — MIT, 1.070 bytes, "Copyright (c) 2026 Matt Van Horn", íntegro; `README.md` (32.062 bytes, lidos 6 KB: proposta, instalação em dois caminhos, tabela de fontes por plataforma); `pyproject.toml` **integral** (versão, pytest, configuração de cobertura com portão e justificativa); `.claude-plugin/`; **busca por diretório de teste na raiz efetiva — ausente**; sinais `hooks/`, `mcp/`, `skills/`, `CONFIGURATION.md`, `CONCEPTS.md`, `.skillignore`. **Não lidos:** `skills/`, `mcp/`, `hooks/`.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** não se aplica

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 4 | Artefato completo e inspecionável (skill com especificação de runtime declarada como fonte da verdade, servidor MCP, hooks, plugins para quatro harnesses) **mais** procedimento de verificação declarado **e quantificado** no próprio manifesto: `fail_under = 84` com a regra escrita "Do not lower without documenting why in the PR" | — |
| E03 Maturidade | 4 | Versionado com release identificável (`version = "3.14.0"`) **mais** documentação de instalação e uso (marketplace, CLI multiagente, `CONFIGURATION.md`, `CONCEPTS.md`) **mais** tratamento de erro visível na configuração (`.skillignore`, assistente de configuração de primeira execução, ativação automática condicionada à presença de binário no `PATH`) | — |
| E05 Manutenção | 4 | Atividade recente por evidência datada **dentro da fonte**: o comentário do portão de cobertura registra "Baseline measured **2026-07-03** on main before feat/hosted-api-mode" — 26 dias antes desta avaliação — e referencia uma issue numerada **mais** responsável nomeado (no `LICENSE`) **mais** canal de reporte declarado (repositório e regra de PR citada em `AGENTS.md`) | — |
| E06 Segurança ⚠ | 2 | **Superfície ampla sem controle documentado na raiz efetiva.** O produto declara operar sobre "your own keys **and browser sessions**" para plataformas que exigem autenticação (X, TikTok, Instagram, LinkedIn, Xiaohongshu, Threads, Pinterest), instala binários auxiliares detectados no `PATH` e traz `hooks/` e `mcp/`. **Procurado e não encontrado**: `SECURITY.md`, política de retenção de sessão, escopo de permissão | — |
| E07 Licença ⚠ | 4 | Permissiva padrão presente e íntegra: MIT, 1.070 bytes, titular nomeado. Cópia local não prova titularidade → teto 4 | — |
| E13 Testes/evals | 2 | Testes existem — o portão de cobertura de 84% com baseline datado é evidência de que há suíte — **mas não são executáveis isoladamente a partir do que foi lido**: `testpaths = ["tests"]` aponta para um diretório que **não aparece na listagem da raiz efetiva**. Mesma inconsistência observada em `AC-05-REP-004` | — |
| E15 Alegações ⚠ | 1 | Alegações numéricas fortes com fonte citada porém **não conferidas e não conferíveis** com o material disponível: "shipping **23 PRs at 85% merge rate**", "r/ClaudeCode hit **569 upvotes**", "the creator reaching **3.6M people**", "**825 points, 899 comments**", mais badges de "Trending #1". **P-3** aplicado | — |

**NF = 4 · 7/7 · 0 ND** *(mediana de [1,2,2,4,4,4,4] = 4)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 4 | Endereça diretamente a pergunta central **mais** artefato concreto: 16 fontes com critério de pontuação declarado por fonte, busca em paralelo e síntese por agente julgador | — |
| E04 Transferibilidade | 4 | Transferível por configuração: instalação por marketplace ou CLI multiagente, com escopo global ou por projeto declarado | — |
| E14 Diferencial | 4 | Sem equivalente pronto no acervo **mais** custo alto de reconstrução: a tese operacional — **pontuar por engajamento medido em vez de por curadoria editorial**, com fontes heterogêneas normalizadas — não aparece em nenhum outro item | — |

**RP = 4 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 4 | Instalação declarada em um comando (`/plugin install last30days` ou `npx skills add … -g`), com assistente de configuração e quatro fontes funcionando sem configuração | — |
| E09 Custo | 3 | Custo variável por uso, com controle possível: quatro fontes declaradas sem chave, e o restante exige "your own keys" — parte delas de APIs pagas, fora do controle do artefato | — |
| E10 Contexto/tokens | 2 | Medido: **153 arquivos, 13,1 MB**. Contagem fecharia a âncora 3 (50–300), tamanho fecha a âncora 2 (5–20 MB); vale a pior das duas | — |
| E11 Fornecedor | 4 | Abstração de fornecedor documentada: mais de 50 hosts de skill declarados, quatro plugins de harness no repositório, e ativação por fonte condicionada a binário presente | — |
| E12 Reversibilidade | 4 | Reversível por remoção, sem efeito residual no projeto: a skill é arquivo de instrução mais scripts; o estado externo (chaves, sessões) fica fora do artefato | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (buscador conduzido por agente, pontuação por upvotes, curtidas e dinheiro real em vez de editor, e a localização exata da especificação de runtime) e o detalhe **confere**: o README declara literalmente que "The runtime skill spec lives in `skills/last30days/SKILL.md`, which is the source of truth".
**O que o catálogo afirma:** "Buscador conduzido por agente, pontuado por upvotes, curtidas e dinheiro real — não por editor. A especificação de runtime está em `skills/last30days/SKILL.md`."
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "shipping 23 PRs at 85% merge rate… r/ClaudeCode hit 569 upvotes" | `README.md` da fonte (exemplo de saída) | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA`; **P-3** |
| "You can't get this search anywhere else because no single AI has access to all of it." | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "you can bring your own keys and **browser sessions**, and suddenly an AI agent can search all of them at once" | `README.md` da fonte | **FATO DECLARADO** sobre o desenho | sustenta `E06 = 2`: reúso de sessão autenticada em plataformas que a restringem |
| "Coverage gate (issue #254). Floor intended to rise over time, not a ceiling. Baseline measured 2026-07-03… Do not lower without documenting why in the PR" | `pyproject.toml` da fonte | **FATO OBSERVADO** | é a evidência datada que sustenta `E05 = 4` — e o único portão de qualidade **quantificado** encontrado no acervo inteiro |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V2 · V3 · V4 · V5 · V6 · V7 · V8 | **nenhuma** | `E06 = 2` (≠ 0 e ≠ ND) · `E07 = 4` · `LV = 4` · 0 ND · `E15 = 1` (≠ 0) · reconferência confere |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** §9 — as duas classificações de candidato exigem `E06 ≥ 3`, e aqui `E06 = 2`; PADRÃO A ESTUDAR exige `E03`, `E05` ou `E08` baixos ou ND, e os três estão em 4. Resta EXIGE PESQUISA, com lacuna nomeada.
**Se EXIGE PESQUISA — lacuna nomeada:** duas: (1) o **reúso de sessão autenticada** em plataformas cujos termos costumam proibi-lo, sem `SECURITY.md` nem política de retenção declarada; (2) o diretório `tests/` declarado em `pyproject.toml` e ausente da raiz efetiva, apesar do portão de cobertura de 84%.  **Verificação que a fecharia:** ler `skills/last30days/SKILL.md` e `mcp/` para enumerar o que é lido, armazenado e enviado por fonte; localizar a suíte de testes; e submeter a questão de termos de serviço a avaliação jurídica antes de qualquer piloto.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

> **Cobertura padrão dos 13 PRINT desta área:** inspeção visual do original pela trilha Codex (`107`, lote 08, `H-P1-002`), com a descrição do `_CONTEUDO.md` confrontada contra os pixels. Esta frente **não** abriu as imagens — ver DEF-06. `AC-06-PRT-007` a `AC-06-PRT-012` formam o carrossel `mcp0`–`mcp5`, **série completa de 6 slides**, avaliados individualmente por `05` §2.2.

### AC-06-PRT-001 — `Captura de tela 2026-07-28 154159.png`

**Tipo:** PRINT · **Área:** 06_CONECTORES-MCP
**Hash F0:** `73EB85F00A07C3F3`   **Hash reconferido:** `73EB85F00A07C3F3`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`107`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-06-PRT-001 · `H-P1-002` (relatório `107`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só listagem: matriz de dez tarefas com três candidatos cada, **sem preço, integração, segurança nem critério de seleção** — ausência que o próprio catálogo registra (`107`, CONFIRMADA) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e sua data |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial ou instrução ao leitor |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhum critério de comparação exibido |
| E15 Alegações ⚠ | 1 | Alegações de adequação por tarefa, com nomes citados porém não conferidos; `107` registra a grafia observada "NanoBanana 2" | — |

**NF = 1 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça a pergunta de forma genérica: lista candidatos por capacidade sem tratar de integração ou autoridade | — |
| E04 Transferibilidade | 1 | Só a ideia viaja; a seleção é datada e sem critério | — |
| E14 Diferencial | 1 | Conveniência sobre inventário já acessível; sobrepõe `AC-01-PRT-004` e `AC-06-PRT-005` | — |

**RP = 1 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 953,6 KB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `107` + parágrafo do `_CONTEUDO.md`; < 1 MB | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (as dez tarefas com três candidatos cada, nomeados) conferido contra os pixels; CONFIRMADA em `107`. O catálogo acerta ao registrar a ausência de preço, integração, segurança e critério.
**O que o catálogo afirma:** "Matriz de dez tarefas com três opções cada… **O que extrair:** lista de candidatos por capacidade. Não traz preço, integração, segurança nem critério de seleção."
**Confere com a fonte:** sim — CONFIRMADA em `107`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "30 ferramentas para empresários" | print (título observado, via `107`) | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "o print escreve “NanoBanana 2”" | `107` (texto observado) | FATO OBSERVADO | grafia preservada, não normalizada |

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

### AC-06-PRT-002 — `Captura de tela 2026-07-28 160157.png`

**Tipo:** PRINT · **Área:** 06_CONECTORES-MCP
**Hash F0:** `3EBD11C0D9EC87C8`   **Hash reconferido:** `3EBD11C0D9EC87C8`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`107`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-06-PRT-002 · `H-P1-002` (relatório `107`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Seis **cadeias de produção** exibidas em tela, organizadas por saída em vez de por ferramenta — o que é mais que uma lista, embora nenhum artefato acompanhe (`107`, CONFIRMADA) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e sua data |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial ou instrução ao leitor |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhum artefato testável associado |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas (qual ferramenta em qual etapa); nenhum número decisivo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: mostra **composição** de conectores em cadeia por tipo de entrega, não ferramentas isoladas | — |
| E04 Transferibilidade | 2 | O **padrão** (organizar por saída) transfere; as cadeias são do contexto do autor | — |
| E14 Diferencial | 2 | Agregação; a composição em cadeia reaparece em `AC-06-VID-014` | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 1,2 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `107` + parágrafo do `_CONTEUDO.md` | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (as seis cadeias e suas ferramentas) conferido; CONFIRMADA em `107`.
**O que o catálogo afirma:** "Organiza por saída: páginas de vendas/apps…; conteúdo…; vídeos “zero a zero”…; slides…; edição de aulas e reels…; ensaios fotográficos… **O que extrair:** revela cadeias de produção, não só ferramentas isoladas."
**Confere com a fonte:** sim — CONFIRMADA em `107`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Magnific aparece em vídeo e fotografia; Claude atravessa quase todas as etapas." | `_CONTEUDO.md` área 06 | ALEGAÇÃO DO CATÁLOGO | **conferida contra os pixels** por `107` |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 3` · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-06-PRT-003 — `Captura de tela 2026-07-28 160340.png`

**Tipo:** PRINT · **Área:** 06_CONECTORES-MCP
**Hash F0:** `7A7372E11146E56C`   **Hash reconferido:** `7A7372E11146E56C`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`107`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-06-PRT-003 · `H-P1-002` (relatório `107`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só índice: página de links por categoria, com endereços **encurtados**; `107` registra que "a captura **não valida os destinos**" | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e sua data |
| E05 Manutenção | ND | — | Localizar o canal de origem com data — um índice de links envelhece rápido |
| E06 Segurança ⚠ | ND | — | **Superfície retratada e não inspecionada**: links encurtados escondem o destino. Resolveria resolver cada endereço antes de qualquer acesso |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhum artefato testável associado |
| E15 Alegações ⚠ | 1 | Alegações de existência e utilidade de dezenas de recursos, com fonte citada (os links) porém **não conferidas** — e não conferíveis a partir da imagem, por serem encurtados | — |

**NF = 1 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça a pergunta de forma genérica: é lista de fontes a consolidar, não mecanismo de alcance | — |
| E04 Transferibilidade | 1 | Só a ideia viaja; os links não foram resolvidos | — |
| E14 Diferencial | 1 | Conveniência sobre índice já acessível | — |

**RP = 1 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 1,4 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `107` + parágrafo do `_CONTEUDO.md` | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (as categorias de link) conferido; CONFIRMADA em `107`. O catálogo registra corretamente que "muitos endereços são links encurtados e não foram verificados; a captura é índice, não conteúdo".
**O que o catálogo afirma:** "Página com links para documentação oficial, diretórios, MCP servers, skills, multiplexers, frameworks de agente, automação, artigos, certificado, lista de MCP, banco, controle de navegador, desenvolvimento paralelo e ferramentas CLI."
**Confere com a fonte:** sim — CONFIRMADA em `107`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "a captura não valida os destinos" | `107` (ressalva da trilha Codex) | FATO OBSERVADO sobre a cobertura | — sustenta `E06 = ND` e `E15 = 1` |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4. Resolver dezenas de links encurtados não é verificação de um artefato nomeado, e sim navegação — fora do escopo desta frente.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-06-PRT-004 — `conectores essenciais.png`

**Tipo:** PRINT · **Área:** 06_CONECTORES-MCP
**Hash F0:** `2645BF023BC646AE`   **Hash reconferido:** `2645BF023BC646AE`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`107`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-06-PRT-004 · `H-P1-002` (relatório `107`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Oito conectores exibidos **com caso de uso concreto por conector** — o que é mais informativo que uma lista de nomes: agrupar e-mails em três destinos, achar 30 minutos livres, destacar as três coisas que exigem reação. Exemplo isolado, sem configuração (`107`, CONFIRMADA) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e sua data |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | **Superfície retratada e não inspecionada, de alta sensibilidade**: e-mail, calendário, arquivos e mensagens corporativas. Resolveria inspecionar o escopo de permissão de cada conector |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhum artefato testável associado |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas (o que cada conector faria); nenhum número decisivo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: mostra **o que se pede a cada conector**, que é a parte reutilizável — e não apenas que o conector existe | — |
| E04 Transferibilidade | 3 | Os oito padrões de pedido transferem com adaptação declarada | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto no acervo: é o único item que associa **um prompt operacional a cada conector**, e não uma lista de nomes | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 1,9 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `107` + parágrafo do `_CONTEUDO.md` | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (os oito conectores com seus casos de uso) conferido; CONFIRMADA em `107`.
**O que o catálogo afirma:** "os 8 que Ruben Hassid usa toda semana… **O que extrair:** o padrão de prompt associado a cada conector. Isso é insumo direto para desenhar as rotinas do sistema."
**Confere com a fonte:** sim — CONFIRMADA em `107`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| Atribuição nominal de uso semanal a uma pessoa | `_CONTEUDO.md` área 06 / print | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "não para terceirizar meu pensamento, para ter mais ideias" | print (texto observado, via `107`) | ALEGAÇÃO DO AUTOR | não |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 3` · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-06-PRT-005 — `ferramentas.png`

**Tipo:** PRINT · **Área:** 06_CONECTORES-MCP
**Hash F0:** `FF02C789343A14B5`   **Hash reconferido:** `FF02C789343A14B5`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`107`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-06-PRT-005 · `H-P1-002` (relatório `107`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só listagem: onze combinações de ferramenta com promessa associada, sem demonstração, medição ou artefato (`107`, CONFIRMADA "como texto visível") | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e sua data |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial ou instrução ao leitor |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhum artefato testável associado |
| E15 Alegações ⚠ | 1 | Alegações de aceleração com nomes citados porém **não conferidas**; `107` registra que "as onze combinações **e promessas** conferem **como texto visível**" — ou seja, confere que foram ditas, não que sejam verdadeiras | — |

**NF = 1 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central por um ângulo útil: cada linha é um **"não construa isso"** — decisão de plugar em vez de construir | — |
| E04 Transferibilidade | 2 | O **padrão** (decidir construir × plugar por capacidade) transfere; a seleção é datada | — |
| E14 Diferencial | 2 | Agregação de material público; sobrepõe `AC-06-PRT-001` e `AC-06-VID-014` | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 3,2 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `107` + parágrafo do `_CONTEUDO.md` | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (as onze combinações, nomeadas) conferido; CONFIRMADA em `107`.
**O que o catálogo afirma:** "11 formas de acelerar uma empresa com IA (em português)… **O que extrair:** ajuda a decidir o que construir versus o que plugar. Cada linha é um “não construa isso”."
**Confere com a fonte:** sim — CONFIRMADA em `107`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "11 formas de acelerar uma empresa com IA" | print (título observado, via `107`) | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-06-PRT-006 — `ferramente de voz.png`

**Tipo:** PRINT · **Área:** 06_CONECTORES-MCP
**Hash F0:** `52FB83F636338C56`   **Hash reconferido:** `52FB83F636338C56`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`107`). Grafia do nome preservada como está no disco.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-06-PRT-006 · `H-P1-002` (relatório `107`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Captura de um README com badges e **um gráfico de avaliação declaradamente subjetiva**, comparando cinco sistemas. Exemplo isolado: o gráfico está na imagem, o método não (`107`, CONFIRMADA) | — |
| E03 Maturidade | ND | — | Localizar o repositório retratado e inspecionar versão e estabilidade |
| E05 Manutenção | ND | — | Verificar atividade datada no repositório de origem |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem; e, separadamente, inspeção do repositório retratado — clonagem de voz é superfície de risco própria |
| E07 Licença ⚠ | ND | — | **A aba MIT aparece no print**, mas `107` adverte que a captura "não prova… licença efetiva do artefato". Resolveria ler o `LICENSE` no repositório de origem |
| E13 Testes/evals | ND | — | O gráfico é avaliação subjetiva declarada, não eval reprodutível |
| E15 Alegações ⚠ | 0 | A proposta do item **depende** de uma alegação forte **sem fonte**, e o próprio catálogo a isola: "a afirmação de que substitui o ElevenLabs vem da **legenda de um post**, não do benchmark". Os números do gráfico (3,75 · 3,71 · 3,81) são de preferência subjetiva | — |

**NF = 1 · 2/7 · 5 ND** *(mediana de [0,2] = 1)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: propõe uma camada de voz **auto-hospedável**, alternativa a serviço externo — decisão de fronteira | — |
| E04 Transferibilidade | 2 | O **padrão** (internalizar a camada de voz) transfere; o produto não foi identificado nem inspecionado | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto no acervo: é o único item que apresenta alternativa auto-hospedada para voz | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente para consultar; PNG local de 1 MB. *O custo do produto retratado não é pontuado aqui* (§3.3 do índice) | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `107` + parágrafo do `_CONTEUDO.md` | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (README do repositório, badges de TTS/ASR, aba MIT, os três números do gráfico e os cinco sistemas comparados) conferido; CONFIRMADA em `107`. O catálogo acerta ao separar a legenda promocional do gráfico.
**O que o catálogo afirma:** "README do repositório do VibeVoice (licença MIT). Gráfico de avaliação subjetiva com **VibeVoice-7B liderando**… A legenda do post afirma: “a Microsoft acabou de lançar uma ferramenta que substitui ElevenLabs e HiggsAudio, 100% grátis”. **Verifique antes de decidir.**"
**Confere com a fonte:** sim — CONFIRMADA em `107`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "a Microsoft acabou de lançar uma ferramenta que substitui ElevenLabs e HiggsAudio, 100% grátis" | legenda do post, capturada no print | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA`; sustenta `E15 = 0`. Atribuição de autoria a uma empresa **não conferida** |
| Notas 3,75 / 3,71 / 3,81 em preferência, realismo e riqueza | print (texto observado, via `107`) | ALEGAÇÃO DO AUTOR | não — avaliação **declaradamente subjetiva** |
| "Não prova substituição, gratuidade ou licença efetiva do artefato." | `107` (ressalva da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | — |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |
| **V7** | **sim** | `E15 = 0` e a proposta depende da alegação de substituição → teto EXIGE PESQUISA |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** V7 (§8) — teto EXIGE PESQUISA.
**Se EXIGE PESQUISA — lacuna nomeada:** identidade, autoria, licença efetiva e desempenho medido do produto retratado — nenhum dos quatro é observável na imagem, e a alegação de substituição vem de legenda de post.  **Verificação que a fecharia:** localizar o repositório na origem pública, ler o `LICENSE` e a metodologia do gráfico; e, para a camada de voz, um teste comparativo próprio com amostras desta casa — **sem clonar voz de ninguém sem autorização**.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-06-PRT-007 — `mcp0.png` *(série 1/6 — os cinco universais)*

**Tipo:** PRINT · **Área:** 06_CONECTORES-MCP · **Série:** `mcp0`–`mcp5`, 6 slides
**Hash F0:** `D09356FEB962324D`   **Hash reconferido:** `D09356FEB962324D`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`107`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-06-PRT-007 · `H-P1-002` (relatório `107`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Cinco conectores exibidos **com função declarada por conector** (código, documentação viva, navegador, arquivos, busca). Exemplo isolado, sem configuração nem escopo (`107`, CONFIRMADA) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e sua data |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | **Superfície retratada e não inspecionada, ampla**: acesso a repositório, sistema de arquivos "além da pasta atual", navegador e busca web. Resolveria ler o manifesto de permissões de cada servidor |
| E07 Licença ⚠ | ND | — | Ler a licença de cada servidor citado na origem |
| E13 Testes/evals | ND | — | Nenhum artefato testável associado |
| E15 Alegações ⚠ | 1 | Alegação forte com fonte citada porém não conferida: o slide instrui **"Install first"**, o que `107` registra como "recomendação do slide, **não autorização**" | — |

**NF = 1 · 2/7 · 5 ND** *(mediana de [1,2] = 1,5 → §14.3 vale o inferior)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: define um **conjunto mínimo** de fronteiras externas, em vez de um catálogo | — |
| E04 Transferibilidade | 2 | O **padrão** (começar por poucos conectores de função distinta) transfere; os produtos são datados | — |
| E14 Diferencial | 2 | Agregação; é a capa da série, cujo conteúdo operacional está nos slides seguintes | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 1,2 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `107` + item do `_CONTEUDO.md` | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (os cinco conectores com suas funções) conferido; CONFIRMADA em `107`.
**O que o catálogo afirma:** "**GitHub** (PRs, issues, busca de código) · **Context7** (documentação viva, evita API alucinada) · **Playwright** (navegador controlável) · **Filesystem** (arquivos além da pasta atual) · **Brave Search** (busca web)."
**Confere com a fonte:** sim — CONFIRMADA em `107`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Install first" | print (texto observado, via `107`) | ALEGAÇÃO DO AUTOR + `DECISÃO DE ESCOPO DE TERCEIRO` | **não obedecida**; `107`: "recomendação do slide, não autorização" |
| "Context7… evita API alucinada" | `_CONTEUDO.md` área 06 | ALEGAÇÃO DO CATÁLOGO | não — a mesma alegação está registrada e **não verificada** em `AC-06-REP-003` |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4. Um dos cinco conectores citados **está no acervo** com ficha própria e licença lida (`AC-06-REP-003`).
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> **Nota de conjunto da série `mcp0`–`mcp5` (não substitui as fichas):** os seis slides estão presentes e íntegros, e organizam conectores por **perfil de usuário** — universal, desenvolvedor, empresa, criador, finanças, mercados. A frase operativa da série, capturada no slide 2, é *"This is a menu. Not a shopping spree."*

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-06-PRT-008 — `mcp1.png` *(série 2/6 — desenvolvedores)*

**Tipo:** PRINT · **Área:** 06_CONECTORES-MCP · **Série:** `mcp0`–`mcp5`
**Hash F0:** `97CBA09DC37D8F23`   **Hash reconferido:** `97CBA09DC37D8F23`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`107`), com conferência dos nomes de produto.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-06-PRT-008 · `H-P1-002` (relatório `107`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Conectores por função **mais um encadeamento concreto**: detectar erro em produção → sugerir correção → abrir a proposta de mudança, em um passo. Exemplo isolado, sem execução (`107`, PARCIAL) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e sua data |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | **Superfície retratada e não inspecionada, crítica**: acesso a banco de dados de produção, log de erro e cluster. Resolveria ler o escopo de permissão de cada servidor |
| E07 Licença ⚠ | ND | — | Ler a licença de cada servidor citado |
| E13 Testes/evals | ND | — | Nenhum artefato testável associado |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas (o que cada conector faz); nenhum número decisivo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central **e traz a regra mais útil da série**: *"This is a menu. Not a shopping spree."* — instalar por combinação útil, não por volume | — |
| E04 Transferibilidade | 3 | O princípio de combinação transfere com adaptação declarada | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto no acervo: é o único ponto do material que exibe **um encadeamento de conectores com resultado único**, em vez de uma lista | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 1,6 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `107` + item do `_CONTEUDO.md` | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 2** — **PARCIAL** em `107`: funções e a regra "menu, not a shopping spree" conferem, mas o catálogo **normaliza um nome de produto sem evidência no print** — a imagem escreve `Postgres / Supabase / **Neo**`, e o catálogo grafa "**Neon**". Correção 5 de `107`: preservar "Neo [texto visível; identidade a verificar]". Teto 2 (§14.4).
**O que o catálogo afirma:** "Postgres/Supabase/**Neon** (explorar banco e schema sem SQL manual) · Sentry… · Docker Hub · Kubernetes… · Brave Search."
**Confere com a fonte:** parcialmente

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "This is a menu. Not a shopping spree." | print (texto observado, via `107`) | ALEGAÇÃO DO AUTOR | não — mas é a única regra de contenção declarada na série |
| "Neon" | `_CONTEUDO.md` área 06 | ALEGAÇÃO DO CATÁLOGO | **normalização não observável no print** → sustenta `NC = 2` |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 3` · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-06-PRT-009 — `mcp2.png` *(série 3/6 — times e empresas)*

**Tipo:** PRINT · **Área:** 06_CONECTORES-MCP · **Série:** `mcp0`–`mcp5`
**Hash F0:** `1CA42A848658AFDB`   **Hash reconferido:** `1CA42A848658AFDB`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`107`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-06-PRT-009 · `H-P1-002` (relatório `107`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Seis conectores corporativos exibidos com função, **e um controle explícito**: aprovação humana no envio. Exemplo isolado, sem implementação do controle (`107`, CONFIRMADA) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e sua data |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | O slide **declara** o controle mais importante da área — humano no loop para escrita externa — mas nenhuma implementação foi inspecionada. Resolveria ler o escopo de cada servidor e verificar se a aprovação é imposta ou opcional |
| E07 Licença ⚠ | ND | — | Ler a licença de cada servidor citado |
| E13 Testes/evals | ND | — | Nenhum teste do portão de aprovação |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas; nenhum número decisivo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central **no ponto certo**: distingue leitura de escrita externa e nomeia o portão humano | — |
| E04 Transferibilidade | 3 | O princípio (aprovação humana antes de efeito externo) transfere com adaptação declarada e independe de produto | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto no acervo: é o **primeiro** item da área em que o controle aparece explicitamente ligado à operação de escrita | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 1,1 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `107` + item do `_CONTEUDO.md` | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (os seis conectores e a regra de aprovação humana no envio) conferido; CONFIRMADA em `107`.
**O que o catálogo afirma:** "Slack… · Linear… · Notion… · Jira/Confluence via Atlassian Rovo · Google Calendar · Gmail — **com aprovação humana no envio**. **O que extrair:** o padrão humano-no-loop aparece explicitamente para ação de escrita externa."
**Confere com a fonte:** sim — CONFIRMADA em `107`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "com aprovação humana no envio" | print (texto observado, via `107`) | ALEGAÇÃO DO AUTOR | não — controle **declarado**, não verificado |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 3` · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-06-PRT-010 — `mcp3.png` *(série 4/6 — criadores de conteúdo)*

**Tipo:** PRINT · **Área:** 06_CONECTORES-MCP · **Série:** `mcp0`–`mcp5`
**Hash F0:** `74E8A0946CAB7085`   **Hash reconferido:** `74E8A0946CAB7085`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`107`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-06-PRT-010 · `H-P1-002` (relatório `107`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Cinco conectores de produção criativa exibidos com função; `107` registra que os **números promocionais também conferem como texto visível** — isto é, estão na imagem, não verificados | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e sua data |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | **Superfície retratada e não inspecionada**: clonagem de voz e acesso a projeto de design. Resolveria ler o escopo de cada servidor |
| E07 Licença ⚠ | ND | — | Ler a licença e os termos de cada serviço citado — clonagem de voz tem restrição própria |
| E13 Testes/evals | ND | — | Nenhum artefato testável associado |
| E15 Alegações ⚠ | 1 | Alegações numéricas com fonte citada porém não conferidas: "hub com **30+ modelos**", "free tier de **10 mil créditos/mês**" | — |

**NF = 1 · 2/7 · 5 ND** *(mediana de [1,2] = 1,5 → §14.3 vale o inferior)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça a pergunta de forma genérica para um domínio específico: produção audiovisual, sem tratar de autoridade ou controle | — |
| E04 Transferibilidade | 2 | O **padrão** (conectar a cadeia criativa) transfere; os produtos são datados | — |
| E14 Diferencial | 2 | Agregação; sobrepõe `AC-06-VID-001`, `AC-06-VID-013` e `AC-06-VID-020` no mesmo domínio | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 1,1 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `107` + item do `_CONTEUDO.md` | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (os cinco conectores com função e os números de cada um) conferido; CONFIRMADA em `107`, "inclusive números promocionais".
**O que o catálogo afirma:** "Higgsfield (hub com 30+ modelos de imagem e vídeo…) · DaVinci Resolve… · Figma… · ElevenLabs (fala, clonagem de voz, transcrição; free tier de 10 mil créditos/mês) · YouTube…"
**Confere com a fonte:** sim — CONFIRMADA em `107`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "hub com 30+ modelos de imagem e vídeo" e "free tier de 10 mil créditos/mês" | print (texto observado, via `107`) | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| **Risco de uso registrado**, não pontuado em eixo: clonagem de voz exige autorização da pessoa cuja voz é clonada | esta ficha | `INFERÊNCIA` — marcada como tal | — |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-06-PRT-011 — `mcp4.png` *(série 5/6 — pagamentos e finanças)*

**Tipo:** PRINT · **Área:** 06_CONECTORES-MCP · **Série:** `mcp0`–`mcp5`
**Hash F0:** `EBB7DC91258790FE`   **Hash reconferido:** `EBB7DC91258790FE`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`107`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-06-PRT-011 · `H-P1-002` (relatório `107`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Três conectores financeiros exibidos com função **e uma regra dura declarada no próprio slide**: começar somente-leitura, nunca deixar a IA movimentar dinheiro sem supervisão, confirmar manualmente toda escrita. Exemplo isolado, sem implementação (`107`, CONFIRMADA) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e sua data |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | **Superfície retratada e não inspecionada, a mais sensível da série**: cliente, assinatura, reembolso, saldo e transação bancária. A regra está declarada; a implementação, não |
| E07 Licença ⚠ | ND | — | Ler os termos de cada serviço citado |
| E13 Testes/evals | ND | — | Nenhum teste do portão de confirmação manual |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas; a menção a "servidor oficial" é de origem, não de resultado, e permanece não verificada | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central no ponto de maior consequência: **onde o alcance externo vira efeito financeiro irreversível** | — |
| E04 Transferibilidade | 3 | A regra (somente-leitura primeiro; confirmação manual em toda escrita) transfere com adaptação declarada e independe de produto | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto no acervo: é o item que enuncia com mais clareza a **assimetria entre ler e movimentar dinheiro** | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 1,4 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `107` + item do `_CONTEUDO.md` | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (os três serviços e a regra de somente-leitura com aprovação manual) conferido; CONFIRMADA em `107`.
**O que o catálogo afirma:** "Stripe… · Plaid… · QuickBooks. **Regra dura que o próprio slide impõe:** comece sempre somente-leitura; nunca deixe a IA movimentar dinheiro real sem supervisão; confirme manualmente toda operação de escrita, sem exceção."
**Confere com a fonte:** sim — CONFIRMADA em `107`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "comece sempre somente-leitura; nunca deixe a IA movimentar dinheiro real sem supervisão" | print (texto observado, via `107`) | ALEGAÇÃO DO AUTOR | não — controle **declarado**, não verificado. É, entre todos os itens da área, a restrição mais explícita |
| "servidor oficial" (Stripe) | print / `_CONTEUDO.md` área 06 | ALEGAÇÃO DO AUTOR | não — oficialidade não verificada |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 3` · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-06-PRT-012 — `mcp5.png` *(série 6/6 — mercados e trading)*

**Tipo:** PRINT · **Área:** 06_CONECTORES-MCP · **Série:** `mcp0`–`mcp5`
**Hash F0:** `3F7D540DA6F9B8BB`   **Hash reconferido:** `3F7D540DA6F9B8BB`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`107`), com conferência do texto literal e da numeração.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-06-PRT-012 · `H-P1-002` (relatório `107`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só listagem: quatro fontes de dado de mercado nomeadas, com um princípio de uma linha. `107` registra ainda um **defeito gráfico**: numeração `3` repetida em dois itens (`107`, PARCIAL) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e sua data |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | **Superfície retratada e não inspecionada, de altíssima consequência**: um dos itens dá acesso a mais de vinte corretoras. Resolveria ler o escopo de permissão — e, em particular, se a chave usada permite ordem |
| E07 Licença ⚠ | ND | — | Ler os termos de cada serviço citado |
| E13 Testes/evals | ND | — | Nenhum artefato testável associado |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas; nenhum número decisivo em jogo | — |

**NF = 1 · 2/7 · 5 ND** *(mediana de [1,3] = 2 → §14.3 vale o inferior)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça a pergunta de forma genérica: lista fontes de dado sem definir autoridade nem separar leitura de ordem | — |
| E04 Transferibilidade | 2 | O princípio "dados primeiro" transfere; a seleção de fontes é datada | — |
| E14 Diferencial | 1 | Conveniência; é o slide de menor conteúdo operacional da série | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 1,4 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `107` + item do `_CONTEUDO.md` | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 2** — **PARCIAL** em `107`: os quatro serviços conferem, mas o catálogo escreve "ferramentas de dados (leitura) primeiro, **execução depois**", e o print diz **apenas** "Data tools first". A segunda metade é **inferência prudente do catálogo, não texto visível** — e, por ser prudente, é ainda mais importante não atribuí-la à fonte. Correção 6 de `107`; teto 2 (§14.4).
**O que o catálogo afirma:** "**Princípio declarado:** ferramentas de dados (leitura) primeiro, execução depois."
**Confere com a fonte:** parcialmente

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Data tools first" | print (texto observado, via `107`) | ALEGAÇÃO DO AUTOR | não |
| "execução depois" | `_CONTEUDO.md` área 06 | `INFERÊNCIA` do catálogo — **marcada como tal**, não presente no print | sustenta `NC = 2` |
| Numeração `3` repetida em dois itens | `107` (fato observado) | FATO OBSERVADO | defeito gráfico do original, preservado |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 3` · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> **Lacuna de série registrada:** a série `mcp0`–`mcp5` **não define, em nenhum slide, o escopo de permissão concreto** de nenhum conector — apenas a categoria e, em dois casos, a regra de aprovação humana.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-06-PRT-013 — `plugins.png`

**Tipo:** PRINT · **Área:** 06_CONECTORES-MCP
**Hash F0:** `D6E429573D002B5D`   **Hash reconferido:** `D6E429573D002B5D`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`107`), incluindo conferência dos erros gráficos.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-06-PRT-013 · `H-P1-002` (relatório `107`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só listagem: 20 conectores agrupados por categoria, com caminho de instalação. `107` confere inclusive **os defeitos**: numeração duplicada e os erros de grafia "Ontlook" e "Microsoft 366" | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e sua data |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | **Superfície retratada e não inspecionada**: documentos, comunicação, CRM, vendas e finanças. Resolveria ler o escopo de cada conector |
| E07 Licença ⚠ | ND | — | Ler os termos de cada serviço citado |
| E13 Testes/evals | ND | — | Nenhum artefato testável associado |
| E15 Alegações ⚠ | 1 | Alegações de capacidade e suporte com nomes citados porém **não conferidas**; `107` registra que "capacidades e suporte **não foram validados**", e os erros de grafia comprometem o uso do item como fonte de nomes exatos | — |

**NF = 1 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça a pergunta de forma genérica: inventário por categoria com caminho de instalação, sem critério nem escopo | — |
| E04 Transferibilidade | 2 | O **padrão** (agrupar conectores por função de negócio) transfere; a lista é datada e com erros | — |
| E14 Diferencial | 1 | Conveniência: sobrepõe `AC-06-PRT-004` e a série `mcp0`–`mcp5` | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 3,1 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `107` + parágrafo do `_CONTEUDO.md` | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (os 20 itens agrupados, o caminho de instalação **e os próprios defeitos do original**) conferido; CONFIRMADA em `107`. O catálogo acerta ao advertir que "não é fonte confiável para nomes exatos".
**O que o catálogo afirma:** "…é um catálogo de conectores para empresários, com o caminho de instalação… e 20 itens agrupados… *O infográfico tem erro de numeração e alguns typos (“Ontlook”, “Microsoft 366”) — não é fonte confiável para nomes exatos.*"
**Confere com a fonte:** sim — CONFIRMADA em `107`, inclusive quanto aos erros

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Ontlook" e "Microsoft 366" | print (texto observado, via `107`) | FATO OBSERVADO | erros do original, **preservados sem correção** — corrigi-los seria reescrever a fonte |
| "não é fonte confiável para nomes exatos" | `_CONTEUDO.md` área 06 | ALEGAÇÃO DO CATÁLOGO | **conferida** por `107` |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

> **Cobertura padrão dos 23 VÍDEO desta área:** ficha visual de 9 quadros (4%–92%) em `101` sob `H-M2-005`; ficha STT individual em `TRANSCRICOES-BRUTAS-STT/06_CONECTORES-MCP/`, sob `H-M3-001` e manifesto `117`. **LV3-V + LV3-A não produz LV4.** Nenhum binário aberto por esta frente. Fala automática é **provável, nunca citação exata**.
>
> **Bloco C — leitura uniforme (§3.3 do índice).** Para os 23 vídeos: `E08 = 3` (item documental, sem instalação, formato de consumo não declarado) · `E09 = 5` (arquivo local, sem custo recorrente) · `E10 = 4` (evidência derivada = ficha visual + ficha STT, < 1 MB) · `E11 = 5` (MP4, container aberto) · `E12 = 4` (consulta sem estado) → **`AA = 4 · 5/5 · 0 ND`**. A tabela é repetida em cada ficha para cumprir `04` §12; a **ferramenta retratada nunca é pontuada no lugar do vídeo**.
>
> **Cluster promocional desta área**, declarado por `101`: `AC-06-VID-007`, `015`, `016`, `018`, `021` e `022` se sobrepõem entre si e com o cluster da área 05; `AC-06-VID-001` e `013` repetem a mesma demonstração. A repetição reduz `E14`, nunca confirma (P-3).

### AC-06-VID-001 — `gemini + higs.mp4`

**Tipo:** VÍDEO · **Área:** 06_CONECTORES-MCP
**Hash F0:** `908681CB76437C69`   **Hash reconferido:** `908681CB76437C69`   **Confere:** sim
**LV:** LV3-V + LV3-A *(12,3 s, `en`, 10 palavras, p = 0,902, **ALTA AUTOMÁTICA** — fala curta e não descritiva)*
**Cobertura da leitura:** 9 quadros (`101`); transcrição integral (uma frase de abertura).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-06-VID-001 · `H-M2-005` (`101`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Demonstração isolada e não reprodutível: transformações de vídeo quadro a quadro (redefinição de cenário, preservação de movimento, HUD inserido, recorte social, trajetória sobre mapa). Nenhum prompt, insumo ou parâmetro acompanha (`101`) | — |
| E03 Maturidade | ND | — | Identificar os produtos retratados e inspecionar seu estágio |
| E05 Manutenção | ND | — | Localizar o canal de publicação com data |
| E06 Segurança ⚠ | ND | — | Nenhuma superfície inspecionada; geração audiovisual levanta questões de direito de imagem não avaliadas aqui |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos do vídeo e dos produtos |
| E13 Testes/evals | ND | — | Nenhuma comparação medida de qualidade |
| E15 Alegações ⚠ | 1 | Alegações de capacidade com produtos nomeados porém **não conferidas**: `101` registra que "identidade do produto, disponibilidade, qualidade, direitos e privacidade precisam de confirmação" | — |

**NF = 1 · 2/7 · 5 ND** *(mediana de [1,2] = 1,5 → §14.3 vale o inferior)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça a pergunta de forma genérica: mostra alcance a uma ferramenta externa de mídia, sem tratar de conector, permissão ou contrato | — |
| E04 Transferibilidade | 1 | Só a ideia viaja; a demonstração depende de produto e conta do autor | — |
| E14 Diferencial | 1 | Conveniência: `101` registra que `AC-06-VID-013` é "visualmente equivalente" — os dois formam uma repetição da mesma família promocional | — |

**RP = 1 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 15,3 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 1** — o item está na tabela "Vídeo (NÃO é legível por IA)" com a coluna "Assunto": descrição derivada do nome do arquivo (`gemini + higs.mp4` → "Gemini combinado com Higgsfield"), sem indício de inspeção. Compatível com o observado, mas compatibilidade não eleva a nota (§6, âncora 1).
**O que o catálogo afirma:** "`gemini + higs.mp4` | 16 MB | Gemini combinado com Higgsfield"
**Confere com a fonte:** sim, em nível genérico

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Alright, let's check the vibe of our new design space." | LV3-A bruto, 00:00:00–00:00:11,120 — **fala provável, não citação exata** | ALEGAÇÃO DO AUTOR | não — sem conteúdo técnico |
| "Identidade do produto, disponibilidade, qualidade, direitos e privacidade precisam de confirmação." | `101` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | não |

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

### AC-06-VID-002 — `Gravando 2026-07-28 154542.mp4`

**Tipo:** VÍDEO · **Área:** 06_CONECTORES-MCP
**Hash F0:** `D459E96B86C3B742`   **Hash reconferido:** `D459E96B86C3B742`   **Confere:** sim
**LV:** LV3-V *(LV3-A = `SEM NARRAÇÃO CONFIÁVEL — EFEITO, MÚSICA OU ALUCINAÇÃO DO STT`, 4 palavras, p = 0,686)*
**Cobertura da leitura:** 9 quadros (`101`); ficha STT (40,1 s).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-06-VID-002 · `H-M2-005` (`101`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só listagem parcial: `101` registra que **a lista completa não ficou visível** — oito conectores foram lidos de um total anunciado de quinze. Sem demonstração | — |
| E03 Maturidade | ND | — | Identificar cada conector e inspecionar seu estágio |
| E05 Manutenção | ND | — | Localizar o canal de publicação com data |
| E06 Segurança ⚠ | ND | — | **Superfície declarada e não inspecionada**: `101` registra "permissões amplas e efeitos externos" |
| E07 Licença ⚠ | ND | — | Ler os termos de cada conector |
| E13 Testes/evals | ND | — | Nenhum teste exibido |
| E15 Alegações ⚠ | 1 | Alegação numérica com fonte implícita porém **não conferível**: o título anuncia quinze conectores e só oito são legíveis nos quadros | — |

**NF = 1 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça a pergunta de forma genérica: lista conectores sem escopo, permissão ou contrato | — |
| E04 Transferibilidade | 1 | Só a ideia viaja; a lista está incompleta | — |
| E14 Diferencial | 1 | Conveniência; sobrepõe `AC-06-PRT-004` e `AC-06-PRT-013` | — |

**RP = 1 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 38,4 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 2** — **PARCIAL.** O método é declarado e o tema confere, mas **dois dos três produtos citados no título não aparecem** entre os oito legíveis em `101` (que lê Algrow, Adobe, Gmail, Drive, Supabase, Metricool, Zapier e um item que parece Firecrawl). Apenas um coincide. Atribuição material não conferida → teto 2 (§14.4).
**O que o catálogo afirma:** "`Gravando 2026-07-28 154542.mp4` | 38,4 MB | Claude conectado a Tally, Notion, Metricool e outras ferramentas | não transcrito"
**Confere com a fonte:** parcialmente

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "15 conectores para Claude" | `101` (título observado) | ALEGAÇÃO DO AUTOR | não — **não conferível**: só oito ficaram legíveis |
| "não avaliar os quinze sem áudio ou fonte primária" | `101` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | — regra seguida nesta ficha |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-06-VID-003 — `Gravando 2026-07-28 162702.mp4`

**Tipo:** VÍDEO · **Área:** 06_CONECTORES-MCP
**Hash F0:** `F33F44D82D56E6BF`   **Hash reconferido:** `F33F44D82D56E6BF`   **Confere:** sim
**LV:** LV3-V *(LV3-A = `SEM NARRAÇÃO CONFIÁVEL — EFEITO, MÚSICA OU ALUCINAÇÃO DO STT`, 68 palavras, p = 0,719 — texto descartado como não confiável)*
**Cobertura da leitura:** 9 quadros (`101`); ficha STT (20,8 s).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-06-VID-003 · `H-M2-005` (`101`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só listagem: seis alternativas legíveis de dez anunciadas, por função (documentos/OCR, segredos, conhecimento local, bloqueio de rede, sincronização, automação residencial). Sem demonstração (`101`) | — |
| E03 Maturidade | ND | — | Identificar cada projeto e inspecionar seu estágio |
| E05 Manutenção | ND | — | Verificar atividade de cada projeto na origem |
| E06 Segurança ⚠ | ND | — | **Superfície declarada e não inspecionada**; `101` registra o ponto central: "Self-hosting **transfere operação e segurança para a empresa**; não elimina risco" |
| E07 Licença ⚠ | ND | — | Ler a licença de cada projeto na origem |
| E13 Testes/evals | ND | — | Nenhum teste exibido |
| E15 Alegações ⚠ | 1 | Alegação de substituição de assinaturas pagas, com nomes citados porém não conferidos; quatro dos dez itens sequer ficaram legíveis | — |

**NF = 1 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central por um ângulo estrutural: **substituir serviço externo por serviço próprio** muda a natureza da fronteira, não só o fornecedor | — |
| E04 Transferibilidade | 2 | O **padrão** (avaliar auto-hospedagem por função) transfere; os projetos não foram identificados | — |
| E14 Diferencial | 2 | Agregação; forma família com `AC-06-VID-004`, `005` e `011`, todos listas de projetos abertos | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 12,6 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado ("Título pelo conteúdo visível") **e confirmado** pelos quadros: "dez alternativas open source a assinaturas pagas" corresponde ao observado, incluindo o total anunciado (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 162702.mp4` | 12,6 MB | dez alternativas open source a assinaturas pagas | não transcrito"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Self-hosting transfere operação e segurança para a empresa; não elimina risco." | `101` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | não |
| "“grátis” e “open source” não significam baixo risco. Licença, manutenção, telemetria e privilégio de execução não aparecem nos vídeos." | `_CONTEUDO.md` área 06 | ALEGAÇÃO DO CATÁLOGO | — ressalva correta, registrada |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4. A lacuna de identidade dos projetos é **de família** e está nomeada uma única vez em `AC-06-VID-011`.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-06-VID-004 — `Gravando 2026-07-28 162934.mp4`

**Tipo:** VÍDEO · **Área:** 06_CONECTORES-MCP
**Hash F0:** `67801C74A12B7A31`   **Hash reconferido:** `67801C74A12B7A31`   **Confere:** sim
**LV:** LV3-V *(LV3-A = `SEM FALA LEXICAL CONFIÁVEL`, 1 palavra, p = 0,751)*
**Cobertura da leitura:** 9 quadros (`101`); ficha STT (27,5 s).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-06-VID-004 · `H-M2-005` (`101`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só listagem: oito projetos legíveis de dez anunciados, por domínio (finanças, agentes, interface local, suporte, assinatura, BI, colaboração, workflows). Sem demonstração (`101`) | — |
| E03 Maturidade | ND | — | Identificar cada projeto e inspecionar seu estágio |
| E05 Manutenção | ND | — | Verificar atividade de cada projeto na origem |
| E06 Segurança ⚠ | ND | — | **Superfície declarada e não inspecionada**; `101` exige "identidade, licença, isolamento, dados, manutenção e **controles específicos de domínio**" — dois dos domínios são finanças e assinatura eletrônica |
| E07 Licença ⚠ | ND | — | Ler a licença de cada projeto |
| E13 Testes/evals | ND | — | Nenhum teste exibido |
| E15 Alegações ⚠ | 1 | Alegações de capacidade por projeto, com nomes citados porém não conferidos; dois itens não ficaram legíveis | — |

**NF = 1 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça a pergunta de forma genérica: lista alternativas por domínio, sem escopo de dado nem controle | — |
| E04 Transferibilidade | 1 | Só a ideia viaja | — |
| E14 Diferencial | 1 | Conveniência: integra a família de listas de projetos abertos desta área | — |

**RP = 1 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 13,1 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado **e confirmado** pelos quadros: os quatro domínios citados no título correspondem aos observados (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 162934.mp4` | 13,1 MB | apps open source para finanças, atendimento, produtividade e documentos | não transcrito"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "**Gate:** identidade, licença, isolamento, dados, manutenção e controles específicos de domínio." | `101` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | não |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-06-VID-005 — `Gravando 2026-07-28 164155.mp4`

**Tipo:** VÍDEO · **Área:** 06_CONECTORES-MCP
**Hash F0:** `87CFFBA015D41D49`   **Hash reconferido:** `87CFFBA015D41D49`   **Confere:** sim
**LV:** LV3-V *(LV3-A = `SEM FALA LEXICAL CONFIÁVEL`, 1 palavra, p = 0,130)*
**Cobertura da leitura:** 9 quadros (`101`); ficha STT (21,6 s).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-06-VID-005 · `H-M2-005` (`101`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só listagem: nove ferramentas legíveis de dez, por domínio (mídia, conhecimento, CRM, compartilhamento, whiteboard, assinatura, segurança, e-mail). Sem demonstração (`101`) | — |
| E03 Maturidade | ND | — | Identificar cada ferramenta e inspecionar seu estágio |
| E05 Manutenção | ND | — | Verificar atividade na origem |
| E06 Segurança ⚠ | ND | — | **Superfície declarada e não inspecionada**: uma das ferramentas legíveis é de defesa de rede, outra de assinatura eletrônica |
| E07 Licença ⚠ | ND | — | Ler a licença de cada ferramenta |
| E13 Testes/evals | ND | — | Nenhum teste exibido |
| E15 Alegações ⚠ | 1 | `101` registra que "**social proof e promessas de economia são alegações**", com fonte implícita e não conferida | — |

**NF = 1 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça a pergunta de forma genérica: inventário por domínio sem escopo nem controle | — |
| E04 Transferibilidade | 1 | Só a ideia viaja | — |
| E14 Diferencial | 1 | Conveniência: integra a família de listas de projetos abertos desta área | — |

**RP = 1 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 12,6 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado **e confirmado** pelos quadros: as três ferramentas citadas no título estão entre as nove legíveis (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 164155.mp4` | 12,6 MB | alternativas open source: Anytype, Jellyfin, CrowdSec e outras | não transcrito"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Social proof e promessas de economia são alegações." | `101` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | não — coerente com **P-3** |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-06-VID-006 — `Gravando 2026-07-28 164243.mp4`

**Tipo:** VÍDEO · **Área:** 06_CONECTORES-MCP
**Hash F0:** `5BA3E29ACE6451C1`   **Hash reconferido:** `5BA3E29ACE6451C1`   **Confere:** sim
**LV:** LV3-V + LV3-A
**Cobertura da leitura:** 9 quadros (`101`); transcrição automática bruta integral (29,8 s, `en`, 6 segmentos, p = 0,849, **MÉDIA AUTOMÁTICA**). Sem revisão humana.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-06-VID-006 · `H-M2-005` (`101`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Cinco ferramentas exibidas **com função declarada por ferramenta**, e a fala provável descreve cada uma: busca web ao vivo, controle de navegador com preenchimento de formulário e teste, leitura de sites inteiros, conexão a ferramentas de mídia, e leitura das abas abertas. Exemplo isolado, sem configuração | — |
| E03 Maturidade | ND | — | Identificar cada ferramenta e inspecionar seu estágio. **Uma delas está no acervo**: `AC-06-REP-001` |
| E05 Manutenção | ND | — | Localizar o canal de publicação com data |
| E06 Segurança ⚠ | ND | — | **Superfície declarada, crítica e não inspecionada**: `101` registra "**Risco alto:** conteúdo web não confiável, prompt injection, credenciais e ações no navegador; requer navegação isolada, allowlist e confirmação para escrita" |
| E07 Licença ⚠ | ND | — | Ler a licença de cada ferramenta |
| E13 Testes/evals | ND | — | Nenhum teste exibido |
| E15 Alegações ⚠ | 0 | A proposta central **depende** de alegações numéricas fortes **sem fonte**: "They make it **10 times more powerful**" (LV3-A, 00:00:00–00:00:05) e "**34,000 stars** on github" (00:00:10–00:00:16). **P-3** aplicado à segunda | — |

**NF = 1 · 2/7 · 5 ND** *(mediana de [0,2] = 1)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: cinco mecanismos distintos de alcance externo, cada um com função declarada | — |
| E04 Transferibilidade | 2 | O **padrão** (compor pesquisa + navegador + coleta) transfere; a implementação depende das ferramentas | — |
| E14 Diferencial | 2 | Agregação; uma das cinco tem ficha própria no acervo, com licença lida e superfície analisada | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 27,1 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT de 6 segmentos; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado **e confirmado** por duas evidências: os quadros (`101`) e a fala provável, que nomeia as três ferramentas do título (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 164243.mp4` | 27,1 MB | stack de pesquisa e navegador ao vivo: Perplexity, Firecrawl e Chrome | não transcrito"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Open Cloud Code again until you install these five tools. They make it **10 times more powerful**." | LV3-A bruto, 00:00:00–00:00:05,280 — **fala provável, não citação exata** | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "cloud drives a browser, clicks, fills forms, tests your app, **34,000 stars on github**" | LV3-A bruto, 00:00:10,400–00:00:16,240 — fala provável | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA`; **P-3** |
| "**Risco alto:** conteúdo web não confiável, prompt injection, credenciais e ações no navegador." | `101` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | não |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |
| **V7** | **sim** | `E15 = 0` e a proposta depende do ganho de "10×" → teto EXIGE PESQUISA |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** V7 (§8) — teto EXIGE PESQUISA.
**Se EXIGE PESQUISA — lacuna nomeada:** o ganho de "10 vezes" não tem medição nem definição, e a superfície de conteúdo web não confiável — o vetor de injeção de prompt mais direto do acervo — não foi inspecionada em nenhuma das cinco ferramentas.  **Verificação que a fecharia:** para a ferramenta que **já está no acervo**, a lacuna correspondente está nomeada em `AC-06-REP-001`; para as demais, localizar cada uma na origem pública e ler licença e escopo — **sem instalar**.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-06-VID-007 — `Gravando 2026-07-28 164517.mp4`  ·  cluster promocional

**Tipo:** VÍDEO · **Área:** 06_CONECTORES-MCP
**Hash F0:** `61856E2B8BBCFBEC`   **Hash reconferido:** `61856E2B8BBCFBEC`   **Confere:** sim
**LV:** LV3-V *(LV3-A = `SEM FALA LEXICAL CONFIÁVEL`, 1 palavra, p = 0,751)*
**Cobertura da leitura:** 9 quadros (`101`); ficha STT (13,8 s).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-06-VID-007 · `H-M2-005` (`101`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só listagem: 24 complementos repetindo nomes já divulgados na área 05, sem demonstração. `101` classifica como "**valor marginal:** índice de descoberta" | — |
| E03 Maturidade | ND | — | Identificar cada item e inspecionar seu estágio |
| E05 Manutenção | ND | — | Verificar atividade na origem |
| E06 Segurança ⚠ | ND | — | **Superfície declarada e não inspecionada**: conectores com acesso a documentos, mensagens e automação |
| E07 Licença ⚠ | ND | — | Ler a licença de cada item |
| E13 Testes/evals | ND | — | Nenhum teste exibido |
| E15 Alegações ⚠ | 1 | Alegações com nomes citados porém não conferidas; sem critério de seleção declarado | — |

**NF = 1 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça a pergunta de forma genérica: índice de descoberta sem escopo nem permissão | — |
| E04 Transferibilidade | 1 | Só a ideia viaja | — |
| E14 Diferencial | 1 | Conveniência: `101` registra que o item "integra o cluster promocional já identificado na área 05; repetição não é validação" | — |

**RP = 1 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 8,1 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 2** — **PARCIAL.** A distinção "plugin × skill × MCP" confere, mas o catálogo afirma "**três instalações para começar**" e `101` observa **24 complementos** divulgados. Contagem material divergente → teto 2 (§14.4).
**O que o catálogo afirma:** "`Gravando 2026-07-28 164517.mp4` | 8,1 MB | plugin × skill × MCP e três instalações para começar | não transcrito"
**Confere com a fonte:** parcialmente

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Integra o cluster promocional já identificado na área 05; **repetição não é validação**." | `101` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | — coerente com P-3 |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4. Lacuna do cluster nomeada uma única vez em `AC-05-VID-009`.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-06-VID-008 — `Gravando 2026-07-28 164648.mp4`  ·  ⚠ item de evasão declarado

**Tipo:** VÍDEO · **Área:** 06_CONECTORES-MCP
**Hash F0:** `BAE56116AFDB9262`   **Hash reconferido:** `BAE56116AFDB9262`   **Confere:** sim
**LV:** LV3-V *(LV3-A = `SEM FALA LEXICAL CONFIÁVEL`, 1 palavra, p = 0,130)*
**Cobertura da leitura:** 9 quadros (`101`); ficha STT (23,9 s).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-06-VID-008 · `H-M2-005` (`101`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só divulgação: nove repositórios legíveis de dez, sem demonstração nem artefato inspecionável (`101`) | — |
| E03 Maturidade | ND | — | Identificar cada repositório e inspecionar seu estágio |
| E05 Manutenção | ND | — | Verificar atividade na origem |
| E06 Segurança ⚠ | ND | — | **Superfície declarada, crítica e não inspecionada.** `101` é explícito: "**Risco crítico:** trading, envio de email e **navegador furtivo**. Camoflox é apresentado como forma de **parecer humano e contornar detecção**; manter em rejeição/quarentena por evasão e possível violação de termos". Nenhuma inspeção direta foi feita — por isso ND, não 0 |
| E07 Licença ⚠ | ND | — | Ler a licença de cada repositório |
| E13 Testes/evals | ND | — | Nenhum teste exibido |
| E15 Alegações ⚠ | 1 | Alegações de capacidade com nomes citados porém não conferidas; um item não ficou legível | — |

**NF = 1 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça a pergunta de forma genérica: lista repositórios de alcance externo, incluindo dois de domínio financeiro e um de evasão | — |
| E04 Transferibilidade | 1 | Só a ideia viaja | — |
| E14 Diferencial | 1 | Conveniência sobre lista já acessível | — |

**RP = 1 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 14,1 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado **e confirmado** pelos quadros: os três produtos citados no título estão entre os nove legíveis (`04` §6.1.5). **Registrada divergência de grafia**: o catálogo escreve "Camofox" e `101` lê "Camoflox" — nenhuma das duas foi confirmada na origem.
**O que o catálogo afirma:** "`Gravando 2026-07-28 164648.mp4` | 14,1 MB | Fincept Terminal, Open LLM VTuber, Camofox Browser e outras ferramentas | não transcrito"
**Confere com a fonte:** sim, com a ressalva de grafia

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Camoflox é apresentado como forma de **parecer humano e contornar detecção**" | `101` (texto visual observado) | ALEGAÇÃO DO AUTOR | não — **achado de risco registrado**: é o segundo caso de evasão declarada no acervo, ao lado de `AC-04-REP-005` e `AC-06-REP-002` |
| "manter em **rejeição/quarentena** por evasão e possível violação de termos" | `101` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | não — **registrada, não executada**: esta frente não rejeita por alegação de terceiro, só por evidência (§9) |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 | **não** | `E06 = ND`, **não 0**: o risco de evasão é **declarado por terceiro** e não foi confirmado por inspeção direta. §9: "Rejeitado **por evidência**, nunca por ND" |
| V3 · V5 · V6 · V7 · V8 | não | `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** §9 — relevância aparente com lacuna nomeada e endereçável; teto de V2/V4 respeitado. **Deliberadamente não é REJEITADO**: a rejeição exigiria `E06 = 0` por inspeção direta, como ocorreu em `AC-05-REP-003`.
**Se EXIGE PESQUISA — lacuna nomeada:** a identidade e a função real do navegador apresentado como capaz de contornar detecção — inclusive a grafia correta do nome, que diverge entre catálogo e inspeção visual.  **Verificação que a fecharia:** localizar o repositório na origem pública e ler README e licença. **Se a função de evasão se confirmar por inspeção direta, o item passa a `E06 = 0` e V1 impõe REJEITADO** — como já ocorreu com `AC-05-REP-003`.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-06-VID-009 — `Gravando 2026-07-28 164826.mp4`

**Tipo:** VÍDEO · **Área:** 06_CONECTORES-MCP
**Hash F0:** `5E60EE16894BA6FC`   **Hash reconferido:** `5E60EE16894BA6FC`   **Confere:** sim
**LV:** LV3-V *(LV3-A = `SEM FALA LEXICAL CONFIÁVEL`, 1 palavra, p = 0,130)*
**Cobertura da leitura:** 9 quadros (`101`); ficha STT (18,9 s).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-06-VID-009 · `H-M2-005` (`101`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só listagem: sete aplicativos de consumo nomeados por categoria (armazenamento, acesso remoto, bookmarks, saúde, finanças, viagem, tarefas), sem relação declarada com agentes (`101`) | — |
| E03 Maturidade | ND | — | Identificar cada aplicativo e inspecionar seu estágio |
| E05 Manutenção | ND | — | Verificar atividade na origem |
| E06 Segurança ⚠ | ND | — | **Superfície retratada e não inspecionada**: um dos itens é acesso remoto a máquina; outro, dado de saúde | — |
| E07 Licença ⚠ | ND | — | Ler os termos de cada aplicativo |
| E13 Testes/evals | ND | — | Nenhum teste exibido |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas (para que serve cada aplicativo); nenhum número decisivo | — |

**NF = 1 · 2/7 · 5 ND** *(mediana de [1,3] = 2 → §14.3 vale o inferior)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 1 | Tangencia a área: `101` classifica o **valor direto como baixo** — são aplicativos de consumo, não conectores nem mecanismos de alcance | — |
| E04 Transferibilidade | 1 | Só a ideia viaja | — |
| E14 Diferencial | 0 | **Reprodutível em horas com ferramenta já disponível**: é uma lista de aplicativos populares | — |

**RP = 1 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 10,1 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado **e confirmado** pelos quadros: os quatro aplicativos citados no título estão entre os sete observados (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 164826.mp4` | 10,1 MB | sete apps úteis: Terabox, AnyDesk, Raindrop, Wise e outros | não transcrito"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Não tratar aplicativos de consumo como infraestrutura empresarial sem caso e controles." | `101` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | não |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 3` · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`. **`E01 = 1` (≠ 0)**, portanto **não** cabe REJEITADO, apesar de ser o item de menor relevância da área.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-06-VID-010 — `Gravando 2026-07-28 175754.mp4`

**Tipo:** VÍDEO · **Área:** 06_CONECTORES-MCP
**Hash F0:** `9C413104BD0D0020`   **Hash reconferido:** `9C413104BD0D0020`   **Confere:** sim
**LV:** LV3-V *(LV3-A = `SEM FALA LEXICAL CONFIÁVEL`, 1 palavra, p = 0,751)*
**Cobertura da leitura:** 9 quadros (`101`); ficha STT (13,4 s).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-06-VID-010 · `H-M2-005` (`101`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Cinco conectores de negócio exibidos com função (criação, mídia paga, comércio, pesquisa fundamentada, reuniões), **e um achado estrutural**: `101` registra a diferenciação entre "leitura/relatório" e "otimização/execução" | — |
| E03 Maturidade | ND | — | Identificar cada conector e inspecionar seu estágio |
| E05 Manutenção | ND | — | Localizar o canal de publicação com data |
| E06 Segurança ⚠ | ND | — | **Superfície declarada, crítica e não inspecionada**: mídia paga (gasto), comércio (transação) e transcrições de reunião (dado de terceiro). `101` exige "consentimento, segregação e aprovação" | — |
| E07 Licença ⚠ | ND | — | Ler os termos de cada conector |
| E13 Testes/evals | ND | — | Nenhum teste exibido |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas; nenhum número decisivo em jogo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central **e faz a distinção que importa**: ler e relatar é uma coisa; otimizar e executar é outra | — |
| E04 Transferibilidade | 3 | A distinção leitura × execução transfere com adaptação declarada e independe de produto | — |
| E14 Diferencial | 2 | Agregação; a mesma distinção aparece, mais desenvolvida, em `AC-06-PRT-009` e `AC-06-PRT-011` | — |

**RP = 3 · 3/3 · 0 ND**

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
**NC = 5** — método declarado **e confirmado** pelos quadros: os três produtos citados no título estão entre os cinco observados (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 175754.mp4` | 7,6 MB | combinações Claude + Higgsfield, Hotmart e Granola | não transcrito"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "**Achado:** diferenciar leitura/relatório de otimização/execução. Gastos, dados comerciais, transcrições e ações exigem consentimento, segregação e aprovação." | `101` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | não |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 3` · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-06-VID-011 — `Gravando 2026-07-28 175840.mp4`

**Tipo:** VÍDEO · **Área:** 06_CONECTORES-MCP
**Hash F0:** `CABB3A6508DA4A5A`   **Hash reconferido:** `CABB3A6508DA4A5A`   **Confere:** sim
**LV:** LV3-V *(LV3-A = `SEM FALA LEXICAL CONFIÁVEL`, 1 palavra, p = 0,751)*
**Cobertura da leitura:** 9 quadros (`101`); ficha STT (20,1 s).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-06-VID-011 · `H-M2-005` (`101`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só listagem: nove ferramentas legíveis de dez, por função (construtor de app local, agente executor, pesquisa, sandbox, codificação paralela, scraping adaptativo, clonagem de site, recuperação, voz). Sem demonstração (`101`) | — |
| E03 Maturidade | ND | — | Identificar cada ferramenta e inspecionar seu estágio |
| E05 Manutenção | ND | — | Verificar atividade na origem |
| E06 Segurança ⚠ | ND | — | **Superfície declarada, crítica e não inspecionada**: `101` registra que "clonagem/scraping, **execução de código** e voz elevam riscos de IP, segurança e privacidade" |
| E07 Licença ⚠ | ND | — | Ler a licença de cada ferramenta |
| E13 Testes/evals | ND | — | Nenhum teste exibido |
| E15 Alegações ⚠ | 1 | Alegações de capacidade com nomes citados porém não conferidas; um item não ficou legível | — |

**NF = 1 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça a pergunta de forma genérica: inventário de ferramentas de alcance sem escopo nem controle | — |
| E04 Transferibilidade | 1 | Só a ideia viaja | — |
| E14 Diferencial | 2 | Agregação; integra a família de listas de projetos abertos, mas acrescenta duas categorias que as outras não trazem — sandbox de execução e codificação paralela | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 12 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado **e confirmado** pelos quadros: as três ferramentas citadas no título estão entre as nove legíveis (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 175840.mp4` | 12,0 MB | ferramentas open source: Goose, Parallel Code, RAGFlow e outras | não transcrito"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Clonagem/scraping, execução de código e voz elevam riscos de IP, segurança e privacidade." | `101` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | não |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** §9 — relevância aparente com lacuna nomeada e endereçável; teto de V2/V4 respeitado.
**Se EXIGE PESQUISA — lacuna nomeada:** identidade, licença e superfície de execução dos projetos abertos citados **nesta e nas três fichas irmãs** (`AC-06-VID-003`, `004`, `005`) — em particular os que executam código de terceiro (sandbox) e os que clonam ou raspam conteúdo alheio, com a questão de propriedade intelectual anexa.  **Verificação que a fecharia:** localizar cada projeto na origem pública e ler licença, README e escopo de execução — **sem clonar nem executar**. Lacuna **da família**, contada uma vez.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-06-VID-012 — `Gravando 2026-07-28 180001.mp4`

**Tipo:** VÍDEO · **Área:** 06_CONECTORES-MCP
**Hash F0:** `7DA8C6E5E7A1C06F`   **Hash reconferido:** `7DA8C6E5E7A1C06F`   **Confere:** sim
**LV:** LV3-V *(LV3-A = `SEM FALA LEXICAL CONFIÁVEL`, 1 palavra, p = 0,751)*
**Cobertura da leitura:** 9 quadros (`101`); ficha STT (12,2 s).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-06-VID-012 · `H-M2-005` (`101`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só listagem: cinco produtos associados a funções heterogêneas (ditado, atas, scraping, criação audiovisual, automação), sem demonstração (`101`) | — |
| E03 Maturidade | ND | — | Identificar cada produto e inspecionar seu estágio |
| E05 Manutenção | ND | — | Localizar o canal de publicação com data |
| E06 Segurança ⚠ | ND | — | **Superfície retratada e não inspecionada**: ditado captura áudio; scraping alcança conteúdo de terceiro | — |
| E07 Licença ⚠ | ND | — | Ler os termos de cada produto |
| E13 Testes/evals | ND | — | Nenhum teste exibido |
| E15 Alegações ⚠ | 0 | A proposta central **depende** de promessas fortes **sem fonte**, que `101` registra: "Promessas de preço, velocidade, qualidade e **“rodar o negócio inteiro”** não foram verificadas" | — |

**NF = 0 · 2/7 · 5 ND** *(mediana de [0,1] = 0,5 → §14.3 vale o inferior)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça a pergunta de forma genérica; o achado útil é **corretivo**: `101` observa que "são classes de ferramentas **diferentes**, não cinco IAs equivalentes" | — |
| E04 Transferibilidade | 1 | Só a ideia viaja | — |
| E14 Diferencial | 1 | Conveniência sobre lista já acessível | — |

**RP = 1 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 8 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado **e confirmado** pelos quadros: os três produtos citados no título estão entre os cinco observados (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 180001.mp4` | 8,0 MB | cinco ferramentas: Wispr Flow, Apify, Claude Code e outras | não transcrito"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Promessas de preço, velocidade, qualidade e “rodar o negócio inteiro” não foram verificadas." | `101` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | não — sustenta `E15 = 0` |
| "são classes de ferramentas diferentes, **não cinco IAs equivalentes**" | `101` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | — correção material do enquadramento do próprio vídeo |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |
| **V7** | **sim** | `E15 = 0` e a proposta depende das promessas → teto EXIGE PESQUISA |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** V7 (§8) — teto EXIGE PESQUISA.
**Se EXIGE PESQUISA — lacuna nomeada:** as promessas de preço, velocidade e qualidade, e o enquadramento de "cinco IAs" que agrupa classes incomparáveis.  **Verificação que a fecharia:** separar as cinco por função e, para cada uma, obter preço e limite na fonte primária do fornecedor — sem o que a comparação não é avaliável.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-06-VID-013 — `Gravando 2026-07-28 180429.mp4`  ·  duplicação de conteúdo declarada

**Tipo:** VÍDEO · **Área:** 06_CONECTORES-MCP
**Hash F0:** `3F5CCF7CB3C788EE`   **Hash reconferido:** `3F5CCF7CB3C788EE`   **Confere:** sim
**LV:** LV3-V + LV3-A *(39,1 s, `en`, 41 palavras, p = 0,737, **BAIXA AUTOMÁTICA — FALA BREVE COM MÚSICA**)*
**Cobertura da leitura:** 9 quadros (`101`); ficha STT com dois trechos abaixo do limiar, registrados como tal.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-06-VID-013 · `H-M2-005` (`101`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Demonstração isolada de transformação de vídeo, **visualmente equivalente** a `AC-06-VID-001` segundo `101`. A fala provável é curta e mistura música; a confiança é declarada **BAIXA** | — |
| E03 Maturidade | ND | — | Identificar os produtos retratados e inspecionar seu estágio |
| E05 Manutenção | ND | — | Localizar o canal de publicação com data |
| E06 Segurança ⚠ | ND | — | Nenhuma superfície inspecionada | — |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos | — |
| E13 Testes/evals | ND | — | Nenhuma comparação medida | — |
| E15 Alegações ⚠ | 1 | Alegação de qualidade com produto nomeado porém não conferida: a fala provável diz "let's check the vibe of this new model… **She's absolutely insane**" | — |

**NF = 1 · 2/7 · 5 ND** *(mediana de [1,2] = 1,5 → §14.3 vale o inferior)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça a pergunta de forma genérica: alcance a ferramenta externa de mídia, sem contrato nem permissão | — |
| E04 Transferibilidade | 1 | Só a ideia viaja | — |
| E14 Diferencial | 0 | **Reprodutível em horas com ferramenta já disponível** — e, mais que isso, `101` declara: "conteúdo **visualmente equivalente** ao AC-06-VID-001. **Deduplicação:** tratar como repetição da mesma família promocional, não evidência independente" | — |

**RP = 1 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 31,4 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado **e confirmado** pelos quadros (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 180429.mp4` | 31,4 MB | Higgsfield + Gemini para transformar vídeo e criar tomadas | não transcrito"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "let's check the vibe of this new model… **She's absolutely insane**." | LV3-A bruto, 00:00:09,200–00:00:13,680 — **fala provável, confiança BAIXA declarada** | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "Deduplicação: tratar como repetição da mesma família promocional, **não evidência independente**." | `101` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | **conferida** entre as duas fichas visuais |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4. **Não é `DUPLICADO`**: os hashes diferem e a sobreposição é de **conteúdo visual**, não binária — `05` §10 reserva `DUPLICADO` para identidade de hash ou sobreposição medida, e nenhuma medição de sobreposição foi feita aqui.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-06-VID-014 — `Gravando 2026-07-28 180542.mp4`

**Tipo:** VÍDEO · **Área:** 06_CONECTORES-MCP
**Hash F0:** `C137535557DFD8DA`   **Hash reconferido:** `C137535557DFD8DA`   **Confere:** sim
**LV:** LV3-V *(LV3-A = `SEM FALA LEXICAL CONFIÁVEL`, 1 palavra, p = 0,130)*
**Cobertura da leitura:** 9 quadros (`101`); ficha STT (20,5 s).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-06-VID-014 · `H-M2-005` (`101`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Mapa exibido em tela associando **ferramenta a função** — escrita, pesquisa, fontes, conteúdo, visuais, análise, conhecimento — e, no último item, uma **composição** de três ferramentas para conhecimento. Exemplo isolado (`101`) | — |
| E03 Maturidade | ND | — | Identificar cada produto e inspecionar seu estágio |
| E05 Manutenção | ND | — | Localizar o canal de publicação com data |
| E06 Segurança ⚠ | ND | — | Nenhuma superfície inspecionada |
| E07 Licença ⚠ | ND | — | Ler os termos de cada produto |
| E13 Testes/evals | ND | — | Nenhum critério de escolha por função exibido |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas (qual ferramenta para qual função); nenhum número decisivo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: **separação por função e composição de pipeline**, que é o padrão útil sob a lista | — |
| E04 Transferibilidade | 3 | A separação por função transfere com adaptação declarada; as marcas são substituíveis | — |
| E14 Diferencial | 2 | Agregação; sobrepõe `AC-06-PRT-002` e `AC-01-VID-006` no mesmo padrão | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 12,5 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado **e confirmado** pelos quadros: as quatro ferramentas citadas no título estão entre as observadas (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 180542.mp4` | 12,5 MB | guia de combinações Claude, ChatGPT, Obsidian e NotebookLM | não transcrito"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "**Valor:** separação por função e composição de pipeline. Marcas e combinações são candidatas, **não arquitetura**." | `101` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | não |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 3` · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-06-VID-015 — `Gravando 2026-07-28 180747.mp4`  ·  cluster promocional

**Tipo:** VÍDEO · **Área:** 06_CONECTORES-MCP
**Hash F0:** `3F844FA66FED4350`   **Hash reconferido:** `3F844FA66FED4350`   **Confere:** sim
**LV:** LV3-V *(LV3-A = `SEM FALA LEXICAL CONFIÁVEL`, 1 palavra, p = 0,751)*
**Cobertura da leitura:** 9 quadros (`101`); ficha STT (12,6 s).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-06-VID-015 · `H-M2-005` (`101`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só divulgação: seis repositórios nomeados por função (equipes especializadas, memória de código, vídeo, pesquisa web, paralelismo, roteamento de modelo), sem demonstração (`101`) | — |
| E03 Maturidade | ND | — | Identificar cada repositório. **Três estão no acervo com ficha própria**: `AC-04-REP-003`, `AC-06-REP-002` e `AC-03-REP-007` |
| E05 Manutenção | ND | — | Verificar atividade na origem dos três não avaliados |
| E06 Segurança ⚠ | ND | — | **Superfície declarada e não inspecionada**; `101` registra "scraping, dependência de agregador, memória persistente, custos e coordenação concorrente" |
| E07 Licença ⚠ | ND | — | Ler a licença dos três repositórios ainda não avaliados |
| E13 Testes/evals | ND | — | Nenhum teste exibido |
| E15 Alegações ⚠ | 1 | Alegações com nomes citados porém não conferidas; `101` registra que "números promocionais **não** foram verificados" | — |

**NF = 1 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça a pergunta de forma genérica: índice de repositórios sem contrato nem escopo | — |
| E04 Transferibilidade | 1 | Só a ideia viaja; três dos seis já têm avaliação própria e mais forte no acervo | — |
| E14 Diferencial | 1 | Conveniência: integra o cluster promocional | — |

**RP = 1 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 8,1 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado **e confirmado** pelos quadros: os três repositórios citados no título estão entre os seis observados (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 180747.mp4` | 8,1 MB | Agency Agents, OpenMontage e OmniRoute | não transcrito"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Agency-Agents, Codebase Memory MCP, OpenMontage, Agent-Reach, Orca e OmniRoute" | `101` (texto visual observado) | ALEGAÇÃO DO AUTOR | **três conferidos por presença no acervo** (`AC-04-REP-003`, `AC-06-REP-002`, `AC-03-REP-007`), três não localizados |
| "**Risco:** scraping, dependência de agregador, memória persistente, custos e coordenação concorrente." | `101` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | não |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4. Metade dos itens citados já tem ficha própria com licença lida; a lacuna dos demais é do cluster, nomeada em `AC-05-VID-009`.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-06-VID-016 — `Gravando 2026-07-28 180942.mp4`  ·  cluster promocional

**Tipo:** VÍDEO · **Área:** 06_CONECTORES-MCP
**Hash F0:** `C9ACFA036D9674D8`   **Hash reconferido:** `C9ACFA036D9674D8`   **Confere:** sim
**LV:** LV3-V *(LV3-A = `SEM FALA LEXICAL CONFIÁVEL`, 1 palavra, p = 0,130)*
**Cobertura da leitura:** 9 quadros (`101`); ficha STT (21,1 s).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-06-VID-016 · `H-M2-005` (`101`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só listagem: oito itens legíveis de uma pilha, por função (método, diagrama, navegador, memória, mídia, criação de extensão). Sem demonstração (`101`) | — |
| E03 Maturidade | ND | — | Identificar cada item. **Cinco estão no acervo**: `AC-03-REP-010`, `AC-07-REP-001`, `AC-06-REP-001`, `AC-05-REP-002` e `AC-04-REP-002` |
| E05 Manutenção | ND | — | Verificar atividade na origem dos não avaliados |
| E06 Segurança ⚠ | ND | — | **Superfície declarada e não inspecionada**; `101` registra o ponto essencial: "**a combinação amplia drasticamente a superfície**; avaliar cada capacidade isoladamente" |
| E07 Licença ⚠ | ND | — | Ler a licença dos itens ainda não avaliados |
| E13 Testes/evals | ND | — | Nenhum teste exibido |
| E15 Alegações ⚠ | 1 | Alegações com nomes citados porém não conferidas; sem critério de seleção declarado | — |

**NF = 1 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça a pergunta de forma genérica: pilha de complementos sem contrato de composição | — |
| E04 Transferibilidade | 1 | Só a ideia viaja; cinco dos oito já têm ficha própria | — |
| E14 Diferencial | 1 | Conveniência: integra o cluster promocional, com sobreposição declarada à área 05 | — |

**RP = 1 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 10,6 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado **e confirmado** pelos quadros: os três itens citados no título estão entre os oito legíveis (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 180942.mp4` | 10,6 MB | Context7, skills de Karpathy e MCP Builder | não transcrito"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "**Risco:** a combinação amplia drasticamente a superfície; avaliar cada capacidade isoladamente e deduplicar com a área 05." | `101` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | — regra seguida: cada capacidade tem ficha própria |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-06-VID-017 — `Gravando 2026-07-28 181016.mp4`

**Tipo:** VÍDEO · **Área:** 06_CONECTORES-MCP
**Hash F0:** `0AEE94B186A0670F`   **Hash reconferido:** `0AEE94B186A0670F`   **Confere:** sim
**LV:** LV3-V *(LV3-A = `SEM FALA LEXICAL CONFIÁVEL`, 1 palavra, p = 0,751)*
**Cobertura da leitura:** 9 quadros (`101`); ficha STT (14,4 s).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-06-VID-017 · `H-M2-005` (`101`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Pipeline exibido em tela com **saída estruturada declarada**: conectar histórico e transcrições, adicionar uma skill, classificar a reunião e gerar resumo, decisões, tarefas, perguntas e próximos passos. Exemplo isolado, sem a skill nem o resultado (`101`) | — |
| E03 Maturidade | ND | — | Identificar o conector e a skill e inspecionar seu estágio |
| E05 Manutenção | ND | — | Localizar o canal de publicação com data |
| E06 Segurança ⚠ | ND | — | **Superfície declarada, crítica e não inspecionada**: `101` impõe "**Gate crítico:** consentimento, retenção, acesso, **dados de clientes**, correção e aprovação de tarefas" — transcrição de reunião contém fala de terceiros |
| E07 Licença ⚠ | ND | — | Ler os termos do conector |
| E13 Testes/evals | ND | — | Nenhuma verificação de que as decisões extraídas correspondem ao que foi dito |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas; nenhum número decisivo em jogo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central com um pipeline **reunião → decisão rastreável**, que é alcance externo com saída estruturada | — |
| E04 Transferibilidade | 3 | O pipeline transfere com adaptação declarada; o conector é substituível | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto no acervo: é o único item que transforma **fala de reunião em itens acionáveis com classificação prévia** | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 9 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado **e confirmado** pelos quadros: "Granola conectado ao Claude para analisar reuniões e vendas" corresponde ao pipeline observado, incluindo o complemento de vendas (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 181016.mp4` | 9,0 MB | Granola conectado ao Claude para analisar reuniões e vendas | não transcrito"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "**Gate crítico:** consentimento, retenção, acesso, dados de clientes, correção e aprovação de tarefas." | `101` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | não |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 3` · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-06-VID-018 — `Gravando 2026-07-28 203600.mp4`  ·  cluster promocional

**Tipo:** VÍDEO · **Área:** 06_CONECTORES-MCP
**Hash F0:** `3388A4CF6D502EB8`   **Hash reconferido:** `3388A4CF6D502EB8`   **Confere:** sim
**LV:** LV3-V *(LV3-A = `SEM FALA LEXICAL CONFIÁVEL`, 2 palavras, p = 0,497)*
**Cobertura da leitura:** 9 quadros (`101`); ficha STT (23,8 s).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-06-VID-018 · `H-M2-005` (`101`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só divulgação: oito repositórios legíveis de dez, por função (pesquisa, compressão, agente pessoal, conversão documental, notebook, gestão). Sem demonstração (`101`) | — |
| E03 Maturidade | ND | — | Identificar cada repositório. **Quatro estão no acervo**: `AC-06-REP-004`, `AC-08-REP-002`, `AC-03-REP-005`, `AC-04-REP-004` e `AC-04-REP-006` — cinco, contando o notebook |
| E05 Manutenção | ND | — | Verificar atividade na origem dos não avaliados |
| E06 Segurança ⚠ | ND | — | **Superfície declarada e não inspecionada**; `101` registra que "**autoaplicação a vagas** e coleta web produzem efeitos externos" |
| E07 Licença ⚠ | ND | — | Ler a licença dos repositórios ainda não avaliados |
| E13 Testes/evals | ND | — | Nenhum teste exibido |
| E15 Alegações ⚠ | 1 | Alegações de crescimento com fonte implícita porém não conferidas; `101` é explícito: "**estrelas e “crescimento” não provam qualidade**". **P-3** aplicado | — |

**NF = 1 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça a pergunta de forma genérica: índice de repositórios ordenado por popularidade, não por função ou contrato | — |
| E04 Transferibilidade | 1 | Só a ideia viaja; cinco dos oito já têm ficha própria e mais forte | — |
| E14 Diferencial | 1 | Conveniência: integra o cluster promocional | — |

**RP = 1 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 9 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado **e confirmado** pelos quadros: os três repositórios citados no título estão entre os oito legíveis (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 203600.mp4` | 9,0 MB | Last30days, MarkItDown, Career Ops e outras ferramentas | não transcrito"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "dez repositórios **em crescimento**" | `101` (texto visual observado) | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA`; **P-3** |
| "Autoaplicação a vagas e coleta web produzem **efeitos externos**." | `101` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | não |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-06-VID-019 — `Gravando 2026-07-28 213625.mp4`

**Tipo:** VÍDEO · **Área:** 06_CONECTORES-MCP
**Hash F0:** `C6E7C78FF5EC4BB8`   **Hash reconferido:** `C6E7C78FF5EC4BB8`   **Confere:** sim
**LV:** LV3-V *(LV3-A = `SEM FALA LEXICAL CONFIÁVEL`, 1 palavra, p = 0,751)*
**Cobertura da leitura:** 9 quadros (`101`); ficha STT (12,6 s).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-06-VID-019 · `H-M2-005` (`101`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só divulgação: cinco repositórios nomeados por função (multimídia, pesquisa, grafo de código, design, minimalismo), sem demonstração (`101`) | — |
| E03 Maturidade | ND | — | Identificar cada repositório e inspecionar seu estágio |
| E05 Manutenção | ND | — | Verificar atividade na origem |
| E06 Segurança ⚠ | ND | — | **Superfície declarada e não inspecionada**: `101` registra que um dos itens é apresentado como **API não oficial** de um produto de terceiro, e outro exigiria baixar e transcrever arquivos |
| E07 Licença ⚠ | ND | — | Ler a licença de cada repositório — e, no caso da API não oficial, também os termos do produto original |
| E13 Testes/evals | ND | — | Nenhum teste exibido |
| E15 Alegações ⚠ | 1 | Alegações de capacidade com nomes citados porém não conferidas | — |

**NF = 1 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça a pergunta de forma genérica: repositórios que **corrigem limitações** do agente, sem contrato nem escopo | — |
| E04 Transferibilidade | 1 | Só a ideia viaja | — |
| E14 Diferencial | 2 | Agregação; dois dos cinco nomes reaparecem em `AC-04-VID-008` e `AC-05-VID-021`, com fichas próprias | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 3,4 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado **e confirmado** pelos quadros: os três repositórios citados no título estão entre os cinco observados (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 213625.mp4` | 3,4 MB | Claude Video, Graphify e Ponytail para corrigir limitações | não transcrito"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "NotebookLM-Py é apresentado como **API não oficial**" | `101` (texto visual observado) | ALEGAÇÃO DO AUTOR | não — **achado de risco registrado**: API não oficial de produto de terceiro é superfície de termos de serviço |
| "Não executar nesta trilha; revisar licença, privacidade e dependências." | `101` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | — regra seguida |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** §9 — relevância aparente com lacuna nomeada e endereçável; teto de V2/V4 respeitado.
**Se EXIGE PESQUISA — lacuna nomeada:** o item apresentado como **API não oficial** de um produto de terceiro — identidade, licença e situação perante os termos do produto original. É o mesmo tipo de exposição já registrado em `AC-04-REP-005`, agora por outro caminho.  **Verificação que a fecharia:** localizar o repositório na origem pública, ler licença e README, e confrontar com os termos de uso do produto que ele acessa.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-06-VID-020 — `Gravando 2026-07-29 090139.mp4`

**Tipo:** VÍDEO · **Área:** 06_CONECTORES-MCP
**Hash F0:** `220CB74C92A0D19E`   **Hash reconferido:** `220CB74C92A0D19E`   **Confere:** sim
**LV:** LV3-V + LV3-A
**Cobertura da leitura:** 9 quadros (`101`); transcrição automática bruta integral (79,0 s, `pt`, 27 segmentos, p = 0,902, **ALTA AUTOMÁTICA** — a mais longa da área). Sem revisão humana.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-06-VID-020 · `H-M2-005` (`101`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Demonstração isolada e não reprodutível, mas **detalhada**: a fala provável descreve a cadeia inteira — conectar o agente ao produto de mídia por uma ferramenta de controle de navegador, instalar skills, selecionar modelo, subir imagem, montar o prompt, ajustar iluminação e tempo. Nenhum arquivo ou configuração acompanha | — |
| E03 Maturidade | ND | — | Identificar o produto e a ferramenta de controle e inspecionar seu estágio |
| E05 Manutenção | ND | — | Localizar o canal de publicação com data |
| E06 Segurança ⚠ | ND | — | **Superfície declarada, crítica e não inspecionada.** A fala provável é explícita: a ferramenta "dá **controle total do meu navegador** para iar", e o agente "consegue **logar na minha conta**, clicar nos botões e ajustar tudo sozinho". Credencial e sessão autenticada operadas por agente, sem controle declarado |
| E07 Licença ⚠ | ND | — | Ler os termos do produto de mídia e da ferramenta de controle |
| E13 Testes/evals | ND | — | Nenhuma verificação do resultado gerado |
| E15 Alegações ⚠ | 0 | A proposta central **depende** de alegações fortes **sem fonte**, inclusive comercial: "o **melhor modelo de vídeo atual**", "o pessoal paga uma fortuna em agência" e "**até 70% de desconto** … ilimitado", com "o preço mais barato do mercado" (LV3-A, 00:00:29 e 00:01:05–00:01:16) | — |

**NF = 1 · 2/7 · 5 ND** *(mediana de [0,2] = 1)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: mostra o alcance externo **operando por navegador em sessão autenticada**, que é a forma mais poderosa e mais arriscada de conector | — |
| E04 Transferibilidade | 2 | O **padrão** (agente orquestrando produto externo por navegador) transfere; a implementação depende de conta, produto e ferramenta específicos | — |
| E14 Diferencial | 2 | Agregação: forma família com `AC-06-VID-001` e `AC-06-VID-013`; o diferencial deste é mostrar a **cadeia de controle**, não só o resultado | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 72,2 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT de 27 segmentos; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado **e confirmado** por duas evidências: os quadros (`101`) e a fala provável, que descreve exatamente a automação do produto de mídia pelo agente (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-29 090139.mp4` | 72,2 MB | Higgsfield automatizado com Claude para gerar vídeos | não transcrito"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "usando essa ferramenta, que dá **controle total do meu navegador** para iar" | LV3-A bruto, 00:00:11,520–00:00:17,400 — **fala provável, não citação exata** | ALEGAÇÃO DO AUTOR | não — **achado de superfície registrado** |
| "Aí o cloud consegue **logar na minha conta**, clicar nos botões e ajustar tudo sozinho" | LV3-A bruto, 00:00:17,400–00:00:23,800 — fala provável | ALEGAÇÃO DO AUTOR | não — sessão autenticada operada por agente |
| "com até **70% de desconto** no “Occidense” ilimitado… É literalmente **o preço mais barato do mercado**." | LV3-A bruto, 00:01:09,140–00:01:16,520 — fala provável | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA`; **alegação comercial**, sustenta `E15 = 0` |
| "é um **sistema automático** rodando dentro do cloud e do Higgs Field" | LV3-A bruto, 00:00:57,800–00:01:05,160 — fala provável | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |

> O motor grafou "Higgs Field", "iar" e "Occidense"; nomes de produto **não** foram normalizados (`117`, regra de uso).

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |
| **V7** | **sim** | `E15 = 0` e a proposta depende das alegações comerciais → teto EXIGE PESQUISA |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** V7 (§8) — teto EXIGE PESQUISA.
**Se EXIGE PESQUISA — lacuna nomeada:** (1) o **desconto e a alegação de preço**, que são comerciais e podem envolver vínculo de afiliação não declarado no vídeo; (2) a ferramenta que dá "controle total do navegador" — identidade, escopo e o que ocorre com a credencial da conta operada.  **Verificação que a fecharia:** identificar a ferramenta de controle na origem pública e ler seu escopo de permissão; e tratar a oferta comercial como material promocional, não como dado de custo.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-06-VID-021 — `Gravando 2026-07-29 091727.mp4`  ·  cluster promocional

**Tipo:** VÍDEO · **Área:** 06_CONECTORES-MCP
**Hash F0:** `6397C8A308AC9CAA`   **Hash reconferido:** `6397C8A308AC9CAA`   **Confere:** sim
**LV:** LV3-V *(LV3-A = `SEM FALA LEXICAL CONFIÁVEL`, 1 palavra, p = 0,751)*
**Cobertura da leitura:** 9 quadros (`101`); ficha STT (11,3 s).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-06-VID-021 · `H-M2-005` (`101`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Mapa exibido em tela de **16 capacidades**, separadas em skills de formato de arquivo, ferramentas de criação e conectores corporativos. Exemplo isolado, sem escopo por item (`101`) | — |
| E03 Maturidade | ND | — | Confirmar em fonte primária quais das 16 existem e em que versão |
| E05 Manutenção | ND | — | Localizar o canal de publicação com data |
| E06 Segurança ⚠ | ND | — | **Superfície declarada, crítica e não inspecionada**; `101` é literal: "**Risco crítico:** pagamentos, código, tickets, mensagens e automação; **“instalar tudo” é antipadrão**" |
| E07 Licença ⚠ | ND | — | Ler os termos de cada conector |
| E13 Testes/evals | ND | — | Nenhum teste exibido |
| E15 Alegações ⚠ | 1 | Alegação numérica de existência (16 capacidades) com fonte implícita porém não conferida contra documentação primária | — |

**NF = 1 · 2/7 · 5 ND** *(mediana de [1,2] = 1,5 → §14.3 vale o inferior)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: mapeia **as superfícies empresariais alcançáveis** em um só quadro — que é a pergunta da área, ainda que sem escopo | — |
| E04 Transferibilidade | 2 | O **mapa de superfícies** transfere; os itens são de um produto específico e datados | — |
| E14 Diferencial | 1 | Conveniência: integra o cluster promocional; o mesmo mapa aparece em `AC-06-PRT-013` e `AC-05-VID-013` | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 2,2 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado **e confirmado** pelos quadros: "skills de arquivos e conectores para trabalho e negócio" corresponde às três famílias observadas (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-29 091727.mp4` | 2,2 MB | skills de arquivos e conectores para trabalho e negócio | não transcrito"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "**Risco crítico:** pagamentos, código, tickets, mensagens e automação; “instalar tudo” é antipadrão." | `101` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | não — converge com a regra "menu, not a shopping spree" de `AC-06-PRT-008` |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-06-VID-022 — `Gravando 2026-07-29 092123.mp4`  ·  cluster promocional

**Tipo:** VÍDEO · **Área:** 06_CONECTORES-MCP
**Hash F0:** `C32CFE23278948B9`   **Hash reconferido:** `C32CFE23278948B9`   **Confere:** sim
**LV:** LV3-V *(LV3-A = `SEM FALA LEXICAL CONFIÁVEL`, 2 palavras, p = 0,964 — confiança alta sobre duas palavras, sem valor lexical)*
**Cobertura da leitura:** 9 quadros (`101`); ficha STT (15,4 s).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-06-VID-022 · `H-M2-005` (`101`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só divulgação: cinco repositórios nomeados, dos quais `101` observa que **quatro já apareceram** neste lote ou na área 05. Sem demonstração | — |
| E03 Maturidade | ND | — | Identificar cada repositório. **Dois estão no acervo**: `AC-04-REP-003` e `AC-06-REP-002` |
| E05 Manutenção | ND | — | Verificar atividade na origem dos não avaliados |
| E06 Segurança ⚠ | ND | — | **Superfície declarada, crítica e não inspecionada**: um dos cinco é monitor de mercado. `101` adverte: "**não confundir análise com autorização para operar**" |
| E07 Licença ⚠ | ND | — | Ler a licença dos repositórios ainda não avaliados |
| E13 Testes/evals | ND | — | Nenhum teste exibido |
| E15 Alegações ⚠ | 1 | Alegações com nomes citados porém não conferidas; sem critério de seleção declarado | — |

**NF = 1 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça a pergunta de forma genérica: índice de repositórios de ampliação, sem contrato | — |
| E04 Transferibilidade | 1 | Só a ideia viaja; dois dos cinco já têm ficha própria | — |
| E14 Diferencial | 0 | **Reprodutível em horas com ferramenta já disponível**: `101` registra que quatro dos cinco são repetição dentro do mesmo lote | — |

**RP = 1 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 6,6 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado **e confirmado** pelos quadros: "cinco repositórios que ampliam agentes com skills e internet" corresponde ao observado (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-29 092123.mp4` | 6,6 MB | cinco repositórios que ampliam agentes com skills e internet | não transcrito"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "**Deduplicação:** quatro já aparecem neste lote ou na área 05." | `101` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | **conferida** entre as fichas |
| "O monitor de mercado é candidato de **alto risco**; não confundir análise com autorização para operar." | `101` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | não |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`. **`E01 = 2` (≠ 0)**, portanto não cabe REJEITADO, apesar de `E14 = 0`.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-06-VID-023 — `Gravando 2026-07-29 092344.mp4`  ·  ⚠ efeito externo irreversível

**Tipo:** VÍDEO · **Área:** 06_CONECTORES-MCP
**Hash F0:** `7C9FA64467DCA0AA`   **Hash reconferido:** `7C9FA64467DCA0AA`   **Confere:** sim
**LV:** LV3-V + LV3-A
**Cobertura da leitura:** 9 quadros (`101`); transcrição automática bruta integral (33,0 s, `pt`, 7 segmentos, p = 0,890, **ALTA AUTOMÁTICA**). Sem revisão humana.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-06-VID-023 · `H-M2-005` (`101`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Demonstração isolada com mecanismo declarado: um gateway local em contêiner, conectado por MCP, expondo cerca de 40 ferramentas de mensageria ao agente. A fala provável descreve a instalação em um comando e o envio de mensagem, inclusive **disparo para lista de contatos**. Nenhum arquivo ou configuração acompanha | — |
| E03 Maturidade | ND | — | Identificar o projeto e inspecionar seu estágio |
| E05 Manutenção | ND | — | Localizar o repositório de origem e verificar atividade datada |
| E06 Segurança ⚠ | ND | — | **Superfície declarada, a mais consequente da área, e não inspecionada.** `101` é literal: "**Risco crítico:** mensagens são **efeitos externos irreversíveis**; exigir opt-in, identidade, aprovação, auditoria, limites, privacidade, **política anti-spam** e conformidade com termos". Resolveria inspecionar o projeto e o escopo das ~40 ferramentas expostas |
| E07 Licença ⚠ | ND | — | Ler a licença do projeto na origem |
| E13 Testes/evals | ND | — | Nenhum teste exibido; nenhum limite de taxa ou confirmação demonstrado |
| E15 Alegações ⚠ | 2 | Alegações numéricas **com fonte citada e conferível, ainda não conferida**: "quase **40 ferramentas** de WhatsApp" e "**tudo self-hosted**, seus dados ficam no seu computador" — verificáveis no repositório público do projeto nomeado | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central no ponto de maior consequência: **comunicação com pessoas reais**, que é alcance externo irreversível | — |
| E04 Transferibilidade | 2 | O **padrão** (gateway local expondo canal por MCP) transfere; a implementação depende do projeto e de conta pessoal | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto no acervo: é o único item que mostra um canal de mensagem **bidirecional e auto-hospedado** ligado a um agente | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 26,7 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT de 7 segmentos; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado **e confirmado** por duas evidências: os quadros (`101`) e a fala provável, que nomeia o projeto e descreve a ponte MCP (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-29 092344.mp4` | 26,7 MB | OpenWA como MCP de WhatsApp para Claude | não transcrito"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Ele se chama OpenWare e sobe em um API de WhatsApp no seu próprio computador, **de graça**." | LV3-A bruto, 00:00:03,720–00:00:08,800 — **fala provável, não citação exata** (o motor grafou "OpenWare") | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "O Cloud enxerga **quase 40 ferramentas** de WhatsApp e passa a operar tudo por você." | LV3-A bruto, 00:00:17,480–00:00:22,260 — fala provável | ALEGAÇÃO DO AUTOR | não — **conferível** no repositório do projeto |
| "Depois é só pedir no chat para mandar mensagem, avisar no grupo ou **disparar para uma lista de contatos**." | LV3-A bruto, 00:00:22,260–00:00:27,520 — fala provável | ALEGAÇÃO DO AUTOR | não — **achado de risco registrado**: disparo em lista é exatamente o caso que exige política anti-spam e consentimento |
| "Tudo self-hosted, seus dados ficam no seu computador, sem depender de API paga por fora." | LV3-A bruto, 00:00:27,520–00:00:32,400 — fala provável | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` (crítico, mas **não confirmado por inspeção**) · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 2` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** §9 — relevância aparente com lacuna nomeada e endereçável; teto de V2/V4 respeitado.
**Se EXIGE PESQUISA — lacuna nomeada:** identidade, licença e **escopo das ~40 ferramentas** que o gateway expõe ao agente — em particular quais produzem efeito externo irreversível (envio, disparo em lista, entrada em grupo) e se existe confirmação, limite de taxa ou trilha de auditoria.  **Verificação que a fecharia:** localizar o repositório na origem pública, ler licença e a lista de ferramentas expostas, e confrontar com os termos de uso da plataforma de mensagem — **sem instalar nem conectar conta**.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

## Fechamento da área 06

| Métrica | Valor |
|---|---:|
| Itens representados | 40 / 40 |
| Fichas válidas contra `04` §13 | 40 |
| Hashes / estruturas reconferidos · divergentes | 40 · **0** |
| Itens em **LV4** | 4 (os 4 repositórios) |
| `RF = CANDIDATO FORTE` | 0 |
| `RF = CANDIDATO A PILOTO` | 1 — AC-06-REP-003 |
| `RF = PADRÃO A ESTUDAR` | 0 |
| `RF = EXIGE PESQUISA` | 9 |
| `RF = REFERÊNCIA` | 30 |
| `RF = INDETERMINADO` | 0 |
| Total de eixos possíveis (40 × 15) | 600 |
| Eixos determinados | 417 |
| Eixos em `ND` | **183 (30,5%)** *(recontado por ferramenta sobre as fichas em 2026-07-29; o valor anterior, 207, era estimativa e foi corrigido — ver `99_RELATORIO-DA-FASE-2.md` §6)* |
| Divergências catálogo × fonte | **0 divergentes** · **6 parciais** (PRT-008, PRT-012, VID-002, VID-007, mais as grafias divergentes em VID-008 e a inconsistência de versão em REP-002) |

**Achados registrados nesta área, sem resolução silenciosa:**

1. **Três casos de contorno de controle de terceiro**, em graus diferentes de evidência: `AC-06-REP-002` **declara** o roteamento em torno de bloqueio de plataforma como funcionalidade (`E06 = 1`, V2 disparada); `AC-06-VID-008` retrata um navegador apresentado como capaz de "parecer humano e contornar detecção" (`E06 = ND` — **não** rejeitado, porque §9 exige evidência, não alegação de terceiro); `AC-06-VID-019` retrata uma **API não oficial** de produto de terceiro.
2. **Dois casos de sessão autenticada operada por agente**: `AC-06-REP-004` ("bring your own keys **and browser sessions**") e `AC-06-VID-020` ("controle total do meu navegador… **logar na minha conta**"). Nenhum dos dois declara controle, limite ou auditoria.
3. **Um caso de efeito externo irreversível**: `AC-06-VID-023` — disparo de mensagem para lista de contatos por agente, sem confirmação nem limite demonstrados.
4. **Assimetria registrada entre o que o material recomenda e o que ele controla:** os prints `AC-06-PRT-009` e `AC-06-PRT-011` enunciam os únicos controles explícitos da área — aprovação humana no envio e somente-leitura em finanças —, e **nenhum** dos 23 vídeos exibe implementação de controle equivalente.
5. **`AC-06-REP-004` traz o único portão de qualidade quantificado do acervo inteiro** — cobertura mínima de 84% com baseline datado e regra escrita de não rebaixamento — e ainda assim o diretório de testes declarado não está na raiz efetiva.
6. **Duas contagens de versão inconsistentes** dentro da mesma fonte: `AC-06-REP-002` (`1.5.0` no manifesto × `1.3.1` no changelog).

Nenhuma fonte foi modificada. Nenhum repositório foi executado, instalado ou importado. Nenhuma conta foi conectada. Nenhum item foi adotado, ordenado, priorizado ou recomendado.
