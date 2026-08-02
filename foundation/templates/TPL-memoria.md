---
id: TPL-memoria
titulo: Template de Registro de Memoria
tipo: template
versao: 1.0.0
status: ativo
camada_memoria: nao-aplicavel
autor: DEP-GOV
proprietario: DEP-KMS
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0001]
substitui: []
substituido_por: null
---

# Template — Registro de Memoria

## Proposito
Padronizar o registro de memoria organizacional nas cinco camadas, conforme
[FND-06 §6](../06-arquitetura-memoria.md).

## Escopo
Todo registro em `memory/`. Camadas: `estrategica`, `produto`, `tecnica`, `operacional`,
`aprendizado`.

## Responsaveis
Curador de todas as camadas: DEP-KMS · Dono do conteudo: conforme FND-06 §2.1 ·
Auditoria de proveniencia: DEP-GOV.

## Instrucoes de uso
1. Antes de escrever, rode o criterio de alocacao (FND-06 §4). **Um fato, um lugar** (MM-01).
2. Grave em `memory/<camada>/MEM-<CAMADA>-<NNNN>-<slug>.md`.
3. `ttl` e obrigatorio em OPR (FM-02). `evidencia` vazia forca `confianca: baixa` (FM-01).
4. Relacione por ID. **Nunca recole conteudo de outro registro** (MM-01, FM-05).
5. Corrija por acrescimo e superacao, nunca por exclusao (MM-09).

---
---
id: MEM-<EST|PRD|TEC|OPR|APR>-<NNNN>-<slug>
titulo: <o fato ou a licao em uma linha>
tipo: memoria
versao: 1.0.0
status: ativo
camada_memoria: <estrategica|produto|tecnica|operacional|aprendizado>
autor: <DEP-xxx | SOBERANO>
proprietario: <DEP-xxx dono da camada>
aprovador: <DEP-KMS | DEP-GOV se EST>
criado_em: <AAAA-MM-DD>
atualizado_em: <AAAA-MM-DD>
revisao_prevista: <AAAA-MM-DD | null>
decisoes_relacionadas: []
substitui: []
substituido_por: null
origem: <MSG-id | INC-id | PRJ-id | ADR-id | observacao direta>
evidencia: <como se sabe que e verdade>
confianca: <alta|media|baixa>
ocorrencias: <N>
ttl: <AAAA-MM-DD | permanente>
aplica_se_a: [<PRO-id | DEP-id | global>]
---

# <Titulo>

## Proposito
<Por que este registro existe. Ate 3 frases.>

## Escopo
| Item | Definicao |
|---|---|
| Aplica-se a | |
| **Nao** se aplica a | |
| Camada e por que esta camada | |

## Responsaveis
| Papel | Quem |
|---|---|
| Dono da camada | |
| Curador | DEP-KMS |
| Leitura obrigatoria por | |

## Conteudo

<!-- Use a estrutura da camada correspondente -->

### Se camada APR (Aprendizado) — estrutura obrigatoria (FND-06 §3.5)

**Situacao**
<O contexto em que aconteceu.>

**Observado**
<O que de fato ocorreu. Fato, nao interpretacao.>

**Causa**
<Por que ocorreu. Causa, nao sintoma.>

**Licao**
<A conclusao, de forma generalizavel.>

**Condicoes**
<Quando esta licao se aplica — e, obrigatoriamente, quando NAO se aplica.>

**Acao**
<O que muda daqui em diante, e quem e o dono da mudanca.>

**Confianca**
<alta | media | baixa — com base em quantas ocorrencias independentes.>

### Se camada TEC — lembrar
> "Usamos X" nao e memoria tecnica. "Usamos X porque Y, tendo descartado Z por W" e.

### Se camada OPR — lembrar
> `ttl` obrigatorio. Expirar e o comportamento padrao e desejado (MM-05).

## Proveniencia
| Campo | Conteudo |
|---|---|
| Origem (ID) | |
| Autor | |
| Data do fato | |
| Evidencia | |
| Grau de confianca e por que | |

## Relacionados
| ID | Relacao |
|---|---|
| [[MEM-...]] | complementa / contradiz / supera / deriva de |
| ADR-... | decisao correspondente |

## Gatilhos de promocao (FND-06 §5.2)
- [ ] O fato sobrevive ao ciclo em que nasceu → promover OPR a PRD/TEC
- [ ] A experiencia rendeu licao com causa e acao → promover a APR
- [ ] Confirmado em 2+ ocorrencias independentes → candidato a EST (exige ADR)
- [ ] Recuperado repetidamente para o mesmo fim → candidato a Skill (PI-14)

## Gatilhos de expiracao (FND-06 §5.3)
- [ ] TTL vencido sem promocao
- [ ] Nunca recuperado ao longo de um horizonte (RC-05)
- [ ] Refutado por evidencia nova → `superado`, nunca apagado
