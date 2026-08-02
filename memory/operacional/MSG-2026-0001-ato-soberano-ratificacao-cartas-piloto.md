---
id: MSG-2026-0001
titulo: Ato Soberano de aprovacao e ratificacao das Cartas DEP-QAR e DEP-ENG
tipo: relatorio
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: SOBERANO
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: null
decisoes_relacionadas: [ADR-0011]
substitui: []
substituido_por: null
canal: DIRETIVA
emissor: SOBERANO
destinatario: DEP-GOV
ttl: 1 ciclo — expira sem perda; o efeito duravel foi promovido no mesmo ato (§5)
resumo: Registra, como fonte canonica unica, o ato soberano de 2026-07-28 que aprova e ratifica as Cartas DEP-QAR e DEP-ENG nas versoes submetidas ao encerramento da Missao 1.6.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# MSG-2026-0001 — Ato Soberano sobre as Cartas piloto

## Proposito
Registrar **uma unica vez** o ato soberano de 2026-07-28 sobre `DEP-QAR` e `DEP-ENG`, com os
IDs, versoes e hashes que ele vincula. Indices, frontmatters e catalogo **referenciam** esta
secao; nenhum a reproduz (CM-09, PJ-01).

## Escopo
| Item | Definicao |
|---|---|
| Inclui | O ato de 2026-07-28 e **apenas** ele; seu alcance, sua condicao de eficacia e os efeitos aplicados |
| **Nao** inclui | Merito das Cartas *(objeto de [REV-INTERCLASSES](../../foundation/revisao-arquitetural-validacao-interclasses-2026-07-28.md))*; qualquer artefato que o ato nao nomeie |
| Instrumento | **Diretiva**, tipo documental de [FND-10 §4.6](../../foundation/10-artifact-framework.md), entidade `MSG`. Nenhum tipo, entidade, camada ou diretorio novo |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| **Emissor** | **SOBERANO** | PI-01 — autoridade final, indelegavel |
| **Registra** | **DEP-GOV** | **LM-05, CV-09** — quem registra e papel distinto de quem executou a mudanca. A mudanca foi executada por **DEP-EXE** |
| **Verifica a eficacia** | **DEP-QAR** | FND-10 §10.5: *"`ratificacao` coerente com a classe — a cada C3/Tipo 1 — executa DEP-QAR"* |
| Nao participa | **DEP-EXE** | Autor das duas Cartas; registrar a propria ratificacao repetiria a causa de [INC-2026-001](../../governance/incidents/INC-2026-001-ratificacao-inferida.md) |

---

## 1. O ato

| Campo | Conteudo |
|---|---|
| Emissor | **SOBERANO** (Lucas) |
| Canal | **DIRETIVA** (FND-05 §2) |
| Data do ato | **2026-07-28** |
| Objeto | O **texto final** das Cartas `DEP-QAR` e `DEP-ENG`, nas versoes canonicas submetidas ao encerramento da **Missao 1.6** |
| Natureza | **Aprovacao e ratificacao no mesmo ato** — a matriz de FND-09 §8.2, linha `DEP`, atribui as duas ao SOBERANO |
| Condicao de eficacia | Entrada em vigor **apos verificacao independente** do registro, da integridade dos artefatos e da inexistencia de alteracao entre as versoes revisadas e as ratificadas |
| Instrucao acessoria | O registro canonico vincula o ato aos **IDs, versoes e hashes** correspondentes |
| Limite expresso | Nenhuma alteracao posterior dessas Cartas esta abrangida |

### 1.1 Texto do ato

> Apos revisar os resultados, evidencias, ressalvas e riscos registrados na Missao 1.6, aprovo
> e ratifico expressamente as Cartas de Departamento DEP-QAR e DEP-ENG, exatamente nas versoes
> canonicas submetidas a minha decisao no encerramento dessa missao.
>
> Determino que o registro canonico vincule este ato aos IDs, versoes e hashes correspondentes.
> Nenhuma alteracao posterior dessas Cartas esta abrangida por esta ratificacao.
>
> Autorizo sua entrada em vigor apos verificacao independente do registro, da integridade dos
> artefatos e da inexistencia de alteracao entre as versoes revisadas e as versoes ratificadas.
>
> Este ato nao ratifica MEM-EST-0001, FIT-2026-001, FIT-2026-002, ADRs ou qualquer outro
> artefato pendente.

> **Transcricao literal.** O texto e reproduzido como emitido; o registro normativo usa o termo
> oficial quando diverge (LX-07). Nao ha divergencia terminologica neste ato.

## 2. Objeto vinculado — IDs, versoes e hashes

Cumprimento da instrucao acessoria de §1. Hash = **SHA-256 do conteudo integral do arquivo**,
do texto **tal como submetido a decisao**, medido **antes** de qualquer transicao de estado.

| Artefato | ID | Versao ratificada | **SHA-256 do texto ratificado** | Linhas | Local |
|---|---|---|---|---|---|
| Carta de Qualidade e Risco | **`DEP-QAR`** | **1.0.0** | `fa07f55f5534d8b15166e48388a27007c640dd7d7bc498f83271267cd3d1f286` | **386** | [`departments/qar/carta.md`](../../departments/qar/carta.md) |
| Carta de Engenharia | **`DEP-ENG`** | **1.0.0** | `57aebf81a9864586771489ec141ac21de184674ece57acfcc7b3344b1b401a48` | **400** | [`departments/eng/carta.md`](../../departments/eng/carta.md) |

**Reproduzir:** `sha256sum departments/qar/carta.md departments/eng/carta.md`

> **O hash e do texto, nao do estado.** A transicao **O4** de §5 altera exclusivamente dois
> campos de frontmatter — `status` e `ratificacao` — e **nenhuma linha do corpo**. O hash do
> texto ratificado permanece a referencia do que o Soberano decidiu; o hash do arquivo apos a
> transicao consta de §5.2, ao lado do **diff exato** que os separa. Registrar apenas um dos
> dois esconderia a diferenca que o proprio ato manda vigiar.

## 3. Alcance — o que o ato ratifica e o que **nao** alcanca

Ratificacao **nao se estende por analogia** (LM-03).

| Artefato | Ratificado por este ato? | Efeito |
|---|---|---|
| **`DEP-QAR` 1.0.0** | **Sim** | `em-revisao` → `ativo`; `ratificacao: ratificada` |
| **`DEP-ENG` 1.0.0** | **Sim** | `em-revisao` → `ativo`; `ratificacao: ratificada` |
| `MEM-EST-0001` | **Nao** — excluido expressamente | Permanece `aprovado`, `ratificacao: pendente` |
| `FIT-2026-001` · `FIT-2026-002` | **Nao** — excluidos expressamente | [INC-2026-002 §7](../../governance/incidents/INC-2026-002-ratificacao-declarada-em-fitness-check.md) permanece `contido` |
| ADR-0005, ADR-0007 a ADR-0011 | **Nao** | `ratificacao: nao-exigida` — inalterado |
| Cartas `DEP-EXE` e `DEP-KMS` *(criadas na Missao 1.7)* | **Nao** — **nao existiam** na data do ato | Nascem e permanecem em `em-revisao`, `ratificacao: pendente` |
| Qualquer versao futura de `DEP-QAR` ou `DEP-ENG` | **Nao** — excluido expressamente | Versao nova exige **ato novo** |
| As sete Cartas restantes | **Nao** | Nao escritas |

> **O ato nao ratifica a Missao 1.6.** Ratifica **dois textos**. Os artefatos avaliativos dessa
> missao — `FIT-2026-005` e `REV-DEPARTAMENTO` — permanecem `ratificacao: nao-exigida`, e o
> ato nao os alcanca nem precisaria alcancar.

## 4. Verificacao independente da condicao de eficacia

Executada por **DEP-QAR** e **DEP-GOV** — nenhum dos dois produziu as Cartas (autor: DEP-EXE).
Executada **antes** de qualquer edicao desta missao.

| # | O que o ato exigiu | Metodo | Resultado |
|---|---|---|---|
| V1 | Integridade do **registro** | Reproducao da baseline vigente `BL-2026-07-28-03`: contagem, linhas e impressao digital | **107 artefatos · 26.506 linhas · `541ed5b6…d6b1`** — os tres reproduzem o valor registrado |
| V2 | Integridade dos **artefatos** | `sha256sum` das duas Cartas | Hashes de §2, medidos e registrados |
| V3 | **Inexistencia de alteracao** entre as versoes revisadas e as ratificadas | Confronto do numero de linhas com o valor registrado no [catalogo mestre §4.3.1](../../governance/artifact-registry.md) ao encerramento da Missao 1.6 | **386 = 386** e **400 = 400** |
| V4 | Idem, por via independente da anterior | Impressao digital do acervo — cobre caminho e extensao de **todos** os 107 arquivos | **Reproduz.** Nenhum arquivo acrescentado, removido, renomeado ou alterado em extensao |
| V5 | Idem, por via temporal | `mtime` das duas Cartas contra o `mtime` do ultimo artefato da Missao 1.6 | `qar` **17:58:44** · `eng` **17:21:16** · ultimo artefato da missao **17:59:12** — **ambas anteriores**; nenhuma tocada apos o encerramento |
| V6 | Ausencia de autoverificacao | Papel de quem verifica × papel de quem produziu | **DEP-QAR** e **DEP-GOV** verificam; **DEP-EXE** produziu. Zero coincidencia (FT-02, RM-06b) |
| V7 | Ausencia de credencial no objeto ratificado | Varredura das duas Cartas | **0 ocorrencias** (PI-08, LV-02) |

### 4.1 Limite declarado da verificacao

> **A impressao digital nao detecta edicao que preserve o numero de linhas** — o limite ja
> consta do [catalogo mestre §10.2](../../governance/artifact-registry.md) e nao e omitido aqui.
> Por isso a condicao de eficacia **nao** repousa sobre ela sozinha: V2 mede o **conteudo byte a
> byte** das duas Cartas por SHA-256, e V3 e V5 checam por vias independentes. **Tres vias
> convergem**; nenhuma delas sozinha bastaria (PI-10, LV-12).

**Condicao de eficacia: SATISFEITA.** As sete verificacoes passam, por tres vias independentes.

## 5. Efeitos aplicados

| # | Efeito | Onde | Operacao |
|---|---|---|---|
| E1 | `DEP-QAR`: `status` `em-revisao` → **`ativo`**; `ratificacao` `pendente` → **`ratificada`** | [`departments/qar/carta.md`](../../departments/qar/carta.md) | **O4** (FND-10 §5.2) |
| E2 | `DEP-ENG`: idem | [`departments/eng/carta.md`](../../departments/eng/carta.md) | **O4** |
| E3 | Linha de rastreabilidade e classificacao atualizadas | [catalogo mestre §4.3.1 e §6](../../governance/artifact-registry.md) | Projecao (PJ-02) |
| E4 | Ressalva **R4** de FIT-2026-005 — *"os dois pilotos nao estao em vigor"* — reconciliada | [FIT-2026-006](../../governance/fitness/FIT-2026-006-validacao-interclasses.md) | Reconciliacao |
| E5 | Condicao 1 do rollout de FIT-2026-005 satisfeita | [FIT-2026-006 §Rollout](../../governance/fitness/FIT-2026-006-validacao-interclasses.md) | — |

### 5.1 O efeito duravel foi promovido — por isso o `ttl` desta Diretiva nao ameaca nada

FND-03 §3.13 determina que mensagem portadora de **fato duravel** seja **promovida ao
instrumento proprio** (FND-05 §9.1). A promocao ocorreu **no mesmo ato**:

| Fato | Instrumento proprio que passa a guarda-lo | Fonte da regra |
|---|---|---|
| **Estado de ratificacao** de cada Carta | O campo `ratificacao` do **frontmatter da propria Carta** | FND-10 §5.4, tabela de condicao de entrada em `ativo` |
| **Vigencia** de cada Carta | O campo `status` da propria Carta | FND-10 §5.2, operacao O4 |
| **Vinculo ID × versao × hash** | [Catalogo mestre §10](../../governance/artifact-registry.md) — evidencia de integridade | FND-10 §10.4 |

**Consequencia:** se esta Diretiva expirar pelo `ttl` de OPR, **nenhum fato duravel se perde** —
os tres ja vivem no instrumento que a norma designa. O que esta Diretiva guarda e o **ato**, e
o ato e reproduzido aqui em §1.1 para que a fonte permaneca percorrivel (LN-07).

### 5.2 Diff exato aplicado, e o hash resultante

**Nenhuma linha do corpo das Cartas foi alterada.** Duas linhas de frontmatter por Carta:

| Carta | Campo | Antes | Depois |
|---|---|---|---|
| `DEP-QAR` | `status` | `em-revisao` | `ativo` |
| `DEP-QAR` | `ratificacao` | `pendente` | `ratificada` |
| `DEP-ENG` | `status` | `em-revisao` | `ativo` |
| `DEP-ENG` | `ratificacao` | `pendente` | `ratificada` |

| Carta | Linhas antes | **Linhas depois** | **SHA-256 apos a transicao** |
|---|---|---|---|
| `DEP-QAR` | 386 | **386** | `c591fd62e84216d416c190cd56d5b665b038add5d901866f371a116bb6bc311b` |
| `DEP-ENG` | 400 | **400** | `f50891c7096e50632a9f7d21e2b7d99ecee250129c87207642fcfb02e6fd67db` |

> **Contagem de linhas identica antes e depois — 386 e 400.** E a prova de que a transicao nao
> tocou o corpo: dois campos substituidos, nenhuma linha acrescentada ou removida. Por isso a
> impressao digital do acervo, que cobre caminho e extensao, **nao muda por efeito desta
> transicao** — o que muda o acervo nesta missao sao os artefatos novos, nao a ativacao.

> **Por que a versao permanece 1.0.0.** FND-03 §6 vincula o incremento MAIOR/MENOR a mudanca de
> **conteudo**; transicao de estado nao e emenda (ADR-0009, AC-08). Incrementar a versao criaria
> uma versao **nao ratificada** a partir de um ato que ratificou a 1.0.0 — o oposto do que o ato
> determina. Pela mesma razao **nenhuma linha e acrescentada ao Historico de versoes**: o
> historico registra emendas, e nao houve emenda.

## 6. O que deliberadamente **nao** foi feito

| Nao feito | Norma que o impede | Consequencia assumida |
|---|---|---|
| Editar `FIT-2026-005` ou `REV-DEPARTAMENTO` para refletir a vigencia | **M1** (FND-10 §6.2); PJ-04; [MEM-APR-0003](../aprendizado/MEM-APR-0003-campo-de-estado-em-artefato-imutavel.md) | Os dois continuam registrando o estado **no ato de sua emissao** — `em-revisao`. Quem le precisa desta Diretiva para saber o estado corrente; o custo e um salto de referencia |
| Editar `INC-2026-001 §11` para acrescentar este ato | **M1**; e §11 e a fonte canonica de **outro** ato | Dois atos, duas fontes canonicas — nunca uma fonte que acumule |
| Ratificar `MEM-EST-0001`, `FIT-2026-001` ou `FIT-2026-002` | Exclusao **expressa** no proprio ato; LM-03 | Permanecem pendentes; INC-2026-002 §7 segue aberto |
| Estender a ratificacao as Cartas criadas nesta missao | LM-03 — ratificacao nao alcanca o que **nao existia** na data do ato | `DEP-EXE` e `DEP-KMS` nascem em `em-revisao` |
| Reproduzir os hashes em indices | CM-09, PJ-01 | Indices referenciam **esta secao** |

## 7. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Contrato que exigia o ato | [ADR-0011 §5.3, **DC-09**](../../decisions/ADR-0011-contrato-de-carta-de-departamento.md) |
| Ressalva que o ato desbloqueia | **R4** de [FIT-2026-005](../../governance/fitness/FIT-2026-005-cartas-de-departamento.md) |
| Precedente de registro de ato soberano | [INC-2026-001 §11](../../governance/incidents/INC-2026-001-ratificacao-inferida.md) — mesma forma: **uma** fonte canonica, tudo o mais referencia |
| Verificacao independente | §4 desta Diretiva; [REV-INTERCLASSES §1](../../foundation/revisao-arquitetural-validacao-interclasses-2026-07-28.md) |
| Baseline sobre a qual a integridade foi conferida | **`BL-2026-07-28-03`**, preservada e nao editada (BL-02) |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-GOV *(registro)* · SOBERANO *(emissao)* | Registro canonico do ato soberano de 2026-07-28 sobre `DEP-QAR` e `DEP-ENG`, com IDs, versoes e hashes vinculados, verificacao independente da condicao de eficacia por tres vias e promocao do efeito duravel ao instrumento proprio. |
