---
id: ADR-0023-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas
titulo: Emenda C2 Tipo 2 que propaga ADR-0018 e ADR-0019 as Cartas de DEP-PRD e DEP-EXE, sem criar titular, portao ou direito decisorio
tipo: adr
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-EXE
proprietario: DEP-EXE
aprovador: DEP-GOV
criado_em: 2026-07-29
atualizado_em: 2026-07-29
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0011, ADR-0012, ADR-0018, ADR-0019, ADR-0021]
substitui: []
substituido_por: null
classe_mudanca: C2
tipo_decisao: 2
supera: []
superado_por: null
resumo: Corrige as oito afirmacoes que ADR-0018 e ADR-0019 tornaram falsas na Carta de DEP-PRD, faz DEP-EXE declarar QG-1 pela primeira vez, e fecha RD-31 nas duas Cartas sem decidir autoridade alguma.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# ADR-0023: Propagacao de `QG-1` e da aprovacao de `Spec` as Cartas

> ## O que este ADR decide, e o que ele apenas propaga
>
> **Nada de autoridade e decidido aqui.** `QG-1` e de **`DEP-EXE`** por
> [ADR-0018](ADR-0018-liberacao-do-portao-qg-1.md), **ratificado**; a aprovacao de `Spec` segue
> **a classe** por [ADR-0019](ADR-0019-aprovador-e-ratificador-de-spec.md), **ratificado**; e
> `C2` e aprovado por `DEP-EXE` por **`FND-04 §2`**, anterior aos dois. **Este ADR e cascata**
> (`CV-04`, `CC-03`).
>
> **As Cartas nao entram em vigor por este ADR.** `FND-09 §8.2`, linha `DEP`, atribui **aprovacao
> e ratificacao** ao **SOBERANO**: enquanto nao houver ato, `DEP-PRD` permanece em **1.0.0** e
> `DEP-EXE` em **1.0.0**, com as **oito** afirmacoes falsas **vigentes**.

## Proposito

Fechar **`RD-31`** nas duas Cartas determinadas: corrigir as **oito** afirmacoes que `ADR-0018` e
`ADR-0019` tornaram falsas em `DEP-PRD`, e fazer **`DEP-EXE` declarar `QG-1`**, que hoje **nao
consta de nenhuma linha da sua Carta**.

## Escopo

| Item | Definicao |
|---|---|
| Inclui | **8** correcoes + **7** blocos revisados em `DEP-PRD` **1.1.0** · **11** blocos alterados em `DEP-EXE` **1.1.0** |
| **Nao** inclui | O **merito** de `ADR-0018` e `ADR-0019`, **nao reaberto** · **titular, portao, papel, classe ou direito decisorio novo** · `DEP-OPS`, `DEP-GRW` e `DEP-TLS`, onde o defeito **tambem foi medido** — **`RD-37`**, §7.3 · `DEP-ENG` *(revisada; nada a corrigir)* · `FND-01`, `FND-04`, `FND-09`, `FND-10`, `TPL-spec` — **`0` bytes** · a sede da norma da `Spec` — [ADR-0022](ADR-0022-sede-canonica-do-framework-de-specifications.md), **pacote separado** · `RD-27`, `RD-33`, `RD-36` |
| Origem | [RFC-0019](../rfcs/RFC-0019-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md) |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| Propoe / autor | **DEP-EXE** | [FND-09 §8.2](../foundation/09-meta-model.md), linha `DEP` — **proponente unico** de Carta de Departamento |
| Revisor independente | **DEP-QAR** | `RM-06b`; `AC-03` |
| Aprova **este ADR** | **DEP-GOV**, em lugar de `DEP-EXE` | **`C2`** exigiria `DEP-EXE` (`FND-04 §2`), **impedido pela propria autoria** (`DEP-EXE §10 I-1`, `PI-05`, `LV-03`). Precedente: **`FIT-2026-003`**, aprovado por DEP-GOV pela mesma razao |
| Aprova e **ratifica as Cartas** | **SOBERANO** | `FND-09 §8.2`, linha `DEP`; **`DC-09`**. Indelegavel |

> **Residuo declarado (`PI-10`).** **DEP-EXE e o autor e e a area que ganha a declaracao de
> titularidade.** A titularidade **nao nasce aqui** — nasce em `ADR-0018`, do qual DEP-EXE **nao
> foi autor nem revisor** —, e `FND-09 §8.2` **nao admite outro proponente** de Carta
> (`IC-3`). **DEP-PRD, a area que perde declaracoes, tambem nao e autora nem revisora**, pela
> mesma razao. Residuo **de posicao, nao de interesse**, e mitigado por **revisao de DEP-QAR** e
> **aprovacao de DEP-GOV**.

---

## 1. Contexto

O sexto ato soberano
([MSG-2026-0006](../memory/operacional/MSG-2026-0006-ato-soberano-aplicacao-integral.md))
ratificou `ADR-0018` e `ADR-0019` e promulgou `FND-01` **1.5.0**, `FND-09` **1.5.0** e `FND-10`
**1.4.0**. **`ADR-0018 §7` declarou a cascata nas Cartas como devida**, com dono `DEP-EXE` e
gatilho *"ato sobre esta emenda"*. **O ato veio. A cascata nao.**

`ADR-0021` mediu o efeito ao **simular o consumo**: o caso `T-12` resolveu *"quem libera
`QG-1`?"* **pelas Cartas** e obteve **`DEP-PRD`** — resposta errada, deterministica. Virou
**`RD-31`**, severidade **Alta**, e a ressalva **`R3`** de `FIT-2026-015` fixou o gatilho:
**antes da primeira `Spec`**.

## 2. Problema / Pergunta de decisao

**Como fazer as Cartas dizerem o que a fonte ja diz, sem que a correcao seja lida como decisao
nova sobre autoridade?**

## 3. Criterios de decisao

`L1` a `L8` de [RFC-0019 §4](../rfcs/RFC-0019-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md),
declarados **antes** das opcoes e **nao reproduzidos aqui** (`PJ-01`).

## 4. Alternativas consideradas

**Quatro opcoes e a opcao Z**, em
[RFC-0019 §5](../rfcs/RFC-0019-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md) — **`A`
emendar as duas Cartas revisando todos os blocos** *(escolhida)* · **`B` corrigir so `§5` e
`§5.2`** · **`C` emendar as quatro Cartas** · **`D` nota interpretativa** · **`Z` nao propagar**.

**Por que `A`.** `B` **falha por medicao**: deixaria **seis** das oito afirmacoes vivas e **nao
daria titular declarado a `QG-1`** — e foi exatamente o erro de amostragem que fez
`PT-2026-004 §3.1` enumerar **4** onde `RD-31` mediu **8**. `C` e **tecnicamente superior** e foi
recusada **por escopo determinado, nao por merito** — §7.3. `D` criaria **terceira fonte** para a
mesma pergunta, agravando o defeito. `Z` mantem divergencia conhecida entre fonte fundacional e
Carta vigente.

**Tradeoff aceito (`VD-04`):** o acervo sai de **11 afirmacoes falsas em 4 Cartas** para **3 em
3**. **E melhora medida, nao fechamento** — e `RD-37` fica **aberto com dono, gatilho e custo**.

## 5. Decisao *(as Cartas dependem de ato do Soberano)*

### 5.1 `DEP-PRD` 1.1.0 — as oito correcoes

| # | Local | Antes | Depois |
|---|---|---|---|
| **P1** | `§3 P-8` | *"**Portao QG-1**"* | *"**Completude da spec submetida a `QG-1`**"*, com **"liberar o portao e de DEP-EXE"** |
| **P2** | `§5` | *"Liberacao de **QG-1** · A2 · —"* | *"**Submissao da spec a `QG-1`** · A2 · consulta DEP-QAR"*, com **"a liberacao do portao e de DEP-EXE"** |
| **P3** | `§5` | *"**Aprovar Spec** · fonte: `FND-09 §8.2`: **aprova DEP-PRD (QG-1)**"* | *"**Aprovar Spec de classe `C0` ou `C1`**, como proprietario"*, com a fonte **atual**: *"aprova conforme classe (FND-04 §2)"*, `C1` como piso, **`C2` DEP-EXE, `C3` SOBERANO** |
| **P4** | `§5.2` | tabela *"Portoes sob minha responsabilidade"* com `QG-1` | **"Nenhum."** + tabela *"Meu papel: **Submetido — nunca liberador**"* |
| **P5** | `§5.2` | *"**QG-1 e o unico portao que DEP-PRD libera sozinho**"* | Nota nova: **"nenhum portao e criado nem transferido aqui"**; *"liberar nao e aprovar"*; **"DEP-PRD segue decidindo o escopo"**; veto de DEP-QAR **integral** |
| **P6** | `§7` | `Spec` — *"**Autor e aprovador** (QG-1)"* · *"`projects/`"* | *"**Autor e proponente**; aprovador **apenas** quando a classe for `C0`/`C1`; **nunca liberador de `QG-1`**"* · **`products/<slug>/specs/`** *(`RD-41`)* |
| **P7** | `§10.1 RP-1` | risco **vivo**, impacto **Alto**, mitigacao *"assimetrica"* | **"EXTINTO NA FONTE"** por `ADR-0018`, **linha conservada** (`MM-09`), com a mitigacao original citada |
| **P8** | `§12.3` | *"**Portao QG-1** · destino explicito obrigatorio"* | *"**Submissao da spec a `QG-1`**"*; declara que **o portao nao e destino desta extincao** porque `DEP-PRD` **nao o detem** |

**Os sete blocos adicionais revisados** — exigencia da missao, *"nao somente §5 e §5.2"*:

| # | Local | O que muda |
|---|---|---|
| **P9** | `§4` *(o que nao me compete)* | **+2 linhas** — *"liberar `QG-1`"* → `DEP-EXE`; *"aprovar a Spec `C2`/`C3` que eu escrevo"* → `DEP-EXE`/`SOBERANO` |
| **P10** | `§5.1` *(o que nao decido)* | **+2 linhas**, espelhando `P9` |
| **P11** | `§8` *(escalonamento)* | *"nao se libera QG-1"* → *"**a spec nao e submetida a `QG-1`**"* |
| **P12** | `§8.2` *(handoff)* | *"QG-1 liberado"* → *"`QG-1` liberado **por DEP-EXE**"* |
| **P13** | `§10` *(impedimentos)* | **`I-12` novo** — *"liberar o portao `QG-1` sobre a Spec que eu escrevi"*, substituto **DEP-EXE** |
| **P14** | `§10.2` *(incompatibilidades)* | **+1 linha** — *"produtor da spec × liberador do portao que a verifica"* |
| **P15** | `§11 KP-6` | *"Liberacoes de **QG-1**"* → *"**Specs submetidas a `QG-1`**"*, remetendo a `KX-15` de `DEP-EXE`; **valor `0` mantido, data remedida** |
| **P16** | `§9.1`, `§13.2`, `§13.3` | `TPL-spec` **132 → 272** linhas *(consequencia de `ADR-0021`)*; recortes **remedidos** *(53→55, 130→145, 429→445, 30%→33%)*; rastreabilidade recebe `ADR-0018`, `ADR-0019`, `ADR-0023`, `RD-31` e `RD-41` |

> **O que `§9.1` NAO corrige, e por que.** O custo do **nucleo** permanece **`1.099` linhas**,
> valor de 2026-07-28. **Ele divergiu**, e a divergencia e materia de **`RD-27`** — *"`FND-10 §8.5`
> declara `1.087` contra `1.116` medidos"* —, que **esta missao esta determinada a nao tratar**.
> **Corrigido apenas `TPL-spec`**, cuja variacao vem de `ADR-0021` e **nao** de `RD-27`.

### 5.2 `DEP-EXE` 1.1.0 — `QG-1` passa a existir na Carta

| # | Local | O que passa a constar |
|---|---|---|
| **E1** | `§3` | **`X-13`** — *"**Portao `QG-1`**"*, com *"verifico presenca e verificabilidade, nunca merito de escopo"* |
| **E2** | `§5` | **+2 linhas** — *"Liberacao de **QG-1** · A3"*, consulta `DEP-PRD` e `DEP-QAR`; e *"**Aprovar Spec quando a classe do efeito for `C2`**"*, com `C0`/`C1` no proprietario e `C3` no SOBERANO |
| **E3** | `§5.2` | **`QG-1` na tabela de portoes**, com *"liberar nao e aprovar"* |
| **E4** | `§5.2`, nota | **Paragrafo novo:** `QG-1` verifica **artefato produzido por outro**, e e **essa alteridade que satisfaz** a regra de portao, em vez de excepciona-la. Declara que **`I-5` continua vedando decidir merito** e que **o portao nao e via para contorna-lo** |
| **E5** | `§6.1` | **Entrada nova** — *"spec submetida a `QG-1`"*, de `DEP-PRD`, canal **HANDOFF** |
| **E6** | `§6.2` | **Saida nova** — *"liberacao de `QG-1`"*, com **responsavel e data** |
| **E7** | `§7` | **`SPC` novo** — *"liberador de `QG-1`; aprovador quando `C2`; **nunca autor nem revisor**"*, em `products/<slug>/specs/` |
| **E8** | `§10` | **`I-10` novo** — *"definir, redigir ou alterar o conteudo da `Spec` que eu libero"*, substituto **DEP-PRD** |
| **E9** | `§10.1` | **`RX-8` novo** — *"`QG-1` virar gargalo, ou virar via para decidir escopo"*, herdando `RS-1` e `RS-2` de `ADR-0018` |
| **E10** | `§10.2` | **+1 linha** — *"liberador de `QG-1` × autor ou revisor da `Spec` liberada"* |
| **E11** | `§11` | **`KX-15` novo** — *"liberacoes de `QG-1`"*, valor **`0` medido**; contagem passa de **14/9/5** para **15/10/5** |
| **E12** | `§12.3` | **Destino de `QG-1` na extincao** — **nunca** a `DEP-PRD`, **nunca** a `DEP-ENG` |
| **E13** | `§13.2`, `§13.3` | Recortes **remedidos** *(155→172, 481→506, 32%→34%)*; rastreabilidade recebe `ADR-0018`, `ADR-0019`, `ADR-0023` e o **achado que a Carta fecha** |

**Diff literal, hashes integrais e minuta do ato:**
[PS-2026-010](../governance/pacote-soberano-2026-07-29-rd-31.md).

### 5.3 O que esta decisao **nao** faz

| # | Nao faz | Verificacao |
|---|---|---|
| **N1** | **Nao cria titular.** `DEP-EXE` detem `QG-1` por `ADR-0018` e aprova `C2` por `FND-04 §2` | **Cada linha nova cita a fonte anterior** |
| **N2** | **Nao cria portao.** **7 antes, 7 depois** | `FND-01 §6.2` |
| **N3** | **Nao cria papel, classe, verbo de autoridade, entidade ou tipo documental** | `FND-09 §8.1`, `§11.1` |
| **N4** | **Nao altera direito de decisao de `FND-01 §7.3`** — *escopo e prioridade de produto* segue **decide DEP-PRD, homologa DEP-EXE** | `0` bytes em `FND-01` |
| **N5** | **Nao retira de `DEP-PRD` o que continua sendo dele** — escopo, criterio de aceite funcional, autoria da `Spec`, e a **aprovacao de `Spec` `C0` e `C1`** como proprietario | `P3`; `FND-04 §2` |
| **N6** | **Mantem `DEP-ENG` e `DEP-QAR` como revisores da `Spec`** — `I-2` de `DEP-PRD` **intacto** | `FND-09 §8.2`, linha `SPC` |
| **N7** | **Nao emenda fonte alguma** | **`0` bytes** em `FND-01`, `FND-04`, `FND-09`, `FND-10`, `TPL-spec` |
| **N8** | **Nao apaga risco:** `RP-1` e **conservado e declarado extinto** | `MM-09`; `P7` |
| **N9** | **Nao corrige `DEP-OPS`, `DEP-GRW` nem `DEP-TLS`** | **`RD-37`**, §7.3 — declarado, com custo |
| **N10** | **Nao altera o vinculo `Spec` × `Produto`.** `P6` corrige a Carta **para** o local canonico, **nunca o local canonico** | `RD-33` permanece **aberto e bloqueante** |
| **N11** | **Nao edita `ADR`, `MSG`, `FIT` nem baseline historica** | `LV-04`; `BL-02` |
| **N12** | **Nao cria `Spec`, `Produto`, `Skill`, `Tool`, `Command`, `Workflow`, `Agente`, codigo ou infraestrutura** | Restricao expressa da missao |

## 6. Justificativa

**Porque a cascata era devida e tinha dono e gatilho escritos.** `ADR-0018 §7` e
`PS-2026-007 §5` declararam a emenda das tres Cartas como **nao executada, com dono `DEP-EXE` e
gatilho "ato sobre esta emenda"**. O ato ocorreu em 2026-07-29. **Nao propagar deixaria de ser
cascata declarada e passaria a ser cascata omitida.**

**Porque corrigir so `§5` seria repetir o erro que produziu o achado.** `PT-2026-004 §3.1` mediu
*"o conjunto estreito"* e enumerou **4** afirmacoes; `ADR-0021` mediu **8**. A causa foi procurar
**a frase que ficaria falsa** em vez de **o papel que mudou de titular**. **Esta decisao percorre
os 12 blocos das duas Cartas** — e foi por isso que `RFC-0019 §3.2` encontrou **3 afirmacoes a
mais em outras 3 Cartas**.

**Porque `RP-1` merecia ser declarado extinto, e nao apagado.** A Carta 1.0.0 registrava, com
honestidade incomum, *"o unico portao do sistema liberado sem contraditorio previo"*, com
mitigacao **"assimetrica e declarada como tal"**. **Apagar a linha apagaria o registro de que o
defeito existiu e de que a correcao veio da fonte** — e `MM-09` proibe exatamente isso.

**Porque `DEP-EXE` tinha de receber um impedimento junto com o portao.** O risco real de
`ADR-0018` nunca foi o gargalo: era **`RS-2`** — *"DEP-EXE passa a decidir escopo por via de
portao"*. **`I-10` e a resposta em forma de Carta**, e ela e mais forte que a nota de `FND-01 §6.2`
porque **impedimento tem substituto nomeado**: `DEP-PRD`.

## 7. Impacto

### 7.1 Quadro geral

| Dimensao | Impacto |
|---|---|
| **Cartas emendadas** | **2** — `DEP-PRD` **1.0.0 → 1.1.0** *(429 → 445 linhas)* · `DEP-EXE` **1.0.0 → 1.1.0** *(481 → 506)* |
| **Cartas NAO emendadas** | **7** — `DEP-ENG` *(nada a corrigir)*, `DEP-QAR`, `DEP-GOV`, `DEP-KMS`, `DEP-OPS`, `DEP-GRW`, `DEP-TLS`. **`0` bytes** |
| **Fontes de `foundation/` emendadas** | **0** |
| **Titulares · portoes · papeis · classes · direitos de decisao criados** | **0 · 0 · 0 · 0 · 0** |
| **Impedimentos novos** | **2** — `I-12` em `DEP-PRD`, `I-10` em `DEP-EXE`. **Impedimento restringe; nao concede** |
| **Riscos novos** | **1** — `RX-8` em `DEP-EXE`. **1 extinto** — `RP-1` em `DEP-PRD` |
| **Indicadores** | **1 novo** *(`KX-15`)* · **1 retitulado** *(`KP-6`)*. **Nenhum valor afirmado sem medicao** — os dois valem **`0`**, e o motivo e `RD-33` |
| **Documentos `M3` em cascata `CV-04`** | **4** — [catalogo mestre](../governance/artifact-registry.md) · [`README` raiz](../README.md) · [`decisions/README`](README.md) · [`rfcs/README`](../rfcs/README.md) |
| **Custo de contexto** | **+41 linhas** em duas Cartas de perfil `missao`. O **recorte de decisao** sobe de **130 → 145** em `DEP-PRD` e **155 → 172** em `DEP-EXE` — **medido, nao estimado** |
| **Ganho `PI-14`** | **Correcao** — a pergunta *"quem libera `QG-1`?"* passa a ter **a mesma resposta pelos dois caminhos**. **Reavaliacao: 2027-01-28** |

### 7.2 O que a emenda faz com `RD-31`, medido

| Medida | Antes | Depois |
|---|---|---|
| Afirmacoes falsas em `DEP-PRD` | **8** | **0** |
| Ocorrencias de `QG-1` na Carta de `DEP-EXE` | **0** | **22**, em **16** linhas — medido por `grep -o` |
| Cartas em que `QG-1` tem **titular declarado** | **0 de 9** | **2 de 9** |
| Resposta a *"quem libera `QG-1`?"* pelas Cartas | **`DEP-PRD`** — errada | **`DEP-EXE`** — igual a fonte |
| Resposta a *"quem aprova `Spec` `C2`?"* pelas Cartas | **`DEP-PRD`** — errada | **`DEP-EXE`** — igual a fonte |
| **Afirmacoes falsas remanescentes no acervo** | **11 em 4 Cartas** | **3 em 3 Cartas** — **`RD-37`** |

### 7.3 `RD-37` — o que fica aberto, com o custo na mesa

| Carta | Local | Correcao necessaria | Custo |
|---|---|---|---|
| `DEP-OPS` | `§5.2` | *"DEP-PRD (QG-1)"* → *"DEP-EXE (QG-0 e QG-1)"* | **1 linha** |
| `DEP-GRW` | `§5.2` | idem | **1 linha** |
| `DEP-TLS` | `§5.2` | idem | **1 linha** |

**Severidade Media · dono `DEP-EXE` · revisa `DEP-GOV` · aprova e ratifica `SOBERANO` · gatilho
*"proximo ato soberano que alcance `DEP-OPS`, `DEP-GRW` ou `DEP-TLS`"*.**

> **Nao foi omissao, e nao foi impossibilidade normativa: foi escopo determinado.** A missao
> determinou **"as duas Cartas"** e *"gerar candidatos versionados das duas Cartas"*. **A
> alternativa esta a um ato de distancia** — tres candidatos de **uma linha cada** —, e
> `Q1` de [RFC-0019 §9](../rfcs/RFC-0019-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md)
> a leva ao Soberano. **Enquanto isso, `LV-03` continua valendo** — liberacao por quem produziu e
> **nula**, qualquer que seja a Carta que se leia.

## 8. Evidencias

| # | Evidencia | Valor | Confianca |
|---|---|---|---|
| **V1** | Afirmacoes falsas em `DEP-PRD`, com local | **8** — `§3`, `§5` (2), `§5.2` (2), `§7`, `§10.1`, `§12.3` | **Alta — medida** |
| **V2** | Ocorrencias de `QG-1` na Carta de `DEP-EXE`, antes | **0** | **Alta — medida** |
| **V3** | A fonte citada por `DEP-PRD §5` **nao existe mais** | `FND-09 §8.2`, linha `SPC`, coluna *Aprova*: **`conforme classe (FND-04 §2)`** | **Alta — literal** |
| **V4** | Cascata declarada devida, com dono e gatilho | [ADR-0018 §7](ADR-0018-liberacao-do-portao-qg-1.md); [PS-2026-007 §5](../governance/pacote-soberano-2026-07-29-rd-14.md) | **Alta — literal** |
| **V5** | O ato que disparou o gatilho ocorreu | [MSG-2026-0006](../memory/operacional/MSG-2026-0006-ato-soberano-aplicacao-integral.md), 2026-07-29 | **Alta** |
| **V6** | **Afirmacoes falsas em outras Cartas** — nunca enumeradas | **3**, em `DEP-OPS`, `DEP-GRW`, `DEP-TLS` | **Alta — medida por `grep` nas 9** |
| **V7** | `DEP-ENG` revisada: **`0`** afirmacoes falsas | 2 mencoes, ambas **gatilho ou criterio de devolucao** | **Alta — medida** |
| **V8** | `Spec` alojada em `projects/` na Carta de `DEP-PRD` | `§7`, contra **3** fontes vigentes | **Alta — medida** *(`RD-41`)* |
| **V9** | `H-N` **invariante sob `O4`** nos dois candidatos, e `IR-09` reproduz `H-A` | **2 de 2** em cada teste | **Alta — medida** |
| **A1** | **Evidencia ausente, declarada:** **nenhuma `Spec` existe**, logo **nenhuma liberacao de `QG-1` jamais ocorreu**. `KP-6` e `KX-15` valem **`0`**, e o defeito de `RD-31` **nunca produziu efeito pratico** | `PI-10`; `RD-33` | — |
| **A2** | **Evidencia ausente, declarada:** o impedimento `I-10` e o risco `RX-8` sao **determinados, nao observados** | `PI-10` | — |

## 9. Riscos e mitigacao

| # | Risco | Prob. | Impacto | Mitigacao |
|---|---|---|---|---|
| **RC-1** | **A propagacao ser lida como transferencia de poder a `DEP-EXE`** | Media | **Alto** | **Cada linha nova cita a fonte anterior** (`N1`); `I-10` **veda** decidir conteudo da `Spec`; `I-5` intacto; a nota de `E4` declara *"liberar nao e aprovar"* |
| **RC-2** | **`DEP-PRD` ser lido como esvaziado** | Media | Medio | `N5`: conserva escopo, criterio de aceite, autoria e **aprovacao de `C0`/`C1`**. `P3` **nomeia** o que ele mantem, em vez de so remover |
| **RC-3** | **`RD-37` ser lido como esquecimento** | **Alta** | Baixo | §7.3 enumera as **3** Cartas com local, correcao e custo por linha |
| **RC-4** | **`QG-1` virar gargalo** | Media | Medio | `RX-8` na Carta de `DEP-EXE`, com mitigacao declarada |
| **RC-5** | **O ato nao vir** | Media | **Alto** | `LV-03` mitiga e **nao cumpre**: as **8** afirmacoes falsas permanecem vigentes, e a primeira `Spec` continuara recebendo resposta errada pelas Cartas |
| **RC-6** | **Aplicar so uma das duas Cartas** | Baixa | **Alto** | **Nao ha aprovacao parcial util:** aplicar so `DEP-PRD` deixaria `QG-1` **sem titular declarado em Carta alguma** — o defeito central de `RD-31`; aplicar so `DEP-EXE` deixaria **duas Cartas afirmando titulares diferentes** para o mesmo portao. **Declarado em [PS-2026-010 §1](../governance/pacote-soberano-2026-07-29-rd-31.md)** |

## 10. Classificacao

| Campo | Valor |
|---|---|
| **Classe de mudanca** | **C2** — altera **componente** *(duas Cartas)*. **Teste de `C3`, item a item:** principio imutavel — **nao toca** *(`PI-05` e **restaurado** nas duas Cartas)*; linha vermelha — **nao toca** *(`LV-03` deixa de ter caso permanente)*; hierarquia normativa — **nao toca**; direitos de decisao de `FND-01 §7.3` — **nao toca**; a propria Fundacao — **`0` bytes em `foundation/`** |
| **Tipo de reversibilidade** | **2** — reversao pelos diffs literais, com `H-A` das versoes substituidas publicado |
| **Instrumento** | **RFC → ADR** (`FND-04 §2`, `C2`) |
| **Aprovador deste ADR** | **DEP-GOV**, por impedimento de `DEP-EXE` *(autoria)*. Precedente `FIT-2026-003` |
| **Aprovador e ratificador das Cartas** | **SOBERANO**, indelegavel |
| **Ratificacao deste ADR** | **nao exigida** — `C2 · Tipo 2` (`FND-04 §2.1`) |
| Data · vigencia | **candidata** · **depende de ato sobre as Cartas** |

## 11. Plano de reversao

| Passo | Acao | Responsavel |
|---|---|---|
| 1 | ADR sucessor que supere este (`SU-04`, `O6`) | **DEP-EXE**; aprova **DEP-GOV** |
| 2 | **Ato do Soberano** — Carta de Departamento so muda por ato (`DC-09`) | **SOBERANO** |
| 3 | Restaurar `DEP-PRD` **1.0.0** *(`H-A` `6a11652f…c277`)* e `DEP-EXE` **1.0.0** *(`H-A` `fa7a6ae2…2bb8`)*, com incremento de versao devido (`AC-11`) | **DEP-EXE**; registra **DEP-GOV** |
| 4 | Verificar que **nenhuma liberacao de `QG-1` ocorreu** sob a regra nova — **`0` medido** (`KX-15`) | **DEP-QAR** |
| 5 | Reprocessar os **4** indices `M3` (`RG-03`) | **DEP-GOV** |

**Custo medido: 1 ADR + 1 ato + 2 restauracoes por hash publicado + 4 indices. `0` liberacoes de
`QG-1` a desfazer, porque `0` ocorreram.**

## 12. Revisao

| Campo | Conteudo |
|---|---|
| Revisor independente | **DEP-QAR** |
| Autor | **DEP-EXE** — **autor ≠ revisor ≠ aprovador** (`ADR-0005`, `RM-06b`) |
| Aprovador | **DEP-GOV** — porque `DEP-EXE`, aprovador natural de `C2`, **e o autor** |
| Residuo declarado (`PI-10`) | **As duas areas alcancadas sao autor e objeto**: `DEP-EXE` propoe e ganha declaracao; `DEP-PRD` perde declaracoes e **nao pode propor** (`FND-09 §8.2`, `IC-3`) |
| Gatilho de revisao | **A primeira liberacao real de `QG-1`** — que tornara `I-10`, `RX-8` e `KX-15` observados |

## 13. Rastreabilidade

| Campo | Conteudo |
|---|---|
| **Origem** | [RFC-0019](../rfcs/RFC-0019-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md) |
| **Pacote de decisao** | [PS-2026-010](../governance/pacote-soberano-2026-07-29-rd-31.md) |
| **Achado que fecha** | **`RD-31`** — quanto as **duas** Cartas determinadas. **Fecha o defeito central:** `QG-1` passa a ter titular declarado em Carta |
| **Ressalva que fecha** | **`R3`** de [FIT-2026-015](../governance/fitness/FIT-2026-015-framework-de-specifications.md) |
| **Achados que abre** | **`RD-37`** *(Media — 3 Cartas, 3 afirmacoes falsas, **nao corrigidas por escopo determinado**)* |
| **Achado que fecha de passagem** | **`RD-41`** *(Baixa — `Spec` alojada em `projects/`; corrigida **para** o local canonico)* |
| **Decisoes que propaga** | [ADR-0018](ADR-0018-liberacao-do-portao-qg-1.md) · [ADR-0019](ADR-0019-aprovador-e-ratificador-de-spec.md) — **as duas ratificadas, nenhuma reaberta** |
| **Cascata declarada devida que consome** | [ADR-0018 §7](ADR-0018-liberacao-do-portao-qg-1.md) · [PS-2026-007 §5](../governance/pacote-soberano-2026-07-29-rd-14.md) |
| **ADR irmao, materia separada** | [ADR-0022](ADR-0022-sede-canonica-do-framework-de-specifications.md) — pacote **PS-2026-009** |
| **Regra de integridade** | [ADR-0012](ADR-0012-integridade-do-ato-de-ratificacao.md), `IR-01` a `IR-10` |
| **Verificacao de aptidao** | [FIT-2026-016](../governance/fitness/FIT-2026-016-canonizacao-e-propagacao.md) |
| **Relatorio da missao** | [PT-2026-008](../governance/relatorio-transicao-2026-07-29-canonizacao.md) |

## Checklist de validade (FND-07 §4.1)

| # | Regra | Cumprida |
|---|---|---|
| VD-01 | ≥ 2 alternativas reais + *"nao fazer nada"* | ✅ **quatro + Z** |
| VD-02 | Criterios declarados **antes** da escolha | ✅ RFC-0019 §4 precede §5 |
| VD-03 | Nenhuma alternativa de palha | ✅ **`C` e tecnicamente superior a escolhida** e foi recusada **por escopo, com o custo medido** |
| VD-04 | Tradeoff aceito explicito | ✅ fim de §4 — **11 em 4 → 3 em 3**, melhora medida e nao fechamento |
| VD-05 | Evidencia ausente declarada | ✅ **`A1`** *(nenhuma liberacao jamais ocorreu)* e **`A2`** |
| VD-06 | Plano de reversao | ✅ §11, com hash das versoes substituidas |
| VD-07 | Impacto em cascata mapeado | ✅ §7.1 — **4** indices `M3`; §7.3 — o que **nao** foi corrigido |
| VD-08 | Data e responsavel presentes | ✅ §10, §12 |
| VD-09 | Gatilho de revisao definido | ✅ §12 |

---

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-EXE | Emenda **C2 · Tipo 2** candidata que **propaga** `ADR-0018` e `ADR-0019` — **ambos ratificados** — as Cartas de `DEP-PRD` e `DEP-EXE`, consumindo a cascata que `ADR-0018 §7` declarara devida com dono e gatilho. **Corrige as oito afirmacoes falsas de `DEP-PRD`** *(`§3 P-8`, `§5` ×2, `§5.2` ×2, `§7`, `§10.1 RP-1`, `§12.3`)* e **revisa outros sete blocos** — `§4`, `§5.1`, `§8`, `§8.2`, `§10` *(impedimento novo `I-12`)*, `§10.2`, `§11 KP-6`, `§9.1`, `§13.2` e `§13.3` —, cumprindo a exigencia de **nao parar em `§5` e `§5.2`**. **Faz `DEP-EXE` declarar `QG-1` pela primeira vez**, onde havia **`0` ocorrencias medidas** e passam a haver **22, em 16 linhas**: **11 blocos**, com `X-13`, a liberacao em `§5`, a **aprovacao de `Spec` `C2`**, o portao em `§5.2` com a nota que explica por que `QG-1` **satisfaz** a regra de portao em vez de excepciona-la, entrada e saida de interface, o tipo `SPC` em `§7`, o impedimento **`I-10`** *(liberar nao concede autoridade sobre o artefato)*, o risco **`RX-8`**, a incompatibilidade de papel, o indicador **`KX-15`** com valor **`0` medido** e o destino do portao na extincao. **`RP-1` nao foi apagado: foi declarado EXTINTO NA FONTE** (`MM-09`), com a mitigacao original citada. **Fecha `RD-41` de passagem** — a `Spec` estava alojada em `projects/` contra tres fontes vigentes. **Mede o efeito:** afirmacoes falsas em `DEP-PRD` **8 → 0**; ocorrencias de `QG-1` em `DEP-EXE` **0 → 8**; Cartas com titular declarado **0 de 9 → 2 de 9**; e a resposta a *"quem libera `QG-1`?"* passa a ser **a mesma pelos dois caminhos**. **Abre `RD-37`:** a medicao das **nove** Cartas — e nao das duas — encontrou a mesma afirmacao falsa em **`DEP-OPS`, `DEP-GRW` e `DEP-TLS`**, **nunca enumeradas**; o acervo sai de **11 afirmacoes falsas em 4 Cartas para 3 em 3**, e a diferenca e **escopo determinado, nao merito** — §7.3 publica o custo: **uma linha por Carta**. **`0` titulares · `0` portoes · `0` papeis · `0` classes · `0` direitos de decisao criados · `0` bytes em `foundation/` · 7 portoes antes, 7 depois.** Aprovado por **DEP-GOV** porque `DEP-EXE`, aprovador natural de `C2`, **e o autor** — precedente `FIT-2026-003`. **As Cartas nao vigoram sem ato do SOBERANO** (`FND-09 §8.2` linha `DEP`, `DC-09`). |
