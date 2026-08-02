---
id: ADR-0013-criterio-de-horizonte-e-consolidacao
titulo: Fixar o criterio de horizonte avaliavel e de revisao de consolidacao determinado pelo Soberano, sem emendar documento fundacional
tipo: adr
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0003, ADR-0004, ADR-0008, ADR-0010, ADR-0011, ADR-0012]
substitui: []
substituido_por: null
classe_mudanca: C2
tipo_decisao: 2
supera: []
superado_por: null
resumo: Fixa que crescimento e gatilho de revisao e nao obrigacao de consolidar, define quando um horizonte se torna avaliavel e legitima o resultado nenhum candidato elegivel com evidencia individual.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# ADR-0013: Criterio de horizonte avaliavel e de revisao de consolidacao

## Proposito
Formalizar, pelo rito aplicavel, o criterio de consolidacao **determinado pelo Soberano** em
2026-07-28 — sem emendar documento fundacional, sem criar entidade, tipo documental, camada,
ontologia ou horizonte novo.

## Escopo
| Item | Definicao |
|---|---|
| **Aplica-se a** | Toda revisao de consolidacao do sistema: `EV-08` de [FND-09 §12](../foundation/09-meta-model.md) e os gatilhos de [FND-02 §9.3](../foundation/02-estrutura-organizacional.md) |
| **Nao se aplica a** | Especializacao *(FND-02 §9.2, movimento simetrico e inverso)*; os horizontes **H1–H3** de FND-01 §5, que **nao sao redefinidos**; a decisao de **executar** uma consolidacao concreta |
| **Subordinado a** | FND-01 · FND-02 · FND-04 · FND-09. Em conflito, prevalece a fonte; a divergencia e defeito deste ADR |
| Origem | [Ato soberano de 2026-07-28, item 2](../memory/operacional/MSG-2026-0003-ato-soberano-emenda-qar-e-criterio-de-consolidacao.md) · [RFC-0010](../rfcs/RFC-0010-criterio-de-horizonte-avaliavel.md), Opcao B |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| Proponente | **DEP-GOV** | Guardiao normativo; codono de `EV-08` |
| Revisor independente | **DEP-QAR** | AC-03; nao produziu o pacote de PS-1 |
| Aprovador | **DEP-EXE** | FND-04 §2.1, linha C2 |
| Ratificador | **Nao aplicavel** | **C2/Tipo 2.** O ato declara *"nao ratifica futura emenda C3"*; esta decisao **nao e C3** e **nao se apoia** em ratificacao alguma |
| Executor | **DEP-EXE** *(avaliacao)* · **DEP-QAR** *(verificacao)* · **DEP-KMS** *(evidencia)* |

---

## 1. Contexto

Sete ciclos consecutivos de crescimento do acervo, **zero** consolidacoes, e **duas** propostas
de consolidacao abertas e encerradas **sem objeto**. O diagnostico esta medido em
[REV-ESTRUTURAL-I §8.3](../foundation/revisao-estrutural-01-2026-07-28.md) e registrado como
achado **RE-06**: *"o gatilho `R3` dispara por crescimento; `EV-08` exige horizonte fechado; os
dois nunca coincidem"*.

A pendencia **PS-1** foi a **unica** escalada pela Primeira Revisao Estrutural, com tres opcoes.
**O Soberano escolheu a terceira** — determinar outro criterio — e ordenou a formalizacao pelo
rito aplicavel, declarando que o ato **nao edita diretamente FND-09**.

**Se nada mudar:** o criterio existe como ato de `ttl: 1 ciclo` e nao como norma, e a proxima
revisao volta a medir crescimento contra criterio inaplicavel — pela **terceira** vez.

## 2. Problema / Pergunta de decisao

> **Onde vive o criterio determinado, e como ele se torna verificavel, de modo que `EV-08` e os
> gatilhos de FND-02 §9.3 passem a ter definicao operavel de *horizonte* — sem segunda fonte da
> mesma regra e sem depender de ratificacao que o ato nao concede?**

## 3. Criterios de decisao

> Herdados de [RFC-0010 §3](../rfcs/RFC-0010-criterio-de-horizonte-avaliavel.md), declarados
> antes das alternativas (CD-01).

| # | Criterio |
|---|---|
| J1 | Entra em vigor **sem ato adicional** do Soberano |
| J2 | **Fonte unica** — o criterio vive em um lugar so |
| J3 | Alcanca os **dois** consumidores: `EV-08` e FND-02 §9.3 |
| J4 | **Nao amplia o universo** — 0 entidades, tipos, camadas, ontologias e fundacionais |
| J5 | Respeita o limite do ato: *"nao edita diretamente FND-09"* |
| J6 | **Reversibilidade** declarada |

## 4. Alternativas consideradas

Analise integral em [RFC-0010 §4](../rfcs/RFC-0010-criterio-de-horizonte-avaliavel.md).

### Alternativa A — Emendar FND-09 §12
Recusada: **falha J3 e, se corrigida para satisfaze-lo, falha J2.** `EV-08` alcanca *entidade sem
instancia*; o criterio determinado alcanca **toda** revisao de consolidacao, inclusive os quatro
sinais de FND-02 §9.3. Cobrir os dois exigiria escrever o mesmo texto normativo em **duas**
fundacionais — a duplicacao que PJ-01 proibe e que [MEM-APR-0002](../memory/aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md)
registra como o padrao de defeito mais recorrente do acervo.

### Alternativa B — ADR autonomo, consumido pelos dois *(escolhida)*
Satisfaz J1 a J6. Repete o desenho de **ADR-0010**, **ADR-0011** e **ADR-0012** — contrato ou
regra em ADR, **zero** fundacionais emendadas.

### Alternativa C — Nota de Decisao (C1)
Recusada: **falha J3 e J6.** C1 opera *dentro* de norma ja aprovada; aqui a norma e o que se cria.
**GV-03** manda aplicar a classe mais alta na duvida.

### Alternativa Z — Nao formalizar
Recusada: contraria **determinacao expressa** do ato (PI-13, LM-05), e o efeito duravel morreria
com o `ttl` da Diretiva.

## 5. Decisao

**Decidimos fixar neste ADR o criterio de horizonte avaliavel e de revisao de consolidacao
determinado pelo Soberano, sob as regras `HZ-01` a `HZ-08`, sem emendar nenhum documento
fundacional e sem criar entidade, tipo, camada, ontologia ou horizonte.**

### 5.1 As oito regras `HZ`

| # | Regra | Origem |
|---|---|---|
| **HZ-01** | **Crescimento do acervo e gatilho de revisao de consolidacao — nunca obrigacao de consolidar.** Revisao disparada por crescimento que conclui *"nada a consolidar"* **cumpriu** o gatilho; nao o descumpriu. | Ato, item 2, §1 |
| **HZ-02** | **Um horizonte torna-se avaliavel quando, e somente quando, ocorrer ao menos uma destas duas condicoes:** **(a)** uma **camada concluida** for **consumida por camada posterior**; ou **(b)** uma camada concluida for **exercida em prova vertical**. Ate que uma delas ocorra, o horizonte e **nao avaliavel**, e a ausencia de consolidacao **nao e divida**. | Ato, item 2, §1 |
| **HZ-03** | **Leitura operavel dos tres termos de HZ-02**, por remissao a norma vigente — nenhum e definicao nova: **camada concluida** = conjunto de artefatos que satisfaz o **criterio de conclusao** de um objetivo `OB-Hx.y` de FND-01 §5, **declarado satisfeito com evidencia**; **consumo por camada posterior** = artefato da camada seguinte que **declara** `depende-de`, `implementa`, `consome` ou `valida` (FND-09 §6.1.1) sobre artefato da camada concluida; **prova vertical** = **um** caso real que atravessa a camada de ponta a ponta exercendo **cada portao aplicavel** de FND-01 §6.2, com o percurso registrado. | FND-01 §5 e §6.2; FND-09 §6.1.1 |
| **HZ-04** | **Seis antecipadores.** Qualquer um deles dispara a revisao de consolidacao **antes** de o horizonte tornar-se avaliavel: **(1)** duplicacao · **(2)** sobreposicao · **(3)** conflito de autoridade · **(4)** degradacao de recuperacao · **(5)** custo excessivo de contexto · **(6)** existencia de objeto substituido. **Antecipar a revisao nunca dispensa HZ-05.** | Ato, item 2, §2 |
| **HZ-05** | **"Nenhum candidato elegivel" e resultado valido de revisao de consolidacao** — desde que a revisao apresente **avaliacao e evidencia individual de cada candidato**, um a um, com o motivo da inelegibilidade. Revisao que conclua *"nada a consolidar"* **sem** a avaliacao individual e **devolvida**, nao aceita. | Ato, item 2, §3 |
| **HZ-06** | **A conclusao de uma camada e declarada por DEP-EXE, com parecer de DEP-GOV**, no mesmo rito de FND-02 §9.4. Declarar conclusao **nao cria autoridade nova** (AU-09): apenas constata que o criterio de conclusao de FND-01 §5 foi satisfeito, com evidencia. **Sem evidencia, a camada nao esta concluida.** | FND-02 §9.4; AU-09 |
| **HZ-07** | **Nenhum documento fundacional e emendado por esta decisao.** `EV-08` de FND-09 §12 e os gatilhos de FND-02 §9.3 permanecem **literalmente** como estao, e passam a ler *horizonte* por `HZ-02` **pela hierarquia normativa** de FND-01 §10 — ADR vigente vincula os niveis inferiores e complementa os superiores onde eles nao dispoem. **Divergencia entre este ADR e uma fundacional resolve-se a favor da fundacional**, e e defeito deste ADR. | FND-01 §10; PJ-01 |
| **HZ-08** | **`HZ-02` e criterio do Soberano.** Alterar as duas condicoes de avaliabilidade exige **ato do Soberano**; alterar `HZ-03` a `HZ-06` — que sao leitura operavel e rito — e **C2** com ADR que supere este. **Ampliar `HZ-04` sem rito e protecao que se dissolve sem que ninguem decida dissolve-la** (mesmo fundamento de IR-04). | PI-01; ADR-0012, IR-04 |

### 5.2 O que muda, na pratica, para quem executa uma revisao

| Antes | Depois |
|---|---|
| Crescimento dispara `R3`; a revisao **precisa** achar objeto para nao parecer omissa | `HZ-01`: crescimento dispara **revisao**; achar *"nada a consolidar"* e resultado legitimo |
| *"Horizonte"* nao tem definicao operavel; **nenhum** se fechou em sete ciclos | `HZ-02` e `HZ-03`: duas condicoes verificaveis, ambas com fonte declarada |
| Antecipar a revisao nao tinha criterio | `HZ-04`: **seis** sinais observaveis |
| *"Nenhum candidato elegivel"* parecia falha da revisao | `HZ-05`: e resultado valido — **com evidencia individual obrigatoria** |
| Quem declara camada concluida: **indefinido** | `HZ-06`: **DEP-EXE com parecer de DEP-GOV**, com evidencia |

### 5.3 Efeito imediato sobre o acervo — aplicado, nao presumido

| Objeto | Efeito | Fundamento |
|---|---|---|
| **PS-1** | **RESPONDIDA** — opcao (c) do Soberano, formalizada aqui | Ato, item 2 e 3 |
| **RE-06** | ✅ **FECHADO** — *"a cobertura de EV-08 nunca foi testavel"* deixa de ser verdade: `HZ-02` a torna testavel | §5.1 |
| **R2 de FIT-2026-007** | ✅ **FECHA** — o gatilho de reavaliacao era literalmente *"PS-1 — decisao sobre o que fecha um horizonte"*, e a decisao ocorreu | FIT-2026-007 §Ressalvas |
| **R3 de FIT-2026-005** e **R3 de FIT-2026-006** | 🟡 **MANTIDAS, com o defeito removido.** As duas determinam escalar se `EV-08` fechar sem consolidar; **`HZ-01` retira a leitura de que isso e falha**. Nao fecham: o gatilho delas e o **proximo** ciclo de crescimento, e ele nao ocorreu ainda | REV-ESTRUTURAL-I §5.1 |
| **`EV-08` sobre os 17 tipos sem instancia** | **NAO reaberta nesta missao.** `HZ-02` a torna avaliavel **quando** uma das duas condicoes ocorrer; declarar agora que ocorreu seria executar a revisao dentro do instrumento que a regula | Q5 de RFC-0010, aberta |

### 5.4 O que esta decisao **nao** faz

| Nao faz | Por que |
|---|---|
| Nao emenda FND-09, FND-02 nem FND-01 | `HZ-07`; e o limite expresso do ato |
| Nao cria horizonte novo | Os tres de FND-01 §5 permanecem os unicos |
| Nao cria entidade, tipo documental, camada, ontologia ou template | `MT-01`, `CS-01`; nenhum e necessario |
| Nao declara que H1 esta concluido | Materia da **proxima revisao estrutural**, com evidencia. Q5 de RFC-0010 |
| Nao executa consolidacao nenhuma | Fixa **criterio**; executar e ato da revisao (AU-06) |
| Nao valida retroativamente o encerramento de `EV-08` na Missao 1.8 | `HZ-05` vale para diante. Aquele encerramento **ja** trazia evidencia individual dos quatro candidatos ([REV-ESTRUTURAL-I §8.2](../foundation/revisao-estrutural-01-2026-07-28.md)) — satisfazia o criterio **antes** de ele existir, e e por isso que nao precisa ser refeito |
| Nao altera **quem** aprova ou ratifica coisa alguma | AU-09; nenhuma linha de FND-01 §7.3 ou FND-09 §8.2 tocada |

## 6. Justificativa

**J2 e J3 juntos derrubam a Alternativa A.** O criterio determinado alcanca **duas** normas
distintas — `EV-08` e FND-02 §9.3. Inscrito em uma, sub-escopa; inscrito nas duas, duplica. O ADR
autonomo e a **unica** forma de ter um texto normativo que os dois consomem.

**J5 e literal.** O ato diz *"nao edita diretamente FND-09"*. A Alternativa B nao a edita
**de forma alguma** — nem direta, nem pelo rito. Zero linhas.

**J1 e verificavel.** C2/Tipo 2 alcanca `ativo` sem ratificacao (FND-04 §2.1). A Alternativa A,
ainda que classificada C2, **abriria a duvida** — e GV-03 mandaria tratar a duvida como C3, que o
ato **expressamente nao ratifica**. A decisao que nao abre a duvida e melhor que a que a abre e
depois a resolve.

**Tradeoff aceito, e nomeado:** o criterio nasce em **M1**. Corrigi-lo exige **superar** este ADR,
nao versiona-lo. Aceita-se pelo mesmo motivo de ADR-0011 §6: a alternativa que permitiria
versionar e exatamente a que falha nos criterios de maior peso.

**Segundo tradeoff, declarado:** quem le `EV-08` em FND-09 §12 **nao ve** `HZ-02` ali. O custo e
**um salto de referencia**, e e o mesmo custo que ADR-0010, ADR-0011 e ADR-0012 ja impuseram tres
vezes. **A alternativa a esse salto e a duplicacao**, que custa mais e ja tem cinco ocorrencias
registradas de defeito no acervo.

## 7. Impacto

| Dimensao | Impacto |
|---|---|
| **Documentos fundacionais emendados** | **0** — `HZ-07`. FND-09 §12 e FND-02 §9.3 permanecem literalmente como estao |
| Entidades · tipos documentais · camadas · ontologias · horizontes · templates | **0** criados |
| Regras novas | **8** — `HZ-01` a `HZ-08` |
| Departamentos afetados | **DEP-EXE** *(declara camada concluida; executa a avaliacao)* · **DEP-GOV** *(parecer; guarda o criterio)* · **DEP-QAR** *(verifica a evidencia individual de HZ-05)* · **DEP-KMS** *(mede crescimento e custo de contexto)* |
| Ressalvas fechadas | **R2 de FIT-2026-007** |
| Achados fechados | **RE-06** |
| Documentos a atualizar | Catalogo mestre · indices de decisoes e de RFCs · README da raiz |
| Custo de contexto | **+1** ADR e **+1** RFC, ambos fora do nucleo obrigatorio. O nucleo permanece **1.099 linhas** |
| Ganho PI-14 | **Organizacao** — a pergunta *"esta revisao podia concluir 'nada a consolidar'?"* passa de julgamento a **duas condicoes verificaveis** mais uma exigencia de evidencia. **Reducao de contexto** — a revisao deixa de reabrir candidatos cuja inelegibilidade ja foi demonstrada individualmente |

## 8. Evidencias

| # | Evidencia | Origem | Confianca | O que discrimina |
|---|---|---|---|---|
| E1 | **7 ciclos de crescimento, 0 consolidacoes** | [FIT-2026-007 §F1](../governance/fitness/FIT-2026-007-revisao-estrutural-i.md) | **Alta** | Que o problema e real e medido, nao antecipado |
| E2 | **2 propostas de consolidacao abertas e encerradas sem objeto** | REV-ESTRUTURAL-I §8; FIT-2026-006 | **Alta** | Que o defeito e do **criterio**, nao do acervo |
| E3 | **Nenhum horizonte fechado em 7 ciclos** | REV-ESTRUTURAL-I §3.2 | **Alta** | Que `EV-08` era **inaplicavel por construcao** |
| E4 | **Os 4 candidatos de EV-08 testados um a um, todos inelegiveis** | REV-ESTRUTURAL-I §8.2 | **Alta** | Que `HZ-05` **formaliza pratica ja executada**, e nao teoria |
| E5 | **FND-09 emendada por C2 duas vezes** *(1.1.0, 1.3.0)* | Historico de FND-09 | **Alta** | Que a Alternativa A era **viavel**, e foi recusada por alcance — nao por impossibilidade |
| E6 | **Precedente estrutural triplo:** ADR-0010, ADR-0011 e ADR-0012 instituiram regra sem emendar fundacional | Os tres ADRs | **Alta** | Que a Alternativa B ja funcionou tres vezes com o mesmo desenho |
| **A1** | **Evidencia ausente, declarada:** **nenhuma** camada foi ainda declarada concluida sob `HZ-06`, e **nenhuma** prova vertical ocorreu. `HZ-02` nasce com **zero** membros observados | Varredura do acervo, 2026-07-28 | — | Que o criterio e desenhado **antes** de haver caso — e a razao do gatilho de §12 |
| **A2** | **Evidencia ausente, declarada:** os **seis** antecipadores de `HZ-04` sao do ato; **nenhum** foi exercido sob esta regra | Ato, item 2 | — | Que `HZ-04` tambem nasce com zero membros |

## 9. Riscos e mitigacao

| # | Risco | Prob. | Impacto | Mitigacao |
|---|---|---|---|---|
| **RH-1** | **`HZ-02` nunca dispara**, e o criterio novo repete o defeito do antigo por outro caminho | **Media** | **Alto** | `HZ-04` fornece **seis** vias independentes de antecipacao que **nao** dependem de horizonte. E o gatilho de §12 mede exatamente isto: duas revisoes estruturais sem que `HZ-02` nem `HZ-04` disparem |
| **RH-2** | **`HZ-05` vira desculpa:** toda revisao conclui *"nenhum candidato elegivel"* e a evidencia individual vira formalidade | **Media** | Medio | `HZ-05` exige **motivo da inelegibilidade por candidato**; **DEP-QAR** verifica, e revisao sem isso e **devolvida**. Tres revisoes seguidas com o mesmo resultado somam-se ao contador de complacencia de FND-02 §9.4 |
| **RH-3** | **Oito regras novas com zero membros observados** — quarto ciclo consecutivo instituindo regime preventivo inteiro *(FR, PJ, CT, DC, IR, agora HZ)* | **Alta** | Medio | Declarado em **A1** e **A2**. Medicao obrigatoria no Fitness Check: quantas das oito foram exercidas, nominalmente |
| **RH-4** | **`HZ-03` ser lido como definicao nova** de *camada*, e virar ontologia por acumulo | Media | **Alto** | `HZ-03` e **remissao**: cada termo aponta um paragrafo vigente. **`HZ-07`** declara a subordinacao. Criar ontologia continua sendo **C3** com rito proprio (FND-09 §11.1) |
| **RH-5** | **Esta decisao estar errada** — o criterio do Soberano ser inaplicavel na pratica | Baixa | Medio | Sinal em §12. O criterio e **do Soberano**; se falhar, o que se supera e **este instrumento**, nunca a determinacao — que so ele altera (`HZ-08`) |

## 10. Plano de reversao

| Campo | Conteudo |
|---|---|
| Reversivel? | **Sim — Tipo 2** |
| Como desfazer | **(1)** Novo ADR superando este (SU-01), declarando o que mudou. **(2)** Nada mais: **nenhum documento fundacional foi emendado**, entao nao ha texto a restaurar. **(3)** As revisoes ja executadas sob `HZ` permanecem validas como historico |
| Custo da reversao | **Documental integral.** Nenhum dado vivo, nenhuma exposicao externa, nenhuma migracao, nenhuma credencial. Nenhum arquivo apagado (PI-07, RB-05) |
| Janela | **Permanente.** Nao ha efeito irreversivel em nenhum ponto |
| O que **nao** se reverte | A **determinacao do Soberano**. Superar este ADR retira o instrumento, nao o ato — e o criterio voltaria a existir sem forma operavel, que e o estado que esta decisao corrige |
| Backup necessario (PI-07) | Nenhum dado vivo e tocado. A integridade do estado anterior esta na baseline **`BL-2026-07-28-05`**, preservada e nao editada, e na copia datada de **117** arquivos tomada antes das edicoes |

## 11. Classificacao

| Campo | Valor | Justificativa |
|---|---|---|
| Classe | **C2 — Estrutural** | Altera um **padrao** de revisao (FND-04 §2, C2). **Nao** altera principio imutavel, linha vermelha, hierarquia normativa nem direito de decisao: `HZ-06` **constata** autoridade existente e nao a cria (AU-09) |
| Tipo | **2 — reversivel** | §10 |
| Decisor | **DEP-EXE**, com parecer de DEP-GOV | FND-04 §2.1 |
| Ratificacao | **Nao exigida** | C2/Tipo 2. **Nao se apoia** no ato de 2026-07-28 para vigorar — apoia-se nele apenas para o **conteudo**, que o ato determinou |
| Instrumento | **RFC → ADR** | [RFC-0010](../rfcs/RFC-0010-criterio-de-horizonte-avaliavel.md) |
| Fitness Check | **Obrigatorio** | [FIT-2026-008](../governance/fitness/FIT-2026-008-rollout-das-cartas.md) |
| Data da decisao · vigencia | 2026-07-28 · 2026-07-28 | |

> **Por que C2 e nao C3.** C3 alcanca *"principio imutavel, linha vermelha, hierarquia normativa,
> direitos de decisao ou a propria Fundacao"*. Esta decisao **nao emenda a Fundacao** — `HZ-07`,
> verificavel por `diff`: zero linhas de FND-01, FND-02 ou FND-09 alteradas. **Nao altera direito
> de decisao:** `HZ-06` atribui a declaracao de camada concluida a DEP-EXE com parecer de DEP-GOV
> **por analogia ao rito ja vigente de FND-02 §9.4**, sem conceder autoridade que a matriz de
> FND-09 §8.2 nao ja preveja. **Nao toca a hierarquia:** o ADR entra no nivel 3, onde ADR vive.

## 12. Revisao

| Campo | Conteudo |
|---|---|
| Gatilho de reavaliacao | **Evento — cumulativo, o que vier primeiro** |
| Detalhe | **(a)** **Primeiro disparo real de `HZ-02`** — a primeira camada declarada concluida e consumida ou provada verticalmente. **(b)** **Duas revisoes estruturais consecutivas** em que **nem `HZ-02` nem nenhum dos seis `HZ-04` dispare** — sinal de que o criterio novo repete o defeito do antigo (RH-1). **(c)** **Terceira revisao consecutiva** que conclua *"nenhum candidato elegivel"* (RH-2) |
| O que se mede | Quantas das oito regras `HZ` foram exercidas, nominalmente; quantos candidatos receberam evidencia individual; se algum antecipador disparou |
| Sinal de que deu errado | Revisao que conclua *"nada a consolidar"* **sem** evidencia individual e seja **aceita**; ou `HZ-03` sendo citado para criar termo que nenhuma fundacional contenha; ou ampliacao de `HZ-04` sem ADR |
| Responsavel | **DEP-EXE** *(merito)* com **DEP-GOV** *(forma)* e **DEP-QAR** *(aptidao)* |

## 13. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Origem | **Ato soberano de 2026-07-28, item 2 e 3** — [MSG-2026-0003](../memory/operacional/MSG-2026-0003-ato-soberano-emenda-qar-e-criterio-de-consolidacao.md) · [RFC-0010](../rfcs/RFC-0010-criterio-de-horizonte-avaliavel.md), Opcao B |
| Pendencia que resolve | **PS-1** |
| Achado que fecha | **RE-06** |
| Ressalva que fecha | **R2** de FIT-2026-007 |
| Decisoes superadas | **Nenhuma** |
| Decisoes relacionadas | **ADR-0003** *(Meta Model; hospeda `EV-08`)* · **ADR-0004** *(QG-6 e `FIT`)* · **ADR-0008** *(uma fonte, multiplas projecoes — base de HZ-07)* · **ADR-0010**, **ADR-0011**, **ADR-0012** *(precedente de regra em ADR sem emendar fundacional)* |
| Normas que passam a ler *horizonte* por `HZ-02` | [FND-09 §12](../foundation/09-meta-model.md), linha `EV-08` · [FND-02 §9.3](../foundation/02-estrutura-organizacional.md) — **nenhuma das duas alterada** |
| Verificacao de aptidao | [FIT-2026-008](../governance/fitness/FIT-2026-008-rollout-das-cartas.md) |
| Revisao arquitetural | [REV-ROLLOUT](../foundation/revisao-arquitetural-rollout-cartas-2026-07-28.md) |

---

## Checklist de validade (FND-07 §4.1)
- [x] **VD-01** — 3 alternativas reais (A, B, C) + "nao fazer nada" (Z)
- [x] **VD-02** — criterios J1–J6 declarados em §3, antes de §4
- [x] **VD-03** — nenhuma alternativa de palha: **A e a mais obvia** *(escrever na fonte)* e foi recusada por alcance, com evidencia de que era viavel (E5)
- [x] **VD-04** — tradeoff explicito em §6: criterio em M1, e salto de referencia a partir de `EV-08`
- [x] **VD-05** — evidencia ausente declarada: **A1** e **A2**, ambas com zero membros observados
- [x] **VD-06** — plano de reversao em §10
- [x] **VD-07** — impacto em cascata mapeado em §7; **zero** fundacionais na lista
- [x] **VD-08** — data e responsaveis em §11 e no bloco Responsaveis
- [x] **VD-09** — gatilho de revisao em §12, com tres condicoes e sinal de erro

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-GOV | Decisao inicial: formaliza o criterio de horizonte avaliavel e de revisao de consolidacao determinado pelo ato soberano de 2026-07-28, sob `HZ-01` a `HZ-08`, **sem emendar nenhum documento fundacional**. Fecha **PS-1**, **RE-06** e **R2 de FIT-2026-007**. Nasce com **zero membros observados**, declarados em A1 e A2. |
