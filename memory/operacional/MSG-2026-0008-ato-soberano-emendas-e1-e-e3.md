---
id: MSG-2026-0008
titulo: Ato Soberano de aprovacao de ADR-0027 no rito C2 e ratificacao de ADR-0029, com E2 expressamente adiada
tipo: relatorio
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: SOBERANO
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-07-31
atualizado_em: 2026-07-31
revisao_prevista: null
decisoes_relacionadas: [ADR-0005, ADR-0007, ADR-0012, ADR-0027, ADR-0029]
substitui: []
substituido_por: null
canal: DIRETIVA
emissor: SOBERANO
destinatario: DEP-GOV
ttl: 1 ciclo — expira sem perda; o ato fica ancorado por hash e os efeitos duraveis serao promovidos na aplicacao
resumo: Registra, como fonte canonica unica, o oitavo ato soberano — emitido sobre a minuta recortada de PS-2026-015 1.2.0 e ancorado no H-A dela —, que responde Q2 emendando ADR-0007 agora, autoriza DEP-EXE a aprovar ADR-0027 no rito C2, ratifica ADR-0029 e adia E2. NADA foi aplicado por este registro.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# MSG-2026-0008 — Ato Soberano de 2026-07-31 *(oitavo ato)*

## Proposito

Registrar **uma unica vez** o ato que o Fundador emitiu sobre a **minuta recortada de
`PS-2026-015` 1.2.0**, com a **ancora de hash** do texto assinado, os objetos que alcanca, o que
**nao** alcanca, e a **fronteira entre EMITIR e APLICAR** — que este registro **nao** atravessa.

> **⚠️ ATO EMITIDO E NAO CONSUMIDO.** Este e o **primeiro ato do acervo registrado ANTES da
> aplicacao**, por instrucao expressa do Fundador: *"NAO aplicar nada ainda: confirmar o registro
> e parar"*. **`0` transicoes `O4` executadas, `0` `status` alterados, `0` `ratificacao`
> alteradas, `0` registros de `SA-6` criados e `0` aprovacoes de DEP-EXE emitidas.** Os nove
> objetos das tres emendas seguem **byte a byte** como estavam.

> **Oitavo ato soberano registrado.** Os sete anteriores vivem em
> [MSG-2026-0001](MSG-2026-0001-ato-soberano-ratificacao-cartas-piloto.md),
> [MSG-2026-0002](MSG-2026-0002-ato-soberano-cartas-comando-plataforma-e-contexto.md),
> [MSG-2026-0003](MSG-2026-0003-ato-soberano-emenda-qar-e-criterio-de-consolidacao.md),
> [MSG-2026-0004](MSG-2026-0004-ato-soberano-cartas-emenda-constitucional-e-regime-do-fitness-check.md),
> [MSG-2026-0005](MSG-2026-0005-ato-soberano-aplicacao-dep-qar.md),
> [MSG-2026-0006](MSG-2026-0006-ato-soberano-aplicacao-integral.md) e
> [MSG-2026-0007](MSG-2026-0007-ato-soberano-vigencia-do-framework-de-specifications.md).
> **Nenhum dos sete foi editado.** Oito atos, oito fontes.

## Escopo

| Item | Definicao |
|---|---|
| Inclui | O ato e seus **sete** itens; a **ancora de hash** do texto assinado; os **6** objetos que alcanca e os **3** que exclui; os `H-P` dos **dois** que sofrerao `O4`; as condicoes de eficacia; os limites; e a fronteira **emitir × aplicar** |
| **Nao** inclui | O **merito** das emendas — vive em [`PS-2026-015`](../../governance/pacote-soberano-2026-07-31-emendas-de-instrumento.md), `RFC-0022`, `RFC-0024`, `ADR-0027` e `ADR-0029` · **a aplicacao**, que e missao ministerial propria · `E2`, **adiada** |
| Instrumento | **Diretiva**, tipo documental de [FND-10 §4.6](../../foundation/10-artifact-framework.md), entidade `MSG`. Nenhum tipo, entidade, camada ou diretorio novo |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| **Emissor** | **SOBERANO** | `PI-01` — indelegavel |
| **Registra** | **DEP-GOV** | `LM-05`, `CV-09` |
| **Aprova `ADR-0027` no rito `C2`** | **DEP-EXE**, com parecer de DEP-GOV | Item **I** do ato. **Ainda NAO exercido** |
| **Verifica a eficacia da aplicacao** | **DEP-QAR** | FND-10 §10.5; `IR-09` |

---

## 1. Ancora do ato — o texto assinado, por hash

> **O ato foi emitido sobre um texto identificado, nao sobre uma referencia.** Se o arquivo mudar,
> o `H-A` abaixo deixa de reproduzir — e o ato **nao alcanca o texto novo**.

| Campo | Valor |
|---|---|
| **Objeto assinado** | [`PS-2026-015`](../../governance/pacote-soberano-2026-07-31-emendas-de-instrumento.md) — **minuta RECORTADA de §6.1**, linhas **201–415** |
| **Versao** | **1.2.0** — a que corrige `CA-2` |
| Caminho | `governance/pacote-soberano-2026-07-31-emendas-de-instrumento.md` |
| **`H-A` do texto assinado** | `3d242ed8470b3808a9b574373a0e4f6b5d37d09d31d5973dc39867d6feeaca62` |
| Como reproduzir | `sh ferramentas/hashes.sh ha governance/pacote-soberano-2026-07-31-emendas-de-instrumento.md` |
| **Variante NAO assinada** | §6 — minuta **integral**, das tres emendas. **As duas nao se somam, e foi a de §6.1 que se assinou** |

## 2. Decisao soberana — literal

**ATO SOBERANO — EMENDAS E1 E E3**

**Eu, Fundador e Soberano do LucaX Enterprise OS, emito o presente ato sobre a minuta recortada de
PS-2026-015, versao 1.2.0, em `governance/pacote-soberano-2026-07-31-emendas-de-instrumento.md`,
linhas 201-415.**

**I — `Q2` de `PS-2026-014 §7`: [X] EMENDAR `ADR-0007` AGORA.** Autorizo DEP-EXE a aprovar
`ADR-0027` no rito `C2`, com parecer de DEP-GOV, aplicando `O4` somente em `status`, conferindo o
`H-P` declarado em §6.1.1. Ratificacao permanece `nao-exigida`.

**II — `ADR-0029`, caminho de superacao de ato: [X] RATIFICO.** Aplica-se `O4` em `status` e
`ratificacao`, conferindo o `H-P` declarado em §6.1.1. Cria-se o registro de atos superados
exigido por `SA-6`, com contador em `0`. Declaro ciencia de que reverter uma superacao consumada
e impossivel — `RA-1` de `FIT-2026-022`, irreversibilidade certa e nao mitigavel.

**III — `E2` ADIADA, e nao rejeitada, nos termos de §6.1.2.**

**Os demais termos da minuta 1.2.0 ficam integralmente mantidos:** declaracao de independencia
**(IV)**, limites **(V)**, condicoes de eficacia com **`CA-2` informativo (VI)** e materia nao
assinalada como nao decidida **(VII)**.

**Fundador e Soberano — LucaX Enterprise OS · 2026-07-31**

> **`Q2` esta RESPONDIDA, e a resposta e a primeira metade do item I.** A autorizacao a DEP-EXE e
> a segunda, e **so pode ser exercida depois** — nunca antes, porque aprovar antes seria decidir
> pelo Soberano a questao que lhe fora submetida (`FIT-2026-020 §5`).

## 3. Objetos que o ato alcanca — **6**, com o `H-A` de cada um

**Lidos de [`PS-2026-015 §6.1.1`](../../governance/pacote-soberano-2026-07-31-emendas-de-instrumento.md)
e reconferidos no arquivo vivo nesta emissao: 6 de 6.**

| # | Objeto | Emenda | Versao | `H-A` |
|---|---|---|---|---|
| 1 | **`RFC-0022`** | `E1` | 1.0.0 | `29f03a012bcd6754cd32303ee98fe31d8f453b9280b0c532d004f9ee9c557894` |
| 2 | **`ADR-0027`** | `E1` | 1.0.0 | `d1e5f6f461ba58fd1a4b76e19e3e7714d3551bf00176d663a9bb6e2702dac5e3` |
| 3 | **`FIT-2026-020`** | `E1` | 1.0.0 | `281a775088043cee529ea6fce354f6b23e3eed6affdfa3548f650b4f6ed2d06e` |
| 4 | **`RFC-0024`** | `E3` | 1.0.0 | `acf364445c01b6238c2693220b6b3b0a99bab0060a2ae271d6f016acb448bbbe` |
| 5 | **`ADR-0029`** | `E3` | 1.0.0 | `dc2aa539afd249e15c9a13893ed9c2807ddad7b4388b12e12c1d0ea49c399327` |
| 6 | **`FIT-2026-022`** | `E3` | 1.0.0 | `89ed04ac21f2ab51ec836247dec1f0469f581cb5f26d78ef7ee0be26f0ec7080` |

**Os 3 que o ato EXCLUI — `E2`, ADIADA e nao rejeitada:**

| Objeto | `H-A` | Estado em que permanece |
|---|---|---|
| **`RFC-0023`** | `f842cdd430ece57fd85d39bcd3f8df5dd7b29047c7dfea3bbce40d31e2623c49` | `aprovado` |
| **`ADR-0028`** | `56b1fe80835cdd4f3c3a64fdc60dcef7a334ccd233ede7f698df915d646149c0` | `em-revisao` · `ratificacao: pendente` |
| **`FIT-2026-021`** | `caef6f7550a344439ce22d7a29bcaa4f04162e3752968386ef33740d43b369d3` | `ativo` · parecer `apto-com-ressalva` |

> **Adiar nao toca.** Os tres seguem **submetidos e intactos**, e **assinar este ato NAO decidiu
> `E2` em nenhum sentido** — nem aprovacao tacita, nem recusa tacita (`GV-05`, `LM-03`).

## 4. `H-P` — somente os DOIS que sofrerao `O4`

**Lidos do proprio arquivo, jamais de transcricao**, e **recalculados** sobre os objetos vivos
nesta emissao — **2 de 2 reproduzem**.

| Objeto | `O4` autorizado pelo ato | `H-P` *(apos `O4`)* | Reproduz hoje? |
|---|---|---|---|
| **`ADR-0027`** | **somente `status`** — `em-revisao` → `ativo`. **`ratificacao` permanece `nao-exigida`** | `523e0c816ea51e986568f0a04ce491d25f20622c667e4431553ffc1270e03a99` | ✅ |
| **`ADR-0029`** | **`status` E `ratificacao`** — `em-revisao` → `ativo`, `pendente` → `ratificada` | `148d61005948352b606b079cef40344a54e916e3ce64c410c683d85628379f72` | ✅ |
| `RFC-0022` · `RFC-0024` | **nenhum** — `RFC` termina em `aprovado` | **nao se publica** | — |
| `FIT-2026-020` · `FIT-2026-022` | **nenhum** — parecer nasce `ativo` · `nao-exigida` | **nao se publica** | — |

> **O `O4` esta DETERMINADO, nao inferido:** o `H-P` publicado **e** a regra para estes dois, e a
> reproducao acima prova que a transicao declarada e a unica que o alcanca a partir do estado
> atual. **`atualizado_em` NAO e tocado em nenhum dos dois.**

## 5. O que este REGISTRO nao fez — a fronteira entre emitir e aplicar

| # | Estado, medido nesta emissao | Valor |
|---|---|---|
| 1 | `ADR-0027` | segue **`em-revisao`** · `ratificacao: nao-exigida` — **`0` bytes** |
| 2 | `ADR-0029` | segue **`em-revisao`** · `ratificacao: pendente` — **`0` bytes** |
| 3 | Aprovacao de DEP-EXE sobre `ADR-0027` | **NAO emitida** |
| 4 | Registro de atos superados (`SA-6`) | **NAO criado.** Quando nascer, nasce com o contador em **`0`** |
| 5 | Atos superados | **`0`** |
| 6 | `PS-2026-015` | **`0` bytes** — a ancora de §1 continua reproduzindo |
| 7 | Os **9** objetos das tres emendas | **`0` bytes** — `9` de `9` `H-A` reproduzem |
| 8 | `products/`, Produtos, `Spec`s | **inexistente**, **`0`**, **`0`** |

> **Emitir e aplicar sao dois atos de naturezas diferentes, e o Fundador os separou
> expressamente.** Registrar o ato **nao o consome**: o consumo e a missao ministerial de §8, e
> **so ela** pode mover `status` e `ratificacao`.

## 6. Condicoes de eficacia que a aplicacao observara

**Anteriores — [`PS-2026-015 §6.1.4`](../../governance/pacote-soberano-2026-07-31-emendas-de-instrumento.md):**

| # | Condicao | Regime |
|---|---|---|
| `CA-1` | `H-A` dos **6** objetos alcancados confere | **BLOQUEANTE** |
| `CA-2` | Baseline vigente **registrada** no instante da aplicacao | **INFORMATIVO** — nao para nada (§6.1.4.1 da minuta) |
| `CA-3` | Lease vivo com fencing maior que o vigente | **BLOQUEANTE** |
| `CA-4` | Copia datada anterior a aplicacao | **BLOQUEANTE** |
| `CA-5` | Os **3** objetos de `E2` intactos | **BLOQUEANTE** |

> **A ancora do ato e por objeto consumido: `9` `sha256`** — `6` de `CA-1` mais `3` de `CA-5` —,
> **nunca a arvore inteira.** O item `VI` do ato mantem isso integralmente.

**Posteriores — `CP-1` a `CP-7` de §6.1.7**, com **`IR-09` executado por DEP-QAR**. Falha em
condicao **bloqueante** para a aplicacao e abre incidente por `IR-05`, na forma de cada linha.

## 7. Limites — o que este ato NAO faz

| # | Limite |
|---|---|
| **L1** | **Nao fecha `RD-33`**, que segue **bloqueante** |
| **L2** | **Nao admite Produto algum.** `products/` nao existe e continua nao existindo |
| **L3** | **Nao cria `Spec`** — **`0`**, e o Framework segue sem instancia |
| **L4** | **Nao julga candidato.** O medAlly nao e mencionado como candidato neste ato |
| **L5** | **NAO reclassifica o `REWRITE` da Missao 1.13.4.** `RC-1` a `RC-5` de `ADR-0027` **nao sao autoexecutaveis**, e a reclassificacao ocorre em **missao ministerial posterior**, apos `ADR-0027` em vigor |
| **L6** | **Nao resolve `Q1`**, que continua **bloqueante e intacta** |
| **L7** | **Nao decide `E2`, em nenhum sentido** |
| **L8** | **Nao toca o pacote da 1.13.4** — `PS-2026-014`, `PT-2026-011`, `FIT-2026-019`, `ADR-0026` e `RFC-0021`, **`0` bytes** |
| **L9** | **Nao emenda fundacional algum.** `E1` e `E3` alcancam **`0`** `FND` |
| **L10** | **Nao fecha achado algum por inferencia.** `RD-66` e `RD-67` seguem **ABERTOS, com dono e gatilho, e sem missao designada** |

## 8. A missao ministerial que consome este ato — **uma so**

Determinada pelo Fundador na mesma sessao, e registrada aqui para que a fonte permaneca
percorrivel:

| Etapa | O que faz |
|---|---|
| **1** | **Aplicar `E1` e `E3`** — `O4` em `ADR-0029` *(`status` e `ratificacao`)* e em `ADR-0027` *(somente `status`, apos a aprovacao de DEP-EXE)*, conferindo os `H-P` de §4 |
| **2** | **Verificar por `IR-09`** — reconstrucao reproduzindo `H-A`, executada por **DEP-QAR** |
| **3** | **Reconciliar catalogo e indices NA MESMA MUDANCA** — `CV-04`; projecao acompanha a fonte, nunca a precede |
| **4** | **Emitir nova baseline** — `BL-02`, medida **depois** da ultima escrita |

> **Nada alem disso.** **Congelamento em vigor, declarado pelo Fundador:** nenhuma missao de
> governanca nova nas duas trilhas ate existir a **primeira `Spec`**. Achado novo e **registrado
> com dono e gatilho e fica aberto**. **Excecao unica:** a missao de politica do `SSC+`.

**Depois da aplicacao de `E1`**, a sequencia declarada e: marco zero do medAlly → **1.13.4
rejulgada com a classe `RECOGNIZE`** → admissao → **`RD-33` destravado** → **1.13.5, a primeira
`Spec`, escrita contra o medAlly vivo** — nunca contra o candidato congelado.

## 9. Nao edicao das fontes anteriores

**Nenhum `MSG`, `FIT`, `PS`, `PT`, `ADR`, `RFC` ou baseline historica foi editado por este
registro** — `LV-04`, `BL-02`. O registro **cria** um artefato e **projeta** a criacao no
catalogo e nos indices, como `RG-02` e `CV-04` exigem; **nao toca nenhuma fonte normativa** e
**nao toca o texto assinado**, cuja integridade e a propria ancora de §1.

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-31 | SOBERANO | Registro do **oitavo ato soberano**, e o **primeiro do acervo registrado ANTES da aplicacao**, por instrucao expressa do Fundador. Responde **`Q2` emendando `ADR-0007` agora**, autoriza **DEP-EXE** a aprovar **`ADR-0027`** no rito `C2` com `O4` **somente em `status`**, **ratifica `ADR-0029`** com `O4` em `status` **e** `ratificacao`, e **adia `E2`** sem rejeita-la. **Ancorado no `H-A` da minuta 1.2.0** — `3d242ed8…ca62` —, com os **6** objetos alcancados, os **3** excluidos e os **2** `H-P` **lidos do arquivo e reconferidos: 2 de 2**. **`0` transicoes aplicadas, `0` aprovacoes de DEP-EXE, `0` registros de `SA-6`, `0` bytes em `PS-2026-015` e nos nove objetos.** `Q1` e `RD-33` seguem bloqueantes; `RD-66` e `RD-67` seguem abertos e sem missao. |
