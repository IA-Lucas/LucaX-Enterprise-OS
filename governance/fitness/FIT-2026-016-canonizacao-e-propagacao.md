---
id: FIT-2026-016
titulo: Verificacao de aptidao — canonizacao do Framework de Specifications e propagacao de QG-1 nas Cartas
tipo: fitness-check
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: DEP-QAR
proprietario: DEP-QAR
aprovador: DEP-EXE
criado_em: 2026-07-29
atualizado_em: 2026-07-29
revisao_prevista: null
decisoes_relacionadas: [ADR-0004, ADR-0012, ADR-0015, ADR-0021, ADR-0022, ADR-0023]
substitui: []
substituido_por: null
veredito: apto-com-ressalva
resumo: Verifica a aptidao evolutiva dos dois ritos da Missao 1.13.1 e conclui apto-com-ressalva, com quatro ressalvas novas e C11 conforme em 13 de 13.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-GOV
ratificacao: nao-exigida
---

# FIT-2026-016 — Canonizacao e propagacao

> **Este parecer nao ratifica, nao aprova objeto e nao da vigencia a nada** — `FT-10` a `FT-15`
> de [ADR-0015](../../decisions/ADR-0015-fitness-check-e-parecer-nao-decisao.md). Ele julga
> **aptidao evolutiva** (`QG-6`).

## Proposito

Responder as **seis** perguntas de aptidao de [FND-09 §10](../../foundation/09-meta-model.md)
sobre a Missao 1.13.1, e a conformidade **`C11`** de
[FND-10 §11](../../foundation/10-artifact-framework.md).

## Escopo

| Item | Definicao |
|---|---|
| **Objeto avaliado** | `RFC-0018`, `ADR-0022`, `PS-2026-009`, `RFC-0019`, `ADR-0023`, `PS-2026-010`, `PT-2026-008`, os **seis** candidatos e a cascata em **8** indices `M3` |
| **Nao** avaliado | O **merito** de `ADR-0018`, `ADR-0019` e `ADR-0021`, **nao reabertos** · a **aplicacao**, que **nao ocorreu** · `RD-27`, `RD-33`, `RD-36` |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| Executa | **DEP-QAR** | `FND-09 §8.2`, linha `FIT`; `CV-07` |
| Revisa forma | **DEP-GOV** | `FND-09 §8.2` |
| Aprova | **DEP-EXE** | `FND-09 §8.2`, linha `FIT` |

> **`I-2` de `DEP-EXE` foi testado e nao se aplica.** `DEP-EXE` **e autor de `ADR-0023`** e nao
> pode aprovar `FIT` sobre objeto que produziu. **Mas `DEP-EXE` nao produziu o objeto integral
> deste parecer** — `ADR-0022`, `PS-2026-009` e `PT-2026-008` sao de `DEP-GOV`. **A avaliacao
> registra o impedimento parcial e o resolve por recorte:** `DEP-EXE` aprova o parecer **exceto
> quanto a `ADR-0023`, `PS-2026-010` e os dois candidatos de Carta**, cuja aprovacao cabe a
> **`DEP-GOV`** — precedente **`FIT-2026-003`**. Ressalva **`R4`**.

## Sumario

| Campo | Conteudo |
|---|---|
| **Veredito** | **`apto-com-ressalva`** |
| Ressalvas novas | **4** — `R1` a `R4` |
| Ressalvas anteriores | **`R1`, `R2` de FIT-2026-015 MANTIDAS** · **`R3` MIGRADA** para instrumento vivo |
| `C11` | **13 de 13 conformes** |
| Achados produzidos | **8** — `RD-37` a `RD-44` |
| Objetos que entraram em vigor | **`0`** |

---

## F1 — A complexidade aumentou sem ganho proporcional?

### F1.1 O acrescimo, medido

| Item | Valor |
|---|---|
| Artefatos novos no acervo | **8** |
| Linhas novas no acervo | **2.934** |
| Candidatos **fora** do acervo | **6**, **2.963** linhas — **nao pesam no contexto** (`CE-02`) |
| Fontes normativas alteradas **no acervo** | **`0`** |
| Regras normativas criadas | **`0`** — as **32** sao **recebidas**, nao escritas |
| Titulares · portoes · papeis · classes · verbos · entidades · tipos | **`0` criados** |

### F1.2 O ganho, medido

| Ganho | Antes | Depois do ato | Como se mede |
|---|---|---|---|
| **Sede da norma da `Spec`** | `decisions/`, artefato **`M1`** que *"nunca se emenda"* | `foundation/`, artefato **`M2`** emendavel por rito | `FND-10 §4.1`, linha *Framework* |
| **Custo de consumo da norma** | **573** linhas *(`ADR-0021` integral)* | **399** linhas *(`FND-11`)* — **−30%** | `wc -l` |
| **Resposta a *"quem libera `QG-1`?"* pelas Cartas** | **`DEP-PRD`** — errada | **`DEP-EXE`** — igual a fonte | `T-12` de ADR-0021 §9, reexecutado |
| **Cartas com titular do portao declarado** | **0 de 9** | **2 de 9** | `grep` |
| **Afirmacoes falsas sobre `QG-1` no acervo** | **11**, em **4** Cartas | **3**, em **3** | `grep` nas nove Cartas |

**Veredito de F1: o acrescimento e proporcional, e a razao e que quase nada foi inventado.**
**`0`** regras normativas novas, **`0`** titulares, **`0`** fontes alteradas no acervo. O que
cresceu foi **instrumento de decisao** — RFC, ADR, pacote —, que e **`sob-demanda`** e existe para
ser lido **uma vez**, no ato.

## F2 — Algum conceito foi duplicado? E a prevencao foi aplicada?

### a) Houve duplicacao?

| Candidato a duplicacao | Veredito |
|---|---|
| **`FND-11` × `ADR-0021`** | **Duplicacao TEMPORARIA e declarada.** Enquanto o ato nao vier, **so `ADR-0021` vigora** e `FND-11` **nao existe no acervo**. Depois do ato, as 32 regras vivem **nos dois textos** — e e por isso que **`RD-40`** foi aberto, e nao ignorado. **A hierarquia resolve:** `FND-11` e nivel 2; `ADR-0021` e nivel 3 |
| **`FND-11 §4` e `§5` × `FND-03`, `FND-04`, `FND-09`, `FND-10`** | **Projecao declarada, nao duplicacao.** As duas carregam `PJ-02` com as **quatro** informacoes, e `PJ-03` da precedencia a fonte |
| **`DEP-EXE §5` × `FND-01 §6.2`** | **Projecao de Carta, ja prevista** — `DC-08`. A linha **cita a fonte** |
| **`DEP-PRD §5.1` × `§4`** | **Espelho intencional, e ja existente na Carta 1.0.0** — quatro materias ja apareciam nas duas secoes |
| **`PT-2026-008` × os dois pacotes** | **Remissao, nao reproducao:** o relatorio **nao reproduz** diff nem hash de candidato; remete |

### b) A prevencao de `PJ-05` foi aplicada, com evidencia?

**Sim, e barrou quatro reproducoes:**

| # | O que seria reproduzido | Onde | Como foi resolvido |
|---|---|---|---|
| 1 | Os **criterios `K1`–`K8`** | `ADR-0022 §3` | **Remissao** a `RFC-0018 §3` (`PJ-01`) |
| 2 | As **quatro opcoes e a opcao Z** | `ADR-0022 §4` | **Remissao** a `RFC-0018 §4` |
| 3 | A **tabela regra por regra** das 32 | `ADR-0022 §5.2` | **Remissao** a `FND-11 §2.2`; o ADR publica **so a medicao do `diff`** |
| 4 | A tabela de **7 controles de hash** | `PS-2026-010 §4.3` | **Remissao** a `PS-2026-009 §4.3` |

**Decima quinta confirmacao de
[MEM-APR-0002](../../memory/aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md).**

## F3 — Alguma abstracao ficou desnecessaria?

| Abstracao **evitada** | Por que nao foi criada |
|---|---|
| **Tipo documental novo para "Framework de dominio"** | `FND-10 §4.1` **ja tem** *Framework*. Criar seria `C3 · Tipo 1` com sete testes `TE` |
| **Nota interpretativa em `governance/`** para as Cartas | Seria **terceira fonte** para *"quem libera `QG-1`"* — Opcao `D` de `RFC-0019`, recusada |
| **Campo novo de frontmatter** para sucessao parcial | `RD-43` mostrou que o campo existente **altera `H-N`**; criar outro seria resolver por abstracao um defeito de **lista fechada** — `IR-04` manda `C2` com ADR |
| **Registro proprio de `Spec`** | `SF-32` **ja proibia**; `FND-11` conserva |
| **Nivel novo na hierarquia normativa** | `FND-01 §10` **ja resolve** conflito no nivel 2. **8 niveis antes, 8 depois** |

**Cinco abstracoes evitadas, todas com a regra que as dispensa citada.**

## F4 — O sistema continua mais simples de evoluir?

| Dimensao | Efeito |
|---|---|
| **Corrigir uma regra `SF-*`** | **Fica mais caro, e isso e a feicao** — passa de *1 ADR `C2`* a *1 emenda + 1 ato*. **Declarado nos tres instrumentos, no sentido correto** |
| **Encontrar a norma da `Spec`** | **Fica mais simples** — vive em `foundation/`, onde o acervo aloja norma de dominio |
| **Responder *"quem libera `QG-1`?"*** | **Fica deterministico pelos dois caminhos** |
| **Emendar a Carta de `DEP-PRD`** | **Igual** — continua exigindo ato |
| **Superar um `ADR`** | **Fica mais bem compreendido, e nao mais simples:** `RD-43` mediu que o unico campo de sucessao de `ADR` **altera `H-N`**. **O acervo ganhou a informacao, nao a solucao** |

**Veredito de F4: apto.** A unica dimensao que piorou **piorou de proposito**, e a piora esta
escrita em `RFC-0018 §5`, `ADR-0022 §4`, `PS-2026-009 §2.4` e `PT-2026-008 §2.2` — **quatro
lugares, com o sentido do tradeoff invertido em relacao ao intuitivo**.

## F5 — A mudanca reduz ou aumenta o custo de contexto?

### F5.1 A medicao, itemizada — **a decima da serie**

| Artefato | Perfil | Linhas |
|---|---|---|
| `RFC-0018` | `sob-demanda` | **262** |
| `ADR-0022` | `sob-demanda` | **438** |
| `RFC-0019` | `sob-demanda` | **268** |
| `ADR-0023` | `sob-demanda` | **353** |
| `PS-2026-009` | `missao` | **446** |
| `PS-2026-010` | `missao` | **394** |
| `PT-2026-008` | `missao` | **334** |
| `FIT-2026-016` *(este)* | `missao` | **294** |
| **Subtotal** | | **2.789** |
| Delta nos indices `M3` | — | **+145** |
| **Total** | | **2.934** — **6,02%** do acervo |

### F5.2 Comparabilidade — **declarada, e ela e favoravel**

| Missao | Linhas de acervo | Objeto |
|---|---|---|
| 1.12.1 | **2.522** | Aplicacao do sexto ato |
| 1.13 | **3.578** | **Instituir** um dominio — 32 regras escritas do zero |
| **1.13.1** | **2.934** | **Mover** um dominio + propagar duas Cartas |

**A comparacao com a 1.13 e favoravel e a razao e estrutural: nao se escreveu norma.** As 32
regras foram **extraidas e transformadas por ferramenta**. O que se escreveu foi **prova de
equivalencia** — e prova custa menos que norma.

### F5.3 O que **nao** foi carregado, e por que isso conta

**`0` linhas de `_SAIDA-COMPANY-OS/`** *(33.676 linhas disponiveis)*. A missao **vedou** integrar
o SSC+, e a vedacao foi cumprida **na leitura, nao apenas na escrita** — o pacote externo **nao
foi aberto**.

## F6 — Ela favorece reutilizacao?

| # | Metodo reutilizavel | Onde nasceu |
|---|---|---|
| **1** | **Provar equivalencia de migracao por `diff` do bloco extraido**, em vez de reler o texto migrado | `ADR-0022 §5.2` |
| **2** | **Montar candidato por patch programatico com assercao de unicidade** — a substituicao falha se o trecho nao existir **ou** aparecer duas vezes | `PS-2026-010 §4.4` |
| **3** | **Medir a alternativa antes de discuti-la** — foi assim que `RD-43` apareceu | `PS-2026-009 §3.1` |
| **4** | **Submeter duas variantes com hash quando duas normas colidem**, em vez de escolher em silencio | `PS-2026-009 §5` |
| **5** | **Medir a familia inteira, nao os dois membros citados no achado** — foi assim que `RD-37` apareceu | `RFC-0019 §3` |
| **6** | **Verificar independencia de objetos por prova textual** *(`grep` cruzado entre candidatos)* | `PS-2026-009 §6` |
| **7** | **Remedir os recortes de carregamento da Carta apos edita-la** | `ADR-0023 §5.1 P16` |

**O mais forte e o `3`.** `RD-43` **nao era encontravel por leitura**: `FND-10 §6.2` autoriza
mudar *"os campos de sucessao"* em `M1`, e **so o hash revelou** que `IR-03` nao exclui
`superado_por` — logo, para `ADR`, **a autorizacao nao tem objeto praticavel**.

## C11 — Conformidade de [FND-10 §11](../../foundation/10-artifact-framework.md)

| # | Verificacao | Resultado |
|---|---|---|
| 1 | Contrato **L1** completo nos artefatos novos | ✅ **8 de 8** declaram os **cinco** campos do contrato estendido |
| 2 | `revisor` ≠ `autor` | ✅ **8 de 8** — e **`0` coincidencias** no acervo, remedido apos as edicoes |
| 3 | `ratificacao` coerente com a classe | ✅ `ADR-0022` e **C3 · Tipo 1** → **`pendente`**; `ADR-0023` e `C2 · Tipo 2` → `nao-exigida`; `FND-11` candidato → **`pendente`**; os dois candidatos de Carta → **`pendente`**. **Nenhum objeto `C3`/`Tipo 1` declara `nao-exigida`** |
| 4 | Tipo documental consta de FND-10 §4 | ✅ `RFC` §4.2 · `ADR` §4.2 · **`Framework` §4.1** · `Carta de Departamento` §4.3 · `Fitness Check` §4.5 · `Reporte` §4.6. **Nenhum tipo novo** |
| 5 | Atributo **derivavel** declarado em frontmatter | ✅ **`0`** — nenhum artefato novo declara consumidores, relacoes, autoridade, custo ou dependencia transitiva (`AC-01`) |
| 6 | Cadeia **origem → estado → substituicao** percorrivel | ✅ **8 de 8.** `ADR-0022` declara **`supera: [ADR-0021]`**, e a **sucessao parcial** esta legivel em **4** lugares — a insuficiencia do lado de `ADR-0021` esta declarada como **`RD-40`** |
| 7 | Custo de contexto **medido**, nao estimado | ✅ Todas as linhas por `wc -l`. **Uma unica estimativa aparece no acervo, e esta rotulada como estimativa** — o custo de estender `RD-37`, em `PS-2026-010 §9.1` |
| 8 | Entrada no catalogo mestre presente | ✅ **8 de 8** |
| 9 | Divisao com menos de dois sinais | ✅ **Nenhuma divisao proposta** |
| 10 | Tabela reproduzida **sem** declaracao de projecao | ✅ **`0`.** As **duas** projecoes de `FND-11` carregam `PJ-02` com as quatro informacoes, e **`RB-4` de `ADR-0022` declara e resolve a tensao com `CC-05`**, com **2 precedentes medidos em `FND-10`** |
| 11 | **Teste preventivo de projecao aplicado, com evidencia** | ✅ **Aplicado, e com efeito: barrou 4 reproducoes** — F2.b |
| 12 | Conteudo de origem externa fora do portao | ✅ **`0` admitidos.** **`0` linhas externas lidas** — F5.3 |
| 13 | Alteracao de conteudo **sem** incremento de versao | ✅ **`0`.** Os candidatos declaram **1.6.0**, **1.6.0**, **1.0.0**, **1.1.0** e **1.1.0**, cada um com linha de historico (`AC-11`); os indices `M3` sao isentos por `AC-09` |

**13 de 13 conformes.**

---

## Ressalvas

| # | Ressalva | Consequencia se nao tratada | Dono | Gatilho |
|---|---|---|---|---|
| **`R1`** | **A duplicacao temporaria da norma e real, e sobrevive ao ato.** Depois de aplicado, as 32 regras vivem em **dois textos**, e `ADR-0021` **nao dira** que foi superado. Em **31 de 32** o merito e identico; **em `SF-32` a leitura de `ADR-0021` sera errada** | Um consumidor que leia `ADR-0021` concluira que a norma **nao se emenda**, quando ela passou a emendar-se com ato | **DEP-GOV** | **`RD-40`** — primeira emenda a `FND-11` |
| **`R2`** | **`RD-37` deixa 3 Cartas ratificadas afirmando que `DEP-PRD` libera `QG-1`.** A missao corrigiu **2 de 4** Cartas por escopo determinado | O acervo passa de *"titular errado em 4 Cartas"* a *"titular errado em 3"* — melhora medida, **nao fechamento** | **DEP-EXE** *(propoe)*; revisa **DEP-GOV** | **Proximo ato que alcance `DEP-OPS`, `DEP-GRW` ou `DEP-TLS`** |
| **`R3`** | **`FND-01` sera emendada sem os quatro campos de `AC-08` se `V1` for escolhido** — terceira ocorrencia de `RD-27`, e **a primeira em que o ato que a repete tinha como nao repetir**, porque **`V2` existe e esta medido** | `AC-06` segue descumprido por um documento de **nivel 1** da hierarquia normativa | **DEP-GOV** | **O proprio ato** — `Q2` de `PS-2026-009` |
| **`R4`** | **A aprovacao deste parecer e parcialmente impedida.** `DEP-EXE` e **autor de `ADR-0023`** e do candidato `DEP-EXE` 1.1.0, e `I-2` veda aprovar `FIT` sobre objeto proprio. **O recorte resolve, e nao elimina:** parte do objeto avaliado e de quem aprova | Aprovacao **nula** na parte impedida (`LV-03`), se o recorte nao for observado | **DEP-GOV** *(aprova a parte impedida)* | **Este parecer** |

### Ressalvas anteriores — situacao

| Ressalva | Situacao | Justificativa |
|---|---|---|
| **`R1` de `FIT-2026-015`** *(as 32 regras sao determinadas, nao observadas)* | **MANTIDA** | **`0` Specs existem.** Mover a sede **nao produz instancia** — e `FND-11 §14 L1` o declara |
| **`R2` de `FIT-2026-015`** *(21 blocos sem custo medido)* | **MANTIDA** | `CE-04` proibiu estimar, e **nada foi estimado**. O valor sera medido na **primeira `Spec`** |
| **`R3` de `FIT-2026-015`** *(`RD-31` — o portao sem titular em Carta alguma)* | **MIGRADA para instrumento vivo** | Sai de *"ressalva sem instrumento"* e passa a *"tratada pelo rito `C2` completo — RFC, ADR, 2 candidatos, diff literal, hashes, `IR-09`, pacote"*. **Tratada, nao eliminada:** so fecha com ato |

## Veredito

| Campo | Conteudo |
|---|---|
| **Veredito** | **`apto-com-ressalva`** |
| **Por que nao `apto`** | **Quatro ressalvas com consequencia verificavel**, e duas delas *(`R1`, `R3`)* **sobrevivem ao ato** |
| **Por que nao `inapto`** | Nada no objeto avaliado **aumenta o custo de evoluir sem ganho declarado**; a unica dimensao que encarece **encarece de proposito, em quatro lugares**; `C11` e **13 de 13**; e **`0` fontes normativas do acervo foram alteradas** |
| **Efeito processual** | `apto-com-ressalva` **nao bloqueia** o encerramento (`FT-14`). As **4** ressalvas seguem com dono e gatilho |

## Fechamento

| Opcao | Recusada por que |
|---|---|
| **`GO-TO-SKILLS`** | A missao **nao autorizou** `Skill`, e o portao seguinte depende de objetos que **nao vigoram** |
| **`ADJUST`** | **Nada ficou por ajustar dentro do escopo:** dois ritos completos, seis candidatos medidos, sete achados com dono e gatilho, duas colisoes de norma **declaradas com escolha submetida**, `C11` **13 de 13** |
| **`BLOCKED`** | **Nada nesta missao ficou impedido.** `RD-33` bloqueia a **`Spec`**, e o bloqueio esta formalizado como **`PILOTO-DEFERIDO`** |
| **`READY-FOR-RATIFICATION`** | ✅ **A decisao.** Os instrumentos estao prontos, medidos e verificaveis; **a proxima acao e do Fundador** |

## Pendencias para o SOBERANO — **sete**

**Enumeradas em [PT-2026-008 §10.2](../relatorio-transicao-2026-07-29-canonizacao.md), e uma
bloqueia a `Spec`:** a escolha entre **`S1`** e **`S2`**.

## Aprendizado gerado

| # | Licao | Evidencia |
|---|---|---|
| **1** | **Migracao de norma se prova por `diff` do bloco extraido, nao por releitura** | `14` blocos, **`0`** em 30 regras |
| **2** | **Medir a alternativa antes de discuti-la** — a leitura autorizava o que o hash proibiu | **`RD-43`** |
| **3** | **Medir a familia inteira, nao os membros citados no achado** | **`RD-37`** — o defeito estava em 4 Cartas, e o achado citava 2 |
| **5** | **Conferir o indice ao lado do contador, e nao apenas o contador** | **`RD-44`** — `SF-32` codificou o contador, e o defeito migrou para a tabela do mesmo arquivo |
| **4** | **Quando duas normas colidem, submeter duas variantes com hash e mais honesto que escolher** | `PS-2026-009 §5` |

> **Promocao a `MEM-APR` nao e pedida nesta missao.** As licoes **1**, **3** e **4** sao novas com
> **uma** ocorrencia; a licao **2** e a **segunda ocorrencia** da familia de
> [MEM-APR-0006](../../memory/aprendizado/MEM-APR-0006-exercer-o-contador-revela-o-defeito.md) — e
> por isso **reforca** o registro existente em vez de criar outro (`FND-04 §6.1`, nao-proliferacao).

## Historico de vereditos sobre este objeto

| Data | Veredito | Objeto |
|---|---|---|
| 2026-07-29 | `apto-com-ressalva` | Missao 1.13 — instituicao do Framework *(FIT-2026-015)* |
| **2026-07-29** | **`apto-com-ressalva`** | **Missao 1.13.1 — canonizacao e propagacao** *(este)* |

---

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-QAR | Verificacao de aptidao dos **dois ritos** da Missao 1.13.1. Veredito **`apto-com-ressalva`**, com **quatro** ressalvas novas — **`R1`** *(a duplicacao da norma sobrevive ao ato, e `ADR-0021` nao dira que foi superado; em `SF-32` a leitura sera errada)*, **`R2`** *(`RD-37` deixa 3 Cartas ratificadas afirmando titular errado de `QG-1`; a missao corrigiu 2 de 4)*, **`R3`** *(`FND-01` sera emendada sem os quatro campos de `AC-08` se `V1` for escolhido — e **e a primeira vez que o ato que repete `RD-27` tinha como nao repetir**)* e **`R4`** *(a aprovacao deste parecer e parcialmente impedida, porque `DEP-EXE` e autor de parte do objeto avaliado; resolvido por recorte, com `DEP-GOV` aprovando a parte impedida — precedente `FIT-2026-003`)*. **`F1`:** **`0`** regras normativas criadas, **`0`** titulares, **`0`** fontes do acervo alteradas — o que cresceu foi **instrumento de decisao**, e o consumidor da norma passa de **573** para **399** linhas *(−30%)*. **`F2`:** nenhuma duplicacao nao declarada, e a prevencao de `PJ-05` **barrou quatro reproducoes** — decima quinta confirmacao de `MEM-APR-0002`. **`F3`:** **cinco** abstracoes evitadas, cada uma com a regra que a dispensa citada. **`F4`:** a unica dimensao que piorou **piorou de proposito**, e o tradeoff esta declarado em **quatro** lugares com o sentido invertido em relacao ao intuitivo — **promover a norma protege e encarece**. **`F5`:** decima medicao da serie, **comparavelmente favoravel a 1.13**, e a razao e estrutural: **nao se escreveu norma, migrou-se norma por ferramenta**; **`0` linhas de evidencia externa lidas**. **`F6`:** **sete** metodos reutilizaveis, e o mais forte foi **medir a alternativa antes de discuti-la** — foi assim que `RD-43` apareceu, e ele **nao era encontravel por leitura**. **`C11`: 13 de 13 conformes.** Fechamento **`READY-FOR-RATIFICATION`**, com as outras tres opcoes recusadas uma a uma. **`0` objetos entraram em vigor.** |
