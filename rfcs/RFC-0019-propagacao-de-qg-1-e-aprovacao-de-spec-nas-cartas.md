---
id: RFC-0019-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas
titulo: Como propagar ADR-0018 e ADR-0019 as Cartas de DEP-PRD e DEP-EXE sem decidir nada de novo
tipo: rfc
versao: 1.0.0
status: aprovado
camada_memoria: estrategica
autor: DEP-EXE
proprietario: DEP-EXE
aprovador: DEP-GOV
criado_em: 2026-07-29
atualizado_em: 2026-07-29
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0011, ADR-0012, ADR-0018, ADR-0019, ADR-0021]
substitui: []
substituido_por: null
resumo: Submete a propagacao de ADR-0018 e ADR-0019 as Cartas de DEP-PRD e DEP-EXE, enumerando as oito afirmacoes falsas e medindo que o defeito alcanca mais Cartas do que RD-31 declarou.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# RFC-0019: Propagar `QG-1` e a aprovacao de `Spec` as Cartas

> **Pergunta em uma frase.** `ADR-0018` e `ADR-0019` foram **ratificados** e mudaram quem libera
> `QG-1` e quem aprova `Spec`. **As Cartas nao foram propagadas.** Esta RFC pergunta **como
> propagar sem decidir nada de novo** — e mede que o defeito e **maior** do que `RD-31` declarou.

## Proposito

Submeter a **forma** da propagacao. **Esta RFC nao decide autoridade, nao cria titular, nao cria
portao e nao reabre `ADR-0018` nem `ADR-0019`** — os dois estao **ratificados e vigentes**, e o
que falta e cascata (`CV-04`, `CC-03`).

## Escopo

| Item | Definicao |
|---|---|
| Inclui | As **oito** afirmacoes falsas da Carta de `DEP-PRD`; a **ausencia total** de `QG-1` na Carta de `DEP-EXE`; **todos** os blocos afetados das **duas** Cartas |
| **Nao** inclui | O **merito** de `ADR-0018` e `ADR-0019` · a criacao de titular, portao, papel, classe ou direito decisorio · as Cartas de **`DEP-OPS`, `DEP-GRW` e `DEP-TLS`**, onde o defeito **tambem foi medido** — achado **`RD-37`**, §3.2 · `DEP-ENG` *(§3.3 — revisado e sem afirmacao falsa)* · a sede da norma da `Spec` — [RFC-0018](RFC-0018-sede-canonica-do-framework-de-specifications.md), pacote separado |
| Origem | Achado **`RD-31`**; ressalva **`R3`** de [FIT-2026-015](../governance/fitness/FIT-2026-015-framework-de-specifications.md); caso `T-12` de [ADR-0021 §9](../decisions/ADR-0021-framework-de-specifications.md) |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| Propoe | **DEP-EXE** | [FND-09 §8.2](../foundation/09-meta-model.md), linha `DEP` — **proponente unico** de Carta de Departamento |
| Analise de risco e revisao independente | **DEP-QAR** | FND-07 §3.1; `RM-06b` |
| Valida forma | **DEP-GOV** | FND-09 §8.2, linhas `RFC` e `DEP` |
| **Decide (as Cartas)** | **SOBERANO** | FND-09 §8.2, linha `DEP` — aprova **e** ratifica. Indelegavel |

> **Residuo declarado (`PI-10`).** **DEP-EXE e o proponente e e a area que ganha declaracao de
> titularidade** — `QG-1` passa a constar da propria Carta. **A titularidade nao nasce aqui:**
> nasce em `ADR-0018`, **ratificado em 2026-07-29**, do qual DEP-EXE **nao foi autor nem
> revisor**. E `FND-09 §8.2` **nao admite outro proponente** de Carta de Departamento — `IC-3`.
> Residuo **de posicao, nao de interesse**; revisao por **DEP-QAR** e aprovacao por **DEP-GOV**
> em lugar de DEP-EXE, que esta impedido pela propria autoria (`I-1`, `PI-05`).

---

## 1. Situacao atual

`ADR-0018` mudou o liberador de `QG-1` de `DEP-PRD` para `DEP-EXE` e `ADR-0019` fez a aprovacao
de `Spec` **remeter a classe**. Os dois foram **ratificados** pelo sexto ato soberano
([MSG-2026-0006](../memory/operacional/MSG-2026-0006-ato-soberano-aplicacao-integral.md)), e
`FND-01`, `FND-09` e `FND-10` **foram emendadas**.

**As Cartas nao.** `ADR-0018 §7` declarou a cascata como **devida**, com dono `DEP-EXE` e gatilho
*"ato sobre esta emenda"*. **O ato veio; a cascata nao.**

## 2. Problema — **medido, e maior do que o declarado**

### 2.1 O consumidor obtem respostas diferentes conforme o caminho

| Pergunta | Resolvida pela **fonte** | Resolvida pelas **Cartas** |
|---|---|---|
| Quem libera `QG-1`? | **`DEP-EXE`** — `FND-01 §6.2` | **`DEP-PRD`** — 8 afirmacoes |
| Quem aprova a `Spec`? | **conforme a classe** — `FND-09 §8.2`, `FND-04 §2` | **`DEP-PRD`**, citando texto de `FND-09 §8.2` **que nao existe mais** |

**E o caso `T-12` de `ADR-0021 §9`:** *"deterministico e DIVERGENTE"*.

### 2.2 As oito afirmacoes falsas de `DEP-PRD`, enumeradas

| # | Local | O que afirma | Por que e falsa |
|---|---|---|---|
| **1** | `§3 P-8` | *"**Portao QG-1**"* como responsabilidade exclusiva | O portao nao e de `DEP-PRD` desde `ADR-0018` |
| **2** | `§5` | *"Liberacao de **QG-1** · A2"* como materia decidida | Autoridade que a Carta nao tem mais |
| **3** | `§5` | *"**Aprovar Spec** · fonte: `FND-09 §8.2`, linha `SPC`: **aprova DEP-PRD (QG-1)**"* | **A fonte citada nao existe mais:** a celula passou a *"conforme classe (FND-04 §2)"* por `ADR-0019` |
| **4** | `§5.2` | tabela *"Portoes sob minha responsabilidade"* com `QG-1` | Nao ha portao sob responsabilidade de `DEP-PRD` |
| **5** | `§5.2` | *"**QG-1 e o unico portao que DEP-PRD libera sozinho**"* | Nao libera nenhum |
| **6** | `§7` | `Spec` — *"**Autor e aprovador** (QG-1)"* | Autor sim; aprovador **conforme a classe** |
| **7** | `§10.1 RP-1` | *"DEP-PRD e o unico liberador do proprio portao"* como **risco vivo** | O risco foi **extinto na fonte** |
| **8** | `§12.3` | *"**Portao QG-1** · destino explicito obrigatorio"* na extincao | Nao se lega o que nao se detem |

### 2.3 E `DEP-EXE` nao declara `QG-1` em nenhuma linha

**`0` ocorrencias, medido.** **Consequencia verificavel: o portao da `Spec` nao tem titular
declarado em Carta alguma** — quem resolve pelas Cartas obtem `DEP-PRD`; a fonte diz `DEP-EXE`.

## 3. Evidencia nova — o defeito alcanca **quatro** Cartas, nao duas

### 3.1 Metodo

`RD-31` mediu `DEP-PRD` e `DEP-EXE`. **Esta RFC mediu as nove**, por `grep "QG-1"` sobre
`departments/*/carta.md`.

### 3.2 Achado `RD-37` — tres Cartas afirmam o mesmo, e nenhuma foi enumerada

| Carta | Local | Texto literal |
|---|---|---|
| **`DEP-OPS`** | `§5.2` | *"Os sete portoes de FND-01 §6.2 sao liberados por DEP-EXE (QG-0), **DEP-PRD (QG-1)**, ..."* |
| **`DEP-GRW`** | `§5.2` | idem |
| **`DEP-TLS`** | `§5.2` | idem |

**Sao 3 afirmacoes falsas em 3 Cartas ratificadas, todas fora do escopo determinado para esta
missao.** Achado **`RD-37`**, severidade **Media**, dono **DEP-EXE**, revisa **DEP-GOV**,
gatilho *"proximo ato soberano que alcance `DEP-OPS`, `DEP-GRW` ou `DEP-TLS`"*. **NAO corrigido
aqui, e o motivo e escopo determinado — nao impossibilidade normativa.**

> **Por que `RD-31` nao as viu, e e a mesma causa de `RD-23` e da propria `RD-31`:** procurou-se
> **a Carta de quem perdeu a autoridade** e **a Carta de quem a ganhou** — e nao **a projecao da
> tabela de portoes**, que tres Cartas de classe diferente reproduzem por serem as que **nao
> liberam portao nenhum**. **Total medido: 8 + 3 = 11 afirmacoes falsas em 4 Cartas.**

### 3.3 `DEP-ENG` — revisada, **sem afirmacao falsa**

| Local | Texto | Veredito |
|---|---|---|
| `§6.1` | *"gatilho: **Liberacao de QG-1**"* | **Verdadeiro.** O gatilho e o evento, nao o titular |
| `§8.2` | *"criterio de devolucao: **QG-1 nao liberado**"* | **Verdadeiro.** Independe de quem libera |

**`DEP-ENG` nao entra no pacote, e a razao e que nao ha o que corrigir** — nao que esteja fora
de escopo.

### 3.4 Achado `RD-41` — a Carta de `DEP-PRD` aloja a `Spec` no diretorio errado

| Local | Texto | Contra |
|---|---|---|
| `DEP-PRD §7` | `Spec` · *"Onde vive: fase futura — **`projects/`**"* | `FND-03 §3.6`, `FND-04 §6` e `FND-10 §4.4`: **`products/<slug>/specs/`** |

**Encontrado ao reescrever a linha 6 da tabela de §2.2**, e **corrigido no mesmo candidato** —
e correcao **para** o local canonico, **nunca do** local canonico. Severidade **Baixa**.

## 4. Criterios de avaliacao — **declarados antes das opcoes**

| # | Criterio |
|---|---|
| **L1** | **Propagar, nunca decidir** — nenhuma linha nova pode ser a **fonte** de uma autoridade |
| **L2** | **Zero titular, portao, papel, classe ou direito decisorio novo** |
| **L3** | **Todos os blocos afetados**, nao apenas `§5` e `§5.2` |
| **L4** | **`DEP-ENG` e `DEP-QAR` permanecem os revisores da `Spec`** |
| **L5** | **`DEP-PRD` conserva o que continua sendo dele** — escopo, criterio de aceite, e a aprovacao de `Spec` `C0`/`C1` como proprietario |
| **L6** | **Risco extinto e declarado extinto, nunca apagado** (`MM-09`) |
| **L7** | **`QG-1` passa a ter titular declarado em Carta** — o que fecha o defeito de `RD-31` |
| **L8** | **Diff literal, reversivel e com hash**, e **`0` Cartas editadas antes do ato** (`IR-01`) |

## 5. Opcoes

### Opcao A — **Emendar as duas Cartas, revisando todos os blocos** *(recomendada)*

`DEP-PRD` **1.1.0** e `DEP-EXE` **1.1.0**, `C2 · Tipo 2`, com **ato do Soberano** — porque
`FND-09 §8.2`, linha `DEP`, atribui aprovacao **e** ratificacao ao SOBERANO.

**Atende `L1` a `L8`.** Custo: 1 RFC + 1 ADR + 2 candidatos + 1 pacote + 1 ato.

### Opcao B — **Corrigir apenas `§5` e `§5.2` de `DEP-PRD`**

**Recusada: falha `L3` e `L7`.** Deixaria **seis** das oito afirmacoes falsas vivas — `§3 P-8`,
`§7`, `§10.1` e `§12.3` — e **nao daria titular declarado a `QG-1`**, porque a Carta de `DEP-EXE`
nao seria tocada. **E a correcao que parece suficiente e nao e**, e foi por isso que `RD-31`
enumerou 8 onde `PT-2026-004` havia enumerado 4.

### Opcao C — **Emendar as quatro Cartas**, incluindo `DEP-OPS`, `DEP-GRW` e `DEP-TLS`

| Criterio | Atende? | Observacao |
|---|---|---|
| `L1`–`L8` | ✅ | Tecnicamente superior: **zera** as 11 afirmacoes falsas |
| Escopo determinado | ❌ | A missao determinou **"as duas Cartas"** e *"gerar candidatos versionados das duas Cartas"* |

**Recusada por escopo, nao por merito** — e a diferenca esta registrada. **O achado `RD-37` fica
aberto com dono, gatilho e custo**, e a Opcao C permanece disponivel **a um ato de distancia**:
as tres alteracoes sao **uma linha cada**, no mesmo paragrafo, nas tres Cartas.

### Opcao D — **Nota interpretativa em `governance/`, sem emendar Carta**

**Recusada: falha `L1` e `L7`.** Uma nota que diga *"leia `DEP-PRD §5` como se dissesse
DEP-EXE"* **cria uma terceira fonte** para a mesma pergunta e **agrava** o defeito que `RD-31`
descreve. E `PJ-03` ja resolve a divergencia em favor da fonte — **a nota nao acrescentaria
norma, apenas leitura**.

### Opcao Z — **Nao propagar**

**Recusada.** `LV-03` mitiga *(liberacao por quem produziu e **nula**)*, mas **mitigacao nao e
cumprimento**: o acervo permaneceria com **divergencia conhecida entre fonte fundacional e Carta
vigente** sobre o portao do proprio artefato que a Missao 1.13 normatizou. E a ressalva `R3`
fixou o gatilho: **antes da primeira `Spec`**.

## 6. Recomendacao

| Campo | Conteudo |
|---|---|
| **Recomendacao** | **Opcao A** |
| **Classe proposta** | **C2** — altera **componente** *(duas Cartas)*; **nao** altera direito de decisao, principio, linha vermelha nem hierarquia |
| **Tipo proposto** | **2** — reversivel pelos diffs literais, com hash publicado |
| **Aprovacao do ADR** | **DEP-GOV**, em lugar de DEP-EXE, **que esta impedido pela propria autoria** (`I-1`, `PI-05`; precedente `FIT-2026-003`) |
| **Aprovacao e ratificacao das Cartas** | **SOBERANO**, indelegavel (`FND-09 §8.2`, linha `DEP`; `DC-09`) |
| **Fundamento** | **Nada e decidido: tudo e propagado.** `QG-1` e de `DEP-EXE` por `ADR-0018`, **ratificado**; a aprovacao segue a classe por `ADR-0019`, **ratificado**; `C2` e aprovado por `DEP-EXE` por `FND-04 §2`, **anterior as duas**. **Nenhuma linha nova e fonte de autoridade — todas citam a fonte** |
| **Contrapartida honesta** | **`RD-37` fica aberto**: tres Cartas seguem afirmando que `DEP-PRD` libera `QG-1`. **O acervo sai de 11 afirmacoes falsas em 4 Cartas para 3 em 3** — melhora medida, **nao fechamento** |

## 7. Impacto previsto

| Objeto | Efeito | Executado nesta RFC? |
|---|---|---|
| **`DEP-PRD`** | **8** correcoes + **7** blocos revisados; **429 → 445** linhas | **Nao** — candidato fora do acervo |
| **`DEP-EXE`** | **11** blocos alterados; `QG-1` passa a constar; **481 → 506** linhas | **Nao** |
| `DEP-OPS`, `DEP-GRW`, `DEP-TLS` | **`0` bytes** — `RD-37`, declarado | **Nao** |
| `DEP-ENG` e as outras **3** Cartas | **`0` bytes** — nada a corrigir | — |
| **`FND-01`, `FND-04`, `FND-09`, `FND-10`** | **`0` bytes** — a fonte **ja esta correta** | — |
| **Titulares · portoes · papeis · classes · direitos de decisao** | **0 criados · 0 alterados** — **7 portoes antes, 7 depois** | — |
| **Indices `M3`** | **4** — catalogo mestre, `README` raiz, `decisions/README`, `rfcs/README` | **Sim** — cascata `CV-04` |

## 8. Riscos

| # | Risco | Prob. | Impacto | Mitigacao |
|---|---|---|---|---|
| **RQ-1** | **A propagacao ser lida como transferencia de poder para `DEP-EXE`** | Media | **Alto** | Cada linha nova **cita a fonte anterior**; `DEP-EXE` recebe **`I-10`**, que veda decidir conteudo da `Spec` que libera; `I-5` permanece intacto |
| **RQ-2** | **`QG-1` virar gargalo em `DEP-EXE`** | Media | Medio | Novo risco **`RX-8`** na Carta de `DEP-EXE`, com mitigacao declarada. Herdado de `RS-1` de `ADR-0018` |
| **RQ-3** | **`RD-37` ser lido como esquecimento** | **Alta** | Baixo | §3.2 o **enumera com texto literal**, dono, gatilho e custo *(uma linha por Carta)* |
| **RQ-4** | **Apagar `RP-1` esconder que o risco existiu** | Media | Medio | `L6`: a linha e **conservada** e marcada **EXTINTA NA FONTE** (`MM-09`), com a mitigacao original citada |
| **RQ-5** | **O ato nao vir** | Media | **Alto** | **`LV-03` continua valendo** — liberacao por quem produziu e **nula** —, mas o defeito de `RD-31` **permanece**, e a primeira `Spec` continuara a receber resposta errada pelas Cartas |

## 9. Perguntas em aberto

| # | Pergunta | Encaminhamento |
|---|---|---|
| **Q1** | **Estender ao escopo da Opcao C**, corrigindo `DEP-OPS`, `DEP-GRW` e `DEP-TLS` no mesmo ato? | **Do Soberano.** O proponente **cumpre o escopo determinado** e deixa `RD-37` aberto com custo medido: **3 candidatos a mais, uma linha alterada em cada** |
| **Q2** | `DEP-EXE` deve declarar tambem a **aprovacao de `Spec` `C2`**, ou apenas o portao? | **Resolvida na proposta: declara as duas.** Sem isso, a pergunta *"quem aprova uma `Spec` `C2`?"* continua **sem resposta nas Cartas** — e seria repetir o defeito de `RD-31` com outro objeto |

## 10. Resultado

| Campo | Conteudo |
|---|---|
| **Estado** | **ACOLHIDA** → [ADR-0023](../decisions/ADR-0023-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md) |
| **Opcao escolhida** | **A** |
| **Recusadas** | **B** *(insuficiente por medicao)* · **C** *(por escopo determinado, nao por merito)* · **D** *(terceira fonte)* · **Z** *(mitigacao nao e cumprimento)* |
| **Achados que abre** | **`RD-37`** *(Media — 3 Cartas, 3 afirmacoes falsas, nao corrigidas)* · **`RD-41`** *(Baixa — `Spec` alojada em `projects/`; **corrigida** no candidato)* |

## 11. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Achado que trata | **`RD-31`** — [catalogo §7, item 52](../governance/artifact-registry.md) |
| Ressalva que trata | **`R3`** de [FIT-2026-015](../governance/fitness/FIT-2026-015-framework-de-specifications.md) |
| Caso que originou | `T-12` de [ADR-0021 §9](../decisions/ADR-0021-framework-de-specifications.md) |
| Cascata declarada devida | [ADR-0018 §7](../decisions/ADR-0018-liberacao-do-portao-qg-1.md) · [PS-2026-007 §5](../governance/pacote-soberano-2026-07-29-rd-14.md) |
| Decisao resultante | [ADR-0023](../decisions/ADR-0023-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md) |
| Pacote soberano | [PS-2026-010](../governance/pacote-soberano-2026-07-29-rd-31.md) |
| RFC irma, materia separada | [RFC-0018](RFC-0018-sede-canonica-do-framework-de-specifications.md) |
| Baseline vigente na submissao | **`BL-2026-07-29-09`** |

---

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-EXE | Propoe a **forma** da propagacao de `ADR-0018` e `ADR-0019` as Cartas, entre **quatro opcoes e a opcao Z**, com `L1` a `L8` declarados antes delas. **Enumera as oito afirmacoes falsas de `DEP-PRD` com local e razao**, e registra que **`DEP-EXE` nao declara `QG-1` em nenhuma linha** *(`0` ocorrencias)*. **Mede as nove Cartas, e nao as duas:** o defeito alcanca tambem `DEP-OPS`, `DEP-GRW` e `DEP-TLS`, que reproduzem em `§5.2` a frase *"liberados por ... DEP-PRD (QG-1)"* — **3 afirmacoes falsas em 3 Cartas nunca enumeradas**, achado **`RD-37`**, com a causa nomeada: procurou-se a Carta de quem perdeu e a de quem ganhou a autoridade, **nao a projecao da tabela de portoes**. **Total medido: 11 afirmacoes falsas em 4 Cartas.** Registra que **`DEP-ENG` foi revisada e nao tem afirmacao falsa** — as duas mencoes a `QG-1` sao **gatilho e criterio de devolucao**, verdadeiros independentemente do titular. Abre **`RD-41`** *(a Carta de `DEP-PRD` aloja a `Spec` em `projects/`, contra tres fontes vigentes que a alojam em `products/<slug>/specs/`)*, **corrigido no candidato**. Recomenda a **Opcao A**, recusa a **B** por medicao *(deixaria seis das oito vivas)*, a **C** **por escopo determinado e nao por merito** — deixando-a **a um ato de distancia** —, a **D** por criar terceira fonte e a **Z** porque **`LV-03` mitiga e mitigacao nao e cumprimento**. Escala **duas perguntas** ao Soberano, nenhuma bloqueante. **Nenhum titular, portao, papel, classe ou direito decisorio proposto: 7 portoes antes, 7 depois.** |
