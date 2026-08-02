---
id: RFC-0018-sede-canonica-do-framework-de-specifications
titulo: Onde deve viver, em definitivo, a norma da Spec — a sede canonica do Framework de Specifications
tipo: rfc
versao: 1.0.0
status: aprovado
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-GOV
criado_em: 2026-07-29
atualizado_em: 2026-07-29
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0006, ADR-0008, ADR-0009, ADR-0012, ADR-0018, ADR-0019, ADR-0021]
substitui: []
substituido_por: null
resumo: Submete a analise a promocao de SF-01 a SF-32 de ADR-0021 para FND-11, com quatro opcoes, o custo medido de cada uma e a unica alteracao de merito que a promocao produz.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# RFC-0018: A sede canonica do Framework de Specifications

> **Pergunta em uma frase.** `ADR-0021` instituiu a norma da `Spec` **dentro de um artefato
> `M1` que nunca se emenda**, declarando na propria decisao que **`FND-11` seria a sede melhor**
> e estava fora de alcance. **Esta RFC pergunta se e hora de mover, e a que custo.**

## Proposito

Submeter a analise **onde a norma da `Spec` deve viver em definitivo**, com as opcoes reais, o
custo medido de cada uma e o efeito de cada uma sobre o **merito** das 32 regras vigentes.

**Esta RFC nao decide, nao promove, nao emenda e nao cria `Spec`.**

## Escopo

| Item | Definicao |
|---|---|
| Inclui | A **sede** de `SF-01` a `SF-32`; a **classe** e o **tipo** da promocao; a cascata em `FND-01` e `FND-03`; o **regime de mutabilidade** da norma promovida |
| **Nao** inclui | O **merito** de qualquer `SF-*` · o **vinculo `Spec` × `Produto`** *(`RD-33` — nao reaberto)* · a criacao de `Spec`, `Produto` ou `Projeto` · a ampliacao da `Spec` a materia nao-produto *(`S2` de ADR-0021 §7.3)* · `RD-27`, `RD-36` · a propagacao de `QG-1` nas Cartas — materia de [RFC-0019](RFC-0019-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md) |
| Origem | Determinacao da **Missao 1.13.1**; §6 de [ADR-0021](../decisions/ADR-0021-framework-de-specifications.md), que declarou `FND-11` como sede melhor e inexecutavel naquela missao |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| Propoe | **DEP-GOV** | [FND-09 §8.2](../foundation/09-meta-model.md), linha `FND` — *propoe/cria* |
| Materia | **DEP-PRD** | Dono do tipo `SPC`; **autor do merito** em ADR-0021. Consulta obrigatoria |
| Analise de risco | **DEP-QAR** | FND-07 §3.1 |
| Valida forma | **DEP-GOV** | FND-09 §8.2, linha `RFC` |
| **Decide** | **SOBERANO** | **C3**, se a opcao escolhida emendar a Fundacao |

---

## 1. Situacao atual — medida

| # | Fato | Valor | Fonte |
|---|---|---|---|
| **S1** | A norma da `Spec` vive **dentro de um ADR** | `SF-01` a `SF-32`, `ADR-0021` §5.1 a §5.10 — **157 linhas** | [ADR-0021](../decisions/ADR-0021-framework-de-specifications.md) |
| **S2** | Esse ADR e **`M1`** | *"O texto **nunca** muda"*; corrige-se **superando** | `FND-10 §6.2`; `AC-10`; `CC-01`; `LV-04` |
| **S3** | Corrigir **uma virgula** de `SF-16` exige | **1 ADR novo** | `SF-32`; `CC-06`, `SU-01` |
| **S4** | O acervo **ja tem** a forma documental adequada, e ela e `FND` | *"**Framework** · entidade `FND` · Norma que estrutura um dominio inteiro e e consumida por todos · `foundation/NN-*.md`"* | `FND-10 §4.1` |
| **S5** | `FND-01 §10` enumera o nivel 2 por **nome de documento**, e a lista tem **nove** membros | `Estrutura Organizacional / Taxonomia / Governanca / Comunicacao / Memoria / Decisoes / Capability Framework / Meta Model / Artifact Framework` | `FND-01 §10` |
| **S6** | `FND-03 §7` enumera os arquivos de `foundation/` **um a um**, de `01` a `10` | **10** linhas de arvore | `FND-03 §7` |
| **S7** | **Nenhuma `Spec` existe**, e nenhuma e criavel | **0** `SPC` · **0** `PRO` · `products/` ausente | `RD-33`, **aberto e bloqueante** |
| **S8** | As **32** regras sao **determinadas, nao observadas** | ressalva `R1` | [FIT-2026-015](../governance/fitness/FIT-2026-015-framework-de-specifications.md) |
| **S9** | O acervo **ja pratica** projecao declarada **dentro de fundacional** | **2** ocorrencias medidas: `FND-10 §10.3` *(projecao de FND-09 §8.2)* e a coluna *Local* de `FND-10 §4.1` a `§4.7` *(projecao de FND-03 §7)* | `FND-10`; `PJ-02`; `ADR-0008` |
| **S10** | `FND-01 §11` declara a **Fundacao** como *"o conjunto dos **nove** documentos fundacionais (FND-01 a **FND-09**)"* — e **FND-10 existe e e fundacional desde ADR-0006** | **defasagem de um documento**, vigente desde `FND-01` **1.3.0** | Achado **novo** desta RFC — **`RD-38`** |

## 2. Problema

**A norma esta na sede errada, e o defeito nao e estetico: e de custo de correcao e de
localizacao.**

### 2.1 O defeito de custo de correcao

`ADR-0021` aceitou o tradeoff por escrito (`VD-04`): *"as regras `SF-*` vivem em artefato `M1`
e **nao se emendam** — corrigi-las exige **ADR sucessor**"*. **A consequencia e assimetrica:**
a norma de um dominio inteiro passa a ter o regime de mudanca de uma **decisao pontual**, que e
o oposto do que `FND-10 §4.1` reserva a cada uma das duas formas — *Framework* estrutura um
dominio; *ADR* resolve um ponto.

### 2.2 O defeito de localizacao

**Quem procura a norma de um dominio procura em `foundation/`.** Hoje, quem procurar a norma da
`Spec` ali **nao a encontra** — encontra o **template**, que e forma, e nao regra. A norma esta
em `decisions/`, misturada as **21** decisoes pontuais.

### 2.3 O que NAO e o problema

| Nao e problema | Verificacao |
|---|---|
| O **merito** das 32 regras | **Nenhuma foi contestada.** `FIT-2026-015` deu `apto-com-ressalva`, e as tres ressalvas sao sobre **ausencia de instancia**, nao sobre conteudo |
| A **classe** de `ADR-0021` | Contestavel e **declarada como tal** pelo proprio ADR §11. **Esta RFC nao a reabre** |
| O **bloqueio** de `RD-33` | Mover a sede **nao desbloqueia nada**: o bloqueio esta na pre-condicao de `FND-04 §6` e no local canonico de `FND-03 §3.6` e `FND-10 §4.4` |

## 3. Criterios de avaliacao — **declarados antes das opcoes**

| # | Criterio |
|---|---|
| **K1** | **Sede correta pela forma documental** — a norma de um dominio deve viver onde `FND-10 §4.1` a aloja |
| **K2** | **Zero alteracao silenciosa de merito** — toda diferenca entre a norma antiga e a nova deve ser **declarada regra por regra** |
| **K3** | **Zero identificador renumerado** — `SF-nn` deve sobreviver, porque `ADR-0021`, `FIT-2026-015`, `TPL-spec`, `MEM-APR-0006` e cinco indices ja os citam |
| **K4** | **Zero titular, portao, papel, classe ou verbo de autoridade novo** |
| **K5** | **Zero alteracao no vinculo `Spec` × `Produto`**, na sequencia por Produto e nos locais canonicos |
| **K6** | **`ADR-0021` nao e editado** (`M1`, `CC-01`, `LV-04`) |
| **K7** | **Cascata integralmente enumerada e executada no mesmo pacote** (`CV-04`, `CC-03`) |
| **K8** | **Custo de reversao declarado e barato enquanto nao existir `Spec`** |

## 4. Opcoes

### Opcao A — **`FND-11`, documento fundacional proprio** *(recomendada)*

Promove `SF-01` a `SF-32` a `foundation/11-framework-specifications.md`, forma **Framework**,
entidade `FND`, `M2`. Exige emenda a **`FND-01 §10`** *(nivel 2)*, a **`FND-01 §11`** *(verbete
`Fundacao`)*, a **tabela de documentos derivados de `FND-01`** e a **`FND-03 §7`** *(arvore)*.

| Criterio | Atende? | Evidencia |
|---|---|---|
| K1 | ✅ | `FND-10 §4.1`, linha *Framework* |
| K2 | ✅ | **30** regras `T-IDENTICA`, **1** `T-REFERENCIAL`, **1** `T-MERITO-DECLARADO` — medido por `diff` |
| K3 | ✅ | **32 de 32** identificadores preservados |
| K4 | ✅ | **0** criados; **7 portoes antes, 7 depois** |
| K5 | ✅ | **0 bytes** em `FND-03 §3.6`, `FND-04 §6` e `FND-10 §4.4` |
| K6 | ✅ | **0 bytes** em `ADR-0021` |
| K7 | ✅ | **2** fundacionais + **6** indices `M3`, enumerados |
| K8 | ✅ | **0 Specs existem, logo 0 migram** |

**Custo medido:** 1 RFC + 1 ADR `C3 · Tipo 1` + **3 candidatos** *(`FND-11` novo, `FND-01`
1.6.0, `FND-03` 1.6.0)* + 1 pacote soberano + **1 ato do Soberano** + cascata em **6** indices.

### Opcao B — **Secao nova dentro de `FND-10`**

| Criterio | Atende? | Por que falha |
|---|---|---|
| K1 | ⚠️ **parcial** | `FND-10` e o contrato **universal** do artefato. Alojar a norma de **um** tipo dentro dele inverte a relacao geral/especial e cria precedente para 32 secoes |
| K7 | ❌ | `FND-10` tem **`H-N` publicado** por ato soberano; acrescentar secao altera `H-N` de objeto promulgado — `IR-05` |
| Outros | ✅ | — |

**Recusada.** E a opcao que a **Missao 1.13 vedou expressamente** por `RD-27`, e a razao segue
valendo: **o custo nao e escrever a secao, e o `H-N`**.

### Opcao C — **Manter em `ADR-0021`, como esta**

| Criterio | Atende? | Por que falha |
|---|---|---|
| K1 | ❌ | A norma de um dominio permanece com o regime de mudanca de uma decisao pontual |
| K2–K8 | ✅ *(por vacuidade)* | Nada muda, logo nada se altera |

**Recusada, e nao por ser errada — por ser provisoria por construcao.** Foi a escolha **certa**
para a Missao 1.13, que **nao podia** emendar fundacional. **A opcao Z de outra missao nao e a
opcao Z desta.**

### Opcao D — **`FND-11` sem emendar `FND-01` e `FND-03`**

Criar o documento e **nao** inscreve-lo na hierarquia nem na arvore canonica.

| Criterio | Atende? | Por que falha |
|---|---|---|
| K1 | ⚠️ | O arquivo estaria no lugar certo e **nao seria norma**: `FND-01 §10` define a hierarquia por **enumeracao**, e o que nao consta **nao ocupa nivel** |
| K7 | ❌ | Produziria um `FND` **orfao** — exatamente o defeito que `LN-07` e `PI-03` proibem |

**Recusada: e a aparencia da Opcao A sem o efeito dela.** Seria promover a sede e **nao**
promover a norma.

### Opcao Z — **Nao fazer nada agora, e decidir depois da primeira `Spec`**

**Recusada, com o argumento invertido em favor de quem a defende.** O momento de mover e
**agora, e precisamente porque nao existe `Spec`**: `0` Specs existem, logo **`0` migram**
(`LC-05`), e o custo de reversao e o mais baixo que jamais sera. **Esperar a primeira `Spec`
torna a mesma mudanca mais caro, nao mais seguro.**

## 5. A unica alteracao de merito, submetida em separado

**A promocao muda o regime de mutabilidade da norma, e isso e merito.**

| | `ADR-0021` — `M1` | `FND-11` — `M2` |
|---|---|---|
| Como se corrige | **ADR sucessor** | **Emenda por versao** |
| Quem aprova a correcao | Conforme a classe do ADR *(hoje: `DEP-EXE`)* | **SOBERANO**, sempre |
| Texto anterior | Preservado no ADR superado | Preservado no historico |

> **O tradeoff e o inverso do intuitivo, e por isso esta destacado.** Sob `M1`, corrigir
> `SF-16` custava **um ADR `C2 · Tipo 2` e nenhum ato do Soberano**. Sob `M2`, custa **uma
> emenda e um ato do Soberano**, porque `FND` nao vigora sem ratificacao (`LM-02`).
> **Promover nao facilita: protege.** Quem quiser a norma mais facil de mudar deve escolher a
> **Opcao C**, e a escolha e legitima.

## 6. Recomendacao do proponente

| Campo | Conteudo |
|---|---|
| **Recomendacao** | **Opcao A** — `FND-11`, com emenda a `FND-01` e `FND-03` no mesmo pacote |
| **Classe proposta** | **C3** — altera a **hierarquia normativa** de `FND-01 §10` e a **propria Fundacao** (FND-04 §2) |
| **Tipo proposto** | **1** — pela **regra da duvida** (`GV-03`) e pela classificacao **mais restritiva** (`FND-01 §7.1.6`): institui norma **assumida como permanente**, e a reversao, embora tecnicamente barata hoje, **exige novo ato do Soberano** |
| **Instrumento** | **RFC → analise de impacto → ADR → ratificacao do SOBERANO** (FND-04 §2, C3) |
| **Fundamento** | **A forma documental correta ja existe e esta escrita** (`FND-10 §4.1`); **a promocao nao altera merito algum exceto o regime de mutabilidade**, e essa alteracao esta isolada e submetida em separado (§5); **`0` Specs existem, logo `0` migram** e o custo de reversao e o menor que jamais sera |
| **Contrapartida honesta** | **A autoria volta a DEP-GOV** — `FND-09 §8.2` nomeia um unico proponente de `FND` —, e isso **regride** a resposta a `RC-02` que `ADR-0021` havia produzido. Achado **`RD-39`**, declarado e nao resolvido |

## 7. Impacto previsto

| Objeto | Efeito | Executado nesta RFC? |
|---|---|---|
| **`FND-11`** *(novo)* | **399 linhas**, perfil `sob-demanda` | **Nao** — candidato fora do acervo |
| **`FND-01`** | **§10** *(+1 linha)*, **§11** *(1 verbete corrigido)*, *Documentos derivados* *(+1 linha)*, historico *(+1)*. **485 → 488** | **Nao — depende de ato** |
| **`FND-03`** | **§7** *(+1 linha na arvore)*, historico *(+1)*. **631 → 633** | **Nao — depende de ato** |
| **`ADR-0021`** | **`0` bytes.** Permanece `ativo` e e a fonte historica do merito | — |
| **`FND-04`, `FND-09`, `FND-10`, `TPL-spec`** | **`0` bytes.** `FND-10 §4.1` e `§10.3` **ja cobrem** a forma *Framework* sem alteracao | — |
| **Indices `M3`** | **6** — catalogo mestre, `README` raiz, `foundation/README`, `decisions/README`, `rfcs/README`, `governance/README` | **Sim** — cascata `CV-04` desta RFC e do ADR |
| **Entidades · tipos · portoes · papeis · classes · verbos** | **0 criados · 0 alterados** | — |
| **Niveis da hierarquia normativa** | **8 antes, 8 depois.** O nivel 2 recebe um **decimo primeiro membro**; **nenhum nivel e criado, removido ou reordenado** | — |

## 8. Riscos

| # | Risco | Prob. | Impacto | Mitigacao |
|---|---|---|---|---|
| **RR-1** | **A promocao ser lida como reabertura do merito** das 32 regras | Media | **Alto** | §2.3 e o §2 do candidato: **30 regras byte a byte**, medido por `diff`. `K2` e criterio, nao promessa |
| **RR-2** | **`FND-11` virar segunda fonte de verdade sobre autoridade** | Media | **Alto** | As duas projecoes carregam declaracao `PJ-02` completa e `PJ-03` da precedencia a fonte. **Precedente medido:** `FND-10` ja carrega **2** projecoes declaradas *(S9)* |
| **RR-3** | **`CC-05` ser lido como proibicao de projecao em fundacional** | Media | Medio | `CC-05` proibe **reproducao nao declarada**; `PJ-02` e o instrumento que a torna licita, e `ADR-0008` o institui. **Sem `PJ-02`, a projecao seria defeito — e por isso as duas a carregam** |
| **RR-4** | **O ato nao vir** | Media | Baixo | `ADR-0021` **continua vigente e intacto**: a norma **nao fica sem sede**, fica na sede provisoria. **Nenhum bloqueio novo** |
| **RR-5** | **`FND-01` ser emendada sem os quatro campos de `AC-08`** — terceira ocorrencia de `RD-27` | **Alta** | Medio | **Declarada, nao contornada.** §9, `Q2`: o pacote publica **duas variantes** do candidato, `V1` *(escopo estrito)* e `V2` *(que fecha `RD-27` quanto a `FND-01`)*, **cada uma com seu hash** — a escolha e do Soberano |
| **RR-6** | **A autoria concentrar em DEP-GOV** | **Observada** | Medio | `RD-39`. Mitigacao real e insuficiente: **DEP-PRD e consulta obrigatoria**, **DEP-QAR revisa**, e **o merito nao e escrito por DEP-GOV** — e recebido |

## 9. Perguntas em aberto — **escaladas ao SOBERANO**

| # | Pergunta | Por que nao se resolve aqui |
|---|---|---|
| **Q1** | **A promocao e `Tipo 1` ou `Tipo 2`?** O proponente propoe **`Tipo 1`** pela regra da duvida; ha argumento real para `Tipo 2` — *"`0` Specs existem, logo reverter e trivial"* | Classificar **mais restritivamente** e determinacao de `FND-01 §7.1.6`, mas **quem decide a classe em ultima instancia e o Soberano** |
| **Q2** | **`FND-01` 1.6.0 entra como `V1` ou `V2`?** `V2` acrescenta os **quatro** campos de `AC-08` e **fecha `RD-27` quanto a `FND-01`** *(`FND-02` permanece aberta)* | A Missao 1.13.1 determinou **nao tratar `RD-27`**. O proponente **cumpre a determinacao** submetendo `V1` como objeto e `V2` como alternativa medida — **decidir por `V2` e autorizar o tratamento** |
| **Q3** | **`ADR-0021` deve receber `superado_por: ADR-0022` no frontmatter?** `FND-10 §6.2` autoriza *"o estado e os campos de sucessao"* em `M1`; `CC-01` diz *"nem para completar campo"* | **Colisao real entre duas regras de `FND-10`.** O proponente **nao toca `ADR-0021`** e registra a sucessao **no indice**, que e o que `CC-01` prescreve — e submete a alternativa com `H-P` medido |

## 10. Resultado

| Campo | Conteudo |
|---|---|
| **Estado** | **ACOLHIDA** → [ADR-0022](../decisions/ADR-0022-sede-canonica-do-framework-de-specifications.md) |
| **Opcao escolhida** | **A** |
| **Alternativas recusadas** | **B** *(`H-N` de objeto promulgado — `IR-05`)* · **C** *(provisoria por construcao)* · **D** *(`FND` orfao)* · **Z** *(o custo cresce, nao decresce, com o tempo)* |
| **Aberto** | `Q1`, `Q2`, `Q3` — **as tres para o Soberano**, e nenhuma bloqueia a submissao |
| **Achados que abre** | **`RD-38`** *(Baixa — o verbete `Fundacao` de `FND-01 §11` conta nove documentos e existem dez)* · **`RD-39`** *(Baixa — `RC-02`, oitava ocorrencia: a autoria de `FND` e de DEP-GOV por determinacao da matriz)* |

## 11. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Origem | Missao 1.13.1; [ADR-0021 §6](../decisions/ADR-0021-framework-de-specifications.md) |
| Decisao resultante | [ADR-0022](../decisions/ADR-0022-sede-canonica-do-framework-de-specifications.md) |
| Pacote soberano | [PS-2026-009](../governance/pacote-soberano-2026-07-29-fnd-11.md) |
| RFC irma, **materia separada** | [RFC-0019](RFC-0019-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md) — `RD-31` |
| Regra de integridade | [ADR-0012](../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md), `IR-01` a `IR-10` |
| Achado que **nao** fecha | **`RD-33`** — o vinculo `Spec` × `Produto` permanece integralmente vigente |
| Baseline vigente na submissao | **`BL-2026-07-29-09`** — [catalogo mestre §10](../governance/artifact-registry.md) |

---

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-GOV | Propoe a **sede canonica** de `SF-01` a `SF-32` entre **quatro opcoes e a opcao Z**, com `K1` a `K8` declarados **antes** delas. Recomenda a **Opcao A** — `FND-11`, `C3 · Tipo 1` — e submete **em separado** a **unica alteracao de merito** que a promocao produz: o regime de mutabilidade, de `M1` para `M2`, **com o tradeoff declarado no sentido correto — promover protege, nao facilita**. Recusa a **Opcao B** porque acrescentar secao a `FND-10` altera `H-N` de objeto promulgado (`IR-05`), a **Opcao C** por ser provisoria por construcao, a **Opcao D** por produzir `FND` orfao e a **Opcao Z** com o argumento invertido: **`0` Specs existem, logo `0` migram, e o custo de mover so cresce**. Mede **10 fatos** e abre **dois achados** — **`RD-38`** *(o verbete `Fundacao` conta nove documentos fundacionais e existem dez)* e **`RD-39`** *(`RC-02`, oitava ocorrencia — a autoria de `FND` volta a DEP-GOV por determinacao de `FND-09 §8.2`, nao por conveniencia)*. Escala **tres perguntas** ao Soberano, **nenhuma bloqueante**: o **tipo** da decisao, a **variante de `FND-01`** *(`V1` estrita ou `V2` fechando `RD-27`)* e se **`ADR-0021` deve receber `superado_por`**, onde `FND-10 §6.2` e `CC-01` **colidem**. |
