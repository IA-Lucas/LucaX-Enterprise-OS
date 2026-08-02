---
id: PS-2026-004
titulo: Pacote de decisao soberana — emenda C3 a FND-02 §4 que fecha RD-02
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
decisoes_relacionadas: [ADR-0012, ADR-0016]
substitui: []
substituido_por: null
canal: REPORTE
emissor: DEP-GOV
destinatario: SOBERANO
ttl: ate decisao do Soberano
resumo: Submete ao Soberano a emenda C3 a FND-02 §4 que fecha RD-02, com diff literal celula a celula, H-A, H-N e H-P projetado, impacto verificado e minuta do ato preenchida.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# PS-2026-004 — Emenda **C3** a FND-02 §4

> ## Este pacote **informa**. Nao decide, nao aprova, nao promulga e nao edita FND-02.
>
> **FND-02 permanece em 1.2.0**, `ativo`. O candidato **1.3.0** existe como **diff literal +
> hash**, **fora do acervo** — o mesmo desenho de
> [PS-2026-003](pacote-soberano-2026-07-29-emendas.md) e de
> [FIT-2026-007 §F2.a](fitness/FIT-2026-007-revisao-estrutural-i.md). **Nenhum arquivo
> fundacional foi alterado por esta missao.**
>
> **Caminho exato deste pacote:** `governance/pacote-soberano-2026-07-29-rd-02.md` *(RE-01)*.

## Proposito
Levar ao Soberano a emenda que fecha **RD-02** — **o unico achado aberto que toca autoridade**,
e a **condicao nomeada** do fechamento `GO-CONDITIONAL` de
[FIT-2026-010](fitness/FIT-2026-010-aplicacao-do-ato-soberano.md), R4.

## Escopo
| Item | Definicao |
|---|---|
| Inclui | **Um** objeto: `ADR-0016` e a promulgacao de **FND-02 1.3.0** que ele autoriza, com diff literal, `H-A`, `H-N`, `H-P` projetado, impacto e revisao independente |
| **Nao** inclui | **RD-09** — objeto de [PS-2026-005](pacote-soberano-2026-07-29-rd-09.md), **pacote separado por determinacao** · `DEP-KMS` e `DEP-ENG` — [PS-2026-006](pacote-soberano-2026-07-29-kms-eng.md) · `DEP-QAR` 1.2.0, **ja aplicada** · RD-01, RD-03, RD-08, RD-10, RD-11, RD-12 |
| Natureza | **Reporte**, tipo documental de [FND-10 §4.6](../foundation/10-artifact-framework.md), entidade `MSG`. **Nenhum** tipo, entidade, camada, template ou diretorio novo |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| **Autor da emenda** | **DEP-GOV** | FND-09 §8.2, linha `FND` — propoe |
| **Revisor independente** | **DEP-QAR** | RM-06b |
| **Monta este pacote** | **DEP-GOV** | Guardiao normativo |
| **DECIDE** | **SOBERANO** | **C3. Indelegavel** (PI-01, FND-01 §9). **Nao ocorreu** |

> **Residuo declarado (PI-10).** **DEP-QAR e objeto de 2 das 12 celulas** e de **2 das 4 de
> autoridade**. A revisao de merito foi executada por DEP-QAR **sobre texto de DEP-GOV**, e o
> julgamento da propria autoridade e do **SOBERANO** (`DEP-QAR I-5`). **Quarta ocorrencia da
> familia de RC-02**; permanece **declarado, nao resolvido**.

---

## 1. O que se pede

| # | Objeto | Ato pedido | Se **nao** houver ato |
|---|---|---|---|
| **1** | **`ADR-0016`** + promulgacao de **`FND-02` 1.3.0** | **Aprovacao e ratificacao** | FND-02 permanece em **1.2.0**. **RD-02 entra no terceiro ciclo**; `DEP-EXE` e `DEP-KMS` seguem vetados **por Carta e nao pela fonte**; **`GO-TO-SPECS` permanece impossivel** |

## 2. Diff literal

### 2.1 Frontmatter — **3 alteracoes**

| # | Campo | Antes | Depois |
|---|---|---|---|
| **F1** | `versao` | `1.2.0` | `1.3.0` |
| **F2** | `atualizado_em` | `2026-07-28` | `2026-07-29` |
| **F3** | `decisoes_relacionadas` | `[ADR-0001, ADR-0002, ADR-0003, ADR-0004]` | `[ADR-0001, ADR-0002, ADR-0003, ADR-0004, ADR-0016]` |

> **`status` nao muda e nao ha campo `ratificacao` em FND-02.** A promulgacao de fundacional
> **nao executa O4**: quem transita de estado e o **ADR** (§3.2). Por isso **`H-P` = `H-A`** para
> o arquivo fundacional, e a transicao aparece no ADR.

### 2.2 §4 — a legenda passa a §4.1

| # | Antes *(2 linhas)* | Depois |
|---|---|---|
| **L1** | `Legenda: **E** entrega para · **C** consulta obrigatoria · **V** pode vetar · **A** aprova ·` <br> `**—** sem interacao estrutural direta.` | Subsecao **§4.1 Legenda**: declaracao de direcionalidade em 3 linhas + tabela de **6 codigos** com definicao operacional + regra de **celula multivalorada** |

**Os seis codigos, como passam a ser definidos:**

| Codigo | Ato de X sobre Y | Definicao |
|---|---|---|
| `E` | entrega para | X produz e transfere a Y artefato, resultado ou evidencia |
| `C` | consulta obrigatoria | X nao conclui o ato sem ouvir Y. O parecer de Y **nao vincula**; **nao ouvir Y invalida o ato** |
| `V` | pode vetar | X barra o ato de Y. Y **nao executa** enquanto o veto vigorar. So o SOBERANO o reverte (LV-09) |
| `A` | aprova | X **homologa** o ato de Y dentro do rito (FND-01 §7.3). **Nao e ratificacao** |
| **`R`** | **revisa de forma independente** | **CODIGO NOVO.** X e o revisor independente de FND-04 §3.1 sobre o produto de Y |
| `—` | nenhum ato direto | X **nao** pratica ato estrutural direto sobre Y. **Nada afirma** sobre `(Y, X)` |

### 2.3 §4.2 — a matriz: **12 celulas alteradas, 69 inalteradas**

| # | Celula | Antes | Depois | Natureza | Fonte que ja o obriga |
|---|---|---|---|---|---|
| **M1** | `EXE → KMS` | `A` | **`A E`** | interface | QG-5 (FND-01 §6.2); `DEP-EXE §9` — **contribuinte obrigatorio** da camada APR |
| **M2** | `GOV → EXE` | `E` | **`E V`** | **autoridade** | FND-02 §3 *(veto sobre "qualquer componente")*, §6, §7 N3; `DEP-EXE §6.3` |
| **M3** | `QAR → EXE` | `E` | **`E V`** | **autoridade** | FND-02 §3, §6, §7 N3; `DEP-EXE §6.3` |
| **M4** | `GOV → KMS` | `E` | **`E V`** | **autoridade** | Leitura obrigatoria 3; `DEP-GOV §6.3` — *"entrega e veto"*; `DEP-KMS §6.3` |
| **M5** | `QAR → KMS` | `E` | **`E C V`** | **autoridade** | Leitura obrigatoria 3; `DEP-KMS §6.3`; `DEP-QAR §5` — **DEP-KMS e consulta obrigatoria** do veredito `FIT` |
| **M6** | `GOV → QAR` | `C` | **`C R`** | revisao | FND-09 §8.2, linha `FIT` — *"Revisa: DEP-GOV (forma)"* |
| **M7** | `QAR → GOV` | `C` | **`C R`** | revisao | RM-06b; `DEP-QAR §6.3`; `DEP-GOV §6.3` |
| **M8** | `PRD → GRW` | `E` | **`C E`** | interface | `DEP-PRD §6.3` — *"entrega e consulta"* |
| **M9** | `OPS → ENG` | `E` | **`C E`** | interface | `DEP-OPS §6.3` |
| **M10** | `GRW → PRD` | `C` | **`C E`** | interface | `DEP-GRW §6.3` |
| **M11** | `KMS → QAR` | `E` | **`C E`** | interface | `DEP-KMS §6.3` |
| **M12** | `TLS → ENG` | `E` | **`C E`** | interface | `DEP-TLS §6.3` |

**4 de autoridade · 2 de revisao · 6 de interface.**

### 2.4 §4.3 — regras novas: **MI-01 a MI-06**

| # | Regra |
|---|---|
| **MI-01** | A celula e a fonte; as leituras obrigatorias sao **projecao** dela. Em conflito, **prevalece a celula** (ADR-0008, PJ-03) |
| **MI-02** | **A matriz nao concede autoridade**: projeta FND-01 §7.3, FND-02 §2.1 e §3 e FND-09 §8.2. Celula divergente e **erro da tabela** |
| **MI-03** | **O SOBERANO nao figura na matriz.** Autoridade que nele termina le-se em FND-01 §7.3 e FND-09 §8.2 |
| **MI-04** | **Ausencia nao cria nem retira autoridade.** `—` e ausencia de ato **de X sobre Y** |
| **MI-05** | **O veto da Guarda incide sobre o objeto, nao sobre a classe do produtor** |
| **MI-06** | **`R` declara so relacao estrutural e permanente**; o mapa por entidade fica em FND-09 §8.2 |

### 2.5 §4.4 — leituras obrigatorias: **2 corrigidas, 3 inalteradas**

| # | Antes | Depois |
|---|---|---|
| **R1** | *"**Todos entregam a KMS.** Nenhum trabalho termina sem registro na memoria (QG-5)."* | idem **+ *"— o Comando inclusive, contribuinte obrigatorio da camada APR"*** |
| **R2** | *"**GOV e QAR vetam a Linha e a Plataforma, nunca o contrario.**"* | *"**GOV e QAR vetam qualquer departamento — Comando, Linha e Plataforma —, e nenhum departamento veta a Guarda.** So o SOBERANO reverte veto de Guarda (LV-09)."* |
| R3, R4, R5 | *"Todos consultam GOV"* · *"PRD entrega a ENG"* · *"GRW nao instrui ENG"* | **inalteradas** — as tres foram **verificadas por ferramenta** e conferem |

### 2.6 §4.5 — exemplos normativos: **5, todos novos**

`EX-1` veto sobre Comando · `EX-2` veto sobre Plataforma · `EX-3` celula composta ·
`EX-4` `—` direcional · `EX-5` revisao independente.

### 2.7 Historico — **1 linha**

| # | Local | Depois |
|---|---|---|
| **H1** | Historico de versoes | linha `1.3.0`, descrevendo F1 a F3, L1, M1 a M12, MI-01 a MI-06, R1, R2 e os cinco exemplos |

**Total: 3 de frontmatter · 1 de legenda · 12 celulas · 6 regras novas · 2 leituras ·
5 exemplos · 1 de historico.**
**479 → 518 linhas *(+39)* · 57 linhas acrescentadas · 18 substituidas · 9 blocos de diff.**

## 3. Identificadores de integridade

### 3.1 `FND-02` — o documento a promulgar

| Campo | Valor |
|---|---|
| **Versao em vigor hoje** | **1.2.0** · **479** linhas |
| `H-A` **em vigor** | `abde9d9097b262c5394320a99c4fd0f31c40057565c47ab676d9611587bd9138` |
| `H-N` **em vigor** | `00cffb3339923d07ae0571a9f7654e482e35830b9ed29fa31b669268f2e57cc2` |
| **Versao candidata** | **1.3.0** · **518** linhas |
| **`H-A` do candidato** | **`a42fadbf4258b7526f3b5fbdcb0fcea4f93f17528c6ab484530acc533f3530e3`** |
| **`H-N` do candidato** | `1dddf9ff048834664f8236b76b0816a184337166f0de9d7945afa853a006ae6f` |
| **`H-P` projetado** | **identico a `H-A`** — a promulgacao de fundacional **nao executa O4** |

> **`H-N` muda, e deve mudar.** Aqui nao ha transicao de estado: ha **emenda de conteudo**.
> `H-N` invariante seria o sinal de que **nada foi promulgado** — a mesma leitura que
> [MSG-2026-0004 §2.2](../memory/operacional/MSG-2026-0004-ato-soberano-cartas-emenda-constitucional-e-regime-do-fitness-check.md)
> registrou para FND-01 1.4.0.

### 3.2 `ADR-0016` — o objeto que transita de estado

| Campo | Valor |
|---|---|
| Caminho canonico | `decisions/ADR-0016-semantica-da-matriz-de-interacao.md` |
| Versao · linhas | **1.0.0** · **243** |
| Estado hoje | `em-revisao` · `ratificacao: pendente` |
| **`H-A`** | **`90b7e058f377256350715d5d1f508ad3b7843bd85b6bfae15cb0ccb460e85b6a`** |
| `H-N` | `891e6209fece70d5bcb7f1b7a54b6cc131a82926ea8685f64ed228fcc5238b88` |
| **`H-P` projetado** *(apos O4)* | **`07cbba119a7bc392d8ab6fdebe3176290fb90a6e9b448640aa1931026d8bf039`** |
| `H-N` apos O4 | **invariante** — `891e6209…3b88` (IR-02, IR-06) |

> **`H-P` publicado antes de existir.** Se o arquivo pos-transicao nao reproduzir exatamente
> `07cbba11…f039`, houve alteracao alem do diff — e isso e **IR-05**. Exercicio preditivo de
> `IR-07`, conferido em **6 de 6** na aplicacao anterior (FIT-2026-010, F6).

### 3.3 `RFC-0012` — proposta antecedente

| Campo | Valor |
|---|---|
| Caminho · versao · linhas | `rfcs/RFC-0012-semantica-da-matriz-de-interacao.md` · **1.0.0** · **258** |
| `H-A` | `eb3c8180007988cd77b516f3c4fff39cb41c627798ab147e43ece76f7ba8d201` |
| Estado | `aprovado` — **`RFC` nao se ratifica** (FND-09 §8.2, linha `RFC`) |

## 4. Impacto — verificado item a item

| Dimensao | Impacto | Como foi verificado |
|---|---|---|
| **Autoridade criada** | **ZERO** | `V` continua exclusivo de GOV e QAR. Teste **T3** *(veto por nao-Guarda)* = **zero** antes e depois |
| **Titulares de decisao alterados** | **ZERO** | FND-01 §7.3 **nao e tocada** — nenhuma celula, nenhuma linha |
| Departamentos **com** veto | **2 → 2** | GOV, QAR |
| Departamentos **vetaveis na tabela** | **5 → 7** | E **7 ja se declaravam vetados nas proprias Cartas** — 14 afirmacoes, 0 excecoes |
| **Cartas alteradas** | **ZERO** | Nenhum arquivo de `departments/` tocado por este pacote |
| Documentos fundacionais emendados | **1** | FND-02. **FND-01 e FND-03 a FND-10 intactas** |
| Entidades · tipos · camadas · portoes · departamentos · classes | **0 criados · 0 alterados** | 21·33·5·7·9·4 antes e depois |
| Ciclo de veto · dupla aprovacao · conflito de segregacao | **0 · 0 · 0** | Testes **T9**, **T10**, **T11** reexecutados sobre o candidato |
| Projecoes a atualizar | **1** — `departments/README` *(nenhuma linha da comparacao de Cartas muda; a citacao de §4 passa a §4.2)* | — |
| Custo de contexto | **+39 linhas.** FND-02 nao e `nucleo`, mas integra o pacote minimo de **`DEP-EXE`**: o piso dele passa de **1.579** a **1.618** linhas | `DEP-EXE §9.1` |
| Reversibilidade | **Tipo 2** — sem dado vivo, sem exposicao externa, sem migracao, sem credencial | ADR-0016 §10 |

## 5. O que **nao** esta neste pacote

| Objeto | Por que |
|---|---|
| **RD-09** | **Pacote separado por determinacao da missao** — [PS-2026-005](pacote-soberano-2026-07-29-rd-09.md). Materias distintas nao se misturam em um ato |
| **`DEP-KMS` 1.1.0 · `DEP-ENG` 1.1.0** | [PS-2026-006](pacote-soberano-2026-07-29-kms-eng.md) |
| **`DEP-QAR` 1.2.0** | **Ja aplicada** por ato de 2026-07-29 — [MSG-2026-0005](../memory/operacional/MSG-2026-0005-ato-soberano-aplicacao-dep-qar.md) |
| **RD-01** *(citacao em `DEP-PRD §8.2`)* · **RD-03** *(`DEP-KMS §6.3`)* · **RD-10** *(`DEP-TLS §6.3`)* · **RD-11** *(4 residuos de Carta)* | **Todos exigem emenda a Carta em vigor**, cada uma com ato proprio (IR-01, DC-09). **Nenhum e corrigivel por esta emenda**, e nenhum foi corrigido em silencio |
| **RD-08** *(`ADR-0014`)* · **RD-12** *(`FND-04 §2.1`)* | Contidos, com dono e gatilho — [PT-2026-002](relatorio-transicao-2026-07-29-fechamento.md) |
| Spec, agente, skill, workflow, produto, codigo, banco, infraestrutura, ontologia, migracao | **Nenhum foi criado**, por determinacao |

## 6. Minuta do ato — **pronta, com os valores verificados**

> ### Esta secao **nao e um ato**, e nada aqui produz efeito.
> Entregar a minuta **preenchida** e a resposta a **RD-05** e a **RD-07**, as duas ocorrencias em
> que valor publicado nao chegou ao ato. **DEP-GOV registra o ato; nunca o emite** (`DEP-GOV §7`).

```
ATO SOBERANO DO FUNDADOR — <data do ato>

Apos revisar governance/pacote-soberano-2026-07-29-rd-02.md, RFC-0012, ADR-0016,
suas evidencias, revisao independente, riscos e ressalvas:

Aprovo e ratifico expressamente:

- ADR-0016, versao 1.0.0,
  SHA-256 90b7e058f377256350715d5d1f508ad3b7843bd85b6bfae15cb0ccb460e85b6a.

Autorizo a promulgacao das alteracoes correspondentes em FND-02 na versao 1.3.0,
SHA-256 do documento promulgado
a42fadbf4258b7526f3b5fbdcb0fcea4f93f17528c6ab484530acc533f3530e3,
exatamente no diff literal registrado em PS-2026-004 §2.

A entrada em vigor depende de verificacao independente de identidade, versao, hash
integral, diff literal, revisao e inexistencia de alteracao entre o candidato revisado
e o objeto a ser aplicado. FND-02 1.2.0 devera permanecer recuperavel como versao
historica substituida.

Este ato nao amplia titulares, competencias ou direitos decisorios alem do conteudo
expressamente ratificado; nao alcanca RD-01, RD-03, RD-08, RD-09, RD-10, RD-11 nem
RD-12; nao ratifica futuras emendas; e nao alcanca qualquer objeto nao enumerado
expressamente.
```

## 7. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Achado que fecha | **RD-02** — [PT-2026-001 §10](relatorio-transicao-2026-07-29-departamentos.md) |
| Ressalva que fecha | **R4** de [FIT-2026-010](fitness/FIT-2026-010-aplicacao-do-ato-soberano.md) |
| RFC → ADR | [RFC-0012](../rfcs/RFC-0012-semantica-da-matriz-de-interacao.md) → [ADR-0016](../decisions/ADR-0016-semantica-da-matriz-de-interacao.md) |
| Regra de integridade aplicada | [ADR-0012](../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md), `IR-01` a `IR-10` |
| Precedente de forma | [PS-2026-003](pacote-soberano-2026-07-29-emendas.md) · [PT-2026-001 §8](relatorio-transicao-2026-07-29-departamentos.md) |
| Pacotes irmaos, **nao alcancados por este** | [PS-2026-005](pacote-soberano-2026-07-29-rd-09.md) · [PS-2026-006](pacote-soberano-2026-07-29-kms-eng.md) |
| Relatorio que consolida a missao | [PT-2026-002](relatorio-transicao-2026-07-29-fechamento.md) |
| Verificacao de aptidao | [FIT-2026-011](fitness/FIT-2026-011-fechamento-de-autoridade.md) |
| Baseline vigente na submissao | **`BL-2026-07-29-04`** — [catalogo mestre §10](artifact-registry.md) |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-GOV | Pacote da **Missao 1.11**: emenda **C3** a **FND-02 §4** que fecha **RD-02**, com **diff literal** campo a campo e celula a celula — **3** de frontmatter, **1** de legenda, **12 celulas**, **6 regras novas**, **2 leituras corrigidas**, **5 exemplos normativos** e **1** de historico —, `H-A`, `H-N` e **`H-P` projetado** do ADR, impacto **verificado item a item** e **minuta do ato preenchida**. **479 → 518 linhas.** **Zero autoridades criadas · zero titulares alterados · zero Cartas editadas · zero entidades, tipos, camadas ou portoes novos.** **Quarto pacote soberano do sistema**, e o primeiro a submeter emenda a **FND-02**. |
