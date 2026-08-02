---
id: RFC-0020-conformidade-de-contrato-das-fundacionais
titulo: Como fechar RD-27 sem reescrever norma — o backfill de AC-08 em FND-01 e FND-02 e a correcao de FND-10 §8.5
tipo: rfc
versao: 1.0.0
status: aprovado
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-GOV
criado_em: 2026-07-30
atualizado_em: 2026-07-30
revisao_prevista: 2027-01-30
decisoes_relacionadas: [ADR-0009, ADR-0012, ADR-0022]
substitui: []
substituido_por: null
resumo: Submete a forma de fechar RD-27 nos tres objetos que ele alcanca, e mede que FND-10 §8.5 tem cinco valores defasados onde o achado contara tres.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# RFC-0020: Conformidade de contrato das fundacionais

> **Pergunta em uma frase.** `AC-08` obriga cinco campos em todo artefato **emendado apos a
> vigencia de `FND-10`**. **`FND-01` foi emendada quatro vezes e declara um. `FND-02` foi
> emendada tres vezes e declara nenhum.** E **`FND-10 §8.5`**, que mede o custo do nucleo,
> declara numeros de **2026-07-28** como se fossem correntes. Esta RFC pergunta **como
> corrigir os tres sem reescrever uma linha de norma**.

## Proposito

Submeter a **forma** do fechamento de **`RD-27`**. Esta RFC **nao cria campo, nao cria regra,
nao altera `AC-08`, nao altera `IR-03` e nao amplia o nucleo obrigatorio**. O que ela resolve e
**como** cumprir uma obrigacao que ja vigora e **nao esta sendo cumprida por dois documentos de
nivel 1 e 2 da hierarquia normativa** — `AC-06`, ressalva **`R2`** de
[FIT-2026-014](../governance/fitness/FIT-2026-014-regime-ministerial-e-cobertura-de-contexto.md).

## Escopo

| Item | Definicao |
|---|---|
| Inclui | Os **tres** objetos de `RD-27`: **`FND-01`** *(4 campos ausentes)*, **`FND-02`** *(5 campos ausentes)* e **`FND-10 §8.5`** *(valores defasados)* |
| **Nao** inclui | O **merito** de `AC-08`, `AC-06` ou `AC-11`, **nao reabertos** · a **lista fechada de `IR-03`** — altera-la e `C2` com ADR proprio (`IR-04`), e **`RD-43` permanece declarado** · a **ampliacao do nucleo obrigatorio**, que seria `C2` com Fitness Check *(`FND-10 §8.5`)* · `FND-03` a `FND-09` e `FND-11` — **`0` bytes** · as **nove Cartas** — materia de [ADR-0025](../decisions/ADR-0025-extensao-da-propagacao-de-qg-1-as-cartas-restantes.md), rito separado · a **sede** da norma da `Spec` — [ADR-0022](../decisions/ADR-0022-sede-canonica-do-framework-de-specifications.md), pacote separado · `RD-33` *(bloqueante, **nao reaberto**)*, `RD-36`, `RD-13` |
| Origem | Achado **`RD-27`**, [catalogo mestre §7 item 48](../governance/artifact-registry.md); ressalva `R2` de FIT-2026-014; gatilho **disparado** |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| **Propoe / autor** | **DEP-GOV** | [FND-09 §8.2](../foundation/09-meta-model.md), linha `FND` — **proponente unico** |
| **Revisor independente** | **DEP-QAR** | `FND-09 §8.2`, linha `FND`; `RM-06b` |
| Valida a forma | **DEP-GOV** | `FND-09 §8.2`, linha `RFC` |
| **DECIDE a emenda** | **SOBERANO** | **C3. Indelegavel.** **Nao ocorreu** |

> **Residuo declarado (`PI-10`).** `DEP-GOV` **propoe** e **valida a forma** da mesma RFC —
> determinacao de `FND-09 §8.2`, que atribui a linha `RFC` a `DEP-GOV` e a linha `FND` tambem a
> `DEP-GOV`. **A independencia real vem de `DEP-QAR`** *(revisor)* **e do SOBERANO** *(decisor)*,
> nao da validacao de forma. **Nona ocorrencia da familia `RC-02`** — ver `RD-39`.

---

## 1. Situacao atual

`RD-27` esta **ABERTO** desde 2026-07-29 e **nunca foi tocado**, por determinacao expressa de
duas missoes consecutivas. O gatilho registrado e literal:

> *"Proximo ato soberano que alcance `FND-01`, `FND-02` ou `FND-10`"* — `R2` de FIT-2026-014.

**O gatilho ja disparou uma vez e nao foi atendido.** [ADR-0022 §7.3](../decisions/ADR-0022-sede-canonica-do-framework-de-specifications.md)
declarou a colisao entre a determinacao *"nao tratar `RD-27`"* e o gatilho que o proprio ato
dispara, submeteu **duas variantes** de `FND-01` e **recomendou a que nao fecha**. A Missao 1.13.2
recebeu determinacao contraria: **instituir o rito proprio**, e nao trocar um hash na minuta.

## 2. Problema — **medido, e maior do que o achado declarou**

### 2.1 Os campos ausentes, contados campo a campo

| Artefato | Versao | Emendas apos a vigencia de FND-10 | Campos de `AC-08` declarados | **Ausentes** |
|---|---|---|---|---|
| **`FND-01`** | 1.5.0 | **4** *(1.2.0 → 1.5.0)* | `ratificacao` | **4** — `resumo`, `perfil_contexto`, `confidencialidade`, `revisor` |
| **`FND-02`** | 1.3.0 | **3** *(1.1.0 → 1.3.0)* | **nenhum** | **5** — os cinco |
| `FND-03` a `FND-09`, `FND-11` | — | — | — | **0** *(conformes ou nao alcancadas)* |

**`FND-02` e o unico artefato do acervo que nao declara nenhum dos cinco.**

### 2.2 `FND-10 §8.5` — **cinco valores defasados, nao tres**

`RD-27` item *(c)* caracterizou **tres** valores. **A medicao encontrou cinco**, todos na
mesma secao, e **dois deles na mesma frase**:

| # | Valor declarado em `§8.5` | Medido em `BL-2026-07-29-10` | Em `RD-27`? |
|---|---|---|---|
| 1 | `FND-01` **468** | **485** | **Sim** |
| 2 | `FND-03` **619** | **631** | **Sim** |
| 3 | total **1.087** | **1.116** | **Sim** |
| 4 | acervo **18.916** | **51.698** | ❌ **Nao** |
| 5 | **5,7% medido** | **2,2%** | ❌ **Nao** |
| 6 | nota `CE-05`: `FND-09` tem **1.225 linhas** | **1.263** | ❌ **Nao** |

**Achado novo `RD-46`**, severidade **Baixa**, dono **DEP-GOV**. **A causa nao e o numero: e a
ausencia de regra de leitura.** `CE-04` proibe metrica sem fonte e sem valor observado; `§8.5`
tem valor observado, **mas nao diz de quando** — e um numero sem data envelhece virando
**afirmacao falsa** em vez de **registro historico**.

### 2.3 Por que nao foi corrigido antes — a razao e criptografica, e continua valida

`IR-03` e **lista fechada** e **nao** inclui `resumo`, `perfil_contexto`, `confidencialidade`
nem `revisor`. Os quatro **entram em `H-N`**. Acrescenta-los altera o `H-N` de documentos
**promulgados pelo sexto ato soberano**, e `IR-05` determina que divergencia de `H-N` apos o ato
e **alteracao nao ratificada**, *"nao corrigivel por edicao: exige ato novo"*.

**Medido, nao presumido:**

| Objeto | `H-N` em vigor | `H-N` do candidato | Muda? |
|---|---|---|---|
| `FND-01` | `fcb6e4bd…6198` | `f5172f21…e963` | **Sim** |
| `FND-02` | `1dddf9ff…ae6f` | `66d4651b…6a36` | **Sim** |
| `FND-10` | `96ff7418…391b` | `651fbaf0…e146` | **Sim** |

**Logo o caminho e ato soberano, e so ele.** Nao ha versao desta correcao que dispense o ato.

## 3. Criterios de avaliacao — **declarados antes das opcoes**

| # | Criterio | Por que |
|---|---|---|
| **K1** | **Zero linha de norma reescrita** | O defeito e de **declaracao**, nao de conteudo. Reescrever norma para corrigir metadado seria desproporcional |
| **K2** | **Zero valor inventado** | Todo valor tem de vir de fonte ja escrita — catalogo curado, padrao por tipo, matriz de autoridade ou medicao |
| **K3** | **Um unico `FND-01` final** | Duas variantes vivas com hashes distintos e a colisao que a Missao 1.13.2 existe para eliminar |
| **K4** | **Cada objeto bloqueavel isoladamente** | Recusar `FND-02` nao pode arrastar `FND-01` nem `FND-10` |
| **K5** | **Nao recorrer** | Corrigir os numeros sem corrigir a causa garante a terceira ocorrencia |

## 4. Opcoes

### Opcao A — **Backfill nos tres, com regra de leitura em `§8.5`** *(recomendada)*

Os cinco/quatro campos entram no frontmatter com **valor ja escrito em outra fonte**; `§8.5`
recebe os valores medidos **e a regra que vincula cada um a baseline em que vale**.

| K1 | K2 | K3 | K4 | K5 |
|---|---|---|---|---|
| ✅ `0` linhas de corpo | ✅ `0` inventados | ✅ candidato cumulativo unico | ✅ tres objetos independentes | ✅ a causa e corrigida na secao |

### Opcao B — Backfill apenas em `FND-01` e `FND-02`, deixando `§8.5` para depois

Cumpre `AC-08` e **deixa aberto o item *(c)***. **Rejeitada:** o mesmo ato alcanca `FND-10`, e o
gatilho de `RD-27` dispararia de novo no ato seguinte — **quarta ocorrencia**, e desta vez sem
nenhuma determinacao que a explique.

### Opcao C — Emendar `IR-03` para excluir os quatro campos de `H-N`

Tornaria o backfill um `O4`-like sem ato. **Rejeitada, e a razao e `IR-04`:** alterar `IR-03` e
`C2` com ADR proprio, e **`RD-43` mostrou que a lista ja tem uma assimetria nao resolvida**
(`superado_por`). **Mexer na lista para evitar um ato e exatamente o risco `RR-1` de RFC-0009** —
protecao que se dissolve sem que ninguem decida dissolve-la.

### Opcao D — Declarar excecao formal a `AC-06` para os dois documentos

**Rejeitada:** `governance/exceptions/` esta **vazio** desde a fundacao, e abrir a primeira
excecao do acervo para **nao** cumprir um contrato que **se pode cumprir hoje** inverteria o
proposito do instrumento. Excecao e para o que **nao se pode** fazer.

### Opcao Z — **Nao fazer nada**

`AC-06` segue descumprido por dois documentos de nivel 1 e 2; `§8.5` segue afirmando **cinco**
valores falsos; e o gatilho de `RD-27` dispara **em todo ato futuro** que alcance qualquer um dos
tres. **Efeito real e conhecido:** a nao conformidade e **declarada** e os cinco campos tem
**valor padrao** em `FND-10 §2.2` — **ninguem e induzido a erro hoje**. **Nao decidir e resultado
valido**, e o seu custo e a quarta ocorrencia.

## 5. Recomendacao

**Opcao A**, com o candidato de `FND-01` **cumulativo sobre o de `ADR-0022`** — porque os dois
ritos alcancam o mesmo arquivo e **so pode existir um `FND-01` final para o ato**.

## 6. Impacto previsto

| Dimensao | Antes | Depois |
|---|---|---|
| Artefatos nao conformes a `AC-08` | **2** | **0** |
| Valores falsos em `FND-10 §8.5` | **5** | **0** |
| Linhas de **corpo** de norma alteradas | — | **`0`** nos tres |
| Variantes vivas de `FND-01` | **2** *(`V1`, `V2`)* | **1** *(cumulativo)* |
| Regras `AC-*`, `IR-*`, `CE-*`, `PJ-*` criadas ou alteradas | — | **`0`** |
| Nucleo obrigatorio | 4 artefatos | **4 artefatos** — **nao ampliado** |

## 7. Riscos

| # | Risco | Mitigacao |
|---|---|---|
| **RF-1** | O backfill ser lido como **reabertura** das emendas anteriores | `H-N` de corpo inalterado: **`0` bytes** fora do frontmatter e do historico, medido por `diff` |
| **RF-2** | `resumo` divergir do curado no catalogo, criando **segunda fonte** | O valor **e** o curado, literalmente — `PJ-01` respeitado por copia, nao por redacao nova |
| **RF-3** | `§8.5` envelhecer de novo | **A regra de leitura entra na propria secao**, e vincula valor a baseline |
| **RF-4** | `ratificacao: ratificada` em `FND-02` ser lido como autoatribuido | `AC-04`: o preenchimento registra o **ato de 2026-07-29** (`MSG-2026-0006`), e a **1.4.0** so vigora com **novo** ato |

## 8. Perguntas em aberto

| # | Pergunta | Para quem |
|---|---|---|
| **P1** | `C3 · Tipo 1` ou **`Tipo 2`**? A correcao **nao cria sede** e a reversao e byte a byte — mas exige ato nos dois casos | **SOBERANO** |
| **P2** | `RD-46` fecha junto, ou permanece aberto com gatilho proprio? | **SOBERANO** |

## 9. Resultado

**Convertida em [ADR-0024](../decisions/ADR-0024-conformidade-de-contrato-das-fundacionais.md)**,
`C3 · Tipo 2`, submetido em [PS-2026-011](../governance/pacote-soberano-2026-07-30-rd-27.md).
**Esta RFC nao vigora por si.**

## 10. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Achado de origem | **`RD-27`** — [catalogo mestre §7](../governance/artifact-registry.md) |
| Ressalva que fecha | **`R2`** de [FIT-2026-014](../governance/fitness/FIT-2026-014-regime-ministerial-e-cobertura-de-contexto.md) · **`R3`** de [FIT-2026-016](../governance/fitness/FIT-2026-016-canonizacao-e-propagacao.md) |
| Achado que abre | **`RD-46`** — §2.2 |
| Norma aplicada | `AC-06`, `AC-08`, `AC-11` de [FND-10 §2.5](../foundation/10-artifact-framework.md); `IR-01` a `IR-05` de [ADR-0012](../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md) |
| Rito irmao, **independente** | [ADR-0025](../decisions/ADR-0025-extensao-da-propagacao-de-qg-1-as-cartas-restantes.md) — `RD-37` |
| Baseline vigente na submissao | **`BL-2026-07-29-10`** |

---

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-30 | DEP-GOV | RFC da **Missao 1.13.2**. Submete a **forma** de fechar **`RD-27`** nos **tres** objetos que ele alcanca, com **cinco criterios declarados antes das opcoes** e **cinco opcoes**, a de nao fazer nada inclusive. **Mede que `FND-10 §8.5` tem cinco valores defasados onde `RD-27` contara tres** — o denominador do acervo *(18.916 → 51.698)*, o percentual derivado *(5,7% → 2,2%)* e a nota de `CE-05` sobre `FND-09` *(1.225 → 1.263)* **nunca haviam sido contados** — e registra o achado **`RD-46`**, cuja causa e **a ausencia de regra de leitura**, nao o numero. Mede que o `H-N` **muda nos tres** candidatos, confirmando que **nao ha versao desta correcao que dispense o ato**. Recusa **`IR-03`** como caminho, citando `IR-04` e o risco `RR-1` de RFC-0009, e recusa a **primeira excecao formal do acervo** para deixar de cumprir contrato **cumprivel hoje**. Recomenda o candidato de `FND-01` **cumulativo sobre o de `ADR-0022`**, porque **so pode existir um `FND-01` final para o ato**. |
