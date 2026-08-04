---
id: FND-11
titulo: Framework de Specifications do LucaX Enterprise OS
tipo: fundacao
versao: 1.1.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-07-29
atualizado_em: 2026-08-02
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0005, ADR-0008, ADR-0009, ADR-0012, ADR-0015, ADR-0018, ADR-0019, ADR-0020, ADR-0021, ADR-0022, ADR-0032]
substitui: []
substituido_por: null
resumo: Da sede fundacional a norma da Spec — contrato, semantica, perfis, autoridade derivada, DoR, DoD, ciclo, relacoes, mudanca e economia de contexto — em SF-01 a SF-32.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: ratificada
---

# Framework de Specifications

> ## O estado deste documento e o do seu frontmatter, e nada alem dele
>
> **A fonte corrente do estado e o campo `ratificacao`** (FND-10 §5.4). Enquanto ele disser
> `pendente`, este documento **nao produz efeito**, **nao integra a Fundacao** e **nao ocupa
> nivel algum da hierarquia normativa de FND-01 §10** — e a norma da `Spec` continua vivendo
> integralmente em [ADR-0021](../decisions/ADR-0021-framework-de-specifications.md), que
> permanece **vigente e intacto**. **Nenhuma frase deste texto afirma vigencia** — a licao de
> **RD-08**, aplicada.

## Proposito

Dar **sede fundacional** a norma da `Spec`. Este Framework responde, em um lugar so, o que a
`Spec` deve conter para ser aceita, com que semantica ela obriga, quem decide sobre ela, como
ela nasce, muda, e sai de vigor — **sem redefinir autoridade** e **sem alterar o vinculo entre
`Spec` e `Produto`**.

Ele **nao institui** as regras `SF-01` a `SF-32`: elas foram instituidas por
[ADR-0021](../decisions/ADR-0021-framework-de-specifications.md), `C2 · Tipo 2`, em
2026-07-29. Este documento **as recebe**, na forma documental que
[FND-10 §4.1](10-artifact-framework.md) reserva ao **Framework**, e o faz **declarando, regra
por regra, a origem, a transformacao e a equivalencia** (§2).

## Escopo

| Item | Definicao |
|---|---|
| **Inclui** | `SF-01` a `SF-32`; o **Spec Contract** *(21 blocos)*; a semantica normativa de requisito; os **sete perfis**; o mapeamento `C0`–`C3` × `Tipo 1/2` como **projecao declarada**; a cadeia de **nove elos** e as **seis relacoes**; **DoR** e **DoD**; o regime de mudanca da `Spec`; a economia de contexto; e o **regime de mudanca deste proprio Framework** (`SF-32`) |
| **Nao** inclui | O **vinculo `Spec` × `Produto`** *(§13 — inalterado, tres fontes vigentes)* · a **sequencia por Produto** e os **locais canonicos** *(FND-03 §3.6, FND-03 §7, FND-10 §4.4 — inalterados)* · qualquer `Spec`, `Produto`, `Projeto`, `Skill`, `Tool`, `Command`, `Workflow`, `Agente`, codigo ou infraestrutura · **entidade, tipo documental, portao, papel, departamento, classe ou verbo de autoridade novos** · o **merito** de `ADR-0018`, `ADR-0019` e `ADR-0020` · a matriz de autoridade de `FND-09 §8.2`, que **permanece a fonte** |
| **Subordinado a** | [FND-01](01-constituicao.md) *(nivel 1)* · e, no nivel 2, a [FND-03](03-taxonomia.md), [FND-04](04-governanca.md), [FND-07](07-framework-decisoes.md), [FND-08](08-capability-framework.md), [FND-09](09-meta-model.md) *(precedencia parcial sobre pares — FND-01 §10)* e [FND-10](10-artifact-framework.md) |
| Origem | [RFC-0018](../rfcs/RFC-0018-sede-canonica-do-framework-de-specifications.md) → [ADR-0022](../decisions/ADR-0022-sede-canonica-do-framework-de-specifications.md) |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| **Propoe / autor** | **DEP-GOV** | [FND-09 §8.2](09-meta-model.md), linha `FND` — *propoe/cria*. **Nao e escolha:** a matriz atribui a proposicao de `FND` exclusivamente a DEP-GOV |
| **Materia** | **DEP-PRD** | Dono do tipo `SPC` (FND-09 §8.2, linha `SPC`) e **autor do merito** em `ADR-0021`. **Consulta obrigatoria** em toda emenda deste Framework |
| **Revisor independente** | **DEP-QAR** | FND-09 §8.2, linha `FND` — *revisa*; `RM-06b` |
| **Aprova e ratifica** | **SOBERANO** | **C3.** Indelegavel (FND-04 §2; FND-09 §8.2, linha `FND`) |

> **Residuo declarado (`PI-10`), e ele e uma regressao medida.** `ADR-0021` foi o primeiro
> instrumento normativo do acervo cujo autor **nao** e DEP-GOV — a resposta material a
> **`RC-02`** registrada em [FIT-2026-015](../governance/fitness/FIT-2026-015-framework-de-specifications.md).
> **Promover a norma a `FND` devolve a autoria a DEP-GOV, e nao ha alternativa:** `FND-09 §8.2`
> nomeia **um unico** proponente para `FND`. **A concentracao volta por determinacao da matriz,
> nao por conveniencia** — e e a mesma causa de **`IC-3`**. Mitigacao real e nao suficiente:
> **DEP-PRD e consulta obrigatoria**, **DEP-QAR revisa** e **o merito das 32 regras nao e de
> DEP-GOV** — ele e recebido, nao escrito, e §2 prova isso linha a linha. Achado **`RD-39`**,
> familia `RC-02`, **oitava ocorrencia, declarada e nao resolvida**.

---

## 1. Contexto — por que a `Spec` precisou de contrato

**A `Spec` e o unico tipo documental do acervo que acumulou quatro achados em quatro missoes
consecutivas** — `RD-14` *(portao liberado por quem produz)*, `RD-15` *(dois aprovadores)*,
`RD-18` *(duas classes geradoras)* e `RD-23` *(template contra a norma)*. Tres foram fechados
por emenda de fonte; o quarto foi fechado por `ADR-0021`. **A causa comum era uma so: a `Spec`
tinha tipo, entidade, definicao, autoridade e template, e nao tinha contrato.**

`ADR-0021` deu o contrato. **O que ele nao pode dar foi a sede:** as regras `SF-*` nasceram
dentro de um artefato **`M1`**, que por `AC-10` e `CC-01` **nunca se emenda** — corrigir uma
virgula exigia **ADR sucessor**. O proprio `ADR-0021` declarou o tradeoff em §4 (`VD-04`) e
registrou, em §6, que **`FND-11` seria a sede melhor** e estava, naquela missao, fora de
alcance por exigir `C3`.

**Este documento e a sede melhor, produzida pelo rito que ela exige.**

## 2. Origem, transformacao e equivalencia — as 32 regras, uma por uma

> **Regra de leitura desta secao.** *"Origem"* e o local exato em `ADR-0021` de onde a regra
> vem. *"Transformacao"* e o que foi feito ao texto. *"Equivalencia"* e o veredito sobre o
> **merito**. **Uma unica regra tem alteracao de merito, e ela esta nomeada.**

> **Alcance temporal desta secao (`1.1.0`).** A tabela de §2.2 e a medicao de diff de §2.1
> descrevem **a recepcao das 32 regras em `1.0.0`**, e continuam exatas quanto a ela. **A
> versao `1.1.0` emendou 1 celula do corpo** — §5, linha *Aprovacao*, coluna `C1 · T2` —
> por [ADR-0032](../decisions/ADR-0032-separacao-de-proponente-e-aprovador-na-spec-c1.md),
> `C3`, para sanar `RD-91`. **Consequencia declarada, nao silenciosa:** a partir de `1.1.0`
> a matriz de §5 **difere em 1 celula** da matriz de `ADR-0021 §5.3`, que e artefato `M1` e
> **nunca se emenda** (`AC-10`, `CC-01`). **Prevalece esta**, por ser a sede canonica
> ([ADR-0022](../decisions/ADR-0022-sede-canonica-do-framework-de-specifications.md) §5.4);
> a copia de `ADR-0021 §5.3` fica **historica e superada quanto a essa celula**, e o
> registro disso e o achado `RD-98`.

### 2.1 Classes de transformacao — tres, e apenas tres

| Classe | Definicao | Quantas regras |
|---|---|---|
| **`T-IDENTICA`** | O texto normativo e reproduzido **byte a byte**. Zero alteracao | **30** |
| **`T-REFERENCIAL`** | Muda **apenas** como a regra se refere a propria sede *(`"este ADR"` → `"este Framework"`)* ou o **caminho relativo** de um link. O merito e identico | **1** *(`SF-05`)* |
| **`T-MERITO-DECLARADO`** | Ha alteracao de merito, e ela e **declarada, nomeada e justificada** | **1** *(`SF-32`)* |

**Medicao do diff, por ferramenta:** o bloco `§5.1`–`§5.10` de `ADR-0021` *(157 linhas)* contra
o corpo `§3`–`§12` deste Framework *(157 linhas)* produz **14 blocos de diff**: **10** de
cabecalho de secao *(renumeracao `### 5.N` → `## N`)*, **2** de metodo de atualizacao das
declaracoes `PJ-02`, **1** em `SF-05` e **1** em `SF-32`. **Zero blocos de diff nas outras 30
regras.**

### 2.2 A tabela regra por regra

| # | Origem em `ADR-0021` | Transformacao | Equivalencia |
|---|---|---|---|
| **SF-01** | §5.1 | `T-IDENTICA` | **Integral** |
| **SF-02** | §5.1 | `T-IDENTICA` | **Integral** |
| **SF-03** | §5.1 | `T-IDENTICA` | **Integral** |
| **SF-04** | §5.1 | `T-IDENTICA` | **Integral** |
| **SF-05** | §5.2 | **`T-REFERENCIAL`** — *"Nenhum campo novo e criado por **este ADR**"* → *"por **este Framework**"* | **Integral.** O sujeito da negativa muda de nome; a negativa **e a mesma**, e continua verificavel: `0` campos novos |
| **SF-06** | §5.2 | `T-IDENTICA` | **Integral** |
| **SF-07** | §5.2 | `T-IDENTICA` | **Integral** |
| **SF-08** | §5.2 | `T-IDENTICA` | **Integral** |
| **SF-09** | §5.2 | `T-IDENTICA` — inclusive a tabela dos **21 blocos** e a fonte de cada exigencia | **Integral** |
| **SF-10** | §5.3 | `T-IDENTICA` **na recepcao de `1.0.0`** — inclusive a matriz de **50 celulas** e a declaracao `PJ-02` que a governa. **`1.1.0` emendou 1 celula da matriz** *(linha Aprovacao × coluna `C1 · T2`)*, por `ADR-0032` | **Integral na recepcao.** A divergencia posterior e **declarada** em §2 e no historico, nunca silenciosa |
| **SF-11** | §5.4 | `T-IDENTICA` | **Integral** |
| **SF-12** | §5.4 | `T-IDENTICA` | **Integral** |
| **SF-13** | §5.4 | `T-IDENTICA` | **Integral** |
| **SF-14** | §5.4 | `T-IDENTICA` | **Integral** |
| **SF-15** | §5.4 | `T-IDENTICA` | **Integral** |
| **SF-16** | §5.4 | `T-IDENTICA` | **Integral** |
| **SF-17** | §5.5 | `T-IDENTICA` | **Integral** |
| **SF-18** | §5.5 | `T-IDENTICA` | **Integral** |
| **SF-19** | §5.5 | `T-IDENTICA` | **Integral** |
| **SF-20** | §5.6 | `T-IDENTICA` | **Integral** |
| **SF-21** | §5.6 | `T-IDENTICA` — inclusive a tabela das **seis relacoes** | **Integral** |
| **SF-22** | §5.6 | `T-IDENTICA` | **Integral** |
| **SF-23** | §5.7 | `T-IDENTICA` — o `DoR` de **nove** itens, inclusive o item **(9)**, que exige *"Produto existe"* | **Integral.** §13 registra que o item (9) **continua falhando** |
| **SF-24** | §5.7 | `T-IDENTICA` — o `DoD` de **dez** itens | **Integral** |
| **SF-25** | §5.7 | `T-IDENTICA` | **Integral** |
| **SF-26** | §5.7 | `T-IDENTICA` | **Integral** |
| **SF-27** | §5.8 | `T-IDENTICA` | **Integral** |
| **SF-28** | §5.8 | `T-IDENTICA` | **Integral** |
| **SF-29** | §5.8 | `T-IDENTICA` | **Integral** |
| **SF-30** | §5.8 | `T-IDENTICA` | **Integral** |
| **SF-31** | §5.9 | `T-IDENTICA` | **Integral** |
| **SF-32** | §5.10 | **`T-MERITO-DECLARADO`** — tres alteracoes: **(a)** *"por este ADR"* → *"por este Framework"* *(referencial)*; **(b)** caminho relativo de `TPL-spec` corrigido para a nova sede *(referencial)*; **(c)** **a clausula final de imutabilidade `M1` — *"Este ADR e superavel por ADR que o referencie; ele nao se emenda"* — e substituida pelo regime `M2`** | **Parcial, e a parte que muda esta nomeada.** Template, registro mestre, proibicao de registro novo e a regra *"criar Spec e incrementar o contador sao a mesma mudanca"* sao **integrais**. **O regime de mutabilidade nao e equivalente, e nao pretende ser** — e o objeto desta promocao |

### 2.3 A unica alteracao de merito, isolada

| Campo | Antes — `ADR-0021 SF-32` | Depois — `FND-11 SF-32` |
|---|---|---|
| **Classe de mutabilidade** | **`M1`** — imutavel apos eficacia (`FND-10 §6.2`) | **`M2`** — versionavel, texto anterior preservado |
| **Como se corrige um defeito** | **ADR sucessor** que o referencie (`CC-06`, `SU-01`) | **Emenda por versao**, pela classe do efeito (`AL-01`, `CC-02`) |
| **Quem aprova a correcao** | Conforme a classe do ADR sucessor | **SOBERANO**, sempre (`FND-09 §8.2` linha `FND`) |
| **Custo de corrigir uma virgula** | **1 ADR novo** | **1 emenda `CORRECAO`** — e **ainda com ato**, porque `FND` nao se emenda sem ratificacao (`LM-02`) |
| **O que NAO muda** | — | O **conteudo** das 32 regras; **quem decide sobre `Spec`**; o **vinculo com `Produto`**; os **locais canonicos** |

> **A promocao troca rigidez por rito, e nao por facilidade.** Sob `M1`, corrigir `SF-16`
> custava um ADR e **nenhum ato do Soberano** *(o ADR era `C2 · Tipo 2`)*. Sob `M2`, custa uma
> emenda e **um ato do Soberano** — porque `FND` **nao vigora sem ratificacao**. **A sede melhor
> e a sede mais protegida, e tambem a mais caro de mudar. O tradeoff e este, e e o inverso do
> que "promover para facilitar" sugeriria.**

### 2.4 O que a promocao NAO faz

| # | Nao faz | Verificacao |
|---|---|---|
| **N1** | **Nao renumera nenhuma regra.** `SF-01` a `SF-32` conservam identificador | **32 de 32** identificadores identicos |
| **N2** | **Nao altera o conteudo de 30 das 32 regras** | `0` blocos de diff nelas — §2.1 |
| **N3** | **Nao cria titular, portao, papel, classe, verbo de autoridade, entidade ou tipo documental** | `SF-18`; `FND-09 §11.1`; `FND-01 §6.2` — **7 portoes antes, 7 depois** |
| **N4** | **Nao altera a matriz de autoridade de `FND-09 §8.2`** | `0` celulas tocadas. `SF-10` **remete**, nao decide |
| **N5** | **Nao altera o vinculo `Spec` × `Produto`**, a sequencia por Produto nem os locais canonicos | §13; `FND-03 §3.6`, `FND-04 §6`, `FND-10 §4.4` — `0` bytes |
| **N6** | **Nao cria `Spec`, `Produto` nem `Projeto`** | **`0` Specs · `0` Produtos** permanecem — §13 |
| **N7** | **Nao edita `ADR-0021`**, que permanece **`ativo`** e e a **fonte historica** do merito | `M1`, `CC-01`, `LV-04` |
| **N8** | **Nao amplia a `Spec` a materia nao-produto** | A saida `S2` de `ADR-0021 §7.3` **nao e exercida aqui** |
| **N9** | **Nao cria regra de precedencia nova na hierarquia normativa** | `FND-01 §10` ja resolve conflito no nivel 2: *conteudo do tipo* → documento especializado; *autoridade* → documento de origem |


## 3. O que uma `Spec` e, e o que ela nao e — `SF-01` a `SF-04`

| # | Regra |
|---|---|
| **SF-01** | **Uma `Spec` declara o que deve ser verdadeiro, sob que condicao, e por qual evidencia isso sera aceito.** Nada mais. Fundamento: `FND-03 §3.6` — *"definicao do **que** deve existir e de como se verifica que existe. Nunca define o **como**"*. |
| **SF-02** | **Uma `Spec` nao e decisao, Carta, `Skill`, `Workflow`, `Command`, `Agente`, plano, explicacao nem implementacao.** Decisao e `ADR` ou Nota de Decisao (`FND-07 §3`); existencia formal e Carta (`FND-10 §4.3`); procedimento e `SKL`/`WFL` (`§4.4`); `Command` **nao e artefato** (`FND-10 §4.8`). **Spec que decida arquitetura, escolha tecnologia ou detalhe implementacao e devolvida** (`FND-03 §3.6`, conteudo proibido; `RP-2` de DEP-PRD). |
| **SF-03** | **A `Spec` nao cria autoridade e nao aprova a si propria.** Nenhuma Spec institui papel, portao, classe, verbo de autoridade ou titular; nenhuma Spec e sua propria aprovadora, revisora ou verificadora (`LV-03`, `PI-05`, `RM-06b`, `LN-06`, `ADR-0005`). **A autoridade sobre a Spec e funcao do tipo, e vive em `FND-09 §8.2`** — declarar autoridade dentro da Spec e proibido por `AC-01` e `§2.4` de `FND-10`. |
| **SF-04** | **Uma `Spec` nao vale por sua existencia, e sim por ser consumida.** Spec sem **consumidor nomeado** e sem **necessidade demonstrada** e devolvida por `FND-04 §6.1` — as quatro perguntas da regra de nao-proliferacao valem para ela como para qualquer componente. |

## 4. Spec Contract — `SF-05` a `SF-09`

> **Declaracao de projecao (`PJ-02`).**
> **Fonte:** `FND-03 §4` *(nucleo universal de 15 campos)* · `FND-10 §2.2` *(extensao de cinco
> campos + `projecao_de`)* · `FND-10 §2.5` *(`AC-01` a `AC-11`)* · `FND-09 §8.2` linha `SPC` ·
> `FND-04 §6` linha *Spec*.
> **Campos projetados:** apenas **quais blocos a Spec deve conter e onde cada exigencia nasce**.
> **Finalidade:** responder em uma leitura o que hoje exige seis fontes — a causa medida dos
> quatro achados de §1.
> **Metodo de atualizacao:** pela mesma mudanca que altera a fonte (`CV-04`), por **emenda
> deste Framework** (`SF-32`). **Em divergencia prevalece a fonte** (`PJ-03`).

| # | Regra |
|---|---|
| **SF-05** | **O contrato da Spec e o contrato universal do artefato, sem excecao e sem acrescimo de campo novo.** Os **15** campos de `FND-03 §4` e os **cinco** de `FND-10 §2.2` — `resumo`, `perfil_contexto`, `confidencialidade`, `revisor`, `ratificacao` — sao **obrigatorios**, porque toda Spec sera **criada apos a vigencia** de `FND-10` (`AC-08`). **Ausencia = artefato nao conforme = veto de DEP-GOV** (`AC-06`). **Nenhum campo novo e criado por este Framework** (`AC-07`). |
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

## 5. Autoridade e ciclo — `SF-10`

| # | Regra |
|---|---|
| **SF-10** | **A autoridade sobre uma Spec e derivada, nunca declarada no artefato.** Ela e funcao de **quatro** variaveis, nesta ordem: **(a) a classe do efeito** (`AL-01`, com **`C1` como piso** por `FND-04 §6`); **(b) o tipo de reversibilidade** (`FND-04 §2.2`); **(c) a materia** (`FND-01 §7.3`); **(d) o Departamento custodiante** (`FND-02 §3`). **Toda Spec que fixe aprovador em texto e nao conforme** — foi exatamente o defeito de `RD-23`. Na duvida sobre a classe prevalece **a mais restritiva** (`FND-01 §7.1.6`), e a classificacao e **validada por DEP-GOV** (`FND-04 §2`). |

**Mapeamento `C0`–`C3` × `Tipo 1/2` para as dez etapas do ciclo — projecao declarada:**

> **Declaracao de projecao (`PJ-02`).**
> **Fonte:** `FND-04 §2`, `§2.1`, `§2.2`, **`§3.1`**, `§6` · `FND-07 §2.3`, `§2.4`, `§5` · `FND-09 §8.2`
> linha `SPC` e `AU-05` · `FND-10 §5.2`, `§5.4`, `§6.1` · `FND-01 §6.2` · `ADR-0018` ·
> `ADR-0019` · `ADR-0020` `PA-01` a `PA-14`.
> **Campos projetados:** apenas **etapa × titular** e a condicao de eficacia.
> **Finalidade:** a exigencia literal da missao — *"mapear `C0`–`C3` × `Tipo 1/2`"* — que um
> indice de ponteiros nao satisfaz.
> **Metodo de atualizacao:** `CV-04`, por **emenda deste Framework** (`SF-32`). **A fonte prevalece** (`PJ-03`).

| Etapa | **C0 · T2** | **C1 · T2** | **C2 · T2** | **C2 · T1** | **C3 · qualquer** |
|---|---|---|---|---|---|
| **Proposta** | proprietario | **DEP-PRD** | **DEP-PRD** | **DEP-PRD** | **DEP-PRD** |
| **Autoria** | proprietario | **DEP-PRD** | **DEP-PRD** | **DEP-PRD** | **DEP-PRD** |
| **Revisao** | — | **revisor ≠ autor** | **DEP-ENG + DEP-QAR** | **DEP-ENG + DEP-QAR** | **DEP-ENG + DEP-QAR** |
| **Liberacao de `QG-1`** | nao se aplica | **DEP-EXE** | **DEP-EXE** | **DEP-EXE** | **DEP-EXE** |
| **Aprovacao** | proprietario | **DEP-EXE** + revisor | **DEP-EXE** + parecer **DEP-GOV** | **DEP-EXE** propoe | **SOBERANO**, indelegavel |
| **Ratificacao** | **nao exigida** | **nao exigida** | **nao exigida** | **SOBERANO** | **SOBERANO** |
| **Registro / promulgacao** | `atualizado_em` + CORRECAO | **DEP-GOV** | **DEP-GOV**, e o registro **precede** a execucao (`CV-02`) | **DEP-GOV**, **apos** o ato | **DEP-GOV**, apos ato indelegavel |
| **Vigencia / ativacao** | ja `ativo` | nomeado na criacao | **nomeado**; supletivamente o custodiante (`PA-07`) | **nomeado**, **apos** `ratificacao: ratificada` (`LM-02`) | **nomeado**, com `IR-09` por DEP-QAR |
| **Emenda** | CORRECAO | MENOR | MENOR ou MAIOR conforme o efeito (`AL-01`) | idem **+ ato** | idem **+ ato** |
| **Superacao / retirada** | **DEP-PRD** *(`O6`/`O9`)* | **DEP-PRD** | **DEP-PRD**, com dependentes migrados (`LC-05`) | **DEP-PRD**, com ato | **DEP-PRD**, com ato |

**Cinquenta celulas. Nenhum titular novo:** `DEP-PRD`, `DEP-ENG`, `DEP-QAR`, `DEP-EXE`,
`DEP-GOV` e `SOBERANO` **ja constam** de `FND-04 §2` e `FND-09 §8.2`. **`C0 · T1` e `C1 · T1`
nao figuram** porque `FND-04 §2.2` os resolve por escalonamento: `C0/T1` **nao existe** e
`C1/T1` **vira C2**.

## 6. Semantica normativa — `SF-11` a `SF-16`

| # | Regra |
|---|---|
| **SF-11** | **Tres verbos normativos, e apenas tres: `MUST`, `SHOULD`, `MAY`.** `MUST` — condicao de aceite; descumprimento **reprova** a entrega. `SHOULD` — esperado; descumprimento exige **motivo registrado**, e nao reprova por si. `MAY` — permitido; descumprimento **nao tem consequencia**. **Equivalentes oficiais em portugues, exclusivos:** `MUST` = *"deve"*; `SHOULD` = *"deveria"*; `MAY` = *"pode"*. **`MUST NOT` = *"nao deve"*** e requisito negativo (`SF-13`), nao verbo novo. **Qualquer outro verbo — *"precisa"*, *"tem de"*, *"e necessario"*, *"recomenda-se"* — e ambiguo e devolvido.** |
| **SF-12** | **Todo requisito tem seis campos, e nenhum e opcional:** **`ID`** *(`RQ-nn`, unico na Spec e estavel entre versoes)* · **`motivo`** *(por que existe; requisito sem motivo e preferencia)* · **`fonte`** *(citada por identificador — norma, decisao, evidencia ou consumidor)* · **`criterio de aceite`** *(verificavel por terceiro **sem consultar o autor**)* · **`metodo de verificacao`** · **`evidencia esperada`**. **Requisito com menos de seis campos e nao conforme e devolvido.** |
| **SF-13** | **Seis naturezas de enunciado, mutuamente exclusivas, e cada linha declara a sua:** **`FATO`** *(verificavel agora, com fonte)* · **`REQUISITO`** *(o que deve ser verdadeiro — leva `SF-12`)* · **`HIPOTESE`** *(entra **marcada**, com o teste que a confirmaria; invalidada **nao e apagada** — `P-11`/`MM-09`)* · **`DECISAO`** *(nao entra: **remete** a `ADR` ou Nota — `SF-02`)* · **`RECOMENDACAO`** *(nao vincula; `SHOULD` no maximo)* · **`NOTA`** *(nao vincula e nao verifica)*. **Enunciado sem natureza declarada e lido como `NOTA` — logo nao obriga.** |
| **SF-14** | **Cinco metodos de verificacao, e so eles:** **`INSPECAO`** *(leitura por terceiro)* · **`DEMONSTRACAO`** *(execucao observada)* · **`TESTE`** *(procedimento repetivel com resultado registrado)* · **`ANALISE`** *(derivacao de dado medido)* · **`MEDICAO`** *(valor numerico com instrumento e data)*. **Criterio cujo metodo nao caiba em nenhum dos cinco nao e verificavel, logo nao e requisito** (`SF-12`). |
| **SF-15** | **Evidencia esperada e declarada antes, nunca escolhida depois.** Todo requisito diz **que artefato, valor ou observacao** contara como prova, **quem** a produz e **quando**. **Indicador sem valor medido nao prova conformidade** — declara-se `definido, sem valor` (`LM-01`, `CE-04`). **Fabricar evidencia, fonte, citacao, metrica ou resultado e `LV-12`.** |
| **SF-16** | **Adjetivo sem definicao verificavel e proibido em requisito.** *"premium"*, *"robusto"*, *"rapido"*, *"simples"*, *"intuitivo"*, *"escalavel"*, *"seguro"*, *"de qualidade"*, *"moderno"*, *"performatico"* — **dez termos vedados por nome**, e a lista **nao e exaustiva**: o teste e *"existe metodo de `SF-14` que decida isto por terceiro?"*. **Sem metodo, o termo sai ou ganha definicao com numero, instrumento e data.** |

## 7. Perfis — `SF-17` a `SF-19`

| # | Regra |
|---|---|
| **SF-17** | **Sao sete perfis de requisito, e eles classificam requisito — nao criam entidade nem tipo documental.** `FUNCIONAL` *(o que faz)* · `INTERFACE` *(por onde se fala com isso)* · `DADOS` *(o que persiste, com que forma e retencao)* · `QUALIDADE` *(atributo nao funcional com numero)* · `SEGURANCA` *(o que nao pode ocorrer — leva requisito negativo por `SF-13`)* · `OPERACAO` *(como se opera, monitora e recupera)* · `AVALIACAO` *(como se julga que ficou bom)*. |
| **SF-18** | **Perfil nao vira entidade, tipo documental, template, diretorio ou Departamento — nunca automaticamente.** Fundamento: `FND-10 §1.3` *(tipo documental nao e entidade)*, `CS-01`, `MT-01`, e `FND-09 §11.1` — criar entidade e **C3 · Tipo 1** com sete testes `TE`. **Uma Spec pode ter requisitos de todos os sete perfis e continua sendo uma Spec.** |
| **SF-19** | **Especializar um perfil em artefato proprio exige tres coisas cumulativas:** **(a)** autoridade **ou** ciclo de vida distinto do da Spec; **(b)** **dois sinais observados** de `FND-10 §9.2` (`SE-02`); **(c)** o teste de especializacao de `FND-04 §6.2` respondido por escrito, com o ganho `PI-14` e a data de reavaliacao. **Faltando uma, nao se especializa** — e a decisao de nao especializar **se registra** (`FND-04 §6.2`). |

## 8. Rastreabilidade — `SF-20` a `SF-22`

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

## 9. Qualidade — `SF-23` a `SF-26`

| # | Regra |
|---|---|
| **SF-23** | **`DoR` da Spec — nove itens. Faltando um, a Spec nao entra em `em-revisao`** (`O3`): **(1)** problema definido **antes** da solucao (`P-2`); **(2)** consumidor nomeado e necessidade demonstrada (`SF-04`); **(3)** as **quatro** perguntas de nao-proliferacao respondidas por escrito (`FND-04 §6.1`); **(4)** `Capability` ativa vinculada (`VC-01`); **(5)** classe e tipo **classificados pelo proponente** (`FND-04 §2`); **(6)** exclusoes declaradas (`SF-08`); **(7)** todo requisito com os **seis** campos (`SF-12`); **(8)** revisores designados, **≠ autor** (`AC-03`); **(9)** pre-condicoes de `FND-04 §6` linha *Spec* satisfeitas — inclusive **`Produto existe`**. |
| **SF-24** | **`DoD` da Spec — dez itens. Faltando um, a mudanca nao encerra:** **(1)** `QG-1` liberado por **DEP-EXE**, registrado com responsavel e data (`FND-01 §6.2`); **(2)** revisao independente concluida; **(3)** aprovacao pela classe (`SF-10`); **(4)** ratificacao **se** `C3` ou `Tipo 1` (`LM-02`); **(5)** cadeia de nove elos percorrivel (`SF-20`); **(6)** entrada no **catalogo mestre** com custo **medido** (`RG-02`, `CE-02`); **(7)** cobertura das **quatro** categorias de requisito (`SF-25`); **(8)** suposicoes, limites, **rollback** e **criterio de abandono** declarados (`SF-26`); **(9)** `FIT` emitido se `C2` ou `C3` (`CC-04`, `QG-6`); **(10)** indices `M3` atualizados na **mesma** mudanca (`CV-04`, `IX-02`). |
| **SF-25** | **Quatro categorias de requisito, e a ausencia de qualquer uma se declara com motivo:** **`FUNCIONAL`** · **`NAO FUNCIONAL`** *(com numero, instrumento e data — `CE-04`)* · **`NEGATIVO`** *(o que **nao** deve ocorrer; e o unico modo de especificar seguranca e limite)* · **`DE FALHA`** *(o que acontece quando o caminho feliz nao ocorre)*. **Spec que so tenha requisito funcional esta incompleta**, e a incompletude **e declarada, nunca presumida como ausencia de necessidade**. |
| **SF-26** | **Quatro declaracoes de limite, obrigatorias e distintas:** **`SUPOSICAO`** *(o que se assume verdadeiro sem verificar, e o que muda se for falso)* · **`LIMITE`** *(o que esta fora da capacidade declarada, com o numero)* · **`ROLLBACK`** *(como se desfaz, com responsavel e custo — `RB-01`)* · **`ABANDONO`** *(como se sabe que esta Spec deixou de ser necessaria — quarta pergunta de `FND-04 §6.1`)*. **Nenhuma das quatro admite *"nao aplicavel"* sem motivo escrito.** |

## 10. Mudanca — `SF-27` a `SF-30`

| # | Regra |
|---|---|
| **SF-27** | **`Spec` e `M2` — versionavel, com texto anterior preservado no historico** (`FND-10 §6.2`). **A versao segue o efeito, nao o tamanho do texto** (`CC-02`, `AL-01`): **MAIOR** quando um `MUST` e criado, removido ou tem o criterio de aceite alterado; **MENOR** quando um `SHOULD`/`MAY` muda ou um requisito e acrescentado sem alterar `MUST` existente; **CORRECAO** quando nada normativo muda. **Alteracao de conteudo sem incremento de versao e nao conformidade** (`AC-11`). |
| **SF-28** | **Alteracao silenciosa e nula, e heranca implicita e proibida.** Nenhum requisito muda de sentido sem incremento de versao e linha de historico (`LC-01`, `GV-01`). **Nenhuma Spec herda requisito de outra por proximidade, por refinar ou por estar no mesmo produto:** o que vincula e a **relacao declarada** (`SF-21`) e o **requisito citado por `ID`**. |
| **SF-29** | **Toda emenda declara cinco coisas:** **impacto** · **compatibilidade** *(retro-compativel ou nao)* · **dependentes** *(enumerados, nunca *"todos"*)* · **migracao** *(quem migra cada dependente, e quando)* · **depreciacao ou substituicao** *(`O6`/`O7`, com sucessor nomeado)*. **Emenda incompativel sem plano de migracao e mudanca incompleta** (`CV-04`, `CC-03`), **nao norma nova**. |
| **SF-30** | **`Spec` que esteve em `ativo` nunca volta a `rascunho`** (`RB-02`). Corrige-se **superando** (`O6`), com **sucessor `ativo`** e **todos** os dependentes migrados (`LC-05`); anula-se sem substituto por **retirada** (`O9`), declarando **o que passa a valer no lugar** (`SU-04`). **`substitui`/`substituido_por` sao declarados nos dois lados** (`LN-02`). |

## 11. Economia de contexto — `SF-31`

| # | Regra |
|---|---|
| **SF-31** | **Cinco exigencias de economia, e as cinco sao medidas, nunca estimadas.** **(1) `resumo` operacional** — uma linha, ate 200 caracteres, em voz ativa, dizendo **o que a Spec faz** e nao o que ela e (`AC-02`). **(2) Gatilho de ativacao** — a condicao que torna a Spec necessaria, no catalogo mestre (`FND-10 §8.3`). **(3) Pacote minimo** — o que precisa vir junto, **e so isso**. **(4) Secoes sob demanda** — a Spec e escrita em **blocos rotulados e independentes**, e o perfil padrao e **`sob-demanda`** (`FND-10 §10.3`). **(5) Custo medido** — **linhas do arquivo**, por `wc -l`, com data (`CE-02`, `CE-04`). **Carregar a Spec inteira para consultar um requisito e falha de curadoria** (`CE-01`, `PC-01`): **o requisito e enderecavel pelo seu `ID` (`RQ-nn`), e citar `<SPC-id> RQ-nn` obriga a carregar o bloco daquele requisito, nao o documento.** Spec que ultrapasse **o dobro da mediana do seu tipo** e candidata a especializacao por `CE-05` — **e `SF-19` decide se especializa**. |

## 12. Template, registro e regime de mudanca deste Framework — `SF-32`

| # | Regra |
|---|---|
| **SF-32** | **Um template canonico, um registro mestre, e nenhum registro novo.** **Template:** [`TPL-spec`](templates/TPL-spec.md), unico, mantido por `DEP-PRD` *(dono do tipo)* e aprovado por `DEP-GOV` (`FND-09 §8.2` linha `TPL`); especializar template exige `FND-10 §10.2`. **Registro mestre:** o [catalogo mestre](../governance/artifact-registry.md) — que `RG-04` ja declara *"a visao transversal do acervo"* — e o **contador oficial** da sequencia `SPC` e o **indice do diretorio** onde as Specs vivem (`FND-03 §2.3`, `RG-04`). **Nenhum registro de Specs e criado por este Framework:** criar um terceiro seria proliferacao (`FND-04 §6.1`) e arquivo satelite por artefato, proibido por `RG-05`. **Criar Spec e incrementar o contador sao a mesma mudanca** (`CV-04`, `IX-02`) — a regra que `RD-32` mostrou nao estar sendo exercida. **Este Framework e artefato `M2`** (`FND-10 §6.2`): emenda-se **por versao**, com o texto anterior **preservado no historico**, pela **classe do efeito** (`AL-01`, `CC-02`), e a emenda **so vigora com aprovacao e ratificacao do SOBERANO** (`FND-09 §8.2` linha `FND`; `LM-02`). **A clausula de imutabilidade de `M1` da sede anterior nao se transporta** — e a **unica alteracao de merito** desta promocao, declarada em §2 e em [ADR-0022](../decisions/ADR-0022-sede-canonica-do-framework-de-specifications.md). |

## 13. O vinculo `Spec` × `Produto` — **inalterado, e por isso nenhuma `Spec` e criavel hoje**

> **Esta secao nao decide nada. Ela registra o que continua valendo**, para que `SF-23` item (9)
> nao seja lido como cumprivel quando nao e.

| Fonte vigente | Texto | Efeito |
|---|---|---|
| [`FND-04 §6`](04-governanca.md), linha *Spec* | pre-condicoes: ***"Produto existe**; problema definido; criterios de aceite verificaveis; escopo negativo explicito"*, e *"**Todas** precisam ser verdadeiras para a criacao ser aprovada"* | **`O1` nao pode ocorrer** (FND-10 §5.2) |
| [`FND-03 §3.6`](03-taxonomia.md) | *"Vive em `products/<slug>/specs/<SPC-id>.md`"* | **Nao ha caminho canonico** fora de um produto (`FND-03 §7.1`) |
| [`FND-10 §4.4`](10-artifact-framework.md) | Local: **`products/<slug>/specs/`** | Terceira fonte, mesmo vinculo |

**Estado medido em 2026-07-29:** **`0`** artefatos de tipo `spec`; **`0`** de tipo `PRO`;
**`products/` ausente** da raiz. **Criar `Produto` e `C2 · Tipo 1` do SOBERANO**
(`FND-04 §6`, linha *Produto*; `FND-09 §8.2`, linha `PRO`; `FND-01 §7.3`).

**As duas saidas permanecem disjuntas e ambas do SOBERANO**, exatamente como
[ADR-0021 §7.3](../decisions/ADR-0021-framework-de-specifications.md) as declarou: **`S1`**
*(ato que crie o primeiro Produto)* habilita a `Spec` **de produto**; **`S2`** *(RFC `C3` → ADR
`C3` → ato)* habilita a `Spec` **de materia nao-produto**. **Este Framework nao exerce nenhuma
das duas, nao escolhe entre elas e nao cria a terceira.** Achado **`RD-33`**, **ABERTO e
BLOQUEANTE**.

> **Por que a sede mudar nao desbloqueia nada.** O bloqueio nunca esteve na sede da norma:
> esta na **pre-condicao de criacao** de `FND-04 §6` e no **local canonico** de `FND-03 §3.6`
> e `FND-10 §4.4`. Promover `SF-*` a `FND` **nao toca nenhuma das tres** — e afirmar o
> contrario seria `LV-05`.

## 14. Limites declarados — **determinado, nao observado**

| # | Limite | Fundamento |
|---|---|---|
| **L1** | **Nenhuma `Spec` real existe.** Todas as **32** regras sao **determinadas, nao observadas** — nenhuma foi exercida contra um artefato concreto | `PI-10`; ressalva `R1` de [FIT-2026-015](../governance/fitness/FIT-2026-015-framework-de-specifications.md) |
| **L2** | **`SF-09` institui 21 blocos obrigatorios sem custo medido.** `CE-04` proibe estimar, e **nada foi estimado**: o valor sera medido na **primeira `Spec`** | ressalva `R2` de FIT-2026-015; `CE-04` |
| **L3** | **Nenhum conflito real entre `Spec`s ocorreu.** `SF-22` e determinado, nao observado | `PI-10` |
| **L4** | **Nenhuma superacao real de `Spec` ocorreu.** `SF-30` e determinado, nao observado | `PI-10` |
| **L5** | **Os pilotos estao DEFERIDOS, nao dispensados.** A primeira `Spec` real **aciona revisao empirica deste Framework**, e a ausencia dela **nao autoriza** ampliar a `Spec` a materia nao-produto nem criar Produto artificial | §15, gatilho de revisao |

## 15. Rastreabilidade e revisao

| Campo | Conteudo |
|---|---|
| **Origem do merito** | [ADR-0021](../decisions/ADR-0021-framework-de-specifications.md) — `SF-01` a `SF-32`, `C2 · Tipo 2`, 2026-07-29. **Permanece `ativo` e intacto** |
| **Origem da sede** | [RFC-0018](../rfcs/RFC-0018-sede-canonica-do-framework-de-specifications.md) → [ADR-0022](../decisions/ADR-0022-sede-canonica-do-framework-de-specifications.md) — `C3 · Tipo 1` |
| **Fontes que este Framework projeta** | §4 *(Spec Contract)* e §5 *(matriz de 50 celulas)*, ambas com declaracao `PJ-02` completa. **Em divergencia prevalece a fonte** (`PJ-03`) |
| **Fontes que este Framework NAO altera** | `FND-03 §3.6` e `§7` · `FND-04 §2`, `§2.1`, `§2.2`, `§6` · `FND-09 §8.2` · `FND-10 §4.4`, `§10.3` |
| **Template canonico** | [`TPL-spec`](templates/TPL-spec.md) **1.1.0** — corrigido por `ADR-0021 §5.11`, que fechou `RD-23` |
| **Registro mestre** | [catalogo mestre](../governance/artifact-registry.md) — contador oficial da sequencia `SPC` (`SF-32`) |
| **Verificacao de aptidao** | [FIT-2026-016](../governance/fitness/FIT-2026-016-canonizacao-e-propagacao.md) |
| **Achados abertos que este Framework NAO fecha** | **`RD-33`** *(bloqueante — §13)* · `RD-34` · `RD-36` · `RD-37` · `RD-39` · `RD-40` · `RD-24` · `RD-27` · `RD-30` · `RD-10` a `RD-13` · `RD-18` · `RD-21` |
| **Gatilho de revisao** | **A primeira `Spec` real** — o unico evento que transforma `SF-*` de determinado em observado (`L1`); **ou** o primeiro **conflito real** entre `Spec`s (`L3`); **ou** a primeira **superacao real** (`L4`); **ou** o ato que resolva `S1` ou `S2` |
| **O que se mede na revisao** | Quantas `Spec`s foram **devolvidas** por `SF-12`, `SF-16` ou `SF-23`, e por qual regra; **linhas medidas** da primeira `Spec` contra o dobro da mediana do tipo (`CE-05`); quantas vezes o requisito foi consultado **por `RQ-nn`** sem carregar o documento (`SF-31`) |
| **Data de reavaliacao** | **2027-01-28** |

---

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-GOV | **Sede fundacional** da norma da `Spec`. Recebe `SF-01` a `SF-32` de [ADR-0021](../decisions/ADR-0021-framework-de-specifications.md) **declarando, regra por regra, origem, transformacao e equivalencia** (§2): **30** regras `T-IDENTICA` *(byte a byte)*, **1** `T-REFERENCIAL` *(`SF-05`)* e **1** `T-MERITO-DECLARADO` *(`SF-32`)*. **A unica alteracao de merito e o regime de mutabilidade** — de `M1` *(nunca se emenda; corrige-se por ADR sucessor)* para `M2` *(emenda por versao, com ratificacao do SOBERANO)* —, e ela esta isolada em §2.3, **com o tradeoff declarado no sentido correto: a sede melhor e mais protegida e mais caro de mudar**. Preserva integralmente o contrato de **21 blocos**, a semantica normativa *(3 verbos, 6 campos por requisito, 6 naturezas de enunciado, 5 metodos de verificacao, 10 adjetivos vedados)*, os **7 perfis**, a matriz de **50 celulas** `C0`–`C3` × `Tipo 1/2` como **projecao declarada** (`PJ-02`), a cadeia de **9 elos**, as **6 relacoes** *(com `conflita` declarada achado e nao aresta)*, o **`DoR` de 9**, o **`DoD` de 10**, o regime de mudanca da `Spec` e a economia de contexto. **`0` regras renumeradas · `0` titulares criados · `0` portoes criados ou removidos · `0` celulas de `FND-09 §8.2` alteradas · `0` bytes no vinculo `Spec` × `Produto`.** §13 registra que **nenhuma `Spec` e criavel** — `RD-33`, aberto e bloqueante — e que **promover a sede nao desbloqueia nada**. §14 declara os **cinco limites**, comecando por *"nenhuma `Spec` real existe: as 32 regras sao determinadas, nao observadas"*. **Nao vigora sem ato** (FND-01 §9). |
| 1.1.0 | 2026-08-02 | DEP-GOV | Emenda **C3** por [ADR-0032](../decisions/ADR-0032-separacao-de-proponente-e-aprovador-na-spec-c1.md), que sana **`RD-91`**: **§5**, matriz de `SF-10`, linha *Aprovacao*, coluna **`C1 · T2`**, passa de `proprietario + revisor` para **`DEP-EXE + revisor`**, **em cascata** com a emenda da fonte — `FND-09 §8.2`, linha `SPC` **1.6.0** —, na mesma mudanca, como `ADR-0019 §4` *(Alternativa E)* fixou e `CV-04` exige. **`1` celula de `50`.** A declaracao `PJ-02` de §5 acrescenta **`FND-04 §3.1`** a lista de fontes, porque o valor projetado passa a derivar tambem dela. **O defeito nao era desta projecao:** as duas metades da colisao — `Proposta = DEP-PRD` e `Aprovacao = proprietario + revisor` — **reproduziam literalmente** `FND-09 §8.2` linha `SPC` e `FND-04 §2.1` linha `C1`, e por `PJ-03` e `FND-01 §10` **emendar so aqui nao sanaria nada**; por isso a fonte foi emendada primeiro. **`0` regras `SF-*` alteradas em texto normativo** — `SF-10` continua remetendo, nunca decidindo —, **`0` titulares criados** *(`DEP-EXE` ja consta de `FND-04 §2` e desta mesma matriz em `C2`)*, **`0` alteracoes em `DoR`, `DoD`, criterio de aceite ou qualquer regra de conteudo de `Spec`**, **`0` celulas fora da emendada**, **`0` bytes em `FND-04`**. **`SPC-001` NAO e reclassificada:** nasceu `C2 · Tipo 2` validamente, e §2 declara que a emenda **nao retroage**. **`C0 · T2` permanece colapsada e declarada** em `RD-91`. §2 ganha **nota de alcance temporal**: a partir daqui a matriz difere em **1** celula da copia de `ADR-0021 §5.3`, artefato `M1` que nunca se emenda — **prevalece esta**, por `ADR-0022 §5.4`, e o registro e `RD-98`. **Nao vigora sem ato** (FND-01 §9; `LM-02`; `SF-32`). |
