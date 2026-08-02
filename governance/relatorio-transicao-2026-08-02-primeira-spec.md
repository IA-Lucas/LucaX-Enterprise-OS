---
id: PT-2026-017
titulo: Missao 1.13.5 — a primeira Spec do acervo, e o que o primeiro uso real revelou sobre o Framework
tipo: relatorio
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-08-02
atualizado_em: 2026-08-02
revisao_prevista: null
decisoes_relacionadas: [ADR-0031, ADR-0021, ADR-0022, ADR-0030]
substitui: []
substituido_por: null
resumo: Registra a criacao de SPC-001, a primeira Spec real do acervo, e mede regra por regra o que SF-01 a SF-32 mostraram no primeiro uso.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# PT-2026-017 — Missao 1.13.5: a primeira `Spec`

> **Registro de missao. Nao e norma, nao institui nada e nao decide nada.**

## 1. O que a missao fez

**Criou `SPC-001`, a primeira `Spec` real do LucaX Enterprise OS**, sobre a lacuna `LM-6(a)` de
`PRO-nxtrack` — materia que o **nono ato soberano** fixou *"com prioridade sobre as demais de
`LA-7`"*. Ate 2026-08-02 o acervo tinha **`0`** artefatos de tipo `spec`, e as **32** regras
`SF-01`–`SF-32` viviam sob o limite `L1` de `FND-11 §14`: *"determinadas, nao observadas"*.

| Etapa | Resultado |
|---|---|
| **Pre-condicoes** | `BL-2026-08-01-03` **reproduzida** *(218 · 64.383 · `94b85d8f…be5`)* antes de qualquer escrita · `GO-TO-SPECS` **exercivel** · `PRO-nxtrack` `ativo` · `ratificada` · lease **token 13** · escritor unico por janela de tempo · `H-A` integral de **597** arquivos · copia datada de **597** arquivos |
| **Materia** | `LM-6(a)` **remedida e reproduzida** — `0` para os seis termos, em **duas** varreduras |
| **Rito** | `RFC-0026` → `ADR-0031` → `SPC-001` → `FIT-2026-024` → este registro |
| **Classe** | **`C2 · Tipo 2`**, elevada do piso `C1` por colisao **medida** entre `SF-10` e `FND-04 §3.1` |
| **`DoR` · `DoD`** | **9 de 9** e **10 de 10**, **exercidos com o lugar da conferencia declarado** |
| **Achados novos** | **5** — `RD-91` a `RD-95`, todos com dono e gatilho. **`0` gera missao:** congelamento em vigor |
| **Limites respeitados** | `0` bytes em `FND-01`–`FND-11` · `0` bytes no repositorio do candidato · `0` bancos abertos · `0` execucoes de programa do candidato · `0` historicos editados · `0` Skill, Tool, Command, Workflow, Agente, codigo ou infraestrutura |

## 2. Pre-condicoes — conferidas, nao presumidas

| # | Pre-condicao | Como se conferiu | Resultado |
|---|---|---|---|
| 1 | **Reproduzir `BL-2026-08-01-03`** | `ferramentas/baseline.sh`, lista fechada positiva, portao de raiz e portao de split | ✅ **218 · 64.383 · `94b85d8f0daadbf70265b869b433880ba07ccdcd2c64d094d5bc37810d5d5be5`** — os tres valores |
| 2 | **`GO-TO-SPECS` exercivel** | `artifact-registry §2`, linha *Estado do portao*; `PT-2026-016 §3` | ✅ **LIBERADO e EXERCIVEL** desde 2026-08-01, 8 de 8 condicoes |
| 3 | **`PRO-nxtrack` ativo e ratificado** | Frontmatter do arquivo vivo | ✅ `status: ativo` · `ratificacao: ratificada` |
| 4 | **Lease de nome proprio** | `_leases/LucaX-Enterprise-OS.lease` | ✅ **token 13**, titular **DEP-PRD / Missao 1.13.5** — e o **primeiro** lease do acervo cujo titular nao e DEP-GOV |
| 5 | **Escritor unico por janela de tempo** | Ultima escrita no acervo: **2026-08-01 23:35:26.342** *(saidas da 1.13.4.6)*; aquisicao do lease: **23:57** | ✅ **`0`** escritas de qualquer extensao na janela |
| 6 | **Ponto de partida por `H-A`** | `sha256` de **597** arquivos | ✅ manifesto com `sha256` = `9f2923fa32e257631f4d2dda33d7611c07abfbd0e7bef4ae104d700b4ec22684` |
| 7 | **Copia datada** | `_backups/LucaX-Enterprise-OS_2026-08-01_pre-missao-1-13-5` | ✅ **597** arquivos, **antes** da primeira escrita (`PI-07`, `LV-01`) |

## 3. A materia — medida, e a medicao quase falhou em silencio

**O `tree` da subpasta do candidato reproduz nos 40 digitos** o valor ancorado na Carta:
`b9b36be9324ae2d36ddc4149049ebbff9f40fb4b`. O repositorio **nao mudou** no que e rastreado — e a
medicao foi refeita assim mesmo.

> **O primeiro resultado foi `0` para os 21 termos, inclusive para `senha_hash`** — que a Carta
> declara existir. **Zero de instrumento quebrado nao e medicao de ausencia.** A causa foi
> medida *(a lista de caminhos era relativa, e o diretorio de trabalho volta ao acervo entre
> chamadas)*, e so depois de um **controle positivo** passar — `senha_hash` = **11**, `nxtrack` =
> **527** — as contagens foram tomadas. **Sem o controle, esta missao teria publicado `LM-6(a)`
> reproduzida por um instrumento que nao lia arquivo nenhum.**

| Medicao | Rastreados (183) | Arvore de trabalho (262) |
|---|---|---|
| `LGPD` · `GDPR` · `ANPD` · *"dados pessoais"* · *"politica de privacidade"* · *"termos de uso"* | **`0` para os seis** | **`0` para os seis** |

O padrao usado e **mais largo** que o publicado — admite singular e forma acentuada — e ainda
assim devolve `0`. **A lacuna e maior ou igual a declarada, nunca menor.**

### 3.1 O que a varredura **estendida** achou, e que muda a Spec

A varredura de **21 termos correlatos** — que **nao** estava na medicao original — existe para
uma so finalidade: impedir que a `Spec` exija o que ja existe (`FND-04 §6.1`, pergunta 1).

| Achado | Consequencia |
|---|---|
| **`spec-tecnica-v1.md §24` — *"Privacidade e Seguranca"* — EXISTE**, com **oito regras** numa unica frase, inclusive *"permitir exclusao de conta/dados"* e *"oferecer opt-out de treinamento"* | **`LM-6(a)` nao e ausencia de intencao: e ausencia de obrigacao verificavel.** `RQ-3` e `RQ-4` **partem** do que o candidato ja escreveu |
| **`DPO` = 13 ocorrencias → `0`** com fronteira de palavra | Falso positivo integral: `B2_EN**DPO**INT`, `Threa**dPo**olExecutor`, `backgroun**dPo**sition` |
| **`retencao` = 11, todas de backup**, `0` de titular | `RQ-8` nasce dessa distincao |
| **`feedback_recomendacao` nao tem coluna de usuario** | `RQ-2` nasce daqui — e e o fato que o risco `R2` da Carta declarava **sem medir** |
| **`0` caminhos de exclusao de conta** em producao; `DELETE FROM usuarios` so em teste | `RQ-3` |
| **O backup carrega `hash`+`sal` de todos**, declarado pelo proprio codigo | `RQ-7` e `RQ-8` |

## 4. A classe — por que `C2`, e nao o piso `C1`

**`FND-04 §6` fixa `C1` para a criacao de `Spec`, e `SF-10` chama `C1` de *piso*.** Ao montar o
quadro de papeis — e nao ao ler a matriz — apareceu isto:

| Fonte | O que diz | Efeito para o tipo `SPC` |
|---|---|---|
| `SF-10 §5`, coluna **`C1 · T2`** | *Proposta* = proprietario · *Aprovacao* = **proprietario + revisor** | Para `SPC`, `FND-09 §8.2` poe **DEP-PRD** como quem **propoe/cria** e quem **aposenta** |
| `FND-04 §3.1` | *"`Proponente ≠ Aprovador` (PI-05)"* · *"Acumulo indevido de papeis torna a aprovacao **nula** (`LV-03`)"* | **Proponente = Aprovador ⇒ aprovacao NULA** |

**`C2` e o menor valor da matriz de `SF-10` em que a colisao desaparece.** A elevacao aplica
`FND-01 §7.1.6` — *na duvida, a mais restritiva* — a uma duvida **com fundamento citado e
reproduzivel por terceiro**, nunca como cautela generica.

**Conferencia das quatro incompatibilidades absolutas, em `C2 · T2`:** `DEP-PRD ≠ DEP-EXE` ✅ ·
`DEP-PRD ≠ DEP-ENG/DEP-QAR` ✅ · `DEP-GOV ≠ DEP-PRD` ✅ · `DEP-ENG/DEP-OPS ≠ DEP-QAR` ✅.

**Consequencia do `C2`, assumida:** `RFC → ADR` (`FND-04 §2`) e **`FIT`** (`SF-24`, item 9).
**Cinco** artefatos onde a leitura literal previa **dois**. `ADR-0031 §5` declara a elevacao
**restrita a esta criacao**: o piso `C1` continua valendo para as demais `Spec`s.

## 5. O que a `Spec` faz, em quatro linhas

Declara **10 requisitos** sobre o dado pessoal que o nXtrack **ja guarda** — inventario *(`RQ-1`,
`RQ-10`)*, atribuicao ao titular *(`RQ-2`)*, exclusao *(`RQ-3`, `RQ-7`)*, informacao antes da
coleta *(`RQ-4`)* e limite de saida *(`RQ-5`, `RQ-6`, `RQ-8`)*, com verificacao independente
*(`RQ-9`)*. **`0`** requisitos afirmam enquadramento legal; **`0`** autorizam exposicao — `RQ-5` e
`RQ-6` **restringem**, e `EX-1` declara que satisfazer a `Spec` **nao autoriza publicar**, porque
a exposicao de dado vivo e materia do **SOBERANO** (`FND-01 §7.3`). **`LM-6(b)`** — direito
autoral de catalogo musical — esta **declarado fora**, em `EX-2`.

---

## 6. AVALIACAO DO FRAMEWORK — o entregavel que so a primeira `Spec` produz

> **Gatilho de revisao de `FND-11 §15`, disparado.** A fonte declara: *"A primeira `Spec` real —
> **o unico evento que transforma `SF-*` de determinado em observado** (`L1`)"*. Esta secao e a
> medicao desse evento. **Ela nao emenda nada:** `FND-11` e `M2` e so vigora com ratificacao do
> SOBERANO (`LM-02`).

### 6.1 Regra por regra — as 32

| # | Estado | Como foi exercida, ou por que nao foi |
|---|---|---|
| `SF-01` | ✅ **EXERCIDA** | A `Spec` declara *o que deve ser verdadeiro, sob que condicao e por qual evidencia*. **`0`** definicoes de *como* |
| `SF-02` | ✅ **EXERCIDA** | A decisao foi empurrada para `ADR-0031`; `EX-4` declara implementacao fora. **A regra funcionou como filtro**: `RQ-2` chegou a ser redigido como *"acrescentar coluna de usuario"* e foi **reescrito** |
| `SF-03` | ✅ **EXERCIDA** | Autoridade **derivada** no Bloco 5, com a fonte de cada variavel. `EX-1` recusa criar autoridade sobre exposicao |
| `SF-04` | ✅ **EXERCIDA** | **5** consumidores nomeados; necessidade demonstrada por `PB-1`/`PB-2` |
| `SF-05` | ✅ **EXERCIDA** | 15 + 5 campos, **`0`** novos criados pela `Spec` |
| `SF-06` | ⚠️ **EXERCIDA, E INSUFICIENTE** | Ver **6.2, `RD-93`** — o template canonico carrega **3** campos condicionais que nem `FND-03 §4.1` nem `SF-06` preveem para `Spec` |
| `SF-07` | ⚠️ **EXERCIDA, E INSUFICIENTE** | Uma `Capability` e um custodiante, escolhidos com fundamento. Ver **6.2, `RD-94`** — *"exatamente uma"* forca escolha que a materia nao respeita |
| `SF-08` | ✅ **EXERCIDA** | **7** exclusoes, cada uma com *por que* e *quando poderia entrar* |
| `SF-09` | ✅ **EXERCIDA — e o custo, medido pela primeira vez** | **21 de 21** blocos. **Fecha a obrigacao de medicao do limite `L2`**: ver 6.3 |
| `SF-10` | ❌ **EXERCIDA, E DEFEITUOSA** | Ver **6.2, `RD-91`** — a coluna `C1 · T2` produz **aprovacao nula** para todo `SPC` |
| `SF-11` | ✅ **EXERCIDA** | **8 `MUST` + 2 `MUST NOT` · `0` `SHOULD` · `0` `MAY`**, e a distribuicao esta **declarada com motivo** dentro da `Spec` |
| `SF-12` | ✅ **EXERCIDA** | **60 campos, `0` ausentes** — contados por ferramenta, 10 blocos × 6 |
| `SF-13` | ✅ **EXERCIDA, em 3 das 6 naturezas** | `FATO` **8** · `REQUISITO` **10** · `HIPOTESE` **1** *(`H-1`, marcada, com o teste que a confirmaria)*. `DECISAO` **`0` — e isso e a regra obedecida**, nao lacuna: ela *"nao entra: remete"*. `RECOMENDACAO` e `NOTA`: **`0`**, sem ocasiao |
| `SF-14` | ✅ **EXERCIDA nos 5** | `INSPECAO` 3 · `DEMONSTRACAO` 2 · `TESTE` 2 · `ANALISE` 1 · `MEDICAO` 2 |
| `SF-15` | ✅ **EXERCIDA** | **3** evidencias produzidas · **8** declaradas `definido, sem valor`. **`0`** fabricadas |
| `SF-16` | ✅ **EXERCIDA** | **`0` ocorrencias** dos dez adjetivos vedados, contadas por ferramenta sobre o corpo inteiro |
| `SF-17` | ✅ **EXERCIDA nos 7** | Um requisito por perfil, no minimo |
| `SF-18` | ✅ **EXERCIDA (negativa)** | **`0`** entidades, tipos, templates, diretorios ou Departamentos criados a partir de perfil |
| `SF-19` | ✅ **EXERCIDA (negativa)** | Nao se especializou perfil algum, e a **decisao de nao especializar esta registrada**, como `FND-04 §6.2` manda |
| `SF-20` | ✅ **EXERCIDA** | **9 de 9** elos percorriveis sem consultar pessoa |
| `SF-21` | ⚠️ **PARCIAL — 4 das 6 relacoes** | `refina`, `restringe`, `implementa`, `verifica` usadas. `substitui` **`0`** *(nada a superar)*; `conflita` **`0`** *(ver `SF-22`)* |
| `SF-22` | ❌ **NAO EXERCIDA** | **Impossivel com `1` `Spec`.** O limite `L3` de `FND-11 §14` **permanece**: `0` conflitos reais ocorreram |
| `SF-23` | ✅ **EXERCIDA** | `DoR` **9 de 9**, cada item com **onde se confere** — inclusive as quatro perguntas de nao-proliferacao **respondidas por escrito** |
| `SF-24` | ✅ **EXERCIDA** | `DoD` **10 de 10**. O item **(9)** e o que **obrigou** o `FIT` |
| `SF-25` | ✅ **EXERCIDA nas 4** | Funcional 4 · Nao funcional **com numero, instrumento e data** 1 · Negativo 2 · De falha 1. **`0`** ausencias a justificar |
| `SF-26` | ✅ **EXERCIDA nas 4** | `SUPOSICAO`, `LIMITE` *(com numero)*, `ROLLBACK` *(com responsavel e custo medido)* e `ABANDONO` *(3 sinais)*. **Nenhum *"nao aplicavel"*** |
| `SF-27` | ❌ **NAO EXERCIDA** | Versao **1.0.0**; nenhuma emenda ocorreu |
| `SF-28` | ❌ **NAO EXERCIDA** | Nao ha segunda versao nem segunda `Spec` de onde herdar |
| `SF-29` | ❌ **NAO EXERCIDA** | Nenhuma emenda |
| `SF-30` | ❌ **NAO EXERCIDA** | Limite `L4` de `FND-11 §14` **permanece**: `0` superacoes reais |
| `SF-31` | ⚠️ **EXERCIDA, com uma exigencia INAPLICAVEL** | `resumo` **168 caracteres** ✅ · gatilho de ativacao ✅ · pacote minimo ✅ · secoes sob demanda ✅ · **custo medido: 603 linhas por `wc -l`, 2026-08-02** ✅. **O teste do *dobro da mediana do proprio tipo* e INAPLICAVEL: a populacao do tipo e `1`** — e isso esta **declarado**, nunca presumido satisfeito |
| `SF-32` | ✅ **EXERCIDA** | Template canonico usado; **contador incrementado na MESMA mudanca**; **`0`** registros novos criados. **Foi o uso do template que expos `RD-93`** — o defeito e de `TPL-spec` contra `SF-06`, nunca de `SF-32` |

**Contagem, feita por ferramenta sobre as 32 linhas desta tabela — nao de cabeca:**

| Estado | Quantas | Quais |
|---|---|---|
| ✅ **Exercidas sem ressalva** | **22** | `SF-01`–`SF-05`, `SF-08`, `SF-09`, `SF-11`–`SF-20`, `SF-23`–`SF-26`, `SF-32` |
| ⚠️ **Exercidas com insuficiencia ou parcialidade** | **4** | `SF-06`, `SF-07`, `SF-21`, `SF-31` |
| ❌ **Exercida e defeituosa** | **1** | `SF-10` |
| ❌ **Nao exercidas** | **5** | `SF-22`, `SF-27`, `SF-28`, `SF-29`, `SF-30` |
| | **32** | conferido: `22 + 4 + 1 + 5` |

**As cinco nao exercidas sao todas do regime de mudanca e de conflito**, e nenhuma delas pode ser
exercida por uma `Spec` sozinha: `SF-27`, `SF-28` e `SF-29` exigem uma **segunda versao**;
`SF-22` e `SF-30`, uma **segunda `Spec`**. **Os limites `L3` e `L4` de `FND-11 §14` permanecem
abertos**, e esta missao **nao os fecha nem afirma te-los fechado**.

### 6.2 As quatro insuficiencias medidas — e nenhuma foi corrigida aqui

| Achado | Enunciado, com a fonte | Dono · Gatilho |
|---|---|---|
| **`RD-91`** | **A coluna `C1 · T2` de `SF-10` produz aprovacao NULA para todo artefato `SPC`.** Para `SPC`, `FND-09 §8.2` poe **DEP-PRD** como quem propoe/cria **e** como proprietario *(aposenta)*; a coluna `C1 · T2` poe *Aprovacao* = **proprietario + revisor**; `FND-04 §3.1` declara **nula** a aprovacao com `Proponente = Aprovador` (`LV-03`, Linha Vermelha de `FND-01`, **nivel 1**). **A coluna `C0 · T2` tem o mesmo colapso**, e por identica razao. **Consequencia verificavel: `C2` e a MENOR classe da matriz em que uma `Spec` pode ser validamente aprovada** — o piso que `FND-04 §6` fixa e **inutilizavel** | **SOBERANO** *(so ele emenda `FND-11`, `LM-02`)* · *"proxima emenda de `FND-11` ou segunda `Spec` real"* |
| **`RD-92`** | **`DEP-QAR` acumula custodiante da materia e revisor do tipo na mesma mudanca.** Custodiante por ser custodio de `CAP-juridico`; revisor por `FND-09 §8.2` linha `SPC`. **Nao e** incompatibilidade de `FND-04 §3.1` — e por isso **nao anula** —, mas reduz a independencia que a tabela sugere | **DEP-GOV** · *"segunda `Spec` custodiada por DEP-QAR"* |
| **`RD-93`** | **`TPL-spec` 1.1.0 declara tres campos de frontmatter que nenhuma fonte preve para `Spec`.** `FND-03 §4.1` da a `Spec` **dois** campos extras — `produto` e `criterios_aceite_count` — e `SF-06` reproduz **exatamente esses dois**. O esqueleto do template traz **cinco**: acrescenta `classe_mudanca` e `tipo_decisao` *(previstos para **`ADR`**)* e `capabilities` *(previsto para Departamento, agente, subagente, skill, workflow, produto, projeto e ferramenta — **`Spec` nao esta na lista**)*. **Isso contradiz `SF-05`**, que afirma *"nenhum campo novo e criado por este Framework (`AC-07`)"*. **`SPC-001` seguiu o TEMPLATE**, que `SF-32` declara canonico, e a divergencia fica **declarada, nao resolvida por escolha propria** | **DEP-PRD** *(dono do tipo e mantenedor de `TPL-spec`)*, com DEP-GOV *(aprova template)* · *"proxima emenda de `TPL-spec` ou de `FND-03 §4.1`"* |
| **`RD-94`** | **`SF-07` exige *"exatamente uma `Capability`"*, e a materia da primeira `Spec` atravessa tres.** `LM-6(a)` toca `CAP-juridico` *(norma externa)*, `CAP-seguranca` *(`RQ-5`, `RQ-6`)* e `CAP-dados` *(`RQ-1`, `RQ-2`)*. A escolha foi **determinada positivamente** — `CAP-juridico` e a unica cujo escopo declarado diz *"reconhecer obrigacao externa aplicavel"* —, e nao por eliminacao. Mas **a regra obriga a apagar dois vinculos verdadeiros**, e `VC-01` proibe elo que nao corresponde. **`VC-03` ja tinha sinalizado o mesmo padrao no produto** *(`RD-74`, cinco Capabilities)* | **DEP-PRD** · *"segunda `Spec` cuja materia atravesse mais de uma `Capability`"* |

> **Nenhum dos quatro foi corrigido, e a razao e a mesma para os quatro:** corrigir `RD-91` e
> `RD-94` exige emendar `FND-11`, que so vigora com **ratificacao do SOBERANO**; corrigir `RD-93`
> exige emendar `TPL-spec`, mudanca `C2` com rito proprio; e o **congelamento em vigor** determina
> que achado novo **se registra com dono e gatilho e nao gera missao**. **`0` bytes em
> fundacional, `0` bytes em `TPL`.**

### 6.3 O que `SF-09` custa — a medicao que `L2` exigia e ninguem tinha

`FND-11 §14`, limite `L2`: *"`SF-09` institui 21 blocos obrigatorios **sem custo medido**.
`CE-04` proibe estimar, e nada foi estimado: **o valor sera medido na primeira `Spec`**."*

| Medida | Valor | Instrumento · data |
|---|---|---|
| **`SPC-001`** | **603 linhas** | `wc -l` · 2026-08-02 |
| Mediana do acervo *(221 artefatos)* | **270 linhas** | `wc -l` sobre a lista fechada · 2026-08-02 |
| **Razao `SPC-001` ÷ mediana** | **`2,23×`** | derivada das duas acima |
| Carta `PRO-nxtrack`, para comparacao | 263 linhas | `wc -l` |
| **Um bloco de requisito** *(`RQ-3`)* | **13 linhas** | `wc -l` sobre o recorte |
| **Consulta enderecada × leitura integral** | **13** contra **603** — razao **`1:46`** | derivada |

**Leitura.** Os 21 blocos custam caro **na escrita** e barato **na consulta**, e a economia so se
realiza se o consumidor usar `SPC-001 RQ-nn` em vez de carregar o documento — que e exatamente o
que `SF-31` prescreve e o que `FND-11 §15` diz que se mede na revisao. **`CE-05` — *"o dobro da
mediana do seu tipo"* — nao pode ser aplicado: `n = 1`.** Com a **terceira** `Spec` o teste passa
a existir. **Declarado inaplicavel, nunca presumido satisfeito.**

### 6.4 O que o Framework acertou, e vale registrar

| # | Acerto, com o sinal |
|---|---|
| `AC-1` | **`SF-12` pegou requisito fraco na hora de escrever.** Exigir `fonte` **por identificador** derrubou tres enunciados que eram preferencia disfarcada: nao havia `F-n` que os sustentasse |
| `AC-2` | **`SF-02` funcionou como filtro, nao como enfeite.** `RQ-2` foi redigido como *"acrescentar coluna de usuario"* e **reescrito** como *"deve ser possivel determinar o conjunto"* — a regra mudou o texto |
| `AC-3` | **`SF-25` obrigou o requisito de falha**, e ele so foi encontrado porque a busca por *"o que acontece quando falha"* levou a `F-6` — o backup que carrega `hash`+`sal` de todos. **Sem `SF-25`, `RQ-7` e `RQ-8` nao existiriam** |
| `AC-4` | **`SF-23` item (3) — as quatro perguntas de nao-proliferacao — obrigou a achar `spec-tecnica-v1.md §24`.** A pergunta *"isso ja existe em outra forma?"* e o que motivou a varredura estendida, que mudou o recorte da `Spec` inteira |
| `AC-5` | **`SF-15` impediu evidencia inventada.** **8** evidencias entraram como `definido, sem valor` em vez de virarem afirmacao |

## 7. Achados — 5 novos, 0 fechados

| Achado | Severidade | Estado |
|---|---|---|
| **`RD-91`** — `C1 · T2` de `SF-10` produz aprovacao nula para `SPC` | **Alta** *(nao bloqueante: `C2` contorna, e o contorno esta exercido)* | ⚠️ **ABERTO** |
| **`RD-92`** — DEP-QAR custodiante **e** revisor | Baixa | ⚠️ **ABERTO** |
| **`RD-93`** — `TPL-spec` 1.1.0 com 3 campos nao previstos | Media | ⚠️ **ABERTO** |
| **`RD-94`** — *"exatamente uma `Capability`"* × materia que atravessa tres | Media | ⚠️ **ABERTO** |
| **`RD-95`** — **os contadores de `ADR` e de `RFC` estavam DEFASADOS EM UM**, e o defeito so apareceu porque foram **exercidos** contra a copia datada em vez de lidos: `decisions/README` declarava `0030` disponivel com **`ADR-0030` ja existente**, e `rfcs/README` declarava `0025` com **`RFC-0025` ja existente**. Confiar neles produziria **colisao de identificador** (`FND-03 §2.3`). **Quarta ocorrencia da familia de `RD-32`**, e a primeira **depois** de `SF-32` ter codificado a causa. ✅ **Os dois contadores foram CORRIGIDOS nesta missao** — `0032` e `0027` —, e o achado fica aberto porque **a causa e recorrente e nao foi removida** | Media | ⚠️ **ABERTO** |

**`RD-80`, `RD-83` a `RD-90` nao foram tocados** e seguem como estavam. **`RD-88` nao foi
decidido:** a `Spec` de materia nao-produto continua inexistente, e **esta missao nao a criou** —
`SPC-001` e `Spec` **de produto**, e `EX-7` declara isso. **`E2`, `Q3` e `Q4` nao foram
decididos.**

> **`RD-80` — o gatilho disparou pela TERCEIRA vez.** `governance/roadmap-canonico.md` continua
> sendo medido pela baseline **sem ter entrada de classificacao no catalogo**. **Nao foi
> resolvido aqui:** resolver e missao de catalogo, e o congelamento veda abrir uma.

## 8. Baseline

| Campo | Valor |
|---|---|
| **Baseline anterior** | `BL-2026-08-01-03` — 218 · 64.383 · `94b85d8f…be5` |
| **Baseline nova** | **`BL-2026-08-02-01` = 223 artefatos · 66.100 linhas · `cd5ab24eba814472373a7c94bfc7ba2bdd3afcce83b71b2fe461d7405a8e080a`** — [catalogo mestre §10.0](artifact-registry.md), evidencia em **§10.21** |
| **Delta de artefatos** | **+5** — `RFC-0026`, `ADR-0031`, `SPC-001`, `FIT-2026-024` e este registro. **`0` removidos** |
| **Reproducao** | **2 execucoes independentes**, mesmo instrumento, **apos a ultima escrita** |

### 8.1 Pos-verificacao — arquivo a arquivo, contra o ponto de partida

| Medida | Valor |
|---|---|
| **Conferencia por `sha256`, arquivo a arquivo** | **589 identicos + 8 alterados + 5 criados + 0 removidos**, contra o `H-A` de **597** arquivos. **Soma: 589 + 8 = 597** *(todos os de partida respondidos)* **+ 5 = 602** |
| **Dos 8 alterados** | **7 autorizados** — catalogo mestre, `README` da raiz, `decisions/README`, `rfcs/README`, `governance/README`, `governance/fitness/README` e o roadmap — e **1 VOLATIL declarado**: `.obsidian/workspace.json`, raiz `NAO_ACERVO`, escrito pelo proprio Obsidian. **Classificado, jamais descartado** |
| **Fora do conjunto autorizado** | **`0` alterados · `0` criados.** E **`0` autorizados nao tocados** |
| **Camadas que NAO podiam mudar** | **195 arquivos conferidos, `0` alterados** — 11 `FND` · 19 `TPL` · 23 `CAP` · 9 Cartas `DEP` · 1 Carta `PRO` · 30 `ADR` anteriores · 25 `RFC` anteriores · 23 `FIT` anteriores · 15 `PS` · 16 `PT` anteriores · 9 `MSG` · 14 entre `MEM`, `INC` e `atos-superados` |
| **As fontes que a `Spec` mais tocaria** | **`FND-03`, `FND-04`, `FND-10`, `FND-11` e `TPL-spec`: IDENTICOS.** `FND-11` foi **exercido**, nunca emendado; `TPL-spec` foi **usado**, e `RD-93` o declara defeituoso **sem o corrigir** |
| **Repositorio do candidato** | `tree` de `My_WorkSpace/Meus_projetos/nxtrack` = **`b9b36be9324ae2d36ddc4149049ebbff9f40fb4b`**, medido **depois** de todo o trabalho: **identico** ao de antes e ao publicado na Carta |
| **Links relativos** | **1.057** conferidos nos 12 arquivos tocados e criados · **`0` quebrados** |

## 9. Custo da missao — medido, para o Fundador comparar

| Item | Valor |
|---|---|
| **Artefatos criados** | **5** — `RFC-0026` · `ADR-0031` · **`SPC-001`** · `FIT-2026-024` · `PT-2026-017` |
| **Artefatos editados** | **7** — catalogo mestre, `README` raiz, `decisions/README`, `rfcs/README`, `governance/README`, `governance/fitness/README`, roadmap |
| **Linhas criadas** | **1.580** — `RFC-0026` **197** · `ADR-0031` **271** · **`SPC-001` 603** · `FIT-2026-024` **211** · `PT-2026-017` **298**. Medidas por `wc -l`, **nunca estimadas** (`CE-02`, `CE-04`). **A `Spec` e 38,2% do total**, e os **21 blocos obrigatorios de `SF-09`** sao a razao — §6.3 |
| **`0` de que se cuidou** | `0` bytes em `FND-01`–`FND-11` · `0` em `TPL` · `0` em `CAP` · `0` em Carta · `0` em `ADR`/`RFC`/`FIT`/`PS`/`PT`/`MSG` historicos · `0` em baseline anterior · `0` no repositorio do candidato · `0` bancos abertos · `0` execucoes · `0` atos emitidos · `0` Skill, Tool, Command, Workflow, Agente, codigo ou infraestrutura |

## 10. O que esta missao **nao** fez

| # | Nao fez | Por que |
|---|---|---|
| `N1` | **Nao implementou nada** no nXtrack | `SF-02`; restricao expressa da missao |
| `N2` | **Nao emitiu parecer juridico** | `EX-3` da `Spec`; `CAP-juridico` remete a assessoria humana. **`0`** requisitos afirmam enquadramento legal |
| `N3` | **Nao decidiu `E2`, `Q3`, `Q4` nem `RD-88`** | Fora do escopo declarado no lease |
| `N4` | **Nao corrigiu `RD-91` a `RD-94`** | Exigiriam emendar `FND-11` *(SOBERANO)* ou `TPL-spec` *(`C2` proprio)*. **Congelamento: achado nao gera missao** |
| `N5` | **Nao contou titulares do nXtrack** | Exigiria abrir `nxtrack.db`. **Ausencia de medicao, declarada** |
| `N6` | **Nao criou a `Spec` de materia nao-produto** | `RD-88`; so `S2` a cria, e `S2` esta **deferida** pelo SOBERANO |
| `N7` | **Nao editou `PT-2026-015`, o roadmap historico nem qualquer baseline anterior** | `LV-04`, `BL-02` |

## 11. Decisao

**A `Spec` esta criada, aprovada pela classe e em vigor.** `C2 · Tipo 2` **nao exige ato do
Soberano** (`FND-04 §2.1`; `LM-02` alcanca `C3` e `Tipo 1`), e por isso **nao ha
`READY-FOR-RATIFICATION` a declarar sobre ela**.

**O que espera o Fundador nao e a `Spec` — e `RD-91`**, cujo dono e o SOBERANO por construcao:
sanar a coluna `C1 · T2` de `SF-10` exige emendar `FND-11`, e `FND` nao vigora sem ratificacao.
**Ate la, toda `Spec` do acervo tera de nascer em `C2`** para nao nascer nula, e **isso e uma
decisao de custo que so o Fundador pode tomar**.
