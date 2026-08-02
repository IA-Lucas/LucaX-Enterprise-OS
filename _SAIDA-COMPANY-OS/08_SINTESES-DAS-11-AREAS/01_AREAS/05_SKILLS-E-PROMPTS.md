> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

# SÍNTESE — ÁREA 05 — SKILLS E PROMPTS

**Frente:** Programa de Inteligência do Acervo · **Fase 3 — Síntese** (missão **A3**) · **Data:** 2026-07-29 · **Avaliador:** Claude Opus 5 (Fase 3)

**Origem:** external-evidence · **Autoridade:** nenhuma · **Estado:** provisório · **Normativo:** não · **Adoção:** não-decidida

**Entrada:** as 51 fichas de `_SAIDA-COMPANY-OS/07_FICHAS-DE-EVIDENCIA/05_SKILLS-E-PROMPTS.md` (6 REPO · 14 PRINT · 31 VÍDEO), lidas integralmente, mais as pré-correções de `00_PRE-CORRECOES-E-CORRESPONDENCIA.md`. **Pergunta central da área:** *como a capacidade é empacotada, versionada e instruída.*

---

## 1. O que sabemos

**Sobre a forma de empacotar capacidade.** A área cobre o ciclo de vida quase inteiro de uma skill, mas com profundidade muito desigual. Os únicos seis itens com leitura direta de artefato (LV4) são os seis repositórios: `AC-05-REP-001` (fluxo em seis fases com comando por fase e portões entre elas), `AC-05-REP-002` (arquivo único de instruções derivado de modos de falha nomeados do modelo), `AC-05-REP-003` (acervo de prompts de sistema de terceiros — rejeitado), `AC-05-REP-004` (biblioteca em escala com padrão de autoria e pipeline declarados), `AC-05-REP-005` (skill mínima e portátil com frontmatter contratual: versão, licença, compatibilidade e ferramentas permitidas) e `AC-05-REP-006` (meta-skill que observa o trabalho e propõe outras skills). Todo o restante — 45 itens — é evidência visual de tela (LV3-V), com três vídeos que têm também fala automática provável e não revisada (`AC-05-VID-002`, `AC-05-VID-014`, `AC-05-VID-020`).

**O que o acervo mostra, por tema:**

- **Anatomia mínima de uma skill.** A estrutura de quatro pastas (`SKILL.md` obrigatório, `scripts/`, `references/`, `assets/`) e a recomendação de começar só pelo `SKILL.md` aparecem declaradas em `AC-05-PRT-002` e exemplificadas com artefato real em `AC-05-REP-005`, cujo próprio README declara que "the runtime artifact is `SKILL.md`" (`E04 = 5`).
- **Ciclo de vida.** A série completa de cinco slides (`AC-05-PRT-001` a `AC-05-PRT-005`) cobre definição, estrutura, planejamento, geração e teste — e a nota de conjunto da própria ficha registra que nenhum slide traz uma skill real, um caso de teste executado ou um critério de aprovação medido. `AC-05-PRT-005` é o único material da área que exige **teste de não ativação indevida** como critério de qualidade (`E14 = 3`).
- **Portões.** O desenho mais explícito de "o agente não avança sem passar no portão" é `AC-05-REP-001` (`/spec → /plan → /build → /test → /review → /ship`, `E14 = 4`). O mesmo princípio aparece como portão de necessidade antes de gerar código (`AC-05-VID-021`), como inspeção de segurança antes da instalação (`AC-05-VID-018`) e como planejamento antes do prompt (`AC-05-PRT-003`).
- **Contexto persistente acima de pedido longo.** Convergem `AC-05-PRT-006` (mesma tarefa em três níveis de instrução), `AC-05-PRT-007` (perfil e exemplos persistentes separados do pedido momentâneo) e `AC-05-REP-002` (arquivo de instruções permanente).
- **Taxonomias e mapas.** Há mapas conceituais da superfície de um produto (`AC-05-VID-005`, 20 conceitos; `AC-05-PRT-012`, 10 níveis; `AC-05-VID-013`, 18 configurações), taxonomias organizacionais para bibliotecas de skills (`AC-05-VID-011`, 42 skills por departamento; `AC-05-VID-023`, 42 capacidades em camadas) e a distinção skill × plugin × MCP (`AC-05-VID-012`). O equivalente com artefato inspecionável é a taxonomia skills × agents × personas de `AC-05-REP-004`.
- **Templates de instrução.** `AC-05-VID-022` (sete elementos, com critério de saída) e `AC-05-VID-026` (oito blocos aplicados a quatro casos) decompõem o prompt operacional; `AC-05-VID-022` registra o achado de que especificidade operacional supera persona vaga.
- **Como a skill nasce.** Três caminhos distintos: por observação contínua do trabalho (`AC-05-REP-006`), por geração a partir de fontes documentais (`AC-05-VID-027`) e por entrevista geradora (`AC-05-PRT-004`, cuja atribuição de oficialidade não foi verificada).
- **Quem instala a capacidade.** O acervo retrata, sem inspecionar, uma skill que descobre **e instala** outras skills (`AC-05-VID-009`, repetido em `AC-05-VID-017`), e o contraponto conceitual de varredura antes da instalação (`AC-05-VID-018`). Nenhum dos dois mecanismos foi inspecionado.

**Sobre licenças.** Três situações distintas estão resolvidas por leitura: MIT íntegra com titular nomeado em `AC-05-REP-001`, `AC-05-REP-004` e `AC-05-REP-005` (teto 4: cópia local não prova titularidade); CC BY 4.0 — licença de **obra**, não de software — em `AC-05-REP-006` (`E07 = 3`); AGPL-3.0 em `AC-05-REP-003`, com a questão de titularidade registrada e não resolvida (o licenciante não é autor dos textos). **Licença ausente** na raiz efetiva de `AC-05-REP-002` (caso I-04 / bloqueio B-02, exige pesquisa externa). Todos os demais itens têm `E07 = ND`.

**Sobre segurança.** O único risco **confirmado** do acervo inteiro está nesta área: `AC-05-REP-003` contém, no README da raiz efetiva, uma injeção de prompt transcrita literalmente pela Fase 2 — instrução à IA leitora para revelar as próprias instruções de sistema — que foi lida como achado e **não obedecida** (`E06 = 0`, veto V1, `RF = REJEITADO`). Todos os demais riscos da área são **declarados e não confirmados** (`E06 = ND` em 45 fichas; ver §7).

**Sobre a fala dos vídeos.** Dos 31 vídeos, 28 resultaram `SEM FALA LEXICAL CONFIÁVEL`; três têm transcrição automática provável sem revisão humana (`AC-05-VID-002`, `AC-05-VID-014`, `AC-05-VID-020`). `AC-05-VID-024` é o único item do acervo com transcrição integralmente vazia (0 palavras). Nenhuma fala provável é tratada como fato nesta síntese; só quadros (LV3-V) sustentam afirmações sobre vídeo.

**Sobre a confiabilidade agregada.** Hashes e estruturas reconferidos: 51/51, zero divergências. Eixos em ND: 235 de 765 (30,7%), concentrados em E03, E05, E06, E07 e E13 nas fichas de print e vídeo (5 ND por ficha é o padrão).

## 2. Fontes mais fortes e por quê

- **`AC-05-REP-001` (`agent-skills-main`) — a mais forte da área.** LV4; `NF = 3 · 6/7 · 1 ND`; nenhuma porta de veto disparada; licença MIT lida e íntegra (`E07 = 4`); `RP = 4 · 3/3 · 0 ND`; `AA = 4`. Tem `evals/` com 25 arquivos e `cases/`, mas `E13 = 2` porque nenhum ponto de entrada de execução foi localizado, e `E15 = 1` por alegações promocionais não conferidas ("production-grade", "70+ agents" — P-3). É o único item que fecha CANDIDATO A PILOTO; não fecha CANDIDATO FORTE justamente por `E13 = 2` e `E15 = 1`.
- **`AC-05-REP-005` (`humanizer-main`) — evidência de forma mais limpa, pendência de segurança.** LV4; `AA = 5 · 5/5`; `E04 = 5` (Markdown puro, `compatibility: any-agent` declarado); MIT lida e também declarada no frontmatter. Mas `E06 = ND` (corpo de `SKILL.md` e `AGENTS.md` não lidos, numa skill que declara `allowed-tools` com `Write` e `Edit`), `E13 = 0` (nenhum teste na listagem completa) e V2 disparada → teto EXIGE PESQUISA. A lacuna é resolvível na própria fonte e cabe no teto de leitura.
- **`AC-05-REP-004` (`claude-skills-main`) — escala com governança declarada, números por conferir.** LV4; `E02 = 4` e `E03 = 4` (padrão de autoria, pipeline, changelog, portão de CI declarado); mas `E10 = 0` (9.210 arquivos, 85,7 MB), `E13 = 1` (`testpaths = ["tests"]` declarado sem diretório `tests/` na raiz — inconsistência observada) e contradição interna 345 × 355 skills no próprio README. As sete contagens do README são conferíveis dentro da fonte, mas estouram o teto de leitura — dependem do proprietário.
- **`AC-05-REP-002` (`andrej-karpathy-skills-main`) — conteúdo denso, lastro jurídico zero.** LV4; `E01 = 4`, `E10 = 5` (9 arquivos, 36,8 KB); mas licença **ausente** na raiz efetiva (V4, B-02), `E06 = ND` (4 de 9 arquivos não lidos; um caminho de instalação anexa conteúdo remoto via `curl` ao arquivo de instruções do projeto) e `E13 = 0`.
- **`AC-05-REP-006` (`one-skill-to-rule-them-all-main`) — desenho singular, alegação central sem fonte.** LV4; `E14 = 4` (único item cujo produto é a skill que propõe outras skills); controle relevante **declarado** ("doesn't modify your skills directly… you review"). Mas `E15 = 0` com V7 disparada ("600+ melhorias em 40 skills", sem fonte nem método) e `E06 = ND` num artefato que **escreve** no sistema de arquivos e observa todas as sessões.
- **`AC-05-REP-003` (`CL4R1T4S`) — LV4 e rejeitado.** A força da leitura (README integral, licença lida) é o que permitiu **confirmar** a injeção. Evidência forte, destino fechado: REJEITAR.

Os 45 itens restantes são LV3-V (quadros), com ou sem fala provável: por construção, nenhum deles pode sustentar mais do que REFERENCIA ou PESQUISAR, e nenhum número vindo deles entra como fato.

## 3. Padrões recorrentes

1. **Portão antes de avançar.** O padrão mais denso da área: portões entre fases de engenharia (`AC-05-REP-001`), portão de especificação antes do prompt (`AC-05-PRT-003`), portão de necessidade antes de gerar código (`AC-05-VID-021`), portão de segurança antes de instalar (`AC-05-VID-018`), portão de teste — inclusive de não ativação — antes de considerar a skill pronta (`AC-05-PRT-005`) e portão de revisão humana sobre instrução gerada automaticamente (`AC-05-VID-027`, gate exigido por `99`).
2. **Contexto persistente vence pedido longo.** `AC-05-PRT-006` (o melhor nível manda ler arquivos de contexto, proíbe execução imediata e faz perguntas), `AC-05-PRT-007` (perfil e exemplos persistentes separados do pedido), `AC-05-REP-002` (arquivo permanente de instruções) e `AC-05-PRT-010` (memória de lições em arquivo nomeado). Nenhum traz comparação medida — é padrão de forma, não de resultado.
3. **Descoberta, instalação e execução são atos separados.** O cluster promocional mistura os três; as fichas os separam: risco declarado de auto-instalação em `AC-05-VID-009` e `AC-05-VID-017` (regra candidata registrada por `99`: "descoberta pode ser automatizada; instalação, permissão e execução não"), cópia de marketplace sem inspeção intermediária em `AC-05-VID-014`, e o conceito de varredura prévia em `AC-05-VID-018`.
4. **"O padrão transfere; o artefato, não."** Fórmula recorrente em E04 = 2: `AC-05-PRT-004`, `AC-05-PRT-007`, `AC-05-VID-002`, `AC-05-VID-005`, `AC-05-VID-013`, `AC-05-VID-020`, `AC-05-VID-029`, `AC-05-VID-030`, `AC-05-VID-031`. A área é rica em padrões nomeados e pobre em artefatos transferíveis — só os seis repositórios e o frontmatter de `AC-05-REP-005` são artefato.
5. **Especificidade operacional supera persona.** `AC-05-VID-022` registra o achado explícito ("persona não concede expertise real"), coerente com os templates de `AC-05-VID-026` e `AC-05-PRT-006` — e em contradição frontal com `AC-05-VID-004` (ver §4).
6. **Listas não são capacidades.** Recorrência de índices de descoberta sem critério de seleção nem artefato: os 9 itens do cluster (`AC-05-VID-008`, `009`, `012`, `016`, `017`, `019`, `024`, `025`, `028`), mais `AC-05-VID-029`, `AC-05-VID-030`, `AC-05-VID-031`, `AC-05-PRT-008`, `AC-05-PRT-009` e `AC-05-VID-006`. A observação de `99` em `AC-05-VID-029` resume: "prompts genéricos não são Specs nem evidência de que o sistema funcione".
7. **Risco de uso de ocultação de autoria** reaparece três vezes, sempre registrado como inferência ou achado, nunca como fato de execução: `AC-05-REP-005` (função declarada de remover marcas de texto de IA), `AC-05-VID-015` (técnica "ghost") e `AC-05-VID-025`.

## 4. Conflitos e divergências

- **`AC-05-VID-020` × `AC-05-REP-006` — contradição material não resolvida.** A fala provável do vídeo afirma que a meta-skill "melhora as outras skills sozinha em segundo plano"; o README do repositório declara o oposto ("The observer doesn't modify your skills directly. It produces recommendations that you review."). Nenhuma das duas foi verificada; a leitura integral de `SKILL.md` e `USER-GUIDE.md` (já nomeada como lacuna em ambas as fichas) fecharia, e cabe no teto.
- **`AC-05-VID-001` × `AC-05-PRT-008`/`AC-05-PRT-009` — contradição de método.** O vídeo rejeita explicitamente a ideia de "comando secreto" (fato visual); os dois prints vendem exatamente isso ("Claude Commands Secret Codes", "All Claude Commands"), com `107` registrando que são convenções promocionais, não comandos nativos confirmados.
- **`AC-05-VID-022` × `AC-05-VID-004` — contradição de conteúdo.** Um afirma que persona não concede expertise; o outro vende persona como alavanca ("pensar como bilionário"). Mantidas as duas posições; nenhuma medida existe para arbitrar.
- **Contradição interna de `AC-05-REP-004`.** O mesmo README diz "345" e "355" skills; `pyproject.toml` aponta `testpaths = ["tests"]` sem diretório `tests/` na raiz efetiva. Não reconciliado nesta fase.
- **Identidade do scanner de `AC-05-VID-018`.** `99` observa "SkillInspector"; o catálogo grafa "SkillSpector" — nome que colide com `AC-09-REP-001`, já no acervo. A comparação dos quadros com o README de `AC-09-REP-001` é resolvível na própria fonte.
- **Catálogo × inspeção (higiene aplicada).** `AC-05-PRT-011` tem `NC = 0`: esta síntese usa **só** o que `107` mostra — **quatro seções** (conceitos de IA, produtos, recursos principais, agentes e automação); o bloco "Conta/API" do catálogo **não existe** na imagem e não é usado. Sete fichas têm `NC = 2` e entram só na parte confirmada: `AC-05-PRT-006` (o catálogo funde os níveis Better e Best), `AC-05-PRT-007` (três correções materiais, incluindo instrução inexistente atribuída ao print), `AC-05-REP-003` ("70 arquivos" × 99 medidos), `AC-05-REP-005` ("só quatro arquivos" × 6 medidos), `AC-05-VID-014` (omite que o objeto é a skill de revisão como segundo passo), `AC-05-VID-018` (grafia divergente + omissão do terceiro item), `AC-05-VID-023` (decomposição das 42 não confere), `AC-05-VID-026` (o catálogo descreve gradação; `99` observa anatomia de oito blocos).
- **Anomalia de agregação encontrada nesta fase.** O fechamento da área declara `EXIGE PESQUISA = 14` e `REFERÊNCIA = 35`; a contagem ficha a ficha refeita nesta síntese encontra **15 e 34** (ver §12). Também declara "7 parciais" listando **8** IDs com `NC = 2`. As fichas individuais prevalecem sobre os totais do fechamento; a divergência fica registrada, sem correção silenciosa.
- **DEF-13 recorrente.** `AC-05-REP-004` e `AC-05-REP-005` satisfazem simultaneamente as condições de PADRÃO A ESTUDAR e de EXIGE PESQUISA; prevaleceu EXIGE PESQUISA na Fase 2. Esta síntese mantém PESQUISAR para ambos e registra que a classe ADAPTAR-PADRAO ficou sem representante na área **por precedência de regra**, não por ausência de mérito de padrão.

## 5. Candidatos fortes, pilotos e referências

- **CANDIDATO-FORTE:** nenhum. Nenhum item fecha todos os eixos do Bloco A em 3 ou mais — os dois mais próximos param em `E13 = 2` / `E15 = 1` (`AC-05-REP-001`) ou carregam V2 (`AC-05-REP-005`).
- **PILOTO (1):** `AC-05-REP-001` — único item sem nenhuma porta de veto disparada, com `LV = 4`, `RP = 4` e licença lida. Restrições herdadas da ficha: `E13 = 2` (evals sem ponto de entrada localizado) e `E05 = ND` (sem changelog nem data na raiz). PILOTO é classe de registro, não autorização de piloto.
- **ADAPTAR-PADRAO (0):** vazio por precedência — `AC-05-REP-004` e `AC-05-REP-005` satisfazem a condição mas foram classificados EXIGE PESQUISA (DEF-13); permanecem PESQUISAR até as lacunas fecharem.
- **PESQUISAR (15):** com verificação **resolvível na própria fonte e dentro do teto**: `AC-05-REP-005`, `AC-05-REP-006`, `AC-05-VID-018`, `AC-05-VID-020` (as duas últimas compartilham leituras com as duas primeiras). **Dependente do proprietário**: `AC-05-REP-004` (contagem estoura o teto), `AC-05-PRT-013`, `AC-05-VID-004`, `AC-05-VID-027` (exigem experimento/medição própria). **Exige pesquisa externa**: `AC-05-REP-002` (licença — B-02), `AC-05-PRT-004`, `AC-05-PRT-010`, `AC-05-VID-002`, `AC-05-VID-003`, `AC-05-VID-009`, `AC-05-VID-021`.
- **REFERENCIA (34):** o corpo da área — padrões, mapas, taxonomias e listas consultáveis, todos LV3-V com 5 ND típicos. Destaques de conteúdo entre eles: a série de ciclo de vida (`AC-05-PRT-001` a `005`), o teste de não ativação (`AC-05-PRT-005`), os três níveis de instrução (`AC-05-PRT-006`), os mapas (`AC-05-VID-005`, `AC-05-PRT-012`), as taxonomias (`AC-05-VID-011`, `AC-05-VID-012`, `AC-05-VID-023`) e os templates (`AC-05-VID-022`, `AC-05-VID-026`).
- **REJEITAR (1):** `AC-05-REP-003` — único risco confirmado do acervo (injeção de prompt, V1). Permanece no acervo como referência de leitura sujeita ao protocolo de conteúdo hostil; nunca como componente.
- **DUPLICATA (0):** nenhuma nesta área. O cluster promocional é similaridade temática, não duplicata (§4.3 das pré-correções); `AC-05-PRT-014` é ponteiro redundante para `AC-05-REP-003`, mas com `E01 = 1` não cabe rejeição e permanece REFERENCIA vinculada.

## 6. O que não adotar

- **`AC-05-REP-003` como componente, em qualquer hipótese** — injeção de prompt confirmada por inspeção direta (V1). É o único REJEITAR do acervo; a própria ficha admite leitura futura apenas sob o protocolo de conteúdo hostil, porque a injeção continua no arquivo.
- **Qualquer número vindo dos 8 itens V7 como fato**: "80/20" (`AC-05-PRT-013`), "170 mil estrelas" (`AC-05-VID-002`), promessas médicas/produtividade e "semana em quatro horas" (`AC-05-VID-003`), as sete promessas cognitivas (`AC-05-VID-004`), "100 mil skills" e "retrabalho pela metade" (`AC-05-VID-020`), "54% menos código/custo/tempo" (`AC-05-VID-021`), "cinco minutos/zero alucinações" (`AC-05-VID-027`), "600+ melhorias em 40 skills" (`AC-05-REP-006`). Esses itens não têm conteúdo avaliável além do próprio texto no que depende do número.
- **As listas do cluster como base de instalação** (`AC-05-VID-008`, `016`, `017`, `019`, `024`, `025`, `028`): índices de descoberta sem critério de seleção, sem rubrica de segurança e com riscos declarados de instalação em massa, auto-instalação, postagem em canais reais e loop autônomo. Repetição nove vezes não é confirmação (P-3).
- **"Comandos" e atalhos sem implementação** (`AC-05-PRT-008`, `AC-05-PRT-009`, `AC-05-VID-006`): convenções promocionais apresentadas como comandos — a própria inspeção registra que não são comandos nativos confirmados.
- **A descrição de catálogo de `AC-05-PRT-011`** (NC = 0 — bloco inventado) e as partes não confirmadas das oito fichas NC = 2.
- **O glossário de produto de `AC-05-PRT-011` como documentação** — datado, amarrado a nomes comerciais, `RP = 1`.

## 7. Riscos e dependências

**Risco confirmado (1):** injeção de prompt em `AC-05-REP-003` (`E06 = 0`, V1) — o único do acervo.

**Riscos declarados, nunca confirmados (E06 = ND em todos):** auto-instalação de skills sem gate humano (`AC-05-VID-009`, `AC-05-VID-017`); loop autônomo apresentado sem checker, orçamento, idempotência e kill switch (`AC-05-VID-028` — com a ressalva registrada de que o loop citado tem ficha própria, `AC-03-REP-008`, onde o limite de iterações está documentado); instalação em massa e acesso amplo (`AC-05-VID-008`); integração com canais reais e postagem sem matriz de autorização (`AC-05-VID-019`); contrato automático e publicação com efeito externo ou jurídico (`AC-05-VID-030`) e skills de finanças/jurídico sem fontes autorizadas nem segregação de deveres (`AC-05-VID-011`); cópia de skill de marketplace colada como instrução sem inspeção (`AC-05-VID-014`); geração automática de instrução sem rastreabilidade à fonte (`AC-05-VID-027`); meta-skill que escreve no sistema de arquivos e observa todas as sessões (`AC-05-REP-006`, repercutido em `AC-05-VID-020`); 602 scripts CLI, hooks `PreToolUse`, `.mcp.json` e instalador `curl | bash` (`AC-05-REP-004`, controles apenas declarados); instalação por `curl` que anexa conteúdo remoto ao arquivo de instruções do projeto (`AC-05-REP-002`); permissões `Write`/`Edit` declaradas com corpo não lido (`AC-05-REP-005`); modo `/build auto` com controles apenas documentados (`AC-05-REP-001`).

**Dependências:** pesquisa externa para licença de `AC-05-REP-002` (B-02) e para identidade/oficialidade/autoria em `AC-05-PRT-004`, `AC-05-PRT-010`, `AC-05-VID-002`, `AC-05-VID-003`, `AC-05-VID-009` (lacuna do cluster inteiro, contada uma vez), `AC-05-VID-021`; ato do proprietário para `AC-05-REP-004` (autorização de leitura acima do teto), `AC-05-PRT-013`, `AC-05-VID-004`, `AC-05-VID-027` (experimentos próprios); revisão humana de áudio para os três vídeos com fala provável (`AC-05-VID-002`, `AC-05-VID-014`, `AC-05-VID-020`) — resíduo que só transcrição revisada fecha.

## 8. Lacunas

- **Licença ausente em `AC-05-REP-002`** (B-02) — o item de maior densidade de conteúdo da área não tem lastro jurídico verificado.
- **Identidade, licença e escopo de permissão de todas as skills nomeadas pelo cluster** — lacuna única, nomeada em `AC-05-VID-009`, cobrindo 9 fichas.
- **`E06 = ND` estrutural:** 45 fichas sem inspeção de segurança possível (prints e vídeos), e leitura integral pendente nos repositórios que escrevem ou executam (`AC-05-REP-002`, `AC-05-REP-005`, `AC-05-REP-006`).
- **Manutenção desconhecida:** `E05 = ND` em praticamente toda a área — nenhum item tem evidência datada de atividade, exceto sinais parciais (changelog sem data em `AC-05-REP-004`, versão em frontmatter em `AC-05-REP-005`).
- **Testes:** `E13 = 0` em `AC-05-REP-002`, `AC-05-REP-005`, `AC-05-REP-006` (listagens completas sem nenhum teste); evals sem ponto de entrada em `AC-05-REP-001`; `tests/` declarado e ausente em `AC-05-REP-004`; `E13 = ND` em todo o resto.
- **Fala desconhecida:** 28 vídeos sem fala lexical confiável; 3 com fala provável não revisada; o que a fala acrescenta é desconhecido em todos.
- **Nenhuma medição de eficácia em toda a área:** nenhum item traz experimento, benchmark ou critério de aprovação medido — a área inteira descreve forma, não resultado.

## 9. Decisão provisória

Registro por ID, sem ordenação de prioridade. Nenhuma classe equivale a adoção.

| ID | Classe | Motivo (uma linha) |
|---|---|---|
| AC-05-REP-001 | PILOTO | Único sem veto: LV4, RP=4, MIT lida; E13=2 e E15=1 barram CANDIDATO-FORTE |
| AC-05-REP-002 | PESQUISAR | Licença ausente (V4/B-02) e E06=ND; lacuna externa endereçável |
| AC-05-REP-003 | REJEITAR | Injeção de prompt confirmada por inspeção direta (E06=0, V1) |
| AC-05-REP-004 | PESQUISAR | Contradição 345×355 e tests/ ausente; contagem estoura teto — depende do proprietário |
| AC-05-REP-005 | PESQUISAR | V2: corpo de SKILL.md e AGENTS.md não lidos, skill declara Write/Edit; cabe no teto |
| AC-05-REP-006 | PESQUISAR | V7 (alegação 600+ sem fonte) + V2 (artefato escreve no FS); cabe no teto |
| AC-05-PRT-001 | REFERENCIA | LV3-V; definição de skill confirmada em `107`; 5 ND |
| AC-05-PRT-002 | REFERENCIA | LV3-V; anatomia de quatro pastas confirmada em `107` |
| AC-05-PRT-003 | REFERENCIA | LV3-V; quatro perguntas de planejamento confirmadas em `107` |
| AC-05-PRT-004 | PESQUISAR | Oficialidade da skill geradora atribuída a fornecedor, não verificada (E15=1) |
| AC-05-PRT-005 | REFERENCIA | LV3-V; único com teste de não ativação (E14=3); sem caso executado |
| AC-05-PRT-006 | REFERENCIA | LV3-V; três níveis conferidos; NC=2 — usa-se só a parte confirmada |
| AC-05-PRT-007 | REFERENCIA | LV3-V; NC=2 com três correções materiais — parte confirmada apenas |
| AC-05-PRT-008 | REFERENCIA | LV3-V; atalhos sem implementação — a ausência é o achado (E02=1) |
| AC-05-PRT-009 | REFERENCIA | LV3-V; ampliação de PRT-008, mesma limitação |
| AC-05-PRT-010 | PESQUISAR | Autoria e autenticidade do arquivo atribuído não verificadas |
| AC-05-PRT-011 | REFERENCIA | NC=0: síntese usa só as quatro seções da inspeção `107`; RP=1 |
| AC-05-PRT-012 | REFERENCIA | LV3-V; dez níveis nomeados conferidos; sem critério de passagem |
| AC-05-PRT-013 | PESQUISAR | V7: proporção 80/20 sem medição; fecharia com medição própria (proprietário) |
| AC-05-PRT-014 | REFERENCIA | Ponteiro redundante para REP-003; E01=1 impede rejeição; vinculado |
| AC-05-VID-001 | REFERENCIA | LV3-V; oito lentes em tela; rejeita "comando secreto" (fato visual) |
| AC-05-VID-002 | PESQUISAR | V7: "170 mil estrelas" contradiz o observado; licença do retratado ausente |
| AC-05-VID-003 | PESQUISAR | V7: alegações médicas/produtividade sem fonte nem método |
| AC-05-VID-004 | PESQUISAR | V7: a proposta é a alegação; sem conteúdo avaliável além do texto |
| AC-05-VID-005 | REFERENCIA | LV3-V; mapa de 20 conceitos conferido; "não documentação oficial" |
| AC-05-VID-006 | REFERENCIA | LV3-V; atalhos sem implementação; "embalagem como comando mágico" |
| AC-05-VID-007 | REFERENCIA | LV3-V; quatro capacidades mínimas; autocorreção afirmada, não medida |
| AC-05-VID-008 | REFERENCIA | Cluster; índice de descoberta; lacuna do cluster em VID-009 |
| AC-05-VID-009 | PESQUISAR | Identidade/licença/escopo das cinco skills — lacuna do cluster, contada uma vez |
| AC-05-VID-010 | REFERENCIA | Anúncio de produto de terceiro; verificação cabe ao fornecedor |
| AC-05-VID-011 | REFERENCIA | Taxonomia 42×7; equivalente com artefato é REP-004 |
| AC-05-VID-012 | REFERENCIA | Cluster; único que separa skill × plugin × MCP; lista sem rubrica |
| AC-05-VID-013 | REFERENCIA | Checklist de 18 configurações; disponibilidade não verificada |
| AC-05-VID-014 | REFERENCIA | Ciclo completo de aquisição; artefato equivalente mais forte em AC-03-REP-001 |
| AC-05-VID-015 | REFERENCIA | Três técnicas com valor decisório; "ghost" = risco de uso registrado |
| AC-05-VID-016 | REFERENCIA | Cluster; catálogo 8+8+8 sem nome novo; P-3 |
| AC-05-VID-017 | REFERENCIA | Cluster; auto-instalação já registrada em VID-009 |
| AC-05-VID-018 | PESQUISAR | Identidade do scanner (SkillInspector × SkillSpector × AC-09-REP-001) |
| AC-05-VID-019 | REFERENCIA | Cluster; quarta repetição da lista, valor marginal declarado |
| AC-05-VID-020 | PESQUISAR | V7 + contradição com README de REP-006; leitura cabe no teto |
| AC-05-VID-021 | PESQUISAR | V7: 54% sem fonte; identidade e licença da skill na origem |
| AC-05-VID-022 | REFERENCIA | Sete elementos com critério de saída; achado "persona não concede expertise" |
| AC-05-VID-023 | REFERENCIA | Taxonomia em camadas; NC=2 — decomposição do catálogo não confere |
| AC-05-VID-024 | REFERENCIA | Cluster; único STT integralmente vazio do acervo; cinco plugins nomeados |
| AC-05-VID-025 | REFERENCIA | Cluster; "oficial" e autoria atribuída exigem confirmação |
| AC-05-VID-026 | REFERENCIA | Oito blocos aplicados a quatro casos; NC=2 — enquadramento do catálogo não confere |
| AC-05-VID-027 | PESQUISAR | V7: "zero alucinações" falso ou não verificado; exige experimento (proprietário) |
| AC-05-VID-028 | REFERENCIA | Cluster; agrupado por função; risco de loop declarado, não confirmado |
| AC-05-VID-029 | REFERENCIA | 100+ prompts genéricos; "prompts genéricos não são Specs" |
| AC-05-VID-030 | REFERENCIA | Ranking sem rubrica; valor nos domínios sugeridos |
| AC-05-VID-031 | REFERENCIA | Cinco skills de design; NC=1 — descrição derivada do nome do arquivo |

**Distribuição: PILOTO 1 · PESQUISAR 15 · REFERENCIA 34 · REJEITAR 1 · CANDIDATO-FORTE 0 · ADAPTAR-PADRAO 0 · DUPLICATA 0 — total 51.**

## 10. Experimento que poderia validá-la

**Proposta — não é plano aprovado.** Quatro verificações, em ordem de custo crescente, cobririam as decisões mais carregadas da área:

1. **Leituras internas que cabem no teto (sem rede, sem execução):** ler por inteiro `SKILL.md` e `AGENTS.md` de `AC-05-REP-005`; `USER-GUIDE.md` e o corpo de `SKILL.md` de `AC-05-REP-006`; comparar os quadros de `AC-05-VID-018` com o README de `AC-09-REP-001`, já no acervo. Isso fecharia quatro das quinze fichas PESQUISAR e resolveria a contradição `AC-05-VID-020` × `AC-05-REP-006`.
2. **Pesquisa externa pontual:** ler a licença de `AC-05-REP-002` na origem pública (fecha B-02 e, de quebra, a lacuna de `AC-05-VID-002`); verificar identidade, licença e manifesto de permissões das skills nomeadas em `AC-05-VID-009` — **sem instalar nada**.
3. **Piloto controlado de `AC-05-REP-001` (depende do proprietário):** instalar em projeto descartável e registrar se os portões entre fases de fato bloqueiam avanço sem `/test`, e se os `evals/` executam a partir de um ponto de entrada identificável — validaria `E13 = 2` e a relevância que sustenta a classe PILOTO.
4. **Medição local de uma prática V7 (depende do proprietário):** escolher uma das seis práticas de `AC-05-PRT-013` ou o portão de perguntas de `AC-05-VID-021` e medir, sobre trabalho real desta casa, linhas geradas ou retrabalho com e sem a prática — transformaria uma alegação sem fonte em dado próprio, ou aposentaria o número.

## 11. Confiança da síntese

**Média.** Justificativa rastreável:

- **Cobertura de LV:** apenas 6 dos 51 itens (11,8%) têm leitura direta de artefato (LV4) — todos os repositórios. Os outros 45 dependem de quadros (LV3-V); três têm fala provável não revisada e 28 não têm fala aproveitável. O que os vídeos dizem além dos quadros é **desconhecido**.
- **Volume de ND:** 235 de 765 eixos (30,7%) em ND — padrão de 5 ND por ficha de print/vídeo (E03, E05, E06, E07, E13).
- **Itens degradados:** 8 com V7 (nenhum número entra como fato), 1 com NC=0 (`AC-05-PRT-011`, tratado só pela inspeção), 8 com NC=2 (usados só na parte confirmada), 9 fichas de cluster com redundância declarada (P-3 aplicado), 15 itens em PESQUISAR — a maior taxa de pendência entre as classes não-referência.
- **Pontos que sustentam a nota média e não baixa:** hashes 51/51 conferem; a pergunta central da área está coberta em todo o ciclo de vida; a única rejeição do acervo está nesta área e é sólida (inspeção direta, transcrição literal); as fichas individuais são internamente consistentes — a inconsistência encontrada está nos **totais do fechamento** (§4), não nas fichas, e foi registrada sem correção silenciosa.

## 12. Cobertura

| ID | Decisão provisória | ID | Decisão provisória |
|---|---|---|---|
| AC-05-REP-001 | PILOTO | AC-05-VID-009 | PESQUISAR |
| AC-05-REP-002 | PESQUISAR | AC-05-VID-010 | REFERENCIA |
| AC-05-REP-003 | REJEITAR | AC-05-VID-011 | REFERENCIA |
| AC-05-REP-004 | PESQUISAR | AC-05-VID-012 | REFERENCIA |
| AC-05-REP-005 | PESQUISAR | AC-05-VID-013 | REFERENCIA |
| AC-05-REP-006 | PESQUISAR | AC-05-VID-014 | REFERENCIA |
| AC-05-PRT-001 | REFERENCIA | AC-05-VID-015 | REFERENCIA |
| AC-05-PRT-002 | REFERENCIA | AC-05-VID-016 | REFERENCIA |
| AC-05-PRT-003 | REFERENCIA | AC-05-VID-017 | REFERENCIA |
| AC-05-PRT-004 | PESQUISAR | AC-05-VID-018 | PESQUISAR |
| AC-05-PRT-005 | REFERENCIA | AC-05-VID-019 | REFERENCIA |
| AC-05-PRT-006 | REFERENCIA | AC-05-VID-020 | PESQUISAR |
| AC-05-PRT-007 | REFERENCIA | AC-05-VID-021 | PESQUISAR |
| AC-05-PRT-008 | REFERENCIA | AC-05-VID-022 | REFERENCIA |
| AC-05-PRT-009 | REFERENCIA | AC-05-VID-023 | REFERENCIA |
| AC-05-PRT-010 | PESQUISAR | AC-05-VID-024 | REFERENCIA |
| AC-05-PRT-011 | REFERENCIA | AC-05-VID-025 | REFERENCIA |
| AC-05-PRT-012 | REFERENCIA | AC-05-VID-026 | REFERENCIA |
| AC-05-PRT-013 | PESQUISAR | AC-05-VID-027 | PESQUISAR |
| AC-05-PRT-014 | REFERENCIA | AC-05-VID-028 | REFERENCIA |
| AC-05-VID-001 | REFERENCIA | AC-05-VID-029 | REFERENCIA |
| AC-05-VID-002 | PESQUISAR | AC-05-VID-030 | REFERENCIA |
| AC-05-VID-003 | PESQUISAR | AC-05-VID-031 | REFERENCIA |
| AC-05-VID-004 | PESQUISAR | | |
| AC-05-VID-005 | REFERENCIA | | |
| AC-05-VID-006 | REFERENCIA | | |
| AC-05-VID-007 | REFERENCIA | | |
| AC-05-VID-008 | REFERENCIA | | |

**Contagem de controle:** 51 IDs listados · PILOTO 1 · PESQUISAR 15 · REFERENCIA 34 · REJEITAR 1. Diverge dos totais declarados no fechamento da Fase 2 (14 EXIGE PESQUISA / 35 REFERÊNCIA) por um item; a contagem ficha a ficha desta síntese prevalece e a anomalia está registrada em §4.

---

> Este arquivo é evidência externa, provisória e não normativa. Não autoriza adoção de nada.
