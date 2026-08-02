---
id: ADR-0025-extensao-da-propagacao-de-qg-1-as-cartas-restantes
titulo: Emenda C2 Tipo 2 que estende a propagacao de ADR-0018 as Cartas de DEP-OPS, DEP-GRW e DEP-TLS, corrigindo tres afirmacoes falsas sem alterar responsabilidade alguma
tipo: adr
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-EXE
proprietario: DEP-EXE
aprovador: DEP-GOV
criado_em: 2026-07-30
atualizado_em: 2026-07-30
revisao_prevista: 2027-01-30
decisoes_relacionadas: [ADR-0011, ADR-0012, ADR-0018, ADR-0023]
substitui: []
substituido_por: null
classe_mudanca: C2
tipo_decisao: 2
supera: []
superado_por: null
resumo: Corrige a unica afirmacao falsa sobre QG-1 que sobra em cada uma das tres Cartas nao alcancadas por ADR-0023, levando a familia das nove de onze afirmacoes falsas a zero.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# ADR-0025: Extensao da propagacao de `QG-1` as Cartas restantes

> ## Nada de autoridade e decidido aqui — e desta vez nem a forma e nova
>
> **`QG-1` e de `DEP-EXE`** por [ADR-0018](ADR-0018-liberacao-do-portao-qg-1.md), **ratificado**
> e **em vigor desde 2026-07-29** em `FND-01 §6.2`. **Este ADR e cascata** (`CV-04`, `CC-03`) —
> e a **continuacao literal** de [ADR-0023](ADR-0023-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md),
> que corrigiu **2 das 4** Cartas defeituosas **por escopo determinado**, deixando as outras tres
> declaradas em `RD-37`.
>
> **As Cartas nao entram em vigor por este ADR.** [FND-09 §8.2](../foundation/09-meta-model.md),
> linha `DEP`: **aprovacao e ratificacao sao do SOBERANO**. Enquanto nao houver ato, `DEP-OPS`,
> `DEP-GRW` e `DEP-TLS` permanecem em **1.0.0**, com as **tres** afirmacoes falsas **vigentes**.

## Proposito

Fechar **`RD-37`**: fazer as tres Cartas que ainda afirmam que **`DEP-PRD` libera `QG-1`**
declararem o titular que a fonte ratificada ja fixou.

## Escopo

| Item | Definicao |
|---|---|
| Inclui | **Uma** afirmacao falsa por Carta, em `§5.2` de **`DEP-OPS`**, **`DEP-GRW`** e **`DEP-TLS`** |
| **Nao** inclui | O **merito** de `ADR-0018`, **nao reaberto** · **qualquer outra responsabilidade destas tres Cartas** — `0` bytes em `§1`–`§5.1` e `§5.3`–`§13` · **titular, portao, papel, classe ou direito decisorio novo** · `DEP-PRD` e `DEP-EXE` — [ADR-0023](ADR-0023-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md), **pacote separado** · `DEP-ENG`, `DEP-GOV`, `DEP-KMS`, `DEP-QAR` — **medidas: nada a corrigir** (§5.3) · `ADR-0019` e a aprovacao de `Spec` — **nao alcanca estas tres Cartas**, que **nao a mencionam** · `FND-01`, `FND-04`, `FND-09`, `FND-10`, `TPL-spec` — **`0` bytes** · `RD-27`, `RD-33`, `RD-36` |
| Origem | Achado **`RD-37`**; `Q1` de [PS-2026-010 §10](../governance/pacote-soberano-2026-07-29-rd-31.md), que **previu este pacote proprio** |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| **Propoe / autor** | **DEP-EXE** | `FND-09 §8.2`, linha `DEP` — **proponente unico** de Carta de Departamento |
| **Revisa** | **DEP-GOV** | `FND-09 §8.2`, linha `DEP` |
| **Aprova o ADR** | **DEP-GOV** | `C2` e de `DEP-EXE` com parecer de `DEP-GOV` (`FND-04 §2`), **mas `DEP-EXE` e o autor** — aprovar o proprio ADR seria autoverificacao (`PI-05`, `LV-03`, `AC-03`). **Precedente literal: `ADR-0023`** |
| **Revisor independente** | **DEP-QAR** | `RM-06b` |
| **Aprova e ratifica as Cartas** | **SOBERANO** | `FND-09 §8.2`, linha `DEP`. **Indelegavel. Nao ocorreu** |

---

## 1. Contexto — e por que este e o **menor rito competente**

A Missao 1.13.2 determinou *"produzir o menor rito competente"*. **Ele e este: `ADR` `C2` sem
`RFC`.** A dispensa nao e atalho — e clausula expressa de `FND-04 §2`:

> *"Instrumento | **RFC → ADR** (RFC **dispensavel** se a alternativa unica for obvia e DEP-GOV
> concordar por escrito)"*

| Condicao | Verificacao |
|---|---|
| **A alternativa unica e obvia** | ✅ A fonte ratificada **`FND-01 §6.2`** diz **`DEP-EXE`**. A Carta diz `DEP-PRD`. **`PJ-03`: em divergencia, a fonte prevalece, e o defeito e da projecao.** Nao ha segunda alternativa a considerar — corrigir a fonte para caber na projecao e **proibido** |
| **DEP-GOV concorda por escrito** | ✅ **Registrado em §4**, assinado por `DEP-GOV`, que **nao e o autor** — o autor e `DEP-EXE` (`FND-09 §8.2` linha `DEP`). **A concordancia e entre duas partes distintas**, nao autoconcordancia |

> **Divergencia declarada em relacao ao precedente.** `ADR-0023`, de materia identica, **teve**
> `RFC-0019`. **Este nao tem, e a razao e que a materia encolheu**: `RFC-0019` existia para
> **medir** o defeito e **descobrir seu alcance real** — foi ela que encontrou `RD-37`. Aqui o
> alcance **ja esta medido, enumerado e publicado** em `RFC-0019 §3` e em `PS-2026-010 §Q1`, com
> as tres Cartas nomeadas e o custo estimado. **Reinstruir o que ja esta instruido seria rito por
> simetria, nao por competencia** — e `FND-04 §2` autoriza expressamente a dispensa. **A economia
> e declarada, nao silenciosa** (`PI-13`).

## 2. Problema / Pergunta de decisao

> **Como fazer tres Cartas ratificadas pararem de afirmar um titular de portao que a fonte
> ratificada contradiz, sem tocar em nenhuma outra responsabilidade delas?**

## 3. Alternativas consideradas

| # | Alternativa | Veredito |
|---|---|---|
| **A** | **Substituir o titular na enumeracao de `§5.2`** — `DEP-EXE *(QG-0 e QG-1)*` | ✅ **ESCOLHIDA** |
| **B** | Trocar so a sigla, mantendo dois itens: `DEP-EXE *(QG-0)*, DEP-EXE *(QG-1)*` | ❌ **1 linha** em vez de 2, mas produz enumeracao com o **mesmo titular duas vezes** — verdadeira e ilegivel. **A economia de uma linha nao paga a piora de leitura** |
| **C** | Acrescentar nota normativa remetendo a `ADR-0018`, deixando a frase | ❌ **Deixaria a afirmacao falsa no texto** e criaria contradicao interna na mesma secao. Nota nao revoga frase |
| **D** | Esperar a proxima emenda de cada Carta e corrigir junto | ❌ `RD-37` esta aberto desde 2026-07-29 e **nenhuma das tres tem emenda prevista**. Equivale a `Z` com aparencia de plano |
| **Z** | **Nao fazer nada** | ❌ mas **valido**: **3 Cartas ratificadas** seguem afirmando titular errado de portao. **Nao bloqueia trabalho** — nao ha `Spec`, logo `QG-1` nunca foi atravessado. **O custo e que a pergunta *"quem libera `QG-1`?"* continua com duas respostas no acervo** |

## 4. Concordancia escrita de `DEP-GOV` com a dispensa de RFC — `FND-04 §2`

> **`DEP-GOV` concorda, por escrito e nesta data, com a dispensa de RFC para esta decisao.**
>
> **Fundamento verificado, e nao presumido:** *(i)* a alternativa e unica porque `PJ-03` **nao
> deixa escolha** — a projecao diverge da fonte, e quem cede e a projecao; *(ii)* o alcance do
> defeito **ja foi instruido** por `RFC-0019 §3`, que o mediu em **4 Cartas e 11 afirmacoes**, e
> **enumerou nominalmente** as tres aqui tratadas; *(iii)* o custo **ja foi publicado** em
> `PS-2026-010 §Q1`, que previu *"pacote proprio"* para exatamente estas tres; *(iv)* **`0`
> alternativas de merito** existem, porque **nenhuma autoridade e decidida** — `ADR-0018`
> decidiu, e este ADR **transcreve**.
>
> **A concordancia nao alcanca o merito**, que e de `DEP-EXE` propor e do **SOBERANO** ratificar
> nas Cartas. — **DEP-GOV**, 2026-07-30.

> **Residuo declarado (`PI-10`).** `DEP-GOV` **concorda com a dispensa**, **revisa** e **aprova**
> o ADR. As tres funcoes sao de `FND-09 §8.2` e de `FND-04 §2`, e **nenhuma delas e a autoria** —
> mas concentram-se numa parte so. **A independencia real vem de `DEP-QAR`** *(revisor
> independente)* **e do SOBERANO** *(que ratifica as Cartas)*. **Decima ocorrencia da familia
> `RC-02`** — `RD-39`.

## 5. Decisao *(as Cartas dependem de ratificacao)*

### 5.1 A correcao, literal e identica nas tres

```
antes  (DEP-OPS §5.2, DEP-GRW §5.2, DEP-TLS §5.2 — texto identico nas tres):
**Nenhum.** Os sete portoes de FND-01 §6.2 sao liberados por DEP-EXE *(QG-0)*, DEP-PRD
*(QG-1)*, DEP-ENG + DEP-GOV *(QG-2)*, DEP-QAR *(QG-3, QG-4)*, DEP-KMS *(QG-5)* e
DEP-QAR + DEP-GOV *(QG-6)*.

depois:
**Nenhum.** Os sete portoes de FND-01 §6.2 sao liberados por **DEP-EXE** *(QG-0 e QG-1)*,
DEP-ENG + DEP-GOV *(QG-2)*, DEP-QAR *(QG-3, QG-4)*, DEP-KMS *(QG-5)* e
DEP-QAR + DEP-GOV *(QG-6)*.
```

**Os sete portoes continuam enumerados; nenhum ganha ou perde dono; a contagem *"sete"* continua
exata.**

> **Divergencia de convencao, declarada em vez de escondida.** `RD-37` e `PS-2026-010 §Q1`
> publicaram o custo como **"1 linha por Carta"**. O `diff` mede **2 linhas substituidas e `0`
> acrescentadas**, **delta `0`** — porque a frase ocupa **duas** linhas fisicas e a correcao
> reflui a quebra. **Uma afirmacao corrigida, duas linhas tocadas, zero linhas de delta**: as
> tres medidas sao verdadeiras e contam coisas diferentes. **A alternativa `B` custaria
> literalmente 1 linha e foi recusada por legibilidade, nao por impossibilidade.**

### 5.2 O que muda no frontmatter das tres

| Campo | Antes | Depois | Fundamento |
|---|---|---|---|
| `versao` | `1.0.0` | **`1.1.0`** | `AC-08`/`FND-03 §6` — alteracao normativa incrementa MENOR |
| `atualizado_em` | `2026-07-28` | **`2026-07-30`** | Data real de execucao |
| `decisoes_relacionadas` | *(sem `ADR-0018`)* | **`+ ADR-0018, ADR-0025`** | A fonte da titularidade e a decisao em cascata |
| `status` | `ativo` | **`em-revisao`** | Nova versao de Carta volta a revisao e recebe **`O4`** no ato — **precedente literal: `DEP-PRD` e `DEP-EXE` 1.1.0** em `PS-2026-010` |
| `ratificacao` | `ratificada` | **`pendente`** | idem |

> **Os cinco campos de `AC-08` ja estao declarados nas tres Cartas** — `resumo`,
> `perfil_contexto`, `confidencialidade`, `revisor` e `ratificacao`. **`RD-27` nao as alcanca**, e
> este ADR **nao acrescenta campo nenhum**.

> ### Assimetria de regime de estado, declarada e **nao** resolvida por antecipacao — `RD-47`
>
> Nova versao de **Carta** volta a `em-revisao`/`pendente` e recebe `O4` no ato; nova versao de
> **fundacional** permanece `ativo`/`ratificada` e **nao** recebe `O4` — [PS-2026-009 §4.1](../governance/pacote-soberano-2026-07-29-fnd-11.md)
> e §5.2 acima. **As duas praticas sao precedentes vigentes, e nenhuma regra escrita as
> distingue:** `FND-10 §5.2` define `O4` sem dizer quando a promulgacao de versao nova o exige.
> **Consequencia pratica: o `H-P` de um objeto depende de qual precedente se aplica**, e hoje isso
> se resolve por tipo documental **por costume**. Achado **`RD-47`**, severidade **Baixa**, dono
> **DEP-GOV**, gatilho *"proxima emenda de `FND-10 §5`"*. **Nao resolvido aqui**: seria `C2` com
> ADR proprio sobre `FND-10`, e **este ADR nao tem competencia sobre `FND-10`**.

### 5.3 As outras seis Cartas — **medidas, e nada a corrigir**

| Carta | Ocorrencias de `QG-1` | Afirmacao falsa? | Por que |
|---|---|---|---|
| `DEP-ENG` | **2** | **Nao** | `§6.1` cita `QG-1` como **gatilho** de recebimento *(recebe a Spec quando o portao libera)* e `§6.2` como **condicao de devolucao**. **Nenhuma atribui titularidade** |
| `DEP-GOV`, `DEP-KMS`, `DEP-QAR` | **0** | **Nao** | Nao mencionam o portao |
| `DEP-PRD`, `DEP-EXE` | 27 · 22 *(candidatos)* | **Nao** | Corrigidas por [ADR-0023](ADR-0023-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md) |

### 5.4 O que esta decisao **nao** faz

| Nao faz | Verificacao |
|---|---|
| Criar ou transferir titular de portao | **`0`** — `ADR-0018` transferiu em 2026-07-29; isto **transcreve** |
| Alterar qualquer outra responsabilidade das tres Cartas | **`0` bytes** fora de `§5.2` e do frontmatter, medido por `diff` |
| Alterar quem **nao** libera portao | **`0`** — `DEP-OPS`, `DEP-GRW` e `DEP-TLS` continuam **nao liberando nenhum** |
| Alterar interfaces, riscos, metricas, Capabilities, autonomia ou classe | **`0`** |
| Alcancar `ADR-0019` / aprovacao de `Spec` | **`0`** — as tres Cartas **nao mencionam** aprovacao de `Spec` |
| Emendar `FND-01`, `FND-04`, `FND-09`, `FND-10` ou `TPL-spec` | **`0` bytes** |
| Criar excecao formal | **`0`** |

## 6. Justificativa

**O defeito e de projecao, e `PJ-03` ja decidiu quem cede.** Uma Carta ratificada afirmando que
`DEP-PRD` libera `QG-1` **contradiz `FND-01 §6.2`**, que e nivel 1 da hierarquia normativa contra
uma Carta de nivel inferior. **A duvida nao existe — existe apenas o texto errado.**

**E o momento e o mais barato que havera.** `0` Specs existem, `0` Produtos existem, `QG-1`
**nunca foi atravessado**: `KP-6` de `DEP-PRD` registra **0 liberacoes**. **Corrigir agora nao
invalida nenhuma decisao passada** — porque nao houve nenhuma sob a regra errada.

## 7. Impacto — a verificacao que importa

| Verificacao | Resultado | Evidencia |
|---|---|---|
| **Afirmacoes falsas sobre `QG-1` na familia das 9 Cartas** | **11 em 4 → `0` em `0`** *(com `ADR-0023`)*; **3 em 3 → `0` em `0`** *(por este ADR)* | [PS-2026-012 §5](../governance/pacote-soberano-2026-07-30-rd-37.md) — varredura das **nove** |
| **Cartas que nomeiam `DEP-EXE` como titular de `QG-1`** | **0 de 9 → 5 de 9** | idem |
| **Titulares criados ou transferidos** | **ZERO** | `ADR-0018`, ratificado |
| **Portoes** | **7 antes · 7 depois** | §5.1 — a contagem *"sete"* permanece exata |
| **Linhas de delta** | **`0`** nas tres · **+1** por Carta *(a linha de historico)* | §5.1 |
| **Outras responsabilidades alteradas** | **ZERO** | §5.4 |
| **Fontes de `foundation/` emendadas** | **ZERO** | `sha256` inalterado |
| Reversibilidade | **Tipo 2** — `H-A` das versoes substituidas publicado | §9 |

## 8. Riscos e mitigacao

| # | Risco | Sev. | Mitigacao |
|---|---|---|---|
| **RB-1** | A dispensa de RFC virar habito | Media | **§1 declara as duas condicoes e verifica cada uma**, e `§4` registra a concordancia por escrito. **A dispensa e do caso, nao da classe** |
| **RB-2** | **Ato nao vir** | Media | As tres Cartas seguem em **1.0.0** com a afirmacao falsa **vigente e declarada**. **Nao bloqueia** — `0` Specs, `QG-1` nunca atravessado |
| **RB-3** | A correcao ser lida como **rebaixamento de `DEP-PRD`** | Baixa | **`DEP-PRD` segue decidindo escopo e aprovando a `Spec`**; o que ele nao faz e **liberar o portao que verifica o que ele produz** — `FND-01 §6.2`, *regra de portao* |
| **RB-4** | `RD-47` ser lido como resolvido | Baixa | **§5.2 declara que nao e**, com dono e gatilho proprios |

## 9. Classificacao

| Campo | Valor |
|---|---|
| **Classe de mudanca** | **C2** — altera **texto de componente** (`FND-04 §2`). **Nao** toca principio imutavel, linha vermelha, hierarquia normativa, direito de decisao nem a Fundacao — teste item a item em §5.4 |
| **Tipo de reversibilidade** | **2** — restaurar tres arquivos aos `H-A` publicados |
| **Decisor do ADR** | **DEP-GOV** — `C2` com autor `DEP-EXE` (§Responsaveis) |
| **Ratificador do ADR** | **—** *(`C2 · Tipo 2` nao exige — `FND-04 §2.1`)* |
| **Aprovador e ratificador das Cartas** | **SOBERANO** — `FND-09 §8.2`, linha `DEP` |
| Data da decisao | **2026-07-30** |
| Data de vigencia | **as Cartas: pendente de ato** |

## 10. Plano de reversao

| Passo | Acao | Responsavel |
|---|---|---|
| 1 | ADR sucessor que supere este (`SU-04`, `O6`) | DEP-EXE; aprova DEP-GOV |
| 2 | Restaurar as tres Cartas aos `H-A` **`09d97a4c…3757`** *(OPS)*, **`0533fdf2…2ca1`** *(GRW)* e **`d5eede38…d9fc`** *(TLS)*, por copia binaria | DEP-GOV |
| 3 | `IR-09` em 3 de 3 | DEP-QAR |

**Custo medido da reversao: 3 restauracoes binarias + 1 ADR novo + 1 ato.** **Nenhum artefato
migra.**

## 11. Revisao

| Campo | Valor |
|---|---|
| Revisor independente | **DEP-QAR** — ≠ autor (`AC-03`, `RM-06b`) |
| Parecer | [PS-2026-012 §6](../governance/pacote-soberano-2026-07-30-rd-37.md) |
| Verificacao de aptidao | [FIT-2026-017](../governance/fitness/FIT-2026-017-convergencia-pre-ratificacao.md) |

## 12. Rastreabilidade

| Campo | Conteudo |
|---|---|
| **RFC** | **Dispensada** por `FND-04 §2`, com as duas condicoes verificadas (§1) e a concordancia escrita de `DEP-GOV` (§4). **Peca instrutoria: [RFC-0019 §3](../rfcs/RFC-0019-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md)**, que **mediu e nomeou** estas tres Cartas |
| Decisao de origem | [ADR-0018](ADR-0018-liberacao-do-portao-qg-1.md) — **ratificado** |
| Decisao irma, mesma cascata | [ADR-0023](ADR-0023-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md) — `DEP-PRD`, `DEP-EXE` |
| Pacote soberano | [PS-2026-012](../governance/pacote-soberano-2026-07-30-rd-37.md) |
| **Achado que fecha** | **`RD-37`** — integralmente, e com a familia das **nove** Cartas medida |
| Achado que abre | **`RD-47`** *(§5.2)* |
| Ressalva que fecha | **`R2`** de [FIT-2026-016](../governance/fitness/FIT-2026-016-canonizacao-e-propagacao.md) |
| Rito irmao, **independente** | [ADR-0024](ADR-0024-conformidade-de-contrato-das-fundacionais.md) — `RD-27` |
| Baseline vigente na submissao | **`BL-2026-07-29-10`** |

## Checklist de validade (FND-07 §4.1)

| # | Exigencia | Estado |
|---|---|---|
| VD-01 | Problema antes da solucao | ✅ §2 |
| VD-02 | ≥2 alternativas reais | ✅ **4** + `Z` |
| VD-03 | *"Nao fazer nada"* | ✅ `Z`, com efeito real |
| VD-04 | Criterios antes da escolha | ✅ §3 — legibilidade, alcance, `PJ-03` |
| VD-05 | Impacto medido | ✅ §7 — varredura das nove Cartas |
| VD-06 | Plano de reversao | ✅ §10 |
| VD-07 | Revisor ≠ autor | ✅ DEP-QAR ≠ DEP-EXE |
| VD-08 | Evidencia ausente declarada | ✅ `KP-6`: **0 liberacoes de `QG-1` observadas** — a correcao **nao** tem caso real de dano |
| VD-09 | Classificacao justificada | ✅ §9; dispensa de RFC fundamentada em §1 e §4 |

---

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-30 | DEP-EXE | Emenda **C2 · Tipo 2** candidata que **fecha `RD-37`**, estendendo a cascata de `ADR-0018` as **tres** Cartas que `ADR-0023` deixou de fora **por escopo determinado**. **Menor rito competente, e a menoridade e verificada, nao alegada:** a **RFC e dispensada** pela clausula expressa de `FND-04 §2`, com as **duas condicoes conferidas uma a uma** — a alternativa e unica porque **`PJ-03` nao deixa escolha**, e o alcance **ja fora instruido** por `RFC-0019 §3`, que mediu **4 Cartas e 11 afirmacoes** e **nomeou** estas tres — e com a **concordancia escrita de `DEP-GOV`** registrada em §4, entre **partes distintas**, porque o autor e `DEP-EXE`. **A divergencia em relacao ao precedente `ADR-0023`, que teve RFC, esta declarada com a razao: a materia encolheu, e reinstruir o instruido seria rito por simetria, nao por competencia.** **Uma afirmacao falsa por Carta, duas linhas substituidas, `0` de delta** — e a **divergencia de convencao contra o custo publicado de *"1 linha por Carta"* esta declarada em vez de escondida**, com a alternativa literalmente de 1 linha *(`B`)* **recusada por legibilidade**. §5.3 mede as **outras seis** Cartas e conclui **nada a corrigir**, distinguindo em `DEP-ENG` o uso de `QG-1` como **gatilho** do uso como **titularidade**. §5.2 declara e **nao resolve** a **assimetria de regime de estado** entre Carta e fundacional na promulgacao de versao nova — achado **`RD-47`** —, porque resolve-la seria `C2` sobre `FND-10`, fora da competencia deste ADR. **`0` titulares criados ou transferidos · 7 portoes antes e depois · `0` bytes fora de `§5.2` e do frontmatter · `0` outras responsabilidades alteradas · `0` fontes de `foundation/` emendadas · `0` excecoes formais.** **As Cartas nao vigoram sem ato do SOBERANO** (`FND-09 §8.2`, linha `DEP`). |
