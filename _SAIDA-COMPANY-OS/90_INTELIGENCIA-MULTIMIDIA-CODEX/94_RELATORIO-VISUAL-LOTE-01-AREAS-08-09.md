> EVIDÊNCIA EXTERNA  
> PROVISÓRIO  
> NÃO NORMATIVO  
> CANDIDATO À AVALIAÇÃO

# Relatório visual — Lote 01 — Áreas 08 e 09

**Handoff:** H-M2-001  
**Data:** 2026-07-29  
**Escopo:** 15 vídeos; 8 da área 08 e 7 da área 09  
**Cobertura:** 135 quadros examinados, nove por vídeo  
**Nível de legibilidade:** LV3-V (quadros-chave revisados); áudio ainda sem transcrição  
**Regra:** o acervo informa o LucaX Enterprise OS, mas não determina sua arquitetura.

## 1. Método e limites

Foram extraídos nove quadros distribuídos entre 4% e 92% da duração de cada vídeo. A inspeção cobriu texto incorporado ao vídeo, diagramas, interfaces e sequência visual. Nenhuma fala foi reconstruída como transcrição. Fragmentos de legenda são tratados como **texto visual capturado**, e não como registro integral do áudio.

As afirmações de autores, benchmarks, preços, percentuais, versões de modelos, popularidade e segurança permanecem **alegações não verificadas**. Nomes de ferramentas e repositórios são somente pistas para avaliação posterior; nada foi baixado, instalado ou executado.

## 2. Cobertura e rastreabilidade

| ID | Arquivo | Duração | Hash SHA-256 (prefixo) | Estado deste lote |
|---|---|---:|---|---|
| AC-08-VID-001 | `Caching layers.mp4` | 15,0 s | `95C7C2C3E9D2DD3D` | LV3-V |
| AC-08-VID-002 | `Gravando 2026-07-28 153711.mp4` | 50,5 s | `4779F1249C5D9516` | LV3-V; fala pendente |
| AC-08-VID-003 | `Gravando 2026-07-28 155545.mp4` | 53,6 s | `6AEFF65BE08979CA` | LV3-V; fala pendente |
| AC-08-VID-004 | `Gravando 2026-07-28 163216.mp4` | 16,5 s | `66B279D261DBF011` | LV3-V |
| AC-08-VID-005 | `Gravando 2026-07-28 163244.mp4` | 16,5 s | `66B279D261DBF011` | duplicata exata de 004 |
| AC-08-VID-006 | `Gravando 2026-07-28 214120.mp4` | 9,2 s | `4E9239D2BB085477` | LV3-V |
| AC-08-VID-007 | `Gravando 2026-07-29 090249.mp4` | 12,3 s | `CB50B41864BC2725` | LV3-V |
| AC-08-VID-008 | `handoff.mp4` | 43,8 s | `2789E1E271CDE926` | LV3-V; fala pendente |
| AC-09-VID-001 | `erros e correcóes.mp4` | 43,2 s | `2EE427F03CFBF5C1` | LV3-V; fala pendente |
| AC-09-VID-002 | `Gravando 2026-07-28 164102.mp4` | 31,7 s | `DADD32FE83806418` | LV3-V; fala pendente |
| AC-09-VID-003 | `Gravando 2026-07-28 203100.mp4` | 16,3 s | `A22DC01AF3A61516` | LV3-V |
| AC-09-VID-004 | `Gravando 2026-07-28 203833.mp4` | 16,7 s | `87DDC4FDF6612A91` | LV3-V |
| AC-09-VID-005 | `Gravando 2026-07-28 204533.mp4` | 16,4 s | `CEFCACDEF936F55C` | LV3-V |
| AC-09-VID-006 | `Gravando 2026-07-29 090207.mp4` | 8,4 s | `FFA2AA3762397410` | LV3-V |
| AC-09-VID-007 | `Gravando 2026-07-29 091447.mp4` | 38,5 s | `879770140F9DF65B` | LV3-V; fala pendente |

## 3. Fichas de evidência — Área 08, Custo e Contexto

### AC-08-VID-001 — camadas de cache

- **Descrição visual:** infográfico com o percurso Browser → CDN → Redis → Database e a instrução “check the closest copy first, hit the DB last”.
- **Ideia extraível:** consultar primeiro a cópia mais próxima e tratar o banco como último recurso; separar leituras frias, quentes, acertos de cache e acessos ao banco.
- **Alegação do material:** em um cenário ilustrativo de 1.000 leituras de API, apenas três chegariam ao banco.
- **Uso candidato:** princípio de infraestrutura e de observabilidade de cache; exigir política de invalidação, consistência, segurança e métricas antes de adoção.
- **Limite:** o número “3 de 1.000” não foi demonstrado nem reproduzido.

### AC-08-VID-002 — custo da duplicação de contexto entre subagentes

- **Descrição visual:** apresentador sobre diagrama em que Skills, Tools, MCPs, Prompt, arquivos de contexto e `AGENTS.md` aparecem replicados em ramificações de subagentes; o diagrama mostra uma janela aproximada de 200k.
- **Texto visual capturado:** fragmentos como “entender subagents”, “lentos”, “caro”, “principal, separando”, “o contexto” e “então o segredo”.
- **Ideia extraível:** o desenho do contexto de cada subagente deve ser explícito; replicar indiscriminadamente todas as definições pode aumentar custo e latência.
- **Uso candidato:** orçamento de contexto por agente, pacote mínimo de capacidades e medição de bytes/tokens transferidos por delegação.
- **Limite:** sem transcrição, não é possível reconstruir a recomendação completa nem confirmar as relações causais.

### AC-08-VID-003 — modelo caro para planejar, barato para executar

- **Descrição visual:** demonstração no Claude Code com modo de planejamento e troca de modelo.
- **Texto visual capturado:** “como economizar tokens lá dentro do Claude Code”, “vai colocar no modo planejar”, “o Opus ou Fable”, “você só precisa validar”, “sem ficar pensando e gastando tokens”, “o modelo mais barato pra trabalhar”.
- **Ideia extraível:** separar arquitetura/planejamento/validação de execução mecânica e rotear cada etapa para um modelo proporcional ao risco.
- **Uso candidato:** matriz de roteamento por complexidade, risco, reversibilidade e necessidade de julgamento.
- **Limite:** nomes, versões, qualidade e economia não foram verificados; a fala integral está pendente.

### AC-08-VID-004 e AC-08-VID-005 — sete níveis de redução de custo

AC-08-VID-005 é duplicata binária exata de AC-08-VID-004.

- **Nível 1 — Meter:** auditar a conversa e apontar os três maiores desperdícios de tokens.
- **Nível 2 — Budget:** impor formato e orçamento de resposta, sem preâmbulo ou resumo e com limite de palavras.
- **Nível 3 — Route:** classificar tarefas simples/complexas e encaminhar as simples a modelo menor.
- **Nível 4 — Compact:** criar handoff curto antes de saturar a janela; o material também menciona `/compact`.
- **Nível 5 — Prune:** reduzir `CLAUDE.md` a conteúdo que realmente altera comportamento e desligar MCPs ociosos.
- **Nível 6 — Delegate:** subagente lê o conjunto de arquivos e devolve somente achados necessários.
- **Nível 7 — Batch:** agrupar tarefas e aproveitar processamento em lote e cache.
- **Alegações do material:** 75–85% de redução em roteamento, 40–50% da janela como momento para compactar, 6.100 tokens de entrada para 420 de saída em delegação, batch em API a -50% e cache a -90%.
- **Uso candidato:** taxonomia de controles de custo e telemetria, nunca como meta oficial sem benchmark local.

### AC-08-VID-006 — pxpipe e contexto renderizado como imagem

- **Descrição visual:** carrossel que apresenta `pxpipe` como proxy local que converteria partes volumosas do contexto em PNG antes do envio.
- **Alegações do material:** custo de imagem baseado em pixels; código/JSON/saída de ferramentas teria cerca de 3,1 caracteres por token de imagem contra aproximadamente um por token textual; economia total de 59–70%.
- **Risco crítico:** texto transformado em imagem pode reduzir fidelidade, acessibilidade, capacidade de busca, auditabilidade e proteção contra injeção. O artefato não demonstra preservação semântica nem segurança.
- **Uso candidato:** somente como hipótese experimental isolada, com corpus de teste, comparação de exatidão e medição de custo. Não instalar ou colocar em produção por evidência social.

### AC-08-VID-007 — cinco táticas associadas a “Fable 5”

- **Descrição visual:** carrossel datado de julho de 2026 sobre limites de plano/API e cinco táticas de custo.
- **Táticas visíveis:** reduzir esforço; usar o modelo mais caro como arquiteto e outro como executor; reduzir verbosidade; usar modelos baratos/subagentes para pesquisa; chamar o modelo caro apenas como consultor quando o executor travar.
- **Alegações do material:** economia de até 80%, “22% mais barato sem perda de qualidade”, 109 subagentes e comparações de preço/qualidade entre versões.
- **Uso candidato:** reforça a hipótese de roteamento por função e escalonamento sob exceção.
- **Limite:** versões, preços, disponibilidade, nomenclatura e benchmarks são voláteis e não foram verificados.

### AC-08-VID-008 — handoff em vez de depender de compactação

- **Descrição visual:** gráfico “Output quality vs context filled” com marcações de rotação em 65% e auto-compactação em 80%; em seguida, criação de `handoff.md`, uso de `/clear` e retomada por nova sessão.
- **Campos visíveis do handoff:** Goal, Current State, Changed, Failed attempts e Next steps.
- **Ideia extraível:** tornar a continuidade explícita e auditável em artefato versionável; iniciar nova sessão com objetivo, estado, alterações, tentativas falhas e próximos passos.
- **Alegação do material:** a qualidade cai com o preenchimento da janela e `/compact` seria inferior ao handoff limpo.
- **Uso candidato:** protocolo de retomada e prevenção de perda de estado; comparar empiricamente com compactação antes de normatizar.

## 4. Fichas de evidência — Área 09, Segurança e Qualidade

### AC-09-VID-001 — limpar contexto após ciclos repetidos de erro

- **Descrição visual:** apresentador com legendas e demonstração do comando `/clear`.
- **Texto visual capturado:** referência a um “documento da Anthropic”; fragmentos “no mesmo problema”, “na terceira tentativa”, “em cima de dois fracassos”, “limpa o contexto inteiro”, “sessão limpa com prompt melhor” e “tudo seja melhorado”.
- **Ideia extraível:** depois de várias tentativas fracassadas, preservar diagnóstico e reiniciar em contexto limpo pode evitar que correções ruins se acumulem.
- **Uso candidato:** limite de tentativas, registro de hipóteses/erros e reinício controlado com prompt melhorado.
- **Limite:** a fonte atribuída à Anthropic e a causalidade sobre alucinação não foram verificadas; fala integral pendente.

### AC-09-VID-002 — AIOps correlacionando sinais com aprovação humana

- **Descrição visual:** terminal Kubernetes e painel de um “AIOps Agent”. O exemplo correlaciona alerta `OOMKilled`, logs, métricas e eventos para um `payment-svc`.
- **Evidências visíveis:** `connection refused redis:6379`, `timeout: cache-svc`, três reinícios em dez minutos e p99 de 184 ms.
- **Hipótese exibida:** falha de conexão com Redis causando timeout e reinícios em cascata; a confiança visual evolui de 33% para 92%.
- **Plano exibido:** reiniciar o pod, escalar réplicas de 3 para 5 e notificar o time SRE; estado final “aguardando aprovação”.
- **Ideia extraível:** separar coleta, correlação, hipótese, confiança, evidências e plano; manter ação de produção sob aprovação e trilha de auditoria.
- **Risco:** a demonstração não prova correção da causa raiz nem segurança das ações sugeridas. Automação de produção exige autorização, reversão, limites e verificação pós-ação.

### AC-09-VID-003 — loops de autoavaliação e `plan-optimizer`

- **Descrição visual:** carrossel “Prompts are dead. Build loops instead”. O loop mostrado é Do → Grade → Critique → Rewrite → Repeat.
- **Ferramenta citada:** `plan-optimizer`, atribuída a `seangeng.com`, com instalação mostrada por download encadeado a execução em shell.
- **Ideia extraível:** transformar uma saída única em ciclo limitado por checklist, crítica e critério de aprovação.
- **Riscos:** alegação de que OpenAI e Anthropic “concordam” não foi verificada; “1,49M pessoas viram” é apenas prova social; comando remoto encadeado a shell não deve ser executado sem inspeção, licença, hash e sandbox.
- **Uso candidato:** avaliar o padrão do loop, não adotar automaticamente a implementação divulgada.

### AC-09-VID-004 — primeiro loop de revisão somente leitura

- **Descrição visual:** tutorial para criar `codex-review-loop/` com `input/` e `reviews/`, adicionar `first-review.md` e pedir revisão.
- **Prompt visual:** seguir `AGENTS.md`; revisar todos os arquivos em `input/`; não editar `input/`; escrever um relatório em `reviews/review-001.md`; ser claro, específico e útil.
- **Fluxo mostrado:** usuário deposita arquivo → Codex revisa → grava feedback → usuário lê e decide.
- **Ideia extraível:** iniciar automação por um loop somente leitura, com separação entre fonte e saída, antes de permitir correções automáticas.
- **Limite:** o vídeo chama a checagem de “diária”, mas não demonstra agendamento, controle de duplicidade ou falhas.

### AC-09-VID-005 — `chaseai-yt/grill-me-codex`

- **Descrição visual:** carrossel que apresenta quatro skills: `grill-me-codex`, `grill-with-docs-codex`, `codex-review` e `codex-build`.
- **Fluxo proposto:** Grill → Review → Verdict → Build. Claude entrevista até fechar decisões em `PLAN.md`; Codex revisa o plano em sandbox somente leitura; a resposta termina em `VERDICT: APPROVED` ou `VERDICT: REVISE`; revisões são limitadas a cinco rodadas; depois Codex escreve e Claude verifica.
- **Itens procurados na revisão:** falhas de segurança, condições de corrida, casos de borda ausentes e premissas erradas.
- **Candidato identificado:** repositório `chaseai-yt/grill-me-codex`.
- **Uso candidato:** avaliação documental e de segurança do repositório; comparar o protocolo com os Frameworks 1.11–1.19. Não instalar.

### AC-09-VID-006 — quatro perguntas de auditoria

- **Ajustar o sistema:** “Analise como eu uso IA hoje — meus prompts, meus fluxos, minhas ferramentas — e me diga o que, se eu melhorar, vai melhorar todo o resto.”
- **Auditoria de vida/conteúdo:** olhar o que já foi criado/publicado, encontrar tema e apontar o que ficará obsoleto ou pode multiplicar resultado.
- **Auditoria de segurança:** revisar prompts contra prompt injection, listar o que está em produção e pedir varredura contínua de vulnerabilidades.
- **Pergunta difícil:** usar a janela de maior capacidade para o problema que bloqueia há mais tempo, com contexto completo.
- **Valor candidato:** perguntas de diagnóstico e priorização.
- **Risco:** pedir a uma IA que “audite segurança” não substitui escopo, ferramentas, autorização, testes, revisão humana ou controles contínuos.

### AC-09-VID-007 — busca de skills por catálogo

- **Descrição visual:** demonstração de `/find-skills adaptar aplicativo web para app mobile`, consulta a `vercel-labs/skills` e páginas de `skills.sh`.
- **Candidatos exibidos:** `alinaqi/claude-bootstrap@pwa-development` e `ruvnet/ruflo@agent-spec-mobile-react-native`.
- **Sinal de cautela visível:** a própria resposta informa que as opções não são de fonte oficial e não devem ser tratadas como totalmente confiáveis.
- **Alegação do material:** o mecanismo filtraria opções ruins e permitiria vasculhar “700.000 skills por IA”.
- **Uso candidato:** descoberta, nunca confiança automática. A seleção deve exigir origem, licença, manutenção, permissões, conteúdo integral do `SKILL.md`, scripts, dependências e testes em isolamento.
- **Limite:** tamanho do catálogo, confiabilidade do hub e qualidade dos candidatos não foram verificados.

## 5. Síntese provisória para as duas áreas

### Área 08

O lote converge em cinco hipóteses: medir antes de otimizar; limitar e podar contexto; rotear tarefas por complexidade/risco; delegar com retorno compacto; e manter handoff explícito entre sessões. Há ainda duas hipóteses de infraestrutura — cache em camadas e compressão visual de contexto — que exigem validação técnica muito diferente. A primeira é um padrão estabelecido em termos gerais; a segunda apresenta riscos de fidelidade e segurança e deve permanecer em quarentena experimental.

### Área 09

O lote converge em loops controlados: revisão somente leitura antes de escrita, ciclos limitados de crítica, separação entre evidência e hipótese, confiança explícita, aprovação humana antes de ação e reinício limpo após tentativas falhas. O material também revela um risco recorrente: instalar skills ou executar scripts sugeridos por conteúdo social. Descoberta e adoção precisam ser fases distintas.

## 6. Candidatos encaminhados, sem adoção

| Candidato | Tipo | Motivo para avaliar | Bloqueios antes de qualquer uso |
|---|---|---|---|
| `chaseai-yt/grill-me-codex` | repositório/skills | protocolo Grill–Review–Verdict–Build | origem, licença, código integral, permissões, compatibilidade e sandbox |
| `plan-optimizer` / `seangeng.com` | skill/script remoto | loop de checklist e autoavaliação | não executar comando remoto; identificar repositório, licença, hash e conteúdo |
| `vercel-labs/skills` | catálogo/repositório | descoberta de skills | confirmar escopo, governança e diferença entre oficial e comunitário |
| `skills.sh` e `/find-skills` | catálogo/mecanismo | busca assistida de capacidades | proveniência, ranking, injeção, supply chain e política de instalação |
| `alinaqi/claude-bootstrap@pwa-development` | skill comunitária | PWA como alternativa a reescrita mobile | auditoria completa; fonte não oficial |
| `ruvnet/ruflo@agent-spec-mobile-react-native` | skill comunitária | especificação React Native | auditoria completa; fonte não oficial |
| `pxpipe` | proxy/hipótese | possível economia de contexto | identidade, código, licença, segurança, fidelidade e benchmark local |

## 7. Encaminhamento ao Claude

1. Usar as fichas como LV3-V, jamais como transcrição.
2. Manter ND nos eixos que dependem da fala integral.
3. Incluir os padrões nas sínteses das áreas 08 e 09 como hipóteses, com a origem por ID.
4. Registrar os sete candidatos na fila de avaliação, sem promover nenhum a Spec, Skill, Agente, Command, Workflow ou decisão.
5. Aplicar penalidade de evidência a claims de custo, benchmark, segurança, popularidade e autoridade não confirmados.
6. Tratar instalação por `curl | shell` e skills comunitárias como risco de supply chain.

## 8. Lacunas remanescentes

- Transcrição do áudio dos sete vídeos com apresentador/fala relevante.
- Verificação das fontes atribuídas a Anthropic/OpenAI.
- Identificação inequívoca, licença e integridade de `pxpipe` e `plan-optimizer`.
- Verificação atualizada dos repositórios/catálogos citados.
- Benchmark local de roteamento, handoff, cache, delegação e compressão.

