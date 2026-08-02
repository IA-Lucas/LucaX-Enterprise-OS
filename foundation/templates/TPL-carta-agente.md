---
id: TPL-carta-agente
titulo: Template de Carta de Agente e Subagente
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

# Template — Carta de Agente / Subagente

## Proposito
Dar existencia formal a um agente ou subagente, com departamento de origem, escopo, limites
e nivel de autonomia, conforme [FND-03 §3.3](../03-taxonomia.md) e [FND-04 §6](../04-governanca.md).

## Escopo
Criacao e alteracao de agente e subagente. Mudanca C2.

> **Nesta fase da fundacao nenhum agente pode ser criado.** Este template existe para que a
> fase seguinte comece com o padrao pronto, nao para ser usado agora.

## Responsaveis
Proprietario: departamento de origem · Conformidade: DEP-GOV · Aprovacao: DEP-EXE.

## Instrucoes de uso
1. Agente: `departments/<dep>/agents/AGT-<dep>-<papel>.md`.
   Subagente: `departments/<dep>/agents/sub/SUB-<dep>-<papel>.md`.
2. Autonomia do agente e sempre **menor ou igual** a do departamento (FND-02).
3. Autonomia do subagente e sempre **menor ou igual** a do agente pai.
4. Profundidade maxima e 1: **subagente nao tem subagente** (IV-04).
5. A secao **O que nao me compete** e obrigatoria — e a defesa contra PI-09.

---
---
id: <AGT-<DEP>-<papel> | SUB-<DEP>-<papel>>
titulo: <Nome do papel>
tipo: carta
versao: 1.0.0
status: rascunho
camada_memoria: nao-aplicavel
autor: <DEP-xxx>
proprietario: <DEP-xxx>
aprovador: DEP-EXE
criado_em: <AAAA-MM-DD>
atualizado_em: <AAAA-MM-DD>
revisao_prevista: <AAAA-MM-DD>
decisoes_relacionadas: [<ADR de criacao>]
substitui: []
substituido_por: null
departamento: <DEP-xxx>
nivel_autonomia: <A0|A1|A2|A3>
agente_pai: <AGT-id | null>
---

# <Nome do papel>

## Proposito
<Que resultado este papel produz. Ate 3 frases.>

## Escopo
| Item | Definicao |
|---|---|
| Departamento de origem | |
| Agente pai (se subagente) | |
| Nivel de autonomia | |
| Autonomia do departamento | <deve ser >= a deste papel> |

## Responsaveis
| Papel | Quem |
|---|---|
| Proprietario | <departamento de origem> |
| Aprovador | DEP-EXE |
| Guardiao normativo | DEP-GOV |

## 1. Missao
<Uma frase.>

## 2. O que faco
| # | Atividade | Resultado esperado | Como se verifica |
|---|---|---|---|

## 3. O que NAO me compete
> Secao obrigatoria. Sem ela, a carta nao e aprovada.

| Materia | Dono real | O que faco em vez disso |
|---|---|---|

## 4. Entradas que recebo
| Entrada | De quem | Canal (FND-05 §2) | Contexto minimo necessario |
|---|---|---|---|

## 5. Saidas que produzo
| Saida | Para quem | Canal | Formato |
|---|---|---|---|

## 6. Contexto minimo (PI-14)
> Apenas o que a execucao usa. Item que a tarefa nao consome nao entra (PC-02).

| Camada / fonte | O que preciso | Por que preciso |
|---|---|---|

## 7. Limites de autonomia
| Situacao | Posso decidir? | Se nao, escalo para |
|---|---|---|
| Decisao Tipo 2 no meu dominio | | |
| Decisao Tipo 1 | **Nunca** | SOBERANO (via departamento) |
| Desvio de escopo | **Nunca** | Proprietario |
| Conflito com norma | **Nunca** | DEP-GOV |

## 8. Quando devolvo trabalho
> Motivos legitimos de devolucao de handoff (HO-02).

- [ ] Escopo insuficiente
- [ ] Contexto insuficiente
- [ ] Fora do meu dominio
- [ ] Conflito com norma vigente
- [ ] Dependencia nao resolvida

## 9. Quando escalo
| Gatilho | Nivel (FND-05 §7.1) | Para quem |
|---|---|---|

## 10. Ferramentas autorizadas
| Ferramenta (TOL-id) | Para que | Limite de uso |
|---|---|---|

> Credencial nunca aparece aqui — apenas o nome da variavel de ambiente (PI-08).

## 11. Skills que utilizo
| Skill (SKL-id) | Quando |
|---|---|

## 12. Criterio de sucesso
| Metrica | Direcao |
|---|---|

## 13. Criterio de extincao ou especializacao
<Como saberemos que este papel deixou de ser necessario, deve ser dividido (PI-14) ou
reunificado (FND-02 §9.3).>

## 14. Rastreabilidade
| Campo | Conteudo |
|---|---|
| ADR de criacao | |
| Ganho PI-14 declarado na criacao | |
| Data de reavaliacao do ganho | |
