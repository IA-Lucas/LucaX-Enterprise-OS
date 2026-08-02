---
id: TPL-nota-decisao
titulo: Template de Nota de Decisao
tipo: template
versao: 1.0.0
status: ativo
camada_memoria: nao-aplicavel
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0001]
substitui: []
substituido_por: null
---

# Template — Nota de Decisao

## Proposito
Registrar decisoes C1 de escopo local, reversiveis, com o minimo irrenunciavel de
rastreabilidade — sem o peso de um ADR.

## Escopo
Decisao C1 · Tipo 2 · escopo local. **Nao se aplica** a decisao que cria precedente (DR-5),
que afeta mais de um departamento (DR-3) ou que seja Tipo 1 — nesses casos, use ADR.

## Responsaveis
Proprietario: DEP-GOV · Revisor: papel distinto do proponente (PI-05) · Registro: camada
de memoria Operacional.

## Instrucoes de uso
1. Grave em `memory/operacional/`, com id `MEM-OPR-<NNNN>-<slug>`.
2. Se a nota vier a ser invocada como precedente, ela **deve** ser promovida a ADR.
3. Nota sem revisor de papel distinto e invalida.

---
---
id: MEM-OPR-<NNNN>-<slug>
titulo: <a escolha em uma linha>
tipo: memoria
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: <DEP-xxx>
proprietario: <DEP-xxx>
aprovador: <DEP-xxx>
criado_em: <AAAA-MM-DD>
atualizado_em: <AAAA-MM-DD>
revisao_prevista: null
decisoes_relacionadas: []
substitui: []
substituido_por: null
origem: <MSG-id | PRJ-id | observacao direta>
evidencia: <base da escolha>
confianca: <alta|media|baixa>
ocorrencias: 1
ttl: <AAAA-MM-DD>
aplica_se_a: [<PRO-id | DEP-id>]
---

# Nota de Decisao: <Titulo>

## Proposito
<Por que esta escolha precisou ser feita.>

## Escopo
<Onde vale. Onde nao vale.>

## Responsaveis
| Papel | Quem |
|---|---|
| Decisor | |
| Revisor (papel distinto) | |

## Contexto
<Em duas ou tres frases: qual era a situacao.>

## Escolha
**Optamos por <...>.**

## Alternativa descartada
<Ao menos uma, com o motivo do descarte.>

## Motivo
<Por que esta e nao a outra.>

## Reversao
<Como desfazer, e por que e trivial. Se nao for trivial, isto nao e C1/Tipo 2 — vire ADR.>

## Data e responsavel
<AAAA-MM-DD> — <DEP-xxx>

---
### Gatilhos de promocao a ADR
- [ ] Foi invocada como precedente
- [ ] Passou a afetar outro departamento
- [ ] Revelou-se irreversivel na pratica
- [ ] Repetiu-se em 2+ ocorrencias

Marcado qualquer item, abrir ADR referenciando esta nota.
