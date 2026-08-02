---
id: IDX-artifact-registry
titulo: Catalogo Mestre do Acervo
tipo: relatorio
versao: 2.20.0
status: ativo
camada_memoria: operacional
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-QAR
criado_em: 2026-07-28
atualizado_em: 2026-08-02
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0006, ADR-0007, ADR-0008, ADR-0009, ADR-0010, ADR-0011, ADR-0012, ADR-0020, ADR-0021, ADR-0026]
substitui: []
substituido_por: null
resumo: Classifica os artefatos do acervo por tipo documental, entidade, perfil, custo medido e proveniencia, e materializa a baseline canonica 218.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
projecao_de: o frontmatter e o corpo de cada artefato-fonte listado
---

# Catalogo Mestre do Acervo

## Proposito
Classificar **todos** os artefatos do sistema por tipo documental, entidade, perfil de
contexto e custo medido, e guardar o resumo operacional de cada um — para que decidir se um
artefato e relevante nao exija abri-lo.

## Escopo
| Item | Definicao |
|---|---|
| Inclui | Os **217** artefatos em Markdown do repositorio, sem excecao — **inclusive a raiz `products/`, criada pelo nono ato**; a **baseline canonica** (§10). *O valor declarava **206**, e antes **164** — familia de `RD-57`; recontado por ferramenta nesta emissao* |
| Nao inclui | Contadores de sequencia — aqueles vivem nos indices por diretorio (RG-04); conteudo do **LucaX Legacy**, que nao e acervo (ADR-0007 §5.1) |
| Subordinado a | [FND-10 §10.4](../foundation/10-artifact-framework.md) |

## Responsaveis
| Papel | Responsavel |
|---|---|
| Proprietario | DEP-GOV |
| Curadoria do resumo e do custo | DEP-KMS |
| Verificacao de sincronia | DEP-QAR |

---

## 1. Natureza deste artefato

**Vista derivada (M3).** Nao contem informacao original: toda linha aponta ao artefato-fonte.

| # | Regra |
|---|---|
| RG-01 | Nao contem informacao original. Informacao que so exista aqui deve migrar para a fonte |
| RG-02 | Artefato sem entrada aqui e **nao localizavel** — falha DoD-7 |
| RG-03 | Desatualizado apos mudanca aprovada = **mudanca incompleta** (CV-04), nao norma nova |
| RG-04 | **Nao substitui os indices por diretorio:** aqueles sao contadores oficiais; este e a visao transversal |
| RG-05 | **Nenhum arquivo auxiliar por artefato** — a classificacao vive aqui, por referencia |

## 2. Estado do acervo

Medicao de **2026-08-02**, ao encerramento da **Missao 1.13.5.1 — a emenda que sana `RD-91`**,
produzida pelo rito `C3` completo e **nao aplicada**.

| Medida | Valor | Fonte |
|---|---|---|
| Artefatos | **228** — **`+5`** sobre `BL-2026-08-02-01`: `RFC-0027`, `ADR-0032`, `FIT-2026-025`, `PS-2026-017` e `PT-2026-018`. **`0` removidos.** *(Enunciado anterior, preservado: **223**, `+5` sobre `BL-2026-08-01-03` — `RFC-0026`, `ADR-0031`, **`SPC-001`**, `FIT-2026-024` e `PT-2026-017`.)* | `ferramentas/baseline.sh`, lista fechada positiva com portao de raiz e portao de split |
| Linhas | **67.279** | idem, sobre os mesmos **228** arquivos |
| Classificados | **227 de 228**, e a **unica** ausencia continua sendo a mesma, nomeada — `roadmap-canonico.md`, achado **`RD-80`**, cujo gatilho disparou pela **QUARTA** vez e **segue nao resolvido** | Este catalogo, **contado por ferramenta** |
| **Reproducao da baseline — instrumento** | **`BL-2026-07-30-01` reproduz nos 64 digitos** *(**185 · 54.190 · `3d8dbea0…84da`**)* sobre a copia datada em que o comando publicado dava **198**. **A baseline sempre esteve certa; o comando e que nao media o que dizia medir** | [PT-2026-012 §2.1](relatorio-transicao-2026-07-31-manutencao-instrumentos.md) |
| Sem tipo documental declarado | **0** | — |
| **Entidades instanciadas** | **12 de 21** | `FND` `ADR` `RFC` `INC` `FIT` `CAP` `DEP` `TPL` `MEM` `MSG` e — **pela primeira vez** — **`PRO`** *(nono ato, item III)* e **`SPC`**, com `SPC-001` em `products/nxtrack/specs/` *(Missao 1.13.5)*. **Nenhuma entidade foi criada:** `PRO` consta de [FND-09 `E-17`](../foundation/09-meta-model.md) desde a fundacao, com identidade `PRO-<slug>` em `products/<slug>/` — **21 permanece**. **Corrigido de 11 para 10** em emissao anterior — achado **RE-05**: `ORG` e `SOBERANO` **nao podem** ter instancia de artefato, por serem as duas unicas entidades **fora do arquetipo A2** (FND-09 §4.2). `IDX` **nao e entidade** (FND-10 §4.7) |
| **Tipos documentais com instancia** | **19 de 33** | §4 e §5. **`Carta de Produto` sai de "sem instancia"** — **primeira instancia do tipo**. **Nenhum tipo novo foi criado:** ele consta de [`FND-10 §4.3`](../foundation/10-artifact-framework.md) desde a origem, com local `products/<slug>/` e template `TPL-carta-produto`, e **33 permanece**. **`Spec` SAI de "sem instancia"** — `SPC-001`, **primeira instancia do tipo**, em `products/nxtrack/specs/`. **Nenhum tipo novo foi criado:** ele consta de [`FND-10 §4.4`](../foundation/10-artifact-framework.md) desde a origem, e **33 permanece** |
| **Cobertura de `perfil_contexto`** | **208 de 208 — 100% classificados · 0 nao classificados** | **§2.1**, pelo metodo de **FND-10 §2.3** |
| **Autoverificacao — medida pelos DOIS criterios** | **`0`** por **divergencia de campo** *(`autor` ≠ `revisor`)* · **`130`** por **independencia de fornecedor**, sobre os **137** artefatos que declaram os dois campos. **Os 7 que sobrevivem ao segundo criterio sao os sete atos do Soberano** | [PT-2026-012 §6.1](relatorio-transicao-2026-07-31-manutencao-instrumentos.md) · **minuta B**, preparada e **nao aplicada** |
| **Nao conformidades de contrato conhecidas** | **`0` vigentes** — `FND-01` **1.7.0** e `FND-02` **1.4.0** entraram em vigor com os **4** e os **5** campos de `AC-08` presentes | Achado **RD-27**, ✅ **FECHADO pelo ato de 2026-07-30** — [ADR-0024](../decisions/ADR-0024-conformidade-de-contrato-das-fundacionais.md) e [PS-2026-011](pacote-soberano-2026-07-30-rd-27.md). O backfill alterou **`H-N`** (`IR-01`, `IR-03`, `IR-05`), e por isso **so podia fechar com ato** — o ato veio |
| Proveniencia `native` | **223 de 223 — 100%**, **inclusive `PRO-nxtrack` e `SPC-001`** | §9. **A admissao do nXtrack NAO produziu artefato `adapted` nem `migrated`:** produziu **um artefato `native`** — a Carta, escrita neste sistema —, porque `G0` e `IDENTIDADE` e **`0` bytes** do repositorio do candidato entraram. *(O valor anterior declarava **208 de 208** com o acervo em **213** — familia de `RD-77`, corrigida aqui **por contagem de ferramenta**.)* |
| **Oitavo ato soberano — CONSUMIDO** | ✅ [MSG-2026-0008](../memory/operacional/MSG-2026-0008-ato-soberano-emendas-e1-e-e3.md), de **2026-07-31**, aplicado pela **Missao 1.13.4.3**. **`ADR-0027` `ativo`** *(aprovado por **DEP-EXE** no rito `C2`, com parecer de DEP-GOV; `ratificacao` permanece `nao-exigida`)* e **`ADR-0029` `ativo` · `ratificada`**. **`H-P` conferido 2 de 2**, `H-N` invariante **2 de 2**, `IR-09` **2 de 2**. **`E2` ADIADA e intacta — `0` bytes nos tres objetos** | §10.17 · [atos-superados](atos-superados.md) |
| **Nono ato soberano — CONSUMIDO** | ✅ [MSG-2026-0009](../memory/operacional/MSG-2026-0009-ato-soberano-admissao-do-nxtrack.md), de **2026-08-01**, aplicado pela **Missao 1.13.4.5** na ordem de [`PS-2026-016 §6.2`](pacote-soberano-2026-08-01-nxtrack.md). **`ADR-0030` `ativo` · `ratificada`** · **`RFC-0025` `aprovado`** *(pela **variante** de `§2.1`, nunca pelo instrumento padrao, que poria `ativo`)* · **`PRO-nxtrack` CRIADO** em `products/nxtrack/carta.md`, `H-A` do aplicado **`fca656a904e67b11b965354233b7352be9cf41131c88fda2baebc30e8eb039e2`**. **`H-P` conferido `2` de `2`**, `H-N` invariante **`2` de `2`**, `IR-09` **`3` de `3`**. **`CA-1` a `CA-6` em `6` de `6`**; **`CA-2` INFORMATIVO** — medido e registrado, jamais exigido como igualdade. **`0` bytes do candidato**: `G0` = `IDENTIDADE` | [PT-2026-015](relatorio-transicao-2026-08-01-aplicacao-nxtrack.md) · [MSG-2026-0009 §8](../memory/operacional/MSG-2026-0009-ato-soberano-admissao-do-nxtrack.md) · §10.19 |
| Baseline vigente | **BL-2026-08-02-01** | §10.0. *(Esta linha declarava `BL-2026-07-31-02`, **seis** emissoes atras — mesma familia de `RD-77`.)* |
| **Portao de origem externa (`ADR-0007 §5.3`)** | **EXERCIDO DUAS VEZES.** **2a passagem, e a PRIMEIRA sob a norma emendada** — Missao 1.13.4.4, sobre o **nXtrack**: **`G0` = `IDENTIDADE`** *(declarado antes de `G1`, `GA-01`)* · **`G1` FECHA por medicao** *(17 de 17 fontes com autoria e data; `0` caminhos sem commit em 183 rastreados)* · **`G2`** com **12** linhas de fit-gap · **`G3` = `RECOGNIZE`**, determinado **entre dois membros** e com `RETIRE` descartada por **fato citado** · **`G4`** por `FIT-2026-023` · **`G5` CONSUMIDO em 2026-08-01** — a decisao formal veio pelo **nono ato**, e a **admissao esta APLICADA**: `PRO-nxtrack` em vigor, `products/` criada. **`0` bytes admitidos**, medido por **`0` colisoes** de hash — [PT-2026-015](relatorio-transicao-2026-08-01-aplicacao-nxtrack.md) · [PT-2026-014](relatorio-transicao-2026-08-01-portao-nxtrack.md) · [PS-2026-016](pacote-soberano-2026-08-01-nxtrack.md). **1a passagem:** sobre **um** candidato nomeado — o **medAlly**. **`G1`–`G4` comprovados · `G5` preparado · `G3` = `REWRITE` · `0` bytes admitidos**. **`RC-1` EM VIGOR desde 2026-07-31:** o registro da 1.13.4 **le-se `G3` = `RECOGNIZE`, com `G0` = `IDENTIDADE`** — a regra vive em [`ADR-0027 §RC-1`](../decisions/ADR-0027-classe-de-admissao-de-existencia-no-portao-de-origem-externa.md) e **os cinco artefatos da 1.13.4 NAO sao editados** (`RC-2`). **`0` hashes mudam, nenhuma baseline e reaberta** (`RC-3`), e a reclassificacao **nao revalida o candidato** (`RC-4`) | [ADR-0026 §5](../decisions/ADR-0026-admissao-do-medally-como-primeiro-produto.md) · [PS-2026-014](pacote-soberano-2026-07-31-medally.md) |
| **Produtos** | **`1` em vigor — o primeiro Produto do acervo.** [`PRO-nxtrack`](../products/nxtrack/carta.md), `status: ativo` · `ratificacao: ratificada`, em `products/nxtrack/carta.md`, criado pelo **item III do nono ato** e **executado** pela Missao 1.13.4.5. `products/` **nasce como raiz do acervo** e entra na lista fechada positiva do medidor no mesmo conjunto de mudanca *(`OA-1`)*. **`0` bytes do repositorio do candidato entraram**: `G0` = `IDENTIDADE`, e cada peca que um dia queira entrar tera **portao proprio** *(`LA-1`)*. **`1` candidato integro ainda NAO admitido**: `PRO-medally` *(1.13.4)*, cujo ato **nao foi emitido** | [PS-2026-016 §2](pacote-soberano-2026-08-01-nxtrack.md) · [PS-2026-014 §3](pacote-soberano-2026-07-31-medally.md) |
| **`Spec`s** | **`1` em vigor — a PRIMEIRA do acervo.** [`SPC-001`](../products/nxtrack/specs/SPC-001-governanca-de-dado-pessoal-do-nxtrack.md), `status: ativo` · `ratificacao: nao-exigida`, em `products/nxtrack/specs/`, criada por [`ADR-0031`](../decisions/ADR-0031-primeira-spec-governanca-de-dado-pessoal-do-nxtrack.md) em classe **`C2 · Tipo 2`**. **10** requisitos, **4 de 4** categorias de `SF-25`, **7 de 7** perfis de `SF-17`, **`DoR` 9/9** e **`DoD` 10/10**. Materia: **`LM-6(a)`**, fixada pelo nono ato *"com prioridade sobre as demais de `LA-7`"*. **`0` bytes no repositorio do candidato** | [ADR-0031](../decisions/ADR-0031-primeira-spec-governanca-de-dado-pessoal-do-nxtrack.md) · [FIT-2026-024](fitness/FIT-2026-024-primeira-spec.md) · [PT-2026-017](relatorio-transicao-2026-08-02-primeira-spec.md) |
| **Artefatos retidos por falta de ato — reaberto** | **2** no acervo *(`ADR-0026` e `ADR-0028`, ambos `em-revisao` · `pendente`)*. **A fila de retidos por falta de APLICACAO ZEROU:** `ADR-0030` e `RFC-0025` sairam dela pela Missao 1.13.4.5, que executou o `O4` de `PS-2026-016 §6.2` — **`0` retidos por falta de aplicacao**. **A distincao nao e formal, e foi ela que se moveu:** falta de ato depende do Soberano e **nao mudou**; falta de aplicacao dependia de missao, e a missao veio. *(Enunciado anterior desta linha, preservado: **4** no acervo — `ADR-0026`, `ADR-0028`, `ADR-0030` e `RFC-0025`)* — **`ADR-0027` e `ADR-0029` SAIRAM da fila pelo oitavo ato**; a contagem declarava **1** e estava **tres ADR atras** *(achado `RD-69`)* e **4** candidatos fora dele: a Carta **`PRO-medally`** *(1.13.4)* e as tres Cartas **`DEP-OPS`**, **`DEP-GRW`** e **`DEP-TLS` 1.2.0** *(1.13.4.1, achado `RD-49`)*. **A fila havia zerado em 2026-07-30 e reabre por construcao** | §4.2 · [PS-2026-014 §3](pacote-soberano-2026-07-31-medally.md) · [PT-2026-012 §3.1](relatorio-transicao-2026-07-31-manutencao-instrumentos.md) |
| **Instrumentos de medicao — estado** | **3 construidos e CALIBRADOS ANTES DO USO:** `baseline.sh` *(3 execucoes, hash identico)* · `hashes.sh` *(**8 de 8** controles publicados)* · `manifesto.sh` *(**4 de 4** classes de delta)*. **Vivem FORA do acervo**, deliberadamente: script dentro da raiz seria invisivel a medicao que ele executa | [PT-2026-012 §2.3, §5](relatorio-transicao-2026-07-31-manutencao-instrumentos.md) |
| **✅ `Q1` — RESPONDIDA em 2026-08-01, e nao se reabre** | **O Fundador decidiu: o `nXtrack`.** O fundamento e que **`PT-2026-009` e `PS-2026-013` sao artefatos DISTINTOS**: a decisao **7** de `PT-2026-009 §1` nomeia o nXtrack **em texto literal e sem ressalva**, e a oracao *"se seguir sendo o primeiro produto comercial"* mora em `PS-2026-013 §7`. A palavra `comercial` tem **`0`** ocorrencias no arquivo de `PT-2026-009` — **medido**. **Le-los como um so foi o que gerou `L1` × `L2`** *(`RD-64`)*. A ressalva **nao desapareceu**: virou **`Q2` de `PS-2026-016`** | [PT-2026-014 §2](relatorio-transicao-2026-08-01-portao-nxtrack.md) · [PS-2026-016 §8](pacote-soberano-2026-08-01-nxtrack.md) |
| **✅ `Q2` — RESPONDIDA, e agora GRAVADA COMO ARTEFATO** | **A ressalva de `PS-2026-013 §7` NAO condiciona o ato.** Respondida por despacho soberano de **2026-08-01** e **retida ate a reassinatura** do pacote, por determinacao do proprio despacho — de modo que `CA-6` se apoiava, ate aqui, **em despacho e nao em artefato**. Com o **nono ato**, a decisao entra no acervo em [MSG-2026-0009 §5](../memory/operacional/MSG-2026-0009-ato-soberano-admissao-do-nxtrack.md), e **`CA-6` fecha**. **`Q3` e `Q4` seguem NAO respondidas** — nenhuma das duas e condicao anterior de eficacia; o ato **dispoe da materia de `Q4`** ao admitir sem esperar e fixar `LM-6(a)` como materia da primeira `Spec`, **sem rotula-la respondida** | [MSG-2026-0009 §5](../memory/operacional/MSG-2026-0009-ato-soberano-admissao-do-nxtrack.md) · [PS-2026-016 §8](pacote-soberano-2026-08-01-nxtrack.md) |
| **Departamentos com Carta** | **9 de 9 — cobertura documental completa, e 9 de 9 em vigor.** A cobertura **vigente** alcanca a documental pelo ato de 2026-07-29 | §4.3.1 |
| **Artefatos em vigor por ato soberano** | **28 ENUMERADOS** *(o rotulo anterior dizia **26** sobre **25** enumerados — divergencia **medida** nesta emissao ao acrescentar os tres do nono ato, achado **`RD-84`**, **ABERTA**: nao se resolve aqui qual dos dois estava certo, porque decidir isso e missao de catalogo)* — **`ADR-0030`** *(`ativo` · `ratificada`)*, **`RFC-0025`** *(`aprovado`)* e **`PRO-nxtrack`** *(`ativo` · `ratificada`, **primeiro Produto**)* **(nono ato, 2026-08-01)** · **`ADR-0027`** e **`ADR-0029`** *(oitavo ato, 2026-07-31)* · `DEP-QAR` *(**1.2.0**)* · `DEP-ENG` *(**1.1.0**)* · `MEM-EST-0001` · `DEP-GOV` · `ADR-0014` · `ADR-0016` · `ADR-0017` · `ADR-0018` · `ADR-0019` · **`DEP-EXE`**, **`DEP-PRD`**, **`DEP-OPS`**, **`DEP-GRW`** e **`DEP-TLS`** *(todas **1.1.0**)* · **`ADR-0022`** · **`ADR-0023`** · **`ADR-0024`** · **`ADR-0025`** · **`FND-11`** *(1.0.0)* · **`FND-01`** *(1.7.0)* · **`FND-02`** *(1.4.0)* · **`FND-03`** *(1.6.0)* · **`FND-10`** *(1.5.0)* | MSG-2026-[0001](../memory/operacional/MSG-2026-0001-ato-soberano-ratificacao-cartas-piloto.md), [0002](../memory/operacional/MSG-2026-0002-ato-soberano-cartas-comando-plataforma-e-contexto.md), [0003](../memory/operacional/MSG-2026-0003-ato-soberano-emenda-qar-e-criterio-de-consolidacao.md) , [**0004**](../memory/operacional/MSG-2026-0004-ato-soberano-cartas-emenda-constitucional-e-regime-do-fitness-check.md), [0005](../memory/operacional/MSG-2026-0005-ato-soberano-aplicacao-dep-qar.md), [0006](../memory/operacional/MSG-2026-0006-ato-soberano-aplicacao-integral.md) e [**0007**](../memory/operacional/MSG-2026-0007-ato-soberano-vigencia-do-framework-de-specifications.md), [**0008**](../memory/operacional/MSG-2026-0008-ato-soberano-emendas-e1-e-e3.md) |
| **Artefatos retidos pelo ato anterior** | **`0`** — os **4** `ADR` e os **10** candidatos submetidos entraram em vigor pelo ato de **2026-07-30**. **Permanecem fora do acervo, como evidencia historica e sem vigencia, 3 variantes NAO promulgadas** de `FND-01`: `ALT` 1.6.0 *(490)*, `V1` *(488)* e `V2` *(492)* — **nao ha fallback automatico para nenhuma** | §10.9 · [MSG-2026-0007 §VI.4](../memory/operacional/MSG-2026-0007-ato-soberano-vigencia-do-framework-de-specifications.md) |
| **Estado do portao `GO-TO-SPECS`** | **✅ EXERCIDO desde 2026-08-02 — `SPC-001` existe.** *(Enunciado anterior, preservado: LIBERADO e EXERCIVEL desde 2026-08-01)* — **8 de 8** condicoes de §X. **Deixa de estar *"liberado e nao exercivel"***, estado em que viveu de 2026-07-29 a 2026-08-01: o `DoR` de `SF-23` foi **reexercido** e o item **(9)** — *"Produto existe"* — **passa**, com o item (4) em **5 de 5** `Capabilities` ativas. **A primeira `Spec` FOI CRIADA pela Missao 1.13.5**, pelo rito `RFC-0026` → `ADR-0031` → [`SPC-001`](../products/nxtrack/specs/SPC-001-governanca-de-dado-pessoal-do-nxtrack.md) → `FIT-2026-024`, em classe `C2 · Tipo 2`. **O portao seguinte, `GO-TO-SKILLS`, NAO e liberado aqui** — sua liberacao nunca foi condicionada a este catalogo, e a divergencia registrada no roadmap sobre onde Skills entra **continua sendo decisao do Fundador** | [PT-2026-016 §3](relatorio-transicao-2026-08-01-fechamento-rd-33.md) · [PT-2026-006 §8](relatorio-transicao-2026-07-29-fechamento-operacional.md) · [FIT-2026-014](fitness/FIT-2026-014-regime-ministerial-e-cobertura-de-contexto.md) |
| **Pre-correcao obrigatoria antes da 1a Spec** | ✅ **FECHADA** — `TPL-spec` **1.1.0**, **5** defeitos corrigidos onde `RD-23` declarava **2** | Achado **RD-23**, **RESOLVIDO** — [ADR-0021 §5.11](../decisions/ADR-0021-framework-de-specifications.md) · [PT-2026-007 §3](relatorio-transicao-2026-07-29-specifications.md) |
| **Framework de Specifications** | **EM VIGOR, COM SEDE FUNDACIONAL** — **`SF-01` a `SF-32`** vivem em **`FND-11`**, nivel 2 da hierarquia normativa. `ADR-0021` permanece **vigente e intacto**, superado **somente quanto a sede** | [ADR-0021](../decisions/ADR-0021-framework-de-specifications.md) · [FIT-2026-015](fitness/FIT-2026-015-framework-de-specifications.md) |
| **Sede canonica do Framework** | ✅ **EM VIGOR** — `FND-11` **1.0.0** *(399 linhas)*, `C3 · Tipo 1`, **promulgada e ratificada** em 2026-07-30, com **30 de 32** regras migradas **byte a byte** e **1 alteracao de merito declarada** *(`SF-32`, `M1` → `M2`)*. **`foundation/` passa a ter 11 documentos** | [ADR-0022](../decisions/ADR-0022-sede-canonica-do-framework-de-specifications.md) · [PS-2026-009](pacote-soberano-2026-07-29-fnd-11.md) |
| **`RD-31` e `RD-37` — o portao da `Spec` nas Cartas** | ✅ **FECHADOS NO ACERVO EM VIGOR** — as **5** Cartas 1.1.0 entraram em vigor, e a familia das **nove** foi de **11 afirmacoes falsas em 4 Cartas** para **`0` em `0`**, com **5 de 9** nomeando `DEP-EXE` e **5 de 5** caminhos coerentes. **Medido no acervo, nao em candidato** | [ADR-0023](../decisions/ADR-0023-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md) · [PS-2026-010](pacote-soberano-2026-07-29-rd-31.md) |
| **Pilotos de `Spec`** | **`PILOTO-DEFERIDO` quanto ao piloto INTERDEPARTAMENTAL, e CUMPRIDO quanto ao de produto.** `SPC-001` e a `Spec` **de produto**, e com ela o piloto de produto deixa de ser hipotese. *(Enunciado anterior, preservado: `PILOTO-DEFERIDO`, e MANTIDO apos o fechamento de `RD-33`)* — registro formal em [PT-2026-008 §4](relatorio-transicao-2026-07-29-canonizacao.md). **Nao e cumprido, nao e dispensado e nao e omissao**; a primeira `Spec` real **aciona revisao empirica** de `FND-11`. **O piloto de produto passa a ser possivel** *(`S1` consumida)*; **o interdepartamental nao** — depende de `S2`, **deferida**, achado **`RD-88`** | `RD-88` · [PT-2026-016 §4.2](relatorio-transicao-2026-08-01-fechamento-rd-33.md) · [FIT-2026-016](fitness/FIT-2026-016-canonizacao-e-propagacao.md) |
| **✅ Pendencias BLOQUEANTES do acervo** | **`0` — pela primeira vez desde 2026-07-29.** **`RD-33` esta FECHADO em 2026-08-01**, pela Missao **1.13.4.6**, por rito **MINISTERIAL**. A causa foi removida por `S1` — nono ato, item **III**, ja consumido —, e a **reserva do item VII e `LA-3` era TEMPORAL** *("apos a vigencia")* **e DE SEDE** *("missao propria")*, **nunca de classe de rito**: as palavras *ato*, *ratificacao*, *`C3`* e *`1.13.5`* tem **`0`** ocorrencias nela, e [`MSG-2026-0009 §8`](../memory/operacional/MSG-2026-0009-ato-soberano-admissao-do-nxtrack.md) poe *"`RD-33` destravado"* **ANTES** de 1.13.5. **`0` atos emitidos, `0` fontes emendadas.** **O residuo NAO fechou junto:** a parte **(b)** — a categoria de `Spec` sobre materia **nao-produto**, que so `S2` cria e que segue **DEFERIDA** — **migrou para `RD-88`**, aberto, com dono e gatilho proprios | Achados **RD-33** *(fechado)* e **RD-88** *(aberto)*, §7 · [PT-2026-016](relatorio-transicao-2026-08-01-fechamento-rd-33.md) · [ADR-0021 §7.3](../decisions/ADR-0021-framework-de-specifications.md) |

### 2.1 Custo por perfil de contexto — **reconciliada, com metodo declarado**

> **Declaracao de metodo (`CE-04`, `BL-03`).** Esta tabela era o **unico item de §X.7 nao
> reconciliado** — achado **`RD-26`**. Ela passa a derivar de **duas regras**, ambas escritas em
> [FND-10 §2.3](../foundation/10-artifact-framework.md), e de nenhuma invencao:
>
> 1. **Perfil = `perfil_contexto` do frontmatter**, quando declarado — **109** artefatos.
> 2. **Perfil = padrao por tipo documental de [FND-10 §10.3](../foundation/10-artifact-framework.md)**,
>    quando ausente — **60** artefatos. E o que §2.3 manda: *"padrao por tipo (§10.3),
>    **aplicado por referencia no catalogo**"*.
>
> **Custo = linhas do arquivo, medido por `wc -l`** (`CE-02`), em **2026-07-29**.
> **Coorte = os 169 artefatos da lista fechada de `RD-17`** — a mesma da baseline.
> **A particao foi RECOMPUTADA por ferramenta sobre a coorte inteira**, nao obtida por soma dos
> **5** artefatos novos aos valores anteriores — e essa e a razao pela qual **`TPL-spec` migrou de
> *por padrao* para *declarado***: a versao **1.1.0** passou a declarar `perfil_contexto`, e as
> ausencias caem de **61** para **60**.

| Perfil | Declarado | Por padrao §10.3 | **Artefatos** | **Linhas** | **% do acervo** |
|---|---|---|---|---|---|
| `nucleo` | 3 | 1 | **4** | **3.157** | **6,47%** |
| `missao` | 61 | 8 | **69** | **25.484** | **52,26%** |
| `sob-demanda` | 45 | 51 | **96** | **20.123** | **41,27%** |
| `arquivo` | 0 | 0 | **0** | **0** | **0%** |
| **Total** | **109** | **60** | **169** | **48.764** | **100,00%** |

> **A prova de que o metodo fecha, e e ela que responde a `RD-26`.** O total reproduz
> **169 artefatos** e **48.764 linhas** — **exatamente** o denominador e a contagem de
> `BL-2026-07-29-09`, pelo comando publicado em §10.6. **Uma particao que reproduz o total do
> acervo nao pode ter dupla contagem nem omissao.** **Segunda emissao consecutiva em que a
> particao fecha**, e a primeira em que ela foi **recomputada em vez de incrementada** — o que
> capturou a migracao de `TPL-spec` que a soma teria perdido.
>
> **O que ela declarava antes:** `nucleo` *2 + 2 recortes*, `missao` **24 / 8.718** e
> `sob-demanda` **79 / 14.682** — **105 artefatos**, **65,9%** do acervo, **sem dizer que era
> parcial** e **sem metodo declarado**. Os itens que continha **nao estavam errados**; a tabela
> estava **incompleta**. Item 3 do achado **`RD-28`**.
>
> **`CE-01` e `CE-02` permanecem afirmaveis**, com cobertura de **100%**: nenhum papel carrega o
> acervo por padrao, e o nucleo obrigatorio custa **6,47%** do total — **medido, nao
> estimado**. **Dois dos 4 artefatos de `nucleo` entram por recorte** (`FND-09` e `FND-10`),
> e por isso o custo **efetivo** e menor que o declarado; o valor acima e o **teto**. **O nucleo
> nao cresceu nesta missao: `3.157` linhas, identicas** — `ADR-0021` e `sob-demanda`, e ampliar o
> nucleo seria **C2** com `FIT` obrigatorio (`FND-10 §8.2`). Missao tipica: §11.
>
> **`perfil_contexto` ausente nao e defeito para a coorte anterior a vigencia de FND-10** — e
> exatamente o que a **migracao de custo zero** de §2.3 prescreve. As **duas** nao conformidades
> reais estao em **`RD-27`**, §7, e sao `FND-01` e `FND-02`.
>
> **Relacao com as coortes anteriores, para que os numeros nao pareçam divergir.**
> [PT-2026-006 §3](relatorio-transicao-2026-07-29-fechamento-operacional.md) auditou
> **`BL-2026-07-29-07` — 159 artefatos**, com **98 declarando** e **61 ausentes**. A emissao
> anterior desta tabela projetou **`BL-2026-07-29-08` — 164**, com **103** e **61**. Esta projeta
> **`BL-2026-07-29-09` — 169**, com **109** e **60**: os **5** artefatos criados na Missao 1.13
> declaram os cinco campos *(103 → 108)*, e **`TPL-spec` 1.1.0 passou a declarar** *(108 → 109;
> ausencias 61 → 60)*. **Tres coortes, tres datas, nenhuma contradicao** — e as tres estao
> declaradas.

### 2.2 Os cinco maiores artefatos — **remedidos**

| # | Artefato | Linhas | Perfil | Observacao |
|---|---|---|---|---|
| 1 | `foundation/09-meta-model.md` | **1.263** | `nucleo` *(por recorte)* | Maior do acervo; entra por §5, §6.2 e §8.2, nunca integral (CE-05) |
| 2 | `governance/artifact-registry.md` | **989** | `sob-demanda` | **Este catalogo.** Segundo do acervo — e **nao constava desta lista** |
| 3 | `foundation/10-artifact-framework.md` | **778** | `nucleo` *(por recorte)* | Entra por §2 e §4 |
| 4 | `foundation/revisao-arquitetural-validacao-interclasses-2026-07-28.md` | **746** | `missao` | **Nao constava desta lista** |
| 5 | `foundation/03-taxonomia.md` | **631** | `nucleo` | Integral |

> ⚠️ **Esta lista estava errada, e o erro nao era de projecao contra fonte — era da fonte
> derivada contra si mesma.** Ate 2026-07-29 ela declarava `FND-08` **522** e `FND-06` **533**
> nas posicoes 4 e 5, quando **quatro** artefatos maiores existiam: este catalogo *(**989**)*,
> `REV-interclasses` *(**746**)* e `REV-ESTRUTURAL-I` *(**609**)*. **Os valores individuais
> estavam corretos; a ordenacao nao.** E declarava ainda que o maior artefato novo tinha **496**
> linhas e era o **sexto** do acervo, quando tem **516** e e o **decimo**. Itens 4 e 5 do achado
> **`RD-28`**, encontrados ao **ordenar a propria coluna** — a mitigacao de **`RG-2`** da
> [Carta de DEP-GOV](../departments/gov/carta.md), escrita desde a Missao 1.9 e **exercida pela
> primeira vez** aqui.
>
> **`CE-05` reverificado nas nove Cartas, com valores medidos:** **388 · 402 · 424 · 429 ·
> 437 · 443 · 457 · 464 · 481**. A **mediana e 437** e o dobro dela e **874**: **nenhuma das
> nove dispara CE-05**, e com **nove** instancias a mediana deixou de ser fraca. *(A verificacao
> original, feita com duas instancias e mediana 393, fica preservada no historico e **nao foi
> reescrita** — MEM-APR-0004.)*
>
> **`CE-05` sobre os dois maiores.** `FND-09` **1.263** e este catalogo **989** ultrapassam o
> dobro da mediana do proprio tipo e **permanecem sinais registrados**, nao acoes: `FND-09` entra
> no nucleo **por recorte** e o catalogo e **`M3` derivado**, cujo custo cresce por definicao com
> o acervo. Registrado como sinal (CE-05, SE-06).

## 3. Nucleo obrigatorio

O que um papel precisa para **nao violar norma** — nao o que seria util saber.

| Artefato | Recorte | Custo | Por que |
|---|---|---|---|
| FND-01 Constituicao | integral | **485** | Principios imutaveis e linhas vermelhas |
| FND-03 Taxonomia | integral | 631 | Nomear e localizar qualquer coisa |
| FND-09 Meta Model | §5, §6.2, §8.2 | parcial | O tipo existe? que relacao vale? quem aprova? |
| FND-10 Artifact Framework | §2, §4 | parcial | Que contrato o artefato cumpre, e de que tipo e |

**Total integral: 1.116 linhas.** Ampliar o nucleo e mudanca **C2** com Fitness
Check (CE-01).

> **`FND-01` declarava 468 linhas e o total 1.099 — valores anteriores a promulgacao de
> `FND-01` 1.5.0**, que a levou a **485**. Itens 6 e 7 do achado **`RD-28`**, corrigidos na
> projecao. **A tabela homonima de [FND-10 §8.5](../foundation/10-artifact-framework.md), que
> declara 468 · 619 · 1.087, NAO foi corrigida:** ela vive em **fonte promulgada**, e edita-la
> alteraria `H-N` — item **(c)** de **`RD-27`**, aberto.

> **O nucleo nao foi ampliado nesta missao.** Nenhum artefato entrou nem saiu: os dois
> integrais e os dois recortes sao os mesmos. O total sobe apenas porque **FND-03 e FND-10
> foram emendados** — crescimento de conteudo dentro do nucleo ja existente, nao ampliacao
> de escopo. O contrato sobre o Soberano **nao** entra no nucleo: e `sob-demanda`, carregado
> por pacote (CT-21).

## 4. Classificacao — **todos os medidos, menos `roadmap-canonico` (`RD-80`)**

Legenda de perfil: **N** nucleo · **M** missao · **S** sob-demanda · **A** arquivo.
Proveniencia de **todo** artefato listado: `native` (§9). **Linhas remedidas por ferramenta em 2026-07-29**, na reconciliacao exigida por §X.7 do ato — achado **RD-25**.

> **O cabecalho desta secao estava defasado, e o defeito e de agregado escrito como literal.**
> Ele declarava **`159 de 159`** enquanto a soma das proprias subsecoes dava **169** —
> `10 + 40 + 32 + 19 + 24 + 11 + 33`. Achado **`RD-42`**, familia de **`RD-35`**, **segunda
> ocorrencia**; a causa e a mesma: **agregado escrito como valor, nao derivado da tabela**
> (`RG-03`). **Corrigido nesta emissao, e a conferencia de §4 agora recalcula o cabecalho a
> partir dos blocos, em vez de conferi-lo contra §2.**

### 4.1 Normativa — 11 artefatos, entidade `FND`

| Artefato | Tipo documental | Perfil | Linhas | Resumo operacional |
|---|---|---|---|---|
| [01-constituicao](../foundation/01-constituicao.md) **1.7.0** | Constituicao | **N** | **493** | Fixa missao, valores, 14 principios imutaveis, 12 linhas vermelhas, 7 portoes e a hierarquia normativa |
| [02-estrutura-organizacional](../foundation/02-estrutura-organizacional.md) **1.4.0** | Doc. Fundacional | M | **524** | Define 9 departamentos em 4 classes, matriz de interacao e a escada de especializacao |
| [03-taxonomia](../foundation/03-taxonomia.md) **1.6.0** | Doc. Fundacional | **N** | **633** | Fixa nomes, identificadores, frontmatter, estados, versionamento e localizacao de tudo |
| [04-governanca](../foundation/04-governanca.md) | Doc. Fundacional | M | 445 | Define 4 classes de mudanca, 8 papeis, ciclo de 13 etapas, excecoes e incidentes |
| [05-framework-comunicacao](../foundation/05-framework-comunicacao.md) | Framework | S | 345 | Define 5 canais, envelope de mensagem, contrato de handoff e escalonamento |
| [06-arquitetura-memoria](../foundation/06-arquitetura-memoria.md) | Framework | S | 533 | Define as 5 camadas de memoria, alocacao, promocao, expiracao e curadoria |
| [07-framework-decisoes](../foundation/07-framework-decisoes.md) | Framework | S | 440 | Define classificacao, instrumentos e as 13 secoes obrigatorias do registro de decisao |
| [08-capability-framework](../foundation/08-capability-framework.md) | Framework | M | 522 | Define Capability, 13 atributos, 3 eixos, ciclo, relacoes e vinculacao obrigatoria |
| [09-meta-model](../foundation/09-meta-model.md) **1.5.0** | Meta Model | **N** *(recorte)* | **1.263** | Declara o universo fechado de 21 entidades, relacoes, estados, autoridade e evolucao |
| [10-artifact-framework](../foundation/10-artifact-framework.md) **1.5.0** | Framework | **N** *(recorte)* | **785** | Define o contrato universal de artefato, tipos, ciclo, linhagem e economia de contexto |
| [11-framework-specifications](../foundation/11-framework-specifications.md) **1.0.0** | Framework | S | **399** | **Sede canonica da norma da `Spec`** — contrato, semantica, perfis, autoridade derivada, `DoR`, `DoD`, ciclo, relacoes, mudanca e economia de contexto, em `SF-01` a `SF-32`. **Em vigor por ato soberano de 2026-07-30** |

### 4.2 Decisoria — **61** artefatos

| Artefato | Tipo | Entidade | Perfil | Linhas | Resumo operacional |
|---|---|---|---|---|---|
| [ADR-0001](../decisions/ADR-0001-adocao-da-fundacao-organizacional.md) | ADR | `ADR` | S | 271 | Adota a Fundacao como fonte oficial de verdade. **Ratificada** (INC-2026-001 §11) |
| [ADR-0002](../decisions/ADR-0002-adocao-da-camada-de-capabilities.md) | ADR | `ADR` | S | 280 | Adota a camada de Capabilities e a vinculacao obrigatoria. **Ratificada** |
| [ADR-0003](../decisions/ADR-0003-adocao-do-enterprise-meta-model.md) | ADR | `ADR` | S | 372 | Adota o Meta Model com universo fechado de 21 entidades. **Ratificada** |
| [ADR-0004](../decisions/ADR-0004-adocao-do-architecture-fitness-check.md) | ADR | `ADR` | S | 351 | Cria o Fitness Check, a entidade `FIT` e o portao QG-6. **Ratificada** |
| [ADR-0005](../decisions/ADR-0005-proibicao-de-autoverificacao.md) | ADR | `ADR` | S | 260 | Proibe par reflexivo de `verifica` e corrige a autoverificacao de `CAP-governanca` |
| [ADR-0006](../decisions/ADR-0006-adocao-do-enterprise-artifact-framework.md) | ADR | `ADR` | S | 409 | Adota o Artifact Framework. **Ratificada** — FND-10 em vigor |
| [ADR-0007](../decisions/ADR-0007-fronteira-greenfield-legado.md) | ADR | `ADR` | **M** | 354 | Declara a fronteira greenfield/legado e o portao de admissao de origem externa |
| [ADR-0008](../decisions/ADR-0008-uma-fonte-multiplas-projecoes.md) | ADR | `ADR` | **M** | 316 | Institui "uma fonte, multiplas projecoes" e o teste preventivo antes da submissao |
| [ADR-0009](../decisions/ADR-0009-o-que-conta-como-emenda-de-artefato.md) | ADR | `ADR` | **M** | 301 | Fixa que "emendado" e a alteracao que incrementa MAIOR ou MENOR. Fecha o achado C13 |
| [ADR-0010](../decisions/ADR-0010-contrato-de-conhecimento-do-soberano.md) | ADR | `ADR` | **M** | 469 | Institui o Contrato de Conhecimento sobre o Soberano — 28 regras, sem autoridade normativa |
| [ADR-0011](../decisions/ADR-0011-contrato-de-carta-de-departamento.md) | ADR | `ADR` | **M** | 362 | Institui o Contrato de Carta de Departamento — 12 blocos, 10 regras `DC`, 2 pilotos autorizados |
| [**ADR-0012**](../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md) | ADR | `ADR` | **M** | **260** | Fixa que o ato de ratificacao vincula o **conteudo normativo** (`H-N`); 12 regras `IR`, tres hashes e teste de reconstrucao |
| [**ADR-0013**](../decisions/ADR-0013-criterio-de-horizonte-e-consolidacao.md) | ADR | `ADR` | **M** | **293** | Fixa o criterio de **horizonte avaliavel** e de revisao de consolidacao determinado pelo Soberano; 8 regras `HZ`, **zero** fundacionais emendadas |
| [**ADR-0014**](../decisions/ADR-0014-candidato-emenda-fnd-01-7-3-homologa.md) | ADR | `ADR` | S | **261** | **EM VIGOR** — `ativo` · `ratificacao: ratificada` pelo ato de **2026-07-29** ([MSG-2026-0004](../memory/operacional/MSG-2026-0004-ato-soberano-cartas-emenda-constitucional-e-regime-do-fitness-check.md)). Emenda **C3** a FND-01 §7.3 e §11: separa **ratificacao** de **homologacao**. **O slug do arquivo conserva a palavra `candidato`, que descreve a origem e nao o estado** — achado `RD-51` |
| [RFC-0001](../rfcs/RFC-0001-camada-de-capabilities.md) | RFC | `RFC` | S | 174 | Propos a camada de Capabilities. Aceita → ADR-0002 |
| [RFC-0002](../rfcs/RFC-0002-enterprise-meta-model.md) | RFC | `RFC` | S | 221 | Propos o Meta Model com universo fechado. Aceita → ADR-0003 |
| [RFC-0003](../rfcs/RFC-0003-architecture-fitness-check.md) | RFC | `RFC` | S | 190 | Propos o Fitness Check como verificacao de aptidao. Aceita → ADR-0004 |
| [RFC-0004](../rfcs/RFC-0004-enterprise-artifact-framework.md) | RFC | `RFC` | S | 200 | Propos o contrato universal de artefato. Aceita → ADR-0006 |
| [RFC-0005](../rfcs/RFC-0005-fronteira-greenfield-legado.md) | RFC | `RFC` | S | 194 | Propos a fronteira greenfield/legado. Aceita → ADR-0007 |
| [RFC-0006](../rfcs/RFC-0006-contrato-de-artefato-o-que-e-emenda.md) | RFC | `RFC` | S | 218 | Propos o criterio de "emendado" no contrato de artefato. Aceita → ADR-0009 |
| [RFC-0007](../rfcs/RFC-0007-conhecimento-sobre-o-soberano.md) | RFC | `RFC` | S | 262 | Propos onde registrar conhecimento sobre o Soberano; aplica o Teste de Entidade. Aceita → ADR-0010 |
| [RFC-0008](../rfcs/RFC-0008-contrato-de-carta-de-departamento.md) | RFC | `RFC` | S | 200 | Propos onde vive o contrato de Carta de Departamento. Aceita com ajuste → ADR-0011 |
| [**RFC-0009**](../rfcs/RFC-0009-integridade-e-alcance-do-ato-de-ratificacao.md) | RFC | `RFC` | S | **222** | Propos o que o ato de ratificacao vincula. **Aceita em parte** → ADR-0012; **Q1 e Q2 seguem abertas** e escaladas ao Soberano |
| [**RFC-0010**](../rfcs/RFC-0010-criterio-de-horizonte-avaliavel.md) | RFC | `RFC` | S | **207** | Propos o **instrumento** de formalizacao do criterio de horizonte. **Aceita** → ADR-0013 |
| [**RFC-0011**](../rfcs/RFC-0011-emenda-constitucional-ratifica-homologa.md) | RFC | `RFC` | S | **251** | Leva **Q1 e Q2** de pergunta a **texto**: 8 alteracoes em FND-01 e 3 em FND-10/FND-09. **Aberta — escalada ao SOBERANO** |
| [INC-2026-001](incidents/INC-2026-001-ratificacao-inferida.md) | Incidente | `INC` | M | 353 | Registra, contem e encerra a ratificacao inferida; **§11 e a fonte canonica do ato soberano**. `fechado` |
| [INC-2026-002](incidents/INC-2026-002-ratificacao-declarada-em-fitness-check.md) | Incidente | `INC` | M | **237** | Contem o estado incorreto de ratificacao em FIT-2026-001 e FIT-2026-002. **`fechado`** pelo ato de 2026-07-28; causa propria **migrada para RFC-0009 Q2, aberta** |

| [**ADR-0015**](../decisions/ADR-0015-fitness-check-e-parecer-nao-decisao.md) | ADR | `ADR` | S | 249 | `Fitness Check` e `Revisao Arquitetural` sao **pareceres M1** e **nao se ratificam** — `FT-10` a `FT-15`. **Responde Q2** |
| [**ADR-0016**](../decisions/ADR-0016-semantica-da-matriz-de-interacao.md) | ADR | `ADR` | S | **243** | **RATIFICADO** — semantica de FND-02 §4, codigo `R`, celula multivalorada, `MI-01` a `MI-06` e **12 celulas**. **`ativo`** · **ratificada**; promulgou **FND-02 1.3.0** |
| [**ADR-0017**](../decisions/ADR-0017-harmonizacao-do-regime-do-parecer.md) | ADR | `ADR` | S | **228** | **RATIFICADO** — linha `Fitness Check` de FND-09 §8.2 e FND-10 §10.3 passa a `—`. **`ativo`** · **ratificada**; entrou no **cumulativo** FND-09 1.5.0 / FND-10 1.4.0 |
| [**RFC-0012**](../rfcs/RFC-0012-semantica-da-matriz-de-interacao.md) | RFC | `RFC` | S | **258** | Determina a semantica de FND-02 §4 e testa as **81 celulas**; propoe a emenda que fecha **RD-02** |
| [**RFC-0013**](../rfcs/RFC-0013-harmonizacao-do-regime-do-parecer.md) | RFC | `RFC` | S | **178** | Propoe alinhar FND-09 §8.2 e FND-10 §10.3 a `FT-10`; fecha **RD-09**. Abre **RD-12** |
| [**ADR-0018**](../decisions/ADR-0018-liberacao-do-portao-qg-1.md) | ADR | `ADR` | S | **243** | **RATIFICADO** — o portao `QG-1` passa a ser liberado por **`DEP-EXE`**, com nota que distingue **liberar portao** de **aprovar artefato**. **`ativo`** · **ratificada**; promulgou **FND-01 1.5.0** |
| [**ADR-0019**](../decisions/ADR-0019-aprovador-e-ratificador-de-spec.md) | ADR | `ADR` | S | **251** | **RATIFICADO** — linhas `SPC` e `Spec` passam a **remeter a classe**, e o conflito e **registrado como erro da propria tabela**. **`ativo`** · **ratificada**; entrou no **cumulativo** FND-09 1.5.0 / FND-10 1.4.0 |
| [**RFC-0014**](../rfcs/RFC-0014-liberacao-do-portao-qg-1.md) | RFC | `RFC` | S | **226** | Reconstroi o fluxo de `QG-1` em **dez elementos** e determina que a colisao e **interna a FND-01 §6.2**; fecha **RD-14** |
| [**RFC-0015**](../rfcs/RFC-0015-aprovador-e-ratificador-de-spec.md) | RFC | `RFC` | S | **241** | Mapeia **C0–C3 × Tipo 1/2** para onze atos; fecha **RD-15**. Abre **RD-18** e **RD-19** |
| [**ADR-0020**](../decisions/ADR-0020-regime-ministerial-de-promulgacao-e-ativacao.md) | ADR | `ADR` | S | **379** | **`C2 · Tipo 2`** — promulgar e ativar sao **operacoes ministeriais**; institui `PA-01` a `PA-14` e a **matriz de regime operacional**. **Fecha `RD-22`**; **0 fontes emendadas · 0 titulares criados** |
| [**RFC-0016**](../rfcs/RFC-0016-regime-ministerial-de-promulgacao-e-ativacao.md) | RFC | `RFC` | S | **277** | Inventaria **20 declaracoes em 5 fontes vigentes** que nomeiam executor, verificador e registrador; demonstra que `AU-09` **nao alcanca** promulgar e ativar. **Acolhida** → ADR-0020 |
| [**ADR-0021**](../decisions/ADR-0021-framework-de-specifications.md) | ADR | `ADR` | S | **573** | **`C2 · Tipo 2`** — institui o **Framework de Specifications** em **`SF-01` a `SF-32`**: contrato de 21 blocos, semantica normativa, 7 perfis, matriz de 50 celulas, cadeia de 9 elos, `DoR`/`DoD`, mudanca e economia de contexto. **Fecha `RD-23`** com `TPL-spec` 1.1.0. **0 fontes emendadas · 0 titulares criados.** Declara que **nenhuma Spec e criavel** — `RD-33` |
| [**ADR-0022**](../decisions/ADR-0022-sede-canonica-do-framework-de-specifications.md) | ADR | `ADR` | S | **438** | **`C3 · Tipo 1` — EM VIGOR**, `ativo` · `ratificacao: ratificada` pelo ato de **2026-07-30**. Cria **`FND-11`** como sede fundacional de `SF-01` a `SF-32` e emenda `FND-01` e `FND-03`. **30 de 32 regras migram byte a byte**; **1** alteracao de merito declarada *(`SF-32`)*; **0 de 32 identificadores renumerados**. `supera: [ADR-0021]` — **so a sede** |
| [**ADR-0023**](../decisions/ADR-0023-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md) | ADR | `ADR` | S | **353** | **`C2 · Tipo 2`** — propaga `ADR-0018` e `ADR-0019` as Cartas de `DEP-PRD` e `DEP-EXE`: **8 afirmacoes falsas corrigidas**, `QG-1` **declarado em Carta pela primeira vez**. **0 titulares, portoes, papeis, classes ou direitos decisorios criados.** Aprovado por **DEP-GOV** *(DEP-EXE e o autor)* |
| [**ADR-0024**](../decisions/ADR-0024-conformidade-de-contrato-das-fundacionais.md) | ADR | `ADR` | S | **341** | Emenda **C3 · Tipo 2** que **fecha `RD-27` integralmente** — backfill de `AC-08` em `FND-01` *(4 campos)* e `FND-02` *(5)*, e correcao de `FND-10 §8.5` *(6 valores + regra de leitura)*, com **`0` bytes de corpo nos tres**. **`em-revisao`** · **pendente**. Abre e fecha **`RD-45`** e **`RD-46`** |
| [**ADR-0025**](../decisions/ADR-0025-extensao-da-propagacao-de-qg-1-as-cartas-restantes.md) | ADR | `ADR` | S | **292** | Emenda **C2 · Tipo 2** que **fecha `RD-37`** nas Cartas de `DEP-OPS`, `DEP-GRW` e `DEP-TLS`. **Primeira dispensa de RFC do acervo** (`FND-04 §2`), com as duas condicoes verificadas. **`em-revisao`** · nao exigida. Abre **`RD-47`** |
| [**RFC-0018**](../rfcs/RFC-0018-sede-canonica-do-framework-de-specifications.md) | RFC | `RFC` | S | **262** | Propoe a **sede canonica** de `SF-01` a `SF-32` entre **quatro opcoes e a opcao Z**; submete **em separado** a unica alteracao de merito; abre `RD-38` e `RD-39`. **Acolhida** → ADR-0022 |
| [**RFC-0019**](../rfcs/RFC-0019-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md) | RFC | `RFC` | S | **268** | Propoe a **forma** da propagacao nas Cartas; **enumera as 8 afirmacoes falsas** e **mede as nove Cartas**, encontrando **3 a mais em 3 Cartas nunca enumeradas** — `RD-37`. **Primeira `RFC` do acervo cujo autor e DEP-EXE.** **Acolhida** → ADR-0023 |
| [**RFC-0020**](../rfcs/RFC-0020-conformidade-de-contrato-das-fundacionais.md) | RFC | `RFC` | S | **227** | **Como fechar `RD-27` sem reescrever norma.** Declara **5 criterios antes das opcoes** e **5 opcoes**, `Z` inclusive; mede que **`FND-10 §8.5` tem 5 valores defasados onde `RD-27` contara 3** — **`RD-46`** |
| [**ADR-0026**](../decisions/ADR-0026-admissao-do-medally-como-primeiro-produto.md) | ADR | `ADR` | S | **315** | **`C2 · Tipo 1` — NAO ESTA EM VIGOR**, `em-revisao` · `ratificacao: pendente`. **Primeiro exercicio do portao de `ADR-0007`**: `G1`–`G4` comprovados, `G5` preparado, **`G3` = `REWRITE`** com **`0`** bytes admitidos. Cria `PRO-medally` **somente por ato**. **7** regras `AM` do que **nao** faz; abre **`RD-54`** e **`RD-55`** |
| [**ADR-0027**](../decisions/ADR-0027-classe-de-admissao-de-existencia-no-portao-de-origem-externa.md) | ADR | `ADR` | S | **311** | **`C2 · Tipo 2` — EM VIGOR desde 2026-07-31**, `ativo` · `ratificacao: nao-exigida`, **aprovado por DEP-EXE** no oitavo ato. Acrescenta **`G0`** e **`RECOGNIZE`** ao portao, superando **`ADR-0007 §5.3` linha `G3` e `§5.4`** quanto a lista — **`0` bytes** em `ADR-0007`. `RC-1` a `RC-5` reclassificam o `REWRITE` da 1.13.4 **na vigencia** |
| [**ADR-0028**](../decisions/ADR-0028-independencia-de-verificacao-por-fornecedor.md) | ADR | `ADR` | S | **291** | **`C3 · Tipo 1` — NAO ESTA EM VIGOR**, `em-revisao` · `ratificacao: pendente`. `AV-1` a `AV-6`: independencia por **fornecedor**. Supera **`AC-03` de `FND-10 §2.5` quanto a suficiencia** — **nao `ADR-0005`**. Diferenca medida: **`0` contra `131`**, base **138** |
| [**ADR-0029**](../decisions/ADR-0029-superacao-de-ato-por-evidencia-posterior.md) | ADR | `ADR` | S | **260** | **`C3 · Tipo 1` — EM VIGOR desde 2026-07-31**, `ativo` · **`ratificada`** pelo oitavo ato. `SA-1` a `SA-6`: superacao de ato por evidencia posterior. **Nenhuma norma revogada** — lacuna de omissao. `ADR-0012` vira **pre-condicao**, `0` bytes |
| [**RFC-0022**](../rfcs/RFC-0022-classe-de-admissao-de-existencia-no-portao-de-origem-externa.md) | RFC | `RFC` | S | **174** | Submete `G0` e `RECOGNIZE`. **Tres alternativas reais mais `Z`**. Corrige a fonte: a quarta classe de `G3` e **`RETIRE`**, nao `REJECT` |
| [**RFC-0023**](../rfcs/RFC-0023-independencia-de-verificacao-por-fornecedor.md) | RFC | `RFC` | S | **180** | Submete a troca do criterio de afericao. Corrige a fonte: **`ADR-0005` nao contem criterio de afericao** |
| [**RFC-0024**](../rfcs/RFC-0024-superacao-de-ato-por-evidencia-posterior.md) | RFC | `RFC` | S | **168** | Submete o caminho de superacao de ato. **Quatro alternativas reais mais `Z`**; lacuna medida em **`0`** caminhos vigentes |
| [**RFC-0021**](../rfcs/RFC-0021-admissao-do-medally-como-primeiro-produto.md) | RFC | `RFC` | S | **253** | **Qual produto exerce `S1`.** **Tres** opcoes reais — medAlly agora, nXtrack primeiro, ambos — mais `Z`; recomenda a **Opcao A** e **declara que a leitura da decisao 7 e do Soberano** *(`Q1`, bloqueante)*. Registra a **ausencia de manifestacao de DEP-EXE**. **Acolhida** → ADR-0026 |
| [**ADR-0030**](../decisions/ADR-0030-admissao-do-nxtrack-como-primeiro-produto.md) | ADR | `ADR` | S | **340** | **Admissao do nXtrack** com `G0` = `IDENTIDADE` e `G3` = `RECOGNIZE`; cria `PRO-nxtrack`. `C2 · Tipo 1`. **`ativo` · `ratificacao: ratificada` — EM VIGOR pelo nono ato**, aplicado em 2026-08-01; `H-P` conferido *(`906dccd3…719fa`)*, `H-N` invariante, `atualizado_em` **nao tocado**. `G3` determinado **entre dois membros**, com `RETIRE` descartada por **fato citado**. **`0`** bytes do candidato |
| [**RFC-0025**](../rfcs/RFC-0025-admissao-do-nxtrack-como-primeiro-produto.md) | RFC | `RFC` | S | **187** | **O nXtrack deve ser admitido agora, com `G0` = `IDENTIDADE`?** **Tres** alternativas reais mais `Z`. Registra que `PT-2026-009` e `PS-2026-013` sao **artefatos distintos** *(`RD-64`)*. **`aprovado` pelo nono ato** — o ciclo de `RFC` **termina em `aprovado`**, e a transicao foi feita pela **variante** de `PS-2026-016 §2.1`, nunca pelo instrumento padrao, que poria `ativo`; `H-P` conferido *(`eecde504…a7b63`)* |
| [**RFC-0017**](../rfcs/RFC-0017-framework-de-specifications.md) | RFC | `RFC` | S | **393** | Propoe a sede da norma da `Spec` pela **Opcao C** *(regras dentro do ADR)*, entre **cinco alternativas e a opcao Z**; mede **5** defeitos em `TPL-spec` onde `RD-23` citava **2**; submete o vinculo `Spec × Produto`. **Primeira peca instrutoria do acervo cujo autor nao e DEP-GOV.** **Acolhida** → ADR-0021 |
| [**ADR-0031**](../decisions/ADR-0031-primeira-spec-governanca-de-dado-pessoal-do-nxtrack.md) | ADR | `ADR` | S | **271** | **Cria `SPC-001`, a primeira `Spec` do acervo**, sobre `LM-6(a)` de `PRO-nxtrack`, em **`C2 · Tipo 2`**. A elevacao acima do piso `C1` de `FND-04 §6` e fundada em colisao **medida** entre a coluna `C1 · T2` de `SF-10` e `FND-04 §3.1` — *Proponente = Aprovador* para `SPC` —, que torna a aprovacao **nula** por `LV-03`. **`ativo` · `ratificacao: nao-exigida`.** **3 alternativas reais + `Z`**; §5 declara a elevacao **restrita a esta criacao**. **Primeiro `ADR` do acervo cujo autor e DEP-PRD** |
| [**RFC-0026**](../rfcs/RFC-0026-primeira-spec-governanca-de-dado-pessoal-do-nxtrack.md) | RFC | `RFC` | S | **197** | **Em que recorte e sob que classe se cria a primeira `Spec` sobre `LM-6(a)`?** **Tres** opcoes reais mais `Z`, com `CR-1` a `CR-6` declarados antes. **`aprovado`** → `ADR-0031`. Registra a manifestacao das **quatro** areas, inclusive a ressalva de DEP-QAR sobre a propria concentracao de papeis *(`RD-92`)* |
| [**ADR-0032**](../decisions/ADR-0032-separacao-de-proponente-e-aprovador-na-spec-c1.md) | ADR | `ADR` | S | **227** | **Emenda `C3 · Tipo 2` que sana `RD-91`:** a aprovacao de `Spec` `C1` passa do **proprietario**, que e quem a propoe, para **DEP-EXE**. **`aprovado` · `ratificacao: pendente` — NAO VIGORA.** Emenda **`1`** celula de `FND-09 §8.2`, **`1`** da matriz de `SF-10` em cascata e **`6`** linhas em **`2`** Cartas ratificadas. **A celula que `RD-91` nomeava nao era a sede:** reproduz literalmente `FND-09 §8.2` linha `SPC` e `FND-04 §2.1` linha `C1`. **`0` bytes em `FND-04` · `0` titulares · `0` regras de conteudo de `Spec`** |
| [**RFC-0027**](../rfcs/RFC-0027-separacao-de-proponente-e-aprovador-na-spec-c1.md) | RFC | `RFC` | S | **203** | **Onde se emenda para separar proponente de aprovador na `Spec` `C1`, e ate onde.** **4 opcoes + `Z`**; a opcao que o achado sugeria cai **por medicao**. Declara `F9`: o mesmo colapso em `FND-09 §8.2` linhas **`PRJ`** e **`TPL`**. `aprovado` |

> **Correcao aplicada nesta emissao (achado D7 de [REV-SOBERANO §0](../foundation/revisao-arquitetural-conhecimento-do-soberano-2026-07-28.md)).**
> Os tres registros `MEM-APR` constavam desta classe **Decisoria**. Registro de aprendizado nao
> e artefato decisorio: FND-10 §4.6 aloca `MEM` a classe **Cognitiva**. Os tres migraram para
> §4.7. **Nenhum arquivo-fonte foi tocado** — o defeito era da vista derivada (PJ-03, RG-03).

### 4.3 Constitutiva — **33 Cartas: 23 de Capability, 9 de Departamento e 1 de Produto**

Todas com perfil **S**, tipo documental **Carta de Capability**, em `capabilities/`.
Resumo comum: *declara uma competencia permanente com 13 atributos, limites, indicadores e
criterios de evolucao*. Resumo especifico e custo:

| Carta | Linhas | Dominio · Classe | O que a organizacao sabe fazer |
|---|---|---|---|
| [estrategia](../capabilities/CAP-estrategia.md) | 161 | DIR · nucleo | Traduzir direcao em algo operavel |
| [governanca](../capabilities/CAP-governanca.md) | 162 | DIR · nucleo | Manter integridade normativa e rastreabilidade |
| [coordenacao](../capabilities/CAP-coordenacao.md) | 159 | DIR · habilitadora | Priorizar, alocar e arbitrar |
| [pesquisa](../capabilities/CAP-pesquisa.md) | 155 | VAL · habilitadora | Descobrir o que vale a pena existir |
| [produto](../capabilities/CAP-produto.md) | 164 | VAL · nucleo | Definir o problema e o resultado verificavel |
| [design](../capabilities/CAP-design.md) | 158 | VAL · habilitadora | Dar forma, comportamento e linguagem |
| [arquitetura](../capabilities/CAP-arquitetura.md) | 166 | REA · habilitadora | Decidir estrutura tecnica defensavel |
| [engenharia](../capabilities/CAP-engenharia.md) | 159 | REA · habilitadora | Construir a solucao mais simples que satisfaz |
| [dados](../capabilities/CAP-dados.md) | 158 | REA · habilitadora | Modelar, mover e confiar em dados |
| [inteligencia-artificial](../capabilities/CAP-inteligencia-artificial.md) | 162 | REA · nucleo | Escolher, instruir e avaliar modelos |
| [engenharia-de-agentes](../capabilities/CAP-engenharia-de-agentes.md) | 175 | REA · nucleo | Projetar papeis executores com escopo e limite |
| [qualidade](../capabilities/CAP-qualidade.md) | 178 | GAR · nucleo | Verificar de forma independente |
| [seguranca](../capabilities/CAP-seguranca.md) | 164 | GAR · habilitadora | Proteger dado, acesso e segredo |
| [juridico](../capabilities/CAP-juridico.md) | 159 | GAR · suporte | Verificar licitude contra norma externa |
| [operacoes](../capabilities/CAP-operacoes.md) | 163 | SUS · habilitadora | Manter funcionando o que existe |
| [infraestrutura](../capabilities/CAP-infraestrutura.md) | 156 | SUS · habilitadora | Prover e sustentar a base tecnica |
| [integracao](../capabilities/CAP-integracao.md) | 163 | SUS · habilitadora | Conectar capacidades externas com criterio |
| [marketing](../capabilities/CAP-marketing.md) | 161 | MER · habilitadora | Posicionar e comunicar ao publico |
| [comercial](../capabilities/CAP-comercial.md) | 157 | MER · habilitadora | Converter interesse em resultado |
| [financeiro](../capabilities/CAP-financeiro.md) | 161 | MER · suporte | Acompanhar custo, consumo e limite |
| [conhecimento](../capabilities/CAP-conhecimento.md) | 157 | COG · nucleo | Persistir e devolver o que se sabe |
| [aprendizado-organizacional](../capabilities/CAP-aprendizado-organizacional.md) | 160 | COG · nucleo | Converter experiencia em capacidade |
| [comunicacao](../capabilities/CAP-comunicacao.md) | 160 | COG · habilitadora | Transferir trabalho sem perder contexto |

**Subtotal: 3.718 linhas.**

#### 4.3.1 Cartas de Departamento — **9 de 9**, entidade `DEP`

Perfil **M**, em `departments/<dep>/`. Indice e projecao comparativa em [`departments/README.md`](../departments/README.md).
Contrato: [ADR-0011](../decisions/ADR-0011-contrato-de-carta-de-departamento.md).

| Carta | Classe | Linhas | Estado | Capabilities | Resumo operacional |
|---|---|---|---|---|---|
| [DEP-QAR](../departments/qar/carta.md) **1.2.0** | **Guarda** | **388** | **`ativo`** · ratificacao **ratificada** | 3 custodiadas | Verifica de forma independente, mede risco e barra entrega que nao atende o DoD |
| [DEP-ENG](../departments/eng/carta.md) **1.1.0** | **Linha** | **402** | **`ativo`** · ratificacao **ratificada** | 5 custodiadas | Constroi a solucao mais simples defensavel que satisfaz a spec e a sustenta |
| [**DEP-EXE**](../departments/exe/carta.md) **1.1.0** | **Comando** | **506** | **`ativo`** · ratificacao **ratificada** | 4 custodiadas | Converte direcao em prioridade executavel, aloca capacidade e arbitra entre areas de Linha |
| [**DEP-KMS**](../departments/kms/carta.md) **1.1.0** | **Plataforma** | **464** | **`ativo`** · ratificacao **ratificada** | 2 custodiadas · **1 exercida sem custodiar** | Faz a organizacao lembrar: cura as cinco camadas e devolve o contexto certo |
| [**DEP-GOV**](../departments/gov/carta.md) **1.0.0** | **Guarda** | **457** | **`ativo`** · ratificacao **ratificada** | 1 custodiada | Mantem a integridade normativa e barra o que exista sem rastreabilidade ou responsavel |
| [**DEP-TLS**](../departments/tls/carta.md) **1.1.0** | **Plataforma** | **425** | **`ativo`** · ratificacao **ratificada** | 1 custodiada | Prove, avalia e mantem as capacidades externas, para que ninguem improvise acesso |
| [**DEP-PRD**](../departments/prd/carta.md) **1.1.0** | **Linha** | **445** | **`ativo`** · ratificacao **ratificada** | 3 custodiadas | Define o que deve existir e por que, com criterio de aceite verificavel |
| [**DEP-OPS**](../departments/ops/carta.md) **1.1.0** | **Linha** | **438** | **`ativo`** · ratificacao **ratificada** | 2 custodiadas | Mantem em funcionamento o que ja existe, com backup verificado e continuidade |
| [**DEP-GRW**](../departments/grw/carta.md) **1.1.0** | **Linha** | **444** | **`ativo`** · ratificacao **ratificada** | 2 custodiadas | Leva o construido a quem tem o problema, sob aprovacao humana para toda saida externa |

**Subtotal: 3.925 linhas.** **9 de 9 departamentos com Carta — cobertura documental completa.**
**9 em vigor; 0 aguardando ato do Soberano** (DC-09).

> **As nove Cartas estao em vigor, por quatro atos soberanos distintos.** `DEP-QAR` e `DEP-ENG`
> por [MSG-2026-0001](../memory/operacional/MSG-2026-0001-ato-soberano-ratificacao-cartas-piloto.md);
> `DEP-EXE` e `DEP-KMS` por [MSG-2026-0002](../memory/operacional/MSG-2026-0002-ato-soberano-cartas-comando-plataforma-e-contexto.md);
> `DEP-GOV`, `DEP-TLS`, `DEP-PRD`, `DEP-OPS` e `DEP-GRW` por [MSG-2026-0004](../memory/operacional/MSG-2026-0004-ato-soberano-cartas-emenda-constitucional-e-regime-do-fitness-check.md);
> e as emendas `DEP-KMS` **1.1.0** e `DEP-ENG` **1.1.0** por
> [**MSG-2026-0006**](../memory/operacional/MSG-2026-0006-ato-soberano-aplicacao-integral.md).
> **Quatro atos, quatro fontes** — nenhuma acumula (CM-09). **As nove Cartas estao escritas**, e
> o achado **IC-4** está **fechado desde a Missao 1.9**.
>
> **Esta secao declarava, ate a aplicacao do sexto ato, cinco Cartas em `em-revisao` que estavam
> em vigor havia tres missoes, e `DEP-QAR` em 1.1.0 · 387 linhas.** Eram **13 valores
> divergentes da fonte**, **11 deles anteriores a este ato** — achado **RD-25**, corrigido
> **na projecao**, valor a valor, **sem alterar fonte alguma** (`PJ-03`, `RG-03`).

> **A entrada em vigor e a operacao `O4`** (FND-10 §5.2): dois campos de frontmatter por Carta,
> com **`H-N` invariante**. Nas sete Cartas que nao foram emendadas, **nenhuma linha de corpo
> mudou**. Em `DEP-KMS` **1.1.0** e `DEP-ENG` **1.1.0** o corpo **mudou por emenda ratificada**,
> nao por transicao: **+4** e **+2** linhas, exatamente nos diffs `K1`—`K10` e `E1`—`E7` de
> [PS-2026-006](pacote-soberano-2026-07-29-kms-eng.md), com `IR-09` reproduzindo `H-A`.

#### 4.3.2 Carta de Produto — **1 de 1**, entidade `PRO`

**Primeira instancia do tipo `Carta de Produto`** e **primeira instancia da entidade `PRO`** na
historia do acervo. Perfil **S**, em `products/<slug>/`, forma de `TPL-carta-produto` **1.1.0**.

| Carta | Linhas | Estado | Capabilities | O que o Produto e |
|---|---|---|---|---|
| [**PRO-nxtrack**](../products/nxtrack/carta.md) **1.0.0** | **263** | **`ativo`** · ratificacao **ratificada** | **5** consumidas — `CAP-produto`, `CAP-inteligencia-artificial`, `CAP-dados`, `CAP-engenharia`, `CAP-operacoes` | Camada de inteligencia sobre o Rekordbox que prepara sets, cuida da biblioteca do DJ e **explica cada recomendacao**, sem alterar o banco interno do software |

**Subtotal: 263 linhas. 1 de 1 Produto com Carta, e 1 em vigor.**

> **Em vigor pelo NONO ato soberano**, [MSG-2026-0009](../memory/operacional/MSG-2026-0009-ato-soberano-admissao-do-nxtrack.md)
> item **III**, aplicado pela Missao 1.13.4.5. `H-A` do arquivo **aplicado**:
> **`fca656a904e67b11b965354233b7352be9cf41131c88fda2baebc30e8eb039e2`** — **medido no arquivo do
> acervo**, e distinto do `H-A` do **candidato** *(`4d4c12e0…75c5`, em
> `_missao-1-13-4-4-2026-08-01/candidatos/`)*, que **nao e artefato** e permanece intacto.
> Publicar um pelo outro foi o defeito `RD-19`, que `DF-1` de [`PS-2026-016 §3`](pacote-soberano-2026-08-01-nxtrack.md) fecha.

> **`VC-03` dispara e esta declarado, e a Carta nao o esconde.** Cinco vinculos e **mais de
> tres** — sinal de componente amplo demais (`FND-08`, `VC-03`). **Nenhuma Capability foi
> criada** e a lista **nao foi reduzida para caber no limiar**: reduzi-la falsearia o vinculo, e
> `VC-01` proibe elo que nao corresponde. Achado **`RD-74`**, dono DEP-PRD, gatilho na primeira `Spec`.

> **A custodia descrita e a que o ato institui, nao a que existe.** O produto vive em subarvore
> de repositorio de terceiro, **sem repositorio proprio** — achado **`RD-71`**, ABERTO. `G0` e
> `IDENTIDADE`: **`0` bytes** do repositorio do candidato entraram no acervo.

> **Vinculo ID × versao × hash exigido pelos atos.** Cada registro canonico anexa **tres**
> hashes — **H-A** do arquivo submetido, **H-N** do conteudo normativo e **H-P** apos a
> transicao —, conforme [ADR-0012 §5.2](../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md),
> `IR-07`. Os vinculos estao em [MSG-2026-0001 §2](../memory/operacional/MSG-2026-0001-ato-soberano-ratificacao-cartas-piloto.md)
> e [MSG-2026-0002 §2](../memory/operacional/MSG-2026-0002-ato-soberano-cartas-comando-plataforma-e-contexto.md)
> — **fontes**; esta secao **nao os reproduz** (CM-09, PJ-01).

> **A emenda `DEP-QAR` 1.1.0 nao esta neste catalogo, e isso e correto.** Ela e **proposta**, e
> nao artefato do acervo: o texto candidato **nao foi escrito** em `departments/qar/carta.md`,
> que permanece com a **1.0.0 ratificada** intacta. O pacote — diff, hash e impacto — vive em
> [REV-ESTRUTURAL-I §7](../foundation/revisao-estrutural-01-2026-07-28.md).

### 4.4 Formal — 19 Templates, entidade `TPL`

Todos com perfil **S**, em `foundation/templates/`. Resumo comum: *fixa a forma obrigatoria
de um tipo documental*.

| Template | Linhas | Formaliza |
|---|---|---|
| [TPL-documento](../foundation/templates/TPL-documento.md) | 166 | **Template universal** — estrutura minima + contrato de artefato + teste preventivo de projecao |
| [TPL-adr](../foundation/templates/TPL-adr.md) | 198 | ADR, com as 13 secoes obrigatorias |
| [TPL-rfc](../foundation/templates/TPL-rfc.md) | 137 | RFC |
| [TPL-nota-decisao](../foundation/templates/TPL-nota-decisao.md) | 102 | Nota de Decisao (C1/Tipo 2) |
| [TPL-capability](../foundation/templates/TPL-capability.md) | 182 | Carta de Capability, 13 atributos |
| [TPL-carta-departamento](../foundation/templates/TPL-carta-departamento.md) | **339** | Carta de Departamento, com os 12 blocos e o checklist do contrato de **ADR-0011** |
| [TPL-carta-agente](../foundation/templates/TPL-carta-agente.md) | 155 | Carta de Agente e de Subagente |
| [TPL-carta-produto](../foundation/templates/TPL-carta-produto.md) **1.1.0** | **183** | Carta de Produto — **com `capabilities`, os cinco campos de `FND-10 §2.2`, Capabilities consumidas e interfaces.** Fecha **`RD-56`** |
| [TPL-carta-projeto](../foundation/templates/TPL-carta-projeto.md) | 120 | Carta de Projeto |
| [**TPL-spec**](../foundation/templates/TPL-spec.md) | **272** | Spec — **1.1.0**, emenda **C2** por `ADR-0021` que fecha **`RD-23`**: aprovador **derivado da classe**, `ratificacao` presente, os cinco campos do contrato, `QG-1` liberado por **DEP-EXE**, e o corpo exigido por `SF-05` a `SF-31` |
| [TPL-skill](../foundation/templates/TPL-skill.md) | 124 | Skill |
| [TPL-workflow](../foundation/templates/TPL-workflow.md) | 124 | Workflow |
| [TPL-ferramenta](../foundation/templates/TPL-ferramenta.md) | 145 | Ficha de Ferramenta |
| [TPL-memoria](../foundation/templates/TPL-memoria.md) | 141 | Registro de memoria, 5 camadas |
| [TPL-handoff](../foundation/templates/TPL-handoff.md) | 114 | Mensagem de canal HANDOFF |
| [TPL-reporte](../foundation/templates/TPL-reporte.md) | 121 | Mensagem de canal REPORTE |
| [TPL-excecao](../foundation/templates/TPL-excecao.md) | 124 | Excecao formal |
| [TPL-incidente](../foundation/templates/TPL-incidente.md) | 157 | Incidente de conformidade |
| [TPL-fitness-check](../foundation/templates/TPL-fitness-check.md) | 244 | Verificacao de aptidao (QG-6), com F2 desdobrada em ocorrencia e prevencao |

**Subtotal: 3.098 linhas** — **2.958 + 140**, o crescimento de `TPL-spec` de **132** para **272**.
*(A soma dos proprios 19 valores desta tabela e **3.098**, conferida por ferramenta; o metodo de
somar a coluna contra a propria linha e a mitigacao `RG-2`, exercida aqui pela segunda vez.)*
Verificados contra T1–T4 de FND-10 §10.2: **19 de 19 passam.**
**Nenhum template criado nesta missao; um emendado** — `TPL-spec` **1.0.0 → 1.1.0**, hash
`cabaa58e…f748` → `afd0dc7e…370f`, **`LF` preservado em 0 bytes `CR`**.

> **Achado `RD-34`, declarado e nao corrigido.** **19 de 19** templates declaram
> **`aprovador: SOBERANO`** no proprio cabecalho, enquanto `FND-09 §8.2` linha `TPL` e
> `FND-10 §10.3` linha *Template* dao **`Aprova: DEP-GOV`** e **`Ratifica: —`**. **Leitura
> alternativa declarada:** o campo pode registrar **fato historico** — os templates foram
> acolhidos pelo ato que adotou a Fundacao — e nao afirmacao de norma. **Corrigir um dos 19
> criaria divergencia entre iguais**, e corrigir os dezenove e outra materia. Severidade
> **Baixa**, dono **DEP-GOV**, gatilho *"proxima emenda que alcance os `TPL`"*. **Encontrado por
> extrair o frontmatter da familia inteira** — e a extracao **barrou** a correcao parcial
> ([MEM-APR-0006](../memory/aprendizado/MEM-APR-0006-exercer-o-contador-revela-o-defeito.md) `V4`).

### 4.5 Avaliativa — **34** artefatos, entidade `FIT`

| Artefato | Tipo | `classe_avaliacao` | Perfil | Linhas | Resumo operacional |
|---|---|---|---|---|---|
| [FIT-2026-001](fitness/FIT-2026-001-meta-model.md) | Fitness Check | aptidao | M | 242 | Avalia a aptidao do Meta Model. `apto-com-ressalva`, 3 ressalvas |
| [FIT-2026-002](fitness/FIT-2026-002-artifact-framework.md) | Fitness Check | aptidao | M | 248 | Avalia a aptidao do Artifact Framework. `apto-com-ressalva`, 4 ressalvas |
| [FIT-2026-003](fitness/FIT-2026-003-consolidacao-baseline.md) | Fitness Check | aptidao | M | 274 | Avalia a aptidao da consolidacao da Missao 1.4. Veredito em §Veredito |
| [REV-CAP-2026-07-28](../capabilities/revisao-arquitetural-2026-07-28.md) | Revisao Arquitetural | corretude | M | 397 | Examina o catalogo de 23 Capabilities. 7 achados, nenhum bloqueante |
| [REV-META-2026-07-28](../foundation/revisao-arquitetural-meta-model-2026-07-28.md) | Revisao Arquitetural | corretude | M | 480 | Examina o Meta Model. 8 achados, 3 divergencias corrigidas na revisao |
| [REV-ARTIFACT-2026-07-28](../foundation/revisao-arquitetural-artifact-framework-2026-07-28.md) | Revisao Arquitetural | corretude | M | 354 | Examina o Artifact Framework e as 3 correcoes obrigatorias. 7 achados |
| [REV-CONSOLIDACAO-2026-07-28](../foundation/revisao-arquitetural-consolidacao-2026-07-28.md) | Revisao Arquitetural | corretude | M | 331 | Examina a consolidacao da Missao 1.4: fronteira, ratificacao, baseline, projecoes e ressalvas |
| [FIT-2026-004](fitness/FIT-2026-004-conhecimento-do-soberano.md) | Fitness Check | aptidao | M | 302 | Avalia a aptidao da Missao 1.5. `apto-com-ressalva`, 4 ressalvas |
| [REV-SOBERANO-2026-07-28](../foundation/revisao-arquitetural-conhecimento-do-soberano-2026-07-28.md) | Revisao Arquitetural | corretude | M | 384 | Examina o contrato sobre o Soberano, o registro canonico e o fechamento de C13. 8 achados |
| [FIT-2026-005](fitness/FIT-2026-005-cartas-de-departamento.md) | Fitness Check | aptidao | M | 325 | Avalia a aptidao da Missao 1.6. `apto-com-ressalva`, 5 ressalvas, rollout **ADJUST** |
| [REV-DEPARTAMENTO-2026-07-28](../foundation/revisao-arquitetural-cartas-de-departamento-2026-07-28.md) | Revisao Arquitetural | corretude | M | 516 | Examina o contrato de Carta, a projecao e os dois pilotos; 6 cenarios de validacao, 8 achados |
| [**FIT-2026-006**](fitness/FIT-2026-006-validacao-interclasses.md) | Fitness Check | aptidao | M | **442** | Avalia a aptidao da Missao 1.7. `apto-com-ressalva`, 4 ressalvas, rollout **ADJUST**, consolidacao **aberta**, 4 pendencias ao Soberano |
| [**REV-INTERCLASSES-2026-07-28**](../foundation/revisao-arquitetural-validacao-interclasses-2026-07-28.md) | Revisao Arquitetural | corretude | M | **746** | Verifica a ativacao dos pilotos, as Cartas de Comando e Plataforma; 8 cenarios interclasses nas 4 classes, comparacao unica das classes, 7 achados |
| [**REV-ESTRUTURAL-I-2026-07-28**](../foundation/revisao-estrutural-01-2026-07-28.md) | Revisao Arquitetural | corretude | M | **609** | **Primeira Revisao Estrutural** (FND-02 §9.4): rito sobre Fundacao, 23 Capabilities, 21 entidades, 33 tipos e 4 classes; **mapa unico de bloqueios**; IC-8 resolvido; EV-08 encerrada; 6 achados |
| [**FIT-2026-007**](fitness/FIT-2026-007-revisao-estrutural-i.md) | Fitness Check | aptidao | M | **364** | Avalia a aptidao da Missao 1.8. `apto-com-ressalva`, 4 ressalvas, rollout **GO-CONDITIONAL**, 1 pendencia ao Soberano |
| [**REV-ROLLOUT-2026-07-28**](../foundation/revisao-arquitetural-rollout-cartas-2026-07-28.md) | Revisao Arquitetural | corretude | M | **297** | Valida as **cinco** Cartas novas em **onze testes cada** — 55 execucoes, 0 falhas estruturais; varredura do termo *ratificar*; 8 achados |
| [**FIT-2026-008**](fitness/FIT-2026-008-rollout-das-cartas.md) | Fitness Check | aptidao | M | **373** | Avalia a aptidao da Missao 1.9. `apto-com-ressalva`, 4 ressalvas, fechamento **`READY-FOR-RATIFICATION`**, 3 pendencias ao Soberano |

| [**FIT-2026-009**](fitness/FIT-2026-009-ativacao-e-endurecimento.md) | Fitness Check | aptidao | M | **369** | Avalia a aptidao da Missao 1.10. `apto-com-ressalva`, 4 ressalvas, fechamento **`BLOCKED`** |
| [**FIT-2026-010**](fitness/FIT-2026-010-aplicacao-do-ato-soberano.md) | Fitness Check | aptidao | M | **305** | Avalia a **aplicacao do ato de 2026-07-29**. `apto-com-ressalva`, 4 ressalvas, fechamento **`GO-CONDITIONAL`**. **Primeiro `FIT` sob `FT-10`** |
| [**FIT-2026-011**](fitness/FIT-2026-011-fechamento-de-autoridade.md) | Fitness Check | aptidao | M | **341** | Avalia o **fechamento de autoridade** da Missao 1.11. `apto-com-ressalva`, **3 ressalvas + 2 reclassificacoes**, fechamento **`READY-FOR-RATIFICATION`**. **Aprovacao escalada ao SOBERANO** |
| [**FIT-2026-012**](fitness/FIT-2026-012-fechamento-normativo-final.md) | Fitness Check | aptidao | M | **342** | Avalia o **fechamento normativo** da Missao 1.12. `apto-com-ressalva`, **2 ressalvas + 2 reclassificacoes**, fechamento **`READY-FOR-RATIFICATION`**. **Fecha R4 de FIT-2026-002**; aprovacao escalada ao SOBERANO |
| [**FIT-2026-013**](fitness/FIT-2026-013-verificacao-de-ratificacao.md) | Fitness Check | aptidao | M | **297** | Avalia a **continuacao da Missao 1.12**. `apto-com-ressalva`, **1 ressalva + 1 reclassificacao que corrige erro proprio**, fechamento **`BLOCKED`** por **ausencia de ato**. **12 objetos verificados, 0 falhas** |
| [**FIT-2026-014**](fitness/FIT-2026-014-regime-ministerial-e-cobertura-de-contexto.md) | Fitness Check | aptidao | M | **334** | Avalia o **fechamento operacional** da Missao 1.12.1. `apto-com-ressalva`, **2 ressalvas**, **`C11` 13 de 13**, fechamento **`GO-TO-SPECS`**. **Primeira recusa registrada de verbo de autoridade**; `RD-23` como **pre-correcao obrigatoria** |
| [**FIT-2026-016**](fitness/FIT-2026-016-canonizacao-e-propagacao.md) | Fitness Check | aptidao | M | **294** | Avalia os **dois ritos** da Missao 1.13.1. `apto-com-ressalva`, **4 ressalvas novas**, **`C11` 13 de 13**, fechamento **`READY-FOR-RATIFICATION`**. **Cinco abstracoes evitadas**; **7 metodos reutilizaveis**; `PJ-05` **barrou 4 reproducoes**. **`R4` registra impedimento parcial de aprovacao**, resolvido por recorte |
| [**FIT-2026-017**](fitness/FIT-2026-017-convergencia-pre-ratificacao.md) | Fitness Check | evolutiva | S | **271** | Aptidao da **Missao 1.13.2**: `apto-com-ressalva`, **3** ressalvas novas e **3 fechadas**; **`C11` 13 de 13**; **20 de 20** controles de integridade reproduzem; `F6` registra que **remedir o custo de `ADR-0020` mostrou o que a medicao original nao contava** |
| [**FIT-2026-018**](fitness/FIT-2026-018-vigencia-do-framework-de-specifications.md) | Fitness Check | evolutiva | S | **135** | Aptidao da **aplicacao** do setimo ato soberano: **15 de 15** controles conformes, **5** dimensoes de melhora medidas, **3** ressalvas e **3** ausencias de evidencia declaradas. Veredito **`apto-com-ressalva`** |
| [**FIT-2026-019**](fitness/FIT-2026-019-admissao-do-medally.md) | Fitness Check | evolutiva | S | **180** | Aptidao da **Missao 1.13.4**: **20 de 20** controles conformes e **`C11` 13 de 13** — a **primeira vez** que `C11-12` *(conteudo externo admitido fora do portao)* tem objeto real. **4** ressalvas, sendo **`R4`** *(`Q1`)* **nao resolvivel por parecer**; **6** ausencias declaradas. Veredito **`apto-com-ressalva`** |
| [**FIT-2026-020**](fitness/FIT-2026-020-emenda-do-portao-de-origem-externa.md) | FIT | `FIT` | M | **133** | `apto-com-ressalva` · **3** ressalvas · **`C11` 13 de 13**. Avalia `RFC-0022` e `ADR-0027` |
| [**FIT-2026-021**](fitness/FIT-2026-021-independencia-de-verificacao-por-fornecedor.md) | FIT | `FIT` | M | **142** | `apto-com-ressalva` · **4** ressalvas · **`C11` 13 de 13**. Registra que a correcao do objeto superado **elevou o rito de `C2` para `C3`** |
| [**FIT-2026-022**](fitness/FIT-2026-022-superacao-de-ato-por-evidencia-posterior.md) | FIT | `FIT` | M | **134** | `apto-com-ressalva` · **4** ressalvas · **`C11` 13 de 13**. `RA-1`: irreversibilidade **certa**, nao mitigavel |
| [**FIT-2026-023**](fitness/FIT-2026-023-admissao-do-nxtrack.md) | FIT | `FIT` | M | **151** | `apto-com-ressalva` · **4** ressalvas · **14 de 14** controles conformes, remedidos por metodo distinto. Cumpre **`G4`** do portao sobre o **nXtrack** e `CV-07`. **`9`** resultados negativos declarados |
| [**FIT-2026-024**](fitness/FIT-2026-024-primeira-spec.md) | FIT | `FIT` | M | **211** | `apto-com-ressalva` · **4** ressalvas. Avalia a **primeira `Spec` do acervo** — `SPC-001`, `ADR-0031` e `RFC-0026`. **Exigido, nao opcional:** a classe e `C2`, e `SF-24` item (9) o poe no `DoD`. Mede **27 de 32** regras `SF-*` saindo de *determinadas* para *observadas*; **`1`** reproducao barrada antes de escrita *(a matriz de 50 celulas de `SF-10`)*; custo de contexto **desce** para a consulta enderecada *(13 linhas contra 555 que nao respondiam)* e **sobe 311** na leitura integral — **as duas direcoes declaradas** |
| [**FIT-2026-025**](fitness/FIT-2026-025-emenda-de-sf-10.md) | FIT | `FIT` | M | **175** | `apto-com-ressalva` · **4** ressalvas. Avalia **`ADR-0032`, `RFC-0027` e os 4 candidatos** da emenda que sana `RD-91`. **Exigido, nao opcional:** a classe e `C3`, e `CC-04`/`CV-07` o poem em `QG-6`. Mede **27** linhas de norma nova contra **3** artefatos por `Spec` economizados, e **4 de 4** incompatibilidades de `FND-04 §3.1` dissolvidas. **`1`** reproducao barrada antes de escrita — *a emenda confinada a `FND-11 §5`, que nao sanaria*. Ressalva `S2`: `PRJ` e `TPL` ficam com o defeito identico |
| [**FIT-2026-015**](fitness/FIT-2026-015-framework-de-specifications.md) | Fitness Check | aptidao | M | **394** | Avalia o **Framework de Specifications** da Missao 1.13. `apto-com-ressalva`, **3 ressalvas**, **`C11` 13 de 13**, fechamento **`ADJUST`** com as outras quatro opcoes recusadas uma a uma. **Quatro abstracoes evitadas**; **7 metodos reutilizaveis**; **`RD-23` FECHADA**. **Primeiro `FIT` do acervo em que `DEP-GOV` nao e autor de nenhum objeto avaliado** |

### 4.6 Registro — **12** indices, entidade **a que indexam**

| Indice | Indexa | Perfil | Linhas | Resumo operacional |
|---|---|---|---|---|
| [**IDX-atos-superados**](atos-superados.md) | os atos soberanos **superados por evidencia posterior** | S | **95** | **Registro exigido por `SA-6`**, criado pelo **oitavo ato** que ratificou `ADR-0029`. **Nasce com o contador em `0`** — `0` atos superados, `0` instauracoes abertas, **8** atos vigentes superaveis. **E fonte, nao projecao** |
| [IDX-raiz](../README.md) | o acervo *(composto, IX-03)* | S | **392** | Porta de entrada: o que existe, o que nao existe por decisao, por onde comecar |
| [IDX-foundation](../foundation/README.md) | `FND` e `TPL` | S | **218** | Indexa os 10 documentos normativos e os 19 templates, com ordem de leitura. **Declara o candidato `FND-11`, submetido e nao vigente** |
| [IDX-decisions](../decisions/README.md) | `ADR` | S | **141** | Contador oficial da sequencia ADR; **projeta** o estado de ratificacao de INC-2026-001 §11. **Contador corrigido de `0019` para `0021`** — achado `RD-32` |
| [IDX-rfcs](../rfcs/README.md) | `RFC` | S | **103** | Contador oficial da sequencia RFC e resultado de cada proposta. **Contador corrigido de `0015` para `0017`** — achado `RD-32` |
| [IDX-capabilities](../capabilities/README.md) | `CAP` | M | **354** | Catalogo das 23 Capabilities, mapa de dependencias, relacoes de verificacao e a **projecao Departamento × Capability** |
| [IDX-governance](README.md) | `EXC` `INC` `FIT` *(composto)* | S | **207** | Contadores e estado de excecoes, incidentes e verificacoes de aptidao. **Contador `FIT` corrigido de `013` para `015`** *(`RD-32`)* e **agregado de ressalvas corrigido de `46` para `50`** *(`RD-35`)* |
| [IDX-exceptions](exceptions/README.md) | `EXC` | S | **51** | Registro de excecoes formais vigentes — nenhuma |
| [IDX-incidents](incidents/README.md) | `INC` | S | **91** | Registro de incidentes de conformidade — **2, ambos `fechado`** |
| [IDX-fitness](fitness/README.md) | `FIT` | S | **260** | Contador e serie de vereditos de aptidao. **Contador corrigido de `013` para `015`** — achado `RD-32` |
| [IDX-artifact-registry](artifact-registry.md) | o acervo *(transversal)* | S | *(este)* | Classifica **216 de 217** artefatos por tipo, entidade, perfil, custo e proveniencia; materializa a baseline. *(Este resumo declarava **194** — cinco baselines atras, familia de `RD-77`; corrigido **na projecao**, por contagem de ferramenta.)* |
| [**IDX-departamentos**](../departments/README.md) | `DEP` | S | **333** | Indexa as **9** Cartas e projeta a **comparacao unica** entre elas: classes, custodia, portoes, memoria, impedimentos e lacunas. **Fecha DR-4** |

> **`products/` nasce SEM indice de diretorio, e a ausencia e declarada, nao suprida.** Todas as
> outras raizes do acervo tem `README` contador *(`RG-04`)*; `products/` **nao tem**, porque a
> lista de reconciliacao do nono ato — [`PS-2026-016 §3`](pacote-soberano-2026-08-01-nxtrack.md)
> — enumera **catalogo §2/§4/§7/§9/§10, `decisions/README`, `rfcs/README`, `governance/README`,
> `governance/fitness/README` e o `README` da raiz**, e **nao inclui um indice de `products/`**.
> **Cria-lo seria a missao ministerial criando artefato que o ato nao autorizou** e mexendo na
> contagem da baseline por conta propria. Achado **`RD-85`**, dono **DEP-GOV**, gatilho *"missao
> de catalogo, ou segunda admissao de Produto — o que ocorrer primeiro"*. **ABERTO, e nao gera
> missao:** congelamento em vigor. **Os indices seguem `12`.**

### 4.7 Cognitiva — 6 indices e **50** registros, entidades `MEM` e `MSG`

| Registro | Camada | Perfil | Linhas | Resumo operacional |
|---|---|---|---|---|
| [MEM-EST-0001](../memory/estrategica/MEM-EST-0001-contexto-do-soberano.md) | **EST** | S | 282 | Registra o que se sabe, com prova, sobre o Soberano — e o que nao se sabe. **`ativo`**, ratificacao **ratificada**, com as **11 lacunas `unknown` intactas** |
| [MEM-APR-0001](../memory/aprendizado/MEM-APR-0001-ratificacao-por-precedente.md) | APR | S | 122 | Licao: ressalva escrita nao neutraliza condicao de validade |
| [MEM-APR-0002](../memory/aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md) | APR | S | **156** | Licao: detectar duplicacao nao previne duplicacao — o autor verifica antes de submeter. **5 ocorrencias** |
| [MEM-APR-0003](../memory/aprendizado/MEM-APR-0003-campo-de-estado-em-artefato-imutavel.md) | APR | S | 127 | Licao: campo de estado em artefato M1 registra o estado no ato, nunca o corrente |
| [MEM-APR-0004](../memory/aprendizado/MEM-APR-0004-projecao-revela-divergencia-antiga.md) | APR | S | 162 | Licao: projetar a mesma fonte por outro eixo revela divergencia que a leitura habitual nao revela |
| [**MEM-APR-0005**](../memory/aprendizado/MEM-APR-0005-medir-a-ausencia-na-fonte-errada.md) | APR | S | **184** | Licao: **buscar o termo em vez da funcao produz achado de lacuna onde ha titular declarado** — causa de `RD-22`, `RD-23` e `RD-26`. **3 ocorrencias**; `V1` a `V4` obrigatorias antes de afirmar ausencia |
| [**MEM-APR-0006**](../memory/aprendizado/MEM-APR-0006-exercer-o-contador-revela-o-defeito.md) | APR | S | **178** | Licao: **exercer o instrumento revela o defeito que ler o instrumento nao revela** — origem de `RD-31`, `RD-32`, `RD-33` e `RD-34`. **1 ocorrencia, confianca `alta` justificada como mecanica e nao estatistica**; `V1` a `V4` obrigatorias; declara os **7** achados que somente a leitura encontraria |
| [**MSG-2026-0001**](../memory/operacional/MSG-2026-0001-ato-soberano-ratificacao-cartas-piloto.md) | **OPR** | **M** | **222** | **Fonte canonica unica** do ato soberano de 2026-07-28 sobre `DEP-QAR` e `DEP-ENG`, com IDs, versoes e hashes vinculados. **Primeira instancia do tipo `Diretiva`** |
| [**MSG-2026-0002**](../memory/operacional/MSG-2026-0002-ato-soberano-cartas-comando-plataforma-e-contexto.md) | **OPR** | **M** | **303** | **Fonte canonica unica** do ato soberano de 2026-07-28 sobre `DEP-EXE`, `DEP-KMS`, `MEM-EST-0001`, os dois `FIT` e a Primeira Revisao Estrutural. **Tres hashes por artefato** e o **teste de reconstrucao** do texto ratificado |
| [**MSG-2026-0003**](../memory/operacional/MSG-2026-0003-ato-soberano-emenda-qar-e-criterio-de-consolidacao.md) | **OPR** | **M** | **295** | **Fonte canonica unica** do ato soberano de 2026-07-28 sobre a emenda **`DEP-QAR` 1.1.0** e o **criterio de consolidacao**. Preserva a versao **1.0.0** por quatro vias; **dez** verificacoes de eficacia |
| [**PS-2026-002**](pacote-soberano-2026-07-28-cartas.md) | **OPR** | **M** | **261** | **Pacote de decisao soberana**: as **5** Cartas em `em-revisao` com ID, versao, dois hashes e recomendacao, mais a emenda **C3** candidata e a questao **Q2** escalada |

| Indice | Camada | Perfil | Linhas | Resumo operacional |
|---|---|---|---|---|
| [memory/README](../memory/README.md) | todas | S | **136** | Indexa as 5 camadas, criterio de alocacao e regras de curadoria. **Dois valores corrigidos** — autoridade de `APR` de `5` para **`4`** *(fonte: `FND-06 §2`)* e registros `OPR` de `3` para **`6`**: achado **`RD-35`** |
| [estrategica/README](../memory/estrategica/README.md) | EST | S | **132** | Camada de identidade e direcao — **1 registro** |
| [produto/README](../memory/produto/README.md) | PRD | S | 73 | Camada de entendimento de produto — **0 registros.** Continua vazia: **nenhum produto existe**, e criar produto e ato do SOBERANO — achado `RD-33` |
| [tecnica/README](../memory/tecnica/README.md) | TEC | S | 78 | Camada de como o sistema esta construido — 0 registros |
| [operacional/README](../memory/operacional/README.md) | OPR | S | **123** | Camada de estado corrente, efemera por padrao — **6 registros**. **`1.2.1`**, correcao `C0` do achado **`RD-29`** |
| [aprendizado/README](../memory/aprendizado/README.md) | APR | S | **120** | Camada de licoes extraidas — **6 registros**. **Unico contador de sequencia que `RD-32` encontrou correto** entre os que verificou |

| [**MSG-2026-0004**](../memory/operacional/MSG-2026-0004-ato-soberano-cartas-emenda-constitucional-e-regime-do-fitness-check.md) | OPR | M | **293** | **Ato soberano** de 2026-07-29: cinco Cartas, ADR-0014 e regime do `FIT`. Fonte canonica unica |
| [**MSG-2026-0005**](../memory/operacional/MSG-2026-0005-ato-soberano-aplicacao-dep-qar.md) | OPR | M | **221** | **Ato soberano** que libera a **aplicacao** de `DEP-QAR` 1.2.0 e determina a Missao 1.11 |
| [**PS-2026-003**](pacote-soberano-2026-07-29-emendas.md) | OPR | M | **328** | Pacote das **tres** emendas locais a Cartas ratificadas |
| [**PS-2026-004**](pacote-soberano-2026-07-29-rd-02.md) | OPR | M | **279** | Pacote da emenda **C3** a FND-02 §4 — fecha **RD-02** |
| [**PS-2026-005**](pacote-soberano-2026-07-29-rd-09.md) | OPR | M | **270** | Pacote da emenda **C3** a FND-09 §8.2 e FND-10 §10.3 — fecha **RD-09** |
| [**PS-2026-006**](pacote-soberano-2026-07-29-kms-eng.md) | OPR | M | **269** | **Reemissao** de `DEP-KMS` 1.1.0 e `DEP-ENG` 1.1.0, com prova de identidade |
| [**PT-2026-001**](relatorio-transicao-2026-07-29-departamentos.md) | EST | M | **397** | Pacote de transicao da Missao 1.10; decisao **`BLOCKED`**; **RS-1 a RS-10** para o Specification Framework |
| [**PT-2026-002**](relatorio-transicao-2026-07-29-fechamento.md) | EST | M | **316** | Pacote de fechamento da Missao 1.11; **teste de consumo por Specs**; **mapa de bloqueios**; decisao **`READY-FOR-RATIFICATION`** |
| [**PS-2026-007**](pacote-soberano-2026-07-29-rd-14.md) | OPR | M | **283** | Pacote da emenda **C3** a FND-01 §6.2 — fecha **RD-14** |
| [**PS-2026-008**](pacote-soberano-2026-07-29-rd-15.md) | OPR | M | **333** | Pacote da emenda **C3** a FND-09 §8.2 e FND-10 §10.3 — fecha **RD-15**; declara **RD-19** |
| [**PT-2026-003**](relatorio-transicao-2026-07-29-fechamento-normativo.md) | EST | M | **405** | Pacote de fechamento da Missao 1.12; **prova de consumo executada duas vezes**; **divida reconciliada de RD-08 a RD-20**; decisao **`READY-FOR-RATIFICATION`** |
| [**PT-2026-004**](relatorio-transicao-2026-07-29-ratificacao.md) | EST | M | **408** | Continuacao da Missao 1.12; **mapa de ratificacao** das cinco cadeias; **verificacao pre-aplicacao de 12 objetos**; **candidato cumulativo**; decisao **`BLOCKED`** |
| [**MSG-2026-0006**](../memory/operacional/MSG-2026-0006-ato-soberano-aplicacao-integral.md) | OPR | M | **443** | **Fonte canonica unica** do **sexto ato soberano**: ratifica `ADR-0016` a `ADR-0019`, promulga **FND-01 1.5.0**, **FND-02 1.3.0**, **FND-09 1.5.0 cum.** e **FND-10 1.4.0 cum.**, e ativa `DEP-KMS` **1.1.0** e `DEP-ENG` **1.1.0**. **30 hashes**; **6 `H-P` projetados reproduzidos** |
| [**MSG-2026-0007**](../memory/operacional/MSG-2026-0007-ato-soberano-vigencia-do-framework-de-specifications.md) | OPR | M | **204** | **Fonte canonica unica do SETIMO ato soberano** — o maior do acervo em numero de objetos *(14)* e o primeiro que **cria** documento fundacional. Matriz integral de `H-A`, `H-N` e `H-P`, atomicidade, ordem, condicoes anteriores e posteriores, limites e rollback |
| [**MSG-2026-0008**](../memory/operacional/MSG-2026-0008-ato-soberano-emendas-e1-e-e3.md) | OPR | M | **236** | **Fonte canonica unica do OITAVO ato soberano**, e o **primeiro do acervo registrado ANTES da aplicacao**. Ancorado no `H-A` da minuta `PS-2026-015` **1.2.0**; **6** objetos alcancados, **3** excluidos com `E2` adiada, e os **2** `H-P` lidos do arquivo e reconferidos. **`0` transicoes aplicadas por este registro** |
| [**MSG-2026-0009**](../memory/operacional/MSG-2026-0009-ato-soberano-admissao-do-nxtrack.md) | OPR | M | **375** | **Fonte canonica unica do NONO ato soberano**, e o **segundo do acervo registrado ANTES da aplicacao**. Ratifica `ADR-0030`, aprova `RFC-0025` e **cria `PRO-nxtrack`**. Ancorado no `H-A` do pacote `PS-2026-016` **1.2.0** *(`e6fa26e8…44ae`, **medido e nao transcrito**)*, itens **I a VII**, linhas **185–328**, com o recorte hasheado e a faixa conferida linha a linha. **`5` de `5`** `H-A`, **`2` de `2`** `H-P` — o de `RFC-0025` pela **variante declarada** — e **`2` de `2`** `H-N`. **Grava `Q2` como artefato pela primeira vez.** **`0` transicoes aplicadas por este registro** |
| [**PT-2026-005**](relatorio-transicao-2026-07-29-aplicacao.md) | OPR | M | **430** | Aplicacao integral do sexto ato nas **quatro etapas obrigatorias**; **prova de consumo reexecutada sobre as fontes vigentes** — **55 de 55 celulas**; decisao **`GO-TO-SPECS` NAO AUTORIZADO** por **`RD-22`** |
| [**PT-2026-006**](relatorio-transicao-2026-07-29-fechamento-operacional.md) | OPR | M | **451** | **Fechamento operacional:** `RD-22` **fechado por refutacao de premissa**, `RD-26` **reconciliado** com metodo declarado e cobertura **100%**, **10 objetos rehasheados**, **55/55 com as cinco exigencias de §IX**; **8 de 8 condicoes**; decisao **`GO-TO-SPECS`** |
| [**PS-2026-009**](pacote-soberano-2026-07-29-fnd-11.md) | OPR | M | **446** | Pacote da emenda **C3 · Tipo 1** que cria **`FND-11`** e emenda `FND-01` e `FND-03`. **Setimo pacote soberano.** Publica **duas variantes** do candidato `FND-01` para a colisao com `RD-27`, mede a alternativa de `Q3` e **descobre `RD-43`**: gravar `superado_por` em `ADR` **altera o `H-N`** |
| [**PS-2026-010**](pacote-soberano-2026-07-29-rd-31.md) | OPR | M | **394** | Pacote da emenda **C2 · Tipo 2** das Cartas de `DEP-PRD` e `DEP-EXE` — fecha **`RD-31`** quanto as duas Cartas determinadas; abre **`RD-37`**. **Oitavo pacote soberano, e o primeiro cujo autor e DEP-EXE** |
| [**PT-2026-008**](relatorio-transicao-2026-07-29-canonizacao.md) | OPR | M | **334** | **Missao 1.13.1 — canonizacao e propagacao:** dois ritos completos, **6 candidatos medidos**, **`PILOTO-DEFERIDO` formalizado**, **7 achados novos**, **duas colisoes de norma declaradas com escolha submetida** e divida reconciliada em **6 categorias**; decisao **`READY-FOR-RATIFICATION`** |
| [**PS-2026-011**](pacote-soberano-2026-07-30-rd-27.md) | OPR | M | **376** | Pacote da emenda **C3 · Tipo 2** que fecha **`RD-27`** em `FND-01`, `FND-02` e `FND-10`. **Oitavo pacote soberano.** **Responde NAO** a pergunta se `V2` e byte a byte o cumulativo — e descobre **`RD-45`**. Publica a **`ALT`** medida para o acoplamento com `FND-11` |
| [**PS-2026-012**](pacote-soberano-2026-07-30-rd-37.md) | OPR | M | **319** | Pacote da emenda **C2 · Tipo 2** das Cartas de `DEP-OPS`, `DEP-GRW` e `DEP-TLS` — fecha **`RD-37`**. **Nono pacote soberano.** Traz a **prova de autoridade de `QG-1` sobre as nove Cartas**: **`0`** afirmacoes falsas, contra **11 em 4** |
| [**PS-2026-013**](pacote-soberano-2026-07-30-consolidado.md) | OPR | M | **343** | **Pacote consolidado — decimo, e o primeiro que nao submete objeto novo.** Matriz dos **14** objetos e **minuta unica**, com **sobreposicao de diff igual a `0`** e o **recalculo do custo de reversao de `ADR-0020`** *(**`RD-48`**)*. Projecao declarada `PJ-02` |
| [**PT-2026-009**](relatorio-transicao-2026-07-30-convergencia.md) | OPR | M | **187** | **Missao 1.13.2 — convergencia pre-ratificacao:** dois ritos novos, a coordenacao de `PS-2026-009` **2.0.0** e a consolidacao dos catorze objetos. **`0` objetos em vigor · `0` de 73 fontes normativas alteradas.** Decisao **`READY-FOR-RATIFICATION`** |
| [**PT-2026-010**](relatorio-transicao-2026-07-30-vigencia.md) | OPR | M | **166** | **Missao 1.13.3 — vigencia do Framework de Specifications:** relatorio **e parecer de aplicacao**. **14 objetos em vigor**, `H-P` **14/14**, `H-N` invariante **10/10**, `IR-09` **10/10**, `0` bytes fora dos diffs. Decisao **`SPEC-FRAMEWORK-IN-FORCE`** |
| [**PS-2026-014**](pacote-soberano-2026-07-31-medally.md) | OPR | M | **428** | **Pacote da admissao do medAlly — decimo primeiro pacote soberano, e o primeiro sobre origem externa.** **Dois** objetos com `H-A`/`H-N`/`H-P` medidos, `IR-09` **2 de 2**, instrumento validado em **10 de 10** **apos a calibracao reprovar a primeira versao**; revisao independente com **15** controles e **4** ressalvas; **5** questoes, **`Q1` bloqueante** |
| [**PT-2026-012**](relatorio-transicao-2026-07-31-manutencao-instrumentos.md) | OPR | M | **761** | **Missao 1.13.4.1 — manutencao dos instrumentos:** Item 0 fechado em **19 de 19** caminhos atribuidos a processo e horario, **`0`** escritores concorrentes no acervo; **`RD-53`** fechado por instrumento novo, com **`BL-2026-07-30-01` reproduzindo nos 64 digitos**; **`RD-56`**, **`RD-57`** e **`RD-58`** fechados; **`RD-49`** corrigido em tres candidatos medidos e **nao aplicados**; **tres minutas** preparadas e **`0`** aplicadas; autoverificacao medida pelos **dois** criterios *(`0` e `130`)*; **cinco** achados novos. **Item 0 REPROVA — 5 de 19 caminhos NAO ATRIBUIVEL.** Decisao **`BLOCKED`** |
| [**PS-2026-015**](pacote-soberano-2026-07-31-emendas-de-instrumento.md) | OPR | M | **405** | **Pacote das tres emendas de instrumento — decimo segundo pacote soberano.** Nove objetos em **tres unidades independentes**, dependencia **medida em `0`**. Minuta de ato **redigida e NAO emitida**, com decisao **item a item** |
| [**PS-2026-016**](pacote-soberano-2026-08-01-nxtrack.md) | OPR | M | **253** | **Pacote da admissao do nXtrack — decimo terceiro pacote soberano, e o segundo sobre origem externa.** **5** objetos hasheados, `H-P` publicado **so onde ha `O4`** — com a **diferenca de instrumento entre `ADR` e `RFC` declarada** —, diff literal de **duas** linhas de frontmatter, rollback objeto a objeto e **tres** questoes, das quais **so `Q2`** e condicao anterior de eficacia. Minuta **redigida e NAO emitida** |
| [**PT-2026-017**](relatorio-transicao-2026-08-02-primeira-spec.md) | OPR | M | **298** | **Missao 1.13.5 — a PRIMEIRA `Spec` do acervo.** Registra o rito `RFC-0026` → `ADR-0031` → `SPC-001` → `FIT-2026-024`, a reproducao de `LM-6(a)` *(`0` nos seis termos, em duas varreduras, com **controle positivo** aplicado antes de se acreditar em qualquer zero)* e, em **§6**, a **AVALIACAO DO FRAMEWORK no primeiro uso real** — gatilho de revisao de `FND-11 §15`, disparado: **22** regras exercidas sem ressalva, **4** com insuficiencia, **1** defeituosa *(`SF-10`)* e **5** nao exercidas, com o custo de `SF-09` **medido pela primeira vez** *(603 linhas, `2,23x` a mediana do acervo)*, fechando a obrigacao de medicao do limite `L2` |
| [**PS-2026-017**](pacote-soberano-2026-08-02-rd-91.md) | OPR | M | **276** | **Submete ao SOBERANO a emenda `C3` que sana `RD-91`.** **4** objetos com `H-A`, `H-N` e `H-P` publicados — `FND-09` 1.6.0, `FND-11` 1.1.0, Cartas `DEP-PRD` e `DEP-EXE` 1.2.0 —, **todos fora do acervo**. Diff **literal e reversivel** em §2; **`0` bytes escritos nos arquivos vivos**. §1.1 traz **os tres numeros de custo** com a natureza de cada um declarada: **5** medido · **2** derivado · **7** medido em precedente. Minuta do ato **redigida e NAO emitida**, com os quatro `H-P` como condicao de parada da aplicacao. **3** questoes ao Soberano — largura, `C0` e o conflito *versao MAIOR × `AL-01`* |
| [**PT-2026-018**](relatorio-transicao-2026-08-02-emenda-sf-10.md) | OPR | M | **182** | **Missao 1.13.5.1 — a emenda que sana `RD-91`, produzida e NAO aplicada.** Registra o Item 0 que **redirecionou a emenda da projecao para a fonte** *(a celula do achado reproduz duas fontes, palavra por palavra)* e a **varredura das 21 linhas** de `FND-09 §8.2`, que achou o mesmo colapso em **`PRJ`** e **`TPL`**. Classe determinada por **4** fundamentos citados, nunca por analogia. **5** achados novos, **`0`** fechados, **`0`** atos emitidos |
| [**PT-2026-016**](relatorio-transicao-2026-08-01-fechamento-rd-33.md) | OPR | M | **484** | **Missao 1.13.4.6 — o fechamento de `RD-33`, por rito MINISTERIAL determinado antes de exercido.** A causa caiu com `S1`, ja consumida; a reserva do item **VII** e de `LA-3` e **temporal e de sede, nunca de classe de rito**. Prova **por exercicio**: o `DoR` de `SF-23` reexercido, item **(9)** **PASSA**. **`0` atos emitidos, `0` fontes emendadas, `0` `Spec`s criadas, `0` bytes em `products/`.** O residuo **(b)** migra para **`RD-88`**; `RD-89` corrigido na projecao. Baseline **`BL-2026-08-01-03`** |
| [**PT-2026-015**](relatorio-transicao-2026-08-01-aplicacao-nxtrack.md) | OPR | M | **371** | **Missao 1.13.4.5 — aplicacao ministerial da admissao do nXtrack:** consome o **nono ato** na ordem de `PS-2026-016 §6.2`. `O4` em **`RFC-0025`** *(pela variante)* e em **`ADR-0030`**, com `H-P` **2 de 2** e `H-N` invariante **2 de 2**; **`PRO-nxtrack` criado** — `H-A` do aplicado `fca656a9…39e2`, distinto do `H-A` do candidato; `products` e `CLAUDE.md` **declarados no medidor** *(`OA-1`, `RD-81`)*; baseline **`BL-2026-08-01-02`** reproduzida em **2** execucoes. **`0` bytes** fora do conjunto autorizado, provado **arquivo a arquivo**; candidato **intacto** por objeto de commit. Achados novos **`RD-83`** a **`RD-87`** |
| [**PT-2026-014**](relatorio-transicao-2026-08-01-portao-nxtrack.md) | OPR | M | **292** | **Missao 1.13.4.4 — portao `ADR-0007` sobre o nXtrack:** **segunda** passagem pelo portao e a **primeira sob a norma emendada**. `G0` = `IDENTIDADE` · **`G1` FECHA** *(17 de 17 fontes atribuiveis; `0` sem commit em 183 rastreados; 758 no hospedeiro)* · `G2` com **12** linhas · **`G3` = `RECOGNIZE`** por fundamento citado · `G4` por `FIT-2026-023` · `G5` **preparado e nao consumido**. **7** limites do candidato medidos; **`0`** bytes admitidos; **5** achados novos. Decisao **`READY-FOR-RATIFICATION`** |
| [**PT-2026-013**](relatorio-transicao-2026-07-31-emendas-de-instrumento.md) | OPR | M | **203** | **Missao 1.13.4.2 — as tres emendas de instrumento:** rito completo, classes **determinadas** percorrendo as cinco hipoteses de `C3`, autoverificacao remedida em **`0` / `131`**. Decisao **`READY-FOR-RATIFICATION`** |
| [**PT-2026-011**](relatorio-transicao-2026-07-31-admissao-medally.md) | OPR | M | **283** | **Missao 1.13.4 — S1, a admissao canonica do medAlly:** primeiro exercicio do portao de `ADR-0007`, **`0`** bytes admitidos e **`0`** bytes escritos no candidato. **`0` Produtos em vigor**; `RD-33` **segue bloqueante**. **7** achados novos e **1** candidata a primeira `Spec`. Decisao **`READY-FOR-RATIFICATION`** |
| [**PT-2026-007**](relatorio-transicao-2026-07-29-specifications.md) | OPR | M | **468** | **Missao 1.13 — Framework de Specifications:** `SF-01` a `SF-32` instituidos com **0** fontes emendadas, **`RD-23` fechada com 5 defeitos onde o achado citava 2**, **12** casos de determinismo *(11 coerentes, 1 divergente que virou `RD-31`)*, **evidencia externa avaliada e nao adotada** *(0,70% lido, 0 formatos importados)*, **5 achados novos** e o registro de que **nenhuma Spec e criavel**; decisao **`ADJUST`**. **Primeiro relatorio de transicao cujo autor nao e DEP-GOV** |

> **Conferencia dos blocos de §4, RECONTADA POR FERRAMENTA nesta emissao** *(linhas de artefato
> por bloco, nao soma sobre o valor anterior)*: **11** + **57** + **33** + **19** + **32** +
> **12** + **53** = **217**. **A soma NAO iguala o total de §2, e a diferenca esta
> nomeada:** o acervo medido tem **218** arquivos, e o que falta e
> [`governance/roadmap-canonico.md`](roadmap-canonico.md) — achado **`RD-80`**, **ABERTO, e com o
> gatilho DISPARADO PELA SEGUNDA VEZ** em `BL-2026-08-01-03`. **`+1` em §4.7** *(`PT-2026-016`)*.
> **Declarar a diferenca e o que impede que ela volte a ser silenciosa**, que foi como `RD-42` e
> `RD-57` nasceram. **§4.3 passa a somar tres blocos** — 23 `CAP` + 9 `DEP` + **1 `PRO`** —, e a
> entidade `PRO` estreia. *(Esta linha estava DUAS emissoes atrasada quando)* declarava `10 + 47 + 32 + 19 + 26 + 11 + 40 = 185` contra
> `11 + 47 + 32 + 19 + 27 + 11 + 42 = 189` no vigente, e o `10` contradizia a **propria §4.1**,
> que lista **11** `FND` desde a vigencia de `FND-11`. Achado **`RD-57`**. **O cabecalho
> de §4 passa a ser derivado desta soma** — e foi por nao o ser que `RD-42` existiu. Somatorio verificado por ferramenta —
> o defeito **C12** da Missao 1.4 foi um header que nao fechava com a propria tabela, e **RE-04**
> da Missao 1.8 foi da mesma familia.
>
> **A verificacao que e mais forte que o somatorio, reexecutada — e ela pegou tres erros desta
> propria emissao.** Os alvos de link de §4 foram resolvidos **um a um contra o sistema de
> arquivos** e comparados a medicao de `wc -l`. **Resultado: 169 alvos existentes · 0 duplicados ·
> 0 orfaos**, e **3 divergencias de contagem de linha, todas introduzidas por esta missao**:
> `governance/README` *(205 → **206**)*, `governance/fitness/README` *(232 → **251**)* e
> `PT-2026-007` *(456 → **468**)*. **Corrigidas.**
>
> **A causa e a que a serie ja conhece, e vale registra-la contra a propria missao:** os tres
> valores foram escritos a partir de uma medicao **anterior a ultima rodada de edicoes**, e os
> tres arquivos cresceram depois — ao receber o razao de ressalvas, os agregados corrigidos e o
> tratamento de `RD-36`. **E `CV-04` outra vez, dentro do proprio ciclo que o estava corrigindo.**
> Na emissao anterior foram **4** divergencias, item 9 de `RD-28`; nesta, **3** — e a diferenca
> **nao e progresso**: e a mesma causa, apanhada **antes** de fechar, e nao na missao seguinte.
> **A licao operacional e de `MEM-APR-0006`: medir depois de TODAS as edicoes, e reconferir a
> conferencia.**
>
> **Os 5 artefatos criados na Missao 1.13.4, e as 3 tabelas onde cada um entra:** `ADR-0026` e
> `RFC-0021` em **§4.2**; `FIT-2026-019` em **§4.5**; `PS-2026-014` e `PT-2026-011` em **§4.7**.
> **A Carta candidata `PRO-medally` NAO entra em tabela alguma de §4**, porque **nao e artefato
> do acervo**: candidato nao tem ID de sequencia e nao ocupa entrada de catalogo (`FR-10`). Ela
> aparece **somente** em §9, como **candidato nomeado**.

### 4.8 Executavel — **1** artefato, entidade `SPC`

> **Subsecao NOVA, criada nesta emissao.** Ate 2026-08-01 a classe **Executavel** de §5 tinha
> **`1`** tipo com instancia — `Carta de Produto` nao pertence a ela —, e **`Spec` estava entre os
> sem instancia**. Com `SPC-001` a classe ganha o seu primeiro artefato de tipo `spec`, e §4
> passa a ter **oito** blocos. **Nenhum tipo, entidade ou classe foi criado:** `SPC` consta de
> [FND-09 `E-19`](../foundation/09-meta-model.md) desde a fundacao, com identidade
> `SPC-<NNN>-<slug>` em `products/<slug>/specs/` e **sequencia por produto**.

| Artefato | Tipo | Entidade | Perfil | Linhas | Resumo operacional |
|---|---|---|---|---|---|
| [**SPC-001**](../products/nxtrack/specs/SPC-001-governanca-de-dado-pessoal-do-nxtrack.md) **1.0.0** | Spec | `SPC` | S | **603** | **A PRIMEIRA `Spec` DO ACERVO.** Fixa o que o nXtrack precisa provar sobre o dado pessoal que ja guarda — inventario, atribuicao ao titular, exclusao, informacao antes da coleta e limite de saida — **antes de sair do loopback**. `C2 · Tipo 2`, `CAP-juridico`, custodiante DEP-QAR. **10** requisitos com os **6** campos de `SF-12` *(60 campos, `0` ausentes)*, **4 de 4** categorias de `SF-25`, **7 de 7** perfis de `SF-17`, **5 de 5** metodos de `SF-14`, **9 de 9** elos de `SF-20`, **21 de 21** blocos de `SF-09`, `DoR` **9/9** e `DoD` **10/10**. **`0`** requisitos afirmam enquadramento legal; **`0`** autorizam exposicao |

**Contador oficial da sequencia `SPC` — `SF-32`, `RG-04`:**

| Produto | Sequencia | Ultimo emitido | Proximo livre |
|---|---|---|---|
| **`PRO-nxtrack`** | por produto — `FND-09 E-19` | **`SPC-001`** | **`SPC-002`** |
| *(demais produtos)* | — | — | **`0` produtos alem de `PRO-nxtrack`** |

> **Criar `Spec` e incrementar o contador sao a MESMA mudanca** (`SF-32`, `CV-04`, `IX-02`) — a
> regra que `RD-32` mostrou nao estar sendo exercida, e que aqui **e exercida na origem**, e nao
> por correcao posterior. **`0` registros novos de `Spec` foram criados:** o contador vive neste
> catalogo, como `SF-32` determina, e criar um terceiro registro seria proliferacao (`RG-05`).

> **`products/` continua sem indice de diretorio.** `SPC-001` **nao** o exige: o indice do
> diretorio onde as `Spec`s vivem e **este catalogo** (`SF-32`). Achado **`RD-85`** segue
> **ABERTO**, com o enunciado **inalterado** — e o gatilho *"missao de catalogo, ou segunda
> admissao de Produto"* **nao disparou**, porque nenhuma das duas ocorreu.

## 5. Matriz de cobertura — tipo documental × instancia

| Classe | Tipos declarados | Com instancia | Sem instancia | Quais estao sem instancia |
|---|---|---|---|---|
| Normativa | **4** | **4** | **0** | — |
| Decisoria | 5 | **3** | **2** | Nota de Decisao · Excecao Formal |
| Constitutiva | 7 | **3** | **4** | Agente · Subagente · Projeto · Ferramenta |
| **Executavel** | 4 | **2** | **2** | Skill · Workflow |
| Avaliativa | 2 | **2** | **0** | — |
| **Cognitiva** | **10** | **4** | **6** | Memoria PRD · TEC · OPR · Handoff · Consulta · Alerta |
| Registro | 1 | **1** | **0** | — |
| **Total** | **33** | **19** | **14** | — |

**Conferencia:** 4+5+7+4+2+10+1 = **33** · 4+3+3+2+2+4+1 = **19** · 0+2+4+2+0+6+0 = **14** ·
14+19 = **33**. Os quatro somatorios fecham.

> **`Spec` sai de "sem instancia" em 2026-08-02, pela Missao 1.13.5.** `SPC-001`, em
> `products/nxtrack/specs/`, e a **primeira instancia** do tipo documental `Spec` e da entidade
> **`SPC`**. **Nenhum tipo e nenhuma entidade foram criados:** o tipo consta de
> [FND-10 §4.4](../foundation/10-artifact-framework.md) e a entidade de
> [FND-09 `E-19`](../foundation/09-meta-model.md) desde a fundacao — **33 e 21 permanecem**, e
> as **entidades instanciadas** passam de **11** para **12 de 21**.

> **`Produto` sai de "sem instancia" pelo NONO ato soberano, em 2026-08-01.** `PRO-nxtrack`, em
> `products/nxtrack/carta.md`, e a **primeira instancia** do tipo documental `Carta de Produto` e
> da entidade **`PRO`**. **Nenhum tipo e nenhuma entidade foram criados:** o tipo consta de
> [FND-10 §4.3](../foundation/10-artifact-framework.md) e a entidade de
> [FND-09 `E-17`](../foundation/09-meta-model.md) desde a fundacao — **33 e 21 permanecem**.
> **Restam 15 tipos sem instancia**, e a ausencia continua **determinada, nao ociosa**: `Spec`
> segue sem instancia por `RD-33`, que **o proprio ato reservou** a missao propria (item **VII**).

> ### IC-8 **fechado**, e duas divergencias novas corrigidas com ele
>
> **A pergunta era de merito, e a fonte ja a respondia.** Aplicando **CS-02**
> ([FND-10 §3.2](../foundation/10-artifact-framework.md)) — *"dois tipos documentais da mesma
> entidade diferem por **finalidade, conteudo permitido ou autoridade**"*:
>
> | Candidato | Diferem por que? | Veredito |
> |---|---|---|
> | **Memoria EST/PRD/TEC/OPR/APR** | **Autoridade** — escrita em EST **sempre exige ADR** (FND-06 §3.1, MI-04); OPR **expira por padrao**. **Conteudo permitido** — FND-06 §3 fixa conteudo distinto por camada | **CINCO** tipos |
> | **Diretiva/Consulta/Alerta** | **Finalidade** — *determinar* · *obter parecer* · *comunicar risco*, declaradas na propria linha de FND-10 §4.6 | **TRES** tipos |
> | ~~**Norma Derivada**~~ | **Recusada** em FND-10 §4.8, ao lado de Command, Prompt, Playbook, Checklist e Evaluation — **nenhum dos quais conta** | **NAO conta** |
>
> **Resultado: 33, identico a FND-10 §4. Nenhuma emenda a FND-10 foi necessaria e nenhuma
> entidade foi inventada.** A fonte sempre esteve certa; **esta projecao** errava em **dois**
> pontos que se mascaravam — contava **5** na Normativa *(incluindo a recusada)* e **9** na
> Cognitiva *(faltando um)*. Aplicacao literal de **RG-03** e **M3**: corrige-se a vista
> derivada, **nunca** a fonte.
>
> **Duas divergencias adicionais, encontradas ao fechar a soma:**
> **RE-04** — §2 declarava **16** tipos com instancia e esta secao declarava **17**: o mesmo
> documento divergia de si proprio. **Correto: 16.**
> **RE-05** — §2 declarava **11** entidades instanciadas e enumerava **10**. **Correto: 10**;
> `ORG` e `SOBERANO` **nao podem** ter instancia de artefato, por serem as duas unicas fora do
> arquetipo **A2**.
>
> **`Nota de Decisao` sai de com-instancia.** Ela e tipo documental de entidade `MEM (OPR)`
> (FND-10 §4.2) e **nunca teve instancia**: `MSG-2026-0001` e `MSG-2026-0002` sao **Diretivas**,
> entidade `MSG`. A contagem anterior de **4** na Decisoria a incluia por engano.
>
> **17 tipos sem instancia** — nao 18, como se registrava. **Doze** deles sao de componentes
> cuja criacao esta **expressamente proibida** nesta fase: ausencia **determinada**, nao
> ociosidade. EV-08 so alcanca tipo que atravesse **um horizonte inteiro** sem instancia, e
> **nenhum horizonte se fechou** — [REV-ESTRUTURAL-I §8.2](../foundation/revisao-estrutural-01-2026-07-28.md).

> **A Missao 1.6 instancia um tipo pela primeira vez.** `Carta de Departamento` sai de
> "sem instancia" e a entidade `DEP` passa a ter instancia. **Nenhum tipo e nenhuma entidade
> foram criados:** ambos ja constavam de FND-10 §4.3 e FND-09 §5.4 desde a fundacao —
> **33 e 21 permanecem**. Os demais artefatos novos instanciam tipos que ja tinham instancia.

> **A Missao 1.9 instancia um terceiro tipo pela primeira vez.** `Reporte` sai de "sem
> instancia": [PS-2026-002](pacote-soberano-2026-07-28-cartas.md) e o **pacote de decisao
> soberana**, canal `REPORTE` (FND-05 §2), entidade `MSG`. **Nenhum tipo e nenhuma entidade
> foram criados** — `Reporte` consta de FND-10 §4.6 desde a origem, e so nunca tivera
> instancia. **Restam 16 tipos sem instancia**, e **doze** deles sao de componentes cuja
> criacao esta expressamente proibida nesta fase: ausencia **determinada**, nao ociosidade.
>
> **A Missao 1.7 instancia outro tipo pela primeira vez.** `Diretiva` sai de "sem instancia" e a
> entidade **`MSG`** passa a ter instancia, com [MSG-2026-0001](../memory/operacional/MSG-2026-0001-ato-soberano-ratificacao-cartas-piloto.md).
> **Nenhum tipo e nenhuma entidade foram criados:** `Diretiva` consta de FND-10 §4.6 e `MSG` de
> FND-03 §3.13 e FND-09 §5 desde ADR-0003 — **33 e 21 permanecem**. As duas Cartas novas
> instanciam tipo que ja tinha instancia.

> **17 tipos sem instancia** e coerente com a fase: nenhum agente, produto, projeto, skill,
> workflow ou ferramenta foi criado — por determinacao. O gatilho EV-08 so se aplica a tipo
> que atravesse **um horizonte inteiro** sem instancia.

## 6. Rastreabilidade origem → estado → substituicao

| Artefato | Origem | Estado | Ratificacao | Substitui / substituido por |
|---|---|---|---|---|
| FND-01 a FND-07 | ADR-0001 | `ativo` | **ratificada** | — |
| FND-08 | RFC-0001 → ADR-0002 | `ativo` | **ratificada** | — |
| FND-09 | RFC-0002 → ADR-0003; emendado por ADR-0008 | `ativo` | **ratificada** | — |
| FND-10 | RFC-0004 → ADR-0006; emendado por ADR-0007 e ADR-0008 | **`ativo`** | **ratificada** | — |
| 23 Cartas `CAP` | ADR-0002 | `ativo` | herda ADR-0002 — **ratificada** | — |
| ADR-0005 | REV-META §4.6 | `ativo` | nao exigida | — |
| ADR-0007 | RFC-0005 | `ativo` | nao exigida *(C2/Tipo 2)* | — |
| ADR-0008 | R2 de FIT-2026-001 e de FIT-2026-002 | `ativo` | nao exigida *(C2/Tipo 2)* | — |
| RFC-0005 | Missao 1.4 | `aprovado` | n/a | — |
| INC-2026-001 | Determinacao do Soberano | `ativo` · **`fechado`** | n/a | — |
| MEM-APR-0001 | INC-2026-001 | `ativo` | n/a | — |
| MEM-APR-0002 | FIT-2026-002 §Aprendizado | `ativo` | n/a | — |
| MEM-APR-0003 | INC-2026-001 §11.4 | `ativo` | n/a | — |
| 19 Templates | ADR-0001; `TPL-fitness-check` por ADR-0004; ambos emendados por ADR-0008 | `ativo` | herda | — |
| 9 Avaliacoes | ADR-0004, ADR-0006, ADR-0007, ADR-0008, ADR-0009, ADR-0010 | `ativo` | nao exigida | — |
| 10 Indices | ADR-0001, ADR-0006 | `ativo` | nao exigida | — |
| FND-03 · FND-06 · FND-10 | emendados por **ADR-0009** e **ADR-0010** | `ativo` | **ratificada** *(herda ADR-0001/0006)* | — |
| RFC-0006 · RFC-0007 | Missao 1.5 | `aprovado` | n/a | — |
| ADR-0009 · ADR-0010 | RFC-0006 · RFC-0007 | `ativo` | nao exigida *(C2/Tipo 2)* | — |
| **MEM-EST-0001** | ADR-0010 | **`ativo`** | **ratificada** — [MSG-2026-0002](../memory/operacional/MSG-2026-0002-ato-soberano-cartas-comando-plataforma-e-contexto.md) | — |
| RFC-0008 | Missao 1.6 | `aprovado` | n/a | — |
| ADR-0011 | RFC-0008 | `ativo` | nao exigida *(C2/Tipo 2)* | — |
| `TPL-carta-departamento` · `capabilities/README` | emendados por **ADR-0011** | `ativo` | herda | — |
| **DEP-QAR** · **DEP-ENG** | ADR-0001 *(criacao do departamento)*; ADR-0011 *(contrato da Carta)* | **`ativo`** | **ratificada** — [MSG-2026-0001](../memory/operacional/MSG-2026-0001-ato-soberano-ratificacao-cartas-piloto.md) | — |
| FIT-2026-005 · REV-DEPARTAMENTO | ADR-0011 | `ativo` | nao exigida | — |
| MEM-APR-0004 | FIT-2026-005 | `ativo` | n/a | — |
| **MSG-2026-0001** | **Ato do SOBERANO**, 2026-07-28 | `ativo` | n/a — **e o proprio ato** | — |
| **DEP-EXE** · **DEP-KMS** | ADR-0001 *(criacao)*; ADR-0011 *(contrato)* | **`ativo`** | **ratificada** — [MSG-2026-0002](../memory/operacional/MSG-2026-0002-ato-soberano-cartas-comando-plataforma-e-contexto.md) | — |
| **RFC-0009** | Missao 1.8; achados IC-2 e G1/G2 | `aprovado` | n/a — **aceita em parte**; Q1 e Q2 **abertas** | — |
| **ADR-0012** | RFC-0009 | `ativo` | nao exigida *(C2/Tipo 2)* | — |
| **MSG-2026-0002** | **Ato do SOBERANO**, 2026-07-28 | `ativo` | n/a — **e o proprio ato** | — |
| **REV-ESTRUTURAL-I** · **FIT-2026-007** | **Determinacao do Soberano**; rito de FND-02 §9.4 | `ativo` | nao exigida | — |
| **INC-2026-002** | Auditoria da Missao 1.4 | `ativo` · **`fechado`** | n/a | — |
| `TPL-carta-departamento` | emendado por **ADR-0011**; **propagacao de M1 concluida** na Missao 1.7 | `ativo` | herda | — |
| FIT-2026-006 · REV-INTERCLASSES | ADR-0011 | `ativo` | nao exigida | — |

**Nenhum artefato `superado`, `revogado` ou `arquivado` nesta data.** A coluna existe porque
a cadeia precisa ser percorrivel desde ja (LN-08).

| **`DEP-QAR` 1.1.0** | Emenda por REV-ESTRUTURAL-I §7; ato soberano de 2026-07-28 | **`ativo`** | **ratificada** — [MSG-2026-0003 §2](../memory/operacional/MSG-2026-0003-ato-soberano-emenda-qar-e-criterio-de-consolidacao.md) | **substitui `DEP-QAR` 1.0.0**, preservada por hash e diff reversivel (§2.1 daquela Diretiva) |
| **`DEP-GOV` · `DEP-TLS` · `DEP-PRD` · `DEP-OPS` · `DEP-GRW`** | ADR-0001 *(criacao)* + ADR-0011 *(contrato)*; **ato soberano de 2026-07-29** | **`ativo`** | **ratificada** — [MSG-2026-0004 §2.1](../memory/operacional/MSG-2026-0004-ato-soberano-cartas-emenda-constitucional-e-regime-do-fitness-check.md) | `H-P` conferido contra valor **projetado antes do ato**; `IR-09` reproduz `H-A` nas cinco |
| **ADR-0013** | RFC-0010; ato soberano de 2026-07-28, item 2 | `ativo` | nao exigida *(C2/Tipo 2)* | — |
| **ADR-0014** | RFC-0011, Q1 | **`ativo`** | **ratificada** — [MSG-2026-0004 §2.2](../memory/operacional/MSG-2026-0004-ato-soberano-cartas-emenda-constitucional-e-regime-do-fitness-check.md) | **Promulga FND-01 1.4.0** e **fecha IC-2** |
| **RFC-0010** · **RFC-0011** | Missao 1.9 | `aprovado` | nao exigida | RFC-0010 **aceita**; RFC-0011 **aberta e escalada** |
| **MSG-2026-0003** · **PS-2026-002** · **IDX-departamentos** · **REV-ROLLOUT** · **FIT-2026-008** | Missao 1.9 | `ativo` | nao exigida | — |
| **PS-2026-003** · **PT-2026-001** · **FIT-2026-009** | Missao 1.10 | `ativo` | nao exigida | — |
| **`DEP-KMS` 1.1.0 · `DEP-ENG` 1.1.0** | Missao 1.10; achados RC-05 e RC-07 | **`candidato`** — **nenhum arquivo existe no acervo** | **MANTIDAS SEM RATIFICACAO** por determinacao expressa do ato de 2026-07-29 *(segundo)* | **Reemitidas** em [PS-2026-006](pacote-soberano-2026-07-29-kms-eng.md), com ID, versao, caminho, linhas, `H-A` integral, diff literal, versao substituida, revisao independente e **prova criptografica de identidade** — **8 verificacoes, 2 de 2 em todas** |
| **`DEP-QAR` 1.2.0** | Missao 1.10; achado RC-01 | **`ativo` · APLICADA** — `departments/qar/carta.md`, **388** linhas | **RATIFICADA** — [MSG-2026-0004 §3](../memory/operacional/MSG-2026-0004-ato-soberano-cartas-emenda-constitucional-e-regime-do-fitness-check.md); **aplicacao liberada** por [MSG-2026-0005 §1](../memory/operacional/MSG-2026-0005-ato-soberano-aplicacao-dep-qar.md) | `H-P` **`9b180b71…ad29`**; `H-N` **invariante**; **`IR-09` reproduz `H-A` byte a byte**. **`RC-01` FECHADO.** 1.1.0 preservada pelas **quatro vias** |
| **`ADR-0016`** · **`ADR-0017`** | Missao 1.11; achados RD-02 e RD-09 | **`ativo`** — **em vigor** | **RATIFICADAS** — [MSG-2026-0006 §2.1](../memory/operacional/MSG-2026-0006-ato-soberano-aplicacao-integral.md) | **`H-P` medido reproduz o projetado** de [PS-2026-004 §3.2](pacote-soberano-2026-07-29-rd-02.md) e [PS-2026-005 §3.1](pacote-soberano-2026-07-29-rd-09.md), nos 64 digitos. `IR-09` reproduz `H-A`; `H-N` **invariante** |
| **`ADR-0018`** · **`ADR-0019`** | Missao 1.12; achados RD-14 e RD-15 | **`ativo`** — **em vigor** | **RATIFICADAS** — [MSG-2026-0006 §2.1](../memory/operacional/MSG-2026-0006-ato-soberano-aplicacao-integral.md) | **`H-P` medido reproduz o projetado** de [PS-2026-007 §3.1](pacote-soberano-2026-07-29-rd-14.md) e [PS-2026-008 §3.1](pacote-soberano-2026-07-29-rd-15.md). `IR-09` reproduz `H-A`; **`H-N` invariante sob `O4` em 4 de 4** |
| **`ADR-0020`** | **RFC-0016**; achado **RD-22** | **`ativo`** — **em vigor** | **nao exigida** *(`C2 · Tipo 2` — FND-04 §2.1)* | — . **Nao emenda fonte alguma:** institui `PA-01` a `PA-14` **dentro do proprio ADR**, na forma de `ADR-0012` e `ADR-0015` |
| **`RFC-0016`** | Missao 1.12.1; achado **RD-22** | `aprovado` | n/a | **Acolhida** → `ADR-0020` |
| **`MEM-APR-0005`** | **PT-2026-005 §5.3** e **RFC-0016 §2.4** | `ativo` | n/a | — . `ocorrencias: 3` — `RD-22`, `RD-23` e `RD-26` |
| **`FIT-2026-014`** | Missao 1.12.1 | `ativo` | **—** *(`FT-10` — parecer nao se ratifica)* | — |
| **`PT-2026-006`** | §IX e §X de MSG-2026-0006 | `ativo` | nao exigida | — |
| **`FND-02` 1.3.0 · `FND-09` 1.4.0 · `FND-10` 1.3.0** | Missao 1.11 | **`candidato`** — **nenhum arquivo existe no acervo** | **PENDENTE** | Vivem como **diff literal + `H-A` + `H-N`** em PS-2026-004 §2 e PS-2026-005 §2 |
| **`FND-01` 1.5.0 · `FND-09` 1.4.0 · `FND-10` 1.3.0** | Missao 1.12 | **`candidato`** — **nenhum arquivo existe no acervo** | **PENDENTE** | Vivem como **diff literal + `H-A` + `H-N`** em [PS-2026-007 §2](pacote-soberano-2026-07-29-rd-14.md) e [PS-2026-008 §2](pacote-soberano-2026-07-29-rd-15.md). ⚠️ **Os candidatos de FND-09 e FND-10 concorrem com os da Missao 1.11** — achado **RD-19**. **Nenhuma fundacional foi emendada em nenhuma das duas missoes** |
| **RFC-0012** · **RFC-0013** · **PS-2026-004** · **PS-2026-005** · **PS-2026-006** · **MSG-2026-0005** · **PT-2026-002** · **FIT-2026-011** | Missao 1.11 | `ativo` | nao exigida | **FIT-2026-011 com aprovacao escalada ao SOBERANO** — cascata de `DEP-EXE I-2` no terminus |
| **RFC-0014** · **RFC-0015** · **PS-2026-007** · **PS-2026-008** · **PT-2026-003** · **FIT-2026-012** | Missao 1.12 | `ativo` | nao exigida | **Nenhum ato foi consumido nesta missao** — a pre-condicao de aplicacao **nao foi satisfeita** ([PT-2026-003 §1](relatorio-transicao-2026-07-29-fechamento-normativo.md)). **FIT-2026-012 com aprovacao escalada ao SOBERANO** |
| **PT-2026-004** · **FIT-2026-013** | Continuacao da Missao 1.12 | `ativo` | nao exigida | **Nenhum ato consumido.** Os **12 objetos** das cinco cadeias foram **verificados sem falha**, e os **candidatos cumulativos** de FND-09 **1.5.0** e FND-10 **1.4.0** vivem **fora do acervo**, com caminho declarado em [PT-2026-004 §4](relatorio-transicao-2026-07-29-ratificacao.md) |
| **FND-01 1.4.0** | **ADR-0014**, ratificado | **`ativo`** | **ratificada** — ato de 2026-07-29 | **Fecha IC-2.** Oito alteracoes; **zero** titulares |
| **ADR-0015** · **MSG-2026-0004** | Missao 1.10; **item 4** do ato de 2026-07-29 | `ativo` | nao exigida *(`FT-10`)* | ADR-0015 **responde Q2** |

**Dois artefatos passam a aguardar ato: `ADR-0016` e `ADR-0017`.** A fila de retidos zerou no
ato de 2026-07-29 e **volta a dois** — desta vez **por producao propria da missao**, e nao por
defeito de forma do ato. **Os dois nasceram `em-revisao`, e nenhum afirma vigencia no proprio
texto** — a licao de **RD-08**, aplicada.

> **O que continua fora de vigor nao esta retido por ausencia de ato, e a distincao importa.**
> `DEP-KMS` 1.1.0 e `DEP-ENG` 1.1.0 sao **candidatas com identificador invalido no ato**
> *(marcador de 40 caracteres no lugar do SHA-256 — achado **RD-07**)*; `DEP-QAR` 1.2.0 esta
> **ratificada e nao aplicada**, por determinacao posterior do proprio Soberano. **As tres nao
> sao artefatos do acervo** — nao tem arquivo, e por isso **nao entram na contagem de 137**.

> **A distincao mudou de lado nesta missao, e por isso esta reescrita.** Na Missao 1.8, o que
> dependia do Soberano **retinha correcao**, nao vigencia. Agora **retem vigencia**: as cinco
> Cartas existem, estao validadas e **nao vigoram** (LM-02). **A emenda `DEP-QAR` 1.1.0 e a
> pendencia PS-1 foram ambas resolvidas** pelo ato de 2026-07-28; **Q1 e Q2 continuam retendo
> correcao**, com o texto pronto em [RFC-0011](../rfcs/RFC-0011-emenda-constitucional-ratifica-homologa.md).
> Tudo reunido em [PS-2026-002](pacote-soberano-2026-07-28-cartas.md).

> **As duas Cartas piloto da Missao 1.6 deixaram de estar retidas.** `DEP-QAR` e `DEP-ENG`
> passaram a **`ativo`** pela operacao **O4** (FND-10 §5.2), com a condicao de validade de
> **LM-02** satisfeita — ato explicito, datado e sobre o texto final, com integridade verificada
> por tres vias independentes. **E a segunda aplicacao completa da regra** que o Artifact
> Framework instituiu; a primeira foi a propria entrada em vigor de FND-10.

> **Fonte do estado de ratificacao:** [INC-2026-001 §11](incidents/INC-2026-001-ratificacao-inferida.md).
> Esta coluna e projecao (PJ-02); em divergencia, prevalece a fonte (PJ-03). O frontmatter dos
> ADRs permanece congelado no ato de aprovacao e **nao** e fonte corrente (PJ-04).

## 7. Achados desta classificacao

| # | Achado | Acao |
|---|---|---|
| 1 | **10 artefatos** — 8 indices e 2 revisoes — estavam sem tipo declarado antes desta missao | Resolvido: `IDX` e `REV` registrados sem criar entidade |
| 2 | `foundation/` abriga 3 revisoes arquiteturais alem dos 10 FND e dos templates | Aceito: revisao vive ao lado do que revisa (FND-03 §7) |
| 3 | Nenhuma Carta de Capability declara `perfil_contexto` | Aceito: valor padrao por tipo (`S`), aplicado por referencia — zero migracao |
| 4 | `memory/` tem 6 indices e **1** registro real | Coerente com a fase; a camada APR foi a primeira a receber conteudo |
| 5 | O acervo cresceu **18,7%** na Missao 1.3 — de 15.939 para 18.916 linhas | Registrado como ressalva R1 em [FIT-2026-002](fitness/FIT-2026-002-artifact-framework.md) |
| 6 | O acervo cresceu **12,7%** na Missao 1.4 — de 18.916 para 21.318 linhas, com 8 artefatos novos | Avaliado em [FIT-2026-003](fitness/FIT-2026-003-consolidacao-baseline.md) §F1 |
| 7 | Duas ressalvas abertas desde missoes anteriores foram **fechadas** (R2 de FIT-2026-001 e R2 de FIT-2026-002) | Executado por [ADR-0008](../decisions/ADR-0008-uma-fonte-multiplas-projecoes.md) §5.3 |
| 8 | O acervo cresceu **11,4%** na Missao 1.5 — de 21.318 para **23.742** linhas, com 7 artefatos novos. **Quarto ciclo consecutivo de crescimento** | Avaliado em [FIT-2026-004](fitness/FIT-2026-004-conhecimento-do-soberano.md) §F1; ressalva **R3** |
| 9 | Os tres registros `MEM-APR` estavam classificados na classe **Decisoria**, contrariando FND-10 §4.6 | **Corrigido nesta emissao** — §4.2 e §4.7. Achado **D7** de [REV-SOBERANO](../foundation/revisao-arquitetural-conhecimento-do-soberano-2026-07-28.md) |
| 10 | **Cinco** artefatos passaram a declarar os cinco campos do contrato, por serem emendados — nenhum por retroatividade | [ADR-0009](../decisions/ADR-0009-o-que-conta-como-emenda-de-artefato.md), AC-08. Restam **63** sem os campos, atendidos por L2 |
| 11 | O acervo cresceu **11,6%** na Missao 1.6 — de 23.742 para **26.506** linhas, com 7 artefatos novos. **Quinto ciclo consecutivo de crescimento**, e nenhum artefato foi fundido, aposentado ou dividido em nenhum deles | Avaliado em [FIT-2026-005](fitness/FIT-2026-005-cartas-de-departamento.md) §F1; ressalva **R3** |
| 12 | **`MEM-APR-0002` declarava 2 ocorrencias com 5 documentadas.** As ocorrencias 3, 4 e 5 foram registradas em REV-CONSOLIDACAO, REV-SOBERANO e REV-DEPARTAMENTO e nunca chegaram ao registro-fonte | **Corrigido nesta missao** — registro em **1.1.0**, `ocorrencias: 5`. Defeito de propagacao (CV-04); achado **DR-8** de REV-DEPARTAMENTO |
| 13 | **Dois artefatos ficam retidos em `em-revisao`** por dependerem de ato do Soberano — as duas Cartas piloto | **Resolvido na Missao 1.7** pelo ato de 2026-07-28: ambas em `ativo`, `ratificada`. Ressalva **R4** de FIT-2026-005 **fechada** |
| 14 | O acervo cresceu **9,3%** na Missao 1.7 — de 26.506 para **28.966** linhas, com **5** artefatos novos. **Sexto ciclo consecutivo de crescimento** | Avaliado em [FIT-2026-006 §F1](fitness/FIT-2026-006-validacao-interclasses.md); ressalva **R3**. **Diferente dos cinco anteriores, a proposta de consolidacao EV-08 foi aberta** — a primeira do sistema |
| 15 | **A correcao M1 foi declarada aplicada em REV-DEPARTAMENTO §3.7 e nunca chegou ao template.** Duas Cartas foram escritas sob checklist que se acreditava corrigido | **Corrigido na Missao 1.7** — `TPL-carta-departamento` **1.2.0**, com a conferencia cruzada **B4 × B9**. Achado **IC-1** de REV-INTERCLASSES. Quarta ocorrencia da familia de `MEM-APR-0002` |
| 16 | **§5 declarava `Memoria EST` sem instancia**, embora MEM-EST-0001 conste de §4.7 **deste mesmo catalogo**; e a linha Cognitiva soma **10** tipos declarando **9** | ✅ **Integralmente corrigido na Missao 1.8** — §5. `Memoria <camada>` sao **cinco** tipos e `Diretiva/Consulta/Alerta` sao **tres**, por **CS-02**; `Norma Derivada` **nao conta**, por ser recusada. Total **33**, identico a FND-10 §4 — **sem emendar FND-10**. Achado **IC-8**, **fechado** |
| 17 | O acervo cresceu **6,8%** na Missao 1.8 — de 28.966 para **30.947** linhas, com **5** artefatos novos. **Setimo ciclo consecutivo de crescimento** | Avaliado em [FIT-2026-007 §F1](fitness/FIT-2026-007-revisao-estrutural-i.md); ressalvas **R2** e **R3**. **EV-08 encerrada como `AJUSTAR`, com zero artefatos consolidados** — escalado ao Soberano em **PS-1** |
| 18 | **§2 declarava 16 tipos com instancia e §5 declarava 17** — o mesmo documento divergindo de si proprio. E **`Nota de Decisao`** era contada como instanciada, embora nunca tenha tido instancia | ✅ **Corrigido** — §5. Correto: **16 com instancia · 17 sem**. Achado **RE-04** de [REV-ESTRUTURAL-I](../foundation/revisao-estrutural-01-2026-07-28.md) |
| 19 | **§2 declarava 11 entidades instanciadas e enumerava 10.** `ORG` e `SOBERANO` nao podem ter instancia de artefato — sao as duas unicas fora do arquetipo **A2** (FND-09 §4.2) | ✅ **Corrigido** — §2. Achado **RE-05**. **E o unico exercicio discriminante de A2 registrado no acervo**, e por isso **fechou a ressalva R3 de FIT-2026-001** |
| 20 | **Tres divergencias do catalogo contra a fonte foram corrigidas na Missao 1.8, e nenhuma fonte foi alterada** — IC-8, RE-04 e RE-05 | Aplicacao literal de **M3** e **RG-03**. **E a evidencia que fechou R3 de FIT-2026-002**: a classe M3 tem um unico membro, e **uso decisivo** |
| 21 | O acervo cresceu **15,4%** na Missao 1.9 — de 30.947 para **35.701** linhas, com **14** artefatos novos. **Oitavo ciclo consecutivo de crescimento**, e o **maior acrescimo absoluto da serie** | Avaliado em [FIT-2026-008 §F1](fitness/FIT-2026-008-rollout-das-cartas.md); ressalva **R2**. **`HZ-01` de [ADR-0013](../decisions/ADR-0013-criterio-de-horizonte-e-consolidacao.md) retira a leitura de que crescer e falha — e nao retira o fato** |
| 22 | **As contagens de linha de §4.6 e §4.7 divergiam da fonte em oito indices**, por nao terem sido remedidas apos as missoes 1.7 e 1.8 | ✅ **Corrigido nesta emissao** — remedidas por ferramenta, **zero fontes alteradas** (RG-03, M3). Sexta ocorrencia da familia de [MEM-APR-0002](../memory/aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md) |
| 23 | **Tres achados desta missao estao em Cartas ja ratificadas e nao podem ser corrigidos sem ato novo** — **RC-01** *(`DEP-QAR` declara 386 linhas, tem 387)*, **RC-05** *(`DEP-KMS` nao trata incidente)* e **RC-07** *(`DEP-ENG` nao declara impedimento sobre a propria Carta)* | Declarados em [REV-ROLLOUT §7](../foundation/revisao-arquitetural-rollout-cartas-2026-07-28.md); ressalva **R4** de FIT-2026-008. **Segunda vez que a imutabilidade por ratificacao retem defeito conhecido** — a primeira foi IC-5, **agora corrigido**. **Missao 1.10:** as tres ganham **emenda candidata** com diff literal e hash em [PS-2026-003](pacote-soberano-2026-07-29-emendas.md) — **reclassificadas, nao fechadas** |
| 24 | O acervo cresceu **5,8%** na Missao 1.10 — de 35.701 para **37.766** linhas, com **6** artefatos novos, em **duas** mudancas: **+3,3%** na verificacao *(3 artefatos)* e **+2,4%** na aplicacao do ato *(3 artefatos)*. **Decimo ciclo consecutivo de crescimento** | Avaliado em [FIT-2026-009 §F1](fitness/FIT-2026-009-ativacao-e-endurecimento.md) e [FIT-2026-010 §F1](fitness/FIT-2026-010-aplicacao-do-ato-soberano.md); ressalvas **R4** e **R2**. **Nenhuma Carta teve linha de corpo alterada em toda a missao** — as cinco ativadas mudaram **dois campos de frontmatter** cada, e as tres emendas seguem fora do acervo |
| 25 | **`governance/README` declarava a baseline `BL-…-05`, 117 artefatos e 30.947 linhas — uma baseline atras da fonte desde o encerramento da Missao 1.9 — e 14 ressalvas abertas onde `fitness/README` contava 15** | ✅ **Corrigido na Missao 1.10**, **na projecao**; zero fontes alteradas (RG-03, PJ-03, M3). Achado **RD-04**. **Setima ocorrencia** da familia de [MEM-APR-0002](../memory/aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md) |
| 26 | **Tres achados novos que nenhuma verificacao anterior alcancava** — **RD-01** *(citacao inexata de FND-02 §4 em `DEP-PRD`)*, **RD-02** *(ambiguidade de veto Guarda × Plataforma na propria FND-02 §4)* e **RD-03** *(`DEP-KMS` declara entregar a sete; a linha tem seis)* | Produzidos pela verificacao das **treze dimensoes** em [`departments/README §2.2`](../departments/README.md). **RD-02 nao e defeito de Carta: e da fonte fundacional**, e e o **unico achado aberto que toca autoridade** |
| 27 | **Este catalogo divergia de si proprio em dois lugares:** o `resumo` do frontmatter declarava *"os 117 artefatos do acervo"* e **§9** declarava **112** `native`, enquanto **§10.0** declarava **131**. Os tres numeros sao do **mesmo arquivo**, e correspondem a **tres missoes diferentes** — 1.8, 1.7 e 1.9 | ✅ **Corrigido na Missao 1.10**, nos dois lugares. Achado **RD-06**. **Mesmo mecanismo do achado 18** *(§2 dizia 16, §5 dizia 17)*: o campo que resume nao foi remedido quando a secao que ele resume mudou (CV-04). **Terceira ocorrencia de o catalogo divergir de si proprio** — as anteriores foram **IC-8** e **RE-04** |
| 28 | **O ato soberano de 2026-07-29 enumerou 6 de 8 objetos corretamente e trouxe marcador de 40 caracteres no lugar do SHA-256 integral em dois deles** — `DEP-KMS` 1.1.0 e `DEP-ENG` 1.1.0 | **Nenhuma Carta ativada por esses dois itens; nenhum candidato alterado; nenhum incidente aberto.** A fonte canonica foi conferida hash a hash: **0** valores com comprimento diferente de 64 em [PS-2026-003](pacote-soberano-2026-07-29-emendas.md). Achado **RD-07**, **segunda ocorrencia da familia de RD-05**. Identificadores reemitidos e reconferidos byte a byte |
| 29 | **`FND-10 §10.3` e `FND-09 §8.2` continuam declarando *"Ratifica: SOBERANO se C3"* para `Fitness Check`, e a regra vigente passou a ser `FT-10`, que diz o contrario** | Achado **RD-09**, dono DEP-GOV, gatilho *"proximo ato soberano que alcance FND-09 ou FND-10"*. **Nao corrigido de proposito:** emendar `FND` exige ato do Soberano, e o de 2026-07-29 **nao as menciona**. [ADR-0015 §5.3](../decisions/ADR-0015-fitness-check-e-parecer-nao-decisao.md) |
| 37 | **Este catalogo estava DUAS MISSOES desatualizado em §4:** o cabecalho declarava *"117 de 117"*, as tabelas somavam **131** linhas de artefato para **137** artefatos em disco, e **seis** artefatos — `ADR-0015`, `FIT-2026-009`, `FIT-2026-010`, `PS-2026-003`, `PT-2026-001` e `MSG-2026-0004` — **nunca foram acrescentados** | ✅ **Corrigido nesta missao, na projecao**; **zero fontes alteradas** (RG-03, PJ-03, M3). Achado **RD-16**. **Quarta ocorrencia de o catalogo divergir de si proprio** — as anteriores foram **IC-8**, **RE-04** e **RD-06** —, e a **oitava** da familia de [MEM-APR-0002](../memory/aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md). **A causa e sempre a mesma: o campo que resume nao e remedido quando a secao que ele resume muda** (CV-04) |
| 36 | **Para Spec `C2` ou `C3`, `FND-09 §8.2` *(aprova DEP-PRD, ratifica `—`)* e `FND-04 §2` *(aprova DEP-EXE/SOBERANO, ratifica SOBERANO)* dao respostas diferentes** | Achado **RD-15**, **severidade Alta**, dono DEP-GOV, gatilho *"antes da primeira Spec C2"*. A regra de precedencia de FND-09 §8.2 **resolve** a favor de FND-04, e a **segunda metade dela — registrar o conflito como erro desta tabela — nunca fora cumprida**: o registro foi feito em [PT-2026-002 §4.2](relatorio-transicao-2026-07-29-fechamento.md). **As fontes tambem nao distinguem *aprovar o artefato* de *liberar o portao*** |
| 35 | **`QG-1` e liberado por `DEP-PRD`, que produz a Spec**, contra a regra literal de **FND-01 §6.2** — *"portao nao pode ser liberado por quem produziu o artefato"* | Achado **RD-14**, **severidade Alta**, dono DEP-GOV, gatilho *"antes da primeira Spec"*. `DEP-PRD §5.2` reconhece o fato e `RP-1` declara o **risco**; **nenhum dos dois nomeia a colisao normativa**, e `governance/exceptions/` tem **0** excecoes. **Encontrado pela simulacao de consumo, e nao pelas 117 verificacoes de contrato** |
| 34 | **O historico de versoes de `FND-10` esta fora de ordem** — `1.1.0` figura depois de `1.2.0` | Achado **RD-13**, severidade Baixa, dono DEP-GOV, gatilho *"proxima emenda a FND-10"*. **Nao corrigido:** o texto esta **dentro de `H-N`** de fundacional ratificada (IR-01) |
| 33 | **`FND-04 §2.1` nao distingue artefato de decisao de parecer** — e a regra que **gerou** o texto que RD-09 corrige | Achado **RD-12**, severidade Media, dono DEP-GOV, gatilho *"proxima emenda a FND-04"*. **Declarado em vez de corrigido:** emendar FND-04 **nao foi pedido nem ratificado** (LM-03). Aplicacao literal da licao de FIT-2026-010 sobre **fechar colisao sem varrer o mecanismo** |
| 32 | **Quatro celulas do candidato `FND-02` 1.3.0 declaram mais do que a Carta do proprio emissor** — `EXE→KMS`, `GOV→EXE`, `QAR→EXE` e `QAR→KMS` | Achado **RD-11**, severidade Baixa, dono DEP-EXE, gatilho *"proxima emenda a `DEP-EXE`, `DEP-GOV` e `DEP-QAR`"*. **Residuo de propagacao** (CV-04); as tres Cartas estao **em vigor** |
| 31 | **`DEP-TLS §6.3` declara *"sem interacao estrutural direta"* com `DEP-PRD` e `DEP-GRW` e diz que o pedido de capacidade chega *"por DEP-ENG ou DEP-EXE"*; `DEP-PRD §6.3` e `DEP-GRW §6.3` declaram consulta direta, e a fonte declara `C` nos dois casos** | Achado **RD-10**, severidade Media, dono DEP-EXE, gatilho *"proxima emenda a `DEP-TLS`"*. **Duas Cartas em vigor descrevem caminhos operacionais incompativeis.** A causa e a mesma de **RD-01**: leitura **relacional** de tabela **direcional** — determinada em [RFC-0012 §4](../rfcs/RFC-0012-semantica-da-matriz-de-interacao.md), P1 |
| 30 | **`ADR-0014` esta `ativo` e o proprio texto abre com *"⛔ ESTE ADR NAO ESTA EM VIGOR"*** | O bloco esta **dentro de `H-N`**: corrigi-lo seria alteracao **nao ratificada** (IR-01, IR-05). A fonte corrente do estado e o **frontmatter** (FND-10 §5.4). Achado **RD-08**, dono DEP-GOV, gatilho *"proxima emenda a ADR-0014"*. **Mesmo mecanismo de RC-01** — texto ratificado que a propria ratificacao tornou desatualizado |
| 38 | **A baseline `BL-2026-07-29-04` nao reproduzia pelo comando que ela propria publica:** o comando de §10.2 excluia apenas `./.obsidian/*`, e o repositorio contem tambem `_SAIDA-COMPANY-OS/` — **4 arquivos, 1.123 linhas** —, que **nao e acervo**. Executado como publicado, dava **151 artefatos e 41.552 linhas** | ✅ **Corrigido nesta missao, na projecao**, em `BL-2026-07-29-05`; **`BL-2026-07-29-04` NAO foi editada** (BL-02) — nova medicao recebe **novo identificador**. Achado **RD-17**, severidade **Media**. A baseline **e valida**; o que falhava era a **instrucao de reproduzi-la**, e **BL-03** declara nula a baseline sem evidencia reproduzivel. **O conteudo de `_SAIDA-COMPANY-OS/` nao foi lido — apenas contado** |
| 39 | **`FND-04 §6`, linha *Spec*, atribui classe `C1` a criacao de uma Spec, e `FND-04 §2` atribui a classe **pelo efeito**.** Era a **terceira fonte de RD-15**, e **nunca entrara na conta** | Achado **RD-18**, severidade **Media**, dono DEP-GOV, gatilho *"proxima emenda a FND-04"*. As duas convivem por **AL-01** e **FND-01 §7.1.6**, mas o texto **nao declara qual prevalece**. [ADR-0019](../decisions/ADR-0019-aprovador-e-ratificador-de-spec.md) **remete a §2** e deixa §6 como **piso**, sem emenda-lo. **Segunda ocorrencia da licao *o achado registrado pode ser menor que o defeito*** — a primeira foi RD-02 |
| 40 | **[PS-2026-005](pacote-soberano-2026-07-29-rd-09.md) e [PS-2026-008](pacote-soberano-2026-07-29-rd-15.md) emendam os mesmos dois documentos** — FND-09 §8.2 e FND-10 §10.3 — **em celulas e pontos de insercao disjuntos**, e **reivindicam os mesmos numeros de versao** | Achado **RD-19**, severidade **Media**, dono DEP-GOV, gatilho *"promulgacao do primeiro dos dois pacotes"*. **Nenhum byte e disputado.** Resolvido por `O1`–`O4` de [PS-2026-008 §5](pacote-soberano-2026-07-29-rd-15.md): **versao e atribuida na promulgacao**, e o segundo a ser ratificado e **reemitido rebaseado**. ⚠️ **CARACTERIZACAO CORRIGIDA na continuacao da Missao 1.12** — [PT-2026-004 §5](relatorio-transicao-2026-07-29-ratificacao.md). A afirmacao *"candidatos sao publicados sem arquivo"* era **falsa**: os **seis** candidatos **existem em disco e reproduzem os `H-A` publicados**. O defeito real e que **o pacote nao declara o caminho do arquivo que mede**. **A lacuna do cumulativo FECHOU com evidencia**: FND-09 **1.5.0** e FND-10 **1.4.0** foram **construidos, medidos e preservados**, com ordem explicita |
| 41 | **As contagens de linha de §4 divergiam da fonte em 18 de 153 artefatos declarados**, e **14 dessas divergencias sao anteriores a esta missao** — entre elas **`FND-01`** *(declarava 468, tem 475)*, **`IDX-departamentos`** *(declarava 256, tem 317)* e o **`README` da raiz** *(declarava 272, tem 287)* | ✅ **Corrigido nesta missao, na projecao** — remedidas **uma a uma por ferramenta**, **zero fontes alteradas** (RG-03, PJ-03, M3). Achado **RD-20**, severidade **Baixa**. **Quinta ocorrencia de o catalogo divergir de si proprio** — as anteriores foram **IC-8**, **RE-04**, **RD-06** e **RD-16** —, e a **nona** da familia de [MEM-APR-0002](../memory/aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md). **A causa e sempre a mesma** (CV-04), e a novidade e o metodo: **a reconciliacao passou a ser executada artefato a artefato, e nao por amostragem** |
| 42 | **A reemissao rebaseada de `PS-2026-008` e devida e nao foi executada.** A minuta de §7 do pacote enumera o candidato **nao cumulativo** de FND-09 e FND-10, valido **apenas** se PS-2026-008 for ratificado **sem** PS-2026-005 | Achado **RD-21**, severidade **Media**, dono **DEP-GOV**, gatilho *"primeira missao sem a vedacao de produzir minuta, ou ato que alcance os dois pacotes"*. **Mitigado, nao suprido:** os identificadores cumulativos estao publicados e medidos em [PT-2026-004 §4](relatorio-transicao-2026-07-29-ratificacao.md). **A vedacao e da propria missao**, e por isso o achado nasce **declarado**, nao por omissao |
| 43 | **Nenhuma fonte do acervo declara titular para *promulgacao* ou *ativacao*.** Os **cinco verbos de autoridade** de FND-09 §8.1 sao *Criar, Alterar, Aprovar, Consumir, Aposentar*; a palavra *"promulg"* aparece **3 vezes** em toda a camada normativa, **as tres em prosa de ADR**; `FND-10 §5.2` `O4` declara **operacao, transicao, criterio e rollback**, nao o ator; e `FND-10 §5.4` declara a **condicao** de entrada em `ativo`, nao o ator | Achado **RD-22**, severidade **Alta**, dono **DEP-GOV**, gatilho *"antes de nova tentativa de GO-TO-SPECS"*. **Bloqueia a condicao 6 de §X do ato de 2026-07-29**: as 55 celulas respondem, mas **2 das 10 titularidades** que §IX manda identificar *"sem interpretacao informal"* nao estao declaradas. **`AU-09` determina que autoridade nao declarada em §8.2 nao existe.** **Contra-leitura declarada** em [PT-2026-005 §5.3](relatorio-transicao-2026-07-29-aplicacao.md): promulgar e ativar seriam **execucao de `O4`** sob a autoridade de quem aprova ou ratifica — **defensavel, e ela mesma interpretacao**. ✅ **FECHADO na Missao 1.12.1, por REFUTACAO DE PREMISSA — nao por emenda, nao por ato.** A varredura media o **termo** *"promulg"* e a matriz de **autoridade**; o titular estava declarado na **funcao**, no documento de **ciclo**: **`FND-04 §4 [7]`** — *"REGISTRO: **DEP-GOV** atribui ID definitivo, **publica**, atualiza indices"* — e **`FND-07 §5 [10]`**, com **`FND-07 §5 [13]`** *(`VIGENCIA`)* sendo a **unica das catorze etapas sem ator**, porque vigencia e **efeito**. **`AU-09` nao os alcanca:** `FND-09 §8.1` fecha os verbos de autoridade em **cinco**, e execucao nao e autoridade — a regra que responde e **`AU-06`**. **20 declaracoes em 5 fontes vigentes**, inventariadas em [RFC-0016 §2.3](../rfcs/RFC-0016-regime-ministerial-de-promulgacao-e-ativacao.md). Instrumento efetivo: **[ADR-0020](../decisions/ADR-0020-regime-ministerial-de-promulgacao-e-ativacao.md), `C2 · Tipo 2`** — o **menor competente** —, com **0 fontes emendadas**, **0 titulares criados** e **0 atos exigidos**. Causa registrada em [MEM-APR-0005](../memory/aprendizado/MEM-APR-0005-medir-a-ausencia-na-fonte-errada.md) |
| 44 | **`TPL-spec` fixa `autor: DEP-PRD` e `aprovador: DEP-PRD` e nao tem campo `ratificacao`** — o que **contradiz `ADR-0019`** desde o instante em que ele passou a vigorar: aprovacao segue a **classe** e a ratificacao e do **SOBERANO** se C3 ou Tipo 1 | Achado **RD-23**, severidade **Alta**, dono **DEP-GOV**, gatilho *"antes de qualquer Spec ser criada"*. **NAO corrigido:** o ato de 2026-07-29 exclui `TPL-spec` **expressamente** (§VIII). Causa da omissao: a medicao do *"conjunto estreito"* em [PT-2026-004 §3.1](relatorio-transicao-2026-07-29-ratificacao.md) procurou **afirmacao em prosa** e nao **valor em frontmatter de template**, e por isso achou **1** artefato em vez de **2** |
| 45 | **§10.2 declara, para `BL-2026-07-29-06`, *155 artefatos / 42.785 linhas* — que sao os valores de `BL-05` — enquanto o comando que a propria linha publica devolve *157 / 43.498*** | Achado **RD-24**, severidade **Media**, dono DEP-GOV. **Reproduzido por ferramenta antes de qualquer edicao desta aplicacao:** **157 · 43.498 · `f9859941…3fba`** — **a impressao digital reproduz; o que divergia era a contagem ao lado dela**. **NAO corrigido, por duas razoes independentes:** o ato exclui o catalogo mestre (§VIII) e **`BL-02` proibe editar baseline**. Atendido por **nova medicao com novo identificador**: `BL-2026-07-29-07`, §10.4. **Setima ocorrencia** de o catalogo divergir de si proprio |
| 46 | **§4.3 divergia da fonte em 13 valores:** cinco Cartas declaradas **`em-revisao` · `pendente`** quando estao em vigor desde [MSG-2026-0004](../memory/operacional/MSG-2026-0004-ato-soberano-cartas-emenda-constitucional-e-regime-do-fitness-check.md) *(10 valores)*, `DEP-QAR` em **1.1.0 · 387** quando esta em **1.2.0 · 388** *(2)* e o subtotal declarado **3.918** *(1)*. **11 dos 13 sao anteriores a esta aplicacao**, o mais antigo com **tres missoes de atraso**. §4.7 declarava ainda **17** registros onde a tabela tem **21**; e o **`README` da raiz** *(`IDX-raiz`)* declarava **`BL-2026-07-28-06`**, **117 artefatos** e **4 Cartas em vigor** — **quatro missoes de atraso** | Achado **RD-25**, severidade **Media**, dono DEP-GOV. ✅ **CORRIGIDO na projecao**, valor a valor, **medido por ferramenta**, **zero fontes alteradas** (`PJ-03`, `RG-03`) — mesmo metodo de **RD-20**. **Oitava ocorrencia** da familia, e **decima segunda** de [MEM-APR-0002](../memory/aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md). **A causa e sempre `CV-04`:** a projecao nao e atualizada pela mesma mudanca que altera a fonte |
| 47 | **A distribuicao por perfil de contexto de §2.1 nao e reproduzivel a partir das fontes:** **61 de 159 artefatos nao declaram `perfil_contexto` no frontmatter** — **as 24 Cartas de Capability**, **23 arquivos de `foundation/`** *(Templates inclusos)*, 5 de `decisions/`, 4 de `memory/`, 3 de `rfcs/` e 2 de `governance/`. Os valores de §2.1 derivam da **coluna de perfil de §4**, e o **metodo nao esta declarado na propria secao** | Achado **RD-26**, severidade **Media**, dono **DEP-GOV**, gatilho *"proxima emenda a §2.1 ou a FND-10 §6"*. **§2.1 ficou DECLARADAMENTE NAO RECONCILIADA** nesta aplicacao: recalcular por metodo diferente do original produziria numero novo **sem base para dizer qual esta certo**, e afirma-lo seria **LV-05**. **Afeta as afirmacoes `CE-01` e `CE-02`** — *"medido, nao estimado"* — que dependem de uma medicao cuja base **nao existe no frontmatter**. **Nao e defeito de acervo:** e **campo obrigatorio ausente** onde FND-10 o exige, ou secao que projeta sem declarar metodo. ✅ **RECONCILIADO na Missao 1.12.1 — e nenhuma das duas hipoteses era a certa.** A norma tem uma **terceira** resposta, literal: **`FND-10 §2.3` PRESCREVE o metodo** — *"padrao por tipo (§10.3), **aplicado por referencia no catalogo**"* — e declara **migracao de custo zero**, com a obrigacao nascendo so da **emenda posterior a vigencia** (`AC-08`), isenta em `CORRECAO` e em `M3` derivado (`AC-09`) e inaplicavel a `M1` (`AC-10`). Auditoria dos **159**: **98 declaram** · **2 sao nao conformes** *(`FND-01`, `FND-02` — achado 48)* · **58 sao anteriores a vigencia** · **1 isento por `AC-09`**. **Cobertura 100% · 0 nao classificados · 0 preenchimentos por inferencia.** §2.1 passa a reproduzir **o total do acervo**, que e a prova de que a particao nao tem dupla contagem nem omissao. [PT-2026-006 §3](relatorio-transicao-2026-07-29-fechamento-operacional.md) |

| 48 | **`FND-01` 1.5.0 e `FND-02` 1.3.0 foram emendadas em 2026-07-29 — apos a vigencia de FND-10 — sem os cinco campos que `AC-08` passou a exigir no instante da emenda.** `FND-01` declara so `ratificacao`; `FND-02`, **nenhum** dos cinco. Alem disso, **`FND-10 §8.5`** declara o custo do nucleo em `FND-01` **468** · `FND-03` **619** · total **1.087**, contra **485** · **631** · **1.116** medidos | Achado **RD-27**, severidade **Media**, dono **DEP-GOV**, gatilho *"proximo ato soberano que alcance FND-01, FND-02 ou FND-10"*. **NAO corrigido, e a razao e criptografica:** **`IR-03` e lista fechada** e **nao** inclui `resumo`, `perfil_contexto`, `confidencialidade` nem `revisor` — todos **entram em `H-N`**. Acrescenta-los alteraria o `H-N` de **dois documentos promulgados pelo sexto ato**, e **`IR-05`** determina que divergencia de `H-N` apos o ato e **alteracao nao ratificada**, *"nao corrigivel por edicao: exige ato novo"*. **Atenuante real, e nao e cumprimento:** os cinco campos tem **valor padrao declarado** em FND-10 §2.2, e por isso **nenhum consumidor e induzido a erro**. **`AC-06` esta descumprido por dois documentos de nivel 2 da hierarquia normativa** — ressalva **`R2`** de [FIT-2026-014](fitness/FIT-2026-014-regime-ministerial-e-cobertura-de-contexto.md). **Primeira vez que `AC-08` foi CONTADO** |
| 49 | **O catalogo e o indice de `governance/` divergiam da fonte, ou de si proprios, em 10 valores** — `resumo` do frontmatter *(155)*, §Escopo *(117)*, §2.1 *(cobria 105 de 159 sem declarar parcialidade)*, §2.2 *(a lista dos cinco maiores omitia **este catalogo** e `REV-interclasses`, e declarava o maior artefato novo como **sexto** quando e o **decimo**)*, §3 *(`FND-01` **468**, total **1.099**)*, §4.4 *(subtotal **2.952** contra **2.958** somados na propria tabela)* e §4.6/§4.7 *(linhas de **4** indices)*; e **[`governance/README`](README.md)** declarava **`BL-2026-07-29-06` · 157 · 43.498** — **uma baseline atras da fonte** — e **13** `FIT` emitidos. **9 dos 10 sao anteriores a esta missao** | Achado **RD-28**, severidade **Media**, dono DEP-GOV. ✅ **CORRIGIDO na projecao**, valor a valor, **medido por ferramenta**, **zero fontes alteradas** (`PJ-03`, `RG-03`). **Nona ocorrencia** de o catalogo divergir de si proprio — IC-8, RE-04, RD-06, RD-16, RD-17, RD-20, RD-24, RD-25 e esta. **O que ha de novo:** os itens de §2.2 e §4.4 **nao sao divergencia projecao × fonte** — sao a **fonte derivada nao conferindo contra si mesma** *(soma que nao fecha, ordinal que nao corresponde a ordenacao)*, que e exatamente o risco **`RG-2`** da [Carta de DEP-GOV](../departments/gov/carta.md). **A mitigacao — *"somar as tabelas da fonte, nao apenas compara-las com a projecao"* — estava escrita desde a Missao 1.9 e nunca havia sido exercida. Exercida uma vez, produziu 2 achados** |
| 50 | **[`memory/operacional/README`](../memory/operacional/README.md) declarava `atualizado_em: 2026-07-28` enquanto ja listava `MSG-2026-0006`, de 2026-07-29** — atualizacao derivada aplicada sem registrar a data | Achado **RD-29**, severidade **Baixa**, dono DEP-GOV. ✅ **CORRIGIDO** como **`C0` editorial** — `atualizado_em` + incremento de **CORRECAO** para **`1.2.1`** (FND-04 §2). **`AC-09` isenta** a obrigacao dos cinco campos, porque a mudanca e derivada de `M3` e nao emenda |
| 51 | **§10.4 declara *"1.965 links relativos verificados"* sem declarar o metodo de contagem.** Uma segunda implementacao mede **2.121** sobre um acervo cuja impressao digital reproduz identica | Achado **RD-30**, severidade **Baixa**, dono DEP-GOV, gatilho *"proxima baseline"*. **Metrica sem metodo declarado nao e reproduzivel por terceiro**, contra **`CE-04`** e **`BL-03`**. ✅ **ATENDIDO em `BL-2026-07-29-08`**, que **declara o metodo** em §10.5. **§10.4 NAO foi editada** — `BL-02`: baseline nunca e editada, e nova medicao recebe **novo identificador**. **ABERTO quanto ao registro historico de `BL-07`** |
| 52 | **A Carta de [`DEP-PRD`](../departments/prd/carta.md) 1.0.0 — `ativo`, `ratificada` — contem 8 afirmacoes que `ADR-0018` e `ADR-0019` tornaram FALSAS**: `§3 P-8`, `§5` L135 e L136, `§5.2` L159 e L162, `§7` L211, `§10.1 RP-1` e `§12.3` L382. Ela reivindica **`QG-1`** como portao proprio e cita, como fundamento, um texto de `FND-09 §8.2` **que nao existe mais**. E **`DEP-EXE` — o titular real desde `ADR-0018` — nao declara `QG-1` em nenhuma linha da propria Carta: `0` ocorrencias, medido** | Achado **`RD-31`**, severidade **Alta**, dono **DEP-EXE** *(propoe — `FND-09 §8.2` linha `DEP`)*, revisa **DEP-GOV**, aprova e ratifica **SOBERANO**, gatilho *"antes da primeira Spec"*. **Consequencia verificavel: o portao da Spec nao tem titular declarado em Carta alguma** — quem resolve pelas Cartas obtem `DEP-PRD`, quem resolve pela fonte obtem `DEP-EXE`. E o caso **`T-12`** de [ADR-0021 §9](../decisions/ADR-0021-framework-de-specifications.md). **NAO corrigivel aqui:** emendar Carta ratificada exige **ato**. **Atenuante real, e nao e cumprimento:** `LV-03` continua valendo — liberacao por quem produziu e **nula**, independentemente do que a Carta diga. **[PT-2026-004 §3.1](relatorio-transicao-2026-07-29-ratificacao.md) mediu o *"conjunto estreito"* e enumerou 4; esta medicao encontra 8** — a causa e a mesma de `RD-23`: procurou-se **a frase que ficaria falsa**, nao **o papel que mudou de titular**. Ressalva **`R3`** de [FIT-2026-015](fitness/FIT-2026-015-framework-de-specifications.md) |
| 53 | **Quatro contadores oficiais de sequencia declaravam um numero A MENOS do que a propria tabela abaixo deles lista:** `ADR` **`0019`/`0020`** com `ADR-0020` existente · `RFC` **`0015`/`0016`** com `RFC-0016` existente · `FIT` **`013`/`014`** com `FIT-2026-014` existente, **em `fitness/README` E em `governance/README`**. **4 tabelas · 8 valores** | Achado **`RD-32`**, severidade **Media**, dono **DEP-GOV**. **O risco nao e cosmetico: quem confiasse no contador criaria `ADR-0020`, que ja existe** — colisao de identificador, contra `FND-03 §2.3`, *"numero nunca e reaproveitado"*. **O que foi varrido, declarado:** **9 sequencias em 7 indices** — `ADR`, `RFC`, `FIT` *(×2)*, `EXC`, `INC`, `MEM-APR`, `MEM-EST`, `MSG` —, **4 defasadas e 5 corretas**; o defeito **nao e sistemico**, e das sequencias movimentadas pelas Missoes 1.12 e 1.12.1. **SEGUNDA OCORRENCIA:** [`governance/README`](README.md) documenta a primeira em nota propria — `FIT` *"um numero atras do real desde a Missao 1.3"*, fechada como `C11` de REV-CONSOLIDACAO —, e **a correcao anterior atingiu o valor e nao o gatilho `CV-04`**. **CORRIGIDO nos quatro**, valor a valor; **0 fontes normativas alteradas** (`RG-03`, `PJ-03`, `M3`). **E a causa foi codificada em regra: `SF-32`** de ADR-0021 — *criar artefato de sequencia e incrementar o contador sao a mesma mudanca*. **Encontrado por EXERCER o contador**, ao pedir o numero de `ADR-0021`: **ler o indice nao revelaria, porque a tabela estava certa** — [MEM-APR-0006](../memory/aprendizado/MEM-APR-0006-exercer-o-contador-revela-o-defeito.md) `V1` |
| 54 | **A `Spec` esta vinculada a `Produto` em TRES fontes vigentes** — `FND-04 §6` linha *Spec* *(pre-condicao **"Produto existe"**, e *"todas precisam ser verdadeiras"*)*, `FND-03 §3.6` *("vive em `products/<slug>/specs/`")* e `FND-10 §4.4` *(mesmo local)* — **e medem-se `0` artefatos de tipo `spec`, `0` de produto e `products/` ausente das 8 entradas da raiz.** `KP-3` da Carta de `DEP-PRD` declara, na fonte, *"`0` — **proibido nesta fase, por determinacao**"* | Achado **`RD-33`**, severidade **Alta**, dono **SOBERANO** *(decide)*, instrui **DEP-PRD**, gatilho **imediato**. **E a UNICA pendencia bloqueante do acervo:** `GO-TO-SPECS` esta liberado e **nao pode ser exercido**. **Nao e defeito de acervo — e norma funcionando**, mais uma **lacuna de cobertura**: nao existe categoria de Spec sobre materia **interdepartamental**, que a Missao 1.13 pediu. **Duas saidas, disjuntas, ambas do SOBERANO:** **`S1`** — ato que crie o primeiro Produto *(`C2 · Tipo 1`, `FND-04 §6`)*, que habilita a Spec **de produto**; **`S2`** — `RFC C3 → ADR C3 → ato` ampliando a `Spec` a materia nao-produto, que habilita a **interdepartamental**. **`S1` nao habilita `S2` e vice-versa**, e cada piloto pedido depende de uma delas. **As duas Specs piloto NAO foram criadas**, e as duas saidas faceis — escrever em outro diretorio *(`MT-01`, `FND-03 §7.1`)* ou criar `products/` *(`LV-06`, `LV-07`)* — **foram recusadas com norma citada**. [ADR-0021 §7.3](../decisions/ADR-0021-framework-de-specifications.md) · [PT-2026-007 §6](relatorio-transicao-2026-07-29-specifications.md). **Encontrado por rodar o `DoR` contra o artefato que ainda nao existia** — `V3` de MEM-APR-0006. ✅ **FECHADO em 2026-08-01, pela Missao 1.13.4.6, por rito MINISTERIAL — e o fechamento e PARCIAL POR CONSTRUCAO, com o residuo nomeado.** **A causa da parte (a) foi removida por `S1`**, o nono ato (item **III**), **ja emitido e ja consumido** — nao faltava autoridade, faltava registro. **Rito, com a norma citada:** `PA-01` *(execucao da autoridade **ja exercida**)*, `PA-03` *(promulgar e a etapa `[7]` de `FND-04 §4`; titular **DEP-GOV**; consiste em **atualizar indices**)*, `PA-07` *(executor e o custodiante declarado)* e **`PA-13`** *(**o SOBERANO nao e executor ministerial** e **nenhuma regra o poe a atualizar catalogo**)* de [ADR-0020](../decisions/ADR-0020-regime-ministerial-de-promulgacao-e-ativacao.md); **`AU-06`**; `FND-04 §4 [7]`; `RG-01`, `RG-03`, `RG-04` e `AC-09` de `FND-10`. **A reserva do item VII e de `LA-3` foi lida LITERALMENTE: e TEMPORAL e DE SEDE, nunca de classe de rito** — *ato*, *ratificacao*, *`C3`* e *`1.13.5`* tem **`0`** ocorrencias nela, e [`MSG-2026-0009 §8`](../memory/operacional/MSG-2026-0009-ato-soberano-admissao-do-nxtrack.md) declara a sequencia *"**`RD-33` destravado → 1.13.5**"*, pondo o destravamento **antes** da missao da `Spec`. **A leitura divergente de [PT-2026-015 §10](relatorio-transicao-2026-08-01-aplicacao-nxtrack.md) e do roadmap — *"fecha na 1.13.5"* — foi DECLARADA e nao silenciada**, e **nenhum dos dois foi editado**: um e historico (`LV-04`), o outro nao tem autoridade. **`READY-FOR-RATIFICATION` foi construida e descartada com prova:** as tres hipoteses de conteudo do ato sao **repeticao** *(`S1` ja declarada)*, **incompetencia pela forma** *(`PA-13`)* ou **`S2`, ja deferida**. **Prova por EXERCICIO, jamais por leitura** — o mesmo metodo que abriu o achado: o `DoR` de `SF-23` foi reexercido e o item **(9)** **PASSA**; item (4) em **5 de 5** `Capabilities` ativas. **`0` bytes nas tres fontes:** o vinculo `Spec` × `Produto` **nao foi removido nem afrouxado — foi SATISFEITO**. **O que NAO fechou:** a parte **(b)**, a categoria de `Spec` sobre materia **nao-produto**, que `S1` **nao alcanca por construcao** — **migra para `RD-88`**. [PT-2026-016](relatorio-transicao-2026-08-01-fechamento-rd-33.md) |
| 55 | **Os 19 `TPL` declaram `aprovador: SOBERANO` no proprio cabecalho — 19 de 19 —, enquanto `FND-09 §8.2` linha `TPL` da `Aprova: DEP-GOV` e `FND-10 §10.3` linha *Template* da `Aprova: DEP-GOV` · `Ratifica: —`** | Achado **`RD-34`**, severidade **Baixa**, dono **DEP-GOV**, gatilho *"proxima emenda que alcance os `TPL`"*. **Leitura alternativa declarada, e ela e plausivel:** o campo pode registrar **fato historico** — os templates foram acolhidos pelo ato que adotou a Fundacao — e nao afirmacao de norma. **NAO corrigido, e a razao e metodologica: corrigir um dos 19 criaria divergencia entre iguais**, e corrigir os dezenove e outra materia com rito proprio. **Encontrado por extrair o frontmatter da familia inteira**, e **a extracao barrou a correcao parcial** — `V4` de MEM-APR-0006. Pergunta `Q4` de [RFC-0017 §9](../rfcs/RFC-0017-framework-de-specifications.md), aberta |
| 56 | **Tres agregados de indice divergiam da fonte:** *(a)* [`memory/README`](../memory/README.md) dava a camada **`APR`** autoridade **`5`** — **o mesmo valor de `OPR`** —, e `FND-06 §2` da **`4`**; *(b)* o mesmo indice declarava **`3`** registros `OPR` enumerando `MSG-0001` a `MSG-0003`, quando `memory/operacional/` contem **`6`**; *(c)* o [`README` da raiz](../README.md) anunciava **seis artefatos aguardando decisao do Soberano**, quando a fila **zerou** no sexto ato | Achado **`RD-35`**, severidade **Media**, dono **DEP-GOV**, gatilho imediato. **O item (a) tornava `MM-03` INDETERMINADO** — *"vence o de numero menor"* nao decide entre dois cincos —, e o proprio `aprendizado/README` sempre declarou **`4`**. O item (b) estava **tres missoes atrasado**, e `MSG-2026-0006` e o **sexto ato soberano**, cuja aplicacao sustenta a baseline vigente. O item *(c)* e o [`README` da raiz](../README.md), cujo bloco `📋` **declarava *"seis artefatos aguardam decisao do Soberano"*** quando o catalogo §2 — **fonte** — declara **`0` retidos** desde o sexto ato: **quatro missoes de atraso**. **CORRIGIDO na projecao**, item a item; **0 fontes alteradas** (`PJ-03`, `RG-03`, `M3`). **A enumeracao de `OPR` foi substituida por remissao a fonte** (`PJ-01`), para nao envelhecer outra vez — **correcao de causa, nao de valor**. **Decima primeira ocorrencia** da familia de [MEM-APR-0002](../memory/aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md); causa `CV-04`. **Segunda vez que a mitigacao `RG-2` — somar o agregado contra a propria linha — e exercida, e a segunda vez que produz achado** |
| 57 | **`RD-23` FECHADA, e maior do que estava declarada.** O achado citava **dois** defeitos em `TPL-spec` — `aprovador: DEP-PRD` fixo e ausencia de `ratificacao`. A medicao campo a campo contra `FND-10 §2.2` e `FND-09 §8.2` encontrou **cinco**: os dois citados, mais a ausencia de `resumo`, `perfil_contexto`, `confidencialidade` e `revisor`; mais §11 declarando *"Liberado por `DEP-PRD`"* contra `FND-01 §6.2` pos-`ADR-0018`; mais §Responsaveis sem revisor, contra `AC-03` | **RESOLVIDO na fonte** por [ADR-0021 §5.11](../decisions/ADR-0021-framework-de-specifications.md), rito **C2**, aprovado por **DEP-GOV** *(`FND-09 §8.2` linha `TPL`)*. `TPL-spec` **1.0.0 → 1.1.0**: `cabaa58e…f748` · **132** linhas → `afd0dc7e…370f` · **272** linhas, **`LF` preservado em `0` bytes `CR`**, diff **literal e reversivel** em §5.12. **A autoridade passou a ser DERIVADA, nao fixada** — a exigencia literal da pre-correcao: `aprovador: <derivado da classe — FND-04 §2>`, com `SF-10` fazendo-a depender de classe do efeito *(piso `C1`)*, tipo, materia e Departamento custodiante. **`DEP-PRD` deixa de ser aprovador universal e a ratificacao aparece quando `C3` ou `Tipo 1`.** **Terceira ocorrencia da licao *o achado registrado pode ser menor que o defeito*** — as anteriores foram `RD-02` e `RD-18` |
| 59 | **O razao de ressalvas nao fecha, e a divergencia e maior do que a que a missao foi corrigir.** Medido por ferramenta: [`governance/fitness/README`](fitness/README.md) tem **31 linhas** e **28 ressalvas distintas** na tabela de abertas *(tres aparecem duas vezes, como reclassificacao — `FIT-2026-011 R1`, `FIT-2026-011 R2` e `FIT-2026-012 R1`)* e **18** na de fechadas; os **15 arquivos `FIT`** contem **55** linhas de ressalva, das quais **5** sao reclassificacoes embutidas; e [`governance/README`](README.md) declarava **`28` abertas · `19` de `46` emitidas**. **Nenhum dos conjuntos reconcilia com os outros.** Alem disso, **as 2 ressalvas de `FIT-2026-014` estavam ausentes do razao desde a missao anterior** | Achado **`RD-36`**, severidade **Media**, dono **DEP-QAR** *(fonte — `fitness/README`)* e **DEP-GOV** *(projecao — `governance/README`)*, gatilho **proxima auditoria de ressalvas**. **PARCIALMENTE tratado, e o limite esta declarado:** ✅ a **cascata devida foi executada** — as **2** ressalvas de `FIT-2026-014` e as **3** de `FIT-2026-015` entraram no razao (`CV-04`); ✅ os agregados de `governance/README` foram **substituidos pelos valores medidos**, com a nao reconciliacao **dita com esse nome**. ❌ **A reconciliacao completa NAO foi executada:** exigiria classificar as **55** linhas uma a uma entre **aberta**, **fechada**, **reclassificada** e **absorvida** — auditoria propria, fora do escopo da Missao 1.13. **O caminho errado era arredondar:** a hipotese inicial foi que o defeito era uma divergencia de **um** *(`46` contra `47`)*, e **medir na fonte mostrou que nao era** — corrigir o `46` para `47` teria produzido um numero **igualmente indefensavel**, e por isso **nao foi feito**. `LV-05` e `CE-04`: nao se declara reconciliado o que nao foi reconciliado |
| 67 | **O indice [`decisions/README`](../decisions/README.md) terminava em `ADR-0020`: `ADR-0021` nunca recebeu linha na tabela de decisoes**, embora tenha sido criado na Missao 1.13 e o **contador** tenha sido corrigido **na mesma missao** | Achado **`RD-44`**, severidade **Media**, dono **DEP-GOV**, gatilho imediato. ✅ **CORRIGIDO nesta emissao** *(a linha de `ADR-0021` foi acrescentada, com o registro da superacao parcial)*. **A ironia e o dado:** a Missao 1.13 **corrigiu o contador de `ADR` e esqueceu a tabela do mesmo arquivo**, na propria missao em que **codificou a causa em `SF-32`** — *criar artefato de sequencia e incrementar o contador sao a mesma mudanca*. **Terceira ocorrencia da familia `RD-32`**, e a **primeira em campo diferente do contador**; a licao operacional e que **`SF-32` fala de contador e o defeito migrou para a tabela ao lado** |
| 60 | **Tres Cartas ratificadas declaram literalmente que `QG-1` e liberado por `DEP-PRD`**, e nenhuma delas foi enumerada por `RD-31`: [`DEP-OPS §5.2`](../departments/ops/carta.md), [`DEP-GRW §5.2`](../departments/grw/carta.md) e [`DEP-TLS §5.2`](../departments/tls/carta.md) — as tres reproduzem a frase *"os sete portoes de FND-01 §6.2 sao liberados por DEP-EXE (QG-0), **DEP-PRD (QG-1)**, ..."*. **O defeito de `RD-31` estava em 4 Cartas, nao em 2: 11 afirmacoes falsas no total** | Achado **`RD-37`**, severidade **Media**, dono **DEP-EXE** *(propoe)*, revisa **DEP-GOV**, aprova e ratifica **SOBERANO**, gatilho *"proximo ato que alcance `DEP-OPS`, `DEP-GRW` ou `DEP-TLS`"*. **NAO corrigido, e o motivo e escopo determinado — nao impossibilidade normativa:** a Missao 1.13.1 determinou *"as duas Cartas"*. **Custo publicado: 1 linha por Carta** — [PS-2026-010 §5](pacote-soberano-2026-07-29-rd-31.md). **A causa e a mesma familia de `RD-23` e `RD-31`:** mediu-se a Carta de **quem perdeu** e a de **quem ganhou** a autoridade, e nao a **projecao da tabela de portoes**, que tres Cartas reproduzem justamente por **nao liberarem portao nenhum**. **O acervo passa de 11 afirmacoes falsas em 4 Cartas para 3 em 3** — melhora medida, **nao fechamento**. Ressalva **`R2`** de [FIT-2026-016](fitness/FIT-2026-016-canonizacao-e-propagacao.md) |
| 61 | **`FND-01 §11`, verbete `Fundacao`, declara *"o conjunto dos **nove** documentos fundacionais (FND-01 a **FND-09**)"*** — e **`FND-10` e fundacional desde `ADR-0006`**, incorporada ao nivel 2 da hierarquia por `FND-01` **1.3.0**. O verbete esta defasado **desde a propria emenda que criou a defasagem** | Achado **`RD-38`**, severidade **Baixa**, dono **DEP-GOV**, gatilho *"ato que alcance `FND-01`"*. ✅ **CORRIGIDO no candidato `FND-01` 1.6.0** — de **nove/FND-09** para **onze/FND-11** —, e **depende de ato**. **A causa e `CV-04` dentro do proprio glossario:** `ADR-0006` acrescentou `FND-10` ao **§10** e ao rodape de *Documentos derivados*, e **nao ao §11** |
| 62 | **A autoria de instrumento normativo volta a DEP-GOV, e isso e regressao medida.** `ADR-0021` foi o **primeiro** instrumento normativo do acervo cujo autor **nao** e DEP-GOV — a resposta material a `RC-02` registrada em `FIT-2026-015`. **Promover a norma a `FND` devolve a autoria a DEP-GOV**, porque `FND-09 §8.2`, linha `FND`, nomeia **um unico** proponente | Achado **`RD-39`**, severidade **Baixa**, familia **`RC-02`**, **oitava ocorrencia**, dono **DEP-GOV**, gatilho *"primeira Carta ou `FND` escrito apos a existencia de agentes"*. **DECLARADO, NAO RESOLVIDO.** **Determinado pela matriz, nao por conveniencia** — mesma familia de **`IC-3`**. Mitigacao real e insuficiente: **`DEP-PRD` e consulta obrigatoria** em toda emenda de `FND-11`, **`DEP-QAR` revisa**, e **o merito das 32 regras nao e escrito por DEP-GOV — e recebido**, com a equivalencia provada por `diff` |
| 63 | **`ADR-0021` nao declara a propria superacao parcial.** Quem o ler **sem o indice** nao descobrira que a sede da norma mudou, e aplicara `SF-*` a partir dele | Achado **`RD-40`**, severidade **Baixa**, dono **DEP-GOV**, gatilho *"primeira emenda a `FND-11`"*. **DECLARADO, NAO RESOLVIDO.** **O efeito e nulo em 31 das 32 regras**, porque o merito e identico; **em `SF-32` a leitura sera errada** — o ADR dira *"nao se emenda"* onde `FND-11` dira *"emenda-se com ato"*. A sucessao esta legivel em **quatro** lugares permanentes: `ADR-0022 supera:`, `FND-11 §15`, [`decisions/README`](../decisions/README.md) e **§6 deste catalogo**. **A alternativa foi medida e tem preco:** ver item **66**. Ressalva **`R1`** de [FIT-2026-016](fitness/FIT-2026-016-canonizacao-e-propagacao.md) |
| 64 | **A Carta de [`DEP-PRD §7`](../departments/prd/carta.md) aloja a `Spec` em `projects/`**, contra as **tres** fontes vigentes que a alojam em `products/<slug>/specs/` — `FND-03 §3.6`, `FND-04 §6` e `FND-10 §4.4` | Achado **`RD-41`**, severidade **Baixa**, dono **DEP-EXE**, gatilho *"ato sobre `PS-2026-010`"*. ✅ **CORRIGIDO no candidato `DEP-PRD` 1.1.0** — e a correcao e **para** o local canonico, **nunca do** local canonico: **`0` bytes** nas tres fontes, e **`RD-33` permanece aberto e bloqueante**. **Encontrado ao reescrever a linha do tipo `SPC`**, nao por varredura — o mesmo metodo que produziu `RD-37` |
| 65 | **O cabecalho de §4 deste catalogo declarava *"159 de 159"* enquanto a soma das proprias subsecoes dava 169** — `10 + 40 + 32 + 19 + 24 + 11 + 33`. §2 declarava **169**; o cabecalho de §4, **159** | Achado **`RD-42`**, severidade **Baixa**, familia **`RD-35`**, **segunda ocorrencia**, dono **DEP-GOV**, gatilho imediato. ✅ **CORRIGIDO nesta emissao**, e a **causa** tambem: o cabecalho passa a ser **derivado da conferencia dos blocos**, em vez de escrito como literal (`RG-03`). **A conferencia de §4 da emissao anterior comparava a soma contra §2 e nao contra o proprio cabecalho** — e foi essa a lacuna do instrumento |
| 66 | **`IR-03` exclui `substituido_por` de `H-N` e NAO exclui `superado_por`.** Como `superado_por` e **o unico campo de sucessao que um `ADR` possui**, gravar a superacao de um `ADR` **altera o `H-N`** dele — medido: `ADR-0021` passa de `511ace98…5316` para `09814377…b89a`. Logo a autorizacao de **`FND-10 §6.2`** para `M1` — *"muda apenas o estado e **os campos de sucessao**"* — **fica sem objeto praticavel para `ADR`** | Achado **`RD-43`**, severidade **Media**, dono **DEP-GOV**, gatilho *"proxima superacao de `ADR`"*. **DECLARADO, NAO RESOLVIDO:** alterar `IR-03` e **`C2` com ADR** (`IR-04`) e **nao e materia da Missao 1.13.1**. **Encontrado por exercer o instrumento, nao por le-lo:** a leitura de `FND-10 §6.2` **autorizava** a gravacao, e **so a medicao do hash** revelou a assimetria — [PS-2026-009 §3.1](pacote-soberano-2026-07-29-fnd-11.md). **Se a alternativa tivesse sido escolhida por leitura, o acervo teria alterado o `H-N` de um artefato `M1` acreditando estar dentro da regra.** Decima quinta confirmacao de [MEM-APR-0006](../memory/aprendizado/MEM-APR-0006-exercer-o-contador-revela-o-defeito.md) |
| 58 | **O Framework de Specifications foi instituido sem que exista uma unica `Spec`** — `SF-01` a `SF-32` sao **determinados e nao observados**, e `SF-09` institui **21 blocos obrigatorios** cujo custo **nao foi medido** | Registrado como ressalvas **`R1`** e **`R2`** de [FIT-2026-015](fitness/FIT-2026-015-framework-de-specifications.md), dono **DEP-PRD**, gatilhos **a primeira `Spec` real** e **a primeira `Spec` medida contra o dobro da mediana do tipo** (`CE-05`). **Nenhum numero foi estimado** — `CE-04` proibe, e o registro **declara a ausencia em vez de preenche-la**. E o mesmo regime de `A1` e `A2` de [ADR-0020 §8](../decisions/ADR-0020-regime-ministerial-de-promulgacao-e-ativacao.md): **regra em vigor sem membro observado, dito com esse nome** |
| 68 | **A variante `V2` de `FND-01`, medida na Missao 1.13.1 como *alternativa*, atribui a `ADR-0022` o backfill de `AC-08` — que o **escopo literal de `ADR-0022` exclui** em `J14` e §7.3.** Promulga-la poria, no **nivel 1** da hierarquia normativa, uma afirmacao que um `ADR` **`M1`** contradiz e **nao pode ser corrigido para concordar** (`CC-01`, `LV-04`) | Achado **`RD-45`**, severidade **Media**, dono **DEP-GOV**. ✅ **CORRIGIDO no candidato** — [ADR-0024 §5.3](../decisions/ADR-0024-conformidade-de-contrato-das-fundacionais.md) separa as duas linhas de historico, uma por `ADR`. **Encontrado por construir o cumulativo e comparar**, nao por reler `V2`: a variante fora montada para **medir uma hipotese**, e reaproveita-la como candidato de rito proprio **sem reatribuir a autoria** produz afirmacao falsa dentro da norma |
| 69 | **`FND-10 §8.5` declarava CINCO valores de 2026-07-28 como se fossem correntes, e `RD-27` item *(c)* contara TRES.** Os nao contados: o **denominador do acervo** *(`18.916` → **51.698**)*, o **percentual derivado** *(`5,7%` → **2,2%**)* e a **nota de `CE-05`** sobre `FND-09` *(`1.225` → **1.263**)*. **Dois deles estao na mesma frase que os tres contados** | Achado **`RD-46`**, severidade **Baixa**, dono **DEP-GOV**. ✅ **CORRIGIDO no candidato** — [ADR-0024 §5.4](../decisions/ADR-0024-conformidade-de-contrato-das-fundacionais.md). **A causa nao e o numero: e a ausencia de regra de leitura.** `CE-04` exige fonte e valor observado; `§8.5` tinha valor observado **e nao dizia de quando** — e numero sem data **nao envelhece virando historico, envelhece virando afirmacao falsa**. O candidato **vincula cada valor a baseline em que vale** |
| 70 | **O regime de estado na promulgacao de versao nova e costume, nao regra escrita.** Carta volta a `em-revisao`/`pendente` e recebe **`O4`** *(precedente `PS-2026-010`)*; fundacional permanece `ativo`/`ratificada` e **nao** recebe *(precedente `PS-2026-009 §4.1`)*. **`FND-10 §5.2` define `O4` e nao diz quando a promulgacao de versao nova o exige** | Achado **`RD-47`**, severidade **Media**, dono **DEP-GOV**, gatilho *"proxima emenda de `FND-10 §5`"*. **NAO corrigido** — seria `C2` com ADR proprio sobre `FND-10`, fora da competencia dos ritos desta missao. **Consequencia pratica: o `H-P` de todo objeto futuro depende de qual precedente se aplica**, e a escolha **nao e derivavel de norma**. Encontrado por **montar candidatos dos dois tipos na mesma missao** |
| 71 | **O custo de reversao declarado de `ADR-0020` envelheceu exatamente na parte que ninguem contou.** `§10` daquele ADR mediu *"1 ADR novo + 6 indices `M3`"* — e **os 6 continuam 6**, a medicao acertou. O que **nao entrou na conta** foram os artefatos **`M1`/historico** que passariam a citar decisao superada e **nao sao corrigiveis**: de **4** na Missao 1.13 para **10** na 1.13.1 e **12** agora | Achado **`RD-48`**, severidade **Baixa**, dono **DEP-GOV**, gatilho *"proxima superacao de `ADR` com mais de 10 citacoes em `M1`"*. **`ADR-0020` NAO e reclassificado e NAO e tocado** — e `M1` (`AC-10`, `CC-01`). **`C2 · Tipo 2` continua correto**, porque **`0` artefatos normativos migram; o que deixa de ser verdade e que a reversao seja *limpa***. O recalculo vive em [PS-2026-013 §5](pacote-soberano-2026-07-30-consolidado.md), **fora do ADR**, que e o unico lugar onde pode viver |
| 72 | **O setimo ato soberano foi consumido integralmente: 14 objetos, 14 arquivos, `0` divergencias.** E o **primeiro ato que cria um documento fundacional** *(`FND-11`)*, o **primeiro que move dez objetos com `O4`** e o **primeiro em que o `O4` foi DETERMINADO por reproducao de `H-P`**, e nao inferido do costume — achado **70** deixa de ser risco operacional | ✅ **Aplicado e provado** — `H-P` **14/14**, `H-N` invariante **10/10**, `IR-09` **10/10**, identidade binaria **4/4**, `0` bytes fora dos diffs. `RD-27`, `RD-31` e `RD-37` **FECHADOS**. [MSG-2026-0007](../memory/operacional/MSG-2026-0007-ato-soberano-vigencia-do-framework-de-specifications.md) · [PT-2026-010](relatorio-transicao-2026-07-30-vigencia.md) · [FIT-2026-018](fitness/FIT-2026-018-vigencia-do-framework-de-specifications.md) |
| 73 | **`RD-49` — `DEP-OPS`, `DEP-GRW` e `DEP-TLS` 1.1.0 declaram em §13.2 *Carta integral* `437 · 443 · 424` linhas, contra `438 · 444 · 425` medidas por `wc -l`.** As tres receberam a **linha de historico** que `FND-03 §6` obriga e **nao remediram §13.2** — o mesmo defeito que `RC-01` mediu em `DEP-QAR` e que `RD-46` mediu em `FND-10 §8.5`, agora na **terceira** familia. `DEP-PRD` e `DEP-EXE` **remediram** e nao tem o defeito | ⚠️ **ABERTO. Nao corrigivel por edicao:** as tres Cartas foram **ratificadas** em 2026-07-30 (`LV-04`), e a correcao exige **ato novo**. `D-12` cai de **8/9** para **6/9** em [`departments/README §2.2`](../departments/README.md). **Detectado por exercer o instrumento de `DC-10`, nao por ler o texto** | ⟵ ✅ **CORRIGIDO POR RITO ATE O LIMITE DA MISSAO 1.13.4.1 — e NAO aplicado.** Tres candidatos **1.2.0** medidos fora do acervo, declarando **439 · 445 · 426** e remedidos **DEPOIS** da linha de historico, como `RA-1` de `FIT-2026-018` prescrevia; `H-N` invariante sob `O4`, `IR-09` e `O4` de dois campos: **3 de 3** em cada prova. **PERMANECE ABERTO:** emendar Carta ratificada **exige ato novo** do Soberano — `DC-09`, `LM-03`, `IR-01`, precedente `DEP-QAR` **1.2.0**. [PT-2026-012 §3.1](relatorio-transicao-2026-07-31-manutencao-instrumentos.md)
| 74 | **`RD-50` — `foundation/README` projetava o custo do nucleo em `5,1%`, contra `5,7%` de `FND-10 §8.5` 1.4.0 e `2,2%` da 1.5.0.** A projecao estava defasada em **duas geracoes** e de **duas fontes distintas**: nao acompanhou nem a medicao que copiava, nem a correcao de `RD-46` | ✅ **CORRIGIDO nesta emissao** — o indice passa a declarar **2,2%** **e a baseline em que o valor vale** (`BL-2026-07-29-10`), pela regra de leitura que `FND-10` 1.5.0 instituiu. Indice e **projecao** (`RG-03`, `CV-04`), corrigivel sem ato |
| 75 | **`RD-51` — o catalogo mestre declarava `ADR-0014` como *"CANDIDATO, sem vigencia · `ratificacao: pendente`"*, enquanto o arquivo esta `ativo` · `ratificada` desde o ato de 2026-07-29 — e o proprio §2 deste catalogo ja o listava entre os artefatos em vigor.** O **mesmo documento** afirmava as duas coisas. A causa e o slug `ADR-0014-candidato-...`, que descreve **a origem** e foi lido como **estado** | ✅ **CORRIGIDO nesta emissao** — §4.2 passa a declarar o estado do frontmatter, que e a fonte corrente (`FND-10 §5.4`). **O slug NAO foi alterado:** renomear arquivo ratificado exige rito proprio, e o achado fica registrado como a razao pela qual o nome engana. Familia de `RD-42` — cabecalho divergindo da propria subsecao |
| 76 | **`RD-52` — [`governance/README`](README.md) estava DUAS baselines atras e o contador de `FIT` uma emissao atras**: declarava `BL-2026-07-29-08` · **164** · **46.353** contra `BL-2026-07-30-01` · **185** · **54.190** na fonte, e **16** `FIT` onde existiam **17** arquivos. **Decima primeira ocorrencia** da familia de `MEM-APR-0002`, e a **terceira nesta mesma secao** | ✅ **CORRIGIDO na projecao**, nenhuma fonte alterada (`RG-03`, `PJ-03`, `M3`). **A reincidencia no mesmo lugar apos duas correcoes ja registradas e o achado real:** `CV-04` **nao tem gatilho automatico** naquela secao, e ela so e tocada quando alguem lembra dela. **Registrado como causa, nao como descuido** |
| 77 | **`RD-53` — o comando publicado da baseline nao reproduzia `BL-2026-07-30-01` sobre a copia datada em que ela foi medida.** O comando exclui `./.obsidian/*` e `./_SAIDA-COMPANY-OS/*`, e a raiz continha tambem **`_candidatos/`** com **13** arquivos `.md`: executado **como publicado**, da **198**, nao **185**. **E §10.9 declara que as tres variantes de `FND-01` *"permanecem em `_candidatos/`"* — diretorio que NAO existe na raiz do acervo.** As tres **existem**, com **490 · 488 · 492** linhas e hashes que reproduzem os publicados, em `_backups/…_2026-07-30_pre-missao-1-13-3/_candidatos/` | Achado **`RD-53`**, severidade **Media**, dono **DEP-GOV**, gatilho *"proxima emissao de baseline"*. **A baseline VIGENTE reproduz** — `189 · 55.280 · `a3ca6ce3…ca5d`` —, porque `_candidatos/` ja nao esta na raiz. **`BL-2026-07-30-01` e `§10.9` NAO sao editadas** (`BL-02`, `CC-01`). **Segunda ocorrencia da familia de `RD-17`.** **Mitigado nesta missao pela escolha de caminho:** os candidatos da 1.13.4 vivem **fora** do acervo | ⟵ ✅ **FECHADO na Missao 1.13.4.1 por INSTRUMENTO NOVO, sem editar baseline alguma.** O defeito era do **comando**, nao da baseline: `BL-2026-07-30-01` **reproduz nos tres valores e nos 64 digitos** — **185 · 54.190 · `3d8dbea0…84da`** — sobre a mesma copia em que o comando publicado dava **198**. Correcao por **lista fechada positiva** + **portao de raiz** + **portao de split**, provada em **3 execucoes** com hash identico. [PT-2026-012 §2](relatorio-transicao-2026-07-31-manutencao-instrumentos.md)
| 78 | **`RD-54` — o portao de `ADR-0007 §5.3` nao distingue admitir *identidade* de admitir *conteudo*.** `G1` a `G5` sao escritos para *"conteudo externo"*, e o primeiro caso real exigiu uma distincao que **nenhuma das cinco condicoes nomeia**: sem ela, admitir um produto de **550** arquivos poderia ser lido como admitir os 550 | Achado **`RD-54`**, severidade **Media**, dono **DEP-GOV**, gatilho *"segunda admissao pelo portao, ou emenda a `ADR-0007`"*. **Contornado por `AM-01` e pela classificacao `G3`, nao fechado.** **Encontrado por exercer o portao, e nao por le-lo** — nenhuma leitura de `ADR-0007` o revelaria |
| 79 | **`RD-55` — as quatro classificacoes de `G3` descrevem destino de CONTEUDO, e nenhuma descreve *"admitir a existencia sem admitir nada"*.** **`REWRITE` foi escolhida por eliminacao**, e a sua definicao — *"a solucao do Legacy nao serve"* — **nao e literalmente verdadeira** no caso: a solucao **nao foi avaliada**, porque **nao foi submetida** | Achado **`RD-55`**, severidade **Media**, dono **DEP-GOV**, mesmo gatilho de `RD-54`. **O efeito de `REWRITE` e o correto — `0` entradas e proveniencia `native`** —, e a imprecisao do nome esta **declarada em vez de dissolvida**. `Q2` de [PS-2026-014 §7](pacote-soberano-2026-07-31-medally.md) pergunta ao Soberano se deve ser emendada |
| 80 | **`RD-56` — `TPL-carta-produto` 1.0.0 nao preve `capabilities` no frontmatter nem os cinco campos de `FND-10 §2.2`**, embora `FND-09` E-17 declare `capabilities` como **atributo minimo** de `PRO` e `FND-04 §6` faca do vinculo a Capability **pre-condicao universal I**. Nao ha secao para **Capabilities consumidas** nem para **interfaces** | Achado **`RD-56`**, severidade **Media**, dono **DEP-GOV** *(forma)* + **DEP-PRD** *(conteudo)*, gatilho *"antes da segunda Carta de Produto"*. **Segunda ocorrencia da familia de `RD-23`** — template que contradiz a norma que deveria instrumentar. **NAO corrigido:** emendar template e `C2` propria, e correcao silenciosa e proibida. **A Carta candidata excede o template**, por norma superior, e declara por que | ⟵ ✅ **FECHADO na Missao 1.13.4.1.** `TPL-carta-produto` **1.1.0** *(133 → 183 linhas)*: `capabilities` e os cinco campos no frontmatter da instancia, **§8 Capabilities consumidas** e **§9 Interfaces**, secoes contiguas 1–14. Rito **`C2`**, aprovador **DEP-GOV** por `FND-09 §8.2` linha `TPL`, precedente `TPL-spec` **1.1.0**. [PT-2026-012 §4](relatorio-transicao-2026-07-31-manutencao-instrumentos.md)
| 81 | **`RD-57` — este catalogo divergia de si proprio em CINCO lugares, todos anteriores a esta missao.** `resumo` declarava **169**; §Escopo, **164**; §2, **185** artefatos e **54.190** linhas *(os valores de `BL-2026-07-30-01`)*; a conferencia de §4 somava `10 + 47 + … = 185`, com um `10` que a **propria §4.1** contradiz desde `FND-11`; e §9 declarava **169** `native` — enquanto §10.0 do **mesmo documento** declarava **189 · 55.280** | Achado **`RD-57`**, severidade **Media**, dono **DEP-GOV**. ✅ **CORRIGIDO nesta emissao, na projecao**, valor a valor, **medido por ferramenta**, **zero fontes alteradas** (`PJ-03`, `RG-03`, `M3`). **Sexta ocorrencia de o catalogo divergir de si proprio** — as anteriores foram `IC-8`, `RE-04`, `RD-06`, `RD-16` e `RD-42` — e **decima quarta** da familia de [MEM-APR-0002](../memory/aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md). **A causa e sempre `CV-04`**, e a novidade e o alcance: a emissao anterior remediu §10 e §4.1 e **nao remediu os agregados que os resumem** | ⟵ ✅ **FECHADO na Missao 1.13.4.1**, por conferencia **valor a valor** dos cinco lugares contra `§10.0`. [PT-2026-012 §3.2](relatorio-transicao-2026-07-31-manutencao-instrumentos.md)
| 82 | **`RD-58` — [`governance/README`](README.md) mantem uma DUPLICATA do contador `FIT`, e ela estava TRES emissoes atras.** A tabela *Contadores oficiais* declarava **`016` / `017`** enquanto a **linha imediatamente seguinte do mesmo arquivo** reconhece [`fitness/README`](fitness/README.md) como a fonte — e la o valor era **`018` / `019`**. **`PJ-01` proibe a segunda fonte de verdade**, e o defeito **nao e a divergencia: e a duplicata** | Achado **`RD-58`**, severidade **Baixa**, dono **DEP-GOV**, gatilho *"proxima emenda a `governance/README`"*. ✅ **Valor corrigido na projecao**; **a supressao da linha duplicada e mudanca de estrutura do indice** *(`AC-09`)* e fica **declarada, nao executada**. **Quarta ocorrencia da familia dentro deste mesmo arquivo**, apos `RD-04`, `RD-32` e `RD-52` | ⟵ ✅ **FECHADO na Missao 1.13.4.1, e a correcao foi SUPRIMIR a linha, nao corrigir o valor.** O defeito nunca foi a divergencia — era a **duplicata** (`PJ-01`), e corrigir o valor de uma duplicata **adia** o defeito. O gatilho declarado era *"proxima emenda a este indice"*; foi esta. [PT-2026-012 §3.3](relatorio-transicao-2026-07-31-manutencao-instrumentos.md)
| 83 | **`RD-59` — `G1` do portao exige *"em que data foi observado"*, e data nao basta para repositorio vivo.** O candidato mudou **entre a abertura e o fechamento da mesma missao, no mesmo dia**: **1** arquivo novo e **15** alterados, **todos** material de demonstracao e os seus tres geradores. **Nenhum foi lido ou executado pela missao, e as 5 fontes consumidas estao byte a byte identicas** | Achado **`RD-59`**, severidade **Media**, dono **DEP-GOV**, gatilho *"segunda admissao pelo portao"*. **Terceira lacuna medida do portao**, ao lado de `RD-54` e `RD-55`. **A evidencia continua valida** porque o instante ficou fixado por um manifesto `sha256` de **527** arquivos *(`cc6fbbcf…aadc`)* — **produzido por determinacao da missao, e nao exigido por `G1`**. **Correcao possivel e barata:** `G1` passar a exigir **instante verificavel** *(commit, manifesto ou hash de arvore)* em vez de data. Reconciliacao integral em [PS-2026-014 §2.2](pacote-soberano-2026-07-31-medally.md) |
| 84 | **`RD-60` — o recorte enumerado de [`PS-2026-014 §2.2`](pacote-soberano-2026-07-31-medally.md) ficou TRES caminhos curto, e o total de fechamento nao foi medido.** Mudaram **19** caminhos no repositorio externo dentro da janela da 1.13.4; o pacote enumerou **16**. **Os 15 alterados batem exatamente**; dos **4** arquivos NOVOS so **1** foi enumerado — faltaram `tests/test_paginas_felipe.py`, `tests/__pycache__/test_paginas_felipe…pyc` e `ferramentas/__pycache__/montar_paginas_felipe…pyc`. E o total de fechamento **medido e 554**, contra **551** publicado como *"observado, nos dois instantes"*: **`551 = 550 + 1`** e aritmetica sobre o unico novo enumerado, nao medicao | **Media** | ⚠️ **ABERTO.** **A conclusao do pacote sobrevive** — os tres omitidos sao da **mesma** linha de trabalho paralela, **`0`** foi lido ou executado pela missao, e **`0` bytes** seguem atribuiveis a ela; **o que nao sobrevive e a completude da enumeracao**. Causa: a prova deixou de ser o manifesto e virou **lista escrita a mao**, e lista escrita a mao **omite em silencio**. **Instrumento novo entregue** — o delta passa a ser **calculado** e o volatil **classificado**, nunca descartado: [PT-2026-012 §5](relatorio-transicao-2026-07-31-manutencao-instrumentos.md). `PS-2026-014` **nao e editavel** por missao de manutencao |
| 85 | **`RD-61` — a passagem de `73` para `71` fontes normativas soma duas mudancas de naturezas OPOSTAS num unico numero.** **`−3`** por **mudanca de criterio** *(os tres indices `README` das arvores `foundation/`, `capabilities/` e `departments/` deixaram de ser contados quando a baseline passou a escrever "excluidos os indices")* e **`+1`** por **mudanca de acervo** *(`FND-11` criada)*. **`73 − 3 + 1 = 71`** | Baixa | ✅ **EXPLICADO com evidencia**, medido nas **duas** copias datadas pelos **dois** criterios — [PT-2026-012 §3.4](relatorio-transicao-2026-07-31-manutencao-instrumentos.md). **As baselines NAO foram editadas** (`BL-02`). **Os sinais opostos tornaram as duas causas mutuamente invisiveis**, e nenhuma baseline declarou a mudanca de criterio. Dono **DEP-GOV**; gatilho *"proxima baseline"*: **declarar o criterio ao lado do numero** |
| 86 | **`RD-62` — [`FND-10 §2.2`](../foundation/10-artifact-framework.md) intitula *"Extensao do contrato — CINCO campos novos"* e a tabela imediatamente abaixo tem SEIS linhas**: `resumo`, `perfil_contexto`, `confidencialidade`, `revisor`, `ratificacao` e **`projecao_de`**. Todo o acervo cita *"os cinco campos"*, e a leitura sobrevive porque `projecao_de` e **condicional** — mas titulo e tabela **nao concordam** | Baixa | ⚠️ **ABERTO e NAO corrigido.** `FND-10` e **fundacional em vigor**: editar altera `H-N` e **exige ato** (`LV-04`, `IR-01`). **Fora da lista da Missao 1.13.4.1** — declarado, jamais corrigido em silencio. **Familia de `RD-46`**, agora na segunda ocorrencia dentro de `FND-10` |
| 87 | **`RD-63` — os 19 templates declaram `aprovador: SOBERANO` no proprio frontmatter, e `FND-09 §8.2`, linha `TPL`, declara `DEP-GOV`.** A pratica segue a **norma**, nao o campo: `TPL-spec` **1.1.0** foi emendado e aplicado *"aprovado por DEP-GOV"*, e a Missao 1.13.4.1 emendou `TPL-carta-produto` pelo mesmo fundamento | Baixa | ⚠️ **ABERTO e NAO corrigido.** Alcanca **19** arquivos e e rito proprio; **fora da lista**. **Declarado porque a missao exerceu a norma contra o campo** — exercer sem declarar seria o defeito. Dono **DEP-GOV**; gatilho *"proxima emenda de template"* |
| 88 | **`RD-64` — a oracao condicional que gera `Q1` NAO esta em `PT-2026-009 §1`.** *"se seguir sendo o primeiro produto comercial"* esta em **[`PS-2026-013 §7`](pacote-soberano-2026-07-30-consolidado.md)**; a palavra `comercial` tem **`0` ocorrencias** no arquivo de [`PT-2026-009`](relatorio-transicao-2026-07-30-convergencia.md), cuja decisao **7** le, literalmente: *"Via futura e `S1` com Produto real (`nXtrack`); `S2` deferida"*. **Quatro** artefatos vigentes atribuem a citacao a `PT-2026-009 §1`; **`ADR-0026` `E8` e `RFC-0021` §5 atribuem corretamente** | **Media** | ⚠️ **ABERTO.** **Nao altera `Q1` nem o merito dela** — o texto existe e esta num pacote submetido ao Fundador. **`Q1` pergunta como ler UM TEXTO, e quatro artefatos apontam o lugar errado ao busca-lo.** Alcanca `PS-2026-014` e `PT-2026-011` *(nao editaveis por missao de manutencao)* e duas projecoes `M3`. Dono **DEP-GOV**; gatilho *"ato que resolver `Q1`"* — [PT-2026-012 §7](relatorio-transicao-2026-07-31-manutencao-instrumentos.md) |
| 89 | **`RD-65` — a classe do rito nao se herda da fonte que descreveu o defeito.** A minuta B da Missao 1.13.4.1 declarava superar **`ADR-0005`** *"quanto ao criterio de afericao"*, e **`ADR-0005` nao contem criterio de afericao algum** — ele proibe o **par reflexivo** da relacao `verifica` (`RM-06`). O criterio mora em **`AC-03` de [`FND-10 §2.5`](../foundation/10-artifact-framework.md)**. Herdar o objeto superado teria produzido **`C2` onde a norma exige `C3`** — isto e, **aprovacao por DEP-EXE onde a Constituicao exige ratificacao do Soberano** | **Media** | ✅ **CORRIGIDO na Missao 1.13.4.2**, nos tres instrumentos — [ADR-0028 §1.1](../decisions/ADR-0028-independencia-de-verificacao-por-fornecedor.md). Registrado porque **o metodo e reutilizavel**: antes de aceitar a classe declarada por uma fonte, **localizar a norma superada no documento que a CONTEM**, nunca no que a cita. **O erro nao estava na classe — estava no OBJETO, e a classe era consequencia.** Familia de `MEM-APR-0002`, aplicada a **norma** em vez de a **numero** |
| 90 | **`RD-66` — o [`README` da raiz](../README.md) nao declara QUAIS sao as arvores normativas, e a fronteira entre norma e nao-norma existe na pratica sem estar escrita como conjunto.** O *Mapa do repositorio* enumera **9** linhas de diretorio e descreve o conteudo de cada uma **sem classificar nenhuma** como normativa ou nao normativa — a unica ocorrencia do termo esta **dentro** da celula de `foundation/`, *"os 11 documentos normativos"*. O acervo, porem, **opera** com o termo: as baselines declaram *"a camada normativa NAO mudou"* enumerando **`FND` + `TPL` + `CAP` + Cartas** — as tres arvores `foundation/`, `capabilities/` e `departments/` — e [`ADR-0027 §E4`](../decisions/ADR-0027-classe-de-admissao-de-existencia-no-portao-de-origem-externa.md) mede por *"varredura das tres arvores"*. **Nenhum artefato declara esse conjunto:** a extensao do termo vive em **convencao de medicao** | Achado **`RD-66`**, severidade **Baixa**, dono **DEP-GOV**, gatilho *"missao de catalogo"*. ⚠️ **ABERTO e NAO corrigido** — **registrar e apontar**, por despacho do Fundador; corrigir e da missao de catalogo. **A terceira oracao do enunciado original NAO sobreviveu a conferencia, e esta corrigida aqui:** *"artefato normativo pode ser criado fora das tres arvores sem violar regra alguma"* e **falso** — [`FND-10 §4.1`](../foundation/10-artifact-framework.md) fixa o **Local** dos quatro tipos da classe Normativa em `foundation/01-constituicao.md`, `foundation/NN-*.md` e `foundation/09-meta-model.md`, e [`FND-03 §7`](../foundation/03-taxonomia.md) enumera a arvore canonica. **O que a conferencia CONFIRMOU e mais estreito e mais preciso:** **(a)** o `README` **nao declara o conjunto**; **(b)** o unico conjunto declarado em norma e a **classe Normativa** de `FND-10 §4.1`, que tem **somente `FND`**, enquanto o conjunto que o acervo **mede** e a **camada normativa** das tres arvores, com `FND` + `TPL` + `CAP` + Cartas — **e nenhum artefato declara o segundo**; **(c)** `FND-03 §3` da *"Vive em"* a **17** tipos e **nao tem entrada para `FND` nem para a Carta de Departamento** — a localizacao dos dois so existe na arvore de `§7` e na coluna *Local* de `FND-10 §4`, que o proprio `FND-10` declara **projecao**. **Consequencia registrada:** a verificacao *"nenhum dos alterados e norma"* de `BL-2026-07-31-04` **e verdadeira pelas duas leituras** — e ainda assim **se apoia em convencao de medicao, nao em regra escrita** |
| 91 | **`RD-67` — o §2 *Estado do acervo* e o `versao` do frontmatter DESTE catalogo ficaram para tras enquanto §4, §10.0 e as projecoes seguiram a fonte.** Medido nesta emissao, **antes de qualquer escrita**: §2 declara **`Baseline vigente: BL-2026-07-31-02`** *(apontando `§10.11`)* e **`Linhas 57.769`**, *"sobre os mesmos **195** arquivos"*, **na mesma tabela** em que declara **`Artefatos 206`**, **`Classificados 206 de 206`** e **`Proveniencia 206 de 206`**; e o frontmatter declarava **`versao: 2.8.0`** quando o *Historico de versoes* do mesmo arquivo ja trazia **`2.9.0`** e **`2.10.0`** | Achado **`RD-67`**, severidade **Media**, dono **DEP-GOV**, gatilho *"missao de catalogo"*. ⚠️ **ABERTO e NAO reconciliado — §2 nao foi tocado nesta emissao:** esta missao **registra**, a de catalogo corrige. Corrigido **somente** o `versao` do frontmatter, **`2.8.0` → `2.11.0`**, porque emendar o arquivo sem versionar **criaria** a divergencia em vez de herda-la — correcao **declarada, nunca silenciosa**, com o estado original preservado na copia datada `_backups/LucaX-Enterprise-OS_2026-07-31_pre-rd-66/`. **Familia de o catalogo divergir de si proprio:** as listas ja registradas em §7 nomeiam `IC-8`, `RE-04`, `RD-06`, `RD-16`, `RD-17`, `RD-20`, `RD-24`, `RD-25` e `RD-42`. **Este achado NAO reivindica ordinal** — o proprio contador da familia aparece em §7 como **`Setima`**, **`Nona`** e **`Sexta`**, e afirmar um ordinal seria repetir o defeito que se registra |

| 92 | **`RD-68` — o contador `MSG-2026-NNNN` de [`memory/operacional/README`](../memory/operacional/README.md) estava UMA emissao atras.** Declarava *"ultimo atribuido `0006`; proximo `0007`"* **enquanto a tabela de Registros do mesmo arquivo ja listava `MSG-2026-0007`**, emitido em 2026-07-30. Medido nesta emissao, ao exercer o contador para numerar `MSG-2026-0008` — **nao ao le-lo** | Achado **`RD-68`**, severidade **Baixa**, dono **DEP-GOV**, gatilho *"proxima emissao de `MSG`"*. **O VALOR foi corrigido aqui por obrigacao de `SF-32`** — *criar artefato de sequencia e incrementar o contador sao a mesma mudanca* —, e passa a **`0008` / `0009`**. **A CAUSA fica ABERTA:** `CV-04` nao tem gatilho automatico neste indice, e e a **setima ocorrencia** da familia de [`MEM-APR-0006`](../memory/aprendizado/MEM-APR-0006-exercer-o-contador-revela-o-defeito.md) e `RD-32`. **Congelamento em vigor: registrado com dono e gatilho, sem missao designada** |
| 93 | **`RD-69` — a linha *Artefatos retidos por falta de ato* de §2 estava TRES `ADR` atras.** Declarava **1** *(`ADR-0026`)* enquanto `ADR-0027`, `ADR-0028` e `ADR-0029` estavam, os tres, `em-revisao` e retidos por falta de ato desde 2026-07-31. **Medido ao aplicar o oitavo ato**, quando dois deles sairam da fila — **nao ao ler a linha** | Achado **`RD-69`**, severidade **Baixa**, dono **DEP-GOV**, gatilho *"proxima criacao de `ADR` retido"*. **O VALOR foi reconciliado nesta emissao**, porque a aplicacao o alterava de qualquer modo (`CV-04`, `RG-03`): passa a **2** — `ADR-0026` e `ADR-0028`. **A CAUSA fica ABERTA e sem missao designada** — familia de `RD-32`, `RD-57` e `RD-68`: agregado de §2 que nenhum gatilho automatico alcanca |
| 94 | **`RD-70` — o `versao` do frontmatter do [`README` da raiz](../README.md) esta UMA emissao atras do proprio *Historico de versoes*.** Declarava **`1.16.0`** enquanto o historico do mesmo arquivo ja trazia **`1.17.0`**, da Missao 1.13.4.2. **E a mesma forma de `RD-67`**, que registrou o defeito neste catalogo — agora medida no indice mestre | Achado **`RD-70`**, severidade **Baixa**, dono **DEP-GOV**, gatilho *"missao de catalogo"*. ⚠️ **ABERTO e NAO corrigido.** Esta emissao **declara** a defasagem e **nao a fecha**: corrigi-la e escolher entre renumerar o historico ou saltar a versao, e **essa escolha e da missao de catalogo**, congelada. **O incremento desta emissao segue o historico**: o `README` da raiz passa a **`1.18.0`** no historico **e** no frontmatter, o que **para a deriva daqui em diante**. **A defasagem preterita permanece registrada e NAO reconciliada** — a versao **`1.17.0`** nunca existiu no frontmatter, e decidir se ela e renumerada ou preservada como salto e da **missao de catalogo**, congelada |
| 95 | **`RD-71` — o candidato `nXtrack` NAO tem repositorio proprio: e subarvore de `lucaX`.** A subarvore esta limpa — **`0`** caminhos sem commit em **183** rastreados —, mas o **hospedeiro** tem **758** *(636 nao rastreados + 122 modificados)* e **escritor concorrente ativo** *(sessao `2bad2c98`, 08:25:47, e commit `b9fbccd` as 07:37, fora do candidato)*. **Nao ha fronteira de custodia separavel do hospedeiro**, e a Carta descreve a custodia **que o ato institui**, nao a que existe | Achado **`RD-71`**, severidade **Alta**, dono **DEP-PRD**, gatilho *"primeira `Spec` do `PRO-nxtrack`, ou primeira admissao com `G0` = `CONTEUDO`"*. ⚠️ **ABERTO. Congelamento em vigor: NAO gera missao.** **Nao impede `G1`**, porque nenhuma das 17 fontes consumidas esta fora dos rastreados |
| 96 | **`RD-72` — `13.182` arquivos da subarvore do candidato nao tem commit, e portanto nao tem autoria nem data atribuivel.** Incluem `.pytest_cache`, `.scratch`, `.venv`, `node_modules` e **os bancos com dado real** *(`nxtrack.db`, **4.919.296** bytes, mais 15 copias)*. **`183 + 13.182 = 13.365`, soma exata:** nao existe arquivo fora dessas duas classes | Achado **`RD-72`**, severidade **Media**, dono **DEP-PRD**, gatilho *"qualquer consumo de fonte fora dos 183 rastreados"*. ⚠️ **ABERTO, sem missao.** **Nenhum dos 13.182 foi consumido**, e por isso o achado **nao alcanca** as 17 fontes de `G1` |
| 97 | **`RD-73` — atribuicao por commit nao e atribuicao por processo gerador.** As **17 de 17** fontes consumidas tem autor e data — `Lucas <lucastx13.projetosia@gmail.com>`, em **18 de 18** commits —, mas isso identifica **quem commitou**, nao **o que gerou o texto**. O candidato tem `CLAUDE.md`, `.claude/agents/` e `.claude/skills/` rastreados, e **nenhum registro nomeia qual processo produziu qual arquivo** | Achado **`RD-73`**, severidade **Media**, dono **DEP-QAR**, gatilho *"segunda admissao pelo portao — junto ao gatilho de `ADR-0027 §12`"*. ⚠️ **ABERTO, sem missao.** Registrado como `AT-1` para que *"17 de 17 atribuidas"* **nunca seja lido como atribuicao de autoria intelectual** |
| 98 | **`RD-74` — `VC-03` dispara no primeiro Produto candidato.** `PRO-nxtrack` vincula **5** Capabilities — `produto`, `inteligencia-artificial`, `dados`, `engenharia`, `operacoes` — onde `FND-08 VC-03` sinaliza em **mais de tres**. **Reduzir a lista para tres falsearia o vinculo**, e `VC-01` proibe elo que nao corresponde; a regra manda **avaliar especializacao do componente**, nunca criar Capability | Achado **`RD-74`**, severidade **Media**, dono **DEP-PRD**, gatilho *"primeira `Spec`"*. ⚠️ **ABERTO, sem missao.** É `S4` de [FIT-2026-023](fitness/FIT-2026-023-admissao-do-nxtrack.md) |
| 99 | **`RD-75` — `ADR-0027` tem CORPO que contradiz o proprio frontmatter.** O preambulo do artefato declara *"NAO ESTA EM VIGOR. `status: em-revisao`"* enquanto o frontmatter declara **`status: ativo`** desde o oitavo ato. **O frontmatter e a autoridade de vigencia**; o corpo e texto da redacao original, **nao editado** por `BL-02` e `CC-01` — mas **quem ler so o corpo conclui o oposto do vigente**, e `RECOGNIZE` depende dessa vigencia | Achado **`RD-75`**, severidade **Media**, dono **DEP-GOV**, gatilho *"proxima emenda que tocar `ADR-0027`, ou primeira leitura por terceiro"*. ⚠️ **ABERTO e NAO corrigido.** Corrigi-lo exigiria **editar `ADR` aprovado**, o que `AL-02`/`LV-04` proibem — a saida e ADR novo ou nota de catalogo, e **essa escolha e da missao de catalogo**, congelada |
| 100 | **`RD-77` — o §2 *Estado do acervo* deste catalogo estava SEIS baselines atras em duas linhas.** *Linhas* declarava **57.769** sobre **195** arquivos e *Baseline vigente* declarava **`BL-2026-07-31-02`**, quando §10.0 ja registrava `BL-2026-07-31-08` com **208 · 60.921**. **É a mesma familia de `RD-67`**, que fechou a divergencia de §2 uma emissao antes e **reincidiu nas linhas que aquela correcao nao alcancou** | Achado **`RD-77`**, severidade **Media**, dono **DEP-GOV**, gatilho *"missao de catalogo"*. ✅ **Corrigido NA PROJECAO nesta emissao** *(`RG-03`, `PJ-03`, `M3`; nenhuma fonte alterada)*, e **registrado** porque a reincidencia apos correcao e **sinal, nao acidente**: `CV-04` nao tem gatilho automatico nesta secao |
| 101 | **`RD-76` — a serie de vigilancia de [`fitness/README`](fitness/README.md) conta `13` vereditos emitidos com `23` arquivos `FIT` no acervo.** A metrica esta rotulada *"Vereditos emitidos"* e a linha seguinte enumera **13 ciclos** — **o rotulo e a semantica divergem**, e nao ha como saber, do proprio artefato, se o numero conta ciclo ou veredito | Achado **`RD-76`**, severidade **Baixa**, dono **DEP-QAR**, gatilho *"proxima auditoria de ressalvas"*. ⚠️ **ABERTO e NAO corrigido — deliberadamente.** **Corrigir um numero cuja semantica nao foi estabelecida seria inventar a semantica**; a reconciliacao pertence a auditoria que [FIT-2026-018](fitness/FIT-2026-018-vigencia-do-framework-de-specifications.md) ja declarou fora de escopo. Familia de `RD-36` |
| 102 | **`RD-78` — artefato publicado e hasheado alterado sem bump de versao e sem entrada de historico, com os bytes originais NAO recuperaveis.** `PT-2026-014` foi alterado **14 minutos depois** de `PS-2026-016` **1.0.0** publicar o `H-A` dele; a versao seguiu **`1.0.0`, inalterada**, e o historico manteve **uma unica entrada**. Os bytes de `f4f63f1e…a826e` **nao reproduzem em `14.112` arquivos** varridos em **quatro** arvores — **o diff e IMPOSSIVEL** | Achado **`RD-78`**, severidade **Alta**, dono **DEP-GOV**, gatilho *"missao de catalogo, ou proxima emissao de baseline — o que ocorrer primeiro"*. ⚠️ **ABERTO. Congelamento em vigor: NAO gera missao.** **Linha de PROJECAO** (`CV-04`, `PJ-03`): a **fonte** e [`PS-2026-016 §2.3`](pacote-soberano-2026-08-01-nxtrack.md), emitida na `1.1.0`; §7 estava **sem entrada** para ela, e a ausencia foi medida ao registrar o **nono ato**. **Nenhum merito novo e afirmado aqui** — nao se afirma **o que** mudou em `PT-2026-014`, nem que a alteracao tenha sido indevida ou inocua: **as duas leituras exigiriam o diff que nao existe** |
| 103 | **`RD-79` — a correcao soberana de `CA-2` nao alcancou o pacote seguinte.** O Soberano ja emitira a mesma correcao em `PS-2026-015 §6.1.4.1` e no item **VI** daquele ato, em **2026-07-31**; ela **nao alcancou** `PS-2026-016`, emitido no dia seguinte, porque **viveu num pacote e nao no molde de pacote soberano** — cada pacote redige as suas condicoes do zero, e um defeito corrigido num deles **renasce no proximo** | Achado **`RD-79`**, severidade **Alta**, dono **DEP-GOV**, gatilho *"proxima emissao de pacote soberano, ou missao que tocar o molde/`TPL` de pacote soberano"*. ⚠️ **ABERTO. Congelamento em vigor: NAO gera missao.** **Linha de PROJECAO**, mesma condicao de `RD-78`: fonte em [`PS-2026-016 §6.1.1`](pacote-soberano-2026-08-01-nxtrack.md), `1.2.0`. **Regra que o achado fixa:** *toda condicao anterior de eficacia que meca a arvore inteira nasce insatisfazivel e deve nascer INFORMATIVA* — ancoragem de ato e **por objeto consumido** |
| 104 | **`RD-80` — [`governance/roadmap-canonico.md`](roadmap-canonico.md) e MEDIDO pelo instrumento e NAO tem entrada no catalogo.** Ele declara-se *"registro de acompanhamento, autoridade nenhuma, nao normativo, atualizavel sem rito"* — mas vive em `governance/`, **dentro da lista fechada positiva** de `baseline.sh`, e por isso **conta como artefato**: a medicao desta emissao devolve **214 · 62.536 · `7ea160e2…d3dc`** contra **213 · 62.250 · `4252fe47…621c`** de `BL-2026-08-01-01`. **`RG-02`: artefato sem entrada aqui e nao localizavel.** O frontmatter de um arquivo **nao instrui o medidor** — a lista fechada instrui | Achado **`RD-80`**, severidade **Media**, dono **DEP-GOV**, gatilho *"proxima emissao de baseline"*. ⚠️ **O GATILHO DISPAROU em 2026-08-01, com `BL-2026-08-01-02`, e o achado segue ABERTO — declarado, nao esquecido.** Ele **nao** foi corrigido porque as tres saidas continuam sendo **decisoes** — dar entrada de catalogo a um registro que se declara nao-artefato, mover o arquivo, ou declara-lo `NAO_ACERVO` —, e **nenhuma e reconciliacao de projecao**. **A diferenca em relacao a `RD-81` esta no dono:** ali o dono e o **SOBERANO** e ele **decidiu no despacho de abertura**; aqui o dono e **DEP-GOV** e **nao ha decisao**. Esta emissao **nomeia a ausencia nos tres lugares que a escondiam** — §2 *Classificados*, o cabecalho de §4 e a *Conferencia dos blocos*, que agora declara que a soma **nao** iguala o total medido e **por que**. **Congelamento em vigor: NAO gera missao.** **Corrigi-lo e escolher** entre dar entrada de catalogo a um registro que se declara nao-artefato, mover o arquivo para fora das raizes medidas, ou declara-lo `NAO_ACERVO` no instrumento — **as tres sao decisoes**, e nenhuma e reconciliacao de projecao. **O `+1` nao nasceu no nono ato:** o arquivo ja existia antes desta sessao |
| 105 | **`RD-81` — `CLAUDE.md` na raiz do acervo faz o portao de raiz RECUSAR medir a baseline.** Criado por determinacao do Fundador para abrigar a regra permanente do roadmap, o arquivo **nao esta declarado** na lista fechada de `baseline.sh` — nem como acervo, nem como nao-acervo —, e o instrumento **para com erro**: *"entrada nao declarada na raiz do acervo"*, saida **`2`**. **Medido nesta emissao, ao exercer o instrumento apos a escrita — nao ao le-lo** | Achado **`RD-81`**, severidade **Media**, dono **SOBERANO** *(a escolha do lado da lista e do Nivel 0, como foi a criacao do arquivo)*, gatilho *"proxima emissao de baseline"*. ✅ **FECHADO em 2026-08-01 pelo PROPRIO DONO, e nao pelo executor.** O Fundador decidiu **antes** da missao ministerial, no despacho de abertura da 1.13.4.5: **`CLAUDE.md` entra em `NAO_ACERVO`, pelo precedente de `.obsidian`** — *"declara-lo acervo obrigaria dar contrato `FND-10` a arquivo que a regra define como nao-acervo"*. Executado no **passo 6** de `§6.2`, na mesma passagem em que `products` entrou em `ACERVO`. **A decisao nasceu em despacho e passa a artefato aqui e em [PT-2026-015](relatorio-transicao-2026-08-01-aplicacao-nxtrack.md)** — a mesma forma pela qual `Q2` deixou de viver so em despacho. **O medidor voltou a medir**, e o portao **nao foi afrouxado**: a lista continua fechada e positiva, com uma entrada a mais de cada lado. **A recusa era o portao funcionando, nao falha** — e o mesmo mecanismo que `OA-1` de [`PS-2026-016 §6.2`](pacote-soberano-2026-08-01-nxtrack.md) preve para `products/`, que a missao de aplicacao **tera de declarar no passo 6**. **Nao para o nono ato**, porque `CA-2` e INFORMATIVO e nenhuma baseline e emitida no registro; **para o passo 7 da aplicacao**, e por isso os **dois** — `CLAUDE.md` e `products` — precisam ser resolvidos na mesma passagem. **O instrumento NAO foi editado nesta emissao:** editar o medidor sem autorizacao seria mover o numero para caber na escrita |
| 106 | **`RD-82` — o *Mapa do repositorio* do [`README` da raiz](../README.md) estava para tras em QUATRO linhas ao mesmo tempo.** Declarava **25** `ADR` *(sao **30**)*, **20** `RFC` *(sao **25**)*, **7** registros na camada `OPR` *(sao **9**)* e **18 `FIT` · 12 `PS` · 10 `PT`** *(sao **23 · 15 · 14**)*. **Medido ao acrescentar a linha de `memory/` que o nono ato obrigava** — nao ao ler a tabela | Achado **`RD-82`**, severidade **Media**, dono **DEP-GOV**, gatilho *"missao de catalogo"*. ✅ **Corrigido NA PROJECAO nesta emissao** *(`RG-03`, `PJ-03`, `M3`; **nenhuma fonte alterada**)*, com **todos os valores contados por ferramenta** e **nenhum obtido por soma sobre o valor anterior**. **A CAUSA fica ABERTA e sem missao designada:** e a mesma de `RD-57`, `RD-68`, `RD-69` e `RD-77` — **agregado de projecao que nenhum gatilho automatico alcanca**; `CV-04` so e cumprido quando alguem toca a tabela por outro motivo. **A conferencia devolveu um erro do proprio corretor, e ele esta declarado:** a primeira redacao desta correcao escreveu *"27 em `ativo`"* **por subtracao** *(30 menos os 3 `em-revisao`)*, e a contagem por `status` devolveu **26 `ativo` mais 1 `aprovado`** — `ADR-0006`. **Corrigido antes de gravar**, e registrado porque **numero derivado por aritmetica nao e numero contado** |
| 107 | **`RD-83` — a ancora `HEAD` de `CA-5` mede a arvore do TERCEIRO, nao o objeto consumido, e ja NAO reproduz.** `PS-2026-016 §2.2` publicou *"`tree` `b9b36be9…fb4b` e `HEAD` `b9fbccd…3bcb` identicos antes e depois"*, e o item **VI** do nono ato repete `HEAD` como ancora. **Medido nesta aplicacao, ANTES da primeira escrita:** o hospedeiro `lucaX` esta em `HEAD` **`6f81dfc9…`** — commit **`6f81dfc`, 2026-08-01 21:20:26**, *"docs(vslt): manual de teste e demonstracao"*, **fora do candidato** —, e `b9fbccd` era de **07:37:40**. **O que o ato consome REPRODUZ:** `tree(nxtrack)` = **`b9b36be9324ae2d36ddc4149049ebbff9f40fb4b`**, identico em `b9fbccd` **e** em `6f81dfc`, com `git status` da subarvore em **`0`** linhas. **`CA-5` esta CUMPRIDA** — a condicao, na forma escrita em `§6.1`, e *"nenhuma escrita da missao no repositorio de terceiro"*, e foram **`0`** | Achado **`RD-83`**, severidade **Media**, dono **DEP-GOV**, gatilho *"proxima passagem pelo portao de origem externa, ou missao que toque o molde de pacote soberano"*. ⚠️ **ABERTO. Congelamento em vigor: NAO gera missao.** **E a MESMA forma de `RD-79`, agora em `CA-5`:** ancora que mede **arvore inteira** — aqui a de um repositorio de terceiro **com escritor concorrente declarado** — em vez do **objeto consumido**. `RD-79` fixou a regra para condicao que meca o acervo; **ninguem a estendeu ao candidato**, e por isso o defeito renasceu no campo vizinho. **O objeto de commit da subarvore e a ancora que sobrevive ao repositorio vivo** — foi a propria 1.13.4.4 que o disse, e o pacote publicou `HEAD` ao lado dele assim mesmo |
| 108 | **`RD-84` — dois agregados de §2 divergem do que eles proprios enumeram.** *(a)* **`Artefatos em vigor por ato soberano` declarava `26` e enumerava `25`** — medido ao acrescentar os tres do nono ato, contando os identificadores da propria linha por ferramenta. *(b)* **`Cobertura de perfil_contexto` declara `208 de 208 — 100%` e aponta `§2.1`, cuja coorte declarada e `169`**, com o acervo medido em **217**: **tres numeros para a mesma medida**, no mesmo documento | Achado **`RD-84`**, severidade **Media**, dono **DEP-GOV**, gatilho *"missao de catalogo"*. ⚠️ **ABERTO.** *(a)* teve a **enumeracao recontada e publicada** — **28**, contada por ferramenta, com o rotulo anterior preservado no texto —, mas **qual dos dois estava certo NAO se decide aqui**: resolver exige auditar ato por ato, e isso e missao de catalogo, congelada. *(b)* **NAO foi tocado**: reconcilia-lo exige recomputar a particao de `§2.1` sobre a coorte inteira, que e o metodo que a propria secao declara — **e recomputa-la seria a missao ministerial refazendo catalogo**. **Familia de `RE-04`, `RD-42`, `RD-57` e `RD-67`:** agregado escrito como literal, nao derivado da tabela |
| 109 | **`RD-85` — `products/` nasce como raiz do acervo SEM indice de diretorio.** Todas as outras raizes tem `README` contador (`RG-04`); esta **nao tem**, porque a lista de reconciliacao de [`PS-2026-016 §3`](pacote-soberano-2026-08-01-nxtrack.md) enumera catalogo, **quatro** `README` e o da raiz, e **nao inclui um indice de `products/`** | Achado **`RD-85`**, severidade **Baixa**, dono **DEP-GOV**, gatilho *"missao de catalogo, ou segunda admissao de Produto — o que ocorrer primeiro"*. ⚠️ **ABERTO e deliberadamente NAO suprido.** **Cria-lo seria a missao ministerial criando artefato que o ato nao autorizou**, e mexendo por conta propria na contagem da baseline que o passo 7 mede. **A ausencia declarada custa menos que o artefato nao autorizado** |
| 110 | **`RD-86` — o candidato de Carta foi redigido para viver FORA do acervo, e o ato ordenou dois ajustes onde o arquivo aplicado exigiu cinco.** *(a)* `PS-2026-016 §3` manda `status: rascunho` → `ativo` e `ratificacao: pendente` → `ratificada`. **Aplicados so esses dois, o artefato entraria no acervo declarando de si**: *"CARTA CANDIDATA. NAO E ARTEFATO DO ACERVO"*, *"`products/` nao existe"*, *"nenhum Produto foi admitido"*, *"`ADR-0030` — `em-revisao`, nao vigente"* e *"Decisao do Soberano: PENDENTE"* — **cinco afirmacoes que o proprio ato torna falsas**, mais **um link relativo que so resolvia de fora do acervo**. *(b)* `TPL-carta-produto` **nao preve `Historico de versoes` na instancia**, secao que as **9** Cartas de Departamento carregam — a Carta de Produto nasce **sem lugar para registrar a propria emenda** | Achado **`RD-86`**, severidade **Media**, dono **DEP-PRD** *(autor do candidato)* com conformidade de **DEP-GOV**, gatilho *"proxima admissao de candidato como artefato, ou missao que toque `TPL-carta-produto`"*. ⚠️ **ABERTO.** *(a)* foi **tratado na aplicacao, por transformacao calculada e declarada** — instrumento `aplicar-carta.py`, **5** substituicoes literais, cada uma com motivo escrito, **abortando se qualquer uma nao casar exatamente uma vez**; o diff completo esta em [PT-2026-015](relatorio-transicao-2026-08-01-aplicacao-nxtrack.md). **Que o ato tenha previsto isso esta no proprio texto:** ele publicou `H-P` para `ADR-0030` e `RFC-0025`, cuja transformacao era determinada, e **para este objeto mandou a missao publicar o `H-A` do aplicado** — sinal de que o arquivo aplicado difere por mais que substituicao mecanica. *(b)* **NAO foi suprido:** acrescentar secao que o template nao preve seria a missao ministerial emendando a forma |
| 111 | **`RD-87` — tres indices foram EMENDADOS sem `versao` nova, e a deriva so aparece quando alguem os toca de novo.** Medido por `diff` entre **duas copias datadas do mesmo dia** — `_backups/…_2026-08-01_pre-missao-1-13-4-4` e `…_2026-08-01_pre-aplicacao-nxtrack`: [`decisions/README`](../decisions/README.md) **`1` linha alterada** com `versao` parada em **`1.9.0`** · [`rfcs/README`](../rfcs/README.md) **`1` linha** com `versao` em **`1.5.0`** · [`governance/fitness/README`](fitness/README.md) **`8` linhas** com `versao` em **`1.13.0`**. **`ADR-0009` define emenda como a alteracao que incrementa MAIOR ou MENOR** — e um indice que recebe linha nova de artefato foi emendado | Achado **`RD-87`**, severidade **Baixa**, dono **DEP-GOV**, gatilho *"missao de catalogo"*. ⚠️ **ABERTO quanto ao passado, e PARADO daqui em diante.** Esta emissao **bumpou os cinco indices que tocou** — `decisions/README` **1.10.0**, `rfcs/README` **1.6.0**, `governance/README` **1.15.0**, `fitness/README` **1.14.0** e o `README` da raiz **1.21.0** —, porque **emendar sem versionar CRIA a divergencia em vez de herda-la**: e literalmente o remedio que `RD-67` aplicou a este catalogo. **As emendas preteritas NAO foram renumeradas**: decidir entre renumerar o historico ou registrar salto e da **missao de catalogo**, congelada — a mesma escolha que `RD-70` deixou aberta. **Familia de `RD-67`, `RD-70` e `RD-78`:** artefato alterado sem versao. **`RD-78` e o caso extremo dela** — la os bytes originais nao existiam mais; aqui existem, nas copias datadas, e foi por isso que o `diff` foi possivel |
| 112 | **`RD-88` — a categoria de `Spec` sobre materia NAO-PRODUTO continua inexistente, e o fechamento de `RD-33` nao a cria.** E a **parte (b) de `RD-33`**, que **`S1` nao alcanca por construcao**: [`ADR-0021 §7.3`](../decisions/ADR-0021-framework-de-specifications.md) declara as duas saidas **disjuntas** — *"`S1` nao habilita o piloto interdepartamental e `S2` nao cria produto"* —, e **`S2` esta DEFERIDA** por decisao do proprio SOBERANO em `PT-2026-009 §1`, decisao **7**: *"Via futura e `S1` com Produto real (nXtrack); **`S2` deferida**"*. **Consequencia verificavel:** uma `Spec` sobre materia interdepartamental **continua sem caminho canonico** *(`FND-03 §3.6` e `FND-10 §4.4` so preveem `products/<slug>/specs/`)* **e sem pre-condicao satisfazivel** *(`FND-04 §6` exige *"Produto existe"*, e materia interdepartamental **nao tem produto**)*. **Nasce por MIGRACAO, nunca por descoberta:** o enunciado ja vivia dentro de `RD-33` desde 2026-07-29, e **fechar `RD-33` inteiro teria afirmado que `S2` ocorreu** | Achado **`RD-88`**, severidade **Media** *(era **Alta e bloqueante** enquanto vivia dentro de `RD-33`; **deixa de bloquear** porque **nenhuma `Spec` interdepartamental e demandada** — `PILOTO-DEFERIDO` e a materia da primeira `Spec` esta fixada pelo ato em `LM-6(a)`, que e **de produto**)*, dono **SOBERANO** *(so `S2` a resolve, e `S2` e `C3`)*, gatilho *"primeira demanda real de `Spec` sobre materia nao-produto, ou missao que retome o piloto de `PILOTO-DEFERIDO`"*. ⚠️ **ABERTO. Congelamento em vigor: NAO gera missao.** [PT-2026-016 §4.2](relatorio-transicao-2026-08-01-fechamento-rd-33.md) |
| 113 | **`RD-89` — duas entradas de §7 deste catalogo viviam na MESMA linha fisica.** As entradas **110** *(`RD-86`)* e **111** *(`RD-87`)* estavam separadas por `\|\| 111 \|` **sem quebra de linha**, e por isso a **111 nao renderizava como linha de tabela**: o registro inteiro de `RD-87` ficava **dentro da celula** de `RD-86`. **O achado existia no arquivo e nao existia na tabela** | Achado **`RD-89`**, severidade **Baixa**, dono **DEP-GOV**, gatilho *"missao de catalogo"*. ✅ **CORRIGIDO NA PROJECAO nesta emissao** — **uma quebra de linha inserida**, `0` caracteres de conteudo alterados, `0` celulas movidas, `0` valores tocados (`PJ-03`, `RG-03`, `M3`). **A causa fica registrada aqui, e nao so o valor:** corrigir valor sem registrar causa foi o que fez `RD-32` e `RD-58` reincidirem. **Encontrado ao CONTAR as entradas de §7 por ferramenta**, nao ao le-las — quarta ocorrencia da familia de [MEM-APR-0006](../memory/aprendizado/MEM-APR-0006-exercer-o-contador-revela-o-defeito.md) |
| 114 | **`RD-90` — os ponteiros de sucessao entre baselines de §10.0.x apontam para a subsecao ERRADA em 26 de 31 casos.** Medido por ferramenta **antes** de qualquer edicao desta emissao: um mapa `identificador → subsecao onde ele vive` foi construido a partir dos proprios cabecalhos, e cada campo *Supera* e *Superada por* foi confrontado com ele. **`5` corretos · `26` divergentes · `31` no total.** **O padrao e deterministico e a causa e unica:** cada emissao nova **renumera os cabecalhos `§10.0.x`** e **nao renumera os ponteiros dentro das tabelas**. Por isso **11** campos *Superada por* dizem **`§10.0`** — que hoje e uma baseline **completamente diferente** daquela a que se referiam — e os demais estao deslocados pelo acumulo. **Quem seguir o ponteiro chega ao registro errado**, e o texto ao lado nao denuncia o erro porque **o identificador esta certo e so a secao esta errada** | Achado **`RD-90`**, severidade **Media**, dono **DEP-GOV**, gatilho *"missao de catalogo"*. ⚠️ **ABERTO, e deliberadamente NAO varrido.** **`BL-02` proibe editar baseline**, e a unica excecao que a convencao abriu e o **campo *Superada por* do par de sucessao** — que esta emissao preencheu, e so ele. Varrer **26** ponteiros em **15** tabelas historicas e **missao de catalogo**, congelada, e e a mesma escolha que `RD-70`, `RD-84` e `RD-87` deixaram aberta. **A alternativa estrutural — substituir o ponteiro numerico por remissao ao identificador, que nao envelhece — e correcao de CAUSA e nao de valor**, do tipo que `RD-35` aplicou a enumeracao de `OPR`; decidi-la tambem e da missao de catalogo. **Encontrado ao construir o mapa por ferramenta para renumerar com seguranca** — ler as tabelas nao revelaria, porque **cada linha, isolada, parece correta**: e a quinta ocorrencia da familia de [MEM-APR-0006](../memory/aprendizado/MEM-APR-0006-exercer-o-contador-revela-o-defeito.md) e a **decima sexta** de [MEM-APR-0002](../memory/aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md) |
| 115 | **`RD-91` — a coluna `C1 · T2` de `SF-10` produz aprovacao NULA para todo artefato `SPC`, e o piso que `FND-04 §6` fixa e portanto INUTILIZAVEL.** Para `SPC`, [`FND-09 §8.2`](../foundation/09-meta-model.md) poe **DEP-PRD** como quem **propoe/cria** e como quem **aposenta** *(logo, proprietario)*; a coluna `C1 · T2` de [`FND-11 §5`](../foundation/11-framework-specifications.md) poe *Aprovacao* = **proprietario + revisor**; e [`FND-04 §3.1`](../foundation/04-governanca.md) declara, em termos absolutos, *"`Proponente ≠ Aprovador` (PI-05)"* e *"Acumulo indevido de papeis torna a aprovacao **nula** (`LV-03`)"* — sendo `LV-03` **Linha Vermelha de `FND-01`, nivel 1** da hierarquia normativa. **A coluna `C0 · T2` colapsa pela identica razao.** **Consequencia verificavel por terceiro, lendo duas linhas de fontes vigentes: `C2` e a MENOR classe da matriz em que uma `Spec` pode ser validamente aprovada** | Achado **`RD-91`**, severidade **Alta** *(**nao bloqueante**: `C2` contorna, e o contorno esta **exercido** em `SPC-001`)*, dono **SOBERANO** — sanar exige emendar `FND-11`, e `FND` **nao vigora sem ratificacao** (`LM-02`; `FND-09 §8.2` linha `FND`) —, gatilho *"proxima emenda de `FND-11`, ou segunda `Spec` real"*. **Encontrado por EXERCER a matriz de autoridade, nunca por le-la** — terceira ocorrencia do padrao de `MEM-APR-0005` e `MEM-APR-0006`. ⚠️ **ABERTO. Congelamento em vigor: NAO gera missao.** [PT-2026-017 §6.2](relatorio-transicao-2026-08-02-primeira-spec.md) · [ADR-0031 §6](../decisions/ADR-0031-primeira-spec-governanca-de-dado-pessoal-do-nxtrack.md) |
| 116 | **`RD-92` — DEP-QAR acumula custodiante da materia e revisor do tipo na mesma mudanca.** Custodiante de `SPC-001` por ser **custodio de `CAP-juridico`** (`SF-07`); revisor por `FND-09 §8.2` linha `SPC`. **Os dois papeis NAO constam de `FND-04 §3.1` como incompativeis** — e por isso a aprovacao **nao e nula** —, mas a independencia e **menor do que a tabela sugere**, e a diferenca nao estava escrita em lugar nenhum | Achado **`RD-92`**, severidade **Baixa**, dono **DEP-GOV**, gatilho *"segunda `Spec` custodiada por DEP-QAR"*. **Declarado pelo proprio DEP-QAR** em [RFC-0026 §10](../rfcs/RFC-0026-primeira-spec-governanca-de-dado-pessoal-do-nxtrack.md), como ressalva a propria manifestacao de apoio. ⚠️ **ABERTO, sem missao.** |
| 117 | **`RD-93` — `TPL-spec` 1.1.0 declara TRES campos de frontmatter que nenhuma fonte preve para `Spec`, e isso contradiz `SF-05`.** [`FND-03 §4.1`](../foundation/03-taxonomia.md) da a `Spec` **dois** campos extras — `produto` e `criterios_aceite_count` — e **`SF-06` reproduz exatamente esses dois**. O esqueleto de [`TPL-spec`](../foundation/templates/TPL-spec.md) traz **cinco**: acrescenta `classe_mudanca` e `tipo_decisao` *(previstos por `FND-03 §4.1` para **`ADR`**)* e `capabilities` *(previsto para Departamento, agente, subagente, skill, workflow, produto, projeto e ferramenta — **`Spec` NAO esta na lista**)*. **`SF-05` afirma *"nenhum campo novo e criado por este Framework (`AC-07`)"***, e a afirmacao nao se sustenta contra o template que `SF-32` declara canonico. **`SPC-001` seguiu o TEMPLATE**, e a divergencia fica **declarada**, jamais resolvida por escolha do autor | Achado **`RD-93`**, severidade **Media**, dono **DEP-PRD** *(dono do tipo e mantenedor de `TPL-spec` — `FND-09 §8.2` linha `TPL`)*, com **DEP-GOV** *(aprova template)*, gatilho *"proxima emenda de `TPL-spec` ou de `FND-03 §4.1`"*. **Corrigir e mudanca `C2` com rito proprio; o congelamento veda abrir missao.** ⚠️ **ABERTO.** |
| 118 | **`RD-94` — `SF-07` exige *"exatamente uma `Capability`"*, e a materia da primeira `Spec` atravessa TRES.** `LM-6(a)` toca **`CAP-juridico`** *(norma externa — `RQ-3`, `RQ-4`)*, **`CAP-seguranca`** *(`RQ-5`, `RQ-6`)* e **`CAP-dados`** *(`RQ-1`, `RQ-2`)*. A escolha de `CAP-juridico` foi **determinada positivamente** — e a unica cujo escopo declarado diz *"reconhecer obrigacao externa aplicavel"* —, e **nao por eliminacao**; mas a regra **obriga a apagar dois vinculos verdadeiros**, enquanto `VC-01` proibe elo que nao corresponde. **E o mesmo padrao que `VC-03` ja sinalizara no proprio Produto** *(`RD-74`, cinco Capabilities)*, agora um nivel abaixo | Achado **`RD-94`**, severidade **Media**, dono **DEP-PRD**, gatilho *"segunda `Spec` cuja materia atravesse mais de uma `Capability`"*. **Familia de `RD-74`.** ⚠️ **ABERTO, sem missao.** |
| 119 | **`RD-96` — `FND-09 §8.2`, linha `PRJ`, poe `DEP-EXE` como quem PROPOE e como quem APROVA.** `Proponente = Aprovador` **incondicional**: ao contrario das linhas cujo proponente e variavel *(`qualquer DEP`, `quem detecta`, `DEP de origem`)*, **nao existe atribuicao conforme possivel** — e `FND-04 §3.1` torna **nula** (`LV-03`) toda aprovacao de `Projeto`. **E o mesmo defeito de `RD-91`, fora de `SPC`, e nenhum achado anterior o registrava.** Encontrado por varrer a **coluna** e nao a **celula**, durante o Item 0 da Missao 1.13.5.1 | Achado **`RD-96`**, severidade **Alta** *(**nao bloqueante**: `0` `PRJ` existem no acervo)*, dono **SOBERANO** — sanar exige emendar `FND-09`, e `FND` nao vigora sem ratificacao (`LM-02`) —, gatilho *"antes do primeiro `PRJ`, ou proxima emenda de `FND-09 §8.2`"*. **NAO corrigido por `ADR-0032`, e a razao esta escrita:** a largura da emenda e decisao do Soberano, submetida como `Q1` de [PS-2026-017 §7](pacote-soberano-2026-08-02-rd-91.md). ⚠️ **ABERTO. Congelamento em vigor: NAO gera missao.** [PT-2026-018 §2.2](relatorio-transicao-2026-08-02-emenda-sf-10.md) |
| 120 | **`RD-97` — `FND-09 §8.2`, linha `TPL`, poe `DEP-GOV` como quem PROPOE, quem REVISA e quem APROVA.** Tres papeis no mesmo nome, e a linha fere **duas** regras de `FND-04 §3.1` de uma vez: *"Proponente ≠ Aprovador"* e *"Proponente ≠ Revisor"* (`PI-05`), mais **`ES-02`** *(Guardiao ≠ Proponente)*. **Ja ocorreu na pratica, e esta registrado:** `TPL-carta-produto` **1.1.0** foi emendado na Missao 1.13.4.1 com **DEP-GOV como autor e como aprovador** | Achado **`RD-97`**, severidade **Alta**, dono **SOBERANO**, gatilho *"proxima emenda de template"* — **o mesmo gatilho de `RD-63`, que ja disparou duas vezes**. **NAO corrigido por `ADR-0032`** *(`Q1` de `PS-2026-017 §7`)*. **Leitura alternativa declarada, e ela nao salva a linha:** se *"dono do tipo"* fosse o proponente real e DEP-GOV so validasse forma, `ES-02` continuaria ferido, porque a coluna *Propoe/cria* **nomeia DEP-GOV**. ⚠️ **ABERTO, sem missao.** [PT-2026-018 §2.2](relatorio-transicao-2026-08-02-emenda-sf-10.md) |
| 121 | **`RD-98` — a partir de `FND-11` 1.1.0 a matriz de `SF-10` difere em UMA celula da copia de `ADR-0021 §5.3`**, que e artefato **`M1`** e **nunca se emenda** (`AC-10`, `CC-01`). Prevalece `FND-11`, por [ADR-0022 §5.4](../decisions/ADR-0022-sede-canonica-do-framework-de-specifications.md) — **mas quem resolver autoridade pela copia obtem o valor SUPERADO**, e nada no texto de `ADR-0021` avisa | Achado **`RD-98`**, severidade **Media**, dono **DEP-GOV**, gatilho *"apos o ato que promulgar `FND-11` 1.1.0"*. **Declarado no proprio candidato**, em `FND-11 §2`, nota de alcance temporal — **nunca silencioso**. **Consequencia estrutural de promover norma de `M1` para `M2`**, prevista em `ADR-0022` e agora **realizada pela primeira vez**. ⚠️ **ABERTO, sem missao.** |
| 122 | **`RD-99` — `FND-04 §2`, bloco `C3`, manda registrar *"nova versao MAIOR do documento"*, e as emendas `C3` exercidas produziram versao MENOR.** `ADR-0017` levou `FND-09` a **1.4.0**; `ADR-0019`, a **1.5.0**; `ADR-0022` levou `FND-01` a **1.6.0**; `ADR-0024`, a **1.7.0** — **quatro emendas `C3`, quatro incrementos MENORES**, porque `AL-01`/`CC-02` fazem a versao seguir **o efeito**, nao a classe. **Conflito DENTRO de `FND-04`**, entre `§2` e a regra de versionamento que ele proprio remete | Achado **`RD-99`**, severidade **Media**, dono **DEP-GOV**, gatilho *"proxima emenda a `FND-04`"* — **o mesmo de `RD-18`, que segue aberto**. **`ADR-0032` seguiu a pratica exercida** *(MENOR)* **e declarou a divergencia em vez de a resolver em silencio**; submetida como `Q3` de [PS-2026-017 §7](pacote-soberano-2026-08-02-rd-91.md). ⚠️ **ABERTO, sem missao.** |
| 123 | **`RD-100` — `FND-11 §14`, limites `L1` e `L2`, ficaram FALSOS em 2026-08-02 e continuam no texto.** `L1` diz *"**Nenhuma `Spec` real existe.** Todas as **32** regras sao determinadas, nao observadas"* e `L2` diz *"o valor sera medido na **primeira `Spec`**"*. `SPC-001` existe desde 2026-08-02, e `SF-09` foi medido em **603** linhas por `FIT-2026-024`. **A emenda de `ADR-0032` NAO os corrige** — nao sao a celula autorizada, e corrigi-los aqui seria carona silenciosa num ato alheio | Achado **`RD-100`**, severidade **Baixa**, dono **DEP-GOV**, gatilho *"proxima emenda de `FND-11`"*. **Declarado, nao corrigido**, pela mesma razao que manteve *"fase futura"* nas duas Cartas: **o que ja era falso antes da emenda nao se corrige de carona nela**. ⚠️ **ABERTO, sem missao.** [PT-2026-018 §7](relatorio-transicao-2026-08-02-emenda-sf-10.md) |

## 8. Manutencao

| Quando | O que fazer |
|---|---|
| Ao criar artefato | Acrescentar linha com tipo, entidade, perfil, custo medido e resumo (RG-02) |
| Ao encerrar mudanca C2/C3 | Verificar sincronia; desatualizado = mudanca incompleta (RG-03) |
| Ao superar ou revogar | Atualizar §6, nunca apagar a linha |
| Ao admitir conteudo externo | Registrar a proveniencia em §9 e o ADR de admissao (ADR-0007 §5.3) |
| Na revisao estrutural | Recalcular custos, reavaliar perfis e **emitir nova baseline** (§10) |

## 9. Proveniencia — fronteira greenfield / legado

**Fonte da regra e do vocabulario:** [ADR-0007 §5.5](../decisions/ADR-0007-fronteira-greenfield-legado.md).
Esta secao e **projecao** dela (PJ-02): campos projetados — os cinco valores e o padrao;
finalidade — dizer, sem abrir o artefato, se ele nasceu aqui; atualizacao — pelo ADR de
admissao de cada candidato (CV-04).

| Proveniencia | Artefatos | Quais |
|---|---|---|
| `native` | **223** | **Todo o acervo.** Produzido dentro do LucaX Enterprise OS — **inclusive [`PRO-nxtrack`](../products/nxtrack/carta.md)**, o primeiro Produto, e **[`SPC-001`](../products/nxtrack/specs/SPC-001-governanca-de-dado-pessoal-do-nxtrack.md)**, a primeira `Spec`: os dois foram **escritos neste sistema**, e por isso a admissao de um candidato externo produziu artefato **`native`**, jamais `adapted` ou `migrated` |
| `legacy-candidate` | **2 nomeados, `0` no acervo — e um deles ADMITIDO POR IDENTIDADE, sem que um byte entrasse** | **`medAlly`** — `E:/LucasIA/Projetos/lucaX/My_WorkSpace/Meus_projetos/medally`, **550** arquivos, `HEAD` `e4458f29…9e95c`. **Nomeado em 2026-07-31 e submetido ao portao.** · **`nXtrack`** — `E:/LucasIA/Projetos/lucaX/My_WorkSpace/Meus_projetos/nxtrack`, **183** arquivos rastreados *(+ **13.182** ignorados, **nao consumidos**)*, **congelado no objeto `tree` `b9b36be9…fb4b`** desde `2026-07-27T18:20:33`. **NAO tem repositorio proprio: e subarvore de `lucaX`** *(achado `RD-71`)*. **Nomeado em 2026-08-01 e submetido ao portao.** Candidato **nao** e artefato do acervo, **nao tem ID de sequencia e nao ocupa entrada de catalogo** (`FR-10`) |
| `adapted` | 0 | — |
| `migrated` | 0 | — |
| `rejected` | 0 | — |

> **Custo de migracao: zero.** `native` e o valor padrao (FR-09, AC-07) e vive **no catalogo**
> (L2 curado), nunca no frontmatter — **nenhum dos 223 arquivos foi tocado** para
> receber proveniencia. *(A contagem declarava **169** ate 2026-07-31 — tres missoes de atraso,
> achado `RD-57`.)*

> **`FR-08` cumprido pela SEGUNDA vez, e desta vez com ato.** O portao terminou com **`0` bytes
> do candidato no acervo**, e o que entrou foi **identidade**: a Carta `PRO-nxtrack`, `native`.
> **O repositorio do nXtrack permanece NAO admitido e NAO inventariado** — `LA-1` e `LA-2` de
> [`PS-2026-016 §6.3`](pacote-soberano-2026-08-01-nxtrack.md) —, e cada peca dele que um dia
> queira entrar tera **portao proprio** (`FR-07`, `AD-02`). **O candidato saiu intacto:**
> `tree(nxtrack)` = `b9b36be9…fb4b`, identico antes e depois, `git status` da subarvore em **`0`**
> linhas. **O `HEAD` do hospedeiro andou por trabalho de terceiro, fora do candidato** — achado
> **`RD-83`**, §7, que e por isso que a ancora e o `tree` da subarvore e nao o `HEAD` da arvore alheia.

> **O portao foi exercido, e o resultado foi `REWRITE`: `0` bytes entraram** — e, **desde 2026-07-31,
> esse registro le-se `G3` = `RECOGNIZE` com `G0` = `IDENTIDADE`**, por `RC-1` de `ADR-0027`, **em vigor
> pelo oitavo ato**. **O efeito registrado NAO muda** (`RC-3`): seguem `0` bytes admitidos e proveniencia
> `native`. O medAlly e o
> **primeiro `legacy-candidate` da historia do acervo**, e a sua admissao — se o ato ocorrer —
> **nao produz artefato `migrated` nem `adapted`**: produz **um artefato `native`**, a Carta,
> escrita neste sistema do zero. **`FR-08` cumprido de propria mao:** o portao terminou sem que
> nada entrasse, e **isso e sucesso do portao, nao falha**. **O conteudo do repositorio
> permanece nao admitido**, e cada peca dele que um dia queira entrar tera **portao proprio**
> (`FR-07`) — [ADR-0026 §5](../decisions/ADR-0026-admissao-do-medally-como-primeiro-produto.md).

> **A Missao 1.13 leu evidencia externa e nao a admitiu — e por isso esta tabela nao muda.**
> **236 de 33.676 linhas** de `_SAIDA-COMPANY-OS/09_PACOTE-DE-INTEGRACAO/` foram lidas
> *(**0,70%**, consumo seletivo determinado pela missao)*. **`0` bytes copiados · `0` formatos
> importados · `0` candidatos nomeados**, e **duas praticas fortes foram recusadas com norma
> citada** — [ADR-0021 §8.2](../decisions/ADR-0021-framework-de-specifications.md). **`FR-04`
> distingue consultar de importar**, e isto foi consulta: o pacote permanece
> **`external-evidence`, provisorio, nao normativo e nao adotado**, com **`ADOPT = 0`** declarado
> na propria fonte. **Nenhum artefato passou a `legacy-candidate`**, porque candidato exige
> **nomeacao e portao de admissao** (`FR-10`, `ADR-0007 §5.3`), e nenhum foi pedido.

> **CT-11 nao altera esta tabela.** MEM-EST-0001 invoca duas fontes **externas ao acervo**
> (F9 e F10 do proprio registro), mas o **artefato** e `native`: foi produzido aqui. Fonte de
> evidencia externa nao muda proveniencia — FR-04 distingue **consultar** de **importar**, e
> nada foi importado.

> **O portao foi exercido uma SEGUNDA vez, e a segunda foi a primeira sob a norma emendada.**
> Missao 1.13.4.4, sobre o **nXtrack**: **`G0` = `IDENTIDADE`** e **`G3` = `RECOGNIZE`** —
> **primeira aplicacao PROSPECTIVA da classe**, onde `RC-1` foi retrospectiva. **`0` bytes
> admitidos**, e desta vez a afirmacao esta **medida**: **179** hashes distintos dos 183
> arquivos rastreados do candidato foram confrontados com **todos** os arquivos do acervo, e
> houve **`0` colisoes**. A admissao, **se o ato ocorrer**, produz **um artefato `native`** — a
> Carta `PRO-nxtrack`, escrita neste sistema do zero —, e **nao produz `migrated` nem
> `adapted`**. **O conteudo do repositorio permanece nao admitido**, e cada peca dele que um dia
> queira entrar tera **portao proprio** (`FR-07`, `AD-02` de
> [ADR-0030 §5.3](../decisions/ADR-0030-admissao-do-nxtrack-como-primeiro-produto.md)) —
> [PT-2026-014 §3](relatorio-transicao-2026-08-01-portao-nxtrack.md).

> **`FR-04` foi exercido de propria mao, e a fronteira esta escrita.** As **17** fontes do
> nXtrack que sustentam o fit-gap e a Carta foram **lidas, congeladas por hash e citadas** — e
> isso e **consulta**, que `G1` e `G2` **exigem**. **Nenhum arquivo foi proposto como artefato**,
> e por isso **nenhum foi avaliado** como `ADOPT`, `ADAPT`, `REWRITE` ou `RETIRE`. É a diferenca
> que `GA-03` protege, e ela foi declarada **antes** de alguem perguntar.

> **O LucaX Legacy nao aparece neste catalogo, e isso e correto.** Ele nao e acervo: e sistema
> externo (ADR-0007 §5.1). Inventaria-lo aqui violaria FR-07. Esta tabela registra o que
> **entrou**, nao o que existe do outro lado da fronteira.

## 10. Baseline canonica

**Projecao do catalogo, nao entidade nova** (RG-07). Nenhum arquivo por artefato (RG-05).

### 10.0 Baseline vigente

| Campo | Valor |
|---|---|
| **Identificador** | **BL-2026-08-02-02** |
| Data | **2026-08-02** |
| Marco | **A EMENDA QUE SANA `RD-91` EXISTE, E NAO FOI APLICADA.** A **Missao 1.13.5.1** produziu o rito `C3` completo — [RFC-0027](../rfcs/RFC-0027-separacao-de-proponente-e-aprovador-na-spec-c1.md) → [ADR-0032](../decisions/ADR-0032-separacao-de-proponente-e-aprovador-na-spec-c1.md) → [FIT-2026-025](fitness/FIT-2026-025-emenda-de-sf-10.md) → [PS-2026-017](pacote-soberano-2026-08-02-rd-91.md) → [PT-2026-018](relatorio-transicao-2026-08-02-emenda-sf-10.md) — para fazer a aprovacao de `Spec` `C1` passar do **proprietario**, que e quem a propoe, para **DEP-EXE**. **O Item 0 mediu antes de emendar e mudou a sede da emenda:** a celula que `RD-91` nomeava, em `FND-11 §5`, **reproduz literalmente** `FND-09 §8.2` linha `SPC` e `FND-04 §2.1` linha `C1` — e por `PJ-03` com `FND-01 §10` emendar so a projecao **nao sanaria**. A varredura das **21** linhas de `FND-09 §8.2` achou o **mesmo colapso** em **`PRJ`** e **`TPL`**, **fora de `SPC`** |
| Artefatos | **228** — **`+5`** sobre `BL-2026-08-02-01`: `RFC-0027`, `ADR-0032`, `FIT-2026-025`, `PS-2026-017` e `PT-2026-018`. **`0` removidos** |
| Linhas | **67.279** |
| Estado normativo | **A camada normativa NAO mudou. `0` fontes alteradas** — `FND-01` a `FND-11`, as **23 `CAP`**, os **19 `TPL`**, as **9 Cartas de Departamento** e a **Carta de Produto** estao **identicos**. As **4** versoes candidatas — `FND-09` **1.6.0**, `FND-11` **1.1.0**, Cartas `DEP-PRD` e `DEP-EXE` **1.2.0** — vivem **fora do acervo**, com `H-A`, `H-N` e `H-P` publicados em [PS-2026-017 §3](pacote-soberano-2026-08-02-rd-91.md) |
| Ratificacao | **Nenhum ato soberano foi emitido nem consumido — seguem `9` `MSG`, inalterados.** A minuta esta **redigida e NAO emitida** em `PS-2026-017 §6`. **Fila de retidos por falta de ato: `3`** — `ADR-0026`, `ADR-0028` e agora **`ADR-0032`** *(`aprovado` · `ratificacao: pendente`)*. **`E2`, `Q3`, `Q4`, `RD-88` e `RD-90` intactos** |
| Proveniencia | **228** `native`, **`0`** externos admitidos. **`1` Produto · `1` `Spec` · `1` `legacy-candidate` ainda nao admitido** *(medAlly)*. **`0` bytes escritos no repositorio do candidato** |
| Supera | **`BL-2026-08-02-01`** — §10.0.1 |
| Superada por | *(nenhuma — esta e a baseline vigente)* |
| Evidencia de integridade | §**10.22**. **§10.0.1 a §10.21 nao foram editadas** (`BL-02`), exceto o campo *Superada por* de `BL-2026-08-02-01`, que e o par de sucessao |

### 10.0.1 Baseline superada nesta emissao — `BL-2026-08-02-01`, com os valores ORIGINAIS

| Campo | Valor |
|---|---|
| **Identificador** | **BL-2026-08-02-01** |
| Data | **2026-08-02** |
| Marco | **A PRIMEIRA `Spec` DO ACERVO EXISTE.** A **Missao 1.13.5** criou [`SPC-001`](../products/nxtrack/specs/SPC-001-governanca-de-dado-pessoal-do-nxtrack.md), sobre a lacuna **`LM-6(a)`** de `PRO-nxtrack` — materia que o **nono ato** fixou *"com prioridade sobre as demais de `LA-7`"*. **`GO-TO-SPECS` passa de *exercivel* a EXERCIDO.** O tipo documental `Spec` e a entidade `SPC` saem de *sem instancia*, e **nenhum dos dois foi criado**: constam de `FND-10 §4.4` e `FND-09 E-19` desde a fundacao. **O limite `L1` de `FND-11 §14` cai** — as 32 regras deixam de ser *determinadas e nao observadas* —, e o **gatilho de revisao de `FND-11 §15` disparou**: `PT-2026-017 §6` mede **22** exercidas sem ressalva, **4** com insuficiencia, **1** defeituosa e **5** nao exercidas. **`0` atos emitidos, `0` fontes emendadas** |
| Artefatos | **223** — **`+5`** sobre `BL-2026-08-01-03`: `RFC-0026`, `ADR-0031`, **`SPC-001`**, `FIT-2026-024` e `PT-2026-017`. **`0` removidos** |
| Linhas | **66.100** |
| Estado normativo | **A camada normativa NAO mudou. `0` fontes alteradas** — `FND-01` a `FND-11`, as **23 `CAP`**, os **19 `TPL`**, as **9 Cartas de Departamento** e a **1 Carta de Produto** com **`0` bytes**, conferidos contra o `H-A` do ponto de partida. **`0` bytes em `TPL-spec`**, apesar de `RD-93` te-lo por defeituoso: emenda-lo e `C2` com rito proprio, e o congelamento veda abrir missao. Criados: **5**. Reconciliadas na **mesma mudanca**: catalogo *(§2, §4.2, §4.5, §4.7, **§4.8 nova**, §5, §7, §9, §10)*, `README` da raiz, `decisions/README`, `rfcs/README`, `governance/README`, `governance/fitness/README` e o roadmap |
| Ratificacao | **Nenhum ato soberano foi emitido nem consumido — seguem `9` `MSG`, inalterados.** `ADR-0031` e **`C2 · Tipo 2`**, classe que **nao exige ratificacao** (`FND-04 §2.1`); `LM-02` alcanca `C3` e `Tipo 1`. **Fila de retidos por falta de ato: `2`**, inalterada — `ADR-0026` e `ADR-0028`. **`E2`, `Q3`, `Q4` e `RD-88` intactos.** **O que espera o Fundador e `RD-91`**, cujo dono e o SOBERANO por construcao: sanar a coluna `C1 · T2` de `SF-10` exige emendar `FND-11`, e `FND` nao vigora sem ratificacao |
| Proveniencia | **223** `native`, **`0`** externos admitidos. **`1` Produto · `1` `Spec` · `1` `legacy-candidate` ainda nao admitido** *(medAlly)*. **`0` bytes escritos no repositorio do candidato**, **`0` bancos abertos**, **`0` execucoes** — a consulta se deu sobre o `tree` `b9b36be9…fb4b`, que **reproduz** o ancorado na Carta |
| Supera | **`BL-2026-08-01-03`** — §10.0.1 |
| Superada por | **`BL-2026-08-02-02`** — §10.0. **Unico campo tocado nesta baseline** (`BL-02`): e o par de sucessao, e nada mais |
| Evidencia de integridade | §**10.21**. **§10.0.1 a §10.20 nao foram editadas** (`BL-02`), exceto o campo *Superada por* de `BL-2026-08-01-03`, que e o par de sucessao, e a **renumeracao de §10.0.x** — que desloca subsecao, **nunca valor**. **`RD-90` continua ABERTO e deliberadamente NAO varrido** |

### 10.0.2 Baseline superada em emissao anterior — `BL-2026-08-01-03`, com os valores ORIGINAIS

| Campo | Valor |
|---|---|
| **Identificador** | **BL-2026-08-01-03** |
| Data | **2026-08-01** |
| Marco | **O ACERVO SEM PENDENCIA BLOQUEANTE — pela primeira vez desde 2026-07-29.** A **Missao 1.13.4.6** fechou **`RD-33`** por rito **MINISTERIAL**, determinado **antes** de exercido e fundado em `PA-01`, `PA-03`, `PA-07` e `PA-13` de [ADR-0020](../decisions/ADR-0020-regime-ministerial-de-promulgacao-e-ativacao.md), `AU-06`, `FND-04 §4 [7]` e `RG-01`/`RG-03`/`RG-04`/`AC-09` de `FND-10`. **A reserva do item VII do nono ato e de `LA-3` era TEMPORAL e DE SEDE, nunca de classe de rito.** **`GO-TO-SPECS` passa de *liberado e nao exercivel* a EXERCIVEL**, provado **por exercicio** do `DoR` de `SF-23`, item **(9)**. **`0` atos emitidos, `0` fontes emendadas, `0` `Spec`s criadas** |
| Artefatos | **218** — **`+1`** sobre `BL-2026-08-01-02`: [`PT-2026-016`](relatorio-transicao-2026-08-01-fechamento-rd-33.md), o instrumento de fechamento. **`0` removidos** |
| Linhas | **64.383** |
| Estado normativo | **A camada normativa NAO mudou. `0` fontes alteradas** — `FND-01` a `FND-11`, as **23 `CAP`**, os **19 `TPL`**, as **9 Cartas de Departamento** e a **1 Carta de Produto** com **`0` bytes**, conferidos contra o `H-A` do ponto de partida. **`0` bytes nas TRES fontes que vinculam `Spec` a `Produto`** — `FND-04 §6`, `FND-03 §3.6` e `FND-10 §4.4`: o vinculo **nao foi removido nem afrouxado, foi SATISFEITO**. **`0` `ADR` e `0` `RFC` alterados** — nenhuma transicao `O4` nesta missao. Criado: **1** — `PT-2026-016`. Reconciliadas: as projecoes `M3` de `CV-04` — catalogo, `governance/README`, `foundation/README`, `decisions/README` e o `README` da raiz |
| Ratificacao | **Nenhum ato soberano foi emitido nem consumido — seguem `9` `MSG`, inalterados.** A missao **executa autoridade ja exercida** (`PA-01`), e por isso **nao precisa de ato novo**: `S1` foi consumida no nono ato e aplicada pela 1.13.4.5. **Fila de retidos por falta de ato: `2`**, inalterada — `ADR-0026` e `ADR-0028`. **Fila por falta de aplicacao: `0`**. **`E2` ADIADA e intacta:** `RFC-0023`, `ADR-0028` e `FIT-2026-021` com **`0` bytes**. **`Q3` e `Q4` seguem NAO respondidas.** **`RD-33` ✅ FECHADO**, e o residuo **(b)** — a `Spec` de materia nao-produto, que so `S2` cria — **migrou para `RD-88`, ABERTO** |
| Proveniencia | **218** `native`, **`0`** externos admitidos. **`1` Produto em vigor**, **`0` `Spec`s criadas**, **`1` `legacy-candidate` ainda nao admitido** *(medAlly)*. **`0` bytes escritos em `products/`** e **`0` acessos ao repositorio do candidato** nesta missao |
| Supera | **`BL-2026-08-01-02`** — §10.0.1 |
| Superada por | **`BL-2026-08-02-01`** — §10.0. **Unico campo tocado nesta baseline** (`BL-02`): e o par de sucessao, e nada mais |
| Evidencia de integridade | §**10.20**. **§10.0.1 a §10.19 nao foram editadas** (`BL-02`), exceto o campo *Superada por* de `BL-2026-08-01-02`, que e o par de sucessao, e a **renumeracao de §10.0.x** — que desloca subsecao, **nunca valor**. **A divergencia acumulada dos ponteiros de sucessao foi MEDIDA e NAO varrida** — achado **`RD-90`** |

### 10.0.3 Baseline superada em emissao anterior — `BL-2026-08-01-02`, com os valores ORIGINAIS

| Campo | Valor |
|---|---|
| **Identificador** | **BL-2026-08-01-02** |
| Data | **2026-08-01** |
| Marco | **O PRIMEIRO PRODUTO DO ACERVO, E O NONO ATO SOBERANO CONSUMIDO.** A **Missao 1.13.4.5** aplicou [MSG-2026-0009](../memory/operacional/MSG-2026-0009-ato-soberano-admissao-do-nxtrack.md) na ordem de [`PS-2026-016 §6.2`](pacote-soberano-2026-08-01-nxtrack.md): **`ADR-0030` `ativo` · `ratificada`**, **`RFC-0025` `aprovado`** *(pela **variante**, porque o ciclo de `RFC` termina em `aprovado`)* e **`PRO-nxtrack` CRIADO** em `products/nxtrack/carta.md`. **`products/` nasce como raiz do acervo**, e a entidade **`PRO`** e o tipo **`Carta de Produto`** estreiam. **`0` bytes do repositorio do candidato entraram** — `G0` e `IDENTIDADE` |
| Artefatos | **217** — **`+4`** sobre `BL-2026-08-01-01`: `PRO-nxtrack`, `MSG-2026-0009`, `PT-2026-015` e `roadmap-canonico` — este **ja existia e ja era medido**, sem entrada de catalogo *(`RD-80`, ABERTO)* |
| Linhas | **63.816** |
| Estado normativo | **A camada normativa NAO mudou. `0` fontes alteradas** — `FND-01` a `FND-11`, as **23 `CAP`**, os **19 `TPL`** e as **9 Cartas de Departamento** com **`0` bytes**, conferidos contra o `H-A` do ponto de partida. **`ADR-0007`, `ADR-0026` e `ADR-0027` com `0` bytes.** Alterados **exclusivamente nos campos que o ato autorizou**: `ADR-0030` *(`status` e `ratificacao`)* e `RFC-0025` *(`status`)*. Criados: **2** — a Carta `PRO-nxtrack` e `PT-2026-015`. Reconciliadas: as projecoes `M3` de `CV-04` — catalogo, `decisions/README`, `rfcs/README`, `governance/README`, `fitness/README` e o `README` da raiz |
| Ratificacao | **O nono ato soberano foi CONSUMIDO integralmente — seguem `9` `MSG`, nenhum novo.** `H-P` **2 de 2**, `H-N` invariante **2 de 2**, `IR-09` **3 de 3**, `atualizado_em` **nao tocado** em nenhum dos dois. **Fila de retidos por falta de APLICACAO: `0`** *(era `2` — `ADR-0030` e `RFC-0025`)*. **Fila por falta de ato: `2`**, inalterada — `ADR-0026` e `ADR-0028`. **`E2` ADIADA e intacta:** `RFC-0023`, `ADR-0028` e `FIT-2026-021` com **`0` bytes**. **`Q3` e `Q4` seguem NAO respondidas.** **`RD-33` SEGUE BLOQUEANTE por reserva do proprio ato** *(item VII, `LA-3`)*: a condicao de fato caiu — ha **`1` Produto em vigor** —, mas o fechamento e de **missao propria** |
| Proveniencia | **217** `native`, **`0`** externos admitidos. **`1` Produto em vigor**, **`0` `Spec`s**, **`1` `legacy-candidate` ainda nao admitido** *(medAlly)*. **`0` bytes do candidato**, medido por **`0` colisoes** de hash contra o acervo inteiro |
| Supera | **`BL-2026-08-01-01`** — §10.0.2 |
| Superada por | **`BL-2026-08-01-03`** — §10.0 |
| Evidencia de integridade | §**10.19**. **§10.0.1 a §10.18 nao foram editadas** (`BL-02`), exceto o campo *Superada por* de `BL-2026-08-01-01`, que e o par de sucessao, e a **renumeracao de §10.0.x** — que desloca subsecao, **nunca valor** |

### 10.0.4 Baseline superada em emissao anterior — `BL-2026-08-01-01`, com os valores ORIGINAIS

| Campo | Valor |
|---|---|
| **Identificador** | **BL-2026-08-01-01** |
| Data | **2026-08-01** |
| Marco | **O PORTAO DE ORIGEM EXTERNA EXERCIDO PELA SEGUNDA VEZ — e a primeira sob a norma emendada.** A **Missao 1.13.4.4** aplicou `ADR-0007 §5.3` ao candidato **nXtrack**, com **`G0` = `IDENTIDADE`** *(declarado antes de `G1`, `GA-01`)* e **`G3` = `RECOGNIZE`** — **primeira aplicacao PROSPECTIVA da classe** que `ADR-0027` criou, onde `RC-1` foi retrospectiva. **`G1` FECHA por medicao:** **17 de 17** fontes consumidas com autoria e data, **`0`** nao atribuiveis, congeladas no objeto `tree` `b9b36be9…fb4b`. **Nenhum Produto foi admitido e nenhum ato foi emitido** |
| Artefatos | **213** — **`+5`**: `RFC-0025`, `ADR-0030`, `FIT-2026-023`, `PT-2026-014` e `PS-2026-016` |
| Linhas | **62.250** |
| Estado normativo | **A camada normativa NAO mudou. `0` fontes alteradas** — `FND-01` a `FND-11`, as **23 `CAP`**, os **19 `TPL`** e as **9 Cartas** com **`0` bytes**, conferidos contra o `H-A` do ponto de partida. **`ADR-0007` NAO foi emendado: foi APLICADO** — `0` bytes. `ADR-0026` e `ADR-0027` tambem com **`0` bytes**. Alterados: **`0` `ADR` existentes** e **5** projecoes `M3` de `CV-04` *(catalogo, `decisions/README`, `rfcs/README`, `governance/README`, `fitness/README`)*, mais o `README` da raiz |
| Ratificacao | **Nenhum ato soberano foi emitido nem consumido — seguem `8` `MSG`.** `ADR-0030` esta **`em-revisao` · `ratificacao: pendente`**, e `RFC-0025` **`em-revisao`**. **`E2` ADIADA e intacta:** `RFC-0023`, `ADR-0028` e `FIT-2026-021` com **`0` bytes**. **Fila de retidos passa de `2` a `4`** *(`ADR-0026`, `ADR-0028`, `ADR-0030`, `RFC-0025`)*. **`Q1` RESPONDIDA** — o nXtrack, por `PT-2026-009 §1` decisao 7; a ressalva de `PS-2026-013 §7` vira `Q2` de `PS-2026-016`. **`RD-33` SEGUE BLOQUEANTE:** `S1` esta **preparada e nao consumida** |
| Proveniencia | **213** `native`, **`0`** externos admitidos — **medido por `0` colisoes de hash** entre os 179 hashes distintos do candidato e o acervo inteiro. **`2` `legacy-candidate` nomeados** *(medAlly, nXtrack)*, **`0` Produtos, `0` `Spec`s, `products/` inexistente** |
| Supera | **`BL-2026-07-31-08`** — §10.0.2 |
| Superada por | **`BL-2026-08-01-02`** — §10.0 |
| Evidencia de integridade | §**10.18**. **§10.0.2 a §10.17 nao foram editadas** (`BL-02`), exceto o campo *Superada por* de `BL-2026-07-31-08`, que e o par de sucessao, e a **renumeracao de §10.0.x** — que desloca subsecao, **nunca valor** |

### 10.0.5 Baseline superada em emissao anterior — `BL-2026-07-31-08`, com os valores ORIGINAIS

| Campo | Valor |
|---|---|
| **Identificador** | **BL-2026-07-31-08** |
| Data | **2026-07-31** |
| Marco | **O OITAVO ATO SOBERANO, CONSUMIDO — `E1` e `E3` em vigor.** A **Missao 1.13.4.3** aplicou [MSG-2026-0008](../memory/operacional/MSG-2026-0008-ato-soberano-emendas-e1-e-e3.md): **`ADR-0029` `ativo` · `ratificada`** *(`C3`/`Tipo 1`, ratificado pelo Soberano)* e **`ADR-0027` `ativo`** *(`C2`, aprovado por **DEP-EXE** com parecer de DEP-GOV, `ratificacao` **nao-exigida** e **nao criada**)*. Nasce o **registro de atos superados** de `SA-6`, [atos-superados](atos-superados.md), **com o contador em `0`**. **`RC-1` entra em vigor**: o `REWRITE` da 1.13.4 **le-se `RECOGNIZE`**, e os **cinco** artefatos daquela missao seguem com **`0` bytes** (`RC-2`) |
| Artefatos | **208** — **`+1`**, o registro de `SA-6` |
| Linhas | **60.921** |
| Estado normativo | **A camada normativa NAO mudou. `0` fontes alteradas** — `FND-01` a `FND-11`, as **23 `CAP`**, os **19 `TPL`** e as **9 Cartas** com **`0` bytes**. **`ADR-0007` NAO foi emendado** *(`E1` supera por instrumento novo)*. Alterados: **2 `ADR`**, **exclusivamente nos campos que o ato autorizou** — `ADR-0027` *(`status`, `−5` bytes)* e `ADR-0029` *(`status` e `ratificacao`, `−3` bytes)* —, mais **1 criado** e as **4** projecoes `M3` de `CV-04` |
| Ratificacao | **O oitavo ato soberano foi CONSUMIDO integralmente.** `H-P` **2 de 2**, `H-N` invariante **2 de 2**, `IR-09` **2 de 2**, `atualizado_em` **nao tocado**. **`E2` ADIADA e intacta:** `RFC-0023`, `ADR-0028` e `FIT-2026-021` com **`0` bytes** — **fila de retidos: `2`** *(`ADR-0026` e `ADR-0028`)*. **`Q1` e `RD-33` seguem bloqueantes**; `RD-66`, `RD-67`, `RD-68`, `RD-69` e `RD-70` **abertos e sem missao designada** |
| Proveniencia | **208** `native`, **`0`** externos admitidos. **`0` Produtos, `0` `Spec`s, `products/` inexistente** |
| Supera | **`BL-2026-07-31-07`** — §10.0.3 |
| Superada por | **`BL-2026-08-01-01`** — §10.0 |
| Evidencia de integridade | §**10.17**. **§10.0.3 a §10.16 nao foram editadas** (`BL-02`), exceto o campo *Superada por* de `BL-2026-07-31-07`, que e o par de sucessao, e a **renumeracao de §10.0.x** — que desloca subsecao, **nunca valor** |

### 10.0.6 Baseline superada em emissao anterior — `BL-2026-07-31-07`, com os valores ORIGINAIS

| Campo | Valor |
|---|---|
| **Identificador** | **BL-2026-07-31-07** |
| Data | **2026-07-31** |
| Marco | **O OITAVO ATO SOBERANO, registrado e NAO consumido.** O Fundador emitiu o ato sobre a minuta recortada de [PS-2026-015](pacote-soberano-2026-07-31-emendas-de-instrumento.md) **1.2.0** — **`Q2` respondida com `EMENDAR ADR-0007 AGORA`**, DEP-EXE autorizado a aprovar `ADR-0027` no rito `C2`, **`ADR-0029` RATIFICADO** e **`E2` ADIADA** —, e determinou **registrar e parar**. Nasce [MSG-2026-0008](../memory/operacional/MSG-2026-0008-ato-soberano-emendas-e1-e-e3.md), **ancorado no `H-A` do texto assinado**, e **`0` transicoes foram aplicadas** |
| Artefatos | **207** — **`+1`**, o registro do ato. **Primeira criacao de artefato desde `BL-2026-07-31-03`** |
| Linhas | **60.763** |
| Estado normativo | **A camada normativa NAO mudou. `0` fontes alteradas.** Criado: **1** artefato — `MSG-2026-0008`, entidade `MSG`, tipo `Diretiva` de `FND-10 §4.6`, **nenhum tipo, entidade ou diretorio novo**. Alterados: **4** projecoes `M3` que `CV-04` obriga a acompanhar — este catalogo, `memory/operacional/README`, `governance/README` e o `README` da raiz. **`PS-2026-015` e os `9` objetos das tres emendas com `0` bytes** |
| Ratificacao | **O oitavo ato soberano foi EMITIDO e NAO consumido** — estado novo no acervo. `ADR-0027` segue **`em-revisao`** · `nao-exigida`; `ADR-0029` segue **`em-revisao`** · **`pendente`**; o registro de `SA-6` **nao existe**; **`0`** aprovacoes de DEP-EXE. **`E2` ADIADA e intacta**; **`Q1` e `RD-33` seguem bloqueantes**; `RD-66`, `RD-67` e o novo **`RD-68`** seguem **ABERTOS e sem missao designada** |
| Proveniencia | **207** `native`, **`0`** externos admitidos |
| Supera | **`BL-2026-07-31-06`** — §10.0.3 |
| Superada por | **`BL-2026-07-31-08`** — §10.0 |
| Evidencia de integridade | §**10.16**. **§10.0.2 a §10.15 nao foram editadas** (`BL-02`), exceto o campo *Superada por* de `BL-2026-07-31-06`, que e o par de sucessao, e a **renumeracao de §10.0.x** — que desloca subsecao, **nunca valor**. **O ponteiro *Supera* de `BL-2026-07-31-06` acompanha o deslocamento** *(§10.0.2 → §10.0.3)*, pelo mesmo fundamento |

### 10.0.7 Baseline superada em emissao anterior — `BL-2026-07-31-06`, com os valores ORIGINAIS

| Campo | Valor |
|---|---|
| **Identificador** | **BL-2026-07-31-06** |
| Data | **2026-07-31** |
| Marco | **`CA-2` corrigido ANTES da assinatura, e somente ele**, por despacho do Fundador. [PS-2026-015](pacote-soberano-2026-07-31-emendas-de-instrumento.md) passa a **1.2.0**: a condicao de partida de §6.1.4 deixa de ser **bloqueante** e passa a **INFORMATIVA**, com o motivo escrito em **§6.1.4.1** — **o pacote mora dentro do acervo que a condicao mede**, logo **toda emissao legitima a invalida**, e ela era **insatisfazivel por construcao, nao por desvio**. **A ancora do ato e por objeto consumido: `9` `sha256`** — `6` de `CA-1` mais `3` de `CA-5` —, **nunca a arvore inteira**. O item `VI` da minuta, onde o mesmo efeito bloqueante estava **duplicado**, foi corrigido no mesmo ato |
| Artefatos | **206** — **inalterado**, o trabalho foi texto dentro de arquivo existente |
| Linhas | **60.480** |
| Estado normativo | **A camada normativa NAO mudou. `0` fontes alteradas.** Alterados: **`PS-2026-015`** — o **proprio pacote desta missao**, submetido e **nao consumido** — e as **3** projecoes `M3` que `CV-04` obriga a acompanhar: este catalogo, `governance/README` e o `README` da raiz. **Nenhum e norma**, e **os `9` objetos das tres emendas seguem com `0` bytes tocados** |
| Ratificacao | **Nenhum ato soberano foi consumido, e nenhum foi emitido.** A minuta recortada de §6.1 continua **texto submetido, nunca ato** — corrigir a condicao de partida **nao a aproxima de ato**. **`3` `ADR` retidos no acervo**, **`E2` ADIADA**, e **`RD-66` e `RD-67` seguem ABERTOS, sem missao designada**, sob o congelamento declarado pelo Fundador |
| Proveniencia | **206** `native`, **`0`** externos admitidos |
| Supera | **`BL-2026-07-31-05`** — §10.0.3 |
| Superada por | **`BL-2026-07-31-07`** — §10.0 |
| Evidencia de integridade | §**10.15**. **§10.0.2 a §10.14 nao foram editadas** (`BL-02`), exceto o campo *Superada por* de `BL-2026-07-31-05`, que e o par de sucessao, e a **renumeracao de §10.0.x** — que desloca subsecao, **nunca valor**. **O ponteiro *Supera* de `BL-2026-07-31-05` acompanha o deslocamento** *(§10.0.2 → §10.0.3)* **pelo mesmo fundamento: ponteiro de subsecao nao e valor de baseline** |

### 10.0.8 Baseline superada em emissao anterior — `BL-2026-07-31-05`, com os valores ORIGINAIS

| Campo | Valor |
|---|---|
| **Identificador** | **BL-2026-07-31-05** |
| Data | **2026-07-31** |
| Marco | **Registro do achado preexistente sobre a fronteira norma / nao-norma**, por despacho do Fundador. §7 recebe **`RD-66`** *(o [`README` da raiz](../README.md) nao declara QUAIS sao as arvores normativas)* e **`RD-67`** *(o §2 e o `versao` deste catalogo ficaram para tras)*. **Os dois nascem ABERTOS e NAO corrigidos** — esta emissao **registra e aponta**; corrigir e da **missao de catalogo** |
| Artefatos | **206** — **inalterado**, o trabalho foi texto dentro de arquivo existente |
| Linhas | **60.390** |
| Estado normativo | **A camada normativa NAO mudou. `0` fontes alteradas.** Alterados: **este catalogo** *(§7, §10 e frontmatter)* e as **2** projecoes `M3` que `CV-04` obriga a acompanhar — `governance/README` e o `README` da raiz. **Nenhum e norma** — e **`RD-66` registra que essa afirmacao se apoia em convencao de medicao, nao em regra escrita** |
| Ratificacao | **Nenhum ato soberano foi consumido, e nenhum foi emitido.** [PS-2026-015](pacote-soberano-2026-07-31-emendas-de-instrumento.md) segue **submetido, com `0` bytes tocados nesta emissao**; a minuta recortada de §6.1 continua **texto submetido, nunca ato**. **`3` `ADR` retidos no acervo**, e **`E2` ADIADA** |
| Proveniencia | **206** `native`, **`0`** externos admitidos |
| Supera | **`BL-2026-07-31-04`** — §10.0.3 |
| Superada por | **`BL-2026-07-31-06`** — §10.0 |
| Evidencia de integridade | §**10.14**. **§10.0.2 a §10.13 nao foram editadas** (`BL-02`), exceto o campo *Superada por* de `BL-2026-07-31-04`, que e o par de sucessao, e a **renumeracao de §10.0.x** — que desloca subsecao, **nunca valor**. **O ponteiro *Supera* de `BL-2026-07-31-04` acompanha o deslocamento** *(§10.0.2 → §10.0.3)* **pelo mesmo fundamento: ponteiro de subsecao nao e valor de baseline** |

### 10.0.9 Baseline superada em emissao anterior — `BL-2026-07-31-04`, com os valores ORIGINAIS

| Campo | Valor |
|---|---|
| **Identificador** | **BL-2026-07-31-04** |
| Data | **2026-07-31** |
| Marco | **A minuta de ato RECORTADA a `E1` e `E3`**, por despacho do Fundador. [PS-2026-015](pacote-soberano-2026-07-31-emendas-de-instrumento.md) passa a **1.1.0** e recebe **§6.1** — a variante **submetida** —, com os **6** objetos enumerados por ID, versao, caminho, linhas, `H-A` e `H-N`, e **`H-P` somente nos DOIS que sofrem `O4``. **`E2` fica ADIADA e nao rejeitada**, com o motivo escrito |
| Artefatos | **206** — **inalterado**, o trabalho foi texto dentro de arquivo existente |
| Linhas | **60.355** |
| Estado normativo | **A camada normativa NAO mudou. `0` fontes alteradas.** **1** artefato alterado nesta emissao: `PS-2026-015`, o proprio pacote da missao — **nao e norma, nao e historico alheio e nao esta consumido** |
| Ratificacao | **Nenhum ato soberano foi consumido.** [PS-2026-015](pacote-soberano-2026-07-31-emendas-de-instrumento.md) segue **submetido**, agora com **duas** variantes de minuta e **a recortada como submetida**. **`3` `ADR` retidos no acervo**, e **`E2` ADIADA** |
| Proveniencia | **206** `native`, **`0`** externos admitidos |
| Supera | **`BL-2026-07-31-03`** — §10.0.3 |
| Superada por | **`BL-2026-07-31-05`** — §10.0 |
| Evidencia de integridade | §**10.13**. **§10.0.2 a §10.12 nao foram editadas** (`BL-02`), exceto o campo *Superada por* de `BL-2026-07-31-03`, e a **renumeracao de §10.0.x** — que desloca subsecao, **nunca valor** |

### 10.0.10 Baseline superada em emissao anterior — `BL-2026-07-31-03`, com os valores ORIGINAIS

| Campo | Valor |
|---|---|
| **Identificador** | **BL-2026-07-31-03** |
| Data | **2026-07-31** |
| Marco | **As tres emendas de instrumento, com rito completo e NENHUMA em vigor.** Nove objetos criados — `RFC-0022` a `RFC-0024`, `ADR-0027` a `ADR-0029`, `FIT-2026-020` a `FIT-2026-022` — mais [PS-2026-015](pacote-soberano-2026-07-31-emendas-de-instrumento.md) e [PT-2026-013](relatorio-transicao-2026-07-31-emendas-de-instrumento.md). **A dependencia entre as tres foi MEDIDA em `0`** por quatro criterios, e por isso **nao ha conjunto atomico**: sao **tres unidades independentes** |
| Artefatos | **206** |
| Linhas | **60.151** |
| Estado normativo | **A camada normativa NAO mudou. `0` fontes alteradas** — `FND-01` a `FND-11`, as **23 `CAP`**, os **19 `TPL`** e as **9 Cartas** estao **byte a byte identicos** a copia datada. O diff de `FND-10` de `ADR-0028 §5.3` esta **escrito e NAO aplicado** |
| Ratificacao | **Nenhum ato soberano foi consumido, e a fila CRESCEU outra vez.** [PS-2026-014](pacote-soberano-2026-07-31-medally.md) segue **submetido e suspenso**; [PS-2026-015](pacote-soberano-2026-07-31-emendas-de-instrumento.md) entra **submetido**, com **tres** decisoes independentes. **`3` `ADR` retidos no acervo** — `ADR-0027` `nao-exigida`, `ADR-0028` e `ADR-0029` `pendente` |
| Proveniencia | **206** `native`, **`0`** externos admitidos. **1 candidato de Produto nomeado e nao admitido** — §9 |
| Supera | **`BL-2026-07-31-02`** — §10.0.2 |
| Superada por | **`BL-2026-07-31-04`** — §10.0 |
| Evidencia de integridade | §**10.12**. **§10.0.2 a §10.11 nao foram editadas** (`BL-02`), exceto o campo *Superada por* de `BL-2026-07-31-02`, que e o par de sucessao, e a **renumeracao de §10.0.x** — que desloca subsecao, **nunca valor** |

### 10.0.11 Baseline superada em emissao anterior — `BL-2026-07-31-02`, com os valores ORIGINAIS

| Campo | Valor |
|---|---|
| **Identificador** | **BL-2026-07-31-02** |
| Data | **2026-07-31** |
| Marco | **Manutencao dos instrumentos.** O **comando de reproducao da baseline foi corrigido** — lista fechada positiva, portao de raiz e portao de split — e **`BL-2026-07-30-01` volta a reproduzir nos 64 digitos** sobre a copia datada em que o comando publicado dava **198**: **o defeito era do instrumento, nunca da baseline** *(`RD-53`, ✅ FECHADO)*. **`RD-56`** *(`TPL-carta-produto` **1.1.0**)*, **`RD-57`** e **`RD-58`** ✅ **FECHADOS**; **`RD-49`** corrigido em **tres candidatos medidos e NAO aplicados**. **Item 0 REPROVA:** dos **19** caminhos do repositorio externo medidos na janela, **14** estao atribuidos a processo nomeado e **5 sao NAO ATRIBUIVEL** — **nenhuma mudanca da janela foi commitada**, e sem commit nao existe registro de autoria. **`0`** sobra silenciosa e **`0`** escritores concorrentes no acervo. **Tres minutas preparadas e `0` aplicadas.** **NENHUM ato emitido, nada ratificado, `0` Produtos em vigor, nenhuma `Spec` criada e `RD-33` permanece BLOQUEANTE** |
| Artefatos | **195** |
| Linhas | **57.769** |
| Estado normativo | **A camada normativa mudou em UM arquivo, e so nele.** Das **71** fontes de `foundation/`, `departments/` e `capabilities/` *(excluidos os indices)*, **exatamente 1 mudou** — `foundation/templates/TPL-carta-produto.md`, **1.0.0 → 1.1.0**, rito **`C2`**, aprovador **DEP-GOV** por `FND-09 §8.2` linha `TPL`, `ratificacao` **nao exigida** — e as outras **70** sao **byte a byte identicas**, conferidas `sha256` **arquivo a arquivo** contra a copia datada. **`FND-01` a `FND-11`, as 23 `CAP`, as 9 Cartas de Departamento e os outros 18 `TPL` com `0` bytes tocados.** `ADR-0001` a `ADR-0025` `ativo`; **`ADR-0026` segue `em-revisao` · `pendente`**, retido por falta de ato. `RFC-0001` a `RFC-0021` `aprovado`. **`ADR-0005`, `ADR-0007` e `ADR-0012` NAO emendados — `0` bytes**; as tres minutas que os alcancariam estao **fora do acervo** |
| Ratificacao | **Nenhum ato soberano foi consumido, e a fila CRESCEU.** [PS-2026-014](pacote-soberano-2026-07-31-medally.md) permanece **submetido, suspenso e nao alterado** *(`0` bytes)*, com **`Q1` bloqueante e intacta**; somam-se a ele **3 Cartas `1.2.0`** medidas e prontas *(`RD-49`)* e **3 minutas** *(`RD-54`/`RD-55`, `ADR-0005`, superacao de ato)*. **`GO-TO-SPECS` permanece LIBERADO e EXERCIDO EM PARTE:** **`RD-33`** continua sendo a **unica pendencia bloqueante do acervo** |
| Proveniencia | **195** `native`, **`0`** externos admitidos. **1 candidato de Produto nomeado e nao admitido** — §9 |
| Supera | **`BL-2026-07-31-01`** — §10.0.2 |
| Superada por | **`BL-2026-07-31-03`** — §10.0 |
| Evidencia de integridade | §**10.11**. **§10.0.2 a §10.10 nao foram editadas** (`BL-02`), exceto o campo *Superada por* de `BL-2026-07-31-01`, que e o par de sucessao, e a **renumeracao das subsecoes de §10.0.x sem alteracao de valor** |

### 10.0.12 Baseline superada em emissao anterior — `BL-2026-07-31-01`, com os valores ORIGINAIS

| Campo | Valor |
|---|---|
| **Identificador** | **BL-2026-07-31-01** |
| Data | **2026-07-31** |
| Marco | **S1 — a admissao canonica do medAlly.** O **portao de origem externa de [ADR-0007 §5.3](../decisions/ADR-0007-fronteira-greenfield-legado.md) foi EXERCIDO PELA PRIMEIRA VEZ**, sobre **um** candidato nomeado: `G1`–`G4` **comprovados**, `G5` **preparado**, **`G3` = `REWRITE`**, **`0` bytes admitidos** e **`0` bytes escritos** no repositorio de origem. **Dois** objetos submetidos — [ADR-0026](../decisions/ADR-0026-admissao-do-medally-como-primeiro-produto.md) e a **Carta candidata `PRO-medally`** —, ambos com `H-A`/`H-N`/`H-P` medidos. **NENHUM Produto entrou em vigor:** `products/` **nao existe**, **`0`** artefatos de tipo `PRO` sao vigentes, **nenhuma `Spec` nasceu** e **`RD-33` permanece BLOQUEANTE** |
| Artefatos | **194** |
| Linhas | **56.854** |
| Estado normativo | **A camada normativa NAO mudou.** `FND-01` a `FND-11`, as **23 `CAP`**, os **19 `TPL`** e as **9 Cartas de Departamento** estao **byte a byte identicos** a `BL-2026-07-30-02`, verificado **arquivo a arquivo** contra a copia datada — **71 fontes conferidas · `0` alteradas**. **`ADR-0001` a `ADR-0025` `ativo`, com uma excecao nova declarada: `ADR-0026` esta `em-revisao` e `ratificacao: pendente`**, retido por falta de ato. **`RFC-0001` a `RFC-0021` `aprovado`.** `INC-2026-001` e `INC-2026-002` `fechado`; `MEM-EST-0001` `ativo`. **`ADR-0007` exercido e NAO emendado — `0` bytes** |
| Ratificacao | **Nenhum ato soberano foi consumido, e um pacote esta pendente:** [PS-2026-014](pacote-soberano-2026-07-31-medally.md) — **dois objetos que formam um conjunto atomico**, com **sobreposicao de diff igual a `0`**. **`GO-TO-SPECS` permanece LIBERADO e EXERCIDO EM PARTE:** **`RD-33`** continua sendo a **unica pendencia bloqueante do acervo**, e **so fecha apos a VIGENCIA da Carta**. **Pendencias para o SOBERANO: cinco, e uma bloqueia** — `Q1` de [PS-2026-014 §7](pacote-soberano-2026-07-31-medally.md), verificado por [FIT-2026-019](fitness/FIT-2026-019-admissao-do-medally.md) |
| Proveniencia | **194** `native`, **`0`** externos admitidos. **1 candidato nomeado e nao admitido** — §9 |
| Supera | **`BL-2026-07-30-02`** — §10.0.2 |
| Superada por | **`BL-2026-07-31-02`** — §10.0 |
| Evidencia de integridade | §**10.10**. **§10.0.2 a §10.9 nao foram editadas** (`BL-02`), exceto o campo *Superada por* de `BL-2026-07-30-02`, que e o par de sucessao, e a **renumeracao das subsecoes de §10.0.x sem alteracao de valor** |

### 10.0.13 Baseline superada em emissao anterior — `BL-2026-07-30-02`, com os valores ORIGINAIS

| Campo | Valor |
|---|---|
| **Identificador** | **BL-2026-07-30-02** |
| Data | **2026-07-30** |
| Marco | **Vigencia do Framework de Specifications** — o **setimo ato soberano** ([MSG-2026-0007](../memory/operacional/MSG-2026-0007-ato-soberano-vigencia-do-framework-de-specifications.md)) foi consumido e **os catorze objetos entraram em vigor**: [ADR-0022](../decisions/ADR-0022-sede-canonica-do-framework-de-specifications.md) a [ADR-0025](../decisions/ADR-0025-extensao-da-propagacao-de-qg-1-as-cartas-restantes.md), **`FND-11` 1.0.0** *(criacao)*, `FND-01` **1.7.0 cumulativa**, `FND-02` **1.4.0**, `FND-03` **1.6.0**, `FND-10` **1.5.0** e as **5 Cartas 1.1.0**. **`RD-27`, `RD-31` e `RD-37` FECHADOS.** **Nenhum Produto, Projeto ou `Spec` criado** — `RD-33` permanece **bloqueante** |
| Artefatos | **189** |
| Linhas | **55.280** |
| Estado normativo | **A camada normativa MUDOU, e mudou apenas onde o ato autorizou.** **Das 71 fontes normativas, exatamente as 10 autorizadas mudaram** — 9 alteradas e **1 criada** *(`foundation/11-framework-specifications.md`)* —, e as outras **61** permanecem **byte a byte** identicas: `FND-04` a `FND-09`, as **23 `CAP`**, os **19 `TPL`** e as **4** Cartas nao alcancadas. **`0` bytes fora dos diffs autorizados**, medido arquivo a arquivo contra a copia datada |
| Ratificacao | **O setimo ato soberano foi consumido integralmente.** `H-P` reproduz em **14 de 14**; `H-N` **invariante** nas **10** transicoes `O4`; **`IR-09`** reconstroi `H-A` nos **10**; identidade binaria nos **4** sem `O4`. **`0` pacotes pendentes** |
| Proveniencia | **189** `native`, 0 externos. **`0` linhas de evidencia externa lidas nesta missao** — §9 |
| Supera | **`BL-2026-07-30-01`** — §10.0.3 |
| Superada por | **`BL-2026-07-31-01`** — §10.0 |
| Evidencia de integridade | §**10.9**. **§10.0.3 a §10.8 nao foram editadas** (`BL-02`), exceto o campo *Superada por* de `BL-2026-07-30-01`, que e o par de sucessao, e a **renumeracao das subsecoes de §10.0.x sem alteracao de valor** |

### 10.0.14 Baseline superada em emissao anterior — `BL-2026-07-30-01`, com os valores ORIGINAIS

| Campo | Valor |
|---|---|
| **Identificador** | **BL-2026-07-30-01** |
| Data | **2026-07-30** |
| Marco | **Convergencia pre-ratificacao** — **dois ritos completos, uma coordenacao, uma consolidacao e nada aplicado**: [ADR-0024](../decisions/ADR-0024-conformidade-de-contrato-das-fundacionais.md) *(`C3 · Tipo 2`)* fecha **`RD-27`** nos tres objetos com **`0` bytes de corpo alterados**; [ADR-0025](../decisions/ADR-0025-extensao-da-propagacao-de-qg-1-as-cartas-restantes.md) *(`C2 · Tipo 2`, **primeira dispensa de RFC do acervo**)* fecha **`RD-37`** e leva a familia das **nove** Cartas de **11 afirmacoes falsas em 4** para **`0` em `0`**. **`FND-01` sai de duas variantes vivas para uma**, cumulativa, e a **sobreposicao de diff entre objetos do ato vai de 1 para `0`** — **14 objetos sobre 14 arquivos**. **4 achados novos**; **`RD-45` e `RD-46` fechados no candidato** |
| Artefatos | **185** |
| Linhas | **54.190** |
| Estado normativo | **Inalterado em toda a camada normativa de `foundation/*.md`, `departments/` e `capabilities/`.** `FND-01` a `FND-10`, as **9 Cartas**, as **23 `CAP`** e os **19 `TPL`** estao **byte a byte identicos** a `BL-2026-07-29-10`, verificado por `cmp` contra a copia datada — **73 fontes conferidas · `0` alteradas**. **`ADR-0001` a `ADR-0025` `ativo`, com quatro excecoes declaradas: `ADR-0022`, `ADR-0023`, `ADR-0024` e `ADR-0025` estao `em-revisao`**, retidos por falta de ato. **`RFC-0001` a `RFC-0020` `aprovado`.** `INC-2026-001` e `INC-2026-002` `fechado`; `MEM-EST-0001` `ativo`. **`ADR-0020` e `ADR-0021` intactos — `0` bytes, inclusive frontmatter** |
| Ratificacao | **Nenhum ato soberano foi consumido, e quatro pacotes estao pendentes:** [PS-2026-009](pacote-soberano-2026-07-29-fnd-11.md) **2.0.0**, [PS-2026-010](pacote-soberano-2026-07-29-rd-31.md), [PS-2026-011](pacote-soberano-2026-07-30-rd-27.md) e [PS-2026-012](pacote-soberano-2026-07-30-rd-37.md), **consolidados em [PS-2026-013](pacote-soberano-2026-07-30-consolidado.md)** — **14 objetos, cada um bloqueavel isoladamente, com `0` sobreposicao de diff**. **`GO-TO-SPECS` permanece LIBERADO e EXERCIDO EM PARTE:** **`RD-33`** continua sendo a **unica pendencia bloqueante do acervo**. **Pendencias para o SOBERANO: quatro, e uma bloqueia** — [PT-2026-009 §9](relatorio-transicao-2026-07-30-convergencia.md), verificado por [FIT-2026-017](fitness/FIT-2026-017-convergencia-pre-ratificacao.md) |
| Proveniencia | **185** `native`, 0 externos. **`0` linhas de evidencia externa lidas nesta missao** — §9 |
| Supera | **`BL-2026-07-29-10`** — §10.0.4 |
| Superada por | **`BL-2026-07-30-02`** — §10.0 |
| Evidencia de integridade | §**10.8**. **§10.0.4 a §10.7 nao foram editadas** (`BL-02`), exceto o campo *Superada por* de `BL-10`, que e o par de sucessao, e a **renumeracao das subsecoes**, que **nao altera valor algum** |

### 10.0.15 Baseline superada em emissao anterior — `BL-2026-07-29-10`, com os valores ORIGINAIS

| Campo | Valor |
|---|---|
| **Identificador** | **BL-2026-07-29-10** |
| Data | **2026-07-29** |
| Marco | **Canonizacao e propagacao** — **dois ritos completos e nada aplicado**: [ADR-0022](../decisions/ADR-0022-sede-canonica-do-framework-de-specifications.md) *(`C3 · Tipo 1`)* submete **`FND-11`** como sede fundacional de `SF-01` a `SF-32`, com **30 de 32 regras migrando byte a byte** e **1** alteracao de merito declarada; [ADR-0023](../decisions/ADR-0023-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md) *(`C2 · Tipo 2`)* corrige as **8** afirmacoes falsas de `DEP-PRD` e faz `DEP-EXE` **declarar `QG-1` pela primeira vez**. **`PILOTO-DEFERIDO` formalizado**; **7 achados novos**; **duas colisoes de norma declaradas com escolha submetida** |
| Artefatos | **177** |
| Linhas | **51.698** |
| Estado normativo | **Inalterado em toda a camada normativa de `foundation/*.md`, `departments/` e `capabilities/`.** `FND-01` a `FND-10`, as **9 Cartas**, as **23 `CAP`** e os **19 `TPL`** estao **byte a byte identicos** a `BL-2026-07-29-09`, verificado por `cmp` contra a copia datada — **0 fontes alteradas** e **0 artefatos `M2` emendados**, a primeira vez em duas missoes. **`ADR-0001` a `ADR-0023` `ativo`, com uma excecao declarada: `ADR-0022` esta `em-revisao` e `ratificacao: pendente`** — `C3 · Tipo 1`, retido por falta de ato. **`RFC-0001` a `RFC-0019` `aprovado`.** `INC-2026-001` e `INC-2026-002` `fechado`; `MEM-EST-0001` `ativo`. **`ADR-0021` intacto — `0` bytes, inclusive frontmatter** |
| Ratificacao | **Nenhum ato soberano foi consumido, e dois pacotes estao pendentes:** [PS-2026-009](pacote-soberano-2026-07-29-fnd-11.md) *(`FND-11`, `FND-01` 1.6.0, `FND-03` 1.6.0)* e [PS-2026-010](pacote-soberano-2026-07-29-rd-31.md) *(`DEP-PRD` 1.1.0, `DEP-EXE` 1.1.0)*, **independentes, verificaveis e bloqueaveis isoladamente**. **`GO-TO-SPECS` permanece LIBERADO e EXERCIDO EM PARTE:** o Framework existe, a sede canonica esta submetida e **a primeira `Spec` continua nao sendo criavel** — **`RD-33`**, a **unica pendencia bloqueante do acervo**. **Pendencias para o SOBERANO: sete, e uma bloqueia** — [PT-2026-008 §10.2](relatorio-transicao-2026-07-29-canonizacao.md), verificado por [FIT-2026-016](fitness/FIT-2026-016-canonizacao-e-propagacao.md) |
| Proveniencia | **177** `native`, 0 externos. **`0` linhas de evidencia externa lidas nesta missao** — §9 |
| Supera | **`BL-2026-07-29-09`** — §10.0.5 |
| Superada por | **`BL-2026-07-30-01`** — §10.0.3 |
| Evidencia de integridade | §**10.7**. **§10.0.4 a §10.6 nao foram editadas** (`BL-02`), exceto o campo *Superada por* de `BL-09`, que e o par de sucessao |

### 10.0.16 Baseline superada em emissao anterior — `BL-2026-07-29-09`, com os valores ORIGINAIS

| Campo | Valor |
|---|---|
| **Identificador** | **BL-2026-07-29-09** |
| Data | **2026-07-29** |
| Marco | **Framework de Specifications** — **`SF-01` a `SF-32`** instituidos em [ADR-0021](../decisions/ADR-0021-framework-de-specifications.md), `C2 · Tipo 2`, com **`0`** arquivos de `foundation/*.md` alterados; **`RD-23` FECHADA** com `TPL-spec` **1.1.0** *(5 defeitos onde o achado citava 2)*; **12** casos de determinismo, **11 coerentes e 1 divergente que virou `RD-31`**; **5** achados novos; e o registro de que **nenhuma `Spec` e criavel** — `RD-33` |
| Artefatos | **169** |
| Linhas | **48.764** |
| Estado normativo | **Inalterado em toda a camada normativa de `foundation/*.md`, `departments/` e `capabilities/`.** `FND-01` a `FND-10`, as **9 Cartas** e as **23 `CAP`** estao **byte a byte identicos** a `BL-2026-07-29-08`, verificado por `cmp` contra a copia datada — **0 fontes alteradas**, e **`FND-01`, `FND-02` e `FND-10` com `0` bytes tocados**, por determinacao *(pre-correcao `RD-27`)*. **Um artefato `M2` emendado:** `TPL-spec` **1.0.0 → 1.1.0**, rito **C2** por `ADR-0021`, aprovado por **DEP-GOV** *(`FND-09 §8.2` linha `TPL`)*, com diff **literal e reversivel**. **`ADR-0001` a `ADR-0021` `ativo`**; `ADR-0021` e **`C2 · Tipo 2`**, `ratificacao: nao-exigida`, e **nao emenda fonte alguma**. **`RFC-0001` a `RFC-0017` `aprovado`**. `INC-2026-001` e `INC-2026-002` `fechado`; `MEM-EST-0001` `ativo`. **Nenhum artefato retido por falta de ato** |
| Ratificacao | **Nenhum ato soberano novo foi consumido, e nenhum e devido para o estado desta baseline.** `ADR-0021` e **C2 · Tipo 2**, cuja classe **nao exige ratificacao** (`FND-04 §2.1`). **`GO-TO-SPECS` permanece LIBERADO e passa a estar EXERCIDO EM PARTE:** o Framework existe e **a primeira Spec nao e criavel** — **`RD-33`**, a **unica pendencia bloqueante do acervo**, cujo desbloqueio e **`S1`** *(ato criando Produto)* ou **`S2`** *(RFC C3 → ADR C3 → ato)*, **disjuntas, ambas do SOBERANO**. **Pendencias para o SOBERANO: cinco, e uma bloqueia** — [PT-2026-007 §11.1](relatorio-transicao-2026-07-29-specifications.md), verificado por [FIT-2026-015](fitness/FIT-2026-015-framework-de-specifications.md) |
| Proveniencia | **169** `native`, 0 externos. **Evidencia externa `A4` lida e nao admitida** — §9 |
| Supera | **`BL-2026-07-29-08`** — §10.0.6 |
| Superada por | **`BL-2026-07-29-10`** — §10.0.4 |
| Evidencia de integridade | §**10.6**. **§10.0.4 a §10.5 nao foram editadas** (`BL-02`), inclusive nas divergencias registradas como `RD-24` e `RD-30` |

### 10.0.17 Baseline superada em emissao anterior — `BL-2026-07-29-08`, com os valores ORIGINAIS

| Campo | Valor |
|---|---|
| **Identificador** | **BL-2026-07-29-08** |
| Data | **2026-07-29** |
| Marco | **Fechamento operacional** — **`RD-22` fechado por refutacao de premissa** e **`RD-26` reconciliado com metodo declarado**, com os **dez objetos do sexto ato rehasheados** *(10 de 10 nos 64 digitos)*, a prova final em **55/55 com as cinco exigencias de §IX** e as **oito condicoes de §X satisfeitas** |
| Artefatos | **164** |
| Linhas | **46.353** |
| Estado normativo | **Inalterado em toda a camada normativa.** `FND-01` a `FND-10`, as **9 Cartas**, as **23 `CAP`** e os **19 `TPL`** estao **byte a byte identicos** a `BL-2026-07-29-07`, verificado por `cmp` contra a copia datada — **0 fontes alteradas**. **`ADR-0001` a `ADR-0020` `ativo`**; `ADR-0020` e **`C2 · Tipo 2`**, `ratificacao: nao-exigida`, e **nao emenda fonte alguma**. **`RFC-0001` a `RFC-0016` `aprovado`**. `INC-2026-001` e `INC-2026-002` `fechado`; `MEM-EST-0001` `ativo`. **Nenhum artefato retido por falta de ato** |
| Ratificacao | **Nenhum ato soberano novo foi consumido, e nenhum e devido para o estado desta baseline.** `ADR-0020` e **C2 · Tipo 2**, cuja classe **nao exige ratificacao** (FND-04 §2.1). **`GO-TO-SPECS` LIBERADO** pelas **8 de 8** condicoes de §X do sexto ato, que **ja o autorizou sob condicao objetiva** — [PT-2026-006 §8](relatorio-transicao-2026-07-29-fechamento-operacional.md), verificado por [FIT-2026-014](fitness/FIT-2026-014-regime-ministerial-e-cobertura-de-contexto.md). **Pendencias para o SOBERANO: tres, e nenhuma bloqueia trabalho** |
| Proveniencia | **164** `native`, 0 externos |
| Supera | **`BL-2026-07-29-07`** — §10.0.7 |
| Superada por | **`BL-2026-07-29-09`** — §10.0.5 |
| Evidencia de integridade | §**10.5**, com o **metodo de contagem de links declarado** — atende **`RD-30`**. §10.2 e §10.4 **nao foram editadas** (`BL-02`), inclusive nas divergencias registradas como `RD-24` e `RD-30` |

> **Somente o campo *Superada por* foi preenchido nesta emissao, e ele e o unico que `BL-02`
> nao congela** — e o par de sucessao, na mesma logica de `LN-02`, que exige a relacao legivel
> **dos dois lados**. **Os demais valores sao os ORIGINAIS, nao recalculados**, e a impressao
> digital de `BL-08` **reproduziu tres vezes** nesta missao antes de qualquer escrita:
> **164 · 46.353 · `8cf2143c…b027a7f`**.

### 10.0.18 Baseline superada em emissao anterior — `BL-2026-07-29-07`, com os valores ORIGINAIS

| Campo | Valor |
|---|---|
| **Identificador** | **BL-2026-07-29-07** |
| Data | **2026-07-29** |
| Marco | **Aplicacao integral do sexto ato soberano** — **dez objetos em vigor**, nas **quatro etapas da ordem obrigatoria**, com **30 hashes medidos**, **6 `H-P` projetados reproduzidos nos 64 digitos**, `IR-09` reproduzindo `H-A` em **6 de 6** e **exatamente 10 arquivos alterados** em todo o acervo |
| Artefatos | **159** |
| Linhas | **44.539** |
| Estado normativo | **FND-01 1.5.0 · FND-02 1.3.0 · FND-09 1.5.0 cumulativa · FND-10 1.4.0 cumulativa** promulgadas e `ativo`; FND-03 a FND-08 `ativo` e **inalteradas**. **ADR-0001 a ADR-0019 `ativo`** — `ADR-0016` a `ADR-0019` **ratificadas por este ato**, e **nenhum ADR permanece retido**. **RFC-0001 a RFC-0015 `aprovado`** — as quatro ultimas **acolhidas como propostas**, nunca convertidas em decisao. INC-2026-001 e INC-2026-002 `fechado`; MEM-EST-0001 `ativo`. **9 de 9 Cartas escritas e 9 de 9 em vigor**, com `DEP-QAR` em **1.2.0**, `DEP-KMS` em **1.1.0** e `DEP-ENG` em **1.1.0**. **As versoes intermediarias FND-09 1.4.0 e FND-10 1.3.0 nunca existiram como arquivo** |
| Ratificacao | **O sexto ato soberano foi consumido integralmente** — [MSG-2026-0006](../memory/operacional/MSG-2026-0006-ato-soberano-aplicacao-integral.md). **Os cinco pacotes soberanos pendentes — PS-2026-004 a PS-2026-008 — foram consumidos de uma vez, e a fila de artefatos retidos zerou.** Condicoes de eficacia: **5 de 5 anteriores** e **5 de 5 posteriores** ([PT-2026-005 §2](relatorio-transicao-2026-07-29-aplicacao.md)). **`GO-TO-SPECS` NAO foi autorizado:** **7 das 8 condicoes de §X satisfeitas**, e a **condicao 6** falha por **`RD-22`** — `promulgacao` e `ativacao` **sem titular declarado em fonte alguma**. **Pela primeira vez em cinco missoes, o bloqueio nao e ausencia de ato soberano** |
| Proveniencia | **159** `native`, 0 externos |
| Supera | **`BL-2026-07-29-06`** — §10.1 |
| Superada por | **`BL-2026-07-29-08`** — §10.0.6 |
| Evidencia de integridade | §**10.4** — §10.2 permanece como registro de `BL-06` e **nao foi editada** (`BL-02`), inclusive na divergencia de contagem registrada como **RD-24** |

### 10.1 Baselines anteriores — preservadas, nao editadas

| Campo | **`BL-2026-07-29-06`** | `BL-2026-07-29-05` | `BL-2026-07-29-04` | `BL-2026-07-29-03` | `BL-2026-07-29-02` | `BL-2026-07-29-01` | `BL-…-06` | `BL-…-05` | `BL-…-04` | `BL-…-03` | `BL-…-02` | `BL-…-01` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marco | **Verificacao de ratificacao — continuacao da Missao 1.12** | **Fechamento normativo — Missao 1.12** | Fechamento de autoridade — Missao 1.11 — Missao 1.11** | **Aplicacao do ato de 2026-07-29** | **Missao 1.10** *(reemissao apos RD-07)* | **Missao 1.10** *(decisao `BLOCKED`)* | Missao **1.9** | Missao **1.8** | Missao **1.7** | Missao **1.6** | Missao **1.5** | Missao **1.4** |
| Artefatos · linhas | **157** · **43.498** | **155** · **42.785** | **147** · **40.429** | **137** · **37.766** | **134** · **36.888** | **134** · **36.886** | **131** · **35.701** | **117** · **30.947** | **112** · **28.966** | **107** · **26.506** | **100** · **23.742** | **93** · **21.318** |
| Impressao digital | `f9859941ec7c772d1aed28ee1125a111dd342a1d93b88cd237f303cba22f3fba` | `6a5c065f58c70b03e0b32e2c2ce4613faefe2f00473e5183903f73c29ce035bc` | `272be52e352bfef237ca6bf46fdae13190dc4a4ea8d838e98e4c1db3faa8d20a` | `d39998daa010245a14a8090396f315ce7dc194284a562fd6d68cb0cf34e286de` | `976f7708b2d2dd3a1cd04a18fad3a78f8da8f1a31746a1c06bc5fbb5c9ae69a5` | `08fad263b021dd374eed960c48e6ff484600d204cb87ab0005152a8b80daf856` | `164214e40e7e56277e292dd57dc9db1ee9c7cfebfc345b17fbdbf8e492a6f9c6` | `c9a25651fc3920ac70e144a3ced0656f52694a197456ded679583f7b821b6c8f` | `d411c1bf2415d1cbd4eec132f5e4ec4d99f5ece1097df074f745ba8e073d8c43` | `541ed5b6f85b3318b3e8cb8671db6d0f1eff532177ba40c69bcc93ddde07d6b1` | `df00ab4a0ba67cea104bba344b2a723c7535c9a46500ec52eca08a7f4ad60b7a` | `399c45050e3edb1fd4eccedfb7ab93fcfc087ff1bb140241b70f879592d3b85e` |
| Estado | **Superada por `BL-2026-07-29-07`** | Superada por `BL-2026-07-29-06` | Superada por `BL-2026-07-29-05` | Superada por `BL-2026-07-29-04` | Superada por `BL-2026-07-29-03` | Superada por `BL-2026-07-29-02` | Superada por `BL-2026-07-29-01` | Superada por `BL-…-06` | Superada por `BL-…-05` | Superada por `BL-…-04` | Superada por `BL-…-03` | Superada por `BL-…-02` |

> **`BL-2026-07-29-05` e `BL-2026-07-29-06` entram nesta tabela agora, com os valores
> ORIGINAIS.** Nenhuma das duas havia sido movida para §10.1 quando foi superada — a tabela
> saltava de `BL-04` para a baseline vigente. **Os valores de `BL-06` sao os de §10.0, que
> reproduzem por ferramenta** *(157 · 43.498 · `f9859941…3fba`)*, **nao os de §10.2**, que
> declarava a contagem de `BL-05` ao lado da impressao digital de `BL-06` — achado **RD-24**.
> Os de `BL-05` vem de [PT-2026-003 §9](relatorio-transicao-2026-07-29-fechamento-normativo.md),
> **C1 a C3**. **Nenhuma das duas foi recalculada, e §10.2 nao foi tocada.**

> **BL-02 aplicada pela setima vez: baseline nunca e editada.** Os valores acima sao os
> **originais**, nao recalculados. A integridade de `BL-2026-07-28-06` foi **conferida antes de
> qualquer edicao desta missao** — as tres evidencias reproduziram exatamente **131 artefatos**,
> **35.701 linhas** e a impressao digital `164214e4…f9c6` —, e **nenhum dos seis registros foi
> tocado depois**. A conferencia previa nao e formalidade: e ela que sustenta a verificacao
> **V1** de [PT-2026-001 §1.1](relatorio-transicao-2026-07-29-departamentos.md), e e o que
> permite afirmar que **nenhuma alteracao ocorreu entre a revisao e a decisao** — a exigencia
> literal que o segundo ato soberano elevou a condicao de eficacia.
> A nova medicao recebeu **identidade nova**, conforme **BL-02**.

> **Copia datada tomada antes das edicoes da Missao 1.10** — **131** arquivos, preservados fora
> do acervo, com contagem e impressao digital **reconferidas na copia** (PI-07, AF-35).

> **Copia datada tomada antes das edicoes** — **117** arquivos, preservados fora do acervo,
> conforme **PI-07** e **AF-35**. Ela e a **terceira via de preservacao** de `DEP-QAR` **1.0.0**,
> ao lado do hash registrado e do diff reversivel ([MSG-2026-0003 §2.1](../memory/operacional/MSG-2026-0003-ato-soberano-emenda-qar-e-criterio-de-consolidacao.md)).

### 10.2 Evidencia de integridade — `BL-2026-07-29-06`

Medida com os instrumentos ja existentes (CE-02), sem criar ferramenta nova:

| Evidencia | Valor | Como reproduzir |
|---|---|---|
| Contagem de artefatos | **155** | `find . -name "*.md" -not -path "./.obsidian/*" -not -path "./_SAIDA-COMPANY-OS/*" \| wc -l` |
| Contagem de linhas | **42.785** | idem `\| sort \| xargs wc -l \| tail -1` |
| **Impressao digital do acervo** | `f9859941ec7c772d1aed28ee1125a111dd342a1d93b88cd237f303cba22f3fba` | idem `\| sort \| xargs wc -l \| sha256sum` |
| **Exclusao declarada por lista fechada** | `.obsidian/` e `_SAIDA-COMPANY-OS/` | **Correcao de RD-17.** O comando de `BL-2026-07-29-04` omitia a segunda, e por isso **nao reproduzia**. `BL-2026-07-29-04` **nao foi editada** (BL-02) |
| **Links relativos resolvidos** | **1.924 verificados · 0 quebrados** | resolucao de cada alvo de link relativo contra o sistema de arquivos |
| **Autoverificacao** | **96 artefatos com `autor` e `revisor` · 0 coincidencias** | comparacao dos dois campos de frontmatter |
| **Hashes dos artefatos ratificados** *(H-A · H-N · H-P)* | 6 artefatos, 3 hashes cada | [MSG-2026-0001 §2](../memory/operacional/MSG-2026-0001-ato-soberano-ratificacao-cartas-piloto.md), [MSG-2026-0002 §2](../memory/operacional/MSG-2026-0002-ato-soberano-cartas-comando-plataforma-e-contexto.md) e [MSG-2026-0003 §2](../memory/operacional/MSG-2026-0003-ato-soberano-emenda-qar-e-criterio-de-consolidacao.md) — **fontes**; nao reproduzidos aqui |
| **Hashes das 5 Cartas submetidas** *(H-A · H-N)* · **`H-P` projetado** | 5 artefatos, 2 hashes cada · 5 `H-P` | [PS-2026-002 §2](pacote-soberano-2026-07-28-cartas.md) e [PT-2026-001 §1.2 e §1.3](relatorio-transicao-2026-07-29-departamentos.md) — **fontes**; nao reproduzidos aqui |
| **Hashes das 2 emendas candidatas de Carta** *(H-A · H-N · `H-P` projetado)* | 2 candidatos, 3 hashes cada | [PS-2026-006 §2](pacote-soberano-2026-07-29-kms-eng.md) — **fonte**; nao reproduzidos aqui |
| **Hashes dos candidatos fundacionais** *(H-A · H-N)* · **ADR candidatos** *(H-A · H-N · `H-P` projetado)* | **6 fundacionais · 4 ADR** | [PS-2026-004 §3](pacote-soberano-2026-07-29-rd-02.md), [PS-2026-005 §3](pacote-soberano-2026-07-29-rd-09.md), [PS-2026-007 §3](pacote-soberano-2026-07-29-rd-14.md) e [PS-2026-008 §3](pacote-soberano-2026-07-29-rd-15.md) — **fontes**; nao reproduzidos aqui |
| **Reimplementacao de `IR-02`/`IR-03` validada antes do uso** | **6 de 6** hashes de controle reproduzem | `FND-09` 1.3.0, `FND-10` 1.2.0 e o `H-P` de `DEP-QAR` 1.2.0 — [PS-2026-007 §3.3](pacote-soberano-2026-07-29-rd-14.md) |
| **Credencial em texto** | **0 ocorrencias** no acervo **e** nos cinco candidatos | Varredura por padrao de segredo (PI-08, LV-02) |
| **Terminadores de linha dos candidatos** | **Preservados em 3 de 3** nesta missao, byte a byte | **`FND-10` usa `CRLF` — 771 de 771 linhas**; os demais, `LF`. Montagem **em modo binario na origem** — [PS-2026-008 §3](pacote-soberano-2026-07-29-rd-15.md) |

> **A impressao digital muda por acrescimo de artefato, e nao pela ativacao.** O que separou
> `BL-05` de `BL-06` foram os **14 artefatos novos**, a expansao dos indices e **uma unica linha**
> acrescentada a `DEP-QAR` pela emenda 1.1.0 — de **386** para **387**. A transicao **O4** que a
> colocou em `ativo` **nao alterou nenhuma linha de corpo**, e `H-N` permaneceu invariante
> (W7 de MSG-2026-0003).

> **O que separa `BL-06` de `BL-2026-07-29-01` e de outra natureza, e a diferenca merece ser
> lida.** Sao **3 artefatos novos** e a expansao de **quatro** indices — e **nenhuma Carta**.
> **As nove Cartas tem, nesta baseline, exatamente os mesmos hashes e as mesmas contagens de
> linha que tinham na anterior**, verificados um a um: e a prova, pelo instrumento mais barato
> do sistema, de que **a Missao 1.10 nao tocou nenhum objeto submetido a decisao do Soberano**.

> **O limite desta evidencia deixou de ser o limite da verificacao.** A impressao digital cobre
> **caminhos e tamanhos**, e **nao** detecta edicao que preserve o numero de linhas — o limite
> continua declarado (PI-10, LV-12). Mas a integridade do que foi **ratificado** ja **nao
> depende** dela: **`IR-09`** ([ADR-0012](../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md))
> reconstroi o texto ratificado e o confere contra **H-A**, byte a byte — e o teste **passou nos
> dois artefatos em que pode ser aplicado retroativamente**, `DEP-QAR` e `DEP-ENG`.

### 10.3 Regras da baseline

| # | Regra |
|---|---|
| BL-01 | A baseline e **projecao do catalogo**, emitida em um marco. Nao e artefato novo, nao tem arquivo proprio e nao cria entidade (RG-07). |
| BL-02 | Baseline nunca e editada: nova medicao gera **novo identificador** `BL-<AAAA-MM-DD>-<NN>`, e a anterior fica registrada como superada. |
| BL-03 | Baseline emitida sem evidencia reproduzivel e nula (LV-12, CE-04). |
| BL-04 | Divergencia entre a baseline e o acervo real e **defeito do catalogo** (RG-03, PJ-03) — nunca motivo para alterar artefato. |

### 10.4 Evidencia de integridade — `BL-2026-07-29-07`

Medida com os instrumentos ja existentes (CE-02), **apos** todas as edicoes desta aplicacao.
A exclusao segue a **lista fechada** corrigida em `RD-17`.

| Evidencia | Valor | Como reproduzir |
|---|---|---|
| Contagem de artefatos | **159** | `find . -name "*.md" -not -path "./.obsidian/*" -not -path "./_SAIDA-COMPANY-OS/*" \| wc -l` |
| Contagem de linhas | **44.539** | idem `\| sort \| xargs wc -l \| tail -1` |
| **Impressao digital do acervo** | `6841e2e5ef9e1bb03321e23e4017edcfbd887699528fe27c4a0d47963b34753d` | idem `\| sort \| xargs wc -l \| sha256sum` |
| **Links relativos resolvidos** | **1.965 verificados · 0 quebrados** | resolucao de cada alvo de link relativo contra o sistema de arquivos |
| **Autoverificacao** | **98 artefatos com `autor` e `revisor` · 0 coincidencias** | comparacao dos dois campos de frontmatter |
| **Credencial em texto** | **0 ocorrencias** | varredura por padrao de segredo (PI-08, LV-02) |
| **Frontmatter** — `id` e `versao` | **0 ausencias em 159** | verificacao campo a campo |
| **Arquivos alterados por esta aplicacao** | **exatamente 10** · **0 criados** · **0 removidos** *(entre os preexistentes)* | `cmp` de cada `.md` contra a copia datada pre-ato |
| **Terminadores** | `FND-10` **`CRLF` em 778 de 778**; os outros nove objetos **`LF` integral** | contagem de bytes `CR` e `LF` |
| **Hashes dos dez objetos** *(H-A · H-N · H-P)* | 10 objetos, 3 hashes cada = **30** | [MSG-2026-0006 §2](../memory/operacional/MSG-2026-0006-ato-soberano-aplicacao-integral.md) — **fonte**; nao reproduzidos aqui |
| **Copia datada anterior as edicoes** | **531** arquivos, fora do acervo, reconferida **na copia** | `_backups/LucaX-Enterprise-OS_2026-07-29_pre-ato-soberano-06/` (PI-07, AF-35) |

> **§10.2 nao foi editada, e continua sendo o registro de `BL-2026-07-29-06`** — inclusive na
> divergencia de contagem que **RD-24** registra. Corrigi-la seria **editar baseline**, o que
> `BL-02` proibe; a correcao legitima e **nova medicao com novo identificador**, que e esta.

### 10.5 Evidencia de integridade — `BL-2026-07-29-08`

Medida com os instrumentos ja existentes (`CE-02`), **apos** todas as edicoes desta missao.
A exclusao segue a **lista fechada** corrigida em `RD-17`.

| Evidencia | Valor | Como reproduzir |
|---|---|---|
| Contagem de artefatos | **164** | `find . -name "*.md" -not -path "./.obsidian/*" -not -path "./_SAIDA-COMPANY-OS/*" \| wc -l` |
| Contagem de linhas | **46.353** | idem `\| sort \| xargs wc -l \| tail -1` |
| **Impressao digital do acervo** | `8cf2143c7d20d4688f911f716a7a683bc82b72d155e7d424e3f4875c8b027a7f` | idem `\| sort \| xargs wc -l \| sha256sum` |
| **Links relativos resolvidos** | **2.121 verificados · 0 quebrados** | **Metodo declarado — atende `RD-30`:** todo alvo da forma `] (destino)` em arquivo `.md` da coorte, **excluidos** `http:`, `https:`, `mailto:` e ancoras puras *(`#...`)*, com o fragmento `#` **removido** antes da resolucao, normalizado contra o diretorio do arquivo de origem e testado por existencia no sistema de arquivos. **Cada ocorrencia conta uma vez**, inclusive alvos repetidos |
| **Autoverificacao** | **103 artefatos com `autor` e `revisor` · 0 coincidencias** | comparacao dos dois campos de frontmatter |
| **Cobertura de `perfil_contexto`** | **164 de 164 classificados · 0 nao classificados** | **§2.1**: frontmatter quando declarado, padrao de FND-10 §10.3 quando ausente. **A soma reproduz 164 · 46.353** |
| **Frontmatter** — `id` e `versao` | **0 ausencias em 164** | verificacao campo a campo |
| **Fontes normativas alteradas por esta missao** | **0** | `cmp` de cada `.md` preexistente contra `_backups/LucaX-Enterprise-OS_2026-07-29_pre-missao-1-12-1/` |
| **Arquivos alterados por esta missao** | **9** · **5 criados** · **0 removidos** | idem. Os alterados sao **todos `M3`** — catalogo e indices |
| **Hashes dos dez objetos do sexto ato** *(reproducao)* | **10 de 10 reproduzem nos 64 digitos** | `sha256sum` de cada objeto contra [MSG-2026-0006 §2](../memory/operacional/MSG-2026-0006-ato-soberano-aplicacao-integral.md) e [PS-2026-006](pacote-soberano-2026-07-29-kms-eng.md) — [PT-2026-006 §2](relatorio-transicao-2026-07-29-fechamento-operacional.md) |
| **Credencial em texto** | **0 ocorrencias** | varredura por padrao de segredo (PI-08, LV-02) |
| **Copia datada anterior as edicoes** | **537** arquivos, fora do acervo, **reconferida na copia** *(159 · 44.539 · `6841e2e5…753d`)* | `_backups/LucaX-Enterprise-OS_2026-07-29_pre-missao-1-12-1/` (PI-07, AF-35) |

> **§10.4 nao foi editada, e continua sendo o registro de `BL-2026-07-29-07`** — inclusive na
> divergencia de contagem de links que **`RD-30`** registra. **A impressao digital de `BL-07`
> reproduziu tres vezes nesta missao, antes de qualquer escrita**, e e ela que sustenta a
> afirmacao de que **nenhuma fonte normativa foi alterada**.
>
> **O limite da impressao digital continua declarado:** ela cobre **caminhos e contagens de
> linha**, e **nao** detecta edicao que preserve o numero de linhas (`PI-10`, `LV-12`). Nesta
> missao, esse limite **nao e o limite da verificacao**: as fontes foram conferidas por **`cmp`
> byte a byte** contra a copia datada, e os **dez objetos ratificados** por **`sha256`** contra o
> ato.

### 10.6 Evidencia de integridade — `BL-2026-07-29-09`

Medida com os instrumentos ja existentes (`CE-02`), **apos** todas as edicoes da Missao 1.13.
A exclusao segue a **lista fechada** corrigida em `RD-17`.

| Evidencia | Valor | Como reproduzir |
|---|---|---|
| Contagem de artefatos | **169** | `find . -name "*.md" -not -path "./.obsidian/*" -not -path "./_SAIDA-COMPANY-OS/*" \| wc -l` |
| Contagem de linhas | **48.764** | idem `\| sort \| xargs wc -l \| tail -1` |
| **Impressao digital do acervo** | `572bbbdfe2c45217373995f22f8be7d0ecbbbcf35754c98fc511f19c5652a87f` | idem `\| sort \| xargs wc -l \| sha256sum` |
| **Links relativos resolvidos** | **2.336 verificados · 0 quebrados** | **Metodo de §10.5, aplicado sem alteracao:** todo alvo da forma `] (destino)` em arquivo `.md` da coorte, **excluidos** `http:`, `https:`, `mailto:` e ancoras puras *(`#...`)*, com o fragmento `#` **removido** antes da resolucao, normalizado contra o diretorio do arquivo de origem e testado por existencia. **Cada ocorrencia conta uma vez** |
| **Autoverificacao** | **109 artefatos com `autor` e `revisor` · 0 coincidencias** | comparacao dos dois campos de frontmatter |
| **Cobertura de `perfil_contexto`** | **169 de 169 classificados · 0 nao classificados** | **§2.1**: frontmatter quando declarado, padrao de FND-10 §10.3 quando ausente. **A particao foi RECOMPUTADA sobre a coorte inteira, nao incrementada**, e a soma reproduz **169 · 48.764** |
| **Frontmatter** — `id` e `versao` | **0 ausencias em 169** | verificacao campo a campo |
| **Fontes normativas alteradas por esta missao** | **0** | `cmp` de cada `.md` preexistente de `foundation/*.md`, `departments/` e `capabilities/` contra `_backups/LucaX-Enterprise-OS_2026-07-29_pre-missao-1-13/` |
| **`FND-01`, `FND-02` e `FND-10`** | **0 bytes alterados** — pre-correcao `RD-27` cumprida | `cmp` byte a byte contra a copia datada |
| **Baselines historicas editadas** | **0** — pre-correcao `RD-28` cumprida | §10.0.3 a §10.5 conferidas; **somente o campo *Superada por* de `BL-08` foi preenchido**, que e o par de sucessao |
| **Artefatos `M2` emendados** | **1** — `TPL-spec` **1.0.0 → 1.1.0** | `sha256`: `cabaa58e…f748` · **132** linhas → `afd0dc7e…370f` · **272** linhas |
| **Terminadores de linha** | **`LF` integral em `TPL-spec`, preservado — 0 bytes `CR` antes e depois** | contagem de bytes `CR` e `LF` |
| **Arquivos alterados por esta missao** | **9** · **5 criados** · **0 removidos** | idem. Os alterados sao **1 `M2`** *(`TPL-spec`)* e **8 `M3`** — catalogo e indices |
| **Credencial em texto** | **0 ocorrencias** | varredura por padrao de segredo (`PI-08`, `LV-02`) |
| **Copia datada anterior as edicoes** | **542** arquivos, fora do acervo, **reconferida na copia** *(164 · 46.353 · `8cf2143c…b027a7f`)* | `_backups/LucaX-Enterprise-OS_2026-07-29_pre-missao-1-13/` (`PI-07`, `AF-35`) |

> **§10.5 nao foi editada, e continua sendo o registro de `BL-2026-07-29-08`.** A impressao
> digital de `BL-08` **reproduziu tres vezes nesta missao, antes de qualquer escrita**, e e ela
> que sustenta a afirmacao de que **nenhuma fonte normativa foi alterada**.
>
> **O limite da impressao digital continua declarado, e nesta missao ele importa mais que nas
> anteriores.** Ela cobre **caminhos e contagens de linha** e **nao** detecta edicao que preserve
> o numero de linhas (`PI-10`, `LV-12`). Como esta missao **alterou um artefato `M2`** — e nao
> apenas projecoes `M3` —, a verificacao **nao se apoia** na impressao digital: `TPL-spec` tem
> **`sha256` medido antes e depois**, **diff literal reversivel** publicado em
> [ADR-0021 §5.12](../decisions/ADR-0021-framework-de-specifications.md) e **terminadores
> conferidos byte a byte**; e as fontes intocadas foram conferidas por **`cmp`** contra a copia
> datada.
>
> **Nenhum objeto ratificado foi rehasheado nesta missao, e a razao esta dita:** **nenhum ato
> soberano foi consumido**, e os **dez objetos do sexto ato** ja reproduziram **10 de 10 nos 64
> digitos** em [PT-2026-006 §2](relatorio-transicao-2026-07-29-fechamento-operacional.md),
> **sob a mesma impressao digital de acervo que esta missao reproduziu antes de escrever**. A
> invariancia da fonte e o que dispensa a remedicao (`PJ-01`) — **e ela foi medida, nao
> presumida**.

### 10.7 Evidencia de integridade — `BL-2026-07-29-10`

Medida com os instrumentos ja existentes (`CE-02`), **apos** todas as edicoes da Missao 1.13.1.
A exclusao segue a **lista fechada** corrigida em `RD-17`.

| Evidencia | Valor | Como reproduzir |
|---|---|---|
| Contagem de artefatos | **177** | `find . -name "*.md" -not -path "./.obsidian/*" -not -path "./_SAIDA-COMPANY-OS/*" \| wc -l` |
| Contagem de linhas | **51.698** | idem `\| sort \| xargs wc -l \| tail -1` |
| **Impressao digital do acervo** | `f7e56bc835409cd848fcb03f3998ac58ba78e57a09b584f583a56fdc25d11bd4` | idem `\| sort \| xargs wc -l \| sha256sum` |
| **Links relativos resolvidos** | **2.550 verificados · 0 quebrados** | **Metodo de §10.5 e §10.6, aplicado sem alteracao:** todo alvo da forma `] (destino)` em arquivo `.md` da coorte, **excluidos** `http:`, `https:`, `mailto:` e ancoras puras *(`#...`)*, com o fragmento `#` **removido** antes da resolucao, normalizado contra o diretorio do arquivo de origem e testado por existencia. **Cada ocorrencia conta uma vez** |
| **Autoverificacao** | **117 artefatos com `autor` e `revisor` · 0 coincidencias** | comparacao dos dois campos de frontmatter |
| **Cobertura de `perfil_contexto`** | **177 de 177 classificados · 0 nao classificados** | frontmatter quando declarado, padrao de FND-10 §10.3 quando ausente. **Os 8 artefatos novos declaram o campo** |
| **Frontmatter** — `id` e `versao` | **0 ausencias em 177** | verificacao campo a campo |
| **Fontes normativas alteradas por esta missao** | **0** | `cmp` de cada `.md` preexistente de `foundation/*.md`, `departments/` e `capabilities/` contra `_backups/LucaX-Enterprise-OS_2026-07-29_pre-missao-1-13-1/` |
| **Artefatos `M2` emendados** | **0** — **a primeira missao em duas que nao emenda nenhum `M2` no acervo** | os **6** candidatos vivem **fora** do acervo |
| **`ADR-0021` — texto e frontmatter** | **0 bytes alterados** | `H-A` reproduz `cafd28fb…bbc1` apos todas as edicoes da missao |
| **`ADR`, `MSG`, `FIT` e baselines historicas editadas** | **0** — `LV-04`, `BL-02` cumpridos | §10.0.3 a §10.6 conferidas; **somente o campo *Superada por* de `BL-09` foi preenchido**, que e o par de sucessao |
| **Candidatos medidos fora do acervo** | **6** — `FND-11` **399** · `FND-01` `V1` **488** e `V2` **492** · `FND-03` **633** · `DEP-PRD` **445** · `DEP-EXE` **506** | `sha256` de cada um publicado em [PS-2026-009 §4](pacote-soberano-2026-07-29-fnd-11.md) e [PS-2026-010 §4](pacote-soberano-2026-07-29-rd-31.md), **reconferido apos a copia** |
| **`IR-02`/`IR-03` validados antes do uso** | **7 de 7 controles reproduzem**, em **4** tipos documentais | PS-2026-009 §4.3 |
| **`H-N` invariante sob `O4`** | **3 de 3** | `FND-11`, `DEP-PRD`, `DEP-EXE` |
| **`IR-09` — reconstrucao reproduz `H-A`** | **4 de 4** | `FND-11`, `ADR-0022`, `DEP-PRD`, `DEP-EXE` |
| **Terminadores de linha** | **`LF` integral nos 8 artefatos novos e nos 6 candidatos — 0 bytes `CR`** | contagem de bytes `CR` e `LF` |
| **Arquivos alterados por esta missao** | **8** · **8 criados** · **0 removidos** | os alterados sao **8 `M3`** — catalogo e indices. **Nenhum `M1` e nenhum `M2`** |
| **Credencial em texto** | **0 ocorrencias** | varredura por padrao de segredo (`PI-08`, `LV-02`) |
| **Copia datada anterior as edicoes** | **553** arquivos, fora do acervo, com **`_candidatos/`** | `_backups/LucaX-Enterprise-OS_2026-07-29_pre-missao-1-13-1/` (`PI-07`, `AF-35`) |

> **§10.6 nao foi editada, e continua sendo o registro de `BL-2026-07-29-09`.** A impressao
> digital de `BL-09` — **169 · 48.764 · `572bbbdf…a87f`** — **reproduziu antes de qualquer
> escrita** desta missao, e e ela que sustenta a afirmacao de que **nenhuma fonte normativa foi
> alterada**.
>
> **O limite da impressao digital continua declarado, e nesta missao ele pesa menos que nas
> anteriores.** Ela cobre **caminhos e contagens de linha** e **nao** detecta edicao que preserve
> o numero de linhas (`PI-10`, `LV-12`). **Nesta missao a verificacao nao depende dela:** **`0`
> artefatos `M2` foram emendados no acervo**, e as fontes intocadas foram conferidas por **`cmp`**
> contra a copia datada — **arquivo a arquivo, nao por agregado**.
>
> **Nenhum objeto ratificado foi rehasheado, e a razao esta dita:** **nenhum ato soberano foi
> consumido.** Em compensacao, **seis candidatos foram medidos e reconferidos apos a copia**, e os
> **7** controles de `IR-02`/`IR-03` foram validados **antes** de qualquer medicao nova — o que e
> mais forte do que remedir objetos que ninguem tocou.

### 10.8 Evidencia de integridade — `BL-2026-07-30-01`

Medida com os instrumentos ja existentes (`CE-02`), **apos** todas as edicoes da Missao 1.13.2.
A exclusao segue a **lista fechada** corrigida em `RD-17`.

| Evidencia | Valor | Como reproduzir |
|---|---|---|
| Contagem de artefatos | **185** | `find . -name "*.md" -not -path "./.obsidian/*" -not -path "./_SAIDA-COMPANY-OS/*" \| wc -l` |
| Contagem de linhas | **54.190** | idem `\| sort \| xargs wc -l \| tail -1` |
| **Impressao digital do acervo** | `3d8dbea0f9ee534707156c54fa2ab58c95640ef0fb2436a981b50bb2adea84da` | idem `\| sort \| xargs wc -l \| sha256sum` |
| **Links relativos resolvidos** | **2.727 verificados · 0 quebrados** | **Metodo de §10.5 a §10.7, aplicado sem alteracao** |
| **Autoverificacao** | **125 artefatos com `autor` e `revisor` · 0 coincidencias** | comparacao dos dois campos de frontmatter |
| **Frontmatter** — `id` e `versao` | **0 ausencias em 185** | verificacao campo a campo |
| **Cobertura de `perfil_contexto`** | **185 de 185 classificados · 0 nao classificados** | frontmatter quando declarado, padrao de FND-10 §10.3 quando ausente. **Os 8 artefatos novos declaram o campo** |
| **Fontes normativas alteradas por esta missao** | **`0` de 73 conferidas** | `cmp` de **cada** `.md` de `foundation/`, `departments/` e `capabilities/` contra `_backups/LucaX-Enterprise-OS_2026-07-30_pre-missao-1-13-2/` — **arquivo a arquivo, nao por agregado** |
| **Artefatos `M1` editados** | **`0`** — inclusive **`ADR-0020`**, **`ADR-0021`**, `ADR-0022` e `ADR-0023` | `cmp` contra a copia datada |
| **`ADR`, `MSG`, `FIT` e baselines historicas editadas** | **`0`** — `LV-04`, `BL-02` cumpridos | §10.0.3 a §10.7 conferidas; **somente o campo *Superada por* de `BL-10` foi preenchido**, que e o par de sucessao, e as subsecoes foram **renumeradas sem alteracao de valor** |
| **Artefato do acervo emendado** | **1** — `PS-2026-009` **1.0.0 → 2.0.0**, com a **1.0.0 preservada** *(446 linhas, `H-A` `e349b4fb…c3be`, medido **antes** de qualquer edicao)* | `M3` por tipo; `AC-11` cumprida |
| **Candidatos medidos fora do acervo** | **13** — `FND-01` **1.7.0** *(493)*, `ALT` *(490)*, `V1` *(488)*, `V2` *(492)* · `FND-02` **1.4.0** *(524)* · `FND-03` *(633)* · `FND-10` **1.5.0** *(785, `CRLF`)* · `FND-11` *(399)* · `DEP-PRD` *(445)* · `DEP-EXE` *(506)* · **`DEP-OPS`** *(438)* · **`DEP-GRW`** *(444)* · **`DEP-TLS`** *(425)* | `sha256` de cada um em [PS-2026-013 §2](pacote-soberano-2026-07-30-consolidado.md), **reconferido apos a copia** |
| **`IR-02`/`IR-03` validados antes do uso** | **20 de 20 controles reproduzem**, em **4** tipos documentais e nas **3** medidas | [PS-2026-011 §4.3](pacote-soberano-2026-07-30-rd-27.md); `ADR-0023` foi **remedido**, nao copiado, e virou o **vigesimo** |
| **`H-N` invariante sob `O4`** | **6 de 6** | `FND-11`, `DEP-PRD`, `DEP-EXE`, `DEP-OPS`, `DEP-GRW`, `DEP-TLS` |
| **`IR-09` — reconstrucao reproduz `H-A`** | **6 de 6** | as 5 Cartas e `FND-11`; mais `ADR-0024` e `ADR-0025` |
| **Sobreposicao de diff entre objetos do ato** | **`0`** — **14 objetos, 14 arquivos, um para um** | [PS-2026-013 §4.1](pacote-soberano-2026-07-30-consolidado.md) |
| **Equivalencia `SF-01`–`SF-32`, remedida** | **30 `T-IDENTICA` · 1 referencial · 1 de merito · `0` de 32 renumerados · ordem literalmente identica** | Medicao independente que **reproduz a declaracao de `FND-11 §2.1`** |
| **Afirmacoes falsas sobre `QG-1` nas 9 Cartas, apos os candidatos** | **`0`** *(eram **11** em **4**)*; **5 de 9** nomeiam `DEP-EXE`; **5 de 5** caminhos coerentes | [PS-2026-012 §5](pacote-soberano-2026-07-30-rd-37.md) |
| **Terminadores de linha** | **`LF` nos 8 artefatos novos e em 12 dos 13 candidatos — `0` bytes `CR`.** **`FND-10` e `CRLF`: 785 de 785 preservados, `0` convertidos** | contagem de bytes `CR` e `LF`, **em modo binario** |
| **Arquivos alterados por esta missao** | **7** · **8 criados** · **0 removidos** | os alterados sao **`M3`** — catalogo, indices — mais **`PS-2026-009`**. **Nenhum `M1` e nenhum `M2`** |
| **Credencial em texto** | **`0` ocorrencias** | varredura por padrao de segredo sobre **185** artefatos **e 13** candidatos (`PI-08`, `LV-02`) |
| **Copia datada anterior as edicoes** | **568** arquivos, fora do acervo, com **`_candidatos/`** | `_backups/LucaX-Enterprise-OS_2026-07-30_pre-missao-1-13-2/` (`PI-07`, `AF-35`) |

> **§10.7 nao foi editada, e continua sendo o registro de `BL-2026-07-29-10`.** A impressao
> digital de `BL-10` — **177 · 51.698 · `f7e56bc8…1bd4`** — **reproduziu antes de qualquer
> escrita** desta missao, e e ela que sustenta a afirmacao de que **nenhuma fonte normativa foi
> alterada**.
>
> **O limite da impressao digital continua declarado, e nesta missao ele pesa pouco.** Ela cobre
> **caminhos e contagens de linha** e **nao** detecta edicao que preserve o numero de linhas
> (`PI-10`, `LV-12`). **A verificacao nao depende dela:** as **73** fontes normativas foram
> conferidas por **`cmp`**, arquivo a arquivo, e **`0` artefatos `M2` foram emendados no acervo**.
>
> **Nenhum objeto ratificado foi rehasheado, e a razao esta dita: nenhum ato soberano foi
> consumido.** Em compensacao, **13 candidatos foram medidos e reconferidos apos a copia**, e os
> **20** controles de `IR-02`/`IR-03` foram validados **antes** de qualquer medicao nova.

### 10.9 Evidencia de integridade — `BL-2026-07-30-02`

Medida com os instrumentos ja existentes (`CE-02`), **apos** todas as edicoes da Missao 1.13.3.
A exclusao segue a **lista fechada** corrigida em `RD-17`.

| Evidencia | Valor | Como reproduzir |
|---|---|---|
| Contagem de artefatos | **189** | `find . -name "*.md" -not -path "./.obsidian/*" -not -path "./_SAIDA-COMPANY-OS/*" \| wc -l` |
| Contagem de linhas | **55.280** | idem `\| sort \| xargs wc -l \| tail -1` |
| **Impressao digital do acervo** | `a3ca6ce33aa28c048d07831b5355e2f3ce0c83958bb5df42a092ff432655ca5d` | idem `\| sort \| xargs wc -l \| sha256sum` |
| **`H-P` reproduzido** | **14 de 14** — **10** transicoes `O4` e **4** objetos com `H-P` = `H-A` | `sha256` de cada arquivo em vigor contra [MSG-2026-0007 §2](../memory/operacional/MSG-2026-0007-ato-soberano-vigencia-do-framework-de-specifications.md) |
| **`H-N` invariante sob `O4`** | **10 de 10** | `IR-02`: `sha256` do arquivo com as linhas de `IR-03` removidas, **antes e depois** da transicao |
| **`IR-09` — reconstrucao reproduz `H-A`** | **10 de 10** com `O4` · **identidade binaria em 4 de 4** sem `O4` | revertendo **apenas** os campos de `IR-03` que o ato autorizou, e remedindo |
| **Bytes fora dos diffs autorizados** | **`0`** — **das 71 fontes normativas de `foundation/`, `departments/` e `capabilities/` *(excluidos os indices)*, exatamente as 10 autorizadas mudaram: **9 alteradas e 1 criada**; as outras **61** sao byte a byte identicas. Os demais **4** objetos do ato sao `ADR`. **164 dos 185** artefatos anteriores estao **binariamente intactos**; os **8** restantes sao **projecoes `M3`** reconciliadas por §V.8 do ato, e **3** artefatos novos sao os **registros que §V.9 exige**. **`0` removidos** | `sha256` de **cada** `.md` do acervo contra `_backups/LucaX-Enterprise-OS_2026-07-30_pre-missao-1-13-3/`, **arquivo a arquivo, nao por agregado** |
| **Terminadores de linha** | **`FND-10`: 785 de 785 linhas em `CRLF`, `0` convertidas.** `LF` nos outros 13 objetos | contagem de bytes `CR` e `LF`, **em modo binario** |
| **Links relativos resolvidos** | **2.834 verificados · 0 quebrados** | **Metodo de §10.5 a §10.8, aplicado sem alteracao** |
| **Autoverificacao** | **128 artefatos com `autor` e `revisor` · 0 coincidencias** | comparacao dos dois campos de frontmatter (`ADR-0005`) |
| **Credencial em texto** | **`0` ocorrencias** | varredura por padrao de segredo sobre **189** artefatos (`PI-08`, `LV-02`) |
| **Afirmacoes falsas sobre `QG-1` nas 9 Cartas, NO ACERVO EM VIGOR** | **`0` em `0` Cartas** *(eram **11** em **4**)* · **63** ocorrencias · **5 de 9** nomeiam `DEP-EXE` · **5 de 5** caminhos coerentes | detector calibrado **primeiro no estado vigente**, onde reproduziu as **11 em 4** de [PS-2026-012 §5](pacote-soberano-2026-07-30-rd-37.md) celula a celula |
| **`IR-02`/`IR-03` validados antes do uso** | **6 de 6 controles reproduzem** — `FND-01` 1.5.0, `FND-02` 1.3.0, `FND-10` 1.4.0 *(`CRLF`)*, `ADR-0024`, `RFC-0020` e `FND-01` `ALT` | reimplementacao independente conferida contra hashes **ja publicados**, **antes** de medir qualquer objeto do ato |
| **`O4` determinado por reproducao, nao por inferencia** | **10 de 10** — `status` `em-revisao` → `ativo` nos dez, e `ratificacao` `pendente` → `ratificada` em **oito** | busca no espaco de transicoes de `IR-03` pela unica que reproduz o `H-P` publicado. **`atualizado_em` NAO foi tocado em nenhum** |
| **Baseline anterior reproduzida antes da escrita** | **`BL-2026-07-30-01`: 185 · 54.190 · `3d8dbea0…84da` · 2.727 links · 125 pares** | reproducao integral **antes** de qualquer edicao |
| **Baseline historica de submissao preservada** | **`BL-2026-07-29-10`: 177 · 51.698 · `f7e56bc8…1bd4`** | reproduzida sobre `_backups/…_2026-07-30_pre-missao-1-13-2/` (§IV.2 do ato) |
| **`ADR-0020` e `ADR-0021`** | **`0` bytes alterados · nenhum `superado_por` gravado** | `sha256` contra a copia datada (§VI.2 do ato) |
| **Candidatos nao promulgados, preservados** | **3** — `FND-01` `ALT` *(490)*, `V1` *(488)* e `V2` *(492)* | permanecem em `_candidatos/` como **evidencia historica**; **nao ha fallback automatico** (§VI.4 do ato) |
| **Copia datada anterior as edicoes** | **576** arquivos, fora do acervo, com **`_candidatos/`** | `_backups/LucaX-Enterprise-OS_2026-07-30_pre-missao-1-13-3/` (`PI-07`, `AF-35`) |

> **§10.0.3 a §10.8 nao foram editadas**, exceto o campo *Superada por* de `BL-2026-07-30-01`,
> que e o par de sucessao, e a **renumeracao de §10.0.x** — que desloca subsecao, **nunca valor**.
>
> **O limite da impressao digital continua declarado, e nesta missao ele pesa pouco.** Ela cobre
> **caminhos e contagens de linha** e **nao** detecta edicao que preserve o numero de linhas
> (`PI-10`, `LV-12`). **A verificacao desta missao nao depende dela:** os **14** objetos foram
> conferidos por `sha256` **um a um** contra os `H-P` publicados **antes** da escrita, e **todo o
> acervo** foi comparado por `sha256` **arquivo a arquivo** contra a copia datada.
> **Das 71 fontes normativas de `foundation/`, `departments/` e `capabilities/` *(excluidos os indices)*, exatamente as 10 autorizadas mudaram — 9 alteradas e 1 criada — e as outras 61 estao byte a byte identicas.** Os outros 4 objetos do ato sao `ADR`. **164 dos 185 artefatos anteriores estao binariamente intactos.** **A impressao digital e o resumo, nao a prova.**

### 10.10 Evidencia de integridade — `BL-2026-07-31-01`

Medida com os instrumentos ja existentes (`CE-02`), **apos** todas as edicoes da Missao 1.13.4.
A exclusao segue a **lista fechada** corrigida em `RD-17`.

| Evidencia | Valor | Como reproduzir |
|---|---|---|
| Contagem de artefatos | **194** | `find . -name "*.md" -not -path "./.obsidian/*" -not -path "./_SAIDA-COMPANY-OS/*" \| wc -l` |
| Contagem de linhas | **56.854** | idem `\| sort \| xargs wc -l \| tail -1` |
| **Impressao digital do acervo** | `b355e227b6c0a842dc1be0e0a78f2030a88e7a7ab7cd2686103bc1b9752775bf` | idem `\| sort \| xargs wc -l \| sha256sum` |
| **Baseline anterior reproduzida antes da escrita** | **`BL-2026-07-30-02`: 189 · 55.280 · `a3ca6ce33aa28c048d07831b5355e2f3ce0c83958bb5df42a092ff432655ca5d`** | reproducao integral **antes** de qualquer edicao, e **reconferida na copia datada** |
| **`IR-02`/`IR-03` validados antes do uso** | **10 de 10 controles reproduzem** — `FND-01`, `FND-02`, `FND-03`, `FND-10` *(`CRLF`)*, `FND-11`, `ADR-0022`, `ADR-0023`, `ADR-0024`, `ADR-0025` e `DEP-PRD` | reimplementacao conferida contra `H-N` **ja publicados** em [PS-2026-013 §2](pacote-soberano-2026-07-30-consolidado.md), **antes** de medir qualquer objeto novo. **A primeira versao do filtro REPROVOU em `FND-03`** — removia linhas do **corpo**, e `RA-4` de `ADR-0012` exige filtro **por chave de frontmatter** |
| **`H-A` dos objetos submetidos** | **2 de 2 medidos** — `PRO-medally` `e7b853f7…f388` *(359 linhas)* · `ADR-0026` `9e6a586d…7da4` *(315 linhas)* | `sha256` de cada arquivo — [PS-2026-014 §3](pacote-soberano-2026-07-31-medally.md) |
| **`H-N` invariante sob `O4`** | **2 de 2** | `IR-02`: `sha256` com as linhas de `IR-03` removidas, **antes e depois** da transicao projetada |
| **`IR-09` — reconstrucao reproduz `H-A`** | **2 de 2** | revertendo **apenas** `status` e `ratificacao` no frontmatter do arquivo pos-`O4`, e remedindo |
| **`O4` alcanca exatamente dois campos** | **`-3` bytes por objeto** — `em-revisao` → `ativo` *(`-5`)* e `pendente` → `ratificada` *(`+2`)*. **`atualizado_em` NAO e tocado** | aritmetica de bytes, conferida nos dois |
| **Camada normativa inalterada** | **71 fontes de `foundation/`, `departments/` e `capabilities/` conferidas · `0` alteradas** | `sha256` de cada `.md` contra `_backups/LucaX-Enterprise-OS_2026-07-31_pre-missao-1-13-4/`, **arquivo a arquivo, nao por agregado** |
| **Bytes admitidos do repositorio de origem** | **`0`** — `G3` = `REWRITE`. **Nenhum arquivo do medAlly foi proposto para entrada** | `AM-01` de [ADR-0026 §5.4](../decisions/ADR-0026-admissao-do-medally-como-primeiro-produto.md) |
| **Bytes ESCRITOS no repositorio de origem, atribuiveis a missao** | **`0`** — **e o manifesto NAO e identico**: **16** caminhos divergem *(1 novo, 15 alterados)*, **todos** material de demonstracao e os seus **3** geradores, **`0`** deles lido ou executado pela missao. **As 5 fontes consumidas estao byte a byte identicas**, e **todas** as contagens publicadas remedem igual — exceto o total de arquivos, **550 → 551** | manifesto `sha256` de **527** arquivos *(`cc6fbbcf…aadc`)* tomado **antes** de qualquer leitura e **remedido** ao fim; delta enumerado caminho a caminho em [PS-2026-014 §2.2](pacote-soberano-2026-07-31-medally.md) — **`RD-59`** |
| **Produtos em vigor** | **`0`** — `products/` **nao existe** na raiz; **`0`** artefatos de tipo `PRO` no catalogo | varredura do acervo |
| **`Spec`s criadas** | **`0`** — `RD-33` **permanece bloqueante** | `SF-23` item (9); [FND-11 §13](../foundation/11-framework-specifications.md) |
| **Links relativos resolvidos** | **2.936 verificados · 0 quebrados** | **Metodo de §10.5 a §10.9, aplicado sem alteracao.** **A Carta candidata esta FORA do acervo e por isso fora desta varredura** — ressalva `R2` de [FIT-2026-019](fitness/FIT-2026-019-admissao-do-medally.md) |
| **Autoverificacao** | **136 artefatos com `autor` e `revisor` · 0 coincidencias** | comparacao dos dois campos de frontmatter (`ADR-0005`) |
| **Credencial em texto** | **`0` ocorrencias** | varredura por padrao de segredo sobre **194** artefatos (`PI-08`, `LV-02`) |
| **Copia datada anterior as edicoes** | **567** arquivos, fora do acervo | `_backups/LucaX-Enterprise-OS_2026-07-31_pre-missao-1-13-4/` (`PI-07`, `AF-35`) |
| **Candidato fora do acervo** | **1** — `PRO-medally`, em `_candidatos-LucaX-Enterprise-OS-2026-07-31-M1.13.4/products/medally/carta.md` | **Deliberadamente FORA da raiz**, para nao repetir `RD-53` |

> **§10.0.2 a §10.9 nao foram editadas**, exceto o campo *Superada por* de `BL-2026-07-30-02`,
> que e o par de sucessao, e a **renumeracao de §10.0.x** — que desloca subsecao, **nunca valor**.
>
> **O limite da impressao digital continua declarado.** Ela cobre **caminhos e contagens de
> linha** e **nao** detecta edicao que preserve o numero de linhas (`PI-10`, `LV-12`). **A
> verificacao desta missao nao depende dela:** a camada normativa foi comparada por `sha256`
> **arquivo a arquivo** contra a copia datada, e os dois objetos submetidos foram medidos **um a
> um** com instrumento **validado contra dez controles publicados antes do uso**.
> **A impressao digital e o resumo, nao a prova.**


### 10.11 Evidencia de integridade — `BL-2026-07-31-02`

Medida com o **instrumento corrigido** (`RD-53`), **apos** todas as edicoes da Missao 1.13.4.1.
A raiz e enumerada por **lista fechada positiva**, e entrada nao declarada **para** a medicao.

| Evidencia | Valor | Como reproduzir |
|---|---|---|
| Contagem de artefatos | **195** | `sh ferramentas/baseline.sh <acervo>` — lista fechada `README.md capabilities decisions departments foundation governance memory rfcs`, com **portao de raiz** e **portao de split** |
| Contagem de linhas | **57.769** | idem |
| **Impressao digital do acervo** | `74b62fe9fd750c736778b3c420d969661989bac7ae4ac78c8f3cd711e0858335` | idem |
| **Baseline anterior reproduzida antes da escrita** | **`BL-2026-07-31-01`: 194 · 56.854 · `b355e227b6c0a842dc1be0e0a78f2030a88e7a7ab7cd2686103bc1b9752775bf`** | reproducao integral **antes** de qualquer edicao, e **reconferida na copia datada** |
| **O comando corrigido reproduz em execucoes independentes** | ✅ **3 de 3**, hash identico nos 64 digitos — acervo vigente · copia datada · via PowerShell | [PT-2026-012 §2.3](relatorio-transicao-2026-07-31-manutencao-instrumentos.md) |
| **Baseline historica recuperada pelo instrumento corrigido** | ✅ **`BL-2026-07-30-01`: 185 · 54.190 · `3d8dbea0f9ee534707156c54fa2ab58c95640ef0fb2436a981b50bb2adea84da`** — **sobre a copia em que o comando publicado dava 198.** A baseline sempre esteve certa | `sh ferramentas/baseline.sh _backups/LucaX-Enterprise-OS_2026-07-30_pre-missao-1-13-3` |
| **Portao de raiz exercido contra caso real** | ✅ **recusa medir** e sai com codigo **2**, nomeando `_candidatos` — a condicao exata de `RD-53` | idem, sobre a copia de 1.13.3 |
| **`IR-02`/`IR-03`/`O4` validados antes do uso** | ✅ **8 de 8** controles publicados reproduzem — `H-A`, `H-N` e `H-P` de `ADR-0026`; `H-A` e `H-N` de `RFC-0021`; `H-A`, `H-N` e `H-P` da Carta candidata `PRO-medally` | `sh ferramentas/hashes.sh` conferido contra [PS-2026-014 §3](pacote-soberano-2026-07-31-medally.md), **antes** de medir qualquer objeto novo |
| **Instrumento de manifesto validado antes do uso** | ✅ **4 de 4** classes de delta — novo de conteudo, novo volatil, alterado e removido —, cada uma detectada e **classificada**, contra controle **fabricado**. **`0` escritas no repositorio externo para calibrar** | `sh ferramentas/manifesto.sh comparar <antes> <depois>` |
| **Camada normativa** | **71 fontes conferidas · exatamente 1 alterada** — `TPL-carta-produto` **1.1.0**, autorizada por `FND-09 §8.2` linha `TPL`. As outras **70** sao **byte a byte identicas** | `sha256` de cada `.md` contra `_backups/LucaX-Enterprise-OS_2026-07-31_pre-missao-1-13-4-1/`, **arquivo a arquivo, nao por agregado** |
| **Bytes fora dos diffs autorizados** | **`0`** — **4** artefatos alterados e **1** criado, todos enumerados em [PT-2026-012 §9.2](relatorio-transicao-2026-07-31-manutencao-instrumentos.md). **`0` removidos** | comparacao `sha256` **arquivo a arquivo** contra a copia datada |
| **Fundacionais, `ADR`, `MSG`, `FIT`, `PT` historicos e baselines editados** | **`0`** — inclusive `ADR-0005`, `ADR-0007` e `ADR-0012`, que as tres minutas alcancariam | `sha256` contra a copia datada |
| **Pacote da 1.13.4 alterado** | **`0` bytes** — `PS-2026-014`, `PT-2026-011`, `FIT-2026-019`, `ADR-0026` e `RFC-0021` **binariamente intactos** | idem |
| **Bytes ESCRITOS no repositorio externo, atribuiveis a missao** | **`0`** — e **o manifesto NAO reproduz**: **52** caminhos alterados, **`0`** novos, **`0`** removidos, **52 de 52 atribuidos** a processo e janela. **O que reproduz e o INSTRUMENTO, nao a arvore viva** | manifesto de **531** arquivos, `2a9a2725701a6e7859010419269b4ad451d9eafa46d1966c62f348d21311600e`, tomado **antes de qualquer leitura de conteudo** e **remedido** no fechamento — §10.11.1 |
| **Bytes admitidos do repositorio externo** | **`0`** | nenhum candidato foi julgado nesta missao |
| **Item 0 — caminhos atribuidos a processo e horario** | ❌ **14 de 19 a processo · 19 de 19 a horario · 5 NAO ATRIBUIVEL** — nenhuma mudanca da janela foi **commitada**, e sem commit nao ha registro de autoria. **`0` sobra silenciosa** e **`0` escritores concorrentes no acervo**. **Ordem gerador × gerado: 2 compativeis, 1 incompativel** | [PT-2026-012 §1](relatorio-transicao-2026-07-31-manutencao-instrumentos.md) |
| **Escritor concorrente no acervo** | **nenhum** — os **11** `.md` alterados em 2026-07-31 antes desta missao sao **exatamente** as saidas da 1.13.4; os dois arquivos restantes sao estado do editor Obsidian, **na lista de exclusao da propria baseline** | `mtime` de todos os arquivos e diretorios do acervo |
| **Lease e fencing** | **vivo do inicio ao fim** — `fencing_token: 1`, adquirido **antes** da primeira escrita e liberado **so** apos a pos-verificacao | `_leases/LucaX-Enterprise-OS.lease`, **fora do acervo** |
| **Produtos em vigor · `Spec`s criadas** | **`0`** e **`0`** — `products/` **nao existe**; **`RD-33` permanece bloqueante** | varredura do acervo |
| **Links relativos resolvidos** | **2.974 verificados · 0 quebrados** | metodo de §10.5 a §10.10, aplicado sem alteracao |
| **Autoverificacao — pelos DOIS criterios** | **`0`** por divergencia de campo · **`130`** por independencia de fornecedor, sobre **137** artefatos com os dois campos. **Os 7 restantes sao os atos do Soberano** | comparacao de `autor` e `revisor` (`ADR-0005`), **e** classificacao por fornecedor — [PT-2026-012 §6.1](relatorio-transicao-2026-07-31-manutencao-instrumentos.md) |
| **Credencial em texto** | **`0` ocorrencias** | varredura por padrao de segredo (`PI-08`, `LV-02`) |
| **Copia datada anterior as edicoes** | **572** arquivos, fora do acervo, **com a baseline reconferida na copia** | `_backups/LucaX-Enterprise-OS_2026-07-31_pre-missao-1-13-4-1/` (`PI-07`, `AF-35`) |
| **Ponto de rollback por `H-A`** | **194** artefatos; `sha256` do proprio ponto `0f0a3fba6be8759b9092ae455d4bcd2890436b134a152bab36f04eb38d0745dd` | tomado **antes** de qualquer escrita |
| **Candidatos fora do acervo** | **4** — `PRO-medally` *(1.13.4)* e as Cartas `DEP-OPS`, `DEP-GRW` e `DEP-TLS` **1.2.0** *(`RD-49`)*. Mais **3 minutas**, sem numero atribuido | **Deliberadamente FORA da raiz**, para nao repetir `RD-53` |

> **§10.0.2 a §10.10 nao foram editadas**, exceto o campo *Superada por* de `BL-2026-07-31-01`,
> que e o par de sucessao, e a **renumeracao de §10.0.x** — que desloca subsecao, **nunca valor**.
>
> **O limite da impressao digital continua declarado, e agora ela tem portao.** Ela cobre
> **caminhos e contagens de linha** e **nao** detecta edicao que preserve o numero de linhas
> (`PI-10`, `LV-12`) — isso nao mudou. **O que mudou e que ela deixou de poder medir a arvore
> errada em silencio:** raiz nao declarada **para** a medicao, e `xargs` quebrado em lotes
> **para** a medicao. **A impressao digital continua sendo o resumo, nao a prova** — a prova e a
> comparacao `sha256` arquivo a arquivo contra a copia datada.

#### 10.11.1 O manifesto do repositorio externo — **o instrumento reproduz; a arvore viva, nao**

| Campo | Valor |
|---|---|
| Arquivos no manifesto | **531** *(exclui `.git/`, `.mypy_cache/` e `.pytest_cache/`, declarado)* |
| `sha256` do manifesto de **abertura** | `2a9a2725701a6e7859010419269b4ad451d9eafa46d1966c62f348d21311600e` |
| `sha256` do manifesto de **fechamento** | `48c5e92e62b6d49ffa4f56f9e7ae983d6a58467eb4a4183030d905b615e2d26c` |
| **Delta abertura → fechamento** | **52 caminhos: `0` novos · 52 alterados · `0` removidos.** Total de arquivos **554 → 554** |
| Atribuicao | ✅ **52 de 52** — **44** sob `sessoes-convidado/` *(execucao de `ferramentas/explorar.py`, 10:01:58 → 10:03:39)*, **7** de sessao de desenvolvimento *(10:10:40 → 10:17:01)* e **1** `.pyc` volatil. **`0` nao atribuiveis · `0` atribuiveis a esta missao** |

> **A diferenca em relacao a 1.13.4 nao esta no resultado — esta no metodo.** La a prova deixou
> de ser o manifesto e virou **lista escrita a mao**, que omitiu **3 de 4** arquivos novos
> (`RD-60`). Aqui o delta e **calculado**, o volatil e **classificado em vez de descartado**, e
> **nenhum passo depende de alguem redigir a lista**.

### 10.12 Evidencia de integridade — `BL-2026-07-31-03`

Medida com o **instrumento corrigido** (`RD-53`), **apos** todas as edicoes da Missao 1.13.4.2.

| Evidencia | Valor | Como reproduzir |
|---|---|---|
| Contagem de artefatos | **206** | `sh ferramentas/baseline.sh <acervo>` — lista fechada positiva, com portao de raiz e portao de split |
| Contagem de linhas | **60.151** | idem |
| **Impressao digital do acervo** | `17a5ea411b4fb0871ff632e330cf18c5d42755971a4206fb9b4feba97356986d` | idem |
| **Baseline anterior reproduzida antes da escrita** | ✅ **`BL-2026-07-31-02`: 195 · 57.769 · `74b62fe9fd750c736778b3c420d969661989bac7ae4ac78c8f3cd711e0858335`** — reproducao integral **antes** de qualquer edicao, e **reconferida na copia datada** | [PT-2026-013 §0](relatorio-transicao-2026-07-31-emendas-de-instrumento.md) |
| **Instrumento de hash calibrado antes do uso** | ✅ **8 de 8** controles de [PS-2026-014 §3](pacote-soberano-2026-07-31-medally.md) reproduzem nos 64 digitos. O instrumento foi **estendido** para `aprovado → ativo` (`LM-02`), e a extensao **nao move nenhum controle publicado** | `sh ferramentas/hashes.sh` |
| **`P1` — `H-N` invariante sob `O4`** | ✅ **3 de 3** nos `ADR` candidatos | `IR-02` |
| **`P2` — `IR-09` reconstroi `H-A`** | ✅ **3 de 3** | `IR-09`, por DEP-QAR |
| **`P3` — `O4` alcanca exatamente os campos declarados** | ✅ `ADR-0027` **`−5` bytes / 1 campo**; `ADR-0028` e `ADR-0029` **`−3` bytes / 2 campos**. **`atualizado_em` NAO e tocado: `0` ocorrencias no diff** | `IR-08` |
| **`H-P` publicado somente onde ha `O4`** | ✅ **3 de 9.** `RFC` termina em `aprovado` e `FIT` nasce `ativo` — **publicar `H-P` deles seria publicar transicao que nunca ocorre** | [PS-2026-015 §2.1](pacote-soberano-2026-07-31-emendas-de-instrumento.md) |
| **Dependencia entre as tres emendas** | **`0`**, por **quatro** medicoes independentes — referencia cruzada, norma alcancada, intersecao de arquivos e alcance de `AV-3`. **Por isso NAO ha conjunto atomico** | [PS-2026-015 §3](pacote-soberano-2026-07-31-emendas-de-instrumento.md) |
| **Camada normativa** | **`0` fontes alteradas** — `FND-01` a `FND-11`, as **23 `CAP`**, os **19 `TPL`** e as **9 Cartas** byte a byte identicos a copia datada | `sha256` arquivo a arquivo |
| **Fundacionais, `ADR`, `MSG`, `FIT`, `PT` historicos e baselines editados** | **`0`** — inclusive **`ADR-0005`, `ADR-0007`, `ADR-0012` e `FND-10`**, que as tres emendas alcancariam | idem |
| **Pacote da 1.13.4 alterado** | **`0` bytes** — `PS-2026-014`, `PT-2026-011`, `FIT-2026-019`, `ADR-0026` e `RFC-0021` intactos | idem |
| **Contador exercido, nao lido** | ✅ **9 de 9** testados contra a copia datada: **nenhum existia**. `ADR` **26 → 29** · `RFC` **21 → 24** · `FIT` **19 → 22** | `V1` de `MEM-APR-0006` |
| **Autoverificacao — pelos DOIS criterios** | **`0`** por divergencia de campo · **`131`** por independencia de fornecedor, sobre **138** artefatos com os dois campos. **Os 7 restantes sao os atos do Soberano.** **Remedido nesta missao**, nao herdado da 1.13.4.1 *(que mediu `0`/`130` sobre `137`)* | `sh ferramentas/autoverificacao.sh` |
| **Atos emitidos · candidatos julgados · Produtos admitidos · `Spec`s criadas** | **`0`** em cada. **`RD-33` permanece bloqueante** | varredura do acervo |
| **Copia datada anterior as edicoes** | **573** arquivos, fora do acervo, **com a baseline reconferida na copia** | `_backups/LucaX-Enterprise-OS_2026-07-31_pre-missao-1-13-4-2/` |
| **Ponto de rollback por `H-A`** | **195** artefatos; `sha256` do proprio ponto `96dfe8ff6b5150721090fe713532b0931ec9baf3ef9b1b3de58769817924caab` | tomado **antes** de qualquer escrita |
| **Escritor unico** | confirmado por **janela de tempo**, nunca por hash de arvore alheia: **`0`** escritas no acervo entre `11:00:00` e a aquisicao do lease | `mtime` de todos os arquivos |
| **Lease e fencing** | **`fencing_token: 4`**, adquirido **antes** da primeira escrita | `_leases/LucaX-Enterprise-OS.lease`, fora do acervo |
| **Links relativos resolvidos** | **3.095 verificados · 0 quebrados** | metodo de §10.5 a §10.11, aplicado sem alteracao |

> **O limite da impressao digital continua declarado.** Ela cobre **caminhos e contagens de
> linha**, e **nao** detecta edicao que preserve o numero de linhas (`PI-10`, `LV-12`). **A
> prova e a comparacao `sha256` arquivo a arquivo contra a copia datada**; a digital e o resumo.


### 10.13 Evidencia de integridade — `BL-2026-07-31-04`

| Evidencia | Valor | Como reproduzir |
|---|---|---|
| Contagem de artefatos | **206** — **inalterada** | `sh ferramentas/baseline.sh <acervo>` |
| Contagem de linhas | **60.355** | idem |
| **Impressao digital do acervo** | `f49717b7e565fef6ceef5701fb8a7968aabbbaa9681b75d5cd54f9a25d3584bf` | idem |
| **Baseline anterior reproduzida antes da escrita** | ✅ **`BL-2026-07-31-03`: 206 · 60.151 · `17a5ea411b4fb0871ff632e330cf18c5d42755971a4206fb9b4feba97356986d`** | medida antes da primeira escrita desta emissao |
| **Conjunto de mudanca** | **4 alterados · `0` criados · `0` removidos.** **1 fonte** — `PS-2026-015`, o **proprio pacote desta missao**, cujo registro proprio se emenda sem alterar historico alheio — e **3 projecoes `M3`** que `CV-04` obriga a acompanhar: este catalogo, `governance/README` e o `README` da raiz. **Nenhuma e norma** | `sha256` arquivo a arquivo |
| **Os 6 objetos do ato recortado** | **`0` bytes tocados** — `RFC-0022`, `ADR-0027`, `FIT-2026-020`, `RFC-0024`, `ADR-0029`, `FIT-2026-022` reproduzem os `H-A` de §6.1.1 | `sh ferramentas/hashes.sh ha` |
| **Os 3 objetos de `E2`, ADIADA** | **`0` bytes tocados** — `RFC-0023`, `ADR-0028`, `FIT-2026-021` intactos. **Adiar nao toca** | idem |
| **Fundacionais, `ADR`, `MSG`, `FIT`, `PT` historicos e baselines editados** | **`0`** | `sha256` contra a copia datada |
| **Pacote da 1.13.4 alterado** | **`0` bytes** | idem |
| **Atos emitidos** | **`0`** — a minuta recortada e **texto submetido**, nunca ato | varredura de `memory/operacional/MSG-*` |
| **Links relativos resolvidos** | **3.098 verificados · 0 quebrados** | metodo de §10.5 a §10.12 |
| **Lease e fencing** | **`fencing_token: 5`**, adquirido antes da primeira escrita desta emissao | `_leases/LucaX-Enterprise-OS.lease` |

### 10.14 Evidencia de integridade — `BL-2026-07-31-05`

| Evidencia | Valor | Como reproduzir |
|---|---|---|
| Contagem de artefatos | **206** — **inalterada** | `sh ferramentas/baseline.sh <acervo>` |
| Contagem de linhas | **60.390** | idem |
| **Impressao digital do acervo** | `1deded95c5d445dea5f92add4c3ab28e61475329b12edd4eec83a8093996b597` | idem |
| **Baseline anterior reproduzida antes da escrita** | ✅ **`BL-2026-07-31-04`: 206 · 60.355 · `f49717b7e565fef6ceef5701fb8a7968aabbbaa9681b75d5cd54f9a25d3584bf`** — reproduzida **no acervo e, de novo, NA COPIA DATADA**, antes da primeira escrita | `sh ferramentas/baseline.sh` sobre o acervo e sobre `_backups/LucaX-Enterprise-OS_2026-07-31_pre-rd-66/` |
| **Conjunto de mudanca** | **3 alterados · `0` criados · `0` removidos.** **`0` fontes** — **este catalogo** *(§7, §10 e frontmatter)* e as **2** projecoes `M3` que `CV-04` obriga a acompanhar: `governance/README` e o `README` da raiz | `sha256` **arquivo a arquivo** contra a copia datada |
| **`PS-2026-015` e os NOVE objetos das tres emendas** | **`0` bytes tocados** — o pacote submetido e os `RFC`, `ADR` e `FIT` de `E1`, `E2` e `E3` reproduzem os `H-A` publicados em `§2` e `§6.1.1` do pacote | `sh ferramentas/hashes.sh ha <arquivo>` |
| **Fundacionais, Cartas, `CAP`, `TPL`, `ADR`, `MSG`, `FIT` e `PT` historicos** | **`0` bytes** — inclusive `FND-03` e `FND-10`, que `RD-66` **cita e NAO emenda** | `sha256` contra a copia datada |
| **Atos emitidos** | **`0`.** Registrar achado e **ato ministerial de DEP-GOV**, nao ato soberano: **nada foi aplicado, ativado, ratificado ou emitido** | varredura de `memory/operacional/MSG-*` |
| **Achados registrados nesta emissao** | **2**, ambos **ABERTOS e NAO corrigidos** — **`RD-66`** *(Baixa)* e **`RD-67`** *(Media)* | §7, itens **90** e **91** |
| **Links relativos resolvidos** | **3.105 verificados · 0 quebrados** | **Metodo de §10.5 a §10.13, aplicado sem alteracao**, agora **por instrumento**: `sh ferramentas/links.sh <acervo>`. **Calibrado antes do uso** — reproduz **3.098 · 0** sobre a copia datada, o valor publicado em §10.13 |
| **Lease e fencing** | **`fencing_token: 6`**, adquirido **antes** da primeira escrita desta emissao | `_leases/LucaX-Enterprise-OS.lease`, fora do acervo |

### 10.15 Evidencia de integridade — `BL-2026-07-31-06`

| Evidencia | Valor | Como reproduzir |
|---|---|---|
| Contagem de artefatos | **206** — **inalterada** | `sh ferramentas/baseline.sh <acervo>` |
| Contagem de linhas | **60.480** | idem |
| **Impressao digital do acervo** | `c454ba6bbfe0e38cf8ec00a4e3210a3383bf4d538a8e88cc4fd0857506577f22` | idem |
| **Baseline anterior reproduzida antes da escrita** | ✅ **`BL-2026-07-31-05`: 206 · 60.390 · `1deded95c5d445dea5f92add4c3ab28e61475329b12edd4eec83a8093996b597`** — reproduzida **no acervo e, de novo, NA COPIA DATADA**, antes da primeira escrita | `sh ferramentas/baseline.sh` sobre o acervo e sobre `_backups/LucaX-Enterprise-OS_2026-07-31_pre-ca-2/` |
| **Conjunto de mudanca** | **4 alterados · `0` criados · `0` removidos.** **1 fonte** — `PS-2026-015` **1.1.0 → 1.2.0**, o **proprio pacote desta missao**, submetido e nao consumido — e **3 projecoes `M3`** que `CV-04` obriga a acompanhar: este catalogo, `governance/README` e o `README` da raiz. **Nenhuma e norma** | `sha256` **arquivo a arquivo** contra a copia datada |
| **Os NOVE objetos das tres emendas** | **`0` bytes tocados** — **9 de 9** `H-A` reproduzem os publicados em `§2`, `§6.1.1` e `§6.1.2` do pacote, **medidos nesta emissao**. E e essa medicao que **funda** a correcao de `CA-2`: **a arvore andou duas vezes e os nove objetos nao** | `sh ferramentas/hashes.sh ha <arquivo>` |
| **Alcance da mudanca dentro de `PS-2026-015`** | **`CA-2` de §6.1.4, a nova §6.1.4.1, o item `VI` da minuta recortada, o frontmatter `versao` e a linha `1.2.0` do historico.** **`0` bytes** em §6.1.1, §6.1.2, §6.1.3, §6.1.5, §6.1.6, §6.1.7, §6.1.8, na minuta integral de §6 e nas demais secoes | `diff` contra a copia datada |
| **`CA-1`, `CA-3`, `CA-4` e `CA-5`** | **BLOQUEANTES, com `0` bytes tocados** — a correcao alcanca **somente `CA-2`** | idem |
| **Fundacionais, Cartas, `CAP`, `TPL`, `ADR`, `RFC`, `MSG`, `FIT` e `PT` historicos** | **`0` bytes** | `sha256` contra a copia datada |
| **Pacote da 1.13.4** | **`0` bytes** — `PS-2026-014`, `PT-2026-011`, `FIT-2026-019`, `ADR-0026` e `RFC-0021` | idem |
| **Atos emitidos** | **`0`.** Corrigir condicao de partida e **ato ministerial de DEP-GOV** sobre pacote submetido: **nada foi aplicado, ativado, ratificado ou emitido** | varredura de `memory/operacional/MSG-*` |
| **Achados registrados nesta emissao** | **`0`.** **`RD-66` e `RD-67` seguem ABERTOS, NAO corrigidos e SEM missao designada** — congelamento declarado pelo Fundador | §7, itens **90** e **91** |
| **Links relativos resolvidos** | **3.107 verificados · 0 quebrados** | `sh ferramentas/links.sh <acervo>`, metodo de §10.5 a §10.14 |
| **Lease e fencing** | **`fencing_token: 7`**, adquirido **antes** da primeira escrita desta emissao | `_leases/LucaX-Enterprise-OS.lease`, fora do acervo |

### 10.16 Evidencia de integridade — `BL-2026-07-31-07`

| Evidencia | Valor | Como reproduzir |
|---|---|---|
| Contagem de artefatos | **207** — **`+1`**, `MSG-2026-0008` | `sh ferramentas/baseline.sh <acervo>` |
| Contagem de linhas | **60.763** | idem |
| **Impressao digital do acervo** | `69815205906e9c2788c9971710c49036a37b072656261fe8269adbcc2d8009cd` | idem |
| **Baseline anterior reproduzida antes da escrita** | ✅ **`BL-2026-07-31-06`: 206 · 60.480 · `c454ba6bbfe0e38cf8ec00a4e3210a3383bf4d538a8e88cc4fd0857506577f22`** — reproduzida **no acervo e, de novo, NA COPIA DATADA** | `sh ferramentas/baseline.sh` sobre o acervo e sobre `_backups/LucaX-Enterprise-OS_2026-07-31_pre-ato-e1-e3/` |
| **Conjunto de mudanca** | **1 criado · 4 alterados · `0` removidos.** Criado: `MSG-2026-0008`. Alterados: **`0` fontes** — este catalogo, `memory/operacional/README`, `governance/README` e o `README` da raiz, **todas projecoes `M3`** | `sha256` **arquivo a arquivo** contra a copia datada |
| **Ancora do ato** | ✅ **`PS-2026-015` 1.2.0 reproduz `3d242ed8470b3808a9b574373a0e4f6b5d37d09d31d5973dc39867d6feeaca62`**, medido **antes e depois** desta emissao. **`0` bytes** — registrar o ato **nao toca o texto assinado** | `sh ferramentas/hashes.sh ha <arquivo>` |
| **`H-P` dos dois objetos com `O4` autorizado** | ✅ **2 de 2** — `ADR-0027` `523e0c81…3a99` e `ADR-0029` `148d6100…8f72` **recalculados sobre os objetos vivos** e identicos aos publicados em `§6.1.1`. **Conferencia, NAO aplicacao** | `sh ferramentas/hashes.sh hp <arquivo>` |
| **Os NOVE objetos das tres emendas** | **`0` bytes tocados** — **9 de 9** `H-A` reproduzem | `sh ferramentas/hashes.sh ha <arquivo>` |
| **Transicoes aplicadas** | **`0`.** `ADR-0027` e `ADR-0029` seguem **`em-revisao`**; `ADR-0029` segue `ratificacao: pendente`; registro de `SA-6` **inexistente**; **`0`** aprovacoes de DEP-EXE | `grep` de `^status:` e `^ratificacao:` nos dois arquivos |
| **Fundacionais, Cartas, `CAP`, `TPL`, `ADR`, `RFC`, `FIT` e `PT` historicos** | **`0` bytes** | `sha256` contra a copia datada |
| **Pacote da 1.13.4** | **`0` bytes** | idem |
| **`MSG` anteriores** | **`0` bytes** — **oito atos, oito fontes**; `MSG-2026-0001` a `0007` intactos (`LV-04`) | idem |
| **Achados registrados nesta emissao** | **1** — **`RD-68`** *(Baixa)*, **valor corrigido por `SF-32`, causa ABERTA e sem missao** | §7, item **92** |
| **Links relativos resolvidos** | **3.130 verificados · 0 quebrados** | `sh ferramentas/links.sh <acervo>` |
| **Lease e fencing** | **`fencing_token: 8`**, adquirido **antes** da primeira escrita | `_leases/LucaX-Enterprise-OS.lease`, fora do acervo |

### 10.17 Evidencia de integridade — `BL-2026-07-31-08`

| Evidencia | Valor | Como reproduzir |
|---|---|---|
| Contagem de artefatos | **208** — **`+1`**, `atos-superados` | `sh ferramentas/baseline.sh <acervo>` |
| Contagem de linhas | **60.921** | idem |
| **Impressao digital do acervo** | `5d3c97960fa125d0cfc573e8a43e3046cec2af4ff292634d8e9ca9597f981baf` | idem |
| **Baseline anterior reproduzida antes da escrita** | ✅ **`BL-2026-07-31-07`: 207 · 60.763 · `69815205906e9c2788c9971710c49036a37b072656261fe8269adbcc2d8009cd`** — no acervo **e na copia datada** | `sh ferramentas/baseline.sh` sobre `_backups/LucaX-Enterprise-OS_2026-07-31_pre-aplicacao-e1-e3/` |
| **Ponto de partida por `H-A`** | **207 artefatos**, manifesto tomado **antes da primeira escrita**; `sha256` do proprio manifesto `d388b539f49a4ce1d2d9c1b301c9f31f1fa250e361b2fe95cfacdcdcf210d8ed` | `_missao-1-13-4-2-2026-07-31/evidencia/H-A-ponto-de-partida-1-13-4-3.txt` |
| **`CP-1` — `H-P` conferido** | ✅ **2 de 2** — `ADR-0027` `523e0c81…3a99` · `ADR-0029` `148d6100…8f72`, identicos aos publicados em `§6.1.1` | `sh ferramentas/hashes.sh hp` antes · `sha256sum` depois |
| **`CP-2` — `H-N` invariante sob `O4`** | ✅ **2 de 2** — `7e2db207…ba9e` e `c3ff590d…e1b0`, identicos aos de `§6.1.1` | `sh ferramentas/hashes.sh hn <arquivo>` |
| **`CP-3` — `IR-09`, reconstrucao reproduz `H-A`** | ✅ **2 de 2**. Revertendo **apenas** `status` e `ratificacao`, o `sha256` volta a `d1e5f6f4…c5e3` e `dc2aa539…9327`. **Executado por DEP-QAR** | reversao dos campos de `IR-03` + `sha256sum` |
| **`CP-4` — `O4` alcancou exatamente os campos declarados** | ✅ `ADR-0027`: **1 campo, `−5` bytes, 1 linha no diff**. `ADR-0029`: **2 campos, `−3` bytes, 2 linhas**. **`atualizado_em` NAO tocado — `0` ocorrencias no diff dos dois** | `diff` contra a copia datada |
| **`CP-5` — os tres objetos de `E2` intactos** | ✅ **3 de 3** — `RFC-0023`, `ADR-0028` e `FIT-2026-021` reproduzem os `H-A` de `§6.1.2`. **O recorte nao falhou** | `sha256sum` contra `§6.1.2` |
| **`CP-6` — `0` bytes fora do conjunto autorizado** | ✅ **201 identicos · 6 alterados · 1 criado · `0` removidos**, conferidos **arquivo a arquivo** (`cmp`). Alterados: os **2 `ADR`** do ato e as **4** projecoes `M3` — este catalogo, `decisions/README`, `governance/README` e o `README` da raiz | `cmp` de cada `.md` contra a copia datada |
| **`CP-7` — nova baseline reproduzivel** | ✅ medida **apos** a ultima escrita e reproduzida em **2 execucoes independentes** | `sh ferramentas/baseline.sh` duas vezes |
| **Pacote da 1.13.4 — `RC-2`** | **`0` bytes** em `PS-2026-014`, `PT-2026-011`, `FIT-2026-019`, `ADR-0026` e `RFC-0021`. **A reclassificacao vive em `ADR-0027`, nunca por reescrita** | `cmp` contra a copia datada |
| **`PS-2026-015` e a ancora do ato** | **`0` bytes** — `3d242ed8…ca62` reproduz **depois** da aplicacao | `sh ferramentas/hashes.sh ha` |
| **Atos emitidos nesta missao** | **`0`.** A missao **executa** o ato de 2026-07-31; **nao emite ato algum**. **8** `MSG` no acervo, inalterado | varredura de `memory/operacional/MSG-*` |
| **Registro de `SA-6`** | **criado, com o contador em `0`** — `0` atos superados, `0` instauracoes abertas | [atos-superados](atos-superados.md) |
| **Achados registrados nesta emissao** | **2** — **`RD-69`** *(Baixa, valor reconciliado, causa ABERTA)* e **`RD-70`** *(Baixa, **ABERTO e NAO corrigido**)*. **Nenhum gerou missao** — congelamento em vigor | §7, itens **93** e **94** |
| **Links relativos resolvidos** | **3.150 verificados · 0 quebrados** | `sh ferramentas/links.sh <acervo>` |
| **Lease e fencing** | **`fencing_token: 9`**, adquirido **antes** da primeira escrita | `_leases/LucaX-Enterprise-OS.lease`, fora do acervo |

### 10.18 Evidencia de integridade — `BL-2026-08-01-01`

| Evidencia | Valor | Como reproduzir |
|---|---|---|
| Contagem de artefatos | **213** — **`+5`**: `RFC-0025`, `ADR-0030`, `FIT-2026-023`, `PT-2026-014`, `PS-2026-016` | `sh ferramentas/baseline.sh <acervo>` |
| Contagem de linhas | **62.250** | idem |
| **Impressao digital do acervo** | `4252fe474a3db86df993265a9eba75fe861c841f65fa0f8f636c09c7697e621c` | idem |
| **Baseline anterior reproduzida antes da escrita** | ✅ **`BL-2026-07-31-08`: 208 · 60.921 · `5d3c97960fa125d0cfc573e8a43e3046cec2af4ff292634d8e9ca9597f981baf`** — no acervo **e na copia datada** | `sh ferramentas/baseline.sh` sobre `_backups/LucaX-Enterprise-OS_2026-08-01_pre-missao-1-13-4-4/` |
| **Ponto de partida por `H-A`** | **208 artefatos**, manifesto tomado **antes da primeira escrita**; `sha256` do proprio manifesto `e48f5908d8d4fbf9484ffacb564f71ee5fa1ebcc2aa99905cb5e859e1faa3caf` | `_missao-1-13-4-4-2026-08-01/evidencia/H-A-ponto-de-partida-1-13-4-4.txt` |
| **`CQ-1` — `G1` fecha por MEDICAO** | ✅ **17 de 17** fontes consumidas com autoria e data atribuiveis a commit · **`0`** nao atribuiveis · **`0`** caminhos sem commit em **183** rastreados · **13.182** ignorados **nao consumidos** · soma **13.365** exata | `git status --porcelain=v1 -uall --ignored -- <sub>`; `git log -- <arquivo>` |
| **`CQ-2` — candidato congelado por objeto de COMMIT** | ✅ `tree(nxtrack)` = **`b9b36be9324ae2d36ddc4149049ebbff9f40fb4b`**, identico em `HEAD` `b9fbccd` *(de hoje)* e em `a7fc0946` *(2026-07-27)*, **e identico apos toda a escrita da missao**. Hash de arvore em disco **nao sobreviveria** ao repositorio vivo | `git rev-parse HEAD:<sub>` |
| **`CQ-3` — escritor concorrente MEDIDO, nao presumido ausente** | ✅ **Presenca detectada** no hospedeiro: **758** caminhos sem commit, sessao de agente ativa **08:25:47** e commit `b9fbccd` as **07:37:40** tocando **1** caminho **fora** do candidato. **`0`** escritas na subarvore apos `T0` | `mtime` × `T0`; `git log --since --name-only` |
| **`CQ-4` — `0` bytes do candidato no acervo** | ✅ **`0` colisoes** entre os **179** hashes distintos dos 183 arquivos rastreados do candidato e **todos** os arquivos do acervo | `Get-FileHash` cruzado |
| **`CQ-5` — `0` fundacionais e `0` historicos alterados** | ✅ **10 de 10 identicos** ao `H-A` do ponto de partida: `FND-01`, `FND-04`, `FND-08`, `FND-09`, `FND-10`, `FND-11`, `ADR-0007`, `ADR-0026`, `ADR-0027` e `TPL-carta-produto` | `sha256` contra o manifesto de partida |
| **`CQ-6` — candidato NAO alterado pela missao** | ✅ `tree` e `HEAD` identicos antes e depois · `git status` da subarvore: **`0`** linhas · **`0`** commits · **`0`** locks · **`0`** execucoes de codigo do candidato · **`0`** bancos abertos | `git rev-parse`; `git status`; inventario de `*.lock` |
| **`CQ-7` — nova baseline reproduzivel** | ✅ medida **apos** a ultima escrita e reproduzida em **2 execucoes independentes** | `sh ferramentas/baseline.sh` duas vezes |
| **Atos emitidos nesta missao** | **`0`.** **8** `MSG` no acervo, inalterado. A minuta de `PS-2026-016 §6` esta **redigida e NAO assinada** | varredura de `memory/operacional/MSG-*` |
| **Produtos admitidos** | **`0`.** `products/` **nao existe**; `ADR-0030` `em-revisao`; **2** candidatos fora do acervo | inventario da raiz |
| **`Spec`s criadas · `RD-33`** | **`0` criadas.** `RD-33` **segue bloqueante**; `S1` **preparada e nao consumida** | unica ocorrencia de `tipo: spec` e `TPL-spec.md` |
| **Achados registrados nesta emissao** | **7** — `RD-71` a `RD-77`: **6 ABERTOS e nao corrigidos**, **1** *(`RD-77`)* corrigido **na projecao**. **Nenhum gerou missao** — congelamento em vigor | §7, itens **95** a **101** |
| **Links relativos resolvidos** | **3.241 verificados · 0 quebrados** | `sh ferramentas/links.sh <acervo>` |
| **Lease e fencing** | **`fencing_token: 10`**, adquirido **antes** da primeira escrita | `_leases/LucaX-Enterprise-OS.lease`, fora do acervo |

### 10.19 Evidencia de integridade — `BL-2026-08-01-02`

| Evidencia | Valor | Como reproduzir |
|---|---|---|
| Contagem de artefatos | **217** — **`+4`**: `PRO-nxtrack`, `MSG-2026-0009`, `PT-2026-015` e `roadmap-canonico` *(preexistente, `RD-80`)* | `sh ferramentas/baseline.sh <acervo>` |
| Contagem de linhas | **63.816** | idem |
| **Impressao digital do acervo** | `e3d68db33155b6dee756ad54303f4ec6198af34b9f57f153be4a8131d1ecabae` | idem |
| **`CA-2` INFORMATIVO — baseline vigente medida e REGISTRADA, jamais exigida** | ✅ A publicada era **`BL-2026-08-01-01`: 213 · 62.250 · `4252fe47…621c`**. **Ela NAO reproduzia no instante da aplicacao, e isso nao para nada:** o instrumento **RECUSAVA medir** — portao de raiz, `CLAUDE.md` nao declarado, saida **`2`** *(`RD-81`)* —, e a recusa foi exercida **no acervo E na copia datada**, com a mesma saida. **A ancora do ato sao os `5` `sha256` por objeto de `CA-4`**, nunca a arvore | `sh ferramentas/baseline.sh` antes do passo 6 |
| **`CB-1` — `CA-4`, os cinco objetos** | ✅ **`5` de `5`** reproduzem os `H-A` de `PS-2026-016 §2`, **lidos do arquivo e nunca da transcricao**, **antes** da primeira escrita: `ADR-0030` `80b4989e…a89f` · `RFC-0025` `0db95362…221c` · `FIT-2026-023` `331fcf47…2cff` · `PT-2026-014` `a6db51da…7929` *(reancorado, `RD-78`)* · candidato `4d4c12e0…75c5`. **O `H-A` do pacote assinado tambem reproduz:** `e6fa26e8…44ae` | `sh ferramentas/hashes.sh ha <arquivo>` |
| **`CB-2` — `H-P` conferido nos DOIS objetos com `O4`** | ✅ **`2` de `2`**. `ADR-0030` → `906dccd303c6240561a30ec5f62253d247567beb661a62b21d3f89b0e7c719fa` · `RFC-0025` → `eecde50420cb88e0619a30cd435506049567259753f8c01d8776ba1d844a7b63`, este **pela variante** *(`status: em-revisao` → `aprovado`, campo unico)*. **O instrumento padrao poria `ativo` em `RFC-0025`, que NAO e a transicao do ato** | `sh ferramentas/hashes.sh ha` apos o `O4`, contra `§2.1` do pacote |
| **`CB-3` — `H-N` invariante ao `O4`** | ✅ **`2` de `2`**, remedidos apos a escrita: `ADR-0030` `6325d9c1…b266` · `RFC-0025` `adb4e4c4…305f`. **`atualizado_em` NAO foi tocado** em nenhum dos dois — o `H-N` invariante e a prova | `sh ferramentas/hashes.sh hn <arquivo>` |
| **`CB-4` — diff literal, medido e nao descrito** | ✅ **`ADR-0030`: 2 linhas** *(`status`, `ratificacao`)* · **`RFC-0025`: 1 linha** *(`status`)*. **Nada mais**, provado por `diff` contra a copia datada | `diff <copia> <acervo>` |
| **`CB-5` — `H-A` do arquivo APLICADO, publicado** | ✅ `products/nxtrack/carta.md` = **`fca656a904e67b11b965354233b7352be9cf41131c88fda2baebc30e8eb039e2`**, **medido no acervo**. **Distinto do `H-A` do candidato** *(`4d4c12e0…75c5`, em `_missao-1-13-4-4-2026-08-01/candidatos/`)*, que **nao e artefato** — `DF-1` e `RD-19` | `sh ferramentas/hashes.sh ha products/nxtrack/carta.md` |
| **`CB-6` — a transformacao do candidato foi CALCULADA, nao redigida** | ✅ **5** substituicoes literais declaradas, cada uma com motivo: **2 ORDENADAS** pelo ato *(`status`, `ratificacao`)* e **3 CONSEQUENTES** dele — o bloco *"NAO E ARTEFATO DO ACERVO"*, o link relativo que so resolvia de fora, e as duas linhas de `§14` sobre `ADR-0030` e a decisao do Soberano. **O instrumento ABORTA se qualquer uma nao casar exatamente uma vez.** Achado **`RD-86`** | `_missao-1-13-4-5-2026-08-01/ferramentas/aplicar-carta.py`; `diff` candidato × aplicado |
| **`CB-7` — `0` bytes fora do conjunto autorizado, ARQUIVO A ARQUIVO** | ✅ ****584 identicos + 10 alterados + 2 criados + 0 removidos**, soma **596** exata contra o manifesto posterior. Dos **10** alterados, **9 sao autorizados** — os `2` do `O4`, o catalogo, as `5` projecoes `M3` e o roadmap, este pela regra de `CLAUDE.md` e nao pelo ato — **e `1` e VOLATIL declarado**: `.obsidian/workspace.json`, raiz `NAO_ACERVO`, escrito pelo **proprio Obsidian** e nao por esta missao. **Nada foi descartado do delta** — o que e volatil e **classificado**, que e a regra que `RD-59` fixou** | `diff` de manifestos `sha256` contra a copia datada |
| **`CB-8` — `0` fundacionais e `0` historicos alterados** | ✅ ****194 de 194 identicos** ao `H-A` do ponto de partida: **11** `FND` · **19** `TPL` · **8** revisoes de `foundation/` · **23** `CAP` · **9** Cartas de Departamento · **29** `ADR` *(todos menos `ADR-0030`)* · **24** `RFC` *(todos menos `RFC-0025`)* · **23** `FIT` · **15** `PS` · **14** `PT` preexistentes · **9** `MSG` · **2** `INC` · **7** `MEM` · `atos-superados`. **`ADR-0007`, `ADR-0026`, `ADR-0027`, `PS-2026-016` e `MSG-2026-0009` estao entre os 194** — o texto assinado **nao foi tocado**** | `sha256` contra o manifesto de partida |
| **`CB-9` — candidato INTACTO, por objeto de commit** | ✅ `tree(nxtrack)` = **`b9b36be9324ae2d36ddc4149049ebbff9f40fb4b`**, identico **antes e depois** · `git status` da subarvore: **`0`** linhas · **`0`** commits, **`0`** escritas, **`0`** execucoes de codigo do candidato. **O `HEAD` do HOSPEDEIRO andou** — `b9fbccd` *(07:37:40)* → `6f81dfc` *(21:20:26)* —, **por trabalho de terceiro FORA do candidato**, e por isso a ancora e o `tree` da subarvore: achado **`RD-83`** | `git -C <lucaX> --no-optional-locks rev-parse HEAD:<sub>` |
| **`CB-10` — nova baseline reproduzivel** | ✅ medida **apos** a ultima escrita e reproduzida em **2 execucoes independentes**, com o medidor ja declarando `products` e `CLAUDE.md` | `sh ferramentas/baseline.sh` duas vezes |
| **`CB-11` — o medidor foi DECLARADO, nao afrouxado** | ✅ `ACERVO` recebe **`products`** *(passo 6, `OA-1`)* e `NAO_ACERVO` recebe **`CLAUDE.md`** *(decisao do dono do achado `RD-81`, o SOBERANO, no despacho de abertura)*. **A lista continua fechada e positiva, o portao de raiz continua parando com erro, e o portao de split continua exigindo uma linha `total`** — **`0` regras removidas** | `diff` do instrumento herdado × o desta missao |
| **Atos emitidos nesta missao** | **`0`.** **9** `MSG` no acervo, **inalterados** — a missao **consome** o nono ato, nao emite ato algum | varredura de `memory/operacional/MSG-*` |
| **Produtos admitidos** | **`1`** — `PRO-nxtrack`, `ativo` · `ratificada`. **1** candidato integro **nao** admitido: `PRO-medally` | inventario de `products/` |
| **`Spec`s criadas · `RD-33`** | **`0` criadas.** `RD-33` **segue bloqueante**, e **por reserva do ato**, nao por ausencia de Produto | unica ocorrencia de `tipo: spec` e `TPL-spec.md` |
| **Achados registrados nesta emissao** | **5** — **`RD-83`** a **`RD-87`**, todos **ABERTOS com dono e gatilho**. **`RD-81` FECHADO** pelo proprio dono, o SOBERANO. **Nenhum gerou missao** — congelamento em vigor | §7, itens **107** a **111** |
| **Links relativos resolvidos** | ****3.358 verificados · `0` quebrados**** | `sh ferramentas/links.sh <acervo>` |
| **Lease e fencing** | **`fencing_token: 11`**, adquirido **antes** da primeira escrita | `_leases/LucaX-Enterprise-OS.lease`, fora do acervo |

### 10.20 Evidencia de integridade — `BL-2026-08-01-03`

| Evidencia | Valor | Como reproduzir |
|---|---|---|
| Contagem de artefatos | **218** — **`+1`**: `PT-2026-016`. **`0`** removidos | `sh ferramentas/baseline.sh <acervo>` |
| Contagem de linhas | **64.383** | idem |
| **Impressao digital do acervo** | `94b85d8f0daadbf70265b869b433880ba07ccdcd2c64d094d5bc37810d5d5be5` | idem |
| **`CC-1` — a baseline anterior reproduziu ANTES da primeira escrita** | ✅ **`BL-2026-08-01-02` = 217 · 63.816 · `e3d68db3…abae`**, medida no acervo **e** na copia datada, **identica nas duas**. **Medir e depois comparar**, nunca o contrario | `sh ferramentas/baseline.sh` nos dois caminhos |
| **`CC-2` — o instrumento foi CALIBRADO no mesmo instante, e nao foi afrouxado** | ✅ Portao de raiz com entrada nao declarada: **recusa, saida `2`**. Portao de split: **uma** linha `total`. **`0` regras removidas**, `0` bytes no medidor | copia da copia datada + `touch` de entrada nao declarada |
| **`CC-3` — o rito foi DETERMINADO antes de exercido** | ✅ **`0`** regras de rito de fechamento de achado existem no acervo — varredura em `foundation/`, `decisions/`, `rfcs/` e `governance/README`. O rito veio de **`PA-01`, `PA-03`, `PA-07`, `PA-13`, `AU-06`, `FND-04 §4 [7]`** e de **cinco precedentes medidos**, cada um seguindo o rito da materia que removia a causa | [PT-2026-016 §2](relatorio-transicao-2026-08-01-fechamento-rd-33.md) |
| **`CC-4` — a reserva do item VII, medida por varredura literal** | ✅ *ato*, *ratificacao*, *`C3`* e *`1.13.5`* tem **`0`** ocorrencias no item **VII** e em `LA-3`. **A reserva e temporal e de sede** | `grep` no bloco de `PS-2026-016 §6.3` e em `MSG-2026-0009 §2.1` |
| **`CC-5` — prova do destravamento por EXERCICIO, nao por leitura** | ✅ `DoR` de `SF-23` reexercido: item **(9)** **PASSA** *(1 Produto `ativo` · `ratificada`)*; item **(4)** em **5 de 5** `Capabilities` **ativas**. Os **7** restantes sao propriedades da `Spec` a escrever e **nao foram afirmados** | [PT-2026-016 §3](relatorio-transicao-2026-08-01-fechamento-rd-33.md) |
| **`CC-6` — `0` bytes nas tres fontes do vinculo** | ✅ `FND-04`, `FND-03` e `FND-10` identicos ao `H-A` do ponto de partida. **O vinculo foi SATISFEITO, nunca removido** — remove-lo continua sendo `S2` | `diff` do manifesto `H-A` |
| **`CC-7` — `0` bytes fora do conjunto autorizado, ARQUIVO A ARQUIVO** | ✅ ver [PT-2026-016 §8.2](relatorio-transicao-2026-08-01-fechamento-rd-33.md) | `diff` de manifestos de **596** arquivos |
| **`CC-8` — fundacionais e historicos intactos** | ✅ **11** `FND` · **19** `TPL` · **23** `CAP` · **9** Cartas `DEP` · **1** Carta `PRO` · **30** `ADR` · **25** `RFC` · **23** `FIT` · **15** `PS` · **15** `PT` anteriores · **9** `MSG` · **2** `INC` · **7** `MEM` · `atos-superados` — **todos com `0` bytes** | idem |
| **`CC-9` — nova baseline reproduzivel** | ✅ medida **apos** a ultima escrita e reproduzida em **2 execucoes independentes** | `sh ferramentas/baseline.sh <acervo>` |
| **Atos emitidos nesta missao** | **`0`.** **9** `MSG` no acervo, **inalterados**. A missao **executa autoridade ja exercida**, e por isso **nao emite nem consome ato** | `ls memory/operacional/MSG-*` |
| **Produtos admitidos · bytes em `products/`** | **`0`** e **`0`**. `PRO-nxtrack` permanece o unico, **inalterado** | manifesto `H-A` |
| **`Spec`s criadas · `RD-33`** | **`0` criadas**, e criar a primeira e a Missao **1.13.5**. **`RD-33` ✅ FECHADO** — e o residuo **(b)** migrou para **`RD-88`**, ABERTO | unica ocorrencia de `tipo: spec` continua sendo `TPL-spec.md` |
| **Achados registrados nesta emissao** | **3** — **`RD-88`** *(migrado de `RD-33`, ABERTO)*, **`RD-89`** *(corrigido na projecao)* e **`RD-90`** *(ABERTO)*. **`RD-33` FECHADO**; **`RD-80` e `RD-83` a `RD-87` declarados e NENHUM fechado** | §7 |
| **Lease e fencing** | **`fencing_token: 12`**, adquirido **antes** da primeira escrita | `_leases/LucaX-Enterprise-OS.lease`, fora do acervo |

### 10.21 Evidencia de integridade — `BL-2026-08-02-01`

| Evidencia | Valor | Como reproduzir |
|---|---|---|
| Contagem de artefatos | **223** — **`+5`**: `RFC-0026`, `ADR-0031`, `SPC-001`, `FIT-2026-024`, `PT-2026-017`. **`0`** removidos | `sh ferramentas/baseline.sh <acervo>` |
| Contagem de linhas | **66.100** | idem |
| **Impressao digital do acervo** | `cd5ab24eba814472373a7c94bfc7ba2bdd3afcce83b71b2fe461d7405a8e080a` | idem |
| **`CD-1` — a baseline anterior reproduziu ANTES da primeira escrita** | ✅ **`BL-2026-08-01-03` = 218 · 64.383 · `94b85d8f0daadbf70265b869b433880ba07ccdcd2c64d094d5bc37810d5d5be5`**, nos tres valores. **Medir e depois comparar**, nunca o contrario | `sh ferramentas/baseline.sh <acervo>` |
| **`CD-2` — a materia foi remedida, e o INSTRUMENTO foi validado antes de se acreditar no zero** | ✅ A primeira execucao devolveu **`0` para os 21 termos, inclusive `senha_hash`**, que a Carta declara existir — **defeito de instrumento**, descartado. Com **controle positivo** *(`senha_hash` = **11**, `nxtrack` = **527**, `def ` = **691**, `import` = **666**)*, `LM-6(a)` foi remedido e **reproduziu `0` nos seis termos**, em **duas** varreduras *(183 rastreados e 262 da arvore de trabalho)*, com padrao **mais largo** que o publicado | Item 0 da missao, §2 e §3 |
| **`CD-3` — o candidato NAO mudou, e a ancora e o `tree`, nao a data** | ✅ `tree` de `My_WorkSpace/Meus_projetos/nxtrack` = **`b9b36be9324ae2d36ddc4149049ebbff9f40fb4b`**, **identico** ao publicado em `PRO-nxtrack §14` e `PT-2026-014 §5` | `git rev-parse "HEAD:<subpasta>"` no repositorio de terceiro |
| **`CD-4` — repositorio de terceiro em SOMENTE LEITURA** | ✅ **`0`** escritas · **`0`** execucoes de programa do candidato · **`0`** bancos abertos. Todo schema foi lido em **codigo rastreado** | manifesto de leitura do Item 0 |
| **`CD-5` — a classe foi DERIVADA, e a derivacao e reproduzivel por terceiro** | ✅ Colisao entre a coluna `C1 · T2` de `SF-10 §5` e `FND-04 §3.1` — *Proponente = Aprovador* para `SPC` —, que `LV-03` torna **nula**. `C2` e o **menor** valor da matriz que a dissolve. **4 de 4** incompatibilidades absolutas conferidas | Leitura confrontada de duas fontes vigentes; `SPC-001` Bloco 5 |
| **`CD-6` — `DoR` e `DoD` EXERCIDOS, com o lugar da conferencia declarado** | ✅ `DoR` **9 de 9**, `DoD` **10 de 10**. **`60`** campos de `SF-12` contados por ferramenta, `0` ausentes. **`0`** ocorrencias dos dez adjetivos vedados de `SF-16` | `SPC-001`, blocos `DoR` e `DoD`; contagem por `grep` |
| **`CD-7` — o `FIT` foi EXIGIDO pela classe, nao escolhido** | ✅ `SF-24` item **(9)**: *"`FIT` emitido se `C2` ou `C3`"*. Objeto `C2` ⇒ [`FIT-2026-024`](fitness/FIT-2026-024-primeira-spec.md), autor **DEP-QAR** ≠ produtor **DEP-PRD** | `CC-04`, `QG-6` |
| **`CD-8` — contadores EXERCIDOS, nao lidos — e dois estavam defasados** | ✅ `ADR` declarava `0030` disponivel com **`ADR-0030` ja existente**; `RFC` declarava `0025` com **`RFC-0025` ja existente**. Testada a existencia contra a **copia datada**, `0031` e `0026` estavam livres. **Achado `RD-95`**, quarta ocorrencia da familia de `RD-32` | `ls` contra `_backups/…_2026-08-01_pre-missao-1-13-5/` |
| **`CD-9` — `0` bytes na camada normativa e nos historicos** | ✅ **11** `FND` · **19** `TPL` · **23** `CAP` · **9** Cartas `DEP` · **1** Carta `PRO` · **30** `ADR` anteriores · **25** `RFC` anteriores · **23** `FIT` anteriores · **15** `PS` · **16** `PT` anteriores · **9** `MSG` · **2** `INC` · **7** `MEM` · `atos-superados` — **todos com `0` bytes** | `diff` do manifesto `H-A` de **597** arquivos |
| **`CD-10` — `0` bytes fora do conjunto autorizado, ARQUIVO A ARQUIVO** | ✅ **589 identicos + 8 alterados + 5 criados + 0 removidos** sobre **597** de partida *(soma 602, exata)*. Dos 8: **7 autorizados** e **1 VOLATIL declarado** — `.obsidian/workspace.json`, raiz `NAO_ACERVO`. **`0`** fora do conjunto e **`0`** autorizados nao tocados. **1.057** links relativos conferidos, **`0`** quebrados | [PT-2026-017 §8.1](relatorio-transicao-2026-08-02-primeira-spec.md) |
| **`CD-11` — nova baseline reproduzivel** | ✅ medida **apos** a ultima escrita e reproduzida em **2 execucoes independentes** | `sh ferramentas/baseline.sh <acervo>` |
| **Atos emitidos nesta missao** | **`0`.** **9** `MSG` no acervo, **inalterados**. `ADR-0031` e `C2 · Tipo 2` e **nao exige ratificacao** | `ls memory/operacional/MSG-*` |
| **`Spec`s criadas** | **`1` — `SPC-001`, a primeira do acervo.** O tipo `spec` deixa de ter uma unica ocorrencia em `TPL-spec.md` | `grep -l "^tipo: spec"` |
| **Achados registrados nesta emissao** | **5** — **`RD-91`** *(Alta, dono SOBERANO)*, **`RD-92`** *(Baixa)*, **`RD-93`** *(Media)*, **`RD-94`** *(Media)* e **`RD-95`** *(Media)*. **`0` fechados.** `RD-80` teve o gatilho disparado pela **terceira** vez e **nao** foi resolvido | §7 |
| **Lease e fencing** | **`fencing_token: 13`**, adquirido **antes** da primeira escrita. **Primeiro lease do acervo cujo titular e DEP-PRD** | `_leases/LucaX-Enterprise-OS.lease`, fora do acervo |
### 10.22 Evidencia de integridade — `BL-2026-08-02-02`

| Evidencia | Valor | Como reproduzir |
|---|---|---|
| Contagem de artefatos | **228** — **`+5`**: `RFC-0027`, `ADR-0032`, `FIT-2026-025`, `PS-2026-017`, `PT-2026-018`. **`0`** removidos | `sh ferramentas/baseline.sh <acervo>` |
| Contagem de linhas | **67.279** | idem |
| **Impressao digital do acervo** | `d9e8b706718cfb234fc703df0ecee47554297d18ec50585a72bf9a971516e213` | idem |
| **`CE-1` — a baseline anterior reproduziu ANTES da primeira escrita** | ✅ **223 · 66.143 · `1aae3f4fa65cc295c56af0cefb1e8388e23afd96517e41c9c75fc5981272ba56`** — os tres valores. Difere de `BL-2026-08-02-01` em **`+43` linhas**, exatamente a escrita autorizada do token 14 no roadmap *(313 → 356)*; **contagem de artefatos inalterada** | `sh ferramentas/baseline.sh <acervo>` |
| **`CE-2` — o Item 0 foi MEDIDO antes de emendar, e mudou a sede da emenda** | ✅ Confronto literal: a celula `C1 · T2` de `FND-11 §5` reproduz **palavra por palavra** `FND-09 §8.2` linha `SPC` *(`DEP-PRD`)* e `FND-04 §2.1` linha `C1` *(`Proprietario + revisor`)*. `PJ-03` + `FND-01 §10` ⇒ **emendar so a projecao nao sana**. **A emenda foi redirecionada para a fonte** | `grep -n` nas tres tabelas; `ADR-0032 §2` |
| **`CE-3` — a coluna foi varrida, nao so a celula** | ✅ **21 linhas** de `FND-09 §8.2` conferidas uma a uma. **`3`** com colapso estrutural — `SPC`, **`PRJ`** e **`TPL`** —, **`9`** contingentes *(proponente variavel, resolvidos por `FND-04 §3.1` caso a caso)* e **`9`** sem colapso | `PT-2026-018 §2.2` |
| **`CE-4` — a classe do rito foi determinada por NORMA CITADA, nunca por analogia** | ✅ **4** fundamentos independentes, todos dizendo `C3`: `FND-04 §2` bloco `C3` *(direitos de decisao)* · `FND-09 §8.2` linha `FND` · `SF-32` · `LM-02`. **`Tipo 2`** vem do campo *Reversao* do mesmo bloco | `ADR-0032 §11` |
| **`CE-5` — `0` bytes na camada normativa e nos historicos** | ✅ **11** `FND` · **19** `TPL` · **23** `CAP` · **9** Cartas `DEP` · **1** Carta `PRO` · **31** `ADR` anteriores · **26** `RFC` anteriores · **24** `FIT` anteriores · **16** `PS` anteriores · **17** `PT` anteriores · **9** `MSG`: **IDENTICOS**, conferidos `sha256` arquivo a arquivo | `diff -rq` contra a copia datada |
| **`CE-6` — os 4 candidatos vivem FORA do acervo, com `H-A`, `H-N` e `H-P`** | ✅ `_candidatos-LucaX-Enterprise-OS-2026-08-02-M1.13.5.1/` — **4** arquivos. **`0`** deles no acervo; **`0` bytes** nos quatro arquivos vivos | `PS-2026-017 §3`; `ls` do diretorio de candidatos |
| **`CE-7` — o `FIT` foi EXIGIDO pela classe, nao escolhido** | ✅ `CC-04` e `CV-07`: *"mudanca `C2`/`C3` nao encerra sem Fitness Check emitido"* (`QG-6`). Objeto `C3` ⇒ [`FIT-2026-025`](fitness/FIT-2026-025-emenda-de-sf-10.md) | `FND-10 §CC-04`; `FND-04 §4.1 CV-07` |
| **`CE-8` — contadores EXERCIDOS, nao lidos** | ✅ **26** `RFC` no acervo com `RFC-0026` como ultimo ⇒ `0027`; **31** `ADR` com `ADR-0031` ⇒ `0032`; **24** `FIT` ⇒ `025`; **15** `PS` de `002` a `016` ⇒ `017`; **17** `PT` ⇒ `018`. **Nenhum estava defasado nesta emissao** — o defeito de `RD-95` **nao reincidiu** | `ls | wc -l` e `grep "^id:"` por familia |
| **`CE-9` — `0` bytes fora do conjunto autorizado, ARQUIVO A ARQUIVO** | ✅ `diff -rq` do acervo inteiro contra `_backups/LucaX-Enterprise-OS_2026-08-02_pre-instrumentos-1-13-5-1` | `diff -rq` |
| **`CE-10` — nova baseline reproduzivel** | ✅ medida **apos** a ultima escrita e reproduzida em **2 execucoes independentes** | `sh ferramentas/baseline.sh <acervo>` |
| **Atos emitidos nesta missao** | **`0`.** **9** `MSG` no acervo, **inalterados**. A minuta esta **redigida e nao emitida** em `PS-2026-017 §6` | `ls memory/operacional/MSG-*` |
| **Fundacionais e Cartas alteradas** | **`0` e `0`.** `ADR-0032` e `aprovado` · `ratificacao: pendente`, e **nao vigora** (`LM-02`) | `diff -rq`; frontmatter |
| **Achados registrados nesta emissao** | **5** — **`RD-96`** *(Alta, linha `PRJ`)*, **`RD-97`** *(Alta, linha `TPL`)*, **`RD-98`** *(Media)*, **`RD-99`** *(Media)* e **`RD-100`** *(Baixa)*. **`0` fechados.** **`RD-91` NAO fecha aqui: fecha pelo ato, e parcialmente** — `C0 · T2` segue colapsada | §7, itens **119 a 123** |
| **`RD-90` — nao varrido, e cresceu** | ⚠️ A renumeracao de §10.0.1→§10.0.18 **desloca subsecao, nunca valor** (`BL-02`), de modo que os ponteiros *Supera* das baselines superadas **continuam apontando para a subsecao errada**. **Nao foi corrigido**, porque corrigi-lo exigiria editar baseline superada, que `BL-02` proibe | §7, item 114 |
| **Lease e fencing** | **`fencing_token: 14`** *(roadmap, Item 0)* e **`15`** *(instrumentos)*, ambos adquiridos **antes** da respectiva escrita, com copia datada e `H-A` de rollback | `_leases/LucaX-Enterprise-OS.lease` |


## 11. Custo de contexto por missao tipica

Medicao real sobre os 131 artefatos, em 2026-07-28. **Nenhuma meta e fixada aqui** — apenas o
custo observado de cada pacote (CE-04).

| Missao tipica | Pacote minimo | Linhas | % do acervo |
|---|---|---|---|
| Qualquer tarefa *(piso obrigatorio)* | nucleo: FND-01 + FND-03 integrais; FND-09 §5/§6.2/§8.2 e FND-10 §2/§4 por recorte | **1.099** + recortes | **3,6%** |
| Criar ou emendar artefato | nucleo + `TPL-documento` + entrada no catalogo | 1.265 | 4,1% |
| Registrar decisao (ADR) | nucleo + FND-07 + `TPL-adr` | 1.737 | 5,6% |
| Encerrar mudanca C2/C3 | nucleo + FND-04 + `TPL-fitness-check` | 1.788 | 5,8% |
| **Criar Carta de departamento** *(medido na Missao 1.6)* | nucleo + FND-02 + **ADR-0011** + `TPL-carta-departamento` + `capabilities/README §10` | **2.347** | **7,6%** |
| **Executar uma revisao estrutural** *(medido na Missao 1.8)* | **Composicao itemizada** em [FIT-2026-007 §F5.1](fitness/FIT-2026-007-revisao-estrutural-i.md) — 4.158 integrais + 648 recortes normativos + **1.230 indices** + 140 recortes | **6.176** | **21,3%** *(sobre `BL-04`)* |
| **Executar um rollout de Cartas** *(medido na Missao 1.9)* | **Composicao itemizada** em [FIT-2026-008 §F5.1](fitness/FIT-2026-008-rollout-das-cartas.md) — 4.779 integrais + 782 recortes normativos + 267 extracoes + **20 indices** | **5.848** | **18,9%** *(sobre `BL-05`)* |
| **Instituir o Framework de um dominio** *(medido na Missao 1.13)* | **Composicao itemizada** em [FIT-2026-015 §F5.1](fitness/FIT-2026-015-framework-de-specifications.md) — a cadeia de autoridade da `Spec` em **15 secoes de 5 fundacionais**, **3 ADR integrais**, **1 Carta**, **7 indices** e **236 linhas de evidencia externa** | **3.578** *(acervo)* · **3.814** *(total)* | **7,72%** · **8,23%** *(sobre `BL-08`)* |
| **Mover o Framework de um dominio de sede** *(medido na Missao 1.13.1)* | **Composicao itemizada** em [FIT-2026-016 §F5.1](fitness/FIT-2026-016-canonizacao-e-propagacao.md) — os **2** ADR e as **2** RFC de origem, `ADR-0021` integral, `FND-01`, `FND-03` e `FND-10` por recorte, as **2** Cartas integrais e **8** indices | **2.934** *(acervo)* | **6,02%** *(sobre `BL-09`)* |
| **Convergir pacotes pendentes num ato unico** *(medido na Missao 1.13.2)* | **Composicao itemizada** em [FIT-2026-017 §F5.1](fitness/FIT-2026-017-convergencia-pre-ratificacao.md) — as **fontes** consumidas, os **13** candidatos **medidos e nao lidos**, e **`0` linhas de evidencia externa** | **~2.100** integrais + **~5.400** medidos por ferramenta | **13,8%** |
| **Ler o ato consolidado em vez dos pacotes** *(medido)* | [PS-2026-013](pacote-soberano-2026-07-30-consolidado.md) — matriz dos 14 objetos + minuta unica | **343** | **0,6%** — contra **2,9%** dos quatro pacotes somados *(**1.581** linhas)*. **Primeira vez que o acervo mede o custo de decidir, e nao o de escrever** |
| **Consumir a norma da `Spec`** *(projetado por `SF-31`, nao medido)* | [ADR-0021](../decisions/ADR-0021-framework-de-specifications.md) `sob-demanda` + [`TPL-spec`](../foundation/templates/TPL-spec.md); para **uma exigencia**, o bloco de `RQ-nn` | **845** *(os dois integrais)* | **1,73%** |
| **Consumir a norma da `Spec` apos o ato** *(projetado, nao medido)* | `FND-11` `sob-demanda` + `TPL-spec` — **`FND-11` nao existe no acervo enquanto nao houver ato, e por isso esta linha nao o referencia por link** *(`LN-03`)* | **671** *(399 + 272)* | **1,38%** — **−20,6%** contra a linha acima |
| **Saber o que distingue os nove departamentos** | [`departments/README §2`](../departments/README.md) — uma tabela | **16** | **0,05%** |
| **Saber o que um departamento custodia e exerce** | `capabilities/README §10.1` — uma linha da tabela | **1** | **0,003%** |
| **Decidir se um departamento pode aprovar ou verificar algo** | Recorte de decisao da Carta — secoes 1, 2, 4, 5 e 10 | **111** *(DEP-QAR)* · **115** *(DEP-ENG)* | **0,4%** |
| **Consultar o criterio do Soberano** | **P1 de MEM-EST-0001 §9** — nunca o registro inteiro (CT-22) | **28** | 0,1% |
| **Decidir C2/C3 com o criterio do Soberano** | nucleo + FND-07 + **P2 de MEM-EST-0001 §9** | 1.591 | 5,1% |
| Auditoria historica | perfil `arquivo` | 0 | 0% |

> **CE-01 permanece:** nenhum papel carrega o acervo por padrao. O piso obrigatorio custa
> **3,6%** do acervo. **O pacote mais caro deixou de ser o de criar Carta:** executar uma
> revisao estrutural custa **21,3%**, e **20% desse pacote sao indices** abertos para propagar.

> **A linha *Consumir a norma da `Spec`* e projecao, e esta rotulada como tal.** As **845**
> linhas sao a soma medida de `ADR-0021` *(573)* e `TPL-spec` *(272)*, mas **o valor real de
> consumo sera menor**, porque `SF-31` obriga blocos independentes e requisito enderecavel por
> `RQ-nn`. **Nao ha `Spec` para medir**, e `CE-04` proibe estimar o ganho — por isso a linha
> declara o **teto integral**, nao o consumo esperado. Ressalvas `R1` e `R2` de
> [FIT-2026-015](fitness/FIT-2026-015-framework-de-specifications.md).

> **A terceira medicao itemizada da serie SUBIU, e a razao esta declarada.** **21,3% → 18,9% →
> 7,72%** nao e a serie: as duas primeiras sao **revisao estrutural** e **rollout de Cartas**, e a
> terceira e **instituicao de dominio** — pacotes de naturezas distintas, e comparar as tres como
> tendencia seria o erro que **RE-08** registrou. **A comparacao valida e contra a Missao 1.12.1**,
> a mais proxima em natureza *(fechar uma questao normativa)*: **2.522 · 5,7% → 3.578 · 7,72%**,
> **+41,9%** em linhas. **A causa e medida:** `RD-22` era **uma** pergunta com **cinco** fontes
> nomeadas no proprio achado; esta missao teve de reconstruir a cadeia inteira da `Spec` **porque
> nenhum lugar a tinha reunida — e era esse o defeito que ela corrigiu**.

> **A serie de missao tem agora duas medicoes itemizadas, e por isso duas comparaveis.** As
> quatro anteriores registraram **um numero**, sem a lista do que entrou, e **nao sao comparaveis**
> (achado **RE-08**). Entre as duas itemizadas ha **descida**: **21,3% → 18,9%**. **A causa esta
> medida, e nao e ganho estrutural:** a Missao 1.8 abriu **1.230 linhas de indices** para propagar
> correcoes por todo o acervo; a 1.9 abriu **20**, porque suas correcoes sao acrescimos
> localizados. **R4 de FIT-2026-002 exige duas descidas consecutivas itemizadas, e esta e a
> primeira.** **Os percentuais das demais linhas permanecem calculados sobre 30.947 linhas**
> *(`BL-05`)*, para que a comparacao entre elas continue valida.

> **Prova exigida pela Missao 1.5.** Uma decisao C2 que precise do criterio do Soberano carrega
> **P2 = 52 linhas** do registro, e nao as **282** que ele tem — **81,6% do
> registro nao e carregado**. O numero e medido por secao, com `sed`+`wc -l` (CE-02, CE-04).
> **O beneficio, porem, nao esta comprovado:** nao ha componente que consuma os pacotes, e isso
> esta declarado como evidencia ausente **A1** em ADR-0010 §8 e como ressalva **R2** em
> FIT-2026-004. **O registro entrou em vigor em 2026-07-28**, e **P1 ganhou seu primeiro
> consumidor** — esta missao. Mas **R2 nao fecha**: o gatilho exige consumidor que **nao seja a
> propria execucao de missao**, e nenhum componente foi criado (REV-ESTRUTURAL-I §10.2).

> **Prova exigida pela Missao 1.6.** Decidir se um departamento pode aprovar ou verificar algo
> passou de *"nao havia fonte"* para **111 linhas** — **29%** da Carta de DEP-QAR, e **0,4%**
> do acervo. E o mesmo mecanismo de recorte do nucleo e dos pacotes `CT-21`, aplicado a um
> **terceiro** objeto. Diferentemente dos pacotes, este **tem consumidor declarado**: os
> cenarios CN-1, CN-3a e CN-3b de REV-DEPARTAMENTO §3.

### 11.1 Carregamento sob demanda e invalidacao

| Instrumento | Regra |
|---|---|
| **Pacote minimo** | O da linha aplicavel acima. Carregar alem dele exige **gatilho declarado** (CE-01) |
| **Sob demanda** | Artefato de perfil `S` entra pelo ID; o conteudo so e aberto se o gatilho ocorrer (FND-10 §8.2) |
| **Resumo operacional** | Uma linha por artefato, em §4 — substitui abrir o arquivo para decidir relevancia |
| **Invalidacao** | Toda medicao deste catalogo tem **data** e vale ate a proxima mudanca C2/C3. Encerrar C2/C3 sem recalcular = mudanca incompleta (RG-03, CV-04). A baseline (§10) e o marco a partir do qual se sabe se a medicao envelheceu |

Template: [`TPL-documento`](../foundation/templates/TPL-documento.md) ·
Norma: [FND-10 §10.4](../foundation/10-artifact-framework.md)

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-GOV | Catalogo inicial: 85 artefatos classificados. |
| 1.1.0 | 2026-07-28 | DEP-GOV | Emenda por ADR-0007 e ADR-0008: proveniencia curada (§9) e baseline como projecao (§10); 93 artefatos. |
| 2.20.0 | 2026-08-02 | DEP-GOV | **Emenda pela Missao 1.13.5.1 — a EMENDA QUE SANA `RD-91`, produzida e NAO aplicada.** §4.2 vai a **61** com `ADR-0032` e `RFC-0027`; §4.5 a **34** com `FIT-2026-025`; §4.7 a **50** com `PS-2026-017` e `PT-2026-018`. **O Item 0 mediu antes de emendar, e a medicao mudou a sede da emenda:** a celula `C1 · T2` de `FND-11 §5`, que `RD-91` nomeava, **reproduz literalmente** `FND-09 §8.2` linha `SPC` e `FND-04 §2.1` linha `C1` — e por `PJ-03` com `FND-01 §10` **emendar so a projecao nao sanaria**. A emenda foi **redirecionada para a fonte**, com cascata declarada. §7 recebe os achados **119 a 123**: **`RD-96`** *(Alta — `FND-09 §8.2` linha **`PRJ`** poe DEP-EXE propondo E aprovando, incondicional)*, **`RD-97`** *(Alta — linha **`TPL`** poe DEP-GOV propondo, revisando E aprovando)*, **`RD-98`** *(Media — a matriz de `FND-11` passara a diferir em 1 celula da copia `M1` de `ADR-0021 §5.3`)*, **`RD-99`** *(Media — `FND-04 §2` manda versao MAIOR em `C3` e 4 emendas exercidas produziram MENOR)* e **`RD-100`** *(Baixa — `FND-11 §14` `L1` e `L2` falsos desde `SPC-001`)*. §10 emite **`BL-2026-08-02-02`**, demove `BL-2026-08-02-01` a **§10.0.1 com os valores ORIGINAIS**, **renumera §10.0.1 a §10.0.17 para §10.0.2 a §10.0.18** *(desloca subsecao, nunca valor)* e cria **§10.22**; **`0` baselines editadas** alem do campo *Superada por* do par de sucessao (`BL-02`). **`RD-90` continua ABERTO e NAO varrido** — corrigi-lo exigiria editar baseline superada; **`RD-80` teve o gatilho disparado pela QUARTA vez e nao foi resolvido**. **Correcao declarada, nao silenciosa:** o frontmatter deste catalogo declarava `versao: 2.18.0` enquanto o historico ja registrava **2.19.0** — divergencia deixada pela emissao anterior, contra `AC-11`, **corrigida adiante nesta emissao** e registrada aqui em vez de emendada em silencio. **`0` atos emitidos, `0` fontes emendadas, `0` bytes em `FND-01`–`FND-11`, `0` em `TPL`, `0` em `CAP`, `0` em Carta, `0` em `ADR`/`RFC`/`FIT`/`PS`/`PT`/`MSG` historicos, `0` em baseline anterior, `0` no repositorio do candidato, `0` `Spec` criada, `0` execucoes.** Os **4** candidatos — `FND-09` **1.6.0**, `FND-11` **1.1.0**, Cartas `DEP-PRD` e `DEP-EXE` **1.2.0** — vivem **fora do acervo**, com `H-A`, `H-N` e `H-P` publicados. |
| 2.19.0 | 2026-08-02 | DEP-GOV | **Emenda pela PRIMEIRA `Spec` DO ACERVO — Missao 1.13.5.** §4 ganha um **oitavo bloco, §4.8 Executavel**, com [`SPC-001`](../products/nxtrack/specs/SPC-001-governanca-de-dado-pessoal-do-nxtrack.md) e o **contador oficial da sequencia `SPC`** que `SF-32` manda viver aqui — **`0` registros novos criados**. §5 leva `Spec` de *sem instancia* a **com instancia**: **19 de 33** tipos e **12 de 21** entidades, **sem criar tipo nem entidade** *(`FND-10 §4.4` e `FND-09 E-19` desde a fundacao)*. §2 registra `GO-TO-SPECS` **EXERCIDO**, saindo de *exercivel*. §4.2 vai a **59** com `ADR-0031` e `RFC-0026`; §4.5 a **33** com `FIT-2026-024`; §4.7 a **48** com `PT-2026-017`. **A classe foi ELEVADA de `C1` para `C2` por colisao MEDIDA**, nunca por cautela: a coluna `C1 · T2` de `SF-10` poe *Proposta* e *Aprovacao* no mesmo Departamento para o tipo `SPC`, e `FND-04 §3.1` declara **nula** a aprovacao com acumulo de papel (`LV-03`, Linha Vermelha de **nivel 1**) — de modo que **`C2` e a menor classe em que uma `Spec` pode ser validamente aprovada**. §7 recebe os achados **115 a 118**: **`RD-91`** *(Alta — a colisao acima; dono **SOBERANO**, porque sanar exige emendar `FND-11`)*, **`RD-92`** *(Baixa — DEP-QAR custodiante da materia e revisor do tipo na mesma mudanca)*, **`RD-93`** *(Media — `TPL-spec` 1.1.0 declara **tres** campos de frontmatter que nem `FND-03 §4.1` nem `SF-06` preveem para `Spec`, o que **contradiz `SF-05`**)* e **`RD-94`** *(Media — *"exatamente uma `Capability`"* contra materia que atravessa tres; familia de `RD-74`)*. **`RD-95`** *(Media — os contadores de `ADR` e de `RFC` estavam **defasados em um**, descoberto por **exercicio** contra a copia datada; quarta ocorrencia da familia de `RD-32`)* vive nos indices proprios. §10 emite **`BL-2026-08-02-01`**, demove `BL-2026-08-01-03` a **§10.0.1 com os valores ORIGINAIS**, **renumera §10.0.1 a §10.0.16 para §10.0.2 a §10.0.17** *(desloca subsecao, nunca valor)* e cria **§10.21**; **`0` baselines editadas** alem do campo *Superada por* do par de sucessao (`BL-02`). **`RD-90` continua ABERTO e nao varrido**; **`RD-80` teve o gatilho disparado pela TERCEIRA vez e nao foi resolvido.** **`0` atos emitidos, `0` fontes emendadas, `0` bytes em `FND-01`–`FND-11`, `0` em `TPL`, `0` em `CAP`, `0` em Carta, `0` em `ADR`/`RFC`/`FIT`/`PS`/`PT`/`MSG` historicos, `0` em baseline anterior, `0` no repositorio do candidato, `0` bancos abertos, `0` execucoes.** |
| 2.18.0 | 2026-08-01 | DEP-GOV | **Emenda pelo FECHAMENTO DE `RD-33` — Missao 1.13.4.6, ministerial, e a primeira missao do acervo cujo objeto unico foi fechar um achado.** O achado **54** de §7 passa a **✅ FECHADO**, e com ele o acervo fica **sem pendencia bloqueante pela primeira vez desde 2026-07-29**. **O rito foi DETERMINADO antes de exercido, nunca presumido por analogia:** `0` regras de rito de fechamento existem no acervo — varredura declarada —, e o rito veio de **`PA-01`, `PA-03`, `PA-07` e `PA-13`** de [ADR-0020](../decisions/ADR-0020-regime-ministerial-de-promulgacao-e-ativacao.md), **`AU-06`**, **`FND-04 §4 [7]`** e **`RG-01`/`RG-03`/`RG-04`/`AC-09`** de `FND-10`, com **cinco precedentes medidos** mostrando que **o rito de fechar achado e o rito da materia que remove a causa**. **A reserva do item VII do nono ato e de `LA-3` foi lida LITERALMENTE — e TEMPORAL *(«apos a vigencia»)* e DE SEDE *(«missao propria»)*, jamais de classe de rito:** *ato*, *ratificacao*, *`C3`* e *`1.13.5`* tem **`0`** ocorrencias nela, e `MSG-2026-0009 §8` poe *"`RD-33` destravado"* **ANTES** de 1.13.5. **A leitura divergente de `PT-2026-015 §10` e do roadmap foi DECLARADA e nenhum dos dois foi editado.** **`READY-FOR-RATIFICATION` foi construida e descartada com prova**, hipotese por hipotese. **Prova por EXERCICIO**, o mesmo metodo que abriu o achado: `DoR` de `SF-23` reexercido, item **(9)** **PASSA**, item **(4)** em **5 de 5** `Capabilities` ativas — §2 registra `GO-TO-SPECS` como **LIBERADO e EXERCIVEL**, saindo de *"liberado e nao exercivel"*. **`0` bytes nas TRES fontes do vinculo `Spec` × `Produto`: ele nao foi removido, foi SATISFEITO.** **O fechamento e PARCIAL POR CONSTRUCAO:** a parte **(b)** — a categoria de `Spec` sobre materia nao-produto, que so `S2` cria e que segue **DEFERIDA** por decisao soberana — **migra para `RD-88`**, e fechar `RD-33` inteiro teria afirmado que `S2` ocorreu. §4.7 vai a **47** registros com `PT-2026-016`; a conferencia de blocos passa a `11+57+33+19+32+12+53` e a diferenca para o total **continua nomeada** (`RD-80`, **gatilho disparado pela segunda vez**). §10 emite **`BL-2026-08-01-03`**, demove `BL-2026-08-01-02` a **§10.0.1 com os valores ORIGINAIS**, **renumera §10.0.1 a §10.0.15 para §10.0.2 a §10.0.16** *(desloca subsecao, nunca valor)* e cria **§10.20**; **`0` baselines editadas** alem do campo *Superada por* do par de sucessao (`BL-02`). Achados novos: **`RD-88`** *(a `Spec` de materia nao-produto continua inexistente — migrado, nao descoberto; dono SOBERANO)*, **`RD-89`** *(duas entradas de §7 na mesma linha fisica, com a **111** nao renderizando como linha; ✅ **corrigido na projecao**, uma quebra de linha, `0` caracteres de conteudo)* e **`RD-90`** *(**26 de 31** ponteiros de sucessao de §10.0.x apontam para a subsecao errada, medido por ferramenta antes de qualquer edicao; **ABERTO e deliberadamente nao varrido**, por `BL-02` e pelo congelamento)*. **`RD-80` e `RD-83` a `RD-87` declarados, e NENHUM fechado.** **`0` atos emitidos, `0` `Spec`s criadas, `0` bytes em `products/`, `0` bytes em fundacional, `TPL`, `CAP`, Carta, `ADR`, `RFC`, `FIT`, `PS`, `PT` historico, `MSG` ou baseline anterior.** |
| 2.17.0 | 2026-08-01 | DEP-GOV | **Emenda pela APLICACAO do nono ato soberano — Missao 1.13.4.5, ministerial.** O ato [MSG-2026-0009](../memory/operacional/MSG-2026-0009-ato-soberano-admissao-do-nxtrack.md) passa de **emitido** a **CONSUMIDO**, na ordem de [`PS-2026-016 §6.2`](pacote-soberano-2026-08-01-nxtrack.md): **`ADR-0030` `ativo` · `ratificada`**, **`RFC-0025` `aprovado`** *(pela **variante** de `§2.1`, jamais pelo instrumento padrao)* e **`PRO-nxtrack` CRIADO** em `products/nxtrack/carta.md`, `H-A` do **aplicado** `fca656a9…39e2` — **distinto do `H-A` do candidato**, `DF-1`. **Nasce `products/` como raiz do acervo**, e com ela **§4.3.2**: a entidade **`PRO`** e o tipo **`Carta de Produto`** estreiam, levando §2 a **11 de 21** entidades e **18 de 33** tipos, e §5 a `Constitutiva 7 | 3 | 4`. **Baseline `BL-2026-08-01-02`** em §10.0, com §10.19 nova e **§10.0.x renumerada** *(desloca subsecao, nunca valor)*. **`H-P` 2/2, `H-N` invariante 2/2, `IR-09` 3/3, `atualizado_em` nao tocado.** **`CA-2` INFORMATIVO cumprido MEDINDO:** a baseline publicada **nao reproduzia**, porque o instrumento **recusava medir** *(`RD-81`)* — e a recusa foi exercida no acervo **e** na copia datada. **Fila de retidos por falta de aplicacao: `0`.** **`RD-33` NAO fecha**, por reserva do proprio ato *(item VII, `LA-3`)*, embora a condicao de fato tenha caido. **`RD-81` ✅ FECHADO pelo dono** — o SOBERANO decidiu `CLAUDE.md` em `NAO_ACERVO` no despacho de abertura, e a decisao **passa de despacho a artefato aqui**. **`RD-80` segue ABERTO com o gatilho DISPARADO**, e a ausencia dele passa a ser **nomeada** em §2 *Classificados*, no cabecalho de §4 e na *Conferencia dos blocos*, que agora declara que a soma **nao** iguala o total medido. **§4 recontada por ferramenta bloco a bloco** — `11+57+33+19+32+12+52` —, e **28 enumerados** em *artefatos em vigor por ato*, contra rotulo anterior de **26** sobre **25**. Achados novos **`RD-83`** *(ancora `HEAD` de `CA-5` mede a arvore do terceiro e ja nao reproduz; o `tree` da subarvore reproduz)*, **`RD-84`** *(dois agregados de §2 divergem do que enumeram)*, **`RD-85`** *(`products/` sem indice de diretorio)* **`RD-86`** *(o candidato de Carta exigiu 5 ajustes onde o ato ordenou 2)* e **`RD-87`** *(tres indices emendados sem `versao` nova)* — **todos com dono e gatilho, nenhum gera missao**. **`0` bytes** em fundacional, `TPL`, `CAP`, Carta de Departamento, `MSG`, `FIT`, `PS`, `PT` historico ou baseline anterior. |
| 2.16.0 | 2026-08-01 | DEP-GOV | Emenda pelo **NONO ATO SOBERANO, emitido e NAO consumido** — [MSG-2026-0009](../memory/operacional/MSG-2026-0009-ato-soberano-admissao-do-nxtrack.md), ancorado no `H-A` `e6fa26e8…44ae` do pacote [PS-2026-016](pacote-soberano-2026-08-01-nxtrack.md) **1.2.0**, itens **I a VII**, linhas **185–328**. **RATIFICA `ADR-0030`**, **APROVA `RFC-0025`** e **CRIA `PRO-nxtrack`**; **`CA-1` a `CA-6` em 6 de 6**, com **`Q2` gravada como artefato pela primeira vez**. §2 recebe a linha do **nono ato** e a de **`Q2` RESPONDIDA**, e reconcilia **Produtos**, **retidos** *(de `4` para `2`, com a distincao falta de ato × falta de aplicacao declarada)* e **`RD-33`**; §4.7 vai a **45** registros; §7 acrescenta **5** linhas — **`RD-78` e `RD-79` por PROJECAO** *(fonte em `PS-2026-016`, §7 estava sem entrada)* e **`RD-80`**, **`RD-81`** e **`RD-82`** novos. **`0` transicoes `O4`, `0` arquivos em `products/`, `0` baselines emitidas, `0` bytes em `PS-2026-016` e nos cinco objetos**, e os `H-P` **conferidos sem aplicar: 2 de 2**. **§10.0 NAO foi editada** — `BL-2026-08-01-01` segue vigente, e reescrever o registro dela para dizer *"nove `MSG`"* seria o proprio defeito de `RD-78`. |
| 2.15.0 | 2026-08-01 | DEP-GOV | Emenda pela **Missao 1.13.4.4 — portao `ADR-0007` sobre o nXtrack**: **213** artefatos *(**`+5`**)*, **`BL-2026-08-01-01`** em §10.0, evidencia em §10.18 e renumeracao de §10.0.x. **Segunda passagem pelo portao de origem externa, e a primeira sob a norma emendada:** `G0` = `IDENTIDADE`, `G3` = `RECOGNIZE` — **primeira aplicacao prospectiva da classe**. §2 registra `Q1` **RESPONDIDA** e o portao **exercido duas vezes**; §4.2 passa a **57**, §4.5 a **32** e §4.7 a **44** registros; §9 passa a **2** `legacy-candidate` nomeados; §7 acrescenta **7** achados *(`RD-71` a `RD-77`)*. **`0`** Produtos admitidos, **`0`** atos emitidos, **`0`** bytes do candidato no acervo *(medido por `0` colisoes de hash)*, **`0`** fundacionais e **`0`** historicos alterados. `RD-77` corrigido **na projecao**; os demais **abertos, sem missao**. |
| 2.14.0 | 2026-07-31 | DEP-GOV | Emenda pela **Missao 1.13.4.3 — aplicacao ministerial de `E1` e `E3`**: **208** artefatos *(**`+1`**)*, **`BL-2026-07-31-08`**. **O oitavo ato soberano foi CONSUMIDO:** `ADR-0029` passa a **`ativo` · `ratificada`** e `ADR-0027` a **`ativo`** *(aprovado por **DEP-EXE**; `ratificacao` `nao-exigida` e **nao criada**)*, com **`H-P` 2 de 2, `H-N` invariante 2 de 2, `IR-09` 2 de 2** e **`atualizado_em` nao tocado**. Nasce [atos-superados](atos-superados.md), o registro de `SA-6`, **com o contador em `0`** — §4.6 vai a **12** indices. **`RC-1` em vigor**: §2 e §9 passam a declarar que o `REWRITE` da 1.13.4 **le-se `RECOGNIZE`**, e os **cinco** artefatos daquela missao seguem com **`0` bytes** (`RC-2`), **sem hash algum mudar** (`RC-3`). §7 recebe **`RD-69`** *(retidos tres `ADR` atras — valor reconciliado, causa aberta)* e **`RD-70`** *(`versao` do `README` da raiz uma emissao atras — **ABERTO e nao corrigido**)*. **`E2` intacta, `Q1` e `RD-33` bloqueantes, `0` Produtos, `0` `Spec`s.** |
| 2.13.0 | 2026-07-31 | DEP-GOV | Emenda pelo **OITAVO ATO SOBERANO, registrado e NAO consumido**: **207** artefatos *(**`+1`**)*, **`BL-2026-07-31-07`**. Nasce [MSG-2026-0008](../memory/operacional/MSG-2026-0008-ato-soberano-emendas-e1-e-e3.md) — o ato do Fundador sobre a minuta [PS-2026-015](pacote-soberano-2026-07-31-emendas-de-instrumento.md) **1.2.0**, **ancorado no `H-A` `3d242ed8…ca62` do texto assinado**: `Q2` respondida com **EMENDAR `ADR-0007` AGORA**, DEP-EXE autorizado a aprovar `ADR-0027` em `C2`, **`ADR-0029` RATIFICADO** e **`E2` ADIADA**. §2 recebe a linha de **ato emitido e nao consumido**; §4.7 vai a **42** registros; §9 a **207** `native`; §7 recebe **`RD-68`** *(contador de `MSG` uma emissao atras — **valor corrigido por `SF-32`, causa ABERTA e sem missao**)*. **`0` transicoes aplicadas, `0` normas alteradas, `0` bytes em `PS-2026-015` e nos nove objetos**, e os `H-P` dos dois objetos com `O4` **conferidos sem aplicar: 2 de 2**. |
| 2.12.0 | 2026-07-31 | DEP-GOV | Emenda pelo **despacho do Fundador na Missao 1.13.4.2 — correcao de `CA-2`, e somente dela, ANTES da assinatura**: **206** artefatos *(inalterado)*, **`BL-2026-07-31-06`**. §10 emite a nova baseline, demove `BL-2026-07-31-05` a §10.0.2 com os **valores ORIGINAIS**, renumera §10.0.x *(deslocamento de subsecao, **nunca** valor)* e acrescenta a **evidencia §10.15**. **Fonte alterada: nenhuma** — o unico artefato de conteudo tocado e [PS-2026-015](pacote-soberano-2026-07-31-emendas-de-instrumento.md) **1.1.0 → 1.2.0**, o proprio pacote submetido e nao consumido, onde `CA-2` passa de **bloqueante a INFORMATIVO** porque **o pacote mora dentro do acervo que a condicao mede** — **insatisfazivel por construcao, nao por desvio** —, e a ancora do ato passa a ser **por objeto consumido: `9` `sha256`**, `6` de `CA-1` mais `3` de `CA-5`, **nunca a arvore inteira**. **`0` atos emitidos, `0` normas alteradas, `0` bytes nos nove objetos das tres emendas** *(`9` de `9` `H-A` reproduzem)*, **`0` achados novos**, e **`RD-66` e `RD-67` seguem ABERTOS e sem missao designada**. |
| 2.11.0 | 2026-07-31 | DEP-GOV | Emenda pelo **despacho do Fundador na Missao 1.13.4.2 — registro do achado preexistente sobre a fronteira norma / nao-norma**: **206** artefatos *(inalterado)*, **`BL-2026-07-31-05`**. §7 recebe **`RD-66`** — o [`README` da raiz](../README.md) **nao declara QUAIS sao as arvores normativas**, e o unico conjunto declarado em norma *(a **classe Normativa** de `FND-10 §4.1`, somente `FND`)* **nao e o que o acervo mede** *(a **camada normativa** das tres arvores: `FND` + `TPL` + `CAP` + Cartas)* — e **`RD-67`** — **o §2 e o `versao` deste catalogo ficaram para tras** enquanto §4, §10.0 e as projecoes seguiram a fonte. **Os dois ficam ABERTOS: esta emissao registra e aponta para a missao de catalogo, e nao corrige nenhum.** **A terceira oracao do enunciado de `RD-66` nao sobreviveu a conferencia e esta corrigida no proprio registro:** `FND-10 §4.1` **fixa o Local** dos quatro tipos da classe Normativa em `foundation/`, e `FND-03 §7` enumera a arvore canonica. **`versao` do frontmatter corrigido de `2.8.0` para `2.11.0`** — divergencia **herdada**, registrada em `RD-67` e **declarada, nunca silenciosa**. **`0` atos emitidos · `0` fontes normativas alteradas · `0` bytes em `PS-2026-015` e nos nove objetos das tres emendas.** |
| 2.10.0 | 2026-07-31 | DEP-GOV | Emenda pelo **despacho do Fundador na Missao 1.13.4.2 — minuta de ato RECORTADA**: **206** artefatos *(inalterado)*, **`BL-2026-07-31-04`**. [PS-2026-015](pacote-soberano-2026-07-31-emendas-de-instrumento.md) passa a **1.1.0** e recebe **§6.1**, a variante **submetida**, restrita a **`E1`** e **`E3`** — **6** objetos enumerados por ID, versao, caminho, linhas, `H-A` e `H-N`, com **`H-P` somente nos DOIS que sofrem `O4`**. **`E2` fica FORA, ADIADA e NAO rejeitada**, com o motivo escrito: a decisao de retroatividade sobre **131 de 138** exige rito proprio. A independencia de `E1` e `E3` esta **declarada e medida em `0` por quatro vias nominalmente citadas**. Acrescenta ordem de aplicacao, **rollback por objeto**, ponto de partida por `H-A`, **condicoes anteriores `CA-1` a `CA-5` e posteriores `CP-1` a `CP-7`** com `IR-09`, e **nove limites** — entre eles que o ato **NAO reclassifica o `REWRITE` da 1.13.4**, reservado a **missao ministerial posterior**. §10 emite **`BL-2026-07-31-04`**, move `BL-2026-07-31-03` a **§10.0.2** com os valores ORIGINAIS, renumera as demais e cria **§10.13**, sem tocar §10.1 a §10.12 (`BL-02`). **1 artefato alterado — o proprio pacote da missao — · `0` criados · `0` removidos · `0` fontes normativas · `0` bytes nos 6 objetos do ato e nos 3 de `E2` · `0` atos emitidos.** |
| 2.9.0 | 2026-07-31 | DEP-GOV | Emenda pela **Missao 1.13.4.2 — as tres emendas de instrumento**: **206** artefatos, **`BL-2026-07-31-03`**. §4.2 recebe **`ADR-0027`**, **`ADR-0028`**, **`ADR-0029`**, **`RFC-0022`**, **`RFC-0023`** e **`RFC-0024`** *(49 → 55)*; §4.5 recebe **`FIT-2026-020`** a **`FIT-2026-022`** *(28 → 31)*; §4.7 recebe **`PS-2026-015`** e **`PT-2026-013`** *(39 → 41 registros)*. **Conferencia recalculada: 11 + 55 + 32 + 19 + 31 + 11 + 47 = 206.** **As tres classes foram DETERMINADAS percorrendo as cinco hipoteses de `C3`**, nunca presumidas: `E1` **`C2`/`Tipo 2`** *(a hipotese "a propria Fundacao" descartada **por medicao** — `0` ocorrencias das quatro classificacoes em `FND` algum)*, `E2` e `E3` **`C3`/`Tipo 1`**. **A dependencia entre as tres foi medida em `0`** por quatro criterios, e por isso **NAO ha conjunto atomico**. §7 recebe o achado **89**: **`RD-65`** *(Media — **a classe do rito nao se herda da fonte**; a minuta declarava superar `ADR-0005`, que **nao contem criterio de afericao**, e herda-la teria produzido `C2` onde a norma exige `C3`; ✅ **CORRIGIDO**)*. §10 emite **`BL-2026-07-31-03`**, move `BL-2026-07-31-02` a **§10.0.2** com os **valores ORIGINAIS**, renumera **§10.0.2 a §10.0.8** para **§10.0.3 a §10.0.9** — deslocando subsecao, **nunca valor** — e cria **§10.12**, sem tocar §10.1 a §10.11 (`BL-02`). **`0` fontes normativas alteradas · `0` bytes em `ADR-0005`, `ADR-0007`, `ADR-0012` e `FND-10` · `0` artefatos `M1` editados · `0` baselines historicas editadas · `0` bytes no pacote da 1.13.4 · `0` atos emitidos · `0` candidatos julgados. Decisao da missao: `READY-FOR-RATIFICATION`.** |
| 2.8.0 | 2026-07-31 | DEP-GOV | Emenda pela **Missao 1.13.4.1 — manutencao dos instrumentos**: **195** artefatos, **57.769** linhas, **`BL-2026-07-31-02`**. **`RD-53` FECHADO por instrumento novo** — o defeito era do **comando**, nao da baseline, e `BL-2026-07-30-01` **reproduz nos 64 digitos** sobre a copia em que o comando publicado dava **198**. **`RD-56`** *(`TPL-carta-produto` **1.1.0**)*, **`RD-57`** e **`RD-58`** ✅ **FECHADOS** — `RD-58` por **supressao da duplicata**, nao por correcao de valor. **`RD-49`** corrigido em **tres candidatos medidos e nao aplicados**. **Cinco achados novos: `RD-60` a `RD-64`.** §2 passa a publicar a **autoverificacao pelos dois criterios** *(`0` e `130`)*; §10.11 registra a nova baseline e §10.11.1, o manifesto externo que **reproduz**. **`0` bytes em fundacionais, `ADR`, `MSG`, `FIT`, `PT` historicos, baselines e no pacote da 1.13.4.** |
| 2.7.0 | 2026-07-31 | DEP-GOV | Emenda pela **Missao 1.13.4 — S1, a admissao canonica do medAlly**: **194** artefatos, **56.854** linhas, **`BL-2026-07-31-01`**. **§2 registra o portao de origem externa EXERCIDO PELA PRIMEIRA VEZ** — `G1`–`G4` comprovados, `G5` preparado, **`G3` = `REWRITE`**, **`0` bytes admitidos**, **`0` bytes escritos no candidato** — e a **fila de retidos reaberta por construcao**: **1** no acervo *(`ADR-0026`)* e **1** candidato fora dele *(a Carta `PRO-medally`)*. **`0` Produtos em vigor · `products/` inexistente · `0` `Spec`s · `RD-33` BLOQUEANTE.** §4.2 recebe **`ADR-0026`** e **`RFC-0021`** *(47 → 49)*; §4.5 recebe **`FIT-2026-019`** *(27 → 28)*; §4.7 recebe **`PS-2026-014`** e **`PT-2026-011`** *(36 → 38 registros)*. **Conferencia recalculada: 11 + 49 + 32 + 19 + 28 + 11 + 44 = 194.** §9 registra o **primeiro `legacy-candidate` da historia do acervo**, nomeado e **nao admitido**. §7 recebe os achados **77 a 83**: **`RD-53`** *(Media — **o comando publicado da baseline nao reproduzia `BL-2026-07-30-01` sobre a copia datada**, porque a raiz continha `_candidatos/` com 13 `.md` que a exclusao nao cobre: **198**, nao **185**; e §10.9 declara que as tres variantes de `FND-01` *"permanecem em `_candidatos/`"*, **diretorio que nao existe na raiz** — as tres **existem**, medidas em **490 · 488 · 492**, nos backups. **Segunda ocorrencia da familia de `RD-17`**; **mitigado pela escolha de caminho** desta missao)*, **`RD-54`** *(Media — **o portao nao distingue admitir identidade de admitir conteudo**; contornado por `AM-01`, **nao fechado**)*, **`RD-55`** *(Media — **nenhuma das quatro classificacoes de `G3` descreve *admitir existencia sem admitir nada***; `REWRITE` escolhida **por eliminacao**, com o efeito correto e o nome impreciso, **declarado**)*, **`RD-56`** *(Media — **`TPL-carta-produto` nao preve `capabilities` nem os cinco campos de `FND-10 §2.2`**, contra `FND-09` E-17 e `FND-04 §6`; **segunda ocorrencia da familia de `RD-23`**; **nao corrigido**)* e **`RD-57`** *(Media — **este catalogo divergia de si proprio em CINCO lugares**, todos anteriores: `resumo` **169**, §Escopo **164**, §2 **185 · 54.190**, a conferencia de §4 somando **185** com um `10` que a **propria §4.1** contradiz, e §9 **169** — contra **189 · 55.280** em §10.0 do mesmo documento. ✅ **Corrigido na projecao**, valor a valor, **`0` fontes alteradas**; **sexta ocorrencia** de o catalogo divergir de si proprio e **decima quarta** da familia de `MEM-APR-0002`)* e **`RD-58`** *(Baixa — **`governance/README` mantem uma DUPLICATA do contador `FIT`**, tres emissoes atras da fonte que a linha seguinte reconhece; **o defeito e a duplicata, nao a divergencia** (`PJ-01`); ✅ **valor corrigido na projecao**, **supressao da linha declarada e nao executada**)* e **`RD-59`** *(Media — **`G1` exige data, e data nao basta para repositorio vivo**: o candidato mudou **entre a abertura e o fechamento da mesma missao**, em **16** caminhos de material de demonstracao, **`0`** deles lidos ou executados; as **5** fontes consumidas **inalteradas**; **terceira lacuna medida do portao**)*. §10 emite **`BL-2026-07-31-01`**, move `BL-2026-07-30-02` a **§10.0.2** e renumera **§10.0.2 a §10.0.6** para **§10.0.3 a §10.0.7**, **todas com os valores ORIGINAIS**, cria **§10.10** e **nao toca §10.1 a §10.9** (`BL-02`) — apenas o campo *Superada por* de `BL-2026-07-30-02` foi preenchido. **`0` fontes normativas alteradas · `0` artefatos `M2` emendados · `0` bytes em `ADR-0007`, `ADR-0020` e `ADR-0021` · `0` artefatos `M1` editados · `0` baselines historicas editadas · `0` bytes admitidos de origem externa · `0` bytes escritos no candidato PELA MISSAO · `0` Produtos em vigor. Decisao da missao: `READY-FOR-RATIFICATION`, com `Q1` bloqueante.** |
| 2.6.0 | 2026-07-30 | DEP-GOV | Emenda pela **Missao 1.13.2 — convergencia pre-ratificacao**: **185** artefatos, **54.190** linhas, **`BL-2026-07-30-01`**. **§2 registra a fila crescida por construcao** — **4** artefatos retidos no acervo *(`ADR-0022` a `ADR-0025`)* e **13 candidatos fora dele** — e passa a declarar `RD-27` como **tratado por rito completo**, com `0` nao conformidades **no candidato** e **2 ainda vigentes**, porque **so o ato fecha**. §4.2 recebe **`ADR-0024`**, **`ADR-0025`** e **`RFC-0020`** *(44 → 47)*; §4.5 recebe **`FIT-2026-017`** *(25 → 26)*; §4.7 recebe **`PS-2026-011`**, **`PS-2026-012`**, **`PS-2026-013`** e **`PT-2026-009`** *(30 → 34 registros)*. **Conferencia recalculada: 10 + 47 + 32 + 19 + 26 + 11 + 40 = 185.** §7 recebe os achados **68 a 71**: **`RD-45`** *(Media — a variante `V2` de `FND-01` **atribui a `ADR-0022` o backfill de `AC-08` que o escopo literal de `ADR-0022` exclui** em `J14` e §7.3; promulga-la poria no **nivel 1** da hierarquia uma afirmacao que um `ADR` **`M1`** contradiz e **nao pode ser corrigido para concordar**; ✅ **corrigido no candidato**, e **encontrado por construir o cumulativo e comparar**)*, **`RD-46`** *(Baixa — **`FND-10 §8.5` tinha CINCO valores defasados onde `RD-27` contara TRES**: o denominador do acervo, o percentual derivado e a nota de `CE-05`, **dois deles na mesma frase que os tres contados**; ✅ **corrigido no candidato**, e **a causa foi corrigida junto** — a secao passa a **vincular cada valor a baseline em que vale**, porque numero sem data **nao envelhece virando historico, envelhece virando afirmacao falsa**)*, **`RD-47`** *(Media — **o regime de estado na promulgacao de versao nova e costume, nao regra escrita**: Carta volta a `em-revisao`/`pendente` e recebe `O4`, fundacional permanece `ativo`/`ratificada` e nao recebe, e **`FND-10 §5.2` nao os distingue**; **NAO corrigido**, seria `C2` proprio, e a consequencia e que **o `H-P` de todo objeto futuro depende de qual precedente se aplica**)* e **`RD-48`** *(Baixa — **o custo de reversao de `ADR-0020` envelheceu na parte que ninguem contou**: os **6 indices `M3`** que ele mediu **continuam 6, e a medicao acertou**; as referencias em artefato **`M1`, nao corrigiveis**, foram de **4** a **10** a **12** em duas missoes. **`ADR-0020` NAO e reclassificado nem tocado** — `C2 · Tipo 2` continua correto porque **`0` artefatos normativos migram**; **o que deixa de ser verdade e que a reversao seja *limpa***)*. §10 emite **`BL-2026-07-30-01`**, move `BL-10` a **§10.0.3**, `BL-09` a **§10.0.4**, `BL-08` a **§10.0.5** e `BL-07` a **§10.0.6**, **todas com os valores ORIGINAIS**, cria **§10.8** e **nao toca §10.1 a §10.7** (`BL-02`) — apenas o campo *Superada por* de `BL-10` foi preenchido, e a renumeracao **nao altera valor algum**. §11 recebe **duas** linhas: a medicao de **convergir pacotes pendentes num ato unico** e — **pela primeira vez no acervo** — **o custo de *decidir* em vez do de *escrever***: ler o ato consolidado custa **343** linhas contra **1.581** dos quatro pacotes somados. **`0` fontes normativas alteradas, medido por `cmp` em 73 arquivos · `0` artefatos `M2` emendados · `0` bytes em `ADR-0020` e `ADR-0021`, inclusive frontmatter · `0` artefatos `M1` editados · `0` baselines historicas editadas · `0` candidatos historicos tocados · `0` linhas de evidencia externa lidas · `0` sobreposicao de diff em 14 objetos. Decisao da missao: `READY-FOR-RATIFICATION`.** |
| 2.5.0 | 2026-07-29 | DEP-GOV | Emenda pela **Missao 1.13.1 — canonizacao de Specifications e correcao de `RD-31`**: **177** artefatos, **51.698** linhas, **`BL-2026-07-29-10`**. **§2 registra a fila reaberta por construcao** — **1** artefato retido no acervo *(`ADR-0022`, `C3 · Tipo 1`)* e **6 candidatos fora dele** — e acrescenta tres linhas de estado: a **sede canonica submetida**, a **correcao de `RD-31` em candidato** e o **`PILOTO-DEFERIDO`**. **O cabecalho de §4 declarava `159 de 159` contra `169` na soma das proprias subsecoes** — achado **`RD-42`**, **corrigido**, e a **causa** tambem: o cabecalho passa a ser **derivado da conferencia dos blocos**. §4.2 recebe **`ADR-0022`**, **`ADR-0023`**, **`RFC-0018`** e **`RFC-0019`** *(40 → 44)*; §4.5 recebe **`FIT-2026-016`** *(24 → 25)*; §4.7 recebe **`PS-2026-009`**, **`PS-2026-010`** e **`PT-2026-008`** *(27 → 30 registros)*. **Conferencia recalculada: 10 + 44 + 32 + 19 + 25 + 11 + 36 = 177.** §7 recebe os achados **60 a 67**: **`RD-37`** *(Media — **3 Cartas ratificadas** afirmam que `DEP-PRD` libera `QG-1`, nunca enumeradas; o defeito de `RD-31` estava em **4** Cartas e **11** afirmacoes, nao 2 e 8; **NAO corrigido, por escopo determinado**, com custo publicado de **1 linha por Carta**)*, **`RD-38`** *(Baixa — o verbete `Fundacao` de `FND-01 §11` conta **nove** fundacionais e existem **dez**; ✅ corrigido no candidato)*, **`RD-39`** *(Baixa — `RC-02`, **oitava ocorrencia**: a autoria de `FND` volta a DEP-GOV **por determinacao da matriz**)*, **`RD-40`** *(Baixa — `ADR-0021` **nao declara a propria superacao parcial**; a sucessao vive em 4 lugares, e o residuo esta declarado)*, **`RD-41`** *(Baixa — a Carta de `DEP-PRD` aloja a `Spec` em `projects/`; ✅ corrigido **para** o local canonico)*, **`RD-42`** *(Baixa — o agregado de §4; ✅ corrigido)*, **`RD-43`** *(Media — **`IR-03` exclui `substituido_por` de `H-N` e nao exclui `superado_por`**: para `ADR`, o unico campo de sucessao do frontmatter **altera `H-N`**, e a autorizacao de `FND-10 §6.2` fica **sem objeto praticavel**; **encontrado por medir, nao por ler**)* e **`RD-44`** *(Media — `ADR-0021` **nunca recebeu linha** na tabela de `decisions/README`; ✅ corrigido, **terceira ocorrencia da familia `RD-32`** e a primeira **em campo diferente do contador**)*. §10 emite **`BL-2026-07-29-10`**, move `BL-09` a **§10.0.3**, `BL-08` a **§10.0.4** e `BL-07` a **§10.0.5**, **todas com os valores ORIGINAIS**, cria **§10.7** e **nao toca §10.1 a §10.6** (`BL-02`) — apenas o campo *Superada por* de `BL-09` foi preenchido. §11 recebe **duas linhas**: a medicao itemizada de **mover um dominio de sede** e a **projecao rotulada** do consumo da norma apos o ato *(**671** linhas contra **845**, **−20,6%**)*. **`0` fontes normativas alteradas · `0` artefatos `M2` emendados — a primeira vez em duas missoes · `0` bytes em `ADR-0021`, inclusive frontmatter · `0` artefatos `M1` editados · `0` baselines historicas editadas · `0` linhas de evidencia externa lidas. Decisao da missao: `READY-FOR-RATIFICATION`.** |
| 2.4.0 | 2026-07-29 | DEP-GOV | Emenda pela **Missao 1.13 — Framework de Specifications**: **169** artefatos, **48.764** linhas, **`BL-2026-07-29-09`**. **§2.1 foi RECOMPUTADA sobre a coorte inteira, nao incrementada** — e a recomputacao capturou a migracao de **`TPL-spec` de *por padrao* para *declarado*** que a soma teria perdido: declarados **103 → 109**, ausencias **61 → 60**, cobertura **100%**, e a particao **reproduz o total do acervo** pela **segunda emissao consecutiva**. §2 registra **`RD-23` FECHADA**, o **Framework INSTITUIDO** e a **unica pendencia bloqueante do acervo** — `RD-33`. §4.2 recebe **`ADR-0021`** e **`RFC-0017`** *(38 → 40)*; **§4.4 registra o unico artefato `M2` emendado da missao** — `TPL-spec` **132 → 272** linhas, subtotal **2.958 → 3.098**, com hash antes e depois e `LF` preservado — e o achado **`RD-34`**; §4.5 recebe **`FIT-2026-015`** *(23 → 24)*; §4.6 corrige as linhas de **5 indices** e registra as correcoes de contador; §4.7 recebe **`MEM-APR-0006`** e **`PT-2026-007`** *(25 → 27 registros)*. **A conferencia de §4 nao produziu nenhuma divergencia de contagem — a primeira vez**, contra **4** na emissao anterior, e a causa nao foi mais cuidado, foi **medir depois de todas as edicoes**. §7 recebe os achados **52 a 59**: **`RD-31`** *(Alta — a Carta de `DEP-PRD` tem **8** afirmacoes que `ADR-0018` e `ADR-0019` tornaram falsas, **4 nunca enumeradas**, e **`DEP-EXE` nao declara `QG-1` em nenhuma linha**: o portao da `Spec` **nao tem titular declarado em Carta alguma**)*, **`RD-32`** *(Media — **4** contadores oficiais defasados em **8** valores, com risco de **colisao de identificador**; ✅ corrigidos, e a causa **codificada em `SF-32`**; **segunda ocorrencia**, e a correcao anterior atingiu o valor e nao o gatilho)*, **`RD-33`** *(Alta e **BLOQUEANTE** — a `Spec` esta vinculada a `Produto` em **tres** fontes vigentes e **`0` produtos existem**; as duas Specs piloto **nao foram criadas**, e as duas saidas faceis foram **recusadas com norma citada**)*, **`RD-34`** *(Baixa — **19 de 19** `TPL` declaram `aprovador: SOBERANO`; **nao corrigido**, porque corrigir um criaria divergencia entre iguais)*, **`RD-35`** *(Media — **3** agregados de indice divergentes; ✅ corrigidos, e a enumeracao de `OPR` **substituida por remissao a fonte**, correcao de causa e nao de valor)*, o registro do **fechamento de `RD-23` com 5 defeitos onde o achado citava 2**, o registro de que **as 32 regras `SF-*` sao determinadas e nao observadas**, e **`RD-36`** *(Media — **o razao de ressalvas nao fecha**: `31` linhas e `28` ressalvas distintas em abertas, `18` em fechadas e `55` linhas nos proprios `FIT`, **nenhum conjunto reconciliando com os outros**; a **cascata devida foi executada** e a **reconciliacao integral NAO**, com o motivo escrito)*. §9 corrige a proveniencia para **169** e registra que a **evidencia externa `A4` foi lida e NAO admitida** — **236 de 33.676 linhas, `0,70%`**, **0 formatos importados**, **0 candidatos nomeados**. §10 emite **`BL-2026-07-29-09`**, move `BL-08` a **§10.0.3** e `BL-07` a **§10.0.4**, ambas **com os valores ORIGINAIS**, e cria **§10.6**, **sem tocar §10.2, §10.4 nem §10.5** (`BL-02`) — apenas o campo *Superada por* de `BL-08` foi preenchido, que e o par de sucessao. §11 recebe **duas linhas**: a medicao itemizada de **instituir um dominio** *(**3.578 · 7,72%**, declarada como **subida** contra a Missao 1.12.1, com a razao medida)* e a **projecao rotulada** de consumir a norma da `Spec`. **`0` fontes normativas alteradas · `0` bytes em `FND-01`, `FND-02` e `FND-10` · `0` baselines historicas editadas · `1` artefato `M2` emendado pelo rito. Decisao da missao: `ADJUST`.** |
| 2.3.0 | 2026-07-29 | DEP-GOV | Emenda pelo **fechamento operacional da Missao 1.12.1**: **164** artefatos, **46.353** linhas, **`BL-2026-07-29-08`**. **§2.1 deixa de ser lacuna declarada e passa a ser tabela reconciliada**, pelo metodo que **`FND-10 §2.3` sempre prescreveu — frontmatter quando declarado, padrao de §10.3 quando ausente —, e a prova de que o metodo fecha e reproduzir o total do acervo: 164 artefatos e 46.353 linhas.** Cobertura **100%**, **0 nao classificados**, **0 preenchimentos por inferencia**. **Achado `RD-26` RECONCILIADO** e **`RD-22` FECHADO por refutacao de premissa** — os titulares de promulgacao e ativacao estavam declarados em `FND-04 §4 [7]`, `FND-07 §5 [10]`, `FND-09 §7.5` e `AU-06`, e a varredura original mediu o **termo** em vez da **funcao**. §2 recebe **quatro medidas novas** — cobertura de perfil, nao conformidades de contrato conhecidas, estado do portao `GO-TO-SPECS` e pre-correcao obrigatoria. §2.2 e **remedida por ordenacao** e passa a incluir **este catalogo** e `REV-interclasses`, que **nao constavam dos cinco maiores**. §3 passa `FND-01` a **485** e o total integral a **1.116**. §4.2 recebe **`ADR-0020`** e **`RFC-0016`** *(36 → 38)*; §4.4 corrige o subtotal de **2.952** para **2.958** — soma dos proprios valores da tabela; §4.5 recebe **`FIT-2026-014`** *(22 → 23)*; §4.6 e §4.7 corrigem as linhas de **4 indices** e recebem **`MEM-APR-0005`** e **`PT-2026-006`** *(23 → 25 registros)*; §6 recebe **cinco** linhas de rastreabilidade. §7 recebe os achados **48 a 51**: **`RD-27`** *(Media — `FND-01`, `FND-02` e `FND-10 §8.5` nao conformes a `AC-08`; **NAO corrigidos**, porque o backfill altera **`H-N`** e `IR-05` exige **ato novo**)*, **`RD-28`** *(Media — **10** valores divergentes, **9 anteriores**; ✅ corrigidos na projecao, **zero fontes alteradas**; **dois deles sao a fonte derivada nao conferindo contra si mesma**, e foram achados exercendo pela **primeira vez** a mitigacao de `RG-2`, escrita desde a Missao 1.9)*, **`RD-29`** *(Baixa — ✅ corrigido como `C0`)* e **`RD-30`** *(Baixa — metrica de links sem metodo declarado; ✅ atendido em §10.5)*. §9 corrige a proveniencia de **137** para **164**. §10 emite **`BL-2026-07-29-08`**, move `BL-07` a **§10.0.3 com os valores ORIGINAIS** e cria **§10.5** com evidencia nova, **sem tocar §10.2 nem §10.4** (`BL-02`). **Os dez objetos do sexto ato foram rehasheados: 10 de 10 reproduzem nos 64 digitos. Zero fontes normativas alteradas, medido por `cmp`. Portao `GO-TO-SPECS` LIBERADO — 8 de 8 condicoes de §X.** |
| 2.2.0 | 2026-07-29 | DEP-GOV | Emenda pela **aplicacao do sexto ato soberano**: **159** artefatos. **Primeira emenda deste catalogo em que ha promulgacao de documento fundacional.** §2 registra **15 artefatos em vigor por ato**, **a fila de retidos em 0** — *(zerada pela primeira vez em quatro atos)* — e **`BL-2026-07-29-07`** como baseline vigente. §4.1 passa `FND-01` a **1.5.0 · 485**, `FND-02` a **1.3.0 · 518**, `FND-09` a **1.5.0 · 1.263** e `FND-10` a **1.4.0 · 778**; §4.2 marca `ADR-0016` a `ADR-0019` como **RATIFICADOS**; §4.3 e **reconciliada por inteiro** — `DEP-KMS` **1.1.0 · 464**, `DEP-ENG` **1.1.0 · 402**, as nove Cartas **em vigor** e o subtotal em **3.925**; §4.7 recebe **MSG-2026-0006** e **PT-2026-005**. §6 registra os quatro `ADR` **ratificados com `H-P` medido reproduzindo o projetado**. §7 recebe os achados **43 a 46**: **`RD-22`** *(Alta — `promulgacao` e `ativacao` **sem titular declarado**, o que **bloqueia a condicao 6 de §X** e por isso **`GO-TO-SPECS` NAO foi autorizado**)*, **`RD-23`** *(Alta — `TPL-spec` contradiz `ADR-0019` desde que ele vigora; **nao corrigido**, por vedacao expressa)*, **`RD-24`** *(Media — §10.2 declara a contagem de `BL-05` ao lado da impressao digital de `BL-06`; **nao corrigida**, porque `BL-02` proibe editar baseline)* e **`RD-25`** *(Media — §4.3 divergia da fonte em **13** valores, **11 anteriores a esta aplicacao**; ✅ corrigido **na projecao**, zero fontes alteradas)*. §10 emite **`BL-2026-07-29-07`**, **acrescenta `BL-05` e `BL-06` a §10.1 com os valores originais** — nenhuma das duas havia sido movida quando foi superada — e cria **§10.4** com a evidencia nova, **sem tocar §10.2**. **Dez objetos aplicados; exatamente 10 arquivos alterados; 0 fontes corrigidas fora do diff autorizado.** |
| 2.1.0 | 2026-07-29 | DEP-GOV | Emenda pela **continuacao da Missao 1.12**: **157** artefatos. **Nenhum ato foi consumido**, e por isso **zero aplicacoes, zero promulgacoes, zero transicoes O4, zero fundacionais, zero Cartas e zero pacotes alterados**. §4.5 recebe **FIT-2026-013** e §4.7 recebe **PT-2026-004**; §6 registra que os **12 objetos** das cinco cadeias foram **verificados sem falha** e que os **candidatos cumulativos** de FND-09 **1.5.0** e FND-10 **1.4.0** existem **fora do acervo**, com caminho declarado; **§7 corrige a caracterizacao do achado 40 (`RD-19`)** — os candidatos **existem**, e o defeito real e o **caminho nao declarado** — e recebe o achado **42** (`RD-21`); §10 emite **`BL-2026-07-29-06`** e preserva `BL-01` a `BL-2026-07-29-05` **sem edita-las**. |
| 2.0.0 | 2026-07-29 | DEP-GOV | Emenda pela **Missao 1.12**: **155** artefatos. §2 registra que a **pre-condicao de aplicacao foi verificada e NAO satisfeita** — **nenhum ato consumido**, **zero promulgacoes**, **zero fundacionais e zero Cartas alteradas** — e que os **artefatos retidos por falta de ato dobraram**, de **2** para **4**, porque a missao **produziu instrumento para os dois bloqueios que nao tinham**; §4.2 recebe **ADR-0018**, **ADR-0019**, **RFC-0014** e **RFC-0015**, §4.5 recebe **FIT-2026-012** e §4.7 recebe **PS-2026-007**, **PS-2026-008** e **PT-2026-003**; §6 registra os **dois ADR candidatos novos** e os **tres candidatos fundacionais** *(FND-01 1.5.0, FND-09 1.4.0, FND-10 1.3.0)*, que vivem **fora do acervo** e cujos dois ultimos **concorrem** com os da Missao 1.11 — achado **RD-19**; §7 recebe os achados **38 a 40** *(**RD-17**, **RD-18**, **RD-19**)*; §10 emite **`BL-2026-07-29-05`** e preserva `BL-01` a `BL-2026-07-29-04` **sem edita-las**, e §10.2 **corrige a exclusao do comando de reproducao** — achado **RD-17**, a baseline anterior **nao reproduzia por omitir `_SAIDA-COMPANY-OS/`** — e acrescenta a **reimplementacao de `IR-02`/`IR-03` validada contra 6 hashes de controle antes do uso**. **Nenhuma fundacional foi emendada; nenhuma Carta foi alterada; nenhum artefato M1 foi editado.** |
| 1.9.0 | 2026-07-29 | DEP-GOV | Emenda pela **Missao 1.11**: **147** artefatos. §2 registra `DEP-QAR` em **1.2.0 aplicada** e o **quinto ato soberano**; **§4 reconciliado apos duas missoes de atraso** — o cabecalho declarava *"117 de 117"*, as tabelas somavam **131** para **137** em disco, e **seis** artefatos anteriores nunca haviam sido acrescentados *(achado **RD-16**, quarta ocorrencia de o catalogo divergir de si proprio)*; §6 registra `DEP-QAR` **APLICADA** com `IR-09` reproduzindo `H-A`, as duas Cartas **reemitidas** e os **dois ADR candidatos** retidos; §7 recebe os achados **31 a 37** *(RD-10 a RD-16, dois de severidade **Alta**)*; §10 emite **`BL-2026-07-29-04`** e preserva `BL-01` a `BL-2026-07-29-03` **sem edita-las**, e §10.2 acrescenta **credencial** e **terminadores de linha** as evidencias. **Nenhuma fundacional foi emendada**: os tres candidatos vivem **fora do acervo**. |
| 1.8.0 | 2026-07-29 | DEP-GOV | Emenda pela **aplicacao do ato soberano de 2026-07-29**: **137** artefatos. §6 registra as **cinco Cartas em `ativo` · `ratificada`**, **ADR-0014** em vigor, **FND-01 1.4.0**, **ADR-0015** e **MSG-2026-0004**, e declara que **a fila de artefatos retidos por falta de ato zerou** — primeira vez em quatro atos; §7 recebe os achados **29** *(RD-09)* e **30** *(RD-08)*; §10 emite **`BL-2026-07-29-03`** e preserva `BL-01` a `BL-2026-07-29-02` **sem edita-las**. **Nenhuma Carta teve linha de corpo alterada**: as cinco mudaram **dois campos de frontmatter** cada, com `H-P` conferido contra valor **projetado antes do ato**. |
| 1.7.0 | 2026-07-29 | DEP-GOV | Emenda pela **Missao 1.10**: **134** artefatos. §6 registra **PS-2026-003**, **PT-2026-001**, **FIT-2026-009** e as **tres emendas candidatas** — que **nao sao artefatos do acervo** e nao entram na contagem; §7 recebe os achados **24 a 27**; §9 e o `resumo` do frontmatter sao **corrigidos** *(achado **RD-06** — o catalogo divergia de si proprio em dois lugares)*; §10 emite **`BL-2026-07-29-01`** e preserva `BL-01` a `BL-06` **sem edita-las**, e §10.2 acrescenta **link** e **autoverificacao** as evidencias de integridade. **Nenhuma Carta foi alterada nesta missao.** |
| 1.6.0 | 2026-07-28 | DEP-GOV | Emenda por **ADR-0013** e pelo **rollout das Cartas**, Missao 1.9: **131** artefatos; §2 passa a **9 de 9 Cartas escritas** *(4 em vigor, 5 retidas)* e a **17 de 33** tipos com instancia — **`Reporte` instanciado pela primeira vez**, sem criar tipo; §4.2 recebe **ADR-0013**, **ADR-0014** *(candidato, sem vigencia)*, **RFC-0010** e **RFC-0011**; §4.3 passa a **32 Cartas** e §4.3.1 as **nove** de Departamento, com `DEP-QAR` em **1.1.0** e **387** linhas; §4.5 recebe **REV-ROLLOUT** e **FIT-2026-008**; §4.6 recebe **IDX-departamentos** e tem as contagens de linha **remedidas em oito indices** *(achado 22)*; §4.7 recebe **MSG-2026-0003** e **PS-2026-002**; §5 corrigida para **17 com instancia · 16 sem**; §6 registra os **seis** artefatos retidos; §7 recebe os achados **21 a 23**; §10 emite **`BL-2026-07-28-06`** e preserva `BL-01` a `BL-05` **sem edita-las**; §11 recebe o custo itemizado do rollout — **18,9%**, a **primeira descida comparavel** da serie. |
| 1.5.0 | 2026-07-28 | DEP-GOV | Emenda por **ADR-0012** e pela **Primeira Revisao Estrutural**, Missao 1.8: **117** artefatos; §2 corrige **entidades instanciadas de 11 para 10** (achado **RE-05** — `ORG` e `SOBERANO` estao fora de A2) e passa a **5 artefatos em vigor por ato soberano**; §4.2 recebe **ADR-0012** e **RFC-0009**; §4.3.1 passa as **quatro Cartas a `ativo`/`ratificada`**; §4.5 recebe **REV-ESTRUTURAL-I** e **FIT-2026-007**; §4.7 recebe **MSG-2026-0002** e passa `MEM-EST-0001` a `ativo`; **§5 integralmente corrigida — IC-8 fechado a partir da fonte**, com `Memoria <camada>` = **cinco** tipos, `Diretiva/Consulta/Alerta` = **tres** e `Norma Derivada` **fora da conta**, totalizando **33 sem emendar FND-10**, mais **RE-04** *(16 vs 17)* e a retirada de `Nota de Decisao` de com-instancia; §6 registra os cinco artefatos em vigor e **nenhum retido**; §7 recebe os achados **17 a 20**; §10 emite **`BL-2026-07-28-05`** e preserva `BL-01` a `BL-04` **sem edita-las**. |
| 1.4.0 | 2026-07-28 | DEP-GOV | Emenda por **ADR-0011**, Missao 1.7: **112** artefatos; §2 passa a **11 de 21** entidades e **16 de 33** tipos com instancia — `Diretiva` e `MSG` instanciados pela primeira vez, **sem criar nenhum dos dois**; §4.3.1 passa a **4 de 9** Cartas de Departamento, com **DEP-QAR** e **DEP-ENG** em **`ativo`/`ratificada`** e **DEP-EXE** e **DEP-KMS** em `em-revisao`; §4.7 passa a reunir `MEM` **e** `MSG`; §5 corrige `Memoria EST` para com-instancia e **registra sem ajustar** a divergencia aritmetica da linha Cognitiva (achado **IC-8**); §6 vincula as duas ratificacoes a **MSG-2026-0001** como fonte canonica; §7 recebe os achados **14, 15 e 16**; §10 emite **`BL-2026-07-28-04`** e preserva `BL-01`, `BL-02` e `BL-03` **sem edita-las**. |
| 1.3.0 | 2026-07-28 | DEP-GOV | Emenda por **ADR-0011**: **107** artefatos; §4.3.1 acrescenta as **duas Cartas de Departamento** — primeira instancia do tipo e da entidade `DEP`, ambas em `em-revisao`; §5 passa a **15 de 33** tipos com instancia; §10 emite **`BL-2026-07-28-03`** e preserva `BL-01` e `BL-02` **sem edita-las**; §11 recebe o custo medido de tres pacotes novos; §7 recebe os achados **11, 12 e 13**. |
| 1.2.0 | 2026-07-28 | DEP-GOV | Emenda por **ADR-0009** e **ADR-0010**: 100 artefatos; §4.7 passa a reunir indices **e registros** de memoria, corrigindo a classificacao dos tres `MEM-APR` (achado D7); §10 emite **`BL-2026-07-28-02`** e preserva `BL-01` como superada, **sem edita-la**; §11 recebe os pacotes de contexto do Soberano com custo medido. |
