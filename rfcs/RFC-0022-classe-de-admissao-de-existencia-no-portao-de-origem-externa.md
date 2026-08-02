---
id: RFC-0022-classe-de-admissao-de-existencia-no-portao-de-origem-externa
titulo: O portao de ADR-0007 deve distinguir admitir IDENTIDADE de admitir CONTEUDO, e ganhar a classe que hoje falta em G3?
tipo: rfc
versao: 1.0.0
status: aprovado
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-GOV
criado_em: 2026-07-31
atualizado_em: 2026-07-31
revisao_prevista: 2027-01-31
decisoes_relacionadas: [ADR-0007, ADR-0009, ADR-0010]
substitui: []
substituido_por: null
classe_mudanca: C2
prazo_analise: 2026-08-31
resumo: Submete a decisao de acrescentar a condicao G0 e a classificacao RECOGNIZE ao portao de origem externa, fechando as duas lacunas que o primeiro exercicio real do portao revelou.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# RFC-0022: a classe que falta no portao de origem externa

## Proposito

Submeter a decisao de emendar o portao de admissao de origem externa de
[`ADR-0007 §5.3`](../decisions/ADR-0007-fronteira-greenfield-legado.md) para que ele distinga
**admitir a existencia** de algo externo de **admitir o conteudo** dele, e para que exista uma
classificacao que descreva a primeira coisa.

## Escopo

| Item | Definicao |
|---|---|
| **Inclui** | A condicao `G0` *(objeto da admissao)* · a classificacao `RECOGNIZE` · a regra de reclassificacao do registro que a Missao 1.13.4 gravou |
| **Nao inclui** | O merito de candidato algum · a admissao do medAlly · a criacao de Produto ou `Spec` · qualquer alteracao a `G1`, `G2`, `G4` ou `G5` |
| **Subordinado a** | [FND-04 §2](../foundation/04-governanca.md) · [FND-07](../foundation/07-framework-decisoes.md) |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| Proponente | **DEP-GOV** | Proprietario de `ADR-0007` |
| Revisor | **DEP-QAR** | `FND-09 §8.2`, linha `RFC` — areas afetadas; `AC-03` |
| Valida a forma | **DEP-GOV** | `FND-09 §8.2`, linha `RFC` |

---

## 1. O defeito, medido — nao opinado

O portao de `ADR-0007 §5.3` foi **exercido pela primeira vez** na Missao 1.13.4, sobre **um**
candidato nomeado. O exercicio produziu duas lacunas que nenhuma leitura teria revelado, e as
duas estao registradas no catalogo:

| Achado | Enunciado | Onde nasceu |
|---|---|---|
| **`RD-54`** | As cinco condicoes sao escritas para *"conteudo externo"*. Admitir a **existencia** de um produto e admitir os **arquivos** dele sao atos diferentes, e **nenhuma das cinco condicoes nomeia a diferenca** | [PT-2026-011 §3.1](../governance/relatorio-transicao-2026-07-31-admissao-medally.md), item 1 |
| **`RD-55`** | As quatro classificacoes de `G3` descrevem **destino de conteudo**. Nenhuma descreve *"admitir a existencia sem admitir nada"*. **`REWRITE` foi escolhida por eliminacao**, e a sua definicao — *"a solucao do Legacy nao serve"* — **nao e literalmente verdadeira**: a solucao **nao foi avaliada, porque nao foi submetida** | idem, item 2 |

> ### O efeito registrado esta certo; a afirmacao implicita esta falsa
>
> `REWRITE` produziu **`0` bytes admitidos** e proveniencia `native` — que e exatamente o
> efeito desejado. O que e falso no registro e a **afirmacao implicita** de que a solucao
> externa foi **avaliada e recusada**. **Afirmacao falsa dentro da norma e o defeito, mesmo
> quando o efeito e certo.**

### 1.1 Correcao de fato sobre a fonte da minuta

A minuta que precede esta `RFC` — `_missao-1-13-4-1-2026-07-31/minutas/MINUTA-A-…md`,
`sha256` `76eb131918c63e34228ceceb07b4bf8604a76c1fb418f2695e3c6dc7544552d5` — enumera as quatro
classes como `ADOPT · ADAPT · REWRITE · **REJECT**`.

**O texto vigente diz `RETIRE`.** `ADR-0007 §5.3`, linha `G3`, exige *"exatamente uma de
**ADOPT · ADAPT · REWRITE · RETIRE**"*, e `§5.4` define as quatro com esses nomes. **`rejected`
e o valor de PROVENIENCIA de `§5.5`, nao o nome da classe.**

> **A minuta entrou como EVIDENCIA, nao como norma, e e por isso que o erro foi apanhado.**
> Missao `BLOCKED` nao confere autoridade ao que produziu; o conteudo e materia-prima
> legitima, e materia-prima se confere contra a fonte antes de virar norma (`PJ-03`).

## 2. A pergunta de decisao

**O portao deve ganhar `G0` e `RECOGNIZE` agora, ou as duas lacunas devem permanecer
declaradas, com dono e gatilho?**

A pergunta ja esta na mesa do Soberano como **`Q2`** de
[`PS-2026-014 §7`](../governance/pacote-soberano-2026-07-31-medally.md), onde consta como
**nao bloqueante**.

## 3. Criterios de decisao

> Declarados antes do exame das alternativas (`CD-01`).

| # | Criterio | Peso | Como se mede |
|---|---|---|---|
| `K1` | Nenhum registro futuro do portao nasce com afirmacao falsa | **Bloqueante** | Existe classe cuja definicao literal descreve o que se fez |
| `K2` | Nenhum artefato historico e editado | **Bloqueante** | `0` bytes em `PS-2026-014`, `PT-2026-011`, `FIT-2026-019`, `ADR-0026`, `RFC-0021` |
| `K3` | Nao amplia o universo de entidades nem cria tipo documental | Alto | Universo permanece em **21** entidades e **33** tipos |
| `K4` | Nao altera quem decide | **Bloqueante** | `G1`, `G2`, `G4`, `G5` intactos; nenhum titular novo |
| `K5` | Reversivel | Alto | Desfazer nao destroi nada e nao exige migracao |

## 4. Alternativas consideradas

### Alternativa A — Acrescentar `G0` **e** `RECOGNIZE`, por ADR que supera parcialmente `ADR-0007`

| Campo | Conteudo |
|---|---|
| Descricao | `G0` declara o **objeto** da admissao *(`IDENTIDADE` · `CONTEUDO` · `AMBOS`)* e determina qual lista de `G3` se aplica; `RECOGNIZE` e a classe de `G0 = IDENTIDADE` |
| A favor | Satisfaz `K1` a `K5`. Fecha `RD-54` **e** `RD-55` de uma vez, e a segunda admissao pelo portao **nao** repete o registro falso |
| Contra | Acrescenta duas nocoes a um portao que so foi exercido uma vez |
| Custo | 1 `RFC` + 1 `ADR` + 1 entrada de catalogo + indices. **`0`** artefatos historicos |
| Avaliacao | `K1` ✔ · `K2` ✔ · `K3` ✔ · `K4` ✔ · `K5` ✔ |

### Alternativa B — Redefinir `REWRITE` para abarcar admissao de identidade

| Campo | Conteudo |
|---|---|
| Descricao | Ampliar a definicao de `REWRITE` para cobrir *"nada entra porque nada foi submetido"* |
| A favor | Custo minimo: uma definicao alterada, nenhuma classe nova |
| Contra | **Falha em `K1` por outro caminho.** Altera o significado de uma classe **ja usada** e torna **ambiguo todo registro anterior**: quem ler `REWRITE` em `ADR-0026` nao sabera se significa *"avaliei e recusei"* ou *"nao avaliei"*. É emenda que reescreve o passado sem tocar num byte dele |
| Avaliacao | `K1` **falha** · `K2` ✔ · `K3` ✔ · `K4` ✔ · `K5` ✔ |

### Alternativa C — Criar `G0` sem criar `RECOGNIZE`

| Campo | Conteudo |
|---|---|
| Descricao | Declarar o objeto da admissao e manter as quatro classes |
| A favor | Fecha `RD-54` com metade do custo |
| Contra | **Deixa `RD-55` aberto**, e de forma pior: haveria distincao **declarada** e **nenhuma classe para exerce-la**. `G0 = IDENTIDADE` obrigaria a escolher entre quatro classes das quais nenhuma cabe — o defeito de hoje, agora com um campo que o nomeia |
| Avaliacao | `K1` **falha** · `K2` ✔ · `K3` ✔ · `K4` ✔ · `K5` ✔ |

### Alternativa Z — Nao fazer nada: manter declarado, com dono e gatilho

| Campo | Conteudo |
|---|---|
| O que acontece | `RD-54` e `RD-55` seguem abertos, com dono **DEP-GOV** e gatilho *"segunda admissao pelo portao"* |
| Custo real da inacao | **O gatilho e a propria repeticao do defeito.** A segunda admissao **nascera com o mesmo registro falso**, e so entao a correcao seria feita — com dois registros a reclassificar em vez de um |
| Por que nao venceu | Declarar impede esquecer; **nao impede repetir**. O momento barato de corrigir e agora, com **um** registro alcancado |

## 5. Recomendacao

**Alternativa A.** Vence pelos cinco criterios; `B` e `C` falham no bloqueante `K1` por
caminhos opostos — `B` torna ambiguo o passado, `C` declara a distincao e nao a instrumenta.

## 6. Impacto levantado

| Dimensao | Impacto |
|---|---|
| Norma alcancada | **`ADR-0007 §5.3` linha `G3` e `§5.4`** — **duas** secoes, nao uma linha |
| Artefatos historicos editados | **`0`** — a superacao e por instrumento novo (`AL-02`, `LV-04`) |
| Fundacionais alcancados | **`0` — medido.** As quatro classificacoes **nao constam de nenhum `FND`**: fora de `ADR-0007`, as ocorrencias estao em `ADR-0010 CT-09`, `ADR-0026`, `FIT-2026-003` e projecoes `M3` |
| Entidades · tipos documentais | **`0`** e **`0`** |
| Produtos ou `Spec`s alcancados | **`0`** — nenhum existe |
| Documentos dependentes | `ADR-0010 CT-09` *(cita o vocabulario como precedente; **nao** e lista fechada)* · catalogo `§7` · indices `M3` |

## 7. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Achados que fecha | **`RD-54`** e **`RD-55`** |
| Questao do Soberano que responde | **`Q2`** de [PS-2026-014 §7](../governance/pacote-soberano-2026-07-31-medally.md) |
| Evidencia de origem | `_missao-1-13-4-1-2026-07-31/minutas/MINUTA-A-classe-de-admissao-de-existencia-em-G3.md`, `sha256` `76eb131918c63e34228ceceb07b4bf8604a76c1fb418f2695e3c6dc7544552d5` — **evidencia, nunca norma** |
| Decisao gerada | [ADR-0027](../decisions/ADR-0027-classe-de-admissao-de-existencia-no-portao-de-origem-externa.md) |
| Verificacao | [FIT-2026-020](../governance/fitness/FIT-2026-020-emenda-do-portao-de-origem-externa.md) |

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-31 | DEP-GOV | Proposta inicial. Submete `G0` e `RECOGNIZE` como resposta a `RD-54` e `RD-55`, com **tres** alternativas reais mais *"nao fazer nada"*. Registra a **correcao de fato** sobre a minuta de origem: a quarta classe e **`RETIRE`**, nao `REJECT`. |
