---
id: PT-2026-020
titulo: Missao 1.13.10 — admissao do Framework de Skills, primeiro item da cadeia sob a ordem nova
tipo: reporte
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-08-03
atualizado_em: 2026-08-03
revisao_prevista: null
decisoes_relacionadas: [ADR-0021, ADR-0022, ADR-0033]
substitui: []
substituido_por: null
resumo: Admite SK-01 a SK-26 em ADR-0033 sob C2 Tipo 2 sem ato, declara os dois custos distintos de instituir e de promover a FND, reconcilia 102 linhas e emite baseline nova pelo IR-BL/4.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
---

# PT-2026-020 — Missao 1.13.10: admissao do Framework de Skills

**Decisao: `ADMITIDO`.**

## 1. Item 0 — a classe, medida e nao presumida

O despacho ordenou medir se o precedente de `ADR-0021` valia aqui, e **parar** se saisse
diferente. **Saiu igual, e por norma citada.**

| Variavel | Valor | Fundamento |
|---|---|---|
| Classe | **`C2`** | `FND-04 §2.1` — `C2` → `RFC` → `ADR`, aprova `DEP-EXE` + parecer `DEP-GOV` |
| Tipo | **`2`** | `FND-04 §2.2`. Norma em `ADR` e **superavel por sucessor** (`CC-06`, `SU-01`) |
| Ratificacao | **nao exigida** | `FND-04 §2.1` *(so se `Tipo 1`)*; `FND-09 §8.2` linha `ADR` |
| Precedente | `ADR-0021` | `classe_mudanca: C2` · `tipo_decisao: 2` · `ratificacao: nao-exigida` — **lido no frontmatter** |

**A medicao que mais importou, e ela quase mudou a classe.** Se o candidato criasse **campo
novo**, `AC-07` seria violado e o efeito deixaria de ser o de `ADR-0021`. **Nao cria:**
`FND-09 §E-13` **ja declara `gatilho` duas vezes** — em *Relacionamentos validos*
(*"`e-acionada-por` gatilho declarado"*) e em ***Atributos minimos*** (*"Universal +
`capabilities`, **gatilho**, entradas, passos, saidas, criterio de verificacao"*). **`SK-06`
recebe; nao institui.**

### 1.1 Os dois custos, declarados separadamente — como o despacho exigiu

| O que se faz | Classe | Ato? | Feito aqui |
|---|---|---|---|
| **Instituir a norma** | `C2 · Tipo 2` | **Nao** | ✅ **sim** |
| **Promover a sede `FND`** | `C3 · Tipo 1` | **Sim** | ❌ **nao** — precedente `ADR-0022` |

**A promocao foi recusada por CRITERIO, nao por economia:** as **26** regras sao
*determinadas e nao observadas* — **`0`** `Skill`s existem —, e canonizar em sede fundacional
antes do primeiro exercicio repete `L1` de `FND-11 §14` e `RD-107`.

**Custo declarado da sede escolhida, e ele e real:** nascendo em `ADR`, o Framework e **`M1`**
(`FND-10 §6.2`, que lista `M2` sem incluir `ADR`). **`M1` nunca se emenda** (`AC-10`,
`CC-01`): corrigir uma virgula exige **`ADR` sucessor**. **E o custo que `ADR-0021` pagou e
que `ADR-0022` desfez.**

## 2. O que foi admitido

**`SK-01` a `SK-26`**, em [`ADR-0033`](../decisions/ADR-0033-framework-de-skills.md), a partir
do candidato de **253** linhas redigido fora do acervo na Missao 1.14.

| Transformacao | Quantas | Quais |
|---|---|---|
| **`T-IDENTICA`** | **25** | `SK-01` a `SK-25` |
| **`T-MERITO-DECLARADO`** | **1** | **`SK-26`** — `M2` → **`M1`** |

**A unica alteracao de merito esta isolada e declarada.** O candidato afirmava *"Este
Framework e `M2`: emenda-se por versao e NAO exige ato"* — **falso para a sede `ADR`**.
Corrigi-la em silencio seria a familia de **`RD-101`**. **A `Skill` — o tipo — continua
`M2`; o que e `M1` e o `ADR`.**

## 3. Custo em artefatos — medido

| Artefato | Linhas |
|---|---|
| [`RFC-0028`](../rfcs/RFC-0028-sede-e-instituicao-do-framework-de-skills.md) | ver §4 do catalogo |
| [`ADR-0033`](../decisions/ADR-0033-framework-de-skills.md) | idem |
| [`FIT-2026-026`](fitness/FIT-2026-026-framework-de-skills.md) | idem |
| **`PT-2026-020`** *(este)* | idem |

**`4` artefatos criados.** Comparacao com os precedentes, medida e nao estimada: a **primeira
`Spec`** custou **5** *(`RFC`, `ADR`, `SPC`, `FIT`, `PT`)*; a **emenda de `RD-91`** custou
**7**; **admitir um Produto** custa **8**. **Este e o rito mais barato ja exercido sobre
materia normativa no acervo** — e a razao e estrutural: **a norma mora dentro do `ADR`**, de
modo que nao ha artefato separado para ela, e **`0` atos sao necessarios**.

## 4. `AS-1` / `RD-122` — registrado e nao sanado, e a pergunta do despacho respondida

**`FND-10 §4.8` recusa criar o tipo `Command` dizendo que ele mora no atributo `gatilho` de
`SKL`/`WFL`. Medido: `TPL-workflow` tem o campo; `TPL-skill` tem `0`.**

**Medicao ampliada nesta missao, e ela agrava o achado:** o problema **nao e so o `gatilho`**.
`FND-09 §E-13` lista como **atributos minimos** de `SKL`: *Universal + `capabilities`,
`gatilho`, entradas, passos, saidas, criterio de verificacao*. **O frontmatter de `TPL-skill`
omite `capabilities` E `gatilho`** — `0` ocorrencias de cada, com **controle positivo**
(`proprietario` = **1**, instrumento vivo). O corpo cobre entradas, passos, saidas e criterio
nas **4** secoes correspondentes.

### **Impede a `Skill` de funcionar? NAO.**

| Pergunta | Resposta |
|---|---|
| Impede o **Framework**? | **Nao.** Ele nasce em `ADR` e **nao usa** o template |
| Impede criar uma **`Skill`**? | **Nao impede — encarece.** Os campos sao **exigidos pela norma** e podem ser escritos a mao; faze-lo **nao cria campo novo** (`AC-07`). O template e **esqueleto de partida**, nao esquema que barre acrescimo |
| Aumenta risco de erro? | **Sim** — quem partir do template sem conhecer `FND-09 §E-13` produz ficha nao conforme, e o veto de `AC-06` so cairia na revisao. **Por isso e ressalva `R1` de `FIT-2026-026`, e nao nota** |
| A admissao piora ou melhora? | **Melhora.** `SK-06` torna a exigencia **vinculante e citada**; antes, a omissao do template era invisivel |

**`RD-122` permanece ABERTO.** Corrigi-lo e **rito de `TPL`** — `C2`, **sem ato** — e **missao
propria**, por restricao expressa. **`0` bytes em `TPL-skill`.**

## 5. Reconciliacao

| O que | Estado |
|---|---|
| Catalogo mestre — §2, §4, contadores, §7, §10 | ✅ na **mesma mudanca** (`CV-04`, `IX-02`) |
| Indices `M3` — `rfcs/README`, `decisions/README`, `governance/README`, `governance/fitness/README` | ✅ na mesma mudanca |
| **Divergencia de 102 linhas** do token 24 | ✅ **RECONCILIADA**, por ordem expressa do despacho |
| Baseline | ✅ **`BL-2026-08-03-02`** — §10.25 do catalogo, `IR-BL/4`, **2** execucoes |

## 6. O que esta missao NAO fez

- **Nao liberou `GO-TO-SKILLS`** — liberar portao e **ato de autoridade** (`FND-01 §6.2`).
  **O portao passa a ser EXERCIVEL** *(a norma existe e criar `Skill` e `C2` sem ato)*, e
  **exerce-lo e criar a primeira `Skill`**, que e missao propria.
- **Nao admitiu os outros quatro candidatos** — seguem fora do acervo, **intactos**.
- **Nao emendou Fundacional** — `0` bytes em `FND-01` a `FND-11`.
- **Nao decidiu `RD-116`**; **nao abriu a missao do item IV**; **nao corrigiu `RD-122`**.
- **Nao criou `Skill` nem `skills/`.**
- **Nao promoveu a `FND`.**

## 7. Achados

**`0` novos.** **`0` fechados.** `RD-122` **confirmado e ampliado** *(de `gatilho` para
`gatilho` + `capabilities`)*, e **nao corrigido**. `RD-123` e `RD-124` inalterados.

## 8. Decisao

**`ADMITIDO`.** O Framework de Skills vigora desde 2026-08-03, em `ADR-0033`,
`ativo` · `ratificacao: nao-exigida`, classe **`C2 · Tipo 2`**, **`0` atos emitidos**.
