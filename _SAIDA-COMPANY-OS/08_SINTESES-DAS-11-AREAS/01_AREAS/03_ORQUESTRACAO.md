> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

# SÍNTESE — ÁREA 03 — ORQUESTRAÇÃO DE AGENTES

**Frente:** Programa de Inteligência do Acervo · **Fase 3 — Síntese** (missão **A3**) · **Data:** 2026-07-29 · **Avaliador:** Claude Opus 5 (Fase 3)

**Origem:** external-evidence · **Autoridade:** nenhuma · **Estado:** provisório · **Normativo:** não · **Adoção:** não-decidida

**Entrada:** as 31 fichas de `_SAIDA-COMPANY-OS/07_FICHAS-DE-EVIDENCIA/03_ORQUESTRACAO-DE-AGENTES.md` (10 REPO · 8 PRINT · 13 VÍDEO), lidas integralmente, mais as pré-correções de `08_SINTESES-DAS-11-AREAS/00_PRE-CORRECOES-E-CORRESPONDENCIA.md`. Nenhuma fonte original foi aberta nesta fase; nenhuma nota foi alterada.

**Pergunta central da área:** como os agentes coordenam trabalho entre si — quem decide, quem executa, quem revisa.

---

## 1. O que sabemos

A área cobre cinco mecanismos de coordenação observados em artefato inspecionável (LV4) e mais um conjunto de formulações observadas apenas em quadros (LV3-V):

- **Separação explícita de quem decide, quem executa e quem revisa, com papel de revisão dedicado.** `AC-03-REP-004` nomeia 23 papéis como skills em Markdown (`plan-ceo-review`, `design-review`, `review`, `qa`, `cso`, `ship`, `retro`…), cada um com diretório próprio. `AC-03-REP-001` entrega revisão adversarial **por modelo de outro fornecedor** como artefato oficial, com contrato declarado de somente leitura ("This command is read-only and will not perform any changes"). A mesma separação aparece em quadros: quatro papéis e um veredito em `AC-03-VID-002`; sabatina → revisão → veredito → construção, com permissão de escrita por etapa e limite de iterações, em `AC-03-VID-006`; um papel dedicado à auditoria do resultado em `AC-03-VID-007`; seis funções não intercambiáveis em `AC-03-PRT-004`.
- **Portão obrigatório entre especificação e implementação.** `AC-03-REP-010` impede a escrita de código antes de spec extraída, apresentada em blocos legíveis e assinada pelo humano, com TDD vermelho/verde, YAGNI e DRY declarados, e só depois delega a subagentes.
- **Loop autônomo com memória externa e critério de parada, em vez de contexto vivo.** `AC-03-REP-008` implementa: `prd.json` como lista de tarefas com campo `passes`, `progress.txt` append-only, instância nova com contexto limpo a cada iteração e `max_iterations` (padrão 10) como controle de custo. A formulação do padrão — o loop, e não o prompt, como unidade de projeto, com ritmo, isolamento, memória, verificação e handoff — aparece em `AC-03-PRT-008`. `AC-03-VID-012` mostra em quadros loop agendado que age, verifica e reporta, com condição de saída explícita e alerta contra loop infinito sem verificador; a fala do vídeo permanece desconhecida (LV3-A sem fala lexical confiável).
- **Isolamento de execução paralela por worktree.** `AC-03-REP-007` declara "Fan one prompt across five agents, each in its own isolated git worktree — compare the results and merge the winner"; é o único item do acervo que trata isolamento por worktree como mecanismo central.
- **Infraestrutura de agente sempre ativa.** `AC-03-REP-005` entrega delegação a subagentes isolados, agendamento (`cron/`), handoff entre sessões e um loop de aprendizado declarado como produto central. `AC-03-REP-006` separa gateway como plano de controle do assistente ("The Gateway is just the control plane — the product is the assistant"), com camada de adaptadores para 23 canais de mensageria — coordenação de superfícies, pela borda da pergunta da área. `AC-03-REP-009` declara roteador, enxame, memória e loop de aprendizado (diagrama `User → Ruflo → Router → Swarm → Agents → Memory → LLM Providers`).
- **Distribuição do mesmo conjunto de instruções para múltiplos harnesses.** `AC-03-REP-002` publica o mesmo conteúdo para 18 diretórios de harness distintos, com `manifests/` e `schemas/`; `AC-03-REP-010` declara instalação independente em dez harnesses.
- **Handoff como unidade de coordenação.** `AC-03-VID-005` mostra em quadros quem planeja, quem executa e quem revisa, com `diff.patch` como artefato intermediário de handoff; `AC-03-VID-004` mostra handoff do agente principal para subagentes equipados com skills e conectores.
- **Deliberação distribuída como padrão documental.** A série `AC-03-PRT-001` a `AC-03-PRT-007` apresenta, em quadros: diagnóstico (blind spots, weak reasoning, no debate — `AC-03-PRT-002`), fan-out de uma pergunta para seis perspectivas (`AC-03-PRT-003`), protocolo objeção → contraponto → suposição → trade-off → síntese (`AC-03-PRT-005`) e trabalho em quatro rodadas com papéis distintos por rodada (`AC-03-PRT-006`).
- **Ordem de adoção de capacidades.** `AC-03-VID-013` propõe em quadros uma escada prompt → MCP → subagentes → automação e marca a camada de equipes como a última e menos madura; `AC-03-VID-009` trata de como o trabalho caro vira ativo reutilizável por um executor mais barato (`CLAUDE.md`, skills, `/goal`, workflows). `AC-03-VID-011` apresenta cinco mecanismos (arquivo de instruções, limpeza de contexto, subagentes, comando próprio e arquivo de memória) — o catálogo registrou apenas um, omissão nomeada na ficha (NC=2).

Medições de escala feitas pela Fase 2 e citáveis como fato de inspeção: `AC-03-REP-006` é o maior item do acervo (23.953 arquivos, 289,3 MB, E10=0); `AC-03-REP-007` (9.477 arquivos, 127,3 MB, E10=0); `AC-03-REP-005` (6.265 arquivos, 134 MB, E10=0); `AC-03-REP-009` (5.116 arquivos, 74,5 MB, E10=0); `AC-03-REP-002` (3.322 arquivos, 43,7 MB, E10=1); `AC-03-REP-004` (1.171 arquivos, 53,1 MB, E10=1); `AC-03-REP-003` (delta: 1.176 arquivos, 53 MB no total, E10=1); `AC-03-REP-001` (63 arquivos, 374,2 KB, E10=3); `AC-03-REP-008` (31 arquivos, 4,9 MB, E10=3); `AC-03-REP-010` (172 arquivos, 1,3 MB, E10=3).

## 2. Fontes mais fortes e por quê

Critério: dados da ficha (LV, NF, ND, vetos), nunca popularidade — a regra P-3 foi aplicada pela Fase 2 em todos os itens com badges (ex.: `AC-03-REP-002`, `AC-03-REP-007`).

- **`AC-03-REP-004` (`gstack-garrytan-main`)** — LV4, NF=4 com 7/7 eixos determinados e **0 ND**, nenhuma porta de veto disparada. É o único item da área com **evals de comportamento de agente** identificados na listagem de testes (`test/skill-llm-eval.test.ts`, `test/skill-routing-e2e.test.ts`, `test/codex-e2e.test.ts`, E13=4), e o único com E15=4: as alegações numéricas vêm com critério, universo medido e documento de metodologia com script de reprodução dentro da própria fonte — método declarado, não verificado, como a própria ficha registra.
- **`AC-03-REP-010` (`superpowers-main`)** — LV4, NF=4, 7/7, 0 ND, nenhum veto. E10=3 (172 arquivos, 1,3 MB): a menor superfície entre os candidatos fortes.
- **`AC-03-REP-005` (`hermes-agent-main`)** — LV4, NF=4, 7/7, 0 ND, nenhum veto; E11=4 (troca de modelo declarada por `hermes model`, mais de dez provedores). Ressalva registrada: E10=0 (6.265 arquivos, 134 MB).
- **`AC-03-REP-001` (`codex-plugin-cc-main`)** — LV4, NF=3, 6/7, **1 ND** (E05 manutenção — cópia estática sem histórico), nenhum veto. E10=3 e superfície pequena; `plugins/` não lido, lacuna declarada na ficha.

As demais fontes são mais fracas por dados objetivos: `AC-03-REP-002` tem E15=1 (badges não conferíveis) e E10=1; `AC-03-REP-007` tem E06=2 e E05=ND; `AC-03-REP-003` tem E06=2 e 3 ND sobre o delta; os 13 vídeos e 8 prints estão em LV3-V, com 5 ND estruturais por ficha (E03, E05, E06, E07, E13 não determináveis por inspeção visual).

## 3. Padrões recorrentes

- **Revisor separado de executor, idealmente de outro fornecedor ou com contexto limpo.** `AC-03-REP-001` (modelo de outro fornecedor), `AC-03-REP-004` (papéis `review`/`qa`/`cso`), `AC-03-VID-002`, `AC-03-VID-006` (permissão de escrita por etapa), `AC-03-VID-007` (papel de auditoria), `AC-03-PRT-005` (objeção e contraponto antes da síntese). A recorrência é de **formulação**, não de verificação: nenhum item mede o ganho dessa separação — `AC-03-PRT-007` promete quatro ganhos sem fonte (V7) e `AC-03-VID-005` declara economia não medida (V7).
- **Contexto limpo + memória externa em artefato versionável.** `AC-03-REP-008` (git + `progress.txt` + `prd.json`), `AC-03-VID-009` (`CLAUDE.md`, skills, workflows como ativos), `AC-03-VID-011` (arquivo de instruções e arquivo de memória entre os cinco mecanismos), `AC-03-VID-012` (memória entre sessões em loop agendado).
- **Loop com condição de parada e verificador, contra loop infinito.** `AC-03-REP-008` (`max_iterations`, portão de qualidade antes do commit), `AC-03-VID-012` (condição de saída explícita e alerta contra loop sem verificador), `AC-03-VID-006` (limite de cinco rodadas como parâmetro do protocolo), `AC-03-PRT-008` (verificação nomeada como componente do loop).
- **Fan-out com consolidação.** `AC-03-PRT-003` (uma pergunta, seis perspectivas), `AC-03-VID-011` (assistentes paralelos com consolidação em relatório único), `AC-03-REP-007` (cinco agentes em worktrees, merge do vencedor).
- **Multi-harness como estratégia de distribuição.** `AC-03-REP-002` (18 diretórios), `AC-03-REP-010` (dez harnesses), `AC-03-REP-004` (`model-overlays/`, testes `codex-e2e`/`gemini-e2e`), `AC-03-REP-008` (`--tool amp|claude`).
- **Número de marketing sem fonte conferível.** `AC-03-REP-002` (badges, E15=1), `AC-03-REP-007` (badges e slogan, E15=1), `AC-03-VID-003` (E15=0), `AC-03-VID-004` (E15=0), `AC-03-VID-005` (E15=0), `AC-03-PRT-001` e `AC-03-PRT-007` (E15=0). Nenhum desses números entra nesta síntese como fato.

## 4. Conflitos e divergências

- **`AC-03-VID-001` × `AC-03-REP-002`:** o vídeo divulga "181 skills, 47 sub-agentes, 78 comandos" e "50 mil estrelas"; o README do repositório no acervo diz "211.9K+ stars". Divergência observável dentro do próprio acervo, não reconciliada; a verificação (contar `skills/`, `agents/`, `commands/` em `AC-03-REP-002`) estoura o teto de leitura e depende de autorização do proprietário. Por P-3, a contagem de estrelas não move eixo algum.
- **Contradição interna de `AC-03-REP-009`:** o README declara "100+ specialized agents" e o `package.json` declara "60+ specialized agents"; a versão "3.25.6" do pacote diverge de "3.5.0" do changelog. Não reconciliado; verificável dentro da própria fonte, mas estoura o teto.
- **Catálogo × inspeção (NC=0):** `AC-03-REP-003` — o catálogo afirma "nenhum conteúdo original" e instrui a não analisar; a inspeção mede um delta real de 7 arquivos de empacotamento (`plugin.json`, `hooks/`, `.gitmodules`, workflow de upstream, `.gitlab-ci.yml`, README próprio de 967 bytes). Descrição e instrução do catálogo descartadas; esta síntese usa só o delta.
- **Catálogo × inspeção (NC=2), omissões que mudam o sentido:** `AC-03-VID-002` — o catálogo nomeia "Builder" onde o observado é "Coder" e acrescenta um "Orchestrator" que não aparece na descrição visual; `AC-03-PRT-008` — o catálogo inclui "navegador" entre os componentes do diagrama e a inspeção registra que não há componente de navegador visível; `AC-03-VID-011` — o vídeo apresenta cinco mecanismos e o catálogo registra apenas um; `AC-03-VID-003` — a descrição do catálogo só confere pela metade (a parte "agente com acesso a website, API, apps e dados" não corresponde ao observado).
- **`AC-03-VID-005` × `AC-03-REP-001`:** o vídeo propõe a separação planejador/executor como novidade com "80%" de economia declarada e não medida (V7); a própria ficha registra que `AC-03-REP-001` já entrega o mesmo acoplamento como artefato oficial, com licença Apache-2.0 lida.
- **Sobreposição de escopo entre repositórios:** `AC-03-REP-009` sobrepõe fortemente `AC-03-REP-002` e `AC-03-REP-010` (registrado em E14 da ficha); `AC-03-PRT-004` sobrepõe `AC-03-VID-002` na função de nomear papéis; `AC-03-PRT-006` converge com `AC-03-VID-006` e `AC-09-VID-005` no padrão de rodadas limitadas. Pela regra P-3, repetição não é confirmação.
- **Duplicata exata:** `AC-03-VID-008` é cópia de `AC-03-VID-007` (SHA-256 idêntico, reconferido); o conteúdo conta uma vez, em `AC-03-VID-007`.

## 5. Candidatos fortes, pilotos e referências

Registro por ID, sem ordenação por prioridade. Nenhuma classe equivale a adoção.

**CANDIDATO-FORTE (4):** `AC-03-REP-001` (revisão adversarial por modelo de outro fornecedor; LV4, NF3, 1 ND, sem veto) · `AC-03-REP-004` (23 papéis com rubricas; único com evals de comportamento, E13=4, E15=4) · `AC-03-REP-005` (loop de aprendizado e handoff; NF4, 0 ND — ressalva E10=0) · `AC-03-REP-010` (portão spec→código com TDD; NF4, 0 ND, menor superfície).

**PILOTO (2):** `AC-03-REP-002` (distribuição multi-harness; E15=1 e E10=1 barram candidato forte) · `AC-03-REP-008` (loop com memória externa; E03=2 e E13=1 — não há teste do próprio artefato).

**ADAPTAR-PADRAO (1):** `AC-03-REP-007` (o valor é o padrão worktree-por-agente; E06=2 fecha as classes de candidato, E05=ND).

**REFERENCIA (11):** `AC-03-PRT-002`, `AC-03-PRT-003`, `AC-03-PRT-004`, `AC-03-PRT-005`, `AC-03-PRT-006` (série deliberativa, insumo de consulta em quadros) · `AC-03-VID-002`, `AC-03-VID-006`, `AC-03-VID-007`, `AC-03-VID-009`, `AC-03-VID-011`, `AC-03-VID-013` (contratos de papéis, protocolos e escada de adoção, insumo de consulta em quadros).

**PESQUISAR (12):** `AC-03-REP-003`, `AC-03-REP-006`, `AC-03-REP-009`, `AC-03-PRT-001`, `AC-03-PRT-007`, `AC-03-PRT-008`, `AC-03-VID-001`, `AC-03-VID-003`, `AC-03-VID-004`, `AC-03-VID-005`, `AC-03-VID-010`, `AC-03-VID-012` — motivos na tabela da seção 9.

**DUPLICATA (1):** `AC-03-VID-008` → original `AC-03-VID-007`.

**REJEITAR (0):** nenhum item da área foi rejeitado — a rejeição se dá por evidência, nunca por ND, e nenhum risco foi confirmado por inspeção nesta área.

## 6. O que não adotar

Sem que nada disso constitua rejeição formal (nenhuma ficha tem RF = REJEITADO), a síntese registra o que **não entra como fato** nem como candidato:

- **Nenhum número dos cinco itens V7** (`AC-03-PRT-001`, `AC-03-PRT-007`, `AC-03-VID-003`, `AC-03-VID-004`, `AC-03-VID-005`): esses itens não têm conteúdo avaliável além do próprio texto nas partes que dependem de alegação sem fonte — os quatro ganhos de `AC-03-PRT-007`, a "economia de 80%" de `AC-03-VID-005`, os números de receita e de atendimento de `AC-03-VID-004`, as "37 ferramentas" e o "milhão de tokens" de `AC-03-VID-003`.
- **Instalação em massa de plugins como prática:** `AC-03-VID-003` manda instalar plugins em massa cuja identidade e escopo de permissão são desconhecidos; a ficha registra E01=1 (núcleo promocional) e nenhum risco confirmado — e também nenhum controle verificado.
- **Badges de popularidade** de `AC-03-REP-002` e `AC-03-REP-007` (E15=1, P-3): não sustentam decisão em nenhuma direção.
- **O delta de `AC-03-REP-003` como contribuição de orquestração:** a própria ficha mede E01=2 — o delta é distribuição/empacotamento, não coordenação entre agentes — e E14=1 (99,4% do conteúdo é `AC-03-REP-004`, já acessível).
- **`AC-03-VID-008` como segundo exemplar:** duplicata exata; contar seu conteúdo duas vezes inflaria a evidência.
- **A descrição de catálogo onde NC < 3:** `AC-03-REP-003` (NC=0), `AC-03-VID-001` (NC=1), `AC-03-VID-002`, `AC-03-VID-003`, `AC-03-VID-011`, `AC-03-PRT-008` (NC=2) — usa-se a inspeção, não o catálogo.

## 7. Riscos e dependências

**Riscos (declarados nas fichas; nenhum confirmado — nenhum item da área tem E06=1):**

- `AC-03-REP-003` (E06=2, sobre o delta): o `hooks/` declara que "SessionStart hook builds the browse binary and creates backward-compat symlinks" — compilação e criação de symlinks disparadas no início de sessão, sem `SECURITY.md` nem escopo de permissão declarado no wrapper. Superfície declarada, não inspecionada em código.
- `AC-03-REP-007` (E06=2): terminais com scrollback persistente, worktrees remotos por SSH com port forwarding e navegador Chromium embarcado; `SECURITY.md`, `.env.example` e política de permissão **procurados e não encontrados** na raiz efetiva.
- `AC-03-REP-004` (E06=3, com contrapeso registrado): a instalação recomendada é colar `git clone … && ./setup` para o próprio agente executar, e o modo de equipe **commita** `.claude/` e `CLAUDE.md` no repositório do usuário — superfície de cadeia de suprimentos declarada, não inspecionada.
- `AC-03-REP-008` (E06=3): loop autônomo que cria branch e commita sem intervenção; controles declarados (máximo de iterações, contexto limpo, portão de qualidade).
- `AC-03-REP-005` (E06=3): shell em seis backends, cron e mensageria em cinco plataformas, com pinagem exata de dependências justificada no manifesto; sem escopo de permissão explícito observado.
- Reversibilidade com perda: `AC-03-REP-009` (E12=2) — remover o diretório descarta `agentdb.rvf` e o histórico de aprendizado; `AC-03-REP-004` e `AC-03-REP-008` (E12=3) — reversão exige git porque escrevem no repositório do usuário.
- Fornecedor único por desenho: `AC-03-REP-001` (E11=2, existe para acoplar Claude Code a Codex/OpenAI) e `AC-03-REP-003` (E11=2, plugin de Claude Code).
- Custo de contexto: E10=0 em `AC-03-REP-005`, `AC-03-REP-006`, `AC-03-REP-007`, `AC-03-REP-009` (todas acima de 5.000 arquivos; `AC-03-REP-006` e `AC-03-REP-005` também acima de 100 MB).

**Dependências (classes de `00_PRE-CORRECOES` §2):**

- **Depende do proprietário para executar** (resolvível na própria fonte, mas estoura o teto de leitura): `AC-03-REP-009` (ler 4 arquivos internos e recontar agentes em `v3/`), `AC-03-VID-001` (contar `skills/`, `agents/`, `commands/` em `AC-03-REP-002`).
- **Depende do proprietário (experimento próprio):** `AC-03-PRT-007` — resposta única × deliberação por papéis, com rubrica desta casa.
- **Exige pesquisa externa:** `AC-03-REP-003` (titularidade ambígua da licença do upstream `ahacad/gstack`), `AC-03-REP-006` (superfície efetivamente distribuída via pacote npm publicado), `AC-03-PRT-001` (identidade da série do "conselho" — contada uma vez para as sete fichas), `AC-03-PRT-008` (identidade do repositório "Loop Engineering"), `AC-03-VID-003` (identidade e permissões dos plugins), `AC-03-VID-004` (escopo de autorização dos conectores), `AC-03-VID-005` (identidade e licença do "plugin de rotas"), `AC-03-VID-010` (cinco repositórios nomeados, nenhum no acervo), `AC-03-VID-012` (confirmar se o "Hermes" do vídeo é `AC-03-REP-005`; identidade de "SkillSmith").

## 8. Lacunas

- **Identidade da série do "conselho de IAs"** (`AC-03-PRT-001`): quem construiu, onde está o artefato, se é público — desconhecido; a verificação fecha a lacuna das sete fichas da série e é contada uma vez.
- **Titularidade e licença dos 7 arquivos do delta de `AC-03-REP-003`**: o `LICENSE` presente é o do upstream e nomeia outro titular — desconhecido se o wrapper declara titular próprio.
- **Superfície efetiva de `AC-03-REP-006`**: 23.953 arquivos e 289,3 MB sem manifesto que declare qual subconjunto precisa ser carregado — desconhecido se a superfície distribuída cai abaixo do limiar de 5.000 arquivos / 100 MB.
- **Manutenção (E05=ND)** de `AC-03-REP-001`, `AC-03-REP-007`, `AC-03-REP-008` e de todo o bloco LV3-V: cópias estáticas sem histórico — desconhecido.
- **Testes do próprio artefato em `AC-03-REP-008`** (E13=1): a raiz efetiva não contém diretório de teste; os testes citados no fluxo são do projeto-alvo.
- **Fala desconhecida em oito vídeos sem fala lexical confiável** (`AC-03-VID-002`, `AC-03-VID-006`, `AC-03-VID-007`, `AC-03-VID-008`, `AC-03-VID-009`, `AC-03-VID-010`, `AC-03-VID-012`, `AC-03-VID-013`): apenas quadros foram avaliados (LV3-V); o que a fala acrescenta permanece desconhecido e nenhuma "fala provável" é citada como fato nestes itens.
- **Nenhum eval de comportamento de agente fora de `AC-03-REP-004`**: todos os demais repositórios têm E13≤3 com testes de infraestrutura, não de comportamento — o ganho dos padrões de coordenação (separação de papéis, deliberação, loops) não tem medição em nenhuma fonte da área.
- **Nenhuma verificação pontual foi executada nesta fase** (`00_PRE-CORRECOES` §2.9): as 12 verificações em PESQUISAR permanecem por fazer.

## 9. Decisão provisória

Vocabulário fechado, mapeado do RF de cada ficha. Registro por ID, nunca por prioridade. **Nenhuma classificação equivale a adoção oficial.**

| ID | Classe | Motivo (uma linha, com base na ficha) |
|---|---|---|
| `AC-03-REP-001` | CANDIDATO-FORTE | RF = CANDIDATO FORTE: LV4, Bloco A ≥ 3, E06=3, E07=4, 1 ND ≤ 2, RP=4; lacuna remanescente E05=ND e `plugins/` não lido |
| `AC-03-REP-002` | PILOTO | RF = CANDIDATO A PILOTO: E15=1 (badges não conferíveis) barra CANDIDATO FORTE; E10=1 (3.322 arq., 43,7 MB) |
| `AC-03-REP-003` | PESQUISAR | RF = EXIGE PESQUISA (ficha de delta, NC=0): titularidade e licença dos 7 arquivos do delta — o LICENSE é do upstream e nomeia outro titular |
| `AC-03-REP-004` | CANDIDATO-FORTE | RF = CANDIDATO FORTE: LV4, Bloco A ≥ 4, 0 ND, E13=4 com evals de comportamento, E15=4 com método declarado |
| `AC-03-REP-005` | CANDIDATO-FORTE | RF = CANDIDATO FORTE: LV4, 0 ND, E11=4; ressalva registrada E10=0 (6.265 arq., 134 MB) |
| `AC-03-REP-006` | PESQUISAR | RF = EXIGE PESQUISA: RP=3 e E10=0; superfície de leitura/instalação não delimitável a partir do lido (23.953 arq., 289,3 MB) |
| `AC-03-REP-007` | ADAPTAR-PADRAO | RF = PADRÃO A ESTUDAR: o valor é o padrão worktree-por-agente (E04=3); E06=2 fecha as classes de candidato; E05=ND |
| `AC-03-REP-008` | PILOTO | RF = CANDIDATO A PILOTO: E03=2 e E13=1 (sem teste do próprio artefato) barram CANDIDATO FORTE; RP=4 |
| `AC-03-REP-009` | PESQUISAR | RF = EXIGE PESQUISA: contradição interna "100+"×"60+" agentes e versões divergentes; E15=2, E10=0; verificação estoura o teto e depende de autorização |
| `AC-03-REP-010` | CANDIDATO-FORTE | RF = CANDIDATO FORTE: LV4, 0 ND, portão spec→código com TDD; E10=3 (172 arq., 1,3 MB) |
| `AC-03-PRT-001` | PESQUISAR | RF = EXIGE PESQUISA via V7 (E15=0): identidade do "conselho" desconhecida; item sem conteúdo avaliável além do próprio texto na parte que sustenta a relevância |
| `AC-03-PRT-002` | REFERENCIA | RF = REFERÊNCIA: diagnóstico (blind spots, weak reasoning, no debate) como insumo de consulta LV3-V |
| `AC-03-PRT-003` | REFERENCIA | RF = REFERÊNCIA: padrão de fan-out para seis perspectivas, insumo de consulta LV3-V |
| `AC-03-PRT-004` | REFERENCIA | RF = REFERÊNCIA: decomposição em seis funções não intercambiáveis, insumo de consulta LV3-V |
| `AC-03-PRT-005` | REFERENCIA | RF = REFERÊNCIA: protocolo objeção→contraponto→suposição→trade-off→síntese, insumo de consulta LV3-V |
| `AC-03-PRT-006` | REFERENCIA | RF = REFERÊNCIA: estrutura de quatro rodadas com papéis por rodada, insumo de consulta LV3-V |
| `AC-03-PRT-007` | PESQUISAR | RF = EXIGE PESQUISA via V7 (E15=0): quatro ganhos sem medição nem fonte; fechamento depende de experimento do proprietário |
| `AC-03-PRT-008` | PESQUISAR | RF = EXIGE PESQUISA: identidade do repositório "Loop Engineering" desconhecida; NC=2 (catálogo inclui "navegador" não visível) |
| `AC-03-VID-001` | PESQUISAR | RF = EXIGE PESQUISA: contagens divulgadas divergem de `AC-03-REP-002`; verificação interna estoura o teto e depende de autorização |
| `AC-03-VID-002` | REFERENCIA | RF = REFERÊNCIA: contrato de quatro papéis + veredito em quadros; fala desconhecida; NC=2 (uso da parte confirmada) |
| `AC-03-VID-003` | PESQUISAR | RF = EXIGE PESQUISA via V7 (E15=0): identidade e escopo de permissão dos plugins instalados em massa desconhecidos; não é REJEITAR porque nenhum risco foi confirmado |
| `AC-03-VID-004` | PESQUISAR | RF = EXIGE PESQUISA via V7 (E15=0): escopo de autorização dos conectores e procedência dos números desconhecidos |
| `AC-03-VID-005` | PESQUISAR | RF = EXIGE PESQUISA via V7 (E15=0): "80%" de economia sem fonte; identidade do plugin desconhecida; `AC-03-REP-001` já entrega acoplamento similar |
| `AC-03-VID-006` | REFERENCIA | RF = REFERÊNCIA: protocolo sabatina→revisão→veredito→construção com cinco rodadas; lacuna do artefato nomeado registrada em `AC-09-VID-005`, não contada duas vezes |
| `AC-03-VID-007` | REFERENCIA | RF = REFERÊNCIA: pipeline com papel dedicado à auditoria do resultado; original da duplicata `AC-03-VID-008` |
| `AC-03-VID-008` | DUPLICATA | RF = DUPLICADO: SHA-256 idêntico a `AC-03-VID-007`, reconferido; conteúdo conta uma vez, no original |
| `AC-03-VID-009` | REFERENCIA | RF = REFERÊNCIA: trabalho caro convertido em ativo reutilizável (`CLAUDE.md`, skills, `/goal`, workflows); fala desconhecida |
| `AC-03-VID-010` | PESQUISAR | RF = EXIGE PESQUISA: cinco repositórios nomeados, nenhum no acervo; atenção a `ai-website-cloner-template` (direito autoral) e `daily_stock_analysis` (risco financeiro) |
| `AC-03-VID-011` | REFERENCIA | RF = REFERÊNCIA: cinco mecanismos de coordenação em quadros; NC=2 — o catálogo registrou só um, omissão nomeada |
| `AC-03-VID-012` | PESQUISAR | RF = EXIGE PESQUISA: identidade de "SkillSmith" desconhecida e pendente confirmar se o "Hermes" do vídeo é `AC-03-REP-005`; fala desconhecida |
| `AC-03-VID-013` | REFERENCIA | RF = REFERÊNCIA: escada de adoção prompt→MCP→subagentes→automação, com equipes como camada menos madura; fala desconhecida |

## 10. Experimento que poderia validá-la

**Proposta — não é plano aprovado.** Depende de ato do proprietário e não foi executada nesta fase.

1. **Resposta única × deliberação por papéis** (fecha a lacuna de `AC-03-PRT-007` e testa o padrão recorrente da seção 3): um mesmo conjunto de perguntas com resposta conhecida, respondido por um agente único e por uma decomposição em papéis como a de `AC-03-VID-002` ou `AC-03-PRT-005`, com rubrica definida por esta casa — medindo acerto, custo em tokens e número de rodadas. É exatamente a verificação escrita na ficha de `AC-03-PRT-007`.
2. **Medição do acoplamento planejador/executor** (fecha `AC-03-VID-005`): consumo de tokens com e sem separação planejador caro / executor barato, sobre tarefas definidas por esta casa — a alegação de "80%" permanece não verificada até medição própria.
3. **Verificações internas sob autorização de estouro de teto** (fecham `AC-03-REP-009` e `AC-03-VID-001`): ler `package.json`, changelog, `clone-data.proof.json` e `clone-data.ledger.json` de `AC-03-REP-009` e recontar agentes em `v3/`; contar `skills/`, `agents/`, `commands/` em `AC-03-REP-002`. Resolvem as duas contradições numéricas sem rede e sem execução.

## 11. Confiança da síntese

**Média.** Justificativa rastreável:

- **Cobertura de LV:** 10 dos 31 itens (todos os REPO) estão em LV4 com leitura de raiz, licença, README, manifesto e listagem de testes — base sólida para as decisões de CANDIDATO-FORTE, PILOTO e ADAPTAR-PADRAO. Os outros 21 itens estão em LV3-V (apenas quadros), 8 deles também com LV3-A; em 8 vídeos a fala é declaradamente não confiável e permanece desconhecida.
- **Volume de ND:** as 21 fichas LV3-V carregam 5 ND estruturais cada (E03, E05, E06, E07, E13 não determináveis por inspeção visual); entre os REPO, apenas 4 ND no total (`AC-03-REP-001`, `AC-03-REP-007`, `AC-03-REP-008` com 1 cada; `AC-03-REP-003` com 3 sobre o delta).
- **Itens degradados:** 5 itens V7 (`AC-03-PRT-001`, `AC-03-PRT-007`, `AC-03-VID-003`, `AC-03-VID-004`, `AC-03-VID-005`) sem conteúdo avaliável além do próprio texto nas partes decisivas; 1 item NC=0 (`AC-03-REP-003`); 5 itens NC≤2 com uso restrito à parte confirmada; 12 itens em PESQUISAR com verificação escrita mas **nenhuma executada** nesta fase.
- **O que sustenta "média" e não "baixa":** as quatro decisões de CANDIDATO-FORTE repousam todas em LV4 com 0–1 ND e nenhum veto disparado; as incertezas concentram-se no bloco documental (prints/vídeos), que a síntese trata apenas como REFERENCIA ou PESQUISAR — nunca como base de candidato.

## 12. Cobertura

| ID | Tipo | RF da ficha | Decisão provisória |
|---|---|---|---|
| `AC-03-REP-001` | REPO | CANDIDATO FORTE | CANDIDATO-FORTE |
| `AC-03-REP-002` | REPO | CANDIDATO A PILOTO | PILOTO |
| `AC-03-REP-003` | REPO (delta) | EXIGE PESQUISA | PESQUISAR |
| `AC-03-REP-004` | REPO | CANDIDATO FORTE | CANDIDATO-FORTE |
| `AC-03-REP-005` | REPO | CANDIDATO FORTE | CANDIDATO-FORTE |
| `AC-03-REP-006` | REPO | EXIGE PESQUISA | PESQUISAR |
| `AC-03-REP-007` | REPO | PADRÃO A ESTUDAR | ADAPTAR-PADRAO |
| `AC-03-REP-008` | REPO | CANDIDATO A PILOTO | PILOTO |
| `AC-03-REP-009` | REPO | EXIGE PESQUISA | PESQUISAR |
| `AC-03-REP-010` | REPO | CANDIDATO FORTE | CANDIDATO-FORTE |
| `AC-03-PRT-001` | PRINT | EXIGE PESQUISA | PESQUISAR |
| `AC-03-PRT-002` | PRINT | REFERÊNCIA | REFERENCIA |
| `AC-03-PRT-003` | PRINT | REFERÊNCIA | REFERENCIA |
| `AC-03-PRT-004` | PRINT | REFERÊNCIA | REFERENCIA |
| `AC-03-PRT-005` | PRINT | REFERÊNCIA | REFERENCIA |
| `AC-03-PRT-006` | PRINT | REFERÊNCIA | REFERENCIA |
| `AC-03-PRT-007` | PRINT | EXIGE PESQUISA | PESQUISAR |
| `AC-03-PRT-008` | PRINT | EXIGE PESQUISA | PESQUISAR |
| `AC-03-VID-001` | VÍDEO | EXIGE PESQUISA | PESQUISAR |
| `AC-03-VID-002` | VÍDEO | REFERÊNCIA | REFERENCIA |
| `AC-03-VID-003` | VÍDEO | EXIGE PESQUISA | PESQUISAR |
| `AC-03-VID-004` | VÍDEO | EXIGE PESQUISA | PESQUISAR |
| `AC-03-VID-005` | VÍDEO | EXIGE PESQUISA | PESQUISAR |
| `AC-03-VID-006` | VÍDEO | REFERÊNCIA | REFERENCIA |
| `AC-03-VID-007` | VÍDEO | REFERÊNCIA | REFERENCIA |
| `AC-03-VID-008` | VÍDEO | DUPLICADO | DUPLICATA → `AC-03-VID-007` |
| `AC-03-VID-009` | VÍDEO | REFERÊNCIA | REFERENCIA |
| `AC-03-VID-010` | VÍDEO | EXIGE PESQUISA | PESQUISAR |
| `AC-03-VID-011` | VÍDEO | REFERÊNCIA | REFERENCIA |
| `AC-03-VID-012` | VÍDEO | EXIGE PESQUISA | PESQUISAR |
| `AC-03-VID-013` | VÍDEO | REFERÊNCIA | REFERENCIA |

**Controle:** 31 IDs na área · 31 IDs na tabela · 30 itens únicos sintetizados + 1 cópia vinculada (`AC-03-VID-008`) · 1 ficha de delta sintetizada só no delta (`AC-03-REP-003`, artefato comum contado uma vez em `AC-03-REP-004`) · distribuição: CANDIDATO-FORTE 4 · PILOTO 2 · ADAPTAR-PADRAO 1 · REFERENCIA 11 · PESQUISAR 12 · REJEITAR 0 · DUPLICATA 1.

> Este arquivo é evidência externa, provisória e não normativa. Não autoriza adoção de nada.
