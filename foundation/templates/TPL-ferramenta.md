---
id: TPL-ferramenta
titulo: Template de Ficha de Ferramenta
tipo: template
versao: 1.0.0
status: ativo
camada_memoria: nao-aplicavel
autor: DEP-GOV
proprietario: DEP-TLS
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0001]
substitui: []
substituido_por: null
---

# Template — Ficha de Ferramenta

## Proposito
Padronizar o registro de capacidades externas usadas pela organizacao, conforme
[FND-03 §3.12](../03-taxonomia.md).

## Escopo
Todo servico, API, MCP, aplicacao de terceiro ou fonte de dados externa adotada
oficialmente. Adocao e mudanca C2, Tipo 1 — cria dependencia.

> **Credencial nunca aparece nesta ficha.** Apenas o nome da variavel de ambiente que a
> contem (PI-08, LV-02).

## Responsaveis
Proprietario: DEP-TLS · Risco: DEP-QAR · Aprovacao: DEP-EXE · Ratificacao: SOBERANO.

## Instrucoes de uso
1. Grave em `tools/TOL-<classe>-<slug>.md`. Classes: `mcp`, `api`, `saas`, `local`, `dados`.
2. Aplique PI-11: o criterio primario e o resultado para a tarefa; custo e restricao
   declarada, nao criterio dominante.
3. Criterio de descarte e obrigatorio na adocao (DP-05).

---
---
id: TOL-<classe>-<slug>
titulo: <Nome da Ferramenta>
tipo: ferramenta
versao: 1.0.0
status: rascunho
camada_memoria: tecnica
autor: DEP-TLS
proprietario: DEP-TLS
aprovador: DEP-EXE
criado_em: <AAAA-MM-DD>
atualizado_em: <AAAA-MM-DD>
revisao_prevista: <AAAA-MM-DD>
decisoes_relacionadas: [<ADR de adocao>]
substitui: []
substituido_por: null
classe: <mcp|api|saas|local|dados>
dado_trafegado: <nenhum|publico|interno|sensivel>
custo: <descricao do custo, recorrente ou nao>
criticidade: <baixa|media|alta>
---

# <Nome da Ferramenta> (TOL-<classe>-<slug>)

## Proposito
<Para que a organizacao usa esta ferramenta. Ate 3 frases.>

## Escopo
| Item | Definicao |
|---|---|
| Usos autorizados | |
| Usos **nao** autorizados | |
| Quem pode usar | |

## Responsaveis
| Papel | Quem |
|---|---|
| Proprietario | DEP-TLS |
| Avaliacao de risco | DEP-QAR |
| Aprovador | DEP-EXE |

## 1. Finalidade
<Que problema esta ferramenta resolve para a organizacao.>

## 2. Alternativas avaliadas
| Alternativa | Por que nao foi escolhida |
|---|---|
| Nao usar ferramenta alguma | |

## 3. Dado que trafega
| Tipo de dado | Sensibilidade | Sai do ambiente do Soberano? | Autorizacao correspondente |
|---|---|---|---|

> Envio de dado a servico externo e ato de exposicao: exige autorizacao especifica, nao
> geral (EX-03, LV-08).

## 4. Acesso e segredo
| Campo | Conteudo |
|---|---|
| Nome da variavel de ambiente | `<NOME_DA_VARIAVEL>` |
| Onde a credencial e guardada | <cofre / variavel de ambiente> |
| Quem pode rotacionar | |

> **Nunca** escrever aqui o valor da credencial (PI-08).

## 5. Custo
| Campo | Conteudo |
|---|---|
| Modelo de cobranca | |
| Custo recorrente | |
| Limite definido | |
| Quem monitora | DEP-EXE (funcao Recursos) |

## 6. Dependencia e risco
| Campo | Conteudo |
|---|---|
| Criticidade | baixa / media / alta |
| O que quebra se a ferramenta cair | |
| Plano de contingencia | |
| Lock-in criado | |

## 7. Limites de uso
| Limite | Valor | Consequencia de ultrapassar |
|---|---|---|

## 8. Criterio de descarte
> Obrigatorio (DP-05). Quando esta ferramenta deixa de valer a pena.

| Condicao | Sinal observavel | Substituto previsto |
|---|---|---|

## 9. Avaliacao PI-11
| Campo | Conteudo |
|---|---|
| Por que esta e a melhor opcao **para a tarefa** | |
| Custo declarado como restricao | |
| Qualidade que se ganha em relacao a alternativa | |

## 10. Rastreabilidade
| Campo | Conteudo |
|---|---|
| ADR de adocao | |
| Ratificacao do Soberano (data) | |
| Revisao prevista | |
