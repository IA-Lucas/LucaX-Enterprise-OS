---
id: CAP-qualidade
titulo: Qualidade
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
dominio: GAR
classe: nucleo
maturidade: experimental
custodio: DEP-QAR
exercentes: [DEP-QAR]
depende_de: [CAP-governanca, CAP-aprendizado-organizacional]
consumida_por: []
especializa: null
---

# Qualidade (CAP-qualidade)

## Proposito
Assegurar, por verificacao independente, que o que a organizacao entrega esta correto e
defensavel. E a competencia que realiza a Visao V3: qualidade produzida pela estrutura, nao
pela atencao momentanea do humano.

## Escopo
A competencia de verificar de forma adversarial e independente: confrontar entrega com
criterio, exigir evidencia, encontrar o defeito que o produtor nao viu e vetar o que nao
passa.

| Item | Definicao |
|---|---|
| Dominio | `GAR` — Garantia |
| Classe estrategica | `nucleo` |
| Maturidade | `experimental` |
| Custodio | DEP-QAR *(classe Guarda, conforme OW-05)* |
| Exercentes | DEP-QAR |

## Responsaveis
| Papel | Quem |
|---|---|
| Custodio (unico) | DEP-QAR |
| Exercentes | DEP-QAR |
| Autoridade de evolucao | DEP-QAR, com parecer de DEP-GOV |
| Ratificador | SOBERANO |

---

## 1. Identidade (A-01)
| Campo | Valor |
|---|---|
| ID | `CAP-qualidade` |
| Nome | Qualidade |
| Dominio | GAR |
| Classe | nucleo |
| Maturidade | experimental |
| Especializa | nenhuma |

## 2. Missao (A-03)
> Garantir que nada saia da organizacao afirmando funcionar sem que alguem independente
> tenha verificado que funciona.

## 3. Limites (A-05)
| **Nao** abrange | Pertence a |
|---|---|
| Definir o que construir e qual o criterio de valor | `CAP-produto` |
| Decidir como construir | `CAP-arquitetura` / `CAP-engenharia` |
| Verificar conformidade com norma **interna** | `CAP-governanca` |
| Proteger contra ameaca e controlar acesso | `CAP-seguranca` |
| Conformidade com norma **externa** | `CAP-juridico` |
| **Produzir** o que verifica | qualquer Capability de realizacao (PI-05) |
| Extrair a licao do defeito encontrado | `CAP-aprendizado-organizacional` |

> **Fronteira intransponivel (PI-05, ES-02, LV-03):** esta Capability **nunca** e exercida
> por quem produziu o artefato. Custodia obrigatoriamente na Guarda (OW-05). Verificacao
> exercida pelo produtor nao e qualidade — e autoaprovacao.
>
> **Fronteira com `CAP-governanca`:** aquela verifica **forma e conformidade**; esta,
> **conteudo e correcao**. Um ADR pode estar perfeitamente conforme e conter decisao errada.

## 4. Responsabilidades (A-06)
| # | A organizacao e capaz de... |
|---|---|
| R1 | Confrontar entrega com criterio de aceite, sem indulgencia |
| R2 | Exigir evidencia e recusar "feito" como prova |
| R3 | Procurar o defeito de forma adversarial, tentando refutar a entrega |
| R4 | Avaliar risco e decidir o que exige aprovacao humana |
| R5 | Vetar entrega que nao atende, com fundamento registrado |
| R6 | Verificar que backup e plano de reversao existem e funcionam |
| R7 | Distinguir decisao boa de resultado bom |
| R8 | Reconhecer antipadroes de decisao e de execucao |

## 5. Entradas (A-07)
| Entrada | Origem | Obrigatoria? |
|---|---|---|
| Artefato a verificar | qualquer Capability de realizacao | Sim |
| Criterios de aceite | `CAP-produto` | Sim |
| Norma vigente | `CAP-governanca` | Sim |
| Antipadroes e falhas conhecidas | `CAP-aprendizado-organizacional` | Sim |
| Metodo de avaliacao de saida de IA | `CAP-inteligencia-artificial` | Nao |

## 6. Saidas (A-08)
| Saida | Consumida por |
|---|---|
| Parecer de revisao: passa ou devolve | Capability produtora, `CAP-coordenacao` |
| Lista de defeitos com evidencia | Capability produtora |
| Laudo de risco | `CAP-coordenacao`, Soberano |
| Veto fundamentado | todas |
| Verificacao de backup e reversao | `CAP-operacoes` |
| Materia-prima de licao | `CAP-aprendizado-organizacional` |

## 7. Artefatos produzidos (A-09)
| Tipo de artefato | Exemplo |
|---|---|
| Relatorio | Parecer de revisao, laudo de risco |
| Memoria (`MEM-TEC`) | Achado estrutural recorrente |
| ADR | Decisao de padrao de aceite |

## 8. Dependencias (A-10)
| Capability | Relacao | Por que |
|---|---|---|
| `CAP-governanca` | depende-de | Verificar exige norma contra a qual comparar |
| `CAP-aprendizado-organizacional` | depende-de | Sem antipadroes conhecidos, a revisao redescobre tudo |

## 9. Consumidores (A-11)
| Capability | Relacao | O que consome |
|---|---|---|
| `CAP-engenharia` | verifica | Esta Capability verifica a saida daquela |
| `CAP-arquitetura` | verifica | Idem |
| `CAP-produto` | verifica | Idem |
| `CAP-dados` | verifica | Idem |
| `CAP-engenharia-de-agentes` | verifica | Idem |
| `CAP-aprendizado-organizacional` | fornece-para | Defeitos e vereditos como materia-prima |

> Nenhuma Capability `depende-de` esta, por desenho: a Guarda nao pode ser dependencia
> estrutural de quem ela verifica (RL-05).

## 10. Indicadores (A-12)
| # | Indicador | Direcao | Como se mede | Estado |
|---|---|---|---|---|
| I1 | Taxa de reprovacao em QG-3 | **estavel e nao-zero** | Registro de revisao | nao medido |
| I2 | Defeitos que escaparam da revisao e apareceram depois | ↓ | Postmortem | nao medido |
| I3 | Entregas aceitas sem evidencia verificada | → 0 | Auditoria de parecer | nao medido |
| I4 | Vetos revertidos pelo Soberano | ↓ | Registro de reversao de veto | nao medido |
| I5 | Verificacoes feitas por quem produziu | → 0 | Auditoria de papeis (LV-03) | **0** |
| I6 | Planos de reversao verificados como executaveis | → 100% | Registro em QG-4 | nao medido |

> **I1 merece leitura cuidadosa:** reprovacao **zero** e sinal de alerta, nao de excelencia
> — indica revisao complacente ou nao independente (FND-01 §6.3).

## 11. Criterios de evolucao (A-13)
| Movimento | Gatilho | Ganho PI-14 |
|---|---|---|
| Especializar | Verificacao de artefato e analise de risco divergirem em metodo | Organizacao |
| Especializar | Avaliacao de saida de agentes exigir tecnica propria | Reducao de contexto |
| Fundir | Deixar de ser distinguivel de `CAP-seguranca` na pratica | Organizacao |
| Depreciar | **Nunca sem emenda C3** — classe `nucleo`; sustenta a Visao V3 (CL-05) |

## 12. Historico de maturidade
| Data | De | Para | Evidencia | Instrumento |
|---|---|---|---|---|
| 2026-07-28 | proposta | experimental | Catalogo aprovado; nenhuma entrega de produto verificada — as auditorias ate aqui foram de conformidade, exercicio de `CAP-governanca` | ADR-0002 |

## 13. Rastreabilidade
| Campo | Conteudo |
|---|---|
| ADR de criacao | ADR-0002 |
| RFC de origem | RFC-0001 |
| Normas que exerce | [FND-01 §6](../foundation/01-constituicao.md), [FND-07 §10](../foundation/07-framework-decisoes.md) |
| Componentes vinculados | nenhum ainda |
