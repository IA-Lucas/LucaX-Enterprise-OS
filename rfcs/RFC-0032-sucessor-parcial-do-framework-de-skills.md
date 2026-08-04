---
id: RFC-0032-sucessor-parcial-do-framework-de-skills
titulo: O sucessor parcial de ADR-0033 — a classe de defeito comum a SK-24 e SK-21, o erro de categoria de SK-09, a insuficiencia de SK-10 e o singular de SK-19
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
decisoes_relacionadas: [ADR-0033, ADR-0034, ADR-0035, ADR-0036]
substitui: []
substituido_por: null
classe_mudanca: C2
prazo_analise: 2026-08-03
---

# RFC-0032: O sucessor parcial do Framework de `Skill`s

## Proposito

**Corrigir `ADR-0033` no unico instrumento que a norma admite para artefato `M1`** — um `ADR`
sucessor —, e corrigi-lo **na forma geral**, porque **dois dos quatro defeitos sao a mesma classe**
e um remedio pontual deixaria a classe viva.

> **Este `RFC` nao propoe uma `Skill`.** Os tres `RFC` anteriores da cadeia — `RFC-0029`,
> `RFC-0030`, `RFC-0031` — propunham cada um a admissao de uma capacidade. **Este propoe a
> correcao do instrumento que julgou as tres**, e o sinal que o autoriza foi produzido **por elas**.

## Escopo

| Item | Definicao |
|---|---|
| **Entra** | A correcao de **`SK-09`**, **`SK-10`**, **`SK-19`** e — pela classe comum — **`SK-24`** e **`SK-21 (b)`** |
| **NAO entra** | A promocao de `ADR-0033` ou do sucessor a `FND` *(`C3 · Tipo 1`, com ato)* · a emenda de `TPL-skill` e o saneamento de `RD-122` *(`C2` sobre `TPL`, missao propria)* · qualquer emenda Fundacional · a decisao de `RD-116` · a admissao do segundo candidato da F8 · a criacao de `Skill` |
| **Fronteira com `ADR-0033`** | **Superacao PARCIAL.** As **`22`** regras nao alcancadas **continuam vigorando em `ADR-0033`, que permanece `ativo`** |

---

## 1. Item 0 — qual e o instrumento competente, determinado ANTES de redigir

**A pergunta nao e *"pode-se corrigir?"* — `ADR-0033 §SK-26` ja responde que sim, por sucessor.
A pergunta e *"corrige-se superando o todo, ou parte?"*, e as duas respostas produzem acervos
diferentes.**

### 1.1 A regra que fecha a porta da emenda

| Norma | O que diz | Consequencia aqui |
|---|---|---|
| `FND-10 §6.2` | `ADR` e **`M1` — imutavel apos eficacia**: *"o texto **nunca** muda; muda apenas o estado e os campos de sucessao"* | **`0` bytes** em `ADR-0033` |
| `AC-10` | *"Artefato `M1` nunca e emendado, logo `AC-08` nunca o alcanca. Corrige-se **superando**"* | Emenda por versao **nao esta disponivel** |
| `CC-01` | *"`ADR` historico **nunca** e editado — nem para corrigir erro"* | Nem uma virgula |
| `CC-06` | *"Artefato `M1` com erro material gera **novo artefato**"* | Este `ADR` |
| `SU-01` | *"Superacao sem explicar **o que mudou** e substituicao de opiniao, nao decisao. **E devolvida**"* | §2 a §5 existem para isso |

> **Nada disto e descoberta desta missao: e o preco que `ADR-0033` declarou ao nascer**, na sua
> propria caixa de tradeoff — ***"a sede barata e a sede mais cara de corrigir"***. **A missao paga
> o preco anunciado; nao o descobre.**

### 1.2 ⭐ A determinacao: `AJUSTAR`, e a norma nomeia o instrumento

**`FND-07 §8.1` — *Resultado da revisao* — enumera TRES resultados, e o do meio e exatamente este:**

| Resultado | Acao prescrita | E este caso? |
|---|---|---|
| **Confirmar** | Nota registrando que foi revista e mantida | ❌ **nao** — quatro regras reprovaram por medicao |
| ⭐ **Ajustar** | **Novo `ADR` que supera PARCIALMENTE o anterior** | ✅ **SIM** |
| **Superar** | Novo `ADR` pelo rito de `§7` | ❌ **nao** — `22` das `26` regras seguem servindo |

**E o gatilho da revisao ja disparou, tres vezes, e esta escrito no proprio `ADR-0033`:**
*"Gatilho de revisao: **a primeira `Skill` real** (`L1`)"*. **`ADR-0034`, `ADR-0035` e `ADR-0036`
o dispararam.** Este `RFC` **nao inaugura** a revisao: **entrega o resultado dela**.

### 1.3 Por que NAO o rito de `§7` — e a razao e operacional, nao estetica

**Superar o todo poria `ADR-0033` em `status: superado`.** E `LN-03` de `FND-10 §7.2` diz:
***"Relacao com artefato `depreciado`, `superado` ou `revogado` nao pode ser CRIADA"***.

| Consequencia | Efeito medido |
|---|---|
| As **`22`** regras nao corrigidas perderiam a sede vigente | Teriam de ser **reproduzidas** no sucessor — **segunda sede**, que e o defeito que `SK-23` e `PJ-01` nomeiam |
| Nenhuma `Skill` futura poderia declarar `decisoes_relacionadas: [ADR-0033]` | `LN-03`. As **`3`** fichas existentes ja o declaram |

> **Superar o todo para corrigir `4` de `26` custaria reproduzir `22` regras integras dentro de um
> artefato novo — e cada reproducao e uma sede a mais que deriva em silencio.** **`AJUSTAR` existe
> na norma exatamente para nao pagar isso.**

### 1.4 Onde o espelho da sucessao e declarado — medido, nao presumido

**`supera` e `R-08`, e `R-08` NAO esta na excecao de `LN-02`:**

| Regra | O que fixa |
|---|---|
| `LN-01` | *"**Bilateralidade e do registro, nao do frontmatter.** A relacao e declarada uma vez, **na fonte**, e o espelho e derivado"* |
| `LN-02` | A excecao — declarar nos dois lados — vale para **`substitui`/`substituido_por`**, e **so** |

**Logo:** `supera: [ADR-0033]` e declarado **neste sucessor**, e o espelho vive no **catalogo
mestre** (`M3`), reconciliado na **mesma mudanca** (`CC-03`, `CV-04`). **`ADR-0033` fica com
`0` bytes, e `superado_por: null` continua CORRETO — nao e omissao: ele nao esta superado.**

### 1.5 ⭐ E o precedente foi MEDIDO depois de a norma ter decidido — nao antes

**Varredura de `supera:` nos `37` `ADR`:** **`28` `[]` · `6` `null` · `3` preenchidos** —
**`ADR-0022` supera `ADR-0021`**, **`ADR-0027` supera `ADR-0007`**, e este.
**`superado_por` preenchido: `0` de `37`.** **Status dos dois superados: `ativo` nos dois.**

> **Esta e a TERCEIRA superacao de `ADR` do acervo, e nas duas anteriores o superado ficou `ativo`,
> com `superado_por: null`** — **exatamente o que `LN-01` prescreve e o que `§1.4` determinou aqui
> ANTES de olhar o precedente.** E **`ADR-0022` supera `ADR-0021`**, que e o `ADR` que o proprio
> `ADR-0033` cita como **precedente identico** da sua classe: **mesma materia, mesma sede barata,
> mesmo desfecho.**

---

## 2. `SK-24` e `SK-21` — **uma** classe, nao dois defeitos

### 2.1 O que `ADR-0036 §3.2` entregou, e o que falta fazer com isso

| Regra | Piso real | Declarado no enunciado? | Como se manifestou |
|---|---|---|---|
| **`SK-24`** | **`n ≥ 3`** instancias do tipo | ❌ nao | Devolveu *"nao"* em `n=1` e `n=2` por **impossibilidade algebrica**, indistinguivel de *"nao"* informativo |
| **`SK-21 (b)`** | **`≥ 1`** aresta de dependencia entre componentes | ❌ nao | Registrada como *"nao exercida por falta de agentes"* — **razao errada**, medida em `ADR-0036 §3` |

### 2.2 A medicao propria desta missao — remedida, nunca herdada (`SK-20`)

**`wc -l` sobre as tres fichas, nesta sessao:**

| Ficha | Linhas |
|---|---|
| `SKL-custodia-criar-copia-datada` | **`175`** |
| `SKL-seguranca-varrer-credencial` | **`188`** |
| `SKL-custodia-provar-restauracao-de-backup` | **`231`** |
| **Mediana** | **`188`** · **limiar `376`** · **maior `231`** — **nao dispara** |

**Reproduz `ADR-0036 §1.2` digito a digito.** *(Memoria de missao: **candidato de fabrica chega
vencido** — remedir mediana, contador e baseline e passo do rito, e aqui foi exercido.)*

### 2.3 ⭐ Por que a forma GERAL, e nao dois remendos

**Duas regras distantes no documento — `§7` e `§8` de `ADR-0033` — falharam pelo MESMO motivo
estrutural:** o antecedente exige uma **populacao** ou uma **aresta** que o enunciado **nao
declara**, e o resultado e um teste que so pode responder uma coisa.

> **Teste com uma unica resposta possivel nao esta medindo — esta decorando.** E o pior efeito nao
> e o falso negativo: e que **o *"nao"* de regra vazia entra no `FIT` como ✅ e DESAPARECE**,
> enquanto um **`INAPLICAVEL`** ficaria visivel e **cobraria o piso**.

**Corrigir so `SK-24` e so `SK-21` deixaria a classe viva para a proxima regra que dependa de
populacao.** **`SK-27` fecha a classe.**

### 2.4 ⚠️ E a classe tem CINCO membros, nao dois — apurado varrendo as `26`

**Ao percorrer as `26` uma a uma, a classe revelou-se maior do que o sinal que a originou:**

| Regra | Antecedente | Piso | `n` atual |
|---|---|---|---|
| `SK-21 (a)` | *"nao depende de agente"* | `≥ 1` agente | **`0`** |
| `SK-21 (b)` | *"a cadeia nao tem ciclo"* | `≥ 1` aresta | **`0`** |
| **`SK-22`** | *"**Duas** `Skill`s que facam a mesma coisa"* | **`n ≥ 2`** | `3` ✅ |
| `SK-24` | *"o dobro da **mediana**"* | `n ≥ 3` | `3` ✅ |
| **`SK-25`** | *"`Skill` superada **migra os dependentes**"* | `≥ 1` superada | **`0`** — **nunca medida por missao alguma** |

> **`SK-22` e `SK-25` nao apareceram em tres missoes porque cada uma media a regra que a `Skill` da
> vez exercia. So a varredura POR CLASSE as alcanca** — e e a demonstracao pratica de que o remedio
> geral encontra o que o pontual nao encontraria. **Regra geral nao varrida seria regra pontual com
> nome de geral.**

---

## 3. `SK-09` — erro de categoria, medido com controle positivo

**O enunciado:** *"Os blocos obrigatorios sao os **ONZE** do template vigente, **mais o `gatilho`:
doze**."*

### 3.1 A medicao

| Medida | Instrumento | Resultado |
|---|---|---|
| Blocos numerados de corpo em `TPL-skill` | `grep -c "^## [0-9]"` | **`11`** — `§1` a `§11` |
| `gatilho` no frontmatter de `TPL-skill` | `grep -c "^gatilho:"` | **`0`** |
| `capabilities` no frontmatter de `TPL-skill` | `grep -c "^capabilities:"` | **`0`** |
| **Controle positivo** *(sem ele, `0` de instrumento morto e indistinguivel de `0` real)* | `grep -c "^proprietario:"` | **`2`** ✅ |
| **`gatilho` materializado nas fichas** | frontmatter **e** bloco de corpo | **`3` de `3`** — `1` + `1` em cada |

### 3.2 O defeito, nomeado

**`gatilho` e ATRIBUTO DE FRONTMATTER** — `FND-09 §E-13` o lista entre os *atributos minimos*,
ao lado de `capabilities`, **nunca entre blocos de corpo**. **Soma-lo a uma contagem de blocos e
somar grandezas de categorias diferentes.**

**A consequencia foi medida, e nao e teorica:** para satisfazer *"doze blocos"*, **as tres fichas
materializaram o `gatilho` DUAS vezes** — no frontmatter, onde a norma o quer, e num `§1` de corpo,
onde a contagem o exigia. **Isso e segunda sede dentro do mesmo arquivo**, familia de `RD-101`,
e e o defeito que `SK-23` proibe.

> ### ⭐ Por que a terceira ocorrencia decide, e nao apenas repete
>
> **Nas duas primeiras, o autor desconhecia o defeito.** Restava a hipotese de **defeito de
> LEITOR**. **Na terceira o autor SABIA, escreveu um `§0` para separar as categorias — e
> materializou o `gatilho` duas vezes assim mesmo.** **Conhecimento nao corrigiu o defeito.**
> **A hipotese de leitor CAI, e sobra a de ENUNCIADO** — que e a unica que um sucessor pode sanar.

---

## 4. `SK-10` — insuficiente, e a medicao do custo fecha a questao

**O enunciado remete a autoridade a classe do efeito — e esta correto no que diz.** O que lhe falta
e a **advertencia**: **`C2` nao e so *"quem aprova"*; `C2` arrasta o RITO INTEIRO.**

| Missao | `Skill` | Artefatos do rito | Reducao |
|---|---|---|---|
| `1.13.11` | primeira | **`5`** | — |
| `1.13.12` | segunda | **`5`** | **`0`** |
| `1.13.13` | terceira | **`5`** | **`0`** |

> **A terceira medicao e a conclusiva: o candidato DECLAROU o preco antes**, no `§11` dele, **e o
> preco nao mudou**. **Conhecer o custo nao o desconta.**

**A causa e normativa:** a classe e a do **efeito** (`AL-01`), e `FND-04 §6` diz ***"alem do rito da
classe"***. **O barato e o ATO — `0` em tres missoes; o rito nunca foi barato**, e `SK-10` deixa
quem le acreditar que a `Skill` e o componente barato do acervo.

---

## 5. `SK-19` — o singular, medido em `2` de `3`

**O enunciado:** *"Os modos de falha conhecidos incluem obrigatoriamente **a saida PLAUSIVEL E
ERRADA**"* — **artigo definido, substantivo no singular**.

| Ficha | Saidas plausiveis-e-erradas declaradas | Singular bastou? |
|---|---|---|
| `custodia-criar-copia-datada` | **`1`** — `VERIFICADO` com arquivo divergente | ✅ sim |
| `seguranca-varrer-credencial` | **`2`** — falso negativo silencioso · ruido que desliga o portao | ❌ **nao** |
| `custodia-provar-restauracao-de-backup` | **`2`** — copia coerente e vazia · o veredito que viaja | ❌ **nao** |

**`2` de `3`.** As duas fichas que precisaram de mais de uma **numeraram `(I)` e `(II)` por conta
propria**, contra a letra do enunciado. **Quando a pratica corrige a norma em `2` de `3` casos,
o defeito e da norma.**

---

## 6. ⚠️ `FIT-2026-029 R4` — AVALIADO, e a proposta e que **NAO entre**

**O despacho manda avaliar e declarar. Avaliado, com o criterio desta propria missao aplicado
contra o proprio interesse dela.**

### 6.1 O que `R4` registra

| Parte | Observacao de DEP-QAR |
|---|---|
| **6.1** | *"O veredito que viaja"* — nao ha **portao** que impeca reusar veredito de um repositorio como prova de outro. `SK-19` obriga a **DECLARAR** o modo de falha, **nao a IMPEDI-LO** |
| **6.2** | O merito vem de **`1`** produto, `1` ferramenta, `1` banco. A generalidade da ficha e **projetada, nao observada** |

### 6.2 ⭐ Por que fica de fora — e a razao e a regra que esta missao esta criando

**`SK-27` — o remedio central deste sucessor — diz que regra cujo antecedente dependa de POPULACAO
so se aplica acima do seu piso. Aplicar isso ao proprio sucessor:**

| Sinal | Instancias medidas | Piso para generalizar |
|---|---|---|
| `SK-09` | **`3` de `3`** | ✅ atingido |
| `SK-10` | **`3` de `3`** | ✅ atingido |
| `SK-19` | **`2` de `3`** | ✅ atingido |
| `SK-24` | piso **provado algebricamente**, `n = 3` | ✅ atingido |
| **`R4`** | ⚠️ **`1` de `3`** — a ressalva aparece **so** no terceiro `FIT` | ❌ **NAO atingido** |

**E ha tres razoes independentes, e nenhuma delas e economia:**

| # | Razao | Fundamento |
|---|---|---|
| **1** | **Sinal de uma instancia e antecipacao.** *"Vai acontecer de novo"* e conjectura | `FND-08 §7.1` recusa antecipacao · `SK-20`: ***"sinal antecipado nao serve"*** |
| **2** | **`R4` nao e defeito de ENUNCIADO.** `SK-19` faz exatamente o que diz: obriga **declarar**. Obrigar a **impedir** seria regra **nova**, com efeito diferente — nao correcao | `SU-01` exige explicar **o que deixou de servir**; aqui nada deixou |
| **3** | **DEP-QAR ja declarou o objeto CORRETO.** *"O objeto esta correto e declara os proprios limites"*, e *"exigir prova em `n` produtos seria criar portao que `ADR-0033` nao pede de nenhuma"* | `FIT-2026-029 §6.2`, criterio `FT-09` |

> ### ⚠️ O custo de nao entrar, declarado no sentido correto e nao no que convem
>
> **Se o sinal amadurecer, custara OUTRO `ADR` sucessor — e o sucessor tambem sera `M1`.** O
> despacho enunciou essa economia, e ela **e real**. **A missao a recusa assim mesmo**, porque o
> precedente contrario ja esta escrito **dentro de `ADR-0033`**: **`L3`** declara que `SK-12` foi
> *"derivada da norma, **nao da experiencia**"*, e `L2` a nomeia ***"a parte MENOS testada"***.
> **Escrever a quinta regra por economia de rito repetiria, no sucessor, o defeito que motivou o
> sucessor.**
>
> **Gatilho registrado, para que a espera nao seja esquecimento:** a **segunda** `Skill` cujo
> veredito seja consumido fora do contexto que o produziu, **ou** o **segundo** `FIT` que levante
> ressalva da mesma classe. **Ai `n = 2`, e a classe passa a ser mensuravel.**

---

## 7. Decisao proposta

**Emitir `ADR-0037`** — sucessor **PARCIAL** de `ADR-0033` pelo resultado **`AJUSTAR`** de
`FND-07 §8.1` —, instituindo **`SK-27` a `SK-30`**:

| Nova | Materia | Desloca de `ADR-0033` |
|---|---|---|
| **`SK-27`** | **Piso de populacao e de aresta** — a forma GERAL, **com a classe VARRIDA** | A leitura de **`SK-21 (a)`** · **`SK-21 (b)`** · **`SK-22`** · **`SK-24`** · **`SK-25`** — **cinco membros**, apurados um a um |
| **`SK-28`** | **Duas categorias que nao se somam** — frontmatter × blocos de corpo | **`SK-09`** |
| **`SK-29`** | **A autoridade e derivada, E o rito da classe vem inteiro** | **`SK-10`** |
| **`SK-30`** | **Saidas plausiveis e erradas, no PLURAL** | **`SK-19`** |

**Identificadores NOVOS, e a razao e normativa, nao estilistica:** reenunciar sob os mesmos numeros
poria **dois textos com o mesmo nome** em dois artefatos vigentes — **exatamente a segunda sede que
`PJ-01` e `SK-23` proibem**, e dentro do documento que institui `SK-23`.

### Classe proposta

| Variavel | Valor | Fundamento |
|---|---|---|
| **Classe** | **`C2`** | `AL-01` — a classe e a do **efeito**, e o efeito e **instituir norma sobre entidade existente**; `FND-04 §2.1`: `C2` → **`RFC` → `ADR`**. **Identica a de `ADR-0033`**, e a superacao nao muda a classe da materia |
| **Tipo** | **`2` — reversivel** | `FND-04 §2.2`. Norma em `ADR` e superavel por `ADR` sucessor |
| **Aprovador** | **`DEP-EXE`**, parecer de **`DEP-GOV`** | `FND-04 §2.2`, celula `C2 × Tipo 2`. `PI-05`: **`DEP-GOV` nao aprova o que propos** |
| **Ratificacao** | **nao exigida** | `FND-04 §2.1` *(nao e `Tipo 1`)*; `FND-09 §8.2` linha `ADR` — *`SOBERANO` se `C3` ou `Tipo 1`*. **`SU-02` nao incide: `ADR-0033` NAO foi ratificado** *(`ratificacao: nao-exigida`, conferido no frontmatter)* |
| **Atos** | **`0`** | — |

**Rito:** `RFC-0032` → `ADR-0037` → `FIT-2026-030` → `PT-2026-024` = **`4` artefatos**.
**`5` menos a ficha**, porque **nenhuma `Skill` e criada** — e e a **quarta** medicao do custo de
`SK-29`, agora sobre materia que **nao** e `Skill`.

## 8. Riscos

| # | Risco | Mitigacao |
|---|---|---|
| `R1` | **O sucessor tambem e `M1`.** Errar aqui custa **outro** sucessor | Os quatro sinais entram **medidos em `3` instancias disjuntas**; o quinto (`R4`) **fica de fora por piso** |
| `R2` | **Dois artefatos vigentes descrevem o mesmo Framework** | `SK-27` a `SK-30` **declaram o que deslocam**, tabela a tabela; o catalogo mestre reconcilia na **mesma mudanca** |
| `R3` | **Quem ler `ADR-0033` isolado le `SK-09` defeituosa sem aviso** | ⚠️ **NAO se mitiga, e nao se dissimula:** `M1` proibe o aviso dentro dele (`CC-01`). **E o custo declarado da sede barata**, e fica em `L1` do sucessor |
| `R4` | **`SU-03`** — superacao frequente indica materia mal enquadrada | **Primeira** superacao desta materia. A promocao a `FND` **continua sendo** a resposta se houver segunda, e **nao e feita aqui** |

## 9. Perguntas abertas

| # | Pergunta | Dono |
|---|---|---|
| `Q1` | **Promover o Framework a `FND`?** | **Fundador** — `C3 · Tipo 1`, **com ato**. `FIT-2026-029` recomenda **NAO**, e a razao permanece: `3` instancias sao **exercicio**, nao populacao |
| `Q2` | **`RD-122`** — sanar `TPL-skill` ou pagar `2` campos a mao pela quarta vez? | **DEP-GOV**, missao propria. **Nao se estima o ponto de cruzamento** (`CE-04`) |
