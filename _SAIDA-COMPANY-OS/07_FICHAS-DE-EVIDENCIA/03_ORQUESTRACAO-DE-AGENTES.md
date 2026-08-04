> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

# FICHAS DE EVIDÊNCIA — ÁREA 03 — ORQUESTRAÇÃO DE AGENTES

**Fase:** 2 — Extração · **Data:** 2026-07-29 · **Avaliador:** Claude Opus 5 (Fase 2)
**Itens:** 31 — 10 REPO · 8 PRINT · 13 VÍDEO · 0 PLANILHA
**Convenções de aplicação:** `00_INDICE-DA-FASE-2.md` §3

**Pergunta central da área (base de E01):** *como os agentes coordenam trabalho entre si — quem decide, quem executa, quem revisa.*

**Cobertura padrão dos REPO desta área** (teto de `05` §8, ≤ 8 arquivos): listagem da raiz efetiva · texto de `LICENSE` · `README` (até 6 KB do início, com o total declarado) · manifesto de dependências · `CHANGELOG`/`RELEASE-NOTES`/`VERSION` quando presente · listagem do diretório de testes/evals · presença de `.env.example`, `SECURITY.md`, `Dockerfile`, instaladores. **Código-fonte não foi lido em massa; nenhum repositório foi executado ou instalado.**

---

### AC-03-REP-001 — `codex-plugin-cc-main`

**Tipo:** REPO · **Área:** 03_ORQUESTRACAO-DE-AGENTES
**Hash F0:** `dir · 63 arq.`   **Hash reconferido:** `63 arq. · aninhamento 0`   **Confere:** sim (reconferência estrutural, `05` §6)
**LV:** LV4
**Cobertura da leitura:** raiz efetiva `codex-plugin-cc-main` (12 entradas); `LICENSE` — Apache License 2.0, 10.944 bytes, íntegro; `README.md` (10.907 bytes, lidos os primeiros 6 KB: comandos, requisitos, instalação, uso de `/codex:review`, `/codex:adversarial-review`, `/codex:rescue`, `/codex:transfer`); `package.json` integral; `.claude-plugin/` (`marketplace.json`); `tests/` — 10 arquivos listados. **Não lidos:** `plugins/`, `scripts/`, `.github/`.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** não se aplica

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 4 | Artefato completo e inspecionável (comandos, subagente `codex:codex-rescue`, manifesto de marketplace) **mais** procedimento de verificação declarado: `"test": "node --test tests/*.test.mjs"` e 10 arquivos em `tests/`. Não executado por esta frente | — |
| E03 Maturidade | 3 | `"version": "1.0.6"` em `package.json`, com scripts `bump-version` e `check-version` de controle de versão. Sem `CHANGELOG` na raiz efetiva | — |
| E05 Manutenção | ND | — | Consultar a origem pública (`openai/codex-plugin-cc`): datas de commit, issues e cadência. Cópia estática sem histórico |
| E06 Segurança ⚠ | 3 | Superfície declarada com controles parciais documentados: o README afirma literalmente "This command is read-only and will not perform any changes" para `/codex:review` e `/codex:adversarial-review`; delega execução a um binário externo (`@openai/codex`) sob credencial do usuário; `--background` e `/codex:cancel` dão controle de execução. **Código de `plugins/` não lido** | — |
| E07 Licença ⚠ | 4 | Permissiva padrão presente e íntegra na raiz efetiva: `LICENSE` = Apache License 2.0 (10.944 bytes, cabeçalho canônico lido), com `NOTICE` acompanhante e `"license": "Apache-2.0"` no `package.json`. **Não chega a 5**: cópia local não prova titularidade (`04` §5, E07) | — |
| E13 Testes/evals | 3 | `tests/` inspecionado: 10 arquivos (`broker-endpoint`, `commands`, `git`, `process`, `render`, `runtime`, `state`, `bump-version`, mais dois utilitários), com ponto de entrada declarado (`npm test`). Nenhum eval de comportamento de agente | — |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas no README ("the same quality of code review as running `/review` inside Codex directly"); nenhum número decisivo em jogo. Requisitos declarados de forma verificável (Node ≥ 18.18, assinatura ChatGPT ou chave de API) | — |

**NF = 3 · 6/7 · 1 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 4 | Endereça diretamente a pergunta central — **quem revisa** — **mais** artefato concreto e reutilizável (§14.2): comandos com contrato declarado, incluindo revisão adversarial dirigível e um subagente de delegação | — |
| E04 Transferibilidade | 4 | Transferível por **configuração**, sem alteração de código: instalação por marketplace e uso por slash command. Premissa de ambiente declarada (assinatura ChatGPT ou chave de API) impede a nota 5 | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto **dentro do acervo**: é o único item que entrega revisão adversarial **por modelo de outro fornecedor** como artefato oficial, impedindo que um modelo valide o próprio trabalho | — |

**RP = 4 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 4 | Instalação declarada em um comando (`/plugin install codex@openai-codex`), configuração por comando (`/codex:setup`). Não alcança 5: exige serviço externo obrigatório (Codex/OpenAI) | — |
| E09 Custo | 3 | Custo variável por uso, com controle possível: o README declara "Usage will contribute to your Codex usage limits" e admite assinatura gratuita; o limite é do provedor, não do artefato | — |
| E10 Contexto/tokens | 3 | Medido: **63 arquivos, 374,2 KB**. Tamanho fecharia a âncora 4 (< 1 MB), contagem fecha a âncora 3 (50–300 arquivos); vale **a pior das duas** (`04` §5, E10) | — |
| E11 Fornecedor | 2 | Fornecedor único por desenho — o artefato existe para acoplar Claude Code a Codex/OpenAI —, porém com formato de dados aberto (saída textual de revisão, sessões `.jsonl` importáveis) | — |
| E12 Reversibilidade | 3 | Reversível por remoção do plugin, com efeitos colaterais documentados: `/codex:transfer` cria thread persistente no Codex e `--background` deixa jobs em execução, com `/codex:status` e `/codex:cancel` declarados | — |

**AA = 3 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (os sete comandos, na ordem) e o detalhe **confere**: todos aparecem no README lido. Não chega a 4 porque o `_CONTEUDO.md` não declara o método.
**O que o catálogo afirma:** "Plugin oficial da OpenAI. Comandos: `/codex:review` (revisão somente leitura), `/codex:adversarial-review` (revisão de desafio), `/codex:rescue`, `/codex:transfer`, `/codex:status`, `/codex:result`, `/codex:cancel`."
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Plugin oficial da OpenAI" | `_CONTEUDO.md` área 03 | ALEGAÇÃO DO CATÁLOGO | **parcialmente conferida**: `package.json` declara `"name": "@openai/codex-plugin-cc"` e o marketplace `openai/codex-plugin-cc` — fato observado na fonte; a oficialidade na origem pública não foi verificada |
| "This command is read-only and will not perform any changes." | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — `plugins/` não lido |
| "Usage will contribute to your Codex usage limits." | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não |
| "**O que extrair:** o padrão de **revisão adversarial por um modelo de outro fornecedor**." | `_CONTEUDO.md` área 03 | ALEGAÇÃO DO CATÁLOGO | não |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V2 · V3 · V4 · V5 · V6 · V7 · V8 | **nenhuma** | `E06 = 3` · `E07 = 4` · `LV = 4` · 1 ND de 15 · `E15 = 3` · reconferência estrutural confere |

#### Resultado
**RF = CANDIDATO FORTE**
**Regra que produziu:** §9, condições de entrada de CANDIDATO FORTE, todas satisfeitas: `LV = 4 ≥ 4` · nenhum eixo do Bloco A abaixo de 3 (mínimo 3) · `E06 = 3 ≥ 3` · `E07 = 4 ≥ 3` · **1 ND** ≤ 2 · `RP = 4 ≥ 4`.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> **CANDIDATO FORTE não significa adotar.** Significa: pronto para avaliação pelos Frameworks oficiais 1.11–1.19, fora desta frente. Lacuna remanescente registrada: `E05 = ND` (manutenção) e `plugins/` não inspecionado.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-03-REP-002 — `ECC-main`

**Tipo:** REPO · **Área:** 03_ORQUESTRACAO-DE-AGENTES
**Hash F0:** `dir · 3322 arq. · aninhado`   **Hash reconferido:** `3322 arq. · aninhamento 1`   **Confere:** sim
**LV:** LV4
**Cobertura da leitura:** raiz efetiva `ECC-main/ECC-main` (78 entradas listadas); `LICENSE` — MIT, 1.071 bytes, "Copyright (c) 2026 Affaan Mustafa", íntegro; `README.md` (90.528 bytes — lidos os primeiros 6 KB: badges, aviso de fontes oficiais, proposta, matriz de harnesses, patrocínio); `package.json` (parcial) e `pyproject.toml` (parcial); `CHANGELOG.md` (cabeçalho e entrada `2.0.0 - 2026-06-09`); `.claude-plugin/`; `tests/` — 192 arquivos, topo listado; sinais `.env.example`, `SECURITY.md`, `install.sh`, `install.ps1`. **Não lidos:** os 3.322 arquivos de conteúdo, `skills/`, `agents/`, `docs/`.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** não se aplica

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 4 | Artefato completo e inspecionável (skills, agents, hooks, `mcp-configs/`, `manifests/`, `schemas/`) **mais** procedimento de verificação declarado: `tests/` com 192 arquivos, incluindo `ci`, `integration`, `plugin-manifest.test.js`, `codex-config.test.js` e `conftest.py`; `pytest`/`ruff`/`mypy` em `optional-dependencies.dev` | — |
| E03 Maturidade | 4 | Versionado com release identificável (`"version": "2.0.0"`, arquivo `VERSION`, `CHANGELOG.md` com `## 2.0.0 - 2026-06-09`) **mais** documentação de instalação e uso (`install.sh`, `install.ps1`, `TROUBLESHOOTING.md`, três guias) **mais** tratamento de erro visível na configuração (`.gitleaksignore`, `commitlint`, `.markdownlint.json`). Não alcança 5: nenhuma política de compatibilidade declarada foi observada | — |
| E05 Manutenção | 4 | Atividade recente por evidência datada **dentro da fonte** (`CHANGELOG.md`: `2.0.0 - 2026-06-09` e seção `Unreleased` referindo auditoria de junho de 2026) **mais** responsável nomeado (`author.name: "Affaan Mustafa"`) **mais** canal de reporte declarado (`bugs.url` para issues, `SECURITY.md`, Discord). Este é o **caso excepcional** previsto em `04` §5 E05 — a maioria dos repositórios do acervo permanece ND | — |
| E06 Segurança ⚠ | 3 | Superfície declarada (instaladores de shell/PowerShell, hooks, configurações MCP, escaneamento de código) **com controles parciais documentados**: `SECURITY.md`, `.gitleaksignore`, `the-security-guide.md`, pacote `ecc-agentshield`, e aviso literal no README restringindo canais de instalação. **Código não lido** — a nota mede a superfície documentada | — |
| E07 Licença ⚠ | 4 | Permissiva padrão presente e íntegra na raiz efetiva: MIT, 1.071 bytes, titular nomeado; `"license": "MIT"` em `package.json` e `pyproject.toml`. Cópia local não prova titularidade → teto 4 | — |
| E13 Testes/evals | 3 | `tests/` inspecionado: 192 arquivos com subdiretórios `ci`, `commands`, `docs`, `hooks`, `integration`, `lib`, `scripts` e ponto de entrada declarado por `pytest` em `pyproject.toml`. Nenhum eval de comportamento de agente identificado na listagem | — |
| E15 Alegações ⚠ | 1 | Alegações numéricas fortes com fonte citada porém **não conferível com o material disponível**: "**211.9K+ stars** \| **32.5K+ forks** \| **230+ contributors** \| **12+ language ecosystems**" e "evolved over 10+ months of intensive daily use". As fontes são badges apontando para `api.ecc.tools` e GitHub, fora do alcance desta frente | — |

**NF = 4 · 7/7 · 0 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 4 | Endereça diretamente a pergunta central **mais** artefato concreto e reutilizável: publica o mesmo conjunto de instruções para 18 diretórios de harness distintos (`.claude/`, `.codex/`, `.cursor/`, `.gemini/`, `.hermes/`, `.kimi/`, `.zed/`, `.opencode/`, `.openclaw/`…), com `manifests/` e `schemas/` | — |
| E04 Transferibilidade | 4 | Transferível por configuração, sem alteração de código: o conteúdo é skill/hook/rule em Markdown e JSON, instalado por script; `llm-abstraction` declara camada agnóstica de provedor | — |
| E14 Diferencial | 4 | Sem equivalente pronto no acervo **mais** custo alto de reconstrução: 3.322 arquivos de curadoria acumulada cobrindo múltiplos harnesses; nenhum outro item do acervo cobre mais de dois | — |

**RP = 4 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 4 | Instalação declarada em um comando (`install.sh` / `install.ps1`, pacotes npm `ecc-universal` e `ecc-agentshield`), configuração por arquivo. Não alcança 5: exige um harness hospedeiro | — |
| E09 Custo | 4 | Custo marginal: o repositório é MIT e gratuito; o próprio README declara "OSS stays free", com `ECC Pro` a US$ 19/assento **opcional** para repositórios privados. O custo recorrente é o das chamadas de modelo já previstas | — |
| E10 Contexto/tokens | 1 | Medido: **3.322 arquivos, 43,7 MB**. Contagem fecha a âncora 1 (1.000–5.000 arquivos) e o tamanho também (20–100 MB) | — |
| E11 Fornecedor | 4 | Abstração de fornecedor documentada: sete harnesses declarados no README, `mcp-configs/mcp-servers.json` com conectores opt-in e `pyproject.toml` de `llm-abstraction` ("Provider-agnostic LLM abstraction layer", com `anthropic` e `openai` como dependências) | — |
| E12 Reversibilidade | 3 | Reversível por remoção, com efeitos colaterais documentados: os instaladores escrevem em diretórios de configuração de harness; o `CHANGELOG` registra alteração de conectores padrão como mudança de comportamento | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (3.322 arquivos, 15+ harnesses, documentação em português em `docs/pt-BR/README.md`) e o detalhe **confere**: a contagem bate com a reconferência estrutural e o README lista o link para `docs/pt-BR/README.md`.
**O que o catálogo afirma:** "O maior item do acervo: **3.322 arquivos**, com configuração para 15+ harnesses diferentes… Tem versão de documentação em português (`docs/pt-BR/README.md`). **Como ler sem se afogar:** não varra os 3.322 arquivos."
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "**211.9K+ stars** \| **32.5K+ forks** \| **230+ contributors**" | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA`; **P-3**: popularidade não move nenhum eixo |
| "Production-ready agents, skills, hooks, rules, MCP configurations… evolved over 10+ months of intensive daily use building real products." | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "**Official sources only.** … Third-party re-uploads and unofficial mirrors are not maintained or reviewed by the project and may contain malware." | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não. **Registrada como achado**: o item no acervo **é** uma cópia local, fora dos canais que o próprio autor declara verificados |
| "OSS stays free. This repo is MIT-licensed forever." | `README.md` da fonte | ALEGAÇÃO DO AUTOR | licença MIT presente na cópia — o "forever" não é verificável |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V2 · V3 · V4 · V5 · V6 · V7 · V8 | **nenhuma** | `E06 = 3` · `E07 = 4` · `LV = 4` · 0 ND · `E15 = 1` (≠ 0) · reconferência estrutural confere |

#### Resultado
**RF = CANDIDATO A PILOTO**
**Regra que produziu:** §9. **Não** alcança CANDIDATO FORTE porque `E15 = 1` está abaixo de 3 no Bloco A. Satisfaz CANDIDATO A PILOTO: `LV ≥ 3` · `E06 = 3 ≥ 3` · `E07 = 4 ≥ 3` · `RP = 4 ≥ 3` · **0 ND** ≤ 4 · nenhum eixo do Bloco C em 0 (`E10 = 1`).
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> **CANDIDATO A PILOTO não significa pilotar.** Significa: pronto para *proposta* de piloto à avaliação oficial. Restrição registrada na própria ficha: `E10 = 1` — o item exige 3.322 arquivos e 43,7 MB de superfície.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-03-REP-003 — `gstack-Ahacad-main`  ·  POSSÍVEL DUPLICATA

**Tipo:** REPO · **Área:** 03_ORQUESTRACAO-DE-AGENTES
**Hash F0:** `dir · 1176 arq.`   **Hash reconferido:** `1176 arq. · aninhamento 0`   **Confere:** sim
**LV:** LV4 **sobre o delta**
**Cobertura da leitura:** **ficha de delta** (`05` §10): sobrepõe 99,4% do conteúdo de `AC-03-REP-004`, cuja avaliação é herdada para a parte comum. Foi lido apenas o que difere — listagem da raiz efetiva (99 entradas, contra 97 do original); `LICENSE` (MIT, 1.066 bytes, "Copyright (c) 2026 **Garry Tan**"); `README.md` **integral** (967 bytes — é o arquivo que difere por inteiro); `package.json`; `SKILL.md`; `.claude-plugin/plugin.json`; presença de `.gitmodules`, `vendor/`, `hooks/`, `.gitlab-ci.yml`. Sobreposição medida na Fase 0: **99,4%**, delta de **7 arquivos de empacotamento**.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** não se aplica

#### Bloco A — Fonte *(apenas o delta)*
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 3 | Artefato completo e inspecionável correspondente à afirmação do delta — `.claude-plugin/plugin.json`, `hooks/`, `vendor/gstack` como submódulo e `skills/` por symlink —, **sem** procedimento de verificação próprio do wrapper | — |
| E03 Maturidade | 3 | `"version": "1.60.1.0"` e `CHANGELOG.md` presentes na raiz — herdados do upstream vendorizado; o wrapper declara o mesmo número | — |
| E05 Manutenção | ND | — | Consultar a origem pública `ahacad/gstack` para atividade **do wrapper**. O `CHANGELOG` datado (`2026-07-09`) pertence ao upstream, não ao delta |
| E06 Segurança ⚠ | 2 | Superfície ampla **sem controle documentado no delta**: o README declara que "`hooks/` — SessionStart hook builds the browse binary and creates backward-compat symlinks", isto é, compilação e criação de symlinks disparadas no início de sessão. Nenhum `SECURITY.md`, nenhum escopo de permissão declarado no wrapper | — |
| E07 Licença ⚠ | ND | — | **Titularidade ambígua**: o `LICENSE` da raiz é o MIT do upstream, "Copyright (c) 2026 Garry Tan", enquanto o repositório é o wrapper de outro autor; os 7 arquivos do delta não declaram titular. `04` §5 E07: titularidade ambígua ⇒ ND. Resolveria ler a licença e a atribuição na origem pública `ahacad/gstack` |
| E13 Testes/evals | ND | — | `test/` contém 352 arquivos, todos do upstream vendorizado; nenhum teste específico do wrapper foi identificado na listagem de topo. Resolveria enumerar `test/` procurando cobertura de `hooks/`, symlinks e `plugin.json` |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas no README de 967 bytes ("No fork divergence. Upstream changes flow through"); nenhum número decisivo em jogo | — |

**NF = 3 · 4/7 · 3 ND** *(mediana dos determinados [2,3,3,3] = 3)*

#### Bloco B — Relevância potencial *(apenas o delta)*
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | O delta endereça de forma genérica: **distribuição** de um conjunto de skills como plugin, não a coordenação entre agentes que a área pergunta | — |
| E04 Transferibilidade | 2 | O **padrão** (submódulo + symlinks + manifesto de plugin) é transferível; a implementação depende do upstream específico | — |
| E14 Diferencial | 1 | Conveniência sobre algo que já existe e já é acessível: 99,4% do conteúdo é `AC-03-REP-004` | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção *(apenas o delta)*
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 4 | Instalação declarada em um comando (`claude plugin add ahacad/gstack`), com alternativa manual documentada | — |
| E09 Custo | 4 | Custo marginal: apenas as chamadas de modelo já previstas pelo upstream | — |
| E10 Contexto/tokens | 1 | Medido: **1.176 arquivos, 53 MB** — contagem na faixa 1.000–5.000 e tamanho na faixa 20–100 MB | — |
| E11 Fornecedor | 2 | Fornecedor único por desenho (plugin de Claude Code), porém com formato de dados aberto (skills em Markdown) | — |
| E12 Reversibilidade | 3 | Reversível por remoção do plugin, com efeitos colaterais documentados no README: symlinks e binário construído pelo hook | — |

**AA = 3 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 0** — **DIVERGENTE.** O catálogo afirma "**Nenhum conteúdo original.**" e, com base nisso, instrui a não analisar. Fato observado contradiz: o delta contém **7 arquivos de empacotamento** medidos na Fase 0 (`plugin.json`, `hooks/`, `.gitmodules`, workflow de upstream, `.gitlab-ci.yml` e README próprio de 967 bytes). Conteúdo original existe, é pequeno e é justamente o que esta ficha avalia. A fonte prevalece (`05` §5.1.5, `04` §14.5.5).
**O que o catálogo afirma:** "`gstack-Ahacad-main/` — DUPLICATA, pode pular. É apenas um wrapper de plugin do `gstack-garrytan-main`, com submódulo git e symlinks. Nenhum conteúdo original. **Não analise.**"
**Confere com a fonte:** **não**

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "**Não analise.**" | `_CONTEUDO.md` área 03 | ALEGAÇÃO DO CATÁLOGO + `DECISÃO DE ESCOPO DE TERCEIRO` | **instrução não obedecida** (`04` §14.5.1 e §14.5.4): o item recebeu ficha com o mesmo rigor dos demais. Este é o caso que originou o defeito DEF-05 na Fase 1 |
| "Nenhum conteúdo original." | `_CONTEUDO.md` área 03 | ALEGAÇÃO DO CATÁLOGO | **contradita por fato observado** → `NC = 0` |
| "No fork divergence. Upstream changes flow through with `git submodule update --remote`." | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — o submódulo não foi resolvido nem atualizado |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V2 · V3 · V5 · V6 · V7 · V8 | não | `E06 = 2` (≠ 0 e ≠ ND, logo V2 **não** dispara) · `E07 ≠ 0` · `LV = 4` · 3 ND de 15 · `E15 = 3` · reconferência estrutural confere |
| **V4** | **sim** | `E07 = ND` por titularidade ambígua → nunca CANDIDATO FORTE nem CANDIDATO A PILOTO |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** V4 (§8) somada à condição de entrada de EXIGE PESQUISA (§9): relevância aparente do delta com lacuna nomeada e endereçável. **Não é `DUPLICADO`**: `DUPLICADO` exige hash idêntico ou sobreposição total; aqui a sobreposição é 99,4%, e `05` §10 manda avaliar apenas o delta.
**Se EXIGE PESQUISA — lacuna nomeada:** titularidade e licença dos 7 arquivos do delta — o `LICENSE` presente é o do upstream e nomeia outro titular.  **Verificação que a fecharia:** ler a licença e a atribuição de autoria no repositório público `ahacad/gstack`, e confirmar se o wrapper declara titular próprio.

> **Herança:** tudo que não é delta herda a avaliação de `AC-03-REP-004`, sem ser reavaliado (`05` §10).

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-03-REP-004 — `gstack-garrytan-main`

**Tipo:** REPO · **Área:** 03_ORQUESTRACAO-DE-AGENTES
**Hash F0:** `dir · 1171 arq.`   **Hash reconferido:** `1171 arq. · aninhamento 0`   **Confere:** sim
**LV:** LV4
**Cobertura da leitura:** raiz efetiva `gstack-garrytan-main` (97 entradas); `LICENSE` — MIT, 1.066 bytes, "Copyright (c) 2026 Garry Tan", íntegro; `README.md` (45.212 bytes — lidos os primeiros 6 KB: tese, números de produtividade, proposta dos 23 especialistas, quick start, instalação, modo de equipe, integração OpenClaw); `package.json` (scripts, incluindo `test`, `test:evals`, `test:e2e`); `SKILL.md` (frontmatter e preâmbulo); `CHANGELOG.md` (entrada `[1.60.1.0] - 2026-07-09` com tabela de métricas); `test/` — 352 arquivos, topo listado; `.env.example`. **Não lidos:** os 23 diretórios de skill, `lib/`, `browse/`, `docs/`.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** não se aplica

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 4 | Artefato completo e inspecionável (23 diretórios de skill, binários `browse` e `make-pdf`, `ARCHITECTURE.md`, `DESIGN.md`, `ETHOS.md`) **mais** procedimento de verificação declarado e explícito: `test`, `test:free`, `test:windows`, `test:evals`, `test:e2e` em `package.json`, sobre `test/` com 352 arquivos. Não executado por esta frente | — |
| E03 Maturidade | 4 | Versionado com release identificável (`"version": "1.60.1.0"`, arquivo `VERSION`, `CHANGELOG.md`) **mais** documentação de instalação e uso (`README`, `setup`, `USING_GBRAIN_WITH_GSTACK.md`) **mais** tratamento de erro visível na configuração: o preâmbulo de `SKILL.md` usa `2>/dev/null || true` e valores padrão em cada chamada | — |
| E05 Manutenção | 4 | Atividade recente por evidência datada **dentro da fonte**: `CHANGELOG.md` com `[1.60.1.0] - 2026-07-09`, vinte dias antes desta avaliação, descrevendo regressões corrigidas e medições reproduzíveis **mais** responsável nomeado (Garry Tan, no `LICENSE` e no README) **mais** canal declarado (`CONTRIBUTING.md`, repositório público citado) | — |
| E06 Segurança ⚠ | 3 | Superfície declarada com controles parciais documentados: existe um papel de segurança dedicado (`cso/`) e o README declara auditorias OWASP + STRIDE; `.env.example` em vez de segredo versionado; `guard/`, `freeze/`, `unfreeze/` e `careful/` são controles de execução nomeados. **Contrapeso registrado**: a instalação recomendada consiste em colar um `git clone … && ./setup` para o próprio agente executar, e o modo de equipe **commita** `.claude/` e `CLAUDE.md` no repositório do usuário — superfície de cadeia de suprimentos declarada, não inspecionada | — |
| E07 Licença ⚠ | 4 | Permissiva padrão presente e íntegra na raiz efetiva: MIT, 1.066 bytes, titular nomeado; `"license": "MIT"` em `package.json`. Cópia local não prova titularidade → teto 4 | — |
| E13 Testes/evals | 4 | `test/` inspecionado: 352 arquivos, com ponto de entrada declarado **mais** evals de comportamento de agente — `test/skill-llm-eval.test.ts`, `test/skill-e2e-*.test.ts`, `test/skill-routing-e2e.test.ts`, `test/codex-e2e.test.ts`, `test/gemini-e2e.test.ts`, executados por `test:evals` com `EVALS=1`. Não alcança 5: resultados não publicados na fonte de forma reprodutível por esta frente | — |
| E15 Alegações ⚠ | 4 | Alegações numéricas fortes **acompanhadas de método declarado e dados de apoio dentro da própria fonte**: "~810× my 2013 pace (11,417 vs 14 logical lines/day)" e "240× the entire 2013 year" vêm com o critério (mudança lógica, não LOC bruto), o universo medido (40 repositórios `garrytan/*`, excluindo um demo) e um documento de metodologia com script de reprodução (`docs/ON_THE_LOC_CONTROVERSY.md`). **Método declarado ≠ alegação verificada** — nada foi conferido por esta frente | — |

**NF = 4 · 7/7 · 0 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 4 | Endereça diretamente a pergunta central — quem decide, quem executa, quem revisa — **mais** artefato concreto e reutilizável: 23 papéis nomeados como skills em Markdown (`plan-ceo-review`, `plan-eng-review`, `design-review`, `review`, `qa`, `cso`, `ship`, `land-and-deploy`, `retro`…), cada um com diretório próprio | — |
| E04 Transferibilidade | 4 | Transferível por configuração, sem alteração de código: skills em Markdown, instalação por script, `model-overlays/` para troca de modelo. Premissas de ambiente declaradas (Bun, Git, Claude Code) impedem a nota 5 | — |
| E14 Diferencial | 4 | Sem equivalente pronto no acervo **mais** custo alto de reconstrução: a decomposição em 23 papéis com rubricas próprias é curadoria acumulada; nenhum outro item do acervo nomeia papéis com esse grau de especialização | — |

**RP = 4 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 4 | Instalação declarada em um comando (`git clone … && ./setup`, colável no agente), configuração por arquivo. Não alcança 5: exige Bun, Git e um harness hospedeiro | — |
| E09 Custo | 4 | Custo marginal: MIT, sem licença paga; o consumo é o das chamadas de modelo já previstas. `test:evals` tem custo de modelo, mas é opcional e controlado por `EVALS=1` | — |
| E10 Contexto/tokens | 1 | Medido: **1.171 arquivos, 53,1 MB** — contagem na faixa 1.000–5.000 e tamanho na faixa 20–100 MB | — |
| E11 Fornecedor | 3 | Dois ou mais fornecedores suportados, com troca custosa: `model-overlays/`, `codex/` e testes `codex-e2e` e `gemini-e2e` evidenciam suporte além do harness principal, mas o produto é declaradamente "Garry's Stack — **Claude Code** skills" | — |
| E12 Reversibilidade | 3 | Reversível por remoção, com efeitos colaterais documentados: o modo de equipe **commita** `.claude/` e `CLAUDE.md` no repositório do usuário, o que exige reversão explícita em git | — |

**AA = 3 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (23 especialistas e 8 ferramentas, todos como slash commands em Markdown, licença MIT, arquivos-chave `ARCHITECTURE.md`, `DESIGN.md`, `ETHOS.md`, `AGENTS.md`) e o detalhe **confere**: os quatro arquivos-chave existem na raiz efetiva, a licença é MIT e os diretórios de papel estão presentes.
**O que o catálogo afirma:** "De Garry Tan… Transforma o Claude Code em **23 especialistas e 8 ferramentas**, todos como slash commands em Markdown… Licença MIT. **Atenção:** o README abre com números de produtividade próprios do autor (810× o ritmo de 2013). É argumento de venda — ignore os números, fique com a estrutura."
**Confere com a fonte:** sim — inclusive a ressalva sobre os números, que o `README` confirma

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "my 2026 run rate is **~810× my 2013 pace** (11,417 vs 14 logical lines/day)" | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA`; método e script de reprodução declarados em `docs/ON_THE_LOC_CONTROVERSY.md`, não lidos nem executados |
| "Year-to-date (through April 18), 2026 has already produced **240× the entire 2013 year**." | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "Peter Steinberger built OpenClaw — 247K GitHub stars — essentially solo with AI agents." | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA`; **P-3**: popularidade não move eixo. Ver `AC-03-REP-006`, o próprio OpenClaw, que está no acervo |
| "I don't think I've typed like a line of code probably since December" (atribuída a Andrej Karpathy) | `README.md` da fonte | ALEGAÇÃO DO AUTOR (citação de terceiro) | não — `NÃO VERIFICADA` |
| "ignore os números, fique com a estrutura" | `_CONTEUDO.md` área 03 | ALEGAÇÃO DO CATÁLOGO | — coincide com P-3, mas não foi seguida como comando: os números foram registrados e pontuados em E15 |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V2 · V3 · V4 · V5 · V6 · V7 · V8 | **nenhuma** | `E06 = 3` · `E07 = 4` · `LV = 4` · 0 ND · `E15 = 4` · reconferência estrutural confere |

#### Resultado
**RF = CANDIDATO FORTE**
**Regra que produziu:** §9, condições de entrada satisfeitas: `LV = 4` · nenhum eixo do Bloco A abaixo de 3 (mínimo 4) · `E06 = 3` · `E07 = 4` · **0 ND** · `RP = 4`.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> **CANDIDATO FORTE não significa adotar.** Restrições registradas na própria ficha: `E10 = 1` (superfície de 1.171 arquivos), instalação por comando colado em agente e modo de equipe que commita no repositório do usuário.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-03-REP-005 — `hermes-agent-main`

**Tipo:** REPO · **Área:** 03_ORQUESTRACAO-DE-AGENTES
**Hash F0:** `dir · 6265 arq. · aninhado`   **Hash reconferido:** `6265 arq. · aninhamento 1`   **Confere:** sim
**LV:** LV4
**Cobertura da leitura:** raiz efetiva `hermes-agent-main/hermes-agent-main` (74 entradas); `LICENSE` — MIT, 1.070 bytes, "Copyright (c) 2025 Nous Research", íntegro; `README.es.md` (16.820 bytes — lidos os primeiros 6 KB: proposta, tabela de capacidades, instalação por `curl | bash` e `irm | iex`, backends de terminal); `package.json` integral; `pyproject.toml` (cabeçalho, versão, `requires-python`, comentário de política de pinagem); `tests/` — 2.080 arquivos, topo listado; sinais `.env.example`, `SECURITY.md`, `Dockerfile`, `docker-compose.yml`. **Não lidos:** `agent/`, `skills/`, `gateway/`, `providers/`, `docs/`.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** não se aplica

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 4 | Artefato completo e inspecionável (CLI, gateway, TUI, adaptadores ACP, `providers/`, `skills/`, `cron/`) **mais** procedimento de verificação declarado: `tests/` com **2.080 arquivos**, incluindo `e2e`, `ci`, `docker`, `fakes` e `fixtures` | — |
| E03 Maturidade | 4 | Versionado (`version = "0.18.2"` em `pyproject.toml`; `1.0.0` no `package.json` de workspaces) **mais** documentação de instalação e uso (instaladores para Linux/macOS/WSL/Termux/Windows, site de docs, `CONTRIBUTING.md` em duas línguas) **mais** tratamento de erro visível na configuração: `requires-python = ">=3.11,<3.14"` com justificativa escrita de por que o teto é "load-bearing, not cosmetic". Não alcança 5: versão < 1.0 no pacote principal | — |
| E05 Manutenção | 4 | Atividade datada **dentro da fonte**: o comentário de `pyproject.toml` registra "This was tightened on **2026-05-12** in response to the Mini Shai-Hulud worm hitting mistralai 2.4.6 on PyPI" **mais** responsável nomeado (Nous Research, no `LICENSE` e em `authors`) **mais** canal declarado (`bugs.url`, `SECURITY.md`, Discord) | — |
| E06 Segurança ⚠ | 3 | Superfície muito ampla (shell em seis backends — local, Docker, SSH, Singularity, Modal, Daytona —, cron, mensageria em cinco plataformas, navegador) **com controles parciais documentados**: `SECURITY.md` em duas línguas, `.env.example`, `Dockerfile`/`docker-compose` para confinamento, e **pinagem exata de todas as dependências diretas com justificativa antimalware escrita no próprio manifesto**. Não alcança 4: nenhum escopo de permissão explícito foi observado | — |
| E07 Licença ⚠ | 4 | Permissiva padrão presente e íntegra: MIT, 1.070 bytes; `license = "MIT"` e `license-files = ["LICENSE"]` em `pyproject.toml`. Cópia local não prova titularidade → teto 4 | — |
| E13 Testes/evals | 3 | `tests/` inspecionado: 2.080 arquivos com `e2e`, `ci`, `cli`, `cron`, `gateway`, `computer_use`, e ponto de entrada por `pytest` (declarado em `optional-dependencies`). Nenhum eval de comportamento de agente identificado na listagem de topo | — |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas de capacidade; nenhum número decisivo em jogo. A alegação de exclusividade — "**El único** agente con un bucle de aprendizaje integrado" — é registrada abaixo como não verificada, mas não é numérica | — |

**NF = 4 · 7/7 · 0 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 4 | Endereça diretamente a pergunta central — delegação a subagentes isolados, agendamento e handoff entre sessões — **mais** artefato concreto e reutilizável (`cron/`, `acp_adapter/`, `skills/`, `trajectory_compressor.py`) | — |
| E04 Transferibilidade | 4 | Transferível por configuração, sem alteração de código: o README declara troca de modelo por `hermes model`, "sin cambios de código, sin dependencias", com mais de dez provedores nomeados | — |
| E14 Diferencial | 4 | Sem equivalente pronto no acervo **mais** custo alto de reconstrução: é o único item do acervo cujo produto declarado é o **loop de aprendizado** — skill criada a partir da experiência e melhorada durante o uso —, além de compressão de trajetória para treino | — |

**RP = 4 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 4 | Instalação declarada em um comando (`curl -fsSL … \| bash` ou `iex (irm …)`), configuração por `.env` e `cli-config.yaml.example`. Não alcança 5: exige provedor de modelo externo | — |
| E09 Custo | 3 | Custo variável por uso, com limite ou controle possível: o README declara operação em "VPS de $5" e backends serverless que "cuestan casi nada cuando está inactivo" — há custo recorrente de infraestrutura, dimensionável | — |
| E10 Contexto/tokens | **0** | Medido: **6.265 arquivos, 134 MB**. Contagem **acima de 5.000** e tamanho **acima de 100 MB** — a pior âncora do eixo, nas duas medidas | — |
| E11 Fornecedor | 4 | Abstração de fornecedor documentada: `providers/`, troca por `hermes model`, endpoint próprio suportado, compatibilidade com o padrão aberto `agentskills.io` | — |
| E12 Reversibilidade | 3 | Reversível por remoção, com efeitos colaterais documentados: o instalador cria `%LOCALAPPDATA%\hermes\git` isolado, e cron/VMs/containers criados exigem desmontagem explícita | — |

**AA = 3 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (loop de aprendizado, VPS de US$ 5, Telegram, troca de modelo por `hermes model`, sem lock-in) e o detalhe **confere**: todos os pontos aparecem no README lido.
**O que o catálogo afirma:** "Da Nous Research. O único do acervo com **loop de aprendizado embutido**… Roda em VPS de US$ 5 ou cluster de GPU; fala por Telegram enquanto trabalha numa VM. Modelo trocável (`hermes model`), sem lock-in."
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "**El único** agente con un bucle de aprendizaje integrado: crea habilidades a partir de la experiencia, las mejora durante el uso…" | `README.es.md` da fonte | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA`; exclusividade não conferível |
| "Ejecútalo en un VPS de $5, un clúster de GPUs o infraestructura sin servidor que cuesta casi nada cuando está inactivo." | `README.es.md` da fonte | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "OpenRouter (más de 200 modelos)" | `README.es.md` da fonte | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "This was tightened on 2026-05-12 in response to the Mini Shai-Hulud worm hitting mistralai 2.4.6 on PyPI" | `pyproject.toml` da fonte | ALEGAÇÃO DO AUTOR | não verificada quanto ao incidente; **a pinagem exata em si é fato observado** no manifesto |
| "Cruze com `05_SKILLS-E-PROMPTS/one-skill-to-rule-them-all-main`, que resolve o mesmo problema por outro caminho." | `_CONTEUDO.md` área 03 | ALEGAÇÃO DO CATÁLOGO | não conferida nesta ficha — ver `AC-05-REP-006` |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V2 · V3 · V4 · V5 · V6 · V7 · V8 | **nenhuma** | `E06 = 3` · `E07 = 4` · `LV = 4` · 0 ND · `E15 = 3` · reconferência estrutural confere |

#### Resultado
**RF = CANDIDATO FORTE**
**Regra que produziu:** §9, condições de entrada satisfeitas: `LV = 4` · nenhum eixo do Bloco A abaixo de 3 · `E06 = 3` · `E07 = 4` · **0 ND** · `RP = 4`.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> **Contradição do instrumento, registrada como DEF-11.** Este item tem `E10 = 0` — a pior nota possível de superfície de contexto — e ainda assim satisfaz CANDIDATO FORTE, porque §9 só proíbe `Bloco C = 0` em CANDIDATO A PILOTO. O mesmo item **não** poderia ser proposto como piloto. A contradição não foi resolvida em silêncio: está declarada aqui e no relatório final.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-03-REP-006 — `openclaw-main`

**Tipo:** REPO · **Área:** 03_ORQUESTRACAO-DE-AGENTES
**Hash F0:** `dir · 23953 arq. · aninhado`   **Hash reconferido:** `23953 arq. · aninhamento 1`   **Confere:** sim
**LV:** LV4
**Cobertura da leitura:** raiz efetiva `openclaw-main/openclaw-main` (61 entradas); `LICENSE` — MIT, 1.170 bytes, "Copyright (c) 2026 OpenClaw Foundation", íntegro; `README.md` (87.538 bytes — lidos os primeiros 6 KB: proposta, lista de 23 canais, patrocinadores, instalação); `package.json` (parcial); `CHANGELOG.md` (seção `Unreleased` com entradas referenciando números de PR); `test/` — 750 arquivos, topo listado; sinais `.env.example`, `SECURITY.md`, `Dockerfile`, `docker-compose.yml`, `security/`, `.semgrepignore`, `THIRD_PARTY_NOTICES.md`. **Não lidos:** `src/`, `packages/`, `apps/`, `extensions/`, `docs/`.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** não se aplica

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 4 | Artefato completo e inspecionável (monorepo com `apps/`, `packages/`, `extensions/`, `ui/`, `deploy/`) **mais** procedimento de verificação declarado: `test/` com 750 arquivos (`e2e`, `mocks`, `vitest`, `fixtures`), `vitest.config.ts`, `.pre-commit-config.yaml` e workflow de CI referenciado por badge | — |
| E03 Maturidade | 4 | Versionado com release identificável (`"version": "2026.7.2"`, `CHANGELOG.md`, `appcast.xml` de atualização, página de releases) **mais** documentação de instalação e uso (`openclaw onboard`, docs, FAQ, guia Windows) **mais** tratamento de erro visível na configuração (`patches/`, `npm-shrinkwrap.json`, `.oxlintrc.json`) | — |
| E05 Manutenção | 4 | Atividade recente por evidência datada **dentro da fonte**: a versão `2026.7.2` é calendário e situa a cópia em julho de 2026; o `CHANGELOG` traz seção `Unreleased` com PRs numerados e agradecimentos nominais a contribuidores **mais** responsável declarado (OpenClaw Foundation) **mais** canais (`SECURITY.md`, `bugs.url`, Discord) | — |
| E06 Segurança ⚠ | 3 | Superfície declarada, muito ampla (23 canais de mensageria, voz, Canvas ao vivo, gateway como plano de controle, execução em Docker/Fly/Render) **com controles parciais documentados**: `SECURITY.md`, diretório `security/`, `.semgrepignore`, `git-hooks/`, `.pre-commit-config.yaml`, `THIRD_PARTY_NOTICES.md`. **Código não lido** | — |
| E07 Licença ⚠ | 4 | Permissiva padrão presente e íntegra: MIT, 1.170 bytes, titular nomeado; `"license": "MIT"` em `package.json`. Cópia local não prova titularidade → teto 4 | — |
| E13 Testes/evals | 3 | `test/` inspecionado: 750 arquivos com `e2e`, `plugins`, `scripts`, `vitest`, ponto de entrada declarado (`vitest.config.ts`), mais um diretório `qa/` separado. Nenhum eval de comportamento de agente identificado na listagem | — |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas no trecho lido ("If you want a personal, single-user assistant that feels local, fast, and always-on, this is it."); os números presentes são badges de CI e release, não sustentam a proposta | — |

**NF = 4 · 7/7 · 0 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central de uma área, mas pela borda: o padrão observável é **gateway como plano de controle separado do assistente**, com camada de adaptadores de canal — coordenação de superfícies, não de agentes entre si | — |
| E04 Transferibilidade | 4 | Transferível por configuração: `docker-compose.yml`, `fly.toml`, `render.yaml`, `.env.example` e assistente de onboarding; o próprio README declara suporte a npm, pnpm e bun | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto **dentro do acervo**: nenhum outro item entrega camada de adaptadores para 23 canais de mensageria | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 4 | Instalação declarada em um comando (`openclaw onboard`), configuração por arquivo e variável de ambiente. Não alcança 5: requer processo gateway sempre ativo | — |
| E09 Custo | 3 | Custo variável por uso, com limite ou controle possível: sem licença paga (MIT), mas exige host sempre ligado (Docker, Fly, Render declarados) além das chamadas de modelo | — |
| E10 Contexto/tokens | **0** | Medido: **23.953 arquivos, 289,3 MB** — o maior item do acervo em contagem de arquivos. Acima de 5.000 arquivos e de 100 MB nas duas medidas | — |
| E11 Fornecedor | 4 | Abstração de fornecedor documentada: "many providers and models are supported", com nota de preferência e assinatura OAuth opcional; troca por configuração no onboarding | — |
| E12 Reversibilidade | 3 | Reversível por remoção, com efeitos colaterais documentados: o gateway mantém estado e sessões; `deploy/` e `docker-compose` criam infraestrutura que exige desmontagem explícita | — |

**AA = 3 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (assistente de usuário único, resposta em múltiplos canais, "o Gateway é só o plano de controle") e o detalhe **confere** literalmente com o README: "The Gateway is just the control plane — the product is the assistant."
**O que o catálogo afirma:** "Assistente de usuário único rodando nos próprios dispositivos. Responde em WhatsApp, Telegram, Slack, Discord, Signal, iMessage, Teams, Matrix e mais 15 canais… O Gateway é só o plano de controle."
**Confere com a fonte:** sim — a contagem "mais 15 canais" é conservadora; o README lista 23

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "**OpenClaw** is a _personal AI assistant_ you run on your own devices." | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não |
| "Peter Steinberger built OpenClaw — 247K GitHub stars — essentially solo with AI agents." | `README.md` de `AC-03-REP-004` (fonte de terceiro sobre este item) | ALEGAÇÃO DO AUTOR (de outro item do acervo) | não — `NÃO VERIFICADA`. O `LICENSE` deste repositório nomeia "OpenClaw Foundation", não uma pessoa; a atribuição de autoria individual **não confere** com o que a fonte declara |
| Logotipos de patrocínio (OpenAI, GitHub, NVIDIA, Vercel, Blacksmith, Convex) | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA`; **P-3**: patrocínio não move nenhum eixo |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V2 · V3 · V4 · V5 · V6 · V7 · V8 | **nenhuma** | `E06 = 3` · `E07 = 4` · `LV = 4` · 0 ND · `E15 = 3` · reconferência estrutural confere |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** §9, por eliminação escrita — **CANDIDATO FORTE** exige `RP ≥ 4` e `RP = 3`; **CANDIDATO A PILOTO** exige "nenhum eixo do Bloco C em 0" e `E10 = 0`; **PADRÃO A ESTUDAR** exige `E03`, `E05` ou `E08` baixos ou ND, e os três estão em 4; **REFERÊNCIA** é para insumo de consulta, não para repositório. Resta EXIGE PESQUISA, com lacuna nomeada.
**Se EXIGE PESQUISA — lacuna nomeada:** a superfície de leitura e instalação não é delimitável a partir do que foi lido — 23.953 arquivos e 289,3 MB, sem manifesto que declare qual subconjunto precisa ser carregado para usar o produto.  **Verificação que a fecharia:** identificar, a partir de `package.json` `files[]` e do pacote npm publicado, qual é a superfície efetivamente distribuída, e medir se ela cai abaixo do limiar de 5.000 arquivos / 100 MB — sem instalar.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-03-REP-007 — `orca-main`

**Tipo:** REPO · **Área:** 03_ORQUESTRACAO-DE-AGENTES
**Hash F0:** `dir · 9477 arq. · aninhado`   **Hash reconferido:** `9477 arq. · aninhamento 1`   **Confere:** sim
**LV:** LV4
**Cobertura da leitura:** raiz efetiva `orca-main/orca-main` (32 entradas); `LICENSE` — MIT, 1.070 bytes, "Copyright (c) 2026 Lovecast Inc.", íntegro; `README.md` (16.620 bytes — lidos os primeiros 6 KB: proposta, mural de funcionalidades com worktrees paralelos, terminais, Design Mode, SSH, anotação de diffs); `package.json` (versão e scripts de lint/teste/verificação); `tests/` — 234 arquivos (`e2e`, `playwright.config.ts`); **busca por `SECURITY.md` e `.env.example` na raiz efetiva — ausentes**. **Não lidos:** `src/`, `native/`, `mobile/`, `docs/`, `skills/`.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** não se aplica

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 4 | Artefato completo e inspecionável (aplicativo Electron com `src/`, `native/`, `mobile/`, `Casks/`) **mais** procedimento de verificação declarado: `"test": … vitest run --config config/vitest.config.ts`, `tests/e2e` com `playwright.config.ts` e portões de lint (`check:reliability-gates`, `check:max-lines-ratchet`, `verify:skill-bundle-manifest`) | — |
| E03 Maturidade | 3 | Versionado com release identificável: `"version": "1.4.148-rc.1"` e diretório `Casks/` de distribuição. **Não alcança 4**: é release candidate, não há `CHANGELOG` na raiz efetiva e o tratamento de erro não foi observado | — |
| E05 Manutenção | ND | — | **Nenhuma evidência datada dentro da fonte**: sem `CHANGELOG`, sem `VERSION` datado, sem comentário com data. Resolveria consultar a origem pública `stablyai/orca` — releases, commits e issues |
| E06 Segurança ⚠ | 2 | Superfície ampla **sem controle documentado na raiz efetiva**: terminais com scrollback persistente, worktrees remotos por SSH com auto-reconexão e port forwarding, navegador Chromium embarcado que captura HTML/CSS/screenshot da página. **Procurado e não encontrado**: `SECURITY.md`, `.env.example`, política de permissão. O único controle observável é o script `verify:macos-entitlements`, que sozinho não documenta a superfície | — |
| E07 Licença ⚠ | 4 | Permissiva padrão presente e íntegra: MIT, 1.070 bytes, titular nomeado (Lovecast Inc.), badge MIT no README. Cópia local não prova titularidade → teto 4 | — |
| E13 Testes/evals | 3 | `tests/` inspecionado: 234 arquivos, com `e2e` e `playwright.config.ts`, e ponto de entrada declarado (`npm test` → vitest). Nenhum eval de comportamento de agente identificado | — |
| E15 Alegações ⚠ | 1 | Alegações numéricas com fonte citada porém não conferíveis com o material disponível: badges de estrelas e de "Total downloads across all releases", mais o slogan "The AI Orchestrator for **100x builders**". **P-3**: nada disso move outro eixo | — |

**NF = 3 · 6/7 · 1 ND** *(mediana dos determinados [1,2,3,3,4,4] = 3)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 4 | Endereça diretamente a pergunta central — execução paralela de agentes sem colisão — **mais** artefato concreto: "Fan one prompt across five agents, each in its own isolated git worktree — compare the results and merge the winner" | — |
| E04 Transferibilidade | 3 | Transferível com adaptação declarada e delimitada: o **padrão** (um worktree por agente) é independente do produto; a implementação é um aplicativo desktop Electron com dependências nativas | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto **dentro do acervo**: é o único item que trata isolamento por worktree como mecanismo central, e não como detalhe | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 4 | Instalação declarada em um passo (página de download, `Casks/` para Homebrew), configuração por `orca.yaml`. Não alcança 5: exige agentes externos (Codex, Claude Code, OpenCode ou Pi) | — |
| E09 Custo | 4 | Custo marginal: aplicativo MIT, sem licença paga declarada; o consumo é o dos agentes já previstos | — |
| E10 Contexto/tokens | **0** | Medido: **9.477 arquivos, 127,3 MB** — acima de 5.000 arquivos e de 100 MB | — |
| E11 Fornecedor | 4 | Abstração de fornecedor documentada: quatro agentes suportados lado a lado (Codex, ClaudeCode, OpenCode, Pi), com troca por configuração | — |
| E12 Reversibilidade | 3 | Reversível por remoção do aplicativo, com efeitos colaterais documentados: cria worktrees git nos repositórios do usuário e mantém scrollback persistente entre reinícios | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (slogan literal, quatro agentes lado a lado, worktree por agente, app desktop para macOS/Windows/Linux, MIT) e o detalhe **confere** com o README e o `LICENSE`.
**O que o catálogo afirma:** "“The AI Orchestrator for 100x builders.” Roda Codex, Claude Code, OpenCode ou Pi **lado a lado, cada um no seu git worktree**, com tudo rastreado num lugar só. App desktop (macOS, Windows, Linux). MIT."
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "The AI Orchestrator for 100x builders." | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| Badges de estrelas no GitHub e "Total downloads across all releases" | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA`; **P-3** |
| "Run agents on a beefy remote box with full file editing, git, and terminals — auto-reconnect and port forwarding included." | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — superfície declarada, não inspecionada; sustenta `E06 = 2` |
| "isolamento por worktree é a resposta ao problema de agentes paralelos pisando nos arquivos uns dos outros" | `_CONTEUDO.md` área 03 | ALEGAÇÃO DO CATÁLOGO | não |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V2 · V3 · V4 · V5 · V6 · V7 · V8 | **nenhuma** | `E06 = 2` (≠ 0 e ≠ ND, logo V2 não dispara) · `E07 = 4` · `LV = 4` · 1 ND · `E15 = 1` (≠ 0) · reconferência confere |

#### Resultado
**RF = PADRÃO A ESTUDAR**
**Regra que produziu:** §9, condição de entrada de PADRÃO A ESTUDAR: o valor está no **padrão**, não no artefato — `E04 = 3 ≥ 3` com `E05 = ND`. As duas classificações de candidato estão fechadas por condição de entrada: ambas exigem `E06 ≥ 3` e aqui `E06 = 2`.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> **PADRÃO A ESTUDAR não significa copiar o código.** O que a ficha registra como estudável é o isolamento por worktree; o artefato permanece com `E06 = 2` e `E05 = ND`.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-03-REP-008 — `ralph-main`

**Tipo:** REPO · **Área:** 03_ORQUESTRACAO-DE-AGENTES
**Hash F0:** `dir · 31 arq. · aninhado`   **Hash reconferido:** `31 arq. · aninhamento 1`   **Confere:** sim
**LV:** LV4
**Cobertura da leitura:** raiz efetiva `ralph-main/ralph-main` (14 entradas, listagem completa); `LICENSE` — MIT, 1.066 bytes, "Copyright (c) 2026 snarktank", íntegro; `README.md` (7.377 bytes — lidos os primeiros 6 KB: pré-requisitos, três opções de instalação, fluxo em sete passos, tabela de arquivos-chave, conceitos críticos); `.claude-plugin/` (`marketplace.json`, `plugin.json`); **busca por diretório de teste na raiz efetiva — ausente**. **Não lidos:** `skills/`, `flowchart/`, conteúdo de `ralph.sh`.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** não se aplica

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 4 | Artefato completo e inspecionável (`ralph.sh`, `prompt.md`, `CLAUDE.md`, `prd.json.example`, `skills/prd`, `skills/ralph`, manifesto de plugin) **mais** procedimento de verificação declarado na fonte: o passo 4 do fluxo é "Run quality checks (typecheck, tests)" e o passo 5 só commita se passarem — passos reproduzíveis, não executados por esta frente | — |
| E03 Maturidade | 2 | Funciona no cenário demonstrado, mas **sem versionamento, sem release e sem tag**: a raiz efetiva não tem `VERSION`, `CHANGELOG` nem `package.json` com versão | — |
| E05 Manutenção | ND | — | Nenhuma evidência datada dentro da fonte. Resolveria consultar a origem pública `snarktank/ralph` |
| E06 Segurança ⚠ | 3 | Superfície declarada (loop autônomo que executa uma ferramenta de código, cria branch e **commita** sem intervenção) **com controles parciais documentados**: número máximo de iterações como parâmetro (padrão 10), contexto limpo a cada iteração, portão de qualidade antes do commit e branch dedicada vinda do PRD | — |
| E07 Licença ⚠ | 4 | Permissiva padrão presente e íntegra: MIT, 1.066 bytes, titular nomeado. Cópia local não prova titularidade → teto 4 | — |
| E13 Testes/evals | 1 | Apenas instruções de "rode e veja": o README documenta como executar o loop, mas **a listagem completa da raiz efetiva não contém diretório de teste, eval ou verificação do próprio Ralph**. Os testes citados no fluxo são os do projeto-alvo, não os do artefato | — |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas; nenhum número decisivo em jogo. As referências externas (padrão de Geoffrey Huntley, artigo do autor) são citadas com link, sem cifras | — |

**NF = 3 · 6/7 · 1 ND** *(mediana dos determinados [1,2,3,3,4,4] = 3)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 4 | Endereça diretamente a pergunta central — quem executa, em que ordem, com que critério de parada — **mais** artefato concreto e reutilizável: `prd.json` como lista de tarefas com campo `passes`, `progress.txt` append-only e o script do loop | — |
| E04 Transferibilidade | 4 | Transferível por configuração, sem alteração de código: copiar três arquivos ou instalar por marketplace; seleção de ferramenta por flag `--tool amp\|claude` | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto **dentro do acervo**: a solução de memória entre iterações **sem manter contexto vivo** (git + `progress.txt` + `prd.json`) não aparece em nenhum outro item | — |

**RP = 4 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 4 | Instalação declarada em um comando pelo marketplace (`/plugin marketplace add snarktank/ralph`), com alternativa por cópia de arquivos; configuração por `prd.json` | — |
| E09 Custo | 3 | Custo variável por uso, **com limite declarado**: o loop consome chamadas de modelo a cada iteração, e o parâmetro `max_iterations` (padrão 10) é o controle | — |
| E10 Contexto/tokens | 3 | Medido: **31 arquivos, 4,9 MB**. Contagem fecharia a âncora 4 (< 50 arquivos), tamanho fecha a âncora 3 (1–5 MB); vale a pior das duas | — |
| E11 Fornecedor | 4 | Abstração de fornecedor documentada: duas ferramentas suportadas (Amp e Claude Code), com troca por flag de linha de comando e template de prompt por ferramenta | — |
| E12 Reversibilidade | 3 | Reversível por remoção dos arquivos, com efeitos colaterais documentados: o loop cria branch, commita e **altera arquivos `AGENTS.md` do projeto** a cada iteração — reversão exige git | — |

**AA = 3 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (loop até o PRD acabar, instância nova com contexto limpo a cada iteração, memória em git + `progress.txt` + `prd.json`, base no padrão Ralph de Geoffrey Huntley) e **todos** os detalhes conferem com o README lido.
**O que o catálogo afirma:** "Roda uma ferramenta de código (Amp ou Claude Code) repetidamente até todos os itens de um PRD estarem completos. **Cada iteração é uma instância nova com contexto limpo** — a memória persiste em histórico do git, `progress.txt` e `prd.json`. Baseado no padrão Ralph de Geoffrey Huntley."
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Each iteration spawns a **new AI instance** (Amp or Claude Code) with clean context." | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — `ralph.sh` não foi lido nem executado |
| "Ralph only works if there are feedbac[k loops]" | `README.md` da fonte (trecho truncado no teto de leitura) | ALEGAÇÃO DO AUTOR | não |
| "Based on [Geoffrey Huntley's Ralph pattern](https://ghuntley.com/ralph/)." | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — atribuição externa não conferida |
| "É barato e resolve degradação de contexto em tarefa longa." | `_CONTEUDO.md` área 03 | ALEGAÇÃO DO CATÁLOGO | não — `NÃO VERIFICADA` |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V2 · V3 · V4 · V5 · V6 · V7 · V8 | **nenhuma** | `E06 = 3` · `E07 = 4` · `LV = 4` · 1 ND · `E15 = 3` · reconferência estrutural confere |

#### Resultado
**RF = CANDIDATO A PILOTO**
**Regra que produziu:** §9. **Não** alcança CANDIDATO FORTE: `E03 = 2` e `E13 = 1` estão abaixo de 3 no Bloco A. Satisfaz CANDIDATO A PILOTO: `LV ≥ 3` · `E06 = 3 ≥ 3` · `E07 = 4 ≥ 3` · `RP = 4 ≥ 3` · **1 ND** ≤ 4 · nenhum eixo do Bloco C em 0.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> **CANDIDATO A PILOTO não significa pilotar.** Restrição registrada: o artefato **não tem testes próprios** (`E13 = 1`) e é um loop que commita sem intervenção humana.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-03-REP-009 — `ruflo-main`

**Tipo:** REPO · **Área:** 03_ORQUESTRACAO-DE-AGENTES
**Hash F0:** `dir · 5116 arq. · aninhado`   **Hash reconferido:** `5116 arq. · aninhamento 1`   **Confere:** sim
**LV:** LV4
**Cobertura da leitura:** raiz efetiva `ruflo-main/ruflo-main` (35 entradas); `LICENSE` — MIT, 1.068 bytes, "Copyright (c) 2024-2026 ruvnet", íntegro; `README.md` (30.004 bytes — lidos os primeiros 6 KB: badges, tese "Agent = Model + Harness", diagrama de arquitetura, dois caminhos de instalação); `package.json` (nome, versão, `files[]`); `Cargo.toml`; `CHANGELOG.md` (cabeçalho, `Unreleased`, `[3.5.0] - 2026-02-27`); `.claude-plugin/`; `tests/` — 31 arquivos listados; `SECURITY.md` presente. **Não lidos:** `v3/`, `ruflo/`, `plugins/`, `docs/`, `crates`.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** não se aplica

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 3 | Artefato completo e inspecionável (CLI, plugins, `v3/`, crates Rust de federação) correspondente à afirmação, **sem** procedimento de verificação **correspondente à afirmação central**: os 31 arquivos de `tests/` cobrem o banco vetorial (`rvf-*.test.ts`) e hooks, não a coordenação de "100+ agentes em enxames" que é a tese do README | — |
| E03 Maturidade | 3 | Versionado com release identificável e changelog presente: `"version": "3.25.6"` em `package.json` e `CHANGELOG.md` com `[3.5.0] - 2026-02-27`. **Não alcança 4** — e registra-se a **inconsistência interna**: o número do pacote (3.25.6) e o do changelog (3.5.0) não se reconciliam a partir do que foi lido | — |
| E05 Manutenção | 3 | Atividade identificável por evidência datada dentro da fonte (`CHANGELOG.md`, `[3.5.0] - 2026-02-27`, mais seção `Unreleased` sem data). Responsável nomeado (ruvnet) e canais declarados (`bugs.url`, `support@ruv.io`, `SECURITY.md`) **fechariam a âncora 4**, mas a única data observável é de cinco meses antes desta avaliação — a evidência não fecha "atividade recente" com folga, e §5.0.4 manda valer a âncora inferior | — |
| E06 Segurança ⚠ | 3 | Superfície declarada (hooks que roteiam tarefas automaticamente, federação entre máquinas, banco vetorial local `agentdb.rvf`, 314 ferramentas MCP alegadas) **com controles parciais documentados**: `SECURITY.md`, `verification/`, `.githooks/`, `.harness/`. **Código não lido** | — |
| E07 Licença ⚠ | 4 | Permissiva padrão presente e íntegra: MIT, 1.068 bytes, titular nomeado. Cópia local não prova titularidade → teto 4 | — |
| E13 Testes/evals | 3 | `tests/` inspecionado: 31 arquivos com ponto de entrada declarado, cobrindo `rvf-backend`, `rvf-embeddings`, `rvf-learning-store`, `rvf-migration`, hooks e regressão em Docker. Nenhum eval de comportamento de agente | — |
| E15 Alegações ⚠ | 2 | Alegações numéricas fortes **com fonte citada e conferível, ainda não conferida**: "ecosystem downloads 8.1M+" e "git clones 14d 106k" apontam para `data/clone-data.proof.json` e `data/clone-data.ledger.json` **dentro do próprio repositório** — conferíveis sem sair da fonte, mas não conferidos sob o teto de leitura. Registra-se ainda a **contradição interna**: o README fala em "100+ specialized agents" e o `package.json` em "60+ specialized agents" | — |

**NF = 3 · 7/7 · 0 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 4 | Endereça diretamente a pergunta central — roteador, enxame, memória e loop de aprendizado — **mais** artefato concreto: `.claude-plugin/`, `v3/`, crates de federação e o diagrama `User → Ruflo → Router → Swarm → Agents → Memory → LLM Providers` | — |
| E04 Transferibilidade | 4 | Transferível por configuração: `npx ruflo init` e plugin de Claude Code/Codex, sem alteração de código do usuário | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto no acervo — federação entre máquinas com banco vetorial próprio —, mas sobrepõe fortemente `AC-03-REP-002` e `AC-03-REP-010` no restante | — |

**RP = 4 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 4 | Instalação declarada em um comando (`npx ruflo init` ou plugin), configuração por arquivo. Não alcança 5: exige harness hospedeiro | — |
| E09 Custo | 3 | Custo variável por uso, com controle possível: MIT e local, mas o roteamento automático por hooks consome modelo em segundo plano, e há serviços hospedados opcionais (`flo.ruv.io`, `goal.ruv.io`) | — |
| E10 Contexto/tokens | **0** | Medido: **5.116 arquivos, 74,5 MB** — acima de 5.000 arquivos | — |
| E11 Fornecedor | 3 | Dois ou mais fornecedores suportados, com troca custosa: plugins para Claude Code e Codex declarados; a arquitetura é acoplada ao ecossistema próprio (RuVector, Cognitum.One) | — |
| E12 Reversibilidade | 2 | Reversível **com perda de estado ou de histórico**: `init` cria `.claude/`, `agentdb.rvf` e `agentdb.rvf.lock`, e o produto é declaradamente uma memória que "aprende de cada tarefa"; remover o diretório descarta esse histórico | — |

**AA = 3 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (ecossistema ruvnet, UI, planejador de metas, banco vetorial próprio RuVector, plugin para Claude Code e Codex; e a advertência de que "o README é quase inteiro badge e número de download") e o detalhe **confere**: o README lido é dominado por badges, e `Cargo.toml` confirma os crates de federação.
**O que o catálogo afirma:** "Ecossistema do ruvnet com UI, planejador de metas e banco vetorial agêntico próprio (RuVector). Plugin para Claude Code e Codex. **Atenção:** o README é quase inteiro badge e número de download. Vá direto para `docs/` e `plugin/`."
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "ecosystem downloads 8.1M+" e "git clones 14d 106k" | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — **conferível dentro da fonte** (`data/clone-data.proof.json`, `data/clone-data.ledger.json`), não conferida sob o teto de leitura; **P-3** |
| "adds 100+ specialized agents, coordinated swarms, self-learning memory, federated comms" | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — **contradita internamente** por `package.json`: "Deploy 60+ specialized agents" |
| "You don't need to learn 314 MCP tools or 26 CLI commands." | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "**Agent = Model + Harness.** … **Ruflo é o harness**" | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não. Converge com o padrão observado em `AC-02-VID-010`, sem que a convergência valide qualquer um dos dois |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V2 · V3 · V4 · V5 · V6 · V7 · V8 | **nenhuma** | `E06 = 3` · `E07 = 4` · `LV = 4` · 0 ND · `E15 = 2` (≠ 0) · reconferência confere |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** §9, por eliminação escrita — CANDIDATO FORTE exige nenhum eixo do Bloco A abaixo de 3 e `E15 = 2`; CANDIDATO A PILOTO exige nenhum eixo do Bloco C em 0 e `E10 = 0`; PADRÃO A ESTUDAR exige `E03`, `E05` ou `E08` baixos ou ND, e estão em 3, 3 e 4. Resta EXIGE PESQUISA, com lacunas nomeadas.
**Se EXIGE PESQUISA — lacuna nomeada:** duas, ambas conferíveis **dentro da própria fonte**: (1) reconciliar "100+ agentes" do README com "60+" do `package.json`, e "3.25.6" do pacote com "3.5.0" do changelog; (2) conferir os números de download contra `data/clone-data.proof.json` e `data/clone-data.ledger.json`.  **Verificação que a fecharia:** ler esses quatro arquivos e recontar os agentes declarados em `v3/` — leitura adicional que estoura o teto de `05` §8 e precisa ser autorizada explicitamente.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-03-REP-010 — `superpowers-main`

**Tipo:** REPO · **Área:** 03_ORQUESTRACAO-DE-AGENTES
**Hash F0:** `dir · 172 arq. · aninhado`   **Hash reconferido:** `172 arq. · aninhamento 1`   **Confere:** sim
**LV:** LV4
**Cobertura da leitura:** raiz efetiva `superpowers-main/superpowers-main` (27 entradas, listagem completa); `LICENSE` — MIT, 1.070 bytes, "Copyright (c) 2025 Jesse Vincent", íntegro; `README.md` (10.737 bytes — lidos os primeiros 6 KB: proposta, funcionamento, instalação para dez harnesses, início do fluxo básico); `package.json` integral; `RELEASE-NOTES.md` (entradas `v6.1.1 (2026-07-02)` e `v6.1.0 (2026-06-30)`); `.claude-plugin/`; `tests/` — 52 arquivos, subdiretórios listados. **Não lidos:** `skills/`, `hooks/`, `docs/`, `scripts/`.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** não se aplica

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 4 | Artefato completo e inspecionável (`skills/`, `hooks/`, extensões por harness, manifestos de plugin) **mais** procedimento de verificação declarado: `tests/` com 52 arquivos organizados **por harness** (`antigravity`, `claude-code`, `codex`, `kimi`, `opencode`, `pi`), mais `shell-lint` e `.pre-commit-config.yaml` | — |
| E03 Maturidade | 4 | Versionado com release identificável (`"version": "6.1.1"`, `RELEASE-NOTES.md` com histórico) **mais** documentação de instalação e uso (dez caminhos de instalação distintos, `docs/README.kimi.md`, `docs/README.opencode.md`) **mais** tratamento de erro visível na configuração: as notas de versão documentam o comportamento de fallback de descoberta de hooks e por que o valor precisa ser exatamente `{}` | — |
| E05 Manutenção | 4 | Atividade recente por evidência datada **dentro da fonte**: `RELEASE-NOTES.md` traz `v6.1.1 (2026-07-02)` e `v6.1.0 (2026-06-30)` — a mais recente a 27 dias desta avaliação **mais** responsável nomeado (Jesse Vincent, no `LICENSE`) **mais** canal declarado (`CODE_OF_CONDUCT.md`, contato comercial `sales@primeradiant.com`, vaga de community engineer). Não alcança 5: oferta de suporte comercial não é política de suporte declarada | — |
| E06 Segurança ⚠ | 3 | Superfície declarada (hook de `SessionStart` que injeta bootstrap, skills que dirigem o comportamento do agente, instalação por marketplace de terceiros e por `Fetch and follow instructions from <URL>` no OpenCode) **com controles parciais documentados**: `.pre-commit-config.yaml`, `shell-lint` nos testes, e as notas de versão descrevendo explicitamente a correção de um hook que se auto-registrava sem intenção | — |
| E07 Licença ⚠ | 4 | Permissiva padrão presente e íntegra: MIT, 1.070 bytes, titular nomeado. Cópia local não prova titularidade → teto 4 | — |
| E13 Testes/evals | 3 | `tests/` inspecionado: 52 arquivos, com suíte por harness e diretórios `brainstorm-server` e `explicit-skill-requests`, que sugerem verificação de acionamento de skill. **Não elevado a 4**: não foi lido nenhum arquivo de teste, então não se afirma que sejam evals de comportamento (P-1) | — |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas ("It's not uncommon for your agent to work autonomously for a couple hours at a time"); nenhum número decisivo em jogo | — |

**NF = 4 · 7/7 · 0 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 4 | Endereça diretamente a pergunta central — **quem decide antes de executar** — **mais** artefato concreto: o fluxo declarado impede a escrita de código antes de spec extraída, apresentada em blocos legíveis e assinada pelo humano, e depois delega a subagentes | — |
| E04 Transferibilidade | 4 | Transferível por configuração, sem alteração de código: instalação independente em dez harnesses, skills em Markdown, extensão declarada em `package.json` (`pi.extensions`, `pi.skills`) | — |
| E14 Diferencial | 4 | Sem equivalente pronto no acervo **mais** custo alto de reconstrução: o portão obrigatório entre especificação e implementação, com TDD vermelho/verde, YAGNI e DRY embutidos e portabilidade para dez harnesses, é curadoria acumulada que nenhum outro item entrega | — |

**RP = 4 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 4 | Instalação declarada em um comando por harness (`/plugin install superpowers@claude-plugins-official`), configuração por manifesto. Não alcança 5: exige harness hospedeiro | — |
| E09 Custo | 4 | Custo marginal: MIT, sem licença paga obrigatória; apenas chamadas de modelo já previstas. Suporte comercial é opcional e declarado como tal | — |
| E10 Contexto/tokens | 3 | Medido: **172 arquivos, 1,3 MB**. Contagem na faixa 50–300 e tamanho na faixa 1–5 MB — as duas fecham a âncora 3 | — |
| E11 Fornecedor | 4 | Abstração de fornecedor documentada: dez harnesses com instalação própria, skills em formato comum, extensão isolada por harness | — |
| E12 Reversibilidade | 3 | Reversível por remoção do plugin, com efeitos colaterais documentados: as notas de versão descrevem registro e desregistro de hook de `SessionStart` por harness | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (skills componíveis, extração de spec antes do código, apresentação em pedaços curtos, plano legível por júnior, TDD vermelho/verde, YAGNI e DRY) e **todos** os detalhes conferem literalmente com o README lido.
**O que o catálogo afirma:** "Skills componíveis mais instruções iniciais que garantem que o agente as use… o agente é proibido de codar antes de o humano assinar o design. Enfatiza TDD vermelho/verde, YAGNI e DRY."
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "It's not uncommon for your agent to work autonomously for a couple hours at a time without deviating from the plan you put together." | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "an implementation plan that's clear enough for an enthusiastic junior engineer with poor taste, no judgement, no project context, and an aversion to testing to follow" | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não |
| "Superpowers is available via the [official Claude plugin marketplace]" | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — oficialidade não verificada na origem |
| "**O que extrair:** o portão entre especificação e implementação" | `_CONTEUDO.md` área 03 | ALEGAÇÃO DO CATÁLOGO | não |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V2 · V3 · V4 · V5 · V6 · V7 · V8 | **nenhuma** | `E06 = 3` · `E07 = 4` · `LV = 4` · 0 ND · `E15 = 3` · reconferência estrutural confere |

#### Resultado
**RF = CANDIDATO FORTE**
**Regra que produziu:** §9, condições de entrada satisfeitas: `LV = 4` · nenhum eixo do Bloco A abaixo de 3 (mínimo 3) · `E06 = 3` · `E07 = 4` · **0 ND** · `RP = 4`.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> **CANDIDATO FORTE não significa adotar.** Restrição registrada: um dos caminhos de instalação documentados manda o agente buscar e seguir instruções de uma URL — superfície de conteúdo hostil que qualquer avaliação oficial precisa tratar (`05` §7.1).

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

> **Nota de série — AC-03-PRT-001 a AC-03-PRT-007.** São sete capturas de um carrossel declarado de oito slides; **o slide 8/8 não está no acervo**. `05` §2.2 obriga ficha individual por ID; o valor de conjunto é registrado como nota adicional em cada ficha, nunca substituindo a avaliação individual. Cobertura, LV e origem Codex são idênticos nas sete: inspeção visual do original pela trilha Codex (`105`, lote 07, `H-P1-001`), sem abertura da imagem por esta frente.

### AC-03-PRT-001 — `Captura de tela 2026-07-28 152354.png`

**Tipo:** PRINT · **Área:** 03_ORQUESTRACAO-DE-AGENTES · **Série:** AI Council 1/8
**Hash F0:** `C46488B2F372FAA5`   **Hash reconferido:** `C46488B2F372FAA5`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`105`); descrição do `_CONTEUDO.md` confrontada com os pixels.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-03-PRT-001 · `H-P1-001` (relatório `105`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só promessa: o slide de abertura afirma "um prompt, vários pensadores, resposta melhor" e declara o sistema "aberto e modular", sem nenhum artefato inspecionável que corresponda (`105`, CONFIRMADA) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e o repositório do "conselho", se existir |
| E05 Manutenção | ND | — | Localizar o canal de publicação com data e cadência |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial ou instrução dirigida ao leitor |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos de uso do carrossel |
| E13 Testes/evals | ND | — | Nenhum artefato testável associado; resolveria localizar a implementação do conselho |
| E15 Alegações ⚠ | 0 | A proposta central do slide **depende** da alegação "Someone built an AI council of genius minds" e do ganho prometido, **sem fonte** e não verificável com o material disponível | — |

**NF = 0 · 2/7 · 5 ND** *(mediana de [0,1] = 0,5 → §14.3 vale o inferior)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça a pergunta de forma genérica: nomeia seis perspectivas e um núcleo deliberativo, sem particularizar quem decide nem como | — |
| E04 Transferibilidade | 1 | Só a ideia viaja; o slide de capa não traz nada implementável | — |
| E14 Diferencial | 1 | Conveniência sobre algo já acessível; o conteúdo útil da série está nos slides 4/8 a 6/8 | — |

**RP = 1 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação; formato de consumo não declarado | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 1,8 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `105` + parágrafo do `_CONTEUDO.md`; < 1 MB | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (os seis papéis nomeados e o núcleo deliberativo) conferido contra os pixels; CONFIRMADA em `105`.
**O que o catálogo afirma:** "**1/8 — “Someone built an AI council of genius minds”**: um núcleo deliberativo conecta seis papéis — Logic, Strategy, First Principles, Philosophy, Systems Thinking e Ethics. A promessa é um prompt, vários pensadores, resposta melhor; sistema aberto e modular."
**Confere com a fonte:** sim — CONFIRMADA em `105`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Someone built an AI council of genius minds" | print (texto observado) | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "Sete capturas de um carrossel de oito slides; o slide 8 não veio na remessa." | `_CONTEUDO.md` área 03 | ALEGAÇÃO DO CATÁLOGO | **conferida** — o acervo contém sete IDs para esta série (lacuna registrada) |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |
| **V7** | **sim** | `E15 = 0` e a proposta depende da alegação → teto EXIGE PESQUISA |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** V7 (§8) — teto EXIGE PESQUISA.
**Se EXIGE PESQUISA — lacuna nomeada:** a identidade do "conselho" — quem o construiu, onde está o artefato, se é público.  **Verificação que a fecharia:** localizar a publicação original do carrossel e o repositório do sistema, se existir; a mesma verificação fecha a lacuna das sete fichas da série, e é contada uma vez.

> **Nota de conjunto (não substitui esta ficha):** a série 1/8–7/8 descreve fan-out, especialização, crítica cruzada, revisão e síntese. `105` registra o ponto ausente: **nenhum slide define o critério de parada do debate**.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-03-PRT-002 — `Captura de tela 2026-07-28 152407.png`

**Tipo:** PRINT · **Área:** 03_ORQUESTRACAO-DE-AGENTES · **Série:** AI Council 2/8
**Hash F0:** `CB5FA1539B4798B3`   **Hash reconferido:** `CB5FA1539B4798B3`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`105`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-03-PRT-002 · `H-P1-001` (relatório `105`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só afirmação: o slide enuncia os limites da resposta única (contexto oculto, raciocínio fraco, ausência de debate) sem exemplo, medição ou artefato (`105`, CONFIRMADA) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial ou instrução ao leitor |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhum artefato testável associado |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas (diagnóstico do problema); nenhum número decisivo em jogo | — |

**NF = 1 · 2/7 · 5 ND** *(mediana de [1,3] = 2 → §14.3 vale o inferior)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça de forma genérica: motiva a deliberação distribuída sem definir papéis nem decisão | — |
| E04 Transferibilidade | 1 | Só a ideia viaja | — |
| E14 Diferencial | 1 | Conveniência; slide de diagnóstico da mesma série | — |

**RP = 1 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 1,2 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `105`; < 1 MB | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (blind spots, weak reasoning, no debate) conferido contra os pixels; CONFIRMADA em `105`.
**O que o catálogo afirma:** "**2/8 — limite da resposta única**: prompt → resposta pode esconder contexto, raciocínio fraco e ausência de debate/correção."
**Confere com a fonte:** sim — CONFIRMADA em `105`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "blind spots, weak reasoning e no debate" | print (texto observado, via `105`) | ALEGAÇÃO DO AUTOR | não |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 3` · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4 do índice.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-03-PRT-003 — `Captura de tela 2026-07-28 152418.png`

**Tipo:** PRINT · **Área:** 03_ORQUESTRACAO-DE-AGENTES · **Série:** AI Council 3/8
**Hash F0:** `142864ED243780E9`   **Hash reconferido:** `142864ED243780E9`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`105`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-03-PRT-003 · `H-P1-001` (relatório `105`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Diagrama isolado e não reprodutível: a mesma pergunta distribuída às seis perspectivas antes da deliberação (`105`, CONFIRMADA) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial ou instrução ao leitor |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhum artefato testável associado |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas; nenhum número decisivo em jogo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: o fan-out é o mecanismo de distribuição de trabalho entre agentes | — |
| E04 Transferibilidade | 2 | O **padrão** (uma pergunta, N perspectivas) é transferível; a implementação não está no print | — |
| E14 Diferencial | 2 | Agregação de material público; converge com AC-03-VID-002 e AC-03-VID-011 no acervo | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 1,1 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `105`; < 1 MB | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (distribuição às seis perspectivas) conferido; CONFIRMADA em `105`.
**O que o catálogo afirma:** "**3/8 — fan-out da pergunta**: a mesma pergunta é distribuída ao conselho, ativando as seis perspectivas antes da deliberação."
**Confere com a fonte:** sim — CONFIRMADA em `105`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| — nenhuma alegação numérica ou de autoridade identificada neste slide | `105` | — | — |

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

### AC-03-PRT-004 — `Captura de tela 2026-07-28 152428.png`

**Tipo:** PRINT · **Área:** 03_ORQUESTRACAO-DE-AGENTES · **Série:** AI Council 4/8
**Hash F0:** `268B1CE65EDB581B`   **Hash reconferido:** `268B1CE65EDB581B`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`105`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-03-PRT-004 · `H-P1-001` (relatório `105`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Arquitetura de papéis exibida em tela, com função declarada para cada um (Logic verifica raciocínio; Strategy antecipa movimentos; First Principles remove suposições; Ethics examina consequências; Systems vê interações; Philosophy questiona o enquadramento). Exemplo isolado, sem implementação (`105`, CONFIRMADA) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial ou instrução ao leitor |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhum artefato testável associado |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas; nenhum número decisivo em jogo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: define **quem faz o quê** com seis funções distintas e não intercambiáveis | — |
| E04 Transferibilidade | 3 | A decomposição por função é transferível com adaptação declarada; independe de fornecedor | — |
| E14 Diferencial | 2 | Agregação de material público; sobrepõe AC-03-VID-002 (Planner/Coder/Tester/Reviewer) na função de nomear papéis | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 1,2 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `105`; < 1 MB | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (as seis funções, uma a uma) conferido contra os pixels; CONFIRMADA em `105`.
**O que o catálogo afirma:** "**4/8 — arquitetura de papéis**: Logic verifica raciocínio; Strategy antecipa movimentos; First Principles remove suposições; Ethics examina consequências; Systems vê interações; Philosophy questiona o enquadramento."
**Confere com a fonte:** sim — CONFIRMADA em `105`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "não são seis personas decorativas. Há especialização, fan-out, crítica cruzada, revisão e síntese." | `_CONTEUDO.md` área 03 | ALEGAÇÃO DO CATÁLOGO | não. **Contraponto registrado por `105`:** "seis personas no mesmo modelo/contexto podem produzir correlação, teatro de debate ou custo sem ganho" |

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

### AC-03-PRT-005 — `Captura de tela 2026-07-28 152439.png`

**Tipo:** PRINT · **Área:** 03_ORQUESTRACAO-DE-AGENTES · **Série:** AI Council 5/8
**Hash F0:** `7292AD51C92754CC`   **Hash reconferido:** `7292AD51C92754CC`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`105`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-03-PRT-005 · `H-P1-001` (relatório `105`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Diagrama isolado do mecanismo de debate: cada papel envia objeções, contrapontos, suposições e trade-offs ao núcleo, que sintetiza, pesa, refina e decide. Sem implementação nem exemplo executado (`105`, CONFIRMADA) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial ou instrução ao leitor |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhum artefato testável associado |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas; nenhum número decisivo em jogo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: define o protocolo de troca entre agentes e o ponto onde a decisão é tomada | — |
| E04 Transferibilidade | 3 | O protocolo (objeção → contraponto → suposição → trade-off → síntese) transfere com adaptação declarada | — |
| E14 Diferencial | 2 | Agregação de material público; converge com AC-03-VID-006 e AC-09-VID-005 | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 1,3 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `105`; < 1 MB | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (objeções, contrapontos, suposições, trade-offs, síntese no núcleo) conferido; CONFIRMADA em `105`.
**O que o catálogo afirma:** "**5/8 — debate**: cada papel envia objeções, contrapontos, suposições e trade-offs ao núcleo, que sintetiza, pesa, refina e decide."
**Confere com a fonte:** sim — CONFIRMADA em `105`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| — nenhuma alegação numérica ou de autoridade identificada neste slide | `105` | — | — |

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

### AC-03-PRT-006 — `Captura de tela 2026-07-28 152608.png`

**Tipo:** PRINT · **Área:** 03_ORQUESTRACAO-DE-AGENTES · **Série:** AI Council 6/8
**Hash F0:** `DB54B7F918730F27`   **Hash reconferido:** `DB54B7F918730F27`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`105`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-03-PRT-006 · `H-P1-001` (relatório `105`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Sequência de rodadas exibida em tela: respostas iniciais → rodada de desafio → revisão → síntese final. Exemplo isolado, sem execução (`105`, CONFIRMADA) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial ou instrução ao leitor |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | **A rodada de desafio pressupõe critério de aprovação, ausente do print**; resolveria obter a fonte primária com a rubrica de convergência |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas; nenhum número decisivo em jogo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: estrutura o trabalho em rodadas com papéis distintos por rodada | — |
| E04 Transferibilidade | 3 | A estrutura de rodadas transfere com adaptação declarada | — |
| E14 Diferencial | 2 | Agregação de material público; o mesmo padrão de rodadas limitadas aparece em AC-03-VID-006 e AC-09-VID-005, ali **com** limite explícito de cinco rodadas | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 879,7 KB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `105`; < 1 MB | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (as quatro rodadas, na ordem) conferido; CONFIRMADA em `105`.
**O que o catálogo afirma:** "**6/8 — rodadas estruturadas**: respostas iniciais → rodada de desafio → revisão → síntese final."
**Confere com a fonte:** sim — CONFIRMADA em `105`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "O ponto ausente é o critério de parada: o carrossel não define como o sistema sabe que o debate convergiu." | `_CONTEUDO.md` área 03 | ALEGAÇÃO DO CATÁLOGO | **conferida** — nenhum dos sete slides exibe critério de parada (`105`) |

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

### AC-03-PRT-007 — `Captura de tela 2026-07-28 152621.png`

**Tipo:** PRINT · **Área:** 03_ORQUESTRACAO-DE-AGENTES · **Série:** AI Council 7/8
**Hash F0:** `8D7450D9384F9B3D`   **Hash reconferido:** `8D7450D9384F9B3D`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`105`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-03-PRT-007 · `H-P1-001` (relatório `105`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só promessa: o slide de fechamento enuncia quatro ganhos (fewer blind spots, clearer reasoning, stronger decisions, better synthesis) sem medição, comparação ou artefato (`105`, CONFIRMADA "como promessas do slide") | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial ou instrução ao leitor |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | **Os quatro ganhos são exatamente o que um eval mediria, e não há nenhum**; resolveria obter da fonte primária qualquer comparação com resposta única |
| E15 Alegações ⚠ | 0 | A proposta do slide **depende** de quatro alegações de ganho **sem fonte** e não verificáveis com o material disponível | — |

**NF = 0 · 2/7 · 5 ND** *(mediana de [0,1] = 0,5 → §14.3 vale o inferior)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça de forma genérica: enuncia o resultado esperado da deliberação sem definir mecanismo | — |
| E04 Transferibilidade | 1 | Só a ideia viaja | — |
| E14 Diferencial | 1 | Conveniência; slide de fechamento da mesma série | — |

**RP = 1 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 966,9 KB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `105`; < 1 MB | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (os quatro ganhos enunciados) conferido; CONFIRMADA em `105`, com a ressalva explícita de que conferem "como promessas do slide".
**O que o catálogo afirma:** "**7/8 — veredito**: o sistema funde os melhores argumentos em uma resposta, buscando menos pontos cegos, raciocínio mais claro, decisões mais fortes e síntese melhor."
**Confere com a fonte:** sim — CONFIRMADA em `105`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Fewer blind spots, clearer reasoning, stronger decisions e better synthesis" | print (texto observado, via `105`) | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |
| **V7** | **sim** | `E15 = 0` e a proposta depende das quatro alegações → teto EXIGE PESQUISA |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** V7 (§8) — teto EXIGE PESQUISA.
**Se EXIGE PESQUISA — lacuna nomeada:** os quatro ganhos prometidos não têm medição, comparação nem fonte.  **Verificação que a fecharia:** experimento próprio comparando resposta única e deliberação por papéis sobre um mesmo conjunto de perguntas, com rubrica definida por esta casa — não a repetição da promessa do slide.

> **Lacuna de série registrada:** o slide **8/8 não existe no acervo**. Nenhum dos sete presentes define critério de parada do debate.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-03-PRT-008 — `Captura de tela 2026-07-28 165210.png`

**Tipo:** PRINT · **Área:** 03_ORQUESTRACAO-DE-AGENTES
**Hash F0:** `7D5EAF262CA86CD5`   **Hash reconferido:** `7D5EAF262CA86CD5`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`105`), com conferência item a item dos componentes do diagrama.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-03-PRT-008 · `H-P1-001` (relatório `105`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Captura do README de um repositório: exemplo isolado e não reprodutível — a tese e o diagrama aparecem, o repositório não. Componentes visíveis confirmados por `105`: scheduling, worktrees, subagentes, skills e memória/estado persistente | — |
| E03 Maturidade | ND | — | Identificar o repositório "Loop Engineering" e inspecionar versão, release e estabilidade |
| E05 Manutenção | ND | — | Localizar o repositório de origem e verificar atividade datada |
| E06 Segurança ⚠ | ND | — | Inspecionar o repositório: o diagrama declara scheduling, worktrees e estado persistente — superfície ampla, retratada e não inspecionada |
| E07 Licença ⚠ | ND | — | Identificar o repositório e ler o texto da licença |
| E13 Testes/evals | ND | — | A tese cita "verificação" como componente do loop, mas nenhum teste é exibido; resolveria inspecionar o repositório |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas (substituir a pessoa como "quem dá prompts" por um sistema que conduz o agente); nenhum número decisivo em jogo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: desloca o controle do prompt para o desenho do loop — ritmo, isolamento, memória, verificação e handoff | — |
| E04 Transferibilidade | 2 | O **padrão** é transferível; a implementação está num repositório não identificado | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto no acervo **como formulação**: nomeia o loop, e não o prompt, como unidade de projeto. Converge com AC-03-REP-008 (Ralph), que o implementa | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 813,4 KB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `105` + parágrafo do `_CONTEUDO.md`; < 1 MB | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 2** — **PARCIAL** em `105`: tese, definição de loop, subagentes, verificação e estado externo conferem, mas o catálogo inclui **"navegador"** entre os componentes do diagrama e `105` registra que **não há componente de navegador visível**. Correção material 4 de `105`. Detalhe verificável parcialmente não conferido → teto 2 (§14.4).
**O que o catálogo afirma:** "O diagrama mostra scheduling, worktrees, subagentes, skills, navegador e memória/estado persistente."
**Confere com a fonte:** parcialmente — remover "navegador" do inventário visual

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "substituir a pessoa como “quem dá prompts” por um sistema que conduz o agente" | `_CONTEUDO.md` área 03 / print | ALEGAÇÃO DO AUTOR | não |
| "navegador" como componente do diagrama | `_CONTEUDO.md` área 03 | ALEGAÇÃO DO CATÁLOGO | **contradita pela inspeção visual** → sustenta `NC = 2` |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 3` · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** §9 — relevância aparente (`E01 = 3`) com lacuna nomeada e endereçável; teto de V2/V4 respeitado.
**Se EXIGE PESQUISA — lacuna nomeada:** identidade do repositório "Loop Engineering" — origem, licença, conteúdo e se implementa o diagrama exibido.  **Verificação que a fecharia:** localizar o repositório público pelo título do README capturado e ler licença e estrutura — sem clonar nem executar.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

> **Cobertura padrão dos VÍDEO desta área:** ficha visual de 9 quadros distribuídos entre 4% e 92% da duração, em `95` sob `H-M2-002`; ficha STT individual em `TRANSCRICOES-BRUTAS-STT/03_ORQUESTRACAO-DE-AGENTES/`, sob `H-M3-001` e manifesto `117`. **LV3-V + LV3-A não produz LV4.** Nenhum binário foi aberto por esta frente. Fala automática é **provável, nunca citação exata**.

### AC-03-VID-001 — `ECC.mp4`

**Tipo:** VÍDEO · **Área:** 03_ORQUESTRACAO-DE-AGENTES
**Hash F0:** `6434AF4CA455407B`   **Hash reconferido:** `6434AF4CA455407B`   **Confere:** sim
**LV:** LV3-V + LV3-A
**Cobertura da leitura:** 9 quadros (`95`); transcrição automática bruta integral (44,0 s, `pt`, 13 segmentos, p = 0,851, **ALTA AUTOMÁTICA**). Sem revisão humana.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-03-VID-001 · `H-M2-002` (`95`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só divulgação: a fala provável enumera capacidades ("são 181 skills prontas, 47 sub-agentes, 78 comandos prontos") sem exibir nenhum artefato inspecionável no vídeo. **O artefato existe, mas fora do vídeo** — é `AC-03-REP-002`, avaliado nesta mesma área | — |
| E03 Maturidade | ND | — | Não é o vídeo que amadurece; resolver exigiria avaliar o repositório — já feito em `AC-03-REP-002` (`E03 = 4`) |
| E05 Manutenção | ND | — | Localizar o canal de publicação do vídeo com data |
| E06 Segurança ⚠ | ND | — | O vídeo não expõe superfície própria; a do artefato citado está avaliada em `AC-03-REP-002` (`E06 = 3`) |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos do vídeo. A licença do artefato citado está em `AC-03-REP-002` (MIT) |
| E13 Testes/evals | ND | — | Nenhum teste exibido no vídeo |
| E15 Alegações ⚠ | 2 | Alegações numéricas fortes **com fonte citada e conferível, ainda não conferida**: "181 skills, 47 sub-agentes, 78 comandos" e "50 mil estrelas" são conferíveis **dentro do próprio acervo**, contra `AC-03-REP-002`. **Divergência já observável**: o vídeo diz "50 mil estrelas"; o `README.md` do repositório no acervo diz "**211.9K+ stars**" | — |

**NF = 1 · 2/7 · 5 ND** *(mediana de [1,2] = 1,5 → §14.3 vale o inferior)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça a pergunta de forma genérica: anuncia um conjunto de agentes e comandos sem explicar como coordenam trabalho | — |
| E04 Transferibilidade | 1 | Só a ideia viaja; o que é transferível está no repositório, não no vídeo | — |
| E14 Diferencial | 1 | Conveniência: é divulgação de um item que **já está no acervo** com ficha própria (`AC-03-REP-002`) | — |

**RP = 1 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 41 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 1** — o item está na tabela "Vídeo (NÃO é legível por IA)" com a coluna "Assunto": descrição derivada do nome do arquivo (`ECC.mp4` → "demonstração do ECC"), sem indício de inspeção. Compatível com o conteúdo, mas compatibilidade não eleva a nota.
**O que o catálogo afirma:** "`ECC.mp4` | 43 MB | demonstração do ECC"
**Confere com a fonte:** sim, em nível genérico — o conteúdo observado é **divulgação**, não demonstração de uso

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "são 181 skills prontas, 47 sub-agentes, 78 comandos prontos" | LV3-A bruto, 00:00:09,380–00:00:14,880 — **fala provável, não citação exata** | ALEGAÇÃO DO AUTOR | não — **conferível contra `AC-03-REP-002`** |
| "ganhou o último hackathon da antropa que liberou o setup inteiro dele do cloud code de graça" | LV3-A bruto, 00:00:00–00:00:04,700 — fala provável | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "o cara refinou a estrutura por 10 meses de trabalho real" | LV3-A bruto, 00:00:24,800–00:00:27,900 — fala provável | ALEGAÇÃO DO AUTOR | não — converge com "10+ months" do README de `AC-03-REP-002`; **convergência entre duas peças do mesmo autor não é verificação** |
| "ele usou esse setup para criar uma startup inteira em 8 horas" | LV3-A bruto, 00:00:27,900–00:00:31,280 — fala provável | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "50 mil estrelas" | `95` (texto visual observado) | ALEGAÇÃO DO AUTOR | não — **divergente** do README do próprio repositório no acervo ("211.9K+ stars"); **P-3**: nenhum dos dois números move eixo |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 2` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** §9 — relevância aparente com lacuna nomeada e endereçável; teto de V2/V4 respeitado.
**Se EXIGE PESQUISA — lacuna nomeada:** as três contagens divulgadas (181 skills, 47 subagentes, 78 comandos) e a contagem de estrelas, que **divergem** entre o vídeo e o README do repositório correspondente.  **Verificação que a fecharia:** contar `skills/`, `agents/` e `commands/` em `AC-03-REP-002` — leitura adicional que estoura o teto de `05` §8 e precisa ser autorizada; a contagem de estrelas exige a origem pública e, por P-3, não move eixo algum.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-03-VID-002 — `Gravando 2026-07-28 153202.mp4`

**Tipo:** VÍDEO · **Área:** 03_ORQUESTRACAO-DE-AGENTES
**Hash F0:** `397112332ABD593D`   **Hash reconferido:** `397112332ABD593D`   **Confere:** sim
**LV:** LV3-V *(LV3-A = `SEM FALA LEXICAL CONFIÁVEL`, 2 palavras, p = 0,565)*
**Cobertura da leitura:** 9 quadros (`95`); ficha STT (38,0 s).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-03-VID-002 · `H-M2-002` (`95`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Especificação de papéis exibida em tela, com contrato por papel: Planner lê o código, fecha a spec e marca dúvidas; Coder implementa estritamente o escopo; Tester cobre caminho feliz, bordas e falha **e interrompe sem reparar**; Reviewer é somente leitura e emite SHIP/NEEDS WORK/BLOCK. Exemplo isolado, sem implementação (`95`) | — |
| E03 Maturidade | ND | — | Localizar a implementação real desses papéis e inspecionar seu estágio |
| E05 Manutenção | ND | — | Localizar a publicação de origem com data |
| E06 Segurança ⚠ | ND | — | Nenhuma superfície inspecionada; "Reviewer somente leitura" é contrato retratado, não controle verificado |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | O papel Tester é descrito, mas nenhum teste é exibido; resolveria inspecionar a implementação |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas (atribuição de função a papel); nenhum número decisivo em jogo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central — quem decide, quem executa, quem revisa — com quatro papéis e um veredito nomeado | — |
| E04 Transferibilidade | 3 | A decomposição por papel, com contrato de saída (SHIP/NEEDS WORK/BLOCK), transfere com adaptação declarada | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto no acervo **na forma**: é o item que separa **independência da revisão** (somente leitura) de execução, com veredito discreto. `AC-03-REP-004` implementa papéis, mas não publica esse contrato de três estados | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 21,5 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 2** — **PARCIAL.** O método é declarado ("Título pelo conteúdo visível") e o núcleo confere, mas há **duas imprecisões materiais** contra o observado em `95`: o catálogo nomeia o segundo papel como **"Builder"** e o observado é **"Coder"**; e acrescenta um **"Orchestrator"** que não aparece na descrição visual. Normalização não conferida → teto 2 (§14.4).
**O que o catálogo afirma:** "`Gravando 2026-07-28 153202.mp4` | 21,5 MB | pipeline Planner → Builder → Tester → Reviewer com Orchestrator | não transcrito"
**Confere com a fonte:** parcialmente

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Reviewer é somente leitura e emite SHIP/NEEDS WORK/BLOCK" | `95` (texto visual observado) | ALEGAÇÃO DO AUTOR | não |
| "Tester cobre caminho feliz, bordas e falha e interrompe sem reparar" | `95` (texto visual observado) | ALEGAÇÃO DO AUTOR | não |
| "**Achado central:** separação de funções e independência da revisão." | `95` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | não |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 3` · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4 (o valor é o contrato de papéis em si).
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-03-VID-003 — `Gravando 2026-07-28 154123.mp4`

**Tipo:** VÍDEO · **Área:** 03_ORQUESTRACAO-DE-AGENTES
**Hash F0:** `E09098CF9DF15DAC`   **Hash reconferido:** `E09098CF9DF15DAC`   **Confere:** sim
**LV:** LV3-V + LV3-A
**Cobertura da leitura:** 9 quadros (`95`); transcrição automática bruta integral (31,7 s, `pt`, 12 segmentos, p = 0,810, **MÉDIA AUTOMÁTICA**). Sem revisão humana.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-03-VID-003 · `H-M2-002` (`95`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 0 | A afirmação central — de que fornecedores estariam "liberando" capacidades por disputa de mercado e que "um comando e você instala tudo" — **não tem nenhuma sustentação na fonte**: nenhum artefato, exemplo ou referência acompanha (`95`: "Risco alto: marketing, instalação em massa, permissões e cadeia de suprimentos. Não usar como instrução") | — |
| E03 Maturidade | ND | — | Identificar quais são as ferramentas e plugins citados e inspecionar seu estágio |
| E05 Manutenção | ND | — | Localizar o canal de publicação com data |
| E06 Segurança ⚠ | ND | — | **Superfície declarada e não inspecionada**: instalação em massa de plugins com escopos de render, deploy e cobrança. Resolveria identificar cada plugin e inspecionar permissões |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhum artefato testável associado |
| E15 Alegações ⚠ | 0 | A proposta central **depende** de alegações numéricas fortes **sem fonte**: "Google liberou um milhão do Tolkien de graça", "Antrop abriu o cofre, **37 ferramentas** que eles usaram pra construir o próprio cloud" (LV3-A, 00:00:05–00:00:15). Não verificáveis com o material disponível | — |

**NF = 0 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 1 | Tangencia a área — cita ferramentas de agente —, mas o núcleo é aquisição promocional, não coordenação de trabalho entre agentes | — |
| E04 Transferibilidade | 1 | Só a ideia viaja; nada implementável acompanha | — |
| E14 Diferencial | 0 | Reprodutível em horas com ferramenta já disponível: é uma lista de anúncios de terceiros | — |

**RP = 1 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 75,3 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 2** — **PARCIAL.** O método é declarado, mas a descrição só confere pela metade: "comparação com Anthropic" corresponde ao observado; "**agente com acesso a website, API, apps e dados**" **não** corresponde — `95` e a fala provável descrevem divulgação de plugins e "tokens grátis", não um agente com esses acessos. Normalização material não conferida → teto 2.
**O que o catálogo afirma:** "`Gravando 2026-07-28 154123.mp4` | 50,3 MB | agente com acesso a website, API, apps e dados; comparação com Anthropic | não transcrito"
**Confere com a fonte:** parcialmente

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Google liberou um milhão do Tolkien de graça" | LV3-A bruto, 00:00:03–00:00:05 — **fala provável, não citação exata** (o motor grafou "Tolkien" por "token") | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "Antrop abriu o cofre, 37 ferramentas que eles usaram pra construir o próprio cloud" | LV3-A bruto, 00:00:08–00:00:12 — fala provável | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "agora são suas, de graça, um comando e você instala tudo" | LV3-A bruto, 00:00:12–00:00:15 — fala provável | ALEGAÇÃO DO AUTOR | não — **instrução de instalação em massa; registrada como achado de risco, não obedecida** (`05` §7.1) |
| "Essa guerra não vai durar por acerto. Pega tudo o que puder." | LV3-A bruto, 00:00:29–00:00:31 — fala provável | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V8 | não | `E06 ≠ 0` (não inspecionado) · `E07 ≠ 0` · `LV = 3` · 5 ND · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |
| **V7** | **sim** | `E15 = 0` e a proposta depende das alegações → teto EXIGE PESQUISA |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** V7 (§8) — teto EXIGE PESQUISA. **Não é REJEITADO**: `E01 = 1` (≠ 0) e nenhum risco foi **confirmado** por inspeção — §9 é explícito em que a rejeição se dá por evidência, nunca por ND.
**Se EXIGE PESQUISA — lacuna nomeada:** identidade e escopo de permissão das ferramentas e plugins que o vídeo manda instalar em massa, e a procedência das duas alegações numéricas.  **Verificação que a fecharia:** identificar cada plugin citado, ler seu manifesto de permissões e sua licença na origem pública — **sem instalar**; e localizar os anúncios primários dos dois fornecedores citados.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-03-VID-004 — `Gravando 2026-07-28 161341.mp4`

**Tipo:** VÍDEO · **Área:** 03_ORQUESTRACAO-DE-AGENTES
**Hash F0:** `A08BCBF5DFEF093E`   **Hash reconferido:** `A08BCBF5DFEF093E`   **Confere:** sim
**LV:** LV3-V + LV3-A
**Cobertura da leitura:** 9 quadros (`95`); transcrição automática bruta integral (79,4 s, `en`, 12 segmentos, p = 0,897, **ALTA AUTOMÁTICA**). Sem revisão humana.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-03-VID-004 · `H-M2-002` (`95`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Demonstração isolada e não reprodutível: comando de voz aciona o agente, que consulta receita de aplicativo, anúncios, email e atendimento. Números aparecem em tela ("2,459 new downloads", "$4,289 revenue"), mas nenhum insumo, configuração ou procedimento acompanha | — |
| E03 Maturidade | ND | — | Identificar os conectores demonstrados (RevenueCat MCP, Buffer MCP, Gmail MCP, Meta Ads MCP) e inspecionar o estágio de cada um |
| E05 Manutenção | ND | — | Localizar o canal de publicação com data |
| E06 Segurança ⚠ | ND | — | **Superfície declarada, ampla e não inspecionada**: acesso a navegador, receita, anúncios pagos, email e atendimento ao cliente, acionado por voz. Resolveria inspecionar cada conector: escopo, autorização, confirmação e auditoria |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos do vídeo e dos conectores |
| E13 Testes/evals | ND | — | Nenhum teste exibido |
| E15 Alegações ⚠ | 0 | A demonstração **depende** de números exibidos sem fonte — "2,459 new downloads and generated $4,289 revenue" (LV3-A, 00:00:23–00:00:31) e "Claude will handle **90%** of customer service" (00:00:51–00:00:55) —, não verificáveis com o material disponível | — |

**NF = 1 · 2/7 · 5 ND** *(mediana de [0,2] = 1)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central em um ponto específico: **handoff** — "Define custom sub agents and equip them with proper skills and connectors then your main agent can hand off work to the proper sub agent" | — |
| E04 Transferibilidade | 2 | O **padrão** (agente principal delegando a subagentes equipados por conector) transfere; a implementação depende de contas, credenciais e produtos do autor | — |
| E14 Diferencial | 2 | Agregação de capacidades públicas; a rotina diária consolidada converge com AC-03-VID-011 e AC-06-VID-017 | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 75,3 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado ("Título pelo conteúdo visível") **e confirmado** pelos quadros e pela fala provável: ElevenLabs e o handoff de trabalho aparecem literalmente na transcrição (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 161341.mp4` | 75,3 MB | sistema multiagente com ElevenLabs e handoff de trabalho | não transcrito"
**Confere com a fonte:** sim — LV3-A 00:00:15–00:00:20 ("Connect 11 labs…") e 00:00:59–00:01:05 (handoff)

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "We have 2,459 new downloads and generated $4,289 revenue" | LV3-A bruto, 00:00:23,820–00:00:31,620 — **fala provável, não citação exata** | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "Organize all of your FAQs and markdown and Claude will handle 90% of customer service" | LV3-A bruto, 00:00:51,540–00:00:55,640 — fala provável | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "Meta launched an official ads MCP so you can run more campaigns and give them more of your money" | LV3-A bruto, 00:00:40,660–00:00:45,000 — fala provável | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "**Risco crítico:** acesso amplo a produção, clientes, receita e email exige identidade, autorização granular, confirmação e auditoria." | `95` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | não |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |
| **V7** | **sim** | `E15 = 0` e a demonstração depende dos números → teto EXIGE PESQUISA |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** V7 (§8) — teto EXIGE PESQUISA.
**Se EXIGE PESQUISA — lacuna nomeada:** escopo de autorização de cada conector demonstrado (receita, anúncios pagos, email, atendimento) e a procedência dos números exibidos.  **Verificação que a fecharia:** ler a documentação de permissões de cada MCP citado na origem primária, registrando quais operações são de leitura e quais produzem efeito externo — sem conectar conta alguma.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-03-VID-005 — `Gravando 2026-07-28 162357.mp4`

**Tipo:** VÍDEO · **Área:** 03_ORQUESTRACAO-DE-AGENTES
**Hash F0:** `E1198B32D4660DBA`   **Hash reconferido:** `E1198B32D4660DBA`   **Confere:** sim
**LV:** LV3-V + LV3-A
**Cobertura da leitura:** 9 quadros (`95`); transcrição automática bruta integral (35,8 s, `pt`, 10 segmentos, p = 0,891, **ALTA AUTOMÁTICA**). Sem revisão humana.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-03-VID-005 · `H-M2-002` (`95`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Demonstração isolada: os quadros mostram um `routes.yaml` que encaminha planner/executor/reviewer/tools e um `diff.patch` como entrega revisável; a fala provável descreve o mesmo fluxo. Nenhum arquivo acompanha o vídeo | — |
| E03 Maturidade | ND | — | Identificar o "plugin de rotas" citado e inspecionar seu estágio |
| E05 Manutenção | ND | — | Localizar o canal de publicação com data |
| E06 Segurança ⚠ | ND | — | **Superfície declarada**: um agente lê e audita `src` e devolve patch; o outro revisa. Resolveria inspecionar o plugin de rotas — escopo de leitura, escrita e execução |
| E07 Licença ⚠ | ND | — | Identificar o plugin e ler o texto da licença |
| E13 Testes/evals | ND | — | Nenhum teste exibido |
| E15 Alegações ⚠ | 0 | A proposta central **depende** de uma alegação numérica forte sem fonte: "Com isso você economiza **80%** do limite das duas" (LV3-A, 00:00:25,960–00:00:29,240). Não verificável com o material disponível | — |

**NF = 1 · 2/7 · 5 ND** *(mediana de [0,2] = 1)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: define quem planeja, quem executa e quem revisa, com o artefato intermediário (`diff.patch`) como unidade de handoff | — |
| E04 Transferibilidade | 3 | O padrão (arquivo de rotas declarando papéis, worker entregando artefato revisável) transfere com adaptação declarada | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto no acervo **na forma**: o `routes.yaml` como declaração explícita de quem é chefe e quem é operário não aparece em nenhum outro item | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 33,9 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado **e confirmado** pelos quadros e pela fala provável, inclusive a ressalva de que a economia é **declarada** e não medida (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 162357.mp4` | 33,9 MB | Claude como “chefe” e Codex como “operário”, com economia declarada de tokens | não transcrito"
**Confere com a fonte:** sim — LV3-A 00:00:04,480–00:00:09,440 ("O Cloud vira o chefe, o Codex vira o operário, um planeja e outro executa")

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Com isso você economiza 80% do limite das duas." | LV3-A bruto, 00:00:25,960–00:00:29,240 — **fala provável, não citação exata** | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "No final das contas, usar um só modelo é perder tempo e dinheiro." | LV3-A bruto, 00:00:31,360–00:00:35,000 — fala provável | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "É só instalar o plugin de rotas no terminal." | LV3-A bruto, 00:00:29,240–00:00:31,360 — fala provável | ALEGAÇÃO DO AUTOR | não — plugin não identificado |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |
| **V7** | **sim** | `E15 = 0` e a proposta depende dos 80% → teto EXIGE PESQUISA |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** V7 (§8) — teto EXIGE PESQUISA.
**Se EXIGE PESQUISA — lacuna nomeada:** identidade e licença do "plugin de rotas", e a procedência do ganho de 80%.  **Verificação que a fecharia:** identificar o plugin na origem pública e ler licença e escopo; medir localmente o consumo com e sem separação planejador/executor, com tarefas definidas por esta casa. Note-se que `AC-03-REP-001` já entrega o mesmo acoplamento como artefato oficial, com licença Apache-2.0 lida.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-03-VID-006 — `Gravando 2026-07-28 163546.mp4`

**Tipo:** VÍDEO · **Área:** 03_ORQUESTRACAO-DE-AGENTES
**Hash F0:** `9317AB60D45D7EAF`   **Hash reconferido:** `9317AB60D45D7EAF`   **Confere:** sim
**LV:** LV3-V *(LV3-A = `SEM FALA LEXICAL CONFIÁVEL`, 1 palavra, p = 0,751)*
**Cobertura da leitura:** 9 quadros (`95`); ficha STT (21,7 s).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-03-VID-006 · `H-M2-002` (`95`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Protocolo exibido em tela com parâmetros concretos: sandbox somente leitura, correção em uma linha, **máximo de cinco rodadas** e inversão de papéis para implementação e revisão. Exemplo isolado, sem implementação inspecionável (`95`) | — |
| E03 Maturidade | ND | — | Identificar a implementação do protocolo e inspecionar seu estágio |
| E05 Manutenção | ND | — | Localizar o canal de publicação com data |
| E06 Segurança ⚠ | ND | — | "Sandbox somente leitura" é controle **retratado**, não inspecionado; resolveria inspecionar a implementação |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhum teste exibido; o veredito é o critério de aprovação, sem rubrica visível |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas; o número presente (cinco rodadas) é **parâmetro do protocolo**, não alegação de resultado | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: define ordem (sabatina → revisão → veredito → construção), quem tem permissão de escrita em cada etapa e o limite de iterações | — |
| E04 Transferibilidade | 3 | O protocolo transfere com adaptação declarada; independe de fornecedor | — |
| E14 Diferencial | 2 | Agregação: é a versão em português do mesmo padrão de `AC-09-VID-005`, que **nomeia o repositório** `chaseai-yt/grill-me-codex`. Repetição aumenta exposição, não independência da evidência | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 11,1 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado **e confirmado** pelos quadros: sabatina, revisão e inversão de papéis correspondem ao observado (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 163546.mp4` | 11,1 MB | Fable planeja, Sol executa; sabatina, revisão e inversão de papéis | não transcrito"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "sandbox somente leitura, uma linha de correção, máximo de cinco rodadas, depois inversão de papéis" | `95` (texto visual observado) | ALEGAÇÃO DO AUTOR | não |
| "Converge com AC-09-VID-005." | `95` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | **conferida** entre as duas fichas visuais — convergência registrada, sem valer como validação |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 3` · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4. O artefato nomeado aparece em `AC-09-VID-005`, e é lá que a lacuna endereçável está registrada — **não é contada duas vezes**.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-03-VID-007 — `Gravando 2026-07-28 164919.mp4`

**Tipo:** VÍDEO · **Área:** 03_ORQUESTRACAO-DE-AGENTES · **Original de uma duplicata exata** (ver `AC-03-VID-008`)
**Hash F0:** `192C3748B93DDE8B`   **Hash reconferido:** `192C3748B93DDE8B`   **Confere:** sim
**LV:** LV3-V *(LV3-A = `SEM FALA LEXICAL CONFIÁVEL`, 1 palavra, p = 0,322)*
**Cobertura da leitura:** 9 quadros (`95`); ficha STT (10,8 s).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-03-VID-007 · `H-M2-002` (`95`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Decomposição exibida em tela de uma linha de produção analítica em seis papéis fixos — Cleaner, DAX, Layout, Insights, Data Auditor e Executive Delivery —, cada um com função declarada. Exemplo isolado, sem implementação (`95`) | — |
| E03 Maturidade | ND | — | Identificar a implementação dos seis agentes e inspecionar seu estágio |
| E05 Manutenção | ND | — | Localizar o canal de publicação com data |
| E06 Segurança ⚠ | ND | — | Nenhuma superfície inspecionada; o papel "Data Auditor" é retratado, não verificado |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhum teste exibido |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas (atribuição de função a papel); nenhum número decisivo em jogo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central em um domínio concreto: limpeza, cálculo, visual, insight, **revisão** e entrega, com um papel dedicado à auditoria do resultado | — |
| E04 Transferibilidade | 3 | A decomposição por etapa transfere com adaptação declarada; a implementação depende da ferramenta analítica do autor | — |
| E14 Diferencial | 2 | Agregação: repete o padrão de papéis já visto em AC-03-VID-002 e AC-03-PRT-004, particularizado para uma linha de dados | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 6,7 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado **e confirmado** pelos quadros (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 164919.mp4` | 6,7 MB | equipe de agentes especializados para dashboard e análise | não transcrito"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Cleaner, DAX, Layout, Insights, Data Auditor e Executive Delivery" | `95` (texto visual observado) | ALEGAÇÃO DO AUTOR | não |

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

### AC-03-VID-008 — `Gravando 2026-07-28 165017.mp4`  ·  FICHA DE PONTE

**Tipo:** VÍDEO · **Área:** 03_ORQUESTRACAO-DE-AGENTES
**Hash F0:** `192C3748B93DDE8B`   **Hash reconferido:** `192C3748B93DDE8B`   **Confere:** sim
**Original:** **`AC-03-VID-007`** — `Gravando 2026-07-28 164919.mp4`, mesmo SHA-256 (`192C3748B93DDE8B`), mesmo tamanho (6,7 MB), mesma duração (10,8 s)
**LV:** LV3-V *(herdado de `AC-03-VID-007`)*
**Cobertura da leitura:** reconferência de hash desta cópia (idêntico ao do original e ao do manifesto) e da correspondência de duração no manifesto STT. **O conteúdo não foi reavaliado** — `05` §10: duplicata exata herda a ficha do original e mantém rastreabilidade própria.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-03-VID-008 · `H-M2-002` (`95`, que registra "008 é duplicata exata de 007") · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 · E03 · E05 · E06 · E07 · E13 · E15 | **herdados** | Todos os sete eixos herdam integralmente `AC-03-VID-007`, por identidade binária comprovada por SHA-256. Reavaliar o mesmo byte duas vezes produziria duplicação de evidência, não evidência independente | — |

**NF = herdado de `AC-03-VID-007` (2 · 2/7 · 5 ND)**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 · E04 · E14 | **herdados** | Idem — identidade binária | — |

**RP = herdado de `AC-03-VID-007` (3 · 3/3 · 0 ND)**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 · E09 · E10 · E11 · E12 | **herdados** | Idem — identidade binária | — |

**AA = herdado de `AC-03-VID-007` (4 · 5/5 · 0 ND)**

#### Catálogo (separado da fonte)
**NC = 5** — o catálogo **identifica corretamente a duplicata** e declara o critério: "Duplicata confirmada por hash: `164919` e `165017` têm conteúdo binário idêntico. Ambos foram preservados porque o pedido foi catalogar, não eliminar." Método declarado e confirmado pela reconferência de hash desta fase.
**O que o catálogo afirma:** "`Gravando 2026-07-28 165017.mp4` | 6,7 MB | equipe de agentes especializados para dashboard e análise — duplicata exata | duplicata; não transcrito"
**Confere com a fonte:** sim — reconferência independente de SHA-256 nesta fase confirma a identidade

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Ambos foram preservados porque o pedido foi catalogar, não eliminar." | `_CONTEUDO.md` área 03 | ALEGAÇÃO DO CATÁLOGO | — coerente com esta frente: `DUPLICADO` **não significa descartável** (`04` §9) |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V8 | não | hash reconferido idêntico ao do manifesto **e** ao do original |
| V5 | **não se aplica** | `04` §8, V5 tem exceção literal para item `DUPLICADO` por hash idêntico |
| V1 · V2 · V3 · V4 · V6 · V7 | herdados | as portas do original valem para a cópia |

#### Resultado
**RF = DUPLICADO**
**Regra que produziu:** §9, condição de entrada de DUPLICADO — hash idêntico a outro item do acervo, comprovado por reconferência SHA-256 nesta fase.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> `DUPLICADO` **não significa descartável.** O item mantém ID próprio, rastreabilidade e esta ficha de ponte; a avaliação de conteúdo vive em `AC-03-VID-007`.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-03-VID-009 — `Gravando 2026-07-28 203752.mp4`

**Tipo:** VÍDEO · **Área:** 03_ORQUESTRACAO-DE-AGENTES
**Hash F0:** `64A5943E3815E957`   **Hash reconferido:** `64A5943E3815E957`   **Confere:** sim
**LV:** LV3-V *(LV3-A = `SEM FALA LEXICAL CONFIÁVEL`, 1 palavra, p = 0,130)*
**Cobertura da leitura:** 9 quadros (`95`); ficha STT (22,6 s).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-03-VID-009 · `H-M2-002` (`95`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Cinco procedimentos exibidos em tela, com saída declarada em cada um: reescrever instruções persistentes; usar modelo caro como consultor produzindo roadmap e *stop list*; converter pesquisa profunda em notas atômicas ligadas; executar objetivo com prova e limite; registrar problema, abordagem, tentativas rejeitadas e regra reutilizável. Exemplo isolado, sem artefato (`95`) | — |
| E03 Maturidade | ND | — | Localizar a implementação e inspecionar seu estágio |
| E05 Manutenção | ND | — | Localizar o canal de publicação com data |
| E06 Segurança ⚠ | ND | — | Nenhuma superfície inspecionada |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | O procedimento 4 cita "prova e limite" como condição de saída, mas nenhuma rubrica é exibida; resolveria inspecionar a implementação |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas; nenhum número decisivo em jogo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: trata de **como o trabalho caro vira ativo reutilizável** por um executor mais barato — decisão de divisão de trabalho | — |
| E04 Transferibilidade | 3 | Os cinco procedimentos transferem com adaptação declarada; nenhum depende de ambiente do autor | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto no acervo: o registro de **tentativas rejeitadas** como parte do ativo — e não só da solução — não aparece em nenhum outro item | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 3,3 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado **e confirmado** pelos quadros: os quatro elementos citados no título (`CLAUDE.md`, skills, `/goal`, workflows) correspondem a quatro dos cinco procedimentos observados (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 203752.mp4` | 3,3 MB | cinco jogadas de `CLAUDE.md`, skills, `/goal` e workflows | não transcrito"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "**Achado central:** transformar trabalho caro em ativo permanente reproduzível por modelo mais barato." | `95` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | não |

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

### AC-03-VID-010 — `Gravando 2026-07-28 204200.mp4`

**Tipo:** VÍDEO · **Área:** 03_ORQUESTRACAO-DE-AGENTES
**Hash F0:** `ECA00A613D86A8C2`   **Hash reconferido:** `ECA00A613D86A8C2`   **Confere:** sim
**LV:** LV3-V *(LV3-A = `SEM FALA LEXICAL CONFIÁVEL`, 1 palavra, p = 0,130)*
**Cobertura da leitura:** 9 quadros (`95`); ficha STT (13,5 s).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-03-VID-010 · `H-M2-002` (`95`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só divulgação: cinco repositórios nomeados em tela (`google-labs-code/design.md`, `JCodesMore/ai-website-cloner-template`, `jamiepine/voicebox`, `penpot/penpot`, `ZhuLinsen/daily_stock_analysis`) sem demonstração, insumo ou artefato inspecionável (`95`) | — |
| E03 Maturidade | ND | — | Localizar cada um dos cinco repositórios e inspecionar versão, release e estabilidade |
| E05 Manutenção | ND | — | Verificar atividade datada em cada repositório na origem |
| E06 Segurança ⚠ | ND | — | **Superfície declarada e não inspecionada** em pelo menos dois dos cinco: clonagem de site e análise automática de mercado. Resolveria inspecionar cada repositório |
| E07 Licença ⚠ | ND | — | Ler a licença de cada um dos cinco na origem pública |
| E13 Testes/evals | ND | — | Nenhum teste exibido |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas (o que cada repositório faria); nenhum número decisivo em jogo nos quadros | — |

**NF = 1 · 2/7 · 5 ND** *(mediana de [1,3] = 2 → §14.3 vale o inferior)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça a pergunta de forma genérica: apresenta agentes verticais sem tratar de coordenação entre eles | — |
| E04 Transferibilidade | 1 | Só a ideia viaja; o que seria transferível está nos repositórios, não no vídeo | — |
| E14 Diferencial | 2 | Agregação de material público; a função de descoberta sobrepõe AC-06-VID-015 e AC-06-VID-018 | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 3,7 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado **e confirmado** pelos quadros: "direção visual, voz e análise de mercado" corresponde a três dos cinco repositórios observados (`design.md`, `voicebox`, `daily_stock_analysis`), sem contradizer os outros dois (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 204200.mp4` | 3,7 MB | agentes para direção visual, voz e análise de mercado | não transcrito"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "`google-labs-code/design.md`, `JCodesMore/ai-website-cloner-template`, `jamiepine/voicebox`, `penpot/penpot` e `ZhuLinsen/daily_stock_analysis`" | `95` (texto visual observado) | ALEGAÇÃO DO AUTOR | não — nenhum dos cinco foi localizado, lido ou clonado |
| "Verificar existência, licença, maturidade e segurança; não clonar/executar." | `95` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | — coerente com `05` §7.4 |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 3` · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** §9 — relevância aparente com lacuna nomeada e endereçável; teto de V2/V4 respeitado.
**Se EXIGE PESQUISA — lacuna nomeada:** existência, licença, maturidade e superfície de risco dos **cinco repositórios nomeados**, nenhum dos quais está no acervo.  **Verificação que a fecharia:** localizar cada repositório na origem pública e ler licença, README e estrutura — **sem clonar nem executar**; atenção reforçada a `ai-website-cloner-template` (direito autoral) e `daily_stock_analysis` (risco financeiro).

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-03-VID-011 — `Gravando 2026-07-29 091150.mp4`

**Tipo:** VÍDEO · **Área:** 03_ORQUESTRACAO-DE-AGENTES
**Hash F0:** `D5DE42134A780823`   **Hash reconferido:** `D5DE42134A780823`   **Confere:** sim
**LV:** LV3-V + LV3-A
**Cobertura da leitura:** 9 quadros (`95`); transcrição automática bruta integral (59,0 s, `pt`, 21 segmentos, p = 0,876, **ALTA AUTOMÁTICA**). Sem revisão humana.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-03-VID-011 · `H-M2-002` (`95`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Demonstração isolada: os quadros mostram subagentes paralelos gerando relatório para a sessão seguinte; a fala provável enumera cinco mecanismos — arquivo de instruções lido no início de toda conversa, limpeza de contexto, disparo de assistentes paralelos, comando próprio e arquivo de memória. Nenhum arquivo acompanha o vídeo | — |
| E03 Maturidade | ND | — | Localizar a implementação demonstrada e inspecionar seu estágio |
| E05 Manutenção | ND | — | Localizar o canal de publicação com data |
| E06 Segurança ⚠ | ND | — | Nenhuma superfície inspecionada; o arquivo de memória que "salva tudo que você corrige" é superfície de dados retratada, não inspecionada |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhum teste exibido |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas; nenhum número decisivo em jogo. A **atribuição à Anthropic** do uso de arquivo de instruções contra alucinação (`95`) é registrada abaixo como não verificada, mas não é numérica | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: fan-out para assistentes paralelos com consolidação em relatório único, mais memória explícita entre sessões | — |
| E04 Transferibilidade | 3 | Os cinco mecanismos transferem com adaptação declarada; independem de ambiente do autor | — |
| E14 Diferencial | 2 | Agregação: sobrepõe AC-02-VID-012, AC-04-VID-010 e AC-04-VID-011 no acervo | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 56,2 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT de 21 segmentos; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 2** — **PARCIAL.** O método é declarado e o que o catálogo registra confere, mas é **omissão material**: o vídeo apresenta **cinco** mecanismos (arquivo de instruções, limpeza de contexto, subagentes, comando próprio e arquivo de memória) e o catálogo registra apenas o terceiro e sua consolidação. Detalhe verificável parcialmente não conferido → teto 2 (§14.4).
**O que o catálogo afirma:** "`Gravando 2026-07-29 091150.mp4` | 56,2 MB | Claude dispara assistentes e consolida relatório | não transcrito"
**Confere com a fonte:** parcialmente

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Tudo que você escreve ali, aí a ler automaticamente no começo de toda a conversa." | LV3-A bruto, 00:00:09,280–00:00:12,920 — **fala provável, não citação exata** | ALEGAÇÃO DO AUTOR | não |
| "Aí ela começou a alucinar, dá um barra clear, e você tem o contexto novo." | LV3-A bruto, 00:00:18,680–00:00:22,080 — fala provável | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA`; relação causal entre contexto e alucinação não demonstrada |
| "atribui à Anthropic o uso de `CLAUDE.md` contra alucinação" | `95` (texto visual observado) | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA`; atribuição a fornecedor sem fonte identificada |
| "Tudo que você corrige, ele salva na próxima sessão, na próxima semana, no próximo mês." | LV3-A bruto, 00:00:52,360–00:00:56,720 — fala provável | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |

> O motor grafou "Cloud.md", "Calde", "suba a gente" (por *subagente*) e "com o texto da sessão" (por *contexto*). Não normalizado (`117`, regra de uso).

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

### AC-03-VID-012 — `Gravando 2026-07-29 091519.mp4`

**Tipo:** VÍDEO · **Área:** 03_ORQUESTRACAO-DE-AGENTES
**Hash F0:** `FF4B9F882F4FF0D9`   **Hash reconferido:** `FF4B9F882F4FF0D9`   **Confere:** sim
**LV:** LV3-V *(LV3-A = `SEM FALA LEXICAL CONFIÁVEL`, 1 palavra, p = 0,751)*
**Cobertura da leitura:** 9 quadros (`95`); ficha STT (8,6 s).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-03-VID-012 · `H-M2-002` (`95`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Fluxo operacional exibido em tela com componentes nomeados: objetivo com **condição de saída**, skill criada, execução local ou em VPS por SSH, agendamento por CRON, autoverificação e relatório a um canal de mensagem. Exemplo isolado, sem artefato (`95`) | — |
| E03 Maturidade | ND | — | Identificar "Hermes" e "SkillSmith" e inspecionar o estágio de cada um. **Nota**: um repositório Hermes está no acervo com ficha própria (`AC-03-REP-005`, `E03 = 4`); a identidade entre os dois **não foi confirmada** |
| E05 Manutenção | ND | — | Localizar o canal de publicação com data |
| E06 Segurança ⚠ | ND | — | **Superfície declarada, crítica e não inspecionada**: execução 24/7, acesso SSH a VPS, agendamento por CRON e credenciais. Resolveria inspecionar a implementação e os escopos exigidos |
| E07 Licença ⚠ | ND | — | Identificar os artefatos citados e ler suas licenças |
| E13 Testes/evals | ND | — | A "autoverificação" é exibida como etapa, não como suíte; resolveria inspecionar a implementação |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas; nenhum número decisivo em jogo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: um loop agendado que age, verifica e reporta — com **condição de saída** explícita e alerta contra loop infinito sem verificador | — |
| E04 Transferibilidade | 2 | O **padrão** transfere; a implementação depende de VPS, SSH e produtos não identificados | — |
| E14 Diferencial | 2 | Agregação: o loop com condição de saída já aparece em `AC-03-REP-008` (implementado) e em AC-05-VID-028 (citado) | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 3,9 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado **e confirmado** pelos quadros: loops agendados, autocheck e execução 24/7 correspondem ao observado (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-29 091519.mp4` | 3,9 MB | loops Hermes agendados, autocheck e execução 24/7 | não transcrito"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "goal com condição de saída, skill criada, Hermes local/VPS via SSH, CRON, auto-verificação e relatório ao Slack" | `95` (texto visual observado) | ALEGAÇÃO DO AUTOR | não |
| "**risco alto:** execução 24/7, SSH, cron, credenciais e custos. Hermes/SkillSmith ficam candidatos, não autorizados." | `95` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | não |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 3` · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** §9 — relevância aparente com lacuna nomeada e endereçável; teto de V2/V4 respeitado.
**Se EXIGE PESQUISA — lacuna nomeada:** (1) se o "Hermes" do vídeo é o mesmo `hermes-agent` de `AC-03-REP-005`, que já está no acervo com licença MIT lida; (2) identidade, origem e licença de "SkillSmith", que **não** está no acervo.  **Verificação que a fecharia:** comparar os quadros com o README de `AC-03-REP-005` e localizar "SkillSmith" na origem pública — sem instalar nem executar.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-03-VID-013 — `Gravando 2026-07-29 091907.mp4`

**Tipo:** VÍDEO · **Área:** 03_ORQUESTRACAO-DE-AGENTES
**Hash F0:** `6CAB17662ACBADD8`   **Hash reconferido:** `6CAB17662ACBADD8`   **Confere:** sim
**LV:** LV3-V *(LV3-A = `SEM FALA LEXICAL CONFIÁVEL`, 2 palavras, p = 0,508)*
**Cobertura da leitura:** 9 quadros (`95`); ficha STT (14,1 s).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-03-VID-013 · `H-M2-002` (`95`) · `H-M3-001` (`117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Escada de capacidades exibida em tela, com sete degraus ordenados — Prompt → Contexto/arquivo de instruções → Ferramentas → MCP → Skills → Subagentes → Equipes de Agentes — e o último **declarado experimental/manual**. Exemplo isolado, sem implementação (`95`) | — |
| E03 Maturidade | ND | — | Localizar a publicação de origem e seu versionamento |
| E05 Manutenção | ND | — | Localizar o canal de publicação com data |
| E06 Segurança ⚠ | ND | — | Nenhuma superfície inspecionada; cada degrau amplia a superfície sem que o vídeo declare controles |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhum critério de passagem entre degraus é exibido; resolveria obter a fonte primária |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas (ordenação de maturidade); nenhum número decisivo em jogo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: propõe **ordem de adoção** de capacidades de coordenação, e marca a camada de equipes como a última e menos madura | — |
| E04 Transferibilidade | 3 | A escada transfere com adaptação declarada; independe de fornecedor | — |
| E14 Diferencial | 2 | Agregação: o mesmo ordenamento aparece em AC-02-PRT-004 (iceberg) e AC-05-PRT-012 (dez níveis) dentro do acervo | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 3,8 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado **e confirmado** pelos quadros: a progressão "de prompt a MCP, subagentes e automação" corresponde à escada observada (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-29 091907.mp4` | 3,8 MB | evolução de prompt a MCP, subagentes e automação | não transcrito"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "A última camada é apresentada como experimental/manual." | `95` (texto visual observado) | ALEGAÇÃO DO AUTOR | não |
| "**Valor alto:** modelo de maturidade; não implica que todas as camadas sejam necessárias." | `95` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | não |

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

## Fechamento da área 03

| Métrica | Valor |
|---|---:|
| Itens representados | 31 / 31 |
| Fichas válidas contra `04` §13 | 31 |
| Hashes / estruturas reconferidos · divergentes | 31 · **0** |
| Itens em **LV4** | 10 (os 10 repositórios) |
| `RF = CANDIDATO FORTE` | 4 — AC-03-REP-001, AC-03-REP-004, AC-03-REP-005, AC-03-REP-010 |
| `RF = CANDIDATO A PILOTO` | 2 — AC-03-REP-002, AC-03-REP-008 |
| `RF = PADRÃO A ESTUDAR` | 1 — AC-03-REP-007 |
| `RF = EXIGE PESQUISA` | 9 |
| `RF = REFERÊNCIA` | 14 |
| `RF = DUPLICADO` | 1 — AC-03-VID-008 |
| `RF = INDETERMINADO` | 0 |
| Total de eixos possíveis (31 × 15) | 465 |
| Eixos determinados | 354 |
| Eixos em `ND` | **111 (23,9%)** — **105 deles em itens de mídia** (21 itens × 5) e **6 nos dez repositórios** *(recontado por ferramenta sobre as fichas em 2026-07-29; o valor anterior, 152, com "145 em mídia", era estimativa e foi corrigido — ver `99_RELATORIO-DA-FASE-2.md` §6)* |
| Divergências catálogo × fonte | **2 divergentes** (`NC = 0`: AC-03-REP-003, e a instrução "Não analise." não obedecida) · **4 parciais** (AC-03-PRT-008, AC-03-VID-002, AC-03-VID-003, AC-03-VID-011) |

**Achados de contradição registrados nesta área, sem resolução silenciosa:**

1. **AC-03-VID-001 × AC-03-REP-002** — o vídeo divulga "50 mil estrelas"; o README do mesmo projeto, no acervo, declara "211.9K+ stars". Nenhum dos dois foi verificado; **P-3** impede que qualquer um mova eixo.
2. **AC-03-REP-009** — o README declara "100+ specialized agents" e o `package.json` do mesmo repositório declara "60+"; a versão do pacote (3.25.6) não se reconcilia com a do changelog (3.5.0).
3. **AC-03-REP-002** — o README adverte contra "third-party re-uploads and unofficial mirrors"; o item avaliado **é** uma cópia local fora desses canais.
4. **AC-03-REP-003** — o catálogo instrui `"Não analise."` alegando "nenhum conteúdo original", e o delta medido na Fase 0 tem 7 arquivos. Instrução não obedecida, `NC = 0`.
5. **DEF-11** — `AC-03-REP-005` alcança CANDIDATO FORTE com `E10 = 0`, porque §9 só proíbe `Bloco C = 0` em CANDIDATO A PILOTO. O mesmo item não poderia ser proposto como piloto.
6. **DEF-12** — `AC-03-REP-006` e `AC-03-REP-009` satisfazem todos os portões de qualidade mas falham em uma única condição de entrada (`RP = 3`, ou `E10 = 0`), e §9 não oferece classificação natural para esse caso; ambos caíram em EXIGE PESQUISA com lacuna nomeada.

Nenhuma fonte foi modificada. Nenhum repositório foi executado, instalado ou importado. Nenhum item foi adotado, ordenado, priorizado ou recomendado.
