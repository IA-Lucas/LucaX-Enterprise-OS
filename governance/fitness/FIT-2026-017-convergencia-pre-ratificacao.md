---
id: FIT-2026-017
titulo: Verificacao de aptidao da convergencia pre-ratificacao — os dois ritos novos e a consolidacao dos catorze objetos
tipo: fitness-check
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: DEP-QAR
proprietario: DEP-QAR
aprovador: DEP-EXE
criado_em: 2026-07-30
atualizado_em: 2026-07-30
revisao_prevista: null
decisoes_relacionadas: [ADR-0015, ADR-0020, ADR-0022, ADR-0023, ADR-0024, ADR-0025]
substitui: []
substituido_por: null
veredito: apto-com-ressalva
resumo: Verifica a aptidao evolutiva dos dois ritos da Missao 1.13.2 e da consolidacao dos catorze objetos, e conclui apto-com-ressalva com tres ressalvas novas e C11 conforme em 13 de 13.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-GOV
ratificacao: nao-exigida
---

# FIT-2026-017: Convergencia pre-ratificacao

> **Parecer, nao decisao** (`ADR-0015`, `FT-10`). Este documento **nao aprova, nao ratifica e nao
> promulga**. `FND-09 §8.2`, linha `FIT`: **ratifica `—`**.

## Proposito

Verificar a **aptidao evolutiva** dos dois ritos novos da Missao 1.13.2 — `RD-27` e `RD-37` — e
da **consolidacao** dos catorze objetos, e a conformidade **`C11`** de `FND-10 §11`.

## Escopo

| Item | Definicao |
|---|---|
| Avaliado | `RFC-0020` · `ADR-0024` · `ADR-0025` · `PS-2026-011` · `PS-2026-012` · `PS-2026-013` · `PS-2026-009` **2.0.0** · os **7** candidatos novos |
| **Nao** avaliado | O **merito** de `ADR-0018`, `ADR-0021`, `ADR-0022`, `ADR-0023`, **nao reabertos** · a **aplicacao**, que **nao ocorreu** · `RD-33`, `S1`, `S2`, `RD-36`, `RD-13` |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| Autor do parecer | **DEP-QAR** | `FND-09 §8.2`, linha `FIT` |
| Revisor de forma | **DEP-GOV** | idem |
| Aprova | **DEP-EXE** | idem |

> **Impedimento parcial declarado e resolvido por recorte — precedente `FIT-2026-003` e
> `R4` de `FIT-2026-016`.** `DEP-EXE` e **autor de `ADR-0025` e de `PS-2026-012`**, que este
> parecer avalia. **A parte impedida — `F1` a `F6` e `C11` quanto a `ADR-0025` e `PS-2026-012` —
> e aprovada por `DEP-GOV`**; o restante, por `DEP-EXE`. **`DEP-QAR` nao e autor de nenhum objeto
> avaliado**, e por isso a autoria do parecer **nao** e impedida.

## Sumario

| Dimensao | Resultado |
|---|---|
| `F1` complexidade × ganho | ✅ **`0`** regras normativas criadas; **`2`** nao conformidades fechadas; **`11 → 0`** afirmacoes falsas |
| `F2` duplicacao e prevencao | ✅ **`0`** duplicacoes; prevencao **barrou 3 reproducoes** |
| `F3` abstracao desnecessaria | ✅ **4** abstracoes evitadas, cada uma com a regra que a dispensa |
| `F4` simplicidade de evoluir | ✅ **melhora medida**; **1** dimensao piora, e a piora e declarada |
| `F5` custo de contexto | ✅ **decima primeira** medicao da serie |
| `F6` reutilizacao | ✅ **5** metodos reutilizaveis |
| **`C11`** | ✅ **13 de 13 conformes** |
| **Veredito** | **`apto-com-ressalva`** — **3** ressalvas novas |

---

## F1 — A complexidade aumentou sem ganho proporcional?

### F1.1 O acrescimo, medido

| O que entrou | Quantidade |
|---|---|
| Artefatos novos | **8** — `RFC-0020`, `ADR-0024`, `ADR-0025`, `PS-2026-011`, `PS-2026-012`, `PS-2026-013`, e **`FIT-2026-017`** e **`PT-2026-009`** |
| **Regras normativas novas** | **`0`** — nenhuma `AC-*`, `IR-*`, `CE-*`, `PJ-*`, `SF-*`, `MI-*`, `IV-*` |
| **Titulares, portoes, papeis, classes, verbos, entidades, tipos documentais** | **`0` criados** |
| Linhas de **norma** acrescidas pelos candidatos | **+21** *(`FND-01` +8 · `FND-02` +6 · `FND-10` +7)* **+3** *(1 por Carta)* = **24** |
| Excecoes formais | **`0`** — `governance/exceptions/` permanece **vazio** desde a fundacao |

### F1.2 O ganho, medido

| Ganho | Antes | Depois |
|---|---|---|
| **Nao conformidades de contrato conhecidas** | **2** | **`0`** |
| **Valores falsos em `FND-10 §8.5`** | **5** | **`0`** |
| **Afirmacoes falsas sobre `QG-1` nas 9 Cartas** | **11 em 4** | **`0` em `0`** |
| **Variantes vivas de `FND-01`** | **2** | **1** |
| **Sobreposicao de diff entre objetos do ato** | **1** *(`FND-01`)* | **`0`** |
| Achados fechados | — | **`RD-27`**, **`RD-37`**, **`RD-45`**, **`RD-46`** |

> **O ganho e desproporcional ao acrescimo, e no sentido favoravel:** `0` regras novas fecharam
> **quatro** achados e eliminaram **16** afirmacoes falsas ou nao conformes. **O que cresceu foi
> instrumento de decisao, nao norma** — pela segunda missao consecutiva.

## F2 — Algum conceito foi duplicado? E a prevencao foi aplicada?

### a) Houve duplicacao?

**Nao.** Uma projecao foi criada — a **matriz de `PS-2026-013 §2`** — e ela **declara `PJ-02`
com as quatro informacoes** *(fonte, campos, finalidade, metodo de atualizacao)* **e `projecao_de`
no frontmatter**, que a torna detectavel por varredura.

### b) A prevencao de `PJ-05` foi aplicada, com evidencia?

**Sim, e barrou tres reproducoes:**

| # | O que seria reproduzido | Como foi resolvido |
|---|---|---|
| 1 | Os **hashes de `ADR-0023`** na matriz consolidada | **Remedidos**, nao copiados — e a remedicao **reproduziu a fonte digito a digito**, virando o **vigesimo controle** |
| 2 | O **diff de `FND-01`** repetido em `PS-2026-009` e `PS-2026-011` | `PS-2026-009` **2.0.0 remete**; `§2.1` e `§5` marcadas **SUPERADAS** |
| 3 | A **minuta do ato** em quatro pacotes | **Uma unica** em `PS-2026-013 §6`; a de `PS-2026-009 §9` marcada **SUPERADA** com a razao |

**Decima sexta confirmacao de `MEM-APR-0002`.**

## F3 — Alguma abstracao ficou desnecessaria?

| Abstracao evitada | Regra que a dispensa |
|---|---|
| **Tipo documental novo** para "revisao independente" | `FND-09 §8.2` ja atribui `revisor`; o precedente `PS-2026-002`/`003`/`006` a materializa como **secao do pacote** |
| **Campo novo** de frontmatter para vincular valor a baseline | `CE-04` ja exige fonte e valor observado; bastou **regra de leitura em `§8.5`** |
| **Emenda a `IR-03`** para baratear o backfill | `IR-04` — e o risco `RR-1` de `RFC-0009`: mexer na protecao para evitar o ato que ela existe para exigir |
| **Excecao formal** a `AC-06` | Excecao e para o que **nao se pode** fazer; isto **se podia fazer hoje** |

## F4 — O sistema continua mais simples de evoluir?

| Dimensao | Efeito | Medida |
|---|---|---|
| **Ato soberano** | **Melhora forte** | De **4 pacotes a reconciliar** para **1 matriz e 1 minuta** |
| **Bloqueio isolado** | **Melhora** | De **1 sobreposicao** para **`0`**; **14 objetos, 14 arquivos** |
| **Leitura de `§8.5`** | **Melhora** | O valor passa a **envelhecer como historico datado** em vez de virar afirmacao falsa |
| **Emendar `FND-01`, `FND-02`, `FND-10`** | **Piora, e de proposito** | Os tres passam a declarar mais campos, e **todo campo declarado e campo a manter**. `AC-01` foi respeitada — **nenhum e derivavel** —, mas o custo de manutencao **sobe** |

> **A unica dimensao que piora esta declarada, e o sentido do tradeoff e o mesmo da missao
> anterior:** cumprir contrato **encarece a manutencao e protege o consumidor**. Quem le `FND-02`
> hoje precisa abrir o catalogo para saber o resumo, o perfil e o revisor; depois, **nao precisa**.

## F5 — A mudanca reduz ou aumenta o custo de contexto?

### F5.1 A medicao — **a decima primeira da serie**

| Item | Linhas |
|---|---|
| Fontes consumidas *(`FND-01`, `FND-02`, `FND-04 §2`, `FND-09 §8.2`, `FND-10 §2`, `§8.5`, `§10.3`, `ADR-0012`, `ADR-0020 §10`, `ADR-0022`, `ADR-0023`, `RFC-0019 §3`, `PS-2026-009`, `PS-2026-010`, `RD-27`, `RD-37`)* | **~2.100** |
| Candidatos medidos *(7 novos + 6 preservados)* | **~5.400** *(medidos por ferramenta, **nao lidos integralmente**)* |
| **Linhas de evidencia externa lidas** | **`0`** |

### F5.2 Comparabilidade — declarada

**Favoravel, e a razao e estrutural:** a missao **nao escreveu norma** — ela **corrigiu metadado e
uma secao de medicao**, e **construiu instrumento por ferramenta**. A parte cara foi **medir**, e
a medicao e reutilizavel: o mesmo modulo validou **20 controles** e mediu **14 objetos**.

### F5.3 O que **nao** foi carregado, e por que conta

**`0` linhas externas.** **`0` leituras integrais de candidato** — os 13 candidatos foram
**medidos**, e o unico lido por inteiro na comparacao foi `FND-11`, para a prova `SF-01`–`SF-32`.
**O `diff` substituiu a leitura em 11 de 12.**

## F6 — Ela favorece reutilizacao?

| # | Metodo reutilizavel | Onde |
|---|---|---|
| 1 | **Validar o instrumento contra controles publicados antes de medir objeto novo** — 20 de 20 | `PS-2026-011 §4.3` |
| 2 | **Construir o cumulativo e comparar, em vez de reler a variante** — foi assim que `RD-45` apareceu | `PS-2026-011 §2.3` |
| 3 | **Vincular valor medido a baseline nomeada**, para que envelheca como historico e nao como mentira | `FND-10 §8.5` candidato |
| 4 | **Medir a alternativa antes de discuti-la** — a `ALT` de `FND-01` e o recalculo de `ADR-0020` | `PS-2026-011 §2.4`, `PS-2026-013 §5` |
| 5 | **Remedir o custo declarado de uma decisao `M1` em vez de reler** — o que estava contado ficou estavel; o que **nao** estava triplicou | `PS-2026-013 §5` |

> **O mais forte e o `5`.** `ADR-0020 §10` mediu *"1 ADR + 6 indices"* e **acertou** — os 6
> continuam 6. **O defeito nao estava no que foi medido, e sim no que nao entrou na conta**:
> referencias penduradas em artefato **imutavel**, de **4 para 12** em duas missoes. **Isso so
> aparece remedindo.**

---

## C11 — Conformidade de [FND-10 §11](../../foundation/10-artifact-framework.md)

| # | Verificacao | Resultado |
|---|---|---|
| 1 | Contrato **L1** completo nos artefatos novos | ✅ **8 de 8** declaram os **cinco** campos |
| 2 | `revisor` ≠ `autor` | ✅ **8 de 8** — e **`0` coincidencias em 125** artefatos do acervo com os dois campos, remedido apos as edicoes |
| 3 | `ratificacao` coerente com a classe | ✅ `ADR-0024` e **C3 · Tipo 2** → **`pendente`**; `ADR-0025` e `C2 · Tipo 2` → **`nao-exigida`**; os 3 candidatos de Carta → **`pendente`**; os 3 candidatos `FND` → **`ratificada`**, pelo regime de `PS-2026-009 §4.1`, **com a assimetria declarada como `RD-47`**. **Nenhum objeto `C3`/`Tipo 1` declara `nao-exigida`** |
| 4 | Tipo documental consta de FND-10 §4 | ✅ `RFC` §4.2 · `ADR` §4.2 · `Reporte` §4.6 · `Fitness Check` §4.5 · `Relatorio de transicao` §4.7. **Nenhum tipo novo** |
| 5 | Atributo **derivavel** declarado em frontmatter | ✅ **`0`** — `AC-01` respeitada; os 9 campos do backfill sao **L1 declarado**, nao derivado |
| 6 | Cadeia **origem → estado → substituicao** percorrivel | ✅ **8 de 8.** `PS-2026-009` **1.0.0 → 2.0.0** com a anterior **preservada e hasheada**; `V1`/`V2` **aposentados com razao registrada, nao apagados** |
| 7 | Custo de contexto **medido**, nao estimado | ✅ Todas por ferramenta. **Duas estimativas aparecem, e as duas estao rotuladas** — o custo de `RD-37` em `PS-2026-010 §9.1` e o consumo de `F5.1` |
| 8 | Entrada no catalogo mestre presente | ✅ **8 de 8** |
| 9 | Divisao com menos de dois sinais | ✅ **Nenhuma divisao proposta** |
| 10 | Tabela reproduzida **sem** declaracao de projecao | ✅ **`0`.** A matriz de `PS-2026-013 §2` declara `PJ-02` com as **quatro** informacoes **e** `projecao_de` no frontmatter |
| 11 | **Teste preventivo de projecao aplicado, com evidencia** | ✅ **Aplicado, e com efeito: barrou 3 reproducoes** — `F2.b` |
| 12 | Conteudo de origem externa fora do portao | ✅ **`0` admitidos · `0` linhas lidas** |
| 13 | Alteracao de conteudo **sem** incremento de versao | ✅ **`0`.** Os candidatos declaram **1.7.0**, **1.4.0**, **1.5.0** e **1.1.0** ×3, cada um com linha de historico (`AC-11`); `PS-2026-009` sobe a **2.0.0**; os indices `M3` sao isentos por `AC-09` |

**13 de 13 conformes.**

---

## Ressalvas

| # | Ressalva | Consequencia se nao tratada | Dono | Gatilho |
|---|---|---|---|---|
| **`R1`** | **`FND-01` 1.7.0 nao e aplicavel sem `FND-11`.** O candidato escreve **link markdown vivo** para `11-framework-specifications.md`. **A `ALT` existe e esta medida**, mas **e o ato que precisa escolher** — nao ha versao unica que sirva aos dois cenarios | Se o ato promulgar `FND-01` e bloquear `FND-11`, o acervo ganha **1 link quebrado** e uma hierarquia que **enumera documento inexistente** | **SOBERANO** | **O proprio ato** — `Q2` de `PS-2026-011 §9` |
| **`R2`** | **Primeira dispensa de RFC do acervo.** Legitima — `FND-04 §2`, duas condicoes verificadas, concordancia escrita entre partes distintas —, **e e precedente** | O proximo caso pode **invocar** este em vez de **reverificar as duas condicoes** | **DEP-GOV** | **Proxima decisao `C2` que dispense RFC** |
| **`R3`** | **`RD-47` — o regime de estado na promulgacao de versao nova e costume, nao regra escrita.** Carta volta a `em-revisao`/`pendente`; fundacional permanece `ativo`/`ratificada`. **Os dois sao precedentes vigentes e nenhuma regra os distingue** | O **`H-P`** de todo objeto futuro depende de qual precedente se aplica, e a escolha **nao e derivavel de norma** | **DEP-GOV** | **Proxima emenda de `FND-10 §5`** |

### Ressalvas anteriores — situacao

| # | Origem | Situacao |
|---|---|---|
| **`R2`** de FIT-2026-014 *(`RD-27`)* | 2026-07-29 | ✅ **FECHADA no candidato** — `ADR-0024`. **Vigora com o ato** |
| **`R3`** de FIT-2026-016 *(`FND-01` sem `AC-08`)* | 2026-07-29 | ✅ **FECHADA** — a variante que a repetia **deixou de ser objeto** |
| **`R2`** de FIT-2026-016 *(`RD-37`, 3 Cartas)* | 2026-07-29 | ✅ **FECHADA no candidato** — `ADR-0025` |
| **`R1`** de FIT-2026-016 *(`ADR-0021` nao dira que foi superado)* | 2026-07-29 | 🔁 **ABERTA e reafirmada.** O Soberano decidiu **nao gravar `superado_por`**; **`RD-43`** permanece declarado |
| **`R4`** de FIT-2026-016 *(impedimento parcial de `DEP-EXE`)* | 2026-07-29 | 🔁 **RECORRE, e resolvida pelo mesmo recorte** — ver §Responsaveis |
| **`R1`** de FIT-2026-014 *(`PA-07` supletiva sem membro observado)* | 2026-07-29 | 🔁 **ABERTA, inalterada** |

## Veredito

| Campo | Valor |
|---|---|
| **Veredito** | **`apto-com-ressalva`** |
| **Por que nao `apto`** | **`R1` e uma escolha real que so o ato pode fazer**, e ela nao e cosmetica: um dos dois cenarios deixa o acervo com link quebrado. **Declarar nao e resolver** |
| **Por que nao `inapto`** | **`0`** regras normativas criadas; **`0`** fontes do acervo alteradas; **`C11` 13 de 13**; **`20 de 20`** controles de integridade reproduzem; **quatro** achados fechados e **`16`** afirmacoes falsas ou nao conformes eliminadas. **Nada aqui aumenta o custo de evoluir sem ganho declarado** |
| **`0` objetos entraram em vigor** | Confirmado por `cmp` — §Fechamento |

## Fechamento

| Verificacao | Resultado |
|---|---|
| **Fontes normativas alteradas** | **`0`** — `foundation/*.md`, `departments/` e `capabilities/` **byte a byte identicos** a `BL-2026-07-29-10`, por `cmp` contra a copia datada |
| **Artefatos `M1` editados** | **`0`** — inclusive `ADR-0020`, `ADR-0021`, `ADR-0022`, `ADR-0023` |
| **`MSG`, `FIT` e baselines historicas editadas** | **`0`** |
| **Candidatos historicos editados** | **`0`** — `V1`, `V2` e os 4 de 2026-07-29 **intactos** |
| **Artefato do acervo emendado** | **1** — `PS-2026-009` **1.0.0 → 2.0.0**, com a anterior **preservada e hasheada**, e **`M3`** por tipo |
| **Credencial em texto** | **`0`** no acervo **e** nos **13** candidatos |
| **Objetos em vigor por esta missao** | **`0`** |

## Pendencias para o SOBERANO — **quatro, e uma bloqueia**

| # | Pendencia | Bloqueia? |
|---|---|---|
| 1 | **`S1` com Produto real** *(`nXtrack`)* — **`RD-33`** | **SIM** — nenhuma `Spec` e criavel |
| 2 | **O ato consolidado** — os catorze objetos de `PS-2026-013 §6` | Nao |
| 3 | **`Q2` de `PS-2026-011`** — `FND-01` cumulativa ou `ALT` | Nao *(so se `FND-11` for bloqueado)* |
| 4 | **`Q1` de `PS-2026-011`** — `ADR-0024` `Tipo 2` ou `Tipo 1` | Nao *(nao altera hash)* |

## Aprendizado gerado

| # | Licao | Confirmacao |
|---|---|---|
| 1 | **A variante medida em missao anterior nao e candidato de rito proprio.** `V2` foi montado como **alternativa**, e por isso atribuiu a autoria ao ADR que a media — nao ao que a decidiria. **Reaproveitar sem reatribuir produz afirmacao falsa dentro da norma** | **`RD-45`** — nova |
| 2 | **Achado que conta valores conta os que olhou.** `RD-27` item *(c)* nomeou **tres** e a secao tinha **cinco** — os dois nao contados estavam **na mesma frase** | **`RD-46`** — nova |
| 3 | **Custo declarado de decisao `M1` envelhece na parte que ninguem contou.** Os 6 indices continuaram 6; as referencias imutaveis foram de 4 a 12 | **`RD-48`** — nova |
| 4 | **Medir antes de discutir, de novo** — `MEM-APR-0006`, decima sexta confirmacao | `RD-45`, `RD-48` |

## Historico de vereditos sobre este objeto

| Data | Veredito | Objeto |
|---|---|---|
| 2026-07-30 | **`apto-com-ressalva`** | Missao 1.13.2 — convergencia pre-ratificacao |

---

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-30 | DEP-QAR | Verificacao de aptidao da **Missao 1.13.2**. Veredito **`apto-com-ressalva`**, com **tres** ressalvas novas — **`R1`** *(`FND-01` 1.7.0 **nao e aplicavel sem `FND-11`**, e a `ALT` medida **nao dispensa a escolha do ato**)*, **`R2`** *(**primeira dispensa de RFC do acervo** — legitima, e precedente que **se reverifica, nao se invoca**)* e **`R3`** *(**`RD-47`** — o regime de estado que define o `H-P` e **costume, nao regra escrita**)*. **Tres ressalvas anteriores FECHAM:** `R2` de `FIT-2026-014` e `R2`/`R3` de `FIT-2026-016`. **`F1`:** **`0`** regras normativas criadas, **`0`** titulares, **`0`** fontes do acervo alteradas — e o ganho e **desproporcional no sentido favoravel**: `0` regras novas fecharam **quatro** achados e eliminaram **16** afirmacoes falsas ou nao conformes. **`F2`:** nenhuma duplicacao, e a prevencao de `PJ-05` **barrou tres reproducoes** — a primeira delas produziu efeito colateral util, porque **remedir os hashes de `ADR-0023` em vez de copia-los** transformou-o no **vigesimo controle**. **`F3`:** **quatro** abstracoes evitadas, cada uma com a regra que a dispensa — inclusive a **primeira excecao formal do acervo**, recusada por ser **para o que nao se pode fazer**. **`F4`:** a unica dimensao que piora **piora de proposito**, e o tradeoff e o mesmo da missao anterior: **cumprir contrato encarece a manutencao e protege o consumidor**. **`F5`:** decima primeira medicao da serie, com **`0` linhas de evidencia externa** e **`0` leituras integrais de candidato** — o `diff` substituiu a leitura em **11 de 12**. **`F6`:** cinco metodos reutilizaveis, e o mais forte e **remedir o custo declarado de uma decisao `M1`**: `ADR-0020 §10` **acertou no que contou** — 6 indices continuam 6 — e o defeito estava **no que nao entrou na conta**, referencias penduradas em artefato imutavel, de **4 para 12** em duas missoes. **`C11`: 13 de 13 conformes.** **Impedimento parcial de `DEP-EXE` declarado e resolvido por recorte**, precedente `FIT-2026-003`. **Quatro pendencias para o SOBERANO, e uma bloqueia — `RD-33`, que continua sendo a unica.** **`0` objetos entraram em vigor · `0` fontes normativas alteradas · `0` artefatos `M1` editados · `0` candidatos historicos tocados · `0` credenciais em 185 artefatos e 13 candidatos.** |
