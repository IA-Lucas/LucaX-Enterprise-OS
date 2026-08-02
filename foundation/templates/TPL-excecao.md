---
id: TPL-excecao
titulo: Template de Excecao Formal
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

# Template — Excecao Formal ("quebra-vidro")

## Proposito
Registrar autorizacao temporaria, nominal e com prazo para descumprir norma nao-petrea,
conforme [FND-01 §8.3](../01-constituicao.md) e [FND-04 §9](../04-governanca.md).

## Escopo
Somente normas **nao-petreas**.

> **Nao admitem excecao:** Principios Imutaveis PI-01 a PI-14 e as Linhas Vermelhas
> LV-02 (credencial em texto), LV-05 (reportar falso) e LV-12 (fabricar evidencia).

## Responsaveis
Autoriza: **SOBERANO** (indelegavel) · Registra: DEP-GOV · Fiscaliza expiracao: DEP-GOV.

## Instrucoes de uso
1. Grave em `governance/exceptions/EXC-<AAAA>-<NNN>.md`.
2. **Excecao sem prazo e invalida.** Nao ha renovacao tacita.
3. Silencio do Soberano nunca autoriza (GV-05, CM-07).
4. Excecao vencida e nao regularizada vira incidente de conformidade automaticamente.

---
---
id: EXC-<AAAA>-<NNN>
titulo: <o que se excepciona, em uma linha>
tipo: excecao
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: <DEP-xxx solicitante>
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: <AAAA-MM-DD>
atualizado_em: <AAAA-MM-DD>
revisao_prevista: <data de expiracao>
decisoes_relacionadas: []
substitui: []
substituido_por: null
ttl: <AAAA-MM-DD — obrigatorio>
---

# EXC-<AAAA>-<NNN>: <Titulo>

## Proposito
<Por que esta excecao foi necessaria. Ate 3 frases.>

## Escopo
| Item | Definicao |
|---|---|
| Norma excepcionada | <referencia exata: documento, secao, regra> |
| Alcance exato | <o que exatamente fica dispensado> |
| O que **continua** valendo | |
| Componentes afetados | |

## Responsaveis
| Papel | Quem |
|---|---|
| Solicitante | |
| Autorizador | **SOBERANO** |
| Registrador | DEP-GOV |
| Responsavel pela regularizacao | |

## 1. Motivo
<Por que cumprir a norma neste caso especifico causaria dano maior que descumpri-la.>

## 2. Alternativas descartadas
| Alternativa que respeitaria a norma | Por que nao serve |
|---|---|

## 3. Risco assumido
| Risco | Impacto | Mitigacao adotada |
|---|---|---|

## 4. Prazo
| Campo | Conteudo |
|---|---|
| Inicio | <AAAA-MM-DD> |
| **Expiracao** | <AAAA-MM-DD — obrigatorio> |
| O que acontece na expiracao | estado regular restaurado automaticamente |

## 5. Autorizacao do Soberano
| Campo | Conteudo |
|---|---|
| Autorizado explicitamente? | sim / nao |
| Data | |
| Forma da autorizacao | |

> Autorizacao presumida, tacita ou por silencio e **invalida**. Sem esta secao preenchida
> com "sim", a excecao nao existe.

## 6. Plano de regularizacao
| Etapa | Responsavel | Prazo |
|---|---|---|

Ao expirar, uma das tres deve ocorrer:
- [ ] Estado regular restaurado
- [ ] Nova excecao explicitamente autorizada
- [ ] Norma alterada via RFC (a excecao virou regra)

## 7. Encerramento
| Campo | Conteudo |
|---|---|
| Data de encerramento | |
| Como foi regularizada | |
| Registro APR gerado | <por que a organizacao precisou de excecao> |
| Verificado por | DEP-GOV |
