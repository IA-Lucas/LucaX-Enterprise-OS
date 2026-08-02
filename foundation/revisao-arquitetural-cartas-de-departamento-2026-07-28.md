---
id: REV-DEPARTAMENTO-2026-07-28
titulo: Revisao arquitetural do Contrato de Carta de Departamento, da matriz Departamento × Capability e dos dois pilotos
tipo: fitness
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-QAR
proprietario: DEP-QAR
aprovador: DEP-EXE
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0011]
substitui: []
substituido_por: null
objeto_avaliado: [RFC-0008, ADR-0011, TPL-carta-departamento, IDX-capabilities, DEP-QAR, DEP-ENG]
classe_avaliacao: corretude
resumo: Examina a corretude do contrato de Carta de Departamento, da projecao Departamento × Capability e dos dois pilotos, e valida-os em seis cenarios.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-GOV
ratificacao: nao-exigida
---

# REV-DEPARTAMENTO-2026-07-28

## Proposito
Examinar a **corretude estrutural** do Contrato de Carta de Departamento, da projecao
Departamento × Capability e dos dois pilotos — e submeter os pilotos a seis cenarios reais
antes de qualquer rollout.

## Escopo
| Item | Definicao |
|---|---|
| Inclui | RFC-0008 · ADR-0011 · `TPL-carta-departamento` v1.1.0 · a projecao de `capabilities/README §10` · as Cartas **DEP-QAR** e **DEP-ENG** · a reconciliacao das ressalvas de aptidao abertas · a varredura C11 · a reconciliacao catalogo-fonte · a terceira medicao de contexto |
| **Nao** inclui | **Aptidao evolutiva** — objeto de [FIT-2026-005](../governance/fitness/FIT-2026-005-cartas-de-departamento.md). As sete Cartas restantes. Qualquer alteracao em Carta de Capability |
| Metodo | Confronto com FND-01 a FND-10; leitura do frontmatter das 23 Cartas de Capability por ferramenta; varredura de links relativos sobre **todos** os `.md`; varredura **C11** dos indices contra as fontes; reconciliacao catalogo-fonte artefato a artefato; medicao `wc -l` e `sed`+`wc -l`; execucao dos seis cenarios de validacao |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| **Executa** | **DEP-QAR** | FT-02, RM-06b — **nao produziu nenhum artefato avaliado**. Autor das Cartas e DEP-EXE |
| **Desvio declarado** | **DEP-GOV** verifica os blocos **B4**, **B9** e **B12** da Carta **DEP-QAR** | DEP-QAR esta impedido de julgar o instrumento que define a propria autoridade (§4) |
| Forma | DEP-GOV | |
| Evidencia | DEP-KMS | Medicoes de acervo, de secao e de pacote |
| Aprova | DEP-EXE | FND-10 §10.3 |

---

## 0. Divergencias corrigidas durante esta revisao

| # | Divergencia | Correcao aplicada |
|---|---|---|
| **D1** | **`projecao_de` declarado em Carta de Departamento.** O template e as duas Cartas declaravam `projecao_de` no frontmatter porque a secao 2 projeta a custodia. **FND-10 §2.2 restringe o campo a artefato "cujo conteudo seja *majoritariamente* projecao — indice, catalogo, matriz derivada"**. Uma Carta tem **uma** secao projetada entre treze; declarar o campo marcaria a Carta inteira como vista derivada em qualquer varredura, quando ela e **M2** e contem informacao original | Campo **removido** do template e das duas Cartas. A projecao da secao 2 permanece declarada **no corpo**, com as quatro informacoes de PJ-02 — que e o instrumento correto e suficiente. **Encontrado pelo cenario CN-4**, antes de qualquer rollout |

> **D1 e o primeiro defeito que a validacao por cenario encontrou, e ele nao teria sido
> encontrado pela leitura do contrato.** So apareceu quando se perguntou *"que artefato esta
> sendo criado, e sob que contrato?"* — o cenario de criacao de artefato. Registrado como
> evidencia a favor da validacao por cenario em §3.

---

## 1. Os entregaveis foram cumpridos?

| # | Entregavel exigido | Onde esta | Veredito |
|---|---|---|---|
| 1 | **Department Charter Contract** — conteudo minimo e limites | [ADR-0011 §5.1 a §5.4](../decisions/ADR-0011-contrato-de-carta-de-departamento.md): **doze blocos** B1–B12 e **oito** conteudos proibidos | **Cumprido** |
| 2 | **Regras de desenho** — as sete exigidas | ADR-0011 §5.3: **DC-01 a DC-07** correspondem uma a uma as sete; DC-08 a DC-10 cobrem projecao, vigencia e medicao | **Cumprido** |
| 3 | **Matriz Departamento × Capability** — projecao unica, com custodia, exercicio, dependencia e lacunas | [capabilities/README §10](../capabilities/README.md): §10.1 custodia e exercicio · §10.2 exposicao derivada · §10.3 **oito achados** | **Cumprido** |
| 4 | **Template revisado**, com resumo operacional e perfil minimo de carregamento | `TPL-carta-departamento` **1.1.0**: emenda MENOR; nenhum template concorrente criado | **Cumprido** |
| 5 | **Dois pilotos de classes distintas**, um testando independencia/segregacao e outro execucao/interfaces | **DEP-QAR** *(Guarda)* e **DEP-ENG** *(Linha)*; justificativa da amostra em §2.1 | **Cumprido, com limite declarado** — Comando e Plataforma sem piloto |
| 6 | **Validacao em seis cenarios**, com correcao do contrato antes do rollout | §3 desta revisao; **uma** correcao aplicada antes do encerramento (D1) | **Cumprido** |

### 1.1 O que a missao **nao** criou, e devia nao criar

| Nao criado | Verificacao |
|---|---|
| **FND-11** ou qualquer documento fundacional | `foundation/` continua com **10** documentos normativos |
| Entidade nova | **21** entidades; `DEP` ja existia (FND-09 §5.4) |
| Tipo documental novo | **33** tipos; `Carta de Departamento` ja existia (FND-10 §4.3) |
| Camada de memoria nova | **5** camadas |
| Template novo | **19** templates; um **emendado**, nenhum criado |
| Departamento, agente, subagente, skill, workflow, produto, projeto, ferramenta | **0** de cada. Os dois departamentos **ja existiam** desde ADR-0001 |
| Codigo, banco, infraestrutura, migracao do Legacy | **0**; proveniencia do acervo permanece **100% `native`** |
| Ratificacao | **Nenhuma produzida.** Nenhum ato do Soberano foi inferido, presumido ou declarado |

## 2. Conformidade dos artefatos produzidos

| Artefato | Frontmatter completo | 5 campos do contrato | `revisor` ≠ `autor` | Tipo em FND-10 §4 | Local conforme FND-03 §7 | Blocos obrigatorios |
|---|---|---|---|---|---|---|
| RFC-0008 | Sim | Sim | DEP-GOV ≠ DEP-EXE | RFC | `rfcs/` | Sim |
| ADR-0011 | Sim | Sim | DEP-GOV ≠ DEP-EXE | ADR | `decisions/` | Sim, 13 secoes |
| TPL-carta-departamento 1.1.0 | Sim | Sim *(AC-08)* | DEP-QAR ≠ DEP-GOV | Template | `foundation/templates/` | Sim |
| capabilities/README 1.1.0 | Sim | Sim *(AC-08)* | DEP-GOV ≠ DEP-EXE | Indice | `capabilities/` | Sim |
| **DEP-QAR** carta | Sim | Sim | DEP-GOV ≠ DEP-EXE | Carta de Departamento | `departments/qar/` | Sim, 12 blocos |
| **DEP-ENG** carta | Sim | Sim | DEP-GOV ≠ DEP-EXE | Carta de Departamento | `departments/eng/` | Sim, 12 blocos |
| MEM-APR-0002 1.1.0 | Sim | Sim *(AC-08)* | DEP-QAR ≠ DEP-KMS | Memoria APR | `memory/aprendizado/` | Sim |
| FIT-2026-005 | Sim | Sim | DEP-GOV ≠ DEP-QAR | Fitness Check | `governance/fitness/` | Sim |
| MEM-APR-0004 | Sim | Sim | DEP-QAR ≠ DEP-KMS | Memoria APR | `memory/aprendizado/` | Sim |
| Esta revisao | Sim | Sim | DEP-GOV ≠ DEP-QAR | Revisao Arquitetural | `foundation/` | Sim |

**AC-08 aplicado, nao retroatividade.** **Tres** artefatos preexistentes foram **emendados**
com incremento MENOR — `TPL-carta-departamento`, `capabilities/README` e `MEM-APR-0002` — e os
tres ja declaravam os cinco campos. **Nenhum outro artefato do acervo foi tocado** para receber
campo, e **nenhum** foi reescrito por retroatividade (EV-03).

Os **nove** indices atualizados sao **M3 derivados** e, por **AC-09**, a atualizacao derivada
**nao** dispara a obrigacao — exceto `capabilities/README`, cuja **estrutura** mudou com a
secao §10 nova, o que incrementa MENOR e dispara AC-08.

### 2.1 Justificativa da amostra de pilotos

| Criterio | DEP-QAR | DEP-ENG |
|---|---|---|
| **Classe** | **Guarda** | **Linha** — classes distintas, como exigido |
| **O que testa** | **Independencia e segregacao** | **Execucao e interfaces** |
| Por que este, e nao outro da mesma classe | DEP-GOV e o **revisor** de Carta de Departamento (FND-09 §8.2). Se DEP-GOV fosse piloto, revisaria a propria Carta — **violacao direta de RM-06b sem saida**. Com DEP-QAR, DEP-GOV revisa normalmente e o residuo se reduz a §4 | E o departamento de **maior custodia** (5 de 23), o unico com **duas** Capabilities `nucleo` no mesmo dominio, o que tem a Capability mais profunda do grafo *(nivel 7)* e o maior numero de linhas na matriz de interacao de FND-02 §4 |
| Sinal que a escolha expoe | Poder de **veto**, custodia obrigatoria na Guarda (OW-05), **sete** impedimentos, e o caso `verifica` × `depende-de` de ADR-0005 | **VC-03 disparado** (5 > 3), fronteira IA × agentes, e o maior numero de handoffs recebidos e emitidos |
| **Limite declarado** | As classes **Comando** *(DEP-EXE)* e **Plataforma** *(DEP-KMS, DEP-TLS)* ficam **sem piloto**. O contrato tera sido exercido em **2 de 4** classes quando o rollout for decidido | |

## 3. Validacao dos pilotos — seis cenarios

**Metodo:** cada cenario e uma pergunta real. A pergunta e respondida **usando apenas as duas
Cartas e as normas que elas citam**. Se a resposta for ambigua, o defeito e do contrato e ele
e corrigido **antes** do rollout.

### CN-1 — Decisao

> **Situacao:** DEP-ENG conclui que um modelo de IA novo e superior ao vigente e quer passar a
> usa-lo. Quem decide?

| Passo | Fonte na Carta | Resultado |
|---|---|---|
| DEP-ENG pode **escolher e avaliar** modelo? | DEP-ENG §5, linha "Escolha e avaliacao de modelo de IA", **A2**, fonte FND-02 §3 e PI-11 | **Sim** |
| DEP-ENG pode **adotar** a ferramenta? | DEP-ENG **§10, I-4**: impedido — adocao e de DEP-TLS, aprova DEP-EXE, ratifica SOBERANO | **Nao** |
| Quem julga o risco? | DEP-QAR §5, "Nivel de risco", A2 | DEP-QAR |
| Ha conflito entre as duas linhas? | §5 concede A2 sobre a **escolha**; §10 I-4 nega a **adocao** | **Nao ha conflito** — sao atos distintos |

**Veredito: resolvido sem ambiguidade.** A distincao *escolher* × *adotar* so fica nitida
porque **B4 e B9 coexistem**: a linha de autoridade e lida contra o impedimento
correspondente. **Melhoria identificada e aplicada:** o checklist do template passa a exigir
que **B4 e B9 sejam conferidos um contra o outro** — ver §3.7, correcao **M1**.

### CN-2 — Handoff

> **Situacao:** DEP-PRD entrega a DEP-ENG uma spec sem criterio de aceite verificavel.

| Passo | Fonte na Carta | Resultado |
|---|---|---|
| DEP-ENG pode recusar? | DEP-ENG §8.2, "Spec para construcao", criterio de devolucao: *criterio nao verificavel* | **Sim, devolve** |
| A responsabilidade transfere-se? | HO-01 — silencio nunca transfere; sem aceite, o dono continua sendo DEP-PRD | **Nao** |
| DEP-ENG pode "consertar" a spec? | DEP-ENG §4, "Decidir o que construir" — nao lhe compete; §10 **I-3** repete como impedimento | **Nao** |
| E se acontecer duas vezes? | DEP-ENG §8.2, nota: **HO-03** escala a DEP-EXE — defeito de fronteira | Escalonamento **E2** |

**Veredito: resolvido sem ambiguidade.** O cenario tambem confirma que B3 *(o que nao me
compete)* e B9 *(impedimento)* **nao sao redundantes**: o primeiro delimita dominio, o segundo
declara **quem substitui**. Sem I-3, a Carta diria o que DEP-ENG nao faz sem dizer para onde
o trabalho volta.

### CN-3 — Conflito de autoridade

#### CN-3a — Veto contestado

> **Situacao:** DEP-QAR veta uma entrega de DEP-ENG. DEP-ENG discorda tecnicamente.

| Passo | Fonte | Resultado |
|---|---|---|
| DEP-ENG pode prosseguir? | DEP-ENG §4: nao decide se a entrega passa. **LV-09**: ignorar veto sem decisao do Soberano e violacao | **Nao executa** |
| DEP-QAR pode reverter o proprio veto sob pressao? | DEP-QAR §4: *"Reverter o proprio veto — SOBERANO"* | **Nao** |
| Quem resolve? | DEP-QAR §8, gatilho *"Veto contestado pela Linha"* → **E4**, bloqueante | **SOBERANO** |
| DEP-ENG pode instruir DEP-QAR? | DEP-QAR §10, **I-6**: Guarda nunca e priorizada nem instruida por Linha (ES-02, IV-01) | **Nao** |

**Veredito: resolvido sem ambiguidade, nos dois sentidos.** As duas Cartas convergem sem se
citarem: DEP-ENG declara que nao decide, DEP-QAR declara que nao reverte. A convergencia vem
de ambas citarem a **mesma fonte**, o que e o efeito pretendido por DC-04.

#### CN-3b — Impedimento do verificador *(teste de segregacao)*

> **Situacao:** a mudanca a encerrar foi **produzida por DEP-QAR**. Quem emite o `FIT`?

| Passo | Fonte | Resultado |
|---|---|---|
| DEP-QAR pode executar o `FIT`? | DEP-QAR §10, **I-1**: executor ≠ produtor; acumulo torna o veredito **nulo** | **Nao** |
| Quem substitui? | I-1: revisor independente designado na mudanca; se nenhum for possivel, **escala ao SOBERANO** | Substituto nomeado |
| DEP-QAR pode aprovar o proprio veredito? | §10, **I-4**: aprovacao e de DEP-EXE | **Nao** |
| E se DEP-EXE tambem estiver impedido? | DEP-QAR §10.1, **RQ-2**: impedimento cruzado, achado **C5** de REV-CONSOLIDACAO, dono DEP-GOV | **A Carta nomeia o achado em vez de improvisar** |

**Veredito: resolvido, com limite declarado.** A Carta **nao resolve** o impedimento cruzado —
e nao deveria: o achado C5 tem dono e gatilho fixados por outra revisao, e resolve-lo aqui
usurparia o dono declarado. O que a Carta faz e **tornar o impedimento legivel antes de ele
ocorrer**, que e a funcao de B9.

### CN-4 — Criacao de artefato

> **Situacao:** DEP-ENG quer criar uma **Skill**.

| Passo | Fonte | Resultado |
|---|---|---|
| DEP-ENG pode ser autor? | DEP-ENG §7, linha `SKL`: **autor** | Sim |
| DEP-ENG pode aprovar? | FND-09 §8.2, linha `SKL`: revisa DEP-GOV + DEP-QAR, **aprova DEP-EXE**. DEP-ENG §5.1 nao lista aprovacao de Skill | **Nao** |
| A Skill precisa de vinculo a Capability? | VC-01, pre-condicao universal I de FND-04 §6 | **Sim**, ao menos uma ativa |
| O tipo existe? | FND-10 §4.4, `SKL` | Sim |

**Veredito: resolvido — e foi este cenario que encontrou o defeito D1.** Ao perguntar *"que
artefato esta sendo criado, e sob que contrato?"*, verificou-se que a **propria Carta**
declarava `projecao_de` sem ser majoritariamente projecao. Corrigido em §0.

### CN-5 — Uso de memoria

> **Situacao:** DEP-QAR conclui que "toda entrega sem plano de reversao deve ser barrada" e
> quer gravar isso como norma organizacional.

| Passo | Fonte | Resultado |
|---|---|---|
| DEP-QAR pode escrever em **EST**? | DEP-QAR §9: *"Leitor obrigatorio. **Nao escrevo**"* — escrita em EST e de DEP-GOV, mediante ADR (FND-06 §3.1) | **Nao** |
| Onde a conclusao cabe? | Criterio de alocacao de FND-06 §4: e **licao generalizavel** → camada **APR**, dono DEP-KMS | **APR** |
| Vira norma? | MM-07: memoria informa, nao obriga. Virar norma exige **ADR** | **Nao por registro** |
| DEP-QAR pode registrar direto em APR? | DEP-QAR §9: **contribuinte obrigatorio**; o **dono** e DEP-KMS | Contribui; nao decide alocacao |

**Veredito: resolvido sem ambiguidade.** O bloco B7 impediu tres erros distintos numa unica
leitura: escrever na camada errada, transformar registro em norma, e assumir propriedade de
camada alheia.

### CN-6 — Especializacao

> **Situacao:** DEP-ENG custodia **5** Capabilities e VC-03 fixa o sinal em **tres**. Dividir?

| Passo | Fonte | Resultado |
|---|---|---|
| Ha sinal observado? | DEP-ENG §12.1: **um** — a contagem 5 > 3 | Um sinal |
| Quantos SE-02 exige? | **Dois** sinais observados | Insuficiente |
| Os demais gatilhos tem sinal? | §12.1: carga concentrada, contexto excessivo, fronteira em disputa, duplicacao e gargalo — **todos com zero** sinal medido | Nao |
| Qual e a decisao? | **Nao especializar**, registrada com custo assumido (FND-04 §6.2, PI-14 regra 2) | Registrada |
| O custo fica invisivel? | §12.1 declara: DEP-ENG opera acima do limite de VC-03 ate a 1a revisao estrutural | **Declarado** |

**Veredito: resolvido sem ambiguidade, e no sentido contra-intuitivo.** O contrato **impediu**
uma divisao que a contagem isolada sugeriria. Dividir DEP-ENG hoje produziria dois
departamentos sem producao em vez de um — fragmentacao, nao especializacao. E o exercicio
mais forte de DC-06: **ganho previsto nao autoriza divisao**.

### 3.7 Correcoes aplicadas ao contrato antes do rollout

| # | Origem | Correcao |
|---|---|---|
| **D1** | CN-4 | `projecao_de` removido do template e das duas Cartas; a projecao da secao 2 declara-se no corpo (§0) |
| **M1** | CN-1 | Checklist do template passa a exigir a **conferencia cruzada B4 × B9**: toda linha de autoridade e lida contra o impedimento correspondente. Sem ela, a distincao *escolher* × *adotar* de CN-1 dependeria de leitura atenta em vez de verificacao |

### 3.8 Sintese da validacao

| Cenario | Ambiguidade encontrada? | Defeito no contrato? |
|---|---|---|
| CN-1 Decisao | Nao | **Sim — melhoria M1 aplicada** |
| CN-2 Handoff | Nao | Nao |
| CN-3a Conflito de autoridade | Nao | Nao |
| CN-3b Segregacao | Nao — limite declarado | Nao |
| CN-4 Criacao de artefato | Nao | **Sim — defeito D1 corrigido** |
| CN-5 Uso de memoria | Nao | Nao |
| CN-6 Especializacao | Nao | Nao |

**Seis cenarios · zero ambiguidades nao resolvidas · duas correcoes aplicadas antes do
encerramento.**

## 4. Segregacao — o residuo de DEP-QAR ser piloto

| Campo | Conteudo |
|---|---|
| **Conflito identificado** | DEP-QAR e **objeto** de um piloto e **autor** desta revisao |
| **O que nao e conflito** | DEP-QAR **nao produziu** nenhum artefato avaliado: autor das duas Cartas e DEP-EXE, revisor e DEP-GOV. FT-02 e CV-08 estao satisfeitos quanto a producao |
| **O que e conflito** | Julgar favoravelmente os blocos **B4** *(autoridade)*, **B9** *(impedimentos)* e **B12** da propria Carta seria confirmar a propria autoridade — vizinho de AU-03 e LV-07, e alcancado por **RM-06b** |
| **Desvio aplicado** | Os tres blocos da Carta **DEP-QAR** foram verificados por **DEP-GOV**, e o resultado esta em §4.1. Mesmo instrumento do desvio declarado em FIT-2026-003 |
| **Residuo remanescente** | DEP-QAR **redige** o documento que contem a verificacao de DEP-GOV. O residuo e de **forma**, nao de merito: DEP-GOV pode contradizer o texto, e a contradicao seria registrada. **Declarado em vez de omitido** (PI-10) |
| **Alternativa avaliada e recusada** | Trocar o piloto de Guarda por DEP-GOV **agrava**: DEP-GOV e o revisor previsto de toda Carta de Departamento (FND-09 §8.2) e revisaria a propria Carta, sem substituto possivel. A troca move o problema de **forma** para **merito** |

### 4.1 Verificacao de DEP-GOV sobre os blocos impedidos da Carta DEP-QAR

| Bloco | O que DEP-GOV verificou | Resultado |
|---|---|---|
| **B4** — autoridade | Cada uma das **8** linhas de §5 tem coluna **Fonte** preenchida, e cada fonte foi conferida no documento citado | **Conforme.** Nenhuma autoridade autodeclarada; nenhuma linha excede FND-01 §7.3 ou FND-02 §3 |
| **B4** — o que nao decide | **4** linhas em §5.1, todas com dono e fonte | **Conforme** |
| **B9** — impedimentos | **7** impedimentos, todos com materia, motivo, **substituto nomeado** e fonte | **Conforme.** I-3 e o mais relevante: reconhece que `CAP-qualidade` **depende de** `CAP-governanca` e que, por RL-05, DEP-QAR **nao** pode exercer verificacao permanente sobre a competencia de DEP-GOV |
| **B12** — carregamento | Numeros de §13.2 reproduzidos por DEP-GOV com `sed`+`wc -l`: **50**, **111** e **386** linhas | **Conforme** — os tres valores conferem |
| Ampliacao de autoridade | Comparacao linha a linha entre §5 da Carta e FND-02 §3 | **Nenhuma ampliacao.** A Carta declara **menos** do que FND-02 §3 permitiria em dois pontos, e nada alem em nenhum |

## 5. Reconciliacao das ressalvas de aptidao abertas

> **Pre-correcao 1 da missao.** Todas as **12** ressalvas abertas ao inicio foram
> reconciliadas: fechadas com evidencia, mantidas com dono, gatilho e custo, ou escaladas.

| Origem | Ressalva | Gatilho disparou? | **Tratamento** |
|---|---|---|---|
| FIT-2026-001 R1 | Acrescimo liquido sem proporcao comprovada | **Nao** — gatilho e a 1a revisao estrutural, que esta missao **nao e** | **Mantida.** Dono DEP-EXE · custo: atravessa **cinco** ciclos |
| FIT-2026-001 R3 | Arquetipo A2 reune 19 de 21 entidades | **Nao** | **Mantida.** Dono DEP-GOV · custo: inalterado, nenhuma entidade instanciada |
| FIT-2026-002 R1 | 40 regras novas, proporcao nao comprovada | **Nao** | **Mantida, com progresso medido:** §5.1 |
| FIT-2026-002 R3 | Classe M3 com um unico membro | **Nao** | **Mantida.** Dono DEP-GOV · custo: inalterado |
| FIT-2026-002 R4 | Reducao de contexto **calculada**, nao observada | **Ja disparado**, mantida em FIT-2026-004 | **Mantida.** A terceira medicao **nao demonstra reducao** (§9). Fechar aqui seria maquiar |
| FIT-2026-003 R1 | 10 regras de fronteira sem exercicio possivel | **Nao** — gatilho e a 2a revisao estrutural | **Mantida.** Dono DEP-EXE |
| FIT-2026-003 R2 | Portao de admissao e 4 classificacoes com zero membros | **Nao** — nenhum candidato do Legacy | **Mantida.** Dono DEP-GOV |
| **FIT-2026-003 R3** | **Reducao de contexto medida uma unica vez, em missao atipica** | **Sim** — "proxima missao" | ✅ **FECHADA** — §5.2 |
| FIT-2026-004 R1 | 32 regras novas; 15 sem exercicio possivel | **Sim** — "segunda missao sob o contrato" | **Mantida, medida e escalada:** §5.3 |
| FIT-2026-004 R2 | Tres abstracoes com zero membros | **Sim** — "primeiro componente criado" | **Mantida, com o gatilho avaliado e inconclusivo:** §5.4 |
| **FIT-2026-004 R3** | 4a missao consecutiva de crescimento; nenhuma ressalva fechada; custo subiu | **Sim** — "proxima mudanca C2/C3: terceira medicao" | ✅ **FECHADA** — §5.5 |
| FIT-2026-004 R4 | MEM-EST-0001 permanece `aprovado` | **Nao** — nenhum ato do Soberano; achado C2 nao resolvido | **Mantida e escalada ao SOBERANO** |

**Resultado: 12 reconciliadas · 2 fechadas com evidencia · 8 mantidas com dono, gatilho e
custo · 2 escaladas.** Nenhuma ressalva ficou sem destino.

> **Nao houve incidente de estagnacao.** A pre-correcao 1 obrigava registra-lo caso **nenhuma**
> ressalva anterior pudesse fechar. Duas fecharam com evidencia reproduzivel, e o fundamento de
> cada uma esta abaixo — nao no fato de haver duas.

### 5.1 FIT-2026-002 R1 — progresso medido, sem fechamento

Regras de FND-10 exercidas **nesta missao**, nominalmente: `AC-01` *(nenhum derivavel no
frontmatter)* · `AC-02` · `AC-03` · `AC-06` · **`AC-08`** *(dois artefatos emendados)* ·
`AC-09` *(indices atualizados sem disparar a obrigacao)* · `CS-01` · `CE-01` · `CE-02` ·
`CE-04` · `LM-02` · `LN-07` · `PJ-01` · `PJ-02` · `PJ-03` · `PJ-05` · `RG-01` · `RG-02` ·
`RG-03` · `SE-01` · `SE-02` · `SE-07` · `IX-02` — **23 regras**.

**Por que nao fecha:** a ressalva pede **proporcao comprovada** entre as 40 regras e o ganho,
e o gatilho declarado pelo dono e a **1a revisao estrutural**. Fechar antes do gatilho, com
contagem de exercicio em vez de proporcao de ganho, responderia outra pergunta.

### 5.2 FIT-2026-003 R3 — **fechada**

| Campo | Conteudo |
|---|---|
| Texto da ressalva | *"Reducao de contexto medida **uma unica vez**, em **missao atipica**"* |
| Gatilho | *"Proxima missao"* — disparado |
| **Evidencia do fechamento** | Ha agora **tres** medicoes observadas, em **tres naturezas distintas** de missao: consolidacao *(1.4)*, construcao sobre a Fundacao *(1.5)* e construcao de componente *(1.6)*. **23% · 33% · 30,6%** |
| Por que isso fecha | A ressalva questionava a **suficiencia amostral** — uma medicao, e atipica. Tres medicoes em tres naturezas encerram exatamente essa duvida |
| **O que nao fecha com ela** | A **direcao** da serie. Isso e R4 de FIT-2026-002, que **permanece aberta** (§5). Separar as duas e o que impede que este fechamento seja maquiagem |
| Dono | DEP-KMS |

### 5.3 FIT-2026-004 R1 — medida, mantida, criterio escalado

| Campo | Conteudo |
|---|---|
| Gatilho | *"Segunda missao sob o contrato: medir quantas das 28 regras `CT` foram exercidas. Menos de um terco abre proposta de consolidacao"* |
| **Medicao** | **0 de 28.** Nenhuma regra `CT` foi exercida: esta missao **nao registrou nenhuma afirmacao sobre o Soberano** e **nao carregou nenhum pacote** de MEM-EST-0001, que permanece `aprovado` e nao vigente |
| A condicao literal foi atingida? | **Sim** — 0 < 1/3 |
| **A proposta de consolidacao foi aberta?** | **Nao**, e o motivo esta declarado: zero exercicio numa missao cujo **objeto e outro** nao e evidencia de que as regras sejam excessivas. Abrir EV-08 com esse fundamento mediria a coisa errada. Abrir a proposta e ato de **DEP-EXE**; nao se usurpa o dono |
| **Achado novo** | O gatilho de R1 confunde *"segunda missao"* com *"segunda missao que toque a materia do contrato"*. Como escrito, produz **falso positivo** em qualquer missao de outro assunto — e produzira de novo. Registrado como achado **DR-1** (§6) |
| Tratamento | **Mantida**, com a medicao registrada e o defeito de criterio escalado |

### 5.4 FIT-2026-004 R2 — gatilho disparado, resultado inconclusivo

| Abstracao | Membros antes | Membros agora | Leitura |
|---|---|---|---|
| Classe `inferred` | 0 | **0** | Inalterada — nenhuma afirmacao sobre o Soberano foi produzida |
| Classe 4 de autoridade | 0 | **0** | Inalterada |
| Os quatro pacotes P1–P4 | 0 consumidores | **0 consumidores** | Os dois primeiros componentes do sistema **nao os consumiram** |

**Por que os componentes nao consumiram os pacotes:** os pacotes recortam
[MEM-EST-0001](../memory/estrategica/MEM-EST-0001-contexto-do-soberano.md), que permanece
`aprovado` e **nao vigente** — exatamente a ressalva **R4** de FIT-2026-004. O gatilho de R2
disparou, mas o teste **nao pode ser executado** enquanto R4 estiver aberta.

> **Achado novo — DR-2.** R2 e R4 estao **acopladas**: R2 nao e avaliavel antes de R4 resolver.
> O gatilho de R2 precisa ser reformulado para *"primeiro componente criado **apos** o registro
> entrar em vigor"*.

**Evidencia parcial, favoravel:** o **mecanismo** dos pacotes — recorte por secao com custo
medido — **foi reusado** nesta missao, em `DEP-QAR §13.2`, `DEP-ENG §13.2` e nas politicas de
contexto de §9.1 das duas Cartas. O mecanismo tem consumidor; **os quatro pacotes especificos,
nao**. A distincao esta registrada porque confundi-las fecharia R2 sem fundamento.

### 5.5 FIT-2026-004 R3 — **fechada**

| Campo | Conteudo |
|---|---|
| Texto da ressalva | *"Quarta missao consecutiva de crescimento, primeira em que **nenhuma ressalva anterior foi fechada**, e primeira em que o **custo de contexto medido subiu**"* |
| Gatilho | *"Proxima mudanca C2/C3: **terceira medicao**. **Se tambem subir**, a serie deixa de ser ruido e vira tendencia — aplicar EV-08 as ressalvas mais antigas"* |
| **Evidencia do fechamento** | Terceira medicao: **30,6%**, contra **33%** na anterior. **Nao subiu.** A condicao explicita que a ressalva fixou para escalar — *"se tambem subir"* — **nao ocorreu** |
| Segundo componente | *"nenhuma ressalva fechada"* — este ciclo **fecha duas** (esta e §5.2) |
| **O que nao fecha com ela** | O **crescimento do acervo**, que continua: esta e a **quinta** missao consecutiva de crescimento. Isso vira ressalva **nova** em FIT-2026-005, com o numero medido — nao se herda a antiga para parecer que o problema sumiu |
| Dono | DEP-EXE |

## 6. Achados

| # | Achado | Severidade | Dono | Gatilho |
|---|---|---|---|---|
| **D1** | `projecao_de` declarado em Carta de Departamento, contra FND-10 §2.2 | Media | DEP-GOV | ✅ **Corrigido nesta revisao** — §0 |
| **DR-1** | **O gatilho de R1 de FIT-2026-004 produz falso positivo.** Como escrito, qualquer missao de outro assunto mede 0 de 28 e satisfaz a condicao de consolidacao | **Media** | DEP-EXE | Proxima missao que registre afirmacao sobre o Soberano, **ou** ato do Soberano sobre MEM-EST-0001 |
| **DR-2** | **R2 e R4 de FIT-2026-004 estao acopladas.** R2 nao e avaliavel enquanto MEM-EST-0001 nao estiver em vigor | **Media** | DEP-GOV | Entrada em vigor de MEM-EST-0001 |
| **DR-3** | **`departments/<dep>` e ambiguo em FND-03 §7.** A arvore canonica nao diz se `<dep>` e o codigo em minusculas *(`qar`)* ou o ID completo *(`dep-qar`)*. Adotou-se o codigo, por LX-01 e pelo padrao `AGT-<DEP>-<papel>` de FND-09 §5.5 — **decisao declarada, nao silenciosa** | Baixa | DEP-GOV | Terceira Carta, ou primeira Carta de agente |
| **DR-4** | **`departments/` nao recebeu indice.** Todo `README.md` de diretorio e um indice (FND-03 §7), mas `DEP` **nao tem sequencia** (§2.3) e a lista dos nove e canonica em FND-02 §2.1 — um indice aqui reproduziria a fonte (PJ-01). **Precedente:** `foundation/templates/` reune 19 templates **sem** README | Baixa | DEP-GOV | Quinta Carta escrita, ou primeira Carta de agente |
| **DR-5** | **O contrato foi validado em 2 de 4 classes.** Comando e Plataforma nao tem piloto; a Carta de DEP-EXE em particular acumula o papel de **autor de todas as Cartas** com o de objeto da propria | Media | DEP-EXE | Primeira Carta de classe Comando ou Plataforma |
| **DR-6** | **A medicao de §13.2 e autorreferente.** O custo do recorte e medido sobre o arquivo que contem a medicao. O metodo adotado — medir, depois substituir o valor **sem alterar o numero de linhas** — mantem o valor valido, mas nao esta escrito em lugar nenhum como regra | Baixa | DEP-KMS | Terceira Carta escrita |
| **DR-7** | **`capabilities/README` nao tinha tabela de Historico de versoes**, exigida por FND-03 §6 para toda mudanca MAIOR ou MENOR | Baixa | DEP-GOV | ✅ **Corrigido nesta revisao** — tabela criada com as duas versoes |
| **DR-8** | **`MEM-APR-0002` declarava `ocorrencias: 2` com **cinco** documentadas.** As ocorrencias 3, 4 e 5 foram registradas em REV-CONSOLIDACAO §0 *(C4, que se declarou expressamente "terceira ocorrencia da familia, **nunca registrada**")*, em REV-SOBERANO *(D8)* e nesta revisao *(D1)*, e **nenhuma chegou ao registro-fonte**. Defeito de propagacao (CV-04), aberto ha **tres** ciclos | **Media** | DEP-KMS | ✅ **Corrigido nesta revisao** — `MEM-APR-0002` **1.1.0**, `ocorrencias: 5`, com a serie de ocorrencias documentada |

**Achados: 9 · corrigidos nesta revisao: 3 · abertos com dono e gatilho: 6 · sem destino: 0.**

> **DR-8 e o achado mais significativo desta revisao, e nao foi encontrado por nenhum cenario.**
> Apareceu na **propagacao obrigatoria aos indices** (CV-04): ao atualizar o indice da camada
> APR, a contagem de ocorrencias de `MEM-APR-0002` nao conferia com o que tres revisoes ja
> haviam documentado. E a mesma familia de defeito que o proprio registro descreve — **segunda
> fonte de verdade** — aplicada, desta vez, **ao registro que a descreve**.

## 7. Varredura C11 — os indices contra as fontes

Acao **C11** de REV-CONSOLIDACAO §10: *"varredura de todos os indices contra as fontes que
projetam, a cada encerramento de C2/C3"*. Dono DEP-GOV.

| # | Indice | Indexa | Conferido contra | Resultado |
|---|---|---|---|---|
| 1 | `README.md` *(raiz)* | o acervo | Contagens de §1.1 e o catalogo mestre | **Atualizado nesta missao** |
| 2 | `foundation/README.md` | `FND` e `TPL` | 10 `FND` + 19 `TPL` em disco | **Conforme, sem alteracao** — nao lista versao de template nem revisao arquitetural; nada a atualizar |
| 3 | `decisions/README.md` | `ADR` | 11 arquivos `ADR-*` | **Atualizado** — ADR-0011, contador **0012** |
| 4 | `rfcs/README.md` | `RFC` | 8 arquivos `RFC-*` | **Atualizado** — RFC-0008, contador **0009** |
| 5 | `capabilities/README.md` | `CAP` | 23 arquivos `CAP-*`; frontmatter conferido campo a campo | **Conforme e ampliado** — §10 |
| 6 | `governance/README.md` | `EXC` `INC` `FIT` | 0 · 2 · 10 | **Atualizado** |
| 7 | `governance/exceptions/README.md` | `EXC` | 0 arquivos | **Conforme** — nenhuma excecao vigente |
| 8 | `governance/incidents/README.md` | `INC` | 2 arquivos | **Conforme** — inalterado por esta missao |
| 9 | `governance/fitness/README.md` | `FIT` | 5 `FIT` + 6 `REV` | **Atualizado** — FIT-2026-005, contador **005**, serie e ressalvas |
| 10 | `governance/artifact-registry.md` | o acervo | Arquivo a arquivo, §8 | **Atualizado** — v1.3.0, baseline `BL-2026-07-28-03` |
| 11 | `memory/README.md` | as 5 camadas | **5** registros — 1 EST + 4 APR | **Atualizado** — MEM-APR-0004 |
| 12 | `memory/aprendizado/README.md` | `APR` | 4 arquivos | **Atualizado** — MEM-APR-0004, contador **0005** |
| 13 | `memory/estrategica/README.md` | `EST` | 1 registro | **Conforme** — inalterado |
| 14 | `memory/produto/README.md` | `PRD` | 0 registros | **Conforme** |
| 15 | `memory/tecnica/README.md` | `TEC` | 0 registros | **Conforme** |
| 16 | `memory/operacional/README.md` | `OPR` | 0 registros | **Conforme** |

**16 indices varridos · 9 atualizados como parte desta mudanca** (IX-02, CV-04).

**Uma divergencia encontrada: DR-8.** O indice da camada APR e o registro-fonte
`MEM-APR-0002` divergiam quanto ao numero de ocorrencias — 2 declaradas, **5** documentadas.
**A varredura preventiva volta a encontrar defeito** depois de um ciclo sem encontrar nenhum, e
o defeito estava aberto ha **tres** ciclos. Corrigido **na fonte**, nunca no indice (PJ-03).

### 7.1 Integridade referencial

| Verificacao | Metodo | Resultado |
|---|---|---|
| Links relativos quebrados | Varredura por ferramenta sobre **todos** os `.md`, resolvendo cada caminho contra o disco | **0 quebrados** em **891** links verificados |
| Vinculo a Capability valido (VC-01) | `capabilities` das duas Cartas conferido contra o catalogo | **8 vinculos**, todos a Capability `ativo` e **nenhuma** `proposta` ou `aposentada` |
| Relacao fora dos pares permitidos (RM-02) | `custodia` DEP→CAP e `exerce` DEP→CAP conferidas contra FND-09 §6.2 | **Conforme.** `DEP → DEP` **nao** foi declarado como relacao — §10.2 do catalogo declara-o expressamente como leitura, nao aresta |
| Ciclo em `depende-de` | Grafo de Capabilities inalterado | **Sem ciclo** — nenhuma Carta de Capability foi tocada |
| Dependencia ascendente (PD-11) | Estrato 3 *(DEP)* → estrato 2 *(CAP)* | **Conforme** — e a direcao permitida |
| Credencial em texto (PI-08, LV-02) | Varredura dos artefatos novos | **0 ocorrencias** |

## 8. Reconciliacao catalogo-fonte

| Verificacao | Resultado |
|---|---|
| Todo artefato novo tem entrada no catalogo mestre (RG-02) | **7 de 7** |
| Todo artefato emendado tem a linha atualizada | **2 de 2** — `TPL-carta-departamento`, `capabilities/README` |
| Contagem do catalogo × contagem em disco | **107 = 107** |
| `MEM-APR-0002` — `ocorrencias` × ocorrencias documentadas | **Divergente: 2 × 5.** Corrigido na fonte — achado **DR-8** |
| Linhas do catalogo × `wc -l` | Conferido arquivo a arquivo |
| Proveniencia | **107 `native`** — nenhum conteudo externo admitido |
| Baseline anterior `BL-2026-07-28-02` editada? | **Nao.** Integridade conferida **antes** de qualquer edicao desta missao |
| Baseline anterior `BL-2026-07-28-01` editada? | **Nao** — preservada desde a emissao |

## 9. Economia de contexto — terceira medicao observada

### 9.1 A serie

| Missao | Natureza | Linhas carregadas | Acervo na baseline vigente | **%** |
|---|---|---|---|---|
| 1.4 | Consolidacao | — | 18.916 | **23%** |
| 1.5 | Construcao sobre a Fundacao | — | 21.318 | **33%** |
| **1.6** | **Construcao de componente** | **7.274** | **23.742** | **30,6%** |

**Metodo:** soma das linhas dos artefatos abertos integralmente com as linhas dos recortes
efetivamente lidos, dividida pelo acervo da baseline **vigente ao inicio** da missao
(`BL-2026-07-28-02`). Medido com `wc -l` e `sed`+`wc -l` (CE-02, CE-04).

| Componente | Linhas |
|---|---|
| **Integrais** — README, FND-01 a FND-05, FND-08, FND-10, 4 templates, catalogo mestre, indice de aptidao, FIT-2026-004, `capabilities/README`, `TPL-carta-departamento` | **5.950** |
| **Recortes** — FND-09 *(482)*, FND-06 *(322)*, ADR-0010 *(83)*, REV-CONSOLIDACAO *(68)*, REV-SOBERANO *(51)*, REV-CAP *(13)*, MEM-EST-0001 *(30, so frontmatter)* | 1.049 |
| **Frontmatter das 23 Cartas de Capability** — 9 campos por Carta | 207 |
| Indices e medicoes por ferramenta | 68 |
| **Total** | **7.274** |

### 9.2 Leitura honesta

**A serie nao sobe — e tambem nao desce.** 23% · 33% · 30,6%. A segunda medicao continua sendo
a mais alta, e a terceira ficou **7,4 pontos acima da primeira**. O que a terceira medicao
autoriza dizer e apenas isto: **a alta de 1.5 nao se confirmou como tendencia**, que era
exatamente a pergunta de R3 de FIT-2026-004.

**O que nao se pode afirmar:** que houve **reducao**. Nenhuma das tres medicoes mostra o custo
caindo, e por isso R4 de FIT-2026-002 permanece aberta.

### 9.3 O que melhorou, e e local

| Pergunta | Antes | Depois |
|---|---|---|
| *"O que DEP-QAR custodia e exerce?"* | Abrir **23** Cartas de Capability e ler `custodio`/`exercentes` — **3.718 linhas** | `capabilities/README §10.1`, **uma linha** da tabela |
| *"DEP-QAR pode verificar isto?"* | **Nao havia fonte** — inferia-se de FND-02 §3 e de tres normas | Recorte de decisao da Carta: **111 linhas**, medido |
| *"DEP-ENG pode adotar esta ferramenta?"* | Cruzar FND-02 §3, FND-09 §8.2 e ADR-0007 | Recorte de decisao: **115 linhas**, medido |
| Carregar as 5 Cartas de Capability de DEP-ENG | 820 linhas, **3,5%** do acervo | Politica de §9.1: carrega-se **a Capability do item**, nao as cinco |

## 10. Achados que geram acao futura

| # | Acao | Quando | Responsavel |
|---|---|---|---|
| **DR-1** | Reformular o gatilho de R1 de FIT-2026-004 para *"segunda missao que toque a materia do contrato"* | Proxima missao que registre afirmacao sobre o Soberano | DEP-EXE |
| **DR-2** | Reformular o gatilho de R2 de FIT-2026-004 para *"primeiro componente criado apos a entrada em vigor do registro"* | Entrada em vigor de MEM-EST-0001 | DEP-GOV |
| **DR-3** | Desambiguar `departments/<dep>` em FND-03 §7 | Terceira Carta, ou primeira Carta de agente | DEP-GOV |
| **DR-4** | Decidir se `departments/` recebe indice | Quinta Carta escrita | DEP-GOV |
| **DR-5** | Exercer o contrato em uma classe **Plataforma** antes de fecha-lo | Primeira Carta apos os pilotos | DEP-EXE |
| **DR-6** | Escrever a regra de medicao autorreferente de secao | Terceira Carta escrita | DEP-KMS |
| **DR-8** | Verificar, a cada `FIT`, se a confirmacao de licao declarada **chegou ao registro-fonte** | A cada Fitness Check que declare confirmacao de `MEM-APR` | DEP-KMS |
| **Herdadas** | C1, C2, C5, C6, C7, C9 de REV-CONSOLIDACAO; A1 a A7 de REV-CAP; M2 a M8 de REV-META; A2, A3, A6 de REV-ARTIFACT; D-* de REV-SOBERANO | Inalteradas | Donos ja fixados |

---

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-QAR | Revisao inicial: 6 cenarios de validacao com 2 correcoes aplicadas antes do encerramento, **9 achados** *(3 corrigidos)*, reconciliacao das 12 ressalvas abertas com **2 fechamentos**, varredura C11 dos 16 indices com **1 divergencia encontrada e corrigida na fonte**, 0 links quebrados em **891**, terceira medicao observada de contexto. Verificacao dos blocos impedidos por **DEP-GOV**, com desvio declarado. |
