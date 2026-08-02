---
id: FIT-2026-025-emenda-de-sf-10
titulo: Verificacao de aptidao da emenda que sana RD-91 — ADR-0032, RFC-0027 e os quatro candidatos
tipo: fitness
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-QAR
proprietario: DEP-QAR
aprovador: DEP-EXE
criado_em: 2026-08-02
atualizado_em: 2026-08-02
revisao_prevista: 2027-02-02
decisoes_relacionadas: [ADR-0032, ADR-0019, ADR-0021, ADR-0022, ADR-0031]
substitui: []
substituido_por: null
objeto_avaliado: [ADR-0032, RFC-0027, FND-09-1.6.0, FND-11-1.1.0, DEP-PRD-1.2.0, DEP-EXE-1.2.0]
classe_mudanca: C3
veredito: apto-com-ressalva
---

# FIT-2026-025: A emenda que sana `RD-91`

## Proposito

Verificar se a emenda que separa proponente de aprovador na `Spec` `C1` deixa a arquitetura
**mais apta a evoluir** do que estava. **Exigido, nao opcional:** a classe e `C3`, e
`CC-04`/`CV-07` poem o Fitness Check no encerramento de toda mudanca `C2` ou `C3` (`QG-6`).

## Escopo

| Item | Definicao |
|---|---|
| **Inclui** | `ADR-0032` · `RFC-0027` · os **quatro candidatos** *(FND-09 1.6.0, FND-11 1.1.0, Cartas DEP-PRD 1.2.0 e DEP-EXE 1.2.0)*, avaliados **fora do acervo** |
| **Nao** inclui | O **merito** da decisao do Soberano · a **largura** da emenda, que e escolha dele · `SPC-001` · qualquer `Spec` futura |
| Executor | **DEP-QAR** — **distinto do produtor** (`FND-04 §6`, linha *Verificacao de aptidao*; `ADR-0005`; `LV-03`) |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| **Produz** | **DEP-QAR** | FND-09 §8.2, linha `FIT` — *propoe/cria* |
| **Forma** | **DEP-GOV** | FND-09 §8.2, linha `FIT` — *revisa* |
| **Aprova** | **DEP-EXE** | FND-09 §8.2, linha `FIT` |
| **Ratifica** | **—** | `FT-10` de [ADR-0015](../../decisions/ADR-0015-fitness-check-e-parecer-nao-decisao.md): parecer nao se ratifica |

> **Este parecer nao decide e nao aprova.** Ele avalia aptidao. A ratificacao incide sobre **a
> mudanca avaliada**, nunca sobre o parecer (`FT-11`).

## Sumario

| Pergunta | Veredito |
|---|---|
| `F1` — complexidade aumentou sem ganho proporcional? | ✅ **Nao** |
| `F2` — algum conceito foi duplicado? | ✅ **Nao**, e uma duplicacao **preexistente foi reduzida** |
| `F3` — alguma abstracao ficou desnecessaria? | ✅ **Nao** |
| `F4` — continua mais simples de evoluir? | ✅ **Sim** |
| `F5` — reduz ou aumenta o custo de contexto? | ✅ **Reduz**, medido |
| `F6` — favorece reutilizacao? | ⚠️ **Sim, e parcialmente** — ver ressalva `S2` |

## F1 — A complexidade aumentou sem ganho proporcional?

**Nao.** O que a emenda acrescenta e **uma reserva de sete palavras** numa celula e **uma
nota** que a fundamenta.

| Medida | Antes | Depois | Delta |
|---|---|---|---|
| Celulas de `FND-09 §8.2` | 126 | 126 | **`0`** |
| Celulas da matriz de `SF-10` | 50 | 50 | **`0`** |
| Titulares nomeados nas duas tabelas | 6 | 6 | **`0`** |
| Entidades, tipos, portoes, papeis, classes | — | — | **`0` criados** |
| Linhas de `FND-09` | 1.263 | 1.278 | **+15** *(1 celula, 14 de nota e historico)* |
| Linhas de `FND-11` | 399 | 411 | **+12** |
| Linhas das duas Cartas | 951 | 953 | **+2** |

**O ganho e desproporcionalmente maior que o custo:** **3 artefatos por `Spec`** deixam de ser
exigidos. Custo da emenda: **27 linhas** de norma. **Nao ha assimetria a declarar contra.**

## F2 — Algum conceito foi duplicado?

**Nao — e o oposto aconteceu.** A verificacao preventiva de `PJ-05` foi aplicada **antes** da
escrita, e ela **barrou a emenda que o despacho literalmente pedia**:

| Verificacao | Resultado |
|---|---|
| A celula de `FND-11 §5` reproduz alguma fonte? | ✅ **Sim, duas, literalmente** — `FND-09 §8.2` linha `SPC` e `FND-04 §2.1` linha `C1` |
| Emendar so a projecao criaria segunda fonte de verdade? | ✅ **Sim** — e `PJ-03` a chamaria de **defeito da projecao** |
| A emenda foi redirecionada para a fonte? | ✅ **Sim** — `H1`/`H2` na fonte, `H3`/`H4` em cascata declarada |
| A `PJ-02` de `FND-11 §5` passou a listar a fonte nova? | ✅ **Sim** — `FND-04 §3.1` acrescentado (`H4`) |
| Alguma reproducao foi **barrada antes** de ser escrita? | ✅ **Uma, nomeada:** a emenda confinada a `FND-11 §5`. **Este e o achado central da missao** |

**`PJ-06` cumprido nas duas metades:** houve duplicacao? **Nao.** O teste preventivo foi
aplicado, com evidencia? **Sim** — o confronto literal esta em `ADR-0032 §2` e `PS-2026-017 §2`.

## F3 — Alguma abstracao ficou desnecessaria?

**Nao.** A remissao a classe — *"conforme classe (`FND-04 §2`)"*, que `ADR-0019` instituiu —
**permanece**, e continua sendo a forma correta. A reserva **nao a substitui**: a especializa
no unico ponto em que ela produzia resultado que `LV-03` proibe. **Nenhuma indirecao nova, e
nenhuma removida.**

## F4 — O sistema continua mais simples de evoluir do que antes?

**Sim, e a prova e o proprio piso.** Antes, `FND-04 §6` fixava `C1` como piso da `Spec` e o
piso **nao podia ser usado** — toda `Spec` tinha de subir para `C2` para nao nascer nula.
Depois, o degrau barato **existe de fato**.

**Conferencia das quatro incompatibilidades absolutas de `FND-04 §3.1`, em `C1 · T2` apos a
emenda:** `DEP-PRD` *(proponente)* ≠ `DEP-EXE` *(aprovador)* ✅ · `DEP-PRD` ≠ revisor ✅ ·
`DEP-GOV` *(guardiao)* ≠ `DEP-PRD` ✅ · executor ≠ verificador ✅. **4 de 4.**

## F5 — A mudanca reduz ou aumenta o custo de contexto?

**Reduz, e o numero e medido, nunca estimado.**

| Cenario | Artefatos | Linhas |
|---|---|---|
| `Spec` em `C2` *(o que `SPC-001` custou)* | **5** | **1.580**, por `wc -l` |
| `Spec` em `C1` apos a emenda *(instrumentos do rito)* | **2** | — **nao medido**: nenhuma `Spec` `C1` existe |
| Custo da emenda, uma vez | **27 linhas** de norma + **7** artefatos de rito | — |

> **`CE-04` respeitado.** As **1.580** linhas sao medicao. As **2** sao **derivacao da norma**
> — `FND-07 §2.3` da `C1 · Tipo 2` = Nota de Decisao, e `SF-24` item (9) so exige `FIT` em
> `C2`/`C3`. **O valor em linhas da segunda `Spec` fica `definido, sem valor`** (`LM-01`,
> `CE-04`) ate a segunda `Spec` real existir.

## F6 — Ela favorece reutilizacao?

**Sim, e parcialmente.** O raciocinio — *"quando a matriz poe o proprietario como proponente,
`FND-04 §3.1` desloca o default de `§2`"* — e **generalizavel** e esta escrito na nota de
`H2`, disponivel para qualquer tipo. **Mas ele foi aplicado a `1` linha de `3` que precisam
dele.** Ver ressalva `S2`.

## Ressalvas

| # | Ressalva | Severidade | Dono | Gatilho |
|---|---|---|---|---|
| **`S1`** | **`C0 · T2` continua colapsada.** A emenda alcanca `C1` e nao `C0`, por determinacao de escopo. O piso de criacao e `C1`, logo `C0` so ocorre em `Spec` ja existente — **o alcance real e menor que o do defeito**, e nao e zero | **Baixa** | SOBERANO | Primeira mudanca `C0` sobre `Spec` viva |
| **`S2`** | **Duas linhas da mesma tabela ficam com o defeito identico:** `PRJ` *(DEP-EXE propoe e aprova)* e `TPL` *(DEP-GOV propoe, revisa e aprova)*. **Emendar `SPC` e nao emendar as vizinhas cria assimetria dentro de uma tabela so** — quem ler `PRJ` depois desta emenda encontrara a mesma nulidade **com a solucao ja escrita duas linhas acima** | **Media** | SOBERANO *(largura)* / DEP-GOV *(instrumento)* | `RD-96` e `RD-97`; *"proximo `PRJ` criado ou proximo `TPL` emendado"* |
| **`S3`** | **O ganho de `2` contra `5` e derivado, nao observado.** Nenhuma `Spec` `C1` existiu — o piso nasceu nulo. `PI-10` | **Baixa** | DEP-PRD | Segunda `Spec` real |
| **`S4`** | **`FND-11 §14`, limites `L1` e `L2`, ficaram falsos desde `SPC-001`** *(*"nenhuma `Spec` real existe"*, *"o valor sera medido na primeira `Spec`"*)*, e **esta emenda nao os corrige** — nao sao a celula autorizada. `RD-100` | **Baixa** | DEP-GOV | Proxima emenda de `FND-11` |

## Veredito

> ## `apto-com-ressalva`
>
> **A emenda deixa a arquitetura mais apta.** Ela remove uma nulidade estrutural pelo menor
> texto que a remove, **na sede certa** — e a sede certa **nao era a que o achado nomeava**,
> o que so apareceu porque a projecao foi confrontada com a fonte **antes** de escrever.
> **`4` ressalvas**, nenhuma bloqueante, e a que mais importa e **`S2`**: corrige-se uma linha
> de uma tabela que tem tres com o mesmo defeito. **Isso e escolha de largura, e ela e do
> Soberano** — mas o parecer registra que a assimetria e visivel a olho nu na tabela emendada.

**O que este parecer NAO diz:** nao diz que a emenda esta em vigor *(depende de ato)*, nao diz
que `PRJ` e `TPL` podem esperar *(diz que a decisao de esperar e do Soberano)*, e nao aprova
nada — `FT-10`, `FT-11`.

## Aprendizado gerado

**`V1` — a celula que o achado nomeia pode nao ser a sede do defeito.** `RD-91` foi registrado
contra `FND-11 §5`, e `FND-11 §5` **nao tinha merito proprio ali**. Quem emendasse o texto
apontado teria produzido uma emenda **inocua e formalmente perfeita**. **O que revelou foi o
confronto literal com as fontes que a propria `PJ-02` lista** — nao a leitura do achado.
Familia de `MEM-APR-0002` *(reproducao)* e de `MEM-APR-0005`/`0006` *(exercer, nao ler)*.

**`V2` — varrer a tabela inteira, e nao so a linha citada.** As linhas `PRJ` e `TPL` estavam
la desde a fundacao, com o mesmo colapso, e **`0` achados as registravam**. Apareceram porque
se leu a **coluna**, e nao a **celula**.

## Historico de vereditos sobre este objeto

| Data | Objeto | Veredito | Registro |
|---|---|---|---|
| 2026-08-02 | `ADR-0032`, `RFC-0027` e os 4 candidatos | **`apto-com-ressalva`** — 4 ressalvas | Este `FIT` |
| 2026-08-02 | `SPC-001`, `ADR-0031`, `RFC-0026` | `apto-com-ressalva` — 4 ressalvas | [FIT-2026-024](FIT-2026-024-primeira-spec.md) |
