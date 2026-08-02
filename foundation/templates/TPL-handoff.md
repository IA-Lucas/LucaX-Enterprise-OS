---
id: TPL-handoff
titulo: Template de Handoff
tipo: template
versao: 1.0.0
status: ativo
camada_memoria: nao-aplicavel
autor: DEP-GOV
proprietario: DEP-EXE
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0001]
substitui: []
substituido_por: null
---

# Template — Handoff

## Proposito
Transferir trabalho e responsabilidade entre areas sem perda de contexto, conforme
[FND-05 §4](../05-framework-comunicacao.md).

## Escopo
Toda transferencia lateral de trabalho entre departamentos ou, futuramente, entre agentes.

> **Silencio nunca transfere responsabilidade** (HO-01). Sem aceite explicito, o trabalho
> continua sendo do emissor.

## Responsaveis
Proprietario: DEP-EXE · Registro: camada de memoria Operacional · Curadoria: DEP-KMS.

## Instrucoes de uso
1. Handoff que atravessa portao so e emitido apos a liberacao do portao (HO-04).
2. Contexto e **curado**, nao despejado (PC-01). Referencie por ID (CM-09).
3. Devolvido duas vezes pelo mesmo motivo, escale a DEP-EXE (HO-03).

---
---
msg_id: MSG-<AAAA>-<NNNN>
canal: HANDOFF
de: <DEP-xxx | AGT-xxx>
para: <DEP-xxx | AGT-xxx>
com_copia: []
assunto: <uma linha, sem ambiguidade>
prioridade: <rotina|alta|critica>
referencias: []
prazo: <AAAA-MM-DD | null>
nivel_autonomia_concedido: <A0|A1|A2|A3>
resposta_esperada: aceite
criado_em: <AAAA-MM-DD>
estado_do_trabalho: <em que ponto esta>
o_que_falta: <resumo>
criterio_de_devolucao: <em que condicao o receptor pode recusar>
---

# Handoff: <Assunto>

## Contexto
<O que o receptor precisa saber para agir — e apenas isso (CM-04).>

## Pedido
<Uma frase imperativa. Exatamente um pedido (CM-05).>

## Criterio de aceite
<Como se verifica objetivamente que o pedido foi atendido.>

## Fora de escopo
<O que explicitamente nao se pede.>

## Restricoes
<Normas, limites, riscos e dependencias aplicaveis.>

---

## Contrato de handoff (FND-05 §4.1)

| Clausula | Conteudo |
|---|---|
| **Objeto** | O que exatamente esta sendo transferido |
| **Estado** | Em que ponto o trabalho esta agora |
| **Feito** | O que ja foi concluido **e verificado** |
| **Nao feito** | O que falta e o que foi deliberadamente deixado de fora |
| **Decisoes tomadas** | Escolhas fechadas, por ID — nao devem ser reabertas |
| **Decisoes em aberto** | O que o receptor precisa decidir |
| **Premissas** | O que se assumiu sem confirmar |
| **Riscos conhecidos** | O que pode dar errado e o que ja se sabe |
| **Criterio de aceite** | Como o receptor sabe que terminou |
| **Criterio de devolucao** | Em que condicao pode recusar |

## Pacote de contexto (FND-05 §5)

| Camada | Conteudo |
|---|---|
| **Nucleo** | <o minimo indispensavel — sempre curto> |
| **Suporte** | <lista de IDs consultaveis sob demanda — nunca conteudo> |
| **Historico** | <o que ja foi tentado e por que nao serviu> |
| **Fronteira** | <o que esta fora do escopo e nao deve ser tocado> |

---

## Resposta do receptor

| Campo | Conteudo |
|---|---|
| Decisao | **aceite** / **devolucao** |
| Data | |
| Se devolucao, motivo (HO-02) | escopo insuficiente / contexto insuficiente / fora do dominio / conflito com norma / dependencia nao resolvida |
| Detalhe do motivo | |
| O que falta para aceitar | |

> Aceito o handoff, a responsabilidade passa ao receptor a partir da data acima.
> Sem aceite registrado, ela permanece com o emissor.
