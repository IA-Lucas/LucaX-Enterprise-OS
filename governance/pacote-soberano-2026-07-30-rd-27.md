---
id: PS-2026-011
titulo: Pacote de decisao soberana — emenda C3 Tipo 2 que fecha RD-27 em FND-01, FND-02 e FND-10
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
decisoes_relacionadas: [ADR-0009, ADR-0012, ADR-0022, ADR-0024]
substitui: []
substituido_por: null
canal: REPORTE
emissor: DEP-GOV
destinatario: SOBERANO
ttl: ate decisao do Soberano
resumo: Submete ao Soberano o fechamento integral de RD-27, com o candidato cumulativo unico de FND-01, a prova de que V2 nao o e, e a alternativa de contingencia medida.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# PS-2026-011 — `RD-27`: conformidade de contrato das fundacionais

> ## Este pacote **informa**. Nao decide, nao aprova, nao promulga e nao edita nada.
>
> **`FND-01` permanece em 1.5.0, `FND-02` em 1.3.0 e `FND-10` em 1.4.0.** Os candidatos existem
> como **arquivo real fora do acervo**, com caminho declarado em §4.4 — aplicacao de **`RD-19`**.
>
> **Caminho exato:** `governance/pacote-soberano-2026-07-30-rd-27.md` *(`RE-01`)*.
>
> **Pacote irmao e independente:** [PS-2026-012](pacote-soberano-2026-07-30-rd-37.md) *(`RD-37`)*.
> **Pacote coordenado, cuja base este substitui em parte:**
> [PS-2026-009 2.0.0](pacote-soberano-2026-07-29-fnd-11.md) — §3.

## Proposito

Levar ao Soberano o fechamento **integral** de **`RD-27`** — os tres objetos, os nove campos
ausentes e os seis valores defasados — pela unica via que `IR-05` deixa aberta.

## Escopo

| Item | Definicao |
|---|---|
| Inclui | **Quatro** objetos: `ADR-0024` e as promulgacoes de **`FND-01` 1.7.0 cumulativa**, **`FND-02` 1.4.0** e **`FND-10` 1.5.0** |
| **Nao** inclui | `RD-37` — [PS-2026-012](pacote-soberano-2026-07-30-rd-37.md) · o **merito** de `AC-06`, `AC-08`, `CE-04` · a **lista de `IR-03`** — **`RD-43` permanece aberto** · a **ampliacao do nucleo** · `FND-03` a `FND-09`, `FND-11`, `TPL-spec` e as **nove Cartas** — **`0` bytes** · `ADR-0021` e `ADR-0022`, que **nao sao editados** *(M1, CC-01, LV-04)* · `RD-33` *(bloqueante)*, `RD-36`, `RD-13` |
| Natureza | **Reporte**, entidade `MSG`. **Nenhum** tipo, entidade, camada, template ou diretorio novo |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| **Autor da emenda** | **DEP-GOV** | `FND-09 §8.2`, linha `FND` — **proponente unico** |
| **Materia alcancada** | **DEP-EXE** | **proprietario de `FND-02`** — consulta obrigatoria |
| **Revisor independente** | **DEP-QAR** | `RM-06b` — §5 |
| **DECIDE** | **SOBERANO** | **C3. Indelegavel.** **Nao ocorreu** |

---

## 1. O que se pede

| # | Objeto | Ato pedido | Se **nao** houver ato |
|---|---|---|---|
| **1** | **`ADR-0024`** | **Aprovacao e ratificacao** | `RD-27` permanece **ABERTO**, e o gatilho **redispara** no proximo ato que alcance qualquer um dos tres |
| **2** | **`FND-01` 1.7.0** | **Promulgacao** | `FND-01` segue **nao conforme a `AC-08`** *(4 campos)* e **sem** a hierarquia de `ADR-0022` |
| **3** | **`FND-02` 1.4.0** | **Promulgacao** | `FND-02` segue sendo o **unico artefato do acervo com zero dos cinco campos** |
| **4** | **`FND-10` 1.5.0** | **Promulgacao** | `§8.5` segue declarando **seis** valores de 2026-07-28 como se fossem correntes |

> **Aprovacao parcial e util aqui, e essa e a diferenca em relacao a `PS-2026-009`.** Os itens
> **3** e **4** sao **integralmente independentes**: recusar `FND-02` nao afeta `FND-10`, e
> vice-versa. **O item 2 tem um acoplamento, e ele esta declarado em §2.4.**

## 2. Diff literal

### 2.1 `FND-01` **1.5.0 → 1.7.0 cumulativa** — **8 blocos · +8 linhas · 5 substituidas · 8 acrescentadas**

| # | Local | Antes | Depois | Autoriza |
|---|---|---|---|---|
| **A1** | frontmatter L5 | `versao: 1.5.0` | `versao: 1.7.0` | cumulativa |
| **A2** | frontmatter L12 | `atualizado_em: 2026-07-29` | `atualizado_em: 2026-07-30` | data real |
| **A3** | frontmatter L14 | `[…, ADR-0018]` | `[…, ADR-0018, ADR-0022, ADR-0024]` | ambos |
| **A4** | frontmatter, apos `ratificacao` | *(inexistente)* | **4 linhas**: `resumo`, `perfil_contexto: nucleo`, `confidencialidade: interno`, `revisor: DEP-QAR` | **`ADR-0024`** |
| **A5** | **§10**, bloco da hierarquia | `… / Artifact Framework` | `… / Artifact Framework /`<br>`   Specifications Framework` | `ADR-0022` |
| **A6** | **§11**, verbete `Fundacao` | *"nove documentos (FND-01 a FND-09)"* | *"onze documentos (FND-01 a FND-11)"* | `ADR-0022` |
| **A7** | *Documentos derivados*, apos `FND-10` | *(inexistente)* | uma linha de tabela com rotulo `[FND-11]`, destino `11-framework-specifications.md` e titulo *Framework de Specifications*, **escrita como link markdown vivo no candidato**. **O destino nao e reproduzido aqui na forma de link**, porque o arquivo ainda nao existe e reproduzi-lo criaria alvo quebrado neste pacote — `LN-03` | `ADR-0022` |
| **A8** | Historico | *(inexistente)* | **2 linhas**: `1.6.0` *(literal de `V1`)* + `1.7.0` | ambos |

**`A5`, `A6`, `A7` e a linha `1.6.0` de `A8` sao byte a byte os de `V1`**, o candidato ja
submetido em `PS-2026-009`. **O que este rito acrescenta e `A4` e a linha `1.7.0`.**

### 2.2 O que o diff de `FND-01` **nao** contem

| Nao contem | Verificacao |
|---|---|
| Alteracao em **§1 a §11** *(corpo)*, exceto `A5`–`A7` | **`0` bytes** — `diff` do intervalo entre o fim do frontmatter e o inicio do historico contra `V1`: **vazio** |
| Nivel novo na hierarquia | **8 antes · 8 depois** |
| Alteracao da regra de precedencia interna do nivel 2 | **`0` linhas tocadas** |
| Alteracao em §4 *(Principios)*, §6.2 *(portoes)*, §7.3 *(direitos)*, §8 *(Linhas Vermelhas)*, §9 *(rito de emenda)* | **`0`** — **7 portoes antes, 7 depois** |
| Campo novo no contrato | **`0`** — os quatro **ja sao exigidos** por `AC-08` |

### 2.3 `V2` **nao** e byte a byte o candidato cumulativo — a resposta a pergunta da missao

**Medido:** `V2` **492** linhas · `43cae800…6767`; cumulativo **493** · `d3192235…f935b`.
**4 blocos de diff, +1 linha.**

| # | `V2` | Cumulativo | Natureza |
|---|---|---|---|
| 1 | `versao: 1.6.0` | `versao: 1.7.0` | Degrau cumulativo |
| 2 | `atualizado_em: 2026-07-29` | `2026-07-30` | Data real de execucao |
| 3 | `decisoes_relacionadas` **sem** `ADR-0024` | **com** `ADR-0024` | Rastreabilidade |
| 4 | **1** linha de historico, atribuindo `AC-08` a **`ADR-0022`** | **2** linhas, atribuindo `AC-08` a **`ADR-0024`** | **`RD-45` — afirmacao falsa** |

> ### ⚠ **`RD-45`** — Media, **fechado por este pacote**
>
> `ADR-0022` declara, em **`J14`** e em §7.3, que **nao trata `RD-27`** e que o candidato **nao**
> acrescenta os quatro campos. **A linha de historico de `V2` afirma o contrario, dentro de
> `FND-01`.** Promulgar `V2` poria no nivel 1 da hierarquia normativa uma afirmacao que um `ADR`
> **`M1`** contradiz — e `M1` **nao se emenda** para concordar.
>
> **Encontrado por construir o cumulativo e comparar, nao por reler `V2`.** Decima sexta
> confirmacao de `MEM-APR-0006`.

### 2.4 O acoplamento de `FND-01`, declarado — e a alternativa **medida**

**`A7` escreve um link markdown para `11-framework-specifications.md`.** Se o ato promulgar
`FND-01` 1.7.0 e **nao** promulgar `FND-11`, o acervo ganha **1 link quebrado** e uma hierarquia
que **enumera documento inexistente** — exatamente o que `PS-2026-009 §1` ja declarara ao dizer
que **`FND-11` + `FND-01` + `FND-03` formam um objeto normativo unico**.

| | **`1.7.0` cumulativa** *(objeto submetido)* | **`1.6.0` ALT** *(contingencia medida)* |
|---|---|---|
| Contem `ADR-0022` *(§10, §11, derivados)* | **Sim** | **Nao** |
| Contem `ADR-0024` *(`AC-08`)* | **Sim** | **Sim** |
| Links para `11-framework-specifications.md` | **1** | **`0`** |
| Aplicavel **sem** `FND-11` | **Nao** | **Sim** |
| Linhas · `H-A` | **493** · `d3192235…f935b` | **490** · `a9c0334a…69bb` |

**Recomendacao: `1.7.0` cumulativa.** A `ALT` existe **para que a escolha seja possivel**, nao
para que seja tomada — mesmo metodo de `PS-2026-009 §3.1`. **Escolhe-la exige trocar um hash na
minuta e declarar que o ato nao alcanca `FND-11`.** **Apenas uma das duas entra em vigor: em
nenhum cenario existem dois `FND-01`.**

### 2.5 `FND-02` **1.3.0 → 1.4.0** — **5 blocos · +6 linhas**

| # | Local | Antes | Depois |
|---|---|---|---|
| **B1** | frontmatter L5 | `versao: 1.3.0` | `versao: 1.4.0` |
| **B2** | frontmatter L12 | `atualizado_em: 2026-07-29` | `2026-07-30` |
| **B3** | frontmatter L14 | `[…, ADR-0016]` | `[…, ADR-0016, ADR-0024]` |
| **B4** | frontmatter, apos `substituido_por` | *(inexistente)* | **5 linhas**: `resumo`, `perfil_contexto: missao`, `confidencialidade: interno`, `revisor: DEP-QAR`, `ratificacao: ratificada` |
| **B5** | Historico | *(inexistente)* | linha `1.4.0` |

**O que o diff de `FND-02` nao contem:** `§1` a `§10` — **`0` bytes**; **9 departamentos antes e
depois**; **4 classes**; a **matriz de interacao de 81 celulas** e `MI-01` a `MI-06` — **`0`
tocados**; a escada de especializacao — **`0`**; invariantes `IV-*` e `ES-*` — **`0`**.

### 2.6 `FND-10` **1.4.0 → 1.5.0** — **6 blocos · +7 linhas · 11 substituidas**

| # | Local | Antes | Depois |
|---|---|---|---|
| **C1** | frontmatter L5 | `versao: 1.4.0` | `versao: 1.5.0` |
| **C2** | frontmatter L12 | `atualizado_em: 2026-07-29` | `2026-07-30` |
| **C3** | frontmatter L14 | `[…, ADR-0019]` | `[…, ADR-0019, ADR-0024]` |
| **C4** | **§8.5**, cabecalho e 2 linhas da tabela | `Custo medido` · `468` · `619` | ``Custo medido em `BL-2026-07-29-10` `` · **485** · **631** |
| **C5** | **§8.5**, paragrafo-resumo e nota `CE-05` | `1.087` · `18.916` · `5,7%` · `1.225` | **1.116** · **51.698** · **2,2%** · **1.263**, mais **6 linhas** de regra de leitura |
| **C6** | Historico | *(inexistente)* | linha `1.5.0` |

**O que o diff de `FND-10` nao contem — medido, nao afirmado:** `§1` ate `§8.4` e `§9` ate `§11`
sao **identicos byte a byte** ao arquivo em vigor. **`0`** regras `AC-*`, `PJ-*`, `CE-*`, `IR-*`,
`RG-*`, `CV-*` criadas, removidas ou alteradas. **O nucleo obrigatorio continua sendo os mesmos 4
artefatos** — amplia-lo seria `C2` com Fitness Check, e **isto nao o amplia**.

> **`FND-10` e `CRLF`.** **778 → 785 linhas, `785` de `785` terminadores `CRLF` preservados, `0`
> convertidos.** A montagem foi **binaria**; montar em modo texto converteria o arquivo inteiro e
> destruiria o `H-A` **sem mudar uma linha de norma**.

## 3. Coordenacao com `PS-2026-009` — **um unico `FND-01` para o ato**

| Estado | `PS-2026-009` **1.0.0** | `PS-2026-009` **2.0.0** *(atualizado)* |
|---|---|---|
| Objeto `FND-01` | **`V1`** 1.6.0 `acec800b…a3a8` *(recomendado)* + **`V2`** 1.6.0 `43cae800…6767` | **remetido a este pacote** — `FND-01` **1.7.0** `d3192235…f935b` |
| `FND-11`, `FND-03`, `ADR-0022` | inalterados | **inalterados**, mesmos hashes |
| Variantes vivas de `FND-01` | **2** | **1** |

**A versao 1.0.0 e preservada como evidencia**, integral e nao editada, em
`_backups/LucaX-Enterprise-OS_2026-07-30_pre-missao-1-13-2/`, com **446 linhas** e `H-A`
**`e349b4fbb3cfb5de61b5e551d844300b19cf4e85d6b00d7adcba6a2bec17c3be`**, medido **antes** de
qualquer edicao e **identico ao do arquivo no acervo naquele instante**, verificado por
comparacao. **Nenhum pacote aponta para base substituida:** `PS-2026-009` 2.0.0
**deixa de enumerar `V1` e `V2` como objetos** e passa a remeter a este pacote.

> **`V1` e `V2` nao sao apagados — sao aposentados com razao registrada.** `V1` porque
> **nao fecha `RD-27`**, e a determinacao da missao que o justificava foi substituida; `V2` porque
> **contem `RD-45`**. **Os dois arquivos permanecem em `_candidatos/` como evidencia historica**,
> e seus hashes continuam publicados em `PS-2026-009 §4.1`, que **nao e reescrito**.

## 4. Identificadores de integridade

### 4.1 Objetos em vigor e candidatos

| Objeto | Versao | Linhas | `H-A` | `H-N` |
|---|---|---|---|---|
| **`FND-01` em vigor** | 1.5.0 | **485** | `2d962616ebd1b1e952eac1f3c98873385d32d26160d7e8f3f9e2c82de7ac310d` | `fcb6e4bd5dd2e8d59c5f8038d0f85b2fdc1239fe78f7be5439bf640779536198` |
| **`FND-01` candidato — cumulativo** | **1.7.0** | **493** | **`d319223519dfd576ef279e413736eda7496d553d309c2266b18f4cbcd69f935b`** | `f5172f2179793bbd2ee86bd5cf92af3e449297e9a0bc981c3b4585176e65e963` |
| **`FND-01` `ALT`** *(contingencia — §2.4)* | **1.6.0** | **490** | **`a9c0334a376755a275f2b5c1629b32303cb1cd3a1773acd10a67071989e269bb`** | `f3a1e2a0c3b2677adfe9f36bc1ea13adc881c10005b71f75e05ef088baf6e629` |
| **`FND-02` em vigor** | 1.3.0 | **518** | `a42fadbf4258b7526f3b5fbdcb0fcea4f93f17528c6ab484530acc533f3530e3` | `1dddf9ff048834664f8236b76b0816a184337166f0de9d7945afa853a006ae6f` |
| **`FND-02` candidato** | **1.4.0** | **524** | **`1fb4e49b6f82abd98977b4c1ee1ea89c11fda2a6303ff8c3e7cca2b0f837ddb6`** | `66d4651b7f121642ae344498d87aa0fafbfff80233c6743da9fe5bda10c06a36` |
| **`FND-10` em vigor** | 1.4.0 | **778** `CRLF` | `d52e6284a85bd39185bff345b296aa8d4161e46f19eb1aefa031d862cab70e80` | `96ff74181eac9f3886f321ecb57dae9c08940c01495ac8c76394cff0a199391b` |
| **`FND-10` candidato** | **1.5.0** | **785** `CRLF` | **`10f03ebd6ac3583a17a2819d9a2296ecad6f106913d96224e5b4db0826f506f0`** | `651fbaf091731a845045f25c7f3ec77cc49a9e909229826889142c64bc72e146` |

**`H-P` dos tres candidatos = `H-A`** — a promulgacao **nao executa `O4`** sobre eles: os tres ja
estao `ativo` e `ratificada`, mesmo regime aplicado a `FND-01` e `FND-03` em `PS-2026-009 §4.1`.
**A assimetria em relacao as Cartas esta declarada como `RD-47`** em
[ADR-0025 §5.2](../decisions/ADR-0025-extensao-da-propagacao-de-qg-1-as-cartas-restantes.md).

### 4.2 `ADR-0024`, `RFC-0020` e a versao preservada de `PS-2026-009`

| Objeto | Caminho · versao · linhas | `H-A` | `H-N` | `H-P` projetado |
|---|---|---|---|---|
| **`ADR-0024`** | `decisions/ADR-0024-conformidade-de-contrato-das-fundacionais.md` · **1.0.0** · **341** | **`9adfa251357efa63841f763f036f9026a28b5b13a0c4e43a7d0cea2f9ab66072`** | `4db0bcb73a9fdaad86c94dd08c7e86285aef4a3e970646a0914129b064e004aa` | **`874ae531e26096897fca61adb766853829c065c9d43ee6411f99c4d35573b0ce`** |
| **`RFC-0020`** | `rfcs/RFC-0020-conformidade-de-contrato-das-fundacionais.md` · **1.0.0** · **227** | `bbec81f145c471707cadeacbaf6ccac08d0168f9e8a9b6f5381ed6f5ffec696b` | — | — |
| **`PS-2026-009` 1.0.0** *(preservada)* | `_backups/…_2026-07-30_pre-missao-1-13-2/governance/pacote-soberano-2026-07-29-fnd-11.md` · **1.0.0** · **446** | `e349b4fbb3cfb5de61b5e551d844300b19cf4e85d6b00d7adcba6a2bec17c3be` | — | — |

**Estado de `ADR-0024` hoje:** `em-revisao` · `ratificacao: pendente`. **`H-N` invariante sob
`O4` — verificado.** **`O4` = `status` + `ratificacao`** *(C3, ratificacao **exigida**)*.

### 4.3 Metodo de medicao — **reimplementacao validada antes do uso**

`IR-02` e `IR-03` foram **reimplementados de forma independente** e validados **primeiro contra
artefatos com hash ja publicado**, antes de medir qualquer candidato:

| Controle | Fonte do valor esperado | Medidas |
|---|---|---|
| `FND-01` 1.5.0 · `FND-03` 1.5.0 | PS-2026-009 §4.1 | `H-A` ✅ · `H-N` ✅ |
| `ADR-0021` *(em vigor)* | PS-2026-009 §3.1 | `H-A` ✅ · `H-N` ✅ |
| `ADR-0022` | PS-2026-009 §4.2 | `H-A` ✅ · `H-N` ✅ · `H-P` ✅ |
| `RFC-0018` | PS-2026-009 §4.2 | `H-A` ✅ |
| `FND-11` candidato | PS-2026-009 §4.1 | `H-A` ✅ · `H-N` ✅ · `H-P` ✅ |
| `FND-01` `V1` e `V2` · `FND-03` candidato | PS-2026-009 §4.1 | `H-A` ✅ · `H-N` ✅ |
| `DEP-PRD` e `DEP-EXE` candidatos | PS-2026-010 §4.1 | `H-A` ✅ · `H-N` ✅ · `H-P` ✅ |

**19 de 19 controles reproduzem, digito a digito**, em **quatro** tipos documentais
*(`FND`, `ADR`, `RFC`, `DEP`)* e nas **tres** medidas. **A medicao dos candidatos so ocorreu
depois.**

**Baseline reconferida antes de qualquer escrita:** `BL-2026-07-29-10` reproduziu **177
artefatos · 51.698 linhas · `f7e56bc835409cd848fcb03f3998ac58ba78e57a09b584f583a56fdc25d11bd4`**.

### 4.4 Onde os candidatos vivem — aplicacao de `RD-19`

```
E:\LucasIA\Projetos\_backups\LucaX-Enterprise-OS_2026-07-30_pre-missao-1-13-2\_candidatos\
  fnd-01-1.7.0.md                  493 linhas  LF     d3192235…f935b   (cumulativo — submetido)
  fnd-01-1.6.0-ALT-sem-fnd-11.md   490 linhas  LF     a9c0334a…69bb    (contingencia — §2.4)
  fnd-02-1.4.0.md                  524 linhas  LF     1fb4e49b…ddb6
  fnd-10-1.5.0.md                  785 linhas  CRLF   10f03ebd…506f0
  fnd-01-1.6.0.md  · fnd-01-1.6.0-V2.md  · fnd-03-1.6.0.md · fnd-11-1.0.0.md
  prd-1.1.0.md     · exe-1.1.0.md                      (preservados de 2026-07-29)
```

**Os arquivos existem e reproduzem os `H-A` acima, conferidos apos a copia.** **Terminadores:
`LF` em todos, exceto `FND-10`, que e `CRLF` em 785 de 785.** **Montados por transformacao
programatica do arquivo em vigor**, nunca por reescrita manual — e e essa a razao pela qual
*"`0` bytes de corpo"* pode ser afirmado **byte a byte**.

### 4.5 `IR-09` — teste de reconstrucao

| Objeto | Operacao | Resultado |
|---|---|---|
| `ADR-0024` | Reverter **apenas** `status` e `ratificacao` no arquivo pos-`O4` e medir | **Reproduz `H-A`** |
| `FND-01`, `FND-02`, `FND-10` | Nao se aplica — **nao executam `O4`** | — |

## 5. Revisao independente — **DEP-QAR**, objeto a objeto

> **Escopo da revisao:** identidade, versao, hash, diff literal, conformidade de contrato e
> ausencia de alteracao alem do declarado. **Nao alcanca o merito da decisao**, que e do Soberano.

| Objeto | O que foi conferido | Veredito |
|---|---|---|
| **`ADR-0024`** | 13 secoes de `FND-07 §4.1`; `VD-01` a `VD-09`; `revisor ≠ autor`; classificacao com duvida declarada | **CONFORME**, com a ressalva `QR-1` |
| **`FND-01` 1.7.0** | `A1`–`A8`; corpo contra `V1` **byte a byte**; `A5`–`A7` identicos ao ja submetido; `RD-45` fechado | **CONFORME** |
| **`FND-02` 1.4.0** | `B1`–`B5`; corpo **`0` bytes**; cada um dos 5 valores rastreado a fonte escrita | **CONFORME** |
| **`FND-10` 1.5.0** | `C1`–`C6`; `§1`–`§8.4` e `§9`–`§11` **identicos byte a byte**; `CRLF` 785/785 | **CONFORME** |

| # | Ressalva de `DEP-QAR` | Severidade |
|---|---|---|
| **`QR-1`** | **`ratificacao: ratificada` e escrito no candidato de `FND-02` antes do ato que promulga a 1.4.0.** O valor e verdadeiro quanto ao ato de 2026-07-29 e ao proprio ato pedido, e **repete literalmente o regime ja aplicado** a `FND-01` 1.6.0 e `FND-03` 1.6.0 em `PS-2026-009`. **A ressalva nao pede mudanca — registra que o regime nunca foi decidido por ADR**, e e o que `RD-47` declara | **Baixa** |
| **`QR-2`** | **`DEP-QAR` revisa e `DEP-GOV` propoe e valida a forma da RFC.** Determinacao de `FND-09 §8.2`. **Nona ocorrencia de `RC-02`** — `RD-39` | **Observada** |

## 6. Independencia dos objetos

| Objeto | Independente? | Verificavel? | Bloqueavel isoladamente? |
|---|---|---|---|
| **`ADR-0024`** | **Sim** | **Sim** — `H-A`, `H-N`, `H-P` | **Sim** — recusa-lo recusa os tres |
| **`FND-02` 1.4.0** | **Sim** | **Sim** | **Sim** — **`0` dependencias** |
| **`FND-10` 1.5.0** | **Sim** | **Sim** | **Sim** — os valores sao os de `BL-2026-07-29-10`, **nao** os projetados, **justamente para nao depender de `FND-01`** |
| **`FND-01` 1.7.0** | **Nao, e esta declarado** | **Sim** | **Com condicao** — §2.4: depende de `FND-11`. **A `ALT` `a9c0334a…69bb` restaura a independencia, e esta medida** |

**Prova textual da independencia de `FND-02` e `FND-10`:** nenhuma linha dos seus diffs cita
`FND-11`, `ADR-0022` ou o outro candidato — verificavel por `grep` sobre §2.5 e §2.6.

## 7. Impacto

| Verificacao | Resultado | Evidencia |
|---|---|---|
| **Artefatos nao conformes a `AC-08`** | **2 → 0** | §2.1, §2.5 |
| **Valores falsos em `FND-10 §8.5`** | **5 → 0** | §2.6 |
| **Variantes vivas de `FND-01`** | **2 → 1** | §3 |
| **Linhas de corpo de norma alteradas** | **`0`** em `FND-01` *(fora de `A5`–`A7`, de `ADR-0022`)* · **`0`** em `FND-02` · **`0`** em `FND-10` fora de `§8.5` | `diff` |
| **Regras criadas ou alteradas** | **`0`** `AC-*` · **`0`** `IR-*` · **`0`** `CE-*` · **`0`** `PJ-*` · **`0`** `MI-*` · **`0`** `IV-*` | §2.2, §2.5, §2.6 |
| **Titulares · portoes · papeis · classes · verbos · entidades · tipos documentais** | **`0` criados · `0` alterados** | `FND-09 §11.1` |
| **Niveis da hierarquia normativa** | **8 antes · 8 depois** | §2.2 |
| **Departamentos · classes · celulas da matriz de interacao** | **9 · 4 · 81 — inalterados** | §2.5 |
| **Nucleo obrigatorio** | **4 artefatos antes · 4 depois** | §2.6 |
| **Vinculo `Spec` × `Produto`** | **`0` bytes.** **`RD-33` permanece aberto e BLOQUEANTE** | — |
| **`ADR-0021` e `ADR-0022`** | **`0` bytes** — `M1` | — |
| **Excecoes formais** | **`0` criadas** — `governance/exceptions/` **vazio** | — |
| **Custo de contexto** | **+8** `FND-01` · **+6** `FND-02` · **+7** `FND-10` = **+21 linhas de norma**. **`0`** artefato novo no nucleo | `CE-02` |
| Reversibilidade | **Tipo 2** — 3 restauracoes binarias, `H-A` de partida publicado | [ADR-0024 §11](../decisions/ADR-0024-conformidade-de-contrato-das-fundacionais.md) |

## 8. Risco residual

| # | Risco | Sev. | Mitigacao declarada |
|---|---|---|---|
| **RS-1** | **`FND-01` promulgado sem `FND-11`** → link quebrado + hierarquia orfa | **Alta** | **§2.4**, com a **`ALT` medida e publicada**. **Nao ha versao deste ato que evite o acoplamento — ha versao que o declare e resolva** |
| **RS-2** | `§8.5` envelhecer de novo | Media | **A regra de leitura entra na secao** e vincula valor a baseline |
| **RS-3** | `Tipo 2` ser contestado | Media | **`Q1`** — declarar `Tipo 1` **nao altera nenhum hash** |
| **RS-4** | **Ato nao vir** | Media | `AC-06` segue descumprido e **declarado**; padroes de `FND-10 §2.2` seguem valendo. **Nenhum bloqueio novo** |
| **RS-5** | Autoria concentrada em `DEP-GOV` | **Observada** | **`RD-39`, nona ocorrencia.** `DEP-EXE` e consulta obrigatoria |

## 9. As escolhas que o ato pode fazer diferente

| # | Escolha | Como se expressa | Altera hash? |
|---|---|---|---|
| **Q1** | Classificar `ADR-0024` como **`Tipo 1`** | Declaracao expressa no ato | **Nao** |
| **Q2** | Promulgar a **`ALT`** de `FND-01`, **sem** `FND-11` | Trocar o `SHA-256` de `FND-01` por `a9c0334a…69bb` e declarar que o ato **nao alcanca `FND-11`, `FND-03` nem `ADR-0022`** | **Sim** — so o de `FND-01` |
| **Q3** | Bloquear **`FND-02`** ou **`FND-10`** isoladamente | Omitir o objeto da enumeracao | **Nao** — os outros permanecem validos |
| **Q4** | Manter **`RD-46`** aberto em vez de fechar | Declarar expressamente. **`C5` ja corrige os valores**; o que ficaria aberto e o **registro** | **Nao** |

## 10. Recomendacao

| Campo | Conteudo |
|---|---|
| **Recomendacao** | **APROVAR** os quatro objetos, com `FND-01` na variante **cumulativa 1.7.0** |
| **Fundamento** | A obrigacao **ja vigora desde 2026-07-28** e **e cumprivel hoje sem reescrever uma linha de norma** — `0` bytes de corpo nos tres, medido. **Nenhum valor foi inventado:** os nove campos vem de catalogo curado, padrao por tipo, padrao do acervo, matriz de autoridade e ato datado. E a correcao alcanca **a causa**, nao so os numeros |
| **Contrapartida honesta** | **Tres.** *(i)* **`FND-01` fica acoplado a `FND-11`** — declarado em §2.4, com a `ALT` medida. *(ii)* **`RD-43` continua aberto**: a assimetria de `IR-03` que torna a correcao cara **nao e resolvida aqui**, e resolve-la seria `C2` proprio. *(iii)* **`RD-47` nasce declarado e nao resolvido** — o regime de estado na promulgacao de versao nova **nunca foi decidido por ADR** |
| **O pacote informa; nao decide** | **Nao decidir e resultado valido.** `RD-27` permanece aberto e declarado, e **ninguem e induzido a erro**, porque os cinco campos tem padrao. **O custo e a quarta ocorrencia** |

## 11. Rastreabilidade

| Campo | Conteudo |
|---|---|
| RFC → ADR | [RFC-0020](../rfcs/RFC-0020-conformidade-de-contrato-das-fundacionais.md) → [ADR-0024](../decisions/ADR-0024-conformidade-de-contrato-das-fundacionais.md) |
| **Achados que fecha** | **`RD-27`** *(integral)* · **`RD-45`** *(§2.3)* · **`RD-46`** *(§2.6)* |
| Achados que **nao** fecha | **`RD-33`** *(bloqueante)* · **`RD-43`** · **`RD-47`** *(novo, declarado)* · `RD-13` · `RD-36` · `RD-39` |
| Ressalvas que fecha | **`R2`** de [FIT-2026-014](fitness/FIT-2026-014-regime-ministerial-e-cobertura-de-contexto.md) · **`R3`** de [FIT-2026-016](fitness/FIT-2026-016-canonizacao-e-propagacao.md) |
| Pacote coordenado | [PS-2026-009](pacote-soberano-2026-07-29-fnd-11.md) **2.0.0** — §3 |
| Pacote irmao, **independente** | [PS-2026-012](pacote-soberano-2026-07-30-rd-37.md) |
| Minuta unica do ato | [PS-2026-013](pacote-soberano-2026-07-30-consolidado.md) |
| Regra de integridade | [ADR-0012](../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md), `IR-01` a `IR-10` |
| Verificacao de aptidao | [FIT-2026-017](fitness/FIT-2026-017-convergencia-pre-ratificacao.md) |
| Relatorio da missao | [PT-2026-009](relatorio-transicao-2026-07-30-convergencia.md) |
| Baseline vigente na submissao | **`BL-2026-07-29-10`** |

---

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-30 | DEP-GOV | Pacote da **Missao 1.13.2**: emenda **C3 · Tipo 2** que **fecha `RD-27` integralmente** — `FND-01` **1.7.0 cumulativa** *(485 → 493)*, `FND-02` **1.4.0** *(518 → 524)* e `FND-10` **1.5.0** *(778 → 785, `CRLF`)* —, com **diff literal item a item**, `H-A` e `H-N` integrais de base e candidato, `IR-09` e minuta remetida a `PS-2026-013`. **Oitavo pacote soberano.** **§2.3 responde a pergunta que a missao determinou, e a resposta e NAO:** `V2` **nao** e byte a byte o candidato cumulativo — **4 blocos, +1 linha** — e **uma das quatro diferencas nao e cosmetica**: `V2` atribui a **`ADR-0022`** o backfill de `AC-08`, que o **escopo literal de `ADR-0022` exclui** em `J14` e §7.3, e `ADR-0022` e **`M1`**, logo **nao poderia ser corrigido para concordar** — achado **`RD-45`**, **encontrado por construir o cumulativo e comparar**. **§2.4 declara um acoplamento que a missao exigia eliminar e que nao se elimina por redacao:** `A7` escreve **link markdown** para `11-framework-specifications.md`, logo `FND-01` **1.7.0 nao e aplicavel sem `FND-11`** — e o pacote **mede a alternativa em vez de discuti-la**, publicando a **`ALT` 1.6.0** *(490 linhas, `a9c0334a…69bb`, **`0` links para `FND-11`**)*, que **restaura a independencia** e cuja escolha exige **trocar um hash e declarar o alcance menor**. **§2.6 corrige `FND-10 §8.5` na causa:** **seis** valores contra os **tres** de `RD-27` — o denominador do acervo, o percentual e a nota de `CE-05` **nunca haviam sido contados**, achado **`RD-46`** —, e a secao recebe **regra de leitura que vincula cada valor a baseline em que vale**; **os valores sao os de `BL-2026-07-29-10`, e nao os projetados, precisamente para que `FND-10` nao dependa da aprovacao de `FND-01`**. **§3 elimina a colisao de `FND-01`: de duas variantes vivas para uma**, com `PS-2026-009` atualizado a **2.0.0** e a **1.0.0 preservada como evidencia**, sem que `V1` e `V2` sejam apagados — **sao aposentados com razao registrada**. **§4.3 registra `IR-02`/`IR-03` reimplementados e validados contra 19 controles publicados, em 4 tipos documentais e nas 3 medidas, antes de medir qualquer candidato**, e a **baseline reconferida antes de qualquer escrita**. **§5 traz a revisao independente de `DEP-QAR` objeto a objeto**, com **duas ressalvas**. **`0` regras criadas · `0` titulares · `0` portoes · `0` papeis · `0` classes · `0` verbos · `0` entidades · `0` tipos documentais · 8 niveis de hierarquia antes e depois · 9 departamentos e 81 celulas de matriz intocados · nucleo obrigatorio de 4 antes e 4 depois · `0` bytes em `ADR-0021` e `ADR-0022` · `0` excecoes formais · `0` bytes no vinculo `Spec` × `Produto`.** |
