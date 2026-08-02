---
id: TPL-carta-projeto
titulo: Template de Carta de Projeto
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

# Template — Carta de Projeto

## Proposito
Dar existencia formal a um esforco temporario com inicio, fim e resultado definido,
conforme [FND-03 §3.2](../03-taxonomia.md).

## Escopo
Criacao e encerramento de projeto. Classe C1 ou C2, conforme o impacto.

> **Projeto termina; produto continua.** Se nao houver criterio de encerramento, isto e
> produto ou operacao contínua — nao projeto.

## Responsaveis
Proprietario: DEP-EXE (alocacao) + departamento dono do resultado · Conformidade: DEP-GOV.

## Instrucoes de uso
1. Grave em `projects/PRJ-<AAAA>-<NNN>/carta.md`.
2. Projeto sem criterio de encerramento **nao e aprovado** (FND-04 §6).
3. Ao encerrar, o registro de aprendizado e obrigatorio (QG-5).

---
---
id: PRJ-<AAAA>-<NNN>
titulo: <Nome do Projeto>
tipo: carta
versao: 1.0.0
status: rascunho
camada_memoria: operacional
autor: <DEP-xxx>
proprietario: <DEP-xxx>
aprovador: DEP-EXE
criado_em: <AAAA-MM-DD>
atualizado_em: <AAAA-MM-DD>
revisao_prevista: <AAAA-MM-DD>
decisoes_relacionadas: []
substitui: []
substituido_por: null
---

# <Nome do Projeto> (PRJ-<AAAA>-<NNN>)

## Proposito
<Que resultado este projeto entrega. Ate 3 frases.>

## Escopo
| Item | Definicao |
|---|---|
| Inclui | |
| Nao inclui | |
| Produto relacionado | <PRO-id ou "nenhum"> |

## Responsaveis
| Papel | Quem |
|---|---|
| Dono do resultado | <DEP-xxx> |
| Alocacao e prioridade | DEP-EXE |
| Verificacao final | DEP-QAR |

## 1. Resultado esperado
<Uma frase inequivoca: o que existira ao fim que nao existe hoje.>

## 2. Criterio de encerramento
> Obrigatorio. Sem isto, a carta nao e aprovada.

| Condicao de termino | Como se verifica |
|---|---|

### 2.1 Criterio de cancelamento
<Sob que condicoes este projeto deve ser interrompido antes do fim.>

## 3. Entregaveis
| # | Entregavel | Portao aplicavel | Dono |
|---|---|---|---|

## 4. Fora de escopo
| Item | Por que fica de fora |
|---|---|

## 5. Dependencias
| Dependencia | Dono | Bloqueia o que |
|---|---|---|

## 6. Riscos
| # | Risco | Impacto | Mitigacao |
|---|---|---|---|

## 7. Premissas
| Premissa | Se falsa, o que muda |
|---|---|

## 8. Memoria consultada (QG-0)
| Registro (MEM-id) | O que ele informou a este projeto |
|---|---|

## 9. Encerramento
| Campo | Conteudo |
|---|---|
| Data de encerramento | |
| Criterio atendido? | |
| Nao entregue (e por que) | |
| Registro APR gerado | <MEM-APR-id> |
| Verificacao QG-5 | |
