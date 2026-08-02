---
id: RFC-0024-superacao-de-ato-por-evidencia-posterior
titulo: Deve existir caminho para superar um ato ja emitido quando prova posterior contradiz a condicao tecnica que o fundamentou?
tipo: rfc
versao: 1.0.0
status: aprovado
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-GOV
criado_em: 2026-07-31
atualizado_em: 2026-07-31
revisao_prevista: 2027-01-31
decisoes_relacionadas: [ADR-0012, ADR-0015, ADR-0020]
substitui: []
substituido_por: null
classe_mudanca: C3
prazo_analise: 2026-08-31
resumo: Submete a decisao de instituir caminho de superacao de ato soberano por evidencia posterior, preservando integralmente o ato original e reservando a decisao ao Soberano.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# RFC-0024: superacao de ato por evidencia posterior

## Proposito

Submeter a decisao de instituir um caminho pelo qual um **ato ja emitido** possa ser
**superado** — nunca editado, nunca anulado retroativamente — quando prova **posterior e
independente** contradiz a condicao tecnica sobre a qual ele foi emitido.

## Escopo

| Item | Definicao |
|---|---|
| **Inclui** | O caminho de superacao · quem instaura · quem decide · o efeito temporal · o registro de atos superados |
| **Nao inclui** | Edicao, anulacao ou reescrita de ato · recurso contra decisao **de merito** · qualquer poder novo a departamento algum · alteracao de [`ADR-0012`](../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md) |
| **Subordinado a** | [FND-01 §7.3 e §9](../foundation/01-constituicao.md) · [FND-04 §2](../foundation/04-governanca.md) |

## Responsaveis

| Papel | Quem |
|---|---|
| Proponente | **DEP-GOV** |
| Revisor | **DEP-QAR** |
| Valida a forma | **DEP-GOV** |

---

## 1. A lacuna, medida

**Ato emitido nao tem hoje mecanismo de revisao quando a prova o contradiz.**

| O que o acervo sabe fazer | Onde |
|---|---|
| Superar **artefato** | `O6` de `FND-10 §5.2`; `superado`/`revogado` de `FND-03 §12` e `FND-04 §4` |
| Garantir a **integridade** do ato | `IR-01` a `IR-12` de [`ADR-0012`](../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md) |
| **Superar o ATO** | **nao existe** |

**Medido nesta missao, sobre o acervo vigente:**

| Verificacao | Resultado |
|---|---|
| Atos soberanos no acervo | **7** — `MSG-2026-0001` a `MSG-2026-0007` |
| Estado de cada um | **`ativo`**, `substituido_por: null` — **7 de 7** |
| Atos ja superados | **`0`** |
| Ocorrencias de caminho de superacao de ato em norma vigente | **`0`** — a varredura sobre `foundation/`, `decisions/` e `governance/` so encontra o **diagnostico** desta lacuna, nunca a norma |

> `ADR-0012` torna o ato **integro e imutavel**, o que e certo. **A imutabilidade, sem caminho
> de superacao, vira imunidade a evidencia.**

## 2. A pergunta de decisao

**Deve existir esse caminho — e, existindo, quem instaura, quem decide, e o que acontece com o
que o ato ja produziu?**

## 3. Criterios de decisao

| # | Criterio | Peso | Como se mede |
|---|---|---|---|
| `K1` | O ato original permanece **byte a byte** | **Bloqueante** | `0` bytes tocados em qualquer `MSG` |
| `K2` | So o Soberano supera | **Bloqueante** | Nenhum departamento consegue desfazer decisao soberana sozinho |
| `K3` | Nao vira recurso permanente contra decisao | **Bloqueante** | Exige prova **posterior e independente**; releitura nao basta |
| `K4` | O que o ato ja produziu nao cai por padrao | Alto | Efeito prospectivo salvo declaracao expressa, item a item |
| `K5` | `ADR-0012` permanece integro | **Bloqueante** | `0` bytes; `IR-01`–`IR-12` viram **pre-condicao** do caminho |

## 4. Alternativas consideradas

### Alternativa A — Instituir o caminho: instaura-se com prova, supera-se por ato novo

| Campo | Conteudo |
|---|---|
| Descricao | `SA-1` a `SA-6`: superacao por ato novo do Soberano, com o ato superado citado por `id` e `H-A`, a condicao contradita citada literalmente, a prova por caminho e `sha256`, e o que passa a valer |
| A favor | Satisfaz `K1` a `K5`. **Acrescenta sem retirar**: `ADR-0012` vira pre-condicao, nao obstaculo |
| Contra | Cria caminho que alcanca o instrumento mais alto do acervo |
| Avaliacao | `K1` ✔ · `K2` ✔ · `K3` ✔ · `K4` ✔ · `K5` ✔ |

### Alternativa B — Tratar como incidente de conformidade (`INC`)

| Campo | Conteudo |
|---|---|
| Contra | **Falha em `K3` por inversao.** `INC-2026-001` e `INC-2026-002` trataram **ratificacao inferida** e **declarada em lugar errado** — defeitos de **forma do ato**. Aqui **a forma esta perfeita e o FATO e que mudou**. Incidente **registraria**; nao superaria. O ato errado seguiria de pe, agora com um `INC` ao lado |
| Avaliacao | `K1` ✔ · `K2` ✔ · `K3` **falha** · `K5` ✔ |

### Alternativa C — Permitir anotacao no ato original

| Campo | Conteudo |
|---|---|
| Contra | **Falha em `K1` e `K5`.** Editar ato e exatamente o que `ADR-0012` impede, e com razao. **Anotacao e edicao com outro nome**: muda `H-A`, dispara `IR-05` e abre incidente |
| Avaliacao | `K1` **falha** · `K5` **falha** |

### Alternativa D — Superacao automatica quando a prova contradiz

| Campo | Conteudo |
|---|---|
| Contra | **Falha em `K2`.** Retira do Soberano a decisao e a entrega ao detector. Um detector que pode desfazer ato soberano **e** autoridade soberana, sob outro nome |
| Avaliacao | `K2` **falha** |

### Alternativa Z — Nao fazer nada

| Campo | Conteudo |
|---|---|
| O que acontece | O ato permanece integro e imune. Registros aditivos empilham-se ao lado dele |
| Custo real da inacao | **`0` hoje** — nenhum dos 7 atos tem contradicao de prova conhecida. **O custo aparece inteiro no primeiro caso**, e a regra teria de ser escrita com o caso concreto a vista e sob pressao — **exatamente o que `ADR-0007 §6` recusou fazer com a fronteira** |
| Por que nao venceu | O momento barato de escrever a regra e o momento em que ela parece desnecessaria |

## 5. Recomendacao

**Alternativa A.** `B`, `C` e `D` falham cada uma num bloqueante diferente, e as falhas sao
estruturais, nao de calibragem.

## 6. A evidencia externa — declarada com o seu limite

A minuta que precede esta `RFC` cita um caso vivo fora do acervo, no laboratorio `SSC+`, em que
uma decisao `READY` permaneceu `ativo` enquanto duas decisoes posteriores registraram `ADJUST`,
e a prova que sustentava a primeira foi contradita.

| Campo | Conteudo |
|---|---|
| O que a evidencia mostra | **A forma do defeito**: cada missao registrou corretamente que *"a decisao anterior NAO foi reescrita"*, e o resultado foi um ato de pe contra a prova. **O defeito nao e de conduta; e de instrumento ausente** |
| **Limite declarado** | **`SSC+` NAO e acervo.** Todo registro dele declara `autoridade: nenhuma` e `normativo: nao`. **Nao e precedente, nao e norma, e nao vincula nada aqui** — e por isso serve de evidencia sem criar precedente (`FR-04` de `ADR-0007`: consultar nao e importar) |
| **Confianca** | **Media — declarada pela Missao 1.13.4.1 e NAO reconferida por esta.** Esta missao nao remediu o corpus do `SSC+`. **A ausencia de reconferencia fica declarada, nunca suprida por presuncao** (`PI-10`, `LV-12`) |

## 7. Impacto levantado

| Dimensao | Impacto |
|---|---|
| Norma revogada | **Nenhuma.** A lacuna e de **omissao**, nao de contradicao |
| `ADR-0012` | **`0` bytes.** `IR-01`–`IR-12` tornam-se **pre-condicao** do caminho: sem `H-A` registrado nao ha ato superavel identificavel |
| Fundacionais emendados | **`0`** — precedente literal: `ADR-0012` instituiu **12** regras `IR` com **`0`** fundacionais emendados |
| Atos superaveis hoje | **`0`** — os **7** estao consumidos e sem contradicao de prova conhecida |
| **Direito de decisao criado** | **`SA-4` cria o direito de INSTAURAR**, que hoje nao existe. **É o que torna a mudanca `C3`** |

## 8. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Evidencia de origem *(nao norma)* | `MINUTA-C-superacao-de-ato-por-evidencia-posterior.md`, `sha256` `b5cd82aeb06ebf5845f9b8a1aafc457df91d639e5df0c2da23319934d08e678a` |
| Decisao gerada | [ADR-0029](../decisions/ADR-0029-superacao-de-ato-por-evidencia-posterior.md) |
| Verificacao | [FIT-2026-022](../governance/fitness/FIT-2026-022-superacao-de-ato-por-evidencia-posterior.md) |

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-31 | DEP-GOV | Proposta inicial. Submete o caminho de superacao de ato, com **quatro** alternativas reais mais *"nao fazer nada"*. Lacuna **medida**: `7` atos `ativo`, `0` superados, **`0`** ocorrencias de caminho em norma vigente. Evidencia externa do `SSC+` citada **com o limite e a confianca declarados**. |
