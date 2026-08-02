---
id: RFC-0010-criterio-de-horizonte-avaliavel
titulo: Por qual instrumento se formaliza o criterio de horizonte avaliavel e de consolidacao determinado pelo Soberano
tipo: rfc
versao: 1.0.0
status: aprovado
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0003, ADR-0004, ADR-0008, ADR-0012]
substitui: []
substituido_por: null
resumo: Propoe o instrumento de formalizacao do criterio de consolidacao determinado pelo ato soberano de 2026-07-28, comparando emenda a FND-09, ADR autonomo e nota de decisao.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# RFC-0010: Criterio de horizonte avaliavel e de consolidacao — por qual instrumento

## Proposito
Escolher o **instrumento** que formaliza o criterio determinado pelo
[ato soberano de 2026-07-28](../memory/operacional/MSG-2026-0003-ato-soberano-emenda-qar-e-criterio-de-consolidacao.md),
item 2, que responde a pendencia **PS-1**.

> **O conteudo do criterio nao esta em discussao.** Ele foi **determinado pelo Soberano** e esta
> transcrito em [MSG-2026-0003 §1.1](../memory/operacional/MSG-2026-0003-ato-soberano-emenda-qar-e-criterio-de-consolidacao.md).
> Esta RFC decide **onde ele vive** e **como se torna operavel** — nada mais. Propor conteudo
> alternativo ao determinado seria simular uma escolha que ja nao existe (LM-03, PI-01).

## Escopo
| Item | Definicao |
|---|---|
| Inclui | O instrumento de formalizacao; a leitura operavel dos termos *camada concluida*, *consumo por camada posterior* e *prova vertical*; o alcance sobre `EV-08` e sobre FND-02 §9.3 |
| **Nao** inclui | O **merito** do criterio *(determinado)*; a criacao de entidade, tipo documental, camada ou ontologia; qualquer alteracao a FND-01 §5, que define o que **e** um horizonte |
| Prazo de analise | Encerrada na mesma missao — o ato determina a formalizacao e nao fixa prazo maior |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| Proponente | **DEP-GOV** | Guardiao normativo; dono de `EV-08` junto a DEP-EXE |
| Revisor | **DEP-QAR** | AC-03; nao produziu o pacote de PS-1 |
| Aprova a forma | **DEP-GOV** | FND-09 §8.2, linha `RFC` |
| Decide | **DEP-EXE** | FND-04 §2.1, C2 |

---

## 1. Contexto

**PS-1** foi a unica pendencia escalada pela Primeira Revisao Estrutural
([FIT-2026-007 §Pendencia](../governance/fitness/FIT-2026-007-revisao-estrutural-i.md)). O
diagnostico, medido, e o achado **RE-06**:

| Fato medido | Fonte |
|---|---|
| **Sete ciclos** consecutivos de crescimento do acervo | FIT-2026-007 §F1 |
| **Zero** consolidacoes executadas em sete ciclos | idem |
| **Duas** propostas de consolidacao abertas e encerradas **sem objeto** | REV-ESTRUTURAL-I §8 |
| O gatilho `R3` dispara por **crescimento**; `EV-08` exige **horizonte fechado** | REV-ESTRUTURAL-I §8.3 |
| **Nenhum horizonte se fechou** em sete ciclos | REV-ESTRUTURAL-I §3.2 |

**O Soberano decidiu.** Escolheu a opcao **(c)** das tres oferecidas — *determinar outro
criterio* — e ordenou a formalizacao **pelo rito aplicavel**, declarando que o ato **nao edita
diretamente FND-09**.

**Se nada mudar:** o criterio existe como **ato** e nao como **norma**, e a proxima revisao
estrutural volta a medir crescimento contra um criterio que nenhum documento operacionaliza.

## 2. Problema / Pergunta de decisao

> **Em que instrumento vive o criterio determinado, de modo que `EV-08` (FND-09 §12) e os
> gatilhos de consolidacao (FND-02 §9.3) passem a ter definicao operavel de *horizonte*, sem
> criar segunda fonte da mesma regra e sem que o ato precise de ratificacao que ele nao concede?**

## 3. Criterios de decisao

> Preenchidos **antes** de examinar as opcoes (CD-01, FND-07 §4.1).

| # | Criterio | Como se mede |
|---|---|---|
| **J1** | **Entra em vigor sem ato adicional do Soberano** | O instrumento alcanca `ativo` sob a classe que lhe cabe. O ato declara: *"nao ratifica futura emenda C3"* |
| **J2** | **Fonte unica** | O criterio vive em **um** lugar; os demais o **referenciam** (MM-01, PJ-01) |
| **J3** | **Alcanca os dois consumidores** | `EV-08` de FND-09 §12 **e** os gatilhos de consolidacao de FND-02 §9.3 |
| **J4** | **Nao amplia o universo** | Entidades, tipos documentais, camadas, ontologias e documentos fundacionais criados. Meta: **0** |
| **J5** | **Respeita o limite do ato** | *"Este ato nao edita diretamente FND-09"* |
| **J6** | **Reversibilidade** | O que e preciso desfazer se o criterio se mostrar errado |

## 4. Opcoes

### Opcao A — Emendar **FND-09 §12**, inscrevendo o criterio na linha de `EV-08`

| Campo | Conteudo |
|---|---|
| Como funciona | A linha *"Entidade sem instancia por um horizonte"* passa a trazer a definicao operavel de horizonte, e o texto de `EV-08` recebe D1 a D4 |
| Classe | **C2.** FND-09 ja foi emendada por C2 duas vezes — **1.1.0** (ADR-0005) e **1.3.0** (ADR-0008). Nao toca principio, linha vermelha, hierarquia nem direito de decisao |
| A favor | O criterio fica **na fonte** que o consome; quem le `EV-08` le a definicao junto |
| **Contra** | **Falha J3.** `EV-08` alcanca **entidade sem instancia**; o criterio determinado alcanca **toda revisao de consolidacao**, inclusive os quatro sinais de **FND-02 §9.3**, que `EV-08` nao cobre. Inscreve-lo so em FND-09 §12 **sub-escopa** a determinacao |
| Contra, 2 | **Tensiona J5.** O ato declara nao editar FND-09 *diretamente*; emenda-lo pelo rito e admissivel, mas escrever ali um criterio de alcance maior que a linha que o hospeda cria **regra em lugar errado** |
| Contra, 3 | **Falha J2 se corrigida.** Cobrir os dois consumidores exigiria escrever o mesmo criterio **tambem** em FND-02 §9.3 — duas fundacionais com o mesmo texto normativo, exatamente a duplicacao que PJ-01 proibe e que [MEM-APR-0002](../memory/aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md) registra como padrao recorrente |
| Avaliacao | J1 passa · **J2 falha** *(se corrigida para cobrir J3)* · **J3 falha** · J4 passa · **J5 tensiona** · J6 passa |

### Opcao B — **ADR autonomo** que fixa o criterio; FND-09 §12 e FND-02 §9.3 o consomem *(recomendada)*

| Campo | Conteudo |
|---|---|
| Como funciona | Um ADR institui as regras `HZ-01` a `HZ-08`: crescimento como gatilho de revisao, definicao operavel de horizonte avaliavel, os seis antecipadores e a validade do resultado *"nenhum candidato elegivel"*. **Nenhum documento fundacional e emendado**; ambos os consumidores passam a ler *horizonte* por `HZ-02`, pela hierarquia normativa de FND-01 §10 |
| Classe | **C2 / Tipo 2** — altera um **padrao** de revisao (FND-04 §2, C2) |
| A favor | **Precedente exato, tres vezes:** [ADR-0010](../decisions/ADR-0010-contrato-de-conhecimento-do-soberano.md), [ADR-0011](../decisions/ADR-0011-contrato-de-carta-de-departamento.md) e [ADR-0012](../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md) instituiram contrato ou regra **sem emendar fundacional** — o ultimo declara literalmente *"documentos fundacionais: 0 emendados"* |
| A favor, 2 | **Fonte unica que alcanca os dois consumidores** sem escrever a regra duas vezes |
| A favor, 3 | **Cumpre J5 na letra e no espirito:** zero linhas de FND-09 alteradas |
| Contra | O criterio fica em **M1** (FND-10 §6.2): evoluir exige **superar** o ADR, nao versiona-lo |
| Contra, 2 | Quem le `EV-08` **nao ve** o criterio ali: precisa saber que ele existe. Mitigado por `HZ-07`, que declara o vinculo, e pelo registro no catalogo mestre |
| Avaliacao | **J1 passa** · **J2 passa** · **J3 passa** · **J4 passa** *(0/0/0/0)* · **J5 passa** · **J6 passa** *(§10 do ADR)* |

### Opcao C — **Nota de Decisao** (C1)

| Campo | Conteudo |
|---|---|
| Como funciona | Registro leve, sem ADR |
| **Contra** | **Falha por definicao.** C1 muda *como* algo e feito dentro de norma ja aprovada (FND-04 §2); aqui **nao ha** norma aprovada que defina horizonte avaliavel — e ela que se cria. **GV-03:** na duvida, a classe mais alta |
| Avaliacao | **J1 passa** · J2 passa · **J3 falha** *(Nota de Decisao nao vincula documento fundacional)* · J4 passa · J5 passa · **J6 falha** *(sem plano de reversao nem gatilho)* |

### Opcao Z — Nao formalizar

| Campo | Conteudo |
|---|---|
| O que acontece | O criterio permanece **ato**, nao norma. A proxima revisao estrutural o consulta em `MSG-2026-0003`, que tem `ttl: 1 ciclo` |
| **Custo real** | **O ato determina a formalizacao.** Nao formalizar e descumprimento direto (PI-13, LM-05). E o efeito duravel morreria com o `ttl` da Diretiva — exatamente o defeito que §7.1 daquela Diretiva existe para evitar |
| Avaliacao | **Recusada** — contraria determinacao expressa |

## 5. Recomendacao do proponente

**Opcao B.**

| # | Fundamento |
|---|---|
| 1 | **E a unica que satisfaz J2 e J3 ao mesmo tempo.** A opcao A cobre um consumidor e, ao cobrir os dois, duplica |
| 2 | **Nao inventa instrumento:** repete o desenho que ja funcionou tres vezes seguidas, com o mesmo fundamento e o mesmo tradeoff declarado |
| 3 | **Cumpre o limite do ato na letra:** zero linhas de FND-09 alteradas, hoje e no futuro deste instrumento |
| 4 | **Nao cria ontologia.** *Camada*, *horizonte* e *prova vertical* sao lidos contra o que ja existe — FND-01 §5 e FND-02 §9.3 —, e a leitura e declarada como **regra de aplicacao**, nao como entidade nova (MT-01, CS-01) |

## 6. A leitura operavel — o que cada termo do ato significa quando aplicado

> Sem esta secao o criterio nao e verificavel, e criterio nao verificavel repete o defeito de
> `EV-08` que **RE-06** nomeou.

| Termo do ato | Leitura operavel proposta | Ancorado em |
|---|---|---|
| **Horizonte** | Os horizontes **H1, H2 e H3** de FND-01 §5 — *ordem de precedencia*, nunca prazo de calendario. **Nenhum horizonte novo e criado** | FND-01 §5 |
| **Camada concluida** | O conjunto de artefatos que satisfaz o **criterio de conclusao** de um objetivo `OB-Hx.y` de FND-01 §5, declarado satisfeito com evidencia | FND-01 §5 |
| **Consumida por camada posterior** | Um artefato pertencente a camada seguinte **declara vinculo formal** — `depende-de`, `implementa`, `consome` ou `valida` (FND-09 §6.1.1) — a um artefato da camada concluida | FND-09 §6.1.1 |
| **Prova vertical** | Um unico caso real **atravessa** a camada de ponta a ponta, exercendo cada portao aplicavel, e o percurso esta registrado | FND-01 §6.2 |
| **Antecipar a revisao** | Qualquer dos **seis** sinais do ato dispara a revisao **antes** de o horizonte tornar-se avaliavel — nunca dispensa a evidencia individual | Ato, item 2 |

> **Nenhuma destas leituras cria termo novo.** As cinco sao **remissoes** a norma vigente. Onde a
> norma nao responde, a lacuna e declarada em §8, nao preenchida por inferencia (PI-10, LM-03).

## 7. Impacto previsto

| Dimensao | Impacto |
|---|---|
| Documentos fundacionais | **0 emendados.** FND-09 §12 e FND-02 §9.3 permanecem literalmente como estao |
| Entidades · tipos · camadas · ontologias · templates | **0** criados |
| Regras novas | **8** — `HZ-01` a `HZ-08` |
| Ressalvas afetadas | **R2 de FIT-2026-007** *(criterio de consolidacao)* — fecha · **R3 de FIT-2026-005** e **R3 de FIT-2026-006** — o gatilho passa a ter criterio |
| Achado afetado | **RE-06** — fecha |
| Quem passa a fazer algo novo | **DEP-EXE** e **DEP-QAR**: toda revisao de consolidacao passa a declarar candidatos **um a um**, com evidencia individual |
| Custo de contexto | **+1** ADR e **+1** RFC, ambos fora do nucleo obrigatorio |

## 8. Perguntas em aberto

| # | Pergunta | Quem decide | Estado |
|---|---|---|---|
| **Q4** | Quem **declara** que uma camada esta concluida — DEP-EXE, DEP-GOV ou o Soberano? | **DEP-EXE com parecer de DEP-GOV**, por analogia ao rito de FND-02 §9.4 | **Resolvida no ADR**, `HZ-06`. Nao ha materia constitucional: declarar conclusao **nao** cria autoridade nova (AU-09) |
| **Q5** | O horizonte **H1** ja e avaliavel hoje? | DEP-EXE + DEP-QAR, na proxima revisao estrutural | **Aberta — e deliberadamente nao respondida aqui.** Respondê-la nesta RFC seria executar a revisao dentro do instrumento que a regula |
| **Q6** | *"Prova vertical"* exige produto real, ou basta um caso que atravesse os portoes? | **DEP-EXE** | **Aberta.** A leitura de §6 exige **portoes exercidos**, e nao produto; se a pratica mostrar que sem produto a prova e vazia, o gatilho de revisao do ADR dispara |

## 9. Manifestacoes

| Departamento | Posicao | Observacao |
|---|---|---|
| **DEP-GOV** *(proponente)* | Opcao **B** | Dono de `EV-08` com DEP-EXE |
| **DEP-QAR** *(revisor)* | **De acordo com B.** Registra que a Opcao A tem melhor localizacao e pior alcance, e que a diferenca **e** o achado RE-06 | Nao produziu o pacote de PS-1 |
| **DEP-EXE** *(decide)* | Aprova a Opcao B | Dono de `R3`; e quem passa a executar a avaliacao candidato a candidato |
| **DEP-KMS** *(evidencia)* | Sem objecao | Forneceu as medicoes de crescimento dos sete ciclos |

## 10. Resultado

| Campo | Conteudo |
|---|---|
| Estado | **Aceita** |
| Aceito | **Opcao B**, integralmente, com a leitura operavel de §6 → [ADR-0013](../decisions/ADR-0013-criterio-de-horizonte-e-consolidacao.md) |
| **Nao decidido** | **Q5** e **Q6** — registradas como abertas, com dono e gatilho. **Nao sao escaladas ao Soberano:** nenhuma e materia dele, e reescala-las inflaria a contagem de pendencias (LM-06) |
| Data | 2026-07-28 |
| Aprovado por | **DEP-EXE**, com parecer de forma de **DEP-GOV** e revisao de **DEP-QAR** |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-GOV | Proposta inicial: tres opcoes de instrumento mais "nao formalizar" para o criterio de horizonte avaliavel determinado pelo ato soberano de 2026-07-28. Aceita — Opcao B, ADR autonomo sem emendar fundacional, com leitura operavel de cinco termos. **Q5 e Q6 abertas**, nao escaladas. |
