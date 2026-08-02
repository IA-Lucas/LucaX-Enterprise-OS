---
id: PT-2026-018
titulo: Missao 1.13.5.1 — a emenda que sana RD-91, e por que a celula que o achado nomeava nao era a sede
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
decisoes_relacionadas: [ADR-0032, ADR-0019, ADR-0021, ADR-0022, ADR-0031]
substitui: []
substituido_por: null
resumo: Registra a producao dos instrumentos que sanam RD-91, a medicao do Item 0 que redirecionou a emenda da projecao para a fonte, e os cinco achados novos.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# PT-2026-018 — Missao 1.13.5.1: a emenda que sana `RD-91`

> **Registro de missao. Nao e norma, nao institui nada e nao decide nada.**

## 1. O que a missao fez

**Produziu os instrumentos do rito `C3` que sanam `RD-91`, e nao aplicou nenhum deles.** O
defeito: a coluna `C1 · T2` poe *Proposta* e *Aprovacao* no mesmo Departamento para `SPC`,
tornando a aprovacao **nula** por `LV-03` — e o piso de `FND-04 §6`, **inutilizavel**.

| Etapa | Resultado |
|---|---|
| **Pre-condicoes** | `baseline.sh` reproduzido **antes** de qualquer escrita: **223 · 66.143 · `1aae3f4f…ba56`** · copia datada de **602** arquivos · `H-A` integral de **602** · lease **token 14** e **15** |
| **Item 0** | **Medido e reportado ao Fundador antes de redigir.** Ele reafirmou o menu, e a decisao de escopo foi exercida por ele |
| **Rito** | `RFC-0027` → `ADR-0032` → `FIT-2026-025` → `PS-2026-017` → este registro |
| **Classe** | **`C3 · Tipo 2`**, determinada por **quatro** fundamentos citados, nunca por analogia |
| **Candidatos** | **4**, **fora do acervo**, com `H-A`, `H-N` e `H-P` publicados |
| **Achados novos** | **5** — `RD-96` a `RD-100`. **`0` gera missao:** congelamento em vigor |
| **Limites respeitados** | `0` bytes em `FND-01`–`FND-11` · `0` em `TPL` · `0` em `CAP` · `0` em Carta · `0` em `ADR`/`RFC`/`FIT`/`PS`/`PT`/`MSG` historicos · `0` atos emitidos · `0` `Spec` criada · `0` execucoes · `0` historicos editados |

## 2. O Item 0 — o que a medicao encontrou, e o que ela mudou

O despacho mandava **medir antes de emendar** e parar se o defeito passasse de `SPC`. **A
medicao encontrou duas coisas, e a primeira mudou a emenda inteira.**

### 2.1 A celula que o achado nomeava nao tem merito proprio

| Metade da colisao | Texto em `FND-11 §5` | Texto na fonte | Veredito |
|---|---|---|---|
| Quem propoe | `**DEP-PRD**` | `FND-09 §8.2` linha `SPC`, *Propoe/cria* | **reproducao literal** |
| Quem aprova | `proprietario **+ revisor**` | `FND-04 §2.1` linha `C1`, *Aprova* | **reproducao literal** |

`FND-11 §5` e **projecao declarada** (`PJ-02`). `PJ-03`: *"em divergencia, a fonte prevalece, e
o defeito e da projecao"*. `FND-01 §10`: *"sobre autoridade, prevalece sempre o documento de
origem"*. **Consequencia: a emenda que o despacho pedia literalmente — mexer em `FND-11 §5` —
seria inocua.** Ela nao sanaria nada; produziria divergencia.

**A emenda foi redirecionada para a fonte**, com cascata declarada na projecao — a forma que
`ADR-0019 §4` *(Alternativa E)* ja tinha fixado e que `CV-04` exige.

### 2.2 O mesmo defeito existe fora de `SPC` — varredura das 21 linhas de `FND-09 §8.2`

| Linha | Propoe / cria | Aprova | Natureza |
|---|---|---|---|
| **`PRJ`** | `DEP-EXE` | **`DEP-EXE`** | **estrutural e incondicional** — nao existe atribuicao conforme |
| **`TPL`** | **`DEP-GOV`** + dono do tipo | **`DEP-GOV`** | **estrutural** — tres papeis; fere `PI-05` **e** `ES-02` |
| **`SPC`** | `DEP-PRD` | conforme classe → em `C0`/`C1`, o proprietario | **estrutural em `C0` e `C1`** — e `RD-91` |
| `ADR`, `RFC`, `EXC`, `INC`, `AGT`, `SUB`, `SKL`, `WFL`, `MEM` | variavel *(`qualquer DEP`, `quem detecta`, `DEP de origem`…)* | fixo | **contingente** — existe atribuicao conforme, e `FND-04 §3.1` a resolve caso a caso |
| `FND`, `CAP`, `DEP`, `PRO`, `TOL`, `FIT`, `MSG`, `ORG`, `SOBERANO` | — | — | **sem colapso** |

**O criterio que separa as duas colunas:** quando a matriz **fixa os dois papeis no mesmo nome**,
nao ha atribuicao conforme possivel e **toda** aprovacao daquele tipo e nula. Quando um dos
lados e variavel, existe saida.

**Reportado ao Fundador antes de redigir**, como o Item 0 mandava. **Ele reafirmou o menu**, e
a emenda seguiu **no escopo mais estreito que a medicao prova eficaz**: `SPC` apenas, com
`PRJ` e `TPL` **declarados e nao tocados** — `RD-96` e `RD-97`.

## 3. A classe do rito — determinada por norma citada, nunca por analogia

| # | Fundamento | O que ele diz |
|---|---|---|
| 1 | [`FND-04 §2`](../foundation/04-governanca.md), bloco `C3` | *"Altera principio imutavel, linha vermelha, hierarquia normativa, **direitos de decisao** ou a propria Fundacao"* — e a emenda muda **quem aprova** |
| 2 | [`FND-09 §8.2`](../foundation/09-meta-model.md), linha `FND` | *Aprova* **SOBERANO** · *Ratifica* **SOBERANO** |
| 3 | [`SF-32`](../foundation/11-framework-specifications.md) | A emenda de `FND-11` *"so vigora com aprovacao e ratificacao do SOBERANO"* |
| 4 | `LM-02` | `FND` **nao vigora sem ratificacao** |

**Tipo 2**, por `FND-04 §2`, bloco `C3`, campo *Reversao* — *"emenda revogatoria, com mesmo
rito"*. **A distincao nao afrouxa nada:** `FND-04 §2.2` poe `C3` terminando em ratificacao
**em qualquer tipo**.

## 4. O que a emenda faz, em quatro linhas

Em **`FND-09 §8.2`**, linha `SPC`, a coluna *Aprova* passa a dizer **`em C1, DEP-EXE`**, com
nota que declara a derivacao — **nao redefine `FND-04 §2`, aplica `FND-04 §3.1`**. Em
**`FND-11 §5`**, a celula *Aprovacao* × `C1 · T2` passa de `proprietario + revisor` para
**`DEP-EXE + revisor`**, em cascata. As Cartas de **DEP-PRD** *(4 linhas)* e **DEP-EXE**
*(2 linhas)* acompanham, porque a emenda as tornaria falsas. **`0` bytes em `FND-04`.**

## 5. Os tres numeros de custo

| # | Pergunta | Resposta | Natureza do numero |
|---|---|---|---|
| **1** | Primeira `Spec`, em `C2` | **5 artefatos · 1.580 linhas** | **Medido** — `wc -l`, 2026-08-02 |
| **2** | Segunda `Spec`, em `C1`, apos a emenda | **2 artefatos** *(Nota de Decisao + `Spec`)* · **3** com o registro de missao | **Derivado de norma** — `FND-07 §2.3`; `SF-24` item (9); `FND-04 §2` |
| **3** | Esta emenda | **7 artefatos** · **+4 documentos emendados** · **27 linhas** de norma nova | **Medido no precedente** `PS-2026-008` → `MSG-2026-0006`, cadeia identica |

> **`CE-04` respeitado:** o numero **1** e medicao; **2** e derivacao declarada; **3** e
> medicao de precedente. **Nenhum foi estimado**, e a natureza de cada um esta escrita.

## 6. Achados

| # | Achado | Sev. | Dono | Gatilho |
|---|---|---|---|---|
| **`RD-96`** | **`FND-09 §8.2`, linha `PRJ`, poe `DEP-EXE` como quem propoe E como quem aprova.** `Proponente = Aprovador` **incondicional** — nao ha atribuicao conforme possivel, e `LV-03` torna **nula** toda aprovacao de `PRJ`. **E o mesmo defeito de `RD-91`, fora de `SPC`, e nenhum achado anterior o registrava** | **Alta** *(nao bloqueante: `0` `PRJ` existem)* | **SOBERANO** *(so ele emenda `FND-09`)* | *"antes do primeiro `PRJ`, ou proxima emenda de `FND-09 §8.2`"* |
| **`RD-97`** | **`FND-09 §8.2`, linha `TPL`, poe `DEP-GOV` como quem propoe, quem revisa E quem aprova.** Tres papeis no mesmo nome: fere `PI-05` *(Proponente ≠ Aprovador **e** Proponente ≠ Revisor)* e **`ES-02`** *(Guardiao ≠ Proponente)*. **Ja ocorreu na pratica:** `TPL-carta-produto` **1.1.0** foi emendado na Missao 1.13.4.1 com autor e aprovador ambos DEP-GOV | **Alta** | **SOBERANO** | *"proxima emenda de template"* — o mesmo de `RD-63`, que disparou 2 vezes |
| **`RD-98`** | **A partir de `FND-11` 1.1.0 a matriz de `SF-10` difere em 1 celula da copia de `ADR-0021 §5.3`**, que e `M1` e **nunca se emenda**. Prevalece `FND-11`, por `ADR-0022 §5.4` — mas quem resolver autoridade pela copia obtem o valor **superado** | **Media** | DEP-GOV | *"apos o ato"* — declarado em `FND-11 §2` |
| **`RD-99`** | **`FND-04 §2`, bloco `C3`, manda registrar *"nova versao MAIOR do documento"*, e as emendas `C3` exercidas produziram versao MENOR**, por `AL-01`/`CC-02`. **Conflito dentro de `FND-04`.** Esta emenda seguiu a **pratica exercida** e declarou, em vez de resolver em silencio | **Media** | DEP-GOV | *"proxima emenda a `FND-04`"* — o mesmo de `RD-18` |
| **`RD-100`** | **`FND-11 §14`, limites `L1` e `L2`, ficaram falsos em 2026-08-02** — *"nenhuma `Spec` real existe"* e *"o valor sera medido na primeira `Spec`"*. `SPC-001` existe e `SF-09` foi medido em **603** linhas. **Esta emenda NAO os corrige**: nao sao a celula autorizada | **Baixa** | DEP-GOV | *"proxima emenda de `FND-11`"* |

**`RD-91` NAO fecha aqui.** Fecha **pelo ato**, e **parcialmente**: `C0 · T2` permanece
colapsada e declarada.

## 7. O que NAO foi feito, e por que

| Nao feito | Razao, com fundamento |
|---|---|
| **Aplicar, ativar ou ratificar** | Vedado pelo despacho; e `LM-02` poria `FND` sem vigencia de qualquer modo |
| **Emendar `FND-04`** | `K7`; e `ADR-0019 §4` ja recusara *(Alternativa D, criterio `K6`)*, deixando `RD-18` aberto |
| **Sanar `PRJ` e `TPL`** | Largura e do Soberano — `Q1` de `RFC-0027 §9`. Declarados em `RD-96` e `RD-97` |
| **Sanar `C0 · T2`** | Despacho: *"nada alem disso"*. `Q2` de `RFC-0027 §9` |
| **Reclassificar `SPC-001`** | Vedado pelo despacho, e correto: nasceu `C2` validamente. A emenda **nao retroage** |
| **Tocar `DoR`, `DoD` ou regra de conteudo** | Vedado pelo despacho. **`SF-01` a `SF-09` e `SF-11` a `SF-32`: `0` bytes** |
| **Corrigir *"fase futura"* nas duas Cartas** | Ja era falso **antes** desta emenda. Corrigi-lo aqui seria carona silenciosa num ato alheio. **Declarado, nao corrigido** |
| **Emitir baseline nova** | Emitida — **5** artefatos criados. Ver §8 |

## 8. Estado do acervo ao fechar

| Medida | Valor |
|---|---|
| Artefatos | **228** — `+5` sobre `BL-2026-08-02-01`: `RFC-0027`, `ADR-0032`, `FIT-2026-025`, `PS-2026-017` e este registro. **`0` removidos** |
| Fundacionais alteradas | **`0`** — os quatro candidatos vivem **fora do acervo** |
| Cartas alteradas | **`0`** |
| Atos emitidos | **`0`** — a minuta esta **redigida e nao emitida** em `PS-2026-017 §6` |
| Fila de retidos por falta de ato | **3** — `ADR-0026`, `ADR-0028` e agora **`ADR-0032`** |
| O que espera o Fundador | **`ADR-0032`** e as **tres questoes** de `PS-2026-017 §7` |

## 9. Rastreabilidade

| Elo | Artefato |
|---|---|
| Achado | `RD-91` — [artifact-registry §7](artifact-registry.md), item 115 |
| Pergunta | [RFC-0027](../rfcs/RFC-0027-separacao-de-proponente-e-aprovador-na-spec-c1.md) |
| Decisao | [ADR-0032](../decisions/ADR-0032-separacao-de-proponente-e-aprovador-na-spec-c1.md) — `aprovado` · `ratificacao: pendente` |
| Aptidao | [FIT-2026-025](fitness/FIT-2026-025-emenda-de-sf-10.md) — `apto-com-ressalva` |
| Pacote ao Soberano | [PS-2026-017](pacote-soberano-2026-08-02-rd-91.md) |
| Candidatos | `_candidatos-LucaX-Enterprise-OS-2026-08-02-M1.13.5.1/` — 4 arquivos, fora do acervo |
| Evidencia | `_missao-1-13-5-1-2026-08-02/evidencia/` — `H-A` de rollback e tabela de hashes |

## 10. Licao da missao

**A celula que o achado nomeia pode nao ser a sede do defeito.** `RD-91` apontava `FND-11 §5`,
e `FND-11 §5` **nao decidia nada ali** — reproduzia duas fontes, palavra por palavra. Uma
emenda obediente ao texto do achado teria sido **formalmente perfeita e sem efeito algum**.

**O que revelou foi confrontar a projecao com as fontes que a propria `PJ-02` lista** — nao
ler o achado com mais atencao. E o mesmo movimento que produziu `RD-91`: **exercer, nao ler**.
Familia de `MEM-APR-0002`, `MEM-APR-0005` e `MEM-APR-0006`.

**Corolario, e ele custou dois achados novos:** varrer a **coluna**, nao a **celula**. `PRJ` e
`TPL` estavam com o mesmo colapso desde a fundacao, e **`0`** achados os registravam.

---

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-08-02 | DEP-GOV | Criacao. Registra a Missao 1.13.5.1 — os instrumentos `C3` que sanam **`RD-91`**, produzidos e **nao aplicados**. O **Item 0** mediu antes de emendar e encontrou que **a celula do achado nao era a sede**: `FND-11 §5` reproduz **literalmente** `FND-09 §8.2` linha `SPC` e `FND-04 §2.1` linha `C1`, e por `PJ-03` com `FND-01 §10` a emenda foi **redirecionada da projecao para a fonte**. A varredura das **21** linhas de `FND-09 §8.2` achou o **mesmo defeito** em **`PRJ`** e **`TPL`**, fora de `SPC` — reportado ao Fundador antes de redigir, e mantido **fora** da emenda por decisao dele. **5 artefatos criados** *(`RFC-0027`, `ADR-0032`, `FIT-2026-025`, `PS-2026-017`, este)*, **4 candidatos fora do acervo** com `H-A`/`H-N`/`H-P`, **5 achados novos** *(`RD-96` a `RD-100`)*, **`0` fechados**, **`0` atos emitidos**, **`0` bytes em fundacional, Carta, `TPL`, `CAP` ou historico**. Os **tres numeros de custo**, com a natureza de cada um declarada: **5** medido · **2** derivado · **7** medido em precedente. |
