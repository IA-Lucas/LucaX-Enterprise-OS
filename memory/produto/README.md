---
id: IDX-mem-produto
titulo: Camada de Produto da Memoria
tipo: relatorio
versao: 1.0.0
status: ativo
camada_memoria: produto
autor: DEP-GOV
proprietario: DEP-PRD
aprovador: DEP-KMS
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: null
decisoes_relacionadas: [ADR-0001]
substitui: []
substituido_por: null
---

# Camada PRD — Memoria de Produto

## Proposito
Guardar o entendimento acumulado sobre o que se constroi, para quem e sob quais criterios.
Definicao completa em [FND-06 §3.2](../../foundation/06-arquitetura-memoria.md).

## Escopo
| Item | Definicao |
|---|---|
| Pergunta que responde | O que construimos e para quem? |
| Volatilidade | Baixa a media |
| TTL | Vida do produto. Encerrado o produto, a memoria e **arquivada, nao apagada**. |
| Autoridade em conflito | 2 |

## Responsaveis
| Papel | Responsavel |
|---|---|
| Dono | DEP-PRD |
| Escreve | DEP-PRD; DEP-GRW contribui sinal de mercado; DEP-OPS contribui sinal de uso |
| Le (obrigatorio) | DEP-ENG antes de construir · DEP-QAR antes de aceitar · DEP-GRW antes de comunicar |
| Curador | DEP-KMS |

---

## Pertence a esta camada
- Definicao de cada produto: problema, publico, proposta de valor
- Personas, contextos de uso, jornadas
- Requisitos duraveis e criterios de aceite recorrentes
- **Escopo negativo**: o que o produto deliberadamente nao faz, e por que
- Roadmap e sua justificativa; o que foi despriorizado e por que
- Feedback de uso, metricas de produto, hipoteses validadas e invalidadas
- Vocabulario do dominio do produto

## **Nao** pertence
| Conteudo | Vai para |
|---|---|
| Como foi implementado | TEC |
| Estado de uma tarefa | OPR |
| Estrategia da empresa | EST |
| Licao generalizavel alem deste produto | APR |

## Regra de escrita
> Hipotese entra **marcada como hipotese**, com o teste que a confirmaria.

Hipotese invalidada **nao e apagada** — e marcada como refutada, com o que se aprendeu
(MM-09). Saber o que nao funcionou evita repetir a aposta.

## Registros

| ID | Titulo | Produto | Status | Confianca |
|---|---|---|---|---|
| — | *nenhum registro — nenhum produto criado nesta fase* | — | — | — |

Template: [`TPL-memoria`](../../foundation/templates/TPL-memoria.md) ·
Carta de produto: [`TPL-carta-produto`](../../foundation/templates/TPL-carta-produto.md)
