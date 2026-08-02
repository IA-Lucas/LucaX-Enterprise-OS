---
id: REV-ESTRUTURAL-I-2026-07-28
titulo: Primeira Revisao Estrutural do LucaX Enterprise OS
tipo: fitness
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-QAR
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0010, ADR-0011, ADR-0012]
substitui: []
substituido_por: null
objeto_avaliado: [FND-01, FND-02, FND-03, FND-04, FND-05, FND-06, FND-07, FND-08, FND-09, FND-10, IDX-capabilities, artifact-registry, MSG-2026-0002, DEP-EXE, DEP-KMS, DEP-QAR, DEP-ENG, MEM-EST-0001]
classe_avaliacao: corretude
resumo: Executa o rito de FND-02 §9.4 sobre a Fundacao, as 23 Capabilities, as 21 entidades, os 33 tipos e as 4 classes de Departamento, reconcilia todas as ressalvas abertas e produz o mapa unico de bloqueios.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# REV-ESTRUTURAL-I — Primeira Revisao Estrutural

## Proposito
Executar o rito de **revisao estrutural periodica** de
[FND-02 §9.4](02-estrutura-organizacional.md) — o primeiro do sistema —, determinado pelo
**ato soberano de 2026-07-28**, e produzir o **mapa unico de bloqueios** que decide se a
arquitetura esta apta ao rollout das cinco Cartas restantes.

> **Esta revisao consolida e corrige. Nao expande a organizacao.** Nenhuma Carta nova, agente,
> skill, comando, workflow, produto, codigo, infraestrutura, ontologia ou framework foi criado.

## Escopo
| Item | Definicao |
|---|---|
| Inclui | Os **10** documentos fundacionais · **23** Capabilities · **21** entidades · **33** tipos documentais · as **4** classes de Departamento e as relacoes **exercidas** · **todas** as ressalvas e achados abertos · o ato soberano de 2026-07-28 · `RFC-0009` e `ADR-0012` |
| **Nao** inclui | **Aptidao evolutiva** — objeto de [FIT-2026-007](../governance/fitness/FIT-2026-007-revisao-estrutural-i.md), obrigatorio por FND-02 §9.4. O **merito** do ato soberano. O **LucaX Legacy**, nao consultado (ADR-0007 §5.1) |
| Rito aplicado | **FND-02 §9.4** — o que ja existia. Nenhum rito novo foi desenhado |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| **Forma** | **DEP-GOV** | FND-02 §9.4, literal |
| **Merito** | **DEP-EXE** | FND-02 §9.4, literal |
| **Evidencia da memoria** | **DEP-KMS** | FND-02 §9.4, literal |
| **Revisao independente** | **DEP-QAR** | AC-03, RM-06b — **unico departamento que nao produz esta revisao** |
| **Aprova** | **DEP-QAR** | **Desvio declarado** — §0.1 |

### 0.1 Nota de conflito de interesse (PI-10)

| Campo | Conteudo |
|---|---|
| **Fato estrutural** | FND-02 §9.4 torna a revisao estrutural um produto **tri-departamental**: GOV *(forma)*, EXE *(merito)*, KMS *(evidencia)*. **Sobra exatamente um** departamento que nao a produz: **DEP-QAR** |
| Consequencia | DEP-QAR e, ao mesmo tempo, o **unico revisor independente possivel** e o **unico aprovador possivel**. A matriz de FND-09 §8.2 daria a aprovacao a **DEP-EXE**, que esta impedido por ter contribuido o merito (PI-05, `DEP-EXE §10, I-2`) |
| **Residuo** | DEP-QAR revisa e aprova o mesmo documento. **Nao ha alternativa disponivel na estrutura atual** |
| Alternativa avaliada e **recusada** | Escalar a aprovacao ao **SOBERANO**. Recusada porque o Soberano **determinou** esta revisao: aprova-la seria aproximar determinante e aprovador, o mesmo defeito de PI-05 que se pretende evitar. A recusa fica registrada para ser auditavel |
| Mitigacao aplicada | **DEP-QAR nao produziu nenhum artefato avaliado** e nao participou da redacao. `FIT-2026-007` tem objeto **distinto** desta revisao e aprovador **distinto** (DEP-GOV) |
| **Quando desaparece** | Quando **DEP-GOV** tiver Carta *(IC-4)* e quando existirem **agentes** *(IC-3)*. Antes disso, nao desaparece |
| Achado gerado | **RE-03** — §9 |

---

## 1. Verificacao independente do ato soberano

O ato de 2026-07-28, seu alcance, seus tres hashes por artefato, as **nove** verificacoes da
condicao de eficacia e o **teste de reconstrucao** vivem em
[**MSG-2026-0002**](../memory/operacional/MSG-2026-0002-ato-soberano-cartas-comando-plataforma-e-contexto.md)
— **fonte canonica unica**. Esta secao **nao os reproduz** (CM-09, PJ-01); registra apenas o
que a revisao verificou de forma independente.

| # | O que foi verificado aqui | Resultado |
|---|---|---|
| 1 | O objeto do ato e **univocamente determinavel**, apesar da designacao imprecisa do pacote | **Sim** — §1.2 daquela Diretiva; achado **RE-01** |
| 2 | Os efeitos aplicados correspondem **exatamente** ao que o ato determina, sem excesso | **Sim** — 3 ratificacoes, 2 acolhimentos, 1 encerramento, 1 determinacao. **Nenhum efeito alem** |
| 3 | Nenhum artefato **excluido** pelo ato foi alcancado | **Sim** — `DEP-QAR` 1.1.0 permanece proposta; `ADR-0012` e `RFC-0009` sao `nao-exigida` **por classe**, nao por suprimento |
| 4 | O ato **nao** foi usado para fechar divida que ele nao alcanca | **Sim** — §4 daquela Diretiva separa o que foi resolvido, o que foi contido e o que nao foi tocado |
| 5 | Autoverificacao | **0 ocorrencias.** DEP-QAR e DEP-GOV verificam; DEP-EXE e DEP-KMS produziram |

## 2. Integridade de ratificacao — a ambiguidade resolvida

> **A pergunta que a Missao 1.7 deixou aberta:** o ato ratifica o **arquivo completo**, o
> **conteudo normativo** ou a **versao**?

**Resposta institucionalizada:** o **conteudo normativo**, medido por **H-N**, com lista
fechada de metadados mutaveis — [ADR-0012 §5.1](../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md),
regras `IR-01` a `IR-12`, propostas por [RFC-0009](../rfcs/RFC-0009-integridade-e-alcance-do-ato-de-ratificacao.md).

### 2.1 Por que as outras duas respostas quebram

| Resposta | Onde quebra | Consequencia se adotada |
|---|---|---|
| **Arquivo completo** | A operacao **O4**, que a propria ratificacao obriga a executar, altera o arquivo | A ratificacao seria **autodestrutiva**: aplica-la invalidaria a prova dela |
| **Versao** | Transicao de estado, `C0` e ajuste de redacao **nao incrementam versao** (ADR-0009) | Alteracao nao submetida **pareceria ratificada** — exatamente o que o ato manda impedir |
| **Conteudo normativo** | — | H-N **invariante sob O4**; qualquer alteracao fora da lista fechada muda H-N e abre incidente (IR-05) |

### 2.2 Verificacao executada — a prova que faltava

| Campo | Conteudo |
|---|---|
| Metodo | **IR-09.** Sobre `DEP-QAR` e `DEP-ENG` — ratificadas e transicionadas na Missao 1.7 —, reverteu-se **apenas** `status` e `ratificacao`, e mediu-se o SHA-256 do texto reconstruido |
| `DEP-QAR` | Reconstruido = **`fa07f55f…f286`** = hash do ato — **identico** |
| `DEP-ENG` | Reconstruido = **`57aebf81…1a48`** = hash do ato — **identico** |
| **O que fica provado** | Que a **unica** diferenca entre o texto ratificado pelo Soberano e o arquivo em disco sao **exatamente os dois campos de ciclo de vida**. Byte a byte. **Nenhuma alteracao pos-ato ocorreu**, nem de corpo, nem de espaco, nem de qualquer outro campo |
| Limite superado | `MSG-2026-0001 §4.1` declarava que a impressao digital **nao detecta edicao que preserve o numero de linhas**. **IR-09 detecta** — e o detectaria mesmo que a edicao preservasse tudo menos um byte |

### 2.3 O que **nao** foi resolvido, e por que

| Questao | Estado | Motivo |
|---|---|---|
| **IC-2** — colisao do termo *"ratifica"* em FND-01 §7.3 | **ABERTO.** **Contido**, nao fechado | Corrigir e emenda **C3** a Constituicao, que exige ratificacao do Soberano. O ato de 2026-07-28 **nao ratifica ADRs novos**. Contencao imediata em `IR-11`: nenhum artefato novo registra *"ratificado por"* nome que nao seja o SOBERANO; o termo oficial e **homologacao** |
| **G1/G2** — FND-10 §2.2 × §10.3 sobre `FIT` | **ABERTO.** **Migrado**, nao resolvido | Emendar reduziria o que chega ao Soberano; o rito C2 nao deve faze-lo sozinho (PI-01). Migrado para **Q2 de RFC-0009**, escalada |

> **Condicao 3 do rollout de FIT-2026-006 e satisfeita na forma *"formalmente adiado"* — nao na
> forma *"resolvido"*.** A propria condicao admite as duas; registrar qual delas ocorreu e a
> diferenca entre divida tratada e divida renomeada.

## 3. O rito de FND-02 §9.4 executado

### 3.1 Gatilhos de especializacao — §9.2

| Gatilho | Sinal observavel? | Evidencia | Movimento |
|---|---|---|---|
| **Escopo heterogeneo** | **SIM** | `CAP-governanca` cobre **sete** responsabilidades exclusivas distintas de DEP-GOV (FND-02 §3), e DEP-GOV custodia **1** Capability que **verifica as outras 22** — achado **P7** | **Proposta obrigatoria.** Ver §3.5 |
| **Fronteira em disputa** | **PARCIAL** | **P2** — dono de camada × exercente de `CAP-conhecimento`; **P3, P4, P5** — divergencias aparentes em portoes, seguranca e comunicacao. Nenhuma produziu **conflito real registrado** | Redesenho **nao** justificado; as quatro sao **divergencia de leitura**, resolvidas em §3.6 |
| **Duplicacao** | **NAO** | Toda exibicao de conteudo alheio esta declarada como projecao (7 declaracoes verificadas em §11) | — |
| **Contexto excessivo** | **NAO** | Piso obrigatorio **inalterado** em 1.099 linhas; recorte de decisao de Carta entre 111 e 155 linhas | — |
| **Gargalo de decisao** | **SIM** | **DEP-EXE** e autor de 4 de 4 Cartas, aprova `FIT`, abre EV-08, decide rollout e da o merito desta revisao. Impedido em **tres** dos cinco atos, sem substituto na **autoria** (IC-3) | **Proposta obrigatoria.** Ver §3.5 |
| **Carga concentrada** | **SIM** | Mesmo fato acima. **VC-03** dispara em DEP-ENG *(5 Capabilities)* e DEP-EXE *(4)* — achado **P6** | §3.5 |
| **Conhecimento ilhado** | **SIM** | *"Um resultado so sai bem quando um papel especifico atua"* — **quatro** Cartas, **um** autor | §3.5 |

### 3.2 Gatilhos de consolidacao — §9.3

| Sinal | Observado? | Evidencia |
|---|---|---|
| Componente sem acionamento ao longo de um **horizonte inteiro** | **NAO AVALIAVEL** | **Nenhum horizonte se fechou.** O criterio exige horizonte fechado, e o sistema nao produziu nenhum. Registrado como o **defeito central do gatilho** — §8 |
| Duas areas que **sempre** atuam juntas e nunca isoladas | **NAO** | `DEP-KMS` + `DEP-TLS` e a unica fusao que nenhuma norma proibe *(IC-7)*, e falta **sinal**: DEP-TLS nao tem Carta e nao registrou nenhum ato |
| Handoff que so transporta | **NAO** | **Zero** instancias do tipo `Handoff` no acervo |
| Custo de coordenacao maior que o ganho declarado | **NAO MEDIDO** | Nao ha metrica de custo de coordenacao. Declarado como ausencia, nao como negativo |

### 3.3 Necessidade, autoridade, sobreposicao, ciclos e dependencias

| Verificacao | Metodo | Resultado |
|---|---|---|
| **Capability sem custodio** (OW-03) | Projecao §10.1 de `capabilities/README` contra as 23 Cartas | **0** |
| **Custodia dupla** (OW-01) | idem | **0** |
| **Capability sem exercente** | idem | **0** |
| **Departamento sem custodia** | idem | **0** — os 9 custodiam |
| **Ciclo em `depende-de`** | Grafo das 23 Capabilities, §4 do catalogo | **Sem ciclo** |
| **Dependencia ascendente** (PD-11) | Estrato 3 `DEP` → estrato 2 `CAP` | **Conforme** |
| **Relacao fora dos pares permitidos** (RM-02) | `custodia` e `exerce` DEP→CAP contra FND-09 §6.2 | **Conforme.** `DEP → DEP` **nao** declarada |
| **Autoridade conforme FND-09 §8.2** | Cada ato desta missao contra a matriz | **Conforme**, com **2** desvios declarados: aprovacao desta revisao (§0.1) e de `FIT-2026-007` |
| **Sobreposicao de escopo entre departamentos** | FND-02 §3 contra a projecao §10.1 | **0 sobreposicoes de custodia.** **1** exercicio compartilhado declarado: `CAP-comunicacao` (EXE + KMS), que e o **unico membro de OW-02** |

### 3.4 As quatro classes de Departamento e as relacoes **exercidas**

| Classe | Carta | Estado apos o ato | Relacoes exercidas |
|---|---|---|---|
| **Comando** | `DEP-EXE` | **`ativo` · ratificada** | `custodia` ×4 · `exerce` ×4 · autoridade sobre Linha e Plataforma |
| **Guarda** | `DEP-QAR` | `ativo` · ratificada | `custodia` ×3 · `exerce` ×3 · `verifica` |
| **Guarda** | `DEP-GOV` | **SEM CARTA** | `custodia` ×1 · `verifica` ×22 · unico escritor de EST — **exercidos 5 vezes sem Carta** |
| **Linha** | `DEP-ENG` | `ativo` · ratificada | `custodia` ×5 · `exerce` ×5 |
| **Plataforma** | `DEP-KMS` | **`ativo` · ratificada** | `custodia` ×2 · `exerce` ×3 — **unica linha "exerce sem custodiar"** |

**As quatro classes estao exercidas e, pela primeira vez, as quatro tem ao menos uma Carta em
vigor.** O sistema passa de **2** para **4** artefatos `DEP` em vigor.

### 3.5 Produto do rito: **registro fundamentado**, nao proposta de especializacao

FND-02 §9.4 admite tres produtos. Quatro gatilhos de especializacao dispararam, e **todos
apontam para o mesmo objeto**: a concentracao em **DEP-EXE**.

| Campo | Conteudo |
|---|---|
| **Movimento tipico** que o gatilho sugere | *"Promover funcao a agente"* e *"devolver direito de decisao"* (FND-02 §9.2) |
| **Por que nao e executado agora** | **Promover funcao a agente exige criar agente**, expressamente proibido nesta missao e sem sinal proprio. **Devolver direito de decisao** exige alterar `FND-09 §8.2` — **C3**, sem ato do Soberano |
| **Decisao** | **MANTER**, com fundamento e custo declarado. FND-02 §9.2 exige *"executa-la, seja para registrar por escrito a decisao de adia-la"*; este e o **registro por escrito** |
| **Custo assumido** | A concentracao permanece. Enquanto DEP-EXE for autor unico, **R1 de FIT-2026-006 nao pode fechar** e o contrato de Carta continua sem teste contra autor distinto |
| **Gatilho de reexecucao** | **Existencia do primeiro agente**, ou resolucao de **IC-3** — o que vier antes |
| Dono | **DEP-EXE**, com parecer de DEP-GOV |

> **Primeira das tres.** FND-02 §9.4: *"revisao que conclui 'manter tudo' tres vezes seguidas e
> sinal de analise complacente e escala ao Soberano"*. **Esta e a 1a de 3** — e **nao** conclui
> *"manter tudo"*: fecha **8** ressalvas e achados com evidencia (§5) e corrige **IC-8** (§4).
> O contador fica registrado para que a terceira nao passe despercebida.

### 3.6 As quatro divergencias aparentes — P2, P3, P4, P5

Gatilho **disparado** nas quatro: *"1a revisao estrutural"*.

| # | Pergunta | **Resolucao** | Efeito |
|---|---|---|---|
| **P2** | Ser **dono de camada** de memoria e exercer `CAP-conhecimento`? | **NAO.** `FND-06 §2.1` atribui **custodia de conteudo** por camada; `CAP-conhecimento` e a competencia de **persistir e devolver o que se sabe**. Sao coisas distintas: DEP-GOV e dono da camada EST e **nao** persiste nem devolve — quem o faz e **DEP-KMS**, o curador. **O catalogo esta correto**; faltava a leitura escrita | **FECHADO.** Nenhuma Carta de Capability alterada (PJ-03) |
| **P3** | DEP-GOV colibera QG-2 e QG-6 sem constar como exercente de `CAP-qualidade`? | **Coliberar portao nao e exercer a Capability.** DEP-GOV libera pela **forma** (`CAP-governanca`), DEP-QAR pelo **merito** (`CAP-qualidade`). Duas competencias, um portao — e exatamente o desenho que ADR-0005 protege ao proibir autoverificacao | **FECHADO** |
| **P4** | DEP-TLS gere acesso e segredo, DEP-OPS verifica backups — sem constar em `CAP-seguranca`? | **Operar sob politica nao e custodiar a politica.** `CAP-seguranca` e definir e verificar; executar a rotina sob ela e `CAP-infraestrutura` e `CAP-operacoes`. FND-02 §3 diz *"por referencia"* — e a referencia e a politica de DEP-QAR | **FECHADO** |
| **P5** | DEP-GOV guarda o **formato** da comunicacao sem ser exercente de `CAP-comunicacao`? | **Guardar a forma de um artefato e `CAP-governanca`**, nao `CAP-comunicacao`. Mesma distincao de P3, aplicada a outro objeto | **FECHADO** |

> **As quatro fecham pelo mesmo mecanismo, e isso e o achado.** Nenhuma era divergencia de
> **dado**: as quatro eram **ausencia de uma distincao escrita** entre *deter a competencia* e
> *operar sob ela*. **Zero Cartas alteradas**; a correcao foi escrever a leitura, nao mudar a
> fonte — e e a aplicacao literal de **PJ-03**. Registrado como aprendizado em §10 de
> `FIT-2026-007`.

## 4. IC-8 resolvido — a aritmetica dos 33 tipos, a partir da fonte

> **A pergunta:** *"Memoria &lt;camada&gt;"* e **um** tipo parametrizado ou **cinco**? E
> *"Diretiva / Consulta / Alerta"*, **um** ou **tres**?

**Regra aplicavel — CS-02** ([FND-10 §3.2](10-artifact-framework.md)): *"dois tipos
documentais da mesma entidade diferem por **finalidade, conteudo permitido ou autoridade** —
nunca apenas por nome"*.

| Candidato | Diferem por que? | Veredito |
|---|---|---|
| **Memoria EST · PRD · TEC · OPR · APR** | **Autoridade** — escrita em EST **sempre exige ADR** (FND-06 §3.1, MI-04), OPR **expira por padrao**. **Conteudo permitido** — FND-06 §3 fixa conteudo distinto por camada | **CINCO tipos.** Nao sao sinonimos |
| **Diretiva · Consulta · Alerta** | **Finalidade** — *determinar* · *obter parecer* · *comunicar risco*, declaradas na propria linha de FND-10 §4.6 | **TRES tipos** |
| ~~**Norma Derivada**~~ | **Recusada** em FND-10 §4.8, ao lado de Command, Prompt, Playbook, Checklist e Evaluation — **nenhum dos quais conta** | **NAO conta.** E slot nomeado, nao tipo declarado |

### 4.1 A conta que fecha

| Classe | Tipos | Verificacao |
|---|---|---|
| Normativa | **4** | Constituicao · Documento Fundacional · Meta Model · Framework. *(Norma Derivada recusada, §4.8)* |
| Decisoria | **5** | — |
| Constitutiva | **7** | — |
| Executavel | **4** | — |
| Avaliativa | **2** | — |
| **Cognitiva** | **10** | Memoria ×5 + Handoff + Reporte + Diretiva/Consulta/Alerta ×3 |
| Registro | **1** | — |
| **Total** | **33** | **4+5+7+4+2+10+1 = 33** — reproduz **exatamente** FND-10 §4 |

**Nenhuma emenda a FND-10 e necessaria. Nenhuma entidade foi inventada.** A fonte sempre
esteve certa; a **projecao** do catalogo estava errada em **dois** pontos que se mascaravam:
contava **5** na Normativa *(incluindo a recusada)* e **9** na Cognitiva *(faltando um)*.

### 4.2 Duas divergencias adicionais, encontradas ao fechar a conta

| # | Divergencia | Correto | Acao |
|---|---|---|---|
| **RE-04** | `artifact-registry §2` declara **16 de 33** tipos com instancia; **§5 do mesmo catalogo** declara **17**. O mesmo documento diverge de si proprio | **16** — contado tipo a tipo: 4+3+2+1+2+3+1 | Corrigido no catalogo |
| **RE-05** | `artifact-registry §2` declara **11 de 21** entidades instanciadas; a enumeracao lista **10** | **10** — `FND` `ADR` `RFC` `INC` `FIT` `CAP` `DEP` `TPL` `MEM` `MSG`. **`ORG` e `SOBERANO` nao podem ter instancia de artefato**: sao as duas unicas entidades **fora do arquetipo A2** (FND-09 §4.2) | Corrigido no catalogo |

> **RE-05 e o unico exercicio discriminante de A2 encontrado no acervo** — e nasceu de tentar
> fechar uma soma. Ver §5, FIT-2026-001 R3.

> **Terceira missao seguida em que o defeito de maior alcance vem de executar a propagacao, e
> nao de auditar.** DR-8 veio da propagacao aos indices; IC-1, de abrir o template; IC-8, de
> somar a tabela; **RE-04 e RE-05, de fechar a soma que IC-8 abriu**. O ponto cego e o mesmo:
> **a auditoria confere projecao contra fonte, e nao confere a fonte contra si mesma.**

## 5. Mapa unico de bloqueios — reconciliacao de **todas** as ressalvas e achados

> **Tres estados sao distinguidos, e a distincao e o produto principal desta secao:**
> **RESOLVIDA** — a condicao foi satisfeita e ha evidencia · **RECLASSIFICADA** — mudou o
> estado do julgamento, **nao** o do objeto · **MANTIDA** — segue aberta, com dono, gatilho e
> custo. **Nenhuma ressalva foi fechada por reformulacao de texto.**

### 5.1 Ressalvas de aptidao — 17 abertas na entrada

| Origem | Gatilho disparou? | **Estado de saida** | Evidencia / motivo |
|---|---|---|---|
| **FIT-2026-001 R1** — acrescimo do Meta Model sem proporcao comprovada | **Sim** — 1a revisao estrutural | ✅ **RESOLVIDA** | Condicao literal: *"se **nenhum Framework** tiver sido construido sobre o Meta Model, aplicar EV-08"*. **FND-10 foi construido sobre ele** — §4 mapeia os 33 tipos as 21 entidades por CS-01, e ADR-0011 consome §8.2. A condicao **nao** se verifica |
| **FIT-2026-001 R3** — arquetipo A2 reune 19 de 21 e nunca discriminara | **Sim** | ✅ **RESOLVIDA** | Condicao: *"se A2 nao tiver sido invocado para decidir nenhum caso"*. **Foi invocado em dois casos registrados:** recusa da entidade *"Artifact"* (FND-10 §3.3) e, agora, **RE-05** — a exclusao de `ORG` e `SOBERANO` e a razao pela qual a contagem de entidades instanciadas e 10, e nao 21. **Consolidar A2 apagaria a distincao que acabou de corrigir o catalogo** |
| **FIT-2026-002 R1** — 40 regras novas, nenhuma exercida | **Sim** | ✅ **RESOLVIDA** | Condicao: *"aplicar EV-08 a FND-10 **se nenhum artefato tiver sido criado sob o contrato**"*. **Cinco** artefatos nascem sob o contrato so nesta missao, e todos os de 1.6 e 1.7 tambem. A condicao **nao** se verifica |
| **FIT-2026-002 R3** — classe M3 com um unico membro | **Sim** | ✅ **RESOLVIDA** | Condicao: *"se continuar com um membro **e sem uso**"*. **M3 tem uso intenso e decisivo:** a regra *"nunca editar a fonte para caber no indice"* **decidiu IC-8, RE-04 e RE-05** — tres correcoes feitas na vista derivada, com **zero** alteracoes na fonte. Um membro, **muito** usado |
| **FIT-2026-002 R4** — reducao de contexto calculada, nao observada | **Sim** | 🟡 **MANTIDA, com o criterio ENDURECIDO** | A 5a medicao **SOBE**: **21,3%** contra 18,5%. E, por ser **a primeira com composicao itemizada**, revelou que **a serie nunca foi comparavel** — achado **RE-08**. O criterio passa a exigir **duas descidas consecutivas com composicao declarada**. [FIT-2026-007 §F5.1](../governance/fitness/FIT-2026-007-revisao-estrutural-i.md). Dono **DEP-KMS** |
| **FIT-2026-003 R1** — 10 regras de fronteira sem exercicio | **Nao** — gatilho e a **2a** revisao estrutural | 🟡 **MANTIDA** | Gatilho intacto. Dono DEP-EXE |
| **FIT-2026-003 R2** — portao de admissao com zero membros | **Nao** — gatilho e o 1o candidato do Legacy | 🟡 **MANTIDA** | Nenhum candidato. Dono DEP-GOV |
| **FIT-2026-004 R1** — 28 regras `CT` sem exercicio | **Sim** — 1a missao a tocar a materia **com o registro em vigor** | ✅ **RESOLVIDA** | **13 de 28 exercidas** nesta missao — **46,4%**, contra o limiar de **um terco (33,3%)**. A condicao de abertura de EV-08 **nao** se verifica. Medicao regra a regra em §10.1 |
| **FIT-2026-004 R2** — tres abstracoes com zero membros | **Nao** — gatilho e *"1o componente criado apos a vigencia"*, e **nenhum componente foi criado** | 🔁 **RECLASSIFICADA** | **Muda o motivo da nao-avaliacao, nao o resultado.** Sai de `nao-avaliavel por registro inativo` *(Correcao 2)* e volta a **aberta, aplicavel, gatilho nao disparado**. **Isto nao e progresso** — §10.2 |
| **FIT-2026-004 R4** — MEM-EST-0001 nao esta em vigor | **Sim** — ato do Soberano | ✅ **RESOLVIDA** | `MEM-EST-0001` **`ativo` · `ratificada`**, com as **11 `unknown`** intactas (V9 de MSG-2026-0002) |
| **FIT-2026-005 R1** — 10 regras `DC` exercidas por construcao | **Nao** — exige autor distinto de DEP-EXE | 🟡 **MANTIDA** | Nenhuma Carta escrita nesta missao. Gatilho intacto |
| **FIT-2026-005 R3** — 5o ciclo de crescimento | **Sim** — encerramento de EV-08 | 🟡 **MANTIDA e ESCALADA** | EV-08 encerrada como **AJUSTAR** (§8), **sem nenhum artefato fundido**. A propria ressalva manda **escalar ao Soberano** nesse caso — §5.4 |
| **FIT-2026-005 R5** — 1a revisao estrutural nao agendada | **Sim** | ✅ **RESOLVIDA** | **A 1a revisao estrutural foi determinada pelo Soberano e esta executada** — este documento. **Doze** itens que dependiam dela foram destravados |
| **FIT-2026-006 R1** — DEP-EXE autor de 4 de 4 | **Nao** | 🟡 **MANTIDA** | Reforcada por §3.5: quatro gatilhos de especializacao apontam para o mesmo objeto |
| **FIT-2026-006 R2** — 5 de 9 sem Carta, um deles DEP-GOV | **Nao** — nenhuma Carta escrita | 🟡 **MANTIDA e AGRAVADA** | DEP-GOV exerceu os dois papeis criticos **pela 5a vez** sem Carta, e **produziu esta revisao**. Ver IC-4 em §6 |
| **FIT-2026-006 R3** — 6o ciclo de crescimento | **Sim** | 🟡 **MANTIDA e ESCALADA** | **7o ciclo.** Mesma escalada de R3 — §5.4 |
| **FIT-2026-006 R4** — DEP-QAR retem IC-5 | **Sim** — P4 tratada | 🟡 **MANTIDA** | **Pacote de emenda 1.1.0 pronto e hasheado** (§7). **Nao ativado** — o ato exclui expressamente. Aguarda ato novo |

**Resultado: 7 RESOLVIDAS com evidencia · 1 RECLASSIFICADA · 9 MANTIDAS · 0 sem destino.**

### 5.2 Achados de revisao e de projecao

| Origem | Achado | Gatilho | **Estado de saida** |
|---|---|---|---|
| `capabilities` **P1** | OW-02 com um unico membro | **Sim** | 🟡 **MANTIDO.** Continua com **1** membro — `CAP-comunicacao`, agora declarado nas duas Cartas. Um membro **exercido** e melhor que zero, e nao chega a dois (AQ-03) |
| `capabilities` **P2 · P3 · P4 · P5** | Divergencias aparentes | **Sim** | ✅ **FECHADOS** — §3.6, os quatro pelo mesmo mecanismo |
| `capabilities` **P6** | VC-03 dispara em ENG e EXE | **Sim** | 🟡 **MANTIDO.** Avaliado em `DEP-EXE §12.1`, decisao de **nao dividir** com custo declarado; reforcado por §3.5 |
| `capabilities` **P7** | Assimetria de custodia de DEP-GOV | **Sim** | 🟡 **MANTIDO e QUALIFICADO.** Gatilho de **escopo heterogeneo** confirmado (§3.1). Resolucao depende da **Carta de DEP-GOV** — IC-4 |
| `capabilities` **P8** | EXE ↔ GRW e ENG ↔ TLS mutuamente expostos | **Nao** — gatilho e a **2a** revisao | 🟡 **MANTIDO** |
| **IC-2** | Colisao do termo *"ratifica"* | **Sim** | 🟠 **CONTIDO, NAO FECHADO** — §2.3. Contencao `IR-11`; correcao exige **C3** |
| **IC-3** | Impedimento sem substituto na proposicao | **Nao** — exige agentes | 🟡 **MANTIDO** |
| **IC-4** | DEP-GOV com dois papeis criticos sem Carta | **Sim** | 🟡 **MANTIDO e DECIDIDO** — §6.1 |
| **IC-5** | Materia de I-6 de DEP-QAR nomeia so a Linha | **Sim** | 🟠 **EMENDA PRONTA, NAO ATIVADA** — §7 |
| **IC-6** | Fronteira defeito × violacao vive so em REV-INTERCLASSES | **Nao** — exige 3o caso | 🟡 **MANTIDO** |
| **IC-7** | Fusao KMS+TLS e a unica sem vedacao | **Sim** — 1a revisao estrutural | ✅ **FECHADO.** Testada em §3.2: **sem sinal**. DEP-TLS nao tem Carta e nao registrou nenhum ato. *"Sem vedacao"* e *"sem sinal"* permanecem distintos e agora estao **medidos** |
| **IC-8** | Divergencia aritmetica do catalogo §5 | **Sim** | ✅ **FECHADO** — §4, a partir da fonte, **sem emendar FND-10** |
| **DR-4** | `departments/` sem indice | **Nao** — gatilho e a **quinta** Carta; ha **quatro** | 🟡 **MANTIDO** |
| **DR-8** | Licao declarada que nao chega ao registro-fonte | **Sim** — a cada `FIT` | 🟡 **MANTIDO e materializado** como criterio de QG-5 (`DEP-KMS §5.2`); **aplicado** nesta missao — §11 |
| **C5** de REV-CONSOLIDACAO | Impedimento cruzado | **Sim** — **3a ocorrencia** | 🟡 **MANTIDO e AGRAVADO.** 3a ocorrencia registrada (§0.1). Dono DEP-GOV |
| **G1/G2** de INC-2026-002 | FND-10 §2.2 × §10.3 | **Sim** | 🔀 **MIGRADO, NAO RESOLVIDO** → **Q2 de RFC-0009**, aberta |

### 5.3 Achados novos desta revisao

Registrados em §9: **RE-01** a **RE-06**.

### 5.4 Escalada ao SOBERANO — uma unica pendencia

> **R3 de FIT-2026-005 e R3 de FIT-2026-006 determinam a mesma escalada, pelo mesmo fato.**
> Escalam-se **como uma**, para nao inflar a contagem de pendencias (LM-06).

| Campo | Conteudo |
|---|---|
| **PS-1** | **Setimo ciclo consecutivo de crescimento do acervo, e a primeira proposta de consolidacao encerrou sem fundir, aposentar ou dividir nenhum artefato** |
| Fato medido | Crescimento em [FIT-2026-007 §F1](../governance/fitness/FIT-2026-007-revisao-estrutural-i.md). **Consolidacoes executadas em 7 ciclos: 0** |
| Por que escala | As duas ressalvas determinam, **literalmente**, escalar se EV-08 fechar sem nada consolidado. **Fechou** — como **AJUSTAR** (§8) |
| **O que NAO se pede** | Nao se pede autorizacao para consolidar. **Nao ha objeto consolidavel elegivel** — §8.2 demonstra os quatro candidatos, um a um |
| **O que se pede** | Decisao sobre **o proprio criterio**: EV-08 exige *"horizonte inteiro sem instancia"*, e **nenhum horizonte se fechou em sete ciclos**. Ou **(a)** o Soberano fixa o que fecha um horizonte; ou **(b)** aceita que EV-08 permaneca inaplicavel por tempo indeterminado, com a divida declarada; ou **(c)** determina outro criterio |
| Dono | DEP-EXE com DEP-GOV; **decisao: SOBERANO** |

> **Esta e a unica pendencia escalada.** As quatro de FIT-2026-006 — P1 a P4 — foram
> **respondidas pelo ato de 2026-07-28**. As duas questoes de RFC-0009 *(Q1 e Q2)* ficam
> registradas como **abertas na RFC**, com dono e gatilho; nao sao reescaladas aqui para nao
> criar segunda fonte da mesma pergunta (MM-01).

## 6. IC-4 — a Carta de DEP-GOV bloqueia o rollout?

### 6.1 Decisao

| Pergunta | **Resposta** | Fundamento |
|---|---|---|
| A ausencia de Carta de DEP-GOV **bloqueia** o rollout das cinco restantes? | **NAO** | A autoridade de DEP-GOV nao deriva da Carta: deriva de **FND-02 §3** e da matriz de **FND-09 §8.2**, ambas vigentes e ratificadas. Carta **declara** autoridade; nao a **constitui** (ADR-0011 §5.3, DC-01) |
| Entao qual e o efeito de IC-4? | **ORDENA** o rollout, e nao o interrompe | O residuo e de **segregacao**, nao de autoridade: DEP-GOV revisa toda Carta e escreve sozinho em EST **sem ter declarado seus proprios impedimentos** |
| **Prioridade** | **MAXIMA — a quinta Carta e a de DEP-GOV, escrita sozinha** | Confirma a **Condicao 1** de FIT-2026-006, agora com fundamento medido: **5a ocorrencia** do exercicio sem Carta, e **1a vez** que DEP-GOV produz uma revisao estrutural |
| **Condicao adicional** | A Carta de DEP-GOV deve declarar, em **B9**, o impedimento que esta revisao expos: **revisar Carta de departamento de cuja revisao estrutural DEP-GOV foi autor** | §0.1, achado **RE-03** |

> **Por que nao bloqueia — e por que a distincao importa.** Declarar bloqueio faria a
> organizacao parar por um documento que **nao cria nenhuma autoridade nova**. Declarar que
> nao ha problema esconderia um residuo que ja tem **cinco** ocorrencias. A resposta correta
> nao e nem uma nem outra: **nao bloqueia, e e a proxima**.

### 6.2 IC-8 — resolvido em §4

`Memoria <camada>` sao **cinco** tipos; `Diretiva/Consulta/Alerta` sao **tres**; `Norma
Derivada` **nao conta**. Total **33**, identico a FND-10 §4. **Catalogo e projecoes corrigidos;
nenhuma entidade inventada; nenhuma emenda a FND-10.**

## 7. P4 — pacote de ratificacao da emenda `DEP-QAR` 1.1.0

> **Este pacote informa. Nao produz, nao registra e nao antecipa ato soberano** (DC-09, LM-03).
> O ato de 2026-07-28 declara expressamente que **nao aprova futura emenda de DEP-QAR**.

### 7.1 Identificacao

| Campo | Conteudo |
|---|---|
| **ID** | `DEP-QAR` |
| **Versao proposta** | **1.1.0** — emenda **MENOR** (AL-01: altera conteudo normativo sem quebrar compatibilidade) |
| **Versao em vigor** | **1.0.0**, `ativo` · `ratificada` — **nao alterada por esta missao** |
| **H-A da versao proposta** | `3e69441e2acab1cc34ff03da16c9e8bb004b65295736e08f9da53dfe0eaca3a0` |
| **Linhas** | **387** *(1.0.0 tem 386; +1 linha de historico)* |
| **Estado proposto** | `em-revisao` · `ratificacao: pendente` |
| **Onde o texto vive hoje** | **Fora do acervo.** A versao candidata foi construida e medida em area de trabalho, e **nao** foi escrita em `departments/qar/carta.md`, que permanece com o texto **ratificado** intacto |
| **Reprodutibilidade** | O diff de §7.2 e **completo e literal**: aplicado a 1.0.0, reproduz exatamente o H-A acima. Qualquer terceiro pode reconstrui-lo e conferir |

### 7.2 Diff normativo — completo

**Uma linha normativa; tres campos de frontmatter; uma linha de historico. Nada mais.**

| # | Local | Antes | Depois |
|---|---|---|---|
| 1 | frontmatter `versao` | `1.0.0` | **`1.1.0`** |
| 2 | frontmatter `status` | `ativo` | **`em-revisao`** |
| 3 | frontmatter `ratificacao` | `ratificada` | **`pendente`** |
| 4 | **§10, linha `I-6`, coluna Materia** | *"Ser priorizado, avaliado ou instruido por departamento de **Linha**"* | *"Ser priorizado, avaliado ou instruido por departamento de **Linha**, de **Plataforma** ou de **Comando**"* |
| 5 | **§10, linha `I-6`, coluna Motivo** | *"Independencia da Guarda nao se dilui"* | *"Independencia da Guarda nao se dilui, e o risco nao vem so da Linha: quem prioriza a organizacao inteira e o **Comando**"* |
| 6 | **§10, linha `I-6`, coluna Substituto** | *"DEP-EXE coordena Linha e Plataforma, **nunca** a Guarda"* | *"**SOBERANO** — DEP-QAR responde diretamente a ele. DEP-EXE coordena Linha e Plataforma, **nunca** a Guarda"* |
| 7 | **§10, linha `I-6`, coluna Fonte** | `ES-02, IV-01; FND-09 §6.2, R-07` | `ES-02, IV-01; FND-09 §6.2, R-07; **IC-5**` |
| 8 | Historico de versoes | — | **+1 linha**, registrando a emenda |

**Nenhum outro bloco, linha, tabela ou campo e alterado.** Os doze blocos B1–B12 permanecem
identicos, exceto a linha `I-6` de B9.

### 7.3 Por que esta e a correcao minima suficiente

| Alternativa | Avaliada | Veredito |
|---|---|---|
| Nomear apenas o **Comando** alem da Linha | Sim | **Insuficiente.** Deixaria a **Plataforma** de fora, e `DEP-KMS` presta servico a Guarda |
| Escrever *"qualquer departamento que nao seja da Guarda"* | Sim | **Recusada.** Abstracao por elegancia (AQ-03, SE-01): as classes sao **quatro e fechadas** (FND-02 §2.1); enumera-las e verificavel, a formula negativa nao |
| Mover a protecao para `FND-02` | Sim | **Recusada.** Seria **C3** e resolveria por norma geral um defeito de **uma linha de uma Carta** |
| **Enumerar Linha, Plataforma e Comando** | — | **Escolhida.** Cobre o risco real de IC-5, e verificavel contra as quatro classes, e **nao cria conceito novo** |

### 7.4 Revisao independente e impacto

| Campo | Conteudo |
|---|---|
| Autor da emenda | **DEP-EXE** — autor da Carta original |
| **Revisao independente** | **DEP-GOV** *(forma)* e **DEP-QAR** *(materia)*. **DEP-QAR e objeto da Carta**; por isso a materia foi conferida tambem por **DEP-GOV**, e o desvio esta declarado |
| Conformidade ao contrato | **12 de 12 blocos** preenchidos · `B4 × B9` conferida sob o checklist **1.2.0** *(corrigido por IC-1)* · nenhum conteudo proibido de ADR-0011 §5.4 |
| **Impacto** | **Nenhum artefato depende de `I-6`.** Nenhuma Carta, `FIT`, `REV` ou indice o cita. O impacto e **local a `DEP-QAR §10`** |
| Efeito sobre `H-N` | **Muda** — e por isso exige **ato novo** (IR-01, IR-05). E precisamente o caso que ADR-0012 existe para tornar visivel |
| Risco de **nao** emendar | O impedimento de DEP-QAR contra instrucao do **Comando** so e legivel cruzando **duas** Cartas. Um leitor de boa-fe de `DEP-QAR §10` conclui que o Comando pode instrui-lo |
| Risco de emendar | **Baixo.** A Carta volta a `em-revisao` ate o ato; nesse intervalo, `DEP-QAR` **1.0.0** permanece a versao em vigor. Nao ha vacuo |

### 7.5 Recomendacao

**APROVAR e RATIFICAR `DEP-QAR` 1.1.0**, em ato novo, explicito e datado, vinculado ao
**H-A `3e69441e…a3a0`**. Ate la, **`DEP-QAR` 1.0.0 permanece em vigor com o defeito IC-5 vivo e
declarado** — e o primeiro caso do sistema em que a imutabilidade por ratificacao retem um
defeito conhecido, registrado em R4 de FIT-2026-006 e **nao dissolvido** por esta revisao.

## 8. EV-08 — encerramento da proposta de consolidacao

### 8.1 Decisao: **AJUSTAR**

| Campo | Conteudo |
|---|---|
| **Estado de saida** | **ENCERRADA — AJUSTAR** |
| **Artefatos fundidos, aposentados ou divididos** | **ZERO** |
| **Por que nao "executar"** | **Nenhum dos quatro candidatos e elegivel** — §8.2, testado um a um. Fundir para satisfazer a metrica seria **destruir estrutura sadia para melhorar um numero** |
| **Por que nao "retirar"** | O sinal que a abriu e **real**: sete ciclos de crescimento, zero consolidacoes. Retirar a proposta apagaria o sinal sem trata-lo |
| **O que se ajusta** | O **criterio**, nao o acervo — §8.3 |

### 8.2 Teste de elegibilidade dos quatro candidatos

| # | Candidato | Elegivel? | Motivo |
|---|---|---|---|
| **1** | As **13 ressalvas** abertas, **12** dependentes da 1a ou 2a revisao estrutural | **NAO — e deixou de ser candidato** | O bloqueio era a **ausencia da revisao**. Ela ocorreu: **7 resolvidas, 1 reclassificada, 9 mantidas** (§5.1). Consolidar ressalva **nunca foi** o objeto de EV-08, que trata de **tipo, regra ou abstracao** |
| **2** | As **28 regras `CT`** de ADR-0010 | **NAO** | Agora **avaliaveis** — e **13 de 28 foram exercidas** nesta missao (§10.1), **46,4%** contra o limiar de um terco. A condicao de abertura **nao se verifica** |
| **3** | As **duas camadas** de memoria com zero registros — **PRD** e **TEC** | **NAO** | Camada de memoria **nao e tipo, regra nem abstracao**: e estrutura fixada por `FND-06 §2.1`, e reduzi-las e emenda **C3**. Alem disso, EV-08 exige **horizonte fechado**, e nenhum se fechou |
| **4** | Os **17** tipos documentais sem instancia *(nao 18 — §4)* | **NAO** | EV-08 exige *"atravessar **um horizonte inteiro** sem instancia"*. **Nenhum horizonte se fechou em sete ciclos.** Alem disso, 12 dos 17 sao de componentes cuja criacao esta **expressamente proibida** — ausencia **determinada**, nao ociosidade |

> **O resultado desconfortavel, repetido e agora medido.** Os quatro candidatos mais obvios
> sao inelegiveis, e **dois deles deixaram de ser candidatos por evidencia produzida nesta
> missao** — nao por reformulacao. Isso **nao invalida** a abertura de EV-08: **valida o
> diagnostico** de que o gatilho de R3 mede **crescimento** sem verificar se existe **objeto
> consolidavel**.

### 8.3 O ajuste — e por que ele nao pode ser feito aqui

| Campo | Conteudo |
|---|---|
| **Defeito do gatilho** | **R3 dispara por crescimento do acervo**; **EV-08 exige horizonte fechado**. Os dois nunca coincidem, e por isso a proposta abre e fecha sem objeto — **duas vezes seguidas** |
| **Ajuste necessario** | R3 so deve disparar quando houver **objeto consolidavel elegivel**; e **"horizonte"** precisa de definicao operavel |
| **Por que nao se corrige nesta revisao** | R3 vive em `FIT-2026-005` e `FIT-2026-006`, ambos **M1** — nao se editam (LV-04, MEM-APR-0003). E **EV-08** vive em `FND-09 §12`: alterar o criterio e emenda a documento fundacional, e **definir o que fecha um horizonte** e decisao sobre o **ritmo da organizacao**, materia do **Soberano** |
| **Encaminhamento** | **PS-1** — §5.4. A pergunta escalada e exatamente esta |
| **O que esta revisao faz** | Registra o defeito, mede-o e **encerra EV-08 com resultado** — cumprindo a **Condicao 4** do rollout de FIT-2026-006. **Nao** fecha R3 |

## 9. Achados novos

| # | Achado | Sev. | Dono | Gatilho |
|---|---|---|---|---|
| **RE-01** | **O ato soberano designa o pacote de ratificacao como sendo "de FIT-2026-006"; ele esta em REV-INTERCLASSES §6.** O objeto e univocamente determinavel, mas a designacao aponta arquivo que nao o contem | Baixa | DEP-GOV | **Proximo ato soberano** — anexar ao pedido de decisao o **caminho exato** do pacote, alem do ID da missao |
| **RE-02** | **`MEM-EST-0001` contem, no corpo, a nota *"Estado `aprovado`, nao `ativo`"*, que o ato tornou falsa.** Corrigi-la e **emenda** (ADR-0009) e produziria versao **1.1.0 nao ratificada** | **Media** | DEP-KMS | **Primeira emenda a `MEM-EST-0001`** por qualquer motivo. Ate la, o frontmatter e a fonte do estado (PJ-04) |
| **RE-03** | **DEP-QAR revisa e aprova a revisao estrutural.** FND-02 §9.4 torna GOV, EXE e KMS produtores; sobra um unico departamento para revisar **e** aprovar | **Media** | DEP-GOV | **Carta de DEP-GOV** *(IC-4)*, que deve declarar este impedimento em B9; **3a ocorrencia** do impedimento cruzado C5 |
| **RE-04** | **`artifact-registry` diverge de si proprio:** §2 declara **16** tipos com instancia, §5 declara **17** | Baixa | DEP-GOV | ✅ **Corrigido nesta revisao** — §4.2 |
| **RE-05** | **`artifact-registry §2` declara 11 entidades instanciadas e enumera 10.** `ORG` e `SOBERANO` **nao podem** ter instancia de artefato: sao as duas fora de A2 | Baixa | DEP-GOV | ✅ **Corrigido nesta revisao** — §4.2 |
| **RE-06** | **A cobertura de EV-08 nunca foi testavel:** o criterio exige horizonte fechado e o sistema nao fecha horizonte. Duas propostas abertas, duas encerradas sem objeto | **Media** | DEP-EXE; **SOBERANO** | **PS-1**, §5.4 |
| **RE-07** | **O indice mestre declarava `versao: 1.5.0` no frontmatter enquanto seu proprio Historico de versoes ja registrava `1.6.0`** — emenda aplicada sem incrementar o campo (AC-08, ADR-0009). As linhas do historico tambem estavam **fora de ordem** | Baixa | DEP-GOV | ✅ **Corrigido nesta revisao** — `README.md` passa a **1.7.0**, com o historico reordenado |
| **RE-08** | **A serie de custo de contexto nao e comparavel.** As quatro medicoes anteriores — 23% · 33% · 30,6% · 18,5% — registraram **um numero cada, sem a composicao do pacote**. A 5a medicao e **a primeira itemizada**, e por isso **nao se pode afirmar** que 21,3% e comparavel a 18,5%: a diferenca pode ser de custo real, de escopo **ou de criterio de contagem** | **Media** | DEP-KMS | **Toda medicao futura declara a composicao.** **R4 de FIT-2026-002 nao fecha** ate haver **duas descidas consecutivas com composicao itemizada** — [FIT-2026-007 §F5.1](../governance/fitness/FIT-2026-007-revisao-estrutural-i.md) |

**Achados: 8 · corrigidos nesta revisao: 3 · abertos com dono e gatilho: 5 · sem destino: 0.**

> **RE-07 e a quarta ocorrencia do mesmo padrao nesta missao** — IC-8, RE-04, RE-05 e RE-07 sao
> todos **defeitos da fonte contra si propria**, encontrados ao **executar a propagacao**, nunca
> por varredura. A varredura C11 confere **projecao contra fonte**; nenhum destes quatro seria
> encontrado por ela. **Registrado como sinal estrutural, nao como quatro acidentes.**

## 10. Contexto do Soberano — avaliacao com o registro em vigor

### 10.1 As 28 regras `CT`, uma a uma

> **Tres estados, e "nao aplicavel" exige motivo.** **Exercida** — a regra governou um ato ou
> uma verificacao desta missao. **Nao aplicavel** — a materia que ela alcanca **nao ocorreu**;
> o motivo esta escrito. **Aplicavel e nao exercida** — a materia ocorreu e a regra **nao**
> agiu: isso seria defeito.

| Regra | Estado | Motivo |
|---|---|---|
| **CT-01** | **Exercida** | **AF-35** *(backup antes do risco)* orientou a copia datada do acervo antes das edicoes de catalogo e indices. Orientou onde a norma admite escolha; nao obrigou |
| CT-02 | Nao aplicavel | Nenhuma regra do contrato foi invocada para criar autoridade |
| CT-03 | Nao aplicavel | **Nenhum conflito** entre Contexto e norma ocorreu |
| **CT-04** | **Exercida** | **AF-35** e **AF-39** permaneceram **classe 3**; nenhuma foi promovida a norma por esta missao |
| CT-05 | Nao aplicavel | Nenhuma afirmacao reproduziu conteudo decisorio |
| CT-06 | Nao aplicavel | **Nenhuma afirmacao nova** foi registrada |
| **CT-07** | **Exercida** | **11 lacunas `unknown` verificadas uma a uma e mantidas** — V9 de MSG-2026-0002. O proprio ato determinou que permanecem desconhecidas |
| CT-08 | Nao aplicavel | **Zero** afirmacoes `inferred` no registro |
| CT-09 | Nao aplicavel | Nenhuma classe nova nomeada |
| CT-10 | Nao aplicavel | Nenhuma afirmacao alterada |
| CT-11 | Nao aplicavel | Nenhuma afirmacao nova derivada de fonte externa |
| **CT-12** | **Exercida** | O **acolhimento** dos dois `FIT` **nao** foi lido como ratificacao. Classe **nao subiu** por utilidade |
| **CT-13** | **Exercida** | Duas vezes: a designacao imprecisa **nao** foi resolvida por precedente (§1.2 de MSG-2026-0002); e *"sem eleva-los a norma"* foi lido **literalmente**, recusando generalizacao (LM-03) |
| CT-14 | Nao aplicavel | Nenhuma afirmacao classificada |
| **CT-15** | **Exercida** | Varredura de conformidade a lista fechada nos artefatos ratificados — **0 ocorrencias** (V8) |
| CT-16 | Nao aplicavel | Nenhuma afirmacao registrada |
| CT-17 | Nao aplicavel | Nenhuma afirmacao incorreta detectada |
| CT-18 | Nao aplicavel | **Zero** afirmacoes `restrito` ou `soberano` |
| CT-19 | Nao aplicavel | O Soberano **nao** retirou nenhuma afirmacao |
| **CT-20** | **Exercida** | §10.3 declara **qual** pacote foi carregado e **sob que gatilho** |
| CT-21 | Nao aplicavel | Perfil declarado, nao ato |
| **CT-22** | **Exercida** | Carregamento **acima** do minimo ocorreu, **sob gatilho declarado** — §10.3 |
| **CT-23** | **Exercida** | Custo do pacote **medido em linhas**, nunca estimado — §10.3 |
| **CT-24** | **Exercida** | Resumo do catalogo conferido **contra o registro**; em divergencia prevaleceu a fonte — §4 e §12 |
| CT-25 | Nao aplicavel | Nenhuma afirmacao com prazo curto |
| **CT-26** | **Exercida** | Divisao do registro avaliada em §8.2: **zero** sinais observados; **nao dividir** |
| **CT-27** | **Exercida** | Os **tres** gatilhos de promocao a fundacional testados: **(a)** segunda instancia `MEM-EST` — **nao**; **(b)** segundo consumidor formal — **nao**; **(c)** sinal S5 — **nao**. Nenhum disparou |
| **CT-28** | **Exercida** | E a regra que exigia o ato: o registro **nasceu `aprovado`** e so agora entra em `ativo` |

| Medida | Valor |
|---|---|
| **Exercidas** | **13** |
| **Nao aplicaveis, com motivo escrito** | **15** |
| **Aplicaveis e nao exercidas** | **0** |
| **Total** | **28** |
| **Proporcao exercida** | **13/28 = 46,4%** — acima do limiar de **um terco (33,3%)** de R1 |
| Leitura sob a **Correcao 1** *(ausencia fora do dominio nao e ocorrencia negativa)* | **13 de 13 aplicaveis = 100%** |

**Sob qualquer das duas leituras, a condicao de abertura de EV-08 contra as regras `CT` nao se
verifica. R1 de FIT-2026-004 fecha.**

### 10.2 As tres abstracoes — e um erro de contagem na propria ressalva

| Abstracao | Membros | Estado | Leitura |
|---|---|---|---|
| Classe `inferred` | **0** | 🟡 **Mantida** | **Zero e o resultado bom:** nada foi inferido, e a regra existe para garanti-lo. Consolida-la removeria a garantia. Mesma forma de `PR-1`/`PR-2` |
| **Classe 4 de autoridade** | **0** | ⚠️ **Nao e abstracao distinta** | `ADR-0010 §5.3` define classe 4 como *"Hipotese sobre o Soberano — **instrumento: afirmacao `inferred`**"*. **E o mesmo conjunto**, visto de outro documento. **R2 contou duas vezes o mesmo objeto** |
| Os **4 pacotes** de contexto | **1 consumidor** *(P1, esta missao)* | 🟡 **Mantida** | O gatilho de R2 exige *"consumidor que **nao seja a propria execucao de missao**"*. Esta missao **e** execucao de missao: **nao conta** |

> **R2 de FIT-2026-004 media tres abstracoes onde ha dois objetos.** Registrado como
> observacao sobre a ressalva, **nao** como fechamento dela: corrigir a contagem **nao** cria
> membro nenhum. Os dois objetos continuam com **zero** membros elegiveis.

> **A reclassificacao de R2 nao e progresso, e esta escrito para que nao seja lida como tal.**
> Ela sai de *"nao-avaliavel porque o registro esta inativo"* e volta a *"aberta, aplicavel,
> gatilho nao disparado"*. **Mudou o motivo; nao mudou o objeto.** Nenhum componente foi
> criado, porque criar componente esta proibido nesta missao.

### 10.3 Pacote minimo carregado — declaracao de CT-20

| Campo | Conteudo |
|---|---|
| **Pacote minimo para a avaliacao de §10.1** | **P1** — §1 e §7 do registro. **28 linhas**, **9,9%** do registro *(medicao do proprio `MEM-EST-0001 §9`)* |
| **O que esta missao efetivamente carregou** | **O registro alem de P1**, incluindo §5, §8 e §9 |
| **Gatilho declarado do carregamento acima do minimo** | **Verificacao independente de versao, hash e integridade exigida como condicao de eficacia pelo ato soberano** — impossivel de executar sobre um recorte |
| **Conformidade** | **CT-22 satisfeita** — o carregamento acima do minimo tem gatilho declarado. **CT-20 satisfeita** — a declaracao esta aqui, no artefato que consome |
| **Honestidade da medicao** | **Declarar 28 linhas sem declarar o excedente seria falso.** O piso da consulta e 28; **esta missao nao operou no piso**, e o motivo esta escrito |

## 11. Varredura C11 — indices contra fontes

Acao **C11** de REV-CONSOLIDACAO §10. Dono **DEP-GOV**. Resultado detalhado em §12.

| # | Indice | Conferido contra | Resultado |
|---|---|---|---|
| 1 | `README.md` *(raiz)* | Catalogo e contagens em disco | **Atualizado** — 4 Cartas em vigor, estado dos tres ratificados |
| 2 | `foundation/README.md` | 10 `FND` + 19 `TPL` em disco | **Conforme, sem alteracao** — **nenhum `FND` emendado e nenhum `TPL` criado** nesta missao; o indice nao lista revisoes arquiteturais |
| 3 | `decisions/README.md` | 12 arquivos `ADR-*` | **Atualizado** — contador **0012** |
| 4 | `rfcs/README.md` | 9 arquivos `RFC-*` | **Atualizado** — contador **0009** |
| 5 | `capabilities/README.md` | 23 arquivos; frontmatter | **Atualizado** — §10.3 recebe a resolucao de P2–P5 |
| 6 | `governance/README.md` | 0 `EXC` · 2 `INC` · 14 avaliacoes | **Atualizado** |
| 7 | `governance/exceptions/README.md` | 0 arquivos | **Conforme** — nenhuma excecao vigente |
| 8 | `governance/incidents/README.md` | 2 arquivos | **Atualizado** — INC-2026-002 **`fechado`** |
| 9 | `governance/fitness/README.md` | 7 `FIT` + 8 `REV` | **Atualizado** — contador **007**; estado dos `FIT` acolhidos |
| 10 | `governance/artifact-registry.md` | Arquivo a arquivo | **Atualizado** — v1.5.0, baseline `BL-2026-07-28-05`, §5 corrigida |
| 11 | `memory/README.md` | 8 registros | **Atualizado** |
| 12 | `memory/operacional/README.md` | 2 registros — MSG-0001 e MSG-0002 | **Atualizado** |
| 13 | `memory/estrategica/README.md` | 1 registro, agora **`ativo`** | **Atualizado** |
| 14 | `memory/aprendizado/README.md` | 4 arquivos | **Conforme** — nenhum `APR` novo |
| 15 | `memory/produto/README.md` | 0 registros | **Conforme** |
| 16 | `memory/tecnica/README.md` | 0 registros | **Conforme** |
| 17 | `departments/` | 4 subdiretorios | **Sem indice, por decisao** — DR-4 aberto; gatilho e a **quinta** Carta |

**17 varridos · 11 atualizados como parte desta mudanca** (IX-02, CV-04).

### 11.1 Integridade referencial

| Verificacao | Resultado |
|---|---|
| Links relativos quebrados | **0** — §12 |
| Vinculo a Capability valido (VC-01) | **15** vinculos das 4 Cartas, todos a Capability `ativo` |
| Relacao fora dos pares permitidos (RM-02) | **Conforme** |
| Ciclo em `depende-de` | **Sem ciclo** — nenhuma Carta de Capability tocada |
| Dependencia ascendente (PD-11) | **Conforme** |
| **Autoverificacao** | **0 ocorrencias** — §0.1 declara o residuo estrutural de aprovacao, que **nao e** autoverificacao: DEP-QAR **nao produziu** nenhum artefato avaliado |
| Credencial em texto (PI-08, LV-02) | **0 ocorrencias** |
| **Artefatos M1 editados** | **0** — nenhum `FIT`, `REV` ou baseline anterior tocado |
| **Texto ratificado alterado** | **0** — `DEP-QAR` 1.0.0, `DEP-ENG` 1.0.0 e o corpo dos tres ratificados intactos; provado por **IR-09** |

## 12. Reconciliacao catalogo-fonte

| Verificacao | Resultado |
|---|---|
| Todo artefato novo tem entrada no catalogo (RG-02) | **5 de 5** — `MSG-2026-0002`, `RFC-0009`, `ADR-0012`, `REV-ESTRUTURAL-I`, `FIT-2026-007` |
| Todo artefato alterado tem a linha atualizada | **4 de 4** — `DEP-EXE`, `DEP-KMS`, `MEM-EST-0001`, `INC-2026-002` |
| Estado de ratificacao × fonte canonica | Projecao conferida contra **MSG-2026-0002**, fonte unica (PJ-03) |
| Divergencia catalogo × fonte encontrada | **3** — IC-8, **RE-04**, **RE-05**. **Todas corrigidas na vista derivada; zero fontes alteradas** (RG-03, M3) |
| Proveniencia | **100% `native`** |
| Baselines `BL-01` a `BL-04` editadas? | **Nao.** `BL-04` teve a integridade **conferida antes** de qualquer edicao e nao foi tocada depois (BL-02) |
| Nova medicao recebeu identidade nova? | **Sim** — `BL-2026-07-28-05` |
| **Copia datada antes das edicoes** | **Sim** — 115 arquivos, tomada antes da reescrita de catalogo e indices (AF-35, PI-07) |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-GOV *(forma)* · DEP-EXE *(merito)* · DEP-KMS *(evidencia)* | **Primeira Revisao Estrutural.** Rito de FND-02 §9.4 executado sobre Fundacao, 23 Capabilities, 21 entidades, 33 tipos e 4 classes de Departamento. **IC-8 resolvido a partir da fonte** — 33 = 4+5+7+4+2+10+1, sem emendar FND-10. **P2 a P5 fechados** pela distincao entre deter competencia e operar sob ela. Mapa unico de bloqueios: **7 resolvidas · 1 reclassificada · 9 mantidas · 2 achados corrigidos · 4 abertos**. **EV-08 encerrada como AJUSTAR**, com os quatro candidatos testados e inelegiveis. **Pacote de emenda `DEP-QAR` 1.1.0** preparado e hasheado, **nao ativado**. **28 regras `CT` avaliadas uma a uma**: 13 exercidas, 15 nao aplicaveis com motivo, 0 aplicaveis-nao-exercidas. **6 achados novos.** **Uma unica pendencia escalada ao Soberano.** |
