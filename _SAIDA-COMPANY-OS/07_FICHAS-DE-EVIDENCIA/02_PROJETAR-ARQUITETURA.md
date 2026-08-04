> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

# FICHAS DE EVIDÊNCIA — ÁREA 02 — PROJETAR ARQUITETURA

**Fase:** 2 — Extração · **Data:** 2026-07-29 · **Avaliador:** Claude Opus 5 (Fase 2)
**Itens:** 24 — 1 REPO · 10 PRINT · 13 VÍDEO · 0 PLANILHA
**Convenções de aplicação:** `00_INDICE-DA-FASE-2.md` §3 (LV por tipo, Bloco C para mídia, NC, REFERÊNCIA × EXIGE PESQUISA)

**Pergunta central da área (base de E01):** *que forma o sistema tem — quais camadas, em que ordem de construção.*

---

### AC-02-REP-001 — `ai-orchestrator-starter`

**Tipo:** REPO
**Área:** 02_PROJETAR-ARQUITETURA
**Hash F0:** `dir · 25 arq. · aninhado`   **Hash reconferido:** `25 arq. · aninhamento 1`   **Confere:** sim (reconferência estrutural, `05` §6)
**LV:** LV4
**Cobertura da leitura:** raiz efetiva `ai-orchestrator-starter/ai-orchestrator-starter`; listagem completa da raiz (10 entradas); busca por `LICENSE`/`COPYING`/`LICENCE` na raiz efetiva — **ausente**; `README.md` integral (2.285 bytes); `pyproject.toml` integral; listagem de `tests/` (1 arquivo, `test_router.py`); presença de `.env.example`, `Dockerfile`, `docker-compose.yml`, `Makefile`. **Não lidos:** `app/`, `config/`, `skills/` (teto de `05` §8).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** não se aplica

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 4 | Artefato completo e inspecionável (código, `Dockerfile`, `docker-compose.yml`, `pyproject.toml`) correspondente à afirmação do README, **mais** procedimento de verificação declarado: seção "Teste rápido" com três chamadas `curl` reproduzíveis e `tests/test_router.py`. Não executado por esta frente | — |
| E03 Maturidade | 2 | `version = "0.1.0"` em `pyproject.toml`; **sem** tag, release ou changelog na raiz efetiva; README lista sete "Próximos passos de produção", entre eles "Trocar o armazenamento em memória por PostgreSQL" e "Adicionar autenticação e RBAC" | — |
| E05 Manutenção | ND | — | Consultar a origem pública do repositório: datas de commit, issues e cadência. Cópia estática `-main` sem histórico (`04` §5, regra específica do acervo) |
| E06 Segurança ⚠ | 3 | Superfície declarada na fonte (portas 8000/5678/4000 em `docker-compose.yml`, chaves de provedor via `.env.example`) **com controles parciais documentados**: Policy Engine que "bloqueia ações críticas sem aprovação" e endpoint `POST /v1/runs/{id}/approve` com revisor humano. `.env.example` em vez de segredo versionado. **`app/` não foi lido** — a nota mede a superfície documentada, não o código | — |
| E07 Licença ⚠ | ND | — | **Não há arquivo de licença na raiz efetiva** (procurado e não encontrado). Resolveria ler a licença na origem pública. `05` §3.1: ausência é indeterminação de procedência, não permissão negada |
| E13 Testes/evals | 2 | `tests/` inspecionado: existe e contém **1 arquivo** (`test_router.py`) para um fluxo de cinco estados; `pytest>=8.0` declarado em `optional-dependencies.dev`. Nenhum eval de comportamento de agente | — |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas no README ("MVP vendor-neutral", "funciona em `MOCK_MODE=true` sem chaves"); nenhum número decisivo em jogo | — |

**NF = 3 · 5/7 · 2 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 4 | Endereça diretamente a pergunta central da área — camadas e ordem — **mais** traz artefato concreto e reutilizável (§14.2): grafo de cinco estados `triage → plan → execute → review → approval`, tabela de roteamento por `task_type` e `pyproject.toml` executável | — |
| E04 Transferibilidade | 3 | Transferível com adaptação declarada e delimitada: dependências de ambiente estão explícitas (`docker-compose.yml`, `.env.example`, `requires-python >=3.12`), mas exigem Docker, PostgreSQL, Redis e n8n | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto **dentro do acervo**: é o único dos 43 repositórios cuja proposta central é o grafo de orquestração com portão de aprovação, e não uma coleção de skills ou uma ferramenta pontual | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 4 | Instalação declarada em dois comandos (`cp .env.example .env`; `docker compose up --build`), configuração por variável de ambiente. Não alcança 5: exige serviços acompanhantes (PostgreSQL, Redis, n8n, LiteLLM) | — |
| E09 Custo | 4 | Custo marginal: `MOCK_MODE=true` roda sem chave; em uso real, apenas chamadas de modelo já previstas. Infra roda em contêineres locais, sem licença paga declarada | — |
| E10 Contexto/tokens | 4 | Medido: **25 arquivos, 19,3 KB** — menos de 1 MB e menos de 50 arquivos, com superfície delimitada pelo `README.md` | — |
| E11 Fornecedor | 4 | Abstração de fornecedor documentada: LiteLLM como "gateway único para múltiplos provedores" e tabela de roteamento com sete pares executor/revisor; troca por configuração | — |
| E12 Reversibilidade | 3 | Reversível por remoção (`docker compose down`), com efeito colateral declarado no próprio README: armazenamento ainda em memória, a ser trocado por PostgreSQL | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (stack de oito itens, grafo de cinco estados, `MOCK_MODE=true`, "apenas 25 arquivos") e o detalhe **confere**: os 25 arquivos foram contados, o grafo e o stack estão no README, `MOCK_MODE` está declarado. Não chega a 4 porque o `_CONTEUDO.md` não declara o método pelo qual obteve a descrição.
**O que o catálogo afirma:** "MVP vendor-neutral para orquestrar OpenAI, Anthropic, Gemini, xAI/Grok e tarefas delegadas ao Manus… Roda em `MOCK_MODE=true` sem nenhuma chave de API. Apenas 25 arquivos — dá para ler inteiro."
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "**Comece pelo `ai-orchestrator-starter`.**" | `_CONTEUDO.md` área 02 | ALEGAÇÃO DO CATÁLOGO + `DECISÃO DE ESCOPO DE TERCEIRO` | instrução **não obedecida** (`04` §14.5); a ordem de avaliação seguiu o ID do manifesto |
| "É o único item do acervo que já é um blueprint executável, não uma referência." | `_CONTEUDO.md` área 02 | ALEGAÇÃO DO CATÁLOGO | **contradita** por fato observado: `AC-03-REP-005`, `AC-03-REP-006`, `AC-03-REP-007`, `AC-08-REP-002` e outros também são projetos executáveis. A contradição é sobre o acervo, não sobre esta fonte — registrada aqui, sem alterar NC |
| "As assinaturas dos aplicativos não substituem créditos de API. O projeto funciona em `MOCK_MODE=true` sem chaves." | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não |
| "**Policy Engine**: bloqueia ações críticas sem aprovação." | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — `app/` não lido |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V2 · V3 · V5 · V6 · V7 · V8 | não | `E06 = 3` (≠ 0 e ≠ ND) · `E07 ≠ 0` · `LV = 4` · 2 ND de 15 · `E15 = 3` · reconferência estrutural confere |
| **V4** | **sim** | `E07 = ND` — licença ausente na raiz efetiva → nunca CANDIDATO FORTE nem CANDIDATO A PILOTO |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** V4 (§8) — `E07 = ND` bloqueia as duas classificações de candidato; §9 EXIGE PESQUISA com lacuna nomeada.
**Se EXIGE PESQUISA — lacuna nomeada:** licença e titularidade do repositório, ausentes na raiz efetiva (bloqueio B-02).  **Verificação que a fecharia:** localizar a origem pública do repositório e ler o texto da licença; secundariamente, ler `app/` para confirmar se o Policy Engine implementa o controle que o README declara.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-02-PRT-001 — `AgenticWOorld.png`

**Tipo:** PRINT · **Área:** 02_PROJETAR-ARQUITETURA
**Hash F0:** `93FD2C2D75311F44`   **Hash reconferido:** `93FD2C2D75311F44`   **Confere:** sim
**LV:** LV3-V
**Cobertura da leitura:** inspeção visual do original pela trilha Codex (`105`, lote 07); descrição do `_CONTEUDO.md` confrontada com os pixels. Esta frente não abriu a imagem.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** AC-02-PRT-001 · `H-P1-001` (relatório `105`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Diagrama isolado e não reprodutível: quatro camadas concêntricas (LLMs · AI Agents · Agentic Systems · Agentic Infra) sem insumo, método ou artefato acompanhante (`105`, CONFIRMADA) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e seu versionamento |
| E05 Manutenção | ND | — | Localizar o canal de publicação com data e cadência |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial visível ou instrução dirigida ao leitor |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos de uso do infográfico |
| E13 Testes/evals | ND | — | Não há artefato testável; resolveria localizar a fonte primária do modelo de camadas |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas (nomes de capacidade por camada, incl. HIPAA e AI Act como itens de governança); nenhum número decisivo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: define **quais camadas** existem e a relação de dependência entre elas | — |
| E04 Transferibilidade | 3 | Taxonomia transferível com adaptação declarada — as quatro camadas não dependem de ambiente do autor | — |
| E14 Diferencial | 2 | Agregação de material público; sobrepõe AC-02-PRT-010 e AC-02-VID-007 na função de mapa de camadas | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação; formato de consumo não declarado | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 1,3 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `105` + parágrafo do `_CONTEUDO.md`; < 1 MB | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (as quatro camadas e seus itens) conferido contra os pixels; CONFIRMADA em `105`.
**O que o catálogo afirma:** "Círculos concêntricos, de dentro para fora: 1. **LLMs**… 2. **AI Agents**… 3. **Agentic Systems**… 4. **Agentic Infra** — governança (HIPAA, AI Act), observabilidade, segurança e controle de acesso, viés, tratamento de erro e retentativa."
**Confere com a fonte:** sim — CONFIRMADA em `105`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "cada camada só existe apoiada na anterior" | `_CONTEUDO.md` área 02 | ALEGAÇÃO DO CATÁLOGO | não |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 3` · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` → teto REFERÊNCIA / PADRÃO A ESTUDAR / EXIGE PESQUISA |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4 do índice (o valor é o próprio conteúdo, sem artefato externo a verificar).
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-02-PRT-002 — `AI Agent.png`

**Tipo:** PRINT · **Área:** 02_PROJETAR-ARQUITETURA
**Hash F0:** `7B1EA2076807A263`   **Hash reconferido:** `7B1EA2076807A263`   **Confere:** sim
**LV:** LV3-V
**Cobertura da leitura:** inspeção visual do original pela trilha Codex (`105`, lote 07). Esta frente não abriu a imagem.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** AC-02-PRT-002 · `H-P1-001` (relatório `105`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Checklist isolado e não reprodutível: nove componentes com prós, contras e "use quando", sem insumo nem artefato (`105`, CONFIRMADA) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e seu versionamento |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial ou instrução ao leitor |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhum artefato testável associado |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas (prós/contras por componente); nenhum número decisivo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: enumera os componentes que compõem o sistema e obriga uma decisão dentro/fora por item | — |
| E04 Transferibilidade | 3 | Checklist transferível com adaptação declarada; inclui explicitamente guardrails e humano no loop | — |
| E14 Diferencial | 2 | Agregação de material público; sobrepõe AC-02-PRT-003 e AC-05-VID-005 | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 2,8 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `105` + parágrafo do `_CONTEUDO.md` | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (os nove componentes nomeados e seus subitens) conferido contra os pixels; CONFIRMADA em `105`.
**O que o catálogo afirma:** "1 LLM (o cérebro) · 2 Memória… · 3 RAG… · 4 Ferramentas · 5 Planejamento… · 6 Reflexão… · 7 Multi-agente… · 8 Monitoramento e guardrails… · 9 Humano no loop (aprovar / editar / rejeitar)."
**Confere com a fonte:** sim — CONFIRMADA em `105`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "use como lista de verificação — o desenho final precisa dizer, para cada um dos nove, se está dentro ou fora e por quê" | `_CONTEUDO.md` área 02 | ALEGAÇÃO DO CATÁLOGO | não |

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

### AC-02-PRT-003 — `Captura de tela 2026-07-28 152916.png`

**Tipo:** PRINT · **Área:** 02_PROJETAR-ARQUITETURA
**Hash F0:** `CEAA0CEEBF477F85`   **Hash reconferido:** `CEAA0CEEBF477F85`   **Confere:** sim
**LV:** LV3-V
**Cobertura da leitura:** inspeção visual do original pela trilha Codex (`105`, lote 07). Esta frente não abriu a imagem.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** AC-02-PRT-003 · `H-P1-001` (relatório `105`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Roadmap isolado e não reprodutível: oito blocos mais tabela comparativa de categorias de produto, sem insumo nem artefato (`105`, CONFIRMADA) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e seu versionamento |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial ou instrução ao leitor |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | O bloco 8 nomeia "Testes e evals" como etapa, mas o print não traz nenhum; resolveria localizar a fonte primária |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas (sequência de decisões, comparação por categoria); nenhum número decisivo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a segunda metade da pergunta central — **em que ordem de construção** —, colocando propósito e critério de sucesso antes de framework | — |
| E04 Transferibilidade | 3 | Sequência transferível com adaptação declarada; não depende de produto específico | — |
| E14 Diferencial | 2 | Agregação de material público; sobrepõe AC-02-PRT-002 e AC-02-PRT-010 | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 2,2 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `105` + parágrafo do `_CONTEUDO.md` | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (os oito blocos, na ordem, mais a tabela de rodapé) conferido contra os pixels; CONFIRMADA em `105`.
**O que o catálogo afirma:** "Roadmap “How to Build an AI Agent”… 1. Definir propósito e escopo… 8. Testes e evals — teste unitário, latência, qualidade, iteração e melhoria."
**Confere com a fonte:** sim — CONFIRMADA em `105`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "é uma sequência de decisões, não uma lista de ferramentas. A ordem evita escolher framework antes de definir propósito, contrato de saída e critério de qualidade." | `_CONTEUDO.md` área 02 | ALEGAÇÃO DO CATÁLOGO | não |

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

### AC-02-PRT-004 — `coisas para criar e melhorar .png`

**Tipo:** PRINT · **Área:** 02_PROJETAR-ARQUITETURA
**Hash F0:** `884C58983621E0FC`   **Hash reconferido:** `884C58983621E0FC`   **Confere:** sim
**LV:** LV3-V
**Cobertura da leitura:** inspeção visual do original pela trilha Codex (`105`, lote 07). Esta frente não abriu a imagem. Nome preservado com o espaço antes da extensão, como está no disco.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** AC-02-PRT-004 · `H-P1-001` (relatório `105`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Iceberg isolado e não reprodutível: progressão de capacidades sem critério de passagem entre níveis nem artefato (`105`, CONFIRMADA) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e seu versionamento |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial ou instrução ao leitor. O conteúdo cita "execuções noturnas não supervisionadas" e "agentes gerenciando agentes" — superfície de risco **retratada**, não inspecionada |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhum artefato testável associado |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas (ordenação de maturidade); nenhum número decisivo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente "em que ordem de construção": ordena MCP, subagentes, hooks, skills, headless e orquestração multi-repositório em oito degraus | — |
| E04 Transferibilidade | 3 | Progressão transferível com adaptação declarada; os produtos citados são exemplos, não requisitos | — |
| E14 Diferencial | 2 | Agregação de material público; sobrepõe AC-01-PRT-001 (mesmo formato de iceberg) e AC-03-VID-013 (escada de capacidades) | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 3,1 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `105` + parágrafo do `_CONTEUDO.md` | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (os oito degraus, em ordem, com os produtos de cada um) conferido contra os pixels; CONFIRMADA em `105`.
**O que o catálogo afirma:** "Da superfície ao fundo: Lovable/Bolt/ChatGPT… → **agentes gerenciando agentes, orquestração multi-repositório, ferramentas construídas por agentes**."
**Confere com a fonte:** sim — CONFIRMADA em `105`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "é o roadmap de ambição. Diz em que ordem adotar MCP, subagentes, hooks, skills e execução headless — e qual é o horizonte final." | `_CONTEUDO.md` área 02 | ALEGAÇÃO DO CATÁLOGO + `DECISÃO DE ESCOPO DE TERCEIRO` (propõe roadmap) | não — não convertido em roadmap (`04` §11) |

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

### AC-02-PRT-005 — `loop0.png`

**Tipo:** PRINT · **Área:** 02_PROJETAR-ARQUITETURA · **Série:** `loop0`–`loop3` (carrossel de 4, avaliados individualmente — `05` §2.2)
**Hash F0:** `062BBCCF3D2BA4E2`   **Hash reconferido:** `062BBCCF3D2BA4E2`   **Confere:** sim
**LV:** LV3-V
**Cobertura da leitura:** inspeção visual do original pela trilha Codex (`105`, lote 07). Esta frente não abriu a imagem.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** AC-02-PRT-005 · `H-P1-001` (relatório `105`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só afirmação: o slide sustenta a tese de que "os dois labs concordam" sem nenhum artefato, citação ou referência inspecionável (`105`: "consenso e caráter de “padrão” não foram verificados") | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e seu versionamento |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial ou instrução ao leitor |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhum artefato testável associado |
| E15 Alegações ⚠ | 0 | A proposta central do slide **depende** de uma alegação de autoridade sem fonte — que Anthropic e OpenAI teriam chegado à mesma conclusão —, não verificável com o material disponível. É atribuição a terceiro, não medição | — |

**NF = 0 · 2/7 · 5 ND** *(mediana de [0,1] = 0,5 → §14.3 vale o inferior)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça a pergunta de forma genérica: afirma a superioridade do loop sem particularizar camada, ordem ou implementação | — |
| E04 Transferibilidade | 1 | Só a ideia viaja; o slide não traz nada implementável | — |
| E14 Diferencial | 1 | Conveniência sobre algo já acessível; é o slide de abertura de uma série cujo conteúdo está em AC-02-PRT-006 a 008 | — |

**RP = 1 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 1,5 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `105` + linha do `_CONTEUDO.md` | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável conferido contra os pixels; CONFIRMADA em `105` ("O print contém a alegação catalogada").
**O que o catálogo afirma:** "**loop0** — *Os dois labs*: Anthropic e OpenAI chegaram sozinhas à mesma ideia — loop agêntico rende mais que prompt de uma tacada só. “Quando concorrente concorda, virou padrão.”"
**Confere com a fonte:** sim — a **existência** da alegação confere; a alegação em si não foi verificada

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Quando concorrente concorda, virou padrão." | print (texto observado) | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "Anthropic e OpenAI chegaram sozinhas à mesma ideia" | `_CONTEUDO.md` área 02 / print | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |
| **V7** | **sim** | `E15 = 0` e a tese do slide depende da alegação de autoridade → teto EXIGE PESQUISA |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** V7 (§8) — teto EXIGE PESQUISA.
**Se EXIGE PESQUISA — lacuna nomeada:** a atribuição a Anthropic e OpenAI não tem fonte identificada.  **Verificação que a fecharia:** localizar as publicações primárias dos dois fornecedores e confirmar se, e em que termos, cada um afirma o que o slide lhes atribui.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-02-PRT-006 — `loop1.png`

**Tipo:** PRINT · **Área:** 02_PROJETAR-ARQUITETURA · **Série:** `loop0`–`loop3`
**Hash F0:** `1AC57D8A900F703B`   **Hash reconferido:** `1AC57D8A900F703B`   **Confere:** sim
**LV:** LV3-V
**Cobertura da leitura:** inspeção visual do original pela trilha Codex (`105`, lote 07). Esta frente não abriu a imagem.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** AC-02-PRT-006 · `H-P1-001` (relatório `105`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Diagrama isolado e não reprodutível: os cinco nós do loop (faz → se avalia → critica → reescreve → repete) aparecem como fluxo visual, sem insumo nem execução (`105`, CONFIRMADA) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e seu versionamento |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial ou instrução ao leitor |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | O nó "se avalia" pressupõe rubrica, ausente do print; resolveria localizar a fonte primária com o checklist |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas; nenhum número decisivo em jogo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: define uma camada de controle (avaliador + condição de convergência) do sistema | — |
| E04 Transferibilidade | 2 | O **padrão** do loop é transferível; a implementação (quem avalia, contra o quê) não está no print | — |
| E14 Diferencial | 2 | Agregação de material público; converge com AC-09-VID-003 e AC-03-VID-006 dentro do acervo | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 1,5 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `105` + linha do `_CONTEUDO.md` | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (os cinco nós, nomeados) conferido contra os pixels; CONFIRMADA em `105`.
**O que o catálogo afirma:** "**loop1** — *O conceito*: o modelo faz o trabalho, se nota contra um checklist e conserta, até ficar bom. Cinco nós: faz → se avalia → critica → reescreve → repete."
**Confere com a fonte:** sim — CONFIRMADA em `105`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "o modelo faz o trabalho, se nota contra um checklist e conserta, até ficar bom" | `_CONTEUDO.md` área 02 / print | ALEGAÇÃO DO AUTOR | não |

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

### AC-02-PRT-007 — `loop2.png`

**Tipo:** PRINT · **Área:** 02_PROJETAR-ARQUITETURA · **Série:** `loop0`–`loop3`
**Hash F0:** `8D0159C96C9C8E7A`   **Hash reconferido:** `8D0159C96C9C8E7A`   **Confere:** sim
**LV:** LV3-V
**Cobertura da leitura:** inspeção visual do original pela trilha Codex (`105`, lote 07). Esta frente não abriu a imagem.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** AC-02-PRT-007 · `H-P1-001` (relatório `105`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só afirmação de contraste ("One-shot é sorte. Loop é sistema."), sem artefato, medição ou exemplo reprodutível (`105`, CONFIRMADA) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e seu versionamento |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial ou instrução ao leitor |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhum artefato testável associado |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas; nenhum número decisivo em jogo | — |

**NF = 1 · 2/7 · 5 ND** *(mediana de [1,3] = 2 → §14.3 vale o inferior: 1)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça a pergunta de forma genérica: justifica o loop sem particularizar camada ou ordem | — |
| E04 Transferibilidade | 1 | Só a ideia viaja | — |
| E14 Diferencial | 1 | Conveniência; é o slide de contraste da mesma série | — |

**RP = 1 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 1,5 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `105` + linha do `_CONTEUDO.md` | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (a frase de contraste e a estrutura do slide) conferido contra os pixels; CONFIRMADA em `105`.
**O que o catálogo afirma:** "**loop2** — *O contraste*: “One-shot é sorte. Loop é sistema.” Prompt te dá o que voltar; loop continua até passar."
**Confere com a fonte:** sim — CONFIRMADA em `105`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "One-shot é sorte. Loop é sistema." | print (texto observado) | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |

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

### AC-02-PRT-008 — `loop3.png`

**Tipo:** PRINT · **Área:** 02_PROJETAR-ARQUITETURA · **Série:** `loop0`–`loop3`
**Hash F0:** `FCE71FCD00DEBCC2`   **Hash reconferido:** `FCE71FCD00DEBCC2`   **Confere:** sim
**LV:** LV3-V
**Cobertura da leitura:** inspeção visual do original pela trilha Codex (`105`, lote 07). Esta frente não abriu a imagem.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** AC-02-PRT-008 · `H-P1-001` (relatório `105`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Procedimento em três passos exibido no slide (ideia crua → autoavaliação contra checklist → parada por aprovação), sem checklist concreto nem execução (`105`, CONFIRMADA) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e seu versionamento |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial ou instrução ao leitor |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | O passo 02 pressupõe um checklist que o print não exibe; resolveria localizar a fonte primária |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas; nenhum número decisivo em jogo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central ao definir **critério de parada** como aprovação em rubrica — requisito de uma camada de controle | — |
| E04 Transferibilidade | 2 | O padrão é transferível; a rubrica de parada, que é a parte difícil, não está no print | — |
| E14 Diferencial | 2 | Agregação de material público; converge com AC-09-VID-003 e AC-03-VID-006 | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 1,5 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `105` + linha do `_CONTEUDO.md` | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (os três passos numerados) conferido contra os pixels; CONFIRMADA em `105`.
**O que o catálogo afirma:** "**loop3** — *Na prática*: 01 dá uma ideia crua (meia ideia serve) · 02 deixa ele se avaliar contra um checklist · 03 só para quando passa."
**Confere com a fonte:** sim — CONFIRMADA em `105`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "o critério de parada é aprovação em rubrica, não “primeira resposta aceitável”. Isso vira código: o orquestrador precisa de um avaliador e de uma condição de convergência." | `_CONTEUDO.md` área 02 | ALEGAÇÃO DO CATÁLOGO + `DECISÃO DE ESCOPO DE TERCEIRO` (prescreve implementação) | não — não convertido em requisito (`04` §11) |

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

### AC-02-PRT-009 — `Rag + IA.png`

**Tipo:** PRINT · **Área:** 02_PROJETAR-ARQUITETURA
**Hash F0:** `32D0CE07F68D01D6`   **Hash reconferido:** `32D0CE07F68D01D6`   **Confere:** sim
**LV:** LV3-V
**Cobertura da leitura:** inspeção visual do original pela trilha Codex (`105`, lote 07). Esta frente não abriu a imagem.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** AC-02-PRT-009 · `H-P1-001` (relatório `105`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Três diagramas de fluxo comparados (RAG · AI Agents · Agentic RAG), isolados e não reprodutíveis; nenhum insumo, medição ou implementação (`105`, CONFIRMADA "em nível essencial") | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e seu versionamento |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial ou instrução ao leitor |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhum artefato testável associado |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas (o que cada arquitetura faz); nenhum número decisivo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: escolhe o **nível de sofisticação** em que o sistema nasce, decisão de camada | — |
| E04 Transferibilidade | 3 | Comparação transferível com adaptação declarada; os três fluxos são independentes de fornecedor | — |
| E14 Diferencial | 2 | Agregação de material público; sobrepõe AC-04-VID-001 e AC-04-VID-005 (RAG/CAG/MAG) dentro do acervo | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 1,9 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `105` + parágrafo do `_CONTEUDO.md` | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (os três fluxos e o resumo do rodapé) conferido contra os pixels; CONFIRMADA em `105`.
**O que o catálogo afirma:** "Três faixas comparadas… Resumo do rodapé: *RAG recupera conhecimento, agentes tomam ação, Agentic RAG orquestra sistemas autônomos*."
**Confere com a fonte:** sim — CONFIRMADA em `105`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "RAG recupera conhecimento, agentes tomam ação, Agentic RAG orquestra sistemas autônomos" | print (texto observado) | ALEGAÇÃO DO AUTOR | não |
| "é a escolha do nível de sofisticação em que o sistema nasce. Decidir isso cedo evita reescrita." | `_CONTEUDO.md` área 02 | ALEGAÇÃO DO CATÁLOGO | não |

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

### AC-02-PRT-010 — `The agent knwoledge.png`

**Tipo:** PRINT · **Área:** 02_PROJETAR-ARQUITETURA
**Hash F0:** `3161859DAD8333A5`   **Hash reconferido:** `3161859DAD8333A5`   **Confere:** sim
**LV:** LV3-V
**Cobertura da leitura:** inspeção visual do original pela trilha Codex (`105`, lote 07), com verificação da atribuição da anotação de rodapé. Esta frente não abriu a imagem. Grafia do nome preservada.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** AC-02-PRT-010 · `H-P1-001` (relatório `105`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Grafo de dependências em cinco níveis, isolado e não reprodutível; a fonte é nomeada (Field Guide Vol. 02, Brij Kishore Pandey) mas nenhum artefato acompanha (`105`) | — |
| E03 Maturidade | ND | — | Localizar o Field Guide Vol. 02 na origem e verificar versão/edição |
| E05 Manutenção | ND | — | Verificar cadência de publicação da série na origem |
| E06 Segurança ⚠ | ND | — | Inspeção direta da imagem procurando credencial ou instrução ao leitor |
| E07 Licença ⚠ | ND | — | Identificar termos de uso do Field Guide |
| E13 Testes/evals | ND | — | O nível 4 nomeia "avaliação e observabilidade", mas o print não traz nenhum eval; resolveria obter a fonte primária |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas (ordem de aprendizado, papel do loop de reflexão); nenhum número decisivo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente as duas metades da pergunta central: **quais camadas** (cinco níveis) e **em que ordem** (de baixo para cima) | — |
| E04 Transferibilidade | 3 | Grafo transferível com adaptação declarada; independe de fornecedor | — |
| E14 Diferencial | 2 | Agregação de material público; sobrepõe AC-02-PRT-001 e AC-02-PRT-004 | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; PNG local de 2,8 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = entrada em `105` + parágrafo do `_CONTEUDO.md` | — |
| E11 Fornecedor | 5 | PNG, formato aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 2** — **PARCIAL** em `105`: os cinco níveis estão bem descritos, mas o catálogo **atribui ao bloco Reflection/Self-Critique** a anotação "This is the loop that separates agents that compound from agents that repeat", e o print não permite essa atribuição exclusiva — a seta aponta para um ciclo de feedback/memória mais amplo. Inferência material não conferida → teto 2 (§14.4).
**O que o catálogo afirma:** "A anotação do autor é a parte útil: *não se aprende de cima para baixo — a maioria dos times tenta começar no nível 5*. E: *o loop de reflexão é o que separa agentes que compõem dos que repetem*."
**Confere com a fonte:** parcialmente — correção material 3 de `105`: substituir "o loop de reflexão" por "o ciclo de feedback/memória indicado pelo autor"

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "This is the loop that separates agents that compound from agents that repeat" | print (texto observado) | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA`; atribuição de bloco corrigida por `105` |
| "não se aprende de cima para baixo — a maioria dos times tenta começar no nível 5" | print / `_CONTEUDO.md` área 02 | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "é a ordem de construção. Use como cronograma, não como catálogo." | `_CONTEUDO.md` área 02 | ALEGAÇÃO DO CATÁLOGO + `DECISÃO DE ESCOPO DE TERCEIRO` (propõe cronograma) | não — não convertido em roadmap (`04` §11) |

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

### AC-02-VID-001 — `anatomai de projeto.mp4`

**Tipo:** VÍDEO · **Área:** 02_PROJETAR-ARQUITETURA
**Hash F0:** `5CB921F03732277F`   **Hash reconferido:** `5CB921F03732277F`   **Confere:** sim
**LV:** LV3-V *(LV3-A bruto = `SEM FALA LEXICAL CONFIÁVEL`, 2 palavras, p = 0,595)*
**Cobertura da leitura:** ficha visual de 9 quadros (4%–92%) em `95` sob `H-M2-002`; ficha STT (7,7 s) em `TRANSCRICOES-BRUTAS-STT/02_.../AC-02-VID-001`. Binário não aberto por esta frente.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** AC-02-VID-001 · `H-M2-002` (relatório `95`) · `H-M3-001` (manifesto `117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Árvore de diretórios exibida em tela (`CLAUDE.md`, `.mcp.json`, `.claude/settings*.json`, `rules/`, `context/`, `commands/`, `skills/`, `agents/`, `hooks/`): exemplo isolado, não reprodutível — nenhum repositório ou arquivo acompanha (`95`) | — |
| E03 Maturidade | ND | — | Localizar o projeto real que a árvore retrata e inspecionar seu estágio |
| E05 Manutenção | ND | — | Localizar a publicação de origem com data |
| E06 Segurança ⚠ | ND | — | Inspecionar o conteúdo real de `hooks/` e `.claude/settings*.json` num projeto concreto — o vídeo os nomeia como guardrails sem mostrar regra |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos do material |
| E13 Testes/evals | ND | — | A árvore não inclui diretório de testes; resolveria inspecionar um projeto real com essa estrutura |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas (o que cada pasta serve); nenhum número decisivo em jogo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: define quais camadas de configuração existem e separa instruções globais, conexões, permissões, convenções, conhecimento durável, playbooks, especialistas e guardrails | — |
| E04 Transferibilidade | 3 | Taxonomia de pastas transferível com adaptação declarada; não depende de ambiente do autor | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto **dentro do acervo**: é a única peça que mapeia a estrutura de projeto inteira em um só quadro; AC-02-VID-013 cobre só o arquivo de instruções | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação; formato de consumo não declarado | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 7,3 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual em `95` + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 1** — item listado sob "Vídeos (NÃO são legíveis por IA — catalogados por título)", coluna "Assunto pelo título": descrição derivada do nome do arquivo (`anatomai de projeto.mp4` → "anatomia de um projeto"), sem indício de inspeção. Compatível com o conteúdo observado, mas compatibilidade não eleva a nota (§6, âncora 1).
**O que o catálogo afirma:** "`anatomai de projeto.mp4` | 7,7 MB | anatomia de um projeto"
**Confere com a fonte:** sim, em nível genérico

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "**Valor alto como taxonomia externa**, não como estrutura oficial." | `95` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | não |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 3` · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4 (o valor é a taxonomia em si, sem artefato externo nomeado).
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-02-VID-002 — `Data base scalling.mp4`

**Tipo:** VÍDEO · **Área:** 02_PROJETAR-ARQUITETURA
**Hash F0:** `5CDAFC52A550F07D`   **Hash reconferido:** `5CDAFC52A550F07D`   **Confere:** sim
**LV:** LV3-V *(LV3-A bruto = `SEM FALA LEXICAL CONFIÁVEL`, 1 palavra, p = 0,130)*
**Cobertura da leitura:** ficha visual de 9 quadros em `95` sob `H-M2-002`; ficha STT (9,0 s). Binário não aberto por esta frente.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** AC-02-VID-002 · `H-M2-002` (relatório `95`) · `H-M3-001` (manifesto `117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só listagem: dez técnicas nomeadas (indexing, vertical scaling, caching, sharding, replication, query optimization, connection pooling, vertical partitioning, denormalization, materialized views) sem exemplo, insumo ou medição (`95`) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e seu versionamento |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Nenhuma superfície inspecionada |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhum artefato testável associado |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas; nenhum número decisivo em jogo | — |

**NF = 1 · 2/7 · 5 ND** *(mediana de [1,3] = 2 → §14.3 vale o inferior: 1)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça a pergunta de forma genérica: é checklist de camada de dados, sem particularizar carga, consistência ou ordem de adoção | — |
| E04 Transferibilidade | 2 | O padrão (checklist de escala) transfere; a escolha depende de carga e operação não descritas | — |
| E14 Diferencial | 2 | Agregação de material público amplamente conhecido | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 7,1 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 1** — "Assunto pelo título" (`Data base scalling.mp4` → "escalabilidade de banco de dados"), sem indício de inspeção.
**O que o catálogo afirma:** "`Data base scalling.mp4` | 7,4 MB | escalabilidade de banco de dados"
**Confere com a fonte:** sim, em nível genérico

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| — nenhuma alegação numérica ou de autoridade identificada nos quadros | `95` | — | — |

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

### AC-02-VID-003 — `data structure.mp4`

**Tipo:** VÍDEO · **Área:** 02_PROJETAR-ARQUITETURA
**Hash F0:** `2EBE06451AE24AD0`   **Hash reconferido:** `2EBE06451AE24AD0`   **Confere:** sim
**LV:** LV3-V *(LV3-A bruto = `SEM FALA LEXICAL CONFIÁVEL`, 1 palavra, p = 0,130)*
**Cobertura da leitura:** ficha visual de 9 quadros em `95` sob `H-M2-002`; ficha STT (10,3 s). Binário não aberto por esta frente.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** AC-02-VID-003 · `H-M2-002` (relatório `95`) · `H-M3-001` (manifesto `117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só listagem: doze estruturas nomeadas (array, linked list, stack, hash map, matrix, queue, deque, binary tree, BST, heap, trie, graph), conteúdo introdutório sem artefato (`95`) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e seu versionamento |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Nenhuma superfície inspecionada |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhum artefato testável associado |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas; nenhum número decisivo em jogo | — |

**NF = 1 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 1 | Tangencia a área: é fundamento de programação, não decisão de camada ou de ordem de construção do sistema (`95`: "sem recomendação direta para o OS") | — |
| E04 Transferibilidade | 2 | O padrão (vocabulário de estruturas) transfere; nada implementável acompanha | — |
| E14 Diferencial | 1 | Conveniência sobre material amplamente acessível; sobrepõe AC-11-VID-002 e AC-11-VID-003 | — |

**RP = 1 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 9,4 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 1** — "Assunto pelo título" (`data structure.mp4` → "estruturas de dados"), sem indício de inspeção.
**O que o catálogo afirma:** "`data structure.mp4` | 9,9 MB | estruturas de dados"
**Confere com a fonte:** sim, em nível genérico

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| — nenhuma alegação numérica ou de autoridade identificada nos quadros | `95` | — | — |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 3` · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`. `E01 = 1` (≠ 0), portanto **não** cabe REJEITADO.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-02-VID-004 — `Desgin pattern.mp4`

**Tipo:** VÍDEO · **Área:** 02_PROJETAR-ARQUITETURA
**Hash F0:** `53B62E28ED2FE661`   **Hash reconferido:** `53B62E28ED2FE661`   **Confere:** sim
**LV:** LV3-V *(LV3-A bruto = `SEM FALA LEXICAL CONFIÁVEL`, 2 palavras, p = 0,572)*
**Cobertura da leitura:** ficha visual de 9 quadros em `95` sob `H-M2-002`; ficha STT (7,1 s). Binário não aberto por esta frente. Grafia do nome preservada.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** AC-02-VID-004 · `H-M2-002` (relatório `95`) · `H-M3-001` (manifesto `117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só listagem: quinze padrões nomeados (Singleton, Factory Method, Builder, Adapter, Decorator, Facade, Proxy, Composite, Observer, Strategy, Command, Iterator, State, Template Method, Chain of Responsibility) sem exemplo de código ou problema concreto (`95`) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e seu versionamento |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Nenhuma superfície inspecionada |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhum artefato testável associado |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas; nenhum número decisivo em jogo | — |

**NF = 1 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça a pergunta de forma genérica: fornece vocabulário de estruturação sem indicar camada nem ordem | — |
| E04 Transferibilidade | 2 | O padrão (catálogo de padrões) transfere; a implementação não acompanha | — |
| E14 Diferencial | 1 | Conveniência sobre material amplamente acessível | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 5,2 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 1** — "Assunto pelo título" (`Desgin pattern.mp4` → "padrões de projeto"), sem indício de inspeção.
**O que o catálogo afirma:** "`Desgin pattern.mp4` | 5,5 MB | padrões de projeto"
**Confere com a fonte:** sim, em nível genérico

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "evitar adoção por catálogo sem problema concreto" | `95` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | não |

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

### AC-02-VID-005 — `fundamentais.mp4`

**Tipo:** VÍDEO · **Área:** 02_PROJETAR-ARQUITETURA
**Hash F0:** `8357024D553AAE0F`   **Hash reconferido:** `8357024D553AAE0F`   **Confere:** sim
**LV:** LV3-V + LV3-A *(a combinação não produz LV4)*
**Cobertura da leitura:** ficha visual de 9 quadros em `95` sob `H-M2-002`; transcrição automática bruta integral (90,2 s, `pt`, 17 segmentos, p = 0,921, **ALTA AUTOMÁTICA**) em `TRANSCRICOES-BRUTAS-STT/02_.../AC-02-VID-005`. Sem revisão humana. Binário não aberto por esta frente.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** AC-02-VID-005 · `H-M2-002` (relatório `95`) · `H-M3-001` (manifesto `117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só narrativa: a fala provável apresenta um ranking de cinco padrões arquiteturais com justificativa oral, sem código, diagrama executável ou medição. Os quadros confirmam texto de Value Objects, Aggregates, Use Cases e CQRS; o primeiro item não ficou legível no visual, mas a fala provável o identifica como modularização | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e seu estágio |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Nenhuma superfície de risco inspecionada | 
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhum artefato testável associado |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas ("por isso que eu coloco ele em terceiro lugar"); a ordenação é declaradamente opinativa e nenhum número decisivo está em jogo | — |

**NF = 1 · 2/7 · 5 ND** *(mediana de [1,3] = 2 → §14.3 vale o inferior: 1)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: nomeia as unidades de decomposição do sistema — modularização, objetos de valor, agregados, casos de uso e CQRS — que são escolhas de camada | — |
| E04 Transferibilidade | 3 | Padrões transferíveis com adaptação declarada; independem de fornecedor e de ambiente do autor | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto **dentro do acervo**: é o único item que trata decomposição de domínio (DDD/CQRS) em vez de estrutura de pastas ou catálogo de ferramentas | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 86,4 MB — o maior vídeo do acervo | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT de 17 segmentos; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 1** — "Assunto pelo título" (`fundamentais.mp4` → "fundamentos de arquitetura"), sem indício de inspeção. O catálogo ainda registra: "`fundamentais.mp4` é o maior vídeo do acervo e provavelmente o mais denso. Nada dele está capturado em texto." — afirmação **superada**: o áudio foi transcrito (LV3-A) e os quadros revisados (LV3-V).
**O que o catálogo afirma:** "`fundamentais.mp4` | 91 MB | fundamentos de arquitetura"
**Confere com a fonte:** sim, em nível genérico. Divergência de tamanho (91 MB × 86,4 MB) consistente com conversão MiB→MB (D-09), não reaberta.

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Qual são as cinco melhores skills para um projeto?" | LV3-A bruto, 00:00:00–00:00:02 — **fala provável, não citação exata** | ALEGAÇÃO DO AUTOR | não |
| "Objetos de valor são os melhores lugares da tua aplicação para você colocar as regras de negócio" | LV3-A bruto, 00:00:37,600–00:00:43,600 — fala provável | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "é a parte de CQRS… vai simplificar muito a tua arquitetura" | LV3-A bruto, 00:00:53,900–00:01:00,400 — fala provável | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "Nada dele está capturado em texto." | `_CONTEUDO.md` área 02 | ALEGAÇÃO DO CATÁLOGO | **superada** pela entrega Codex (LV3-V + LV3-A) |

> O motor grafou "skills" onde o conteúdo trata de **padrões arquiteturais**, e "de plói" por "deploy". Nomes e termos não foram normalizados (`117`, regra de uso).

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 3` · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4 (o valor é o conteúdo conceitual, sem artefato externo nomeado a verificar).
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-02-VID-006 — `Gravando 2026-07-28 162144.mp4`

**Tipo:** VÍDEO · **Área:** 02_PROJETAR-ARQUITETURA
**Hash F0:** `E523AFC4EDDF0AA6`   **Hash reconferido:** `E523AFC4EDDF0AA6`   **Confere:** sim
**LV:** LV3-V + LV3-A *(a combinação não produz LV4)*
**Cobertura da leitura:** ficha visual de 9 quadros em `95` sob `H-M2-002`; transcrição automática bruta integral (47,9 s, `pt`, 13 segmentos, p = 0,876, **ALTA AUTOMÁTICA**). Sem revisão humana. Binário não aberto por esta frente.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** AC-02-VID-006 · `H-M2-002` (relatório `95`) · `H-M3-001` (manifesto `117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Demonstração isolada e não reprodutível: os quadros mostram projeto real, dashboard e código, e a fala provável cita OpenSpec e skills implementadas, mas nenhum arquivo, spec ou repositório acompanha o vídeo | — |
| E03 Maturidade | ND | — | Localizar o projeto e o OpenSpec demonstrados e inspecionar seu estágio |
| E05 Manutenção | ND | — | Localizar a publicação de origem com data |
| E06 Segurança ⚠ | ND | — | Inspecionar as skills e especificações reais que o vídeo exibe |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos do material e do OpenSpec citado |
| E13 Testes/evals | ND | — | Nenhum teste exibido; resolveria inspecionar o projeto demonstrado |
| E15 Alegações ⚠ | 1 | Alegação forte com fonte identificável mas não conferível com o material disponível: economia de créditos atribuída a encapsular trabalho em skills e specs (`95`), e "o resultado é simplesmente incrível" / "faz um diferençado absurdo" (LV3-A). Nenhum número exibido, mas a tese depende de um ganho não medido | — |

**NF = 1 · 2/7 · 5 ND** *(mediana de [1,2] = 1,5 → §14.3 vale o inferior)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: propõe que padrões de projeto sejam materializados como skills e que especificações encadeiem passos referenciando esses padrões — decisão de camada e de ordem | — |
| E04 Transferibilidade | 2 | O **padrão** (mapear padrões arquiteturais em skills; specs que referenciam skills) é transferível; a implementação depende do projeto e da ferramenta do autor | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto no acervo: liga padrão arquitetural a capacidade reutilizável, ponte que AC-02-VID-001 e AC-05-VID-005 não fazem | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 45,6 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT de 13 segmentos; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado ("Título pelo conteúdo visível") **e confirmado** pelos quadros e pela fala provável; o nome do arquivo não contém assunto (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 162144.mp4` | 45,6 MB | especificações antes do código com Claude Code | não transcrito" e "o primeiro aparenta defender geração/validação de especificações antes da implementação"
**Confere com a fonte:** sim — LV3-A confirma specs/OpenSpec como eixo do vídeo

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Tu já pensou em mapear os padrões de projetos da tua aplicação em skills?" | LV3-A bruto, 00:00:03,420–00:00:07,620 — **fala provável, não citação exata** | ALEGAÇÃO DO AUTOR | não |
| "E o resultado é simplesmente incrível." | LV3-A bruto, 00:00:16,660–00:00:18,660 — fala provável | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "juntando essas duas coisas, faz um diferençado absurdo" | LV3-A bruto, 00:00:37,780–00:00:41,700 — fala provável | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |

> O motor grafou "Cloud Code" por Claude Code. Nomes não normalizados (`117`).

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** §9 — relevância aparente (`E01 = 3`) com lacuna nomeada e endereçável; teto de V2/V4 respeitado.
**Se EXIGE PESQUISA — lacuna nomeada:** identidade, licença e conteúdo do "OpenSpec" exibido, e o ganho de crédito/token que a tese pressupõe.  **Verificação que a fecharia:** localizar a especificação do OpenSpec na origem pública e ler sua licença; medir localmente o consumo com e sem encapsulamento em skills, com tarefas definidas por esta casa.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-02-VID-007 — `Gravando 2026-07-28 162729.mp4`

**Tipo:** VÍDEO · **Área:** 02_PROJETAR-ARQUITETURA
**Hash F0:** `C3FC42F0EFF959D6`   **Hash reconferido:** `C3FC42F0EFF959D6`   **Confere:** sim
**LV:** LV3-V *(LV3-A bruto = `SEM FALA LEXICAL CONFIÁVEL`, 1 palavra, idioma detectado `km`, p = 0,781 — detecção de idioma improvável, registrada como ruído)*
**Cobertura da leitura:** ficha visual de 9 quadros em `95` sob `H-M2-002`; ficha STT (9,6 s). Binário não aberto por esta frente.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** AC-02-VID-007 · `H-M2-002` (relatório `95`) · `H-M3-001` (manifesto `117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só mapa: onze categorias nomeadas (LLM, Agentic AI, RAG, Embedding, MCP, AI Security, Observability, Memory, AI Agent, Automation, Vector Database) com marcas como exemplo, sem artefato ou critério de seleção (`95`) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e seu versionamento |
| E05 Manutenção | ND | — | Localizar o canal de origem com data — mapas de ecossistema envelhecem rápido |
| E06 Segurança ⚠ | ND | — | Nenhuma superfície inspecionada; "AI Security" é categoria retratada, não avaliada |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhum artefato testável associado |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas (pertencimento de marca a categoria); nenhum número decisivo. `95` registra: "marcas são exemplos, não endosso" | — |

**NF = 1 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: enumera as categorias de componente que compõem o sistema — é mapa de camadas, não de produtos | — |
| E04 Transferibilidade | 3 | O mapa de categorias transfere com adaptação declarada; as marcas, não | — |
| E14 Diferencial | 2 | Agregação de material público; sobrepõe AC-02-PRT-001 e AC-02-PRT-010 | — |

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
**NC = 5** — método declarado ("Título pelo conteúdo visível") **e confirmado** pelos quadros; o `_CONTEUDO.md` enumera as mesmas categorias observadas (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 162729.mp4` | 6,7 MB | mapa do ecossistema moderno de IA por camada" e "o segundo organiza LLM, Agentic AI, RAG, embeddings, MCP, segurança, observabilidade, memória e automação"
**Confere com a fonte:** sim — `95` lista as mesmas onze categorias

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "**Valor alto como mapa de categorias;** marcas são exemplos, não endosso." | `95` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | não |

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

### AC-02-VID-008 — `Gravando 2026-07-28 163313.mp4`

**Tipo:** VÍDEO · **Área:** 02_PROJETAR-ARQUITETURA
**Hash F0:** `C8F33826431AF318`   **Hash reconferido:** `C8F33826431AF318`   **Confere:** sim
**LV:** LV3-V *(LV3-A bruto = `SEM NARRAÇÃO CONFIÁVEL — EFEITO, MÚSICA OU ALUCINAÇÃO DO STT`, 3 palavras, p = 0,797)*
**Cobertura da leitura:** ficha visual de 9 quadros em `95` sob `H-M2-002`; ficha STT (4,5 s — o vídeo mais curto do acervo). Binário não aberto por esta frente.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** AC-02-VID-008 · `H-M2-002` (relatório `95`) · `H-M3-001` (manifesto `117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Comparação de responsabilidades exibida em tela — load balancer (distribuição, health check, failover, sticky sessions), reverse proxy (TLS, cache, compressão, URL rewriting), API gateway (autenticação, rate limit, agregação, roteamento) —, isolada e sem configuração ou medição (`95`) | — |
| E03 Maturidade | ND | — | Identificar a publicação de origem e seu versionamento |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | Nenhuma superfície inspecionada; TLS, autenticação e rate limit aparecem como rótulos, não como controle verificado |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | Nenhum artefato testável associado |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas (atribuição de função a componente); nenhum número decisivo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: separa três camadas de borda que costumam ser confundidas, decisão de arquitetura | — |
| E04 Transferibilidade | 3 | Separação de responsabilidades transferível com adaptação declarada; independe de fornecedor | — |
| E14 Diferencial | 2 | Agregação de material público amplamente conhecido | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 2,6 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado ("Título pelo conteúdo visível") **e confirmado** pelos quadros; o `_CONTEUDO.md` descreve as três funções observadas (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 163313.mp4` | 2,6 MB | load balancer × reverse proxy × API gateway" e "o terceiro separa distribuição de carga, porta de entrada dos servidores e roteamento/autenticação de serviços"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| — nenhuma alegação numérica identificada; o STT registrou 3 palavras classificadas como efeito/música, não narração | `117` · `95` | — | — |

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

### AC-02-VID-009 — `Gravando 2026-07-28 204335.mp4`

**Tipo:** VÍDEO · **Área:** 02_PROJETAR-ARQUITETURA
**Hash F0:** `FC4086F4B3102370`   **Hash reconferido:** `FC4086F4B3102370`   **Confere:** sim
**LV:** LV3-V *(LV3-A bruto = `SEM FALA LEXICAL CONFIÁVEL`, 1 palavra, p = 0,751)*
**Cobertura da leitura:** ficha visual de 9 quadros em `95` sob `H-M2-002`; ficha STT (6,9 s). Binário não aberto por esta frente.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** AC-02-VID-009 · `H-M2-002` (relatório `95`) · `H-M3-001` (manifesto `117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só divulgação: carrossel que propõe "PAUL" como framework construtor de dashboard-OS com Graphify + Obsidian, exibindo comandos (`init`, `plan`, `apply`, `verify`, `help/status`) sem repositório, código ou execução inspecionável (`95`) | — |
| E03 Maturidade | ND | — | Identificar o repositório de "PAUL"/"Charlie OS" e inspecionar seu estágio |
| E05 Manutenção | ND | — | Localizar o repositório de origem e verificar atividade datada |
| E06 Segurança ⚠ | ND | — | **Superfície declarada e não inspecionada**: execução local ou em Railway, empacotamento em repositório clonável e comando `apply`. Resolveria inspecionar código, credenciais exigidas e isolamento |
| E07 Licença ⚠ | ND | — | Identificar o repositório e ler o texto da licença |
| E13 Testes/evals | ND | — | O comando `verify` é exibido, mas nenhum teste; resolveria inspecionar o repositório |
| E15 Alegações ⚠ | 1 | Alegações fortes sobre capacidade ("framework construtor de dashboard OS") com fonte nominalmente citada (PAUL / Graphify) porém **não identificável** com o material disponível — `95` classifica o item como "candidato em quarentena" | — |

**NF = 1 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: propõe a forma inteira do sistema — grafo de conhecimento como "brain" mais dashboard operacional, com ciclo `init → plan → apply → verify` | — |
| E04 Transferibilidade | 2 | O **padrão** (ciclo declarativo sobre um grafo) é transferível; a implementação depende de produto não identificado e de execução local ou em Railway | — |
| E14 Diferencial | 2 | Agregação: converge com AC-02-VID-011, AC-04-VID-008 e AC-04-VID-012 dentro do próprio acervo, formando um mesmo cluster | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 2,1 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado ("Título pelo conteúdo visível") **e confirmado** pelos quadros (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 204335.mp4` | 2,1 MB | PAUL: sistema operacional pessoal com IA | não transcrito"
**Confere com a fonte:** sim — `95` descreve o mesmo conteúdo

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "PAUL como framework construtor de dashboard OS" | `95` (texto visual observado) | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "**Candidato em quarentena:** identidade, repositório, licença, código, credenciais e isolamento precisam ser descobertos antes de qualquer avaliação." | `95` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | não |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** §9 — relevância aparente com lacuna nomeada e endereçável; teto de V2/V4 respeitado.
**Se EXIGE PESQUISA — lacuna nomeada:** identidade inequívoca de "PAUL" / "Charlie OS" / "Graphify" — repositório, licença, credenciais exigidas e modelo de execução.  **Verificação que a fecharia:** localizar o repositório público de cada nome, ler licença e README, e mapear as permissões que o comando `apply` exige — sem clonar nem executar.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-02-VID-010 — `Gravando 2026-07-28 214021.mp4`

**Tipo:** VÍDEO · **Área:** 02_PROJETAR-ARQUITETURA
**Hash F0:** `AA4EA39A4E8A8466`   **Hash reconferido:** `AA4EA39A4E8A8466`   **Confere:** sim
**LV:** LV3-V + LV3-A *(a combinação não produz LV4)*
**Cobertura da leitura:** ficha visual de 9 quadros em `95` sob `H-M2-002`; transcrição automática bruta integral (57,9 s, `pt`, 16 segmentos, p = 0,886, **ALTA AUTOMÁTICA**). Sem revisão humana. Binário não aberto por esta frente.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** AC-02-VID-010 · `H-M2-002` (relatório `95`) · `H-M3-001` (manifesto `117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Diagrama exibido em tela decompondo o harness em guias/feedforward (`AGENTS.md`, specs/tasks, arquitetura, convenções), memória/bootstrap (`init.sh`, `progress.md`, disciplina Git) e sensores/feedback (linters, type checkers, testes/E2E, agente revisor); a fala provável desenvolve a analogia de controle. Exemplo isolado — nenhum repositório ou arquivo acompanha | — |
| E03 Maturidade | ND | — | Localizar o projeto real que o diagrama retrata e inspecionar seu estágio |
| E05 Manutenção | ND | — | Localizar a publicação de origem com data |
| E06 Segurança ⚠ | ND | — | Nenhuma superfície inspecionada; "review agents" e `init.sh` são citados, não inspecionados |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | O diagrama **nomeia** testes, linters e type checkers como sensores, mas nenhum é exibido ou executável; resolveria inspecionar o projeto retratado |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas; nenhum número decisivo em jogo — a fala provável não apresenta cifras | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: separa o modelo do sistema de trabalho que o cerca e nomeia as duas malhas de controle — antecipação e correção | — |
| E04 Transferibilidade | 3 | O padrão feedforward/feedback é transferível com adaptação declarada; independe de fornecedor e de linguagem | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto **dentro do acervo**: é a formulação mais explícita da tese "desempenho depende do harness, não só do modelo", que os demais itens só tocam de lado | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 5,5 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT de 16 segmentos; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado ("Título pelo conteúdo visível") **e confirmado** por duas evidências: os quadros (`95`) e a fala provável, que reproduz a mesma separação descrita pelo catálogo (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-28 214021.mp4` | 5,5 MB | agente = modelo + harness: anatomia de um sistema agêntico | não transcrito" e "o diagrama “modelo + harness” separa o LLM de especificações, convenções, memória, ferramentas, testes, linters e agentes de revisão"
**Confere com a fonte:** sim — LV3-A bruto 00:00:29–00:00:36 confirma os sensores nomeados

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "o primeiro é o Feedforward, onde tu dá instruções antes da execução para aumentar a chance de dar certo. É preventivo." | LV3-A bruto, 00:00:00–00:00:09 — **fala provável, não citação exata** | ALEGAÇÃO DO AUTOR | não |
| "No nosso mundo são os linters, os testes, os type checkers, o review agents, tudo o que detecta um erro e permite autocorreção." | LV3-A bruto, 00:00:29,000–00:00:36,320 — fala provável | ALEGAÇÃO DO AUTOR | não |
| "Se tivesse só a rota, tu ia te perder no primeiro erro. Só com o recalculo, tu sai sem direção nenhuma, então tu precisa dos dois" | LV3-A bruto, 00:00:47,000–00:00:54,440 — fala provável | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "**Achado central:** desempenho do agente depende do sistema de trabalho, não só do modelo." | `95` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | não |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 3` · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4 (o valor é o padrão de controle em si; não há artefato externo nomeado cuja verificação mude o que o item vale).
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-02-VID-011 — `Gravando 2026-07-29 090647.mp4`

**Tipo:** VÍDEO · **Área:** 02_PROJETAR-ARQUITETURA
**Hash F0:** `7396803D345736D6`   **Hash reconferido:** `7396803D345736D6`   **Confere:** sim
**LV:** LV3-V *(LV3-A bruto = `SEM FALA LEXICAL CONFIÁVEL`, 1 palavra, p = 0,130)*
**Cobertura da leitura:** ficha visual de 9 quadros em `95` sob `H-M2-002`; ficha STT (13,1 s). Binário não aberto por esta frente.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** AC-02-VID-011 · `H-M2-002` (relatório `95`) · `H-M3-001` (manifesto `117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | Só divulgação: mesma família de AC-02-VID-009 — Graphify + Obsidian como "brain" e PAUL como construtor —, sem repositório, código ou execução inspecionável (`95` trata os dois como carrosséis relacionados) | — |
| E03 Maturidade | ND | — | Identificar os repositórios de Graphify e PAUL e inspecionar seu estágio |
| E05 Manutenção | ND | — | Localizar os repositórios de origem e verificar atividade datada |
| E06 Segurança ⚠ | ND | — | **Superfície declarada e não inspecionada**: agente com acesso a um vault pessoal e execução em serviço externo. Resolveria inspecionar código, escopos e credenciais |
| E07 Licença ⚠ | ND | — | Identificar os repositórios e ler o texto das licenças |
| E13 Testes/evals | ND | — | Nenhum teste exibido |
| E15 Alegações ⚠ | 1 | Alegações fortes de capacidade com fontes nominalmente citadas (Graphify, PAUL, Obsidian) porém não identificáveis com o material disponível | — |

**NF = 1 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça a pergunta de forma genérica: propõe uma pilha (grafo + vault + construtor) sem particularizar camadas ou ordem de construção | — |
| E04 Transferibilidade | 2 | O padrão transfere; a implementação depende de produtos não identificados | — |
| E14 Diferencial | 1 | Conveniência: é reapresentação do mesmo material de AC-02-VID-009, com sobreposição adicional a AC-04-VID-008 | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 7,7 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — método declarado ("Título pelo conteúdo visível") **e confirmado** pelos quadros (`04` §6.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-29 090647.mp4` | 7,7 MB | Graphify + Obsidian + PAUL como sistema operacional pessoal | não transcrito"
**Confere com a fonte:** sim — `95` descreve os mesmos três nomes

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "propõem Graphify + Obsidian como “brain”, PAUL como framework construtor de dashboard OS, execução local ou em Railway e empacotamento em um repositório clonável" | `95` (texto visual observado) | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** §9 — relevância aparente com lacuna nomeada e endereçável; teto de V2/V4 respeitado.
**Se EXIGE PESQUISA — lacuna nomeada:** identidade, repositório e licença de "Graphify" e "PAUL"; escopos de acesso que o agente exigiria sobre o vault.  **Verificação que a fecharia:** localizar os repositórios públicos, ler licença e README, e mapear permissões — sem clonar nem executar. Mesma lacuna de AC-02-VID-009, contada uma vez.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-02-VID-012 — `Gravando 2026-07-29 091319.mp4`

**Tipo:** VÍDEO · **Área:** 02_PROJETAR-ARQUITETURA
**Hash F0:** `ECF9BF67DE98F5A3`   **Hash reconferido:** `ECF9BF67DE98F5A3`   **Confere:** sim
**LV:** LV3-V + LV3-A *(a combinação não produz LV4)*
**Cobertura da leitura:** ficha visual de 9 quadros em `95` sob `H-M2-002`; transcrição automática bruta integral (59,2 s, `pt`, 21 segmentos, p = 0,885, **ALTA AUTOMÁTICA**). Sem revisão humana. Binário não aberto por esta frente.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** AC-02-VID-012 · `H-M2-002` (relatório `95`) · `H-M3-001` (manifesto `117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Demonstração isolada: os quadros contrastam prompt avulso com arquivo de instruções persistentes e exibem regras de legibilidade, padrões, testes, documentação, proteção de segredos, exceções, segurança e qualidade; a fala provável descreve o mesmo. Nenhum arquivo real acompanha | — |
| E03 Maturidade | ND | — | Localizar o projeto retratado e inspecionar seu estágio |
| E05 Manutenção | ND | — | Localizar a publicação de origem com data |
| E06 Segurança ⚠ | ND | — | O material **cita** "proteção de segredos" como regra, mas nenhuma superfície foi inspecionada; resolveria inspecionar um arquivo de instruções real |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | "Testes" aparece como categoria de regra, não como suíte; resolveria inspecionar o projeto retratado |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas; nenhum número decisivo em jogo | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: define a camada de conhecimento persistente do projeto e o que ela deve conter | — |
| E04 Transferibilidade | 3 | Transferível com adaptação declarada; a lista de blocos independe de fornecedor | — |
| E14 Diferencial | 2 | Agregação: sobrepõe AC-02-VID-013, AC-03-VID-011 e AC-04-VID-010 dentro do acervo | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): sem instalação | — |
| E09 Custo | 5 | Sem custo recorrente; MP4 local de 41,3 MB | — |
| E10 Contexto/tokens | 4 | Evidência derivada = ficha visual + ficha STT de 21 segmentos; < 1 MB | — |
| E11 Fornecedor | 5 | MP4, container aberto | — |
| E12 Reversibilidade | 4 | Consulta sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 0** — **DIVERGENTE.** O catálogo descreve este ID como "Claude Code cria aplicação full-stack e escolhe a pilha", detalhando "React/Next/TypeScript/Tailwind, Node/Nest/Express, GraphQL/Prisma e infraestrutura de deploy". A fonte — quadros (`95`) e fala provável integral — trata de **instruções persistentes em arquivo de projeto**, sem qualquer construção full-stack ou escolha de pilha. A fonte prevalece (`05` §5.1.5).
**O que o catálogo afirma:** "`Gravando 2026-07-29 091319.mp4` | 41,3 MB | Claude Code cria aplicação full-stack e escolhe a pilha | não transcrito"
**Confere com a fonte:** **não** — divergência registrada

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Você acha que o segredo do Calde é escrever prontos melhores? Não é. O segredo está nessa pasta." | LV3-A bruto, 00:00:00–00:00:07 — **fala provável, não citação exata** | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "Eles criam uma base de conhecimento por projeto." | LV3-A bruto, 00:00:22,140–00:00:24,620 — fala provável | ALEGAÇÃO DO AUTOR | não |
| "quem domina a AI não perde tempo criando prompts de goods. Primeiro, organiza o conhecimento e depois deixa a AI trabalhar." | LV3-A bruto, 00:00:50,540–00:00:58,580 — fala provável | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "Claude Code cria aplicação full-stack e escolhe a pilha" | `_CONTEUDO.md` área 02 | ALEGAÇÃO DO CATÁLOGO | **contradita pela fonte** → `NC = 0` |

> O motor grafou "Calde", "Calda Converse" e "Calde AMD" por Claude e `CLAUDE.md`. Não normalizado (`117`).

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 3` · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4. `NC = 0` é achado sobre o catálogo, **não** rebaixa a fonte (`04` §6.1.4).
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-02-VID-013 — `verificar arquitetura.mp4`

**Tipo:** VÍDEO · **Área:** 02_PROJETAR-ARQUITETURA
**Hash F0:** `88FA51513F9BABE9`   **Hash reconferido:** `88FA51513F9BABE9`   **Confere:** sim
**LV:** LV3-V *(LV3-A bruto = `SEM FALA LEXICAL CONFIÁVEL`, 2 palavras, p = 0,587)*
**Cobertura da leitura:** ficha visual de 9 quadros em `95` sob `H-M2-002`; ficha STT (9,3 s). Binário não aberto por esta frente.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)
**Origem Codex:** AC-02-VID-013 · `H-M2-002` (relatório `95`) · `H-M3-001` (manifesto `117`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Rubrica exibida em tela: dez blocos de um arquivo de instruções (Project overview, Tech stack, Commands, Architecture, Code conventions, Testing, Git & PR rules, Do not touch, Gotchas, imports) mais três regras de forma — menos de 500 linhas, instruções em vez de prosa, atualizar quando estiver errado. Exemplo isolado, sem arquivo real (`95`) | — |
| E03 Maturidade | ND | — | Localizar a publicação de origem e seu versionamento |
| E05 Manutenção | ND | — | Localizar o canal de origem com data |
| E06 Segurança ⚠ | ND | — | O bloco "Do not touch" é uma regra retratada, não um controle inspecionado |
| E07 Licença ⚠ | ND | — | Identificar autoria e termos |
| E13 Testes/evals | ND | — | "Testing" aparece como seção do documento, não como suíte; resolveria inspecionar um arquivo real |
| E15 Alegações ⚠ | 2 | Alegação numérica com fonte citada e **conferível**, ainda não conferida: o limite de "menos de 500 linhas" é uma regra de forma verificável em qualquer arquivo real, mas nenhum foi inspecionado | — |

**NF = 2 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: define o conteúdo e o limite de tamanho da camada de instruções persistentes | — |
| E04 Transferibilidade | 3 | Rubrica transferível com adaptação declarada; independe de fornecedor | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto **dentro do acervo**: é o único item que dá **critério de concisão e manutenção** ao arquivo de instruções, e não apenas sua lista de seções | — |

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
**NC = 1** — "Assunto pelo título" (`verificar arquitetura.mp4` → "como verificar uma arquitetura"), sem indício de inspeção. A descrição é, além disso, **imprecisa**: o conteúdo observado é a anatomia e a rubrica de um arquivo de instruções, não um método de verificação de arquitetura. Permanece 1 (âncora de descrição derivada do nome), com a imprecisão registrada.
**O que o catálogo afirma:** "`verificar arquitetura.mp4` | 9,4 MB | como verificar uma arquitetura"
**Confere com a fonte:** parcialmente — o vídeo trata de rubrica de documento de instruções

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Recomenda menos de 500 linhas, instruções em vez de prosa, especificidade e atualização quando estiver errado." | `95` (texto visual observado) | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA`, porém **conferível** |
| "**Valor alto como rubrica de concisão e manutenção.**" | `95` (avaliação da trilha Codex) | ALEGAÇÃO DO CATÁLOGO (trilha paralela) | não |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 2` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — insumo de consulta com `LV ≥ 3`; critério §3.4 (o valor é a rubrica em si).
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

## Fechamento da área 02

| Métrica | Valor |
|---|---:|
| Itens representados | 24 / 24 |
| Fichas válidas contra `04` §13 | 24 |
| Hashes / estruturas reconferidos · divergentes | 24 · **0** |
| `RF = REFERÊNCIA` | 19 |
| `RF = EXIGE PESQUISA` | 5 (AC-02-REP-001, AC-02-PRT-005, AC-02-VID-006, AC-02-VID-009, AC-02-VID-011) |
| `RF = INDETERMINADO` | 0 |
| Total de eixos possíveis (24 × 15) | 360 |
| Eixos determinados | 243 |
| Eixos em `ND` | **117 (32,5%)** *(recontado por ferramenta sobre as fichas em 2026-07-29; o valor anterior, 115, era estimativa e foi corrigido — ver `99_RELATORIO-DA-FASE-2.md` §6)* |
| Único item em LV4 | AC-02-REP-001 |
| Divergências catálogo × fonte | **1 divergente** (AC-02-VID-012, `NC = 0`) · 1 parcial (AC-02-PRT-010) · 1 alegação de acervo contradita (AC-02-REP-001) |

Nenhuma fonte foi modificada. Nenhum item foi adotado, ordenado, priorizado ou recomendado.
