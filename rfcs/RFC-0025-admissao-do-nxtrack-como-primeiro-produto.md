---
id: RFC-0025-admissao-do-nxtrack-como-primeiro-produto
titulo: O nXtrack deve ser admitido agora pelo portao de origem externa, com G0 IDENTIDADE, e tornar-se o primeiro Produto do acervo?
tipo: rfc
versao: 1.0.0
status: aprovado
camada_memoria: estrategica
autor: DEP-PRD
proprietario: DEP-PRD
aprovador: DEP-GOV
criado_em: 2026-08-01
atualizado_em: 2026-08-01
revisao_prevista: 2027-02-01
decisoes_relacionadas: [ADR-0007, ADR-0027, ADR-0002, ADR-0021]
substitui: []
substituido_por: null
classe_mudanca: C2
prazo_analise: 2026-09-01
resumo: Submete a admissao do nXtrack pelo portao de origem externa com G0 IDENTIDADE e G3 RECOGNIZE, criando o primeiro Produto do acervo por ato do Soberano.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# RFC-0025: admissao do nXtrack como primeiro Produto

## Proposito

Submeter a decisao de **admitir a existencia formal do nXtrack** neste acervo, pelo portao de
origem externa de [ADR-0007 §5.3](../decisions/ADR-0007-fronteira-greenfield-legado.md), com a
condicao `G0` e a classificacao de [ADR-0027](../decisions/ADR-0027-classe-de-admissao-de-existencia-no-portao-de-origem-externa.md),
**em vigor desde 2026-07-31**.

## Escopo

| Item | Definicao |
|---|---|
| **Inclui** | A **identidade** do nXtrack como entidade `PRO` deste acervo · a Carta `PRO-nxtrack` · a custodia, as interfaces e os limites declarados · a entrada de `legacy-candidate` no catalogo |
| **Nao inclui** | **Qualquer byte de codigo, schema, dado ou texto do candidato** · a criacao de `Spec` · o fechamento de `RD-33` · a decisao sobre `E2` · a alteracao do repositorio do candidato · o merito tecnico do produto |
| **Subordinado a** | [FND-01](../foundation/01-constituicao.md) · [FND-04](../foundation/04-governanca.md) · [FND-08](../foundation/08-capability-framework.md) · [FND-09](../foundation/09-meta-model.md) · [ADR-0007](../decisions/ADR-0007-fronteira-greenfield-legado.md) · [ADR-0027](../decisions/ADR-0027-classe-de-admissao-de-existencia-no-portao-de-origem-externa.md) |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| Proponente | **DEP-PRD** | Custodio de `CAP-produto`; `FND-04 §6`, linha **Produto** |
| Confere o portao | **DEP-GOV** | `ADR-0007 §5.3`, `G2`; sem julgar merito (`FND-04 §12`) |
| Revisor independente | **DEP-QAR** | `AC-03`; `ADR-0007 §5.3`, `G4` |
| Aprovador da `RFC` | **DEP-GOV** | `FND-04 §2`, `C2` |
| Decide a admissao | **SOBERANO** | `FND-04 §6`, linha **Produto**: `C2`/`Tipo 1` |

---

## 1. O que existe hoje, medido

| Fato | Valor | Como se sabe |
|---|---|---|
| Produtos no acervo | **`0`** | `products/` **nao existe**; `0` arquivos com `id: PRO-` fora do template |
| `Spec`s instanciadas | **`0`** | unica ocorrencia de `tipo: spec` e `TPL-spec.md` |
| Candidatos nomeados pelo portao | **`1`** — `medAlly` | catalogo `§9` |
| Admissoes concluidas pelo portao | **`0`** | `ADR-0026` esta **`em-revisao`**, nao vigente |
| Instrumento de Carta de Produto | **existe** — `TPL-carta-produto` **1.1.0**, `ativo` | `foundation/templates/` |
| Classe `RECOGNIZE` disponivel | **sim, desde 2026-07-31** | `ADR-0027` `status: ativo`, §5.2 |
| `Q1` | **RESPONDIDA** | `PT-2026-009 §1`, decisao **7** |

> **`Q1` nao e reaberta por esta `RFC`.** O Soberano fixou, em texto literal: *"Via futura e
> `S1` com Produto real (`nXtrack`); `S2` deferida"* — [PT-2026-009 §1, decisao 7](../governance/relatorio-transicao-2026-07-30-convergencia.md).
> A oracao *"se seguir sendo o primeiro produto comercial"* **nao esta nesse documento**: ela
> mora em [PS-2026-013 §7](../governance/pacote-soberano-2026-07-30-consolidado.md), artefato
> **distinto**. A palavra `comercial` tem **`0`** ocorrencias no arquivo de `PT-2026-009` —
> **medido**. Tratar os dois como um so **produziu a ambiguidade** que travou a questao; o
> achado e `RD-64`. Esta `RFC` os trata como **dois documentos**, e a ressalva vira `Q2` do
> pacote soberano — **pergunta ao Soberano, nao pressuposto do proponente**.

## 2. A pergunta de decisao

**O nXtrack deve ser admitido agora, com `G0 = IDENTIDADE`, tornando-se o primeiro Produto do
acervo — ou a admissao deve esperar?**

Nao se pergunta se o nXtrack e bom. Pergunta-se se a **existencia formal** dele deve nascer
agora, e sob que forma.

## 3. Criterios de decisao

> Declarados **antes** do exame das alternativas (`CD-01`, `VD-02`).

| # | Criterio | Peso | Como se mede |
|---|---|---|---|
| `K1` | **Nenhum byte do candidato entra no acervo sem portao proprio** | **Bloqueante** | Arquivos do candidato copiados = `0` |
| `K2` | **Nenhuma afirmacao da admissao nasce falsa** | **Bloqueante** | Toda classificacao tem fundamento citado; nenhuma por eliminacao |
| `K3` | **A custodia do candidato e declarada como e, nao como se gostaria** | **Bloqueante** | O registro diz que o produto vive em subarvore de terceiro |
| `K4` | Nao cria entidade nem tipo documental novo | Alto | Universo permanece em 21 entidades e 33 tipos |
| `K5` | Reversivel a custo medido | Alto | Custo de reversao enumerado objeto a objeto |
| `K6` | Nao antecipa `Spec` nem fecha `RD-33` | **Bloqueante** | `0` `Spec` criada; `RD-33` segue aberto |

## 4. Alternativas consideradas

### Alternativa A — Admitir **agora**, com `G0 = IDENTIDADE` e `G3 = RECOGNIZE`

| Campo | Conteudo |
|---|---|
| Descricao | `ADR` de admissao + Carta `PRO-nxtrack` escrita **neste sistema, do zero**, com `0` bytes do candidato. O codigo permanece no repositorio operacional. Ato do Soberano cria a identidade |
| A favor | Satisfaz `K1`–`K6`. Executa a decisao **7** de `PT-2026-009` sem inventar nada. Desbloqueia o caminho de `RD-33` **sem fecha-lo**. Usa a classe que `ADR-0027` criou **exatamente para este caso** |
| Contra | Cria Produto cuja custodia real esta fora do acervo — assimetria declarada, nao resolvida |
| Custo | 1 `RFC` + 1 `ADR` + 1 `FIT` + 1 Carta candidata + 1 pacote + entradas de catalogo e indices |
| Risco | O Soberano entender que a ressalva *"primeiro produto comercial"* de `PS-2026-013 §7` condiciona o ato |
| Avaliacao | `K1` ✔ · `K2` ✔ · `K3` ✔ · `K4` ✔ · `K5` ✔ · `K6` ✔ |

### Alternativa B — Admitir com `G0 = AMBOS`, trazendo tambem a `spec-tecnica-v1` do candidato

| Campo | Conteudo |
|---|---|
| Descricao | Alem da identidade, admitir como artefato do acervo a especificacao tecnica do candidato, por `ADOPT` ou `ADAPT` |
| A favor | O acervo ganharia de imediato uma descricao tecnica rica, ja escrita |
| Contra | **Falha em `K1`.** Traria **958 linhas** de conteudo externo produzido sob outra norma, com arquitetura recomendada (`PostgreSQL`, `Neo4j`, `Redis`, `Tauri`) que **contradiz o que o proprio candidato implementou** (`SQLite`, React+FastAPI). Admitir isso como artefato seria **normatizar um plano que o produto ja abandonou**. Falha tambem em `K2`: `ADOPT` afirmaria *"serve como esta"*, e nao serve |
| Custo | Alto, e recorrente: cada divergencia futura entre o texto admitido e o produto vivo vira emenda |
| Risco | Alto — o acervo passa a carregar arquitetura que ninguem construiu |
| Avaliacao | `K1` **falha** · `K2` **falha** · `K3` ✔ · `K4` ✔ · `K5` **falha** · `K6` ✔ |

### Alternativa C — Adiar a admissao ate a ressalva comercial estar resolvida

| Campo | Conteudo |
|---|---|
| Descricao | Nao admitir enquanto o Soberano nao declarar se o nXtrack *"segue sendo o primeiro produto comercial"* (`PS-2026-013 §7`) |
| A favor | Nao arrisca admitir um Produto que a ressalva excluiria |
| Contra | **Falha em `K6` por inversao, e e o ponto mais delicado desta `RFC`.** A ressalva esta em documento **distinto** da decisao, e a decisao **7** de `PT-2026-009` **nao a contem**. Adiar por causa dela e **repetir o erro de `RD-64`**: tratar dois documentos como um. Alem disso, o adiamento **nao tem gatilho**: nada no acervo diz quando "seguir sendo comercial" se verifica — e criterio sem sinal observavel e adiamento indefinido |
| Custo | `0` hoje; **o custo aparece inteiro** quando `RD-33`, congelado, tornar a primeira `Spec` impossivel |
| Risco | O congelamento declarado pelo Fundador *(nenhuma missao de governanca nova ate existir a primeira `Spec`)* **nunca destrava**, porque a `Spec` exige Produto e o Produto espera a ressalva |
| Avaliacao | `K1` ✔ · `K2` ✔ · `K3` ✔ · `K4` ✔ · `K5` ✔ · `K6` **falha** |

### Alternativa Z — Nao fazer nada

| Campo | Conteudo |
|---|---|
| O que acontece | O portao segue exercido **uma vez** e **nunca concluido**. `0` Produtos, `0` `Spec`s, `RD-33` bloqueante, `Q1` respondida e nao executada |
| Custo real da inacao | A decisao **7** do Soberano permanece **registrada e nao executada** — estado que `PT-2026-009` ja descreve com essas palavras. Cada missao seguinte recomeca a discussao |
| Por que nao venceu | O trabalho de admissao **ja esta feito e medido**; nao executa-lo nao poupa custo, apenas adia o registro do que ja se sabe |

## 5. Recomendacao

**Alternativa A.** Unica que satisfaz os tres bloqueantes e nao inverte `K6`.

**Por que `B` e o risco maior, nao o menor.** Trazer a especificacao tecnica pareceria ganho de
conteudo, e seria divida: o documento descreve `PostgreSQL`, `Neo4j`, `Redis` e `Tauri`, e o
produto real roda `SQLite`, React e FastAPI. **O acervo passaria a normatizar uma arquitetura
que o proprio candidato nao seguiu** — e corrigir isso depois custaria emenda a cada divergencia.

**Por que `C` merece a analise mais longa.** É a alternativa **defensavel**, e por isso
nenhuma linha dela e de palha. Ela perde por dois motivos medidos: *(i)* a ressalva nao esta na
decisao — esta em outro documento, e confundi-los e o achado `RD-64`; *(ii)* ela nao tem
gatilho observavel. **A resposta correta a ressalva nao e adiar: e perguntar.** Por isso ela
entra como **`Q2`** do pacote soberano, e o ato pode ser assinado com ou sem ela.

**Tradeoff aceito:** o acervo passa a ter um Produto cuja **custodia real esta fora dele**. O
custo e conhecido e esta escrito — achado `RD-71` —, e a alternativa era nao ter Produto algum.

## 6. Impacto levantado

| Dimensao | Impacto |
|---|---|
| Entidades novas | **`0`** — `PRO` ja e `E-17` do Meta Model |
| Tipos documentais novos | **`0`** |
| Fundacionais emendados | **`0`** |
| Artefatos historicos editados | **`0`** |
| Bytes do candidato admitidos | **`0`** — por definicao de `RECOGNIZE` (`ADR-0027 §5.2`) |
| Capabilities vinculadas | **5** — `VC-03` **dispara e esta declarado** (achado `RD-74`) |
| Documentos a atualizar | Catalogo `§2`, `§4`, `§7`, `§9`, `§10` · indices `M3` · `README` da raiz |
| Custo de reversao | Medido objeto a objeto em `ADR-0030 §10` |

## 7. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Decisao que originou | [PT-2026-009 §1](../governance/relatorio-transicao-2026-07-30-convergencia.md), decisao **7** |
| Portao aplicado | [PT-2026-014 §3](../governance/relatorio-transicao-2026-08-01-portao-nxtrack.md) |
| Decisao resultante | [ADR-0030](../decisions/ADR-0030-admissao-do-nxtrack-como-primeiro-produto.md) |
| Verificacao de aptidao | [FIT-2026-023](../governance/fitness/FIT-2026-023-admissao-do-nxtrack.md) |
| Pacote soberano | [PS-2026-016](../governance/pacote-soberano-2026-08-01-nxtrack.md) |
| Achados abertos por esta `RFC` | `RD-71` · `RD-72` · `RD-73` · `RD-74` — **registrados com dono e gatilho, sem missao** |
| Achado que esta `RFC` invoca | `RD-64` — atribuicao da citacao de `Q1` ao documento errado |

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-08-01 | DEP-PRD | Proposta inicial. Submete a admissao do nXtrack com `G0 = IDENTIDADE` e `G3 = RECOGNIZE`, com **quatro** alternativas reais — `B` *(admitir conteudo)* e `C` *(adiar pela ressalva comercial)* analisadas como respostas defensaveis ao mesmo problema. Registra que `PT-2026-009` e `PS-2026-013` sao **documentos distintos**, e que a ressalva comercial vira `Q2` do pacote em vez de bloqueio silencioso. |
