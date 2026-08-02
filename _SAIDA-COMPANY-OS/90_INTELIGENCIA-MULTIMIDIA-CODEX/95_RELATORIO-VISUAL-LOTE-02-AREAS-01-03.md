> EVIDÊNCIA EXTERNA  
> PROVISÓRIO  
> NÃO NORMATIVO  
> CANDIDATO À AVALIAÇÃO

# Relatório visual — Lote 02 — Áreas 01, 02 e 03

**Data:** 2026-07-29  
**Escopo:** 32 vídeos; 6 da área 01, 13 da área 02 e 13 da área 03  
**Cobertura:** 288 quadros examinados, nove por vídeo  
**Legibilidade:** LV3-V; áudio sem transcrição  
**Rastreabilidade:** IDs, nomes, duração e hashes permanecem no `92_MANIFESTO-TECNICO-DOS-VIDEOS.md`.

## Método e limites

Foram revisados nove quadros distribuídos entre 4% e 92% de cada vídeo. Texto incorporado, diagramas e interfaces são fatos visuais; falas, rankings, benchmarks, preços, popularidade e atribuições a fornecedores continuam alegações não verificadas. Nenhuma ferramenta foi instalada ou executada. AC-03-VID-008 é duplicata binária de AC-03-VID-007.

## Fichas — Área 01, modelos e ferramentas

- **AC-01-VID-001 — OmniRoute:** apresenta “OmniRoute — The Free AI Gateway”, instalação por `npm install -g omniroute`, provedores OAuth, chaves e painel de consumo. Alega agregar tiers gratuitos de 39 provedores/460+ modelos e cerca de 1,4 bilhão de tokens/mês. **Candidato:** gateway/roteador. **Riscos:** custódia de chaves, termos de serviço, disponibilidade, privacidade, supply chain e claims não verificados.
- **AC-01-VID-002 — planejador caro, executores baratos:** carrossel com orquestrador “Fable 5”, workers “Sonnet 5” e padrão inverso de executor barato com consultor sob demanda. Alega 54% de economia e 96% de desempenho. **Valor:** hipótese de roteamento por função; números e versões não verificados.
- **AC-01-VID-003 — rankings de ferramentas:** opinião visual: pesquisa de mercado (Gemini, Perplexity, ChatGPT), criação de sistemas (Claude Code, Cursor, Lovable), automação (Zapier, Make, Shortcuts) e imagens (Higgsfield, Gemini, Canva). **Valor:** lista de categorias; o ranking não tem rubrica nem teste reproduzível.
- **AC-01-VID-004 — Kimi K3:** divulga modelo aberto/gratuito e posição em arenas/benchmarks contra modelos “Fable/Sol”. **Candidato:** modelo para avaliação controlada; origem, licença, pesos, hardware, segurança e benchmarks precisam ser verificados.
- **AC-01-VID-005 — ferramentas audiovisuais:** classificação subjetiva por faixas (“excelente”, “bom”, “dá para usar”, “perda de tempo”), com ChatGPT, Higgsfield e ferramentas de transcrição/edição. Ícones não permitem identificar todos os produtos com segurança; fala pendente.
- **AC-01-VID-006 — ferramenta por tarefa:** rankings falados para brainstorming, pesquisa, programação, automação, imagens e criação de apps/sites. **Valor:** reforça seleção por caso de uso, não uma ferramenta universal. Identificação e justificativa completas dependem do áudio.

## Fichas — Área 02, arquitetura e estrutura

- **AC-02-VID-001 — anatomia de projeto Claude Code:** árvore com `CLAUDE.md`, `.mcp.json`, `.claude/settings*.json`, `rules/`, `context/`, `commands/`, `skills/`, `agents/` e `hooks/`. Separa instruções globais, conexões, permissões, convenções, conhecimento durável, playbooks, especialistas e guardrails. **Valor alto como taxonomia externa**, não como estrutura oficial.
- **AC-02-VID-002 — dez técnicas de escala de banco:** indexing, vertical scaling, caching, sharding, replication, query optimization, connection pooling, vertical partitioning, denormalization e materialized views. **Valor:** checklist arquitetural; escolha depende de carga, consistência e operação.
- **AC-02-VID-003 — estruturas de dados:** array, linked list, stack, hash map, matrix, queue, deque, binary tree, BST, heap, trie e graph. Conteúdo introdutório, sem recomendação direta para o OS.
- **AC-02-VID-004 — quinze design patterns:** Singleton, Factory Method, Builder, Adapter, Decorator, Facade, Proxy, Composite, Observer, Strategy, Command, Iterator, State, Template Method e Chain of Responsibility. **Valor:** vocabulário; evitar adoção por catálogo sem problema concreto.
- **AC-02-VID-005 — cinco fundamentos full-stack:** texto visual permite recuperar Value Objects, Aggregates, Use Cases e CQRS; o primeiro item não ficou legível. Parece uma lista de DDD/arquitetura, não “skills” operacionais. Áudio pendente.
- **AC-02-VID-006 — Claude Code, skills e OpenSpec:** demonstra projeto real, dashboard e código; associa economia de créditos a encapsular trabalho em skills e especificações. Fragmentos visuais não bastam para reconstruir o método.
- **AC-02-VID-007 — mapa do ecossistema de IA:** organiza ferramentas em LLM, Agentic AI, RAG, Embedding, MCP, AI Security, Observability, Memory, AI Agent, Automation e Vector Database. **Valor alto como mapa de categorias;** marcas são exemplos, não endosso.
- **AC-02-VID-008 — LB, reverse proxy e API gateway:** load balancer (distribuição, health check, failover, sticky sessions), reverse proxy (TLS, cache, compressão, URL rewriting) e gateway (autenticação, rate limit, agregação, roteamento). **Valor:** separação clara de responsabilidades.
- **AC-02-VID-009 e AC-02-VID-011 — “PAUL/Charlie OS”:** carrosséis relacionados propõem Graphify + Obsidian como “brain”, PAUL como framework construtor de dashboard OS, execução local ou em Railway e empacotamento em um repositório clonável. Comandos visíveis incluem init, plan, apply, verify, help/status. **Candidato em quarentena:** identidade, repositório, licença, código, credenciais e isolamento precisam ser descobertos antes de qualquer avaliação.
- **AC-02-VID-010 — agente = modelo + harness:** o harness possui **guias/feedforward** (`AGENTS.md`, specs/tasks, arquitetura, convenções), **memória/bootstrap** (`init.sh`, `progress.md`, disciplina Git) e **sensores/feedback** (linters, type checkers, testes/E2E, agente revisor). **Achado central:** desempenho do agente depende do sistema de trabalho, não só do modelo.
- **AC-02-VID-012 — instruções persistentes:** contrasta prompt avulso com `CLAUDE.md`; mostra regras de legibilidade, padrões, testes, documentação, proteção de segredos, exceções, segurança e qualidade. **Valor:** princípios candidatos; formulação integral depende do áudio e deve ser comparada aos Frameworks oficiais.
- **AC-02-VID-013 — anatomia do `CLAUDE.md`:** Project overview, Tech stack, Commands, Architecture, Code conventions, Testing, Git & PR rules, Do not touch, Gotchas e imports. Recomenda menos de 500 linhas, instruções em vez de prosa, especificidade e atualização quando estiver errado. **Valor alto como rubrica de concisão e manutenção.**

## Fichas — Área 03, agentes e orquestração

- **AC-03-VID-001 — Everything Claude Code:** divulga repositório com “181 skills, 47 subagentes e 78 comandos” e 50 mil estrelas. **Candidato:** `Everything Claude Code`; verificar se já está entre os 43 repositórios, licença, conteúdo, redundância e segurança. Quantidades/popularidade não verificadas.
- **AC-03-VID-002 — equipe de quatro agentes:** Planner lê o código, fecha a spec e marca dúvidas; Coder implementa estritamente o escopo; Tester cobre caminho feliz, bordas e falha e interrompe sem reparar; Reviewer é somente leitura e emite SHIP/NEEDS WORK/BLOCK. **Achado central:** separação de funções e independência da revisão.
- **AC-03-VID-003 — plugins e “tokens grátis”:** alega disputa Google/Anthropic, 37 ferramentas e instalação em massa de plugins como render/deploy/billing. **Risco alto:** marketing, instalação em massa, permissões e cadeia de suprimentos. Não usar como instrução.
- **AC-03-VID-004 — “Jarvis” por voz e MCPs:** comando de voz aciona Claude Code, RevenueCat MCP, dados de anúncios, emails e atendimento. **Valor:** interface multimodal e conexão operacional. **Risco crítico:** acesso amplo a produção, clientes, receita e email exige identidade, autorização granular, confirmação e auditoria.
- **AC-03-VID-005 — Claude chefe/Codex operário:** `routes.yaml` encaminha planner/executor/reviewer/tools; Codex lê/audita `src`, entrega `diff.patch`, Claude revisa. Alega 80% menos tokens. **Valor:** worker produz artefato revisável; economia não verificada.
- **AC-03-VID-006 — sabatina/revisão/veredito/build:** versão em português do padrão Grill–Review–Verdict–Build; sandbox somente leitura, uma linha de correção, máximo de cinco rodadas, depois inversão de papéis para implementação e revisão. Converge com AC-09-VID-005.
- **AC-03-VID-007 e AC-03-VID-008 — seis agentes de dados:** Cleaner, DAX, Layout, Insights, Data Auditor e Executive Delivery. Cada etapa tem função fixa; limpeza, cálculo, visual, insight, revisão e entrega. **Valor:** decomposição de uma linha de produção analítica. 008 é duplicata exata de 007.
- **AC-03-VID-009 — cinco formas de capturar capacidade:** (1) reescrever instruções persistentes, (2) usar modelo caro como consultor e produzir roadmap/stop list, (3) transformar deep research em notas atômicas ligadas, (4) executar `/goal` e workflows com prova/limite, (5) registrar problema, abordagem, tentativas rejeitadas e regra reutilizável. **Achado central:** transformar trabalho caro em ativo permanente reproduzível por modelo mais barato.
- **AC-03-VID-010 — cinco repositórios divulgados:** `google-labs-code/design.md`, `JCodesMore/ai-website-cloner-template`, `jamiepine/voicebox`, `penpot/penpot` e `ZhuLinsen/daily_stock_analysis`. **Candidatos:** direção visual, clonagem de página, voz, design colaborativo e analista de mercado. Verificar existência, licença, maturidade e segurança; não clonar/executar.
- **AC-03-VID-011 — contexto persistente e subagentes:** atribui à Anthropic o uso de `CLAUDE.md` contra alucinação e mostra subagentes paralelos gerando relatório para sessão seguinte. **Valor:** memória explícita e handoff; atribuição/causalidade não verificadas.
- **AC-03-VID-012 — loops com Hermes/SkillSmith:** goal com condição de saída, skill criada, Hermes local/VPS via SSH, CRON, auto-verificação e relatório ao Slack. Alerta contra loop infinito sem checker. **Valor:** padrão operacional; **risco alto:** execução 24/7, SSH, cron, credenciais e custos. Hermes/SkillSmith ficam candidatos, não autorizados.
- **AC-03-VID-013 — escada de capacidades:** Prompt → Contexto/`CLAUDE.md` → Ferramentas → MCP → Skills → Subagentes → Equipes de Agentes. A última camada é apresentada como experimental/manual. **Valor alto:** modelo de maturidade; não implica que todas as camadas sejam necessárias.

## Síntese provisória

### Área 01

O material favorece portfólio e roteamento: escolher ferramenta/modelo pelo trabalho, usar capacidade cara onde há julgamento e capacidade barata onde há especificação clara. Gateways e modelos abertos são candidatos econômicos, mas elevam risco de credenciais, licença, privacidade e volatilidade.

### Área 02

O achado mais forte é o **harness**: guias antecipam comportamento, memória sustenta retomada e sensores fecham o ciclo. A estrutura de projeto e do arquivo de instruções oferece uma taxonomia útil, mas deve ser comparada — item por item — com os Frameworks 1.11–1.19, nunca adotada em paralelo.

### Área 03

Há convergência em equipes com papéis separados, revisão independente, loops com saída, artefatos intermediários e codificação de aprendizado. A escada de capacidades sugere progressão: primeiro contexto e ferramentas, depois skills/subagentes, e equipes somente quando a coordenação justificar o custo.

## Candidatos novos para fila de avaliação

| Candidato | Motivo | Barreira obrigatória |
|---|---|---|
| OmniRoute | gateway/roteamento | segurança de chaves, licença, ToS, privacidade e benchmark |
| Kimi K3 | modelo aberto | identidade, pesos/licença, hardware, segurança e avaliação local |
| Everything Claude Code | catálogo amplo | redundância, licença, injeção, scripts e qualidade por componente |
| PAUL / Charlie OS / Graphify | OS/framework externo | identidade inequívoca, código, licença e sandbox |
| Hermes / SkillSmith | loops agendados | SSH/cron/segredos, limites, kill switch, idempotência e auditoria |
| design.md | direção visual | confirmar repositório e escopo |
| ai-website-cloner-template | prototipação | direitos autorais, segurança e proveniência |
| voicebox | voz | licença, privacidade e qualidade |
| Penpot | design colaborativo | encaixe, operação e integração |
| daily_stock_analysis | agente vertical | dados, risco financeiro, licença e manutenção |

## Encaminhamento ao Claude

1. Usar todas as fichas como LV3-V; manter ND no conteúdo que depende da fala.
2. Levar às sínteses apenas padrões, sempre com ID e camada de afirmação.
3. Registrar candidatos sem baixar, instalar, importar ou promover.
4. Comparar a taxonomia de harness/estrutura com os Frameworks oficiais, procurando lacunas e não substituição.
5. Dar prioridade de avaliação a: harness; papéis Planner/Coder/Tester/Reviewer; condição de saída; revisão somente leitura; registro reutilizável de decisões.

