---
id: TPL-incidente
titulo: Template de Incidente de Conformidade
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

# Template — Incidente de Conformidade

## Proposito
Registrar violacao de norma detectada, sua causa, seu efeito e a correcao aplicada,
conforme [FND-04 §10](../04-governanca.md).

## Escopo
Violacao de Principio Imutavel ou Linha Vermelha, mudanca sem instrumento, acumulo indevido
de papeis, artefato ativo sem rastreabilidade, excecao vencida, credencial exposta, portao
pulado sem excecao formal.

> **Incidente nao e punicao — e informacao.** Deixar de registrar incidente observado e,
> em si, violacao (LV-11).

## Responsaveis
Abre e conduz: DEP-GOV · Verifica fechamento: DEP-QAR · Grava aprendizado: DEP-KMS.

## Instrucoes de uso
1. Grave em `governance/incidents/INC-<AAAA>-<NNN>.md`.
2. **Etapa 1 e parar**, nao registrar. A execucao em curso e interrompida primeiro.
3. Incidente fechado sem correcao de **causa** nao esta fechado.
4. Registro APR e obrigatorio no fechamento.

---
---
id: INC-<AAAA>-<NNN>
titulo: <a violacao em uma linha>
tipo: incidente
versao: 1.0.0
status: <aberto|em-analise|corrigido|fechado>
camada_memoria: operacional
autor: <quem detectou>
proprietario: DEP-GOV
aprovador: DEP-QAR
criado_em: <AAAA-MM-DD>
atualizado_em: <AAAA-MM-DD>
revisao_prevista: null
decisoes_relacionadas: []
substitui: []
substituido_por: null
severidade: <baixa|media|alta|critica>
---

# INC-<AAAA>-<NNN>: <Titulo>

## Proposito
<Registrar o que foi violado e garantir que causa e efeito sejam tratados.>

## Escopo
| Item | Definicao |
|---|---|
| Norma violada | <referencia exata: PI-xx, LV-xx, secao> |
| Componentes afetados | |
| Periodo em que vigorou | |

## Responsaveis
| Papel | Quem |
|---|---|
| Detectou | |
| Conduz | DEP-GOV |
| Corrige | |
| Verifica fechamento | DEP-QAR |

## 1. Fato
<O que aconteceu. Fato observavel, sem interpretacao e sem atribuicao de culpa.>

| Campo | Conteudo |
|---|---|
| Quando ocorreu | |
| Quando foi detectado | |
| Como foi detectado | |
| Quem executou o ato | |

## 2. Norma violada
| Norma | Texto da norma | Como foi violada |
|---|---|---|

## 3. Efeito
| Campo | Conteudo |
|---|---|
| O que o ato produziu | |
| E reversivel? | |
| Dado afetado | |
| Terceiros afetados | |

## 4. Contencao (etapa 3)
| Acao imediata | Executada por | Data |
|---|---|---|

- [ ] Execucao interrompida
- [ ] Efeito revertido (ou isolado, se irreversivel)
- [ ] Backup verificado (se aplicavel, PI-07)
- [ ] Credencial rotacionada (se LV-02)

## 5. Analise de causa (etapa 4)
> Causa, nao sintoma. Classifique em uma das quatro:

| Classe de causa | Marque | Detalhe |
|---|---|---|
| Falha de **norma** (a regra nao previa o caso) | [ ] | |
| Falha de **instrumento** (nao havia como cumprir) | [ ] | |
| Falha de **compreensao** (a regra nao estava clara) | [ ] | |
| Falha de **execucao** (a regra era clara e nao foi seguida) | [ ] | |

**Causa raiz:** <descricao>

## 6. Correcao (etapa 5)
| Campo | Acao | Responsavel | Prazo |
|---|---|---|---|
| Correcao do **efeito** | | | |
| Correcao da **causa** | | | |

> Corrigir so o efeito deixa o incidente aberto. Causa nao corrigida reincide.

## 7. Aprendizado (etapa 6)
| Campo | Conteudo |
|---|---|
| Licao generalizavel | |
| Condicoes em que se aplica | |
| Registro MEM-APR gerado | |
| Norma a alterar (se houver) | <RFC proposta> |

## 8. Fechamento (etapa 7)
| Campo | Conteudo |
|---|---|
| Efeito tratado? | |
| Causa tratada? | |
| Registro APR criado? | |
| Verificado por | DEP-QAR |
| Data de fechamento | |

> Incidente so fecha com efeito **e** causa tratados, e com aprendizado gravado.

## 9. Escalonamento
| Campo | Conteudo |
|---|---|
| Escalado ao Soberano? | sim / nao |
| Motivo | <violacao de PI ou LV vai direto a E4, EC-02> |
| Data | |
