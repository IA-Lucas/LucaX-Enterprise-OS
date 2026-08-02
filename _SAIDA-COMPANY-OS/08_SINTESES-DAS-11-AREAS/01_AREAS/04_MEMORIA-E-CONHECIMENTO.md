> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

# SÍNTESE — ÁREA 04 — MEMÓRIA E CONHECIMENTO

**Frente:** Programa de Inteligência do Acervo · **Fase 3 — Síntese** (missão **A3**) · **Data:** 2026-07-29 · **Avaliador:** Claude Opus 5 (Fase 3)

**Origem:** external-evidence · **Autoridade:** nenhuma · **Estado:** provisório · **Normativo:** não · **Adoção:** não-decidida

**Entrada:** as 32 fichas de `_SAIDA-COMPANY-OS/07_FICHAS-DE-EVIDENCIA/04_MEMORIA-E-CONHECIMENTO.md` (7 REPO · 13 PRINT · 12 VÍDEO · 0 PLANILHA), lidas integralmente, mais as pré-correções de `00_PRE-CORRECOES-E-CORRESPONDENCIA.md`. Pergunta central da área: *como o sistema lembra, indexa e recupera*.

**Registro de contagem desta síntese:** a contagem ficha a ficha produz **10** itens em `EXIGE PESQUISA` e **19** em `REFERÊNCIA`; a tabela de fechamento do próprio arquivo de fichas declara 9 e 20. As fichas individuais prevalecem nesta síntese; a divergência de 1 item é registrada como anomalia (ver §4 e §12), sem resolução silenciosa.

---

## 1. O que sabemos

A área cobre as três etapas da pergunta central — ingestão, indexação e recuperação — com artefatos concretos em cada uma:

- **Ingestão documental:** existe um conversor pronto de PDF, Office, imagem, áudio, HTML e EPUB para Markdown, com aviso de segurança do próprio autor (I/O com os privilégios do processo) e plugins desabilitados por padrão (`AC-04-REP-004`, LV4). A série de slides nomeia cinco carregadores por tipo de fonte (`AC-04-PRT-003`) e registra que o pré-processamento **não** é fornecido pelo framework — é camada que o usuário escreve (`AC-04-PRT-006`).
- **Memória entre sessões:** há um artefato LV4 que captura observações por hook — sem que o agente precise "lembrar de lembrar" — com 213 arquivos de teste, incluindo diretório de segurança, e módulo de recuperação próprio (`AC-04-REP-002`). Um vídeo demonstra o padrão análogo por skill de fechamento que salva a conversa e recupera por busca semântica em plataforma de terceiro — é isto que a inspeção mostra, e **não** o "Agent View / consumo de tokens" que o catálogo declarou (`AC-04-VID-002`, NC=0). Um segundo vídeo exibe o ciclo completo — bootstrap, trabalho, consolidação, retomada — como estrutura de diretórios nomeada e copiável (`AC-04-VID-011`).
- **Indexação estrutural de código:** existe um artefato LV4 que indexa funções, classes, cadeias de chamada e rotas em grafo persistente exposto por 14 ferramentas MCP, com binário estático e processamento declaradamente local (`AC-04-REP-003`). Seus números centrais vêm de um preprint citado e **não lido**; nenhum número dele entra nesta síntese como fato (`AC-04-REP-003`, E15=2).
- **Recuperação fundamentada em fonte (RAG):** a série completa de 12 slides percorre o pipeline inteiro — stack, carregamento, pré-processamento, segmentação, embedding, banco vetorial, recuperação, geração, avaliação, ajuste e resumo (`AC-04-PRT-002` a `AC-04-PRT-013`) —, e a nota de conjunto registra que **nenhum slide traz corpus, medição ou resultado**, com valores numéricos apresentados como padrões sem método (`AC-04-PRT-004`, `AC-04-PRT-007`, `AC-04-PRT-010`). O slide de avaliação nomeia métricas sem exibir nenhum eval executado (`AC-04-PRT-013`). Há ainda a via de RAG hospedado por terceiro via automação de navegador (`AC-04-REP-005`) e a alternativa auto-hospedada completa ao mesmo produto (`AC-04-REP-006`).
- **Três vias de memória em disputa, declaradas pelo próprio acervo e não decididas:** pasta de markdown sem banco vetorial (`AC-04-REP-001`), RAG próprio (série `AC-04-PRT-002`–`013`) e RAG hospedado por terceiro (`AC-04-REP-005`). O fechamento da área registra que a decisão permanece em aberto.
- **Comparação de estratégias:** um item contrasta RAG, CAG e MAG no mesmo quadro, com riscos nomeados, e registra a hipótese híbrida "núcleo em cache + cauda por recuperação" como hipótese a testar, não decisão (`AC-04-VID-001`); um segundo reduz o mesmo conteúdo a um diagrama (`AC-04-VID-005`, E14=1).
- **Memória com governança:** os quadros mostram grafo de pessoas × projetos com exigência declarada de segregação de acesso por papel (`AC-04-VID-003`), memória ligada a rituais operacionais datados (`AC-04-VID-006`), e o princípio de separar preparação de evidências de raciocínio/redação, com formato de entrega definido (`AC-04-VID-004`).

## 2. Fontes mais fortes e por quê

Os sete repositórios são os únicos itens LV4 da área; os 25 itens de mídia são LV3-V (alguns com LV3-A), sem inspeção direta do binário por esta frente. Dentro do LV4, as fichas mais fortes, pelos dados da própria ficha:

- **`AC-04-REP-002`** — NF=4, **7/7 eixos determinados, 0 ND**, E06=3 com controles documentados (`SECURITY.md`, testes de segurança), E07=4, 213 arquivos de teste, nenhuma porta de veto. Restrições registradas: E12=2 (memória persistente, reversão com perda), E10=2 (16,6 MB) e fluxo declarado de dados para serviço externo `cmem.ai`.
- **`AC-04-REP-004`** — NF=4, E06=4 (superfície delimitada pelo próprio README, menor privilégio declarado), E07=4, nenhum veto; chegou a CANDIDATO FORTE **no limite** de 2 ND (E05 e E13) — um terceiro ND o fecharia.
- **`AC-04-REP-003`** — NF=4, E06=4, E07=4, 173 arquivos de teste com contratos de escala; é tecnicamente o mais denso da área, mas E15=2 (números dependentes de preprint não lido), E10=0 (1,23 GB, o maior item do acervo) e E05=ND o mantêm fora das classes de candidato (DEF-13 registrada).
- **`AC-04-REP-006`** — NF=3 (mediana 3,5 arredondada para baixo por regra), 1 ND, nenhum veto; única alternativa auto-hospedada completa ao produto de terceiro que `AC-04-REP-005` acessa por automação.

Os 12 slides RAG+LangChain têm LV3-V, 5 ND cada e vetos V2/V4 disparados (`AC-04-PRT-002` a `AC-04-PRT-013`): valem como mapa conceitual confirmado por inspeção visual (`107`), nunca como validação de parâmetro. Nenhum item da área foi pontuado por popularidade; badges e contagens de visualização foram explicitamente neutralizados por P-3 nas fichas (`AC-04-REP-001`, `AC-04-REP-002`).

## 3. Padrões recorrentes

- **Números sem método.** O padrão se repete em pelo menos cinco itens: "300 is optimal" (`AC-04-PRT-007`), chunk/overlap/k/temperatura como padrões de produção (`AC-04-PRT-004`), k=5 e faixa 3–10 (`AC-04-PRT-010`), "memória infinita" e "custo muito menor" (`AC-04-VID-002`, V7), "zero alucinação" (`AC-04-VID-004`, V7), e os números do preprint não lido (`AC-04-REP-003`). Em todos, a ficha marcou a alegação como não verificada e a lacuna foi nomeada.
- **A recomendação de medir antes de adotar.** O roteiro de diagnóstico sintoma→parâmetro (`AC-04-PRT-004`), a tríade de métricas de avaliação (`AC-04-PRT-013`) e o "comece simples e otimize com base em resultado" (`AC-04-PRT-005`) convergem: nenhum valor padrão entra sem conjunto de avaliação.
- **Proveniência como requisito.** Cada nota ligada à origem (`AC-04-VID-008`), pacote fechado de evidências com colunas fixas (`AC-04-VID-004`), "acumulação não equivale a verdade" (`AC-04-VID-011`).
- **Divulgação progressiva / economia de contexto.** Carregar esquema só quando necessário (`AC-04-REP-007`), compactação de histórico como gestão de memória (`AC-04-VID-010`), compressão semântica na captura (`AC-04-REP-002`).
- **Captura que não depende da disciplina do agente.** Hook de captura (`AC-04-REP-002`), skill de fechamento (`AC-04-VID-002`), rotinas periódicas sobre o vault (`AC-04-VID-006`, `AC-04-VID-009`), ciclo de consolidação ao fim da sessão (`AC-04-VID-011`).
- **Superfícies sensíveis declaradas e não inspecionadas.** Dados de pessoas com segregação só afirmada (`AC-04-VID-003`), dados financeiros e execução desassistida (`AC-04-VID-006`), plugins e servidor MCP com acesso ao vault (`AC-04-VID-009`), conversa inteira salva em plataforma de terceiro (`AC-04-VID-002`), agente com escrita autônoma em memória (`AC-04-VID-012`).

## 4. Conflitos e divergências

- **As três vias de memória se contradizem mutuamente**: markdown puro sem banco vetorial (`AC-04-REP-001`) × RAG próprio (série `AC-04-PRT-002`–`013`) × RAG hospedado por terceiro (`AC-04-REP-005`). O próprio acervo declara a disputa e ela permanece em aberto; esta síntese não a decide.
- **Contradição explícita dentro do acervo:** "quanto mais contexto, melhor" (`AC-04-VID-010`, fala provável não verificada) × queda de qualidade com o preenchimento da janela (`AC-08-VID-008`, fora desta área). Nenhuma das duas verificada; nenhuma prevalece.
- **Divergência interna de número no mesmo item:** a fala provável diz "4 pessoas mapeadas" e os quadros mostram "24 pessoas" (`AC-04-VID-012`); nenhum dos dois confirmado, e nenhum entra como fato.
- **Tensão interna no mesmo README:** "10× fewer tokens" (atribuído ao preprint) × "120x fewer tokens" (exemplo próprio) (`AC-04-REP-003`) — registrada na ficha, não reconciliada.
- **Catálogo × fonte:** um item divergente (NC=0): `AC-04-VID-002` — o catálogo diz "Agent View: histórico/memória e consumo de tokens"; a inspeção mostra persistência entre sessões por busca semântica em plataforma de terceiro com skill de fechamento. **Esta síntese usa só a inspeção.** Três parciais (NC=2): o atributo "pago" de um modelo de embedding não aparece no print (`AC-04-PRT-008`); o "foco em privacidade" não tem suporte no material lido (`AC-04-REP-006`); e o catálogo condensa em uma frase as **cinco práticas numeradas** que a fonte anuncia como cinco (`AC-04-VID-010`) — a omissão muda o sentido e está nomeada aqui.
- **Anomalia de contagem da área:** a tabela de fechamento das fichas declara 9 `EXIGE PESQUISA` e 20 `REFERÊNCIA`; a soma ficha a ficha dá 10 e 19. Registrada, não reconciliada — as fichas individuais prevalecem.
- **Classificação dupla formalmente aberta:** `AC-04-REP-003` satisfaz ao mesmo tempo EXIGE PESQUISA e PADRÃO A ESTUDAR, sem regra de precedência na rubrica (DEF-13); prevaleceu EXIGE PESQUISA na ficha, e esta síntese o registra como PESQUISAR.

## 5. Candidatos fortes, pilotos e referências

- **CANDIDATO-FORTE (3):** `AC-04-REP-002` (captura por hook com testes e zero ND), `AC-04-REP-004` (ingestão documental com E06=4), `AC-04-REP-006` (auto-hospedado completo, NF=3). Nenhum equivale a adoção; as restrições estão em §7.
- **PILOTO:** nenhum — a área teve zero `CANDIDATO A PILOTO` (fechamento da área; conferido ficha a ficha).
- **REFERENCIA (19):** os 11 slides da série RAG não pendentes (`AC-04-PRT-001`, `002`, `003`, `005`, `006`, `008`, `009`, `010`, `011`, `012`, `013`) e 8 vídeos (`AC-04-VID-001`, `003`, `005`, `006`, `007`, `010`, `011`, `012`) — insumos de consulta LV3-V com valor de padrão ou de mapa conceitual, todos com 5 ND e vetos V2/V4, nenhum verificável como artefato.
- **PESQUISAR (10):** ver §9. Inclui os dois itens cujo número é o próprio conteúdo e que, por V7, **não têm conteúdo avaliável além do próprio texto** (`AC-04-VID-002`, `AC-04-VID-004`), e o item com risco declarado e experimento pendente (`AC-04-REP-005`).

## 6. O que não adotar

- **Nenhum número de slide como padrão:** chunk 300, overlap 50–100, k 3–10, temperatura 0, k=5 — todos sem corpus, método ou medição declarados (`AC-04-PRT-004`, `AC-04-PRT-007`, `AC-04-PRT-010`); a própria ficha cita `107`: são hipóteses de partida que exigem corpus e evals representativos.
- **Nenhuma promessa de marketing como fato:** "memória infinita" e "custo muito menor" (`AC-04-VID-002`), "zero alucinação" (`AC-04-VID-004`), "16 milhões de views" (`AC-04-REP-001`), os números do preprint não lido (`AC-04-REP-003`), "145 documentos, 591 ideias, 685 conexões" (`AC-04-VID-008`), e a contagem interna divergente de `AC-04-VID-012`.
- **A tabela comparativa "Why NotebookLM, Not Local RAG?"** — sem fonte, método ou amostra, produzida pelo próprio autor; sustenta E15=0 e V7 (`AC-04-REP-005`).
- **O modo anti-detecção como funcionalidade:** declarado pelo próprio material ("better anti-detection with Google services"), risco **declarado e não confirmado** (E06=1, `AC-04-REP-005`) — não é risco confirmado, e também não é benefício estabelecido; a avaliação jurídica é pendência do proprietário.
- **A descrição de catálogo de `AC-04-VID-002`** (NC=0) e os acréscimos parciais de catálogo (`AC-04-PRT-008` "pago"; `AC-04-REP-006` "privacidade"; a condensação de `AC-04-VID-010`).
- **A prescrição de terceiro embutida no catálogo** ("se o sistema for mexer em código próprio, esta é a peça", `AC-04-REP-003`) — instrução registrada e não obedecida já na Fase 2.
- **Nada por repetição:** o cluster Graphify (`AC-04-VID-008`, `AC-04-VID-012`, mais `AC-02-VID-009`/`011` fora da área) e as convergências temáticas (`AC-04-VID-005` × `AC-04-VID-001`) não verificam nada (regra P-3 aplicada nas fichas).

## 7. Riscos e dependências

- **Risco declarado, não confirmado (E06=1):** modo anti-detecção contra serviço de terceiro, com autenticação persistente armazenada localmente (`AC-04-REP-005`). Dependência: avaliação jurídica de termos de serviço + experimento comparativo — ato do proprietário, não desta frente.
- **Fluxo de dados para serviço externo por padrão:** o changelog de `AC-04-REP-002` registra sincronização de memórias para `cmem.ai` com credencial própria — achado registrado na ficha, modelo de cobrança não declarado no trecho lido (E09=3).
- **Reversão com perda:** memória persistente descartada na remoção (`AC-04-REP-002`, E12=2); estado acumulado em banco (`AC-04-REP-006`, E12=2).
- **Superfície de 1,23 GB não delimitável** a partir do que foi lido (`AC-04-REP-003`, E10=0) — o item foi o caso R-04 da calibração; o teto de leitura foi respeitado.
- **Licença ausente na raiz efetiva** (`AC-04-REP-007`, caso I-04 / bloqueio B-02) — depende de pesquisa externa à origem pública.
- **Vendor lock declarado:** todo o valor depende de um produto de terceiro acessado por automação de navegador, sem API nem exportação (`AC-04-REP-005`, E11=1).
- **Segurança não fechada em candidato:** três arquivos de `AC-04-REP-001` permanecem não lidos (E06=ND) e o fluxo pede Acesso Total ao Disco, Gmail e login em navegador — pendência resolvível na própria fonte, dentro do teto de leitura.
- **Permissões sobre a memória:** segregação por papel apenas afirmada (`AC-04-VID-003`), plugins e MCP com acesso ao vault (`AC-04-VID-009`), escrita autônoma de aprendizados sem revisão declarada (`AC-04-VID-012`) — todos LV3-V, superfícies retratadas, não avaliadas.

## 8. Lacunas

- **Preprint arXiv:2603.27277 nunca lido** — sustenta os três números centrais de `AC-04-REP-003`; verificação externa escrita na ficha.
- **Licença e titularidade de `AC-04-REP-007`** — ausentes na raiz efetiva (B-02); exige origem pública.
- **Identidade, repositório e licença de "Graphify"** — lacuna nomeada uma vez em `AC-04-VID-008` e compartilhada com `AC-04-VID-012` e itens da área 02.
- **Identidade, licença e escopo de permissão dos sete plugins e do servidor MCP** de `AC-04-VID-009`.
- **Os três arquivos não lidos de `AC-04-REP-001`** (E06=ND) — única pendência da área resolvível dentro da própria fonte e dentro do teto.
- **E05 (manutenção) em ND** nos CANDIDATO-FORTE `AC-04-REP-004` e `AC-04-REP-006` e em `AC-04-REP-003` — nenhuma data observável dentro das fontes.
- **E13 (testes) em ND em `AC-04-REP-004`** — suíte não localizada sob o teto de leitura (monorepo com `packages/`).
- **Nenhuma medição própria existe na área:** todos os experimentos que fechariam lacunas (chunk/overlap/k — `AC-04-PRT-004`/`AC-04-PRT-007`, contado uma vez; consumo de `AC-04-VID-002`; perguntas de resposta conhecida de `AC-04-VID-004`; comparativo de `AC-04-REP-005`) dependem de ato do proprietário e nenhum foi executado.
- **Fala dos vídeos sem revisão humana** — toda fala citada nas fichas é provável, nunca exata; em dois vídeos o STT é lexicalmente vazio (`AC-04-VID-001`, `AC-04-VID-004` entre outros), e onde a fala diverge dos quadros (`AC-04-VID-012`) o desconhecido permanece desconhecido.
- **A decisão entre as três vias de memória** (`AC-04-REP-001` × série `AC-04-PRT` × `AC-04-REP-005`) — declarada em aberto pelo próprio acervo; não é lacuna de evidência apenas, é decisão que esta frente não toma.

## 9. Decisão provisória

| ID | Classe | Motivo (uma linha, com base na ficha) |
|---|---|---|
| `AC-04-REP-001` | PESQUISAR | E06=ND (V2): 3 arquivos não lidos com superfície ampla declarada; verificação cabe no teto |
| `AC-04-REP-002` | CANDIDATO-FORTE | RF homônimo: LV4, NF=4, 0 ND, E06=3, E07=4, nenhum veto |
| `AC-04-REP-003` | PESQUISAR | E15=2 e E10=0 fecham as classes de candidato; preprint não lido é a lacuna (DEF-13 registrada) |
| `AC-04-REP-004` | CANDIDATO-FORTE | RF homônimo: LV4, NF=4, 2 ND no limite, E06=4, nenhum veto |
| `AC-04-REP-005` | PESQUISAR | V2 (E06=1) + V7 (E15=0): anti-detecção declarado e tabela sem fonte; depende do proprietário |
| `AC-04-REP-006` | CANDIDATO-FORTE | RF homônimo: LV4, NF=3, 1 ND, nenhum veto; "privacidade" do catálogo não confirmada (NC=2) |
| `AC-04-REP-007` | PESQUISAR | V4: licença ausente na raiz efetiva (I-04/B-02); 3 ND |
| `AC-04-PRT-001` | REFERENCIA | RF homônimo: infográfico LV3-V, 5 ND, V2/V4; valor de mapa conceitual |
| `AC-04-PRT-002` | REFERENCIA | RF homônimo: capa da série; decomposição em sete componentes, sem execução |
| `AC-04-PRT-003` | REFERENCIA | RF homônimo: padrão um-carregador-por-fonte; implementação específica não verificada |
| `AC-04-PRT-004` | PESQUISAR | Valores padrão sem corpus nem método (E15=1); fecha só com experimento próprio |
| `AC-04-PRT-005` | REFERENCIA | RF homônimo: resumo da série; "comece simples e otimize com resultado" |
| `AC-04-PRT-006` | REFERENCIA | RF homônimo: único slide que nomeia etapa não resolvida pelo framework |
| `AC-04-PRT-007` | PESQUISAR | "300 is optimal" é alegação do slide (E15=1); mesmo experimento de `AC-04-PRT-004`, contado uma vez |
| `AC-04-PRT-008` | REFERENCIA | RF homônimo: comparação de embeddings; "pago" é acréscimo do catálogo (NC=2), fora da síntese |
| `AC-04-PRT-009` | REFERENCIA | RF homônimo: padrão local × gerenciado; seleção datada, sem benchmark |
| `AC-04-PRT-010` | REFERENCIA | RF homônimo: lacuna dos números já nomeada em `AC-04-PRT-004`/`007`, não contada de novo |
| `AC-04-PRT-011` | REFERENCIA | RF homônimo: trade-off das três estratégias de cadeia; agregação de material público |
| `AC-04-PRT-012` | REFERENCIA | RF homônimo: código exibido e declaradamente não testado |
| `AC-04-PRT-013` | REFERENCIA | RF homônimo: slide de avaliação sem eval executado; métricas nomeadas valem como vocabulário |
| `AC-04-VID-001` | REFERENCIA | RF homônimo: único contraste RAG×CAG×MAG; quadros simplificam e não mostram evals |
| `AC-04-VID-002` | PESQUISAR | V7 (E15=0) + NC=0: sem conteúdo avaliável além do próprio texto; fala provável não é fato |
| `AC-04-VID-003` | REFERENCIA | RF homônimo: segregação por papel afirmada, produto não identificável |
| `AC-04-VID-004` | PESQUISAR | V7 (E15=0): "zero alucinação" sem medição; fecha só com experimento próprio |
| `AC-04-VID-005` | REFERENCIA | RF homônimo: mesmo conteúdo de `AC-04-VID-001` reduzido a diagrama (E14=1) |
| `AC-04-VID-006` | REFERENCIA | RF homônimo: memória por rituais; riscos altos declarados pela trilha, não avaliados |
| `AC-04-VID-007` | REFERENCIA | RF homônimo: só narrativa (E02=1); tese sem caso medido |
| `AC-04-VID-008` | PESQUISAR | Identidade/licença de "Graphify" fora do acervo; lacuna do cluster contada uma vez aqui |
| `AC-04-VID-009` | PESQUISAR | Identidade, licença e permissões de 7 plugins + MCP; exige pesquisa externa |
| `AC-04-VID-010` | REFERENCIA | RF homônimo: cinco práticas; omissão do catálogo nomeada (NC=2); contradição registrada, não verificada |
| `AC-04-VID-011` | REFERENCIA | RF homônimo: RP=4, esquema de diretórios copiável é o próprio valor; nada externo a verificar |
| `AC-04-VID-012` | REFERENCIA | RF homônimo: ferramenta não identificada; números internos divergentes, nenhum confirmado |

Nenhuma das 32 classificações equivale a adoção oficial.

## 10. Experimento que poderia validá-la

**Proposta — não plano aprovado.** A decisão provisória mais carregada da área é o trio CANDIDATO-FORTE (§9), e a lacuna transversal mais repetida é "números sem método" (§3). Um único desenho atacaria as duas: montar, sobre um corpus desta casa e um conjunto de perguntas de resposta conhecida, um pipeline de ingestão+recuperação usando os artefatos de `AC-04-REP-004` (ingestão) e da decomposição da série `AC-04-PRT-002`–`013` (chunking, embedding, k), variando chunk/overlap/k e medindo qualidade de recuperação e custo — o **mesmo** experimento que fecha `AC-04-PRT-004` e `AC-04-PRT-007` (contado uma vez nas fichas) — e, em paralelo, submeter o mesmo conjunto de perguntas à via de captura por hook de `AC-04-REP-002`, medindo se a memória acumulada melhora respostas sem degradar contexto, com atenção ao fluxo declarado para `cmem.ai`. Critério de validação declarado de antemão: taxa de afirmação sustentada pelas fontes fornecidas e custo por resposta. A execução exigiria ato do proprietário (benchmark próprio), que esta frente não tem autoridade para iniciar; e nenhuma das 67 verificações de EXIGE PESQUISA foi executada nesta fase.

## 11. Confiança da síntese

**Média.** Justificativa rastreável:

- **Cobertura de LV:** apenas 7 dos 32 itens são LV4 (todos os repositórios); os 25 restantes são LV3-V (14 deles também LV3-A, sem revisão humana) — a evidência de mídia é derivada de quadros e STT bruto, nunca de inspeção direta.
- **Volume de ND:** 133 eixos em ND de 480 possíveis (27,7%), valor recontado por ferramenta na Fase 2 e registrado no fechamento da área — a maioria concentrada nos 25 itens de mídia, com 5 ND cada.
- **Itens V7 na área:** 3 (`AC-04-REP-005`, `AC-04-VID-002`, `AC-04-VID-004`), todos com E15=0 — neles, nenhum número entrou como fato.
- **Itens NC=0:** 1 (`AC-04-VID-002`), tratado pela inspeção; **NC=2:** 3 (`AC-04-REP-006`, `AC-04-PRT-008`, `AC-04-VID-010`), omissões nomeadas.
- **EXIGE PESQUISA na área:** 10 de 32 (pela contagem ficha a ficha), com 5 verificações dependentes do proprietário — três delas experimentos e uma jurídica — e nenhuma executada nesta fase.
- **Anomalias não resolvidas:** divergência de 1 item entre a contagem ficha a ficha e a tabela de fechamento da área (§4); DEF-13 em `AC-04-REP-003`; divergência interna de número em `AC-04-VID-012`.

A confiança é **média e não alta** porque mais de três quartos da área repousa em LV3-V e quase um terço dos eixos é ND; é **média e não baixa** porque os sete LV4 têm hashes reconferidos sem divergência, as três classificações de CANDIDATO-FORTE têm as regras de entrada citadas na própria ficha, e nenhuma lacuna ficou sem nome.

## 12. Cobertura

| ID | Tipo | LV | RF da ficha | Decisão provisória |
|---|---|---|---|---|
| `AC-04-REP-001` | REPO | LV4 | EXIGE PESQUISA | PESQUISAR |
| `AC-04-REP-002` | REPO | LV4 | CANDIDATO FORTE | CANDIDATO-FORTE |
| `AC-04-REP-003` | REPO | LV4 | EXIGE PESQUISA | PESQUISAR |
| `AC-04-REP-004` | REPO | LV4 | CANDIDATO FORTE | CANDIDATO-FORTE |
| `AC-04-REP-005` | REPO | LV4 | EXIGE PESQUISA | PESQUISAR |
| `AC-04-REP-006` | REPO | LV4 | CANDIDATO FORTE | CANDIDATO-FORTE |
| `AC-04-REP-007` | REPO | LV4 | EXIGE PESQUISA | PESQUISAR |
| `AC-04-PRT-001` | PRINT | LV3-V | REFERÊNCIA | REFERENCIA |
| `AC-04-PRT-002` | PRINT | LV3-V | REFERÊNCIA | REFERENCIA |
| `AC-04-PRT-003` | PRINT | LV3-V | REFERÊNCIA | REFERENCIA |
| `AC-04-PRT-004` | PRINT | LV3-V | EXIGE PESQUISA | PESQUISAR |
| `AC-04-PRT-005` | PRINT | LV3-V | REFERÊNCIA | REFERENCIA |
| `AC-04-PRT-006` | PRINT | LV3-V | REFERÊNCIA | REFERENCIA |
| `AC-04-PRT-007` | PRINT | LV3-V | EXIGE PESQUISA | PESQUISAR |
| `AC-04-PRT-008` | PRINT | LV3-V | REFERÊNCIA | REFERENCIA |
| `AC-04-PRT-009` | PRINT | LV3-V | REFERÊNCIA | REFERENCIA |
| `AC-04-PRT-010` | PRINT | LV3-V | REFERÊNCIA | REFERENCIA |
| `AC-04-PRT-011` | PRINT | LV3-V | REFERÊNCIA | REFERENCIA |
| `AC-04-PRT-012` | PRINT | LV3-V | REFERÊNCIA | REFERENCIA |
| `AC-04-PRT-013` | PRINT | LV3-V | REFERÊNCIA | REFERENCIA |
| `AC-04-VID-001` | VÍDEO | LV3-V | REFERÊNCIA | REFERENCIA |
| `AC-04-VID-002` | VÍDEO | LV3-V + LV3-A | EXIGE PESQUISA | PESQUISAR |
| `AC-04-VID-003` | VÍDEO | LV3-V + LV3-A | REFERÊNCIA | REFERENCIA |
| `AC-04-VID-004` | VÍDEO | LV3-V | EXIGE PESQUISA | PESQUISAR |
| `AC-04-VID-005` | VÍDEO | LV3-V | REFERÊNCIA | REFERENCIA |
| `AC-04-VID-006` | VÍDEO | LV3-V | REFERÊNCIA | REFERENCIA |
| `AC-04-VID-007` | VÍDEO | LV3-V + LV3-A | REFERÊNCIA | REFERENCIA |
| `AC-04-VID-008` | VÍDEO | LV3-V | EXIGE PESQUISA | PESQUISAR |
| `AC-04-VID-009` | VÍDEO | LV3-V | EXIGE PESQUISA | PESQUISAR |
| `AC-04-VID-010` | VÍDEO | LV3-V + LV3-A | REFERÊNCIA | REFERENCIA |
| `AC-04-VID-011` | VÍDEO | LV3-V + LV3-A | REFERÊNCIA | REFERENCIA |
| `AC-04-VID-012` | VÍDEO | LV3-V + LV3-A | REFERÊNCIA | REFERENCIA |

**Totais:** 32/32 IDs representados · CANDIDATO-FORTE 3 · PILOTO 0 · ADAPTAR-PADRAO 0 · REFERENCIA 19 · PESQUISAR 10 · REJEITAR 0 · DUPLICATA 0.

> Este arquivo é evidência externa, provisória e não normativa. Não autoriza adoção de nada.
