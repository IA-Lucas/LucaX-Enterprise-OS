---
id: ADR-0037-sucessor-parcial-do-framework-de-skills
titulo: Sucessor parcial de ADR-0033 — institui SK-27 a SK-30, fecha a classe de regra com antecedente de populacao ou aresta, separa frontmatter de bloco de corpo, declara o rito inteiro da classe e poe as saidas plausiveis e erradas no plural
tipo: adr
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-08-03
atualizado_em: 2026-08-03
revisao_prevista: 2027-02-03
decisoes_relacionadas: [ADR-0021, ADR-0022, ADR-0033, ADR-0034, ADR-0035, ADR-0036]
substitui: []
substituido_por: null
classe_mudanca: C2
tipo_decisao: 2
supera: [ADR-0033]
superado_por: null
resumo: Supera PARCIALMENTE ADR-0033 pelo resultado AJUSTAR de FND-07 8.1, instituindo SK-27 a SK-30 — piso de populacao e de aresta, separacao entre atributo de frontmatter e bloco de corpo, advertencia do rito inteiro da classe e plural das saidas plausiveis e erradas —, deslocando SK-09, SK-10, SK-19, SK-24 e a leitura de SK-21 (b), sem tocar as outras 22 regras, sem promover a FND e sem emendar fonte alguma.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# ADR-0037: O sucessor parcial do Framework de `Skill`s

## Contexto

`ADR-0033` instituiu **`SK-01` a `SK-26`** em **2026-08-03**, e declarou, na propria caixa de
tradeoff, o preco da sede que escolheu:

> *"Nascendo em `ADR`, este Framework e **`M1`** … **`M1` nunca se emenda**: **corrigir uma virgula
> exige `ADR` sucessor**. **A sede barata e a sede mais cara de corrigir**."*

**Tres `Skill`s reais o exerceram** — `ADR-0034`, `ADR-0035`, `ADR-0036` —, sobre materias
**disjuntas**, e o exercicio produziu **quatro defeitos medidos**:

| Regra | Natureza | Instancias | Estado |
|---|---|---|---|
| **`SK-09`** | ❌ **DEFEITUOSA** — erro de categoria | **`3` de `3`** | Sinal **fechado** |
| **`SK-10`** | ⚠️ **INSUFICIENTE** — nao adverte do rito | **`3` de `3`** | Sinal **fechado** |
| **`SK-19`** | ⚠️ **INSUFICIENTE** — singular | **`2` de `3`** | Sinal **maduro** |
| **`SK-24`** | ⚠️ **INSUFICIENTE** — sem piso de `n` | piso **provado** em `n = 3` | Sinal **maduro** |
| **`SK-21 (b)`** | ⚠️ **mesma classe de `SK-24`** — sem piso de aresta | `0` arestas | Sinal **maduro** |

**O sinal deixou de estar bloqueado por falta de medicao**, e `FIT-2026-029 §8` recomendou **ABRIR
AGORA**, com a razao escrita: **a quarta `Skill` moveria o limiar de `SK-24` mas nao acrescentaria
CLASSE de sinal** — o terceiro uso ja produziu a evidencia decisiva, **o autor CIENTE do defeito
errando assim mesmo**.

## Decisao

**Superar PARCIALMENTE `ADR-0033`** — resultado **`AJUSTAR`** de `FND-07 §8.1` —, instituindo
**`SK-27` a `SK-30`**, que **deslocam** `SK-09`, `SK-10`, `SK-19`, `SK-24` e a leitura de
`SK-21 (b)`.

**As outras `22` regras seguem vigorando em `ADR-0033`, que permanece `ativo`.**

---

## 1. O instrumento — determinado por norma citada, ANTES de redigir

### 1.1 Por que sucessor, e nao emenda

| Norma | Texto | Efeito aqui |
|---|---|---|
| `FND-10 §6.2` | `ADR` e **`M1`**: *"o texto **nunca** muda; muda apenas o estado e os campos de sucessao"* | **`0` bytes** em `ADR-0033` |
| `AC-10` | *"Artefato `M1` nunca e emendado … Corrige-se **superando**, e o sucessor ja nasce sob o contrato por ser artefato novo"* | Este `ADR` |
| `CC-01` | *"`ADR` historico **nunca** e editado — nem para corrigir erro, nem para completar campo"* | Nem uma virgula |
| `CC-06` | *"Artefato `M1` com erro material gera **novo artefato**"* | Este `ADR` |
| `SU-01` | *"Superacao sem explicar **o que mudou** e substituicao de opiniao, nao decisao. **E devolvida**"* | §3 a §6 |

> **O custo foi anunciado por `ADR-0033` e e pago aqui, nao descoberto aqui.**

### 1.2 ⭐ Por que PARCIAL — e a norma nomeia este instrumento

**`FND-07 §8.1`, *Resultado da revisao*, enumera tres, e o do meio e este caso:**

| Resultado | Acao prescrita | Este caso? |
|---|---|---|
| Confirmar | Nota registrando que foi revista e mantida | ❌ quatro regras reprovaram **por medicao** |
| ⭐ **Ajustar** | **Novo `ADR` que supera PARCIALMENTE o anterior** | ✅ **SIM** |
| Superar | Novo `ADR` pelo rito de `FND-07 §7` | ❌ `22` de `26` seguem servindo |

**E a revisao nao e inaugurada aqui: o gatilho ja disparou.** `ADR-0033` fixou
*"**Gatilho de revisao:** a **primeira `Skill` real** (`L1`)"* — e houve **tres**.
**Este `ADR` entrega o RESULTADO de uma revisao devida, no verbo que a norma nomeia.**

### 1.3 O que a superacao total custaria — medido, nao suposto

`LN-03` de `FND-10 §7.2`: ***"Relacao com artefato `depreciado`, `superado` ou `revogado` nao pode
ser CRIADA."***

| Se `ADR-0033` passasse a `superado` | Consequencia |
|---|---|
| As **`22`** regras integras perderiam a sede vigente | Teriam de ser **reproduzidas** aqui — **segunda sede**, o defeito de `PJ-01` e do proprio `SK-23` |
| `decisoes_relacionadas: [ADR-0033]` | **Proibido criar** dali em diante — e as **`3`** fichas vigentes ja o declaram |

> **Reproduzir `22` regras para corrigir `4` seria trocar um defeito por vinte e dois.**

### 1.4 Onde vive o espelho da sucessao — e por que `ADR-0033` fica com `0` bytes

| Regra | O que fixa | Aplicacao |
|---|---|---|
| `LN-01` | *"**Bilateralidade e do registro, nao do frontmatter.** A relacao e declarada uma vez, **na fonte**, e o espelho e derivado"* | `supera: [ADR-0033]` **aqui** |
| `LN-02` | A excecao vale para **`substitui`/`substituido_por`**, e **so** | `supera` e **`R-08`** — **fora** da excecao |
| `CC-03`, `CV-04` | Alteracao em cascata e parte da **mesma mudanca** | Catalogo mestre (`M3`) reconciliado nesta mudanca |

> **`ADR-0033` conserva `status: ativo` e `superado_por: null`, e os dois valores estao CORRETOS —
> nao sao omissao.** Ele **nao** esta superado: **`22` das suas `26` regras sao a sede vigente do
> Framework**, e `PJ-04` ja fixa que campo de estado em `M1` registra **o estado no ato**.

### 1.5 ⭐ PRECEDENTE MEDIDO — o acervo ja fez isto duas vezes, e nao de memoria

**Varredura do campo `supera:` nos `37` `ADR`, nesta sessao:**

| Valor | Ocorrencias |
|---|---|
| `[]` | **`28`** |
| `null` | **`6`** |
| **preenchido** | **`3`** — [`ADR-0022`](ADR-0022-sede-canonica-do-framework-de-specifications.md) supera `ADR-0021` · [`ADR-0027`](ADR-0027-classe-de-admissao-de-existencia-no-portao-de-origem-externa.md) supera `ADR-0007` · **este** |
| **`superado_por` preenchido** | **`0` de `37`** — ⭐ **inclusive em `ADR-0007` e `ADR-0021`** |
| **`status` dos dois superados** | ⭐ **`ativo` nos dois** |

> **A construcao desta emissao nao e nova: e a TERCEIRA vez que o acervo supera um `ADR`, e nas
> DUAS anteriores o superado ficou `ativo`, com `superado_por: null` e o espelho FORA do
> frontmatter** — exatamente o que `LN-01` prescreve e o que `§1.4` determinou aqui **antes** de
> medir o precedente. **A norma e a pratica coincidem, e a coincidencia foi conferida no
> frontmatter, nunca lembrada.**
>
> ⚠️ **E o precedente e proximo, nao analogico:** **`ADR-0022` supera `ADR-0021`**, que e o `ADR`
> que `ADR-0033` cita como **precedente identico** da sua propria classe — o Framework de `Spec`s,
> mesma materia, mesma sede, mesmo defeito de sede barata.

---

## 2. As quatro novas regras

> **Declaracao de projecao (`PJ-02`).** **Fonte:** `FND-03 §4`, `§3.5` · `FND-09 §E-13` ·
> `FND-10 §4.8`, `§6.2`, `§7.2` · `FND-04 §2.1`, `§2.2`, `§6` · `FND-07 §8.1` · `FND-08 §7.1`.
> **Campos projetados:** apenas **o piso, a categoria, o custo do rito e a cardinalidade das
> saidas de falha**. **Em divergencia prevalece a fonte** (`PJ-03`).

| # | Regra |
|---|---|
| **SK-27** | **Toda regra deste Framework cujo antecedente dependa de POPULACAO ou de ARESTA declara o seu PISO — e, abaixo do piso, e `INAPLICAVEL`, nunca `satisfeita`.** **Piso** e o menor valor do antecedente em que o conjunto-solucao **deixa de ser vazio**, apurado **resolvendo a condicao**, jamais estimado (`CE-04`). **Regra cujo piso nao se possa apurar e `INAPLICAVEL` ate que se apure.** **A distincao e operacional, e e a razao de existir da regra:** *"satisfeita"* entra no `FIT` como ✅ e **desaparece**; **`INAPLICAVEL` fica visivel e COBRA o piso**, declarando `piso n ≥ k, atual n = j`. **A classe e VARRIDA, nao amostrada:** os pisos de **todos** os membros entre `SK-01` e `SK-26` sao apurados em **§4.3** — **`SK-21 (a)`**, **`SK-21 (b)`**, **`SK-22`**, **`SK-24`** e **`SK-25`**, cinco membros —, e **regra nova deste Framework so entra em vigor com o piso declarado ou com a declaracao de que nao depende de nenhum**. *(Nota: referencia de FRONTEIRA nao e aresta de dependencia — delimitar-se CONTRA um vizinho e o oposto de depender dele.)* **Quem aplicar membro da classe abaixo do piso e escrever ✅ esta fabricando evidencia** (`LV-12`). |
| **SK-28** | **O contrato da `Skill` tem DUAS categorias, e elas NAO se somam: atributos de FRONTMATTER e blocos de CORPO.** **(a) Frontmatter:** os universais de `FND-03 §4` e `FND-10 §2.2`, **mais `capabilities` e `gatilho`**, que `FND-09 §E-13` lista como *atributos minimos* — **`SK-06` permanece integralmente em vigor**. **(b) Corpo:** os **`11`** blocos numerados de `TPL-skill`. **`gatilho` e atributo de frontmatter e NAO e decimo segundo bloco.** Materializa-lo tambem no corpo e **projecao** e declara-se como tal (`PJ-02`), **ou omite-se** — nos dois casos **nao conta como bloco**. **A conformidade afere-se por categoria, separadamente**, e **`11 + 1 = 12` nao e contagem: e soma de grandezas de categorias diferentes.** |
| **SK-29** | **A autoridade sobre uma `Skill` e derivada, nunca declarada no artefato — E o rito da classe vem INTEIRO, sem desconto.** A parte derivada de `SK-10` **permanece**: autoridade e funcao de **(a)** a classe do efeito (`AL-01`, **`C2` como piso de criacao** por `FND-04 §6`), **(b)** o tipo de reversibilidade, **(c)** o dado que a `Skill` toca; **`Skill` que fixe aprovador em texto e nao conforme** (`RD-23`); **ratificacao nao se exige nunca** (`FND-09 §8.2` linha `SKL`). **O QUE SE ACRESCENTA, e e o que faltava:** **`C2` nao e apenas quem aprova — `C2` arrasta `RFC` → `ADR` → `FIT` → ficha → incremento do contador**, e `FND-04 §6` diz ***"alem do rito da classe"***. **Nada nele e dispensado** por precedente, por candidato pre-redigido sob este Framework, nem por conhecer o preco de antemao — **medido `5`, `5` e `5`, com `0` reducao, e na terceira o candidato declarou o custo antes**. **O barato e o ATO — `0` em tres missoes —, nunca o RITO**, e **quem propuser `Skill` esperando componente barato medira `5` de novo.** |
| **SK-30** | **Os modos de falha conhecidos incluem obrigatoriamente TODAS as saidas plausiveis e erradas identificadas — no PLURAL —, cada uma com o seu metodo de deteccao de `SF-14`.** Resultado **bem-formado e incorreto** nao dispara alarme nenhum, e **uma so nao basta quando ha mais**: medido em **`2` de `3`** fichas, que numeraram `(I)` e `(II)` **por conta propria**, contra a letra do enunciado anterior. **A lista declara-se INCOMPLETA por construcao:** *"nenhuma outra conhecida"* e afirmacao sobre **o que se sabe**, jamais sobre **o que existe** — e escreve-la como se fosse a segunda **e** a saida plausivel e errada da propria regra. |

### 2.1 O que cada nova regra desloca — enumerado, nunca *"o resto"*

| Nova | Desloca | O que da regra anterior **PERMANECE** |
|---|---|---|
| **`SK-27`** | **A LEITURA de todo membro da classe** — apurados em §4.3: **`SK-21 (a)`**, **`SK-21 (b)`**, **`SK-22`**, **`SK-24`** e **`SK-25`** | **Os enunciados permanecem INTEGROS**: `SK-27` **nao reescreve nenhum deles** — acrescenta o **piso** e troca *"satisfeita"* por **`INAPLICAVEL`** abaixo dele. De `SK-24`: **o custo continua MEDIDO** (`CE-02`), a `Skill` continua **escrita em blocos rotulados e independentes**, e **carregar a ficha inteira para um passo continua sendo falha de curadoria** |
| **`SK-28`** | **`SK-09`** — a contagem | **`SK-06` inteiro**: `gatilho` e `capabilities` seguem **obrigatorios**, e ausencia segue **veto de `DEP-GOV`** (`AC-06`). **O deslocamento e de CONTAGEM, nunca de exigencia** |
| **`SK-29`** | **`SK-10`** — por absorcao | **Todo o merito de `SK-10`** e reproduzido **e ampliado**. Nada dele se perde |
| **`SK-30`** | **`SK-19`** — a cardinalidade | **A obrigacao central**: declarar a saida plausivel e errada e **como se detecta**, por metodo de `SF-14` |

> ⚠️ **`SK-01` a `SK-08`, `SK-11` a `SK-18`, `SK-20`, `SK-22`, `SK-23`, `SK-25` e `SK-26` NAO sao
> tocadas — `22` regras —, e continuam com sede em `ADR-0033`, `ativo`.**

### 2.2 Por que identificadores NOVOS, e nao os mesmos numeros corrigidos

**Reenunciar `SK-09` sob o numero `SK-09` poria DOIS textos com o mesmo nome em DOIS artefatos
vigentes.** E **`SK-23` — que continua em vigor — chama isso pelo nome:** *"copiar o texto da norma
dentro da `Skill` cria **segunda sede que deriva em silencio**"*, familia de `RD-101`; e `PJ-01`:
*"tabela, matriz ou diagrama normativo vive em **exatamente uma fonte**"*.

> **Cometer o defeito de `SK-23` dentro do `ADR` que corrige o Framework de `SK-23` seria a forma
> mais cara possivel de errar.** **Numero novo, deslocamento declarado, sede unica por enunciado.**

---

## 3. `SK-09` — a medicao, com controle positivo

| Medida | Instrumento | Resultado |
|---|---|---|
| Blocos numerados de corpo em `TPL-skill` | `grep -c '^## [0-9]'` | **`11`** |
| **Controle positivo** *(blocos nao numerados)* | `grep -c '^## [^0-9]'` | **`7`** ✅ |
| `gatilho` no frontmatter de `TPL-skill` | `grep -c '^gatilho:'` | **`0`** |
| `capabilities` no frontmatter de `TPL-skill` | `grep -c '^capabilities:'` | **`0`** |
| **Controle positivo** *(`RD-122`)* | `grep -c '^proprietario:'` | **`2`** ✅ |
| **`gatilho` materializado nas fichas** | frontmatter **e** bloco de corpo | **`3` de `3`** |

> **Zero de instrumento morto e indistinguivel de zero real** — por isso os dois controles positivos
> antes de qualquer conclusao.

**O defeito:** `gatilho` e **atributo de frontmatter** (`FND-09 §E-13`), e `SK-09` o somou a uma
contagem de **blocos de corpo**. Para satisfazer *"doze"*, **as tres fichas o materializaram DUAS
vezes** — segunda sede dentro do mesmo arquivo.

> ### ⭐ Por que a hipotese de defeito de LEITOR caiu
>
> Em `n = 1` e `n = 2` o autor **desconhecia** o defeito. Na terceira **sabia**, escreveu um `§0`
> para separar as categorias — **e materializou o `gatilho` duas vezes assim mesmo**.
> **Conhecimento nao corrigiu o defeito. Sobra a hipotese de ENUNCIADO** — a unica que um sucessor
> pode sanar, e a razao de este `ADR` existir agora e nao depois da quarta `Skill`.

## 4. `SK-24` e `SK-21` — a classe, e por que o remedio e geral

### 4.1 A medicao, remedida nesta sessao e nao herdada

| Ficha | Linhas (`wc -l`) |
|---|---|
| `SKL-custodia-criar-copia-datada` | **`175`** |
| `SKL-seguranca-varrer-credencial` | **`188`** |
| `SKL-custodia-provar-restauracao-de-backup` | **`231`** |

**Mediana `188` · limiar `376` · maior `231` — NAO dispara.** Reproduz `ADR-0036 §1.2`.

### 4.2 O conjunto-solucao, que e o que prova o piso

| `n` | Mediana | Condicao para disparar | Conjunto-solucao |
|---|---|---|---|
| `1` | `a` | `a > 2a` ⟺ `a < 0` | ⛔ **VAZIO** |
| `2` | `(a+b)/2` | `b > a+b` ⟺ `a < 0` | ⛔ **VAZIO** |
| **`3`** | `b` | **`c > 2b`** | ✅ **NAO VAZIO** |

**`SK-21 (b)` tem a mesma forma com aresta no lugar de populacao:** exige que *"a cadeia nao tenha
ciclo"*, e **cadeia com `0` arestas nao tem ciclo por vacuidade** — o teste so pode responder
*"sim"*. **`0` dependencias entre componentes, medidas com `n = 3`.**

> **Duas regras distantes no documento — `§7` e `§8` de `ADR-0033` — falharam pelo MESMO motivo
> estrutural.** Corrigir uma a uma deixaria a **classe** viva para a proxima regra que dependa de
> populacao. **`SK-27` fecha a classe, e e por isso que o remedio e geral.**

### 4.3 ⭐ A VARREDURA — porque regra geral nao varrida e regra pontual com nome de geral

**As `26` foram percorridas UMA A UMA procurando antecedente que dependa de populacao ou de aresta.
A classe tem CINCO membros, nao dois — e os outros tres nao apareceram em missao alguma porque
ninguem os procurou.**

| Regra | Antecedente | **Piso apurado** | `n` atual | Estado sob `SK-27` |
|---|---|---|---|---|
| **`SK-21 (a)`** | *"`Skill` nao depende de agente"* | **`≥ 1` agente** | **`0`** | ⚠️ **INAPLICAVEL** — nunca *"satisfeita"* |
| **`SK-21 (b)`** | *"a cadeia nao tem ciclo"* (`R-04`) | **`≥ 1` aresta** de dependencia | **`0`** | ⚠️ **INAPLICAVEL** |
| **`SK-22`** | *"**Duas** `Skill`s que facam a mesma coisa"* | **`n ≥ 2`** instancias | **`3`** | ✅ **APLICAVEL**, e **exercida** |
| **`SK-24`** | *"o dobro da **mediana** do seu tipo"* | **`n ≥ 3`** instancias | **`3`** | ✅ **APLICAVEL** — nao dispara |
| **`SK-25`** | *"`Skill` superada **migra os dependentes**"* | **`≥ 1`** `Skill` superada | **`0`** | ⚠️ **INAPLICAVEL** |

**As demais `21` regras aferem-se dentro de UMA instancia** — contrato, gatilho, procedimento,
entradas, saidas, normas, custo, descontinuacao — **e nao tem antecedente de populacao nem de
aresta.** Nenhuma delas entra na classe.

> ### ⭐ A prova independente de que o piso e real, e ela nao foi construida para isto
>
> **`SK-22` tem piso `n ≥ 2` — e o registro do acervo diz que `SK-22` foi exercida pela PRIMEIRA
> vez na segunda `Skill`**, isto e, **exatamente em `n = 2`**. **A previsao de `SK-27` e o fato
> historico coincidem sem que ninguem os tivesse relacionado**, e a coincidencia foi **encontrada**
> ao varrer, nunca procurada para confirmar.

⚠️ **Correcao que esta varredura faz de leitura anterior:** `ADR-0036 §3` mediu que `SK-21 (a)` e
*"**vacuamente satisfeita** com `0` agentes"*, e o proprio termo *vacuamente* ja denunciava o
defeito. **Sob `SK-27` ela deixa de ser *satisfeita* e passa a `INAPLICAVEL`** — a distincao que
`§2` desta emissao chama de operacional: **a primeira desaparece do `FIT`; a segunda cobra o piso.**

⚠️ **E `SK-25` NUNCA foi medida por missao alguma.** Nao e regressao nem descuido das tres missoes
anteriores: **elas mediam a regra que a `Skill` da vez exercia**, e nenhuma `Skill` foi superada
ainda. **So a varredura por CLASSE a alcanca — e e a demonstracao de que o remedio geral encontra
o que o pontual nao encontraria.**

## 5. `SK-10` — o custo do rito, quarta medicao

| Missao | Materia | Artefatos | Reducao |
|---|---|---|---|
| `1.13.11` | primeira `Skill` | **`5`** | — |
| `1.13.12` | segunda `Skill` | **`5`** | **`0`** |
| `1.13.13` | terceira `Skill` | **`5`** | **`0`** |
| **`1.13.14`** | **este `ADR` — materia que NAO e `Skill`** | **`4`** | — |

> **A quarta medicao nao contradiz as tres: confirma a causa.** **`4 = 5 − 1`, e o `1` que falta e
> a ficha**, porque **nenhuma `Skill` e criada**. **O rito da classe — `RFC` → `ADR` → `FIT` → `PT`
> — veio inteiro**, sobre materia inteiramente diversa. **O custo e da CLASSE, nunca da novidade**,
> e e exatamente o que `SK-29` passa a advertir.

## 6. `SK-19` — o singular, medido em `2` de `3`

| Ficha | Saidas plausiveis-e-erradas | Singular bastou? |
|---|---|---|
| `custodia-criar-copia-datada` | **`1`** | ✅ sim |
| `seguranca-varrer-credencial` | **`2`** — falso negativo silencioso · ruido que desliga o portao | ❌ **nao** |
| `custodia-provar-restauracao-de-backup` | **`2`** — copia coerente e vazia · o veredito que viaja | ❌ **nao** |

> **As duas fichas que precisaram de mais de uma numeraram `(I)` e `(II)` por conta propria, contra
> a letra do enunciado.** **Quando a pratica corrige a norma em `2` de `3` casos, o defeito e da
> norma** — e a correcao e do tamanho medido: **plural**, nao portao novo.

## 7. ⚠️ `FIT-2026-029 R4` — AVALIADO, e fica de FORA

**O despacho manda avaliar e declarar. Declarado:**

| Sinal | Instancias | Piso de `SK-27` atingido? |
|---|---|---|
| `SK-09` · `SK-10` | `3` de `3` | ✅ |
| `SK-19` | `2` de `3` | ✅ |
| `SK-24` · `SK-21 (b)` | piso **provado** | ✅ |
| **`R4`** | ⚠️ **`1` de `3`** | ❌ **NAO** |

| # | Razao | Fundamento |
|---|---|---|
| **1** | **Uma instancia e antecipacao, nao sinal** | `FND-08 §7.1` recusa antecipacao; **`SK-20`, em vigor:** *"sinal antecipado nao serve"* |
| **2** | **`R4` nao e defeito de ENUNCIADO.** `SK-19`/`SK-30` obrigam a **DECLARAR**; obrigar a **IMPEDIR** e regra **nova**, de efeito diverso — nao correcao | `SU-01`: superacao exige explicar **o que deixou de servir**. Aqui nada deixou |
| **3** | **DEP-QAR ja declarou o objeto CORRETO** — *"o objeto esta correto e declara os proprios limites"*; *"exigir prova em `n` produtos seria criar portao que `ADR-0033` nao pede de nenhuma"* | `FIT-2026-029 §6.2`, criterio `FT-09` |

> ### O custo de nao entrar, declarado no sentido correto
>
> **Se o sinal amadurecer, custara OUTRO sucessor, tambem `M1`.** A economia enunciada no despacho
> **e real**, e a missao a **recusa assim mesmo** — porque o precedente contrario esta escrito
> **dentro de `ADR-0033`**: **`L3`** declara `SK-12` *"derivada da norma, **nao da experiencia**"*, e
> **`L2`** a nomeia ***"a parte MENOS testada"***. **Escrever a quinta regra por economia de rito
> repetiria, no sucessor, o defeito que motivou o sucessor** — e o remedio central desta emissao,
> `SK-27`, e precisamente a regra que proibe aplicar antecedente abaixo do piso.
>
> **Aplicar `SK-27` contra o interesse da propria missao e a unica forma de nao o ter escrito em
> vao.**

---

## 8. O que este ADR NAO faz

| # | Nao faz | Verificacao |
|---|---|---|
| **N1** | **Nao supera `ADR-0033` por inteiro** | Resultado **`AJUSTAR`** de `FND-07 §8.1`. `ADR-0033` segue **`ativo`**, com **`22`** regras vigentes e **`0` bytes** tocados |
| **N2** | **Nao promove `ADR-0033` nem a si mesmo a `FND`** | `C3 · Tipo 1` **com ato** — precedente `ADR-0022`. `FIT-2026-029 §8` recomenda **NAO**, e a razao permanece: `3` instancias sao **exercicio**, nao populacao (`FND-01 §6.2`) |
| **N3** | **Nao emenda fonte alguma** | **`0` bytes** em `FND-01` a `FND-11` |
| **N4** | **Nao emenda `TPL-skill` nem sana `RD-122`** | **`0` bytes.** `RD-122` segue **ABERTO**, exercido `3` vezes |
| **N5** | **Nao cria `Skill`, entidade, tipo, campo, template, diretorio, papel nem classe** | `MT-01`, `CS-01`. **`3`** `Skill`s antes, **`3`** depois |
| **N6** | **Nao cria nem libera portao** | **`GO-TO-SKILLS` continua EXERCIDO e NAO liberado** (`FND-01 §6.2`). Portoes de sequencia por nome: **`2` antes, `2` depois**. `QG-0`–`QG-6`: **`7` e `7`**. ⚠️ **Contados por NOME de portao existente, nunca por curinga** — o metodo de `ADR-0033 §N4`, que se auto-contamina |
| **N7** | **Nao admite o segundo candidato da F8** | Segue **fora do acervo, intacto** — *um por missao* |
| **N8** | **Nao decide `RD-116`** | Segue **ABERTO por determinacao expressa do Fundador**, com gatilho *"proxima emenda Fundacional"* |
| **N9** | **Nao move codigo para o acervo** | **`0` bytes.** As implementacoes seguem fora; o canonico tem as **fichas** |
| **N10** | **Nao emite ato, nao exige ratificacao e nao a antecipa** | **`0` atos.** `SU-02` **nao incide**: `ADR-0033` tem `ratificacao: nao-exigida`, conferido no frontmatter e nao de memoria |
| **N11** | **Nao altera o medidor de baseline** | **`0` bytes em `baseline.sh`**, inclusive diante do `EXIT=2` do portao de raiz sobre a copia datada — **OITAVA** ocorrencia de `RD-53`/`RD-81` |

## 9. Limites declarados

| # | Limite |
|---|---|
| **L1** | ⚠️ **Quem ler `ADR-0033` isolado le `SK-09` defeituosa SEM AVISO.** `CC-01` proibe o aviso dentro dele, e **isso nao se mitiga: e o custo da sede `M1`**, agora exercido e nao mais so previsto. **O aviso vive no catalogo mestre (`M3`) e neste `ADR`** |
| **L2** | **`SK-27` e a contribuicao propria e a MENOS testada.** Foi **derivada de duas instancias medidas** — `SK-24` e `SK-21 (b)` — e **aplicada a cinco** pela varredura de §4.3; mas **`SK-22` e `SK-25` entraram por LEITURA do enunciado, nunca por reprovacao observada**. **`SK-25` em particular nunca foi exercida por missao alguma.** **Mesma natureza de `L3` de `ADR-0033`, e declarada pelo mesmo motivo** |
| **L3** | **Nenhuma das quatro novas regras foi exercida.** Elas nascem **determinadas, nao observadas** — o mesmo estado em que `ADR-0033` nasceu, e o gatilho de revisao e o mesmo: **a quarta `Skill`** |
| **L4** | **`SK-29` adverte do custo; nao o reduz.** A reducao exigiria mudar `FND-04 §6` — **Fundacional**, `C3`, com ato. **Advertir e o maximo que um `ADR` pode fazer** |
| **L5** | **O piso de `SK-24` foi apurado, e a mediana com `3` pontos NAO e estavel.** Uma quarta `Skill` **move o limiar sem que ficha alguma mude** |
| **L6** | **`FIT-2026-029 R4` fica de fora com gatilho registrado** — e **se o sinal amadurecer custara outro sucessor `M1`**. O risco esta assumido, medido e escrito |

## 10. Consequencias

| Para quem | O que muda |
|---|---|
| **Quem for criar a quarta `Skill`** | **Nao escrevera mais o `gatilho` duas vezes** (`SK-28`) · **sabera o preco `5` antes de propor** (`SK-29`) · **declarara TODAS as saidas plausiveis e erradas** (`SK-30`) · **e ainda escrevera `gatilho` e `capabilities` a mao** — `RD-122` **nao e sanado aqui** |
| **DEP-QAR** | Ganha `INAPLICAVEL` como veredito de `FIT` distinto de ✅ — **regra abaixo do piso deixa de desaparecer no relatorio** (`SK-27`) |
| **DEP-GOV** | Ganha criterio para **nao escrever regra sem piso**, e o mesmo criterio o obriga a **nao generalizar de uma instancia** |
| **Framework** | Passa a ter **duas sedes vigentes** — `ADR-0033` para `22` regras, este para `4`. **A promocao a `FND`, que unificaria, segue `C3 · Tipo 1` com ato, e nao e feita aqui** |
| **Fundador** | **`0` atos.** O que espera decisao continua sendo **`Q1`** *(promover a `FND`?)* e **`RD-116`**, nenhum dos dois movido por esta missao |

## 11. Rastreabilidade

| Campo | Conteudo |
|---|---|
| **Origem** | [RFC-0032](../rfcs/RFC-0032-sucessor-parcial-do-framework-de-skills.md) → este `ADR` |
| **Supera parcialmente** | [ADR-0033](ADR-0033-framework-de-skills.md) — `SK-09`, `SK-10`, `SK-19`, `SK-24`, `SK-21 (b)`. **As outras `22` regras seguem nele, `ativo`** |
| **Sinal que o autorizou** | [ADR-0034](ADR-0034-primeira-skill-copia-datada.md) · [ADR-0035](ADR-0035-segunda-skill-varrer-credencial.md) · [ADR-0036](ADR-0036-terceira-skill-provar-restauracao-de-backup.md) — `3` exercicios sobre materias disjuntas |
| **Recomendacao acolhida** | [FIT-2026-029 §8](../governance/fitness/FIT-2026-029-terceira-skill.md), itens `1` a `4` e `6` |
| **Verificacao de aptidao** | [FIT-2026-030](../governance/fitness/FIT-2026-030-sucessor-parcial-do-framework-de-skills.md) |
| **Registro da missao** | [PT-2026-024](../governance/relatorio-transicao-2026-08-03-sucessor-parcial-skills.md) |
| **Achados que este `ADR` NAO fecha** | **`RD-122`** *(`TPL-skill` sem `gatilho`)* · **`RD-53`/`RD-81`** *(**oitava** da familia)* · **`RD-116`** · **`RD-109`** |
| **Gatilho de revisao** | A **quarta `Skill`** — primeiro exercicio real de `SK-27` a `SK-30`, e move o limiar de `SK-24`; **ou** a primeira **aresta de dependencia** entre componentes *(exerce `SK-21 (a)+(b)` e testa o piso de `SK-27`)*; **ou** o **segundo** `FIT` com ressalva da classe de `R4` *(ai `n = 2` e a materia passa a ser mensuravel)* |
| **Data de reavaliacao** | **2027-02-03** |
