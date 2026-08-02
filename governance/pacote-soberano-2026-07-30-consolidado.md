---
id: PS-2026-013
titulo: Pacote consolidado — matriz dos catorze objetos e minuta unica do ato soberano
tipo: relatorio
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-07-30
atualizado_em: 2026-07-30
revisao_prevista: null
decisoes_relacionadas: [ADR-0012, ADR-0020, ADR-0022, ADR-0023, ADR-0024, ADR-0025]
substitui: []
substituido_por: null
canal: REPORTE
emissor: DEP-GOV
destinatario: SOBERANO
ttl: ate decisao do Soberano
projecao_de: PS-2026-009 §4, PS-2026-010 §4, PS-2026-011 §4, PS-2026-012 §4
resumo: Consolida os catorze objetos dos quatro pacotes pendentes numa matriz unica e numa unica minuta, com ordem de aplicacao e bloqueio isolado por objeto.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# PS-2026-013 — Pacote consolidado e minuta unica

> ## Este pacote **informa** e **projeta**. Nao decide, nao aprova, nao promulga e nao edita nada.
>
> **Nenhum objeto novo e submetido aqui.** Os **catorze** ja estao submetidos em
> [PS-2026-009](pacote-soberano-2026-07-29-fnd-11.md) **2.0.0**,
> [PS-2026-010](pacote-soberano-2026-07-29-rd-31.md),
> [PS-2026-011](pacote-soberano-2026-07-30-rd-27.md) e
> [PS-2026-012](pacote-soberano-2026-07-30-rd-37.md). **Este pacote os enumera numa unica
> matriz e numa unica minuta, para que o ato nao precise reconciliar quatro documentos.**
>
> **Caminho exato:** `governance/pacote-soberano-2026-07-30-consolidado.md` *(`RE-01`)*.

> ### Declaracao de projecao — `PJ-02`
>
> | Campo | Conteudo |
> |---|---|
> | **Fonte** | `PS-2026-009 §4`, `PS-2026-010 §4`, `PS-2026-011 §4`, `PS-2026-012 §4` |
> | **Campos projetados** | `id` · `versao vigente` · `versao candidata` · `linhas` · `H-A` · `H-N` · `H-P` · `pacote` · `ordem` |
> | **Finalidade** | O ato soberano precisa enumerar **catorze** objetos numa peca so. Linkar quatro pacotes **transferiria ao Soberano** a reconciliacao — e e exatamente a reconciliacao que esta missao existe para fazer |
> | **Metodo de atualizacao** | **`CV-04`** — pela mesma mudanca que altera qualquer pacote de origem. **Em divergencia, a fonte prevalece** (`PJ-03`), e o defeito e desta matriz |

## Proposito

Entregar ao Soberano **uma** peca: a matriz completa dos objetos e **uma** minuta que os enumere
integralmente, com **cada objeto bloqueavel isoladamente** e **sobreposicao de diff igual a zero**.

## Escopo

| Item | Definicao |
|---|---|
| Inclui | A **matriz** dos catorze objetos *(§2)*, a **ordem de aplicacao** *(§3)*, a **prova de nao sobreposicao** *(§4)*, o **recalculo do custo de reversao de `ADR-0020`** *(§5)* e a **minuta unica** *(§6)* |
| **Nao** inclui | Objeto novo · diff novo · hash novo — **todos vem das fontes** · o **merito** de qualquer um dos quatro pacotes · `RD-33`, `S1`, `S2` — **nao resolvidos, e §7 diz por que** |

---

## 1. De onde vem cada objeto

| Pacote | Versao | Objetos | Achado |
|---|---|---|---|
| [PS-2026-009](pacote-soberano-2026-07-29-fnd-11.md) | **2.0.0** | `ADR-0022` · `FND-11` · `FND-03` | canonizacao |
| [PS-2026-010](pacote-soberano-2026-07-29-rd-31.md) | 1.0.0 | `ADR-0023` · `DEP-PRD` · `DEP-EXE` | `RD-31` |
| [PS-2026-011](pacote-soberano-2026-07-30-rd-27.md) | 1.0.0 | `ADR-0024` · **`FND-01`** · `FND-02` · `FND-10` | **`RD-27`** |
| [PS-2026-012](pacote-soberano-2026-07-30-rd-37.md) | 1.0.0 | `ADR-0025` · `DEP-OPS` · `DEP-GRW` · `DEP-TLS` | **`RD-37`** |

> **`FND-01` migrou de pacote, e essa e a coordenacao que a missao exigia.** Ele era objeto de
> `PS-2026-009` em **duas variantes**; passa a ser objeto de `PS-2026-011` em **uma**, cumulativa
> sobre a emenda que `ADR-0022` autoriza. **`PS-2026-009` 2.0.0 remete, e nao duplica.**

## 2. Matriz — objeto → versao vigente → candidato → `H-A` → `H-N` → `H-P` → pacote → ordem

| # | Objeto | Vigente | Candidato | Linhas | `H-A` do candidato | `H-N` | `H-P` *(apos `O4`)* | Pacote | Ordem |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **`ADR-0022`** | *(retido)* | **1.0.0** | 438 | `f02fbaf78e1627ecf9b819cb33f7da9760e65b69c16e34ee88e79f38ab513810` | `a6f954c304496041199c8c80c666d36016337aab3e26f3d745390b288f7e0316` | `2dd4d591bf8051845ee9985d459a9fa69c196a4482c6fd3d2f262a02005b4a05` | 009 | **1** |
| 2 | **`ADR-0023`** | *(retido)* | **1.0.0** | 353 | `3f8886d6892954c4a6f5703fe1b272290fc4165a7175fd4289d46b04f2907e51` | `e727f50cd3c7a0399edb2a6c3c089433a16c47a44d69dc25aaf3b4e017bc8f10` | `e0d6aa2dff881e62260af38672356ecc8057c01d925af861e40b24820bac84cc`※ | 010 | **2** |
| 3 | **`ADR-0024`** | — | **1.0.0** | 341 | `9adfa251357efa63841f763f036f9026a28b5b13a0c4e43a7d0cea2f9ab66072` | `4db0bcb73a9fdaad86c94dd08c7e86285aef4a3e970646a0914129b064e004aa` | `874ae531e26096897fca61adb766853829c065c9d43ee6411f99c4d35573b0ce` | 011 | **3** |
| 4 | **`ADR-0025`** | — | **1.0.0** | 292 | `a6f4ee80a59f02c8238f6d463ccfcbc2103d29f9af8a1848a91c1b2fcccf9124` | `0c58c58b4758203123f5a75172b6af60abf09a579de17d080e31dbe60e2afaea` | `a1e7f8c04024ed50998f11c49455fc7efe8cdf6af4221ab21968c2b489c68b59` | 012 | **4** |
| 5 | **`FND-11`** | *(nao existe)* | **1.0.0** | 399 | `4b5620f9cad1213350633f88893dfe3384ecb461955881e74da8f559d06ee6c6` | `90f4efb74e2d2573e9f4fdf69db43e3da863f3b1e09926febe22517f32ca79ee` | `383ee51df8ee8782a693897f07423529bc4dd5a7d866603ad31e61fe06ad7c20` | 009 | **5** |
| 6 | **`FND-01`** | 1.5.0 | **1.7.0** *(cumulativa)* | 493 | `d319223519dfd576ef279e413736eda7496d553d309c2266b18f4cbcd69f935b` | `f5172f2179793bbd2ee86bd5cf92af3e449297e9a0bc981c3b4585176e65e963` | **= `H-A`** | **011** | **6** |
| 7 | **`FND-02`** | 1.3.0 | **1.4.0** | 524 | `1fb4e49b6f82abd98977b4c1ee1ea89c11fda2a6303ff8c3e7cca2b0f837ddb6` | `66d4651b7f121642ae344498d87aa0fafbfff80233c6743da9fe5bda10c06a36` | **= `H-A`** | 011 | **7** |
| 8 | **`FND-03`** | 1.5.0 | **1.6.0** | 633 | `82694fad45f3de1ff1e93b6cfc81bd570d7d087e63374f46a2ba69800286b959` | `1004673a5d01941560d073c022849cea17bb074caf010c48e8fa7b1062424b4e` | **= `H-A`** | 009 | **8** |
| 9 | **`FND-10`** | 1.4.0 | **1.5.0** `CRLF` | 785 | `10f03ebd6ac3583a17a2819d9a2296ecad6f106913d96224e5b4db0826f506f0` | `651fbaf091731a845045f25c7f3ec77cc49a9e909229826889142c64bc72e146` | **= `H-A`** | 011 | **9** |
| 10 | **`DEP-PRD`** | 1.0.0 | **1.1.0** | 445 | `09d076dd305e2bd8cc2119772706141cdcfef998cd3ba9e7540267909699fb24` | `ce3490049a57e6c141a40a07bcb7da1881b0389c4fe8134b359c7bf406d40279` | `0e98511630faf9d5bec4c7cb36d8a37fa0bf15506dfde36954f0419e2720fc15` | 010 | **10** |
| 11 | **`DEP-EXE`** | 1.0.0 | **1.1.0** | 506 | `975e26dbf3f7f8760af01310b27b6b7e1667593d3dc12b520aeed9981013f25b` | `537eb9f474dcc6e778c911d3abbe5cc9e4a84ec79914cf2aadb15d6aa929aab6` | `a75a1ffea140e1f962e97b5b8772df70cf28831df882a25cf804b4e931f17e12` | 010 | **11** |
| 12 | **`DEP-OPS`** | 1.0.0 | **1.1.0** | 438 | `9a5b52c40e0b724a1174641eec63e96becd232c3cacf052d3f738a29f23bfbee` | `b38da97b64be98bd1c84aad4639bf45834d77763eb85802d52b20c9257d26baa` | `78a434888e20ebd30ce85707f64578f94a402c9013ad8740d1dbae464c786e5a` | 012 | **12** |
| 13 | **`DEP-GRW`** | 1.0.0 | **1.1.0** | 444 | `90d596381340bb14ee0a2a38f85e6d97aea95aa6f1ec6d83056c61f1a2f6e9cf` | `304fa9a3119539b210df34fdeb187dac6894732b01a34bfabaa7707c746ac88d` | `22ec7b45bf46970c14d3254732530ec41ff80c0f6ccfc1c5f9c8ed4fb2be92e9` | 012 | **13** |
| 14 | **`DEP-TLS`** | 1.0.0 | **1.1.0** | 425 | `9e27ca81ad53dc8059806084eee07a7e2a15c467ab520b2ca6bf1681fbf93b35` | `65b83520de23c94ad045fb76f71814b7f1db12b0ff29791180aa17759b688d7e` | `857d6703faca27cae0b4d23d743ebe9bc7b1bb1776191f5467f1a4193e165e31` | 012 | **14** |

**Objeto alternativo, medido e NAO submetido** — so vale se o ato bloquear `FND-11`:

| Objeto | Candidato | Linhas | `H-A` | Quando usar |
|---|---|---|---|---|
| `FND-01` **`ALT`** | 1.6.0 | 490 | `a9c0334a376755a275f2b5c1629b32303cb1cd3a1773acd10a67071989e269bb` | **Somente** se o ato **nao** promulgar `FND-11` — [PS-2026-011 §2.4](pacote-soberano-2026-07-30-rd-27.md) |

> **※ `ADR-0023` — os tres valores foram REMEDIDOS, nao copiados.** A fonte e
> [PS-2026-010 §4.2](pacote-soberano-2026-07-29-rd-31.md), **nao reescrita por esta missao**. Esta
> matriz **remediu o arquivo com o instrumento validado de `PS-2026-011 §4.3`** e obteve **353
> linhas** e os **tres hashes acima**, que **reproduzem a fonte digito a digito** — e por isso
> `ADR-0023` conta como **vigesimo controle** da validacao. **`PJ-03` continua valendo:** em
> divergencia futura, **prevalece `PS-2026-010`**, e o defeito e desta matriz. **O `H-P` alcanca
> SOMENTE `status`** — `ratificacao` e `nao-exigida` e **nao vira `ratificada`**.

## 3. Ordem de aplicacao — e por que ela **nao** e arbitraria

| Etapa | Objetos | Por que nesta posicao |
|---|---|---|
| **1** | `ADR-0022`, `ADR-0023`, `ADR-0024`, `ADR-0025` | **Decisao antes de execucao.** Nenhuma promulgacao tem fundamento antes do `ADR` que a autoriza |
| **2** | **`FND-11`** *(criacao)* | **`FND-01` 1.7.0 escreve link para `11-framework-specifications.md`.** Aplicar `FND-01` antes deixaria o acervo com **1 link quebrado** entre as duas escritas |
| **3** | `FND-01`, `FND-02`, `FND-03`, `FND-10` | Norma de nivel 1 e 2, depois da sede que ela enumera |
| **4** | `DEP-PRD`, `DEP-EXE`, `DEP-OPS`, `DEP-GRW`, `DEP-TLS` | Cartas por ultimo: **elas declaram o que `FND-01 §6.2` ja fixou**, e nenhuma norma depende delas |

**Dentro de cada etapa a ordem e indiferente** — nenhum objeto da mesma etapa alcanca arquivo de
outro. **A unica dependencia real do ato inteiro e a de etapa 2 → 3**, e ela esta nomeada.

### 3.1 Como aplicar — `PT-2026-008 §10.1`, sem alteracao

1. **Conferir `H-A` do candidato ANTES de escrever.** Divergencia = **parar**.
2. **Aplicar por copia binaria.** **`FND-10` e `CRLF`** — modo texto converteria 785 terminadores
   e destruiria o `H-A` sem mudar uma linha de norma.
3. **`O4` apenas em `status` e `ratificacao`.** `atualizado_em` **nao** entra: altera-lo daria
   hash diferente do projetado. **`ADR-0023` e `ADR-0025` executam `O4` so em `status`** —
   `ratificacao` e `nao-exigida` e **nao vira `ratificada`**.
4. **Conferir `H-P` contra o projetado.** Divergencia = **`IR-05`**, incidente.
5. **`IR-09`** por `DEP-QAR`.
6. **So entao** Fitness Check e nova baseline — `BL-02` e a licao de que a baseline se mede
   **depois** da ultima escrita.

## 4. Bloqueio isolado e **sobreposicao de diff igual a zero**

### 4.1 Nenhum arquivo e alcancado por mais de um objeto

| Arquivo | Objetos que o alcancam |
|---|---|
| `foundation/01-constituicao.md` | **1** — `FND-01` 1.7.0 *(cumulativa: contem `ADR-0022` e `ADR-0024`)* |
| `foundation/02-…`, `03-…`, `10-…`, `11-…` | **1** cada |
| `departments/{prd,exe,ops,grw,tls}/carta.md` | **1** cada |
| `decisions/ADR-002{2,3,4,5}-….md` | **1** cada — **`O4`**, nao emenda |

**`0` sobreposicoes em 14 objetos e 14 arquivos.** **Era exatamente aqui que a colisao existia**:
`FND-01` tinha **dois** objetos concorrentes *(`V1`/`V2` de `PS-2026-009`)* e passou a ter **um**.

### 4.2 Bloqueio isolado, objeto a objeto

| Objeto | Bloqueavel sozinho? | O que arrasta |
|---|---|---|
| `ADR-0022` | **Sim** | Arrasta `FND-11`, `FND-01` *(parte `ADR-0022`)* e `FND-03` — **declarado em `PS-2026-009 §1`** |
| `ADR-0023` | **Sim** | Arrasta `DEP-PRD` e `DEP-EXE` |
| `ADR-0024` | **Sim** | Arrasta `FND-01` *(parte `AC-08`)*, `FND-02` e `FND-10` |
| `ADR-0025` | **Sim** | Arrasta `DEP-OPS`, `DEP-GRW`, `DEP-TLS` |
| `FND-11` | **Sim** | **Arrasta `FND-01` 1.7.0** → usar a **`ALT`** `a9c0334a…69bb` |
| **`FND-01`** | **Sim** | **Nao arrasta ninguem** — nenhum outro objeto depende dele |
| `FND-02` · `FND-10` | **Sim** | **`0` dependencias** — `FND-10 §8.5` cita `BL-2026-07-29-10`, **nao** `FND-01` 1.7.0 |
| `FND-03` | **Sim** | `0` — a arvore ganharia linha sem arquivo se `FND-11` cair junto |
| **Cada uma das 5 Cartas** | **Sim** | **`0`** — nenhuma cita outra |

**Um unico acoplamento sobrevive a consolidacao, e ele e de `ADR-0022`, nao desta missao:**
`FND-11` + `FND-01` + `FND-03` foram declarados **objeto normativo unico** em `PS-2026-009 §1`,
porque hierarquia se define **por enumeracao** e o que nao consta **nao ocupa nivel**. **A `ALT`
de `FND-01` existe para que ate esse acoplamento tenha saida medida.**

## 5. Recalculo do custo de reversao futuro de `ADR-0020` — **sem reclassificacao retroativa**

> **`ADR-0020` permanece `C2 · Tipo 2`, e `0` bytes seus sao tocados.** Ele e **`M1`** e **nao se
> emenda** (`AC-10`, `CC-01`, `LV-04`). **Este recalculo vive aqui, fora dele** — que e o unico
> lugar onde pode viver.

`ADR-0020 §10` mediu, em 2026-07-29: **"1 ADR novo + 6 indices `M3`"**. **A contagem de `M3`
continua exata. O que a medicao original nao contava triplicou:**

| Medida | Missao 1.13 *(quando `ADR-0020` foi escrito)* | Missao 1.13.1 | **Agora — 1.13.2** |
|---|---|---|---|
| Artefatos que citam `ADR-0020` | **11** | **17** | **19** |
| — **`M3`** *(indices e catalogo, **editaveis** na reversao)* | **6** | **6** | **6** |
| — **`M1` / historico** *(**nao** editaveis)*, exceto o proprio `ADR-0020` | **4** | **10** | **12** |

**Custo recalculado da reversao futura de `ADR-0020`:**

| Componente | Valor | Natureza |
|---|---|---|
| ADR sucessor | **1** | inalterado |
| Indices `M3` a atualizar | **6** | **inalterado — a medicao original acertou** |
| Artefatos normativos a migrar | **`0`** | **inalterado** — nenhum depende de `PA-*` para existir |
| **`M1`/historico que passam a citar decisao superada, e `nao` sao corrigiveis** | **4 → 12** | **triplicou, e nunca fora contado** |

> **O que o recalculo mostra, e nao e o numero.** A parte do custo que `ADR-0020 §10` mediu
> **permaneceu estavel**; a que ele **nao mediu** — a referencia pendurada em artefato imutavel —
> **cresceu 3×** em duas missoes, e **cresce a cada `ADR`, `FIT`, `PT` ou `MEM` que o cite**.
> **Isso nao reclassifica `ADR-0020`:** `Tipo 2` continua correto, porque **nenhum artefato
> normativo migra** e a reversao continua **barata e conhecida**. **O que muda e que ela deixa de
> ser limpa** — e essa distincao so aparece quando o custo e **remedido**, nao relido. Achado
> **`RD-48`**, severidade **Baixa**, dono **DEP-GOV**, gatilho *"proxima superacao de `ADR` com
> mais de 10 citacoes em `M1`"*.

## 6. Minuta unica do ato — **os catorze objetos, integralmente enumerados**

> ### Esta secao **nao e um ato**. Nada aqui produz efeito. **Nenhum objeto entrou em vigor.**

```
ATO SOBERANO DO FUNDADOR — <data do ato>

Apos revisar governance/pacote-soberano-2026-07-30-consolidado.md e os quatro pacotes
que ele consolida — PS-2026-009 2.0.0, PS-2026-010, PS-2026-011 e PS-2026-012 —, as
RFC-0018, RFC-0019 e RFC-0020, os ADR-0022 a ADR-0025, os candidatos, os diffs
literais, as evidencias, as revisoes independentes, os riscos e as ressalvas:

I — APROVO E RATIFICO EXPRESSAMENTE:

- ADR-0022, versao 1.0.0, C3 Tipo 1,
  SHA-256 f02fbaf78e1627ecf9b819cb33f7da9760e65b69c16e34ee88e79f38ab513810,
  cujo SHA-256 apos a transicao de estado devera ser
  2dd4d591bf8051845ee9985d459a9fa69c196a4482c6fd3d2f262a02005b4a05;

- ADR-0024, versao 1.0.0, C3 Tipo 2,
  SHA-256 9adfa251357efa63841f763f036f9026a28b5b13a0c4e43a7d0cea2f9ab66072,
  cujo SHA-256 apos a transicao de estado devera ser
  874ae531e26096897fca61adb766853829c065c9d43ee6411f99c4d35573b0ce.

II — APROVO (C2 Tipo 2, ratificacao nao exigida — FND-04 §2.1):

- ADR-0023, versao 1.0.0,
  SHA-256 3f8886d6892954c4a6f5703fe1b272290fc4165a7175fd4289d46b04f2907e51,
  cujo SHA-256 apos a transicao de estado devera ser
  e0d6aa2dff881e62260af38672356ecc8057c01d925af861e40b24820bac84cc,
  transicao que alcanca SOMENTE o campo status;

- ADR-0025, versao 1.0.0,
  SHA-256 a6f4ee80a59f02c8238f6d463ccfcbc2103d29f9af8a1848a91c1b2fcccf9124,
  cujo SHA-256 apos a transicao de estado devera ser
  a1e7f8c04024ed50998f11c49455fc7efe8cdf6af4221ab21968c2b489c68b59,
  transicao que alcanca SOMENTE o campo status.

III — AUTORIZO A PROMULGACAO, NESTA ORDEM:

- FND-11, versao 1.0.0, criacao,
  SHA-256 4b5620f9cad1213350633f88893dfe3384ecb461955881e74da8f559d06ee6c6,
  cujo SHA-256 apos a transicao de estado devera ser
  383ee51df8ee8782a693897f07423529bc4dd5a7d866603ad31e61fe06ad7c20;

- FND-01, versao 1.7.0, cumulativa das emendas 1.6.0 (ADR-0022) e 1.7.0 (ADR-0024),
  SHA-256 d319223519dfd576ef279e413736eda7496d553d309c2266b18f4cbcd69f935b;

- FND-02, versao 1.4.0,
  SHA-256 1fb4e49b6f82abd98977b4c1ee1ea89c11fda2a6303ff8c3e7cca2b0f837ddb6;

- FND-03, versao 1.6.0,
  SHA-256 82694fad45f3de1ff1e93b6cfc81bd570d7d087e63374f46a2ba69800286b959;

- FND-10, versao 1.5.0, arquivo CRLF,
  SHA-256 10f03ebd6ac3583a17a2819d9a2296ecad6f106913d96224e5b4db0826f506f0.

IV — APROVO E RATIFICO AS CARTAS DE DEPARTAMENTO:

- DEP-PRD 1.1.0, SHA-256 09d076dd305e2bd8cc2119772706141cdcfef998cd3ba9e7540267909699fb24,
  H-P 0e98511630faf9d5bec4c7cb36d8a37fa0bf15506dfde36954f0419e2720fc15;
- DEP-EXE 1.1.0, SHA-256 975e26dbf3f7f8760af01310b27b6b7e1667593d3dc12b520aeed9981013f25b,
  H-P a75a1ffea140e1f962e97b5b8772df70cf28831df882a25cf804b4e931f17e12;
- DEP-OPS 1.1.0, SHA-256 9a5b52c40e0b724a1174641eec63e96becd232c3cacf052d3f738a29f23bfbee,
  H-P 78a434888e20ebd30ce85707f64578f94a402c9013ad8740d1dbae464c786e5a;
- DEP-GRW 1.1.0, SHA-256 90d596381340bb14ee0a2a38f85e6d97aea95aa6f1ec6d83056c61f1a2f6e9cf,
  H-P 22ec7b45bf46970c14d3254732530ec41ff80c0f6ccfc1c5f9c8ed4fb2be92e9;
- DEP-TLS 1.1.0, SHA-256 9e27ca81ad53dc8059806084eee07a7e2a15c467ab520b2ca6bf1681fbf93b35,
  H-P 857d6703faca27cae0b4d23d743ebe9bc7b1bb1776191f5467f1a4193e165e31,

exatamente nos diffs literais registrados em PS-2026-009 §2, PS-2026-010 §2 e §3,
PS-2026-011 §2 e PS-2026-012 §2.

V — DECLARACOES EXPRESSAS DESTE ATO:

1. ADR-0022 e classificado C3 Tipo 1, e a reversao da sede fundacional exige emenda
   de mesmo rito. A duvida de Q1 de PS-2026-009 §9.1 fica RESOLVIDA neste sentido.
2. ADR-0020 permanece C2 Tipo 2. Este ato NAO o reclassifica e NAO o edita; o
   recalculo do seu custo de reversao futuro esta em PS-2026-013 §5, fora dele.
3. Este ato NAO autoriza gravar superado_por em ADR-0021. Q3 de PS-2026-009 §9.1
   fica RESOLVIDO no sentido de NAO gravar: ADR-0021 permanece com 0 bytes
   alterados, inclusive no frontmatter, e a sucessao permanece legivel nos quatro
   lugares de PS-2026-009 §3. RD-43 permanece DECLARADO e nao resolvido.
4. FND-01 entra em vigor em UMA unica versao — 1.7.0 cumulativa. As variantes V1
   (acec800b…a3a8) e V2 (43cae800…6767) NAO sao promulgadas e permanecem apenas
   como evidencia historica. A variante ALT (a9c0334a…69bb) so teria objeto se
   este ato NAO promulgasse FND-11, o que nao e o caso.
5. A entrada em vigor depende de verificacao independente de identidade, versao,
   hash integral, diff literal, revisao e inexistencia de alteracao entre o
   candidato revisado e o objeto aplicado. A aplicacao e por copia binaria; FND-10
   e CRLF e sua conversao invalida o ato quanto a ele.
6. As versoes substituidas — FND-01 1.5.0, FND-02 1.3.0, FND-03 1.5.0, FND-10 1.4.0
   e as cinco Cartas 1.0.0 — deverao permanecer recuperaveis como versoes
   historicas.

VI — O QUE ESTE ATO NAO FAZ:

Nao cria titular, portao, papel, classe, verbo de autoridade, entidade ou tipo
documental novo; nao altera direito de decisao de FND-01 §7.3, principio imutavel,
linha vermelha ou nivel da hierarquia normativa — o nivel 2 recebe um decimo
primeiro membro e a regra de precedencia interna permanece literalmente identica;
nao altera o vinculo entre Spec e Produto, a sequencia por Produto ou os locais
canonicos; nao amplia o nucleo obrigatorio, que continua sendo quatro artefatos;
nao altera a lista fechada de IR-03; nao cria excecao formal; nao edita ADR-0020,
ADR-0021, artefato historico, MSG, FIT ou baseline; nao resolve RD-33, S1, S2,
RD-13, RD-36, RD-43 nem RD-47; e nao alcanca qualquer objeto nao enumerado
expressamente nas secoes I a IV.

VII — NENHUMA SPEC, PRODUTO, PROJETO, SKILL, TOOL, COMMAND, WORKFLOW, AGENTE,
CODIGO OU INFRAESTRUTURA e criado, autorizado ou tornado criavel por este ato.
RD-33 permanece a unica pendencia bloqueante do acervo.
```

## 7. O que este pacote **nao** resolve — e por determinacao

| Item | Estado | Por que |
|---|---|---|
| **`RD-33`** | **ABERTO e BLOQUEANTE** | Nenhuma `Spec` e criavel: `FND-04 §6` exige *"Produto existe"* e **`0` Produtos existem**. **Nao reaberto** |
| **`S1` / `S2`** | **Via decidida, execucao deferida** | O Soberano fixou **`S1`, com Produto real — `nXtrack`, se seguir sendo o primeiro produto comercial** — e **`S2` deferida** ate surgir necessidade observada de `Spec` nao vinculada a Produto. **Este ato nao cria Produto**, e a missao proibe cria-lo |
| **`RD-43`** | **DECLARADO** | Alterar `IR-03` e `C2` com ADR proprio (`IR-04`) |
| **`RD-47`, `RD-48`** | **Nascem declarados** | Dono e gatilho proprios; resolve-los seria `C2` sobre `FND-10` e sobre a norma de superacao |
| `RD-13`, `RD-36` | **ABERTOS** | Fora do escopo determinado |

## 8. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Pacotes consolidados | [PS-2026-009](pacote-soberano-2026-07-29-fnd-11.md) **2.0.0** · [PS-2026-010](pacote-soberano-2026-07-29-rd-31.md) · [PS-2026-011](pacote-soberano-2026-07-30-rd-27.md) · [PS-2026-012](pacote-soberano-2026-07-30-rd-37.md) |
| Regra de integridade | [ADR-0012](../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md), `IR-01` a `IR-10` |
| Ordem de aplicacao | [PT-2026-008 §10.1](relatorio-transicao-2026-07-29-canonizacao.md) |
| Achado que abre | **`RD-48`** — §5 |
| Verificacao de aptidao | [FIT-2026-017](fitness/FIT-2026-017-convergencia-pre-ratificacao.md) |
| Relatorio da missao | [PT-2026-009](relatorio-transicao-2026-07-30-convergencia.md) |
| Baseline vigente na submissao | **`BL-2026-07-29-10`** |

---

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-30 | DEP-GOV | Pacote consolidado da **Missao 1.13.2**. **Decimo pacote soberano, e o primeiro que nao submete objeto novo:** projeta os **catorze** objetos dos **quatro** pacotes pendentes numa **matriz unica** *(objeto → vigente → candidato → linhas → `H-A` → `H-N` → `H-P` → pacote → ordem)* e numa **unica minuta**, com **declaracao de projecao `PJ-02` completa** e `projecao_de` no frontmatter. **§4 prova o que a missao exigia: sobreposicao de diff igual a `0` em 14 objetos e 14 arquivos** — e nomeia onde a colisao existia, `FND-01`, que tinha **dois** objetos concorrentes e passou a ter **um**. **§4.2 declara o unico acoplamento que sobrevive** — `FND-11` + `FND-01` + `FND-03`, herdado de `PS-2026-009 §1` e nao desta missao — e registra que ate ele tem **saida medida**, a `ALT` `a9c0334a…69bb`. **§3 fixa a ordem por dependencia, nao por conveniencia**, e nomeia a **unica** dependencia real do ato inteiro: `FND-01` escreve link para `FND-11`, logo a criacao precede a promulgacao. **§5 recalcula o custo de reversao futuro de `ADR-0020` sem reclassifica-lo e sem toca-lo** — ele e `M1` —, medindo em **tres pontos no tempo**: os **6 indices `M3`** que a medicao original declarou **continuam sendo 6, e ela acertou**; o que **nunca fora contado** — artefatos `M1`/historico que passariam a citar decisao superada, **nao corrigiveis** — foi de **4 para 12**, **triplicou em duas missoes** e **cresce a cada `ADR`, `FIT`, `PT` ou `MEM` que o cite**. **Isso nao reclassifica nada:** `Tipo 2` segue correto porque **`0` artefatos normativos migram; o que deixa de ser verdade e que a reversao seja *limpa***, e a distincao so aparece **remedindo, nao relendo** — achado **`RD-48`**. **§2 assinala em vez de simular:** os hashes de `ADR-0023` vivem em `PS-2026-010 §4.2`, **nao foram reproduzidos de memoria** e ficam marcados para conferencia contra a fonte na aplicacao (`PJ-03`, `LV-12`, `PI-10`). **A minuta de §6 resolve expressamente `Q1` e `Q3` de `PS-2026-009 §9.1`** — `ADR-0022` **`Tipo 1`** e `superado_por` **NAO** gravado em `ADR-0021` — e declara, em **seis** itens, o que o ato faz, e em **dois**, o que ele **nao** faz. **`0` objetos novos · `0` diffs novos · `0` hashes novos · `0` objetos em vigor.** |
