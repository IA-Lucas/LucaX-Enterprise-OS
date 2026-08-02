---
id: CAP-juridico
titulo: Juridico e Regulatorio
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
classe: suporte
maturidade: experimental
custodio: DEP-QAR
exercentes: [DEP-QAR]
depende_de: [CAP-governanca]
consumida_por: [CAP-comercial]
especializa: null
---

# Juridico e Regulatorio (CAP-juridico)

## Proposito
Manter a organizacao dentro da norma **externa**: lei, regulacao, contrato, licenca e termo
de terceiro. E a competencia que impede que uma decisao internamente correta produza
ilicitude.

## Escopo
A competencia de reconhecer obrigacao externa aplicavel, avaliar risco juridico, ler termo
de terceiro antes de depender dele e identificar quando o assunto exige assessoria humana
qualificada.

| Item | Definicao |
|---|---|
| Dominio | `GAR` — Garantia |
| Classe estrategica | `suporte` |
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
| ID | `CAP-juridico` |
| Nome | Juridico e Regulatorio |
| Dominio | GAR |
| Classe | suporte |
| Maturidade | experimental |
| Especializa | nenhuma |

## 2. Missao (A-03)
> Garantir que a organizacao reconheca a obrigacao externa que a alcanca — e que saiba
> quando a questao ultrapassa sua propria competencia e exige um profissional humano.

## 3. Limites (A-05)
| **Nao** abrange | Pertence a |
|---|---|
| Conformidade com norma **interna** do LucaX | `CAP-governanca` |
| Protecao tecnica contra vazamento e dano | `CAP-seguranca` |
| Correcao da entrega | `CAP-qualidade` |
| Negociar termos comerciais | `CAP-comercial` |
| Adotar e manter o fornecedor | `CAP-integracao` |
| **Substituir assessoria juridica humana** | profissional externo qualificado |

> **Limite de competencia declarado:** esta Capability **reconhece e sinaliza** questao
> juridica; nao emite parecer que substitua profissional habilitado. Tratar sua saida como
> aconselhamento juridico definitivo e uso indevido.
>
> **Fronteira com `CAP-governanca`:** aquela cuida da norma que o LucaX **escreveu para si**;
> esta, da norma que **incide de fora**, independentemente da vontade da organizacao.

## 4. Responsabilidades (A-06)
| # | A organizacao e capaz de... |
|---|---|
| R1 | Reconhecer quando uma acao tem implicacao juridica ou regulatoria |
| R2 | Ler e sintetizar termo de terceiro antes de criar dependencia |
| R3 | Identificar obrigacao sobre dado pessoal e sobre uso de IA |
| R4 | Avaliar risco de propriedade intelectual e de licenca |
| R5 | **Reconhecer o proprio limite** e escalar ao Soberano para assessoria humana |
| R6 | Manter registro do que foi aceito ao contratar terceiros |

## 5. Entradas (A-07)
| Entrada | Origem | Obrigatoria? |
|---|---|---|
| Rito de registro e decisao | `CAP-governanca` | Sim |
| Termos e licencas de terceiros | `CAP-integracao` | Sim |
| Acao com exposicao externa | `CAP-marketing`, `CAP-comercial` | Sim |
| Classificacao de dado sensivel | `CAP-seguranca` | Sim |

## 6. Saidas (A-08)
| Saida | Consumida por |
|---|---|
| Sinalizacao de risco juridico | `CAP-coordenacao`, Soberano |
| Sintese de obrigacao contratual aceita | `CAP-integracao`, `CAP-comercial` |
| Requisitos de conformidade externa | `CAP-dados`, `CAP-marketing` |
| Escalonamento para assessoria humana | Soberano |

## 7. Artefatos produzidos (A-09)
| Tipo de artefato | Exemplo |
|---|---|
| Relatorio | Sinalizacao de risco, sintese de termo |
| Memoria (`MEM-EST`) | Obrigacao permanente reconhecida |
| ADR | Decisao com implicacao juridica registrada |

## 8. Dependencias (A-10)
| Capability | Relacao | Por que |
|---|---|---|
| `CAP-governanca` | depende-de | Registrar obrigacao externa exige o instrumento interno |

## 9. Consumidores (A-11)
| Capability | Relacao | O que consome |
|---|---|---|
| `CAP-comercial` | depende-de | Limites do que pode ser prometido e contratado |
| `CAP-integracao` | consome-saida-de | Sintese dos termos que se esta aceitando |
| `CAP-marketing` | consome-saida-de | Requisitos de conformidade na comunicacao |

## 10. Indicadores (A-12)
| # | Indicador | Direcao | Como se mede | Estado |
|---|---|---|---|---|
| I1 | Dependencias externas adotadas sem leitura de termos | → 0 | Auditoria de ficha de ferramenta | **0** (nenhuma adotada) |
| I2 | Questoes escaladas para assessoria humana quando cabia | → 100% | Registro de escalonamento | sem ocorrencia |
| I3 | Obrigacoes externas reconhecidas antes do fato, nao depois | ↑ | Comparacao registro × incidente | nao medido |
| I4 | Pareceres tratados como definitivos indevidamente | → 0 | Auditoria de uso da saida | **0** |

## 11. Criterios de evolucao (A-13)
| Movimento | Gatilho | Ganho PI-14 |
|---|---|---|
| Especializar | Propriedade intelectual e protecao de dado divergirem em metodo | Organizacao |
| Promover a `habilitadora` | Quando houver contrato com terceiro ou tratamento de dado pessoal | — |
| Fundir | Deixar de ser distinguivel de `CAP-governanca` na pratica | Organizacao |
| Depreciar | Improvavel — obrigacao externa nao depende da vontade da organizacao |

## 12. Historico de maturidade
| Data | De | Para | Evidencia | Instrumento |
|---|---|---|---|---|
| 2026-07-28 | proposta | experimental | Catalogo aprovado; nenhum contrato, terceiro ou dado pessoal envolvido ate aqui | ADR-0002 |

## 13. Rastreabilidade
| Campo | Conteudo |
|---|---|
| ADR de criacao | ADR-0002 |
| RFC de origem | RFC-0001 |
| Componentes vinculados | nenhum ainda |
