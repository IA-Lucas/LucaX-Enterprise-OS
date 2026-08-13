---
id: ADR-0043-framework-de-execucao-e-avaliacao
titulo: Execution & Evaluation Framework — institui EA-01 a EA-28, distinguindo atividade de resultado com os quatro estados, sem criar o tipo Evaluation
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
decisoes_relacionadas: [ADR-0021, ADR-0033, ADR-0040, ADR-0041, ADR-0042]
substitui: []
substituido_por: null
classe_mudanca: C2
tipo_decisao: 2
supera: []
superado_por: null
resumo: Institui o Execution & Evaluation Framework - EA-01 a EA-28 - dentro do proprio ADR, quarto e ultimo rito do decimo terceiro ato, fechando o Bloco A inteiro. Distingue atividade de resultado pelos quatro estados (executado, verificado, aprovado, comprovado), com Golden Tests, scorecard, controle positivo e prova por reversao - a contribuicao propria concentrada exatamente onde a medicao achou zero, remedida na admissao. NAO cria o tipo Evaluation (recusa vigente de FND-10 §4.8, o achado AE-1 registra a unica recusa sem gatilho de reabertura). O conflito AE-3 (DEP-QAR autor e titular da materia) dispara na propria admissao e esta DECLARADO no FIT, nunca omitido. 21 de 28 regras sao recepcao.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# ADR-0043: O Execution & Evaluation Framework

## Contexto

Quarto e **ultimo** rito do Bloco A do **decimo terceiro ato** — com ele, **a ordem
despachada fecha inteira**: Skills ✅ *(pre-ato)* → 1.16 ✅ → 1.14 ✅ → 1.17 ✅ → **1.18**.
O acervo distingue atividade de resultado **na pratica** *(controle positivo, prova por
reversao, reproducao em duas execucoes)* e **nao na norma** — este Framework poe a pratica
em contrato, **sem criar o tipo `Evaluation`** *(recusa vigente de `FND-10 §4.8`, recebida)*.

## Recepcao do candidato — conferida e REMEDIDA na admissao (2026-08-13)

| Verificacao | Resultado |
|---|---|
| **`H-A` do candidato** | `5f8562e93d6d2985909035bf00e993010d47f8541b541a1a3b86a1e73c34013b` *(259 linhas)* |
| **Os zeros da contribuicao** | **SEGURAM:** `scorecard`, `golden` e `determinist*` com **`0`** arquivos em `foundation/` hoje — a contribuicao propria continua mirando exatamente onde nada existe |
| **`AE-2` — declarado × comprovado** | **CONFIRMA como assimetria:** hoje **18 arquivos** usam *declarado* e **5** usam *comprovado* *(o candidato media 27×5 por OCORRENCIAS em 2026-08-02; remedido por ARQUIVOS, metodo declarado)* — **e a diferenca segue sem definicao em norma**, que e o que o achado registra |
| **`AE-3` — o conflito de titularidade** | **O GATILHO E ESTA ADMISSAO**, e o conflito esta **DECLARADO** em `FIT-2026-036` com a mitigacao do proprio candidato: revisor `DEP-GOV`, aprovador `DEP-EXE`, **21 de 28 regras sao recepcao** |
| **`L2`** | **CONFIRMA:** `0` Golden Tests — `EA-20`–`EA-22` nascem como a parte menos testada, o mesmo padrao dos tres frameworks anteriores |

## Decisao

**Instituir `EA-01` a `EA-28` como o Execution & Evaluation Framework do acervo**, com o
corpo do candidato transcrito abaixo — **`0` entidades ou tipos criados** *(o tipo
`Evaluation` segue RECUSADO — `AE-1` registra que e a unica recusa sem gatilho de
reabertura, dono SOBERANO)*. Classe **`C2 · Tipo 2`, `0` atos**. Os **quatro estados do
resultado** — `executado` · `verificado` · `aprovado` · `comprovado` — **nao retroagem**
*(`EV-01`; `L3`)*: instancia ja aprovada nao se reclassifica.

---

## 1. Contexto — o acervo distingue os quatro estados na pratica e nao na norma

**A distincao que este Framework institui ja e EXERCIDA pelo acervo, e com rigor.** As
missoes 1.13.4.4 a 1.13.6 dizem, repetidamente, coisas como *"determinado, nao observado"*,
*"exercido, nao afirmado"*, *"medido por ferramenta, nunca de cabeca"* e *"controle positivo
antes de crer no zero"*. **Nenhuma dessas frases esta em norma vigente.** Sao pratica.

**Medido no acervo normativo *(`foundation/`)*, com controle positivo na mesma execucao:**

| Termo | Arquivos | Leitura |
|---|---|---|
| `declarado` | **27** | ✅ existe — **controle positivo** |
| `aceite` | **15** | ✅ existe — **controle positivo** |
| `executado` | **9** | ✅ existe |
| `comprovado` | **5** | ✅ existe, **e e o mais raro dos quatro** |
| `scorecard` | **0** | ❌ **lacuna** |
| `determinist*` | **0** | ❌ **lacuna** |
| `golden` | **0** no acervo normativo — **1** ocorrencia no acervo inteiro, **e ela esta no proprio roadmap** | ❌ **lacuna** |

**Os zeros sao reais:** a mesma varredura devolveu **27** e **15** para termos que tinham de
aparecer.

**A leitura que importa:** `declarado` aparece **27** vezes e `comprovado` **5**. **A norma
fala cinco vezes mais em declarar do que em comprovar** — e a diferenca entre os dois e
exatamente o que este Framework existe para fixar.

## 2. Onde a avaliacao vive — e por que `Evaluation` NAO e criado aqui

> **Esta secao decide a fronteira do Framework, e ela e a razao de ele nao custar ato.**

**`FND-10 §4.8` — tabela de tipos recusados — recusa `Evaluation` nestes termos:**

| Candidato | Por que nao e tipo | Onde vive | Gatilho de reabertura |
|---|---|---|---|
| **Evaluation** | *"Nome guarda-chuva de Fitness Check e Revisao Arquitetural"* | *Entidade `FIT`, dois tipos documentais* | **`—`** |

**O gatilho de reabertura e `—`, e essa e a unica linha da tabela sem caminho de volta
escrito.** As outras cinco recusas — `Norma Derivada`, `Command`, `Prompt`, `Playbook`,
`Checklist` — todas declaram a condicao que as reabriria. **`Evaluation`, nao.**

**Consequencia, e ela e dura:** criar `Evaluation` nao e caro — e **impossivel pelo caminho
ordinario**. Nao ha gatilho a satisfazer; so a superacao expressa de `FND-10`, que e
**`C3 · Tipo 1` com ato**. **Este Framework nao a tenta, e nao precisa.**

### 2.1 Mas `FIT` nao cobre tudo, e isso tambem esta medido

**`FIT` avalia *"a aptidao EVOLUTIVA de uma mudanca ESTRUTURAL"*** (`FND-03 §3.14`), com
portao `QG-6`, obrigatorio em `C2` e `C3`. **Ele nao avalia se o resultado de uma execucao
ficou bom.** Sao perguntas diferentes: `FIT` pergunta *"a arquitetura ficou mais apta a
evoluir?"*; a execucao pergunta *"isto que foi produzido atende ao que foi pedido?"*.

**A segunda pergunta JA TEM sede, e nao e um tipo novo — sao tres coisas que ja vigoram:**

| Pergunta | Sede vigente | Titular |
|---|---|---|
| O resultado atende ao pedido? | **`DoD`** de `FND-01 §6.1` + **`QG-3`** — *"atende o DoD e passou por revisao independente?"* | **DEP-QAR** |
| O requisito foi satisfeito? | **criterio de aceite** e **metodo de verificacao** da `Spec` — `SF-12`, `SF-14`, `SF-15` | quem a `Spec` nomear |
| A mudanca deixou a arquitetura melhor? | **`FIT`** — `QG-6` | **DEP-QAR** |

**A conclusao e o achado `AE-1`:** o acervo **nao precisa** de tipo `Evaluation`; ele precisa
que o **`DoD` e o `QG-3` sejam exercidos**, e hoje **nenhum dos dois tem contrato escrito
sobre o que conta como prova**. **Este Framework da esse contrato — e nao cria tipo algum.**

## 3. Os quatro estados do resultado — `EA-01` a `EA-05`

| # | Regra |
|---|---|
| **EA-01** | **Quatro estados, mutuamente exclusivos, e todo resultado esta em exatamente um:** **`EXECUTADO`** *(a atividade ocorreu — ha registro de que rodou)* · **`DECLARADO`** *(alguem afirma o resultado — ha alegacao, e ela tem autor)* · **`COMPROVADO`** *(ha evidencia que um terceiro verifica sem consultar o autor)* · **`APROVADO`** *(quem tem autoridade aceitou, pela classe)*. **A ordem e de precedencia, nao de tempo:** nenhum estado presume o anterior, e **cada um se declara**. |
| **EA-02** | **Executado nao implica declarado; declarado nao implica comprovado; comprovado nao implica aprovado.** **As tres implicacoes sao falsas e cada uma tem nome de falha:** presumir declaracao do que rodou e **omissao**; presumir prova da declaracao e **`LV-12`** *(evidencia fabricada)*; presumir aprovacao da prova e **`LV-03`** *(autoaprovacao)*. **Prova nao aprova: quem aprova e autoridade.** |
| **EA-03** | **A implicacao inversa tambem e falsa, e ela e a menos lembrada: APROVADO nao implica COMPROVADO.** Autoridade pode aprovar sob risco declarado, e isso e legitimo — mas o registro **nao pode dizer *comprovado*** quando o que houve foi decisao. **Confundir os dois converte juizo em fato**, e e a forma mais dificil de detectar depois, porque o documento parece completo. |
| **EA-04** | **Todo registro de resultado declara em QUE ESTADO ele esta, e o silencio le-se como `DECLARADO`.** A regra de leitura e deliberadamente conservadora — a mesma escolha de `WF-18`/`TF-18`: **na duvida, o estado mais fraco**. **Resultado sem estado declarado nao conta como prova em portao algum**, e usa-lo assim e falha de curadoria, nao formalidade. |
| **EA-05** | **`0` e resultado, e resultado com significado — mas so depois de CONTROLE POSITIVO.** **Zero de instrumento morto e indistinguivel de zero real.** Antes de qualquer `0` ser declarado `COMPROVADO`, mede-se, **com o mesmo instrumento e na mesma execucao**, um termo que **tem** de aparecer. **A regra tem precedente medido e caro:** na primeira Spec do acervo, a varredura de `LM-6(a)` devolveu `0` para tudo — **inclusive para o que existia** — por defeito de instrumento, e as contagens so foram tomadas apos o controle positivo *(`senha_hash`=11, `nxtrack`=527)*. **Sem controle positivo, o zero e `DECLARADO`, nunca `COMPROVADO`.** |

## 4. Registro de execucao — `EA-06` a `EA-08`

| # | Regra |
|---|---|
| **EA-06** | **Toda execucao registra, no minimo, cinco campos:** **o que foi executado** · **quando** · **por quem** *(papel)* · **com que entrada** · **o que saiu**. **Execucao sem registro nao e `EXECUTADO`: e nao verificavel**, e nao pode sustentar nenhum dos outros tres estados. |
| **EA-07** | **Execucao que nao ocorreu registra-se como NAO OCORRIDA, com motivo — nunca por omissao.** Etapa pulada, teste nao rodado, verificacao adiada: **o registro diz que nao houve**, e diz por que. **Silencio sobre o que nao se fez le-se como se tivesse sido feito**, e essa leitura e a que produz `DoD` falsamente completo. |
| **EA-08** | **O registro nomeia o INSTRUMENTO e permite reproducao.** Fundamento: `CE-04` *(proibido estimar)* e `SF-14` *(cinco metodos)*. **Numero sem instrumento e sem data nao e medicao** — e `LM-01`. **O instrumento e identificavel por versao ou `sha256` sempre que exista como arquivo**, porque instrumento alterado produz numero incomparavel: **e a licao de `IR-BL`, cujas versoes o acervo numera e cujo `sha256` publica.** |

## 5. Evidencia — `EA-09` a `EA-12`

| # | Regra |
|---|---|
| **EA-09** | **Evidencia e declarada ANTES, nunca escolhida depois.** Recebida de **`SF-15`**, que ja o exige da `Spec`: todo requisito diz **que artefato, valor ou observacao** contara como prova, **quem** a produz e **quando**. **Escolher a evidencia depois do resultado e selecionar o que confirma** — e o registro nao consegue distinguir isso de prova honesta. |
| **EA-10** | **Fabricar evidencia, fonte, citacao, metrica ou resultado e `LV-12`**, e alcanca quatro formas que parecem menores: **(a)** citar fonte que nao diz aquilo; **(b)** declarar `nao informado` como `nenhum`; **(c)** apresentar o resultado de um instrumento como se fosse de outro; **(d)** **declarar remediado sem reconferir**. **A quarta tem precedente proprio no acervo** — a regra de que apagar exige prova de byte nao-unico **antes e depois**. |
| **EA-11** | **Teste que so passa nao prova nada: exige-se que ele FALHE quando deveria.** **Toda verificacao nova e validada por reversao** — desfaz-se a correcao e exige-se vermelho. **Sem isso, o verde e indistinguivel de teste que nao testa**, e o acervo tem o caso medido: uma assercao de forma passava verde contra comando que o CLI recusava. **Reversao e a versao negativa do controle positivo de `EA-05`**, e as duas juntas fecham os dois lados. |
| **EA-12** | **A evidencia e verificavel por terceiro SEM CONSULTAR O AUTOR.** Recebida de `SF-12`, campo *criterio de aceite*. **Evidencia que exija o autor para ser interpretada nao e evidencia: e testemunho**, e testemunho nao atravessa portao — `QG-3` pede **revisao independente**. |

## 6. Verificacao deterministica e por modelo — `EA-13` a `EA-16`

| # | Regra |
|---|---|
| **EA-13** | **Duas naturezas de verificacao, e a escolha entre elas e declarada com motivo:** **`DETERMINISTICA`** *(mesmo insumo produz sempre o mesmo veredito; reproduzivel por qualquer um)* · **`POR JUIZO`** *(o veredito depende de avaliacao, humana ou por modelo)*. **As duas mapeiam nos cinco metodos de `SF-14` e nao criam metodo novo:** `TESTE`, `MEDICAO` e `ANALISE` sao tipicamente deterministicas; `INSPECAO` e `DEMONSTRACAO` admitem juizo. |
| **EA-14** | **Onde a verificacao deterministica for possivel, ela e OBRIGATORIA — juizo nao substitui medicao disponivel.** **Usar juizo onde havia instrumento e degradar a prova por conveniencia.** O teste e direto: *"existe metodo de `SF-14` que decida isto sem opiniao?"*. Se existe, e ele que vale. |
| **EA-15** | **Avaliacao POR MODELO e verificacao por juizo, e declara-se como tal — com o modelo, a versao e o prompt registrados.** **Ela nao e deterministica**, ainda que devolva numero: numero produzido por juizo continua sendo juizo. **O modelo que avalia e `TOL` de classe `modelo`** (`FND-03 §3.12`) e leva as regras do Framework de Ferramentas — inclusive `TF-13`, exposicao de dado, que **alcanca o dado enviado para ser avaliado**. |
| **EA-16** | **Nenhum modelo avalia a propria saida.** Derivada de `LN-06` *(verificacao reflexiva vedada)*, `LV-03` e `RM-06b`. **A proibicao e por PAPEL, nao por instancia** — a mesma leitura de `AR-18`: **a mesma familia de modelo, com o mesmo prompt, nao e avaliador independente**, ainda que seja outra chamada. **Autoavaliacao registra-se como `DECLARADO`, nunca como `COMPROVADO`.** |

## 7. Revisao humana e independencia — `EA-17` a `EA-19`

| # | Regra |
|---|---|
| **EA-17** | **Independencia e de PAPEL, e o revisor e ≠ autor.** Recebida de `AC-03`, `RM-06b` e `R-06` de `FND-09 §6.1`, que exclui de DEP-GOV a verificacao do que DEP-GOV produziu. **Portao nao pode ser liberado por quem produziu o artefato** (`FND-01 §6.2`). |
| **EA-18** | **Tres classes de resultado exigem juizo HUMANO e nao admitem automacao:** **(a)** exposicao de dado a terceiro (`EX-03`, `LV-08`); **(b)** o portao **`QG-4`** — *"antes de expor ao mundo"* —, que `FND-01 §6.2` ja atribui a **DEP-QAR + Soberano**; **(c)** todo efeito de classe **`Tipo 1`**. **Onde a norma exige ato do Soberano, nenhuma avaliacao o substitui** (`LM-02`) — a mesma regra que `WF-28` impoe ao Workflow. |
| **EA-19** | **O veredito e registrado com as tres saidas de `FIT` quando for `FIT`, e nunca reescrito.** Recebido de `FND-03 §3.14` e **`FT-09`**: `apto` · `apto-com-ressalva` · `inapto`; **`inapto` bloqueia o encerramento**; **veredito posterior SUPERA o anterior, e nao o apaga**. **Reescrever veredito e `LV-04`** — instrumento nao se edita apos eficacia. |

## 8. Golden Tests — `EA-20` a `EA-22`

> **`golden` tem `0` ocorrencias no acervo normativo**, e a unica do acervo inteiro esta no
> **proprio roadmap**, que os pede. **Esta secao e contribuicao propria integral.**

| # | Regra |
|---|---|
| **EA-20** | **Um `Golden Test` e par ENTRADA → SAIDA ESPERADA, fixado ANTES da implementacao e versionado com ela.** Ele nao descreve como se produz a saida — **so o que a saida deve ser**. **E `SF-01` aplicado a execucao:** *declara o que deve ser verdadeiro e por qual evidencia isso sera aceito*. **Golden Test escrito depois de ver a saida nao e golden: e a saida com outro nome**, e registra-se `DECLARADO`. |
| **EA-21** | **Alterar a saida esperada de um Golden Test e mudanca NORMATIVA e leva versao e motivo.** **Ajustar o esperado para caber no obtido e mover o alvo**, e o acervo ja nomeou essa falha ao exigir **inercia antes de emendar instrumento**: quatro provas antes do uso, *"senao alterar o medidor e mover o numero para caber"*. **A regra vale igual aqui**: o esperado muda quando **o requisito** muda, nunca quando o resultado desaponta. |
| **EA-22** | **O primeiro conjunto de Golden Tests cobre as QUATRO categorias de requisito de `SF-25`, ou declara a ausencia com motivo:** `FUNCIONAL` · `NAO FUNCIONAL` · **`NEGATIVO`** *(o que nao deve ocorrer)* · **`DE FALHA`** *(o que acontece quando o caminho feliz nao ocorre)*. **Conjunto so com casos funcionais esta incompleto**, e a incompletude **se declara**. **O caso negativo e o que raramente se escreve e o unico que testa limite.** |

## 9. Aceite e scorecard — `EA-23` a `EA-24`

| # | Regra |
|---|---|
| **EA-23** | **Aceite e ato de AUTORIDADE, pela classe, e registra-se com responsavel e data.** Recebido de `FND-04 §2` e `FND-01 §6.2`. **Aceite nao e consequencia automatica de teste verde:** verde e `COMPROVADO`; aceite e `APROVADO`, e sao estados distintos por `EA-01`. **Quem aceita declara o que esta aceitando** — inclusive ressalva e risco assumido. |
| **EA-24** | **`Scorecard` e VISAO DERIVADA, nunca fonte, e nao e artefato novo.** Ele agrega valores que ja existem em evidencia registrada. **Tres regras:** **(a)** cada celula aponta a evidencia de origem, por identificador; **(b)** **celula sem valor medido declara-se `definido, sem valor`** (`LM-01`), nunca `0` nem em branco; **(c)** **scorecard nao aprova nada** — ele informa quem aprova. **Scorecard que vire a fonte do numero e `PJ-03` violado:** em divergencia **prevalece a fonte**. |

## 10. Erro, incidente e rollback — `EA-25` a `EA-26`

| # | Regra |
|---|---|
| **EA-25** | **Erro detectado ABRE `INC`, e a abertura e obrigatoria — nao discricionaria.** Fundamento literal: `FND-09 §8.2` linha `INC`, coluna *Propoe* — ***"quem detecta (obrigatorio)"***. **Erro corrigido com sucesso continua sendo erro ocorrido**, e a decisao de registrar **nao e de quem o cometeu**. |
| **EA-26** | **Rollback declara responsavel e custo, e o que ja foi entregue a terceiros.** Recebido de `RB-01` e `RB-02` — o que esteve `ativo` nao volta a `rascunho`. **Rollback que apague o registro de que a entrega ocorreu nao e rollback: e `LV-12`.** **Ponto de retomada declarado e verificado, nunca so declarado** — `RD-103`, severidade **Alta**, e o precedente medido em que um ponto de retorno declarado foi destruido. |

## 11. Custo, tempo e reproducao — `EA-27`

| # | Regra |
|---|---|
| **EA-27** | **Custo, tokens e tempo sao MEDIDOS com instrumento e data, ou declarados `definido, sem valor`.** `CE-04` proibe estimar; `CE-02` exige custo medido no catalogo. **Reproducao e a prova mais forte disponivel e exige-se em duas execucoes independentes** para todo numero que sustente decisao — **e a pratica que o acervo ja exerce em toda baseline** *(sempre reproduzida em 2 execucoes)*, aqui **elevada de pratica a regra**. **Numero nao reproduzido registra-se `DECLARADO`.** |

## 12. Aprendizado e promocao para memoria — `EA-28`

| # | Regra |
|---|---|
| **EA-28** | **O portao `QG-5` — *"o aprendizado foi extraido e gravado na memoria?"* — nao e opcional**, e e liberado por **DEP-KMS** (`FND-01 §6.2`). **O que se grava e o que MUDA decisao futura**, nunca o relato do que aconteceu. **Promocao a camada `EST` tem aprovacao propria** — `DEP-GOV`, ratificacao do SOBERANO se `EST` (`FND-09 §8.2` linha `MEM`) — **e quem executou nao promove a propria licao**: seria `EA-16` por outra porta. **Hipotese invalidada NAO se apaga** (`MM-09`): ela fica marcada como invalidada, com o que a derrubou. |

## 13. O que este Framework NAO faz

| # | Nao faz | Verificacao |
|---|---|---|
| **N1** | **Nao cria o tipo `Evaluation`** | `FND-10 §4.8` — **recusado, gatilho `—`**. §2 mede |
| **N2** | **Nao cria entidade, tipo, template, diretorio, papel nem portao** | `FND-09 §11.1`; `MT-01`, `CS-01`. `QG`: **7 antes, 7 depois**; `GO-TO-*`: **2 antes, 2 depois** |
| **N3** | **Nao cria metodo de verificacao novo** | Os **5** de `SF-14` recebidos; `EA-13` apenas **classifica** os existentes em duas naturezas |
| **N4** | **Nao altera `FIT`, `FT-01`–`FT-15`, o `DoD` nem os portoes** | `0` bytes; todos **recebidos** |
| **N5** | **Nao altera a matriz de `FND-09 §8.2`** | `0` celulas |
| **N6** | **Nao executa, nao testa, nao mede sistema real, nao cria Golden Test** | **`0`** execucoes · **`0`** Golden Tests · **`0`** scorecards |
| **N7** | **Nao autoriza avaliacao a substituir ato do Soberano** | `EA-18` |
| **N8** | **Nao promove a si mesmo a `FND`** | `C3 · Tipo 1` com ato |

## 14. Recepcao × contribuicao — medido

| Origem | Quantas regras | Quais |
|---|---|---|
| **Recebidas** de fonte vigente | **21** | `EA-06` a `EA-19`, `EA-23`, `EA-25` a `EA-28` |
| **Contribuicao propria** | **7** | `EA-01` a `EA-05` *(os quatro estados)* · `EA-20` a `EA-22` *(Golden Tests)* · `EA-24` *(scorecard)* — **contadas como 7 porque `EA-05` recebe `CE-04` e so acrescenta o controle positivo** |

**Vinte e uma de vinte e oito sao recepcao.** **A contribuicao propria concentra-se
exatamente onde a medicao de §1 achou `0`:** `scorecard`, `determinist*` e `golden`.

## 15. Limites declarados — **determinado, nao observado**

| # | Limite | Fundamento |
|---|---|---|
| **L1** | **Nenhuma execucao real foi avaliada por estas regras.** As **28** sao determinadas, nao observadas | `PI-10` |
| **L2** | **`0` Golden Tests existem**, e `EA-20`–`EA-22` sao a parte **menos testada** — o mesmo padrao de `WF-19`–`WF-25` e `AR-16`–`AR-19` | Medido 2026-08-02 |
| **L3** | **`EA-01` distingue quatro estados que o acervo nunca declarou explicitamente em artefato algum.** Aplicar retroativamente **reclassificaria** afirmacoes ja publicadas — **e este Framework NAO retroage** | `EV-01`: *"entidade ou atributo novo nunca invalida instancia ja aprovada"* |
| **L4** | **A avaliacao de resultado de execucao nao tem, hoje, artefato proprio** — vive no `DoD`, no `QG-3` e no criterio de aceite da `Spec`. **`AE-1` registra que isso e suficiente**, e a afirmacao **nao foi testada contra caso real** | `AE-1` |
| **L5** | **DEP-QAR e autor e titular da materia** — conflito declarado em `AE-3`, familia de `RD-92` | `RD-92` |

## 16. Achados que este candidato ABRE

| # | Achado | Severidade | Dono | Gatilho |
|---|---|---|---|---|
| **AE-1** | **`Evaluation` e a UNICA das 6 recusas de `FND-10 §4.8` sem gatilho de reabertura** *(`—`)*. As outras cinco declaram a condicao que as reabriria. **Efeito:** avaliacao de resultado de execucao **nao tem caminho ordinario para virar tipo**, ainda que a necessidade apareca; so superacao expressa de `FND-10`, `C3 · Tipo 1` | **Media** | `SOBERANO` | Primeira necessidade real de avaliar execucao |
| **AE-2** | **A norma fala 27 vezes em *declarado* e 5 em *comprovado***, e **nao define a diferenca em lugar nenhum**. A pratica das missoes a exerce com rigor *(controle positivo, reproducao em 2 execucoes, prova por reversao)* — **e a pratica nao esta em norma** | **Media** | `DEP-QAR` | Primeira avaliacao de execucao real |
| **AE-3** | **DEP-QAR seria autor deste Framework E titular das regras que ele contrata** — mesma forma de `RD-92`. Mitigado por revisor `DEP-GOV`, aprovador `DEP-EXE` e por **21 de 28 regras serem recepcao**; **nao sanado** | **Baixa** | `DEP-GOV` | Admissao deste candidato |

## 17. Rastreabilidade e revisao

| Campo | Conteudo |
|---|---|
| **Fontes recebidas e nao alteradas** | `FND-01 §6.1`, `§6.2` · `FND-03 §3.14` · `FND-04 §2` · `FND-06` e `MM-09` · `FND-09 §6.1`, `§8.2`, `§10`, `§11.4` · `FND-10 §4.8`, `§6.2` · `FND-11` `SF-12`, `SF-14`, `SF-15`, `SF-25` · `FT-01`–`FT-15` |
| **Metodo** | O de `ADR-0021`: contrato em ADR `C2 · Tipo 2`, **sem emendar fonte alguma** |
| **Gatilho de revisao** | A **primeira execucao real avaliada** (`L1`); **ou** o primeiro Golden Test (`L2`); **ou** o primeiro caso em que `EA-03` — *aprovado sem comprovado* — for exercido |
| **O que se mede na revisao** | Quantos resultados foram registrados em cada um dos **4** estados; quantas vezes `EA-05` *(controle positivo)* mudou um veredito; quantas vezes `EA-11` *(prova por reversao)* reprovou um teste que passava; se `EA-24` impediu scorecard de virar fonte |

---

## Rito e rastreabilidade da admissao

Cadeia: [RFC-0038](../rfcs/RFC-0038-framework-de-execucao-e-avaliacao.md) → este ADR →
[FIT-2026-036](../governance/fitness/FIT-2026-036-framework-de-execucao-e-avaliacao.md).
Achados `AE-1`–`AE-3` **abertos** com dono *(`AE-3` exercido e declarado NESTA admissao)*.
**Gatilho de revisao:** a primeira execucao real avaliada, ou o primeiro Golden Test, ou o
primeiro `aprovado sem comprovado` exercido. **Com este ADR, o Bloco A do 13º ato esta
INTEIRO: os quatro Frameworks sao norma.**
