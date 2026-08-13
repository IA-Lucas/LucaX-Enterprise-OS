---
id: IDX-fitness
titulo: Registro de Aptidao Arquitetural (FIT)
tipo: relatorio
versao: 1.16.0
status: ativo
camada_memoria: estrategica
autor: DEP-QAR
proprietario: DEP-QAR
aprovador: DEP-GOV
criado_em: 2026-07-28
atualizado_em: 2026-07-31
revisao_prevista: null
decisoes_relacionadas: [ADR-0004, ADR-0006, ADR-0008, ADR-0011]
substitui: []
substituido_por: null
resumo: Conta a sequencia FIT, mantem a serie de vereditos e projeta o estado de ratificacao e das ressalvas abertas e fechadas.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-GOV
ratificacao: nao-exigida
projecao_de: INC-2026-002 §1 e §3; ressalvas de FIT-2026-001 a FIT-2026-005
---

# Registro de Aptidao Arquitetural

## Proposito
Manter o registro unico e o contador oficial da sequencia `FIT-AAAA-NNN`, e a serie historica
de vereditos que alimenta a metrica de complacencia (FT-04).

## Escopo
Toda verificacao de aptidao arquitetural emitida. O mecanismo esta em
[FND-09 §10](../../foundation/09-meta-model.md); a decisao que o criou, em
[ADR-0004](../../decisions/ADR-0004-adocao-do-architecture-fitness-check.md).

## Responsaveis
| Papel | Responsavel |
|---|---|
| Executa | **DEP-QAR** — nunca quem produziu o artefato avaliado (FT-02) |
| Verifica a forma | DEP-GOV |
| Fornece evidencia | DEP-KMS |
| Aprova | DEP-EXE |
| Ratifica (C3) | **SOBERANO** |

---

## Contador oficial

| Sequencia | Ultimo atribuido | Proximo | Reinicia |
|---|---|---|---|
| `FIT-2026-NNN` | **036** | **037** | A cada ano |

> Numero **nunca e reaproveitado** (FND-03 §2.3). Atribuido por DEP-GOV.

> **Contador exercido, nao lido — aplicacao do PS-2026-018 (2026-08-12).** Antes de atribuir **`032`**: **`FIT-2026-031` ✅ existe · `FIT-2026-032` ✅ NAO existe** contra a copia datada *(`_backups/LucaX-Enterprise-OS_2026-08-12_pre-aplicacao-ps018-t44/`)* — `V1`. Movido na mesma mudanca.

> **⚠️ Contador exercido — e estava DEFASADO EM DOIS, quinta ocorrencia da familia de `RD-32` (Onda 3, 2026-08-12).** O cabecalho dizia **`028`/`029`** enquanto `FIT-2026-029` **e** `FIT-2026-030` existiam desde 2026-08-03. Antes de atribuir **`031`**, testou-se a existencia de `FIT-2026-031-*` contra a **copia datada anterior as edicoes** *(`_backups/LucaX-Enterprise-OS_2026-08-12_pre-onda-3/`)*: **`FIT-2026-030` ✅ existe · `FIT-2026-031` ✅ NAO existe** — `V1`. Corrigido **`028`/`029` → `031`/`032`**.

> **Contador exercido, nao lido — Missao 1.13.14.** Antes de atribuir **`030`**, testou-se a
> existencia de `FIT-2026-030-*` contra a **copia datada anterior as edicoes**
> *(`_backups/LucaX Enterprise OS-2026-08-03-antes-do-adr-sucessor/`)*: **`FIT-2026-029` ✅ existe ·
> `FIT-2026-030` ✅ NAO existe**. `SF-32`: criar o artefato e incrementar o contador sao **a mesma
> mudanca** (`CV-04`, `IX-02`).
>
> **Contador exercido, nao lido — Missao 1.13.13.** Antes de atribuir **`029`**, testou-se a
> existencia de `FIT-2026-029-*` contra a **copia datada anterior as edicoes**
> *(`_backups/LucaX Enterprise OS-2026-08-03-antes-da-terceira-skill/`)*: **`FIT-2026-028` ✅ existe ·
> `FIT-2026-029` ✅ NAO existe**. `SF-32`: criar o artefato e incrementar o contador sao **a mesma
> mudanca** (`CV-04`, `IX-02`).
>
> **Contador exercido, nao lido — Missao 1.13.12.** Antes de atribuir **`028`**, testou-se a
> existencia de `FIT-2026-028-*` contra a **copia datada anterior as edicoes**
> *(`_backups/LucaX Enterprise OS-2026-08-03-pre-missao-1-13-12/`)*: **`FIT-2026-027` ✅ existe ·
> `FIT-2026-028` ✅ NAO existe**. `SF-32`: criar o artefato e incrementar o contador sao **a mesma
> mudanca**.

> **Contador exercido, nao lido — Missao 1.13.4.4.** Antes de atribuir **`023`**, contaram-se
> **22** arquivos `FIT-2026-*` no acervo e testou-se a existencia de `FIT-2026-023`: **nao
> existia**. Depois da criacao, a contagem foi remedida em **23**. `SF-32`: criar o artefato e
> incrementar o contador sao **a mesma mudanca**.

> **Contador exercido, nao lido — Missao 1.13.4.2.** Contaram-se **19** arquivos `FIT-2026-*` na
> **copia datada anterior as edicoes** *(`_backups/…_2026-07-31_pre-missao-1-13-4-2/`)* e testou-se a
> existencia de `FIT-2026-020`, `-021` e `-022`: **nenhum existia**, e a contagem foi de **19 → 22**.

> **Contador exercido, nao lido — `V1` de MEM-APR-0006.** Antes de atribuir **`019`**, contaram-se
> **18** arquivos `FIT-2026-*` na **copia datada anterior as edicoes** *(`_backups/…_2026-07-31_pre-missao-1-13-4/`)*
> e testou-se a existencia de `FIT-2026-019-*.md`: **nao existia**, e a contagem foi de **18 → 19**.
> Antes de atribuir **`018`**, contaram-se
> **17** arquivos `FIT-2026-*` na **copia datada anterior as edicoes** e testou-se a existencia de
> `FIT-2026-018-*.md`: **nao existia**, e a contagem foi de **17 → 18**. Antes de atribuir **`017`**, testou-se a
> existencia de `FIT-2026-017-*.md` contra a **copia datada anterior as edicoes**: **nao existia**,
> e a contagem foi de **16 → 17**. Antes de atribuir **`016`**, testou-se
> a existencia de `FIT-2026-016-*.md`: **nao existia**. **Primeira vez que a verificacao e
> exercida apos `RD-32` codificar a causa em `SF-32`**, e ela passou.

> **Correcao de `RD-32`.** Este contador declarava **`013` / `014`** enquanto a tabela abaixo ja
> listava **`FIT-2026-014`** — defasagem de **um**, e o mesmo valor defasado constava de
> [`governance/README`](../README.md). **Segunda ocorrencia da familia**, cuja primeira correcao
> — documentada em nota daquele indice — atingiu o **valor** e nao o **gatilho `CV-04`**. A causa
> esta agora codificada em **`SF-32`** de
> [ADR-0021](../../decisions/ADR-0021-framework-de-specifications.md), e o metodo que a encontrou
> em [MEM-APR-0006](../../memory/aprendizado/MEM-APR-0006-exercer-o-contador-revela-o-defeito.md)
> `V1` — *pedir ao contador, nao le-lo*.

## Verificacoes emitidas

| ID | Objeto avaliado | Classe | Veredito | Ressalvas | Ratificacao | Data |
|---|---|---|---|---|---|---|
| [**FIT-2026-019**](FIT-2026-019-admissao-do-medally.md) | **RFC-0021, ADR-0026, a Carta candidata `PRO-medally` e o PRIMEIRO exercicio do portao de `ADR-0007`** | **C2** | `apto-com-ressalva` | **4** | **nao exigida** *(`ADR-0015`, `FT-10`)* | 2026-07-31 |
| [**FIT-2026-020**](FIT-2026-020-emenda-do-portao-de-origem-externa.md) | **`RFC-0022` e `ADR-0027`** — `G0` e `RECOGNIZE` no portao de origem externa | **C2** | `apto-com-ressalva` | **3** | **nao exigida** *(`ADR-0015`, `FT-10`)* | 2026-07-31 |
| [**FIT-2026-021**](FIT-2026-021-independencia-de-verificacao-por-fornecedor.md) | **`RFC-0023` e `ADR-0028`** — independencia de verificacao por fornecedor | **C3** | `apto-com-ressalva` | **4** | **nao exigida** *(`ADR-0015`, `FT-10`)* | 2026-07-31 |
| [**FIT-2026-022**](FIT-2026-022-superacao-de-ato-por-evidencia-posterior.md) | **`RFC-0024` e `ADR-0029`** — caminho de superacao de ato por evidencia posterior | **C3** | `apto-com-ressalva` | **4** | **nao exigida** *(`ADR-0015`, `FT-10`)* | 2026-07-31 |
| [**FIT-2026-023**](FIT-2026-023-admissao-do-nxtrack.md) | **`RFC-0025`, `ADR-0030` e o SEGUNDO exercicio do portao de `ADR-0007`** — o primeiro sob a norma emendada. **Os dois objetos avaliados entraram em VIGOR em 2026-08-01**, pelo nono ato: `ADR-0030` `ativo` · `ratificada`, `RFC-0025` `aprovado`, e o Produto [`PRO-nxtrack`](../../products/nxtrack/carta.md) criado. **As 4 ressalvas seguem ABERTAS**, com dono e gatilho — o item **V** do ato as manteve expressamente, e `RECOGNIZE` **declara que nao avaliou merito** | **C2** | `apto-com-ressalva` | **4** | **nao exigida** *(`ADR-0015`, `FT-10`)* | **2026-08-01** |
| [**FIT-2026-024**](FIT-2026-024-primeira-spec.md) | **`SPC-001`, `ADR-0031` e `RFC-0026` — a PRIMEIRA `Spec` do acervo.** `FIT` **exigido, nao opcional**: a classe do objeto e `C2`, e `SF-24` item **(9)** o poe no `DoD`. Mede **27 de 32** regras `SF-*` saindo de *determinadas* para *observadas*, **1** reproducao **barrada antes de escrita** e o custo de contexto nas **duas** direcoes — desce a `13` linhas na consulta enderecada, sobe `311` na leitura integral. **Contador exercido, nao lido:** testou-se a existencia de `FIT-2026-024` contra a copia datada — **nao existia** | **C2** | `apto-com-ressalva` | **4** | **nao exigida** *(`ADR-0015`, `FT-10`)* | **2026-08-02** |
| [**FIT-2026-025**](FIT-2026-025-emenda-de-sf-10.md) | **`ADR-0032`, `RFC-0027` e os 4 candidatos — a emenda que sana `RD-91`.** `FIT` **exigido, nao opcional**: a classe e `C3`, e `CC-04`/`CV-07` o poem em `QG-6`. Mede **27 linhas** de norma nova contra **3 artefatos por `Spec`** economizados, e conta **4 de 4** incompatibilidades de `FND-04 §3.1` dissolvidas em `C1 · T2`. **`1` reproducao barrada antes de escrita** — a emenda confinada a `FND-11 §5`, que **nao sanaria** | **C3** | `apto-com-ressalva` | **4** | **nao exigida** *(`ADR-0015`, `FT-10`)* | **2026-08-02** |
| [**FIT-2026-026**](FIT-2026-026-framework-de-skills.md) | **`ADR-0033` — a instituicao do Framework de Skills** | **`apto-com-ressalva`** | `QG-6` liberado. **`R1`, e nao bloqueia:** `TPL-skill` **nao produz `Skill` conforme** — omite `gatilho` **e** `capabilities` do frontmatter, contra os *atributos minimos* de `FND-09 §E-13`, medido com controle positivo. **NAO impede** a Skill de funcionar: os campos sao exigidos pela norma e podem ser escritos a mao (`AC-07`), e `0` Skills existem, logo `0` fichas nao conformes foram produzidas. `RD-122` ABERTO. **DEP-QAR NAO recomenda liberar `GO-TO-SKILLS` aqui** — liberar portao e ato de autoridade, nao materia de parecer (`FT-10`) |
| [**FIT-2026-027**](FIT-2026-027-primeira-skill.md) | **`ADR-0034` e a primeira `Skill`** | **`apto-com-ressalva`** | `QG-6` liberado, **13 verificacoes**, 11 verdes. **`R1`** — `TPL-skill` omite `capabilities` e `gatilho` (`RD-122`), **nao bloqueia**: escritos a mao sem criar campo novo. **`R2`** — **o Framework nao saiu ileso do primeiro uso**: `SK-09` **defeituosa** *(erro de categoria: conta atributo de frontmatter como bloco de corpo)*, `SK-10` e `SK-24` **insuficientes**. **3 em 26 (11,5%)** contra **5 em 32 (15,6%)** de `SPC-001`. Corrigi-los exige **`ADR` sucessor**, porque `ADR-0033` e `M1` |
| [**FIT-2026-028**](FIT-2026-028-segunda-skill.md) | **`ADR-0035` e a segunda `Skill`** | **`apto-com-ressalva`** | `QG-6` liberado, **16 verificacoes**, 13 verdes. **`R1` — DEP-QAR corrige o proprio registro:** `SK-24` nunca foi *"incalculavel"* *(a mediana de um elemento e esse elemento)*; ela e **calculavel e VAZIA ate `n = 3`**, demonstrado por algebra. A conclusao de `FIT-2026-027` sobrevive; o fundamento e que estava errado. **`R2` — os tres defeitos sao do FRAMEWORK**, por reaparecerem identicos em caso disjunto; **`0` defeitos novos no segundo uso**. **`R3` — `RD-122` exercido pela segunda vez**, e a repeticao o converte de peculiaridade do caso em **propriedade do template**. **DEP-QAR recomenda ESPERAR a terceira `Skill`** para o `ADR` sucessor: `SK-09` e `SK-10` tem sinal maduro, **`SK-24` nao** |
| [**FIT-2026-029**](FIT-2026-029-terceira-skill.md) | **`ADR-0036` e a terceira `Skill`** | **`apto-com-ressalva`** | `QG-6` liberado, **10 verificacoes verdes**, **4 ressalvas**. **`R1` — recusa a leitura confortavel de `SK-24`:** os dois *"nao"* anteriores eram **impossibilidade algebrica** e este e **propriedade das instancias**; **a serie util tem `1` elemento**, e com `3` pontos a mediana **nao e estavel**. **`R2` — `SK-09` e `SK-10` FECHAM**, e a terceira prova mais que a segunda porque **o autor conhecia os defeitos e escreveu contra eles, e eles ocorreram assim mesmo**. **`R3` — `RD-122` pela terceira vez.** **`R4` — a ancoragem do veredito nao tem portao, e o merito e de UM produto so.** **DEP-QAR recomenda ABRIR o `ADR` sucessor AGORA, e NAO esperar a quarta `Skill`** |
| [**FIT-2026-030**](FIT-2026-030-sucessor-parcial-do-framework-de-skills.md) | **`ADR-0037` e o sucessor parcial do Framework** | **`apto-com-ressalva`** | `QG-6` liberado, **13 verificacoes verdes**, **3 ressalvas**. **`R1` — o Framework passa a ter DUAS sedes vigentes** e o custo de contexto **sobe**; a unica coisa que unifica e a promocao a `FND`, **`C3` com ato**, e o ponto de cruzamento **nao se estima** (`CE-04`). **`R2` — `SK-22` e `SK-25` entraram em `SK-27` por LEITURA, nao por reprovacao observada**, e `SK-25` **nunca fora exercida**; homologados porque `SK-27` **nao reescreve enunciado, so acrescenta piso**. **`R3` — o custo do rito NAO caiu:** `4 = 5 − 1`, e o `1` e a ficha. **DEP-QAR confere na fonte a corroboracao de `SK-22` no piso `n = 2`, e homologa a exclusao de `R4` DECLARANDO o proprio conflito de interesse**, por te-la levantado |
| [**FIT-2026-031**](FIT-2026-031-a-mente-reconhece-o-corpo.md) | **`ADR-0038` e `RFC-0033` — a Mente reconhece o Corpo** | **`apto-com-ressalva`** | `QG-6` liberado, **9 verificacoes verdes**, **3 ressalvas**. **`R1` — o acervo passa a apontar para `3` repositorios que NAO mede** e o ponteiro envelhece (`A-297`); dono **DEP-GOV**, gatilho: mudanca de caminho das camadas. **`R2` — os TRES contadores de sequencia estavam DEFASADOS** *(familia `RD-32`/`RD-95`; a Missao 1.13.14 gravou a nota e nao moveu o cabecalho)* — corrigidos nesta emissao, e **o sinal e reincidencia estrutural**. **`R3` — rito inteiro em sessao unica**, separacao **por papel** declarada; mitigacao: `F3`–`F5` e `F8` sao **mecanicos**, reproduziveis contra a copia datada e o git |
| [**FIT-2026-032**](FIT-2026-032-aplicacao-do-decimo-primeiro-ato.md) | **`MSG-2026-0011`, `RFC-0034`, `ADR-0039` e a aplicacao dos itens I–VIII do `PS-2026-018`** | **`apto-com-ressalva`** | `QG-6` liberado, **9 verificacoes verdes**, **3 ressalvas**. **`F4` e a estrela: a parada `§5(a)` foi EXERCIDA** — `gente` e `coo` devolvidos ao Soberano em vez de esticados. `R1` Cartas crescem ~30–40% (dono DEP-KMS/DEP-EXE) · `R2` fila do Soberano +2 · `R3` `PADRAO→§8` mecanico com encaixe fraco, muda por sucessor |
| [**FIT-2026-033**](FIT-2026-033-framework-de-workflows.md) | **`ADR-0040` e `RFC-0035` — o Framework de Workflows** | **`apto-com-ressalva`** | `QG-6` liberado, 6 verificacoes verdes, 3 ressalvas: `R1` 30 regras determinadas-nao-observadas *(0 Workflows)* · `R2` a contribuicao propria (`WF-19`–`25`) e a parte menos testada — a historia de `SK-12` outra vez, nomeada · `R3` `AW-2`/`AW-3` abertos, o primeiro Workflow real esbarra neles |
| [**FIT-2026-034**](FIT-2026-034-framework-de-ferramentas-e-modelos.md) | **`ADR-0041` e `RFC-0036` — o Tool & Model Framework** | **`apto-com-ressalva`** | `QG-6` liberado, 6 verdes, 3 ressalvas: `R1` determinadas-nao-observadas *(0 `TOL`)* · **`R2` a via de uso esta BLOQUEADA por defeito alheio** *(`AF-1`/`AF-2` do template, pre-condicao nao cumprida — na cara)* · `R3` fallback e falha plausivel-e-errada sem instancia |
| [**FIT-2026-035**](FIT-2026-035-framework-de-agentes.md) | **`ADR-0042` e `RFC-0037` — o Agent Framework** | **`apto-com-ressalva`** | `QG-6` liberado, 6 verdes, 3 ressalvas: `R1` determinadas-nao-observadas *(0 agentes)* · **`R2` a armadilha do piloto de guarda nomeada ANTES do desenho** *(`ES-02`: Guarda nunca coordenada por Linha)* · `R3` `AA-1` aberto *(colisao atenuada no cartao, viva nas fontes)* |
| [**FIT-2026-036**](FIT-2026-036-framework-de-execucao-e-avaliacao.md) | **`ADR-0043` e `RFC-0038` — o Execution & Evaluation Framework** | **`apto-com-ressalva`** | `QG-6` liberado, 6 verdes, 3 ressalvas. **`AE-3` DISPARA nesta verificacao e esta NA CARA** *(DEP-QAR titular da materia — mitigacao do candidato + sinais mecanicos; segunda vez do precedente FIT-2026-030)*; e o padrao MEDIDO da fabrica: **a contribuicao propria e sempre a parte menos testada — quatro membros na serie** |
| [**FIT-2026-018**](FIT-2026-018-vigencia-do-framework-de-specifications.md) | **A APLICACAO do setimo ato soberano** — os **14** objetos em vigor, a ordem, a atomicidade, a integridade e a reconciliacao | **C3** | `apto-com-ressalva` | **3** | **nao exigida** *(`ADR-0015`, `FT-10`)* | 2026-07-30 |
| [**FIT-2026-017**](FIT-2026-017-convergencia-pre-ratificacao.md) | **RFC-0020, ADR-0024, ADR-0025, PS-2026-011, PS-2026-012, PS-2026-013, PS-2026-009 2.0.0**, os **6** candidatos novos e a cascata de indices | **C3** | `apto-com-ressalva` | **3** | **nao exigida** *(`FT-10`)* | 2026-07-30 |
| [**FIT-2026-016**](FIT-2026-016-canonizacao-e-propagacao.md) | **RFC-0018, ADR-0022, PS-2026-009, RFC-0019, ADR-0023, PS-2026-010, PT-2026-008**, os **6** candidatos e a cascata de indices | **C3** | `apto-com-ressalva` | **4** | **nao exigida — por `FT-10`** | **2026-07-29** |
| [FIT-2026-001](FIT-2026-001-meta-model.md) | ADR-0003, ADR-0004, FND-09 | C3 | `apto-com-ressalva` | **3** | **nao exigida** *(por ato — MSG-2026-0002 §4)* | 2026-07-28 |
| [FIT-2026-002](FIT-2026-002-artifact-framework.md) | ADR-0005, ADR-0006, FND-10 | C3 | `apto-com-ressalva` | **4** | **nao exigida** *(por ato — MSG-2026-0002 §4)* | 2026-07-28 |
| [FIT-2026-003](FIT-2026-003-consolidacao-baseline.md) | ADR-0007, ADR-0008, FND-03/09/10, INC-2026-001/002 | **C2** | `apto-com-ressalva` | **3** | nao exigida | 2026-07-28 |
| [FIT-2026-004](FIT-2026-004-conhecimento-do-soberano.md) | ADR-0009, ADR-0010, FND-03/06/10, MEM-EST-0001 | **C2** | `apto-com-ressalva` | **4** | nao exigida | 2026-07-28 |
| [FIT-2026-005](FIT-2026-005-cartas-de-departamento.md) | ADR-0011, TPL-carta-departamento, IDX-capabilities, **DEP-QAR**, **DEP-ENG** | **C2** | `apto-com-ressalva` | **5** | nao exigida | 2026-07-28 |
| [**FIT-2026-006**](FIT-2026-006-validacao-interclasses.md) | MSG-2026-0001, **DEP-QAR**, **DEP-ENG**, **DEP-EXE**, **DEP-KMS**, TPL-carta-departamento | **C2** | `apto-com-ressalva` | **4** | nao exigida | 2026-07-28 |
| [**FIT-2026-007**](FIT-2026-007-revisao-estrutural-i.md) | MSG-2026-0002, **DEP-EXE**, **DEP-KMS**, **MEM-EST-0001**, RFC-0009, ADR-0012, INC-2026-002 | **C2** | `apto-com-ressalva` | **4** | nao exigida | 2026-07-28 |
| [**FIT-2026-008**](FIT-2026-008-rollout-das-cartas.md) | **DEP-GOV**, **DEP-TLS**, **DEP-PRD**, **DEP-OPS**, **DEP-GRW**, MSG-2026-0003, RFC-0010, ADR-0013, RFC-0011, ADR-0014, IDX-departamentos, PS-2026-002 | **C2** | `apto-com-ressalva` | **4** | nao exigida | 2026-07-28 |
| [**FIT-2026-009**](FIT-2026-009-ativacao-e-endurecimento.md) | **PS-2026-003**, **PT-2026-001**, IDX-departamentos **1.1.0**, IDX-governance **1.3.0**, catalogo mestre, **as nove Cartas** *(verificacao, sem alteracao)* | **C2** | `apto-com-ressalva` | **4** | nao exigida | 2026-07-29 |
| [**FIT-2026-010**](FIT-2026-010-aplicacao-do-ato-soberano.md) | **DEP-GOV**, **DEP-TLS**, **DEP-PRD**, **DEP-OPS**, **DEP-GRW**, **ADR-0014**, **FND-01 1.4.0**, **ADR-0015**, **MSG-2026-0004**, IDX-departamentos **1.2.0**, catalogo mestre | **C3** | `apto-com-ressalva` | **4** | **nao exigida — por `FT-10`** | 2026-07-29 |
| [**FIT-2026-011**](FIT-2026-011-fechamento-de-autoridade.md) | **DEP-QAR 1.2.0**, **RFC-0012**, **ADR-0016**, **RFC-0013**, **ADR-0017**, **PS-2026-004**, **PS-2026-005**, **PS-2026-006**, **MSG-2026-0005**, **PT-2026-002**, IDX-departamentos **1.3.0**, catalogo mestre | **C3** | `apto-com-ressalva` | **3 + 2 recl.** | **nao exigida — por `FT-10`** | 2026-07-29 |
| [**FIT-2026-012**](FIT-2026-012-fechamento-normativo-final.md) | **RFC-0014**, **ADR-0018**, **PS-2026-007**, **RFC-0015**, **ADR-0019**, **PS-2026-008**, **PT-2026-003**, catalogo mestre | **C3** | `apto-com-ressalva` | **2 + 2 recl.** | **nao exigida — por `FT-10`** | 2026-07-29 |
| [**FIT-2026-013**](FIT-2026-013-verificacao-de-ratificacao.md) | **PT-2026-004**, **candidatos cumulativos**, **PS-2026-004 a 008**, catalogo mestre | **C3** | `apto-com-ressalva` | **1 + 1 recl.** | **nao exigida — por `FT-10`** | 2026-07-29 |
| [**FIT-2026-014**](FIT-2026-014-regime-ministerial-e-cobertura-de-contexto.md) | **RFC-0016**, **ADR-0020**, **PT-2026-006**, **MEM-APR-0005**, catalogo mestre **2.3.0** | **C2** | `apto-com-ressalva` | **2** | **nao exigida — por `FT-10`** | 2026-07-29 |
| [**FIT-2026-015**](FIT-2026-015-framework-de-specifications.md) | **RFC-0017**, **ADR-0021**, **`TPL-spec` 1.1.0**, **PT-2026-007**, **MEM-APR-0006**, catalogo mestre | **C2** | `apto-com-ressalva` | **3** | **nao exigida — por `FT-10`** | 2026-07-29 |

> **FIT-2026-010 e o primeiro `FIT` do acervo cujo `nao-exigida` tem fundamento normativo, e
> nao inferencia.** Ate ele, o campo era preenchido por leitura de FND-10 §2.2 **com duvida
> declarada**; a partir de **`FT-10`**
> ([ADR-0015](../../decisions/ADR-0015-fitness-check-e-parecer-nao-decisao.md)), e regra.
> **As tres coisas que a nota abaixo declarava verdadeiras continuam verdadeiras** — `FIT-2026-001`
> segue afirmando ratificacao inexistente, e **o ato de 2026-07-29 vedou expressamente a edicao
> retroativa**. O que mudou e que a **causa normativa** deixou de estar aberta.

> **FIT-2026-006 e o primeiro `FIT` aprovado por DEP-GOV por impedimento de DEP-EXE declarado
> em Carta.** FIT-2026-003 ja o fora, mas por desvio sem Carta que o sustentasse; agora o
> impedimento esta escrito em `DEP-EXE §10, I-2`. **Segunda ocorrencia** do impedimento cruzado
> — achado **C5** de REV-CONSOLIDACAO.

> **Coluna Ratificacao — projecao de [MSG-2026-0002 §4](../../memory/operacional/MSG-2026-0002-ato-soberano-cartas-comando-plataforma-e-contexto.md)**
> (PJ-02). O que os arquivos de FIT-2026-001 e FIT-2026-002 declaram em si proprios **nao** e a
> fonte corrente: sao artefatos **M1**, congelados no ato (PJ-04).
>
> **O ato soberano de 2026-07-28 acolheu os dois como pareceres, *sem eleva-los a norma*.** O
> estado corrente e **`nao exigida` por ato explicito** — nao por inferencia, e **nao por
> ratificacao**: *acolher* nao e *ratificar*.
>
> **Tres coisas continuam verdadeiras, e nenhuma foi corrigida pelo ato:**
> **(1)** FIT-2026-001 **continua afirmando, no proprio texto**, uma ratificacao que nunca
> ocorreu — e **M1**, e nao se edita.
> **(2)** O `nao-exigida` de FIT-2026-002 **coincidiu** com o estado correto, mas **nao foi
> corretamente derivado** quando escrito; a coincidencia nao e acerto.
> **(3)** A ambiguidade normativa **FND-10 §2.2 × §10.3** que causou os dois defeitos
> **permanece aberta**, migrada para [RFC-0009 Q2](../../rfcs/RFC-0009-integridade-e-alcance-do-ato-de-ratificacao.md).
> [INC-2026-002](../incidents/INC-2026-002-ratificacao-declarada-em-fitness-check.md) fechou com
> a **causa tratada, nao eliminada**.

## Serie de vigilancia (FT-04)

| Metrica | Valor | Direcao |
|---|---|---|
| Vereditos consecutivos `apto` **sem nenhuma ressalva** | **0** | Tres seguidos escalam ao Soberano |
| Vereditos emitidos | **13** | — |
| Vereditos `inapto` emitidos | 0 | Zero permanente e sinal de criterio frouxo |
| Ressalvas abertas com dono e gatilho | **26** | → 0 na reavaliacao |
| **Ressalvas fechadas por ciclo** | **0, 0, 2, 0, 2, 2, 7, 3, 0, 2, 0, 1, 0** *(1o ao 13o ciclo)* | Divida declarada que nunca fecha e divida, nao controle |
| Ressalvas **fechadas no total** | **19** de **44** emitidas | **R4 de FIT-2026-002 fechou com evidencia** — duas descidas consecutivas itemizadas |
| **Ressalvas reclassificadas sem duplicar** | **8** — as sete anteriores mais **FIT-2026-012 R1**, esta ultima **com correcao de erro proprio** | **FIT-2026-013 nao registrou nenhum objeto em duplicidade** |
| Ressalvas declaradas **`nao-avaliaveis`** | **0** | R1 de FIT-2026-004 **fechou com medicao**; R2 voltou a **aberta e aplicavel** |
| **Ciclos consecutivos de crescimento do acervo** | **11** | **PS-1 respondida pelo Soberano e formalizada em [ADR-0013](../../decisions/ADR-0013-criterio-de-horizonte-e-consolidacao.md):** crescimento e **gatilho de revisao**, nao obrigacao de consolidar (`HZ-01`) |
| **Pendencias escaladas ao SOBERANO** | **6** | **PS-5** *(`DEP-KMS` e `DEP-ENG`)* · **PS-6** *(RD-09)* · **PS-7** *(RD-02)* · **PS-9** *(RD-14 — [PS-2026-007](../pacote-soberano-2026-07-29-rd-14.md))* · **PS-10** *(RD-15 — [PS-2026-008](../pacote-soberano-2026-07-29-rd-15.md))* · **PS-11** *(aprovacao de FIT-2026-011 e FIT-2026-012 — cascata no terminus, duas vezes)*. **PS-1 a PS-4 respondidas** |
| **Revisoes estruturais executadas** | **1** | FND-02 §9.4: tres *"manter tudo"* seguidos escalam ao Soberano. **Esta e a 1a, e nao concluiu "manter tudo"** |

### Ressalvas abertas

| Origem | Ressalva | Dono | Gatilho |
|---|---|---|---|
| **FIT-2026-018 R1** | **`RD-49` — `DEP-OPS`, `DEP-GRW` e `DEP-TLS` 1.1.0 declaram em §13.2 `437 · 443 · 424` linhas contra `438 · 444 · 425` medidas.** Terceira ocorrencia da familia de `RC-01` e `RD-46`. **Nao corrigivel por edicao:** as tres estao ratificadas (`LV-04`) | DEP-EXE | **Proximo ato que alcance Carta de Departamento** |
| **FIT-2026-018 R2** | **A prova de `QG-1` depende de detector construido nesta missao**, cuja primeira versao tinha **8 falsos positivos** achados na calibracao | DEP-QAR | **Proximo uso do detector** — recalibrar contra estado conhecido, **nao invocar este precedente** |
| **FIT-2026-018 R3** | **`RD-47` e `RD-48` seguem abertos**, e o ato de 2026-07-30 **nao os alcanca** | DEP-GOV | **Regra escrita de regime de estado** |
| FIT-2026-002 R4 | Reducao de contexto calculada, nao observada — serie de **seis** medicoes | DEP-KMS | **Duas descidas consecutivas com composicao itemizada** *(criterio endurecido por RE-08)*. **A 1a ocorreu**: 21,3% -> **18,9%** ([FIT-2026-008 §F5.1](FIT-2026-008-rollout-das-cartas.md)) |
| FIT-2026-003 R1 | 10 regras de fronteira sem possibilidade de exercicio hoje | DEP-EXE | **2a** revisao estrutural |
| FIT-2026-003 R2 | Portao de admissao e 4 classificacoes com zero membros | DEP-GOV | 1o candidato do Legacy |
| FIT-2026-004 R2 | Abstracoes com zero membros: `inferred` *(= classe 4 de autoridade — **o mesmo objeto**, REV-ESTRUTURAL-I §10.2)* e os 4 pacotes de contexto | DEP-GOV | 🔁 **RECLASSIFICADA, nao resolvida.** Sai de `nao-avaliavel por registro inativo` e volta a **aberta e aplicavel** — o registro entrou em vigor, mas **nenhum componente foi criado**. Gatilho intacto: *"1o componente criado apos a vigencia"* |
| **FIT-2026-005 R1** | 10 regras `DC` exercidas 10 de 10; `PR-1` e `PR-2` com 0 membros. **10 de 10 medidas** na Missao 1.9 ([REV-ROLLOUT §3.2](../../foundation/revisao-arquitetural-rollout-cartas-2026-07-28.md)) — e a medicao **nao fecha** a ressalva | DEP-EXE | *"1a Carta escrita por **autor distinto de DEP-EXE**"* — nenhuma Carta escrita na Missao 1.8 |
| **FIT-2026-005 R3** | Crescimento consecutivo do acervo sem nenhuma consolidacao | DEP-EXE; **SOBERANO** | **Disparado.** EV-08 encerrada como **`AJUSTAR`**, com **zero** artefatos consolidados → **ESCALADO em PS-1** |
| **FIT-2026-006 R1** | **DEP-EXE e autor de 9 de 9 Cartas**; contrato nunca testado contra autor distinto | DEP-EXE | 1a Carta por autor distinto — depende de **IC-3**. **AGRAVADA na Missao 1.9:** de 4 de 4 para **9 de 9** |
| **FIT-2026-006 R3** | Crescimento consecutivo do acervo — **7o ciclo** | DEP-EXE; **SOBERANO** | **Disparado.** Mesma escalada de R3 de FIT-2026-005 → **PS-1**. Escaladas **como uma**, para nao inflar a contagem |
| **FIT-2026-007 R1** | **Concentracao em DEP-EXE confirmada por quatro gatilhos de especializacao**, e o movimento corretivo e **impossivel nesta fase**: exige criar agente *(proibido)* ou alterar FND-09 §8.2 *(C3)* | DEP-EXE | **Primeiro agente**, ou **IC-3** resolvido |
| **FIT-2026-007 R3** | **DEP-QAR revisa e aprova a revisao estrutural.** **Sem alternativa na estrutura atual** | DEP-GOV | 🔁 **RECLASSIFICADA na Missao 1.9.** O gatilho — *Carta de DEP-GOV declarando o impedimento em B9* — **foi cumprido** (`DEP-GOV I-2`); **o residuo persiste** em REV-ROLLOUT §0.1. Novo gatilho: **primeiro agente** *(IC-3)*. Achado **RC-08** |
| **FIT-2026-008 R1** | **As 8 regras `HZ` nascem com zero membros observados.** `HZ-02` nunca disparou; `HZ-04` tambem nao. **5o ciclo** instituindo regime preventivo inteiro | DEP-EXE | **Duas revisoes estruturais consecutivas** sem que `HZ-02` nem nenhum `HZ-04` dispare ([ADR-0013 §12](../../decisions/ADR-0013-criterio-de-horizonte-e-consolidacao.md)) |
| **FIT-2026-008 R2** | **8o ciclo consecutivo de crescimento, e o maior acrescimo absoluto da serie: +4.754 linhas (15,4%)** | DEP-EXE | **Primeiro horizonte avaliavel sob `HZ-02`.** `HZ-01` retira a leitura de que crescer e falha; **nao retira o fato** |
| **FIT-2026-008 R3** | **Segregacao no limite pela 3a missao seguida, e de forma nova:** DEP-QAR executa o `FIT` com a propria Carta ratificada no ciclo; DEP-GOV o aprova tendo sido autor da forma de REV-ROLLOUT; **DEP-EXE e autor de 9 de 9** | DEP-GOV | **Primeiro agente criado**, ou **IC-3** resolvido. Achado **RC-08** |
| **FIT-2026-008 R4** | **Tres achados retidos em Cartas ja ratificadas, nao corrigiveis sem ato novo** — **RC-01**, **RC-05** e **RC-07** | DEP-EXE | 🔁 **RECLASSIFICADA na Missao 1.10, nao fechada.** O gatilho literal — *"proxima emenda a cada uma das tres Cartas"* — **foi cumprido**: as tres emendas existem, com diff literal e hash, em [PS-2026-003](../pacote-soberano-2026-07-29-emendas.md). **Fechar depende do ato**, nao da emenda. Novo gatilho: **ato soberano sobre PS-2026-003** |
| **FIT-2026-009 R2** | **`RD-02` — os campos `GOV→KMS` e `QAR→KMS` de FND-02 §4 declaram `E`, e a leitura obrigatoria da mesma tabela declara que a Guarda veta Linha e Plataforma.** As Cartas resolvem de **tres** formas. **E o unico achado aberto que toca autoridade** | DEP-GOV | Proxima emenda a **FND-02**, ou primeiro veto real sobre Plataforma. **Impede `GO-TO-SPECS` nos tres cenarios de ato** ([PT-2026-001 §11.1](../relatorio-transicao-2026-07-29-departamentos.md)) |
| **FIT-2026-009 R3** | **`RD-01` e `RD-03` retidos, por motivos opostos:** RD-03 esta em Carta **ratificada**; RD-01 esta em Carta **em revisao** cujo `H-A` **ja foi submetido** ao Soberano. **3a vez que a imutabilidade retem defeito conhecido** | DEP-EXE | RD-03: proxima emenda a `DEP-KMS`. RD-01: **apos** a decisao sobre PS-2026-002 |
| **FIT-2026-009 R4** | **9o ciclo consecutivo de crescimento, e o segundo sem nenhuma Carta entrando em vigor.** Tres artefatos novos, zero consolidacoes | DEP-EXE | **Primeiro horizonte avaliavel sob `HZ-02`** — mesmo gatilho de R2 de FIT-2026-008, **nao contado em dobro** |
| **FIT-2026-010 R1** | **`RD-09` — `FND-10 §10.3` e `FND-09 §8.2` divergem de `FT-10`.** Duas fundacionais dizem que `FIT` se ratifica; a regra vigente diz que nao. **IC-2 fechou em FND-01 e o mecanismo reapareceu em outras duas** | **DEP-GOV** | **Proximo ato soberano que alcance FND-09 ou FND-10** — **PS-6** |
| **FIT-2026-010 R2** | **`RD-07` — duas emendas nao ratificadas por identificador invalido no ato.** **RC-05** e **RC-07** seguem abertos em Cartas em vigor | DEP-GOV; **SOBERANO** | **Reemissao do item 2 do ato** — **PS-5** |
| **FIT-2026-010 R3** | **`RD-08` — `ADR-0014` esta `ativo` e o proprio texto abre com *"NAO ESTA EM VIGOR"*.** O bloco esta dentro de `H-N`; corrigir exige ato novo | DEP-EXE | Proxima emenda a `ADR-0014`. **Mesmo mecanismo de RC-01** |
| **FIT-2026-010 R4** | **`RD-02` nao foi alcancado pelo ato, e continua sendo o unico achado aberto que toca autoridade.** **E a condicao nomeada do `GO-CONDITIONAL`** | **DEP-GOV** | 🔁 **RECLASSIFICADA na Missao 1.11** — junto com **R2 de FIT-2026-009**, mesmo objeto. Sai de *"sem instrumento"* e passa a *"**tratada pelo rito C3 completo**, com [RFC-0012](../../rfcs/RFC-0012-semantica-da-matriz-de-interacao.md), [ADR-0016](../../decisions/ADR-0016-semantica-da-matriz-de-interacao.md), diff literal, hashes e [PS-2026-004](../pacote-soberano-2026-07-29-rd-02.md)"*. Gatilho novo: **ato sobre PS-2026-004**. ⚠️ **As duas contam nas 24 abertas; o objeto e um so** |
| **FIT-2026-011 R1** | **`RD-14` — `QG-1` e liberado por `DEP-PRD`, que produz a Spec**, contra a regra literal de **FND-01 §6.2**, e **sem excecao formal registrada**. `DEP-PRD §5.2` reconhece o fato e `RP-1` declara o **risco**; **nenhum dos dois nomeia a colisao normativa** | **DEP-GOV** | **Antes da primeira Spec**, ou proxima emenda a FND-01 §6.2 / FND-09 §8.2. **Severidade Alta; sem instrumento pronto** |
| **FIT-2026-011 R2** | **`RD-15` — para Spec C2/C3, `FND-09 §8.2` e `FND-04 §2` dao aprovador e ratificador diferentes.** A regra de precedencia de FND-09 §8.2 resolve, e a **segunda metade dela — registrar o conflito como erro da tabela — nunca fora cumprida** | **DEP-GOV** | **Antes da primeira Spec C2**. O **registro do erro foi feito** em [PT-2026-002 §4.2](../relatorio-transicao-2026-07-29-fechamento.md); a **correcao** exige rito. **Severidade Alta** |
| **FIT-2026-011 R1** | 🔁 **RECLASSIFICADA na Missao 1.12.** Sai de *"severidade Alta, bloqueante e **sem instrumento**"* e passa a *"**tratada pelo rito C3 completo**, com [RFC-0014](../../rfcs/RFC-0014-liberacao-do-portao-qg-1.md), [ADR-0018](../../decisions/ADR-0018-liberacao-do-portao-qg-1.md), diff literal, hashes integrais e [PS-2026-007](../pacote-soberano-2026-07-29-rd-14.md)"* | **DEP-GOV** | Gatilho novo: **ato sobre PS-2026-007** — **PS-9** |
| **FIT-2026-011 R2** | 🔁 **RECLASSIFICADA na Missao 1.12.** Idem, com [RFC-0015](../../rfcs/RFC-0015-aprovador-e-ratificador-de-spec.md), [ADR-0019](../../decisions/ADR-0019-aprovador-e-ratificador-de-spec.md) e [PS-2026-008](../pacote-soberano-2026-07-29-rd-15.md). **A medicao encontrou uma terceira fonte** — FND-04 §6 —, que virou **RD-18** | **DEP-GOV** | Gatilho novo: **ato sobre PS-2026-008** — **PS-10** |
| **FIT-2026-011 R3** | **`RD-10` a `RD-13`** — `DEP-TLS §6.3` contradiz `DEP-PRD §6.3` e `DEP-GRW §6.3` sobre caminho operacional *(RD-10)*; **4 celulas** do candidato FND-02 declaram mais que a Carta do emissor *(RD-11)*; **FND-04 §2.1** nao distingue parecer de artefato de decisao *(RD-12)*; historico de **FND-10** fora de ordem *(RD-13)* | DEP-EXE *(RD-10, RD-11)* · DEP-GOV *(RD-12, RD-13)* | Proxima emenda ao artefato de cada um |
| **FIT-2026-012 R1** | **`RD-19` — dois pacotes pendentes reivindicam as mesmas versoes de FND-09 e FND-10.** Causa raiz do acervo: **candidatos sao publicados como *diff + hash*, sem arquivo**, e a emenda posterior **nao consegue se medir sobre a anterior** | **DEP-GOV** | **Promulgacao do primeiro dos dois pacotes.** Mitigado por `O1`–`O4` de [PS-2026-008 §5](../pacote-soberano-2026-07-29-rd-15.md), que vivem **no pacote e nao em norma** |
| **FIT-2026-012 R2** | **`RD-18` — FND-04 §6 e §2 geram a classe de uma Spec por criterios diferentes**, e o texto nao declara qual prevalece. A emenda **remete a §2** e deixa §6 como piso, **sem toca-lo** | **DEP-GOV** | **Proxima emenda a FND-04.** Mesma forma de defeito que **RD-12** nomeou |
| **FIT-2026-012 R1** | 🔁 **RECLASSIFICADA E CORRIGIDA na continuacao da Missao 1.12.** A afirmacao de que os candidatos viviam *"sem arquivo"* era **falsa** — os **6 existem e reproduzem os `H-A` publicados**. O defeito real e **o caminho nao declarado no pacote**. **A lacuna do cumulativo FECHOU** | **DEP-GOV** | **Reemissao de PS-2026-004, 005 ou 006** |
| **FIT-2026-013 R1** | **`RD-21` — a reemissao rebaseada de `PS-2026-008` e devida e nao foi executada**, por vedacao expressa a produzir minuta. A minuta vigente enumera o candidato **nao cumulativo** | **DEP-GOV** | **Primeira missao sem a vedacao**, ou **ato que alcance os dois pacotes**. **Mitigado, nao suprido**, por [PT-2026-004 §4](../relatorio-transicao-2026-07-29-ratificacao.md) |

| **FIT-2026-014 R1** | **`PA-07` supletiva nunca foi exercida** — a regra que designa o custodiante como executor na ausencia de nomeacao tem **zero casos observados**: e determinada, nao verificada | DEP-GOV | **Primeira invocacao real de `PA-07`**, ou o primeiro ato soberano que **nao nomeie** executor. **A Missao 1.13 nao a invocou:** `ADR-0021` nomeia executor em `SF-32` e na matriz de §5.3 |
| **FIT-2026-014 R2** | ✅ **FECHADA no candidato pela Missao 1.13.2** — [ADR-0024](../../decisions/ADR-0024-conformidade-de-contrato-das-fundacionais.md) fecha `RD-27` nos tres objetos. **Vigora com o ato.**  **`RD-27` deixa `FND-01` e `FND-02` em nao conformidade declarada** — vigoram sem quatro e sem cinco campos do contrato, e a correcao **altera `H-N`**, so cabendo em ato soberano. `AC-06` esta descumprido por dois documentos de **nivel 2** | DEP-GOV | **Proximo ato soberano que alcance `FND-01`, `FND-02` ou `FND-10`**. **Inalterada na Missao 1.13:** `0` bytes tocados nos tres, por determinacao |
| **FIT-2026-015 R1** | **As 32 regras `SF-*` do Framework de Specifications sao determinadas e nao observadas — nao existe nenhuma `Spec`.** `T-01` a `T-12` resolvem por regra citada, **nao por caso ocorrido** | **DEP-PRD** | **A primeira `Spec` real** — que depende de **`S1`** *(ato criando Produto)* ou **`S2`** *(ampliar a `Spec` a materia nao-produto, C3)*, ambas do SOBERANO |
| **FIT-2026-015 R2** | **`SF-09` institui 21 blocos obrigatorios de corpo sem que o custo tenha sido medido.** A mitigacao de `SF-31` — blocos independentes e requisito enderecavel por `RQ-nn` — e **projetada, nao verificada**; `CE-04` proibiu estimar, e **nada foi estimado** | **DEP-PRD** | **A primeira `Spec` medida contra o dobro da mediana do tipo** (`CE-05`) |
| **FIT-2026-016 R1** | **A duplicacao da norma da `Spec` sobrevive ao ato.** Apos aplicado `FND-11`, as 32 regras vivem em **dois textos**, e `ADR-0021` **nao dira** que foi superado — em **31 de 32** o merito e identico; **em `SF-32` a leitura sera errada** | **DEP-GOV** | **Primeira emenda a `FND-11`** — achado `RD-40` |
| **FIT-2026-016 R2** | ✅ **FECHADA no candidato pela Missao 1.13.2** — [ADR-0025](../../decisions/ADR-0025-extensao-da-propagacao-de-qg-1-as-cartas-restantes.md); a familia das 9 Cartas vai a **`0` afirmacoes falsas**.  **`RD-37` deixa 3 Cartas ratificadas afirmando que `DEP-PRD` libera `QG-1`.** A Missao 1.13.1 corrigiu **2 de 4** Cartas, por escopo determinado. O acervo passa de **11 afirmacoes falsas em 4 Cartas** para **3 em 3** | **DEP-EXE** *(propoe)*; revisa **DEP-GOV** | **Proximo ato que alcance `DEP-OPS`, `DEP-GRW` ou `DEP-TLS`.** Custo: **1 linha por Carta** |
| **FIT-2026-016 R3** | ✅ **FECHADA pela Missao 1.13.2** — a variante que a repetia **deixou de ser objeto**; `FND-01` entra em **uma** versao, cumulativa.  **`FND-01` sera emendada sem os quatro campos de `AC-08` se a variante `V1` for escolhida** — terceira ocorrencia de `RD-27`, e **a primeira em que o ato que a repete tinha como nao repetir**: a variante `V2` existe, esta medida e cabe no mesmo ato | **DEP-GOV** | **O proprio ato** — `Q2` de [PS-2026-009](../pacote-soberano-2026-07-29-fnd-11.md) |
| **FIT-2026-016 R4** | **A aprovacao de `FIT-2026-016` e parcialmente impedida:** `DEP-EXE` e **autor de `ADR-0023`** e do candidato `DEP-EXE` 1.1.0, e `I-2` veda aprovar `FIT` sobre objeto proprio. **Resolvido por recorte**, com `DEP-GOV` aprovando a parte impedida — precedente `FIT-2026-003` | **DEP-GOV** | **O proprio parecer** |
| **FIT-2026-017 R2** | **Primeira dispensa de RFC do acervo.** Legitima — `FND-04 §2`, duas condicoes verificadas e concordancia escrita entre partes distintas —, **e e precedente** | O proximo caso pode **invocar** este em vez de **reverificar as duas condicoes** | **DEP-GOV** | **Proxima decisao `C2` que dispense RFC** |
| **FIT-2026-017 R3** | **`RD-47` — o regime de estado na promulgacao de versao nova e costume, nao regra escrita.** Carta volta a `em-revisao`/`pendente` e recebe `O4`; fundacional permanece `ativo`/`ratificada` e **nao** recebe. Os dois sao precedentes vigentes, e **`FND-10 §5.2` nao os distingue** | O **`H-P`** de todo objeto futuro depende de qual precedente se aplica, e a escolha **nao e derivavel de norma** | **DEP-GOV** | **Proxima emenda de `FND-10 §5`** |
| **FIT-2026-015 R3** | 🔁 **MIGRADA na Missao 1.13.1** para instrumento vivo — **`RD-31` deixa o portao da `Spec` sem titular declarado em Carta alguma.** `DEP-PRD` reivindica `QG-1` em **8** afirmacoes que `ADR-0018` e `ADR-0019` tornaram falsas; **`DEP-EXE` nao o declara em nenhuma** *(0 ocorrencias, medido)*. Quem resolve pelas Cartas obtem `DEP-PRD`; a fonte diz `DEP-EXE` | **DEP-EXE** *(propoe)*; revisa **DEP-GOV** | **Antes da primeira `Spec`**, ou o proximo ato que alcance `DEP-PRD` ou `DEP-EXE`. **Atenuante que nao e cumprimento:** `LV-03` continua valendo — liberacao por quem produziu e **nula** |

> **Este razao NAO fecha, e a Missao 1.13 declara isso em vez de fechar por arredondamento —
> achado `RD-36`.** Medido por ferramenta nesta emissao: a tabela acima tem **31 linhas** e
> **28 ressalvas distintas** *(tres aparecem duas vezes, como **reclassificacao**: `FIT-2026-011 R1`,
> `FIT-2026-011 R2` e `FIT-2026-012 R1`)*; a de fechadas tem **18**; e a contagem de linhas de
> ressalva **nos proprios 15 arquivos `FIT`** devolve **55**, das quais **5** sao reclassificacoes
> embutidas. **Os tres numeros nao se reconciliam entre si**, e
> [`governance/README`](../README.md) declarava um quarto conjunto. **A reconciliacao completa
> NAO foi executada nesta missao** — exigiria classificar as 55 linhas uma a uma entre aberta,
> fechada, reclassificada e absorvida, o que e auditoria propria e nao cabia no escopo. **O que
> foi feito:** a cascata devida — **as 2 ressalvas de `FIT-2026-014`, ausentes desde a missao
> anterior, e as 3 de `FIT-2026-015`** — e **o registro do defeito com dono e gatilho**. Dono
> **DEP-QAR** *(fonte)* e **DEP-GOV** *(projecao)*; gatilho **proxima auditoria de ressalvas**.

### Ressalvas fechadas

| Origem | Ressalva | Fechada por | Data |
|---|---|---|---|
| **FIT-2026-017 R1** | **`FND-01` 1.7.0 nao e aplicavel sem `FND-11`** — o candidato escreve link markdown vivo para `11-framework-specifications.md` | ✅ **O ato de 2026-07-30 promulgou os dois, e `FND-11` PRIMEIRO** — [MSG-2026-0007 §3](../../memory/operacional/MSG-2026-0007-ato-soberano-vigencia-do-framework-de-specifications.md). **`0` links quebrados** medidos apos a aplicacao; a variante `ALT` **nao entrou em vigor** | 2026-07-30 |
| FIT-2026-001 R2 | Grafo de estados reproduzido em FND-03 e FND-09 | [ADR-0008](../../decisions/ADR-0008-uma-fonte-multiplas-projecoes.md) §5.3 | 2026-07-28 |
| FIT-2026-002 R2 | Coluna Local da matriz FND-10 §10.3 repete FND-03 §7 | [ADR-0008](../../decisions/ADR-0008-uma-fonte-multiplas-projecoes.md) §5.3 | 2026-07-28 |
| **FIT-2026-003 R3** | Reducao de contexto medida uma unica vez, em missao atipica | **Terceira medicao observada** — 3 medicoes em 3 naturezas de missao: 23% · 33% · 30,6% ([REV-DEPARTAMENTO §5.2](../../foundation/revisao-arquitetural-cartas-de-departamento-2026-07-28.md)) | 2026-07-28 |
| **FIT-2026-004 R3** | 4a missao consecutiva de crescimento; nenhuma ressalva fechada; custo subiu | **A condicao de escalonamento nao ocorreu:** a terceira medicao **nao subiu** (33% → 30,6%) e este ciclo fecha duas ressalvas ([REV-DEPARTAMENTO §5.5](../../foundation/revisao-arquitetural-cartas-de-departamento-2026-07-28.md)) | 2026-07-28 |
| **FIT-2026-005 R2** | Contrato validado em **2 de 4 classes**; Comando e Plataforma sem piloto | **Quatro classes exercidas** em 8 cenarios interclasses; o impedimento de DEP-EXE foi **exercido** e mudou o aprovador desta missao ([REV-INTERCLASSES §8.2](../../foundation/revisao-arquitetural-validacao-interclasses-2026-07-28.md)) | 2026-07-28 |
| **FIT-2026-005 R4** | **Os dois pilotos nao estao em vigor**; o rollout esta bloqueado | **Ato soberano de 2026-07-28**, com condicao de eficacia verificada por tres vias independentes ([MSG-2026-0001](../../memory/operacional/MSG-2026-0001-ato-soberano-ratificacao-cartas-piloto.md)) | 2026-07-28 |
| **FIT-2026-001 R1** | Acrescimo do Meta Model sem proporcao comprovada | **Condicao literal nao se verifica:** FND-10 foi construido sobre o Meta Model — §4 mapeia os 33 tipos as 21 entidades por CS-01 ([REV-ESTRUTURAL-I §5.1](../../foundation/revisao-estrutural-01-2026-07-28.md)) | 2026-07-28 |
| **FIT-2026-001 R3** | Arquetipo A2 reune 19 de 21 e nunca discriminara | **A2 foi invocado em dois casos registrados:** recusa da entidade *"Artifact"* (FND-10 §3.3) e a exclusao de `ORG` e `SOBERANO` que corrigiu a contagem do catalogo (**RE-05**) | 2026-07-28 |
| **FIT-2026-002 R1** | 40 regras novas, nenhuma exercida | **Condicao literal nao se verifica:** cinco artefatos nascem sob o contrato so na Missao 1.8 | 2026-07-28 |
| **FIT-2026-002 R3** | Classe de mutabilidade M3 com um unico membro | **Um membro, uso decisivo:** a regra *"nunca editar a fonte para caber no indice"* decidiu **IC-8, RE-04 e RE-05** — tres correcoes na vista derivada, zero na fonte | 2026-07-28 |
| **FIT-2026-004 R1** | 28 regras `CT` sem exercicio | **13 de 28 exercidas — 46,4%**, acima do limiar de um terco. Medicao regra a regra em [REV-ESTRUTURAL-I §10.1](../../foundation/revisao-estrutural-01-2026-07-28.md) | 2026-07-28 |
| **FIT-2026-004 R4** | MEM-EST-0001 permanece `aprovado` | **Ato soberano de 2026-07-28** — `ativo` · `ratificada`, com as **11 lacunas `unknown` intactas** ([MSG-2026-0002 §2 e V9](../../memory/operacional/MSG-2026-0002-ato-soberano-cartas-comando-plataforma-e-contexto.md)) | 2026-07-28 |
| **FIT-2026-005 R5** | 1a revisao estrutural nao agendada em cinco ciclos | **Determinada pelo Soberano e executada** — [REV-ESTRUTURAL-I](../../foundation/revisao-estrutural-01-2026-07-28.md). **Doze** itens que dependiam dela foram destravados | 2026-07-28 |
| **FIT-2026-006 R2** | **5 de 9 departamentos sem Carta**, um deles DEP-GOV | **Cobertura 9/9 alcancada.** DEP-GOV foi a **quinta**, escrita sozinha, cumprindo a Condicao 1 ([departments/README](../../departments/README.md)) | 2026-07-28 |
| **FIT-2026-006 R4** | A Carta de DEP-QAR retem o defeito conhecido **IC-5** | **Ato soberano de 2026-07-28:** `DEP-QAR` **1.1.0** em vigor, IC-5 corrigido, `IR-09` reproduzindo `H-A` exatamente ([MSG-2026-0003](../../memory/operacional/MSG-2026-0003-ato-soberano-emenda-qar-e-criterio-de-consolidacao.md)) | 2026-07-28 |
| **FIT-2026-007 R2** | EV-08 encerrada sem objeto; gatilho e criterio mediam coisas diferentes | **PS-1 respondida pelo Soberano** e formalizada em [ADR-0013](../../decisions/ADR-0013-criterio-de-horizonte-e-consolidacao.md), `HZ-01` a `HZ-08`, **sem emendar nenhuma fundacional** | 2026-07-28 |
| **FIT-2026-007 R4** | **Q1 e Q2 abertas, dependendo de ato do Soberano; IC-2 contido por regra de redacao** | **Ato soberano de 2026-07-29:** Q1 **ratificada** *(ADR-0014 → FND-01 1.4.0, IC-2 fechado na fonte)* e Q2 **determinada** *(item 4 → [ADR-0015](../../decisions/ADR-0015-fitness-check-e-parecer-nao-decisao.md), `FT-10` a `FT-15`)*. **As duas questoes que a ressalva nomeava foram decididas** | 2026-07-29 |
| **FIT-2026-009 R1** | **Cobertura vigente 4/9 pelo segundo ciclo consecutivo** | **Ato soberano de 2026-07-29**, com `H-P` conferido contra valor projetado **antes** do ato e `IR-09` reproduzindo `H-A` em 5 de 5 ([MSG-2026-0004 §5](../../memory/operacional/MSG-2026-0004-ato-soberano-cartas-emenda-constitucional-e-regime-do-fitness-check.md)). **Cobertura vigente 9/9** | 2026-07-29 |

> **Sete ressalvas fecharam em um ciclo — mais que os seis ciclos anteriores somados.** O
> motivo nao e criterio mais frouxo: **seis das sete tinham como gatilho literal a 1a revisao
> estrutural**, que nunca havia ocorrido. Quando ela ocorreu, as condicoes puderam **enfim ser
> testadas** — e quatro delas **nao se verificaram**, o que fecha a ressalva pelo texto que ela
> propria escreveu. **Nenhuma fechou por reformulacao.**

## Quando e obrigatorio

| Situacao | Fitness Check |
|---|---|
| Mudanca **C3** | **Obrigatorio**, com ratificacao do Soberano |
| Mudanca **C2** | **Obrigatorio** |
| Trabalho que altere Fundacao, catalogo de Capabilities ou Meta Model | **Obrigatorio** |
| Revisao estrutural periodica | **Obrigatorio** |
| Mudanca **C1** | Opcional; recomendado em lote |
| Mudanca **C0** | Nao se aplica |

## As seis perguntas

| # | Pergunta |
|---|---|
| F1 | A complexidade aumentou sem ganho proporcional? |
| F2 | Algum conceito foi duplicado? **e** o teste preventivo foi aplicado, com evidencia? *(PJ-06)* |
| F3 | Alguma abstracao ficou desnecessaria? |
| F4 | O sistema continua mais simples de evoluir do que antes? |
| F5 | A mudanca reduz ou aumenta o custo de contexto? |
| F6 | Ela favorece reutilizacao? |

**Toda resposta exige sinal observavel.** Resposta sem sinal e opiniao e a verificacao e
devolvida sem analise de merito (FT-03, DoD-5).

## Regras rapidas

| # | Regra |
|---|---|
| 1 | Nao substitui o Architecture Review. Em C2 e C3, **ambos** sao obrigatorios (FT-01). |
| 2 | Executor ≠ produtor. Acumulo torna o veredito **nulo** (FT-02, LV-03). |
| 3 | Ressalva sem dono e sem gatilho e invalida: converte o veredito em `inapto` (FT-06). |
| 4 | `inapto` **bloqueia o encerramento**; a mudanca volta a etapa [2] de FND-04 §4 (FT-05). |
| 5 | Tres `apto` consecutivos sem uma unica ressalva escalam ao Soberano (FT-04). |
| 6 | `FIT` e permanente: nunca reescrito. Veredito posterior **supera** o anterior (FT-09). |

Template: [`TPL-fitness-check`](../../foundation/templates/TPL-fitness-check.md) ·
Portao: **QG-6** (FND-01 §6.2)
