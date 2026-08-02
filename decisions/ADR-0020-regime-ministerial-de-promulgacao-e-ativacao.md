---
id: ADR-0020-regime-ministerial-de-promulgacao-e-ativacao
titulo: Promulgar e ativar sao operacoes ministeriais, com executor, verificador e registrador ja declarados
tipo: adr
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-07-29
atualizado_em: 2026-07-29
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0005, ADR-0008, ADR-0012, ADR-0015, ADR-0016, ADR-0017, ADR-0018, ADR-0019]
substitui: []
substituido_por: null
classe_mudanca: C2
tipo_decisao: 2
supera: null
superado_por: null
resumo: Declara que promulgar e ativar decorrem de aprovacao ou ratificacao valida, institui PA-01 a PA-14 e a matriz de regime operacional como projecao declarada, sem criar autoridade nem emendar documento fundacional.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# ADR-0020: Promulgar e ativar sao **operacoes ministeriais**

> **Decisao em uma frase.** **Promulgacao e ativacao nao sao decisoes discricionarias: sao
> operacoes ministeriais que decorrem de aprovacao ou ratificacao valida**, e seus **executor,
> verificador e registrador ja estao nomeados** em FND-04 §3 e §4, FND-07 §5, FND-09 §7.5 e
> `AU-06`, FND-10 §5.2, §5.4 e §6.1, e na Carta de DEP-GOV. **Nenhum titular e criado.**

## Proposito

Fechar o achado **`RD-22`** declarando, pelo menor instrumento competente, a natureza de
`promulgar` e `ativar` e o mapeamento de cada ato a autoridade decisoria, executor ministerial,
verificador e registrador.

## Escopo

| Item | Definicao |
|---|---|
| **Inclui** | Natureza de promulgacao e ativacao; `PA-01` a `PA-14`; a **matriz de regime operacional** como projecao declarada; a cascata de impedimento, de ausencia de ato, de falha de hash, de rollback e de superacao |
| **Nao inclui** | Qualquer emenda a `foundation/`; qualquer titular novo; qualquer verbo de autoridade novo; `RD-23`, `RD-24`, `RD-26`, `RD-27`, `RD-10` |
| **Subordinado a** | [FND-01](../foundation/01-constituicao.md) · [FND-04](../foundation/04-governanca.md) · [FND-07](../foundation/07-framework-decisoes.md) · [FND-09](../foundation/09-meta-model.md) · [FND-10](../foundation/10-artifact-framework.md) |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| **Propoe / autor** | **DEP-GOV** | Materia de **forma e conformidade** — DEP-GOV §5, autonomia **A2**; FND-07 §2.4, linha *materia de veto (conformidade)* |
| **Revisa** | **DEP-QAR** | **DEP-GOV `I-1`** — nao revisa o que produz (RM-06b, ADR-0005, LV-03) |
| **Aprova** | **DEP-EXE** | FND-04 §2, C2; FND-07 §2.4, *C2 · Tipo 2*. **DEP-GOV nao aprova o que propos** (PI-05) |
| **Verifica aptidao** | **DEP-QAR** | CV-07, CC-04, QG-6 — [FIT-2026-014](../governance/fitness/FIT-2026-014-regime-ministerial-e-cobertura-de-contexto.md) |
| **Ratifica** | **—** | C2 · Tipo 2 nao exige ratificacao (FND-04 §2.1, FND-07 §2.3) |

---

## 1. Contexto

O sexto ato soberano exigiu, em
[MSG-2026-0006 §IX](../memory/operacional/MSG-2026-0006-ato-soberano-aplicacao-integral.md),
que a prova de consumo por Specs identificasse *"sem interpretacao informal"* os titulares de
**dez** atos, entre eles **promulgacao** e **ativacao**.

A aplicacao foi integral e provada:
[PT-2026-005](../governance/relatorio-transicao-2026-07-29-aplicacao.md) resolveu **55 de 55
celulas** sobre as fontes vigentes, com **0 indeterminadas** e **0 autoverificacoes**. Mas
**10 celulas — as linhas *Promulga* e *Ativa* — responderam por regra e nao por titular**, e
por isso a **condicao 6 de §X** falhou e **`GO-TO-SPECS` nao foi autorizado**.

**Estado do mundo antes desta decisao:** dez objetos em vigor; fila do Soberano zerada;
**sete das oito condicoes** de §X satisfeitas; **uma lacuna nomeada** — `RD-22` —, com
severidade Alta, dono DEP-GOV e gatilho *"antes de nova tentativa de `GO-TO-SPECS`"*.
**Pela primeira vez em cinco missoes, o bloqueio nao era ausencia de ato soberano.**

## 2. Problema / Pergunta de decisao

**`Promulgar` e `ativar` sao decisoes discricionarias, que exigem titular declarado em matriz
de autoridade, ou operacoes ministeriais decorrentes de aprovacao ou ratificacao valida?**

Uma unica pergunta. Dela decorre tudo o mais: se sao decisoes, falta titular e o instrumento e
C3; se sao execucao, o titular e o executor, e ele **ja esta nomeado**.

## 3. Criterios de decisao

Declarados **antes** de examinar as alternativas.

| # | Criterio | Peso | Por que |
|---|---|---|---|
| K1 | **Nao criar autoridade** — nenhum nome fora das fontes anteriores | **Alto** | `AU-03`, `AU-09`, `AU-10`, `LM-03`; e a linha vermelha que `RD-22` corretamente se recusou a cruzar |
| K2 | **Determinismo** — toda celula resolvida por fonte citada por identificador | **Alto** | Exigencia literal de §IX: *"sem interpretacao informal"* |
| K3 | **Menor instrumento competente** | **Alto** | Diretriz da missao; FND-09 §11.2 *gradacao de instrumento* |
| K4 | **Separacao de papeis preservada** — decisor ≠ executor ≠ verificador ≠ registrador | **Alto** | FND-04 §3.1, PI-05, LV-03, CV-08, `LM-05` |
| K5 | **O Soberano nao vira operador tecnico recorrente** | Medio | Exigencia expressa da missao; `PI-06` protege o inverso, nao isto |
| K6 | **Nenhuma segunda fonte de verdade** | Medio | `PJ-01`, `MM-01`, `CC-05` |
| K7 | **Reversibilidade** | Medio | GV-03, `RB-01` |

## 4. Alternativas consideradas

### Alternativa A — **Declarar a natureza ministerial e nomear o executor por remissao** *(escolhida)*

Regras `PA-*` **dentro do ADR**, na forma de `IR-01` a `IR-12` de ADR-0012 e de `FT-10` a
`FT-14` de ADR-0015. Matriz como **projecao declarada** (`PJ-02`).

| | |
|---|---|
| **A favor** | Satisfaz K1 a K7. **Zero** arquivos de `foundation/` tocados. Zero titulares novos. Reversivel por superacao |
| **Contra** | As regras vivem em artefato **M1**: a matriz nao se emenda, superа-se. Aceito — e o mesmo regime de `IR-*` e `FT-*` |
| Custo | Um ADR, uma RFC, um `FIT` |

### Alternativa B — Emendar **FND-09 §8.1** para acrescentar os verbos `promulgar` e `ativar`

| | |
|---|---|
| **A favor** | Poria os dois atos na matriz de §8.2, onde `RD-22` os procurou |
| **Contra** | **Amplia o universo fechado de verbos de autoridade de cinco para sete** — `C3`, exige ato soberano, e **transforma execucao em autoridade**, que e o oposto do que a evidencia sustenta. Viola K1 e K3 |
| Custo | RFC C3 + ADR C3 + pacote soberano + ato; e cria autoridade que hoje nao existe |

### Alternativa C — Emendar **FND-04 §4** acrescentando coluna de titular a cada etapa

| | |
|---|---|
| **A favor** | Poria o titular no ciclo, onde ele opera |
| **Contra** | **Ja esta la**: `[7]` diz *"DEP-GOV atribui ID definitivo, publica ADR, atualiza indices"*. A emenda **reescreveria o que o texto ja declara** — duplicacao proibida por `CC-05` e `PJ-01`. Viola K3 e K6 |
| Custo | Emenda a fundacional, com `H-N` alterado, exigindo ato soberano |

### Alternativa D — Registrar a leitura em **Nota de Decisao** (C1)

| | |
|---|---|
| **A favor** | Instrumento ainda menor |
| **Contra** | **Vedado pelo proprio template.** [TPL-nota-decisao](../foundation/templates/TPL-nota-decisao.md) §Escopo: *"**Nao se aplica** a decisao que cria precedente (DR-5), que afeta mais de um departamento (DR-3) ou que seja Tipo 1 — nesses casos, use ADR"*. Esta decisao **cria precedente** e alcanca **GOV, QAR, KMS e EXE**. Viola K3 por incompetencia do instrumento |
| Custo | Nulo — e invalido |

### Alternativa E — Levar a duvida ao **SOBERANO** como pergunta aberta

| | |
|---|---|
| **A favor** | Preserva integralmente K1 |
| **Contra** | Devolve ao Soberano uma pergunta que **a fonte vigente responde em vinte declaracoes**, e viola K5 no proprio ato de proteger K1: transformaria cada promulgacao futura em consulta. `EC-01` manda escalar **na duvida** — e depois de RFC-0016 §2.3 **nao ha duvida a escalar** |
| Custo | Uma missao inteira por ato de publicacao |

### Alternativa Z — **Nao fazer nada**

| | |
|---|---|
| **A favor** | Custo zero imediato; `RD-22` permanece registrado com dono e gatilho |
| **Contra** | `GO-TO-SPECS` fica bloqueado **por tempo indeterminado**, e o bloqueio nao tem caminho: nao e falta de ato, e falta de leitura. Toda promulgacao futura reabre a mesma duvida. Viola K2 e K5 |
| Custo | O Specification Framework nao comeca |

**Tradeoff aceito (VD-04):** as regras `PA-*` vivem em artefato **M1** e por isso **nao se
emendam** — corrigi-las exige um ADR sucessor. Aceita-se a rigidez em troca de **nao tocar
nenhuma fonte fundacional**, que e o custo que B e C imporiam.

## 5. Decisao

### 5.1 As regras — `PA-01` a `PA-14`

| # | Regra |
|---|---|
| **PA-01** | **Promulgar e ativar sao operacoes ministeriais.** Nenhuma das duas tem autoridade decisoria propria: ambas **executam** a autoridade ja exercida na aprovacao (FND-04 §2) ou na ratificacao (FND-10 §5.4). Fundamento literal: **`AU-06`** — *"Instrumento autoriza; nao executa (...) quem o cria e o executor nomeado"*. |
| **PA-02** | **Nenhum verbo de autoridade e criado.** Os verbos permanecem **cinco** (FND-09 §8.1: Criar, Alterar, Aprovar, Consumir, Aposentar). Nenhuma celula, linha ou coluna de **FND-09 §8.2** e alterada. **`AU-09` continua integral** — autoridade nao declarada nao existe —, e nao alcanca promulgar nem ativar, porque **nenhum dos dois e autoridade**. |
| **PA-03** | **Promulgacao e a etapa `[7]` de FND-04 §4 e `[10]` de FND-07 §5. Titular: `DEP-GOV`.** Consiste em: confirmar o identificador, **publicar o texto autorizado**, atualizar indices e contadores, e registrar `H-A`, `H-N`, `H-P` e o diff (`IR-07`, `IR-08`, `G-10`). |
| **PA-04** | **Promulgacao publica exatamente o conteudo autorizado.** O promulgador **nao altera** diff, escopo, versao, terminador de linha nem campo algum fora da lista fechada de **`IR-03`**. Alteracao fora do autorizado e **`IR-05`** — alteracao nao ratificada — e abre incidente de conformidade; **nao e corrigivel por edicao**. |
| **PA-05** | **Falha de hash impede a promulgacao do objeto afetado, isoladamente.** `H-A` que nao reproduza o valor autorizado, ou `H-P` que nao reproduza o projetado, **bloqueia aquele objeto** e exige registro. **Nenhuma divergencia e corrigida silenciosamente** (`IR-05`, `BL-04`). |
| **PA-06** | **Ativacao e a operacao `O4`** (FND-10 §5.2), e seu instrumento e **publicacao + atualizacao de indice** (FND-09 §7.5). **Emenda a artefato `M2` que ja esta `ativo` nao executa `O4`:** o estado nao transita, e quem transita e o `ADR` que a autoriza. |
| **PA-07** | **Executor ministerial e quem o instrumento autorizador nomear** (`AU-06`). **Nao havendo nomeacao, executa o custodiante declarado do artefato** — `DEP-GOV` para `FND`, `ADR`, `RFC`, `EXC`, `INC`, `TPL`, Cartas e indices (`G-1` a `G-11`, DEP-GOV §7); `DEP-KMS` para registros de memoria (FND-02 §3). **O executor nunca acumula, na mesma mudanca, papel incompativel** (FND-04 §3.1). |
| **PA-08** | **Verificacao e sempre de `DEP-QAR`, e nunca de quem promulgou ou ativou.** Fundamento: FND-04 §3 e §4 `[9]`, `CV-08`, **`IR-09`** e **DEP-GOV `I-7`** — *quem registra o ato nao pode ser a unica prova de que o registro esta integro*. |
| **PA-09** | **Registro e duplo e de papeis distintos:** `DEP-GOV` registra o ato, os tres hashes e o diff (`G-10`, `IR-07`, `IR-08`); `DEP-KMS` grava na camada de memoria correta (FND-04 §4 `[12]`, QG-5, `CV-05`). **Registrador ≠ executor** (`LM-05`, `CV-09`). |
| **PA-10** | **A ordem e obrigatoria:** aprovacao ou ratificacao → **promulgacao** → **ativacao** → verificacao → registro em memoria. Para **C2 e C3** o registro precede a execucao (**`CV-02`**). **Ativacao sem promulgacao registrada e transicao silenciosa, e transicao silenciosa e nula** (`LC-01`, GV-01). |
| **PA-11** | **Ausencia de ato:** sem ato explicito e datado **sobre o texto final**, nao ha o que promulgar; o artefato permanece **`aprovado`** e declara **`ratificacao: pendente`** (`LM-02`, `CV-09`). **Instrucao generica anterior, determinacao originadora, precedente e silencio nao suprem** (`LM-03`), e **ressalva nao neutraliza condicao de validade** (`LM-06`). |
| **PA-12** | **Impedimento tem cascata deterministica.** Simples: substitui o papel declarado na Carta do impedido. Duplo: substitui o substituto; **esgotada a cadeia declarada, o terminus e o `SOBERANO`** (`AU-10`, `EC-01`). **Impedimento transfere execucao, nunca autoridade decisoria** — quem substitui o executor nao passa a decidir merito. |
| **PA-13** | **O `SOBERANO` nao e executor ministerial.** Ele aparece em **duas** posicoes, ambas decisorias: **ratificacao** de C3 e de Tipo 1 (`AU-05`, indelegavel) e **terminus de impedimento duplo** (`AU-10`). **Nenhuma regra deste ADR o poe a publicar, indexar, medir hash, atualizar catalogo ou emitir baseline.** |
| **PA-14** | **Rollback e superacao.** Rollback de promulgacao ou de ativacao e **transicao registrada, com responsavel e data** (`RB-01`); nunca reversao silenciosa. Artefato que esteve em `ativo` **nunca volta** a `rascunho` (`RB-02`): corrige-se **superando** (`O6`). **Este ADR e superavel por ADR que o referencie** (`CC-06`, FND-07 §7); ele **nao se emenda** (`AC-10`, `CC-01`). |

### 5.2 A matriz de regime operacional — **projecao declarada**

> **Declaracao de projecao (`PJ-02`).**
> **Fonte:** FND-01 §6.2 · FND-02 §4.2 · FND-04 §2, §3 e §4 · FND-07 §2.4 e §5 · FND-09 §7.5,
> §8.2, `AU-06`, `LC-01` · FND-10 §5.2, §5.4, §6.1, `LM-05` · ADR-0012 `IR-05` a `IR-09` ·
> Cartas de DEP-GOV, DEP-QAR, DEP-KMS e DEP-EXE.
> **Campos projetados:** apenas o **par ato × papel** e a condicao de eficacia.
> **Finalidade:** responder, em uma leitura, quem decide, quem executa, quem verifica e quem
> registra — a exigencia literal de §IX do ato, que um indice de ponteiros nao satisfaz.
> **Metodo de atualizacao:** pela mesma mudanca que altera a fonte (`CV-04`), por **ADR
> sucessor** (`PA-14`). **Em divergencia prevalece a fonte** (`PJ-03`).

| Ato | Autoridade decisoria | Executor ministerial | Verificador | Registrador | Condicao | Evidencia | Estado resultante |
|---|---|---|---|---|---|---|---|
| **Propor** | conforme entidade | — | — | DEP-GOV | Classe validada por DEP-GOV | Instrumento da classe | `rascunho` |
| **Escrever** | proprietario | autor designado | — | — | Pre-condicoes do tipo (FND-04 §6) | Artefato com contrato L1 | `rascunho` |
| **Revisar** | — | — | **revisor ≠ autor** | DEP-GOV | `AC-03`, `RM-06b` | Parecer independente | `em-revisao` |
| **Liberar `QG-1`** | **DEP-EXE** | — | DEP-EXE | DEP-GOV | Resultado, criterio de aceite e fora-de-escopo presentes | Portao registrado com responsavel | `em-revisao` |
| **Aprovar** | **conforme classe** *(FND-04 §2)* | — | DEP-QAR | DEP-GOV | Revisao concluida; vetos sanados | Data + aprovador no frontmatter | `aprovado` |
| **Vetar** | **DEP-QAR** · **DEP-GOV** | — | — | DEP-GOV | Norma citada por identificador | ALERTA fundamentado | ciclo volta a `[2]` |
| **Ratificar** | **SOBERANO** *(se C3 ou Tipo 1)* | — | DEP-QAR *(`IR-09`)* | DEP-GOV *(`G-10`)* | Ato explicito e datado **sobre o texto final** | `MSG` canonica + `H-A`, `H-N`, `H-P`, diff | `aprovado` → apto a `ativo` |
| **Promulgar** | **nenhuma — decorre do ato** | **DEP-GOV** *(FND-04 §4 `[7]`; FND-07 §5 `[10]`)* | **DEP-QAR** | **DEP-GOV** | `H-A` reproduz o autorizado; diff literal; escopo intocado | Texto publicado + indices + tres hashes | conteudo **em vigor** |
| **Ativar** | **nenhuma — decorre do ato** | **nomeado no ato**; supletivamente o **custodiante** *(`PA-07`)* | **DEP-QAR** *(`IR-09`)* | **DEP-GOV** + **DEP-KMS** | Condicao de `LM-02` satisfeita; `H-P` reproduz o projetado | `O4` registrada com responsavel e data | **`ativo`** |
| **Superar** | conforme classe | autor do sucessor | DEP-QAR | DEP-GOV | Sucessor `ativo`; **todos** os dependentes migrados (`LC-05`) | `substitui` / `substituido_por` nos dois lados (`LN-02`) | `superado` |
| **Registrar** | — | DEP-GOV | DEP-QAR | **DEP-KMS** *(memoria)* | `QG-5`; camada correta | Entrada em `memory/` + catalogo | mudanca **encerrada** |

**Onze atos. Duas celulas de autoridade decisoria declaradamente vazias — e vazias por
norma, nao por omissao.** As outras nove nomeiam titular ja declarado.

### 5.3 O regime testado — **doze casos**

| # | Caso | Resposta pela matriz | Deterministico? |
|---|---|---|---|
| **T-01** | **C0 · Tipo 2** — correcao editorial | Decide o proprietario; executa o proprietario; **nao ha promulgacao autonoma**: registro e `atualizado_em` + CORRECAO. `O4` nao ocorre | ✅ |
| **T-02** | **C1 · Tipo 2** | Decide proprietario + revisor; executa o executor da nota; registra DEP-GOV; memoria OPR por DEP-KMS. Sem ratificacao | ✅ |
| **T-03** | **C2 · Tipo 2** | Decide **DEP-EXE** com parecer DEP-GOV; **promulga DEP-GOV** `[7]`; executa o nomeado `[8]`; verifica DEP-QAR `[9]`; `FIT` obrigatorio `[11]`; memoria `[12]`. **Registro precede execucao** (`CV-02`) | ✅ |
| **T-04** | **C2 · Tipo 1** | Idem, **mais ratificacao do SOBERANO** antes da promulgacao (`AU-05`, FND-07 §2.3). Sem o ato: `aprovado` + `pendente` (`PA-11`) | ✅ |
| **T-05** | **C3 · Tipo 1** | RFC obrigatoria → ADR → **ratificacao indelegavel** → promulgacao por DEP-GOV → `O4` → `IR-09` por DEP-QAR → memoria. Plano de reversao explicito exigido | ✅ |
| **T-06** | **`O4` sobre `ADR` ratificado** | Transicao do **par** `status` + `ratificacao`, com `H-N` invariante (`IR-02`) e `H-P` conferido. Executa o nomeado; verifica DEP-QAR; registra DEP-GOV | ✅ **provado 6 de 6 em MSG-2026-0006 §2** |
| **T-07** | **Promulgacao de fundacional** | **Nao executa `O4`** (`PA-06`): o `FND` e `M2` e ja esta `ativo`; quem transita e o `ADR`. `H-P` = `H-A` | ✅ |
| **T-08** | **Impedimento simples** — DEP-GOV promulgaria e verificaria | **`I-7`**: DEP-QAR executa `IR-09`, DEP-GOV confere de forma independente | ✅ |
| **T-09** | **Impedimento duplo** — executor e verificador impedidos | Cascata declarada nas Cartas → esgotada, **SOBERANO** (`PA-12`, `AU-10`, `EC-01`). **Terminus literal, com custo declarado** | ✅ **com custo** |
| **T-10** | **Falha de hash** | `PA-05`: bloqueia **somente** o objeto afetado; abre registro; `IR-05` se a divergencia for de `H-N`. **Nunca correcao silenciosa** | ✅ |
| **T-11** | **Ausencia de ato** | `PA-11`: permanece `aprovado`, `ratificacao: pendente`. Precedente, silencio e determinacao originadora **nao suprem** | ✅ |
| **T-12** | **Rollback e superacao** | `PA-14`: rollback e transicao registrada (`RB-01`); `ativo` nao volta a `rascunho` (`RB-02`); corrige-se por `O6` com dependentes migrados (`LC-05`) | ✅ |

**Doze de doze deterministicos.** Nenhum caso exige interpretacao; todos resolvem por regra
citada por identificador.

### 5.4 O que esta decisao **nao** faz

| Nao faz | Fundamento |
|---|---|
| **Nao** cria entidade, arquetipo, papel, departamento, portao ou verbo de autoridade | `PA-02`; FND-09 §11.1; FND-01 §6.2 |
| **Nao** altera FND-01 §7.3, FND-02 §4, FND-09 §8.2 nem FND-04 §2 | Nenhum arquivo de `foundation/` e tocado |
| **Nao** amplia a autoridade de DEP-GOV | `AU-03`; todos os nomes ja constavam — RFC-0016 §5 |
| **Nao** transforma parecer em decisao | `FT-10`, `FT-11` de ADR-0015 |
| **Nao** dispensa ratificacao onde a classe a exige | `PA-11`; `AU-05`; `LM-02` |
| **Nao** fecha `RD-23`, `RD-24`, `RD-26`, `RD-27` nem `RD-10` | RFC-0016 §6 |

## 6. Justificativa

**Porque a evidencia e literal e convergente.** Vinte declaracoes em cinco fontes vigentes
distintas — FND-04, FND-07, FND-09, FND-10 e a Carta de DEP-GOV — dizem, cada uma a seu modo,
a mesma coisa: **o instrumento autoriza, o executor executa, o verificador confere e o
registrador registra**. `RD-22` nao encontrou o titular porque procurou em **FND-09 §8.2**,
que distribui **autoridade**, e promulgar nao e autoridade — **§8.1 fecha a lista em cinco
verbos**, e nenhum deles e promulgar ou ativar.

**Porque a alternativa oposta cria o que se quer evitar.** Declarar promulgar e ativar como
verbos de autoridade (Alternativa B) **amplia o universo fechado de §8.1** e transforma
execucao em direito de decisao. Seria criar autoridade para preencher a celula que `RD-22`
corretamente se recusou a preencher por inferencia.

**Porque `FND-07 §5 [13]` e a prova mais forte, e ela e uma ausencia deliberada.** O ciclo da
decisao tem catorze etapas, e treze delas nomeiam quem age. A decima terceira diz apenas
***"VIGENCIA — decisao passa a valer e vincula"***. **Nao ha ator porque nao ha ato:** vigencia
e o **efeito** da aprovacao registrada. `CD-05` fecha o raciocinio — *"decisao vigente vincula
todos, inclusive quem discordou"* —: nao sobra discricionariedade a exercer depois.

**Porque isto protege o Soberano em vez de expo-lo.** Sem o regime declarado, cada publicacao
futura devolve a mesma duvida a mesa dele. Com o regime declarado, ele decide **merito** e e
**terminus de excecao** — e nada mais (`PA-13`, K5).

## 7. Impacto

| Dimensao | Impacto |
|---|---|
| **Departamentos afetados** | **DEP-GOV** *(promulga, registra, indexa — nada novo)* · **DEP-QAR** *(verifica — nada novo)* · **DEP-KMS** *(memoria — nada novo)* · **DEP-EXE** *(aprova esta decisao)*. **Nenhum ganha responsabilidade que nao tivesse** |
| **Componentes afetados** | **Nenhum.** Nenhum componente e criado, alterado ou removido |
| **Camadas de memoria a atualizar** | **APR** — [MEM-APR-0005](../memory/aprendizado/MEM-APR-0005-medir-a-ausencia-na-fonte-errada.md) · **OPR** — [PT-2026-006](../governance/relatorio-transicao-2026-07-29-fechamento-operacional.md) |
| **Decisoes superadas** | **Nenhuma.** Complementa ADR-0012, ADR-0015 e ADR-0019 sem supera-los |
| **Documentos a atualizar** | [`decisions/README`](README.md) · [`rfcs/README`](../rfcs/README.md) · [`governance/fitness/README`](../governance/fitness/README.md) · [`governance/README`](../governance/README.md) · [catalogo mestre](../governance/artifact-registry.md) · [`README` raiz](../README.md) — **todos `M3`, cascata `CV-04`** |
| **Custo e dependencia criados** | **Custo de contexto: 1 artefato `sob-demanda`.** Nenhuma dependencia externa. Nenhuma ferramenta nova (`CE-02`) |
| **Ganho de PI-14** | **Organizacao** — 10 celulas antes resolvidas por regra passam a nomear titular declarado. **Reducao de contexto** — a matriz responde em uma leitura o que exigia cinco fontes |

## 8. Evidencias

| # | Evidencia | Fonte | Confianca | Uso |
|---|---|---|---|---|
| **E1** | Os verbos de autoridade sao **cinco**, e `promulgar`/`ativar` **nao** estao entre eles | FND-09 §8.1, medido na fonte vigente | **Alta — medida** | Afasta `AU-09` |
| **E2** | *"Instrumento autoriza; nao executa (...) quem o cria e o executor nomeado"* | FND-09 `AU-06`, literal | **Alta — literal** | Fundamento de `PA-01` |
| **E3** | *"REGISTRO — DEP-GOV atribui ID definitivo, publica ADR, atualiza indices e contadores"* | FND-04 §4 `[7]`, literal | **Alta — literal** | Titular da promulgacao |
| **E4** | *"REGISTRO — DEP-GOV atribui numero e publica o ADR"* | FND-07 §5 `[10]`, literal | **Alta — literal** | Segunda fonte, mesmo titular |
| **E5** | *"VIGENCIA — decisao passa a valer e vincula"* — **etapa sem ator** | FND-07 §5 `[13]`, literal | **Alta — literal** | Ativacao e efeito, nao ato |
| **E6** | *"Entra em vigor · `ativo` · **Publicacao + atualizacao de indice**"* | FND-09 §7.5, literal | **Alta — literal** | Instrumento operacional da ativacao |
| **E7** | Papeis **Executor**, **Guardiao**, **Verificador**, **Curador**, **Ratificador**, com o que cada um **nao pode** | FND-04 §3, literal | **Alta — literal** | Separacao de `PA-07` a `PA-09` |
| **E8** | *"Para C2 e C3, o registro (7) precede a execucao (8)"* | FND-04 `CV-02`, literal | **Alta — literal** | Ordem de `PA-10` |
| **E9** | `O4` com **criterio verificavel** e rollback; ratificacao como **condicao de validade** | FND-10 §5.2 e §5.4 | **Alta — literal** | Ausencia de discricionariedade |
| **E10** | *"Quem registra a ratificacao e papel distinto de quem executou a mudanca"* | FND-10 `LM-05`, `CV-09` | **Alta — literal** | `PA-09` |
| **E11** | DEP-GOV **registra, nunca emite**; e **nao** executa `IR-09` sobre o que registrou | DEP-GOV §7 e `I-7` | **Alta — literal** | `PA-08` |
| **E12** | Os **seis** atos soberanos ja aplicados foram **promulgados por DEP-GOV e verificados por DEP-QAR** — `IR-09` reproduziu `H-A` em **6 de 6** | MSG-2026-0001 a 0006; PT-2026-005 §2 | **Alta — medida** | **Coerencia da pratica com a norma. Nao e fundamento** — `LM-03`: precedente nao ratifica |
| **E13** | Precedente de **forma** para C2 · Tipo 2 instituindo regras dentro do ADR | `ADR-0012` (`IR-01` a `IR-12`) · `ADR-0015` (`FT-10` a `FT-14`) | **Alta — medida** | Classe e forma do instrumento |
| **A1** | **Evidencia ausente, declarada:** nenhum caso de **impedimento duplo real** ocorreu no acervo. `T-09` e **determinado, nao observado** | `PI-10`, `LV-12` | — | Limite declarado |
| **A2** | **Evidencia ausente, declarada:** nenhum **rollback real** de promulgacao ocorreu. `T-12` e determinado, nao observado | `PI-10` | — | Limite declarado |

## 9. Riscos e mitigacao

| # | Risco | Prob. | Impacto | Mitigacao |
|---|---|---|---|---|
| RA-1 | **O ministerial virar discricionario na pratica** — executor "interpretando" o diff | Media | **Alto** | `PA-04` e `PA-05`: publica-se **exatamente** o autorizado, conferido por hash; divergencia e `IR-05`, nao correcao |
| RA-2 | **A matriz de §5.2 virar segunda fonte de verdade** | Media | Medio | Declarada `PJ-02` com as quatro informacoes; `PJ-03` da precedencia a fonte; `PA-14` obriga ADR sucessor |
| RA-3 | **Concentracao em DEP-GOV** — promulga, registra, indexa e cataloga | **Observada — familia `RC-02`, 6a ocorrencia** | **Alto** | `PA-08` e `I-7`: verificacao sempre de DEP-QAR. **Residuo declarado, nao resolvido**; so desaparece com agentes (`IC-3`) |
| RA-4 | **A classe C2 ser contestada** | Media | Medio | RFC-0016 §8 aplica o teste de FND-04 §2 item a item; superacao e barata (`PA-14`) |
| RA-5 | `PA-07` supletiva ser lida como **titular novo** | Media | **Alto** | `PA-07` remete a custodia **ja declarada** (`G-1` a `G-11`, FND-02 §3); nao cria custodia. **Declarado como o unico ponto em que a fonte exigiu regra supletiva** |
| RA-6 | Regras `PA-*` em `M1` envelhecerem sem via de correcao | Baixa | Medio | `PA-14` + `CC-06`: erro material gera **novo artefato**, com registro APR |

## 10. Plano de reversao

**Tipo 2 — reversao barata e conhecida.**

| Passo | Acao | Responsavel |
|---|---|---|
| 1 | ADR sucessor que **supere** este, declarando o que passa a valer (`SU-04`, `O6`) | qualquer DEP; aprova DEP-EXE |
| 2 | `status: superado` + `superado_por` neste ADR; `substitui`/`substituido_por` nos dois lados (`LN-02`) | DEP-GOV |
| 3 | Remover a matriz de §5.2 da cadeia de consumo; **nenhum artefato migra**, porque nenhum depende dela para existir | DEP-GOV |
| 4 | Verificar que nenhuma decisao tomada sob `PA-*` perdeu fundamento — cada uma cita **tambem** a fonte original | DEP-QAR |

**Custo medido da reversao: 1 ADR novo + 6 indices `M3`.** Nenhum artefato normativo e
alterado, porque **nenhum foi alterado para instituir isto**.

## 11. Classificacao

| Campo | Valor |
|---|---|
| **Classe de mudanca** | **C2** — institui padrao de execucao; **nao** toca principio imutavel, linha vermelha, hierarquia normativa, direitos de decisao nem a Fundacao (teste item a item em RFC-0016 §8) |
| **Tipo de reversibilidade** | **2** — reversao barata e conhecida (§10) |
| **Decisor** | **DEP-EXE**, com parecer de DEP-GOV (FND-04 §2; FND-07 §2.4) |
| **Ratificador** | **—** *(C2 · Tipo 2 nao exige — FND-04 §2.1)* |
| Data da decisao | **2026-07-29** |
| Data de vigencia | **2026-07-29** |

> **Sobre a classificacao, com a duvida declarada.** `GV-03` manda tratar como **Tipo 1** o que
> nao se sabe classificar, e um dos indicadores de Tipo 1 e *"mudanca de norma"*. **Esta decisao
> nao muda norma: declara a que vigora**, e o teste dessa afirmacao e verificavel — **zero
> arquivos de `foundation/` alterados**, medido por `cmp`. Se o SOBERANO entender de outro modo,
> o caminho e `RFC → ADR C3 → ratificacao`, e RFC-0016 serve de peca instrutoria sem reescrita.
> **A escolha da classe permanece contestavel, e o registro diz isso em vez de esconder.**

## 12. Revisao

| Campo | Valor |
|---|---|
| **Gatilho de revisao** | **Primeiro caso real de impedimento duplo** *(`T-09`)*, **ou** primeiro **rollback real** de promulgacao *(`T-12`)*, **ou** a criacao do primeiro **agente**, que muda a materia de `RA-3` |
| **O que se mede** | Quantas vezes uma promulgacao ou ativacao exigiu consulta ao Soberano *(alvo: zero fora de `T-09`)*; quantos objetos foram bloqueados por `PA-05`; se `PA-07` supletiva foi invocada e com que resultado |
| **Data de reavaliacao** | **2027-01-28** |
| **Aprendizado registrado** | A varredura procurou o **termo** e nao a **funcao** — [MEM-APR-0005](../memory/aprendizado/MEM-APR-0005-medir-a-ausencia-na-fonte-errada.md). **Mesma causa de `RD-23`**, que procurou afirmacao em prosa e nao valor em frontmatter |

## 13. Rastreabilidade

| Campo | Conteudo |
|---|---|
| **Origem** | [RFC-0016](../rfcs/RFC-0016-regime-ministerial-de-promulgacao-e-ativacao.md) |
| **Achado que fecha** | **`RD-22`** — [PT-2026-005 §5.3](../governance/relatorio-transicao-2026-07-29-aplicacao.md) |
| **Ato que tornou o achado mensuravel** | [MSG-2026-0006 §IX](../memory/operacional/MSG-2026-0006-ato-soberano-aplicacao-integral.md), quinta exigencia |
| **Verificacao de aptidao** | [FIT-2026-014](../governance/fitness/FIT-2026-014-regime-ministerial-e-cobertura-de-contexto.md) |
| **Relatorio de aplicacao** | [PT-2026-006](../governance/relatorio-transicao-2026-07-29-fechamento-operacional.md) |
| **Complementa** | [ADR-0012](ADR-0012-integridade-do-ato-de-ratificacao.md) *(`IR-*`)* · [ADR-0015](ADR-0015-fitness-check-e-parecer-nao-decisao.md) *(`FT-*`)* · [ADR-0019](ADR-0019-aprovador-e-ratificador-de-spec.md) |
| **Fontes projetadas** | §5.2, declaracao `PJ-02` completa |

## Checklist de validade (FND-07 §4.1)

| # | Regra | Cumprida |
|---|---|---|
| VD-01 | ≥ 2 alternativas reais + "nao fazer nada" | ✅ **cinco** + Z |
| VD-02 | Criterios declarados antes da escolha | ✅ §3 precede §4 |
| VD-03 | Nenhuma alternativa de palha | ✅ B, C, D e E tem defensor identificavel; **D e recusada pelo proprio template**, nao por conveniencia |
| VD-04 | Tradeoff aceito explicito | ✅ fim de §4 — rigidez de `M1` |
| VD-05 | Evidencia ausente declarada | ✅ **A1** e **A2** |
| VD-06 | Plano de reversao obrigatorio em Tipo 1 | ✅ apresentado ainda sendo **Tipo 2** (§10) |
| VD-07 | Impacto em cascata mapeado | ✅ §7, seis indices `M3` |
| VD-08 | Data e responsavel presentes | ✅ §11 |
| VD-09 | Gatilho de revisao definido | ✅ §12 |

---

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-GOV | Decisao **C2 · Tipo 2** que fecha **`RD-22`**: **promulgar e ativar sao operacoes ministeriais**, sem autoridade decisoria propria, decorrentes de aprovacao ou ratificacao valida. Institui **`PA-01` a `PA-14`** **dentro do proprio ADR**, na forma de `ADR-0012` e `ADR-0015`, e a **matriz de regime operacional** de §5.2 como **projecao declarada** (`PJ-02`) de treze secoes de cinco fontes. **Zero arquivos de `foundation/` alterados**; **zero verbos de autoridade criados** — §8.1 permanece com cinco; **zero titulares ampliados**, verificado nome a nome em RFC-0016 §5. Demonstra que **`AU-09` nao alcanca os dois atos** porque nenhum deles e autoridade, e que **`AU-06`** e a regra que responde. A prova mais forte e uma **ausencia deliberada**: `FND-07 §5 [13]` — *"VIGENCIA: decisao passa a valer e vincula"* — e a **unica das catorze etapas sem ator**, porque vigencia e **efeito**, nao ato. **Regime testado em doze casos** — C0 a C3 × Tipo 1/2, `O4`, promulgacao de fundacional, impedimento simples e duplo, falha de hash, ausencia de ato, rollback e superacao —, **12 de 12 deterministicos**, com **`T-09` e `T-12` declarados como determinados e nao observados** (`PI-10`). Classe **contestavel e declarada como tal**: se o SOBERANO entender que e C3, o caminho e RFC → ADR C3 → ratificacao. **`RA-3` registra a sexta ocorrencia da familia `RC-02`** — concentracao em DEP-GOV — como **residuo declarado, nao resolvido**. |
