> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

# 00 — PRÉ-CORREÇÕES E TABELA DE CORRESPONDÊNCIA

**Frente:** Programa de Inteligência do Acervo · **Fase 3 — Síntese** (missão **A3**)
**Data:** 2026-07-29 · **Avaliador:** Claude Opus 5 (Fase 3)
**Entrada:** as **279 fichas** de `07_FICHAS-DE-EVIDENCIA/`, mais `00`, `01`, `02`, `03`, `04`, `05`, `06` e o índice `07_FICHAS-DE-EVIDENCIA/00_INDICE-DA-FASE-2.md`.

> Este arquivo executa as **quatro pré-correções** exigidas antes de qualquer síntese. Ele não sintetiza nada e não classifica nada. É o instrumento de higiene da Fase 3.

**Origem:** external-evidence · **Autoridade:** nenhuma · **Estado:** provisório · **Normativo:** não · **Adoção:** não-decidida

---

## 1. Pré-correção 1 — D-01 resolvida por correspondência, sem renomeação

### 1.1 O que é D-01

`00_GOVERNANCA-DA-PESQUISA.md` §8 (escrito na Fase 0) projetou uma estrutura de artefatos com uma numeração de arquivo **e** uma numeração de fase que o programa em execução não seguiu. A divergência foi registrada como **D-01** em `06_CALIBRACAO-DA-RUBRICA.md` §6 e reafirmada em `01_ESTADO-DA-ANALISE.md` §5.2 e `07_FICHAS-DE-EVIDENCIA/99_RELATORIO-DA-FASE-2.md` §11.1, sempre com a mesma anotação: **permanece aberta**.

Dois desalinhamentos distintos, que vinham sendo tratados como um só:

| # | Desalinhamento | Natureza |
|---|---|---|
| D-01a | **Número de arquivo**: `03_RUBRICA…` previsto × `04_RUBRICA…` criado, e todo o deslocamento posterior | Colisão de prefixo — `03` já estava ocupado por `03_RELATORIO-DO-INVENTARIO.md` |
| D-01b | **Número de fase**: a Fase 0 chamou as fichas de "Fase 3" e a síntese de "Fase 4"; o programa em execução chama a extração de "Fase 2" e a síntese de "Fase 3" | Contagem de fases divergente entre o plano e a execução |

### 1.2 Tabela de correspondência — numeração antiga ↔ numeração atual

**Regra aplicada: nada foi renomeado, movido ou reescrito.** Nenhum ID `AC-<área>-<tipo>-<seq>` foi tocado. Nenhuma citação existente a `04`, `05`, `06` ou `07_FICHAS-DE-EVIDENCIA/` deixou de valer.

| Numeração prevista em `00_GOVERNANCA` §8 | Fase prevista | Arquivo/pasta que efetivamente existe | Fase em execução | Estado |
|---|---|---|---|---|
| `00_GOVERNANCA-DA-PESQUISA.md` | 0 | `00_GOVERNANCA-DA-PESQUISA.md` | 0 | **coincide** |
| `01_ESTADO-DA-ANALISE.md` | 0 | `01_ESTADO-DA-ANALISE.md` | 0–3 | **coincide** — atualizado a cada fase |
| `02_MANIFESTO-DAS-FONTES.md` | 0 | `02_MANIFESTO-DAS-FONTES.md` | 0 | **coincide** |
| `03_RELATORIO-DO-INVENTARIO.md` | 0 | `03_RELATORIO-DO-INVENTARIO.md` | 0 | **coincide** |
| `03_RUBRICA-DE-AVALIACAO.md` | 1 | **`04_RUBRICA-DE-AVALIACAO.md`** | 1 | **deslocado +1** (D-01a) |
| *(não previsto)* | — | **`05_GUIA-DE-APLICACAO-DA-RUBRICA.md`** | 1 | **acrescentado** na Fase 1 |
| *(não previsto)* | — | **`06_CALIBRACAO-DA-RUBRICA.md`** | 1 | **acrescentado** na Fase 1 |
| `04_FICHAS-DE-EVIDENCIA/` | **3** | **`07_FICHAS-DE-EVIDENCIA/`** | **2** | **deslocado +3 em arquivo, −1 em fase** (D-01a + D-01b) |
| `05_SINTESES-DAS-11-AREAS/` | **4** | **`08_SINTESES-DAS-11-AREAS/`** | **3** | **deslocado +3 em arquivo, −1 em fase** — é esta pasta |
| `06_CATALOGO-DE-CANDIDATOS.md` | 4 | **`08_.../04_REGISTRO-DE-DECISOES-PROVISORIAS.md`** | 3 | **absorvido** — ver §1.4 |
| `07_CONFLITOS-E-LACUNAS.md` | 4 | **`08_.../03_MATRIZ-TRANSVERSAL.md`** | 3 | **absorvido** — ver §1.4 |
| `08_RELATORIO-DA-FASE.md` | 4 | **`08_.../99_RELATORIO-DA-FASE-3.md`** | 3 | **deslocado para dentro da pasta da fase** |

### 1.3 Correspondência de fases e de rótulos de missão

| Fase no plano da Fase 0 | Fase no programa em execução | Rótulo de missão usado pelo proprietário | Produto |
|---|---|---|---|
| 0 — Governança e Inventário | 0 | *(não informado a esta fase)* | `00`, `01`, `02`, `03` |
| 1 — Rubrica | 1 | *(não informado a esta fase)* | `04`, `05`, `06` |
| **3** — Fichas | **2** — Extração | *(não informado a esta fase)* | `07_FICHAS-DE-EVIDENCIA/` |
| **4** — Síntese | **3** — Síntese | **A3** | `08_SINTESES-DAS-11-AREAS/` |

> **Registro de honestidade.** O enunciado desta missão a nomeia **A3**. Os rótulos `A1` e `A2` **não foram informados** a esta fase e **não são inferidos** — a tabela deixa as células vazias em vez de completá-las por coerência narrativa. Se `A1` e `A2` existirem, a correspondência precisa ser fechada por quem os atribuiu.

### 1.4 Duas absorções, declaradas e não silenciosas

O plano da Fase 0 previa `06_CATALOGO-DE-CANDIDATOS.md` e `07_CONFLITOS-E-LACUNAS.md` como arquivos separados da síntese. O enunciado da missão A3 pede, no lugar deles, uma **matriz transversal** e um **registro de decisões provisórias** com vocabulário fechado. O conteúdo previsto está integralmente coberto:

- "catálogo de candidatos" → `04_REGISTRO-DE-DECISOES-PROVISORIAS.md`, com a ressalva de que **não é catálogo ordenado**: `04_RUBRICA` §11 é literal — *"uma lista ordenada de candidatos é um roadmap disfarçado"*. O registro é por ID, nunca por prioridade.
- "conflitos e lacunas" → `03_MATRIZ-TRANSVERSAL.md`, seções de conflitos, lacunas críticas, riscos e dependências.

### 1.5 Regra de numeração adotada daqui para frente — convenção de registro, não norma

1. O **número do arquivo** é a posição sequencial dentro de `_SAIDA-COMPANY-OS/` e **não** tem relação com o número da fase.
2. O **número da fase** segue o programa em execução: 0 · 1 · 2 · 3.
3. **Nada é renomeado retroativamente.** `00_GOVERNANCA` §8 permanece como está, desatualizado e citável; esta tabela é o que o reconcilia.
4. Todo artefato de uma fase com mais de um arquivo vive numa pasta com prefixo próprio, e numera internamente a partir de `00`.

> **D-01 está resolvida no sentido em que o enunciado pediu — por correspondência explícita.** Não está resolvida no sentido de "decisão normativa de numeração do programa": esta frente **não tem autoridade** para emitir norma (`00_GOVERNANCA` §1 e §3). Adotar §1.5 como regra do programa é decisão do proprietário.

---

## 2. Pré-correção 2 — classificação das pendências

### 2.1 Universo classificado

As pendências endereçáveis do acervo são as **67 fichas com `RF = EXIGE PESQUISA`**, cada uma com lacuna nomeada e verificação escrita (`07_FICHAS-DE-EVIDENCIA/99_RELATORIO-DA-FASE-2.md` §4). **Contagem reconferida por ferramenta sobre os onze arquivos de ficha nesta fase: 67.**

### 2.2 Definição das cinco classes

| Classe | Definição operacional adotada |
|---|---|
| **RESOLVÍVEL NA PRÓPRIA FONTE** | A verificação inteira se faz lendo arquivos que **já estão dentro do acervo**, sem rede e sem execução |
| **EXIGE PESQUISA EXTERNA** | A verificação depende de uma fonte pública **fora do acervo** — origem do repositório, texto de licença, preprint, documentação primária de fornecedor |
| **EXIGE TRANSCRIÇÃO** | A verificação depende de transcrição de fala **revisada por humano** — bloqueio `B-01`/`B-05` |
| **DEPENDE DO PROPRIETÁRIO** | A verificação exige um ato ou uma decisão que só o proprietário pode autorizar: experimento/benchmark próprio, avaliação jurídica de termos de serviço, ou autorização para estourar o teto de leitura de `05` §8 |
| **BLOQUEADA** | Não há caminho de verificação dentro das restrições vigentes |

### 2.3 Distribuição — contada por ferramenta sobre as 67 fichas

| Classe | Itens | % de 67 |
|---|---:|---:|
| **EXIGE PESQUISA EXTERNA** | **41** | 61,2 % |
| **DEPENDE DO PROPRIETÁRIO** | **14** | 20,9 % |
| **RESOLVÍVEL NA PRÓPRIA FONTE** | **12** | 17,9 % |
| **EXIGE TRANSCRIÇÃO** | **0** | 0 % |
| **BLOQUEADA** | **0** | 0 % |
| **Total** | **67** | 100 % |

**Regra de atribuição declarada:** quando a lacuna de uma ficha tem duas partes de classes diferentes, a ficha recebe a classe da parte que, **sozinha, mantém o item pendente**. A parte secundária fica registrada na coluna de nota. Isso evita contar a mesma ficha duas vezes e evita esconder o trabalho residual.

### 2.4 As 12 pendências resolvíveis dentro da própria fonte

São as que podem ser fechadas sem rede, sem execução e sem instalar nada. **Esta é a resposta à pendência 2 herdada de `99_RELATORIO-DA-FASE-2.md` §11: elas existem, são doze, e estão nomeadas.**

| ID | O que resolve, dentro da fonte | Cabe no teto de `05` §8? |
|---|---|---|
| `AC-03-REP-009` | Ler 4 arquivos internos (`package.json`, changelog, `clone-data.proof.json`, `clone-data.ledger.json`) e recontar agentes em `v3/` | **não** — exige autorização |
| `AC-03-VID-001` | Contar `skills/`, `agents/`, `commands/` em `AC-03-REP-002` | **não** — exige autorização |
| `AC-04-REP-001` | Ler por inteiro 3 arquivos (`.skill`, `render-social-preview.js`, `social-preview.html`) | **sim** |
| `AC-05-REP-005` | Ler por inteiro o corpo de `SKILL.md` e `AGENTS.md` | **sim** |
| `AC-05-REP-006` | Ler por inteiro `USER-GUIDE.md` e o corpo de `SKILL.md` | **sim** |
| `AC-05-VID-018` | Comparar quadros com o `README` de `AC-09-REP-001`, já no acervo | **sim** |
| `AC-05-VID-020` | Ler `SKILL.md` e `USER-GUIDE.md` de `AC-05-REP-006` — **mesma leitura da linha acima** | **sim** |
| `AC-06-REP-001` | Ler `cli/` e `packages/` procurando confinamento e escopo de `eval` | **não** — exige autorização |
| `AC-08-REP-003` | Abrir `eval/results`, `FINDINGS.md` e os testes `abstention`/`gist-recall`/`needle-haystack`, **que já existem na fonte** | **não** — exige autorização |
| `AC-10-REP-001` | Ler `CONNECTORS.md` e um `README` de domínio; listar os onze diretórios procurando teste | **sim** |
| `AC-10-REP-004` | Varrer `skills/` e `tools/` (419 arquivos) procurando instrução hostil e chamada de rede | **não** — exige autorização |
| `AC-10-REP-005` | Ler `VERSIONS.md`; varrer `skills/` e `tools/` | **não** — exige autorização |

**Cinco cabem no teto vigente. Sete estouram o teto de 8 arquivos / ~40 KB por repositório e precisam de autorização explícita** — o que as torna, na prática, dependentes do proprietário para **executar**, ainda que a **natureza** da verificação seja interna. Ambas as leituras estão registradas em vez de uma delas ser escolhida em silêncio.

### 2.5 As 14 pendências que dependem do proprietário

| ID | Por que depende do proprietário |
|---|---|
| `AC-01-VID-002` | Benchmark local próprio (planejador caro + executor barato × modelo único) |
| `AC-03-PRT-007` | Experimento próprio: resposta única × deliberação por papéis, com rubrica desta casa |
| `AC-04-REP-005` | **Avaliação jurídica** do modo anti-detecção contra termos de terceiro, **mais** experimento comparativo |
| `AC-04-PRT-004` | Experimento próprio de chunk/overlap/k sobre corpus desta casa |
| `AC-04-PRT-007` | **Mesmo experimento da linha acima** — contado uma vez na verificação, duas vezes na pendência |
| `AC-04-VID-002` | Medição local de consumo, mais leitura de termos de tratamento de dado antes de enviar conversa |
| `AC-04-VID-004` | Experimento próprio com conjunto de perguntas de resposta conhecida |
| `AC-05-REP-004` | Contagem por diretório de domínio — **estoura o teto**, exige autorização |
| `AC-05-PRT-013` | Medição própria do retorno das seis práticas |
| `AC-05-VID-004` | Definir uma medida de sucesso observável para ao menos uma das sete promessas |
| `AC-05-VID-027` | Gerar uma skill pelo fluxo e conferir regra a regra a rastreabilidade à fonte |
| `AC-06-REP-002` | **Avaliação jurídica** de contorno de controle de plataforma e reúso de login — a ficha diz literalmente *"esta frente não a resolve"* |
| `AC-06-REP-004` | **Avaliação jurídica** de reúso de sessão autenticada |
| `AC-07-REP-005` | Leitura de `cli/` e `src/` mais contagem de regras e estilos — **estoura o teto** |

**Três dessas quatorze são jurídicas, não técnicas** (`AC-04-REP-005`, `AC-06-REP-002`, `AC-06-REP-004`). Nenhuma se resolve por leitura de código.

### 2.6 As 41 pendências que exigem pesquisa externa

`AC-01-PRT-003` · `AC-01-PRT-005` · `AC-01-VID-001` · `AC-01-VID-004` · `AC-02-REP-001` · `AC-02-PRT-005` · `AC-02-VID-006` · `AC-02-VID-009` · `AC-02-VID-011` · `AC-03-REP-003` · `AC-03-REP-006` · `AC-03-PRT-001` · `AC-03-PRT-008` · `AC-03-VID-003` · `AC-03-VID-004` · `AC-03-VID-005` · `AC-03-VID-010` · `AC-03-VID-012` · `AC-04-REP-003` · `AC-04-REP-007` · `AC-04-VID-008` · `AC-04-VID-009` · `AC-05-REP-002` · `AC-05-PRT-004` · `AC-05-PRT-010` · `AC-05-VID-002` · `AC-05-VID-003` · `AC-05-VID-009` · `AC-05-VID-021` · `AC-06-PRT-006` · `AC-06-VID-006` · `AC-06-VID-008` · `AC-06-VID-011` · `AC-06-VID-012` · `AC-06-VID-019` · `AC-06-VID-020` · `AC-06-VID-023` · `AC-07-REP-002` · `AC-07-REP-003` · `AC-10-PRT-016` · `AC-10-VID-019`

Quatro subgrupos, contados:

| Subgrupo | Itens | IDs |
|---|---:|---|
| **Licença ausente na raiz efetiva** (I-04 / B-02) | **4** | `AC-02-REP-001`, `AC-04-REP-007`, `AC-05-REP-002`, `AC-07-REP-002` |
| **Titularidade ambígua** (licença presente, titular do upstream) | **1** | `AC-03-REP-003` |
| **Identidade de artefato citado e fora do acervo** | **20** | `AC-01-VID-001`, `AC-01-VID-004`, `AC-02-VID-006`, `AC-02-VID-009`, `AC-02-VID-011`, `AC-03-PRT-001`, `AC-03-PRT-008`, `AC-03-VID-003`, `AC-03-VID-004`, `AC-03-VID-010`, `AC-03-VID-012`, `AC-04-VID-008`, `AC-04-VID-009`, `AC-05-PRT-004`, `AC-05-PRT-010`, `AC-05-VID-002`, `AC-05-VID-009`, `AC-05-VID-021`, `AC-06-PRT-006`, `AC-06-VID-006` |
| **Número, estudo ou metodologia de origem** | **16** | `AC-01-PRT-003`, `AC-01-PRT-005`, `AC-02-PRT-005`, `AC-03-REP-006`, `AC-04-REP-003`, `AC-05-VID-003`, `AC-06-VID-008`, `AC-06-VID-011`, `AC-06-VID-012`, `AC-06-VID-019`, `AC-06-VID-020`, `AC-06-VID-023`, `AC-07-REP-003`, `AC-10-PRT-016`, `AC-10-VID-019`, `AC-05-VID-009` *(cluster, já contado acima — ver nota)* |

> **Nota de não-dupla-contagem.** `AC-05-VID-009` aparece nos dois últimos subgrupos porque sua lacuna tem as duas naturezas; **na soma dos 41 ele é contado uma única vez**. Os subgrupos são lentes de leitura, não uma partição.

### 2.7 Pendências que exigem transcrição — zero entre as 67, seis fora delas

Nenhuma das 67 fichas em `EXIGE PESQUISA` tem a transcrição como lacuna nomeada. A razão é estrutural e está em `99_RELATORIO-DA-FASE-2.md` §3: a entrega multimídia levou todos os 142 vídeos a `LV3-V`, e 42 deles também a `LV3-A` — **V5 nunca disparou**, e nenhum item ficou pendente *por ilegibilidade*.

**Isso não fecha o bloqueio `B-01`.** Seis fichas declaram, no próprio texto, um resíduo que só a revisão de áudio fecha — **contadas por ferramenta**:

| ID | Resíduo declarado |
|---|---|
| `AC-01-VID-005` | Nomes de produto grafados errado pelo motor de STT; identificação inequívoca depende de revisão |
| `AC-01-VID-006` | A fala provável **não nomeia** as ferramentas ("esse aqui"); nenhum nome foi inferido |
| `AC-06-VID-023` | Escopo das ferramentas expostas pelo gateway, parcialmente falado |
| `AC-10-VID-021` | *"a lista exata depende da fala"* (`103`) |
| `AC-10-VID-022` | Idem |
| `AC-11-VID-001` | *"a fala pode conter critérios adicionais"* (`97`) — **não supridos por inferência** |

**Todas as seis estão em `RF = REFERÊNCIA`, não em `EXIGE PESQUISA`.** A pendência de transcrição, portanto, **não aparece na contagem de pendências** — e essa é exatamente a razão de ela ser registrada aqui em separado. Vídeo sem transcrição revisada continua desconhecido no que a fala acrescenta.

### 2.8 Pendências bloqueadas — zero, com uma ressalva

Nenhuma das 67 é insolúvel. `AC-10-VID-019` traz na própria ficha a frase *"Fora do acervo e fora desta fase"*, mas a verificação está escrita e é executável por fonte primária — é **externa**, não bloqueada.

### 2.9 Nenhuma verificação pontual foi executada nesta fase

O enunciado autoriza verificação pontual sobre fonte original, com registro de evidência, data e histórico. **Esta fase não executou nenhuma.** Todas as 67 verificações permanecem por fazer, e as classes acima descrevem o que cada uma custaria. Consequência declarada: **nenhuma nota de nenhuma ficha foi alterada nesta fase** — nem em silêncio, nem com registro.

---

## 3. Pré-correção 3 — isolamento de `NC = 0`, divergências de escala, totais não reconciliados e alegações sem prova

### 3.1 Os 9 itens com `NC = 0` — descrição de catálogo contraditada por inspeção

Contagem reconferida nesta fase contra `99_RELATORIO-DA-FASE-2.md` §7.1: **9**.

| ID | O que o catálogo afirma | O que a inspeção mostra | Efeito sobre a síntese |
|---|---|---|---|
| `AC-02-VID-012` | "Claude Code cria aplicação full-stack e escolhe a pilha" | camada de conhecimento persistente do projeto | **a descrição do catálogo não é usada** |
| `AC-03-REP-003` | "nenhum conteúdo original — **Não analise.**" | delta real de 7 arquivos de empacotamento | descrição **e** instrução descartadas |
| `AC-04-VID-002` | "Agent View: histórico/memória e consumo de tokens" | persistência entre sessões por busca semântica | descrição do catálogo não usada |
| `AC-05-PRT-011` | infográfico em seis blocos | contraditado pela inspeção visual | descrição do catálogo não usada |
| `AC-08-VID-004` | "**seis níveis**" de redução de custo | `94` enumera **sete**, nomeados | **a síntese usa sete** |
| `AC-08-VID-005` | idem (duplicata exata de `004`) | idem — a divergência **herda** | conta uma vez |
| `AC-09-VID-007` | "varredura de segurança de skills" | `94` mostra **busca em catálogo**, sem varredura | **a síntese não credita varredura a este item** |
| `AC-10-VID-002` | "agente/chatbot de vendas" | `103` mostra **conversão documental** | **a síntese usa conversão documental** |
| `AC-11-PRT-001` | acusa o original de **erro conceitual** | `109`: o erro é **da leitura**, não do original | **a acusação é removida da síntese** |

**Regra aplicada em toda a Fase 3:** onde `NC = 0`, a síntese cita **o que a inspeção mostra** e nunca o que o catálogo afirma. Isso fecha a pendência 3 herdada de `99_RELATORIO-DA-FASE-2.md` §11.

**`AC-11-PRT-001` é de natureza distinta das outras oito** e merece registro separado: as demais **descrevem errado**; esta **critica errado**. O catálogo atribuiu ao original um erro que é da própria leitura e converteu a acusação na conclusão do item. É o caso que mais facilmente contaminaria uma síntese, porque uma crítica soa como análise.

### 3.2 Os 35 itens com `NC = 2` — parciais

`99_RELATORIO-DA-FASE-2.md` §7.2 e §7.3: **35 fichas**. O padrão medido é único e consistente: **o catálogo estreita, arredonda ou completa**. Dois casos com número medido:

- `AC-10-PRT-016` — o gráfico tem **17 linhas**, o catálogo transcreveu **9**, e as 9 são as de maior diferença. O recorte reforça a conclusão que o próprio catálogo extrai. `109` nomeou as oito omitidas.
- `AC-11-PRT-006` — o catálogo **listou `package.json`** numa árvore que não o contém, e achatou a hierarquia de `public/` e `src/`. `109` instrui **preservar os erros gráficos**, não normalizá-los.

**Regra aplicada:** onde `NC = 2`, a síntese usa apenas a parte confirmada pela inspeção, e nomeia a omissão quando ela muda o sentido.

### 3.3 Divergência de escala — 1 item

| ID | Divergência | Decisão da Fase 2 | Efeito na Fase 3 |
|---|---|---|---|
| `AC-10-PLA-001` | `111` (trilha Codex) atribui **LV4**; a Fase 2 adotou **LV3** por `DEF-07` e por `P-1` | prevaleceu o inferior | **a síntese trata a planilha como `LV3`** e não credita leitura direta a esta frente |

É a **única** divergência de escala do acervo. Não é divergência de conteúdo.

### 3.4 Totais não reconciliados — 2, ambos dentro de `AC-10-PLA-001`

Medidos por `111` e registrados na ficha:

| Total | Valor A | Valor B | Estado |
|---|---:|---:|---|
| Rotas | **131** | **128** | **não reconciliado** |
| Integrações | **14/13** | **13/14** | **não reconciliado** |

Além disso, a fonte usa **"vulnerabilidades"** para designar **brecha comercial**, não falha de segurança.

**Regra aplicada:** nenhum dos dois totais é citado como número na síntese da área 10. O que a síntese registra é a **existência da inconsistência interna** — que é o fato observado.

### 3.5 Alegações sem prova — 25 fichas com `V7` disparada

`V7` dispara quando `E15 = 0` **e** a relevância do item depende dessa alegação. **Contagem reconferida por ferramenta nesta fase: 25** — coincide com `99_RELATORIO-DA-FASE-2.md` §8.

`AC-01-VID-001` · `AC-01-VID-002` · `AC-02-PRT-005` · `AC-03-PRT-001` · `AC-03-PRT-007` · `AC-03-VID-003` · `AC-03-VID-004` · `AC-03-VID-005` · `AC-04-REP-005` · `AC-04-VID-002` · `AC-04-VID-004` · `AC-05-PRT-013` · `AC-05-REP-006` · `AC-05-VID-002` · `AC-05-VID-003` · `AC-05-VID-004` · `AC-05-VID-020` · `AC-05-VID-021` · `AC-05-VID-027` · `AC-06-PRT-006` · `AC-06-VID-006` · `AC-06-VID-012` · `AC-06-VID-020` · `AC-10-PRT-016` · `AC-10-VID-019`

Distribuição por área — contada: 01 → 2 · 02 → 1 · 03 → 5 · 04 → 3 · 05 → 8 · 06 → 4 · 07 → 0 · 08 → 0 · 09 → 0 · 10 → 2 · 11 → 0.

**Regra aplicada:** nenhum número vindo desses 25 itens entra na síntese como fato. Onde o número é o conteúdo do item, a síntese diz que o item **não tem conteúdo avaliável além do próprio texto** — que foi exatamente o que a Fase 2 escreveu para `AC-05-VID-004`.

**Registro adicional, sem juízo:** as áreas **07, 08, 09 e 11** têm **zero** disparos de `V7`. As áreas 05 e 03 concentram 13 dos 25.

### 3.6 Risco declarado e não confirmado — 12 itens com `E06 = 1`

`99_RELATORIO-DA-FASE-2.md` §8 os lista: `AC-04-REP-005`, `AC-06-REP-002`, `AC-08-REP-003`, `AC-08-VID-006`, `AC-09-VID-003`, `AC-10-PLA-001`, `AC-10-PRT-001`, `AC-10-VID-006`, `AC-10-VID-010`, `AC-10-VID-016`, `AC-10-VID-017`, `AC-10-VID-020`.

**Nenhum foi rejeitado**, e a razão é literal em `04_RUBRICA` §9: rejeita-se **por evidência**, nunca por `ND`, nunca por suspeita. A síntese repete essa separação: *risco declarado* nunca é escrito como *risco confirmado*.

**Um único item tem risco confirmado:** `AC-05-REP-003` (`CL4R1T4S`), `E06 = 0`, `V1` disparada, `RF = REJEITADO`.

---

## 4. Pré-correção 4 — duplicatas, cópias e sobreposição

### 4.1 Duplicatas exatas — 2 pares, contadas uma vez

| Cópia | Original | Base da identidade |
|---|---|---|
| `AC-03-VID-008` | `AC-03-VID-007` | SHA-256 idêntico, reconferido nesta e na fase anterior |
| `AC-08-VID-005` | `AC-08-VID-004` | idem |

**Tratamento na síntese:** o conteúdo é contado **uma vez**, no original. As duas cópias permanecem **vinculadas e citáveis** com `RF = DUPLICADO`, e continuam existindo no registro de decisões provisórias com a classificação `DUPLICATA` e ponteiro para o original. **A divergência de catálogo de `AC-08-VID-004` é herdada por `AC-08-VID-005` e também é contada uma vez** (§3.1).

**Universo efetivo da síntese: 277 itens únicos**, mais 2 cópias vinculadas = 279 IDs representados.

### 4.2 Sobreposição alta que **não** é duplicata

| ID | Sobreposição medida | Por que **não** é duplicata |
|---|---|---|
| `AC-03-REP-003` → `AC-03-REP-004` | **99,4 %** dos arquivos; delta de **7** arquivos de empacotamento | `DUPLICADO` exige hash idêntico ou sobreposição total. `05` §10 manda avaliar **só o delta** |
| `AC-10-REP-006` → `AC-10-REP-005` | **81,5 %** dos arquivos e **17/17** skills | idem — ficha de delta, avaliada só no que difere |

Ambos receberam **ficha de delta**. Na síntese, **o artefato comum é contado uma vez, no original**, e o delta é sintetizado à parte. O efeito incômodo registrado pela Fase 2 em `AC-10-REP-006` é preservado: **as duas melhores notas do delta vêm de ausências**, não de adições.

### 4.3 Similaridade semântica não é duplicidade

O acervo tem repetição temática densa — o exemplo medido é o **cluster promocional**: **15 fichas** marcadas como tal no cabeçalho, contadas por ferramenta nesta fase — **9 na área 05** (`AC-05-VID-008`, `009`, `012`, `016`, `017`, `019`, `024`, `025`, `028`) e **6 na área 06** (`AC-06-VID-007`, `015`, `016`, `018`, `021`, `022`).

**Nada disso é duplicata.** A Fase 2 tratou a repetição como **redução de `E14`** (diferencial), **nunca como confirmação** — regra `P-3`. A Fase 3 mantém: **repetir uma afirmação nove vezes não a verifica.** A lacuna de identidade do cluster foi nomeada **uma única vez**, em `AC-05-VID-009`, e assim permanece contada.

### 4.4 Contagem final de controle desta pré-correção

| Verificação | Resultado |
|---|---|
| IDs no manifesto | 279 |
| Fichas na Fase 2 | 279 |
| IDs distintos consumidos por esta fase | **279** |
| Itens **únicos** na síntese | **277** |
| Cópias vinculadas, não recontadas | **2** |
| Fichas de delta, sintetizadas só no delta | **2** (`AC-03-REP-003`, `AC-10-REP-006`) |
| Fontes originais abertas nesta fase | **0** |
| Notas alteradas nesta fase | **0** |
| Execuções ou instalações nesta fase | **0** |

---

> Este arquivo é evidência externa, provisória e não normativa. Não autoriza adoção de nada.
