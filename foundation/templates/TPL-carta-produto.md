---
id: TPL-carta-produto
titulo: Template de Carta de Produto
tipo: template
versao: 1.1.0
status: ativo
camada_memoria: nao-aplicavel
autor: DEP-GOV
proprietario: DEP-PRD
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-31
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0001, ADR-0002, ADR-0006]
substitui: []
substituido_por: null
resumo: Da a forma da Carta de Produto com os atributos minimos que FND-09 E-17 exige, inclusive o vinculo a Capability e as interfaces do produto.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# Template — Carta de Produto

## Proposito
Dar existencia formal a um produto, com problema, publico, criterio de sucesso e criterio
de encerramento, conforme [FND-03 §3.1](../03-taxonomia.md).

## Escopo
Criacao e alteracao de produto. Mudanca C2, Tipo 1 — exige decisao do Soberano.

## Responsaveis
Proprietario: DEP-PRD · Aprovacao: SOBERANO · Conformidade: DEP-GOV.

## Historico de versoes deste template
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-GOV | Criacao. Ratificado por ADR-0001. |
| 1.1.0 | 2026-07-31 | DEP-GOV | Fecha o achado **RD-56**, aberto pelo primeiro uso real do template na Missao 1.13.4. Passa a prever `capabilities` no frontmatter da instancia — **atributo minimo** de `PRO` em [FND-09 E-17](../09-meta-model.md) e pre-condicao universal I de [FND-04 §6](../04-governanca.md) — e os **cinco campos** de [FND-10 §2.2](../10-artifact-framework.md). Cria as secoes **8 Capabilities consumidas** e **9 Interfaces**, e renumera 8–12 para 10–14. **Nenhuma secao removida e nenhum texto anterior alterado.** |

> **O que esta emenda NAO faz.** Nao cria atributo, secao obrigatoria ou regra nova: **todos**
> os campos que ela acrescenta ja eram exigidos por norma superior, e o defeito era o template
> **nao os instrumentar**. Nao altera quem aprova a Carta *(SOBERANO)* nem a classe da mudanca
> de criar Produto *(`C2 · Tipo 1`)*. **Nao alcanca nenhuma Carta ja escrita** — nao existe
> nenhuma.

## Instrucoes de uso
1. Grave em `products/<slug>/carta.md`.
2. Aplique o teste de existencia (FND-03 §3.1): *se for descontinuado, alguem perde algo?*
   Se a resposta for nao, isto e projeto, nao produto.
3. Criterio de encerramento e obrigatorio na criacao — nao se cria produto sem saber quando
   ele acaba.
4. **`capabilities` e obrigatorio e nao e derivavel.** `FND-09` E-17 o declara **atributo
   minimo** de `PRO`, e `FND-04 §6` faz do vinculo a Capability **pre-condicao universal I**.
   Toda Capability listada tem de estar `ativo` no [catalogo](../../capabilities/README.md)
   *(`VC-01`, `FND-08 §8`)*. Produto que nao consome Capability alguma **nao e aprovavel**.
5. **Os cinco campos de FND-10 §2.2** — `resumo`, `perfil_contexto`, `confidencialidade`,
   `revisor` e `ratificacao` — sao obrigatorios. `projecao_de` **nao se aplica**: Carta de
   Produto e fonte, nunca projecao (`PJ-02`).
6. **`revisor` distinto de `autor`** (`AC-03`, `ADR-0005`). Igualdade torna a aprovacao nula.
7. **`ratificacao: pendente` enquanto nao houver ato do Soberano.** Criar Produto e
   `C2 · Tipo 1`; sem ato, a Carta nao entra em `ativo`.

---
---
id: PRO-<slug>
titulo: <Nome do Produto>
tipo: carta
versao: 1.0.0
status: rascunho
camada_memoria: produto
autor: DEP-PRD
proprietario: DEP-PRD
aprovador: SOBERANO
criado_em: <AAAA-MM-DD>
atualizado_em: <AAAA-MM-DD>
revisao_prevista: <AAAA-MM-DD>
decisoes_relacionadas: [<ADR de criacao>]
substitui: []
substituido_por: null
capabilities: [<CAP-...>, <CAP-...>]
resumo: <Uma linha, ate 200 caracteres, em voz ativa: o que este produto faz.>
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: pendente
---

# <Nome do Produto> (PRO-<slug>)

## Proposito
<Que problema este produto resolve, para quem. Ate 3 frases.>

## Escopo
| Item | Definicao |
|---|---|
| Faz parte do produto | |
| Nao faz parte do produto | |
| Estagio | ideia / descoberta / construcao / operacao / encerramento |

## Responsaveis
| Papel | Quem |
|---|---|
| Proprietario | DEP-PRD |
| Construcao | DEP-ENG |
| Operacao | DEP-OPS |
| Comunicacao | DEP-GRW |
| Aprovador | SOBERANO |

## 1. Problema
<Qual dor existe hoje, para quem, com que consequencia. Com evidencia.>

## 2. Publico
| Persona | Contexto de uso | Dor principal | Como resolve hoje |
|---|---|---|---|

## 3. Proposta de valor
<Uma frase: por que este produto e melhor que a alternativa atual do publico.>

## 4. Escopo negativo
> O que este produto deliberadamente **nao** faz, e por que. Protege contra ampliacao
> silenciosa (PI-09).

| Nao faz | Por que |
|---|---|

## 5. Criterio de sucesso
| Metrica | Definicao | Meta | Prazo |
|---|---|---|---|

## 6. Criterio de encerramento
> Obrigatorio. Sob quais condicoes este produto deve ser descontinuado.

| Condicao | Sinal observavel |
|---|---|

## 7. Hipoteses
| # | Hipotese | Como sera testada | Status (aberta/confirmada/refutada) |
|---|---|---|---|

## 8. Capabilities consumidas
> Obrigatorio. `FND-09` E-17 declara `capabilities` **atributo minimo** de `PRO`, e o
> relacionamento valido e `consome CAP (n→1..n)`. Toda linha aqui tem de aparecer no
> frontmatter, e vice-versa — **a divergencia entre os dois e nao conformidade**.

| Capability | Estado no catalogo | Para que este produto a consome | Departamento custodiante |
|---|---|---|---|

## 9. Interfaces
> O que este produto expoe e o que ele exige de fora. Interface **nao declarada** e
> acoplamento que ninguem pode revisar.

| Direcao | Interface | Contraparte | Natureza (observado/alegado) |
|---|---|---|---|
| expoe | | | |
| consome | | | |

## 10. Restricoes
| Restricao | Origem (norma, tecnica, legal, custo) |
|---|---|

## 11. Riscos
| # | Risco | Impacto | Mitigacao |
|---|---|---|---|

## 12. Decisoes fundadoras
| ADR | O que decidiu |
|---|---|

## 13. Memoria
| Camada | O que este produto alimenta |
|---|---|
| PRD | definicao, personas, hipoteses, feedback |
| TEC | arquitetura propria (via DEP-ENG) |
| APR | licoes generalizaveis |

## 14. Rastreabilidade
| Campo | Conteudo |
|---|---|
| ADR de criacao | |
| Decisao do Soberano (data) | |
| Specs derivadas | |
