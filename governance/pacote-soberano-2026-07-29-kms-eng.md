---
id: PS-2026-006
titulo: Reemissao do pacote de decisao soberana sobre as emendas DEP-KMS 1.1.0 e DEP-ENG 1.1.0
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
resumo: Reemite as duas emendas nao ratificadas por identificador invalido, com ID, versao, caminho canonico, linhas, H-A integral, diff literal, versao substituida, revisao independente e prova criptografica de identidade com o candidato revisado.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# PS-2026-006 — Reemissao de `DEP-KMS` 1.1.0 e `DEP-ENG` 1.1.0

> ## Este pacote **informa**. Nao decide, nao aprova, nao ativa e nao edita nenhuma Carta.
>
> **`DEP-KMS` e `DEP-ENG` permanecem em 1.0.0**, `ativo` · `ratificada`. Os candidatos **1.1.0**
> existem como **diff literal + hash**, fora do acervo. **Nenhum arquivo de Carta foi alterado
> por esta missao** — exceto `DEP-QAR`, por ato expresso, e o registro dessa aplicacao esta em
> [MSG-2026-0005](../memory/operacional/MSG-2026-0005-ato-soberano-aplicacao-dep-qar.md).
>
> **Caminho exato:** `governance/pacote-soberano-2026-07-29-kms-eng.md` *(RE-01)*.

## Proposito
**Reemitir** as duas emendas que o ato de 2026-07-29 **nao ratificou por defeito de forma** —
achado **RD-07** —, com todos os campos que a pre-condicao do ato exige, e com **prova de
identidade** entre o objeto submetido agora e o candidato revisado na Missao 1.10.

> **Este pacote nao substitui [PS-2026-003](pacote-soberano-2026-07-29-emendas.md), e nao o
> edita.** PS-2026-003 permanece como **fonte** do merito das tres emendas. Este reune, num
> unico lugar e **com finalidade distinta declarada** — servir de **vinculo do ato** —, os
> identificadores que o ato precisa carregar. E o mesmo desenho que
> [MSG-2026-0004 §2.1](../memory/operacional/MSG-2026-0004-ato-soberano-cartas-emenda-constitucional-e-regime-do-fitness-check.md)
> usou ao republicar os cinco `H-A`, e que **FIT-2026-010 F2** aceitou como **nao duplicacao**.

## Escopo
| Item | Definicao |
|---|---|
| Inclui | **Duas** emendas **MENORES** a Cartas `ativo` · `ratificada`: `DEP-KMS` **1.1.0** *(RC-05)* e `DEP-ENG` **1.1.0** *(RC-07)* |
| **Nao** inclui | `DEP-QAR` 1.2.0 — **ratificada e ja aplicada** · **RD-02** *([PS-2026-004](pacote-soberano-2026-07-29-rd-02.md))* · **RD-09** *([PS-2026-005](pacote-soberano-2026-07-29-rd-09.md))* · o **merito** das duas emendas, que vive em PS-2026-003 §2.1 e §2.2 e **nao foi reaberto** |
| Natureza | **Reporte**, entidade `MSG`. **Nenhum** tipo, entidade, camada ou template novo |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| **Autor das emendas** | **DEP-EXE** | FND-09 §8.2, linha `DEP` — proprietario das nove Cartas |
| **Revisor independente** | **DEP-GOV** | RM-06b — quem e objeto nao revisa. **DEP-KMS e DEP-ENG sao objeto** |
| **Monta e reemite** | **DEP-GOV** | Guardiao normativo; nao produziu as emendas |
| **Revisa este pacote** | **DEP-QAR** | AC-03 |
| **DECIDE** | **SOBERANO** | **Indelegavel** (DC-09). **Nao ocorreu** |

---

## 1. Por que uma reemissao

| Marco | O que ocorreu |
|---|---|
| **PS-2026-003** *(Missao 1.10)* | As tres emendas submetidas com diff literal, `H-A` e `H-N` — os **tres** com 64 caracteres |
| **Ato de 2026-07-29**, item 2 | Enumerou `DEP-QAR` com hash integral e substituiu os de `DEP-KMS` e `DEP-ENG` por **`[INSERIR HASH INTEGRAL DE 64 CARACTERES]`** — **40 caracteres** |
| **MSG-2026-0004 §3** | Item 2 declarado **parcialmente valido**. As duas **nao ratificadas**. Achado **RD-07** |
| **Ato de 2026-07-29** *(segundo)* | Mantem as duas **sem ratificacao** e determina **nova submissao** com ID, versao, caminho canonico, linhas, `H-A` integral, diff literal, versao substituida, revisao independente e prova de identidade |

> **A recusa foi o cumprimento da condicao de eficacia, nao a sua violacao.** Preencher os
> marcadores por conta propria e **exatamente** a causa de
> [INC-2026-001](incidents/INC-2026-001-ratificacao-inferida.md). **Nenhum incidente foi aberto**,
> porque a fonte canonica nunca conteve hash invalido.

## 2. Os dois objetos — ficha completa

### 2.1 `DEP-KMS` 1.0.0 → **1.1.0**

| Campo exigido | Valor |
|---|---|
| **ID** | `DEP-KMS` |
| **Versao** | **1.1.0** *(emenda MENOR)* |
| **Versao substituida** | **1.0.0** — permanece recuperavel *(§4)* |
| **Caminho canonico** | `departments/kms/carta.md` |
| **Linhas** | **460 → 464** *(+4)* |
| **`H-A` integral** *(64)* | **`10cfc73d5e3b7779beb22bef5dc11b0ace1d15f8b0d9855aa8cfbfbb6fec33e5`** |
| **`H-N` integral** *(64)* | `194da2b59c46902cfe2eca5b9f18357221db7c0bceb44530765795cea9d229e8` |
| **`H-P` projetado** *(apos O4)* | **`2c5bd70616e509d8c64085a6ba56775f31a54fbc62a728cb8d60735fc8f40f81`** |
| `H-A` · `H-N` **em vigor** *(1.0.0)* | `a63bb267d15d5d81335a60776ebb130d60dbd5b89e62e0702794a25bc638aacf` · `613ec1a42677787e21cb3aef8fd7c9bfd72eeeedc85d53f3c05577b154bff327` |
| **Achado que fecha** | **RC-05** — a **unica** das nove Cartas sem nenhuma linha sobre incidente |
| **Revisao independente** | **DEP-GOV** — DEP-KMS e objeto e nao revisa o instrumento que define a propria autoridade |
| **Recomendacao** | **APROVAR** |

**Diff literal — 10 alteracoes, medidas sobre o arquivo candidato nesta missao:**

| # | Local | Antes | Depois |
|---|---|---|---|
| **K1** | frontmatter | `versao: 1.0.0` | `versao: 1.1.0` |
| **K2** | frontmatter | `status: ativo` | `status: em-revisao` |
| **K3** | frontmatter | `ratificacao: ratificada` | `ratificacao: pendente` |
| **K4** | **§4**, apos *"Alterar Carta de Capability que exerco sem custodiar"* | *(inexistente)* | linha de exclusao: **Registrar, numerar ou fechar incidente** de conformidade → **DEP-GOV** *(registra e numera)* · **DEP-QAR** *(fecha)* · fonte FND-09 §8.2, linha `INC`; FND-03 §2.3 |
| **K5** | **§7**, apos *"Reporte / Alerta"* | *(inexistente)* | linha de artefato: **Incidente de conformidade** · `INC` · **Detecto e reporto — nao registro, nao numero, nao fecho** · `governance/incidents/` |
| **K6** | **§10**, apos `I-10` | *(inexistente)* | impedimento **I-11** — **Registrar, numerar ou fechar incidente de conformidade**; substitutos **DEP-GOV** e **DEP-QAR**; fonte FND-09 §8.2, linha `INC` |
| **K7** | **§13.2**, recorte 1-2-4 | `**68 linhas**` | `**69 linhas**` |
| **K8** | **§13.2**, recorte + 5 e 10 | `**139 linhas**` | `**141 linhas**` |
| **K9** | **§13.2**, Carta integral | `**460 linhas**` | `**464 linhas**` |
| **K10** | Historico de versoes | *(inexistente)* | linha `1.1.0`, descrevendo K4 a K9 |

**3 de frontmatter · 3 linhas normativas novas · 3 valores de medicao · 1 de historico.**
**Blocos tocados: B3 *(§4)* · B6 *(§7)* · B9 *(§10)* · B12 *(§13.2)*. Nenhum outro.**

### 2.2 `DEP-ENG` 1.0.0 → **1.1.0**

| Campo exigido | Valor |
|---|---|
| **ID** | `DEP-ENG` |
| **Versao** | **1.1.0** *(emenda MENOR)* |
| **Versao substituida** | **1.0.0** — permanece recuperavel *(§4)* |
| **Caminho canonico** | `departments/eng/carta.md` |
| **Linhas** | **400 → 402** *(+2)* |
| **`H-A` integral** *(64)* | **`38d4613d88b8253cd8b34d6b2b51fcc68624dfeb9509093de6678f9968428be9`** |
| **`H-N` integral** *(64)* | `e486a9f6206e73a80ef60b57b02efc190d586b6510f38f8b62f90c924ffab713` |
| **`H-P` projetado** *(apos O4)* | **`fb8b3b49c0b4c06a204050a7f83b661c8b06ba83c4b6b9fbef3feae4bc650c82`** |
| `H-A` · `H-N` **em vigor** *(1.0.0)* | `f50891c7096e50632a9f7d21e2b7d99ecee250129c87207642fcfb02e6fd67db` · `4c0b111df1da13a0bd70d693436102bf5bc853a19e2f3e4c57b3ba34cee061f7` |
| **Achado que fecha** | **RC-07** — a **unica** das nove sem o impedimento sobre a propria Carta |
| **Revisao independente** | **DEP-GOV** |
| **Recomendacao** | **APROVAR** |

**Diff literal — 7 alteracoes:**

| # | Local | Antes | Depois |
|---|---|---|---|
| **E1** | frontmatter | `versao: 1.0.0` | `versao: 1.1.0` |
| **E2** | frontmatter | `status: ativo` | `status: em-revisao` |
| **E3** | frontmatter | `ratificacao: ratificada` | `ratificacao: pendente` |
| **E4** | **§10**, apos `I-8` | *(inexistente)* | impedimento **I-9** — **Aprovar, revisar ou emendar esta Carta**; substitutos **DEP-GOV** *(revisa)* e **SOBERANO** *(aprova e ratifica)*; fonte RM-06b, LV-03; FND-09 §8.2 |
| **E5** | **§13.2**, recorte + 5 e 10 | `**115 linhas**` | `**116 linhas**` |
| **E6** | **§13.2**, Carta integral | `**400 linhas**` | `**402 linhas**` |
| **E7** | Historico de versoes | *(inexistente)* | linha `1.1.0`, descrevendo E4 a E6 |

**3 de frontmatter · 1 linha normativa nova · 2 valores de medicao · 1 de historico.**
**Blocos tocados: B9 *(§10)* · B12 *(§13.2)*. Nenhum outro.**

## 3. Prova de identidade com o candidato revisado

**A exigencia e a mais dura do ato, e a prova e criptografica, nao declaratoria.**

| # | Verificacao | Metodo | Resultado |
|---|---|---|---|
| **V1** | O objeto submetido agora **e o mesmo** revisado na Missao 1.10 | `sha256sum` do candidato × valor publicado em **PS-2026-003 §2.1 e §2.2**, escrito **antes** do primeiro ato | **`DEP-KMS` reproduz `10cfc73d…33e5` · `DEP-ENG` reproduz `38d4613d…28be9`** — **2 de 2**, nos 64 digitos |
| **V2** | `H-N` reproduz o valor revisado | Reimplementacao **independente** de `IR-02` + `IR-03`, validada **primeiro** contra as tres Cartas ja em vigor — reproduziu `747862a9…4487`, `613ec1a4…f327` e `4c0b111d…061f7` | **2 de 2 reproduzem** |
| **V3** | As Cartas **em vigor** nao foram tocadas desde a revisao | `sha256sum` de `departments/kms/carta.md` e `departments/eng/carta.md` × valores de PS-2026-003 | **2 de 2 identicos** — `a63bb267…aacf` e `f50891c7…67db` |
| **V4** | O diff e **exatamente** o revisado | `diff -u` entre a Carta em vigor e o candidato | **10 alteracoes em `DEP-KMS`, 7 em `DEP-ENG`** — **identicas** as de PS-2026-003 §2.1 e §2.2, **nenhuma a mais** |
| **V5** | `H-N` **invariante sob O4** | `H-N` do candidato × `H-N` apos aplicar O4 | **Invariante em 2 de 2** (IR-02, IR-06) |
| **V6** | `IR-09` — reconstrucao | Reverter **apenas** `status` e `ratificacao` no arquivo pos-O4 projetado e medir | **2 de 2 reproduzem `H-A`** |
| **V7** | Integridade do acervo antes de qualquer medicao | Reproducao de `BL-2026-07-29-03` | **137 artefatos · 37.766 linhas · `d39998da…86de`** — as tres reproduzem |
| **V8** | Ausencia de credencial nos dois candidatos | Varredura | **0 ocorrencias** (PI-08, LV-02) |

> **O que V1 prova, e o que ela nao prova.** Prova que **nao houve uma unica alteracao** entre a
> revisao da Missao 1.10 e esta submissao — **nem no candidato, nem na Carta em vigor**. Nao
> prova o merito, que continua sendo o de PS-2026-003 e **nao foi reaberto nesta missao**.

## 4. Preservacao das versoes substituidas

`DEP-KMS` **1.0.0** e `DEP-ENG` **1.0.0** permanecem recuperaveis por **quatro vias**, sem
segunda Carta canonica e sem area historica nova — o desenho fixado em
[MSG-2026-0003 §2.1](../memory/operacional/MSG-2026-0003-ato-soberano-emenda-qar-e-criterio-de-consolidacao.md),
**PV-1 a PV-4**:

| Via | `DEP-KMS` 1.0.0 | `DEP-ENG` 1.0.0 |
|---|---|---|
| **PV-1 — hash registrado** | `H-A` `a63bb267…aacf` · `H-N` `613ec1a4…f327` | `H-A` `f50891c7…67db` · `H-N` `4c0b111d…061f7` |
| **PV-2 — diff reversivel** | §2.1, literal e completo | §2.2, literal e completo |
| **PV-3 — copia datada** | **Tripla** — 131 arquivos *(Missao 1.10)*, 134 *(aplicacao do ato)* e **137** *(esta missao)*, fora do acervo | idem |
| **PV-4 — historico da propria Carta** | A linha `1.0.0` permanece e **nunca sai** (AL-04) | idem |

**Duas Cartas do mesmo departamento nunca coexistem** (MM-01).

## 5. Quadro consolidado

| Carta | De → Para | Achado | Classe | Alteracoes | Linhas | Blocos normativos | **Recomendacao** |
|---|---|---|---|---|---|---|---|
| `DEP-KMS` | 1.0.0 → **1.1.0** | **RC-05** | **Normativo** | **10** | 460 → **464** | B3 · B6 · B9 | **APROVAR** |
| `DEP-ENG` | 1.0.0 → **1.1.0** | **RC-07** | **Normativo** | **7** | 400 → **402** | B9 | **APROVAR** |

**17 alteracoes · +6 linhas · 0 titulares alterados · 0 autoridades criadas · 0 documentos em
cascata.**

> ### A vigilancia de **FT-04**, atualizada e honesta
> **PS-2026-002 recomendou 5 de 5 · PS-2026-003, 3 de 3 · este, 2 de 2.** Somados, **10 objetos
> submetidos e nenhuma devolucao.**
>
> **A mitigacao continua verificavel:** as duas emendas **nao sao julgamento novo**. Sao os
> mesmos objetos de PS-2026-003, **byte a byte** (§3, V1), nascidos de achados que o sistema
> registrou contra si e remedidos por ferramenta: `DEP-KMS` tem **0** ocorrencias do termo
> *incidente* em 460 linhas; `DEP-ENG` tem **8** impedimentos e **nenhum** sobre a propria Carta.
> **Devolver seria coerente apenas se o achado fosse falso.**

## 6. O que **nao** esta neste pacote

| Objeto | Por que |
|---|---|
| **`DEP-QAR` 1.2.0** | **Ratificada e aplicada** por ato expresso de 2026-07-29 — [MSG-2026-0005](../memory/operacional/MSG-2026-0005-ato-soberano-aplicacao-dep-qar.md) |
| **RD-02** · **RD-09** | Pacotes **separados** — PS-2026-004 e PS-2026-005 |
| O **merito** das duas emendas | Vive em **PS-2026-003 §2.1 e §2.2**, **nao reaberto e nao reproduzido em substancia** |
| **RC-01, RC-05, RC-07** como achados fechados | **RC-01 fechou** com a aplicacao de `DEP-QAR` 1.2.0. **RC-05 e RC-07 permanecem abertos** — a existencia da emenda **nao os fecha** |
| Spec, agente, skill, workflow, produto, codigo, infraestrutura | **Nenhum criado**, por determinacao |

## 7. Minuta do ato — **pronta, com os valores verificados**

> ### Esta secao **nao e um ato**. Nada aqui produz efeito.
> **Terceira vez que a minuta e entregue preenchida** — resposta acumulada a **RD-05** e a
> **RD-07**.

```
ATO SOBERANO DO FUNDADOR — <data do ato>

Apos revisar governance/pacote-soberano-2026-07-29-kms-eng.md, o diff literal, a
revisao independente e a prova de identidade com o candidato revisado:

Aprovo e ratifico expressamente:

- DEP-KMS, versao 1.1.0, caminho departments/kms/carta.md, 464 linhas,
  SHA-256 10cfc73d5e3b7779beb22bef5dc11b0ace1d15f8b0d9855aa8cfbfbb6fec33e5;
- DEP-ENG, versao 1.1.0, caminho departments/eng/carta.md, 402 linhas,
  SHA-256 38d4613d88b8253cd8b34d6b2b51fcc68624dfeb9509093de6678f9968428be9.

A ratificacao alcanca exclusivamente os conteudos candidatos e os diffs literais
identificados individualmente em PS-2026-006 §2.1 e §2.2.

A entrada em vigor depende de verificacao independente de identidade, versao, hash
integral, diff literal, revisao e inexistencia de alteracao entre o candidato revisado
e o objeto a ser aplicado. DEP-KMS 1.0.0 e DEP-ENG 1.0.0 deverao permanecer
recuperaveis como versoes historicas substituidas.

Nenhuma alteracao posterior esta abrangida por este ato, e ele nao alcanca qualquer
objeto nao enumerado expressamente.
```

## 8. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Fonte do **merito** | [PS-2026-003 §2.1 e §2.2](pacote-soberano-2026-07-29-emendas.md) — **nao editada, nao reaberta** |
| Achado que motiva a reemissao | **RD-07** — [PT-2026-001 §10](relatorio-transicao-2026-07-29-departamentos.md) |
| Ressalva que fecha, **se houver ato** | **R2** de [FIT-2026-010](fitness/FIT-2026-010-aplicacao-do-ato-soberano.md) · pendencia **PS-5** |
| Achados que fecha, **se houver ato** | **RC-05** *(`DEP-KMS`)* · **RC-07** *(`DEP-ENG`)* |
| Contrato das Cartas | [ADR-0011](../decisions/ADR-0011-contrato-de-carta-de-departamento.md), DC-01 a DC-10 |
| Regra de integridade aplicada | [ADR-0012](../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md), `IR-01` a `IR-10` |
| Ato que **nao** os alcancou | [MSG-2026-0004 §3](../memory/operacional/MSG-2026-0004-ato-soberano-cartas-emenda-constitucional-e-regime-do-fitness-check.md) |
| Pacotes irmaos | [PS-2026-004](pacote-soberano-2026-07-29-rd-02.md) · [PS-2026-005](pacote-soberano-2026-07-29-rd-09.md) |
| Relatorio da missao | [PT-2026-002](relatorio-transicao-2026-07-29-fechamento.md) |
| Verificacao de aptidao | [FIT-2026-011](fitness/FIT-2026-011-fechamento-de-autoridade.md) |
| Baseline vigente na submissao | **`BL-2026-07-29-04`** — [catalogo mestre §10](artifact-registry.md) |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-GOV | **Reemissao** das duas emendas nao ratificadas por identificador invalido *(RD-07)*, com **todos os campos que o ato exige**: ID, versao, caminho canonico, linhas, `H-A` e `H-N` integrais de 64 caracteres, **`H-P` projetado**, diff literal item a item, versao substituida com as **quatro vias de preservacao**, revisao independente e **prova criptografica de identidade** com o candidato revisado — **oito verificacoes, 2 de 2 em todas**. **17 alteracoes · +6 linhas · 0 titulares alterados · 0 autoridades criadas.** **Nenhuma Carta editada**; **PS-2026-003 nao foi editada nem reaberta**. **Sexto pacote soberano.** |
