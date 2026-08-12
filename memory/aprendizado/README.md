---
id: IDX-mem-aprendizado
titulo: Camada de Aprendizado da Memoria
tipo: relatorio
versao: 1.2.0
status: ativo
camada_memoria: aprendizado
autor: DEP-GOV
proprietario: DEP-KMS
aprovador: DEP-KMS
criado_em: 2026-07-28
atualizado_em: 2026-07-29
revisao_prevista: null
decisoes_relacionadas: [ADR-0001, ADR-0008, ADR-0011]
substitui: []
substituido_por: null
resumo: Indexa a camada de aprendizado, seus seis registros e as regras que invalidam uma licao.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# Camada APR — Memoria de Aprendizado

## Proposito
Converter experiencia em capacidade: o que funcionou, o que falhou, e o que a proxima
ocorrencia precisa saber. Definicao completa em
[FND-06 §3.5](../../foundation/06-arquitetura-memoria.md).

## Escopo
| Item | Definicao |
|---|---|
| Pergunta que responde | O que aprendemos ao fazer? |
| Volatilidade | Media — um aprendizado vale ate ser refutado |
| TTL | Ate refutacao ou promocao a EST |
| Autoridade em conflito | 4 |
| Natureza | **Transversal** — alimenta-se de todas as camadas e promove para todas |

## Responsaveis
| Papel | Responsavel |
|---|---|
| Dono | DEP-KMS |
| Escreve | DEP-KMS, a partir de contribuicao **obrigatoria** de todos os departamentos |
| Le (obrigatorio) | Todos, antes de iniciar trabalho semelhante (QG-0) |
| Portao | QG-5 — nenhum trabalho encerra sem registro aqui |

---

## Pertence a esta camada
- Postmortems de incidentes: causa, efeito, correcao de causa
- Padroes que funcionaram — **e em que condicoes**
- Antipadroes: o que falhou, por que, e como reconhecer cedo
- Heuristicas de estimativa e de risco calibradas pela experiencia
- Retrospectivas de ciclo e de projeto
- Calibracao de execucao: que tipo de instrucao produz bom resultado
- **Ganhos de especializacao constatados ou nao confirmados** (PI-14)
- Erros de conformidade e sua causa raiz

## **Nao** pertence
| Conteudo | Por que |
|---|---|
| Relato de evento sem licao extraida | Isso e OPR |
| Opiniao sem evidencia | Falha MM-02 |
| Norma | Vai para EST, via ADR |
| Decisao | Vai para `../../decisions/` |

## Estrutura obrigatoria do registro

```markdown
## Situacao     o contexto em que aconteceu
## Observado    o que de fato ocorreu (fato, nao interpretacao)
## Causa        por que ocorreu — causa, nao sintoma
## Licao        o que se conclui, de forma generalizavel
## Condicoes    quando esta licao se aplica — e quando NAO se aplica
## Acao         o que muda daqui em diante, e quem e o dono da mudanca
## Confianca    alta | media | baixa — com base em quantas ocorrencias
```

### Duas regras que invalidam o registro
| Ausencia | Por que invalida |
|---|---|
| Sem **Condicoes** | Vira regra universal a partir de caso unico — perigoso |
| Sem **Acao** | E observacao, nao aprendizado |

## Promocao para EST
Uma licao sobe a camada Estrategica quando:
- confirmada em **≥ 2 ocorrencias independentes**, ou
- determinada diretamente pelo Soberano.

Em ambos os casos, **ADR obrigatorio** (FND-06 §5.2).

## Refutacao
Licao refutada por evidencia nova passa a `superado`, apontando para o registro que a
refutou. **Nunca e apagada** (MM-09) — saber o que a organizacao acreditou e por que
deixou de acreditar tem valor proprio.

## Registros

| ID | Titulo | Confianca | Ocorrencias | Status |
|---|---|---|---|---|
| [MEM-APR-0001](MEM-APR-0001-ratificacao-por-precedente.md) | Ressalva escrita nao neutraliza condicao de validade | alta | 4 | `ativo` |
| [MEM-APR-0002](MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md) | Detectar duplicacao nao previne duplicacao | alta | **5** | `ativo` |
| [MEM-APR-0003](MEM-APR-0003-campo-de-estado-em-artefato-imutavel.md) | Campo de estado em artefato imutavel so registra o estado no ato | alta | 1 | `ativo` |
| [MEM-APR-0004](MEM-APR-0004-projecao-revela-divergencia-antiga.md) | Projetar a mesma fonte por outro eixo revela divergencia antiga | media | 1 | `ativo` |
| [**MEM-APR-0005**](MEM-APR-0005-medir-a-ausencia-na-fonte-errada.md) | **Buscar o termo em vez da funcao produz achado de lacuna onde ha titular declarado** | **alta** | **3** | `ativo` |
| [**MEM-APR-0006**](MEM-APR-0006-exercer-o-contador-revela-o-defeito.md) | **Exercer o instrumento revela o defeito que ler o instrumento nao revela** | **alta** | **1** | `ativo` |
| [**MEM-APR-0007**](MEM-APR-0007-plausibilidade-nao-e-verificacao.md) | **Plausibilidade nao e verificacao** — coerencia usada como evidencia, a causa n. 1 de reprovacao medida (9 de 17) | **alta** | **9** | `ativo` |
| [**MEM-APR-0008**](MEM-APR-0008-campo-obrigatorio-com-escape-vazio.md) | **Campo obrigatorio com escape vazio e falso cumprimento** — o campo que aceita o valor que o esvazia (5 de 17) | **media** | **5** | `ativo` |

**Contador oficial:** ultimo `MEM-APR-0006` · proximo **`MEM-APR-0007`**.

> **Este contador estava correto quando `RD-32` mediu todos.** A varredura cobriu **9
> sequencias em 7 indices** — `ADR`, `RFC`, `FIT` *(em dois indices)*, `EXC`, `INC`, `MEM-APR`,
> `MEM-EST` e `MSG`. **Quatro estavam defasadas em um** *(`ADR`, `RFC` e as duas de `FIT`)* e
> **cinco estavam corretas**, esta entre elas. Registrado porque **contra-exemplo tambem e
> evidencia**: o defeito nao e sistemico a todos os contadores, e sim aos das sequencias
> movimentadas pelas missoes 1.12 e 1.12.1. Metodo em
> [MEM-APR-0006](MEM-APR-0006-exercer-o-contador-revela-o-defeito.md) `V1`.

Template: [`TPL-memoria`](../../foundation/templates/TPL-memoria.md) ·
Incidentes: [`TPL-incidente`](../../foundation/templates/TPL-incidente.md)
