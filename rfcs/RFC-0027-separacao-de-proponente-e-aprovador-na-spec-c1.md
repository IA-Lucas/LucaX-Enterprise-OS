---
id: RFC-0027-separacao-de-proponente-e-aprovador-na-spec-c1
titulo: Como separar quem propoe de quem aprova uma Spec em C1 — onde emendar, e ate onde
tipo: rfc
versao: 1.0.0
status: aprovado
camada_memoria: nao-aplicavel
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-08-02
atualizado_em: 2026-08-02
revisao_prevista: null
decisoes_relacionadas: [ADR-0019, ADR-0021, ADR-0022, ADR-0031, ADR-0032]
substitui: []
substituido_por: null
classe_mudanca: C3
prazo_analise: 2026-08-02
---

# RFC-0027: Separacao de proponente e aprovador na `Spec` de classe `C1`

## Proposito

Submeter a analise **uma** pergunta que a Missao 1.13.5.1 nao pode resolver por presuncao:
**onde** se emenda para que uma `Spec` de classe `C1` tenha proponente e aprovador distintos —
e **ate onde** essa emenda alcanca. O defeito e `RD-91`, medido e registrado por
[PT-2026-017 §6.2](../governance/relatorio-transicao-2026-08-02-primeira-spec.md); ele nao e
opiniao, e a duvida nunca foi *se* sanar, e sim **em que documento e com que largura**.

## Escopo

| Item | Definicao |
|---|---|
| **Inclui** | A celula *Aprovacao* × `C1 · T2` para o tipo `SPC` · a **sede** dessa celula *(fonte contra projecao)* · a **largura** da emenda *(so `SPC`, ou tambem os outros tipos com o mesmo defeito)* · a **propagacao obrigatoria** as Cartas que a emenda torna falsas (`CV-04`) |
| **Nao** inclui | `DoR`, `DoD`, criterio de aceite ou **qualquer** regra de conteudo de `Spec` — `SF-01` a `SF-09` e `SF-11` a `SF-32` ficam **intactos** · a **reclassificacao de `SPC-001`**, que nasceu `C2` validamente · a celula `C0 · T2` · as linhas `PRJ` e `TPL` de `FND-09 §8.2` · `E2`, `Q3`, `Q4`, `RD-88`, `RD-90` · criar `Spec`, `Produto` ou `Capability` |
| **Subordinado a** | [FND-01 §10](../foundation/01-constituicao.md) *(hierarquia normativa)* · [FND-04 §2](../foundation/04-governanca.md) e **§3.1** · [FND-09 §8.2](../foundation/09-meta-model.md) · [FND-11 §5](../foundation/11-framework-specifications.md) e `SF-32` |
| Origem | Despacho da Missao 1.13.5.1; achado **`RD-91`**, dono **SOBERANO** |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| **Propoe / autor** | **DEP-GOV** | [FND-09 §8.2](../foundation/09-meta-model.md), linha `FND` — *propoe/cria*. **Nao e escolha:** a matriz atribui a proposicao de `FND` exclusivamente a DEP-GOV |
| **Materia** | **DEP-PRD** *(dono do tipo `SPC`)* e **DEP-EXE** *(titular que recebe a aprovacao `C1`)* | FND-09 §8.2, linhas `SPC` e `DEP`. **Consulta obrigatoria** — sao os dois Departamentos cujas Cartas mudam |
| **Revisor independente** | **DEP-QAR** | FND-09 §8.2, linha `FND` — *revisa*; `RM-06b` |
| **Aprova e ratifica** | **SOBERANO** | **C3.** Indelegavel (FND-04 §2; FND-09 §8.2, linha `FND`; `SF-32`; `LM-02`) |

> **Residuo declarado (`PI-10`), e ja tem nome.** O autor desta RFC e **DEP-GOV**, que e
> tambem o **Guardiao** — `FND-04 §3.1` poe *"Guardiao ≠ Proponente (ES-02)"*. A concentracao
> **volta por determinacao da matriz**, nao por conveniencia: `FND-09 §8.2` nomeia **um unico**
> proponente para `FND`. E o achado **`RD-39`**, familia `RC-02`, **nona ocorrencia, declarada
> e nao resolvida**. Mitigacao real e nao suficiente: **DEP-PRD e DEP-EXE sao consulta
> obrigatoria**, **DEP-QAR revisa**, e **o merito nao e de DEP-GOV** — ele foi medido por
> DEP-PRD na Missao 1.13.5 e esta em `PT-2026-017 §6.2`.

## 1. Situacao atual — fatos verificaveis

| # | Fato | Fonte, verificavel por terceiro |
|---|---|---|
| `F1` | Para `SPC`, **DEP-PRD** e quem **propoe/cria** e quem **aposenta** — logo, o proprietario | [FND-09 §8.2](../foundation/09-meta-model.md), linha `SPC`, colunas *Propoe/cria* e *Aposenta* |
| `F2` | Em `C1`, o aprovador e o **proprietario do artefato**, com revisor de papel distinto | [FND-04 §2](../foundation/04-governanca.md), bloco `C1`; **§2.1**, linha `C1` |
| `F3` | *"`Proponente ≠ Aprovador` (PI-05)"* e *"Acumulo indevido de papeis torna a aprovacao **nula** (`LV-03`)"* | [FND-04 §3.1](../foundation/04-governanca.md). `LV-03` e **Linha Vermelha de `FND-01`**, nivel **1** da hierarquia |
| `F4` | `F1` + `F2` ⇒ `Proponente = Aprovador` para **toda** `Spec` `C1` ⇒ aprovacao **nula** por `F3` | Composicao das tres fontes vigentes. E `RD-91` |
| `F5` | **`C1` e o piso** que `FND-04 §6` fixa para criar `Spec` — logo o piso e **inutilizavel** | [FND-04 §6](../foundation/04-governanca.md), linha *Spec*; `SF-10` chama `C1` de piso |
| `F6` | `SPC-001` nasceu em **`C2 · Tipo 2`** para contornar, ao custo de **3** artefatos que nao vieram da materia | [ADR-0031 §5](../decisions/ADR-0031-primeira-spec-governanca-de-dado-pessoal-do-nxtrack.md); [PT-2026-017 §4](../governance/relatorio-transicao-2026-08-02-primeira-spec.md) |
| `F7` | A celula de `FND-11 §5` **nao tem merito proprio**: *Proposta* = `DEP-PRD` reproduz `FND-09 §8.2` linha `SPC`, e *Aprovacao* = `proprietario + revisor` reproduz `FND-04 §2.1` linha `C1` — **literais nas duas** | Confronto literal das tres tabelas, feito nesta missao |
| `F8` | `FND-11 §5` e **projecao declarada** (`PJ-02`); em divergencia **prevalece a fonte** (`PJ-03`), e sobre **autoridade** prevalece sempre o documento de origem | [FND-10 §6.1 `PJ-03`](../foundation/10-artifact-framework.md); [FND-01 §10](../foundation/01-constituicao.md), precedencia interna do nivel 2 |
| `F9` | O mesmo colapso existe em **`FND-09 §8.2` linha `PRJ`** *(DEP-EXE propoe **e** aprova)* e **linha `TPL`** *(DEP-GOV propoe, revisa **e** aprova)* | Leitura direta da matriz. **Medido nesta missao**; `0` achados anteriores o registravam |
| `F10` | `ADR-0019` ja **recusou** fixar `DEP-EXE` na celula *Aprova* *(Alternativa B, criterio `K3`)* e ja **recusou** emendar `FND-04 §6` *(Alternativa D, criterio `K6`)* — esta virou **`RD-18`, aberto** | [ADR-0019 §4](../decisions/ADR-0019-aprovador-e-ratificador-de-spec.md) |
| `F11` | `ADR-0019` fixou que **fonte e projecao mudam na mesma mudanca** *(Alternativa E recusou emendar so a fonte)* | [ADR-0019 §4](../decisions/ADR-0019-aprovador-e-ratificador-de-spec.md); `CV-04` |
| `F12` | **2 Cartas ratificadas** afirmam hoje que a aprovacao `C0`/`C1` de `Spec` e do proprietario: **DEP-PRD** *(4 linhas)* e **DEP-EXE** *(2 linhas)* | `departments/prd/carta.md` §4, §5, §5.1 e §7; `departments/exe/carta.md` §5 e §7. **Medido linha a linha** |

## 2. Problema

**O defeito e certo; a sede nao era.** `RD-91` foi registrado como defeito de `FND-11 §5`, e
`PT-2026-017` disse, com razao, que *"sanar `SF-10` exige emendar `FND-11`"*. **`F7` e `F8`
mostram que emendar so `FND-11` nao sana**: a celula reproduz duas fontes, e a norma manda a
fonte prevalecer. Uma emenda confinada a projecao produziria **divergencia**, que `PJ-03`
chama de *defeito da projecao* — trocaria um defeito por outro.

**E `F9` acrescenta uma pergunta que ninguem tinha feito:** se o mesmo colapso esta em outras
duas linhas da mesma tabela, a emenda deve alcanca-las?

## 3. Pergunta de decisao

> **`P1` — Onde se emenda para separar proponente de aprovador na `Spec` `C1`, e com que
> largura: so a linha `SPC` da fonte, a regra generica de `FND-04 §2`, ou o piso de
> `FND-04 §6`?**

## 4. Criterios de avaliacao

| # | Criterio | Origem |
|---|---|---|
| `K1` | **Sanar na fonte**, nao na projecao — a emenda tem de produzir efeito | `PJ-03`; `FND-01 §10`; e o `K1` de `ADR-0019` |
| `K2` | **Nao ampliar titular** — nenhum nome que ja nao esteja em `FND-04 §2` | `K2` de `ADR-0019`; `AU-03` |
| `K3` | **Nao reabrir o merito das classes** de `FND-04 §2` | `K3` de `ADR-0019` |
| `K4` | **Nao encarecer a `Spec`** — o objetivo declarado e tornar `C1` utilizavel, nao empurrar tudo para `C2` | Despacho da 1.13.5.1; `CE-01` |
| `K5` | **Nao tocar regra de conteudo de `Spec`** — `DoR`, `DoD` e criterio de aceite ficam intactos | Despacho da 1.13.5.1; foi o que produziu valor em `SPC-001` |
| `K6` | **Propagar na mesma mudanca** o que a emenda tornar falso | `CV-04`; `F11`; licao de `RD-31` |
| `K7` | **Nao emendar fundacional alem do necessario** a esta celula | Despacho da 1.13.5.1; `FND-04 §6.1` |

## 5. Opcoes

### Opcao A — Emendar **so** `FND-11 §5` *(a celula que o achado nomeia)*
Trocar `proprietario + revisor` por outro titular **apenas na matriz de `SF-10`**.
**Falha `K1`, e a falha e medida:** por `F7` a celula reproduz `FND-04 §2.1` e `FND-09 §8.2`;
por `F8` a fonte prevalece. **A emenda nao sanaria: criaria divergencia.**

### Opcao B — Emendar `FND-09 §8.2`, linha `SPC`, coluna *Aprova*, **+ cascata** *(escolhida)*
A celula passa de `conforme classe (FND-04 §2)` para
**`conforme classe (FND-04 §2); em C1, DEP-EXE`**, com **nota** que declara a derivacao: nao
redefine `§2`, **aplica `§3.1`** ao unico caso em que a propria matriz torna o default de `§2`
impossivel. Cascata obrigatoria em **`FND-11 §5`** (`F11`) e propagacao as **2 Cartas** (`K6`).
**Satisfaz `K1` a `K7`.**

**Sobre a colisao aparente com `F10`.** `ADR-0019` recusou fixar `DEP-EXE` **na celula inteira**,
porque *"tornaria toda Spec `C2`, inclusive as `C0` e `C1`"*. **Esta opcao nao faz isso:** a
remissao a classe **permanece**, `C0` **nao e tocado**, e a classe `C1` **continua `C1`** — com
Nota de Decisao, sem `RFC`, sem `ADR`, sem `FIT` e sem ratificacao. Muda **quem assina**, nao
**o que se exige**. A objecao de `K3` era ao **excesso**; a reserva e ao **exato**.

### Opcao C — Emendar a regra generica de `FND-04 §2`/`§2.1` *(linha `C1`)*
Faria a separacao valer para **todos** os tipos e sanaria `PRJ` e `TPL` junto (`F9`).
**Recusada: falha `K3` e `K7`.** Reabre o merito das classes — exatamente o que `ADR-0019`
recusou — e emenda a norma de governanca inteira para corrigir uma linha. **O ganho e real e
a largura e do Fundador, nao do proponente**: por isso `PRJ` e `TPL` saem daqui como
**achados com dono e gatilho**, nao como omissao.

### Opcao D — Elevar o piso de `FND-04 §6`, linha *Spec*, de `C1` para `C2`
Uma celula, uma fundacional, **`0` Cartas tornadas falsas**, e **fecharia `RD-18`** junto.
**Recusada: falha `K4` frontalmente.** Toda `Spec` passaria a custar **5** artefatos em vez de
**2**. Resolve a nulidade **abolindo o degrau barato**, que e o oposto do que se pediu.

### Opcao Z — Nao emendar
**Recusada.** Toda `Spec` seguiria nascendo em `C2` para nao nascer nula, e o piso que
`FND-04 §6` fixa seguiria **inutilizavel** (`F5`). O contorno existe e esta exercido, mas
contorno exercido **nao e norma sanada**.

## 6. Recomendacao do proponente

**Opcao B.** E a unica que satisfaz `K1` *(sana na fonte)* e `K4` *(nao encarece)* ao mesmo
tempo. `A` nao produz efeito, `C` excede a largura autorizada e `D` compra a correcao com o
preco que a missao existe para evitar.

**Largura recomendada, e ela e estreita por escolha declarada:** **`SPC` apenas.** `C0 · T2`,
`PRJ` e `TPL` ficam **abertos, medidos e com dono** — `RD-91` *(parcial)*, `RD-96` e `RD-97`.
**Declarar e mais barato que corrigir errado**, e a largura e decisao do Soberano.

## 7. Impacto previsto

| Dimensao | Impacto |
|---|---|
| Fundacionais emendadas | **2** — `FND-09` **1.5.0 → 1.6.0** *(1 celula + 1 nota)*, `FND-11` **1.0.0 → 1.1.0** *(1 celula + 1 nota + fonte da `PJ-02`)* |
| Cartas emendadas | **2** — `DEP-PRD` **1.1.0 → 1.2.0** *(4 linhas)*, `DEP-EXE` **1.1.0 → 1.2.0** *(2 linhas)* |
| Celulas de `FND-09 §8.2` alteradas | **1** de 126 |
| Celulas da matriz de `SF-10` alteradas | **1** de 50 |
| Titulares criados | **`0`** — `DEP-EXE` ja aprova `Spec` `C2` na mesma linha |
| Regras `SF-*` alteradas em texto normativo | **`0`** |
| `FND-04` | **`0` bytes** |
| Custo da segunda `Spec` | de **5** artefatos para **2** *(instrumentos do rito)* / **3** *(contando o registro de missao)* |
| `SPC-001` | **inalterada** — nasceu `C2` validamente, e a emenda **nao retroage** |

## 8. Riscos

| # | Risco | Prob. | Impacto | Mitigacao, e o sinal de que se realizou |
|---|---|---|---|---|
| `R1` | **Ler a emenda como redefinicao de `FND-04 §2`**, transformando `FND-09 §8.2` em fonte de autoridade | Media | **Alto** | A nota da celula declara, em texto, que **aplica `§3.1`** e nao redefine `§2`. Sinal: alguem citar `FND-09 §8.2` como fonte de classe |
| `R2` | **`DEP-EXE` acumular portao e aprovacao** em `C1` | Media | Medio | Ja e assim em `C2` na mesma matriz, e `ADR-0019 H3` separou os atos. `I-10` da Carta de DEP-EXE permanece. Sinal: `QG-1` liberado sem registro de responsavel e data |
| `R3` | **`PRJ` e `TPL` ficarem esquecidos** por terem sido declarados e nao corrigidos | **Alta** | Medio | `RD-96` e `RD-97` nascem com dono e gatilho explicitos. Sinal: criar um `PRJ` ou emendar um `TPL` sem que o achado seja citado |
| `R4` | **Divergencia com `ADR-0021 §5.3`**, artefato `M1` que nunca se emenda | **Certa** | Baixo | Declarada em `FND-11 §2` e em `RD-98`; `ADR-0022 §5.4` ja poe `FND-11` como sede. Sinal: alguem resolver a autoridade pela copia de `ADR-0021` |

## 9. Perguntas em aberto

| # | Pergunta | Quem responde |
|---|---|---|
| `Q1` | A largura fica em **`SPC`**, ou o Soberano quer `PRJ` e `TPL` no mesmo ato? | **SOBERANO** |
| `Q2` | `C0 · T2` colapsa pela identica razao. Sanar `C0` agora, ou manter declarado? | **SOBERANO** |
| `Q3` | `FND-04 §2` C3 manda registrar *"nova versao **MAIOR** do documento"*, e **4** emendas `C3` conferidas uma a uma produziram versao **MENOR**, por `AL-01` — `ADR-0017` e `ADR-0019` em `FND-09` *(1.4.0, 1.5.0)*, `ADR-0022` e `ADR-0024` em `FND-01` *(1.6.0, 1.7.0)*. Qual prevalece? | **DEP-GOV**, com homologacao do Soberano — achado `RD-99` |

## 10. Manifestacoes

| Area | Manifestacao | Registro |
|---|---|---|
| **DEP-PRD** *(materia; perde a aprovacao `C1`)* | **De acordo.** Nao perde materia: segue autor, proponente e proprietario, e segue decidindo escopo e criterio de aceite (`FND-01 §7.3`). O que sai e um papel que **`LV-03` ja lhe vedava de fato** | Carta 1.2.0, §5.1 e §7 |
| **DEP-EXE** *(recebe a aprovacao `C1`)* | **De acordo.** `C1` e degrau abaixo de `C2`, que ja aprova desde `ADR-0019`. `I-10` intacto: aprovar nao e redigir | Carta 1.2.0, §5.1 e §7 |
| **DEP-QAR** *(revisor)* | **De acordo, com a ressalva `R3`** — declarar `PRJ` e `TPL` sem corrigi-los deixa dois defeitos vivos na mesma tabela que se esta emendando | [FIT-2026-025](../governance/fitness/FIT-2026-025-emenda-de-sf-10.md), ressalva `S2` |
| **DEP-GOV** *(guarda)* | Classe **`C3`** validada; forma conferida; residuo `RD-39` declarado em §Responsaveis | Esta RFC |

## 11. Resultado

**APROVADA** — segue para [ADR-0032](../decisions/ADR-0032-separacao-de-proponente-e-aprovador-na-spec-c1.md),
que decide pela **Opcao B**. A eficacia depende de **ato do Soberano**
([PS-2026-017](../governance/pacote-soberano-2026-08-02-rd-91.md)); **nada foi aplicado,
ativado ou ratificado por esta missao**.

---

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-08-02 | DEP-GOV | Criacao. Submete **`P1`** — onde e com que largura se emenda para separar proponente de aprovador na `Spec` `C1`. **4 opcoes reais + `Z`**, das quais **`A` e recusada por medicao**, nao por preferencia: a celula que `RD-91` nomeia **reproduz literalmente** `FND-09 §8.2` linha `SPC` e `FND-04 §2.1` linha `C1`, e `PJ-03` com `FND-01 §10` fazem a fonte prevalecer. Recomenda a **Opcao B** — emendar a fonte, com cascata em `FND-11 §5` e propagacao a **2** Cartas ratificadas cujas **6** linhas ficariam falsas ou incompletas, medidas uma a uma. Declara **`F9`**: o mesmo colapso existe nas linhas **`PRJ`** e **`TPL`** de `FND-09 §8.2`, **fora de `SPC`** — e **nao** as corrige, por `K7`. **`0` regras de conteudo de `Spec` tocadas · `0` titulares criados · `0` bytes em `FND-04` · `SPC-001` nao reclassificada.** |
