---
id: RFC-0034-contrato-fabrica-acervo-e-migracao
titulo: O contrato fabrica-acervo entra como norma e os setores CONVOCADOS migram — o rito C3 unico autorizado pelo decimo primeiro ato
tipo: rfc
versao: 1.0.0
status: aprovado
camada_memoria: nao-aplicavel
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-08-12
atualizado_em: 2026-08-12
revisao_prevista: null
decisoes_relacionadas: [ADR-0007, ADR-0011, ADR-0038]
substitui: []
substituido_por: null
classe_mudanca: C3
prazo_analise: 2026-08-12
---

# RFC-0034: O contrato fabrica↔acervo e a migracao dos CONVOCADOS

## Proposito

Formalizar a proposta que o **`PS-2026-018` 1.1.0** submeteu e o **decimo primeiro ato**
([`MSG-2026-0011`](../memory/operacional/MSG-2026-0011-ato-soberano-migracao-e-contrato.md))
assinou: gravar o **contrato fabrica↔acervo** (`F35 §2.2`, copia literal) como norma, e migrar
os **setores `CONVOCADO` da F34** as Cartas dos Departamentos que os amparam — **um rito `C3`,
pago uma vez** *(a economia medida pela M-01)*.

## Pergunta clara

**A fronteira fabrica↔acervo passa a ser norma do acervo — com o exercicio da F34 como portao
de migracao — e os dez setores aprovados entram nas Cartas por custodia declarada?**

## Alternativas analisadas

| # | Alternativa | Analise | Veredito |
|---|---|---|---|
| (a) | **Dois atos** *(um do contrato, um da migracao)* | paga o custo fixo do rito `C3` **duas vezes**; as hipoteses de `FND-04 §2` sao as mesmas nos dois | ❌ |
| (b) | **Contrato sem forca normativa** *(Diretiva `C1`)* | vira registro de que algo foi dito — **nao faz o contrato valer**; `FND-10 §4.2` veta Nota de Decisao para precedente *(e este contrato E o precedente dos setores — `DR-5`, `DR-3`)* | ❌ |
| (c) | ⭐ **Um ato `C3` unico, com o rito completo** *(`RFC` → analise de impacto → `ADR` → ratificacao + reversao + `FIT` + `REV`)* | as tres incidencias de `FND-04 §2` medidas no `PS-2026-018 §3.I`; o gatilho *(linha 5 do contrato)* ja **exercido**: F34 fechou `20/20` | ✅ **assinada** |

## Analise de impacto *(o levantamento obrigatorio de `FND-04 §4 [4]`)*

- **Alcance normativo:** 1 `ADR` novo *(o contrato)*; **`0` Fundacionais emendadas** — a linha 3
  entra com leitura compativel *("executor" = o Departamento que ampara)*, sem tocar `FND-02 §10`.
- **Alcance nas Cartas:** as dos custodios declarados dos `CONVOCADO` *(mapa medido antes da
  primeira escrita; setor sem custodia **volta nominalmente** — parada `§5(a)` do pacote)*.
- **Cascata:** os **nove perfis §13.2 remedidos** *(`DC-10`; o gate de `RD-49` dispara — este e
  "o proximo ato que alcanca Carta de Departamento")*.
- **Reversao:** `RB-01` — copia datada verificada + commits atomicos + revert + baseline.

## Desfecho

**Aprovada pelo proprio ato** *(a assinatura do `PS-2026-018` e a aprovacao desta proposta —
o pacote levou a minuta com este conteudo)*. Decisao em
[`ADR-0039`](../decisions/ADR-0039-contrato-fabrica-acervo.md); aptidao em
[`FIT-2026-032`](../governance/fitness/FIT-2026-032-aplicacao-do-decimo-primeiro-ato.md);
revisao/transicao em [`PT-2026-026`](../governance/relatorio-transicao-2026-08-12-aplicacao-ps018.md).
