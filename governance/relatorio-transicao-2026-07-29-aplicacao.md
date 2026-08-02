---
id: PT-2026-005
titulo: Relatorio de transicao da aplicacao integral do sexto ato soberano e da prova final de autoridade
tipo: relatorio
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-07-29
atualizado_em: 2026-07-29
revisao_prevista: null
decisoes_relacionadas: [ADR-0012, ADR-0016, ADR-0017, ADR-0018, ADR-0019]
substitui: []
substituido_por: null
canal: REPORTE
emissor: DEP-GOV
destinatario: SOBERANO
ttl: ate a proxima missao
resumo: Registra a aplicacao integral dos dez objetos do sexto ato soberano na ordem obrigatoria, a verificacao das condicoes de eficacia, a reexecucao da prova de consumo por Specs sobre as fontes vigentes, os achados novos e a decisao sobre a liberacao GO-TO-SPECS conforme as oito condicoes do ato.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# PT-2026-005 — Aplicacao do sexto ato soberano e prova final

> ## Decisao desta missao: **`GO-TO-SPECS` NAO AUTORIZADO**
>
> **A aplicacao foi integral e esta provada.** Os **dez objetos vigoram**, e as **oito condicoes
> de §X foram testadas uma a uma: seis passam integralmente, uma e parcial, uma falha.**
>
> **A que falha e a condicao 6**, e ela falha por **uma clausula especifica de §IX**, nao pela
> contagem de celulas: **as 55 celulas respondem**, mas **duas das dez titularidades que o ato
> manda identificar — promulgacao e ativacao — nao estao declaradas em fonte alguma do
> acervo** *(`RD-22`)*. **A parcial e a condicao 7:** o catalogo foi reconciliado em tudo o que
> este ato mudou e em **13 valores pre-existentes**, mas **§2.1 nao e reproduzivel das fontes**
> e ficou **declaradamente nao reconciliada** *(`RD-26`)*.
>
> O proprio ato determina o que fazer neste caso: *"Falhando qualquer condicao, GO-TO-SPECS nao
> esta autorizado e o estado devera refletir o bloqueio ou ajuste real."* **E o que este
> relatorio faz.** O achado e novo, tem numero, dono e gatilho: **`RD-22`**, §5.3.

## Proposito
Registrar o que foi aplicado, em que ordem, com que prova, o que a prova final mediu sobre as
**fontes vigentes** — nao em sandbox — e por que `GO-TO-SPECS` **nao** esta autorizado.

## Escopo
| Item | Definicao |
|---|---|
| Inclui | A aplicacao dos **dez** objetos; as **10** verificacoes de eficacia; a **prova de consumo por Specs** reexecutada sobre as fontes vigentes; **cinco** achados novos *(`RD-22` a `RD-26`)*; a decisao de §X |
| **Nao** inclui | O **merito** das emendas *(PS-2026-004 a PS-2026-008)* · o **tratamento** de `RD-22`, `RD-23`, `RD-24` e `RD-26`, que exige rito proprio · qualquer objeto que o ato exclui |
| Natureza | **Reporte**, tipo documental de [FND-10 §4.6](../foundation/10-artifact-framework.md), entidade `MSG`. **Nenhum** tipo, entidade, camada, template ou diretorio novo |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| **Aplica** | **DEP-GOV** | Guardiao normativo; `DEP-GOV §7` — registra o ato, nunca o emite |
| **Verifica** | **DEP-QAR** | FND-10 §10.5; `IR-09` |
| **Nao participa da verificacao** | **DEP-EXE** | Autor das nove Cartas |
| **DECIDE sobre `GO-TO-SPECS`** | **SOBERANO** | §X do ato fixou as condicoes; este relatorio **apura**, nao decide |

> **Residuo declarado (PI-10).** **DEP-GOV aplicou e DEP-GOV redige este relatorio.** A revisao
> e de **DEP-QAR**, e o julgamento da autoridade de DEP-GOV e do **SOBERANO**. **Quinta
> ocorrencia da familia de `RC-02`**; permanece **declarado, nao resolvido**.

---

## 1. O que foi aplicado

**Dez objetos, na ordem literal de §V do ato.** Detalhe criptografico completo em
[MSG-2026-0006 §2](../memory/operacional/MSG-2026-0006-ato-soberano-aplicacao-integral.md).

| Etapa | Objeto | De | Para | Linhas | Operacao |
|---|---|---|---|---|---|
| **1** | `DEP-KMS` | 1.0.0 | **1.1.0** | 460 → **464** | Emenda MENOR + **`O4`** |
| **1** | `DEP-ENG` | 1.0.0 | **1.1.0** | 400 → **402** | Emenda MENOR + **`O4`** |
| **2** | `FND-02` | 1.2.0 | **1.3.0** | 479 → **518** | Emenda **C3** |
| **2** | `ADR-0016` | `em-revisao`/`pendente` | **`ativo`/`ratificada`** | 243 | **`O4`** |
| **3** | `FND-01` | 1.4.0 | **1.5.0** | 475 → **485** | Emenda **C3** |
| **3** | `ADR-0018` | `em-revisao`/`pendente` | **`ativo`/`ratificada`** | 243 | **`O4`** |
| **4** | `FND-09` | 1.3.0 | **1.5.0 cumulativa** | 1.243 → **1.263** | Emenda **C3** dupla, em uma etapa |
| **4** | `FND-10` | 1.2.0 | **1.4.0 cumulativa** | 764 → **778** | Emenda **C3** dupla, em uma etapa |
| **4** | `ADR-0017` | `em-revisao`/`pendente` | **`ativo`/`ratificada`** | 228 | **`O4`** |
| **4** | `ADR-0019` | `em-revisao`/`pendente` | **`ativo`/`ratificada`** | 251 | **`O4`** |

### 1.1 A transicao `O4` foi **determinada**, nao suposta

O ato publicou **quatro `H-P` projetados** para os `ADR` e **dois** para as Cartas, e proibiu a
aplicacao de qualquer objeto cujo `H-P` nao reproduzisse o valor projetado. **Antes de escrever
qualquer arquivo**, as variantes possiveis de `O4` foram construidas em area de trabalho e
medidas:

| Variante testada | Reproduz o `H-P` projetado? |
|---|---|
| So `status: em-revisao` → `ativo` | ❌ **Nao**, em 4 de 4 `ADR` |
| `status` **e** `ratificacao: pendente` → `ratificada` | ✅ **Sim, em 6 de 6** — os 4 `ADR` e as 2 Cartas, nos 64 digitos |

**A transicao autorizada, portanto, e exatamente o par de campos** — e isso foi **provado por
reproducao**, nao lido de uma instrucao. `atualizado_em` **nao** foi tocado em objeto algum:
altera-lo produziria hash diferente do projetado, o que o ato proibe.

### 1.2 `FND-09` e `FND-10` — uma etapa, nunca duas

O ato vedou aplicar os dois em etapas separadas e autorizou **somente** os cumulativos. As
versoes **`FND-09` 1.4.0** e **`FND-10` 1.3.0** **nunca existiram como arquivo** — o que existe
delas sao as **linhas de historico dentro do proprio candidato cumulativo**, que e a forma em
que §III as admite: *"evidencias da composicao"*. **`RD-19` nao se repetiu:** os pacotes
concorrentes foram resolvidos pelo cumulativo, e nao por dois hashes que nenhum objeto
aplicavel reproduziria.

## 2. Verificacao das condicoes de eficacia — **10 de 10**

Cinco antes de qualquer escrita, cinco depois de cada aplicacao. Metodo e valores em
[MSG-2026-0006 §3 e §5](../memory/operacional/MSG-2026-0006-ato-soberano-aplicacao-integral.md).

| # | Exigencia | Resultado |
|---|---|---|
| **A1** | Copia datada integral fora do repositorio | ✅ **531 arquivos**, reconferida **na copia**: **157 · 43.498 · `f9859941…3fba`** |
| **A2** | Reproducao da baseline vigente | ✅ **`BL-2026-07-29-06` reproduz** pelo comando publicado |
| **A3** | ID, versao, caminho, linhas, `H-A` dos dez | ✅ **10 de 10** |
| **A4** | Correspondencia com os diffs autorizados | ✅ **6 de 6**, pelos **dois extremos fixados por hash** |
| **A5** | Candidatos identicos aos objetos revisados | ✅ **6 de 6 intocados** |
| **B1** | `H-A`, `H-N`, `H-P` conforme `IR-07` | ✅ **30 hashes** medidos no acervo |
| **B2** | `IR-09` — reconstrucao | ✅ **6 de 6 reproduzem `H-A`**; vacuo nos 4 fundacionais, por `H-P` = `H-A` |
| **B3** | Nenhum conteudo fora do diff autorizado | ✅ **exatamente 10** arquivos diferem; **0 criados · 0 removidos** |
| **B4** | Versao substituida e recuperabilidade | ✅ **6 de 6** pelas quatro vias |
| **B5** | `H-N` invariante sob `O4` | ✅ **6 de 6** |

**Zero divergencias. Zero objetos bloqueados. Zero incidentes abertos.**

> **Por que `A4` e mais forte do que comparar contagem de blocos.** O candidato de cada objeto
> reproduz o `H-A` **do ato**, e o arquivo que estava no acervo reproduzia o `H-A` **"em vigor"
> publicado no pacote**. Com os **dois extremos fixados criptograficamente**, o diff entre eles
> **e** o diff autorizado — nao ha terceira possibilidade. A contagem de blocos de `diff`, por
> contraste, depende de convencao: em `FND-02` o pacote declara *"57 acrescentadas · 18
> substituidas"* e a ferramenta mede **55 e 16**, porque `diff` alinhou como contexto duas
> linhas que a redacao contou como substituidas. **As duas leituras dao o mesmo delta de +39 e
> o mesmo arquivo final**, e o hash decide. **A convencao divergente foi medida e esta
> declarada aqui, nao escondida.**

## 3. Estado normativo apos a aplicacao

| Fonte | Antes | **Agora** |
|---|---|---|
| **FND-01 §6.2** — quem libera `QG-1` | `DEP-PRD` *(quem produz a Spec)* | **`DEP-EXE`** + nota que distingue **liberar portao** de **aprovar artefato** |
| **FND-02 §4** — matriz de interacao | Legenda de 2 linhas, 5 codigos, sem semantica | **§4.1 a §4.5**: 6 codigos com definicao operacional, **12 celulas corrigidas**, **MI-01 a MI-06**, 5 exemplos normativos |
| **FND-09 §8.2** — linha `SPC` | *Aprova:* `DEP-PRD (QG-1)` · *Ratifica:* `—` | ***Aprova:* `conforme classe (FND-04 §2)`** · ***Ratifica:* `SOBERANO se C3 ou Tipo 1`** + **conflito registrado como erro da tabela** |
| **FND-09 §8.2** — linha `FIT` | *Ratifica:* `SOBERANO se C3` | ***Ratifica:* `—` (`FT-10`)** + nota que distingue parecer de mudanca avaliada |
| **FND-10 §10.3** — linhas `Spec` e `Fitness Check` | idem, em projecao divergente | **Acompanham a fonte**, com duas notas de cascata (CV-04) |
| **DEP-KMS** | Sem nenhuma linha sobre incidente | **§4, §7 e `I-11`** declaram o papel diante de incidente. **`RC-05` FECHADO** |
| **DEP-ENG** | Sem o impedimento sobre a propria Carta | **`I-9`** declarado, como nas outras oito. **`RC-07` FECHADO** |

**Seis achados fechados com evidencia na fonte:** `RD-02`, `RD-09`, `RD-14`, `RD-15`, `RC-05`,
`RC-07`.

> **Fechados, nao renomeados.** Cada um tinha uma condicao escrita na propria ressalva, e a
> condicao foi testada contra a fonte vigente — nao contra o pacote. `RD-14` fecha porque
> `FND-01 §6.2` **hoje** diz `DEP-EXE`; `RD-15` fecha porque `FND-09 §8.2` **hoje** remete a
> classe. Nenhum foi reclassificado para melhorar a metrica.

## 4. Prova final de autoridade — reexecutada sobre as **fontes vigentes**

**§IX do ato exigiu a reexecucao sobre o acervo vigente e declarou que sandbox nao substitui.**
A execucao anterior — [PT-2026-004 §E6](relatorio-transicao-2026-07-29-ratificacao.md) —
resolveu as 55 celulas contra **fontes simuladas**. Esta resolve contra **as fontes reais, ja
emendadas**.

**Metodo.** Cinco casos *(C0/T2, C1/T2, C2/T2, C2/T1, C3/T1)* × **onze atos** = **55 celulas**.
Cada celula e resolvida **citando a fonte viva que a responde**. `C1/T1` nao e testado porque
**a celula nao existe**: FND-04 §2.2 determina que C1 Tipo 1 **escala e vira C2**.

### 4.1 As 55 celulas contra as fontes vigentes

| Ato | **C0/T2** | **C1/T2** | **C2/T2** | **C2/T1** | **C3/T1** | Fonte viva que responde |
|---|---|---|---|---|---|---|
| **Propoe** | DEP-PRD | DEP-PRD | DEP-PRD | DEP-PRD | DEP-PRD | FND-09 §8.2, `SPC`, col. *Propoe / cria* |
| **Escreve** | DEP-PRD | DEP-PRD | DEP-PRD | DEP-PRD | DEP-PRD | idem |
| **Revisa** | ENG+QAR | ENG+QAR | ENG+QAR | ENG+QAR | ENG+QAR | idem, col. *Revisa* |
| **Libera `QG-1`** | **DEP-EXE** | **DEP-EXE** | **DEP-EXE** | **DEP-EXE** | **DEP-EXE** | **FND-01 §6.2 — vigente** |
| **Aprova** | proprietario | proprietario + revisor | **DEP-EXE** + parecer GOV | **DEP-EXE** + parecer GOV | **SOBERANO** | **FND-09 §8.2 `conforme classe`** → FND-04 §2 e §2.1 |
| **Veta** | DEP-QAR | DEP-QAR | DEP-QAR | DEP-QAR | DEP-QAR | **FND-02 §4.2, linha `QAR`, codigo `V`**; §4.4 R2; LV-09 |
| **Ratifica** | — | — | — | **SOBERANO** | **SOBERANO** | **FND-09 §8.2 `SOBERANO se C3 ou Tipo 1`**; FND-04 §2.2 |
| **Promulga** | *(segue o aprovador)* | *(segue o aprovador)* | *(segue o aprovador)* | *(apos o ato)* | *(apos o ato)* | ⚠️ **FND-10 §5.2 `O4` — declara a operacao e o criterio, NAO o titular** |
| **Ativa** | `status: ativo` | `status: ativo` | `status: ativo` | apos `ratificada` | apos `ratificada` | ⚠️ **FND-10 §5.4 — declara a condicao, NAO o titular** |
| **Supera** | nova versao | Nota de Decisao | ADR que supere | ADR + ato | ADR + ato | FND-01 §7.1.5; FND-10 `O6`; FND-09 §8.2 col. *Aposenta* = DEP-PRD |
| **Registra** | `atualizado_em` + CORRECAO | Nota + MEM OPR | ADR + afetados | ADR + `MSG` | ADR + `MSG` | FND-04 §2, col. *Registro*; `DEP-GOV G-10`; LM-05 |

**Contagem: 55 de 55 celulas respondem · 0 indeterminadas.** Toda celula produz **uma** resposta
a partir de fonte viva. **45 delas nomeiam um titular declarado**; **10 — as linhas *Promulga* e
*Ativa* — respondem por regra e condicao declaradas, sem titular declarado.** A distincao esta
em §5.3.

### 4.2 Impedimento e escalonamento

| # | Caso | Resposta da fonte viva | Deterministico? |
|---|---|---|---|
| **I-A** | Simples — DEP-PRD seria revisor da propria Spec | **`DEP-PRD I-2`** → **DEP-ENG + DEP-QAR** | ✅ |
| **I-B** | Simples — DEP-PRD verificaria a propria spec | **`DEP-PRD I-1`** → **DEP-QAR** em `QG-3` | ✅ |
| **I-C** | **Duplo** — aprovador e parecerista impedidos | **`DEP-EXE I-2`** → DEP-GOV; se impedido → **SOBERANO**. Terminus literal | ✅ **com custo** |
| **I-D** | Ausencia de titular | **`AU-09`** — autoridade nao declarada **nao existe**; na duvida escala-se (`EC-01`) | ✅ |
| **I-E** | **Conflito entre fontes** | Precedencia de FND-09 §8.2: prevalece a origem **e o conflito e registrado como erro da tabela**. **As duas metades sao cumpriveis agora** — a segunda foi exercida na propria nota da linha `SPC` | ✅ **pela primeira vez integral** |
| **I-F** | **Escalonamento — 6 caminhos** | **6 de 6 tem alvo determinado.** O de aprovacao C2/C3 fecha com `ADR-0019` vigente; o de `PRD → TLS` tem alvo certo *(DEP-TLS)* mas **rota contestada** — **`RD-10`, aberto, de Carta e nao de portao** | ✅ **6 de 6**, com `RD-10` aberto |

### 4.3 Autoverificacao — medida, nao presumida

| Evidencia | Valor medido |
|---|---|
| Artefatos com `autor` **e** `revisor` | **96** |
| Coincidencias `autor` = `revisor` | **0** |
| `QG-1` liberado por quem produz a Spec | ❌ **deixou de ocorrer** — `DEP-EXE` libera, `DEP-PRD` produz |

**`S3` de PT-2026-003 passa na fonte, e nao no papel.** Era a unica exigencia da prova que
estava em **falha aberta**, e a causa era normativa: o portao era liberado por quem o produz.

### 4.4 Veredito da prova, exigencia por exigencia de §IX

| Exigencia de §IX | Resultado sobre as fontes vigentes |
|---|---|
| **55 de 55 celulas deterministicas** | ✅ **55 de 55** |
| **Zero celulas indeterminadas** | ✅ **0** |
| **Zero autoverificacao** | ✅ **96 artefatos · 0 coincidencias**; `QG-1` corrigido na fonte |
| **Impedimentos e escalonamentos deterministas** | ✅ **I-A a I-F**; **6 de 6** escalonamentos, com `RD-10` **declarado aberto** |
| **Titulares de proposta, autoria, revisao, aprovacao, veto, ratificacao, promulgacao, ativacao, superacao e registro identificados sem interpretacao informal** | ❌ **8 das 10 titularidades sim; `promulgacao` e `ativacao` NAO** — §5.3 |

**Quatro das cinco exigencias: satisfeitas. A quinta: nao.**

## 5. Achados

### 5.1 Achado `RD-23` *(Achado A)* — `TPL-spec` fora da cascata de `ADR-0019`

| Campo | Conteudo |
|---|---|
| **Objeto** | `foundation/templates/TPL-spec.md` — **132** linhas, **1.0.0**, `ativo` |
| **Defeito** | O esqueleto fixa `autor: DEP-PRD` **e** `aprovador: DEP-PRD`, e **nao tem campo `ratificacao`**. Com `ADR-0019` **agora vigente**, o esqueleto **contradiz a fonte**: aprovacao segue a **classe** e a ratificacao e do **SOBERANO** se C3 ou Tipo 1 |
| **Por que nao foi corrigido** | **§VIII do ato exclui `TPL-spec` expressamente.** Corrigi-lo seria emenda nao autorizada |
| **Causa da omissao** | A medicao do *"conjunto estreito"* em [PT-2026-004 §3.1](relatorio-transicao-2026-07-29-ratificacao.md) procurou **afirmacao em prosa** e nao **valor em frontmatter de template** — por isso achou **1** artefato e nao **2** |
| Severidade · dono · gatilho | **Alta** — o defeito passa a existir **no instante em que `ADR-0019` vigora** · **DEP-GOV** · **antes de qualquer Spec ser criada** |
| **Estado** | **ABERTO e registrado.** Deixa de existir apenas na memoria de sessao |

### 5.2 Achado `RD-24` *(Achado B)* — §10.2 do catalogo nao reproduz

| Campo | Conteudo |
|---|---|
| **Objeto** | [`governance/artifact-registry.md` §10.2](artifact-registry.md) |
| **Defeito** | Para `BL-2026-07-29-06`, §10.2 declara **155 artefatos / 42.785 linhas** — que sao os valores de `BL-05` —, enquanto o comando que a propria linha publica devolve **157 / 43.498**, que e o que o cabecalho §10.0 declara. **A impressao digital reproduz**; o que divergia era a contagem ao lado dela |
| **Verificado por ferramenta** | ✅ Reproduzido nesta missao **antes** de qualquer edicao: **157 · 43.498 · `f9859941…3fba`** |
| **Por que nao foi corrigido** | Duas razoes independentes: **§VIII do ato exclui o catalogo mestre**, e **`BL-02` proibe editar baseline** — nova medicao recebe **novo identificador** |
| Severidade · dono · gatilho | **Media** · **DEP-GOV** · atendido nesta missao pela emissao de **`BL-2026-07-29-07`**, medida e conferida |
| **Estado** | **ABERTO quanto ao registro historico de `BL-06`**, que **nao** foi tocado. **Setima ocorrencia** da familia de o catalogo divergir de si proprio |

### 5.3 Achado `RD-22` — **`promulgacao` e `ativacao` nao sao titularidades declaradas**

| Campo | Conteudo |
|---|---|
| **Defeito** | §IX do ato manda identificar, *"sem interpretacao informal"*, os titulares de **dez** atos, entre eles **promulgacao** e **ativacao**. **Nenhuma fonte do acervo declara titular para nenhum dos dois** |
| **Evidencia medida** | **(a)** os **cinco verbos de autoridade** de FND-09 §8.1 sao *Criar, Alterar, Aprovar, Consumir, Aposentar* — **`promulgar` nao esta entre eles**; **(b)** a palavra *"promulg"* aparece **3 vezes** em toda a camada normativa *(`foundation/`, `departments/`, `decisions/`)*, **as tres em prosa de ADR descrevendo o rito**, nenhuma declarando titular; **(c)** `FND-10 §5.2` `O4` declara **operacao, transicao, criterio e rollback** — **nao o ator**; **(d)** `FND-10 §5.4` declara a **condicao** de entrada em `ativo` — **nao o ator** |
| **Consequencia** | As **10 celulas** das linhas *Promulga* e *Ativa* respondem por **regra**, nunca por **titular declarado**. Preencher essas celulas com um nome — como *"DEP-GOV apos o ato"* — e **inferencia**, e `AU-09` determina que **autoridade nao declarada em §8.2 nao existe** |
| **Contra-leitura, declarada** | Cabe sustentar que promulgacao e ativacao **nao sao atos autonomos**, e sim a **execucao** de `O4`, cuja autorizacao ja esta nomeada no aprovador ou ratificador. **Essa leitura e defensavel — e e, ela mesma, interpretacao**, que e exatamente o que §IX veda. **A escolha entre as duas e do SOBERANO**, nao deste relatorio |
| Severidade · dono · gatilho | **Alta** — bloqueia a condicao 6 de §X · **DEP-GOV** · **antes de nova tentativa de `GO-TO-SPECS`** |
| **Instrumento adequado** | **RFC → ADR** de classe **C3** *(toca direitos de decisao — FND-04 §2)*, ou **ato soberano** que declare a contra-leitura como norma. **Nenhum dos dois foi criado nesta missao**, por vedacao de §VIII |

> **Este achado nao existia antes do ato — foi o ato que o tornou mensuravel.** Enquanto o
> requisito era *"55 de 55 celulas"*, a prova passava. §IX acrescentou a exigencia de
> **titular por ato**, e e essa clausula que a arquitetura nao cumpre. **Nao e regressao: e
> medicao nova de uma lacuna antiga.**

### 5.4 Divida reconciliada — categoria por categoria

| Achado | Categoria | Evidencia |
|---|---|---|
| `RD-02` · `RD-09` · `RD-14` · `RD-15` | **RESOLVIDA** | Condicao escrita na ressalva testada **contra a fonte vigente**, nao contra o pacote |
| `RC-05` · `RC-07` | **RESOLVIDA** | `DEP-KMS §4/§7/I-11` e `DEP-ENG I-9` vigentes |
| `RD-19` *(pacotes concorrentes)* | **RESOLVIDA** | Cumulativo aplicado; caminho dos candidatos **declarado** em MSG-2026-0006 §3 |
| `RD-17` *(baseline nao reproduzia)* | **MANTIDA RESOLVIDA** | O comando com a lista fechada reproduziu **duas vezes** nesta missao |
| **`RD-23`** *(Achado A — `TPL-spec`)* | **MIGRADA** — de memoria de sessao para **achado numerado no acervo** | §5.1. **Tratada, nao eliminada** |
| **`RD-24`** *(Achado B — §10.2)* | **MIGRADA** + **MANTIDA** | §5.2. O registro de `BL-06` **nao** foi editado |
| **`RD-22`** | **NOVA — ABERTA** | §5.3 |
| **`RD-25`** | **NOVA — RESOLVIDA na projecao** | §7.1. O catalogo §4.3 divergia da fonte em **13 valores**, **11 anteriores a este ato** |
| **`RD-26`** | **NOVA — ABERTA, com lacuna declarada** | §7.2. **61 de 159 artefatos sem `perfil_contexto`**; §2.1 **nao reconciliada, e dito assim** |
| `RD-21` *(reemissao rebaseada de PS-2026-008)* | **RESOLVIDA — perdeu objeto** | O ato alcancou **os dois** pacotes e autorizou **somente o cumulativo**; a minuta nao cumulativa nunca teve efeito |
| `RD-10` · `RD-11` · `RD-12` · `RD-13` · `RD-18` | **MANTIDAS** | Nao enumeradas pelo ato; dono e gatilho inalterados |

**Zero renomeacoes. Zero reclassificacoes. Zero reaberturas.** **Tres achados sairam de
"existem so na memoria" para "existem no acervo"** — e essa mudanca **nao** e progresso de
divida, e progresso de **rastreabilidade**; esta dito assim de proposito.

## 6. As oito condicoes de §X — apuracao

| # | Condicao do ato | Resultado | Evidencia |
|---|---|---|---|
| **1** | Os dez objetos verificados e legitimamente colocados em vigor | ✅ **SIM** | §1; MSG-2026-0006 §2 |
| **2** | Todos os hashes e diffs conferirem | ✅ **SIM** | **30 hashes**; **6 `H-P` projetados reproduzem nos 64 digitos** |
| **3** | Ordem obrigatoria integralmente respeitada | ✅ **SIM** | §1, quatro etapas na ordem literal |
| **4** | Nenhuma alteracao fora do escopo autorizado | ✅ **SIM** | **exatamente 10** arquivos diferem; 0 criados · 0 removidos |
| **5** | `IR-09` passar objeto por objeto | ✅ **SIM** | **6 de 6** reproduzem `H-A`; vacuo nos 4 fundacionais por `H-P` = `H-A` |
| **6** | **A prova final produzir 55/55** | ❌ **NAO INTEGRALMENTE** | **55 de 55 celulas** ✅, mas a **quinta exigencia de §IX falha**: `promulgacao` e `ativacao` **sem titular declarado** — **`RD-22`** |
| **7** | Catalogo, indices e fontes reconciliados | ⚠️ **PARCIAL** | §7 — reconciliado tudo o que este ato mudou, **mais 13 valores pre-existentes de §4.3** *(`RD-25`)*. **`§2.1` do catalogo ficou declaradamente NAO reconciliada** *(`RD-26`)*: a distribuicao por perfil **nao e reproduzivel das fontes**, porque **61 de 159 artefatos nao declaram `perfil_contexto`** |
| **8** | Nova baseline integra emitida | ✅ **SIM** | **`BL-2026-07-29-07`** — [catalogo §10](artifact-registry.md) |

### 6.1 Decisao

> **`GO-TO-SPECS` NAO ESTA AUTORIZADO.**
>
> **Sete das oito condicoes estao satisfeitas.** A condicao **6** nao esta, e o ato e literal
> sobre a consequencia: *"Falhando qualquer condicao, GO-TO-SPECS nao esta autorizado e o estado
> devera refletir o bloqueio ou ajuste real."*
>
> **O que muda em relacao a todas as missoes anteriores:** o bloqueio **deixou de ser falta de
> ato**. Cinco missoes seguidas fecharam por *"falta ato soberano"*. **O ato chegou, foi
> integralmente cumprido, e os dez objetos vigoram.** O que resta e **uma lacuna normativa
> nomeada**, com instrumento identificado — e ela **cabe em um unico rito**.
>
> **Menor caminho para `GO-TO-SPECS`:** decidir `RD-22`. Se o SOBERANO adotar a contra-leitura
> de §5.3 — promulgacao e ativacao **nao** sao atos autonomos, e sim execucao de `O4` sob a
> autoridade de quem aprova ou ratifica —, a condicao 6 fecha **sem emendar fonte alguma**,
> porque a leitura passa a ser **declarada** em vez de inferida. Se preferir declarar o titular
> na fonte, o instrumento e **RFC → ADR C3** sobre FND-09 §8.1 e §8.2.

## 7. Reconciliacao de catalogo, indices e fontes — §X.7

| Objeto | Reconciliado | Natureza |
|---|---|---|
| [Catalogo mestre §4.1](artifact-registry.md) | Versoes e linhas de `FND-01`, `FND-02`, `FND-09`, `FND-10` | **Projecao** (PJ-02) |
| [Catalogo mestre §4.2](artifact-registry.md) | `ADR-0016` a `ADR-0019` → `ativo` · `ratificada` | Projecao |
| [Catalogo mestre §4.3](artifact-registry.md) | `DEP-KMS` **464** · `DEP-ENG` **402**, versao **1.1.0** | Projecao |
| [Catalogo mestre §4.7](artifact-registry.md) | **`MSG-2026-0006`** acrescentado | Projecao |
| [Catalogo mestre §10](artifact-registry.md) | **`BL-2026-07-29-07`** emitida; `BL-06` movida a §10.1 **sem edicao de valor** | **BL-02** |
| [`departments/README`](../departments/README.md) | `DEP-KMS` 460 → **464** · `DEP-ENG` 400 → **402** | Projecao |
| [`foundation/README`](../foundation/README.md) | Versoes dos quatro fundacionais | Projecao |
| [`decisions/README`](../decisions/README.md) | Estado dos quatro `ADR` | Projecao |
| **Fontes** | **Nenhuma alterada pela reconciliacao** | RG-03, PJ-03 |

**A reconciliacao nao corrige defeito de catalogo — ela projeta o novo estado.** O defeito de
§10.2 permanece **aberto e registrado** em §5.2, precisamente porque `BL-02` proibe editar
baseline e §VIII exclui o catalogo do alcance do ato.

### 7.1 Achado `RD-25` — §4.3 do catalogo divergia da fonte em **13** valores

Ao reconciliar §4.3, a comparacao **Carta a Carta contra a fonte medida** encontrou divergencias
que **nao vinham deste ato**:

| Divergencia encontrada | Quantos valores | Origem |
|---|---|---|
| Cinco Cartas declaradas **`em-revisao` · `pendente`** — `DEP-GOV`, `DEP-TLS`, `DEP-PRD`, `DEP-OPS`, `DEP-GRW` — quando estao **`ativo` · `ratificada`** desde [MSG-2026-0004](../memory/operacional/MSG-2026-0004-ato-soberano-cartas-emenda-constitucional-e-regime-do-fitness-check.md) | **10** *(5 linhas × 2 campos)* | **Anterior a este ato — tres missoes de atraso** |
| `DEP-QAR` declarada em **1.1.0 · 387** linhas quando esta em **1.2.0 · 388** | **2** | **Anterior a este ato** |
| Subtotal de linhas de Carta declarado **3.918** quando a soma media era **3.919** | **1** | **Anterior a este ato** |
| `DEP-ENG` **400 → 402** e `DEP-KMS` **460 → 464**, com versao **1.1.0** | **4** | **Deste ato** |

**11 dos 13 valores divergentes sao anteriores a este ato**, e o mais antigo tem **tres missoes**.

| Campo | Conteudo |
|---|---|
| **Achado** | **`RD-25`** — §4.3 do catalogo mestre divergia da fonte em **13** valores |
| Severidade | **Media** — **defeito de projecao, nunca do acervo** (`BL-04`, `PJ-03`, `RG-03`) |
| **Tratamento** | ✅ **CORRIGIDO na projecao**, valor a valor, **medido por ferramenta**. **Zero fontes alteradas** |
| Precedente de forma | **`RD-20`**, que corrigiu **18 de 153** contagens do mesmo modo — *"remedidas uma a uma por ferramenta, zero fontes alteradas"* |
| Familia | **Oitava ocorrencia** de o catalogo divergir de si proprio — IC-8, RE-04, RD-06, RD-16, RD-17, RD-20, `RD-24` e agora esta. **A causa e sempre `CV-04`**: a projecao nao e atualizada pela mesma mudanca que altera a fonte |

> **Por que corrigir §4.3 e permitido, e corrigir §10.2 nao e.** §4.3 e **projecao de estado
> corrente**, e `PJ-03` determina que divergencia entre projecao e fonte e **defeito da
> projecao**, corrigivel nela. §10.2 e **registro historico de uma baseline**, e `BL-02` proibe
> editar baseline — nova medicao recebe **novo identificador**, que e exatamente o que
> `BL-2026-07-29-07` faz. **A distincao nao e conveniencia: e a diferenca entre projetar o
> presente e reescrever o passado.**

### 7.2 Achado `RD-26` — §2.1 do catalogo **nao** foi reconciliada, e a razao esta declarada

A tabela de **custo por perfil de contexto** declara artefatos e linhas por `perfil_contexto`.
Ao tentar reproduzi-la a partir das fontes, a medicao encontrou o seguinte:

| Medicao | Valor |
|---|---|
| Artefatos **sem** `perfil_contexto` no frontmatter | **61 de 159** |
| Onde estao | **24** Cartas de Capability · **23** de `foundation/` *(Templates inclusos)* · 5 de `decisions/` · 4 de `memory/` · 3 de `rfcs/` · 2 de `governance/` |
| Consequencia | A distribuicao de §2.1 **nao deriva do frontmatter**; deriva da **coluna de perfil de §4**, que e projecao |
| Metodo original | **Nao declarado na propria secao** |

**Por isso §2.1 ficou intacta.** Recalcula-la por um metodo diferente do original produziria
numeros novos **sem base para afirmar qual dos dois esta certo** — e escrever o resultado como
fato medido seria **LV-05**, a mesma falha que este acervo ja registrou quatro vezes.

| Campo | Conteudo |
|---|---|
| **Achado** | **`RD-26`** — §2.1 nao e reproduzivel das fontes; **61 de 159** artefatos sem `perfil_contexto` |
| Severidade | **Media** — atinge as afirmacoes **`CE-01`** e **`CE-02`**, que dizem *"medido, nao estimado"* |
| Dono · gatilho | **DEP-GOV** · *"proxima emenda a §2.1 ou a FND-10 §6"* |
| **Estado** | **ABERTO, com lacuna declarada.** E o **unico** item de §X.7 que **nao** foi reconciliado, e por isso a condicao **7** e reportada como **PARCIAL**, nunca como satisfeita |

> **Duas hipoteses, e nenhuma foi medida ainda:** ou **`perfil_contexto` e obrigatorio** e falta
> em 61 artefatos — defeito de acervo, grande —, ou **nao e obrigatorio** para `CAP` e `TPL` e
> §2.1 projeta sem declarar metodo — defeito de projecao, pequeno. **Decidir qual exige ler
> FND-10 §6 e FND-03 contra a lista de tipos, e isso nao foi feito nesta aplicacao.** Registrar a
> duvida com o numero medido e o que o acervo permite afirmar hoje.

## 8. O que deliberadamente **nao** foi feito

| Nao feito | Norma que o impede | Consequencia assumida |
|---|---|---|
| Corrigir `TPL-spec` | **§VIII** exclui expressamente | **`RD-23` aberto** — §5.1 |
| Corrigir §10.2 do catalogo | **§VIII** + **`BL-02`** | **`RD-24` aberto** — §5.2 |
| Declarar titular de promulgacao ou ativacao | Seria **ampliar titular sem rito** — `AU-09`, `AU-10`, `LM-03` | **`RD-22` aberto** — §5.3 |
| Criar `FND-09` 1.4.0 ou `FND-10` 1.3.0 como arquivo | **§III** — nao promulgadas | Existem so como linhas de historico |
| Alterar `atualizado_em` dos `ADR` ou das Cartas | Fora do diff autorizado — `IR-05`; e produziria `H-P` diferente do projetado | Campos preservados |
| Editar qualquer `ADR`, `RFC`, `FIT`, `MSG`, incidente, pacote, revisao, relatorio ou baseline | **§VII** — vedacao expressa | Verificado por `cmp`: **0 tocados** |
| Criar Spec, Skill, Command, Workflow, Agente, Produto, codigo, infraestrutura, ontologia ou migracao | **§VIII** | **Nenhum foi criado** |
| Emitir `FIT` desta aplicacao | **Nao foi determinado pelo ato**, e `FIT` e parecer que **nao se ratifica** (`FT-10`) | A verificacao de aptidao fica para quando houver determinacao |

## 9. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Ato aplicado | [MSG-2026-0006](../memory/operacional/MSG-2026-0006-ato-soberano-aplicacao-integral.md) — **sexto ato soberano** |
| Pacotes consumidos | [PS-2026-004](pacote-soberano-2026-07-29-rd-02.md) · [PS-2026-005](pacote-soberano-2026-07-29-rd-09.md) · [PS-2026-006](pacote-soberano-2026-07-29-kms-eng.md) · [PS-2026-007](pacote-soberano-2026-07-29-rd-14.md) · [PS-2026-008](pacote-soberano-2026-07-29-rd-15.md) — **os cinco, zerando a fila** |
| Prova anterior, em sandbox | [PT-2026-004 §E6](relatorio-transicao-2026-07-29-ratificacao.md) — **substituida**, nao contestada |
| Regra de integridade | [ADR-0012](../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md), `IR-01` a `IR-10` |
| Achados fechados | `RD-02` · `RD-09` · `RD-14` · `RD-15` · `RC-05` · `RC-07` |
| Achados abertos nesta missao | **`RD-22`** *(Alta)* · **`RD-23`** *(Alta)* · **`RD-24`** *(Media)* · **`RD-26`** *(Media)*. **`RD-25`** nasce e fecha na mesma aplicacao |
| Baseline conferida **antes** das edicoes | **`BL-2026-07-29-06`** — reproduzida, **nao editada** (BL-02) |
| Baseline emitida | **`BL-2026-07-29-07`** — [§10](artifact-registry.md) |
| Copia datada | **531** arquivos em `_backups/LucaX-Enterprise-OS_2026-07-29_pre-ato-soberano-06/` (PI-07, AF-35) |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-GOV | Relatorio da **aplicacao integral do sexto ato soberano** — **os dez objetos em vigor**, nas **quatro etapas da ordem obrigatoria**, consumindo os **cinco** pacotes pendentes e **zerando a fila do Soberano pela primeira vez**. **Condicoes de eficacia: 10 de 10.** **30 hashes medidos**; os **seis `H-P` projetados reproduzem nos 64 digitos**, e a transicao `O4` foi **determinada por reproducao** antes de qualquer escrita. **`IR-09` reproduz `H-A` em 6 de 6**; **`H-N` invariante em 6 de 6**; **exatamente 10 arquivos alterados** em todo o acervo. **Seis achados fechados na fonte** — RD-02, RD-09, RD-14, RD-15, RC-05, RC-07. **Prova de consumo reexecutada sobre as fontes vigentes**, nao em sandbox: **55 de 55 celulas · 0 indeterminadas · 96 artefatos com autor e revisor e 0 autoverificacoes · 6 de 6 escalonamentos**, e **`I-E` integral pela primeira vez**. **Decisao: `GO-TO-SPECS` NAO AUTORIZADO** — das **8 condicoes de §X**, **seis passam integralmente, a 7 e parcial e a 6 falha**. A **condicao 6** falha pela **quinta exigencia de §IX**: **`promulgacao` e `ativacao` nao tem titular declarado em fonte alguma** — achado **`RD-22`**, severidade **Alta**, com **contra-leitura declarada** e instrumento identificado. A **condicao 7** e parcial porque **§2.1 do catalogo nao e reproduzivel das fontes** — **61 de 159 artefatos sem `perfil_contexto`**, achado **`RD-26`** — e **nao foi recalculada por metodo inventado**, o que seria LV-05. **Cinco achados novos, `RD-22` a `RD-26`**, dois deles **migrados de memoria de sessao para o acervo** — `RD-23` *(`TPL-spec`)* e `RD-24` *(§10.2)* —, e **`RD-25` nasce e fecha na mesma aplicacao**. **`RD-21` perdeu objeto.** **Primeira missao do acervo cujo bloqueio nao e ausencia de ato soberano.** |
