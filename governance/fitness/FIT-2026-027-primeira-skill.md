---
id: FIT-2026-027-primeira-skill
titulo: Verificacao de aptidao — a primeira Skill do acervo (ADR-0034)
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
decisoes_relacionadas: [ADR-0033, ADR-0034]
substitui: []
substituido_por: null
veredito: apto-com-ressalva
---

# FIT-2026-027 — A primeira `Skill`

**Objeto avaliado:** [`ADR-0034`](../../decisions/ADR-0034-primeira-skill-copia-datada.md) e
[`SKL-custodia-criar-copia-datada`](../../skills/SKL-custodia-criar-copia-datada.md).
**Portao:** `QG-6`. **Obrigatorio** por ser `C2`.

> **`FT-02`, `LV-03`:** executado por **DEP-QAR**, que **nao** produziu o avaliado.
> **`FT-10`:** parecer, nao decisao — nao se ratifica.

## Veredito

**`apto-com-ressalva`.** Duas ressalvas, **nenhuma bloqueia**: `R1` e `R2`.

## 1. `QG-6` — a arquitetura ficou mais apta a evoluir?

**Sim, e o sinal e o mais forte que o acervo produziu ate aqui sobre um Framework proprio:**
`ADR-0033` nasceu com **26** regras *determinadas e nao observadas*, e **`0`** `Skill`s. Depois
desta mudanca, **`22` das 26 foram aplicadas contra um objeto concreto**, e a medicao devolveu
**3 defeitos que nenhuma leitura tinha achado**. **Framework so se prova sendo usado, e este
foi.**

## 2. Conformidade — com sinal observavel

| # | Verificacao | Sinal | Resultado |
|---|---|---|---|
| `F1` | **Escolha por medicao, nao por preferencia** | `67` × `22` × `56` artefatos de sinal; `22` tokens de uso real; `RD-103` **Alta** so na escolhida | ✅ |
| `F2` | **Pre-condicoes de `FND-04 §6` linha *Skill*** | repete ✓ · verificavel ✓ · mais de um papel ✓ — **3 de 3** | ✅ |
| `F3` | **Pre-condicao universal I** | `CAP-governanca`, **`ativo`** (`VC-01`) | ✅ |
| `F4` | **Pre-condicao universal II** | `SKL` consta do Meta Model — `FND-09 §E-13` | ✅ |
| `F5` | **Rito da classe cumprido** | `C2` → `RFC-0029` → `ADR-0034`, aprova `DEP-EXE` | ✅ |
| `F6` | **`0` campos novos** | `capabilities` e `gatilho` sao **atributos minimos** de `FND-09 §E-13` (`AC-07`) | ✅ |
| `F7` | **`0` bytes de codigo no acervo** | A ficha **cita** o caminho externo; nada foi movido | ✅ |
| `F8` | **Autoverificacao** | `autor` DEP-GOV · `revisor` DEP-QAR · `aprovador` DEP-EXE — distintos (`AC-03`) | ✅ |
| `F9` | **`GO-TO-SKILLS` nao LIBERADO** | Portoes de sequencia medidos **por nome**: `GO-TO-SPECS` e `GO-TO-SKILLS`, **2 antes, 2 depois**. `QG-0`–`QG-6`: **7 e 7** | ✅ |
| `F10` | **A avaliacao das 26 regras foi produzida** | `PT-2026-021 §4`: **19 / 4 / 2 / 1** | ✅ |
| `F11` | **`SK-03` foi exercida contra o objeto** | O nome externo **reprovou** e foi corrigido | ✅ |
| `F12` | **`TPL-skill` produz ficha conforme?** | **Nao** — omite `capabilities` e `gatilho` | ⚠️ **`R1`** |
| `F13` | **O Framework saiu ileso do primeiro uso?** | **Nao** — **1 defeituosa** (`SK-09`) e **2 insuficientes** (`SK-10`, `SK-24`) | ⚠️ **`R2`** |

## 3. `R1` — o template ficou para tras

**Ja conhecido e ja inscrito: `RD-122`.** Esta mudanca **o exerceu** e confirmou a ampliacao: o
frontmatter de `TPL-skill` omite **`capabilities` e `gatilho`**, ambos *atributos minimos* de
`FND-09 §E-13`.

**Nao bloqueia**, e a razao e verificavel: os dois campos foram **escritos a mao**, a ficha
**esta conforme**, e faze-lo **nao criou campo novo** (`AC-07`). **O custo e de atrito e de
risco de erro futuro**, nao de conformidade desta ficha.

## 4. `R2` — o Framework tem 3 defeitos, e eles so apareceram no uso

| Regra | Natureza | O que se observou |
|---|---|---|
| **`SK-09`** | ❌ **defeituosa** | **Erro de categoria:** conta `gatilho` — **atributo de frontmatter** — junto com **blocos de corpo**, e chama o total de *"doze blocos"*. Obrigou a ficha a materializar o gatilho **duas vezes** |
| **`SK-10`** | ⚠️ insuficiente | Remete corretamente a classe, **mas nao adverte** que `C2` arrasta `RFC` → `ADR`. Produz a leitura *"Skill e barata"*, e a primeira custou **5** artefatos |
| **`SK-24`** | ⚠️ insuficiente | O teste *"dobro da mediana do tipo"* e **incalculavel com 1 instancia**. So decide a partir da **terceira** `Skill` |

**Nao bloqueiam, e a razao e de sede:** `ADR-0033` e **`M1`** — corrigi-los exige **`ADR`
sucessor**, que e **rito proprio** e nao cabe nesta mudanca. **Sao o produto esperado do
primeiro uso**, e o proprio `ADR-0033` fixou a primeira `Skill` como seu gatilho de revisao.

**Comparacao que DEP-QAR registra:** `SPC-001` achou **5 defeitos em 32 regras (15,6%)**; esta
missao, **3 em 26 (11,5%)**. **Menos defeito por regra, e a causa provavel esta declarada: 23
das 26 sao recepcao.**

## 5. Recomendacao

**`QG-6` LIBERADO.**

**DEP-QAR recomenda, e a recomendacao e nova:** com a primeira `Skill` existindo, **o gatilho de
revisao de `ADR-0033` disparou**, e os **3** defeitos de §4 tem sede natural — um **`ADR`
sucessor**. **DEP-QAR nao o abre**, porque abrir missao nao e materia de parecer (`FT-10`).

**DEP-QAR NAO recomenda liberar `GO-TO-SKILLS`:** liberar portao e **ato de autoridade**
(`FND-01 §6.2`). **Exercer, que e o que ocorreu, nao e liberar.**
