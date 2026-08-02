---
id: FIT-2026-010-aplicacao-do-ato-soberano
titulo: Aptidao arquitetural da aplicacao do ato soberano de 2026-07-29 — cobertura vigente 9/9, emenda constitucional e regime do Fitness Check
tipo: fitness
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-QAR
proprietario: DEP-QAR
aprovador: DEP-GOV
criado_em: 2026-07-29
atualizado_em: 2026-07-29
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0011, ADR-0012, ADR-0014, ADR-0015]
substitui: []
substituido_por: null
objeto_avaliado: [DEP-GOV, DEP-TLS, DEP-PRD, DEP-OPS, DEP-GRW, ADR-0014, FND-01, ADR-0015, MSG-2026-0004, IDX-departamentos, artifact-registry]
classe_mudanca: C3
classe_avaliacao: aptidao
veredito: apto-com-ressalva
resumo: Verifica se a aplicacao do ato soberano de 2026-07-29 deixou a arquitetura mais apta a evoluir; veredito apto-com-ressalva, quatro ressalvas e fechamento GO-CONDITIONAL.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-GOV
ratificacao: nao-exigida
---

# FIT-2026-010: Aplicacao do ato soberano de 2026-07-29

## Proposito
Verificar se a **aplicacao** do ato de 2026-07-29 — cinco Cartas em vigor, emenda **C3** a
FND-01 promulgada e regime do `Fitness Check` formalizado — deixou a arquitetura **mais apta a
evoluir**.

> **Obrigatorio por QG-6** sobre mudanca **C3** (FND-01 §6.2; FND-09 §10.2).

> **Este `FIT` nao se ratifica, e o fundamento e novo.** Ate hoje o campo `ratificacao:
> nao-exigida` de um `FIT` era **inferencia com duvida declarada**; a partir de **`FT-10`**
> ([ADR-0015](../../decisions/ADR-0015-fitness-check-e-parecer-nao-decisao.md)) e **regra**.
> **Este e o primeiro `FIT` do acervo emitido sob fundamento normativo, e nao sob leitura.**

## Escopo
| Item | Definicao |
|---|---|
| Objeto avaliado | As **cinco** Cartas ativadas · `ADR-0014` em vigor · **`FND-01` 1.4.0** · `ADR-0015` · `MSG-2026-0004` · `IDX-departamentos` 1.2.0 · catalogo mestre |
| Estado anterior | **134 artefatos, 36.888 linhas** *(`BL-2026-07-29-02`)*; **4 de 9** Cartas em vigor; **19** ressalvas abertas; **9** vereditos consecutivos `apto-com-ressalva` |
| **Nao** inclui | O **merito** do ato · as duas emendas **nao ratificadas** *(RD-07)* · `DEP-QAR` 1.2.0, **ratificada e nao aplicada** |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| **Executa** | **DEP-QAR** | FT-02, CV-08 — nao produziu nenhum dos objetos avaliados |
| Forma | DEP-GOV | |
| Evidencia | DEP-KMS | Medicoes de hash, linha, link e acervo |
| **Aprova** | **DEP-GOV** | **Desvio declarado.** DEP-EXE e **autor das nove Cartas** (`DEP-EXE §10, I-2`). Cenario **CX-3**; quinta ocorrencia |
| Ratifica | **Nao aplicavel** | **`FT-10`** — parecer nao se ratifica. **Fundamento normativo, nao inferencia** |

---

## Sumario

| # | Pergunta | Resposta | Sinal |
|---|---|---|---|
| F1 | Complexidade aumentou sem ganho proporcional? | **Nao** | **+878 linhas (2,4%)** contra **cobertura vigente 9/9**, **IC-2 fechado apos 4 ciclos**, **Q2 respondida apos 2**, **6 artefatos saindo da retencao** e **1** fundacional emendada — **a unica expressamente ratificada** |
| F2 | Algum conceito foi duplicado? **e** a prevencao foi aplicada? | **Nao · aplicada** | **1** fonte canonica do ato; **3** reproducoes barradas |
| F3 | Alguma abstracao ficou desnecessaria? | **Nao** | **6** regras novas *(`FT-10` a `FT-15`)*, **5 delas com membro observado**; `IR-07` ganha **exercicio preditivo** |
| F4 | Continua mais simples de evoluir? | **Sim** | **Cinco** perguntas que exigiam julgamento passam a ter resposta na fonte |
| F5 | Custo de contexto subiu ou desceu? | **SUBIU** — **15,1%** contra 13,3% | **8a medicao, 4a itemizada.** **A serie de descidas quebra**, e a causa esta declarada |
| F6 | Favorece reutilizacao? | **Sim** | **`H-P` projetado** e **minuta preenchida** viram procedimento padrao de todo ato futuro |

**Veredito:** `apto-com-ressalva` — **quatro** ressalvas, todas com dono e gatilho.
**Fechamento da camada: `GO-CONDITIONAL`** (§Fechamento).

---

## F1 — A complexidade aumentou sem ganho proporcional?

| Medida | Antes | Depois | Variacao |
|---|---|---|---|
| Artefatos | 134 | **137** | **+3** |
| Linhas | 36.888 | **37.766** | **+878 (2,4%)** |
| **Cartas em vigor** | **4** | **9** | **+5 — cobertura vigente 9/9** |
| **Artefatos retidos por falta de ato** | **6** | **0** | **−6.** Primeira vez, em quatro atos, que a fila zera |
| Documentos fundacionais | 10 | **10** | **0** criados |
| **Documentos fundacionais emendados** | — | **1** | **FND-01 1.4.0** — a **unica** expressamente ratificada; FND-02 a FND-10 **intactas** |
| Entidades · tipos · camadas · portoes · departamentos | 21·33·5·7·9 | **21·33·5·7·9** | **0** |
| Regras normativas novas | — | **6** *(`FT-10` a `FT-15`)* | **+6** |
| **Achados e ressalvas fechados** | — | **4** | **IC-2** · **RC-03** · **Q2/G1/G2** · **L-1** |
| Achados **novos** | — | **3** *(RD-07, RD-08, RD-09)* | **0** corrigidos; 3 com dono e gatilho |
| Artefatos **M1** editados | — | **0** | Nenhum `FIT`, `REV`, `MSG` ou baseline anterior |
| Cartas de Capability alteradas | — | **0** | — |
| Agentes, skills, workflows, specs, produtos, codigo, infra | — | **0** | Conforme determinacao |
| Indices atualizados *(M3 derivado)* | — | **5** | — |

**Leitura.** O acrescimo e **pequeno** e a contrapartida e **a maior da serie em efeito
normativo**: a cobertura **vigente** alcanca a documental depois de dois ciclos parada em 4/9;
**IC-2 fecha na fonte**, nao por contencao, depois de **quatro ciclos**; e **Q2**, escalada desde
ADR-0012 §5.5, volta decidida e formalizada.

**Contrapartida honesta:** **seis regras novas**, **tres achados novos**, e **duas emendas que o
ato nao alcancou** — RC-05 e RC-07 seguem abertos, agora por **defeito de forma do ato**, e nao
por falta de instrumento.

**Resposta:** **nao**.

## F2 — Algum conceito foi duplicado? E a prevencao foi aplicada?

| Conceito | Onde ja estava | Como a mudanca o trata |
|---|---|---|
| **O ato de 2026-07-29** | — | **Fonte canonica unica:** `MSG-2026-0004`. As tres Diretivas anteriores **nao foram editadas**. Quatro atos, quatro fontes |
| **O diff da emenda C3** | `RFC-0011 §3.2` | **Referenciado**, nao recopiado — nem em ADR-0014, nem em MSG-2026-0004, nem aqui |
| **Os hashes das cinco Cartas** | `PS-2026-002 §2` | `MSG-2026-0004 §2.1` os republica **como vinculo do ato**, com finalidade distinta declarada, e aponta a fonte |
| **O regime do `FIT`** | RFC-0011 §5.2 *(texto proposto)* | **Um** instrumento: `ADR-0015`. O texto de FND-10 §10.3 **nao** foi editado — §5.3 daquele ADR |

**3 reproducoes barradas · 0 duplicacoes novas.**

> **A prevencao mais relevante foi nao emendar FND-10 e FND-09.** Havia texto pronto em
> RFC-0011 §5.2 e uma determinacao soberana que o justificava — e **o ato nao mencionou as duas
> fundacionais**. Aplicar seria **LM-03**: ler autorizacao no silencio. **A divergencia ficou
> declarada como RD-09**, e essa e a decisao mais conservadora que esta missao tomou.

**Resposta:** nao houve duplicacao nova · prevencao **aplicada**.

## F3 — Alguma abstracao ficou desnecessaria?

| Abstracao | Membros antes | **Membros agora** | Veredito |
|---|---|---|---|
| **`FT-10` a `FT-15`** *(regime do parecer)* | — | **5 de 6 com membro observado** | **Justificada.** Cinco descrevem pratica ja exercida em **9** `FIT`; so `FT-13` *(contestacao)* nasce com **zero** — declarado em ADR-0015 A1 |
| **`IR-07`** *(tres hashes no registro)* | 6 artefatos | **12 artefatos** · **exercicio preditivo inedito** | **Justificada e ampliada.** `H-P` publicado **antes** do ato e conferido depois, em **6 de 6** |
| **`IR-09`** *(reconstrucao)* | 3 artefatos | **9 artefatos** | **Justificada** — reproduziu `H-A` em **6 de 6** nesta aplicacao |
| **`DC-09`** *(Carta nao vigora por si)* | 4 exercicios | **9 exercicios** | **Justificada.** Exercida **9 de 9 vezes sem excecao** |
| **`HZ-01` a `HZ-08`** | 0 membros | **0 membros** | ⚠️ **Suspeita mantida** — terceiro ciclo. R1 de FIT-2026-008, intacta |
| **`IR-11`** *(contencao terminologica)* | 1.210 ocorrencias, 0 violacoes | **redundancia benigna** | **Nao revogada.** Com IC-2 fechado na fonte, ela deixa de ser a unica protecao — e revoga-la seria decisao propria |

**Resposta:** **nao**.

## F4 — O sistema continua mais simples de evoluir?

| Mudanca-tipo | Antes | Depois | Aprovacoes |
|---|---|---|---|
| **Saber se um departamento pode agir** | Carta escrita, **sem vigencia** em 5 de 9 | **9 de 9 em vigor** | Inalterado |
| **Saber se *ratificar* significa dar vigencia** | Duas acepcoes na Constituicao, contidas por regra de redacao | **FND-01 §7.3 distingue os dois institutos, e §11 define Homologacao** | Inalterado |
| **Saber se um `FIT` exige ratificacao** | Duas fundacionais em conflito, com duvida declarada | **`FT-10`** — regra, com fundamento | Inalterado |
| **Provar que um ato foi aplicado sem desvio** | Reconstruir depois e comparar | **`H-P` publicado antes; conferido no ato** | Inalterado |
| **Emitir o proximo ato** | Levantar hash de outro arquivo | **Minuta preenchida no proprio pacote** | Inalterado |

**Nenhuma aprovacao nova foi criada; nenhum papel ganhou veto; nenhum titular mudou** — X9 de
MSG-2026-0004.

**Contrapartida:** **duas fundacionais** passam a divergir da regra vigente *(RD-09)*, e **um
ADR em vigor contradiz o proprio cabecalho** *(RD-08)*.

**Resposta:** **sim**.

## F5 — A mudanca reduz ou aumenta o custo de contexto?

| Papel / tarefa-tipo | Antes | Depois | Direcao |
|---|---|---|---|
| **Piso obrigatorio de qualquer tarefa** | 1.099 linhas | **1.106 linhas** | **SOBE 7** — FND-01 e `nucleo`, e a emenda acrescenta 7 linhas |
| **Executar e aplicar um ato soberano** | — | **15,1%** — 8a medicao | **primeira da especie** |
| **Saber quem homologa e quem ratifica** | Julgamento sobre texto ambiguo | **Uma nota normativa em FND-01 §7.3** | **desce** |
| Acervo total | 36.888 | **37.766** | **sobe 2,4%** |

### F5.1 A medicao, itemizada — **a quarta da serie**

**Pacote minimo medido: 5.581 linhas sobre 36.888 = 15,1%.** Composicao **itemizada**:

| Bloco | Linhas |
|---|---|
| **Artefatos integrais** — FND-01 *(1.3.0)*, RFC-0011, ADR-0014, ADR-0012, PS-2026-003, PT-2026-001, e as **cinco** Cartas ativadas | **4.155** |
| **Recortes normativos** — FND-09 §8, FND-10 §5.2/§5.4/§10.3, FND-04 §2 | **280** |
| **Extracoes por ferramenta** — frontmatter e hash das 9 Cartas; §7.3 e §11 de FND-01 | **286** |
| **Indices abertos para propagar (C11)** | **860** |
| **Total** | **5.581** |

**A serie observada e 23% · 33% · 30,6% · 18,5% · 21,3% · 18,9% · 13,3% · 15,1%.**

> ### A serie de descidas quebra aqui, e o motivo esta declarado
> **A 7a medicao desceu a 13,3% porque a missao era de verificacao** — abriu poucos indices.
> **Esta e de aplicacao de ato**: exige carregar as cinco Cartas integrais, a Constituicao, a RFC
> e o ADR da emenda, e propagar por **cinco** indices. **A subida e da natureza da missao, nao
> da arquitetura** — exatamente o que a licao da Missao 1.9 mandou declarar ao lado do numero.
>
> **R4 de FIT-2026-002 permanece aberta**, e o criterio endurecido em FIT-2026-009 se confirma
> util: se a ressalva tivesse sido fechada com duas descidas de mesma causa, esta subida a teria
> reaberto no ciclo seguinte. **O gatilho continua sendo uma descida em missao de producao.**
>
> **O piso obrigatorio subiu 7 linhas, e e a primeira subida do piso desde a Missao 1.4.** Uma
> emenda a FND-01 alcanca **todo** carregamento do sistema, porque FND-01 e `nucleo`. **7 linhas
> em 1.099 e 0,6%** — declarado, nao dissimulado.

**Resposta:** **subiu** — **e a subida esta explicada por composicao e por natureza da missao.**

## F6 — Ela favorece reutilizacao?

| Definicao produzida | Reutilizavel por | Especifica do caso? |
|---|---|---|
| **`H-P` projetado antes do ato, conferido depois** | **Todo ato de ratificacao futuro** — exercido em **6 de 6** | Nao |
| **Minuta preenchida no pacote soberano** | **Todo pacote soberano futuro.** Resposta a RD-05 | Nao |
| **`FT-10` a `FT-15`** | **Todo parecer** — `FIT` e `REV`, presentes e futuros | Nao |
| **Formalizar determinacao sem emendar a fundacional nao mencionada** | **Toda determinacao soberana** que nao enumere o documento a emendar | Nao |
| **Recusar item de ato com identificador invalido, sem recusar o ato inteiro** | **Todo ato com multiplos objetos** | Nao |
| RD-07, RD-08, RD-09 | — | **Sim** |

**Evidencia mais forte:** **a granularidade da recusa**. O ato trouxe **oito** objetos; **seis**
foram aplicados e **dois** recusados, sem que a recusa contaminasse o resto. **Ate hoje o acervo
so conhecia ato inteiro aceito ou missao inteira bloqueada.**

**Resposta:** **sim**.

---

## Ressalvas

| # | Ressalva | Custo assumido | **Dono** | **Gatilho de reavaliacao** |
|---|---|---|---|---|
| **R1** | **`RD-09` — `FND-10 §10.3` e `FND-09 §8.2` divergem de `FT-10`.** Duas fundacionais dizem que `FIT` se ratifica; a regra vigente diz que nao | **A colisao de institutos saiu de FND-01 e reapareceu em outras duas fundacionais.** IC-2 fechou; **o mecanismo nao** | **DEP-GOV** | **Proximo ato soberano que alcance FND-09 ou FND-10** |
| **R2** | **`RD-07` — duas emendas nao ratificadas por identificador invalido.** **RC-05** e **RC-07** seguem abertos em Cartas em vigor | **Terceiro ciclo** com defeito conhecido retido em Carta ratificada. O instrumento existe e **nao foi consumido por defeito de forma** | DEP-GOV; **SOBERANO** | **Reemissao do item 2 do ato** |
| **R3** | **`RD-08` — `ADR-0014` esta `ativo` e abre com *"NAO ESTA EM VIGOR"*.** Corrigir exige ato novo | Um artefato **em vigor** cujo primeiro paragrafo nega a propria vigencia. **Efeito nulo** — o frontmatter e a fonte —, **assimetria real** | DEP-EXE | Proxima emenda a `ADR-0014` |
| **R4** | **`RD-02` permanece aberto, e continua sendo o unico achado que toca autoridade.** A ambiguidade de veto Guarda × Plataforma em FND-02 §4 **nao foi alcancada por este ato** | **E o que impede `GO-TO-SPECS`.** Nove Cartas em vigor **nao bastam** se a fonte nao resolve quem veta quem | **DEP-GOV** | Proxima emenda a **FND-02**, ou primeiro veto real sobre Plataforma |

## Veredito

| Campo | Conteudo |
|---|---|
| Veredito | **`apto-com-ressalva`** |
| Fundamento | As seis perguntas tem sinal observavel. **A cobertura vigente alcanca 9/9**; **IC-2 fecha na fonte apos quatro ciclos**, com **zero titulares alterados**; **Q2 volta decidida e formalizada**; **a fila de artefatos retidos zera pela primeira vez em quatro atos**; e a integridade foi provada por **onze** verificacoes, entre elas a **conferencia de `H-P` contra valor publicado antes do ato**. Em contrapartida, **o custo de contexto sobe e o piso obrigatorio sobe com ele**, **seis** regras novas entram, **duas** fundacionais passam a divergir da regra vigente e **duas** emendas nao foram alcancadas por defeito de forma. **Nao e `inapto`** porque nenhuma contrapartida revela degradacao sem contrapartida verificavel. **Nao e `apto` sem ressalva** porque quatro dividas seguem abertas |
| Efeito | **Encerra a mudanca C3.** As quatro ressalvas viram divida declarada (FND-07 §9) |
| Data | 2026-07-29 |
| Executado por | **DEP-QAR** |
| Aprovado por | **DEP-GOV** — DEP-EXE impedido (CX-3) |
| Ratificado por | **Nao aplicavel — por `FT-10`**, e nao por leitura |

## Fechamento da camada — **`GO-CONDITIONAL`**

> **Criterio herdado sem alteracao** de [FIT-2026-008](FIT-2026-008-rollout-das-cartas.md):
> **(a)** cobertura 9/9, **(b)** autoridade inequivoca, **(c)** validacao independente,
> **(d)** rastreabilidade, **(e)** pacote soberano completo.

| # | Condicao | Estado | Evidencia |
|---|---|---|---|
| **(a)** | **Cobertura 9/9** | ✅ **CUMPRIDA — documental e vigente** | **9** Cartas, **9** em `ativo` · `ratificada`. **A condicao (a) nunca estivera cumprida quanto a vigencia** |
| **(b)** | **Autoridade inequivoca** | ⚠️ **CUMPRIDA COM RESSALVA** | **IC-2 fechado na fonte**; **76 de 76** linhas de autoridade com fonte citada; **0** autoridades autodeclaradas. **A ressalva e `RD-02`** — a fonte nao resolve o veto Guarda × Plataforma. **Melhora em relacao a FIT-2026-009, onde nao estava cumprida** |
| **(c)** | **Validacao independente** | ✅ **Cumprida** | **117** verificacoes de contrato · **11** verificacoes de eficacia do ato · **1.521** links com **0** quebrados · **0** autoverificacoes |
| **(d)** | **Rastreabilidade** | ✅ **Cumprida** | Cadeia **ato → versao → conteudo → estado** fechada por `H-A`, `H-N`, **`H-P` projetado e conferido** e `IR-09` em **6 de 6** |
| **(e)** | **Pacote soberano completo** | ✅ **Cumprida** | PS-2026-002 · PS-2026-003 · PT-2026-001 · **MSG-2026-0004** como fonte canonica unica |

### A decisao

| Campo | Conteudo |
|---|---|
| **Decisao** | **`GO-CONDITIONAL`** |
| **Condicao nomeada** | **`RD-02`** — a ambiguidade de FND-02 §4. **E a mesma condicao que PT-2026-001 §11.1 projetou para os tres cenarios de ato, e ela se confirmou** |
| **Por que nao `GO-TO-SPECS`** | Exige *"nenhuma divida que comprometa autoridade ou consumo"*. **RD-02 compromete autoridade**, e **RD-09** compromete a leitura de duas fundacionais |
| **Por que nao `READY-FOR-AMENDMENT-RATIFICATION`** | As emendas locais **nao impedem o fechamento**: RC-05 e RC-07 tem efeito nulo ou local, e as tres candidatas estao prontas |
| **Por que nao `BLOCKED`** | **O ato chegou, foi verificado e foi aplicado.** A pre-condicao 1 esta satisfeita e provada |
| **A camada esta pronta para consumo?** | **SIM, sob condicao.** As nove Cartas **vigoram** e podem ser consumidas (LM-02 satisfeito). O que resta e **uma ambiguidade de fonte**, nao uma lacuna de cobertura |
| **Desempenho** | **Nao exercido, logo nao comprovado.** **41 de 123** indicadores `definido, sem valor`. **Vigencia nao e competencia** — e a distincao que a camada existe para preservar |

## Pendencias para o SOBERANO — **duas**

| # | Pendencia | Origem | Se nao houver ato |
|---|---|---|---|
| **PS-5** | **As duas emendas nao ratificadas** — `DEP-KMS` 1.1.0 e `DEP-ENG` 1.1.0 | RD-07 | **RC-05 e RC-07 permanecem abertos** em Cartas em vigor |
| **PS-6** | **`RD-09`** — FND-10 §10.3 e FND-09 §8.2 divergem de `FT-10` | ADR-0015 §5.3 | A divergencia envelhece. **`FT-10` prevalece**; as duas fundacionais ficam desatualizadas |

> **PS-2, PS-3 e PS-4 saem da lista: as tres foram respondidas** pelo ato de 2026-07-29 — as
> cinco Cartas, a emenda C3 e o regime do `FIT`. **E a primeira vez que a lista de pendencias
> soberanas encolhe.**

### Nota sobre FT-04

| Verificacao | Estado |
|---|---|
| Vereditos emitidos | **10** |
| Consecutivos `apto` **sem nenhuma ressalva** | **0** — os dez com ressalvas |
| `inapto` emitidos | **0** — **em dez oportunidades** |
| Ressalvas e achados fechados neste ciclo | **4** |
| Achados novos | **3** |

FT-04 exige tres `apto` **sem ressalva**; nao e o caso. **Permanece o numero a vigiar: nenhum
`inapto` em dez oportunidades.**

## Aprendizado gerado

| Registro APR | Licao |
|---|---|
| A gravar por DEP-KMS *(QG-5)* | **Ato com multiplos objetos admite recusa granular.** Seis objetos aplicados e dois recusados, sem contaminar o resto. Acao: **todo ato multi-objeto e verificado objeto a objeto, e a recusa alcanca so o objeto defeituoso.** Dono: DEP-GOV |
| A gravar por DEP-KMS *(QG-5)* | **Fechar uma colisao na fonte nao fecha o mecanismo que a produziu.** IC-2 fechou em FND-01 e a mesma colisao reapareceu em FND-10 e FND-09 *(RD-09)*. Acao: **ao fechar colisao terminologica, varrer todas as projecoes do termo antes de declarar fechamento.** Dono: DEP-GOV |
| A gravar por DEP-KMS *(QG-5)* | **Emendar `nucleo` sobe o piso de todo o sistema.** FND-01 +7 linhas = +0,6% no piso obrigatorio de **toda** tarefa. Acao: **toda emenda a artefato `nucleo` declara o efeito no piso, ao lado do efeito normativo.** Dono: DEP-KMS |

## Historico de vereditos sobre este objeto

| FIT | Data | Veredito | Relacao |
|---|---|---|---|
| FIT-2026-008 | 2026-07-28 | `apto-com-ressalva` | Rollout; fechamento **`READY-FOR-RATIFICATION`** |
| FIT-2026-009 | 2026-07-29 | `apto-com-ressalva` | Verificacao; fechamento **`BLOCKED`**; rebaixou a condicao **(b)** |
| **FIT-2026-010** | 2026-07-29 | **`apto-com-ressalva`** | **Nao supera nem edita nenhum anterior** (M1, LV-04, FT-09). **Recupera a condicao (b)** para *cumprida com ressalva* e leva o fechamento de `BLOCKED` a **`GO-CONDITIONAL`** |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-QAR | Verificacao de aptidao da **aplicacao do ato soberano de 2026-07-29**: **cobertura vigente 9/9**, **IC-2 fechado na fonte** apos quatro ciclos com **zero titulares alterados**, **Q2 respondida e formalizada** em ADR-0015, e **a fila de artefatos retidos zerada** pela primeira vez em quatro atos. **`H-P` conferido contra valor publicado antes do ato em 6 de 6** — exercicio preditivo inedito de `IR-07`. **F5 sobe**, e a serie de descidas quebra com a causa declarada; **o piso obrigatorio sobe 7 linhas**, primeira subida desde a Missao 1.4. **Quatro ressalvas**; **tres achados novos** *(RD-07, RD-08, RD-09)*; fechamento **`GO-CONDITIONAL`**, com **RD-02** como condicao nomeada. **Primeiro `FIT` do acervo emitido sob `FT-10`** — fundamento normativo, nao inferencia. |
