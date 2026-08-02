---
id: PS-2026-017
titulo: Pacote de decisao soberana — emenda C3 que sana RD-91, separando proponente de aprovador na Spec C1
tipo: relatorio
versao: 1.1.0
status: ativo
camada_memoria: operacional
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-08-02
atualizado_em: 2026-08-02
revisao_prevista: null
decisoes_relacionadas: [ADR-0019, ADR-0021, ADR-0022, ADR-0031, ADR-0032]
substitui: []
substituido_por: null
canal: REPORTE
emissor: DEP-GOV
destinatario: SOBERANO
ttl: ate decisao do Soberano
resumo: Submete ao Soberano a emenda C3 que faz DEP-EXE aprovar Spec C1, com diff literal, hashes integrais dos quatro candidatos, os tres numeros de custo e a minuta do ato. Em 1.1.0 as tres questoes do paragrafo 7 estao respondidas por despacho, a minuta foi reemitida com item VIII para Q3 e os quatro H-P reconferidos — e segue nao emitida.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
---

# PS-2026-017 — Emenda **C3** que sana `RD-91`

> ## Este pacote **informa**. Nao decide, nao aprova, nao promulga e nao edita nada.
>
> **`FND-09` permanece em `1.5.0`, `FND-11` em `1.0.0`, as Cartas de `DEP-PRD` e `DEP-EXE` em
> `1.1.0`.** Os candidatos `1.6.0`, `1.1.0`, `1.2.0` e `1.2.0` existem como **diff literal +
> hash**, **fora do acervo**, em
> `_candidatos-LucaX-Enterprise-OS-2026-08-02-M1.13.5.1/`.
>
> **`0` bytes foram escritos nos quatro arquivos vivos.** Conferido por `sha256` arquivo a
> arquivo em §3, e **reconferido apos o despacho** em §3.2.
>
> **Caminho exato:** `governance/pacote-soberano-2026-08-02-rd-91.md` *(RE-01)*.

> ## `1.1.0` — despacho do Soberano de 2026-08-02: as tres questoes de §7, RESPONDIDAS
>
> **`Q1`** ESTENDE a `PRJ` e `TPL`, com missao propria ordenada · **`Q2`** `C0` PERMANECE
> declarado em `RD-91` · **`Q3`** prevalece a PRATICA EXERCIDA, incremento **MENOR**.
>
> A minuta de §6 foi **reemitida** com **as tres caixas marcadas** e com o **item VIII**, que
> da a `Q3` casa de decisao propria — sem ele, o ato decidiria `Q3` **em silencio**, pelos
> numeros de versao do item I, que e exatamente o que §7 recusou fazer.
>
> **A minuta continua NAO EMITIDA, NAO assinada e NAO aplicada. Congelamento em vigor.** O
> que muda de `1.0.0` para `1.1.0` esta listado, linha a linha, em **§9**.

## Proposito

Levar ao Soberano a emenda que sana **`RD-91`** — a colisao que torna **nula** (`LV-03`) a
aprovacao de **toda** `Spec` de classe `C1` e, com isso, **inutilizavel** o piso que
`FND-04 §6` fixa. A decisao e dele por construcao: **`FND` nao vigora sem ratificacao**
(`LM-02`; `FND-09 §8.2`, linha `FND`; `SF-32`), e **duas Cartas ratificadas** so se emendam
por ato.

## 1. O que se pede, em uma frase

> **Aprovar e ratificar [ADR-0032](../decisions/ADR-0032-separacao-de-proponente-e-aprovador-na-spec-c1.md),
> promulgando quatro versoes: `FND-09` 1.6.0, `FND-11` 1.1.0, Carta `DEP-PRD` 1.2.0 e Carta
> `DEP-EXE` 1.2.0** — de modo que a aprovacao de `Spec` `C1` passe do **proprietario**, que e
> quem a propoe, para **DEP-EXE**, que nao a propoe.

## 1.1 Os tres numeros de custo — medidos, em destaque

| # | Pergunta | Resposta | Como se apurou |
|---|---|---|---|
| **1** | Quanto custou a **primeira** `Spec`, em `C2` | ## **5 artefatos** *(1.580 linhas)* | `wc -l` em 2026-08-02: `RFC-0026` **197** · `ADR-0031` **271** · `SPC-001` **603** · `FIT-2026-024` **211** · `PT-2026-017` **298** |
| **2** | Quanto custara a **segunda**, em `C1`, **depois** desta emenda | ## **2 artefatos** *(Nota de Decisao + a `Spec`)* — **3** contando o registro de missao | **Derivado de norma, nao medido:** `FND-07 §2.3` da `C1 · Tipo 2` = **Nota de Decisao**; `SF-24` item (9) so exige `FIT` em `C2`/`C3`; `FND-04 §2` nao exige `RFC` nem `ADR` em `C1` |
| **3** | Quanto custa **esta emenda** | ## **7 artefatos** *(+ 4 documentos emendados)* | `RFC-0027` · `ADR-0032` · `FIT-2026-025` · **este pacote** · `PT-2026-018` · **o ato (`MSG`)** · o `PT` da aplicacao. Medido na cadeia identica de `PS-2026-008` → `MSG-2026-0006` |

> **A economia se paga na segunda `Spec` e sobra a partir da terceira.** Emenda: **7**,
> uma vez. Cada `Spec` que deixa de subir a `C2`: **3 a menos**. **`CE-04` respeitado:** o
> numero **1** e medicao; os numeros **2** e **3** sao **derivacao de norma e de precedente**,
> e estao declarados como tal — nenhuma linha foi estimada.

## 2. Diff literal

### 2.1 `FND-09` — §8.2, linha `SPC`, coluna *Aprova* *(a fonte)*

**Antes** *(linha 900)*:
```
| SPC | DEP-PRD | DEP-ENG + DEP-QAR | conforme classe (FND-04 §2) | SOBERANO se C3 ou Tipo 1 | DEP-PRD |
```

**Depois**:
```
| SPC | DEP-PRD | DEP-ENG + DEP-QAR | conforme classe (FND-04 §2); em **C1**, **DEP-EXE** | SOBERANO se C3 ou Tipo 1 | DEP-PRD |
```

**Nota acrescentada** *(apos as notas existentes de §8.2, antes de §8.3 — 14 linhas)*:
```
> **Sobre a linha `SPC`, coluna *Aprova*, em `C1`.** Esta celula **nao redefine FND-04 §2**:
> ela **aplica FND-04 §3.1** ao unico caso em que a propria matriz torna o default de §2
> impossivel. Para `SPC`, esta tabela poe **DEP-PRD** como quem **propoe/cria** e como quem
> **aposenta** — logo, proprietario —, e `FND-04 §2` atribui a aprovacao `C1` ao
> **proprietario**. As duas leituras juntas produzem `Proponente = Aprovador`, que
> `FND-04 §3.1` declara **nula** por **`LV-03`**, Linha Vermelha de `FND-01`, **nivel 1** da
> hierarquia normativa. **Entre um default de §2 e uma incompatibilidade absoluta de §3.1,
> prevalece a incompatibilidade** — e o aprovador passa a ser o titular que `FND-04 §2` ja
> nomeia no degrau seguinte: **DEP-EXE**. **Nenhum titular foi ampliado:** `DEP-EXE` ja
> aprova `Spec` `C2` na mesma linha desta tabela. **A classe NAO muda:** `C1` continua `C1`,
> com **Nota de Decisao** como instrumento (`FND-04 §2`, `FND-07 §2.3`), **sem** `RFC`,
> **sem** `ADR`, **sem** `FIT` e **sem** ratificacao. **`C0` NAO e alcancado por esta emenda,
> e o colapso de `C0` permanece declarado** em `RD-91`.
```

**Frontmatter:** `versao` 1.5.0 → **1.6.0** · `atualizado_em` → **2026-08-02** ·
`decisoes_relacionadas` **+ ADR-0032** · `status` → `aprovado` · `ratificacao` → `pendente`
*(os dois ultimos voltam a `ativo`/`ratificada` **pelo ato** — e o que `H-P` projeta em §3)*.
**Mais 1 linha de historico.**

**Total: 6 blocos de diff. `0` fora deles.**

### 2.2 `FND-11` — §5, matriz de `SF-10`, celula *Aprovacao* × `C1 · T2` *(cascata)*

**Antes** *(linha 260)*:
```
| **Aprovacao** | proprietario | proprietario **+ revisor** | **DEP-EXE** + parecer **DEP-GOV** | **DEP-EXE** propoe | **SOBERANO**, indelegavel |
```

**Depois**:
```
| **Aprovacao** | proprietario | **DEP-EXE** + revisor | **DEP-EXE** + parecer **DEP-GOV** | **DEP-EXE** propoe | **SOBERANO**, indelegavel |
```

**Declaracao `PJ-02` de §5, linha *Fonte*** — acrescenta **`§3.1`**:
```
> **Fonte:** `FND-04 §2`, `§2.1`, `§2.2`, **`§3.1`**, `§6` · `FND-07 §2.3`, `§2.4`, `§5` · `FND-09 §8.2`
```

**Linha de §2.2, regra `SF-10`** — passa a datar a equivalencia:
```
| **SF-10** | §5.3 | `T-IDENTICA` **na recepcao de `1.0.0`** — inclusive a matriz de **50 celulas** e a declaracao `PJ-02` que a governa. **`1.1.0` emendou 1 celula da matriz** *(linha Aprovacao × coluna `C1 · T2`)*, por `ADR-0032` | **Integral na recepcao.** A divergencia posterior e **declarada** em §2 e no historico, nunca silenciosa |
```

**Nota de alcance temporal em §2** *(11 linhas)* — declara que a matriz passa a diferir em
**1** celula da copia de `ADR-0021 §5.3`, artefato `M1` que nunca se emenda, e que **prevalece
`FND-11`** por `ADR-0022 §5.4`. Achado `RD-98`.

**Frontmatter:** `versao` 1.0.0 → **1.1.0**, mesmos cinco campos. **Mais 1 linha de historico.**

**Total: 8 blocos de diff. `0` celulas da matriz alteradas alem de uma.**

### 2.3 Carta de `DEP-PRD` — 4 linhas *(propagacao obrigatoria, `CV-04`)*

| § | Antes | Depois |
|---|---|---|
| **§4** *(o que NAO me compete)*, L126 | *"Aprovar a Spec de classe **`C2` ou `C3`** que eu escrevo"* | *"Aprovar a Spec de classe **`C1`, `C2` ou `C3`** que eu escrevo"* — e `DEP-EXE` cobre `C1` e `C2` |
| **§5** *(o que decido)*, L138 | *"**Aprovar Spec** (`SPC`) **de classe `C0` ou `C1`**, como proprietario"* · *"`C2` aprova DEP-EXE; `C3`, o SOBERANO"* | *"**Aprovar Spec** (`SPC`) **de classe `C0`**, como proprietario"* · *"**`C1` aprova DEP-EXE** (pos-`ADR-0032`: sou o proponente de toda `Spec`, e `FND-04 §3.1` veda `Proponente = Aprovador`); `C2` aprova DEP-EXE; `C3`, o SOBERANO"* |
| **§5.1** *(o que NAO decido)*, L153 | *"Aprovar Spec **`C2` ou `C3`**"* | *"Aprovar Spec **`C1`, `C2` ou `C3`**"* |
| **§7** *(artefatos mantidos)*, L224 | *"aprovador **apenas quando a classe do efeito for `C0` ou `C1`**"* | *"aprovador **apenas quando a classe do efeito for `C0`**"* |

### 2.4 Carta de `DEP-EXE` — 2 linhas

| § | Antes | Depois |
|---|---|---|
| **§5** *(o que decido)*, L158 | *"**Aprovar Spec** (`SPC`) **quando a classe do efeito for `C2`**"* · *"**`C0`/`C1`: o proprietario.** `C3`: SOBERANO"* | *"**Aprovar Spec** (`SPC`) **quando a classe do efeito for `C1` ou `C2`**"* · *"**`C0`: o proprietario.** `C3`: SOBERANO"* — parecer de DEP-GOV **so em `C2`** |
| **§7** *(artefatos mantidos)*, L260 | *"aprovador **quando a classe do efeito for `C2`**"* | *"aprovador **quando a classe do efeito for `C1` ou `C2`**"* |

> **`0` linhas de historico editadas nas duas Cartas.** A linha `1.1.0` de `DEP-PRD` conserva
> *"segue aprovando Spec `C0` e `C1`"* — **verdadeira quando escrita**, e agora **superada por
> versao**, nunca reescrita (`AC-10`, `LV-04`). Historico nao se corrige: se supera.

## 3. Identificadores de integridade

**Instrumento:** `hashes.sh` — `H-A` = `sha256` do arquivo submetido (`IR-07`); `H-N` =
`sha256` com as linhas de `IR-03` removidas **so dentro do frontmatter** (`IR-02`); `H-P` =
`sha256` projetado **apos** a transicao `O4` que o ato realiza (`status: aprovado → ativo`,
`ratificacao: pendente → ratificada`).

| Objeto | Estado | Linhas | `H-A` | `H-N` |
|---|---|---|---|---|
| **`FND-09`** | **VIGENTE 1.5.0** | 1.263 | `191ff367eead695b4a1c2622ea20dfb89d47c40bfe2d5945286bf99e7bbd1952` | `052a948a159babe6a83fbd44763ce13774ee3195792bf738352909762212edcf` |
| **`FND-09`** | **CANDIDATO 1.6.0** | 1.278 | `defdf5b8e815ce1e6d76ae453348726625e42b13b4a3c523ffce8eed247e6c6c` | `eee41dfcf2147ab81ab1a477d6bdf0e91bc67f3310a9ca59c7248597386dbaf3` |
| **`FND-11`** | **VIGENTE 1.0.0** | 399 | `383ee51df8ee8782a693897f07423529bc4dd5a7d866603ad31e61fe06ad7c20` | `90f4efb74e2d2573e9f4fdf69db43e3da863f3b1e09926febe22517f32ca79ee` |
| **`FND-11`** | **CANDIDATO 1.1.0** | 411 | `efa9e10959a095fc51c327bf553ee6171bff6b8ef7c94c8c92ce953599fce373` | `7b1ff33aeea2f0dc7a70247783d9290e86db7a1643971c1bdeebc590a3985f47` |
| **`DEP-PRD`** | **VIGENTE 1.1.0** | 445 | `0e98511630faf9d5bec4c7cb36d8a37fa0bf15506dfde36954f0419e2720fc15` | `ce3490049a57e6c141a40a07bcb7da1881b0389c4fe8134b359c7bf406d40279` |
| **`DEP-PRD`** | **CANDIDATO 1.2.0** | 446 | `abf2ddfd70692833b92ace28b3b0a64f6da8b853263fad07aa93f533cb50ea9e` | `10f2ae9fc8f261f697006bc6c9478964a96627e14a2174b37f21ca6ab7025237` |
| **`DEP-EXE`** | **VIGENTE 1.1.0** | 506 | `a75a1ffea140e1f962e97b5b8772df70cf28831df882a25cf804b4e931f17e12` | `537eb9f474dcc6e778c911d3abbe5cc9e4a84ec79914cf2aadb15d6aa929aab6` |
| **`DEP-EXE`** | **CANDIDATO 1.2.0** | 507 | `087fc63454e617c37c688f2d6391b880db3cdcd7538475c1a87afbe8c0c531b3` | `a191fb9e86bb6518f0935ec7203861ae61701d7f632632ed23a5edb40daaa192` |

### 3.1 `H-P` — o valor que o arquivo tera **depois** do ato

| Objeto | `H-P` *(projetado)* |
|---|---|
| **`FND-09` 1.6.0** | `ea5efd35249c12f9587b7ded68a72d165a14b4adf399fdb2f9dc09dad395a8db` |
| **`FND-11` 1.1.0** | `b2cff9f59e9f0d47034f02322d32438552d122c867ae0e954bb30fc42cd16e08` |
| **`DEP-PRD` 1.2.0** | `b9ac470c9227dd5bc4445d96faf1ff6b1d67c2d6f40ea6d0fd8a4f37180babdd` |
| **`DEP-EXE` 1.2.0** | `a07c765a9134b3f4caad76b2750c38beff53b6f7f2e8659717c42c881c9619e4` |

> **Para que serve o `H-P`.** A missao que aplicar o ato **tem de reproduzir estes quatro
> valores** depois de mover `status` e `ratificacao`. Se nao reproduzir, alguma coisa alem da
> transicao `O4` foi tocada, e a aplicacao **para**. **A transicao fica testavel antes de
> ocorrer.**

### 3.2 Reconferencia dos quatro `H-P` — ordenada pelo despacho, executada antes da devolucao

**Instante da medicao:** `2026-08-02 10:40:11 -03:00`. **Instante, e nao data** — os candidatos
vivem **fora do acervo**, em arvore que pode mudar dentro da propria missao, e a data sozinha
nao ancora nada.

**Instrumento:** `hashes.sh`, `sha256` = `729cafadee7fd10ec218216919e585dc2ac90315a2b5cb4fd9322a85fc8487ec`,
recuperado de `_arquivo/missoes-encerradas/_missao-1-13-5-2026-08-01/ferramentas/`. **Nao foi
reescrito nem reimplementado:** e o mesmo binario de texto que produziu os valores de §3.
**Controle positivo antes do uso** — o instrumento rodou sobre **si proprio** e devolveu o
proprio `sha256`, provando que `ha()` mede o que diz medir e que um `0` posterior nao seria
`0` de instrumento morto.

| Objeto | `H-P` **publicado em §3.1** | `H-P` **reconferido em 2026-08-02 10:40** | |
|---|---|---|---|
| **`FND-09` 1.6.0** | `ea5efd35…a8db` | `ea5efd35249c12f9587b7ded68a72d165a14b4adf399fdb2f9dc09dad395a8db` | ✅ **reproduz** |
| **`FND-11` 1.1.0** | `b2cff9f5…6e08` | `b2cff9f59e9f0d47034f02322d32438552d122c867ae0e954bb30fc42cd16e08` | ✅ **reproduz** |
| **`DEP-PRD` 1.2.0** | `b9ac470c…abdd` | `b9ac470c9227dd5bc4445d96faf1ff6b1d67c2d6f40ea6d0fd8a4f37180babdd` | ✅ **reproduz** |
| **`DEP-EXE` 1.2.0** | `a07c765a…19e4` | `a07c765a9134b3f4caad76b2750c38beff53b6f7f2e8659717c42c881c9619e4` | ✅ **reproduz** |

**`4` de `4` reproduzem.** Reconferidos tambem, no mesmo instante e pelo mesmo instrumento, os
**`8`** `H-A`/`H-N` de §3 e os **`4`** `H-A` dos arquivos vigentes: **`12` de `12` reproduzem**
— os quatro arquivos vivos **continuam intocados**, e o `H-P` continua sendo a projecao dos
candidatos que §3 publica.

**Prova de que a projecao `O4` alcanca exatamente dois campos, e nao mais.** O `diff` entre
cada candidato e a sua projecao foi tomado objeto a objeto: **`2` linhas alteradas em cada um
dos quatro** — `status: aprovado → ativo` e `ratificacao: pendente → ratificada`. **`0` linhas
de corpo, `0` linhas de historico, `atualizado_em` nao tocado.** Os quatro candidatos estao,
de fato, em `status: aprovado` **com** `ratificacao: pendente` — sem isso a projecao seria
identidade, e o `H-P` valeria `H-A` sem que nada avisasse.

> ### ⚠️ Divergencia encontrada na reconferencia — na EVIDENCIA, nunca no pacote
>
> `_missao-1-13-5-1-2026-08-02/evidencia/hashes-candidatos.txt`, citado por
> [`PT-2026-018`](relatorio-transicao-2026-08-02-emenda-sf-10.md) como a tabela de hashes da
> missao, **nao reproduz para as duas Cartas**: registra `H-A` `20fd1450…d2ed` / `H-P`
> `a0e23d60…9228` para `DEP-PRD` e `H-A` `7d00d46b…9bbe` / `H-P` `eb35d890…b9db` para
> `DEP-EXE` — **`6` valores divergentes de `24`**. `FND-09` e `FND-11` reproduzem nos dois
> lugares.
>
> **A causa esta medida, nao suposta.** `hashes-candidatos.txt` foi escrito as **01:31:14**;
> `DEP-PRD-carta-1.2.0.md` e `DEP-EXE-carta-1.2.0.md` foram modificados as **01:39:33** —
> **oito minutos depois**. `FND-09` *(01:28:04)* e `FND-11` *(01:29:16)* sao anteriores ao
> arquivo de evidencia, e por isso batem. **Divergem exatamente os dois arquivos tocados
> depois do instantaneo, e so eles.**
>
> **Quem esta certo e o pacote.** §3 e §3.1 carregam os valores dos arquivos que existem
> agora, e a reconferencia acima os reproduz um a um; o que ficou para tras foi a evidencia,
> que **nunca foi reemitida**. **`0` linhas de `PS-2026-017` estavam erradas** — e os seis
> valores das Cartas **so existem neste pacote**: nao aparecem em `ADR-0032`, `RFC-0027`,
> `FIT-2026-025`, `PT-2026-018` nem no catalogo mestre, de modo que **nenhum artefato do
> acervo propaga o valor superado**.
>
> **Efeito sobre o ato: nenhum.** O item VI manda reproduzir os `H-P` **do item I**, que sao
> os de §3.1. **Efeito sobre quem aplicar: existe, e e por isto que fica escrito** — quem
> conferir pela evidencia da missao, e nao pelo pacote, obtera `2` de `4` falhando e **parara
> uma aplicacao correta**. **Candidato a achado `RD-101`, severidade Baixa, dono DEP-GOV,
> gatilho *"aplicacao do ato"*. NAO registrado: registrar e ato de catalogo, e o congelamento
> esta em vigor** — entra por decisao do Soberano, junto com a aplicacao do item VI.

## 4. Rollback por objeto

| Objeto | Ponto de retorno exato |
|---|---|
| `FND-09` | `H-A` vigente `191ff367…1952` — o arquivo **nao foi tocado** |
| `FND-11` | `H-A` vigente `383ee51d…7c20` — idem |
| `DEP-PRD` | `H-A` vigente `0e985116…fc15` — idem |
| `DEP-EXE` | `H-A` vigente `a75a1ffe…7e12` — idem |
| Acervo inteiro | `H-A` integral de **602** arquivos em `_missao-1-13-5-1-2026-08-02/evidencia/H-A-rollback-pre-escrita.txt`, `sha256` = `a44370df7931e8963e8cd585c5c2cec5cfa9a3dd3325ba70589fc49d49084538`; copia datada em `_backups/LucaX-Enterprise-OS_2026-08-02_pre-instrumentos-1-13-5-1` |

**Antes do ato o rollback e trivial: basta nao emitir.** Depois do ato, e **emenda revogatoria
de mesmo rito** (`FND-04 §2`, C3).

> ### ⚠️ O rollback do acervo inteiro MUDOU DE LUGAR — conferido em `2026-08-02 10:42`
>
> **Os dados estao integros; o caminho publicado acima esta errado.** A copia datada
> `LucaX-Enterprise-OS_2026-08-02_pre-instrumentos-1-13-5-1` **nao esta mais em `_backups/`**:
> foi movida, junto com **todas** as demais copias datadas do acervo, para
> **`_to_delete/_backups/`** — por processo de manutencao externo a esta missao, durante a
> propria sessao que reemitiu esta minuta.
>
> **Integridade conferida, e ela reproduz:** a copia tem **602** arquivos, exatamente os `602`
> declarados; e `H-A-rollback-pre-escrita.txt` tem **602** linhas e `sha256`
> `a44370df7931e8963e8cd585c5c2cec5cfa9a3dd3325ba70589fc49d49084538` — **igual ao publicado**.
> **`0` bytes perdidos ate aqui.**
>
> **Por que isto importa para o ato, e nao so para a arrumacao.** Este pacote declara aquela
> copia como **ponto de retorno do acervo inteiro** de um ato `C3` cuja reversao, depois de
> emitido, e **emenda revogatoria de mesmo rito**. Um diretorio chamado `_to_delete` **nao e
> lugar de rollback declarado de ato soberano**: basta que alguem o esvazie para que a linha
> acima passe a apontar para o vazio, e ninguem seria avisado.
>
> **O caminho publicado NAO foi reescrito de proposito.** `_to_delete/` e local **transitorio**;
> gravar um caminho transitorio dentro de um ato assinado trocaria um defeito por outro pior.
> **A decisao e do Soberano** — restaurar `_backups/`, ou fixar outra sede e reemitir esta
> linha antes da assinatura. **Enquanto nao decidir, a copia permanece onde esta, e este
> paragrafo e o aviso.**
>
> **Copia datada desta sessao:** `_backups/LucaX-Enterprise-OS_2026-08-02_pos-reemissao-minuta-ps-2026-017`,
> **607** arquivos, tomada **depois** da reemissao — e **nao substitui** a copia pre-escrita
> acima, que e a unica anterior a missao.

## 5. Classe, aprovador e o que se pede

| Campo | Valor | Fundamento **citado**, nunca por analogia |
|---|---|---|
| Classe | **`C3`** | `FND-04 §2`, bloco `C3` — *"altera ... direitos de decisao ou a propria Fundacao"* |
| Tipo | **2** | `FND-04 §2`, bloco `C3`, campo *Reversao* — *"emenda revogatoria, com mesmo rito"* |
| Instrumento | **RFC → analise de impacto → ADR → ratificacao** | `FND-04 §2`, bloco `C3`; `FND-07 §2.3` |
| `FIT` | **obrigatorio** | `CC-04`, `CV-07`, `QG-6` — em `C2` e `C3` |
| Aprova | **SOBERANO**, indelegavel | `FND-04 §2`; `FND-09 §8.2`, linha `FND` |
| Ratifica | **SOBERANO** | `FND-09 §8.2`, linha `FND`; `LM-02`; `SF-32` |

## 6. Minuta do ato soberano — **reemitida `1.1.0`, e NAO emitida**

> **O que mudou de `1.0.0` para `1.1.0`:** as **tres caixas** que o despacho marcou *(item IV
> segunda, item V primeira, item VIII primeira)*, o **item VIII** que o despacho mandou
> acrescentar, os **fundamentos** do Soberano transcritos sob cada decisao, e a **reconciliacao
> do item VII**, que `1.0.0` deixava incompativel com a caixa marcada em IV. **Itens I, II, III
> e VI: `0` bytes alterados**, exceto a nota de reconferencia acrescida ao fim do item I.
> Lista linha a linha em **§9**.

```
ATO SOBERANO — EMENDA QUE SANA RD-91
Data: <a definir pelo SOBERANO>

I.   RATIFICO o ADR-0032, classe C3, tipo 2, e promulgo as quatro versoes abaixo,
     que entram em vigor na data deste ato:

     (a) FND-09 1.6.0   H-P esperado: ea5efd35249c12f9587b7ded68a72d165a14b4adf399fdb2f9dc09dad395a8db
     (b) FND-11 1.1.0   H-P esperado: b2cff9f59e9f0d47034f02322d32438552d122c867ae0e954bb30fc42cd16e08
     (c) Carta DEP-PRD 1.2.0  H-P esperado: b9ac470c9227dd5bc4445d96faf1ff6b1d67c2d6f40ea6d0fd8a4f37180babdd
     (d) Carta DEP-EXE 1.2.0  H-P esperado: a07c765a9134b3f4caad76b2750c38beff53b6f7f2e8659717c42c881c9619e4

     Os quatro H-P acima foram RECONFERIDOS em 2026-08-02 10:40, depois do
     despacho e antes desta devolucao, e os quatro reproduziram — junto com os
     8 H-A/H-N dos candidatos e os 4 H-A dos arquivos vigentes, 12 de 12.
     Medicao e instrumento em 3.2.

II.  DECLARO que a aprovacao de Spec de classe C1 passa a ser de DEP-EXE, e que
     isso NAO altera a classe C1, NAO cria titular e NAO toca regra de conteudo
     de Spec.

III. DECLARO que SPC-001 NAO e reclassificada: nasceu C2 - Tipo 2 validamente.

IV.  QUANTO A LARGURA — decido a questao Q1 de RFC-0027 §9:
     [ ] a emenda fica em SPC, e RD-96 (PRJ) e RD-97 (TPL) seguem abertos
     [X] estendo a emenda a PRJ e TPL, e ordeno missao propria para redigi-la
     [ ] outra: ______________________________________________

     FUNDAMENTO. TPL tem 19 objetos vivos no acervo contra 1 de SPC: o defeito
     com mais efeito real ficaria de fora. ACOLHO a ressalva S2 de FIT-2026-025
     contra a recomendacao de RFC-0027 §6 — emendar uma linha e deixar duas
     quebradas ao lado, com a solucao visivel duas linhas acima, convida a
     copia sem rito.

     ALCANCE DA MISSAO ORDENADA: FND-09 §8.2, linhas PRJ (RD-96) e TPL (RD-97),
     e o que delas cascatear. A missao REDIGE; nao aplica. Este ato NAO se
     estende com ela: os quatro objetos do item I continuam quatro, e os quatro
     H-P continuam os do item I. RD-96 e RD-97 seguem ABERTOS ate o ato proprio
     que os sanar.

V.   QUANTO A C0 - decido a questao Q2 de RFC-0027 §9:
     [X] C0 permanece declarado em RD-91, sem emenda
     [ ] ordeno sanar C0 no mesmo rito

     FUNDAMENTO. Sanar agora obriga reescrever os quatro candidatos e recalcular
     os quatro H-P, atrasando o conserto de C1, que custa 3 artefatos por Spec.
     C0 so ocorre em Spec ja viva, e existe 1 Spec. O risco real e pequeno.

     RD-91 FECHA PARCIALMENTE por este ato: fecha quanto a C1 e PERMANECE ABERTO
     quanto a C0 - T2, com o alcance ja declarado no proprio achado.

VI.  A aplicacao e MINISTERIAL e cabe a DEP-GOV: mover status e ratificacao dos
     quatro objetos, reproduzir os quatro H-P acima, atualizar o catalogo mestre
     e emitir baseline nova. Se qualquer H-P nao reproduzir, a aplicacao PARA.

VII. O congelamento permanece em vigor. Este ato gera EXATAMENTE duas frentes, e
     nenhuma outra: a aplicacao ministerial do item VI, e a missao propria
     ordenada no item IV, que NAO comeca antes de concluida e conferida a
     aplicacao do item VI.

VIII. QUANTO A VERSAO — decido a questao Q3 de RFC-0027 §9, achado RD-99:
     [X] prevalece a PRATICA EXERCIDA: incremento MENOR, por AL-01/CC-02, e os
         numeros do item I ficam como estao — FND-09 1.6.0, FND-11 1.1.0,
         Cartas DEP-PRD e DEP-EXE 1.2.0
     [ ] prevalece a letra de FND-04 §2, bloco C3: incremento MAIOR, e o item I
         e reescrito, com os quatro candidatos e os quatro H-P refeitos
     [ ] outra: ______________________________________________

     DECIDO POR DELIBERACAO, E NAO POR OMISSAO. Os numeros de versao do item I
     NAO decidem Q3 calando: quem decide Q3 e este item, e os numeros do item I
     sao consequencia dele. Sem este item, o ato decidiria Q3 em silencio —
     exatamente o que RFC-0027 §9 e PS-2026-017 §7 recusaram fazer.

     FUNDAMENTO. MAIOR obrigaria a reescrever os quatro candidatos, refazer os
     quatro H-P, e deixaria ADR-0017, ADR-0019, ADR-0022 e ADR-0024 etiquetados
     errado — inconsistencia maior que a corrigida.

     O QUE ESTE ITEM NAO DECIDE. O conflito DENTRO de FND-04 — §2, bloco C3,
     mandando "nova versao MAIOR do documento" contra AL-01/CC-02, que fazem a
     versao seguir o EFEITO — NAO e resolvido aqui, e este ato NAO emenda
     FND-04: 0 bytes. A divergencia permanece ABERTA em RD-99, dono DEP-GOV,
     com o MESMO gatilho de RD-18: proxima emenda a FND-04, que e a sede do
     conflito.
```

## 7. Questoes ao Soberano — **as tres, RESPONDIDAS por despacho de 2026-08-02**

| # | Questao | Por que so ele decide | **Decisao** |
|---|---|---|---|
| **`Q1`** | A emenda fica em **`SPC`**, ou alcanca **`PRJ`** e **`TPL`**, que tem o defeito identico? | **Largura muda o alcance da norma.** Medido: `PRJ` poe `DEP-EXE` propondo **e** aprovando; `TPL` poe `DEP-GOV` propondo, revisando **e** aprovando. `FIT-2026-025` ressalva `S2` registra a assimetria | **ESTENDE a `PRJ` e `TPL`**, com **missao propria** ordenada para redigir. **Segunda caixa** do item IV. `RD-96` e `RD-97` seguem **abertos** ate o ato proprio |
| **`Q2`** | **`C0 · T2`** colapsa pela identica razao. Sanar agora, ou manter declarado? | Escopo, e o piso de criacao e `C1` — `C0` so ocorre em `Spec` ja viva | **PERMANECE declarado** em `RD-91`, sem emenda. **Primeira caixa** do item V. `RD-91` fecha **so quanto a `C1`** |
| **`Q3`** | `FND-04 §2`, bloco `C3`, manda registrar *"nova versao **MAIOR** do documento"*, e as emendas `C3` ja exercidas produziram versao **MENOR**, por `AL-01`. Qual prevalece? | Conflito **dentro de `FND-04`**, achado `RD-99`. **Esta emenda seguiu a pratica exercida** *(MENOR)* e **declara a divergencia em vez de a resolver em silencio** | **PREVALECE A PRATICA EXERCIDA — MENOR.** **Primeira caixa** do **item VIII**, casa criada por este despacho. `RD-99` segue **aberto**, gatilho de `RD-18` |

> **Por que `Q3` ganhou item proprio, e nao so a marcacao de uma caixa.** `Q1` e `Q2` ja
> tinham casa na minuta `1.0.0`; **`Q3` nao tinha**. Um ato que promulgasse `1.6.0`, `1.1.0`,
> `1.2.0` e `1.2.0` **sem dizer por que** decidiria `Q3` **pelos numeros**, calando — e o §7
> de `1.0.0` existe precisamente porque a sessao **recusou** decidir `Q3` em silencio. **O
> defeito foi apontado pela propria sessao que redigiu a minuta**, e o despacho mandou
> corrigi-lo **antes da assinatura**. O item VIII e essa correcao.

> **`0` das tres respostas altera os quatro objetos do item I, os quatro candidatos ou os
> quatro `H-P`.** Conferido: `Q1` difere a largura para missao propria; `Q2` mantem o estado
> declarado; `Q3` ratifica os numeros de versao que os candidatos **ja carregam**. Por isso a
> reconferencia de §3.2 pode reproduzir os valores de §3.1 — **e reproduziu, `12` de `12`**.

## 8. Rastreabilidade — decisao → instrumento → minuta

| Elo | Artefato |
|---|---|
| Achado | **`RD-91`**, [artifact-registry §7](artifact-registry.md), item 115 · [PT-2026-017 §6.2](relatorio-transicao-2026-08-02-primeira-spec.md) |
| Pergunta | [RFC-0027](../rfcs/RFC-0027-separacao-de-proponente-e-aprovador-na-spec-c1.md) |
| Decisao | [ADR-0032](../decisions/ADR-0032-separacao-de-proponente-e-aprovador-na-spec-c1.md) |
| Aptidao | [FIT-2026-025](fitness/FIT-2026-025-emenda-de-sf-10.md) — `apto-com-ressalva`, 4 ressalvas |
| Candidatos | `_candidatos-LucaX-Enterprise-OS-2026-08-02-M1.13.5.1/` — **fora do acervo** |
| Minuta | §6 deste pacote |
| Registro de missao | [PT-2026-018](relatorio-transicao-2026-08-02-emenda-sf-10.md) |
| Despacho que respondeu §7 | SOBERANO, **2026-08-02** — reemissao da minuta em `1.1.0` |

## 9. O que `1.1.0` mudou, linha a linha — e o que deliberadamente NAO mudou

**Ordenado pelo despacho, e feito:**

| # | Onde | Mudanca |
|---|---|---|
| 1 | §6, item **IV** | **Segunda** caixa marcada `[X]` — *estendo a emenda a `PRJ` e `TPL`, e ordeno missao propria*. **Texto da caixa: `0` bytes alterados** |
| 2 | §6, item **V** | **Primeira** caixa marcada `[X]` — *`C0` permanece declarado em `RD-91`*. **Texto da caixa: `0` bytes alterados** |
| 3 | §6, item **VIII** | **Criado.** Casa de decisao propria para `Q3`, com tres caixas, a primeira marcada, mais a declaracao de que a escolha e **deliberada e nao por omissao** |
| 4 | §3.2 | **Criada.** Reconferencia dos quatro `H-P` com instante, instrumento, controle positivo e resultado |

**Nao ordenado, e feito assim mesmo — declarado aqui para ser conferido ou riscado:**

| # | Onde | Mudanca | Por que |
|---|---|---|---|
| 5 | §6, item **VII** | Reescrito. `1.0.0` dizia *"este ato NAO gera missao alem da aplicacao ministerial do item VI"*; `1.1.0` diz **duas frentes** — a aplicacao do item VI e a missao ordenada no item IV, nesta ordem | **A caixa marcada em IV ordena uma missao.** Com o item VII de `1.0.0` intacto, o ato **ordenaria e proibiria a mesma missao, em dois itens**. Nao ha como marcar a segunda caixa de IV e conservar VII como estava |
| 6 | §6, itens **IV** e **V** | Acrescido, sob cada caixa marcada, o **FUNDAMENTO** do despacho, e o **alcance** do que foi decidido | O despacho **fundamentou** as tres escolhas. Minuta que registra a decisao e descarta o fundamento **perde o motivo**, e o motivo e o que impede a releitura errada depois |
| 7 | §6, item **I** | Acrescida ao fim a nota de que os quatro `H-P` foram **reconferidos** e reproduziram | O despacho pediu a devolucao *"com os quatro `H-P` reconferidos"*. **Nenhum valor foi alterado** |
| 8 | §4 | Acrescida a nota de que a copia datada citada como **rollback do acervo inteiro** foi movida para `_to_delete/_backups/` por manutencao externa, durante esta sessao. **Caminho publicado NAO reescrito** | Descoberto ao conferir o rollback. **Dados integros — `602` arquivos e `sha256` do `H-A` integral reproduzem** —, mas a sede virou transitoria. Reescrever para `_to_delete/` gravaria caminho transitorio em ato assinado. **Decisao do Soberano** |

> **Os itens 5, 6, 7 e 8 sao acrescimo desta sessao, nao palavra do Soberano.** Ficam
> **listados em separado** para que sejam riscados na assinatura, se ele quiser. **O item 5 e
> o unico cuja remocao pura deixa o ato incoerente** — se for para riscar, a caixa de IV
> tambem muda.

**Deliberadamente NAO mudado:**

| O que | Por que |
|---|---|
| Os **4** candidatos, fora do acervo | **`0` bytes.** Nenhuma das tres respostas os alcanca — conferido em §7. `H-A` reconferidos em §3.2 |
| Os **4** `H-P` de §3.1 | **`0` bytes.** Reproduzem em `2026-08-02 10:40` |
| Os **4** arquivos vivos — `FND-09`, `FND-11`, as duas Cartas | **`0` bytes.** `H-A` vigentes reconferidos em §3.2 |
| §1, §1.1, §2, §3, §4, §5, §8 | **`0` bytes.** A emenda alcanca frontmatter, cabecalho, §3.2 *(nova)*, §6, §7, §9 *(nova)* e historico |
| `artifact-registry.md` — a linha de `PS-2026-017` diz **276** linhas e *"3 questoes ao Soberano"* | **Ficou desatualizada, e fica declarado.** Reconciliar catalogo mestre e baseline e a **aplicacao ministerial do item VI**, que so corre **depois** do ato. Emitir baseline agora produziria baseline que a propria aplicacao superaria em seguida |
| `RD-101` — a evidencia de missao que nao reproduz *(§3.2)* | **Nao registrado. Registrar e ato de catalogo, e o congelamento esta em vigor.** Entra pela decisao do Soberano, com a aplicacao do item VI |
| `ADR-0032`, `RFC-0027`, `FIT-2026-025`, `PT-2026-018` | **`0` bytes.** O despacho nao os alcanca: `Q1`, `Q2` e `Q3` sao questoes **da minuta**, e a minuta mora aqui |

---

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.1.0 | 2026-08-02 | DEP-GOV | **Despacho do Soberano: as tres questoes de §7, RESPONDIDAS, e a minuta REEMITIDA — ANTES da assinatura.** **`Q1`** ESTENDE a `PRJ` e `TPL`, com **missao propria** ordenada *(segunda caixa do item IV)*, acolhendo a ressalva **`S2`** de `FIT-2026-025` **contra** a recomendacao de `RFC-0027 §6`: `TPL` tem **19** objetos vivos contra **1** de `SPC`, e o defeito com mais efeito real ficaria de fora. **`Q2`** `C0` PERMANECE declarado em `RD-91` *(primeira caixa do item V)*: sanar agora obrigaria reescrever os quatro candidatos e refazer os quatro `H-P`. **`Q3`** prevalece a **PRATICA EXERCIDA — incremento MENOR**, e para isso §6 recebe o **item VIII**, casa de decisao que `1.0.0` nao tinha: sem ele o ato decidiria `Q3` **pelos numeros de versao do item I, em silencio** — que e exatamente o que §7 recusou fazer. **O defeito foi apontado pela propria sessao que redigiu a minuta.** §3.2 nova: os **`4`** `H-P` **RECONFERIDOS** em `2026-08-02 10:40` com o mesmo instrumento *(`sha256` `729cafad…87ec`, com controle positivo sobre si antes do uso)* — **`4` de `4` reproduzem**, e com os `H-A`/`H-N` dos candidatos e os `H-A` dos vigentes, **`12` de `12`**; a projecao `O4` provada alcancar **`2`** linhas por objeto, nem uma a mais. **Divergencia encontrada e declarada, na EVIDENCIA e nunca no pacote:** `hashes-candidatos.txt` da missao **nao reproduz** para as duas Cartas — **`6`** valores de **`24`** —, porque foi escrito as **01:31:14** e os dois arquivos foram tocados as **01:39:33**; os seis valores superados **so existem fora do acervo**, e nenhum artefato os propaga. Candidato a **`RD-101`**, **nao registrado** por congelamento. **Segunda divergencia declarada, em §4:** a copia datada citada como **rollback do acervo inteiro** foi movida para **`_to_delete/_backups/`** por manutencao externa **durante esta sessao** — **dados integros**, `602` arquivos e `sha256` do `H-A` integral **reproduzindo**, mas a sede de rollback de um ato `C3` passou a ser um diretorio marcado para exclusao. **Caminho publicado NAO reescrito**, por ser `_to_delete/` transitorio; decisao do Soberano antes da assinatura. §7 passa de *questoes* a *questoes respondidas*; §9 nova lista **linha a linha** o que mudou, **separando o que o despacho ordenou do que esta sessao acrescentou** — o item **VII** reconciliado, os **fundamentos** transcritos e a nota de reconferencia do item I —, para que sejam riscados na assinatura se ele quiser. **`0` bytes nos 4 candidatos · `0` nos 4 arquivos vivos · `0` nos quatro `H-P` · `0` em `ADR-0032`, `RFC-0027`, `FIT-2026-025` e `PT-2026-018` · `0` no catalogo mestre · `0` baselines emitidas.** **A minuta continua NAO emitida, NAO assinada e NAO aplicada.** |
| 1.0.0 | 2026-08-02 | DEP-GOV | Criacao. Submete ao Soberano a emenda **`C3 · Tipo 2`** que sana **`RD-91`**: a aprovacao de `Spec` `C1` passa do **proprietario** — que e quem a propoe — para **DEP-EXE**. **4 objetos**, com `H-A`, `H-N` e `H-P` publicados: `FND-09` **1.6.0**, `FND-11` **1.1.0**, Cartas `DEP-PRD` e `DEP-EXE` **1.2.0**. **Diff literal e reversivel** em §2; **`0` bytes escritos nos arquivos vivos**, conferido por `sha256`. Traz os **tres numeros de custo** em §1.1: **5** *(medido)*, **2** *(derivado de norma)* e **7** *(medido no precedente `PS-2026-008`)*. §7 leva **tres questoes** que so o Soberano decide — a **largura** *(`PRJ` e `TPL` tem o defeito identico e ficam de fora)*, **`C0`**, e o conflito *versao MAIOR × `AL-01`* dentro de `FND-04`. Minuta do ato **redigida e NAO emitida**, com os quatro `H-P` como condicao de parada da aplicacao. |
