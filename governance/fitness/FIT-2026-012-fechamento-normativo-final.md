---
id: FIT-2026-012-fechamento-normativo-final
titulo: Aptidao arquitetural do fechamento normativo final — RD-14 e RD-15 tratados pelo rito, prova de consumo em cinco casos e liberacao para o Specification Framework
tipo: fitness
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-QAR
proprietario: DEP-QAR
aprovador: SOBERANO
criado_em: 2026-07-29
atualizado_em: 2026-07-29
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0012, ADR-0015, ADR-0018, ADR-0019]
substitui: []
substituido_por: null
objeto_avaliado: [RFC-0014, ADR-0018, PS-2026-007, RFC-0015, ADR-0019, PS-2026-008, PT-2026-003, artifact-registry]
classe_mudanca: C3
classe_avaliacao: aptidao
veredito: apto-com-ressalva
resumo: Verifica se o fechamento normativo da Missao 1.12 deixou a arquitetura mais apta a evoluir; veredito apto-com-ressalva, duas ressalvas novas, duas reclassificacoes e fechamento READY-FOR-RATIFICATION com cenario de GO-TO-SPECS alcancavel pela primeira vez.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-GOV
ratificacao: nao-exigida
---

# FIT-2026-012: Fechamento normativo final

## Proposito
Verificar se a **Missao 1.12** — verificacao da pre-condicao de aplicacao, tratamento de
**RD-14** e **RD-15** pelo rito **C3** e **prova de consumo por Specs** — deixou a arquitetura
**mais apta a evoluir**.

> **Obrigatorio por QG-6** sobre mudanca **C3** (FND-01 §6.2; FND-09 §10.2).
> **Este `FIT` nao se ratifica** — **`FT-10`**. **Terceiro `FIT` do acervo emitido sob
> fundamento normativo.**

## Escopo
| Item | Definicao |
|---|---|
| Objeto avaliado | **RFC-0014 → ADR-0018 → PS-2026-007** · **RFC-0015 → ADR-0019 → PS-2026-008** · **PT-2026-003** · catalogo mestre e `BL-2026-07-29-05` |
| Estado anterior | **147 artefatos, 40.429 linhas** *(`BL-2026-07-29-04`)*; **9 de 9** Cartas em vigor; **24** ressalvas abertas; **11** vereditos consecutivos `apto-com-ressalva` |
| **Nao** inclui | O **merito** dos dois pacotes · os **tres candidatos fundacionais**, que **nao entram no acervo** e **nao vigoram** · qualquer Spec — **nenhuma criada** · **FIT-2026-011**, que **nao foi editado** |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| **Executa** | **DEP-QAR** | FT-02, CV-08 — **nao produziu nenhum** dos objetos avaliados |
| Forma | **DEP-GOV** | FND-09 §8.2, linha `FIT` |
| Evidencia | **DEP-KMS** | Medicoes de hash, linha, link e acervo |
| **Aprova** | **SOBERANO** | **A cascata de `DEP-EXE I-2` chega ao terminus pela segunda vez** — §Nota de aprovacao |
| Ratifica | **Nao aplicavel** | **`FT-10`** |

### Nota de aprovacao — **a cascata chega ao terminus de novo, e a causa e a mesma**

| Candidato a aprovador | Impedido? | Por que |
|---|---|---|
| **DEP-EXE** | **Sim** | E **area alcancada** por ADR-0018 — passa a liberar `QG-1` — e por ADR-0019 — passa a aprovar Spec C2 |
| **DEP-GOV** | **Sim** | **Produziu 8 dos 8 objetos avaliados** — conferido campo a campo. Aprovar seria **autoverificacao no passo de aprovacao** |
| **SOBERANO** | — | **Terminus literal da cascata** |

> **Segunda ocorrencia consecutiva, e `PT-2026-003 §4.4` explica por que.** O terminus e
> **invariante** por `AU-10` e `PI-01`; o que se repete e a **concentracao de autoria**, medida
> desde `FIT-2026-006 R1`. **Este `FIT` fica emitido e pendente de aprovacao**, e `FT-14`
> preserva integralmente o seu efeito processual **sem depender de ato**.
>
> **Quarta ocorrencia de `RQ-2`** — impedimento cruzado — e **segunda em que os dois substitutos
> previstos estao impedidos ao mesmo tempo**. **O sinal para R1 de FIT-2026-006 deixou de ser
> forte e passou a ser sistematico.**

---

## Sumario

| # | Pergunta | Resposta | Sinal |
|---|---|---|---|
| F1 | Complexidade aumentou sem ganho proporcional? | **Nao** | **+8 artefatos** contra **RD-14 e RD-15 resolvidos pelo rito** e a **fila de bloqueios de autoridade sem instrumento zerada** — **zero fundacionais emendadas** |
| F2 | Algum conceito foi duplicado? **e** a prevencao foi aplicada? | **Nao · aplicada** | **5** reproducoes barradas; **0** duplicacoes novas; **0** pacotes anteriores reabertos |
| F3 | Alguma abstracao ficou desnecessaria? | **Nao** | **Zero regras novas criadas.** `W1`–`W6` e `T1`–`T5` sao **leitura de regras existentes** e **nao entram em texto normativo** |
| F4 | Continua mais simples de evoluir? | **Sim** | **Dez atos** do ciclo de Spec passam de indeterminados a respondidos na fonte — **se houver ato** |
| F5 | Custo de contexto subiu ou desceu? | **DESCEU** — **6,1%** contra 12,0% | **10a medicao, 6a itemizada. A mais baixa da serie** |
| F6 | Favorece reutilizacao? | **Sim** | **Prova de consumo executada duas vezes** e **reimplementacao de hash validada antes do uso** viram procedimento |

**Veredito:** `apto-com-ressalva` — **duas** ressalvas novas e **duas reclassificacoes**,
todas com dono e gatilho.
**Fechamento da camada: `READY-FOR-RATIFICATION`** (§Fechamento).

---

## F1 — A complexidade aumentou sem ganho proporcional?

| Medida | Antes | Depois | Variacao |
|---|---|---|---|
| Artefatos | 147 | **155** | **+8** |
| Linhas | 40.429 | **42.785** | **+2.356 (+5,8%)** |
| **Cartas em vigor** | **9** | **9** | **0** |
| **Documentos fundacionais emendados** | — | **0** | **FND-01 a FND-10 intactas.** Os **tres candidatos vivem fora do acervo** |
| **Cartas emendadas** | — | **0** | **As nove intactas**, `H-A` conferido contra a abertura |
| Entidades · tipos · camadas · portoes · departamentos · classes | 21·33·5·7·9·4 | **21·33·5·7·9·4** | **0** |
| **Regras normativas em vigor** | — | **0** | Os candidatos **nao vigoram sem ato** |
| **Achados e ressalvas fechados** | — | **2** | **RD-17** e **RD-20**, corrigidos na projecao |
| Achados **novos** | — | **4** | RD-17 e **RD-20** *(os dois resolvidos)*, RD-18 e RD-19 |
| Artefatos **M1** editados | — | **0** | Nenhum `FIT`, `REV`, `MSG`, `INC` ou baseline anterior |
| **Bloqueios de autoridade sem instrumento** | **2** | **0** | **B4 e B5 ganharam pacote** |
| Indices atualizados *(M3 derivado)* | — | **5** | — |
| **Pacotes soberanos emitidos** | — | **2** | Total pendente sobe a **5** |

**Leitura.** O acrescimo e **o menor da serie desde a Missao 1.9 em numero de artefatos**, e o
ganho e o **maior em efeito estrutural**: **a fila de bloqueios de autoridade sem instrumento
zerou**, e **pela primeira vez existe um cenario alcancavel que produz `GO-TO-SPECS`**
(PT-2026-003 §8.1).

**Contrapartida honesta:** **quatro achados novos**, e **o numero de artefatos retidos por falta
de ato dobrou** — de **2** para **4** —, porque produzir instrumento **aumenta a fila do
Soberano antes de diminui-la**.

**Resposta:** **nao**.

## F2 — Algum conceito foi duplicado? E a prevencao foi aplicada?

| Conceito | Onde ja estava | Como a mudanca o trata |
|---|---|---|
| **O mapa C0–C3 × Tipo 1/2** | FND-04 §2, §2.1, §2.2 | **RFC-0015 §3 o monta a partir das fontes e nao as reproduz** — cada celula cita a origem |
| **Os requisitos que a camada impoe as Specs** | `PT-2026-001 §7`, RS-1 a RS-10 | **PT-2026-003 §4 os testa e nao os reproduz** |
| **A matriz de FND-09 §8.2** | FND-09 §8.2 | **Nao reproduzida** em RFC-0015, ADR-0019 nem PS-2026-008 — os tres declaram **so as celulas que mudam** |
| **A tabela de portoes de FND-01 §6.2** | FND-01 §6.2 | **Nao reproduzida** — RFC-0014 e ADR-0018 declaram **so a linha `QG-1`** |
| **O merito de RD-09 e das emendas de Carta** | PS-2026-005, PS-2026-006 | **Referenciado, nao reaberto.** **Zero pacotes anteriores editados** |
| **O registro do ato** | `MSG-2026-0005` | **Nao editado.** Esta missao **nao consumiu ato**, e por isso **nao criou registro de ato** |

**5 reproducoes barradas · 0 duplicacoes novas · 0 pacotes anteriores reabertos.**

> **A prevencao mais relevante foi nao criar um `MSG` de ausencia de ato.** Havia motivo
> aparente — a missao verificou a pre-condicao e produziu a conclusao. **Registrar a ausencia
> como Diretiva teria criado um sexto ato que nao existe.** A ausencia vive em **PT-2026-003
> §1**, onde e **conclusao de verificacao**, e nao fonte canonica de ato.

**Resposta:** nao houve duplicacao nova · prevencao **aplicada**.

## F3 — Alguma abstracao ficou desnecessaria?

| Abstracao | Membros antes | **Membros agora** | Veredito |
|---|---|---|---|
| **`W1` a `W6`** *(classe de uma Spec)* | — | **5 casos observados** — os cinco da prova de consumo | **Justificada, e deliberadamente nao normativa.** **Nao entram no texto emendado**: a celula que **remete a classe** ja as convoca. **Zero regras criadas** |
| **`T1` a `T5`** *(terminus da cascata)* | — | **2 ocorrencias observadas** — FIT-2026-011 e este | **Justificada como determinacao, nao como norma.** `T5` declara que **generalizar exige instrumento proprio**, e nenhum foi criado |
| **`O1` a `O4`** *(rebase de pacotes concorrentes)* | — | **2 membros** — PS-2026-005 e PS-2026-008 | **Justificada, no limite.** Exatamente **dois**, o minimo de AQ-03. Vivem **no pacote**, nao em fundacional |
| **`IR-07`** *(tres hashes)* | 17 artefatos | **19 artefatos** | **Justificada e ampliada** |
| **`IR-02` invariante sob O4** | 12 artefatos | **14 artefatos** | **Justificada** — invariante em **2 de 2** novos |
| **`HZ-01` a `HZ-08`** | 0 membros | **0 membros** | ⚠️ **Suspeita mantida — quinto ciclo.** R1 de FIT-2026-008, intacta |
| **`PV-1` a `PV-4`** *(preservacao)* | 3 versoes | **3 versoes** | **Inalterada** — **nenhuma versao foi substituida nesta missao** |

**Resposta:** **nao**. **E o sinal mais forte e negativo: zero regras normativas foram criadas
numa missao que produziu dois pacotes C3.**

## F4 — O sistema continua mais simples de evoluir?

| Mudanca-tipo | Antes | Depois | Aprovacoes |
|---|---|---|---|
| **Saber quem libera `QG-1`** | **Duas respostas na mesma subsecao**, e a regra proibia a que a tabela dava | **`DEP-EXE`**, com o nome ja escrito em §7.3 | Inalterado |
| **Saber quem aprova uma Spec C2** | **Dois titulares**, sem regra de escolha executada | **`conforme classe`** — remissao a FND-04 §2 | Inalterado |
| **Saber quem ratifica uma Spec Tipo 1** | `—` numa tabela, **SOBERANO** noutra | **`SOBERANO se C3 ou Tipo 1`**, nas duas | Inalterado |
| **Saber se liberar portao e aprovar artefato** | **Nao respondido em lugar nenhum** | **Nota normativa em FND-01 §6.2 e em FND-09 §8.2** | Inalterado |
| **Saber o que fazer com impedimento duplo** | Resolvido **por desvio** em cinco ocorrencias | **Cascata seguida ao pe da letra, segunda vez**, com a causa raiz nomeada | Inalterado |
| **Saber a classe de uma Spec** | **Duas regras geradoras**, sem declaracao de qual prevalece | **Achado `RD-18`, declarado** — **nao resolvido** | Inalterado |

**Nenhuma aprovacao nova foi criada; nenhum papel ganhou veto; nenhum titular foi ampliado.**

**Contrapartida:** **quatro** das seis respostas acima **so passam a valer com ato**. Hoje sao
**texto de pacote**, e o `FIT` **nao as conta como vigentes**.

**Resposta:** **sim** — condicionado.

## F5 — A mudanca reduz ou aumenta o custo de contexto?

### F5.1 A medicao, itemizada — **a sexta da serie**

**Pacote minimo medido: 2.477 linhas sobre 40.429 = 6,1%.** Composicao **itemizada**:

| Bloco | Linhas |
|---|---|
| **Artefatos integrais** — FIT-2026-011, PT-2026-002, MSG-2026-0005, PS-2026-005 | **1.148** |
| **Recortes normativos** — FND-01 §6.2/§7.x e frontmatter, FND-04 §2 e §6, FND-09 §8, FND-10 §10.3, ADR-0012 §5, ADR-0017 abertura | **613** |
| **Extracoes por ferramenta** — `QG-1` nas fundacionais; §5, §10 e §12 de `DEP-PRD`; §10 de `DEP-EXE`; §6.3 e §7 de `DEP-ENG` e `DEP-QAR`; grep de `PS-2026-00[456]` | **197** |
| **Indices abertos para propagar (C11)** | **519** |
| **Total** | **2.477** |

**A serie observada e 23% · 33% · 30,6% · 18,5% · 21,3% · 18,9% · 13,3% · 15,1% · 12,0% ·
6,1%.**

> ### A segunda descida consecutiva itemizada — e ela fecha **R4 de FIT-2026-002**
> **R4 exige *duas descidas consecutivas itemizadas*.** A 9a medicao desceu a **12,0%**; esta
> desce de novo. **A ressalva fecha com evidencia**, e o criterio endurecido por FIT-2026-009
> **foi aplicado, nao contornado**: as duas descidas sao **itemizadas**, **consecutivas** e
> **medidas por ferramenta**.
>
> **A causa esta declarada e e verificavel:** **nenhuma das nove Cartas foi carregada
> integralmente**, e **nenhum dos pacotes anteriores alem de PS-2026-005** o foi. O que a
> missao consumiu deles foram **recortes extraidos por ferramenta** e a **consolidacao canonica
> de PT-2026-002 §2 e FIT-2026-011**, que existem exatamente para isso.
>
> **Limite declarado (PI-10).** **PS-2026-004, PS-2026-006, ADR-0016, RFC-0012 e RFC-0013 nao
> foram lidos integralmente.** Foram consumidos **por referencia**, atraves de PT-2026-002 §2 e
> FIT-2026-011 §Escopo, que sao suas consolidacoes canonicas. **Nenhuma afirmacao desta missao
> depende do texto integral deles**, e as que tocam seus objetos — RD-19 — usam **apenas os
> identificadores e as celulas publicadas em PS-2026-005 §2**, que **foi** lido integralmente.
>
> **O piso obrigatorio nao subiu:** **nenhuma fundacional foi emendada**. As emendas propostas
> subiriam o piso em **+10 linhas** *(FND-01)* e **+18** *(FND-09 e FND-10)* — declarado em
> PS-2026-007 §4 e PS-2026-008 §4, **antes** do ato, e **nao contabilizado aqui** porque
> **nao vigora**.

**Resposta:** **desceu** — **segunda descida consecutiva itemizada**, e **a menor medicao da
serie**.

## F6 — Ela favorece reutilizacao?

| Definicao produzida | Reutilizavel por | Especifica do caso? |
|---|---|---|
| **Executar a prova de consumo duas vezes — vigente e com pacotes — para medir o que o ato compra** | **Toda camada com pacote pendente** | Nao |
| **Validar a reimplementacao de hash contra artefatos de controle antes de medir candidato** | **Toda medicao de `H-A`/`H-N`** | Nao |
| **Verificar se a regra violada e projecao de PI antes de propor excecao** | **Todo pedido de quebra-vidro** | Nao |
| **Ler tabela normativa contra a regra que a acompanha, e nao so contra outros documentos** | **Toda tabela de FND** | Nao |
| **Tratar duplo impedimento recorrente como sinal de concentracao de autoria** | **Todo impedimento cruzado** | Nao |
| **Reproduzir a baseline pelo comando publicado antes de cita-la** | **Toda missao** | Nao |
| RD-17, RD-18, RD-19 | — | **Sim** |

**Evidencia mais forte:** **a prova executada duas vezes**. **40 de 55** contra **55 de 55** e
uma medida — nao uma opiniao — de **exatamente o que os cinco atos compram**. **A Missao 1.11
provou que o teste reprovava; esta mediu o tamanho da reprovacao.**

**Resposta:** **sim**.

---

## Ressalvas

| # | Ressalva | Custo assumido | **Dono** | **Gatilho de reavaliacao** |
|---|---|---|---|---|
| **R1** | **`RD-19` — dois pacotes pendentes reivindicam as mesmas versoes de FND-09 e FND-10.** A causa raiz e do acervo: **candidatos sao publicados como *diff + hash*, sem arquivo**, e por isso a emenda posterior **nao consegue se medir sobre a anterior** | **Aplicar um dos dois sobre base errada.** Mitigado por `O1`–`O4`, que **existem no pacote e nao em norma** | **DEP-GOV** | **Promulgacao do primeiro dos dois pacotes** |
| **R2** | **`RD-18` — FND-04 §6 e §2 geram a classe de uma Spec por criterios diferentes**, e o texto nao declara qual prevalece. A emenda **remete a §2** e deixa §6 como piso, **sem toca-lo** | A regra geradora **segue viva** — a mesma forma de defeito que RD-12 nomeou | **DEP-GOV** | **Proxima emenda a FND-04** |

### As duas seguintes sao **reclassificacoes**, e **nao entram na contagem de abertas**

> **Registrar de novo o mesmo objeto infla a divida e esconde o progresso.**

| # | Ressalva existente | De | **Para** |
|---|---|---|---|
| **R3** | **R1 e R2 de FIT-2026-011** *(`RD-14`, `RD-15`)* | *"achado de severidade Alta, bloqueante e **sem instrumento**"* | 🔁 **RECLASSIFICADAS** — *"tratadas pelo rito **C3 completo**, em **pacotes separados**, com RFC, ADR candidato, diff literal, hashes integrais e minuta. **Nao vigoram sem ato.**"* Gatilho novo: **ato sobre PS-2026-007 e PS-2026-008** |
| **R4** | **R4 de FIT-2026-002** *(reducao de custo de contexto)* | *"exige duas descidas consecutivas itemizadas; ha uma"* | ✅ **FECHADA COM EVIDENCIA** — **duas descidas consecutivas itemizadas**: **12,0%** *(9a)* e **6,1%** *(10a)*, ambas medidas por ferramenta. §F5.1 |

**Ressalvas abertas apos este ciclo: 24 + 2 − 1 = 25.** **Zero registradas em duplicidade.**

## Veredito

| Campo | Conteudo |
|---|---|
| Veredito | **`apto-com-ressalva`** |
| Fundamento | As seis perguntas tem sinal observavel. **A fila de bloqueios de autoridade sem instrumento zerou** — RD-14 e RD-15 receberam **rito C3 completo em pacotes separados** —, **zero regras normativas foram criadas** numa missao que produziu **dois pacotes C3**, **zero fundacionais e zero Cartas foram alteradas**, o **custo de contexto desce pela segunda vez consecutiva e fecha R4 de FIT-2026-002**, e a **prova de consumo executada duas vezes mediu exatamente o que os atos compram** — **40 de 55** contra **55 de 55**. Em contrapartida, **quatro achados novos**, **a fila do Soberano dobrou** de 2 para 4 artefatos retidos, e **nada do que a missao produziu de normativo esta em vigor**. **Nao e `inapto`** porque nenhuma contrapartida revela degradacao sem contrapartida verificavel. **Nao e `apto` sem ressalva** porque **25 dividas seguem abertas**, e porque **`RD-19` toca a aplicacao de pacotes que ja estavam na mesa do Soberano antes desta missao** |
| Efeito | **Encerra a mudanca C3.** As **duas** ressalvas novas viram divida declarada (FND-07 §9); **uma ressalva antiga fecha com evidencia**; as **duas reclassificacoes** alteram o estado de ressalvas existentes **sem duplica-las** |
| Data | 2026-07-29 |
| Executado por | **DEP-QAR** |
| Aprovado por | **SOBERANO** — **pendente**; DEP-EXE e DEP-GOV impedidos, cascata de `I-2` no terminus |
| Ratificado por | **Nao aplicavel — `FT-10`** |

## Fechamento da camada — **`READY-FOR-RATIFICATION`**

> **Criterio herdado sem alteracao** de [FIT-2026-008](FIT-2026-008-rollout-das-cartas.md):
> **(a)** cobertura 9/9, **(b)** autoridade inequivoca, **(c)** validacao independente,
> **(d)** rastreabilidade, **(e)** pacote soberano completo.

| # | Condicao | Estado | Evidencia |
|---|---|---|---|
| **(a)** | **Cobertura 9/9** | ✅ **CUMPRIDA** | **9** Cartas, **9** em `ativo` · `ratificada`, **nenhuma alterada nesta missao** |
| **(b)** | **Autoridade inequivoca** | ⚠️ **NAO CUMPRIDA — com instrumento pronto para todos os casos** | **Rebaixada em FIT-2026-011 por RD-14 e RD-15, que nao tinham pacote.** **Agora tem.** A condicao **so nao e cumprida porque os pacotes nao vigoram** — e **nao mais porque falta instrumento**. **Primeira vez em quatro ciclos que a causa e apenas o ato** |
| **(c)** | **Validacao independente** | ✅ **Cumprida** | **1.882** links com **0** quebrados · **94** artefatos com `autor` e `revisor`, **0** coincidencias · **0** credenciais · **6 de 6** hashes de controle reproduzindo · **11** verificacoes de integridade |
| **(d)** | **Rastreabilidade** | ✅ **Cumprida** | Cadeia **achado → RFC → ADR → pacote → diff → hash → minuta** fechada nos **dois** casos; `H-N` **invariante sob O4 em 2 de 2** |
| **(e)** | **Pacote soberano completo** | ✅ **Cumprida** | **PS-2026-007** e **PS-2026-008**, os dois com **minuta preenchida** e **hashes integrais de 64 caracteres** · **PT-2026-003** |

### A decisao

| Campo | Conteudo |
|---|---|
| **Decisao** | **`READY-FOR-RATIFICATION`** |
| **Condicao nomeada** | **Cinco atos** — PS-2026-004, 005, 006, **007** e **008**. **Zero instrumentos faltando** |
| **Por que nao `GO-TO-SPECS`** | Exige **pacotes vigentes e ciclo deterministico**. **O ciclo e deterministico — 55 de 55 —, mas so com os pacotes**, e **nenhum vigora**. C3 so existe com ato |
| **Por que nao `GO-CONDITIONAL`** | Afirma que a camada **pode ser consumida sob condicao**. **Ela nao pode:** `QG-1` segue sem liberador legitimo |
| **Por que nao `BLOCKED`** | **A ausencia de ato foi verificada e declarada, nao inferida.** Nenhum objeto foi recusado por defeito — **nao havia objeto a verificar** — e **tudo o que nao dependia de ato foi executado** |
| **A camada esta pronta para consumo?** | **NAO, e pela primeira vez a razao e apenas a assinatura.** Ha um ciclo a razao era **cobertura**; depois **ambiguidade de fonte**; depois **um portao sem instrumento**. **Agora todo bloqueio de autoridade tem pacote pronto** |
| **Desempenho** | **Nao exercido, logo nao comprovado.** **41 de 123** indicadores `definido, sem valor` |

## Pendencias para o SOBERANO — **seis**

| # | Pendencia | Origem | Se nao houver ato |
|---|---|---|---|
| **PS-5** | **`DEP-KMS` 1.1.0 e `DEP-ENG` 1.1.0** | PS-2026-006 | **RC-05 e RC-07 permanecem abertos** |
| **PS-6** | **`RD-09`** — FND-09 §8.2 e FND-10 §10.3 | PS-2026-005 | **`FT-10` prevalece**; a divergencia envelhece |
| **PS-7** | **`RD-02`** — FND-02 §4 | PS-2026-004 | **Quarto ciclo.** `DEP-EXE` e `DEP-KMS` seguem vetados **por Carta e nao pela fonte** |
| **PS-9** | **`RD-14`** — FND-01 §6.2 | **PS-2026-007** | **`QG-1` segue sem liberador legitimo. Nenhuma Spec pode ser aberta** |
| **PS-10** | **`RD-15`** — FND-09 §8.2 e FND-10 §10.3 | **PS-2026-008** | **Spec C2 e C3 seguem sem titular unico de aprovacao** |
| **PS-11** | **Aprovacao deste `FIT` e do `FIT-2026-011`** | Cascata de `DEP-EXE I-2` no terminus, **duas vezes** | Os vereditos **existem e produzem efeito processual** (`FT-14`); falta o **aceite formal** |

### Nota sobre FT-04

| Verificacao | Estado |
|---|---|
| Vereditos emitidos | **12** |
| Consecutivos `apto` **sem nenhuma ressalva** | **0** — os doze com ressalvas |
| `inapto` emitidos | **0** — **em doze oportunidades** |
| Ressalvas e achados fechados neste ciclo | **3** — **RD-17**, **RD-20** e **R4 de FIT-2026-002** |
| Achados novos | **4** |
| Condicao **rebaixada** neste ciclo | **0** — e a condicao **(b)** teve a **causa alterada**, de *"falta instrumento"* para *"falta ato"* |

FT-04 exige tres `apto` **sem ressalva**; nao e o caso. **Permanece o numero a vigiar: nenhum
`inapto` em doze oportunidades.** **Em contrapartida, este ciclo fechou uma ressalva de custo
com evidencia medida e abriu tres achados** — o oposto de complacencia, e sinal contra `RQ-1`.

## Aprendizado gerado

| Registro APR | Licao |
|---|---|
| A gravar por DEP-KMS *(QG-5)* | **Colisao normativa pode caber dentro de uma unica subsecao.** RD-14 opoe a tabela de FND-01 §6.2 a regra escrita **sete linhas abaixo**. Acao: **toda tabela normativa e lida contra a regra que a acompanha**. Dono: DEP-GOV |
| A gravar por DEP-KMS *(QG-5)* | **Excecao formal nao alcanca Principio Imutavel.** FND-01 §8.3 e literal, e isso **elimina alternativas antes da analise**. Acao: **antes de propor excecao, verificar se a regra e projecao de PI**. Dono: DEP-GOV |
| A gravar por DEP-KMS *(QG-5)* | **Candidato publicado como *diff + hash* sem arquivo impede a proxima emenda de se medir.** E RD-19. Acao: **candidato submetido a ato tem arquivo preservado fora do acervo, com caminho declarado no pacote**. Dono: DEP-KMS |
| A gravar por DEP-KMS *(QG-5)* | **Reproduzir a baseline pelo comando que ela publica e teste barato e nao era feito.** E RD-17. Acao: **a baseline e reproduzida antes de ser citada, e a exclusao e declarada por lista fechada**. Dono: DEP-GOV |
| A gravar por DEP-KMS *(QG-5)* | **Reconciliar catalogo e fonte por amostragem esconde a divergencia.** A verificacao **artefato a artefato** encontrou **18 de 153**, **14 anteriores a esta missao**. Acao: **a reconciliacao catalogo–fonte e executada por ferramenta sobre todos os artefatos declarados, nunca por amostra**. Dono: DEP-GOV |
| A gravar por DEP-KMS *(QG-5)* | **Executar a prova de consumo duas vezes mede o que o ato compra.** **40 de 55** contra **55 de 55**. Acao: **toda camada com pacote pendente reporta o resultado nos dois estados**. Dono: DEP-QAR |

## Historico de vereditos sobre este objeto

| FIT | Data | Veredito | Relacao |
|---|---|---|---|
| FIT-2026-009 | 2026-07-29 | `apto-com-ressalva` | Fechamento **`BLOCKED`** |
| FIT-2026-010 | 2026-07-29 | `apto-com-ressalva` | Fechamento **`GO-CONDITIONAL`** |
| FIT-2026-011 | 2026-07-29 | `apto-com-ressalva` | Fechamento **`READY-FOR-RATIFICATION`**; condicao **(b)** rebaixada por RD-14 e RD-15 |
| **FIT-2026-012** | 2026-07-29 | **`apto-com-ressalva`** | **Nao supera nem edita nenhum anterior** (M1, LV-04, FT-09). **Mantem o fechamento e muda a causa da condicao (b)**: de *"nao cumprida por falta de instrumento"* para *"nao cumprida por falta de ato"*. **Primeiro ciclo em que todo bloqueio de autoridade tem pacote pronto** |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-QAR | Verificacao de aptidao do **fechamento normativo da Missao 1.12**: **pre-condicao de aplicacao verificada e nao satisfeita**, **RD-14 e RD-15 tratados pelo rito C3 completo em pacotes separados** e **prova de consumo executada duas vezes** — **40 de 55 celulas** hoje contra **55 de 55** com os pacotes, nos cinco casos e nos cinco tipos de impedimento. **A fila de bloqueios de autoridade sem instrumento zerou**, e a condicao **(b)** muda de causa: de *"falta instrumento"* para *"falta ato"*. **F5 desce a 6,1% — segunda descida consecutiva itemizada —, e isso FECHA R4 de FIT-2026-002**, aberta desde a segunda missao. **Zero regras normativas criadas** numa missao com **dois pacotes C3**; **zero fundacionais, zero Cartas e zero artefatos M1 alterados**. **Quatro achados novos:** **RD-17** e **RD-20** *(os dois de projecao, **resolvidos**: a baseline nao reproduzia pelo comando publicado, e **18 de 153** contagens de linha do catalogo divergiam da fonte)*, **RD-18** *(FND-04 §6 × §2)* e **RD-19** *(pacotes concorrentes)*, os dois ultimos viram ressalvas **R1** e **R2**. Fechamento **`READY-FOR-RATIFICATION`**, com **cenario de `GO-TO-SPECS` alcancavel pela primeira vez** por atos que ja tem pacote. **Terceiro `FIT` emitido sob `FT-10`**, e **o segundo consecutivo cuja aprovacao percorre a cascata de `I-2` ate o SOBERANO** — quarta ocorrencia de `RQ-2`. |
