---
id: ADR-0024-conformidade-de-contrato-das-fundacionais
titulo: Emenda C3 Tipo 2 que fecha RD-27 — backfill de AC-08 em FND-01 e FND-02 e correcao de FND-10 §8.5, sem reescrever norma
tipo: adr
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-07-30
atualizado_em: 2026-07-30
revisao_prevista: 2027-01-30
decisoes_relacionadas: [ADR-0009, ADR-0012, ADR-0016, ADR-0018, ADR-0022]
substitui: []
substituido_por: null
classe_mudanca: C3
tipo_decisao: 2
supera: []
superado_por: null
resumo: Fecha RD-27 nos tres objetos que ele alcanca com zero linha de corpo alterada, e corrige em FND-10 §8.5 a causa que fez cinco valores envelhecerem virando afirmacao falsa.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: ratificada
---

# ADR-0024: Conformidade de contrato das fundacionais

> ## O que este ADR decide, e o que ele deliberadamente **nao** toca
>
> **Nenhuma norma e reescrita.** Os tres candidatos tem **`0` bytes alterados no corpo** — o que
> muda e **frontmatter** em `FND-01` e `FND-02`, e **uma secao de medicao** em `FND-10`. Medido
> por `diff`, nao afirmado por leitura.
>
> **Nenhum campo, regra ou obrigacao e criada.** `AC-08` vigora desde 2026-07-28. Este ADR
> **cumpre** uma obrigacao existente; nao institui nenhuma.
>
> **As fundacionais nao entram em vigor por este ADR.** [FND-09 §8.2](../foundation/09-meta-model.md),
> linha `FND`, atribui **aprovacao e ratificacao** ao **SOBERANO**: enquanto nao houver ato,
> `FND-01` permanece em **1.5.0**, `FND-02` em **1.3.0** e `FND-10` em **1.4.0**, com as **nove**
> ausencias de campo e os **cinco** valores defasados **vigentes**.

## Proposito

Fechar **`RD-27`** nos **tres** objetos que ele alcanca, pela unica via que `IR-05` deixa aberta:
**ato soberano**. E corrigir, em `FND-10 §8.5`, **a causa** — a ausencia de regra de leitura que
transforma numero medido em afirmacao falsa quando a baseline avanca.

## Escopo

| Item | Definicao |
|---|---|
| Inclui | **Tres** objetos: **`FND-01` 1.7.0 cumulativa** *(4 campos)*, **`FND-02` 1.4.0** *(5 campos)* e **`FND-10` 1.5.0** *(§8.5 — 6 valores e a regra de leitura)* |
| **Nao** inclui | O **merito** de `AC-06`, `AC-08`, `AC-11`, `CE-04`, **nao reabertos** · a **lista fechada de `IR-03`** — `C2` com ADR proprio (`IR-04`); **`RD-43` permanece declarado e nao resolvido** · a **ampliacao do nucleo obrigatorio** — seria `C2` com Fitness Check, e **isto nao o amplia** · `FND-03` a `FND-09` e `FND-11` — **`0` bytes** · as **nove Cartas** — [ADR-0025](ADR-0025-extensao-da-propagacao-de-qg-1-as-cartas-restantes.md), rito separado · a **sede** da norma da `Spec` — [ADR-0022](ADR-0022-sede-canonica-do-framework-de-specifications.md), pacote separado · **`ADR-0021`**, que **nao e editado** *(M1, CC-01, LV-04)* · `RD-33` *(bloqueante, **nao reaberto**)*, `RD-36`, `RD-13` · **excecao formal** — `governance/exceptions/` permanece **vazio** |
| Origem | [RFC-0020](../rfcs/RFC-0020-conformidade-de-contrato-das-fundacionais.md) |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| **Propoe / autor** | **DEP-GOV** | `FND-09 §8.2`, linha `FND` — **proponente unico** |
| **Revisor independente** | **DEP-QAR** | `FND-09 §8.2`, linha `FND`; `RM-06b`; `AC-03` |
| **Aprova e ratifica** | **SOBERANO** | **C3. Indelegavel** (`FND-04 §2`) |
| Materia alcancada | **DEP-EXE** | **proprietario** de `FND-02` — **consulta obrigatoria**, e nao e autor nem revisor por determinacao de `FND-09 §8.2` |

---

## 1. Contexto

`RD-27` nasceu em 2026-07-29, na primeira vez em que `AC-08` foi **contado** em vez de lido.
Desde entao **duas missoes o deixaram intacto por determinacao**, e o gatilho registrado —
*"proximo ato soberano que alcance `FND-01`, `FND-02` ou `FND-10`"* — **ja disparou uma vez sem
ser atendido**: [ADR-0022 §7.3](ADR-0022-sede-canonica-do-framework-de-specifications.md) declarou
a colisao, submeteu duas variantes de `FND-01` e recomendou a que **nao** fecha.

**Esta e a terceira vez que o gatilho dispara, e a primeira em que existe rito proprio.**

## 2. Problema / Pergunta de decisao

> **Como cumprir `AC-08` em dois documentos ja promulgados, e corrigir uma secao de medicao
> defasada, sem reescrever uma linha de norma e sem alterar a lista fechada que torna a correcao
> cara?**

## 3. Criterios de decisao

Declarados em [RFC-0020 §3](../rfcs/RFC-0020-conformidade-de-contrato-das-fundacionais.md),
**antes** das alternativas: `K1` zero norma reescrita · `K2` zero valor inventado · `K3` um unico
`FND-01` final · `K4` cada objeto bloqueavel isoladamente · `K5` nao recorrer.

## 4. Alternativas consideradas

| # | Alternativa | Veredito |
|---|---|---|
| **A** | Backfill nos tres + regra de leitura em `§8.5` | ✅ **ESCOLHIDA** — 5 de 5 criterios |
| **B** | Backfill so em `FND-01` e `FND-02` | ❌ `K5` — o gatilho dispararia no ato seguinte, **quarta ocorrencia** |
| **C** | Emendar `IR-03` para excluir os quatro campos de `H-N` | ❌ `IR-04`; risco `RR-1` de RFC-0009 — **mexer na protecao para evitar o ato que ela existe para exigir** |
| **D** | Excecao formal a `AC-06` | ❌ Seria a **primeira excecao do acervo**, aberta para **nao** cumprir contrato **cumprivel hoje** |
| **Z** | **Nao fazer nada** | ❌ mas **valido**: `AC-06` segue descumprido, `§8.5` segue com 5 valores falsos, e **ninguem e induzido a erro** porque os cinco campos tem padrao declarado. **O custo e a quarta ocorrencia** |

## 5. Decisao *(depende de ratificacao)*

### 5.1 Os tres atos

| # | Objeto | Ato | Efeito |
|---|---|---|---|
| **1** | **`FND-01` 1.7.0 cumulativa** | Promulgacao | Frontmatter recebe `resumo`, `perfil_contexto`, `confidencialidade`, `revisor`. **`RD-27` fecha quanto a `FND-01`** |
| **2** | **`FND-02` 1.4.0** | Promulgacao | Frontmatter recebe os **cinco**. **`RD-27` fecha quanto a `FND-02`**, e o acervo deixa de ter artefato com **zero** dos cinco |
| **3** | **`FND-10` 1.5.0** | Promulgacao | `§8.5` recebe **6 valores corrigidos** e a **regra de leitura**. **`RD-27` item *(c)* e `RD-46` fecham** |

### 5.2 `FND-01` — o candidato e **cumulativo**, e a razao e que so pode existir um

**Dois ritos alcancam o mesmo arquivo:** `ADR-0022` *(§10, §11, tabela de derivados)* e este
*(frontmatter)*. **Um unico `FND-01` entra em vigor.**

| Degrau | Versao | Autoriza | Existe como arquivo? |
|---|---|---|---|
| 1 | **1.6.0** | `ADR-0022` | **Nao** — nunca existira |
| 2 | **1.7.0** | **`ADR-0024`** | **Sim** — e o objeto do ato |

> **Precedente identico, ja aplicado:** `FND-09` **1.5.0** e `FND-10` **1.4.0** sao cumulativas, e
> **`FND-09` 1.4.0 e `FND-10` 1.3.0 nunca existiram como arquivo** — [BL-2026-07-29-07](../governance/artifact-registry.md).
> **As duas linhas de historico permanecem**, uma por ADR: e o que mantem legivel **qual decisao
> autorizou o que**. Fundi-las numa linha so economizaria uma linha e apagaria a autoria.

### 5.3 `V2` **nao** e o candidato cumulativo — e a diferenca **nao e cosmetica**

A Missao 1.13.2 determinou validar se `V2` ja e, byte a byte, o candidato cumulativo.
**Nao e.** `diff` mede **4 blocos** e **+1 linha**:

| # | `V2` *(492 linhas)* | Cumulativo *(493 linhas)* | Natureza |
|---|---|---|---|
| 1 | `versao: 1.6.0` | `versao: 1.7.0` | Degrau cumulativo (§5.2) |
| 2 | `atualizado_em: 2026-07-29` | `atualizado_em: 2026-07-30` | **Data real de execucao** |
| 3 | `decisoes_relacionadas: [… ADR-0022]` | `[… ADR-0022, ADR-0024]` | Rastreabilidade da decisao que autoriza |
| 4 | **Uma** linha de historico `1.6.0`, atribuindo os quatro campos a **`ADR-0022`** | **Duas** linhas: `1.6.0` **literal de `V1`** + `1.7.0` atribuindo os campos a **`ADR-0024`** | **Correcao de afirmacao falsa** — abaixo |

> ### ⚠ Achado `RD-45` — `V2` atribui a `ADR-0022` uma alteracao que o **proprio escopo de
> `ADR-0022` exclui**
>
> A linha de historico de `V2` diz que a emenda **1.6.0**, *"por **ADR-0022**"*, acrescenta os
> quatro campos de `AC-08`. Mas o **escopo literal** de `ADR-0022` declara, em **`J14`** e em
> §7.3: *"**Nao trata `RD-27`** — `FND-01` 1.6.0 `V1` **nao** acrescenta os quatro campos de
> `AC-08`"*.
>
> **Promulgar `V2` faria o acervo carregar, dentro de `FND-01`, uma afirmacao que `ADR-0022`
> contradiz textualmente** — e `ADR-0022` e `M1`, logo **nao poderia ser corrigido para
> concordar**. Severidade **Media**, dono **DEP-GOV**, **fechado por este ADR** ao separar as
> duas linhas de historico. **`V2` foi montado como *alternativa medida*, nao como candidato de
> rito proprio; o defeito e da hipotese, nao de quem a mediu** — e **so apareceu porque o
> cumulativo foi construido e comparado**, nao porque alguem releu o texto.

**Os dois extremos estao fixados criptograficamente** — `FND-01` em vigor reproduz
`2d962616…310d` e o cumulativo reproduz `d3192235…f935b` —, **logo o diff entre eles e o
autorizado**, e nao depende de convencao de contagem.

### 5.4 `FND-10 §8.5` — a correcao alcanca a **causa**, nao so os numeros

| O que muda | Antes | Depois |
|---|---|---|
| Cabecalho da coluna | `Custo medido` | ``Custo medido em `BL-2026-07-29-10` `` |
| `FND-01` | 468 | **485** |
| `FND-03` | 619 | **631** |
| Total | 1.087 | **1.116** |
| Denominador | 18.916 | **51.698** |
| Percentual | 5,7% | **2,2%** |
| Nota `CE-05` | `FND-09` tem 1.225 linhas | **1.263** |
| **Regra de leitura** | *(inexistente)* | **6 linhas novas**: valor vinculado a baseline; numerador e denominador da **mesma** medicao; nenhum dos dois e perene |

> **Por que a regra de leitura entra na secao, e nao num achado.** `CE-04` proibe metrica sem
> fonte e sem valor observado. `§8.5` **tinha** valor observado e **nao dizia de quando** — e
> numero sem data nao envelhece virando historico: **envelhece virando mentira**. Corrigir so os
> seis numeros garantiria a terceira ocorrencia. **Corrigir a secao e o que satisfaz `K5`.**

**Os valores sao os de `BL-2026-07-29-10`, e nao os projetados para depois do ato — de
proposito.** Se `§8.5` citasse as **493** linhas que `FND-01` tera, ficaria **dependente** da
aprovacao de `FND-01`: bloquear um arrastaria o outro. Ancorar na baseline **preserva `K4`** e
torna a afirmacao **permanentemente verdadeira**, porque e datada.

### 5.5 Os valores do backfill — **nenhum inventado**, cada um com fonte

| Campo | `FND-01` | `FND-02` | Fonte do valor |
|---|---|---|---|
| `resumo` | *(V2, ja igual ao curado)* | *"Define 9 departamentos em 4 classes, matriz de interacao e a escada de especializacao."* | **Catalogo mestre §4.1**, curado pela via de migracao de `FND-10 §2.3` |
| `perfil_contexto` | `nucleo` | `missao` | **Padrao por tipo**, `FND-10 §10.3` — *Constituicao* → `nucleo`; *Doc. Fundacional* → `missao` |
| `confidencialidade` | `interno` | `interno` | **Padrao unico do acervo**, `FND-10 §2.3` |
| `revisor` | `DEP-QAR` | `DEP-QAR` | `FND-09 §8.2`, linha `FND`. **≠ `autor`** — `AC-03` cumprida |
| `ratificacao` | *(ja declarado)* | `ratificada` | **`MSG-2026-0006`** — o sexto ato promulgou `FND-02` **1.3.0** |

> **`AC-04` e o unico ponto que merece leitura em voz alta.** *"`ratificacao: ratificada` so e
> preenchido por papel distinto do executor, apos ato explicito e datado."* O valor registra o
> ato de **2026-07-29**, que existiu e esta datado; e a **1.4.0** so vigora com **ato novo**.
> **Residuo declarado (`PI-10`):** entre a montagem e o ato, o candidato — que vive **fora do
> acervo** — declara `ratificada` para uma versao ainda nao ratificada. **E exatamente o que
> `FND-01` 1.6.0 e `FND-03` 1.6.0 ja fazem** em `PS-2026-009`, e a alternativa *(declarar
> `pendente` e executar `O4`)* mudaria o regime de estado das fundacionais sem ADR que o decida.

### 5.6 O que esta decisao **nao** faz

| Nao faz | Verificacao |
|---|---|
| Criar campo, regra ou obrigacao | **`0`** — `AC-08` vigora desde 2026-07-28 |
| Alterar `IR-03` | **`0` bytes.** `RD-43` **permanece aberto e declarado** |
| Ampliar o nucleo obrigatorio | **4 artefatos antes, 4 depois** |
| Alterar linha de **corpo** em qualquer um dos tres | **`0` bytes**, medido por `diff` |
| Tocar principio imutavel, linha vermelha, portao, direito de decisao ou nivel da hierarquia | **`0`** |
| Criar departamento, classe, invariante ou celula de matriz | **`0`** — `FND-02 §1` a `§10` intocadas |
| Editar `ADR-0021`, `ADR-0022`, `MSG`, `FIT` ou baseline | **`0` bytes** |
| Criar excecao formal | **`0`** — `governance/exceptions/` permanece **vazio** |
| Fechar `RD-33` | **Nao alcanca.** O vinculo `Spec` × `Produto` permanece **integralmente vigente** |

## 6. Justificativa

**A obrigacao ja existe e e cumprivel hoje.** O que faltava nao era decisao de merito — era
**rito**. `AC-08` foi escrita em 2026-07-28, contada em 2026-07-29 e **nunca cumprida** nos dois
documentos que a hierarquia normativa coloca no topo. Enquanto isso, o acervo exige o contrato de
**todo artefato novo** — inclusive dos que este proprio rito produz.

**O custo de nao fazer e assimetrico e cresce.** Cada ato futuro que alcance qualquer um dos tres
**redispara** o gatilho, e cada disparo nao atendido e uma ocorrencia a mais de um achado que
**ja foi declarado tres vezes**.

## 7. Impacto

| Verificacao | Resultado | Evidencia |
|---|---|---|
| **Artefatos nao conformes a `AC-08`** | **2 → 0** | §5.5 |
| **Valores falsos em `FND-10 §8.5`** | **5 → 0** | §5.4 |
| **Linhas de corpo de norma alteradas** | **`0` nos tres** | `diff` — [PS-2026-011 §2](../governance/pacote-soberano-2026-07-30-rd-27.md) |
| **Variantes vivas de `FND-01`** | **2 → 1** | §5.2, §5.3 |
| **Regras criadas ou alteradas** | **`0`** `AC-*` · **`0`** `IR-*` · **`0`** `CE-*` · **`0`** `PJ-*` | — |
| **Titulares, portoes, papeis, classes, verbos, entidades, tipos documentais** | **`0` criados · `0` alterados** | `FND-09 §11.1` |
| **Niveis da hierarquia normativa** | **8 antes · 8 depois** | `0` bytes em `FND-01 §10` **por este ADR** |
| **Custo de contexto** | **+8** linhas em `FND-01` · **+6** em `FND-02` · **+7** em `FND-10`. **`0`** artefato novo no nucleo | `CE-02` |
| **Cartas alteradas** | **`0`** | [ADR-0025](ADR-0025-extensao-da-propagacao-de-qg-1-as-cartas-restantes.md) e rito separado |

## 8. Evidencias

| # | Evidencia | Fonte |
|---|---|---|
| E1 | `IR-02`/`IR-03` reimplementados e validados contra **19 controles publicados**, em **4** tipos documentais, **antes** de medir candidato | [PS-2026-011 §4.3](../governance/pacote-soberano-2026-07-30-rd-27.md) |
| E2 | `H-N` **muda nos tres** candidatos — a correcao **nao** cabe em `O4` | RFC-0020 §2.3 |
| E3 | **`0` bytes de corpo** alterados: `diff` do intervalo entre o fim do frontmatter e o inicio do historico e **vazio** em `FND-01`; em `FND-10`, `§1`–`§8.4` e `§9`–`§11` sao **identicos byte a byte** | PS-2026-011 §2 |
| E4 | `FND-10` e **`CRLF`** — **785 de 785** linhas no candidato, **`0`** convertidas | PS-2026-011 §4.4 |
| E5 | Baseline `BL-2026-07-29-10` reproduziu **antes de qualquer escrita**: **177 · 51.698 · `f7e56bc8…1bd4`** | PS-2026-011 §4.3 |
| **A1** | **Evidencia ausente, declarada:** **nenhum consumidor** foi observado sendo induzido a erro pelos campos ausentes ou pelos valores defasados. O prejuizo e **de conformidade e de confianca na medicao**, nao de dano observado | `PI-10`, `LV-12` |

## 9. Riscos e mitigacao

| # | Risco | Sev. | Mitigacao declarada |
|---|---|---|---|
| **RA-1** | O backfill ser lido como **reabertura** das emendas anteriores | Media | **`0` bytes de corpo**, medido; as linhas de historico anteriores **nao sao tocadas** |
| **RA-2** | `§8.5` envelhecer de novo | Media | A **regra de leitura** entra na secao e vincula valor a baseline — `K5` |
| **RA-3** | **Ato nao vir** | Media | `AC-06` segue descumprido e **declarado**; os cinco campos tem **padrao**. **Nenhum bloqueio novo**, e `RD-33` continua sendo o unico bloqueante |
| **RA-4** | `Tipo 2` ser contestado como brando | Media | **Escalado como `Q1`** em PS-2026-011. Declarar `Tipo 1` **nao altera nenhum hash** — muda a exigencia de plano de reversao explicito, **que este ADR ja apresenta** (§11) |
| **RA-5** | Autoria concentrada em `DEP-GOV` | **Observada** | **`RD-39`, nona ocorrencia.** Determinada por `FND-09 §8.2`; **`DEP-EXE` e consulta obrigatoria** como proprietario de `FND-02` |

## 10. Classificacao

| Campo | Valor |
|---|---|
| **Classe de mudanca** | **C3** — altera **a propria Fundacao** (`FND-04 §2`). **Nao** altera principio imutavel, linha vermelha, hierarquia normativa nem direito de decisao — teste item a item em §5.6 |
| **Tipo de reversibilidade** | **2** — a reversao e **byte a byte** e conhecida (§11) |
| **Decisor** | **SOBERANO.** Indelegavel |
| **Ratificador** | **SOBERANO** (`FND-09 §8.2`, linha `FND`) |
| Data da decisao | **pendente de ato** |
| Data de vigencia | **pendente de ato** |

> **Sobre a classificacao, com a duvida declarada.** `GV-03` manda tratar como **Tipo 1** o que
> nao se sabe classificar, e foi por `GV-03` que `ADR-0022` se declarou `Tipo 1`. **A diferenca
> entre os dois casos e verificavel:** `ADR-0022` **cria sede fundacional** — desfaze-lo exige
> mover norma de volta e emendar a hierarquia. **Este ADR nao cria nada**: a reversao e remover
> nove linhas de frontmatter e restaurar seis valores, com o `H-A` de partida publicado. **Ainda
> assim exige ato**, porque `FND` nao se emenda sem ratificacao — e por isso a diferenca entre
> `Tipo 1` e `Tipo 2` aqui **nao muda quem decide, so o que o ato precisa declarar**. **A escolha
> permanece contestavel, e `Q1` a submete em vez de esconder.**

## 11. Plano de reversao

**Tipo 2 — reversao byte a byte, com os extremos publicados.**

| Passo | Acao | Responsavel |
|---|---|---|
| 1 | ADR sucessor que supere este, declarando o que passa a valer (`SU-04`, `O6`) | DEP-GOV; ratifica SOBERANO |
| 2 | Restaurar `FND-01` ao `H-A` **`acec800b…a3a8`** *(1.6.0 `V1`)* ou **`2d962616…310d`** *(1.5.0)*, conforme o alcance da reversao | DEP-GOV |
| 3 | Restaurar `FND-02` ao `H-A` **`a42fadbf…30e3`** e `FND-10` ao `H-A` **`d52e6284…0e80`**, por **copia binaria** — `FND-10` e `CRLF` | DEP-GOV |
| 4 | `IR-09` em 3 de 3, e conferencia de que **nenhum outro artefato** dependia dos campos removidos | DEP-QAR |

**Custo medido da reversao: 3 restauracoes binarias + 1 ADR novo + 1 ato + os indices `M3`.**
**Nenhum artefato migra**, porque nenhum passou a depender destes campos para existir.

> **Recalculo do custo de reversao futuro de [ADR-0020](ADR-0020-regime-ministerial-de-promulgacao-e-ativacao.md),
> determinado pela Missao 1.13.2 — sem reclassificacao retroativa.** `ADR-0020` permanece
> **`C2 · Tipo 2`**, e **`0` bytes seus sao tocados**. O que muda e o **custo**: §10 daquele ADR
> mediu *"1 ADR novo + 6 indices `M3`"* quando o acervo tinha **164** artefatos. O recalculo esta
> em [PS-2026-013 §5](../governance/pacote-soberano-2026-07-30-consolidado.md), **fora** de
> `ADR-0020`, porque **`ADR-0020` e `M1` e nao se emenda** (`AC-10`, `CC-01`, `LV-04`).

## 12. Revisao

| Campo | Valor |
|---|---|
| Revisor independente | **DEP-QAR** — `FND-09 §8.2` linha `FND`; **≠ autor** (`AC-03`, `RM-06b`, `PI-05`) |
| Parecer | [PS-2026-011 §5](../governance/pacote-soberano-2026-07-30-rd-27.md) — revisao independente, objeto a objeto |
| Verificacao de aptidao | [FIT-2026-017](../governance/fitness/FIT-2026-017-convergencia-pre-ratificacao.md) |

## 13. Rastreabilidade

| Campo | Conteudo |
|---|---|
| RFC → ADR | [RFC-0020](../rfcs/RFC-0020-conformidade-de-contrato-das-fundacionais.md) → **ADR-0024** |
| Pacote soberano | [PS-2026-011](../governance/pacote-soberano-2026-07-30-rd-27.md) |
| **Achados que fecha** | **`RD-27`** *(integral — os tres itens)* · **`RD-45`** *(§5.3)* · **`RD-46`** *(§5.4)* |
| Achados que **nao** fecha | **`RD-33`** *(bloqueante)* · **`RD-43`** *(`IR-03`; `IR-04` exige ADR proprio)* · `RD-13` · `RD-36` · `RD-39` *(nona ocorrencia, declarada)* |
| Ressalvas que fecha | **`R2`** de [FIT-2026-014](../governance/fitness/FIT-2026-014-regime-ministerial-e-cobertura-de-contexto.md) · **`R3`** de [FIT-2026-016](../governance/fitness/FIT-2026-016-canonizacao-e-propagacao.md) |
| Cumulatividade | `FND-01` **1.7.0** contem **1.6.0** de [ADR-0022](ADR-0022-sede-canonica-do-framework-de-specifications.md) |
| Rito irmao, **independente** | [ADR-0025](ADR-0025-extensao-da-propagacao-de-qg-1-as-cartas-restantes.md) |
| Regra de integridade | [ADR-0012](ADR-0012-integridade-do-ato-de-ratificacao.md), `IR-01` a `IR-10` |
| Baseline vigente na submissao | **`BL-2026-07-29-10`** |

## Checklist de validade (FND-07 §4.1)

| # | Exigencia | Estado |
|---|---|---|
| VD-01 | Problema declarado antes da solucao | ✅ §2 |
| VD-02 | ≥2 alternativas reais | ✅ **4** + `Z` |
| VD-03 | *"Nao fazer nada"* considerada | ✅ **Alternativa Z**, com efeito real medido |
| VD-04 | Criterios declarados **antes** da escolha | ✅ RFC-0020 §3 — `K1` a `K5` |
| VD-05 | Impacto medido, nao estimado | ✅ §7 — por `diff` e `sha256` |
| VD-06 | Plano de reversao | ✅ §11, **apresentado ainda sendo `Tipo 2`** |
| VD-07 | Revisor ≠ autor | ✅ DEP-QAR ≠ DEP-GOV |
| VD-08 | Evidencia ausente **declarada** | ✅ **A1** |
| VD-09 | Classificacao justificada e contestavel declarada | ✅ §10 e `Q1` |

---

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-30 | DEP-GOV | Emenda **C3 · Tipo 2** candidata que **fecha `RD-27` integralmente**, nos **tres** objetos que ele alcanca, com **`0` bytes de corpo alterados nos tres** — medido por `diff`, nao afirmado. **`FND-01` 1.7.0 e cumulativa sobre a 1.6.0 de `ADR-0022`**, que **nunca existira como arquivo**, pelo mesmo metodo ja aplicado a `FND-09` 1.5.0 e `FND-10` 1.4.0, e com **as duas linhas de historico preservadas, uma por ADR** — fundi-las apagaria a autoria. **§5.3 responde a pergunta que a missao determinou e a resposta e NAO:** `V2` **nao** e byte a byte o candidato cumulativo — `4` blocos de diff, `+1` linha —, e **uma das quatro diferencas nao e cosmetica**: `V2` atribui a **`ADR-0022`** o backfill de `AC-08`, que o **escopo literal de `ADR-0022` exclui** em `J14` e §7.3. Promulgar `V2` faria `FND-01` carregar afirmacao que um `ADR` **`M1`** contradiz e **nao pode ser corrigido para concordar** — achado **`RD-45`**, **encontrado por construir o cumulativo e comparar**, nao por reler. **§5.4 corrige `FND-10 §8.5` na causa:** **seis** valores, e nao os tres de `RD-27` — o denominador do acervo, o percentual derivado e a nota de `CE-05` **nunca haviam sido contados**, achado **`RD-46`** —, e a secao recebe **regra de leitura** que **vincula cada valor a baseline em que vale**, para que envelheca como historico datado em vez de virar afirmacao falsa. **Os valores sao os de `BL-2026-07-29-10` de proposito:** citar as 493 linhas projetadas de `FND-01` tornaria `FND-10` **dependente** da aprovacao de `FND-01`, quebrando a exigencia de bloqueio isolado. **`0` campos, regras, titulares, portoes, papeis, classes, verbos, entidades ou tipos documentais criados · `0` bytes em `IR-03`, com `RD-43` permanecendo aberto e declarado · `0` ampliacao do nucleo obrigatorio · `0` excecoes formais · `0` bytes em `ADR-0021`, `ADR-0022`, `MSG`, `FIT` e baselines · 8 niveis de hierarquia antes e depois.** **Nao vigora sem ato** (FND-01 §9). |
