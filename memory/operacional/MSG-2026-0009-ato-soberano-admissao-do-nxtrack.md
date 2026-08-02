---
id: MSG-2026-0009
titulo: Ato Soberano de admissao do nXtrack como primeiro Produto, com a decisao de Q2 gravada como artefato
tipo: relatorio
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: SOBERANO
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-08-01
atualizado_em: 2026-08-01
revisao_prevista: null
decisoes_relacionadas: [ADR-0005, ADR-0007, ADR-0012, ADR-0027, ADR-0030]
substitui: []
substituido_por: null
canal: DIRETIVA
emissor: SOBERANO
destinatario: DEP-GOV
ttl: 1 ciclo — expira sem perda; o ato fica ancorado por hash e os efeitos duraveis serao promovidos na aplicacao
resumo: Registra, como fonte canonica unica, o nono ato soberano — emitido sobre os itens I a VII da minuta de PS-2026-016 1.2.0, linhas 185-328, e ancorado no H-A do pacote —, que ratifica ADR-0030, aprova RFC-0025, cria PRO-nxtrack e determina a ordem de aplicacao. Grava tambem, pela primeira vez como artefato, a decisao de Q2. NADA foi aplicado por este registro.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# MSG-2026-0009 — Ato Soberano de 2026-08-01 *(nono ato)*

## Proposito

Registrar **uma unica vez** o ato que o Fundador emitiu sobre os **itens I a VII da minuta de
[`PS-2026-016`](../../governance/pacote-soberano-2026-08-01-nxtrack.md) 1.2.0**, com a **ancora de
hash** do texto assinado, os objetos que alcanca, o que **nao** alcanca, e a **fronteira entre
EMITIR e APLICAR** — que este registro **nao** atravessa. Registra tambem a **decisao de `Q2`**,
ate aqui existente **so em despacho**.

> **⚠️ ATO EMITIDO E NAO CONSUMIDO.** Por instrucao expressa do Fundador — *"NAO aplicar:
> confirmar o registro, assinalar o roadmap e parar"*. **`0` transicoes `O4` executadas, `0`
> `status` alterados, `0` `ratificacao` alteradas, `0` arquivos criados em `products/` e `0`
> baselines emitidas.** Os cinco objetos de `PS-2026-016 §2` seguem **byte a byte** como estavam.

> **Nono ato soberano registrado.** Os oito anteriores vivem em
> [MSG-2026-0001](MSG-2026-0001-ato-soberano-ratificacao-cartas-piloto.md),
> [MSG-2026-0002](MSG-2026-0002-ato-soberano-cartas-comando-plataforma-e-contexto.md),
> [MSG-2026-0003](MSG-2026-0003-ato-soberano-emenda-qar-e-criterio-de-consolidacao.md),
> [MSG-2026-0004](MSG-2026-0004-ato-soberano-cartas-emenda-constitucional-e-regime-do-fitness-check.md),
> [MSG-2026-0005](MSG-2026-0005-ato-soberano-aplicacao-dep-qar.md),
> [MSG-2026-0006](MSG-2026-0006-ato-soberano-aplicacao-integral.md),
> [MSG-2026-0007](MSG-2026-0007-ato-soberano-vigencia-do-framework-de-specifications.md) e
> [MSG-2026-0008](MSG-2026-0008-ato-soberano-emendas-e1-e-e3.md).
> **Nenhum dos oito foi editado.** Nove atos, nove fontes.

## Escopo

| Item | Definicao |
|---|---|
| Inclui | O ato e seus **sete** itens; a **ancora de hash** do texto assinado; os **5** objetos que alcanca, com `H-A`; os **2** `H-P` dos que sofrerao `O4`; as **6** condicoes anteriores de eficacia; a **decisao de `Q2`**; os limites; e a fronteira **emitir × aplicar** |
| **Nao** inclui | O **merito** da admissao — vive em [`PS-2026-016`](../../governance/pacote-soberano-2026-08-01-nxtrack.md), [`RFC-0025`](../../rfcs/RFC-0025-admissao-do-nxtrack-como-primeiro-produto.md), [`ADR-0030`](../../decisions/ADR-0030-admissao-do-nxtrack-como-primeiro-produto.md) e [`FIT-2026-023`](../../governance/fitness/FIT-2026-023-admissao-do-nxtrack.md) · **a aplicacao**, que e missao ministerial propria · `Q3` e `Q4`, **nao respondidas** |
| Instrumento | **Diretiva**, tipo documental de [FND-10 §4.6](../../foundation/10-artifact-framework.md), entidade `MSG`. Nenhum tipo, entidade, camada ou diretorio novo |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| **Emissor** | **SOBERANO** | `PI-01` — indelegavel; `FND-04 §6`, linha **Produto** |
| **Registra** | **DEP-GOV** | `LM-05`, `CV-09` |
| **Aplica** | **missao ministerial propria**, na ordem de `PS-2026-016 §6.2` | Item **VI** do ato. **Ainda NAO exercida** |
| **Verifica a eficacia da aplicacao** | **DEP-QAR** | FND-10 §10.5; `IR-09` |

---

## 1. Ancora do ato — o texto assinado, por hash

> **O ato foi emitido sobre um texto identificado, nao sobre uma referencia.** Se o arquivo mudar,
> o `H-A` abaixo deixa de reproduzir — e o ato **nao alcanca o texto novo**.

| Campo | Valor |
|---|---|
| **Objeto assinado** | [`PS-2026-016`](../../governance/pacote-soberano-2026-08-01-nxtrack.md) — **itens I a VII da minuta de §6**, linhas **185–328** |
| **Versao** | **1.2.0** — a que torna `CA-2` INFORMATIVO |
| Caminho | `governance/pacote-soberano-2026-08-01-nxtrack.md` |
| **`H-A` do pacote assinado** | **`e6fa26e84bffc40f14f73b57f436f1eee6194b7fa605c3540d872f7b227744ae`** |
| Como reproduzir | `sh ferramentas/hashes.sh ha governance/pacote-soberano-2026-08-01-nxtrack.md` |
| **`sha256` do recorte `185–328`** | **`8f4c6eacace5f123f5b71c7483cd9e1a4e8a45aa1c90d5b0d857bd58d4c9369a`** |
| **`sha256` do recorte `185–327`** *(so o texto)* | `00f97328d30d6295463c1ec0d73f5b3ac88c596a2b487408ad0f27542ad7a467` |
| **`sha256` do bloco `ATO SOBERANO`, `290–327`** *(itens I a VII)* | `ae821d8a8b6e3c42433efa11d917523bf390beb0b26a4749a4c0ccb24c1cd622` |

> **`AN-1` — a faixa declarada foi CONFERIDA linha a linha, e a precisao esta escrita.** A linha
> **185** e `## 6. Minuta do ato soberano`; a linha **327** e `> **Soberano** · data: ___`; a linha
> **328** e **em branco**; e `## 7. Rastreabilidade` comeca em **329**. **O recorte assinado
> contem §6 inteira e nao alcanca um unico byte de §7.** A faixa que o Fundador declarou —
> `185–328` — inclui a linha em branco final, e por isso os **dois** `sha256` estao publicados
> acima: quem conferir por qualquer das duas leituras reproduz.

> **`AN-2` — o `H-A` foi MEDIDO no arquivo, nunca lido da transcricao.** O despacho declarou
> `e6fa26e8…`; a medicao independente sobre `governance/pacote-soberano-2026-08-01-nxtrack.md`
> devolveu `e6fa26e84bffc40f14f73b57f436f1eee6194b7fa605c3540d872f7b227744ae` — **os 64 digitos
> conferem**. A ordem importa: **medir e depois comparar**, nunca copiar e depois declarar
> conferido.

> **`AN-3` — este pacote e o mesmo que a `1.1.0` reancorou.** O ato emitido sobre a **1.0.0**
> **nao foi gravado**, por determinacao do proprio despacho que o reteve ate a reassinatura
> (`PS-2026-016`, historico da `1.1.0`). **Este registro e o do ato reassinado sobre a `1.2.0`, e
> e o unico.**

## 2. Decisao soberana — literal

**ATO SOBERANO — ADMISSAO DO nXtrack (reassinatura)**

**Eu, Soberano do LucaX Enterprise OS, no exercicio da competencia de `FND-04 §6` sobre criacao de
Produto (`C2` · `Tipo 1`), tendo conferido `CA-1` a `CA-6` de `PS-2026-016 §6.1` em 6 de 6, EMITO
o ato dos itens I a VII da minuta redigida em
`governance/pacote-soberano-2026-08-01-nxtrack.md`, versao 1.2.0, `H-A` do pacote `e6fa26e8...`,
linhas 185-328, integralmente e sem alteracao de termo.**

**Declaro ciencia de que `RECOGNIZE` nao afirma merito tecnico; de que as quatro ressalvas de
`FIT-2026-023` seguem abertas; e de que a lacuna `LM-6(a)` — zero ocorrencias de LGPD, ANPD,
politica de privacidade e termos de uso, num produto com nome, `senha_hash` e sal por conta — e
materia da primeira `Spec`, com prioridade sobre as demais de `LA-7`.**

**Fundador e Soberano — LucaX Enterprise OS**

### 2.1 Os sete itens incorporados por referencia

O ato foi emitido **integralmente e sem alteracao de termo**. Os itens vivem em
[`PS-2026-016 §6`](../../governance/pacote-soberano-2026-08-01-nxtrack.md), linhas 290–327, e sao
transcritos aqui **em sumario** — o texto que vale e o do pacote, ancorado pelos `sha256` de §1.

| Item | O que determina |
|---|---|
| **I** | **RATIFICA `ADR-0030`** — admite a **existencia** do nXtrack pelo portao de origem externa de `ADR-0007 §5.3`, com **`G0` = `IDENTIDADE`** e **`G3` = `RECOGNIZE`**, nos termos de `ADR-0027 §5.1` e `§5.2` |
| **II** | **APROVA `RFC-0025`**, instrumento de origem da decisao |
| **III** | **CRIA o Produto `PRO-nxtrack`**, em `products/nxtrack/carta.md`, a partir do candidato de `H-A` `4d4c12e0…75c5`, com as **cinco** Capabilities declaradas e o criterio de encerramento de §6 da Carta |
| **IV** | **DECLARA** que o ato admite **identidade e nada mais**: **`0` bytes** do repositorio do candidato entram no acervo, e cada peca que um dia queira entrar tera **portao proprio** |
| **V** | **DECLARA** que o ato **nao afirma merito tecnico**, **nao valida** `H1`, **nao mede** usuarios reais e **nao resolve** a custodia — as **quatro** ressalvas de `FIT-2026-023` seguem **abertas, com dono e gatilho** |
| **VI** | **DETERMINA** a ordem de aplicacao de `§6.2`, com reconciliacao **na mesma mudanca** e `products` declarado no medidor **antes** da baseline. **`CA-1`, `CA-3`, `CA-4`, `CA-5` e `CA-6` sao BLOQUEANTES; `CA-2` e INFORMATIVO e nao para nada.** A ancora sao os **5** `sha256` por objeto mais `tree` e `HEAD` do candidato — **nunca a arvore inteira** |
| **VII** | **DECLARA** que o ato **nao cria `Spec`, nao fecha `RD-33` e nao decide `E2`** |

### 2.2 A declaracao de ciencia — o que ela acrescenta, medido

| # | Declaracao do Fundador | Estado medido |
|---|---|---|
| `DC-1` | *"`RECOGNIZE` nao afirma merito tecnico"* | Coincide com o item **V** e com `LA-6` de `§6.3`. [`ADR-0027 §5.2`](../../decisions/ADR-0027-classe-de-admissao-de-existencia-no-portao-de-origem-externa.md): a classe **declara que nao avaliou** |
| `DC-2` | *"as quatro ressalvas de `FIT-2026-023` seguem abertas"* | ✅ **Conferido no parecer: `4` ressalvas**, cada uma com dono e gatilho — [`FIT-2026-023 §3`](../../governance/fitness/FIT-2026-023-admissao-do-nxtrack.md), veredito **`apto-com-ressalva`** |
| `DC-3` | *"`LM-6(a)` e materia da primeira `Spec`, **com prioridade sobre as demais de `LA-7`**"* | **Acrescimo do ato.** `LA-7` de `§6.3` remete **tres** trabalhos a primeira `Spec` — `RD-71` *(custodia)*, `LM-6` *(dado pessoal)* e `RD-74` *(`VC-03`)* — **sem ordem entre eles**. O ato **fixa a ordem**: `LM-6(a)` primeiro |
| `DC-4` | *"num produto com nome, `senha_hash` e sal por conta"* | Caracterizacao do dado pessoal do candidato, coerente com `FG-11` de [`PT-2026-014 §3`](../../governance/relatorio-transicao-2026-08-01-portao-nxtrack.md) — **dado real vivo** e **aprendizado coletivo entre usuarios** |

> **`LM-6(a)`, medido na fonte e nao parafraseado.** [`PT-2026-014 §4`](../../governance/relatorio-transicao-2026-08-01-portao-nxtrack.md)
> registra **`0` ocorrencias** de **seis** termos — `LGPD`, `GDPR`, `ANPD`, *"dados pessoais"*,
> *"politica de privacidade"* e *"termos de uso"* —, apuradas em varredura de **nove** termos
> regulatorios. O ato enumera **quatro** dos seis; **a medicao e `0` para os seis**, e o
> enunciado do ato e subconjunto exato dela. **Nada foi ampliado nem reduzido aqui.**

## 3. Objetos que o ato alcanca — **5**, com o `H-A` de cada um

**Lidos de [`PS-2026-016 §2`](../../governance/pacote-soberano-2026-08-01-nxtrack.md) e
reconferidos no arquivo vivo nesta emissao: `5` de `5`.**

| # | Objeto | Estado hoje | `H-A` | Reproduz? |
|---|---|---|---|---|
| `O-1` | [**`ADR-0030`**](../../decisions/ADR-0030-admissao-do-nxtrack-como-primeiro-produto.md) | `em-revisao` · `ratificacao: pendente` | `80b4989efbb1f256e4d6f9c09d64fff7d201dd9d1ec6afe3395417b34fcba89f` | ✅ |
| `O-2` | [**`RFC-0025`**](../../rfcs/RFC-0025-admissao-do-nxtrack-como-primeiro-produto.md) | `em-revisao` | `0db9536258d117a15b731e4a7bd01c683a630dca1f134b5e2155fdf260b1221c` | ✅ |
| `O-3` | [**`FIT-2026-023`**](../../governance/fitness/FIT-2026-023-admissao-do-nxtrack.md) | `ativo` — parecer, **nao transiciona** | `331fcf47db35cc98d8ca5df0f3de9f1ee5b30963602dc351adade64c2bcc9cff` | ✅ |
| `O-4` | [**`PT-2026-014`**](../../governance/relatorio-transicao-2026-08-01-portao-nxtrack.md) | `ativo` — registro, **nao transiciona** | `a6db51da4eeebf83a84f9dc88d5e05f9e0e15014a3131e54fd31a0ebf2217929` | ✅ *(valor **reancorado** na `1.1.0` — `RD-78`)* |
| `O-5` | **Carta `PRO-nxtrack` 1.0.0** — candidata, **FORA do acervo** | **nao e artefato** (`FR-10`) | `4d4c12e0403344535ec410f4ff71353c1e7feaad6230bc33343f42018cea75c5` | ✅ |

> **`CA-4` conferida em `5` de `5` nesta emissao**, e o caminho de cada medicao esta declarado —
> `O-5` foi medido em
> `_missao-1-13-4-4-2026-08-01/candidatos/carta-pro-nxtrack-1.0.0.md`, **fora do acervo**. Publicar
> `H-A` sem declarar o caminho medido foi o defeito `RD-19`; `DF-1` de `§3` do pacote o fecha, e
> este registro o repete de propria mao.

> **`O-4` reproduz o valor REANCORADO, e a perda que a reancoragem nao apaga continua registrada.**
> O `H-A` publicado na `1.0.0` — `f4f63f1e…a826e` — **nao existe em nenhuma arvore alcancada**, e
> **nao ha diff**. Achado **`RD-78`**, severidade **Alta**, dono **DEP-GOV**, gatilho *"missao de
> catalogo ou proxima emissao de baseline"* — [`PS-2026-016 §2.3`](../../governance/pacote-soberano-2026-08-01-nxtrack.md).
> **Nenhum item do ato toca `O-4`**, e por isso a aplicacao nao depende dos bytes dele — mas a
> **decisao** se apoiou neles.

## 4. `H-P` — somente os DOIS que sofrerao `O4`

**Lidos do proprio arquivo, jamais de transcricao**, e **recalculados** sobre os objetos vivos
nesta emissao — **`2` de `2` reproduzem**.

| Objeto | `O4` autorizado pelo ato | `H-P` *(apos `O4`)* | Reproduz hoje? |
|---|---|---|---|
| **`ADR-0030`** | **`status` E `ratificacao`** — `em-revisao` → `ativo`, `pendente` → `ratificada` | `906dccd303c6240561a30ec5f62253d247567beb661a62b21d3f89b0e7c719fa` | ✅ |
| **`RFC-0025`** | **somente `status`** — `em-revisao` → **`aprovado`** | `eecde50420cb88e0619a30cd435506049567259753f8c01d8776ba1d844a7b63` | ✅ |
| `FIT-2026-023` · `PT-2026-014` | **nenhum** — parecer e registro nascem `ativo` | **nao se publica** | — |
| Carta `PRO-nxtrack` | **nenhum** — o arquivo aplicado tera `H-A` **proprio**, que a missao de aplicacao publica | **nao se publica** | — |

> **`IN-1` — a diferenca de instrumento esta DECLARADA, e foi exercida.** O `H-P` de `ADR-0030`
> reproduz pelo **instrumento padrao** (`hashes.sh hp`). O de `RFC-0025` **nao** reproduz por ele:
> o padrao implementa *"`em-revisao`|`aprovado` → `ativo`"*, e o ciclo de `RFC` **termina em
> `aprovado`** — precedente literal, `RFC-0022` esta `aprovado`, nao `ativo`. O valor acima foi
> reproduzido pela **variante explicita** *(`status: em-revisao` → `status: aprovado`, campo
> unico, dentro do frontmatter)*, a mesma que `PS-2026-016 §2.1` declara. **Aplicar o instrumento
> padrao a `RFC-0025` produziria `ativo`, que NAO e a transicao que o ato autoriza.**

**`H-N` invariante ao `O4` — `2` de `2`, remedidos nesta emissao:**

| Objeto | `H-N` publicado | Reproduz? |
|---|---|---|
| `ADR-0030` | `6325d9c11974b1958d64f1e0636bef8736c6e35fbb22e5e84094d30f7bd2b266` | ✅ |
| `RFC-0025` | `adb4e4c40d00fc6cd55bb03de347f496f72b10e555eef9cc827f5af7e661305f` | ✅ |

> **O `O4` esta DETERMINADO, nao inferido:** o `H-P` publicado **e** a regra para estes dois, e a
> reproducao acima prova que a transicao declarada e a unica que os alcanca a partir do estado
> atual. **`atualizado_em` NAO e tocado em nenhum dos dois** — o filtro de `IR-03` o remove, e o
> `H-N` invariante e a prova.

## 5. `Q2` — a decisao, gravada como artefato pela primeira vez

> **Ate este registro, `Q2` vivia SO em despacho.** `PS-2026-016 §6.1` declarava, na emenda
> `1.1.0`: *"a decisao ainda NAO esta gravada como artefato, por determinacao do proprio despacho,
> que a reteve ate a reassinatura deste pacote"*. **A reassinatura ocorreu, e a retencao termina
> aqui.**

| Campo | Valor |
|---|---|
| **Questao** | **`Q2` de [`PS-2026-016 §8`](../../governance/pacote-soberano-2026-08-01-nxtrack.md)** — *"A ressalva **«se seguir sendo o primeiro produto comercial»** de `PS-2026-013 §7` condiciona este ato?"* |
| **Decisao** | **NAO.** A ressalva **nao condiciona** o ato |
| **Quem decidiu** | **SOBERANO**, por despacho de **2026-08-01** — *"É interpretacao de ato proprio do Nivel 0"* |
| **Fundamento** | [`PT-2026-009 §1`](../../governance/relatorio-transicao-2026-07-30-convergencia.md) e `PS-2026-013 §7` **sao artefatos DISTINTOS**. A decisao **7** nomeia o nXtrack **em texto literal e sem ressalva**, e a palavra `comercial` tem **`0`** ocorrencias no arquivo de `PT-2026-009` — **medido**. Le-los como um so foi o que gerou `L1` × `L2`, achado **`RD-64`** |
| **Efeito** | **`CA-6` CONFERIDA.** Era a **unica** condicao anterior de eficacia ainda aberta; com ela, `CA-1` a `CA-6` fecham em **6 de 6**, como o ato declara |
| **A ressalva desapareceu?** | **Nao.** Ela **nao foi descartada nem revogada**: foi **respondida**. Continua legivel em `PS-2026-013 §7`, artefato historico **nao editado** (`BL-02`, `LV-04`) |

> **`ET-1` — a etiqueta, conferida antes de gravar.** A questao respondida e o **`Q2` de
> `PS-2026-016 §8`** — **nao** o `Q2` de `PS-2026-014 §7`, que e o pacote do **medAlly** e cujo
> `Q2` ja fora respondido no **oitavo ato** ([`MSG-2026-0008 §2`](MSG-2026-0008-ato-soberano-emendas-e1-e-e3.md),
> item **I**). Confundir os dois gravaria **duas respostas para a mesma etiqueta** em dois atos
> distintos. A linhagem correta esta no catalogo: *"a ressalva de `PS-2026-013 §7` vira `Q2` de
> `PS-2026-016`"*.

**`Q3` e `Q4` — NAO respondidas, e o ato nao as respondeu:**

| # | Questao | Estado apos este ato |
|---|---|---|
| **`Q3`** | **Qual e a meta do criterio de sucesso do Produto?** | ⚠️ **ABERTA.** O ato **nao fixa numero**, e a Carta segue com a meta **em aberto**. `FND-04 §6` poe a decisao no Soberano. **Nao e condicao de eficacia** — `PS-2026-016 §8` |
| **`Q4`** | **A admissao deve esperar politica de dado pessoal?** | ⚠️ **NAO ROTULADA COMO RESPONDIDA pelo ato** — e o ato **dispoe da mesma materia**: admite **sem esperar** e determina que `LM-6(a)` seja a **materia da primeira `Spec`, com prioridade**. **Registrar isso como *"`Q4` respondida"* seria afirmar rotulo que o ato nao usou**; registrar o efeito e o que a fonte sustenta |

## 6. O que este REGISTRO nao fez — a fronteira entre emitir e aplicar

| # | Estado, medido nesta emissao | Valor |
|---|---|---|
| 1 | `ADR-0030` | segue **`em-revisao`** · `ratificacao: pendente` — **`0` bytes** |
| 2 | `RFC-0025` | segue **`em-revisao`** — **`0` bytes** |
| 3 | `products/` | **NAO existe** na raiz do acervo |
| 4 | `products/nxtrack/carta.md` | **NAO criado**. O candidato permanece **fora do acervo** |
| 5 | `products` na lista fechada de `baseline.sh` | **NAO declarado** — passo **6** de `§6.2`, da missao de aplicacao |
| 6 | Baseline nova | **NAO emitida** — passo **7** de `§6.2` |
| 7 | `PS-2026-016` | **`0` bytes** — a ancora de §1 continua reproduzindo |
| 8 | Os **5** objetos alcancados | **`0` bytes** — `5` de `5` `H-A` reproduzem |
| 9 | Candidato nXtrack | **intacto** — nenhuma escrita desta emissao no repositorio de terceiro |
| 10 | Produtos em vigor · `Spec`s | **`0`** · **`0`** |
| 11 | `RD-33` | **BLOQUEANTE**, e **nao fecha aqui** — item **VII** do ato e `LA-3` |

> **Emitir e aplicar sao dois atos de naturezas diferentes, e o Fundador os separou
> expressamente.** Registrar o ato **nao o consome**: o consumo e a missao ministerial de §8, e
> **so ela** pode mover `status`, `ratificacao` e criar a Carta.

> **Este e o SEGUNDO ato do acervo registrado ANTES da aplicacao** — o primeiro foi
> [`MSG-2026-0008`](MSG-2026-0008-ato-soberano-emendas-e1-e-e3.md). **A pratica deixa de ser
> excecao e passa a ter precedente**, e a separacao continua sendo **do Fundador**, nao do
> executor.

## 7. Condicoes de eficacia — `6` de `6`, com o regime de cada uma

**Anteriores — [`PS-2026-016 §6.1`](../../governance/pacote-soberano-2026-08-01-nxtrack.md):**

| # | Condicao | Regime | Estado |
|---|---|---|---|
| `CA-1` | `ADR-0027` **`ativo`**, tornando `G0` e `RECOGNIZE` disponiveis | **BLOQUEANTE** | ✅ conferido no frontmatter |
| `CA-2` | **Registrar a baseline vigente no instante da aplicacao** | **INFORMATIVO** — **nao para nada** (`§6.1.1` + item **VI**) | ✅ regime declarado nas **duas** metades |
| `CA-3` | `G1` a `G5` **cumpridos e registrados** | **BLOQUEANTE** | ✅ `PT-2026-014 §3` |
| `CA-4` | Os **5** objetos reproduzindo os `H-A` publicados | **BLOQUEANTE** | ✅ **`5` de `5`**, remedidos — §3 |
| `CA-5` | Candidato **intacto** — `tree` e `HEAD` | **BLOQUEANTE** | ✅ nenhuma escrita desta emissao no repositorio de terceiro |
| `CA-6` | **`Q2` respondida** | **BLOQUEANTE** | ✅ **RESPONDIDA**, e agora **gravada como artefato** — §5 |

> **A ancora do ato e por objeto consumido: `5` `sha256` de `CA-4`, mais `tree` e `HEAD` do
> candidato em `CA-5`** — **nunca a arvore inteira**. O item **VI** do ato mantem isso
> integralmente, e `§6.1.1` escreve o motivo: **o pacote mora dentro do acervo que `CA-2`
> mediria**, e toda emissao legitima a invalidaria — inclusive as emendas que o Soberano ordenou.

> **`CA-2` sera cumprida na aplicacao MEDINDO, nunca comparando contra valor congelado.** O trio
> medido entra no relatorio de transicao da missao ministerial. Divergencia contra qualquer valor
> anterior e **esperada** num acervo vivo.

## 8. A missao ministerial que consome este ato — **uma so**

Determinada pelo item **VI**, na ordem de
[`PS-2026-016 §6.2`](../../governance/pacote-soberano-2026-08-01-nxtrack.md):

| Passo | O que faz |
|---|---|
| **1** | Conferir os **5** `H-A` publicados em `§2` do pacote |
| **2** | `O4` em `RFC-0025`: `status` → **`aprovado`** — pela **variante**, nunca pelo instrumento padrao (`IN-1`) |
| **3** | `O4` em `ADR-0030`: `status` → **`ativo`**; `ratificacao` → **`ratificada`** |
| **4** | Criar `products/nxtrack/carta.md` a partir do candidato `4d4c12e0…75c5`, com `status: ativo` e `ratificacao: ratificada`, **publicando o `H-A` do arquivo aplicado** |
| **5** | Reconciliar catalogo `§2`, `§4`, `§7`, `§9`, `§10` e as projecoes `M3` — **na mesma mudanca** |
| **6** | Acrescentar **`products`** a lista fechada positiva de `baseline.sh` — **antes** de medir |
| **7** | Emitir nova baseline e **reproduzi-la em duas execucoes** |

> **`OA-1` — o passo 6 nao e detalhe de ferramenta.** `baseline.sh` mede por **lista fechada
> positiva** e **para com erro** diante de raiz nao declarada. Criar `products/` sem declara-la
> **impede medir a baseline** — e isso e o portao funcionando, nao falha.

> **Congelamento em vigor**, declarado pelo Fundador: nenhuma missao de governanca nova ate
> existir a **primeira `Spec`**. Achado novo e **registrado com dono e gatilho e fica aberto**.
> **Depois da aplicacao**, a sequencia declarada e: `RD-33` destravado → **1.13.5, a primeira
> `Spec`**, cuja materia o ato ja fixou — **`LM-6(a)`, com prioridade sobre as demais de `LA-7`**.

## 9. Limites — o que este ato NAO faz

**De [`PS-2026-016 §6.3`](../../governance/pacote-soberano-2026-08-01-nxtrack.md), integralmente
mantidos pelo ato:**

| # | O ato **nao** |
|---|---|
| `LA-1` | Admite **conteudo** algum do candidato. `G0` e `IDENTIDADE`; **`0` bytes**. Admitir conteudo depois e **passagem nova pelo portao** (`FR-07`, `AD-02`) |
| `LA-2` | Autoriza inventariar o repositorio do candidato |
| `LA-3` | Cria `Spec`, nem fecha `RD-33` — que **so fecha apos a vigencia**, por missao propria |
| `LA-4` | Decide `E2`. `RFC-0023`, `ADR-0028` e `FIT-2026-021` seguem **intactos**; fila de retidos: **2** |
| `LA-5` | Altera `ADR-0007`, `ADR-0026` ou qualquer fundacional — **`0` bytes** |
| `LA-6` | Afirma merito tecnico do nXtrack. `RECOGNIZE` **declara que nao avaliou** |
| `LA-7` | Resolve a custodia do candidato (`RD-71`), a lacuna de dado pessoal (`LM-6`) ou `VC-03` (`RD-74`) — **os tres sao trabalho da primeira `Spec`**, e o ato **fixa `LM-6(a)` como o primeiro deles** |

**Acrescentados por este registro, e medidos:**

| # | Limite |
|---|---|
| `LR-1` | **Nao responde `Q3` nem `Q4`** — §5 |
| `LR-2` | **Nao fecha achado algum por inferencia.** `RD-71` a `RD-79` seguem **ABERTOS, com dono e gatilho, e sem missao designada** |
| `LR-3` | **Nao edita `MSG`, `FIT`, `PS`, `PT`, `ADR`, `RFC` nem baseline historica** — `LV-04`, `BL-02` |
| `LR-4` | **Nao reabre `Q1`**, respondida em 2026-08-01 e que **nao se reabre** |
| `LR-5` | **Nao emite baseline.** A baseline vigente publicada continua sendo **`BL-2026-08-01-01`**; o valor **medido** nesta emissao esta em §10 e **nao a substitui** |

## 10. Estado do acervo medido nesta emissao — e por que ele nao para nada

> **Medido pelo instrumento de lista fechada positiva, e declarado como o que e: medicao, nao
> baseline emitida.** `CA-2` e **INFORMATIVO**, e a ancora do ato sao os `5` `sha256` por objeto.

| Momento | Artefatos | Linhas | Impressao digital |
|---|---|---|---|
| **`BL-2026-08-01-01`** — baseline **publicada** e vigente | **213** | **62.250** | `4252fe47…621c` |
| **Antes desta emissao**, medido pelo instrumento | **214** | **62.536** | `7ea160e2a5035004f275c1143a9aa09105acdd403e23bb823a12cdc84c3cd3dc` |

> **O `+1` sobre a baseline publicada nao nasceu nesta emissao.** [`governance/roadmap-canonico.md`](../../governance/roadmap-canonico.md)
> ja existia no acervo antes desta sessao e **entra na lista fechada positiva** do medidor, sem
> ter entrada no catalogo — achado **`RD-80`**, aberto com dono e gatilho.

> **A partir desta emissao o instrumento RECUSA medir**, e a recusa e correta: `CLAUDE.md` foi
> criado na raiz do acervo por determinacao do Fundador e **nao esta declarado** na lista fechada
> — nem como acervo, nem como nao-acervo. **Portao de raiz, exatamente o mecanismo de `OA-1`.**
> Achado **`RD-81`**, dono **SOBERANO** *(a escolha do lado da lista e dele)*, gatilho *"proxima
> emissao de baseline"*. **Nao para este registro**, porque `CA-2` e informativo e **nenhuma
> baseline e emitida aqui**; **para a missao de aplicacao**, cujo passo **7** exige medir.

## 11. Nao edicao das fontes anteriores

**Nenhum `MSG`, `FIT`, `PS`, `PT`, `ADR`, `RFC` ou baseline historica foi editado por este
registro** — `LV-04`, `BL-02`. O registro **cria** um artefato e **projeta** a criacao no catalogo
e nos indices, como `RG-02` e `CV-04` exigem; **nao toca nenhuma fonte normativa** e **nao toca o
texto assinado**, cuja integridade e a propria ancora de §1.

**Copia datada anterior a primeira escrita:**
`_backups/LucaX-Enterprise-OS_2026-08-01_pre-registro-nono-ato` — **592** arquivos, baseline
reconferida **na copia**: **214 · 62.536 · `7ea160e2…d3dc`**.

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-08-01 | SOBERANO | Registro do **nono ato soberano**, e o **segundo do acervo registrado ANTES da aplicacao**, por instrucao expressa do Fundador. **RATIFICA `ADR-0030`**, **APROVA `RFC-0025`**, **CRIA `PRO-nxtrack`** e determina a ordem de aplicacao de `§6.2`, com `CA-2` INFORMATIVO nas duas metades. **Ancorado no `H-A` do pacote `PS-2026-016` 1.2.0** — `e6fa26e8…44ae`, **medido no arquivo e nao lido da transcricao** —, com o recorte `185–328` hasheado em `8f4c6eac…369a` e a faixa conferida linha a linha *(`327` e a assinatura; `328` e branco; §7 comeca em `329`)*. **`5` de `5`** `H-A` reproduzem, **`2` de `2`** `H-P` — o de `RFC-0025` pela **variante declarada** — e **`2` de `2`** `H-N` invariantes. **Grava `Q2` como artefato pela primeira vez**: a ressalva de `PS-2026-013 §7` **NAO condiciona** o ato, e `CA-6` fecha em **6 de 6**. `Q3` e `Q4` **nao respondidas**. **`0` transicoes aplicadas, `0` arquivos em `products/`, `0` baselines emitidas, `0` bytes em `PS-2026-016` e nos cinco objetos.** `RD-33` segue **bloqueante**; `RD-71` a `RD-79` seguem **abertos**; achados novos **`RD-80`** e **`RD-81`**, ambos **com dono e gatilho e sem missao designada**. |
