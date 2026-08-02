---
id: FIT-2026-007-revisao-estrutural-i
titulo: Aptidao arquitetural da Primeira Revisao Estrutural e do fechamento de divida
tipo: fitness
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-QAR
proprietario: DEP-QAR
aprovador: DEP-GOV
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0010, ADR-0011, ADR-0012]
substitui: []
substituido_por: null
objeto_avaliado: [MSG-2026-0002, DEP-EXE, DEP-KMS, MEM-EST-0001, RFC-0009, ADR-0012, INC-2026-002]
classe_mudanca: C2
classe_avaliacao: aptidao
veredito: apto-com-ressalva
resumo: Verifica se a Missao 1.8 deixou a arquitetura mais apta a evoluir; veredito apto-com-ressalva, quatro ressalvas, rollout GO-CONDITIONAL e uma unica pendencia escalada ao Soberano.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-GOV
ratificacao: nao-exigida
---

# FIT-2026-007: Primeira Revisao Estrutural e fechamento de divida

## Proposito
Verificar se a **Missao 1.8** — segundo ato soberano, Primeira Revisao Estrutural, `RFC-0009`,
`ADR-0012` e o fechamento de `INC-2026-002` — deixou a arquitetura **mais apta a evoluir**, e
decidir **GO / GO-CONDITIONAL / ADJUST / STOP** para as **cinco** Cartas restantes.

> **Obrigatorio por dois fundamentos independentes:** FND-02 §9.4 — *"a revisao estrutural so
> fecha com `FIT` emitido"* — e QG-6 sobre mudanca **C2**.

## Escopo
| Item | Definicao |
|---|---|
| Objeto avaliado | `MSG-2026-0002` · `DEP-EXE` · `DEP-KMS` · `MEM-EST-0001` · `RFC-0009` · `ADR-0012` · `INC-2026-002` |
| Estado anterior | **112 artefatos, 28.966 linhas** *(`BL-2026-07-28-04`)*; **17** ressalvas abertas; **6** vereditos consecutivos `apto-com-ressalva`; **3** artefatos retidos por falta de ato |
| **Nao** inclui | **Corretude estrutural** — objeto de [REV-ESTRUTURAL-I](../../foundation/revisao-estrutural-01-2026-07-28.md). As cinco Cartas restantes. O **merito** do ato soberano |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| **Executa** | **DEP-QAR** | FT-02, CV-08 — **nao produziu nenhum dos sete artefatos avaliados** |
| Forma | DEP-GOV | |
| Evidencia | DEP-KMS | Medicoes de acervo, de secao, de pacote e de hash |
| **Aprova** | **DEP-GOV** | **Desvio declarado.** A matriz atribui a aprovacao de `FIT` a **DEP-EXE**, impedido por ter contribuido o merito da revisao estrutural (`DEP-EXE §10, I-2`). Cenario **CX-3**; precedentes FIT-2026-003 e FIT-2026-006 |
| Ratifica | **Nao aplicavel** | Objeto **C2/Tipo 2** |

> **Residuo declarado (PI-10).** **DEP-QAR aprovou a REV-ESTRUTURAL-I** e executa este `FIT`.
> O objeto deste `FIT` **nao inclui a REV** — sao os sete artefatos acima, nenhum produzido por
> DEP-QAR. Ainda assim, os dois papeis convivem no mesmo departamento porque **nao ha outro
> disponivel**: FND-02 §9.4 faz de GOV, EXE e KMS os produtores da revisao. Registrado como
> ressalva **R3** e achado **RE-03**.

---

## Sumario

| # | Pergunta | Resposta | Sinal |
|---|---|---|---|
| F1 | Complexidade aumentou sem ganho proporcional? | **Nao** | **+1.981 linhas (6,8%)** contra **3 artefatos em vigor**, **2 incidentes fechados**, **7 ressalvas** e **7 achados** fechados, **4 divergencias de catalogo corrigidas** e **0** entidades, tipos, camadas ou documentos fundacionais criados |
| F2 | Algum conceito foi duplicado? **e** a prevencao foi aplicada? | **Nao · aplicada** | **4** reproducoes barradas; **7** projecoes declaradas; **1** fonte canonica nova, nao acumulada |
| F3 | Alguma abstracao ficou desnecessaria? | **Nao — e duas saem da suspeita com evidencia** | **A2** e **M3** deixam de ser suspeitas por **uso demonstrado**, nao por reclassificacao |
| F4 | Continua mais simples de evoluir? | **Sim** | **Cinco** perguntas antes sem resposta verificavel passam a ter uma; **nenhuma aprovacao nova** criada |
| F5 | Custo de contexto subiu ou desceu? | **SUBIU** — 21,3% contra 18,5% | E a **5a** medicao. **Nao fecha R4 de FIT-2026-002**, e revela que **as cinco medicoes nao sao comparaveis** — achado **RE-08** |
| F6 | Favorece reutilizacao? | **Sim** | **12 regras `IR`** aplicaveis a todo ato futuro; **1** distincao que fechou **quatro** achados de uma vez |

**Veredito:** `apto-com-ressalva` — **quatro** ressalvas, todas com dono e gatilho.
**Decisao de rollout: GO-CONDITIONAL** (§Rollout). **Uma** pendencia escalada ao SOBERANO.

---

## F1 — A complexidade aumentou sem ganho proporcional?

| Medida | Antes | Depois | Variacao |
|---|---|---|---|
| Artefatos | 112 | **117** | **+5** |
| Linhas | 28.966 | **30.947** | **+1.981 (6,8%)** |
| Entidades declaradas | 21 | **21** | **0** |
| **Entidades instanciadas** | 11 *(declarado)* | **10** *(medido)* | **−1 por correcao** — RE-05 |
| Tipos documentais | 33 | **33** | **0** — IC-8 resolvido **sem emendar FND-10** |
| Documentos fundacionais | 10 | **10** | **0** |
| Camadas de memoria · templates · portoes · departamentos | 5 · 19 · 7 · 9 | **5 · 19 · 7 · 9** | **0** |
| Departamentos com Carta | 4 | **4** | **0** |
| **Cartas em vigor** | **2** | **4** | **+2** |
| **Artefatos em vigor por ato soberano** | 2 | **5** | **+3** |
| **Artefatos retidos por falta de ato** | **3** | **0** | **−3** |
| **Incidentes abertos** | 1 | **0** | **−1** |
| Regras normativas novas | — | **12** *(`IR-01` a `IR-12`)* | **+12** |
| **Ressalvas fechadas** | — | **7** | Mais que os **seis ciclos anteriores somados** |
| **Achados fechados** | — | **7** | P2 · P3 · P4 · P5 · IC-7 · IC-8 · DR-1/DR-2 ja fechados |
| Achados **novos** | — | **7** *(RE-01 a RE-07)* | 3 corrigidos, 4 com dono e gatilho |
| **Divergencias catalogo × fonte corrigidas** | — | **4** | IC-8, RE-04, RE-05, RE-07 — **zero fontes alteradas** |
| Artefatos **M1** editados | — | **0** | Nenhum `FIT`, `REV` ou baseline anterior |
| **Texto ratificado alterado** | — | **0** | Provado por `IR-09`, byte a byte |
| Cartas de Capability alteradas | — | **0** | — |
| Cartas, agentes, skills, workflows ou produtos criados | — | **0** | Conforme determinacao |
| Indices atualizados *(M3 derivado)* | — | **11** | — |
| **Consolidacoes executadas** | **0** em 6 ciclos | **0** | **7o ciclo** — §Ressalvas R2 |

**Leitura.** O acrescimo tem contrapartida verificavel e, pela primeira vez, **parte dela e
subtracao**: tres artefatos saem de retencao, um incidente sai de aberto, quatro divergencias
aritmeticas saem do catalogo. **Nenhum tipo, entidade, camada ou documento fundacional foi
criado** — e **IC-8, que parecia exigir emenda a FND-10, foi resolvido a partir da propria
fonte**.

**Contrapartida honesta:** **doze regras novas** (`IR`) e **setimo ciclo consecutivo de
crescimento**. As doze regras nascem com **dois membros verificados** (`DEP-QAR` e `DEP-ENG`, via
`IR-09`), e nao com zero — mas continuam sendo doze regras a mais.

**Resposta:** **nao**.

## F2 — Algum conceito foi duplicado? E a prevencao foi aplicada?

### F2.a — Ocorrencia

| Conceito | Onde ja estava | Como a mudanca o trata |
|---|---|---|
| Ato soberano de 2026-07-28 sobre os pilotos | `MSG-2026-0001` | **Barrado.** O segundo ato recebeu **fonte canonica propria** (`MSG-2026-0002`); a primeira **nao foi editada** |
| Hashes das Cartas ja ratificadas | `MSG-2026-0001 §2` | **Referenciados.** O catalogo §10.2 deixou de listar hash e passou a apontar as duas fontes |
| Aritmetica dos 33 tipos | FND-10 §4 | **Corrigida na projecao**, nunca na fonte (RG-03, M3) |
| Estado de ratificacao dos dois `FIT` | — | **Fonte unica nova:** `MSG-2026-0002 §4`; `fitness/README` projeta |
| Ambiguidade G1/G2 | `INC-2026-002 §5` | **Movida, nao copiada** — vive agora **so** em `RFC-0009 Q2`; o incidente **referencia** |
| Texto candidato de `DEP-QAR` 1.1.0 | — | **Nao escrito no acervo.** Vive como **diff reproduzivel** em REV-ESTRUTURAL-I §7 — evita duas Cartas do mesmo departamento |
| 28 regras `CT` | ADR-0010 §5 | **Referenciadas por ID.** A avaliacao de §10.1 da REV **nao reproduz o texto** de nenhuma |

**Nenhuma duplicacao nova introduzida.**

### F2.b — Prevencao *(PJ-06)*

| Verificacao | Evidencia | Resultado |
|---|---|---|
| O autor percorreu cada tabela pelo item de PJ-05? | Todas as tabelas dos artefatos novos e emendados | **Sim** |
| Toda exibicao de conteudo de outra fonte declara projecao? | **7** declaracoes: `MSG-2026-0002 §2` · catalogo §5, §9 e §10 · `fitness/README` *(coluna Ratificacao)* · `capabilities/README §10` · `decisions/README` | **Sim** |
| Alguma reproducao foi **barrada antes** de ser escrita? | **4** — o ato em `MSG-2026-0001`, os hashes no catalogo, o texto de `DEP-QAR` 1.1.0 e o texto das 28 regras `CT` | **Sim** |
| O teste encontrou algo que a auditoria posterior nao encontraria? | **4 — IC-8, RE-04, RE-05 e RE-07.** Nenhum e projecao contra fonte: sao **defeitos da fonte contra si propria**, e a varredura C11 **nao os alcanca** | **Sim** |

> **Quinta confirmacao observada de [MEM-APR-0002](../../memory/aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md),
> e a primeira em que o mecanismo aparece quatro vezes na mesma missao.** A familia percorreu:
> *copiar tabela* → *afirmacao derivada divergente* → *declarar-se projecao sem ser* → *declarar
> correcao aplicada sem aplica-la* → **agora, documento que diverge de si proprio** (IC-8, RE-04,
> RE-05, RE-07). **O ponto cego esta nomeado:** a auditoria confere **projecao contra fonte**, e
> **nao confere a fonte contra si mesma**.

**Resposta:** nao houve duplicacao nova · prevencao **aplicada**, com evidencia.

## F3 — Alguma abstracao ficou desnecessaria?

| Abstracao | Membros antes | **Membros agora** | Veredito |
|---|---|---|---|
| **Arquetipo `A2` ARTEFATO** | **0 usos discriminantes registrados** | **2** — recusa da entidade *"Artifact"* (FND-10 §3.3) e a exclusao de `ORG`/`SOBERANO` que corrigiu o catalogo (**RE-05**) | **Justificada — e nao por reclassificacao.** Consolida-la apagaria a distincao que acabou de corrigir uma contagem |
| **Classe de mutabilidade `M3`** | 1 membro, uso nao demonstrado | **1 membro, 4 usos decisivos** — IC-8, RE-04, RE-05 e RE-07 corrigidos **na vista derivada, zero na fonte** | **Justificada.** Um membro **muito** usado nao e abstracao ociosa |
| **`IR-01` a `IR-12`** *(novas)* | — | **5 artefatos** com tres hashes; **2** com `IR-09` executado | **Justificada — nasce com membros medidos** |
| Classe `inferred` · classe 4 de autoridade | 0 · 0 | **0** — e sao **o mesmo objeto** (REV §10.2) | **Mantida.** Zero e o resultado bom: nada foi inferido. **A ressalva contava dois objetos onde ha um** |
| Os **4 pacotes** de contexto `CT` | 0 consumidores | **0 consumidores elegiveis** | **Mantida.** O gatilho exige consumidor que **nao seja execucao de missao**; nenhum componente foi criado |
| **`PR-1` · `PR-2`** | 0 · 0 | **0 · 0** | **Mantidas** — nenhuma Carta escrita; nenhuma divergencia possivel |
| **Portao de admissao** de ADR-0007 *(5 condicoes)* | 0 | **0** | **Mantido** — nenhum candidato do Legacy |

**Regra aplicada:** abstracao com menos de dois membros e suspeita (AQ-03).

**Resposta:** **nao** — e **duas saem da suspeita porque foram usadas**, nao porque o criterio
mudou. A diferenca em relacao a FIT-2026-006, onde `PR-1` e `PR-2` mudaram de estado sem que
nenhum numero melhorasse, esta declarada de proposito.

## F4 — O sistema continua mais simples de evoluir?

| Mudanca-tipo | Antes | Depois | Aprovacoes |
|---|---|---|---|
| Saber **o que** um ato de ratificacao vincula | **Nao havia resposta** — e a pratica variava | `IR-01` a `IR-03`: conteudo normativo, lista fechada, **H-N** | Inalterado |
| Provar que um artefato ratificado **nao foi alterado** | Impressao digital, que **nao detecta** edicao de mesmo tamanho | **`IR-09`** reconstroi o texto e confere byte a byte | Inalterado |
| Saber se `Memoria <camada>` e um tipo ou cinco | **Divergencia aritmetica aberta** | **Cinco**, por **CS-02** — e a soma fecha em 33 | Inalterado |
| Distinguir **deter uma competencia** de **operar sob ela** | **Nao havia criterio** — quatro divergencias aparentes em aberto | Criterio escrito; **P2 a P5 fechados de uma vez** | Inalterado |
| Saber se a ausencia de Carta de DEP-GOV **bloqueia** | Julgamento | **Nao bloqueia; ordena.** Autoridade vem de FND-02 §3 e FND-09 §8.2 | Inalterado |

**Leitura.** **Cinco** perguntas antes sem resposta verificavel passam a ter uma. **Nenhuma
aprovacao nova foi criada**; nenhum caminho de decisao ficou mais longo; **nenhum papel ganhou
veto novo**.

**Contrapartida:** **doze regras novas** a carregar, e **duas questoes normativas escaladas** —
o sistema ficou mais simples de **verificar** e continua igualmente dependente do Soberano para
**decidir**.

**Resposta:** **sim**.

## F5 — A mudanca reduz ou aumenta o custo de contexto?

| Papel / tarefa-tipo | Antes | Depois | Direcao |
|---|---|---|---|
| Piso obrigatorio de qualquer tarefa | 1.099 linhas | **1.099 linhas** | **inalterado** |
| **Executar uma missao estrutural** | **18,5%** — 4a medicao | **21,3%** — 5a medicao | **SOBE** |
| Provar integridade de artefato ratificado | Impressao digital do acervo — **117 arquivos** | **1 arquivo + 1 diff** (`IR-09`) | **desce** |
| Consultar o criterio do Soberano | **Indisponivel** — registro nao vigente | **P1 = 28 linhas**, em vigor | **desce, a partir do indisponivel** |
| Saber o estado de ratificacao de qualquer artefato | 2 fontes canonicas | 2 fontes canonicas | **inalterado** |
| Acervo total | 28.966 | **30.947** | **sobe 6,8%** |

### F5.1 A medicao, e o que ela revela sobre as anteriores

**Pacote minimo medido: 6.176 linhas sobre 28.966 = 21,3%.** Composicao **itemizada**:

| Bloco | Linhas |
|---|---|
| Artefatos integrais — FND-01, FND-03, catalogo, FIT-2026-006, INC-2026-002, MSG-2026-0001, MEM-EST-0001, `fitness/README`, `capabilities/README`, ADR-0010, ADR-0011 | **4.158** |
| Recortes normativos — FND-02 §9, FND-04 §2/§8, FND-09 §4/§5, FND-10 §3–§6, REV-INTERCLASSES §6–§10 | **648** |
| **Indices abertos para propagar (C11)** | **1.230** |
| Recortes de Carta e de `FIT` historicos | **140** |
| **Total** | **6.176** |

**A serie observada e 23% · 33% · 30,6% · 18,5% · 21,3%.** A quinta medicao **sobe 2,8 pontos**.

> ### O achado que a medicao produziu — **RE-08**
> **Esta e a primeira medicao da serie cuja composicao foi itemizada.** As quatro anteriores
> registraram **um numero**, sem a lista do que entrou. Isso significa que **nao e possivel
> afirmar que 21,3% e comparavel a 18,5%**: a diferenca pode ser de custo real, de escopo de
> missao **ou de criterio de contagem**.
>
> **Consequencia declarada:** o numero desta missao **subiu**, e por isso **R4 de FIT-2026-002
> nao fecha** — mas nem a subida nem uma eventual descida poderiam fechar R4 enquanto a serie
> nao for comparavel. **O defeito e da serie, nao desta medicao.**
>
> **Nao se corrigiram as medicoes anteriores.** Elas vivem em artefatos **M1**. O criterio de
> fechamento de R4 passa a exigir, alem de **duas descidas consecutivas**, que **ambas tenham
> composicao itemizada** — e a primeira itemizada e esta.

**O que subiu, e por que.** A missao teve de abrir **1.230 linhas de indices** para propagar as
correcoes — **20% do proprio pacote**. Uma revisao estrutural toca **todo o acervo por
definicao**; comparar seu custo com o de uma missao que exerce um contrato existente e
exatamente a duvida amostral de **R3 de FIT-2026-003**.

**Resposta:** **subiu** na missao medida. **→ R4 de FIT-2026-002 permanece aberta**, com o
criterio **endurecido** e o defeito da serie declarado.

## F6 — Ela favorece reutilizacao?

| Definicao produzida | Reutilizavel por | Especifica do caso? |
|---|---|---|
| **`IR-01` a `IR-12`** — o que um ato de ratificacao vincula | **Todo ato soberano futuro** — e havera um por Carta | Nao |
| **`IR-09`** — teste de reconstrucao do texto ratificado | **Todo artefato ratificado**, inclusive retroativamente | Nao |
| **Distincao *deter a competencia* × *operar sob ela*** | **Toda** divergencia aparente entre FND e catalogo de Capabilities. **Fechou quatro de uma vez** | Nao |
| Criterio **CS-02** aplicado a contagem de tipos | **Toda** duvida sobre se dois nomes sao um tipo ou dois | Nao |
| **Carta declara autoridade; nao a constitui** | **Toda** pergunta *"a falta de Carta bloqueia?"* — nas cinco restantes | Nao |
| **Registro fundamentado de "manter"** com contador de 3 | **Toda** revisao estrutural futura (FND-02 §9.4) | Nao |
| **Itemizacao da composicao do pacote de contexto** | **Toda** medicao futura de custo | Nao |
| RE-01 a RE-07 | — | **Sim** — descrevem o estado atual |

**Criterio:** DoD-8.

**Evidencia mais forte:** **uma unica distincao fechou quatro achados abertos ha um ciclo**
(P2, P3, P4, P5), **sem alterar nenhuma Carta de Capability**. O segundo mais forte e **`IR-09`**,
que **eliminou um limite declarado** da verificacao de integridade — a impressao digital nao
detecta edicao de mesmo tamanho; a reconstrucao detecta.

**Resposta:** **sim**.

---

## Ressalvas

| # | Ressalva | Custo assumido | **Dono** | **Gatilho de reavaliacao** |
|---|---|---|---|---|
| **R1** | **A concentracao em DEP-EXE foi confirmada por quatro gatilhos de especializacao — e o movimento corretivo e impossivel nesta fase.** *Escopo heterogeneo*, *gargalo de decisao*, *carga concentrada* e *conhecimento ilhado* dispararam, e os movimentos que FND-02 §9.2 indica exigem **criar agente** *(proibido)* ou **alterar FND-09 §8.2** *(C3)* | A revisao estrutural registrou **"manter" com fundamento**, e nao por ausencia de sinal. O sinal existe e permanece; e a **1a de tres** conclusoes de manutencao antes da escalada obrigatoria de FND-02 §9.4 | **DEP-EXE** | **Primeiro agente criado**, ou **IC-3** resolvido |
| **R2** | **EV-08 foi encerrada pela primeira vez, e nenhum dos quatro candidatos era elegivel.** O gatilho de R3 mede **crescimento**; o criterio de EV-08 exige **horizonte fechado** — e **nenhum horizonte se fechou em sete ciclos** | **Sete ciclos de crescimento, zero consolidacoes.** A proposta abriu e fechou **sem objeto**, e o instrumento de consolidacao permanece **inaplicavel por construcao** | **DEP-EXE**; decisao do **SOBERANO** | **PS-1** — decisao sobre o que fecha um horizonte |
| **R3** | **DEP-QAR revisou e aprovou a revisao estrutural, e executa este `FIT`.** FND-02 §9.4 torna GOV, EXE e KMS **produtores** da revisao; sobra **um unico** departamento para revisar e aprovar | A segregacao de papeis, que o sistema protege desde ADR-0005, opera aqui **no limite do possivel**. **Nao ha alternativa na estrutura atual**, e a alternativa de escalar ao Soberano foi avaliada e recusada com motivo | **DEP-GOV** | **Carta de DEP-GOV** *(IC-4)*, que deve declarar este impedimento em **B9**. **3a ocorrencia** do achado C5 |
| **R4** | **Duas questoes normativas seguem abertas e dependem de ato do Soberano.** **Q1** — emenda **C3** a FND-01 §7.3 — e **Q2** — se `FIT` exige ratificacao. **IC-2 esta contido por regra de redacao (`IR-11`), nao corrigido** | O termo *"ratifica"* continua nomeando **dois institutos** na Constituicao. A contencao impede **artefato novo** de propagar a ambiguidade, e **nao** corrige o texto que a origina. Ha risco real de a contencao ser tomada por solucao | **DEP-GOV**; decisao do **SOBERANO** | Ato do Soberano sobre Q1/Q2, **ou** proxima emenda a FND-01 |

## Veredito

| Campo | Conteudo |
|---|---|
| Veredito | **`apto-com-ressalva`** |
| Fundamento | As seis perguntas tem sinal observavel. **Nenhum artefato permanece retido por falta de ato**; **os dois incidentes do sistema estao fechados**; **sete ressalvas e sete achados fecham com evidencia** — mais que os seis ciclos anteriores somados —; **IC-8 foi resolvido a partir da fonte, sem emendar FND-10**; e **duas abstracoes saem da suspeita por uso demonstrado**. Em contrapartida, o **custo de contexto subiu**, o acervo cresce pelo **setimo** ciclo, **EV-08 encerrou sem objeto**, a segregacao de papeis opera **no limite do possivel**, e **duas questoes normativas continuam dependendo do Soberano**. Nao e `inapto` porque nenhuma contrapartida revela degradacao sem contrapartida verificavel — e porque **nenhuma divida foi fechada por renomeacao** |
| Efeito | **Encerra.** As quatro ressalvas viram divida declarada com dono e gatilho (FND-07 §9) |
| Data | 2026-07-28 |
| Executado por | **DEP-QAR** |
| Aprovado por | **DEP-GOV** — DEP-EXE impedido (CX-3) |
| Ratificado por | **Nao aplicavel** — objeto C2/Tipo 2 |

## Rollout das cinco Cartas restantes — **GO-CONDITIONAL**

| Campo | Conteudo |
|---|---|
| **Decisao** | **GO-CONDITIONAL** — a revisao esta apta; o que resta e **ato soberano sobre artefato ja validado** |
| **As quatro condicoes de FIT-2026-006** | **1** ✅ confirmada com fundamento medido *(IC-4 ordena, nao bloqueia)* · **2** ✅ instrumento integro *(checklist 1.2.0)*, medicao na quinta Carta · **3** ⚠️ **formalmente adiada**, com contencao `IR-11` · **4** ✅ EV-08 **encerrada** como `AJUSTAR` |
| Por que nao **GO** | **A Condicao 3 foi cumprida na forma fraca que ela propria admitia.** IC-2 esta **adiado**, nao resolvido, e corrigi-lo e **C3**. Alem disso, **R1 de FIT-2026-006 continua aberta**: o contrato nunca foi testado contra autor distinto de DEP-EXE |
| Por que nao **ADJUST** | As quatro condicoes **foram cumpridas**; a revisao estrutural **ocorreu** e destravou **doze** itens; **nenhuma correcao delimitada resta pendente dentro do mandato desta missao**. O que resta e **ato do Soberano**, nao trabalho |
| Por que nao **STOP** | Nenhuma falha estrutural foi encontrada. As verificacoes de necessidade, autoridade, sobreposicao, ciclos e dependencias passaram **integralmente**; **zero** ciclos, **zero** sobreposicoes de custodia, **zero** relacoes nulas |
| **Condicao unica de saida** | A **quinta Carta e a de DEP-GOV**, escrita **sozinha**, e deve declarar em **B9** o impedimento exposto por **RE-03** |
| Quem decide | **DEP-EXE**, com parecer de DEP-GOV; cada Carta e aprovada e ratificada pelo **SOBERANO** |

## Pendencia para o SOBERANO — **uma**

> **As quatro pendencias de FIT-2026-006 foram respondidas pelo ato de 2026-07-28.** Esta secao
> **informa e pergunta**; nao decide, nao presume e nao antecipa (LM-03, LM-06).

| # | Pendencia | Origem | Opcoes |
|---|---|---|---|
| **PS-1** | **Setimo ciclo de crescimento, e a primeira proposta de consolidacao encerrou sem consolidar nada — porque nenhum dos quatro candidatos era elegivel.** EV-08 exige *"horizonte inteiro sem instancia"*, e **nenhum horizonte se fechou em sete ciclos**. O gatilho mede crescimento; o criterio exige horizonte; os dois **nunca coincidem** | **R3 de FIT-2026-005** e **R3 de FIT-2026-006**, que determinam escalar se EV-08 fechar sem nada consolidado. Achado **RE-06** | **(a)** Fixar o que **fecha um horizonte** — numero de missoes, marco, ou outro criterio; **(b)** aceitar que EV-08 permaneca **inaplicavel por tempo indeterminado**, com a divida declarada; **(c)** determinar **outro criterio** de consolidacao, pelo rito de emenda a FND-09 §12 |

> **Nao se pede autorizacao para consolidar.** Pede-se decisao sobre o **criterio** — porque a
> revisao demonstrou, candidato a candidato, que **nao ha objeto consolidavel elegivel hoje**, e
> que isso decorre do desenho do gatilho, nao do estado do acervo.

### Nota sobre FT-04 — vigilancia de complacencia

| Verificacao | Estado |
|---|---|
| Vereditos emitidos | **7** |
| Consecutivos `apto` **sem nenhuma ressalva** | **0** — os sete com ressalvas |
| `inapto` emitidos | **0** |
| Ressalvas fechadas neste ciclo | **7** |
| Achados fechados neste ciclo | **7** |
| Ressalvas **reclassificadas** sem melhora de numero | **1** — R2 de FIT-2026-004, **declarada como nao-progresso** |
| Achados novos | **7** |
| **Revisoes estruturais que concluiram "manter"** | **1 de 3** antes da escalada obrigatoria (FND-02 §9.4) |

FT-04 exige tres `apto` **sem ressalva** para disparar; nao e o caso.

> **O alarme desta verificacao.** **Sete ressalvas fecharam num unico ciclo** — mais que os seis
> anteriores somados. Um ciclo que fecha muito **e** um ciclo a auditar. **Mitigacao verificada:**
> **seis das sete** tinham como gatilho literal a **1a revisao estrutural**, que nunca havia
> ocorrido; quando ela ocorreu, as condicoes puderam **enfim ser testadas**, e **quatro delas nao
> se verificaram** — o que fecha a ressalva **pelo texto que ela propria escreveu**. **Nenhuma
> fechou por reformulacao de criterio**, e as tres que **nao** podiam fechar — R2 de FIT-2026-004,
> R4 de FIT-2026-002 e IC-2 — **continuam abertas**, inclusive quando fecha-las teria melhorado
> este relatorio.

Permanece o numero a vigiar: **nenhum `inapto` em sete oportunidades**.

### Nota de conflito de interesse (PI-10)

| Campo | Conteudo |
|---|---|
| Conflitos identificados | **Dois.** **(1)** DEP-QAR **aprovou** a REV-ESTRUTURAL-I e executa este `FIT`. **(2)** DEP-GOV **aprova** este parecer tendo sido **autor da forma** daquela revisao |
| Por que nao invalidam | **(1)** O objeto deste `FIT` **nao inclui** a REV: sao sete artefatos, **nenhum produzido por DEP-QAR** (FT-02). **(2)** DEP-GOV **nao produziu** nenhum dos sete objetos avaliados |
| Desvios aplicados | Aprovacao transferida de DEP-EXE para DEP-GOV (CX-3); verificacao do ato executada por **DEP-QAR e DEP-GOV**, nenhum dos quais produziu os artefatos ratificados |
| Alternativa recusada | Escalar a aprovacao ao **SOBERANO** — recusada por proporcionalidade *(objeto C2/Tipo 2)* e porque o Soberano **determinou** esta missao |
| **Residuo** | A estrutura **nao comporta** segregacao completa com 4 de 9 departamentos com Carta e **um unico autor**. **Declarado em vez de omitido**, em R3 e RE-03. Desaparece quando DEP-GOV tiver Carta e existirem agentes |

## Aprendizado gerado

| Registro APR | Licao |
|---|---|
| [MEM-APR-0002](../../memory/aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md) | **Quinta confirmacao, com alcance ampliado pela quarta vez:** o mecanismo chegou a *documento que diverge de si proprio* — **quatro ocorrencias na mesma missao** (IC-8, RE-04, RE-05, RE-07). **A auditoria por varredura confere projecao contra fonte, e nao confere a fonte contra si mesma.** Acao: toda propagacao deve **somar as tabelas da fonte**, nao apenas compara-las com a projecao. Dono: DEP-GOV |
| A gravar por DEP-KMS *(QG-5)* | **Ratificacao e transicao de estado sao inseparaveis, e por isso o ato nao pode vincular o arquivo.** A regra so apareceu quando um ato exigiu *"comprovar que nenhuma alteracao ocorreu"* — e a resposta ja existia na pratica de `MSG-2026-0001`, sem estar escrita. Acao: **pratica que funciona duas vezes vira regra antes da terceira**. Dono: DEP-GOV |
| A gravar por DEP-KMS *(QG-5)* | **Gatilho e criterio de consolidacao mediam coisas diferentes, e por isso a proposta nunca teve objeto.** Dois ciclos abriram e encerraram EV-08 sem consolidar nada. Acao: **todo gatilho que dispara uma proposta deve verificar a existencia do objeto que a proposta consolidaria** — antes de disparar. Dono: DEP-EXE |
| A gravar por DEP-KMS *(QG-5)* | **Serie de medicoes sem composicao itemizada nao e serie.** Quatro medicoes de custo de contexto foram registradas como numeros isolados; a quinta, ao ser itemizada, revelou que a comparacao nunca foi verificavel. Acao: **toda metrica de serie declara sua composicao na primeira medicao**. Dono: DEP-KMS |

## Historico de vereditos sobre este objeto

| FIT | Data | Veredito | Relacao |
|---|---|---|---|
| FIT-2026-006 | 2026-07-28 | `apto-com-ressalva` | Ativacao dos pilotos; rollout **ADJUST**; EV-08 **aberta**; 4 pendencias ao Soberano |
| **FIT-2026-007** | 2026-07-28 | **`apto-com-ressalva`** | **Supera a leitura** de R1 e R2 de FIT-2026-004 quanto ao estado *(de `nao-avaliavel` para medido e para aberto-aplicavel)*, e **endurece** o criterio de R4 de FIT-2026-002, **sem editar nenhum dos dois** (M1, LV-04, FT-09) |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-QAR | Verificacao de aptidao da **Missao 1.8**: seis perguntas com sinal observavel; **7 ressalvas** e **7 achados** fechados; **F5 sobe para 21,3%** e revela que a serie **nao era comparavel** (achado RE-08), mantendo **R4 de FIT-2026-002 aberta** com criterio endurecido; **4 ressalvas** novas; rollout **GO-CONDITIONAL**; **uma** pendencia escalada ao Soberano. |
