> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

# FICHAS DE EVIDÊNCIA — ÁREA 10 — APLICAÇÕES DE NEGÓCIO

**Fase:** 2 — Extração · **Data:** 2026-07-29 · **Avaliador:** Claude Opus 5 (Fase 2)
**Itens:** 46 — 6 REPO · 16 PRINT · 23 VÍDEO · **1 PLANILHA** — **é a maior área do acervo**
**Convenções de aplicação:** `00_INDICE-DA-FASE-2.md` §3
**Lotes:** L-22 (6 REPO + 1 PLANILHA) · L-23 (16 PRINT) · L-24 (VÍDEO 001–012) · L-25 (VÍDEO 013–023)

**Pergunta central da área (base de E01):** *que verticais provar primeiro, e como um sistema de agentes é empacotado por domínio.*

> **Caso particular registrado antes de qualquer nota.** `AC-10-REP-006` é **possível duplicata** de `AC-10-REP-005` — `05` §10 mede **81,5 % dos arquivos** e **17/17 skills**. Recebe **ficha do delta apenas**; o restante herda. `AC-10-VID-014` é o item que o índice do acervo chamou de "candidato a descarte": **não descartado** — `05` §10 é explícito, a sinalização é alegação do catálogo.

---

### AC-10-REP-001 — `claude-for-legal-main`

**Tipo:** REPO · **Área:** 10_APLICACOES-DE-NEGOCIO
**Hash F0:** `dir · 315 arq.`   **Hash reconferido:** `315 arq. · aninhamento 0`   **Confere:** sim
**LV:** LV4
**Cobertura da leitura:** raiz efetiva `claude-for-legal-main` (profundidade 0; 26 entradas); `LICENSE` — Apache License 2.0, 11.358 bytes, íntegro; `README.md` (**53.485 bytes** — o maior do acervo; lidos 6 KB: proposta, os dois destinos de instalação e parte da tabela de agentes por nome de cargo); `.claude-plugin/` (`marketplace.json`); presença de `QUICKSTART.md`, `CLA.md`, `CONNECTORS.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `CLAUDE.md`, `references/`, `managed-agent-cookbooks/`, `external_plugins/` e **onze diretórios de domínio jurídico**; **buscados e ausentes na raiz efetiva: `SECURITY.md`, `CHANGELOG`, `VERSION`, diretório de testes**. **Não lidos:** os diretórios de domínio, `references/`, `scripts/`, `marketplace.json`.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** não se aplica

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 3 | Artefato completo e inspecionável — onze domínios jurídicos empacotados, cada um com agentes nomeados por cargo, mais cadernos de agente gerenciado e referências —, **sem** procedimento de verificação declarado na raiz | — |
| E03 Maturidade | 2 | Funciona no cenário demonstrado (`QUICKSTART.md` promete instalação em 60 segundos), **sem versionamento identificável**: procurados e ausentes `CHANGELOG`, `VERSION` e `package.json`. **Resolvível com uma leitura**: `.claude-plugin/marketplace.json` pode conter versão e não foi aberto | — |
| E05 Manutenção | ND | — | Nenhuma evidência datada dentro da fonte. Resolveria consultar commits e releases na origem pública |
| E06 Segurança ⚠ | 2 | **Superfície ampla sem controle documentado na raiz**: `CONNECTORS.md` declara conectores de dados, e o material trata de contrato, litígio, privacidade e regulação — dado sensível por definição. **Procurados e ausentes: `SECURITY.md`, escopo de permissão, política de retenção.** O portão de revisão humana que o catálogo atribui ao item **não foi observado** no trecho lido | — |
| E07 Licença ⚠ | 4 | Permissiva padrão presente e íntegra: Apache License 2.0, 11.358 bytes. Cópia local não prova titularidade → teto 4 | — |
| E13 Testes/evals | ND | — | Não há diretório de testes **na raiz efetiva**; não foi inspecionado o interior dos onze diretórios de domínio. Resolveria listá-los |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas, nenhum número decisivo em jogo: "the legal workflows we see most", "install in 60 seconds". A proposta do item é o próprio artefato, não um resultado medido | — |

**NF = 3 · 5/7 · 2 ND** *(mediana dos determinados [2,2,3,3,4] = 3)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 4 | Endereça diretamente a pergunta central **mais** artefato concreto: é um **exemplo executável de empacotamento por domínio**, que é metade da pergunta da área | — |
| E04 Transferibilidade | 4 | Transferível por configuração, sem alteração de código: o README declara **uma fonte e dois destinos** — plugin ou agente gerenciado por API, mesmo prompt e mesmas skills | — |
| E14 Diferencial | 4 | Sem equivalente no acervo **mais** custo alto de reconstrução: onze domínios com agentes nomeados por cargo, cadernos de agente gerenciado e conectores declarados não se refazem por descrição | — |

**RP = 4 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 4 | Instalação declarada em um comando, com guia de partida dedicado | — |
| E09 Custo | 4 | Custo marginal: Apache-2.0, sem serviço próprio; o custo é a inferência dos agentes | — |
| E10 Contexto/tokens | 2 | Medido: **315 arquivos, 3 MB** — contagem na faixa 300–1.000; o tamanho sozinho daria 4 | — |
| E11 Fornecedor | 2 | **Dependência declarada de um fornecedor**: os dois destinos de instalação são produtos do mesmo fabricante. A abstração não é oferecida — é o oposto do que faz `AC-10-REP-004` | — |
| E12 Reversibilidade | 4 | Reversível por remoção: o artefato é conteúdo de plugin | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (os nomes de cargo dos agentes, o padrão de uma fonte e dois destinos, a entrevista de partida a frio gravada em arquivo de perfil, o plugin autocontido, o portão antes do irreversível, os agentes agendados) e o detalhe **confere** no que foi lido: os nomes de cargo e o duplo destino estão no README. **Os itens 2, 4 e 5 do catálogo não foram observados** sob o teto de leitura — não estão negados, estão fora da cobertura.
**O que o catálogo afirma:** "São repositórios de referência da própria Anthropic… **Uma fonte, dois destinos**… **Entrevista de partida a frio**… **Portão explícito antes de qualquer coisa irreversível** — toda saída é rascunho para revisão humana… **O que extrair:** o item 2 é o mais transferível."
**Confere com a fonte:** sim, no que foi lido

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Reference agents, skills, and data connectors for **the legal workflows we see most**" | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| "repositórios de referência da **própria Anthropic**" | `_CONTEUDO.md` área 10 | ALEGAÇÃO DO CATÁLOGO — atribuição de origem | **não observada na fonte** sob o teto de leitura; os links do README apontam para produtos da empresa, o que é indício, não declaração de autoria |
| "toda saída é rascunho para revisão humana, com atribuição de fonte em cada citação" | `_CONTEUDO.md` área 10 | ALEGAÇÃO DO CATÁLOGO — **controle de segurança** | **não observada** aqui; **observada literalmente** em `AC-10-REP-003`, que é o repositório irmão — o que torna a alegação plausível e ainda assim não verificada para este item |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V2 · V3 · V4 · V5 · V6 · V7 · V8 | **nenhuma** | `E06 = 2` — **nem 0, nem 1, nem ND**, portanto V1 e V2 não disparam · `E07 = 4` · `LV = 4` · 2 ND · `E15 = 3` · reconferência confere |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** §9 — **nenhuma porta de veto disparou**; a classificação é fechada pelas condições de entrada. CANDIDATO FORTE exige "nenhum eixo do Bloco A abaixo de 3" e `E06 = 2`; CANDIDATO A PILOTO exige `E06 ≥ 3`. PADRÃO A ESTUDAR também caberia (`E04 = 4` com `E03 = 2` e `E05 = ND`) — **nova ocorrência de DEF-13**; prevaleceu EXIGE PESQUISA pelo critério §3.4, porque o valor está no artefato e há verificação nomeada.
**Se EXIGE PESQUISA — lacuna nomeada:** duas: (1) **superfície de segurança** — um pacote que conecta dados jurídicos sem política de segurança nem escopo de permissão na raiz; (2) **verificação** — nenhum teste localizado, e o portão de revisão humana atribuído pelo catálogo não foi observado.  **Verificação que a fecharia:** ler `CONNECTORS.md` e o `README` de um dos domínios até o ponto em que descrevem permissão e revisão humana, e listar os onze diretórios procurando teste — leitura curta e sem execução.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-10-REP-002 — `claude-seo-main`

**Tipo:** REPO · **Área:** 10_APLICACOES-DE-NEGOCIO
**Hash F0:** `dir · 364 arq.`   **Hash reconferido:** `364 arq. · aninhamento 0`   **Confere:** sim
**LV:** LV4
**Cobertura da leitura:** raiz efetiva `claude-seo-main` (profundidade 0; 33 entradas); `LICENSE` — MIT, 1.069 bytes, "Copyright (c) 2026 agricidaniel", íntegro; `README.md` (37.501 bytes, lidos 6 KB); **`CHANGELOG.md` — entrada `[2.2.0] - 2026-06-12` lida por inteiro**, descrita pelo autor como "Security, cross-platform, and data-accuracy release"; listagem de `tests/` com nomes por risco; presença de `SECURITY.md`, `PRIVACY.md`, `CITATION.cff`, `install.sh`/`install.ps1`, `uninstall.sh`/`uninstall.ps1`, `.devcontainer/`, `hooks/`, `schema/`, `pdf/`, `agents/`, `skills/`. **Não lidos:** `src`/`skills/`, `agents/`, `docs/`, `SECURITY.md`, `PRIVACY.md`.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** não se aplica

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 4 | Artefato completo **mais** procedimento de verificação declarado e **nomeado por risco**: `tests/` inclui `test_extension_installer_injection.py`, `test_google_api_key_safety.py`, `test_manifest_consistency.py`, `test_drift_portability.py` e `test_google_report_full_audit.py` — teste que existe porque uma falha existiu | — |
| E03 Maturidade | 4 | Versionado com release identificável (`CHANGELOG.md`, versão `2.2.0` datada, `CITATION.cff`) **mais** documentação de instalação e uso (`docs/`, instaladores e **desinstaladores** para dois sistemas, `.devcontainer/`) **mais** tratamento de erro visível — o changelog descreve correções de borda com caso e reprodução | — |
| E05 Manutenção | **4** | **Atividade recente datada dentro da fonte** — `2026-06-12`, seis semanas antes desta avaliação — **mais responsável nomeado** (titular do aviso de copyright) **mais canal de reporte declarado e em uso**: o changelog credita relatores externos por número de questão e por identificador de usuário. Não alcança 5: nenhuma política de suporte ou de versões foi lida | — |
| E06 Segurança ⚠ | 4 | **Superfície delimitada, controles documentados e escopo explícito**: `SECURITY.md`, `PRIVACY.md`, e um release de segurança que corrige **injeção de credencial no instalador**, **desvio de validação de URL por confusão de autoridade**, **vazamento de chave de API em URL** — movida para cabeçalho com saída redigida — e adiciona **portão de varredura de segredo na integração contínua**. Não alcança 5 apenas porque `SECURITY.md` e o resultado da auditoria citada não foram lidos por esta frente | — |
| E07 Licença ⚠ | 4 | Permissiva padrão presente e íntegra: MIT, 1.069 bytes, titular nomeado. Cópia local não prova titularidade → teto 4 | — |
| E13 Testes/evals | 4 | Suíte executável identificável **mais** verificação de comportamento e de regressão de segurança, com auditoria de relatório completo entre os testes. Não alcança 5: nenhum resultado publicado foi lido | — |
| E15 Alegações ⚠ | 2 | Alegações numéricas **conferíveis dentro da própria fonte, ainda não conferidas**: "25 sub-skills", "18 specialist agents", "até 15 agentes simultâneos". Contáveis em `skills/` e `agents/`, não contadas sob o teto de leitura | — |

**NF = 4 · 7/7 · 0 ND** *(mediana de [2,4,4,4,4,4,4] = 4)*

> **Segundo item do acervo com Bloco A integralmente determinado.** O primeiro é `AC-08-REP-003`. Os dois têm a mesma causa: licença, changelog datado e testes na própria fonte.

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 4 | Endereça diretamente a pergunta central **mais** artefato: é uma vertical inteira empacotada, com execução paralela declarada | — |
| E04 Transferibilidade | 4 | Transferível por configuração: instalador para dois sistemas, plugin, desinstalador | — |
| E14 Diferencial | 4 | Sem equivalente no acervo **mais** custo alto de reconstrução — e o diferencial **não é o domínio**: é a metodologia de saída que o catálogo destaca, em que cada recomendação carrega a observação de primeiro princípio, as dependências, uma checagem de **"como saberíamos que isto falhou?"** e um indicador antecedente. Falseabilidade embutida na saída do agente é o padrão mais raro do acervo | — |

**RP = 4 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 4 | Instalação declarada em um comando por sistema, com contêiner de desenvolvimento e desinstalador | — |
| E09 Custo | 3 | **Custo recorrente previsível e mensurável**: até 15 agentes simultâneos por auditoria, mais serviços externos de dados de SEO cujos instaladores o changelog cita nominalmente. Não é licença — é inferência e API de terceiro | — |
| E10 Contexto/tokens | 2 | Medido: **364 arquivos, 3,8 MB** — contagem na faixa 300–1.000 | — |
| E11 Fornecedor | 3 | Abstração parcial: o plugin é de um harness específico, e a coleta depende de provedores externos de dados nomeados | — |
| E12 Reversibilidade | 4 | Reversível por remoção **com desinstalador próprio para dois sistemas** — raro no acervo e verificável na listagem da raiz | — |

**AA = 3 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (25 sub-skills, 18 agentes, até 15 simultâneos, as sete frentes de SEO cobertas, e a metodologia de quatro partes na saída) e o detalhe **confere** com o README lido. O catálogo identifica corretamente qual é o valor arquitetural do item, e não o domínio.
**O que o catálogo afirma:** "25 sub-skills e 18 agentes especialistas rodando em paralelo — auditoria de site inteiro dispara **até 15 agentes simultâneos**… **O que extrair — e este é o item mais importante da pasta para arquitetura:** a metodologia declarada… uma checagem explícita de *'como saberíamos que isto falhou?'*… Isso é falseabilidade embutida na saída do agente."
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "It runs **25 sub-skills** and **18 specialist agents** in parallel" | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — **conferível dentro da fonte**, não conferida |
| "**Installer credential injection (blocker).** … Credentials now pass as `argv` through a quoted heredoc, and the settings file is written atomically with `0600` permissions." | `CHANGELOG.md` da fonte | **FATO OBSERVADO** — o autor documenta uma falha própria e a correção | sim, como registro; a eficácia da correção não foi verificada |
| "Found by an independent audit." | `CHANGELOG.md` da fonte | ALEGAÇÃO DO AUTOR — auditoria externa | **não** — a auditoria não é nomeada nem publicada no trecho lido; é o que separa `E06 = 4` de `E06 = 5` |
| "Verified against the full history and tracked tree: no real secret present." | `CHANGELOG.md` da fonte | ALEGAÇÃO DO AUTOR — resultado de varredura | não — não reproduzida por esta frente |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V2 · V3 · V4 · V5 · V6 · V7 · V8 | **nenhuma** | `E06 = 4` · `E07 = 4` · `LV = 4` · **0 ND** · `E15 = 2` (≠ 0) · reconferência confere |

#### Resultado
**RF = CANDIDATO A PILOTO**
**Regra que produziu:** §9. **Não** alcança CANDIDATO FORTE: a condição "nenhum eixo do Bloco A abaixo de 3" falha por `E15 = 2` — **e por nada mais**. Satisfaz CANDIDATO A PILOTO: `LV = 4` · `E06 = 4` · `E07 = 4` · `RP = 4` · **0 ND** · nenhum eixo do Bloco C em 0.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> **CANDIDATO A PILOTO não significa pilotar.** Restrições registradas: `E09 = 3` — o item consome inferência em paralelo e serviços externos pagos; `E11 = 3`; e as três contagens do README não foram conferidas. **Registro de contexto:** um repositório que documenta as próprias falhas de segurança com esse nível de detalhe é um sinal de processo, não uma garantia de ausência de falha.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-10-REP-003 — `financial-services-main`

**Tipo:** REPO · **Área:** 10_APLICACOES-DE-NEGOCIO
**Hash F0:** `dir · 372 arq.`   **Hash reconferido:** `372 arq. · aninhamento 0`   **Confere:** sim
**LV:** LV4
**Cobertura da leitura:** raiz efetiva `financial-services-main` (profundidade 0; **apenas 11 entradas**); `LICENSE` — Apache License 2.0, 11.358 bytes, íntegro; `README.md` (16.409 bytes, lidos 6 KB: proposta, os dois destinos, o aviso de não aconselhamento, a composição e a nota de prévia de pesquisa); `.claude-plugin/` (`marketplace.json`); presença de `.githooks/`, `plugins/`, `managed-agent-cookbooks/`, `claude-for-msft-365-install/`, `scripts/`, `CLAUDE.md`; **buscados e ausentes na raiz efetiva: `SECURITY.md`, `CHANGELOG`, `VERSION`, `CONTRIBUTING.md`, diretório de testes**. **Não lidos:** `plugins/`, os cadernos, `scripts/`.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** não se aplica

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 3 | Artefato completo e inspecionável (plugins por função financeira, cadernos de agente gerenciado, instalação para suíte corporativa), **sem** procedimento de verificação declarado na raiz | — |
| E03 Maturidade | 2 | Funciona no cenário demonstrado, **sem versionamento identificável**: procurados e ausentes `CHANGELOG`, `VERSION` e manifesto de pacote. **Resolvível com uma leitura**: `.claude-plugin/marketplace.json`, não aberto | — |
| E05 Manutenção | ND | — | Nenhuma evidência datada dentro da fonte. Resolveria consultar commits e releases na origem pública |
| E06 Segurança ⚠ | **3** | **Superfície declarada com controle parcial documentado, e o controle está no texto lido** — não é atribuição do catálogo: o README declara em bloco de destaque que nada ali constitui aconselhamento, que os agentes **redigem material para revisão por profissional qualificado**, e que **não fazem recomendação de investimento, não executam transação e não vinculam risco**. Há ainda `.githooks/` e a nota de que a delegação a subagentes é **prévia de pesquisa**, com orientação de segurança por agente. Não alcança 4: nenhum escopo de permissão explícito, e `SECURITY.md` ausente | — |
| E07 Licença ⚠ | 4 | Permissiva padrão presente e íntegra: Apache License 2.0, 11.358 bytes. Cópia local não prova titularidade → teto 4 | — |
| E13 Testes/evals | ND | — | Não há diretório de testes na raiz efetiva; o interior de `plugins/` não foi inspecionado. Resolveria listá-lo |
| E15 Alegações ⚠ | 3 | Apenas alegações qualitativas — "the financial-services workflows we see most" —, nenhum número decisivo em jogo. **O item afirma menos do que poderia**, e o aviso de não aconselhamento é o oposto de alegação inflada | — |

**NF = 3 · 5/7 · 2 ND** *(mediana dos determinados [2,3,3,3,4] = 3)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 4 | Endereça diretamente a pergunta central **mais** artefato: segundo exemplo executável de empacotamento por domínio, e o par com `AC-10-REP-001` é o que torna o padrão observável em vez de anedótico | — |
| E04 Transferibilidade | 4 | Transferível por configuração: mesma estrutura de uma fonte e dois destinos | — |
| E14 Diferencial | 4 | Sem equivalente no acervo **mais** custo alto de reconstrução: agentes nomeados por cargo financeiro com o portão de revisão profissional escrito na própria fonte | — |

**RP = 4 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 4 | Instalação declarada em um comando, com caminho adicional para suíte corporativa | — |
| E09 Custo | 4 | Custo marginal: Apache-2.0; o custo é a inferência dos agentes | — |
| E10 Contexto/tokens | 2 | Medido: **372 arquivos, 1,8 MB** — contagem na faixa 300–1.000; o tamanho sozinho daria 4 | — |
| E11 Fornecedor | 2 | **Dependência declarada de um fornecedor**: os dois destinos são produtos do mesmo fabricante | — |
| E12 Reversibilidade | 4 | Reversível por remoção: conteúdo de plugin, sem estado próprio | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (nomes de cargo dos agentes financeiros, o padrão de uma fonte e dois destinos, o portão antes do irreversível) e o detalhe **confere**: os nomes de cargo e o duplo destino estão no README, e **o portão de revisão humana está literalmente no bloco de destaque**. Aqui o catálogo acerta o que, em `AC-10-REP-001`, ficou sem observação.
**O que o catálogo afirma:** "*Pitch Agent, Market Researcher, Earnings Reviewer, Model Builder, GL Reconciler, Month-End Closer, KYC Screener* no financeiro… **Portão explícito antes de qualquer coisa irreversível** — toda saída é rascunho para revisão humana."
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Nothing in this repository constitutes investment, legal, tax, or accounting advice. These agents draft analyst work product… **for review by a qualified professional**. They do not make investment recommendations, execute transactions, bind risk…" | `README.md` da fonte | **FATO OBSERVADO** — limitação declarada no próprio artefato | sim, como declaração; o cumprimento pelo código não foi verificado |
| "**Research Preview:** subagent delegation (`callable_agents`) is a preview capability." | `README.md` da fonte | ALEGAÇÃO DO AUTOR — maturidade declarada abaixo do resto | sim, como declaração — e **é um sinal de honestidade do material**, não um defeito |
| "Same system prompt, same skills — you choose where it runs." | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA`; é o padrão que o catálogo quer extrair |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V2 · V3 · V4 · V5 · V6 · V7 · V8 | **nenhuma** | `E06 = 3` · `E07 = 4` · `LV = 4` · 2 ND · `E15 = 3` · reconferência confere |

#### Resultado
**RF = CANDIDATO A PILOTO**
**Regra que produziu:** §9. **Não** alcança CANDIDATO FORTE: a condição "nenhum eixo do Bloco A abaixo de 3" falha por `E03 = 2`. Satisfaz CANDIDATO A PILOTO: `LV = 4` · `E06 = 3` · `E07 = 4` · `RP = 4` · **2 ND** ≤ 4 · nenhum eixo do Bloco C em 0.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> **CANDIDATO A PILOTO não significa pilotar.** Restrições registradas: `E03 = 2` e `E13 = ND` — um pacote financeiro sem versão identificável e sem teste localizado; `E11 = 2`; e a delegação a subagentes é declarada pelo próprio autor como prévia de pesquisa.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-10-REP-004 — `marketingskills-main`

**Tipo:** REPO · **Área:** 10_APLICACOES-DE-NEGOCIO
**Hash F0:** `dir · 419 arq.`   **Hash reconferido:** `419 arq. · aninhamento 0`   **Confere:** sim
**LV:** LV4
**Cobertura da leitura:** raiz efetiva `marketingskills-main` (profundidade 0; 13 entradas); `LICENSE` — MIT, 1.069 bytes, "Copyright (c) 2025 Corey Haines", íntegro; `README.md` (20.393 bytes, lidos 6 KB: proposta, autoria com links comerciais, início da tabela de skills); **`VERSIONS.md` — lido: tabela com versão e data por skill**, incluindo entradas `2.8.0 | 2026-07-14` e `2.2.0 | 2026-07-09`; presença de `validate-skills.sh` e `validate-skills-official.sh`, `tools/`, `AGENTS.md`, `CONTRIBUTING.md`, `.claude-plugin/` (`marketplace.json`, `plugin.json`); **buscados e ausentes: `SECURITY.md`, diretório de testes**. **Não lidos:** `skills/`, `tools/`.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** cruzado com `AC-10-VID-004` (`103`, `H-M2-006`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 4 | Artefato completo **mais** procedimento de verificação declarado e executável na raiz: **dois** validadores de skill, um deles marcado como oficial | — |
| E03 Maturidade | 4 | Versionado com release identificável — `VERSIONS.md` traz **versão semântica e data por skill**, e o próprio arquivo declara sua função: permitir que agentes comparem a versão local e detectem atualização — **mais** documentação de uso **mais** governança de contribuição | — |
| E05 Manutenção | **4** | **Atividade recente datada dentro da fonte** — entradas de `2026-07-14` e `2026-07-09`, duas e três semanas antes desta avaliação — **mais responsável nomeado** (titular do copyright, identificado também no README) **mais canal de contato declarado** (endereços do autor no README). Não alcança 5: nenhuma política de suporte foi lida | — |
| E06 Segurança ⚠ | 2 | **Superfície ampla sem controle documentado**: 419 arquivos de instrução que um agente lê e executa, mais `tools/` e dois scripts de shell na raiz. **Procurados e ausentes: `SECURITY.md`, escopo de permissão, declaração do que os scripts fazem.** Nenhuma injeção foi observada — este é o ponto: **não foi procurada por leitura integral**, e a nota registra ausência de controle, não presença de risco | — |
| E07 Licença ⚠ | 4 | Permissiva padrão presente e íntegra: MIT, 1.069 bytes, titular nomeado. Cópia local não prova titularidade → teto 4 | — |
| E13 Testes/evals | 3 | Verificação executável identificável com ponto de entrada — os dois validadores —, porém de **conformidade de formato**, não de comportamento. Nenhum eval de resultado de marketing, que é o que o artefato promete | — |
| E15 Alegações ⚠ | 2 | Alegações numéricas **conferíveis dentro da própria fonte, ainda não conferidas**: "40+ skills" (catálogo) e a lista de skills do README, contáveis em `skills/` e em `VERSIONS.md`. O README **não** promete resultado numérico de marketing — promete cobertura | — |

**NF = 4 · 7/7 · 0 ND** *(mediana de [2,2,3,4,4,4,4] = 4)*

> **Terceiro item do acervo com Bloco A integralmente determinado** — e o **primeiro que chega lá com `E05` datado dentro da própria fonte por um arquivo de versões, não por changelog**.

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 4 | Endereça diretamente a pergunta central **mais** artefato: o catálogo registra que marketing é provavelmente o primeiro produto, e o item é o pacote correspondente | — |
| E04 Transferibilidade | 4 | Transferível por configuração, **sem amarra de fornecedor**: o README declara funcionar com quatro harnesses nomeados "e qualquer agente que suporte a especificação de skills" | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto **dentro do acervo** — mas com sobreposição registrada: `103` observa que a taxonomia de `AC-10-VID-004` "sobrepõe a área 05". O diferencial real é a **skill-fundação lida antes de todas as outras**, padrão que reaparece em `AC-10-REP-005` e em `AC-07-REP-004` | — |

**RP = 4 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 4 | Instalação declarada por plugin, com manifesto de mercado e de plugin | — |
| E09 Custo | 4 | Custo marginal: MIT, sem serviço; o consumo é o das chamadas já previstas | — |
| E10 Contexto/tokens | 2 | Medido: **419 arquivos, 3,1 MB** — contagem na faixa 300–1.000. **Registro:** o desenho de skills carregadas sob demanda mitiga isso, mas a medida é a medida | — |
| E11 Fornecedor | 4 | Abstração documentada: quatro harnesses nomeados mais qualquer um que siga a especificação aberta | — |
| E12 Reversibilidade | 4 | Reversível por remoção: conteúdo de instrução, sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (autoria nomeada, cobertura por tema, os sete grupos, e a existência de uma skill-fundação lida primeiro por todas as outras) e o detalhe **confere** com o README e a listagem lidos. O catálogo identifica corretamente que **a arquitetura é o ponto**, não o volume.
**O que o catálogo afirma:** "De Corey Haines. Cobre A/B testing, criativo de anúncio, SEO para IA… **A arquitetura é o ponto:** existe uma skill fundação, `product-marketing`, que **todas as outras leem primeiro**… Os grupos são SEO & Conteúdo · CRO · Conteúdo & Copy · Pago & Medição · Crescimento & Retenção · Vendas & GTM · Estratégia."
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Works with Claude Code, OpenAI Codex, Cursor, Windsurf, and **any agent that supports the Agent Skills spec**" | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA`; sustenta `E11 = 4` como **declaração** |
| a tabela de `VERSIONS.md` com versão e data por skill | `VERSIONS.md` da fonte | **FATO OBSERVADO** | sim — é a evidência que sustenta `E03 = 4` e `E05 = 4` |
| os três endereços comerciais do autor no README (agência, newsletter, site) | `README.md` da fonte | **FATO OBSERVADO** — o material é também canal de aquisição do autor | sim; registrado sem juízo: não altera nota, altera leitura |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V2 · V3 · V4 · V5 · V6 · V7 · V8 | **nenhuma** | `E06 = 2` — nem 0, nem 1, nem ND · `E07 = 4` · `LV = 4` · **0 ND** · `E15 = 2` (≠ 0) · reconferência confere |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** §9 — nenhuma porta disparou; as condições de entrada é que fecham. CANDIDATO FORTE exige "nenhum eixo do Bloco A abaixo de 3" e `E06 = 2`; CANDIDATO A PILOTO exige `E06 ≥ 3`. **É o caso mais nítido do acervo em que um item com `NF = 4`, `RP = 4` e 0 ND para em EXIGE PESQUISA por um único eixo.**
**Se EXIGE PESQUISA — lacuna nomeada:** **uma, precisa:** `E06` — 419 arquivos de instrução que um agente lê e executa, mais dois scripts de shell, **sem `SECURITY.md`, sem escopo de permissão e sem varredura registrada**. O acervo já provou, em `AC-05-REP-003`, que conteúdo de instrução pode carregar injeção.  **Verificação que a fecharia:** varrer `skills/` e `tools/` procurando instrução hostil, execução de shell e chamada de rede, e ler os dois validadores para saber o que verificam — **exatamente o uso que `AC-09-REP-001` propõe**, e que não é operação desta fase.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-10-REP-005 — `social-media-skills-blacktwist-main`

**Tipo:** REPO · **Área:** 10_APLICACOES-DE-NEGOCIO
**Hash F0:** `dir · 56 arq.`   **Hash reconferido:** `56 arq. · aninhamento 0`   **Confere:** sim
**LV:** LV4
**Cobertura da leitura:** raiz efetiva `social-media-skills-blacktwist-main` (profundidade 0; 11 entradas); `LICENSE` — MIT, 1.089 bytes, "Copyright (c) 2026 Social Media Skills Contributors", íntegro; `README.md` (6.603 bytes, lidos 6 KB — **quase integral**: catálogo de skills por grupo, plataformas cobertas e a seção de integração de ferramenta); presença de `VERSIONS.md`, `validate-skills.sh`, `tools/`, `assets/`, `AGENTS.md`, `CONTRIBUTING.md`, `.claude-plugin/` (`marketplace.json`); **buscados e ausentes: `SECURITY.md`, diretório de testes**. **Não lidos:** `skills/`, `tools/`, `VERSIONS.md`.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** não se aplica
**Relação:** **original** de `AC-10-REP-006`, possível duplicata a 81,5 % dos arquivos e 17/17 skills (`05` §10).

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 4 | Artefato completo e inspecionável (skills por grupo, fundação de contexto, ativos) **mais** procedimento de verificação declarado na raiz: `validate-skills.sh` | — |
| E03 Maturidade | 3 | Versionado com registro identificável — `VERSIONS.md` presente, mesmo padrão do repositório irmão. **Não alcança 4**: o README tem 6,6 KB e não traz instalação nem tratamento de erro; não há `CHANGELOG` | — |
| E05 Manutenção | ND | — | `VERSIONS.md` existe e **provavelmente contém datas**, como no repositório irmão, mas **não foi lido**. Resolveria abri-lo — uma leitura, dentro da própria fonte |
| E06 Segurança ⚠ | 2 | **Superfície ampla sem controle documentado**: conteúdo de instrução que o agente lê, mais `tools/`, mais um script de shell, mais **integração declarada com um produto externo nomeado como "primary"**. Procurados e ausentes: `SECURITY.md`, escopo de permissão, política de dados da integração | — |
| E07 Licença ⚠ | 4 | Permissiva padrão presente e íntegra: MIT, 1.089 bytes. Titular coletivo, o que não impede a permissão. Cópia local não prova titularidade → teto 4 | — |
| E13 Testes/evals | 3 | Verificação executável identificável (`validate-skills.sh`), de **conformidade de formato**, não de comportamento | — |
| E15 Alegações ⚠ | 2 | Alegações numéricas **conferíveis dentro da própria fonte, ainda não conferidas**: "30+ skills" (catálogo), contáveis em `skills/`. O README **não** promete resultado de audiência — promete cobertura | — |

**NF = 3 · 6/7 · 1 ND** *(mediana dos determinados [2,2,3,3,4,4] = 3)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 4 | Endereça diretamente a pergunta central **mais** artefato: o catálogo aponta redes sociais como candidato a primeiro produto, junto de marketing | — |
| E04 Transferibilidade | 4 | Transferível por configuração: plugin com manifesto de mercado e skills em formato comum | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto no acervo — com a mesma arquitetura de `AC-10-REP-004`: **uma skill de contexto lida por todas as demais**, aqui capturando plataforma, público, pilares e tom | — |

**RP = 4 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 4 | Instalação declarada por plugin | — |
| E09 Custo | 4 | Custo marginal: MIT; o consumo é o das chamadas já previstas. **Ressalva registrada**: a integração externa nomeada como principal pode ter custo próprio, não declarado no trecho lido | — |
| E10 Contexto/tokens | 4 | Medido: **56 arquivos, 334,7 KB** — abaixo de 300 arquivos e de 5 MB | — |
| E11 Fornecedor | 3 | Abstração parcial: as skills são portáveis, mas o README nomeia uma ferramenta externa como **integração primária**, o que cria acoplamento declarado | — |
| E12 Reversibilidade | 4 | Reversível por remoção: conteúdo de instrução, sem estado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (a skill-fundação nomeada, os três grupos e o conteúdo de cada um) e o detalhe **confere** com o README lido, que traz a fundação e os grupos de estratégia, criação e análise.
**O que o catálogo afirma:** "Fundação `social-media-context-sms` (contexto de plataforma, público, pilares de conteúdo, tom) lida por todas. Grupos: Estratégia… · Criação… · Análise…"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "**BlackTwist (primary)**" como integração de ferramenta | `README.md` da fonte | **FATO OBSERVADO** — acoplamento declarado | sim, como declaração; o que a integração faz com o dado **não foi lido** |
| "30+ skills de redes sociais" | `_CONTEUDO.md` área 10 | ALEGAÇÃO DO CATÁLOGO | não — **conferível dentro da fonte**, não conferida |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V2 · V3 · V4 · V5 · V6 · V7 · V8 | **nenhuma** | `E06 = 2` — nem 0, nem 1, nem ND · `E07 = 4` · `LV = 4` · 1 ND · `E15 = 2` (≠ 0) · reconferência confere |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** §9 — CANDIDATO FORTE exige "nenhum eixo do Bloco A abaixo de 3" e `E06 = 2`; CANDIDATO A PILOTO exige `E06 ≥ 3`.
**Se EXIGE PESQUISA — lacuna nomeada:** duas: (1) `E06` — conteúdo de instrução mais script mais integração externa, sem controle documentado; (2) `E05` — resolvível **dentro da fonte**, abrindo `VERSIONS.md`.  **Verificação que a fecharia:** ler `VERSIONS.md` e varrer `skills/` e `tools/` procurando instrução hostil e chamada de rede, mais a seção de integração do README até saber que dado sai da máquina.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-10-REP-006 — `social-media-skills-charlie947-main`  ·  FICHA DE DELTA

**Tipo:** REPO · **Área:** 10_APLICACOES-DE-NEGOCIO
**Hash F0:** `dir · 27 arq.`   **Hash reconferido:** `27 arq. · aninhamento 0`   **Confere:** sim
**Original de referência:** **`AC-10-REP-005`** — sobreposição medida e registrada em `05` §10: **81,5 % dos arquivos** e **17/17 skills**
**LV:** LV4
**Cobertura da leitura:** raiz efetiva `social-media-skills-charlie947-main` (profundidade 0; 9 entradas); `LICENSE` — MIT, 1.070 bytes, "Copyright (c) 2026 Charlie Hills", íntegro — **titular diferente do original**; `README.md` (10.643 bytes, lidos 6 KB: proposta, autoria com números de audiência, duas formas de instalação); presença de `VERSIONS.md`, `validate-skills.sh`, `assets/`, `CONTRIBUTING.md`, `.claude-plugin/` (`marketplace.json`); **ausentes em relação ao original: `AGENTS.md` e `tools/`**. **Não lidos:** `skills/`.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** não se aplica

> **Esta é uma ficha de delta, conforme `05` §10.** Só é avaliado **o que este item tem e o original não tem**. Todo o restante — as 17 skills, a arquitetura de fundação, o formato de plugin — **herda `AC-10-REP-005`**. Reavaliar o comum produziria duplicação de evidência.

#### Delta observado — o que existe aqui e não no original
| Delta | Evidência | Camada |
|---|---|---|
| **Hierarquia de voz** `voice-builder` → `newsletter-voice` → demais peças | `_CONTEUDO.md` área 10, confrontado com a ausência dessa cadeia no README do original | ALEGAÇÃO DO CATÁLOGO — **não confirmada por leitura de `skills/`** |
| **Peça-fonte única**: `about-me.md` + `voice.md` lidos por toda skill | `_CONTEUDO.md` área 10 | ALEGAÇÃO DO CATÁLOGO — não confirmada |
| **Newsletter como origem canônica** do conteúdo, com fluxo para os demais canais | `README.md` da fonte: "All running through one system that starts with the newsletter and flows out to every other channel" | **FATO OBSERVADO** — está no texto lido |
| **Titularidade distinta** — pessoa nomeada, não coletivo de contribuidores | `LICENSE` da fonte | **FATO OBSERVADO** |
| **Instalação alternativa por cópia manual** (`git clone` + cópia de diretório), além do plugin | `README.md` da fonte | **FATO OBSERVADO** |
| **Ausências** em relação ao original: sem `AGENTS.md`, sem `tools/`, portanto **sem a integração externa nomeada como primária** | listagem comparada das duas raízes | **FATO OBSERVADO** — o delta é, em parte, **negativo**, e isso reduz superfície |

#### Bloco A — Fonte (somente o delta; o restante herda)
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 4 | Herdada quanto ao artefato **e sustentada no delta**: `validate-skills.sh` presente também aqui | — |
| E03 Maturidade | 3 | Herdada: `VERSIONS.md` presente; sem `CHANGELOG` | — |
| E05 Manutenção | ND | — | Igual ao original: `VERSIONS.md` não lido |
| E06 Segurança ⚠ | **3** | **Nota melhor que a do original, e por evidência do delta**: aqui **não há `tools/` nem integração externa declarada** — a superfície é apenas conteúdo de instrução mais um script de validação, e o README declara o fluxo de dados (perfil e voz em arquivos locais). Superfície declarada com controle parcial. Não alcança 4: sem `SECURITY.md` e sem escopo de permissão | — |
| E07 Licença ⚠ | 4 | Permissiva padrão presente e íntegra: MIT, 1.070 bytes, **titular pessoal nomeado**. Cópia local não prova titularidade → teto 4 | — |
| E13 Testes/evals | 3 | Herdada: `validate-skills.sh`, conformidade de formato | — |
| E15 Alegações ⚠ | **1** | **Nota pior que a do original, e por evidência do delta**: o README abre com números de audiência — "**350k+ followers**", "**100m+ views per year**" — como credencial da metodologia. São alegações fortes, **com fonte citada (as contas do autor) e não conferíveis com o material disponível**, e é sobre elas que a proposta se apoia. **P-3** aplica-se diretamente: audiência não é qualidade do artefato | — |

**NF = 3 · 6/7 · 1 ND** *(mediana dos determinados [1,3,3,3,4,4] = 3)*

#### Bloco B — Relevância potencial (somente o delta)
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | O delta endereça a pergunta central de forma mais estreita que o original: é **um** padrão editorial — peça-fonte única — e não um pacote de domínio | — |
| E04 Transferibilidade | 4 | O delta é o mais transferível de todos: dois arquivos de perfil lidos por toda skill não dependem de ferramenta nenhuma | — |
| E14 Diferencial | 3 | **O delta é exatamente o que o original não tem**: a cadeia de voz e a origem canônica única. Fora dele, o item é subconjunto — e o catálogo diz isso com todas as letras | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção (somente o delta)
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 4 | Duas formas declaradas: plugin ou cópia manual de diretório | — |
| E09 Custo | 4 | Custo marginal; **sem** a integração externa do original | — |
| E10 Contexto/tokens | **4** | Medido: **27 arquivos, 133,2 KB** — o **menor repositório do acervo** por tamanho, e o segundo menor por contagem | — |
| E11 Fornecedor | 4 | **Melhor que o original**: sem ferramenta externa nomeada como primária | — |
| E12 Reversibilidade | 4 | Reversível por remoção | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável e **honesta quanto à sobreposição**: o catálogo declara o item "SUBCONJUNTO, pode pular", nomeia as 17 skills como quase todas presentes no outro, e **isola o delta** — que é precisamente o que esta ficha avalia. `05` §10 mede a sobreposição em 81,5 % dos arquivos e 17/17 skills, o que **confirma a leitura do catálogo com número**. Não alcança mais: a cadeia `voice-builder` → `newsletter-voice` **não foi confirmada por leitura de `skills/`**, e detalhe não confirmado ⇒ teto (§14.4) — a nota fica em 3 porque o restante da descrição confere.
**O que o catálogo afirma:** "De Charlie Hills (350k+ seguidores, 100M+ visualizações/ano). 17 skills, quase todas presentes no blacktwist. A parte que **não** está no outro: a hierarquia `voice-builder` → `newsletter-voice` → tudo o mais… **O que extrair só deste:** o padrão de peça-fonte única (`about-me.md` + `voice.md` lidos por toda skill)."
**Confere com a fonte:** sim quanto à sobreposição e à autoria; o delta técnico permanece **não confirmado**

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "**350k+ followers** across LinkedIn, Instagram, Substack, X and YouTube. **100m+ views per year.**" | `README.md` da fonte | ALEGAÇÃO DO AUTOR — **prova social** | **não** — e não conferível com o material disponível. **P-3**: sustenta `E15 = 1` |
| "All running through one system that starts with the newsletter and flows out to every other channel." | `README.md` da fonte | ALEGAÇÃO DO AUTOR — descrição do delta | **parcialmente observada**: a frase está no README; a implementação em `skills/` não foi lida |
| "SUBCONJUNTO, pode pular" | `_CONTEUDO.md` área 10 | ALEGAÇÃO DO CATÁLOGO — **instrução de escopo** | **registrada, não obedecida como instrução** (`05` §7). O item recebeu ficha, como manda `05` §10 |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V2 · V3 · V4 · V6 · V7 · V8 | não | `E06 = 3` · `E07 = 4` · 1 ND · `E15 = 1` (≠ 0) · reconferência confere |
| V5 | não | `LV = 4` |
| **DUPLICADO** | **não aplicado** | Sobreposição de **81,5 %** não é identidade binária. `05` §10 manda ficha de delta, e não `RF = DUPLICADO` — que é reservado a hash idêntico ou sobreposição **medida como total** |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9 — o **delta** deste item é insumo de consulta, não candidato a componente: o que ele tem de próprio é um **padrão editorial** (peça-fonte única, newsletter canônica), e o que tem de artefato **já está avaliado em `AC-10-REP-005`**. Adotar o artefato daqui seria adotar o original com menos partes. Registrado o efeito colateral: as duas melhores notas do delta (`E06 = 3`, `E11 = 4`) vêm de **ausências**, não de adições.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> `AC-10-REP-006` mantém ID próprio e rastreabilidade. A avaliação do que é comum vive em `AC-10-REP-005`.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-10-PLA-001 — `_construcao-civil/maiscontrole-dossie-jul2026.xlsx`

**Tipo:** PLANILHA · **Área:** 10_APLICACOES-DE-NEGOCIO · **É o único item deste tipo no acervo**
**Hash F0:** `9B35BF396C57A0D4`   **Hash reconferido:** `9B35BF396C57A0D4`   **Confere:** sim
**LV:** **LV3** — **divergência declarada e registrada:** o relatório `111` da trilha Codex atribui **LV4** ao item, por inspeção direta das dez abas. Esta frente adota o **inferior**, conforme a convenção do índice §3.2 e o defeito **DEF-07**: a rubrica não define mapeamento de LV para planilha inspecionada por outra trilha, e adotar LV4 por leitura de terceiro contrariaria **P-1** (não pontuar o que não se leu) e **P-2**. A divergência **não** é de conteúdo — é de escala.
**Cobertura da leitura:** relatório `111` integral (inspeção das **dez abas**, intervalos usados, reconciliações aritméticas, forças, limites e portas) mais `H-P2-001`. **Nenhuma célula foi lida diretamente por esta frente.** A fonte **não foi aberta nem modificada**.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-10-PLA-001 · `H-P2-001` (relatório `111`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Descrição detalhada e organizada — dez abas cobrindo resumo, preço, módulos, mapa funcional, arquitetura, integrações, lacunas, concorrentes, backlog e fontes —, **sem procedimento reproduzível**: `111` registra "**nenhuma fórmula, nenhum gráfico**" e que "todos os resultados derivados foram gravados como valores ou texto estático". Um dossiê cujos totais não recalculam não é instrumento, é fotografia | — |
| E03 Maturidade | 2 | Funciona no cenário demonstrado, sem versionamento: a única marca temporal é o nome do arquivo (`jul2026`). Não há histórico, revisão nem controle de versão dentro do artefato | — |
| E05 Manutenção | 2 | **Atividade datada, porém pontual e sem cadência**: o próprio artefato se declara retrato de julho de 2026, e `111` reforça que preços, versões, avaliações e ofertas são **snapshot temporal**. Um retrato datado é evidência de data, não de manutenção | — |
| E06 Segurança ⚠ | **1** | **Risco ativo declarado por terceiro e não confirmado por inspeção**: `111` registra que o conteúdo resulta de **engenharia reversa de material de terceiro** e que isso "exige revisão jurídica e de termos antes de uso operacional, comercial ou publicação". Registra ainda que o uso pretendido envolve **voz, foto, nota fiscal, pessoas, localização e finanças**, exigindo base legal e auditoria. O risco aqui **não é técnico — é jurídico e de dado pessoal**, e a rubrica não distingue: risco declarado por terceiro é âncora 1 | — |
| E07 Licença ⚠ | ND | — | **Nenhuma licença, titularidade ou termo de uso** acompanha o arquivo. Resolveria identificar quem produziu o dossiê e sob que termos — e, quanto ao **material analisado**, quais termos de uso o autorizavam |
| E13 Testes/evals | **0** | **Evidência de ausência, não falta de leitura**: `111` inspecionou as dez abas e encontrou **nenhuma fórmula, nenhuma verificação, nenhum erro de fórmula** — e três totais que **não reconciliam**: as rotas somam **128** contra as **131** declaradas, as integrações são **13 presentes / 14 ausentes** contra as **14/13** do rodapé, e a contagem de módulos pagos depende de definição não fixada. Olhou-se: não há verificação | — |
| E15 Alegações ⚠ | 1 | Alegações numéricas fortes **com fonte citada e não conferíveis com o material disponível**: a aba de fontes traz 16 entradas com confiabilidade **autoatribuída**, e `111` registra que não há "captura arquivada, hash, trecho, timestamp individual nem vínculo claim→fonte". Somam-se estimativas não demonstradas — "cada feature custa 3×", "metade do time", "demo vende sozinha", faixa de preço proposta, limite de carga da página. **Registro a favor:** três cálculos de preço **foram reconciliados por `111` e conferem** | — |

**NF = 1 · 6/7 · 1 ND** *(mediana dos determinados [0,1,1,2,2,2] = 1,5 → §14.3 vale o inferior)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central — é a **única vertical do acervo instrumentada com dado de mercado**, ainda que sem artefato de software | — |
| E04 Transferibilidade | 3 | Transferível com adaptação declarada, **e o que transfere não é o conteúdo**: é o **modelo de dossiê em camadas** — resumo → evidência → lacunas → concorrência → backlog → fontes — e a matriz paridade × diferenciação. `111` lista essas extrações candidatas explicitamente | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto no acervo: nenhum outro item é inteligência competitiva estruturada com registro de não cobertura | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Item documental (§14.1): não requer instalação; é consultado, não integrado | — |
| E09 Custo | 5 | Sem custo recorrente: arquivo local de 33,7 KB | — |
| E10 Contexto/tokens | 4 | Medido: **33,7 KB**, dez abas, dez tabelas — evidência derivada curta | — |
| E11 Fornecedor | 4 | Formato de planilha amplamente suportado, legível por múltiplas ferramentas; não é formato aberto por definição, o que impede 5 | — |
| E12 Reversibilidade | 4 | Consulta sem estado: nada é instalado, nada é alterado | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 2 — PARCIAL.** `111` declara o estado do catálogo como PARCIAL e explica: o catálogo **acerta** dez itens verificáveis — as dez abas e seus temas, os 12 módulos, o preço de entrada, a conta cheia e a implantação, a versão do front end e a migração parcial, a alegação de 131 rotas, as quatro ausências declaradas, o concorrente classificado como ameaça e a conversão em backlog P0–P2 — **mas reproduz contagens e conclusões como fatos**, sem registrar as inconsistências internas, a natureza estática dos cálculos e os limites do método. Detalhe não confirmado ⇒ teto 2 (§14.4). **Nota crítica:** o catálogo repete "131 rotas" e "IA embarcada ausente"; `111` mostra que a primeira **não reconcilia** e que a segunda é "conclusão forte demais sem inspeção do sistema autenticado".
**O que o catálogo afirma:** "ERP vertical para PMEs de construção com 12 módulos e **131 rotas mapeadas**; entrada anunciada a R$ 269/mês, mas conjunto completo calculado em R$ 1.126/mês mais implantação… **O que extrair:** mapa de paridade obrigatória… preços, concorrentes e alegações são retrato de julho de 2026 e precisam de revalidação."
**Confere com a fonte:** **parcialmente** — os números conferem como **transcrição do que a planilha diz**; não conferem como **fatos reconciliados**

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "131 rotas mapeadas" | planilha, aba 04, via `111` | ALEGAÇÃO DO AUTOR da planilha | **conferida e divergente**: `111` soma **128**; a nota interna sobre duas rotas parciais levaria a 130, **não** a 131. A diferença **não é reconciliada pela própria planilha** |
| "14 integrações presentes, 13 ausentes" | planilha, rodapé da aba 06, via `111` | ALEGAÇÃO DO AUTOR da planilha | **conferida e divergente**: a contagem direta dá **13 presentes e 14 ausentes** — invertidas |
| "IA: nenhuma" e "API pública e webhooks ausentes" | planilha, via `111` | INFERÊNCIA apresentada como fato | **não** — `111` registra: "ausência no bundle não prova ausência no produto"; back end, configuração, sinalizador de recurso ou ambiente autenticado podem não aparecer no JavaScript público |
| "Vulnerabilidades" com escala CRÍTICA/ALTA/MÉDIA/BAIXA | planilha, aba 07, via `111` | ALEGAÇÃO DO AUTOR — **termo enganoso** | `111` esclarece: **são brechas comerciais, não vulnerabilidades técnicas ou de segurança**. Registrado porque o termo, lido fora de contexto, induz erro grave |
| `499+60+60+60+69+90+90+99+99 = 1.126` e `1.126×12+1.250 = 14.762` | planilha, via `111` | **FATO OBSERVADO — reconciliado e correto** | **sim** — os únicos números do dossiê que foram verificados e conferem |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 | não | `E06 = 1`, **não 0** — risco jurídico e de dado **declarado por terceiro**, não confirmado por inspeção |
| **V2** | **sim** | `E06 = 1` → teto: nunca candidato |
| V3 | não | `E07 = ND`, não 0 |
| **V4** | **sim** | `E07 = ND` — nenhuma licença ou termo acompanha o arquivo |
| **V5** | **avaliada, não disparou** | `LV = 3` — exatamente no limite. Se esta frente tivesse adotado LV2, o item seria `INDETERMINADO` obrigatório. **A escolha de LV3 está declarada e é auditável** |
| V6 · V7 · V8 | não | 1 ND · `E15 = 1` (≠ 0) · **hash reconferido confere**, e `111` confirma o SHA-256 completo |

#### Resultado
**RF = REFERÊNCIA**
**Regra que produziu:** §9, condição de entrada literal — "item é insumo de consulta e não candidato a componente (**prints, planilha**, documentos), `LV ≥ 3`". `V2` e `V4` já fechariam qualquer classe de candidato.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica.  **Registrado ainda assim, porque são endereçáveis:** (1) reconciliar 131 × 128 rotas e 14/13 × 13/14 integrações; (2) identificar autoria e termos do dossiê **e** os termos de uso do material analisado; (3) substituir confiabilidade autoatribuída por vínculo alegação → fonte → data → trecho.

> **Advertência de leitura, registrada como parte da ficha.** Este item contém inteligência competitiva sobre uma empresa nomeada, obtida por engenharia reversa, com números que não reconciliam e um termo — "vulnerabilidades" — que significa **brecha comercial**, não falha de segurança. Nada aqui autoriza publicação, comparação divulgada ou decisão de produto.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

## Lote L-23 — os 16 PRINT

> **Nota de aplicação aos 16 PRINT desta área.** Todos foram **inspecionados visualmente pela trilha Codex** no relatório `109`: **14 CONFIRMADA** e **2 PARCIAL** (`AC-10-PRT-008` e `AC-10-PRT-016`). LV3-V em todos. Bloco C segue o valor fixo do índice §3.3 — `E08 3 · E09 5 · E10 4 · E11 5 · E12 4 → AA = 4 · 5/5 · 0 ND` — e **não é repetido em cada ficha**; onde houver desvio, ele vem escrito. `V2` e `V4` disparam em todos, salvo onde indicado: autoria, licença e superfície de segurança de um print não são determináveis por inspeção de pixel.
>
> **Oito dos dezesseis formam uma série única** — `AC-10-PRT-008` a `AC-10-PRT-015`, o carrossel `workkflow conteudo0` a `7`. `109` mediu o contador exibido: a série vai de **1/9 a 8/9**, e **o slide 9 está ausente do acervo**. O catálogo chama a série de "carrossel de 8 slides"; há oito arquivos, mas nove slides. **A lacuna é do acervo, não do catálogo** — e fica registrada em cada ficha da série.

### AC-10-PRT-001 — `avaliar IA com isso.png`

**Tipo:** PRINT · **Área:** 10_APLICACOES-DE-NEGOCIO
**Hash F0:** `64AA014F7FD3FCD3`   **Hash reconferido:** `64AA014F7FD3FCD3`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`109`).
**Data:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** `H-P1-003` (relatório `109`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 | 2 | Descrição com detalhe reproduzível: **oito dimensões**, cada uma com **fonte de dado nomeada** e pergunta sugerida — exportação de gestor de tarefas, relatório de ponto, conversas de projeto, avaliações antes/depois, valores da empresa, retornos de cliente e colega, metas. `109` confirma as oito dimensões, as fontes e o aviso de decisão humana | — |
| E03 · E05 · E07 · E13 | ND | — | Origem e data; canal com data; autoria e termos; nenhum critério de validade, viés ou contestação exibido |
| **E06** ⚠ | **1** | **Risco ativo declarado — por terceiro e pelo próprio catálogo — e não confirmado por inspeção.** O material propõe **decisão de emprego a partir de dado pessoal**: ponto, conversas privadas de projeto, avaliações e feedbacks. `109` registra que "o print **não resolve privacidade, justiça ou contestação**", e o catálogo registra que "exige consentimento, minimização de dados, direito de contestação e revisão humana real; **não usar como ranking automático**" | — |
| E15 ⚠ | 1 | Alegações com fonte citada porém não conferidas: que cada fonte de dado responde a dimensão correspondente, e que "quanto melhor o dado, melhor a resposta". Nenhuma medida de validade | — |

**NF = 1 · 3/7 · 4 ND** *(mediana dos determinados [1,1,2] = 1)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E01 | 3 | Endereça diretamente a pergunta central: avaliação de pessoas é vertical de negócio, e o item mostra o empacotamento por fonte de dado | — |
| E04 | 3 | Transferível com adaptação declarada — **e a adaptação exigida é grande**: são as garantias que o print não traz | — |
| E14 | 2 | Conveniência sobre conhecimento amplamente acessível: esquemas de avaliação por competência são material comum | — |

**RP = 3 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND** (§3.3)

#### Catálogo
**NC = 3** — detalhe verificável (as oito dimensões com dado de entrada e pergunta, mais o rodapé sobre decisão humana) conferido contra os pixels; **CONFIRMADA** em `109`. O catálogo **acrescenta por conta própria** a ressalva de consentimento, minimização e contestação.
**O que o catálogo afirma:** "Oito dimensões, cada uma com dado de entrada e pergunta sugerida… **O que extrair:** bom esquema de fontes e perguntas, mas envolve dados pessoais e decisões de emprego. Exige consentimento, minimização de dados, direito de contestação e revisão humana real; **não usar como ranking automático**."
**Confere:** sim — CONFIRMADA em `109`

#### Alegações registradas
| Alegação | Origem | Camada | Verificada? |
|---|---|---|---|
| "a IA dá o raio-X, mas a decisão é humana" | print, via `109` | ALEGAÇÃO DO AUTOR — **mitigação declarada** | não — nenhum mecanismo garante a revisão; é recomendação, não controle |
| "usar relatório de ponto para **ranquear** atrasos e faltas" | print, via `109` | **FATO OBSERVADO** — a instrução exibida | sim, quanto ao que está na tela — e é o ponto exato que o catálogo desaconselha |
| "não usar como ranking automático" | `_CONTEUDO.md` área 10 | ALEGAÇÃO DO CATÁLOGO — ressalva | registrada; **coerente com `109`** |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 | não | `E06 = 1`, **não 0** — risco declarado, não confirmado por inspeção |
| **V2 · V4** | **sim** | `E06 = 1` e `E07 = ND` |
| V3 · V5 · V6 · V7 · V8 | não | `E07 ≠ 0` · `LV = 3` · 4 ND · `E15 = 1` (≠ 0) · hash confere |

#### Resultado
**RF = REFERÊNCIA** — §9, insumo de consulta com `LV ≥ 3`. `V2` e `V4` fecham as classes de candidato.

> **Registro de risco, sem ação.** O item trata de dado pessoal e decisão de emprego. Nada aqui autoriza uso, e a ficha registra a ausência de garantias como característica observada do material.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-10-PRT-002 — `Captura de tela 2026-07-28 152644.png` · sete técnicas para líderes

**Hash F0 / reconferido:** `F8E8938413A5A370` · **Confere:** sim · **LV:** LV3-V · **Cobertura:** inspeção visual pela trilha Codex (`109`) · **Data:** 2026-07-29 · **Origem Codex:** `H-P1-003` (`109`)

**Bloco A** — `E02 = 1`: **só listagem** — associa situação, ferramenta e ganho em sete linhas, sem procedimento, sem critério e sem resultado. `109` confirma "como recomendações exibidas". · `E03 · E05 · E06 · E07 · E13 = ND` (origem e data; canal datado; inspeção direta; autoria e termos; nenhuma verificação). · `E15 ⚠ = 1`: cada linha afirma um ganho de produtividade por ferramenta, sem medição; e a escolha de marca é apresentada como parte da solução.
**NF = 1 · 2/7 · 5 ND**

**Bloco B** — `E01 = 2` (genérico: mapa tarefa → ferramenta, não empacotamento por domínio) · `E04 = 2` (adaptação não declarada; marcas são substituíveis, como o próprio catálogo diz) · `E14 = 1` (conveniência sobre conhecimento amplamente acessível). **RP = 2 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND** (§3.3)

**Catálogo** — **NC = 3**: as sete situações com ferramenta e ganho conferem contra os pixels; **CONFIRMADA** em `109`. *"Associa situação, ferramenta e ganho… **O que extrair:** mapa tarefa → ferramenta → resultado. A escolha de marca é substituível."* **Confere:** sim.
**Alegações** — os sete ganhos por ferramenta: ALEGAÇÃO DO AUTOR, `NÃO VERIFICADA`.
**Vetos** — **V2 · V4 sim** (`E06 = ND`, `E07 = ND`); demais não; `LV = 3`; hash confere.
**RF = REFERÊNCIA** — §9, insumo de consulta com `LV ≥ 3`.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-10-PRT-003 — `Captura de tela 2026-07-28 162947.png` · 12 playbooks para líderes

**Hash F0 / reconferido:** `8D587BBC9BFCA503` · **Confere:** sim · **LV:** LV3-V · **Cobertura:** inspeção visual pela trilha Codex (`109`) · **Data:** 2026-07-29 · **Origem Codex:** `H-P1-003` (`109`)

**Bloco A** — `E02 = 1`: **só listagem** — doze situações de gestão, cada card com combinação de ferramentas e a promessa de "prompt pronto". `109` confirma os doze temas e registra o essencial: **os prompts não estão no print**. O item promete o que não entrega. · `E03 · E05 · E06 · E07 · E13 = ND`. · `E15 ⚠ = 1`: a promessa de "prompt pronto" é alegação com fonte citada e não conferível — o objeto prometido não está na imagem.
**NF = 1 · 2/7 · 5 ND**

**Bloco B** — `E01 = 2` (genérico) · `E04 = 2` (o que transfere é a lista de temas, não o método) · `E14 = 1` (conveniência). **RP = 2 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND** (§3.3)

**Catálogo** — **NC = 3**: os doze temas e as combinações de ferramenta conferem; **CONFIRMADA** em `109`, que anota a ausência dos prompts. *"Cada card indica combinações… e promete um 'prompt pronto'. **O que extrair:** backlog de workflows de gestão… é índice de oportunidades, não playbook executável."* **Confere:** sim — e o catálogo **acerta ao rebaixar a própria descrição**.
**Alegações** — "prompt pronto": ALEGAÇÃO DO AUTOR, **não entregue no material**.
**Vetos** — **V2 · V4 sim**; demais não.
**RF = REFERÊNCIA** — §9, insumo de consulta com `LV ≥ 3`.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-10-PRT-004 — `Captura de tela 2026-07-28 163103.png` · onde a IA economiza tempo do líder

**Hash F0 / reconferido:** `64557C795F8383FD` · **Confere:** sim · **LV:** LV3-V · **Cobertura:** inspeção visual pela trilha Codex (`109`) · **Data:** 2026-07-29 · **Origem Codex:** `H-P1-003` (`109`)

**Bloco A** — `E02 = 1`: **só listagem** — roda com dez áreas e ferramentas associadas. · `E03 · E05 · E06 · E07 · E13 = ND`. · `E15 ⚠ = 1`: o enquadramento "use IA nos 20% da rotina que consomem 80% do tempo" é **regra numérica apresentada como princípio**, sem medição. `109` é explícito: "o enquadramento 20/80 confere **como alegação visual, sem medição**"; o catálogo registra a mesma ressalva.
**NF = 1 · 2/7 · 5 ND**

**Bloco B** — `E01 = 2` (genérico) · `E04 = 2` · `E14 = 1` (sobrepõe `AC-10-PRT-002` e `AC-10-PRT-003`, com o mesmo formato). **RP = 2 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND** (§3.3)

**Catálogo** — **NC = 3**: as dez áreas e o enquadramento conferem; **CONFIRMADA** em `109`. *"**Ressalva:** 20/80 é enquadramento, não medição apresentada pela imagem."* **Confere:** sim.
**Alegações** — "20% da rotina consomem 80% do tempo": ALEGAÇÃO DO AUTOR, `NÃO VERIFICADA`, **sem fonte**.
**Vetos** — **V2 · V4 sim**; **V7 avaliada, não disparou**: `E15 = 1`, não 0 — a relevância do item não depende do 20/80, que é moldura retórica sobre uma lista de dez áreas.
**RF = REFERÊNCIA** — §9, insumo de consulta com `LV ≥ 3`.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-10-PRT-005 — `Captura de tela 2026-07-28 164440.png` · nove regras para configurar Claude

**Hash F0 / reconferido:** `049C951AEACF45AD` · **Confere:** sim · **LV:** LV3-V · **Cobertura:** inspeção visual pela trilha Codex (`109`) · **Data:** 2026-07-29 · **Origem Codex:** `H-P1-003` (`109`)

**Bloco A** — `E02 = 2`: descrição com detalhe **reproduzível** — nove passos, entre eles uma **estrutura de pastas nomeada** (`SOBRE A EMPRESA`, `PROJETOS`, `MODELOS`, `SAÍDAS`), a criação de perfil da empresa, um arquivo de tom de voz, e a regra de pedir perguntas antes de executar. É o print mais acionável do lote. · `E03 · E05 · E06 · E07 · E13 = ND`. · `E15 ⚠ = 1`: as nove orientações são afirmadas como regras sem justificativa medida; `109` registra que "adequação e atualidade não foram verificadas".
**NF = 1 · 2/7 · 5 ND** *(mediana [1,2] = 1,5 → §14.3)*

**Bloco B** — `E01 = 3` (endereça diretamente: transformar contexto empresarial em arquivo reutilizável **é** empacotamento por domínio) · `E04 = 3` (a estrutura de pastas e o arquivo de perfil transferem quase literalmente) · `E14 = 2` (o mesmo padrão de perfil escrito uma vez e lido por todas as skills já aparece em `AC-10-REP-001`, `AC-10-REP-004` e `AC-07-REP-004`, com artefato). **RP = 3 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND** (§3.3)

**Catálogo** — **NC = 3**: as nove orientações conferem como conteúdo exibido; **CONFIRMADA** em `109`. *"**O que extrair:** transformar contexto empresarial em arquivos reutilizáveis… Seleção de modelo e detalhes de interface são temporais e precisam ser verificados."* **Confere:** sim.
**Alegações** — "usar Cowork, não chat, para arquivos reais" e a seleção de modelo: ALEGAÇÃO DO AUTOR, **temporal**, `NÃO VERIFICADA`.
**Vetos** — **V2 · V4 sim**; demais não.
**RF = REFERÊNCIA** — §9, insumo de consulta com `LV ≥ 3`.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-10-PRT-006 — `Captura de tela 2026-07-28 180038.png` · 63 formas de usar IA na empresa

**Hash F0 / reconferido:** `68952CF377C92DA4` · **Confere:** sim · **LV:** LV3-V · **Cobertura:** inspeção visual pela trilha Codex (`109`) · **Data:** 2026-07-29 · **Origem Codex:** `H-P1-003` (`109`)

**Bloco A** — `E02 = 1`: **só listagem**, ainda que ampla — matriz de casos de uso por sete funções empresariais. `109` confirma "como inventário de oportunidades". · `E03 · E05 · E06 · E07 · E13 = ND`. · `E15 ⚠ = 1`: "63 usos" é contagem apresentada como valor; o catálogo registra que ela "não informa impacto, frequência, dados exigidos nem risco".
**NF = 1 · 2/7 · 5 ND**

**Bloco B** — `E01 = 3` (endereça diretamente: é o inventário por função de negócio, que é o lado "quais verticais" da pergunta da área) · `E04 = 2` (adaptação não declarada: sem critério de priorização) · `E14 = 2` (conveniência sobre inventário já acessível; sobrepõe `AC-10-VID-012`, que traz cem). **RP = 2 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND** (§3.3)

**Catálogo** — **NC = 3**: o mapa de departamentos e casos de uso confere; **CONFIRMADA** em `109`. *"**Ressalva:** '63 usos' não informa impacto, frequência, dados exigidos nem risco; priorizar por volume × repetição × reversibilidade e exigir revisão humana nos usos de pessoas, finanças e comunicação externa."* **Confere:** sim.
**Alegações** — "63 formas": ALEGAÇÃO DO AUTOR — contagem **não conferida por esta frente**; `109` não a recontou.
**Vetos** — **V2 · V4 sim**; demais não.
**RF = REFERÊNCIA** — §9, insumo de consulta com `LV ≥ 3`.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-10-PRT-007 — `Captura de tela 2026-07-28 203019.png` · dez prompts de pesquisa de mercado

**Hash F0 / reconferido:** `2BC80F67A3DDE95F` · **Confere:** sim · **LV:** LV3-V · **Cobertura:** inspeção visual pela trilha Codex (`109`) · **Data:** 2026-07-29 · **Origem Codex:** `H-P1-003` (`109`)

**Bloco A** — `E02 = 2`: descrição com detalhe reproduzível — **dez papéis nomeados em sequência ordenada**, de varredura de mercado a estrutura de produto, o que faz do conjunto um pipeline e não uma lista solta. `109` confirma os dez temas e estruturas. · `E03 · E05 · E06 · E07 · E13 = ND`. · `E15 ⚠ = 1`: os nomes de papel prometem resultado — "Profit Validation", "Competition Gap" — sem fonte, critério de evidência ou validação de demanda; `109` registra que "resultados e fontes exigem validação".
**NF = 1 · 2/7 · 5 ND** *(mediana [1,2] = 1,5 → §14.3)*

**Bloco B** — `E01 = 3` (endereça diretamente: é pesquisa **antes** de escolher a vertical) · `E04 = 2` (adaptação não declarada: os prompts em si não estão no print) · `E14 = 2` (conveniência). **RP = 2 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND** (§3.3)

**Catálogo** — **NC = 3**: os dez papéis, nomeados, conferem; **CONFIRMADA** em `109`. *"**O que extrair:** pipeline de pesquisa antes da produção: mercado → público → concorrência → proposta → viabilidade → blueprint. **Ressalva:** nomes de prompt não substituem fontes, critérios de evidência ou validação de demanda real."* **Confere:** sim.
**Alegações** — "Profit Validation" como etapa que valida lucro: ALEGAÇÃO DO AUTOR, `NÃO VERIFICADA`.
**Vetos** — **V2 · V4 sim**; demais não.
**RF = REFERÊNCIA** — §9, insumo de consulta com `LV ≥ 3`.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

> **Série `workkflow conteudo` — `AC-10-PRT-008` a `AC-10-PRT-015`.** Oito arquivos, contador exibido de **1/9 a 8/9**, medido por `109`. **O slide 9 não está no acervo.** Todas as oito fichas compartilham: LV3-V por `109`; `E03 · E05 · E06 · E07 · E13 = ND` pelas mesmas razões (origem e data, canal datado, inspeção direta, autoria e termos, nenhuma verificação exibida); Bloco C fixo §3.3; `V2` e `V4` disparam; hash confere. Só variam `E02`, `E15` e o Bloco B — que é o que cada ficha registra.

### AC-10-PRT-008 — `_redes-sociais/workkflow conteudo0.png` · capa · **slide 1/9**

**Hash F0 / reconferido:** `6DAFE579A904D6AB` · **Confere:** sim · **LV:** LV3-V · **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`109`) · **Origem Codex:** `H-P1-003` (`109`) · **Data:** 2026-07-29

**Bloco A** — `E02 = 1`: **só promessa** — capa com "um sistema / conteúdo infinito / crescimento composto". Nenhum conteúdo operacional. · `E15 ⚠ = 1`: "conteúdo infinito" e "crescimento composto" são alegações de resultado sem qualquer medida.
**NF = 1 · 2/7 · 5 ND** · **Bloco B** — `E01 = 2` · `E04 = 1` (só a ideia viaja, e a ideia é a promessa) · `E14 = 1`. **RP = 1 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND**

**Catálogo** — **NC = 2 — PARCIAL.** `109`: "Capa e promessa conferem, **mas o contador visível é 1/9**. O catálogo chama a série de 'carrossel de 8 slides'. Há oito arquivos capturados, cobrindo 1/9 a 8/9; **o slide 9 está ausente**." Detalhe não confirmado ⇒ teto 2 (§14.4). A divergência é **de contagem da série**, e a lacuna é do acervo.
**Alegações** — "Um sistema / conteúdo infinito / crescimento composto": ALEGAÇÃO DO AUTOR, `NÃO VERIFICADA`. · "carrossel de 8 slides": ALEGAÇÃO DO CATÁLOGO — **contradita pelo contador exibido**.
**Vetos** — **V2 · V4 sim**; demais não; hash confere.
**RF = REFERÊNCIA** — §9, insumo de consulta com `LV ≥ 3`.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-10-PRT-009 — `workkflow conteudo1.png` · o pipeline · **slide 2/9**

**Hash F0 / reconferido:** `CF8563E00B687FEB` · **Confere:** sim · **LV:** LV3-V · **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`109`) · **Origem Codex:** `H-P1-003` (`109`) · **Data:** 2026-07-29

**Bloco A** — `E02 = 2`: descrição com detalhe reproduzível — **oito etapas nomeadas em ciclo fechado**, com a análise realimentando a pesquisa. `109` confirma a sequência inteira. · `E15 ⚠ = 1`: o ciclo é apresentado como funcionando, sem nenhum resultado medido.
**NF = 1 · 2/7 · 5 ND** *(mediana [1,2] = 1,5 → §14.3)* · **Bloco B** — `E01 = 3` (endereça diretamente: é desenho de fluxo de produção) · `E04 = 3` (as oito etapas transferem sem depender de ferramenta) · `E14 = 3` (**o catálogo identifica este slide como arquitetura disfarçada de marketing**, e a leitura confere: laço fechado com realimentação não aparece assim em nenhum outro item da área). **RP = 3 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND**

**Catálogo** — **NC = 3**: "Research→Ideas→Hooks→Draft→Rewrite→Post→Analyze→Repeat confere; contador 2/9" (`109`). **CONFIRMADA.** *"**O que extrair:** os slides 1, 3 e 5 são desenho de arquitetura disfarçado de marketing… o slide 1 fecha o loop com analytics realimentando a entrada."* **Confere:** sim.
**Vetos** — **V2 · V4 sim**; demais não.
**RF = REFERÊNCIA** — §9, insumo de consulta com `LV ≥ 3`.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-10-PRT-010 — `workkflow conteudo2.png` · fontes de pesquisa · **slide 3/9**

**Hash F0 / reconferido:** `0D6195AEB9E3E3E0` · **Confere:** sim · **LV:** LV3-V · **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`109`) · **Origem Codex:** `H-P1-003` (`109`) · **Data:** 2026-07-29

**Bloco A** — `E02 = 2`: detalhe reproduzível — **sete fontes de pesquisa nomeadas**, todas acessíveis, mais a regra de entrada e a síntese "great content is found, not invented". `109` confirma as sete. · `E15 ⚠ = 1`: "*garbage in, garbage out*" e a síntese são afirmações sem medida.
**NF = 1 · 2/7 · 5 ND** *(§14.3)* · **Bloco B** — `E01 = 2` (endereça a pergunta de forma genérica: é etapa de um fluxo, não empacotamento por domínio) · `E04 = 3` (as sete fontes transferem literalmente) · `E14 = 2` (conveniência sobre conhecimento acessível). **RP = 2 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND**

**Catálogo** — **NC = 3**: as sete fontes conferem; **CONFIRMADA** em `109`, com o contador 3/9 registrado. **Confere:** sim.
**Alegações** — "great content is found, not invented": ALEGAÇÃO DO AUTOR, `NÃO VERIFICADA`.
**Vetos** — **V2 · V4 sim**; demais não.
**RF = REFERÊNCIA** — §9, insumo de consulta com `LV ≥ 3`.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-10-PRT-011 — `workkflow conteudo3.png` · fan-out · **slide 4/9**

**Hash F0 / reconferido:** `4C2C62E56412FEE8` · **Confere:** sim · **LV:** LV3-V · **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`109`) · **Origem Codex:** `H-P1-003` (`109`) · **Data:** 2026-07-29

**Bloco A** — `E02 = 2`: detalhe reproduzível — **um tópico de entrada e a lista completa das saídas**: dez ganchos, cinco ideias de carrossel, cinco de vídeo curto, newsletter, sequência, publicação profissional, roteiro e isca. `109` confirma todas as saídas. · `E15 ⚠ = 1`: "30+ peças" é contagem apresentada como resultado, sem demonstração de que as peças se sustentam.
**NF = 1 · 2/7 · 5 ND** *(§14.3)* · **Bloco B** — `E01 = 3` (endereça diretamente) · `E04 = 3` (o padrão transfere: uma entrada canônica dispara N gerações) · `E14 = 3` (**o catálogo o nomeia padrão de fan-out**, e a leitura confere: é o desenho de "cada formato uma skill", que reaparece como artefato em `AC-10-REP-004` e `AC-10-REP-005`). **RP = 3 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND**

**Catálogo** — **NC = 3**: as saídas conferem; **CONFIRMADA** em `109`, contador 4/9. *"O slide 3 é o padrão **fan-out** (um input canônico dispara N gerações paralelas, cada formato uma skill)."* **Confere:** sim.
**Vetos** — **V2 · V4 sim**; demais não.
**RF = REFERÊNCIA** — §9, insumo de consulta com `LV ≥ 3`.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-10-PRT-012 — `workkflow conteudo4.png` · cinco fórmulas de gancho · **slide 5/9**

**Hash F0 / reconferido:** `954814C87819562F` · **Confere:** sim · **LV:** LV3-V · **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`109`) · **Origem Codex:** `H-P1-003` (`109`) · **Data:** 2026-07-29

**Bloco A** — `E02 = 2`: detalhe reproduzível — **cinco fórmulas nomeadas, cada uma com exemplo literal**. `109` confirma as cinco com exemplos. · `E15 ⚠ = 1`: os próprios exemplos contêm alegações fortes — "salvo 10+ horas por semana", "99% das pessoas não sabem disto" — exibidas como modelo de gancho, isto é, **como técnica de persuasão, não como fato**. Registrado nessa camada.
**NF = 1 · 2/7 · 5 ND** *(§14.3)* · **Bloco B** — `E01 = 2` (genérico) · `E04 = 3` (as cinco fórmulas transferem literalmente) · `E14 = 1` (conveniência sobre conhecimento amplamente acessível: fórmulas de gancho são material comum de copy). **RP = 2 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND**

**Catálogo** — **NC = 3**: as cinco fórmulas com exemplos conferem; **CONFIRMADA** em `109`, contador 5/9. O catálogo classifica este slide como copy de venda, não arquitetura — leitura coerente com o observado. **Confere:** sim.
**Alegações** — os exemplos de gancho são **exemplos**, não afirmações do autor sobre o mundo; registrados como tal.
**Vetos** — **V2 · V4 sim**; demais não.
**RF = REFERÊNCIA** — §9, insumo de consulta com `LV ≥ 3`.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-10-PRT-013 — `workkflow conteudo5.png` · distribuição · **slide 6/9**

**Hash F0 / reconferido:** `C4354993F8570813` · **Confere:** sim · **LV:** LV3-V · **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`109`) · **Origem Codex:** `H-P1-003` (`109`) · **Data:** 2026-07-29

**Bloco A** — `E02 = 2`: detalhe reproduzível — **uma peça canônica e seis saídas por plataforma**, com a regra "mude o formato, não a mensagem". `109` confirma a peça-base e as seis saídas. · `E15 ⚠ = 1`: a regra é afirmada sem medição de alcance ou desempenho por formato.
**NF = 1 · 2/7 · 5 ND** *(§14.3)* · **Bloco B** — `E01 = 3` (endereça diretamente) · `E04 = 3` (transfere como camada de adaptadores de saída) · `E14 = 3` (**o catálogo o nomeia camada de adaptadores por plataforma**; junto com os slides 2/9 e 4/9, forma o trio que ele identifica como arquitetura). **RP = 3 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND**

**Catálogo** — **NC = 3**: **CONFIRMADA** em `109`, contador 6/9. *"o slide 5 é a camada de **adaptadores de saída por plataforma**."* **Confere:** sim.
**Vetos** — **V2 · V4 sim**; demais não.
**RF = REFERÊNCIA** — §9, insumo de consulta com `LV ≥ 3`.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-10-PRT-014 — `workkflow conteudo6.png` · sem sistema × com sistema · **slide 7/9**

**Hash F0 / reconferido:** `5555F0AC7FAF6158` · **Confere:** sim · **LV:** LV3-V · **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`109`) · **Origem Codex:** `H-P1-003` (`109`) · **Data:** 2026-07-29

**Bloco A** — `E02 = 1`: **contraste retórico** — três dores de um lado, três benefícios do outro — mais uma redução do pipeline a cinco passos. `109` confirma o contraste e o pipeline reduzido. O catálogo classifica como copy de venda. · `E15 ⚠ = 1`: "fluxo consistente, ideias sob demanda, mais tempo" são resultados afirmados sem medida.
**NF = 1 · 2/7 · 5 ND** · **Bloco B** — `E01 = 2` (genérico) · `E04 = 2` (o pipeline de cinco passos é versão empobrecida do slide 2/9) · `E14 = 1` (conveniência; sobrepõe `AC-10-PRT-009`). **RP = 2 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND**

**Catálogo** — **NC = 3**: **CONFIRMADA** em `109`, contador 7/9. O catálogo o classifica entre "os slides 0, 4 e 6 são copy de venda" — juízo coerente com o observado. **Confere:** sim.
**Vetos** — **V2 · V4 sim**; demais não.
**RF = REFERÊNCIA** — §9, insumo de consulta com `LV ≥ 3`.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-10-PRT-015 — `workkflow conteudo7.png` · automação · **slide 8/9 · último do acervo**

**Hash F0 / reconferido:** `7DF45C13DF675E65` · **Confere:** sim · **LV:** LV3-V · **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`109`) · **Origem Codex:** `H-P1-003` (`109`) · **Data:** 2026-07-29

**Bloco A** — `E02 = 1`: **só listagem** — seis classes de automação nomeadas. · `E15 ⚠ = 1`: "**automatize 80% do trabalho repetitivo**" e "10+ horas" são alegações numéricas fortes; `109` confirma que estão no texto visível, e **confirmar que o texto existe não é confirmar que o número é verdadeiro**. Sem fonte e sem método.
**NF = 1 · 2/7 · 5 ND** · **Bloco B** — `E01 = 2` (genérico) · `E04 = 2` · `E14 = 1`. **RP = 2 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND**

**Catálogo** — **NC = 3**: "Seis classes de automação e alegações de 80%/10+ horas conferem **como texto visível**" (`109`) — a formulação do relatório é exata e foi preservada. **CONFIRMADA**, contador 8/9. **Confere:** sim.
**Alegações** — "Automatize 80% do trabalho repetitivo": ALEGAÇÃO DO AUTOR, sem fonte, `NÃO VERIFICADA`. · **`V7` avaliada, não disparou**: `E15 = 1`, não 0 — a relevância do slide está nas seis classes de automação, que existem independentemente do número.
**Vetos** — **V2 · V4 sim**; demais não.
**RF = REFERÊNCIA** — §9, insumo de consulta com `LV ≥ 3`.

> **Fecha a série.** Os oito arquivos cobrem os slides 1/9 a 8/9; **o slide 9 permanece ausente do acervo** — lacuna registrada, não suprida por inferência.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-10-PRT-016 — `_renda-extra/dores.png` · gráfico "Humanos + IA"

**Tipo:** PRINT · **Área:** 10_APLICACOES-DE-NEGOCIO
**Hash F0:** `55BA1338BCB6123E`   **Hash reconferido:** `55BA1338BCB6123E`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`109`), **que recontou as linhas do gráfico**.
**Data:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** `H-P1-003` (relatório `109`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 | 1 | **Só um gráfico de barras com números** — tempo de conclusão com e sem IA, por tarefa. Nenhuma metodologia, nenhuma amostra, nenhuma definição de tarefa, nenhum intervalo de confiança. `109` é literal: "**Não há fonte nem método**" | — |
| E03 · E05 · E06 · E07 · E13 | ND | — | Origem e data do estudo; canal datado; inspeção direta; autoria e termos; nenhuma verificação |
| **E15** ⚠ | **0** | **A proposta central do item depende inteiramente de alegação numérica forte, sem fonte e não verificável.** O item **é** a tabela de números: 17 pares de valores em minutos, dos quais o catálogo transcreveu nove. Sem estudo nomeado, sem método e sem definição operacional de tarefas como "Pensamento Crítico", nada nele é conferível — e não sobra conteúdo além dos números | — |

**NF = 0 · 2/7 · 5 ND** *(mediana dos determinados [0,1] = 0,5 → §14.3 vale o inferior)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E01 | 3 | Endereça diretamente a pergunta central: onde o ganho percebido é maior é exatamente "que vertical provar primeiro" — **e é por isso que o item é perigoso**: sua relevância depende dos números que ninguém pode conferir | — |
| E04 | 1 | Só a ideia viaja: sem método, os deltas não se reproduzem em outro contexto | — |
| E14 | 1 | Conveniência sobre conhecimento amplamente acessível | — |

**RP = 1 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND** (§3.3)

#### Catálogo
**NC = 2 — PARCIAL, com omissão medida.** `109`: "Os nove valores catalogados e os três maiores deltas **conferem**, mas o gráfico tem **17 tarefas, não nove**. Foram omitidas Aprendizagem Ativa, Resolução de Problemas, Julgamento e Tomada de Decisão, Gestão de Recursos Materiais, Matemática, Instrução, Análise de Operações e Gestão de Pessoal." O catálogo apresentou **um recorte como se fosse a tabela**, e o recorte é dos maiores deltas — o que **reforça a conclusão que ele extrai**. `109` registra a correção necessária: "a tabela atual é recorte dos nove maiores interesses editoriais, não transcrição completa". Detalhe não confirmado ⇒ teto 2 (§14.4).
**O que o catálogo afirma:** "**O que extrair:** os três maiores deltas — design de tecnologia, programação e resolução de problema complexo — são onde o valor percebido é maior. Se o produto precisa provar valor rápido, é por aí. **Ressalva:** a imagem não traz metodologia nem fonte do estudo. Trate como indicativo, não como dado."
**Confere:** **parcialmente** — os nove valores conferem; **a completude, não**

#### Alegações registradas
| Alegação | Origem | Camada | Verificada? |
|---|---|---|---|
| os 17 pares de valores em minutos, com e sem IA | print, via `109` | ALEGAÇÃO DO AUTOR — **sem estudo nomeado** | **não, e não verificável com o material disponível** — sustenta `E15 = 0` |
| "os três maiores deltas… são onde o valor percebido é maior" | `_CONTEUDO.md` área 10 | **INFERÊNCIA do catálogo sobre alegação não verificada** | **não** — a inferência herda a fragilidade da base, e foi extraída de um recorte de 9 das 17 linhas |
| "Trate como indicativo, não como dado." | `_CONTEUDO.md` área 10 | ALEGAÇÃO DO CATÁLOGO — ressalva correta | registrada — o catálogo **desqualifica a própria fonte** e ainda assim extrai conclusão dela |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V8 | não | `E06 = ND` (não 0) · `E07 = ND` (não 0) · `LV = 3` · 5 ND < 8 · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |
| **V7** | **sim** | `E15 = 0` **e a relevância do item depende inteiramente dessa alegação** → teto EXIGE PESQUISA |

#### Resultado
**RF = EXIGE PESQUISA**
**Regra que produziu:** **V7** — é a porta que manda, e ela é decisiva aqui: o item **é** a alegação. §9 confirma a condição de entrada — há relevância aparente e uma lacuna nomeada e endereçável.
**Se EXIGE PESQUISA — lacuna nomeada:** **o estudo de origem** — quem mediu, com que amostra, com que definição de tarefa e em que período; e a **transcrição completa das 17 linhas**, já que a tabela em uso no acervo é um recorte de nove.  **Verificação que a fecharia:** identificar a publicação de origem do gráfico e reler a imagem transcrevendo as 17 linhas — a segunda parte é operação de minutos e **corrige um erro que já está circulando dentro do acervo**.

> **É o único dos 16 PRINT desta área que não termina em REFERÊNCIA** — contado por ferramenta sobre o arquivo. No acervo inteiro há outros doze prints em EXIGE PESQUISA, das áreas 01 a 06.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

## Lote L-24 — VÍDEO 001 a 012

> **Nota de aplicação aos 23 VÍDEO desta área.** LV3-V vem de `H-M2-006` (relatório `103`); LV3-A, quando existe, do manifesto `117`. **LV3-V + LV3-A não produz LV4**; transcrição automática **não autoriza citação exata**. **V5 não é aplicado automaticamente a vídeo.** Bloco C segue o valor fixo do índice §3.3 (`3 · 5 · 4 · 5 · 4 → AA = 4 · 5/5 · 0 ND`) e não é repetido em cada ficha. `E03 · E05 · E07 · E13 = ND` em **todos** os 23, pelas mesmas razões (origem e data; canal datado; autoria e termos; nenhuma verificação exibida); `E06 = ND` salvo onde a ficha registrar nota, e cada nota vem com a evidência que a sustenta. `V4` dispara em todos.
>
> **Fala aproveitável em 8 dos 23**: `002`, `003`, `006`, `008`, `016`, `021`, `022` em ALTA AUTOMÁTICA e `023` em **MÉDIA AUTOMÁTICA** — o único do acervo nesse estado, e por isso o de menor confiança entre os que têm fala. Os outros quinze não têm narração confiável.

### AC-10-VID-001 — `Gravando 2026-07-28 154241.mp4` · antes e depois da IA
**Hash F0:** `06A62BC09DFAB1B8`   **Hash reconferido:** `06A62BC09DFAB1B8`   **Confere:** sim   **LV:** **LV3-V**
**Cobertura da leitura:** 18,2 s, `es`, 1 palavra, confiança 1,000, **SEM FALA LEXICAL CONFIÁVEL** (`117`) · quadros por `103` · 2026-07-29
**A:** `E02 = 1` — só contraste de ícones, ferramenta a ferramenta; `103` registra que "alguns ícones ficaram desfocados" e que o item "não demonstra qualidade, custo ou superioridade". `E15 ⚠ = 1` — substituição afirmada sem qualquer comparação. **NF = 1 · 2/7 · 5 ND**
**B:** `E01 = 2` (genérico) · `E04 = 1` (só a ideia) · `E14 = 1`. **RP = 1 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND** (§3.3)
**Catálogo — NC = 5:** título pelo conteúdo visível ("apresentações, pesquisas e sites antes e depois da IA") **confirmado** por `103`. **Confere:** sim.
**Alegações:** a superioridade implícita das cinco ferramentas de IA — ALEGAÇÃO DO AUTOR, `NÃO VERIFICADA`.
**Vetos:** **V2 · V4 sim** (`E06 = ND`, `E07 = ND`); V5 não aplicado (`LV = 3`); demais não. **RF = REFERÊNCIA** (§9; `RP = 1`).

### AC-10-VID-002 — `Gravando 2026-07-28 155209.mp4` · processamento documental
**Hash F0:** `B11867F9A2EDA07B`   **Hash reconferido:** `B11867F9A2EDA07B`   **Confere:** sim   **LV:** **LV3-V + LV3-A**
**Cobertura da leitura:** 67,1 s, `pt`, 205 palavras, 20 segmentos, 0,892, ALTA AUTOMÁTICA (`117`) · quadros por `103` · 2026-07-29
**A:** `E02 = 2` — demonstração com objeto identificável: `103` descreve repositório na tela e **conversão de PDF, DOCX, PPTX e HTML para formatos estruturados**, mais teste com um arquivo real. `E15 ⚠ = 1` — nenhuma medida de fidelidade, OCR ou preservação de tabela; `103` exige "confirmar origem, licença, OCR, preservação de tabelas, segurança e benchmark". **NF = 1 · 2/7 · 5 ND** *(§14.3)*
**B:** `E01 = 3` (endereça diretamente: ingestão documental é pré-requisito de qualquer vertical) · `E04 = 2` · `E14 = 3` (**camada de ingestão documental não tem equivalente no acervo**). **RP = 3 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND**
**Catálogo — NC = 0 — DIVERGENTE.** O catálogo declara, como título pelo conteúdo visível: "**agente/chatbot de vendas atuando como vendedor**". A inspeção de quadros mostra **outra coisa**: uma biblioteca de conversão de documentos, com repositório e teste de arquivo. Não há vendedor, não há conversa comercial nos quadros. **Confere:** **não**.
> Divergência **de catálogo**, não de fonte: hash confere, **V8 não dispara**. Rebaixa `NC` a 0 (§3.5) e fica registrada. `NC` nunca entra em `NF`.
**Alegações:** o repositório exibido — ALEGAÇÃO DO AUTOR sobre origem, **não conferida**: o item está **fora do acervo** e não foi baixado. · "agente/chatbot de vendas" — **ALEGAÇÃO DO CATÁLOGO, contradita pela inspeção**.
**Vetos:** **V2 · V4 sim**; V5 não aplicado; demais não. **RF = REFERÊNCIA** (§9).

### AC-10-VID-003 — `Gravando 2026-07-28 155428.mp4` · conta de retorno em social media
**Hash F0:** `B1BD4D087C66E41C`   **Hash reconferido:** `B1BD4D087C66E41C`   **Confere:** sim   **LV:** **LV3-V + LV3-A**
**Cobertura da leitura:** **110,3 s — o vídeo mais longo da área** ·`pt`, 319 palavras, 5 segmentos, 0,850, ALTA AUTOMÁTICA (`117`) · quadros por `103` · 2026-07-29
**A:** `E02 = 1` — três números numa tela e uma pergunta; `103`: "Valores, causalidade, período e atribuição são desconhecidos". `E15 ⚠ = 1` — "3.000 / 250 / 73.000" é razão de retorno exibida **sem período, sem atribuição e sem contrafactual**. **NF = 1 · 2/7 · 5 ND**
**B:** `E01 = 2` (genérico) · `E04 = 1` · `E14 = 1`. **RP = 1 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND**
**Catálogo — NC = 5:** título pelo conteúdo visível ("orçamento de social media, ajuda de custo e retorno financeiro") **confirmado** por `103`, inclusive nos três valores. **Confere:** sim.
**Alegações:** retorno de 73.000 sobre 3.250 — ALEGAÇÃO DO AUTOR, `NÃO VERIFICADA`; **a atribuição causal é o que falta, não o número**.
**Vetos:** **V2 · V4 sim**; **V7 avaliada, não disparou** (`E15 = 1`, não 0: há fonte — a tela —, apenas não conferível). **RF = REFERÊNCIA** (§9; `RP = 1`).

### AC-10-VID-004 — `Gravando 2026-07-28 163030.mp4` · skills de marketing por departamento
**Hash F0:** `C505946ECDDA9090`   **Hash reconferido:** `C505946ECDDA9090`   **Confere:** sim   **LV:** **LV3-V**
**Cobertura da leitura:** 23,1 s, `en`, 1 palavra, 0,751, SEM FALA LEXICAL CONFIÁVEL (`117`) · quadros por `103` · 2026-07-29
**A:** `E02 = 1` — listagem: **33 skills distribuídas em sete departamentos**, com funções nomeadas. `E15 ⚠ = 1` — a contagem e a cobertura são exibidas sem fonte; `103` adverte "não instalar como pacote… requer métricas, fontes e gates por efeito". **NF = 1 · 2/7 · 5 ND**
**B:** `E01 = 3` (endereça diretamente: é taxonomia por função de negócio) · `E04 = 2` · `E14 = 2` (**sobreposição registrada**: `103` observa que "sobrepõe a área 05", e o pacote correspondente está no acervo como `AC-10-REP-004`, com artefato). **RP = 2 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND**
**Catálogo — NC = 5:** título pelo conteúdo visível ("departamentos de skills de marketing: SEO, anúncios, vendas e GTM") **confirmado** por `103`. **Confere:** sim.
**Vetos:** **V2 · V4 sim**. **RF = REFERÊNCIA** (§9).

### AC-10-VID-005 — `Gravando 2026-07-28 165415.mp4` · central de decisão
**Hash F0:** `FA4BBA01520E2B6B`   **Hash reconferido:** `FA4BBA01520E2B6B`   **Confere:** sim   **LV:** **LV3-V**
**Cobertura da leitura:** 20,7 s, `en`, 1 palavra, confiança **0,130**, SEM FALA LEXICAL CONFIÁVEL (`117`) · quadros por `103` · 2026-07-29
**A:** `E02 = 2` — detalhe reproduzível: fluxo **dados → organização/insights/alertas → visualização → decisão**, com **cinco blocos nomeados** (indicadores, alertas, tendências, diagnóstico, próxima ação). `103` chama de "achado alto". `E15 ⚠ = 1` — nenhuma medida; `103` adverte que "IA não deve fabricar causas" e que decisões exigem dado reconciliado, confiança e responsável. **NF = 1 · 2/7 · 5 ND** *(§14.3)*
**B:** `E01 = 3` · `E04 = 3` (as cinco perguntas que um painel deve responder transferem sem ferramenta) · `E14 = 3` (o desenho "o que ocorreu, desviou, arrisca, merece atenção e vem depois" não aparece assim em nenhum outro item). **RP = 3 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND**
**Catálogo — NC = 5:** título pelo conteúdo visível ("central de operação com Claude + Power BI para decisão") **confirmado** por `103`. **Confere:** sim.
**Vetos:** **V2 · V4 sim**. **RF = REFERÊNCIA** (§9).

### AC-10-VID-006 — `Gravando 2026-07-28 181253.mp4` · skills de construção de marca
**Hash F0:** `C962CEC5810B5D23`   **Hash reconferido:** `C962CEC5810B5D23`   **Confere:** sim   **LV:** **LV3-V + LV3-A**
**Cobertura da leitura:** 41,7 s, `pt`, 138 palavras, 18 segmentos, 0,857, ALTA AUTOMÁTICA (`117`) · quadros por `103` · 2026-07-29
**A:** `E02 = 1` — listagem de skills interligadas (contexto, estratégia, nomeação, posicionamento, identidade, voz, diretrizes, auditoria, relançamento, concorrência, e-mail, influenciadores), sem demonstração. **`E06` ⚠ = 1** — **risco declarado por terceiro, não confirmado**: `103` registra que "identidade, licença, qualidade e **comando `npx skills add`** não foram validados; **não instalar**". O comando de instalação por execução de pacote remoto **está na tela**; o que ele instala não foi inspecionado. `E15 ⚠ = 1` — cobertura afirmada sem fonte. **NF = 1 · 3/7 · 4 ND**
**B:** `E01 = 3` · `E04 = 2` · `E14 = 2` (sobrepõe `AC-10-REP-004`/`005` e a área 05). **RP = 2 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND**
**Catálogo — NC = 5:** título pelo conteúdo visível ("biblioteca de skills de marketing com contexto de marca") **confirmado** por `103`, inclusive quanto à skill de contexto. **Confere:** sim.
**Vetos:** V1 não (`E06 = 1`, não 0) · **V2 sim** (`E06 = 1`) · **V4 sim** · demais não. **RF = REFERÊNCIA** (§9).
> **Registro de risco, sem ação.** Nada foi baixado, instalado ou executado.

### AC-10-VID-007 — `Gravando 2026-07-28 204425.mp4` · seis painéis empresariais
**Hash F0:** `4157EBDAC6BB43A2`   **Hash reconferido:** `4157EBDAC6BB43A2`   **Confere:** sim   **LV:** **LV3-V**
**Cobertura da leitura:** 18,2 s, `en`, 1 palavra, 0,751, SEM FALA LEXICAL CONFIÁVEL (`117`) · quadros por `103` · 2026-07-29
**A:** `E02 = 2` — detalhe reproduzível: **seis painéis nomeados** — vendas, financeiro, cobrança, crise, pessoas, executivo — **cada um com seus indicadores** (receita e meta e funil; caixa e resultado; envelhecimento e recuperação; ponto de equilíbrio e fôlego de caixa; quadro, rotatividade e absenteísmo; visão por semáforo). `E15 ⚠ = 1` — `103`: "Métricas e dados ilustrativos não são evidência operacional". **NF = 1 · 2/7 · 5 ND** *(§14.3)*
**B:** `E01 = 3` · `E04 = 3` (a lista de indicadores por painel transfere) · `E14 = 3` (`103` chama de "mapa de perguntas"; é o mais completo da família de painéis). **RP = 3 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND**
**Catálogo — NC = 5:** título pelo conteúdo visível ("dashboards executivos de finanças, cobrança e pessoas") **confirmado** por `103`, que observa **mais** painéis do que o título cita — acréscimo, não contradição. **Confere:** sim.
**Vetos:** **V2 · V4 sim**. **RF = REFERÊNCIA** (§9).

### AC-10-VID-008 — `Gravando 2026-07-28 213549.mp4` · ecossistema de conectores
**Hash F0:** `980922B24450ED62`   **Hash reconferido:** `980922B24450ED62`   **Confere:** sim   **LV:** **LV3-V + LV3-A**
**Cobertura da leitura:** 54,0 s, `en`, 145 palavras, 20 segmentos, **0,916 — a maior confiança de STT desta área** (`117`) · quadros por `103` · 2026-07-29
**A:** `E02 = 1` — `103` registra **ficha parcial**: o visual mostra um ecossistema de ícones e "apenas 'Chrome MCP' fica nomeado com clareza", com a instrução explícita de **não inferir nomes pelos ícones**. `E15 ⚠ = 1` — a promessa de "cinco" conectores não é verificável nos quadros. **NF = 1 · 2/7 · 5 ND**
**B:** `E01 = 2` · `E04 = 1` · `E14 = 1` (a área 06 do acervo cobre conectores com 40 itens). **RP = 1 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND**
**Catálogo — NC = 2 — PARCIAL.** O catálogo declara "agentes para scraping, benchmarking, contratos e segurança"; os quadros mostram um **ecossistema de conectores** com um único nome legível. As duas leituras não se contradizem frontalmente, mas **o organizador do conteúdo é outro**, e o detalhe do catálogo não se confirma (§14.4).
**Alegações:** "cinco MCP servers" — ALEGAÇÃO DO AUTOR, **não conferida**; `103` proíbe inferir os nomes pelos ícones, e esta ficha **não os infere**.
**Vetos:** **V2 · V4 sim**. **RF = REFERÊNCIA** (§9; `RP = 1`).

### AC-10-VID-009 — `Gravando 2026-07-28 214422.mp4` · sete painéis com IA
**Hash F0:** `E54754AD9477F830`   **Hash reconferido:** `E54754AD9477F830`   **Confere:** sim   **LV:** **LV3-V**
**Cobertura da leitura:** 16,2 s, `en`, 1 palavra, confiança **0,130**, SEM FALA LEXICAL CONFIÁVEL (`117`) · quadros por `103` · 2026-07-29
**A:** `E02 = 1` — listagem de painéis; `103` registra que "**um painel não foi capturado**". `E15 ⚠ = 1` — "criar em minutos" e os números exibidos são, no registro de `103`, "promocionais/não verificados". **NF = 1 · 2/7 · 5 ND**
**B:** `E01 = 2` · `E04 = 2` · `E14 = 1` (**sobrepõe `AC-10-VID-007`**, que é mais completo). **RP = 2 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND**
**Catálogo — NC = 2 — PARCIAL.** O catálogo declara "dashboards de finanças, **logística** e produção"; os quadros mostram financeiro, vendas, marketing, pessoas, produção e executivo — **logística não foi observada**, e três dos painéis observados não estão no título. Detalhe não confirmado ⇒ teto 2 (§14.4).
**Vetos:** **V2 · V4 sim**. **RF = REFERÊNCIA** (§9).

### AC-10-VID-010 — `Gravando 2026-07-29 085629.mp4` · casos de uso com prompts iniciais
**Hash F0:** `DCB72717037106DE`   **Hash reconferido:** `DCB72717037106DE`   **Confere:** sim   **LV:** **LV3-V**
**Cobertura da leitura:** 15,6 s, `en`, 1 palavra, confiança **0,130**, SEM FALA LEXICAL CONFIÁVEL (`117`) · quadros por `103` · 2026-07-29
**A:** `E02 = 1` — listagem de casos com prompt inicial; `103` observou **oito**, com "um caso não apareceu". **`E06` ⚠ = 1** — **risco declarado por terceiro, não confirmado**: `103` nomeia "IP na clonagem, execução longa, finanças, **dados bancários** e publicação". Um dos casos exibidos é **clonagem local de aplicativo de terceiro**, outro envolve dado financeiro. `E15 ⚠ = 1` — `103`: "prompts não provam resultados". **NF = 1 · 3/7 · 4 ND**
**B:** `E01 = 2` · `E04 = 2` · `E14 = 1`. **RP = 2 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND**
**Catálogo — NC = 2 — PARCIAL.** O catálogo declara "**onze** casos de uso"; a inspeção de quadros observou **oito**, e `103` não afirma o total. A contagem **não se confirma** — pode ser amostragem de quadros, e por isso é PARCIAL e não DIVERGENTE (§14.4).
**Vetos:** V1 não · **V2 sim** (`E06 = 1`) · **V4 sim** · demais não. **RF = REFERÊNCIA** (§9).
> **Registro de risco, sem ação.** Clonagem de aplicativo de terceiro é questão de propriedade intelectual, não de capacidade técnica. Registrada, não avaliada.

### AC-10-VID-011 — `Gravando 2026-07-29 085700.mp4` · papéis de direção
**Hash F0:** `DBE4D7F496C46231`   **Hash reconferido:** `DBE4D7F496C46231`   **Confere:** sim   **LV:** **LV3-V**
**Cobertura da leitura:** **6,7 s — o vídeo mais curto do acervo** · `en`, 1 palavra, 0,751, SEM FALA LEXICAL CONFIÁVEL (`117`) · quadros por `103` · 2026-07-29
**A:** `E02 = 1` — matriz densa de responsabilidades por seis papéis de direção, sem demonstração. `E15 ⚠ = 1` — a atribuição de responsabilidades é apresentada como padrão, sem fonte; `103` adverte que "papéis se sobrepõem, variam por empresa e **não equivalem a seis agentes autônomos**". **NF = 1 · 2/7 · 5 ND**
**B:** `E01 = 3` (endereça diretamente: é o lado "como se empacota por domínio", em forma de responsabilidade) · `E04 = 2` · `E14 = 2`. **RP = 2 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND**
**Catálogo — NC = 5:** título pelo conteúdo visível ("papéis de CEO, CFO, COO, CIO, CMO e CRO") **confirmado** por `103`, nos seis papéis. **Confere:** sim.
**Vetos:** **V2 · V4 sim**. **RF = REFERÊNCIA** (§9).
> **Registro:** a advertência de `103` — papel de direção **não é** agente autônomo — é a única do lote que trata de erro de projeto, não de erro de fato. Registrada como alegação de terceiro, não como norma.

### AC-10-VID-012 — `Gravando 2026-07-29 091940.mp4` · cem funções empresariais
**Hash F0:** `454B48A0A2AA19EC`   **Hash reconferido:** `454B48A0A2AA19EC`   **Confere:** sim   **LV:** **LV3-V**
**Cobertura da leitura:** 9,2 s, `en`, 1 palavra, confiança **0,130**, SEM FALA LEXICAL CONFIÁVEL (`117`) · quadros por `103` · 2026-07-29
**A:** `E02 = 1` — listagem: **quatro blocos de 25**. `E15 ⚠ = 1` — `103`: "não são cem capacidades comprovadas"; cada função exigiria entrada, fonte, risco, saída, aprovação e evidência. **NF = 1 · 2/7 · 5 ND**
**B:** `E01 = 3` · `E04 = 2` · `E14 = 2` (**sobrepõe `AC-10-PRT-006`**, que traz 63 por função). **RP = 2 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND**
**Catálogo — NC = 5:** título pelo conteúdo visível ("cem usos do Claude em operação, estratégia e gestão") **confirmado** por `103` quanto ao total e a dois dos quatro blocos; os outros dois blocos observados (conteúdo e avançado) **acrescentam**, não contradizem. **Confere:** sim.
**Vetos:** **V2 · V4 sim**. **RF = REFERÊNCIA** (§9).

---

## Lote L-25 — VÍDEO 013 a 023

*Mesma nota de aplicação do lote L-24: LV3-V por `103`, LV3-A por `117`, a soma não produz LV4, V5 não aplicado a vídeo, Bloco C fixo §3.3, `E03 · E05 · E07 · E13 = ND` em todos.*

### AC-10-VID-013 — `Gravando 2026-07-29 092149.mp4` · indicadores por papel de direção
**Hash F0:** `1309F595714F3C9E`   **Hash reconferido:** `1309F595714F3C9E`   **Confere:** sim   **LV:** **LV3-V**
**Cobertura da leitura:** **5,7 s — o menor vídeo do acervo** · `en`, 1 palavra, 0,751, SEM FALA LEXICAL CONFIÁVEL (`117`) · quadros por `103` · 2026-07-29
**A:** `E02 = 1` — listagem: **dez indicadores por papel**, para três papéis, todos nomeados. É índice, não método. `E15 ⚠ = 1` — `103`: valor "sujeito a definição, contexto, fonte contábil e dono" — ou seja, os nomes dos indicadores não carregam definição. **NF = 1 · 2/7 · 5 ND**
**B:** `E01 = 3` · `E04 = 3` (a lista de indicadores por papel transfere literalmente) · `E14 = 2` (sobrepõe `AC-10-VID-007` e `AC-10-VID-011`). **RP = 3 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND**
**Catálogo — NC = 2 — PARCIAL.** O catálogo declara "KPIs para CEO, CFO e COO **com kit financeiro**". Os três papéis e os indicadores **conferem** em `103`; o "kit financeiro" **não foi observado**. Detalhe não confirmado ⇒ teto 2 (§14.4).
**Vetos:** **V2 · V4 sim**. **RF = REFERÊNCIA** (§9).

### AC-10-VID-014 — `_construcao-civil/3d de planta e alteraçao .mp4` · planta em casa navegável
**Hash F0:** `ACB7A05027494E80`   **Hash reconferido:** `ACB7A05027494E80`   **Confere:** sim   **LV:** **LV3-V**
**Cobertura da leitura:** 30,2 s, `en`, 2 palavras, 0,647, SEM FALA LEXICAL CONFIÁVEL (`117`) · quadros por `103` · 2026-07-29
> **Item sinalizado pelo índice do acervo como "candidato a descarte". `05` §10 é literal: não descartar.** A sinalização é **alegação do catálogo**, e `FORA DE ESCOPO = 0` é decisão deliberada da rubrica. O item recebeu ficha completa como qualquer outro. **O próprio catálogo se corrigiu depois**, na remessa de 28/07: "construção civil deixou de ser um único item isolado e virou uma vertical consistente, agora com sete vídeos. Já não deve ser tratada como 'candidato a descarte' sem revisão."
**A:** `E02 = 1` — demonstração de resultado: planta entra, casa virtual navegável sai, com opções e alterações. Nenhum processo, nenhuma precisão declarada. `E15 ⚠ = 1` — `103`: "produto, precisão, interoperabilidade BIM/CAD, regras e responsabilidade técnica não foram verificados". **NF = 1 · 2/7 · 5 ND**
**B:** `E01 = 3` (endereça diretamente: é a vertical de construção, a única do acervo fora do eixo de software) · `E04 = 1` (só a ideia; é produto de terceiro, não artefato) · `E14 = 2`. **RP = 2 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND**
**Catálogo — NC = 1 — assunto pelo título:** "geração e alteração de planta em 3D", numa tabela que só traz arquivo, tamanho e assunto. Confere com `103` no pouco que afirma.
**Alegações:** o produto nomeado nos quadros — ALEGAÇÃO DO AUTOR sobre origem, **não conferida**; está fora do acervo. · "candidato a descarte" — **ALEGAÇÃO DO CATÁLOGO, registrada e não obedecida** (`05` §10).
**Vetos:** **V2 · V4 sim**. **RF = REFERÊNCIA** (§9).

### AC-10-VID-015 — `_construcao-civil/Gravando 2026-07-28 160740.mp4` · apresentação arquitetônica
**Hash F0:** `458FB3C1F4193FEC`   **Hash reconferido:** `458FB3C1F4193FEC`   **Confere:** sim   **LV:** **LV3-V**
**Cobertura da leitura:** 84,9 s, `en`, 4 palavras, 0,886, **SEM NARRAÇÃO CONFIÁVEL — EFEITO, MÚSICA OU ALUCINAÇÃO DO STT** (`117`) · quadros por `103` · 2026-07-29
**A:** `E02 = 1` — listagem de sete efeitos de apresentação (holograma, transformação de fachada, planta virando obra, tour sincronizado, miniatura em escala, troca de estilo, antes/depois). `E15 ⚠ = 1` — `103` registra a **proibição candidata** mais forte da área: "render criativo **não pode ser apresentado como viabilidade, projeto executivo ou resultado garantido**". **NF = 1 · 2/7 · 5 ND**
**B:** `E01 = 2` (genérico: é comunicação e venda de conceito, não empacotamento de sistema) · `E04 = 1` · `E14 = 2`. **RP = 2 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND**
**Catálogo — NC = 5:** título pelo conteúdo visível ("holograma 3D, projeto construído e mudança de interiores em tempo real") **confirmado** por `103`. **Confere:** sim.
**Vetos:** **V2 · V4 sim**. **RF = REFERÊNCIA** (§9).
> **Registro:** o estado de áudio "efeito, música ou alucinação do STT" é declaração de que **as 4 palavras transcritas não são fala** — não devem ser tratadas como conteúdo.

### AC-10-VID-016 — `_construcao-civil/Gravando 2026-07-28 160920.mp4` · planejamento de obra
**Hash F0:** `0A0CC29628F183BC`   **Hash reconferido:** `0A0CC29628F183BC`   **Confere:** sim   **LV:** **LV3-V + LV3-A**
**Cobertura da leitura:** 64,7 s, `pt`, 232 palavras, 17 segmentos, **0,922 — a maior confiança de STT do acervo** (`117`) · quadros por `103` · 2026-07-29
**A:** `E02 = 2` — detalhe reproduzível: **cinco usos encadeados** — planilha e orçamento, análise de projeto, especificações, transformação em apresentação, cronograma e visão do gestor. **`E06` ⚠ = 1** — **risco declarado por terceiro, não confirmado por inspeção**: `103` marca "**risco crítico**: orçamento, especificação e cronograma exigem **documentos controlados, profissional responsável e validação determinística**". `E15 ⚠ = 1` — nenhuma validação de número de orçamento é exibida. **NF = 1 · 3/7 · 4 ND**
**B:** `E01 = 3` · `E04 = 2` · `E14 = 3` (é o item que liga documento de obra a saída de gestão; sem equivalente no acervo). **RP = 3 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND**
**Catálogo — NC = 2 — PARCIAL.** O catálogo declara "proposta de obra gerada a partir de planilha para o cliente"; `103` observa **cinco usos**, dos quais a proposta é um. A descrição é **verdadeira e estreita** — o detalhe não cobre o observado (§14.4).
**Vetos:** V1 não (`E06 = 1`, não 0) · **V2 sim** · **V4 sim** · demais não. **RF = REFERÊNCIA** (§9).

### AC-10-VID-017 — `_construcao-civil/Gravando 2026-07-28 161049.mp4` · pranchas a partir de planta
**Hash F0:** `B88657D2EAF892CB`   **Hash reconferido:** `B88657D2EAF892CB`   **Confere:** sim   **LV:** **LV3-V**
**Cobertura da leitura:** 14,7 s, `en`, 1 palavra, confiança **0,130**, SEM FALA LEXICAL CONFIÁVEL (`117`) · quadros por `103` · 2026-07-29
**A:** `E02 = 1` — listagem de prompts que transformam planta, imagem ou corte em prancha com layout, cortes, elevações, materiais e detalhes. **`E06` ⚠ = 1** — **risco declarado por terceiro**: `103` marca "**risco crítico**: IA pode **inventar dimensões, estrutura, fundação e detalhes**; saída **não é documentação executiva** sem reconstrução e verificação profissional". `E15 ⚠ = 1` — a qualidade "executiva" da saída é afirmada e não demonstrada. **NF = 1 · 3/7 · 4 ND**
**B:** `E01 = 2` (genérico: é ideação editorial, no registro de `103`) · `E04 = 2` · `E14 = 2`. **RP = 2 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND**
**Catálogo — NC = 2 — PARCIAL, e a divergência é de qualificação.** O catálogo declara "prancha arquitetônica **executiva**"; `103` diz o contrário sobre o produto: **não é documentação executiva**. A transformação exibida confere; **o adjetivo não** (§14.4). É a diferença entre descrever o que a tela mostra e endossar o que ela promete.
**Vetos:** V1 não · **V2 sim** · **V4 sim**. **RF = REFERÊNCIA** (§9).

### AC-10-VID-018 — `_construcao-civil/Gravando 2026-07-28 161155.mp4` · levantamento sobre planta
**Hash F0:** `209424B2371FE9EF`   **Hash reconferido:** `209424B2371FE9EF`   **Confere:** sim   **LV:** **LV3-V**
**Cobertura da leitura:** 34,6 s, `en`, 4 palavras, 0,565, **SEM NARRAÇÃO CONFIÁVEL — EFEITO, MÚSICA OU ALUCINAÇÃO DO STT** (`117`) · quadros por `103` · 2026-07-29
**A:** `E02 = 2` — o mais concreto da vertical: marcar ambientes e medidas sobre a planta, editar elementos, **classificar** ambientes, estruturas, superfícies e cobertura, e **exportar o levantamento em formato estruturado**. `E15 ⚠ = 1` — `103` exige, como porta, "escala/calibração, tolerância, rastreabilidade por marcação, revisão e teste contra levantamento real"; nada disso é exibido. **NF = 1 · 2/7 · 5 ND** *(§14.3)*
**B:** `E01 = 3` · `E04 = 2` · `E14 = 3` (`103` o chama "**candidato forte de fluxo**": medição → quantidade → estrutura de dados; é o único item do acervo que fecha essa cadeia). **RP = 3 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND**
**Catálogo — NC = 3:** "sistema de IA para analisar e editar planta baixa" — o detalhe verificável (analisar e editar sobre a planta) **confere** com `103`; a exportação estruturada é acréscimo observado, não contradição.
**Vetos:** **V2 · V4 sim**. **RF = REFERÊNCIA** (§9).

### AC-10-VID-019 — `_construcao-civil/Gravando 2026-07-28 164000.mp4` · projeto validado contra código construtivo
**Hash F0:** `B844787C060DC6A9`   **Hash reconferido:** `B844787C060DC6A9`   **Confere:** sim   **LV:** **LV3-V**
**Cobertura da leitura:** 87,3 s, `en`, 3 palavras, 0,710, SEM FALA LEXICAL CONFIÁVEL (`117`) · quadros por `103` · 2026-07-29
**A:** `E02 = 1` — carrossel de alegações sobre um produto de terceiro: configurador, validação contra código construtivo, adaptação ao local, fábrica robótica em cidade nomeada, custo muito inferior. Nenhuma demonstração. **`E15` ⚠ = 0** — **a proposta central do item depende inteiramente de alegações fortes, sem fonte e não verificáveis com o material disponível**: `103` é explícito — "**todas** as capacidades, locais e faixas de custo exigem fonte primária e validação de engenharia". Tirando as alegações, não sobra conteúdo. **NF = 0 · 2/7 · 5 ND** *(determinados `E02 = 1` e `E15 = 0`; mediana de [0,1] = 0,5 → §14.3 vale o inferior)*
**B:** `E01 = 3` (endereça diretamente: **integração vertical projeto → regra → fabricação** é modelo de negócio, e `103` o registra como achado) · `E04 = 1` (só a ideia; é empresa de terceiro) · `E14 = 3` (nenhum outro item do acervo descreve cadeia projeto-a-fábrica). **RP = 3 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND**
**Catálogo — NC = 5:** título pelo conteúdo visível ("projeto de casa com IA e checagem contra código de construção") **confirmado** por `103`. **Confere:** sim — o catálogo descreve corretamente o que a tela alega.
**Alegações:** validação contra código construtivo · fábrica robótica em local nomeado · "custo muito inferior" — **todas ALEGAÇÃO DO AUTOR sobre empresa de terceiro, `NÃO VERIFICADAS` e não verificáveis com o material disponível**. Sustentam `E15 = 0`.
**Vetos:** V1 · V3 · V5 · V6 · V8 não · **V2 · V4 sim** (`E06 = ND`, `E07 = ND`) · **V7 SIM** — `E15 = 0` **e a relevância do item depende dessa alegação** → teto EXIGE PESQUISA.
**RF = EXIGE PESQUISA** — regra: **V7**, mais §9 (relevância aparente + lacuna nomeada).
**Lacuna nomeada:** a existência e o desempenho do que é alegado — configurador, validação normativa automatizada, fábrica e faixa de custo. **Verificação que a fecharia:** fonte primária da empresa citada (documentação técnica, registro industrial, publicação revisada) e avaliação de engenharia sobre a validação normativa. **Fora do acervo e fora desta fase.**

### AC-10-VID-020 — `_construcao-civil/Gravando 2026-07-28 164422.mp4` · prospecção outbound
**Hash F0:** `70731C4B988258E0`   **Hash reconferido:** `70731C4B988258E0`   **Confere:** sim   **LV:** **LV3-V**
**Cobertura da leitura:** 33,0 s, idioma detectado **`km`** com 27 palavras, 0,843, **SEM NARRAÇÃO CONFIÁVEL — EFEITO, MÚSICA OU ALUCINAÇÃO DO STT** (`117`) · quadros por `103` · 2026-07-29
> **Registro técnico:** o detector de idioma devolveu **khmer** para um vídeo do acervo em contexto lusófono, com 27 palavras e confiança alta. `117` classifica como **alucinação do STT**. As 27 palavras **não são conteúdo** e não foram usadas. É a demonstração mais clara, no acervo, de por que LV3-A bruto não vira LV4.
**A:** `E02 = 1` — encadeamento demonstrado: busca em mapa, seleção de negócio sem site, geração de site, ligação comercial. **`E06` ⚠ = 1** — **risco declarado por terceiro, não confirmado**: `103` registra "coleta de dados, spam, direitos sobre marca/conteúdo, qualidade, transparência e **contato não solicitado**; **não automatizar prospecção/publicação**". `E15 ⚠ = 1` — nenhuma taxa de conversão ou resultado é exibida. **NF = 1 · 3/7 · 4 ND**
**B:** `E01 = 2` (genérico: é hipótese de serviço, não empacotamento de sistema) · `E04 = 1` · `E14 = 1`. **RP = 1 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND**
**Catálogo — NC = 2 — PARCIAL.** O catálogo declara "busca de **lojas de construção**"; `103` observa busca por **negócios sem presença web**, sem restringir a ramo. O restante — geração de site e ligação — confere. Detalhe não confirmado ⇒ teto 2 (§14.4).
**Vetos:** V1 não · **V2 sim** · **V4 sim**. **RF = REFERÊNCIA** (§9; `RP = 1`).
> **Registro de risco, sem ação.** Nenhum dado foi coletado, nenhuma empresa foi contactada, nada foi publicado.

### AC-10-VID-021 — `_redes-sociais/configiraçao para melhorar instagram e coisas a fazer.mp4`
**Hash F0:** `C49034BE41C61523`   **Hash reconferido:** `C49034BE41C61523`   **Confere:** sim   **LV:** **LV3-V + LV3-A**
**Cobertura da leitura:** 50,1 s, `pt`, 195 palavras, 14 segmentos, 0,887, ALTA AUTOMÁTICA (`117`) · quadros por `103` · 2026-07-29
> **Grafia preservada, não normalizada** (`configiraçao`), conforme `05` §10.
**A:** `E02 = 1` — checklist de configuração de conta: nome e categoria, perfil, painel profissional, privacidade, compartilhamento, downloads, qualidade de mídia. `103` observa que "a lista exata depende da fala". `E15 ⚠ = 1` — `103`: "alegações de impulsionamento, crescimento e causalidade **não verificadas**". **NF = 1 · 2/7 · 5 ND**
**B:** `E01 = 2` (genérico) · `E04 = 2` (checklist operacional, dependente de uma plataforma e de sua versão) · `E14 = 1`. **RP = 2 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND**
**Catálogo — NC = 1 — assunto pelo título:** "configuração e tarefas de Instagram", em tabela com arquivo, tamanho e assunto. Confere no pouco que afirma.
**Vetos:** **V2 · V4 sim**. **RF = REFERÊNCIA** (§9).

### AC-10-VID-022 — `_redes-sociais/estrategia de 300 dias 100k seguidores  intagram.mp4`
**Hash F0:** `0F7CC1DE5826EF9C`   **Hash reconferido:** `0F7CC1DE5826EF9C`   **Confere:** sim   **LV:** **LV3-V + LV3-A**
**Cobertura da leitura:** 76,4 s, `pt`, 178 palavras, 25 segmentos, 0,888, ALTA AUTOMÁTICA (`117`) · quadros por `103` · 2026-07-29
> **Nome com espaço duplo e grafia preservada** — item **I-01** do acervo. `05` §10: localizar **por ID e caminho literal do manifesto**, nunca por busca de nome. Foi o que se fez.
**A:** `E02 = 1` — quadros mostram planejamento por tema, formato e frequência, pesquisa, inspiração, carrossel e a regra "três por dia"; `103` registra **ficha parcial** — "a estratégia completa depende do áudio". `E15 ⚠ = 1` — meta e prazo (100 mil seguidores em 300 dias) **estão no nome do arquivo e na tela, sem nenhuma evidência**; `103`: "volume não substitui qualidade, adequação nem sustentabilidade". **NF = 1 · 2/7 · 5 ND**
**B:** `E01 = 2` · `E04 = 1` · `E14 = 1`. **RP = 1 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND**
**Catálogo — NC = 1 — assunto pelo título:** "estratégia de crescimento no Instagram". Confere no pouco que afirma.
**Alegações:** "100 mil seguidores em 300 dias" — ALEGAÇÃO DO AUTOR, `NÃO VERIFICADA`, **sem qualquer dado de apoio**. · **`V7` avaliada, não disparou:** `E15 = 1`, não 0 — há conteúdo operacional nos quadros (temas, formato, frequência) que existe independentemente da meta.
**Vetos:** **V2 · V4 sim**. **RF = REFERÊNCIA** (§9; `RP = 1`).

### AC-10-VID-023 — `_renda-extra/afiliados.mp4`
**Hash F0:** `6F1014323874CE99`   **Hash reconferido:** `6F1014323874CE99`   **Confere:** sim   **LV:** **LV3-V + LV3-A**
**Cobertura da leitura:** 87,2 s, `pt`, 364 palavras — **o maior volume de fala do acervo** —, 29 segmentos, 0,838, **MÉDIA AUTOMÁTICA** (`117`) — **o único item do acervo nesse estado de confiança**, e por isso o de transcrição menos confiável entre os que têm fala · quadros por `103` · 2026-07-29
**A:** `E02 = 1` — `103`: "diálogo majoritariamente oral **termina em oferta promocional**… valor extraível muito baixo sem transcrição". Nenhum procedimento, nenhum dado. `E15 ⚠ = 1` — é **alegação de renda** em funil comercial; `103` manda "não converter em recomendação ou oportunidade validada". **Não é 0** porque a proposta do item não é sustentada por um número específico: é oferta, não tese quantificada. **NF = 1 · 2/7 · 5 ND**
**B:** `E01 = 1` (**não endereça a pergunta da área**: não trata de vertical a provar nem de empacotamento por domínio — trata de venda de método) · `E04 = 1` · `E14 = 1`. **RP = 1 · 3/3 · 0 ND** · **AA = 4 · 5/5 · 0 ND**
**Catálogo — NC = 1 — assunto pelo título:** "marketing de afiliados. Não transcrito." Confere no pouco que afirma; o marcador "não transcrito" está **superado** por `117`.
**Alegações:** promessa de renda e o nome comercial da oferta — **ALEGAÇÃO DO AUTOR, `NÃO VERIFICADA`**; registrada literalmente como o que é: material promocional dentro do acervo.
**Vetos:** **V2 · V4 sim**; **V7 avaliada, não disparou** (`E15 = 1`); V1 não — `E06 = ND`: o risco aqui é comercial e informacional, **não superfície técnica**, e a rubrica mede superfície em `E06`; V5 não aplicado (`LV = 3`).
**RF = REFERÊNCIA** — §9, insumo de consulta com `LV ≥ 3`. **Registro explícito:** `E01 = 1` e `RP = 1` fecham qualquer candidatura, e **EXIGE PESQUISA não se aplica** porque sua condição de entrada exige *relevância aparente*, que aqui não existe. Classificar como REFERÊNCIA **não é endosso** — é o lugar do item que só serve para constar.

---

## Fechamento da área 10 — contagem factual

**Itens com ficha:** 46 de 46 · **IDs faltando:** 0 · **IDs repetidos:** 0 · **É a maior área do acervo**

| RF | Quantidade | IDs |
|---|---|---|
| CANDIDATO FORTE | 0 | — |
| **CANDIDATO A PILOTO** | **2** | `AC-10-REP-002`, `AC-10-REP-003` |
| PADRÃO A ESTUDAR | 0 | — |
| **EXIGE PESQUISA** | **5** | `AC-10-REP-001`, `AC-10-REP-004`, `AC-10-REP-005`, `AC-10-PRT-016`, `AC-10-VID-019` |
| **REFERÊNCIA** | **39** | `AC-10-REP-006` (ficha de delta), `AC-10-PLA-001`, os 15 PRINT restantes e os 22 VÍDEO restantes |
| REJEITADO · DUPLICADO · INDETERMINADO | 0 | — |

| LV | Itens |
|---|---|
| LV4 | 6 (os seis REPO) |
| LV3-V | 31 (16 PRINT + 15 VÍDEO sem fala aproveitável) |
| LV3-V + LV3-A | 8 (`VID-002`, `003`, `006`, `008`, `016`, `021`, `022`, `023`) |
| LV3 | 1 (`AC-10-PLA-001` — **divergência declarada**: `111` atribui LV4; esta frente adota o inferior, DEF-07) |

**ND:** **196** de 690 células de eixo (46 itens × 15 eixos) = **28,4 %** — contados por grupo: **6** nos seis REPO (2+0+2+0+1+1), **1** na PLANILHA, **79** nos dezesseis PRINT (4 em `PRT-001`, 5 nos demais quinze) e **110** nos vinte e três VÍDEO (4 em `VID-006`, `010`, `016`, `017`, `020`; 5 nos outros dezoito). Nenhum item chegou ao gatilho de V6 (8 ND). Todos os 196 nomeiam o que os resolveria.

**Portas de veto na área:** V1 — 0 · **V2 — 40** (`E06 = ND` em 33, **`E06 = 1` em 7**: `PLA-001`, `PRT-001`, `VID-006`, `VID-010`, `VID-016`, `VID-017`, `VID-020`) · V3 — 0 · **V4 — 40** (todos os não-REPO) · V5 — 0 (não aplicado a vídeo; e `PLA-001` ficou exatamente em `LV3`, o limite) · V6 — 0 · **V7 — 2** (`PRT-016` e `VID-019`, ambos com `E15 = 0`) · **V8 — 0 divergências**: os 46 reconferem.

**Catálogo** — contagem por ficha, medida por ferramenta sobre o arquivo (soma 46):

| `NC` | Itens | Quais |
|---|---:|---|
| **5** | 10 | `VID-001`, `003`, `004`, `005`, `006`, `007`, `011`, `012`, `015`, `019` |
| **3** | 21 | os seis REPO, `PRT-001` a `PRT-007`, `PRT-009` a `PRT-015`, `VID-018` |
| **2 — PARCIAL** | 10 | `PLA-001`, `PRT-008`, `PRT-016`, `VID-008`, `VID-009`, `VID-010`, `VID-013`, `VID-016`, `VID-017`, `VID-020` |
| **1 — assunto pelo título** | 4 | `VID-014`, `VID-021`, `VID-022`, `VID-023` |
| **0 — DIVERGENTE** | 1 | `AC-10-VID-002` |

**Registros novos desta área:**
1. **Terceira divergência de catálogo da rodada** — `AC-10-VID-002`: descrito como agente de vendas, os quadros mostram uma biblioteca de conversão documental. Com as duas da área 08 e a da área 09, o acervo acumula **quatro `NC = 0`** nesta rodada, **todas por descrição de conteúdo, nenhuma por hash**.
2. **Dez descrições PARCIAIS numa só área** — mais que em todas as áreas anteriores somadas. O padrão é consistente: o catálogo **estreita ou arredonda** — a inspeção mostrou mais itens, contou diferente, ou não confirmou o adjetivo usado.
3. **Série incompleta medida** — o carrossel `workkflow conteudo` cobre os slides **1/9 a 8/9**; **o slide 9 não está no acervo**. Lacuna do acervo, registrada nas oito fichas.
4. **Recorte editorial detectado em transcrição** — `AC-10-PRT-016`: o gráfico tem **17 linhas**, o catálogo transcreveu **9**, e as 9 são as de maior delta, o que reforça a conclusão que ele extrai. `109` nomeou as oito omitidas.
5. **Dois totais que não reconciliam na planilha** — 131 × **128** rotas e 14/13 × **13/14** integrações, medidos por `111`. E o termo "vulnerabilidades", que ali significa **brecha comercial**, não falha de segurança.
6. **Sete itens com `E06 = 1`** — o maior número do acervo numa área, e por três naturezas distintas: **dado pessoal e decisão de emprego** (`PRT-001`), **execução de pacote remoto exibida** (`VID-006`), **propriedade intelectual e dado financeiro** (`VID-010`), **documento técnico de obra sem responsável** (`VID-016`, `VID-017`), **prospecção não solicitada** (`VID-020`) e **engenharia reversa com dado de terceiro** (`PLA-001`). **Nenhum foi rejeitado**: V1 exige risco confirmado por inspeção.
7. **Primeira ficha de delta do acervo** — `AC-10-REP-006`, com sobreposição medida de **81,5 % dos arquivos e 17/17 skills**. Registrado o efeito incômodo: as duas melhores notas do delta vêm de **ausências**, não de adições.
8. **Dois itens com Bloco A integralmente determinado** — `AC-10-REP-002` e `AC-10-REP-004` (0 ND), somando-se a `AC-08-REP-003`. Três no acervo, todos repositórios com licença, versão datada e testes na própria fonte.
9. **`AC-10-REP-004` é o caso mais nítido de eixo único fechando classificação**: `NF = 4`, `RP = 4`, `AA = 4`, **0 ND** — e para em EXIGE PESQUISA por `E06 = 2`.
10. **O item que o índice mandou descartar recebeu ficha** — `AC-10-VID-014`, conforme `05` §10. O próprio catálogo se retratou depois, ao ver a vertical crescer para sete vídeos.
11. **Alucinação de STT documentada** — `AC-10-VID-020`, idioma detectado khmer com 27 palavras e confiança alta, num vídeo em contexto lusófono. É a prova prática da regra "LV3-A bruto não vira LV4".

> Esta seção é contagem de fichas, não classificação de valor. Não há ordenação, ranking ou recomendação.

