---
id: RFC-0036-framework-de-ferramentas-e-modelos
titulo: Admissao do candidato Tool & Model Framework - TF-01 a TF-32 - o segundo rito da ordem do decimo terceiro ato
tipo: rfc
versao: 1.0.0
status: aprovado
camada_memoria: nao-aplicavel
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-08-13
atualizado_em: 2026-08-13
revisao_prevista: null
decisoes_relacionadas: [ADR-0003, ADR-0021, ADR-0040]
substitui: []
substituido_por: null
classe_mudanca: C2
prazo_analise: 2026-08-13
---

# RFC-0036: Admissao do Tool & Model Framework

## Proposito

Segundo rito do Bloco A do 13º ato: admitir `TF-01`–`TF-32` *(Missao 1.14, 2026-08-02,
`H-A 1cd2403b…fc1d`)* como o Tool & Model Framework do Goal `1.14`.

## Pergunta clara

**O contrato da Ferramenta — registro, permissoes, classificacao de dados, isolamento,
credencial, custo, e Modelo como classe (selecao, roteamento, fallback) — entra como norma
pelo metodo do Framework-dentro-do-ADR, sem criar nada e sem integrar provedor algum?**

## Alternativas analisadas

| # | Alternativa | Analise | Veredito |
|---|---|---|---|
| (a) | Manter fora do acervo | descumpre o 13º ato | ❌ |
| (b) | Emendar fontes/template | os defeitos AF-1/AF-2 sao rito de `TPL` *(dono proprio)* — emendar aqui seria usurpar competencia; e espalhar 32 regras e o caminho que `ADR-0022` desfez | ❌ |
| (c) | ⭐ ADR unico com o Framework dentro | sede unica `M1`, `C2 · Tipo 2`, `0` atos; defeitos de template REGISTRADOS abertos como pre-condicao de uso | ✅ |

## Condicao de admissao — candidato REMEDIDO

`AF-1` *(modelo = 1 homonimo)*, `AF-2` *(0 Capabilities habilitadas)* e `AF-3` *(`tools/`
inexistente)* **CONFIRMAM hoje**; `L6` **envelheceu a favor** *(ordem decidida)*. Detalhe em
[ADR-0041](../decisions/ADR-0041-framework-de-ferramentas-e-modelos.md).

## Desfecho

**Aprovada** — autorizacao do proprio 13º ato. Decisao em
[ADR-0041](../decisions/ADR-0041-framework-de-ferramentas-e-modelos.md); aptidao em
[FIT-2026-034](../governance/fitness/FIT-2026-034-framework-de-ferramentas-e-modelos.md).
