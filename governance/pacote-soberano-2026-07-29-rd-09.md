---
id: PS-2026-005
titulo: Pacote de decisao soberana — emenda C3 a FND-09 §8.2 e FND-10 §10.3 que fecha RD-09
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
decisoes_relacionadas: [ADR-0012, ADR-0015, ADR-0017]
substitui: []
substituido_por: null
canal: REPORTE
emissor: DEP-GOV
destinatario: SOBERANO
ttl: ate decisao do Soberano
resumo: Submete ao Soberano a emenda C3 que alinha a linha Fitness Check de FND-09 §8.2 e FND-10 §10.3 a regra vigente FT-10, com diff literal, hashes e verificacao de que nenhum titular e ampliado.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# PS-2026-005 — Emenda **C3** a FND-09 §8.2 e FND-10 §10.3

> ## Este pacote **informa**. Nao decide, nao aprova, nao promulga e nao edita nada.
>
> **FND-09 permanece em 1.3.0 e FND-10 em 1.2.0.** Os candidatos **1.4.0** e **1.3.0** existem
> como **diff literal + hash**, **fora do acervo**.
>
> **Pacote separado de [PS-2026-004](pacote-soberano-2026-07-29-rd-02.md), por determinacao.**
> RD-02 e RD-09 sao materias distintas e **nao se misturam num ato**.
>
> **Caminho exato:** `governance/pacote-soberano-2026-07-29-rd-09.md` *(RE-01)*.

## Proposito
Levar ao Soberano a emenda que fecha **RD-09**: duas fundacionais em vigor declaram
*"Ratifica: SOBERANO se C3"* para `Fitness Check`, e a regra vigente — **`FT-10`** — diz o
contrario.

## Escopo
| Item | Definicao |
|---|---|
| Inclui | **Um** objeto: `ADR-0017` e a promulgacao de **FND-09 1.4.0** *(fonte)* e **FND-10 1.3.0** *(cascata, CV-04)* |
| **Nao** inclui | **RD-02** — [PS-2026-004](pacote-soberano-2026-07-29-rd-02.md) · `DEP-KMS`/`DEP-ENG` — [PS-2026-006](pacote-soberano-2026-07-29-kms-eng.md) · o **merito** de `FT-10`, ja decidido em ADR-0015 · `Revisao Arquitetural` · **FND-04 §2.1** *(RD-12)* · qualquer `FIT` historico *(`FT-15`)* |
| Natureza | **Reporte**, entidade `MSG`. **Nenhum** tipo, entidade, camada, template ou diretorio novo |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| **Autor da emenda** | **DEP-GOV** | FND-09 §8.2, linha `FND` |
| **Revisor independente** | **DEP-QAR** | RM-06b |
| **DECIDE** | **SOBERANO** | **C3. Indelegavel.** Nao ocorreu |

> **Residuo declarado (PI-10).** **DEP-QAR e autor de todo `FIT`** e, portanto, **objeto da linha
> alterada**. O que muda para DEP-QAR e **nada**: os **dez** `FIT` do acervo ja declaram
> `ratificacao: nao-exigida`, e **`FT-14`** preserva integralmente o efeito do veredito `inapto`.
> Residuo **de posicao, nao de interesse** — declarado, nao suprido.

---

## 1. O que se pede

| # | Objeto | Ato pedido | Se **nao** houver ato |
|---|---|---|---|
| **1** | **`ADR-0017`** + promulgacao de **`FND-09` 1.4.0** e **`FND-10` 1.3.0** | **Aprovacao e ratificacao** | As duas permanecem em 1.3.0 e 1.2.0. **`FT-10` prevalece** e **duas fundacionais seguem declarando o contrario dela**. RD-09 envelhece |

> **Aprovacao parcial e desaconselhada com fundamento.** FND-10 §10.3 **declara-se projecao** de
> FND-09 §8.2; ratificar so a fonte deixaria a projecao contradizendo o documento de que ela
> propria diz derivar — **estado pior que o atual** (RFC-0013 §8, D2).

## 2. Diff literal

### 2.1 `FND-09` 1.3.0 → **1.4.0** — a **fonte**

| # | Local | Antes | Depois |
|---|---|---|---|
| **N1** | frontmatter | `versao: 1.3.0` | `versao: 1.4.0` |
| **N2** | frontmatter | `atualizado_em: 2026-07-28` | `atualizado_em: 2026-07-29` |
| **N3** | frontmatter | `decisoes_relacionadas: [ADR-0001, ADR-0002, ADR-0003, ADR-0004, ADR-0005, ADR-0006, ADR-0008]` | `[..., ADR-0008, ADR-0017]` |
| **N4** | **§8.2**, linha `FIT`, coluna *Ratifica* | `SOBERANO se C3` | **`—` *(`FT-10`)*** |
| **N5** | **§8.2**, apos a matriz, antes de §8.3 | *(inexistente)* | Nota normativa de **6 linhas** + linha em branco *(texto integral em §2.3)* |
| **N6** | Historico de versoes | *(inexistente)* | linha `1.4.0`, descrevendo N1 a N5 |

**A linha `FIT`, integral, antes e depois:**

```
antes:  | FIT | DEP-QAR | DEP-GOV (forma) | DEP-EXE | SOBERANO se C3 | nao se aposenta — e historico |
depois: | FIT | DEP-QAR | DEP-GOV (forma) | DEP-EXE | **—** *(`FT-10`)* | nao se aposenta — e historico |
```

**Colunas *Propoe/cria*, *Revisa* e *Aprova* inalteradas. Nenhuma outra das 21 linhas tocada.**
**1.243 → 1.252 linhas *(+9)* · 13 acrescentadas · 4 substituidas · 6 blocos de diff.**

### 2.2 `FND-10` 1.2.0 → **1.3.0** — a **cascata**

| # | Local | Antes | Depois |
|---|---|---|---|
| **P1** | frontmatter | `versao: 1.2.0` | `versao: 1.3.0` |
| **P2** | frontmatter | `atualizado_em: 2026-07-28` | `atualizado_em: 2026-07-29` |
| **P3** | frontmatter | `decisoes_relacionadas: [ADR-0003, ADR-0005, ADR-0006, ADR-0007, ADR-0008, ADR-0009]` | `[..., ADR-0009, ADR-0017]` |
| **P4** | **§10.3**, linha `Fitness Check`, coluna *Ratifica* | `SOBERANO se C3` | **`—` *(`FT-10`)*** |
| **P5** | **§10.3**, apos a matriz, antes da nota da coluna Local | *(inexistente)* | Nota de **5 linhas** + linha em branco *(texto integral em §2.3)* |
| **P6** | Historico de versoes, **ao final** | *(inexistente)* | linha `1.3.0`, descrevendo P1 a P5 |

**A linha `Fitness Check`, integral, antes e depois:**

```
antes:  | Fitness Check | DEP-EXE | SOBERANO se C3 | **M1** | `missao` |
depois: | Fitness Check | DEP-EXE | **—** *(`FT-10`)* | **M1** | `missao` |
```

**`Revisao Arquitetural` ja declarava `—` e nao muda. Nenhum dos outros 24 tipos documentais
tocado.**
**764 → 771 linhas *(+7)* · 11 acrescentadas · 4 substituidas · 6 blocos de diff.**

> **Nota sobre a posicao de P6.** O historico de FND-10 **ja estava fora de ordem** na versao em
> vigor — `1.1.0` figura **depois** de `1.2.0`. A linha nova foi anexada **ao final**, para que a
> ultima linha seja a mais recente, como em todos os demais artefatos. **A desordem preexistente
> nao foi corrigida:** o texto esta **dentro de `H-N`** de uma fundacional ratificada, e
> corrigi-la seria alteracao nao ratificada (IR-01). Achado **RD-13**, severidade **Baixa**, dono
> **DEP-GOV**, gatilho *"proxima emenda a FND-10"*.

### 2.3 As duas notas, texto integral

**N5 — em FND-09 §8.2:**

> **Sobre a linha `FIT`.** `Fitness Check` e `Revisao Arquitetural` sao **pareceres**, nao
> artefatos de decisao, e **nao se ratificam** — regra **`FT-10`** de ADR-0015. A ratificacao
> incide sobre **a mudanca avaliada**, nunca sobre o parecer que a avalia (`FT-11`). O efeito
> do veredito `inapto` e **processual** e independe de ato do Soberano (`FT-14`). **Nenhum
> titular foi ampliado por esta alteracao: uma materia saiu da mesa do ratificador, e nenhuma
> entrou.**

**P5 — em FND-10 §10.3:**

> **A linha `Fitness Check` acompanha a fonte.** A coluna **Ratifica** desta matriz e projecao
> de FND-09 §8.2 (PJ-02); a alteracao ali e **fonte**, e esta e **cascata** (CV-04). O
> fundamento e **`FT-10`** de ADR-0015: parecer nao se ratifica. `Revisao Arquitetural` **ja**
> declarava `—` e **nao muda**.

## 3. Identificadores de integridade

| Objeto | Versao | Linhas | `H-A` | `H-N` |
|---|---|---|---|---|
| **`FND-09` em vigor** | 1.3.0 | **1.243** | `711709a7f6fa71f07818c7f646922f6b4bda1067e844300a4f049f2744ce2ddd` | `093a49626ecd2fbfdfa0e3e21d90e634a66479095f5eb1401e788333f8d36183` |
| **`FND-09` candidato** | **1.4.0** | **1.252** | **`e172c3ea545ab6187048e02704eb8cd3dcb340564484a2d57070d3c4bf3bd519`** | `755170116f52ab756bfdfe12c52b813f66e4e55baf6dddcc8ce0605ffea7b5d2` |
| **`FND-10` em vigor** | 1.2.0 | **764** | `acba465671d3fbae08653dd87b478bc576c30a80ada0a93aa6adf5c114f157e3` | `cd1c6d33b200b9769e8515249731fff9ac33194b5b54fe2af9e3e49b59143c9e` |
| **`FND-10` candidato** | **1.3.0** | **771** | **`ff0611ae5c5e9405643768bd0e80cc28ced32eec25a275b4fb964ad029843105`** | `1de4ab5741d642a50ca66ad08b722f8bc395e32b2730c419085d7816b3c3c75b` |

**`H-P` dos dois fundacionais = `H-A`** — a promulgacao **nao executa O4**.

### 3.1 `ADR-0017` — o objeto que transita de estado

| Campo | Valor |
|---|---|
| Caminho canonico | `decisions/ADR-0017-harmonizacao-do-regime-do-parecer.md` |
| Versao · linhas | **1.0.0** · **228** |
| Estado hoje | `em-revisao` · `ratificacao: pendente` |
| **`H-A`** | **`f812dfda4189858a5a712ead28d62bea39eb122fe3e6b25761fc1cf873388be3`** |
| `H-N` | `e83df30417ffdce6d8dad679187322675b669dacba547514cbc68354a0380f9c` |
| **`H-P` projetado** *(apos O4)* | **`cc8a20738850f4fb52bc70c39ceae7e58b944d28714039961a7c8fef33a8410d`** |
| `H-N` apos O4 | **invariante** (IR-02, IR-06) |

### 3.2 `RFC-0013` — proposta antecedente

| Campo | Valor |
|---|---|
| Caminho · versao · linhas | `rfcs/RFC-0013-harmonizacao-do-regime-do-parecer.md` · **1.0.0** · **178** |
| `H-A` | `130f3d2fdedb6431840f8efc28cd737e3335bfc7ae21c958bf7cd1818293f073` |

> **CRLF declarado.** **`FND-10` usa terminadores `CRLF`**, enquanto FND-02 e FND-09 usam `LF`.
> O candidato **preserva `CRLF` em 771 de 771 linhas**, verificado byte a byte. **Uma primeira
> montagem do candidato converteu os terminadores e foi descartada:** o hash teria mudado o
> arquivo inteiro sem que uma unica linha de norma mudasse. **Registrado porque a proxima
> emenda a FND-10 corre o mesmo risco.**

## 4. Impacto — a verificacao que importa

| Verificacao | Resultado | Evidencia |
|---|---|---|
| **Titulares ampliados** | **ZERO** | Nenhum nome entra na coluna *Ratifica* de nenhuma das duas matrizes |
| **Titulares reduzidos** | **1 materia** — `FIT` sai da coluna *Ratifica* | Por determinacao do **proprio Soberano**, ato de 2026-07-29, item 4 |
| **Parecer convertido em norma** | **ZERO** | **`FT-12`** ja proibe, e nao e tocado |
| **`FIT` historicos editados** | **ZERO** | **`FT-15`** — vedacao expressa |
| **`FIT` que mudam de valor** | **ZERO de 10** | Os dez ja declaram `nao-exigida`. Muda o **fundamento**, nao o valor |
| Efeito de `inapto` | **Inalterado** | **`FT-14`** — processual, independe de ato |
| `Revisao Arquitetural` | **Nao tocada** | Ja declara `—` |
| Outras linhas das matrizes | **20 de 21** em FND-09 · **24 de 25** em FND-10 **inalteradas** | Diff de §2 |
| Cartas alteradas | **ZERO** | — |
| Entidades · tipos · camadas · portoes | **0 criados · 0 alterados** | — |
| Custo de contexto | **+16 linhas.** FND-09 e FND-10 sao **`nucleo` por recorte**, e o recorte alcanca §8.2 e §10.3: **+2 de matriz, +11 de nota, +3 de frontmatter/historico** | FND-10 §2.3 |
| Reversibilidade | **Tipo 2** | ADR-0017 §10 |

## 5. O limite declarado — **RD-12**

**A regra que gerou o defeito nao e corrigida aqui.** FND-09 §8.2 declara-se derivada de
**FND-04 §2 e §6** *"sem redefini-las"*; a celula `FIT · Ratifica · SOBERANO se C3` e a aplicacao
literal da regra geral de **FND-04 §2.1** — *toda mudanca C3 exige ratificacao* — a uma entidade
que **nao e artefato de decisao**.

| Achado | Sev. | Dono | Gatilho |
|---|---|---|---|
| **RD-12** — **FND-04 §2.1 nao distingue artefato de decisao de parecer** | **Media** | DEP-GOV | **Proxima emenda a FND-04** |

> **Corrigir a projecao sem tocar a regra geradora deixa o mecanismo vivo** — e e exatamente a
> licao que FIT-2026-010 gravou ao ver **IC-2 fechar em FND-01 e reaparecer em FND-09 e FND-10**.
> **Aqui a licao esta aplicada na forma de achado declarado, e nao de correcao silenciosa:**
> emendar FND-04 **nao foi pedido, nao foi ratificado e nao sera presumido** (LM-03).

## 6. Minuta do ato — **pronta, com os valores verificados**

> ### Esta secao **nao e um ato**. Nada aqui produz efeito.

```
ATO SOBERANO DO FUNDADOR — <data do ato>

Apos revisar governance/pacote-soberano-2026-07-29-rd-09.md, RFC-0013, ADR-0017,
suas evidencias, revisao independente, riscos e ressalvas:

Aprovo e ratifico expressamente:

- ADR-0017, versao 1.0.0,
  SHA-256 f812dfda4189858a5a712ead28d62bea39eb122fe3e6b25761fc1cf873388be3.

Autorizo a promulgacao das alteracoes correspondentes em:

- FND-09, versao 1.4.0,
  SHA-256 e172c3ea545ab6187048e02704eb8cd3dcb340564484a2d57070d3c4bf3bd519;
- FND-10, versao 1.3.0,
  SHA-256 ff0611ae5c5e9405643768bd0e80cc28ced32eec25a275b4fb964ad029843105,

exatamente no diff literal registrado em PS-2026-005 §2.

A entrada em vigor depende de verificacao independente de identidade, versao, hash
integral, diff literal, revisao e inexistencia de alteracao entre o candidato revisado
e o objeto a ser aplicado. FND-09 1.3.0 e FND-10 1.2.0 deverao permanecer recuperaveis
como versoes historicas substituidas.

Este ato nao amplia titulares, competencias ou direitos decisorios; nao converte
parecer em norma; nao edita nenhum Fitness Check historico; nao alcanca FND-04, RD-02
nem qualquer outro achado; e nao alcanca qualquer objeto nao enumerado expressamente.
```

## 7. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Achado que fecha | **RD-09** — [MSG-2026-0004 §8](../memory/operacional/MSG-2026-0004-ato-soberano-cartas-emenda-constitucional-e-regime-do-fitness-check.md) |
| Ressalva que fecha | **R1** de [FIT-2026-010](fitness/FIT-2026-010-aplicacao-do-ato-soberano.md) |
| Pendencia soberana que fecha | **PS-6** de FIT-2026-010 |
| Achados que **abre** | **RD-12** *(FND-04 §2.1)* · **RD-13** *(historico de FND-10 fora de ordem)* |
| RFC → ADR | [RFC-0013](../rfcs/RFC-0013-harmonizacao-do-regime-do-parecer.md) → [ADR-0017](../decisions/ADR-0017-harmonizacao-do-regime-do-parecer.md) |
| Decisao propagada | [ADR-0015](../decisions/ADR-0015-fitness-check-e-parecer-nao-decisao.md), `FT-10` |
| Regra de integridade | [ADR-0012](../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md) |
| Pacotes irmaos, **nao alcancados por este** | [PS-2026-004](pacote-soberano-2026-07-29-rd-02.md) · [PS-2026-006](pacote-soberano-2026-07-29-kms-eng.md) |
| Relatorio da missao | [PT-2026-002](relatorio-transicao-2026-07-29-fechamento.md) |
| Verificacao de aptidao | [FIT-2026-011](fitness/FIT-2026-011-fechamento-de-autoridade.md) |
| Baseline vigente na submissao | **`BL-2026-07-29-04`** — [catalogo mestre §10](artifact-registry.md) |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-GOV | Pacote da **Missao 1.11**: emenda **C3** a **FND-09 §8.2** *(fonte)* e **FND-10 §10.3** *(cascata)* que fecha **RD-09**, com **diff literal** — **duas celulas** e **duas notas**, texto integral reproduzido —, `H-A`, `H-N`, `H-P` projetado do ADR e **minuta preenchida**. **Zero titulares ampliados · zero pareceres convertidos em norma · zero `FIT` historicos editados · zero `FIT` com valor alterado.** Declara o limite: a regra geradora vive em **FND-04 §2.1** — achado **RD-12** —, e registra **RD-13**, a desordem preexistente do historico de FND-10. Registra tambem que **FND-10 usa `CRLF`** e que uma primeira montagem do candidato converteu os terminadores e foi **descartada**. **Quinto pacote soberano; separado de PS-2026-004 por determinacao.** |
