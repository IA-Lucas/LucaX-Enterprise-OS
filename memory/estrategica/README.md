---
id: IDX-mem-estrategica
titulo: Camada Estrategica da Memoria
tipo: relatorio
versao: 1.1.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-GOV
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: null
decisoes_relacionadas: [ADR-0001, ADR-0010]
substitui: []
substituido_por: null
resumo: Indexa a camada estrategica da memoria: o que pertence a ela, como um registro entra e quais registros existem.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-KMS
ratificacao: nao-exigida
---

# Camada EST — Memoria Estrategica

## Proposito
Guardar a identidade e a direcao da organizacao: o que nao muda com o projeto da semana.
Definicao completa em [FND-06 §3.1](../../foundation/06-arquitetura-memoria.md).

## Escopo
| Item | Definicao |
|---|---|
| Pergunta que responde | Por que existimos? Para onde vamos? |
| Volatilidade | Muito baixa — mudanca aqui e sempre evento formal |
| TTL | **Permanente.** Nao expira; e superada. |
| Autoridade em conflito | **1 — a mais alta.** Vence todas as demais camadas. |

## Responsaveis
| Papel | Responsavel |
|---|---|
| Dono | DEP-GOV |
| Escreve | **Somente DEP-GOV**, e somente mediante ADR aprovado |
| Le (obrigatorio) | Todos, antes de qualquer decisao C2 ou C3 |
| Curador | DEP-KMS |

---

## Pertence a esta camada
- Missao, visao, valores, principios imutaveis, linhas vermelhas
- Objetivos de longo prazo e criterios de sucesso organizacional
- **O catalogo de Capabilities** — o que a organizacao sabe fazer (FND-08)
- Estrutura organizacional vigente e direitos de decisao
- Decisoes de portfolio: por que um produto existe ou foi encerrado
- Posicionamento estrategico e apostas de longo prazo
- Restricoes permanentes impostas pelo Soberano
- Padroes duraveis de preferencia do Soberano sobre como o trabalho e feito

## **Nao** pertence
| Conteudo | Vai para |
|---|---|
| Detalhe de produto | PRD |
| Decisao tecnica | TEC |
| Estado de execucao | OPR |
| Aprendizado ainda nao consolidado | APR |
| Qualquer coisa com prazo de validade curto | OPR |

## Regra de escrita
> So entra em EST o que **sobreviveu a um horizonte inteiro** ou o que foi determinado
> diretamente pelo Soberano.

**Escrita em EST sempre exige ADR** (C2 ou C3). Nunca ha promocao automatica para esta
camada (FND-06 §5.2).

## Promocao para ca
| Origem | Criterio |
|---|---|
| APR → EST | A licao se confirmou em **≥ 2 ocorrencias independentes**, ou foi determinada pelo Soberano |
| PRD/TEC → EST | O fato deixou de ser especifico e virou principio da organizacao |

Em todos os casos: **ADR obrigatorio**.

## Registros

| ID | Titulo | Status | Ratificacao | Origem |
|---|---|---|---|---|
| [MEM-EST-0001](MEM-EST-0001-contexto-do-soberano.md) | Contexto do Soberano | **`ativo`** | **ratificada** | [ADR-0010](../../decisions/ADR-0010-contrato-de-conhecimento-do-soberano.md) |

**Contador oficial:** ultimo atribuido `0001` · proximo disponivel **`0002`**. Numero nunca e
reaproveitado (FND-03 §2.3).

> **Em vigor desde 2026-07-28.** O Soberano ratificou o registro **exatamente na versao
> canonica 1.0.0**, *"incluindo as afirmacoes registradas como unknown, que permanecem
> desconhecidas e nao podem ser preenchidas por inferencia"*. Fonte canonica:
> [MSG-2026-0002](../operacional/MSG-2026-0002-ato-soberano-cartas-comando-plataforma-e-contexto.md);
> vinculo ID × versao × **tres hashes** em §2 daquela Diretiva. **As 11 lacunas foram conferidas
> uma a uma e permanecem `unknown`** (V9).

> **A entrada em vigor nao preencheu nenhuma lacuna, e nao autoriza carregamento integral.**
> **CT-22** continua valendo: carregar alem do pacote aplicavel exige **gatilho declarado**, e o
> piso da consulta e **P1 = 28 linhas** — 9,9% do registro.

> **Residuo declarado (achado RE-02).** O **corpo** do registro ainda contem a nota *"Estado
> `aprovado`, nao `ativo`"*, escrita antes do ato. Corrigi-la seria **emenda** (ADR-0009) e
> produziria uma versao **1.1.0 nao ratificada** a partir de um ato que ratificou a **1.0.0**.
> **Ate a proxima emenda, o frontmatter e a fonte do estado** (PJ-04); a nota do corpo registra
> o estado **no ato de sua emissao**, como todo campo de estado congelado.

> O demais conteudo estrategico vigente vive em dois lugares, ambos parte desta camada:
>
> | Onde | O que | Ratificado por |
> |---|---|---|
> | [`../../foundation/`](../../foundation/) | Missao, visao, principios, estrutura, normas | ADR-0001, ADR-0002 |
> | [`../../capabilities/`](../../capabilities/) | O que a organizacao sabe fazer | ADR-0002 |
>
> MEM-EST-0001 **nao duplica** nenhum dos dois: registra conhecimento **sobre o Soberano** —
> quem ele e, o que declarou, o que recusa e o que nao se sabe —, que nenhum deles contem
> (MM-01). Onde a Fundacao ja diz algo, o registro **referencia** em vez de reproduzir (CT-05).

## Regime especial

Registro sobre o Soberano segue o Contrato de Conhecimento sobre o Soberano —
[ADR-0010 §5](../../decisions/ADR-0010-contrato-de-conhecimento-do-soberano.md), **fonte** das
regras, nao reproduzida aqui (PJ-01).

Template: [`TPL-memoria`](../../foundation/templates/TPL-memoria.md)

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-GOV | Indice inicial da camada, sem registros. |
| 1.1.0 | 2026-07-28 | DEP-GOV | Registra **MEM-EST-0001**, primeiro registro formal da camada, com contador oficial e regime especial de [ADR-0010](../../decisions/ADR-0010-contrato-de-conhecimento-do-soberano.md). Frontmatter passa a declarar os cinco campos do contrato de artefato (AC-08, **ADR-0009**). |
