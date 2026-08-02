---
id: PS-2026-015
titulo: Pacote soberano das tres emendas de instrumento — portao de origem externa, independencia de verificacao e superacao de ato
tipo: pacote-soberano
versao: 1.2.0
status: ativo
camada_memoria: operacional
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-07-31
atualizado_em: 2026-07-31
revisao_prevista: null
decisoes_relacionadas: [ADR-0005, ADR-0007, ADR-0012, ADR-0027, ADR-0028, ADR-0029]
substitui: []
substituido_por: null
resumo: Submete ao Soberano tres emendas de instrumento independentes entre si, com dependencia medida em zero, hashes por objeto e duas variantes de minuta nao emitida, sendo a submetida a recortada a E1 e E3.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# PS-2026-015 — as tres emendas de instrumento

> **Nenhum ato foi emitido. Nada foi aplicado, ativado ou ratificado.** Os **nove** objetos
> deste pacote existem no acervo em estado **nao vigente**, e as minutas de §6 e §6.1 sao
> **texto submetido**, nunca ato.
>
> **A variante SUBMETIDA e a de §6.1** — recortada a **`E1`** e **`E3`**, por despacho do
> Fundador. **`E2` fica ADIADA e nao rejeitada** (§6.1.2). §6 permanece como variante
> integral, alternativa. **As duas nao se somam: assina-se uma.**
>
> **Nao toca o medAlly, o nXtrack nem Produto algum. `0` candidatos julgados. `Q1` e `RD-33`
> continuam bloqueantes e intactos.**

## Proposito

Submeter ao Soberano tres emendas que corrigem **instrumentos do proprio acervo** e **nao
dependem de candidato nenhum** — e, por isso, nao dependem do bloqueio de proveniencia que
fechou a Missao 1.13.4.1 em `BLOCKED`.

## 1. Por que este pacote existe separado

A Missao 1.13.4.1 fechou **`BLOCKED`** porque **5 de 19** caminhos do repositorio do medAlly
sao **NAO ATRIBUIVEL** — nenhuma mudanca da janela foi commitada, e sem commit nao existe
registro de autoria.

**Aquele defeito e do candidato.** As tres emendas corrigem `ADR-0007`, `FND-10` e uma lacuna
de omissao sobre atos — **`0` delas le, mede ou depende do repositorio do medAlly**. Mante-las
presas ao `BLOCKED` seria acoplar por proximidade de missao, nao por dependencia.

## 2. Matriz dos objetos — `H-A` · `H-N` · `H-P`

| # | Objeto | Estado | Linhas | Bytes | `H-A` | `H-N` |
|---|---|---|---|---|---|---|
| `O-1` | **`RFC-0022`** | `aprovado` | 174 | 9.725 | `29f03a012bcd6754cd32303ee98fe31d8f453b9280b0c532d004f9ee9c557894` | `f3ed416e2bfe2b1b65d02b0363ee4192856b7f6867d767804ed8d05a2249af1e` |
| `O-2` | **`ADR-0027`** | `em-revisao` | 311 | 21.626 | `d1e5f6f461ba58fd1a4b76e19e3e7714d3551bf00176d663a9bb6e2702dac5e3` | `7e2db20747b64d27545047081345dc2d9f2b0615c15541dd22f3517f87afba9e` |
| `O-3` | **`FIT-2026-020`** | `ativo` | 133 | 8.324 | `281a775088043cee529ea6fce354f6b23e3eed6affdfa3548f650b4f6ed2d06e` | `2f05dd1c3f29dc5499bc49a08ab5329c47c68f19f2cdd51524f076c351e528a8` |
| `O-4` | **`RFC-0023`** | `aprovado` | 180 | 9.766 | `f842cdd430ece57fd85d39bcd3f8df5dd7b29047c7dfea3bbce40d31e2623c49` | `356449f4b54df3f5c1c6012196d2516f47a2f480be50080b9aab012095451fd2` |
| `O-5` | **`ADR-0028`** | `em-revisao` · `pendente` | 291 | 18.912 | `56b1fe80835cdd4f3c3a64fdc60dcef7a334ccd233ede7f698df915d646149c0` | `72762ec17c2ced02732d59dee451b0edeb61953345b849ce5a2fb26fdbad51a0` |
| `O-6` | **`FIT-2026-021`** | `ativo` | 142 | 9.061 | `caef6f7550a344439ce22d7a29bcaa4f04162e3752968386ef33740d43b369d3` | `804676fcec2fd04175d2c621c8bb478d323f306cc11019d356a803d15eee9599` |
| `O-7` | **`RFC-0024`** | `aprovado` | 168 | 8.708 | `acf364445c01b6238c2693220b6b3b0a99bab0060a2ae271d6f016acb448bbbe` | `c56dc898ec04b9a567f685f077b764e8bb64a7978ca91898959e3aba40726610` |
| `O-8` | **`ADR-0029`** | `em-revisao` · `pendente` | 260 | 17.654 | `dc2aa539afd249e15c9a13893ed9c2807ddad7b4388b12e12c1d0ea49c399327` | `c3ff590d6944c3ceeebf2f51074af712e28e3a70092935a521347420c474e1b0` |
| `O-9` | **`FIT-2026-022`** | `ativo` | 134 | 8.322 | `89ed04ac21f2ab51ec836247dec1f0469f581cb5f26d78ef7ee0be26f0ec7080` | `3613c495607f0bef0c5c5bf3a3ac7d1b90a010f2558cd2a00c6fd5bec5e306b1` |

### 2.1 `H-P` — publicado **somente** onde ha `O4`

**Tres** dos nove objetos sofrem `O4`. Publicar `H-P` para os outros seis seria publicar uma
transicao que **nunca ocorrera**.

| Objeto | `O4` alcanca | `H-P` *(apos `O4`)* |
|---|---|---|
| **`ADR-0027`** | **so `status`** — `ratificacao` e `nao-exigida` e **nao vira `ratificada`** | `523e0c816ea51e986568f0a04ce491d25f20622c667e4431553ffc1270e03a99` |
| **`ADR-0028`** | `status` **e** `ratificacao` | `47523084ab87510acb5b44e9301ecad6ab03b380a54fd4ed8d48bc1c85957fdb` |
| **`ADR-0029`** | `status` **e** `ratificacao` | `148d61005948352b606b079cef40344a54e916e3ce64c410c683d85628379f72` |
| `RFC-0022` · `RFC-0023` · `RFC-0024` | **nenhum** — `RFC` termina em `aprovado`; `FND-09 §8.2` linha `RFC`: **ratifica `—`** | **nao se publica** |
| `FIT-2026-020` · `021` · `022` | **nenhum** — parecer nasce `ativo`, `ratificacao: nao-exigida` (`FT-10`) | **nao se publica** |

### 2.2 As tres provas de integridade — **3 de 3 em cada uma**

| # | Prova | Resultado |
|---|---|---|
| **`P1`** | **`H-N` invariante sob `O4`** (`IR-02`) | ✅ **3 de 3** — `H-N` do candidato e do pos-transicao **identicos** nos tres ADR |
| **`P2`** | **`IR-09` — reconstrucao reproduz `H-A`** | ✅ **3 de 3.** Revertendo **apenas** `status` e `ratificacao`, o `sha256` volta a `d1e5f6f4…c5e3`, `56b1fe80…49c0` e `dc2aa539…9327` |
| **`P3`** | **`O4` alcanca exatamente os campos declarados** | ✅ `ADR-0027`: **`−5` bytes**, **1** campo, `2` linhas no diff. `ADR-0028` e `ADR-0029`: **`−3` bytes**, **2** campos, `4` linhas. **`atualizado_em` NAO e tocado em nenhum** — `0` ocorrencias no diff |

> **`IR-10` aplicado e declarado.** Os nove objetos **nao tem `H-A` registrado por ato
> anterior**, porque **nascem nesta missao**. Este e o **primeiro vinculo** de todos, e a
> inexistencia de alteracao anterior e provada por via independente: **nenhum deles existe** na
> copia datada `_backups/LucaX-Enterprise-OS_2026-07-31_pre-missao-1-13-4-2/`, tomada **antes**
> da primeira escrita. **A ausencia e declarada, nunca suprida por presuncao** (`PI-10`,
> `LV-12`).

## 3. Mapa de dependencias — **medido, e o resultado e zero**

> **A determinacao pediu que o acoplamento so existisse onde houvesse dependencia provada.
> Nao ha nenhuma.**

### 3.1 As quatro medicoes

| # | Medicao | Resultado |
|---|---|---|
| `D1` | **Referencias cruzadas** entre `ADR-0027`, `ADR-0028` e `ADR-0029` | **`0` de 6 pares.** Nenhum cita nenhum |
| `D2` | **Normas alcancadas** — os conjuntos se tocam? | **Disjuntos.** `E1` → `ADR-0007 §5.3`/`§5.4`; `E2` → `FND-10 §2.2`/`§2.5`; `E3` → **nenhuma** *(lacuna de omissao)* |
| `D3` | **Arquivos que cada emenda alteraria no ato** | `E1` = **`{}`** *(supera por instrumento novo)* · `E2` = **`{foundation/10-artifact-framework.md}`** · `E3` = **`{}`**. **Todas as intersecoes vazias** |
| `D4` | **`AV-3` de `E2` alcanca os objetos de `E1` e `E3`?** | **Nao — `0` ocorrencias** de `fornecedor_verificacao` em `ADR-0027`, `ADR-0029`, `RFC-0022` e `RFC-0024`. `AV-6` e **prospectiva**: alcanca o criado **a partir da vigencia** |

### 3.2 As tres relacoes que PARECEM dependencia e nao sao

| Par | Aparencia | Por que **nao** e dependencia |
|---|---|---|
| `E2` → `E1` e `E3` | *"Se `E2` vigorar, os ADR de `E1` e `E3` precisariam declarar `fornecedor_verificacao`"* | **`AV-6` e prospectiva** e `AC-08` define *"emendado"* como incremento **MAIOR ou MENOR**. Os objetos de `E1` e `E3` ja existirao em `1.0.0`; **so seriam alcancados numa emenda futura deles proprios** |
| `E3` → `E2` | *"`SA-2` exige prova, e `E2` muda o que conta como verificacao"* | `SA-2` exige **prova por caminho e `sha256`** — evidencia material. **Nao invoca `AV-1` nem depende de quem verificou** |
| `E1` → `E3` | *"`RC-1` reclassifica um registro de um pacote submetido; superar ato seria o caminho"* | **`RC-1` nao supera ato algum.** `PS-2026-014` **nao e ato** — e pacote **submetido e nao consumido**. `RC-2` preserva os cinco artefatos com `0` bytes, e `RC-4` declara que nao ha revalidacao |

### 3.3 Consequencia — **tres unidades atomicas, nao uma**

| Unidade | Objetos | Falha isolada derruba as outras? |
|---|---|---|
| **`U1`** | `RFC-0022` · `ADR-0027` · `FIT-2026-020` | **Nao** |
| **`U2`** | `RFC-0023` · `ADR-0028` · `FIT-2026-021` | **Nao** |
| **`U3`** | `RFC-0024` · `ADR-0029` · `FIT-2026-022` | **Nao** |

> **O Soberano pode aprovar uma, duas ou as tres, em qualquer ordem, sem que nenhuma perca
> sentido.** Acoplar as tres num conjunto atomico **faria a falha de uma reverter as outras**,
> e **nao ha dependencia que justifique esse custo** — `D1` a `D4`.
>
> **Ordem entre elas: indiferente.** Nenhuma escreve arquivo que outra leia.

## 4. Rollback por objeto

| Objeto | Como reverter | Custo | O que **nao** se reverte |
|---|---|---|---|
| `RFC-0022` · `RFC-0023` · `RFC-0024` | `O8` — `arquivado` | Trivial. `RFC` nunca vigorou como norma | — |
| **`ADR-0027`** | `O9` — `ADR` de retirada | **1** `ADR` + **1** entrada de catalogo + indices `M3`. **`0`** historicos, **`0`** fundacionais | **Nada** enquanto **`0`** admissoes `RECOGNIZE` existirem |
| **`ADR-0028`** | `O9` + `FND-10` por versao **MENOR** | **Alto:** exige **segundo ato soberano** *(emendar fundacional)*; alcanca **todo artefato criado sob a vigencia** | **As evidencias de integridade publicadas sob `AV-5`** — sao `BL-02`, nao editaveis |
| **`ADR-0029`** | `O9` — `ADR` de retirada | **1** `ADR` + indices; o registro de `SA-6` vira historico *(preservado, `FND-04 §7.2`)* | **Toda superacao ja consumida — IMPOSSIVEL.** É a razao de `Tipo 1` |
| `FIT-2026-020` · `021` · `022` | **Nao se revertem** — parecer e historico (`FND-09 §8.2` linha `FIT`) | — | — |
| **Ponto de rollback do acervo inteiro** | `H-A` de **195** artefatos, tomado **antes** da primeira escrita | `_missao-1-13-4-2-2026-07-31/evidencia/H-A-rollback-pre-escrita.txt`, `sha256` `96dfe8ff6b5150721090fe713532b0931ec9baf3ef9b1b3de58769817924caab` | — |

## 5. Classe, aprovador e o que cada emenda pede ao Soberano

| Emenda | Classe **determinada** | Aprovador da classe | O que o ato faria |
|---|---|---|---|
| **`E1`** — `G0` e `RECOGNIZE` | **`C2` · `Tipo 2`** | **DEP-EXE**, com parecer de DEP-GOV | **Nao e ratificacao — `C2`/`Tipo 2` nao a exige.** O que o Soberano decide e **`Q2`**, que ja esta na sua mesa: emendar `ADR-0007` agora, ou manter declarado. **Respondida `Q2`, a aprovacao e de DEP-EXE, no rito ordinario** |
| **`E2`** — independencia por fornecedor | **`C3` · `Tipo 1`** | **SOMENTE o SOBERANO** | **Ratificacao**, indelegavel. Sem ela, `ADR-0028` **nao entra em `ativo`** (`LM-02`) |
| **`E3`** — superacao de ato | **`C3` · `Tipo 1`** | **SOMENTE o SOBERANO** | **Ratificacao**, indelegavel. Um caminho que alcanca atos **so pode nascer de um ato** |

> **`E1` esta neste pacote por `Q2`, nao por classe.** Aprova-la por DEP-EXE **antes** da
> resposta do Soberano seria decidir por ele uma questao que ja lhe foi submetida — e este
> pacote **nao recomenda** essa antecipacao (`FIT-2026-020 §5`).

## 6. Minuta do ato soberano — variante INTEGRAL, redigida e NAO emitida

> **Variante mantida como alternativa.** A variante **SUBMETIDA** e a de **§6.1**, recortada a
> `E1` e `E3` por despacho do Fundador. **As duas nao se somam: assina-se uma.**

> **Texto submetido. Nao e ato, nao produz efeito, e nao esta assinado.** Vira ato quando — e
> **se** — o Soberano o emitir, explicita e datadamente, **sobre o texto final** (`CV-09`,
> `LM-03`, `LM-04`).

---

### ATO SOBERANO — EMENDAS DE INSTRUMENTO *(minuta)*

**Eu, Soberano do LucaX Enterprise OS, decido sobre as tres emendas de `PS-2026-015`,
INDEPENDENTEMENTE uma da outra, na forma abaixo.**

**I — `Q2` de `PS-2026-014 §7`, respondida.** [ ] Emendar `ADR-0007` agora · [ ] Manter
declarado.
Se emendar: **autorizo DEP-EXE a aprovar `ADR-0027`** no rito `C2`, com parecer de DEP-GOV,
aplicando `O4` **somente em `status`** — `em-revisao` → `ativo` —, conferindo `H-P`
`523e0c81…3a99`. **`ratificacao` permanece `nao-exigida`.**

**II — `ADR-0028`.** [ ] **Ratifico** · [ ] Recuso · [ ] Devolvo com ressalva.
Se ratifico: aplica-se `O4` em `status` **e** `ratificacao`, conferindo `H-P` `47523084…7fdb`;
e **`FND-10` recebe a emenda `MENOR` de `ADR-0028 §5.3`**, com a cascata dos templates
executada na mesma mudanca (`CV-04`, ressalva `RA-3` de `FIT-2026-021`).

**III — `ADR-0029`.** [ ] **Ratifico** · [ ] Recuso · [ ] Devolvo com ressalva.
Se ratifico: aplica-se `O4` em `status` **e** `ratificacao`, conferindo `H-P` `148d6100…8f72`;
e **cria-se o registro de atos superados** que `SA-6` exige, nascendo com o contador em **`0`**.

**IV — O que este ato NAO faz.**
1. **Nao julga candidato algum**, nao admite Produto, nao cria `Spec`.
2. **Nao toca o pacote da 1.13.4** — `PS-2026-014`, `PT-2026-011`, `FIT-2026-019`, `ADR-0026`
   e `RFC-0021` seguem **submetidos, suspensos e intactos**.
3. **Nao resolve `Q1`**, que continua **bloqueante**, nem fecha **`RD-33`**.
4. **Nao supera ato algum** — `SA-1` nasce com **`0`** atos superados.
5. **Nao invalida artefato algum** — `AV-6` e prospectiva, e `RC-3` preserva todo efeito
   registrado.
6. **Nao acopla as tres emendas.** Recusar uma **nao** afeta as outras: a dependencia entre
   elas foi **medida em `0`** — §3.

**V — Condicao de eficacia.** Cada item so produz efeito se **assinalado**. Item em branco e
**materia nao decidida**, jamais aprovacao tacita (`GV-05`, `LM-03`).

---

## 6.1 Minuta RECORTADA — somente `E1` e `E3` — **redigida e NAO emitida**

> **Esta e a variante SUBMETIDA.** §6 permanece como **variante integral**, mantida para o caso
> de o Fundador preferir decidir as tres de uma vez. **As duas nao se somam: assina-se uma.**
>
> **Por que recortar.** *"Recorte de ato e onde erro entra"* — e por isso o recorte esta
> **enumerado objeto a objeto**, com `H-A` de cada um, em vez de descrito por referencia.

### 6.1.1 Objetos alcancados — **6**, enumerados sem sobra

| # | Objeto | Versao | Caminho | Linhas | `H-A` | `H-N` |
|---|---|---|---|---|---|---|
| **`E1-a`** | `RFC-0022` | **1.0.0** | `rfcs/RFC-0022-classe-de-admissao-de-existencia-no-portao-de-origem-externa.md` | **174** | `29f03a012bcd6754cd32303ee98fe31d8f453b9280b0c532d004f9ee9c557894` | `f3ed416e2bfe2b1b65d02b0363ee4192856b7f6867d767804ed8d05a2249af1e` |
| **`E1-b`** | `ADR-0027` | **1.0.0** | `decisions/ADR-0027-classe-de-admissao-de-existencia-no-portao-de-origem-externa.md` | **311** | `d1e5f6f461ba58fd1a4b76e19e3e7714d3551bf00176d663a9bb6e2702dac5e3` | `7e2db20747b64d27545047081345dc2d9f2b0615c15541dd22f3517f87afba9e` |
| **`E1-c`** | `FIT-2026-020` | **1.0.0** | `governance/fitness/FIT-2026-020-emenda-do-portao-de-origem-externa.md` | **133** | `281a775088043cee529ea6fce354f6b23e3eed6affdfa3548f650b4f6ed2d06e` | `2f05dd1c3f29dc5499bc49a08ab5329c47c68f19f2cdd51524f076c351e528a8` |
| **`E3-a`** | `RFC-0024` | **1.0.0** | `rfcs/RFC-0024-superacao-de-ato-por-evidencia-posterior.md` | **168** | `acf364445c01b6238c2693220b6b3b0a99bab0060a2ae271d6f016acb448bbbe` | `c56dc898ec04b9a567f685f077b764e8bb64a7978ca91898959e3aba40726610` |
| **`E3-b`** | `ADR-0029` | **1.0.0** | `decisions/ADR-0029-superacao-de-ato-por-evidencia-posterior.md` | **260** | `dc2aa539afd249e15c9a13893ed9c2807ddad7b4388b12e12c1d0ea49c399327` | `c3ff590d6944c3ceeebf2f51074af712e28e3a70092935a521347420c474e1b0` |
| **`E3-c`** | `FIT-2026-022` | **1.0.0** | `governance/fitness/FIT-2026-022-superacao-de-ato-por-evidencia-posterior.md` | **134** | `89ed04ac21f2ab51ec836247dec1f0469f581cb5f26d78ef7ee0be26f0ec7080` | `3613c495607f0bef0c5c5bf3a3ac7d1b90a010f2558cd2a00c6fd5bec5e306b1` |

**`H-P` — somente nos DOIS que sofrem `O4`:**

| Objeto | `O4` alcanca | `H-P` *(apos `O4`)* |
|---|---|---|
| **`ADR-0027`** *(`E1-b`)* | **so `status`** — `em-revisao` → `ativo`. **`ratificacao` e `nao-exigida` e NAO vira `ratificada`** | `523e0c816ea51e986568f0a04ce491d25f20622c667e4431553ffc1270e03a99` |
| **`ADR-0029`** *(`E3-b`)* | **`status` E `ratificacao`** — `em-revisao` → `ativo`, `pendente` → `ratificada` | `148d61005948352b606b079cef40344a54e916e3ce64c410c683d85628379f72` |
| `RFC-0022` · `RFC-0024` | **nenhum** — `RFC` termina em `aprovado`; `FND-09 §8.2` linha `RFC`: **ratifica `—`** | **nao se publica** |
| `FIT-2026-020` · `FIT-2026-022` | **nenhum** — parecer nasce `ativo` · `nao-exigida` (`FT-10`) | **nao se publica** |

> **Publicar `H-P` dos quatro restantes seria publicar transicao que nunca ocorrera.** A
> ausencia e **declarada**, nao omitida.

### 6.1.2 `E2` fica FORA deste ato — **ADIADA, jamais rejeitada**

| Campo | Conteudo |
|---|---|
| **Objetos que ficam fora** | `RFC-0023` *(180 linhas, `H-A` `f842cdd430ece57fd85d39bcd3f8df5dd7b29047c7dfea3bbce40d31e2623c49`)* · `ADR-0028` *(291 linhas, `H-A` `56b1fe80835cdd4f3c3a64fdc60dcef7a334ccd233ede7f698df915d646149c0`)* · `FIT-2026-021` *(142 linhas, `H-A` `caef6f7550a344439ce22d7a29bcaa4f04162e3752968386ef33740d43b369d3`)* |
| **Estado em que permanecem** | **Exatamente o de hoje.** `ADR-0028` segue `em-revisao` · `ratificacao: pendente`; `RFC-0023` segue `aprovado`; `FIT-2026-021` segue `ativo`. **`0` bytes tocados** |
| **O motivo, escrito** | **A decisao de retroatividade sobre os `131 de 138` exige rito proprio.** `AV-6` propoe efeito **prospectivo**, e essa e uma escolha — nao um fato. Decidir que **131** verificacoes ja emitidas **permanecem validas sob criterio que a norma nova nao reconhece** e materia de merito sobre o acervo inteiro, nao consequencia tecnica da emenda. **Cabe-lhe rito proprio, com a pergunta feita ao Fundador em separado** |
| **O que ADIAR significa** | `E2` **nao e recusada, nao e arquivada e nao perde validade**. Os tres objetos continuam **submetidos**, e o parecer `FIT-2026-021` continua `apto-com-ressalva`. **Assinar este ato NAO decide `E2` em nenhum sentido** |
| **O que ADIAR NAO significa** | **Nao e aprovacao tacita nem recusa tacita.** `GV-05`: silencio nunca aprova. `LM-03`: instrucao generica anterior nao ratifica. **Materia nao assinalada e materia nao decidida** |
| **Onde `E2` volta** | Ato proprio, em missao posterior, com a questao de retroatividade **destacada e respondida item a item** — `Q8` de §8 |

### 6.1.3 `E1` e `E3` **nao dependem** de `E2` — dependencia **`0`**, medida por quatro vias

> **Nominalmente citadas, como o despacho exige.** As quatro medicoes estao em
> [§3.1](#31-as-quatro-medicoes) e sao reproduziveis.

| Via | O que mediu | Resultado para `E1` e `E3` contra `E2` |
|---|---|---|
| **`D1` — referencia cruzada** | `ADR-0027` e `ADR-0029` citam `ADR-0028`? | **`0`.** Nenhum dos dois o cita, em nenhum ponto |
| **`D2` — norma alcancada** | Os conjuntos de norma se tocam? | **Disjuntos.** `E1` → `ADR-0007 §5.3`/`§5.4`; `E3` → **nenhuma** *(lacuna de omissao)*; `E2` → `FND-10 §2.2`/`§2.5`. **Interseccao vazia** |
| **`D3` — intersecao de arquivos** | Que arquivo cada uma alteraria no ato? | `E1` = **`{}`** · `E3` = **`{}`** · `E2` = `{foundation/10-artifact-framework.md}`. **`E1 ∩ E2 = {}`** e **`E3 ∩ E2 = {}`** |
| **`D4` — alcance de `AV-3`** | O campo `fornecedor_verificacao` de `E2` alcanca os objetos de `E1` e `E3`? | **`0` ocorrencias** nos seis objetos deste ato. `AV-6` e **prospectiva**, e `AC-08` so alcanca artefato em incremento MAIOR ou MENOR — os seis nascem em `1.0.0` |

> **Consequencia:** adiar `E2` **nao retira fundamento, evidencia nem operabilidade** de `E1` ou
> `E3`. **Nenhum dos seis objetos deste ato le, invoca ou pressupoe `ADR-0028`.**

### 6.1.4 Condicoes ANTERIORES de eficacia — conferidas **antes** de escrever

| # | Condicao | Como se confere | Falha implica |
|---|---|---|---|
| `CA-1` | **`H-A` de cada um dos 6 confere** com §6.1.1 | `sh ferramentas/hashes.sh ha <arquivo>` | **PARAR.** Divergencia = objeto diferente do submetido |
| `CA-2` **INFORMATIVO** *(§6.1.4.1)* | **Registrar a baseline vigente no instante da aplicacao** — a que estiver publicada em `artifact-registry §10.0`, qualquer que seja | `sh ferramentas/baseline.sh <acervo>`; o trio medido entra no relatorio de transicao | **NAO PARA, e nao abre incidente.** Divergencia contra qualquer valor anterior e **esperada** num acervo vivo. A ancora deste ato e **por objeto consumido** — `CA-1` e `CA-5` —, nunca a arvore inteira |
| `CA-3` | **Lease vivo com fencing** maior que o vigente | `_leases/LucaX-Enterprise-OS.lease` | **PARAR.** Escritor obsoleto nao aplica ato |
| `CA-4` | **Copia datada anterior a aplicacao** | `PI-07`, `LV-01` | **PARAR.** Sem copia, nao se aplica |
| `CA-5` | **Os tres objetos de `E2` estao intactos** | `sha256` contra §6.1.2 | **PARAR.** `E2` esta fora e tem de sair sem um byte tocado |

#### 6.1.4.1 Por que `CA-2` e INFORMATIVO — o motivo, escrito

> **A condicao nasceu insatisfazivel POR CONSTRUCAO, nao por desvio de ninguem.** `CA-2` exigia
> que, no instante da aplicacao, o acervo estivesse em `BL-2026-07-31-03` — **206 · 60.151 ·
> `17a5ea41…986d`** — e **PARAR** se nao estivesse. **O pacote que publica essa condicao mora
> dentro do acervo que ela mede**, e por isso **qualquer emissao legitima a invalida**, inclusive
> a que escreveu a propria §6.1.

| # | O que se mediu | Resultado |
|---|---|---|
| 1 | O pacote **entra na medicao** que a condicao exige | `governance/pacote-soberano-2026-07-31-emendas-de-instrumento.md` esta na raiz `governance`, **dentro da lista fechada positiva** de `ferramentas/baseline.sh`. Editar este arquivo **muda o numero que este arquivo exige** |
| 2 | **Escrever a propria §6.1** ja movia o valor | `BL-2026-07-31-03` **206 · 60.151** → `BL-2026-07-31-04` **206 · 60.355** *(catalogo §10.13, evidencia de `BL-2026-07-31-04`)*. **`+204` linhas**, e `0` normas alteradas |
| 3 | O **registro de `RD-66` e `RD-67`** moveu outra vez | `BL-2026-07-31-05` = **206 · 60.390 · `1deded95…b597`** *(catalogo §10.14)* — **reproduzido pelo instrumento nesta emissao, no acervo e na copia datada** |
| 4 | Os **9** objetos, nas duas mudancas | **`0` bytes tocados.** **9 de 9** `H-A` reproduzem os publicados em §2, §6.1.1 e §6.1.2 — **medidos nesta emissao** |

> **Duas emissoes ministeriais que nao tocaram um byte dos nove objetos ja teriam PARADO a
> aplicacao** pela forma anterior de `CA-2`. Nao ha conduta que corrija isso: a condicao fica
> **mais falsa a cada registro legitimo**, e assinar sob ela seria prometer que **nada mais sera
> escrito no acervo** ate a aplicacao — o que um acervo vivo nao pode prometer.

**O que protege o texto assinado e `CA-1`**, e a protecao e **por objeto consumido**:

| Ancora | Cobre | Quantos `sha256` | Efeito da divergencia |
|---|---|---|---|
| **`CA-1`** | os **6** objetos **alcancados** pelo ato — §6.1.1 | **6** | **PARAR.** Objeto diferente do submetido |
| **`CA-5`** | os **3** objetos de `E2`, que tem de sair **intactos** — §6.1.2 | **3** | **PARAR.** O recorte falhou |
| **Total conferido no instante da aplicacao** | **os 9 objetos do pacote** | **9** | — |

> **Se um dos nove divergir, o ato PARA.** Se a arvore andar por trabalho que **nao toca nenhum
> deles**, **nada muda para este ato** — e foi exatamente o que ocorreu duas vezes. **Ancoragem
> por objeto consumido, nunca por arvore inteira.**

| O que a correcao **NAO** faz | Verificacao |
|---|---|
| **Nao afrouxa `CA-1`, `CA-3`, `CA-4` nem `CA-5`** | Os quatro seguem **bloqueantes**, com o texto original e **`0` bytes tocados** |
| **Nao dispensa medir a baseline** | Ela continua **medida e registrada** na aplicacao; deixa de ser **igualdade exigida** contra valor congelado |
| **Nao alcanca `CP-7`** | A baseline **posterior** continua **bloqueante para publicacao** — e ali a medicao e legitima: mede-se **depois** da ultima escrita, e exige-se **reproducao em duas execucoes**, nao igualdade com o passado |
| **Nao muda objeto, `H-A`, `H-P`, ordem, rollback nem limite** | §6.1.1 a §6.1.3 e §6.1.5 a §6.1.8 com **`0` bytes tocados** |

> **Precedente do acervo.** `RD-53` registrou o mesmo genero de defeito no lado do medidor —
> *"o defeito era do instrumento, nunca da baseline"* (`BL-2026-07-31-02`, catalogo §10.11). Um valor de **arvore
> inteira** como portao de ato herda a mesma fragilidade: reprova por causa que **nao e o objeto
> julgado**.
>
> **Equivalencia declarada pelo Fundador e NAO conferida por esta emissao:** e a **mesma correcao
> ja registrada para o lucaX** — ancora por objeto consumido, nunca por arvore inteira. Fica
> **declarada como despacho**, jamais como medicao desta missao (`PI-10`).

### 6.1.5 Ordem de aplicacao

| Etapa | Objeto | Operacao | Por que nesta posicao |
|---|---|---|---|
| **1** | **`ADR-0029`** *(`E3-b`)* | `O4` — `status` **e** `ratificacao` | **`C3`/`Tipo 1` primeiro**: e o que exige ratificacao indelegavel. Aplicar o de maior rito antes evita que uma parada no meio deixe vigente o menor sem o maior |
| **2** | **`ADR-0027`** *(`E1-b`)* | `O4` — **so `status`** | `C2`; **so pode ser aprovado por DEP-EXE apos o item I** deste ato responder `Q2` |
| **3** | `RFC-0022` · `RFC-0024` · `FIT-2026-020` · `FIT-2026-022` | **nenhuma** | **Nao transicionam.** Ja estao no estado final: `RFC` em `aprovado`, `FIT` em `ativo` |
| **4** | Indices `M3` e catalogo | atualizacao `CV-04` | Projecao acompanha a fonte, nunca a precede |
| **5** | Nova baseline | medicao | **`BL-02`**: a baseline se mede **depois** da ultima escrita |

> **A ordem entre `E1` e `E3` e INDIFERENTE — `D1` a `D4` provam.** A sequencia acima e de
> **operabilidade**, nao de dependencia: nenhum objeto le arquivo que o outro escreva. **Se a
> etapa 1 parar, a etapa 2 continua valida e vice-versa.**

### 6.1.6 Rollback por objeto

| Objeto | Como reverter | Custo medido | O que **nao** se reverte |
|---|---|---|---|
| `ADR-0027` | `O9` — `ADR` de retirada | **1** `ADR` + **1** entrada de catalogo `§7` + indices `M3` | **Nada**, enquanto **`0`** admissoes sob `RECOGNIZE` existirem |
| `ADR-0029` | `O9` — `ADR` de retirada | **1** `ADR` + indices; o registro de `SA-6` vira historico, **preservado** (`FND-04 §7.2` etapa 5) | **Toda superacao ja consumida — IMPOSSIVEL.** É a razao de `Tipo 1`. **Hoje: `0` superacoes** |
| `RFC-0022` · `RFC-0024` | `O8` — `arquivado` | Trivial; nunca vigoraram como norma | — |
| `FIT-2026-020` · `FIT-2026-022` | **Nao se revertem** — parecer e historico | — | — |
| **Reversao integral do ato** | Restaurar do ponto de partida | **`H-A` de 206 artefatos**, tomado antes da aplicacao | — |
| **Ponto de partida ja tomado** | `H-A` de **195** artefatos em `BL-2026-07-31-02`, `sha256` do proprio ponto `96dfe8ff6b5150721090fe713532b0931ec9baf3ef9b1b3de58769817924caab` | — | Cobre o estado **anterior a esta missao**; o ponto de **206** e tomado na aplicacao |

### 6.1.7 Condicoes POSTERIORES de eficacia

| # | Condicao | Como se confere | Falha implica |
|---|---|---|---|
| `CP-1` | **`H-P` confere** com §6.1.1 nos **dois** objetos que sofrem `O4` | `sh ferramentas/hashes.sh hp <arquivo>` | **`IR-05`** — incidente de conformidade |
| `CP-2` | **`H-N` invariante sob `O4`** | `IR-02` — `H-N` pos-transicao identico ao de §6.1.1 | **`IR-05`** |
| `CP-3` | **`IR-09` — reconstrucao reproduz `H-A`** | Revertendo **apenas** `status` e `ratificacao`, o `sha256` volta a `d1e5f6f4…c5e3` e `dc2aa539…9327`. **Executa DEP-QAR** | **`IR-05`**, incidente (`ADR-0012 §5.2`) |
| `CP-4` | **`O4` alcancou exatamente os campos declarados** | `ADR-0027` **`−5` bytes / 1 campo**; `ADR-0029` **`−3` bytes / 2 campos**. **`atualizado_em` NAO tocado** | **`IR-05`** |
| `CP-5` | **Os tres objetos de `E2` sairam intactos** | `sha256` contra §6.1.2 — **3 de 3** | **PARAR** e registrar: o recorte falhou |
| `CP-6` | **`0` bytes fora do conjunto autorizado** | `sha256` **arquivo a arquivo** contra a copia datada | **`IR-05`** |
| `CP-7` | **Nova baseline reproduzivel**, medida apos a ultima escrita | duas execucoes independentes, hash identico | Baseline nao publicavel |

### 6.1.8 Limites deste ato — o que ele **NAO** faz

| # | Nao faz | Fundamento |
|---|---|---|
| 1 | **Nao fecha `RD-33`** | Fora do escopo; segue **bloqueante** |
| 2 | **Nao admite Produto algum** | `products/` **nao existe** e continua nao existindo. **`0`** Produtos |
| 3 | **Nao cria `Spec`** | **`0`** `Spec`s, e o Framework segue sem instancia |
| 4 | **Nao julga candidato** | O medAlly **nao e mencionado como candidato** neste ato |
| 5 | **NAO reclassifica o `REWRITE` da Missao 1.13.4** | **`RC-1` a `RC-5` de `ADR-0027` nao sao autoexecutaveis.** `RC-5` e literal: enquanto `ADR-0027` nao estiver `ativo`, o registro le-se `REWRITE`. **E mesmo depois, a reclassificacao ocorre em MISSAO MINISTERIAL POSTERIOR** — nunca neste ato, e nunca por efeito automatico |
| 6 | **Nao resolve `Q1`** | `Q1` continua **bloqueante** e **intacta** |
| 7 | **Nao decide `E2`, em nenhum sentido** | §6.1.2 |
| 8 | **Nao toca o pacote da 1.13.4** | `PS-2026-014`, `PT-2026-011`, `FIT-2026-019`, `ADR-0026` e `RFC-0021` — **`0` bytes** |
| 9 | **Nao emenda fundacional algum** | `E1` e `E3` alcancam **`0`** `FND`. O unico diff sobre `FND-10` pertence a `E2`, que **fica fora** |

---

### ATO SOBERANO — EMENDAS `E1` E `E3` *(minuta recortada, NAO emitida)*

**Eu, Soberano do LucaX Enterprise OS, decido sobre DUAS das tres emendas de `PS-2026-015`,
INDEPENDENTEMENTE uma da outra. A terceira, `E2`, fica expressamente ADIADA.**

**I — `Q2` de `PS-2026-014 §7`, respondida.**
[ ] Emendar `ADR-0007` agora · [ ] Manter declarado.
Se emendar: **autorizo DEP-EXE a aprovar `ADR-0027`** no rito `C2`, com parecer de DEP-GOV,
aplicando `O4` **somente em `status`**, conferindo `H-P` `523e0c81…3a99`. **`ratificacao`
permanece `nao-exigida`** — `C2`/`Tipo 2` nao a exige, e este ato **nao a cria**.

**II — `ADR-0029` — caminho de superacao de ato.**
[ ] **Ratifico** · [ ] Recuso · [ ] Devolvo com ressalva.
Se ratifico: aplica-se `O4` em `status` **e** `ratificacao`, conferindo `H-P` `148d6100…8f72`;
e **cria-se o registro de atos superados** que `SA-6` exige, **nascendo com o contador em `0`**.
Declaro ciencia de que **reverter uma superacao consumada e impossivel** — `RA-1` de
`FIT-2026-022`, irreversibilidade **certa, nao mitigavel**.

**III — `E2` — independencia de verificacao por fornecedor.**
**ADIADA, e nao rejeitada.** `RFC-0023`, `ADR-0028` e `FIT-2026-021` permanecem **submetidos e
intactos**, com **`0` bytes tocados**. **O motivo e escrito:** a decisao sobre a retroatividade
que alcanca **131 de 138** artefatos exige **rito proprio**, e nao se resolve como consequencia
tecnica desta assinatura.

**IV — Declaracao de independencia.** Declaro que `E1` e `E3` **nao dependem de `E2`**, e que a
dependencia foi **medida em `0` por quatro vias nominalmente citadas** — `D1` referencia
cruzada, `D2` norma alcancada, `D3` intersecao de arquivos, `D4` alcance de `AV-3` — §6.1.3.

**V — Limites.** Este ato **nao fecha `RD-33`**, **nao admite Produto**, **nao cria `Spec`**,
**nao julga candidato**, **nao resolve `Q1`** e **NAO reclassifica o `REWRITE` gravado pela
Missao 1.13.4** — a reclassificacao de `RC-1` ocorre **somente em missao ministerial posterior**,
**apos `ADR-0027` estar em vigor**, e **jamais por efeito deste ato**.

**VI — Condicoes de eficacia.** A aplicacao observa `CA-1` a `CA-5` **antes** de escrever e
`CP-1` a `CP-7` **depois**, com **`IR-09` executado por DEP-QAR**. Falha em condicao
**BLOQUEANTE** — `CA-1`, `CA-3`, `CA-4` e `CA-5` antes; `CP-1` a `CP-7` depois — **para a
aplicacao** e abre incidente por `IR-05`, na forma de cada linha. **`CA-2` e INFORMATIVO e nao
para nada:** a baseline vigente e **medida e registrada**, jamais exigida como igualdade contra
valor congelado, porque **o pacote mora dentro do acervo que ela mede** e toda emissao legitima
a invalidaria. **A ancora deste ato sao os `9` `sha256` por objeto** — `6` alcancados em `CA-1`
e `3` de `E2` em `CA-5` —, **nunca a arvore inteira** (§6.1.4.1).

**VII — Materia nao assinalada e materia NAO DECIDIDA**, jamais aprovacao tacita (`GV-05`,
`LM-03`, `LM-04`).

---

## 7. Rastreabilidade — defeito → minuta → `ADR` → minuta de ato

| Defeito | Minuta *(evidencia)* | `RFC` | `ADR` | `FIT` | Item do ato |
|---|---|---|---|---|---|
| **`RD-54`** e **`RD-55`** — o portao nao distingue identidade de conteudo, e `G3` nao tem classe para admitir existencia | `MINUTA-A`, `sha256` `76eb1319…52d5` | [RFC-0022](../rfcs/RFC-0022-classe-de-admissao-de-existencia-no-portao-de-origem-externa.md) | [ADR-0027](../decisions/ADR-0027-classe-de-admissao-de-existencia-no-portao-de-origem-externa.md) | [FIT-2026-020](fitness/FIT-2026-020-emenda-do-portao-de-origem-externa.md) | **I** |
| **O detector de autoverificacao mede o campo errado** — `0` publicado onde a medicao por fornecedor da `131` | `MINUTA-B`, `sha256` `c1a04768…ff88` | [RFC-0023](../rfcs/RFC-0023-independencia-de-verificacao-por-fornecedor.md) | [ADR-0028](../decisions/ADR-0028-independencia-de-verificacao-por-fornecedor.md) | [FIT-2026-021](fitness/FIT-2026-021-independencia-de-verificacao-por-fornecedor.md) | **II** |
| **Ato emitido nao tem caminho de revisao quando a prova o contradiz** | `MINUTA-C`, `sha256` `b5cd82ae…e678a` | [RFC-0024](../rfcs/RFC-0024-superacao-de-ato-por-evidencia-posterior.md) | [ADR-0029](../decisions/ADR-0029-superacao-de-ato-por-evidencia-posterior.md) | [FIT-2026-022](fitness/FIT-2026-022-superacao-de-ato-por-evidencia-posterior.md) | **III** |

### 7.1 As tres correcoes que a cadeia produziu

**As minutas entraram como EVIDENCIA e foram conferidas contra a fonte. Tres afirmacoes delas
nao sobreviveram:**

| # | A minuta dizia | A fonte diz | Consequencia |
|---|---|---|---|
| 1 | `G3` tem `ADOPT · ADAPT · REWRITE · **REJECT**` | **`RETIRE`** — `ADR-0007 §5.3` e `§5.4`. `rejected` e valor de **proveniencia** | Corrigido em `RFC-0022 §1.1` e `ADR-0027 §5.2` |
| 2 | Reverter custa *"1 linha de `ADR-0007`"* | **Duas secoes**, e **nenhuma e editada** — `AL-02`, `LV-04` | Custo remedido em `ADR-0027 §10` |
| 3 | A emenda 2 supera **`ADR-0005`** *"quanto ao criterio de afericao"* | **`ADR-0005` nao contem criterio algum.** O criterio e **`AC-03` de `FND-10 §2.5`** | **A classe subiu de `C2` para `C3`** — `ADR-0028 §1.1` e `§11.1` |

> **A terceira e a que mais importa.** Herdar o objeto superado da minuta teria produzido
> **rito insuficiente**: emendar `ADR` e `C2`; emendar **fundacional** e `C3` com ratificacao
> do Soberano. **Missao `BLOCKED` nao confere autoridade ao que produziu** — e foi conferir que
> revelou isso.

## 8. Questoes ao Soberano

| # | Questao | Bloqueia? |
|---|---|---|
| **`Q1`** *(herdada, intacta)* | A decisao 7 fixou o nXtrack como primeiro produto **comercial** ou como primeiro Produto **do acervo**? | ✅ **SIM** — **para o pacote da 1.13.4**, e **nao** para este |
| `Q6` | **`Q2` de `PS-2026-014`**: emendar `ADR-0007` agora, ou manter declarado? | ❌ Nao |
| `Q7` | **`E1` deve esperar a resposta de `Q2`**, ou DEP-EXE pode aprova-la no rito ordinario desde ja? | ❌ Nao |
| `Q8` | **`E2` publica um numero desconfortavel** — `131` de `138`. Confirmar que **publicar e o proposito**, e nao efeito colateral? | ❌ Nao |
| `Q9` | **`E3` cria o direito de INSTAURAR** para qualquer departamento. Confirmar que instaurar **nao suspende** o ato, como `SA-4` propoe? | ❌ Nao |

> **`Q1` nao bloqueia este pacote**, e a razao esta medida: **`0`** dos nove objetos le, mede
> ou depende do repositorio do medAlly.

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.2.0 | 2026-07-31 | DEP-GOV | **Despacho do Fundador: correcao de `CA-2`, e somente dela, ANTES da assinatura.** `CA-2` de §6.1.4 passa de **bloqueante a INFORMATIVO**: a baseline vigente e **medida e registrada** na aplicacao, jamais exigida como igualdade contra valor congelado. **O motivo esta escrito no proprio texto**, em §6.1.4.1 — **o pacote mora dentro do acervo que a condicao mede**, logo **toda emissao legitima a invalida**, e a condicao e **insatisfazivel por construcao, nao por desvio**. Medido: escrever a propria §6.1 levou `BL-2026-07-31-03` *(206 · 60.151)* a `BL-2026-07-31-04` *(206 · 60.355)*, e o registro de `RD-66`/`RD-67` a **`BL-2026-07-31-05`** *(206 · 60.390 · `1deded95…b597`)*, **com `0` bytes nos nove objetos e `9` de `9` `H-A` reproduzindo**. **A protecao do texto assinado e `CA-1`** — **ancora por objeto consumido, nunca por arvore inteira**: `6` `sha256` de `CA-1` mais `3` de `CA-5` = **`9`**, conferidos **no instante da aplicacao**. O mesmo efeito bloqueante estava **duplicado no item `VI`** da minuta recortada e foi corrigido no mesmo ato, **sem o qual a correcao alcancaria so metade do guarda**. **`CA-1`, `CA-3`, `CA-4`, `CA-5` e `CP-1` a `CP-7` seguem bloqueantes com `0` bytes tocados**; objetos, `H-A`, `H-P`, ordem de aplicacao, rollback e os nove limites **inalterados**. **Nenhum ato emitido, aplicado, ativado ou ratificado**; `E2` segue **ADIADA**; `RD-66` e `RD-67` seguem **ABERTOS e sem missao designada**, sob o congelamento declarado pelo Fundador. |
| 1.1.0 | 2026-07-31 | DEP-GOV | **Despacho do Fundador: minuta de ato RECORTADA.** §6.1 acrescenta a variante **submetida**, restrita a **`E1`** *(`RFC-0022`, `ADR-0027`, `FIT-2026-020` — `C2`/`Tipo 2`)* e **`E3`** *(`RFC-0024`, `ADR-0029`, `FIT-2026-022` — `C3`/`Tipo 1`)*, com os **6** objetos enumerados por **ID, versao, caminho, linhas, `H-A` e `H-N`**, e **`H-P` somente nos DOIS que sofrem `O4`**. **`E2` fica FORA, ADIADA e nao rejeitada**, com o motivo escrito: a decisao de retroatividade sobre **131 de 138** exige rito proprio. **A independencia de `E1` e `E3` em relacao a `E2` esta declarada e medida em `0` por quatro vias nominalmente citadas** — `D1` a `D4`. Acrescenta **ordem de aplicacao**, **rollback por objeto**, **ponto de partida por `H-A`**, **condicoes anteriores `CA-1` a `CA-5`** e **posteriores `CP-1` a `CP-7`** com **`IR-09`**, e **nove limites** — entre eles que o ato **NAO reclassifica o `REWRITE` da 1.13.4**, que so ocorre em **missao ministerial posterior**, apos `E1` em vigor. §6 permanece como **variante integral**, rotulada como alternativa. **`0` bytes nos seis objetos, nos tres de `E2` e em norma alguma.** |
| 1.0.0 | 2026-07-31 | DEP-GOV | Pacote inicial da **Missao 1.13.4.2**. **Decimo primeiro pacote soberano.** Submete **nove** objetos em **tres unidades independentes**, com a dependencia entre elas **medida em `0`** por quatro criterios *(referencia cruzada, norma alcancada, intersecao de arquivos, alcance de `AV-3`)* — e por isso **sem conjunto atomico**. `H-A` e `H-N` dos nove; `H-P` **somente dos tres** que sofrem `O4`. **Provas `P1`, `P2` e `P3`: 3 de 3 em cada.** Minuta de ato em §6, **redigida e NAO emitida**, com decisao **item a item** e clausula de que item em branco e materia **nao decidida**. §7.1 registra as **tres** correcoes que a conferencia das minutas produziu — a terceira **elevou o rito da emenda 2 de `C2` para `C3`**. |
