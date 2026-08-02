---
id: CAP-conhecimento
titulo: Conhecimento
tipo: capability
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-EXE
proprietario: DEP-EXE
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0002]
substitui: []
substituido_por: null
dominio: COG
classe: nucleo
maturidade: experimental
custodio: DEP-KMS
exercentes: [DEP-KMS]
depende_de: []
consumida_por: [CAP-governanca, CAP-comunicacao, CAP-aprendizado-organizacional, CAP-estrategia, CAP-pesquisa, CAP-engenharia-de-agentes]
especializa: null
---

# Conhecimento (CAP-conhecimento)

## Proposito
Fazer com que a organizacao **saiba o que ja sabe**: capturar, alocar, curar e devolver
conhecimento no momento em que ele muda uma decisao. Sem esta competencia, cada trabalho
recomeca do zero e a Visao V2 (memoria que compoe) e impossivel.

## Escopo
A competencia de transformar fato, experiencia e decisao em registro localizavel,
confiavel e recuperavel — e de devolver, sob demanda, o **minimo suficiente** para agir.

| Item | Definicao |
|---|---|
| Dominio | `COG` — Cognicao Organizacional |
| Classe estrategica | `nucleo` |
| Maturidade | `experimental` |
| Custodio | DEP-KMS |
| Exercentes | DEP-KMS (curadoria); todos contribuem conteudo |

## Responsaveis
| Papel | Quem |
|---|---|
| Custodio (unico) | DEP-KMS |
| Exercentes | DEP-KMS |
| Autoridade de evolucao | DEP-KMS, com parecer de DEP-GOV |
| Ratificador | SOBERANO |

---

## 1. Identidade (A-01)
| Campo | Valor |
|---|---|
| ID | `CAP-conhecimento` |
| Nome | Conhecimento |
| Dominio | COG |
| Classe | nucleo |
| Maturidade | experimental |
| Especializa | nenhuma |

## 2. Missao (A-03)
> Garantir que nenhuma informacao que mudaria uma decisao esteja indisponivel no momento
> em que a decisao e tomada.

## 3. Limites (A-05)
| **Nao** abrange | Pertence a |
|---|---|
| Extrair licao de experiencia vivida | `CAP-aprendizado-organizacional` |
| Transferir trabalho e contexto entre partes | `CAP-comunicacao` |
| Julgar o merito do conteudo registrado | a Capability dona do dominio do conteudo |
| Definir a norma sobre o que e obrigatorio registrar | `CAP-governanca` |
| Modelar e persistir dados de produto | `CAP-dados` |

> **Fronteira com `CAP-comunicacao`:** a montagem e a curadoria do Pacote de Contexto sao
> desta Capability; o **protocolo de transferencia** (canal, envelope, aceite) e daquela.

## 4. Responsabilidades (A-06)
| # | A organizacao e capaz de... |
|---|---|
| R1 | Decidir a qual camada de memoria um fato pertence, sem duplicar |
| R2 | Registrar com proveniencia verificavel: origem, autor, data, evidencia, confianca |
| R3 | Recuperar o contexto minimo suficiente para uma tarefa especifica |
| R4 | Detectar duplicidade, contradicao e registro sem proveniencia |
| R5 | Promover, rebaixar e expirar registros conforme evidencia |
| R6 | Responder "nao encontrei" com seguranca, em vez de inventar |

## 5. Entradas (A-07)
| Entrada | Origem | Obrigatoria? |
|---|---|---|
| Decisoes registradas | `CAP-governanca` | Sim |
| Reportes de trabalho concluido | todas as Capabilities | Sim |
| Licoes consolidadas | `CAP-aprendizado-organizacional` | Sim |
| Sinais externos e fontes de terceiros | `CAP-pesquisa` | Nao |

## 6. Saidas (A-08)
| Saida | Consumida por |
|---|---|
| Pacote de contexto curado | todas as Capabilities |
| Registro de memoria com proveniencia | todas |
| Alerta de contradicao ou duplicidade | `CAP-governanca` |
| Indice organizacional | todas |

## 7. Artefatos produzidos (A-09)
| Tipo de artefato | Exemplo |
|---|---|
| Memoria (`MEM`) | Registro em qualquer das cinco camadas |
| Relatorio | Indice, sintese, alerta de contradicao |

## 8. Dependencias (A-10)
| Capability | Relacao | Por que |
|---|---|---|
| — | — | Capability de base: nao depende de nenhuma outra |

## 9. Consumidores (A-11)
| Capability | Relacao | O que consome |
|---|---|---|
| `CAP-governanca` | depende-de | Registro e proveniencia das decisoes |
| `CAP-comunicacao` | depende-de | Conteudo curado do pacote de contexto |
| `CAP-aprendizado-organizacional` | depende-de | Base sobre a qual a licao se assenta |
| `CAP-estrategia` | depende-de | Historico que sustenta a direcao |
| `CAP-pesquisa` | depende-de | O que ja se sabe, para nao repesquisar |
| `CAP-engenharia-de-agentes` | depende-de | Contexto que alimenta os executores |

## 10. Indicadores (A-12)
| # | Indicador | Direcao | Como se mede | Estado |
|---|---|---|---|---|
| I1 | Taxa de recuperacao: registros usados / registros existentes | ↑ | Consultas registradas vs. catalogo | nao medido |
| I2 | Registros com proveniencia completa | → 100% | Auditoria de frontmatter | nao medido |
| I3 | Contradicoes abertas | → 0 | Varredura de curadoria | nao medido |
| I4 | Volume de contexto por consulta | ↓ | Tamanho do nucleo do pacote | nao medido |
| I5 | Decisoes tomadas sem consulta previa a memoria | → 0 | Verificacao em QG-0 | nao medido |

## 11. Criterios de evolucao (A-13)
| Movimento | Gatilho | Ganho PI-14 |
|---|---|---|
| Especializar | Uma camada acumula registros de naturezas nitidamente distintas | Organizacao |
| Especializar | Montagem de contexto recorrente para o mesmo tipo de tarefa | Reducao de contexto |
| Fundir | Curadoria e transferencia deixarem de ser distinguiveis na pratica | Organizacao |
| Depreciar | **Nunca sem emenda C3** — classe `nucleo` (CL-05) |

## 12. Historico de maturidade
| Data | De | Para | Evidencia | Instrumento |
|---|---|---|---|---|
| 2026-07-28 | proposta | experimental | Catalogo aprovado; arquitetura de memoria definida em FND-06, ainda sem registros curados | ADR-0002 |

## 13. Rastreabilidade
| Campo | Conteudo |
|---|---|
| ADR de criacao | ADR-0002 |
| RFC de origem | RFC-0001 |
| Normas que exerce | [FND-06](../foundation/06-arquitetura-memoria.md) |
| Componentes vinculados | nenhum ainda |
