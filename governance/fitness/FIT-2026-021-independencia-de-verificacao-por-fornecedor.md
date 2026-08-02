---
id: FIT-2026-021
titulo: Verificacao de aptidao da emenda que afere independencia de verificacao por fornecedor
tipo: fitness-check
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: DEP-QAR
proprietario: DEP-QAR
aprovador: DEP-EXE
criado_em: 2026-07-31
atualizado_em: 2026-07-31
revisao_prevista: null
decisoes_relacionadas: [ADR-0005, ADR-0006, ADR-0015, ADR-0028]
substitui: []
substituido_por: null
veredito: apto-com-ressalva
resumo: Verifica a aptidao da emenda que troca o criterio de afericao da independencia da verificacao, com C11 conforme em 13 de 13 e quatro ressalvas.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-GOV
ratificacao: nao-exigida
---

# FIT-2026-021: independencia de verificacao por fornecedor

> **Parecer, nao decisao** (`ADR-0015`, `FT-10`). **Nao aprova, nao ratifica, nao promulga.**
> O objeto avaliado esta **`em-revisao` · `ratificacao: pendente`** e **nao esta em vigor**.

## Proposito

Emitir a Verificacao de Aptidao exigida por `CV-07` sobre a mudanca `C3`/`Tipo 1` registrada em
[ADR-0028](../../decisions/ADR-0028-independencia-de-verificacao-por-fornecedor.md).

## Escopo

| Item | Definicao |
|---|---|
| Avaliado | O rito `RFC-0023` → `ADR-0028` · a determinacao da classe · o **diff literal** sobre `FND-10` · o custo de reversao · a medicao dos dois criterios · `C11` |
| **Nao** avaliado | O merito de artefato algum ja emitido · os **19** `FIT` alcancados · as emendas 1 e 3 |

## Responsaveis

| Papel | Quem |
|---|---|
| Emite | **DEP-QAR** |
| Revisa a forma | **DEP-GOV** |
| Aprova | **DEP-EXE** |
| Ratifica | **—** (`FT-10`) — **a ratificacao incide sobre a mudanca avaliada**, e e do **SOBERANO** |

> ### ⚠️ A auto-referencia, declarada — e este e o parecer em que ela mais importa
>
> **Criterio aplicado: o VIGENTE — `AC-03` de `FND-10 §2.5`**, `revisor` ≠ `autor`.
> **Satisfeito:** este parecer tem autor **DEP-QAR** e revisor **DEP-GOV**; o objeto avaliado
> tem autor **DEP-GOV** e revisor **DEP-QAR**.
>
> **`ADR-0028` NAO esta em vigor e NAO se aplica a si mesma nem a este parecer.** Uma norma que
> se aplicasse a propria verificacao antes de vigorar seria retroatividade — `FND-01 §9`,
> `EV-03`.
>
> **E o numero que a propria emenda produz sobre este parecer esta escrito:** sob `C-2`, esta
> verificacao seria **`fornecedor_verificacao: interno`** — **mesmo executor** —, e portanto
> **uma das `131`**. `AV-4` declara que isso **nao e defeito e nao bloqueia**; declara que e
> **conferencia**, nao **atestado**. **Este parecer e uma conferencia interna, e o diz.**

## 1. Controles obrigatorios

| # | Controle | Fonte | Resultado |
|---|---|---|---|
| `F1` | Classe determinada, **nao presumida por analogia** | `FND-04 §2` | ✅ Cinco hipoteses de `C3` percorridas; incide *"a propria Fundacao"* — `ADR-0028 §11.1` |
| `F2` | **O objeto superado foi redeterminado**, nao herdado da minuta | `AL-01`, `PJ-03` | ✅ **`ADR-0005` nao contem criterio de afericao** — o criterio e `AC-03` de `FND-10`. **A correcao muda a classe de `C2` para `C3`** |
| `F3` | `Tipo 1` determinado por custo medido | `FND-04 §2.2` | ✅ Tres custos que `Tipo 2` nao admite: **segundo ato soberano**, **alcance sobre artefatos ja criados**, **residuo nao editavel em `BL-02`** |
| `F4` | **Plano de reversao explicito** — exigido em `C3`/`Tipo 1` | `FND-04 §2.2` | ✅ `ADR-0028 §10`, objeto a objeto, **inclusive o que nao se reverte** |
| `F5` | Diff literal sobre a fonte, conferivel antes da decisao | `IR-08` | ✅ `§5.3` — **2 linhas** em `§2.2` e `§2.5`, mais o bloco `AV`; **`0` bytes** no resto de `FND-10` |
| `F6` | Campo novo com valor padrao declarado | **`AC-07`** | ✅ ausente le-se **`interno`**; **`0`** arquivos tocados na migracao |
| `F7` | Nenhum artefato invalidado | `EV-03`, `AV-6` | ✅ **`0`** — regra prospectiva |
| `F8` | A diferenca entre os criterios **medida**, nao argumentada | `PI-10` | ✅ **`0`** e **`131`**, base **138**, `BL-2026-07-31-02`, **medido nesta missao** |
| `F9` | Numero **nao herdado** de missao anterior | `MEM-APR-0002` | ✅ A 1.13.4.1 mediu `0`/`130` sobre `137`; **remedido**, e a diferenca esta explicada pelo crescimento do acervo |
| `F10` | A proibicao permanece intacta | `LV-03`, `PI-05`, `RM-06` | ✅ `AV-2` **reforca** `AC-03`; `ADR-0005` com **`0` bytes** |
| `F11` | `RFC` obrigatoria produzida | `FND-04 §2`, `C3` | ✅ [RFC-0023](../../rfcs/RFC-0023-independencia-de-verificacao-por-fornecedor.md) |
| `F12` | Achado agravado **declarado, nao corrigido em silencio** | limite da missao | ✅ **`RD-62`** — o titulo *"cinco campos novos"* passa a divergir em **dois**; declarado com dono e gatilho |
| `F13` | Objeto **nao aplicado** | limite da missao | ✅ `em-revisao` · `pendente`; **`0` bytes** em `FND-10` |

## 2. `C11` — conformidade de [FND-10 §11](../../foundation/10-artifact-framework.md)

**13 de 13 conformes**, sobre `RFC-0023`, `ADR-0028` e este parecer.

| # | Verificacao | Resultado |
|---|---|---|
| 1 | Contrato `L1` completo | ✅ nos tres |
| 2 | `revisor` ≠ `autor` | ✅ `RFC-0023` GOV/QAR · `ADR-0028` GOV/QAR · este QAR/GOV |
| 3 | `ratificacao` coerente com a classe | ✅ `ADR-0028` e `C3`/`Tipo 1` → **`pendente`**, e `status` **nao** entra em `ativo` (`LM-02`) |
| 4 | Tipo documental consta de `§4` | ✅ |
| 5 | Atributo derivavel no frontmatter | ✅ **nenhum** |
| 6 | Cadeia percorrivel | ✅ `RFC-0023` → `ADR-0028` → `FIT-2026-021` → `PS-2026-015` |
| 7 | Custo de contexto medido | ✅ catalogo `§4` |
| 8 | Entrada no catalogo presente | ✅ |
| 9 | Divisao com menos de dois sinais | ✅ **nao aplicavel** |
| 10 | Tabela reproduzida sem declaracao de projecao | ✅ **`0`** — o diff de `§5.3` **cita a fonte literalmente e a identifica**, o que e citacao, nao projecao |
| 11 | Teste preventivo de projecao aplicado | ✅ §2 |
| 12 | Origem externa fora do portao | ✅ **`0` bytes** |
| 13 | Alteracao sem incremento de versao | ✅ **`0`** — objetos novos, `1.0.0`; **`FND-10` nao foi alterada** |

## 3. Ressalvas

| # | Ressalva | Dono | Gatilho |
|---|---|---|---|
| `RA-1` | **`AV-4` pode virar licenca.** Declarar *"conferencia interna"* e mais honesto que afirmar independencia, e tambem mais confortavel. O risco de `interno` virar carimbo permanente e **Alto**, e a mitigacao — publicar o numero — e **indireta** | **DEP-QAR** | Segundo horizonte com `100%` `interno` |
| `RA-2` | **Nao existe membro observado do lado `independente`.** `AV-3` define tres valores e **um deles nunca foi exercido**. O criterio novo nasce sem caso que o discrimine na pratica | **DEP-QAR** | Primeiro artefato com `fornecedor_verificacao: independente` |
| `RA-3` | **A cascata de templates nao foi executada.** **19** templates e ao menos tres deles *(`TPL-documento`, `TPL-adr`, `TPL-fitness-check`)* precisariam prever o campo. `CV-04` faz disso **parte da mudanca**, e ela esta **declarada e nao feita** | **DEP-GOV** | Ato que aplicar `ADR-0028` |
| `RA-4` | **`RD-62` agravado.** O titulo de `FND-10 §2.2` passara a divergir da tabela em **dois** campos. **Fora da lista desta missao**, e por isso **nao corrigido** | **DEP-GOV** | Ato que aplicar `ADR-0028` |

## 4. Evidencia ausente, declarada — `PI-10`

| # | Ausencia |
|---|---|
| 1 | **`0`** casos de verificacao independente de fornecedor no acervo — nao ha com que comparar |
| 2 | **A eficacia de `AV-5` e prevista**: nenhuma baseline foi publicada com os dois numeros |
| 3 | **Este parecer nao mediu se publicar `131` mudaria alguma decisao** — nao ha instrumento para isso antes de haver a publicacao |

## 5. Veredito

**`apto-com-ressalva`.**

A mudanca e **apta**: o rito `C3` esta completo, a classe foi **determinada percorrendo as
cinco hipoteses**, o **objeto superado foi corrigido** em relacao a fonte — e a correcao
**elevou** o rito de `C2` para `C3`, em vez de baixa-lo —, o diff e literal e delimitado, o
custo de reversao esta medido **inclusive no que nao se reverte**, e a diferenca entre os
criterios esta **medida nesta missao**, nao herdada.

As **quatro** ressalvas tem dono e gatilho. **`RA-1` e a mais seria** e permanece **aberta**:
este parecer **nao** afirma que `AV-4` resistira ao uso confortavel — afirma que o numero
publicado tornara o uso **visivel**, o que e menos.

> **Este parecer nao ratifica.** `C3`/`Tipo 1` exige **ato explicito e datado do Soberano sobre
> o texto final** (`LM-02`, `CV-09`), e **nenhum ato foi emitido**.

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-31 | DEP-QAR | Parecer inicial sobre `ADR-0028`. **`C11` 13 de 13**; **13** controles obrigatorios conformes. Registra que **a correcao do objeto superado — de `ADR-0005` para `AC-03` de `FND-10` — ELEVOU o rito de `C2` para `C3`**. **Quatro** ressalvas e **tres** ausencias declaradas. A auto-referencia esta escrita: sob o criterio proposto, este parecer seria **`interno`**, uma das **`131`**. Veredito **`apto-com-ressalva`**. |
