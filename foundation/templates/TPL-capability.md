---
id: TPL-capability
titulo: Template de Carta de Capability
tipo: template
versao: 1.0.0
status: ativo
camada_memoria: nao-aplicavel
autor: DEP-GOV
proprietario: DEP-EXE
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0002]
substitui: []
substituido_por: null
---

# Template — Carta de Capability

## Proposito
Dar existencia formal a uma competencia permanente da organizacao, com os treze atributos
obrigatorios de [FND-08 §2](../08-capability-framework.md).

## Escopo
Criacao e alteracao de Capability. Criacao e mudanca **C2, Tipo 1** — exige ratificacao do
Soberano.

## Responsaveis
Proprietario: DEP-EXE · Custodio: um departamento · Conformidade: DEP-GOV ·
Sobreposicao e indicadores: DEP-QAR · Ratificacao: SOBERANO.

## Instrucoes de uso
1. Antes de tudo, aplique os **seis testes TC** (FND-08 §1.1). Falhou um, nao e Capability.
2. Verifique que nao ha sobreposicao com o catalogo vigente (`capabilities/README.md`).
3. Grave em `capabilities/CAP-<slug>.md`.
4. **Limites (A-05) devem nomear a Capability que de fato possui aquilo** — limite generico
   e devolvido.
5. **Indicadores (A-12) medem saude da competencia, nao volume de trabalho.**
6. Declare cada relacao nos **dois lados** (RL-03).

---
---
id: CAP-<slug>
titulo: <Nome da Capability>
tipo: capability
versao: 1.0.0
status: rascunho
camada_memoria: estrategica
autor: <DEP-xxx>
proprietario: DEP-EXE
aprovador: SOBERANO
criado_em: <AAAA-MM-DD>
atualizado_em: <AAAA-MM-DD>
revisao_prevista: <AAAA-MM-DD>
decisoes_relacionadas: [ADR-0002]
substitui: []
substituido_por: null
dominio: <DIR|VAL|REA|GAR|SUS|MER|COG>
classe: <nucleo|habilitadora|suporte>
maturidade: <proposta|experimental|emergente|estabelecida|madura|em-depreciacao|aposentada>
custodio: <DEP-xxx>
exercentes: []
depende_de: []
consumida_por: []
especializa: null
---

# <Nome da Capability> (CAP-<slug>)

## Proposito
<A-02 — Por que esta competencia existe na organizacao. Ate 3 frases.>

## Escopo
<A-04 — O que esta competencia abrange. Descrito sem citar produto especifico.>

| Item | Definicao |
|---|---|
| Dominio | |
| Classe estrategica | |
| Maturidade | |
| Custodio | |
| Exercentes | |

## Responsaveis
| Papel | Quem |
|---|---|
| Custodio (unico) | |
| Exercentes | |
| Autoridade de evolucao | Custodio, com parecer de DEP-GOV |
| Ratificador | SOBERANO |

---

## 1. Identidade (A-01)
| Campo | Valor |
|---|---|
| ID | `CAP-<slug>` |
| Nome | |
| Dominio | |
| Classe | |
| Maturidade | |
| Especializa | <CAP-mae ou "nenhuma"> |

## 2. Missao (A-03)
> <Uma frase: o resultado permanente pelo qual esta competencia responde.>

## 3. Limites (A-05)
> Obrigatorio. Cada limite nomeia **a Capability que de fato possui aquilo**.

| **Nao** abrange | Pertence a |
|---|---|
| | |

## 4. Responsabilidades (A-06)
> O que a organizacao consegue fazer por possuir esta competencia. Verbos de competencia,
> nao de tarefa.

| # | A organizacao e capaz de... |
|---|---|
| R1 | |

## 5. Entradas (A-07)
| Entrada | Origem (CAP-id ou externa) | Obrigatoria? |
|---|---|---|

## 6. Saidas (A-08)
| Saida | Consumida por (CAP-id) |
|---|---|

## 7. Artefatos produzidos (A-09)
> Tipos de artefato da taxonomia (FND-03) que materializam esta competencia.

| Tipo de artefato | Exemplo |
|---|---|

## 8. Dependencias (A-10)
| Capability | Tipo de relacao (FND-08 §5.1) | Por que |
|---|---|---|

## 9. Consumidores (A-11)
| Capability | Tipo de relacao | O que consome |
|---|---|---|

## 10. Indicadores (A-12)
> Medem **existencia e saude da competencia**, nunca volume de trabalho.

| # | Indicador | Direcao | Como se mede | Estado atual |
|---|---|---|---|---|
| I1 | | | | nao medido |

## 11. Criterios de evolucao (A-13)
| Movimento | Gatilho | Ganho PI-14 |
|---|---|---|
| Especializar | | |
| Fundir | | |
| Depreciar | | |
| Mudar de classe | | |

## 12. Historico de maturidade
| Data | De | Para | Evidencia | Instrumento |
|---|---|---|---|---|

## 13. Rastreabilidade
| Campo | Conteudo |
|---|---|
| ADR de criacao | |
| RFC de origem | |
| Componentes vinculados | <preenchido conforme forem criados> |

---

## Checklist de conformidade (FND-08 §9.2)
- [ ] Passa nos seis testes TC (§1.1)
- [ ] Treze atributos presentes
- [ ] Limites nomeiam a Capability dona (A-05)
- [ ] Indicadores medem saude, nao volume (A-12)
- [ ] Custodio unico, apto (OW-01, OW-04, OW-05)
- [ ] Relacoes declaradas nos dois lados (RL-03)
- [ ] Combinacao dominio × classe × maturidade valida (§3.5)
- [ ] Sem sobreposicao com o catalogo vigente
- [ ] Sem dependencia circular dura (RL-01)
