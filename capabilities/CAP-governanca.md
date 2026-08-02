---
id: CAP-governanca
titulo: Governanca Organizacional
tipo: capability
versao: 1.1.0
status: ativo
camada_memoria: estrategica
autor: DEP-EXE
proprietario: DEP-EXE
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0002, ADR-0005]
substitui: []
substituido_por: null
dominio: DIR
classe: nucleo
maturidade: emergente
custodio: DEP-GOV
exercentes: [DEP-GOV]
depende_de: [CAP-conhecimento]
consumida_por: [CAP-estrategia, CAP-qualidade, CAP-seguranca, CAP-juridico]
especializa: null
---

# Governanca Organizacional (CAP-governanca)

## Proposito
Manter a integridade normativa do sistema: garantir que nada exista, mude ou desapareca sem
responsavel, instrumento proporcional ao risco e registro localizavel. E a competencia que
torna a organizacao **auditavel** (Visao V4).

## Escopo
A competencia de classificar mudancas por risco, exigir o instrumento correto, verificar
conformidade, atribuir identidade oficial aos artefatos e barrar o que viola norma vigente.

| Item | Definicao |
|---|---|
| Dominio | `DIR` — Direcao |
| Classe estrategica | `nucleo` |
| Maturidade | `emergente` |
| Custodio | DEP-GOV |
| Exercentes | DEP-GOV |

## Responsaveis
| Papel | Quem |
|---|---|
| Custodio (unico) | DEP-GOV |
| Exercentes | DEP-GOV |
| Autoridade de evolucao | DEP-GOV, com parecer do SOBERANO |
| Ratificador | SOBERANO |

---

## 1. Identidade (A-01)
| Campo | Valor |
|---|---|
| ID | `CAP-governanca` |
| Nome | Governanca Organizacional |
| Dominio | DIR |
| Classe | nucleo |
| Maturidade | emergente |
| Especializa | nenhuma |

## 2. Missao (A-03)
> Garantir que qualquer mudanca no sistema possa ser rastreada ate seu responsavel, sua
> data, sua justificativa e sua evidencia — sem depender da memoria de ninguem.

## 3. Limites (A-05)
| **Nao** abrange | Pertence a |
|---|---|
| Julgar merito tecnico de uma solucao | `CAP-arquitetura` / `CAP-engenharia` |
| Julgar se a entrega tem qualidade suficiente | `CAP-qualidade` |
| Definir prioridade e alocacao | `CAP-coordenacao` |
| Definir escopo de produto | `CAP-produto` |
| Conformidade com norma **externa** (lei, contrato, regulacao) | `CAP-juridico` |
| Guardar e recuperar o registro | `CAP-conhecimento` |

> **Fronteira com `CAP-juridico`:** esta Capability zela pela norma **interna** do LucaX;
> aquela, pela norma **externa** imposta de fora.

## 4. Responsabilidades (A-06)
| # | A organizacao e capaz de... |
|---|---|
| R1 | Classificar qualquer mudanca por impacto e reversibilidade antes de executa-la |
| R2 | Exigir o instrumento proporcional ao risco, nem mais nem menos |
| R3 | Atribuir identidade oficial e unica a cada artefato |
| R4 | Verificar conformidade e barrar o que viola norma vigente |
| R5 | Detectar e registrar violacao, com causa e correcao |
| R6 | Conceder e fiscalizar excecoes formais com prazo |
| R7 | Manter coerencia entre normas ao longo do tempo |

## 5. Entradas (A-07)
| Entrada | Origem | Obrigatoria? |
|---|---|---|
| Propostas de mudanca | todas as Capabilities | Sim |
| Historico normativo e precedentes | `CAP-conhecimento` | Sim |
| Determinacao do Soberano | externa (Soberano) | Sim |

## 6. Saidas (A-08)
| Saida | Consumida por |
|---|---|
| Parecer de conformidade | todas |
| Identidade oficial (ID, numeracao) | todas |
| Veto fundamentado | todas |
| Registro de excecao e de incidente | `CAP-conhecimento`, `CAP-aprendizado-organizacional` |
| Norma vigente e sua interpretacao | todas |

## 7. Artefatos produzidos (A-09)
| Tipo de artefato | Exemplo |
|---|---|
| ADR / RFC | Registro e numeracao oficiais |
| Excecao (`EXC`) | Autorizacao temporaria com prazo |
| Incidente (`INC`) | Violacao detectada e sua causa |
| Documento fundacional (`FND`) | Norma organizacional |
| Relatorio | Auditoria de conformidade |

## 8. Dependencias (A-10)
| Capability | Relacao | Por que |
|---|---|---|
| `CAP-conhecimento` | depende-de | Sem registro recuperavel nao ha rastreabilidade |

## 9. Consumidores (A-11)
| Capability | Relacao | O que consome |
|---|---|---|
| `CAP-estrategia` | depende-de | O rito que da eficacia as decisoes de direcao |
| `CAP-qualidade` | depende-de | A norma contra a qual verifica |
| `CAP-seguranca` | depende-de | O rito de excecao e incidente |
| `CAP-juridico` | depende-de | O instrumento de registro |
| todas **as demais** | verifica *(inversa)* | Esta Capability verifica a conformidade de todas as demais — **nunca a si propria** (RM-06b, LV-03). O que DEP-GOV produz e verificado pelo revisor independente da mudanca e, em materia constitucional, pelo Soberano *(ADR-0005)* |

## 10. Indicadores (A-12)
| # | Indicador | Direcao | Como se mede | Estado |
|---|---|---|---|---|
| I1 | Artefatos que respondem as 7 perguntas de rastreabilidade sem consultar pessoa | → 100% | Auditoria (FND-04 §5) | **100%** (40/40, 2026-07-28) |
| I2 | Decisoes relevantes com instrumento correspondente | → 100% | Comparacao decisao × ADR/Nota | **100%** (2/2) |
| I3 | Excecoes vencidas nao regularizadas | → 0 | Varredura em `governance/exceptions/` | **0** |
| I4 | Incidentes com causa corrigida, nao so efeito | → 100% | Fechamento verificado por DEP-QAR | sem ocorrencia |
| I5 | Mudancas executadas antes do registro (C2/C3) | → 0 | Auditoria de ordem | **0** |

## 11. Criterios de evolucao (A-13)
| Movimento | Gatilho | Ganho PI-14 |
|---|---|---|
| Especializar | Volume de auditoria tornar a verificacao gargalo do fluxo | Organizacao |
| Especializar | Conformidade interna e gestao de risco divergirem em natureza | Organizacao |
| Fundir | Deixar de ser distinguivel de `CAP-qualidade` na pratica | Organizacao |
| Depreciar | **Nunca** — a competencia sustenta PI-03 e a Visao V4 |

## 12. Historico de maturidade
| Data | De | Para | Evidencia | Instrumento |
|---|---|---|---|---|
| 2026-07-28 | proposta | experimental | Catalogo aprovado | ADR-0002 |
| 2026-07-28 | experimental | emergente | Exercida com resultado registrado: 2 ADRs, 1 RFC, taxonomia aplicada a 40 artefatos, auditoria de conformidade executada com 100% de aprovacao | ADR-0002 |

## 13. Rastreabilidade
| Campo | Conteudo |
|---|---|
| ADR de criacao | ADR-0002 |
| RFC de origem | RFC-0001 |
| Normas que exerce | [FND-01](../foundation/01-constituicao.md), [FND-03](../foundation/03-taxonomia.md), [FND-04](../foundation/04-governanca.md), [FND-07](../foundation/07-framework-decisoes.md) |
| Componentes vinculados | nenhum ainda |
