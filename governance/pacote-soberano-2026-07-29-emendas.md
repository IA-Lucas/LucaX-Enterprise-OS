---
id: PS-2026-003
titulo: Pacote de decisao soberana — tres emendas locais a Cartas ja ratificadas
tipo: relatorio
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-07-29
atualizado_em: 2026-07-29
revisao_prevista: null
decisoes_relacionadas: [ADR-0011, ADR-0012]
substitui: []
substituido_por: null
canal: REPORTE
emissor: DEP-GOV
destinatario: SOBERANO
ttl: ate decisao do Soberano
resumo: Reune, para decisao do Soberano, as tres emendas candidatas que fecham RC-05, RC-07 e RC-01 em Cartas ja ratificadas, com diff literal, hashes, impacto e revisao independente por objeto.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# PS-2026-003 — Pacote de decisao soberana sobre tres emendas locais

> ## Este pacote **informa**. Nao decide, nao aprova, nao ativa e nao edita nenhuma Carta.
>
> As tres Cartas alcancadas — `DEP-KMS`, `DEP-ENG` e `DEP-QAR` — estao **em vigor**
> (`ativo` · `ratificada`). Emendar Carta ratificada altera `H-N` e **exige ato novo** do
> Soberano (**IR-01**, **IR-05** de [ADR-0012](../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md);
> **DC-09** de [ADR-0011](../decisions/ADR-0011-contrato-de-carta-de-departamento.md)).
>
> **Nenhum arquivo de Carta foi alterado por esta missao.** Os candidatos existem como **diff
> literal + hash** registrados aqui, fora do acervo — o mesmo desenho que
> [FIT-2026-007 §F2.a](fitness/FIT-2026-007-revisao-estrutural-i.md) fixou ao recusar escrever
> texto candidato no acervo, e que [MSG-2026-0003 §2.1](../memory/operacional/MSG-2026-0003-ato-soberano-emenda-qar-e-criterio-de-consolidacao.md)
> aplicou na emenda `DEP-QAR` 1.1.0. **Duas Cartas do mesmo departamento nunca coexistem** (MM-01).
>
> **Caminho exato deste pacote:** `governance/pacote-soberano-2026-07-29-emendas.md` *(RE-01)*.

## Proposito
Levar ao Soberano, em um unico lugar, as **tres** emendas minimas que fecham a ressalva **R4**
de [FIT-2026-008](fitness/FIT-2026-008-rollout-das-cartas.md) — os achados **RC-05**, **RC-07**
e **RC-01**, retidos ha um ciclo em Cartas que so ele pode reabrir.

## Escopo
| Item | Definicao |
|---|---|
| Inclui | **3** emendas candidatas **MENORES** a Cartas `ativo` · `ratificada`, com diff literal, `H-A`, `H-N`, impacto e revisao independente |
| **Nao** inclui | As **cinco** Cartas em `em-revisao` — objeto separado de [PS-2026-002](pacote-soberano-2026-07-28-cartas.md) · a emenda **C3** *(ADR-0014)* · a questao **Q2** · qualquer achado desta missao que **nao** seja corrigivel por emenda de Carta *(RD-01 a RD-05 — §5)* |
| Natureza | **Reporte**, tipo documental de [FND-10 §4.6](../foundation/10-artifact-framework.md), entidade `MSG`. **Nenhum** tipo, entidade, camada ou template novo |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| **Autor das emendas** | **DEP-EXE** | FND-09 §8.2, linha `DEP` — proprietario das nove Cartas |
| **Revisor independente** | **DEP-GOV** *(`DEP-KMS`, `DEP-ENG`)* · **DEP-QAR** *(`DEP-QAR` — ver residuo abaixo)* | RM-06b — quem e objeto nao revisa |
| **Monta este pacote** | **DEP-GOV** | Guardiao normativo; nao produziu as emendas |
| **Revisa este pacote** | **DEP-QAR** | AC-03 |
| **DECIDE** | **SOBERANO** | **Indelegavel.** Nao ocorreu |

> **Residuo declarado (PI-10).** A emenda de `DEP-QAR` **e sobre a Carta de DEP-QAR**, e
> **`DEP-QAR I-5`** o impede de *aprovar, revisar ou emendar* a propria Carta. A revisao
> independente dessa terceira emenda foi executada por **DEP-GOV**, e o que DEP-QAR fez foi
> **medicao reproduzivel de hash e de contagem de linhas**, sem juizo de merito — a mesma
> distincao que [MSG-2026-0003](../memory/operacional/MSG-2026-0003-ato-soberano-emenda-qar-e-criterio-de-consolidacao.md)
> aplicou e registrou como achado **RC-02**. **Terceira ocorrencia do mesmo residuo**; permanece
> declarado, nao resolvido.

---

## 1. O que se pede, em uma tabela

| # | Objeto | Ato pedido | Se **nao** houver ato |
|---|---|---|---|
| **1** | `DEP-KMS` **1.1.0** | **Aprovacao e ratificacao** | `DEP-KMS` **1.0.0** permanece em vigor. **RC-05 permanece aberto**; a Carta segue sendo a unica das nove sem nenhuma linha sobre incidente |
| **2** | `DEP-ENG` **1.1.0** | **Aprovacao e ratificacao** | `DEP-ENG` **1.0.0** permanece em vigor. **RC-07 permanece aberto**; **efeito nulo** — a autoridade nao existe por AU-09 —, e a declaracao que DC-03 pede continua faltando |
| **3** | `DEP-QAR` **1.2.0** | **Aprovacao e ratificacao** | `DEP-QAR` **1.1.0** permanece em vigor. **RC-01 permanece aberto**; a Carta segue declarando **386** onde o arquivo tem **387** |

> **Os tres sao independentes**, e **nao decidir e resultado valido**. Nenhum dos tres bloqueia
> a ativacao das cinco Cartas de PS-2026-002, e nenhum e alcancado por ela.

### 1.1 Classificacao de cada achado — normativo, operacional ou projecao

| Achado | Classificacao | Fundamento da classificacao |
|---|---|---|
| **RC-05** *(`DEP-KMS`)* | **NORMATIVO** | O que falta e **declaracao exigida por DC-03 e DC-05**: impedimento com substituto nomeado, e fronteira que nomeie o dono real. Ausencia de bloco exigido e nao conformidade de contrato, nao lacuna de operacao |
| **RC-07** *(`DEP-ENG`)* | **NORMATIVO** | Identico em natureza: **DC-03** exige que a Carta nomeie os proprios impedimentos. **Efeito pratico nulo** — AU-09 ja nega a autoridade —, mas a **classificacao segue a norma violada**, nao o tamanho do efeito |
| **RC-01** *(`DEP-QAR`)* | **PROJECAO** | §13.2 e **medicao autorreferente** do proprio arquivo (DC-10, DR-6). Nao concede autoridade, nao cria impedimento e nao altera fronteira. E numero desatualizado **dentro** de `H-N` — por isso exige ato, embora seja projecao |

> **A classificacao muda o que se pede, nao se se pede.** As tres exigem ato porque **as tres
> alteram `H-N`** (IR-01). O que a classificacao informa e o **custo de nao decidir**: dois
> defeitos de contrato e uma medicao errada.

## 2. As tres emendas — diff literal, hashes e impacto

> Hashes conforme [ADR-0012 §5.2, IR-07](../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md):
> **H-A** = `sha256` do arquivo **tal como submetido**; **H-N** = conteudo normativo, com as
> linhas de `IR-03` removidas; **H-P** = apos a transicao **O4**.
> **H-P nao e projetado aqui**: as tres emendas nascem em `em-revisao` e a transicao ocorre
> **apos** o ato, como em `DEP-QAR` 1.1.0.

### 2.1 `DEP-KMS` 1.0.0 → **1.1.0** — fecha **RC-05**

| Campo | Conteudo |
|---|---|
| **ID · versao** | `DEP-KMS` · **1.1.0** *(emenda MENOR sobre 1.0.0)* |
| **Versao em vigor hoje** | **1.0.0** — `H-A` `a63bb267d15d5d81335a60776ebb130d60dbd5b89e62e0702794a25bc638aacf` · `H-N` `613ec1a42677787e21cb3aef8fd7c9bfd72eeeedc85d53f3c05577b154bff327` · **460** linhas |
| **H-A do candidato** | `10cfc73d5e3b7779beb22bef5dc11b0ace1d15f8b0d9855aa8cfbfbb6fec33e5` |
| **H-N do candidato** | `194da2b59c46902cfe2eca5b9f18357221db7c0bceb44530765795cea9d229e8` |
| **Linhas** | **460 → 464** *(+4)* |
| **Alteracoes** | **10** — 3 de frontmatter · **3 linhas normativas novas** · 3 valores de medicao · 1 linha de historico |
| **Blocos tocados** | **B3** *(§4)* · **B6** *(§7)* · **B9** *(§10)* · **B12** *(§13.2)*. **Nenhum outro** |
| **Revisao independente** | **DEP-GOV** — DEP-KMS e objeto e nao revisa o instrumento que define a propria autoridade |
| **Recomendacao** | **APROVAR** |

**Diff literal — campo a campo, e nada alem disto:**

| # | Local | Antes | Depois |
|---|---|---|---|
| K1 | frontmatter | `versao: 1.0.0` | `versao: 1.1.0` |
| K2 | frontmatter | `status: ativo` | `status: em-revisao` |
| K3 | frontmatter | `ratificacao: ratificada` | `ratificacao: pendente` |
| K4 | **§4**, apos a linha *"Alterar Carta de Capability que exerco sem custodiar"* | *(inexistente)* | `\| **Registrar, numerar ou fechar incidente** de conformidade \| **DEP-GOV** *(registra e numera)* · **DEP-QAR** *(fecha)* \| FND-09 §8.2, linha `INC`; FND-03 §2.3 \|` |
| K5 | **§7**, apos a linha *"Reporte / Alerta"* | *(inexistente)* | `\| **Incidente de conformidade** \| `INC` \| **Detecto e reporto** — nao registro, nao numero, nao fecho \| `governance/incidents/` \|` |
| K6 | **§10**, apos `I-10` | *(inexistente)* | `\| **I-11** \| **Registrar, numerar ou fechar incidente de conformidade** \| Detectar e reportar e meu; **registrar e numerar sao de DEP-GOV** e **fechar e de DEP-QAR** \| **DEP-GOV** *(registra e numera)* · **DEP-QAR** *(fecha)* \| FND-09 §8.2, linha `INC` \|` |
| K7 | **§13.2**, secoes 1, 2 e 4 | `**68 linhas**` | `**69 linhas**` |
| K8 | **§13.2**, + secoes 5 e 10 | `**139 linhas**` | `**141 linhas**` |
| K9 | **§13.2**, Carta integral | `**460 linhas**` | `**464 linhas**` |
| K10 | Historico de versoes | *(inexistente)* | linha `1.1.0`, descrevendo K4 a K9 |

> **K7 a K9 nao sao correcao de defeito: sao a regra DR-6 aplicada.** A propria Carta escreveu,
> em §13.2, que medir depois de alterar e obrigatorio e que o metodo e *medir → substituir na
> linha existente → remedir se a contagem mudar*. As tres substituicoes **nao alteram o numero
> de linhas**, e por isso o metodo estabiliza em uma passagem — **verificado**, nao presumido.

**Impacto:**

| Dimensao | Impacto |
|---|---|
| Autoridade criada | **ZERO.** `I-11` e **impedimento**, nao poder. As tres linhas novas so declaram o que **nao** e de DEP-KMS e o que ele **reporta** |
| Titulares alterados | **ZERO.** Registro e numeracao continuam de DEP-GOV; fechamento continua de DEP-QAR (FND-09 §8.2, linha `INC`) |
| Documentos em cascata | **ZERO.** Nenhuma fundacional, nenhuma Carta de Capability, nenhum outro artefato precisa mudar |
| Projecoes a atualizar | **2** — `departments/README §2` *(linhas e impedimentos)* e `capabilities/README` **nao** muda *(custodia inalterada)* |
| Custo de contexto | **+4 linhas** no acervo · o recorte de decisao de DEP-KMS passa de **139** a **141** linhas *(30% da Carta, inalterado)* |
| Reversibilidade | **Tipo 2.** Sem dado vivo, sem exposicao externa, sem migracao |

**Por que aprovar.** DEP-KMS e o unico dos nove que **nao diz uma palavra sobre incidente** — nem
para reivindicar, nem para excluir. Os outros oito declaram o proprio papel, ainda que apenas
para dizer que o incidente operacional e de DEP-OPS. **DEP-KMS escala `E4` por *"perda de
memoria — registro destruido ou irrecuperavel"* e por *"credencial encontrada em registro
curado"*, e nenhuma das duas linhas diz o que acontece com o incidente que essas situacoes
abrem.** A emenda escreve o caminho que ja e obrigatorio por FND-09 §8.2 e o torna legivel na
Carta que o operador carrega.

### 2.2 `DEP-ENG` 1.0.0 → **1.1.0** — fecha **RC-07**

| Campo | Conteudo |
|---|---|
| **ID · versao** | `DEP-ENG` · **1.1.0** *(emenda MENOR sobre 1.0.0)* |
| **Versao em vigor hoje** | **1.0.0** — `H-A` `f50891c7096e50632a9f7d21e2b7d99ecee250129c87207642fcfb02e6fd67db` · `H-N` `4c0b111df1da13a0bd70d693436102bf5bc853a19e2f3e4c57b3ba34cee061f7` · **400** linhas |
| **H-A do candidato** | `38d4613d88b8253cd8b34d6b2b51fcc68624dfeb9509093de6678f9968428be9` |
| **H-N do candidato** | `e486a9f6206e73a80ef60b57b02efc190d586b6510f38f8b62f90c924ffab713` |
| **Linhas** | **400 → 402** *(+2)* |
| **Alteracoes** | **7** — 3 de frontmatter · **1 linha normativa nova** · 2 valores de medicao · 1 linha de historico |
| **Blocos tocados** | **B9** *(§10)* · **B12** *(§13.2)*. **Nenhum outro** |
| **Revisao independente** | **DEP-GOV** |
| **Recomendacao** | **APROVAR** |

**Diff literal:**

| # | Local | Antes | Depois |
|---|---|---|---|
| E1 | frontmatter | `versao: 1.0.0` | `versao: 1.1.0` |
| E2 | frontmatter | `status: ativo` | `status: em-revisao` |
| E3 | frontmatter | `ratificacao: ratificada` | `ratificacao: pendente` |
| E4 | **§10**, apos `I-8` | *(inexistente)* | `\| **I-9** \| **Aprovar, revisar ou emendar esta Carta** \| E o instrumento que define a minha propria autoridade \| **DEP-GOV** *(revisa)* · **SOBERANO** *(aprova e ratifica)* \| RM-06b, LV-03; FND-09 §8.2 \|` |
| E5 | **§13.2**, + secoes 5 e 10 | `**115 linhas**` | `**116 linhas**` |
| E6 | **§13.2**, Carta integral | `**400 linhas**` | `**402 linhas**` |
| E7 | Historico de versoes | *(inexistente)* | linha `1.1.0`, descrevendo E4 a E6 |

**Impacto:**

| Dimensao | Impacto |
|---|---|
| Autoridade criada | **ZERO** — e **removida** tambem zero: `I-9` declara um impedimento que **ja existe** por AU-09 e por FND-09 §8.2. A emenda escreve, nao institui |
| Efeito pratico | **NULO hoje** — e a razao pela qual RC-07 nasceu com severidade **Media** e nao Alta. O que muda e a **simetria**: as nove passam a declarar |
| Documentos em cascata | **ZERO** |
| Projecoes a atualizar | **1** — `departments/README §5`, linha *"Aprovar, revisar ou emendar a propria Carta"*: **8 de 9 → 9 de 9** |
| Custo de contexto | **+2 linhas**; recorte de decisao **115 → 116** *(29% da Carta, inalterado)* |
| Reversibilidade | **Tipo 2** |

**Por que aprovar.** E a **unica** das nove Cartas que nao declara o impedimento sobre a propria
Carta, e a assimetria so aparece quando as nove sao lidas juntas. **O efeito e nulo e a lacuna e
real** — e a natureza dela e exatamente a que `DC-03` existe para impedir: o departamento de
**maior custodia do sistema** (cinco Capabilities) e o que menos declara sobre si.

### 2.3 `DEP-QAR` 1.1.0 → **1.2.0** — fecha **RC-01**

| Campo | Conteudo |
|---|---|
| **ID · versao** | `DEP-QAR` · **1.2.0** *(emenda MENOR sobre 1.1.0)* |
| **Versao em vigor hoje** | **1.1.0** — `H-A` `3e69441e2acab1cc34ff03da16c9e8bb004b65295736e08f9da53dfe0eaca3a0` · `H-N` `747862a940eede8a8ece803d0a3d16cd1a0ecdbceef5d7a84fe6c72d78ee4487` · `H-P` `67407fffa111b7ab4c2910e328013d3d05fd8dcae9455d266eb3fdcf87b3d144` · **387** linhas |
| **H-A do candidato** | `41f55e7369af5a9456e621cb4abd874a5c2c61af7e5a06b1900b4ca1619b5f2b` |
| **H-N do candidato** | `658de6c3d53f53a4ed71adecf793067c377e1b04908d9d259cdb636a1120c725` |
| **Linhas** | **387 → 388** *(+1)* |
| **Alteracoes** | **5** — 3 de frontmatter · 1 valor de medicao · 1 linha de historico |
| **Blocos tocados** | **B12** *(§13.2)*. **Nenhum bloco normativo** |
| **Revisao independente** | **DEP-GOV** — ver residuo no bloco Responsaveis |
| **Recomendacao** | **APROVAR** |

**Diff literal:**

| # | Local | Antes | Depois |
|---|---|---|---|
| Q1 | frontmatter | `versao: 1.1.0` | `versao: 1.2.0` |
| Q2 | frontmatter | `status: ativo` | `status: em-revisao` |
| Q3 | frontmatter | `ratificacao: ratificada` | `ratificacao: pendente` |
| Q4 | **§13.2**, Carta integral | `**386 linhas**` | `**388 linhas**` |
| Q5 | Historico de versoes | *(inexistente)* | linha `1.2.0`, descrevendo Q4 |

> **O valor correto e 388, nao 387 — e a diferenca e a armadilha deste achado.** O arquivo em
> vigor tem **387** linhas; a linha de historico que a emenda 1.2.0 acrescenta faz **388**.
> Declarar **387** seria repetir o defeito com um ciclo de atraso: e exatamente o que a emenda
> 1.1.0 fez ao acrescentar uma linha e nao remedir. **A medicao foi feita sobre o arquivo
> emendado**, e o metodo — `sed`+`wc -l` sobre os intervalos de secao — foi **validado primeiro
> contra os valores ja declarados**, reproduzindo **50** e **111** exatamente.
>
> Os dois recortes menores **nao mudam**: a linha acrescentada esta **depois** da secao 13, fora
> dos intervalos de 1, 2, 4, 5 e 10. **111 / 388 = 28,6%**, que continua arredondando para os
> **29%** declarados.

**Impacto:**

| Dimensao | Impacto |
|---|---|
| Conteudo normativo | **ZERO alterado.** Nenhum impedimento, autoridade, fronteira, interface ou indicador muda |
| Autoridade · titulares | **ZERO** |
| Documentos em cascata | **ZERO** |
| Projecoes a atualizar | **1** — `departments/README §2`, linha *Carta integral*: **387 → 388** |
| Custo de contexto | **+1 linha** |
| Reversibilidade | **Tipo 2** |

**Por que aprovar.** E a emenda mais barata do lote e a que fecha a divida mais visivel: uma
Carta **em vigor** que declara um numero que ela propria contradiz. **O custo de nao aprovar nao
e o numero errado — e a regra que ele corroi:** DC-10 diz que o perfil de carregamento e
**medido, nunca estimado**, e uma medicao publicada e errada e pior do que ausencia declarada.

## 3. Quadro consolidado — as tres em uma leitura

| Carta | De → Para | Achado | Classe do achado | Alteracoes | Linhas | Blocos normativos tocados | **Recomendacao** |
|---|---|---|---|---|---|---|---|
| `DEP-KMS` | 1.0.0 → **1.1.0** | **RC-05** | Normativo | **10** | 460 → **464** | B3 · B6 · B9 | **APROVAR** |
| `DEP-ENG` | 1.0.0 → **1.1.0** | **RC-07** | Normativo | **7** | 400 → **402** | B9 | **APROVAR** |
| `DEP-QAR` | 1.1.0 → **1.2.0** | **RC-01** | Projecao | **5** | 387 → **388** | **nenhum** | **APROVAR** |

**3 recomendacoes de APROVAR · 0 de DEVOLVER · 22 alteracoes · +7 linhas · 0 titulares alterados
· 0 autoridades criadas · 0 documentos em cascata.**

> ### Tres de tres aprovadas, de novo — e a vigilancia que isso obriga
> **PS-2026-002 recomendou 5 de 5.** Este pacote recomenda **3 de 3**. Somados, **8 objetos
> submetidos e nenhuma devolucao** — o numero que **FT-04** manda vigiar.
>
> **A mitigacao e verificavel e esta declarada:** as tres emendas nao nasceram de julgamento
> novo, e sim de **achados que o proprio sistema registrou contra si** ha um ciclo, com dono e
> gatilho — e o gatilho literal de **R4 de FIT-2026-008** era *"proxima emenda a cada uma das
> tres Cartas"*. **Devolver seria coerente apenas se o achado fosse falso**, e os tres foram
> **remedidos por ferramenta nesta missao**: `DEP-KMS` tem **0** ocorrencias do termo
> *incidente* em 460 linhas; `DEP-ENG` tem **8** impedimentos e **nenhum** sobre a propria
> Carta; `DEP-QAR` declara **386** onde `wc -l` conta **387**.
>
> **O que este pacote nao faz e inflar o lote.** Cinco achados novos foram levantados nesta
> missao e **nenhum deles entrou aqui** — §5.

## 4. Se o Soberano aprovar — o que muda, exatamente

| # | Efeito | Operacao |
|---|---|---|
| A1 | As tres Cartas sao **editadas pela primeira vez nesta missao**, exatamente no diff de §2 | Emenda MENOR (AL-01) |
| A2 | `status` `em-revisao` → **`ativo`**; `ratificacao` `pendente` → **`ratificada`** | **O4** (FND-10 §5.2) |
| A3 | Registro canonico do ato, com **H-A, H-N e H-P** por Carta e o diff exato | Novo `MSG`, conforme IR-07 e IR-08 |
| A4 | **`IR-09`** executado sobre as tres, por **DEP-QAR**, com conferencia independente de **DEP-GOV** *(RC-02)* | IR-09 |
| A5 | **R4 de FIT-2026-008 fecha** — as tres, e nao parte delas | Reconciliacao |
| A6 | As versoes substituidas — `DEP-KMS` 1.0.0, `DEP-ENG` 1.0.0, `DEP-QAR` 1.1.0 — ficam preservadas por **hash + diff reversivel + copia datada + historico**, sem segundo arquivo | PV-1 a PV-4 de MSG-2026-0003 §2.1 |
| A7 | Catalogo, projecao `departments/README` e baseline atualizados na mesma mudanca | CV-04, IX-02 |

**Nenhum efeito e irreversivel.** As tres emendas sao **Tipo 2**: sem dado vivo, sem exposicao
externa, sem migracao, sem credencial.

## 5. O que **nao** esta neste pacote, e por que

| Objeto | Por que nao esta |
|---|---|
| As **cinco** Cartas em `em-revisao` | Objeto de **PS-2026-002**, submetido antes e **nao alterado** desde entao — integridade reconferida nesta missao, hash a hash |
| **ADR-0014** *(emenda C3)* | Materia **C3**, separada por rito (DC-09, FND-01 §9). Continua em **PS-2026-002 §4** |
| **Q2** *(`FIT` exige ratificacao?)* | **C2 escalada**, sem ADR candidato, por decisao vigente de ADR-0012 §5.5 |
| **RD-01** — `DEP-PRD §8.2` cita FND-02 §4 como declarando `—` entre PRD e TLS; a matriz declara `C` no sentido PRD→TLS e `—` **apenas** no sentido TLS→PRD | A Carta esta em **`em-revisao`** e o seu `H-A` ja foi submetido em PS-2026-002. Corrigi-la **mudaria o objeto que o Soberano vai decidir**. Divergencia se declara, **nunca se corrige em silencio** |
| **RD-02** — os campos `GOV→KMS` e `QAR→KMS` de FND-02 §4 declaram `E`, e a leitura obrigatoria da mesma tabela declara que a Guarda **veta Linha e Plataforma** | **Ambiguidade na fonte fundacional.** Nao e corrigivel por emenda de Carta: exige emenda a **FND-02**. Dono **DEP-GOV** |
| **RD-03** — `DEP-KMS §6.3` declara *"entrega a sete departamentos e consulta dois"*; a linha KMS de FND-02 §4 tem **6** `E`, **2** `C` e **1** `—` | **Achado desta missao, em Carta ratificada.** Nao foi acrescentado a emenda `DEP-KMS` 1.1.0 **de proposito**: inflaria um pacote cujo objeto o Soberano ja conhece por R4. Dono **DEP-EXE**, gatilho *"proxima emenda a `DEP-KMS`"* |
| **RD-04** — `governance/README` declara baseline `BL-…-05` e **14** ressalvas abertas; as fontes declaram `BL-…-06` e **15** | **Nao depende do Soberano.** E defeito de **projecao** (M3): corrige-se na vista, nunca na fonte (RG-03, PJ-03). **Corrigido nesta missao** |
| **RD-05** — o ato consumido por esta missao chegou como **minuta com marcadores** `[VERSAO]` e `[HASH INTEGRAL]` | E a **causa do BLOCKED** desta missao, nao materia de decisao. Tratado em [PT-2026-001](relatorio-transicao-2026-07-29-departamentos.md) |
| Qualquer agente, skill, workflow, spec, produto ou ferramenta | **Nenhum foi criado**, por determinacao |

## 6. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Contrato das Cartas | [ADR-0011](../decisions/ADR-0011-contrato-de-carta-de-departamento.md), **DC-01 a DC-10** |
| Regra de integridade aplicada | [ADR-0012](../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md), `IR-01` a `IR-10` |
| Ressalva que este pacote existe para fechar | **R4** de [FIT-2026-008](fitness/FIT-2026-008-rollout-das-cartas.md) |
| Achados tratados | **RC-01** · **RC-05** · **RC-07** |
| Onde os achados foram declarados | [REV-ROLLOUT §7](../foundation/revisao-arquitetural-rollout-cartas-2026-07-28.md) · [`departments/README §6`](../departments/README.md), L-5 a L-7 · [catalogo mestre §7](artifact-registry.md), item 23 |
| Precedente de forma da emenda | [MSG-2026-0003 §2.1 e §7.2](../memory/operacional/MSG-2026-0003-ato-soberano-emenda-qar-e-criterio-de-consolidacao.md) — `DEP-QAR` 1.1.0 |
| Pacote irmao, nao alcancado por este | [PS-2026-002](pacote-soberano-2026-07-28-cartas.md) |
| Relatorio que consolida a missao | [PT-2026-001](relatorio-transicao-2026-07-29-departamentos.md) |
| Verificacao de aptidao | [FIT-2026-009](fitness/FIT-2026-009-ativacao-e-endurecimento.md) |
| Baseline vigente na submissao | **`BL-2026-07-29-01`** — [catalogo mestre §10](artifact-registry.md) |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-GOV | Pacote da **Missao 1.10**: **tres** emendas candidatas MENORES a Cartas ja ratificadas — `DEP-KMS` 1.1.0 *(RC-05, normativo)*, `DEP-ENG` 1.1.0 *(RC-07, normativo)* e `DEP-QAR` 1.2.0 *(RC-01, projecao)* —, com **diff literal campo a campo**, `H-A` e `H-N` medidos, impacto e revisao independente por objeto. **22 alteracoes, +7 linhas, 0 titulares alterados, 0 autoridades criadas, 0 cascata.** **Nenhuma Carta foi editada:** os candidatos vivem como diff e hash, fora do acervo. **Terceiro pacote soberano do sistema.** |
