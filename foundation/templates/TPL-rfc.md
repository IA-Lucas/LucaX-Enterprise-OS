---
id: TPL-rfc
titulo: Template de Proposta (RFC)
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

# Template — RFC

## Proposito
Padronizar propostas submetidas a analise antes de virarem decisao, conforme
[FND-07 §3.1](../07-framework-decisoes.md).

## Escopo
Obrigatorio para mudanca C3. Regra para C2. Nao se usa para decisao ja tomada (use ADR)
nem para escolha local (use Nota de Decisao).

## Responsaveis
Proprietario: DEP-GOV · Analise de conformidade: DEP-GOV · Analise de risco: DEP-QAR.

## Instrucoes de uso
1. Copie para `rfcs/RFC-<NNNN>-<slug>.md`. Numero atribuido por DEP-GOV.
2. RFC pode ser rejeitada — isso e resultado valido, nao fracasso.
3. RFC rejeitada vai para `arquivado` e **nunca e apagada**.
4. RFC aceita gera ADR pelo rito de FND-07 §5.

---
---
id: RFC-<NNNN>-<slug>
titulo: <a pergunta ou proposta em uma linha>
tipo: rfc
versao: 1.0.0
status: rascunho
camada_memoria: nao-aplicavel
autor: <DEP-xxx>
proprietario: <DEP-xxx>
aprovador: <DEP-EXE | SOBERANO>
criado_em: <AAAA-MM-DD>
atualizado_em: <AAAA-MM-DD>
revisao_prevista: null
decisoes_relacionadas: []
substitui: []
substituido_por: null
classe_mudanca: <C2|C3>
prazo_analise: <AAAA-MM-DD>
---

# RFC-<NNNN>: <Titulo>

## Proposito
<O que esta proposta busca resolver, em ate 3 frases.>

## Escopo
<O que a proposta abrange. O que deliberadamente nao abrange.>

## Responsaveis
| Papel | Quem |
|---|---|
| Proponente | |
| Areas que devem se manifestar | |
| Aprovador | |
| Prazo de manifestacao | |

## 1. Situacao atual
<Como as coisas funcionam hoje. Fatos verificaveis.>

## 2. Problema
<O que esta ruim, para quem, e com que consequencia. Evidencia do problema.>

## 3. Pergunta de decisao
<A pergunta exata que esta RFC quer ver respondida.>

## 4. Criterios de avaliacao
| # | Criterio | Peso | Como se mede |
|---|---|---|---|

## 5. Opcoes
### Opcao A — <nome>
| Campo | Conteudo |
|---|---|
| Descricao | |
| A favor / Contra | |
| Custo / Risco | |
| Quem e afetado | |

### Opcao B — <nome>
<mesma estrutura>

### Opcao Z — Nao fazer nada
| Campo | Conteudo |
|---|---|
| Consequencia de manter o estado atual | |
| Custo da inacao | |

## 6. Recomendacao do proponente
<Qual opcao e por que. Recomendacao e obrigatoria: RFC sem recomendacao e devolvida (EC-03).>

## 7. Impacto previsto
| Dimensao | Impacto |
|---|---|
| Departamentos | |
| Componentes | |
| Normas afetadas | |
| Camadas de memoria | |
| Ganho PI-14 pretendido e sinal que o comprova | |

## 8. Riscos
| # | Risco | Impacto | Mitigacao |
|---|---|---|---|

## 9. Perguntas em aberto
<O que ainda nao se sabe e precisa ser respondido antes de decidir.>

## 10. Manifestacoes
| Area | Posicao (apoia / objeta / abstem) | Fundamento | Data |
|---|---|---|---|

## 11. Resultado
| Campo | Conteudo |
|---|---|
| Decisao | aceita / aceita com ajuste / rejeitada / adiada |
| ADR gerado | |
| Se rejeitada, por que | |
| Se adiada, ate quando e sob qual condicao | |
| Data | |
| Responsavel | |
