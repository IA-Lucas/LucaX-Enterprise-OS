> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

# 06 — CALIBRAÇÃO DA RUBRICA

**Frente:** Programa de Inteligência do Acervo · **Fase 1 — Rubrica**
**Data:** 2026-07-29
**Instrumento calibrado:** `04_RUBRICA-DE-AVALIACAO.md`, operado por `05_GUIA-DE-APLICACAO-DA-RUBRICA.md`

> **Este documento testa o instrumento, não avalia o acervo.** As dez fichas abaixo existem para descobrir onde a rubrica falha. Nenhuma delas é avaliação oficial de item, nenhuma delas transita para a Fase 2 como resultado, e nenhuma delas autoriza qualquer coisa. A avaliação real é Fase 2, e recomeça do zero.

---

## 1. Desenho do exercício

### 1.1 Amostra

Dez itens, conforme exigido: 3 repositórios documentados, 2 repositórios sem licença clara, 2 prints, 1 planilha, 2 vídeos sem transcrição.

| # | ID | Item | Categoria da amostra |
|---|---|---|---|
| 1 | `AC-03-REP-004` | `gstack-garrytan-main` | repositório documentado |
| 2 | `AC-04-REP-003` | `codebase-memory-mcp-main` | repositório documentado |
| 3 | `AC-10-REP-005` | `social-media-skills-blacktwist-main` | repositório documentado |
| 4 | `AC-02-REP-001` | `ai-orchestrator-starter` | **sem licença** |
| 5 | `AC-07-REP-002` | `frontend-design-main` | **sem licença** |
| 6 | `AC-08-PRT-001` | `Tolkenizaiton.png` | print |
| 7 | `AC-09-PRT-001` | `Captura de tela 2026-07-28 152706.png` | print |
| 8 | `AC-10-PLA-001` | `_construcao-civil/maiscontrole-dossie-jul2026.xlsx` | planilha |
| 9 | `AC-01-VID-001` | `Free Claude Code.mp4` | vídeo sem transcrição |
| 10 | `AC-09-VID-001` | `erros e correcóes.mp4` | vídeo sem transcrição |

### 1.2 Leitura autorizada neste exercício

A Fase 1 proíbe extração profunda. A leitura foi deliberadamente rasa e é declarada aqui por inteiro, para que o exercício seja reproduzível:

| Operação | Itens | Volume |
|---|---|---|
| Reconferência de SHA-256 | os 5 itens de mídia da amostra | 5 hashes |
| Listagem da raiz efetiva | os 5 repositórios | 5 listagens |
| Leitura do **texto** do `LICENSE` (3 primeiras linhas) | os 3 repositórios documentados | 3 leituras |
| Leitura **integral** do repositório | `AC-07-REP-002` — 3 arquivos, 9,3 KB | dentro do teto de `05` §8 |
| Leitura da linha de descrição no `_CONTEUDO.md` | os 10 itens | 10 linhas |
| Medição das durações de vídeo | 142 linhas de `92_MANIFESTO-TECNICO-DOS-VIDEOS.md` | agregado |

**Nenhuma fonte foi executada, movida, renomeada ou alterada.** Nenhum repositório foi percorrido em profundidade. Nenhuma imagem foi aberta. Nenhum vídeo foi aberto.

**Consequência assumida:** a amostra opera majoritariamente em `LV1` e `LV2`, com um único item em `LV3+`. Isso não é acidente — é a condição real de evidência disponível na Fase 1, e é justamente ela que testa se a rubrica fabrica certeza quando não deveria.

### 1.3 Reconferência de hash (porta V8)

Executada em 2026-07-29 sobre os 5 itens de mídia da amostra, contra `02_MANIFESTO-DAS-FONTES.md`:

| ID | Hash Fase 0 | Hash reconferido | Veredito |
|---|---|---|---|
| `AC-08-PRT-001` | `EA62DA1C5BDAFF8B` | `EA62DA1C5BDAFF8B` | confere |
| `AC-09-PRT-001` | `1C25B7AF0B095587` | `1C25B7AF0B095587` | confere |
| `AC-10-PLA-001` | `9B35BF396C57A0D4` | `9B35BF396C57A0D4` | confere |
| `AC-01-VID-001` | `8E00C68D6B3B30B5` | `8E00C68D6B3B30B5` | confere |
| `AC-09-VID-001` | `2EE427F03CFBF5C1` | `2EE427F03CFBF5C1` | confere |

**Divergências: 0.** V8 não disparou em nenhum item. Isso **não** encerra o bloqueio B-04 — cinco itens conferindo hoje não tornam o acervo estável; apenas confirmam que estes cinco não mudaram até esta data.

---

## 2. Fichas de calibração

Formato reduzido (só o que discrimina). O formato completo obrigatório da Fase 2 está em `04` §12.

---

### 2.1 · `AC-03-REP-004` — `gstack-garrytan-main` · REPO · área 03

**LV:** LV3 · **Cobertura:** listagem da raiz efetiva (97 entradas, não aninhada) + 3 primeiras linhas de `LICENSE`.

| Bloco | Eixos determinados | Notas |
|---|---|---|
| A | E07 = **4** | MIT License, "Copyright (c) 2026 Garry Tan", presente e íntegra na raiz efetiva. Não 5: cópia local não prova titularidade na origem |
| A | E02, E03, E05, E06, E13, E15 = **ND** | README, dependências, testes e superfície de risco não inspecionados |
| B | E01, E04, E14 = **ND** | — |
| C | E10 = **1** | 1.171 arquivos → faixa 1; 53,1 MB → faixa 1. Regra da pior das duas: 1 |
| C | E08, E09, E11, E12 = **ND** | — |

**NF = ND (1/7)** · **RP = ND (0/3)** · **AA = ND (1/5)** · **ND total = 13**
**NC = 2** — *"time virtual de engenharia"*: detalhe presente, não conferido (ver DEF-04).
**Vetos:** V6 (13 ND ≥ 8).
**RF = INDETERMINADO** — por V6.

---

### 2.2 · `AC-04-REP-003` — `codebase-memory-mcp-main` · REPO · área 04

**LV:** LV3 · **Cobertura:** raiz efetiva (aninhamento duplo resolvido; 33 entradas) + 3 primeiras linhas de `LICENSE`.

| Bloco | Eixos determinados | Notas |
|---|---|---|
| A | E07 = **4** | MIT License, "Copyright (c) 2025 DeusData" |
| A | demais = **ND** | — |
| B | todos = **ND** | — |
| C | E10 = **0** | 1,23 GB > 100 MB → faixa 0; 1.829 arquivos → faixa 1. Pior das duas: **0** |
| C | demais = **ND** | — |

**NF = ND (1/7)** · **RP = ND (0/3)** · **AA = ND (1/5)** · **ND total = 13**
**NC = 2** — *"grafo de conhecimento de código"*, não conferido.
**Vetos:** V6.
**RF = INDETERMINADO** — por V6.

**Observação de instrumento:** o único eixo com nota real, `E10 = 0`, é o pior valor da escala e foi obtido **sem ler nada** — é um fato físico medido na Fase 0. Isso confirma que `E10` em `LV1` funciona como projetado, e que o maior repositório do acervo já se anuncia como o mais caro de ler (risco R-04).

---

### 2.3 · `AC-10-REP-005` — `social-media-skills-blacktwist-main` · REPO · área 10

**LV:** LV3 · **Cobertura:** raiz efetiva (11 entradas) + 3 primeiras linhas de `LICENSE`.

| Bloco | Eixos determinados | Notas |
|---|---|---|
| A | E07 = **4** | MIT License, "Copyright (c) 2026 Social Media Skills Contributors". Titularidade coletiva genérica — sustenta 4, nunca 5 |
| A | demais = **ND** | — |
| B | todos = **ND** | — |
| C | E10 = **3** | 334,7 KB → faixa 4; **56 arquivos** → faixa 3. Pior das duas: **3** |
| C | demais = **ND** | — |

**NF = ND (1/7)** · **RP = ND (0/3)** · **AA = ND (1/5)** · **ND total = 13**
**NC = 3** — o catálogo afirma *"30+ skills"*; a Fase 0 contou **31** `SKILL.md` (`03_RELATORIO` §3.3). Detalhe verificável **e conferido** → 3. Não 4: o catálogo não declara o método.

**Alegações registradas:**

| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "30+ skills de redes sociais" | `_CONTEUDO.md` área 10 | `ALEGAÇÃO DO CATÁLOGO` | **sim** — 31 contados na Fase 0 |
| "De Charlie Hills (350k+ seguidores, 100M+ visualizações/ano)" | `_CONTEUDO.md` área 10 | `ALEGAÇÃO DO CATÁLOGO` · `NÃO VERIFICADA` | não |

**Vetos:** V6.
**RF = INDETERMINADO** — por V6.

**Teste-chave passado:** a alegação de popularidade (*350k+ seguidores, 100M+ visualizações*) foi registrada em alegações e **não moveu E14**, que permanece `ND`. A proibição P-3 funcionou.

---

### 2.4 · `AC-02-REP-001` — `ai-orchestrator-starter` · REPO · área 02 · **sem licença**

**LV:** LV3 · **Cobertura:** listagem da raiz efetiva (10 entradas, aninhamento resolvido). Busca por `LICENSE`/`COPYING`: **nenhum arquivo**.

| Bloco | Eixos determinados | Notas |
|---|---|---|
| A | **E07 = ND** | Nenhum arquivo de licença na raiz efetiva. **ND, não 0** — indeterminação de procedência, não permissão negada |
| A | demais = **ND** | — |
| B | todos = **ND** | — |
| C | E10 = **4** | 25 arquivos e 19,3 KB → ambos na faixa 4. Não 5: superfície mínima não declarada |
| C | demais = **ND** | — |

**NF = ND (0/7)** · **RP = ND (0/3)** · **AA = ND (1/5)** · **ND total = 14**
**NC = 2** — descrição com detalhe ("blueprint de orquestrador, em português"), não conferida.

**Alegações registradas:**

| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Comece pelo `ai-orchestrator-starter`. É o único item do acervo que já é um blueprint executável, não uma referência." | `_CONTEUDO.md` área 02 | `ALEGAÇÃO DO CATÁLOGO` · `NÃO VERIFICADA` | não |

**Vetos:** V4 (E07 = ND) · V6 (14 ND).
**RF = INDETERMINADO** — por V6. *(V4 também impediria CANDIDATO FORTE/PILOTO, mas V6 já decide.)*

**Teste-chave passado — o mais importante da calibração.** Este é o item que o catálogo elege como ponto de partida do acervo inteiro, com prioridade explícita e superlativo ("o único item que já é um blueprint executável"). A rubrica o classificou como `INDETERMINADO`, exatamente como classificou tudo o mais que não foi lido. **A prioridade declarada por terceiro não produziu nenhuma nota.** Era esse o risco R-05, e o instrumento resistiu.

---

### 2.5 · `AC-07-REP-002` — `frontend-design-main` · REPO · área 07 · **sem licença**

**LV:** **LV4** · **Cobertura: repositório integral** — `README.md`, `.claude-plugin/plugin.json`, `skills/frontend-design/SKILL.md`, listagem recursiva completa (3 arquivos, 2 diretórios, 9,3 KB). Busca por `LICENSE`/`COPYING`: **nenhum arquivo**.

> Único item da amostra em que a cobertura de leitura é de 100% da fonte. É o caso que testa se a rubrica **discrimina** quando a evidência existe.

#### Bloco A — Fonte

| Eixo | Nota | Evidência | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência | **3** | `SKILL.md` é artefato completo e inspecionável, com frontmatter estruturado, correspondente à afirmação do README. Nenhum procedimento de verificação | — |
| E03 Maturidade | **3** | `plugin.json` declara `"version": "1.1.0"`. Sem changelog, sem histórico de releases, sem política de compatibilidade | — |
| E05 Manutenção | **ND** | Autores nomeados com e-mail de contato, mas **nenhuma evidência datada de atividade**. Cópia estática sem histórico | Consultar a origem pública |
| E06 Segurança | **ND** | Inspecionado: sem credencial, sem shell, sem rede, sem execução. **Nenhuma âncora de E06 descreve item exclusivamente documental** — ver DEF-01 | Corrigir a âncora do instrumento |
| E07 Licença | **ND** | Nenhum arquivo de licença. **`SKILL.md` declara `license: Complete terms in LICENSE.txt` — e `LICENSE.txt` não existe nesta cópia** | Obter `LICENSE.txt` da origem pública |
| E13 Testes/evals | **0** | Repositório lido por inteiro: **nenhum teste, nenhum eval, nenhum diretório de verificação**. Ausência **confirmada por busca** → 0, não ND | — |
| E15 Alegações | **3** | Alegações do README são qualitativas ("production-grade", "avoid generic AI aesthetics"). Nenhum número decisivo em jogo | — |

**NF = 3 · 4/7 determinados · 3 ND** — mediana de [0, 3, 3, 3].

#### Bloco B — Relevância potencial

| Eixo | Nota | Evidência |
|---|---|---|
| E01 Relevância | **3** | Endereça diretamente a pergunta central da área 07 ("como o humano vê e comanda o sistema"). Fronteira 3↔4 ambígua — ver DEF-02; aplicada a âncora inferior |
| E04 Transferibilidade | **4** | Prosa + manifesto, sem credencial, sem infraestrutura, sem dado privado. Não 5: pressupõe host de plugin |
| E14 Diferencial | **ND** | Comparação com os demais repositórios de skills do acervo (`AC-05-REP-002`, `AC-04-REP-007`, `AC-10-REP-005`, `AC-10-REP-006`) **não realizada** |

**RP = 3 · 2/3 determinados · 1 ND** — mediana de [3, 4] = 3,5 → **arredondada para baixo** por DEF-03.

#### Bloco C — Atrito de adoção

| Eixo | Nota | Evidência |
|---|---|---|
| E08 Integração | **ND** | Nenhuma documentação de instalação. **Nenhuma âncora descreve "não requer instalação"** — DEF-01 |
| E09 Custo | **4** | Sem custo recorrente; consome apenas contexto de chamadas já previstas |
| E10 Contexto/tokens | **4** | 3 arquivos, 9,3 KB → ambos na faixa 4 |
| E11 Fornecedor | **2** | Formato `.claude-plugin/plugin.json`: host de fornecedor único, porém conteúdo em Markdown e JSON — formatos abertos |
| E12 Reversibilidade | **4** | Apenas arquivos, sem estado, sem efeito residual na remoção. Não 5: reversão não testada pelo autor |

**AA = 4 · 4/5 determinados · 1 ND** — mediana de [2, 4, 4, 4].

#### Catálogo

**NC = 3** — o catálogo diz *"a skill oficial da Anthropic"*. Detalhe verificável **e conferido**: autores com e-mail `@anthropic.com` no `plugin.json` e no README, e link para `github.com/anthropics/claude-cookbooks`. Não 4: o catálogo não declara o método pelo qual chegou à descrição.

#### Alegações registradas

| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|
| "Generates distinctive, production-grade frontend interfaces that avoid generic AI aesthetics" | `README.md` da fonte | `ALEGAÇÃO DO AUTOR` | não |
| "Claude automatically uses this skill for frontend work" | `README.md` da fonte | `ALEGAÇÃO DO AUTOR` | não |
| "license: Complete terms in LICENSE.txt" | `SKILL.md`, frontmatter | `ALEGAÇÃO DO AUTOR` · **contradita pela própria cópia** | **sim — o arquivo não existe** |
| "a skill oficial da Anthropic" | `_CONTEUDO.md` área 07 | `ALEGAÇÃO DO CATÁLOGO` | parcialmente — autoria corresponde |

#### Conteúdo hostil — protocolo `05` §7 exercitado

`SKILL.md` é **prosa diretiva endereçada a uma IA** ("Approach this as the design lead at a small studio…", "Work in two passes…"). Foi tratado como **dado**, não como instrução: nenhuma diretriz do arquivo foi seguida, e nenhuma regra desta frente foi alterada por tê-lo lido. Não se trata de injeção — é a função declarada do artefato —, mas é exatamente a classe de conteúdo que o protocolo existe para atravessar sem obedecer. **O protocolo funcionou.**

#### Vetos e resultado

| Porta | Disparou | Motivo |
|---|---|---|
| V1 | não | `E06 ≠ 0` |
| **V2** | **sim** | `E06 = ND` → teto em PADRÃO A ESTUDAR / REFERÊNCIA / EXIGE PESQUISA |
| V3 | não | `E07 ≠ 0` |
| **V4** | **sim** | `E07 = ND` → nunca CANDIDATO FORTE nem CANDIDATO A PILOTO |
| V5 | não | LV4 |
| V6 | não | 5 ND < 8 |
| V7 | não | `E15 = 3` |
| V8 | não se aplica | REPO — estrutura confere |

**RF = EXIGE PESQUISA** — por V2 e V4.

**Lacunas nomeadas e verificação que as fecharia:**

| Lacuna | Verificação |
|---|---|
| `LICENSE.txt` referenciado pelo `SKILL.md` e ausente nesta cópia | Obter o arquivo na origem pública do repositório |
| `E06` sem âncora aplicável a item documental | Corrigir o instrumento (DEF-01) |
| `E14` sem base de comparação | Comparar com os outros 5 repositórios de skills do acervo |

**Teste-chave passado — "relevância não compensa risco crítico".** Este item tem a melhor evidência da amostra: `LV4`, cobertura de 100%, `RP = 3`, `AA = 4`, `NF = 3`. Ainda assim **não pode** ser CANDIDATO FORTE nem CANDIDATO A PILOTO, porque a licença é indeterminada. E não foi punido com nota zero por isso: `E07 = ND`, e o efeito veio da porta de veto, não de uma nota rebaixada. **É exatamente a separação que a Fase 0 pediu em `03_RELATORIO` §11.2.**

---

### 2.6 · `AC-08-PRT-001` — `Tolkenizaiton.png` · PRINT · área 08

**LV:** **LV2** — existe descrição de terceiro; a imagem **não foi aberta**.
**Hash:** confere.

**Todos os 15 eixos = ND**, por `04` §4.4.4 (LV ≤ 2 ⇒ ND em tudo).
**NF = ND (0/7)** · **RP = ND (0/3)** · **AA = ND (0/5)** · **ND total = 15**
**NC = 2** — *"o que é um token, na prática"*: detalhe presente, não conferido contra a imagem.
**Vetos:** V5 · V6.
**RF = INDETERMINADO** — por V5.
**O que resolveria:** inspeção visual direta da imagem (`05` §2.2), que a levaria a `LV4` e permitiria, no máximo, `E02 = 2`.

---

### 2.7 · `AC-09-PRT-001` — `Captura de tela 2026-07-28 152706.png` · PRINT · área 09

**LV:** **LV2** · **Hash:** confere.

**Todos os 15 eixos = ND.**
**NF = ND (0/7)** · **RP = ND (0/3)** · **AA = ND (0/5)** · **ND total = 15**
**NC = 2** — *"mapa de cyber security"*, não conferido.
**Vetos:** V5 · V6.
**RF = INDETERMINADO** — por V5.

**Observação de área.** A área 09 tem 10 itens: 1 repositório, 2 prints e 7 vídeos (risco R-02). Este print é 1 dos 3 itens teoricamente legíveis da área inteira. Enquanto ele permanecer em `LV2`, a área 09 tem **um único** item potencialmente legível. Fato registrado; nenhuma conclusão extraída.

---

### 2.8 · `AC-10-PLA-001` — `maiscontrole-dossie-jul2026.xlsx` · PLANILHA · área 10

**LV:** **LV2** — conhecem-se os **nomes** das 10 abas (`03_RELATORIO` §3.1); o **conteúdo** não foi lido.
**Hash:** confere.

**Todos os 15 eixos = ND.** Inclusive `E10`: para itens de mídia, `E10` mede a evidência derivada, que ainda não existe (`04` §5, E10, regra para mídia).
**NF = ND (0/7)** · **RP = ND (0/3)** · **AA = ND (0/5)** · **ND total = 15**
**NC = 3** — *"Mais Controle ERP"*, e a Fase 0 conferiu detalhe estrutural verificável: 10 abas, 33,7 KB, nomes lidos de `xl/workbook.xml`.
**Vetos:** V5 · V6.
**RF = INDETERMINADO** — por V5.

**Alerta registrado para a Fase 2:** as abas `07 Vulnerabilidades` e `08 Concorrentes` contêm, pelo nome, juízo de terceiro. Ao serem lidas, entram como `ALEGAÇÃO DO AUTOR` e alimentam `E15` — nunca como fato observado.

---

### 2.9 · `AC-01-VID-001` — `Free Claude Code.mp4` · VÍDEO · área 01

**LV:** **LV1** — metadados técnicos apenas. Sem transcrição, sem quadros.
**Hash:** confere. **Metadados (`92_MANIFESTO-TECNICO`):** 59,5 s · 57,1 MB · 1024×1826 · aac 48 kHz · sem legenda embutida.

**Todos os 15 eixos = ND.**
**NF = ND (0/7)** · **RP = ND (0/3)** · **AA = ND (0/5)** · **ND total = 15**
**NC = 4** — o catálogo diz *"como usar Claude Code sem custo / plano gratuito"* e **declara o método** ("Título pelo conteúdo visível"), o que habilita 4 por `04` §6.1.5. Detalhe de tamanho confere: catálogo grafa "60 MB"; 57,1 MiB = 59,9 MB — consistente sob conversão MiB→MB, **não é divergência**. Só chega a 5 quando os quadros do Codex confirmarem que o título veio do frame e não do nome.
**Vetos:** V5 · V6.
**RF = INDETERMINADO** — por V5.
**Origem Codex:** `AC-01-VID-001` · `H-M1-001`.
**O que resolveria:** transcrição revisada **+** quadros-chave → `LV4`.

---

### 2.10 · `AC-09-VID-001` — `erros e correcóes.mp4` · VÍDEO · área 09

**LV:** **LV1** · **Hash:** confere. **Metadados:** 43,2 s · 41,8 MB · 1026×1836 · aac 48 kHz.

**Todos os 15 eixos = ND.**
**NF = ND (0/7)** · **RP = ND (0/3)** · **AA = ND (0/5)** · **ND total = 15**
**NC = 4** — *"erros comuns e como corrigir"*, com método declarado. Tamanho no catálogo: "44 MB"; 41,8 MiB = 43,8 MB — consistente.
**Vetos:** V5 · V6.
**RF = INDETERMINADO** — por V5.
**Origem Codex:** `AC-09-VID-001` · `H-M1-001`.

**Nota de disciplina:** o nome do arquivo é descritivo e a descrição do catálogo é plausível. Nenhuma das duas coisas produziu uma única nota. É o anti-padrão A-6 sendo barrado na prática.

---

## 3. Resultado agregado da amostra

| RF | Itens | Quais |
|---|---:|---|
| INDETERMINADO | **9** | 2.1 · 2.2 · 2.3 · 2.4 · 2.6 · 2.7 · 2.8 · 2.9 · 2.10 |
| EXIGE PESQUISA | **1** | 2.5 |
| CANDIDATO FORTE · CANDIDATO A PILOTO · PADRÃO A ESTUDAR · REFERÊNCIA · REJEITADO · DUPLICADO | **0** | — |

| Métrica | Valor |
|---|---:|
| Eixos possíveis (10 itens × 15) | 150 |
| Eixos **determinados** | **14** |
| Eixos em `ND` | **136** (90,7%) |
| Itens em LV1 | 2 |
| Itens em LV2 | 3 |
| Itens em LV3 | 4 |
| Itens em LV4 | 1 |
| Hashes reconferidos / divergentes | 5 / **0** |

**Leitura honesta destes números:** 90,7% de `ND` **não** é falha da rubrica. É a medida fiel da evidência que a Fase 1 tinha autorização de levantar. O único item lido por inteiro produziu 10 notas reais de 15 eixos — ou seja, **a rubrica discrimina exatamente na proporção em que é alimentada**.

---

## 4. Os seis critérios de calibração exigidos

| # | Critério | Veredito | Evidência na amostra |
|---|---|---|---|
| 1 | **Material ilegível recebe ND** | ✅ **passou** | Os 2 vídeos (`LV1`) e os 2 prints e a planilha (`LV2`) receberam `ND` em 15/15 eixos. Nenhum recebeu 0 |
| 2 | **Fonte fraca não recebe certeza artificial** | ✅ **passou** | Os 3 repositórios documentados, lidos só na superfície, produziram 1 nota cada e terminaram em `INDETERMINADO` por V6 — não em uma nota agregada aparentemente confiável |
| 3 | **Ausência de licença não vira nota zero automática** | ✅ **passou** | `AC-02-REP-001` e `AC-07-REP-002` receberam `E07 = ND`. O efeito veio da porta V4, não de nota rebaixada. `E07 = 0` permanece reservado a licença que **proíbe** |
| 4 | **Descrição de catálogo não substitui fonte** | ✅ **passou** | `AC-02-REP-001` — eleito pelo catálogo como ponto de partida do acervo ("Comece pelo…", "o único item que já é um blueprint executável") — terminou `INDETERMINADO`, igual a tudo o mais não lido. `NC` ficou isolada em todas as 10 fichas |
| 5 | **Relevância não compensa risco crítico** | ✅ **passou** | `AC-07-REP-002`, o item de melhor evidência da amostra (`LV4`, `RP = 3`, `AA = 4`), foi barrado de CANDIDATO FORTE e CANDIDATO A PILOTO por V2 e V4, e caiu em `EXIGE PESQUISA` |
| 6 | **Resultados reprodutíveis por outro avaliador** | ⚠️ **passou com ressalvas** | Os `ND` e as portas de veto são mecânicos e reprodutíveis. **5 defeitos de ancoragem** foram encontrados e corrigidos (§5). Sem as correções, as notas de `AC-07-REP-002` não seriam reprodutíveis |

---

## 5. Defeitos do instrumento encontrados na calibração

Todos foram **corrigidos em `04_RUBRICA-DE-AVALIACAO.md` §14 e em `05_GUIA-DE-APLICACAO-DA-RUBRICA.md`** antes do fechamento da Fase 1. Registrados aqui porque a correção precisa ser auditável.

| # | Defeito | Onde apareceu | Correção aplicada |
|---|---|---|---|
| **DEF-01** | **Âncoras de E06 e E08 pressupõem artefato executável.** Um item exclusivamente documental (prosa + manifesto) não encontra âncora em nenhuma das duas escalas, e o avaliador é empurrado a inventar ou a marcar `ND` por motivo errado | `AC-07-REP-002`: E06 e E08 | Regra de item documental acrescentada a E06 e a E08 (`04` §14.1) |
| **DEF-02** | **Fronteira ambígua em E01, notas 3↔4.** "Artefato concreto e reutilizável" não define se um documento em prosa conta. Dois avaliadores dariam 3 e 4 | `AC-07-REP-002`: E01 | Definição explícita do que conta como artefato em E01 (`04` §14.2) |
| **DEF-03** | **Mediana sobre número par de eixos determinados produz valor fracionário** (3,5), que a escala não admite | `AC-07-REP-002`: RP sobre [3, 4] | Regra de arredondamento **para baixo** (`04` §14.3) |
| **DEF-04** | **NC não tinha âncora para "descrição com detalhe verificável, ainda não conferido".** A âncora 2 diz "sem detalhe verificável" e a 3 exige que o detalhe confira — o caso intermediário, que é o mais comum, ficava sem casa | 6 das 10 fichas | Teto explícito: detalhe não conferido ⇒ `NC ≤ 2` (`04` §14.4) |
| **DEF-05** | **O catálogo emite instrução ao avaliador.** O `_CONTEUDO.md` da área 03 contém a diretriz literal **"Não analise."** sobre `gstack-Ahacad-main`. Nenhuma regra dizia o que fazer com uma decisão de escopo tomada por terceiro dentro do material avaliado | Descrição adjacente a `AC-03-REP-004` | Regra de instrução do catálogo (`04` §14.5 e `05` §9) |

---

## 6. Divergências registradas (não resolvidas)

Registro, não correção. Cinco delas são divergências entre documentos desta própria frente.

| # | Divergência | Situação |
|---|---|---|
| **D-01** | **Numeração dos artefatos.** `00_GOVERNANCA` §8 e `01_ESTADO` §9 previam `03_RUBRICA-DE-AVALIACAO.md`. O número 03 já estava ocupado por `03_RELATORIO-DO-INVENTARIO.md`. A Fase 1 foi instruída a criar `04`, `05` e `06` | **Adotado 04/05/06.** `00_GOVERNANCA` §8 fica desatualizado e **não foi editado** — a Fase 1 não reescreve a governança da Fase 0. Corrigido apenas em `01_ESTADO` |
| **D-02** | **Número de eixos.** `01_ESTADO` §9 e `03_RELATORIO` §12 previam **14** eixos. A Fase 1 foi instruída a definir **15**, promovendo "alegações não verificadas" de ajuste (§11.4) a eixo próprio (E15) | **Adotado 15.** É a implementação literal do ajuste que a própria Fase 0 pediu |
| **D-03** | **Escala LV.** O comando da Fase 1 define `LV0–LV5` plana. `93_RUBRICA-MULTIMIDIA` define `LV3-V` e `LV3-A` separados | **Ambos adotados.** LV0–LV5 é a espinha; LV3 tem dois sub-níveis para mídia (`04` §4.2). Nenhum sentido foi alterado |
| **D-04** | **Definição de LV4.** Comando: "fonte primária inspecionada". Codex `H-M1-001` item 6: "transcrição revisada combinada com quadros". Não são a mesma coisa | **Reconciliado por tipo de item** em `04` §4.3. Para VÍDEO vale a definição do Codex, literalmente |
| **D-05** | **Resultados permitidos.** `01_ESTADO` §9 lista **7**; o comando da Fase 1 lista **8**, acrescentando `INDETERMINADO` | **Adotados 8.** Sem `INDETERMINADO`, 140 vídeos não teriam classificação possível |
| **D-06** | **Tamanho da lacuna de vídeo, conforme a métrica.** 50,2% por contagem de itens · 2,91 GB por volume · **1,12 h** por conteúdo | **Não resolvida — as três são reportadas juntas** (`04` §10.3). Nenhuma métrica única é adotada como "a" medida da lacuna |
| **D-07** | **Caminho de destravamento dos vídeos.** `01_ESTADO` B-01 pressupõe transcrição. `91_ESTADO-DA-INTELIGENCIA-MULTIMIDIA` comprova que não há STT autorizado, mas que quadros são extraíveis | **Não resolvida.** Registrada como `HIPÓTESE` em `04` §10.3: com mediana de 19,3 s e 141/142 verticais, LV3-V/OCR **pode** ser o caminho principal. Só `H-M2-001` confirma ou refuta |
| **D-08** | **O catálogo decide escopo.** "Não analise." (área 03) e "candidato a descarte" (área 10, `3d de planta*`) são decisões de escopo tomadas por terceiro dentro do material sob avaliação | **Não obedecidas.** Registradas como `ALEGAÇÃO DO CATÁLOGO`. `FORA DE ESCOPO = 0` permanece deliberado |
| **D-09** | **Tamanhos de vídeo no catálogo × manifesto.** Catálogo: "60 MB" e "44 MB". Manifesto: 57,1 MB e 41,8 MB | **Não é divergência.** Consistente sob conversão MiB→MB (59,9 e 43,8). Registrado para não ser reaberto |

---

## 7. Limites desta calibração

Declarados para que ninguém tome este exercício por mais do que ele é:

1. **Um único item em `LV3+` com cobertura completa.** A capacidade da rubrica de discriminar entre itens **bem** evidenciados foi testada em `n = 1`. As faixas altas de quase todos os eixos permanecem não exercitadas.
2. **Nenhum item chegou a `LV5`.** Por desenho: esta frente não executa fontes. As âncoras 5 de E02 e E13 são, na prática, inalcançáveis aqui.
3. **Nenhum item recebeu `CANDIDATO FORTE`, `CANDIDATO A PILOTO`, `PADRÃO A ESTUDAR`, `REFERÊNCIA`, `REJEITADO` nem `DUPLICADO`.** Seis das oito classificações **não foram exercitadas**. `REJEITADO` em particular — nenhum item da amostra tinha `E06 = 0` nem `E07 = 0`.
4. **Nenhuma imagem foi inspecionada visualmente.** A trilha de `LV4` para PRINT está definida (`05` §2.2) mas **não testada**.
5. **Um único avaliador.** O critério 6 foi verificado por análise das regras — mecânicas e sem margem — e pelos 5 defeitos encontrados, não por dois avaliadores independentes. **Reprodutibilidade inter-avaliador permanece não medida empiricamente.**
6. **`DUPLICADO` não foi testado**, embora o acervo tenha 2 duplicatas exatas e 2 possíveis. A regra de herança de ficha (`05` §10) está escrita e não exercitada.
7. **Os 5 hashes que conferem não encerram B-04.** O acervo continua sob escrita concorrente por processo externo (I-06). A reconferência é obrigatória item a item na Fase 2, sempre.

---

## 8. Recomendação de método para a Fase 2

Não é roadmap, não é priorização e não ordena itens. É consequência direta dos números acima:

1. **Reconferir hash antes de qualquer leitura**, item a item. V8 é a primeira porta, não a última.
2. **Começar pelos 137 itens legíveis**, porque os 140 vídeos permanecem `LV1` até `H-M2-001`. Isso é sequência imposta pela evidência disponível, não priorização de valor.
3. **Respeitar o teto de leitura** de `05` §8. `AC-04-REP-003` já pontuou `E10 = 0` sem ser aberto: é o aviso de que ler tudo estoura contexto (R-04).
4. **Aceitar `ND` como resultado frequente e correto.** Uma ficha com muitos `ND` e as lacunas nomeadas vale mais que uma ficha completa e inventada.
5. **Reler `05` §7 antes de tocar em `AC-05-REP-003`** (`CL4R1T4S`). É o único item com risco de injeção declarado.
6. **Não produzir lista ordenada de candidatos.** Fichas por ID. Ordenar é roadmap (`04` §11).

---

> Nenhuma decisão oficial foi tomada nesta calibração. Nenhum item foi adotado, aprovado, descartado ou priorizado. Nenhuma Carta, Framework, ADR, Spec, Skill, Agente, Command, Workflow, arquitetura, política ou roadmap foi produzido. Nenhuma fonte foi modificada.
