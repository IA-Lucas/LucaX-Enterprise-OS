> EVIDÊNCIA EXTERNA  
> PROVISÓRIO  
> NÃO NORMATIVO  
> CANDIDATO À AVALIAÇÃO

# Relatório visual — Lote 03 — Áreas 04, 07 e 11

**Data:** 2026-07-29  
**Escopo:** 18 vídeos; 12 da área 04, 3 da área 07 e 3 da área 11  
**Cobertura:** 162 quadros examinados, nove por vídeo  
**Legibilidade:** LV3-V; áudio sem transcrição  
**Rastreabilidade:** IDs, nomes, duração e hashes permanecem no `92_MANIFESTO-TECNICO-DOS-VIDEOS.md`.

## Método e limites

Foram revisados nove quadros distribuídos entre 4% e 92% de cada vídeo. Texto incorporado, diagramas e interfaces são fatos visuais. Falas, autoria, popularidade, números, versões, desempenho e atribuições continuam alegações não verificadas. A descrição prévia do catálogo foi usada apenas como pista, nunca como comprovação. Nenhuma ferramenta, repositório, plugin, MCP ou automação foi instalado ou executado.

## Fichas — Área 04, conhecimento e memória

- **AC-04-VID-001 — RAG, CAG e MAG:** carrossel compara três padrões. RAG recupera trechos de uma base vetorial para acervo grande, variado e mutável; CAG pré-carrega um núcleo estável no contexto/KV cache; MAG mantém memória de trabalho, episódica e semântica entre sessões. Aponta riscos de latência, perda de contexto em chunks, memória obsoleta, privacidade e complexidade. **Achado alto:** arquitetura híbrida sugerida pelo material — CAG para identidade/núcleo e RAG para cauda longa — é uma hipótese a testar, não decisão.
- **AC-04-VID-002 — NotebookLM como memória fundamentada:** apresentador contrasta repetição/sobrecarga de contexto no Claude com um notebook que preservaria fontes. A interface do NotebookLM aparece, mas método, garantias e comparação dependem da fala. **Candidato:** NotebookLM; manter ND para a tese integral.
- **AC-04-VID-003 — grafo organizacional empresarial:** demonstra grafo de pessoas, funções, departamentos, atribuições e tarefas, com perfil individual e relações navegáveis. **Padrão candidato:** memória corporativa orientada a entidades e relações. O produto não pôde ser identificado visualmente; não promover ferramenta.
- **AC-04-VID-004 — NotebookLM + Claude para pesquisa:** fluxo visual: carregar PDFs no NotebookLM; gerar tabela comparando métodos, achados, limitações, lacunas e citações; fornecer a tabela ao Claude como pacote fechado; pedir crítica, perguntas novas e texto apenas a partir das evidências fornecidas. **Achado alto:** separar preparação fundamentada de evidências e raciocínio/redação. Promessas como “zero alucinação” e ganhos de velocidade não foram verificadas.
- **AC-04-VID-005 — RAG com núcleo em cache:** diagrama contrasta RAG convencional com composição que combina busca vetorial e contexto pré-processado em KV cache. **Valor:** reforça o híbrido “núcleo estável em cache + recuperação dinâmica”; faltam custos, invalidação, segurança e benchmark.
- **AC-04-VID-006 — vault operacional em Obsidian:** propõe Obsidian como memória do negócio, Claude Code como analista e n8n como automação. Um `CLAUDE.md` no vault reúne negócio, clientes, projetos, voz, metas e calendário; briefings matinais/pré-reunião, finanças e revisões seriam automatizados. **Valor:** memória operacional orientada a eventos e rituais. **Riscos altos:** dados pessoais, clientes, finanças, segredos, permissões, retenção e execução desassistida.
- **AC-04-VID-007 — harness de Markdown:** fragmentos de legenda associam a qualidade do software feito por IA ao “harness dos markdowns” e à capacidade de explicar a arquitetura. **Valor:** converge com guias, memória e sensores vistos no Lote 02. A composição dos “segredos” e o argumento completo continuam dependentes do áudio.
- **AC-04-VID-008 — Graphify + Obsidian + Claude Code:** carrossel transforma documentação oficial do Claude Code em notas atômicas e conexões, abre o resultado como vault e recomenda copiar também as fontes e ligar cada nota à origem. Alega 145 documentos, 591 ideias, 685 conexões e 67 grupos. **Achado alto:** grafo derivado precisa preservar proveniência verificável. **Candidato em quarentena:** Graphify.
- **AC-04-VID-009 — ecossistema de plugins Obsidian:** apresenta Smart Connections, Copilot, Templater, Dataview, Tasks, Periodic Notes e `mcpvault`; sugere síntese matinal, cruzamento de ideias, kickoff, auditoria do vault, processamento noturno e múltiplos vaults. **Valor:** biblioteca de padrões operacionais. **Risco crítico:** plugins e MCP com acesso à memória, rotina desassistida, injeção de prompt, exfiltração e cadeia de suprimentos. Números e autoria de “Official Obsidian Skills” não foram verificados.
- **AC-04-VID-010 — práticas de Claude Code:** o vídeo anuncia “cinco segredos”; os quadros permitem recuperar uso de Plan Mode, revisão/ajuste antes da execução, declaração de objetivo/contexto, referências a arquivos e Skills, incluindo exemplo `pr-review`. **Valor:** planejamento explícito e capacidades reutilizáveis. A lista completa e a justificativa dependem da fala.
- **AC-04-VID-011 — segundo cérebro baseado em arquivos:** estrutura visual `vault/` com `CLAUDE.md`, `memory/`, `pessoas/`, `projects/`, `decisoes/` e `agents/`. O ciclo proposto lê instruções/memória no início, acessa o vault durante a sessão, atualiza `memory/` ao final e retoma na sessão seguinte. **Achado alto:** bootstrap → trabalho → consolidação → retomada. **Risco:** acumulação não equivale a verdade; exige fonte, validade, expiração, acesso e revisão.
- **AC-04-VID-012 — grafo de “segundo cérebro”:** afirma que o Claude “não lembra” e mostra um grafo produzido a partir de cerca de 300 arquivos, 24 pessoas e mais de 160 notas diárias, com comunidades e conexões. **Valor:** demonstração visual de recuperação relacional. Quantidades, qualidade, causalidade e ferramenta precisam ser validadas; há forte sobreposição temática com AC-04-VID-008 e AC-04-VID-011.

## Fichas — Área 07, design e experiência

- **AC-07-VID-001 — demonstração visual de site arquitetônico:** gravação de um site escuro, editorial e cinematográfico, atribuído na tela a “Antigravity + Nano Banana 2 + Claude Design” e acompanhado de “Just Copy My Prompts”. **Valor:** referência de direção visual e composição. Não há processo, prompts nem evidência de qual ferramenta produziu qual parte; áudio e artefatos-fonte são necessários.
- **AC-07-VID-002 — dashboard guiado por design system:** mostra dashboard de anúncios/analytics, código em HTML/JavaScript, menção a FastAPI e Claude 4.5 Sonnet, seguida de páginas de design system com cores, superfícies, componentes, motion e interaction. **Achado:** especificar tokens, componentes e movimento antes de gerar/tornar consistente a interface. Versão do modelo, técnica e contribuição causal permanecem alegações.
- **AC-07-VID-003 — cinco capacidades para frontend com Claude Code:** lista visual: `pbakaus/impeccable` para detectar vícios visuais genéricos; `alchaincy/huashu-design` como skill de design/prototipação; `nextlevelbuilder/ui-ux-pro-max-skill` como catálogo de estilos/paletas/regras; `Leonxlnx/taste-skill` para “gosto” visual; e `microsoft/playwright` para o agente observar/testar a UI. **Valor alto como fila de investigação:** direção visual + sistema de design + feedback visual. Nomes, licenças, números e segurança precisam ser confirmados antes de baixar.

## Fichas — Área 11, aprendizagem e fundamentos

- **AC-11-VID-001 — aprender Claude Code por prática deliberada:** quatro recomendações visíveis: fazer engenharia reversa de projetos prontos; aprender a conversar com a ferramenta; realizar dez projetos pequenos antes de um projeto gigante; nunca aceitar código sem entender. **Achado:** progressão por exemplos, ciclos curtos e explicabilidade humana. A fala pode conter critérios adicionais.
- **AC-11-VID-002 — dez padrões de complexidade temporal:** infográfico animado cobre hash lookup O(1), laço que reduz pela metade O(log n), laço simples O(n), laços sequenciais O(n+m), laço com busca binária O(n log n), divide-and-conquer O(n log n), laço aninhado O(n²), laço triangular O(n²), recursão ramificada O(2ⁿ) e permutações O(n!). **Valor:** referência didática; não define arquitetura.
- **AC-11-VID-003 — quinze padrões de algoritmos:** two pointers, sliding window, binary search, frequency counting, matrix traversal, monotonic stack, prefix sum, overlapping intervals, greedy, top-K elements, backtracking, binary-tree traversal, depth-first search, breadth-first search e dynamic programming. **Valor:** mapa de estudo e vocabulário para revisão técnica; não implica adoção.

## Síntese provisória

### Área 04

O conjunto converge em uma memória corporativa composta, não em “um cérebro mágico”: núcleo estável, busca dinâmica, memória entre sessões, entidades/relações, proveniência e consolidação explícita. O padrão mais defensável é **fonte → evidência derivada → raciocínio → registro com origem e validade**. Obsidian, NotebookLM, Graphify, plugins e MCPs são implementações candidatas, não arquitetura oficial.

### Área 07

O aprendizado útil não é uma estética específica, mas o ciclo **direção visual → tokens/design system → geração → observação da interface → teste/revisão**. Ferramentas de “taste” ou antípadrões podem auxiliar crítica, desde que auditadas e subordinadas a critérios próprios do produto.

### Área 11

Há dois níveis: prática deliberada para operar agentes de código e fundamentos algorítmicos para julgar o resultado. A recomendação candidata é começar pequeno, estudar sistemas existentes, exigir explicabilidade e preservar capacidade humana de revisão.

## Candidatos novos ou reforçados

| Candidato | Motivo | Barreira obrigatória |
|---|---|---|
| NotebookLM | pacote de evidências fundamentadas | privacidade, exportação, citações, limites e avaliação comparativa |
| Graphify | notas atômicas e grafo com proveniência | identidade, repositório, licença, segurança e teste isolado |
| Obsidian | memória operacional legível em arquivos | modelo de dados, acesso, backup, retenção e governança |
| Smart Connections, Copilot, Templater, Dataview, Tasks, Periodic Notes | padrões de vault | auditoria individual, permissões, manutenção e supply chain |
| `mcpvault` | acesso de agente ao vault | menor privilégio, injeção, exfiltração, logs e confirmação |
| Impeccable | crítica de vícios visuais | confirmar identidade/licença e medir falsos positivos |
| Huashu Design | prototipação/design como skill | identidade, licença, conteúdo e segurança |
| UI UX Pro Max | catálogo de design/UX | proveniência das regras, licença e encaixe no design system |
| Taste Skill | crítica estética | critérios reproduzíveis, licença e risco de homogeneização |
| Playwright | feedback visual e teste de UI | já conhecido; avaliar integração controlada, isolamento e custo |

## Encaminhamento ao Claude

1. Consumir as fichas como LV3-V e manter ND em qualquer detalhe dependente da fala.
2. Na Fase 2, separar padrões reutilizáveis de ferramentas específicas; não pontuar popularidade ou marketing como evidência.
3. Na Fase 3, registrar proveniência, validade, expiração, acesso e revisão como requisitos de qualquer padrão de memória.
4. Na Fase 4, sintetizar a área 04 como arquitetura de conhecimento candidata; a área 07 como ciclo de design com feedback; e a área 11 como trilha de competência e revisão humana.
5. Não converter candidatos em Carta, Spec, Skill, Agente, Command, Workflow ou decisão oficial.

O acervo informa o LucaX Enterprise OS, mas não determina sua arquitetura.
