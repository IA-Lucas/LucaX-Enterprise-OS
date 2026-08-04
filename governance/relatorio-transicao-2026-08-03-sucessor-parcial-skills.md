---
id: PT-2026-024-sucessor-parcial-do-framework-de-skills
titulo: Relatorio de transicao — Missao 1.13.14, o ADR sucessor de ADR-0033 pelo resultado AJUSTAR, e a varredura que achou tres membros a mais da classe
tipo: relatorio-de-transicao
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-08-03
atualizado_em: 2026-08-03
revisao_prevista: null
decisoes_relacionadas: [ADR-0033, ADR-0034, ADR-0035, ADR-0036, ADR-0037]
substitui: []
substituido_por: null
resumo: Abre o sucessor parcial de ADR-0033 pelo resultado AJUSTAR de FND-07 8.1, institui SK-27 a SK-30, varre as 26 regras por classe e apura cinco membros do piso de populacao ou aresta em vez dos dois enunciados, avalia FIT-2026-029 R4 e o deixa de fora por aplicacao da propria regra nova, e mede o rito da classe fora do dominio Skill pela primeira vez.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# PT-2026-024 — O sucessor parcial do Framework de `Skill`s

## 1. O que a missao entregou

**O `ADR` sucessor de `ADR-0033` foi ABERTO**, acolhendo a recomendacao de `FIT-2026-029 §8`.
**`ADR-0037`** supera **PARCIALMENTE** `ADR-0033` e institui **`SK-27` a `SK-30`**.

| Entregavel | Estado |
|---|---|
| [`RFC-0032`](../rfcs/RFC-0032-sucessor-parcial-do-framework-de-skills.md) | `aprovado` |
| [`ADR-0037`](../decisions/ADR-0037-sucessor-parcial-do-framework-de-skills.md) | `ativo` · `C2 · Tipo 2` · `ratificacao: nao-exigida` |
| [`FIT-2026-030`](fitness/FIT-2026-030-sucessor-parcial-do-framework-de-skills.md) | `apto-com-ressalva` — **`3`** ressalvas, **`0`** bloqueantes |
| Este `PT-2026-024` | `ativo` |
| **Baseline** | **`BL-2026-08-03-06`** — catalogo mestre §10.29 |
| **Atos** | **`0`** |

## 2. Pre-condicoes — todas verdes, e provadas por conteudo

| # | Pre-condicao | Resultado |
|---|---|---|
| `P1` | **Reproduzir `BL-2026-08-03-05`** | ✅ **`249` · `72.996` · manifesto `a0a07b2e…d625bac`**, `2` execucoes, `EXIT=0`. **Impressao `d4a61857…3ac64` — reproduz EXATAMENTE o `estado_no_fechamento` do token 28: `0` deriva** |
| `P2` | **Lease antes da primeira escrita** | ✅ **`fencing_token: 29`**, declarado pelo token 28 |
| `P3` | **Copia datada invocando a PRIMEIRA `Skill`, provada fiel POR CONTEUDO** | ✅ **`630/630`** `sha256` identico a origem, `EXIT=0` — **quarto uso real** da `SKL-custodia-criar-copia-datada`. **E `249/249` contra o `H-A`, diff vazio** |
| `P4` | **Ponto de partida por `H-A`** | ✅ manifesto de **`249`** artefatos, e **o `sha256` do proprio arquivo E a impressao digital** *(gerado na ordem de agregacao do instrumento)* |
| `P5` | **Oitava ocorrencia de `RD-53`/`RD-81`: declarar e seguir** | ✅ **OCORREU e foi CONTADA.** `IR-BL/5` sobre a copia: `EXIT=2`, *"entrada nao declarada na raiz: `MANIFESTO-DA-COPIA.txt`"*. **O despacho a previu e ela ocorreu — `0` correcao de contagem necessaria desta vez** |

> **Sobre a quarta grandeza da baseline publicada, e a nota e do tipo que nao se omite:** dos quatro
> valores de `BL-2026-08-03-05`, **tres reproduzem direto da arvore viva** — `249`, `72.996` e o
> manifesto. **O quarto (`d7909333…`) e por construcao irreproduzivel da arvore viva**, porque foi
> medido com os quatro campos em **placeholder** (`RD-109`). **Nao se afirma aqui que ele
> reproduziu:** afirma-se o que foi medido, e o que foi medido e a impressao **pos-inscricao**
> `d4a61857…`, registrada no token 28.

## 3. Item 0 — QUAL instrumento, determinado ANTES de redigir

**A pergunta nao era *"pode corrigir?"*.** `ADR-0033 §SK-26` ja respondia que sim, por sucessor.
**A pergunta era *"supera o todo, ou parte?"*, e as duas respostas produzem acervos diferentes.**

**`FND-07 §8.1` nomeia os tres resultados de revisao, e o do meio e o instrumento exato:**

| Resultado | Prescricao | Este caso |
|---|---|---|
| Confirmar | Nota de revisao mantida | ❌ quatro regras reprovaram **por medicao** |
| ⭐ **Ajustar** | **Novo `ADR` que supera PARCIALMENTE o anterior** | ✅ **DETERMINADO** |
| Superar | Rito de `FND-07 §7` | ❌ `22` de `26` seguem servindo |

**E a revisao nao foi inaugurada por esta missao: era DEVIDA.** `ADR-0033` fixou
*"Gatilho de revisao: a **primeira `Skill` real**"* — **tres dispararam**.

**O que a superacao total custaria, medido e nao suposto:** `LN-03` proibiria **criar** relacao com
`ADR-0033`, e as **`3`** fichas vigentes ja declaram `decisoes_relacionadas: [ADR-0033]`; e as
**`22`** regras integras teriam de ser **reproduzidas** — **`22` segundas sedes** contra `PJ-01` e
contra o proprio `SK-23`. **Trocar um defeito por vinte e dois.**

## 4. AS QUATRO CORRECOES, e a quinta que foi RECUSADA

### 4.1 `SK-09` → `SK-28` — erro de categoria, com dois controles positivos

| Medida | Resultado |
|---|---|
| Blocos numerados de corpo em `TPL-skill` | **`11`** *(controle positivo: `## ` sem numero = **`7`**)* ✅ |
| `gatilho` / `capabilities` no frontmatter do `TPL` | **`0`** / **`0`** *(controle positivo: `proprietario` = **`2`**)* ✅ |
| **`gatilho` materializado nas fichas** | **`3` de `3`** — frontmatter **e** bloco de corpo |

**`gatilho` e atributo de FRONTMATTER** (`FND-09 §E-13`). **`SK-09` o somou a uma contagem de blocos
de CORPO**, e para satisfazer *"doze"* **as tres fichas o escreveram duas vezes** — segunda sede
dentro do mesmo arquivo, familia de `RD-101`.

### 4.2 `SK-10` → `SK-29` — o rito vem inteiro

| Missao | Materia | Artefatos |
|---|---|---|
| `1.13.11` · `1.13.12` · `1.13.13` | `Skill` | **`5`** · **`5`** · **`5`** |
| **`1.13.14`** | **norma sobre o Framework** | **`4`** |

⚠️ **A quarta medicao NAO e reducao, e ler assim seria erro.** **`4 = 5 − 1`, e o `1` que falta e a
ficha**, porque nenhuma `Skill` foi criada. **O rito da classe veio INTEIRO sobre materia que nao e
`Skill`** — e isso **corrobora** `SK-29` pela primeira vez **fora do proprio dominio dela**.

### 4.3 `SK-19` → `SK-30` — o singular, `2` de `3`

| Ficha | Saidas plausiveis-e-erradas |
|---|---|
| `custodia-criar-copia-datada` | **`1`** |
| `seguranca-varrer-credencial` | **`2`** |
| `custodia-provar-restauracao-de-backup` | **`2`** |

**As duas que precisaram de mais numeraram `(I)` e `(II)` por conta propria, contra a letra do
enunciado.** **Quando a pratica corrige a norma em `2` de `3` casos, o defeito e da norma.**

### 4.4 ⭐ `SK-24` e `SK-21` → `SK-27` — e a VARREDURA acha **cinco**, nao dois

**O despacho mandava cobrir `SK-24` e `SK-21` *"de uma vez"*, na forma geral. A forma geral foi
escrita — e depois EXERCIDA sobre as `26`, uma a uma.**

| Regra | Antecedente | Piso | `n` atual | Estado |
|---|---|---|---|---|
| `SK-21 (a)` | *"nao depende de agente"* | `≥ 1` agente | **`0`** | ⚠️ **INAPLICAVEL** |
| `SK-21 (b)` | *"a cadeia nao tem ciclo"* | `≥ 1` aresta | **`0`** | ⚠️ **INAPLICAVEL** |
| **`SK-22`** | *"**Duas** `Skill`s que facam a mesma coisa"* | **`n ≥ 2`** | `3` | ✅ aplicavel |
| `SK-24` | *"o dobro da **mediana**"* | `n ≥ 3` | `3` | ✅ aplicavel, nao dispara |
| **`SK-25`** | *"`Skill` superada **migra os dependentes**"* | `≥ 1` superada | **`0`** | ⚠️ **INAPLICAVEL** |

**As outras `21` aferem-se dentro de UMA instancia e nao entram na classe.**

> ### ⭐ Os tres achados que so a varredura por CLASSE produz
>
> **(a) `SK-25` NUNCA foi medida por missao alguma.** Nao e descuido das tres anteriores: **cada
> uma mediu a regra que a `Skill` da vez exercia**, e nenhuma `Skill` foi superada. **So a
> varredura por classe a alcanca.**
>
> **(b) `SK-21 (a)` estava classificada errado.** `ADR-0036 §3` a chamou *"**vacuamente**
> satisfeita"* — e o proprio adverbio ja denunciava. **Sob `SK-27` ela e `INAPLICAVEL`**, e a
> diferenca e operacional: *satisfeita* entra no `FIT` como ✅ e **desaparece**; `INAPLICAVEL`
> **fica visivel e cobra o piso**. **`ADR-0036` fica com `0` bytes** — corrige-se a leitura pelo
> sucessor, jamais editando `M1`.
>
> **(c) A corroboracao que ninguem procurou.** **`SK-22` tem piso `n ≥ 2`, e o registro de
> `1.13.12` diz que `SK-22` foi exercida pela PRIMEIRA vez na SEGUNDA `Skill`** — **exatamente no
> piso**. **Previsao retrospectiva acertando sobre dado que ja existia**, encontrada **ao varrer**,
> nunca procurada para confirmar. **Conferida na fonte por DEP-QAR** *(`FIT-2026-030 §4`)*.

### 4.5 ⚠️ `FIT-2026-029 R4` — AVALIADO, e fica de FORA

| Sinal | Instancias | Piso de `SK-27` |
|---|---|---|
| `SK-09` · `SK-10` | `3` de `3` | ✅ |
| `SK-19` | `2` de `3` | ✅ |
| `SK-24` · `SK-21` | piso **provado** | ✅ |
| **`R4`** | ⚠️ **`1` de `3`** | ❌ **NAO atingido** |

**Tres razoes independentes, e nenhuma e economia:** *(1)* uma instancia e **antecipacao**
(`FND-08 §7.1`; **`SK-20`, em vigor:** *"sinal antecipado nao serve"*); *(2)* **`R4` nao e defeito
de ENUNCIADO** — `SK-19`/`SK-30` obrigam a **declarar**, e obrigar a **impedir** e regra **nova**,
que `SU-01` nao autoriza chamar de correcao; *(3)* **DEP-QAR ja declarara o objeto CORRETO**.

> **O despacho oferecia a economia de um `ADR`, e ela e REAL.** A missao **a recusa**, e o
> precedente contrario esta **dentro de `ADR-0033`**: **`L3`** declara `SK-12` *"derivada da norma,
> **nao da experiencia**"* e **`L2`** a nomeia ***"a parte MENOS testada"***. **Escrever a quinta
> regra por economia de rito repetiria, no sucessor, o defeito que motivou o sucessor.**
>
> **Gatilho registrado em `ADR-0037 §11`:** a **segunda** `Skill` com veredito consumido fora do
> contexto, **ou** o **segundo** `FIT` com ressalva da mesma classe. **Ai `n = 2`.**

## 5. Por que identificadores NOVOS

**Reenunciar `SK-09` sob o numero `SK-09` poria dois textos com o mesmo nome em dois artefatos
vigentes** — e **`SK-23`, que continua em vigor**, chama isso de *"segunda sede que deriva em
silencio"*; `PJ-01` exige *"exatamente uma fonte"*.

> **Cometer o defeito de `SK-23` dentro do `ADR` que corrige o Framework de `SK-23` seria a forma
> mais cara possivel de errar.**

## 6. O que a missao NAO fez

| # | Nao fez |
|---|---|
| `1` | **Nao promoveu `ADR-0033` nem `ADR-0037` a `FND`** — `C3 · Tipo 1` **com ato**. `FIT-2026-029 §8.6` e `FIT-2026-030 §7.5` recomendam **NAO** |
| `2` | **Nao superou `ADR-0033` por inteiro** — `0` bytes nele; `status: ativo`, `superado_por: null`, **os dois corretos** |
| `3` | **Nao admitiu o segundo candidato da F8** — segue fora, intacto |
| `4` | **Nao emendou `TPL-skill` nem sanou `RD-122`** — `0` bytes; aberto, exercido `3` vezes |
| `5` | **Nao emendou Fundacional** — `0` bytes em `FND-01` a `FND-11` |
| `6` | **Nao decidiu `RD-116`** — segue aberto por determinacao do Fundador |
| `7` | **Nao moveu codigo** — `0` bytes; `0` `Skill`s criadas *(`3` antes, `3` depois)* |
| `8` | **Nao alterou o medidor** — `baseline.sh` intacto, inclusive diante do `EXIT=2` |
| `9` | **Nao emitiu ato** — **`0`**; `10` `MSG`, todos com `0` bytes |

## 7. Observacoes que NAO viram achado novo

| # | Observacao | Por que nao e achado |
|---|---|---|
| `1` | **O Framework passa a ter DUAS sedes vigentes**, e ler `ADR-0033` isolado devolve `SK-09` defeituosa sem aviso | **Nao e defeito: e a propriedade da sede `M1`**, declarada por `ADR-0033` ao nascer e por `ADR-0037 §L1`. **Ja tem dono e remedio nomeados** — a promocao a `FND`, `C3` com ato |
| `2` | `SK-22` e `SK-25` entraram em `SK-27` por **leitura do enunciado**, nao por reprovacao observada | **Declarado em `ADR-0037 §L2` e ressalvado em `FIT-2026-030 §4`.** `SK-27` **nao reescreve enunciado nenhum**: acrescenta piso. **Errar o piso de `SK-25` custa um `FIT` mais conservador, nunca uma `Skill` recusada** |
| `3` | **Nenhuma das quatro regras novas foi exercida** | **Mesmo estado em que `ADR-0033` nasceu.** Declarado em `§L3`; gatilho de revisao **e a quarta `Skill`** |
| `4` | `SU-03` — superacao frequente indica materia mal enquadrada | **Esta e a TERCEIRA superacao do acervo, e a PRIMEIRA desta materia.** Uma segunda **desta materia** torna a pergunta devida, e o dono e o **Fundador** |

### 7.1 ⚠️ DEFEITO INTRODUZIDO PELA PROPRIA MISSAO, pego pelo instrumento e corrigido

**Nao e observacao sobre terceiro: e erro desta sessao, e omiti-lo seria `LV-12`.**

| O que | Medida |
|---|---|
| **O que ocorreu** | Quatro arquivos foram editados por script que leu em modo texto e reescreveu com `'\n'.join(...)`. **Em Windows isso converte o arquivo INTEIRO de `LF` para `CRLF`** |
| **Alcance, contado por `tr -cd '\r' \| wc -c`** | `artifact-registry` **`2.631`** · `decisions/README` **`170`** · `rfcs/README` **`121`** · `fitness/README` **`314`** = **`3.236`** bytes fora do diff pretendido. `roadmap-canonico`, editado por outra via, ficou com **`0`** |
| **Por que a contagem de linha NAO acusou** | `CRLF` **nao muda `wc -l`**. **`253` e `74.236` reproduziam, e o manifesto `IR-BL/1-3` tambem** — *"tres de quatro valores certos"* |
| ⭐ **O que acusou** | **A IMPRESSAO DIGITAL DE CONTEUDO**, na **prova por reversao**: restaurados os placeholders, o instrumento devolveu impressao **diferente** da medida minutos antes. **Nada mais na missao teria pego** |
| **Correcao** | `CRLF` → `LF` nos quatro, por escrita **binaria**; reconferido `0` `CR` nos cinco arquivos tocados. Baseline **remedida do zero** e reversao **refeita** |

> ### ⭐ Tres coisas que este defeito PROVA, e nenhuma delas e sobre `CRLF`
>
> **(1) `IR-BL/4` nao foi melhoria cosmetica.** A impressao de conteudo foi instituida em
> 2026-08-03 porque o hash de manifesto *"nunca leu um byte de conteudo"* — **e esta e a primeira
> vez que a diferenca importou na pratica**. **Ate `IR-BL/3` esta missao teria fechado verde com
> `3.236` bytes errados no acervo.**
>
> **(2) Receita que so se declara nao e receita.** A reversao foi executada **porque o precedente a
> exige**, nao porque se suspeitasse de algo — e foi **ela** que pegou. **Prova que so passa nao
> prova nada.**
>
> **(3) Medir `CR` com `grep -c $'\\r'` daria falso positivo uniforme.** Contou-se **byte**, com
> `tr -cd '\r' | wc -c`, e por isso o `0` de `roadmap-canonico` **e distinguivel** dos `2.631` do
> catalogo.

## 8. Cobertura das `26` — o que esta emissao muda

| Estado | Antes | Depois |
|---|---|---|
| Regras com sede em `ADR-0033` | **`26`** | **`22`** |
| Regras com sede em `ADR-0037` | `0` | **`4`** *(`SK-27` a `SK-30`)* |
| **Total de regras do Framework** | **`26`** | **`30`** |
| Regras **deslocadas** | — | **`5` leituras** — `SK-09`, `SK-10`, `SK-19`, `SK-24`, `SK-21` |
| Regras **INAPLICAVEIS** declaradas *(estado novo, que antes nao existia)* | `0` | **`3`** — `SK-21 (a)`, `SK-21 (b)`, `SK-25` |

## 9. Recomendacao para a proxima missao

| # | Recomendacao | Dono |
|---|---|---|
| `1` | **A quarta `Skill` e o primeiro exercicio real de `SK-27` a `SK-30`.** Medir se `SK-28` **elimina** o `gatilho` duplicado — hoje `3` de `3` | DEP-GOV |
| `2` | **Registrar `SK-25` como `INAPLICAVEL` no proximo `FIT` de `Skill`**, nunca omiti-la. **E o primeiro teste real de que `SK-27` muda o relatorio** | DEP-QAR |
| `3` | **Decidir `RD-122` antes da quarta ficha**, ou registrar que se optou por paga-lo pela quarta vez. **Reiterada e ainda nao atendida** | DEP-GOV |
| `4` | ⛔ **Nao promover a `FND` sem ato**, e **nao abrir quinto membro de `SK-27` sem `n ≥ 2`** | Fundador · DEP-GOV |

## 10. Decisao

**ABERTO.** O sucessor parcial de `ADR-0033` existe desde **2026-08-03**, pelo resultado **`AJUSTAR`**
de `FND-07 §8.1`.

> ### ⚠️ Afirmacao RETIRADA antes de ser publicada, e o registro fica
>
> **A primeira redacao deste paragrafo dizia *"a PRIMEIRA superacao de `ADR` na historia do
> acervo"*. E FALSO, e a medicao o derrubou:** `grep` do campo `supera:` nos **`37`** `ADR` devolve
> **`28` `[]` · `6` `null` · `3` preenchidos** — **`ADR-0022` supera `ADR-0021`**, **`ADR-0027`
> supera `ADR-0007`**, e este. **Esta e a TERCEIRA.**
>
> **E o que a medicao encontrou vale mais do que a afirmacao que ela derrubou:** nos **`37`** `ADR`,
> `superado_por` e **`null` em `37` de `37`** — inclusive em `ADR-0007` e `ADR-0021`, que **seguem
> `ativo`** depois de superados. **O acervo ja praticava, duas vezes, exatamente a construcao desta
> missao: superacao PARCIAL, com o superado vigente e o espelho fora do frontmatter** (`LN-01`).
> **`ADR-0037` nao inaugura o instrumento — segue precedente conferido no frontmatter, nao de
> memoria.**

**`SK-27` a `SK-30` nascem determinadas e nao observadas.** **`GO-TO-SKILLS` continua EXERCIDO e NAO
liberado** *(`FND-01 §6.2`)*: portoes de sequencia por nome **`2` antes, `2` depois**; `QG-0`–`QG-6`
**`7` e `7`**.

**`0` atos · `0` Fundacionais emendadas · `0` bytes em `TPL-skill` · `0` bytes em `ADR-0033` a
`ADR-0036` · `0` bytes de codigo · `0` bytes no medidor · `0` `Skill`s criadas · segundo candidato
da F8 NAO admitido · `ADR-0033` NAO promovido a `FND` · `RD-122` NAO sanado · `RD-116` NAO decidido ·
`0` achados novos inscritos.**
