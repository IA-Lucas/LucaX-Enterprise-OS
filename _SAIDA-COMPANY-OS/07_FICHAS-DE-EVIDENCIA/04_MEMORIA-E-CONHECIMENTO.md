> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

# FICHAS DE EVIDÊNCIA — ÁREA 04 — MEMÓRIA E CONHECIMENTO

**Fase:** 2 — Extração · **Data:** 2026-07-29 · **Avaliador:** Claude Opus 5 (Fase 2)
**Itens:** 32 — 7 REPO · 13 PRINT · 12 VÍDEO · 0 PLANILHA
**Convenções de aplicação:** `00_INDICE-DA-FASE-2.md` §3

**Pergunta central da área (base de E01):** *como o sistema lembra, indexa e recupera.*

**Cobertura padrão dos REPO desta área** (teto de `05` §8): listagem da raiz efetiva · texto de `LICENSE` · `README` (até 6 KB do início, total declarado) · manifesto de dependências · `CHANGELOG` quando presente · listagem do diretório de testes · sinais de instalação e segurança. **Código-fonte não lido em massa; nada executado ou instalado.**

---

### AC-04-REP-001 — `ai-second-brain-main`

**Tipo:** REPO · **Área:** 04_MEMORIA-E-CONHECIMENTO
**Hash F0:** `dir · 10 arq.`   **Hash reconferido:** `10 arq. · aninhamento 0`   **Confere:** sim
**LV:** LV4
**Cobertura da leitura:** raiz efetiva `ai-second-brain-main` — **listagem completa dos 10 arquivos**; `LICENSE` (MIT, 1.070 bytes, "Copyright (c) 2026 Charlie Hills"); `README.md` (6.373 bytes, lidos 6 KB: instalação, fluxo de três etapas, pré-requisitos, frases de gatilho, FAQ, créditos); `SKILL.md` (frontmatter e início do corpo); `CHANGELOG.md` (`[1.0.0] — 2026-04-17`). **Não lidos por inteiro:** `ai-second-brain.skill`, `render-social-preview.js`, `social-preview.html`.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** não se aplica

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 3 | Artefato completo e inspecionável correspondente à afirmação (`SKILL.md` com frontmatter e gatilhos, `ai-second-brain.skill`, fluxo em três etapas com diagrama mermaid), **sem** procedimento de verificação declarado na fonte | — |
| E03 Maturidade | 3 | Versionado com changelog presente: `CHANGELOG.md` com `[1.0.0] — 2026-04-17` e o conteúdo da versão inicial. Sem tag ou release adicional observável | — |
| E05 Manutenção | 3 | Atividade identificável por evidência datada dentro da fonte (`2026-04-17`) e canal de atualização declarado (`git pull`, com o FAQ prometendo atualizações). **Não alcança 4**: há responsável nomeado, mas uma única entrada de changelog não estabelece cadência | — |
| E06 Segurança ⚠ | ND | — | **Ler por inteiro os 10 arquivos** procurando credencial, segredo ou instrução destinada a subverter o leitor (§14.1). Três arquivos permaneceram não lidos. A superfície declarada é relevante: o fluxo pede Acesso Total ao Disco no macOS, conexão a Gmail e login em navegador |
| E07 Licença ⚠ | 4 | Permissiva padrão presente e íntegra na raiz efetiva: MIT, 1.070 bytes, titular nomeado. Cópia local não prova titularidade → teto 4 | — |
| E13 Testes/evals | 0 | **Inspecionado com listagem completa da raiz: nenhum teste, eval ou verificação de qualquer natureza** entre os 10 arquivos | — |
| E15 Alegações ⚠ | 1 | Alegações numéricas fortes com fonte citada, porém não conferida e não conferível com o material disponível: "the X thread about it hit **16 million views**" (com link para o gist original) e "a creator with **200k+ LinkedIn followers**" | — |

**NF = 3 · 6/7 · 1 ND** *(mediana dos determinados [0,1,3,3,3,4] = 3)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 4 | Endereça diretamente a pergunta central — como o sistema lembra e recupera — **mais** artefato concreto e reutilizável (§14.2): `SKILL.md` com frontmatter, gatilhos declarados e procedimento em três etapas | — |
| E04 Transferibilidade | 4 | Transferível por configuração, sem alteração de código: clonar para o diretório de skills e invocar por frase. Limitação de plataforma declarada (etapa 3b só em macOS) impede a nota 5 | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto **dentro do acervo**: é o único item que sustenta explicitamente a tese "pasta de markdown + LLM basta, sem banco vetorial" — o extremo oposto de `AC-04-REP-005` | — |

**RP = 4 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 5 | Item documental (§14.1): não requer instalação de runtime **e** o artefato declara como é consumido — host (Claude Code), formato (skill em `~/.claude/skills/`) e ponto de entrada (frases de gatilho listadas no README e no frontmatter) | — |
| E09 Custo | 4 | Custo marginal: apenas chamadas de modelo já previstas; Obsidian é declarado gratuito; o FAQ afirma que nada sai da máquina além das chamadas que o próprio agente já faz | — |
| E10 Contexto/tokens | 4 | Medido: **10 arquivos, 579 KB** — menos de 50 arquivos e menos de 1 MB, com superfície delimitada pelo `SKILL.md` | — |
| E11 Fornecedor | 4 | Abstração documentada: o dado fica em Markdown local em um vault; conectores (Gmail, NotebookLM, Granola) são opcionais e declarados etapa a etapa | — |
| E12 Reversibilidade | 5 | Reversível por remoção, sem efeito residual, **e a reversão está documentada pelo próprio autor**: o FAQ traz `rm -rf ~/.claude/skills/ai-second-brain` e afirma que isso "does **not** touch your Obsidian vault, raw folder, or wiki" | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (skill que guia a construção a partir do histórico de ChatGPT e Claude, empacota o gist de Karpathy de abril/2026, "só 10 arquivos") e **todos** os detalhes conferem: os 10 arquivos foram contados, e o README credita explicitamente o gist de 3 de abril de 2026.
**O que o catálogo afirma:** "Skill que guia a construção de uma base de conhecimento pessoal a partir do histórico de ChatGPT e Claude. Empacota a ideia do gist de Andrej Karpathy (abril/2026…) mais um organizador de histórico e um fluxo de slash commands… Só 10 arquivos — leitura rápida."
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Within 48 hours the X thread about it hit **16 million views**." | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA`; **P-3**: popularidade não move eixo |
| "Does this send my data anywhere? **No.** Everything lives in folders on your Mac." | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — os três arquivos restantes não foram lidos; sustenta `E06 = ND` |
| "None of the underlying ideas are mine." | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não |
| "É a alternativa mais barata ao RAG e merece ser considerada seriamente antes de montar infraestrutura." | `_CONTEUDO.md` área 04 | ALEGAÇÃO DO CATÁLOGO | não |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V4 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 = 4` · `LV = 4` · 1 ND · `E15 = 1` (≠ 0) · reconferência confere |
| **V2** | **sim** | `E06 = ND` → teto PADRÃO A ESTUDAR / REFERÊNCIA / EXIGE PESQUISA |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** V2 (§8) fecha as duas classificações de candidato; §9, condição de entrada de EXIGE PESQUISA — relevância aparente com lacuna nomeada e endereçável.
**Se EXIGE PESQUISA — lacuna nomeada:** `E06` — três dos dez arquivos não foram lidos, e o fluxo pede Acesso Total ao Disco, conexão a Gmail e login em navegador.  **Verificação que a fecharia:** ler por inteiro `ai-second-brain.skill`, `render-social-preview.js` e `social-preview.html` procurando credencial, segredo ou instrução de subversão — leitura pequena, dentro do teto de `05` §8.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-04-REP-002 — `claude-mem-main`

**Tipo:** REPO · **Área:** 04_MEMORIA-E-CONHECIMENTO
**Hash F0:** `dir · 850 arq. · aninhado`   **Hash reconferido:** `850 arq. · aninhamento 1`   **Confere:** sim
**LV:** LV4
**Cobertura da leitura:** raiz efetiva `claude-mem-main/claude-mem-main` (40 entradas); `LICENSE` — Apache License 2.0, 11.358 bytes, íntegro; `README.md` (17.179 bytes, lidos 6 KB: i18n em 32 idiomas, badges, proposta, quick start com quatro caminhos de instalação); `package.json` (nome, versão `13.11.0`, autor, licença, `files[]`); `CHANGELOG.md` (`[13.11.0] - 2026-07-13`, com a retirada do daemon `cloud-sync.mjs`); `.claude-plugin/`; `tests/` — 213 arquivos, subdiretórios listados; `SECURITY.md`, `NOTICE`, `docker-compose.yml`. **Não lidos:** `src/`, `plugin/`, `ragtime/`, `docs/`.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** não se aplica

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 4 | Artefato completo e inspecionável (hooks, plugin, `ragtime/`, CLI, Docker) **mais** procedimento de verificação declarado: `tests/` com **213 arquivos** organizados em `cli`, `compat`, `context`, `core`, `hooks`, `infrastructure`, `integration`, `sdk`, **`security`** e `server`, mais `docker-compose.e2e.yml` | — |
| E03 Maturidade | 4 | Versionado com release identificável (`"version": "13.11.0"`, `CHANGELOG.md`) **mais** documentação de instalação e uso (quatro caminhos declarados, docs em 32 idiomas) **mais** tratamento de erro visível na configuração: o changelog descreve *debounce* de 1,5 s, *single-flight flush*, timeout de 30 s e *backoff* exponencial limitado | — |
| E05 Manutenção | 4 | Atividade recente por evidência datada dentro da fonte (`CHANGELOG.md`, `[13.11.0] - 2026-07-13` — dezesseis dias antes desta avaliação) **mais** responsável nomeado (`"author": "Alex Newman"`) **mais** canal de reporte declarado (`bugs.url`, `SECURITY.md`) | — |
| E06 Segurança ⚠ | 3 | Superfície declarada (hooks que capturam uso de ferramenta e transcrições, sincronização para serviço externo `cmem.ai`, credenciais migradas de `.cloud-sync.env`) **com controles parciais documentados**: `SECURITY.md`, diretório de testes `security`, `NOTICE`, e o próprio changelog descrevendo o runbook de migração de credencial. **Código não lido** | — |
| E07 Licença ⚠ | 4 | Permissiva padrão presente e íntegra: Apache License 2.0 (11.358 bytes) mais `NOTICE`; `"license": "Apache-2.0"` no `package.json`. Cópia local não prova titularidade → teto 4 | — |
| E13 Testes/evals | 3 | `tests/` inspecionado: 213 arquivos com ponto de entrada declarado por `bunfig.toml`/`package.json` e cobertura de integração e segurança. Nenhum eval de comportamento de agente identificado na listagem | — |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas no trecho lido ("seamlessly preserves context across sessions"); os números presentes são badges de versão e de tendência, que não sustentam a proposta. **P-3** aplicado aos badges | — |

**NF = 4 · 7/7 · 0 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 4 | Endereça diretamente a pergunta central — o que o agente lembra entre sessões — **mais** artefato concreto: hooks de captura, ferramentas MCP de busca e um módulo de recuperação (`ragtime/`) | — |
| E04 Transferibilidade | 4 | Transferível por configuração, sem alteração de código: `npx claude-mem install`, com variantes `--ide opencode` e `--ide antigravity`, ou instalação por marketplace | — |
| E14 Diferencial | 4 | Sem equivalente pronto no acervo **mais** custo alto de reconstrução: a captura por **hook** — o agente não precisa "lembrar de lembrar" — com compressão semântica e busca posterior é curadoria acumulada em 13 versões maiores | — |

**RP = 4 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 4 | Instalação declarada em um comando (`npx claude-mem install`), configuração por arquivo. Não alcança 5: exige harness hospedeiro e, para sincronização, serviço externo | — |
| E09 Custo | 3 | Custo variável por uso, com controle possível: o produto é Apache-2.0 e local, mas a sincronização para `cmem.ai` implica serviço externo cujo modelo de cobrança não é declarado no trecho lido | — |
| E10 Contexto/tokens | 2 | Medido: **850 arquivos, 16,6 MB** — contagem na faixa 300–1.000 e tamanho na faixa 5–20 MB; as duas fecham a âncora 2 | — |
| E11 Fornecedor | 4 | Abstração de fornecedor documentada: três IDEs suportados por flag de instalação, mais plugin de marketplace; troca por configuração | — |
| E12 Reversibilidade | 2 | **Reversível com perda de estado ou de histórico**: o produto é uma memória persistente; remover a instalação descarta o acervo de observações acumuladas, e o changelog registra sincronização de linhas não enviadas | — |

**AA = 3 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (850 arquivos, hooks, plugin, Docker, módulo `ragtime`, documentação em português, programa Vercel OSS) e **todos** os detalhes conferem: a contagem bate com a reconferência estrutural, `ragtime/` e `docker/` estão na raiz, o link `docs/i18n/README.pt-br.md` aparece no README e o badge do programa Vercel OSS está no cabeçalho.
**O que o catálogo afirma:** "850 arquivos. Camada de memória com hooks, plugin, Docker e um módulo chamado `ragtime`. Tem documentação em português (`docs/i18n/README.pt-br.md`). Programa Vercel OSS. **O que extrair:** como a memória é capturada por *hook* em vez de por chamada explícita."
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Claude-Mem seamlessly preserves context across sessions by automatically capturing tool usage observations, generating semantic summaries…" | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — `src/` não lido |
| "The worker now syncs memories itself — every local write nudges a background flusher that drains unsynced rows to **cmem.ai**" | `CHANGELOG.md` da fonte | ALEGAÇÃO DO AUTOR | não. **Registrado como achado**: há fluxo de dados para serviço externo por padrão, com credencial própria |
| Badges "Mentioned in Awesome Claude Code", Trendshift e Star History | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA`; **P-3** |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V2 · V3 · V4 · V5 · V6 · V7 · V8 | **nenhuma** | `E06 = 3` · `E07 = 4` · `LV = 4` · 0 ND · `E15 = 3` · reconferência confere |

#### Resultado
**RF = CANDIDATO FORTE**
**Regra que produziu:** §9, condições de entrada satisfeitas: `LV = 4` · nenhum eixo do Bloco A abaixo de 3 · `E06 = 3` · `E07 = 4` · **0 ND** · `RP = 4`.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> **CANDIDATO FORTE não significa adotar.** Restrições registradas na própria ficha: `E12 = 2` (memória persistente, reversão com perda) e fluxo declarado de dados para serviço externo.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-04-REP-003 — `codebase-memory-mcp-main`

**Tipo:** REPO · **Área:** 04_MEMORIA-E-CONHECIMENTO
**Hash F0:** `dir · 1829 arq. · aninhado`   **Hash reconferido:** `1829 arq. · aninhamento 1`   **Confere:** sim
**LV:** LV4
**Cobertura da leitura:** raiz efetiva `codebase-memory-mcp-main/codebase-memory-mcp-main` (34 entradas); `LICENSE` — MIT, 1.107 bytes, "Copyright (c) 2025 DeusData", íntegro; `README.md` (**41.814 bytes**, lidos 6 KB: badges, proposta, seção de pesquisa com o preprint, seção "Security & Trust", diferenciais, instalação em uma linha para três sistemas); `tests/` — 173 arquivos, topo listado; sinais `SECURITY.md`, `install.sh`, `install.ps1`, `.gitleaksignore`, `THIRD_PARTY.md`, `DCO`, `MAINTAINERS.md`. **Não lidos:** `src/`, `internal/`, `pkg/`, `graph-ui/`, `vendored/`, `docs/`. **Este é o item de 1,23 GB apontado como risco R-04 na calibração — o teto de leitura foi respeitado.**
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** não se aplica

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 4 | Artefato completo e inspecionável (binário estático, 14 ferramentas MCP, gramáticas vendorizadas, UI de grafo) **mais** procedimento de verificação declarado: `tests/` com 173 arquivos, incluindo `scale_contract.sh`, `smoke_guard.sh` e casos de regressão, além de workflow de CI. **Não alcança 5**: a reprodução exigiria LV5, que esta frente não pode atingir | — |
| E03 Maturidade | 4 | Versionado com release identificável (badge de GitHub Release, `Formula` para Homebrew, binários por plataforma) **mais** documentação de instalação e uso para três sistemas **mais** tratamento de erro visível na configuração: o `README` antecipa a política de execução do PowerShell e a Mark-of-the-Web, com passos de contorno | — |
| E05 Manutenção | ND | — | Nenhum `CHANGELOG` na raiz efetiva e nenhuma data observada no trecho lido. Resolveria consultar a página de releases na origem pública `DeusData/codebase-memory-mcp` |
| E06 Segurança ⚠ | 4 | Superfície **delimitada e declarada explicitamente** ("This tool reads your codebase and writes to your agent configuration files. That is what it is designed to do") **mais** controles documentados (`SECURITY.md`, `.gitleaksignore`, `THIRD_PARTY.md`, `DCO`, binários assinados e com checksum) **mais** escopo de permissão explícito (processamento 100% local, sem chave de API). **Não alcança 5**: os selos de verificação independente (OpenSSF Scorecard, SLSA 3, VirusTotal) são badges não conferidos por esta frente | — |
| E07 Licença ⚠ | 4 | Permissiva padrão presente e íntegra: MIT, 1.107 bytes, titular nomeado. Cópia local não prova titularidade → teto 4 | — |
| E13 Testes/evals | 3 | `tests/` inspecionado: 173 arquivos em C, com scripts de contrato de escala e guarda de fumaça, e `Makefile.cbm` como ponto de entrada. **Não elevado a 4**: os evals de qualidade de resposta existem apenas como **alegação** do preprint, que não foi lido — pontuar 4 aqui seria pontuar alegação (A-5) | — |
| E15 Alegações ⚠ | 2 | Alegações numéricas fortes **com fonte citada e conferível, ainda não conferida**: "83% answer quality, 10× fewer tokens, 2.1× fewer tool calls" e "Evaluated across 31 real-world repositories" vêm com referência formal — preprint **arXiv:2603.27277** —, que é público e conferível, mas não foi lido nesta fase. Também não conferidos: "5604 tests passing", "158 languages", "120x fewer tokens", "28M LOC in 3 minutes" | — |

**NF = 4 · 6/7 · 1 ND** *(mediana dos determinados [2,3,4,4,4,4] = 4)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 4 | Endereça diretamente a pergunta central — como indexar e recuperar — **mais** artefato concreto: grafo persistente de funções, classes, cadeias de chamada, rotas HTTP e vínculos entre serviços, exposto por 14 ferramentas MCP | — |
| E04 Transferibilidade | 4 | Transferível por configuração, sem alteração de código: binário estático único por plataforma, `install` que autodetecta os agentes e escreve as entradas MCP | — |
| E14 Diferencial | 4 | Sem equivalente pronto no acervo **mais** custo alto de reconstrução: gramáticas tree-sitter para 158 linguagens compiladas no binário, mais resolução semântica híbrida por LSP — conhecimento de domínio que nenhum outro item do acervo se aproxima de oferecer | — |

**RP = 4 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 4 | Instalação declarada em um comando (`curl … \| bash` no macOS/Linux; três passos no Windows), configuração automática por agente detectado. **Não alcança 5** por escrever em arquivos de configuração de agente — estado fora do próprio artefato | — |
| E09 Custo | 5 | Sem custo recorrente: roda sobre recurso já existente, sem chave de API, sem Docker e sem dependência de runtime, conforme declarado e coerente com o formato de binário estático | — |
| E10 Contexto/tokens | **0** | Medido: **1.829 arquivos, 1,23 GB** — o maior item do acervo por volume. Tamanho **muito acima** de 100 MB; a contagem sozinha fecharia a âncora 1, mas vale a pior das duas | — |
| E11 Fornecedor | 5 | Sem dependência de fornecedor: roda local, sobre o padrão aberto MCP, com 11 agentes suportados e sem serviço remoto obrigatório | — |
| E12 Reversibilidade | 3 | Reversível por remoção, com efeitos colaterais **documentados**: o próprio README declara que o instalador escreve nos arquivos de configuração dos agentes, o que exige reversão explícita | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (indexação do kernel do Linux em 3 minutos, consulta estrutural em menos de 1 ms, tree-sitter em 158 linguagens, LSP híbrido, 14 ferramentas MCP, binário único, e os números do preprint com a referência arXiv) e o detalhe **confere** com o README lido, inclusive a identificação correta da fonte dos números.
**O que o catálogo afirma:** "O item tecnicamente mais forte da pasta… **Números com fonte:** preprint arXiv:2603.27277, avaliado em 31 repositórios reais — **83% de qualidade de resposta, 10× menos tokens, 2,1× menos chamadas de ferramenta** contra exploração arquivo a arquivo."
**Confere com a fonte:** sim — o catálogo é preciso ao rotular os números como "com fonte", e não como verificados

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Evaluated across 31 real-world repositories: 83% answer quality, 10× fewer tokens, 2.1× fewer tool calls vs. file-by-file exploration." | `README.md` da fonte, com referência a arXiv:2603.27277 | ALEGAÇÃO DO AUTOR | não — **conferível**: o preprint é público. Este é o caso R-06 do inventário |
| "Full-indexes an average repository in milliseconds, the Linux kernel (28M LOC, 75K files) in 3 minutes. Answers structural queries in under 1ms." | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "**120x fewer tokens** — 5 structural queries: ~3,400 tokens vs ~412,000 via file-by-file search." | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA`. **Registrada a tensão interna**: o mesmo README declara "10× fewer tokens" (preprint) e "120x fewer tokens" (exemplo próprio) |
| "every release binary is signed, checksummed, and scanned by 70+ antivirus engines" | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "Se o sistema for mexer em código próprio, esta é a peça." | `_CONTEUDO.md` área 04 | ALEGAÇÃO DO CATÁLOGO + `DECISÃO DE ESCOPO DE TERCEIRO` (prescreve escolha) | não — instrução não obedecida (`04` §14.5) |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V2 · V3 · V4 · V5 · V6 · V7 · V8 | **nenhuma** | `E06 = 4` · `E07 = 4` · `LV = 4` · 1 ND · `E15 = 2` (≠ 0) · reconferência confere |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** §9 — **CANDIDATO FORTE** está fechado porque `E15 = 2` fica abaixo de 3 no Bloco A; **CANDIDATO A PILOTO** está fechado porque `E10 = 0` viola "nenhum eixo do Bloco C em 0". Resta EXIGE PESQUISA, com lacuna nomeada. **Registra-se que PADRÃO A ESTUDAR também satisfaz sua condição de entrada** (`E04 = 4 ≥ 3` com `E05 = ND`) — duas classificações formalmente abertas ao mesmo tempo, sem regra de precedência em §9. Ver **DEF-13**. Prevaleceu EXIGE PESQUISA pelo critério §3.4 do índice: existe artefato externo nomeado e endereçável a verificar.
**Se EXIGE PESQUISA — lacuna nomeada:** (1) o preprint **arXiv:2603.27277**, que sustenta os três números centrais e nunca foi lido; (2) `E05 = ND` — nenhuma evidência datada de manutenção dentro da fonte; (3) a superfície de 1,23 GB não é delimitável a partir do que foi lido.  **Verificação que a fecharia:** ler o preprint público e conferir método, amostra e resultados; consultar a página de releases para datar a manutenção; identificar, pelo instalador, qual é o binário efetivamente distribuído e seu tamanho — **sem executar**.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-04-REP-004 — `markitdown-main`

**Tipo:** REPO · **Área:** 04_MEMORIA-E-CONHECIMENTO
**Hash F0:** `dir · 163 arq. · aninhado`   **Hash reconferido:** `163 arq. · aninhamento 1`   **Confere:** sim
**LV:** LV4
**Cobertura da leitura:** raiz efetiva `markitdown-main/markitdown-main` (13 entradas, listagem completa); `LICENSE` — MIT, 1.141 bytes, "Copyright (c) Microsoft Corporation", íntegro; `README.md` (15.757 bytes, lidos 6 KB: aviso de segurança em destaque, formatos suportados, pré-requisitos, instalação, uso por linha de comando, dependências opcionais, plugins, OCR); **busca por diretório de teste na raiz efetiva — ausente**; sinais `SECURITY.md`, `Dockerfile`, `.pre-commit-config.yaml`, `.devcontainer/`. **Não lidos:** `packages/`, `.github/`.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** não se aplica

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 4 | Artefato completo e inspecionável (pacote Python com CLI, conversores por formato, sistema de plugins, `Dockerfile`, `.devcontainer/`) **mais** procedimento de verificação declarado: `.pre-commit-config.yaml` e workflows em `.github/` | — |
| E03 Maturidade | 4 | Versionado com release identificável (badge PyPI e distribuição por `pip install`) **mais** documentação de instalação e uso (três formas de criar ambiente virtual, uso por linha de comando, extras por formato) **mais** tratamento de erro visível: o README documenta a degradação graciosa do plugin de OCR quando não há cliente de LLM configurado | — |
| E05 Manutenção | ND | — | Nenhum `CHANGELOG` na raiz efetiva e nenhuma data observada. Resolveria consultar o histórico de releases no PyPI ou na origem pública `microsoft/markitdown` |
| E06 Segurança ⚠ | 4 | Superfície **delimitada** e declarada em destaque no topo do README ("MarkItDown performs I/O with the privileges of the current process… Sanitize your inputs in untrusted environments") **mais** controles documentados (`SECURITY.md`, seção própria de Security Considerations, plugins **desabilitados por padrão**) **mais** escopo de permissão explícito: a orientação de "call the narrowest `convert_*` function needed" é exatamente uma regra de menor privilégio | — |
| E07 Licença ⚠ | 4 | Permissiva padrão presente e íntegra: MIT, 1.141 bytes, titular corporativo nomeado. Cópia local não prova titularidade → teto 4 | — |
| E13 Testes/evals | ND | — | **Procurado na listagem completa da raiz efetiva: não há diretório de teste no topo.** O projeto é um monorepo com `packages/`, onde as suítes provavelmente vivem. Resolveria listar `packages/*/tests` — leitura adicional que estoura o teto de `05` §8 |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas ("most comparable to textract, but with a focus on preserving important document structure"); os números presentes são badges de versão e download, que não sustentam a proposta. **P-3** | — |

**NF = 4 · 5/7 · 2 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 4 | Endereça diretamente a primeira etapa da pergunta central — como o material entra no sistema — **mais** artefato concreto e reutilizável: conversor de PDF, PowerPoint, Word, Excel, imagem com OCR, áudio com transcrição, HTML, CSV/JSON/XML, ZIP e EPUB para Markdown | — |
| E04 Transferibilidade | 4 | Transferível por configuração, sem alteração de código: `pip install 'markitdown[all]'`, uso por CLI ou por API Python, extras selecionáveis por formato | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto **dentro do acervo**: é a única camada de ingestão documental pronta; o restante do acervo pressupõe o texto já extraído | — |

**RP = 4 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 4 | Instalação declarada em um comando (`pip install 'markitdown[all]'`), configuração por extras. Não alcança 5: exige Python ≥ 3.10 e, para alguns formatos, serviços Azure opcionais | — |
| E09 Custo | 4 | Custo marginal: biblioteca local sem licença paga; custo de modelo só aparece no plugin opcional de OCR por LLM | — |
| E10 Contexto/tokens | 1 | Medido: **163 arquivos, 23,7 MB**. Contagem fecharia a âncora 3 (50–300), tamanho fecha a âncora 1 (20–100 MB); vale a pior das duas | — |
| E11 Fornecedor | 4 | Abstração de fornecedor documentada: núcleo local; integrações com Azure Document Intelligence e Content Understanding são extras opcionais e nomeados; OCR aceita "any OpenAI-compatible client" | — |
| E12 Reversibilidade | 4 | Reversível por remoção, sem efeito residual: é uma biblioteca sem estado persistente próprio; a saída é Markdown em arquivo | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (utilitário Python da equipe AutoGen/Microsoft, lista de formatos, preservação de estrutura, destino de consumo por LLM **e o aviso de segurança do próprio README**) e **todos** os detalhes conferem com o README lido.
**O que o catálogo afirma:** "Utilitário Python da equipe AutoGen (Microsoft)… **Aviso de segurança que o próprio README dá:** faz I/O com os privilégios do processo. Sanitize entradas em ambiente não confiável e use a função `convert_*` mais estreita possível."
**Confere com a fonte:** sim — inclusive a transcrição fiel do aviso de segurança

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "MarkItDown performs I/O with the privileges of the current process… Sanitize your inputs in untrusted environments" | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não verificada por inspeção de código, mas é **declaração de limitação**, não de capacidade — sustenta `E06 = 4` |
| "Mainstream LLMs… natively “_speak_” Markdown… This suggests that they have been trained on vast amounts of Markdown-formatted text" | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA`; o próprio autor marca como sugestão |
| "É a camada de ingestão pronta. Resolve a etapa 1 do pipeline RAG sem escrever nada." | `_CONTEUDO.md` área 04 | ALEGAÇÃO DO CATÁLOGO | não |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V2 · V3 · V4 · V5 · V6 · V7 · V8 | **nenhuma** | `E06 = 4` · `E07 = 4` · `LV = 4` · **2 ND** (no limite) · `E15 = 3` · reconferência confere |

#### Resultado
**RF = CANDIDATO FORTE**
**Regra que produziu:** §9, condições de entrada satisfeitas: `LV = 4` · nenhum eixo do Bloco A abaixo de 3 · `E06 = 4` · `E07 = 4` · **exatamente 2 ND**, no limite permitido · `RP = 4`.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> **CANDIDATO FORTE não significa adotar.** As duas lacunas que sobraram estão nomeadas na ficha: `E05` (manutenção sem data) e `E13` (suíte de testes não localizada sob o teto de leitura). Um terceiro ND teria fechado esta classificação.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-04-REP-005 — `notebooklm-skill-master`

**Tipo:** REPO · **Área:** 04_MEMORIA-E-CONHECIMENTO
**Hash F0:** `dir · 21 arq.`   **Hash reconferido:** `21 arq. · aninhamento 0`   **Confere:** sim
**LV:** LV4
**Cobertura da leitura:** raiz efetiva `notebooklm-skill-master` (10 entradas, listagem completa); `LICENSE` — MIT, 1.072 bytes, "Copyright (c) 2025 Please Prompto!", íntegro; `README.md` (15.901 bytes, lidos 6 KB: restrição de ambiente, problema, solução, tabela comparativa, instalação, início rápido); `requirements.txt` **integral**; `SKILL.md` (frontmatter e início do corpo); `CHANGELOG.md` (`[1.3.0] - 2025-11-21`). **Não lidos:** `scripts/`, `references/`, `images/`, `AUTHENTICATION.md`.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** não se aplica

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 3 | Artefato completo e inspecionável (`SKILL.md` com procedimento, `scripts/` com `run.py`, `ask_question.py`, `notebook_manager.py`, `requirements.txt` com versões fixadas), **sem** procedimento de verificação declarado na fonte | — |
| E03 Maturidade | 3 | Versionado com changelog presente: `[1.3.0] - 2025-11-21`, descrevendo refatoração modular e mudança de timeout. Sem tag ou release observável | — |
| E05 Manutenção | 2 | **Atividade esparsa e sem cadência discernível, evidenciada por datas internas**: a entrada mais recente do `CHANGELOG` é de **2025-11-21**, oito meses antes desta avaliação, para um artefato que depende de automação de navegador contra um produto de terceiro em evolução | — |
| E06 Segurança ⚠ | 1 | **Risco ativo declarado pelo próprio material e ainda não confirmado por inspeção**: `requirements.txt` fixa `patchright==1.55.2`, e o README declara que a escolha de Chrome real em vez de Chromium se dá por "**better anti-detection with Google services**". Contornar detecção de um terceiro é risco de termos de serviço e de conformidade. Soma-se a isso autenticação persistente do Google armazenada localmente (`AUTHENTICATION.md`, não lido) | — |
| E07 Licença ⚠ | 4 | Permissiva padrão presente e íntegra: MIT, 1.072 bytes, titular nomeado. Cópia local não prova titularidade → teto 4 | — |
| E13 Testes/evals | 0 | **Inspecionada a listagem completa da raiz efetiva: nenhum teste, eval ou verificação de qualquer natureza** — as dez entradas são `images/`, `references/`, `scripts/`, `.gitignore`, `AUTHENTICATION.md`, `CHANGELOG.md`, `LICENSE`, `README.md`, `requirements.txt` e `SKILL.md` | — |
| E15 Alegações ⚠ | 0 | A proposta central do item — "Why NotebookLM, Not Local RAG?" — **depende** de uma tabela comparativa **sem fonte**, produzida pelo próprio autor, atribuindo a quatro abordagens custo de token, tempo de configuração, alucinação e qualidade de resposta. Nenhum dado, método ou amostra acompanha. Não verificável com o material disponível | — |

**NF = 2 · 7/7 · 0 ND** *(mediana de [0,0,1,2,3,3,4] = 2)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 4 | Endereça diretamente a pergunta central — recuperação fundamentada em fonte — **mais** artefato concreto e reutilizável (§14.2): `SKILL.md` com frontmatter, gatilhos e procedimento de duas etapas para descoberta de conteúdo | — |
| E04 Transferibilidade | 3 | Transferível com adaptação declarada e delimitada: exige Claude Code **local** (o próprio README exclui a interface web), Chrome real, conta Google e login por navegador | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto **dentro do acervo**: é o único item que sustenta a via "RAG hospedado por terceiro", oposta à de `AC-04-REP-001` e à do carrossel LangChain desta mesma área | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Runtime já presente e instalação documentada com passos manuais: criar diretório, clonar, e então o primeiro uso cria ambiente virtual e **instala o Google Chrome**. A instalação de um navegador completo impede as âncoras superiores | — |
| E09 Custo | 3 | Custo variável por uso, com limite ou controle possível: sem licença paga declarada, mas o uso depende de conta e de quotas de um produto de terceiro não controladas pelo artefato | — |
| E10 Contexto/tokens | 4 | Medido: **21 arquivos, 262 KB** — menos de 50 arquivos e menos de 1 MB, com superfície delimitada pelo `SKILL.md` | — |
| E11 Fornecedor | 1 | **Preso a fornecedor único, com exportação apenas parcial**: todo o valor depende do NotebookLM do Google, acessado por automação de navegador — sem API declarada, sem formato de exportação e sem alternativa prevista no artefato | — |
| E12 Reversibilidade | 3 | Reversível por remoção da pasta da skill, com efeitos colaterais documentados: permanecem o ambiente virtual, o Chrome instalado e a autenticação persistente | — |

**AA = 3 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (skill que conversa com o NotebookLM por automação de navegador, autenticação persistente, restrição a Claude Code local, e o enunciado do problema) e **todos** os detalhes conferem com o README lido, inclusive a restrição de ambiente, que o catálogo registra como "restrição declarada".
**O que o catálogo afirma:** "Skill que conversa com o NotebookLM do Google por automação de navegador, com autenticação persistente… **Restrição declarada:** só funciona em Claude Code **local**, não na interface web… **O que extrair:** o argumento “RAG hospedado por terceiro vs. RAG próprio” está inteiro neste README."
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| Tabela "Why NotebookLM, Not Local RAG?" — quatro abordagens comparadas por custo de token, tempo de configuração, alucinação e qualidade | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA`, **sem fonte**; sustenta `E15 = 0` |
| "better **anti-detection** with Google services" | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — **achado de risco registrado**: contornar detecção de terceiro. Sustenta `E06 = 1` |
| "**Minimal** - source-grounded only" / "Drastically reduced hallucinations" | `README.md` e `SKILL.md` da fonte | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "Compare com `ai-second-brain-main`, que defende o extremo oposto." | `_CONTEUDO.md` área 04 | ALEGAÇÃO DO CATÁLOGO | **conferida entre as duas fichas** — a oposição existe e está registrada em ambas |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V4 · V5 · V6 · V8 | não | `E06 ≠ 0` (declarado, não confirmado por inspeção) · `E07 = 4` · `LV = 4` · 0 ND · reconferência confere |
| **V2** | **sim** | `E06 = 1` → teto PADRÃO A ESTUDAR / REFERÊNCIA / EXIGE PESQUISA |
| **V7** | **sim** | `E15 = 0` e a relevância do item depende da tabela comparativa → teto EXIGE PESQUISA |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** V2 e V7 (§8), que se somam no mesmo teto.
**Se EXIGE PESQUISA — lacuna nomeada:** duas, ambas endereçáveis: (1) a natureza e a consequência do modo **anti-detecção** — se o uso viola os termos de serviço do produto de terceiro; (2) a tabela comparativa que sustenta a proposta, sem dado, método ou amostra.  **Verificação que a fecharia:** ler `AUTHENTICATION.md` e `scripts/` para delimitar o que é armazenado e como a detecção é contornada; e, para a tabela, um experimento próprio comparando custo e qualidade das quatro abordagens sobre um corpus desta casa.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-04-REP-006 — `open-notebook-main`

**Tipo:** REPO · **Área:** 04_MEMORIA-E-CONHECIMENTO
**Hash F0:** `dir · 574 arq. · aninhado`   **Hash reconferido:** `574 arq. · aninhamento 1`   **Confere:** sim
**LV:** LV4
**Cobertura da leitura:** raiz efetiva `open-notebook-main/open-notebook-main` (41 entradas); `LICENSE` — MIT, 1.061 bytes, "Copyright (c) 2024 Luis Novo", **texto integral lido**; `README.dev.md` (1.021 bytes, integral); `pyproject.toml` (metadados e bloco de dependências, com os comentários de justificativa); `CHANGELOG.md` (seção `Unreleased`, com registro de ADR-007 e números de issue); `tests/` — 45 arquivos, topo listado; sinais `.env.example`, `SECURITY.md`, `Dockerfile`, `docker-compose.yml`, `Makefile`, `VISION.md`, `MAINTAINER_GUIDE.md`. **Não lidos:** `open_notebook/`, `api/`, `frontend/`, `docs/`, `prompts/`.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** não se aplica

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 4 | Artefato completo e inspecionável (API, worker, frontend, prompts, comandos, `docker-compose`) **mais** procedimento de verificação declarado: `tests/` com 45 arquivos e `conftest.py`, incluindo casos de caracterização e de regressão nomeados | — |
| E03 Maturidade | 4 | Versionado com release identificável (`version = "1.12.0"`, ≥ 1.0) **mais** documentação de instalação e uso (`Makefile`, `docker-compose`, guias em `docs/7-DEVELOPMENT/`) **mais** tratamento de erro visível: o changelog descreve degradação graciosa de runtime opcional ("a failed install degrades gracefully… with loud logs") e uma sonda `GET /api/capabilities` que reporta o que está de fato instalado | — |
| E05 Manutenção | ND | — | O `CHANGELOG` traz seção `Unreleased` com referências a issues (#1122, #1104, #1103, #1030, #1106), mas **nenhuma data** no trecho lido, e não há `VERSION` datado. Resolveria ler as entradas datadas abaixo no changelog ou consultar as releases na origem pública |
| E06 Segurança ⚠ | 3 | Superfície declarada (API, banco SurrealDB, worker, extração de conteúdo remoto, renderização de JavaScript por Crawl4AI) **com controles parciais documentados**: `SECURITY.md`, `.env.example`, e nomes de teste que evidenciam controles — `test_config_endpoint_no_leak`, `test_cors_credentials`, `test_credential_provider_validation`. **Não elevado a 4**: os testes não foram lidos e não há escopo de permissão explícito no material lido | — |
| E07 Licença ⚠ | 4 | Permissiva padrão presente e íntegra na raiz efetiva: MIT, 1.061 bytes, com o texto de garantia completo; classificador `License :: OSI Approved :: MIT License` em `pyproject.toml`. Cópia local não prova titularidade → teto 4 | — |
| E13 Testes/evals | 3 | `tests/` inspecionado: 45 arquivos com `conftest.py`, `README.md` próprio e ponto de entrada por pytest. Nenhum eval de comportamento de modelo identificado | — |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas ("An open source implementation of a research assistant, inspired by Google Notebook LM"); nenhum número decisivo em jogo no material lido | — |

**NF = 3 · 6/7 · 1 ND** *(mediana dos determinados [3,3,3,4,4,4] = 3,5 → §14.3 vale o inferior)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 4 | Endereça diretamente a pergunta central — ingestão, indexação e consulta fundamentada em fontes — **mais** artefato concreto: pipeline de extração com motores selecionáveis, banco, API e prompts versionados | — |
| E04 Transferibilidade | 4 | Transferível por configuração, sem alteração de código: `.env.example`, `docker-compose.yml`, `Makefile` e chaveamento de motores por configuração persistida | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto no acervo: é a única alternativa **auto-hospedada e completa** ao produto de terceiro que `AC-04-REP-005` acessa por automação de navegador | — |

**RP = 4 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 4 | Instalação declarada em poucos comandos (`cp .env.example .env`, `uv sync`, `make start-all`), configuração por variável de ambiente. Não alcança 5: exige SurrealDB, API, worker e frontend em conjunto | — |
| E09 Custo | 3 | Custo variável por uso, com limite ou controle possível: auto-hospedado, sem licença paga, mas exige infraestrutura permanente (banco + API + worker) além das chamadas de modelo | — |
| E10 Contexto/tokens | 2 | Medido: **574 arquivos, 5,7 MB** — contagem na faixa 300–1.000 e tamanho na faixa 5–20 MB | — |
| E11 Fornecedor | 4 | Abstração de fornecedor documentada: `esperanto` mais pacotes `langchain-*` para OpenAI, Anthropic, Ollama, Google, Groq e Mistral, com a justificativa escrita no próprio manifesto; troca por configuração | — |
| E12 Reversibilidade | 2 | **Reversível com perda de estado ou de histórico**: o produto persiste notebooks, fontes, insights e episódios em SurrealDB; o changelog registra migração 21 de caminhos de áudio, evidenciando estado acumulado | — |

**AA = 3 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 2** — a descrição é **genérica e curta** para um item de 574 arquivos: "Foco em privacidade. API, frontend, prompts e comandos próprios." Os quatro elementos citados existem na raiz efetiva, mas o "foco em privacidade" **não foi conferido** contra nada observável — não há declaração de privacidade no material lido. Detalhe verificável parcialmente não conferido → teto 2 (§14.4).
**O que o catálogo afirma:** "`open-notebook-main/` — alternativa open source ao NotebookLM. Foco em privacidade. API, frontend, prompts e comandos próprios."
**Confere com a fonte:** parcialmente

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "An open source implementation of a research assistant, inspired by Google Notebook LM" | `pyproject.toml` da fonte | ALEGAÇÃO DO AUTOR | **conferida em nível de metadado** — é a descrição declarada do próprio pacote |
| "Foco em privacidade." | `_CONTEUDO.md` área 04 | ALEGAÇÃO DO CATÁLOGO | não — `NÃO VERIFICADA`; nada no material lido sustenta ou nega |
| "This keeps the default image lean (no Chromium, no multi-GB ML stack) while making both runtimes available on demand." | `CHANGELOG.md` da fonte | ALEGAÇÃO DO AUTOR | não |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V2 · V3 · V4 · V5 · V6 · V7 · V8 | **nenhuma** | `E06 = 3` · `E07 = 4` · `LV = 4` · 1 ND · `E15 = 3` · reconferência confere |

#### Resultado
**RF = CANDIDATO FORTE**
**Regra que produziu:** §9, condições de entrada satisfeitas: `LV = 4` · nenhum eixo do Bloco A abaixo de 3 · `E06 = 3` · `E07 = 4` · **1 ND** ≤ 2 · `RP = 4`.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> **CANDIDATO FORTE não significa adotar.** Restrições registradas: `E12 = 2` (estado persistente em banco) e `E05 = ND` (nenhuma data de manutenção observada).

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-04-REP-007 — `second-brain-skills-main`

**Tipo:** REPO · **Área:** 04_MEMORIA-E-CONHECIMENTO
**Hash F0:** `dir · 97 arq.`   **Hash reconferido:** `97 arq. · aninhamento 0`   **Confere:** sim
**LV:** LV4
**Cobertura da leitura:** raiz efetiva `second-brain-skills-main` — **listagem completa: duas entradas**, `.claude/` e `README.md`; **busca por `LICENSE`/`COPYING`/`LICENCE` na raiz efetiva — ausente**; `README.md` (16.825 bytes, lidos 6 KB: proposta, gerador de marca e voz, arquivos-fonte-da-verdade, skill de cliente MCP com configuração e comandos); **busca por diretório de teste na raiz — ausente**. **Não lidos:** o conteúdo de `.claude/skills/`.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** não se aplica

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 3 | Artefato completo e inspecionável correspondente à afirmação (coleção de skills em `.claude/`, com scripts Python e arquivos de referência declarados no README), **sem** procedimento de verificação declarado na fonte | — |
| E03 Maturidade | 2 | Funciona no cenário demonstrado, mas **sem versionamento, sem release e sem tag**: a raiz efetiva tem apenas `.claude/` e `README.md` — não há `VERSION`, `CHANGELOG` nem manifesto de pacote | — |
| E05 Manutenção | ND | — | Nenhuma evidência datada dentro da fonte. Resolveria consultar a origem pública do repositório |
| E06 Segurança ⚠ | 2 | Superfície ampla **sem controle documentado**: o README instrui copiar um arquivo de configuração de MCP e editá-lo com chaves de API reais, e executar scripts Python que chamam servidores MCP remotos (Zapier e outros). Não há `SECURITY.md`, escopo de permissão nem menor privilégio declarado. **Registrado**: o exemplo de configuração usa o marcador `"YOUR_API_KEY_HERE"` — **não há credencial real no material lido** | — |
| E07 Licença ⚠ | ND | — | **Não há arquivo de licença na raiz efetiva** (procurado e não encontrado). Resolveria ler a licença na origem pública. Este é um dos quatro casos I-04 do inventário e do bloqueio B-02 |
| E13 Testes/evals | ND | — | Não há diretório de teste no topo, mas as skills vivem em `.claude/`, que não foi enumerado. Resolveria listar `.claude/skills/*` procurando teste, eval ou verificação |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas ("there's no magic, just structured knowledge that makes Claude hyper-capable for specific tasks"); nenhum número decisivo em jogo | — |

**NF = 2 · 4/7 · 3 ND** *(mediana dos determinados [2,2,3,3] = 2,5 → §14.3 vale o inferior)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 4 | Endereça diretamente a pergunta central — como o conhecimento é organizado e recuperado sem inchar o contexto — **mais** artefato concreto e reutilizável (§14.2): arquivos-fonte-da-verdade nomeados (`brand.json`, `config.json`, `brand-system.md`, `tone-of-voice.md`) com a tabela de quem consome cada um | — |
| E04 Transferibilidade | 3 | Transferível com adaptação declarada e delimitada: skills em Markdown mais scripts Python; o cliente MCP exige configuração própria com credenciais | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto no acervo: a **divulgação progressiva** — carregar o esquema da ferramenta só quando necessário, em vez de inflar o contexto com definições de MCP — é formulada aqui de modo explícito e operacional | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Runtime já presente (Claude Code + Python) e instalação documentada com passos manuais: copiar o arquivo de configuração de exemplo e editá-lo | — |
| E09 Custo | 4 | Custo marginal: skills locais sem licença paga; o custo recorrente aparece apenas nos serviços MCP de terceiros que o usuário escolher conectar | — |
| E10 Contexto/tokens | 3 | Medido: **97 arquivos, 725 KB**. Tamanho fecharia a âncora 4 (< 1 MB), contagem fecha a âncora 3 (50–300 arquivos); vale a pior das duas. **Nota**: a própria proposta do item é reduzir superfície por divulgação progressiva | — |
| E11 Fornecedor | 3 | Dois ou mais fornecedores suportados, com troca custosa: o cliente MCP aceita servidores remotos e locais (`url`+`api_key`, `command`+`args`, SSE, HTTP), mas cada integração é configurada à mão | — |
| E12 Reversibilidade | 4 | Reversível por remoção, sem efeito residual: são arquivos em `.claude/`; o estado externo fica nos serviços conectados, não no artefato | — |

**AA = 3 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (integrações MCP sem inchar contexto, vídeo com Remotion, apresentações e carrosséis com identidade de marca, runbooks e SOPs, criação de skills, consistência de marca, divulgação progressiva, arquivos-fonte-da-verdade `brand.json` e `tone-of-voice.md`) e os detalhes conferem com o README lido, **inclusive os dois nomes de arquivo citados**.
**O que o catálogo afirma:** "Coleção que estende o Claude Code para além de código… Funciona por **divulgação progressiva** — o Claude só carrega a instrução detalhada quando precisa. **O que extrair:** o padrão de divulgação progressiva e o conceito de arquivos-fonte-da-verdade (`brand.json`, `tone-of-voice.md`) lidos por todas as outras skills."
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "MCP servers expose thousands of tokens worth of tool definitions. This skill wraps them as a lightweight client, loading only what you need when you need it." | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA`; o código do cliente não foi lido |
| "there's no magic, just structured knowledge that makes Claude hyper-capable for specific tasks" | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não |
| Exemplo de configuração com `"api_key": "YOUR_API_KEY_HERE"` | `README.md` da fonte | FATO OBSERVADO | **marcador, não credencial** — registrado conforme `05` §7.5, sem transcrição de segredo algum porque não há segredo |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V2 · V3 · V5 · V6 · V7 · V8 | não | `E06 = 2` (≠ 0 e ≠ ND) · `E07 ≠ 0` · `LV = 4` · 3 ND · `E15 = 3` · reconferência confere |
| **V4** | **sim** | `E07 = ND` — licença ausente na raiz efetiva → nunca CANDIDATO FORTE nem CANDIDATO A PILOTO |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** V4 (§8) somada à condição de entrada de EXIGE PESQUISA (§9).
**Se EXIGE PESQUISA — lacuna nomeada:** licença e titularidade — **ausentes na raiz efetiva** (caso I-04 / bloqueio B-02).  **Verificação que a fecharia:** localizar a origem pública do repositório e ler o texto da licença; secundariamente, enumerar `.claude/skills/` para fechar `E13` e reavaliar `E06`.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

> **Nota de série — AC-04-PRT-002 a AC-04-PRT-013.** Doze capturas de um carrossel de doze slides sobre um pipeline RAG com LangChain, **série completa** (0 a 11). `05` §2.2 obriga ficha individual por ID; o valor de conjunto entra como nota adicional, nunca substituindo a avaliação individual. Cobertura, LV e origem Codex idênticos nas doze e em AC-04-PRT-001: inspeção visual do original pela trilha Codex (`107`, lote 08, `H-P1-002`), sem abertura da imagem por esta frente. **A ordem dos IDs segue o manifesto, não a ordem dos slides** — `PRT-004` é o slide 10 e `PRT-005` é o slide 11.

### AC-04-PRT-001 — `Captura de tela 2026-07-28 152727.png`

**Tipo:** PRINT · **Área:** 04_MEMORIA-E-CONHECIMENTO
**Hash F0:** `FFDCEE7B2B6B571F`   **Hash reconferido:** `FFDCEE7B2B6B571F`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`107`); descrição do `_CONTEUDO.md` confrontada com os pixels.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-04-PRT-001 · `H-P1-002` (relatório `107`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Infográfico isolado e não reprodutível: 13 áreas, fluxo Capture → Organize → Connect → Visualize → Reflect, comparação PARA × Zettelkasten. Nenhum vault, arquivo ou insumo acompanha (`107`, CONFIRMADA) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem do infográfico e seu versionamento |
| E05 Manutenção | ND | — | Localizar o canal de publicação com data e cadência |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial ou instrução dirigida ao leitor. **Superfície retratada**: o infográfico recomenda plugins de terceiro |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos de uso do infográfico |
| E13 Testes/evals | ND | — | Nenhum artefato testável associado |
| E15 Alegações ⚠ | 1 | Alegações numéricas com fonte citada porém não conferida e não conferível com o material disponível: o infográfico exibe "estatísticas do ecossistema" (`_CONTEUDO.md`) sem data nem método | — |

**NF = 1 · 2/7 · 5 ND** *(mediana de [1,2] = 1,5 → §14.3 vale o inferior)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: descreve um sistema local-first de captura, ligação e revisão — uma das três vias de memória em disputa nesta área | — |
| E04 Transferibilidade | 3 | O fluxo (capturar → organizar → conectar → visualizar → refletir) transfere com adaptação declarada; independe de fornecedor | — |
| E14 Diferencial | 2 | Agregação de material público amplamente conhecido; converge com AC-04-VID-006, AC-04-VID-009 e AC-04-VID-011 dentro do acervo | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação; formato de consumo não declarado | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 1,7 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `107` + parágrafo do `_CONTEUDO.md`; < 1 MB | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (13 áreas, fluxo de cinco passos, backlinks, graph view, canvas, daily notes, PARA e Zettelkasten, recomendação de começar simples) conferido contra os pixels; CONFIRMADA em `107`.
**O que o catálogo afirma:** "Infográfico “Master Obsidian” dividido em 13 áreas… workflow Capture → Organize → Connect → Visualize → Reflect… Também compara estruturas como PARA e Zettelkasten e recomenda começar simples antes de instalar muitos plugins."
**Confere com a fonte:** sim — CONFIRMADA em `107`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "o valor não está no grafo bonito; está no fluxo que transforma captura em conexão e revisão" | `_CONTEUDO.md` área 04 | ALEGAÇÃO DO CATÁLOGO | não |
| "o infográfico agrega muitas recomendações sem demonstrar qual serve a cada uso" | `_CONTEUDO.md` área 04 | ALEGAÇÃO DO CATÁLOGO | **conferida** — `107` chega à mesma leitura, sem que a coincidência valha como validação |

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

### AC-04-PRT-002 — `Rag + langchain0.png` *(slide 0/11 — stack)*

**Tipo:** PRINT · **Área:** 04_MEMORIA-E-CONHECIMENTO · **Série:** RAG+LangChain, 12 slides
**Hash F0:** `C8D2EBEB0FED1D6F`   **Hash reconferido:** `C8D2EBEB0FED1D6F`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`107`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-04-PRT-002 · `H-P1-002` (relatório `107`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Exemplo isolado e não reprodutível: comando de instalação e sete componentes nomeados, sem projeto, dado ou execução (`107`, CONFIRMADA "como texto exibido") | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e sua data — o slide fixa versões de biblioteca implicitamente |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial ou instrução ao leitor |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos do carrossel |
| E13 Testes/evals | ND | — | O slide nomeia "avaliação" como um dos sete componentes, mas nenhum eval é exibido; o slide 9 da mesma série o desenvolve |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas (quais componentes compõem o stack); nenhum número decisivo em jogo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: enumera as sete peças de um pipeline de indexação e recuperação | — |
| E04 Transferibilidade | 3 | A decomposição em sete componentes transfere com adaptação declarada; os pacotes citados são de um ecossistema específico | — |
| E14 Diferencial | 2 | Agregação de material público; é a capa de uma série cujo conteúdo operacional está nos slides seguintes | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 1,5 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `107` + linha da tabela do `_CONTEUDO.md`; < 1 MB | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (comando de instalação com os pacotes nomeados e os sete componentes) conferido contra os pixels; CONFIRMADA em `107`.
**O que o catálogo afirma:** "`pip install langchain_community pypdf langchain` + `langchain_huggingface faiss-cpu langchain_groq`. Sete componentes: loaders, splitters, embeddings, vector stores, retrievers, LLMs, avaliação"
**Confere com a fonte:** sim — CONFIRMADA em `107`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "É a documentação mais prática do acervo — **um passo do pipeline por slide, com código**." | `_CONTEUDO.md` área 04 | ALEGAÇÃO DO CATÁLOGO | **parcialmente conferida** — a série tem de fato um passo por slide, e dois slides trazem código; "mais prática do acervo" é juízo comparativo não verificado |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 3` · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> **Nota de conjunto (não substitui esta ficha):** a série 0–11 é o único material do acervo que percorre um pipeline RAG passo a passo. `107` registra o limite: "tecnicamente envelhecível — APIs, imports e modelos não podem virar exemplo oficial sem teste de versão".

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-04-PRT-003 — `Rag + langchain1.png` *(slide 1/11 — document loading)*

**Tipo:** PRINT · **Área:** 04_MEMORIA-E-CONHECIMENTO · **Série:** RAG+LangChain
**Hash F0:** `990DD0B0924CBD04`   **Hash reconferido:** `990DD0B0924CBD04`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`107`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-04-PRT-003 · `H-P1-002` (relatório `107`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Exemplo isolado: cinco carregadores nomeados (PyPDFLoader, TextLoader, WebBaseLoader, CSVLoader, WikipediaLoader), sem execução nem insumo (`107`, CONFIRMADA) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e sua data |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial ou instrução ao leitor. **Superfície retratada**: `WebBaseLoader` ingere conteúdo externo não confiável |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhum artefato testável associado |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas; nenhum número decisivo em jogo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a primeira etapa da pergunta central: como o material entra no índice | — |
| E04 Transferibilidade | 2 | O **padrão** (um carregador por tipo de fonte) transfere; a implementação é de uma biblioteca específica | — |
| E14 Diferencial | 1 | Conveniência sobre algo já acessível; `AC-04-REP-004` entrega a mesma etapa como artefato pronto e mais amplo | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 961,2 KB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `107` + linha do `_CONTEUDO.md` | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (os cinco carregadores, nomeados) conferido; CONFIRMADA em `107`.
**O que o catálogo afirma:** "PyPDFLoader (PDF), TextLoader, WebBaseLoader (sites), CSVLoader, WikipediaLoader"
**Confere com a fonte:** sim — CONFIRMADA em `107`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| — nenhuma alegação numérica ou de autoridade identificada neste slide | `107` | — | — |

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

### AC-04-PRT-004 — `Rag + langchain10.png` *(slide 10/11 — tuning e produção)*

**Tipo:** PRINT · **Área:** 04_MEMORIA-E-CONHECIMENTO · **Série:** RAG+LangChain
**Hash F0:** `F0C7C9BEB4841876`   **Hash reconferido:** `F0C7C9BEB4841876`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`107`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-04-PRT-004 · `H-P1-002` (relatório `107`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Exemplo isolado e não reprodutível: valores padrão e uma tabela de diagnóstico (retrieval ruim → chunk ou embedding; alucinação → contexto insuficiente; lentidão → chunks grandes), sem corpus, medição ou execução (`107`, CONFIRMADA) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e sua data |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial. **Registrado como fato observado**: o slide inclui "segredos protegidos" entre as recomendações de produção | — |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | O slide recomenda monitoramento e fallback, mas não exibe nenhum teste; resolveria obter a fonte primária | — |
| E15 Alegações ⚠ | 1 | Alegações numéricas fortes **sem método**, apresentadas como padrões de produção: chunk 300, overlap 50–100, k entre 3 e 10, temperatura 0. A fonte é o próprio slide; não são conferíveis com o material disponível | — |

**NF = 1 · 2/7 · 5 ND** *(mediana de [1,2] = 1,5 → §14.3 vale o inferior)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: dá pontos de partida e um roteiro de diagnóstico para o comportamento da recuperação | — |
| E04 Transferibilidade | 3 | O roteiro de diagnóstico transfere com adaptação declarada; os números são específicos do corpus de quem os mediu — e nenhum corpus é declarado | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto **dentro do acervo**: nenhum outro item liga sintoma a parâmetro de ajuste | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 1,2 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `107` + linha do `_CONTEUDO.md` | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (os quatro valores padrão, as três linhas de diagnóstico e as quatro recomendações de produção) conferido contra os pixels; CONFIRMADA em `107`.
**O que o catálogo afirma:** "Defaults: chunk 300, overlap 50–100, k 3–10, temperatura 0. Diagnóstico: retrieval ruim → chunk ou embedding; alucinação → contexto insuficiente; lentidão → chunks grandes demais. Produção: cache de embeddings, monitoramento, fallback, segredos protegidos"
**Confere com a fonte:** sim — CONFIRMADA em `107`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "chunk 300, overlap 50–100, k 3–10, temperatura 0" como padrões | print (texto observado, via `107`) | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA`; `107` registra: "valores de chunk, overlap, k, embedding e banco são hipóteses de partida que exigem corpus, perguntas e evals representativos" |
| "os valores de partida (chunk 300 / overlap 50 / k 5 / temperatura 0)" | `_CONTEUDO.md` área 04 | ALEGAÇÃO DO CATÁLOGO | — o catálogo cita `k 5`, que vem do slide 6, não deste; sem contradição |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** §9 — relevância aparente (`E01 = 3`) com lacuna nomeada e endereçável; teto de V2/V4 respeitado.
**Se EXIGE PESQUISA — lacuna nomeada:** os quatro valores padrão não têm corpus, método nem medição declarados.  **Verificação que a fecharia:** medir localmente, sobre um corpus desta casa e um conjunto de perguntas próprio, a variação de qualidade e custo em função de chunk, overlap e k — experimento próprio, não repetição do número do slide.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-04-PRT-005 — `Rag + langchain11.png` *(slide 11/11 — resumo)*

**Tipo:** PRINT · **Área:** 04_MEMORIA-E-CONHECIMENTO · **Série:** RAG+LangChain
**Hash F0:** `46A8CD100DB728A7`   **Hash reconferido:** `46A8CD100DB728A7`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`107`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-04-PRT-005 · `H-P1-002` (relatório `107`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Exemplo isolado: o pipeline completo em sete caixas mais quatro lembretes, sem execução nem insumo (`107`, CONFIRMADA) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e sua data |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial ou instrução ao leitor |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhum artefato testável associado |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas ("comece simples e otimize com base em resultado"); nenhum número decisivo em jogo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: consolida o pipeline inteiro em um só quadro | — |
| E04 Transferibilidade | 3 | O pipeline em sete etapas transfere com adaptação declarada | — |
| E14 Diferencial | 2 | Agregação: é o resumo dos onze slides anteriores da mesma série | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 684,6 KB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `107` + linha do `_CONTEUDO.md` | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (sete caixas e quatro lembretes) conferido; CONFIRMADA em `107`.
**O que o catálogo afirma:** "Pipeline completo em 7 caixas + quatro lembretes, incluindo “comece simples e otimize com base em resultado”"
**Confere com a fonte:** sim — CONFIRMADA em `107`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "comece simples e otimize com base em resultado" | print (texto observado, via `107`) | ALEGAÇÃO DO AUTOR | não |

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

### AC-04-PRT-006 — `Rag + langchain2.png` *(slide 2/11 — pré-processamento)*

**Tipo:** PRINT · **Área:** 04_MEMORIA-E-CONHECIMENTO · **Série:** RAG+LangChain
**Hash F0:** `73A4E647F05AF6E7`   **Hash reconferido:** `73A4E647F05AF6E7`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`107`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-04-PRT-006 · `H-P1-002` (relatório `107`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Exemplo isolado com trecho de código (`re.sub` removendo espaços extras, "Page \d+" e caracteres especiais), não executado e sem insumo (`107`, CONFIRMADA "como conteúdo do slide") | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e sua data |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial ou instrução ao leitor |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhum teste do trecho exibido; resolveria obter a fonte primária com o código completo |
| E15 Alegações ⚠ | 3 | Apenas alegação qualitativa — que a biblioteca não fornece pré-processamento embutido —, sem número em jogo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central e faz o que nenhum outro slide da série faz: **nomeia uma etapa que o framework não resolve** e que precisa ser camada explícita | — |
| E04 Transferibilidade | 3 | O alerta transfere com adaptação declarada; o trecho de limpeza é específico do formato de origem | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto no acervo: é o único ponto do material que separa o que o framework faz do que o usuário precisa escrever | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 1,1 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `107` + linha do `_CONTEUDO.md` | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (a afirmação de que o framework não faz pré-processamento e o exemplo com `re.sub`) conferido contra os pixels; CONFIRMADA em `107`.
**O que o catálogo afirma:** "**O LangChain NÃO faz isso** — é código próprio. Exemplo com `re.sub` removendo espaços extras, “Page \d+” e caracteres especiais"
**Confere com a fonte:** sim — CONFIRMADA em `107`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "LangChain não fornece pré-processamento embutido" | print (texto observado, via `107`) | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "o alerta do slide 2 — pré-processamento é trabalho manual e precisa ser uma camada explícita da arquitetura" | `_CONTEUDO.md` área 04 | ALEGAÇÃO DO CATÁLOGO | não |

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

### AC-04-PRT-007 — `Rag + langchain3.png` *(slide 3/11 — chunking)*

**Tipo:** PRINT · **Área:** 04_MEMORIA-E-CONHECIMENTO · **Série:** RAG+LangChain
**Hash F0:** `FC85EFBC56F122CF`   **Hash reconferido:** `FC85EFBC56F122CF`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`107`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-04-PRT-007 · `H-P1-002` (relatório `107`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Exemplo isolado: `RecursiveCharacterTextSplitter` com parâmetros e cascata de separadores, sem corpus nem medição (`107`, CONFIRMADA) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e sua data |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial ou instrução ao leitor |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhum eval que sustente a escolha de tamanho; resolveria obter a fonte primária |
| E15 Alegações ⚠ | 1 | Alegação numérica forte **sem método**: `107` registra literalmente que "**“300 is optimal” é alegação do slide, não padrão validado**". A fonte é o próprio slide; não conferível com o material disponível | — |

**NF = 1 · 2/7 · 5 ND** *(mediana de [1,2] = 1,5 → §14.3 vale o inferior)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: a segmentação determina o que pode ser recuperado | — |
| E04 Transferibilidade | 2 | O **padrão** (separadores em cascata com sobreposição) transfere; os números dependem do corpus, que não é declarado | — |
| E14 Diferencial | 2 | Agregação de material público amplamente conhecido | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 1,2 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `107` + linha do `_CONTEUDO.md` | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (`chunk_size=300`, `chunk_overlap=50`, faixa 200–1000, sobreposição de 10–20%, separadores em cascata) conferido; CONFIRMADA em `107`.
**O que o catálogo afirma:** "`RecursiveCharacterTextSplitter`, `chunk_size=300`, `chunk_overlap=50`. Faixa recomendada: 200–1000 caracteres, overlap de 10–20%, separadores em cascata `[“\n\n”, “\n”, “.”, “ ”]`"
**Confere com a fonte:** sim — CONFIRMADA em `107`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "300 is optimal" | print (texto observado, via `107`) | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA`; `107` marca explicitamente como alegação do slide |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** §9 — relevância aparente com lacuna nomeada e endereçável; teto de V2/V4 respeitado.
**Se EXIGE PESQUISA — lacuna nomeada:** a afirmação "300 is optimal" não tem corpus, método nem comparação.  **Verificação que a fecharia:** varredura de tamanho de chunk sobre corpus e perguntas próprios, medindo qualidade de recuperação — a mesma verificação que fecha `AC-04-PRT-004`, contada uma vez.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-04-PRT-008 — `Rag + langchain4.png` *(slide 4/11 — embeddings)*

**Tipo:** PRINT · **Área:** 04_MEMORIA-E-CONHECIMENTO · **Série:** RAG+LangChain
**Hash F0:** `8AC03D7E88BBB6B5`   **Hash reconferido:** `8AC03D7E88BBB6B5`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`107`), com conferência atributo a atributo dos três modelos.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-04-PRT-008 · `H-P1-002` (relatório `107`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Exemplo isolado: três modelos de embedding comparados por atributo qualitativo, sem benchmark, corpus ou medição (`107`, PARCIAL) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e sua data — nomes de modelo envelhecem rápido |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial ou instrução ao leitor |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos do carrossel; **e**, separadamente, a licença de cada modelo citado |
| E13 Testes/evals | ND | — | Nenhum benchmark exibido; resolveria obter a fonte primária de cada modelo |
| E15 Alegações ⚠ | 1 | Alegações fortes com fonte citada (nomes de modelo) porém não conferidas e não conferíveis com o material disponível: "melhor equilíbrio", "mais rápido", "alta qualidade". **`107` registra correção material**: o atributo "**pago**" que o catálogo aplica a `text-embedding-ada-002` **não aparece no print** | — |

**NF = 1 · 2/7 · 5 ND** *(mediana de [1,2] = 1,5 → §14.3 vale o inferior)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: a escolha do embedding determina o que a recuperação enxerga | — |
| E04 Transferibilidade | 2 | O **padrão** (comparar embeddings por equilíbrio, velocidade e qualidade) transfere; a seleção é datada | — |
| E14 Diferencial | 2 | Agregação de material público amplamente conhecido | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente para consultar; PNG local de 878,1 KB. *O custo dos modelos retratados não é pontuado aqui* (§3.3 do índice) | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `107` + linha do `_CONTEUDO.md` | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 2** — **PARCIAL** em `107`: os modelos e as comparações conferem, mas o catálogo acrescenta que `text-embedding-ada-002` é "**pago**" — informação que **não aparece no print**. Atributo acrescentado por inferência → correção material 1 de `107`; teto 2 (§14.4).
**O que o catálogo afirma:** "all-mpnet-base-v2 (melhor equilíbrio) · all-MiniLM-L6-v2 (mais rápido) · text-embedding-ada-002 da OpenAI (alta qualidade, **pago**)"
**Confere com a fonte:** parcialmente — manter "pago" como alegação externa separada

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "melhor equilíbrio" / "mais rápido" / "alta qualidade" | print (texto observado, via `107`) | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "pago", atribuído a `text-embedding-ada-002` | `_CONTEUDO.md` área 04 | ALEGAÇÃO DO CATÁLOGO | **não observável no print** → sustenta `NC = 2`; permanece alegação externa não verificada |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4. A escolha de embedding é decisão de projeto, não artefato a verificar neste item.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-04-PRT-009 — `Rag + langchain5.png` *(slide 5/11 — banco vetorial)*

**Tipo:** PRINT · **Área:** 04_MEMORIA-E-CONHECIMENTO · **Série:** RAG+LangChain
**Hash F0:** `F8D94241C959F564`   **Hash reconferido:** `F8D94241C959F564`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`107`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-04-PRT-009 · `H-P1-002` (relatório `107`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Exemplo isolado: FAISS e três alternativas nomeadas com atributo, sem benchmark nem execução (`107`, CONFIRMADA "como alegações exibidas") | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e sua data |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial ou instrução ao leitor |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos do carrossel; **e**, separadamente, a licença de cada banco citado |
| E13 Testes/evals | ND | — | Nenhum benchmark exibido | — |
| E15 Alegações ⚠ | 1 | Alegações fortes com fonte citada (nomes de produto) porém não conferidas: "escala a milhões de vetores", "suporte a GPU", "gerenciado", "leve", "performance" | — |

**NF = 1 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: onde o índice vive | — |
| E04 Transferibilidade | 2 | O **padrão** (escolher entre banco local e gerenciado) transfere; a seleção é datada | — |
| E14 Diferencial | 2 | Agregação de material público amplamente conhecido | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 1 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `107` + linha do `_CONTEUDO.md` | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (FAISS com quatro atributos e três alternativas nomeadas) conferido; CONFIRMADA em `107`.
**O que o catálogo afirma:** "FAISS (gratuito, open source, escala a milhões, suporte a GPU). Alternativas: Pinecone (gerenciado), Chroma (leve), Qdrant (performance)"
**Confere com a fonte:** sim — CONFIRMADA em `107`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "FAISS… escala a milhões, suporte a GPU" | print (texto observado, via `107`) | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |

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

### AC-04-PRT-010 — `Rag + langchain6.png` *(slide 6/11 — recuperação)*

**Tipo:** PRINT · **Área:** 04_MEMORIA-E-CONHECIMENTO · **Série:** RAG+LangChain
**Hash F0:** `428FAB1581B02D29`   **Hash reconferido:** `428FAB1581B02D29`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`107`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-04-PRT-010 · `H-P1-002` (relatório `107`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Exemplo isolado com trecho de código (`db.as_retriever(search_type="similarity", search_kwargs={"k": 5})`) e três ajustes, sem corpus nem medição (`107`, CONFIRMADA) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e sua data |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial ou instrução ao leitor |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhum eval que sustente a escolha de `k`; o slide 9 da série trata de avaliação | — |
| E15 Alegações ⚠ | 1 | Alegações numéricas sem método: `k = 5` como padrão e faixa 3–10, sem corpus declarado | — |

**NF = 1 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente o núcleo da pergunta central: **como recupera** | — |
| E04 Transferibilidade | 3 | Os três parâmetros de ajuste (número de trechos, estratégia, limiar de score) transferem com adaptação declarada | — |
| E14 Diferencial | 2 | Agregação de material público amplamente conhecido | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 1,1 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `107` + linha do `_CONTEUDO.md` | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (chamada com `k=5`, faixa 3–10, `similarity` ou `mmr`, `score_threshold`) conferido; CONFIRMADA em `107`.
**O que o catálogo afirma:** "`db.as_retriever(search_type=“similarity”, search_kwargs={“k”: 5})`. Ajustes: k entre 3 e 10, `similarity` ou `mmr`, `score_threshold`"
**Confere com a fonte:** sim — CONFIRMADA em `107`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "k entre 3 e 10" | print (texto observado, via `107`) | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4. A lacuna dos números já está nomeada e endereçada em `AC-04-PRT-004` e `AC-04-PRT-007`, e **não é contada três vezes**.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-04-PRT-011 — `Rag + langchain7.png` *(slide 7/11 — geração, conceito)*

**Tipo:** PRINT · **Área:** 04_MEMORIA-E-CONHECIMENTO · **Série:** RAG+LangChain
**Hash F0:** `3AE7D462D72F47EC`   **Hash reconferido:** `3AE7D462D72F47EC`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`107`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-04-PRT-011 · `H-P1-002` (relatório `107`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Exemplo isolado: três estratégias de cadeia (`stuff`, `map_reduce`, `refine`) com trade-off declarado, sem execução (`107`, CONFIRMADA) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e sua data |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial ou instrução ao leitor |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhum eval comparando as três estratégias | — |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas (rápido / mais contexto / mais completo, porém lento); nenhum número decisivo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: como o material recuperado é combinado para responder | — |
| E04 Transferibilidade | 3 | O trade-off entre as três estratégias transfere com adaptação declarada | — |
| E14 Diferencial | 2 | Agregação de material público amplamente conhecido | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 1.000,1 KB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `107` + linha do `_CONTEUDO.md` | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (as três estratégias e seus trade-offs) conferido; CONFIRMADA em `107`.
**O que o catálogo afirma:** "Chain types: `stuff` (rápido, contexto limitado) · `map_reduce` (mais contexto) · `refine` (mais completo, lento)"
**Confere com a fonte:** sim — CONFIRMADA em `107`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| — nenhuma alegação numérica identificada neste slide | `107` | — | — |

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

### AC-04-PRT-012 — `Rag + langchain8.png` *(slide 8/11 — geração, implementação)*

**Tipo:** PRINT · **Área:** 04_MEMORIA-E-CONHECIMENTO · **Série:** RAG+LangChain
**Hash F0:** `0D30D673BB76C9E8`   **Hash reconferido:** `0D30D673BB76C9E8`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`107`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-04-PRT-012 · `H-P1-002` (relatório `107`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Exemplo isolado e não reprodutível: trecho de código com cliente, modelo e cadeia nomeados. `107` registra explicitamente que **o código não foi testado** | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e sua data — o trecho fixa um modelo e uma API específicos |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial. **Registrado**: o trecho usa um cliente que exige chave de API, e `107` não relata chave visível | — |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | O código não foi testado (`107`); resolveria obter a fonte primária e um ambiente isolado — o que esta frente **não** faz | — |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas; nenhum número decisivo em jogo além de `temperature=0`, que é parâmetro, não resultado | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central com o fecho do pipeline — a montagem da cadeia de resposta | — |
| E04 Transferibilidade | 2 | O **padrão** transfere; a implementação fixa provedor e modelo específicos | — |
| E14 Diferencial | 2 | Agregação de material público amplamente conhecido | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 807 KB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `107` + linha do `_CONTEUDO.md` | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (cliente, temperatura, modelo e tipo de cadeia) conferido; CONFIRMADA em `107`, com a ressalva registrada de que o código não foi testado.
**O que o catálogo afirma:** "`ChatGroq` com `temperature=0`, `gemma2-9b-it`; `RetrievalQA.from_chain_type(chain_type=“stuff”)`"
**Confere com a fonte:** sim — CONFIRMADA em `107`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "O código não foi testado." | `107` (ressalva da trilha Codex) | FATO OBSERVADO sobre a cobertura | — coerente com `05` §7.4: nenhuma fonte do acervo pode ser executada |

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

### AC-04-PRT-013 — `Rag + langchain9.png` *(slide 9/11 — avaliação)*

**Tipo:** PRINT · **Área:** 04_MEMORIA-E-CONHECIMENTO · **Série:** RAG+LangChain
**Hash F0:** `0E0A210948211FA4`   **Hash reconferido:** `0E0A210948211FA4`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`107`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-04-PRT-013 · `H-P1-002` (relatório `107`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Exemplo isolado: três métricas de qualidade, uma cadeia de avaliação nomeada, três métricas automáticas e duas modalidades de avaliação, sem conjunto de dados nem resultado (`107`, CONFIRMADA) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e sua data |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial ou instrução ao leitor |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | **Este é o slide sobre avaliação, e ainda assim não exibe nenhum eval executado nem conjunto de dados.** Resolveria obter a fonte primária com um caso concreto |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas (quais métricas usar); nenhum número decisivo em jogo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central pelo lado que os demais slides deixam em aberto: **como saber se a recuperação está funcionando** | — |
| E04 Transferibilidade | 3 | A tríade fidelidade / relevância / qualidade de recuperação, mais avaliação humana e contínua, transfere com adaptação declarada | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto no acervo: é o único material que nomeia métricas de avaliação de recuperação | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 1,2 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `107` + linha do `_CONTEUDO.md` | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (as três métricas, `QAEvalChain`, BLEU/ROUGE/BERTScore, avaliação humana e contínua com teste A/B) conferido; CONFIRMADA em `107`.
**O que o catálogo afirma:** "Métricas: fidelidade à fonte, relevância, qualidade do retrieval. `QAEvalChain`. Automática (BLEU, ROUGE, BERTScore), humana e contínua (teste A/B)"
**Confere com a fonte:** sim — CONFIRMADA em `107`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "nenhum valor padrão de RAG entra sem conjunto de avaliação e medição" | `107` (porta candidata da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | não |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 3` · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> **Nota de conjunto da série (não substitui as fichas):** os doze slides estão presentes e íntegros; a série cobre stack, carregamento, pré-processamento, segmentação, embedding, banco, recuperação, geração, avaliação, ajuste e resumo. Duas lacunas de conjunto ficam registradas: **nenhum slide traz corpus, medição ou resultado**, e os valores numéricos são apresentados como padrões sem método.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

> **Cobertura padrão dos VÍDEO desta área:** ficha visual de 9 quadros (4%–92%) em `97` sob `H-M2-003`; ficha STT individual em `TRANSCRICOES-BRUTAS-STT/04_MEMORIA-E-CONHECIMENTO/`, sob `H-M3-001` e manifesto `117`. **LV3-V + LV3-A não produz LV4.** Nenhum binário aberto por esta frente. Fala automática é **provável, nunca citação exata**.

### AC-04-VID-001 — `Gravando 2026-07-28 153509.mp4`

**Tipo:** VÍDEO · **Área:** 04_MEMORIA-E-CONHECIMENTO
**Hash F0:** `072AA736BED616CB`   **Hash reconferido:** `072AA736BED616CB`   **Confere:** sim
**LV:** LV3-V *(LV3-A = `SEM FALA LEXICAL CONFIÁVEL`, 1 palavra, p = 0,998 — confiança alta sobre uma única palavra, sem valor lexical)*
**Cobertura da leitura:** 9 quadros (`97`); ficha STT (42,8 s).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-04-VID-001 · `H-M2-003` (`97`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Comparação exibida em tela de três padrões com trade-off declarado — RAG recupera trechos de base vetorial; CAG pré-carrega núcleo estável em cache; MAG mantém memória de trabalho, episódica e semântica entre sessões —, mais riscos nomeados (latência, perda de contexto em chunks, memória obsoleta, privacidade, complexidade). Exemplo isolado, sem medição (`97`) | — |
| E03 Maturidade | ND | — | Identificar as implementações reais dos três padrões e inspecionar seu estágio |
| E05 Manutenção | ND | — | Localizar o canal de publicação com data |
| E06 Segurança ⚠ | ND | — | Nenhuma superfície inspecionada; "privacidade" e "memória obsoleta" são riscos **retratados**, não avaliados |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | `97` registra que os quadros "simplificam arquiteturas diferentes e **não mostram evals**"; resolveria obter a fonte primária com comparação medida |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas (o que cada padrão faz e arrisca); nenhum número decisivo em jogo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: separa três estratégias de memória e recuperação que a própria pasta trata como decisão em aberto | — |
| E04 Transferibilidade | 3 | A distinção entre os três padrões transfere com adaptação declarada; independe de fornecedor | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto no acervo: é o único item que **contrasta** as três estratégias no mesmo quadro, em vez de defender uma | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 19,7 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado ("Título pelo conteúdo visível") **e confirmado** pelos quadros: os três padrões e seus papéis correspondem ao observado (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 153509.mp4` | 19,7 MB | RAG × CAG × MAG: recuperação, cache e memória evolutiva | não transcrito"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "**Achado alto:** arquitetura híbrida sugerida pelo material — CAG para identidade/núcleo e RAG para cauda longa — é uma hipótese a testar, não decisão." | `97` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) · `HIPÓTESE` | não |
| "os comparativos de RAG/CAG/MAG precisam de revisão técnica: os quadros simplificam arquiteturas diferentes e não mostram evals" | `_CONTEUDO.md` área 04 | ALEGAÇÃO DO CATÁLOGO | **conferida** — `97` chega à mesma leitura |

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

### AC-04-VID-002 — `Gravando 2026-07-28 153951.mp4`

**Tipo:** VÍDEO · **Área:** 04_MEMORIA-E-CONHECIMENTO
**Hash F0:** `60A03F8E7E2BA907`   **Hash reconferido:** `60A03F8E7E2BA907`   **Confere:** sim
**LV:** LV3-V + LV3-A
**Cobertura da leitura:** 9 quadros (`97`); transcrição automática bruta integral (39,4 s, `pt`, 12 segmentos, p = 0,881, **ALTA AUTOMÁTICA**). Sem revisão humana.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-04-VID-002 · `H-M2-003` (`97`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Demonstração isolada: a interface do produto de terceiro aparece nos quadros e a fala provável descreve o mecanismo — uma skill de fechamento que salva a conversa ao fim da sessão e recupera por busca semântica. Nenhum arquivo, skill ou medição acompanha (`97`) | — |
| E03 Maturidade | ND | — | Identificar a skill de fechamento demonstrada e inspecionar seu estágio |
| E05 Manutenção | ND | — | Localizar o canal de publicação com data |
| E06 Segurança ⚠ | ND | — | **Superfície declarada e não inspecionada**: salvar a conversa inteira em plataforma de terceiro. Resolveria inspecionar a skill e o destino dos dados |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhum eval que sustente "custo de token muito menor"; resolveria medir localmente |
| E15 Alegações ⚠ | 0 | A proposta central **depende** de alegações fortes **sem fonte**: "memória infinita", "custo de Tolkien muito menor", "acabou a sobrecarga de contexto" (LV3-A, 00:00:02–00:00:39). Nenhuma é verificável com o material disponível | — |

**NF = 1 · 2/7 · 5 ND** *(mediana de [0,2] = 1)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: propõe um mecanismo concreto de persistência entre sessões — salvar ao fechar, recuperar por busca semântica | — |
| E04 Transferibilidade | 2 | O **padrão** (skill de fechamento + recuperação semântica) transfere; a implementação depende de conta em produto de terceiro | — |
| E14 Diferencial | 2 | Agregação: converge com `AC-04-REP-002` (captura por hook) e `AC-04-REP-005` (mesma plataforma de terceiro), ambos com ficha própria e mais evidência | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 38 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT de 12 segmentos; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 0** — **DIVERGENTE.** O catálogo descreve este ID como "**Agent View do Claude Code: histórico/memória e consumo de tokens**". A fonte — quadros (`97`) e fala provável integral — trata de **conectar o agente a uma plataforma de pesquisa de terceiro para servir de memória**, com uma skill de fechamento; não há Agent View nem painel de consumo de tokens no material observado. A fonte prevalece (`05` §5.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 153951.mp4` | 38,0 MB | Agent View do Claude Code: histórico/memória e consumo de tokens | não transcrito"
**Confere com a fonte:** **não** — divergência registrada

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Eu acabei de dar pro cloud memória infinita." | LV3-A bruto, 00:00:02,800–00:00:05,520 — **fala provável, não citação exata** | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "de repente o cloud ganha um segundo cérebro que nunca esquece" | LV3-A bruto, 00:00:15,080–00:00:20,160 — fala provável | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "Memória que atravessa toda a sessão, custo de Tolkien muito menor" | LV3-A bruto, 00:00:20,160–00:00:24,240 — fala provável (o motor grafou "Tolkien" por "token") | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "esse único setup muda tudo" | LV3-A bruto, 00:00:36,240–00:00:39,360 — fala provável | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |
| **V7** | **sim** | `E15 = 0` e a proposta depende das alegações → teto EXIGE PESQUISA |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** V7 (§8) — teto EXIGE PESQUISA. `NC = 0` é achado sobre o catálogo e **não** rebaixa a fonte (`04` §6.1.4).
**Se EXIGE PESQUISA — lacuna nomeada:** o ganho de custo alegado ("muito menor") não tem medição, e o destino dos dados da conversa salva não é declarado.  **Verificação que a fecharia:** medir localmente o consumo com e sem a estratégia, sobre tarefas próprias; e ler os termos de tratamento de dados da plataforma citada antes de qualquer envio de conversa.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-04-VID-003 — `Gravando 2026-07-28 160036.mp4`

**Tipo:** VÍDEO · **Área:** 04_MEMORIA-E-CONHECIMENTO
**Hash F0:** `4E5BCDA42E08CC58`   **Hash reconferido:** `4E5BCDA42E08CC58`   **Confere:** sim
**LV:** LV3-V + LV3-A
**Cobertura da leitura:** 9 quadros (`97`); transcrição automática bruta integral (79,3 s, `en`, 15 segmentos, p = 0,936, **ALTA AUTOMÁTICA**). Sem revisão humana.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-04-VID-003 · `H-M2-003` (`97`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Demonstração isolada: grafo de pessoas, funções, departamentos, atribuições e tarefas, com perfil individual e relações navegáveis; a fala provável desenvolve o requisito de **controle de acesso por papel** ("you can't have someone in sales accessing part of the HR brain"). Nenhum esquema, dado ou implementação acompanha (`97`) | — |
| E03 Maturidade | ND | — | `97` registra que "o produto não pôde ser identificado visualmente"; resolveria identificar a implementação e inspecionar seu estágio |
| E05 Manutenção | ND | — | Localizar o canal de publicação com data |
| E06 Segurança ⚠ | ND | — | **Superfície declarada e não inspecionada, de alta sensibilidade**: dados de pessoas, credenciais profissionais, projetos e estratégia, com segregação por papel apenas **afirmada**. Resolveria inspecionar o modelo de autorização real |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhum teste do controle de acesso exibido — e é justamente o que precisaria de teste |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas; nenhum número decisivo em jogo na fala provável | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: memória corporativa orientada a **entidades e relações**, com a distinção explícita entre cérebro pessoal e cérebro de empresa | — |
| E04 Transferibilidade | 3 | O padrão (grafo de pessoas × projetos × permissões) transfere com adaptação declarada; a implementação não foi identificada | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto no acervo: é o único item que trata **segregação de acesso** dentro da memória, e não apenas acumulação | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 74,4 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT de 15 segmentos; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado **e confirmado** por duas evidências: os quadros (`97`) e a fala provável, que trata exatamente de pesquisa sobre pessoas e equipes dentro de uma organização (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 160036.mp4` | 74,4 MB | grafo de conhecimento para pesquisa de pessoas e equipes | não transcrito"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "you can't have someone in sales accessing part of the HR brain and data that they aren't allowed to see" | LV3-A bruto, 00:00:18,400–00:00:23,520 — **fala provável, não citação exata** | ALEGAÇÃO DO AUTOR | não — requisito declarado, implementação não inspecionada |
| "this is probably the best way to structure more enterprise AI brain chat kind of use cases" | LV3-A bruto, 00:01:02,560–00:01:09,840 — fala provável | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "I don't think Obsidian can probably cut it but I'd love to know what you think." | LV3-A bruto, 00:01:14,240–00:01:18,640 — fala provável | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA`; **contrasta** com AC-04-PRT-001 e AC-04-VID-006, que defendem o oposto |
| "O produto não pôde ser identificado visualmente; não promover ferramenta." | `97` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | — |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 3` · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4 (o produto não é identificável, logo não há artefato externo nomeado a verificar).
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-04-VID-004 — `Gravando 2026-07-28 163142.mp4`

**Tipo:** VÍDEO · **Área:** 04_MEMORIA-E-CONHECIMENTO
**Hash F0:** `607F24F1952C9EFB`   **Hash reconferido:** `607F24F1952C9EFB`   **Confere:** sim
**LV:** LV3-V *(LV3-A = `SEM FALA LEXICAL CONFIÁVEL`, 1 palavra, p = 0,130)*
**Cobertura da leitura:** 9 quadros (`97`); ficha STT (12,9 s).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-04-VID-004 · `H-M2-003` (`97`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Fluxo exibido em tela com saída estruturada declarada: carregar PDFs na plataforma de fontes; gerar tabela comparando **métodos, achados, limitações, lacunas e citações**; entregar a tabela ao agente como pacote fechado; pedir crítica e perguntas novas apenas a partir das evidências fornecidas. Exemplo isolado, sem os PDFs nem a tabela (`97`) | — |
| E03 Maturidade | ND | — | Identificar as ferramentas demonstradas e inspecionar seu estágio |
| E05 Manutenção | ND | — | Localizar o canal de publicação com data |
| E06 Segurança ⚠ | ND | — | Nenhuma superfície inspecionada; o envio de PDFs a plataforma de terceiro é superfície retratada |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhum eval que sustente "zero alucinação"; resolveria medir sobre corpus próprio |
| E15 Alegações ⚠ | 0 | A proposta **depende** de promessas fortes **sem fonte** que `97` registra literalmente: "**zero alucinação**" e ganhos de velocidade. Não verificáveis com o material disponível | — |

**NF = 1 · 2/7 · 5 ND** *(mediana de [0,2] = 1)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central com um princípio operacional: **separar a preparação fundamentada de evidências do raciocínio e da redação** | — |
| E04 Transferibilidade | 3 | O padrão (pacote fechado de evidências com colunas fixas, entregue ao raciocinador) transfere com adaptação declarada | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto no acervo: é o único item que define **o formato da entrega de evidência** entre duas etapas do trabalho | — |

**RP = 3 · 3/3 · 0 ND**

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
**NC = 5** — método declarado **e confirmado** pelos quadros; o `_CONTEUDO.md` acrescenta a leitura correta do fluxo ("usa NotebookLM como banco de fontes/citações e Claude para a redação final"), que confere com `97` (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 163142.mp4` | 6,6 MB | pesquisa acadêmica com NotebookLM + Claude | não transcrito"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "zero alucinação" | `97` (texto visual observado) | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "**Achado alto:** separar preparação fundamentada de evidências de raciocínio/redação." | `97` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | não |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |
| **V7** | **sim** | `E15 = 0` e a proposta depende da promessa → teto EXIGE PESQUISA |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** V7 (§8) — teto EXIGE PESQUISA.
**Se EXIGE PESQUISA — lacuna nomeada:** a promessa de "zero alucinação" não tem medição, dado nem definição operacional.  **Verificação que a fecharia:** experimento próprio com um conjunto de perguntas cuja resposta correta é conhecida, medindo taxa de afirmação não sustentada pelas fontes fornecidas.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-04-VID-005 — `Gravando 2026-07-28 163335.mp4`

**Tipo:** VÍDEO · **Área:** 04_MEMORIA-E-CONHECIMENTO
**Hash F0:** `214B28CBD48F4AA1`   **Hash reconferido:** `214B28CBD48F4AA1`   **Confere:** sim
**LV:** LV3-V *(LV3-A = `SEM FALA LEXICAL CONFIÁVEL`, 1 palavra, p = 0,751)*
**Cobertura da leitura:** 9 quadros (`97`); ficha STT (5,0 s — um dos vídeos mais curtos do acervo).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-04-VID-005 · `H-M2-003` (`97`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Diagrama isolado contrastando RAG convencional com uma composição que soma busca vetorial e contexto pré-processado em cache. Sem medição, custo ou execução (`97`) | — |
| E03 Maturidade | ND | — | Identificar a implementação e inspecionar seu estágio |
| E05 Manutenção | ND | — | Localizar o canal de publicação com data |
| E06 Segurança ⚠ | ND | — | Nenhuma superfície inspecionada | — |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | `97` registra que faltam "custos, invalidação, segurança e benchmark"; resolveria obter a fonte primária com medição |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas; nenhum número decisivo em jogo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: propõe a composição "núcleo estável em cache + recuperação dinâmica" | — |
| E04 Transferibilidade | 3 | A composição transfere com adaptação declarada; independe de fornecedor | — |
| E14 Diferencial | 1 | Conveniência: é o mesmo conteúdo de `AC-04-VID-001` reduzido a um diagrama, na mesma remessa e na mesma área | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 1,7 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado **e confirmado** pelos quadros: o contraste "RAG × RAG+CAG" corresponde ao diagrama observado (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 163335.mp4` | 1,7 MB | diagrama RAG × RAG+CAG | não transcrito"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "reforça o híbrido “núcleo estável em cache + recuperação dinâmica”; faltam custos, invalidação, segurança e benchmark" | `97` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | não |

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

### AC-04-VID-006 — `Gravando 2026-07-28 203247.mp4`

**Tipo:** VÍDEO · **Área:** 04_MEMORIA-E-CONHECIMENTO
**Hash F0:** `CEA0728F4FD810B6`   **Hash reconferido:** `CEA0728F4FD810B6`   **Confere:** sim
**LV:** LV3-V *(LV3-A = `SEM FALA LEXICAL CONFIÁVEL`, 1 palavra, p = 0,751)*
**Cobertura da leitura:** 9 quadros (`97`); ficha STT (19,3 s).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-04-VID-006 · `H-M2-003` (`97`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Arranjo exibido em tela: vault como memória do negócio, agente como analista e automação como executor; um arquivo de instruções no vault reunindo negócio, clientes, projetos, voz, metas e calendário; briefings matinais e pré-reunião, finanças e revisões automatizados. Exemplo isolado, sem arquivos (`97`) | — |
| E03 Maturidade | ND | — | Identificar a implementação e inspecionar seu estágio |
| E05 Manutenção | ND | — | Localizar o canal de publicação com data |
| E06 Segurança ⚠ | ND | — | **Superfície declarada e não inspecionada, de alta sensibilidade**: dados pessoais, de clientes, financeiros e segredos, com execução desassistida. Resolveria inspecionar permissões, retenção e gatilhos reais |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhum teste das rotinas automatizadas exibido | — |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas; nenhum número decisivo em jogo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: memória operacional do negócio orientada a eventos e rituais, e não apenas a documentos | — |
| E04 Transferibilidade | 3 | O arranjo transfere com adaptação declarada; os produtos citados são substituíveis | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto no acervo: liga a memória a **rituais operacionais datados** (briefing matinal, pré-reunião, revisão), e não a consultas sob demanda | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 6,2 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado **e confirmado** pelos quadros (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 203247.mp4` | 6,2 MB | sistema de conhecimento empresarial no Obsidian | não transcrito"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "**Riscos altos:** dados pessoais, clientes, finanças, segredos, permissões, retenção e execução desassistida." | `97` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | não |

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

### AC-04-VID-007 — `Gravando 2026-07-28 213812.mp4`

**Tipo:** VÍDEO · **Área:** 04_MEMORIA-E-CONHECIMENTO
**Hash F0:** `931B1B1D8B4D69A9`   **Hash reconferido:** `931B1B1D8B4D69A9`   **Confere:** sim
**LV:** LV3-V + LV3-A
**Cobertura da leitura:** 9 quadros (`97`); transcrição automática bruta integral (53,5 s, `pt`, 11 segmentos, p = 0,892, **ALTA AUTOMÁTICA**). Sem revisão humana.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-04-VID-007 · `H-M2-003` (`97`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só narrativa: a tese — de que o conjunto de arquivos de instrução vale o quanto vale a arquitetura que ele descreve — é sustentada apenas por argumentação falada, sem código, projeto ou medição (`97`; fala provável integral) | — |
| E03 Maturidade | ND | — | Identificar o projeto retratado e inspecionar seu estágio |
| E05 Manutenção | ND | — | Localizar o canal de publicação com data |
| E06 Segurança ⚠ | ND | — | Nenhuma superfície inspecionada | — |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | A fala provável afirma que o código "passa nos testes" e ainda assim degrada a arquitetura — afirmação que exigiria um caso medido, ausente |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas; nenhum número decisivo em jogo | — |

**NF = 1 · 2/7 · 5 ND** *(mediana de [1,3] = 2 → §14.3 vale o inferior)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central por um ângulo que nenhum outro item cobre: **o que precisa estar escrito** para que a memória do projeto seja útil — fronteiras entre módulos, dependências permitidas, limites de domínio | — |
| E04 Transferibilidade | 3 | O critério transfere com adaptação declarada; independe de linguagem e de fornecedor | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto no acervo: é o único item que **subordina** o conjunto de arquivos de contexto à qualidade da decisão de arquitetura que ele registra | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 45 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT de 11 segmentos; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado **e confirmado** por duas evidências: os quadros (`97`) e a fala provável, que trata exatamente de arquitetura de contexto em arquivos (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 213812.mp4` | 45,0 MB | arquitetura de contexto e arquivos em projetos com IA | não transcrito"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "O harnes é tão bom quanto a arquitetura que ele descreve, porque a arquitetura também é harnes." | LV3-A bruto, 00:00:11–00:00:18 — **fala provável, não citação exata** | ALEGAÇÃO DO AUTOR | não |
| "Se tu não sabe explicar a fronteira entre os modos do teu sistema… a AI também não sabe." | LV3-A bruto, 00:00:18–00:00:27 — fala provável | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "Ela vai gerar um código que passa nos testos, parece bom, mas apodrece a tua arquitetura" | LV3-A bruto, 00:00:27–00:00:33 — fala provável | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "o harnes dos markdowns é a parte fácil" | LV3-A bruto, 00:00:33–00:00:36 — fala provável | ALEGAÇÃO DO AUTOR | não. **Converge** com `AC-02-VID-010`; convergência não é verificação |

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

### AC-04-VID-008 — `Gravando 2026-07-28 214526.mp4`

**Tipo:** VÍDEO · **Área:** 04_MEMORIA-E-CONHECIMENTO
**Hash F0:** `6D3E3AE21B5A5C6A`   **Hash reconferido:** `6D3E3AE21B5A5C6A`   **Confere:** sim
**LV:** LV3-V *(LV3-A = `SEM FALA LEXICAL CONFIÁVEL`, 2 palavras, p = 0,565)*
**Cobertura da leitura:** 9 quadros (`97`); ficha STT (41,7 s).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-04-VID-008 · `H-M2-003` (`97`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Demonstração isolada: documentação oficial de um produto transformada em notas atômicas e conexões, aberta como vault, com recomendação de copiar as fontes e ligar cada nota à origem. Sem o artefato nem os dados (`97`) | — |
| E03 Maturidade | ND | — | Identificar o repositório de "Graphify" e inspecionar versão e estabilidade |
| E05 Manutenção | ND | — | Localizar o repositório de origem e verificar atividade datada |
| E06 Segurança ⚠ | ND | — | **Superfície declarada e não inspecionada**: uma ferramenta que lê documentação e escreve um vault. Resolveria inspecionar o código e as permissões |
| E07 Licença ⚠ | ND | — | Identificar o repositório e ler o texto da licença |
| E13 Testes/evals | ND | — | Nenhum teste exibido; nenhuma verificação de que as conexões geradas são corretas |
| E15 Alegações ⚠ | 1 | Alegações numéricas fortes com fonte citada — o próprio produto — porém não conferidas e não conferíveis: "**145 documentos, 591 ideias, 685 conexões e 67 grupos**" (`97`) | — |

**NF = 1 · 2/7 · 5 ND** *(mediana de [1,2] = 1,5 → §14.3 vale o inferior)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: converte documento em grafo consultável, com **proveniência preservada** — cada nota ligada à origem | — |
| E04 Transferibilidade | 2 | O **padrão** (derivar grafo preservando origem) transfere; a implementação depende de um produto não identificado | — |
| E14 Diferencial | 2 | Agregação: forma cluster com `AC-02-VID-009`, `AC-02-VID-011` e `AC-04-VID-012`, todos sobre o mesmo produto e o mesmo arranjo | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 10,3 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado **e confirmado** pelos quadros (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 214526.mp4` | 10,3 MB | Graphify + Obsidian como grafo de conhecimento | não transcrito"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Alega 145 documentos, 591 ideias, 685 conexões e 67 grupos." | `97` (texto visual observado) | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "**Achado alto:** grafo derivado precisa preservar proveniência verificável." | `97` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | não |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** §9 — relevância aparente com lacuna nomeada e endereçável; teto de V2/V4 respeitado.
**Se EXIGE PESQUISA — lacuna nomeada:** identidade, repositório e licença de "Graphify" — o mesmo produto citado em `AC-02-VID-009` e `AC-02-VID-011`.  **Verificação que a fecharia:** localizar o repositório público, ler licença e README e mapear o que a ferramenta lê e escreve — **sem clonar nem executar**. Lacuna contada **uma vez** para os quatro itens do cluster.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-04-VID-009 — `Gravando 2026-07-29 085933.mp4`

**Tipo:** VÍDEO · **Área:** 04_MEMORIA-E-CONHECIMENTO
**Hash F0:** `224277B42AD1F4C6`   **Hash reconferido:** `224277B42AD1F4C6`   **Confere:** sim
**LV:** LV3-V *(LV3-A = `SEM FALA LEXICAL CONFIÁVEL`, 1 palavra, p = 0,751)*
**Cobertura da leitura:** 9 quadros (`97`); ficha STT (24,9 s).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-04-VID-009 · `H-M2-003` (`97`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só listagem: sete plugins nomeados e seis rotinas sugeridas (síntese matinal, cruzamento de ideias, kickoff, auditoria do vault, processamento noturno, múltiplos vaults), sem configuração, execução ou medição (`97`) | — |
| E03 Maturidade | ND | — | Identificar cada plugin e inspecionar seu estágio |
| E05 Manutenção | ND | — | Verificar a atividade de cada plugin na origem |
| E06 Segurança ⚠ | ND | — | **Superfície declarada, crítica e não inspecionada**: plugins e um servidor MCP com acesso à memória, mais rotina desassistida. `97` nomeia injeção de prompt, exfiltração e cadeia de suprimentos. Resolveria inspecionar cada plugin |
| E07 Licença ⚠ | ND | — | Ler a licença de cada plugin na origem |
| E13 Testes/evals | ND | — | Nenhum teste exibido |
| E15 Alegações ⚠ | 1 | Alegações com fonte citada (nomes de plugin e "Official Obsidian Skills") porém não conferidas: `97` registra que "números e autoria de “Official Obsidian Skills” não foram verificados" | — |

**NF = 1 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça a pergunta de forma genérica: lista extensões sem particularizar como a memória é indexada ou recuperada | — |
| E04 Transferibilidade | 2 | O **padrão** (rotinas periódicas sobre o vault) transfere; os plugins são específicos de um produto | — |
| E14 Diferencial | 2 | Agregação de material público; sobrepõe AC-04-PRT-001 e AC-04-VID-006 | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 6,9 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado **e confirmado** pelos quadros: plugins e workflows correspondem ao observado (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-29 085933.mp4` | 6,9 MB | plugins e workflows do Obsidian para segundo cérebro | não transcrito"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Smart Connections, Copilot, Templater, Dataview, Tasks, Periodic Notes e `mcpvault`" | `97` (texto visual observado) | ALEGAÇÃO DO AUTOR | não — nenhum identificado ou inspecionado |
| "**Risco crítico:** plugins e MCP com acesso à memória, rotina desassistida, injeção de prompt, exfiltração e cadeia de suprimentos." | `97` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | não |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** §9 — relevância aparente com lacuna nomeada e endereçável; teto de V2/V4 respeitado.
**Se EXIGE PESQUISA — lacuna nomeada:** identidade, licença e escopo de permissão dos sete plugins nomeados, com atenção especial ao servidor MCP que teria acesso ao vault.  **Verificação que a fecharia:** localizar cada plugin na origem pública e ler licença e permissões declaradas — **sem instalar**.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-04-VID-010 — `Gravando 2026-07-29 092503.mp4`

**Tipo:** VÍDEO · **Área:** 04_MEMORIA-E-CONHECIMENTO
**Hash F0:** `57F4F34055387EC2`   **Hash reconferido:** `57F4F34055387EC2`   **Confere:** sim
**LV:** LV3-V + LV3-A
**Cobertura da leitura:** 9 quadros (`97`); transcrição automática bruta integral (63,1 s, `pt`, 21 segmentos, p = 0,881, **ALTA AUTOMÁTICA**). Sem revisão humana.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-04-VID-010 · `H-M2-003` (`97`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Demonstração isolada de cinco práticas nomeadas, com procedimento declarado para cada uma: documento de requisitos antes do prompt; modo de planejamento com revisão antes da execução; arquivo de instruções do projeto; compactação de histórico; e skills reutilizáveis. Nenhum arquivo acompanha (`97` + fala provável) | — |
| E03 Maturidade | ND | — | Localizar o projeto retratado e inspecionar seu estágio |
| E05 Manutenção | ND | — | Localizar o canal de publicação com data |
| E06 Segurança ⚠ | ND | — | Nenhuma superfície inspecionada | — |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhum teste exibido; a revisão do plano é humana e não medida | — |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas ("todo iniciante deveria saber e quase ninguém usa"); nenhum número decisivo em jogo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central em dois pontos: o arquivo de instruções como memória durável do projeto e a compactação como gestão de histórico | — |
| E04 Transferibilidade | 3 | As cinco práticas transferem com adaptação declarada; independem de projeto | — |
| E14 Diferencial | 2 | Agregação: as cinco práticas reaparecem em AC-02-VID-012, AC-03-VID-011 e AC-05-VID-005 dentro do acervo | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 50,9 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT de 21 segmentos; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 2** — **PARCIAL.** O método é declarado e o tema geral confere — o vídeo trata mesmo de regras de contexto e de eficiência sem perder memória —, mas há **omissão material**: a fonte apresenta **cinco práticas numeradas e explicitamente anunciadas como tais** (documento de requisitos, modo de planejamento, arquivo de instruções, compactação e skills), e o catálogo condensa tudo em uma frase temática. Detalhe verificável parcialmente não conferido → teto 2 (§14.4).
**O que o catálogo afirma:** "`Gravando 2026-07-29 092503.mp4` | 50,9 MB | engenharia de contexto: regras e eficiência sem perder memória | não transcrito"
**Confere com a fonte:** parcialmente

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Cinco segredos do Cloud Code que todo iniciante deveria saber e quase ninguém usa." | LV3-A bruto, 00:00:00–00:00:04,260 — **fala provável, não citação exata** | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "Quanto mais contexto, mais o Cloud entrega o que você quer de verdade." | LV3-A bruto, 00:00:12,580–00:00:15,860 — fala provável | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA`; **contrasta** com AC-08-VID-002 e AC-08-VID-008, que sustentam o oposto — janela cheia degrada resposta |
| "Depois de muito tempo na mesma conversa, o Cloud começa a perder desempenho." | LV3-A bruto, 00:00:40,980–00:00:43,860 — fala provável | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |

> **Contradição registrada dentro do próprio acervo:** este item afirma "quanto mais contexto, melhor" e, na área 08, `AC-08-VID-008` exibe um gráfico de queda de qualidade conforme a janela enche. As duas afirmações não foram verificadas; nenhuma prevalece por repetição.

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

### AC-04-VID-011 — `segundo cérebro.mp4`

**Tipo:** VÍDEO · **Área:** 04_MEMORIA-E-CONHECIMENTO
**Hash F0:** `7E78FB9B5FC4D07D`   **Hash reconferido:** `7E78FB9B5FC4D07D`   **Confere:** sim
**LV:** LV3-V + LV3-A
**Cobertura da leitura:** 9 quadros (`97`); transcrição automática bruta integral (52,1 s, `pt`, 17 segmentos, p = 0,898, **ALTA AUTOMÁTICA**). Sem revisão humana.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-04-VID-011 · `H-M2-003` (`97`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Estrutura de diretórios exibida em tela — `vault/` com arquivo de instruções, `memory/`, `pessoas/`, `projects/`, `decisoes/` e `agents/` — mais o ciclo declarado: ler instruções e memória no início, acessar o vault durante a sessão, atualizar `memory/` ao final, retomar na sessão seguinte. Exemplo isolado, sem os arquivos (`97`) | — |
| E03 Maturidade | ND | — | Localizar a implementação real e inspecionar seu estágio |
| E05 Manutenção | ND | — | Localizar o canal de publicação com data |
| E06 Segurança ⚠ | ND | — | **Superfície declarada**: um diretório `pessoas/` com dados de terceiros e um agente com acesso de escrita a `memory/`. Resolveria inspecionar permissões e política de retenção reais |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhuma verificação de que o que é salvo em `memory/` é correto — `97` registra que "acumulação não equivale a verdade" | — |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas na fala provável; nenhum número decisivo em jogo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 4 | Endereça diretamente a pergunta central **mais** artefato concreto e reutilizável (§14.2): a **estrutura de diretórios nomeada** é um esquema copiável, não apenas uma descrição | — |
| E04 Transferibilidade | 4 | Transferível por configuração: são pastas e arquivos de texto, sem dependência de código ou fornecedor | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto no acervo: nomeia o **ciclo completo** — bootstrap, trabalho, consolidação e retomada —, que os demais itens tratam por partes | — |

**RP = 4 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 50,3 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT de 17 segmentos; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 1** — o item está na tabela "Vídeos (NÃO são legíveis por IA)" com a coluna "Assunto": descrição derivada do nome do arquivo (`segundo cérebro.mp4` → "construção de segundo cérebro"), sem indício de inspeção. Compatível com o conteúdo, mas compatibilidade não eleva a nota (§6, âncora 1).
**O que o catálogo afirma:** "`segundo cérebro.mp4` | 53 MB | construção de segundo cérebro"
**Confere com a fonte:** sim, em nível genérico

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "um segundo cérebro é um monte de arquivo em ponte md, empilhado, organizado para o teu cloud code ler" | LV3-A bruto, 00:00:09,300–00:00:17,300 — **fala provável, não citação exata** (o motor grafou "ponte md" por ".md") | ALEGAÇÃO DO AUTOR | não |
| "é salvar todo o contexto de todas as sessões que você já teve" | LV3-A bruto, 00:00:18,400–00:00:22,600 — fala provável | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "**Risco:** acumulação não equivale a verdade; exige fonte, validade, expiração, acesso e revisão." | `97` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | não |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 3` · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4 (o esquema de diretórios é o próprio valor; não há artefato externo nomeado a verificar).
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-04-VID-012 — `segundo cérebro2.mp4`

**Tipo:** VÍDEO · **Área:** 04_MEMORIA-E-CONHECIMENTO
**Hash F0:** `A847A783DACBEDD4`   **Hash reconferido:** `A847A783DACBEDD4`   **Confere:** sim
**LV:** LV3-V + LV3-A
**Cobertura da leitura:** 9 quadros (`97`); transcrição automática bruta integral (37,1 s, `pt`, 14 segmentos, p = 0,867, **ALTA AUTOMÁTICA**). Sem revisão humana.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-04-VID-012 · `H-M2-003` (`97`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Demonstração isolada: grafo com comunidades e conexões, produzido a partir de um acervo pessoal; a fala provável quantifica o acervo. Nenhum dado, esquema ou execução acompanha (`97`) | — |
| E03 Maturidade | ND | — | Identificar a ferramenta que produziu o grafo e inspecionar seu estágio |
| E05 Manutenção | ND | — | Localizar o canal de publicação com data |
| E06 Segurança ⚠ | ND | — | **Superfície declarada**: um agente com acesso a 300 arquivos, 24 pessoas mapeadas e 36 decisões, com escrita autônoma de aprendizados | — |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhuma verificação da qualidade das conexões geradas | — |
| E15 Alegações ⚠ | 1 | Alegações numéricas fortes com fonte citada — o próprio acervo do autor — porém não conferidas e **não conferíveis** com o material disponível: "280 linhas de instruções, 79 arquivos de memória, 4 pessoas mapeadas, 36 decisões, mais de 160 notas diárias" (LV3-A) contra "cerca de 300 arquivos, 24 pessoas e mais de 160 notas" (`97`, visual) | — |

**NF = 1 · 2/7 · 5 ND** *(mediana de [1,2] = 1,5 → §14.3 vale o inferior)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: demonstra recuperação **relacional** — a fala provável diz que o agente "sabe onde tá, porque eu organizei tudo em pastas que ela entende" | — |
| E04 Transferibilidade | 2 | O **padrão** transfere; os números e a organização são do acervo do autor | — |
| E14 Diferencial | 1 | Conveniência: `97` registra "forte sobreposição temática com AC-04-VID-008 e AC-04-VID-011", ambos na mesma área | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 35,3 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT de 14 segmentos; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 1** — "Assunto" derivado do nome do arquivo (`segundo cérebro2.mp4` → "continuação"), sem indício de inspeção e sem informação de conteúdo. É a descrição menos informativa da área.
**O que o catálogo afirma:** "`segundo cérebro2.mp4` | 37 MB | continuação"
**Confere com a fonte:** sim, em nível genérico — é de fato o segundo vídeo da dupla

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "280 linhas de instruções, 79 arquivos de memória, de 4 pessoas mapeadas, 36 decisões, mais de 160 notas diárias" | LV3-A bruto, 00:00:17,820–00:00:22,460 — **fala provável, não citação exata** | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA`. **Divergência interna registrada**: `97` lê "cerca de 300 arquivos, **24** pessoas" nos quadros, contra "**4** pessoas" na fala provável — o STT pode ter perdido um dígito, e nenhum dos dois foi confirmado |
| "Aí a conhece o seu negócio, ela tá fingindo." | LV3-A bruto, 00:00:00–00:00:02,320 — fala provável | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "Ela mesmo salva os próprios aprendizados." | LV3-A bruto, 00:00:34,160–00:00:36,280 — fala provável | ALEGAÇÃO DO AUTOR | não — escrita autônoma em memória, sem revisão declarada |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4. A ferramenta que produziu o grafo não é identificada, e a lacuna correspondente já está nomeada em `AC-04-VID-008`.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

## Fechamento da área 04

| Métrica | Valor |
|---|---:|
| Itens representados | 32 / 32 |
| Fichas válidas contra `04` §13 | 32 |
| Hashes / estruturas reconferidos · divergentes | 32 · **0** |
| Itens em **LV4** | 7 (os 7 repositórios) |
| `RF = CANDIDATO FORTE` | 3 — AC-04-REP-002, AC-04-REP-004, AC-04-REP-006 |
| `RF = CANDIDATO A PILOTO` | 0 |
| `RF = PADRÃO A ESTUDAR` | 0 |
| `RF = EXIGE PESQUISA` | 9 |
| `RF = REFERÊNCIA` | 20 |
| `RF = INDETERMINADO` | 0 |
| Total de eixos possíveis (32 × 15) | 480 |
| Eixos determinados | 347 |
| Eixos em `ND` | **133 (27,7%)** *(recontado por ferramenta sobre as fichas em 2026-07-29; o valor anterior, 167, era estimativa e foi corrigido — ver `99_RELATORIO-DA-FASE-2.md` §6)* |
| Divergências catálogo × fonte | **1 divergente** (`NC = 0`: AC-04-VID-002) · **4 parciais** (AC-04-PRT-008, AC-04-REP-006, AC-04-VID-010, mais o atributo "pago" corrigido por `107`) |

**Achados registrados nesta área, sem resolução silenciosa:**

1. **A decisão em aberto que o próprio catálogo declara** — pasta de markdown sem banco vetorial (`AC-04-REP-001`), RAG próprio (série `AC-04-PRT-002` a `013`) e RAG hospedado por terceiro (`AC-04-REP-005`) — permanece **em aberto** ao fim da Fase 2. As três vias têm ficha própria, e nenhuma foi escolhida: escolher seria decidir arquitetura, o que esta frente não pode fazer.
2. **`AC-04-REP-003`** satisfaz simultaneamente as condições de entrada de **EXIGE PESQUISA** e de **PADRÃO A ESTUDAR**, e §9 não dá regra de precedência → **DEF-13**.
3. **`AC-04-REP-005`** declara modo **anti-detecção** contra um serviço de terceiro como funcionalidade — único caso do acervo, fora da área 06, em que a evasão é apresentada como benefício. `E06 = 1`, V2 disparada.
4. **Contradição entre itens do acervo:** `AC-04-VID-010` afirma "quanto mais contexto, melhor"; `AC-08-VID-008` exibe queda de qualidade com o preenchimento da janela. Nenhuma das duas foi verificada.
5. **`AC-04-REP-007`** é o segundo dos quatro casos I-04 (licença ausente na raiz efetiva) tratados nesta fase.

Nenhuma fonte foi modificada. Nenhum repositório foi executado, instalado ou importado. Nenhum item foi adotado, ordenado, priorizado ou recomendado.
