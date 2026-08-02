---
id: IDX-rfcs
titulo: Indice Oficial de Propostas (RFC)
tipo: relatorio
versao: 1.6.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-GOV
criado_em: 2026-07-28
atualizado_em: 2026-07-31
revisao_prevista: null
decisoes_relacionadas: [ADR-0001, ADR-0003, ADR-0004, ADR-0006, ADR-0007, ADR-0011]
substitui: []
substituido_por: null
resumo: Conta a sequencia oficial RFC e registra o resultado de cada proposta submetida.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# Indice Oficial de Propostas

## Proposito
Manter o registro unico e o contador oficial da sequencia `RFC-NNNN`, conforme
[FND-03 §2.3](../foundation/03-taxonomia.md).

## Escopo
Propostas em analise, aceitas, rejeitadas ou adiadas. Decisoes ja tomadas ficam em
[`../decisions/`](../decisions/).

## Responsaveis
| Papel | Responsavel |
|---|---|
| Proprietario e numerador oficial | DEP-GOV |
| Analise de risco | DEP-QAR |
| Arbitragem de merito | DEP-EXE |

---

## Contador oficial

| Campo | Valor |
|---|---|
| Ultimo numero atribuido | **0027** |
| Proximo numero disponivel | **0028** |
| **⚠️ `RD-95` — este contador estava DEFASADO EM UM, e o defeito foi encontrado EXERCENDO-O (Missao 1.13.5)** | Ele declarava **`0025` disponivel** enquanto **`RFC-0025` ja existia** desde 2026-08-01 *(Missao 1.13.4.5)*. O numero `0026` foi atribuido **por teste de existencia contra a copia datada** *(`_backups/…_2026-08-01_pre-missao-1-13-5/`)* — `RFC-0024` ✅ existe · `RFC-0025` ✅ existe · **`RFC-0026` NAO existe** —, e so depois o contador foi corrigido de **`0025` para `0027`**. **Mesma causa e mesma emissao do defeito gemeo em [`decisions/README`](../decisions/README.md)**: `CV-04` e `IX-02`. **Quarta ocorrencia da familia de `RD-32`**; metodo `V1` de [MEM-APR-0006](../memory/aprendizado/MEM-APR-0006-exercer-o-contador-revela-o-defeito.md) |
| **Contador exercido, nao lido (Missao 1.13.4.2)** | Antes de atribuir **`0022`, `0023` e `0024`**, testou-se a existencia de `RFC-002[234]-*.md` contra a **copia datada anterior as edicoes** *(`_backups/…_2026-07-31_pre-missao-1-13-4-2/`)*: **nenhum dos tres existia**, e a contagem foi de **21 → 24** — `V1` de [MEM-APR-0006](../memory/aprendizado/MEM-APR-0006-exercer-o-contador-revela-o-defeito.md) |
| **Contador exercido, nao lido** | Antes de atribuir **`0021`**, testou-se a existencia de `RFC-0021-*.md` contra a **copia datada anterior as edicoes** *(`_backups/…_2026-07-31_pre-missao-1-13-4/`)*: **nao existia**, e a contagem foi de **20 → 21**. Antes de atribuir **`0020`**, testou-se a existencia de `RFC-0020-*.md` contra a **copia datada anterior as edicoes**: **nao existia**, e a contagem foi de **19 → 20**. Antes de atribuir **`0018`** e **`0019`**, testou-se a existencia de arquivo com esses nomes: **nenhum existia** — `V1` de [MEM-APR-0006](../memory/aprendizado/MEM-APR-0006-exercer-o-contador-revela-o-defeito.md) |
| **Correcao de `RD-32`** | Este contador declarava **`0015` / `0016`** enquanto a tabela abaixo ja listava **`RFC-0016`** — defasagem de **um**. Causa: `CV-04`, codificada em **`SF-32`** de [ADR-0021](../decisions/ADR-0021-framework-de-specifications.md); metodo em [MEM-APR-0006](../memory/aprendizado/MEM-APR-0006-exercer-o-contador-revela-o-defeito.md) `V1` |

## Propostas

| ID | Titulo | Classe | Status | Prazo de analise | Resultado |
|---|---|---|---|---|---|
| [RFC-0001](RFC-0001-camada-de-capabilities.md) | Camada de Capabilities | C3 | `aprovado` | 2026-07-28 | **Aceita** → [ADR-0002](../decisions/ADR-0002-adocao-da-camada-de-capabilities.md) |
| [RFC-0002](RFC-0002-enterprise-meta-model.md) | Enterprise Meta Model | C3 | `aprovado` | 2026-07-28 | **Aceita** → [ADR-0003](../decisions/ADR-0003-adocao-do-enterprise-meta-model.md) |
| [RFC-0003](RFC-0003-architecture-fitness-check.md) | Architecture Fitness Check | C3 | `aprovado` | 2026-07-28 | **Aceita** → [ADR-0004](../decisions/ADR-0004-adocao-do-architecture-fitness-check.md) |
| [RFC-0004](RFC-0004-enterprise-artifact-framework.md) | Enterprise Artifact Framework | C3 | `aprovado` | 2026-07-28 | **Aceita** → [ADR-0006](../decisions/ADR-0006-adocao-do-enterprise-artifact-framework.md) |
| [RFC-0005](RFC-0005-fronteira-greenfield-legado.md) | Fronteira greenfield / legado | **C2** | `aprovado` | 2026-07-28 | **Aceita** → [ADR-0007](../decisions/ADR-0007-fronteira-greenfield-legado.md) |
| [RFC-0006](RFC-0006-contrato-de-artefato-o-que-e-emenda.md) | O que conta como "emendado" no contrato de artefato | **C2** | `aprovado` | 2026-07-28 | **Aceita** → [ADR-0009](../decisions/ADR-0009-o-que-conta-como-emenda-de-artefato.md) |
| [RFC-0007](RFC-0007-conhecimento-sobre-o-soberano.md) | Conhecimento operacional sobre o Soberano | **C2** | `aprovado` | 2026-07-28 | **Aceita** → [ADR-0010](../decisions/ADR-0010-contrato-de-conhecimento-do-soberano.md) |
| [RFC-0008](RFC-0008-contrato-de-carta-de-departamento.md) | Contrato de Carta de Departamento | **C2** | `aprovado` | 2026-07-28 | **Aceita com ajuste** → [ADR-0011](../decisions/ADR-0011-contrato-de-carta-de-departamento.md) |
| [**RFC-0009**](RFC-0009-integridade-e-alcance-do-ato-de-ratificacao.md) | Integridade e alcance do ato de ratificacao | **C2** | `aprovado` | 2026-07-28 | **Aceita em parte** → [ADR-0012](../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md). **Q1 e Q2 permanecem abertas e escaladas ao SOBERANO** |
| [**RFC-0010**](RFC-0010-criterio-de-horizonte-avaliavel.md) | Por qual instrumento se formaliza o criterio de horizonte avaliavel | **C2** | `aprovado` | 2026-07-28 | **Aceita** → [ADR-0013](../decisions/ADR-0013-criterio-de-horizonte-e-consolidacao.md). **Q5 e Q6 abertas, nao escaladas** |
| [**RFC-0011**](RFC-0011-emenda-constitucional-ratifica-homologa.md) | Separar **ratificacao** de **homologacao** em FND-01 §7.3, e harmonizar FND-10 §10.3 quanto a `FIT` | **C3** + C2 | `aprovado` *(forma)* | 2026-07-28 | **Aceita** → [ADR-0014](../decisions/ADR-0014-candidato-emenda-fnd-01-7-3-homologa.md), **ratificado** em 2026-07-29; **FND-01 1.4.0 promulgada** |
| [**RFC-0012**](RFC-0012-semantica-da-matriz-de-interacao.md) | **Semantica da matriz de FND-02 §4 e alcance do veto da Guarda** — fecha **RD-02** | **C3** | `aprovado` *(forma)* | 2026-07-29 | **Aberta — escalada ao SOBERANO.** [ADR-0016](../decisions/ADR-0016-semantica-da-matriz-de-interacao.md) candidato **sem vigencia**; [PS-2026-004](../governance/pacote-soberano-2026-07-29-rd-02.md) |
| [**RFC-0013**](RFC-0013-harmonizacao-do-regime-do-parecer.md) | **Harmonizar FND-09 §8.2 e FND-10 §10.3 ao regime do parecer (`FT-10`)** — fecha **RD-09** | **C3** | `aprovado` *(forma)* | 2026-07-29 | **Aberta — escalada ao SOBERANO.** [ADR-0017](../decisions/ADR-0017-harmonizacao-do-regime-do-parecer.md) candidato **sem vigencia**; [PS-2026-005](../governance/pacote-soberano-2026-07-29-rd-09.md) |
| [**RFC-0014**](RFC-0014-liberacao-do-portao-qg-1.md) | **Quem libera o portao `QG-1`** — resolver a colisao interna de FND-01 §6.2 — fecha **RD-14** | **C3** | `aprovado` *(forma)* | 2026-07-29 | **Aberta — escalada ao SOBERANO.** [ADR-0018](../decisions/ADR-0018-liberacao-do-portao-qg-1.md) candidato **sem vigencia**; [PS-2026-007](../governance/pacote-soberano-2026-07-29-rd-14.md) |
| [**RFC-0015**](RFC-0015-aprovador-e-ratificador-de-spec.md) | **Aprovador e ratificador de `Spec`** — harmonizar FND-09 §8.2 e FND-10 §10.3 com FND-04 §2 e §6 — fecha **RD-15** | **C3** | `aprovado` *(forma)* | 2026-07-29 | **Aberta — escalada ao SOBERANO.** [ADR-0019](../decisions/ADR-0019-aprovador-e-ratificador-de-spec.md) candidato **sem vigencia**; [PS-2026-008](../governance/pacote-soberano-2026-07-29-rd-15.md). Abre **RD-18** e **RD-19** |
| [**RFC-0016**](RFC-0016-regime-ministerial-de-promulgacao-e-ativacao.md) | **Regime ministerial de promulgacao e ativacao** — titular declarado, nao criado — fecha **RD-22** | **C2** | `aprovado` *(forma)* | 2026-07-29 | ✅ **ACOLHIDA** → [ADR-0020](../decisions/ADR-0020-regime-ministerial-de-promulgacao-e-ativacao.md). Inventaria **20 declaracoes em 5 fontes vigentes** e demonstra que **`AU-09` nao alcanca** os dois atos, porque `FND-09 §8.1` fecha os verbos de autoridade em **cinco** |
| [**RFC-0020**](RFC-0020-conformidade-de-contrato-das-fundacionais.md) | **Como fechar `RD-27` sem reescrever norma** — o backfill de `AC-08` em `FND-01` e `FND-02` e a correcao de `FND-10 §8.5` | **C3** | `aprovado` *(forma)* | 2026-07-30 | Convertida em [ADR-0024](../decisions/ADR-0024-conformidade-de-contrato-das-fundacionais.md). **Mede que `§8.5` tem cinco valores defasados onde `RD-27` contara tres** — achado `RD-46` |
| [**RFC-0021**](RFC-0021-admissao-do-medally-como-primeiro-produto.md) | **Qual produto exerce `S1`** — medAlly agora, nXtrack primeiro, ou adiar | **C2** | `aprovado` *(forma)* | 2026-07-31 | Convertida em [ADR-0026](../decisions/ADR-0026-admissao-do-medally-como-primeiro-produto.md). **Tres opcoes reais mais `Z`**, recomendacao declarada, e a **escolha entre `L1` e `L2` da decisao 7 submetida ao Soberano** — `Q1`, **bloqueante**. Registra a **ausencia de manifestacao de DEP-EXE** |
| [**RFC-0022**](RFC-0022-classe-de-admissao-de-existencia-no-portao-de-origem-externa.md) | **O portao de `ADR-0007` deve distinguir IDENTIDADE de CONTEUDO** e ganhar a classe que falta em `G3` | **C2** | `aprovado` *(forma)* | 2026-07-31 | Convertida em [ADR-0027](../decisions/ADR-0027-classe-de-admissao-de-existencia-no-portao-de-origem-externa.md). **Tres alternativas reais mais `Z`**. Corrige a fonte: a quarta classe e **`RETIRE`**, nao `REJECT` |
| [**RFC-0023**](RFC-0023-independencia-de-verificacao-por-fornecedor.md) | **Independencia da verificacao deve ser aferida por divergencia de campo ou por fornecedor?** | **C3** | `aprovado` *(forma)* | 2026-07-31 | Convertida em [ADR-0028](../decisions/ADR-0028-independencia-de-verificacao-por-fornecedor.md). **A diferenca medida: `0` contra `131`, base `138`**. Corrige a fonte: **`ADR-0005` nao contem criterio de afericao** |
| [**RFC-0024**](RFC-0024-superacao-de-ato-por-evidencia-posterior.md) | **Deve existir caminho para superar ato ja emitido quando a prova o contradiz?** | **C3** | `aprovado` *(forma)* | 2026-07-31 | Convertida em [ADR-0029](../decisions/ADR-0029-superacao-de-ato-por-evidencia-posterior.md). **Quatro alternativas reais mais `Z`**. Lacuna medida: **`0`** caminhos em norma vigente |
| [**RFC-0025**](RFC-0025-admissao-do-nxtrack-como-primeiro-produto.md) | **O nXtrack deve ser admitido agora, com `G0` = `IDENTIDADE`, e tornar-se o primeiro Produto?** | **C2** | **`aprovado`** | 2026-08-01 | ✅ **APROVADA pelo nono ato soberano** ([MSG-2026-0009](../memory/operacional/MSG-2026-0009-ato-soberano-admissao-do-nxtrack.md) item **II**), aplicado pela Missao 1.13.4.5. **O ciclo de `RFC` termina em `aprovado`**, e a transicao foi feita pela **variante** de `PS-2026-016 §2.1` — o instrumento padrao poria `ativo`, que **nao** e a transicao do ato; `H-P` conferido `eecde504…a7b63`, `H-N` invariante. Convertida em [ADR-0030](../decisions/ADR-0030-admissao-do-nxtrack-como-primeiro-produto.md), **`ativo` · `ratificada`**. **Tres alternativas reais mais `Z`** — `B` *(admitir tambem conteudo)* e `C` *(adiar pela ressalva comercial)*. Registra que **`PT-2026-009` e `PS-2026-013` sao documentos distintos** (`RD-64`): `comercial` tem **`0`** ocorrencias no primeiro. Abre `RD-71` a `RD-75` |
| [**RFC-0026**](RFC-0026-primeira-spec-governanca-de-dado-pessoal-do-nxtrack.md) | **Em que recorte e sob que classe se cria a primeira `Spec` sobre `LM-6(a)`?** | **C2** | **`aprovado`** | 2026-08-02 | ✅ **ACEITA** — Opcao **A**. Convertida em [ADR-0031](../decisions/ADR-0031-primeira-spec-governanca-de-dado-pessoal-do-nxtrack.md). **Tres opcoes reais mais `Z`**: `B` *(o piso `C1` literal — reprovada por produzir **aprovacao nula**)* e `C` *(politica organizacional — reprovada por `RD-88`, a categoria nao existe e `S2` esta deferida)*. `CR-1` a `CR-6` declarados **antes** das opcoes. Registra a manifestacao das **quatro** areas, com a ressalva de DEP-QAR sobre a **propria** concentracao de papeis *(`RD-92`)* |
| [**RFC-0027**](RFC-0027-separacao-de-proponente-e-aprovador-na-spec-c1.md) | **Onde se emenda para separar proponente de aprovador na `Spec` `C1`, e ate onde?** — trata **`RD-91`** | **C3** | **`aprovado`** | 2026-08-02 | ✅ **ACEITA** — Opcao **B** *(emendar a fonte, com cascata)*. Convertida em [ADR-0032](../decisions/ADR-0032-separacao-de-proponente-e-aprovador-na-spec-c1.md). **A Opcao `A` — emendar so a celula que o achado nomeava — caiu por MEDICAO:** ela reproduz literalmente duas fontes, e `PJ-03` faria a fonte prevalecer |
| [**RFC-0019**](RFC-0019-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md) | **Como propagar `ADR-0018` e `ADR-0019` as Cartas** sem decidir nada de novo — trata **`RD-31`** | **C2** | `aprovado` *(forma)* | 2026-07-29 | ✅ **ACOLHIDA** → [ADR-0023](../decisions/ADR-0023-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md). **Primeira RFC do acervo cujo autor e `DEP-EXE`.** Mediu as **nove** Cartas e encontrou **3 afirmacoes falsas a mais em 3 Cartas nunca enumeradas** — abre **`RD-37`** e **`RD-41`** |
| [**RFC-0018**](RFC-0018-sede-canonica-do-framework-de-specifications.md) | **Onde deve viver, em definitivo, a norma da `Spec`** — a sede canonica do Framework de Specifications | **C3** | `aprovado` *(forma)* | 2026-07-29 | ✅ **ACOLHIDA** → [ADR-0022](../decisions/ADR-0022-sede-canonica-do-framework-de-specifications.md). **Quatro opcoes e a opcao Z**, com a **unica alteracao de merito submetida em separado**. Abre **`RD-38`** e **`RD-39`**; escala **3** perguntas ao Soberano |
| [**RFC-0017**](RFC-0017-framework-de-specifications.md) | **Framework de Specifications** — onde vive a norma da `Spec`, e por que os pilotos nao podem existir hoje — fecha **RD-23** | **C2** | `aprovado` *(forma)* | 2026-07-29 | ✅ **ACOLHIDA** → [ADR-0021](../decisions/ADR-0021-framework-de-specifications.md). **Primeira RFC do acervo cujo autor nao e `DEP-GOV`** *(`RC-02`)*. Mede **5** defeitos em `TPL-spec` onde `RD-23` declarava **2**, e submete que a `Spec` esta vinculada a `Produto` em **3** fontes vigentes, com **`0`** produtos existentes. Abre **`RD-31`** a **`RD-35`**; registra a Opcao **E** como achado, nao como recusa |

> **RFC-0009 e a primeira proposta do sistema aceita *em parte*.** Duas perguntas — **Q1**,
> emenda C3 a FND-01 §7.3, e **Q2**, se `FIT` exige ratificacao — **nao foram decididas** e
> continuam vivas na propria RFC, com dono **DEP-GOV**. Uma RFC aceita em parte **nao fecha as
> perguntas que nao decidiu**; registrar isso e o que impede que a divida pareca resolvida.

## Quando usar RFC

| Situacao | RFC? |
|---|---|
| Mudanca C3 (constitucional) | **Obrigatoria** |
| Criar tipo de entidade novo (FND-09 §11.1) | **Obrigatoria** — e sempre C3 |
| Mudanca C2 (estrutural) | Regra — dispensavel apenas se a alternativa unica for obvia **e** DEP-GOV concordar por escrito |
| Divergencia real entre alternativas | Sim |
| O problema ainda nao esta bem formulado | Sim |
| Decisao ja tomada | Nao — use ADR |
| Escolha local reversivel | Nao — use Nota de Decisao |

## Regras

| # | Regra |
|---|---|
| 1 | RFC **pode ser rejeitada**. Isso e resultado valido, nao fracasso. |
| 2 | RFC rejeitada vai para `arquivado` e **nunca e apagada** — saber o que foi recusado e por que tem valor proprio. |
| 3 | RFC sem alternativas analisadas e devolvida por DEP-GOV sem analise de merito. |
| 4 | RFC sem recomendacao do proponente e devolvida (EC-03). |
| 5 | RFC aceita gera ADR pelo rito de FND-07 §5. O numero da RFC fica registrado na origem do ADR. |

Template: [`TPL-rfc`](../foundation/templates/TPL-rfc.md)
