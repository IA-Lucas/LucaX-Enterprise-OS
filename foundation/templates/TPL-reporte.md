---
id: TPL-reporte
titulo: Template de Reporte de Resultado
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

# Template — Reporte de Resultado

## Proposito
Padronizar o relato de estado, resultado ou conclusao de trabalho, conforme
[FND-05 §6](../05-framework-comunicacao.md).

## Escopo
Todo reporte de baixo para cima. Inclui o reporte consolidado ao Soberano (§6.3 de FND-05).

## Responsaveis
Proprietario: DEP-EXE · Verificacao de evidencia: DEP-QAR · Colheita de aprendizado: DEP-KMS.

## Instrucoes de uso
1. **Reporte sem `Evidencia` e invalido** (RP-01). "Feito" nao e evidencia.
2. **Reporte sem `Nao entregue` presume escopo integral** (RP-02). Omitir viola PI-10.
3. Estado `concluido` exige verificacao independente ja realizada (RP-03). Sem ela, o
   estado correto e `concluido-com-ressalva`.
4. Sem `Aprendizado`, o portao QG-5 nao fecha (RP-05).

---
---
msg_id: MSG-<AAAA>-<NNNN>
canal: REPORTE
de: <DEP-xxx | AGT-xxx>
para: <DEP-xxx | SOBERANO>
com_copia: []
assunto: <uma linha>
prioridade: <rotina|alta|critica>
referencias: []
prazo: null
nivel_autonomia_concedido: <A0|A1|A2|A3>
resposta_esperada: <ciencia|decisao>
criado_em: <AAAA-MM-DD>
estado: <concluido|concluido-com-ressalva|parcial|bloqueado|cancelado>
---

# Reporte: <Assunto>

## Estado
`concluido` | `concluido-com-ressalva` | `parcial` | `bloqueado` | `cancelado`

## Entregue
| # | O que foi produzido | Onde esta (ID ou caminho) |
|---|---|---|

## Evidencia
> Como se sabe que funciona: verificacao, saida, teste, fonte (DoD-5). Obrigatorio.

| # | Afirmacao | Evidencia | Verificada por |
|---|---|---|---|

## Nao entregue
> O que estava no escopo e nao foi feito — e por que (PI-10). Obrigatorio, mesmo que vazio.

| Item | Por que | Impacto | Quem passa a ser dono |
|---|---|---|---|

## Desvios
| Onde divergiu do aprovado | Sob qual autorizacao | Registro |
|---|---|---|

## Decisoes tomadas
| Decisao | Instrumento (ADR / Nota) | ID |
|---|---|---|

## Riscos e pendencias
| # | Pendencia | Dono | Prazo |
|---|---|---|---|

## Aprendizado
> Alimenta a camada APR. Sem esta secao, QG-5 nao fecha.

| Campo | Conteudo |
|---|---|
| O que a proxima ocorrencia deveria saber | |
| Causa (se houve falha) | |
| Condicoes em que a licao se aplica | |
| Registro MEM-APR gerado | |

---

## Se reporte ao Soberano (FND-05 §6.3)

Ordem obrigatoria:

### 1. Precisa da sua decisao
| # | Decisao pendente | Tipo (1/2) | Alternativas | Recomendacao |
|---|---|---|---|---|

### 2. Ma noticia
<Vem antes de boa noticia (CM-08).>

### 3. Resultado
<O que foi entregue e verificado.>

### 4. Fato x estimativa
| Afirmacao | Fato verificado | Estimativa |
|---|---|---|

### 5. Proximo ciclo
<O que se propoe fazer a seguir.>

> Este reporte nao contem credencial, dado sensivel ou segredo em texto (PI-08, SB-05).
