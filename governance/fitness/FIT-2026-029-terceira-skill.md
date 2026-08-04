---
id: FIT-2026-029-terceira-skill
titulo: Verificacao de aptidao — a terceira Skill do acervo (ADR-0036)
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
decisoes_relacionadas: [ADR-0033, ADR-0034, ADR-0035, ADR-0036]
substitui: []
substituido_por: null
veredito: apto-com-ressalva
---

# FIT-2026-029 — A terceira `Skill`

**Objeto avaliado:** [`ADR-0036`](../../decisions/ADR-0036-terceira-skill-provar-restauracao-de-backup.md) e
[`SKL-custodia-provar-restauracao-de-backup`](../../skills/SKL-custodia-provar-restauracao-de-backup.md).
**Portao:** `QG-6`. **Obrigatorio** por ser `C2`.

> **`FT-02`, `LV-03`:** executado por **DEP-QAR**, que **nao** produziu o avaliado.
> **`FT-10`:** parecer, nao decisao — nao se ratifica.

## Veredito

**`apto-com-ressalva`.** **Quatro** ressalvas — `R1` a `R4` —, **nenhuma bloqueia**.

## 1. `QG-6` — a arquitetura ficou mais apta a evoluir?

**Sim, e por dois motivos que nenhuma missao anterior podia produzir.**

`FIT-2026-027` registrou que *"Framework so se prova sendo usado"*; `FIT-2026-028`, que *"Framework
so se DIAGNOSTICA sendo usado DUAS vezes"*.

| # | O que a terceira acrescenta |
|---|---|
| **1** | **Uma regra que so podia responder *"nao"* passou a poder responder *"sim"*.** `SK-24` deixou de ser teste decorativo. **Nenhuma leitura produziria isso** — foi preciso **criar a instancia que muda o denominador** |
| **2** | ⭐ **Pela primeira vez, o autor do candidato CONHECIA os defeitos — e eles ocorreram assim mesmo.** Isso separa *"defeito que some com disciplina"* de **defeito que so some emendando a norma**, e e a distincao que o `ADR` sucessor precisa para nao errar o remedio |

## 2. Conformidade — com sinal observavel

| # | Criterio | Sinal medido | Veredito |
|---|---|---|---|
| `F1` | **Item 0 medido ANTES de propor, com poder de PARAR** | **Nenhuma das `26` recusa.** `SK-22` foi o unico que quase reprovou, isolado em `RFC-0031 §3` | ✅ |
| `F2` | **Afirmacao de candidato CONFERIDA na fonte, nunca acreditada** | **`6` de `6`** conferidas, **`0`** divergentes: `CAP` ativa e custodio · prova **(c) `PASSOU` 16,2 s** · `74afde6c…` · `15.585` linhas · regra `A3` · o instrumento existe | ✅ |
| `F3` | **`SK-03` aplicada ao nome externo** | ⭐ **PASSOU pela primeira vez em tres.** `3` de `4` nomes externos reprovados, e o que passou e **o unico escrito sob a regra** | ✅ |
| `F4` | **Sinal de `SK-20` observado, nunca antecipado** | **`3` fontes independentes**, e uma e **execucao propria com numero**. `0` antecipado | ✅ |
| `F5` | **`SK-24` calculada** | Mediana **`188`** *(`175`, `188`, `231`)*, limiar **`376`**, maior **`231`** — **nao dispara**, e **agora poderia** | ✅ |
| `F6` | **`0` bytes em fonte normativa, `TPL-skill`, `ADR-0033`, codigo e medidor** | Conferido por `sha256` arquivo a arquivo contra o `H-A` | ✅ |
| `F7` | **`0` bytes escritos no `nxtrack`** | Origem do merito lida em **somente leitura** | ✅ |
| `F8` | **Baseline reproduzida ANTES da primeira escrita** | `244 · 71.675 · 055849fe… · d07c2994…`, **`2`** execucoes, `EXIT=0`; e **`244/244`** contra o `H-B` do token 27 | ✅ |
| `F9` | **Copia datada provada por CONTEUDO** | **`625/625`** pela **primeira `Skill`**, e **`244/244`** contra o `H-A`, diff vazio | ✅ |
| `F10` | **Segundo candidato da F8 NAO admitido** | Segue fora, **intacto** — *um por missao* | ✅ |

## 3. `R1` — `SK-24` nao disparou, e o parecer recusa a leitura confortavel

**A leitura confortavel seria:** *"nao disparou tres vezes seguidas, logo a regra esta sa"*.
**DEP-QAR recusa, e o fundamento e algebrico, nao de opiniao.**

| `n` | Por que nao disparou |
|---|---|
| `1` e `2` | ⛔ **Nao podia.** Exigiria `a < 0` |
| **`3`** | ✅ **Podia.** Nao disparou porque as tres instancias tem tamanho comparavel — `175`, `188`, `231` |

**Os dois *"nao"* nao sao o mesmo *"nao"*, e trata-los como serie de tres e erro de leitura.**
**A serie util tem `1` elemento:** esta e a **primeira** medicao informativa de `SK-24` na historia
do acervo.

⚠️ **Ressalva:** com `3` pontos a mediana **nao e estavel** — uma quarta `Skill` **move o limiar sem
que ficha alguma mude**. **`SK-24` ainda nao tem regime, so tem piso.**

## 4. `R2` — `SK-09` e `SK-10` FECHAM, e desta vez com a prova mais forte possivel

| Regra | `n=1` | `n=2` | **`n=3`** | Leitura |
|---|---|---|---|---|
| `SK-09` | ❌ | ❌ | ❌ | **FECHADO** |
| `SK-10` | ⚠️ | ⚠️ | ⚠️ | **FECHADO** |
| `SK-24` | ⚠️ | ⚠️ | ⚠️ | **Sinal MADURO** — o piso e `3` |
| **`SK-21`** | — | — | — | ⚠️ **Segue nao exercida, por DOIS motivos** |

> ### ⭐ Por que a terceira ocorrencia prova mais que a segunda, e nao apenas *"mais uma vez"*
>
> **Nas duas primeiras, o autor desconhecia os defeitos.** Restava a hipotese de que fossem
> **defeito de LEITOR** — alguem que nao entendeu `SK-09` e somou categorias, alguem que nao
> percebeu o custo de `C2`.
>
> **Aqui o autor sabia, escreveu §0 para separar as categorias e §11 para declarar o custo — e o
> `gatilho` foi materializado duas vezes e o custo foi `5` assim mesmo.** **Conhecimento nao
> corrigiu o defeito.** **Isso elimina a hipotese de defeito de leitor e deixa so a de defeito de
> ENUNCIADO** — que e exatamente o que o `ADR` sucessor precisa saber antes de redigir o remedio.

**DEP-QAR homologa tambem a correcao que `ADR-0036 §3` faz do registro anterior sobre `SK-21`:**
`PT-2026-022` nomeou **um** bloqueio *(faltam agentes)* onde ha **dois**, e o segundo — a ausencia
de **aresta de dependencia** — **nao se resolve criando `Skill`s nem citando-as entre si**.

## 5. `R3` — o template continua para tras, pela terceira vez

**`RD-122` exercido `3` de `3` vezes**, e a terceira **com o autor ciente**. Ha agora **`3`**
artefatos carregando a mesma nota de excecao — **`3` lugares onde a divergencia pode derivar**.

⚠️ **DEP-QAR registra, sem transformar em recomendacao de missao:** sanar `RD-122` e **`C2` sobre
`TPL`, sem ato**; **nao** sana-lo cobra **`2` campos a mao por ficha, indefinidamente**. **O ponto
em que as curvas se cruzam nao foi medido, e nao se estima** (`CE-04`).

## 6. ⚠️ `R4` — a ancoragem do veredito nao tem portao, e o limite do merito e de UM produto

**Duas observacoes distintas, agrupadas porque tem o mesmo efeito: a `Skill` promete mais do que
instrumento algum garante.**

### 6.1 O veredito que viaja

| Protecao | Existe? | Natureza |
|---|---|---|
| Identificador do repositorio impresso na saida | ✅ sim | **do instrumento** |
| Regra *"destino novo = backup nao provado"* | ✅ sim | **texto** |
| Passo `3` imprime o repositorio antes de restaurar | ✅ sim | **do instrumento** |
| **Portao que impeca reusar veredito de outro repositorio** | ❌ **NAO EXISTE** | — |

**`SK-19` obriga a DECLARAR o modo de falha, nao a IMPEDI-LO.** A defesa e a comparacao feita por
quem consome — **e consumidor que nao compara nao e detectado por nada**.

### 6.2 O merito e de um produto so

**A capacidade foi provada em `1` execucao, `1` produto, `1` ferramenta de backup, `1` banco.**
A ficha e escrita como **geral** — *"qualquer repositorio de backup de dado sob custodia"* — e a
generalidade e **projetada, nao observada**. `ADR-0036 §L5` ja o declara, e **DEP-QAR confirma que
o limite esta corretamente declarado** e nao dissimulado.

> **Por que NAO bloqueia, e o criterio e `FT-09`:** ressalva bloqueia quando o defeito esta **no
> objeto avaliado**. **Aqui o objeto esta correto e declara os proprios limites.** As duas
> primeiras `Skill`s entraram com merito de escopo igualmente estreito, e **exigir prova em `n`
> produtos seria criar portao que `ADR-0033` nao pede de nenhuma**. **O que se exige — declarar —
> foi feito.**

## 7. A quinta medicao — parecer de DEP-QAR

**DEP-QAR homologa a conclusao de `RFC-0031 §6.4`, e acrescenta a leitura de portao:**

| Economia | Reducao medida | Vale a fabrica? |
|---|---|---|
| **Retrabalho de redacao** | **`1` → `0`** reprovacoes por regra | ✅ **sim** |
| **Custo do rito** | **`5` → `5`** | ❌ **nao, e nunca vai** |

> **A correcao de merito que sobrou — o valor vencido de `SK-24` — e ESTRUTURAL e nao evitavel**, e
> `ADR-0036 §5.1` a enquadra bem: **ha afirmacao que so pode ser feita no momento da admissao**.
> **DEP-QAR registra a consequencia de portao:** todo candidato de fabrica que **cite mediana,
> contador ou baseline** chega **necessariamente vencido**, e **remedir esses campos na admissao
> deve ser passo do rito, nao zelo do autor.**

## 8. Recomendacao

| # | Recomendacao | Dono |
|---|---|---|
| `1` | **ABRIR o `ADR` sucessor de `ADR-0033`.** Os tres sinais estao maduros, e o terceiro uso **eliminou a hipotese de defeito de leitor** | DEP-GOV |
| `2` | **Formular o remedio na forma GERAL de `ADR-0036 §3.2`** — *"regra cujo antecedente exige populacao ou aresta declara o seu piso, e abaixo dele e INAPLICAVEL, nunca satisfeita"* —, porque cobre `SK-24` **e** `SK-21` de uma vez | DEP-GOV |
| `3` | **Corrigir `SK-19` para admitir MAIS DE UMA saida plausivel e errada.** O singular do enunciado **nao bastou em `2` de `3`** fichas | DEP-GOV |
| `4` | **NAO esperar a quarta `Skill`.** Ela move o limiar de `SK-24`, mas **nao acrescenta classe de sinal**: `SK-09`, `SK-10` e o custo repetiram tres vezes com **`0`** variacao | DEP-GOV |
| `5` | Decidir `RD-122` **antes** da quarta ficha, ou registrar que se optou por paga-lo de novo | DEP-GOV |
| `6` | ⛔ **NAO promover `ADR-0033` a `FND` no sucessor.** Promover e `C3 · Tipo 1` **com ato** | Fundador |
