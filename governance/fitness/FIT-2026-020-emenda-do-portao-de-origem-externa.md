---
id: FIT-2026-020
titulo: Verificacao de aptidao da emenda do portao de origem externa — G0 e RECOGNIZE
tipo: fitness-check
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: DEP-QAR
proprietario: DEP-QAR
aprovador: DEP-EXE
criado_em: 2026-07-31
atualizado_em: 2026-07-31
revisao_prevista: null
decisoes_relacionadas: [ADR-0007, ADR-0015, ADR-0026, ADR-0027]
substitui: []
substituido_por: null
veredito: apto-com-ressalva
resumo: Verifica a aptidao da emenda que acrescenta G0 e RECOGNIZE ao portao de origem externa, com C11 conforme em 13 de 13 e tres ressalvas.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-GOV
ratificacao: nao-exigida
---

# FIT-2026-020: emenda do portao de origem externa

> **Parecer, nao decisao** (`ADR-0015`, `FT-10`). **Nao aprova, nao ratifica, nao promulga.**
> `FND-09 §8.2`, linha `FIT`: **ratifica `—`**. O objeto avaliado esta **`em-revisao`** e
> **nao esta em vigor**.

## Proposito

Emitir a Verificacao de Aptidao Arquitetural exigida por `CV-07` de `FND-04 §4.1` sobre a
mudanca `C2` registrada em [ADR-0027](../../decisions/ADR-0027-classe-de-admissao-de-existencia-no-portao-de-origem-externa.md).

## Escopo

| Item | Definicao |
|---|---|
| Avaliado | O **rito** `RFC-0022` → `ADR-0027` · a **determinacao da classe** · o **custo de reversao** · a **norma superada** · a conformidade **`C11`** |
| **Nao** avaliado | O merito de candidato algum · `Q1` · o pacote da 1.13.4 · as emendas 2 e 3, que tem parecer proprio |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| Emite | **DEP-QAR** | `FND-09 §8.2` linha `FIT` |
| Revisa a forma | **DEP-GOV** | idem |
| Aprova | **DEP-EXE** | idem |
| Ratifica | **—** | `FT-10` |

> ### Independencia desta verificacao — declarada pelo criterio VIGENTE
>
> **Criterio aplicado: `AC-03` de `FND-10 §2.5`** — `revisor` ≠ `autor`. **Satisfeito:** autor
> **DEP-QAR**, revisor **DEP-GOV**, e o objeto avaliado tem autor **DEP-GOV**.
>
> **`ADR-0028` NAO esta em vigor e NAO se aplica a este parecer.** Sob o criterio que ela
> propoe, esta verificacao seria **`fornecedor_verificacao: interno`** — mesmo executor. **A
> diferenca esta escrita para que ninguem leia este parecer como independente de fornecedor.**

## 1. Controles obrigatorios

| # | Controle | Fonte | Resultado |
|---|---|---|---|
| `F1` | Classe determinada, **nao presumida por analogia** | `FND-04 §2` | ✅ **As cinco hipoteses de `C3` percorridas uma a uma**, cada uma com o teste que a descarta — `ADR-0027 §11.1` |
| `F2` | A hipotese *"a propria Fundacao"* descartada **por medicao** | idem | ✅ **`0`** ocorrencias das quatro classificacoes em `FND` algum |
| `F3` | Norma superada **nomeada e delimitada** | `AL-02`, `LV-04` | ✅ `ADR-0007 §5.3` linha `G3` **e** `§5.4`, **quanto a lista e somente quanto a ela** |
| `F4` | Superacao **por instrumento novo**, sem editar o superado | `AL-02`, precedente `ADR-0022` | ✅ **`0` bytes** em `ADR-0007`; `superado_por` dele **nao** preenchido |
| `F5` | Custo de reversao **medido objeto a objeto** | `VD-06` | ✅ 1 `ADR` + 1 entrada de catalogo + indices `M3`; **`0`** historicos, **`0`** fundacionais |
| `F6` | `RFC` produzida quando a classe exige | `FND-04 §2` | ✅ [RFC-0022](../../rfcs/RFC-0022-classe-de-admissao-de-existencia-no-portao-de-origem-externa.md) — **dispensa nao disponivel**, tres alternativas defensaveis (`ADR-0027 §11.2`) |
| `F7` | Alternativas reais, sem palha | `VD-01`, `VD-03` | ✅ **3 + Z**; `B` e `C` falham no bloqueante `K1` por caminhos opostos |
| `F8` | Ausencia de evidencia declarada | `PI-10`, `VD-05` | ✅ `A1` — **nenhuma segunda admissao** ocorreu; a eficacia e prevista |
| `F9` | Nao amplia entidades nem tipos | `MT-01`, `CS-01` | ✅ **21** e **33**, inalterados |
| `F10` | Nao move direito de decisao | `FND-09 §8.2` | ✅ `GA-02` — Proponente, DEP-GOV, DEP-QAR e aprovador da classe **sao os de hoje** |
| `F11` | Correcao de fato sobre a fonte, declarada | `PJ-03` | ✅ A quarta classe e **`RETIRE`**, nao `REJECT` — corrigido e registrado, nao dissolvido |
| `F12` | Objeto **nao aplicado** | limite da missao | ✅ `status: em-revisao`; **`0`** admissoes sob `RECOGNIZE` |

## 2. `C11` — conformidade de [FND-10 §11](../../foundation/10-artifact-framework.md)

**13 de 13 conformes**, sobre os objetos criados por esta emenda (`RFC-0022`, `ADR-0027`, este parecer).

| # | Verificacao | Resultado |
|---|---|---|
| 1 | Contrato `L1` completo | ✅ os **15** de `FND-03 §4` + os **cinco** de `FND-10 §2.2` presentes nos tres |
| 2 | `revisor` ≠ `autor` | ✅ `RFC-0022` GOV/QAR · `ADR-0027` GOV/QAR · `FIT-2026-020` QAR/GOV |
| 3 | `ratificacao` coerente com a classe | ✅ `C2`/`Tipo 2` → **`nao-exigida`** nos tres |
| 4 | Tipo documental consta de `§4` | ✅ `rfc`, `adr`, `fitness-check` |
| 5 | Atributo derivavel no frontmatter | ✅ **nenhum** (`AC-01`) |
| 6 | Cadeia origem → estado → substituicao percorrivel | ✅ `RFC-0022` → `ADR-0027` → `FIT-2026-020` → `PS-2026-015` |
| 7 | Custo de contexto medido, nao estimado | ✅ linhas medidas no catalogo `§4` |
| 8 | Entrada no catalogo mestre presente | ✅ `§4.2` e `§4.5` |
| 9 | Divisao com menos de dois sinais | ✅ **nao aplicavel** — nenhuma especializacao proposta |
| 10 | Tabela reproduzida sem declaracao de projecao | ✅ **`0`** — a tabela de `§5.2` de `ADR-0027` e **fonte nova**, nao projecao |
| 11 | Teste preventivo de projecao aplicado | ✅ §2 deste parecer |
| 12 | Conteudo de origem externa admitido fora do portao | ✅ **`0` bytes** de origem externa nesta emenda |
| 13 | Alteracao de conteudo sem incremento de versao | ✅ **`0`** — todos os objetos sao **novos**, `1.0.0` |

## 3. Ressalvas

| # | Ressalva | Dono | Gatilho |
|---|---|---|---|
| `RA-1` | **`RECOGNIZE` nasce com UM membro, e ele e retrospectivo.** `AQ-03` suspeita de abstracao com menos de dois membros. A classe e desenhada a partir do unico caso medido, e `RC-1` a aplica a ele | **DEP-QAR** | **Segunda admissao pelo portao** |
| `RA-2` | **`RD-54` e `RD-55` NAO estao fechados por este parecer.** Fecham na **vigencia** de `ADR-0027`, nunca na redacao. Enquanto isso, o registro da 1.13.4 continua lendo-se `REWRITE` — `RC-5` | **DEP-GOV** | Ato que aplicar `ADR-0027` |
| `RA-3` | **`ADR-0010 CT-09` cita o vocabulario de quatro classes** como precedente de termos em ingles. A quinta classe **estende** o precedente sem contradize-lo, mas `CT-09` **nao foi emendado** e passa a citar uma lista incompleta | **DEP-GOV** | Proxima emenda a `ADR-0010` |

## 4. Evidencia ausente, declarada — `PI-10`

| # | Ausencia |
|---|---|
| 1 | **Nenhuma segunda admissao pelo portao ocorreu.** A utilidade de `G0` e de `RECOGNIZE` e **prevista, nao observada** |
| 2 | **Nenhuma admissao com `G0 = AMBOS` foi exercida.** A operabilidade de duas classificacoes na mesma admissao **nao foi testada** |
| 3 | **Este parecer nao mediu o repositorio do medAlly**, e nao precisava: a emenda alcanca instrumento do proprio acervo |

## 5. Veredito

**`apto-com-ressalva`.**

A mudanca e **apta**: o rito esta completo, a classe foi **determinada e nao presumida**, a
norma superada esta **delimitada**, o custo de reversao esta **medido objeto a objeto** e
**`0`** artefatos historicos sao alcancados. As **tres** ressalvas tem dono e gatilho, e
**nenhuma delas bloqueia** — `RA-1` e limite de evidencia, `RA-2` e consequencia do limite da
missao, `RA-3` e cascata declarada.

> **Este parecer nao coloca `ADR-0027` em vigor.** Quem aprova a mudanca `C2` e **DEP-EXE, com
> parecer de DEP-GOV** (`FND-04 §2.1`) — e a questao **`Q2`** de `PS-2026-014 §7` ja submeteu a
> materia ao Soberano, o que faz da aprovacao por DEP-EXE, **antes** da resposta, uma
> antecipacao que este parecer **nao recomenda**.

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-31 | DEP-QAR | Parecer inicial sobre `ADR-0027`. **`C11` 13 de 13.** `12` controles obrigatorios conformes. **Tres** ressalvas com dono e gatilho; **tres** ausencias de evidencia declaradas. Independencia aferida pelo criterio **VIGENTE** (`AC-03`), com a declaracao de que `ADR-0028` **nao esta em vigor e nao se aplica a este parecer**. Veredito **`apto-com-ressalva`**. |
