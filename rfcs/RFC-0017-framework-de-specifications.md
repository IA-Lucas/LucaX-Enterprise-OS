---
id: RFC-0017
titulo: Framework de Specifications — onde vive a norma da Spec, e por que os pilotos nao podem existir hoje
tipo: rfc
versao: 1.0.0
status: aprovado
camada_memoria: estrategica
autor: DEP-PRD
proprietario: DEP-PRD
aprovador: DEP-GOV
criado_em: 2026-07-29
atualizado_em: 2026-07-29
revisao_prevista: null
decisoes_relacionadas: [ADR-0021]
substitui: []
substituido_por: null
classe_mudanca: C2
prazo_analise: 2026-07-29
resumo: Propoe instituir o Framework de Specifications dentro de um ADR C2, corrigir TPL-spec por RD-23 e declarar que a Spec e vinculada a Produto em tres fontes vigentes, o que impede criar Spec piloto sem ato do Soberano.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# RFC-0017: Framework de Specifications

## Proposito

Propor **onde** a norma da `Spec` deve viver e **com que instrumento** ela se institui, corrigir
o achado **`RD-23`** no `TPL-spec` pelo rito aplicavel, e submeter a decisao um fato que a
medicao desta missao encontrou: **a `Spec` esta vinculada a `Produto` em tres fontes vigentes**,
e por isso **nenhuma Spec pode ser criada** — piloto inclusive — sem ato do Soberano.

## Escopo

| Item | Definicao |
|---|---|
| **Inclui** | O instrumento e a sede da norma da `Spec`; o **Spec Contract**; a semantica normativa; os perfis; o mapeamento autoridade × ciclo; a rastreabilidade; DoR e DoD; o regime de mudanca; a economia de contexto; a correcao de **`RD-23`** em `TPL-spec`; a questao **Spec × Produto** |
| **Nao** inclui | Criar `Skill`, `Tool`, `Command`, `Workflow`, `Agente`, `Produto`, `Projeto`, codigo, infraestrutura, ontologia ou migracao; emendar `FND-01`, `FND-02` ou `FND-10` *(`RD-27`)*; editar baseline historica *(`RD-28`, `BL-02`)*; criar `FND` novo; reabrir o merito de `ADR-0018`, `ADR-0019` ou `ADR-0020` |
| **Subordinado a** | [FND-01](../foundation/01-constituicao.md) · [FND-03](../foundation/03-taxonomia.md) · [FND-04](../foundation/04-governanca.md) · [FND-07](../foundation/07-framework-decisoes.md) · [FND-09](../foundation/09-meta-model.md) · [FND-10](../foundation/10-artifact-framework.md) |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| **Propoe / autor** | **DEP-PRD** | [FND-09 §8.2](../foundation/09-meta-model.md), linha `SPC` — *propoe/cria*; [DEP-PRD §3](../departments/prd/carta.md) `P-4` *(Specs e requisitos)*, autonomia **A2** |
| **Areas que devem se manifestar** | **DEP-ENG** e **DEP-QAR** | FND-09 §8.2, linha `SPC` — *revisa*; `I-2` de DEP-PRD *(autor nao revisa a propria Spec)* |
| **Valida a forma** | **DEP-GOV** | FND-09 §8.2, linha `RFC` |
| **Revisa** | **DEP-QAR** | `AC-03`, `RM-06b`, `ADR-0005` — **revisor ≠ autor** |
| Decide | ver **[ADR-0021](../decisions/ADR-0021-framework-de-specifications.md)** | FND-07 §2.4 |
| **Prazo de manifestacao** | **2026-07-29**, na propria missao | Missao 1.13 |

> **Residuo declarado (`PI-10`), e ele e o oposto do de costume.** Esta RFC **nao e de DEP-GOV**:
> autoria e de **DEP-PRD**, revisao de **DEP-QAR**, validacao de forma de **DEP-GOV** e decisao
> de **DEP-EXE**. E a **primeira peca instrutoria do acervo que nao tem DEP-GOV como autor**, e
> e a resposta direta a exigencia **`RC-02`** da missao. O residuo remanescente e menor e esta
> dito: **DEP-GOV valida a forma do documento que declara defeito em artefato de DEP-GOV**
> *(os contadores oficiais, §3.5)*.

---

## 1. Situacao atual

**O portao foi liberado, e a materia esta madura.** `GO-TO-SPECS` decorre das **8 de 8**
condicoes de §X do sexto ato soberano, apuradas em
[PT-2026-006 §8](../governance/relatorio-transicao-2026-07-29-fechamento-operacional.md) e
verificadas de forma independente em
[FIT-2026-014](../governance/fitness/FIT-2026-014-regime-ministerial-e-cobertura-de-contexto.md).
A baseline **`BL-2026-07-29-08`** reproduziu **nos 64 digitos** antes de qualquer escrita desta
missao — **164 artefatos · 46.353 linhas · `8cf2143c…b027a7f`**.

**A autoridade sobre a Spec ficou determinada por tres decisoes consecutivas:**

| Decisao | O que fixou | Estado |
|---|---|---|
| [ADR-0018](../decisions/ADR-0018-liberacao-do-portao-qg-1.md) | **`QG-1` e liberado por `DEP-EXE`**, nao por quem produz a Spec | `ativo` · **ratificada** |
| [ADR-0019](../decisions/ADR-0019-aprovador-e-ratificador-de-spec.md) | **Aprovacao de Spec segue a classe** (`FND-04 §2`); **ratifica o SOBERANO se C3 ou Tipo 1** | `ativo` · **ratificada** |
| [ADR-0020](../decisions/ADR-0020-regime-ministerial-de-promulgacao-e-ativacao.md) | Promulgar e ativar sao **ministeriais**; `PA-01` a `PA-14` | `ativo` · `nao-exigida` |

**E o que ainda nao existe:** nenhuma `Spec`, nenhum `Produto`, nenhum `Projeto`. O acervo tem
**oito diretorios na raiz**, e `products/` **nao esta entre eles** — medido nesta missao.
`KP-3` e `KP-4` da [Carta de DEP-PRD](../departments/prd/carta.md) declaram, na fonte,
**`0` produtos** *("proibido nesta fase, por determinacao")* e **`0` Specs emitidas**.

## 2. Problema

**Sao tres problemas distintos, e so o primeiro era conhecido.**

### 2.1 `RD-23` — o esqueleto do template contradiz a norma vigente

Medido no arquivo, linha a linha:

| Local em [`TPL-spec`](../foundation/templates/TPL-spec.md) | Texto atual | Norma vigente que ele contradiz |
|---|---|---|
| Esqueleto, `aprovador:` | **`DEP-PRD`** | `FND-09 §8.2`, linha `SPC`: **`conforme classe (FND-04 §2)`** |
| Esqueleto | **campo `ratificacao` ausente** | `FND-09 §8.2`: **`SOBERANO se C3 ou Tipo 1`**; `FND-10 §5.4` `LM-02` |
| Esqueleto | **`resumo`, `perfil_contexto`, `confidencialidade`, `revisor` ausentes** | `FND-10 §2.2` — obrigatorios em artefato **criado** a partir da vigencia; `AC-06` |
| §11, *"Liberado por"* | **`<DEP-PRD, data>`** | `FND-01 §6.2` pos-`ADR-0018`: **`QG-1` e liberado por `DEP-EXE`** |
| §Responsaveis | **sem `revisor`** | `FND-09 §8.2`, linha `SPC`: revisa **`DEP-ENG` + `DEP-QAR`** |

**`RD-23` era declarado com dois defeitos; a medicao encontra cinco.** Os tres novos sao da
mesma causa registrada em
[MEM-APR-0005](../memory/aprendizado/MEM-APR-0005-medir-a-ausencia-na-fonte-errada.md): mediu-se
**o que o achado citava**, nao **o contrato que o artefato deve cumprir**.

### 2.2 A norma da `Spec` nao tem sede

`Spec` tem **tipo documental** (`FND-10 §4.4`), **entidade** (`SPC`, `FND-09 §5`), **definicao**
(`FND-03 §3.6`), **pre-condicao** (`FND-04 §6`), **autoridade** (`FND-09 §8.2`) e **template**.
**Nao tem o que os demais dominios estruturados tem:** contrato proprio, semantica normativa de
requisito, DoR/DoD, regime de mudanca e regra de economia de contexto. Hoje isso vive **em
nenhum lugar**, e a consequencia foi medida: `RD-14`, `RD-15`, `RD-18` e `RD-23` — **quatro
achados em quatro missoes, todos sobre Spec, todos por ausencia de sede**.

### 2.3 A `Spec` esta vinculada a `Produto` em tres fontes vigentes

**Este e o problema que esta missao descobriu, e ele e estrutural.**

| Fonte vigente | Texto literal | Consequencia |
|---|---|---|
| **`FND-03 §3.6`** | *"Vive em `products/<slug>/specs/<SPC-id>.md`"* | Nao ha caminho legal para uma Spec fora de um produto |
| **`FND-04 §6`**, linha *Spec* | Pre-condicao: ***"Produto existe"***; *"**Todas** precisam ser verdadeiras para a criacao ser aprovada"* | Sem produto, `O1` **nao pode ocorrer** (`FND-10 §5.2`) |
| **`FND-10 §4.4`** | Local: **`products/<slug>/specs/`** | Terceira fonte, mesmo vinculo |

E **criar produto e materia do Soberano**: `FND-04 §6`, linha *Produto* — *"Decisao do Soberano"*,
classe **C2 · Tipo 1**; `FND-09 §8.2`, linha `PRO` — aprova e ratifica **SOBERANO**;
`FND-01 §7.3` — *"Portfolio: criar/encerrar produto → Soberano"*. **`DEP-PRD` declara, na propria
Carta §4, que criar produto nao lhe compete**, e escala em **`E4`, bloqueando execucao**.

> **A missao pede duas Specs piloto — uma de baixo risco e uma interdepartamental — e proibe
> criar produtos.** As duas exigencias, somadas as tres fontes acima, **nao podem ser
> satisfeitas ao mesmo tempo**. Isto nao e opiniao: e a leitura literal de tres artefatos
> vigentes de nivel 2 da hierarquia normativa. **A Spec interdepartamental e, ainda, uma
> categoria que a norma nao preve**: nao existe Spec sem produto, logo nao existe Spec cujo
> objeto seja um processo entre departamentos.

## 3. Evidencia medida

Toda contagem abaixo foi produzida **por ferramenta, em 2026-07-29, antes das edicoes**.

| # | Evidencia | Valor | Metodo |
|---|---|---|---|
| **F1** | Baseline vigente reproduz | **164 · 46.353 · `8cf2143c…b027a7f`** | Comando publicado em [catalogo §10.5](../governance/artifact-registry.md) |
| **F2** | Diretorios na raiz do acervo | **8** — `products/` **ausente** | `ls -d */` |
| **F3** | Artefatos de tipo `SPC` no acervo | **0** | Varredura por `tipo: spec` em frontmatter |
| **F4** | Artefatos de tipo `PRO` no acervo | **0** | Varredura por `tipo: carta-produto` e por `products/` |
| **F5** | Fontes vigentes que vinculam `Spec` a `Produto` | **3** — `FND-03 §3.6`, `FND-04 §6`, `FND-10 §4.4` | Leitura literal, citada por identificador |
| **F6** | Defeitos de contrato em `TPL-spec` | **5** — §2.1 | Comparacao campo a campo contra `FND-10 §2.2` e `FND-09 §8.2` |
| **F7** | Afirmacoes da Carta de **`DEP-PRD`** que `ADR-0018` e `ADR-0019` tornaram **falsas** | **8** | Varredura de `QG-1` e de *"aprova DEP-PRD"* na Carta, conferida contra as fontes emendadas — §3.4 |
| **F8** | Contadores oficiais defasados | **4 tabelas · 8 valores** | Comparacao de cada contador contra a propria tabela que ele conta — §3.5 |
| **F9** | Templates que declaram `aprovador: SOBERANO` no proprio cabecalho | **19 de 19** | Extracao de frontmatter dos 19 `TPL` |
| **F10** | Cadeia `objetivo → Capability → Departamento → decisao → Spec` — elos que **existem hoje** | **4 de 5** — o elo `Spec` e vazio | `CAP-produto` `ativo`; `DEP-PRD` `ativo`; `ADR-0018`/`0019`/`0020` `ativo`; `SPC` **inexistente** |

### 3.4 Achado novo — a Carta de `DEP-PRD` afirma autoridade que ela nao tem mais

`ADR-0018` e `ADR-0019` foram **ratificados** e estao **em vigor**. A cascata `CV-04` para a
Carta de `DEP-PRD` foi **declarada devida** em
[PT-2026-004 §3.1](../governance/relatorio-transicao-2026-07-29-ratificacao.md), com **quatro**
afirmacoes enumeradas, e **nunca foi executada** — a Carta permanece em **1.0.0**, `ativo`,
`ratificada`, byte a byte identica a `BL-2026-07-29-07`.

**A medicao desta missao encontra oito, e nao quatro:**

| # | Local | Afirmacao hoje **falsa** | Fonte que a refuta |
|---|---|---|---|
| 1 | `§3`, `P-8` | *"**Portao QG-1**"* listado em **"o que possuo — escopo exclusivo"** | `FND-01 §6.2`: libera **DEP-EXE** |
| 2 | `§5`, L135 | *"Liberacao de **QG-1** \| A2 \| — \| FND-01 §6.2"* | idem — e a fonte citada diz o contrario da citacao |
| 3 | `§5`, L136 | *"**Aprovar Spec** … FND-09 §8.2, linha `SPC`: aprova DEP-PRD (QG-1)"* | `FND-09 §8.2`: **`conforme classe`**. **O texto citado nao existe mais na fonte** |
| 4 | `§5.2`, L159 | `QG-1` em **"portoes sob minha responsabilidade"** | `FND-01 §6.2` |
| 5 | `§5.2`, L162 | *"**QG-1 e o unico portao que DEP-PRD libera sozinho**"* | idem |
| 6 | `§7`, L211 | *"Spec \| `SPC` \| **Autor e aprovador** *(QG-1)*"* | `FND-09 §8.2` + `FND-01 §6.2` |
| 7 | `§10.1`, `RP-1` | *"DEP-PRD e o **unico liberador do proprio portao**"* — o risco **e a mitigacao** | O risco **deixou de existir** por `ADR-0018`; a mitigacao descreve mundo extinto |
| 8 | `§12.3`, L382 | *"**Portao QG-1** \| Destino explicito obrigatorio"* — trata o portao como **custodia de DEP-PRD** transferivel na extincao | `FND-01 §6.2` |

**Quatro das oito nunca foram enumeradas** — 1, 4, 7 e 8. A causa e a **mesma de `RD-23`**: a
medicao do *"conjunto estreito"* procurou **a frase que ficaria falsa** e nao **o papel que
mudou de titular**. `§5.1` da mesma Carta — *"o que **nao** decido"* — **nao lista** a liberacao
de `QG-1`, e deveria.

**Consequencia verificavel, e ela e a razao pela qual isto entra nesta RFC:** um consumidor que
resolva *"quem libera `QG-1`"* lendo **Cartas** obtem **`DEP-PRD`**; lendo **`FND-01 §6.2`**
obtem **`DEP-EXE`**. `DEP-EXE` **nao declara `QG-1` em nenhuma linha da propria Carta** — medido:
**0 ocorrencias**. **O portao da Spec nao tem titular declarado em Carta alguma.**

### 3.5 Achado novo — quatro contadores oficiais estao defasados

`FND-03 §2.3` atribui a `DEP-GOV` o **contador oficial** de cada sequencia, e `RG-04` declara os
indices por diretorio como *"contadores oficiais de sequencia"*. **Cada um deles conta menos do
que a propria tabela abaixo dele lista:**

| Indice | Contador declara | A tabela do mesmo arquivo lista ate | Defasagem |
|---|---|---|---|
| [`decisions/README`](../decisions/README.md) | ultimo **`0019`** · proximo **`0020`** | **`ADR-0020`** | **1** |
| [`rfcs/README`](README.md) | ultimo **`0015`** · proximo **`0016`** | **`RFC-0016`** | **1** |
| [`governance/fitness/README`](../governance/fitness/README.md) | ultimo **`013`** · proximo **`014`** | **`FIT-2026-014`** | **1** |
| [`governance/README`](../governance/README.md) | `FIT` ultimo **`013`** · proximo **`014`** | **`FIT-2026-014`** | **1** |

**8 valores em 4 tabelas.** O risco nao e cosmetico: **quem confiar no contador cria
`ADR-0020`, que ja existe** — colisao de identificador, contra a regra literal de `FND-03 §2.3`
*("numero nunca e reaproveitado")*. **Este defeito foi encontrado por exercer o contador**, ao
pedir o numero desta RFC.

> **O que foi varrido, declarado — a licao de [MEM-APR-0005](../memory/aprendizado/MEM-APR-0005-medir-a-ausencia-na-fonte-errada.md).**
> A varredura cobriu **9 sequencias em 7 indices**: `ADR`, `RFC`, `FIT` *(em `fitness/README` e
> em `governance/README`)*, `EXC`, `INC`, `MEM-APR`, `MEM-EST` e `MSG`. **Quatro defasadas** —
> as quatro acima — e **cinco corretas**. **O defeito nao e sistemico a todos os contadores: e
> das sequencias movimentadas pelas Missoes 1.12 e 1.12.1**, e essa delimitacao e o que impede
> que o achado afirme mais do que mediu.

> **E a segunda ocorrencia registrada da mesma familia.** `governance/README` **documenta a
> primeira**, em nota propria: ate 2026-07-28 declarava `FIT-2026-001` como ultimo atribuido,
> *"um numero atras do real desde a Missao 1.3"*, corrigida como achado `C11` de
> **REV-CONSOLIDACAO**. **A correcao foi aplicada ao valor e nao a causa** — e a causa e `CV-04`:
> o contador nao e remedido pela mesma mudanca que cria o artefato.

## 4. Criterios de avaliacao

Declarados **antes** das opcoes.

| # | Criterio | Peso | Como se mede |
|---|---|---|---|
| **K1** | **Nao criar entidade, tipo, portao, papel nem autoridade** | **Alto** | Contagem antes/depois em `FND-09 §5`, `§8.1`, `FND-01 §6.2` |
| **K2** | **Nao emendar fonte fundacional** — a missao veda `FND-01`, `FND-02` e `FND-10` (`RD-27`), e nao pediu emendar as demais | **Alto** | `cmp` de cada arquivo de `foundation/` contra a copia datada |
| **K3** | **Menor instrumento competente** | **Alto** | `FND-04 §2` item a item; `FND-09 §11.2` |
| **K4** | **Determinismo** — toda regra da Spec resolvida por fonte citada por identificador, sem interpretacao informal | **Alto** | Bateria de casos, resposta por regra citada |
| **K5** | **Nao presumir aprovacao, ratificacao nem existencia de produto** | **Alto** | `LM-02` a `LM-06`; `LV-05` |
| **K6** | **Autoria, teste e avaliacao nao concentrados em DEP-GOV** (`RC-02`) | **Alto** | Departamento por artefato produzido |
| **K7** | **Reversibilidade** | Medio | `GV-03`, `RB-01` |
| **K8** | **Nao proliferar registro** — um template, um registro mestre | Medio | `FND-04 §6.1`; `RG-04`, `RG-05` |

## 5. Opcoes

### Opcao A — **`FND-11`: um documento fundacional proprio para Specifications**

| Campo | Conteudo |
|---|---|
| Descricao | Framework de Specifications como decimo primeiro documento de `foundation/`, no nivel 2 da hierarquia |
| A favor | E a forma que `FND-08`, `FND-09` e `FND-10` usaram para os dominios equivalentes. Sede propria, evolucao por versao (`M2`) |
| **Contra** | **Falha `K2` e `K3`.** Criar `FND` e **C3**: exige RFC → ADR → **ratificacao indelegavel** e emenda a `FND-01 §10` *(hierarquia normativa)* — que a missao veda tocar. A missao diz ainda *"nao criar `FND` por padrao"* |
| Custo / Risco | 1 RFC C3 + 1 ADR C3 + emenda a `FND-01` + pacote soberano + ato. **Nao executavel nesta missao** |
| Quem e afetado | Todos os papeis — o nivel 2 e nucleo de leitura |

### Opcao B — **Uma secao nova dentro de `FND-10`**

| Campo | Conteudo |
|---|---|
| Descricao | A norma da Spec como capitulo do Artifact Framework, onde o tipo documental ja vive |
| A favor | Nenhuma sede nova; proximidade tematica maxima |
| **Contra** | **Falha `K2` de forma direta e nao negociavel.** A pre-correcao `RD-27` da missao determina *"nao alterar `FND-01`, `FND-02` ou `FND-10`"*, e `RD-27` registra que **acrescentar linha a `FND-10` altera `H-N`** de documento promulgado pelo sexto ato — `IR-05`: *"nao corrigivel por edicao: exige ato novo"* |
| Custo / Risco | Ato soberano. **Vedado pela propria missao** |
| Quem e afetado | `FND-10` e os quatro objetos do sexto ato |

### Opcao C — **`ADR` C2 · Tipo 2, com as regras dentro do proprio ADR** *(recomendada)*

| Campo | Conteudo |
|---|---|
| Descricao | Regras `SF-01` a `SF-nn` **dentro do ADR**, na forma que `ADR-0012` *(`IR-01` a `IR-12`)*, `ADR-0015` *(`FT-10` a `FT-14`)* e `ADR-0020` *(`PA-01` a `PA-14`)* **ja usaram**. Matrizes como **projecao declarada** (`PJ-02`). `TPL-spec` corrigido no mesmo rito. **Registro mestre: o catalogo que ja existe** |
| A favor | Satisfaz `K1` a `K8`. **Zero** arquivos de `foundation/` tocados — logo zero `H-N` alterados. **Forma com tres precedentes medidos no acervo.** Reversivel por superacao (`O6`) |
| **Contra** | As regras vivem em artefato **`M1`**: **nao se emendam**, superam-se. **Tradeoff aceito** — e o mesmo regime de `IR-*`, `FT-*` e `PA-*` |
| Custo / Risco | 1 RFC + 1 ADR + 1 `FIT` + 1 `TPL` corrigido + indices `M3`. Risco: a classe **C2** ser contestada |
| Quem e afetado | `DEP-PRD` *(autor de Spec)* · `DEP-ENG` e `DEP-QAR` *(revisores)* · `DEP-EXE` *(aprova e libera `QG-1`)* · `DEP-GOV` *(forma e registro)* |

### Opcao D — **Criar os dois pilotos primeiro, e derivar a norma deles**

| Campo | Conteudo |
|---|---|
| Descricao | Escrever as duas Specs piloto e extrair o framework da pratica |
| **Contra** | **Impossivel por norma, nao por preferencia.** `FND-04 §6` exige *"Produto existe"* e **nao existe produto**; `FND-03 §3.6` e `FND-10 §4.4` nao dao caminho fora de `products/<slug>/specs/`. Criar o produto e **C2 · Tipo 1 do SOBERANO**, e a missao proibe criar produto. Falha `K1` e `K5` |
| Custo / Risco | Uma Spec criada assim seria **nula** por `MT-01`/`AC-06` e abriria incidente (`LV-11`) |

### Opcao E — **Ampliar `Spec` para materia nao-produto, por emenda a `FND-03`, `FND-04` e `FND-10`**

| Campo | Conteudo |
|---|---|
| Descricao | Permitir Spec cujo objeto seja capability, processo interdepartamental ou componente interno — o que a missao chama de *"Spec interdepartamental"* |
| A favor | **E a unica via que torna o piloto interdepartamental possivel.** Ha demanda declarada: a propria missao a pediu |
| **Contra** | **Falha `K2` e `K3` hoje.** Altera **tres** fontes de nivel 2, uma delas `FND-10` — vedada por `RD-27`. Classe **C3** *(muda fronteira de tipo documental e a arvore canonica de `FND-03 §7`)*, com ratificacao indelegavel |
| Custo / Risco | 1 RFC C3 + 1 ADR C3 + diff de 3 fontes + pacote soberano + ato. **Materia do Soberano** |
| Quem e afetado | `DEP-PRD`, `DEP-ENG`, `DEP-QAR`, `DEP-EXE` e todo consumidor futuro de Spec |

### Opcao Z — **Nao fazer nada**

| Campo | Conteudo |
|---|---|
| Consequencia de manter o estado atual | `RD-23` permanece **aberto**, e ele e **pre-correcao obrigatoria e nao negociavel** antes da primeira Spec — logo a primeira Spec fica bloqueada por defeito de template **e** por ausencia de produto. Os oito defeitos da Carta de `DEP-PRD` e os oito valores de contador seguem **nao registrados** |
| Custo da inacao | O `GO-TO-SPECS` liberado **nao produz efeito**: nenhuma Spec e criavel, e a razao **nao esta escrita em nenhum lugar**. A quinta missao consecutiva encontraria o mesmo achado sobre Spec |

## 6. Recomendacao do proponente

**Recomendo a Opcao C, e recomendo que ela seja acompanhada de duas declaracoes explicitas.**

**Por que C.** E a **unica** opcao que institui a norma **sem tocar fonte fundacional** — e
`K2` nao e preferencia desta RFC: e determinacao da missao, ancorada em `IR-05`. E a forma tem
**tres precedentes medidos** no proprio acervo, o mais recente com **doze casos de determinismo
provados**. As alternativas A, B e E sao **melhores em sede** e **inexecutaveis sem ato**; D e
**nula por norma**; Z **congela um portao aberto**.

**Primeira declaracao: os pilotos nao sao adiados por conveniencia — sao impossiveis hoje.** O
ADR deve dizer, com as tres fontes citadas por identificador, que **nenhuma Spec e criavel** e
que a missao **nao criou nenhuma**. Escrever uma Spec piloto em qualquer outro diretorio seria
`LV-05` *(reportar como feito o que a norma nao permite)* e `MT-01` *(artefato fora do tipo
declarado)*.

**Segunda declaracao: as duas saidas existem, sao disjuntas e sao ambas do Soberano.**

| Saida | Instrumento | O que habilita | Custo declarado |
|---|---|---|---|
| **S1** | Ato soberano que **crie o primeiro Produto** *(C2 · Tipo 1, `FND-04 §6`)* | A Spec **de baixo risco** — a de produto, que a norma ja preve integralmente | 1 Carta de Produto + 1 ADR + ratificacao |
| **S2** | **RFC C3 → ADR C3 → ato**, ampliando `Spec` a materia nao-produto | A Spec **interdepartamental** — a que a norma **nao preve** | 1 RFC + 1 ADR + diff de **3** fontes + pacote + ato |

**S1 e S2 nao se substituem.** `S1` sozinha nao habilita o piloto interdepartamental; `S2`
sozinha nao cria produto. **A missao pediu um piloto de cada tipo, e cada um depende de uma
saida diferente.**

**Recomendo, por fim, que a Opcao E seja registrada como achado com dono e gatilho, e nao
descartada.** A necessidade de Spec sobre materia interdepartamental **foi manifestada pelo
proprio Soberano** no enunciado da missao; recusa-la em silencio seria esconder demanda real.

## 7. Impacto previsto

| Dimensao | Impacto |
|---|---|
| **Departamentos** | **`DEP-PRD`** — autor da norma da propria materia, pela primeira vez · **`DEP-ENG`** e **`DEP-QAR`** — revisores · **`DEP-EXE`** — aprova · **`DEP-GOV`** — forma e registro. **Nenhum ganha responsabilidade que nao tivesse** |
| **Componentes** | **Nenhum criado, alterado ou removido.** Nenhuma `Skill`, `Tool`, `Command`, `Workflow`, `Agente`, `Produto`, `Projeto`, codigo, banco, infraestrutura, ontologia ou migracao |
| **Normas afetadas** | **Zero emendas.** `FND-01`, `FND-03`, `FND-04`, `FND-09` e `FND-10` **citadas, nunca alteradas**. Um **`TPL`** corrigido *(`M2`, emenda por versao)*; indices `M3` em cascata `CV-04` |
| **Camadas de memoria** | **APR** — o aprendizado do contador exercido · **OPR** — o relatorio de transicao |
| **Ganho `PI-14` pretendido e sinal que o comprova** | **Organizacao:** a Spec passa a ter sede — **4 achados em 4 missoes** sobre Spec por ausencia de sede e o sinal observado *(`RD-14`, `RD-15`, `RD-18`, `RD-23`)*. **Reducao de contexto:** o consumidor da norma da Spec passa de **5 fontes** *(`FND-01 §6.2`, `FND-03 §3.6`, `FND-04 §2` e `§6`, `FND-09 §8.2`, `FND-10 §10.3`)* para **1 ADR + 1 template**. **Reavaliacao: 2027-01-28** |

## 8. Riscos

| # | Risco | Impacto | Mitigacao |
|---|---|---|---|
| **RS-1** | **A classe C2 ser contestada** — instituir o framework de um dominio pareceria C3 | Medio | O teste de `FND-04 §2` e feito item a item no ADR §11: **nenhum principio imutavel, linha vermelha, nivel da hierarquia ou direito de decisao e alterado**, e a prova e **`0` arquivos de `foundation/` alterados**, medido por `cmp`. A duvida fica **declarada**, e a via C3 fica indicada |
| **RS-2** | **As regras `SF-*` virarem segunda fonte de verdade** sobre autoridade | **Alto** | Toda celula de autoridade e **projecao declarada** (`PJ-02`) de `FND-04 §2` e `FND-09 §8.2`; `PJ-03` da precedencia a fonte. **O ADR nao nomeia titular que a fonte nao nomeie** |
| **RS-3** | **Um framework sem instancia envelhecer sem ser exercido** | Medio | Declarado como limite, na forma de `A1`/`A2` de `ADR-0020 §8`: as regras sao **determinadas, nao observadas**. Gatilho de revisao: **a primeira Spec real** |
| **RS-4** | **A ausencia de piloto ser lida como missao incompleta por omissao** | Medio | O ADR declara a impossibilidade **com as tres fontes citadas** e as duas saidas `S1`/`S2` com custo. `PI-10`: o limite esta escrito |
| **RS-5** | **Os oito defeitos da Carta de `DEP-PRD` seguirem abertos** e um consumidor resolver `QG-1` errado | **Alto** | Registrado como achado com **dono `DEP-EXE`** *(propoe emenda de Carta, `FND-09 §8.2` linha `DEP`)*, revisor `DEP-GOV`, aprovador e ratificador **`SOBERANO`**, gatilho *"antes da primeira Spec"*. **Nao corrigivel aqui:** emendar Carta ratificada exige ato |
| **RS-6** | **A correcao do contador mascarar a causa**, como em 2026-07-28 | Medio | `SF-*` inclui a regra de que **criar artefato de sequencia e incrementar o contador sao a mesma mudanca** (`CV-04`), e o aprendizado vai para **APR** |

## 9. Perguntas em aberto

| # | Pergunta | Quem responde |
|---|---|---|
| **Q1** | **`Spec` deve permanecer vinculada a `Produto`, ou a materia interdepartamental tambem merece Spec?** Se sim, e emenda C3 a tres fontes — Opcao E | **SOBERANO** |
| **Q2** | Qual sera o **primeiro Produto**, se `S1` for a via escolhida? | **SOBERANO** *(`FND-01 §7.3`)* |
| **Q3** | A classe desta decisao e **C2** ou **C3**? | **SOBERANO**, se contestar o teste de §11 do ADR |
| **Q4** | Os **19** templates que declaram `aprovador: SOBERANO` no proprio cabecalho registram **fato historico** *(aprovacao pelo ato que adotou a Fundacao)* ou **contradizem** `FND-09 §8.2` linha `TPL` *(aprova `DEP-GOV`)*? | **DEP-GOV**, com parecer de `DEP-QAR` |

**Nenhuma das quatro bloqueia esta RFC.** `Q1` e `Q2` bloqueiam **os pilotos**, e isso esta dito.

## 10. Manifestacoes

| Area | Posicao | Fundamento | Data |
|---|---|---|---|
| **DEP-PRD** | **propoe** | Materia propria — `P-4`, `P-5`, `P-9` da Carta; autonomia **A2** | 2026-07-29 |
| **DEP-ENG** | **apoia** | `FND-09 §8.2`, linha `SPC` — revisor. A Spec e a **entrada** de `DEP-ENG` *(§6.1 da Carta)*, e hoje ela **nao tem contrato**: `HO-02` e `HO-04` dependem dele | 2026-07-29 |
| **DEP-QAR** | **apoia com ressalva** | Revisor independente. **Ressalva:** framework sem instancia e **determinado e nao observado**; registrada em [FIT-2026-015](../governance/fitness/FIT-2026-015-framework-de-specifications.md) | 2026-07-29 |
| **DEP-GOV** | **valida a forma** | `FND-09 §8.2`, linha `RFC`. **Nao e autor e nao aprova o merito** | 2026-07-29 |
| **DEP-EXE** | **decide** | `FND-04 §2`, C2; `FND-07 §2.4` | 2026-07-29 |

## 11. Resultado

| Campo | Conteudo |
|---|---|
| **Decisao** | **aceita** — Opcao **C**, com as duas declaracoes de §6 |
| **ADR gerado** | [**ADR-0021**](../decisions/ADR-0021-framework-de-specifications.md) |
| Se rejeitada, por que | — |
| Se adiada, ate quando | — |
| **Opcoes nao escolhidas que ficam registradas** | **A** e **B** *(sede melhor, inexecutavel sem ato)* · **E** *(virou achado com dono e gatilho — a demanda e real)* · **D** *(nula por norma)* |
| Data | **2026-07-29** |
| Responsavel | **DEP-PRD** *(propoe)* · **DEP-EXE** *(decide)* |

## 12. Rastreabilidade

| Campo | Conteudo |
|---|---|
| **Pre-condicao consumida** | `GO-TO-SPECS` — [PT-2026-006 §8](../governance/relatorio-transicao-2026-07-29-fechamento-operacional.md), **8 de 8**; `BL-2026-07-29-08` reproduzida |
| **Achado que fecha** | **`RD-23`** — [catalogo §7, achado 44](../governance/artifact-registry.md) |
| **Achados que abre** | **`RD-31`** *(8 afirmacoes falsas na Carta de `DEP-PRD`)* · **`RD-32`** *(4 contadores oficiais defasados)* · **`RD-33`** *(Spec vinculada a Produto impede piloto)* · **`RD-34`** *(19 `TPL` declaram `aprovador: SOBERANO`)* |
| **Achados que nao toca** | `RD-24`, `RD-27`, `RD-28` *(baseline)*, `RD-30`, `RD-10` a `RD-13`, `RD-18`, `RD-21`; familia `RC-02` |
| **Decisoes que consome** | [ADR-0018](../decisions/ADR-0018-liberacao-do-portao-qg-1.md) · [ADR-0019](../decisions/ADR-0019-aprovador-e-ratificador-de-spec.md) · [ADR-0020](../decisions/ADR-0020-regime-ministerial-de-promulgacao-e-ativacao.md) · [ADR-0012](../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md) |
| **Evidencia externa consultada** | `_SAIDA-COMPANY-OS/09_PACOTE-DE-INTEGRACAO/` — resumo executivo, pacote *Specifications* de `02_PACOTES-POR-FRAMEWORK.md` e as fichas de `AC-03-REP-010` e `AC-05-REP-001`. **`external-evidence` · autoridade nenhuma · provisoria · nao normativa · nao adotada.** Avaliada em ADR-0021 §8; **nenhum formato importado** |
| Verificacao de aptidao | [FIT-2026-015](../governance/fitness/FIT-2026-015-framework-de-specifications.md) |
| Relatorio de transicao | [PT-2026-007](../governance/relatorio-transicao-2026-07-29-specifications.md) |

---

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-PRD | **Primeira peca instrutoria do acervo cujo autor nao e `DEP-GOV`** — resposta direta a exigencia `RC-02`. Propoe instituir o **Framework de Specifications** pela **Opcao C**: regras `SF-*` **dentro de um ADR C2 · Tipo 2**, na forma de `ADR-0012`, `ADR-0015` e `ADR-0020`, com **zero** arquivos de `foundation/` tocados, e corrigir **`RD-23`** no `TPL-spec` no mesmo rito. A medicao encontrou **cinco** defeitos de contrato no template onde o achado declarava **dois**. Submete o fato estrutural que a missao descobriu: **a `Spec` esta vinculada a `Produto` em tres fontes vigentes** — `FND-03 §3.6`, `FND-04 §6` *("Produto existe")* e `FND-10 §4.4` — e **nao existe produto**, logo **nenhuma Spec piloto e criavel** sem ato do Soberano; as duas saidas `S1` *(criar Produto)* e `S2` *(ampliar Spec a materia nao-produto, C3)* sao **disjuntas** e **cada piloto pedido depende de uma delas**. Abre **quatro achados novos**: **`RD-31`** — a Carta de `DEP-PRD` tem **8** afirmacoes que `ADR-0018` e `ADR-0019` tornaram falsas, **quatro delas nunca enumeradas**, e **`DEP-EXE` nao declara `QG-1` em nenhuma linha** *(0 ocorrencias)*, de modo que **o portao da Spec nao tem titular declarado em Carta alguma**; **`RD-32`** — **4** contadores oficiais defasados em **8** valores, encontrados **por exercer o contador**, com risco real de colisao de identificador e **segunda ocorrencia** de familia cuja correcao anterior atingiu o valor e nao a causa; **`RD-33`** — o vinculo Spec × Produto; **`RD-34`** — **19 de 19** templates declaram `aprovador: SOBERANO` contra `FND-09 §8.2` linha `TPL`, com a leitura alternativa declarada. **Cinco opcoes e a opcao Z.** |
