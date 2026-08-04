---
id: RFC-0028-sede-e-instituicao-do-framework-de-skills
titulo: Instituir o Framework de Skills — onde a norma nasce, sob que classe, e por que a sede nao e FND agora
tipo: rfc
versao: 1.0.0
status: aprovado
camada_memoria: nao-aplicavel
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-08-03
atualizado_em: 2026-08-03
revisao_prevista: null
decisoes_relacionadas: [ADR-0003, ADR-0021, ADR-0022, ADR-0032, ADR-0033]
substitui: []
substituido_por: null
classe_mudanca: C2
prazo_analise: 2026-08-03
---

# RFC-0028: Sede e instituicao do Framework de Skills

## Proposito

Propor a **instituicao** da norma da `Skill` — `SK-01` a `SK-26` — e decidir **onde ela
nasce**: dentro de um `ADR` *(sede `M1`)* ou promovida a `FND` *(sede `M2`)*. As duas sao
custos distintos, e confundi-las **ja custou retrabalho medido no precedente da `Spec`**.

## Escopo

| Item | Definicao |
|---|---|
| **Inclui** | A instituicao de `SK-01` a `SK-26`; a **determinacao de classe** por norma citada; a **sede** e o regime de mutabilidade que dela decorre; a correcao declarada que a sede impoe ao candidato |
| **Nao** inclui | A **entidade `SKL`** *(`FND-03 §3.5`, `FND-09 §E-13` — inalteradas)* · o **template** `TPL-skill` *(inalterado — o defeito medido fica registrado, nao corrigido)* · a **liberacao de `GO-TO-SKILLS`** *(ato de autoridade, `FND-01 §6.2`)* · a criacao de **qualquer `Skill`** · os **outros quatro candidatos** · qualquer emenda a `foundation/` |
| Origem do merito | Candidato redigido **fora do acervo** na Missao 1.14, `253` linhas, `SK-01` a `SK-26` |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| **Propoe** | **DEP-GOV** | `FND-09 §8.2` linha `ADR` — *qualquer DEP* |
| **Revisa** | **revisor independente + DEP-QAR** | `FND-09 §8.2` linha `ADR`; `AC-03` |
| **Aprova** | **DEP-EXE**, com **parecer de DEP-GOV** | `FND-04 §2.1`, linha `C2` |
| **Ratifica** | **—** | `C2 · Tipo 2` **nao exige ratificacao** (`FND-04 §2.1`, `§2.2`; `FND-09 §8.2` linha `ADR`) |

## 1. Situacao atual — fatos verificaveis

| Fato | Medida |
|---|---|
| `Skill` tem entidade, prefixo, local canonico e template | `FND-03 §3.5`; `FND-09 §E-13`; `TPL-skill` |
| `Skill` **nao tem contrato** | Nenhuma fonte responde o que uma `Skill` deve conter para ser aceita |
| `Skill`s existentes | **`0`**. `skills/` **nao existe** |
| Classe de criacao de `Skill` | **`C2`**, e `FND-09 §8.2` linha `SKL` poe **`—`** em *Ratifica* — **nunca** exige ato |
| Pre-condicao de Produto | **Nao ha.** `FND-04 §6` linha *Skill* exige *"procedimento se repete; resultado verificavel; usavel por mais de um papel"* — **e nao *"Produto existe"*** |
| Posicao na Sequencia | **Primeiro item da cadeia**, por decisao do Fundador de 2026-08-03 |

## 2. Problema

**A `Skill` e o unico componente do acervo cuja norma o proprio acervo nomeia quatro vezes
como *"o portao seguinte"* e que nunca teve contrato escrito.** Sem contrato, a primeira
`Skill` nasceria como `ADR-0021 §1` descreve para a `Spec`: *"tinha tipo, entidade,
definicao, autoridade e template, e nao tinha contrato"* — a causa medida de quatro achados
em quatro missoes consecutivas.

## 3. Pergunta de decisao

**Duas, e sao independentes:**

1. **Instituir `SK-01` a `SK-26`?**
2. **Onde:** dentro de um `ADR` *(`M1`)*, ou promovido a `FND` *(`M2`)*?

## 4. Criterios de avaliacao

| # | Criterio |
|---|---|
| `K1` | **Nao criar** entidade, tipo, template, portao, papel, classe, verbo de autoridade ou campo novo |
| `K2` | **Nao emendar fonte alguma** — `0` bytes em `foundation/` |
| `K3` | **Custo de rito proporcional ao efeito** (`AL-01`, `FND-04 §6.1`) |
| `K4` | **Nao canonizar o que nao foi observado** — a licao de `L1` de `FND-11 §14` e de `RD-107` |
| `K5` | **Sede declarada com o tradeoff no sentido correto**, e nao no sentido que convem |

## 5. Opcoes

### 5.1 Opcao A — instituir em `ADR`, `C2 · Tipo 2` *(recomendada)*

**Rito:** esta `RFC` → `ADR-0033` → `FIT` → `PT`. **Sem ato do Soberano.**
**Precedente identico, conferido no frontmatter e nao de memoria:** `ADR-0021`
*(`classe_mudanca: C2`, `tipo_decisao: 2`, `aprovador: DEP-EXE`,
`ratificacao: nao-exigida`)*, cuja cadeia foi `RFC-0017` → `ADR-0021`, com `FIT-2026-015`.

**Custo declarado, e ele e real:** o `ADR` e **`M1`** — `FND-10 §6.2` lista `M2` como
*"FND, CAP, Cartas, SPC, SKL, WFL, TOL, TPL, MEM"*, e **`ADR` nao consta**. **`M1` nunca se
emenda** (`AC-10`, `CC-01`): corrigir uma virgula exige **`ADR` sucessor**. **E exatamente o
custo que `ADR-0021` pagou, e que `ADR-0022` depois desfez ao promover a `FND-11`.**

### 5.2 Opcao B — promover direto a `FND`

**Rito:** `RFC` `C3` → `ADR` `C3 · Tipo 1` → **ato do Soberano** → emenda de `FND-03`/`FND-09`
para receber a sede. **Custo: ato, e a sede so vigora com ratificacao** (`LM-02`).

**Recusada, e por `K4` antes de por custo.** A norma **nunca foi exercida**: `0` Skills
existem, e as **26** regras sao *determinadas, nao observadas*. Canonizar em sede
fundacional **antes** do primeiro exercicio repete o que `L1` de `FND-11 §14` registrou e o
que `RD-107` mediu — **a sede mais protegida e tambem a mais cara de mudar**, e paga-la sobre
norma nao observada e pagar duas vezes se ela precisar mudar.

### 5.3 Opcao C — nao instituir

**Recusada.** O candidato ja existe e custa `0` fora do acervo, mas **sem admissao ele nao
obriga ninguem**, e a primeira `Skill` nasceria sem contrato — o problema de §2.

## 6. Recomendacao do proponente

**Opcao A.** Ela satisfaz `K1` a `K5`: **`0`** criacoes *(§7)*, **`0`** bytes em fonte,
custo minimo do rito que a classe exige, e **nao canoniza o nao observado**. **A sede pode
ser promovida depois**, pelo caminho que `ADR-0022` ja percorreu — e a promocao **nao e
pre-requisito** da instituicao.

## 7. Impacto previsto

| O que muda | Medida |
|---|---|
| Artefatos criados | **4** — `RFC-0028`, `ADR-0033`, `FIT-2026-026`, `PT-2026-020` |
| Entidades, tipos, templates, diretorios, papeis, portoes, verbos | **`0`** |
| **Campos novos** | **`0`** — e o ponto e medido: **`FND-09 §E-13` ja declara `gatilho`** duas vezes, em *Relacionamentos validos* *(`e-acionada-por` gatilho declarado)* e em ***Atributos minimos*** *(Universal + `capabilities`, **gatilho**, entradas, passos, saidas, criterio de verificacao)*. `SK-06` **recebe**, nao institui. `AC-07` satisfeito |
| Bytes em `foundation/` | **`0`** |
| `Skill`s criadas | **`0`** |
| `GO-TO-SKILLS` | **NAO liberado, NAO exercido** — `FND-01 §6.2` |

## 8. Riscos

| # | Risco | Mitigacao |
|---|---|---|
| `R1` | **Sede `M1`: corrigir defeito custa `ADR` sucessor** | **Declarado, nao mitigado.** E o tradeoff da opcao escolhida, e esta escrito no sentido correto |
| `R2` | **A norma e determinada, nao observada** — `0` Skills | Declarado em `SK` `L1`. O gatilho de revisao e a **primeira Skill real** |
| `R3` | **`TPL-skill` nao produz `Skill` conforme** — omite `gatilho` **e** `capabilities` | **Registrado e nao sanado** *(`AS-1`/`RD-122`)*; §9 responde se impede |
| `R4` | Ler a instituicao como liberacao do portao | `ADR-0033` declara expressamente que **nao libera** |

## 9. Perguntas em aberto — e uma delas o despacho manda responder

**`Q1` — `AS-1` impede a `Skill` de funcionar?** **Nao, e a resposta tem duas partes que nao
se confundem.** **(a)** O **Framework** nao usa `TPL-skill`: ele nasce em `ADR`, e sua
conformidade nao depende do template. **(b)** Uma **`Skill`** gerada pelo template vigente
nasceria **sem `gatilho` e sem `capabilities`** no frontmatter, contra os *atributos minimos*
de `FND-09 §E-13` — logo **nao conforme**, com veto de `DEP-GOV` por `AC-06`. **Mas o
template e esqueleto de partida, nao esquema que impeca acrescimo:** os dois campos sao
**exigidos pela norma** e podem ser escritos a mao, e faze-lo **nao cria campo novo**
(`AC-07`). **Conclusao: `AS-1` nao impede; encarece e torna erro provavel.** E a instituicao
**melhora o quadro**, porque `SK-06` passa a exigir `gatilho` **citando a fonte**, tornando a
omissao do template visivel e vinculante.

**`Q2` — a sede promove depois?** Fica **em aberto**, sem gatilho fixado aqui: e decisao de
quem detiver a materia quando a primeira `Skill` real exercer as 26 regras.
