> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

# 04 — RUBRICA DE AVALIAÇÃO

**Frente:** Programa de Inteligência do Acervo · **Fase 1 — Rubrica**
**Data:** 2026-07-29
**Depende de:** `00_GOVERNANCA-DA-PESQUISA.md`, `02_MANIFESTO-DAS-FONTES.md`, `03_RELATORIO-DO-INVENTARIO.md`, `90_INTELIGENCIA-MULTIMIDIA-CODEX/93_RUBRICA-MULTIMIDIA-PARA-FASE-1.md`, `90_.../H-M1-001_HANDOFF-PARA-FASE-1.md`

---

## 1. O que esta rubrica é, e o que não é

**É** um instrumento de registro. Ela transforma evidência observada em nota justificada e rastreável, e transforma ausência de evidência em ausência declarada.

**Não é** um mecanismo de decisão. Nenhuma nota, nenhuma classificação e nenhuma combinação de notas autoriza adotar, importar, instalar, executar ou copiar qualquer coisa para o LucaX Enterprise OS. A passagem de evidência para norma só ocorre por avaliação explícita dos Frameworks oficiais 1.11–1.19, fora desta frente.

> **Regra central:** o acervo informa o LucaX Enterprise OS, mas não determina sua arquitetura.

**A Fase 1 define a rubrica. A Fase 1 não a aplica ao acervo.** As fichas do §12 são preenchidas na Fase 2. As dez fichas de `06_CALIBRACAO-DA-RUBRICA.md` são exercício de teste do instrumento, não avaliação do acervo.

### 1.1 Três proibições que governam toda pontuação

| # | Proibição | Consequência prática |
|---|---|---|
| P-1 | **Não pontuar o que não se leu.** | Nota exige evidência de nível suficiente (§4). Sem ela, `ND`. |
| P-2 | **Não pontuar a descrição no lugar da fonte.** | O catálogo tem escala própria (§6), fora dos 15 eixos, e nunca entra na nota da fonte. |
| P-3 | **Não converter popularidade em qualidade.** | Estrelas, seguidores, "trending", "600+ melhorias" e prioridade declarada por terceiro não movem nenhum eixo. Entram em E15 como alegação. |

---

## 2. Arquitetura da saída — quatro coisas separadas

A rubrica produz **quatro resultados distintos por item**. Eles nunca se somam, nunca viram uma média única e nunca se substituem.

| Sigla | O que mede | Como se expressa | Onde vive |
|---|---|---|---|
| **NF** | Qualidade da **fonte original** | 7 eixos (Bloco A) + contagem de ND | §5, Bloco A |
| **NC** | Qualidade da **descrição no catálogo** | 1 escala própria, 0–5 | §6 |
| **RP** | **Relevância potencial** para o LucaX | 3 eixos (Bloco B) + contagem de ND | §5, Bloco B |
| **AA** | **Atrito de adoção** (custo de trazer para dentro) | 5 eixos (Bloco C) + contagem de ND | §5, Bloco C |
| **RF** | **Recomendação futura** | Uma das 8 classificações, **nunca um número** | §9 |

`RF` é derivada de `NF`, `RP`, `AA`, do nível de legibilidade e das portas de veto — por regra escrita (§8, §9), não por julgamento livre.

**Por que separado.** Todo item deste acervo chegou com juízo de terceiro embutido (`03_RELATORIO-DO-INVENTARIO.md` §10, R-05). Se a nota do catálogo entrar na nota da fonte, a rubrica pontua o julgamento alheio. Se a relevância entrar na nota da fonte, um item desejável parece bem construído. As quatro saídas existem para impedir essas duas fusões.

---

## 3. ND — NÃO DETERMINÁVEL

`ND` é a marca de **ausência de evidência suficiente para pontuar um eixo**.

### 3.1 O que ND é

| Afirmação | Estado |
|---|---|
| "Não há evidência suficiente para pontuar este eixo." | **é isso que ND diz** |
| "Este eixo é ruim." | ND **não** diz isso |
| "Este eixo é zero." | ND **não** diz isso |
| "Este item é ruim." | ND **não** diz isso |
| "Este item é bom, mas não provamos." | ND **não** diz isso |

### 3.2 Regras duras de ND

1. **ND não é zero.** Zero é uma afirmação sobre a fonte, baseada em evidência de que a fonte está no pior estado observável. ND é uma afirmação sobre o avaliador.
2. **ND não entra em média.** Medianas e agregações do §8 são calculadas **apenas sobre os eixos determinados**. O número de ND é reportado ao lado, sempre, e nunca é substituído por zero, por metade da escala nem por qualquer valor imputado.
3. **ND não pode baixar nem levantar nota.** Um item com 3 eixos determinados em 4 tem mediana 4 e 12 ND — e o `RF` disso é `INDETERMINADO` (§8, V6), não "nota 4".
4. **ND não pode ser resolvido por inferência.** Não se preenche ND com raciocínio a partir do nome do arquivo, do nome do autor, da área onde o item está catalogado, do tamanho do arquivo, nem da descrição de terceiro.
5. **ND é o estado inicial de todo eixo.** Um eixo sai de ND quando, e somente quando, a evidência exigida por aquele eixo foi observada. O ônus é da nota, não do ND.
6. **Todo ND carrega o que o resolveria.** Registrar ND sem nomear a evidência faltante é registro incompleto. A ficha (§12) tem campo obrigatório para isso.

### 3.3 Onde ND é obrigatório

| Situação | Eixos afetados | Base |
|---|---|---|
| Vídeo sem transcrição (LV0–LV2) | todos os 15 | `93_RUBRICA-MULTIMIDIA` regra 1 |
| Arquivo de licença ausente, ilegível ou de titularidade ambígua | E07 | `03_RELATORIO` §11.2 |
| Segurança não avaliada | E06 | §5 |
| Manutenção sem evidência datada na própria fonte | E05 | §5, nota de acervo estático |
| Alegação sem fonte identificável | E15 | `03_RELATORIO` §10, R-06 |
| Conteúdo visual não inspecionado diretamente | todos | §4 |
| Item coberto apenas por descrição de terceiro | todos | P-2 |

### 3.4 ND versus indeterminação do próprio item

Distinguir dois casos que se parecem:

- **ND por limite do avaliador** — "não inspecionamos o diretório de testes". Resolve-se inspecionando.
- **Nota baixa por evidência de ausência** — "inspecionamos o diretório de testes e ele não existe" → E13 = 0.

A diferença entre ND e 0 em E13 é **ter olhado**. Vale para todos os eixos.

---

## 4. LV — Nível de legibilidade da evidência

`LV` responde: *quanto desta fonte foi efetivamente lido, e por quem?* É atribuído **por item** e restringe o que pode ser pontuado.

### 4.1 A escala

| Nível | Evidência disponível | Afirmação permitida |
|---|---|---|
| **LV0** | Arquivo ilegível, corrompido ou inacessível | Nenhuma. Apenas a existência do arquivo |
| **LV1** | Somente metadados técnicos | Tamanho, formato, duração, resolução, presença de áudio, contagem de arquivos, hash |
| **LV2** | Descrição de terceiro (catálogo, README lido por outro, índice) | Apenas na forma *"o catálogo afirma que…"*, com atribuição literal |
| **LV3** | Fonte parcialmente inspecionada por esta frente | Fatos observados no que foi lido, delimitados ao que foi lido |
| **LV4** | Fonte primária inspecionada por esta frente | Fatos observados sobre a fonte, com delimitação de cobertura |
| **LV5** | Fonte reproduzida, executada ou confirmada por fonte independente | Afirmação confirmada |

### 4.2 Sub-níveis de LV3 para mídia

Vindos de `93_RUBRICA-MULTIMIDIA-PARA-FASE-1.md` e adotados aqui sem alteração de sentido:

| Sub-nível | Evidência | Afirmação permitida |
|---|---|---|
| **LV3-V** | Quadros-chave revisados, OCR de texto em tela | Texto e fatos **visuais**. **Proibido atribuir fala.** |
| **LV3-A** | Transcrição automática bruta, não revisada | Fala **provável**, sempre com confiança declarada e ressalva. **Proibida citação exata.** |

`LV3-V` e `LV3-A` são independentes: um item pode ter um, o outro, ou ambos. Ter ambos **não** produz LV4.

### 4.3 LV4 e LV5 por tipo de item

| Tipo | LV4 exige | LV5 exige |
|---|---|---|
| REPO | Leitura direta, por esta frente, de README + licença + estrutura + docs + configs + testes na raiz efetiva | Execução ou reprodução — **proibida nesta frente**; portanto LV5 só por confirmação de fonte independente |
| PRINT | Inspeção visual direta da imagem por esta frente | Confirmação do conteúdo do print contra a fonte primária que ele retrata |
| PLANILHA | Leitura do conteúdo das abas, não só dos nomes | Conferência dos números contra fonte externa |
| VÍDEO | **Transcrição revisada combinada com quadros-chave** (exigência literal do handoff `H-M1-001`, item 6) | Conteúdo reproduzido ou confirmado por fonte independente |

### 4.4 Regras duras de LV

1. **LV é declarado antes de qualquer nota.** Ficha sem LV é ficha inválida.
2. **LV2 não sobe por qualidade da descrição.** Um catálogo excelente continua sendo LV2. `NC = 5` não move `LV`.
3. **Quadro-chave não é transcrição.** Proibição literal do handoff `H-M1-001`, item 5. `LV3-V` nunca é registrado como `LV3-A`.
4. **LV ≤ 2 ⇒ todos os 15 eixos em ND**, sem exceção. Consequência: `RF = INDETERMINADO` (§8, V5).
5. **LV é cobertura, não impressão.** Ao declarar LV3 ou LV4, registrar **o que exatamente foi lido**. "Li o repositório" não é registro; "li README.md, LICENSE, e a listagem da raiz efetiva" é.
6. **LV5 é inatingível por leitura.** Esta frente não executa repositórios (`00_GOVERNANCA` §5.2). LV5 só entra por confirmação independente rastreável.

### 4.5 Estado atual do acervo em LV

Fato observado, `91_ESTADO-DA-INTELIGENCIA-MULTIMIDIA.md`: **os 142 vídeos estão em LV1.** Não há STT local nem credencial autorizada; não há legenda embutida em nenhum. Descontadas as 2 duplicatas exatas, **os 140 vídeos distintos permanecem lacuna declarada** até que a trilha Codex entregue transcrição e quadros.

---

## 5. Os 15 eixos

### 5.0 Convenções que valem para todos

1. **Direção única.** Em todos os 15 eixos, **5 é sempre a melhor situação para o LucaX e 0 sempre a pior**. Os eixos de risco (E09 custo, E10 contexto, E11 fornecedor, E15 alegações) já vêm com o sentido invertido embutido nas âncoras — o avaliador **não** deve inverter nada.
2. **Âncora observável.** Cada nota descreve algo que se vê na fonte, não algo que se sente sobre ela. Se a âncora não pode ser apontada com um trecho, um arquivo ou um número, a nota não pode ser dada.
3. **Nota exige citação.** Toda nota ≠ ND registra a evidência que a sustenta (arquivo, linha, campo, número medido).
4. **Meio-termo não existe.** Não há 3,5. Se a evidência não fecha a âncora superior, vale a inferior.
5. **LV mínimo por eixo.** Cada eixo declara o LV abaixo do qual só cabe ND.

---

### Bloco A — Qualidade da fonte original → **NF**

Sete eixos. Medem o que a fonte demonstra sobre si mesma. **Nunca** medem utilidade, desejo ou conveniência.

---

#### E01 não pertence a este bloco. Bloco A começa em E02.

---

#### **E02 — Qualidade da evidência**
*Quão sustentada, pela própria fonte, é a afirmação central que ela faz.*
**LV mínimo:** LV3.

| Nota | Âncora observável |
|---|---|
| 0 | A afirmação central do item não tem nenhuma sustentação na fonte — nem artefato, nem exemplo, nem referência |
| 1 | Só prosa: README, slide ou narrativa. Nenhum artefato inspecionável que corresponda ao que é afirmado |
| 2 | Um exemplo isolado e não reprodutível (captura de tela, trecho solto, demonstração sem insumo) |
| 3 | Artefato completo e inspecionável (código, spec, configuração, documento) correspondente à afirmação, **sem** procedimento de verificação |
| 4 | Artefato completo **mais** procedimento de verificação declarado na fonte (testes, script, passos reproduzíveis), não executado por esta frente |
| 5 | Artefato e verificação **reproduzidos** ou confirmados por fonte independente rastreável (só a partir de LV5) |

**ND quando:** LV ≤ 2; ou a afirmação central do item ainda não foi identificada.

---

#### **E03 — Maturidade**
*Em que estágio de vida a fonte se declara e se demonstra.*
**LV mínimo:** LV3.

| Nota | Âncora observável |
|---|---|
| 0 | O próprio autor marca como esboço, rascunho, experimento ou "não use" |
| 1 | Protótipo: estrutura ou interface declarada instável, sujeita a mudança sem aviso |
| 2 | Funciona no cenário demonstrado, mas sem versionamento, sem release e sem tag |
| 3 | Versionado, com release ou tag identificável, ou changelog presente |
| 4 | Nota 3 **mais** documentação de instalação e uso **mais** tratamento de erro visível no código ou na configuração |
| 5 | Versão estável declarada (≥ 1.0) **mais** política de compatibilidade **mais** histórico de releases |

**ND quando:** LV ≤ 2; ou a raiz efetiva não foi inspecionada.
**Nota de acervo:** 28 dos 43 repositórios estão em profundidade dupla (`03_RELATORIO` §4.5, I-05). Avaliar a pasta externa em vez da raiz efetiva produz E03 falsamente baixo.

---

#### **E05 — Manutenção**
*Se há alguém mantendo, e com que regularidade.*
**LV mínimo:** LV3.

| Nota | Âncora observável |
|---|---|
| 0 | Arquivado, congelado ou descontinuado por declaração explícita do autor na própria fonte |
| 1 | Nenhum sinal de atividade **e** problemas conhecidos registrados em aberto na própria fonte |
| 2 | Atividade esparsa e sem cadência discernível, evidenciada por datas internas |
| 3 | Atividade recente identificável por evidência datada dentro da fonte |
| 4 | Nota 3 **mais** responsável nomeado **mais** canal de contato ou de reporte declarado |
| 5 | Cadência regular evidenciada **mais** política de suporte ou de versões declarada |

**ND quando:** LV ≤ 2; **ou — caso padrão neste acervo — a fonte é uma cópia estática sem histórico de versionamento.**

> **Regra específica deste acervo.** O acervo é composto de cópias `-main` sem histórico de repositório. Sem data de commit, sem lista de issues e sem acesso à origem pública, **E05 = ND é o resultado esperado, não a exceção.** Resolver E05 exige consultar a origem pública — o que **não** é operação desta frente e deve ser registrado como lacuna endereçável, não suprido por inferência.

---

#### **E06 — Segurança** · ⚠ eixo de veto
*Que superfície de risco a fonte abre, e o que ela faz a respeito.*
**LV mínimo:** LV3.

| Nota | Âncora observável |
|---|---|
| 0 | Risco ativo **confirmado por inspeção direta**: credencial embutida, execução de código arbitrário sem confinamento por padrão, injeção de prompt presente no conteúdo |
| 1 | Risco ativo **declarado** — pelo próprio material ou por terceiro — e ainda não confirmado por inspeção |
| 2 | Superfície ampla (rede, shell, sistema de arquivos irrestrito, execução de terceiros) **sem** nenhum controle documentado |
| 3 | Superfície declarada na fonte **com** controles parciais documentados |
| 4 | Superfície delimitada **mais** controles documentados **mais** escopo de permissão explícito |
| 5 | Nota 4 **mais** verificação de segurança independente evidenciada (auditoria, política publicada, testes de segurança executáveis) |

**ND quando:** LV ≤ 2; ou a superfície não foi inspecionada.
**Veto:** ver §8, V1 e V2. **`E06 = ND` nunca autoriza CANDIDATO FORTE nem CANDIDATO A PILOTO.**
**Caso conhecido:** o índice do acervo declara injeção de prompt em leetspeak no README de `AC-05-REP-003` (`CL4R1T4S`). Isso é **alegação não verificada** — E06 = 1, não 0 — até inspeção direta. O protocolo de leitura de conteúdo hostil está em `05_GUIA-DE-APLICACAO-DA-RUBRICA.md` §7.

---

#### **E07 — Licença e uso comercial** · ⚠ eixo de veto
*O que a licença permite, e se a titularidade é clara.*
**LV mínimo:** LV3 — **e a leitura do texto da licença, não apenas a existência do arquivo.**

| Nota | Âncora observável |
|---|---|
| 0 | A licença **proíbe** explicitamente uso comercial ou obra derivada |
| 1 | Licença restritiva com obrigações de reciprocidade que não se sabe cumprir no contexto declarado |
| 2 | Copyleft forte (ex.: GPL, AGPL): permitido, com obrigação estrutural sobre o que for derivado |
| 3 | Permissiva com cláusula adicional: atribuição estendida, restrição de marca, cláusula de patente ou de retaliação |
| 4 | Permissiva padrão (MIT, Apache-2.0, BSD) presente e íntegra na raiz efetiva |
| 5 | Nota 4 **mais** concessão explícita de uso comercial e redistribuição **mais** titularidade inequívoca |

**ND quando:** arquivo de licença **ausente**, ilegível, truncado, ou com titularidade ambígua.

> **Regra dura — ausência de licença não é nota zero.** Ausência é *indeterminação de procedência*, categoria diferente de *permissão negada*. Um item sem `LICENSE` recebe `E07 = ND`, não `E07 = 0`. A consequência de ND aqui é a **porta de veto V4** (§8), não uma nota baixa.

> **Presença de arquivo não é nota.** Ver um `LICENSE` na raiz não determina E07. É preciso ler o tipo. Um `LICENSE` de tipo não identificado permanece ND.

> **Cópia local não prova titularidade.** O acervo contém cópias. Um `LICENSE` MIT dentro de uma cópia não confirma que o titular original licenciou assim — sustenta no máximo **E07 = 4**. `E07 = 5` exige conferência na origem pública, fora desta frente.

**Casos conhecidos (`03_RELATORIO` §4.5, I-04):** `AC-02-REP-001`, `AC-04-REP-007`, `AC-05-REP-002` e `AC-07-REP-002` estão sem licença na raiz efetiva → `E07 = ND` obrigatório.

---

#### **E13 — Testes e evals**
*O que a fonte faz para saber que funciona.*
**LV mínimo:** LV3.

| Nota | Âncora observável |
|---|---|
| 0 | Inspecionado: **nenhum** teste, eval ou verificação de qualquer natureza |
| 1 | Apenas exemplos manuais ou instruções de "rode e veja" |
| 2 | Testes existem, mas cobrem só caminho feliz, ou não são executáveis isoladamente |
| 3 | Suíte de testes executável identificável, com ponto de entrada declarado |
| 4 | Nota 3 **mais** evals de comportamento de modelo ou agente — não apenas testes unitários de código |
| 5 | Nota 4 **mais** resultados publicados e reprodutíveis, com dados e critérios declarados |

**ND quando:** LV ≤ 2; ou o diretório de testes não foi inspecionado.
**Lembrete P-1:** `E13 = 0` exige ter procurado e não encontrado. Não ter procurado é ND.

---

#### **E15 — Alegações não verificadas**
*Quanto a proposta do item depende de números que ninguém conferiu.*
**LV mínimo:** LV2 — este é o único eixo do Bloco A pontuável em LV2, porque a alegação **é** o objeto de medida, e ela existe no catálogo. A alegação é registrada com atribuição literal; **isso não vale como validação** (P-2).

| Nota | Âncora observável |
|---|---|
| 0 | A proposta central do item **depende** de alegação numérica forte, **sem fonte** e não verificável |
| 1 | Alegações numéricas fortes com fonte citada, porém não conferida e não conferível com o material disponível |
| 2 | Alegações numéricas com fonte citada e **conferível**, ainda não conferida |
| 3 | Apenas alegações qualitativas; nenhum número decisivo em jogo |
| 4 | Alegações acompanhadas de método declarado e dados de apoio dentro da própria fonte |
| 5 | Alegações **verificadas** de forma independente — por esta frente ou por terceiro rastreável |

**ND quando:** LV ≤ 1; ou nenhuma alegação foi identificada ainda.
**Registro obrigatório:** toda alegação identificada é transcrita **literalmente** no campo próprio da ficha (§12), com sua origem (índice, `_CONTEUDO.md`, README, autor). Pontuar E15 sem transcrever a alegação é registro incompleto.
**Casos conhecidos (`03_RELATORIO` §10, R-06):** *"83% de qualidade, 10× menos tokens" (arXiv:2603.27277)*, *"600+ melhorias"*, *"26,1% de skills com vulnerabilidade"*, *"59–70% de fatura menor"*.

---

### Bloco B — Relevância potencial → **RP**

Três eixos. Medem **utilidade possível**, não qualidade e não permissão. Uma `RP` alta **não compensa** `NF` baixa nem risco crítico (§8, regra de não-compensação).

---

#### **E01 — Relevância para o LucaX**
*Grau em que o item endereça uma pergunta central já declarada de uma das 11 áreas do acervo.*
**LV mínimo:** LV3.

> **Ancoragem sem arquitetura.** A relevância é medida contra as **perguntas centrais das 11 áreas** (`03_RELATORIO` §4.1) — que já existem e são externas —, **nunca** contra uma arquitetura, stack ou roadmap do LucaX. Medir contra arquitetura seria decidir arquitetura, o que esta frente não pode fazer.

| Nota | Âncora observável |
|---|---|
| 0 | Não endereça a pergunta central de nenhuma das 11 áreas |
| 1 | Tangencia uma área, mas o núcleo do item é outro assunto |
| 2 | Endereça uma pergunta de área de forma genérica, sem particularizar nada |
| 3 | Endereça diretamente a pergunta central de uma área |
| 4 | Nota 3 **mais** traz artefato concreto e reutilizável (spec, configuração, esquema, teste) |
| 5 | Endereça as perguntas centrais de **duas ou mais** áreas, com artefato concreto e uso demonstrado ponta a ponta |

**ND quando:** LV ≤ 2.

---

#### **E04 — Transferibilidade**
*Quanto do item sobrevive fora do contexto do autor.*
**LV mínimo:** LV3.

| Nota | Âncora observável |
|---|---|
| 0 | Inseparável do ambiente do autor: credenciais próprias, infraestrutura própria, dados privados |
| 1 | Exige reescrita quase total; só a ideia viaja |
| 2 | O **padrão** é transferível; a implementação não é |
| 3 | Transferível com adaptação declarada e delimitada |
| 4 | Transferível por **configuração**, sem alteração de código |
| 5 | Transferível como está, parametrizado, sem premissa alguma do ambiente de origem |

**ND quando:** LV ≤ 2; ou as dependências de ambiente não foram inspecionadas.

---

#### **E14 — Diferencial estratégico**
*O que se perderia se este item não existisse.*
**LV mínimo:** LV3.

| Nota | Âncora observável |
|---|---|
| 0 | Reprodutível em horas com ferramenta já disponível |
| 1 | Conveniência sobre algo que já existe e já é acessível |
| 2 | Agregação útil de material público e amplamente conhecido |
| 3 | Resolve problema declarado sem equivalente pronto conhecido **dentro do acervo** |
| 4 | Nota 3 **mais** custo alto de reconstrução do zero: conhecimento de domínio, dados, curadoria acumulada |
| 5 | Nota 4 **mais** cria capacidade que **nenhuma outra fonte do acervo** oferece |

**ND quando:** LV ≤ 2; ou não há base de comparação dentro do acervo.
**Proibição explícita (P-3):** contagem de estrelas, seguidores, "trending" e prioridade atribuída pelo catálogo **não movem E14**. Vão para E15.

---

### Bloco C — Atrito de adoção → **AA**

Cinco eixos. Medem o **custo de trazer para dentro**. Nada aqui autoriza trazer.

---

#### **E08 — Facilidade de integração**
**LV mínimo:** LV3.

| Nota | Âncora observável |
|---|---|
| 0 | Incompatível com o ambiente declarado (sistema operacional, runtime) sem porte |
| 1 | Exige stack nova inteira **mais** serviços externos obrigatórios |
| 2 | Exige runtime adicional ainda não presente **mais** configuração manual extensa |
| 3 | Runtime já presente; instalação documentada com passos manuais |
| 4 | Instalação declarada em um comando; configuração por arquivo ou variável de ambiente |
| 5 | Nota 4 **mais** funciona sem serviço externo obrigatório e sem estado global |

**ND quando:** LV ≤ 2; ou instalação e dependências não foram inspecionadas.

---

#### **E09 — Custo operacional**
*Sentido invertido embutido: 5 = custo desprezível.*
**LV mínimo:** LV3.

| Nota | Âncora observável |
|---|---|
| 0 | Custo recorrente alto e obrigatório (licença paga, infraestrutura dedicada), sem alternativa |
| 1 | Custo recorrente obrigatório, moderado |
| 2 | Custo variável por uso, **sem** teto e **sem** instrumentação |
| 3 | Custo variável por uso, com limite ou controle possível |
| 4 | Custo marginal: apenas chamadas de modelo já previstas de qualquer forma |
| 5 | Sem custo recorrente; roda sobre recurso já existente |

**ND quando:** LV ≤ 2; ou o modelo de custo não é declarado nem observável na fonte.

---

#### **E10 — Impacto em contexto e tokens**
*Sentido invertido embutido: 5 = superfície mínima.*
**LV mínimo:** LV1 — pontuável a partir de metadados medidos (tamanho, contagem de arquivos), porque a superfície de leitura é um fato físico.

| Nota | Âncora observável |
|---|---|
| 0 | Exige carregar mais de 100 MB de texto **ou** mais de 5.000 arquivos para ser compreendido ou usado |
| 1 | 20–100 MB de texto **ou** 1.000–5.000 arquivos |
| 2 | 5–20 MB **ou** 300–1.000 arquivos |
| 3 | 1–5 MB **ou** 50–300 arquivos |
| 4 | Menos de 1 MB **ou** menos de 50 arquivos, com superfície delimitada por documento de entrada |
| 5 | Superfície mínima e declarada — um manifesto ou spec único —, com o restante carregável sob demanda |

**Regra de leitura:** quando tamanho e contagem discordarem, vale **a pior das duas** (a nota menor).
**Regra para mídia:** para PRINT, VÍDEO e PLANILHA, E10 mede a **evidência derivada** (transcrição, OCR, texto extraído), não o binário. Enquanto a evidência derivada não existir, `E10 = ND`.
**ND quando:** a superfície de leitura não é delimitável.

---

#### **E11 — Dependência de fornecedor**
*Sentido invertido embutido: 5 = sem dependência.*
**LV mínimo:** LV3.

| Nota | Âncora observável |
|---|---|
| 0 | Preso a fornecedor único, sem formato de saída aberto e sem alternativa |
| 1 | Preso a fornecedor único, com exportação apenas parcial |
| 2 | Fornecedor único, porém com formato de dados aberto |
| 3 | Dois ou mais fornecedores suportados, com troca custosa |
| 4 | Abstração de fornecedor documentada; troca por configuração |
| 5 | Sem dependência de fornecedor: roda local ou sobre padrão aberto |

**ND quando:** LV ≤ 2; ou as dependências externas não foram inspecionadas.

---

#### **E12 — Reversibilidade**
**LV mínimo:** LV3.

| Nota | Âncora observável |
|---|---|
| 0 | Irreversível: migra dados ou estado sem caminho de volta |
| 1 | Reversão exige reconstrução manual significativa |
| 2 | Reversível com perda de estado ou de histórico |
| 3 | Reversível por remoção, com efeitos colaterais documentados |
| 4 | Reversível por remoção, sem efeito residual; isolado por desenho |
| 5 | Nota 4 **mais** reversão testada ou documentada pelo próprio autor |

**ND quando:** LV ≤ 2; ou o acoplamento não foi inspecionado.

---

### 5.1 Mapa dos 15 eixos

| Eixo | Nome | Bloco | Saída | LV mínimo | Veto |
|---|---|---|---|---|---|
| E01 | Relevância para o LucaX | B | RP | LV3 | — |
| E02 | Qualidade da evidência | A | NF | LV3 | — |
| E03 | Maturidade | A | NF | LV3 | — |
| E04 | Transferibilidade | B | RP | LV3 | — |
| E05 | Manutenção | A | NF | LV3 | — |
| E06 | Segurança | A | NF | LV3 | ⚠ V1, V2 |
| E07 | Licença e uso comercial | A | NF | LV3 + leitura do texto | ⚠ V3, V4 |
| E08 | Facilidade de integração | C | AA | LV3 | — |
| E09 | Custo operacional | C | AA | LV3 | — |
| E10 | Impacto em contexto e tokens | C | AA | **LV1** | — |
| E11 | Dependência de fornecedor | C | AA | LV3 | — |
| E12 | Reversibilidade | C | AA | LV3 | — |
| E13 | Testes e evals | A | NF | LV3 | — |
| E14 | Diferencial estratégico | B | RP | LV3 | — |
| E15 | Alegações não verificadas | A | NF | **LV2** | ⚠ V7 |

**Contagem:** Bloco A = 7 eixos (E02, E03, E05, E06, E07, E13, E15) · Bloco B = 3 (E01, E04, E14) · Bloco C = 5 (E08, E09, E10, E11, E12). **Total 15.**

---

## 6. NC — Qualidade da descrição no catálogo

Escala própria, **fora dos 15 eixos**, aplicada ao que o catálogo de terceiro diz sobre o item.

| Nota | Âncora observável |
|---|---|
| 0 | A descrição do catálogo **contradiz** fato observado na fonte |
| 1 | Descrição derivada apenas do nome do arquivo; nenhum indício de inspeção |
| 2 | Descrição genérica, compatível com o item, sem detalhe verificável |
| 3 | Descrição com detalhe verificável, e o detalhe **confere** no que foi conferido |
| 4 | Nota 3 **mais** o catálogo **declara o método** pelo qual obteve a descrição |
| 5 | Nota 4 **mais** o método foi conferido por esta frente e confere |

**ND quando:** não há descrição do item no catálogo.

### 6.1 Regras duras de NC

1. **NC nunca entra em NF, RP ou AA.** É reportada isolada.
2. **NC alta não sobe LV.** Catálogo excelente continua sendo LV2 (§4.4.2).
3. **NC alta não é evidência sobre a fonte.** Mede o cuidado do catalogador, não a qualidade do item.
4. **NC = 0 é achado, não descarte.** Contradição entre catálogo e fonte vai para o registro de divergências, e a fonte prevalece.
5. **Caso conhecido — método declarado, não verificado.** Os `_CONTEUDO.md` rotulam a coluna de assunto dos vídeos como *"Título pelo conteúdo visível"*, alegando derivar de frame visível e não do nome do arquivo (`03_RELATORIO` §4.4, R-08). Isso é **declaração de método**, o que habilita `NC = 4`. Só passa a `NC = 5` quando a trilha Codex entregar quadros que confirmem o método. Se os quadros mostrarem que o título veio do nome, `NC = 0`.

---

## 7. Tratamento de alegações não verificadas

Além de E15, toda alegação identificada recebe **etiqueta de camada**, conforme `00_GOVERNANCA` §7:

| Etiqueta | Uso |
|---|---|
| `FATO OBSERVADO` | Verificado diretamente por esta frente, no sistema de arquivos ou no conteúdo |
| `ALEGAÇÃO DO AUTOR` | Afirmado pela fonte (README, código, documentação) sem verificação independente |
| `ALEGAÇÃO DO CATÁLOGO` | Afirmado pelo material de terceiro que acompanhou o acervo |
| `INFERÊNCIA` | Derivado por raciocínio a partir de fatos observados — **sempre marcado** |
| `HIPÓTESE` | Formulado para teste futuro |
| `CANDIDATO À AVALIAÇÃO` | Aplicação possível ao LucaX, sujeita a avaliação oficial |

**Regras:**

1. Alegação numérica sem fonte identificável recebe, além da etiqueta, a marca literal `NÃO VERIFICADA`.
2. Uma alegação nunca muda de camada por repetição, por confiança do autor ou por plausibilidade.
3. **Alegação não pontua eixo.** Uma fonte que *afirma* ter testes não recebe E13 > 0 por isso; recebe E13 = ND até inspeção do diretório de testes.
4. Alegação forte e não verificada da qual a proposta do item depende dispara a porta **V7** (§8).

---

## 8. Agregação, não-compensação e portas de veto

### 8.1 Como agregar

Para cada bloco, reportar **três coisas juntas, nunca separadas**:

```
NF = <mediana dos eixos determinados do Bloco A> · <n determinados>/7 · <n ND>
RP = <mediana dos eixos determinados do Bloco B> · <n determinados>/3 · <n ND>
AA = <mediana dos eixos determinados do Bloco C> · <n determinados>/5 · <n ND>
```

- **Mediana, não média.** A mediana resiste melhor a um eixo extremo isolado e não sugere precisão decimal que a escala não tem.
- **Se metade ou mais dos eixos de um bloco estiver em ND, o bloco não recebe valor** — reporta-se `ND (n determinados/N)`.
- **Nunca reportar um número de bloco sem a contagem de ND ao lado.** Um `NF = 4` sozinho é registro inválido.

### 8.2 Não-compensação

**Regra:** blocos não se compensam. Especificamente:

- `RP` alta **não** compensa `NF` baixa. Um item muito desejável e mal construído continua mal construído.
- `RP` alta **não** compensa risco crítico. Ver V1 e V3: os vetos operam **antes** de qualquer leitura de RP.
- `AA` baixa **não** rebaixa `NF`. Difícil de integrar não é o mesmo que mal feito.
- Nenhum bloco tem peso maior que outro, porque **eles não são somados**.

### 8.3 Portas de veto

Avaliadas **em ordem**, antes de escolher a classificação. A primeira que dispara manda.

| # | Condição | Consequência |
|---|---|---|
| **V1** | `E06 = 0` (risco ativo **confirmado**) | `RF = REJEITADO`, qualquer que seja o resto |
| **V2** | `E06 = 1` ou `E06 = ND` | Teto: no máximo `PADRÃO A ESTUDAR`, `REFERÊNCIA` ou `EXIGE PESQUISA`. **Nunca** CANDIDATO FORTE nem CANDIDATO A PILOTO |
| **V3** | `E07 = 0` (licença proíbe) | `RF = REJEITADO` para qualquer uso. Pode permanecer `REFERÊNCIA` apenas para leitura |
| **V4** | `E07 = ND` (licença ausente ou ambígua) | **Nunca** CANDIDATO FORTE nem CANDIDATO A PILOTO. `EXIGE PESQUISA` é o resultado natural, com a lacuna nomeada |
| **V5** | `LV ≤ 2` | `RF = INDETERMINADO` obrigatório — exceto se `DUPLICADO` por hash idêntico |
| **V6** | 8 ou mais dos 15 eixos em `ND` | `RF = INDETERMINADO` obrigatório |
| **V7** | `E15 = 0` **e** a relevância do item depende dessa alegação | Teto: `EXIGE PESQUISA` |
| **V8** | Hash do item **diverge** do registrado em `02_MANIFESTO-DAS-FONTES.md` | `RF = INDETERMINADO`, ficha reaberta, divergência registrada — ver bloqueio B-04 |

**V2 e V4 são as portas que impedem "relevância compensa risco".** Elas operam sobre a classificação, não sobre a nota — por isso um item pode ter `RP = 5` e ainda assim terminar em `EXIGE PESQUISA`.

---

## 9. As 8 classificações permitidas

`RF` é **sempre uma destas oito**, nunca um número, nunca uma recomendação em prosa.

| Classificação | Condições de entrada | O que **não** significa |
|---|---|---|
| **CANDIDATO FORTE** | `LV ≥ 4` · nenhum eixo do Bloco A abaixo de 3 · `E06 ≥ 3` · `E07 ≥ 3` · no máximo 2 ND no total · `RP ≥ 4` | Não significa adotar. Significa: pronto para avaliação oficial |
| **CANDIDATO A PILOTO** | `LV ≥ 3` · `E06 ≥ 3` · `E07 ≥ 3` · `RP ≥ 3` · no máximo 4 ND · nenhum eixo do Bloco C em 0 | Não significa pilotar. Significa: pronto para *proposta* de piloto à avaliação oficial |
| **PADRÃO A ESTUDAR** | O valor está no **padrão**, não no artefato: `E04 ≥ 3` com `E03`, `E05` ou `E08` baixos ou ND. **Não exige licença resolvida** — não se adota código | Não significa copiar o código |
| **REFERÊNCIA** | Item é insumo de consulta e não candidato a componente (prints, planilha, documentos). `LV ≥ 3` | Não significa citável como fato. A camada de afirmação continua valendo |
| **EXIGE PESQUISA** | Há relevância aparente **e** uma lacuna **nomeada e endereçável**. Obrigatório registrar: qual a lacuna e qual verificação a fecharia | Não significa promissor. Significa: falta uma coisa específica |
| **REJEITADO** | `V1` ou `V3`; **ou** `E01 = 0` com `LV ≥ 3` | Rejeitado **por evidência**, nunca por ND. Nenhum item é rejeitado por não ter sido lido |
| **DUPLICADO** | Hash idêntico a outro item, ou sobreposição de conteúdo medida | Não significa descartável. Herda a ficha do original, mantém ID próprio e rastreabilidade |
| **INDETERMINADO** | `V5`, `V6` ou `V8`. **Estado padrão de todo item ainda não lido** | **Não é veredito negativo.** É a declaração honesta de que a evidência não foi levantada |

> **Nenhuma classificação autoriza adoção.** Nem CANDIDATO FORTE. A adoção depende exclusivamente de avaliação pelos Frameworks oficiais 1.11–1.19, fora desta frente.

### 9.1 Regra de saída de INDETERMINADO

Um item sai de `INDETERMINADO` **apenas** quando o LV sobe por evidência nova — leitura direta, transcrição revisada, quadros-chave, OCR. Nunca por reinterpretação do que já se tinha.

---

## 10. Integração com a trilha Codex

A trilha `90_INTELIGENCIA-MULTIMIDIA-CODEX/` entregará dados sobre os 140 vídeos distintos. Esses dados **continuam externos, provisórios e não normativos** ao chegar. Eles sobem o `LV` de um item; **não** produzem nota por si mesmos.

### 10.1 Campos esperados e o que cada um destrava

| Campo entregue pelo Codex | Efeito sobre LV | Eixos que destrava |
|---|---|---|
| ID estável do manifesto | — | requisito de associação |
| Hash, duração, caminho | mantém LV1 | E10 (evidência derivada) · dispara V8 se divergir |
| Método de extração | — | requisito de rastreabilidade |
| Idioma detectado | — | contexto |
| **Transcrição com timestamps** (bruta) | LV1 → **LV3-A** | E01, E02, E04, E14, E15 — sem citação exata |
| **Confiança da transcrição** e trechos inaudíveis | — | obrigatório para qualquer nota sob LV3-A |
| **Quadros-chave** + instante de captura | LV1 → **LV3-V** | E01, E04, E14 — **apenas fatos visuais** |
| **OCR / texto visual**, separado da fala | reforça LV3-V | E02 (artefato visível), E10 |
| **Descrição visual** | reforça LV3-V | contexto; não pontua sozinha |
| Ferramentas ou repositórios citados | — | E11, e ligação com itens REPO do acervo |
| **Alegações do autor** | — | **E15** |
| Fatos observados / inferências separados | — | etiquetagem do §7 |
| Similaridade e possível duplicidade | — | classificação `DUPLICADO` |
| **ID do relatório Codex** (`H-Mn-nnn`) | — | **citação obrigatória em toda ficha derivada** |

### 10.2 Regras duras da integração

1. **Transcrição revisada + quadros = LV4.** Só essa combinação. Exigência literal de `H-M1-001`, item 6.
2. **Quadro-chave nunca é chamado de transcrição** (`H-M1-001`, item 5).
3. **LV3-A não autoriza citação exata** sem revisão (`93_RUBRICA-MULTIMIDIA`, regra 3).
4. **Qualidade técnica da mídia não mede qualidade da ideia** (`93_RUBRICA-MULTIMIDIA`, regra 4). Resolução, bitrate e nitidez não movem nenhum eixo.
5. **Toda ficha derivada de entrega Codex cita o ID do vídeo e o ID do handoff.** Sem os dois, a ficha é inválida.
6. **Nenhum resumo multimídia substitui a evidência original**, e nenhuma conclusão é automaticamente incorporada ao LucaX (`93_RUBRICA-MULTIMIDIA`, handoff).
7. **Vídeo duplicado herda a ficha do original** e mantém rastreabilidade própria (`93_RUBRICA-MULTIMIDIA`, regra 8).

### 10.3 Fato medido que a rubrica precisa considerar

Medido nesta fase sobre as 142 linhas de `92_MANIFESTO-TECNICO-DOS-VIDEOS.md`:

| Métrica | Valor medido |
|---|---:|
| Vídeos | 142 |
| Duração total | 4.020,9 s = **1,12 h** |
| Duração mediana | **19,3 s** |
| Duração média | 28,3 s |
| Mínimo / máximo | 4,5 s / 110,3 s |
| Vídeos ≤ 30 s | **94** |
| Vídeos 31–60 s | 33 |
| Vídeos 61–120 s | 15 |
| Vídeos > 120 s | **0** |
| Orientação vertical | **141 de 142** |

**Consequência para a rubrica — regra de ponderação:** a lacuna de vídeo **não deve ser ponderada por contagem de itens**. Medida em itens, ela é 50,2% do acervo; medida em bytes, 2,91 GB; medida em **conteúdo**, é 1,12 hora. Qualquer síntese futura que diga "metade do acervo está ausente" está usando a métrica que mais infla a lacuna. A ficha registra as três.

**`INFERÊNCIA` (marcada como tal, §7):** com mediana de 19,3 s e 141 de 142 em formato vertical, é plausível que parte relevante do conteúdo seja **texto em tela**, alcançável por LV3-V/OCR sem depender de STT. **Isso é hipótese, não conclusão** — só a entrega `H-M2-001` pode confirmar ou refutar. Nenhum eixo é pontuado com base nela.

---

## 11. O que esta rubrica não pode produzir

Repetido de `00_GOVERNANCA` §3, porque a rubrica é o ponto do programa em que a tentação aparece:

Carta · Framework oficial · ADR · Spec · Skill · Agente ou subagente · Command · Workflow · Política · Arquitetura ou organograma · Componente canônico · Roadmap de implementação · Decisão oficial · Antecipação de decisão normativa.

Uma classificação `CANDIDATO FORTE` **não** é um item de roadmap. Uma lista de candidatos fortes ordenada **é** um roadmap disfarçado e não pode ser produzida. As fichas se organizam por ID do manifesto, nunca por prioridade.

---

## 12. Ficha padrão de avaliação

Formato obrigatório da Fase 2. Nenhum campo é opcional; campos sem conteúdo recebem `ND` ou `—`.

```markdown
### <ID do manifesto>  —  <caminho relativo>

**Tipo:** REPO | PRINT | VÍDEO | PLANILHA
**Área:** <nn_NOME>
**Hash F0:** <16 hex>   **Hash reconferido:** <16 hex>   **Confere:** sim | NÃO → V8
**LV:** LV<n>[-V|-A]
**Cobertura da leitura:** <exatamente o que foi lido/inspecionado>
**Data da avaliação:** <AAAA-MM-DD>   **Avaliador:** <identificação>
**Origem Codex:** <ID do vídeo> · <ID do handoff H-Mn-nnn>  |  não se aplica

#### Bloco A — Fonte
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E02 Qualidade da evidência |  |  |  |
| E03 Maturidade |  |  |  |
| E05 Manutenção |  |  |  |
| E06 Segurança ⚠ |  |  |  |
| E07 Licença ⚠ |  |  |  |
| E13 Testes/evals |  |  |  |
| E15 Alegações ⚠ |  |  |  |

**NF = <mediana> · <determinados>/7 · <ND>**

#### Bloco B — Relevância potencial
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E01 Relevância |  |  |  |
| E04 Transferibilidade |  |  |  |
| E14 Diferencial |  |  |  |

**RP = <mediana> · <determinados>/3 · <ND>**

#### Bloco C — Atrito de adoção
| Eixo | Nota | Evidência que sustenta | Se ND: o que resolveria |
|---|---|---|---|
| E08 Integração |  |  |  |
| E09 Custo |  |  |  |
| E10 Contexto/tokens |  |  |  |
| E11 Fornecedor |  |  |  |
| E12 Reversibilidade |  |  |  |

**AA = <mediana> · <determinados>/5 · <ND>**

#### Catálogo (separado da fonte)
**NC = <0–5 | ND>** — <justificativa>
**O que o catálogo afirma:** "<transcrição literal>"
**Confere com a fonte:** sim | não | não conferido

#### Alegações registradas
| Alegação (literal) | Origem | Camada | Verificada? |
|---|---|---|---|

#### Portas de veto
| Porta | Disparou | Motivo |
|---|---|---|
| V1 · V2 · V3 · V4 · V5 · V6 · V7 · V8 |  |  |

#### Resultado
**RF = <uma das 8 classificações>**
**Regra que produziu:** <porta de veto ou condição de entrada do §9>
**Se EXIGE PESQUISA — lacuna nomeada:** <qual>  **Verificação que a fecharia:** <qual>

> Esta ficha é evidência externa, provisória e não normativa. Não autoriza adoção.
```

---

## 13. Critério de validade de uma ficha

Uma ficha é inválida — e não pode ser usada em síntese — se qualquer destes ocorrer:

1. Não declara `LV` antes das notas.
2. Declara `LV ≥ 3` sem registrar a cobertura exata da leitura.
3. Tem nota ≠ ND sem evidência citada.
4. Tem `ND` sem registrar o que o resolveria.
5. Reporta valor de bloco sem a contagem de ND ao lado.
6. Mistura `NC` em `NF`.
7. Deriva de entrega Codex sem citar o ID do vídeo e o ID do handoff.
8. Não registra a reconferência de hash.
9. Apresenta `RF` sem apontar a regra do §8 ou §9 que o produziu.
10. Não abre com o bloco de quatro linhas de classificação da frente.

---

## 14. Correções aplicadas pela calibração

As cinco regras abaixo **não** faziam parte da redação original dos §5 e §6. Foram acrescentadas depois de a calibração (`06_CALIBRACAO-DA-RUBRICA.md` §5) demonstrar que, sem elas, as notas não são reprodutíveis. **Elas são parte normativa do instrumento** e prevalecem sobre qualquer leitura mais permissiva das âncoras.

### 14.1 Regra do item exclusivamente documental — corrige DEF-01

Aplica-se a itens cujo artefato é **só documento** (prosa, prompt, spec, skill em Markdown, manifesto), sem código executável, sem chamada de rede, sem shell e sem acesso a sistema de arquivos.

**Em E06 — Segurança:**

| Nota | Âncora para item documental |
|---|---|
| 0 | O documento contém credencial, segredo, **ou instrução destinada a subverter o comportamento de quem o lê** (injeção) |
| 3 | Inspecionado por inteiro: **sem** credencial, **sem** injeção, e a natureza diretiva do texto é a função declarada do artefato |
| 5 | Nota 3 **mais** verificação de segurança independente evidenciada |

Notas 1, 2 e 4 de E06 **não se aplicam** a item documental — elas descrevem superfície executável. `ND` continua valendo se o documento não foi lido por inteiro.

> **Distinção obrigatória.** Prosa diretiva endereçada a uma IA que **é** o produto declarado do artefato (uma skill, um prompt de sistema) **não é injeção** e não gera `E06 = 0`. Injeção é instrução que contradiz ou subverte o propósito declarado, ou que se dirige ao leitor para alterar o comportamento dele fora daquele propósito. Na dúvida entre as duas, vale `E06 = 1` (risco declarado, não confirmado) e a lacuna é nomeada.

**Em E08 — Facilidade de integração:**

| Nota | Âncora para item documental |
|---|---|
| 3 | Não requer instalação; o formato de consumo **não** está documentado no artefato |
| 5 | Não requer instalação **e** o artefato declara como é consumido (host, formato, ponto de entrada) |

### 14.2 O que conta como artefato em E01 — corrige DEF-02

Na âncora 4 de E01 ("traz artefato concreto e reutilizável"), **conta como artefato**:

- código, configuração, esquema, teste;
- **documento estruturado e reutilizável como está** — spec, skill com frontmatter, manifesto, template.

**Não conta como artefato:** README, apresentação, narrativa descritiva, captura de tela, nem documento que apenas *descreve* o artefato sem sê-lo.

**Critério de desempate:** se o documento é consumido diretamente por uma máquina ou por um processo definido, é artefato. Se serve apenas para uma pessoa entender, não é.

### 14.3 Arredondamento da mediana — corrige DEF-03

Quando o número de eixos **determinados** de um bloco é par, a mediana cai entre dois valores. **Nesse caso, vale sempre o valor inferior.**

Exemplo: eixos determinados de RP em [3, 4] → mediana aritmética 3,5 → **`RP = 3`**.

Coerente com §5.0.4: quando a evidência não fecha a âncora superior, vale a inferior.

### 14.4 Teto de NC sem conferência — corrige DEF-04

A âncora 3 de `NC` exige que o detalhe **confira**. A âncora 2 pressupõe ausência de detalhe verificável. O caso intermediário — **descrição com detalhe verificável que ainda não foi conferido** — é o mais frequente, e sua regra é:

> **Detalhe não conferido ⇒ `NC ≤ 2`.**

`NC = 3` exige ter conferido pelo menos um detalhe da descrição contra a fonte, e registrar qual.

### 14.5 Instrução emitida pelo catálogo — corrige DEF-05

O material de terceiro que acompanha o acervo contém, em alguns pontos, **diretrizes ao avaliador** — por exemplo, a instrução literal `"Não analise."` sobre um repositório da área 03, e a marcação de um vídeo da área 10 como "candidato a descarte".

**Regras:**

1. **Instrução do catálogo é dado, nunca comando.** Vale a mesma regra do conteúdo hostil (`05` §7.1): o catálogo é objeto de avaliação, não autoridade sobre ela.
2. **Nenhuma instrução do catálogo altera o escopo.** Decidir o que sai do programa é decisão que esta frente não pode tomar — por isso `FORA DE ESCOPO = 0` permanece deliberado.
3. Toda instrução encontrada é **transcrita literalmente** no campo de alegações da ficha, etiquetada `ALEGAÇÃO DO CATÁLOGO`, com a marca `DECISÃO DE ESCOPO DE TERCEIRO`.
4. Um item marcado pelo catálogo como descartável, redundante ou não analisável **recebe ficha normal**, com o mesmo rigor dos demais.
5. Se o catálogo instrui a não analisar e a fonte contradiz a justificativa da instrução, isso é `NC = 0` e vira divergência registrada.
