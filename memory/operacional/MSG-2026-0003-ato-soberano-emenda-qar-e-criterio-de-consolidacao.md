---
id: MSG-2026-0003
titulo: Ato Soberano de ratificacao da emenda DEP-QAR 1.1.0 e de determinacao do criterio de consolidacao
tipo: relatorio
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: SOBERANO
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: null
decisoes_relacionadas: [ADR-0011, ADR-0012, ADR-0013]
substitui: []
substituido_por: null
canal: DIRETIVA
emissor: SOBERANO
destinatario: DEP-GOV
ttl: 1 ciclo — expira sem perda; o efeito duravel foi promovido no mesmo ato (§7)
resumo: Registra, como fonte canonica unica, o ato soberano de 2026-07-28 que ratifica DEP-QAR 1.1.0 e determina o criterio de consolidacao que resolve PS-1.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# MSG-2026-0003 — Ato Soberano sobre a emenda `DEP-QAR` 1.1.0 e o criterio de consolidacao

## Proposito
Registrar **uma unica vez** o ato soberano de 2026-07-28 que ratifica **`DEP-QAR` 1.1.0** e
determina o **criterio de consolidacao** que responde a pendencia **PS-1**, com os IDs, versoes
e hashes que ele vincula. Indices, frontmatters e catalogo **referenciam** esta secao; nenhum a
reproduz (CM-09, PJ-01).

> **Este e o terceiro ato soberano registrado, e tem fonte canonica propria e nao acumulada.**
> O primeiro vive em [MSG-2026-0001](MSG-2026-0001-ato-soberano-ratificacao-cartas-piloto.md); o
> segundo, em [MSG-2026-0002](MSG-2026-0002-ato-soberano-cartas-comando-plataforma-e-contexto.md).
> **Nenhum dos dois foi editado.** Tres atos, tres fontes.

## Escopo
| Item | Definicao |
|---|---|
| Inclui | O ato de 2026-07-28 sobre `DEP-QAR` 1.1.0 e sobre o criterio de consolidacao; seu alcance, sua condicao de eficacia e os efeitos aplicados |
| **Nao** inclui | O **merito** da emenda *(objeto de [REV-ESTRUTURAL-I §7](../../foundation/revisao-estrutural-01-2026-07-28.md), da missao anterior)*; a **formalizacao** do criterio *(objeto de [ADR-0013](../../decisions/ADR-0013-criterio-de-horizonte-e-consolidacao.md))*; qualquer artefato que o ato nao nomeie |
| Instrumento | **Diretiva**, tipo documental de [FND-10 §4.6](../../foundation/10-artifact-framework.md), entidade `MSG`. Nenhum tipo, entidade, camada ou diretorio novo |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| **Emissor** | **SOBERANO** | PI-01 — autoridade final, indelegavel |
| **Registra** | **DEP-GOV** | LM-05, CV-09 |
| **Verifica a eficacia** | **DEP-QAR** | FND-10 §10.5; IR-09 de ADR-0012 |
| **Nao participa da verificacao** | **DEP-EXE** | **Autor da emenda 1.1.0** — verificar a propria ratificacao repetiria a causa de [INC-2026-001](../../governance/incidents/INC-2026-001-ratificacao-inferida.md) |

> **Residuo declarado (PI-10).** `DEP-QAR` e o **objeto** do artefato ratificado e o **executor**
> de `IR-09`. O impedimento **I-5** da propria Carta veda a DEP-QAR *aprovar, revisar ou emendar*
> a Carta — e **nao** veda executar o teste de reconstrucao, que e operacao de medicao sobre
> hash, sem juizo de merito e reproduzivel por terceiro. Ainda assim, o resultado foi **conferido
> de forma independente por DEP-GOV**, e as duas medicoes coincidem. Achado **RC-02** — §9.

---

## 1. O ato

| Campo | Conteudo |
|---|---|
| Emissor | **SOBERANO** (Lucas) |
| Canal | **DIRETIVA** (FND-05 §2) |
| Data do ato | **2026-07-28** |
| Objeto | Tres determinacoes: **(1)** ratificacao de `DEP-QAR` **1.1.0**, vinculada a hash; **(2)** o **criterio de consolidacao** que responde a PS-1; **(3)** a **formalizacao** desse criterio pelo rito aplicavel |
| Natureza | **Aprovacao e ratificacao no mesmo ato** para a Carta — matriz de FND-09 §8.2, linha `DEP` |
| Condicao de eficacia | Entrada em vigor **apos verificacao independente de versao, hash, diff e integridade** |
| Limite expresso | **Nenhuma alteracao posterior esta abrangida.** O ato **nao edita FND-09**, **nao resolve Q1/Q2 de RFC-0009 por inferencia** e **nao ratifica futura emenda C3** |

### 1.1 Texto do ato

> ATO SOBERANO DO FUNDADOR — 2026-07-28
>
> 1. Aprovo e ratifico expressamente DEP-QAR versao 1.1.0, exatamente no conteudo candidato
> produzido e revisado na Missao 1.8, identificado pelo hash SHA-256 integral 3e69441e…a3a0.
>
> Sua entrada em vigor depende da verificacao independente de versao, hash, diff e integridade.
> DEP-QAR 1.0.0 devera ser preservada como versao historica substituida. Nenhuma alteracao
> posterior esta abrangida por este ato.
>
> 2. Quanto a PS-1, determino que o crescimento do acervo seja gatilho de revisao, nao
> obrigacao de consolidacao. Um horizonte torna-se avaliavel quando uma camada concluida for
> consumida por camada posterior ou exercida em prova vertical.
>
> Duplicacao, sobreposicao, conflito de autoridade, degradacao de recuperacao, custo excessivo
> de contexto ou existencia de objeto substituido podem antecipar a revisao.
>
> A revisao podera concluir "nenhum candidato elegivel", desde que apresente avaliacao e
> evidencia individual dos candidatos.
>
> 3. Determino a formalizacao desse criterio pelo rito aplicavel. Este ato nao edita diretamente
> FND-09, nao resolve RFC-0009 Q1/Q2 por inferencia e nao ratifica futura emenda C3.

> **Transcricao literal.** O texto e reproduzido como emitido (LX-07). A elisao `3e69441e…a3a0`
> e do proprio ato; o valor integral esta em §2.

### 1.2 A designacao do objeto — precisa, e por que isso importa

| Campo | Conteudo |
|---|---|
| **O que o ato diz** | *"exatamente no conteudo candidato produzido e revisado na Missao 1.8, identificado pelo hash SHA-256 integral 3e69441e…a3a0"* |
| **Fato verificado** | O pacote de emenda vive em [REV-ESTRUTURAL-I §7](../../foundation/revisao-estrutural-01-2026-07-28.md), que declara o mesmo **H-A** e o **diff completo**. O objeto e determinavel por **tres** identificadores independentes: ID, versao e hash |
| **Diferenca em relacao ao ato anterior** | `MSG-2026-0002 §1.2` registrou uma designacao **imprecisa** de pacote, geradora do achado **RE-01**, cujo gatilho era *"proximo ato soberano — anexar o caminho exato"*. **Este ato identifica o objeto pelo hash integral**, que nao depende de qual arquivo hospeda o pacote |
| **Efeito sobre RE-01** | ✅ **FECHADO.** O mecanismo que RE-01 pedia — identificacao que nao dependa do arquivo — foi exercido. Registrado em [REV-ROLLOUT §6](../../foundation/revisao-arquitetural-rollout-cartas-2026-07-28.md) |

## 2. Objeto vinculado — ID, versao e hashes

Tres hashes distintos, conforme [ADR-0012 §5.2, IR-07](../../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md):
**H-A** hash do arquivo submetido · **H-N** hash do conteudo normativo · **H-P** hash do arquivo
apos a transicao de estado.

| Artefato | ID | Versao | **H-A — arquivo submetido** | **H-N — conteudo normativo** | **H-P — apos O4** | Linhas |
|---|---|---|---|---|---|---|
| Qualidade e Risco *(Guarda)* | **`DEP-QAR`** | **1.1.0** | `3e69441e2acab1cc34ff03da16c9e8bb004b65295736e08f9da53dfe0eaca3a0` | `747862a940eede8a8ece803d0a3d16cd1a0ecdbceef5d7a84fe6c72d78ee4487` | `67407fffa111b7ab4c2910e328013d3d05fd8dcae9455d266eb3fdcf87b3d144` | **387** |

**H-A conferido contra o ato:** o valor medido reproduz **exatamente** o `3e69441e…a3a0` que o
ato vincula, nos oito primeiros e nos quatro ultimos digitos elididos e em **todos** os 64.

### 2.1 A versao substituida — `DEP-QAR` 1.0.0, preservada

O ato determina que **1.0.0 seja preservada como versao historica substituida**. Preservacao
executada por **tres** vias, nenhuma das quais cria um segundo artefato do mesmo departamento:

| Artefato | ID | Versao | **H-A / arquivo** | **H-N — conteudo normativo** | Linhas | Estado |
|---|---|---|---|---|---|---|
| Qualidade e Risco | **`DEP-QAR`** | **1.0.0** | `c591fd62e84216d416c190cd56d5b665b038add5d901866f371a116bb6bc311b` | `250d1289d9c5f19c18b067246f2907fc565c1787895f0967c7a400fcaa628810` | **386** | **Substituida por 1.1.0** |

| # | Via de preservacao | Conteudo |
|---|---|---|
| **PV-1** | **Hash registrado** | Os dois hashes acima. O `c591fd62…c311b` e o mesmo valor que [ADR-0012 §1](../../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md) ja registrava para o arquivo em disco antes desta missao — **conferido, nao recalculado a esmo** |
| **PV-2** | **Reconstrucao byte a byte** | O diff de §7.2 e **completo e literal**. Aplicado em sentido inverso sobre 1.1.0, reproduz 1.0.0 e o seu `c591fd62…c311b`. E o mesmo mecanismo de `IR-09`, executado para tras |
| **PV-3** | **Copia datada fora do acervo** | 117 arquivos, tomados **antes** de qualquer edicao desta missao (PI-07, AF-35). Inclui `departments/qar/carta.md` em 1.0.0, integral |
| **PV-4** | **Historico de versoes** | A linha 1.0.0 permanece na propria Carta 1.1.0, e **nunca sai** (AL-04) |

> **Por que nao se criou `carta-1.0.0.md`.** Um segundo arquivo de Carta no mesmo diretorio
> criaria **duas Cartas do mesmo departamento** — exatamente a duplicacao que
> [FIT-2026-007 §F2.a](../../governance/fitness/FIT-2026-007-revisao-estrutural-i.md) barrou ao
> recusar escrever o texto candidato no acervo. A preservacao exigida pelo ato e de **conteudo
> recuperavel e identificado**, e PV-1 a PV-4 a entregam sem ambiguidade de fonte (MM-01).
> **A escolha esta declarada para que o Soberano possa determinar outra** — §8, item aberto.

## 3. Alcance — o que o ato alcanca e o que **nao** alcanca

Ratificacao **nao se estende por analogia** (LM-03).

| Artefato | Alcancado? | Efeito |
|---|---|---|
| **`DEP-QAR` 1.1.0** | **Sim — ratificado**, no conteudo de `H-A 3e69441e…a3a0` | `em-revisao` → `ativo`; `ratificacao: ratificada` |
| **`DEP-QAR` 1.0.0** | **Sim — declarada substituida e preservada** | §2.1 |
| **Criterio de consolidacao (PS-1)** | **Sim — determinado**, com formalizacao ordenada pelo rito | §4 |
| **FND-09** | **Nao** — *"este ato nao edita diretamente FND-09"* | Nenhuma linha de FND-09 alterada por este ato nem pela formalizacao — [ADR-0013 §7](../../decisions/ADR-0013-criterio-de-horizonte-e-consolidacao.md) |
| **Q1 e Q2 de RFC-0009** | **Nao** — *"nao resolve por inferencia"* | Permanecem **abertas**. §5 |
| **Emenda C3 a FND-01 §7.3** | **Nao** — *"nao ratifica futura emenda C3"* | [ADR-0014](../../decisions/ADR-0014-candidato-emenda-fnd-01-7-3-homologa.md) nasce **candidato, sem vigencia** |
| **As cinco Cartas produzidas nesta missao** | **Nao** | Nasceram **depois** do ato, em `em-revisao` · `ratificacao: pendente`. *"Nenhuma alteracao posterior esta abrangida"* |
| Qualquer versao futura de `DEP-QAR` | **Nao** | Versao nova exige **ato novo** |

> **O ato nao ratifica a Missao 1.8 nem a 1.9.** Ratifica **um texto** e determina **um
> criterio**.

## 4. A determinacao sobre PS-1 — o que ela decide, e o que ela deixa ao rito

| # | O que o ato determina | Natureza |
|---|---|---|
| **D1** | **Crescimento do acervo e gatilho de revisao, nao obrigacao de consolidacao** | Decide o **defeito** que RE-06 nomeou: gatilho e criterio mediam coisas diferentes |
| **D2** | **Um horizonte torna-se avaliavel quando uma camada concluida for consumida por camada posterior ou exercida em prova vertical** | Fornece a **definicao operavel** que FND-09 §12 nunca teve |
| **D3** | Duplicacao, sobreposicao, conflito de autoridade, degradacao de recuperacao, custo excessivo de contexto ou objeto substituido **podem antecipar** a revisao | Seis **antecipadores**, todos observaveis |
| **D4** | *"Nenhum candidato elegivel"* e **resultado valido**, desde que haja **avaliacao e evidencia individual** dos candidatos | Legitima, ex post, o encerramento de **EV-08** como `AJUSTAR` |
| **D5** | **Formalizacao pelo rito aplicavel**, sem editar FND-09 diretamente | Ordena o instrumento; nao o escolhe |

> **D4 nao e retroativo, e por isso nao valida a EV-08 anterior por decreto.** Ele fixa a regra
> para as revisoes **futuras**. O encerramento de EV-08 na Missao 1.8 permanece o que foi:
> `AJUSTAR`, com os quatro candidatos testados um a um em
> [REV-ESTRUTURAL-I §8.2](../../foundation/revisao-estrutural-01-2026-07-28.md) — e e essa
> **evidencia individual**, produzida antes da regra, que **ja satisfazia** o que D4 agora exige.

**Efeito sobre PS-1: RESPONDIDA.** O Soberano escolheu a opcao **(c)** de
[FIT-2026-007 §Pendencia](../../governance/fitness/FIT-2026-007-revisao-estrutural-i.md) —
*determinar outro criterio* —, e nao **(a)** nem **(b)**.

## 5. O que o ato expressamente **nao** resolve

| Questao | Estado apos o ato | Fundamento |
|---|---|---|
| **Q1** — a coluna *Ratifica* de FND-01 §7.3 passa a **Homologa**? | **ABERTA** | *"nao resolve RFC-0009 Q1/Q2 por inferencia"*; *"nao ratifica futura emenda C3"* |
| **Q2** — `FIT` exige ratificacao do Soberano? | **ABERTA** | idem |
| **IC-2** — colisao do termo *"ratifica"* | **CONTIDO, NAO FECHADO** | `IR-11` de ADR-0012 permanece a unica contencao; a causa segue viva em FND-01 §7.3 |

> **A contencao `IR-11` foi exercida nesta missao e o resultado esta medido**, em
> [REV-ROLLOUT §5](../../foundation/revisao-arquitetural-rollout-cartas-2026-07-28.md): varredura
> do acervo por uso do verbo *ratificar*, artefato a artefato. **Ler no silencio do ato uma
> autorizacao para fechar IC-2 seria LM-03** — e o proprio ato o veda por escrito.

## 6. Verificacao independente da condicao de eficacia

Executada por **DEP-QAR** *(medicao e reconstrucao)* e **DEP-GOV** *(forma e conferencia
independente)*. **DEP-EXE, autor da emenda, nao participou.** Executada **antes** de qualquer
edicao desta missao.

| # | O que o ato exigiu | Metodo | Resultado |
|---|---|---|---|
| **W1** | Integridade do **registro** | Reproducao integral da baseline vigente `BL-2026-07-28-05` sobre a copia pre-edicao | **117 artefatos · 30.947 linhas · impressao digital `c9a25651…6c8f`** — as tres reproduzem o valor registrado |
| **W2** | **Versao** do objeto | Frontmatter do candidato contra REV-ESTRUTURAL-I §7.1 | **1.1.0**, conforme declarado. Emenda **MENOR** sobre 1.0.0 (AL-01) |
| **W3** | **Hash SHA-256 integral** | `sha256sum` do arquivo candidato | **`3e69441e2acab1cc…eaca3a0`** — reproduz **exatamente** o hash do ato |
| **W4** | **Diff** | `diff -u` entre `DEP-QAR` 1.0.0 em disco e o candidato, conferido **linha a linha** contra a tabela de [REV-ESTRUTURAL-I §7.2](../../foundation/revisao-estrutural-01-2026-07-28.md) | **8 de 8 itens conferem, e nada alem deles.** 3 campos de frontmatter · 1 linha normativa *(§10, `I-6`, quatro colunas)* · 1 linha de historico. **Zero** alteracoes fora do diff declarado |
| **W5** | **Integridade do texto substituido** | `diff` entre `departments/qar/carta.md` em disco e a copia da baseline anterior | **Identicos.** `DEP-QAR` 1.0.0 nao sofreu nenhuma alteracao entre a Missao 1.8 e este ato |
| **W6** | **Contagem de linhas** | `wc -l` do candidato contra o valor declarado no pacote | **387 = 387** *(386 + 1 linha de historico)* |
| **W7** | **`H-N` invariante sob O4** | `H-N` do candidato × `H-N` do arquivo apos a transicao | **`747862a9…4487` nos dois** — a transicao nao tocou o conteudo normativo (IR-02, IR-06) |
| **W8** | **`IR-09` — reconstrucao do texto ratificado** | Sobre o arquivo em disco **apos** a transicao, reverteu-se **apenas** `status` e `ratificacao`, e mediu-se o SHA-256 | Reconstruido **`3e69441e2acab1cc…eaca3a0`** = **H-A do ato** — **identico** |
| **W9** | Ausencia de **autoverificacao** | Papel de quem verifica × papel de quem produziu | **DEP-QAR** e **DEP-GOV** verificam; **DEP-EXE** produziu. Zero coincidencia (FT-02, RM-06b). Residuo de objeto declarado no bloco Responsaveis |
| **W10** | Ausencia de **credencial** no objeto ratificado | Varredura do artefato | **0 ocorrencias** (PI-08, LV-02) |

**Condicao de eficacia: SATISFEITA.** Dez verificacoes passam, por **cinco vias independentes** —
hash de arquivo, hash de conteudo normativo, diff literal, contagem de linhas e impressao digital
de acervo. **A quarta via, o diff, foi exigida por este ato e nao pelos anteriores**, e e a que
prova que o objeto ratificado e a emenda **e nada alem dela**.

## 7. Efeitos aplicados

| # | Efeito | Onde | Operacao |
|---|---|---|---|
| **E1** | `DEP-QAR`: `versao` `1.0.0` → **`1.1.0`**; `status` `em-revisao` → **`ativo`**; `ratificacao` `pendente` → **`ratificada`** | [`departments/qar/carta.md`](../../departments/qar/carta.md) | **Emenda MENOR + O4** (FND-10 §5.2) |
| **E2** | `IC-5` **corrigido**: a materia de `I-6` passa a nomear **Linha, Plataforma e Comando**, e o substituto passa a ser o **SOBERANO** | `DEP-QAR §10` | Conteudo da emenda |
| **E3** | Criterio de consolidacao **formalizado pelo rito** | [ADR-0013](../../decisions/ADR-0013-criterio-de-horizonte-e-consolidacao.md), precedida de [RFC-0010](../../rfcs/RFC-0010-criterio-de-horizonte-avaliavel.md) | RFC → ADR (FND-04 §2.1, C2) |
| **E4** | Linhas de rastreabilidade, classificacao e baseline atualizadas | [catalogo mestre §4.3.1, §6 e §10](../../governance/artifact-registry.md) | Projecao (PJ-02) |
| **E5** | **PS-1** passa de `escalada` a **`respondida`** | [REV-ROLLOUT §7](../../foundation/revisao-arquitetural-rollout-cartas-2026-07-28.md) | Reconciliacao |
| **E6** | **R2 de FIT-2026-007** e **R4 de FIT-2026-006** reconciliadas | idem | Reconciliacao |
| **E7** | **RE-01** fechado | §1.2 | Fechamento com evidencia |

### 7.1 O efeito duravel foi promovido — por isso o `ttl` desta Diretiva nao ameaca nada

| Fato | Instrumento proprio que passa a guarda-lo | Fonte da regra |
|---|---|---|
| **Estado de ratificacao** de `DEP-QAR` | O campo `ratificacao` do proprio frontmatter | FND-10 §5.4 |
| **Vigencia** | O campo `status` do proprio artefato | FND-10 §5.2, O4 |
| **Vinculo ID × versao × H-A/H-N/H-P** | §2 desta Diretiva, referenciada pelo [catalogo mestre §10](../../governance/artifact-registry.md) | FND-10 §10.4; ADR-0012, IR-07 |
| **Preservacao de 1.0.0** | §2.1 desta Diretiva *(hash + diff reversivel)* e o Historico da propria Carta | AL-04; IR-09 aplicado para tras |
| **Criterio de consolidacao** | [ADR-0013](../../decisions/ADR-0013-criterio-de-horizonte-e-consolidacao.md) — instrumento vigente | FND-04 §2.1 |

### 7.2 Diff exato aplicado, e os hashes resultantes

| Etapa | Campo | Antes | Depois | Linhas |
|---|---|---|---|---|
| **Emenda** *(Missao 1.8, ratificada agora)* | `versao` · `I-6` · Historico | `1.0.0` · materia so com **Linha** · — | **`1.1.0`** · **Linha, Plataforma e Comando** · **+1 linha** | 386 → **387** |
| **Transicao O4** *(aplicada por este ato)* | `status` · `ratificacao` | `em-revisao` · `pendente` | **`ativo`** · **`ratificada`** | 387 → **387** |

> **A transicao O4 nao tocou nenhuma linha de corpo** — a contagem e identica antes e depois, e
> **H-N e invariante** (W7). O que mudou o corpo foi a **emenda**, submetida e ratificada; o que
> mudou o estado foi a **transicao**, que a propria ratificacao obriga a executar.

## 8. O que deliberadamente **nao** foi feito

| Nao feito | Norma que o impede | Consequencia assumida |
|---|---|---|
| Corrigir *"386 linhas"* em `DEP-QAR §13.2`, que a emenda tornou **desatualizado** | O valor esta **dentro de `H-N`**; altera-lo mudaria o conteudo ratificado e exigiria **ato novo** (IR-01, IR-05) | A Carta declara **386** onde o arquivo tem **387**. Achado **RC-01**, com dono e gatilho — §9. **Mesmo mecanismo de RE-02** |
| Criar `departments/qar/carta-1.0.0.md` | MM-01; precedente de FIT-2026-007 §F2.a | Preservacao por hash, diff reversivel e copia datada — §2.1 |
| Editar `MSG-2026-0001` ou `MSG-2026-0002` para acrescentar este ato | Sao fonte canonica de **outros** atos | Tres atos, tres fontes |
| Editar **FND-09 §12** para inscrever o criterio | *"Este ato nao edita diretamente FND-09"* | O criterio vive em **ADR-0013**, que **referencia** FND-09 §12 sem altera-la |
| Fechar **IC-2**, **Q1** ou **Q2** | *"nao resolve por inferencia"*; *"nao ratifica futura emenda C3"* | As tres permanecem abertas, com dono e gatilho |
| Alcancar as cinco Cartas desta missao | *"Nenhuma alteracao posterior esta abrangida"* | As cinco nascem `em-revisao` · `pendente`, e dependem de **ato novo** |
| Reproduzir os hashes em indices | CM-09, PJ-01 | Indices referenciam **esta secao** |

## 9. Achados desta verificacao

| # | Achado | Sev. | Dono | Gatilho |
|---|---|---|---|---|
| **RC-01** | **`DEP-QAR §13.2` declara *"386 linhas"* para a Carta integral; o arquivo em vigor tem **387**.** A emenda acrescentou uma linha de historico e **nao** atualizou a propria medicao de carregamento — que esta dentro do conteudo ratificado e nao pode ser corrigida sem ato novo | **Baixa** | DEP-EXE | **Proxima emenda a `DEP-QAR`** por qualquer motivo. Ate la, o valor correto e **387**, medido, e vive aqui. Os recortes de decisao — **50** e **111** linhas — **permanecem exatos**: a emenda nao alterou o numero de linhas das secoes 1, 2, 4, 5 e 10 |
| **RC-02** | **`DEP-QAR` executa `IR-09` sobre a propria Carta.** `IR-09` atribui a execucao a DEP-QAR sem prever o caso em que o artefato ratificado **e** a Carta de DEP-QAR | **Media** | DEP-GOV | **Carta de DEP-GOV**, que declara em **B9** o impedimento simetrico. Mitigado nesta missao por **conferencia independente de DEP-GOV**, com resultado coincidente |

## 10. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Pacote de emenda consumido | [REV-ESTRUTURAL-I §7](../../foundation/revisao-estrutural-01-2026-07-28.md) — ID, versao, H-A, diff completo e recomendacao |
| Contrato que exigia o ato sobre a Carta | [ADR-0011 §5.3, **DC-09**](../../decisions/ADR-0011-contrato-de-carta-de-departamento.md) |
| Regra de integridade aplicada | [ADR-0012](../../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md), `IR-01` a `IR-09` |
| Pendencia que o ato responde | **PS-1** — [FIT-2026-007 §Pendencia](../../governance/fitness/FIT-2026-007-revisao-estrutural-i.md); achado **RE-06** |
| Ressalvas que o ato desbloqueia | **R4** de FIT-2026-006 *(DEP-QAR retem IC-5)* · **R2** de FIT-2026-007 *(criterio de consolidacao)* |
| Achado que o ato fecha | **RE-01** — designacao imprecisa de pacote |
| Formalizacao ordenada | [RFC-0010](../../rfcs/RFC-0010-criterio-de-horizonte-avaliavel.md) → [ADR-0013](../../decisions/ADR-0013-criterio-de-horizonte-e-consolidacao.md) |
| Precedente de forma | [MSG-2026-0002](MSG-2026-0002-ato-soberano-cartas-comando-plataforma-e-contexto.md) — **uma** fonte canonica, tudo o mais referencia |
| Baseline sobre a qual a integridade foi conferida | **`BL-2026-07-28-05`**, preservada e **nao editada** (BL-02) |
| Copia datada anterior as edicoes | **117** arquivos, fora do acervo (PI-07, AF-35) |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-GOV *(registro)* · SOBERANO *(emissao)* | Registro canonico do terceiro ato soberano de 2026-07-28: ratificacao de **`DEP-QAR` 1.1.0** vinculada ao hash `3e69441e…a3a0`, preservacao de **1.0.0** como versao substituida por quatro vias, e determinacao do **criterio de consolidacao** que responde a **PS-1**. Condicao de eficacia verificada por **dez verificacoes** em **cinco vias independentes**, incluindo o **diff literal** exigido por este ato e a **reconstrucao `IR-09`**. **RE-01 fechado**; achados **RC-01** e **RC-02** abertos com dono e gatilho. |
