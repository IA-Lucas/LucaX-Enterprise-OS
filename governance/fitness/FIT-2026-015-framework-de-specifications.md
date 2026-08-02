---
id: FIT-2026-015-framework-de-specifications
titulo: Aptidao arquitetural do Framework de Specifications — SF-01 a SF-32, correcao de RD-23 e o bloqueio medido dos dois pilotos
tipo: fitness
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-QAR
proprietario: DEP-QAR
aprovador: DEP-EXE
criado_em: 2026-07-29
atualizado_em: 2026-07-29
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0012, ADR-0015, ADR-0018, ADR-0019, ADR-0020, ADR-0021]
substitui: []
substituido_por: null
objeto_avaliado: [RFC-0017, ADR-0021, TPL-spec, PT-2026-007, MEM-APR-0006]
classe_mudanca: C2
classe_avaliacao: aptidao
veredito: apto-com-ressalva
resumo: Verifica se instituir o Framework de Specifications dentro de um ADR deixou a arquitetura mais apta a evoluir; veredito apto-com-ressalva, tres ressalvas novas, C11 integral e ADJUST por impossibilidade normativa dos pilotos.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-GOV
ratificacao: nao-exigida
---

# FIT-2026-015: Framework de Specifications

## Proposito
Verificar, de forma independente, se a Missao 1.13 deixou a arquitetura **mais apta a evoluir** —
e nao apenas correta —, respondendo as seis perguntas de
[FND-09 §10.3](../../foundation/09-meta-model.md) sobre a instituicao de `SF-01` a `SF-32`, a
correcao de `RD-23` e a decisao de **nao criar** as duas Specs piloto.

## Escopo
| Item | Definicao |
|---|---|
| **Objeto avaliado** | [RFC-0017](../../rfcs/RFC-0017-framework-de-specifications.md) · [ADR-0021](../../decisions/ADR-0021-framework-de-specifications.md) · [`TPL-spec`](../../foundation/templates/TPL-spec.md) **1.1.0** · [PT-2026-007](../relatorio-transicao-2026-07-29-specifications.md) · [MEM-APR-0006](../../memory/aprendizado/MEM-APR-0006-exercer-o-contador-revela-o-defeito.md) · [catalogo mestre](../artifact-registry.md) |
| **Nao avaliado** | O **merito da classe `C2`** *(decisao de DEP-EXE)* · o **merito da escolha entre `S1` e `S2`** *(decisao do SOBERANO)* · `RD-24`, `RD-27`, `RD-28`, `RD-30`, `RD-10` a `RD-13`, `RD-18`, `RD-21` · as Cartas *(materia de ato)* |
| Natureza | **Parecer**, `M1`, que **nao se ratifica** — `FT-10` de [ADR-0015](../../decisions/ADR-0015-fitness-check-e-parecer-nao-decisao.md) |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| **Executa a verificacao** | **DEP-QAR** | FND-09 §10.5; `CV-08` — **nao produziu nenhum dos objetos avaliados** |
| **Revisa a forma** | **DEP-GOV** | FND-09 §8.2, linha `FIT` |
| **Aprova** | **DEP-EXE** | FND-09 §8.2, linha `FIT` |
| **Ratifica** | **—** | `FT-10` — parecer nao se ratifica |
| **Nao participa como produtor** | **DEP-PRD** | `PI-05`, `LV-03` — **DEP-PRD e autor de RFC-0017, ADR-0021 e `TPL-spec` 1.1.0, e por isso nao os verifica** |

> **A separacao desta missao e a mais ampla do acervo, e isso e verificavel.** Autor **DEP-PRD** ·
> revisores **DEP-ENG + DEP-QAR** · aprovador **DEP-EXE** · aprovador do `TPL` **DEP-GOV** ·
> verificador **DEP-QAR** · registrador **DEP-GOV**. **Nas quatorze missoes anteriores, DEP-GOV
> foi autor de todo instrumento normativo.** Nesta, **de nenhum** — e e a resposta material a
> exigencia `RC-02`.

---

## Sumario

| Pergunta | Resposta |
|---|---|
| **F1** — A complexidade aumentou sem ganho proporcional? | **Nao** — **32 regras** e **2 matrizes** contra **4 achados em 4 missoes** e **0** fontes emendadas; o consumidor sai de **5 fontes** para **1 ADR + 1 template** |
| **F2** — Algum conceito foi duplicado? E a prevencao foi aplicada? | **Nao** duplicou; a prevencao **foi aplicada e barrou tres reproducoes** |
| **F3** — Alguma abstracao ficou desnecessaria? | **Nao** — e **quatro** foram evitadas: nenhum `FND`, entidade, tipo documental ou registro novo |
| **F4** — O sistema continua mais simples de evoluir? | **Sim, e com um custo declarado:** a Spec ganhou contrato, **e a impossibilidade de exerce-lo ficou escrita em vez de contornada** |
| **F5** — Reduz ou aumenta o custo de contexto? | **Aumenta no ciclo, reduz no uso** — **3.814 linhas · 8,23%** de pacote, com comparabilidade declarada; o consumo futuro da norma cai a **1 bloco de requisito** |
| **F6** — Favorece reutilizacao? | **Sim** — **7 metodos reutilizaveis**, e o mais forte foi **exercer o instrumento em vez de le-lo** |
| **C11** — Conformidade de FND-10 §11 | **13 de 13 verificacoes conformes** |
| **Veredito** | **`apto-com-ressalva`** — **tres** ressalvas novas, todas com dono e gatilho |

---

## F1 — A complexidade aumentou sem ganho proporcional?

**Nao. O ganho e maior que o acrescimo, e as duas grandezas foram medidas.**

### F1.1 O acrescimo

| Objeto | Quantidade | Onde vive |
|---|---|---|
| Regras normativas novas | **32** — `SF-01` a `SF-32` | **Dentro de `ADR-0021`**, artefato `M1` |
| Matrizes novas | **2** — Spec Contract *(21 blocos)* e `C0`–`C3` × `Tipo 1/2` *(50 celulas)* | Idem, **ambas declaradas `PJ-02`** |
| Artefatos criados | **5** | `RFC-0017` · `ADR-0021` · `FIT-2026-015` · `MEM-APR-0006` · `PT-2026-007` |
| Artefatos `M2` alterados | **1** | `TPL-spec` **1.0.0 → 1.1.0** |
| **Fontes de `foundation/` emendadas** | **0** | Verificado por `cmp` contra a copia datada |
| **Entidades · tipos documentais · portoes · papeis · classes · verbos de autoridade** | **0 criados · 0 alterados** | Contagem antes/depois em `FND-09 §5`, `§8.1`, `FND-10 §4`, `FND-01 §6.2` |
| Titulares ampliados | **0** | As **50** celulas nomeiam apenas nomes de `FND-04 §2` e `FND-09 §8.2` — conferido nome a nome |

### F1.2 O ganho, medido

| Sinal | Valor | Como se mediu |
|---|---|---|
| **Achados sobre `Spec` por ausencia de contrato** | **4 em 4 missoes consecutivas** — `RD-14`, `RD-15`, `RD-18`, `RD-23` | Catalogo §7, achados 35, 36, 39 e 44 |
| **Fontes que o consumidor da norma da Spec precisava ler** | **5**, em **6** secoes — `FND-01 §6.2`, `FND-03 §3.6`, `FND-04 §2` e `§6`, `FND-09 §8.2`, `FND-10 §10.3` | Leitura das citacoes de `TPL-spec` 1.0.0 e de `DEP-PRD §5` |
| **Depois** | **1 ADR `sob-demanda` + 1 template**, e para uma exigencia especifica, **1 bloco de requisito** (`SF-31`) | `ADR-0021 §5` |
| **Defeitos de `RD-23` declarados × medidos** | **2 declarados · 5 medidos** | `ADR-0021 §5.11`, campo a campo contra `FND-10 §2.2` |
| **Achados novos produzidos por esta missao** | **6** — `RD-31`, `RD-32`, `RD-33`, `RD-34`, `RD-35`, `RD-36` | §F6 |

> **A prova de que o acrescimo nao e gordura esta em `T-12`.** O framework, ao ser **exercido**
> sobre a propria pergunta que a missao mandou testar — *"consumo por futura Skill sem
> interpretacao informal"* —, **devolveu uma resposta errada** e **soube dizer que era errada**.
> Um framework que so confirma o que ja se sabia nao produz achado. Este produziu **seis**.

## F2 — Algum conceito foi duplicado? E a prevencao foi aplicada?

### a) Houve duplicacao?

**Nao, e a verificacao foi feita objeto a objeto.**

| Risco de duplicacao | Verificacao | Resultado |
|---|---|---|
| Matriz de autoridade reproduzida de `FND-09 §8.2` | `ADR-0021 §5.3` declara `PJ-02` com as **quatro** informacoes e projeta **etapa × titular**, nao a matriz de entidades | ✅ **projecao, nao reproducao** |
| Contrato de artefato reproduzido de `FND-10 §2.2` | `ADR-0021 §5.2` declara `PJ-02` e projeta **quais blocos a Spec deve conter**, remetendo a fonte de cada exigencia | ✅ idem |
| Classes de mudanca redefinidas | `SF-10` **remete** a `FND-04 §2`; **nao redefine** nenhuma classe | ✅ |
| Relacoes de linhagem redefinidas | `SF-21` declara as seis como **leitura das dez de `FND-09 §6.1`**, com a relacao oficial de cada uma em coluna propria | ✅ |
| **Registro mestre de Specs** duplicando o catalogo | `SF-32` **recusa criar registro novo** e aponta o catalogo existente (`RG-04`) e o indice do diretorio (`FND-03 §2.3`) | ✅ **duplicacao evitada por regra** |

### b) A prevencao de `PJ-05` foi aplicada, com evidencia?

**Sim, e ela barrou tres reproducoes** — `PJ-06` exige as duas respostas, e as duas estao aqui.

| # | O que ia ser reproduzido | Onde foi barrado | O que ficou no lugar |
|---|---|---|---|
| 1 | Os **oito criterios `K1`–`K8`** de avaliacao | `ADR-0021 §3` | **Remissao** a `RFC-0017 §4`, com `PJ-01` citado |
| 2 | As **cinco alternativas + Z** com custo e afetados | `ADR-0021 §4` | **Remissao** a `RFC-0017 §5`, com `PJ-01` e `CM-09` citados |
| 3 | A **tabela de classes `C0`–`C3`** de `FND-04 §2` | `ADR-0021 §5.3` | **Projecao de etapa × titular**, que e informacao nova, com `PJ-02` declarado |

**Decima quarta confirmacao consecutiva de [MEM-APR-0002](../../memory/aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md).**

## F3 — Alguma abstracao ficou desnecessaria?

**Nao — e quatro foram deliberadamente evitadas.** A recusa e o resultado mais forte desta
verificacao.

| Abstracao possivel | Por que seria natural | Por que foi recusada |
|---|---|---|
| **`FND-11` — Specification Framework** | E a forma que `FND-08`, `FND-09` e `FND-10` usaram | **C3** + emenda a `FND-01 §10`; a missao veda tocar `FND-01`. `RFC-0017` Opcao A |
| **Entidade ou tipo documental por perfil** *(`SPC-DADOS`, `SPC-SEGURANCA`…)* | Sete perfis convidam a sete tipos | **`SF-18` proibe expressamente.** Criar entidade e **C3 · Tipo 1** com **7 testes `TE`** (`FND-09 §11.1`), e `SF-19` exige **dois sinais observados** — **ha zero** |
| **`conflita` como relacao no grafo** | Seria simetrico as outras cinco | **`SF-22` a recusa** com o mesmo fundamento de `restringe` em `FND-10 §7.1`: criaria dependencia sem direcao e violaria `PD-11`. **Virou achado, que e o que ela e** |
| **Registro mestre de Specs proprio** | *"Manter registro mestre"* foi pedido | **`SF-32` recusa:** o catalogo **ja e** a visao transversal (`RG-04`), e arquivo satelite por artefato e proibido (`RG-05`). **Manter um registro nao e criar um segundo** |

> **Uma abstracao foi mantida sob observacao, e o registro diz isso.** `SF-09` institui **21
> blocos** obrigatorios de corpo. **Nao ha Spec real para medir se sao caros**, e `RA-6` de
> `ADR-0021` declara o gatilho: **`CE-05`, quando a primeira Spec for medida contra o dobro da
> mediana do tipo.** Registrado como ressalva **`R2`**.

## F4 — O sistema continua mais simples de evoluir?

**Sim — e a resposta tem duas metades, e a segunda e a que importa.**

**Primeira metade: a Spec passou a ter contrato sem custo normativo.** As tres decisoes
anteriores sobre Spec — `ADR-0018`, `ADR-0019`, `ADR-0020` — foram `C3`, `C3` e `C2`, e as duas
primeiras **emendaram fonte fundacional** e **consumiram ato soberano**. Esta institui o
contrato inteiro com **`0` fontes emendadas e `0` atos consumidos**. **Evoluir a norma da Spec
ficou mais barato: superar um ADR `C2 · Tipo 2` custa 1 ADR + 8 indices `M3`, contra 1 RFC + 1
ADR + 1 pacote + 1 ato.**

**Segunda metade: a impossibilidade de exercer a norma ficou escrita.** Havia duas saidas
faceis, e as duas seriam violacao:

| Saida facil | Norma que a proibe | Consequencia se tomada |
|---|---|---|
| Escrever as Specs piloto em outro diretorio | `FND-03 §3.6`, `FND-03 §7.1`, `FND-10 §4.4` | Artefato fora do local canonico — **nulo** por `MT-01`; incidente por `LV-11` |
| Criar `products/` e uma Carta de Produto | `FND-04 §6` — **C2 · Tipo 1 do SOBERANO**; restricao expressa da missao | Componente criado sem competencia — `LV-06`, `LV-07` |
| **Declarar o bloqueio com as fontes e as duas saidas** | `PI-10`, `LV-05` | **E o que foi feito** |

**DEP-QAR verificou as tres fontes uma a uma, na fonte vigente, e confirma:** `FND-04 §6`, linha
*Spec*, exige **`Produto existe`** e declara que *"**todas** precisam ser verdadeiras"*;
`FND-03 §3.6` e `FND-10 §4.4` alojam a Spec em `products/<slug>/specs/`. **Medido de forma
independente:** `products/` **ausente** das entradas da raiz; **`0`** artefatos `tipo: spec`;
**`0`** artefatos de produto. **A conclusao de `ADR-0021 §7.3` esta correta.**

> **Isto e mais apto, nao menos.** Um framework que fosse instituido **e exercido em cima de uma
> Spec criada irregularmente** deixaria a arquitetura com um artefato nulo e um precedente ruim.
> Um framework instituido **com a impossibilidade nomeada, medida e com duas saidas de custo
> declarado** deixa a decisao onde ela pertence — e `FND-01 §7.3` diz onde: no Soberano.

## F5 — A mudanca reduz ou aumenta o custo de contexto?

### F5.1 A medicao, itemizada — **a nona da serie**

**Metodo:** contagem de **linhas efetivamente carregadas** por `wc -l` sobre os arquivos, e sobre
os **intervalos** lidos quando a leitura foi parcial (`CE-02`). **Data: 2026-07-29.**

| Item | Linhas |
|---|---|
| `PT-2026-006` — integral *(pre-condicao)* | **452** |
| `ADR-0020` — integral *(forma do instrumento)* | **379** |
| `ADR-0019` — integral *(autoridade da Spec)* | **252** |
| `FND-10` — §2.2–2.6, §4, §5–7, §8, §10.3, §11 e indice | **555** |
| `FND-01` — §6.2 a §11 | **250** |
| `artifact-registry` — §7, §10, §10.5 e indice | **354** |
| `DEP-PRD` — Carta, parcial | **180** |
| `FIT-2026-014` — parcial | **160** |
| `FND-04` — §2 e §6 | **145** |
| `TPL-spec` **1.0.0** — integral | **132** |
| `TPL-rfc` — parcial | **110** |
| `FND-03` — §3.6–3.8 e §7 | **105** |
| `decisions/README` — parcial | **90** |
| `RFC-0016` — parcial | **70** |
| `FND-09` — §8.2 | **50** |
| `rfcs/README`, `governance/README` — parcial | **45** |
| `FND-07` — §2.3 e §2.4 | **20** |
| Cartas de `DEP-EXE`, `DEP-ENG`, `DEP-QAR` — por varredura | **30** |
| **19 `TPL`** — por extracao de frontmatter | **19** |
| Memoria de sessao — indice + 2 registros | **80** |
| Varreduras por ferramenta — contadores, links, tipos, hashes | **100** |
| **Subtotal — acervo** | **3.578** |
| Evidencia externa `A4` — resumo executivo, pacote *Specifications*, 2 fichas | **236** |
| **TOTAL carregado** | **3.814** |

| Metrica | Valor |
|---|---|
| **Acervo no inicio da missao** | **46.353** linhas |
| **Pacote sobre o acervo** *(so acervo)* | **3.578 / 46.353 = 7,72%** |
| **Pacote total, com evidencia externa** | **3.814 / 46.353 = 8,23%** |

### F5.2 Comparabilidade — **declarada, e ela e desfavoravel**

| Missao | Pacote | % do acervo | Natureza da tarefa |
|---|---|---|---|
| 1.12.1 *(FIT-014)* | **2.522** | **5,7%** | **Fechar uma pergunta** — a natureza de dois verbos, em cinco fontes citadas pelo proprio achado |
| **1.13** *(esta)* | **3.578** *(acervo)* | **7,72%** | **Instituir um dominio** — contrato, semantica, perfis, ciclo, rastreabilidade, qualidade, mudanca e economia |

**O pacote cresceu 41,9% em linhas e 2,02 pontos percentuais, e DEP-QAR nao trata isso como
regressao.** A razao esta medida: `RD-22` era **uma** pergunta com **cinco** fontes nomeadas no
proprio achado; esta missao teve de reconstruir **a cadeia de autoridade inteira da Spec** —
`FND-01 §6.2`, `FND-03 §3.6` e `§7`, `FND-04 §2` e `§6`, `FND-07 §2.3`, `FND-09 §8.2`,
`FND-10 §2`, `§4`, `§5`, `§6`, `§7`, `§8`, `§10`, `§11`, tres ADRs e uma Carta — **porque nenhum
lugar a tinha reunida. E era exatamente esse o defeito que a missao corrigiu.**

**A comparacao honesta e prospectiva, e ela e a unica que interessa:** a proxima missao que
precisar da norma da Spec le **`ADR-0021` (`sob-demanda`) + `TPL-spec`** — e, para uma exigencia
pontual, **um bloco de requisito enderecado por `RQ-nn`** (`SF-31`). **O pacote de instituicao e
pago uma vez; o de consumo e pago sempre.**

### F5.3 O que nao foi carregado, e por que isso conta

| Nao carregado | Por que | Economia |
|---|---|---|
| **As 23 Cartas de Capability** | Nenhuma e materia de Spec nesta missao; `VC-01` foi verificado **pela regra**, nao pelo catalogo de Capabilities | **Nao medida — nao carregada** |
| **6 das 9 Cartas de Departamento** | Somente `DEP-PRD`, `DEP-EXE`, `DEP-ENG` e `DEP-QAR` sao alcancadas | ~2.400 linhas nao lidas |
| **As 33.676 linhas do `_SAIDA-COMPANY-OS`** | Consumo **seletivo** determinado pela missao: **236 de 33.676 = 0,70%** | **33.440 linhas nao lidas** |
| **17 dos 19 `TPL`** | Resolvidos por **extracao de frontmatter** — **19 artefatos com 19 linhas de leitura** | Metodo herdado de `FIT-2026-014` |
| **Os 5 relatorios `PT` anteriores** *(exceto trechos)* | `PT-2026-006` era a pre-condicao; os demais entram por remissao | ~1.500 linhas nao lidas |

## F6 — Ela favorece reutilizacao?

**Sim — sete metodos, e o primeiro e o mais forte que esta serie de verificacoes ja registrou.**

| # | Metodo | Reutilizavel? | Evidencia de que funcionou |
|---|---|---|---|
| **1** | **Exercer o instrumento em vez de le-lo.** Pedir o numero da decisao ao contador oficial, em vez de conferir o contador contra a tabela | **Sim, universal** | **Produziu `RD-32`** — 4 contadores defasados em 8 valores, **com risco real de colisao de identificador**. Ler o indice nao revelaria: a tabela estava certa |
| **2** | **Simular o consumo pelo caminho errado, de proposito.** Resolver *"quem libera `QG-1`"* lendo **Cartas** e depois lendo a **fonte**, e comparar | **Sim** | **Produziu `RD-31`** — 8 afirmacoes falsas, **4 nunca enumeradas**, e a constatacao de que **`DEP-EXE` nao declara `QG-1` em nenhuma linha** |
| **3** | **Verificar a pre-condicao de criacao antes de criar.** Rodar o `DoR` contra o artefato que ainda nao existe | **Sim** | **Produziu `RD-33`** — o vinculo `Spec × Produto`, que **nenhuma das 14 missoes anteriores mediu** |
| **4** | **Extrair frontmatter de uma familia inteira e comparar entre iguais** | **Sim** | **Produziu `RD-34`** — **19 de 19** `TPL` com o mesmo valor divergente, o que mostrou que corrigir **um** criaria defeito novo |
| **5** | **Contar os defeitos do achado, em vez de confiar no enunciado dele** | **Sim** | `RD-23` declarava **2** defeitos; a medicao encontrou **5**. Terceira ocorrencia da licao *"o achado registrado pode ser menor que o defeito"* — as anteriores foram `RD-02` e `RD-18` |
| **5b** | **Somar o agregado do indice contra a propria linha dele** — mitigacao `RG-2`, segunda vez exercida | **Sim** | **Produziu `RD-35`** — 3 agregados divergentes: `governance/README` declarava **`19` de `46`** ressalvas quando `28 + 19 = 47`; `memory/README` dava a camada **APR** autoridade **`5`** onde `FND-06 §2` diz **`4`** *(dois cincos tornavam `MM-03` indeterminado)*; e declarava **`3`** registros `OPR` onde ha **`6`** — **tres missoes de atraso** |
| **6** | **Recusar evidencia externa forte com norma citada, em vez de por desconfianca** | **Sim** | `ADR-0021 §8.2`: **duas** praticas de artefatos `LV4` recusadas — assinatura humana por Spec *(contra `PA-13`)* e cadeia de comandos por fase *(contra `FND-10 §4.8`)*. **`0` formatos importados** |
| **7** | Declarar o crescimento do proprio pacote de contexto como **desfavoravel**, com a razao medida | Especifico da serie `F5` | §F5.2 |

## C11 — Conformidade de [FND-10 §11](../../foundation/10-artifact-framework.md)

| # | Verificacao | Resultado |
|---|---|---|
| 1 | Contrato **L1** completo nos artefatos novos | ✅ **5 de 5** declaram os **cinco** campos do contrato estendido |
| 2 | `revisor` ≠ `autor` | ✅ **0 coincidencias** em todo o acervo, remedido apos as edicoes — PT-2026-007 §7 |
| 3 | `ratificacao` coerente com a classe | ✅ `ADR-0021` e **C2 · Tipo 2** → `nao-exigida`. **Nenhum artefato novo e C3 ou Tipo 1.** `TPL-spec` 1.1.0 → `nao-exigida` (`FND-10 §10.3`, linha *Template*: ratifica `—`) |
| 4 | Tipo documental consta de FND-10 §4 | ✅ `RFC` §4.2 · `ADR` §4.2 · `Template` §4.4 · `Fitness Check` §4.5 · `Memoria APR` §4.6 · `Reporte` §4.6. **Nenhum tipo novo** |
| 5 | Atributo **derivavel** declarado em frontmatter | ✅ **0** — nenhum artefato novo declara consumidores, relacoes, autoridade, custo ou dependencia transitiva (`AC-01`). **`SF-06` institui a regra explicitamente para a Spec** |
| 6 | Cadeia **origem → estado → substituicao** percorrivel | ✅ **5 de 5** — `decisoes_relacionadas`, `status` e o par `substitui`/`substituido_por` presentes |
| 7 | Custo de contexto **medido**, nao estimado | ✅ Linhas de cada artefato novo por `wc -l`, registradas no catalogo. **`SF-31` torna a regra obrigatoria para toda Spec futura** |
| 8 | Entrada no catalogo mestre presente | ✅ **5 de 5**, mais `TPL-spec` remedido em §4.4 |
| 9 | Divisao com menos de dois sinais | ✅ **Nenhuma divisao proposta** — e **`SF-19` codifica o limiar de dois sinais** para a Spec |
| 10 | Tabela reproduzida **sem** declaracao de projecao | ✅ **0** — as **duas** matrizes novas declaram `PJ-02` com as quatro informacoes |
| 11 | **Teste preventivo de projecao aplicado, com evidencia** | ✅ **Aplicado, e com efeito**: barrou **tres** reproducoes — F2.b |
| 12 | Conteudo de origem externa fora do portao | ✅ **0 admitidos.** A `A4` foi **lida, citada como `external-evidence` e nao adotada**; **0 formatos importados**, **0 bytes copiados** (`FR-03`) |
| 13 | Alteracao de conteudo **sem** incremento de versao | ✅ **0** — `TPL-spec` declara **1.1.0** com linha de historico, conforme `AC-11`; os indices `M3` sao isentos por `AC-09` |

**13 de 13 conformes.**

---

## Ressalvas

| # | Ressalva | Custo assumido | **Dono** | **Gatilho** |
|---|---|---|---|---|
| **R1** | **O framework inteiro e determinado e nao observado.** **Nao existe nenhuma `Spec`**, e por isso **nenhuma** das 32 regras tem membro observado. `T-01` a `T-12` de `ADR-0021 §9` resolvem por regra citada, **nao por caso ocorrido**; `A1`, `A2` e `A3` declaram isso | Um dominio normativo completo **sem um unico exercicio real**. `PI-10` exige que esteja escrito, e esta — **em `A1`, em `RA-2` e aqui** | **DEP-PRD** | **A primeira `Spec` real** — que depende de `S1` ou `S2`, ambas do SOBERANO |
| **R2** | **`SF-09` institui 21 blocos obrigatorios sem que o custo tenha sido medido.** O risco `RA-6` e real: 21 blocos podem tornar a Spec caro de escrever, contra `PI-14`. **A mitigacao de `SF-31` — blocos independentes e perfil `sob-demanda` — e projetada, nao verificada** | Uma exigencia de forma cujo custo **sera conhecido depois** de institui-la. `CE-04` proibe estimar, e por isso **nenhum numero foi estimado** | **DEP-PRD** | **A primeira `Spec` medida contra o dobro da mediana do tipo** (`CE-05`) |
| **R3** | **`RD-31` deixa o portao da Spec sem titular declarado em Carta alguma.** `DEP-PRD` reivindica `QG-1` em **8** afirmacoes; `DEP-EXE` **nao o declara em nenhuma** *(0 ocorrencias, medido)*. Um consumidor que resolva pelas Cartas obtem **`DEP-PRD`** — e `FND-01 §6.2` diz **`DEP-EXE`**. **Corrigir exige emendar Carta ratificada: ato do SOBERANO** | O acervo passa a ter **divergencia conhecida entre fonte fundacional e Carta vigente**, sobre o portao do proprio artefato que a missao normatizou. **Atenuante real, e nao e cumprimento:** `LV-03` continua valendo — liberacao por quem produziu e **nula**, independentemente do que a Carta diga | **DEP-EXE** *(propoe emenda de Carta — `FND-09 §8.2`, linha `DEP`)*; revisa **DEP-GOV** | **Antes da primeira Spec**, ou o proximo ato soberano que alcance `DEP-PRD` ou `DEP-EXE` |

### Ressalvas anteriores — situacao

| Ressalva | Origem | Situacao |
|---|---|---|
| **`R1` de FIT-2026-014** *(`PA-07` supletiva sem membro observado)* | FIT-2026-014 | **Aberta, inalterada.** Esta missao **nao invocou `PA-07`**: `ADR-0021` nomeia executor em `SF-32` e no §5.3 |
| **`R2` de FIT-2026-014** *(`RD-27` — `FND-01` e `FND-02` nao conformes)* | FIT-2026-014 | **Aberta, inalterada e deliberadamente nao tocada** — pre-correcao `RD-27` da missao. **`0` bytes alterados em `FND-01`, `FND-02` e `FND-10`**, verificado por `cmp` |
| **`RD-23`** *(pre-correcao obrigatoria)* | FIT-2026-014 | ✅ **FECHADA.** `TPL-spec` **1.1.0**, **5** defeitos corrigidos onde o achado declarava **2** — `ADR-0021 §5.11`, com diff literal reversivel em §5.12 |
| Familia **`RC-02`** | REV-ESTRUTURAL-I | **DECLARADA, NAO RESOLVIDA — setima ocorrencia, e a mais mitigada de todas.** **DEP-GOV nao e autor de nenhum instrumento normativo desta missao** — primeira vez em quinze. Residuo: DEP-GOV **registra** o catalogo que declara defeito em contador de DEP-GOV (`RD-32`). So desaparece com agentes (`IC-3`) |
| `RD-10` *(rota `PRD → TLS`)* · `RD-13` *(historico de `FND-10`)* | RFC-0015 · PS-2026-008 | **Abertas, nao alcancadas.** Materia de Carta e de fonte ratificada |

---

## Veredito

> ## **`apto-com-ressalva`**
>
> **A arquitetura ficou mais apta a evoluir, e por um caminho que esta serie nao havia visto
> antes.** As tres decisoes anteriores sobre `Spec` custaram **duas emendas constitucionais e
> dois atos soberanos**. Esta institui **o contrato inteiro do tipo** com **`0` fontes emendadas,
> `0` atos consumidos, `0` entidades, `0` tipos documentais, `0` portoes e `0` titulares novos** —
> e **fecha a pre-correcao que bloqueava a primeira Spec**.
>
> **Tres ressalvas, todas com dono e gatilho, e a mais grave nao e do framework.** `R1` e `R2`
> sao o preco de normatizar antes de exercer, e o registro as declara em vez de as esconder.
> **`R3` e de outra natureza: e uma divergencia real, vigente, entre fonte fundacional e Carta
> ratificada, sobre o portao da propria Spec** — e ela **existia antes desta missao** e so
> apareceu porque o framework foi **exercido** em `T-12`.
>
> **O que este parecer NAO afirma.** Nao julga a **classe `C2`** — e de DEP-EXE, e `ADR-0021 §11`
> declara a duvida com os dois argumentos de cada lado. Nao escolhe entre **`S1`** e **`S2`** — e
> do SOBERANO (`FND-01 §7.3`). Nao afirma que as 32 regras funcionam — **`R1` diz o contrario:
> nenhuma foi exercida**. E nao converte parecer em norma: `FT-10` e `FT-11` o proibem.
>
> **O que este parecer afirma, e verificou de forma independente:** as **tres** fontes do
> bloqueio existem e dizem o que `ADR-0021 §7.3` afirma; **`0`** Specs e **`0`** produtos
> existem; `products/` **esta ausente**; os **5** defeitos de `RD-23` **estao corrigidos**; as
> **50** celulas de §5.3 **nao ampliam titular**; e **`C11` fecha 13 de 13**.

## Fechamento — **`ADJUST`**

**DEP-QAR nao recomenda `GO-TO-SKILLS`, e a razao nao e a qualidade do framework.**

| Opcao de fechamento | Avaliacao independente |
|---|---|
| **`GO-TO-SKILLS`** | ❌ **Prematura.** O portao anterior — `GO-TO-SPECS` — **foi liberado e nao pode ser exercido**: `0` Specs sao criaveis. Avancar para o Framework de Skills deixaria **dois** portoes abertos e **nenhum** exercido, e `SF-*` continuaria determinado e nao observado por mais um ciclo |
| **`READY-FOR-RATIFICATION`** | ❌ **Nao aplicavel.** `ADR-0021` e **C2 · Tipo 2**: `FND-04 §2.1` **nao exige ratificacao**, e pedi-la seria criar exigencia que a norma nao faz. **O que aguarda o Soberano nao e a ratificacao deste ADR — sao `S1` e `S2`** |
| **`STOP`** | ❌ **Desproporcional.** Oito dos nove entregaveis estao completos e verificados; a pre-correcao obrigatoria **foi fechada**; nenhuma norma foi violada; nenhum artefato e nulo |
| **`BLOCKED`** | ❌ **Incorreta.** `BLOCKED` cabe quando a **pre-condicao** falha, e ela **nao falhou**: `GO-TO-SPECS` estava liberado, `ADR-0020` vigente, prova 55/55, catalogo reconciliado e `BL-08` reproduzida. **O bloqueio e do entregavel 9, nao da missao** |
| **`ADJUST`** | ✅ **Correta.** **Oito entregaveis completos; um parcialmente entregue** *(template e registro sim, pilotos nao)*; **o motivo e normativo, medido e com duas saidas de custo declarado**; **quatro achados novos** com dono e gatilho; **tres ressalvas**. O ajuste devido **nao e desta missao: e um ato** |

### A decisao

> ## **`ADJUST`**
>
> **O Framework de Specifications esta instituido, testado e verificado. Os dois pilotos nao
> existem, e a razao esta escrita com tres fontes citadas por identificador.**
>
> **O ajuste devido e uma escolha do SOBERANO entre duas saidas disjuntas** — `S1`, ato que crie
> o primeiro Produto; `S2`, `RFC C3 → ADR C3 → ato` que amplie a Spec a materia nao-produto —,
> **e cada piloto pedido depende de uma delas**. Nenhum Departamento pode suprir a escolha, e
> tentar supri-la seria `LV-06` ou `LV-07`.
>
> **Nenhuma Spec deve ser criada antes dessa escolha.** Criar uma agora produziria artefato
> **nulo** (`MT-01`, `AC-06`) e incidente de conformidade (`LV-11`).

## Pendencias para o SOBERANO — **cinco**

| # | Materia | Natureza | Bloqueia trabalho? |
|---|---|---|---|
| 1 | **`S1` ou `S2`** — qual via desbloqueia a Spec | **C2 · Tipo 1** *(criar Produto)* **ou** **C3** *(ampliar Spec)*. `FND-01 §7.3` | ✅ **Sim — bloqueia a primeira Spec e os dois pilotos** |
| 2 | **`RD-31`** — emenda a Carta de `DEP-PRD` *(8 afirmacoes)* e a de `DEP-EXE` *(declarar `QG-1`)* | **RFC + ADR + diff + pacote + ato.** `FND-09 §8.2`, linha `DEP` | ⚠️ **Recomendado antes da primeira Spec** — `R3` |
| 3 | **`RD-27`** — backfill em `FND-01`, `FND-02` e `FND-10 §8.5`, que **altera `H-N`** | Idem. **Inalterada desde FIT-2026-014** | ❌ Nao |
| 4 | **A classe de `ADR-0021`** — se declarar o contrato de um tipo e **C3** | Basta a manifestacao; `RFC-0017` serve de peca instrutoria **sem reescrita** | ❌ Nao |
| 5 | **A classe de `ADR-0020`** | **Inalterada desde FIT-2026-014** | ❌ Nao |

**Duas das cinco sao novas, e uma delas bloqueia — pela primeira vez em duas missoes.**
`FIT-2026-014` registrou tres pendencias e **nenhuma bloqueava**. Esta registra cinco, e **`1`
bloqueia**: nao por regressao, mas porque **o trabalho chegou ao ponto em que a norma exige uma
decisao de portfolio**, e portfolio e materia exclusiva do Soberano.

## Aprendizado gerado

| # | Licao | Registro |
|---|---|---|
| 1 | **Exercer o instrumento revela o defeito que ler o instrumento nao revela.** Pedir o numero achou o contador defasado; simular o consumo achou a Carta falsa; rodar o `DoR` achou o vinculo `Spec × Produto` | [MEM-APR-0006](../../memory/aprendizado/MEM-APR-0006-exercer-o-contador-revela-o-defeito.md) |
| 2 | **Corrigir o valor nao corrige a causa.** `governance/README` documenta a correcao de um contador defasado em 2026-07-28 e **o mesmo defeito reapareceu em quatro contadores** — porque a correcao atingiu o valor, nao o gatilho `CV-04` | `MEM-APR-0006`; `SF-32` codifica o gatilho |
| 3 | **O achado registrado pode ser menor que o defeito — terceira ocorrencia.** `RD-23` declarava 2 defeitos e tinha 5. As anteriores foram `RD-02` e `RD-18` | `ADR-0021 §5.11`; dono **DEP-GOV**, gatilho **proxima auditoria de achado** |
| 4 | **Avaliar evidencia externa produz resultado util quando ela e recusada com norma citada** — duas praticas `LV4` recusadas, `0` formatos importados | `ADR-0021 §8.2`; candidato a `MEM-APR` proprio na proxima missao que reutilize o metodo |

## Historico de vereditos sobre este objeto

**Primeiro parecer** sobre o Framework de Specifications. **Nao supera nem contesta
`FIT-2026-014`**, cujo objeto era outro; **consome** dele a apuracao de `GO-TO-SPECS` e a
pre-correcao `RD-23`, e **registra que `RD-23` esta fechada**.

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-QAR | Verificacao de aptidao do **Framework de Specifications**. Veredito **`apto-com-ressalva`**, com **tres** ressalvas novas — **`R1`** *(as 32 regras sao determinadas e nao observadas: nao existe nenhuma `Spec`)*, **`R2`** *(`SF-09` institui 21 blocos obrigatorios sem custo medido; `CE-04` proibiu estimar, e nada foi estimado)* e **`R3`** *(`RD-31` deixa o portao da Spec sem titular declarado em Carta alguma — `DEP-PRD` o reivindica em 8 afirmacoes, `DEP-EXE` em 0)*. **F1:** 32 regras e 2 matrizes contra **4 achados em 4 missoes** e **0** fontes emendadas; o consumidor sai de **5 fontes em 6 secoes** para **1 ADR + 1 template**. **F2:** nenhuma duplicacao, e a prevencao de `PJ-05` **barrou tres reproducoes** — decima quarta confirmacao de `MEM-APR-0002`. **F3:** **quatro** abstracoes evitadas — `FND-11`, tipo documental por perfil, `conflita` como aresta e registro mestre proprio. **F4:** a Spec ganhou contrato **sem custo normativo**, e **a impossibilidade de exerce-lo ficou escrita em vez de contornada** — as duas saidas faceis eram violacao, e as duas estao nomeadas. **F5:** nona medicao da serie — **3.578 linhas de acervo · 7,72%**, **+41,9%** sobre a Missao 1.12.1, com a comparabilidade declarada **como desfavoravel** e a razao medida: nenhum lugar reunia a cadeia de autoridade da Spec, **e era esse o defeito corrigido**. Consumo seletivo da `A4`: **236 de 33.676 linhas = 0,70%**. **F6:** **7 metodos reutilizaveis**, e o mais forte foi **exercer o instrumento em vez de le-lo** — produziu `RD-32` ao pedir o numero da decisao. **`C11`: 13 de 13 conformes.** **`RD-23` FECHADA** — 5 defeitos corrigidos onde o achado declarava 2. Fechamento **`ADJUST`**, com as outras quatro opcoes recusadas uma a uma e com fundamento. **Cinco pendencias para o SOBERANO, e uma bloqueia** — a escolha entre `S1` e `S2` —, **pela primeira vez em duas missoes**; o bloqueio nao e regressao, e o sinal de que o trabalho chegou a uma decisao de portfolio, materia exclusiva do Soberano. **DEP-GOV nao e autor de nenhum instrumento normativo desta missao: primeira vez em quinze, e a resposta material a `RC-02`.** |
