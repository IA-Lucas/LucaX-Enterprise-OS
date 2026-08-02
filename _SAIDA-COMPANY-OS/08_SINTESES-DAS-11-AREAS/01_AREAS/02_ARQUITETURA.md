> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

# SÍNTESE — ÁREA 02 — ARQUITETURA

**Frente:** Programa de Inteligência do Acervo · **Fase 3 — Síntese** (missão **A3**) · **Data:** 2026-07-29 · **Avaliador:** Claude Opus 5 (Fase 3)

**Origem:** external-evidence · **Autoridade:** nenhuma · **Estado:** provisório · **Normativo:** não · **Adoção:** não-decidida

**Pergunta central da área (base de E01):** *que forma o sistema tem — quais camadas, em que ordem de construção.*

---

## 1. O que sabemos

**Há consenso de conteúdo sobre a existência de camadas, com taxonomias convergentes mas não idênticas.** Um modelo propõe quatro camadas concêntricas — LLMs, AI Agents, Agentic Systems, Agentic Infra (governança, observabilidade, segurança) (AC-02-PRT-001). Outro propõe um grafo de dependências em cinco níveis, com a anotação de que times tendem a tentar começar pelo nível mais alto (AC-02-PRT-010 — uso restrito à parte confirmada pela inspeção; ver §4). Um terceiro enumera onze categorias de componente (LLM, Agentic AI, RAG, Embedding, MCP, AI Security, Observability, Memory, AI Agent, Automation, Vector Database) como mapa de camadas, com marcas declaradamente exemplos e não endosso (AC-02-VID-007).

**Há um checklist de composição do sistema com nove componentes** — LLM, memória, RAG, ferramentas, planejamento, reflexão, multi-agente, monitoramento/guardrails, humano no loop —, que obriga decisão dentro/fora por item (AC-02-PRT-002). Sobre **ordem de construção**, um roadmap de oito blocos coloca propósito, escopo e critério de sucesso antes de framework (AC-02-PRT-003), e um iceberg de oito degraus ordena MCP, subagentes, hooks, skills, headless e orquestração multi-repositório (AC-02-PRT-004).

**Há uma formulação recorrente do loop agêntico como camada de controle:** cinco nós — faz → se avalia → critica → reescreve → repete (AC-02-PRT-006) —, com critério de parada definido como aprovação em rubrica, não "primeira resposta aceitável" (AC-02-PRT-008). O slide de abertura da mesma série sustenta essa tese por alegação de autoridade sem fonte e não tem conteúdo avaliável além do próprio texto (AC-02-PRT-005 — ver §4 e §6).

**Há uma formulação explícita da separação modelo × sistema de trabalho:** o harness é decomposto em guias/feedforward (instruções, specs, arquitetura, convenções), memória/bootstrap e sensores/feedback (linters, type checkers, testes/E2E, agente revisor) (AC-02-VID-010).

**Há três itens sobre a camada de instruções persistentes do projeto:** uma taxonomia de pastas (`CLAUDE.md`, `.mcp.json`, `rules/`, `context/`, `commands/`, `skills/`, `agents/`, `hooks/`) (AC-02-VID-001); uma definição do que a base de conhecimento por projeto deve conter — legibilidade, padrões, testes, documentação, proteção de segredos, exceções, segurança, qualidade (AC-02-VID-012 — conforme a inspeção, não o catálogo; ver §4); e uma rubrica de forma para esse arquivo — dez blocos nomeados, menos de 500 linhas, instruções em vez de prosa, atualizar quando estiver errado (AC-02-VID-013).

**Há um único artefato executável na área:** um starter de orquestração com grafo de cinco estados (`triage → plan → execute → review → approval`), tabela de roteamento por `task_type`, Policy Engine declarado com portão de aprovação humana, `MOCK_MODE` sem chaves e 25 arquivos/19,3 KB — mas com `version = "0.1.0"`, um único arquivo de teste e **licença ausente na raiz efetiva** (AC-02-REP-001).

**Há conteúdo de decomposição de domínio** — modularização, objetos de valor, agregados, casos de uso e CQRS, apresentado como ranking declaradamente opinativo (AC-02-VID-005) — e **conteúdo de camadas de borda**, separando load balancer, reverse proxy e API gateway por responsabilidade (AC-02-VID-008). Há ainda listagens de vocabulário sem artefato: dez técnicas de escala de banco de dados (AC-02-VID-002), doze estruturas de dados (AC-02-VID-003) e quinze padrões de projeto (AC-02-VID-004).

**Há três itens cuja identidade de artefato é desconhecida:** um que propõe materializar padrões de projeto como skills com especificações encadeando passos, citando "OpenSpec" (AC-02-VID-006), e dois carrosséis relacionados que propõem "PAUL" como construtor de dashboard-OS sobre Graphify + Obsidian, com ciclo `init → plan → apply → verify` (AC-02-VID-009, AC-02-VID-011).

## 2. Fontes mais fortes e por quê

- **AC-02-REP-001** é a fonte mais forte da área e a única em **LV4**: artefato completo e inspecionável (E02 = 4), com procedimento de verificação declarado (três chamadas `curl` reproduzíveis e `tests/test_router.py` presente), NF = 3 com apenas 2 ND em 7 eixos, e superfície de segurança **documentada e notada** (E06 = 3 — controles parciais declarados, não inspecionados em código). Seu limite é estrutural, não de qualidade: E07 = ND (licença ausente) dispara V4 e o tira de qualquer classe de candidato.
- **AC-02-VID-010** e **AC-02-VID-005**: LV3-V + LV3-A (quadros mais fala provável), E14 = 3 — cada um é, dentro do acervo, a formulação mais explícita de sua tese (harness feedforward/feedback; decomposição DDD/CQRS). NF = 2 e 1, respectivamente, com 5 ND — fortes em relevância, fracas em verificabilidade.
- **AC-02-VID-013**: NF = 2, E14 = 3 — é o único item que dá critério de concisão e manutenção ao arquivo de instruções, e sua alegação numérica ("menos de 500 linhas") é conferível em qualquer arquivo real (E15 = 2).
- **AC-02-VID-001**: NF = 2, E14 = 3 — único mapeamento da estrutura de projeto inteira em um só quadro.
- Os prints com NC = 3 (AC-02-PRT-001, 002, 003, 004, 006, 007, 008, 009) têm descrição de catálogo confirmada contra os pixels, mas todos com NF = 2 ou menos e 5 ND — valem como taxonomia de consulta, não como evidência verificada.

## 3. Padrões recorrentes

- **Mapa de camadas como gênero dominante:** três itens independentes propõem taxonomias de camadas do sistema agêntico (AC-02-PRT-001, AC-02-PRT-010, AC-02-VID-007), e dois outros propõem ordens de construção (AC-02-PRT-003, AC-02-PRT-004). As taxonomias convergem na separação modelo → agente → sistema → infra/governança, mas nenhuma cita insumo ou método — todas são diagramas isolados (E02 = 2 nos cinco).
- **Camada de instruções persistentes como decisão arquitetural:** três vídeos independentes tratam do conhecimento persistente do projeto — estrutura de pastas (AC-02-VID-001), conteúdo da base de conhecimento (AC-02-VID-012) e rubrica de forma do arquivo (AC-02-VID-013).
- **Loop avaliador + critério de parada como camada de controle:** aparece no loop de cinco nós com parada por rubrica (AC-02-PRT-006, AC-02-PRT-008) e reaparece como malha de feedback no harness (AC-02-VID-010) e como estado `review → approval` no grafo executável (AC-02-REP-001).
- **Separação modelo × sistema de trabalho:** a tese de que desempenho depende do harness (AC-02-VID-010) e a tese de que o segredo está na pasta de conhecimento, não no prompt (AC-02-VID-012), são formulações da mesma separação.
- **Repetição dentro do acervo sem verificação mútua:** AC-02-VID-011 é reapresentação do material de AC-02-VID-009 (E14 = 1), e os dois convergem com itens da área 04 (registrado em AC-02-VID-009, E14 = 2). Repetição não é confirmação.
- **Listagens de vocabulário sem artefato:** três vídeos são só listagem nomeada (AC-02-VID-002, AC-02-VID-003, AC-02-VID-004), todos com NF = 1.

## 4. Conflitos e divergências

- **AC-02-VID-012 (NC = 0):** o catálogo descreve o item como "Claude Code cria aplicação full-stack e escolhe a pilha"; a inspeção (quadros + fala provável integral) mostra **camada de conhecimento persistente do projeto**, sem construção full-stack nem escolha de pilha. Esta síntese usa **somente a inspeção**. A divergência é sobre o catálogo e não rebaixa a fonte.
- **AC-02-PRT-010 (NC = 2):** o catálogo atribui ao bloco Reflection/Self-Critique a anotação "the loop that separates agents that compound from agents that repeat"; a inspeção mostra que a seta aponta para um ciclo de feedback/memória mais amplo. Usa-se a formulação corrigida ("ciclo de feedback/memória indicado pelo autor"); a omissão muda o sentido porque atrela a tese central do item a um bloco específico que o print não confirma.
- **AC-02-REP-001:** a alegação do catálogo "é o único item do acervo que já é um blueprint executável" está **contradita por fato observado** — outros repositórios do acervo também são projetos executáveis (a ficha nomeia AC-03-REP-005, AC-03-REP-006, AC-03-REP-007, AC-08-REP-002). A contradição é sobre o acervo, não sobre a fonte. Registra-se também que a instrução do catálogo "comece pelo ai-orchestrator-starter" foi classificada na ficha como decisão de escopo de terceiro, não obedecida.
- **AC-02-VID-013 (NC = 1, com imprecisão registrada):** o catálogo descreve "como verificar uma arquitetura"; o conteúdo observado é a anatomia e a rubrica de um arquivo de instruções, não um método de verificação de arquitetura.
- **AC-02-VID-005:** o catálogo afirmava "nada dele está capturado em texto" — alegação **superada** pela entrega multimídia (LV3-V + LV3-A). O tamanho registrado diverge (91 MB × 86,4 MB), consistente com conversão MiB→MB, não reaberto.
- **AC-02-PRT-005:** o slide sustenta que Anthropic e OpenAI "chegaram sozinhas à mesma ideia" — alegação de autoridade sem fonte identificada (E15 = 0, V7 disparada). O conteúdo avaliável do item se esgota no próprio texto; nenhuma inferência sobre os dois fornecedores entra nesta síntese como fato.
- **Sem divergência de escala, sem duplicatas, sem totais não reconciliados na área.**

## 5. Candidatos fortes, pilotos e referências

**Não há CANDIDATO-FORTE nem PILOTO na área.** Em 23 dos 24 itens, E06 = ND e E07 = ND disparam V2 e V4 (teto REFERÊNCIA / PADRÃO A ESTUDAR / EXIGE PESQUISA); no único item com E06 notado (AC-02-REP-001), E07 = ND dispara V4 isoladamente. Nenhum item recebeu PADRÃO A ESTUDAR na Fase 2, portanto não há ADAPTAR-PADRAO.

- **REFERENCIA (19):** AC-02-PRT-001, AC-02-PRT-002, AC-02-PRT-003, AC-02-PRT-004, AC-02-PRT-006, AC-02-PRT-007, AC-02-PRT-008, AC-02-PRT-009, AC-02-PRT-010, AC-02-VID-001, AC-02-VID-002, AC-02-VID-003, AC-02-VID-004, AC-02-VID-005, AC-02-VID-007, AC-02-VID-008, AC-02-VID-010, AC-02-VID-012, AC-02-VID-013.
- **PESQUISAR (5):** AC-02-REP-001 (licença e titularidade — bloqueio B-02), AC-02-PRT-005 (fonte primária da atribuição a Anthropic/OpenAI), AC-02-VID-006 (identidade, licença e conteúdo do "OpenSpec"; ganho de crédito não medido), AC-02-VID-009 e AC-02-VID-011 (identidade, repositório, licença e permissões de "PAUL"/"Graphify" — mesma lacuna, contada uma vez).

Nenhuma dessas classes equivale a adoção. O registro é por ID, sem ordenação.

## 6. O que não adotar

- **AC-02-PRT-005 como evidência de consenso entre fornecedores:** a tese do item depende integralmente de uma atribuição sem fonte (E15 = 0, V7). O item **não tem conteúdo avaliável além do próprio texto** — não se extrai dele nenhum fato sobre Anthropic ou OpenAI.
- **AC-02-VID-011 como item separado:** é reapresentação do material de AC-02-VID-009 (E14 = 1, conveniência); seu conteúdo conta uma vez, no item mais completo (AC-02-VID-009, que também está pendente de identidade).
- **AC-02-VID-003 como insumo de arquitetura:** E01 = 1 — é fundamento de programação, não decisão de camada ou ordem; tangencia a área (não cabe REJEITAR porque E01 ≠ 0, mas seu peso na síntese é nulo).
- **Nenhuma taxonomia de camadas como estrutura oficial:** todas são agregações de material público sem método declarado (E02 = 2, E14 = 2) — consulta, não fonte de verdade (registrado na própria trilha: "valor alto como taxonomia externa, não como estrutura oficial", AC-02-VID-001).
- **Nenhuma alegação de ganho não medido:** a economia de créditos atribuída a encapsular trabalho em skills/specs (AC-02-VID-006, E15 = 1) e as alegações de capacidade de "PAUL"/"Graphify" (AC-02-VID-009, AC-02-VID-011, E15 = 1) não entram como fato.

## 7. Riscos e dependências

- **Licença desconhecida no único artefato executável:** AC-02-REP-001 não tem arquivo de licença na raiz efetiva (bloqueio B-02); pela regra da casa, ausência é indeterminação de procedência, não permissão negada — e é exatamente o que impede classe de candidato. Dependências de ambiente declaradas: Docker, PostgreSQL, Redis, n8n, LiteLLM (E08 = 4, não chega a 5).
- **Superfícies de segurança declaradas e não inspecionadas (ND, não risco confirmado):** execução local ou em Railway, empacotamento em repositório clonável e comando `apply` (AC-02-VID-009); agente com acesso a um vault pessoal e execução em serviço externo (AC-02-VID-011); skills e especificações reais exibidas mas não inspecionadas (AC-02-VID-006); conteúdo real de `hooks/` e settings nomeado como guardrail sem regra exibida (AC-02-VID-001); Policy Engine declarado em README com `app/` não lido (AC-02-REP-001, E06 = 3 mede a superfície documentada, não o código).
- **Dependência de produtos não identificados:** a transferibilidade de AC-02-VID-006, AC-02-VID-009 e AC-02-VID-011 é parcial (E04 = 2) porque a implementação depende de artefatos cuja identidade é a própria lacuna.
- **Nenhum item da área tem risco declarado (E06 = 1) nem risco confirmado (E06 = 0).** Toda indeterminação acima é ND, escrita como ND.

## 8. Lacunas

- **Licença e titularidade de AC-02-REP-001** — ausentes na raiz efetiva; fechável lendo a origem pública do repositório (pesquisa externa).
- **Identidade de "OpenSpec"** (AC-02-VID-006) e de **"PAUL" / "Charlie OS" / "Graphify"** (AC-02-VID-009, AC-02-VID-011) — repositório, licença, credenciais e permissões; mesma lacuna nos dois últimos, contada uma vez.
- **Fonte primária da atribuição a Anthropic e OpenAI** em AC-02-PRT-005 — sem ela, o item permanece sem conteúdo avaliável.
- **Testes/evals ausentes em toda a área:** E13 = ND em 23 de 24 itens; a exceção é AC-02-REP-001, com um único arquivo de teste para um fluxo de cinco estados e nenhum eval de comportamento de agente (E13 = 2).
- **Autoria, licença e data de todos os prints e vídeos:** E07 = ND e E05 = ND em todos os 23 itens de mídia.
- **Fala não revisada:** os vídeos com LV3-A usam transcrição automática bruta sem revisão humana; a fala permanece "provável", e em oito vídeos o STT não produziu fala lexical confiável (AC-02-VID-001, 002, 003, 004, 007, 008, 009, 011, 013 — nesses, só os quadros sustentam a ficha).

## 9. Decisão provisória

| ID | Classe | Motivo (uma linha, citando a ficha) |
|---|---|---|
| AC-02-REP-001 | PESQUISAR | LV4 e NF = 3, mas E07 = ND (licença ausente na raiz efetiva) dispara V4 — bloqueio B-02, nunca candidato sem a licença (ficha, Portas de veto) |
| AC-02-PRT-001 | REFERENCIA | Mapa de quatro camadas confirmado contra os pixels (NC = 3), LV3-V com V2/V4 (ficha, Resultado) |
| AC-02-PRT-002 | REFERENCIA | Checklist de nove componentes confirmado (NC = 3), LV3-V com V2/V4 (ficha, Resultado) |
| AC-02-PRT-003 | REFERENCIA | Roadmap de oito blocos confirmado (NC = 3), LV3-V com V2/V4 (ficha, Resultado) |
| AC-02-PRT-004 | REFERENCIA | Iceberg de oito degraus confirmado (NC = 3), LV3-V com V2/V4 (ficha, Resultado) |
| AC-02-PRT-005 | PESQUISAR | Tese depende de atribuição sem fonte (E15 = 0, V7) — teto EXIGE PESQUISA (ficha, Portas de veto) |
| AC-02-PRT-006 | REFERENCIA | Loop de cinco nós confirmado (NC = 3), LV3-V com V2/V4 (ficha, Resultado) |
| AC-02-PRT-007 | REFERENCIA | Slide de contraste confirmado (NC = 3), LV3-V com V2/V4 (ficha, Resultado) |
| AC-02-PRT-008 | REFERENCIA | Três passos com parada por rubrica confirmados (NC = 3), LV3-V com V2/V4 (ficha, Resultado) |
| AC-02-PRT-009 | REFERENCIA | Comparação RAG/Agents/Agentic RAG confirmada (NC = 3), LV3-V com V2/V4 (ficha, Resultado) |
| AC-02-PRT-010 | REFERENCIA | Grafo de cinco níveis, NC = 2 — usa-se a parte confirmada pela inspeção (correção material de `105`) (ficha, Catálogo) |
| AC-02-VID-001 | REFERENCIA | Taxonomia de pastas do projeto, NF = 2, E14 = 3, LV3-V com V2/V4 (ficha, Resultado) |
| AC-02-VID-002 | REFERENCIA | Listagem de dez técnicas de escala de BD, NF = 1, LV3-V com V2/V4 (ficha, Resultado) |
| AC-02-VID-003 | REFERENCIA | Listagem introdutória, E01 = 1 tangencia a área — não cabe REJEITAR (ficha, Resultado) |
| AC-02-VID-004 | REFERENCIA | Listagem de quinze padrões, NF = 1, LV3-V com V2/V4 (ficha, Resultado) |
| AC-02-VID-005 | REFERENCIA | Ranking de cinco padrões arquiteturais, E14 = 3, LV3-V+LV3-A com V2/V4 (ficha, Resultado) |
| AC-02-VID-006 | PESQUISAR | Relevância aparente (E01 = 3) com identidade/licença do "OpenSpec" e ganho de crédito por medir (ficha, lacuna nomeada) |
| AC-02-VID-007 | REFERENCIA | Mapa de onze categorias confirmado (NC = 5), LV3-V com V2/V4 (ficha, Resultado) |
| AC-02-VID-008 | REFERENCIA | Separação LB/proxy/gateway confirmada (NC = 5), LV3-V com V2/V4 (ficha, Resultado) |
| AC-02-VID-009 | PESQUISAR | "Candidato em quarentena": identidade, repositório, licença e permissões de PAUL/Graphify desconhecidos (ficha, lacuna nomeada) |
| AC-02-VID-010 | REFERENCIA | Harness feedforward/feedback, E14 = 3, LV3-V+LV3-A com V2/V4 (ficha, Resultado) |
| AC-02-VID-011 | PESQUISAR | Mesma lacuna de AC-02-VID-009, contada uma vez; E14 = 1 (reapresentação) (ficha, lacuna nomeada) |
| AC-02-VID-012 | REFERENCIA | NC = 0 — usa-se só a inspeção (camada de conhecimento persistente); a divergência é do catálogo, não da fonte (ficha, Resultado) |
| AC-02-VID-013 | REFERENCIA | Rubrica de dez blocos com critério de concisão, E14 = 3, LV3-V com V2/V4 (ficha, Resultado) |

## 10. Experimento que poderia validá-la

**Proposta, não plano aprovado.** A decisão provisória dominante (19 REFERENCIA, 0 candidatos) decorre de V2/V4 por ND de segurança e licença, não de fraqueza de conteúdo. O experimento mais informativo seria sobre **AC-02-REP-001**, o único artefato executável: (1) localizar a origem pública e ler a licença — fecha a lacuna B-02 que sozinha o mantém fora de candidato; (2) ler `app/` para conferir se o Policy Engine implementa o portão de aprovação que o README declara; (3) executar o "Teste rápido" de três `curl` em `MOCK_MODE=true` e medir se o grafo de cinco estados se comporta como a ficha descreve. Um segundo experimento, de natureza DEPENDE DO PROPRIETÁRIO, mediria localmente o consumo de créditos com e sem encapsulamento de trabalho em skills/specs, com tarefas definidas por esta casa — é a verificação escrita na própria ficha de AC-02-VID-006. Nenhum dos dois foi executado nesta fase.

## 11. Confiança da síntese

**Média.** Justificativa rastreável:

- **Cobertura de LV alta:** 24/24 itens em LV ≥ 3, com 1 em LV4 (AC-02-REP-001) e 4 vídeos com LV3-V + LV3-A. Nenhum item ilegível.
- **Volume de ND alto:** 117 de 360 eixos em ND (32,5 %), concentrados em E03, E05, E06, E07 e E13 — maturidade, manutenção, segurança, licença e testes de todos os itens de mídia são desconhecidos.
- **5 itens em EXIGE PESQUISA (20,8 % da área)**, todos com verificação escrita mas nenhuma executada nesta fase — incluindo o item mais forte (AC-02-REP-001) e o cluster de maior apelo promocional (AC-02-VID-009, AC-02-VID-011).
- **1 item V7** (AC-02-PRT-005), cujo conteúdo avaliável se esgota no próprio texto; **1 item NC = 0** (AC-02-VID-012), resolvido pela inspeção; **1 item NC = 2** (AC-02-PRT-010), usado só na parte confirmada.
- **0 REJEITAR, 0 DUPLICATA, 0 divergência de escala.** Nenhuma nota foi somada ou mediada; onde não há evidência, a síntese escreveu "desconhecido".

A confiança não é alta porque as duas decisões mais consequentes da área — o que fazer com o único blueprint executável e com o cluster PAUL/Graphify — estão ambas pendentes de pesquisa externa não realizada.

## 12. Cobertura

| ID | Tipo | LV | RF (Fase 2) | Decisão provisória |
|---|---|---|---|---|
| AC-02-REP-001 | REPO | LV4 | EXIGE PESQUISA | PESQUISAR |
| AC-02-PRT-001 | PRINT | LV3-V | REFERÊNCIA | REFERENCIA |
| AC-02-PRT-002 | PRINT | LV3-V | REFERÊNCIA | REFERENCIA |
| AC-02-PRT-003 | PRINT | LV3-V | REFERÊNCIA | REFERENCIA |
| AC-02-PRT-004 | PRINT | LV3-V | REFERÊNCIA | REFERENCIA |
| AC-02-PRT-005 | PRINT | LV3-V | EXIGE PESQUISA | PESQUISAR |
| AC-02-PRT-006 | PRINT | LV3-V | REFERÊNCIA | REFERENCIA |
| AC-02-PRT-007 | PRINT | LV3-V | REFERÊNCIA | REFERENCIA |
| AC-02-PRT-008 | PRINT | LV3-V | REFERÊNCIA | REFERENCIA |
| AC-02-PRT-009 | PRINT | LV3-V | REFERÊNCIA | REFERENCIA |
| AC-02-PRT-010 | PRINT | LV3-V | REFERÊNCIA | REFERENCIA |
| AC-02-VID-001 | VÍDEO | LV3-V | REFERÊNCIA | REFERENCIA |
| AC-02-VID-002 | VÍDEO | LV3-V | REFERÊNCIA | REFERENCIA |
| AC-02-VID-003 | VÍDEO | LV3-V | REFERÊNCIA | REFERENCIA |
| AC-02-VID-004 | VÍDEO | LV3-V | REFERÊNCIA | REFERENCIA |
| AC-02-VID-005 | VÍDEO | LV3-V + LV3-A | REFERÊNCIA | REFERENCIA |
| AC-02-VID-006 | VÍDEO | LV3-V + LV3-A | EXIGE PESQUISA | PESQUISAR |
| AC-02-VID-007 | VÍDEO | LV3-V | REFERÊNCIA | REFERENCIA |
| AC-02-VID-008 | VÍDEO | LV3-V | REFERÊNCIA | REFERENCIA |
| AC-02-VID-009 | VÍDEO | LV3-V | EXIGE PESQUISA | PESQUISAR |
| AC-02-VID-010 | VÍDEO | LV3-V + LV3-A | REFERÊNCIA | REFERENCIA |
| AC-02-VID-011 | VÍDEO | LV3-V | EXIGE PESQUISA | PESQUISAR |
| AC-02-VID-012 | VÍDEO | LV3-V + LV3-A | REFERÊNCIA | REFERENCIA |
| AC-02-VID-013 | VÍDEO | LV3-V | REFERÊNCIA | REFERENCIA |

**Contagem:** 24/24 IDs representados · REFERENCIA 19 · PESQUISAR 5 · CANDIDATO-FORTE 0 · PILOTO 0 · ADAPTAR-PADRAO 0 · REJEITAR 0 · DUPLICATA 0.

> Este arquivo é evidência externa, provisória e não normativa. Não autoriza adoção de nada.
