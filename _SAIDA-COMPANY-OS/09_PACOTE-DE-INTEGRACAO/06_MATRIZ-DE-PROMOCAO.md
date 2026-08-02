> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

# 06 — MATRIZ DE PROMOÇÃO

**Frente:** Programa de Inteligência do Acervo · **Missão A4** · **Data:** 2026-07-29
**Entrada:** `01_CATALOGO-DE-CANDIDATOS.md`, matriz transversal, sínteses. Nenhuma fonte original aberta; nenhuma decisão recalculada.

**Origem:** external-evidence · **Autoridade:** nenhuma · **Estado:** provisório · **Normativo:** não · **Adoção:** não-decidida

> Esta matriz traduz as classes provisórias do acervo para o vocabulário de promoção dos futuros Frameworks: `RETAIN-AS-REFERENCE` · `RESEARCH` · `PILOT` · `ADAPT` · `REWRITE` · `REJECT`. **Nenhum item recebe ADOPT — a classe não existe nesta matriz.** A promoção efetiva de qualquer item ocorre somente no Goal canônico correspondente, atravessando os nove portões do §2. A matriz não ordena por prioridade: ordena por classe e ID.

---

## 1. Mapeamento declarado (classe provisória → classe de promoção)

| Classe provisória (A3/A4) | Classe de promoção (A4) | Observação |
|---|---|---|
| CANDIDATO-FORTE (7) | PILOT (candidato a) | força estrutural (LV4 + licença lida); nenhum com eficácia medida |
| PILOTO (11) | PILOT (candidato a) | com as restrições nomeadas na ficha |
| ADAPTAR-PADRAO (1) | ADAPT (candidato a) | o valor é o padrão, não o artefato |
| PESQUISAR (67) | RESEARCH | com a classe de pendência de `03_BACKLOG` |
| REFERENCIA (190) | RETAIN-AS-REFERENCE | insumo de consulta; nunca componente |
| REJEITAR (1) | REJECT | único risco confirmado |
| DUPLICATA (2) | REJECT (como cópia) | conteúdo retido no original, sem segunda contagem |
| Padrões transversais sem artefato adotável (matriz §3) | REWRITE (candidato a) | reescrever nos termos canônicos se o Framework aprovar — o padrão transfere, o artefato não (T-10) |

## 2. Os nove portões (nenhum item os atravessou — nem deve atravessar aqui)

| # | Portão | O que exige | Onde está a evidência atual |
|---|---|---|---|
| P1 | **Licença** | lida e íntegra, titularidade verificada na origem | E07 dos LV4; B-02 aberto em 4+1 |
| P2 | **Evidência** | LV4 ou medição própria que responda à alegação central | nenhum candidato tem eficácia medida (L-04) |
| P3 | **Segurança** | superfície inspecionada ou varrida, não só declarada | E06 notado em 43 repositórios; varreduras pendentes (S-01) |
| P4 | **Dono** | responsável nomeado pelo Framework consumidor | fora desta frente |
| P5 | **Consumidor** | Framework canônico identificado e existente | indicado por item em `01_CATALOGO` — indicação, não atribuição |
| P6 | **Teste** | resultado de teste/eval executado ou lido | instrumentos existem nas fontes; resultados não lidos (EXP-09) |
| P7 | **Custo** | custo de adoção e de contexto medidos (E09/E10) e aceitos | medido nas fichas; aceitação é do Framework |
| P8 | **Substituição** | análise do que o item substitui ou desloca | fora desta frente |
| P9 | **Aprovação pelo Framework competente** | ato do Goal canônico correspondente | fora desta frente |

**Nenhum item do acervo atravessa P2 e P6 hoje** — é por isso que nenhum, nem os CANDIDATO-FORTE, pode receber mais do que "candidato a PILOT".

## 3. PILOT — candidatos (18)

| ID | Item | Portões já satisfeitos (parcial) | Portões abertos | Restrição principal |
|---|---|---|---|---|
| `AC-03-REP-001` | codex-plugin-cc | P1, P7 | P2, P3 (`plugins/` não lido), P4–P6, P8, P9 | fornecedor único por desenho (E11=2) |
| `AC-03-REP-002` | ECC | P1, P4(autor nomeado) | P2 (E15=1), P6, P8, P9 | E10=1; contagens em conflito (C-05) |
| `AC-03-REP-004` | gstack-garrytan | P1, P6 (evals presentes), P7 | P2 (método declarado, não verificado), P4, P8, P9 | instalação `git clone && ./setup` pelo agente |
| `AC-03-REP-005` | hermes-agent | P1, P4(Nous Research) | P2, P3 (superfície ampla), P7 (**E10=0**), P8, P9 | 6.265 arq. / 134 MB |
| `AC-03-REP-008` | ralph | P1, P7 | P2, P6 (**E13=1** — sem teste próprio), P4, P8, P9 | altera `AGENTS.md` do projeto |
| `AC-03-REP-010` | superpowers | P1, P4(Jesse Vincent), P7 | P2, P4(dono interno), P6, P8, P9 | hook de SessionStart injeta bootstrap |
| `AC-04-REP-002` | claude-mem | P1, P6 (213 testes) | P2, P3 (fluxo para `cmem.ai`), P4, P8, P9 | **E12=2** — reversão com perda |
| `AC-04-REP-004` | markitdown | P1 (Microsoft), P7 | P2, P6 (E13=ND), P4, P8, P9 | 2 ND no limite |
| `AC-04-REP-006` | open-notebook | P1, P6 | P2, P3 (extração remota, Crawl4AI), P4, P8, P9 | **E12=2**; infra permanente |
| `AC-05-REP-001` | agent-skills | P1 (Addy Osmani), P7 | P2 (E15=1), P6 (**E13=2**), P4, P8, P9 | evals sem ponto de entrada localizado |
| `AC-06-REP-003` | context7 | P1 (Upstash), P7 | P2 (**E15=1** — alegação central sem eval), P6 (E13=ND), P4, P8, P9 | **E11=2** — valor depende de índice hospedado |
| `AC-07-REP-001` | excalidraw | P1, P7 | P2, P4, P6, P8, P9 | E10=1; "não é ferramenta de agente" |
| `AC-07-REP-004` | impeccable | P1, P6 (394 testes) | P2 (**E15=2** — contagens não conferidas), P4, P8, P9 | extensão sem SECURITY.md |
| `AC-08-REP-001` | caveman | P1, P7 | P2 (**65% não conferido**), P4, P6 (resultado não lido), P8, P9 | estilo telegráfico × saída para humano (ressalva aberta) |
| `AC-08-REP-002` | headroom | P1, P3 (E06=4), P6 (evals presentes) | P2 (**reversibilidade não verificada**), P4, P8, P9 | duas runtimes (Python + Rust) |
| `AC-09-REP-001` | SkillSpector | P1, P3 (E06=4), P6 (testes por ameaça) | P2 (**sem calibração** — taxa de detecção desconhecida), P4, P8, P9 | custo recorrente por varredura (E09=3) |
| `AC-10-REP-002` | claude-seo | P1, P3 (E06=4), P6 | P2 (**E15=2** — contagens), P4, P8, P9 | até 15 agentes + serviços pagos (E09=3) |
| `AC-10-REP-003` | financial-services | P1, P3 (controle no texto) | P2, P4, P6 (E13=ND), P8, P9 | **E11=2** — dois destinos do mesmo fabricante |

## 4. ADAPT — candidato (1)

| ID | Item | O que se adapta | Portões abertos |
|---|---|---|---|
| `AC-03-REP-007` | orca | **padrão worktree-por-agente** (fan-out, comparar, merge do vencedor) — não o aplicativo | P2, P3 (**E06=2** — SSH, scrollback, Chromium), P6, P8, P9; E10=0 (9.477 arq., 127,3 MB) |

## 5. REWRITE — candidatos (padrões sem artefato adotável)

O artefato de origem não é adotável (mídia LV3, E06/E07=ND); o padrão, se o Framework competente o aprovar, deve ser **reescrito nos termos canônicos** — nunca copiado. Todos os portões abertos; P5 (consumidor) indicado:

| Padrão | IDs-fonte | Consumidor indicado |
|---|---|---|
| Portão humano antes do irreversível (spec→código; aprovação antes de efeito externo) | T-02: `AC-03-REP-010`, `AC-05-REP-001`, `AC-06-PRT-009`/`011`, `AC-10-REP-003` | Specifications; Workflows |
| Laço avaliador com critério de parada (rubrica, limiar de tentativas, teto de rodadas) | T-04: `AC-02-PRT-006`/`008`, `AC-09-VID-001`, `AC-09-VID-005`, `AC-03-VID-006` | Execution & Evaluation; Workflows |
| Memória/instrução persistente em arquivo versionável | T-03: `AC-02-VID-012`, `AC-02-VID-013`, `AC-03-REP-008`, `AC-07-REP-004` | Kernel técnico |
| Compressão de contexto em sete níveis (Meter→Budget→Route→Compact→Prune→Delegate→Batch) | T-12: `AC-08-VID-004` (NC=0 corrigido) | Kernel técnico; Tools & Models |
| Handoff estruturado em cinco campos | `AC-08-VID-008` | Workflows |
| Assimetria leitura × escrita (leitura ampla, escrita com portão) | T-08: `AC-06-PRT-009`/`011`, `AC-06-VID-010`/`022` | Kernel técnico; Agents |
| Verificação determinística antes de opinião de modelo | T-06: `AC-07-REP-004`, `AC-09-REP-001` | Execution & Evaluation |
| Falseabilidade embutida na saída ("como saberíamos que isto falhou?") | `AC-10-REP-002` | Vertical Proof; Execution & Evaluation |
| Skill-fundação / perfil escrito uma vez | `AC-10-REP-004`/`005`, `AC-10-PRT-005`, `AC-07-REP-004` | Fábrica de Produtos; Skills |
| Deliberação por papéis com protocolo explícito | `AC-03-PRT-002`–`006`, `AC-03-VID-002` | Agents — **suspensa por EXP-02** |

## 6. RESEARCH (67)

Mapeamento 1:1 de PESQUISAR. As 67 entradas — com hipótese, verificação, responsável futuro, custo e plano de saída — estão em `03_BACKLOG-DE-VALIDACAO.md` e não se repetem aqui. Subgrupos: 41 externas · 14 proprietário · 12 internas (5 no teto, 7 com autorização). Os cinco itens DEF-13 (`AC-04-REP-003`, `AC-05-REP-004`, `AC-05-REP-005`, `AC-07-REP-003`, `AC-07-REP-005`) carregam **dimensão secundária ADAPT** suspensa até a lacuna fechar.

## 7. RETAIN-AS-REFERENCE (190)

Mapeamento 1:1 de REFERENCIA, por área em `01_CATALOGO` §7. Regra: consulta permitida, citação com ID, **nunca como componente, nunca como fato verificado**; mídia carrega E06/E07=ND estrutural. Itens com marcações especiais: 9 NC=0 (vale a inspeção), 25 V7 (números proibidos como fato), 6 resíduos de transcrição, 12 E06=1 (risco declarado).

## 8. REJECT (3)

| ID | Classe de promoção | Motivo |
|---|---|---|
| `AC-05-REP-003` | REJECT | injeção de prompt confirmada (V1) — ver `04_REJEICOES` §1 |
| `AC-03-VID-008` | REJECT (como cópia) | duplicata exata de `AC-03-VID-007`; conteúdo retido no original |
| `AC-08-VID-005` | REJECT (como cópia) | duplicata exata de `AC-08-VID-004`; conteúdo retido no original |

**Candidatos a REJECT pendentes de evidência:** `AC-06-VID-008` (evasão — se inspeção confirmar, V1 impõe rejeição). Nenhum outro: rejeita-se por evidência, nunca por ND nem por suspeita.

## 9. Controle

| Classe de promoção | Itens |
|---|---:|
| PILOT (candidatos) | 18 |
| ADAPT (candidato) | 1 (+5 dimensões secundárias suspensas) |
| REWRITE (padrões) | 10 padrões (de 20+ IDs-fonte, sem contagem de item) |
| RESEARCH | 67 |
| RETAIN-AS-REFERENCE | 190 |
| REJECT | 3 (1 formal + 2 cópias) |
| **Total de IDs classificados** | **279** (18 + 1 + 67 + 190 + 3; REWRITE não conta ID — classifica padrões, não itens) |
| ADOPT | **0 — sempre** |

> Este arquivo é evidência externa, provisória e não normativa. Não autoriza adoção de nada.
