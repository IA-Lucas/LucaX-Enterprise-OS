---
id: RFC-0035-framework-de-workflows
titulo: Admissao do candidato Framework de Workflows - WF-01 a WF-30 - o primeiro rito da ordem do decimo terceiro ato
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
decisoes_relacionadas: [ADR-0021, ADR-0033]
substitui: []
substituido_por: null
classe_mudanca: C2
prazo_analise: 2026-08-13
---

# RFC-0035: Admissao do Framework de Workflows

## Proposito

Executar o primeiro rito do Bloco A do **decimo terceiro ato**: admitir o candidato
`WF-01`–`WF-30` *(Missao 1.14, 2026-08-02, fora do acervo,
`H-A 881d9abf…a3dc60`)* como o **Workflow Framework** do Goal `1.16`.

## Pergunta clara

**O contrato do Workflow — estados, portoes, handoff, falha/retry/timeout, compensacao/
rollback/retomada, escalonamento, intervencao humana e memoria — entra como norma, pelo
metodo de `ADR-0033` (o Framework dentro do ADR), sem criar entidade alguma?**

## Alternativas analisadas

| # | Alternativa | Analise | Veredito |
|---|---|---|---|
| (a) | **Manter fora do acervo** | o 13º ato ja decidiu admitir; manter seria descumprir | ❌ |
| (b) | **Emendar as fontes** *(espalhar as 30 regras por FND/TPL)* | `ADR-0021` pagou esse caminho e `ADR-0022` o desfez a 1.328 linhas de retrabalho | ❌ |
| (c) | ⭐ **ADR unico com o Framework dentro** *(o metodo de `ADR-0033`)* | sede unica, `M1` — corrige-se por sucessor; `C2 · Tipo 2`, `0` atos *(`WFL` nunca ratifica)* | ✅ |

## Condicao de admissao — o candidato foi REMEDIDO

Os 4 zeros da lacuna **seguram hoje** *(controles vivos 7/8)*; `workflows/` inexistente;
`AW-3` confirmado; **`L5` envelheceu a favor** *(3 Skills; ordem decidida)*. Detalhe na
secao de recepcao de [ADR-0040](../decisions/ADR-0040-framework-de-workflows.md).

## Desfecho

**Aprovada** — a autorizacao e o proprio 13º ato. Decisao em
[ADR-0040](../decisions/ADR-0040-framework-de-workflows.md); aptidao em
[FIT-2026-033](../governance/fitness/FIT-2026-033-framework-de-workflows.md).
