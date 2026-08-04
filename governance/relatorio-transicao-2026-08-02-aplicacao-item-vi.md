---
id: PT-2026-019
titulo: Missao 1.13.5.2 — aplicacao ministerial do item VI do decimo ato soberano
tipo: relatorio
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-08-02
atualizado_em: 2026-08-02
revisao_prevista: null
decisoes_relacionadas: [ADR-0012, ADR-0019, ADR-0020, ADR-0022, ADR-0032]
substitui: []
substituido_por: null
resumo: Registra o consumo do item VI de MSG-2026-0010 — o O4 dos quatro objetos com os quatro H-P reproduzidos, H-N invariante, IR-09 4 de 4, a reconciliacao de catalogo e indices na mesma mudanca, a inscricao de RD-104 e do fechamento parcial de RD-91, e a emissao de BL-2026-08-02-03.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# PT-2026-019 — Missao 1.13.5.2: aplicacao ministerial do item VI

> **Registro de missao. Nao e norma, nao institui nada e nao decide nada.**
> A aplicacao foi **MINISTERIAL** (`ADR-0020`, `PA-01`): executa o ato, **nao o interpreta**.
> O ato e [`MSG-2026-0010`](../memory/operacional/MSG-2026-0010-ato-soberano-emenda-que-sana-rd-91.md),
> ancorado no `H-A` de [`PS-2026-017`](pacote-soberano-2026-08-02-rd-91.md) **1.3.0**.

## 1. O que a missao fez — a ordem do item VI, na ordem

| # | Passo do item VI | Estado |
|---|---|---|
| 1 | Conferir os quatro `H-A` vivos, antes de tocar | ✅ **4 de 4** reproduzem §3 do ato |
| 2 | Mover `status` e `ratificacao` dos quatro objetos *(`O4`)* | ✅ **4 de 4** promulgados, **`+1`**: `ADR-0032`, que o item I **ratifica** — §5.1 |
| 3 | **Reproduzir os quatro `H-P`** — se um falhar, a aplicacao PARA | ✅ **4 de 4**, `0` incidentes |
| 4 | Reconciliar catalogo, indices, contadores e a divergencia de linhas | ✅ na **MESMA** mudanca |
| 5 | Inscrever **`RD-104`** no catalogo | ✅ item **127** de §7 |
| 6 | Emitir baseline nova, reproduzida em duas execucoes | ✅ **`BL-2026-08-02-03`** |

**Acrescentado pelo proprio ato**, [`MSG-2026-0010 §8`](../memory/operacional/MSG-2026-0010-ato-soberano-emenda-que-sana-rd-91.md)
passo 5: **inscrever o fechamento PARCIAL de `RD-91`** — ✅ feito, e **parcial** e literal:
fecha quanto a `C1` e **permanece ABERTO quanto a `C0 · T2`**, pelo item V.

## 2. Ponto de partida — medido por `H-A`, nunca lido de transcricao

**A ordem importa: medir e depois comparar.** Os quatro objetos foram medidos **antes** da
primeira escrita e reproduziram, nos 64 digitos, os valores que o ato publicou em §3.

| Objeto | Versao de partida | `H-A` medido | §3 do ato |
|---|---|---|---|
| `FND-09` | **1.5.0** | `191ff367…1952` | ✅ reproduz |
| `FND-11` | **1.0.0** | `383ee51d…f20` | ✅ reproduz |
| Carta `DEP-PRD` | **1.1.0** | `0e985116…fc15` | ✅ reproduz |
| Carta `DEP-EXE` | **1.1.0** | `a75a1ffe…7e12` | ✅ reproduz |

**Ancora do ato preservada.** `PS-2026-017` mede
`c48cf44323e4327c7cff3db1c96128e509107e2ec7b21e4ad187978d620c0298` — **`0` bytes**, e tinha de
ser `0`: tocar o pacote quebraria a propria ancora do ato que se estava aplicando.

## 3. A FONTE dos `H-P` — de onde os valores vieram, e de onde NAO vieram

> ⚠️ **`RD-101` e um portao, nao uma curiosidade.** `hashes-candidatos.txt` carrega **`6`
> valores superados de `24`** e faria **`2` de `4`** `H-P` falharem — **parando uma aplicacao
> correta**. **`0` valores desta missao vieram de la.**

| Sede lida | Metodo | Resultado |
|---|---|---|
| [`MSG-2026-0010 §4`](../memory/operacional/MSG-2026-0010-ato-soberano-emenda-que-sana-rd-91.md) | Leitura do **proprio arquivo** | **4** valores |
| [`PS-2026-017 §3.1`](pacote-soberano-2026-08-02-rd-91.md) *(sede independente)* | Leitura do **proprio arquivo** | **4** valores |
| Medicao nova sobre os candidatos | `sh hashes.sh hp <candidato>` | **4** valores |

**As tres concordam: `4` × `3` = `12` de `12`.** **`0` de transcricao, `0` de evidencia de
missao.** Os quatro literais foram ainda contados **dentro do pacote**: `5` ocorrencias cada.

## 4. Os quatro `H-P` — **reproduzidos ANTES de escrever no acervo**

**A transicao foi testada fora do acervo e so entrou depois de passar.** O `O4` foi aplicado
sobre os candidatos em arvore de trabalho **fora** do recurso, o `sha256` do resultado foi
conferido contra o `H-P` publicado, e **so entao** o arquivo entrou no acervo — onde foi
**remedido**. **A aplicacao nunca esteve num estado em que um `H-P` errado ja tivesse sido
gravado.**

| Objeto | Versao aplicada | `H-A` do aplicado = `H-P` publicado | Linhas |
|---|---|---|---|
| `FND-09` | **1.6.0** | `ea5efd35249c12f9587b7ded68a72d165a14b4adf399fdb2f9dc09dad395a8db` ✅ | **1.278** |
| `FND-11` | **1.1.0** | `b2cff9f59e9f0d47034f02322d32438552d122c867ae0e954bb30fc42cd16e08` ✅ | **411** |
| Carta `DEP-PRD` | **1.2.0** | `b9ac470c9227dd5bc4445d96faf1ff6b1d67c2d6f40ea6d0fd8a4f37180babdd` ✅ | **446** |
| Carta `DEP-EXE` | **1.2.0** | `a07c765a9134b3f4caad76b2750c38beff53b6f7f2e8659717c42c881c9619e4` ✅ | **507** |

**`4` de `4`. `0` paradas, `0` incidentes abertos.** As quatro contagens de linha reproduzem as
publicadas em `PS-2026-017 §3`. **`CR` = `0` bytes nos quatro**, contado por `tr`, nunca por
`grep`.

## 5. `H-N` invariante e `IR-09` — as duas provas de que so os dois campos se moveram

**`H-N` invariante NAO significa igual ao vigente anterior** — os quatro foram **emendados**, e
emenda muda conteudo normativo por construcao. Significa: **o `H-N` do arquivo aplicado e
identico ao `H-N` do candidato submetido**, de modo que a transicao `O4` **nao tocou uma unica
linha alem de `status` e `ratificacao`.**

| Objeto | `H-N` do candidato *(§3 do pacote)* | `H-N` do aplicado | |
|---|---|---|---|
| `FND-09` | `eee41dfc…baf3` | `eee41dfc…baf3` | ✅ invariante |
| `FND-11` | `7b1ff33a…5f47` | `7b1ff33a…5f47` | ✅ invariante |
| Carta `DEP-PRD` | `10f2ae9f…5237` | `10f2ae9f…5237` | ✅ invariante |
| Carta `DEP-EXE` | `a191fb9e…a192` | `a191fb9e…a192` | ✅ invariante |
| `ADR-0032` | `34949ee9…9acd` | `34949ee9…9acd` | ✅ invariante |

**`IR-09` — teste de reconstrucao**, de [`ADR-0012 §5.2`](../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md),
executado por **DEP-QAR**: desfeito o `O4` sobre o arquivo **aplicado**, o `sha256` reproduz o
`H-A` do **submetido**. **`4` de `4`** — `defdf5b8…6c6c`, `efa9e109…e373`, `abf2ddfd…ea9e` e
`087fc634…31b3`. **Falha abriria incidente por `IR-05`; nao houve falha.**

### 5.1 O quinto objeto — `ADR-0032`, que o item I RATIFICA e o item VI nao enumera

**O item I usa DOIS verbos e alcanca DOIS conjuntos:** *"RATIFICO o `ADR-0032`, classe C3, tipo
2, **e** promulgo as quatro versoes abaixo"*. O item VI enumera **as quatro versoes
promulgadas**; a ratificacao do `ADR` **e do item I**, e e ela que o `O4` de `ADR-0032`
executa — `aprovado` → `ativo`, `pendente` → `ratificada`.

**Nao move-lo seria produzir a contradicao que `RD-08` e `RD-30` nomeiam:** por
[`FND-10 §5.4`](../foundation/10-artifact-framework.md) **o frontmatter e a fonte corrente do
estado**, e um `ADR` ratificado pelo Soberano parado em `ratificacao: pendente` afirma sobre si
o contrario do ato que o alcanca. Promulgar e ativar sao **operacoes ministeriais** por
[`ADR-0020`](../decisions/ADR-0020-regime-ministerial-de-promulgacao-e-ativacao.md).

| Medida | Valor |
|---|---|
| `H-A` **antes** | `74650ef03f60b11e47b851fe6eaed7b161aea5a3c6310a101cc8a556377f48f9` |
| `H-P` **projetado** pelo instrumento, antes de escrever | `725ba83603293d84a579293a7bfe24993c26d09ca57ffcd8628896562963a95d` |
| `H-A` **depois** | `725ba83603293d84a579293a7bfe24993c26d09ca57ffcd8628896562963a95d` ✅ |
| `H-N` | `34949ee9…9acd` — **invariante** |
| Linhas | **227**, inalteradas |

⚠️ **`PS-2026-017` NAO publicou `H-P` para `ADR-0032`** — publicou para `4` dos `5` objetos que
o ato move. A ancora acima foi medida **nesta aplicacao**, e **ancora medida depois nao e
ancora: e reconstituicao**. Achado **`RD-106`**, §9.

## 6. A reconciliacao — na MESMA mudanca, como o item VI manda

| Onde | O que foi movido |
|---|---|
| `artifact-registry` §2 | *Artefatos*, *Linhas* e *Baseline vigente* — as tres linhas que estavam **desatualizadas por declaracao** desde `BL-2026-08-02-02`. O decimo ato passa de **EMITIDO** a **CONSUMIDO** |
| `artifact-registry` §2.2 | `FND-09` remedido — **1.263 → 1.278**; este catalogo remedido |
| `artifact-registry` §4.1 | `FND-09` **1.6.0 · 1.278** · `FND-11` **1.1.0 · 411** |
| `artifact-registry` §4.2 | `ADR-0032` passa a **`ativo` · `ratificada`**; a fila de retidos por falta de ato cai de **3** para **2** |
| `artifact-registry` §4.3.1 | `DEP-EXE` **1.2.0 · 507** · `DEP-PRD` **1.2.0 · 446** · subtotal **3.927** |
| `artifact-registry` §4.7 | Recebe **`PT-2026-019`** — este relatorio; **52** registros |
| `artifact-registry` §4, **todos os blocos** | **`229` alvos resolvidos um a um contra o disco: `0` orfaos e `15` contagens de linha corrigidas por ferramenta.** **`3`** foram agravadas por esta missao *(os tres indices que ela reconciliou)*; **`12`** ja estavam defasadas — a maior, `PS-2026-017`, por **622** linhas. Subtotal de §4.3.1 recontado: **3.925 → 3.971**, e **`44` das `46`** ja estavam la |
| `artifact-registry` §7 | **`RD-91` FECHA PARCIALMENTE** *(item 115)* · **`RD-104` INSCRITO** *(item 127)* · **`RD-105`** *(128)* e **`RD-106`** *(129)* abertos |
| `artifact-registry` §10 | **`BL-2026-08-02-03`** emitida; `BL-2026-08-02-02` demovida com os valores ORIGINAIS |
| `departments/README` | As duas Cartas a **1.2.0**, linhas **507** e **446**, subtotal **3.971**, e `C-9` remedida |
| `foundation/README` | `FND-11` a **1.1.0 · 411 linhas**, e `FND-09` a **1.6.0 · 1.278** |
| `decisions/README` | `ADR-0032` a **`ativo`** · **`ratificada`**, com o ato como fonte |
| `roadmap-canonico` | **1.13.5.2 assinalada**, na mesma sessao, sem rito |

**A divergencia de linhas acumulada desde `BL-2026-08-02-02` esta ATRIBUIDA, nao suposta** —
ver §7.

## 7. A divergencia de linhas, decomposta

| Etapa | Artefatos | Linhas |
|---|---|---|
| **`BL-2026-08-02-02`** — baseline vigente ao abrir | **228** | **67.279** |
| `+` escritas do decimo ato *(`MSG-2026-0010`, catalogo, roadmap)*, token 17 | **229** | **68.318** |
| `+` o `O4` desta missao — `+15`, `+12`, `+1`, `+1` | 229 | **68.347** |
| `+` reconciliacao e `PT-2026-019` | **230** | **68.797** |

**A diferenca entre a baseline vigente e o estado de partida NAO era erro de medicao:** eram as
escritas do proprio ato, feitas sob o token 17 e **deliberadamente nao publicadas como
baseline** — emitir baseline nova e do item VI, e o item VI e esta missao.

## 8. Baseline nova — `BL-2026-08-02-03`

| Medida | Valor |
|---|---|
| Instrumento | **`IR-BL/3`**, `sha256` `0d4f1b3d…4ad7`, conferido antes do uso |
| Execucoes | **2**, ambas `EXIT=0`, **apos a ultima escrita** |
| Artefatos | **230** |
| Linhas | **68.797** |
| Impressao digital | **`e4c307e0bbc9ea17de018bfe098c378436542a0b68102f019adc2af4fb71787a`** |

## 9. Achados novos — `2`, registrados com dono e gatilho, sem missao

### 9.1 `RD-105` — as duas Cartas declaram sobre si um numero que ja nao vale

**As duas Cartas promulgadas declaram, em `§13.2`, um numero de linhas que o proprio arquivo
ja nao tem:** `DEP-PRD` diz *"Carta integral — **445** linhas"* e tem **446**; `DEP-EXE` diz
**506** e tem **507**. O candidato ganhou a linha do historico de versoes e **`§13.2` nao foi
remedida junto**.

**NAO foi corrigido, e a razao e a mesma que o ato impoe:** `§13.2` vive **dentro de `H-N`** de
Carta agora ratificada, e corrigi-la **quebraria o `H-P` que o item VI manda reproduzir**.
Corrigir aqui seria mover o medidor para caber. **Familia de `RC-01` e `RD-49`** — *artefato que
declara sobre si um numero que ja nao vale*. Severidade **Baixa**, dono **DEP-EXE**, gatilho
*"proxima emenda a `DEP-PRD` ou `DEP-EXE`"*. **Congelamento respeitado: `0` missoes abertas.**

### 9.2 `RD-106` — o ato move `5` objetos e o pacote publicou `H-P` para `4`

**`ADR-0032` sofreu o mesmo `O4` sem valor projetado contra o qual conferir.** A aplicacao **nao
parou por isso** — a transicao e deterministica, e foi ancorada **a posteriori** em §5.1 —, mas
**o precedente e contrario, e e ele que torna isto lacuna e nao pratica:** `PS-2026-015`
publicou `H-P` para `ADR-0027` e `ADR-0029`, e `PS-2026-016` para `ADR-0030` e `RFC-0025`.
**`4` `ADR`/`RFC` hasheados em dois atos anteriores, contra `0` neste.**

**NAO corrigido, e a impossibilidade e estrutural:** corrigir seria **editar `PS-2026-017`**, e
o pacote e a **ancora do proprio ato** — um byte nele quebraria `c48cf443…0298`. Severidade
**Baixa**, dono **DEP-GOV**, gatilho *"proximo pacote soberano que submeta `ADR` a
ratificacao"*. **Familia de `RD-19`.** **`0` missoes abertas.**

## 10. O que esta aplicacao NAO fez

| Fronteira | Estado |
|---|---|
| `C0 · T2` | **NAO decidida.** Segue aberta pelo item V, e `RD-91` **nao fecha alem disso** |
| Missao do item IV *(`PRJ` e `TPL`)* | **NAO aberta.** O item VII a proibe ate esta aplicacao estar **conferida** |
| `FND-04` | **`0` bytes.** `RD-99` permanece **ABERTO**, pelo item VIII |
| `SPC-001` | **NAO reclassificada**, pelo item III. **`0` bytes** |
| `Spec` nova | **`0` criadas** |
| `PS-2026-017`, `ADR-0032` *(corpo)*, `RFC-0027`, `FIT-2026-025`, `PT-2026-018` | **`0` bytes de corpo** |
| `MSG-2026-0001` a `MSG-2026-0010` | **`0` bytes.** Historico nao se edita |
| Nota superada do item I do texto assinado | **NAO corrigida** — o ato veio *"sem alteracao de termo"* |
| `TPL-spec` *(`RD-93`)*, `FND-11 §14` *(`RD-100`)* | **`0` bytes.** Nao sao a celula autorizada |
| Congelamento | **EM VIGOR.** `1` achado novo **registrado**, `0` missoes abertas |

## 11. Prova de `0` bytes fora do conjunto autorizado

Conferido **arquivo a arquivo** por `sha256` contra a copia datada
`_backups/LucaX-Enterprise-OS_2026-08-02_pre-aplicacao-item-vi`, **236** arquivos, manifesto
`c794469e…b146`, **provado fiel** — a copia **reproduz os tres valores** do estado de partida,
`229 · 68.318 · 2a28e526…d17f`.

**Camada normativa: alterada EXATAMENTE nos quatro objetos do ato.** `FND-01` a `FND-08`,
`FND-10`, as **23** `CAP`, os **19** `TPL`, as **7** demais Cartas de Departamento e a Carta de
Produto: **`0` bytes**.

## 12. Rastreabilidade

| Elo | Artefato |
|---|---|
| Achado | **`RD-91`** — catalogo §7, item 115. **FECHA PARCIALMENTE aqui** |
| Instrucao | [RFC-0027](../rfcs/RFC-0027-separacao-de-proponente-e-aprovador-na-spec-c1.md) |
| Decisao | [ADR-0032](../decisions/ADR-0032-separacao-de-proponente-e-aprovador-na-spec-c1.md) — **`ativo` · `ratificada`** por este consumo |
| Parecer | [FIT-2026-025](fitness/FIT-2026-025-emenda-de-sf-10.md) |
| Submissao | [PS-2026-017](pacote-soberano-2026-08-02-rd-91.md) **1.3.0** |
| Producao | [PT-2026-018](relatorio-transicao-2026-08-02-emenda-sf-10.md) |
| **Ato** | [MSG-2026-0010](../memory/operacional/MSG-2026-0010-ato-soberano-emenda-que-sana-rd-91.md) — **decimo ato, CONSUMIDO** |
| **Aplicacao** | **este relatorio** |

## 13. Licao da missao

**O `H-P` publicado antes do ato transformou a promulgacao em teste, e o teste rodou fora do
acervo.** A ordem — aplicar o `O4` num diretorio de trabalho, conferir os quatro `sha256`, e so
entao copiar para dentro — significa que **nenhum byte errado chegou a existir no acervo**. Se
um `H-P` tivesse falhado, a aplicacao teria parado com o acervo **intacto**, e nao com o acervo
meio movido.

**O contraponto, e ele e da mesma missao:** o mesmo rigor **nao** alcancou `§13.2` das duas
Cartas, porque **ninguem publicou hash de `§13.2`**. O que tem `H-P` foi conferido quatro vezes;
o que nao tem passou. **`RD-105` e o preco disso, e esta declarado.**

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-08-02 | DEP-GOV | Criacao. Registra a **aplicacao ministerial do item VI** de [`MSG-2026-0010`](../memory/operacional/MSG-2026-0010-ato-soberano-emenda-que-sana-rd-91.md): `O4` nos **quatro** objetos, **`H-P` `4` de `4`**, **`H-N` invariante `4` de `4`**, **`IR-09` `4` de `4`** por DEP-QAR. Os `H-P` foram lidos de **duas sedes do proprio arquivo** e conferidos contra medicao nova — **`12` de `12`**, **`0` de `hashes-candidatos.txt`** *(`RD-101`)*. Catalogo, indices e contadores reconciliados **na mesma mudanca**; **`RD-104` INSCRITO** *(item 127)*, **`RD-91` FECHADO PARCIALMENTE** *(so quanto a `C1`; `C0 · T2` segue aberta pelo item V)* e **`RD-105` aberto** *(`§13.2` das duas Cartas declara `445`/`506` onde ha `446`/`507`)*. Baseline **`BL-2026-08-02-03`** emitida em **2** execucoes. Escrito sob **`fencing_token` 18**, adquirido **antes** da primeira escrita, com copia datada **provada fiel**. |
