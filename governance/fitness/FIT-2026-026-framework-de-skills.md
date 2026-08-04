---
id: FIT-2026-026-framework-de-skills
titulo: Verificacao de aptidao — instituicao do Framework de Skills (ADR-0033)
tipo: fitness-check
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: DEP-QAR
proprietario: DEP-QAR
aprovador: DEP-EXE
criado_em: 2026-08-03
atualizado_em: 2026-08-03
revisao_prevista: null
decisoes_relacionadas: [ADR-0021, ADR-0022, ADR-0033]
substitui: []
substituido_por: null
veredito: apto-com-ressalva
---

# FIT-2026-026 — Framework de Skills

**Objeto avaliado:** [`ADR-0033`](../../decisions/ADR-0033-framework-de-skills.md), que institui
`SK-01` a `SK-26`. **Portao correspondente:** `QG-6`. **Obrigatorio** por ser `C2`
(`FND-03 §3.14`; `CC-04`).

> **`FT-02` e `LV-03`:** o executor desta verificacao e **DEP-QAR**, e **nao** produziu o
> artefato avaliado. **`FT-10`:** este e **parecer**, nao decisao — nao se ratifica.

## Veredito

**`apto-com-ressalva`.** A ressalva e **uma**, e ela **nao bloqueia**: `R1`.

## 1. A pergunta de `QG-6` — a arquitetura ficou mais apta a evoluir?

**Sim**, e o sinal e observavel: antes de `ADR-0033`, **`0`** fontes respondiam o que uma
`Skill` deve conter para ser aceita; depois, **1** responde, e ela **cita a fonte de cada
exigencia**. A `Skill` sai da configuracao que `ADR-0021 §1` diagnosticou como causa de
quatro achados — *"tinha tipo, entidade, definicao, autoridade e template, e nao tinha
contrato"*.

## 2. Conformidade — cada resposta com sinal observavel

| # | Verificacao | Sinal | Resultado |
|---|---|---|---|
| `F1` | **Classe determinada por norma citada, nao por analogia** | `ADR-0033` cita `FND-04 §2.1`, `§2.2`, `FND-09 §8.2` linha `ADR` e `AL-01`, celula a celula | ✅ |
| `F2` | **Precedente conferido na fonte, nao de memoria** | `ADR-0021` tem `classe_mudanca: C2`, `tipo_decisao: 2`, `ratificacao: nao-exigida` — lido no frontmatter | ✅ |
| `F3` | **`0` entidades criadas** | `FND-03 §3.5` e `FND-09 §E-13`/`§8.2`: `0` linhas acrescentadas | ✅ |
| `F4` | **`0` campos novos** *(`AC-07`)* | `FND-09 §E-13` ja lista `capabilities` e `gatilho` como **atributos minimos**, e a relacao `e-acionada-por` gatilho declarado. `SK-06` **recebe** | ✅ |
| `F5` | **`0` portoes criados ou liberados** | `QG-0`–`QG-6`: **7 antes, 7 depois**. `GO-TO-*`: **2 antes, 2 depois**. `GO-TO-SKILLS` **nao liberado** | ✅ |
| `F6` | **`0` bytes em fonte normativa** | `foundation/` conferido por `diff -rq` contra copia datada | ✅ |
| `F7` | **Autoverificacao** *(`AC-03`, `RM-06b`)* | `ADR-0033`: `autor` **DEP-GOV**, `revisor` **DEP-QAR**, `aprovador` **DEP-EXE** — tres papeis distintos | ✅ |
| `F8` | **A alteracao de merito esta ISOLADA e DECLARADA** | **1 de 26** — `SK-26`, `M2` → `M1`, com o fundamento `FND-10 §6.2` citado e a tabela comparativa | ✅ |
| `F9` | **O tradeoff da sede esta no sentido correto** | `ADR-0033` declara que a sede barata e **a mais cara de corrigir**, e nao o contrario | ✅ |
| `F10` | **Nao canoniza o nao observado** | A promocao a `FND` foi **recusada por criterio** (`K4` de `RFC-0028`), com `L1` declarado | ✅ |
| `F11` | **Contadores medidos por ferramenta** *(licao de `RD-95`)* | `RFC-0027`→`0028`, `ADR-0032`→`0033`, `FIT-2026-025`→`026`, `PT-2026-019`→`020` | ✅ |
| `F12` | **`TPL-skill` produz `Skill` conforme?** | **NAO.** Omite `gatilho` e `capabilities` do frontmatter, contra os atributos minimos de `FND-09 §E-13`. Medido com **controle positivo** *(`proprietario` = 1)* | ⚠️ **`R1`** |

## 3. A ressalva — `R1`

**`TPL-skill` nao produz `Skill` conforme, e o Framework nao o corrige.**

| Pergunta | Resposta medida |
|---|---|
| **Impede o Framework de existir ou funcionar?** | **Nao.** O Framework nasce em `ADR` e **nao usa** `TPL-skill`. Sua conformidade nao depende do template |
| **Impede a criacao de uma `Skill`?** | **Nao impede — encarece.** Os dois campos sao **exigidos pela norma** e podem ser escritos a mao; faze-lo **nao cria campo novo** (`AC-07`). O template e **esqueleto de partida**, nao esquema que impeca acrescimo |
| **Aumenta a probabilidade de erro?** | **Sim, e e por isso que e ressalva e nao nota.** Quem partir do template **e nao conhecer `FND-09 §E-13`** produzira ficha nao conforme, e o veto de `AC-06` cairia so na revisao |
| **A instituicao melhora ou piora o quadro?** | **Melhora.** Antes, a omissao do template era invisivel; depois, **`SK-06` a torna vinculante e citada**, e a ficha incompleta passa a ser recusavel por regra nomeada |

**Achado correspondente: `RD-122`, ABERTO.** Correcao e **rito de `TPL`** — `DEP-GOV` + dono do
tipo, **`C2`, sem ato** (`FND-09 §8.2` linha `TPL`) — e **missao propria**, por restricao
expressa do despacho que abriu esta.

**`R1` NAO bloqueia**, e a razao e verificavel: **`0` `Skill`s existem**, de modo que **`0`
fichas nao conformes podem ter sido produzidas**. A ressalva incide sobre a **proxima** Skill,
nao sobre esta mudanca.

## 4. Riscos residuais

| # | Risco | Estado |
|---|---|---|
| `RR1` | Sede `M1`: corrigir uma virgula exige `ADR` sucessor | **Declarado** em `ADR-0033`, `L5`. E o custo da opcao, nao defeito |
| `RR2` | **26 regras determinadas e nao observadas** | **Declarado** em `L1`. Gatilho de revisao: **primeira `Skill` real** |
| `RR3` | Ler a instituicao como liberacao de `GO-TO-SKILLS` | **Mitigado por texto expresso** — `N4` de `ADR-0033` |

## 5. Recomendacao

**`QG-6` LIBERADO.** A mudanca deixa a arquitetura **mais apta a evoluir** do que estava, com
`0` criacoes e `0` bytes em fonte.

**DEP-QAR NAO recomenda liberar `GO-TO-SKILLS` nesta mudanca**, e a razao **nao** e a
qualidade do Framework: liberar portao e **ato de autoridade** (`FND-01 §6.2`) e **nao e
materia de parecer** (`FT-10`). **O portao passa a ser exercivel** — a norma existe e a classe
de criacao e `C2` sem ato —, e **exerce-lo e criar a primeira `Skill`**, que e missao propria.
