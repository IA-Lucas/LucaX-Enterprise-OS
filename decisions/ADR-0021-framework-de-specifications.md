---
id: ADR-0021-framework-de-specifications
titulo: Framework de Specifications — SF-01 a SF-32, contrato, semantica, perfis, ciclo e economia de contexto, sem emendar fonte alguma
tipo: adr
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-PRD
proprietario: DEP-PRD
aprovador: DEP-EXE
criado_em: 2026-07-29
atualizado_em: 2026-07-29
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0005, ADR-0008, ADR-0009, ADR-0012, ADR-0015, ADR-0018, ADR-0019, ADR-0020]
substitui: []
substituido_por: null
classe_mudanca: C2
tipo_decisao: 2
supera: null
superado_por: null
resumo: Institui o Framework de Specifications como SF-01 a SF-32 dentro do proprio ADR, corrige TPL-spec por RD-23, e declara que nenhuma Spec e criavel hoje porque tres fontes vigentes vinculam Spec a Produto e nao existe Produto.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# ADR-0021: Framework de Specifications

> **Decisao em tres frases.** **Uma `Spec` declara o que deve ser verdadeiro, sob que condicao,
> e por qual evidencia isso sera aceito** — nada mais. Sua norma passa a viver em **`SF-01` a
> `SF-32`, dentro deste ADR**, na forma que `ADR-0012`, `ADR-0015` e `ADR-0020` ja usaram, com
> **zero** arquivos de `foundation/` alterados. **E nenhuma `Spec` e criavel hoje:** tres fontes
> vigentes a vinculam a `Produto`, nao existe `Produto`, e criar `Produto` e ato do **SOBERANO**.

## Proposito

Dar sede a norma da `Spec`, corrigir o achado **`RD-23`** no [`TPL-spec`](../foundation/templates/TPL-spec.md)
pelo rito aplicavel, e registrar — com as fontes citadas por identificador — por que os dois
pilotos pedidos pela Missao 1.13 **nao podem existir** sem ato do Soberano.

## Escopo

| Item | Definicao |
|---|---|
| **Inclui** | `SF-01` a `SF-32`; o **Spec Contract**; a semantica normativa de requisito; os **sete perfis**; o mapeamento `C0`–`C3` × `Tipo 1/2` como **projecao declarada**; a cadeia de rastreabilidade e as **seis relacoes**; **DoR** e **DoD**; o regime de mudanca; a economia de contexto; a correcao de `TPL-spec` **1.1.0**; a declaracao do vinculo `Spec × Produto` |
| **Nao** inclui | **Qualquer emenda a `foundation/`** · `Skill`, `Tool`, `Command`, `Workflow`, `Agente`, `Produto`, `Projeto`, codigo, banco, infraestrutura, ontologia, migracao · `FND` novo · entidade, tipo documental, portao, papel, departamento, classe ou verbo de autoridade novos · o **merito** de `ADR-0018`, `ADR-0019`, `ADR-0020` · `RD-24`, `RD-27`, `RD-28`, `RD-30`, `RD-10` a `RD-13`, `RD-18`, `RD-21` |
| **Subordinado a** | [FND-01](../foundation/01-constituicao.md) · [FND-03](../foundation/03-taxonomia.md) · [FND-04](../foundation/04-governanca.md) · [FND-07](../foundation/07-framework-decisoes.md) · [FND-08](../foundation/08-capability-framework.md) · [FND-09](../foundation/09-meta-model.md) · [FND-10](../foundation/10-artifact-framework.md) |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| **Propoe / autor** | **DEP-PRD** | [FND-09 §8.2](../foundation/09-meta-model.md), linha `SPC` — *propoe/cria*; [DEP-PRD §3](../departments/prd/carta.md) `P-4`, `P-5`, `P-9`; autonomia **A2** |
| **Revisores independentes** | **DEP-ENG** + **DEP-QAR** | FND-09 §8.2, linha `SPC` — *revisa*; `AC-03`; `I-2` de DEP-PRD |
| **Aprova** | **DEP-EXE**, com **parecer de DEP-GOV** | FND-04 §2, **C2**; FND-07 §2.4, *C2 · Tipo 2*. **DEP-PRD nao aprova o que propos** (`PI-05`) |
| **Aprova a alteracao de `TPL-spec`** | **DEP-GOV** | FND-09 §8.2, linha `TPL` — *aprova* |
| **Verifica aptidao** | **DEP-QAR** | `CV-07`, `CC-04`, `QG-6` — [FIT-2026-015](../governance/fitness/FIT-2026-015-framework-de-specifications.md) |
| **Ratifica** | **—** | **C2 · Tipo 2** nao exige ratificacao (FND-04 §2.1; FND-07 §2.3) |

> **`RC-02` atendida por construcao, e o residuo remanescente esta dito.** Autoria **DEP-PRD**;
> revisao **DEP-ENG + DEP-QAR**; teste de determinismo **escrito por DEP-PRD e reexecutado por
> DEP-QAR**; avaliacao **DEP-QAR**; aprovacao **DEP-EXE**. **Cinco departamentos, cinco funcoes,
> e DEP-GOV em nenhuma delas exceto forma e registro** — que e o que a Carta dele manda
> (*"registra, nunca emite"*). **Primeira vez no acervo.** Residuo: **DEP-GOV registra o
> catalogo que declara defeito em contadores de DEP-GOV** — `RD-32`, familia `RC-02`, **setima
> ocorrencia, declarada e nao resolvida**.

---

## 1. Contexto

`GO-TO-SPECS` foi liberado pelas **8 de 8** condicoes de §X do sexto ato soberano
([PT-2026-006 §8](../governance/relatorio-transicao-2026-07-29-fechamento-operacional.md)),
com verificacao independente em
[FIT-2026-014](../governance/fitness/FIT-2026-014-regime-ministerial-e-cobertura-de-contexto.md),
e com **uma pre-correcao declarada obrigatoria e nao negociavel: `RD-23`**.

**A `Spec` e o unico tipo documental do acervo que acumula quatro achados em quatro missoes
consecutivas** — `RD-14` *(portao liberado por quem produz)*, `RD-15` *(dois aprovadores)*,
`RD-18` *(duas classes geradoras)* e `RD-23` *(template contra a norma)*. Tres foram fechados
por emenda de fonte; o quarto sobrou. **A causa comum e uma so: a Spec tem tipo, entidade,
definicao, autoridade e template, e nao tem contrato.**

**Estado do mundo antes desta decisao, medido:** `164` artefatos · `46.353` linhas ·
`8cf2143c…b027a7f`; **`0` Specs**, **`0` Produtos**, **`0` Projetos**; `products/` **ausente**
da raiz; `RD-23` **aberto**.

## 2. Problema / Pergunta de decisao

**Onde vive a norma da `Spec`, com que instrumento ela se institui, e o que ela pode
legitimamente exigir sem criar autoridade nem emendar fonte?**

E, como corolario que a medicao impos: **existe hoje algum caminho legal para criar uma `Spec`?**

## 3. Criterios de decisao

Declarados **antes** de examinar as alternativas — `K1` a `K8` de
[RFC-0017 §4](../rfcs/RFC-0017-framework-de-specifications.md), **nao reproduzidos aqui**
(`PJ-01`).

## 4. Alternativas consideradas

**Cinco alternativas e a opcao Z**, com criterios, custo e afetados, em
[RFC-0017 §5](../rfcs/RFC-0017-framework-de-specifications.md) — **`A` `FND-11`** · **`B` secao
em `FND-10`** · **`C` regras no ADR** *(escolhida)* · **`D` pilotos primeiro** · **`E` ampliar
Spec a materia nao-produto** · **`Z` nao fazer nada**. **Este ADR nao as reproduz** (`PJ-01`,
`CM-09`).

**Por que `C`.** `A` e `B` dao **sede melhor** e exigem **emendar fundacional** — `B` colide
frontalmente com a pre-correcao `RD-27` da missao, e `RD-27` mostra que acrescentar linha a
`FND-10` altera `H-N` de objeto promulgado (`IR-05`: *"exige ato novo"*). `D` e **nula por
norma** (§7.3). `E` e a **unica via** do piloto interdepartamental e e **C3**. `Z` congela um
portao aberto.

**Tradeoff aceito (`VD-04`):** as regras `SF-*` vivem em artefato **`M1`** e **nao se emendam** —
corrigi-las exige **ADR sucessor** (`SF-32`). Aceita-se a rigidez em troca de **nao tocar
nenhuma fonte fundacional**. E o mesmo regime de `IR-*`, `FT-*` e `PA-*`.

## 5. Decisao

### 5.1 O que uma Spec e, e o que ela nao e — `SF-01` a `SF-04`

| # | Regra |
|---|---|
| **SF-01** | **Uma `Spec` declara o que deve ser verdadeiro, sob que condicao, e por qual evidencia isso sera aceito.** Nada mais. Fundamento: `FND-03 §3.6` — *"definicao do **que** deve existir e de como se verifica que existe. Nunca define o **como**"*. |
| **SF-02** | **Uma `Spec` nao e decisao, Carta, `Skill`, `Workflow`, `Command`, `Agente`, plano, explicacao nem implementacao.** Decisao e `ADR` ou Nota de Decisao (`FND-07 §3`); existencia formal e Carta (`FND-10 §4.3`); procedimento e `SKL`/`WFL` (`§4.4`); `Command` **nao e artefato** (`FND-10 §4.8`). **Spec que decida arquitetura, escolha tecnologia ou detalhe implementacao e devolvida** (`FND-03 §3.6`, conteudo proibido; `RP-2` de DEP-PRD). |
| **SF-03** | **A `Spec` nao cria autoridade e nao aprova a si propria.** Nenhuma Spec institui papel, portao, classe, verbo de autoridade ou titular; nenhuma Spec e sua propria aprovadora, revisora ou verificadora (`LV-03`, `PI-05`, `RM-06b`, `LN-06`, `ADR-0005`). **A autoridade sobre a Spec e funcao do tipo, e vive em `FND-09 §8.2`** — declarar autoridade dentro da Spec e proibido por `AC-01` e `§2.4` de `FND-10`. |
| **SF-04** | **Uma `Spec` nao vale por sua existencia, e sim por ser consumida.** Spec sem **consumidor nomeado** e sem **necessidade demonstrada** e devolvida por `FND-04 §6.1` — as quatro perguntas da regra de nao-proliferacao valem para ela como para qualquer componente. |

### 5.2 Spec Contract — `SF-05` a `SF-09`

> **Declaracao de projecao (`PJ-02`).**
> **Fonte:** `FND-03 §4` *(nucleo universal de 15 campos)* · `FND-10 §2.2` *(extensao de cinco
> campos + `projecao_de`)* · `FND-10 §2.5` *(`AC-01` a `AC-11`)* · `FND-09 §8.2` linha `SPC` ·
> `FND-04 §6` linha *Spec*.
> **Campos projetados:** apenas **quais blocos a Spec deve conter e onde cada exigencia nasce**.
> **Finalidade:** responder em uma leitura o que hoje exige seis fontes — a causa medida dos
> quatro achados de §1.
> **Metodo de atualizacao:** pela mesma mudanca que altera a fonte (`CV-04`), por **ADR
> sucessor** (`SF-32`). **Em divergencia prevalece a fonte** (`PJ-03`).

| # | Regra |
|---|---|
| **SF-05** | **O contrato da Spec e o contrato universal do artefato, sem excecao e sem acrescimo de campo novo.** Os **15** campos de `FND-03 §4` e os **cinco** de `FND-10 §2.2` — `resumo`, `perfil_contexto`, `confidencialidade`, `revisor`, `ratificacao` — sao **obrigatorios**, porque toda Spec sera **criada apos a vigencia** de `FND-10` (`AC-08`). **Ausencia = artefato nao conforme = veto de DEP-GOV** (`AC-06`). **Nenhum campo novo e criado por este ADR** (`AC-07`). |
| **SF-06** | **Os campos condicionais da Spec sao os que `FND-03 §4.1` ja preve** — `produto` e `criterios_aceite_count`, do esqueleto de `TPL-spec`. **Nao se declara** consumidor, relacao, autoridade, custo de contexto nem dependencia transitiva: os cinco sao **derivaveis** e proibidos no frontmatter por `AC-01` e `FND-10 §2.4`. |
| **SF-07** | **A Spec declara vinculo a exatamente uma `Capability` ativa e a exatamente um Departamento custodiante da materia.** Fundamento: `FND-04 §6`, pre-condicao universal I (`VC-01`); `FND-08 §8`. Capability inexistente, `proposta` ou `aposentada` **bloqueia a aprovacao**; competencia que nao caiba no catalogo exige **RFC de Capability antes** (`VC-02`). |
| **SF-08** | **A Spec declara `exclusoes` em bloco proprio e obrigatorio.** Escopo negativo ausente e **defeito de spec**, nao omissao de estilo: `FND-04 §6` linha *Spec* o exige como pre-condicao de criacao, `PI-09` proibe ampliacao silenciosa e `P-9`/`RP-3` de DEP-PRD o declaram como risco Alto. **Cada exclusao declara por que fica de fora e sob qual condicao poderia entrar.** |
| **SF-09** | **Os blocos obrigatorios de corpo da Spec sao vinte e um**, e cada um existe porque uma fonte o exige. **Bloco ausente = Spec incompleta**, e Spec incompleta **nao entra em `em-revisao`** (`O3`). |

**Os vinte e um blocos, e a fonte de cada exigencia:**

| # | Bloco | Por que e obrigatorio |
|---|---|---|
| 1 | **Identidade** | `id`, `titulo`, `versao`, `status` — `FND-03 §4` |
| 2 | **Proposito** | Bloco obrigatorio de corpo — `FND-10 §2.2` |
| 3 | **Escopo** | idem |
| 4 | **Responsaveis** | idem |
| 5 | **Autoridade — classe, tipo e aprovador derivados** | `SF-10`; `FND-09 §8.2` linha `SPC`; `FND-04 §2` |
| 6 | **Custodiante** | `SF-07`; `FND-08 §6.1` |
| 7 | **Autores** | `FND-09 §8.2` — *propoe/cria* `DEP-PRD` |
| 8 | **Revisores** | `FND-09 §8.2` — `DEP-ENG` + `DEP-QAR`; `AC-03` |
| 9 | **Aprovadores** | `SF-10`; **derivado, nunca fixado** |
| 10 | **Capability** | `SF-07`; `VC-01` |
| 11 | **Departamento** | `SF-07`; `FND-02 §3` |
| 12 | **Consumidores** | `SF-04`; **no corpo, nao no frontmatter** (`AC-01`) |
| 13 | **Requisitos** | `SF-11` a `SF-16` — o nucleo do artefato |
| 14 | **Exclusoes** | `SF-08`; `PI-09` |
| 15 | **Interfaces** | `FND-09 §6.1`, relacoes `R-04`/`R-05` |
| 16 | **Dependencias** | `FND-10 §7`; `LN-03` proibe relacao com `superado` |
| 17 | **Riscos** | `FND-04 §6.2`; `LM-01` — risco sem sinal e devolvido |
| 18 | **Evidencias** | `SF-15`; `LV-12`, `CE-04` |
| 19 | **Verificacao** | `SF-14`; `QG-1`, `QG-3` |
| 20 | **Vigencia** | `FND-10 §5.2`, `§5.4`; `LM-02` |
| 21 | **Contexto e evolucao** | `SF-27` a `SF-31`; `CE-01` a `CE-05` |

### 5.3 Autoridade e ciclo — `SF-10`

| # | Regra |
|---|---|
| **SF-10** | **A autoridade sobre uma Spec e derivada, nunca declarada no artefato.** Ela e funcao de **quatro** variaveis, nesta ordem: **(a) a classe do efeito** (`AL-01`, com **`C1` como piso** por `FND-04 §6`); **(b) o tipo de reversibilidade** (`FND-04 §2.2`); **(c) a materia** (`FND-01 §7.3`); **(d) o Departamento custodiante** (`FND-02 §3`). **Toda Spec que fixe aprovador em texto e nao conforme** — foi exatamente o defeito de `RD-23`. Na duvida sobre a classe prevalece **a mais restritiva** (`FND-01 §7.1.6`), e a classificacao e **validada por DEP-GOV** (`FND-04 §2`). |

**Mapeamento `C0`–`C3` × `Tipo 1/2` para as dez etapas do ciclo — projecao declarada:**

> **Declaracao de projecao (`PJ-02`).**
> **Fonte:** `FND-04 §2`, `§2.1`, `§2.2`, `§6` · `FND-07 §2.3`, `§2.4`, `§5` · `FND-09 §8.2`
> linha `SPC` e `AU-05` · `FND-10 §5.2`, `§5.4`, `§6.1` · `FND-01 §6.2` · `ADR-0018` ·
> `ADR-0019` · `ADR-0020` `PA-01` a `PA-14`.
> **Campos projetados:** apenas **etapa × titular** e a condicao de eficacia.
> **Finalidade:** a exigencia literal da missao — *"mapear `C0`–`C3` × `Tipo 1/2`"* — que um
> indice de ponteiros nao satisfaz.
> **Metodo de atualizacao:** `CV-04`, por ADR sucessor (`SF-32`). **A fonte prevalece** (`PJ-03`).

| Etapa | **C0 · T2** | **C1 · T2** | **C2 · T2** | **C2 · T1** | **C3 · qualquer** |
|---|---|---|---|---|---|
| **Proposta** | proprietario | **DEP-PRD** | **DEP-PRD** | **DEP-PRD** | **DEP-PRD** |
| **Autoria** | proprietario | **DEP-PRD** | **DEP-PRD** | **DEP-PRD** | **DEP-PRD** |
| **Revisao** | — | **revisor ≠ autor** | **DEP-ENG + DEP-QAR** | **DEP-ENG + DEP-QAR** | **DEP-ENG + DEP-QAR** |
| **Liberacao de `QG-1`** | nao se aplica | **DEP-EXE** | **DEP-EXE** | **DEP-EXE** | **DEP-EXE** |
| **Aprovacao** | proprietario | proprietario **+ revisor** | **DEP-EXE** + parecer **DEP-GOV** | **DEP-EXE** propoe | **SOBERANO**, indelegavel |
| **Ratificacao** | **nao exigida** | **nao exigida** | **nao exigida** | **SOBERANO** | **SOBERANO** |
| **Registro / promulgacao** | `atualizado_em` + CORRECAO | **DEP-GOV** | **DEP-GOV**, e o registro **precede** a execucao (`CV-02`) | **DEP-GOV**, **apos** o ato | **DEP-GOV**, apos ato indelegavel |
| **Vigencia / ativacao** | ja `ativo` | nomeado na criacao | **nomeado**; supletivamente o custodiante (`PA-07`) | **nomeado**, **apos** `ratificacao: ratificada` (`LM-02`) | **nomeado**, com `IR-09` por DEP-QAR |
| **Emenda** | CORRECAO | MENOR | MENOR ou MAIOR conforme o efeito (`AL-01`) | idem **+ ato** | idem **+ ato** |
| **Superacao / retirada** | **DEP-PRD** *(`O6`/`O9`)* | **DEP-PRD** | **DEP-PRD**, com dependentes migrados (`LC-05`) | **DEP-PRD**, com ato | **DEP-PRD**, com ato |

**Cinquenta celulas. Nenhum titular novo:** `DEP-PRD`, `DEP-ENG`, `DEP-QAR`, `DEP-EXE`,
`DEP-GOV` e `SOBERANO` **ja constam** de `FND-04 §2` e `FND-09 §8.2`. **`C0 · T1` e `C1 · T1`
nao figuram** porque `FND-04 §2.2` os resolve por escalonamento: `C0/T1` **nao existe** e
`C1/T1` **vira C2**.

### 5.4 Semantica normativa — `SF-11` a `SF-16`

| # | Regra |
|---|---|
| **SF-11** | **Tres verbos normativos, e apenas tres: `MUST`, `SHOULD`, `MAY`.** `MUST` — condicao de aceite; descumprimento **reprova** a entrega. `SHOULD` — esperado; descumprimento exige **motivo registrado**, e nao reprova por si. `MAY` — permitido; descumprimento **nao tem consequencia**. **Equivalentes oficiais em portugues, exclusivos:** `MUST` = *"deve"*; `SHOULD` = *"deveria"*; `MAY` = *"pode"*. **`MUST NOT` = *"nao deve"*** e requisito negativo (`SF-13`), nao verbo novo. **Qualquer outro verbo — *"precisa"*, *"tem de"*, *"e necessario"*, *"recomenda-se"* — e ambiguo e devolvido.** |
| **SF-12** | **Todo requisito tem seis campos, e nenhum e opcional:** **`ID`** *(`RQ-nn`, unico na Spec e estavel entre versoes)* · **`motivo`** *(por que existe; requisito sem motivo e preferencia)* · **`fonte`** *(citada por identificador — norma, decisao, evidencia ou consumidor)* · **`criterio de aceite`** *(verificavel por terceiro **sem consultar o autor**)* · **`metodo de verificacao`** · **`evidencia esperada`**. **Requisito com menos de seis campos e nao conforme e devolvido.** |
| **SF-13** | **Seis naturezas de enunciado, mutuamente exclusivas, e cada linha declara a sua:** **`FATO`** *(verificavel agora, com fonte)* · **`REQUISITO`** *(o que deve ser verdadeiro — leva `SF-12`)* · **`HIPOTESE`** *(entra **marcada**, com o teste que a confirmaria; invalidada **nao e apagada** — `P-11`/`MM-09`)* · **`DECISAO`** *(nao entra: **remete** a `ADR` ou Nota — `SF-02`)* · **`RECOMENDACAO`** *(nao vincula; `SHOULD` no maximo)* · **`NOTA`** *(nao vincula e nao verifica)*. **Enunciado sem natureza declarada e lido como `NOTA` — logo nao obriga.** |
| **SF-14** | **Cinco metodos de verificacao, e so eles:** **`INSPECAO`** *(leitura por terceiro)* · **`DEMONSTRACAO`** *(execucao observada)* · **`TESTE`** *(procedimento repetivel com resultado registrado)* · **`ANALISE`** *(derivacao de dado medido)* · **`MEDICAO`** *(valor numerico com instrumento e data)*. **Criterio cujo metodo nao caiba em nenhum dos cinco nao e verificavel, logo nao e requisito** (`SF-12`). |
| **SF-15** | **Evidencia esperada e declarada antes, nunca escolhida depois.** Todo requisito diz **que artefato, valor ou observacao** contara como prova, **quem** a produz e **quando**. **Indicador sem valor medido nao prova conformidade** — declara-se `definido, sem valor` (`LM-01`, `CE-04`). **Fabricar evidencia, fonte, citacao, metrica ou resultado e `LV-12`.** |
| **SF-16** | **Adjetivo sem definicao verificavel e proibido em requisito.** *"premium"*, *"robusto"*, *"rapido"*, *"simples"*, *"intuitivo"*, *"escalavel"*, *"seguro"*, *"de qualidade"*, *"moderno"*, *"performatico"* — **dez termos vedados por nome**, e a lista **nao e exaustiva**: o teste e *"existe metodo de `SF-14` que decida isto por terceiro?"*. **Sem metodo, o termo sai ou ganha definicao com numero, instrumento e data.** |

### 5.5 Perfis — `SF-17` a `SF-19`

| # | Regra |
|---|---|
| **SF-17** | **Sao sete perfis de requisito, e eles classificam requisito — nao criam entidade nem tipo documental.** `FUNCIONAL` *(o que faz)* · `INTERFACE` *(por onde se fala com isso)* · `DADOS` *(o que persiste, com que forma e retencao)* · `QUALIDADE` *(atributo nao funcional com numero)* · `SEGURANCA` *(o que nao pode ocorrer — leva requisito negativo por `SF-13`)* · `OPERACAO` *(como se opera, monitora e recupera)* · `AVALIACAO` *(como se julga que ficou bom)*. |
| **SF-18** | **Perfil nao vira entidade, tipo documental, template, diretorio ou Departamento — nunca automaticamente.** Fundamento: `FND-10 §1.3` *(tipo documental nao e entidade)*, `CS-01`, `MT-01`, e `FND-09 §11.1` — criar entidade e **C3 · Tipo 1** com sete testes `TE`. **Uma Spec pode ter requisitos de todos os sete perfis e continua sendo uma Spec.** |
| **SF-19** | **Especializar um perfil em artefato proprio exige tres coisas cumulativas:** **(a)** autoridade **ou** ciclo de vida distinto do da Spec; **(b)** **dois sinais observados** de `FND-10 §9.2` (`SE-02`); **(c)** o teste de especializacao de `FND-04 §6.2` respondido por escrito, com o ganho `PI-14` e a data de reavaliacao. **Faltando uma, nao se especializa** — e a decisao de nao especializar **se registra** (`FND-04 §6.2`). |

### 5.6 Rastreabilidade — `SF-20` a `SF-22`

| # | Regra |
|---|---|
| **SF-20** | **A cadeia de rastreabilidade da Spec tem nove elos e e obrigatoria:** `objetivo → Capability → Departamento → decisao → Spec → requisito → aceite → evidencia → resultado`. **Cada elo e percorrivel a partir do artefato, sem consultar pessoa** (`FND-10 §7.3`, `LN-07`). **Elo ausente torna a Spec nao confiavel ate ser saneada**; elo que aponte a artefato `superado`, `revogado` ou `depreciado` **nao pode ser criado** (`LN-03`). |
| **SF-21** | **Seis relacoes, e as seis sao leitura das dez relacoes de `FND-09 §6.1` — nenhuma e nova.** **Declarada uma vez, na fonte; o espelho e derivado** (`LN-01`). |
| **SF-22** | **`conflita` nao e relacao estrutural: e achado.** Conflito entre Specs **nao entra no grafo** — pela mesma razao que `restringe` nao entra (`FND-10 §7.1`): trata-lo como aresta criaria dependencia sem direcao e violaria `PD-11`. **Conflito detectado abre achado com severidade, dono e gatilho**, e resolve-se pela **hierarquia normativa** (`FND-01 §10`) ou por **decisao da classe do efeito**. **Duas Specs vigentes que se contradigam sao defeito, e a mais recente nao prevalece por ser mais recente.** |

**As seis relacoes, e a relacao oficial de cada uma:**

| Relacao | Relacao oficial de `FND-09 §6.1` | Bilateral? | Ciclo? | O que significa entre Specs |
|---|---|---|---|---|
| **`refina`** | `R-04 depende-de` | Sim | **Nao** | A Spec B detalha requisito da Spec A **sem contradizer** |
| **`restringe`** | **ato de autoridade** — nao e aresta (`FND-10 §7.1`) | — | — | A norma superior limita o que a Spec pode exigir |
| **`implementa`** | `R-04 depende-de` | Sim | **Nao** | O componente satisfaz o requisito da Spec |
| **`verifica`** | `R-06 verifica` | Sim | Sim, **exceto reflexivo** (`LN-06`) | A evidencia decide o aceite do requisito |
| **`conflita`** | **nenhuma — e achado** (`SF-22`) | — | — | Duas exigencias vigentes incompativeis |
| **`substitui`** | `R-08 supera` | Sim — **nos dois frontmatters** (`LN-02`) | **Nao** | A Spec sucessora assume, e os dependentes migram (`LC-05`) |

### 5.7 Qualidade — `SF-23` a `SF-26`

| # | Regra |
|---|---|
| **SF-23** | **`DoR` da Spec — nove itens. Faltando um, a Spec nao entra em `em-revisao`** (`O3`): **(1)** problema definido **antes** da solucao (`P-2`); **(2)** consumidor nomeado e necessidade demonstrada (`SF-04`); **(3)** as **quatro** perguntas de nao-proliferacao respondidas por escrito (`FND-04 §6.1`); **(4)** `Capability` ativa vinculada (`VC-01`); **(5)** classe e tipo **classificados pelo proponente** (`FND-04 §2`); **(6)** exclusoes declaradas (`SF-08`); **(7)** todo requisito com os **seis** campos (`SF-12`); **(8)** revisores designados, **≠ autor** (`AC-03`); **(9)** pre-condicoes de `FND-04 §6` linha *Spec* satisfeitas — inclusive **`Produto existe`**. |
| **SF-24** | **`DoD` da Spec — dez itens. Faltando um, a mudanca nao encerra:** **(1)** `QG-1` liberado por **DEP-EXE**, registrado com responsavel e data (`FND-01 §6.2`); **(2)** revisao independente concluida; **(3)** aprovacao pela classe (`SF-10`); **(4)** ratificacao **se** `C3` ou `Tipo 1` (`LM-02`); **(5)** cadeia de nove elos percorrivel (`SF-20`); **(6)** entrada no **catalogo mestre** com custo **medido** (`RG-02`, `CE-02`); **(7)** cobertura das **quatro** categorias de requisito (`SF-25`); **(8)** suposicoes, limites, **rollback** e **criterio de abandono** declarados (`SF-26`); **(9)** `FIT` emitido se `C2` ou `C3` (`CC-04`, `QG-6`); **(10)** indices `M3` atualizados na **mesma** mudanca (`CV-04`, `IX-02`). |
| **SF-25** | **Quatro categorias de requisito, e a ausencia de qualquer uma se declara com motivo:** **`FUNCIONAL`** · **`NAO FUNCIONAL`** *(com numero, instrumento e data — `CE-04`)* · **`NEGATIVO`** *(o que **nao** deve ocorrer; e o unico modo de especificar seguranca e limite)* · **`DE FALHA`** *(o que acontece quando o caminho feliz nao ocorre)*. **Spec que so tenha requisito funcional esta incompleta**, e a incompletude **e declarada, nunca presumida como ausencia de necessidade**. |
| **SF-26** | **Quatro declaracoes de limite, obrigatorias e distintas:** **`SUPOSICAO`** *(o que se assume verdadeiro sem verificar, e o que muda se for falso)* · **`LIMITE`** *(o que esta fora da capacidade declarada, com o numero)* · **`ROLLBACK`** *(como se desfaz, com responsavel e custo — `RB-01`)* · **`ABANDONO`** *(como se sabe que esta Spec deixou de ser necessaria — quarta pergunta de `FND-04 §6.1`)*. **Nenhuma das quatro admite *"nao aplicavel"* sem motivo escrito.** |

### 5.8 Mudanca — `SF-27` a `SF-30`

| # | Regra |
|---|---|
| **SF-27** | **`Spec` e `M2` — versionavel, com texto anterior preservado no historico** (`FND-10 §6.2`). **A versao segue o efeito, nao o tamanho do texto** (`CC-02`, `AL-01`): **MAIOR** quando um `MUST` e criado, removido ou tem o criterio de aceite alterado; **MENOR** quando um `SHOULD`/`MAY` muda ou um requisito e acrescentado sem alterar `MUST` existente; **CORRECAO** quando nada normativo muda. **Alteracao de conteudo sem incremento de versao e nao conformidade** (`AC-11`). |
| **SF-28** | **Alteracao silenciosa e nula, e heranca implicita e proibida.** Nenhum requisito muda de sentido sem incremento de versao e linha de historico (`LC-01`, `GV-01`). **Nenhuma Spec herda requisito de outra por proximidade, por refinar ou por estar no mesmo produto:** o que vincula e a **relacao declarada** (`SF-21`) e o **requisito citado por `ID`**. |
| **SF-29** | **Toda emenda declara cinco coisas:** **impacto** · **compatibilidade** *(retro-compativel ou nao)* · **dependentes** *(enumerados, nunca *"todos"*)* · **migracao** *(quem migra cada dependente, e quando)* · **depreciacao ou substituicao** *(`O6`/`O7`, com sucessor nomeado)*. **Emenda incompativel sem plano de migracao e mudanca incompleta** (`CV-04`, `CC-03`), **nao norma nova**. |
| **SF-30** | **`Spec` que esteve em `ativo` nunca volta a `rascunho`** (`RB-02`). Corrige-se **superando** (`O6`), com **sucessor `ativo`** e **todos** os dependentes migrados (`LC-05`); anula-se sem substituto por **retirada** (`O9`), declarando **o que passa a valer no lugar** (`SU-04`). **`substitui`/`substituido_por` sao declarados nos dois lados** (`LN-02`). |

### 5.9 Economia de contexto — `SF-31`

| # | Regra |
|---|---|
| **SF-31** | **Cinco exigencias de economia, e as cinco sao medidas, nunca estimadas.** **(1) `resumo` operacional** — uma linha, ate 200 caracteres, em voz ativa, dizendo **o que a Spec faz** e nao o que ela e (`AC-02`). **(2) Gatilho de ativacao** — a condicao que torna a Spec necessaria, no catalogo mestre (`FND-10 §8.3`). **(3) Pacote minimo** — o que precisa vir junto, **e so isso**. **(4) Secoes sob demanda** — a Spec e escrita em **blocos rotulados e independentes**, e o perfil padrao e **`sob-demanda`** (`FND-10 §10.3`). **(5) Custo medido** — **linhas do arquivo**, por `wc -l`, com data (`CE-02`, `CE-04`). **Carregar a Spec inteira para consultar um requisito e falha de curadoria** (`CE-01`, `PC-01`): **o requisito e enderecavel pelo seu `ID` (`RQ-nn`), e citar `<SPC-id> RQ-nn` obriga a carregar o bloco daquele requisito, nao o documento.** Spec que ultrapasse **o dobro da mediana do seu tipo** e candidata a especializacao por `CE-05` — **e `SF-19` decide se especializa**. |

### 5.10 Template, registro e superacao deste ADR — `SF-32`

| # | Regra |
|---|---|
| **SF-32** | **Um template canonico, um registro mestre, e nenhum registro novo.** **Template:** [`TPL-spec`](../foundation/templates/TPL-spec.md), unico, mantido por `DEP-PRD` *(dono do tipo)* e aprovado por `DEP-GOV` (`FND-09 §8.2` linha `TPL`); especializar template exige `FND-10 §10.2`. **Registro mestre:** o [catalogo mestre](../governance/artifact-registry.md) — que `RG-04` ja declara *"a visao transversal do acervo"* — e o **contador oficial** da sequencia `SPC` e o **indice do diretorio** onde as Specs vivem (`FND-03 §2.3`, `RG-04`). **Nenhum registro de Specs e criado por este ADR:** criar um terceiro seria proliferacao (`FND-04 §6.1`) e arquivo satelite por artefato, proibido por `RG-05`. **Criar Spec e incrementar o contador sao a mesma mudanca** (`CV-04`, `IX-02`) — a regra que `RD-32` mostrou nao estar sendo exercida. **Este ADR e superavel por ADR que o referencie** (`CC-06`, `SU-01`); ele **nao se emenda** (`AC-10`, `CC-01`). |

### 5.11 A correcao de `RD-23` — `TPL-spec` **1.1.0**

**Cinco defeitos medidos, cinco corrigidos.** O diff literal esta em §5.12; o texto vigente
esta no proprio template.

| # | Defeito medido | Correcao aplicada | Norma |
|---|---|---|---|
| **T1** | Esqueleto fixava `aprovador: DEP-PRD` | **`<derivado da classe — FND-04 §2; ver ADR-0021 SF-10>`** | `FND-09 §8.2` linha `SPC`; `SF-10` |
| **T2** | Esqueleto **sem** campo `ratificacao` | **`ratificacao: <nao-exigida \| pendente \| ratificada>`**, com a regra `C3`/`Tipo 1` na instrucao | `FND-09 §8.2`; `LM-02`; `SF-10` |
| **T3** | Esqueleto **sem** `resumo`, `perfil_contexto`, `confidencialidade`, `revisor` | **os quatro acrescentados**, com valores e dominio declarados | `FND-10 §2.2`; `AC-06`; `SF-05` |
| **T4** | §11 declarava *"Liberado por `<DEP-PRD, data>`"* | **`<DEP-EXE, data>`**, com a nota de que **liberar portao ≠ aprovar artefato** | `FND-01 §6.2` pos-`ADR-0018` |
| **T5** | §Responsaveis **sem revisor** e sem aprovador derivado | **revisores `DEP-ENG` + `DEP-QAR`**; aprovador **derivado** | `FND-09 §8.2`; `AC-03` |

**O que a correcao NAO fez, e por que:**

| Nao feito | Fundamento |
|---|---|
| Alterar `aprovador: SOBERANO` **do cabecalho do proprio template** | **`19 de 19` templates declaram o mesmo valor** — medido. Corrigir um cria divergencia entre iguais; corrigir os dezenove e outra materia. Achado **`RD-34`**, com leitura alternativa declarada |
| Remover o vinculo a `products/<slug>/specs/` | Consta de **tres fontes vigentes** (§7.3). Alterar e **C3** — achado **`RD-33`** |
| Acrescentar campo novo ao contrato | `AC-07`; `SF-05` |
| Criar segundo template ou registro | `SF-32`; `FND-04 §6.1`; `RG-05` |

### 5.12 Diff literal de `TPL-spec` — reversivel

```
--- TPL-spec 1.0.0                          +++ TPL-spec 1.1.0
frontmatter do template
  versao: 1.0.0                          ->  versao: 1.1.0
  atualizado_em: 2026-07-28              ->  atualizado_em: 2026-07-29
  decisoes_relacionadas: [ADR-0001]      ->  decisoes_relacionadas: [ADR-0001, ADR-0018, ADR-0019, ADR-0021]
  (ausente)                              ->  resumo / perfil_contexto / confidencialidade / revisor / ratificacao
esqueleto da Spec
  autor: DEP-PRD                         ->  autor: DEP-PRD            (inalterado — FND-09 §8.2 propoe/cria)
  aprovador: DEP-PRD                     ->  aprovador: <derivado da classe — FND-04 §2>
  (ausente)                              ->  revisor: DEP-QAR
  (ausente)                              ->  ratificacao: <nao-exigida | pendente | ratificada>
  (ausente)                              ->  resumo / perfil_contexto / confidencialidade
  (ausente)                              ->  classe_mudanca / tipo_decisao / capabilities
§11 Portao QG-1
  Liberado por | <DEP-PRD, data>         ->  Liberado por | <DEP-EXE, data>
```

**Reversao:** restaurar `TPL-spec` **1.0.0** pelo diff acima, que e **literal e reversivel**, e
superar este ADR (`SF-32`).

## 6. Justificativa

**Porque a Spec era o unico tipo com autoridade resolvida e contrato ausente.** `ADR-0018`,
`ADR-0019` e `ADR-0020` responderam **quem** decide, libera, promulga e ativa. **Nenhum
respondeu o que a Spec deve conter para ser aceita** — e e disso que os quatro achados de §1 sao
sintoma. Um framework que resolve autoridade sem resolver contrato produz exatamente o que se
mediu: template contradizendo norma vigente por **duas** missoes.

**Porque a sede correta e inexecutavel e a sede executavel tem tres precedentes.** `FND-11`
seria melhor; exige `C3` e emenda a `FND-01 §10`. Secao em `FND-10` seria melhor ainda; **a
propria missao a veda** por `RD-27`, e `IR-05` explica por que: alteraria `H-N` de objeto
promulgado. Regras dentro do ADR e o que `ADR-0012`, `ADR-0015` e `ADR-0020` fizeram — a ultima
com **doze casos de determinismo provados** —, e **nao toca `H-N` de nada**.

**Porque a impossibilidade dos pilotos precisava ser escrita, e nao contornada.** Havia duas
saidas faceis e ambas seriam violacao: **escrever as Specs em outro diretorio** — `MT-01`,
`FND-03 §7.1`, artefato fora do lugar canonico —, ou **criar `products/` e uma Carta de Produto**
— `FND-04 §6`, `C2 · Tipo 1` do Soberano, e restricao expressa da missao. **A terceira saida e
declarar o bloqueio com as fontes citadas e as duas vias de desbloqueio com custo.** `PI-10`
exige que o limite esteja escrito; `LV-05` proibe reportar como feito o que nao foi.

**Porque `SF-31` e a unica parte do framework que muda o custo de quem consome.** O consumidor
da norma da Spec ia a **seis** secoes de **cinco** fontes. Passa a ir a **um** ADR
`sob-demanda` e **um** template — e, para consultar uma exigencia especifica, a **um bloco de
requisito enderecado por `RQ-nn`**, sem carregar o documento. Isto e `PI-14` medido, nao
prometido.

## 7. Impacto

### 7.1 Quadro geral

| Dimensao | Impacto |
|---|---|
| **Departamentos afetados** | **`DEP-PRD`** *(autor e proprietario da norma da propria materia)* · **`DEP-ENG`** e **`DEP-QAR`** *(revisores — nada novo)* · **`DEP-EXE`** *(aprova; libera `QG-1` desde `ADR-0018` — nada novo)* · **`DEP-GOV`** *(forma, registro, catalogo — nada novo)*. **Nenhum ganha responsabilidade que nao tivesse** |
| **Componentes** | **0 criados · 0 alterados · 0 removidos** |
| **Entidades · tipos documentais · portoes · papeis · classes · verbos de autoridade** | **0 criados · 0 alterados** |
| **Fontes de `foundation/` emendadas** | **0** — verificado por `cmp` contra a copia datada |
| **Artefatos `M2` alterados** | **1** — `TPL-spec` **1.0.0 → 1.1.0** |
| **Titulares ampliados** | **0** — as 50 celulas de §5.3 nomeiam apenas nomes de `FND-04 §2` e `FND-09 §8.2` |
| **Camadas de memoria** | **APR** — [MEM-APR-0006](../memory/aprendizado/MEM-APR-0006-exercer-o-contador-revela-o-defeito.md) · **OPR** — [PT-2026-007](../governance/relatorio-transicao-2026-07-29-specifications.md) |
| **Documentos `M3` em cascata `CV-04`** | [catalogo mestre](../governance/artifact-registry.md) · [`README` raiz](../README.md) · [`decisions/README`](README.md) · [`rfcs/README`](../rfcs/README.md) · [`governance/README`](../governance/README.md) · [`governance/fitness/README`](../governance/fitness/README.md) · [`memory/README`](../memory/README.md) · [`memory/aprendizado/README`](../memory/aprendizado/README.md) |
| **Custo de contexto criado** | **1 `ADR` `sob-demanda` + 1 `RFC` `sob-demanda` + 1 `FIT` `missao` + 1 `MEM-APR` `sob-demanda` + 1 relatorio `missao`**, medidos em §8 do relatorio. **Nenhuma dependencia externa; nenhuma ferramenta nova** (`CE-02`) |
| **Ganho `PI-14`** | **Organizacao** — a Spec ganha contrato; **4 achados em 4 missoes** e o sinal observado. **Reducao de contexto** — 6 secoes em 5 fontes → 1 ADR + 1 template, com requisito enderecavel por `ID`. **Reavaliacao: 2027-01-28** |

### 7.2 O que este ADR **nao** faz

| Nao faz | Fundamento |
|---|---|
| **Nao** cria `Skill`, `Tool`, `Command`, `Workflow`, `Agente`, `Produto`, `Projeto`, codigo, banco, infraestrutura, ontologia ou migracao | Restricao expressa da missao; `FND-04 §6` tem rito proprio para cada |
| **Nao** cria `FND`, entidade, tipo documental, portao, papel, classe ou verbo de autoridade | `SF-18`; `FND-09 §11.1`; `FND-01 §6.2`; `FND-09 §8.1` |
| **Nao** emenda `FND-01`, `FND-02` nem `FND-10` | Pre-correcao `RD-27` da missao; `IR-05` |
| **Nao** edita baseline historica | `BL-02`; pre-correcao `RD-28` |
| **Nao** altera a Carta de `DEP-PRD`, `DEP-EXE` ou qualquer outra | `FND-09 §8.2` linha `DEP` — aprova e ratifica **SOBERANO**. Achado **`RD-31`** |
| **Nao** cria as duas Specs piloto | **§7.3** — impossivel por norma |
| **Nao** presume aprovacao, ratificacao ou existencia de Produto | `LM-02` a `LM-06`; `LV-05` |
| **Nao** importa formato da evidencia externa | **§8**; `FR-03`, `ADR-0007` |
| **Nao** fecha `RD-24`, `RD-27`, `RD-28`, `RD-30`, `RD-10` a `RD-13`, `RD-18`, `RD-21`, nem a familia `RC-02` | Cada um tem dono e gatilho proprios |

### 7.3 **Nenhuma `Spec` e criavel hoje — e a razao esta em tres fontes vigentes**

| Fonte | Texto literal | Efeito |
|---|---|---|
| **`FND-04 §6`**, linha *Spec* | pre-condicoes: ***"Produto existe**; problema definido; criterios de aceite verificaveis; escopo negativo explicito"*, e *"**Todas** precisam ser verdadeiras para a criacao ser aprovada"* | **`O1` nao pode ocorrer** (`FND-10 §5.2`) |
| **`FND-03 §3.6`** | *"Vive em `products/<slug>/specs/<SPC-id>.md`"* | **Nao ha caminho canonico** fora de um produto; `FND-03 §7.1` — *"um artefato existe em exatamente um lugar"* |
| **`FND-10 §4.4`** | Local: **`products/<slug>/specs/`** | Terceira fonte, mesmo vinculo |

**Medido nesta missao, antes de qualquer escrita:** **`0`** artefatos de tipo `spec`; **`0`**
artefatos de tipo `PRO`; **`products/` ausente** das **8** entradas da raiz. **`KP-3` da Carta
de `DEP-PRD`** declara, na fonte, **`0` produtos — *"proibido nesta fase, por determinacao"*** —
e **`KP-4`**, **`0` Specs emitidas**.

**E criar `Produto` nao esta ao alcance de nenhum Departamento:** `FND-04 §6`, linha *Produto* —
*"Decisao do Soberano"*, **C2 · Tipo 1**; `FND-09 §8.2`, linha `PRO` — aprova e ratifica
**SOBERANO**; `FND-01 §7.3` — *"Portfolio: criar/encerrar produto → Soberano"*. `DEP-PRD §4`
declara que **nao lhe compete**, e `§8` escala em **`E4`, bloqueando execucao**.

**As duas saidas, disjuntas, ambas do SOBERANO:**

| Saida | Instrumento | Habilita | Custo declarado |
|---|---|---|---|
| **`S1`** | Ato soberano que **crie o primeiro Produto** *(C2 · Tipo 1)* | A Spec **de baixo risco**, de produto — que a norma ja preve **integralmente** | 1 Carta de Produto + 1 ADR + ratificacao |
| **`S2`** | **RFC C3 → ADR C3 → ato**, ampliando `Spec` a materia **nao-produto** | A Spec **interdepartamental** — que a norma **nao preve** | 1 RFC + 1 ADR + diff de **3** fontes + pacote + ato |

**`S1` nao habilita o piloto interdepartamental e `S2` nao cria produto.** A missao pediu **um
de cada**, e **cada um depende de uma saida diferente**. **Este ADR nao escolhe entre elas: a
escolha e do Soberano** (`FND-01 §7.3`).

> **O framework nao depende dos pilotos para ser testavel — e foi testado.** §9 registra **doze
> casos de determinismo**, na forma de `ADR-0020 §5.3`, com **os que sao determinados e nao
> observados declarados como tais** (`PI-10`).

## 8. Evidencias

### 8.1 Evidencia interna — medida

| # | Evidencia | Valor | Confianca |
|---|---|---|---|
| **E1** | Baseline vigente reproduz antes das edicoes | **164 · 46.353 · `8cf2143c…b027a7f`** | **Alta — medida** |
| **E2** | `Spec` vinculada a `Produto` em **3** fontes vigentes | `FND-03 §3.6` · `FND-04 §6` · `FND-10 §4.4` | **Alta — literal** |
| **E3** | `products/` ausente; **0** `SPC`; **0** `PRO` | **8** diretorios na raiz | **Alta — medida** |
| **E4** | Defeitos de contrato em `TPL-spec` | **5** — §5.11 | **Alta — medida** |
| **E5** | Precedente de **forma** para regras dentro de ADR `C2 · Tipo 2` | `ADR-0012` `IR-01`–`IR-12` · `ADR-0015` `FT-10`–`FT-14` · `ADR-0020` `PA-01`–`PA-14` | **Alta — medida** |
| **E6** | Achados sobre `Spec` por ausencia de contrato | **4 em 4 missoes** — `RD-14`, `RD-15`, `RD-18`, `RD-23` | **Alta — medida** |
| **E7** | Afirmacoes falsas na Carta de `DEP-PRD`; `QG-1` em `DEP-EXE` | **8** · **0 ocorrencias** | **Alta — medida** |
| **E8** | Contadores oficiais defasados | **4 tabelas · 8 valores** | **Alta — medida** |
| **A1** | **Evidencia ausente, declarada:** **nenhuma `Spec` real existe.** Todo `SF-*` e **determinado, nao observado** | `PI-10`, `LV-12` | — |
| **A2** | **Evidencia ausente, declarada:** **nenhum conflito real entre Specs** ocorreu. `SF-22` e determinado, nao observado | `PI-10` | — |
| **A3** | **Evidencia ausente, declarada:** **nenhuma superacao real de Spec** ocorreu. `SF-30` e determinado, nao observado | `PI-10` | — |

### 8.2 Evidencia externa — avaliada, **nao adotada**

**Origem:** `_SAIDA-COMPANY-OS/09_PACOTE-DE-INTEGRACAO/`. **`external-evidence` · autoridade
nenhuma · provisoria · nao normativa · adocao nao-decidida** — o proprio pacote o declara em
cada arquivo, e a decisao dele e **`RESEARCH-READY`**, com **`ADOPT = 0`**. **Nenhum conteudo
foi copiado; nenhum formato foi importado** (`FR-03`, `ADR-0007`).

| Item | O que informa | **O que foi aproveitado, e como** | **O que foi recusado, e por que** |
|---|---|---|---|
| **`AC-03-REP-010`** *(CANDIDATO-FORTE, LV4, MIT)* | Portao obrigatorio **spec → codigo**, com spec *"assinada pelo humano"* antes de delegar | **A tese, nao a forma:** a ordem *spec antes de construir* **converge** com o que o acervo ja tem em `QG-1` (`FND-01 §6.2`) e com `SF-24`. **A convergencia e usada como sinal de que o portao existente esta no lugar certo — nao como fundamento** | **A assinatura humana por Spec.** No acervo, quem libera `QG-1` e **`DEP-EXE`** e quem ratifica e o **SOBERANO**, e so quando `C3` ou `Tipo 1` (`ADR-0019`). Exigir ato humano em **toda** Spec **contrariaria `PA-13`** e poria o Soberano como operador recorrente. **TDD, YAGNI e DRY sao materia de `DEP-ENG`** e nao entram em Spec (`SF-02`) |
| **`AC-05-REP-001`** *(PILOTO, LV4, MIT)* | Fluxo por fases com portao entre elas: `/spec → /plan → /build → /test → /review → /ship` | **Nada estrutural.** O acervo **ja tem** sete portoes em `FND-01 §6.2`, e acrescentar portao e **`C3`**. A leitura **confirmou** que `QG-1` → `QG-2` → `QG-3` cobre o mesmo intervalo | **A cadeia de comandos por fase.** `Command` **nao e artefato** no acervo — `FND-10 §4.8` o recusa expressamente, e o gatilho de reabertura e *"superficie com ciclo de vida independente do procedimento"*, **nao observado**. Importar o fluxo criaria **seis portoes paralelos aos sete existentes** |
| **`AC-02-PRT-003`** *(REFERENCIA)* | Proposito, escopo e **criterio de sucesso antes de framework** | **Convergencia registrada** com `SF-23` `DoR` item (1) — problema antes da solucao (`P-2`) | Nada a importar: e o que `FND-04 §6.1` ja exige |

> **O limite desta evidencia, declarado pelo proprio pacote e verificado nesta leitura:**
> **zero medicao de eficacia foi lida** (`L-04` do resumo executivo) — *"toda economia de token,
> taxa de deteccao e ganho de qualidade deste pacote e alegacao, nao fato"*. Logo **nenhum `SF-*`
> tem a evidencia externa como fundamento**, e nenhum numero dela entra neste ADR (`CE-04`,
> `LV-12`). **O uso foi de contraste**, e o resultado do contraste esta na coluna *"o que foi
> recusado"*: **duas praticas fortes foram recusadas com norma citada**, o que e o resultado
> util de avaliar evidencia externa sem adota-la.

## 9. O framework testado — **doze casos**

| # | Caso | Resposta pelas regras | Deterministico? |
|---|---|---|---|
| **T-01** | **Criacao** de Spec de produto, `C1 · T2` | `SF-23` `DoR` **9 de 9**, e o item **(9) falha hoje**: `FND-04 §6` exige *"Produto existe"*. **`O1` bloqueada** — §7.3 | ✅ **e o bloqueio e a resposta** |
| **T-02** | **Criacao** de Spec interdepartamental | **Categoria inexistente na norma:** as 3 fontes de §7.3 vinculam Spec a produto. Exige `S2`, **C3** | ✅ |
| **T-03** | Spec fixa `aprovador` em texto | **Nao conforme por `SF-10`**; devolvida. **Foi o defeito de `RD-23`** | ✅ |
| **T-04** | Requisito diz *"a interface deve ser rapida"* | **Devolvido por `SF-16`** *(termo vedado por nome)* e por `SF-12` *(sem criterio nem metodo de `SF-14`)* | ✅ |
| **T-05** | Requisito sem `motivo` e sem `fonte` | **Devolvido por `SF-12`** — seis campos, nenhum opcional | ✅ |
| **T-06** | Spec declara *"decidimos usar tal tecnologia"* | **`SF-02` + `SF-13`:** decisao **nao entra** — remete a `ADR`. Devolvida por `FND-03 §3.6` *(conteudo proibido)* | ✅ |
| **T-07** | **Conflito** entre duas Specs vigentes | **`SF-22`:** nao e aresta, e **achado** com severidade, dono e gatilho; resolve pela hierarquia (`FND-01 §10`) ou pela classe do efeito. **A mais recente nao prevalece por ser recente** | ✅ **determinado, nao observado** *(`A2`)* |
| **T-08** | **Mudanca** que altera criterio de aceite de um `MUST` | **`SF-27`: MAIOR**; `SF-29`: cinco declaracoes; `SF-28`: sem incremento e **nulo**. Se o efeito for `C2`, aprova `DEP-EXE`; se `Tipo 1`, **ratifica o SOBERANO** | ✅ |
| **T-09** | **Evidencia** — indicador declarado sem valor | **`SF-15` + `LM-01`:** declara-se `definido, sem valor`; **nao prova conformidade**. Afirmar desempenho sem medida e **`LV-12`** | ✅ |
| **T-10** | **Superacao** de Spec `ativo` com dependentes | **`SF-30`:** `O6` com **sucessor `ativo`** e **todos** os dependentes migrados (`LC-05`); `substitui`/`substituido_por` **nos dois lados** (`LN-02`); **nao volta a `rascunho`** (`RB-02`) | ✅ **determinado, nao observado** *(`A3`)* |
| **T-11** | **Consumo por futura `Skill`** — *"quem aprova esta Spec `C2`?"* | **`SF-10` + §5.3:** `DEP-EXE` com parecer `DEP-GOV`; `QG-1` liberado por `DEP-EXE`; ratificacao **nao exigida**. **Resposta por celula, sem interpretacao informal** | ✅ |
| **T-12** | **Consumo por futura `Skill`** — *"quem libera `QG-1`?"*, lendo **Cartas** | ⚠️ **`DEP-PRD`** — **resposta errada**. `FND-01 §6.2` diz `DEP-EXE`; a Carta de `DEP-PRD` ainda reivindica o portao em **8** afirmacoes e `DEP-EXE` **nao o declara em nenhuma**. **Achado `RD-31`** | ⚠️ **deterministico e DIVERGENTE — e por isso e achado** |

**Doze casos. Onze deterministicos e coerentes; um deterministico e divergente**, e a
divergencia **nao foi contornada: virou `RD-31`, com dono, gatilho, custo e instrumento.**
**Tres casos sao determinados e nao observados** — `T-07`, `T-10` e, por `A1`, todos os demais
que pressupoem Spec real.

## 10. Riscos e mitigacao

| # | Risco | Prob. | Impacto | Mitigacao |
|---|---|---|---|---|
| **RA-1** | **`SF-*` virar segunda fonte de verdade sobre autoridade** | Media | **Alto** | §5.2 e §5.3 sao **projecao declarada** (`PJ-02`) com as quatro informacoes; `PJ-03` da precedencia a fonte; **nenhum titular fora de `FND-04 §2` e `FND-09 §8.2`** |
| **RA-2** | **Framework sem instancia envelhecer** | **Observada — `A1`** | Medio | Declarado: **todo `SF-*` e determinado, nao observado**. Gatilho de revisao: **a primeira Spec real**. `SF-32` permite superacao barata |
| **RA-3** | **`RD-31` produzir aprovacao ou liberacao invalida** — alguem lê a Carta e `DEP-PRD` libera `QG-1` | **Media** | **Alto** | Registrado com dono **`DEP-EXE`**, revisor `DEP-GOV`, ratificador **SOBERANO**, gatilho *"antes da primeira Spec"*. **`T-12` documenta a divergencia por escrito**, que e a unica mitigacao possivel sem ato. **`LV-03` continua valendo**: liberacao por quem produziu e **nula**, independentemente do que a Carta diga |
| **RA-4** | **A classe `C2` ser contestada** | Media | Medio | Teste item a item em §11; **`0` arquivos de `foundation/` alterados**, medido por `cmp`. Duvida **declarada**; via `C3` indicada |
| **RA-5** | **`SF-16` virar censura de estilo** | Media | Baixo | A lista de dez termos **nao e exaustiva e nao e o teste**: o teste e *"ha metodo de `SF-14` que decida isto por terceiro?"*. **O termo pode ficar, com definicao** |
| **RA-6** | **`SF-09` — vinte e um blocos tornarem a Spec caro de escrever**, contra `PI-14` | **Media** | Medio | `SF-31` obriga **blocos independentes e perfil `sob-demanda`**: escreve-se tudo, **carrega-se o requisito**. **Se a mediana medida do tipo mostrar Spec acima do dobro, `CE-05` dispara e `SF-19` decide** — o gatilho ja existe, e o valor **sera medido na primeira Spec**, nao estimado agora |
| **RA-7** | **Os pilotos ausentes serem lidos como missao incompleta por omissao** | Media | Medio | §7.3 declara a impossibilidade com **3 fontes citadas** e **2 saidas com custo**; `PI-10` cumprido |
| **RA-8** | **Concentracao em `DEP-GOV`** — familia `RC-02` | **Observada — 7a ocorrencia** | Medio | **Materialmente mitigada nesta decisao:** autoria `DEP-PRD`, revisao `DEP-ENG`+`DEP-QAR`, avaliacao `DEP-QAR`, aprovacao `DEP-EXE`. **Residuo:** `DEP-GOV` registra o catalogo que declara defeito em contador de `DEP-GOV` (`RD-32`). **Declarado, nao resolvido** — so desaparece com agentes (`IC-3`) |

## 11. Classificacao

| Campo | Valor |
|---|---|
| **Classe de mudanca** | **C2** — institui **padrao** de um tipo documental ja existente e altera **um** artefato `M2` *(o template)*. **Teste de `C3`, item a item:** principio imutavel — **nao toca**; linha vermelha — **nao toca**; hierarquia normativa de `FND-01 §10` — **nao toca**; direitos de decisao de `FND-01 §7.3` — **nao toca**; a propria Fundacao — **`0` arquivos alterados, medido por `cmp`** |
| **Tipo de reversibilidade** | **2** — reversao barata e conhecida (§12) |
| **Decisor** | **DEP-EXE**, com parecer de **DEP-GOV** (`FND-04 §2`; `FND-07 §2.4`) |
| **Aprovador da alteracao de `TPL-spec`** | **DEP-GOV** (`FND-09 §8.2`, linha `TPL`) |
| **Ratificador** | **—** *(C2 · Tipo 2 nao exige — `FND-04 §2.1`)* |
| Data da decisao · vigencia | **2026-07-29** · **2026-07-29** |

> **Sobre a classificacao, com a duvida declarada.** `GV-03` manda tratar como **Tipo 1** o que
> nao se sabe classificar, e `FND-01 §7.1.6` manda prevalecer a classificacao mais restritiva.
> **Dois argumentos empurram para `C3`:** instituir o framework de um dominio **parece**
> constitucional, e `SF-10` toca a materia *"quem aprova Spec"*. **Dois argumentos o afastam, e
> sao verificaveis:** `SF-10` **nao decide** quem aprova — **remete** a `FND-04 §2`, exatamente
> como `ADR-0019` **ja ratificou**; e **nenhum arquivo de `foundation/` e alterado**, o que
> distingue este ADR de `ADR-0018` e `ADR-0019`, que **eram** `C3` **porque emendavam fonte**.
> **Se o SOBERANO entender de outro modo, o caminho e `RFC → ADR C3 → ratificacao`, e
> [RFC-0017](../rfcs/RFC-0017-framework-de-specifications.md) serve de peca instrutoria sem
> reescrita. A escolha da classe permanece contestavel, e o registro diz isso.**

## 12. Plano de reversao

**Tipo 2 — reversao barata e conhecida.**

| Passo | Acao | Responsavel |
|---|---|---|
| 1 | ADR sucessor que **supere** este, declarando o que passa a valer (`SU-04`, `O6`, `SF-32`) | qualquer DEP; aprova **DEP-EXE** |
| 2 | `status: superado` + `superado_por`; `substitui`/`substituido_por` **nos dois lados** (`LN-02`) | **DEP-GOV** |
| 3 | Restaurar `TPL-spec` **1.0.0** pelo diff **literal e reversivel** de §5.12, com incremento de versao devido (`AC-11`) | **DEP-PRD**; aprova **DEP-GOV** |
| 4 | Verificar que **nenhuma Spec** perdeu fundamento — **`0` Specs existem**, logo **`0` migram** (`LC-05`) | **DEP-QAR** |
| 5 | Reprocessar os **8** indices `M3` a partir da fonte (`RG-03`) | **DEP-GOV** |

**Custo medido da reversao: 1 ADR novo + 1 `TPL` restaurado + 8 indices `M3`. Zero artefatos
normativos alterados, porque zero foram alterados para instituir isto. Zero Specs migram,
porque zero existem** — e essa e a razao pela qual **reverter agora e mais barato do que sera
depois da primeira Spec**, o que e exatamente o gatilho de §13.

## 13. Revisao

| Campo | Conteudo |
|---|---|
| **Gatilho de revisao** | **A primeira `Spec` real** — o unico evento que transforma `SF-*` de determinado em observado *(`A1`)*; **ou** o primeiro **conflito real** entre Specs *(`T-07`, `A2`)*; **ou** a primeira **superacao real** *(`T-10`, `A3`)*; **ou** o ato que resolva `S1` ou `S2` |
| **O que se mede** | Quantas Specs foram **devolvidas** por `SF-12`, `SF-16` ou `SF-23`, e por qual regra *(uma devolucao por regra ja prova que a regra pega algo)*; **linhas medidas** da primeira Spec contra o dobro da mediana do tipo (`CE-05`, `RA-6`); quantas vezes o requisito foi consultado **por `RQ-nn`** sem carregar o documento (`SF-31`); se `T-12` continuou dando resposta errada |
| **Data de reavaliacao** | **2027-01-28** |
| **Aprendizado registrado** | [MEM-APR-0006](../memory/aprendizado/MEM-APR-0006-exercer-o-contador-revela-o-defeito.md) — **exercer o instrumento revela o defeito que ler o instrumento nao revela**. `RD-32` foi encontrado **ao pedir o numero desta decisao**; `RD-31`, **ao simular o consumo**; `RD-33`, **ao verificar a pre-condicao de criacao** |

## 14. Rastreabilidade

| Campo | Conteudo |
|---|---|
| **Origem** | [RFC-0017](../rfcs/RFC-0017-framework-de-specifications.md) |
| **Pre-condicao consumida** | `GO-TO-SPECS`, **8 de 8** — [PT-2026-006 §8](../governance/relatorio-transicao-2026-07-29-fechamento-operacional.md); `ADR-0020` vigente; prova **55/55**; catalogo reconciliado; **`BL-2026-07-29-08`** reproduzida antes das edicoes |
| **Achado que fecha** | **`RD-23`** — §5.11, **cinco** defeitos medidos e corrigidos, onde o achado declarava **dois** |
| **Achados que abre** | **`RD-31`** *(Alta — 8 afirmacoes falsas na Carta de `DEP-PRD`; `QG-1` sem titular declarado em Carta alguma)* · **`RD-32`** *(Media — 4 contadores oficiais de sequencia, 8 valores; risco de colisao de identificador)* · **`RD-33`** *(Alta — `Spec` vinculada a `Produto` impede os pilotos)* · **`RD-34`** *(Baixa — 19 de 19 `TPL` declaram `aprovador: SOBERANO`)* · **`RD-35`** *(Media — 2 agregados de indice divergentes da fonte, encontrados na cascata `CV-04` desta decisao)* · **`RD-36`** *(Media — o razao de ressalvas nao fecha; parcialmente tratado, com o limite declarado)* |
| **Complementa** | [ADR-0018](ADR-0018-liberacao-do-portao-qg-1.md) *(`QG-1`)* · [ADR-0019](ADR-0019-aprovador-e-ratificador-de-spec.md) *(aprovador e ratificador)* · [ADR-0020](ADR-0020-regime-ministerial-de-promulgacao-e-ativacao.md) *(`PA-*`)* · [ADR-0012](ADR-0012-integridade-do-ato-de-ratificacao.md) *(`IR-*`)* · [ADR-0009](ADR-0009-o-que-conta-como-emenda-de-artefato.md) *(`AC-08` a `AC-11`)* |
| **Decisoes superadas** | **Nenhuma** |
| **Verificacao de aptidao** | [FIT-2026-015](../governance/fitness/FIT-2026-015-framework-de-specifications.md) |
| **Relatorio de aplicacao** | [PT-2026-007](../governance/relatorio-transicao-2026-07-29-specifications.md) |
| **Fontes projetadas** | **§5.2** e **§5.3**, com declaracao `PJ-02` completa nas duas |
| **Evidencia externa** | §8.2 — `external-evidence`, **avaliada e nao adotada**, **0 formatos importados** |

## Checklist de validade (FND-07 §4.1)

| # | Regra | Cumprida |
|---|---|---|
| VD-01 | ≥ 2 alternativas reais + *"nao fazer nada"* | ✅ **cinco + Z** — [RFC-0017 §5](../rfcs/RFC-0017-framework-de-specifications.md) |
| VD-02 | Criterios declarados **antes** da escolha | ✅ RFC-0017 §4 precede §5 |
| VD-03 | Nenhuma alternativa de palha | ✅ **`A` e `B` sao melhores em sede** e recusadas por **inexecutabilidade medida**, nao por conveniencia; **`E` virou achado com dono** |
| VD-04 | Tradeoff aceito explicito | ✅ fim de §4 — rigidez de `M1` |
| VD-05 | Evidencia ausente declarada | ✅ **`A1`, `A2`, `A3`** — e `A1` alcanca **todo** o ADR |
| VD-06 | Plano de reversao obrigatorio em Tipo 1 | ✅ apresentado **ainda sendo Tipo 2** (§12), com custo medido |
| VD-07 | Impacto em cascata mapeado | ✅ §7.1 — **8** indices `M3` |
| VD-08 | Data e responsavel presentes | ✅ §11 |
| VD-09 | Gatilho de revisao definido | ✅ §13 |

---

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-PRD | Decisao **C2 · Tipo 2** que institui o **Framework de Specifications** como **`SF-01` a `SF-32`, dentro do proprio ADR**, na forma de `ADR-0012`, `ADR-0015` e `ADR-0020`, com **`0` arquivos de `foundation/` alterados** — medido por `cmp` — e **`0` entidades, tipos, portoes, papeis, classes ou verbos de autoridade criados**. Cobre **Spec Contract** *(21 blocos, cada um com a fonte da exigencia)*, **semantica normativa** *(`MUST`/`SHOULD`/`MAY` com equivalentes exclusivos; requisito de **seis** campos; **seis** naturezas de enunciado; **cinco** metodos de verificacao; **dez** adjetivos vedados por nome)*, **sete perfis** *(que nao viram entidade nem tipo)*, o mapeamento **`C0`–`C3` × `Tipo 1/2`** em **50 celulas** como projecao declarada, a **cadeia de nove elos** e **seis relacoes** *(com `conflita` declarada **achado**, nao aresta)*, **`DoR` de 9** e **`DoD` de 10**, o regime de mudanca *(versao pelo efeito; alteracao silenciosa nula; heranca implicita proibida)* e a **economia de contexto** *(requisito enderecavel por `RQ-nn`, sem carregar o documento)*. **Fecha `RD-23` com cinco defeitos corrigidos onde o achado declarava dois** — `TPL-spec` **1.1.0**, com diff literal e reversivel. **Testado em doze casos: onze deterministicos e coerentes, e um deterministico e DIVERGENTE** — `T-12`, *"quem libera `QG-1`"* lido nas Cartas devolve `DEP-PRD` — **e a divergencia nao foi contornada: virou `RD-31`**. **Declara, com tres fontes vigentes citadas por identificador, que nenhuma `Spec` e criavel hoje**: `FND-04 §6` exige *"Produto existe"*, `FND-03 §3.6` e `FND-10 §4.4` a alojam em `products/<slug>/specs/`, e **medem-se `0` Specs, `0` Produtos e `products/` ausente**; criar Produto e **C2 · Tipo 1 do SOBERANO**. **As duas Specs piloto pedidas pela missao nao foram criadas — e a razao esta escrita, com as duas saidas `S1` e `S2`, disjuntas, ambas do Soberano.** Evidencia externa da A4 **avaliada e nao adotada**, com **duas praticas fortes recusadas com norma citada** *(assinatura humana por Spec; cadeia de comandos por fase)* e **`0` formatos importados**. **`RC-02` atendida por construcao — cinco departamentos, cinco funcoes, `DEP-GOV` em nenhuma exceto forma e registro; primeira vez no acervo.** Abre **`RD-31`**, **`RD-32`**, **`RD-33`** e **`RD-34`**. Classe **contestavel e declarada como tal**. |
