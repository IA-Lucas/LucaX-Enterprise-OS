---
id: FIT-2026-033-framework-de-workflows
titulo: Verificacao de aptidao - o Framework de Workflows (ADR-0040)
tipo: fitness-check
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: DEP-QAR
proprietario: DEP-QAR
aprovador: DEP-EXE
criado_em: 2026-08-13
atualizado_em: 2026-08-13
revisao_prevista: null
decisoes_relacionadas: [ADR-0033, ADR-0040]
substitui: []
substituido_por: null
veredito: apto-com-ressalva
---

# FIT-2026-033 — O Framework de Workflows

**Objeto avaliado:** [ADR-0040](../../decisions/ADR-0040-framework-de-workflows.md) e
[RFC-0035](../../rfcs/RFC-0035-framework-de-workflows.md). **Portao:** `QG-6`, obrigatorio
(`CV-07`, `C2`).

> `FT-02`/`LV-03`: avaliador `DEP-QAR`; objetos de `DEP-GOV`/candidato de `DEP-EXE` (2026-08-02).
> `FT-10`: parecer, nao decisao.

## Veredito

**`apto-com-ressalva`.** Tres ressalvas, nenhuma bloqueia.

## 1. Conformidade — com sinal observavel

| # | Criterio | Sinal | Veredito |
|---|---|---|---|
| `F1` | **Autorizacao ANTES do rito** | 13º ato, Bloco A, ordem despachada — 1.16 e o primeiro | ✅ |
| `F2` | **Candidato ancorado e REMEDIDO na admissao** | `H-A 881d9abf…` conferido; os 4 zeros da lacuna SEGURAM *(hoje)*; controles vivos com divergencia DECLARADA *(9→7/8, metodo/data)*; `L5` resolvida pelos fatos *(3 SKL; ordem decidida)* — **nada herdado sem remedir** | ✅ |
| `F3` | **`0` criacoes** *(N1–N9 do corpo)* | portoes **7 antes, 7 depois**; matriz `FND-09 §8.2` **`0` celulas**; `workflows/` **nao criado**; `0` campos novos | ✅ |
| `F4` | **Metodo com precedente** | o de `ADR-0033`: Framework dentro do ADR, sede unica `M1`, fonte alguma emendada | ✅ |
| `F5` | **Contadores exercidos e movidos na mesma mudanca** | `RFC-0035` · `ADR-0040` · `FIT-2026-033` — `V1` contra a copia datada do token 49 | ✅ |
| `F6` | **Custo do rito no projetado** | `C2 · Tipo 2`, **`0` atos** — `WFL` nunca ratifica *(`FND-09 §8.2`)*; 3 artefatos + indices | ✅ |

## 2. ⚠️ Ressalvas

- **`R1` — as 30 regras nascem DETERMINADAS, nao observadas** *(`0` Workflows reais; o
  proprio candidato o declara em `L1`)*. Gatilho de revisao escrito: o primeiro Workflow real.
- **`R2` — a contribuicao propria (`WF-19`–`WF-25`) e a parte menos testada** *(`L3`/`L4`:
  nenhum retry/timeout/compensacao/retomada real; falha plausivel-e-errada sem instancia)* —
  exatamente a historia de `SK-12` no Framework de Skills, e fica nomeada para a revisao.
- **`R3` — `AW-2` e `AW-3` seguem ABERTOS** *(o `TPL-workflow` nao tem os blocos da
  contribuicao propria, e o frontmatter do template diz `aprovador: SOBERANO` contra a
  matriz)* — donos e gatilhos do candidato mantidos; **o primeiro Workflow real vai esbarrar
  neles**, e e assim que se cobra.
