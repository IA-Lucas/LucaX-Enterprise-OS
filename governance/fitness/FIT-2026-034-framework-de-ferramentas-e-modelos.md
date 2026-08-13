---
id: FIT-2026-034-framework-de-ferramentas-e-modelos
titulo: Verificacao de aptidao - o Tool & Model Framework (ADR-0041)
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
decisoes_relacionadas: [ADR-0040, ADR-0041]
substitui: []
substituido_por: null
veredito: apto-com-ressalva
---

# FIT-2026-034 — O Tool & Model Framework

**Objeto:** [ADR-0041](../../decisions/ADR-0041-framework-de-ferramentas-e-modelos.md) e
[RFC-0036](../../rfcs/RFC-0036-framework-de-ferramentas-e-modelos.md). **Portao:** `QG-6`
(`CV-07`, `C2`).

> `FT-02`/`LV-03`: avaliador `DEP-QAR` ≠ produtores. `FT-10`: parecer, nao decisao.

## Veredito

**`apto-com-ressalva`.** Tres ressalvas, nenhuma bloqueia.

## 1. Conformidade

| # | Criterio | Sinal | Veredito |
|---|---|---|---|
| `F1` | Autorizacao antes do rito | 13º ato, segundo da ordem *(1.16 fechado antes)* | ✅ |
| `F2` | Candidato ancorado e REMEDIDO | `H-A` conferido; `AF-1`/`AF-2`/`AF-3` **confirmados hoje por ferramenta** *(homonimo da linha 110 inspecionado, nao so contado)*; `L6` resolvida pelos fatos | ✅ |
| `F3` | `0` criacoes | entidade/classe/template/portao/papel: recebidos; matriz intacta; `tools/` NAO criado | ✅ |
| `F4` | Metodo com precedente | Framework-dentro-do-ADR *(`ADR-0033`/`0040`)*; fonte alguma emendada — **inclusive o template defeituoso, por competencia** | ✅ |
| `F5` | Contadores exercidos e movidos | `RFC-0036` · `ADR-0041` · `FIT-2026-034` — `V1` contra a copia do token 50 | ✅ |
| `F6` | Assimetria de custo DECLARADA | a norma `0` atos; **cada adocao de Ferramenta `C2 · Tipo 1` com ratificacao** — gravada na decisao, nao descoberta depois | ✅ |

## 2. ⚠️ Ressalvas

- **`R1`** — as 32 regras nascem **determinadas, nao observadas** *(`0` `TOL`; `tools/`
  inexistente)*. Gatilho: a primeira Ferramenta real.
- **`R2`** — **`AF-1`/`AF-2` sao pre-condicao de uso NAO cumprida**: ate a emenda do
  `TPL-ferramenta` *(rito proprio, dono `DEP-GOV + DEP-TLS`)*, **nenhuma ficha de classe
  `modelo` e registravel** pelo template canonico. O Framework vige; a via de uso esta
  bloqueada por defeito alheio, **e isso fica na cara**.
- **`R3`** — `TF-27` *(fallback)* e `TF-28` *(falha plausivel-e-errada)* sem instancia — a
  parte menos testada, nomeada para a revisao.
