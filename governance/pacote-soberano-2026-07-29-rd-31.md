---
id: PS-2026-010
titulo: Pacote de decisao soberana — emenda C2 Tipo 2 das Cartas de DEP-PRD e DEP-EXE que fecha RD-31
tipo: relatorio
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: DEP-EXE
proprietario: DEP-EXE
aprovador: DEP-GOV
criado_em: 2026-07-29
atualizado_em: 2026-07-29
revisao_prevista: null
decisoes_relacionadas: [ADR-0012, ADR-0018, ADR-0019, ADR-0023]
substitui: []
substituido_por: null
canal: REPORTE
emissor: DEP-EXE
destinatario: SOBERANO
ttl: ate decisao do Soberano
resumo: Submete ao Soberano as duas Cartas que propagam ADR-0018 e ADR-0019, com diff literal das oito correcoes, hashes integrais, H-P projetado e a medicao de que o defeito alcanca outras tres Cartas.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# PS-2026-010 — As Cartas de `DEP-PRD` e `DEP-EXE`, e o fechamento de `RD-31`

> ## Este pacote **informa**. Nao decide, nao aprova, nao promulga e nao edita nada.
>
> **`DEP-PRD` permanece em 1.0.0 e `DEP-EXE` em 1.0.0.** Os candidatos existem como **arquivo
> real fora do acervo**, com caminho declarado em §4.4.
>
> **Enquanto nao houver ato, as oito afirmacoes falsas continuam vigentes** — e a pergunta
> *"quem libera `QG-1`?"* continua tendo **duas respostas** no acervo.
>
> **Pacote separado de [PS-2026-009](pacote-soberano-2026-07-29-fnd-11.md), por determinacao.**
> **Podem compartilhar um ato**, e cada objeto permanece **independente, verificavel e bloqueavel
> isoladamente** — §6.
>
> **Caminho exato:** `governance/pacote-soberano-2026-07-29-rd-31.md` *(RE-01)*.

## Proposito

Levar ao Soberano a **propagacao** de `ADR-0018` e `ADR-0019` — **ambos ratificados em
2026-07-29** — as Cartas de `DEP-PRD` e `DEP-EXE`. **Nenhuma autoridade e decidida aqui:** o que
falta e cascata (`CV-04`, `CC-03`), declarada devida em `ADR-0018 §7` com dono e gatilho.

## Escopo

| Item | Definicao |
|---|---|
| Inclui | **Tres** objetos: `ADR-0023`, `DEP-PRD` **1.1.0** e `DEP-EXE` **1.1.0** |
| **Nao** inclui | A **sede da norma da `Spec`** — [PS-2026-009](pacote-soberano-2026-07-29-fnd-11.md) · o **merito** de `ADR-0018` e `ADR-0019`, **nao reaberto** · **`DEP-OPS`, `DEP-GRW` e `DEP-TLS`**, onde o mesmo defeito **foi medido** — **`RD-37`**, §5 · `DEP-ENG` *(revisada; nada a corrigir)* · **`FND-01`, `FND-04`, `FND-09`, `FND-10`, `TPL-spec`** — **`0` bytes** · `RD-27`, `RD-33`, `RD-36` · qualquer artefato historico |
| Natureza | **Reporte**, entidade `MSG`. **Nenhum** tipo, entidade, camada, template ou diretorio novo |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| **Autor das emendas** | **DEP-EXE** | `FND-09 §8.2`, linha `DEP` — **proponente unico** de Carta de Departamento |
| **Revisor independente** | **DEP-QAR** | `RM-06b`; `AC-03` |
| **Aprovador do `ADR`** | **DEP-GOV** | `DEP-EXE` esta **impedido pela propria autoria** (`I-1`, `PI-05`). Precedente `FIT-2026-003` |
| **DECIDE (as Cartas)** | **SOBERANO** | `FND-09 §8.2`, linha `DEP`; `DC-09`. **Indelegavel.** **Nao ocorreu** |

> **Residuo declarado (`PI-10`).** **`DEP-EXE` e o autor e e a area que ganha a declaracao de
> titularidade** — `QG-1` passa a constar da propria Carta. **A titularidade nao nasce aqui:**
> nasce em `ADR-0018`, do qual DEP-EXE **nao foi autor nem revisor**. **`DEP-PRD`, a area que
> perde declaracoes, tambem nao e autora nem revisora** — `FND-09 §8.2` **nao admite** outro
> proponente de Carta (`IC-3`). Residuo **de posicao, nao de interesse**.

---

## 1. O que se pede

| # | Objeto | Ato pedido | Se **nao** houver ato |
|---|---|---|---|
| **1** | **`ADR-0023`** | **Aprovacao** *(nao exige ratificacao — `C2 · Tipo 2`)* | A propagacao permanece **proposta** |
| **2** | **`DEP-PRD` 1.1.0** | **Aprovacao e ratificacao** | As **8** afirmacoes falsas permanecem vigentes; a Carta continua reivindicando `QG-1` e citando um texto de `FND-09 §8.2` **que nao existe mais** |
| **3** | **`DEP-EXE` 1.1.0** | **Aprovacao e ratificacao** | **`QG-1` continua sem titular declarado em Carta alguma** — o defeito central de `RD-31` |

> **Nao ha aprovacao parcial util entre 2 e 3, e a razao e simetrica.** Aplicar **so `DEP-PRD`**
> retiraria o portao de quem nao o detem **sem dar-lhe titular** — o acervo passaria de *"titular
> errado"* para *"nenhum titular"*, que e **pior para o consumidor**. Aplicar **so `DEP-EXE`**
> deixaria **duas Cartas afirmando titulares diferentes** para o mesmo portao. **Os dois formam um
> objeto normativo unico.**

## 2. Diff literal — `DEP-PRD` **1.0.0 → 1.1.0**

### 2.1 Frontmatter

| # | Antes | Depois |
|---|---|---|
| **F1** | `versao: 1.0.0` | `versao: 1.1.0` |
| **F2** | `status: ativo` | `status: em-revisao` |
| **F3** | `atualizado_em: 2026-07-28` | `atualizado_em: 2026-07-29` |
| **F4** | `decisoes_relacionadas: [ADR-0001, ADR-0002, ADR-0003, ADR-0011]` | `[..., ADR-0011, ADR-0018, ADR-0019, ADR-0023]` |
| **F5** | `ratificacao: ratificada` | `ratificacao: pendente` |

### 2.2 As oito afirmacoes falsas, com o texto literal do antes

| # | Local | **Antes — literal** |
|---|---|---|
| **P1** | `§3 P-8` | `\| P-8 \| **Portao QG-1** \| Nenhuma spec passa a construcao sem resultado, criterio de aceite e escopo negativo \| CAP-produto \|` |
| **P2** | `§5` | `\| Liberacao de **QG-1** \| A2 \| — \| FND-01 §6.2 \|` |
| **P3** | `§5` | `\| **Aprovar Spec** (\`SPC\`) \| A2 \| DEP-ENG + DEP-QAR *(revisores)* \| FND-09 §8.2, linha \`SPC\`: aprova DEP-PRD (QG-1) \|` |
| **P4** | `§5.2` | cabecalho `### 5.2 Portoes sob minha responsabilidade` + tabela com a linha `\| **QG-1** \| A spec define **resultado**, **criterio de aceite** e **o que esta fora**? \| ... \|` |
| **P5** | `§5.2`, nota | `> **QG-1 e o unico portao que DEP-PRD libera sozinho** — e por isso o unico ponto do fluxo em` / `> que a definicao pode passar sem contraditorio. A mitigacao esta em **RP-1**.` |
| **P6** | `§7` | `\| **Spec** \| \`SPC\` \| **Autor e aprovador** *(QG-1)*; **nunca revisor do proprio** \| fase futura — \`projects/\` \|` |
| **P7** | `§10.1` | `\| RP-1 \| **QG-1 sem contraditorio** — DEP-PRD e o unico liberador do proprio portao \| **Media** \| **Alto** \| ... \|` |
| **P8** | `§12.3` | `\| **Portao QG-1** \| Destino explicito obrigatorio; portao sem dono e portao pulado. **Nunca** a DEP-ENG — quem constroi nao define \|` |

**O texto integral do depois esta em [ADR-0023 §5.1](../decisions/ADR-0023-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md)
e no candidato**, cujo `H-A` esta em §4.1 — e **os dois extremos estao fixados
criptograficamente**, o que torna o diff entre eles o autorizado.

### 2.3 Os sete blocos adicionais

| # | Local | Alteracao |
|---|---|---|
| **P9** | `§4` | **+2 linhas** *(o que nao me compete)* |
| **P10** | `§5.1` | **+2 linhas** *(o que nao decido)* |
| **P11** | `§8` | 1 celula — *"nao se libera QG-1"* → *"a spec nao e submetida a `QG-1`"* |
| **P12** | `§8.2` | 1 celula — *"QG-1 liberado"* → *"`QG-1` liberado **por DEP-EXE**"* |
| **P13** | `§10` | **+1 linha** — impedimento **`I-12`** |
| **P14** | `§10.2` | **+1 linha** — incompatibilidade de papel |
| **P15** | `§11 KP-6` | 1 linha — indicador **retitulado**, valor `0` **mantido** |
| **P16** | `§9.1`, `§13.2` | **5 medicoes remedidas** — `TPL-spec` **132 → 272**; recortes **53 → 55**, **130 → 145**, **429 → 445**; proporcao **30% → 33%** |
| **P17** | `§13.3` | **3 linhas** — decisoes, achados e alteracoes |
| **P18** | Historico | **+1 linha** — `1.1.0` |

**429 → 445 linhas *(+16)* · 21 blocos de diff.**

> **O que `§9.1` NAO corrige, e por que.** O custo do **nucleo** permanece **`1.099` linhas**,
> valor de 2026-07-28, **e ele divergiu** — a divergencia e materia de **`RD-27`**
> *(`FND-10 §8.5` declara `1.087` contra `1.116` medidos)*, que esta missao esta determinada a
> **nao tratar**. **Corrigido apenas `TPL-spec`**, cuja variacao vem de `ADR-0021`.

## 3. Diff literal — `DEP-EXE` **1.0.0 → 1.1.0**

### 3.1 Frontmatter

| # | Antes | Depois |
|---|---|---|
| **E0a** | `versao: 1.0.0` | `versao: 1.1.0` |
| **E0b** | `status: ativo` | `status: em-revisao` |
| **E0c** | `atualizado_em: 2026-07-28` | `atualizado_em: 2026-07-29` |
| **E0d** | `decisoes_relacionadas: [ADR-0001, ADR-0002, ADR-0004, ADR-0011]` | `[..., ADR-0011, ADR-0018, ADR-0019, ADR-0023]` |
| **E0e** | `ratificacao: ratificada` | `ratificacao: pendente` |

### 3.2 Os onze blocos — `QG-1` passa de **`0` ocorrencias** a **22, em 16 linhas**

| # | Local | O que e acrescentado |
|---|---|---|
| **E1** | `§3` | **`X-13`** — *"Portao `QG-1`"*, com *"verifico presenca e verificabilidade, nunca merito de escopo"* |
| **E2** | `§5` | **+2 linhas** — liberacao de `QG-1` *(A3)* e **aprovacao de `Spec` `C2`** |
| **E3** | `§5.2` | **+1 linha** — `QG-1` na tabela de portoes |
| **E4** | `§5.2`, nota | **+13 linhas** — por que `QG-1` **satisfaz** a regra de portao em vez de excepciona-la, e por que `I-5` continua vedando decidir merito |
| **E5** | `§6.1` | **+1 linha** — entrada: spec submetida, canal **HANDOFF** |
| **E6** | `§6.2` | **+1 linha** — saida: registro da liberacao, com responsavel e data |
| **E7** | `§7` | **+1 linha** — tipo `SPC`, em `products/<slug>/specs/` |
| **E8** | `§10` | **+1 linha** — impedimento **`I-10`** |
| **E9** | `§10.1` | **+1 linha** — risco **`RX-8`** |
| **E10** | `§10.2` | **+1 linha** — incompatibilidade de papel |
| **E11** | `§11` | **+1 linha** — indicador **`KX-15`**, valor **`0` medido**; contagem **14/9/5 → 15/10/5** |
| **E12** | `§12.3` | **+1 linha** — destino de `QG-1` na extincao |
| **E13** | `§13.2`, `§13.3` | recortes **remedidos** *(155 → 172, 481 → 506, 32% → 34%)*; **+3 linhas** de rastreabilidade |
| **E14** | Historico | **+1 linha** — `1.1.0` |

**481 → 506 linhas *(+25)* · 21 blocos de diff.**

### 3.3 O que os dois diffs **nao** contem

| Nao contem | Verificacao |
|---|---|
| Titular novo | **Zero.** `QG-1` e de `DEP-EXE` por `ADR-0018`; `C2` e de `DEP-EXE` por `FND-04 §2`. **Cada linha nova cita a fonte** |
| Portao novo ou removido | **Zero** — **7 antes, 7 depois** |
| Papel, classe, verbo de autoridade, entidade ou tipo documental novo | **Zero** |
| Direito decisorio novo | **Zero.** Os dois acrescimos de autoridade em `DEP-EXE` sao **projecao** de `ADR-0018` e `FND-04 §2` |
| Alteracao dos revisores da `Spec` | **Zero** — `DEP-ENG` + `DEP-QAR` permanecem; `I-2` de `DEP-PRD` **intacto** |
| Retirada do que continua sendo de `DEP-PRD` | **Zero** — escopo, criterio de aceite, autoria e **aprovacao de `C0`/`C1`** conservados e **nomeados** |
| Risco apagado | **Zero** — `RP-1` e **conservado** e declarado **extinto na fonte** (`MM-09`) |
| Alteracao em `foundation/` | **Zero bytes** em `FND-01`, `FND-04`, `FND-09`, `FND-10` e `TPL-spec` |
| Alteracao do vinculo `Spec` × `Produto` | **Zero.** `P6` corrige a Carta **para** o local canonico — nunca o local canonico |
| Alteracao em `DEP-OPS`, `DEP-GRW`, `DEP-TLS`, `DEP-ENG` e as outras Cartas | **Zero bytes** — §5 |

## 4. Identificadores de integridade

### 4.1 As duas Cartas

| Carta | Versao | Linhas | `H-A` | `H-N` | `H-P` projetado *(apos `O4`)* |
|---|---|---|---|---|---|
| **`DEP-PRD` em vigor** | 1.0.0 | **429** | `6a11652f8719259376771bd398fe5960118185e823cf8217c3246ff0d563c277` | `1af73b7feaad38a162cc6960bb346caed1f554f6b39ce4c5b4d92ccae3128543` | — |
| **`DEP-PRD` candidato** | **1.1.0** | **445** | **`09d076dd305e2bd8cc2119772706141cdcfef998cd3ba9e7540267909699fb24`** | `ce3490049a57e6c141a40a07bcb7da1881b0389c4fe8134b359c7bf406d40279` | **`0e98511630faf9d5bec4c7cb36d8a37fa0bf15506dfde36954f0419e2720fc15`** |
| **`DEP-EXE` em vigor** | 1.0.0 | **481** | `fa7a6ae293afd53577c7c37076d8543a01fa187a4d6490dcf2f2a47b940f2bb8` | `47a499b36fb945ddde1bc6d504cac2c7a2a8e90b647f04e65d22d78dd06ec816` | — |
| **`DEP-EXE` candidato** | **1.1.0** | **506** | **`975e26dbf3f7f8760af01310b27b6b7e1667593d3dc12b520aeed9981013f25b`** | `537eb9f474dcc6e778c911d3abbe5cc9e4a84ec79914cf2aadb15d6aa929aab6` | **`a75a1ffea140e1f962e97b5b8772df70cf28831df882a25cf804b4e931f17e12`** |

**`O4` = `status: em-revisao → ativo` e `ratificacao: pendente → ratificada`, e nada mais.**
**`H-N` invariante sob `O4` — verificado em 2 de 2** (`IR-02`, `IR-06`).

### 4.2 `ADR-0023` e `RFC-0019`

| Objeto | Caminho · versao · linhas | `H-A` | `H-N` | `H-P` projetado |
|---|---|---|---|---|
| **`ADR-0023`** | `decisions/ADR-0023-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md` · **1.0.0** · **353** | **`3f8886d6892954c4a6f5703fe1b272290fc4165a7175fd4289d46b04f2907e51`** | `e727f50cd3c7a0399edb2a6c3c089433a16c47a44d69dc25aaf3b4e017bc8f10` | **`e0d6aa2dff881e62260af38672356ecc8057c01d925af861e40b24820bac84cc`** |
| **`RFC-0019`** | `rfcs/RFC-0019-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md` · **1.0.0** · **268** | `ff41c883a30a24cf9d4569ba8e9eb7cd376f15a026e538737b9b4fbaf3c0c566` | — | — |

### 4.3 Metodo de medicao — **validado antes do uso**

`IR-02` e `IR-03` foram **reimplementados** e validados contra **7 controles com hash publicado**,
em **quatro** tipos documentais, **antes** de medir qualquer candidato — a tabela integral esta em
[PS-2026-009 §4.3](pacote-soberano-2026-07-29-fnd-11.md). **7 de 7 reproduzem, digito a digito**,
e um deles e uma **Carta de Departamento** *(`DEP-QAR` 1.2.0, `H-P` aplicado)* — o mesmo tipo dos
candidatos deste pacote.

### 4.4 Onde os candidatos vivem — aplicacao de `RD-19`

```
E:\LucasIA\Projetos\_backups\LucaX-Enterprise-OS_2026-07-29_pre-missao-1-13-1\_candidatos\
  prd-1.1.0.md   445 linhas   09d076dd…fb24
  exe-1.1.0.md   506 linhas   975e26db…f25b
```

**Os arquivos existem e reproduzem os `H-A` acima**, conferidos **apos** a copia. **Terminadores:
`LF` nos dois**, conferido byte a byte; **`0` bytes `CR`**. **Montados por patch programatico com
assercao de unicidade por trecho** — cada substituicao falha em voz alta se o texto de origem nao
existir **ou** aparecer mais de uma vez, o que e a razao pela qual as **8** correcoes podem ser
afirmadas como **exatamente** as oito enumeradas.

### 4.5 `IR-09` — teste de reconstrucao

| Objeto | Operacao | Resultado |
|---|---|---|
| `DEP-PRD` 1.1.0 | Reverter **apenas** `status` e `ratificacao` no arquivo pos-`O4` e medir | **Reproduz `H-A`** |
| `DEP-EXE` 1.1.0 | idem | **Reproduz `H-A`** |
| `ADR-0023` | idem | **Reproduz `H-A`** |

**3 de 3.**

## 5. `RD-37` — o mesmo defeito em **tres** Cartas que este pacote **nao** corrige

**A medicao foi feita nas nove Cartas, nao nas duas.**

| Carta | Local | Texto literal | Correcao necessaria |
|---|---|---|---|
| **`DEP-OPS`** | `§5.2` | *"...sao liberados por DEP-EXE (QG-0), **DEP-PRD (QG-1)**, DEP-ENG + DEP-GOV (QG-2)..."* | **1 linha** |
| **`DEP-GRW`** | `§5.2` | idem | **1 linha** |
| **`DEP-TLS`** | `§5.2` | idem | **1 linha** |

**Severidade Media · dono `DEP-EXE` · revisa `DEP-GOV` · aprova e ratifica `SOBERANO` · gatilho
*"proximo ato soberano que alcance `DEP-OPS`, `DEP-GRW` ou `DEP-TLS`"*.**

**Efeito medido sobre o acervo:**

| Medida | Antes | Depois deste pacote |
|---|---|---|
| Afirmacoes falsas sobre `QG-1` | **11**, em **4** Cartas | **3**, em **3** Cartas |
| Cartas com titular de `QG-1` declarado | **0 de 9** | **2 de 9** |

> **Nao foi omissao nem impossibilidade normativa: foi escopo determinado.** A missao determinou
> *"as duas Cartas"* e *"gerar candidatos versionados das duas Cartas"*. **A extensao esta a um
> ato de distancia** — tres candidatos de **uma linha cada** —, e `Q1` de
> [RFC-0019 §9](../rfcs/RFC-0019-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md) a leva ao
> Soberano. **Se o ato quiser estende-la, §9.1 diz como.**

**E `DEP-ENG` foi revisada e nao entra: nao ha o que corrigir.** As duas mencoes a `QG-1` sao
**gatilho de entrada** e **criterio de devolucao** — verdadeiras independentemente do titular.

## 6. Independencia dos objetos — a condicao da missao, verificada

| Objeto | Independente? | Verificavel? | Bloqueavel isoladamente? |
|---|---|---|---|
| **`ADR-0023` + `DEP-PRD` + `DEP-EXE`** *(este pacote)* | **Sim** — as Cartas propagam `ADR-0018` e `ADR-0019`, **nao** `ADR-0022` | **Sim** — `H-A`, `H-N`, `H-P` e diff literal em §2, §3 e §4 | **Sim** — recusar este pacote **nao afeta** `FND-11` |
| **`FND-11` + `FND-01` + `FND-03`** *([PS-2026-009](pacote-soberano-2026-07-29-fnd-11.md))* | **Sim** | **Sim** | **Sim** — recusar aquele **nao afeta** as Cartas |

**Prova textual:** **nenhuma linha dos dois candidatos de Carta cita `FND-11` ou `ADR-0022`** —
verificavel por `grep`. **A ordem entre os pacotes e indiferente.**

## 7. Impacto — a verificacao que importa

| Verificacao | Resultado | Evidencia |
|---|---|---|
| **Titulares criados** | **ZERO** | §3.3 — cada linha nova cita a fonte anterior |
| **Materias que mudam de titular** | **ZERO.** As duas mudaram em **2026-07-29**, por `ADR-0018` e `ADR-0019` | §1 de ADR-0023 |
| **Portoes** | **7 antes · 7 depois · 0 criados · 0 removidos** | §3.3 |
| **Direitos de decisao de `FND-01 §7.3`** | **ZERO alterados** — *escopo e prioridade de produto* segue **decide DEP-PRD, homologa DEP-EXE** | `0` bytes em `FND-01` |
| **Principios Imutaveis** | **ZERO alterados** — **`PI-05` e restaurado nas duas Cartas** | — |
| **Linhas Vermelhas** | **ZERO alteradas** — **`LV-03` deixa de ter caso permanente** | — |
| **Fontes de `foundation/` emendadas** | **ZERO** | `sha256` inalterado |
| **Cartas alteradas** | **2 de 9** | §4.1 |
| **Impedimentos novos** | **2** — `I-12` e `I-10`. **Impedimento restringe; nao concede** | §2.3, §3.2 |
| **Riscos** | **1 novo** *(`RX-8`)* · **1 declarado extinto** *(`RP-1`)*, **conservado** | `MM-09` |
| **Indicadores** | **1 novo** *(`KX-15`)* · **1 retitulado** *(`KP-6`)* — **os dois valem `0`, e o motivo e `RD-33`** | `LM-01` |
| **Artefatos `M1` editados** | **ZERO** | — |
| **Excecoes formais** | **ZERO criadas** | `governance/exceptions/` vazio |
| **Custo de contexto** | **+41 linhas** em duas Cartas `missao`. Recorte de decisao: **130 → 145** e **155 → 172** — **medido por `sed`+`wc -l`** | `CE-02` |
| Reversibilidade | **Tipo 2**, com `H-A` das versoes substituidas publicado em §4.1 | [ADR-0023 §11](../decisions/ADR-0023-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md) |

## 8. Risco residual

| # | Risco | Sev. | Mitigacao declarada |
|---|---|---|---|
| **RS-1** | **Lido como transferencia de poder a `DEP-EXE`** | Media | Cada linha cita a fonte; **`I-10`** veda decidir conteudo da `Spec`; `I-5` intacto; a nota de `E4` declara *"liberar nao e aprovar"* |
| **RS-2** | **`DEP-PRD` lido como esvaziado** | Media | `P3` **nomeia** o que ele mantem: escopo, criterio de aceite, autoria e **aprovacao de `C0`/`C1`** |
| **RS-3** | **`RD-37` lido como esquecimento** | **Alta** | §5, com texto literal, dono, gatilho e **custo por linha** |
| **RS-4** | **`QG-1` virar gargalo em `DEP-EXE`** | Media | `RX-8`, com mitigacao declarada. **`0` liberacoes ocorreram** — `KX-15` |
| **RS-5** | **Aplicar so uma das duas Cartas** | **Alta se ocorrer** | §1: **nao ha aprovacao parcial util**, e a razao e simetrica |
| **RS-6** | **Ato nao vir** | Media | **`LV-03` mitiga e nao cumpre.** As 8 afirmacoes falsas permanecem, e a primeira `Spec` recebera resposta errada pelas Cartas. **Atenuante real: `0` Specs existem** (`RD-33`), logo o defeito **nunca produziu efeito pratico** |

## 9. Minuta do ato — **pronta, com os valores verificados**

> ### Esta secao **nao e um ato**. Nada aqui produz efeito.

```
ATO SOBERANO DO FUNDADOR — <data do ato>

Apos revisar governance/pacote-soberano-2026-07-29-rd-31.md, RFC-0019, ADR-0023,
os candidatos, os diffs literais, as evidencias, a revisao independente, os riscos
e as ressalvas:

Aprovo expressamente:

- ADR-0023, versao 1.0.0,
  SHA-256 3f8886d6892954c4a6f5703fe1b272290fc4165a7175fd4289d46b04f2907e51.

Aprovo e ratifico expressamente, autorizando a aplicacao:

- DEP-PRD, versao 1.1.0,
  SHA-256 09d076dd305e2bd8cc2119772706141cdcfef998cd3ba9e7540267909699fb24,
  cujo SHA-256 apos a transicao de estado devera ser
  0e98511630faf9d5bec4c7cb36d8a37fa0bf15506dfde36954f0419e2720fc15;

- DEP-EXE, versao 1.1.0,
  SHA-256 975e26dbf3f7f8760af01310b27b6b7e1667593d3dc12b520aeed9981013f25b,
  cujo SHA-256 apos a transicao de estado devera ser
  a75a1ffea140e1f962e97b5b8772df70cf28831df882a25cf804b4e931f17e12,

exatamente nos diffs literais registrados em PS-2026-010 §2 e §3.

A entrada em vigor depende de verificacao independente de identidade, versao, hash
integral, diff literal, revisao e inexistencia de alteracao entre o candidato revisado
e o objeto a ser aplicado. DEP-PRD 1.0.0 e DEP-EXE 1.0.0 deverao permanecer
recuperaveis como versoes historicas substituidas.

Este ato nao cria titular, portao, papel, classe, verbo de autoridade, entidade ou
tipo documental novo; nao altera direito de decisao de FND-01 §7.3, principio imutavel,
linha vermelha ou nivel da hierarquia normativa; nao reabre ADR-0018 nem ADR-0019; nao
emenda documento fundacional algum; nao altera o vinculo entre Spec e Produto; nao
alcanca as Cartas de DEP-OPS, DEP-GRW, DEP-TLS, DEP-ENG, DEP-QAR, DEP-GOV nem DEP-KMS;
nao edita ADR, MSG, FIT ou baseline; nao alcanca RD-27, RD-33, RD-36, RD-37 nem
qualquer outro achado; e nao alcanca qualquer objeto nao enumerado expressamente.
```

### 9.1 A escolha que o ato pode fazer diferente — estender a `RD-37`

| # | Escolha | Como se expressa |
|---|---|---|
| **Q1** | **Estender a `DEP-OPS`, `DEP-GRW` e `DEP-TLS`** | O ato **nao pode** faze-lo diretamente: **nao ha candidato nem `H-A` medido** para essas tres. O caminho e **determinar a extensao**, e os tres candidatos de **uma linha cada** sao produzidos e submetidos em pacote proprio. **Custo estimado por analogia, e declarado como estimativa:** 1 ADR + 3 candidatos + 1 pacote |
| **Q2** | Aprovar `ADR-0023` **sem** ratificar as Cartas | **Possivel e inutil:** o `ADR` aprovado sem as Cartas **nao corrige nada** — as Cartas so mudam por ato (`DC-09`) |

## 10. Recomendacao

| Campo | Conteudo |
|---|---|
| **Recomendacao** | **APROVAR** os tres objetos |
| **Fundamento** | **Nada e decidido: tudo e propagado.** As duas autoridades foram **ratificadas em 2026-07-29** e as fontes **ja estao corretas**; o que falta e a cascata que `ADR-0018 §7` declarou **devida, com dono e gatilho** — e **o gatilho ja disparou**. O efeito e verificavel: a pergunta *"quem libera `QG-1`?"* passa a ter **a mesma resposta pelos dois caminhos**, e `QG-1` passa a ter **titular declarado em Carta**, onde hoje tem **`0` ocorrencias** |
| **Contrapartida honesta** | **`RD-37` fica aberto:** o acervo sai de **11 afirmacoes falsas em 4 Cartas** para **3 em 3**. **E melhora medida, nao fechamento** — e a diferenca e **escopo determinado, com o custo publicado** |
| **O pacote informa; nao decide** | **Nao decidir e resultado valido.** O efeito de nao decidir esta em §1, e o atenuante em `RS-6`: **`0` Specs existem**, logo o defeito **nunca produziu efeito pratico** |

## 11. Rastreabilidade

| Campo | Conteudo |
|---|---|
| RFC → ADR | [RFC-0019](../rfcs/RFC-0019-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md) → [ADR-0023](../decisions/ADR-0023-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md) |
| Achado que fecha | **`RD-31`**, quanto as duas Cartas determinadas — [catalogo §7, item 52](artifact-registry.md) |
| Ressalva que fecha | **`R3`** de [FIT-2026-015](fitness/FIT-2026-015-framework-de-specifications.md) |
| Achado que fecha de passagem | **`RD-41`** — a `Spec` alojada em `projects/` |
| Achado que abre | **`RD-37`** — **3** Cartas, **3** afirmacoes falsas, **nao corrigidas** |
| Decisoes propagadas | [ADR-0018](../decisions/ADR-0018-liberacao-do-portao-qg-1.md) · [ADR-0019](../decisions/ADR-0019-aprovador-e-ratificador-de-spec.md) — **ratificadas, nao reabertas** |
| Cascata declarada devida que consome | [ADR-0018 §7](../decisions/ADR-0018-liberacao-do-portao-qg-1.md) · [PS-2026-007 §5](pacote-soberano-2026-07-29-rd-14.md) |
| Regra de integridade | [ADR-0012](../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md), `IR-01` a `IR-10` |
| Pacote irmao, **nao alcancado por este** | [PS-2026-009](pacote-soberano-2026-07-29-fnd-11.md) |
| Relatorio da missao | [PT-2026-008](relatorio-transicao-2026-07-29-canonizacao.md) |
| Verificacao de aptidao | [FIT-2026-016](fitness/FIT-2026-016-canonizacao-e-propagacao.md) |
| Baseline vigente na submissao | **`BL-2026-07-29-09`** |

---

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-EXE | Pacote da **Missao 1.13.1**: emenda **C2 · Tipo 2** das Cartas de **`DEP-PRD`** *(429 → 445 linhas, 21 blocos de diff)* e **`DEP-EXE`** *(481 → 506, 21 blocos)*, propagando `ADR-0018` e `ADR-0019` e fechando **`RD-31`** quanto as duas Cartas determinadas. **Oitavo pacote soberano, e o primeiro cujo autor e `DEP-EXE`.** Publica o **texto literal do antes** das **oito** afirmacoes falsas, o `H-A` e o `H-N` de base e candidato, o **`H-P` projetado** das duas Cartas, `IR-09` executado *(3 de 3 reproduzem)* e **minuta preenchida**. **`QG-1` passa de `0` ocorrencias na Carta de `DEP-EXE` a 22, em 16 linhas**, e o acervo passa de **`0` de 9** a **`2` de 9** Cartas com titular do portao declarado. **§5 registra `RD-37`:** a medicao das **nove** Cartas — e nao das duas — encontrou a **mesma afirmacao falsa** em `DEP-OPS`, `DEP-GRW` e `DEP-TLS`, **nunca enumeradas**; o acervo sai de **11 afirmacoes falsas em 4 Cartas para 3 em 3**, e a diferenca e **escopo determinado, nao merito**, com o custo publicado — **uma linha por Carta**. Registra que **`DEP-ENG` foi revisada e nao entra por nao haver o que corrigir**. §6 verifica a **independencia dos objetos** exigida pela missao, por prova textual. **`0` titulares · `0` portoes · `0` papeis · `0` classes · `0` verbos · `0` direitos decisorios criados · `0` bytes em `foundation/` · 7 portoes antes e depois · `RP-1` conservado e declarado extinto na fonte (`MM-09`) · `0` artefatos `M1` editados.** Aprovado por **DEP-GOV** porque `DEP-EXE`, aprovador natural de `C2`, **e o autor** — precedente `FIT-2026-003`. |
