---
id: PT-2026-002
titulo: Pacote de fechamento de autoridade da camada de Departamentos e aptidao para o Specification Framework
tipo: relatorio
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-07-29
atualizado_em: 2026-07-29
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0012, ADR-0015, ADR-0016, ADR-0017]
substitui: []
substituido_por: null
canal: REPORTE
emissor: DEP-GOV
destinatario: DEP-EXE
ttl: ate a decisao sobre a liberacao do Specification Framework
resumo: Consolida a Missao 1.11 — aplicacao de DEP-QAR 1.2.0, os tres pacotes soberanos, o teste de consumo por Specs, a divida reconciliada, o mapa final de bloqueios e a decisao.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# PT-2026-002 — Fechamento de autoridade e aptidao para Specs

> ## Decisao desta missao: **`READY-FOR-RATIFICATION`**
>
> **`GO-TO-SPECS` exige *"RD-02 e RD-09 vigentes"*.** Os dois foram **resolvidos pelo rito** —
> RFC, ADR candidato, diff literal e pacote soberano —, e **nenhum dos dois vigora**, porque
> **C3 so existe com ato do Soberano** e o ato de hoje **expressamente nao ratifica os futuros
> pacotes C3**.
>
> **Nao e bloqueio: e o rito funcionando.** O que faltava na Missao 1.10 era o **instrumento**;
> o que falta agora e **so a assinatura**. Tres pacotes integros, com minuta preenchida.
>
> **E ha mais.** O **teste de consumo por Specs** — executado sem criar Spec alguma — encontrou
> **dois bloqueios que nenhum dos dois pacotes fecha**: **RD-14** e **RD-15**. Estao em §5 e no
> mapa de §8. **Ratificar RD-02 e RD-09 nao produz `GO-TO-SPECS` sozinho**, e isso esta escrito
> antes de o Soberano decidir, e nao depois.

## Escopo
| Item | Definicao |
|---|---|
| Inclui | Estado de **`DEP-QAR` 1.2.0**, aplicada · os **tres** pacotes soberanos *(por referencia)* · o **teste de consumo por Specs** · **RD-08** · a divida reconciliada · o **mapa final de bloqueios** · a decisao |
| **Nao** inclui | O **merito** dos pacotes — [PS-2026-004](pacote-soberano-2026-07-29-rd-02.md), [PS-2026-005](pacote-soberano-2026-07-29-rd-09.md), [PS-2026-006](pacote-soberano-2026-07-29-kms-eng.md), **nao reproduzidos** · o registro do ato — [MSG-2026-0005](../memory/operacional/MSG-2026-0005-ato-soberano-aplicacao-dep-qar.md) · a aptidao — [FIT-2026-011](fitness/FIT-2026-011-fechamento-de-autoridade.md) · **nenhuma Spec, agente, skill, comando, workflow, produto, codigo, banco, infraestrutura, ontologia ou migracao — nenhum foi criado** |
| Metodo | Toda contagem foi **executada por ferramenta** nesta missao. **Nenhum numero herdado sem reconferencia, e nenhum estimado** (CE-04, LV-12) |

---

## 1. `DEP-QAR` 1.2.0 — **aplicada**

| Campo | Estado |
|---|---|
| Ato consumido | **Ato soberano de 2026-07-29**, item 1 — [MSG-2026-0005 §1.1](../memory/operacional/MSG-2026-0005-ato-soberano-aplicacao-dep-qar.md) |
| Verificacao previa | **11 verificacoes** — `W1` a `W11` de MSG-2026-0005 §3. **Todas satisfeitas** |
| Estado hoje | **`ativo` · `ratificada` · 1.2.0 · 388 linhas** |
| `H-A` · `H-N` · `H-P` | `41f55e73…b5f2b` · `658de6c3…0725` · **`9b180b71…ad29`** |
| `IR-09` | **Reproduz `H-A` byte a byte**; o texto reconstruido e **identico** ao candidato ratificado |
| **1.1.0** | **Recuperavel pelas quatro vias** — PV-1 a PV-4, verificadas em MSG-2026-0005 §5 |
| Achado que fecha | **`RC-01`** — §13.2 declarava **386** onde o arquivo tinha **387**; declara **388**, e o arquivo tem **388** |

> **A armadilha de RC-01 nao se repetiu.** O valor correto era **388** e nao 387, porque a
> propria linha de historico da emenda conta. **Medir depois de alterar** (DR-6) foi exercido,
> e a medicao foi **conferida contra o arquivo aplicado**, nao contra o candidato.

## 2. Os tres pacotes — **por referencia, nao reproduzidos**

| Pacote | Objeto | Ato pedido | Estado |
|---|---|---|---|
| [**PS-2026-004**](pacote-soberano-2026-07-29-rd-02.md) | `ADR-0016` + **FND-02 1.3.0** | Aprovacao e ratificacao **C3** | **Integro. Aguarda ato** |
| [**PS-2026-005**](pacote-soberano-2026-07-29-rd-09.md) | `ADR-0017` + **FND-09 1.4.0** e **FND-10 1.3.0** | Aprovacao e ratificacao **C3** | **Integro. Aguarda ato** |
| [**PS-2026-006**](pacote-soberano-2026-07-29-kms-eng.md) | `DEP-KMS` 1.1.0 · `DEP-ENG` 1.1.0 | Aprovacao e ratificacao | **Integro. Aguarda ato** |

**Os tres sao independentes, e nao decidir e resultado valido em cada um.**
**Os tres trazem minuta preenchida** — terceira, quarta e quinta vez que o pacote entrega o
texto do ato com os valores medidos, resposta acumulada a **RD-05** e **RD-07**.

## 3. Integridade — verificada **antes** de qualquer edicao

| # | O que se verificou | Metodo | Resultado |
|---|---|---|---|
| **U1** | Integridade do acervo na abertura | Reproducao integral de `BL-2026-07-29-03` | **137 artefatos · 37.766 linhas · `d39998da…86de`** — as tres reproduzem, **digito a digito** |
| **U2** | Copia datada antes das edicoes | Copia de todos os `.md` para fora do acervo | **137 arquivos**, com contagem e impressao digital **reconferidas na copia** (PI-07, AF-35) |
| **U3** | `H-A` e `H-N` das tres Cartas alcancadas | Reimplementacao **independente** de `IR-02`+`IR-03`, **validada primeiro** contra as tres Cartas em vigor | **6 de 6 reproduzem** os valores de PS-2026-003 |
| **U4** | `H-A` e `H-N` das tres fundacionais | idem | **6 de 6** medidos e publicados |
| **U5** | Diff dos candidatos | `diff -u` contra a fonte | **`DEP-QAR` 5 · `DEP-KMS` 10 · `DEP-ENG` 7 alteracoes** — identicas as revisadas, **nenhuma a mais** |
| **U6** | Links | Resolucao de **1.712** links relativos | **0 quebrados** |
| **U7** | Autoverificacao | `autor` × `revisor` nos **86** artefatos que declaram os dois | **0 coincidencias** (FT-02, RM-06b, ADR-0005) |
| **U8** | Credencial | Varredura por padrao de segredo no acervo **e** nos cinco candidatos | **0 ocorrencias** (PI-08, LV-02) |
| **U9** | Frontmatter | `id` e `versao` em **147** artefatos | **0 ausencias** |
| **U10** | Terminadores de linha dos candidatos | Comparacao byte a byte com a fonte | **Preservados em 5 de 5** — §7, achado de metodo |

**Integridade: INTACTA.**

## 4. Teste de consumo por Specs — **simulado, sem criar Spec**

> **Nenhuma Spec foi criada, e nenhum diretorio `projects/` foi aberto.** O que segue e a
> simulacao do ciclo **proposta → autoria → revisao → aprovacao → ratificacao/vigencia** contra
> as fontes vigentes, com a pergunta unica: **a matriz responde sem interpretacao informal?**

### 4.1 O ciclo de uma `SPC`, ato a ato

Fonte: **FND-09 §8.2** *(linha `SPC`)* · **FND-01 §6.2** *(portoes)* · **FND-04 §2** *(classes)*.

| Ato | Titular | **Um titular?** | Impedimento explicito? | Autoverificacao? | Responde sem interpretacao? |
|---|---|---|---|---|---|
| **Proposta** | **DEP-PRD** | ✅ **1** | — | Nao | ✅ |
| **Autoria** | **DEP-PRD** | ✅ **1** | — | Nao | ✅ |
| **Revisao** | **DEP-ENG** + **DEP-QAR** | ✅ **2, por desenho** — revisao dupla e a regra da linha `SPC`, nao acumulo | ✅ `DEP-ENG I-8`, `DEP-QAR I-1` | ✅ **nenhum dos dois e DEP-PRD** | ✅ |
| **Aprovacao (QG-1)** | **DEP-PRD** | ✅ 1 | ⚠️ **declarado como risco (`RP-1`), nao como impedimento** | ❌ **o produtor libera o proprio portao** | ❌ **RD-14** |
| **Ratificacao** | **nenhum** — a celula e `—` | ✅ n/a | — | — | ⚠️ **so para Spec C0/C1** — **RD-15** |
| **Vigencia** | `status: ativo` | ✅ | — | — | ✅ FND-10 §5.2 |

### 4.2 Por classe de mudanca e por tipo

| Materia da Spec | Classe | Tipo | Instrumento (FND-04 §2) | Aprovador **por FND-04** | Aprovador **por FND-09 §8.2** | Coerente? |
|---|---|---|---|---|---|---|
| Corrigir redacao de uma Spec | **C0** | 2 | nenhum | proprietario = **DEP-PRD** | **DEP-PRD** | ✅ |
| Refinar criterio de aceite dentro da mesma Spec | **C1** | 2 | Nota de Decisao | proprietario + **revisor de papel distinto** | **DEP-PRD**, revisores DEP-ENG + DEP-QAR | ✅ |
| Spec que cria componente ou muda fronteira | **C2** | 2 | **RFC → ADR** | **DEP-EXE**, com parecer de DEP-GOV | **DEP-PRD (QG-1)** | ❌ **dois aprovadores** — **RD-15** |
| Spec com dado vivo ou exposicao externa | **C2** | **1** | RFC → ADR | DEP-EXE **+ ratificacao do SOBERANO** | **DEP-PRD**; ratifica **`—`** | ❌ **ratificador divergente** — **RD-15** |
| Spec que alterasse direito de decisao | **C3** | 1 ou 2 | RFC → analise → ADR → **ratificacao** | **SOBERANO** | ratifica **`—`** | ❌ idem — **RD-15** |

> **A regra de precedencia existe e resolve — e ninguem a executou.** FND-09 §8.2 declara sobre
> si propria: *"Conflito entre esta tabela e o documento de origem resolve-se a favor do
> documento de origem, e **o conflito e registrado como erro deste documento**."* **A primeira
> metade da regra basta para decidir** — prevalece FND-04 §2. **A segunda nunca foi cumprida:
> nenhum conflito foi registrado como erro.** Esta e a primeira vez que um e.

### 4.3 Escalonamento — **deterministico?**

| Situacao | Escala para | Nivel | Deterministico? |
|---|---|---|---|
| DEP-ENG devolve a Spec por inviabilidade | **DEP-PRD**, e disputa vai a **DEP-EXE** | E2 | ✅ FND-02 §7, N2 |
| DEP-QAR veta a Spec por criterio de aceite nao verificavel | **DEP-PRD**; veto contestado vai ao **SOBERANO** | E4 | ✅ LV-09; FND-02 §6 |
| DEP-PRD e DEP-ENG divergem sobre *"suficientemente definido"* | **DEP-EXE** arbitra | E2 | ✅ FND-02 §6 e §7 |
| Spec pressupoe ferramenta externa nao adotada | **DEP-TLS**; adocao e **Tipo 1** | E4 | ⚠️ o caminho de PRD ate TLS **e contestado** — **RD-10** |
| Spec toca dado vivo | **SOBERANO** | **E4** | ✅ FND-01 §7.3; `DEP-QAR §8` |
| Spec **C2 ou C3** chega a aprovacao | **indeterminado entre DEP-PRD e DEP-EXE/SOBERANO** | — | ❌ **RD-15** |

### 4.4 Veredito do teste

| # | Exigencia | Resultado |
|---|---|---|
| **S1** | **Um titular por ato** | ⚠️ **5 de 6 atos** tem titular unico e inequivoco. **A aprovacao de Spec C2/C3 tem dois** — RD-15 |
| **S2** | **Impedimentos explicitos** | ⚠️ **DEP-ENG e DEP-QAR declaram impedimento sobre a Spec.** **DEP-PRD nao declara impedimento sobre QG-1** — declara **risco** (`RP-1`). Risco nao e impedimento — RD-14 |
| **S3** | **Ausencia de autoverificacao** | ❌ **QG-1 e liberado por quem produziu a Spec**, contra a regra literal de FND-01 §6.2 — RD-14 |
| **S4** | **Escalonamento deterministico** | ⚠️ **5 de 6** caminhos deterministicos; o de aprovacao C2/C3 nao — RD-15 |
| **S5** | **A matriz responde sem interpretacao informal** | ❌ **Nao para C2/C3.** Responde **apos** aplicar a regra de precedencia de FND-09 §8.2 — que **e** norma, mas cuja segunda metade *(registrar o erro)* nunca foi cumprida |

> **O teste era para ser passado, e nao foi — e esse e o produto.** A camada entrega
> **autoridade, custodia, interface e contexto**; o que ela **nao** entrega e um ciclo de Spec
> executavel sem colisao normativa. **Descobrir isso simulando custa duas linhas de achado.
> Descobrir isso na primeira Spec real custaria a primeira Spec real.**

## 5. Achados novos desta missao — **sete**

| # | Achado | Sev. | Dono | Gatilho | Corrigivel agora? |
|---|---|---|---|---|---|
| **RD-10** | `DEP-TLS §6.3` declara *"sem interacao estrutural direta"* com **DEP-PRD** e **DEP-GRW**, e diz que o pedido de capacidade chega *"por DEP-ENG ou DEP-EXE"*; `DEP-PRD §6.3` e `DEP-GRW §6.3` declaram **consulta direta**, e a fonte declara `C` nos dois casos. **Duas Cartas em vigor descrevem caminhos operacionais incompativeis** | **Media** | DEP-EXE | Proxima emenda a `DEP-TLS` | **Nao** — Carta ratificada (IR-01) |
| **RD-11** | Quatro celulas do candidato FND-02 1.3.0 declaram mais do que a Carta do proprio emissor: `EXE→KMS`, `GOV→EXE`, `QAR→EXE`, `QAR→KMS`. **Residuo de propagacao** (CV-04) | Baixa | DEP-EXE | Proxima emenda a `DEP-EXE`, `DEP-GOV` e `DEP-QAR` | **Nao** — as tres em vigor |
| **RD-12** | **FND-04 §2.1 nao distingue artefato de decisao de parecer.** E a regra que **gerou** o texto que RD-09 corrige; corrigir a projecao sem toca-la deixa o mecanismo vivo | **Media** | DEP-GOV | Proxima emenda a **FND-04** | **Nao** — exige ato; **nao foi pedido** |
| **RD-13** | O **historico de versoes de FND-10 esta fora de ordem** — `1.1.0` figura depois de `1.2.0` | Baixa | DEP-GOV | Proxima emenda a FND-10 | **Nao** — texto dentro de `H-N` de fundacional ratificada |
| **RD-14** | **`QG-1` e liberado por DEP-PRD, que produz a Spec**, contra a regra literal de **FND-01 §6.2** — *"portao nao pode ser liberado por quem produziu o artefato"*. `DEP-PRD §5.2` reconhece o fato e `RP-1` declara o **risco**; **nenhum dos dois nomeia a colisao normativa**, e **nao existe excecao formal registrada** — `governance/exceptions/` tem **0** | **Alta** | **DEP-GOV** | **Antes da primeira Spec**; ou proxima emenda a FND-01 §6.2 / FND-09 §8.2 | **Nao** — colisao entre **duas fundacionais**; exige ato |
| **RD-16** | **Este catalogo mestre estava DUAS MISSOES desatualizado em §4:** o cabecalho declarava *"117 de 117"*, as tabelas somavam **131** linhas de artefato para **137** artefatos em disco, e **seis** artefatos — `ADR-0015`, `FIT-2026-009`, `FIT-2026-010`, `PS-2026-003`, `PT-2026-001` e `MSG-2026-0004` — **nunca haviam sido acrescentados** | Baixa | DEP-GOV | — | ✅ **CORRIGIDO nesta missao, na projecao**; **zero fontes alteradas** (RG-03, PJ-03). **Quarta ocorrencia de o catalogo divergir de si proprio** — IC-8, RE-04, RD-06 |
| **RD-15** | Para Spec **C2** ou **C3**, **FND-09 §8.2** *(linha `SPC`: aprova DEP-PRD, ratifica `—`)* e **FND-04 §2** *(aprova DEP-EXE/SOBERANO, ratifica SOBERANO)* **dao respostas diferentes**. A regra de precedencia de FND-09 §8.2 **resolve** a favor de FND-04, e a segunda metade dela — *registrar o conflito como erro desta tabela* — **nunca foi cumprida**. As fontes tambem **nao distinguem *aprovar o artefato* de *liberar o portao*** | **Alta** | **DEP-GOV** | **Antes da primeira Spec C2** | **Parcialmente** — o **registro do erro** e devido e **e feito aqui**; a **emenda** exige ato |

> **RD-14 e RD-15 sao os unicos dois achados desta missao que impedem `GO-TO-SPECS`**, e
> **nenhum dos dois e fechado por PS-2026-004 ou PS-2026-005**. Estao aqui **antes** da decisao
> do Soberano, e nao depois dela.

### 5.1 **RD-08** — registro do defeito textual historico

**Determinacao da missao: registrar, nao superar.**

| Campo | Conteudo |
|---|---|
| Objeto | [`ADR-0014`](../decisions/ADR-0014-candidato-emenda-fnd-01-7-3-homologa.md) |
| Defeito | O `id` e o titulo contem **"CANDIDATO"**, e o corpo abre com *"⛔ ESTE ADR NAO ESTA EM VIGOR E NAO PRODUZ NENHUM EFEITO"* — enquanto o frontmatter declara `status: ativo` e `ratificacao: ratificada` |
| Natureza | **Defeito textual historico.** O texto era **verdadeiro quando escrito** e a **propria ratificacao o tornou falso** |
| **Fonte do estado** | **O frontmatter** (`status`, `ratificacao` — FND-10 §5.4) **e o ato** ([MSG-2026-0004 §2.2](../memory/operacional/MSG-2026-0004-ato-soberano-cartas-emenda-constitucional-e-regime-do-fitness-check.md)). **Nunca o cabecalho do corpo** |
| Efeito material | **Nenhum medido.** FND-01 **1.4.0 esta promulgada**; a emenda **produziu efeito**; **nenhum artefato** consome o cabecalho de ADR-0014 como fonte de estado |
| Decisao | **MANTIDO CONTIDO.** Superar exigiria **ato novo** — o texto esta **dentro de `H-N`** (IR-01, IR-05) — e o ato de hoje **veda expressamente alterar artefatos historicos** |
| Criterio de superacao | **Somente com risco material demonstrado.** Nenhum foi demonstrado; **nenhum foi presumido** |
| **Licao aplicada nesta missao** | **`ADR-0016` e `ADR-0017` nao repetem o defeito.** O `id` **nao** contem *"candidato"*, o titulo **nao** afirma estado, e o bloco de abertura **remete ao frontmatter** em vez de afirmar vigencia — texto que **permanece verdadeiro nos dois estados** |

## 6. Divida e ressalvas — reconciliacao

> **Regra aplicada:** *"tratado"* nao significa *"resolvido"*. Cada item recebe **um** dos cinco
> estados, e **nenhum e fechado sem evidencia**.

| Item | Estado | Evidencia ou motivo |
|---|---|---|
| **RC-01** *(`DEP-QAR §13.2` declarava 386)* | **RESOLVIDA** | `DEP-QAR` 1.2.0 **aplicada**; §13.2 declara **388** e `wc -l` conta **388**. MSG-2026-0005 §4, Z4 |
| **RD-05** *(minuta com marcadores)* · **RD-07** *(hash de 40 caracteres no ato)* | **RESOLVIDOS** | O ato de hoje trouxe **o unico hash com 64 caracteres**, e ele confere. **Primeiro ato do acervo sem nenhum identificador recusado** |
| **RD-02** | **TRATADA PELO RITO — nao vigente** | RFC-0012 → ADR-0016 → PS-2026-004. **Fecha com o ato, nao com o instrumento** |
| **RD-09** | **TRATADA PELO RITO — nao vigente** | RFC-0013 → ADR-0017 → PS-2026-005 |
| **RC-05 · RC-07** | **MANTIDOS** | As duas Cartas seguem em **1.0.0**. A reemissao **nao os fecha**; o ato fecha |
| **RD-08** | **MANTIDO — contido** | §5.1. **Registrado como defeito textual historico**, com fonte do estado declarada |
| **RD-01** *(citacao em `DEP-PRD §8.2`)* | **MANTIDO — explicado** | RFC-0012 §4, P1: leitura **relacional** de tabela **direcional**. **A causa passa a ser conhecida; o texto nao muda sem ato** |
| **RD-03** *(`DEP-KMS §6.3`)* | **MANTIDO — confirmado por ferramenta** | A linha KMS tem **6 `E`, 2 `C`, 1 `—`**; a Carta diz *"entrega a todos"* **e** *"entrega a sete e consulta dois"* — **7+2=9 para 8 outros departamentos**. A **fonte esta certa** |
| **R1 de FIT-2026-010** *(RD-09)* | **TRATADA — fecha com o ato** | PS-2026-005 |
| **R2 de FIT-2026-010** *(RD-07, duas emendas)* | **TRATADA — fecha com o ato** | PS-2026-006, com **prova criptografica de identidade** |
| **R3 de FIT-2026-010** *(RD-08)* | **MANTIDA — contida com criterio de superacao declarado** | §5.1 |
| **R4 de FIT-2026-010** *(RD-02)* | **TRATADA — fecha com o ato** | PS-2026-004 |
| **R1 de FIT-2026-005 · R1 de FIT-2026-006 · R1 e R3 de FIT-2026-007 · R3 de FIT-2026-008** *(autor unico, segregacao no limite)* | **MANTIDAS — agravadas** | **Quinta missao seguida** operando no limite. **Nenhum agente criado**, por determinacao |
| **R1 e R2 de FIT-2026-008** *(regras `HZ` sem membros · crescimento)* | **MANTIDAS** | `HZ-02` continua sem disparar — **quarto ciclo** |
| **R4 de FIT-2026-002** *(reducao de contexto)* | **MANTIDA** | Exige **duas** descidas consecutivas itemizadas; **ha uma**, e esta missao **sobe** — FIT-2026-011 §F5 |
| **IC-2** | **RESOLVIDO** *(ciclo anterior)* | Fechado na fonte por FND-01 1.4.0. **Nao reaberto** |
| **RD-04 · RD-06** | **RESOLVIDOS** *(ciclo anterior)* | **Nao reabertos** |
| **RD-10 · RD-11 · RD-12 · RD-13 · RD-14 · RD-15** | **NOVOS — abertos** | §5, com dono e gatilho |
| **RD-16** *(catalogo duas missoes desatualizado)* | **NOVO — RESOLVIDO** | §5; corrigido **na projecao**, zero fontes alteradas |

**Ressalvas renomeadas para parecerem fechadas: ZERO. Ressalvas fechadas por reformulacao:
ZERO.** **Tres itens resolvidos com evidencia** — RC-01, RD-05 e RD-07 —, **dois tratados pelo
rito e nao vigentes**, **um contido com criterio de superacao**, e o restante **mantido**.

## 7. Achado de metodo — **terminadores de linha**

**`FND-10` usa `CRLF`; `FND-02`, `FND-09` e as nove Cartas usam `LF`.** A primeira montagem do
candidato `FND-10 1.3.0` **converteu os terminadores** e foi **descartada e refeita em modo
binario**: o hash teria mudado **o arquivo inteiro** sem que **uma unica linha de norma** mudasse,
e a conferencia de `H-A` teria falhado sem que ninguem soubesse por que.

| Verificacao | Resultado |
|---|---|
| Candidatos com terminadores **preservados** | **5 de 5**, conferidos byte a byte |
| Registrado para | **Toda emenda futura a FND-10** e a qualquer artefato `CRLF` |

> **Nao vira achado numerado porque nao ha defeito no acervo** — os arquivos estao integros.
> **Vira licao de metodo**, gravada em §10.

## 8. Mapa final de bloqueios — o que impede `GO-TO-SPECS`

| # | Bloqueio | O que o remove | Depende do Soberano? |
|---|---|---|---|
| **B1** | **RD-02 nao vigora** — a semantica da matriz de FND-02 §4 e a ambiguidade do veto | **Um ato** sobre [PS-2026-004](pacote-soberano-2026-07-29-rd-02.md). Nada mais | **SIM** |
| **B2** | **RD-09 nao vigora** — duas fundacionais divergem de `FT-10` | **Um ato** sobre [PS-2026-005](pacote-soberano-2026-07-29-rd-09.md) | **SIM** |
| **B3** | **`RC-05` e `RC-07` abertos** em Cartas em vigor | **Um ato** sobre [PS-2026-006](pacote-soberano-2026-07-29-kms-eng.md) | **SIM** |
| **B4** | **RD-14 — `QG-1` liberado por quem produz a Spec** | **Emenda a FND-01 §6.2 ou a FND-09 §8.2**, ou **excecao formal registrada** (FND-01 §8.3). **Nao ha instrumento pronto**: exige RFC → ADR → ato | **SIM**, e **nao ha pacote** |
| **B5** | **RD-15 — aprovador e ratificador divergentes para Spec C2/C3** | **Emenda a FND-09 §8.2**, linha `SPC`. O **registro do erro** ja foi feito *(§4.2)*; a **correcao** exige rito | **SIM**, e **nao ha pacote** |
| **B6** | **Zero agentes existem** — `LC-2`, `IC-3` | Criacao de executores, **fora do escopo desta camada e desta missao** | Nao — mas nenhuma Spec pode ser **atribuida** |
| **B7** | **Desempenho nao exercido** — `LC-4` | Um ciclo de produto real. **Vigencia nao e competencia** | Nao |

> ### O que mudou no mapa desde PT-2026-001
> **PT-2026-001 §11.1 projetou que nenhum ato possivel produziria `GO-TO-SPECS`, e a projecao se
> confirmou nos tres cenarios.** Esta missao **mantem a projecao e muda a causa**: la o
> impedimento era **RD-02, sem instrumento**; aqui **RD-02 e RD-09 tem instrumento pronto**, e
> os impedimentos que sobram — **B4 e B5** — sao **novos, foram encontrados por simulacao, e nao
> tem pacote**.
>
> **Tres atos removem B1, B2 e B3. Nenhum ato existente remove B4 e B5.**

## 9. Decisao

| Campo | Conteudo |
|---|---|
| **Decisao** | **`READY-FOR-RATIFICATION`** |
| **Fundamento** | **Tres pacotes integros aguardam ato.** Toda a materia que dependia desta missao foi executada: `DEP-QAR` **aplicada e verificada**, RD-02 e RD-09 **resolvidos pelo rito aplicavel**, `DEP-KMS` e `DEP-ENG` **reemitidos com prova de identidade** |
| **Por que nao `GO-TO-SPECS`** | O criterio exige **RD-02 e RD-09 vigentes**. Os dois sao **candidatos**, e **C3 so existe com ato** (FND-01 §9). **E mesmo com os tres atos, B4 e B5 permaneceriam** |
| **Por que nao `ADJUST`** | **Nenhuma correcao delimitada resta dentro do mandato.** Tudo o que nao dependia de ato foi executado, e os seis achados novos **exigem ato ou emenda a Carta em vigor** |
| **Por que nao `BLOCKED`** | **O ato chegou, foi verificado e foi aplicado.** A pre-condicao 1 esta **satisfeita e provada** — `IR-09` reproduz `H-A` byte a byte. Nenhum objeto foi recusado |
| **Por que nao `STOP`** | **Zero falhas estruturais.** 1.637 links com **0** quebrados; **0** autoverificacoes em 84 artefatos; **0** credenciais; integridade **intacta**; **0** artefatos M1 editados |
| **O que desbloqueia** | **Tres atos** — PS-2026-004, PS-2026-005, PS-2026-006 —, e depois **dois instrumentos que ainda nao existem**, para **B4** e **B5** |

### 9.1 O que a decisao seria, se os atos chegassem

| Cenario | Decisao projetada | Condicao nomeada |
|---|---|---|
| Ato sobre **PS-2026-006** apenas | **`READY-FOR-RATIFICATION`** | **B1, B2, B4, B5** |
| Ato sobre **PS-2026-004 + PS-2026-005** | **`GO-CONDITIONAL`** | **B4** e **B5** — RD-14 e RD-15, **os dois de severidade Alta** |
| Ato sobre **os tres** | **`GO-CONDITIONAL`** | **B4** e **B5**, identicamente |
| Ato sobre os tres **+ instrumento para B4 e B5** | **`GO-TO-SPECS`** | — |

> **A projecao e a mesma nos tres primeiros cenarios, e isso e informacao — de novo.** Na Missao
> 1.10 o impedimento residual estava numa celula que ninguem tinha lido contra a leitura
> obrigatoria da propria tabela. **Nesta, esta num portao que a Constituicao proibe liberar e que
> a matriz de entidades manda liberar.** **Nenhum dos dois foi antecipado ao ato de hoje**:
> RD-14 e RD-15 nasceram **nesta missao**, nao passaram por RFC, e leva-los ao ato seria
> exatamente a antecipacao que PT-2026-001 §11.1 recusou.

## 10. Aprendizado gerado

| Registro APR | Licao |
|---|---|
| A gravar por DEP-KMS *(QG-5)* | **Ratificado e aplicado sao atos distintos, e a distincao tem valor operacional.** `DEP-QAR` 1.2.0 ficou **ratificada e nao aplicada** por um ciclo inteiro sem que nada quebrasse. Acao: **todo registro de ato declara os dois estados separadamente**. Dono: DEP-GOV |
| A gravar por DEP-KMS *(QG-5)* | **Simular o consumo encontra o que a conformidade nao encontra.** **117 verificacoes de contrato** passaram nas nove Cartas e **nao** encontraram RD-14; **uma simulacao de seis atos** encontrou. Acao: **toda camada declara-se apta so apos simular o ciclo de quem vai consumi-la**. Dono: DEP-QAR |
| A gravar por DEP-KMS *(QG-5)* | **Terminador de linha e parte do artefato.** Converter `CRLF` em `LF` muda o hash **do arquivo inteiro** sem mudar **uma linha de norma**, e a conferencia falha sem causa aparente. Acao: **todo candidato e montado em modo binario e tem os terminadores conferidos contra a fonte**. Dono: DEP-KMS |
| A gravar por DEP-KMS *(QG-5)* | **Texto que afirma o proprio estado envelhece com a ratificacao.** E a causa de RD-08. Acao: **bloco de estado de candidato remete ao frontmatter, nunca afirma vigencia** — aplicado em ADR-0016 e ADR-0017. Dono: DEP-GOV |

## 11. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Ato consumido | [MSG-2026-0005](../memory/operacional/MSG-2026-0005-ato-soberano-aplicacao-dep-qar.md) — **fonte canonica unica** |
| Pacotes submetidos | [PS-2026-004](pacote-soberano-2026-07-29-rd-02.md) · [PS-2026-005](pacote-soberano-2026-07-29-rd-09.md) · [PS-2026-006](pacote-soberano-2026-07-29-kms-eng.md) |
| Instrumentos produzidos | [RFC-0012](../rfcs/RFC-0012-semantica-da-matriz-de-interacao.md) → [ADR-0016](../decisions/ADR-0016-semantica-da-matriz-de-interacao.md) · [RFC-0013](../rfcs/RFC-0013-harmonizacao-do-regime-do-parecer.md) → [ADR-0017](../decisions/ADR-0017-harmonizacao-do-regime-do-parecer.md) |
| Pacote anterior, **nao editado** | [PT-2026-001](relatorio-transicao-2026-07-29-departamentos.md) |
| Requisitos que a camada impoe as Specs | **PT-2026-001 §7**, `RS-1` a `RS-10` — **fonte unica, nao reproduzida**; §4 desta missao os **testa** |
| Contrato das Cartas | [ADR-0011](../decisions/ADR-0011-contrato-de-carta-de-departamento.md) |
| Integridade do ato | [ADR-0012](../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md) |
| Verificacao de aptidao | [FIT-2026-011](fitness/FIT-2026-011-fechamento-de-autoridade.md) |
| Baseline anterior | **`BL-2026-07-29-03`** — preservada, **nao editada** (BL-02) |
| Baseline emitida por esta missao | **`BL-2026-07-29-04`** — [catalogo mestre §10](artifact-registry.md) |
| Copia datada anterior as edicoes | **137** arquivos, fora do acervo (PI-07, AF-35) |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-GOV | Pacote de fechamento da **Missao 1.11**. Decisao **`READY-FOR-RATIFICATION`**: **`DEP-QAR` 1.2.0 aplicada e verificada** por onze vias, com `IR-09` reproduzindo `H-A` **byte a byte**, e **tres pacotes soberanos integros** — RD-02 e RD-09 **resolvidos pelo rito** *(RFC → ADR → pacote)* e `DEP-KMS`/`DEP-ENG` **reemitidos com prova criptografica de identidade**. **Teste de consumo por Specs executado sem criar Spec**, simulando seis atos e cinco classes: **5 de 6 atos com titular unico**, e **dois bloqueios novos de severidade Alta** — **RD-14** *(QG-1 liberado por quem produz)* e **RD-15** *(aprovador e ratificador divergentes para Spec C2/C3)* —, **nenhum deles fechado pelos pacotes**. **Sete achados novos**, `RD-10` a `RD-16` — **um deles ja corrigido na projecao**; **RD-08 registrado como defeito textual historico e mantido contido**, com a licao aplicada em ADR-0016 e ADR-0017. **1.712 links, 0 quebrados · 86 artefatos com autor e revisor, 0 autoverificacoes · 0 credenciais · 0 artefatos M1 editados.** |
