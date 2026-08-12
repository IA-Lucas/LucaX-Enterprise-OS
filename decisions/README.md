---
id: IDX-decisions
titulo: Indice Oficial de Decisoes (ADR)
tipo: relatorio
versao: 1.14.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-GOV
criado_em: 2026-07-28
atualizado_em: 2026-08-12
revisao_prevista: null
decisoes_relacionadas: [ADR-0001, ADR-0003, ADR-0004, ADR-0007, ADR-0008, ADR-0011]
substitui: []
substituido_por: null
resumo: Conta a sequencia oficial ADR e projeta o estado de ratificacao de cada decisao a partir de INC-2026-001 §11.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
projecao_de: INC-2026-001 §11
---

# Indice Oficial de Decisoes

## Proposito
Manter o registro unico e o contador oficial da sequencia `ADR-NNNN`, conforme
[FND-03 §2.3](../foundation/03-taxonomia.md).

## Escopo
Todas as decisoes registradas do sistema. Propostas em aberto ficam em [`../rfcs/`](../rfcs/).

## Responsaveis
| Papel | Responsavel |
|---|---|
| Proprietario e numerador oficial | DEP-GOV |
| Verificacao de validade | DEP-QAR |
| Preservacao na memoria | DEP-KMS |

---

## Contador oficial

| Campo | Valor |
|---|---|
| Ultimo numero atribuido | **0038** |
| Proximo numero disponivel | **0039** |
| **⚠️ Contador exercido — e estava DEFASADO, quinta ocorrencia da familia de `RD-32` (Onda 3, 2026-08-12)** | O cabecalho dizia **`0036`/`0037`** enquanto `ADR-0037` existia desde 2026-08-03: a Missao 1.13.14 gravou a nota de exercicio e **nao moveu o cabecalho** — o contador que se corrige por nota continua errando por cabecalho. Antes de atribuir **`0038`**, testou-se a existencia contra a **copia datada anterior as edicoes** *(`_backups/LucaX-Enterprise-OS_2026-08-12_pre-onda-3/`)*: **`ADR-0037` ✅ existe · `ADR-0038` ✅ NAO existe** — `V1` de [MEM-APR-0006](../memory/aprendizado/MEM-APR-0006-exercer-o-contador-revela-o-defeito.md). Corrigido **`0036`/`0037` → `0038`/`0039`** |
| **Contador exercido, nao lido (Missao 1.13.14)** | Antes de atribuir **`0037`**, testou-se a existencia de `ADR-0037-*.md` contra a **copia datada anterior as edicoes** *(`_backups/LucaX Enterprise OS-2026-08-03-antes-do-adr-sucessor/`)*: **`ADR-0036` ✅ existe · `ADR-0037` ✅ NAO existe** — `V1` de [MEM-APR-0006](../memory/aprendizado/MEM-APR-0006-exercer-o-contador-revela-o-defeito.md) |
| **Contador exercido, nao lido (Missao 1.13.13)** | Antes de atribuir **`0036`**, testou-se a existencia de `ADR-0036-*.md` contra a **copia datada anterior as edicoes** *(`_backups/LucaX Enterprise OS-2026-08-03-antes-da-terceira-skill/`)*: **`ADR-0035` ✅ existe · `ADR-0036` ✅ NAO existe** — `V1` de [MEM-APR-0006](../memory/aprendizado/MEM-APR-0006-exercer-o-contador-revela-o-defeito.md) |
| **Contador exercido, nao lido (Missao 1.13.12)** | Antes de atribuir **`0035`**, testou-se a existencia de `ADR-0035-*.md` contra a **copia datada anterior as edicoes** *(`_backups/LucaX Enterprise OS-2026-08-03-pre-missao-1-13-12/`)*: **`ADR-0034` ✅ existe · `ADR-0035` ✅ NAO existe** — `V1` de [MEM-APR-0006](../memory/aprendizado/MEM-APR-0006-exercer-o-contador-revela-o-defeito.md) |
| **⚠️ `RD-95` — este contador estava DEFASADO EM UM, e o defeito foi encontrado EXERCENDO-O (Missao 1.13.5)** | Ele declarava **`0030` disponivel** enquanto **`ADR-0030` ja existia** desde 2026-08-01 *(Missao 1.13.4.5)*. Confiar nele produziria **colisao de identificador**, contra `FND-03 §2.3`. O numero `0031` foi atribuido **por teste de existencia contra a copia datada** *(`_backups/…_2026-08-01_pre-missao-1-13-5/`)* — `ADR-0029` ✅ existe · `ADR-0030` ✅ existe · **`ADR-0031` NAO existe** —, e so depois o contador foi corrigido de **`0030` para `0032`**. **`SF-32` codificou a causa** — *criar `Spec` e incrementar o contador sao a mesma mudanca* — e a regra vale para toda sequencia (`CV-04`, `IX-02`). **Quarta ocorrencia da familia de `RD-32`**; metodo `V1` de [MEM-APR-0006](../memory/aprendizado/MEM-APR-0006-exercer-o-contador-revela-o-defeito.md) |
| **Contador exercido, nao lido (Missao 1.13.4.2)** | Antes de atribuir **`0027`, `0028` e `0029`**, testou-se a existencia de `ADR-002[789]-*.md` contra a **copia datada anterior as edicoes** *(`_backups/…_2026-07-31_pre-missao-1-13-4-2/`)*: **nenhum dos tres existia**, e a contagem foi de **26 → 29** — `V1` de [MEM-APR-0006](../memory/aprendizado/MEM-APR-0006-exercer-o-contador-revela-o-defeito.md) |
| Numeros reservados | nenhum |
| **Contador exercido, nao lido** | Antes de atribuir **`0026`**, testou-se a existencia de `ADR-0026-*.md` contra a **copia datada anterior as edicoes** *(`_backups/…_2026-07-31_pre-missao-1-13-4/`)*: **nao existia**, e a contagem foi de **25 → 26**. Idem para `RFC-0021` *(20 → 21)* e `FIT-2026-019` *(18 → 19)*. Antes de atribuir **`0024`** e **`0025`**, testou-se a existencia de arquivo com esses nomes contra a **copia datada anterior as edicoes**: **nenhum existia**, e a contagem foi de **23 → 25**. Idem para `RFC-0020` *(19 → 20)* e `FIT-2026-017` *(16 → 17)*. Antes de atribuir **`0022`** e **`0023`**, testou-se a existencia de arquivo com esses nomes: **nenhum existia**. E a verificacao `V1` de [MEM-APR-0006](../memory/aprendizado/MEM-APR-0006-exercer-o-contador-revela-o-defeito.md), e **a primeira vez que ela e exercida apos `RD-32` ter codificado a causa em `SF-32`** |
| **Achado `RD-44`, corrigido nesta emissao** | **A tabela abaixo terminava em `ADR-0020`: `ADR-0021` nunca recebeu linha**, embora tenha sido criado na Missao 1.13 e o contador tenha sido corrigido na mesma missao. **O contador foi atualizado e o indice nao** — `CV-04` e `IX-02` outra vez, **na propria missao que codificou a causa em `SF-32`**. **Terceira ocorrencia da familia**, e a primeira em **campo diferente do contador** |
| **Correcao de `RD-32`** | Este contador declarava **`0019` / `0020`** enquanto a tabela abaixo ja listava **`ADR-0020`** — defasagem de **um**, encontrada ao **pedir** o numero de `ADR-0021`. Confiar nele produziria **colisao de identificador**, contra `FND-03 §2.3`. **Segunda ocorrencia da familia** *(a primeira esta em nota de [`governance/README`](../governance/README.md))*; a causa e `CV-04`, codificada agora em **`SF-32`** de [ADR-0021](ADR-0021-framework-de-specifications.md) — *criar artefato de sequencia e incrementar o contador sao a mesma mudanca*. Metodo em [MEM-APR-0006](../memory/aprendizado/MEM-APR-0006-exercer-o-contador-revela-o-defeito.md) `V1` |

> Numero **nunca e reaproveitado**, mesmo em caso de revogacao ou descarte (FND-03 §2.3).
> O numero e atribuido por DEP-GOV **antes** do preenchimento — nunca autoatribuido.

## Decisoes

| ID | Titulo | Classe | Tipo | Status | **Ratificacao** | Data | Supera |
|---|---|---|---|---|---|---|---|
| [ADR-0001](ADR-0001-adocao-da-fundacao-organizacional.md) | Adotar a Fundacao Organizacional como fonte oficial de verdade | C3 | 1 | `ativo` | **ratificada** | 2026-07-28 | — |
| [ADR-0002](ADR-0002-adocao-da-camada-de-capabilities.md) | Adotar a camada de Capabilities como camada intermediaria | C3 | 1 | `ativo` | **ratificada** | 2026-07-28 | — |
| [ADR-0003](ADR-0003-adocao-do-enterprise-meta-model.md) | Adotar o Enterprise Meta Model como definicao fechada das entidades | C3 | 1 | `ativo` | **ratificada** | 2026-07-28 | — |
| [ADR-0004](ADR-0004-adocao-do-architecture-fitness-check.md) | Adotar o Architecture Fitness Check, com portao QG-6 | C3 | 1 | `ativo` | **ratificada** | 2026-07-28 | — |
| [ADR-0005](ADR-0005-proibicao-de-autoverificacao.md) | Proibir autoverificacao — nenhuma entidade verifica a si propria | C2 | 2 | `ativo` | nao exigida | 2026-07-28 | — |
| [ADR-0006](ADR-0006-adocao-do-enterprise-artifact-framework.md) | Adotar o Enterprise Artifact Framework | C3 | 1 | `ativo` | **ratificada** | 2026-07-28 | — |
| [ADR-0007](ADR-0007-fronteira-greenfield-legado.md) | Declarar a fronteira entre o LucaX Enterprise OS e o LucaX Legacy | C2 | 2 | `ativo` | nao exigida | 2026-07-28 | — |
| [ADR-0008](ADR-0008-uma-fonte-multiplas-projecoes.md) | Adotar "uma fonte, multiplas projecoes" para tabela normativa | C2 | 2 | `ativo` | nao exigida | 2026-07-28 | — |
| [ADR-0009](ADR-0009-o-que-conta-como-emenda-de-artefato.md) | Definir que "emendado" e a alteracao que incrementa MAIOR ou MENOR | C2 | 2 | `ativo` | nao exigida | 2026-07-28 | — |
| [ADR-0010](ADR-0010-contrato-de-conhecimento-do-soberano.md) | Adotar o Contrato de Conhecimento sobre o Soberano | C2 | 2 | `ativo` | nao exigida | 2026-07-28 | — |
| [ADR-0011](ADR-0011-contrato-de-carta-de-departamento.md) | Adotar o Contrato de Carta de Departamento | C2 | 2 | `ativo` | nao exigida | 2026-07-28 | — |
| [**ADR-0012**](ADR-0012-integridade-do-ato-de-ratificacao.md) | Fixar que o ato de ratificacao vincula o **conteudo normativo**, com tres hashes e teste de reconstrucao | C2 | 2 | `ativo` | nao exigida | 2026-07-28 | — |
| [**ADR-0013**](ADR-0013-criterio-de-horizonte-e-consolidacao.md) | Fixar o criterio de **horizonte avaliavel** e de revisao de consolidacao determinado pelo Soberano, **sem emendar fundacional** | C2 | 2 | `ativo` | nao exigida | 2026-07-28 | — |
| [**ADR-0014**](ADR-0014-candidato-emenda-fnd-01-7-3-homologa.md) | Emenda **C3** a FND-01 §7.3 e §11: separar **ratificacao** de **homologacao** | **C3** | 2 | **`ativo`** | **ratificada** — [MSG-2026-0004](../memory/operacional/MSG-2026-0004-ato-soberano-cartas-emenda-constitucional-e-regime-do-fitness-check.md) | 2026-07-29 | **Promulga FND-01 1.4.0; fecha IC-2** |
| [**ADR-0015**](ADR-0015-fitness-check-e-parecer-nao-decisao.md) | `Fitness Check` e `Revisao Arquitetural` sao **pareceres M1** e **nao se ratificam** — `FT-10` a `FT-15` | **C2** | 2 | **`ativo`** | nao exigida | 2026-07-29 | **Responde Q2**; formaliza o **item 4** do ato de 2026-07-29 |
| [**ADR-0016**](ADR-0016-semantica-da-matriz-de-interacao.md) | Emenda **C3** a **FND-02 §4**: semantica da matriz, codigo `R`, celula multivalorada, `MI-01` a `MI-06` e **12 celulas** | **C3** | 2 | **`ativo`** | **ratificada** — [MSG-2026-0006](../memory/operacional/MSG-2026-0006-ato-soberano-aplicacao-integral.md) | 2026-07-29 | **RD-02 FECHADO.** **FND-02 1.3.0 promulgada e em vigor** |
| [**ADR-0017**](ADR-0017-harmonizacao-do-regime-do-parecer.md) | Emenda **C3** a **FND-09 §8.2** *(fonte)* e **FND-10 §10.3** *(cascata)*: linha `Fitness Check` passa a `—` | **C3** | 2 | **`ativo`** | **ratificada** — [MSG-2026-0006](../memory/operacional/MSG-2026-0006-ato-soberano-aplicacao-integral.md) | 2026-07-29 | **RD-09 FECHADO.** Aplicada **no cumulativo**: FND-09 **1.5.0** e FND-10 **1.4.0**; as intermediarias **1.4.0** e **1.3.0** nao foram promulgadas |
| [**ADR-0018**](ADR-0018-liberacao-do-portao-qg-1.md) | Emenda **C3** a **FND-01 §6.2**: o portao **`QG-1`** passa a ser liberado por **`DEP-EXE`**, e a subsecao recebe nota que distingue **liberar portao** de **aprovar artefato** | **C3** | 2 | **`ativo`** | **ratificada** — [MSG-2026-0006](../memory/operacional/MSG-2026-0006-ato-soberano-aplicacao-integral.md) | 2026-07-29 | **RD-14 FECHADO.** **FND-01 1.5.0 promulgada e em vigor** |
| [**ADR-0019**](ADR-0019-aprovador-e-ratificador-de-spec.md) | Emenda **C3** a **FND-09 §8.2** *(fonte)* e **FND-10 §10.3** *(cascata)*: linhas `SPC` e `Spec` passam a **remeter a classe**, e o conflito e **registrado como erro da propria tabela** | **C3** | 2 | **`ativo`** | **ratificada** — [MSG-2026-0006](../memory/operacional/MSG-2026-0006-ato-soberano-aplicacao-integral.md) | 2026-07-29 | **RD-15 FECHADO.** **RD-19 resolvido pelo cumulativo**: FND-09 **1.5.0** e FND-10 **1.4.0**, aplicadas **sobre** a emenda de ADR-0017, na ordem de PS-2026-008 §5 |
| [**ADR-0020**](ADR-0020-regime-ministerial-de-promulgacao-e-ativacao.md) | **Promulgar e ativar sao operacoes ministeriais**, decorrentes de aprovacao ou ratificacao valida: institui **`PA-01` a `PA-14`** e a **matriz de regime operacional** como projecao declarada | **C2** | 2 | **`ativo`** | **nao exigida** *(C2 · Tipo 2)* | 2026-07-29 | **RD-22 FECHADO por refutacao de premissa.** **0 fontes emendadas · 0 titulares criados · 0 atos exigidos.** As regras vivem **no proprio ADR**, na forma de `ADR-0012` e `ADR-0015`. Habilita **`GO-TO-SPECS`** — [PT-2026-006](../governance/relatorio-transicao-2026-07-29-fechamento-operacional.md) |
| [**ADR-0021**](ADR-0021-framework-de-specifications.md) | **Framework de Specifications** — institui **`SF-01` a `SF-32`** dentro do proprio ADR: contrato de 21 blocos, semantica normativa, 7 perfis, matriz de 50 celulas, `DoR`/`DoD`, mudanca e economia de contexto | **C2** | 2 | **`ativo`** | **nao exigida** *(C2 · Tipo 2)* | 2026-07-29 | **`RD-23` FECHADA** com `TPL-spec` **1.1.0**. **0 fontes emendadas · 0 titulares criados.** Declarava que **nenhuma `Spec` e criavel** — `RD-33`, ✅ **FECHADO em 2026-08-01**: a `Spec` **de produto** passou a ser criavel com `S1` consumida; a **interdepartamental** segue bloqueada por `S2` deferida, achado **`RD-88`**. **Superado PARCIALMENTE por `ADR-0022`, so quanto a sede normativa**; `status` permanece `ativo`, texto e frontmatter **intactos** |
| [**ADR-0022**](ADR-0022-sede-canonica-do-framework-de-specifications.md) | **Emenda C3 que cria `FND-11`** — sede fundacional de `SF-01` a `SF-32`, com **30 de 32** regras migrando **byte a byte** e **1** alteracao de merito declarada *(`SF-32`, `M1` → `M2`)* | **C3** | **1** | **`ativo`** | **ratificada** — [MSG-2026-0007](../memory/operacional/MSG-2026-0007-ato-soberano-vigencia-do-framework-de-specifications.md) | 2026-07-29 | **`supera: [ADR-0021]` — so a sede** *(§5.4)*. Emenda `FND-01` **1.6.0** e `FND-03` **1.6.0**, **ambas em vigor** no conjunto atomico com `FND-11`. **0 titulares · 0 portoes · 8 niveis de hierarquia antes e depois.** [PS-2026-009](../governance/pacote-soberano-2026-07-29-fnd-11.md) |
| [**ADR-0023**](ADR-0023-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md) | **Propagacao de `ADR-0018` e `ADR-0019` as Cartas de `DEP-PRD` e `DEP-EXE`** — corrige as **8** afirmacoes falsas e faz `QG-1` ter **titular declarado em Carta pela primeira vez** | **C2** | 2 | **`ativo`** | **nao exigida** *(C2 · Tipo 2)* | 2026-07-29 | **`RD-31` FECHADA** — as duas Cartas **entraram em vigor** pelo ato de 2026-07-30. Abriu **`RD-37`**, **tambem fechado** no mesmo ato. Aprovado por **DEP-GOV**, porque `DEP-EXE` e o autor. [PS-2026-010](../governance/pacote-soberano-2026-07-29-rd-31.md) |
| [**ADR-0024**](ADR-0024-conformidade-de-contrato-das-fundacionais.md) | **Emenda C3 que fecha `RD-27`** — backfill dos campos de `AC-08` em **`FND-01`** *(4)* e **`FND-02`** *(5)*, e correcao de **`FND-10 §8.5`** *(6 valores e a regra de leitura)*, com **`0` bytes de corpo alterados nos tres** | **C3** | 2 | **`ativo`** | **ratificada** — [MSG-2026-0007](../memory/operacional/MSG-2026-0007-ato-soberano-vigencia-do-framework-de-specifications.md) | 2026-07-30 | **`RD-27` FECHADA integralmente** — as tres fundacionais **entraram em vigor** pelo ato de 2026-07-30. `FND-01` **1.7.0 cumulativa** sobre a 1.6.0 de `ADR-0022`. Abre **`RD-45`** e **`RD-46`**, e **fecha os dois**. [PS-2026-011](../governance/pacote-soberano-2026-07-30-rd-27.md) |
| [**ADR-0025**](ADR-0025-extensao-da-propagacao-de-qg-1-as-cartas-restantes.md) | **Extensao da cascata de `ADR-0018`** as Cartas de `DEP-OPS`, `DEP-GRW` e `DEP-TLS` — **uma** afirmacao falsa por Carta, e **nenhuma outra responsabilidade tocada** | **C2** | 2 | **`ativo`** | **nao exigida** *(C2 · Tipo 2)* | 2026-07-30 | **`RD-37` FECHADA** — a familia das **9** Cartas foi de **11 afirmacoes falsas em 4** para **`0` em `0`**, **medido no acervo em vigor** apos o ato de 2026-07-30. **Primeira dispensa de RFC do acervo** (`FND-04 §2`), com as duas condicoes verificadas. Abre **`RD-47`**. Aprovado por **DEP-GOV**, porque `DEP-EXE` e o autor. [PS-2026-012](../governance/pacote-soberano-2026-07-30-rd-37.md) |
| [**ADR-0026**](ADR-0026-admissao-do-medally-como-primeiro-produto.md) | **Admissao do medAlly pelo portao de `ADR-0007` e criacao de `PRO-medally`**, primeiro Produto do acervo — **identidade e proposta admitidas, `0` bytes do repositorio** | **C2** | **1** | **`em-revisao`** | **`pendente`** | *(nao ocorrido)* | **NAO ESTA EM VIGOR.** **Primeiro exercicio do portao de origem externa**: `G1`–`G4` comprovados, `G5` preparado, **`G3` = `REWRITE`**. Abre **`RD-54`** e **`RD-55`**. **`Q1` bloqueante** — a leitura da decisao **7** de `PT-2026-009 §1` e do Soberano. [PS-2026-014](../governance/pacote-soberano-2026-07-31-medally.md) |
| [**ADR-0027**](ADR-0027-classe-de-admissao-de-existencia-no-portao-de-origem-externa.md) | **`G0` e `RECOGNIZE` no portao de origem externa** — admitir existencia sem avaliar conteudo | **C2** | **2** | **`ativo`** | **`nao-exigida`** | *(nao exigida — `C2`/`Tipo 2`)* | ✅ **EM VIGOR desde 2026-07-31**, aprovado por **DEP-EXE** no rito `C2` com parecer de DEP-GOV, pelo **oitavo ato soberano** ([MSG-2026-0008](../memory/operacional/MSG-2026-0008-ato-soberano-emendas-e1-e-e3.md) item **I**). **`RC-1` esta EM VIGOR:** o `REWRITE` da 1.13.4 **le-se `RECOGNIZE`**, e os cinco artefatos daquela missao **nao sao editados** (`RC-2`). Supera **`ADR-0007 §5.3` linha `G3` e `§5.4`**, quanto a lista e so quanto a ela, com **`0` bytes** em `ADR-0007`. Fecha `RD-54` e `RD-55` **na vigencia**. Regra `RC-1` reclassifica o `REWRITE` da 1.13.4. [PS-2026-015](../governance/pacote-soberano-2026-07-31-emendas-de-instrumento.md) |
| [**ADR-0028**](ADR-0028-independencia-de-verificacao-por-fornecedor.md) | **Independencia de verificacao aferida por FORNECEDOR**; `revisor` ≠ `autor` vira pre-condicao | **C3** | **1** | **`em-revisao`** | **`pendente`** | *(nao ocorrido)* | **NAO ESTA EM VIGOR.** Supera **`AC-03` de `FND-10 §2.5` quanto a suficiencia** — **nao** `ADR-0005`, que nao contem criterio. **`0` contra `131`, base `138`.** Agrava `RD-62`, declarado. [PS-2026-015](../governance/pacote-soberano-2026-07-31-emendas-de-instrumento.md) |
| [**ADR-0029**](ADR-0029-superacao-de-ato-por-evidencia-posterior.md) | **Caminho de superacao de ato por evidencia posterior** — `SA-1` a `SA-6` | **C3** | **1** | **`ativo`** | **`ratificada`** | **2026-07-31** — oitavo ato | ✅ **EM VIGOR e RATIFICADO** pelo **oitavo ato soberano** ([MSG-2026-0008](../memory/operacional/MSG-2026-0008-ato-soberano-emendas-e1-e-e3.md) item **II**), com o **registro de atos superados** de `SA-6` criado e o contador em **`0`** — [atos-superados](../governance/atos-superados.md). **Nenhuma norma revogada** — lacuna de omissao, medida em **`0`** caminhos e **7 de 7** atos `ativo`. `ADR-0012` vira **pre-condicao**, `0` bytes. [PS-2026-015](../governance/pacote-soberano-2026-07-31-emendas-de-instrumento.md) |
| [**ADR-0030**](ADR-0030-admissao-do-nxtrack-como-primeiro-produto.md) | **Admissao do nXtrack** com `G0` = `IDENTIDADE` e `G3` = `RECOGNIZE`; cria `PRO-nxtrack` | **C2** | **1** | **`ativo`** | **`ratificada`** | **2026-08-01** — nono ato | ✅ **EM VIGOR e RATIFICADO** pelo **nono ato soberano** ([MSG-2026-0009](../memory/operacional/MSG-2026-0009-ato-soberano-admissao-do-nxtrack.md) item **I**), **aplicado** pela Missao 1.13.4.5 — `H-P` conferido `906dccd3…719fa`, `H-N` invariante, `atualizado_em` **nao tocado**. **Cria o primeiro Produto do acervo**, [`PRO-nxtrack`](../products/nxtrack/carta.md). **Segunda** passagem pelo portao de `ADR-0007` e a **primeira sob a norma emendada** — gatilho de `ADR-0027 §12`. `G3` determinado **entre dois membros**: `RETIRE` descartada por **fato citado** *(decisao 7 de `PT-2026-009`)*, nunca por eliminacao. **`0` bytes** do candidato, **`0`** fundacionais, **`0`** historicos. `Tipo 1` **fixado por norma** (`FND-09 E-17`), nao pelo custo. Abre `RD-71` a `RD-75`. [PT-2026-014](../governance/relatorio-transicao-2026-08-01-portao-nxtrack.md) · [PS-2026-016](../governance/pacote-soberano-2026-08-01-nxtrack.md) |
| [**ADR-0031**](ADR-0031-primeira-spec-governanca-de-dado-pessoal-do-nxtrack.md) | **Cria `SPC-001`, a primeira `Spec` do acervo**, sobre `LM-6(a)` de `PRO-nxtrack`, em `C2 · Tipo 2` | **C2** | **2** | **`ativo`** | **`nao-exigida`** | **2026-08-02** — DEP-EXE, com parecer de DEP-GOV | ✅ **EM VIGOR.** `C2 · Tipo 2` **nao exige ato do Soberano** (`FND-04 §2.1`). Eleva a classe acima do piso `C1` de `FND-04 §6` por **colisao medida** entre a coluna `C1 · T2` de `SF-10` e `FND-04 §3.1` — *Proponente = Aprovador* para `SPC`, que `LV-03` torna **nula**. §5 declara a elevacao **restrita a esta criacao**. **Primeiro `ADR` do acervo cujo autor e DEP-PRD.** Abre `RD-91` a `RD-94`. [SPC-001](../products/nxtrack/specs/SPC-001-governanca-de-dado-pessoal-do-nxtrack.md) · [FIT-2026-024](../governance/fitness/FIT-2026-024-primeira-spec.md) · [PT-2026-017](../governance/relatorio-transicao-2026-08-02-primeira-spec.md) |
| [**ADR-0032**](ADR-0032-separacao-de-proponente-e-aprovador-na-spec-c1.md) | **Emenda `C3` que sana `RD-91`** — a aprovacao de `Spec` `C1` passa do **proprietario**, que a propoe, para **DEP-EXE**. `1` celula de `FND-09 §8.2` + `1` da matriz de `SF-10` + `6` linhas em `2` Cartas | **C3** | 2 | **`ativo`** | **`ratificada`** | [MSG-2026-0010](../memory/operacional/MSG-2026-0010-ato-soberano-emenda-que-sana-rd-91.md) | ✅ **EM VIGOR desde 2026-08-02** — ratificado pelo **item I do decimo ato** e aplicado pela **Missao 1.13.5.2**, que promulgou os quatro objetos: `FND-09` **1.6.0**, `FND-11` **1.1.0**, Cartas `DEP-PRD` e `DEP-EXE` **1.2.0**, com **`H-P` `4` de `4`**, **`H-N` invariante `5` de `5`** e **`IR-09` `4` de `4`**. *(Enunciado anterior, preservado: ⚠️ NAO VIGORA — espera ato.)* A celula que `RD-91` nomeava *(`FND-11 §5`)* **nao era a sede**: reproduz **literalmente** `FND-09 §8.2` linha `SPC` e `FND-04 §2.1` linha `C1`, e por `PJ-03` + `FND-01 §10` emendar so a projecao **nao sanaria**. **`0` bytes em `FND-04` · `0` titulares criados · `0` regras de conteudo de `Spec` tocadas · `SPC-001` NAO reclassificada.** **`RD-91` FECHA PARCIALMENTE** — so quanto a `C1`; **`C0 · T2` segue ABERTA** por decisao expressa do item V. Declara e nao corrige `RD-96` *(linha `PRJ`)*, `RD-97` *(linha `TPL`)*, `RD-98`, `RD-99` e `RD-100` — e o item IV **ordena missao propria** para `PRJ` e `TPL`, que o item VII **proibe comecar** antes de conferida esta aplicacao. [PT-2026-019](../governance/relatorio-transicao-2026-08-02-aplicacao-item-vi.md) · [RFC-0027](../rfcs/RFC-0027-separacao-de-proponente-e-aprovador-na-spec-c1.md) · [FIT-2026-025](../governance/fitness/FIT-2026-025-emenda-de-sf-10.md) · [PS-2026-017](../governance/pacote-soberano-2026-08-02-rd-91.md) · [PT-2026-018](../governance/relatorio-transicao-2026-08-02-emenda-sf-10.md) |
| [**ADR-0033**](ADR-0033-framework-de-skills.md) | **Institui o Framework de Skills — `SK-01` a `SK-26`**, dentro do proprio ADR, **`C2 · Tipo 2`, `ratificacao: nao-exigida`, `0` atos**. Recebe `SKL` de `FND-03 §3.5` e `FND-09 §E-13` **sem criar entidade, tipo, template, portao ou campo novo** — e `gatilho` **nao e campo novo**: `FND-09 §E-13` ja o lista entre os **atributos minimos**. **1 alteracao de merito, isolada:** `SK-26` passa de `M2` a **`M1`**, porque `ADR` e `M1` (`FND-10 §6.2`). **NAO libera `GO-TO-SKILLS`** | **ativo** |
| [**ADR-0034**](ADR-0034-primeira-skill-copia-datada.md) | **Cria a PRIMEIRA `Skill` do acervo** — `SKL-custodia-criar-copia-datada` —, `C2 · Tipo 2`, **`0` atos**. **`GO-TO-SKILLS` passa a EXERCIDO, e exercer NAO e liberar** (`FND-01 §6.2`). **`0` bytes de codigo entraram**: o canonico recebe a **ficha**. **`SK-03` reprovou o nome externo** *(`backup-datado` e substantivo)* e o renomeou. Custo **`5`** artefatos — os mesmos de `SPC-001` | **ativo** |
| [**ADR-0035**](ADR-0035-segunda-skill-varrer-credencial.md) | **Cria a SEGUNDA `Skill` do acervo** — `SKL-seguranca-varrer-credencial` —, `C2 · Tipo 2`, **`0` atos**, e **mede o que `n = 1` nao alcanca**. **`SK-24` foi CALCULADA e provada VAZIA:** mediana `181,5`, limiar `363`, maior instancia `188` — e a algebra mostra que com `2` instancias **nenhum valor pode disparar**, porque `b > a + b` exigiria `a < 0`. **`SK-09` e `SK-10` reprovaram IDENTICAMENTE em caso disjunto: o defeito e do FRAMEWORK, nao do caso.** **`SK-05`, `SK-12` e `SK-22` exercidas pela primeira vez** — cobertura acumulada **`25` de `26`**. **Custo `5` artefatos, igual ao da primeira: o custo e do RITO, nao da novidade.** **NAO abre o `ADR` sucessor** | **ativo** |
| [**ADR-0036**](ADR-0036-terceira-skill-provar-restauracao-de-backup.md) | **Cria a TERCEIRA `Skill` do acervo** — `SKL-custodia-provar-restauracao-de-backup` —, `C2 · Tipo 2`, **`0` atos**, e **mede o PISO DE `n` de `SK-24`**. **⭐ A regra deixa de ser VAZIA:** mediana **`188`** *(`175`, `188`, `231`)*, limiar **`376`**, maior **`231`** — **nao dispara, mas pela primeira vez PODERIA**, porque em `n = 1` e `n = 2` disparar exigia `a < 0` e em `n = 3` exige `c > 2b`, que **tem solucao**. **`SK-09` e `SK-10` reprovam pela TERCEIRA vez, e com o autor CIENTE dos defeitos — o que ELIMINA a hipotese de defeito de LEITOR.** **Corrige a razao registrada de `SK-21`:** ela nao espera agentes, espera a **primeira ARESTA de dependencia**, e ha `0`. **Custo `5` pela terceira vez.** **NAO abre o `ADR` sucessor** | **ativo** |
| [**ADR-0037**](ADR-0037-sucessor-parcial-do-framework-de-skills.md) | ⭐ **SUPERA PARCIALMENTE `ADR-0033`** pelo resultado **`AJUSTAR`** de `FND-07 §8.1`, e institui **`SK-27` a `SK-30`**. `C2 · Tipo 2`, **`0` atos**. **`ADR-0033` fica `ativo`, com `0` bytes e `22` regras vigentes** — superar o todo obrigaria a **reproduzir `22` regras** *(contra `PJ-01`)* e **proibiria por `LN-03`** toda relacao nova, e as `3` fichas ja a declaram. **`SK-27`** — piso de populacao/aresta, **com a classe VARRIDA: `5` membros, nao `2`**, e **`SK-25` jamais fora medida por missao alguma**. **`SK-28`** — `11` blocos + `1` atributo de frontmatter **nao e `12`**. **`SK-29`** — o rito da classe vem **inteiro**. **`SK-30`** — saidas plausiveis e erradas no **plural**. ⚠️ **`FIT-2026-029 R4` avaliado e deixado de FORA por `1` de `3` instancias** — a regra nova aplicada **contra o interesse da missao** | **ativo** |
| [**ADR-0038**](ADR-0038-a-mente-reconhece-o-corpo.md) | ⭐ **A MENTE RECONHECE O CORPO.** `C2 · Tipo 2`, **`0` atos**, rito inteiro `RFC-0033 → ADR-0038 → FIT-2026-031` **por escolha expressa do Fundador** — a dispensa de RFC estava disponivel e **nao foi usada**. Institui as **4 camadas** *(Mente · Oficina · Corpo · Legado)* com caminhos reais; o **Corpo** (`lucax-enterprise`, FastAPI+LangGraph, provado em 2026-08-12: pilha Docker do zero, RLS `EXIT=0` como `app_rt`, 25 testes) e producao **FORA do acervo e do fence, por desenho**; **membrana `M1–M5`** — producao **nunca** escreve na Mente, norma sobe por `RFC → ADR`, evidencia volta como **proposta**, segredo **nao cruza**; a Policy Engine do Corpo e **PROJECAO de `FND-04`**, e em divergencia **prevalece a fonte** (`PJ-03`). Tradeoff declarado: o acervo passa a apontar para `3` repositorios que **nao mede** | **ativo** |

### Ratificacao — [INC-2026-001 §11](../governance/incidents/INC-2026-001-ratificacao-inferida.md), encerrado

As cinco decisoes C3/Tipo 1 foram **ratificadas em ato unico, explicito e datado do Soberano
em 2026-07-28**. O ato e registrado **uma unica vez**, na fonte canonica
[INC-2026-001 §11](../governance/incidents/INC-2026-001-ratificacao-inferida.md); a coluna
acima e **projecao declarada** dessa fonte (ADR-0008, PJ-02). O incidente foi fechado apos
verificacao independente de DEP-QAR (§12).

> **Nenhum arquivo de ADR foi editado** (LV-04, CC-01, e determinacao expressa do ato). O
> frontmatter de cada ADR permanece congelado no ato de aprovacao — inclusive ADR-0006, que
> continua declarando `aprovado` / `pendente` no proprio arquivo. **A fonte corrente do estado
> de ratificacao e INC-2026-001 §11; esta tabela a projeta.** Divergencia entre as duas e
> defeito desta tabela, nunca da fonte.

> **`ADR-0016` a `ADR-0019` seguem regime diferente, e a diferenca importa.** Nelas o
> frontmatter **foi** transitado — `status` `em-revisao` -> `ativo` e `ratificacao` `pendente` ->
> `ratificada` —, porque o **sexto ato soberano**
> ([MSG-2026-0006](../memory/operacional/MSG-2026-0006-ato-soberano-aplicacao-integral.md))
> autorizou expressamente a operacao **`O4`** e publicou o **`H-P` projetado de cada uma**
> **antes** de o arquivo existir. Os quatro `H-P` medidos **reproduzem os projetados nos 64
> digitos**, e **`H-N` ficou invariante nas quatro** (IR-02, IR-06): a ratificacao foi aplicada
> **sem destruir a propria prova**. Aqui a **fonte corrente do estado e o proprio frontmatter**
> (FND-10 §5.4), e nao um incidente — e e por isso que os arquivos puderam ser tocados sem
> violar LV-04.

> **`ADR-0022` a `ADR-0025` seguem o mesmo regime de `O4`, e o setimo ato o exerceu.** O
> **ato soberano de 2026-07-30**
> ([MSG-2026-0007](../memory/operacional/MSG-2026-0007-ato-soberano-vigencia-do-framework-de-specifications.md))
> publicou `H-A`, `H-N` e `H-P` das quatro **antes** da escrita e autorizou `O4` **de forma
> assimetrica**: `ADR-0022` e `ADR-0024` transitaram **`status` e `ratificacao`**; `ADR-0023` e
> `ADR-0025` transitaram **somente `status`**, porque `C2 · Tipo 2` **nao exige ratificacao** e
> o campo permanece `nao-exigida`. Os quatro `H-P` medidos **reproduzem os projetados nos 64
> digitos**, **`H-N` ficou invariante nas quatro** e o **`IR-09`** reconstruiu **`H-A` nas
> quatro** revertendo apenas os campos de `IR-03`. **`0` bytes fora do diff autorizado.**

| Valor da coluna | Significado |
|---|---|
| pendente | Aguarda ato explicito e datado do Soberano sobre o texto final. Silencio nao ratifica (GV-05) |
| **ratificada** | Ato explicito registrado, com data e forma, em fonte canonica referenciada |
| nao exigida | C0, C1, ou C2/Tipo 2 — a classe nao exige ratificacao (FND-07 §2.3) |

> Nenhum campo desta coluna e preenchido por quem produziu o ADR (CV-09, MEM-APR-0001).

## Como registrar uma decisao

1. Verifique se e **decisao relevante** (FND-07 §1).
2. Classifique: impacto C0–C3 × reversibilidade Tipo 1/2 (FND-07 §2).
3. Escolha o instrumento pela matriz de FND-07 §2.3.
4. Solicite o numero a DEP-GOV e atualize o contador acima.
5. Use [`TPL-adr`](../foundation/templates/TPL-adr.md).
6. Passe pelo ciclo de 14 etapas (FND-07 §5).
7. Se for C2 ou C3, o encerramento exige **Verificacao de Aptidao Arquitetural** (QG-6,
   [`governance/fitness/`](../governance/fitness/)).
8. Ao aprovar, o arquivo torna-se **imutavel** (LV-04). Corrigir = superar (FND-07 §7).

## Regras rapidas

| Situacao | Regra |
|---|---|
| Decisao Tipo 1 | Sempre exige ratificacao do Soberano, qualquer que seja a classe |
| ADR aprovado com erro | Nao se edita: supera-se com novo ADR |
| Decisao sem alternativas | Registro invalido (VD-01) |
| Decisao sem gatilho de revisao | Devolvida por DEP-GOV (VD-09) |
| Decisao C2/C3 sem `FIT` emitido | Nao encerra (CV-07, FT-05) |
| Decisao que cria tipo de entidade novo | Sempre C3, pelo rito de FND-09 §11.1 |
| Decisao C3/Tipo 1 sem ato explicito do Soberano | **Ratificacao pendente**; permanece `aprovado`, nao entra em `ativo` (CV-09) |
| Secao de ratificacao preenchida pelo produtor do ADR | Registro **nulo** — quem registra e papel distinto (CV-09, MEM-APR-0001) |
