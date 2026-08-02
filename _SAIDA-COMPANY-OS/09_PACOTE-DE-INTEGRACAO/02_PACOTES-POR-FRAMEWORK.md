> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

# 02 — PACOTES POR FRAMEWORK

**Frente:** Programa de Inteligência do Acervo · **Missão A4** · **Data:** 2026-07-29
**Entrada:** `01_CATALOGO-DE-CANDIDATOS.md` (esta pasta), sínteses de `08_SINTESES-DAS-11-AREAS/` e matriz transversal. Nenhuma fonte original aberta.

**Origem:** external-evidence · **Autoridade:** nenhuma · **Estado:** provisório · **Normativo:** não · **Adoção:** não-decidida

> Cada pacote organiza a evidência que **informa** um futuro Framework canônico, declara explicitamente **o que não prova** e indica **qual Goal canônico** pode consumi-lo. A existência de um pacote **não cria o Framework, não nomeia componente oficial e não autoriza adoção**. Promoção futura ocorre somente no Goal canônico correspondente. Os nomes de Goal abaixo são descritivos (o Goal que vier a instanciar o Framework), não identificadores oficiais — esta frente não conhece nem cria identificadores de Goals canônicos.

---

## 1. Specifications

**O que informa:**
- Portão obrigatório spec → código com spec assinada pelo humano, TDD vermelho/verde, YAGNI/DRY — artefato LV4: `AC-03-REP-010` (CANDIDATO-FORTE).
- Fluxo por fases com comando e portão entre elas (`/spec → /plan → /build → /test → /review → /ship`) — `AC-05-REP-001` (PILOTO).
- Roadmap de oito blocos colocando propósito, escopo e **critério de sucesso antes de framework** — `AC-02-PRT-003` (REFERENCIA).
- Materializar padrões como specs encadeando passos ("OpenSpec", identidade desconhecida) — `AC-02-VID-006` (PESQUISAR).
- Rubrica de forma para arquivo de instruções: dez blocos, < 500 linhas, instruções em vez de prosa — `AC-02-VID-013`; taxonomia de pastas — `AC-02-VID-001` (REFERENCIA).
- Contraponto protótipo × produto (pilha operacional item a item) — `AC-11-PRT-003` (REFERENCIA).

**O que não prova:** que qualquer formato de spec funcione — nenhum item mede resultado; "prompts genéricos não são Specs nem evidência de que o sistema funcione" (`AC-05-VID-029`, registro de `99`); a identidade do "OpenSpec" é desconhecida.

**Goal que pode consumi-lo:** o Goal canônico do Framework de Specifications.

## 2. Skills

**O que informa:**
- Anatomia mínima (quatro pastas; `SKILL.md` como artefato de runtime) — `AC-05-PRT-002` + artefato LV4 `AC-05-REP-005` (E04=5, PESQUISAR por E06=ND, INT✓).
- Ciclo de vida completo em cinco slides, com **teste de não ativação indevida** como critério — `AC-05-PRT-001`–`005`.
- Governança em escala: padrão de autoria, pipeline, changelog, portão de CI declarados — `AC-05-REP-004` (PESQUISAR, PROP); taxonomias skills × agents × personas e por departamento — `AC-05-VID-011`, `AC-05-VID-023`, `AC-10-VID-004`.
- Como a skill nasce: observação do trabalho (`AC-05-REP-006`, PESQUISAR INT✓), geração por fontes (`AC-05-VID-027`, PROP), entrevista (`AC-05-PRT-004`, EXT).
- Verificação determinística antes da instalação — `AC-09-REP-001` (PILOTO); o contra-exemplo fatal: injeção confirmada em `AC-05-REP-003` (REJEITAR).
- Frontmatter contratual (versão, licença, compatibilidade, ferramentas permitidas) — `AC-05-REP-005`.
- Distribuição multi-harness com manifests e schemas — `AC-03-REP-002` (PILOTO).

**O que não prova:** eficácia de qualquer skill — **nenhuma medição de eficácia existe na área 05** (síntese §8); o risco de auto-instalação é declarado, nunca medido; a lacuna de identidade do cluster promocional (15 fichas) está aberta (`AC-05-VID-009`).

**Goal que pode consumi-lo:** o Goal canônico do Framework de Skills.

## 3. Tools & Models

**O que informa:**
- Escolha por tarefa, não por modelo único — padrão recorrente (`AC-01-PRT-003`, `AC-01-PRT-005`, ambos PESQUISAR com números não verificados).
- Separação planejador caro × executor barato — `AC-01-VID-002` (PESQUISAR, PROP; benchmark local é a verificação), `AC-03-VID-005` (V7), `AC-08-VID-003`, `AC-08-VID-007` — repetição, não confirmação (P-3).
- Roteamento como nível da taxonomia de custo (Route) — `AC-08-VID-004` (sete níveis, NC=0 corrigido).
- Recuperação de documentação por versão contra API alucinada — `AC-06-REP-003` (PILOTO; alegação central sem eval lido, E15=1).
- Abstração de fornecedor como propriedade medida: E11=4 em `AC-03-REP-005`, `AC-03-REP-010`, `AC-04-REP-002`, `AC-04-REP-006`, `AC-05-REP-001`, `AC-07-REP-004`, `AC-08-REP-001`, `AC-09-REP-001`.
- Revisão adversarial por modelo de outro fornecedor — `AC-03-REP-001` (CANDIDATO-FORTE).

**O que não prova:** nenhum benchmark, placar Elo ou posição em arena — todos são alegação (área 01 inteira em LV3, 33,3% ND); a eficácia do roteamento nunca foi medida.

**Goal que pode consumi-lo:** o Goal canônico do Framework de Tools & Models.

## 4. Commands

**O que informa:**
- Comandos com contrato declarado e somente leitura (`/codex:review`, `/codex:adversarial-review`…) — `AC-03-REP-001` (CANDIDATO-FORTE).
- Comando por fase com portão (`/spec`…`/ship`) — `AC-05-REP-001` (PILOTO); 23 papéis como slash commands em Markdown — `AC-03-REP-004` (CANDIDATO-FORTE).
- 23 comandos de verificação de design — `AC-07-REP-004` (PILOTO, contagens não conferidas).
- Contra-evidência: "comandos secretos" e atalhos sem implementação são convenções promocionais, não comandos nativos — `AC-05-PRT-008`, `AC-05-PRT-009`, `AC-05-VID-006`, com o contra-exemplo visual de `AC-05-VID-001`.

**O que não prova:** que os comandos executem o que declaram — nenhum foi executado (proibido nesta frente); as contagens são alegações conferíveis não conferidas.

**Goal que pode consumi-lo:** o Goal canônico do Framework de Commands.

## 5. Workflows

**O que informa:**
- Loop com memória externa versionável e critério de parada (`prd.json` + `progress.txt` + contexto limpo + `max_iterations`) — `AC-03-REP-008` (PILOTO); formulação do padrão — `AC-03-PRT-008` (PESQUISAR).
- Loop avaliador com parada por rubrica — `AC-02-PRT-006`/`008`; regra de parada com limiar (2–3 tentativas → contexto limpo) — `AC-09-VID-001`; teto de cinco rodadas — `AC-03-VID-006`, `AC-09-VID-005`.
- Portão humano antes do irreversível — observado em fonte (`AC-10-REP-003`, `AC-03-REP-010`), declarado em prints (`AC-06-PRT-009`, `AC-06-PRT-011`); **declarado ≠ implementado** (matriz T-02/T-08).
- Handoff estruturado com cinco campos — `AC-08-VID-008` (fato observado); handoff entre sessões — `AC-03-REP-005` (CANDIDATO-FORTE).
- Fan-out com consolidação — `AC-03-PRT-003`, `AC-03-VID-011`, `AC-10-PRT-011`; pipeline de produção de conteúdo (ciclo fechado, adaptadores) — `AC-10-PRT-009`/`013`.
- Grafo executável de cinco estados (`triage → plan → execute → review → approval`) com Policy Engine — `AC-02-REP-001` (PESQUISAR, B-02).

**O que não prova:** que qualquer loop melhore resultado — nenhum ganho medido; o alerta contra loop infinito sem verificador (`AC-03-VID-012`) permanece alerta, não controle verificado.

**Goal que pode consumi-lo:** o Goal canônico do Framework de Workflows.

## 6. Agents

**O que informa:**
- Separação decide/executa/revisa com papel de revisão dedicado — `AC-03-REP-004` (CANDIDATO-FORTE), `AC-03-VID-002`/`006`/`007`, `AC-03-PRT-004`.
- Revisão por modelo de outro fornecedor como artefato — `AC-03-REP-001` (CANDIDATO-FORTE).
- Infraestrutura de agente sempre ativa: delegação, cron, handoff, loop de aprendizado — `AC-03-REP-005` (CANDIDATO-FORTE; ressalva E10=0).
- Isolamento de execução paralela por worktree — `AC-03-REP-007` (ADAPTAR-PADRAO; E06=2).
- Gateway como plano de controle, assistente como produto, 23 canais por adaptadores — `AC-03-REP-006` (PESQUISAR; superfície não delimitável).
- Deliberação por papéis como padrão documental — série `AC-03-PRT-001`–`007` (hipótese não medida; experimento proposto).
- Captura de memória por hook, sem disciplina do agente — `AC-04-REP-002` (CANDIDATO-FORTE).
- **Advertência registrada: papel ≠ agente autônomo** (`103`, sobre `AC-10-VID-011`).

**O que não prova:** que deliberação por papéis supere resposta única — os quatro ganhos de `AC-03-PRT-007` são V7; nenhum eval de comportamento de agente fora de `AC-03-REP-004` e `AC-07-REP-004`.

**Goal que pode consumi-lo:** o Goal canônico do Framework de Agents.

## 7. Execution & Evaluation

**O que informa:**
- Scanner de skills com testes nomeados por ameaça — `AC-09-REP-001` (PILOTO; **sem calibração lida** — taxa de detecção e falso positivo desconhecidas).
- Evals de comportamento de agente identificados em artefato — `AC-03-REP-004` (`skill-llm-eval`, `skill-routing-e2e`, `codex-e2e`), `AC-07-REP-004` (`skill-behavior/`), `AC-08-REP-001` (`evals/` por modelo), `AC-08-REP-002` (adversariais + relevância), `AC-10-REP-002` (regressão de segurança).
- Instrumentos de medição **presentes e não abertos** (teto de leitura): `eval/results`, `FINDINGS.md`, `abstention`/`gist-recall`/`needle-haystack` de `AC-08-REP-003`; `benchmarks/` de `AC-08-REP-001`; `compression_benchmark.py` de `AC-08-REP-002`; portão de cobertura de 84% de `AC-06-REP-004` (com `tests/` ausente — contradição).
- Mapa de evals e observabilidade no fluxo de produção — `AC-09-PRT-002` (nove blocos); pipeline de observabilidade com porta de aprovação — `AC-09-VID-002`.
- Falseabilidade embutida na saída ("como saberíamos que isto falhou?") — `AC-10-REP-002` (PILOTO).
- Único risco confirmado como caso-escola de injeção — `AC-05-REP-003` (REJEITAR).

**O que não prova:** **nenhum número de eficácia do acervo foi conferido** — nem economia de token, nem taxa de detecção, nem ganho de qualidade (lacuna L-04); os instrumentos existem nas fontes, os resultados não foram lidos.

**Goal que pode consumi-lo:** o Goal canônico do Framework de Execution & Evaluation.

## 8. Vertical Proof

**O que informa:**
- Empacotamento por domínio com ficha forte: SEO (`AC-10-REP-002`, PILOTO, falseabilidade embutida) e serviços financeiros (`AC-10-REP-003`, PILOTO, portão de revisão profissional no texto).
- Jurídico empacotado em onze domínios — `AC-10-REP-001` (PESQUISAR, INT✓).
- Marketing e social media como pacotes de skills — `AC-10-REP-004` (PESQUISAR, eixo único E06=2), `AC-10-REP-005` (PESQUISAR) e o delta editorial de `AC-10-REP-006`.
- Construção civil: única vertical com dossiê de mercado (`AC-10-PLA-001` — totais não reconciliados, risco jurídico) e sete vídeos (`AC-10-VID-014`–`020`), três com risco declarado (documento controlado sem responsável, dimensões inventadas, prospecção não solicitada).
- Padrão "uma fonte, dois destinos" — `AC-10-REP-001`, `AC-10-REP-003`; skill-fundação lida antes de todas — `AC-10-REP-004`, `AC-10-REP-005`.
- Inventários de casos de uso **sem critério de priorização** — `AC-10-PRT-006` (63), `AC-10-VID-012` (cem) — mapas, não decisão.

**O que não prova:** **nenhum resultado de negócio medido** — toda alegação de ganho é não verificada ou não verificável (síntese 10 §1); "render ≠ viabilidade" (`103`); o dossiê de construção civil tem totais internos inconsistentes e exige revisão jurídica antes de qualquer uso.

**Goal que pode consumi-lo:** o Goal canônico do Framework de Vertical Proof.

## 9. Kernel técnico

**O que informa:**
- Memória persistente em arquivo versionável lida por todas as skills (padrão T-03): `CLAUDE.md`, `AGENTS.md`, `progress.txt`, `PRODUCT.md`/`DESIGN.md` — `AC-02-VID-012`, `AC-03-REP-008`, `AC-07-REP-004`, `AC-10-REP-004`.
- Captura de memória por hook — `AC-04-REP-002` (CANDIDATO-FORTE; atenção ao fluxo para `cmem.ai`).
- Ingestão documental — `AC-04-REP-004` (CANDIDATO-FORTE); série RAG completa como mapa (sem parâmetro validado) — `AC-04-PRT-002`–`013`.
- Indexação estrutural de código em grafo via MCP — `AC-04-REP-003` (PESQUISAR; preprint não lido; E10=0).
- Compressão de contexto nos dois sentidos: saída (`AC-08-REP-001`, PILOTO) e entrada com consciência de tipo (`AC-08-REP-002`, PILOTO) — **somáveis, não concorrentes**; taxonomia de sete níveis — `AC-08-VID-004`; contexto como imagem — `AC-08-REP-003` (PESQUISAR, risco declarado).
- Conectividade: MCP de documentação (`AC-06-REP-003`, PILOTO), árvore de acessibilidade para agentes (`AC-06-REP-001`, PESQUISAR), roteamento de canais com degradação (`AC-06-REP-002`, PESQUISAR — pendência jurídica).
- Três vias de memória em disputa, **não decidida** (C-02): markdown puro × RAG próprio × RAG hospedado.
- Auto-hospedagem como mudança de natureza da fronteira — `AC-06-VID-003`; alternativa auto-hospedada completa — `AC-04-REP-006` (CANDIDATO-FORTE).

**O que não prova:** a decisão entre as vias de memória (aberta); a preservação semântica da compressão (instrumentos existem, resultados não lidos); a tensão C-01 "mais contexto × degradação" — aberta, não medida por nenhuma fonte.

**Goal que pode consumi-lo:** o Goal canônico do Kernel técnico.

## 10. Fábrica de Produtos

**O que informa:**
- Trabalho caro convertido em ativo reutilizável (`CLAUDE.md`, skills, `/goal`, workflows) — `AC-03-VID-009`.
- Uma fonte, dois destinos (plugin × agente gerenciado) — `AC-10-REP-001`/`003`; entrada canônica → N saídas com adaptadores por plataforma — `AC-10-PRT-011`/`013` com correspondente em artefato (`AC-10-REP-004`/`005`).
- Perfil escrito uma vez, lido por todas as skills — `AC-10-REP-004`, `AC-10-REP-005`, `AC-10-PRT-005`, `AC-07-REP-004` (`PRODUCT.md` + `DESIGN.md`).
- Componente de interface embutível e auto-hospedável — `AC-07-REP-001` (PILOTO; "não é ferramenta de agente", E01=2); verificação determinística de design — `AC-07-REP-004` (PILOTO); renderização de HTML em vídeo — `AC-07-REP-003` (PESQUISAR; E10=0).
- Regras de design reproduzíveis por pixel — `AC-07-PRT-001`–`005` (CONFIRMADA em `109`).
- Escada de adoção prompt → MCP → subagentes → automação — `AC-03-VID-013`.

**O que não prova:** que os padrões de empacotamento produzam produto vendável — nenhuma vertical tem resultado medido; a conversão de trabalho em ativo é formulação recorrente, não mecanismo verificado.

**Goal que pode consumi-lo:** o Goal canônico da Fábrica de Produtos.

---

## 11. Regras de consumo (valem para os dez pacotes)

1. Todo item citado carrega sua classe provisória; **classe não é prioridade nem autorização**.
2. Número vindo de item V7 (25 itens, `00` §3.5) **não é fato** em pacote nenhum.
3. Onde NC=0 (9 itens), vale a inspeção, nunca a descrição do catálogo.
4. Risco declarado (E06=1, 12 itens) nunca é escrito como risco confirmado; o único confirmado é `AC-05-REP-003`.
5. As 67 verificações PESQUISAR estão em `03_BACKLOG-DE-VALIDACAO.md` — nenhuma executada.
6. Promoção de qualquer item ocorre somente no Goal canônico correspondente, com os portões de `06_MATRIZ-DE-PROMOCAO.md`.

> Este arquivo é evidência externa, provisória e não normativa. Não autoriza adoção de nada.
