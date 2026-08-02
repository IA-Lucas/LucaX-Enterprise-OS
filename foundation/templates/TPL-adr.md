---
id: TPL-adr
titulo: Template de Registro de Decisao (ADR)
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

# Template — ADR

## Proposito
Padronizar o registro de decisoes tomadas, conforme [FND-07 §4](../07-framework-decisoes.md).

## Escopo
Toda decisao C2, C3 ou Tipo 1, e decisao C1 que crie precedente. Nao se aplica a decisao
C1 local (usar `TPL-nota-decisao`) nem a proposta em aberto (usar `TPL-rfc`).

## Responsaveis
Proprietario: DEP-GOV · Numeracao: DEP-GOV · Verificacao de risco: DEP-QAR.

## Instrucoes de uso
1. Copie o bloco abaixo para `decisions/ADR-<NNNN>-<slug>.md`.
2. Solicite o numero a DEP-GOV **antes** de preencher — numero nao e autoatribuido.
3. Preencha **todas** as secoes. Secao vazia invalida o registro (FND-07 §4.1).
4. Apos `aprovado`, o arquivo se torna imutavel (LV-04). Corrigir = superar.

---
---
id: ADR-<NNNN>-<slug>
titulo: <a decisao em uma frase afirmativa>
tipo: adr
versao: 1.0.0
status: rascunho
camada_memoria: <estrategica|produto|tecnica|operacional|aprendizado>
autor: <DEP-xxx>
proprietario: <DEP-xxx>
aprovador: <DEP-xxx | SOBERANO>
criado_em: <AAAA-MM-DD>
atualizado_em: <AAAA-MM-DD>
revisao_prevista: <AAAA-MM-DD>
decisoes_relacionadas: []
substitui: []
substituido_por: null
classe_mudanca: <C0|C1|C2|C3>
tipo_decisao: <1|2>
supera: []
superado_por: null
---

# ADR-<NNNN>: <Titulo>

## Proposito
<Para que este registro existe, em ate 3 frases.>

## Escopo
<A que se aplica. A que explicitamente nao se aplica. A que se subordina.>

## Responsaveis
| Papel | Quem |
|---|---|
| Proponente | |
| Revisor independente | |
| Aprovador | |
| Ratificador (se Tipo 1 ou C3) | |
| Executor | |

## 1. Contexto
<Situacao atual. Por que isso e um problema agora. O que acontece se nada mudar.
Fatos, nao justificativas.>

## 2. Problema / Pergunta de decisao
<Uma unica pergunta, exata.>

## 3. Criterios de decisao
> Preencher **antes** de examinar as alternativas (FND-07, CD-01).

| # | Criterio | Peso | Como se mede |
|---|---|---|---|
| C1 | | | |
| C2 | | | |
| C3 | | | |

## 4. Alternativas consideradas
> Minimo: 2 alternativas reais + "nao fazer nada". Alternativa de palha invalida o ADR.

### Alternativa A — <nome>
| Campo | Conteudo |
|---|---|
| Descricao | |
| A favor | |
| Contra | |
| Custo | |
| Risco | |
| Avaliacao pelos criterios | |

### Alternativa B — <nome>
<mesma estrutura>

### Alternativa Z — Nao fazer nada
| Campo | Conteudo |
|---|---|
| O que acontece se mantivermos o estado atual | |
| Custo real da inacao | |
| Por que isto nao venceu (ou venceu) | |

## 5. Decisao
> Frase afirmativa e inequivoca. Sem hedge.

**Decidimos <...>.**

## 6. Justificativa
<Por que esta opcao vence pelos criterios da secao 3.>

**Tradeoff aceito:** <do que se esta abrindo mao ao escolher isto.>

## 7. Impacto
| Dimensao | Impacto |
|---|---|
| Departamentos afetados | |
| Componentes afetados | |
| Camadas de memoria a atualizar | |
| Decisoes superadas | |
| Documentos a atualizar | |
| Custo e dependencia criados | |
| Ganho PI-14 (organizacao / reuso / contexto) | |

## 8. Evidencias
| # | Evidencia | Origem (ID) | Confianca | O que ela discrimina |
|---|---|---|---|---|
| E1 | | | alta/media/baixa | |

<Se nao houver evidencia suficiente, declarar aqui explicitamente. Omitir viola PI-10.>

## 9. Riscos e mitigacao
| # | Risco | Probabilidade | Impacto | Mitigacao prevista |
|---|---|---|---|---|
| R1 | | | | |
| R2 | Esta decisao estar errada | | | |

## 10. Plano de reversao
| Campo | Conteudo |
|---|---|
| Como desfazer | |
| Custo da reversao | |
| Janela em que ainda e possivel | |
| Quem executa | |
| Backup necessario (PI-07) | |

<Obrigatorio para Tipo 1. Para Tipo 2, justificar por que a reversao e trivial.>

## 11. Classificacao
| Campo | Valor |
|---|---|
| Classe de mudanca | |
| Tipo de reversibilidade | |
| Decisor | |
| Ratificador | |
| Data da decisao | |
| Data de vigencia | |

## 12. Revisao
| Campo | Conteudo |
|---|---|
| Gatilho de reavaliacao | temporal / evento / sinal de falha / confirmacao de ganho |
| Detalhe do gatilho | |
| Sinal de que esta decisao deu errado | |
| Responsavel pela revisao | |

## 13. Rastreabilidade
| Campo | Conteudo |
|---|---|
| Origem (RFC, incidente, escalada) | |
| Decisoes superadas | |
| Decisoes relacionadas | |
| Registros de memoria gerados | |

---

## Checklist de validade (FND-07 §4.1)
- [ ] VD-01 — 2+ alternativas reais + "nao fazer nada"
- [ ] VD-02 — criterios declarados antes da escolha
- [ ] VD-03 — nenhuma alternativa de palha
- [ ] VD-04 — tradeoff aceito explicito
- [ ] VD-05 — evidencia ausente declarada como ausente
- [ ] VD-06 — plano de reversao (obrigatorio se Tipo 1)
- [ ] VD-07 — impacto em cascata mapeado
- [ ] VD-08 — data e responsavel presentes
- [ ] VD-09 — gatilho de revisao definido
