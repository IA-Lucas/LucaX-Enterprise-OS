---
id: MSG-2026-0005
titulo: Ato Soberano de liberacao da aplicacao de DEP-QAR 1.2.0, manutencao de DEP-KMS e DEP-ENG sem ratificacao e determinacao da Missao 1.11
tipo: relatorio
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: SOBERANO
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-07-29
atualizado_em: 2026-07-29
revisao_prevista: null
decisoes_relacionadas: [ADR-0011, ADR-0012]
substitui: []
substituido_por: null
canal: DIRETIVA
emissor: SOBERANO
destinatario: DEP-GOV
ttl: 1 ciclo — expira sem perda; os efeitos duraveis foram promovidos no mesmo ato (§6.1)
resumo: Registra, como fonte canonica unica, o ato soberano que libera a aplicacao de DEP-QAR 1.2.0, mantem DEP-KMS 1.1.0 e DEP-ENG 1.1.0 sem ratificacao e determina a Missao 1.11, com a verificacao da condicao de eficacia.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# MSG-2026-0005 — Ato Soberano de 2026-07-29 *(segundo do dia)*

## Proposito
Registrar **uma unica vez** o ato que **libera a aplicacao** de `DEP-QAR` 1.2.0, com os
identificadores que ele vincula, o que **nao** alcanca e a verificacao da condicao de eficacia.

> **Quinto ato soberano registrado, e o primeiro que separa *ratificar* de *aplicar*.** Os
> quatro anteriores vivem em [MSG-2026-0001](MSG-2026-0001-ato-soberano-ratificacao-cartas-piloto.md),
> [MSG-2026-0002](MSG-2026-0002-ato-soberano-cartas-comando-plataforma-e-contexto.md),
> [MSG-2026-0003](MSG-2026-0003-ato-soberano-emenda-qar-e-criterio-de-consolidacao.md) e
> [MSG-2026-0004](MSG-2026-0004-ato-soberano-cartas-emenda-constitucional-e-regime-do-fitness-check.md).
> **Nenhum dos quatro foi editado.** Cinco atos, cinco fontes.

## Escopo
| Item | Definicao |
|---|---|
| Inclui | O ato e seus **tres** itens; o que cada um alcanca; a condicao de eficacia; e os efeitos aplicados |
| **Nao** inclui | O **merito** da emenda `DEP-QAR` 1.2.0 *(PS-2026-003 §2.3)*; os pacotes **C3** desta missao, que o ato **expressamente nao ratifica**; qualquer objeto nao nomeado |
| Instrumento | **Diretiva**, tipo documental de [FND-10 §4.6](../../foundation/10-artifact-framework.md), entidade `MSG`. Nenhum tipo, entidade, camada ou diretorio novo |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| **Emissor** | **SOBERANO** | PI-01 — indelegavel |
| **Registra** | **DEP-GOV** | LM-05, CV-09 |
| **Verifica a eficacia** | **DEP-QAR** | FND-10 §10.5; `IR-09` |
| **Nao participa da verificacao** | **DEP-EXE** | **Autor das nove Cartas** |

---

## 1. O ato

| Campo | Conteudo |
|---|---|
| Emissor | **SOBERANO** (Lucas) |
| Canal | **DIRETIVA** (FND-05 §2) |
| Data | **2026-07-29** |
| Objeto | **Tres** itens: **(1)** liberacao da **aplicacao** de `DEP-QAR` 1.2.0, ja ratificada; **(2)** manutencao de `DEP-KMS` 1.1.0 e `DEP-ENG` 1.1.0 **sem ratificacao**, com requisitos de nova submissao; **(3)** determinacao da **Missao 1.11** |
| Condicao de eficacia | Verificacao independente de **identidade, versao, hash integral, diff literal, revisao e inexistencia de alteracao** entre o candidato ratificado e o objeto a ser aplicado |
| Limite expresso | *"Nenhuma alteracao posterior esta abrangida"*; *"nao ratifica os futuros pacotes C3"*; *"nao altera artefatos historicos"*; *"nao alcanca qualquer objeto nao enumerado expressamente"* |

### 1.1 Texto do ato — transcricao literal

> ATO SOBERANO DO FUNDADOR — 2026-07-29
>
> **1.** Libero expressamente a aplicacao da ratificacao ja emitida sobre:
>
> - DEP-QAR, versao 1.2.0,
>   SHA-256 `41f55e7369af5a9456e621cb4abd874a5c2c61af7e5a06b1900b4ca1619b5f2b`.
>
> A entrada em vigor depende da verificacao independente de identidade, versao, hash integral,
> diff literal, revisao e inexistencia de alteracao entre o candidato ratificado e o objeto a
> ser aplicado.
>
> DEP-QAR 1.1.0 devera permanecer recuperavel como versao historica substituida. Nenhuma
> alteracao posterior esta abrangida por este ato.
>
> **2.** Mantenho sem ratificacao:
>
> - DEP-KMS, versao 1.1.0;
> - DEP-ENG, versao 1.1.0.
>
> Nova submissao devera apresentar para cada objeto ID, versao, caminho canonico, quantidade de
> linhas, SHA-256 integral de 64 caracteres, diff literal, versao substituida, revisao
> independente e prova de identidade com o candidato revisado.
>
> **3.** Determino a execucao da Missao 1.11 para resolver RD-02 e RD-09 pelo rito aplicavel e
> verificar a aptidao final da camada de Departamentos para o Specification Framework.
>
> Este ato nao ratifica os futuros pacotes C3, nao altera artefatos historicos e nao alcanca
> qualquer objeto nao enumerado expressamente.

> **Nenhuma elisao e nenhum marcador.** O unico hash do ato vem com os **64 caracteres**, e
> confere. **E o primeiro ato do acervo em que nenhum identificador precisou ser recusado** —
> RD-05 e RD-07 nao se repetem.

## 2. Objeto vinculado — ID, versao e hashes

Tres hashes conforme [ADR-0012 §5.2, IR-07](../../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md).

| Carta | Versao | **H-A** | **H-N** | **H-P** | Linhas |
|---|---|---|---|---|---|
| `DEP-QAR` | **1.2.0** | `41f55e7369af5a9456e621cb4abd874a5c2c61af7e5a06b1900b4ca1619b5f2b` | `658de6c3d53f53a4ed71adecf793067c377e1b04908d9d259cdb636a1120c725` | `9b180b714aec36150baa8ad905b2ab40a3ef93d6778dcdac5d1ad1364c03ad29` | **388** |

**Versao substituida — `DEP-QAR` 1.1.0:** `H-A` `3e69441e2acab1cc34ff03da16c9e8bb004b65295736e08f9da53dfe0eaca3a0` ·
`H-N` `747862a940eede8a8ece803d0a3d16cd1a0ecdbceef5d7a84fe6c72d78ee4487` ·
`H-P` `67407fffa111b7ab4c2910e328013d3d05fd8dcae9455d266eb3fdcf87b3d144` · **387** linhas.

**O `H-A` do ato reproduz exatamente o valor publicado em
[PS-2026-003 §2.3](../../governance/pacote-soberano-2026-07-29-emendas.md) e ratificado em
[MSG-2026-0004 §3](MSG-2026-0004-ato-soberano-cartas-emenda-constitucional-e-regime-do-fitness-check.md),
nos 64 digitos.**

## 3. Verificacao independente da condicao de eficacia

Executada por **DEP-QAR** *(medicao e reconstrucao)* e **DEP-GOV** *(forma e conferencia)*.
**DEP-EXE nao participou.** Executada **antes** de qualquer edicao.

| # | O que o ato exigiu | Metodo | Resultado |
|---|---|---|---|
| **W1** | Integridade do registro | Reproducao de `BL-2026-07-29-03` sobre o acervo intacto | **137 artefatos · 37.766 linhas · `d39998da…86de`** — as tres reproduzem |
| **W2** | **Identidade** | `sha256` do candidato × hash do ato | **`41f55e73…b5f2b` — confere nos 64 digitos** |
| **W3** | **Versao** | frontmatter do candidato | **`versao: 1.2.0`** — confere |
| **W4** | **Hash integral** | Contagem de caracteres do identificador do ato | **64** — nenhum marcador |
| **W5** | **Diff literal** | `diff -u` entre `DEP-QAR` 1.1.0 em vigor e o candidato | **5 alteracoes** — `Q1` a `Q5` de PS-2026-003 §2.3, **e nada alem delas** |
| **W6** | **Revisao** | Revisao de merito registrada em PS-2026-003 §2.3 | **DEP-GOV**, com o residuo `I-5` declarado |
| **W7** | **Inexistencia de alteracao** entre o candidato ratificado e o objeto aplicado | `sha256` do candidato **hoje** × valor publicado **antes** do primeiro ato | **Identico.** O candidato **nao foi tocado** entre a ratificacao e a aplicacao |
| **W8** | `H-N` **invariante sob O4** | `H-N` antes × depois da transicao | **Invariante** — `658de6c3…0725` (IR-02, IR-06) |
| **W9** | **`IR-09` — reconstrucao** | Reverter **apenas** `status` e `ratificacao` no arquivo aplicado e medir | **Reproduz `H-A` exatamente**, e o texto e **byte a byte identico** ao candidato |
| **W10** | Ausencia de **credencial** | Varredura por padrao de segredo | **0 ocorrencias** (PI-08, LV-02) |
| **W11** | **Recuperabilidade de 1.1.0** | Quatro vias de PV-1 a PV-4 | **4 de 4** — §5 |

**Condicao de eficacia: SATISFEITA.**

## 4. Efeitos aplicados

| # | Efeito | Onde | Operacao |
|---|---|---|---|
| **Z1** | Conteudo de `DEP-QAR` **1.2.0** aplicado, exatamente no diff `Q1`–`Q5` | `departments/qar/carta.md` | Emenda **MENOR** (AL-01) |
| **Z2** | `status` `em-revisao` → **`ativo`**; `ratificacao` `pendente` → **`ratificada`** | idem | **O4** (FND-10 §5.2) |
| **Z3** | `H-P` medido: **`9b180b71…ad29`**; **`H-N` invariante** | idem | IR-07 |
| **Z4** | **`RC-01` FECHADO** — §13.2 declarava **386** onde o arquivo tinha **387**; declara **388** e o arquivo tem **388** | idem | Fechamento com evidencia |
| **Z5** | **`DEP-QAR` 1.1.0** preservada por hash, diff reversivel, copia datada e historico | §5 | PV-1 a PV-4 |
| **Z6** | Projecao `departments/README §2` atualizada: `DEP-QAR` **387 → 388** linhas | [`departments/README`](../../departments/README.md) | Projecao (PJ-02) |
| **Z7** | Catalogo, indices e baseline atualizados na mesma mudanca | CV-04, IX-02 | Projecao |

### 4.1 O que deliberadamente **nao** foi feito

| Nao feito | Norma que o impede | Consequencia assumida |
|---|---|---|
| Aplicar `DEP-KMS` 1.1.0 ou `DEP-ENG` 1.1.0 | **Item 2 do ato** — mantidas **sem ratificacao** | Permanecem candidatas. **RC-05 e RC-07 seguem abertos**. Nova submissao em [PS-2026-006](../../governance/pacote-soberano-2026-07-29-kms-eng.md) |
| Alterar `atualizado_em` de `DEP-QAR` | O campo **nao consta do diff ratificado**; altera-lo seria alteracao alem do diff (IR-05) | O campo permanece **2026-07-28**, coerente com a data em que o candidato foi produzido |
| Promulgar **FND-02**, **FND-09** ou **FND-10** | O ato **nao ratifica os futuros pacotes C3**, expressamente | Os tres candidatos vivem **fora do acervo**, como diff e hash |
| Editar `ADR-0014`, `FIT-2026-001` ou qualquer artefato historico | *"nao altera artefatos historicos"*; **M1**, LV-04, `FT-15` | **RD-08** permanece **contido** |
| Criar Spec, agente, skill, workflow, produto, codigo ou infraestrutura | Determinacao da missao; PI-12 | **Nenhum foi criado** |

## 5. Preservacao de `DEP-QAR` 1.1.0 — **as quatro vias, verificadas**

| Via | Estado | Evidencia |
|---|---|---|
| **PV-1 — hash registrado** | ✅ | `H-A` `3e69441e…ca3a0` · `H-N` `747862a9…4487` · `H-P` `67407fff…d144` — PS-2026-003 §2.3 e §2 deste registro |
| **PV-2 — diff reversivel** | ✅ | `Q1` a `Q5` sao **literais e completos**; aplicados em sentido inverso sobre 1.2.0, reproduzem 1.1.0 |
| **PV-3 — copia datada** | ✅ | **Tripla** — 131 arquivos *(Missao 1.10)*, 134 *(aplicacao do ato)* e **137** *(esta missao, anterior a qualquer edicao)*, fora do acervo |
| **PV-4 — historico da propria Carta** | ✅ | As linhas `1.0.0` e `1.1.0` permanecem em `DEP-QAR §Historico` e **nunca saem** (AL-04) |

**Nenhuma segunda Carta canonica foi criada** (MM-01).

## 6. Rastreabilidade

### 6.1 Os efeitos duraveis foram promovidos

| Fato | Instrumento proprio que passa a guarda-lo |
|---|---|
| Vigencia de `DEP-QAR` 1.2.0 | O campo `status` da Carta (FND-10 §5.2) |
| Estado de ratificacao | O campo `ratificacao` do frontmatter (FND-10 §5.4) |
| Vinculo ID × versao × `H-A`/`H-N`/`H-P` | **§2 desta Diretiva**, referenciada pelo [catalogo mestre §10](../../governance/artifact-registry.md) |
| Requisitos da nova submissao *(item 2)* | [PS-2026-006](../../governance/pacote-soberano-2026-07-29-kms-eng.md) |
| Determinacao da Missao 1.11 *(item 3)* | [PT-2026-002](../../governance/relatorio-transicao-2026-07-29-fechamento.md) |

### 6.2 Alcance — o que o ato alcanca e o que **nao** alcanca

Ratificacao **nao se estende por analogia** (LM-03).

| Objeto | Alcancado? | Efeito |
|---|---|---|
| `DEP-QAR` **1.2.0** | **Sim — aplicacao liberada** | Aplicada; `em-revisao` → **`ativo`**, `pendente` → **`ratificada`** |
| `DEP-KMS` 1.1.0 · `DEP-ENG` 1.1.0 | **Nao — expressamente mantidas sem ratificacao** | Permanecem candidatas; requisitos de reemissao cumpridos em PS-2026-006 |
| **Missao 1.11** | **Sim — determinada** | RD-02 e RD-09 tratados **pelo rito aplicavel**: RFC → ADR → pacote soberano |
| **`ADR-0016` · `FND-02` 1.3.0** | **Nao** — *"nao ratifica os futuros pacotes C3"* | Candidatos; [PS-2026-004](../../governance/pacote-soberano-2026-07-29-rd-02.md) |
| **`ADR-0017` · `FND-09` 1.4.0 · `FND-10` 1.3.0** | **Nao** — idem | Candidatos; [PS-2026-005](../../governance/pacote-soberano-2026-07-29-rd-09.md) |
| Artefatos historicos | **Nao** — vedacao expressa | `ADR-0014` e `FIT-2026-001` **contidos, nao corrigidos** |
| Qualquer versao futura de qualquer artefato | **Nao** | Exige ato novo |

### 6.3 Fontes

| Campo | Conteudo |
|---|---|
| Pacote consumido | [PS-2026-003 §2.3](../../governance/pacote-soberano-2026-07-29-emendas.md) |
| Ato que **ratificou** o objeto | [MSG-2026-0004 §3](MSG-2026-0004-ato-soberano-cartas-emenda-constitucional-e-regime-do-fitness-check.md) |
| Regra de integridade aplicada | [ADR-0012](../../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md), `IR-01` a `IR-10` |
| Contrato que exigia o ato | [ADR-0011 §5.3, **DC-09**](../../decisions/ADR-0011-contrato-de-carta-de-departamento.md) |
| Achado que fecha | **RC-01** |
| Relatorio da missao determinada | [PT-2026-002](../../governance/relatorio-transicao-2026-07-29-fechamento.md) |
| Verificacao de aptidao | [FIT-2026-011](../../governance/fitness/FIT-2026-011-fechamento-de-autoridade.md) |
| Baseline conferida **antes** das edicoes | **`BL-2026-07-29-03`**, preservada e **nao editada** (BL-02) |
| Baseline emitida apos as edicoes | **`BL-2026-07-29-04`** |
| Copia datada anterior as edicoes | **137** arquivos, fora do acervo (PI-07, AF-35) |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-GOV *(registro)* · SOBERANO *(emissao)* | Registro canonico do **quinto ato soberano**, e o **primeiro que separa ratificar de aplicar**: libera a aplicacao de `DEP-QAR` **1.2.0**, mantem `DEP-KMS` 1.1.0 e `DEP-ENG` 1.1.0 **sem ratificacao** com requisitos de reemissao, e determina a **Missao 1.11**. Condicao de eficacia verificada por **onze** verificacoes, entre elas **`IR-09` reproduzindo `H-A` byte a byte** e a prova de que o candidato **nao foi tocado entre a ratificacao e a aplicacao**. **Primeiro ato do acervo sem nenhum identificador recusado** — RD-05 e RD-07 nao se repetem. **`RC-01` fechado**; `DEP-QAR` 1.1.0 preservada pelas **quatro vias**. |
