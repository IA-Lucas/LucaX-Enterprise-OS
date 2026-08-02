---
id: PS-2026-012
titulo: Pacote de decisao soberana — emenda C2 Tipo 2 que fecha RD-37 nas Cartas de DEP-OPS, DEP-GRW e DEP-TLS
tipo: relatorio
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: DEP-EXE
proprietario: DEP-EXE
aprovador: DEP-GOV
criado_em: 2026-07-30
atualizado_em: 2026-07-30
revisao_prevista: null
decisoes_relacionadas: [ADR-0011, ADR-0012, ADR-0018, ADR-0023, ADR-0025]
substitui: []
substituido_por: null
canal: REPORTE
emissor: DEP-EXE
destinatario: SOBERANO
ttl: ate decisao do Soberano
resumo: Submete as tres Cartas que fecham RD-37, com diff literal de uma afirmacao falsa por Carta, e mede a familia das nove antes e depois.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# PS-2026-012 — `RD-37`: as tres Cartas restantes

> ## Este pacote **informa**. Nao decide, nao aprova, nao promulga e nao edita nada.
>
> **`DEP-OPS`, `DEP-GRW` e `DEP-TLS` permanecem em 1.0.0**, com a afirmacao falsa **vigente**.
> Os candidatos existem como **arquivo real fora do acervo**, caminho em §4.4 — **`RD-19`**.
>
> **Caminho exato:** `governance/pacote-soberano-2026-07-30-rd-37.md` *(`RE-01`)*.
>
> **Este pacote e a execucao de `Q1` de [PS-2026-010 §10](pacote-soberano-2026-07-29-rd-31.md)**,
> que previu literalmente *"pacote proprio"* para estas tres Cartas.

## Proposito

Fechar **`RD-37`**: levar a **zero** as afirmacoes falsas sobre o titular de `QG-1` na familia
das nove Cartas.

## Escopo

| Item | Definicao |
|---|---|
| Inclui | **Dois** objetos: `ADR-0025` e as promulgacoes de **`DEP-OPS` 1.1.0**, **`DEP-GRW` 1.1.0** e **`DEP-TLS` 1.1.0** |
| **Nao** inclui | `RD-27` — [PS-2026-011](pacote-soberano-2026-07-30-rd-27.md) · o **merito** de `ADR-0018` · **qualquer outra responsabilidade das tres Cartas** — `0` bytes fora de `§5.2` e do frontmatter · `DEP-PRD` e `DEP-EXE` — [PS-2026-010](pacote-soberano-2026-07-29-rd-31.md) · `DEP-ENG`, `DEP-GOV`, `DEP-KMS`, `DEP-QAR` — **medidas, nada a corrigir** *(§5.2)* · `FND-01`, `FND-04`, `FND-09`, `FND-10`, `TPL-spec` — **`0` bytes** · `RD-33`, `RD-36` |
| Natureza | **Reporte**, entidade `MSG` |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| **Autor da emenda** | **DEP-EXE** | `FND-09 §8.2`, linha `DEP` — **proponente unico** |
| **Revisa** | **DEP-GOV** | `FND-09 §8.2`, linha `DEP` |
| **Revisor independente** | **DEP-QAR** | `RM-06b` — §6 |
| **DECIDE as Cartas** | **SOBERANO** | `FND-09 §8.2`, linha `DEP`. **Indelegavel.** **Nao ocorreu** |

> **Residuo declarado (`PI-10`).** **`DEP-OPS`, `DEP-GRW` e `DEP-TLS` sao as areas alcancadas** e
> **nao sao autoras nem revisoras**, porque `FND-09 §8.2` atribui a proposicao de Carta a
> `DEP-EXE` — a quem as tres **respondem**. Residuo **de matriz, nao de interesse** — `IC-3`.

---

## 1. O que se pede

| # | Objeto | Ato pedido | Se **nao** houver ato |
|---|---|---|---|
| **1** | **`ADR-0025`** | **Aprovacao** *(`C2 · Tipo 2` — ratificacao **nao exigida**)* | A cascata de `ADR-0018` permanece **incompleta** |
| **2** | **`DEP-OPS` 1.1.0** | **Aprovacao e ratificacao** | `§5.2` segue afirmando que `DEP-PRD` libera `QG-1` |
| **3** | **`DEP-GRW` 1.1.0** | idem | idem |
| **4** | **`DEP-TLS` 1.1.0** | idem | idem |

> **Os tres sao integralmente independentes entre si.** Recusar `DEP-GRW` **nao afeta** `DEP-OPS`
> nem `DEP-TLS`: cada Carta corrige **a sua propria** afirmacao, e **nenhuma cita a outra**.

## 2. Diff literal — **identico nas tres**

```
antes:
**Nenhum.** Os sete portoes de FND-01 §6.2 sao liberados por DEP-EXE *(QG-0)*, DEP-PRD
*(QG-1)*, DEP-ENG + DEP-GOV *(QG-2)*, DEP-QAR *(QG-3, QG-4)*, DEP-KMS *(QG-5)* e
DEP-QAR + DEP-GOV *(QG-6)*.

depois:
**Nenhum.** Os sete portoes de FND-01 §6.2 sao liberados por **DEP-EXE** *(QG-0 e QG-1)*,
DEP-ENG + DEP-GOV *(QG-2)*, DEP-QAR *(QG-3, QG-4)*, DEP-KMS *(QG-5)* e
DEP-QAR + DEP-GOV *(QG-6)*.
```

| # | Local | Antes | Depois |
|---|---|---|---|
| **D1** | frontmatter, `versao` | `1.0.0` | **`1.1.0`** |
| **D2** | frontmatter, `atualizado_em` | `2026-07-28` | **`2026-07-30`** |
| **D3** | frontmatter, `decisoes_relacionadas` | *(sem `ADR-0018`)* | **`+ ADR-0018, ADR-0025`** |
| **D4** | frontmatter, `status` | `ativo` | **`em-revisao`** |
| **D5** | frontmatter, `ratificacao` | `ratificada` | **`pendente`** |
| **D6** | **§5.2**, duas linhas fisicas da enumeracao | acima | acima |
| **D7** | Historico | *(inexistente)* | linha `1.1.0` |

**Medicao por Carta, identica nas tres: `6` blocos de diff · `7` linhas substituidas ·
`1` acrescentada · `0` removidas · delta `+1`.**

> **Os itens sao sete e os blocos sao seis, e a diferenca e de adjacencia, nao de conteudo:**
> `D1` *(`versao`)* e `D4` *(`status`)* ocupam **linhas consecutivas** do frontmatter e o `diff`
> as funde num unico bloco. **Contar itens e contar blocos sao medidas distintas, e as duas
> estao publicadas** — a mesma disciplina que `PS-2026-008` aplicou quando o pacote declarava
> *"57/18"* e o `diff` media *"55/16"* para o mesmo arquivo final.

> **Divergencia de convencao, declarada.** `RD-37` e `PS-2026-010 §Q1` publicaram o custo como
> **"1 linha por Carta"**; o `diff` mede **2 linhas substituidas na norma** *(a frase ocupa duas
> linhas fisicas e a correcao reflui a quebra)* **e delta `0` na secao**. O **+1** do arquivo e a
> **linha de historico**, que `FND-03 §6` obriga. **As tres medidas sao verdadeiras e contam
> coisas diferentes:** uma afirmacao, duas linhas de norma, uma linha de arquivo. **A alternativa
> literalmente de 1 linha existe** — trocar so a sigla, produzindo `DEP-EXE *(QG-0)*, DEP-EXE
> *(QG-1)*` — **e foi recusada por legibilidade**, nao por impossibilidade: [ADR-0025 §3](../decisions/ADR-0025-extensao-da-propagacao-de-qg-1-as-cartas-restantes.md),
> alternativa `B`.

### 2.1 O que o diff **nao** contem

| Nao contem | Verificacao |
|---|---|
| Alteracao em `§1`–`§5.1` e `§5.3`–`§13` | **`0` bytes** nas tres, medido por `diff` |
| Portao criado, removido ou transferido | **`0`** — **7 antes, 7 depois**, e a contagem *"sete"* permanece exata |
| Responsabilidade, interface, risco, metrica, Capability, autonomia ou classe alterada | **`0`** |
| Campo de `AC-08` acrescentado | **`0`** — as tres **ja declaram os cinco** |
| Alteracao em `DEP-PRD`, `DEP-EXE` ou nas outras quatro Cartas | **`0` bytes** |

## 3. `DEP-OPS`, `DEP-GRW` e `DEP-TLS` continuam **nao liberando portao algum**

**A correcao nao lhes da nada.** As tres declaram **"Nenhum"** antes e depois; o que muda e **de
quem se diz** que libera `QG-1` na enumeracao que elas fazem dos portoes **dos outros**.

## 4. Identificadores de integridade

### 4.1 Cartas em vigor e candidatos

| Carta | Versao | Linhas | `H-A` | `H-N` | `H-P` projetado *(apos `O4`)* |
|---|---|---|---|---|---|
| **`DEP-OPS` em vigor** | 1.0.0 | **437** | `09d97a4c991d7dd1eb2fb8b261276ada267197fb9b8abe1669f7100627b63757` | `6bf590c7ad8bd2f0fc643dcf94f42d8abf6788c1dcef1ac9e56bd0f5c28a0a48` | — |
| **`DEP-OPS` candidato** | **1.1.0** | **438** | **`9a5b52c40e0b724a1174641eec63e96becd232c3cacf052d3f738a29f23bfbee`** | `b38da97b64be98bd1c84aad4639bf45834d77763eb85802d52b20c9257d26baa` | **`78a434888e20ebd30ce85707f64578f94a402c9013ad8740d1dbae464c786e5a`** |
| **`DEP-GRW` em vigor** | 1.0.0 | **443** | `0533fdf26235636e9957bf7da113384f6d4f7464548158335376186a50382ca1` | `2e0e7d95b82e1fff963efd473b1389a55e33bfeee547d26ed18b2bb4c20062ea` | — |
| **`DEP-GRW` candidato** | **1.1.0** | **444** | **`90d596381340bb14ee0a2a38f85e6d97aea95aa6f1ec6d83056c61f1a2f6e9cf`** | `304fa9a3119539b210df34fdeb187dac6894732b01a34bfabaa7707c746ac88d` | **`22ec7b45bf46970c14d3254732530ec41ff80c0f6ccfc1c5f9c8ed4fb2be92e9`** |
| **`DEP-TLS` em vigor** | 1.0.0 | **424** | `d5eede3893868fe8554691a12d8f854ca8b239ae1a399dfed6d6f940235ad9fc` | `716f363a96a51d521ca9a2c589f22fa73f12d81eb90d772daf1801bed93e9858` | — |
| **`DEP-TLS` candidato** | **1.1.0** | **425** | **`9e27ca81ad53dc8059806084eee07a7e2a15c467ab520b2ca6bf1681fbf93b35`** | `65b83520de23c94ad045fb76f71814b7f1db12b0ff29791180aa17759b688d7e` | **`857d6703faca27cae0b4d23d743ebe9bc7b1bb1776191f5467f1a4193e165e31`** |

**`H-N` invariante sob `O4` — verificado em 3 de 3** (`IR-02`, `IR-06`).
**`O4` = `status: em-revisao → ativo` e `ratificacao: pendente → ratificada`**, o mesmo par
determinado por reproducao de hash no sexto ato.

### 4.2 `ADR-0025`

| Objeto | Caminho · versao · linhas | `H-A` | `H-N` | `H-P` projetado |
|---|---|---|---|---|
| **`ADR-0025`** | `decisions/ADR-0025-extensao-da-propagacao-de-qg-1-as-cartas-restantes.md` · **1.0.0** · **292** | **`a6f4ee80a59f02c8238f6d463ccfcbc2103d29f9af8a1848a91c1b2fcccf9124`** | `0c58c58b4758203123f5a75172b6af60abf09a579de17d080e31dbe60e2afaea` | **`a1e7f8c04024ed50998f11c49455fc7efe8cdf6af4221ab21968c2b489c68b59`** |

> **`O4` de `ADR-0025` alcanca APENAS `status`.** Ele e **`C2 · Tipo 2`** e declara
> `ratificacao: nao-exigida`, que **nao vira `ratificada`** — mesmo regime de `ADR-0023`. O
> `H-P` acima reflete **so** `em-revisao → ativo`.

**`RFC`: dispensada** por `FND-04 §2`, com as duas condicoes verificadas e a concordancia escrita
de `DEP-GOV` em [ADR-0025 §4](../decisions/ADR-0025-extensao-da-propagacao-de-qg-1-as-cartas-restantes.md).
**Peca instrutoria: [RFC-0019 §3](../rfcs/RFC-0019-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md)**,
que **mediu e nomeou** estas tres Cartas.

### 4.3 Metodo — **o mesmo instrumento de `PS-2026-011 §4.3`**

`IR-02`/`IR-03` reimplementados e validados contra **19 controles publicados** — incluindo
`DEP-PRD` e `DEP-EXE` de `PS-2026-010 §4.1`, **do mesmo tipo documental destas Cartas** —
**antes** de medir qualquer candidato. **19 de 19 reproduzem.**

### 4.4 Onde os candidatos vivem — `RD-19`

```
E:\LucasIA\Projetos\_backups\LucaX-Enterprise-OS_2026-07-30_pre-missao-1-13-2\_candidatos\
  ops-1.1.0.md   438 linhas  LF   9a5b52c4…bfee
  grw-1.1.0.md   444 linhas  LF   90d59638…e9cf
  tls-1.1.0.md   425 linhas  LF   9e27ca81…3b35
```

**`LF` em 3 de 3 · `0` bytes `CR`.** **Montados por transformacao programatica** do arquivo em
vigor — e e por isso que *"`0` bytes fora de `§5.2` e do frontmatter"* pode ser afirmado byte a
byte.

### 4.5 `IR-09` — teste de reconstrucao

| Objeto | Operacao | Resultado |
|---|---|---|
| `DEP-OPS`, `DEP-GRW`, `DEP-TLS` 1.1.0 | Reverter **apenas** `status` e `ratificacao` no arquivo pos-`O4` e medir | **Reproduz `H-A` — 3 de 3** |
| `ADR-0025` | Reverter **apenas** `status` | **Reproduz `H-A`** |

## 5. Prova de autoridade de `QG-1` — **a familia inteira das nove Cartas, depois dos candidatos**

| Carta | Fonte medida | Ocorr. `QG-1` | **Afirmacoes falsas** | Nomeia `DEP-EXE` titular | Papel coerente |
|---|---|---|---|---|---|
| `DEP-ENG` | acervo vigente | 2 | **0** | — | **Sim** *(gatilho, nao titularidade)* |
| `DEP-EXE` | candidato 1.1.0 | 22 | **0** | **Sim** | **Sim** |
| `DEP-GOV` | acervo vigente | 0 | **0** | — | **n/a** |
| **`DEP-GRW`** | **candidato 1.1.0** | 4 | **0** | **Sim** | **Sim** |
| `DEP-KMS` | acervo vigente | 0 | **0** | — | **n/a** |
| **`DEP-OPS`** | **candidato 1.1.0** | 4 | **0** | **Sim** | **Sim** |
| `DEP-PRD` | candidato 1.1.0 | 27 | **0** | **Sim** | **Sim** *(submetido, nunca liberador)* |
| `DEP-QAR` | acervo vigente | 0 | **0** | — | **n/a** |
| **`DEP-TLS`** | **candidato 1.1.0** | 4 | **0** | **Sim** | **Sim** |
| **TOTAL** | — | **63** | **`0`** | **5 de 9** | **9 de 9** |

**Antes de `ADR-0023` e `ADR-0025`: `11` afirmacoes falsas em `4` Cartas, e `0 de 9` nomeavam o
titular. Depois: `0` em `0`, e `5 de 9`.**

### 5.1 Titularidade coerente **por todos os caminhos**

| Caminho | O que diz | Coerente? |
|---|---|---|
| **`FND-01 §6.2`** *(FONTE, nivel 1)* | `\| QG-1 \| Apos especificar \| … \| **DEP-EXE** \|` | ✅ |
| `FND-09 §8.2`, linha `SPC` | *Aprova:* `conforme classe (FND-04 §2)` — **`QG-1` nao consta desta tabela**, e o registro de conflito diz por que | ✅ **por remissao** |
| `FND-10 §10.3`, linha `Spec` | *Aprova:* `conforme classe` — projecao declarada de `FND-09 §8.2` | ✅ |
| `departments/README`, *Portoes que libera* | `DEP-EXE: QG-0 · **QG-1**` | ✅ |
| **As 9 Cartas**, apos os candidatos | **0 afirmacoes falsas · 5 nomeiam DEP-EXE · 4 nao mencionam** | ✅ |

**Nenhum caminho contradiz outro.** A pergunta *"quem libera `QG-1`?"* passa a ter **uma unica
resposta em todo o acervo**.

### 5.2 As outras seis Cartas — medidas, **nada a corrigir**

`DEP-GOV`, `DEP-KMS` e `DEP-QAR` **nao mencionam `QG-1`**. `DEP-ENG` o menciona **duas vezes**, e
**nenhuma atribui titularidade**: `§6.1` o usa como **gatilho** *(recebe a Spec quando o portao
libera)* e `§6.2` como **condicao de devolucao** *(`QG-1` nao liberado)*. **A distincao entre
mencionar um portao e afirmar quem o libera e o que separa `DEP-ENG` das outras tres** — e foi
por medi-la que `RD-37` nao foi superestimado.

## 6. Revisao independente — **DEP-QAR**

| Objeto | O que foi conferido | Veredito |
|---|---|---|
| **`ADR-0025`** | `VD-01` a `VD-09`; **as duas condicoes de dispensa de RFC, uma a uma**; `revisor ≠ autor`; aprovador ≠ autor | **CONFORME**, com `QS-1` |
| **As tres Cartas** | `D1`–`D7`; `0` bytes fora de `§5.2` e do frontmatter; `H-A`, `H-N`, `H-P`, `IR-09`; os cinco campos de `AC-08` **ja presentes** | **CONFORME — 3 de 3** |

| # | Ressalva de `DEP-QAR` | Severidade |
|---|---|---|
| **`QS-1`** | **A dispensa de RFC e legitima e e a primeira do acervo.** As duas condicoes de `FND-04 §2` estao verificadas e a concordancia esta escrita, entre partes distintas. **A ressalva registra o precedente**, nao o contesta: **o proximo caso tera de verificar as duas condicoes de novo**, e nao invocar este | **Baixa** |
| **`QS-2`** | **`RD-47`** — a assimetria de regime de estado entre Carta e fundacional **nasce declarada e nao resolvida**. **Nao impede este ato**; impede afirmar que o `H-P` se deriva de regra escrita | **Baixa** |

## 7. Independencia dos objetos

| Objeto | Independente? | Verificavel? | Bloqueavel isoladamente? |
|---|---|---|---|
| `ADR-0025` | **Sim** | **Sim** | **Sim** — recusa-lo recusa as tres Cartas |
| `DEP-OPS` 1.1.0 | **Sim** | **Sim** | **Sim** |
| `DEP-GRW` 1.1.0 | **Sim** | **Sim** | **Sim** |
| `DEP-TLS` 1.1.0 | **Sim** | **Sim** | **Sim** |

**Prova textual:** nenhuma das tres Cartas cita as outras duas, `FND-11`, `ADR-0022` ou qualquer
objeto de `PS-2026-009` e `PS-2026-011` — verificavel por `grep`. **Sobreposicao de diff: `0`** —
**nenhum arquivo e alcancado por mais de um objeto deste ato**.

## 8. Impacto

| Verificacao | Resultado |
|---|---|
| **Afirmacoes falsas sobre `QG-1` nas 9 Cartas** | **3 em 3 → `0` em `0`** *(e `11` em `4` → `0`, somando `ADR-0023`)* |
| **Cartas que nomeiam o titular** | **2 de 9 → 5 de 9** |
| **Titulares criados ou transferidos** | **ZERO** |
| **Portoes** | **7 antes · 7 depois** |
| **Outras responsabilidades alteradas** | **ZERO** |
| **Fontes de `foundation/` emendadas** | **ZERO** |
| **Custo de contexto** | **+1 linha por Carta** = **+3** |
| Reversibilidade | **Tipo 2** — `H-A` das versoes substituidas publicado em §4.1 |

## 9. Risco residual

| # | Risco | Sev. | Mitigacao |
|---|---|---|---|
| **RT-1** | A dispensa de RFC virar habito | Media | `QS-1`; `ADR-0025 §1` e `§4` **verificam as duas condicoes** e declaram que a dispensa e **do caso** |
| **RT-2** | **Ato nao vir** | Media | As tres seguem em 1.0.0 com a afirmacao falsa **declarada**. **Nao bloqueia** — `0` Specs, `KP-6` registra **0 liberacoes de `QG-1`** |
| **RT-3** | `RD-47` ser lido como resolvido | Baixa | `QS-2` e `ADR-0025 §5.2` declaram que **nao e** |

## 10. As escolhas que o ato pode fazer diferente

| # | Escolha | Como se expressa | Altera hash? |
|---|---|---|---|
| **Q1** | Aprovar **`ADR-0025`** e **bloquear uma ou mais Cartas** | Omitir o objeto da enumeracao | **Nao** |
| **Q2** | Exigir **RFC** apesar de `FND-04 §2` | Devolver o ADR; a peca instrutoria e `RFC-0019 §3` | **Nao** — mas adia o fechamento |
| **Q3** | Estender a correcao a `DEP-ENG` | **Nao ha objeto**: `§5.2` mede **0 afirmacoes falsas** ali. Exigiria achado novo | **n/a** |

## 11. Recomendacao

| Campo | Conteudo |
|---|---|
| **Recomendacao** | **APROVAR** os quatro objetos |
| **Fundamento** | O defeito e **de projecao contra fonte ratificada**, e `PJ-03` **ja decidiu quem cede**. **Nenhuma autoridade e decidida**: `ADR-0018` decidiu em 2026-07-29, e isto **transcreve**. E o momento e **o mais barato que havera** — `0` Specs, `0` Produtos, **`0` liberacoes de `QG-1` registradas**: corrigir agora **nao invalida nenhuma decisao passada, porque nao houve nenhuma sob a regra errada** |
| **Contrapartida honesta** | **Duas.** *(i)* **Primeira dispensa de RFC do acervo** — legitima, verificada e **registrada como precedente que nao se invoca, se reverifica**. *(ii)* **`RD-47` nasce aberto**: o regime de estado que define o `H-P` de uma Carta nova **e costume, nao regra escrita** |
| **O pacote informa; nao decide** | **Nao decidir e resultado valido**, e **nao bloqueia trabalho algum** |

## 12. Rastreabilidade

| Campo | Conteudo |
|---|---|
| **RFC** | **Dispensada** — `FND-04 §2`; instrutoria em [RFC-0019 §3](../rfcs/RFC-0019-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md) |
| ADR | [ADR-0025](../decisions/ADR-0025-extensao-da-propagacao-de-qg-1-as-cartas-restantes.md) |
| Decisao de origem | [ADR-0018](../decisions/ADR-0018-liberacao-do-portao-qg-1.md) — **ratificado** |
| Pacote irmao, mesma cascata | [PS-2026-010](pacote-soberano-2026-07-29-rd-31.md) — executa seu `Q1` |
| Pacote irmao, **independente** | [PS-2026-011](pacote-soberano-2026-07-30-rd-27.md) |
| Minuta unica do ato | [PS-2026-013](pacote-soberano-2026-07-30-consolidado.md) |
| **Achado que fecha** | **`RD-37`** — integralmente |
| Achado que abre | **`RD-47`** |
| Ressalva que fecha | **`R2`** de [FIT-2026-016](fitness/FIT-2026-016-canonizacao-e-propagacao.md) |
| Verificacao de aptidao | [FIT-2026-017](fitness/FIT-2026-017-convergencia-pre-ratificacao.md) |
| Baseline vigente na submissao | **`BL-2026-07-29-10`** |

---

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-30 | DEP-EXE | Pacote da **Missao 1.13.2**: emenda **C2 · Tipo 2** das Cartas de **`DEP-OPS`** *(437 → 438)*, **`DEP-GRW`** *(443 → 444)* e **`DEP-TLS`** *(424 → 425)*, fechando **`RD-37`** e **executando literalmente o `Q1` de `PS-2026-010 §10`**, que previra *"pacote proprio"* para estas tres. **Nono pacote soberano.** **Menor rito competente, com a menoridade verificada:** a **RFC e dispensada** pela clausula expressa de `FND-04 §2`, com as **duas condicoes conferidas** — alternativa unica por `PJ-03`, alcance ja instruido por `RFC-0019 §3` — e **concordancia escrita de `DEP-GOV` entre partes distintas**; e a **primeira dispensa de RFC do acervo**, registrada por `DEP-QAR` como **precedente que nao se invoca, se reverifica**. **§5 traz a prova de autoridade de `QG-1` sobre a familia inteira das nove Cartas, depois dos candidatos: `0` afirmacoes falsas, contra `11` em `4` antes de `ADR-0023`**, e **`5 de 9`** Cartas nomeando o titular, contra `0 de 9`. **§5.1 prova a coerencia por todos os caminhos** — fonte `FND-01 §6.2`, `FND-09 §8.2`, `FND-10 §10.3`, `departments/README` e as nove Cartas —, e **§5.2 distingue, em `DEP-ENG`, mencionar o portao de afirmar quem o libera**, que e a razao de `RD-37` nao ter sido superestimado. **§2 declara a divergencia de convencao em vez de esconde-la:** o custo publicado era *"1 linha por Carta"* e o `diff` mede **2 linhas substituidas na norma, delta `0` na secao e `+1` no arquivo** — as tres medidas verdadeiras, contando coisas diferentes —, e a alternativa **literalmente de 1 linha foi recusada por legibilidade**, nao por impossibilidade. **`0` titulares criados ou transferidos · 7 portoes antes e depois · `0` bytes fora de `§5.2` e do frontmatter · `0` outras responsabilidades alteradas · `0` fontes de `foundation/` emendadas · `0` sobreposicao de diff com qualquer outro objeto do ato · `H-N` invariante sob `O4` em 3 de 3 · `IR-09` reproduz `H-A` em 4 de 4.** |
