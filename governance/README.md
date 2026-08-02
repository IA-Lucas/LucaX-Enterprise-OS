---
id: IDX-governance
titulo: Registro de Governanca — Excecoes e Incidentes
tipo: relatorio
versao: 1.16.0
status: ativo
camada_memoria: operacional
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-QAR
criado_em: 2026-07-28
atualizado_em: 2026-08-01
revisao_prevista: null
decisoes_relacionadas: [ADR-0001, ADR-0004, ADR-0006, ADR-0008, ADR-0011]
substitui: []
substituido_por: null
resumo: Conta as sequencias EXC, INC e FIT e projeta o estado corrente de excecoes, incidentes, aptidao e baseline.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
projecao_de: governance/fitness/README.md; governance/incidents/README.md; artifact-registry.md §10
---

# Registro de Governanca

## Proposito
Manter o registro vivo de excecoes formais e incidentes de conformidade, conforme
[FND-04 §9 e §10](../foundation/04-governanca.md).

## Escopo
| Diretorio | Conteudo |
|---|---|
| [`exceptions/`](exceptions/) | Excecoes formais (`EXC-AAAA-NNN`) — autorizacoes temporarias do Soberano |
| [`incidents/`](incidents/) | Incidentes de conformidade (`INC-AAAA-NNN`) — violacoes detectadas |
| [`fitness/`](fitness/) | Verificacoes de aptidao arquitetural (`FIT-AAAA-NNN`) — portao QG-6 |

## Responsaveis
| Papel | Responsavel |
|---|---|
| Proprietario | DEP-GOV |
| Autoriza excecao | **SOBERANO** (indelegavel) |
| Verifica fechamento de incidente | DEP-QAR |
| Grava aprendizado | DEP-KMS |

---

## Contadores oficiais

| Sequencia | Ultimo atribuido | Proximo | Reinicia |
|---|---|---|---|
| `EXC-2026-NNN` | 000 | **001** | A cada ano |
| `INC-2026-NNN` | **002** | **003** | A cada ano |

**O contador de `FIT` NAO vive aqui.** Ele vive em [`fitness/README.md`](fitness/README.md),
com a serie de vereditos — **fonte unica**.

> **`RD-58` — ✅ FECHADO na Missao 1.13.4.1, pelo gatilho que o proprio achado declarou.**
> A linha `FIT-2026-NNN` **foi suprimida desta tabela**, e a supressao e a correcao: o defeito
> **nunca foi a divergencia — era a DUPLICATA** (`PJ-01`). Enquanto a linha existiu, ela
> divergiu da fonte **tres emissoes seguidas** *(declarava `016`/`017` contra `018`/`019` em
> [`fitness/README`](fitness/README.md), que a propria linha seguinte reconhecia como fonte)*, e
> a emissao anterior **corrigiu o valor sem remover a linha** — o que garantia a quinta
> ocorrencia. **Corrigir o valor de uma duplicata e adiar o defeito, nao fecha-lo.**
> O gatilho declarado era *"proxima emenda a este indice"*; esta e a emenda. **Quarta e ultima
> ocorrencia da familia dentro deste arquivo, apos `RD-04`, `RD-32` e `RD-52`.**

> **Correcao de defeito IX-02.** Ate 2026-07-28 este indice registrava `FIT-2026-001` como
> ultimo atribuido, um numero atras do real desde a Missao 1.3 — indice desatualizado apos
> mudanca aprovada e **mudanca incompleta**, nao norma nova (IX-02, CV-04). Corrigido, e
> registrado como achado **C11** de
> [REV-CONSOLIDACAO](../foundation/revisao-arquitetural-consolidacao-2026-07-28.md).

> **O MESMO DEFEITO REAPARECEU, e em quatro contadores — achado `RD-32`.** Ate esta missao,
> este indice e [`fitness/README`](fitness/README.md) declaravam `FIT` **`013` / `014`** com
> **`FIT-2026-014`** ja emitido; [`decisions/README`](../decisions/README.md) declarava
> **`0019` / `0020`** com **`ADR-0020`** ja existente; e [`rfcs/README`](../rfcs/README.md),
> **`0015` / `0016`** com **`RFC-0016`** ja existente. **4 tabelas, 8 valores.** Confiar em
> qualquer um deles produziria **colisao de identificador**, contra a regra literal de
> `FND-03 §2.3`. **A correcao de 2026-07-28 atingiu o valor e nao o gatilho `CV-04`** — e e por
> isso que reincidiu. A causa esta agora **codificada em regra**: **`SF-32`** de
> [ADR-0021](../decisions/ADR-0021-framework-de-specifications.md), *criar artefato de sequencia
> e incrementar o contador sao a mesma mudanca*. **Encontrado por exercer o contador, nao por
> le-lo** — [MEM-APR-0006](../memory/aprendizado/MEM-APR-0006-exercer-o-contador-revela-o-defeito.md) `V1`.

## Excecoes formais vigentes

| ID | Norma excepcionada | Autorizada em | **Expira em** | Status |
|---|---|---|---|---|
| — | *nenhuma excecao vigente* | — | — | — |

### Regras
| # | Regra |
|---|---|
| 1 | Somente o **Soberano** autoriza. Silencio nunca autoriza. |
| 2 | **Excecao sem prazo e invalida.** Nao ha renovacao tacita. |
| 3 | Ao expirar: estado regular restaurado, nova excecao explicita, ou norma alterada via RFC. |
| 4 | Excecao vencida e nao regularizada vira **incidente automaticamente**. |
| 5 | **Nao admitem excecao:** PI-01 a PI-14, LV-02, LV-05, LV-12. |

## Incidentes de conformidade

| ID | Norma violada | Severidade | Aberto em | Situacao |
|---|---|---|---|---|
| [INC-2026-001](incidents/INC-2026-001-ratificacao-inferida.md) | PI-01 · PI-06 · GV-05 · CM-07 · **LV-05** | **Alta** | 2026-07-28 | ✅ **`fechado`** — ato soberano em §11, verificacao em §12 |
| [INC-2026-002](incidents/INC-2026-002-ratificacao-declarada-em-fitness-check.md) | **LV-05** · GV-05 · CV-09 | Media | 2026-07-28 | ✅ **`fechado`** — ato soberano de 2026-07-28; comprovacao em §11.3. **Causa propria migrada para [RFC-0009 Q2](../rfcs/RFC-0009-integridade-e-alcance-do-ato-de-ratificacao.md), aberta** |

> **Os dois incidentes do sistema estao fechados, e nenhum dos dois teve a causa eliminada por
> completo.** INC-2026-001 fechou com causa **corrigida e exercida**. INC-2026-002 fechou com a
> causa herdada corrigida e a causa **propria** — a ambiguidade FND-10 §2.2 × §10.3 —
> **migrada para instrumento vivo**, nao resolvida. Manter a divida dentro de um incidente
> `fechado` a congelaria em documento **M1**; move-la para uma RFC aberta a mantem tratavel.
> **A distincao esta escrita para que "fechado" nao seja lido como "resolvido".**

### Quando abrir
- Violacao de Principio Imutavel ou Linha Vermelha
- Mudanca executada sem o instrumento da classe
- Aprovacao com acumulo indevido de papeis
- Artefato ativo sem rastreabilidade
- Excecao vencida sem regularizacao
- Credencial exposta
- Portao pulado sem excecao formal

### Rito (FND-04 §10.2)
```
1. PARAR       execucao interrompida — antes de qualquer registro
2. REGISTRAR   DEP-GOV abre o INC
3. CONTER      reverter o efeito, ou isolar se irreversivel
4. ANALISAR    causa: norma / instrumento / compreensao / execucao?
5. CORRIGIR    efeito E causa
6. APRENDER    registro obrigatorio na camada APR
7. FECHAR      DEP-QAR verifica que causa e efeito foram tratados
```

> **Incidente nao e punicao — e informacao.** Deixar de registrar incidente observado e,
> em si, violacao (LV-11). Incidente fechado sem correcao de causa nao esta fechado.

## Verificacoes de aptidao arquitetural

| Metrica | Valor |
|---|---|
| `FIT` emitidos | **23** — **CONTADOS por ferramenta nesta emissao**, nao lidos. *(Esta linha declarava **19**, **quatro** emissoes atras: `FIT-2026-020` a `-023` ja existiam. **Decima segunda ocorrencia** da familia de [MEM-APR-0002](../memory/aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md), e **quarta nesta secao**. Corrigido **na projecao**; nenhuma fonte alterada — `RG-03`, `PJ-03`, `M3`.)* |
| Vereditos `inapto` | 0 |
| **`FIT-2026-023` acrescenta 4** | `S1` *(**independencia e de PAPEL, nao de fornecedor** — sob `ADR-0028`, adiada, este parecer seria `interno`)* · `S2` *(**a custodia do Produto fica FORA do acervo** — subarvore de repositorio de terceiro com **758** caminhos sem commit; `RD-71`)* · `S3` *(**a Carta descreve produto vivo e nao tem mecanismo de sincronia** — se o candidato evoluir e ninguem emendar, vira ficcao)* · `S4` *(**`VC-03` disparado** — cinco Capabilities onde a norma sinaliza em tres; `RD-74`)* — [FIT-2026-023](fitness/FIT-2026-023-admissao-do-nxtrack.md) |
| **Ressalvas — medido na fonte, e o razao NAO fecha** | **`fitness/README`**: **31 linhas** e **28 ressalvas distintas** na tabela de abertas · **18** na de fechadas. **Nos 15 arquivos `FIT`**: **55** linhas de ressalva, das quais **5** sao reclassificacoes embutidas. **Os tres conjuntos nao se reconciliam entre si.** Achado **`RD-36`** |
| **`FIT-2026-019` acrescenta 4** | `R1` *(**o publico primario do Produto candidato tem UM membro** — o teste de existencia passa pela margem minima)* · `R2` *(os links da Carta candidata **apontam para o destino** e nao resolvem onde ela esta — consequencia necessaria de submeter o byte exato)* · `R3` *(a evidencia central do publico e **alegada**, nao observada — o entrevistado nao foi consultado)* · `R4` *(**`Q1` nao e resolvivel por parecer** — a leitura da decisao 7 e materia de portfolio, do **Soberano**)* |
| **`FIT-2026-018` acrescenta 3** | `R1` *(**`RD-49`** — tres Cartas ratificadas declaram em §13.2 um custo que o proprio arquivo desmente; **nao corrigivel por edicao**)* · `R2` *(a prova de `QG-1` depende de **detector novo**, cuja primeira versao tinha 8 falsos positivos)* · `R3` *(**`RD-47` e `RD-48` seguem abertos**) — [FIT-2026-018](fitness/FIT-2026-018-vigencia-do-framework-de-specifications.md)* |
| **`FIT-2026-017` R1 FECHADA** | ✅ O ato de 2026-07-30 promulgou `FND-11` **antes** de `FND-01`, e o acervo mediu **`0` links quebrados**. `R2` e `R3` **permanecem abertas** por determinacao expressa do ato |
| **`FIT-2026-017` acrescenta 3** | `R1` *(**`FND-01` 1.7.0 nao e aplicavel sem `FND-11`** — o candidato escreve link vivo; a **`ALT` esta medida**, mas **e o ato que escolhe**)* · `R2` *(**primeira dispensa de RFC do acervo** — legitima, e **precedente que se reverifica, nao se invoca**)* · `R3` *(**`RD-47`** — o regime de estado que define o `H-P` e **costume, nao regra escrita**)*. **E fecha tres:** `R2` de `FIT-2026-014` e `R2`/`R3` de `FIT-2026-016` |
| **`FIT-2026-016` acrescenta 4** | `R1` *(a duplicacao da norma da `Spec` **sobrevive ao ato**, e `ADR-0021` nao dira que foi superado — `RD-40`)* · `R2` *(**`RD-37`** — 3 Cartas ratificadas seguem afirmando que `DEP-PRD` libera `QG-1`; a missao corrigiu **2 de 4**)* · `R3` *(**`FND-01` sera emendada sem os quatro campos de `AC-08`** se a variante `V1` for escolhida — e a variante `V2`, que fecha `RD-27` quanto a `FND-01`, **existe e esta medida**)* · `R4` *(a **aprovacao do proprio parecer e parcialmente impedida**: `DEP-EXE` e autor de parte do objeto avaliado; resolvido por recorte, com `DEP-GOV` aprovando a parte impedida)* |
| **`FIT-2026-015` acrescenta 3** | `R1` *(as 32 regras `SF-*` sao **determinadas e nao observadas** — nao existe nenhuma `Spec`)* · `R2` *(**21 blocos obrigatorios** sem custo medido; `CE-04` proibiu estimar, e nada foi estimado)* · `R3` *(**`RD-31`** — o portao da `Spec` **sem titular declarado em Carta alguma**)* |
| **Cascata devida, executada** | **As 2 ressalvas de `FIT-2026-014` estavam ausentes do razao desde a missao anterior** e foram acrescentadas, junto com as 3 de `FIT-2026-015` — `CV-04` |
| **O que NAO foi feito, e por que** | **A reconciliacao completa do razao de ressalvas nao foi executada.** Exigiria classificar as **55** linhas uma a uma entre **aberta**, **fechada**, **reclassificada** e **absorvida** — auditoria propria, fora do escopo da Missao 1.13. Esta linha declarava **`19` de `46`** enquanto a propria soma dava **`47`**, e a medicao mostrou que **o defeito e maior que a divergencia de um**. Dono **DEP-QAR** *(fonte)* e **DEP-GOV** *(projecao)*; gatilho **proxima auditoria de ressalvas** |
| Ressalvas **`nao-avaliaveis`** | **0** — R1 de FIT-2026-004 fechou com medicao; R2 voltou a **aberta e aplicavel** |
| **Pendencias escaladas ao SOBERANO** | **11, e ✅ NENHUMA BLOQUEIA — pela primeira vez desde 2026-07-29.** **`RD-33` foi FECHADO em 2026-08-01** pela Missao 1.13.4.6, por rito ministerial, com **`0` atos emitidos** — [PT-2026-016](relatorio-transicao-2026-08-01-fechamento-rd-33.md). *(O enunciado anterior, preservado porque estava correto quando foi escrito: **11, e uma bloqueia.*** A Missao 1.13.4.1 acrescentou **6** que nao existiam: as **tres Cartas `1.2.0`** de `DEP-OPS`, `DEP-GRW` e `DEP-TLS` *(achado `RD-49`, medidas e **nao aplicadas** — emendar Carta ratificada exige ato novo)* e as **tres minutas** *(classe de admissao de existencia em `G3`; independencia de fornecedor; superacao de ato por evidencia posterior)*, **todas fora do acervo e nenhuma aplicada** — [PT-2026-012](relatorio-transicao-2026-07-31-manutencao-instrumentos.md). **✅ `Q1` DEIXOU DE SER PENDENCIA — RESPONDIDA PELO FUNDADOR em 2026-08-01.** A escolha e o **nXtrack**, e o fundamento e que **`PT-2026-009` e `PS-2026-013` sao artefatos DISTINTOS**: a decisao **7** de `PT-2026-009 §1` nomeia o nXtrack **sem ressalva**, e a oracao *"se seguir sendo o primeiro produto comercial"* mora em `PS-2026-013 §7` — a palavra `comercial` tem **`0`** ocorrencias no arquivo de `PT-2026-009`. **Ler os dois como um so foi o que gerou `L1` × `L2`** *(achado `RD-64`)*. A ressalva **nao foi descartada**: virou **`Q2` de [PS-2026-016](pacote-soberano-2026-08-01-nxtrack.md)**. **✅ `Q2` TAMBEM DEIXOU DE SER PENDENCIA — RESPONDIDA por despacho de 2026-08-01 e GRAVADA COMO ARTEFATO em 2026-08-01**, no **nono ato** ([MSG-2026-0009 §5](../memory/operacional/MSG-2026-0009-ato-soberano-admissao-do-nxtrack.md)): a ressalva **NAO condiciona** o ato, e `CA-6` fecha — **`CA-1` a `CA-6` em 6 de 6**. `S1` foi **consumida no ato e APLICADA** sobre o nXtrack — [PT-2026-015](relatorio-transicao-2026-08-01-aplicacao-nxtrack.md) —, e **`RD-33` continua bloqueando por RESERVA do proprio ato** *(item VII, `LA-3`)*, nao mais por ausencia de Produto: ha **`1` em vigor**. **`Q3` e `Q4` de `PS-2026-016 §8` seguem ABERTAS**, e **nenhuma das duas e condicao de eficacia** · o **ato consolidado** dos **catorze** objetos, em **[PS-2026-013 §6](pacote-soberano-2026-07-30-consolidado.md)** · **`Q2` de [PS-2026-011](pacote-soberano-2026-07-30-rd-27.md)** *(`FND-01` cumulativa ou `ALT`, se `FND-11` for bloqueado)* · **`Q1` de PS-2026-011** *(`ADR-0024` `Tipo 2` ou `Tipo 1` — **nao altera hash**)*. **Caiu de 7 para 4:** a variante de `FND-01`, a extensao a `RD-37` e o tipo de `ADR-0022` foram **resolvidos pela Missao 1.13.2**, e `superado_por` em `ADR-0021` foi **decidido: nao gravar**)* |
| **Propostas de consolidacao EV-08** | **1 aberta · 1 encerrada** como `AJUSTAR`, com **zero** artefatos consolidados |
| **Revisoes estruturais executadas** | **1** — a primeira, em 7 ciclos |

> **Uma ressalva fechou com evidencia neste ciclo, e ela estava aberta desde a segunda missao.**
> **R4 de FIT-2026-002** exigia **duas descidas consecutivas itemizadas** do custo de contexto;
> a 9a medicao desceu a **12,0%** e a 10a desceu de novo, as duas medidas por ferramenta
> ([FIT-2026-012 §F5.1](fitness/FIT-2026-012-fechamento-normativo-final.md)).
>
> **E a fila de bloqueios de autoridade sem instrumento zerou.** **RD-14** e **RD-15** — os dois
> achados de severidade **Alta** que a Missao 1.11 abriu **sem pacote** — receberam **rito C3
> completo em pacotes separados**: [PS-2026-007](pacote-soberano-2026-07-29-rd-14.md) e
> [PS-2026-008](pacote-soberano-2026-07-29-rd-15.md). **Pela primeira vez existe um cenario
> alcancavel que produz `GO-TO-SPECS`** ([PT-2026-003 §8.1](relatorio-transicao-2026-07-29-fechamento-normativo.md)).
>
> **Tres achados novos:** **RD-17** *(a baseline nao reproduzia pelo comando que ela publica —
> **corrigido na projecao**, sem editar `BL-2026-07-29-04`)*, **RD-18** *(FND-04 §6 × §2)* e
> **RD-19** *(dois pacotes concorrendo pelas mesmas versoes de FND-09 e FND-10)*.

Detalhe, serie de vereditos e estado de ratificacao em [`fitness/README.md`](fitness/README.md)
— **fonte** desta projecao (PJ-02). Mudanca C2 ou C3 **nao encerra** sem `FIT` emitido
(CV-07, QG-6).

## Baseline vigente do acervo

| Campo | Valor |
|---|---|
| Identificador | **BL-2026-08-02-01** |
| Artefatos · linhas | **223** · **66.100** |
| Baseline anterior | `BL-2026-08-01-03` — **superada, nao editada** (BL-02) |
| **⚠️ Esta secao estava DUAS baselines atras OUTRA VEZ — Missao 1.13.5** | Declarava `BL-2026-08-01-02` · **217** · **63.816** enquanto a fonte ja registrava `BL-2026-08-01-03` · **218** · **64.383**. **Decima segunda ocorrencia** da familia de [MEM-APR-0002](../memory/aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md) e a **quarta nesta mesma secao**, apos `RD-52` ter registrado a terceira e declarado que *"a causa nao e desatencao"*. **Corrigido na projecao**; `0` fontes alteradas (`RG-03`, `PJ-03`, `M3`). **A reincidencia pela quarta vez no mesmo lugar e o sinal, nao o valor** |
| Onde vive | [Catalogo mestre §10](artifact-registry.md) — **fonte**; esta linha e projecao |
| **Instrumento de reproducao** | **Corrigido na Missao 1.13.4.1** — lista fechada positiva, portao de raiz e portao de split. **`BL-2026-07-30-01` voltou a reproduzir nos 64 digitos**: o defeito era do **comando**, nunca da baseline. Achado **`RD-53`**, ✅ **FECHADO** |
| **✅ Estado do instrumento em 2026-08-01, apos a APLICACAO** | **VOLTOU A MEDIR, e por DECLARACAO — nao por afrouxamento.** A recusa era real: **portao de raiz, `CLAUDE.md` nao declarado, saida `2`** — exercida **no acervo E na copia datada**, com a mesma saida nas duas, que e o que provou a fidelidade da copia. O passo **6** de `PS-2026-016 §6.2` acrescentou **`products` a `ACERVO`** *(`OA-1`)* e **`CLAUDE.md` a `NAO_ACERVO`** *(decisao do dono de `RD-81`, o **SOBERANO**, no despacho de abertura da 1.13.4.5 — precedente `.obsidian`)*. **`0` regras removidas:** a lista continua fechada e positiva, o portao de raiz continua parando com erro e o de split continua exigindo uma linha `total`. **`RD-81` ✅ FECHADO**; **`RD-80` segue ABERTO** — o gatilho *"proxima emissao de baseline"* **disparou** e o achado **nao** foi corrigido, porque as tres saidas sao decisoes de **DEP-GOV**, que nao decidiu |

> **`RD-52` — esta secao estava DUAS baselines atras, e o contador de `FIT` uma emissao atras.**
> Ate 2026-07-30 declarava `BL-2026-07-29-08` · **164** · **46.353**, quando a fonte ja registrava
> `BL-2026-07-30-01` · **185** · **54.190**; e contava **16** `FIT` emitidos quando existiam
> **17** arquivos. **Decima primeira ocorrencia** da familia de
> [MEM-APR-0002](../memory/aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md), e a
> **terceira nesta mesma secao** — o que a torna **sinal, nao acidente**. Corrigido **na
> projecao**; nenhuma fonte alterada (`RG-03`, `PJ-03`, `M3`). **A reincidencia no mesmo lugar
> apos duas correcoes registradas indica que a causa nao e desatencao, e sim que `CV-04` nao tem
> gatilho automatico aqui:** a secao so e tocada quando alguem lembra dela.

> **Correcao do defeito RD-04.** Ate 2026-07-29 esta secao declarava `BL-2026-07-28-05`,
> **117** artefatos e **30.947** linhas — **uma baseline atras da fonte** desde o encerramento
> da Missao 1.9 —, e **14** ressalvas abertas onde
> [`fitness/README`](fitness/README.md) contava **15**. Indice desatualizado apos mudanca
> aprovada e **mudanca incompleta**, nao norma nova (IX-02, CV-04). **Corrigido na projecao;
> nenhuma fonte foi alterada** (RG-03, PJ-03, M3). **Setima ocorrencia** da familia de
> [MEM-APR-0002](../memory/aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md).

> **Este indice estava UMA BASELINE ATRAS outra vez.** Ate 2026-07-29 declarava
> `BL-2026-07-29-06` · **157** · **43.498**, quando a fonte ja registrava
> `BL-2026-07-29-07` · **159** · **44.539**, e contava **13** `FIT` emitidos. **Decima
> ocorrencia** da familia, e **item 10 do achado `RD-28`** — corrigido **na projecao**, nenhuma
> fonte alterada (RG-03, PJ-03, M3). **A causa e a mesma de sempre** (CV-04), e a reincidencia
> **nesta mesma secao** e o que a torna sinal: registrada em
> [PT-2026-006 §7.1](relatorio-transicao-2026-07-29-fechamento-operacional.md).

## Estado do portao `GO-TO-SPECS`

| Campo | Valor |
|---|---|
| **Estado** | **LIBERADO** — **8 de 8** condicoes de §X do sexto ato soberano. **E exercido em parte:** o Framework existe; **a primeira Spec nao e criavel** |
| Onde vive a apuracao | [PT-2026-006 §8](relatorio-transicao-2026-07-29-fechamento-operacional.md) — **fonte**; esta secao e projecao (PJ-02) |
| Verificacao independente | [FIT-2026-014](fitness/FIT-2026-014-regime-ministerial-e-cobertura-de-contexto.md), veredito `apto-com-ressalva` |
| **Pre-correcao obrigatoria antes da 1a Spec** | ✅ **`RD-23` FECHADA** — [`TPL-spec` **1.1.0**](../foundation/templates/TPL-spec.md), **5** defeitos corrigidos onde o achado declarava **2**; rito em [ADR-0021 §5.11](../decisions/ADR-0021-framework-de-specifications.md), diff literal em §5.12 |
| **Framework de Specifications** | ✅ **INSTITUIDO** — **`SF-01` a `SF-32`** em [ADR-0021](../decisions/ADR-0021-framework-de-specifications.md), `C2 · Tipo 2`, com **`0`** fontes de `foundation/` emendadas. Verificacao: [FIT-2026-015](fitness/FIT-2026-015-framework-de-specifications.md), `apto-com-ressalva` |
| **✅ `RD-33` — FECHADO em 2026-08-01, e era o unico bloqueio do acervo** | **A `Spec` de produto passou a ser criavel, e o acervo fica SEM PENDENCIA BLOQUEANTE pela primeira vez desde 2026-07-29.** O fechamento e da **Missao 1.13.4.6**, por rito **MINISTERIAL** determinado **antes** de exercido — `PA-01`, `PA-03`, `PA-07` e `PA-13` de [ADR-0020](../decisions/ADR-0020-regime-ministerial-de-promulgacao-e-ativacao.md), `AU-06`, `FND-04 §4 [7]`, `RG-01`/`RG-03`/`RG-04`/`AC-09` de `FND-10` —, com **`0` atos emitidos** e **`0` fontes emendadas**: a autoridade **ja fora exercida** em `S1`, e o que faltava era **registro**. **A reserva do item VII e de `LA-3` era TEMPORAL e DE SEDE, nunca de classe de rito**, e [`MSG-2026-0009 §8`](../memory/operacional/MSG-2026-0009-ato-soberano-admissao-do-nxtrack.md) poe *"`RD-33` destravado"* **antes** de 1.13.5. **Prova por EXERCICIO**, o mesmo metodo que abriu o achado: o `DoR` de `SF-23` foi reexercido e o item **(9)** **PASSA**. **O residuo NAO fechou junto** — a `Spec` de materia **nao-produto**, que so `S2` cria e que segue **deferida**, migrou para **`RD-88`**, ABERTO. [PT-2026-016](relatorio-transicao-2026-08-01-fechamento-rd-33.md) · **O enunciado anterior, preservado:** *"Nenhuma `Spec` e criavel.* Tres fontes vigentes a vinculam a `Produto` — `FND-04 §6` *("Produto existe")*, `FND-03 §3.6` e `FND-10 §4.4` — e **medem-se `0` Specs, `0` Produtos e `products/` ausente**. Desbloqueio: **`S1`** *(ato que crie o primeiro Produto, C2 · Tipo 1)* **ou** **`S2`** *(RFC C3 → ADR C3 → ato, ampliando `Spec` a materia nao-produto)* — **disjuntas, ambas do SOBERANO** ([ADR-0021 §7.3](../decisions/ADR-0021-framework-de-specifications.md)). **✅ `S1` CONSUMIDA E APLICADA em 2026-08-01 — e `RD-33` MESMO ASSIM NAO FECHA.** O rito completo existe — [RFC-0025](../rfcs/RFC-0025-admissao-do-nxtrack-como-primeiro-produto.md) `aprovado` → [ADR-0030](../decisions/ADR-0030-admissao-do-nxtrack-como-primeiro-produto.md) `ativo` · `ratificada` → [FIT-2026-023](fitness/FIT-2026-023-admissao-do-nxtrack.md) → [PS-2026-016](pacote-soberano-2026-08-01-nxtrack.md) → **nono ato** ([MSG-2026-0009](../memory/operacional/MSG-2026-0009-ato-soberano-admissao-do-nxtrack.md), item **III**) —, e a **Missao 1.13.4.5 executou**: [`PRO-nxtrack`](../products/nxtrack/carta.md) existe, `products/` existe e ha **`1` Produto em vigor**. **A condicao de fato CAIU; o que sustenta o bloqueio agora e a RESERVA do proprio ato** — item **VII** e `LA-3`: *"nao fecha `RD-33`, que so fecha apos a vigencia, por missao propria"*. **A vigencia e de hoje; a missao propria ainda nao correu**, e **fecha-lo na missao ministerial seria decidir o que o ato reservou"* — **preservado porque estava correto quando foi escrito: a missao propria correu DEPOIS, e e a 1.13.4.6** |
| Achados abertos que **nao** bloqueiam | **`RD-37`** *(Media — ✅ **tratada por rito completo** na Missao 1.13.2; so fecha com ato: [PS-2026-012](pacote-soberano-2026-07-30-rd-37.md))* · **`RD-43`** *(Media — `IR-03` nao exclui `superado_por` de `H-N`)* · **`RD-39`**, **`RD-40`** *(Baixa — declarados)* · **`RD-31`** *(Alta — **tratada por rito completo**, e so fecha com ato: [PS-2026-010](pacote-soberano-2026-07-29-rd-31.md))* · **`RD-27`** *(Media — ✅ **tratada por rito completo**; so fecha com ato: [PS-2026-011](pacote-soberano-2026-07-30-rd-27.md))* · **`RD-45`** e **`RD-46`** *(✅ **fechados no candidato**)* · **`RD-47`** e **`RD-48`** *(Baixa/Media — **novos, declarados com dono e gatilho**)* · **`RD-34`** *(Baixa)* · `RD-10` · `RD-11` · `RD-12` · `RD-13` · `RD-18` · `RD-24` · **`RD-30`** *(Baixa)* |

> **O bloqueio deixou de existir sem que nenhuma fonte fosse emendada.** `RD-22` — o unico
> achado que impedia a condicao 6 — **era falso**: os titulares de promulgacao e ativacao
> estavam declarados em `FND-04 §4 [7]` e `FND-07 §5 [10]`, e a varredura mediu o **termo** em
> vez da **funcao** ([MEM-APR-0005](../memory/aprendizado/MEM-APR-0005-medir-a-ausencia-na-fonte-errada.md)).

Templates: [`TPL-excecao`](../foundation/templates/TPL-excecao.md) ·
[`TPL-incidente`](../foundation/templates/TPL-incidente.md) ·
[`TPL-fitness-check`](../foundation/templates/TPL-fitness-check.md)
