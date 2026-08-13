---
id: ADR-0042-framework-de-agentes
titulo: Agent Framework — institui AR-01 a AR-30, com a separacao de papeis enunciada para o agente pela primeira vez, sem criar agente algum
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
decisoes_relacionadas: [ADR-0021, ADR-0033, ADR-0040, ADR-0041]
substitui: []
substituido_por: null
classe_mudanca: C2
tipo_decisao: 2
supera: []
superado_por: null
resumo: Institui o Agent Framework - AR-01 a AR-30 - dentro do proprio ADR, terceiro rito do decimo terceiro ato. Recebe AGT e SUB, os niveis de autonomia e os arquetipos sem criar entidade, nivel, arquetipo, agente, subagente ou piloto - FND-02 §10 recebida INTACTA, nesta fase nao existem agentes e este Framework nao muda isso. A contribuicao propria e a regra central que faltava - AR-16 a AR-19, um agente nao escreve, revisa e aprova sozinho o mesmo objeto, enunciada para o agente pela primeira vez (quatro fontes existiam, nenhuma sobre agente - AA-3). 26 de 30 regras sao recepcao, a maior proporcao dos frameworks. Os dois pilotos contrastantes sao rito proprio futuro com Carta aprovada.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# ADR-0042: O Agent Framework

## Contexto

Terceiro rito do Bloco A do **decimo terceiro ato** *(1.16 ✅ → 1.14 ✅ → **1.17** → 1.18)*.
O Agente e **o componente mais especificado e menos existente do acervo** — e este Framework
da o contrato **sem criar instancia alguma**: `FND-02 §10` *("nesta fase nao existem
agentes")* e **recebida intacta**, e os **dois pilotos contrastantes** que o Goal desenha
*(um de execucao, um de guarda)* sao rito proprio futuro, com Carta aprovada *(`LV-06`)* —
e o de guarda com a restricao estrutural ja vigente: **Guarda nunca e coordenada por Linha**
*(`ES-02`/`IV-01`)*.

## Recepcao do candidato — conferida e REMEDIDA na admissao (2026-08-13)

| Verificacao | Resultado |
|---|---|
| **`H-A` do candidato** | `255ebd2550e6489f4b1b9c9dca0e70520521e51135f8c1222fa430042532cfe3` *(270 linhas)* |
| **`N7`/`AA-2`** | **CONFIRMAM:** `0` `AGT` · `0` `SUB` · `departments/*/agents/` inexistente nos 9 |
| **`AA-1` — a colisao `A1`/`A2`/`A3`** | **PERMANECE no nivel das familias** *(`FND-01 §7.2` niveis × `FND-09 §4` arquetipos)*, **MAS o agravante mudou**: o cartao `E-11` **hoje** traz o rotulo inline *("A1 ATOR", medido em 2026-08-13 — a emenda 1.6.0 de `FND-09` pos a chave dentro do cartao)*. O achado segue **aberto** com o agravante **atenuado, declarado** |
| **`L5` — a cadeia de componentes** | **ENVELHECEU PARCIALMENTE A FAVOR:** dizia *"0 Skills, 0 Ferramentas, 0 Workflows"* — hoje **3 Skills existem** e **`WFL`/`TOL` sao norma** *(`ADR-0040`/`0041`, do proprio dia)*; instancias de `TOL`/`WFL` seguem `0` |
| **`L3` — os pilotos** | **CONFIRMA:** nenhum criado, e o caminho esta declarado *(Carta aprovada, `C2`, com a restricao `ES-02` para o de guarda)* |

## Decisao

**Instituir `AR-01` a `AR-30` como o Agent Framework do acervo**, com o corpo do candidato
transcrito abaixo — **`0` entidades, niveis, arquetipos, agentes, subagentes ou pilotos
criados** *(§13, `N1`–`N9`)*; **`FND-02 §10` intacta**. Classe **`C2 · Tipo 2`, `0` atos**.
**A contribuicao propria e a regra central que o roadmap pedia e nenhuma fonte enunciava
para o agente** *(`AA-3`)*: `AR-16`–`AR-19` — **um agente nao escreve, revisa e aprova
sozinho o mesmo objeto com impacto relevante.**

---

## 2. A colisao de notacao, medida antes de qualquer regra

> **Medido em 2026-08-02, nas duas sedes, por leitura direta da tabela.**

**`A1`, `A2` e `A3` designam coisas diferentes em duas Fundacionais vigentes:**

| Notacao | `FND-01 §7.2` — **nivel de autonomia** | `FND-09 §4` — **arquetipo** |
|---|---|---|
| `A0` | Consultivo | *(nao existe)* |
| **`A1`** | **Executor supervisionado** | **ATOR** |
| **`A2`** | **Executor autonomo** | **ARTEFATO** |
| **`A3`** | **Delegado** | **COMPONENTE** |
| `A4` | *(nao existe — nenhum papel opera acima de `A3`)* | **INSTRUMENTO** |

**As duas familias tem quatro membros cada e colidem em tres.** Os intervalos sao `A0..A3`
e `A1..A4`.

**O agravante nao e a colisao em si: e que as duas aparecem no MESMO cartao.**
`FND-09 §E-11` traz, uma linha abaixo da outra:

- linha **Autoridade** — *"Igual ou inferior a do departamento… nunca opera acima do
  `nivel_autonomia_concedido`"*, remetendo a `FND-01 §7.2`;
- linha **Arquetipos** — ***"A1, A2, A3"***.

**Lidas juntas e sem a chave, as duas sugerem que o agente opera em nivel `A3`
— *Delegado*.** Nao e o que a ficha diz: *"A1, A2, A3"* ali significa **ATOR, ARTEFATO e
COMPONENTE**.

**A leitura errada e exatamente a que `LV-07` proibe** — *"ampliar o proprio nivel de
autonomia"* —, e ela seria alcancada **por engano de notacao, nao por ma-fe**. `AR-12`
fecha a porta; o achado fica aberto em §14, `AA-1`, porque **sanar a fonte nao e materia
deste Framework**.

## 3. O que um Agente e, e o que nao e — `AR-01` a `AR-04`

| # | Regra |
|---|---|
| **AR-01** | **Um `Agente` e PAPEL EXECUTOR ESPECIALIZADO, com Carta, escopo, nivel de autonomia e departamento de origem.** Fundamento: `FND-03 §3.3`. **Agente e papel, nunca pessoa e nunca modelo:** o modelo que o executa e `TOL` de classe `modelo` (`FND-03 §3.12`), e trocar o modelo **nao cria agente novo** nem altera a Carta. **Confundir papel com executor e o erro que faria cada troca de provedor virar mudanca organizacional.** |
| **AR-02** | **O papel no identificador e SUBSTANTIVO DE FUNCAO, nunca verbo.** Fundamento literal: `FND-03 §3.3` — *"`arquiteto`, nao `arquitetar`"*. **A regra nao e de estilo:** verbo nomeia **tarefa**, e tarefa nao tem Carta, autonomia nem ciclo de vida. **Agente nomeado por verbo e quase sempre uma `Skill` com nome errado**, e o teste de `AR-03` o revela. |
| **AR-03** | **Agente nao e `Skill`, `Workflow` nem `Ferramenta`, e o teste e de PERMANENCIA.** `SKL` e procedimento; `WFL` e sequencia; `TOL` e capacidade externa. **O agente PERSISTE entre invocacoes com identidade e responde por resultado** — e o arquetipo **ATOR** de `FND-09 §4`, que exige *"ser sujeito de relacao de autoridade, emitir e receber mensagem, e responder por resultado"*. **O que nao responde por resultado nao e agente**, ainda que execute. |
| **AR-04** | **Agente nao existe sem Carta aprovada, e a Carta e condicao, nao formalidade.** Fundamento literal: **`LV-06`** — *"criar agente, produto, workflow ou ferramenta **sem Carta aprovada**"* e violacao — e `PI-12`, herdado do arquetipo **COMPONENTE**. **Agente que apareca em uso sem Carta e nulo** (`MT-01`, `GV-01`), e seu uso e **incidente de conformidade**, nao improviso tolerado. |

## 4. Agent Contract — `AR-05` a `AR-08`

> **Declaracao de projecao (`PJ-02`).** **Fonte:** `FND-03 §4` · `FND-03 §3.3`, `§3.4` ·
> `FND-09 §E-11`, `§E-12` · `FND-10 §2.2`, `§2.5` · `FND-09 §8.2` linha `AGT` ·
> `FND-04 §6` linha *Agente* · `FND-01 §7.2` · `FND-08 §8`. **Campos projetados:** apenas
> **quais blocos a Carta deve conter**. **Em divergencia prevalece a fonte** (`PJ-03`).

| # | Regra |
|---|---|
| **AR-05** | **O contrato da Carta e o universal do artefato mais os quatro atributos minimos de `FND-09 §E-11`, e nenhum campo novo:** `departamento`, `nivel_autonomia`, `capabilities` e a secao ***"O que nao me compete"***. **Ausencia = nao conforme = veto de DEP-GOV** (`AC-06`). **Nenhum campo novo e criado por este Framework** (`AC-07`). |
| **AR-06** | **A secao *"O que NAO me compete"* tem forca IGUAL a do escopo positivo, e nao e apendice.** Fundamento literal: `FND-09 §E-11`, linha *Responsabilidade* — *"o escopo da propria Carta — **e, com igual forca, o que nao lhe compete**"*; e `FND-03 §3.3`, que a torna **obrigatoria** no template. **Carta com a secao vazia ou generica e devolvida.** **Cada item declara o que fazer no lugar** — a quem devolver, a quem escalar —, porque limite sem destino produz parada sem saida. |
| **AR-07** | **A Carta declara as `Capabilities` exercidas, no minimo uma, e no maximo tres sem justificar.** Fundamento: `FND-08 §8` e `R-02` de `FND-09 §6.1` — vinculo **obrigatorio, minimo 1, nunca vazio**; **`VC-03`**: *"vinculo a mais de tres Capabilities e sinal de componente amplo demais"*. **Capability inexistente, `proposta` ou `aposentada` e elo quebrado** (`VC-01`). **Agente com quatro ou mais Capabilities responde por escrito por que nao sao dois agentes.** |
| **AR-08** | **Os blocos obrigatorios da Carta sao os QUATORZE do template vigente, e este Framework nao acrescenta bloco algum.** `TPL-carta-agente` ja cobre missao, o que faco, o que nao me compete, entradas, saidas, contexto minimo, limites de autonomia, quando devolvo, quando escalo, ferramentas, skills, criterio de sucesso, criterio de extincao e rastreabilidade. **Este e o unico dos frameworks de componente em que o template NAO esta defasado**, e a diferenca esta medida em §15. |

## 5. Departamento, Capability e fronteira — `AR-09` a `AR-11`

| # | Regra |
|---|---|
| **AR-09** | **O agente pertence a EXATAMENTE UM departamento, e a cardinalidade e estrutural.** Fundamento: `FND-03 §3.3` e `R-01` de `FND-09 §6.1` — *"agente pertence a **exatamente um** departamento"*. **Agente compartilhado entre departamentos nao existe**; a necessidade que o sugeriria e **Workflow interdepartamental** (`WF-06` do Framework de Workflows), com **dono do resultado** declarado. |
| **AR-10** | **O agente nunca depende de agente de OUTRO departamento.** Fundamento literal: **`PD-12`**, em `R-04` de `FND-09 §6.1` — `AGT`/`SUB` dependem de `SKL`, `TOL`, `WFL`, **"nunca de agente de outro departamento"**. **A troca entre departamentos e por MENSAGEM ou por saida de artefato** (`R-05`), nunca por dependencia direta. **Dependencia direta criaria autoridade transversal que nenhuma Carta concedeu.** |
| **AR-11** | **Nenhuma entidade depende de entidade de estrato SUPERIOR.** Fundamento: **`PD-11`**. **Consequencia dura e frequentemente tentada:** um agente **nao depende** de `FND`, `ADR` nem `CAP` como componente — ele os **observa** como norma. `PD-02` proibe `FND`/`ADR` → componente, e `PD-03` proibe `CAP` → `DEP`/`AGT`/`TOL`/`PRO`. **Guarda nunca e coordenada por Linha** (`ES-02`, `IV-01`), e isso vincula o desenho de qualquer piloto de guarda. |

## 6. Autonomia — `AR-12` a `AR-15`

| # | Regra |
|---|---|
| **AR-12** | **`A0` a `A3` sao NIVEIS DE AUTONOMIA; `A1` a `A4` sao ARQUETIPOS; e as duas familias nao se somam, nao se comparam e nao se convertem.** Sempre que a notacao aparecer, **declara-se a familia**. Fundamento: `FND-01 §7.2` e `FND-09 §4`, medidos em §2. **Nenhuma Carta cita `A1`, `A2` ou `A3` sem a palavra *nivel* ou *arquetipo* ao lado** — e Carta que o faca e devolvida por ambiguidade, ainda que o autor soubesse o que quis dizer. |
| **AR-13** | **A autonomia do agente e IGUAL OU INFERIOR a do departamento, nunca superior, e nenhum papel opera acima de `A3`.** Fundamento literal: `FND-03 §3.3`, `FND-09 §E-11` e `FND-01 §7.2` — *"nenhum papel opera acima de `A3`"*. **A Carta declara o nivel como NUMERO**, nunca como adjetivo: *"bastante autonomo"* nao e nivel e nao se verifica. |
| **AR-14** | **Nenhum agente se autopromove, e a proibicao alcanca a via indireta.** Fundamento: **`LV-07`**, `AU-03` e `FND-01 §7.2` — *"nenhum papel se autopromove de nivel"*. **Alcanca:** propor a propria emenda de Carta **e aprova-la**; criar subagente de autonomia maior que a propria (`AR-20`); operar acima do `nivel_autonomia_concedido` na mensagem (**`AG-02`**); e **interpretar silencio como permissao**. **O agente que precise de mais autonomia PEDE, e quem concede e quem aprova a Carta.** |
| **AR-15** | **A autonomia e por MATERIA, e o teto do agente nunca excede os direitos de decisao do seu departamento.** Fundamento: `FND-01 §7.3`. **`A2` e `A3` decidem `Tipo 2` no proprio dominio; `Tipo 1` exige aprovacao em todos os quatro niveis** — inclusive `A3`, cuja propria definicao diz *"aprovacao humana apenas para `Tipo 1` e mudanca estrutural"*. **Nao existe nivel de autonomia que dispense ato do Soberano onde a norma o exige** (`LM-02`). |

## 7. A regra central — separacao de papeis sobre o mesmo objeto — `AR-16` a `AR-19`

> **Esta secao e a contribuicao propria deste Framework.** A regra existe hoje **espalhada**
> em `LV-03`, `AC-03`, `PI-05` e `RM-06b`, **sempre enunciada para artefato ou para
> departamento, nunca para o agente**. Aqui ela e enunciada para o agente, **sem criar
> norma nova**: cada item cita a fonte de que deriva.

| # | Regra |
|---|---|
| **AR-16** | **Um agente nao escreve, revisa e aprova sozinho o mesmo objeto com impacto relevante.** Derivada de: **`LV-03`** *(aprovacao pelo proprio proponente e nula)*, **`AC-03`** *(`revisor` ≠ `autor`)*, **`PI-05`** *(emissor ≠ aprovador)* e **`RM-06b`** *(DEP-GOV nao verifica artefato que ele proprio produziu)*. **"Impacto relevante" e definido, nao adjetivo** — `AR-17`. **Violacao torna o ato NULO, nao irregular:** o objeto nao passa a valer por ter sido bem feito. |
| **AR-17** | **"Impacto relevante" e toda mudanca de classe `C1` ou superior, mais toda mudanca `Tipo 1` de qualquer classe.** **A definicao e por classe medida, nunca por juizo do proprio agente** — deixar o executor julgar a relevancia do proprio ato reintroduz exatamente o que `AR-16` fecha. `C0` **e a unica faixa** em que proposta, autoria e aprovacao podem coincidir, e ela ja o preve: `FND-11 §5`, coluna `C0 · T2`, poe *proprietario* nas tres etapas. **Na duvida sobre a classe prevalece a mais restritiva** (`FND-01 §7.1`). |
| **AR-18** | **A separacao e por PAPEL, nunca por instancia, nome ou sessao.** Dois agentes do mesmo papel **nao** satisfazem `AR-16`: o que a norma exige e **independencia de perspectiva**, e duas instancias do mesmo papel carregam a mesma Carta, o mesmo escopo e o mesmo vies. **O revisor tem de ser de papel distinto** — e `FND-09 §8.2` ja nomeia quem, tipo a tipo. **Trocar de sessao nao troca de papel.** |
| **AR-19** | **A verificacao nao pode ser reflexiva, e o grafo o proibe.** Fundamento: **`LN-06`** *(ciclo em `verifica`, exceto reflexivo — ou seja: o reflexivo e vedado)* e `R-06` de `FND-09 §6.1`, que exclui expressamente *"artefato produzido pelo proprio DEP-GOV"* da verificacao de DEP-GOV. **Agente que verifique a propria saida produz evidencia sem valor probatorio**, e declarar essa evidencia como verificacao independente e **`LV-12`** — fabricar evidencia. |

## 8. Subagente — `AR-20` a `AR-22`

| # | Regra |
|---|---|
| **AR-20** | **O subagente declara `agente_pai` no frontmatter, tem escopo ESTRITAMENTE MENOR e autonomia menor ou igual a do pai.** Fundamento: `FND-03 §3.4` e `FND-09 §E-12`. **"Estritamente menor" e literal:** subagente cujo escopo iguale o do pai **e o pai com outro nome**, e a duplicata e recusada por `MT-02`. |
| **AR-21** | **Profundidade maxima um. Subagente nao tem subagente.** Fundamento literal: `FND-03 §3.4` e **`IV-04`**, em `R-01` de `FND-09 §6.1`. **A regra e estrutural e nao admite excecao por conveniencia:** cadeia mais funda dilui responsabilidade ate ninguem responder pelo resultado, que e o oposto do arquetipo **ATOR**. |
| **AR-22** | **O subagente comunica-se com o PAI, nao com outros departamentos, e e aposentado obrigatoriamente com ele.** Fundamento: **`AG-04`** e `FND-09 §E-12` — *"aposentado obrigatoriamente com o pai"*. **Subagente orfao nao existe:** extinto o pai, extingue-se o filho **na mesma mudanca** (`CV-04`), e nao em missao posterior. |

## 9. Componentes que o agente usa — `AR-23` a `AR-24`

| # | Regra |
|---|---|
| **AR-23** | **O agente declara, por nome, as `Skills`, `Ferramentas` e `Workflows` que usa — e a autorizacao NAO se herda por invocacao.** Fundamento: `R-04` de `FND-09 §6.1`, e `TF-30` do Framework de Ferramentas, que ja fixa a simetria: **`SKL` autorizada nao autoriza o `AGT` que a invoca**. **O nivel de dado do agente e o MENOR entre o dele e o do componente**, nunca o maior. ***"Todas as ferramentas do departamento"* nao e enumeracao** e e devolvido — nao se revoga o que nao foi nomeado. |
| **AR-24** | **`Command` nao e componente que o agente use: e ATRIBUTO `gatilho` de `SKL`/`WFL`.** Fundamento literal: **`FND-10 §4.8`**, tabela de **tipos recusados** — *"Command: forma de acionamento, nao artefato; vive no atributo `gatilho` de `SKL`/`WFL`"*. **Carta que declare *"Commands autorizados"* como bloco proprio cria tipo recusado por uso** (`MT-01`), e o uso de entidade nao ritualizada e **nulo**. **O que se declara e a `SKL` ou o `WFL`, e o gatilho vive dentro dele.** |

## 10. Contexto e memoria — `AR-25` a `AR-26`

| # | Regra |
|---|---|
| **AR-25** | **O contexto entregue ao agente segue o Pacote de Contexto: nucleo curto, suporte por referencia.** Fundamento literal: **`AG-05`** de `FND-05 §5`, e **`RC-01`** de `FND-06` — *"recuperacao devolve contexto minimo suficiente"*. **O template ja reserva a secao *"Contexto minimo (`PI-14`)"***, e preenche-la com *"tudo o que for necessario"* e nao preenche-la. **Carregar o maximo disponivel nao e cuidado: e transferir o custo de curadoria para quem executa** (`CE-01`, `PC-01`). |
| **AR-26** | **O agente declara o que GRAVA em memoria e em que camada, e o portao `QG-5` nao e opcional.** Fundamento: `FND-01 §6.2` — `QG-5`, *"o aprendizado foi extraido e gravado na memoria?"*, liberado por **DEP-KMS**. **Memoria de camada `EST` tem aprovacao propria** — `DEP-GOV`, e ratificacao do SOBERANO (`FND-09 §8.2` linha `MEM`) —, e **o agente nao promove a propria saida a `EST`**: seria `AR-16` por outra porta. |

## 11. Devolucao, escalonamento e custo — `AR-27` a `AR-28`

| # | Regra |
|---|---|
| **AR-27** | **A Carta declara QUANDO devolvo e QUANDO escalo, e os dois sao distintos.** O template ja reserva as duas secoes. **Devolver** e recusar entrada que nao satisfaz o criterio de aceite — e o handoff sendo recusado (`WF-17`), **portao funcionando, nao falha**. **Escalar** e levar adiante decisao que excede a propria autonomia (`AR-15`). **Confundir os dois produz escalonamento de trabalho mal-formado**, que consome autoridade para resolver o que era problema de entrada. **Cada um declara destinatario por PAPEL e condicao objetiva.** |
| **AR-28** | **Custo de agente e MEDIDO com instrumento e data, ou declarado `definido, sem valor` — proibido estimar.** Fundamento: `CE-04` e `LM-01`. **Mede-se, no minimo:** invocacoes, custo do `TOL` de classe `modelo` que o executa, e **contexto carregado por invocacao** (`CE-02`). **Agente cujo custo nunca foi medido nao pode ser comparado a alternativa**, e sem comparacao `PI-11` nao e exercivel — o criterio primario continua sendo **o resultado para a tarefa**. |

## 12. Ciclo de vida, extincao e registro — `AR-29` a `AR-30`

| # | Regra |
|---|---|
| **AR-29** | **`AGT` e `SUB` seguem o perfil de ciclo `P1`** (`FND-09 §E-11`, `§E-12`), e **`AGT` e `M2`** (`FND-10 §6.2`). **A versao segue o efeito** (`AL-01`): **MAIOR** quando muda departamento, nivel de autonomia, Capabilities ou a secao *"o que nao me compete"*; **MENOR** quando se acrescenta skill ou ferramenta sem alterar limites; **CORRECAO** quando nada normativo muda. **O criterio de extincao ou especializacao e obrigatorio** — o template ja o exige —, e **aposentar agente e `ADR`** (`FND-09 §8.2` linha `AGT`), nunca ato tacito por desuso. |
| **AR-30** | **Um template canonico, um registro mestre, e nenhum registro novo.** **Template:** `TPL-carta-agente`, unico. **Registro mestre:** o catalogo mestre e o **contador oficial** das sequencias `AGT` e `SUB`; **criar agente e incrementar o contador sao a mesma mudanca** (`CV-04`, `IX-02`). **Nenhum registro novo** — seria proliferacao (`FND-04 §6.1`, `RG-05`). **Este Framework e `M2`, `C2 · Tipo 2`: emenda-se por versao e NAO exige ato.** |

## 13. O que este Framework NAO faz

| # | Nao faz | Verificacao |
|---|---|---|
| **N1** | **Nao cria entidade.** `AGT` e `SUB` ja existem | `FND-03 §3.3`, `§3.4`; `FND-09 §E-11`, `§E-12` — `0` linhas acrescentadas |
| **N2** | **Nao cria nivel de autonomia nem arquetipo** | `A0`–`A3` de `FND-01 §7.2` e `A1`–`A4` de `FND-09 §4` **recebidos**; `AR-12` apenas **desambigua** |
| **N3** | **Nao cria tipo, template, diretorio, papel, portao nem verbo de autoridade** | `FND-09 §11.1`; `MT-01`, `CS-01`. Portoes: `QG` **7 antes, 7 depois**; `GO-TO-*` **2 antes, 2 depois** |
| **N4** | **Nao altera a matriz de `FND-09 §8.2`** | `0` celulas |
| **N5** | **Nao cria norma nova em `AR-16` a `AR-19`** | Cada uma **cita a fonte** de que deriva: `LV-03`, `AC-03`, `PI-05`, `RM-06b`, `LN-06` |
| **N6** | **Nao corrige a colisao `A1`/`A2`/`A3`** | Sanar `FND-01` ou `FND-09` e emenda de Fundacional, **`C3` com ato**. Fica em `AA-1` |
| **N7** | **Nao cria agente, subagente nem piloto** | **`0`** `AGT` · **`0`** `SUB` · `departments/*/agents/` inexistente nos **9** departamentos |
| **N8** | **Nao cria `Command` nem bloco de Commands** | `AR-24`; `FND-10 §4.8` — tipo **recusado** |
| **N9** | **Nao promove a si mesmo a `FND`** | Promover e `C3 · Tipo 1` com ato |

## 14. Achados que este candidato ABRE

| # | Achado | Severidade | Dono | Gatilho |
|---|---|---|---|---|
| **AA-1** | **Colisao de notacao `A1`/`A2`/`A3` entre `FND-01 §7.2` *(niveis de autonomia)* e `FND-09 §4` *(arquetipos)*, com as duas familias no MESMO cartao `E-11`** — linha *Autoridade* remetendo a uma, linha *Arquetipos* usando a outra. Leitura sem chave sugere que o agente opera em `A3` *(Delegado)*, que e o que `LV-07` proibe. **Mitigado** pela linha *Autoridade*, que declara o teto; **nao sanado** | **Media** | `DEP-GOV` | Primeira Carta de agente |
| **AA-2** | **`departments/<dep>/agents/` nao existe em nenhum dos 9 departamentos**, embora `FND-03 §7` o declare na estrutura canonica *"(fase futura)"*. **O obstaculo nao e o diretorio** — e `LV-06`: sem Carta aprovada nao ha agente | **Baixa** | `DEP-EXE` | Primeiro agente |
| **AA-3** | **A regra que o roadmap chama de central — *"um agente nao escreve, revisa e aprova sozinho"* — nao existe enunciada em lugar nenhum do acervo para o AGENTE.** Existe para artefato (`AC-03`), para aprovacao (`LV-03`), para instrumento (`PI-05`) e para DEP-GOV (`RM-06b`). **Quatro fontes, nenhuma sobre agente** | **Media** | `DEP-GOV` | Primeiro agente |

## 15. Recepcao × contribuicao — medido

| Origem | Quantas regras | Quais |
|---|---|---|
| **Recebidas** de fonte vigente | **26** | `AR-01` a `AR-15`, `AR-20` a `AR-30` |
| **Contribuicao propria** | **4** | `AR-16` a `AR-19` — a separacao de papeis, enunciada para o agente pela primeira vez |

**Vinte e seis de trinta sao recepcao — a maior proporcao dos tres frameworks desta
missao**, e a razao esta em §1: o Agente e o componente mais especificado do acervo.
**Comparacao medida:** Ferramentas recebeu menos e **achou dois defeitos de template**;
Workflows recebeu 23 de 30; **Agentes e o unico cujo template NAO esta defasado.**

## 16. Limites declarados — **determinado, nao observado**

| # | Limite | Fundamento |
|---|---|---|
| **L1** | **Nenhum `Agente` real existe.** As **30** regras sao determinadas, nao observadas. `FND-09 §E-11`: *"Nenhuma instancia nesta fase"* | Medido 2026-08-02 |
| **L2** | **`AR-16` a `AR-19` nunca foram exercidas contra um agente**, porque nao ha agente. **A contribuicao propria e a parte menos testada** — o mesmo padrao de `WF-19`–`WF-25` | `PI-10` |
| **L3** | **Os dois pilotos que o roadmap pede — um de execucao, um de guarda — NAO foram criados**, e nao poderiam: `LV-06` exige Carta aprovada, e aprovar Carta e `C2` com `DEP-EXE`, fora do alcance de candidato | `LV-06`; `FND-04 §6` |
| **L4** | **O piloto de guarda tem restricao estrutural ja vigente e nao trivial:** **`ES-02`/`IV-01`** — *"Guarda nunca e coordenada por Linha"*. Um piloto de guarda subordinado a departamento de Linha **nasce invalido** | `ES-02`, `IV-01` |
| **L5** | **`AR-23` depende de `SKL`, `TOL` e `WFL` existirem, e nenhum existe:** `0` Skills, `0` Ferramentas, `0` Workflows. **O agente e o ultimo elo de uma cadeia cujos elos anteriores estao vazios** | Medido 2026-08-02 |

## 17. Rastreabilidade e revisao

| Campo | Conteudo |
|---|---|
| **Origem das entidades** | `FND-03 §3.3`, `§3.4` · `FND-09 §E-11`, `§E-12` · `FND-09 §8.2` linha `AGT` — **recebidas** |
| **Fontes recebidas e nao alteradas** | `FND-01 §6.2`, `§7.2`, `§7.3` · `FND-02` · `FND-04 §6` · `FND-05 §5` e `AG-02`/`AG-04`/`AG-05` · `FND-06 RC-01` · `FND-08 §8` · `FND-09 §4`, `§6.1` · `FND-10 §4.8`, `§6.2` · `TPL-carta-agente` |
| **Metodo** | O de `ADR-0021`: contrato em ADR `C2 · Tipo 2`, **sem emendar fonte alguma** |
| **Gatilho de revisao** | O **primeiro Agente real** (`L1`); **ou** o primeiro exercicio de `AR-16` *(um ato recusado por acumulo de papeis)*; **ou** a criacao do primeiro `SUB` |
| **O que se mede na revisao** | Quantas Cartas foram devolvidas, e por qual regra; quantas vezes `AR-16` **recusou** um ato e quantas foi contornado; se `AR-12` eliminou a ambiguidade `A1`/`A2`/`A3` na pratica; custo medido por invocacao (`AR-28`) contra a alternativa |

---

## Rito e rastreabilidade da admissao

Cadeia: [RFC-0037](../rfcs/RFC-0037-framework-de-agentes.md) → este ADR →
[FIT-2026-035](../governance/fitness/FIT-2026-035-framework-de-agentes.md). Achados `AA-1`
a `AA-3` **abertos** com dono *(o `AA-1` com o agravante atenuado pela emenda 1.6.0,
remedido nesta admissao)*. **Gatilho de revisao:** o primeiro agente real *(que exige Carta
aprovada — e os dois pilotos contrastantes sao o desenho do Goal para isso)*.
