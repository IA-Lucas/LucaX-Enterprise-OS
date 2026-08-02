---
id: CAP-seguranca
titulo: Seguranca
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
classe: habilitadora
maturidade: experimental
custodio: DEP-QAR
exercentes: [DEP-QAR]
depende_de: [CAP-governanca]
consumida_por: [CAP-integracao, CAP-dados]
especializa: null
---

# Seguranca (CAP-seguranca)

## Proposito
Proteger o que a organizacao guarda e o que ela expoe: segredo, dado vivo, acesso e
superficie externa. E a competencia que impede que uma decisao correta produza dano por
descuido.

## Escopo
A competencia de classificar sensibilidade, controlar acesso, proteger segredo, avaliar
superficie de exposicao, verificar backup e reversao, e responder a comprometimento.

| Item | Definicao |
|---|---|
| Dominio | `GAR` — Garantia |
| Classe estrategica | `habilitadora` |
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
| ID | `CAP-seguranca` |
| Nome | Seguranca |
| Dominio | GAR |
| Classe | habilitadora |
| Maturidade | experimental |
| Especializa | nenhuma |

## 2. Missao (A-03)
> Garantir que nenhum segredo vaze, nenhum dado vivo seja perdido e nenhuma exposicao
> externa ocorra sem autorizacao especifica.

## 3. Limites (A-05)
| **Nao** abrange | Pertence a |
|---|---|
| Verificar se a entrega esta correta | `CAP-qualidade` |
| Verificar conformidade com norma interna | `CAP-governanca` |
| Base legal e obrigacao regulatoria | `CAP-juridico` |
| Modelar e qualificar o dado | `CAP-dados` |
| Prover e configurar o ambiente | `CAP-infraestrutura` |
| Contratar a capacidade externa | `CAP-integracao` |
| Executar backup como rotina | `CAP-operacoes` |

> **Fronteira com `CAP-operacoes`:** operacoes **executa** o backup; esta Capability
> **verifica que ele existe, e integro e e restauravel**. Executar e verificar nao se
> concentram no mesmo papel (PI-05).
>
> **Fronteira com `CAP-juridico`:** esta protege contra **dano**; aquela, contra
> **ilicitude**. Vazamento e materia das duas, por razoes diferentes.

## 4. Responsabilidades (A-06)
| # | A organizacao e capaz de... |
|---|---|
| R1 | Classificar sensibilidade de dado e de artefato |
| R2 | Garantir que credencial jamais apareca em texto (PI-08, LV-02) |
| R3 | Avaliar superficie de exposicao antes de qualquer envio externo |
| R4 | Verificar que backup existe, esta integro e e restauravel (PI-07) |
| R5 | Exigir plano de reversao antes de acao irreversivel |
| R6 | Reconhecer comprometimento e acionar rotacao e contencao |
| R7 | Avaliar risco de dependencia externa e de acesso concedido |

## 5. Entradas (A-07)
| Entrada | Origem | Obrigatoria? |
|---|---|---|
| Norma de segredo, backup e exposicao | `CAP-governanca` | Sim |
| Artefato ou acao a avaliar | qualquer Capability | Sim |
| Catalogo de dependencias externas | `CAP-integracao` | Sim |
| Registro de execucao de backup | `CAP-operacoes` | Sim |

## 6. Saidas (A-08)
| Saida | Consumida por |
|---|---|
| Classificacao de sensibilidade | `CAP-dados`, `CAP-integracao` |
| Requisitos de protecao e acesso | `CAP-dados`, `CAP-infraestrutura` |
| Parecer de exposicao externa | `CAP-marketing`, `CAP-integracao`, Soberano |
| Confirmacao de backup e reversao | `CAP-qualidade`, `CAP-coordenacao` |
| Alerta de comprometimento | `CAP-governanca` |

## 7. Artefatos produzidos (A-09)
| Tipo de artefato | Exemplo |
|---|---|
| Relatorio | Laudo de exposicao, avaliacao de risco |
| Incidente (`INC`) | Credencial exposta, comprometimento |
| Memoria (`MEM-TEC`) | Requisito de protecao, risco de dependencia |

## 8. Dependencias (A-10)
| Capability | Relacao | Por que |
|---|---|---|
| `CAP-governanca` | depende-de | Proteger exige norma que defina o proibido |

## 9. Consumidores (A-11)
| Capability | Relacao | O que consome |
|---|---|---|
| `CAP-integracao` | depende-de | Parecer de risco antes de adotar capacidade externa |
| `CAP-dados` | depende-de | Requisitos de protecao e acesso |
| `CAP-engenharia` | verifica *(inversa)* | Esta Capability verifica risco na saida daquela |
| `CAP-infraestrutura` | verifica *(inversa)* | Idem |

## 10. Indicadores (A-12)
| # | Indicador | Direcao | Como se mede | Estado |
|---|---|---|---|---|
| I1 | Credenciais encontradas em texto | → 0 | Varredura de artefatos (PI-08) | **0** (38 arquivos, 2026-07-28) |
| I2 | Acoes destrutivas executadas sem backup verificado | → 0 | Auditoria QG-4 (LV-01) | **0** |
| I3 | Envios externos sem autorizacao especifica | → 0 | Registro de exposicao (LV-08) | **0** |
| I4 | Tempo entre comprometimento e rotacao | ↓ | Registro de incidente | sem ocorrencia |
| I5 | Planos de reversao testados, nao apenas escritos | ↑ | Verificacao em QG-4 | nao medido |

## 11. Criterios de evolucao (A-13)
| Movimento | Gatilho | Ganho PI-14 |
|---|---|---|
| Especializar | Protecao de dado e seguranca de execucao divergirem em metodo | Organizacao |
| Especializar | Gestao de acesso e segredo virar volume proprio | Organizacao |
| Fundir | Deixar de ser distinguivel de `CAP-qualidade` na pratica | Organizacao |
| Promover a `nucleo` | Se a organizacao passar a operar dado de terceiros em escala | — |

## 12. Historico de maturidade
| Data | De | Para | Evidencia | Instrumento |
|---|---|---|---|---|
| 2026-07-28 | proposta | experimental | Catalogo aprovado; exercida apenas em varredura de credencial, sem dado vivo nem exposicao externa | ADR-0002 |

## 13. Rastreabilidade
| Campo | Conteudo |
|---|---|
| ADR de criacao | ADR-0002 |
| RFC de origem | RFC-0001 |
| Normas que exerce | [FND-01 PI-07, PI-08, LV-01, LV-02, LV-08](../foundation/01-constituicao.md) |
| Componentes vinculados | nenhum ainda |
