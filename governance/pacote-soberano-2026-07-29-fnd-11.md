---
id: PS-2026-009
titulo: Pacote de decisao soberana — emenda C3 Tipo 1 que cria FND-11 e promove SF-01 a SF-32 a sede fundacional
tipo: relatorio
versao: 2.0.0
status: ativo
camada_memoria: operacional
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-07-29
atualizado_em: 2026-07-30
revisao_prevista: null
decisoes_relacionadas: [ADR-0012, ADR-0021, ADR-0022, ADR-0024]
substitui: []
substituido_por: null
canal: REPORTE
emissor: DEP-GOV
destinatario: SOBERANO
ttl: ate decisao do Soberano
resumo: Submete ao Soberano a criacao de FND-11 e as emendas a FND-01 e FND-03, com diff literal, hashes integrais, a prova por diff de que 30 das 32 regras migram byte a byte, e duas variantes do candidato FND-01 para a colisao com RD-27.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# PS-2026-009 — `FND-11` e as emendas a `FND-01` e `FND-03`

> ## Este pacote **informa**. Nao decide, nao aprova, nao promulga e nao edita nada.
>
> **`FND-11` nao existe no acervo.** `FND-01` permanece em **1.5.0** e `FND-03` em **1.5.0**.
> Os candidatos existem como **arquivo real fora do acervo**, com caminho declarado em §4.4 —
> aplicacao de **`RD-19`**.
>
> **Pacote separado de [PS-2026-010](pacote-soberano-2026-07-29-rd-31.md), por determinacao.**
> A **sede da norma** e a **propagacao nas Cartas** sao materias distintas. **Podem compartilhar
> um ato**, e cada objeto permanece **independente, verificavel e bloqueavel isoladamente** — §6.
>
> **Caminho exato:** `governance/pacote-soberano-2026-07-29-fnd-11.md` *(RE-01)*.

> ## ⚠ Versao **2.0.0** — o objeto `FND-01` deste pacote foi **substituido**, e a razao esta dita
>
> **A Missao 1.13.2 instituiu o rito proprio de `RD-27`** — [RFC-0020](../rfcs/RFC-0020-conformidade-de-contrato-das-fundacionais.md)
> → [ADR-0024](../decisions/ADR-0024-conformidade-de-contrato-das-fundacionais.md) →
> [PS-2026-011](pacote-soberano-2026-07-30-rd-27.md) —, e com ele **`FND-01` passou a ser
> alcancado por dois ritos**. **So pode existir um `FND-01` final para o ato.**
>
> | Campo | **1.0.0** *(preservada)* | **2.0.0** *(esta)* |
> |---|---|---|
> | Objeto `FND-01` | **`V1`** 1.6.0 `acec800b…a3a8` *(recomendado)* **+ `V2`** 1.6.0 `43cae800…6767` | **remetido a `PS-2026-011 §4.1`** — `FND-01` **1.7.0 cumulativa**, `d3192235…f935b` |
> | `FND-11`, `FND-03`, `ADR-0022` | — | **inalterados, mesmos hashes** |
> | Variantes vivas de `FND-01` | **2** | **1** |
> | `§5` *(a colisao de `RD-27`)* | submete a escolha | **resolvida pelo rito proprio** |
>
> **`V1` e `V2` nao entram em vigor, e nao sao apagados.** `V1` porque **nao fecha `RD-27`**, e a
> determinacao que o justificava foi substituida; **`V2` porque contem `RD-45`** — atribui a
> `ADR-0022` o backfill de `AC-08` que o **escopo literal de `ADR-0022` exclui** (`J14`, §7.3).
> **Os dois arquivos permanecem em `_candidatos/` como evidencia**, e **os hashes publicados em
> §4.1 e §5 nao sao reescritos**: eles registram o que foi submetido em 2026-07-29, e essa e a
> sua funcao.
>
> **A versao 1.0.0 esta preservada integral e nao editada** em
> `_backups/LucaX-Enterprise-OS_2026-07-30_pre-missao-1-13-2/governance/`, **446 linhas**,
> `H-A` **`e349b4fbb3cfb5de61b5e551d844300b19cf4e85d6b00d7adcba6a2bec17c3be`**, medido **antes**
> de qualquer edicao.
>
> **O que continua valendo desta 2.0.0:** §2.3 e §2.4 *(`FND-03` e `FND-11`)*, §3 *(a sucessao
> parcial de `ADR-0021`)*, §4.1 **exceto as linhas de `FND-01` candidato**, §4.2, §4.3, §4.5, §6,
> §7 e §8. **O que foi superado:** §1 item **3**, §2.1, §2.2, §5, §9 e `Q2` de §9.1 —
> **remetidos a [PS-2026-011](pacote-soberano-2026-07-30-rd-27.md)**, e a **minuta unica** esta em
> [PS-2026-013](pacote-soberano-2026-07-30-consolidado.md).

## Proposito

Levar ao Soberano a promocao de **`SF-01` a `SF-32`** de dentro de `ADR-0021` para a **sede
fundacional** que `FND-10 §4.1` reserva a norma de dominio — a forma documental **Framework**,
entidade `FND` — **com a equivalencia provada por ferramenta**.

## Escopo

| Item | Definicao |
|---|---|
| Inclui | **Tres** objetos: `ADR-0022`, a criacao de **`FND-11` 1.0.0** e as promulgacoes de **`FND-01` 1.6.0** e **`FND-03` 1.6.0** |
| **Nao** inclui | `RD-31` — [PS-2026-010](pacote-soberano-2026-07-29-rd-31.md) · o **merito** de `SF-01` a `SF-31` · o **vinculo `Spec` × `Produto`** *(`RD-33`, **nao reaberto**)* · `FND-02`, `FND-04` a `FND-10`, `TPL-spec` e as **nove Cartas** — **`0` bytes** · **`ADR-0021`**, que **nao e editado** *(M1, CC-01, LV-04)* · `RD-27` *(§5)* e `RD-36` · qualquer artefato historico |
| Natureza | **Reporte**, entidade `MSG`. **Nenhum** tipo, entidade, camada, template ou diretorio novo |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| **Autor da emenda** | **DEP-GOV** | `FND-09 §8.2`, linha `FND` — **proponente unico** |
| **Materia** | **DEP-PRD** | Dono do tipo `SPC`; autor do merito em `ADR-0021` |
| **Revisor independente** | **DEP-QAR** | `RM-06b` |
| **DECIDE** | **SOBERANO** | **C3 · Tipo 1. Indelegavel.** **Nao ocorreu** |

> **Residuo declarado (`PI-10`).** **`DEP-PRD` e a area alcancada** — a norma da sua materia muda
> de sede e de regime de mudanca — e **nao e autora nem revisora**, porque `FND-09 §8.2` **nao lhe
> permite** propor nem revisar `FND`. Residuo **de matriz, nao de interesse** — `IC-3`, `RD-39`.

---

## 1. O que se pede

| # | Objeto | Ato pedido | Se **nao** houver ato |
|---|---|---|---|
| **1** | **`ADR-0022`** | **Aprovacao e ratificacao** | A norma da `Spec` permanece em `ADR-0021`, **vigente e intacto**. **Nenhum bloqueio novo** — apenas a sede provisoria continua |
| **2** | **`FND-11` 1.0.0** *(criacao)* | **Promulgacao** | `foundation/` permanece com **10** documentos |
| **3** | **`FND-01` 1.6.0** | **Promulgacao** | O nivel 2 da hierarquia permanece com **9** membros, e o verbete `Fundacao` segue declarando **nove** documentos quando existem **dez** — `RD-38` |
| **4** | **`FND-03` 1.6.0** | **Promulgacao** | A arvore canonica permanece sem `11-framework-specifications.md` |

> **Nao ha aprovacao parcial util entre 2, 3 e 4.** `FND-11` sem `FND-01 §10` seria **`FND`
> orfao**: a hierarquia e definida por **enumeracao**, e o que nao consta **nao ocupa nivel**.
> `FND-01` sem `FND-11` enumeraria um documento **inexistente**. `FND-03` sem `FND-11` apontaria
> a arvore para arquivo **ausente**. **Os tres formam um objeto normativo unico**; o item **1** e
> separavel apenas no sentido de que recusar o ADR recusa os tres.

## 2. Diff literal

### 2.1 `FND-01` **1.5.0 → 1.6.0** — variante `V1` *(recomendada)*

| # | Local | Antes | Depois |
|---|---|---|---|
| **A1** | frontmatter, linha 5 | `versao: 1.5.0` | `versao: 1.6.0` |
| **A2** | frontmatter, linha 14 | `decisoes_relacionadas: [ADR-0001, ADR-0002, ADR-0003, ADR-0004, ADR-0006, ADR-0018]` | `[..., ADR-0018, ADR-0022]` |
| **A3** | **§10**, bloco da hierarquia | `   Decisoes / Capability Framework / Meta Model / Artifact Framework` | `   Decisoes / Capability Framework / Meta Model / Artifact Framework /`<br>`   Specifications Framework` |
| **A4** | **§11**, verbete `Fundacao` | `O conjunto dos nove documentos fundacionais (FND-01 a FND-09).` | `O conjunto dos onze documentos fundacionais (FND-01 a FND-11).` |
| **A5** | *Documentos derivados*, apos `FND-10` | *(inexistente)* | uma linha de tabela com rotulo `[FND-11]`, destino `11-framework-specifications.md` e titulo *Framework de Specifications*. **O destino nao e escrito aqui como link, porque o arquivo ainda nao existe** (`LN-03`) |
| **A6** | Historico, ao final | *(inexistente)* | linha `1.6.0`, descrevendo `A1`–`A5` |

**`atualizado_em` nao muda:** ja declara `2026-07-29`.

**O bloco de §10, integral, antes e depois:**

```
antes:
1. Constituicao (este documento)
2. Estrutura Organizacional / Taxonomia / Governanca / Comunicacao / Memoria /
   Decisoes / Capability Framework / Meta Model / Artifact Framework
3. ADRs aprovados e vigentes

depois:
1. Constituicao (este documento)
2. Estrutura Organizacional / Taxonomia / Governanca / Comunicacao / Memoria /
   Decisoes / Capability Framework / Meta Model / Artifact Framework /
   Specifications Framework
3. ADRs aprovados e vigentes
```

**485 → 488 linhas *(+3)* · 6 blocos de diff · 4 linhas acrescentadas · 3 substituidas.**

### 2.2 O que o diff de `FND-01` **nao** contem

| Nao contem | Verificacao |
|---|---|
| Nivel novo na hierarquia | **8 antes, 8 depois.** O nivel 2 recebe **um membro** |
| Reordenacao de niveis | **Zero** — a ordem `1..8` e literalmente identica |
| Alteracao da **regra de precedencia interna do nivel 2** | **Zero linhas tocadas** — o paragrafo *"Precedencia interna do nivel 2 (acrescentada por ADR-0003)"* permanece **byte a byte** |
| Alteracao em **§4** *(Principios Imutaveis)* | **Zero** |
| Alteracao em **§6.2** *(portoes)* | **Zero** — **7 portoes antes, 7 depois** |
| Alteracao em **§7.3** *(direitos de decisao)* | **Zero linhas tocadas** |
| Alteracao em **§8** *(Linhas Vermelhas)* | **Zero** |
| Alteracao em **§9** *(Emenda Constitucional)* | **Zero** — o rito nao muda; **e cumprido** |
| Excecao formal | **Zero** — `governance/exceptions/` permanece **vazio** |

### 2.3 `FND-03` **1.5.0 → 1.6.0**

| # | Local | Antes | Depois |
|---|---|---|---|
| **B1** | frontmatter, linha 5 | `versao: 1.5.0` | `versao: 1.6.0` |
| **B2** | frontmatter, linha 12 | `atualizado_em: 2026-07-28` | `atualizado_em: 2026-07-29` |
| **B3** | frontmatter, linha 14 | `decisoes_relacionadas: [..., ADR-0010]` | `[..., ADR-0010, ADR-0022]` |
| **B4** | **§7**, arvore, apos `10-artifact-framework.md` | *(inexistente)* | `│   ├── 11-framework-specifications.md` |
| **B5** | Historico, ao final | *(inexistente)* | linha `1.6.0`, descrevendo `B1`–`B4` |

**631 → 633 linhas *(+2)* · 5 blocos de diff.**

**O que o diff de `FND-03` nao contem:** **§3.6** *(a `Spec` vive em `products/<slug>/specs/`,
sequencia por produto)* — **zero linhas tocadas**; **§7.1** *(um artefato existe em exatamente um
lugar)* — **zero**; qualquer identificador, estado, versao, diretorio, tipo documental ou termo
novo — **zero**.

### 2.4 `FND-11` **1.0.0** — criacao

**Arquivo novo: nao ha diff, ha conteudo.** **399 linhas**, `LF`, perfil `sob-demanda`, forma
documental **Framework**, entidade `FND`, mutabilidade **`M2`**.

**A prova de que as 32 regras migraram sem alteracao silenciosa — `diff` entre o bloco de origem
e o de destino:**

| Metrica | Valor |
|---|---|
| Bloco de origem — `ADR-0021 §5.1`–`§5.10` | **157 linhas** |
| Bloco de destino — `FND-11 §3`–`§12` | **157 linhas** |
| **Blocos de diff** | **14** |
| — cabecalho de secao *(`### 5.N` → `## N`)* | **10** |
| — metodo de atualizacao das duas declaracoes `PJ-02` | **2** |
| — `SF-05`, **referencial** *(`"este ADR"` → `"este Framework"`)* | **1** |
| — `SF-32`, **merito declarado** | **1** |
| **Blocos de diff nas outras 30 regras** | **`0`** |
| **Identificadores renumerados** | **`0` de 32** |

**A unica alteracao de merito, texto integral do antes e do depois:**

```
antes  (ADR-0021 SF-32, fim da regra):
  **Este ADR e superavel por ADR que o referencie** (`CC-06`, `SU-01`); ele **nao se emenda**
  (`AC-10`, `CC-01`).

depois (FND-11 SF-32, fim da regra):
  **Este Framework e artefato `M2`** (`FND-10 §6.2`): emenda-se **por versao**, com o texto
  anterior **preservado no historico**, pela **classe do efeito** (`AL-01`, `CC-02`), e a
  emenda **so vigora com aprovacao e ratificacao do SOBERANO** (`FND-09 §8.2` linha `FND`;
  `LM-02`). **A clausula de imutabilidade de `M1` da sede anterior nao se transporta** — e a
  **unica alteracao de merito** desta promocao, declarada em §2 e em ADR-0022.
```

> **O sentido do tradeoff, para que o ato o conheca.** Sob `M1`, corrigir uma regra `SF-*`
> custava **1 ADR `C2 · Tipo 2` e nenhum ato do Soberano**. Sob `M2`, custa **1 emenda e 1 ato
> do Soberano**. **Ratificar isto encarece a manutencao da norma e a protege — nao o contrario.**

## 3. O alcance da sucessao de `ADR-0021` — **parcial, e `ADR-0021` nao e tocado**

| O que | Estado apos o ato |
|---|---|
| Sede normativa de `SF-01` a `SF-32` | **SUPERADA** por `FND-11`. Em divergencia, prevalece `FND-11` — nivel 2 contra nivel 3 (`FND-01 §10`) |
| `status` de `ADR-0021` | **`ativo`, inalterado** |
| Fechamento de `RD-23` e `TPL-spec` **1.1.0** | **VIGENTES, nao superados** |
| Os 12 casos de determinismo de `ADR-0021 §9` | **VIGENTES** como registro historico |
| Texto e frontmatter de `ADR-0021` | **`0` bytes · `0` campos.** `H-A` permanece `cafd28fb…bbc1` |

**Onde a sucessao fica legivel:** `ADR-0022 supera: [ADR-0021]` · `FND-11 §15` ·
[`decisions/README`](../decisions/README.md) · [catalogo mestre §6](artifact-registry.md).
**Quatro lugares permanentes.**

### 3.1 A alternativa de `Q3`, **medida — e ela tem um preco que a leitura nao mostrava**

Grava-se `superado_por: ADR-0022-…` no frontmatter de `ADR-0021`?

| Objeto | Linhas | `H-A` / `H-P` | `H-N` |
|---|---|---|---|
| **`ADR-0021` em vigor** | 573 | `cafd28fbd656b87618c355ad075f36bb02eca0d3c6b2f4040a5206ac9739bbc1` | `511ace984d5a183f29bbe18c29a2fe1b7c8892533356dfba8ac8f78bbf1c5316` |
| **`ADR-0021` com `superado_por`** | 573 | `eddd6a69324019a4cb3fcf41a5529344e4091cfc10cff76d91a1427f9c8daa1f` | **`09814377463a6fc4e997fcbd4fe78bef7091e513e703dccdb9dc0b48198b89a6`** |

**O `H-N` MUDA — e essa e a informacao decisiva.** A causa e uma **assimetria de `IR-03`**: a
lista fechada exclui **`substituido_por`** de `H-N` e **nao exclui `superado_por`**. Logo, para
um `ADR`, **o unico campo de sucessao que o frontmatter oferece e, por definicao de `IR-02`,
conteudo normativo** — e alterar conteudo normativo de artefato `M1` e o que **`LV-04`** proibe.

**Achado `RD-43`**, severidade **Media**, dono **DEP-GOV**, gatilho *"proxima superacao de
`ADR`"*. **Alterar `IR-03` e `C2` com ADR** (`IR-04`) e **nao e materia deste pacote**.

**Recomendacao: NAO gravar.** O pacote publica o `H-P` da alternativa **para que a escolha seja
possivel**, nao para que seja tomada.

## 4. Identificadores de integridade

### 4.1 Objetos em vigor e candidatos

| Objeto | Versao | Linhas | `H-A` | `H-N` |
|---|---|---|---|---|
| **`FND-01` em vigor** | 1.5.0 | **485** | `2d962616ebd1b1e952eac1f3c98873385d32d26160d7e8f3f9e2c82de7ac310d` | `fcb6e4bd5dd2e8d59c5f8038d0f85b2fdc1239fe78f7be5439bf640779536198` |
| **`FND-01` candidato `V1`** | **1.6.0** | **488** | **`acec800b4e6e25c7882827c0bcb8f260f6984034741c1bf9ce954a7e37b0a3a8`** | `b63c279086ef90ac8565d03c01de19d116fda7b595aeceb0e66a3e816f35309f` |
| **`FND-01` candidato `V2`** *(alternativa — §5)* | **1.6.0** | **492** | **`43cae80014f3cb9d1a1f64d73df53a1196e7961d1e63454f89049f45dbd96767`** | `afbb90524da0b4f5a242d4ebceccb10999a73b616bb811c6ed8b092ed1b1420b` |
| **`FND-03` em vigor** | 1.5.0 | **631** | `ad1b47bde9e31a29e445c5a7b8c7cace05a302e1b10a6348ef1153bb386f33a6` | `7ec1dcb75a6436c552b37fe4c57a70105bd2d2828d9f749d3d157ea41884a085` |
| **`FND-03` candidato** | **1.6.0** | **633** | **`82694fad45f3de1ff1e93b6cfc81bd570d7d087e63374f46a2ba69800286b959`** | `1004673a5d01941560d073c022849cea17bb074caf010c48e8fa7b1062424b4e` |
| **`FND-11` candidato** | **1.0.0** | **399** | **`4b5620f9cad1213350633f88893dfe3384ecb461955881e74da8f559d06ee6c6`** | `90f4efb74e2d2573e9f4fdf69db43e3da863f3b1e09926febe22517f32ca79ee` |

**`H-P` de `FND-01` e `FND-03` = `H-A`** — a promulgacao **nao executa `O4`** sobre eles: os dois
ja estao `ativo` e `ratificada`.

**`H-P` de `FND-11`, apos `O4`** *(`status: em-revisao → ativo`; `ratificacao: pendente →
ratificada`)*: **`383ee51df8ee8782a693897f07423529bc4dd5a7d866603ad31e61fe06ad7c20`**.
**`H-N` invariante sob `O4` — verificado** (`IR-02`, `IR-06`).

### 4.2 `ADR-0022` e `RFC-0018`

| Objeto | Caminho · versao · linhas | `H-A` | `H-N` | `H-P` projetado |
|---|---|---|---|---|
| **`ADR-0022`** | `decisions/ADR-0022-sede-canonica-do-framework-de-specifications.md` · **1.0.0** · **438** | **`f02fbaf78e1627ecf9b819cb33f7da9760e65b69c16e34ee88e79f38ab513810`** | `a6f954c304496041199c8c80c666d36016337aab3e26f3d745390b288f7e0316` | **`2dd4d591bf8051845ee9985d459a9fa69c196a4482c6fd3d2f262a02005b4a05`** |
| **`RFC-0018`** | `rfcs/RFC-0018-sede-canonica-do-framework-de-specifications.md` · **1.0.0** · **262** | `1745f5124e21a656b83385889d45dd6664217868c31791a122afeaf48770e55a` | — | — |

**Estado de `ADR-0022` hoje:** `em-revisao` · `ratificacao: pendente`. **`H-N` invariante sob
`O4` — verificado.**

### 4.3 Metodo de medicao — **reimplementacao validada antes do uso**

`IR-02` e `IR-03` foram **reimplementados de forma independente** e **validados primeiro contra
artefatos com hash ja publicado**, antes de medir qualquer candidato:

| Artefato de controle | Valor esperado, e onde foi publicado | `H-A`/`H-P` | `H-N` |
|---|---|---|---|
| `FND-01` **1.5.0** | [PS-2026-007 §3](pacote-soberano-2026-07-29-rd-14.md) | ✅ | ✅ |
| `ADR-0018` **pos-`O4`** | [PS-2026-007 §3.1](pacote-soberano-2026-07-29-rd-14.md) — `H-P` projetado | ✅ | ✅ |
| `RFC-0014` | [PS-2026-007 §3.2](pacote-soberano-2026-07-29-rd-14.md) | ✅ | — |
| `DEP-QAR` **1.2.0** | [MSG-2026-0005 §2](../memory/operacional/MSG-2026-0005-ato-soberano-aplicacao-dep-qar.md) — `H-P` aplicado | ✅ | ✅ |

**7 de 7 reproduzem, digito a digito** — em **quatro** tipos documentais *(`FND`, `ADR`, `RFC`,
`DEP`)* e nas **tres** medidas. A medicao dos candidatos so ocorreu **depois**.

### 4.4 Onde os candidatos vivem — aplicacao de `RD-19`

```
E:\LucasIA\Projetos\_backups\LucaX-Enterprise-OS_2026-07-29_pre-missao-1-13-1\_candidatos\
  fnd-11-1.0.0.md        399 linhas   4b5620f9…e6c6
  fnd-01-1.6.0.md        488 linhas   acec800b…a3a8   (V1 — recomendado)
  fnd-01-1.6.0-V2.md     492 linhas   43cae800…6767   (V2 — alternativa de §5)
  fnd-03-1.6.0.md        633 linhas   82694fad…b959
```

**Os arquivos existem e reproduzem os `H-A` acima**, conferidos **apos** a copia. **Terminadores:
`LF` em todos**, conferido byte a byte; **`0` bytes `CR`**. **Montados por transformacao
programatica do arquivo em vigor**, nunca por reescrita manual — e e essa a razao pela qual as
**30** regras `T-IDENTICA` **podem ser afirmadas byte a byte**.

### 4.5 `IR-09` — teste de reconstrucao

| Objeto | Operacao | Resultado |
|---|---|---|
| `FND-11` | Reverter **apenas** `status` e `ratificacao` no arquivo pos-`O4` e medir | **Reproduz `H-A`** |
| `FND-01`, `FND-03` | Nao se aplica — **nao executam `O4`** | — |
| `ADR-0022` | Reverter **apenas** `status` e `ratificacao` e medir | **Reproduz `H-A`** |

## 5. `RD-27` — a colisao entre a determinacao da missao e um gatilho registrado

> **⚠ SUPERADA na 2.0.0.** A colisao foi **resolvida pelo rito proprio** —
> [ADR-0024](../decisions/ADR-0024-conformidade-de-contrato-das-fundacionais.md). **As duas
> variantes abaixo nao sao mais objetos do ato**; o objeto e `FND-01` **1.7.0 cumulativa**,
> `d3192235…f935b`, em [PS-2026-011 §4.1](pacote-soberano-2026-07-30-rd-27.md). **O texto abaixo
> permanece como registro do que foi submetido em 2026-07-29.**

**Dita literalmente, sem interpretacao:**

| Fonte | Texto |
|---|---|
| **Determinacao da Missao 1.13.1** | *"Nao tratar `RD-27`, `RD-36` ou outros achados neste rito"* |
| **`AC-08`** | Os cinco campos sao obrigatorios em *"artefato criado **ou emendado** a partir da vigencia deste framework"* |
| **Gatilho registrado de `RD-27`** | *"**Proximo ato soberano que alcance `FND-01`, `FND-02` ou `FND-10`**"* — [FIT-2026-014 R2](fitness/README.md) |

**Este ato alcanca `FND-01`. O gatilho de `RD-27` dispara neste ato.** As duas determinacoes
**nao podem ser cumpridas simultaneamente**.

| | `V1` — **objeto submetido** | `V2` — **alternativa medida** |
|---|---|---|
| Os quatro campos de `AC-08` | **ausentes** | **presentes** — `resumo`, `perfil_contexto`, `confidencialidade`, `revisor` |
| Linhas · `H-A` | **488** · `acec800b…a3a8` | **492** · `43cae800…6767` |
| Cumpre a determinacao da missao | **Sim** | **Nao** — trata achado que a missao vedou tratar |
| Efeito sobre `RD-27` | **Terceira ocorrencia** de `FND-01` emendada sem os campos — e **a primeira em que o ato que a repete tinha como nao repetir** | **Fecha `RD-27` quanto a `FND-01`**; `FND-02` permanece aberta |

**Recomendacao: `V1`**, porque a determinacao e do Soberano e o proponente **nao a reinterpreta**.
**`V2` esta pronto, medido e no mesmo diretorio** — escolhe-lo exige **trocar um hash na minuta**,
e nao exige nova missao.

## 6. Independencia dos objetos — a condicao da missao, verificada

**A missao determinou:** *"Os pacotes podem compartilhar um ato somente se cada objeto permanecer
independente, verificavel e bloqueavel isoladamente."*

| Objeto | Independente? | Verificavel? | Bloqueavel isoladamente? |
|---|---|---|---|
| **`ADR-0022` + `FND-11` + `FND-01` + `FND-03`** *(este pacote)* | **Sim** — nao depende de `PS-2026-010` para produzir efeito | **Sim** — `H-A`, `H-N`, `H-P` e diff literal em §2 e §4 | **Sim** — recusar este pacote **nao afeta** as Cartas |
| **`ADR-0023` + `DEP-PRD` + `DEP-EXE`** *([PS-2026-010](pacote-soberano-2026-07-29-rd-31.md))* | **Sim** — as Cartas propagam `ADR-0018`/`ADR-0019`, **nao** `ADR-0022` | **Sim** | **Sim** — recusar aquele pacote **nao afeta** `FND-11` |

**A prova da independencia e textual:** **nenhuma linha dos candidatos `DEP-PRD` e `DEP-EXE` cita
`FND-11` ou `ADR-0022`**, e **nenhuma linha de `FND-11` cita as Cartas** — verificavel por `grep`.
**A ordem entre os dois pacotes e indiferente**; se ambos forem aprovados no mesmo ato, aplica-se
`PS-2026-009` primeiro apenas por conveniencia de indice.

## 7. Impacto — a verificacao que importa

| Verificacao | Resultado | Evidencia |
|---|---|---|
| **Regras com merito alterado** | **1 de 32** — `SF-32`, **declarada** | §2.4 |
| **Regras identicas byte a byte** | **30 de 32** | §2.4 — `0` blocos de diff |
| **Identificadores renumerados** | **`0` de 32** | §2.4 |
| **Titulares criados** | **ZERO** | `SF-10` **remete** a `FND-04 §2`; `0` celulas de `FND-09 §8.2` tocadas |
| **Portoes** | **7 antes · 7 depois · 0 criados · 0 removidos** | §2.2 |
| **Niveis da hierarquia normativa** | **8 antes · 8 depois.** O nivel 2 passa de **9** para **10** membros | §2.2 |
| **Direitos de decisao de `FND-01 §7.3`** | **ZERO alterados** | §2.2 |
| **Principios Imutaveis · Linhas Vermelhas** | **ZERO alterados** | §2.2 |
| **Entidades · tipos documentais · papeis · classes · verbos de autoridade** | **0 criados · 0 alterados** | `FND-09 §11.1` |
| **Vinculo `Spec` × `Produto`** | **ZERO bytes** em `FND-03 §3.6`, `FND-04 §6` e `FND-10 §4.4`. **`RD-33` permanece aberto e BLOQUEANTE** | §2.3 |
| **Fundacionais NAO tocadas** | **8 de 10** — `FND-02`, `FND-04` a `FND-10` | `sha256` inalterado |
| **`TPL-spec`** | **ZERO bytes** — permanece **1.1.0** | — |
| **Cartas alteradas** | **ZERO** | — |
| **Artefatos `M1` editados** | **ZERO** — inclusive `ADR-0021` | §3 |
| **Excecoes formais** | **ZERO criadas** | `governance/exceptions/` vazio |
| **Custo de contexto** | **+399 linhas** `sob-demanda` · **+3** em `FND-01` · **+2** em `FND-03`. **O consumidor da norma da `Spec` paga o mesmo que pagava** — `ADR-0021` era `sob-demanda` e `FND-11` tambem e | `CE-02` |
| Reversibilidade | **Tipo 1** — reversao barata **hoje**, e **exige novo ato** | [ADR-0022 §11](../decisions/ADR-0022-sede-canonica-do-framework-de-specifications.md) |

## 8. Risco residual

| # | Risco | Sev. | Mitigacao declarada |
|---|---|---|---|
| **RS-1** | **Duas sedes coexistirem** — alguem aplica `SF-*` lendo `ADR-0021` | Media | **`RD-40`**, declarado. Merito identico em **31 de 32**; em `SF-32` a leitura sera errada. Resolve pela hierarquia: `FND-11` e nivel 2 |
| **RS-2** | **`FND-01` emendada sem `AC-08`** | **Alta** | **`V2` existe e esta medido** (§5). **Nao ha versao deste ato que evite a colisao — so ha versao que a declare** |
| **RS-3** | **A promocao ser lida como reabertura do merito** | Media | §2.4: **`0` blocos de diff em 30 regras**, medido por ferramenta, nao por leitura |
| **RS-4** | **`Tipo 1` ser contestado como excessivo** | Media | Declarado como **duvida resolvida pela regra mais restritiva** (`GV-03`, `FND-01 §7.1.6`), e escalado como `Q1` |
| **RS-5** | **Ato nao vir** | Media | `ADR-0021` permanece **vigente e intacto**: a norma **nao fica sem sede**. **Nenhum bloqueio novo** |
| **RS-6** | **Autoria concentrada em DEP-GOV** | **Observada** | **`RD-39`.** Determinada por `FND-09 §8.2`; **DEP-PRD e consulta obrigatoria** |

## 9. Minuta do ato — **pronta, com os valores verificados**

> ### Esta secao **nao e um ato**. Nada aqui produz efeito.
>
> **⚠ SUPERADA na 2.0.0.** **A minuta unica do ato esta em
> [PS-2026-013](pacote-soberano-2026-07-30-consolidado.md)**, que enumera integralmente os
> **catorze** objetos. A minuta abaixo **enumera `FND-01` 1.6.0, que nao existira**, e permanece
> **apenas como registro** do que foi submetido em 2026-07-29. **`Q2` de §9.1 esta resolvido**
> pelo rito proprio; **`Q1` e `Q3` seguem vivos** e foram **decididos pelo Soberano** na Missao
> 1.13.2 — `Tipo 1` mantido, `superado_por` **nao** gravado.

```
ATO SOBERANO DO FUNDADOR — <data do ato>

Apos revisar governance/pacote-soberano-2026-07-29-fnd-11.md, RFC-0018, ADR-0022,
o candidato FND-11, os diffs literais, as evidencias, a revisao independente, os
riscos e as ressalvas:

Aprovo e ratifico expressamente:

- ADR-0022, versao 1.0.0,
  SHA-256 f02fbaf78e1627ecf9b819cb33f7da9760e65b69c16e34ee88e79f38ab513810.

Autorizo a promulgacao de:

- FND-11, versao 1.0.0,
  SHA-256 4b5620f9cad1213350633f88893dfe3384ecb461955881e74da8f559d06ee6c6,
  cujo SHA-256 apos a transicao de estado devera ser
  383ee51df8ee8782a693897f07423529bc4dd5a7d866603ad31e61fe06ad7c20;

- FND-01, versao 1.6.0,
  SHA-256 acec800b4e6e25c7882827c0bcb8f260f6984034741c1bf9ce954a7e37b0a3a8;

- FND-03, versao 1.6.0,
  SHA-256 82694fad45f3de1ff1e93b6cfc81bd570d7d087e63374f46a2ba69800286b959,

exatamente nos diffs literais registrados em PS-2026-009 §2.

A entrada em vigor depende de verificacao independente de identidade, versao, hash
integral, diff literal, revisao e inexistencia de alteracao entre o candidato revisado
e o objeto a ser aplicado. FND-01 1.5.0 e FND-03 1.5.0 deverao permanecer recuperaveis
como versoes historicas substituidas.

Este ato nao cria titular, portao, papel, classe, verbo de autoridade, entidade ou
tipo documental novo; nao altera direito de decisao de FND-01 §7.3, principio imutavel,
linha vermelha ou nivel da hierarquia normativa; nao altera o vinculo entre Spec e
Produto, a sequencia por Produto ou os locais canonicos; nao emenda FND-02, FND-04 a
FND-10, TPL-spec nem Carta alguma; nao edita ADR-0021, artefato historico, MSG, FIT ou
baseline; nao alcanca RD-27, RD-31, RD-33, RD-36 nem qualquer outro achado; e nao
alcanca qualquer objeto nao enumerado expressamente.
```

### 9.1 As tres escolhas que o ato pode fazer diferente

| # | Escolha | Como se expressa no ato |
|---|---|---|
| **Q1** | Classificar como **`Tipo 2`** em vez de `Tipo 1` | Declaracao expressa no ato. **Nao altera nenhum hash** |
| **Q2** | Promulgar **`FND-01` `V2`**, fechando `RD-27` quanto a `FND-01` | Trocar o `SHA-256` de `FND-01` por `43cae80014f3cb9d1a1f64d73df53a1196e7961d1e63454f89049f45dbd96767` e declarar que o ato **alcanca `RD-27` quanto a `FND-01`** |
| **Q3** | Autorizar a gravacao de `superado_por` em `ADR-0021` | Autorizar expressamente, com o `H-P` `eddd6a69324019a4cb3fcf41a5529344e4091cfc10cff76d91a1427f9c8daa1f` — **e declarar que o ato altera o `H-N` de um artefato `M1`**, o que `LV-04` de outro modo proibiria. **Nao recomendado** (§3.1) |

## 10. Recomendacao

| Campo | Conteudo |
|---|---|
| **Recomendacao** | **APROVAR**, na variante **`V1`**, sem a gravacao de `Q3` |
| **Fundamento** | A **forma documental correta ja esta escrita** em `FND-10 §4.1` e **nao estava sendo usada**; a migracao e **provada por ferramenta** — `0` blocos de diff em **30 de 32** regras e `0` identificadores renumerados —; a **unica alteracao de merito esta isolada, nomeada tres vezes e submetida em separado**; e **`0` Specs existem**, logo **`0` migram** e o custo de reversao e **o menor que jamais sera** |
| **Contrapartida honesta** | **Tres.** *(i)* A correcao de qualquer regra `SF-*` passa a **exigir ato do Soberano** — a promocao **encarece**, e protege. *(ii)* **`FND-01` sera emendada sem os quatro campos de `AC-08`** se `V1` for escolhido — terceira ocorrencia de `RD-27`, **declarada**. *(iii)* **`ADR-0021` nao dira que foi superado** — `RD-40`, e a alternativa **altera `H-N` de artefato `M1`** |
| **O pacote informa; nao decide** | **Nao decidir e resultado valido.** O efeito de nao decidir esta em §1: `ADR-0021` continua vigente, e **nenhum bloqueio novo aparece** |

## 11. Rastreabilidade

| Campo | Conteudo |
|---|---|
| RFC → ADR | [RFC-0018](../rfcs/RFC-0018-sede-canonica-do-framework-de-specifications.md) → [ADR-0022](../decisions/ADR-0022-sede-canonica-do-framework-de-specifications.md) |
| Decisao superada **parcialmente** | [ADR-0021](../decisions/ADR-0021-framework-de-specifications.md) — **so a sede**; `status` inalterado, texto intacto |
| Achados que abre | **`RD-38`** *(corrigido por `A4`)* · **`RD-39`** *(declarado)* · **`RD-40`** *(declarado)* · **`RD-43`** *(declarado — encontrado por medicao, §3.1)* |
| Achado que **nao** fecha | **`RD-33`** — o vinculo `Spec` × `Produto`, **integralmente vigente** |
| Regra de integridade | [ADR-0012](../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md), `IR-01` a `IR-10` |
| Pacote irmao, **nao alcancado por este** | [PS-2026-010](pacote-soberano-2026-07-29-rd-31.md) — `RD-31` |
| Relatorio da missao | [PT-2026-008](relatorio-transicao-2026-07-29-canonizacao.md) |
| Verificacao de aptidao | [FIT-2026-016](fitness/FIT-2026-016-canonizacao-e-propagacao.md) |
| Baseline vigente na submissao | **`BL-2026-07-29-09`** — [catalogo mestre §10](artifact-registry.md) |

---

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| **2.0.0** | **2026-07-30** | **DEP-GOV** | **Emenda MAIOR pela Missao 1.13.2 — o objeto `FND-01` deste pacote e substituido, e nenhum outro muda.** Instituido o **rito proprio de `RD-27`** *(`RFC-0020` → `ADR-0024` → `PS-2026-011`)*, **`FND-01` passou a ser alcancado por dois ritos**, e a determinacao da missao e que **exista apenas um `FND-01` final para o ato**. As **duas variantes** que §5 submetia — `V1` `acec800b…a3a8` e `V2` `43cae800…6767` — **deixam de ser objetos** e sao **remetidas ao candidato cumulativo `FND-01` 1.7.0, `d3192235…f935b`**, publicado em [PS-2026-011 §4.1](pacote-soberano-2026-07-30-rd-27.md). **`V1` sai porque nao fecha `RD-27`** e a determinacao que o recomendava foi substituida; **`V2` sai porque contem `RD-45`** — a sua linha de historico atribui a **`ADR-0022`** o backfill de `AC-08` que o **escopo literal de `ADR-0022` exclui** em `J14` e §7.3, e `ADR-0022` e **`M1`**, logo **nao poderia ser corrigido para concordar**. **Nada mais deste pacote muda:** `FND-11` `4b5620f9…e6c6`, `FND-03` `82694fad…b959` e `ADR-0022` `f02fbaf7…3810` permanecem **com os mesmos hashes**, e **§4.1 nao e reescrito** — os valores ali registram o que foi submetido em **2026-07-29**, e essa e a funcao deles. **A 1.0.0 esta preservada integral e nao editada** *(446 linhas, `H-A` `e349b4fb…c3be`, medido antes de qualquer edicao)*. **Nenhum objeto entrou em vigor por esta emenda; nenhum candidato foi apagado; nenhum hash historico foi reescrito.** |
| 1.0.0 | 2026-07-29 | DEP-GOV | Pacote da **Missao 1.13.1**: emenda **C3 · Tipo 1** que **cria `FND-11`** *(399 linhas)* como sede fundacional de `SF-01` a `SF-32` e emenda **`FND-01`** *(485 → 488)* e **`FND-03`** *(631 → 633)*, com **diff literal item a item**, o **bloco de §10 reproduzido integralmente antes e depois**, `H-A` e `H-N` integrais de base e candidatos, **`H-P` projetado** de `FND-11` e do `ADR`, `IR-09` executado e **minuta preenchida**. **Setimo pacote soberano.** **A equivalencia das 32 regras e provada por ferramenta, nao por leitura:** `14` blocos de diff, dos quais `10` de cabecalho, `2` de metodo de atualizacao, `1` referencial em `SF-05` e `1` de merito em `SF-32` — **`0` blocos nas outras 30** e **`0` de 32 identificadores renumerados** —, e o antes/depois de `SF-32` esta **reproduzido integralmente**. §3 declara que a sucessao de `ADR-0021` e **PARCIAL** e que o artefato **nao e tocado**; **§3.1 mede a alternativa de `Q3` e descobre que gravar `superado_por` ALTERA o `H-N`**, porque `IR-03` exclui `substituido_por` e **nao exclui `superado_por`** — achado **`RD-43`**, encontrado **por exercer o instrumento**. §5 declara a **colisao entre a determinacao *"nao tratar `RD-27`"* e o gatilho registrado de `RD-27`, que este proprio ato dispara**, e publica **duas variantes do candidato `FND-01` com hash**, recomendando a que cumpre a determinacao. §6 verifica a condicao da missao — **independencia dos objetos** — por prova textual: **nenhuma linha dos candidatos de Carta cita `FND-11` ou `ADR-0022`, e nenhuma linha de `FND-11` cita as Cartas**. §4.3 registra que `IR-02` e `IR-03` foram **reimplementados e validados contra 7 controles publicados, em 4 tipos documentais**, **antes** de medir qualquer candidato. **`0` titulares · `0` portoes · `0` papeis · `0` classes · `0` verbos · `0` entidades · `0` tipos documentais criados · 8 niveis de hierarquia antes e depois · `0` bytes no vinculo `Spec` × `Produto` · `0` artefatos `M1` editados · `0` Cartas alteradas · 8 de 10 fundacionais intocadas.** |
