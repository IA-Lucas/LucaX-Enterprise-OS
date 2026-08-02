---
id: MSG-2026-0004
titulo: Ato Soberano de ratificacao das cinco Cartas de Departamento, da emenda constitucional C3 e do regime do Fitness Check
tipo: relatorio
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: SOBERANO
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-07-29
atualizado_em: 2026-07-29
revisao_prevista: null
decisoes_relacionadas: [ADR-0011, ADR-0012, ADR-0014, ADR-0015]
substitui: []
substituido_por: null
canal: DIRETIVA
emissor: SOBERANO
destinatario: DEP-GOV
ttl: 1 ciclo — expira sem perda; os efeitos duraveis foram promovidos no mesmo ato (§7.1)
resumo: Registra, como fonte canonica unica, o ato soberano de 2026-07-29 que ratifica as cinco Cartas de Departamento, a emenda C3 a FND-01 e determina o regime do Fitness Check, com os IDs, versoes e hashes que ele vincula.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# MSG-2026-0004 — Ato Soberano de 2026-07-29

## Proposito
Registrar **uma unica vez** o ato soberano de 2026-07-29, com os IDs, versoes e hashes que ele
vincula, o que ele **nao** alcanca e a verificacao da condicao de eficacia. Indices, frontmatters
e catalogo **referenciam** esta secao; nenhum a reproduz (CM-09, PJ-01).

> **Quarto ato soberano registrado, e o de maior alcance ate hoje.** Os tres anteriores vivem em
> [MSG-2026-0001](MSG-2026-0001-ato-soberano-ratificacao-cartas-piloto.md),
> [MSG-2026-0002](MSG-2026-0002-ato-soberano-cartas-comando-plataforma-e-contexto.md) e
> [MSG-2026-0003](MSG-2026-0003-ato-soberano-emenda-qar-e-criterio-de-consolidacao.md).
> **Nenhum dos tres foi editado.** Quatro atos, quatro fontes.

## Escopo
| Item | Definicao |
|---|---|
| Inclui | O ato de 2026-07-29 e seus **quatro** itens; o que cada um alcanca; a condicao de eficacia; e os efeitos aplicados |
| **Nao** inclui | O **merito** das Cartas *(PS-2026-002)* e das emendas *(PS-2026-003)*; qualquer objeto que o ato nao nomeie |
| Instrumento | **Diretiva**, tipo documental de [FND-10 §4.6](../../foundation/10-artifact-framework.md), entidade `MSG`. Nenhum tipo, entidade, camada ou diretorio novo |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| **Emissor** | **SOBERANO** | PI-01 — autoridade final, indelegavel |
| **Registra** | **DEP-GOV** | LM-05, CV-09 |
| **Verifica a eficacia** | **DEP-QAR** | FND-10 §10.5; `IR-09` de ADR-0012 |
| **Nao participa da verificacao** | **DEP-EXE** | **Autor das nove Cartas.** Verificar a propria ratificacao repetiria a causa de [INC-2026-001](../../governance/incidents/INC-2026-001-ratificacao-inferida.md) |

---

## 1. O ato

| Campo | Conteudo |
|---|---|
| Emissor | **SOBERANO** (Lucas) |
| Canal | **DIRETIVA** (FND-05 §2) |
| Data do ato | **2026-07-29** |
| Objeto | **Quatro** itens: **(1)** ratificacao das **cinco** Cartas de Departamento; **(2)** ratificacao de **tres** emendas locais — **parcialmente valida**, §3; **(3)** ratificacao de **ADR-0014** e autorizacao de promulgacao de **FND-01 1.4.0**; **(4)** determinacao sobre o regime do `Fitness Check` |
| Condicao de eficacia | Entrada em vigor **apos verificacao independente** de identidade, versao, `H-A`, integridade e inexistencia de alteracao entre revisao e ratificacao |
| Limite expresso | *"Nenhuma alteracao futura esta abrangida"*; *"nao aprova RD-01, RD-02 ou RD-03"*; *"nao alcanca qualquer objeto nao enumerado expressamente"* |

### 1.1 Texto do ato — transcricao literal

> ATO SOBERANO DO FUNDADOR — 2026-07-29
>
> Apos revisar governance/pacote-soberano-2026-07-28-cartas.md,
> governance/pacote-soberano-2026-07-29-emendas.md, suas evidencias, revisoes independentes,
> riscos, ressalvas e identificadores de integridade:
>
> **1.** Aprovo e ratifico expressamente: DEP-GOV, versao 1.0.0, H-A SHA-256 `508c4c56…0227f`;
> DEP-TLS, versao 1.0.0, H-A SHA-256 `2ce3ea24…4616`; DEP-PRD, versao 1.0.0, H-A SHA-256
> `b3cd0f06…349b`; DEP-OPS, versao 1.0.0, H-A SHA-256 `48f53238…3679`; DEP-GRW, versao 1.0.0,
> H-A SHA-256 `7b24602a…c0ba`.
> A entrada em vigor de cada Carta depende da verificacao independente de identidade, versao,
> H-A, integridade e inexistencia de alteracao entre revisao e ratificacao.
> Nenhuma alteracao futura esta abrangida por este ato.
>
> **2.** Aprovo e ratifico expressamente: DEP-KMS, versao 1.1.0, H-A SHA-256 *[marcador]*;
> DEP-ENG, versao 1.1.0, H-A SHA-256 *[marcador]*; DEP-QAR, versao 1.2.0, H-A SHA-256
> `41f55e73…b5f2b`.
> A ratificacao alcanca exclusivamente os conteudos candidatos e os diffs literais identificados
> individualmente em governance/pacote-soberano-2026-07-29-emendas.md.
> A entrada em vigor depende da verificacao independente dos H-A, versoes, diffs e integridade.
> DEP-KMS 1.0.0, DEP-ENG 1.0.0 e DEP-QAR 1.1.0 devem permanecer recuperaveis como versoes
> historicas substituidas pelos mecanismos canonicos de historico, snapshot, hash e
> rastreabilidade. Nenhuma alteracao posterior esta abrangida por este ato.
>
> **3.** Acolho RFC-0011 como proposta antecedente e aprovo e ratifico expressamente ADR-0014,
> H-A SHA-256 `b557a0be…0f49`, exatamente na versao, conteudo e diff registrados no pacote
> soberano. Autorizo a promulgacao das alteracoes correspondentes em FND-01 na versao 1.4.0,
> condicionada a verificacao independente de correspondencia integral entre RFC-0011, ADR-0014,
> diff aprovado e documento promulgado. Este ato nao amplia titulares, competencias ou direitos
> decisorios alem do conteudo expressamente ratificado.
>
> **4.** Determino que Fitness Checks permanecam pareceres M1. Podem ser acolhidos, contestados
> ou superados, mas nao sao ratificados nem adquirem autoridade normativa por ato soberano.
> Determino que esse entendimento seja registrado e formalizado pelo rito aplicavel, sem edicao
> retroativa dos Fitness Checks historicos.
>
> Este ato nao aprova RD-01, RD-02 ou RD-03, nao ratifica futuras emendas e nao alcanca qualquer
> objeto nao enumerado expressamente.

> **Sobre as elisoes.** Os hashes acima estao **elididos nesta transcricao para caber na linha**;
> os valores **integrais de 64 caracteres**, como o ato os traz, estao em §2. **As duas
> ocorrencias marcadas `[marcador]` nao sao elisao**: o ato **nao trouxe** os valores nessas duas
> linhas — e a razao pela qual o item 2 e **parcialmente** valido (§3).

## 2. Objetos vinculados — ID, versao e hashes

Tres hashes conforme [ADR-0012 §5.2, IR-07](../../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md):
**H-A** arquivo submetido · **H-N** conteudo normativo · **H-P** arquivo apos a transicao.

### 2.1 Item 1 — as cinco Cartas de Departamento

| Carta | Versao | **H-A** | **H-N** | **H-P** | Linhas |
|---|---|---|---|---|---|
| `DEP-GOV` | 1.0.0 | `508c4c56f18f8096fdfbe0c418018a83f8b65bd48cbfc2242d1fd32046d0227f` | `3523bd0966d5450851d04e74d97638911b985f930b6c2e61c24d7fb7fbc27784` | `690fd201ecce44bdd0dd829daf950d69762a04d34eea558e61838d75e533111e` | **457** |
| `DEP-TLS` | 1.0.0 | `2ce3ea2493d06cf144fd88614d524d6ec479b3499ab62be6c0570d0e52794616` | `716f363a96a51d521ca9a2c589f22fa73f12d81eb90d772daf1801bed93e9858` | `d5eede3893868fe8554691a12d8f854ca8b239ae1a399dfed6d6f940235ad9fc` | **424** |
| `DEP-PRD` | 1.0.0 | `b3cd0f06b530e9aeeedd535472e8aec0ace03494633534acc6f1aed03cd2349b` | `1af73b7feaad38a162cc6960bb346caed1f554f6b39ce4c5b4d92ccae3128543` | `6a11652f8719259376771bd398fe5960118185e823cf8217c3246ff0d563c277` | **429** |
| `DEP-OPS` | 1.0.0 | `48f53238b55d62e8afc1480816e3cf83aa6613374ba0f6fd71361c3fecd23679` | `6bf590c7ad8bd2f0fc643dcf94f42d8abf6788c1dcef1ac9e56bd0f5c28a0a48` | `09d97a4c991d7dd1eb2fb8b261276ada267197fb9b8abe1669f7100627b63757` | **437** |
| `DEP-GRW` | 1.0.0 | `7b24602ab7416201a6ecddab230d9d331feeae5915013a7139e808b3c5e1c0ba` | `2e0e7d95b82e1fff963efd473b1389a55e33bfeee547d26ed18b2bb4c20062ea` | `0533fdf26235636e9957bf7da113384f6d4f7464548158335376186a50382ca1` | **443** |

**Os cinco `H-A` reproduzem exatamente os valores que o ato vincula, nos 64 digitos.**
**Os cinco `H-P` reproduzem exatamente os valores projetados em
[PT-2026-001 §1.3](../../governance/relatorio-transicao-2026-07-29-departamentos.md) antes do
ato** — e essa e a novidade metodologica deste registro: **o hash do estado futuro foi publicado
antes de existir**, e conferiu.

### 2.2 Item 3 — ADR-0014 e FND-01

| Artefato | Versao | **H-A** | **H-N** | **H-P** | Linhas |
|---|---|---|---|---|---|
| `ADR-0014` | 1.0.0 | `b557a0bebae63dff527424dfb8cd937fb390b4c8670498c84fc22e3dbd550f49` | `e6e420871c09ec6ae584e9433520cc8122133c5579f40993675d2ac76ba93b85` | `d90e73e69185152beafd8b16e8a16e6873c4310ebab081f5d3241d08473c9dc5` | **261** |

| Artefato | Antes | Depois |
|---|---|---|
| `FND-01` — versao | **1.3.0** | **1.4.0** |
| `FND-01` — hash do arquivo | `8c857b8852bb3d7913880c5d53128427f6c8b72a4621e402c011dda4465ef61f` | `1d70efa9b39372f98a92b466c30405eb08393c6ad8a152facd2ce76cb95e1def` |
| `FND-01` — `H-N` | `f36be0c010ae283309ae4e23b307af82df85180cb8ee85fbe18bb58466cb2850` | `a4048ee4cdd2f000662bae6e2d6da1332ce4022ba85009f0d4d7f410bb86e253` |
| `FND-01` — linhas | **468** | **475** *(+7)* |

> **`H-N` de FND-01 muda, e deve mudar.** Aqui nao houve transicao de estado: houve **emenda de
> conteudo**, ratificada. `H-N` invariante seria o sinal de que **nada foi promulgado**.

### 2.3 Item 4 — o instrumento de formalizacao

| Artefato | Versao | **H-A** | Linhas |
|---|---|---|---|
| [`ADR-0015`](../../decisions/ADR-0015-fitness-check-e-parecer-nao-decisao.md) | 1.0.0 | `3333ce303e2e8de917b621f5138f318bafa57ceef1de5c58be6f924bd9a0aae2` | **249** |

## 3. O item 2 — **parcialmente valido**, e o que isso significa

| Objeto | Identificador no ato | Estado |
|---|---|---|
| `DEP-QAR` **1.2.0** | `41f55e7369af5a9456e621cb4abd874a5c2c61af7e5a06b1900b4ca1619b5f2b` — **64 caracteres, confere** | **Ratificado. Nao aplicado** — §5 |
| `DEP-KMS` **1.1.0** | `[INSERIR HASH INTEGRAL DE 64 CARACTERES]` — **40 caracteres** | **NAO ratificado** |
| `DEP-ENG` **1.1.0** | idem — **40 caracteres** | **NAO ratificado** |

**Marcador nao e enumeracao.** As duas Cartas permanecem em **1.0.0**, `ativo` · `ratificada`, e
as duas emendas permanecem **candidatas**, com diff e hash em
[PS-2026-003 §2](../../governance/pacote-soberano-2026-07-29-emendas.md). **RC-05 e RC-07 seguem
abertos.** Achado **RD-07**.

> **`DEP-QAR` 1.2.0 esta ratificada e nao foi aplicada, por determinacao expressa do Soberano
> posterior ao ato** — *"Nao aplique O4, nao altere status, ratificacao, versao ou conteudo"*,
> limitada depois a liberacao dos itens **1, 3 e 4**. **Ratificado e aplicado sao coisas
> distintas, e a distincao esta registrada para que ninguem leia atraso como omissao.**

## 4. Alcance — o que o ato alcanca e o que **nao** alcanca

Ratificacao **nao se estende por analogia** (LM-03).

| Objeto | Alcancado? | Efeito |
|---|---|---|
| As **cinco** Cartas | **Sim — ratificadas** | `em-revisao` → **`ativo`**; `pendente` → **`ratificada`** |
| **`ADR-0014`** | **Sim — ratificado** | `em-revisao` → **`ativo`**; a emenda **C3 existe** |
| **`FND-01` 1.4.0** | **Sim — promulgacao autorizada**, sob condicao | Oito alteracoes aplicadas; **IC-2 fecha** |
| **Regime do `FIT`** | **Sim — determinado** | Formalizado em **ADR-0015**, `FT-10` a `FT-15` |
| `DEP-QAR` **1.2.0** | **Sim — ratificada**; **nao aplicada** | §3 |
| `DEP-KMS` 1.1.0 · `DEP-ENG` 1.1.0 | **Nao** — identificador invalido | Permanecem candidatas |
| **`FND-10` §10.3 · `FND-09` §8.2** | **Nao** — o ato **nao as menciona** | A divergencia com `FT-10` permanece **declarada** — achado **RD-09**, [ADR-0015 §5.3](../../decisions/ADR-0015-fitness-check-e-parecer-nao-decisao.md) |
| **RD-01 · RD-02 · RD-03** | **Nao** — vedacao expressa | Permanecem abertos, com dono e gatilho |
| `FIT` historicos | **Nao** — vedacao expressa de edicao retroativa | `FIT-2026-001` segue com o registro incorreto **contido, nao corrigido** |
| Qualquer versao futura de qualquer artefato | **Nao** | Exige ato novo |

## 5. Verificacao independente da condicao de eficacia

Executada por **DEP-QAR** *(medicao e reconstrucao)* e **DEP-GOV** *(forma e conferencia)*.
**DEP-EXE, autor das Cartas, nao participou.** Executada **antes** de qualquer edicao.

| # | O que o ato exigiu | Metodo | Resultado |
|---|---|---|---|
| **X1** | Integridade do registro | Reproducao de `BL-2026-07-29-02` sobre a copia pre-edicao | **134 artefatos · 36.888 linhas · `976f7708…69a5`** — as tres reproduzem |
| **X2** | **Identidade e versao** | Frontmatter de cada objeto contra o ato | **6 de 6** conferem; **2** trazem marcador e foram **recusados** |
| **X3** | **`H-A` integral** | `sha256sum` de cada objeto | **6 de 6 reproduzem**, nos 64 digitos |
| **X4** | **Inexistencia de alteracao entre revisao e ratificacao** | Impressao digital do acervo na abertura × no momento do ato | **Identica.** As nove Cartas mantiveram hash e contagem de linhas do inicio ao fim |
| **X5** | **`H-P` conferido contra o valor projetado** | Hash de cada arquivo apos **O4** | **5 de 5 CONFEREM** com PT-2026-001 §1.3, e **ADR-0014** produziu `d90e73e6…9dc5` |
| **X6** | **`H-N` invariante sob O4** | `H-N` antes × depois, nas cinco Cartas e em ADR-0014 | **Invariante em 6 de 6** (IR-02, IR-06) |
| **X7** | **`IR-09` — reconstrucao do texto ratificado** | Reverter **apenas** `status` e `ratificacao`, e medir | **6 de 6 reproduzem `H-A` exatamente** |
| **X8** | **Correspondencia integral RFC-0011 × ADR-0014 × diff × documento promulgado** | `diff -u` de FND-01 1.3.0 → 1.4.0, item a item contra [RFC-0011 §3.2](../../rfcs/RFC-0011-emenda-constitucional-ratifica-homologa.md) | **8 de 8 alteracoes aplicadas, e nada alem delas** — mais `versao`, `atualizado_em` e a linha de historico, que a promulgacao obriga (AL-04) e o ato autoriza |
| **X9** | **Titulares de decisao alterados** | Leitura celula a celula de §7.3 apos a emenda | **ZERO.** `DEP-EXE` continua em quatro linhas e `DEP-GOV` em uma, com o mesmo alcance |
| **X10** | Ausencia de **autoverificacao** | `autor` × `revisor` no acervo | **0 coincidencias** em **75** artefatos que declaram os dois |
| **X11** | Ausencia de **credencial** nos objetos ratificados | Varredura | **0 ocorrencias** (PI-08, LV-02) |

**Condicao de eficacia: SATISFEITA para os seis objetos enumerados com hash integral.**
**NAO satisfeita para `DEP-KMS` 1.1.0 e `DEP-ENG` 1.1.0** — e a recusa e o cumprimento da
condicao, nao a sua violacao.

## 6. Efeitos aplicados

| # | Efeito | Onde | Operacao |
|---|---|---|---|
| **Y1** | Cinco Cartas: `em-revisao` → **`ativo`**, `pendente` → **`ratificada`** | `departments/{gov,tls,prd,ops,grw}/carta.md` | **O4** (FND-10 §5.2) |
| **Y2** | **Cobertura vigente passa de 4/9 para 9/9** | [`departments/README §1`](../../departments/README.md) | Projecao (PJ-02) |
| **Y3** | `ADR-0014`: `em-revisao` → **`ativo`**, `pendente` → **`ratificada`** | `decisions/` | **O4** |
| **Y4** | **`FND-01` promulgada em 1.4.0** — 8 alteracoes | `foundation/01-constituicao.md` | Emenda **C3** |
| **Y5** | **`IC-2` FECHADO** — a causa, nao so o efeito | §7.2 | Fechamento com evidencia |
| **Y6** | **`IR-11` deixa de ser contencao e passa a redundancia benigna** | ADR-0012 §5.4 | Nao revogada — revoga-la seria decisao propria |
| **Y7** | Regime do `FIT` formalizado — `FT-10` a `FT-15` | [`ADR-0015`](../../decisions/ADR-0015-fitness-check-e-parecer-nao-decisao.md) | Determinacao → ADR |
| **Y8** | **`Q2` de RFC-0009 RESPONDIDA**; `G1/G2` de INC-2026-002 tratada no plano normativo | ADR-0015 | Fechamento com evidencia |
| **Y9** | Catalogo, indices e baseline atualizados na mesma mudanca | CV-04, IX-02 | Projecao |

### 6.1 O que deliberadamente **nao** foi feito

| Nao feito | Norma que o impede | Consequencia assumida |
|---|---|---|
| Preencher os dois hashes ausentes do item 2 | PI-01, DC-09; e a causa literal de INC-2026-001 | `DEP-KMS` 1.1.0 e `DEP-ENG` 1.1.0 seguem candidatas |
| Aplicar `DEP-QAR` 1.2.0, embora ratificada | Determinacao expressa posterior do Soberano | §3 |
| Editar **FND-10 §10.3** e **FND-09 §8.2** | Emendar `FND` exige ato do Soberano (FND-09 §8.2, linha `FND`); o ato **nao as menciona** | Achado **RD-09** |
| Editar o cabecalho de `ADR-0014` que diz *"NAO ESTA EM VIGOR"* | O texto esta **dentro de `H-N`**; altera-lo seria alteracao nao ratificada (IR-01, IR-05) | Achado **RD-08** — §8 |
| Corrigir `FIT-2026-001` | **M1**, e o ato **veda edicao retroativa** | Registro incorreto **contido, nao corrigido** |
| Criar Spec, agente, skill, workflow, produto, codigo ou infraestrutura | Determinacao da missao; PI-12 | **Nenhum foi criado** |

## 7. Rastreabilidade e fechamento de IC-2

### 7.1 Os efeitos duraveis foram promovidos

| Fato | Instrumento proprio que passa a guarda-lo |
|---|---|
| Vigencia das cinco Cartas | O campo `status` de cada Carta (FND-10 §5.2) |
| Estado de ratificacao | O campo `ratificacao` de cada frontmatter (FND-10 §5.4) |
| Vinculo ID × versao × `H-A`/`H-N`/`H-P` | **§2 desta Diretiva**, referenciada pelo [catalogo mestre §10](../../governance/artifact-registry.md) |
| A emenda constitucional | **FND-01 1.4.0** — o texto **e** a norma |
| O regime do `FIT` | [ADR-0015](../../decisions/ADR-0015-fitness-check-e-parecer-nao-decisao.md), `FT-10` a `FT-15` |

### 7.2 **IC-2 — FECHADO**

| Campo | Conteudo |
|---|---|
| Achado | A coluna *Ratifica* de FND-01 §7.3 nomeava **dois institutos** com **um** nome |
| Aberto ha | **Quatro ciclos** |
| Contencao vigente ate hoje | `IR-11` — **zero** violacoes em **1.210** ocorrencias medidas |
| **Como fecha** | **A causa foi corrigida na fonte**: §7.3 passa a distinguir os dois institutos, e §11 define **Homologacao** |
| Alcance da colisao, corrigido | **Cinco** linhas — quatro `DEP-EXE`, uma `DEP-GOV`. Achado **RC-03** tambem **fecha** |
| Titulares alterados | **ZERO** — X9 |
| O que **nao** fecha com ele | **RD-09**, novo: FND-10 §10.3 e FND-09 §8.2 divergem de `FT-10`. **Colisao diferente, em documentos diferentes** |

## 8. Achados desta verificacao

| # | Achado | Sev. | Dono | Gatilho |
|---|---|---|---|---|
| **RD-08** | **`ADR-0014` esta `ativo` e o proprio texto abre com *"⛔ ESTE ADR NAO ESTA EM VIGOR E NAO PRODUZ NENHUM EFEITO"*.** O bloco esta **dentro de `H-N`**: corrigi-lo seria alteracao nao ratificada (IR-01). **A fonte corrente do estado e o frontmatter** (FND-10 §5.4), nao o cabecalho | Baixa | DEP-GOV | **Proxima emenda a ADR-0014.** Mesmo mecanismo de **RC-01**: texto ratificado que a propria ratificacao tornou desatualizado |
| **RD-09** | **`FND-10 §10.3` e `FND-09 §8.2` continuam declarando *"Ratifica: SOBERANO se C3"* para `Fitness Check`, e `FT-10` diz o contrario.** A regra vigente e `FT-10`; as duas fundacionais divergem dela | **Media** | DEP-GOV | **Proximo ato soberano que alcance FND-09 ou FND-10** |

## 9. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Pacote consumido — Cartas | [PS-2026-002](../../governance/pacote-soberano-2026-07-28-cartas.md) |
| Pacote consumido — emendas | [PS-2026-003](../../governance/pacote-soberano-2026-07-29-emendas.md) |
| Pacote de transicao e minuta do ato | [PT-2026-001](../../governance/relatorio-transicao-2026-07-29-departamentos.md) |
| Contrato que exigia o ato | [ADR-0011 §5.3, **DC-09**](../../decisions/ADR-0011-contrato-de-carta-de-departamento.md) |
| Regra de integridade aplicada | [ADR-0012](../../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md), `IR-01` a `IR-10` |
| Emenda ratificada | [ADR-0014](../../decisions/ADR-0014-candidato-emenda-fnd-01-7-3-homologa.md) ← [RFC-0011](../../rfcs/RFC-0011-emenda-constitucional-ratifica-homologa.md) |
| Formalizacao do item 4 | [ADR-0015](../../decisions/ADR-0015-fitness-check-e-parecer-nao-decisao.md) |
| Incidentes cuja causa este ato fecha | [INC-2026-001](../../governance/incidents/INC-2026-001-ratificacao-inferida.md) *(mecanismo)* · [INC-2026-002](../../governance/incidents/INC-2026-002-ratificacao-declarada-em-fitness-check.md) *(causa normativa)* |
| Verificacao de aptidao | [FIT-2026-010](../../governance/fitness/FIT-2026-010-aplicacao-do-ato-soberano.md) |
| Baseline sobre a qual a integridade foi conferida | **`BL-2026-07-29-02`**, preservada e **nao editada** (BL-02) |
| Copia datada anterior as edicoes | **134** arquivos, fora do acervo (PI-07, AF-35) |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-GOV *(registro)* · SOBERANO *(emissao)* | Registro canonico do **quarto ato soberano**: ratificacao das **cinco** Cartas de Departamento — **cobertura vigente 9/9** —, ratificacao de **ADR-0014** e promulgacao de **FND-01 1.4.0**, que **fecha IC-2** apos quatro ciclos, e determinacao do regime do `Fitness Check`, formalizada em **ADR-0015**. Condicao de eficacia verificada por **onze** verificacoes, entre elas a **conferencia de `H-P` contra valor projetado antes do ato** — inedita no acervo. **Item 2 parcialmente valido:** dois identificadores invalidos, duas emendas **nao** ratificadas *(RD-07)*. Achados **RD-08** e **RD-09** abertos com dono e gatilho. |
