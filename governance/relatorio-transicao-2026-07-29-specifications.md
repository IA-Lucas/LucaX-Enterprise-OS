---
id: PT-2026-007
titulo: Relatorio de transicao da Missao 1.13 — Framework de Specifications instituido, RD-23 fechada e os dois pilotos bloqueados por norma
tipo: relatorio
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: DEP-PRD
proprietario: DEP-PRD
aprovador: DEP-EXE
criado_em: 2026-07-29
atualizado_em: 2026-07-29
revisao_prevista: null
decisoes_relacionadas: [ADR-0012, ADR-0015, ADR-0018, ADR-0019, ADR-0020, ADR-0021]
substitui: []
substituido_por: null
canal: REPORTE
emissor: DEP-PRD
destinatario: SOBERANO
ttl: ate a proxima missao
resumo: Registra a instituicao do Framework de Specifications em SF-01 a SF-32, o fechamento de RD-23 com cinco defeitos corrigidos, seis achados novos e a decisao ADJUST por impossibilidade normativa dos dois pilotos.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# PT-2026-007 — Framework de Specifications

> ## Decisao desta missao: **`ADJUST`**
>
> **O Framework de Specifications esta instituido, testado e verificado de forma independente.**
> `SF-01` a `SF-32` vivem em [ADR-0021](../decisions/ADR-0021-framework-de-specifications.md),
> `C2 · Tipo 2`, com **`0` arquivos de `foundation/` alterados** — medido por `cmp` — e **`0`
> entidades, tipos documentais, portoes, papeis, classes ou verbos de autoridade criados**.
>
> **A pre-correcao obrigatoria fechou, e maior do que estava declarada.** **`RD-23`** apontava
> **dois** defeitos em `TPL-spec`; a medicao campo a campo encontrou **cinco**, e os cinco estao
> corrigidos em **1.1.0**, com diff literal e reversivel.
>
> **As duas Specs piloto NAO foram criadas, e a razao nao e escolha desta missao: e norma.**
> Tres fontes vigentes vinculam `Spec` a `Produto` — **`FND-04 §6`** *("Produto existe", e
> "todas precisam ser verdadeiras")*, **`FND-03 §3.6`** e **`FND-10 §4.4`** —, e mediu-se
> **`0` Specs, `0` Produtos e `products/` ausente da raiz**. **Criar Produto e `C2 · Tipo 1` do
> SOBERANO.** As duas saidas — **`S1`** *(ato que crie o primeiro Produto)* e **`S2`**
> *(`RFC C3 → ADR C3 → ato`, ampliando `Spec` a materia nao-produto)* — sao **disjuntas**, e
> **cada piloto pedido depende de uma delas**.
>
> **Seis achados novos, todos com dono, gatilho e instrumento.** **`RD-31`** *(Alta)* — a Carta
> de `DEP-PRD` tem **8** afirmacoes que `ADR-0018` e `ADR-0019` tornaram falsas, **4 nunca
> enumeradas**, e **`DEP-EXE` nao declara `QG-1` em nenhuma linha**: **o portao da Spec nao tem
> titular declarado em Carta alguma**. **`RD-32`** *(Media)* — **4** contadores oficiais de
> sequencia defasados em **8** valores, com risco real de **colisao de identificador**.
> **`RD-33`** *(Alta)* — o vinculo `Spec × Produto`. **`RD-34`** *(Baixa)* — **19 de 19** `TPL`
> declaram `aprovador: SOBERANO`. **`RD-35`** *(Media)* — **2** agregados de indice divergentes
> da fonte. **`RD-36`** *(Media)* — **o razao de ressalvas nao fecha**, e a reconciliacao completa
> **nao foi executada**: o limite esta declarado, com dono e gatilho.
>
> **`RC-02` atendida por construcao: `DEP-GOV` nao e autor de nenhum instrumento normativo desta
> missao — primeira vez em quinze.**

## Proposito
Registrar o que a Missao 1.13 construiu, com que instrumento, com que evidencia e a que custo; o
fechamento de `RD-23`; os seis achados novos; a reconciliacao de divida; e a decisao.

## Escopo
| Item | Definicao |
|---|---|
| **Inclui** | A instituicao de `SF-01` a `SF-32`; a correcao de `TPL-spec` **1.1.0**; a avaliacao **seletiva** da evidencia externa `A4`; os **doze** casos de determinismo; a reconciliacao de catalogo e indices; **seis** achados novos; a baseline **`BL-2026-07-29-09`**; a medicao de contexto; a decisao |
| **Nao inclui** | As **duas Specs piloto** — §6, impossivel por norma · qualquer `Skill`, `Tool`, `Command`, `Workflow`, `Agente`, `Produto`, `Projeto`, codigo, infraestrutura, ontologia ou migracao · emenda a `FND-01`, `FND-02` ou `FND-10` *(`RD-27`)* · edicao de baseline historica *(`RD-28`, `BL-02`)* · `FND` novo · emenda a Carta *(`RD-31` — exige ato)* · `RD-24`, `RD-30`, `RD-10` a `RD-13`, `RD-18`, `RD-21` |
| Natureza | **Reporte**, tipo documental de [FND-10 §4.6](../foundation/10-artifact-framework.md), entidade `MSG`. **Nenhum tipo, entidade, camada, template ou diretorio novo** |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| **Autor da norma e deste reporte** | **DEP-PRD** | [FND-09 §8.2](../foundation/09-meta-model.md), linha `SPC` — *propoe/cria*; `P-4` da Carta |
| **Revisores independentes** | **DEP-ENG** + **DEP-QAR** | FND-09 §8.2, linha `SPC`; `AC-03` |
| **Verifica aptidao** | **DEP-QAR** | `QG-6`, `CC-04` — [FIT-2026-015](fitness/FIT-2026-015-framework-de-specifications.md) |
| **Aprova este reporte e ADR-0021** | **DEP-EXE** | FND-04 §2, C2; FND-07 §2.4 |
| **Aprova `TPL-spec` 1.1.0** | **DEP-GOV** | FND-09 §8.2, linha `TPL` |
| **Registra e indexa** | **DEP-GOV** | `PA-03`; FND-04 §4 `[7]` |
| **Grava em memoria** | **DEP-KMS** | `PA-09`; `QG-5`; [MEM-APR-0006](../memory/aprendizado/MEM-APR-0006-exercer-o-contador-revela-o-defeito.md) |
| **Decide `S1` ou `S2`** | **SOBERANO** | `FND-01 §7.3` — *portfolio: criar produto* |

> **Residuo declarado (`PI-10`), e ele mudou de lugar.** Nas quatorze missoes anteriores o
> residuo era *"DEP-GOV apura e DEP-GOV redige"*. Nesta, **DEP-GOV nao e autor de nenhum
> instrumento normativo**: autoria **DEP-PRD**, revisao **DEP-ENG + DEP-QAR**, verificacao
> **DEP-QAR**, aprovacao **DEP-EXE**, `TPL` aprovado por **DEP-GOV**, registro **DEP-GOV**.
> **Residuo remanescente:** DEP-GOV **registra** o catalogo que declara defeito em contadores de
> DEP-GOV — **`RD-32`**, familia `RC-02`, **setima ocorrencia, declarada e nao resolvida**.

---

## 1. Condicoes de eficacia desta missao

| # | Exigencia | Resultado |
|---|---|---|
| **A1** | Copia datada integral fora do repositorio, **antes** de qualquer escrita | ✅ **542 arquivos** em `_backups/LucaX-Enterprise-OS_2026-07-29_pre-missao-1-13/`, **reconferida na copia**: **164 · 46.353 · `8cf2143c…b027a7f`** |
| **A2** | Reproducao da baseline vigente antes das edicoes | ✅ **`BL-2026-07-29-08` reproduz nos 64 digitos** pelo comando publicado em §10.5 do catalogo |
| **A3** | Pre-condicao `GO-TO-SPECS` verificada na fonte, nao na memoria | ✅ [PT-2026-006 §8](relatorio-transicao-2026-07-29-fechamento-operacional.md) lido integralmente — **8 de 8**; `ADR-0019` e `ADR-0020` conferidos `ativo` no frontmatter |
| **A4** | **`FND-01`, `FND-02` e `FND-10` nao alteradas** *(pre-correcao `RD-27`)* | ✅ **`0` bytes**, verificado por `cmp` contra a copia datada |
| **A5** | Nenhuma baseline historica editada *(pre-correcao `RD-28`)* | ✅ §10.0 a §10.5 do catalogo **nao foram tocadas**; a nova medicao recebeu **identificador novo** (`BL-02`) |
| **A6** | **`RD-23` corrigida antes de qualquer Spec** | ✅ `TPL-spec` **1.1.0** — §3. E **nenhuma Spec foi criada**, o que torna a ordem trivialmente satisfeita |
| **A7** | Autoria, teste e avaliacao **nao concentrados em DEP-GOV** *(`RC-02`)* | ✅ **5 departamentos em 5 funcoes**; DEP-GOV em **nenhum** instrumento normativo |
| **A8** | Integridade referencial apos as edicoes | ✅ **§7** |

## 2. O que foi construido — `SF-01` a `SF-32`

A norma vive em **fonte unica**:
[ADR-0021 §5](../decisions/ADR-0021-framework-de-specifications.md). **Este relatorio nao a
reproduz** (`PJ-01`, `CM-09`). O mapa dos nove entregaveis da missao contra a regra que os
atende:

| # | Entregavel pedido | Onde vive | Estado |
|---|---|---|---|
| **1** | **Spec Contract** — identidade, proposito, escopo, autoridade, custodiante, autores, revisores, aprovadores, Capability, Departamento, consumidores, requisitos, exclusoes, interfaces, dependencias, riscos, evidencias, verificacao, vigencia, contexto e evolucao | `SF-05` a `SF-09` — **21 blocos**, cada um com **a fonte da exigencia** em coluna propria | ✅ **completo** |
| **2** | **Semantica normativa** — `MUST`/`SHOULD`/`MAY`, requisito com ID, motivo, fonte, aceite, metodo e evidencia; separar fato, requisito, hipotese, decisao, recomendacao e nota; proibir termo sem definicao | `SF-11` a `SF-16` — **3** verbos com equivalentes exclusivos, **6** campos por requisito, **6** naturezas, **5** metodos, **10** adjetivos vedados por nome | ✅ **completo** |
| **3** | **Perfis** — funcional, interface, dados, qualidade, seguranca, operacao, avaliacao; perfil nao vira entidade; especializacao exige evidencia | `SF-17` a `SF-19` — **7** perfis; `SF-18` **proibe** a promocao automatica; `SF-19` exige **autoridade ou ciclo distinto + 2 sinais observados + teste de FND-04 §6.2** | ✅ **completo** |
| **4** | **Autoridade e ciclo** — `C0`–`C3` × `Tipo 1/2` para dez etapas; Spec nao cria autoridade nem aprova a si propria; reutilizar estados e `ADR-0020` | `SF-10` + a matriz de **50 celulas** de §5.3, **projecao declarada** `PJ-02`; `SF-03` | ✅ **completo · 0 titulares novos** |
| **5** | **Rastreabilidade** — a cadeia de nove elos; relacoes refina, restringe, implementa, verifica, conflita, substitui | `SF-20` a `SF-22`; as **6** relacoes mapeadas as **10** de `FND-09 §6.1`, com **`conflita` declarada achado, nao aresta** | ✅ **completo** |
| **6** | **Qualidade** — DoR e DoD; funcionais, nao funcionais, negativos e de falha; suposicoes, limites, rollback, abandono; indicador sem valor nao prova | `SF-23` a `SF-26` — **DoR de 9**, **DoD de 10**, **4** categorias, **4** limites | ✅ **completo** |
| **7** | **Mudanca** — versao, impacto, compatibilidade, dependentes, migracao, depreciacao, substituicao; proibir alteracao silenciosa e heranca implicita | `SF-27` a `SF-30` — versao **pelo efeito**; `SF-28` declara **nula** a alteracao silenciosa e **proibida** a heranca implicita | ✅ **completo** |
| **8** | **Economia de contexto** — resumo, gatilhos, pacote minimo, secoes sob demanda, custo medido; carregar requisito sem o documento | `SF-31` — **5** exigencias, e o requisito **enderecavel por `RQ-nn`** | ✅ **completo** |
| **9** | **Template, registro e dois pilotos** | `SF-32` + [`TPL-spec` **1.1.0**](../foundation/templates/TPL-spec.md) | ⚠️ **PARCIAL** — template ✅ · registro ✅ · **pilotos ❌, §6** |

**Oito de nove completos. Um parcial, e a parte que falta e a que a norma impede.**

### 2.1 Sobre o *"registro mestre"* — **mantido, nao criado**

A missao pediu *"manter um template canonico e registro mestre"*. **`SF-32` mantem os dois que
ja existem e recusa criar um terceiro:**

| Funcao | Onde vive | Fundamento da recusa de criar novo |
|---|---|---|
| **Template canonico** | [`TPL-spec`](../foundation/templates/TPL-spec.md), **unico** | Especializar template exige `FND-10 §10.2` |
| **Registro transversal** | [catalogo mestre](artifact-registry.md) | **`RG-04`** ja o declara *"a visao transversal do acervo"* |
| **Contador oficial de `SPC`** | O **indice do diretorio** onde as Specs vivem | `FND-03 §2.3`, `RG-04` — *"aqueles sao os contadores oficiais de sequencia"* |
| **Arquivo satelite por Spec** | **nao existe** | **`RG-05`** o proibe expressamente |

**Criar um registro proprio de Specs seria proliferacao** (`FND-04 §6.1`) **e segunda fonte de
verdade** (`PJ-01`). **`manter` nao e `criar`.**

## 3. `RD-23` — **fechada, e maior do que estava declarada**

O achado declarava **dois** defeitos: `aprovador: DEP-PRD` fixo e ausencia de `ratificacao`. **A
medicao campo a campo contra `FND-10 §2.2` e `FND-09 §8.2` encontrou cinco.**

| # | Defeito | Norma contrariada | Corrigido |
|---|---|---|---|
| **T1** | Esqueleto fixava `aprovador: DEP-PRD` | `FND-09 §8.2` linha `SPC`: **`conforme classe`** | ✅ **derivado da classe** |
| **T2** | Esqueleto sem `ratificacao` | `FND-09 §8.2`; `LM-02` | ✅ presente, `nao-exigida` salvo **C3/Tipo 1** |
| **T3** | Esqueleto sem `resumo`, `perfil_contexto`, `confidencialidade`, `revisor` | `FND-10 §2.2`; `AC-06` | ✅ **os quatro acrescentados** |
| **T4** | §11 declarava *"Liberado por `DEP-PRD`"* | `FND-01 §6.2` pos-`ADR-0018`: **`DEP-EXE`** | ✅ **`DEP-EXE`**, com a nota *liberar ≠ aprovar* |
| **T5** | §Responsaveis sem revisor | `FND-09 §8.2`; `AC-03` | ✅ **`DEP-ENG` + `DEP-QAR`** |

**Evidencia criptografica da correcao, medida:**

| Campo | Valor |
|---|---|
| `TPL-spec` **1.0.0** — `sha256` · linhas | **`cabaa58e…f748`** · **132** |
| `TPL-spec` **1.1.0** — `sha256` · linhas | **`afd0dc7e…370f`** · **272** |
| **Terminadores de linha** | **`LF` integral, preservado** — **0 bytes `CR`** antes e depois, medido |
| Diff | **literal e reversivel** — [ADR-0021 §5.12](../decisions/ADR-0021-framework-de-specifications.md) |
| Classe do rito | **C2**, aprovado por **DEP-GOV** *(FND-09 §8.2, linha `TPL`)*, dentro de `ADR-0021` aprovado por **DEP-EXE** |

**Autoridade derivada, nao fixada — a exigencia literal da pre-correcao.** O template agora
declara `aprovador: <derivado da classe — FND-04 §2>` e remete a `SF-10`, que faz a autoridade
depender de **classe do efeito** *(com `C1` como piso)*, **tipo de reversibilidade**, **materia**
e **Departamento custodiante**. **`DEP-PRD` deixa de ser aprovador universal**, e a **ratificacao
aparece quando `C3` ou `Tipo 1`** — as duas coisas que a missao exigiu.

## 4. Evidencia externa `A4` — **avaliada, nao adotada**

**Consumo seletivo, medido: 236 de 33.676 linhas — `0,70%`.** O tratamento integral esta em
[ADR-0021 §8.2](../decisions/ADR-0021-framework-de-specifications.md); este relatorio nao o
reproduz (`PJ-01`).

| Item | Veredito |
|---|---|
| **`AC-03-REP-010`** — portao spec → codigo, spec assinada pelo humano | **Tese convergente, forma recusada.** A ordem *spec antes de construir* **confirma** `QG-1`; a **assinatura humana por Spec** foi **recusada** por contrariar `PA-13` e `ADR-0019` — poria o Soberano como operador recorrente. TDD/YAGNI/DRY sao materia de `DEP-ENG` e nao entram em Spec (`SF-02`) |
| **`AC-05-REP-001`** — fluxo `/spec → /plan → /build → /test → /review → /ship` | **Recusado integralmente.** `Command` **nao e artefato** — `FND-10 §4.8` o recusa, com gatilho de reabertura **nao observado**; importar criaria **seis portoes paralelos aos sete de `FND-01 §6.2`**, e portao novo e **C3** |
| **`AC-02-PRT-003`** — criterio de sucesso antes de framework | **Convergencia registrada** com `SF-23` item 1; nada a importar |

**O limite da evidencia, declarado pelo proprio pacote e verificado na leitura:** **zero medicao
de eficacia foi lida** — *"toda economia de token, taxa de deteccao e ganho de qualidade deste
pacote e alegacao, nao fato"* (`L-04` do resumo executivo). **Nenhum `SF-*` tem a `A4` como
fundamento; nenhum numero dela entra no acervo** (`CE-04`, `LV-12`). A `A4` permanece
**`external-evidence`, provisoria, nao normativa e nao adotada**, com **`ADOPT = 0`** declarado
na propria fonte. **0 formatos importados · 0 bytes copiados** (`FR-03`, `ADR-0007`).

> **O resultado util de avaliar evidencia externa foi recusar duas praticas fortes com norma
> citada.** Os dois artefatos recusados sao `LV4` com licenca `MIT` integra e suite de testes —
> **os mais fortes do pacote na materia**. Recusa fundamentada e informacao; adocao por
> qualidade aparente seria `FR-03`.

## 5. O framework testado — **doze casos, e um deles falhou de proposito**

A bateria integral esta em
[ADR-0021 §9](../decisions/ADR-0021-framework-de-specifications.md); **nao reproduzida aqui**
(`PJ-01`). O que importa registrar:

| Resultado | Casos |
|---|---|
| **Deterministicos e coerentes** | **11** — criacao, criacao interdepartamental, aprovador fixado, adjetivo sem definicao, requisito incompleto, decisao embutida, conflito, mudanca de `MUST`, evidencia sem valor, superacao, e *"quem aprova esta Spec `C2`?"* |
| ⚠️ **Deterministico e DIVERGENTE** | **1** — **`T-12`**: *"quem libera `QG-1`?"* **lido nas Cartas** devolve **`DEP-PRD`**; `FND-01 §6.2` diz **`DEP-EXE`** |
| **Determinados e nao observados** | **`T-07`** *(conflito)* · **`T-10`** *(superacao)* · e, por `A1`, **todos os que pressupoem Spec real** |

**A divergencia de `T-12` nao foi contornada: virou `RD-31`**, com dono, gatilho, custo e
instrumento. **Foi o unico teste da missao que a arquitetura reprovou, e ele reprovou porque a
pergunta era exatamente a que a missao mandou testar** — *consumo por futura Skill sem
interpretacao informal*.

## 6. **Os dois pilotos — nao criados, e a razao e norma**

### 6.1 As tres fontes, citadas por identificador

| Fonte vigente | Texto literal | Efeito |
|---|---|---|
| **`FND-04 §6`**, linha *Spec* | pre-condicoes: ***"Produto existe**; problema definido; criterios de aceite verificaveis; escopo negativo explicito"*, e *"**Todas** precisam ser verdadeiras para a criacao ser aprovada"* | **`O1` nao pode ocorrer** (`FND-10 §5.2`) |
| **`FND-03 §3.6`** | *"Vive em `products/<slug>/specs/<SPC-id>.md`"* | **Sem caminho canonico** fora de produto; `FND-03 §7.1`: *"um artefato existe em exatamente um lugar"* |
| **`FND-10 §4.4`** | Local: **`products/<slug>/specs/`** | Terceira fonte, mesmo vinculo |

### 6.2 A medicao, feita antes de qualquer escrita

| Evidencia | Valor | Metodo |
|---|---|---|
| Diretorios na raiz do acervo | **8** — `products/` **ausente** | `ls -d */` |
| Artefatos de tipo `spec` | **0** | varredura de `tipo:` em frontmatter |
| Artefatos de produto | **0** | varredura por `products/` e por tipo |
| Declaracao na fonte | **`KP-3` de `DEP-PRD`**: *"`0` — **proibido nesta fase, por determinacao**"*; **`KP-4`**: *"`0` Specs emitidas"* | leitura da Carta vigente |

### 6.3 E criar Produto nao esta ao alcance de nenhum Departamento

`FND-04 §6`, linha *Produto*: ***"Decisao do Soberano"***, classe **C2 · Tipo 1**.
`FND-09 §8.2`, linha `PRO`: aprova e ratifica **SOBERANO**. `FND-01 §7.3`: *"Portfolio:
criar/encerrar produto → Soberano"*. **`DEP-PRD §4`** declara que **nao lhe compete**, e **`§8`**
escala em **`E4`, bloqueando execucao**.

### 6.4 As duas saidas faceis eram violacao, e as duas foram recusadas

| Saida recusada | Norma que a proibe | O que produziria |
|---|---|---|
| Escrever as Specs em outro diretorio | `FND-03 §3.6`, `FND-03 §7.1`, `FND-10 §4.4` | Artefato **nulo** (`MT-01`, `AC-06`) + incidente (`LV-11`) |
| Criar `products/` e uma Carta de Produto | `FND-04 §6` — **C2 · Tipo 1 do SOBERANO**; restricao expressa da missao | Componente criado sem competencia (`LV-06`, `LV-07`) |
| **Declarar o bloqueio com as fontes e as duas saidas** | `PI-10`, `LV-05` | ✅ **e o que foi feito** |

### 6.5 As duas saidas, disjuntas, ambas do SOBERANO

| Saida | Instrumento | Habilita | Custo declarado |
|---|---|---|---|
| **`S1`** | Ato soberano que **crie o primeiro Produto** *(C2 · Tipo 1)* | A Spec **de baixo risco**, de produto — que a norma **ja preve integralmente** | 1 Carta de Produto + 1 ADR + ratificacao |
| **`S2`** | **`RFC C3 → ADR C3 → ato`**, ampliando `Spec` a materia **nao-produto** | A Spec **interdepartamental** — que a norma **nao preve** | 1 RFC + 1 ADR + diff de **3** fontes + pacote + ato |

**`S1` nao habilita o piloto interdepartamental; `S2` nao cria produto.** **A missao pediu um de
cada, e cada um depende de uma saida diferente.** A escolha e do Soberano (`FND-01 §7.3`), e
**este relatorio nao a antecipa**.

> **O framework nao depende dos pilotos para existir nem para ser testavel — e foi testado em
> doze casos.** O que os pilotos provariam e a **eficacia**, e essa e a ressalva `R1` de
> [FIT-2026-015](fitness/FIT-2026-015-framework-de-specifications.md): **as 32 regras sao
> determinadas e nao observadas**, e o registro diz isso em vez de sugerir o contrario.

## 7. Reconciliacao de catalogo, indices e fontes

### 7.1 Achado `RD-31` — a Carta de `DEP-PRD` afirma autoridade que ela nao tem mais

| Campo | Conteudo |
|---|---|
| **Objeto** | [`departments/prd/carta.md`](../departments/prd/carta.md) **1.0.0**, `ativo`, **`ratificada`** |
| **Defeito** | **8** afirmacoes que `ADR-0018` e `ADR-0019` — **ambos ratificados e vigentes** — tornaram **falsas**: `§3 P-8` · `§5` L135 · `§5` L136 · `§5.2` L159 · `§5.2` L162 · `§7` L211 · `§10.1 RP-1` · `§12.3` L382. Enumeracao integral em [RFC-0017 §3.4](../rfcs/RFC-0017-framework-de-specifications.md) |
| **O que e novo** | [PT-2026-004 §3.1](relatorio-transicao-2026-07-29-ratificacao.md) mediu o *"conjunto estreito"* e enumerou **4**. **A medicao desta missao encontra 8** — as nao enumeradas sao `P-8`, `§5.2` L159, `RP-1` e `§12.3`. **A causa e a mesma de `RD-23`:** procurou-se **a frase que ficaria falsa**, nao **o papel que mudou de titular** |
| **Consequencia verificavel** | **`DEP-EXE` nao declara `QG-1` em nenhuma linha da propria Carta — `0` ocorrencias, medido.** Logo **o portao da Spec nao tem titular declarado em Carta alguma**: quem resolve pelas Cartas obtem `DEP-PRD`; quem resolve pela fonte obtem `DEP-EXE`. E o caso **`T-12`** |
| **Atenuante real, e nao e cumprimento** | **`LV-03` continua valendo integralmente**: liberacao de portao por quem produziu o artefato e **nula**, independentemente do que a Carta diga. `§5.1` da mesma Carta — *"o que **nao** decido"* — **nao lista** `QG-1`, e deveria |
| **Por que nao foi corrigido** | Emendar Carta de Departamento: `FND-09 §8.2`, linha `DEP` — **propoe `DEP-EXE`, revisa `DEP-GOV`, aprova e ratifica o `SOBERANO`**. **Nao cabe em missao ordinaria** |
| Severidade · dono · gatilho | **Alta** · **DEP-EXE** *(propoe)*; revisa **DEP-GOV** · **antes da primeira Spec**, ou proximo ato que alcance `DEP-PRD` ou `DEP-EXE` |
| **Instrumento** | **RFC + ADR + diff + pacote soberano + ato**, com as **duas** Cartas em um unico ato — `DEP-PRD` *(remover 8 afirmacoes, acrescentar `QG-1` a `§5.1`)* e `DEP-EXE` *(declarar `QG-1` em `§5` e `§5.2`)* |
| **Estado** | **ABERTO**, com instrumento identificado e impedimento declarado. Ressalva **`R3`** de FIT-2026-015 |

### 7.2 Achado `RD-32` — quatro contadores oficiais defasados

| Campo | Conteudo |
|---|---|
| **Objeto** | [`decisions/README`](../decisions/README.md) · [`rfcs/README`](../rfcs/README.md) · [`governance/fitness/README`](fitness/README.md) · [`governance/README`](README.md) |
| **Defeito** | Cada contador declarava **um numero a menos** do que a propria tabela abaixo dele lista: `ADR` **`0019`/`0020`** com `ADR-0020` existente · `RFC` **`0015`/`0016`** com `RFC-0016` existente · `FIT` **`013`/`014`** com `FIT-2026-014` existente, **em dois indices**. **4 tabelas · 8 valores** |
| **Consequencia** | **Colisao de identificador.** Quem confiasse no contador criaria `ADR-0020`, que ja existe — contra `FND-03 §2.3`, *"numero nunca e reaproveitado"* |
| **O que foi varrido, declarado** | **9 sequencias em 7 indices** — `ADR`, `RFC`, `FIT` *(×2)*, `EXC`, `INC`, `MEM-APR`, `MEM-EST`, `MSG`. **4 defasadas · 5 corretas.** O defeito **nao e sistemico**: e das sequencias movimentadas pelas Missoes 1.12 e 1.12.1 |
| **Familia** | **Segunda ocorrencia.** `governance/README` **documenta a primeira** em nota propria — `FIT` *"um numero atras do real desde a Missao 1.3"*, fechada como `C11` de REV-CONSOLIDACAO. **A correcao anterior atingiu o valor e nao o gatilho `CV-04`** |
| **Tratamento** | ✅ **CORRIGIDO nos quatro**, valor a valor. **Zero fontes normativas alteradas** — os quatro sao `M3` (`RG-03`, `PJ-03`). **E a causa foi codificada em regra:** `SF-32` — *criar artefato de sequencia e incrementar o contador sao a mesma mudanca* |
| Severidade · dono | **Media** · **DEP-GOV** |
| **Como foi encontrado** | **Exercendo o contador** — pedindo o numero de `ADR-0021`. **Ler o indice nao revelaria: a tabela estava certa.** [MEM-APR-0006](../memory/aprendizado/MEM-APR-0006-exercer-o-contador-revela-o-defeito.md) `V1` |

### 7.3 Achado `RD-33` — a `Spec` esta vinculada a `Produto`

| Campo | Conteudo |
|---|---|
| **Objeto** | `FND-03 §3.6` · `FND-04 §6` linha *Spec* · `FND-10 §4.4` |
| **Defeito** | **Nao e defeito de acervo — e norma funcionando, e uma lacuna de cobertura.** As tres fontes vinculam `Spec` a `Produto`; **nao existe categoria de Spec sobre materia interdepartamental**, que a missao pediu |
| **Consequencia** | **`GO-TO-SPECS` esta liberado e nao pode ser exercido.** Nenhuma Spec e criavel |
| **Por que nao foi corrigido** | Ampliar a Spec altera **tres** fontes de nivel 2, uma delas **`FND-10`** — vedada pela pre-correcao `RD-27` — e a **arvore canonica** de `FND-03 §7`. Classe **C3**, ratificacao indelegavel |
| Severidade · dono · gatilho | **Alta** · **SOBERANO** *(decide `S1` ou `S2`)*; instrui **DEP-PRD** · **imediato — bloqueia a primeira Spec** |
| **Instrumento** | **`S1`** *(ato criando Produto)* **ou** **`S2`** *(RFC C3 → ADR C3 → ato)* — §6.5 |
| **Estado** | **ABERTO e BLOQUEANTE.** E a **unica** pendencia bloqueante do acervo |

### 7.4 Achados `RD-34` e `RD-35`

| Campo | **`RD-34`** | **`RD-35`** |
|---|---|---|
| **Objeto** | Os **19** `TPL` de `foundation/templates/` | [`governance/README`](README.md) · [`memory/README`](../memory/README.md) |
| **Defeito** | **19 de 19** declaram **`aprovador: SOBERANO`** no proprio cabecalho, enquanto `FND-09 §8.2` linha `TPL` e `FND-10 §10.3` linha *Template* dao **`Aprova: DEP-GOV`** e **`Ratifica: —`** | **3 agregados divergentes da fonte:** *(a)* `governance/README` declarava **`19` de `46`** ressalvas quando **`28 + 19 = 47`**; *(b)* `memory/README` dava a camada **APR** autoridade **`5`** onde `FND-06 §2` diz **`4`** — **dois cincos tornavam `MM-03` indeterminado**; *(c)* declarava **`3`** registros `OPR` onde ha **`6`**, **tres missoes de atraso** |
| **Leitura alternativa declarada** | O campo pode registrar **fato historico** — os templates foram acolhidos pelo ato que adotou a Fundacao — e nao afirmacao de norma. **A duvida fica aberta**, e e a pergunta `Q4` de [RFC-0017 §9](../rfcs/RFC-0017-framework-de-specifications.md) | Nenhuma — os tres divergem de fonte citavel por identificador |
| **Por que nao foi corrigido** | **Corrigir um dos 19 cria divergencia entre iguais.** Corrigir os dezenove e **outra materia**, com rito proprio (`FND-09 §8.2` linha `TPL`). **A extracao de frontmatter da familia inteira e o que barrou a correcao parcial** | — |
| **Tratamento** | **NAO corrigido.** Declarado com leitura alternativa | ✅ **CORRIGIDO na projecao**, item a item; **0 fontes alteradas** (`PJ-03`, `RG-03`, `M3`). A enumeracao de `OPR` foi **substituida por remissao a fonte** (`PJ-01`), para nao envelhecer outra vez |
| Severidade · dono · gatilho | **Baixa** · **DEP-GOV** · *"proxima emenda que alcance os `TPL`"* | **Media** · **DEP-GOV** · imediato |
| **Familia** | Primeira ocorrencia | **Decima primeira** de [MEM-APR-0002](../memory/aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md); causa `CV-04`. **Segunda vez que a mitigacao `RG-2` — *somar o agregado contra a propria linha* — e exercida** |

### 7.5 O que esta missao alterou — **medido por `cmp` contra a copia datada**

| Categoria | Quantidade | Quais |
|---|---|---|
| **Fontes normativas alteradas** | **0** | Nenhum arquivo de `foundation/*.md`, `departments/`, `capabilities/`; nenhum `ADR`, `RFC`, `FIT`, `INC`, `MSG`, pacote, revisao, relatorio ou baseline **preexistente**. **`FND-01`, `FND-02` e `FND-10`: `0` bytes** |
| **Artefatos `M2` alterados** | **1** | [`TPL-spec`](../foundation/templates/TPL-spec.md) **1.0.0 → 1.1.0** — emenda **C2** por `ADR-0021`, com diff literal reversivel |
| **Artefatos criados** | **5** | `RFC-0017` · `ADR-0021` · `FIT-2026-015` · `MEM-APR-0006` · `PT-2026-007` |
| **Projecoes `M3` atualizadas** | **8** | catalogo mestre · `README` raiz · `decisions/README` · `rfcs/README` · `governance/README` · `governance/fitness/README` · `memory/README` · `memory/aprendizado/README` |
| **Arquivos removidos** | **0** | `LC-10`, `RB-05` |

### 7.6 Integridade referencial apos as edicoes

| Evidencia | Valor | Metodo declarado |
|---|---|---|
| **Links relativos** | **2.336 verificados · 0 quebrados** | Metodo de §10.5 do catalogo, aplicado sem alteracao: todo alvo `] (destino)` em `.md` da coorte, excluidos `http:`, `https:`, `mailto:` e ancoras puras, com o fragmento `#` removido, normalizado contra o diretorio de origem e testado por existencia. **Cada ocorrencia conta uma vez** |
| **Autoverificacao** | **109 artefatos com `autor` e `revisor` · 0 coincidencias** | Comparacao dos dois campos de frontmatter |
| **`id` e `versao`** | **0 ausencias em 169** | Verificacao campo a campo |
| **Credencial em texto** | **0 ocorrencias** | Varredura por padrao de segredo (`PI-08`, `LV-02`) |

## 8. Custo de contexto — a nona medicao da serie

A itemizacao integral esta em
[FIT-2026-015 §F5.1](fitness/FIT-2026-015-framework-de-specifications.md); **nao reproduzida
aqui** (`PJ-01`).

| Metrica | Valor |
|---|---|
| Pacote carregado — **acervo** | **3.578** linhas |
| Pacote carregado — **evidencia externa `A4`** | **236** linhas |
| **Total** | **3.814** linhas |
| Acervo no inicio da missao | **46.353** linhas |
| **% do acervo, so acervo** | **7,72%** |
| **% do acervo, total** | **8,23%** |
| Comparacao com a Missao 1.12.1 | **2.522 · 5,7%** → **+41,9%** em linhas, **+2,02 p.p.** |
| Consumo seletivo da `A4` | **236 de 33.676 = 0,70%** |

**O crescimento e declarado como desfavoravel, e a razao e medida:** `RD-22` era **uma** pergunta
com **cinco** fontes nomeadas no proprio achado; esta missao teve de reconstruir **a cadeia de
autoridade inteira da Spec** — quinze secoes de cinco fundacionais, tres ADRs e uma Carta —
**porque nenhum lugar a tinha reunida, e era esse o defeito que a missao corrigiu**. **A
comparacao que interessa e prospectiva:** o proximo consumidor le **1 ADR `sob-demanda` + 1
template**, e para uma exigencia pontual, **um bloco de requisito enderecado por `RQ-nn`**
(`SF-31`).

## 9. Divida reconciliada — categoria por categoria

| Achado | Categoria | Evidencia |
|---|---|---|
| **`RD-23`** | ✅ **RESOLVIDA — na fonte, e maior do que declarada** | §3. **5** defeitos corrigidos onde o achado citava **2**; `TPL-spec` **1.1.0**, hash antes e depois medidos |
| **`RD-31`** | **NOVA — ABERTA, com instrumento identificado e impedimento declarado** | §7.1. Exige ato; ressalva `R3` |
| **`RD-32`** | **NOVA — RESOLVIDA na projecao, e a causa codificada em regra** | §7.2. **4** contadores; `SF-32` fecha o gatilho |
| **`RD-33`** | **NOVA — ABERTA e BLOQUEANTE** | §7.3. **Unica pendencia bloqueante do acervo** |
| **`RD-34`** | **NOVA — ABERTA, com leitura alternativa declarada** | §7.4. **19 de 19**; corrigir um criaria defeito novo |
| **`RD-35`** | **NOVA — RESOLVIDA na projecao** | §7.4. **2** agregados; enumeracao substituida por remissao |
| **`RD-36`** | **NOVA — PARCIALMENTE TRATADA, com o limite declarado** | §7.6. A **cascata devida** foi executada *(as 2 ressalvas de `FIT-2026-014`, ausentes desde a missao anterior, e as 3 de `FIT-2026-015`)* e os agregados foram **substituidos pelos valores medidos**; **a reconciliacao completa NAO foi executada**, e o motivo esta escrito |
| **`RD-27`** | **MANTIDA — nao tocada, por determinacao** | Pre-correcao da missao. **`FND-01`, `FND-02` e `FND-10`: `0` bytes alterados**, por `cmp` |
| **`RD-24`** · **`RD-30`** | **MANTIDAS** | §10.0 a §10.5 do catalogo **nao editadas** — `BL-02` |
| **`RD-26`** | **MANTIDA RECONCILIADA** | §2.1 do catalogo **reproduz o total do acervo** outra vez, agora com a coorte de `BL-09` |
| **`RD-17`** | **MANTIDA RESOLVIDA** | A lista fechada reproduziu **tres vezes** nesta missao |
| **`RD-14`** · **`RD-15`** | **MANTIDAS RESOLVIDAS na fonte, e `RD-31` e o residuo de cascata** | As emendas **vigoram**; o que faltou foi **propagar as Cartas** — e isso e `RD-31`, achado **novo**, nao reabertura |
| `RD-10` · `RD-11` · `RD-12` · `RD-13` · `RD-18` · `RD-21` | **MANTIDAS** | Dono e gatilho inalterados; nenhuma alcancada por esta missao |
| Familia **`RC-02`** | **DECLARADA, NAO RESOLVIDA — setima ocorrencia, e a mais mitigada** | **DEP-GOV nao e autor de nenhum instrumento normativo desta missao: primeira vez em quinze.** Residuo em `RD-32` |

**Zero renomeacoes. Zero reclassificacoes de conveniencia.** Uma resolucao **na fonte**
(`RD-23`), duas **na projecao** (`RD-32`, `RD-35`), tres **abertas com instrumento** (`RD-31`,
`RD-33`, `RD-34`) e uma **parcialmente tratada com o limite declarado** (`RD-36`).

> **`RD-36` e o achado que esta missao mais quis fechar e nao fechou, e o registro diz por que.**
> A hipotese inicial era uma divergencia de **um** — `governance/README` declarava **`19` de `46`**
> ressalvas quando a propria soma dava **`47`**. **Medir na fonte desfez a hipotese:** o razao de
> `fitness/README` tem **31 linhas** e **28 ressalvas distintas** na tabela de abertas, **18** na
> de fechadas, e os **15 arquivos `FIT`** contem **55** linhas — **nenhum dos conjuntos reconcilia
> com os outros**. Corrigir o `46` para `47` teria produzido um numero **igualmente
> indefensavel**, e por isso **nao foi feito**: `LV-05` proibe declarar reconciliado o que nao foi
> reconciliado. **A cascata devida foi executada e o defeito ficou registrado com dono e gatilho** —
> a reconciliacao integral e **auditoria propria**.

## 10. O que deliberadamente **nao** foi feito

| Nao feito | Norma que o impede | Consequencia assumida |
|---|---|---|
| **As duas Specs piloto** | `FND-04 §6` *("Produto existe")* · `FND-03 §3.6` · `FND-10 §4.4` | **`RD-33` aberto e bloqueante** — §6. **Entregavel 9 parcial** |
| Criar `products/` ou Carta de Produto | `FND-04 §6` — **C2 · Tipo 1 do SOBERANO**; restricao expressa da missao | Idem |
| Emendar `FND-03`, `FND-04` ou `FND-10` para ampliar a Spec | **C3**; `RD-27` veda `FND-10`; nao foi pedido | `RD-33`, saida `S2` |
| Corrigir a Carta de `DEP-PRD` e a de `DEP-EXE` | `FND-09 §8.2`, linha `DEP` — aprova e **ratifica o SOBERANO** | **`RD-31` aberto**; ressalva `R3` |
| Acrescentar os campos de contrato a `FND-01` e `FND-02` | `IR-01`, `IR-03`, `IR-05` — alteraria `H-N` de objeto promulgado | **`RD-27` mantido** |
| Corrigir `FND-10 §8.5` | Idem | Item (c) de `RD-27` |
| Corrigir `aprovador: SOBERANO` em `TPL-spec` | **19 de 19** declaram o mesmo — corrigir um cria defeito novo | **`RD-34` aberto**, com leitura alternativa |
| Editar §10.0 a §10.5 do catalogo | **`BL-02`** — baseline nunca e editada | `RD-24` e `RD-30` mantidos |
| Criar `FND-11` | **C3** + emenda a `FND-01 §10`; *"nao criar `FND` por padrao"* | Opcao `A` de RFC-0017, **registrada** |
| Criar registro mestre proprio de Specs | `FND-04 §6.1`; **`RG-04`**, **`RG-05`** | `SF-32` — **manter nao e criar** |
| Criar `Skill`, `Tool`, `Command`, `Workflow`, `Agente`, `Produto`, `Projeto`, codigo, infraestrutura, ontologia ou migracao | Restricao expressa da missao; cada um tem rito proprio | **Nenhum foi criado** |
| Importar formato da `A4` | `FR-03`, `ADR-0007` | **0 formatos importados** — §4 |
| Estimar o custo dos 21 blocos de `SF-09` | **`CE-04`** — *"metrica sem valor observado nao entra"* | Ressalva **`R2`** de FIT-2026-015 |

## 11. Decisao

> ## **`ADJUST`**
>
> **Oito dos nove entregaveis estao completos e verificados de forma independente. O nono e
> parcial: template e registro sim, pilotos nao — e o motivo e normativo, medido e citado por
> identificador.**
>
> **As outras quatro opcoes foram avaliadas e recusadas, cada uma com fundamento:**
> **`GO-TO-SKILLS`** e prematura — o portao anterior **foi liberado e nao pode ser exercido**;
> **`READY-FOR-RATIFICATION`** nao se aplica — `ADR-0021` e **C2 · Tipo 2**, e `FND-04 §2.1`
> **nao exige ratificacao**; **`STOP`** e desproporcional — nada foi violado e nenhum artefato e
> nulo; **`BLOCKED`** e incorreta — a **pre-condicao nao falhou**, e o bloqueio e **do entregavel
> 9, nao da missao**. Avaliacao independente em
> [FIT-2026-015](fitness/FIT-2026-015-framework-de-specifications.md).
>
> **O ajuste devido nao e desta missao: e um ato.** O SOBERANO escolhe entre **`S1`** e **`S2`** —
> disjuntas —, e **nenhum Departamento pode suprir a escolha**: tentar seria `LV-06` ou `LV-07`.
>
> **Nenhuma Spec deve ser criada antes dessa escolha.** Criar uma agora produziria artefato
> **nulo** (`MT-01`, `AC-06`) e incidente de conformidade (`LV-11`).

### 11.1 Pendencias para o SOBERANO — **cinco, e uma bloqueia**

| # | Materia | Instrumento | Bloqueia? |
|---|---|---|---|
| **1** | **`S1` ou `S2`** — qual via desbloqueia a `Spec` | **C2 · Tipo 1** *(criar Produto)* **ou** **C3** *(ampliar `Spec`)* | ✅ **SIM** |
| 2 | **`RD-31`** — emendar as Cartas de `DEP-PRD` *(8 afirmacoes)* e `DEP-EXE` *(declarar `QG-1`)* | RFC + ADR + diff + pacote + ato | ⚠️ **Recomendado antes da 1a Spec** |
| 3 | **`RD-27`** — backfill em `FND-01`, `FND-02` e `FND-10 §8.5` | Idem. **Inalterada** | ❌ |
| 4 | **A classe de `ADR-0021`** — se declarar o contrato de um tipo e **C3** | Manifestacao; `RFC-0017` serve de peca instrutoria **sem reescrita** | ❌ |
| 5 | **A classe de `ADR-0020`** | **Inalterada** desde FIT-2026-014 | ❌ |

**A lista cresceu de tres para cinco, e uma passou a bloquear.** Isso **nao e regressao**: e o
sinal de que o trabalho chegou ao ponto em que a norma exige uma **decisao de portfolio**, e
portfolio e materia exclusiva do Soberano (`FND-01 §7.3`).

## 12. Rastreabilidade

| Campo | Conteudo |
|---|---|
| **Pre-condicao consumida** | `GO-TO-SPECS`, **8 de 8** — [PT-2026-006 §8](relatorio-transicao-2026-07-29-fechamento-operacional.md); `ADR-0020` vigente; prova **55/55**; catalogo reconciliado; **`BL-2026-07-29-08`** reproduzida **antes** das edicoes |
| **Instrumento de origem** | [RFC-0017](../rfcs/RFC-0017-framework-de-specifications.md) → [ADR-0021](../decisions/ADR-0021-framework-de-specifications.md) |
| **Achado que fecha** | **`RD-23`** — pre-correcao obrigatoria da missao |
| **Achados que abre** | **`RD-31`** *(Alta)* · **`RD-32`** *(Media)* · **`RD-33`** *(Alta, bloqueante)* · **`RD-34`** *(Baixa)* · **`RD-35`** *(Media)* · **`RD-36`** *(Media — parcialmente tratado, com o limite declarado)* |
| **Verificacao independente e Fitness Check** | [FIT-2026-015](fitness/FIT-2026-015-framework-de-specifications.md) — `apto-com-ressalva`, **3** ressalvas, **`C11` 13 de 13** |
| **Aprendizado** | [MEM-APR-0006](../memory/aprendizado/MEM-APR-0006-exercer-o-contador-revela-o-defeito.md) — `QG-5` |
| **Regra de integridade** | [ADR-0012](../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md), `IR-01` a `IR-12` |
| **Evidencia externa** | `_SAIDA-COMPANY-OS/09_PACOTE-DE-INTEGRACAO/` — **`external-evidence`, provisoria, nao normativa, nao adotada**; **236 de 33.676 linhas lidas**; **0 formatos importados** |
| **Baseline conferida antes das edicoes** | **`BL-2026-07-29-08`** — reproduzida **tres vezes**, **nao editada** (`BL-02`) |
| **Baseline emitida** | **`BL-2026-07-29-09`** — [catalogo §10](artifact-registry.md) |
| **Copia datada** | **542** arquivos em `_backups/LucaX-Enterprise-OS_2026-07-29_pre-missao-1-13/` (`PI-07`, `AF-35`), **reconferida na copia** |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-PRD | Relatorio da **Missao 1.13 — Framework de Specifications**. **`SF-01` a `SF-32` instituidos** dentro de [ADR-0021](../decisions/ADR-0021-framework-de-specifications.md), `C2 · Tipo 2`, na forma de `ADR-0012`, `ADR-0015` e `ADR-0020`, com **`0` arquivos de `foundation/` alterados** *(por `cmp`)* e **`0` entidades, tipos documentais, portoes, papeis, classes ou verbos de autoridade criados**. Cobre os **oito** primeiros entregaveis integralmente: contrato de **21 blocos**, semantica de **3** verbos com **6** campos por requisito e **6** naturezas de enunciado, **7** perfis que **nao viram tipo**, matriz de **50 celulas** `C0`–`C3` × `Tipo 1/2` como projecao declarada, cadeia de **9** elos e **6** relacoes com **`conflita` declarada achado e nao aresta**, **DoR de 9** e **DoD de 10**, regime de mudanca e economia de contexto com **requisito enderecavel por `RQ-nn`**. **`RD-23` FECHADA, e maior do que estava declarada:** o achado citava **2** defeitos em `TPL-spec` e a medicao campo a campo encontrou **5**, os cinco corrigidos em **1.1.0** — `cabaa58e…f748` · 132 linhas → `afd0dc7e…370f` · 272 linhas, `LF` preservado, **0 bytes `CR`** —, com diff **literal e reversivel**. **Testado em doze casos: onze deterministicos e coerentes, e um deterministico e DIVERGENTE** — `T-12`, *"quem libera `QG-1`"* lido nas Cartas devolve `DEP-PRD` onde a fonte diz `DEP-EXE` —, **e a divergencia virou achado em vez de ser contornada**. **As duas Specs piloto NAO foram criadas, e a razao e norma, nao escolha:** `FND-04 §6` exige *"Produto existe"*, `FND-03 §3.6` e `FND-10 §4.4` as alojam em `products/<slug>/specs/`, e mediram-se **`0` Specs, `0` Produtos e `products/` ausente**; **as duas saidas faceis eram violacao** e foram recusadas com norma citada; as duas saidas legitimas — **`S1`** *(ato criando Produto)* e **`S2`** *(RFC C3 → ADR C3 → ato)* — sao **disjuntas**, e **cada piloto pedido depende de uma delas**. **Cinco achados novos:** **`RD-31`** *(Alta — **8** afirmacoes falsas na Carta de `DEP-PRD`, **4 nunca enumeradas**, e **`DEP-EXE` nao declara `QG-1` em nenhuma linha**: o portao da Spec **nao tem titular declarado em Carta alguma**)*; **`RD-32`** *(Media — **4** contadores oficiais defasados em **8** valores, com risco de **colisao de identificador**, encontrados **por exercer o contador**; **segunda ocorrencia**, e a causa foi **codificada em `SF-32`**)*; **`RD-33`** *(Alta e **bloqueante** — o vinculo `Spec × Produto`)*; **`RD-34`** *(Baixa — **19 de 19** `TPL` declaram `aprovador: SOBERANO`, e **corrigir um criaria defeito novo**)*; **`RD-35`** *(Media — **3** agregados de indice divergentes, corrigidos na projecao)*. Evidencia externa `A4` **avaliada e nao adotada**: **236 de 33.676 linhas — 0,70%**, **0 formatos importados**, e **duas praticas `LV4` recusadas com norma citada**. Custo de contexto: **nona medicao da serie — 3.578 linhas de acervo · 7,72%**, **+41,9%** sobre a Missao 1.12.1, com a comparabilidade declarada **como desfavoravel** e a razao medida. **`RC-02` atendida por construcao: `DEP-GOV` nao e autor de nenhum instrumento normativo — primeira vez em quinze missoes.** **Decisao: `ADJUST`**, com as outras quatro opcoes recusadas uma a uma. **Cinco pendencias para o SOBERANO, e uma bloqueia** — a escolha entre `S1` e `S2`. Baseline **`BL-2026-07-29-09`**. |
