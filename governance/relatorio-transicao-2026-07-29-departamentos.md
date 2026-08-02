---
id: PT-2026-001
titulo: Pacote de transicao da camada de Departamentos — estado, integridade, divida e requisitos para o Specification Framework
tipo: relatorio
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-07-29
atualizado_em: 2026-07-29
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0011, ADR-0012, ADR-0013]
substitui: []
substituido_por: null
canal: REPORTE
emissor: DEP-GOV
destinatario: DEP-EXE
ttl: ate a decisao sobre a liberacao da proxima fase
resumo: Consolida o estado e a integridade das nove Cartas, o regime de ratificacao, a divida reconciliada, o mapa Departamento-Capability-artefato futuro e os requisitos que a camada impoe ao Specification Framework.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# PT-2026-001 — Pacote de transicao da camada de Departamentos

> ## Decisao desta missao: **`BLOCKED`**
>
> **Causa unica:** o ato soberano consumido chegou como **minuta com marcadores** —
> `[VERSAO]` e `[HASH INTEGRAL]` — e a **pre-condicao 1** exige ato que enumere `DEP-GOV`,
> `DEP-TLS`, `DEP-PRD`, `DEP-OPS` e `DEP-GRW` **por ID, versao e SHA-256 integral**.
> Marcador nao e enumeracao.
>
> **Nenhuma Carta foi ativada.** Preencher os marcadores por conta propria e **exatamente** a
> causa de [INC-2026-001 — ratificacao inferida](incidents/INC-2026-001-ratificacao-inferida.md):
> ato deduzido em vez de recebido. **A missao parou onde devia parar.**
>
> **Tudo o que nao depende do ato foi executado e esta neste pacote.** A minuta com os
> **valores ja verificados e preenchidos** esta em **§8** — e a unica coisa que falta e a
> assinatura.
>
> **Natureza deste artefato:** **Reporte**, tipo documental de
> [FND-10 §4.6](../foundation/10-artifact-framework.md), entidade `MSG` — o mesmo de
> [PS-2026-002](pacote-soberano-2026-07-28-cartas.md). **Nenhum tipo, entidade, camada,
> template ou diretorio novo.**

## Escopo
| Item | Definicao |
|---|---|
| Inclui | Estado e integridade das **nove** Cartas · regime de ratificacao **C3** · as **tres** emendas candidatas *(por referencia)* · coerencia **9/9** *(por referencia)* · fechamento da camada · divida reconciliada · mapa **Departamento → Capability → artefato futuro** · requisitos para o **Specification Framework** · decisao |
| **Nao** inclui | O **merito** das cinco Cartas *(PS-2026-002)* · o **merito** das tres emendas *(PS-2026-003)* · a projecao comparativa *([`departments/README §2`](../departments/README.md) — fonte unica, nao reproduzida)* · qualquer Spec, agente, skill, workflow, produto, codigo, banco, infraestrutura ou migracao, **nenhum dos quais foi criado** |
| Metodo | Toda contagem deste pacote foi **executada por ferramenta** sobre o acervo, nesta missao. **Nenhum numero foi herdado sem reconferencia, e nenhum foi estimado** (CE-04, LV-12) |

---

## 1. Estado e integridade das nove Cartas

### 1.1 Verificacao de integridade — executada **antes** de qualquer edicao

| # | O que se verificou | Metodo | Resultado |
|---|---|---|---|
| **V1** | Integridade do acervo na abertura | Reproducao integral de `BL-2026-07-28-06` | **131 artefatos · 35.701 linhas · impressao digital `164214e4…f9c6`** — as tres reproduzem o valor registrado, **digito a digito** |
| **V2** | Copia datada antes das edicoes | `cp` de todos os `.md` para fora do acervo | **131 arquivos**, com contagem e impressao digital **reconferidas na copia** (PI-07, AF-35) |
| **V3** | `H-A` das cinco Cartas submetidas | `sha256sum` de cada arquivo | **5 de 5 reproduzem** o valor de [PS-2026-002 §2](pacote-soberano-2026-07-28-cartas.md) |
| **V4** | `H-N` das cinco Cartas | Reimplementacao independente de `IR-02` + `IR-03` | **5 de 5 reproduzem.** A reimplementacao foi **validada primeiro contra as quatro Cartas ja em vigor**, e reproduziu tambem os `H-N` delas |
| **V5** | Contagem de linhas | `wc -l` por arquivo | **9 de 9** conferem com [`departments/README §2`](../departments/README.md); soma **3.918** |
| **V6** | Diff desde a revisao | Comparacao do acervo com a impressao digital de `BL-…-06` | **Zero alteracoes** entre a submissao e agora, nas cinco e em todo o resto |
| **V7** | Links | Resolucao de **1.389** links relativos do acervo | **0 quebrados** |
| **V8** | Autoverificacao | `autor` × `revisor` nos **70** artefatos que declaram os dois | **0 coincidencias** (FT-02, RM-06b, ADR-0005) |

**Integridade: INTACTA. Nenhuma divergencia entre revisao e decisao — `BLOCKED` nao decorre de
defeito de integridade, e sim da forma do ato.**

### 1.2 As cinco Cartas pendentes — objeto exato do ato que falta

| Carta | Versao | **H-A *(arquivo submetido)*** | **H-N *(conteudo normativo)*** | Linhas | Estado |
|---|---|---|---|---|---|
| `DEP-GOV` | **1.0.0** | `508c4c56f18f8096fdfbe0c418018a83f8b65bd48cbfc2242d1fd32046d0227f` | `3523bd0966d5450851d04e74d97638911b985f930b6c2e61c24d7fb7fbc27784` | **457** | `em-revisao` · `pendente` |
| `DEP-TLS` | **1.0.0** | `2ce3ea2493d06cf144fd88614d524d6ec479b3499ab62be6c0570d0e52794616` | `716f363a96a51d521ca9a2c589f22fa73f12d81eb90d772daf1801bed93e9858` | **424** | `em-revisao` · `pendente` |
| `DEP-PRD` | **1.0.0** | `b3cd0f06b530e9aeeedd535472e8aec0ace03494633534acc6f1aed03cd2349b` | `1af73b7feaad38a162cc6960bb346caed1f554f6b39ce4c5b4d92ccae3128543` | **429** | `em-revisao` · `pendente` |
| `DEP-OPS` | **1.0.0** | `48f53238b55d62e8afc1480816e3cf83aa6613374ba0f6fd71361c3fecd23679` | `6bf590c7ad8bd2f0fc643dcf94f42d8abf6788c1dcef1ac9e56bd0f5c28a0a48` | **437** | `em-revisao` · `pendente` |
| `DEP-GRW` | **1.0.0** | `7b24602ab7416201a6ecddab230d9d331feeae5915013a7139e808b3c5e1c0ba` | `2e0e7d95b82e1fff963efd473b1389a55e33bfeee547d26ed18b2bb4c20062ea` | **443** | `em-revisao` · `pendente` |

### 1.3 `H-P` projetado — o que a transicao **O4** produzira, se o ato ocorrer

> **Nao e hash de artefato existente.** E o valor que o arquivo tera **apos** a transicao de
> estado que a propria ratificacao obriga a executar (FND-10 §5.2, O4). Publica-lo **antes**
> torna a aplicacao do ato verificavel por terceiro: se o arquivo pos-transicao nao reproduzir
> exatamente este valor, houve alteracao alem do diff — e isso e **IR-05**.

| Carta | Diff da transicao | **H-P projetado** |
|---|---|---|
| `DEP-GOV` | `status: em-revisao` → `ativo` · `ratificacao: pendente` → `ratificada` | `690fd201ecce44bdd0dd829daf950d69762a04d34eea558e61838d75e533111e` |
| `DEP-TLS` | idem | `d5eede3893868fe8554691a12d8f854ca8b239ae1a399dfed6d6f940235ad9fc` |
| `DEP-PRD` | idem | `6a11652f8719259376771bd398fe5960118185e823cf8217c3246ff0d563c277` |
| `DEP-OPS` | idem | `09d97a4c991d7dd1eb2fb8b261276ada267197fb9b8abe1669f7100627b63757` |
| `DEP-GRW` | idem | `0533fdf26235636e9957bf7da113384f6d4f7464548158335376186a50382ca1` |

**Duas linhas de frontmatter por Carta, nenhuma linha de corpo, contagem de linhas identica —
e `H-N` invariante nas cinco** (IR-02, IR-06). **Dez alteracoes ao todo, e nada alem delas.**

### 1.4 `DEP-QAR` 1.0.0 — restaurabilidade confirmada, sem segunda Carta canonica

| Via | Estado | Evidencia |
|---|---|---|
| **PV-1 — hash registrado** | ✅ | `H-A` `c591fd62…c311b` · `H-N` `250d1289…8810` — [MSG-2026-0003 §2.1](../memory/operacional/MSG-2026-0003-ato-soberano-emenda-qar-e-criterio-de-consolidacao.md) |
| **PV-2 — diff reversivel** | ✅ | O diff de MSG-2026-0003 §7.2 e literal e completo; aplicado em sentido inverso sobre 1.1.0, reproduz 1.0.0 |
| **PV-3 — copia datada** | ✅ | **Dupla**: a de 117 arquivos da Missao 1.9 e a de **131** tomada nesta missao *(V2)* |
| **PV-4 — historico da propria Carta** | ✅ | A linha `1.0.0` permanece em `DEP-QAR §Historico` e **nunca sai** (AL-04) |

**Nenhuma segunda Carta canonica foi criada, e nenhuma area historica nova foi aberta.** As
quatro vias bastam; abrir area historica agora criaria estrutura sem gatilho observado.

## 2. Regime de ratificacao — a emenda **C3**

| Campo | Estado |
|---|---|
| **Ato C3 recebido?** | **NAO.** O item 2 da minuta esta condicionado por escrito — *"[INCLUIR SOMENTE APOS REVISAR E CONCORDAR COM O DIFF C3]"* — e **condicao nao cumprida nao e ato** |
| **ADR-0014** | Permanece **`em-revisao` · `ratificacao: pendente`**. `H-A` `b557a0bebae63dff527424dfb8cd937fb390b4c8670498c84fc22e3dbd550f49` · **261** linhas |
| **RFC-0011** | Permanece `aprovado`. `H-A` `3e1f007502f6b69528d7379b667022d3e9f3bff1dc9faf6a71876f4f2aa0bcea` · **251** linhas |
| **FND-01** | Permanece em **1.3.0**. **Nenhuma linha alterada** |
| **`IR-11`** | **Integralmente em vigor**, como unica contencao |
| **IC-2** | **CONTIDO, NAO FECHADO** — quarto ciclo |
| **Titulares ampliados por inferencia** | **ZERO.** A colisao **nao foi resolvida**, e resolve-la sem ato seria ampliar titular por inferencia — o que a missao proibiu |

**Impacto sobre Specs futuras, declarado:** a coluna *Ratifica* de FND-01 §7.3 continua nomeando
**dois institutos**. `SPC` **nao tem ratificador** na matriz de FND-09 §8.2 — a celula e `—` —,
e por isso a ambiguidade **nao alcanca a Spec diretamente**. Ela alcanca **`PRO`** e **`TOL`**,
que a camada de Specs vai produzir logo em seguida e que **exigem ratificacao do Soberano**.
**A contencao `IR-11` protege o artefato novo e nao protege o leitor do texto constitucional** —
e quem escrever a primeira Carta de Produto le FND-01, nao ADR-0012.

## 3. As tres emendas locais

Objeto integral de [PS-2026-003](pacote-soberano-2026-07-29-emendas.md) — **nao reproduzido
aqui** (PJ-01, CM-09).

| Carta | De → Para | Achado | Classe | Estado |
|---|---|---|---|---|
| `DEP-KMS` | 1.0.0 → **1.1.0** | RC-05 | **Normativo** | **Candidata.** Nenhum arquivo editado |
| `DEP-ENG` | 1.0.0 → **1.1.0** | RC-07 | **Normativo** | **Candidata.** Nenhum arquivo editado |
| `DEP-QAR` | 1.1.0 → **1.2.0** | RC-01 | **Projecao** | **Candidata.** Nenhum arquivo editado |

## 4. Coerencia 9/9

Objeto integral de [`departments/README §2.2`](../departments/README.md) — **projecao unica**,
nao reproduzida aqui. **Nenhuma segunda projecao comparativa foi criada**, porque criar uma
seria a duplicacao que `MEM-APR-0002` registra ha seis ciclos.

**Resultado: 117 verificacoes — 13 dimensoes × 9 Cartas. 113 conformes · 4 achados.**
Tres achados ja eram conhecidos *(RC-01, RC-05, RC-07)*; a verificacao produziu **tres novos**:
**RD-01**, **RD-02** e **RD-03** — §7.

## 5. Fechamento da camada — o contrato de consumo, **testado**

> **O que a camada de Departamentos entrega ao proximo Framework:** **autoridade, custodia,
> interfaces e contexto.** **O que ela nao entrega: competencia executada.**

### 5.1 O teste — quatro perguntas que um Framework consumidor precisa responder

| # | Pergunta do consumidor | A camada responde? | Fonte da resposta |
|---|---|---|---|
| **T1** | *"Quem pode criar este artefato, e com que autoridade?"* | ✅ **Sim, para 21 de 21 entidades** | FND-09 §8.2, com a **fonte citada em 76 de 76 linhas** de autoridade das nove Cartas |
| **T2** | *"Quem custodia a competencia que ele exerce?"* | ✅ **Sim, para 23 de 23 Capabilities** | frontmatter das 23 Cartas de Capability; **0** sem custodio, **0** com custodia dupla |
| **T3** | *"Por onde ele entra e por onde sai?"* | ✅ **Sim** — **9 de 9** Cartas declaram §6.3 conforme a propria linha de FND-02 §4; **11** pares de interface fecham | FND-02 §4; §6 das nove Cartas |
| **T4** | *"O departamento que o produz sabe faze-lo?"* | ❌ **NAO — e a resposta correta** | **41 de 123** indicadores estao `definido, sem valor`; os **82** medidos descrevem o **acervo**, nao desempenho. **Nenhuma Carta foi exercida em operacao real** |

**T1, T2 e T3 passam. T4 falha por desenho, e a falha e o produto.** Uma camada que respondesse
*"sim"* a T4 sem ciclo de produto estaria afirmando desempenho sem medida — **LV-12**.

### 5.2 O limite duro que o consumidor precisa conhecer

| # | Limite | Consequencia para quem consome |
|---|---|---|
| **LC-1** | **Cobertura vigente e 4/9, nao 9/9** | Carta que nao vigora **nao pode ser consumida** (LM-02). Um Framework que se apoie em `DEP-PRD`, `DEP-OPS`, `DEP-GRW`, `DEP-TLS` ou `DEP-GOV` **hoje se apoia em nada** |
| **LC-2** | **Zero agentes existem** | As nove descrevem **dominios**, nao executores. Nenhuma Spec pode ser **atribuida** a um executor |
| **LC-3** | **Autor unico** — DEP-EXE escreveu 9 de 9 | O contrato de Carta **nunca foi testado contra autor distinto**. R1 de FIT-2026-006, **agravada** |
| **LC-4** | **Desempenho nao exercido** | Toda promessa de competencia e **projecao**, nunca evidencia |

### 5.3 Proibicao mantida

**Nenhuma equipe, agente, subagente ou subdepartamento foi criado por antecipacao.** Os gatilhos
de especializacao dispararam em **DEP-ENG** *(VC-03, 5 > 3)*, em **DEP-GOV** *(cinco gatilhos)*
e em **DEP-KMS** *(fronteira P2)* — e **as tres Cartas registraram "nao especializar"**, porque
**SE-02 exige dois sinais observados** e nenhuma tem dois. **Ganho previsto nao autoriza** (SE-01).

## 6. Mapa **Departamento → Capability → artefato futuro**

> **Projecao (PJ-02).** **Fonte:** frontmatter das 23 Cartas de Capability *(custodia)* · §7 das
> nove Cartas *(artefatos mantidos)* · FND-09 §8.2 *(autoridade por entidade)*.
> **Finalidade:** dizer, antes de o Specification Framework existir, **quem produz o que** e
> **com que autoridade**. **Atualizacao:** pela mesma mudanca que altera qualquer das tres fontes.

| Departamento | Capabilities custodiadas | Artefato futuro que **produz** | Papel em `SPC` |
|---|---|---|---|
| **DEP-PRD** | produto · pesquisa · design | **`SPC`** *(autor e aprovador, QG-1)* · **`PRO`** *(autor; ratifica SOBERANO)* | **AUTOR e APROVADOR** |
| **DEP-ENG** | arquitetura · engenharia · dados · IA · engenharia-de-agentes | `AGT` · `SUB` · `SKL` *(autor)* · `ADR` tecnico | **REVISOR** — nunca autor |
| **DEP-QAR** | qualidade · seguranca · juridico | `FIT` · `REV` *(autor)* | **REVISOR** — com DEP-ENG |
| **DEP-TLS** | integracao | **`TOL`** *(autor e proprietario; ratifica SOBERANO)* · catalogo de ferramentas | — *(fornece a ferramenta que a Spec pressupoe)* |
| **DEP-GOV** | governanca | `FND` · `TPL` · `INC` · catalogo · indices | **REVISOR de forma**; numera e registra |
| **DEP-EXE** | estrategia · coordenacao · financeiro · comunicacao | `PRJ` *(autor e aprovador)* · aprova `AGT`/`SUB`/`SKL`/`WFL`/`TOL` | **Prioriza**; nao decide escopo |
| **DEP-OPS** | operacoes · infraestrutura | Runbook · postmortem · `MEM` **OPR** | **Consumidor** — recebe o que a Spec gerou |
| **DEP-GRW** | marketing · comercial | `ADR` de canal · sinal de mercado em `MEM` **PRD** | **Fornece sinal**; nao vira requisito sem PRD |
| **DEP-KMS** | conhecimento · aprendizado-organizacional *(+ comunicacao, exercida)* | Catalogo · baseline · pacote de contexto · `MEM` **APR** | **Fornece contexto**; mede o custo |

**23 custodias · 9 departamentos · 0 Capabilities sem custodio · 0 custodias duplas · 1 exercicio
sem custodia** *(`CAP-comunicacao`, por DEP-KMS)*.

## 7. Requisitos que a camada impoe ao **Specification Framework**

> Derivados **da fonte**, nao propostos: cada requisito cita a linha que ja o obriga. **Nenhum
> deles e norma nova, e nenhum e criado por este pacote.**

| # | Requisito | Fonte que ja o obriga |
|---|---|---|
| **RS-1** | **`SPC` nao cria tipo documental nem entidade.** `SPC` ja existe em FND-09 §5 e FND-10 §4; o Framework o **usa** | CS-01, MT-01 |
| **RS-2** | **Autor = DEP-PRD · revisores = DEP-ENG + DEP-QAR · aprovador = DEP-PRD em QG-1 · ratificador = nenhum** | FND-09 §8.2, linha `SPC` |
| **RS-3** | **Enderecar o acumulo autor×aprovador.** `SPC` e **uma de tres** entidades da matriz cujo propositor e aprovador sao o mesmo departamento — as outras sao `TPL` e `PRJ` — e **a unica das tres cuja aprovacao libera um portao de qualidade**. E o risco **RP-1** que a propria `DEP-PRD` declarou: *o unico portao do sistema sem contraditorio previo* | FND-09 §8.2; `DEP-PRD §10`, RP-1 |
| **RS-4** | **Handoff PRD → ENG com criterio de aceite verificavel e escopo negativo**, e criterio de devolucao declarado | HO-02, HO-04; `DEP-PRD §8.2`; `DEP-ENG §8.2` |
| **RS-5** | **Nenhuma Spec entra em vigor apoiada em Carta que nao vigore** | LM-02; **LC-1** |
| **RS-6** | **Toda Spec entra no catalogo com custo de contexto medido, nunca estimado** | RG-02, CE-04; `DEP-KMS §10`, I-10 |
| **RS-7** | **Indicador de Spec sem valor declara-se `definido, sem valor`** | DC-07, LM-01, LV-12 |
| **RS-8** | **`projects/` nao existe.** `DEP-PRD §7` declara que a Spec vivera em `projects/`; criar o diretorio e parte do Framework, e **nao foi antecipado aqui** | `DEP-PRD §7`; PI-12 |
| **RS-9** | **Nenhuma Spec pode ser atribuida a executor**, porque **nenhum existe** | **LC-2**; IC-3 |
| **RS-10** | **A Spec consome autoridade; nao a concede.** Consumir nao da autoridade sobre o consumido | FND-09 §8.1, verbo **Consumir**; **MT-09** |

## 8. Minuta do ato soberano — **pronta, com os valores verificados**

> ### Esta secao **nao e um ato**. E o texto que faltava, com os marcadores substituidos por
> ### valores medidos e reconferidos nesta missao.
>
> **Nada aqui produz efeito.** Enquanto o Soberano nao emitir o ato, as cinco Cartas permanecem
> `em-revisao` e as tres emendas permanecem candidatas. **DEP-GOV registra o ato; nunca o emite**
> (`DEP-GOV §7`).

```
ATO SOBERANO DO FUNDADOR — <data do ato>

Apos revisar governance/pacote-soberano-2026-07-28-cartas.md e
governance/pacote-soberano-2026-07-29-emendas.md, suas evidencias, revisoes, riscos e ressalvas:

1. Aprovo e ratifico expressamente:

- DEP-GOV, versao 1.0.0,
  SHA-256 508c4c56f18f8096fdfbe0c418018a83f8b65bd48cbfc2242d1fd32046d0227f;
- DEP-TLS, versao 1.0.0,
  SHA-256 2ce3ea2493d06cf144fd88614d524d6ec479b3499ab62be6c0570d0e52794616;
- DEP-PRD, versao 1.0.0,
  SHA-256 b3cd0f06b530e9aeeedd535472e8aec0ace03494633534acc6f1aed03cd2349b;
- DEP-OPS, versao 1.0.0,
  SHA-256 48f53238b55d62e8afc1480816e3cf83aa6613374ba0f6fd71361c3fecd23679;
- DEP-GRW, versao 1.0.0,
  SHA-256 7b24602ab7416201a6ecddab230d9d331feeae5915013a7139e808b3c5e1c0ba.

A entrada em vigor de cada Carta depende da verificacao independente de identidade, versao,
hash, integridade e inexistencia de alteracao entre revisao e ratificacao. Nenhuma alteracao
futura esta abrangida por este ato.

2. [INCLUIR SOMENTE SE APROVAR AS TRES EMENDAS LOCAIS]
Aprovo e ratifico expressamente:

- DEP-KMS, versao 1.1.0,
  SHA-256 10cfc73d5e3b7779beb22bef5dc11b0ace1d15f8b0d9855aa8cfbfbb6fec33e5;
- DEP-ENG, versao 1.1.0,
  SHA-256 38d4613d88b8253cd8b34d6b2b51fcc68624dfeb9509093de6678f9968428be9;
- DEP-QAR, versao 1.2.0,
  SHA-256 41f55e7369af5a9456e621cb4abd874a5c2c61af7e5a06b1900b4ca1619b5f2b.

exatamente no diff literal registrado em PS-2026-003 §2. As versoes substituidas — DEP-KMS
1.0.0, DEP-ENG 1.0.0 e DEP-QAR 1.1.0 — deverao ser preservadas como versoes historicas.

3. [INCLUIR SOMENTE APOS REVISAR E CONCORDAR COM O DIFF C3]
Aprovo e ratifico expressamente a emenda C3 representada por RFC-0011 e ADR-0014,
SHA-256 b557a0bebae63dff527424dfb8cd937fb390b4c8670498c84fc22e3dbd550f49,
exatamente na versao, conteudo e diff registrados em RFC-0011 §3.2, e determino a versao
de promulgacao de FND-01 — 1.4.0 ou 2.0.0. Sua vigencia depende de verificacao independente.

4. Determino que Fitness Checks permanecam pareceres M1. Eles podem ser acolhidos, contestados
ou superados, mas nao sao ratificados nem adquirem autoridade normativa por ato soberano.

Este ato nao aprova RD-01, RD-02 nem RD-03, nao ratifica futuras emendas e nao alcanca
qualquer objeto nao enumerado expressamente.
```

> **Tres observacoes sobre a minuta, todas materiais.**
>
> **(1) O item 4 e o unico que a minuta original ja continha em forma final** — e ele **nao e
> ratificacao**, e sim **determinacao**. Isso importa: a **questao Q2** pergunta se `FIT` **exige**
> ratificacao, e o item 4 responde pelo comportamento *(sao pareceres M1, nao se ratificam)*
> sem emendar FND-10 §10.3. Se o Soberano quiser **fechar Q2**, o item 4 basta como
> determinacao; se quiser **corrigir a norma**, e preciso o rito C2 de RFC-0011 §5.2.
> **A diferenca esta declarada para que o silencio nao decida.**
>
> **(2) A minuta original nao aprovava `RC-01`, `RC-05` nem `RC-07`** — e nao podia, porque nao
> havia emenda candidata quando foi escrita. Agora ha, e o item 2 e opcional e separavel.
>
> **(3) A clausula de nao alcance foi atualizada** para nomear `RD-01`, `RD-02` e `RD-03`, que
> **nao existiam** quando a minuta foi redigida. **Enumerar o que o ato nao alcanca e o que
> impede LM-03.**

## 9. Divida e ressalvas — reconciliacao

> **Regra aplicada:** *"tratado"* nao significa *"resolvido"*. Cada item recebe **um** dos cinco
> estados, e **nenhum e fechado sem evidencia**.

| Item | Estado | Evidencia ou motivo |
|---|---|---|
| **PS-1** *(criterio de consolidacao)* | **RESOLVIDA** | Respondida pelo ato de 2026-07-28 e formalizada em [ADR-0013](../decisions/ADR-0013-criterio-de-horizonte-e-consolidacao.md). **Nao reaberta nesta missao** |
| **RD-04** *(`governance/README` uma baseline atras)* | **RESOLVIDA** | Defeito de **projecao** (M3): corrigido na vista, **zero fontes alteradas** (RG-03, PJ-03) |
| **R4 de FIT-2026-008** *(RC-01, RC-05, RC-07 retidos)* | **RECLASSIFICADA** | Sai de *"retida sem instrumento"* e passa a *"retida **com emenda candidata pronta**"*. O gatilho literal — *"proxima emenda a cada uma das tres Cartas"* — **foi cumprido**; **fechar exige o ato**, nao a emenda |
| **RC-01 · RC-05 · RC-07** | **MANTIDOS** | Os tres continuam **abertos** nas Cartas em vigor. A existencia da emenda **nao os fecha** |
| **IC-2** *(colisao do termo ratificar)* | **MANTIDO — contido** | `IR-11` segue como unica protecao, com **0** violacoes medidas. **Quarto ciclo** |
| **Q2** *(`FIT` exige ratificacao?)* | **MIGRADA** *(ciclo anterior)* · **passivel de determinacao agora** | Vive em RFC-0009 Q2, aberta. O **item 4** da minuta a alcanca por determinacao — §8, observacao (1) |
| **R1 de FIT-2026-005 · R1 de FIT-2026-006 · R1 e R3 de FIT-2026-007 · R3 de FIT-2026-008** *(autor unico, segregacao no limite)* | **MANTIDAS — agravadas** | **Quarta missao seguida** operando no limite. Esta missao **nao criou agente**, por determinacao; o residuo permanece **declarado** |
| **R1 e R2 de FIT-2026-008** *(regras `HZ` sem membros · crescimento)* | **MANTIDAS** | `HZ-02` continua sem disparar. Crescimento: **9o ciclo** — §F1 de [FIT-2026-009](fitness/FIT-2026-009-ativacao-e-endurecimento.md) |
| **R4 de FIT-2026-002** *(reducao de contexto)* | **MANTIDA** | Exige **duas** descidas consecutivas itemizadas; **ha uma** |
| **RD-01 · RD-02 · RD-03** | **NOVOS — abertos** | §10, com dono e gatilho |
| **RD-05** *(minuta com marcadores)* | **NOVO — tratado** | §10; a minuta preenchida esta em §8 |
| **RD-06** *(catalogo diverge de si proprio)* | **RESOLVIDO** | §10; corrigido no `resumo` do catalogo mestre |

**Ressalvas renomeadas para parecerem fechadas: ZERO. Ressalvas fechadas por reformulacao:
ZERO.** Tres itens **resolvidos com evidencia** — PS-1 *(no ciclo anterior)*, RD-04 e RD-06 —,
**um reclassificado** com o motivo escrito, **um migrado** e passivel de determinacao, e o
restante **mantido**. **Nenhuma das ressalvas de aptidao fechou neste ciclo**, e a que a missao
existia para fechar depende de ato.

## 10. Achados novos desta missao

| # | Achado | Sev. | Dono | Gatilho | Corrigivel agora? |
|---|---|---|---|---|---|
| **RD-01** | `DEP-PRD §8.2` cita *"FND-02 §4 declara `—` entre PRD e TLS"*; a matriz declara **`C`** no sentido PRD→TLS e `—` **apenas** no sentido TLS→PRD | Baixa | DEP-EXE | **Apos** a decisao sobre PS-2026-002 | **Nao** — mudaria o `H-A` ja submetido |
| **RD-02** | Os campos `GOV→KMS` e `QAR→KMS` de FND-02 §4 declaram **`E`**; a leitura obrigatoria da mesma tabela declara que a Guarda **veta Linha e Plataforma**. As Cartas resolvem de **tres** formas distintas | **Media** | DEP-GOV | Proxima emenda a **FND-02**, ou primeiro veto real sobre Plataforma | **Nao** — ambiguidade na **fonte fundacional** |
| **RD-03** | `DEP-KMS §6.3` declara *"entrega a sete departamentos"*; a linha KMS de FND-02 §4 tem **6** `E`, **2** `C` e **1** `—`. E cita *"KMS entrega a todos (linha KMS)"* onde a fonte diz *"**Todos entregam a KMS**"* — a **coluna** | Baixa | DEP-EXE | Proxima emenda a `DEP-KMS` | **Nao** — Carta ratificada |
| **RD-04** | `governance/README` declarava `BL-…-05`, **117** artefatos, **30.947** linhas e **14** ressalvas; as fontes declaram `BL-…-06`, **131**, **35.701** e **15** | Baixa | DEP-GOV | — | ✅ **CORRIGIDO** nesta missao, na projecao |
| **RD-05** | O ato soberano chegou como **minuta com marcadores**, embora **PS-2026-002 §2 ja publicasse todos os valores**. O pacote entregou os dados e **nao entregou a minuta preenchida** | **Media** | DEP-GOV | **Proximo pacote soberano** | ✅ **TRATADO** — §8 entrega a minuta com os valores |
| **RD-07** | O ato soberano de **2026-07-29** enumerou corretamente **6 de 8** objetos, e substituiu **2** SHA-256 integrais por um marcador de **40 caracteres** — `[INSERIR HASH INTEGRAL DE 64 CARACTERES]` — nas linhas de `DEP-KMS` 1.1.0 e `DEP-ENG` 1.1.0. **PS-2026-003 §2 e PT-2026-001 §8 publicavam os dois valores, com 64 caracteres cada** | **Media** | DEP-GOV | **Reemissao do item 2 do ato** | **Nao — e nao ha o que corrigir no acervo.** As duas Cartas **nao foram ratificadas**; os candidatos **nao foram alterados**; **nenhum incidente aberto**, porque a fonte canonica **nao contem hash invalido** *(verificado: 0 hashes ≠ 64 em PS-2026-003)*. **Segunda ocorrencia da familia de RD-05** — valor publicado que nao chega ao ato |
| **RD-06** | O **catalogo mestre** divergia de si proprio em **dois** lugares: o `resumo` declarava **117** artefatos e **§9** declarava **112** `native`, enquanto **§10.0** declarava **131**. Tres numeros, tres missoes diferentes, **um** arquivo | Baixa | DEP-GOV | — | ✅ **CORRIGIDO** nos dois lugares. **Terceira ocorrencia** de o catalogo divergir de si proprio — as anteriores foram **IC-8** e **RE-04** |

> **RD-02 e o unico dos cinco que toca autoridade, e por isso e o unico que muda a decisao.**
> Os outros quatro sao citacao, contagem, projecao e forma. **RD-02 pergunta se a Guarda veta a
> Plataforma** — e a fonte responde `E` numa celula e *"veta"* na leitura obrigatoria da mesma
> tabela. **Nenhuma Carta pode resolver isso**, e nenhuma tentou: `DEP-GOV` declarou veto,
> `DEP-QAR` nao declarou, `DEP-KMS` declarou receber de ambos. **Tres leituras de uma fonte
> ambigua, e nenhuma delas errada.**

## 11. Decisao

| Campo | Conteudo |
|---|---|
| **Decisao** | **`BLOCKED`** |
| **Causa** | **Pre-condicao 1 nao satisfeita.** O ato consumido nao enumera as cinco Cartas por versao e SHA-256 integral: traz `[VERSAO]` e `[HASH INTEGRAL]` |
| **Por que nao `GO-TO-SPECS`** | Exige **nove Cartas ativas**. Ha **quatro** |
| **Por que nao `GO-CONDITIONAL`** | Exige **nove ativas** com emendas contidas. Ha **quatro** |
| **Por que nao `READY-FOR-AMENDMENT-RATIFICATION`** | As emendas **nao sao o que impede o fechamento** — as tres tem efeito nulo ou local, e as tres tem candidato pronto. O que impede e a **forma do ato sobre as cinco Cartas** |
| **Por que nao `ADJUST`** | Nenhuma correcao delimitada resta **dentro do mandato**. Tudo o que nao dependia do ato foi executado |
| **Por que nao `STOP`** | **Zero** falhas estruturais: 117 verificacoes de contrato com 113 conformes e 4 achados de severidade baixa ou media; **0** links quebrados; **0** autoverificacoes; integridade **intacta** |
| **O que desbloqueia** | **Um** ato, na forma de §8. Nada mais |

### 11.1 O que a decisao seria, se o ato chegasse hoje

| Cenario | Decisao projetada | Condicao nomeada |
|---|---|---|
| Ato apenas sobre as **cinco Cartas** *(item 1)* | **`GO-CONDITIONAL`** | **RD-02** — a ambiguidade de veto Guarda × Plataforma em FND-02 §4 **toca autoridade**, e `GO-TO-SPECS` exige *"nenhuma divida que comprometa autoridade ou consumo"* |
| Ato sobre **cinco Cartas + tres emendas** *(itens 1 e 2)* | **`GO-CONDITIONAL`** | **RD-02**, igualmente. As emendas fecham RC-01, RC-05 e RC-07 — **nenhum dos tres e RD-02** |
| Ato sobre **tudo, incluindo C3** *(itens 1 a 4)* | **`GO-CONDITIONAL`** | **RD-02** permanece: a emenda C3 alcanca **FND-01 §7.3**, e RD-02 vive em **FND-02 §4** |

> **A projecao e a mesma nos tres cenarios, e isso e informacao.** Nenhum ato possivel hoje
> produz `GO-TO-SPECS`, porque o unico impedimento que sobra **nao esta na mesa do Soberano**:
> esta numa celula de FND-02 §4 que ninguem tinha lido contra a propria leitura obrigatoria da
> tabela. **Levar RD-02 ao ato de hoje seria antecipacao** — ele nasceu nesta missao, nao passou
> por RFC, e emendar FND-02 e **C2 com ADR**, nao materia de ratificacao.

## 12. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Pacote das cinco Cartas | [PS-2026-002](pacote-soberano-2026-07-28-cartas.md) — **nao alterado**; integridade reconferida em §1.1 |
| Pacote das tres emendas | [PS-2026-003](pacote-soberano-2026-07-29-emendas.md) |
| Projecao comparativa e coerencia 9/9 | [`departments/README §2 e §2.2`](../departments/README.md) — **fonte unica** |
| Contrato das Cartas | [ADR-0011](../decisions/ADR-0011-contrato-de-carta-de-departamento.md), DC-01 a DC-10 |
| Integridade do ato | [ADR-0012](../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md), IR-01 a IR-12 |
| Emenda C3 candidata | [RFC-0011](../rfcs/RFC-0011-emenda-constitucional-ratifica-homologa.md) → [ADR-0014](../decisions/ADR-0014-candidato-emenda-fnd-01-7-3-homologa.md) |
| Verificacao de aptidao desta missao | [FIT-2026-009](fitness/FIT-2026-009-ativacao-e-endurecimento.md) |
| Incidente cuja causa este `BLOCKED` evita repetir | [INC-2026-001](incidents/INC-2026-001-ratificacao-inferida.md) |
| Baseline anterior | **`BL-2026-07-28-06`** — preservada, **nao editada** (BL-02) |
| Baseline emitida por esta missao | **`BL-2026-07-29-01`** — [catalogo mestre §10](artifact-registry.md) |
| Copia datada anterior as edicoes | **131** arquivos, fora do acervo (PI-07, AF-35) |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-GOV | Pacote de transicao da **Missao 1.10**. Decisao **`BLOCKED`** por pre-condicao 1: o ato chegou com marcadores em vez de versao e hash. **Integridade das nove Cartas verificada por oito vias, sem uma unica divergencia**; `H-P` das cinco **projetado** para tornar a aplicacao do ato verificavel por terceiro; restaurabilidade de `DEP-QAR` 1.0.0 confirmada por quatro vias, **sem segunda Carta canonica**. Contrato de consumo **testado** em quatro perguntas — **T1 a T3 passam, T4 falha por desenho**. Mapa **Departamento → Capability → artefato futuro** e **dez requisitos** para o Specification Framework, todos derivados de fonte existente. Divida reconciliada em cinco estados, **zero fechamentos por renomeacao**. **Cinco achados novos** — RD-01 a RD-05 —, um deles corrigido e um tratado. **Minuta do ato entregue com os valores preenchidos.** |
