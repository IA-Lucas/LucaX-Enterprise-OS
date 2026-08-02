---
id: TPL-skill
titulo: Template de Skill
tipo: template
versao: 1.0.0
status: ativo
camada_memoria: nao-aplicavel
autor: DEP-GOV
proprietario: DEP-KMS
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0001]
substitui: []
substituido_por: null
---

# Template — Skill

## Proposito
Padronizar capacidades reutilizaveis e nomeadas, conforme [FND-03 §3.5](../03-taxonomia.md).

## Escopo
Procedimento que (a) se repete, (b) tem resultado verificavel e (c) e usavel por mais de um
papel. Faltando qualquer condicao, isto e procedimento interno de uma Carta, nao Skill.

> Skill pertence a **organizacao**, nao a um agente. Skill e o degrau 2 da escada de
> especializacao (FND-02 §9.1) e o principal instrumento de reuso de PI-14.

## Responsaveis
Proprietario: DEP-KMS · Conformidade: DEP-GOV · Aprovacao: DEP-EXE.

## Instrucoes de uso
1. Grave em `skills/SKL-<dominio>-<verbo-objeto>.md`.
2. O nome e sempre acao: `<dominio>-<verbo>-<objeto>`.
3. Declare o ganho PI-14 que a extracao produz e quando ele sera reavaliado.

---
---
id: SKL-<dominio>-<verbo-objeto>
titulo: <o que esta skill faz, em uma linha>
tipo: skill
versao: 1.0.0
status: rascunho
camada_memoria: nao-aplicavel
autor: <DEP-xxx>
proprietario: DEP-KMS
aprovador: DEP-EXE
criado_em: <AAAA-MM-DD>
atualizado_em: <AAAA-MM-DD>
revisao_prevista: <AAAA-MM-DD>
decisoes_relacionadas: [<ADR de criacao>]
substitui: []
substituido_por: null
---

# <Nome da Skill>

## Proposito
<Que resultado esta skill produz. Ate 3 frases.>

## Escopo
| Item | Definicao |
|---|---|
| Aplica-se quando | |
| **Nao** se aplica quando | |
| Papeis que podem usar | |

## Responsaveis
| Papel | Quem |
|---|---|
| Proprietario | DEP-KMS |
| Autor | |
| Aprovador | DEP-EXE |

## 1. Quando usar
| Gatilho | Sinal de que esta skill e a certa |
|---|---|

## 2. Quando NAO usar
| Situacao | O que usar em vez disso |
|---|---|

## 3. Entradas
| Entrada | Obrigatoria? | Origem tipica |
|---|---|---|

## 4. Procedimento
| # | Passo | Resultado do passo | Como verificar |
|---|---|---|---|
| 1 | | | |

## 5. Saidas
| Saida | Formato | Destino tipico |
|---|---|---|

## 6. Criterio de sucesso
<Como se verifica que a skill foi executada corretamente. Verificavel por terceiro.>

## 7. Modos de falha conhecidos
| Falha | Como reconhecer | O que fazer |
|---|---|---|

## 8. Normas aplicaveis
| Norma | Como se manifesta nesta skill |
|---|---|

## 9. Ganho PI-14
| Campo | Conteudo |
|---|---|
| Ganho declarado | organizacao / reuso / reducao de contexto |
| Sinal observado que motivou a extracao | |
| Quantos papeis a utilizam hoje | |
| Data de reavaliacao do ganho | |

## 10. Criterio de descontinuacao
<Quando esta skill deixa de ser necessaria ou deve ser reabsorvida (FND-02 §9.3).>

## 11. Rastreabilidade
| Campo | Conteudo |
|---|---|
| ADR de criacao | |
| Origem (registro APR, repeticao observada) | |
