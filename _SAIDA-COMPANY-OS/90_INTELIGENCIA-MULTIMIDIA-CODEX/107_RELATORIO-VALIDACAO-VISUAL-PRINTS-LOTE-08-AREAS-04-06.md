> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

# Relatório de validação visual de prints — Lote 08 — Áreas 04 a 06

**Data:** 2026-07-29  
**Escopo:** 40 prints — áreas 04, 05 e 06  
**Resultado:** 34 descrições confirmadas, 5 parciais, 1 divergente  
**Legibilidade:** LV3-V — original visual inspecionado; origem e alegações não verificadas  
**Fontes modificadas:** 0

## Método e limites

Cada imagem original foi aberta e comparada diretamente com a descrição correspondente em `_CONTEUDO.md`.

- **CONFIRMADA:** o conteúdo essencial visível está descrito com fidelidade;
- **PARCIAL:** o núcleo confere, mas há omissão, normalização ou inferência material;
- **DIVERGENTE:** uma parte estrutural da descrição não aparece ou contradiz a imagem.

O estado mede fidelidade do catálogo, não verdade externa. “Oficial”, “open source”, “melhor”, “gratuito”, “produção”, compatibilidade, preço, licença, benchmark, versão e capacidade continuam alegações não verificadas, mesmo quando o print exibe essas palavras. Nenhum código, link, conector, repositório ou comando foi executado.

## Resultado agregado

| Área | Prints | Confirmadas | Parciais | Divergentes |
|---|---:|---:|---:|---:|
| 04 — Memória e conhecimento | 13 | 12 | 1 | 0 |
| 05 — Skills e prompts | 14 | 11 | 2 | 1 |
| 06 — Conectores e MCP | 13 | 11 | 2 | 0 |
| **Total** | **40** | **34** | **5** | **1** |

## Matriz de validação

### Área 04 — Memória e conhecimento

| ID | Conteúdo visível | Estado | Observação/correção |
|---|---|---|---|
| AC-04-PRT-001 | Master Obsidian | CONFIRMADA | As 13 áreas, o fluxo Capture→Organize→Connect→Visualize→Reflect, recursos, templates, PARA/Zettelkasten e recomendação de começar simples conferem. |
| AC-04-PRT-002 | LangChain e stack RAG | CONFIRMADA | Instalação e sete componentes conferem como texto exibido. |
| AC-04-PRT-003 | Document Loading | CONFIRMADA | PyPDFLoader, TextLoader, WebBaseLoader, CSVLoader e WikipediaLoader conferem. |
| AC-04-PRT-004 | tuning, problemas e produção | CONFIRMADA | Chunk 300, overlap 50–100, k 3–10, temperatura 0, diagnóstico, cache, monitoramento, fallback e proteção de segredos conferem. |
| AC-04-PRT-005 | Summary do pipeline | CONFIRMADA | Sete caixas e quatro lembretes conferem. |
| AC-04-PRT-006 | Preprocessing manual | CONFIRMADA | A afirmação de que LangChain não fornece pré-processamento embutido e o exemplo com regex conferem como conteúdo do slide. |
| AC-04-PRT-007 | Text Chunking | CONFIRMADA | RecursiveCharacterTextSplitter, 300/50, faixa 200–1000, overlap e separadores conferem. “300 is optimal” é alegação do slide, não padrão validado. |
| AC-04-PRT-008 | Embeddings | PARCIAL | Modelos e comparações conferem; o catálogo acrescenta que `text-embedding-ada-002` é “pago”, informação que **não aparece** no print. Manter esse atributo como alegação externa separada. |
| AC-04-PRT-009 | Vector Database | CONFIRMADA | FAISS, milhões de vetores, open source/GPU e alternativas Pinecone, Chroma e Qdrant conferem como alegações exibidas. |
| AC-04-PRT-010 | Retrieval | CONFIRMADA | Similarity, k=5, faixa 3–10, MMR e score threshold conferem. |
| AC-04-PRT-011 | Generation — conceito | CONFIRMADA | Stuff, map_reduce e refine conferem. |
| AC-04-PRT-012 | Generation — implementação | CONFIRMADA | ChatGroq, temperatura 0, `gemma2-9b-it`, RetrievalQA e `stuff` conferem. O código não foi testado. |
| AC-04-PRT-013 | Evaluation | CONFIRMADA | Faithfulness, relevance, retrieval quality, QAEvalChain, BLEU/ROUGE/BERTScore, avaliação humana e contínua conferem. |

### Área 05 — Skills e prompts

| ID | Conteúdo visível | Estado | Observação/correção |
|---|---|---|---|
| AC-05-PRT-001 | o que é uma skill | CONFIRMADA | Pasta de instruções, reutilização e fluxo entrada→processo→ação→resultado conferem. |
| AC-05-PRT-002 | anatomia de uma skill | CONFIRMADA | `SKILL.md`, scripts, references, assets e recomendação de começar mínimo conferem. |
| AC-05-PRT-003 | planejamento antes de escrever | CONFIRMADA | Problema, pedido, etapas e diferencial conferem. |
| AC-05-PRT-004 | Skill Creator | CONFIRMADA | O print apresenta uma skill “skill-creator”, atribuída a Anthropic, e pede tarefa, processo atual e regras. Oficialidade/versão não foram verificadas. |
| AC-05-PRT-005 | teste de skill | CONFIRMADA | Ativação correta, não ativação indevida, consistência, etapas e melhoria da skill conferem. |
| AC-05-PRT-006 | Bad, Better e Best Prompt | PARCIAL | Bad e Better conferem. No Best, o print manda ler três arquivos, não executar ainda e fazer perguntas para refinar a abordagem; “ângulo, tom e público” aparece explicitamente no **Better**, não no Best. O catálogo funde os dois níveis. |
| AC-05-PRT-007 | setup único do Claude Cowork | PARCIAL | Setup e Build conferem em essência. Corrigir “nunca reler outputs/templates” para **“never auto-read OUTPUTS/TEMPLATES”**. O print não manda editar o prompt original; diz “call out the mistake, don’t accept it”. Também mostra Wispr Flow e nova sessão a cada 20 mensagens, omitidos no catálogo. |
| AC-05-PRT-008 | Claude Commands Secret Codes | CONFIRMADA | Os 14 atalhos e seus propósitos conferem. Continuam convenções promocionais, não comandos nativos confirmados. |
| AC-05-PRT-009 | All Claude Commands | CONFIRMADA | A tabela ampla por propósito confere. Natividade e implementação não foram verificadas. |
| AC-05-PRT-010 | CLAUDE.md atribuído a Boris Cherny | CONFIRMADA | Os seis blocos, task management e princípios conferem. Autoria e autenticidade continuam não verificadas. |
| AC-05-PRT-011 | Dicionário do Claude para empresários | DIVERGENTE | O print tem **quatro seções visíveis**: Conceitos de IA, Produtos, Recursos Principais e Agentes e Automação. Não há bloco “Conta/API”, nem plan, limites, créditos, API key ou console. A descrição em seis blocos mistura/reorganiza itens e acrescenta conteúdo ausente. |
| AC-05-PRT-012 | dez níveis do Claude Code | CONFIRMADA | Terminal, Memória, Comandos, Customização, Skills, MCP, Subagentes, Hooks, Headless e Rotinas conferem. |
| AC-05-PRT-013 | 80/20 do uso do Claude | CONFIRMADA | Os seis itens centrais e seis hábitos da zona cinza conferem. A proporção 80/20 não é demonstrada. |
| AC-05-PRT-014 | link para CLAUDE-FABLE-5.md | CONFIRMADA | O print contém apenas o link catalogado. |

### Área 06 — Conectores e MCP

| ID | Conteúdo visível | Estado | Observação/correção |
|---|---|---|---|
| AC-06-PRT-001 | 30 IAs para empresários | CONFIRMADA | Dez capacidades com três candidatos cada conferem; o print escreve “NanoBanana 2”. |
| AC-06-PRT-002 | ferramentas do dia a dia | CONFIRMADA | As seis cadeias e ferramentas conferem. |
| AC-06-PRT-003 | Claude Code Resource Bible | CONFIRMADA | As categorias e links encurtados conferem; a captura não valida os destinos. |
| AC-06-PRT-004 | oito Claude Connectors | CONFIRMADA | Granola, Gmail, Slack, Canva, Drive, Notion, Calendar e Gamma, com os casos de uso, conferem. |
| AC-06-PRT-005 | 11 formas de acelerar empresa | CONFIRMADA | As onze combinações e promessas conferem como texto visível. |
| AC-06-PRT-006 | VibeVoice | CONFIRMADA | README, badges TTS/ASR, aba MIT, gráfico subjetivo e legenda promocional conferem. Não prova substituição, gratuidade ou licença efetiva do artefato. |
| AC-06-PRT-007 | cinco universais | CONFIRMADA | GitHub, Context7, Playwright, Filesystem e Brave Search conferem. “Install first” é recomendação do slide, não autorização. |
| AC-06-PRT-008 | MCPs para desenvolvedores | PARCIAL | Funções e regra “menu, not a shopping spree” conferem. O print escreve `Postgres / Supabase / Neo`; o catálogo normaliza para **Neon** sem evidência no próprio print. Preservar “Neo [texto visível; identidade a verificar]”. |
| AC-06-PRT-009 | MCPs para times e empresas | CONFIRMADA | Slack, Linear, Notion, Jira/Confluence via Rovo, Calendar e Gmail com aprovação humana no envio conferem. |
| AC-06-PRT-010 | MCPs para criadores | CONFIRMADA | Higgsfield, DaVinci Resolve, Figma, ElevenLabs e YouTube conferem, inclusive números promocionais. |
| AC-06-PRT-011 | pagamentos e finanças | CONFIRMADA | Stripe, Plaid, QuickBooks e regra read-only/aprovação manual conferem. |
| AC-06-PRT-012 | trading e mercados | PARCIAL | Polygon.io, CoinGecko, CCXT e TradingView conferem. O print diz apenas “Data tools first”; “execução depois” é inferência prudente do catálogo, não texto visível. Há numeração `3` repetida em CCXT e TradingView. |
| AC-06-PRT-013 | conectores para empresários | CONFIRMADA | Os 20 itens, categorias, caminho de instalação, numeração duplicada e typos “Ontlook”/“Microsoft 366” conferem. Capacidades e suporte não foram validados. |

## Correções materiais para as fichas da Fase 2

1. **AC-04-PRT-008:** separar “pago” do conteúdo visual.
2. **AC-05-PRT-006:** não atribuir ao Best a frase específica do Better sobre ângulo, tom e público.
3. **AC-05-PRT-007:** usar “não ler automaticamente”, não “nunca reler”; remover a instrução inexistente de editar o prompt original.
4. **AC-05-PRT-011:** refazer a descrição com quatro seções; excluir todo o bloco Conta/API ausente.
5. **AC-06-PRT-008:** preservar `Neo` como texto observado e verificar a identidade antes de normalizar para Neon.
6. **AC-06-PRT-012:** distinguir “data tools first” da interpretação “execução depois”.

## Síntese provisória

1. **Memória, conhecimento e RAG não têm configuração universal:** valores de chunk, overlap, k, embedding e banco são hipóteses de partida que exigem corpus, perguntas e evals representativos.
2. **O carrossel RAG é útil como pipeline, mas tecnicamente envelhecível:** APIs, imports e modelos não podem virar exemplo oficial sem teste de versão.
3. **Skill é contrato comportamental:** gatilho, escopo, etapas, recursos, saída, teste positivo, teste negativo e revisão — não apenas um arquivo com dicas.
4. **Atalhos de prompt não são capacidades:** `/goal`, `/devil` ou `/architect` só se tornam comandos confiáveis com implementação, contrato e testes.
5. **Conector é autoridade externa:** leitura, escrita, envio, publicação e transação devem ter permissões, logs, confirmação, idempotência e rollback proporcionais ao efeito.
6. **Catálogo não é marketplace aprovado:** frases “instale primeiro”, “oficial”, “grátis” e “open source” pedem verificação de origem, licença, manutenção, telemetria e privilégio.
7. **Combinações importam mais que volume:** o próprio material recomenda menu por caso de uso; a arquitetura deve evitar coleção indiscriminada de MCPs.
8. **Finanças e trading ficam em quarentena:** começar somente-leitura é piso, não controle completo; dados, recomendação, execução e custódia devem permanecer separados.

## Portas candidatas de avaliação

- nenhum valor padrão de RAG entra sem conjunto de avaliação e medição;
- nenhum código de carrossel entra sem teste em ambiente isolado e versão fixada;
- nenhuma skill entra sem testes de ativação indevida e não ativação;
- nenhum slash command é tratado como nativo sem documentação primária;
- nenhum conector recebe escrita por padrão;
- emails, mensagens, calendário, CRM, publicação, finanças e trading exigem confirmação humana e trilha de auditoria;
- licença, origem, escopo de dados, retenção, telemetria e revogação precisam ser conhecidos antes de qualquer piloto.

Claude pode usar este relatório para corrigir NC/cobertura e extrair candidatos nas Fases 2–4. Nenhuma correção deve ser aplicada automaticamente ao acervo-fonte ou convertida em Carta, Spec, Skill, Agente, Command, Workflow, arquitetura ou decisão oficial.

O acervo informa o LucaX Enterprise OS, mas não determina sua arquitetura.
