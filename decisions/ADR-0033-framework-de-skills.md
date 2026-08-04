---
id: ADR-0033-framework-de-skills
titulo: Framework de Skills — SK-01 a SK-26, contrato, gatilho, procedimento, reuso e descontinuacao, sem emendar fonte alguma
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
decisoes_relacionadas: [ADR-0003, ADR-0015, ADR-0020, ADR-0021, ADR-0022, ADR-0032]
substitui: []
substituido_por: null
classe_mudanca: C2
tipo_decisao: 2
supera: null
superado_por: null
resumo: Institui o Framework de Skills como SK-01 a SK-26 dentro do proprio ADR, recebendo SKL de FND-03 e FND-09 sem criar entidade, tipo, template, portao ou campo novo, e declara que o gatilho e atributo minimo ja previsto em FND-09 E-13 que TPL-skill omite.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# ADR-0033: Framework de Skills

## Contexto

A `Skill` tem **entidade** (`FND-03 §3.5`, `FND-09 §E-13`), **prefixo**, **local canonico**,
**template** (`TPL-skill`) e **autoridade** (`FND-09 §8.2` linha `SKL`) — e **nao tem
contrato**. Nenhuma fonte responde, em um lugar so, o que uma `Skill` deve conter para ser
aceita.

**E a mesma configuracao que produziu quatro achados em quatro missoes consecutivas na
`Spec`**, e que `ADR-0021 §1` diagnosticou em uma frase: *"tinha tipo, entidade, definicao,
autoridade e template, e nao tinha contrato"*.

**Estado medido em 2026-08-03:** `skills/` **nao existe**; **`0`** `Skill`s.

## Decisao

**Instituir `SK-01` a `SK-26`** — o contrato da `Skill` — **dentro deste ADR**, recebendo a
entidade e os atributos das fontes vigentes, **sem emendar nenhuma delas**.

## Classe — determinada por norma citada, nunca por analogia

| Variavel | Valor | Fundamento |
|---|---|---|
| **Classe** | **`C2`** | `FND-04 §2.1`: `C2` → instrumento **`RFC` → `ADR`**, aprova **`DEP-EXE` + parecer `DEP-GOV`**. `AL-01`: a classe e a do **efeito**, e o efeito e institurir norma sobre entidade existente |
| **Tipo** | **`2` — reversivel** | `FND-04 §2.2`. Norma em `ADR` e **superavel por `ADR` sucessor** (`CC-06`, `SU-01`). Nao cria dependencia externa, nao expoe dado, nao move fronteira |
| **Aprovador** | **`DEP-EXE`**, com parecer de **`DEP-GOV`** | `FND-04 §2.1`, linha `C2`; `FND-04 §2.2`, celula `C2 × Tipo 2` — *"DEP-EXE aprova"*. **`DEP-GOV` nao aprova o que propos** (`PI-05`) |
| **Ratificacao** | **nao exigida** | `FND-04 §2.1` — *"Se Tipo 1"*, e nao e; `FND-09 §8.2` linha `ADR` — *"SOBERANO se `C3` ou `Tipo 1`"* |

**Precedente identico, conferido no frontmatter e nao de memoria:** `ADR-0021`
*(`classe_mudanca: C2` · `tipo_decisao: 2` · `aprovador: DEP-EXE` ·
`ratificacao: nao-exigida`)*, cadeia `RFC-0017` → `ADR-0021`, com `FIT-2026-015`.

### A sede, e os dois custos que nao se confundem

| O que se faz | Classe | Ato do Soberano? | Feito aqui? |
|---|---|---|---|
| **Instituir a norma** | **`C2 · Tipo 2`** | **Nao** | ✅ **sim** |
| **Promover a sede `FND`** | `C3 · Tipo 1` | **Sim** | ❌ **nao** — precedente `ADR-0022` |

**A promocao nao e pre-requisito da instituicao**, e nao e feita aqui **por criterio, nao por
economia**: as **26** regras sao **determinadas e nao observadas** — `0` `Skill`s existem —, e
canonizar em sede fundacional antes do primeiro exercicio repete o que `L1` de `FND-11 §14`
registrou e `RD-107` mediu.

> **O tradeoff, declarado no sentido correto e nao no que convem.** Nascendo em `ADR`, este
> Framework e **`M1`** — `FND-10 §6.2` lista `M2` como *"FND, CAP, Cartas, SPC, SKL, WFL,
> TOL, TPL, MEM"*, e **`ADR` nao consta**. **`M1` nunca se emenda** (`AC-10`, `CC-01`):
> **corrigir uma virgula exige `ADR` sucessor**. **A sede barata e a sede mais cara de
> corrigir**, e e exatamente o custo que `ADR-0021` pagou e que `ADR-0022` depois desfez.

## Origem, transformacao e equivalencia — as 26 regras

**Origem do merito:** candidato redigido **fora do acervo** na Missao 1.14 —
`CANDIDATO-framework-de-skills.md`, **253** linhas, `sha256`
`b9b47d8b75979a8197fa1a22…`. **Ele nao e artefato e nao vigora**; este `ADR` **recebe** o
merito, na forma que `FND-10` reserva a decisao.

| Classe de transformacao | Definicao | Quantas |
|---|---|---|
| **`T-IDENTICA`** | Texto normativo reproduzido sem alteracao de merito | **25** |
| **`T-MERITO-DECLARADO`** | Ha alteracao de merito, e ela e **declarada e nomeada** | **1** — `SK-26` |

### A unica alteracao de merito, isolada

| Campo | Candidato `SK-26` | **`ADR-0033` `SK-26`** |
|---|---|---|
| **Classe de mutabilidade deste Framework** | **`M2`** — *"emenda-se por versao e NAO exige ato"* | **`M1`** — imutavel apos eficacia; **superavel por `ADR` sucessor** |
| Fundamento | — | `FND-10 §6.2`: `M2` lista `FND, CAP, Cartas, SPC, SKL, WFL, TOL, TPL, MEM`; **`ADR` nao consta**, e figura em `M1` |
| **O que NAO muda** | — | O conteudo das **26** regras; quem decide sobre `Skill`; o vinculo com `Capability`; o local canonico |

> **A afirmacao do candidato era FALSA para a sede escolhida, e nao se transporta.** Corrigi-la
> em silencio seria a familia de **`RD-101`** — *artefato que afirma propriedade que ja nao
> vale*. **Fica declarada aqui, e a `Skill` — o tipo — continua `M2`**, porque `FND-10 §6.2`
> a lista: **o que e `M1` e este `ADR`, nao a `Skill`.**

---

## 1. O que uma Skill e, e o que nao e — `SK-01` a `SK-05`

| # | Regra |
|---|---|
| **SK-01** | **Uma `Skill` e capacidade REUTILIZAVEL e NOMEADA: procedimento invocavel por MAIS DE UM PAPEL para produzir resultado previsivel.** `FND-03 §3.5`. As tres condicoes sao **cumulativas**, e `FND-04 §6` linha *Skill* as repete como pre-condicao: *"procedimento se repete; resultado verificavel; usavel por mais de um papel"*. Faltando uma, **nao e Skill**. |
| **SK-02** | **Skill pertence a ORGANIZACAO, nunca a um agente.** `FND-03 §3.5`: *"se so um papel pode usar, e procedimento interno da Carta dele"*. O teste e de **propriedade**, nao de uso: o que a descaracteriza e ela **depender** de quem a invoca. Skill que so faca sentido dentro de um agente e **secao da Carta dele**, e cria-la como `SKL` e proliferacao (`FND-04 §6.1`). |
| **SK-03** | **O nome e sempre ACAO: `<dominio>-<verbo>-<objeto>`.** `FND-03 §3.5`. **E o espelho exato da regra do Agente**, que exige **substantivo de funcao, nunca verbo** (`FND-03 §3.3`): **agente e quem; skill e o que se faz**. |
| **SK-04** | **Skill nao e `Workflow`, e a fronteira e o numero de papeis e a existencia de portao.** `FND-10 §4.8`, linha *Playbook*: *"`SKL` se um papel; `WFL` se atravessa papeis ou tem portao"*. **Reusavel por varios ≠ atravessa varios:** `SK-01` exige que seja **usavel** por mais de um papel; esta regra exige que seja **executada** por um de cada vez. Procedimento que **precise** de dois papeis para completar **e `WFL`**. |
| **SK-05** | **Skill nao e `Prompt` nem `Playbook`, e os dois ja foram recusados como tipos.** `FND-10 §4.8`: **`Prompt`** *"e materializacao textual de Carta de agente ou corpo de Skill"*, com a nota decisiva — ***"prompt reusado por 2+ componentes JA E Skill"***; **`Playbook`** *"e nome de uso para procedimento recorrente"*. Criar tipo para qualquer dos dois e **`MT-01`**, e o uso de entidade nao ritualizada e **nulo**. |

## 2. Skill Contract — `SK-06` a `SK-09`

> **Declaracao de projecao (`PJ-02`).** **Fonte:** `FND-03 §4`, `§3.5` · `FND-09 §E-13` ·
> `FND-10 §2.2`, `§2.5`, `§4.8` · `FND-09 §8.2` linha `SKL` · `FND-04 §6` linha *Skill* ·
> `FND-08 §8`. **Campos projetados:** apenas **quais blocos a Skill deve conter**.
> **Em divergencia prevalece a fonte** (`PJ-03`).

| # | Regra |
|---|---|
| **SK-06** | **O contrato da Skill e o universal do artefato mais os atributos minimos de `FND-09 §E-13`, e NENHUM campo novo.** Os **15** campos de `FND-03 §4` e os **5** de `FND-10 §2.2` sao obrigatorios; e sao obrigatorios tambem **`capabilities`, `gatilho`, entradas, passos, saidas e criterio de verificacao**, porque `FND-09 §E-13` os lista como ***atributos minimos*** e declara a relacao ***`e-acionada-por` gatilho declarado***. **Ausencia = nao conforme = veto de `DEP-GOV`** (`AC-06`). **`gatilho` NAO e campo novo:** e campo que a norma **ja preve** e que `TPL-skill` **omite** — medido, e o achado e `RD-122`. |
| **SK-07** | **A Skill declara a `Capability` que exerce, no minimo uma.** `FND-08 §8` e `R-02` de `FND-09 §6.1` — vinculo **obrigatorio, minimo 1, nunca vazio**; **`VC-03`**: mais de tres e sinal de componente amplo demais. Capability inexistente, `proposta` ou `aposentada` e **elo quebrado** (`VC-01`). |
| **SK-08** | **A Skill declara *Quando NAO usar* em bloco proprio e obrigatorio.** `TPL-skill` ja reserva a secao **§2**, e deixa-la vazia e **defeito**, nao estilo (`PI-09`). **E este bloco que impede a Skill de ser aplicada fora do caso que a justificou** — e Skill aplicada fora do caso produz resultado previsivelmente errado, a pior classe de falha por ser silenciosa (`SK-19`). |
| **SK-09** | **Os blocos obrigatorios sao os ONZE do template vigente, mais o `gatilho`: doze.** O template ja cobre quando usar, quando nao usar, entradas, procedimento, saidas, criterio de sucesso, modos de falha, normas aplicaveis, ganho `PI-14`, criterio de descontinuacao e rastreabilidade. **O decimo segundo e o `gatilho`, e ele nao e acrescimo deste Framework:** e exigencia de `FND-09 §E-13` e de `FND-10 §4.8` que o template **nao atende**. |

## 3. Autoridade e ciclo — `SK-10`

| # | Regra |
|---|---|
| **SK-10** | **A autoridade sobre uma Skill e derivada, nunca declarada no artefato.** E funcao de **(a)** a classe do efeito (`AL-01`, **`C2` como piso de criacao** por `FND-04 §6`); **(b)** o tipo de reversibilidade (`FND-04 §2.2`); **(c)** o dado que a Skill toca. **Skill que fixe aprovador em texto e nao conforme** — foi o defeito de `RD-23`. **Ratificacao nao se exige nunca** (`FND-09 §8.2` linha `SKL`, *Ratifica* = `—`), **e a Skill nao adquire exigencia de ato por ser invocada em contexto que a tenha:** quem exige ato e a **materia**, no seu proprio rito. **Skill nao executa ato do Soberano e nao o antecipa.** |

## 4. Gatilho — onde vive o acionamento — `SK-11` a `SK-13`

| # | Regra |
|---|---|
| **SK-11** | **Toda Skill declara `gatilho`: o que a aciona, quem pode aciona-la, e sob que pre-condicao.** `FND-10 §4.8` aloja o acionamento **no atributo `gatilho` de `SKL`/`WFL`** em vez de criar o tipo `Command`, e `FND-09 §E-13` o lista entre os **atributos minimos**. **Tres campos, nenhum opcional:** **o que dispara** *(evento, invocacao por papel, ou etapa de `WFL`)* · **quem pode disparar** *(papel, nunca pessoa)* · **pre-condicao**. **Gatilho ausente le-se como acionavel por qualquer papel** — e por isso **declara-se sempre**. |
| **SK-12** | **O gatilho NAO cria superficie com ciclo de vida proprio, e essa e a linha que ele nao cruza.** O gatilho **vive e morre com a Skill**: nao tem versao propria, identificador proprio, citabilidade externa nem autoridade propria. **Se um acionamento passar a precisar de qualquer dessas quatro coisas, o gatilho de reabertura de `FND-10 §4.8` estara SATISFEITO** — *"superficie com ciclo de vida independente do procedimento"* — **e o caminho passa a ser o rito de entidade nova** (`FND-09 §11.1`, `C3 · Tipo 1`), **jamais esticar este atributo**. Esticar seria **criar entidade por uso**, que `MT-01` torna **nula**. |
| **SK-13** | **O gatilho declara IDEMPOTENCIA, e a declaracao e obrigatoria.** *"Invocar duas vezes produz o mesmo efeito que invocar uma?"* — **sim** ou **nao**, com o motivo. **Skill nao idempotente com efeito externo nao e elegivel a repeticao automatica**, e quem a invoca precisa saber **antes**. **`nao declarado` le-se como NAO idempotente.** |

## 5. Procedimento — `SK-14` a `SK-16`

| # | Regra |
|---|---|
| **SK-14** | **O procedimento e executavel por outro papel SEM CONSULTAR O AUTOR, e esse e o teste de aceite da Skill.** Deriva de `SF-12`, campo *criterio de aceite*, aplicado ao **fazer** em vez de ao **verificar**. **Procedimento que exija o autor para ser executado nao e Skill: e conhecimento tacito com aparencia de artefato**, e nao satisfaz `SK-01`. |
| **SK-15** | **O procedimento declara os passos em ordem, e cada passo diz o que produz.** **Passo que nao produz nada e candidato a remocao** — `HO-05` aplicado dentro da Skill, pelo mesmo fundamento com que se aplica a etapa de Workflow. |
| **SK-16** | **O procedimento nao decide arquitetura, nao escolhe tecnologia e nao cria norma.** Deriva de `SF-02` e de `PD-02` — componente nao produz `FND`/`ADR`. **Skill que decida e `ADR` ou Nota de Decisao disfarcada**, e a decisao tomada dentro dela **nao vigora** (`GV-01`). **A Skill EXECUTA a decisao; ela nao a toma** — e e o que `FND-09 §E-13` ja diz na linha *Autoridade*: ***"Nenhuma. Skill nao decide, nao aprova e nao concede autonomia a quem a invoca."*** |

## 6. Entradas, saidas e falha — `SK-17` a `SK-19`

| # | Regra |
|---|---|
| **SK-17** | **Entradas declaram origem e obrigatoriedade; saidas declaram formato e destinatario.** Entrada sem origem **nao e verificavel antes da execucao**, e o custo disso aparece so no meio do procedimento. |
| **SK-18** | **O criterio de sucesso e verificavel por um dos cinco metodos de `SF-14`**, ou nao e criterio. *"Funcionou"* nao e criterio; *"produziu o arquivo X com N linhas, conferido por `MEDICAO`"* e. **Recebido, sem criar metodo novo.** |
| **SK-19** | **Os modos de falha conhecidos incluem obrigatoriamente a saida PLAUSIVEL E ERRADA.** A lista **nao esta completa** sem ela: **resultado bem-formado e incorreto nao dispara alarme nenhum**. Declara-se **como se detecta**, por metodo de `SF-14`. **Ausencia e incompletude declarada, nunca ausencia de risco.** |

## 7. Reuso e nao-proliferacao — `SK-20` a `SK-22`

| # | Regra |
|---|---|
| **SK-20** | **As quatro perguntas de `FND-04 §6.1` sao respondidas POR ESCRITO antes da criacao.** Skill sem **consumidor nomeado** e **necessidade demonstrada** e devolvida. **O ganho `PI-14` e declarado com o SINAL QUE O MOTIVOU**, e **sinal antecipado nao serve**: `FND-08 §7.1` recusa antecipacao. ***"Vai ser util depois" nao cria Skill.*** |
| **SK-21** | **Skill nao depende de agente, e a cadeia nao tem ciclo.** `R-04` de `FND-09 §6.1` — `SKL`/`WFL` dependem de `SKL` e `TOL`, **sem ciclo**; `PD-11` proibe depender de estrato superior. **Skill que dependa de um agente inverte a relacao** — o agente e que usa a Skill — **e viola `SK-02`**. |
| **SK-22** | **Duas Skills que facam a mesma coisa sao duplicata, e a duplicata resolve-se reusando, nunca coexistindo** (`MT-02`). A verificacao e **no catalogo mestre, antes de criar**. **Skill quase igual a outra e sinal de que a diferenca deveria ser PARAMETRO**, nao artefato novo. |

## 8. Normas, custo e contexto — `SK-23` a `SK-24`

| # | Regra |
|---|---|
| **SK-23** | **A Skill declara as normas aplicaveis por identificador, e nao as reproduz.** **Copiar o texto da norma dentro da Skill cria segunda sede que deriva em silencio** — familia de `RD-101`. **Cita-se; nao se copia.** Em divergencia **prevalece a fonte** (`PJ-03`, `FND-01 §10`). |
| **SK-24** | **O custo de contexto da Skill e MEDIDO, e ela e escrita para ser carregada em parte.** `CE-01`, `CE-02`, `CE-04` *(proibido estimar)* e `PC-01`. **Skill e escrita em blocos rotulados e independentes**, e **carregar a Skill inteira para executar um passo e falha de curadoria**. Skill que ultrapasse **o dobro da mediana do seu tipo** e candidata a especializacao (`CE-05`), e **`FND-04 §6.2` decide se especializa**. |

## 9. Mudanca, descontinuacao e registro — `SK-25` a `SK-26`

| # | Regra |
|---|---|
| **SK-25** | **`SKL` e `M2`** (`FND-10 §6.2`). A versao segue **o efeito** (`AL-01`): **MAIOR** quando muda o gatilho, o criterio de sucesso, a idempotencia ou uma saida; **MENOR** quando se acrescenta passo sem alterar saida nem criterio; **CORRECAO** quando nada normativo muda. **Alteracao silenciosa e nula** (`AC-11`, `GV-01`). **Criterio de descontinuacao e obrigatorio**, e **aposentar Skill e `ADR`** (`FND-09 §8.2` linha `SKL`), nunca ato tacito por desuso. Skill superada **migra os dependentes** (`LC-05`), **enumerados, nunca *"todos"***. |
| **SK-26** | **Um template canonico, um registro mestre, e nenhum registro novo.** **Template:** [`TPL-skill`](../foundation/templates/TPL-skill.md), unico — **e ele precisa dos campos `gatilho` e `capabilities` antes do primeiro uso** *(`RD-122`; rito de `TPL`, `C2`, sem ato)*. **Registro mestre:** o [catalogo mestre](../governance/artifact-registry.md), **contador oficial** da sequencia `SKL`; **criar Skill e incrementar o contador sao a mesma mudanca** (`CV-04`, `IX-02`). **Nenhum registro novo** — seria proliferacao (`FND-04 §6.1`, `RG-05`). **⚠️ ESTE `ADR` E ARTEFATO `M1`** (`FND-10 §6.2`): **o texto nunca muda**; corrige-se **superando-o com `ADR` sucessor** que o referencie (`CC-06`, `SU-01`). **A `Skill` — o tipo — continua `M2`**; o que e `M1` e **este documento**. |

---

## O que este ADR NAO faz

| # | Nao faz | Verificacao |
|---|---|---|
| **N1** | **Nao cria entidade.** `SKL` ja existe | `FND-03 §3.5`, `FND-09 §E-13`, `FND-09 §8.2` — **`0`** linhas acrescentadas |
| **N2** | **Nao cria campo novo.** `gatilho` e `capabilities` sao **atributos minimos ja declarados** | `FND-09 §E-13`; `AC-07` |
| **N3** | **Nao cria tipo documental, template, diretorio, papel, classe nem verbo de autoridade** | `FND-09 §11.1`; `MT-01`, `CS-01` |
| **N4** | **Nao cria nem libera portao.** **`GO-TO-SKILLS` NAO e liberado aqui** | Liberar portao e **ato de autoridade** (`FND-01 §6.2`), e este ADR nao e autoridade. **Portoes de qualidade:** `QG-0` a `QG-6` — **7 antes, 7 depois**. **Portoes de sequencia:** `GO-TO-SPECS` e `GO-TO-SKILLS` — **2 antes, 2 depois**. ⚠️ **O metodo de contagem e declarado porque o ingenuo se auto-contamina:** medir por `grep -ooh "GO-TO-[A-Z-]*"` devolve **3** depois desta emissao, e o terceiro e o token vazio `GO-TO-`, capturado do proprio literal `GO-TO-` seguido de asterisco escrito nesta celula. **Nao e portao: e a notacao do documento contaminando a medicao do documento.** Conte **nomes de portao existentes**, nunca o padrao com curinga |
| **N5** | **Nao reabre o tipo `Command`** | `SK-12` declara a linha que o gatilho nao cruza e remete ao rito de `FND-09 §11.1`. O gatilho de reabertura de `FND-10 §4.8` segue **nao satisfeito** |
| **N6** | **Nao emenda fonte alguma** | **`0` bytes** em `FND-01` a `FND-11` e em `TPL-skill` |
| **N7** | **Nao cria `Skill` nem `skills/`** | **`0`** `Skill`s · `skills/` **inexistente** |
| **N8** | **Nao promove a si mesmo a `FND`** | `C3 · Tipo 1` **com ato** — precedente `ADR-0022` |
| **N9** | **Nao admite os outros quatro candidatos** | Seguem fora do acervo, intactos |

## Limites declarados — determinado, nao observado

| # | Limite |
|---|---|
| **L1** | **Nenhuma `Skill` real existe.** As **26** regras sao **determinadas, nao observadas** |
| **L2** | **`SK-11` a `SK-13` — o contrato do gatilho — sao a contribuicao propria e a parte MENOS testada** |
| **L3** | **`SK-12` declara a linha que o gatilho nao cruza SEM ter observado nenhuma tentativa de cruza-la.** E derivada da norma, **nao da experiencia** |
| **L4** | **`TPL-skill` nao produz `Skill` conforme:** omite **`gatilho`** e **`capabilities`**, medidos com controle positivo *(`proprietario` = 1)*. **`RD-122`, ABERTO** — este ADR **nao o sana**, e §*Q1* de [`RFC-0028`](../rfcs/RFC-0028-sede-e-instituicao-do-framework-de-skills.md) declara que **nao impede** |
| **L5** | **A sede e `M1`.** Corrigir qualquer das 26 regras exigira **`ADR` sucessor** |

## Consequencias

| Para quem | O que muda |
|---|---|
| **Qualquer DEP** | Passa a poder propor `Skill` com contrato objetivo; antes, nao havia o que cumprir |
| **DEP-GOV** | Ganha criterio de veto verificavel (`AC-06`) sobre ficha incompleta |
| **DEP-EXE** | Aprova `Skill` em `C2`, **sem ato** |
| **DEP-QAR** | `FIT` obrigatorio em `C2` (`CC-04`, `QG-6`) |
| **Quem for criar a primeira `Skill`** | **Tera de acrescentar `gatilho` e `capabilities` a mao**, porque o template os omite — `RD-122` |

## Rastreabilidade

| Campo | Conteudo |
|---|---|
| **Origem** | [RFC-0028](../rfcs/RFC-0028-sede-e-instituicao-do-framework-de-skills.md) → este ADR |
| **Origem do merito** | Candidato fora do acervo, Missao 1.14, **253** linhas |
| **Verificacao de aptidao** | [FIT-2026-026](../governance/fitness/FIT-2026-026-framework-de-skills.md) |
| **Registro da missao** | [PT-2026-020](../governance/relatorio-transicao-2026-08-03-admissao-skills.md) |
| **Achado que este ADR NAO fecha** | **`RD-122`** *(`TPL-skill` sem `gatilho`)* · `RD-123` · `RD-124` *(numero de Goal)* · `RD-116` |
| **Gatilho de revisao** | A **primeira `Skill` real** (`L1`); **ou** a primeira tentativa de dar ciclo de vida proprio a um gatilho (`SK-12`) — **que e o sinal de `TE-7` e reabre `Command`** |
| **Data de reavaliacao** | **2027-02-03** |
