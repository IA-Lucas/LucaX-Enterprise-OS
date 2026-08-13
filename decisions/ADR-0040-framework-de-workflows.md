---
id: ADR-0040-framework-de-workflows
titulo: Framework de Workflows — institui WF-01 a WF-30, recebendo a entidade, o template, o Pacote de Contexto e os portoes sem criar nada novo
tipo: adr
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-08-13
atualizado_em: 2026-08-13
revisao_prevista: 2027-02-13
decisoes_relacionadas: [ADR-0021, ADR-0033, ADR-0037]
substitui: []
substituido_por: null
classe_mudanca: C2
tipo_decisao: 2
supera: []
superado_por: null
resumo: Institui o Framework de Workflows - WF-01 a WF-30 - dentro do proprio ADR, pelo metodo de ADR-0033, aprovado pelo decimo terceiro ato como primeiro da ordem 1.16-1.14-1.17-1.18. Recebe a entidade WFL, o TPL-workflow, o Pacote de Contexto e os portoes QG-0..QG-6 sem criar entidade, tipo, template, papel ou portao. A contribuicao propria e estreita e medida - WF-19 a WF-25, a lacuna de retry, timeout, compensacao e retomada que segue com 0 ocorrencias no acervo normativo, remedida na admissao. 23 de 30 regras sao recepcao. C2 Tipo 2, 0 atos - WFL nunca exige ratificacao.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# ADR-0040: O Framework de Workflows

## Contexto

O **decimo terceiro ato** ([MSG-2026-0013](../memory/operacional/MSG-2026-0013-despacho-frameworks-e-fila.md))
aprovou os quatro Frameworks candidatos, e **1.16 e o primeiro da ordem despachada**. O
candidato — `WF-01` a `WF-30`, redigido pela Missao 1.14 em 2026-08-02, **fora do acervo** —
entra por este ADR pelo metodo de `ADR-0033`: **o Framework vive DENTRO do ADR**.

## Recepcao do candidato — conferida e REMEDIDA na admissao *(a licao: candidato chega vencido)*

| Verificacao | Resultado em 2026-08-13 |
|---|---|
| **`H-A` do candidato** | `881d9abfac60c11570562427a30663ff6c7da21e73ddf285de245ece85a3dc60` *(249 linhas, medido na admissao)* |
| **A lacuna que motiva `WF-19`–`WF-25`** | **SEGURA:** `retry`, `timeout`, `compensacao` e `retomada` com **`0`** arquivos em `foundation/` **hoje** — remedido, nao herdado |
| **Controles positivos** | vivos: `escalonamento` **7** arquivos · `impedimento` **8** *(o candidato media **9** e **9** em 2026-08-02 — divergencia de metodo/data DECLARADA, e o que importa se preserva: zero de lacuna com controle vivo nao e zero de instrumento morto)* |
| **`workflows/`** | segue **inexistente** *(achado `AW-1` confirmado)* |
| **`TPL-workflow` frontmatter** | segue `aprovador: SOBERANO` contra a matriz *(achado `AW-3` confirmado)* |
| **`L5` do candidato — ENVELHECEU A FAVOR** | dizia *"`0` Skills existem"* e *"a ordem da Sequencia nao esta decidida"* — hoje **`3` Skills existem** *(`ADR-0034`–`0036`)* e **a ordem FOI decidida** pelo 13º ato. A divergencia registrada de `L5` esta **RESOLVIDA pelos fatos** |

## Decisao

**Instituir `WF-01` a `WF-30` como o Framework de Workflows do acervo**, com o texto do
candidato transcrito abaixo como corpo normativo — **`0` entidades, tipos, templates,
papeis, portoes ou verbos criados** *(§13, `N1`–`N9`)*. Classe **`C2 · Tipo 2`, `0` atos**:
`WFL` e, junto com `SKL`, o componente que **nunca** exige ratificacao *(`FND-09 §8.2`)*.

---

## 2. O que um Workflow e, e o que nao e — `WF-01` a `WF-04`

| # | Regra |
|---|---|
| **WF-01** | **Um `Workflow` e sequencia definida de etapas com responsavel por etapa e portao, para resultado RECORRENTE.** Fundamento: `FND-03 §3.10`. **O teste de recorrencia e anterior a tudo:** trabalho que ocorre uma vez e **missao ou projeto**, nao Workflow. `FND-04 §6` linha *Workflow* exige *"gatilho, entradas, saidas, responsavel por etapa, portoes e criterio de falha definidos"* — **seis, e todos na criacao**. |
| **WF-02** | **Workflow nao e `Skill`, e a fronteira e o numero de papeis.** `SKL` e procedimento de **um** papel; `WFL` **atravessa papeis** ou **tem portao**. Fundamento: `FND-10 §4.8`, linha *Playbook* — *"`SKL` se um papel; `WFL` se atravessa papeis ou tem portao"*. **Procedimento de um papel e sem portao que seja escrito como Workflow e devolvido** e vira `SKL`. |
| **WF-03** | **O Workflow nao cria autoridade, nao cria portao e nao se aprova.** Nenhum Workflow institui papel, classe ou titular; nenhum e seu proprio aprovador ou verificador (`LV-03`, `AC-03`). **Os portoes que um Workflow declara sao os `QG-0` a `QG-6` de `FND-01 §6.2`, e nenhum outro** — o campo `portoes` do template os **referencia**, e criar portao proprio e `FND-01 §6.2` violado. **Portao nao pode ser liberado por quem produziu o artefato**, e essa regra vale dentro do Workflow como fora dele. |
| **WF-04** | **Etapa que apenas transporta, sem transformar, e candidata a remocao.** Fundamento literal, ja vigente e ja impresso no template: `HO-05`. **Toda etapa declara o que TRANSFORMA**; etapa cuja saida e igual a entrada e **custo de handoff sem ganho**, e o Workflow que a contem responde a quarta pergunta de `FND-04 §6.1` na proxima revisao. |

## 3. Workflow Contract — `WF-05` a `WF-08`

> **Declaracao de projecao (`PJ-02`).** **Fonte:** `FND-03 §4` · `FND-03 §3.10` · `FND-10 §2.2`,
> `§2.5` · `FND-09 §8.2` linha `WFL` · `FND-04 §6` linha *Workflow* · `FND-05 §5` ·
> `FND-01 §6.2`. **Campos projetados:** apenas **quais blocos o Workflow deve conter**.
> **Em divergencia prevalece a fonte** (`PJ-03`).

| # | Regra |
|---|---|
| **WF-05** | **O contrato do Workflow e o contrato universal do artefato, mais `gatilho` e `portoes`, e nenhum campo novo.** Os **15** campos de `FND-03 §4`, os **5** de `FND-10 §2.2` e os **2** proprios do template — `gatilho`, `portoes` — sao obrigatorios. **Ausencia = nao conforme = veto de DEP-GOV** (`AC-06`). **Nenhum campo novo e criado por este Framework** (`AC-07`). |
| **WF-06** | **O Workflow declara o DONO DO RESULTADO FINAL sempre que atravessar departamentos.** Fundamento literal: `FND-03 §3.10`, regra do tipo, e `FND-02 §6`. **Workflow interdepartamental sem dono unico do resultado e devolvido** — sem ele, nenhuma etapa responde pelo todo e o escalonamento de `WF-26` nao tem destinatario. |
| **WF-07** | **O Workflow declara escopo negativo — a que ele NAO se aplica — em bloco proprio e obrigatorio.** O template ja reserva a linha *"**Nao** se aplica a"*, e deixa-la vazia e **defeito**, nao estilo (`PI-09`, ampliacao silenciosa proibida). **O silencio nao estende o Workflow a caso novo:** caso nao previsto **para o Workflow**, e a parada e o comportamento correto, nao a falha. |
| **WF-08** | **Todo bloco do template vigente e obrigatorio, e a este Framework acrescem os SETE que a §1 mediu como lacuna:** estados e transicoes (`WF-10`), Pacote de Contexto do handoff (`WF-18`), retry (`WF-20`), timeout (`WF-21`), compensacao (`WF-23`), retomada (`WF-25`) e ponto de intervencao humana (`WF-28`). **Onze mais sete: dezoito blocos.** **Nenhum dos sete inventa conceito** — cinco preenchem lacuna medida e dois recebem fonte vigente. |

## 4. Autoridade e ciclo — `WF-09`

| # | Regra |
|---|---|
| **WF-09** | **A autoridade sobre um Workflow e derivada, nunca declarada no artefato.** E funcao de: **(a) a classe do efeito** (`AL-01`, com **`C2` como piso de criacao** por `FND-04 §6`); **(b) o tipo de reversibilidade** (`FND-04 §2.2`); **(c) o dono do resultado** (`FND-02 §6`); **(d) os portoes que ele atravessa**. **Workflow que fixe aprovador em texto e nao conforme** — o defeito de `RD-23`. **Ratificacao nao se exige nunca** (`FND-09 §8.2` linha `WFL`), **e um Workflow nao adquire exigencia de ato por atravessar materia que a tenha:** quem exige ato e a materia, no seu proprio rito — `WF-29`. |

## 5. Estados e transicoes — `WF-10` a `WF-12`

| # | Regra |
|---|---|
| **WF-10** | **Os estados de EXECUCAO de um Workflow sao seis, e nenhum e novo no acervo como conceito de artefato:** `nao-iniciado` · `em-curso` · `bloqueado` *(impedimento declarado)* · `em-espera-humana` *(`WF-28`)* · `concluido` · `abandonado` *(criterio de falha atingido)*. **Estes NAO sao os oito estados de artefato de `FND-03 §5`, e confundi-los e erro:** aqueles descrevem o **documento** do Workflow *(rascunho, ativo, superado…)*; estes descrevem uma **execucao** dele. **Um Workflow `ativo` pode ter execucoes em qualquer dos seis.** |
| **WF-11** | **Toda transicao declara o que a dispara e quem a observa.** Transicao sem gatilho escrito e mudanca de estado por criterio nao auditavel, e o acervo exige rastreabilidade **sem consultar pessoa** (`LN-07`). **Transicao para `bloqueado` declara o impedimento**; para `abandonado`, o criterio de falha de `FND-04 §6` que foi atingido. **Nao ha transicao silenciosa de `em-curso` para `concluido`:** a conclusao passa pelo criterio de conclusao do template. |
| **WF-12** | **`bloqueado` e `em-espera-humana` sao estados DISTINTOS e nao se colapsam.** `bloqueado` e impedimento — falta algo, e o sistema nao pode prosseguir sozinho. `em-espera-humana` e ponto de decisao — o sistema **pode** prosseguir tecnicamente e **nao deve** sem juizo humano. **Tratar decisao humana como impedimento produz escalonamento indevido; tratar impedimento como espera produz espera infinita.** Os dois tem relogio proprio (`WF-21`). |

## 6. Portoes e impedimentos — `WF-13` a `WF-15`

| # | Regra |
|---|---|
| **WF-13** | **Portao e ponto obrigatorio de parada, e passar um portao e ATO REGISTRADO com responsavel nomeado.** Fundamento literal: `FND-01 §6.2`. **Portao pulado e registrado como excecao formal, nunca omitido** — e a omissao e incidente de conformidade, nao atraso. |
| **WF-14** | **Portao nao pode ser liberado por quem produziu o artefato**, e o Workflow declara, por portao, **quem libera** — nome de papel, nunca de pessoa. Fundamento: `FND-01 §6.2`, regra de portao. **Workflow cuja tabela de portoes ponha o mesmo papel como produtor e liberador e nulo naquele portao** (`LV-03`), e o defeito e da **estrutura**, nao da execucao. |
| **WF-15** | **Impedimento e declarado com dono e prazo, ou nao e impedimento.** Impedimento sem dono nao e resolvido por ninguem; sem prazo, nao dispara escalonamento (`WF-26`). **Impedimento registrado tres vezes na mesma etapa e sinal observado de defeito estrutural do Workflow**, e obriga revisao — nao mais uma resolucao pontual. |

## 7. Handoff e Pacote de Contexto — `WF-16` a `WF-18`

| # | Regra |
|---|---|
| **WF-16** | **Todo handoff declara o que transfere e o criterio de aceite de quem recebe.** O template ja reserva o bloco; este Framework torna o **criterio de aceite** obrigatorio: **handoff sem criterio de aceite nao e transferencia, e abandono com testemunha.** As regras `HO-01` a `HO-05` de `FND-05` sao **recebidas integralmente** e nao alteradas. |
| **WF-17** | **Quem recebe pode RECUSAR o handoff, e a recusa e registrada com motivo.** Handoff que nao pode ser recusado torna o criterio de aceite decorativo. **Recusa nao e falha do Workflow:** e o portao funcionando — a mesma leitura que o acervo aplica ao portao de raiz do `baseline.sh`, cuja **recusa e o portao funcionando, nao falha**. |
| **WF-18** | **O contexto transferido no handoff segue o Pacote de Contexto, e nao o volume disponivel.** Fundamento: `FND-05 §5`, com `AG-05` — *"contexto entregue a agente segue o Pacote de Contexto: nucleo curto, suporte por referencia"* — e `RC-01` de `FND-06`, que exige **contexto minimo suficiente**. **Transferir tudo o que se tem nao e handoff cuidadoso: e transferir o custo de curadoria para quem recebe**, e viola `CE-01`. **O que vai por referencia vai por identificador**, nunca por copia. |

## 8. Falha, retry e timeout — `WF-19` a `WF-22`

> **As quatro regras desta secao e as tres da §9 sao a contribuicao propria deste
> Framework.** `retry`, `timeout`, `compensacao` e `retomada` tem **`0`** ocorrencias no
> acervo normativo — medido em §1, com controle positivo.

| # | Regra |
|---|---|
| **WF-19** | **Criterio de falha e obrigatorio na criacao, e declara quatro campos por falha:** **como reconhecer** · **onde retorna** · **quem e acionado** · **o que ja foi produzido e o que se faz com isso**. Os tres primeiros ja estao no template; **o quarto e o que falta**, e e o que liga falha a `WF-23`. **Falha cujo efeito parcial nao foi declarado nao tem compensacao possivel.** |
| **WF-20** | **Retry e declarado com LIMITE e com criterio de elegibilidade, ou nao ocorre.** Toda etapa que admita repeticao declara: **quantas vezes** · **com que intervalo** · **sob que condicao a repeticao faz sentido**. **Retry sem limite e laco**, e laco nao e tolerancia a falha. **Nem toda falha e elegivel a retry:** repetir operacao **nao idempotente** produz efeito duplicado, e por isso **etapa com efeito externo declara se e idempotente** — se nao for, o caminho e `WF-23`, nunca retry. |
| **WF-21** | **Todo estado de espera tem relogio, e o relogio tem consequencia declarada.** `em-curso`, `bloqueado` e `em-espera-humana` declaram, cada um, **quanto tempo** antes de a espera virar evento. **Espera sem prazo e Workflow parado que ninguem sabe que parou** — e o acervo ja chama isso pelo nome: indicador sem valor nao prova nada (`LM-01`). **Timeout NAO e falha automaticamente:** ele dispara o que estiver declarado — escalonamento, retry, compensacao ou abandono —, e qual dos quatro **e escolha do autor, registrada na criacao**. |
| **WF-22** | **Falha *plausivel e errada* e natureza propria, e e a que se esquece.** Etapa que produz saida bem-formada e incorreta **nao dispara alarme nenhum** dos anteriores. **Toda etapa cuja saida alimente decisao declara como se detecta que ela esta errada**, por metodo de `SF-14`. **Ausencia dessa declaracao e incompletude declarada, nunca ausencia de risco** — a mesma regra que `SF-25` impoe a `Spec`. |

## 9. Compensacao, rollback e retomada — `WF-23` a `WF-25`

| # | Regra |
|---|---|
| **WF-23** | **Compensacao e como se desfaz o efeito de uma etapa JA CONCLUIDA, e ela e distinta de rollback.** **Rollback** devolve o sistema a um ponto anterior *(`RB-01`: com responsavel e custo)*. **Compensacao** aplica-se quando o efeito **nao pode ser devolvido** — ele ja saiu para fora, e o que se faz e **um ato novo que o neutraliza**. **Toda etapa com efeito EXTERNO declara sua compensacao, ou declara, por escrito, que nao tem** — e *"nao tem compensacao"* e informacao valiosa e legitima: ela diz que aquela etapa e um **ponto sem volta**, e pontos sem volta merecem portao antes, nunca depois. |
| **WF-24** | **Rollback de Workflow declara ate ONDE volta, e o que acontece com o que ja foi entregue a terceiros.** Fundamento: `RB-01`, e `RB-02` — o que esteve `ativo` nao volta a `rascunho`. **Rollback que ignore entrega ja feita nao e rollback: e apagar o registro de que ela ocorreu**, e isso e `LV-12`. |
| **WF-25** | **Retomada exige ponto de retomada DECLARADO ANTES, e ela e a regra que o acervo aprendeu por dano proprio.** Todo Workflow declara **de onde** uma execucao interrompida recomeca, **o que precisa estar preservado** para que isso seja possivel, e **quem verifica que esta**. **Ponto de retomada declarado e nao preservado e pior que nenhum**: cria confianca que o fato nao sustenta. **O acervo tem o precedente medido e ele custou caro** — `RD-103`, severidade **Alta**: um ponto de retorno declarado foi **destruido** porque a listagem exibida ao operador era de primeiro nivel e ele **confirmou sem poder ver** que o ponto estava dentro. **Declarar nao preserva. Verificar preserva.** |

## 10. Escalonamento, incidente, intervencao humana e ato soberano — `WF-26` a `WF-28`

| # | Regra |
|---|---|
| **WF-26** | **Escalonamento e declarado por DEGRAU, com destinatario nomeado por papel e condicao objetiva.** *"Escalar se necessario"* e nulo — nao diz a quem nem quando. **O destinatario final de todo degrau e o dono do resultado** (`WF-06`), e por isso Workflow sem dono do resultado nao pode escalonar. |
| **WF-27** | **Incidente detectado ABRE `INC`, e a abertura e obrigatoria — nao discricionaria.** Fundamento: `FND-09 §8.2` linha `INC`, coluna *Propoe*: ***"quem detecta (obrigatorio)"***. **Workflow nao decide se abre incidente**; ele declara **o que conta como incidente naquele Workflow**, e a abertura segue a norma. **Falha tratada por retry ou compensacao com sucesso continua sendo falha ocorrida**, e a decisao de registrar nao e do executor. |
| **WF-28** | **Intervencao humana e ponto DECLARADO na estrutura, nunca recurso de emergencia.** O Workflow declara, por ponto: **o que se decide ali**, **quem decide** *(papel)*, **o que a pessoa precisa ter em maos** *(Pacote de Contexto — `WF-18`)* e **o que acontece se ela nao responder** *(`WF-21`)*. **Tres casos exigem ponto de intervencao e nao admitem automacao:** **(a)** exposicao de dado a terceiro (`EX-03`, `LV-08`); **(b)** portao `QG-4` — *"antes de expor ao mundo"* —, que `FND-01 §6.2` ja atribui a **DEP-QAR + Soberano**; **(c)** qualquer efeito cuja classe seja **`Tipo 1`**. **Onde a norma exige ATO DO SOBERANO, o Workflow PARA e nao prossegue** — ele nao pode conte-lo, executa-lo nem antecipa-lo. **Workflow que siga adiante sem o ato produz efeito nulo** (`LM-02`), e o efeito nulo nao se conserta executando de novo. |

## 11. Evidencia e memoria — `WF-29`

| # | Regra |
|---|---|
| **WF-29** | **O Workflow declara o que cada etapa GRAVA e em que camada, e a evidencia e declarada antes, nunca escolhida depois.** O template ja reserva o bloco de memoria por etapa; este Framework acrescenta que **a evidencia de conclusao de cada portao e nomeada na criacao** — que artefato, valor ou observacao contara como prova, e quem a produz (`SF-15` aplicado por analogia de metodo, `LV-12`). **`QG-5` — *"o aprendizado foi extraido e gravado na memoria?"* — e portao de `FND-01 §6.2` e nao e opcional**; Workflow que nao alimente memoria nao o atravessa. |

## 12. Mudanca, descontinuacao e registro — `WF-30`

| # | Regra |
|---|---|
| **WF-30** | **`WFL` e `M2`** (`FND-10 §6.2`). **A versao segue o efeito** (`AL-01`): **MAIOR** quando muda portao, dono do resultado, criterio de falha ou ponto de intervencao; **MENOR** quando se acrescenta etapa sem alterar as anteriores; **CORRECAO** quando nada normativo muda. **Alteracao silenciosa e nula** (`AC-11`, `GV-01`). **Criterio de descontinuacao e obrigatorio** e o template ja o exige, remetendo a consolidacao de `FND-02 §9.3`. **Registro mestre:** o catalogo mestre e o **contador oficial** da sequencia `WFL`; **criar Workflow e incrementar o contador sao a mesma mudanca** (`CV-04`, `IX-02`). **Nenhum registro novo e criado** — seria proliferacao (`FND-04 §6.1`, `RG-05`). **Este Framework e `M2`, `C2 · Tipo 2`: emenda-se por versao e NAO exige ato.** |

## 13. O que este Framework NAO faz

| # | Nao faz | Verificacao |
|---|---|---|
| **N1** | **Nao cria entidade.** `WFL` ja existe | `FND-03 §3.10`, `FND-09 §8.2` — `0` linhas acrescentadas |
| **N2** | **Nao cria portao.** Os portoes sao `QG-0` a `QG-6` | `FND-01 §6.2` — **7 antes, 7 depois**; `GO-TO-*`: **2 antes, 2 depois** |
| **N3** | **Nao cria tipo, template, diretorio, papel nem verbo de autoridade** | `FND-09 §11.1`; `MT-01`, `CS-01` |
| **N4** | **Nao altera a matriz de `FND-09 §8.2`** | `0` celulas. `WF-09` **remete**, nao decide |
| **N5** | **Nao cria os estados de execucao como estados de ARTEFATO** | `WF-10` os separa dos **8** de `FND-03 §5` expressamente |
| **N6** | **Nao redefine handoff nem Pacote de Contexto** | `HO-01` a `HO-05` e `FND-05 §5` **recebidos**, `0` bytes |
| **N7** | **Nao cria `WFL`, nao cria `workflows/`, nao orquestra nada** | **`0`** Workflows · `workflows/` **inexistente** |
| **N8** | **Nao promove a si mesmo a `FND`** | Promover e `C3 · Tipo 1` com ato — o custo de `ADR-0022` |
| **N9** | **Nao autoriza Workflow a substituir ato do Soberano** | `WF-28` **para** o Workflow onde a norma exige ato |

## 14. Recepcao × contribuicao — medido

| Origem | Quantas regras | Quais |
|---|---|---|
| **Recebidas** de fonte vigente | **23** | `WF-01` a `WF-18`, `WF-26` a `WF-30` |
| **Contribuicao propria** — lacuna medida em §1 | **7** | `WF-19` a `WF-25` |

**Vinte e tres de trinta sao recepcao.** O Framework que mais acrescenta e o que menos
inventa, e a proporcao esta declarada para que a revisao futura possa contesta-la.

## 15. Limites declarados — **determinado, nao observado**

| # | Limite | Fundamento |
|---|---|---|
| **L1** | **Nenhum `Workflow` real existe.** As **30** regras sao determinadas, nao observadas. `FND-03 §3.10`: *"Nao existe nesta fase"* | Medido 2026-08-02; forma de `L1` de `FND-11 §14` |
| **L2** | **`WF-08` institui 18 blocos sem custo medido.** `CE-04` proibe estimar; o valor sera medido no primeiro Workflow | `CE-04` |
| **L3** | **Nenhum retry, timeout, compensacao ou retomada real ocorreu.** `WF-19` a `WF-25` — **a contribuicao propria e a parte MENOS testada** | `PI-10` |
| **L4** | **`WF-22` — falha *plausivel e errada* — nao tem instancia observada** | `PI-10` |
| **L5** | **A ordem da Sequencia nao esta decidida**, e `WFL` depende de `SKL` para ter o que orquestrar: **`0` Skills existem** | Primeira DIVERGENCIA REGISTRADA, aberta |

## 16. Achados que este candidato ABRE

| # | Achado | Severidade | Dono | Gatilho |
|---|---|---|---|---|
| **AW-1** | **`workflows/` nao existe no disco**, embora `FND-03 §7` **ja o declare** na estrutura canonica *"(fase futura)"* e `FND-03 §3.10` diga *"Nao existe nesta fase"*. **O obstaculo NAO e o diretorio** — e `LV-06`: ***"criar agente, produto, workflow ou ferramenta sem Carta aprovada"***. **Para o Workflow, o proprio documento `WFL` e a Carta**, e ele e aprovado por **DEP-EXE em `C2`, sem ato** — de modo que este obstaculo, aqui, **e o mais barato do acervo** | **Baixa** | `DEP-EXE` | Primeiro Workflow |
| **AW-2** | **`TPL-workflow` nao tem bloco de retry, timeout, compensacao nem retomada** — os quatro com `0` ocorrencias no acervo. Um Workflow criado pelo template vigente **nasce sem declarar o que fazer quando falha repetidamente ou e interrompido** | **Media** | `DEP-GOV + DEP-EXE` *(dono do tipo `TPL`)* | Primeiro Workflow |
| **AW-3** | **`TPL-workflow` poe `aprovador: SOBERANO` no frontmatter do TEMPLATE**, enquanto `FND-09 §8.2` linha `WFL` poe **`DEP-EXE`** em *Aprova* e **`—`** em *Ratifica*. O esqueleto interno poe corretamente `aprovador: DEP-EXE`. **A divergencia e entre o template-documento e o template-esqueleto**, e so o segundo rege o artefato gerado | **Baixa** | `DEP-GOV` | Proxima emenda de `TPL-workflow` |

## 17. Rastreabilidade e revisao

| Campo | Conteudo |
|---|---|
| **Origem da entidade** | `FND-03 §3.10` · `FND-09 §8.2` linha `WFL` — **recebidas** |
| **Fontes recebidas e nao alteradas** | `FND-01 §6.2` *(portoes)* · `FND-02 §6`, `§9.3` · `FND-05 §5` e `HO-01`–`HO-05` · `FND-06 RC-01` · `FND-04 §6` · `TPL-workflow` |
| **Metodo** | O de `ADR-0021`: contrato em ADR `C2 · Tipo 2`, **sem emendar fonte alguma** |
| **Gatilho de revisao** | O **primeiro Workflow real** (`L1`); **ou** o primeiro retry, timeout, compensacao ou retomada reais (`L3`); **ou** a primeira falha *plausivel e errada* (`L4`) |
| **O que se mede na revisao** | Quantos Workflows foram devolvidos, e por qual regra; quantas vezes `WF-17` foi exercido *(handoff recusado)*; quantas vezes `WF-28` **parou** um Workflow por exigir ato; se `WF-20` a `WF-25` foram usados ou ficaram decorativos |

---

## Rito e rastreabilidade da admissao

Cadeia: [RFC-0035](../rfcs/RFC-0035-framework-de-workflows.md) → este ADR →
[FIT-2026-033](../governance/fitness/FIT-2026-033-framework-de-workflows.md). Os achados
`AW-1` a `AW-3` do candidato entram **abertos**, com os donos e gatilhos que ele declara.
**Gatilho de revisao** *(§17 do corpo)*: o primeiro Workflow real, ou o primeiro
retry/timeout/compensacao/retomada real, ou a primeira falha *plausivel e errada* — **o que
ocorrer primeiro**.
