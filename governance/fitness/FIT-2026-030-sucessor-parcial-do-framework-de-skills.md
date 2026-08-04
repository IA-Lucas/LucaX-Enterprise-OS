---
id: FIT-2026-030-sucessor-parcial-do-framework-de-skills
titulo: Verificacao de aptidao — o sucessor parcial do Framework de Skills (ADR-0037)
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
decisoes_relacionadas: [ADR-0033, ADR-0034, ADR-0035, ADR-0036, ADR-0037]
substitui: []
substituido_por: null
veredito: apto-com-ressalva
---

# FIT-2026-030 — O sucessor parcial do Framework de `Skill`s

**Objeto avaliado:** [`ADR-0037`](../../decisions/ADR-0037-sucessor-parcial-do-framework-de-skills.md)
e [`RFC-0032`](../../rfcs/RFC-0032-sucessor-parcial-do-framework-de-skills.md).
**Portao:** `QG-6`. **Obrigatorio** por ser `C2` (`CC-04`).

> **`FT-02`, `LV-03`:** executado por **DEP-QAR**, que **nao** produziu o avaliado.
> **`FT-10`:** parecer, **nao decisao** — nao se ratifica.

## Veredito

**`apto-com-ressalva`.** **Tres** ressalvas — `R1` a `R3` —, **nenhuma bloqueia**.

## 1. `QG-6` — a arquitetura ficou mais apta a evoluir?

**Sim, e a prova nao e o texto novo: e o que a varredura ENCONTROU.**

`FIT-2026-027` registrou *"Framework so se prova sendo usado"*; `FIT-2026-028`, *"so se DIAGNOSTICA
sendo usado DUAS vezes"*; `FIT-2026-029`, que a terceira **elimina a hipotese de defeito de
leitor**. **A quarta acrescenta uma classe nova:**

| # | O que este `ADR` acrescenta, e nenhuma missao anterior podia produzir |
|---|---|
| **1** | ⭐ **Regra geral encontrou defeito que exercicio nenhum encontraria.** `SK-25` **nunca foi medida por missao alguma** — nao por descuido, mas porque **cada missao mede a regra que a `Skill` da vez exerce**. `SK-27` e a primeira regra do acervo cujo cumprimento **exige varrer por classe** |
| **2** | ⭐ **Corrige um veredito ja publicado sem editar o artefato que o publicou.** `ADR-0036 §3` chamou `SK-21 (a)` de *"vacuamente satisfeita"*; sob `SK-27` ela e **`INAPLICAVEL`**. **`ADR-0036` fica com `0` bytes** — e e a demonstracao de que sucessao parcial funciona |
| **3** | **Prova que o remedio nao foi escrito para caber no caso.** `SK-27` foi **aplicado contra o interesse da propria missao** em `§7`, mandando `R4` ficar de fora |

## 2. Conformidade — com sinal observavel

| # | Criterio | Sinal medido | Veredito |
|---|---|---|---|
| `F1` | **Instrumento determinado ANTES de redigir, por norma citada** | **`FND-07 §8.1`, resultado `AJUSTAR`** — *"novo `ADR` que supera **parcialmente** o anterior"*. Os outros dois resultados **descartados com fundamento**, nao por eliminacao | ✅ |
| `F2` | **Gatilho da revisao efetivamente disparado** | `ADR-0033`: *"Gatilho de revisao: a **primeira `Skill` real**"* — **`3` dispararam**. A revisao e **devida**, nao inaugurada | ✅ |
| `F3` | **`SU-01` — explicar o que mudou** | `§3` a `§6`, uma secao por defeito, **cada uma com numero medido** | ✅ |
| `F4` | **`SU-02` nao incide** | `ADR-0033` tem `ratificacao: nao-exigida` — **conferido no frontmatter**, nao de memoria. **`0` atos** | ✅ |
| `F5` | **`0` bytes em `ADR-0033`** | `M1` intacto (`CC-01`, `AC-10`). `status: ativo` e `superado_por: null` **corretos, nao omissos** | ✅ |
| `F6` | **Espelho da sucessao no lugar certo** | `supera: [ADR-0033]` **so na fonte** (`LN-01`); `R-08` **fora** da excecao de `LN-02`; catalogo (`M3`) reconciliado na **mesma mudanca** (`CC-03`) | ✅ |
| `F7` | **Identificadores novos, e nao reenunciacao sob o mesmo numero** | **`SK-27` a `SK-30`.** Reusar `SK-09` criaria **segunda sede** — o defeito que `SK-23`, **em vigor**, proibe | ✅ |
| `F7b` | ⭐ **Precedente CONFERIDO no frontmatter, e afirmacao FALSA retirada antes de publicar** | A redacao inicial de `PT-2026-024` dizia *"PRIMEIRA superacao do acervo"*. **Medido:** `supera:` nos `37` `ADR` = **`28` `[]` · `6` `null` · `3` preenchidos** — **e esta e a TERCEIRA**. **`superado_por` = `null` em `37` de `37`**, e `ADR-0007` e `ADR-0021` seguem **`ativo`** depois de superados. **O erro foi medido pelo proprio autor, retirado e REGISTRADO** *(`PT-2026-024 §10`)*, nunca corrigido em silencio | ✅ |
| `F8` | **Numeros remedidos nesta sessao, nunca herdados** | `175`/`188`/`231` · `11` blocos · `0`/`0` no `TPL` · `3` de `3` `gatilho` duplicado · `1`/`2`/`2` saidas · `0` `Skill`s superadas | ✅ |
| `F9` | **Controle positivo antes de crer em zero** | **`3` controles**: `proprietario` = `2` · `## [^0-9]` = `7` · `substituido_por` = `3` de `3` | ✅ |
| `F10` | **Baseline reproduzida ANTES da primeira escrita** | `249 · 72.996 · a0a07b2e… · d4a61857…`, **`2`** execucoes, `EXIT=0`, **`0` deriva** contra o token 28 | ✅ |
| `F11` | **Copia datada provada por CONTEUDO** | **`630/630`** pela **primeira `Skill`** *(quarto uso real)*, e **`249/249`** contra o `H-A`, **diff vazio** | ✅ |
| `F12` | **`0` bytes em fonte normativa, `TPL-skill`, `ADR-0033`..`ADR-0036`, codigo e medidor** | Conferido por `sha256` arquivo a arquivo contra o `H-A` | ✅ |

## 3. ⚠️ `R1` — o Framework passa a ter DUAS sedes vigentes, e o custo de contexto SOBE

**Este e o defeito real da emissao, e ele e inerente ao instrumento escolhido — nao um erro de
execucao.**

| Antes | Depois |
|---|---|
| Ler o Framework = **`1`** artefato | Ler o Framework = **`2`** artefatos, e **quem ler so o primeiro le `SK-09` defeituosa sem aviso** |

**`CE-01` e `CE-02` incidem, e `ADR-0037 §L1` declara o efeito sem dissimular.** DEP-QAR confirma
que **a alternativa era pior**: superar o todo obrigaria a **reproduzir `22` regras** — segunda sede
de cada uma, contra `PJ-01` — e **proibiria** por `LN-03` toda relacao nova com `ADR-0033`, que as
**`3`** fichas vigentes ja declaram.

> ⚠️ **DEP-QAR registra, sem transformar em recomendacao de missao:** **a promocao a `FND` e a unica
> coisa que UNIFICA as duas sedes**, e ela e `C3 · Tipo 1` **com ato**. **Cada sucessor futuro
> acrescenta uma sede.** **O ponto em que o custo das sedes supera o custo do ato NAO foi medido, e
> nao se estima** (`CE-04`).

## 4. ⚠️ `R2` — `SK-27` foi VARRIDA, mas dois membros entraram por leitura, nao por reprovacao

**A varredura e o melhor da emissao, e e tambem onde esta o risco.**

| Membro | Como entrou | Forca do sinal |
|---|---|---|
| `SK-24` | ❌ **reprovacao medida** em `3` missoes, piso provado algebricamente | **forte** |
| `SK-21 (b)` | ❌ **reprovacao medida**, e a razao registrada estava **errada** | **forte** |
| `SK-21 (a)` | ⚠️ **releitura** — `ADR-0036` a chamara *"vacuamente satisfeita"* | **media** — o termo ja denunciava |
| **`SK-22`** | ⚠️ **leitura do enunciado** | **media** |
| **`SK-25`** | ⚠️ **leitura do enunciado** — **jamais exercida por missao alguma** | ⚠️ **fraca** |

**DEP-QAR homologa a inclusao dos cinco, e o fundamento e que `SK-27` nao reescreve enunciado
nenhum:** ela **acrescenta o piso** e troca *"satisfeita"* por **`INAPLICAVEL`**. **O custo de errar
o piso de `SK-25` e um veredito de `FIT` mais conservador — nunca uma `Skill` recusada.**

> ### ⭐ A corroboracao independente, e DEP-QAR a confere na fonte antes de homologa-la
>
> `ADR-0037 §4.3` afirma que **`SK-22` tem piso `n ≥ 2` e foi exercida pela primeira vez na SEGUNDA
> `Skill`** — isto e, **exatamente no piso**. **Conferido em `governance/roadmap-canonico.md`**, no
> registro da Missao `1.13.12`: *"`3` regras exercidas pela primeira vez (`SK-05`, `SK-12`,
> `SK-22`)"*. ✅ **A afirmacao PROCEDE.**
>
> **Isso e previsao retrospectiva acertando sobre dado que ja existia e que ninguem havia
> relacionado** — a forma mais barata de evidencia disponivel a uma regra ainda nao exercida, e a
> unica que `SK-27` podia oferecer nesta emissao.

⚠️ **Ressalva que fica:** **`SK-27` nao foi exercida sobre nenhuma `Skill` real.** Nasce
**determinada, nao observada** — e `ADR-0037 §L2` e `§L3` o declaram. **E o mesmo estado em que
`ADR-0033` nasceu**, e a historia recente mostra que esse estado custou **um sucessor**.

## 5. ⚠️ `R3` — o custo do rito nao caiu, e a quarta medicao muda de natureza

| Missao | Materia | Artefatos |
|---|---|---|
| `1.13.11` · `1.13.12` · `1.13.13` | `Skill` | **`5`** · **`5`** · **`5`** |
| **`1.13.14`** | **norma sobre o Framework** | **`4`** |

**DEP-QAR recusa a leitura de que *"o custo caiu para `4`"*.** **`4 = 5 − 1`, e o `1` que falta e a
ficha**, porque **nenhuma `Skill` foi criada**. **O rito da classe — `RFC` → `ADR` → `FIT` → `PT` —
veio INTEIRO sobre materia que nao e `Skill`.**

> **Isso CONFIRMA `SK-29` em vez de contradiza-la:** o custo e da **classe do efeito** (`AL-01`),
> nunca da materia nem da novidade. **`SK-29` acaba de ser corroborada pela primeira medicao fora
> do seu proprio dominio** — e essa medicao **so existe porque esta missao pagou o rito**.

⚠️ **Consequencia de portao que DEP-QAR registra:** **corrigir o Framework custa `4` artefatos por
sucessor**, e `SU-03` diz que **superacao frequente da mesma materia indica materia mal enquadrada**.
**Esta e a PRIMEIRA superacao.** **Uma segunda passa a ser sinal, e o dono da resposta e o Fundador,
nao DEP-GOV** — porque a resposta e a promocao a `FND`, `C3 · Tipo 1`, **com ato**.

## 6. `FIT-2026-029 R4` — DEP-QAR homologa a exclusao, e declara o proprio conflito de interesse

**`R4` foi levantada por DEP-QAR, e e DEP-QAR quem agora homologa deixa-la de fora. O conflito e
declarado, nao dissimulado** (`PI-05`, `LV-03`).

| # | Fundamento da exclusao | DEP-QAR concorda? |
|---|---|---|
| `1` | **`1` de `3` instancias** — abaixo do piso que a propria emissao institui | ✅ **sim** |
| `2` | **Nao e defeito de ENUNCIADO:** `SK-19`/`SK-30` obrigam a **declarar**; obrigar a **impedir** e regra nova | ✅ **sim**, e `SU-01` o confirma |
| `3` | **DEP-QAR ja declarara o objeto CORRETO** em `FIT-2026-029 §6.2` | ✅ **sim** — manter `R4` e exclui-la do sucessor **nao se contradizem**: ressalva registra limite, nao exige norma |

> ⭐ **O que DEP-QAR destaca:** a missao **aplicou `SK-27` contra si mesma**. Incluir `R4` teria
> **economizado um `ADR` futuro**, e o despacho o oferecia. **Recusar a economia porque o piso nao
> foi atingido e a evidencia mais forte de que `SK-27` nao foi escrita para caber no caso.**

## 7. Recomendacao

| # | Recomendacao | Dono |
|---|---|---|
| `1` | **Exercer `SK-27` a `SK-30` na quarta `Skill`**, e medir se `SK-28` de fato elimina o `gatilho` duplicado — **`3` de `3` hoje** | DEP-GOV |
| `2` | **Registrar `SK-25` como `INAPLICAVEL` no proximo `FIT` de `Skill`**, e nao omiti-la. **E o primeiro teste real de que `SK-27` muda o relatorio** | DEP-QAR |
| `3` | **Decidir `RD-122` antes da quarta ficha**, ou registrar que se optou por paga-lo pela quarta vez. **Reiterada de `FIT-2026-029 §8.5`, nao atendida** | DEP-GOV |
| `4` | ⛔ **NAO abrir quinto membro de `SK-27` sem `n ≥ 2`.** O gatilho de `R4` esta registrado em `ADR-0037 §11` | DEP-GOV |
| `5` | ⛔ **NAO promover a `FND` agora** — `C3 · Tipo 1` **com ato**. **Mas a segunda superacao desta materia torna a pergunta devida** (`SU-03`) | Fundador |
