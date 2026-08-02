> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

# 03 — BACKLOG DE VALIDAÇÃO

**Frente:** Programa de Inteligência do Acervo · **Missão A4** · **Data:** 2026-07-29
**Entrada:** as 67 pendências classificadas (`08_.../00_PRE-CORRECOES` §2), os 9 experimentos da matriz transversal §8 e as seções 10 das onze sínteses. **Nada aqui foi executado, autorizado ou agendado.**

**Origem:** external-evidence · **Autoridade:** nenhuma · **Estado:** provisório · **Normativo:** não · **Adoção:** não-decidida

> Este backlog registra hipóteses e verificações **para execução futura, fora desta frente**. "Responsável futuro" indica a natureza do ato (proprietário, pesquisador externo, leitor interno autorizado) — **não nomeia pessoa nem atribui tarefa**. Nenhuma entrada é plano aprovado.

---

## 1. Experimentos próprios (9) — todos DEPENDEM DO PROPRIETÁRIO

Os nove campos obrigatórios por experimento. Critérios de sucesso declarados de antemão, como exige a disciplina da própria rubrica.

### EXP-01 — Benchmark planejador caro + executor barato × modelo único
- **Hipótese:** separar planejamento (modelo caro) de execução (modelo barato) reduz custo sem perda relevante de qualidade.
- **Evidência atual:** `AC-01-VID-002` (NF=0, V7 — dois percentuais sem fonte); padrão repetido em `AC-03-VID-005`, `AC-08-VID-003`, `AC-08-VID-007` (P-3: repetição não verifica).
- **Responsável futuro:** proprietário (benchmark próprio).
- **Pré-condições:** tarefas e critérios definidos por esta casa; corpus real da casa; autorização de gasto de tokens.
- **Risco:** custo de inferência do próprio benchmark; conclusão datada (modelos mudam).
- **Custo:** médio (duas configurações × conjunto de tarefas × repetições).
- **Teste:** mesmo conjunto de tarefas nas duas configurações, medindo custo e desempenho com a rubrica desta casa.
- **Sucesso:** diferença de custo/qualidade medida e reproduzível em qualquer direção.
- **Abandono:** se a variância entre repetições impedir conclusão, ou se o corpus não discriminar as configurações.
- **Plano de saída:** resultado vira evidência **interna** (própria), não eleva o item externo; as cinco pendências da área 01 perdem ou ganham relevância conforme o desfecho.
- **Dependências:** nenhuma externa. Fecha a lacuna de `AC-01-VID-002`; informa Tools & Models.

### EXP-02 — Resposta única × deliberação por papéis
- **Hipótese:** decomposição em papéis (como `AC-03-VID-002` ou `AC-03-PRT-005`) supera resposta única em perguntas com resposta conhecida.
- **Evidência atual:** `AC-03-PRT-007` (V7 — quatro ganhos sem fonte); série deliberativa `AC-03-PRT-001`–`007` (REFERENCIA/PESQUISAR).
- **Responsável futuro:** proprietário.
- **Pré-condições:** conjunto de perguntas de resposta conhecida; rubrica própria definida antes de rodar.
- **Risco:** custo multiplicado por rodada; viés de confirmação na rubrica.
- **Custo:** médio-alto (N perguntas × 2 modos × registro de tokens e rodadas).
- **Teste:** medir acerto, custo em tokens e número de rodadas nos dois modos.
- **Sucesso:** acerto e custo medidos; conclusão em qualquer direção é válida.
- **Abandono:** se a rubrica não separar os modos de forma estável.
- **Plano de saída:** se não houver ganho, o padrão deliberação permanece REFERENCIA documental; lacuna de `AC-03-PRT-007` fechada por medição, não por fonte.
- **Dependências:** nenhuma externa. Informa Agents e Execution & Evaluation.

### EXP-03 — Chunk/overlap/k sobre corpus próprio (duas fichas, um experimento)
- **Hipótese:** os valores de chunk/overlap/k dos slides ("300 is optimal", k=5, faixa 3–10) se sustentam sobre corpus desta casa.
- **Evidência atual:** `AC-04-PRT-004` + `AC-04-PRT-007` (E15=1 — valores sem corpus nem método; lacuna contada uma vez); série `AC-04-PRT-002`–`013`.
- **Responsável futuro:** proprietário.
- **Pré-condições:** corpus desta casa; conjunto de perguntas com fonte conhecida; pipeline de ingestão+recuperação (pode usar `AC-04-REP-004` para ingestão).
- **Risco:** nenhum além de custo de computação/inferência.
- **Custo:** médio.
- **Teste:** variar chunk/overlap/k medindo qualidade de recuperação (taxa de afirmação sustentada pelas fontes) e custo por resposta.
- **Sucesso:** superfície custo × qualidade medida; valores de partida próprios, não importados.
- **Abandono:** se o corpus for pequeno demais para discriminar os parâmetros.
- **Plano de saída:** os números dos slides permanecem REFERENCIA; os medidos viram evidência interna. Informa Kernel técnico.
- **Dependências:** nenhuma externa.

### EXP-04 — "Zero alucinação" contra conjunto de resposta conhecida
- **Hipótese:** o método de `AC-04-VID-004` (pacote fechado de evidências) elimina alucinação.
- **Evidência atual:** `AC-04-VID-004` (V7 — "zero alucinação" sem medição; item sem conteúdo avaliável além do texto).
- **Responsável futuro:** proprietário.
- **Pré-condições:** conjunto de perguntas de resposta conhecida, incluindo perguntas-armadilha sem resposta nas fontes.
- **Risco:** nenhum além de custo.
- **Custo:** baixo-médio.
- **Teste:** medir taxa de afirmação sustentada e taxa de abstenção correta, com e sem o método.
- **Sucesso:** taxas medidas; "zero" quase certamente refutado — o valor é a taxa real, não a promessa.
- **Abandono:** se o método não for reproduzível a partir dos quadros (LV3-V).
- **Plano de saída:** item permanece PESQUISAR→REFERENCIA ou sobe apenas se a taxa medida justificar; informa Kernel técnico e Execution & Evaluation.
- **Dependências:** EXP-03 compartilha o conjunto de perguntas (economia declarada, não obrigatória).

### EXP-05 — Medição de consumo da persistência entre sessões
- **Hipótese:** a persistência por busca semântica de `AC-04-VID-002` reduz custo/melhora continuidade sem degradar contexto.
- **Evidência atual:** `AC-04-VID-002` (V7 — "memória infinita", "custo muito menor"; NC=0 — inspeção mostra skill de fechamento + busca semântica em plataforma de terceiro).
- **Responsável futuro:** proprietário.
- **Pré-condições:** **leitura prévia dos termos de tratamento de dado da plataforma** (ato jurídico-anexo); decisão sobre envio de conversa a terceiro.
- **Risco:** **dados da casa para plataforma de terceiro** — o experimento não pode começar antes da avaliação dos termos.
- **Custo:** baixo (instrumentação de tokens) + o custo jurídico da pré-condição.
- **Teste:** medir consumo por sessão com e sem a persistência, sobre tarefas repetidas da casa.
- **Sucesso:** consumo e degradação medidos; alternativa local (`AC-04-REP-002`) medida no mesmo desenho, se aplicável.
- **Abandono:** se os termos de tratamento de dado forem inaceitáveis — abandono antes do início.
- **Plano de saída:** se a plataforma for rejeitada nos termos, a hipótese migra para a via auto-hospedada (`AC-04-REP-002`, `AC-04-REP-006`).
- **Dependências:** questão jurídica J-01 (`05_LACUNAS`); informa Kernel técnico.

### EXP-06 — Medição do retorno das seis práticas de engenharia de prompt
- **Hipótese:** as seis práticas de `AC-05-PRT-013` produzem o retorno "80/20" alegado.
- **Evidência atual:** `AC-05-PRT-013` (V7 — proporção sem medição).
- **Responsável futuro:** proprietário.
- **Pré-condições:** escolher ao menos uma prática operacionalizável; definir medida observável (linhas geradas, retrabalho, tempo).
- **Risco:** prática mal operacionalizada mede a operacionalização, não a prática.
- **Custo:** baixo-médio.
- **Teste:** medir a medida escolhida com e sem a prática, sobre trabalho real desta casa.
- **Sucesso:** uma prática com efeito medido (ou refutado).
- **Abandono:** se nenhuma prática admitir medida observável estável.
- **Plano de saída:** o número "80/20" permanece alegação; a prática medida vira evidência interna. Informa Skills.
- **Dependências:** nenhuma externa.

### EXP-07 — Rastreabilidade de skill gerada automaticamente
- **Hipótese:** skills geradas pelo fluxo de `AC-05-VID-027` preservam rastreabilidade à fonte, regra a regra.
- **Evidência atual:** `AC-05-VID-027` (V7 — "cinco minutos/zero alucinações"; gate de revisão humana exigido por `99`).
- **Responsável futuro:** proprietário.
- **Pré-condições:** fluxo acessível; fonte documental de entrada definida; rubrica de conferência regra a regra.
- **Risco:** instrução gerada sem rastreabilidade é o próprio modo de falha medido — tratar saída como não confiável até o gate.
- **Custo:** baixo.
- **Teste:** gerar uma skill e conferir cada regra contra a fonte, registrando taxa de regras rastreáveis.
- **Sucesso:** taxa medida + gate humano documentado.
- **Abandono:** se o fluxo não expuser a ligação regra ↔ fonte.
- **Plano de saída:** se a taxa for baixa, o padrão "geração sem rastreabilidade" entra como risco em Skills. Informa Skills e Execution & Evaluation.
- **Dependências:** nenhuma externa.

### EXP-08 — Medida de sucesso observável para uma das sete promessas
- **Hipótese:** ao menos uma das sete promessas cognitivas de `AC-05-VID-004` admite medida observável.
- **Evidência atual:** `AC-05-VID-004` (V7 — "a proposta é a alegação"; sem conteúdo avaliável além do texto).
- **Responsável futuro:** proprietário.
- **Pré-condições:** escolher uma promessa e formalizá-la antes de qualquer teste.
- **Risco:** promessa informalizável → o próprio abandono é o resultado.
- **Custo:** baixo.
- **Teste:** definir medida; se definida, medi-la com e sem a prática.
- **Sucesso:** uma promessa com medida definida e resultado registrado.
- **Abandono:** se nenhuma promessa admitir formalização — encerra o item como REFERENCIA promocional.
- **Plano de saída:** o abandono documentado fecha a pendência tanto quanto o sucesso. Informa Skills.
- **Dependências:** nenhuma externa.

### EXP-09 — Abertura dos instrumentos de eval já existentes nas fontes
- **Hipótese:** os instrumentos de medição presentes nas fontes (`AC-08-REP-003`, `AC-03-REP-009`, `AC-06-REP-001`, `AC-10-REP-004`/`005`, `AC-07-REP-005`, `AC-08-REP-001`/`002`) respondem às lacunas E15/E06 sem execução de código.
- **Evidência atual:** os instrumentos existem e foram listados (fichas LV4); nenhum resultado foi lido (teto de `05` §8).
- **Responsável futuro:** proprietário (autorização de estouro de teto) → leitor interno autorizado.
- **Pré-condições:** autorização explícita de estouro do teto de leitura, por item.
- **Risco:** leitura ampliada de artefato de terceiro — manter protocolo de conteúdo hostil (`05` §7) em `AC-10-REP-004`/`005` (o acervo já provou injeção em `AC-05-REP-003`).
- **Custo:** baixo (leitura, sem rede, sem execução).
- **Teste:** abrir `eval/results`, `FINDINGS.md`, testes `abstention`/`gist-recall`/`needle-haystack` e equivalentes; registrar o que cada instrumento mede e o resultado encontrado.
- **Sucesso:** cada lacuna E15/E06 fechada por evidência da própria fonte, com registro de data e cobertura.
- **Abandono:** se os resultados não existirem ou não responderem à lacuna nomeada — o item permanece PESQUISAR com lacuna reescrita.
- **Plano de saída:** resultados lidos entram como emenda probatória nas fichas correspondentes (processo de emenda de `01_ESTADO` §10.8), nunca em silêncio.
- **Dependências:** autorização do proprietário; resolve as 7 pendências `INT⚠` e parte das `EXT`.

---

## 2. Verificações internas resolvíveis no teto vigente (5) — baixo custo, sem rede, sem execução

| # | Item | Verificação | Fecha |
|---|---|---|---|
| V-INT-1 | `AC-04-REP-001` | Ler `.skill`, `render-social-preview.js`, `social-preview.html` | E06=ND (superfície: Acesso Total ao Disco, Gmail) |
| V-INT-2 | `AC-05-REP-005` | Ler corpo de `SKILL.md` e `AGENTS.md` | E06=ND (skill declara `Write`/`Edit`) |
| V-INT-3 | `AC-05-REP-006` | Ler `USER-GUIDE.md` + corpo de `SKILL.md` | contradição `AC-05-VID-020` (modifica × não modifica) |
| V-INT-4 | `AC-05-VID-018` | Comparar quadros com README de `AC-09-REP-001` | identidade do scanner (SkillInspector × SkillSpector) |
| V-INT-5 | `AC-10-REP-001` | Ler `CONNECTORS.md` + 1 README de domínio; listar 11 diretórios | E06=2 e teste não localizado |

**Responsável futuro:** leitor interno (qualquer agente desta frente, sob as regras vigentes). **Pré-condição:** nenhuma além das regras já vigentes. **Risco:** baixo (manter protocolo de conteúdo hostil). **Custo:** minutos por item. **Sucesso:** lacuna fechada e ficha emendada com registro. **Abandono:** lacuna permanece nomeada. **Plano de saída:** cada item reavaliado pela rubrica após a leitura — sem promessa de promoção. **Dependências:** nenhuma.

## 3. Verificações internas que estouram o teto (7) — exigem autorização do proprietário

Cobertas pelo EXP-09: `AC-03-REP-009` (4 arquivos + recontagem em `v3/`), `AC-03-VID-001` (contagem em `AC-03-REP-002`), `AC-06-REP-001` (confinamento de `eval`), `AC-08-REP-003` (evals de preservação), `AC-10-REP-004` (419 arquivos), `AC-10-REP-005` (varredura + `VERSIONS.md`), `AC-07-REP-005` (contagens + escopo). Mesmos campos de EXP-09, por item, em `05_LACUNAS-E-QUESTOES.md` §interna.

## 4. Pesquisas externas (41) — leitura de fonte pública, sem instalar nada

| # | Item(s) | Pergunta a responder | Custo |
|---|---|---|---|
| V-EXT-1 | `AC-02-REP-001`, `AC-04-REP-007`, `AC-05-REP-002`, `AC-07-REP-002` | **Licença e titularidade na origem pública (B-02)** — fecha a porta V4 dos quatro | baixo |
| V-EXT-2 | `AC-03-REP-003` | Titular dos 7 arquivos do delta (LICENSE do upstream nomeia outro titular) | baixo |
| V-EXT-3 | `AC-01-VID-001` | Identidade, licença, custódia de chave e termos do gateway "OmniRoute" | baixo |
| V-EXT-4 | `AC-01-PRT-003`, `AC-01-PRT-005`, `AC-01-VID-004` | Metodologia dos placares/benchmarks/arena; identidade de "Mythos 5" | baixo-médio |
| V-EXT-5 | `AC-02-PRT-005` | Fonte primária da atribuição a Anthropic/OpenAI | baixo |
| V-EXT-6 | `AC-02-VID-006` | Identidade, licença e conteúdo do "OpenSpec" | baixo |
| V-EXT-7 | `AC-02-VID-009`, `AC-02-VID-011`, `AC-04-VID-008`, `AC-04-VID-012` | Identidade, repositório, licença e permissões de "PAUL"/"Graphify" — **uma pesquisa, quatro fichas** | médio |
| V-EXT-8 | `AC-03-PRT-001` (+6 da série) | Identidade da série do "conselho de IAs" — **uma pesquisa, sete fichas** | médio |
| V-EXT-9 | `AC-03-PRT-008` | Identidade do repositório "Loop Engineering" | baixo |
| V-EXT-10 | `AC-03-VID-003`, `AC-03-VID-004`, `AC-03-VID-005` | Identidade e escopo de permissão de plugins/conectores divulgados | médio |
| V-EXT-11 | `AC-03-VID-010` | Cinco repositórios nomeados (atenção: direito autoral em `ai-website-cloner-template`; risco financeiro em `daily_stock_analysis`) | médio |
| V-EXT-12 | `AC-03-VID-012` | "Hermes" do vídeo = `AC-03-REP-005`?; identidade de "SkillSmith" | baixo |
| V-EXT-13 | `AC-03-REP-006` | Superfície efetivamente distribuída via npm (manifesto de distribuição) | baixo |
| V-EXT-14 | `AC-04-REP-003` | **Ler o preprint arXiv:2603.27277** — os três números centrais | baixo |
| V-EXT-15 | `AC-04-VID-009` | Identidade, licença e permissões de 7 plugins + servidor MCP | médio |
| V-EXT-16 | `AC-05-VID-009` (+14 do cluster) | **Identidade/licença/escopo das skills do cluster promocional — uma pesquisa, quinze fichas; sem instalar nada** | médio |
| V-EXT-17 | `AC-05-PRT-004`, `AC-05-PRT-010` | Oficialidade/autoria atribuídas | baixo |
| V-EXT-18 | `AC-05-VID-002`, `AC-05-VID-003`, `AC-05-VID-021` | Identidade e licença dos retratados; origem dos números | baixo |
| V-EXT-19 | `AC-06-PRT-006` | Identidade, autoria e desempenho do produto de voz | baixo |
| V-EXT-20 | `AC-06-VID-006`, `AC-06-VID-012`, `AC-06-VID-020` | Origem das alegações comerciais; vínculo de afiliação | baixo-médio |
| V-EXT-21 | `AC-06-VID-008` | **Inspeção direta do navegador de evasão** — se confirmar função de evasão, V1 impõe rejeição | baixo |
| V-EXT-22 | `AC-06-VID-011` (+`AC-06-VID-003`/`004`/`005`) | Identidade, licença e superfície de execução das listas open source (sandbox, scraping, PI) | médio |
| V-EXT-23 | `AC-06-VID-019` | Identidade, licença e termos do produto cuja API não oficial é apresentada | baixo |
| V-EXT-24 | `AC-06-VID-023` | Enumerar as ~40 ferramentas do gateway na origem; classificar efeitos irreversíveis — **sem conectar conta**; fecha também o resíduo de transcrição por leitura, se a lista existir | baixo |
| V-EXT-25 | `AC-07-REP-003` | Superfície distribuída (`releases/`, `files[]` do `package.json`) | baixo |
| V-EXT-26 | `AC-10-PRT-016` | Publicação de origem do gráfico de 17 linhas + transcrição integral | baixo |
| V-EXT-27 | `AC-10-VID-019` | Existência e desempenho do configurador/validação/fábrica alegados | médio-alto |

**Campos comuns às 27 pesquisas (não repetidos por linha):** **Responsável futuro:** pesquisador autorizado a sair do acervo (ato que esta frente não praticou). **Pré-condições:** autorização de pesquisa externa; registro de fonte, data e trecho. **Risco:** fonte promocional tomada por primária; link encurtado não validado. **Custo:** conforme a coluna. **Teste:** a pergunta da linha, respondida com trecho citável. **Sucesso:** lacuna fechada com fonte citada e ficha emendada. **Abandono:** fonte inexistente ou não conclusiva → lacuna permanece, reescrita com o que foi descartado. **Plano de saída:** emenda probatória registrada; item reavaliado pela rubrica. **Dependências:** nenhuma entre pesquisas; V-EXT-7, V-EXT-8 e V-EXT-16 fecham famílias inteiras de uma vez.

## 5. Questões jurídicas (3) — não se resolvem por leitura de código

| # | Item | Questão | Responsável futuro |
|---|---|---|---|
| J-01 | `AC-04-REP-005` | Modo anti-detecção × termos de serviço de terceiro; autenticação persistente local | proprietário (avaliação jurídica) |
| J-02 | `AC-06-REP-002` | Contorno de controle de plataforma + reúso de login/cookies de cinco redes | proprietário (avaliação jurídica) |
| J-03 | `AC-06-REP-004` | Reúso de sessão autenticada ("your own keys and browser sessions") | proprietário (avaliação jurídica) |

**Pré-condição:** decisão do proprietário de submeter a avaliação. **Risco:** uso antes da avaliação pode violar termos de terceiro. **Custo:** desconhecido por esta frente. **Teste:** parecer jurídico. **Sucesso:** decisão fundamentada de uso, restrição ou descarte. **Abandono:** sem parecer, os itens **permanecem fora de qualquer piloto** — desconhecido não vira conclusão. **Plano de saída:** parecer registrado; itens reclassificados conforme o resultado. **Dependências:** nenhuma técnica. **Esta frente não responde pelo proprietário** — as três permanecem abertas.

## 6. Resíduos de transcrição (6) — só revisão humana de áudio fecha (B-01/B-05)

`AC-01-VID-005` (nomes de produto grafados errado) · `AC-01-VID-006` (fala não nomeia ferramentas) · `AC-06-VID-023` (escopo parcialmente falado — alternativa: V-EXT-24) · `AC-10-VID-021` e `AC-10-VID-022` ("a lista exata depende da fala") · `AC-11-VID-001` ("a fala pode conter critérios adicionais"). **Responsável futuro:** proprietário (mecanismo STT autorizado ou revisão humana). **Pré-condição:** decisão sobre B-05. **Sucesso:** fala revisada citável. **Abandono:** itens permanecem em seu estado atual — todos já estão em REFERENCIA, nenhum bloqueia candidato. **Plano de saída:** emenda com a fala revisada, se produzida. **Dependências:** B-01/B-05.

---

## 7. O que este backlog não é

Não é roadmap, não é plano aprovado, não é atribuição de tarefa, não é cronograma. A ordem das seções reflete **natureza do ato** (experimento → leitura interna → pesquisa externa → jurídico → transcrição), não prioridade. Executar qualquer item exige decisão fora desta frente.

> Este arquivo é evidência externa, provisória e não normativa. Não autoriza adoção de nada.
