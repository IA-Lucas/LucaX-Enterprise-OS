> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

# FICHAS DE EVIDÊNCIA — ÁREA 09 — SEGURANÇA E QUALIDADE

**Fase:** 2 — Extração · **Data:** 2026-07-29 · **Avaliador:** Claude Opus 5 (Fase 2)
**Itens:** 10 — 1 REPO · 2 PRINT · 7 VÍDEO · 0 PLANILHA
**Convenções de aplicação:** `00_INDICE-DA-FASE-2.md` §3

**Pergunta central da área (base de E01):** *como saber que o sistema funciona e que é seguro instalar o que se instala.*

> **Registro de contexto, não de valor.** O catálogo abre esta área afirmando que ela é "a pasta mais vazia do acervo — e isso é em si um achado". Esta frente **não confirma nem nega o juízo**; registra o fato contável: a área tem **10 itens** e **um único repositório**, contra 43 repositórios no acervo inteiro. A contagem está no manifesto; a leitura de significado é trabalho de fase posterior.

---

### AC-09-REP-001 — `SkillSpector-main`

**Tipo:** REPO · **Área:** 09_SEGURANCA-E-QUALIDADE
**Hash F0:** `dir · 242 arq. · aninhado`   **Hash reconferido:** `242 arq. · aninhamento 1`   **Confere:** sim
**LV:** LV4
**Cobertura da leitura:** raiz efetiva `SkillSpector-main/SkillSpector-main` (23 entradas); `LICENSE` — Apache License 2.0, 10.782 bytes, íntegro, mais `THIRD_PARTY_NOTICES.md`; `README.md` (33.501 bytes, lidos 6 KB: proposta, números citados, documentação, lista de recursos e categorias); `pyproject.toml` (dependências: `langchain-anthropic`, `langchain-aws`, `langchain-core`, `langchain-openai`); listagem de `tests/` (**96 arquivos**, com `unit`, `integration`, `docker`, `provider`, `fixtures`, `nodes` e testes nomeados por ameaça); sinais `SECURITY.md`, `.env.example`, `Dockerfile`, `Makefile`, `.pre-commit-config.yaml`, `.skillspector-baseline.example.yaml`, `model_registry.yaml`, `langgraph.json`. **Não lidos:** `src/`, `docs/`, `extensions/`, `contrib/`.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** não se aplica

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 4 | Artefato completo e inspecionável **mais** procedimento de verificação declarado e **alinhado ao que o artefato promete**: `tests/` com 96 arquivos, entre eles `test_mcp_least_privilege.py`, `test_mcp_rug_pull.py`, `test_mcp_tool_poisoning.py` e `test_multi_skill.py` — ou seja, teste nomeado **por ameaça**, não só por função. `Makefile`, `Dockerfile` e ganchos de pré-commit como pontos de entrada | — |
| E03 Maturidade | 4 | Versionado com dependências fixadas (`uv.lock`, `pyproject.toml`, `package.json`) **mais** documentação de instalação e uso (`docs/DEVELOPMENT.md`, `docs/PI_EXTENSION.md`, `CONTRIBUTING.md`, `.github/`) **mais** tratamento de configuração explícito (`model_registry.yaml`, `.env.example`, arquivo de linha de base de exemplo) | — |
| E05 Manutenção | ND | — | Nenhuma evidência datada dentro da fonte — não há `CHANGELOG` na raiz efetiva. Resolveria consultar releases e commits na origem pública |
| E06 Segurança ⚠ | 4 | **Superfície declarada com controles documentados**: `SECURITY.md`, `THIRD_PARTY_NOTICES.md`, `.env.example` em vez de credencial embutida, `Dockerfile` para execução isolada — que é o modo correto de rodar um scanner sobre material não confiável — e ganchos de pré-commit. Coerência observável entre o que o item **é** e o que ele **pratica**. Não alcança 5: nenhuma auditoria externa foi lida, e `src/` não foi inspecionado | — |
| E07 Licença ⚠ | 4 | Permissiva padrão presente e íntegra: Apache License 2.0, 10.782 bytes, acompanhada de avisos de terceiros. Cópia local não prova titularidade → teto 4 | — |
| E13 Testes/evals | 4 | Suíte executável identificável com ponto de entrada (`Makefile`, `tests/conftest.py`) **mais** verificação de comportamento adversarial por ameaça nomeada, incluindo cenários de MCP. Não alcança 5: nenhum resultado publicado (taxa de detecção, falso positivo) foi lido | — |
| E15 Alegações ⚠ | 1 | **Alegação forte com fonte apenas genérica**: "**Research shows** that 26.1% of skills contain vulnerabilities and 5.2% show likely malicious intent" — nenhum estudo é nomeado no trecho lido, e os dois números sustentam a razão de existir do artefato. Enquadra-se em `03_RELATORIO` §10, R-06 (alegação sem fonte identificável). **Registro a favor:** os outros números — "68 padrões", "17 categorias" — são **conferíveis dentro da própria fonte** e valeriam 2; a nota segue a alegação mais fraca porque é ela que sustenta a proposta | — |

**NF = 4 · 6/7 · 1 ND** *(mediana dos determinados [1,4,4,4,4,4] = 4)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 4 | Endereça **literalmente** a pergunta central da área — "é seguro instalar o que se instala" — **mais** artefato concreto e reutilizável | — |
| E04 Transferibilidade | 4 | Transferível por configuração, sem alteração de código: aceita repositório, URL, zip, diretório ou arquivo único como entrada, tem contêiner e extensão declarada para uso de dentro da sessão de agente | — |
| E14 Diferencial | 4 | Sem equivalente no acervo **mais** custo alto de reconstrução: 68 padrões em 17 categorias, com análise de AST, rastreamento de contaminação e assinaturas YARA. É o único item do acervo que **verifica** outros itens em vez de produzir capacidade | — |

**RP = 4 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração | 3 | Instalação declarada, porém com runtime e configuração: Python 3.12+, cadeia `langchain`/`langgraph` e registro de modelo a configurar. Contêiner disponível como alternativa | — |
| E09 Custo | 3 | **Custo recorrente previsível e mensurável**: cada varredura consome chamadas de modelo pelo provedor configurado, proporcionalmente ao volume varrido. Não é custo de licença — Apache-2.0 —, é custo de inferência que **não existiria** sem o item | — |
| E10 Contexto/tokens | 4 | Medido: **242 arquivos, 2,4 MB** — abaixo de 300 arquivos e de 5 MB | — |
| E11 Fornecedor | 4 | Abstração de fornecedor documentada: `model_registry.yaml` mais integrações para três provedores distintos na própria declaração de dependências | — |
| E12 Reversibilidade | 4 | Reversível por remoção, sem efeito residual: produz relatório e linha de base em arquivo; não altera o material varrido | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — descrição com detalhe verificável (a pergunta que o item responde, os dois percentuais citados, 68 padrões em 17 categorias com a lista das categorias, os cinco formatos de entrada, licença e versão de Python) e **todos** conferem com o README e a raiz lidos. O catálogo **reproduz** os percentuais como citação do repositório, sem adotá-los como fato.
**O que o catálogo afirma:** "Responde a uma pergunta que ninguém costuma fazer antes de instalar: **'esta skill é segura?'**… Os números que ele cita de pesquisa: **26,1% das skills contêm vulnerabilidade e 5,2% mostram intenção provavelmente maliciosa**… Cobre **68 padrões de vulnerabilidade em 17 categorias**… Apache 2.0, Python 3.12+."
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Research shows that **26.1% of skills contain vulnerabilities** and **5.2% show likely malicious intent**." | `README.md` da fonte | ALEGAÇÃO DO AUTOR citando pesquisa **não nomeada** | **não** — fonte não identificável no trecho lido; sustenta `E15 = 1` |
| "**68 vulnerability patterns** across **17 categories**" | `README.md` da fonte | ALEGAÇÃO DO AUTOR | não — **conferível dentro da fonte** (`src/`), não conferida sob o teto de leitura |
| "**Rodar o SkillSpector sobre as pastas 03 a 07 antes de adotar qualquer coisa é o uso mais imediato do material.**" | `_CONTEUDO.md` área 09 | **ALEGAÇÃO DO CATÁLOGO — instrução de ação** | **registrada, não obedecida** (`05` §7; e a proibição desta frente de executar repositórios é explícita). Fica como **verificação nomeada e endereçável**, para decisão fora desta fase |
| "Este acervo contém 43 repositórios de terceiros que ninguém auditou." | `_CONTEUDO.md` área 09 | ALEGAÇÃO DO CATÁLOGO | **a contagem confere** com o manifesto (43 REPO); a afirmação de não auditoria é do catálogo e coerente com o que esta frente observou |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V2 · V3 · V4 · V5 · V6 · V8 | não | `E06 = 4` · `E07 = 4` · `LV = 4` · 1 ND · reconferência confere |
| **V7** | **avaliada, não disparou** | `E15 = 1`, **não 0** — há fonte, ainda que genérica. Registro explícito: se os dois percentuais fossem tratados como fato, a relevância do item dependeria de alegação não verificada. **Não é o caso**: `E01 = 4` se sustenta pela pergunta da área e pelo artefato, não pelos percentuais |

#### Resultado
**RF = CANDIDATO A PILOTO**
**Regra que produziu:** §9. **Não** alcança CANDIDATO FORTE: a condição "nenhum eixo do Bloco A abaixo de 3" falha por `E15 = 1`. Satisfaz CANDIDATO A PILOTO: `LV = 4` · `E06 = 4` · `E07 = 4` · `RP = 4` · **1 ND** ≤ 4 · nenhum eixo do Bloco C em 0.
**Se EXIGE PESQUISA — lacuna nomeada:** não se aplica  **Verificação que a fecharia:** —

> **CANDIDATO A PILOTO não significa pilotar.** Restrições registradas: `E05 = ND`; os dois percentuais que motivam o artefato não têm fonte identificável; `E09 = 3` porque cada varredura custa inferência; e nenhuma taxa de detecção ou de falso positivo foi lida — um scanner sem essa medida é instrumento não calibrado.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-09-PRT-001 — `Captura de tela 2026-07-28 152706.png`

**Tipo:** PRINT · **Área:** 09_SEGURANCA-E-QUALIDADE
**Hash F0:** `1C25B7AF0B095587`   **Hash reconferido:** `1C25B7AF0B095587`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`109`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-09-PRT-001 · `H-P1-003` (relatório `109`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 1 | **Só listagem**, ainda que extensa: árvore de disciplinas e ferramentas dividida em defensiva e ofensiva. Nenhum procedimento, nenhum critério, nenhuma implementação. O próprio catálogo registra que "alguns nós misturam disciplina, produto e sistema operacional" — o que a inspeção confirma | — |
| E03 · E05 · E06 · E07 · E13 | ND | — | Origem e data; canal com data; inspeção direta procurando dado sensível; autoria e termos; nenhuma verificação exibida |
| E15 Alegações ⚠ | 1 | Alegações de pertencimento e hierarquia com fonte citada porém não conferidas — e **`109` encontrou erro em uma delas** ao comparar com os pixels | — |

**NF = 1 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 2 | Endereça a pergunta de forma **genérica**: é mapa de competências de segurança corporativa (rede, SIEM, pentest, conformidade), não trata de verificar o que se instala num sistema de agentes — que é a pergunta desta área | — |
| E04 Transferibilidade | 2 | Transferível com adaptação **não declarada**: a árvore serve de vocabulário, mas não diz o que fazer com ele | — |
| E14 Diferencial | 1 | Conveniência sobre conhecimento amplamente acessível: mapas de competência de segurança são material público abundante | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E08 · E09 · E10 · E11 · E12 | 3 · 5 · 4 · 5 · 4 | Valor fixo de mídia do índice §3.3 | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 2 — PARCIAL, com erro de hierarquia identificado.** `109` confirma a divisão Blue/Red e os elementos principais, **mas encontra transcrição incorreta**: o catálogo coloca **Nessus sob Red Teaming**, e no diagrama Nessus está sob **Vulnerability Management**. `109` acrescenta a instrução de não reconstruir hierarquia ambígua por inferência. Detalhe não confirmado ⇒ teto 2 por `04` §14.4.
**O que o catálogo afirma:** "Red Team: Penetration Testing → social engineering, desenvolvimento e Kali Linux; **Red Teaming → Nessus e Metasploit**; Vulnerability Management → OpenVAS, Qualys e Nmap…"
**Confere com a fonte:** **parcialmente** — a estrutura confere, a atribuição de Nessus **não**

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Red Teaming → Nessus e Metasploit" | `_CONTEUDO.md` área 09 | **ALEGAÇÃO DO CATÁLOGO — divergente** | **contradita** por `109`: no diagrama, Nessus está sob Vulnerability Management |
| "alguns nós misturam disciplina, produto e sistema operacional" | `_CONTEUDO.md` área 09 | ALEGAÇÃO DO CATÁLOGO — ressalva | **coerente com a inspeção**: "Kali Linux" ao lado de "social engineering" é exatamente isso |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 1` (≠ 0) · **hash confere** |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

> A divergência aqui é **de transcrição do catálogo**, não da fonte: o hash do print confere e V8 não dispara. Ela rebaixa `NC` e fica registrada.

#### Resultado
**RF = REFERÊNCIA** — §9, insumo de consulta com `LV ≥ 3`; critério §3.4 do índice.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-09-PRT-002 — `Captura de tela 2026-07-28 163441.png`

**Tipo:** PRINT · **Área:** 09_SEGURANCA-E-QUALIDADE
**Hash F0:** `F77D18CFE628E74F`   **Hash reconferido:** `F77D18CFE628E74F`   **Confere:** sim
**LV:** LV3-V   **Cobertura da leitura:** inspeção visual do original pela trilha Codex (`109`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-09-PRT-002 · `H-P1-003` (relatório `109`)

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | 2 | Descrição com detalhe reproduzível, sem artefato: **nove blocos nomeados**, e dois deles trazem o fluxo interno desenhado — o de avaliação (entradas → resposta → camada de avaliação → aprovado/reprovado → métricas) e o de laços agênticos (pensar → executar → monitorar → melhorar). `109` confirma os nove. **Não alcança 3**: `109` também registra que "é mapa de cobertura, não implementação" — sem dataset, métrica ou limiar | — |
| E03 · E05 · E06 · E07 · E13 | ND | — | Origem e data; canal com data; inspeção direta procurando dado sensível; autoria e termos; **o bloco de avaliação é desenhado, não executado** |
| E15 Alegações ⚠ | 1 | Alegações com fonte citada porém não conferidas, uma delas doutrinária: o bloco "Bitter Lesson" afirma que sistemas gerais apoiados em computação tendem a vencer regras artesanais. É tese conhecida, apresentada sem dado no infográfico | — |

**NF = 1 · 2/7 · 5 ND** *(mediana [1,2] = 1,5 → §14.3)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância | 3 | Endereça diretamente a pergunta central: **é o primeiro material do acervo que põe avaliação e observabilidade explicitamente no fluxo de produção** — fato conferido por `109`, que lista os nove blocos, e coerente com o vazio contável desta área | — |
| E04 Transferibilidade | 3 | Transferível com adaptação declarada: os nove blocos funcionam como **lista de cobertura** a responder no desenho, ainda que não digam como | — |
| E14 Diferencial | 3 | Resolve problema declarado sem equivalente pronto **dentro do acervo**: nenhum outro item reúne laço, ferramenta, multiagente, portal, custo, avaliação, proteção de entrada/saída e observabilidade num mesmo quadro | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E08 · E09 · E10 · E11 · E12 | 3 · 5 · 4 · 5 · 4 | Valor fixo de mídia do índice §3.3 | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 3** — detalhe verificável (os nove blocos, nomeados e numerados, com o conteúdo interno de cada um) conferido contra os pixels; **CONFIRMADA** em `109`. O catálogo acrescenta por conta própria o limite: "Ainda é visão geral; não fornece implementação, dataset, métricas nem limiares".
**O que o catálogo afirma:** "Infográfico com nove blocos: 1. loops agênticos… 6. evals: inputs → resposta → camada de avaliação → pass/fail → métricas; 7. guardrails na entrada e saída; 8. observabilidade com traces, logs, métricas e dashboards; 9. 'Bitter Lesson'… **O que extrair:** é o primeiro material do acervo que põe evals e observabilidade explicitamente no fluxo de produção."
**Confere com a fonte:** sim — CONFIRMADA em `109`

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "sistemas gerais, adaptáveis e apoiados em computação tendem a vencer regras artesanais frágeis" | print, via `109` | ALEGAÇÃO DO AUTOR — tese doutrinária | não — `NÃO VERIFICADA`; nenhum dado no infográfico |
| "é o primeiro material do acervo que põe evals e observabilidade explicitamente no fluxo de produção" | `_CONTEUDO.md` área 09 | ALEGAÇÃO DO CATÁLOGO sobre o acervo | **coerente** com as fichas escritas até aqui, que não registram outro item com esse desenho — coerência, não prova |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V5 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · `LV = 3` · 5 ND · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |

#### Resultado
**RF = REFERÊNCIA** — §9, insumo de consulta com `LV ≥ 3`; critério §3.4 do índice.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

> **Nota de aplicação aos sete VÍDEO desta área.** LV3-V vem de `H-M2-001` (relatório `94`); LV3-A, quando existe, do manifesto `117`. **LV3-V + LV3-A não produz LV4**; transcrição automática **não autoriza citação exata**. **V5 não é aplicado automaticamente a vídeo.** Bloco C segue o valor fixo do índice §3.3. Três dos sete têm fala aproveitável (`001`, `002`, `007`, em `pt`, ALTA AUTOMÁTICA); quatro não têm.

### AC-09-VID-001 — `erros e correcóes.mp4`

**Tipo:** VÍDEO · **Área:** 09_SEGURANCA-E-QUALIDADE
**Hash F0:** `2EE427F03CFBF5C1`   **Hash reconferido:** `2EE427F03CFBF5C1`   **Confere:** sim
**LV:** **LV3-V + LV3-A** — a soma **não** produz LV4
**Cobertura da leitura:** quadros-chave (`94`, `H-M2-001`) mais transcrição automática bruta (`117`): 43,2 s, `pt`, 154 palavras, 11 segmentos, confiança 0,872, **ALTA AUTOMÁTICA**. Não revisada; **proibido citar como literal**.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-09-VID-001 · `H-M2-001` (`94`) · `H-M3-001` · `117`

> **Registro literal:** o nome do arquivo está grafado `erros e correcóes.mp4` — acento invertido em "correções". **Grafia preservada, não normalizada.**

#### Bloco A — Fonte
| Eixo | Nota | Evidência | Se ND: o que resolveria |
|---|---|---|---|
| E02 | 2 | Descrição com detalhe reproduzível, sem artefato: **regra com limiar numérico** — após duas ou três tentativas fracassadas no mesmo problema, limpar o contexto inteiro e reabrir sessão com prompt melhorado —, demonstrada na ferramenta | — |
| E03 · E05 · E06 · E07 · E13 | ND | — | Origem e data; canal com data; nenhuma superfície inspecionável; autoria e termos; nenhuma medição do efeito afirmado |
| E15 ⚠ | 1 | Alegações com fonte citada porém não conferidas: o vídeo **atribui a recomendação a "um documento da Anthropic"** sem exibir o documento, e afirma relação causal entre acúmulo de fracassos e degradação da resposta. `94` registra que "a fonte atribuída à Anthropic e a causalidade sobre alucinação não foram verificadas" | — |

**NF = 1 · 2/7 · 5 ND** *(mediana [1,2] = 1,5 → §14.3)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E01 | 3 | Endereça diretamente a pergunta central pelo lado da **qualidade**: é regra de parada, que impede correção ruim de se empilhar | — |
| E04 | 3 | Transferível com adaptação declarada: "limite de tentativas + preservar diagnóstico + reiniciar limpo" é regra operacional independente de ferramenta | — |
| E14 | 2 | Conveniência: o mesmo mecanismo aparece, por outro caminho, em `AC-08-VID-008` (passagem explícita) e no item `ralph-main` da área 03, ambos já no acervo | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E08 · E09 · E10 · E11 · E12 | 3 · 5 · 4 · 5 · 4 | Valor fixo de mídia do índice §3.3 | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 1** — **assunto pelo título**: a tabela registra "erros comuns e como corrigir" e o tamanho. É genérico demais para o conteúdo observado, que tem regra e limiar; mas não afirma nada falso.
**O que o catálogo afirma:** "| `erros e correcóes.mp4` | 44 MB | erros comuns e como corrigir |"
**Confere com a fonte:** sim, no pouco que afirma

#### Alegações registradas
| Alegação (conteúdo aproximado — **STT automático** e texto em tela) | Origem | Camada | Verificada? |
|---|---|---|---|
| que a recomendação vem de "um documento da Anthropic" | quadros (`94`) e LV3-A (`117`) | ALEGAÇÃO DO AUTOR — **atribuição de autoridade** | **não** — o documento não é exibido; `94` registra a não verificação |
| que insistir depois de dois fracassos degrada as respostas seguintes | quadros e LV3-A | ALEGAÇÃO DO AUTOR — causal | **não** — sem medição |

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

### AC-09-VID-002 — `Gravando 2026-07-28 164102.mp4`

**Tipo:** VÍDEO · **Área:** 09_SEGURANCA-E-QUALIDADE
**Hash F0:** `DADD32FE83806418`   **Hash reconferido:** `DADD32FE83806418`   **Confere:** sim
**LV:** **LV3-V + LV3-A** — a soma **não** produz LV4
**Cobertura da leitura:** quadros-chave (`94`) mais transcrição automática bruta (`117`): 31,7 s, `pt`, 98 palavras, 8 segmentos, confiança 0,881, **ALTA AUTOMÁTICA**. Não revisada; **proibido citar como literal**.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-09-VID-002 · `H-M2-001` (`94`) · `H-M3-001` · `117`

#### Bloco A — Fonte
| Eixo | Nota | Evidência | Se ND: o que resolveria |
|---|---|---|---|
| E02 | 2 | Descrição com detalhe reproduzível, sem artefato — **a mais concreta dos sete vídeos**: um caso com sinais nomeados (alerta de encerramento por memória, recusa de conexão a um cache, tempo esgotado em serviço, três reinícios em dez minutos, latência de cauda em 184 ms), hipótese de causa, evolução de confiança e plano de ação com três passos e **estado final "aguardando aprovação"**. Ainda assim: é demonstração, não artefato | — |
| E03 · E05 · E06 · E07 · E13 | ND | — | Origem e data; canal com data; nenhuma superfície inspecionável; autoria e termos; **nenhuma verificação pós-ação é exibida** |
| E15 ⚠ | 1 | Alegações com fonte citada porém não conferidas: a **confiança evoluindo de 33% para 92%** é exibida como número sem método de cálculo, e a correção da causa raiz não é demonstrada. `94` registra: "a demonstração não prova correção da causa raiz nem segurança das ações sugeridas" | — |

**NF = 1 · 2/7 · 5 ND** *(mediana [1,2] = 1,5 → §14.3)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E01 | 3 | Endereça diretamente a pergunta central: observabilidade e aprovação humana são exatamente "saber que o sistema funciona" | — |
| E04 | 2 | Transferível com adaptação **não declarada**: a separação coleta → correlação → hipótese → confiança → plano → aprovação viaja, mas depende de telemetria que o vídeo não especifica | — |
| E14 | 3 | Resolve problema declarado sem equivalente pronto **dentro do acervo**: é o único item que mostra **porta de aprovação humana antes de ação em produção**, com trilha de evidência | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E08 · E09 · E10 · E11 · E12 | 3 · 5 · 4 · 5 · 4 | Valor fixo de mídia do índice §3.3 | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — **título pelo conteúdo visível** ("agente de observabilidade para investigar eventos, contexto e sugerir ação") **confirmado** pela análise de quadros em `94`, inclusive quanto ao "sugerir" — o plano fica aguardando aprovação, não executa.
**O que o catálogo afirma:** "| `Gravando 2026-07-28 164102.mp4` | 27,9 MB | agente de observabilidade para investigar eventos, contexto e sugerir ação | não transcrito |"
**Confere com a fonte:** sim — marcador "não transcrito" **superado** por `117`

#### Alegações registradas
| Alegação (conteúdo aproximado — **STT automático** e texto em tela) | Origem | Camada | Verificada? |
|---|---|---|---|
| confiança da hipótese subindo de 33% para 92% | quadro, via `94` | ALEGAÇÃO DO AUTOR — número exibido sem método | **não** — `NÃO VERIFICADA` |
| a hipótese de falha de cache causando reinícios em cascata | quadro, via `94` | ALEGAÇÃO DO AUTOR — inferência do agente demonstrado | **não** — `94` registra que a correção da causa raiz não é provada |
| os valores de evidência exibidos (três reinícios em dez minutos, latência 184 ms) | quadro, via `94` | **FATO OBSERVADO** — na tela | sim, quanto ao que está exibido; a origem dos números não foi verificada |

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

### AC-09-VID-003 — `Gravando 2026-07-28 203100.mp4`

**Tipo:** VÍDEO · **Área:** 09_SEGURANCA-E-QUALIDADE
**Hash F0:** `A22DC01AF3A61516`   **Hash reconferido:** `A22DC01AF3A61516`   **Confere:** sim
**LV:** **LV3-V** (sem LV3-A aproveitável)
**Cobertura da leitura:** quadros-chave (`94`, `H-M2-001`); áudio — 16,3 s, `en`, 1 palavra, confiança 0,751, **SEM FALA LEXICAL CONFIÁVEL** (`117`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-09-VID-003 · `H-M2-001` (`94`) · `117`

#### Bloco A — Fonte
| Eixo | Nota | Evidência | Se ND: o que resolveria |
|---|---|---|---|
| E02 | 1 | **Só carrossel**: apresenta o laço fazer → avaliar → criticar → reescrever → repetir e nomeia uma ferramenta, sem demonstração e sem medição | — |
| E03 · E05 · E07 · E13 | ND | — | Origem e data; canal com data; autoria e termos; nenhuma verificação exibida |
| E06 ⚠ | **1** | **Risco ativo declarado por terceiro, não confirmado por inspeção**: `94` registra que o vídeo exibe a instalação da ferramenta por **download encadeado a execução em shell**, e que "comando remoto encadeado a shell não deve ser executado sem inspeção, licença, hash e sandbox". O padrão de instalação **está na tela** — o que não está verificado é o que ele instala | — |
| E15 ⚠ | 1 | Alegações fortes com fonte citada porém não conferidas: que "OpenAI e Anthropic concordam" com a tese, e "1,49M pessoas viram" — a segunda é **prova social pura**, sujeita a **P-3**. `94` registra ambas como não verificadas | — |

**NF = 1 · 3/7 · 4 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E01 | 3 | Endereça diretamente a pergunta central: laço com critério de aprovação é mecanismo de qualidade | — |
| E04 | 2 | Transferível com adaptação **não declarada**: o laço é aplicável, mas o critério de nota e o de parada não são exibidos | — |
| E14 | 2 | Conveniência: o padrão de laço com crítica reaparece em `AC-09-VID-004` e `AC-09-VID-005`, ambos com mais detalhe | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E08 · E09 · E10 · E11 · E12 | 3 · 5 · 4 · 5 · 4 | Valor fixo de mídia do índice §3.3 | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — **título pelo conteúdo visível** ("loops autoavaliados com plan-optimizer") **confirmado** pela análise de quadros em `94`.
**O que o catálogo afirma:** "| `Gravando 2026-07-28 203100.mp4` | 10,0 MB | loops autoavaliados com plan-optimizer | não transcrito |"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal, tal como exibida) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Prompts are dead. Build loops instead" | quadro, via `94` | ALEGAÇÃO DO AUTOR | não — `NÃO VERIFICADA` |
| que OpenAI e Anthropic "concordam" com a tese | quadro, via `94` | ALEGAÇÃO DO AUTOR — **atribuição de autoridade a terceiros** | **não** — nenhum documento é exibido |
| "1,49M pessoas viram" | quadro, via `94` | ALEGAÇÃO DO AUTOR — **prova social** | **não** — **P-3**: popularidade nunca é qualidade |
| instalação por download encadeado a shell, atribuída a `seangeng.com` | quadro, via `94` | **FATO OBSERVADO** (padrão exibido) | o padrão está na tela; **o que ele instala não foi inspecionado** — sustenta `E06 = 1` |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 | não | `E06 = 1`, **não 0** — o risco é do padrão exibido, e o alvo não foi inspecionado. Rejeitar aqui seria rejeitar por suspeita |
| **V2** | **sim** | `E06 = 1` → teto: nunca candidato |
| **V4** | **sim** | `E07 = ND` |
| V3 · V6 · V7 · V8 | não | `E07 ≠ 0` · 4 ND · `E15 = 1` (≠ 0) · hash confere |
| V5 | **não aplicado** | `LV = 3` |

#### Resultado
**RF = REFERÊNCIA** — §9, insumo de consulta com `LV ≥ 3`; critério §3.4 do índice. `V2` e `V4` já fechariam as classes de candidato.

> **Registro de risco, sem ação.** Esta frente **não** baixou, inspecionou nem executou a ferramenta citada — o que é proibido nesta fase. O padrão de instalação fica registrado como fato observado.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.

---

### AC-09-VID-004 — `Gravando 2026-07-28 203833.mp4`

**Tipo:** VÍDEO · **Área:** 09_SEGURANCA-E-QUALIDADE
**Hash F0:** `87DDC4FDF6612A91`   **Hash reconferido:** `87DDC4FDF6612A91`   **Confere:** sim
**LV:** **LV3-V** (sem LV3-A aproveitável)
**Cobertura da leitura:** quadros-chave (`94`, `H-M2-001`); áudio — 16,7 s, `en`, 1 palavra, confiança 0,751, **SEM FALA LEXICAL CONFIÁVEL** (`117`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-09-VID-004 · `H-M2-001` (`94`) · `117`

#### Bloco A — Fonte
| Eixo | Nota | Evidência | Se ND: o que resolveria |
|---|---|---|---|
| E02 | 2 | Descrição com detalhe **literalmente reproduzível**, sem artefato: estrutura de diretório nomeada (entrada e saída separadas), arquivo inicial, e o **prompt de revisão exibido por inteiro** — seguir o arquivo de instruções, revisar tudo que está na entrada, **não editar a entrada**, escrever relatório numerado na saída | — |
| E03 · E05 · E06 · E07 · E13 | ND | — | Origem e data; canal com data; inspeção direta; autoria e termos; nenhuma verificação exibida |
| E15 ⚠ | 1 | Alegação com fonte citada porém não conferida: o vídeo chama a checagem de "diária", mas `94` registra que "não demonstra agendamento, controle de duplicidade ou falhas" | — |

**NF = 1 · 2/7 · 5 ND** *(mediana [1,2] = 1,5 → §14.3)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E01 | 3 | Endereça diretamente a pergunta central: revisão automatizada é controle de qualidade | — |
| E04 | 3 | Transferível com adaptação declarada: o prompt e a separação entrada/saída **copiam-se literalmente**, sem depender de ferramenta específica — o próprio catálogo registra "com Codex ou Claude Code" | — |
| E14 | 3 | Resolve problema declarado sem equivalente pronto no acervo **como sequência de segurança**: começar **somente leitura**, com a fonte protegida de escrita, antes de permitir correção automática. É o princípio de menor privilégio aplicado a agente | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E08 · E09 · E10 · E11 · E12 | 3 · 5 · 4 · 5 · 4 | Valor fixo de mídia do índice §3.3 | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — **título pelo conteúdo visível** ("loop de revisão manual com Codex ou Claude Code") **confirmado** pela análise de quadros em `94`, inclusive quanto ao caráter manual do laço.
**O que o catálogo afirma:** "| `Gravando 2026-07-28 203833.mp4` | 3,4 MB | loop de revisão manual com Codex ou Claude Code | não transcrito |"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal, tal como exibida) | Origem | Camada | Verificada? |
|---|---|---|---|
| o prompt de revisão, incluindo "não edite a entrada" | quadro, via `94` | **FATO OBSERVADO** (texto exibido) | sim, quanto ao que está na tela |
| que a checagem seria "diária" | quadro, via `94` | ALEGAÇÃO DO AUTOR | **não** — nenhum agendamento é demonstrado |

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

### AC-09-VID-005 — `Gravando 2026-07-28 204533.mp4`

**Tipo:** VÍDEO · **Área:** 09_SEGURANCA-E-QUALIDADE
**Hash F0:** `CEFCACDEF936F55C`   **Hash reconferido:** `CEFCACDEF936F55C`   **Confere:** sim
**LV:** **LV3-V** (sem LV3-A aproveitável)
**Cobertura da leitura:** quadros-chave (`94`, `H-M2-001`); áudio — 16,4 s, `en`, 1 palavra, confiança 0,751, **SEM FALA LEXICAL CONFIÁVEL** (`117`).
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-09-VID-005 · `H-M2-001` (`94`) · `117`

#### Bloco A — Fonte
| Eixo | Nota | Evidência | Se ND: o que resolveria |
|---|---|---|---|
| E02 | 1 | **Só carrossel**: quatro capacidades nomeadas e um fluxo de quatro etapas, sem demonstração e sem artefato. O que salva o item é a **especificidade do protocolo descrito**, não a evidência que o sustenta | — |
| E03 · E05 · E06 · E07 · E13 | ND | — | Origem e data; canal com data; **o repositório citado não foi baixado nem inspecionado — proibido nesta fase**; autoria e termos; nenhuma verificação exibida |
| E15 ⚠ | 1 | Alegações com fonte citada porém não conferidas: que o protocolo produz veredito confiável, e que a revisão ocorre "em sandbox somente leitura" — condição de segurança **afirmada**, não demonstrada | — |

**NF = 1 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E01 | 3 | Endereça diretamente a pergunta central: é protocolo de revisão antes de construir | — |
| E04 | 2 | Transferível com adaptação **não declarada**: o fluxo é claro, mas depende de duas ferramentas distintas cooperando, e o vídeo não mostra o acoplamento | — |
| E14 | 3 | Resolve problema declarado sem equivalente pronto no acervo: **veredito binário com limite de cinco rodadas** e lista explícita do que procurar — falha de segurança, condição de corrida, caso de borda ausente, premissa errada — é protocolo mais específico que qualquer outro item da área | — |

**RP = 3 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E08 · E09 · E10 · E11 · E12 | 3 · 5 · 4 · 5 · 4 | Valor fixo de mídia do índice §3.3 | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — **título pelo conteúdo visível** ("Grill + Claude + Codex: plano, revisão, veredito e build") **confirmado** pela análise de quadros em `94`, que reproduz o fluxo nas mesmas quatro etapas.
**O que o catálogo afirma:** "| `Gravando 2026-07-28 204533.mp4` | 4,0 MB | Grill + Claude + Codex: plano, revisão, veredito e build | não transcrito |"
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal, tal como exibida) | Origem | Camada | Verificada? |
|---|---|---|---|
| o fluxo Grill → Review → Verdict → Build, com veredito aprovado ou revisar e teto de cinco rodadas | quadros, via `94` | **FATO OBSERVADO** (protocolo exibido) | sim, quanto ao que está na tela |
| que a revisão roda "em sandbox somente leitura" | quadro, via `94` | ALEGAÇÃO DO AUTOR — **condição de segurança** | **não** — afirmada, não demonstrada |
| o repositório `chaseai-yt/grill-me-codex` como origem | quadro, via `94` | ALEGAÇÃO DO AUTOR — atribuição de origem | **não** — está **fora do acervo**; `94` registra "Não instalar" |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · 5 ND · `E15 = 1` (≠ 0) · hash confere |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |
| V5 | **não aplicado** | `LV = 3` |

#### Resultado
**RF = REFERÊNCIA** — §9, insumo de consulta com `LV ≥ 3`; critério §3.4 do índice.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção. O repositório citado **não foi baixado** — está fora do acervo e fora do escopo desta fase.

---

### AC-09-VID-006 — `Gravando 2026-07-29 090207.mp4`

**Tipo:** VÍDEO · **Área:** 09_SEGURANCA-E-QUALIDADE
**Hash F0:** `FFA2AA3762397410`   **Hash reconferido:** `FFA2AA3762397410`   **Confere:** sim
**LV:** **LV3-V** (sem LV3-A aproveitável)
**Cobertura da leitura:** quadros-chave (`94`, `H-M2-001`); áudio — 8,4 s, `en`, 1 palavra, confiança **0,130**, **SEM FALA LEXICAL CONFIÁVEL** (`117`). **É o vídeo mais curto do acervo** e um dos dois de confiança mínima de STT.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-09-VID-006 · `H-M2-001` (`94`) · `117`

#### Bloco A — Fonte
| Eixo | Nota | Evidência | Se ND: o que resolveria |
|---|---|---|---|
| E02 | 1 | **Só listagem**: quatro perguntas para colar num agente. Nenhum procedimento, nenhum critério de aceitação, nenhuma demonstração | — |
| E03 · E05 · E06 · E07 · E13 | ND | — | Origem e data; canal com data; inspeção direta; autoria e termos; nenhuma verificação exibida |
| E15 ⚠ | 1 | Alegação com fonte citada porém não conferida, **e perigosa se aceita**: que pedir a uma IA para "revisar prompts contra injeção, listar o que está em produção e fazer varredura contínua" constitui auditoria de segurança. `94` registra o contra-argumento: isso "não substitui escopo, ferramentas, autorização, testes, revisão humana ou controles contínuos" | — |

**NF = 1 · 2/7 · 5 ND**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E01 | 2 | Endereça a pergunta de forma **genérica**: apenas uma das quatro perguntas trata de segurança, e ainda assim como pedido a um modelo, não como verificação | — |
| E04 | 2 | Transferível com adaptação **não declarada**: as perguntas copiam-se, mas nada garante que a resposta valha | — |
| E14 | 1 | Conveniência sobre conhecimento amplamente acessível: são perguntas de diagnóstico genéricas | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E08 · E09 · E10 · E11 · E12 | 3 · 5 · 4 · 5 · 4 | Valor fixo de mídia do índice §3.3 | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 5** — **título pelo conteúdo visível** ("auditoria de vida, segurança e a pergunta mais difícil") **confirmado** pela análise de quadros em `94`, que enumera as quatro perguntas na mesma ordem.
**O que o catálogo afirma:** "| `Gravando 2026-07-29 090207.mp4` | 1,6 MB | auditoria de vida, segurança e a pergunta mais difícil | não transcrito |… A auditoria de segurança também cita prompt injection, inventário de produção e varredura contínua."
**Confere com a fonte:** sim

#### Alegações registradas
| Alegação (literal, tal como exibida) | Origem | Camada | Verificada? |
|---|---|---|---|
| que pedir a uma IA para auditar segurança produz auditoria de segurança | quadro, via `94` | ALEGAÇÃO DO AUTOR — **implícita e forte** | **não** — `94` registra explicitamente que não substitui escopo, autorização, testes nem revisão humana |
| a pergunta sobre "o que, se eu melhorar, vai melhorar todo o resto" | quadro, via `94` | **FATO OBSERVADO** (texto exibido) | sim, quanto ao que está na tela |

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

### AC-09-VID-007 — `Gravando 2026-07-29 091447.mp4`

**Tipo:** VÍDEO · **Área:** 09_SEGURANCA-E-QUALIDADE
**Hash F0:** `879770140F9DF65B`   **Hash reconferido:** `879770140F9DF65B`   **Confere:** sim
**LV:** **LV3-V + LV3-A** — a soma **não** produz LV4
**Cobertura da leitura:** quadros-chave (`94`) mais transcrição automática bruta (`117`): 38,5 s, `pt`, 139 palavras, 11 segmentos, confiança 0,858, **ALTA AUTOMÁTICA**. Não revisada; **proibido citar como literal**.
**Data da avaliação:** 2026-07-29   **Avaliador:** Claude Opus 5 (Fase 2)   **Origem Codex:** AC-09-VID-007 · `H-M2-001` (`94`) · `H-M3-001` · `117`

#### Bloco A — Fonte
| Eixo | Nota | Evidência | Se ND: o que resolveria |
|---|---|---|---|
| E02 | 2 | Demonstração **na ferramenta**, com consulta real digitada, catálogo consultado e dois candidatos nomeados devolvidos. Sem artefato e sem critério de seleção exibido | — |
| E03 · E05 · E06 · E07 · E13 | ND | — | Origem e data; canal com data; nenhuma superfície inspecionável — **os candidatos devolvidos não foram baixados**; autoria e termos; nenhum critério de aprovação exibido |
| E15 ⚠ | 1 | Alegações fortes com fonte citada porém não conferidas: que o mecanismo "filtraria opções ruins" e permitiria vasculhar "**700.000 skills por IA**". `94` registra que "tamanho do catálogo, confiabilidade do hub e qualidade dos candidatos não foram verificados". **Registro a favor da fonte:** a própria resposta exibida avisa que as opções **não são de fonte oficial e não devem ser tratadas como totalmente confiáveis** — o material carrega o próprio contrapeso | — |

**NF = 1 · 2/7 · 5 ND** *(mediana [1,2] = 1,5 → §14.3)*

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E01 | 3 | Endereça diretamente a pergunta central — pelo avesso: mostra **como o material chega** ao sistema, que é onde a pergunta "é seguro instalar" começa | — |
| E04 | 2 | Transferível com adaptação **não declarada**: a busca depende de um catálogo de terceiro cuja confiabilidade não foi verificada | — |
| E14 | 2 | Conveniência sobre inventário já acessível: descoberta de skills também aparece na área 05; e o item que **verifica** o que se descobre já está nesta área, como `AC-09-REP-001` | — |

**RP = 2 · 3/3 · 0 ND**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência | Se ND |
|---|---|---|---|
| E08 · E09 · E10 · E11 · E12 | 3 · 5 · 4 · 5 · 4 | Valor fixo de mídia do índice §3.3 | — |

**AA = 4 · 5/5 · 0 ND**

#### Catálogo (separado da fonte)
**NC = 0 — DIVERGENTE.** O catálogo declara como "título pelo conteúdo visível": "**varredura de segurança de skills antes da instalação**". A inspeção de quadros da trilha Codex (`94`) mostra outra coisa — **busca de skills por catálogo**: uma consulta digitada, um índice de terceiro consultado e dois candidatos devolvidos, **sem qualquer varredura de vulnerabilidade**. O catálogo repete o erro no fecho da área, ao listar como terceira forma de controle um "scanner de skills contra vulnerabilidade/intenção maliciosa" — descrição que corresponde a `AC-09-REP-001`, não a este vídeo. Descoberta e verificação são operações diferentes, e trocá-las **inverte o sentido de segurança do item**.
**O que o catálogo afirma:** "| `Gravando 2026-07-29 091447.mp4` | 28,9 MB | varredura de segurança de skills antes da instalação | não transcrito |"
**Confere com a fonte:** **não** — ver a divergência acima

> Divergência **de catálogo**, não de fonte: o hash confere e **V8 não dispara**. Rebaixa `NC` a 0 e fica registrada. `NC` nunca entra em `NF` (`04` §12).

#### Alegações registradas
| Alegação (conteúdo aproximado — **STT automático** e texto em tela) | Origem | Camada | Verificada? |
|---|---|---|---|
| "700.000 skills" no catálogo consultado | quadro, via `94` | ALEGAÇÃO DO AUTOR | **não** — `NÃO VERIFICADA` |
| que o mecanismo "filtraria opções ruins" | quadros e LV3-A | ALEGAÇÃO DO AUTOR | **não** — nenhum critério de filtro é exibido |
| que as opções "não são de fonte oficial e não devem ser tratadas como totalmente confiáveis" | **resposta exibida na tela**, via `94` | **FATO OBSERVADO** — ressalva embutida no próprio material | sim, quanto ao que está na tela |
| "varredura de segurança de skills antes da instalação" | `_CONTEUDO.md` área 09 | **ALEGAÇÃO DO CATÁLOGO — DIVERGENTE** | **contradita** pela inspeção: o vídeo mostra descoberta, não varredura |

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V3 · V6 · V7 · V8 | não | `E06 ≠ 0` · `E07 ≠ 0` · 5 ND · `E15 = 1` (≠ 0) · **hash confere** |
| **V2 · V4** | **sim** | `E06 = ND` e `E07 = ND` |
| V5 | **não aplicado** | `LV = 3` |

#### Resultado
**RF = REFERÊNCIA** — §9, insumo de consulta com `LV ≥ 3`; critério §3.4 do índice.

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção. Nenhum dos candidatos exibidos foi baixado ou inspecionado.

---

## Fechamento da área 09 — contagem factual

**Itens com ficha:** 10 de 10 · **IDs faltando:** 0 · **IDs repetidos:** 0

| RF | Quantidade | IDs |
|---|---|---|
| CANDIDATO FORTE | 0 | — |
| **CANDIDATO A PILOTO** | **1** | `AC-09-REP-001` |
| PADRÃO A ESTUDAR · EXIGE PESQUISA | 0 | — |
| **REFERÊNCIA** | **9** | `AC-09-PRT-001`, `AC-09-PRT-002`, `AC-09-VID-001` a `AC-09-VID-007` |
| REJEITADO · DUPLICADO · INDETERMINADO | 0 | — |

| LV | Itens |
|---|---|
| LV4 | 1 (o único REPO) |
| LV3-V | 6 (2 PRINT + `VID-003`, `004`, `005`, `006`) |
| LV3-V + LV3-A | 3 (`VID-001`, `VID-002`, `VID-007`) |

**ND:** **45** de 150 células de eixo (10 itens × 15 eixos) = **30,0 %** — contados item a item: 1 no REPO, 5 em cada PRINT (10), 5 em cada um de `VID-001`, `002`, `004`, `005`, `006`, `007` (30) e **4** em `VID-003`. Nenhum item chegou ao gatilho de V6. Todos os 45 nomeiam o que os resolveria.

**Portas de veto na área:** V1 — 0 · **V2 — 9** (8 por `E06 = ND` e **1 por `E06 = 1`**, em `AC-09-VID-003`) · V3 — 0 · V4 — 9 · V5 — 0 (não aplicado a vídeo) · V6 — 0 · **V7 — 0, mas avaliada explicitamente em `AC-09-REP-001`** · **V8 — 0 divergências**: os 10 reconferem.

**Catálogo:** 5 com `NC = 5` (`VID-002` a `VID-006`) · 2 com `NC = 3` (`REP-001`, `PRT-002`) · **1 PARCIAL (`NC = 2`): `AC-09-PRT-001`**, por erro de hierarquia · 1 com `NC = 1` (`VID-001`) · **1 DIVERGENTE (`NC = 0`): `AC-09-VID-007`**.

**Registros novos desta área:**
1. **Segunda divergência de catálogo consecutiva** — `AC-09-VID-007`: o catálogo descreve varredura de segurança onde a inspeção mostra busca em catálogo. Somada às duas da área 08, o acervo acumula **três `NC = 0`** nesta rodada, todas por descrição de conteúdo, nenhuma por hash.
2. **Erro de hierarquia em transcrição de print** — `AC-09-PRT-001`: Nessus atribuído a Red Teaming onde o diagrama mostra Vulnerability Management. Primeiro caso do acervo em que o catálogo **redistribui** a estrutura do original, e não apenas a resume.
3. **Segundo e terceiro `E06 = 1` do acervo** — `AC-09-VID-003` aqui, após os dois da área 08. Todos por risco **declarado**, nenhum por risco confirmado; **nenhum foi rejeitado**.
4. **O item que verifica os outros está no acervo** — `AC-09-REP-001` é o único item que toma os demais como objeto. O catálogo propõe rodá-lo sobre as áreas 03 a 07; a proposta fica **registrada como verificação nomeada**, não executada: executar repositório é proibido nesta fase.
5. **Área com a maior taxa de ND desta rodada** (30,0 %) e a única com **um só repositório**.

> Esta seção é contagem de fichas, não classificação de valor. Não há ordenação, ranking ou recomendação.

