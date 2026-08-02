---
id: ADR-0022-sede-canonica-do-framework-de-specifications
titulo: Emenda C3 que cria FND-11 — o Framework de Specifications passa a ter sede fundacional, e SF-01 a SF-32 migram sem alteracao silenciosa de merito
tipo: adr
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-07-29
atualizado_em: 2026-07-29
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0006, ADR-0008, ADR-0009, ADR-0012, ADR-0018, ADR-0019, ADR-0020, ADR-0021]
substitui: []
substituido_por: null
classe_mudanca: C3
tipo_decisao: 1
supera: [ADR-0021]
superado_por: null
resumo: Cria FND-11 como sede fundacional de SF-01 a SF-32, emenda FND-01 §10 e §11 e FND-03 §7, e declara regra por regra a origem, a transformacao e a equivalencia — 30 identicas, 1 referencial e 1 com merito declarado.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: ratificada
---

# ADR-0022: A sede canonica do Framework de Specifications e `FND-11`

> ## O estado deste ADR e o do seu frontmatter, e nada alem dele
>
> **A fonte corrente do estado e o campo `ratificacao`** (FND-10 §5.4). Enquanto ele disser
> `pendente`, este ADR **nao produz efeito**: `FND-11` **nao existe no acervo**, `FND-01`
> permanece em **1.5.0**, `FND-03` em **1.5.0**, e a norma da `Spec` continua vivendo
> **integralmente** em [ADR-0021](ADR-0021-framework-de-specifications.md), **vigente e
> intacto**. **Nenhuma frase deste texto afirma vigencia** — a licao de **RD-08**, aplicada.
>
> **`supera: [ADR-0021]` e sucessao PARCIAL, e o alcance esta em §5.4.** `ADR-0021` **nao** e
> substituido, **nao** muda de `status` e **nao** e editado.

## Proposito

Mover a norma da `Spec` para a sede que a propria `FND-10 §4.1` reserva a ela — a forma
documental **Framework**, entidade `FND` — **sem alterar silenciosamente o merito de nenhuma das
32 regras**, e declarando, regra por regra, **origem, transformacao e equivalencia**.

## Escopo

| Item | Definicao |
|---|---|
| Inclui | **Um artefato novo** — `FND-11`, **399 linhas** · **quatro** alteracoes em `FND-01` *(§10, §11, tabela de documentos derivados, historico)* · **duas** em `FND-03` *(§7, historico)* · a **sucessao parcial** de `ADR-0021` quanto a sede |
| **Nao** inclui | O **merito** de `SF-01` a `SF-31` · o **vinculo `Spec` × `Produto`**, a **sequencia por Produto** e os **locais canonicos** — `RD-33`, **nao reaberto** · `FND-04`, `FND-09`, `FND-10`, `TPL-spec` — **`0` bytes** · a criacao de `Spec`, `Produto`, `Projeto`, `Skill`, `Tool`, `Command`, `Workflow` ou `Agente` · a **edicao de `ADR-0021`** *(M1, CC-01, LV-04)* · `RD-27`, `RD-36` · a propagacao de `QG-1` nas Cartas — [ADR-0023](ADR-0023-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md), **pacote separado** |
| Origem | [RFC-0018](../rfcs/RFC-0018-sede-canonica-do-framework-de-specifications.md) |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| Propoe | **DEP-GOV** | [FND-09 §8.2](../foundation/09-meta-model.md), linha `FND` — **proponente unico**; nao e escolha |
| Materia | **DEP-PRD** | Dono do tipo `SPC`; **autor do merito** em `ADR-0021`. **Consulta obrigatoria** |
| Revisor independente | **DEP-QAR** | FND-09 §8.2, linha `FND` — *revisa*; `RM-06b` |
| Aprova e **ratifica** | **SOBERANO** | **C3.** Indelegavel (FND-04 §2; FND-09 §8.2) |

> **Residuo declarado (`PI-10`), e e uma regressao medida.** `ADR-0021` foi o **primeiro**
> instrumento normativo do acervo cujo autor nao e DEP-GOV — a resposta material a **`RC-02`**.
> **Promover a norma a `FND` devolve a autoria a DEP-GOV por determinacao da matriz**, nao por
> conveniencia: `FND-09 §8.2` nomeia **um unico** proponente para `FND`. Achado **`RD-39`**,
> familia `RC-02`, **oitava ocorrencia**. Mitigacao real e insuficiente: **o merito nao e
> escrito aqui — e recebido**, e §5.2 prova isso por `diff`.

---

## 1. Contexto

`ADR-0021` instituiu `SF-01` a `SF-32` **dentro do proprio ADR** e declarou, em §6, que
**`FND-11` seria a sede melhor** e estava fora de alcance naquela missao — porque exigia `C3` e
emenda a `FND-01 §10`, e a Missao 1.13 tinha **`0` fontes de `foundation/` autorizadas**.

**A Missao 1.13.1 autoriza o que a 1.13 nao podia fazer.** O que nao mudou: as **32** regras
continuam **determinadas e nao observadas** *(`0` Specs — ressalva `R1` de
[FIT-2026-015](../governance/fitness/FIT-2026-015-framework-de-specifications.md))*, e o
**vinculo `Spec` × `Produto`** continua **integralmente vigente**.

**Estado do mundo antes desta decisao, medido:** `169` artefatos · `48.764` linhas ·
`BL-2026-07-29-09`; **`0` Specs**, **`0` Produtos**; `foundation/` com **10** documentos;
`ADR-0021` **`ativo`**.

## 2. Problema / Pergunta de decisao

**A norma de um dominio inteiro deve viver em artefato `M1`, que nunca se emenda, ou na forma
documental que o proprio acervo reserva a esse papel?**

E o corolario que a promocao impoe: **como mover 32 regras sem que nenhuma mude de sentido no
caminho, e como provar isso?**

## 3. Criterios de decisao

`K1` a `K8` de [RFC-0018 §3](../rfcs/RFC-0018-sede-canonica-do-framework-de-specifications.md),
declarados **antes** das opcoes e **nao reproduzidos aqui** (`PJ-01`).

## 4. Alternativas consideradas

**Quatro opcoes e a opcao Z**, com criterios, custo e afetados, em
[RFC-0018 §4](../rfcs/RFC-0018-sede-canonica-do-framework-de-specifications.md) — **`A` `FND-11`**
*(escolhida)* · **`B` secao em `FND-10`** · **`C` manter no ADR** · **`D` `FND-11` sem inscrever
na hierarquia** · **`Z` decidir depois da primeira `Spec`**. **Este ADR nao as reproduz**
(`PJ-01`, `CM-09`).

**Por que `A`.** `B` altera **`H-N` de objeto promulgado** por ato soberano — `IR-05`: *"exige
ato novo"* — e inverte a relacao geral/especial de `FND-10`. `C` e **provisoria por construcao**
e foi a escolha certa de outra missao. `D` produz **`FND` orfao**: `FND-01 §10` define a
hierarquia por **enumeracao**, e o que nao consta **nao ocupa nivel**. `Z` **encarece a mesma
mudanca**: hoje `0` Specs migram (`LC-05`).

**Tradeoff aceito (`VD-04`), e ele e o inverso do intuitivo.** Sob `M1`, corrigir uma regra
custava **1 ADR `C2 · Tipo 2`, sem ato do Soberano**. Sob `M2`, custa **1 emenda e 1 ato do
Soberano** (`LM-02`). **Promover nao facilita a manutencao: protege a norma e encarece a
correcao.** Aceita-se o encarecimento em troca de **sede correta, localizacao previsivel e
regime de mudanca proporcional ao objeto**.

## 5. Decisao *(depende de ratificacao)*

### 5.1 Os cinco atos

| # | Conteudo |
|---|---|
| **J1** | **Cria-se `FND-11` — Framework de Specifications**, em `foundation/11-framework-specifications.md`, forma documental **Framework**, entidade **`FND`**, mutabilidade **`M2`**, perfil `sob-demanda`, **399 linhas**, recebendo `SF-01` a `SF-32` |
| **J2** | Em **`FND-01 §10`**, o **nivel 2** da hierarquia normativa passa a enumerar tambem o **`Specifications Framework`**. **Nenhum nivel e criado, removido ou reordenado; a regra de precedencia interna do nivel 2 permanece literalmente identica** |
| **J3** | Em **`FND-01 §11`**, o verbete **`Fundacao`** passa de *"o conjunto dos **nove** documentos fundacionais (FND-01 a **FND-09**)"* para *"o conjunto dos **onze** documentos fundacionais (FND-01 a **FND-11**)"*, **corrigindo de passagem o achado `RD-38`** — a defasagem existia desde a vigencia de `FND-10` |
| **J4** | A tabela **Documentos derivados** de `FND-01` recebe a linha **`FND-11`**, e **`FND-03 §7`** recebe `11-framework-specifications.md` na arvore canonica de `foundation/`. **`FND-01` passa a 1.6.0** e **`FND-03` a 1.6.0** |
| **J5** | **`ADR-0021` e superado PARCIALMENTE — apenas quanto a sede normativa** (§5.4) |

**Diff literal, hashes integrais e minuta do ato:**
[PS-2026-009](../governance/pacote-soberano-2026-07-29-fnd-11.md).

### 5.2 A prova de que nenhum merito mudou em silencio

**Metodo:** `diff` entre o bloco `§5.1`–`§5.10` de `ADR-0021` **(157 linhas)** e o corpo
`§3`–`§12` de `FND-11` **(157 linhas)**.

| Resultado | Valor |
|---|---|
| **Blocos de diff** | **14** |
| dos quais **cabecalho de secao** *(renumeracao `### 5.N` → `## N`)* | **10** |
| dos quais **metodo de atualizacao** das duas declaracoes `PJ-02` *(`"ADR sucessor"` → `"emenda deste Framework"`)* | **2** |
| dos quais **`SF-05`** — `T-REFERENCIAL`: *"por este ADR"* → *"por este Framework"* | **1** |
| dos quais **`SF-32`** — `T-MERITO-DECLARADO` | **1** |
| **Blocos de diff nas outras 30 regras** | **`0`** |
| **Identificadores renumerados** | **`0` de 32** |

**As 30 regras `T-IDENTICA` sao byte a byte identicas**, incluindo a tabela dos **21 blocos**
de `SF-09`, a matriz de **50 celulas** de `SF-10` e a tabela das **seis relacoes** de `SF-21`.
A tabela regra por regra vive em **`FND-11 §2.2`** e **nao e reproduzida aqui** (`PJ-01`).

### 5.3 A unica alteracao de merito, isolada

| Campo | `ADR-0021 SF-32` | `FND-11 SF-32` |
|---|---|---|
| Mutabilidade | **`M1`** — *"ele nao se emenda"* | **`M2`** — emenda por versao |
| Correcao de defeito | **ADR sucessor** (`CC-06`, `SU-01`) | **Emenda pela classe do efeito** (`AL-01`, `CC-02`) |
| Quem aprova a correcao | Conforme a classe do ADR sucessor | **SOBERANO**, sempre (`LM-02`) |
| Tudo o mais de `SF-32` | Template unico · registro mestre · nenhum registro novo · *"criar Spec e incrementar o contador sao a mesma mudanca"* | **Integral** |

### 5.4 O alcance exato da sucessao de `ADR-0021`

| O que | Estado apos o ato |
|---|---|
| **Sede normativa de `SF-01` a `SF-32`** | **SUPERADA.** Passa a ser `FND-11`. Em divergencia entre os dois textos, **prevalece `FND-11`** — nivel 2 contra nivel 3 da hierarquia (`FND-01 §10`) |
| **`status` de `ADR-0021`** | **`ativo`, inalterado** |
| **O fechamento de `RD-23` e a correcao de `TPL-spec` 1.1.0** | **VIGENTES e nao superados.** `ADR-0021 §5.11` e `§5.12` permanecem a fonte da correcao do template |
| **Os 12 casos de determinismo de `ADR-0021 §9`** | **VIGENTES** como registro historico, inclusive `T-12`, que produziu `RD-31` |
| **A declaracao de que nenhuma `Spec` e criavel** (`§7.3`) | **VIGENTE**, e **reproduzida** em `FND-11 §13` |
| **O texto de `ADR-0021`** | **`0` bytes alterados.** `M1`, `CC-01`, `LV-04` |
| **O frontmatter de `ADR-0021`** | **`0` campos alterados** — inclusive `superado_por`, que **permanece `null`**. §5.5 |

### 5.5 Por que `ADR-0021` nao recebe `superado_por` — e a colisao esta declarada

**Duas regras de `FND-10` colidem, e a colisao e real:**

| Regra | Texto | O que autoriza |
|---|---|---|
| **`FND-10 §6.2`**, linha `M1` | *"O texto **nunca** muda. Muda apenas **o estado e os campos de sucessao**"* | **Autorizaria** gravar `superado_por` |
| **`CC-01`** | *"ADR historico **nunca e editado** — nem para corrigir erro, **nem para completar campo**, nem para registrar ratificacao posterior. A ratificacao superveniente e registrada **no indice**"* | **Proibe**, e indica o **indice** como sede do registro |

**Decisao: prevalece `CC-01`**, por quatro razoes verificaveis — **(a)** `CC-01` e a regra
**especial** sobre `ADR`, e `§6.2` e a regra **geral** sobre `M1`; **(b)** `CC-01` **indica a
alternativa** *(o indice)*, e regra que oferece alternativa nao e regra que apenas proibe;
**(c)** a **sucessao aqui e parcial**, e `superado_por` e campo **binario** — grava-lo afirmaria
uma superacao total que §5.4 nega; **(d)** — e esta e **medida, nao argumentada** — **gravar
`superado_por` ALTERA o `H-N` de `ADR-0021`.**

**A quarta razao, e como ela apareceu.** A alternativa de `Q3` foi **montada e medida** antes de
ser discutida, e a medicao devolveu o oposto do esperado:

| Objeto | `H-A` | `H-N` |
|---|---|---|
| **`ADR-0021` em vigor** | `cafd28fb…bbc1` | `511ace98…5316` |
| **`ADR-0021` com `superado_por` gravado** | `eddd6a69…aa1f` | **`09814377…b89a`** — **DIFERENTE** |

**A causa e `IR-03`, e e uma assimetria da propria lista fechada.** `IR-03` exclui de `H-N`
oito campos, entre eles **`substituido_por`** — e **nao inclui `superado_por`**. Logo, para um
`ADR`, **o unico campo de sucessao que o frontmatter oferece e, por definicao de `IR-02`,
conteudo normativo** — e alterar conteudo normativo de artefato `M1` e o que `LV-04` proibe.
**`FND-10 §6.2` autoriza mudar *"os campos de sucessao"* em `M1`, e para `ADR` essa autorizacao
nao tem objeto praticavel.** Achado **`RD-43`**, severidade **Media**, dono **DEP-GOV**, gatilho
*"proxima superacao de `ADR`"*; **alterar `IR-03` e `C2` com ADR** (`IR-04`), e **nao e materia
desta missao**.

> **Isto foi encontrado por exercer o instrumento, nao por le-lo** — o metodo de
> [MEM-APR-0006](../memory/aprendizado/MEM-APR-0006-exercer-o-contador-revela-o-defeito.md).
> A leitura de `FND-10 §6.2` autorizava a gravacao; **a medicao do hash mostrou que a
> autorizacao nao alcanca `ADR`**. Se a alternativa tivesse sido escolhida por leitura, o acervo
> teria alterado o `H-N` de um artefato `M1` **acreditando estar dentro da regra**.

**Onde a sucessao fica legivel, entao:** em **`ADR-0022 supera: [ADR-0021]`** *(frontmatter
deste ADR)*, em **`FND-11 §15`**, no **[`decisions/README`](README.md)** e na **§6 do
[catalogo mestre](../governance/artifact-registry.md)** — quatro lugares, todos permanentes.

> **Residuo declarado (`PI-10`), e ele e real.** Quem ler **apenas `ADR-0021`**, sem o indice,
> **nao descobrira que a sede mudou** — e aplicara `SF-*` a partir do ADR. **O efeito pratico e
> nulo em 31 das 32 regras**, porque o merito e identico; **em `SF-32` a leitura sera errada**,
> pois o ADR dira *"nao se emenda"* onde `FND-11` dira *"emenda-se com ato"*. Achado **`RD-40`**,
> severidade **Baixa**, dono **DEP-GOV**, gatilho *"primeira emenda a `FND-11`"*. **A alternativa
> — gravar `superado_por` — esta submetida no pacote com `H-P` medido, e agora se sabe o preco
> dela: altera o `H-N` de um artefato `M1`** *(§5.5, razao `(d)`)*. A escolha permanece do
> Soberano (`Q3` de RFC-0018 §9), **com o preco na mesa**.

### 5.6 O que esta decisao **nao** faz

| # | Nao faz | Fundamento |
|---|---|---|
| **J6** | **Nao altera o merito de `SF-01` a `SF-31`** | §5.2 — `0` blocos de diff em 30; `SF-05` referencial |
| **J7** | **Nao renumera nenhuma regra** | **32 de 32** identificadores preservados (`K3`) |
| **J8** | **Nao cria entidade, tipo documental, portao, papel, departamento, classe ou verbo de autoridade** | `FND-09 §11.1`; `FND-01 §6.2` — **7 portoes antes, 7 depois** |
| **J9** | **Nao altera a matriz de autoridade de `FND-09 §8.2`** nem `FND-10 §10.3` | **`0` celulas.** `SF-10` **remete**, nao decide |
| **J10** | **Nao altera o vinculo `Spec` × `Produto`, a sequencia por Produto nem os locais canonicos** | **`0` bytes** em `FND-03 §3.6`, `FND-04 §6` e `FND-10 §4.4`. **`RD-33` permanece aberto e bloqueante** |
| **J11** | **Nao cria `Spec`, `Produto` nem `Projeto`**, e **nao amplia a `Spec` a materia nao-produto** | Restricao expressa da missao; `S2` de `ADR-0021 §7.3` **nao e exercida** |
| **J12** | **Nao edita `ADR-0021`** — nem texto, nem frontmatter | `M1`; `CC-01`; `LV-04`; §5.5 |
| **J13** | **Nao cria nivel novo na hierarquia normativa nem regra de precedencia nova** | **8 niveis antes, 8 depois.** `FND-01 §10` ja resolve conflito no nivel 2 |
| **J14** | **Nao trata `RD-27`** — `FND-01` 1.6.0 `V1` **nao** acrescenta os quatro campos de `AC-08` | Determinacao da missao. **Declarado em §7.3, com a variante `V2` submetida em separado** |
| **J15** | **Nao corrige as Cartas** | [ADR-0023](ADR-0023-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md), pacote separado |
| **J16** | **Nao edita baseline historica, `MSG`, `FIT` nem `ADR` algum** | `BL-02`; `LV-04`; `FT-*` |

## 6. Justificativa

**Porque a forma documental correta ja estava escrita, e nao estava sendo usada.**
`FND-10 §4.1` define **Framework** como *"norma que estrutura um dominio inteiro e e consumida
por todos"*, entidade `FND`, em `foundation/NN-*.md`. A norma da `Spec` e exatamente isso, e
vivia em `decisions/`, cujo tipo tem **conteudo proibido** oposto: *"decisao pontual"*.

**Porque a promocao e provavel por medicao, e nao por leitura.** `K2` exigia zero alteracao
silenciosa. O metodo que responde nao e reler as 32 regras: e **extrair o bloco da fonte,
transforma-lo e medir o `diff`** — **14 blocos, dos quais 13 formais e 1 de merito, declarado**.
**Nenhuma das 30 regras `T-IDENTICA` foi retipada**, e por isso nao havia como uma palavra mudar
sem aparecer no `diff`.

**Porque o momento e agora, e o argumento e o oposto do intuitivo.** Nao se promove porque a
norma amadureceu — ela nunca foi exercida (`R1`). Promove-se porque **`0` Specs existem**: a
reversao custa **`0` migracoes** (`LC-05`), e esse custo **so cresce**.

**Porque o encarecimento da correcao e a feicao, nao o efeito colateral.** A norma de um dominio
que muda **sem passar pelo Soberano** e a norma de um dominio que pode ser reescrita por
`DEP-EXE` numa tarde. `M2` com ratificacao e o regime que `FND-10 §10.3` ja atribui a
**Framework** — e a promocao apenas **passa a cumpri-lo**.

## 7. Impacto

### 7.1 Quadro geral

| Dimensao | Impacto |
|---|---|
| **Artefatos criados** | **1** — `FND-11`, **399 linhas**, perfil `sob-demanda` |
| **Fontes de `foundation/` emendadas** | **2** — `FND-01` **1.5.0 → 1.6.0** *(485 → 488 linhas)* · `FND-03` **1.5.0 → 1.6.0** *(631 → 633 linhas)* |
| **Fontes de `foundation/` NAO tocadas** | **8** — `FND-02`, `FND-04`, `FND-05`, `FND-06`, `FND-07`, `FND-08`, `FND-09`, `FND-10`. **`0` bytes**, verificavel por `sha256` |
| **`TPL-spec`** | **`0` bytes.** Permanece **1.1.0**, corrigido por `ADR-0021` |
| **`ADR-0021`** | **`0` bytes.** Permanece `ativo`; sucessao **parcial** registrada em 4 lugares (§5.5) |
| **Departamentos afetados** | **`DEP-GOV`** *(autor; registra)* · **`DEP-PRD`** *(materia; consulta obrigatoria em toda emenda futura)* · **`DEP-QAR`** *(revisa)*. **Nenhum ganha responsabilidade que nao tivesse** |
| **Entidades · tipos documentais · portoes · papeis · classes · verbos de autoridade** | **0 criados · 0 alterados · 0 removidos** |
| **Niveis da hierarquia normativa** | **8 antes · 8 depois.** O nivel 2 passa de **9** para **10** documentos enumerados |
| **Documentos `M3` em cascata `CV-04`** | **6** — [catalogo mestre](../governance/artifact-registry.md) · [`README` raiz](../README.md) · [`foundation/README`](../foundation/README.md) · [`decisions/README`](README.md) · [`rfcs/README`](../rfcs/README.md) · [`governance/README`](../governance/README.md) |
| **Custo de contexto criado** | **+399 linhas** `sob-demanda` *(`FND-11`)* **+3** em `FND-01` `nucleo` **+2** em `FND-03` `nucleo`. **O consumidor da norma da `Spec` nao paga mais:** paga **o mesmo**, em outro arquivo — `ADR-0021` era `sob-demanda` e `FND-11` tambem e |
| **Ganho `PI-14`** | **Organizacao** — a norma de um dominio passa a viver onde o acervo aloja norma de dominio; **quem procura em `foundation/` encontra**. **Reavaliacao: 2027-01-28** |

### 7.2 A cascata, integralmente enumerada

| Objeto | O que muda | Executado no ato? |
|---|---|---|
| `FND-01 §10`, `§11`, *Documentos derivados*, historico | 4 alteracoes, **+3 linhas** | **Sim** — depende de ato |
| `FND-03 §7`, historico | 2 alteracoes, **+2 linhas** | **Sim** — depende de ato |
| `FND-11` | criacao | **Sim** — depende de ato |
| **6 indices `M3`** | registro do novo `FND`, do `ADR`, da `RFC` e do pacote | **Sim** — na mesma mudanca (`CV-04`, `IX-02`) |
| `FND-10 §4.1` e `§10.3` | **Nada.** As linhas *Framework* **ja cobrem** `FND-11` sem alteracao — *"aprova SOBERANO · ratifica SOBERANO · `M2` · perfil `missao`"* | **Nao — nao ha o que alterar** |
| `FND-09 §5`, `§8.2` | **Nada.** `FND` e entidade existente; `FND-11` e **instancia**, nao tipo novo | **Nao** |
| **`TPL-documento`** | **Nada.** `FND-11` segue a forma sem exigir template novo | **Nao** |

> **Divergencia de perfil, declarada.** `FND-10 §10.3` atribui a **Framework** o perfil padrao
> **`missao`**; `FND-11` declara **`sob-demanda`**. **Nao e defeito:** o padrao e *"por tipo"* e
> **admite declaracao propria** (`FND-10 §2.2`, coluna *Valor padrao*), e os quatro Frameworks
> vigentes ja divergem entre si — `FND-05`, `FND-06` e `FND-07` sao **`S`** e `FND-08` e **`M`**,
> medido no [catalogo §4.1](../governance/artifact-registry.md). **`sob-demanda` e o perfil que
> `ADR-0021` ja tinha**, e mante-lo faz o custo de contexto **nao mudar** com a promocao.

### 7.3 `RD-27` — a determinacao da missao colide com um gatilho registrado, e a colisao esta declarada

**A regra propria contradita (`PI-13`), dita literalmente:**

| Fonte | Texto |
|---|---|
| **Determinacao da Missao 1.13.1** | *"Nao tratar `RD-27`, `RD-36` ou outros achados neste rito"* |
| **`AC-08`** *(`FND-10 §2.2`)* | Os cinco campos sao obrigatorios em *"artefato criado **ou emendado** a partir da vigencia deste framework"* |
| **Gatilho registrado de `RD-27`** | *"**Proximo ato soberano que alcance `FND-01`, `FND-02` ou `FND-10`**"* — [FIT-2026-014 R2](../governance/fitness/README.md) |

**Este ato alcanca `FND-01`. Logo o gatilho de `RD-27` dispara neste ato**, e a determinacao da
missao manda nao tratar. **As duas nao podem ser cumpridas ao mesmo tempo.**

**O que foi feito, e nao foi escolher pelo Soberano:**

| | `V1` — **objeto submetido** | `V2` — **alternativa medida** |
|---|---|---|
| Os quatro campos de `AC-08` | **Ausentes** — a determinacao e cumprida | **Presentes** — `RD-27` fecha **quanto a `FND-01`**; `FND-02` permanece aberta |
| Linhas | **488** | **492** |
| `H-A` | `acec800b…a3a8` | `43cae800…6767` |
| Consequencia | **`AC-06` segue descumprido por `FND-01`** — terceira ocorrencia, e a **primeira em que o ato que a repete tinha como nao repetir** | Trata achado que a missao vedou tratar |

**Recomendacao do proponente: `V1`**, porque a determinacao e do Soberano e o proponente nao a
reinterpreta. **`V2` esta pronto, medido e disponivel no mesmo pacote** — escolhe-lo no ato
**e a decisao mais simples do mundo** e nao exige nova missao.

## 8. Evidencias

| # | Evidencia | Valor | Confianca |
|---|---|---|---|
| **E1** | Baseline vigente reproduz antes das edicoes | **169 · 48.764 · `BL-2026-07-29-09`** | **Alta — medida** |
| **E2** | A forma documental **Framework** existe e aloja norma de dominio em `foundation/NN-*.md` | `FND-10 §4.1`, linha *Framework* | **Alta — literal** |
| **E3** | `FND-01 §10` enumera o nivel 2 por nome, com **9** membros | `FND-01 §10` | **Alta — literal** |
| **E4** | `FND-03 §7` enumera **10** arquivos de `foundation/` | `FND-03 §7` | **Alta — literal** |
| **E5** | **30 de 32** regras migram **byte a byte** | **14 blocos de `diff`**, `0` nas 30 | **Alta — medida por ferramenta** |
| **E6** | Projecao declarada **dentro de fundacional** e pratica vigente | **2** ocorrencias em `FND-10` — `§10.3` e a coluna *Local* de `§4.1`–`§4.7` | **Alta — medida** |
| **E7** | Perfil de contexto de Framework **ja divergia** do padrao entre os pares | **3 `S` + 1 `M`** em 4 Frameworks vigentes | **Alta — medida** |
| **E8** | `IR-02`/`IR-03` reimplementados e **validados contra controles publicados antes** de medir candidato | **7 de 7 reproduzem** — [PS-2026-009 §4.3](../governance/pacote-soberano-2026-07-29-fnd-11.md) | **Alta — medida** |
| **E9** | `H-N` **invariante sob `O4`** e `IR-09` reproduz `H-A` | **3 de 3** nos objetos que transitam de estado | **Alta — medida** |
| **A1** | **Evidencia ausente, declarada:** **nenhuma `Spec` real existe.** As 32 regras seguem **determinadas, nao observadas** — a promocao **nao muda isso** | `PI-10`; `R1` de FIT-2026-015 | — |
| **A2** | **Evidencia ausente, declarada:** **`FND-11` nunca foi emendado**, logo o regime `M2` que `SF-32` passa a declarar e **determinado, nao observado** | `PI-10` | — |

## 9. Riscos e mitigacao

| # | Risco | Prob. | Impacto | Mitigacao |
|---|---|---|---|---|
| **RB-1** | **A promocao ser lida como reabertura do merito** | Media | **Alto** | §5.2 mede **`0` blocos de `diff`** em 30 regras; `FND-11 §2.2` declara as 32 uma a uma. **`SF-32` e a unica excecao, e esta nomeada tres vezes** |
| **RB-2** | **Duas sedes coexistirem e divergirem** — alguem aplica `SF-*` lendo `ADR-0021` | **Media** | Medio | **`RD-40`**, declarado em §5.5, com dono e gatilho. **O merito e identico em 31 de 32**, e a hierarquia resolve: `FND-11` e nivel 2, `ADR-0021` e nivel 3 (`FND-01 §10`) |
| **RB-3** | **`FND-11` virar segunda fonte de verdade sobre autoridade** | Media | **Alto** | As duas projecoes carregam declaracao `PJ-02` completa; `PJ-03` da precedencia a fonte; **nenhum titular fora de `FND-04 §2` e `FND-09 §8.2`** |
| **RB-4** | **`CC-05` ser lido como proibicao de projecao em fundacional** | Media | Medio | `CC-05` proibe reproducao **nao declarada**; `PJ-02` a torna licita (`ADR-0008`). **Precedente medido: `FND-10` carrega 2** |
| **RB-5** | **A classe `C3 · Tipo 1` ser contestada como excessiva** | Media | Baixo | **Declarada como duvida resolvida pela regra mais restritiva** (`GV-03`, `FND-01 §7.1.6`). `Q1` de RFC-0018 §9 leva a pergunta ao Soberano **sem esconde-la** |
| **RB-6** | **`FND-01` emendada sem `AC-08`** — terceira ocorrencia de `RD-27` | **Alta** | Medio | §7.3: **duas variantes com hash**, e a determinacao da missao cumprida na recomendada. **Nao ha versao deste ato que evite a colisao** — so ha versao que a declare |
| **RB-7** | **Framework sem instancia envelhecer** | **Observada — `A1`** | Medio | Gatilho de revisao: **a primeira `Spec` real**. `M2` torna a correcao **possivel por emenda**, o que `M1` proibia — e esse e o ganho |
| **RB-8** | **Concentracao em DEP-GOV** — `RC-02` | **Observada — 8a ocorrencia** | Medio | **`RD-39`.** Determinada pela matriz (`FND-09 §8.2`), nao por escolha. **DEP-PRD e consulta obrigatoria** e **o merito nao e de DEP-GOV** — e recebido |

## 10. Classificacao

| Campo | Valor |
|---|---|
| **Classe de mudanca** | **C3** — altera a **hierarquia normativa** (`FND-01 §10`) e a **propria Fundacao** (`FND-04 §2`). **Teste item a item:** principio imutavel — **nao toca**; linha vermelha — **nao toca**; **hierarquia normativa — TOCA**, acrescentando um membro ao nivel 2 sem criar, remover ou reordenar nivel; direitos de decisao de `FND-01 §7.3` — **nao toca**; a propria Fundacao — **1 documento criado, 2 emendados** |
| **Tipo de reversibilidade** | **1** — pela **regra da duvida** (`GV-03`) e pela classificacao **mais restritiva** (`FND-01 §7.1.6`). O plano de reversao de §11 e **barato hoje** e **exige novo ato do Soberano**, o que basta para `Tipo 1` |
| **Instrumento** | **RFC obrigatoria → analise de impacto → ADR → ratificacao do SOBERANO** (`FND-04 §2`, C3) |
| **Decisor** | **SOBERANO. Indelegavel** |
| **Ratificacao** | **Sempre** (`FND-04 §2.1`) |
| Data da decisao · vigencia | **candidata** · **depende de ato** |

> **A duvida sobre o tipo, declarada.** Ha argumento real para **`Tipo 2`**: **`0` Specs
> existem**, `ADR-0021` permanece intacto e reverter e restaurar dois arquivos e apagar um.
> **O que empurra para `Tipo 1` e verificavel:** a reversao **exige novo ato do Soberano**
> (`LM-02`), e a norma e **assumida como permanente**. `Q1` de RFC-0018 §9 leva a escolha ao
> Soberano; **classificar mais alto e o erro barato, e classificar mais baixo e o caro**.

## 11. Plano de reversao

**Exigido em `Tipo 1` (`VD-06`), e o custo esta medido.**

| Passo | Acao | Responsavel |
|---|---|---|
| 1 | ADR sucessor que **supere este**, declarando o que passa a valer (`SU-04`, `O6`) | **DEP-GOV**; aprova e ratifica **SOBERANO** |
| 2 | **Ato do Soberano** autorizando a reversao — **e o passo que torna isto `Tipo 1`** | **SOBERANO** |
| 3 | `FND-11` → **`O9` retirada** (`status: revogado`), declarando que **`ADR-0021` volta a ser a sede** (`SU-04`) | **DEP-GOV** |
| 4 | Restaurar `FND-01` **1.5.0** *(`H-A` `2d962616…310d`)* e `FND-03` **1.5.0** *(`H-A` `ad1b47bd…33a6`)* pelos diffs **literais e reversiveis** de [PS-2026-009 §2](../governance/pacote-soberano-2026-07-29-fnd-11.md) | **DEP-GOV** |
| 5 | Verificar que **nenhuma `Spec` perdeu fundamento** — **`0` Specs existem, logo `0` migram** (`LC-05`) | **DEP-QAR** |
| 6 | Reprocessar os **6** indices `M3` a partir da fonte (`RG-03`) | **DEP-GOV** |

**Custo medido:** 1 ADR + 1 ato + 1 retirada + **2** restauracoes por hash publicado + **6**
indices. **`0` Specs migram, `0` artefatos perdem fundamento, e `ADR-0021` nao precisa ser
restaurado porque nunca foi alterado.** **Reverter agora e mais barato do que sera depois da
primeira `Spec`** — o mesmo argumento que recomenda promover agora.

## 12. Revisao

| Campo | Conteudo |
|---|---|
| Revisor independente | **DEP-QAR** |
| Autor | **DEP-GOV** — **autor ≠ revisor** (`ADR-0005`, `RM-06b`, `FT-02`) |
| Materia | **DEP-PRD** — consultado como dono do tipo `SPC` e autor do merito |
| **Residuo declarado (`PI-10`)** | **DEP-PRD e a area alcancada** — a norma da sua materia muda de sede e de regime de mudanca — e **nao e autor nem revisor deste ADR**, porque `FND-09 §8.2` nao lhe permite propor `FND` nem revisa-lo. **Residuo de matriz, nao de escolha** — `IC-3`, `RD-39` |
| Gatilho de revisao | **A primeira `Spec` real**; **ou** a primeira emenda a `FND-11`, que testara o regime `M2` *(`A2`)* |

## 13. Rastreabilidade

| Campo | Conteudo |
|---|---|
| **Origem** | [RFC-0018](../rfcs/RFC-0018-sede-canonica-do-framework-de-specifications.md) |
| **Pacote de decisao** | [PS-2026-009](../governance/pacote-soberano-2026-07-29-fnd-11.md) |
| **Decisao superada parcialmente** | [ADR-0021](ADR-0021-framework-de-specifications.md) — **apenas quanto a sede normativa** (§5.4). `status` **inalterado**; texto e frontmatter **intactos** |
| **ADR irmao, materia separada** | [ADR-0023](ADR-0023-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md) — `RD-31`, pacote **PS-2026-010** |
| **Achados que abre** | **`RD-38`** *(Baixa — verbete `Fundacao` defasado; **corrigido** por `J3`)* · **`RD-39`** *(Baixa — `RC-02`, 8a ocorrencia; **declarada, nao resolvida**)* · **`RD-40`** *(Baixa — `ADR-0021` nao declara a propria superacao parcial; **declarada, nao resolvida**, com alternativa medida no pacote)* · **`RD-43`** *(Media — `IR-03` exclui `substituido_por` de `H-N` e **nao exclui `superado_por`**: para `ADR`, o unico campo de sucessao do frontmatter **altera `H-N`**, e a autorizacao de `FND-10 §6.2` fica sem objeto praticavel. **Encontrado por medicao** — §5.5)* |
| **Achados que NAO fecha** | **`RD-33`** *(bloqueante — o vinculo `Spec` × `Produto`)* · `RD-27` *(§7.3)* · `RD-34` · `RD-36` · `RD-37` · `RD-24` · `RD-30` · `RD-10` a `RD-13` · `RD-18` · `RD-21` |
| **Regra de integridade** | [ADR-0012](ADR-0012-integridade-do-ato-de-ratificacao.md), `IR-01` a `IR-10` |
| **Verificacao de aptidao** | [FIT-2026-016](../governance/fitness/FIT-2026-016-canonizacao-e-propagacao.md) |
| **Relatorio da missao** | [PT-2026-008](../governance/relatorio-transicao-2026-07-29-canonizacao.md) |
| **Licao aplicada** | **RD-08** — o bloco de abertura **remete ao frontmatter** e nao afirma vigencia |

## Checklist de validade (FND-07 §4.1)

| # | Regra | Cumprida |
|---|---|---|
| VD-01 | ≥ 2 alternativas reais + *"nao fazer nada"* | ✅ **quatro + Z** — [RFC-0018 §4](../rfcs/RFC-0018-sede-canonica-do-framework-de-specifications.md) |
| VD-02 | Criterios declarados **antes** da escolha | ✅ RFC-0018 §3 precede §4 |
| VD-03 | Nenhuma alternativa de palha | ✅ **`C` e a escolha vigente e foi a correta de outra missao**; `B` e recusada por `H-N`, nao por conveniencia; `Z` e recusada com o argumento **invertido em favor de quem a defende** |
| VD-04 | Tradeoff aceito explicito | ✅ fim de §4 — **promover encarece a correcao** |
| VD-05 | Evidencia ausente declarada | ✅ **`A1`** *(nenhuma `Spec` existe)* e **`A2`** *(o regime `M2` nunca foi exercido)* |
| VD-06 | Plano de reversao obrigatorio em Tipo 1 | ✅ §11, com custo medido |
| VD-07 | Impacto em cascata mapeado | ✅ §7.1 e §7.2 — **6** indices `M3`, e o que **nao** muda esta enumerado |
| VD-08 | Data e responsavel presentes | ✅ §10, §12 |
| VD-09 | Gatilho de revisao definido | ✅ §12 |

---

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-GOV | Emenda **C3 · Tipo 1** candidata que **cria `FND-11`** — sede fundacional do **Framework de Specifications**, **399 linhas**, forma documental *Framework*, entidade `FND`, mutabilidade `M2` — e recebe `SF-01` a `SF-32` de [ADR-0021](ADR-0021-framework-de-specifications.md) **com a equivalencia provada por ferramenta, nao por leitura**: `diff` entre o bloco de origem *(157 linhas)* e o corpo de destino *(157 linhas)* produz **14 blocos**, dos quais **10 de cabecalho**, **2 de metodo de atualizacao das projecoes `PJ-02`**, **1 referencial em `SF-05`** e **1 de merito em `SF-32`** — **`0` blocos nas outras 30 regras** e **`0` de 32 identificadores renumerados**. **A unica alteracao de merito e o regime de mutabilidade** — `M1` *(nunca se emenda)* → `M2` *(emenda por versao, com ratificacao do SOBERANO)* —, isolada em §5.3, **com o tradeoff declarado no sentido correto: promover protege a norma e encarece a correcao**. Emenda **`FND-01`** *(§10 acrescenta o `Specifications Framework` ao nivel 2; §11 corrige o verbete `Fundacao` de nove para onze documentos, fechando **`RD-38`**; a tabela de documentos derivados recebe `FND-11`)* **485 → 488 linhas**, e **`FND-03 §7`** *(arvore canonica)* **631 → 633**. **`8` das `10` fundacionais nao sao tocadas · `TPL-spec` `0` bytes · `ADR-0021` `0` bytes, inclusive no frontmatter.** A superacao de `ADR-0021` e **PARCIAL — so a sede normativa** (§5.4): o fechamento de `RD-23`, a correcao de `TPL-spec` 1.1.0, os 12 casos de determinismo e a declaracao de que nenhuma `Spec` e criavel **permanecem vigentes**, e o `status` permanece **`ativo`**. §5.5 declara a **colisao real entre `FND-10 §6.2` e `CC-01`** sobre gravar `superado_por` em `M1`, resolve por `CC-01` com tres razoes verificaveis, registra a sucessao em **quatro** lugares permanentes e **declara o residuo** — achado **`RD-40`**. §7.3 declara a **colisao entre a determinacao da missao *"nao tratar `RD-27`"* e o gatilho registrado de `RD-27`, que este proprio ato dispara**, e submete **duas variantes do candidato `FND-01` com hash medido** — `V1` estrita *(recomendada)* e `V2` fechando `RD-27` quanto a `FND-01` — **sem decidir pelo Soberano**. **`0` entidades, tipos documentais, portoes, papeis, classes ou verbos de autoridade criados · 7 portoes antes, 7 depois · 8 niveis de hierarquia antes, 8 depois · `0` bytes no vinculo `Spec` × `Produto`, que permanece integralmente vigente — `RD-33` segue aberto e BLOQUEANTE.** `IR-02` e `IR-03` foram **reimplementados e validados contra 7 controles publicados** antes de medir qualquer candidato, e `H-N` e **invariante sob `O4`** em **3 de 3**. Abre **`RD-38`**, **`RD-39`**, **`RD-40`** e **`RD-43`** — o ultimo **encontrado por exercer o instrumento**: montar a alternativa de `Q3` e **medir o hash** revelou que `IR-03` exclui `substituido_por` de `H-N` e **nao exclui `superado_por`**, de modo que **o unico campo de sucessao disponivel a um `ADR` altera o proprio `H-N`** — a leitura de `FND-10 §6.2` autorizava a gravacao, e a medicao mostrou que a autorizacao **nao alcanca `ADR`**. **Nao vigora sem ato** (FND-01 §9). |
