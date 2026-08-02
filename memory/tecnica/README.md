---
id: IDX-mem-tecnica
titulo: Camada Tecnica da Memoria
tipo: relatorio
versao: 1.0.0
status: ativo
camada_memoria: tecnica
autor: DEP-GOV
proprietario: DEP-ENG
aprovador: DEP-KMS
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: null
decisoes_relacionadas: [ADR-0001]
substitui: []
substituido_por: null
---

# Camada TEC — Memoria Tecnica

## Proposito
Guardar como o sistema esta construido e, sobretudo, **por que assim** — para que a proxima
mudanca nao repita analise ja feita. Definicao completa em
[FND-06 §3.3](../../foundation/06-arquitetura-memoria.md).

## Escopo
| Item | Definicao |
|---|---|
| Pergunta que responde | Como esta feito e por que assim? |
| Volatilidade | Media |
| TTL | Vida do componente que descreve |
| Autoridade em conflito | 3 |

## Responsaveis
| Papel | Responsavel |
|---|---|
| Dono | DEP-ENG |
| Escreve | DEP-ENG; DEP-TLS (dependencias externas); DEP-QAR (achados estruturais) |
| Le (obrigatorio) | DEP-ENG antes de qualquer mudanca · DEP-QAR · DEP-OPS |
| Curador | DEP-KMS |

---

## Pertence a esta camada
- Arquitetura vigente, componentes e suas fronteiras
- Padroes tecnicos adotados **e proibidos**
- Justificativa das escolhas tecnicas — apontando para os ADRs (MM-07)
- Modelo de dados e contratos de integracao
- Divida tecnica conhecida: o que e, por que foi assumida, o que custa
- Restricoes tecnicas, limites conhecidos, armadilhas do stack
- Dependencias externas e seu risco
- **Caminhos ja tentados e descartados, com o motivo**

## **Nao** pertence
| Conteudo | Vai para |
|---|---|
| O que construir | PRD |
| Incidente ou estado corrente | OPR |
| Licao generalizavel para outros contextos | APR |
| **Credencial** | Lugar nenhum — proibido (PI-08) |

## Regra de escrita
> Registro tecnico **sem o porque** e incompleto.

"Usamos X" nao e memoria tecnica.
"Usamos X porque Y, tendo descartado Z por W" e.

O valor desta camada nao esta em descrever o estado — o codigo ja faz isso. Esta em
preservar o **raciocinio** que produziu o estado, que o codigo nao guarda.

## Registros

| ID | Titulo | Componente | Status | Confianca |
|---|---|---|---|---|
| — | *nenhum registro — nenhum componente construido nesta fase* | — | — | — |

Template: [`TPL-memoria`](../../foundation/templates/TPL-memoria.md) ·
Ferramentas: [`TPL-ferramenta`](../../foundation/templates/TPL-ferramenta.md)
