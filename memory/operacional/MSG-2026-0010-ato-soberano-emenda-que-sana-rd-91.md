---
id: MSG-2026-0010
titulo: Ato Soberano da emenda C3 que sana RD-91, separando proponente de aprovador na Spec C1
tipo: relatorio
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: SOBERANO
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-08-02
atualizado_em: 2026-08-02
revisao_prevista: null
decisoes_relacionadas: [ADR-0017, ADR-0019, ADR-0021, ADR-0022, ADR-0031, ADR-0032]
substitui: []
substituido_por: null
canal: DIRETIVA
emissor: SOBERANO
destinatario: DEP-GOV
ttl: 1 ciclo — expira sem perda; o ato fica ancorado por hash e os efeitos duraveis serao promovidos na aplicacao
resumo: Registra, como fonte canonica unica, o DECIMO ato soberano — emitido sobre os itens I a VIII da minuta de PS-2026-017 1.3.0, linhas 571-655, e ancorado no H-A do pacote c48cf443 —, que ratifica ADR-0032, promulga FND-09 1.6.0, FND-11 1.1.0 e as Cartas DEP-PRD e DEP-EXE 1.2.0, e decide Q1, Q2 e Q3. NADA foi aplicado por este registro: os quatro objetos seguem intocados e a transicao O4 cabe a missao ministerial do item VI.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# MSG-2026-0010 — Ato Soberano de 2026-08-02 *(decimo ato)*

## Proposito

Gravar, como **fonte canonica unica**, o ato soberano que sana **`RD-91`** — a colisao que
punha o **proprietario** de uma `Spec` de classe `C1` propondo **e** aprovando o proprio
artefato, contra `FND-04 §3.1`, que declara **nula** a aprovacao com acumulo de papel
(`LV-03`, Linha Vermelha de nivel 1).

> ## Este registro NAO APLICA o ato. Registra que ele foi emitido.
>
> **`FND-09` permanece em `1.5.0`, `FND-11` em `1.0.0`, as Cartas de `DEP-PRD` e `DEP-EXE`
> em `1.1.0`** — conferido por `sha256` em §3, **depois** desta escrita. Os candidatos
> `1.6.0`, `1.1.0`, `1.2.0` e `1.2.0` continuam **fora do acervo**. A transicao `O4` cabe a
> **missao ministerial do item VI**, que vem em mensagem separada por determinacao expressa
> do proprio Soberano.

## Escopo

| Dentro | Fora |
|---|---|
| O texto do ato, literal | Mover `status` ou `ratificacao` de qualquer objeto |
| A ancora por hash do pacote assinado | Editar `FND-09`, `FND-11` ou as duas Cartas |
| Os quatro `H-P` que a aplicacao tera de reproduzir | Emitir baseline nova |
| A declaracao de ciencia e o que ela alcanca | Abrir a missao do item IV |
| Os limites — o que o ato **nao** faz | Reconciliar catalogo e baseline *(item VI)* |

## Responsaveis

| Papel | Quem |
|---|---|
| Emissor | **SOBERANO** |
| Destinatario | **DEP-GOV** |
| Executor da aplicacao | **DEP-GOV**, pelo item VI — **missao propria, ainda nao aberta** |
| Revisor deste registro | **DEP-QAR** |

## 1. Ancora do ato — o texto assinado, por hash

> **O ato foi emitido sobre um texto identificado, nao sobre uma referencia.** Se o arquivo
> mudar, o `H-A` abaixo deixa de reproduzir — e o ato **nao alcanca o texto novo**.

| Campo | Valor |
|---|---|
| **Objeto assinado** | [`PS-2026-017`](../../governance/pacote-soberano-2026-08-02-rd-91.md) — **itens I a VIII da minuta de §6** |
| **Versao** | **1.3.0** — a que traz §3.4, §9.3 e §10 |
| Caminho | `governance/pacote-soberano-2026-08-02-rd-91.md` |
| **`H-A` do pacote assinado** | **`c48cf44323e4327c7cff3db1c96128e509107e2ec7b21e4ad187978d620c0298`** |
| Como reproduzir | `sh ferramentas/hashes.sh ha governance/pacote-soberano-2026-08-02-rd-91.md` |
| **Recorte §6 inteira**, linhas `556`–`657` | `sha256` `2885f01557c3f5a0d429bab7f941c10c5c1e5e74919f9e9377ab6787941b3cd9` |
| **Recorte §6 sem a linha em branco final**, `556`–`656` | `sha256` `e9f4b459299773fa3ce31e35edefcb40c389f6838251882ee9f975f8e26a6ad8` |
| **Bloco `ATO SOBERANO` com as cercas**, `570`–`656` | `sha256` `2588c4dd644b131fb6e6359a6b8f1f8466b3612604b64343eceda827c65aa0b2` |
| **Bloco `ATO SOBERANO`, itens I a VIII**, `571`–`655` | **`sha256` `7c75ebefa59ff2e47d119cb5bb19ec248859ecd7d4bf23f97f02641a345b496e`** |

> **`AN-1` — a faixa foi CONFERIDA linha a linha, e a precisao esta escrita.** A linha
> **`556`** e `## 6. Minuta do ato soberano — **reemitida 1.1.0, e NAO emitida**`; a **`570`**
> e a cerca ```` ``` ```` de abertura; a **`571`** e `ATO SOBERANO — EMENDA QUE SANA RD-91`;
> a **`655`** e `     conflito.`, ultima linha do item VIII; a **`656`** e a cerca de
> fechamento; a **`657`** e **em branco**; e `## 7. Questoes ao Soberano` comeca em **`658`**.
> **O recorte assinado contem os oito itens inteiros e nao alcanca um unico byte de §7.**
> Os **quatro** `sha256` estao publicados porque ha quatro leituras defensaveis do que
> *"itens I a VIII"* recorta — **quem conferir por qualquer uma reproduz**.

> **`AN-2` — o `H-A` foi MEDIDO no arquivo, nunca lido da transcricao.** A medicao
> independente sobre `governance/pacote-soberano-2026-08-02-rd-91.md`, tomada **antes da
> primeira escrita** desta sessao, devolveu
> `c48cf44323e4327c7cff3db1c96128e509107e2ec7b21e4ad187978d620c0298`. A ordem importa:
> **medir e depois comparar**, nunca copiar e depois declarar conferido.

> **`AN-3` — o `mtime` do pacote andou depois do fechamento anterior, e o byte nao.**
> `pacote-soberano-2026-08-02-rd-91.md` teve `mtime` movido para `2026-08-02 13:38:23`,
> depois da liberacao do token 16 — e o `H-A` **reproduz nos 64 digitos** o valor de
> fechamento daquele token. **O mesmo ocorreu com `roadmap-canonico.md` (`13:35:57`).**
> **Conteudo inalterado, conferido tambem pelo acervo inteiro** contra a copia datada das
> `13:24`, que difere em **exatamente** os `4` arquivos ja declarados. **E por isto que a
> ancora e o hash e nunca a data:** `mtime` e afirmacao do sistema de arquivos, `sha256` e
> medicao do conteudo.

## 2. Decisao soberana — literal

**ATO SOBERANO — EMENDA QUE SANA `RD-91`**

**Eu, Soberano do LucaX Enterprise OS, tendo conferido as condicoes anteriores de eficacia
de `PS-2026-017`, versao 1.3.0, em `governance/pacote-soberano-2026-08-02-rd-91.md`, EMITO o
ato dos itens I a VIII da minuta ali redigida, integralmente e sem alteracao de termo,
incluindo as tres decisoes ja marcadas: `Q1` estendida a `PRJ` e `TPL` com missao propria
ordenada, `Q2` com `C0` permanecendo declarado em `RD-91`, e `Q3` pela pratica exercida,
incremento MENOR.**

**Declaro ciencia de que o ponto de retorno original foi destruido por
`_FAXINA-2-apagar.bat` e que o §4 aponta para o que sobrou, conforme `RD-103`; e de que
`RD-96`, `RD-97`, `RD-99`, `RD-100`, `RD-101`, `RD-102` e `RD-104` seguem abertos com dono e
gatilho.**

**Fundador e Soberano — LucaX Enterprise OS**

### 2.1 Os oito itens incorporados por referencia

O ato foi emitido **integralmente e sem alteracao de termo**. Os itens vivem em
[`PS-2026-017 §6`](../../governance/pacote-soberano-2026-08-02-rd-91.md), linhas `571`–`655`,
e sao aqui **resumidos sem os substituir** — em divergencia, **prevalece o pacote**.

| Item | O que decide |
|---|---|
| **I** | **RATIFICA `ADR-0032`** *(`C3` · Tipo 2)* e **promulga as quatro versoes**, que entram em vigor na data do ato: `FND-09` **1.6.0**, `FND-11` **1.1.0**, Cartas `DEP-PRD` e `DEP-EXE` **1.2.0** — cada uma com seu `H-P` esperado |
| **II** | **DECLARA** que a aprovacao de `Spec` `C1` passa a ser de **DEP-EXE**, e que isso **nao** altera a classe `C1`, **nao** cria titular e **nao** toca regra de conteudo de `Spec` |
| **III** | **DECLARA** que **`SPC-001` NAO e reclassificada**: nasceu `C2 · Tipo 2` validamente |
| **IV** | **`Q1` — LARGURA:** ☑ **estende a emenda a `PRJ` e `TPL`**, e **ordena missao propria** para redigi-la. Alcance: `FND-09 §8.2`, linhas `PRJ` (`RD-96`) e `TPL` (`RD-97`), e a cascata. **A missao REDIGE; nao aplica.** Este ato **nao** se estende com ela: os objetos do item I continuam **quatro** |
| **V** | **`Q2` — `C0`:** ☑ **permanece declarado em `RD-91`, sem emenda**. **`RD-91` FECHA PARCIALMENTE:** fecha quanto a `C1` e **permanece ABERTO quanto a `C0 · T2`** |
| **VI** | **A aplicacao e MINISTERIAL e cabe a DEP-GOV:** mover `status` e `ratificacao` dos quatro objetos, **reproduzir os quatro `H-P`**, atualizar o catalogo mestre e **emitir baseline nova**. **Se qualquer `H-P` nao reproduzir, a aplicacao PARA** |
| **VII** | **O congelamento permanece em vigor.** O ato gera **exatamente duas frentes, e nenhuma outra**: a aplicacao do item VI, e a missao do item IV — que **nao comeca antes** de concluida e conferida a aplicacao do item VI |
| **VIII** | **`Q3` — VERSAO:** ☑ **prevalece a PRATICA EXERCIDA, incremento MENOR** (`AL-01`/`CC-02`), e os numeros do item I ficam como estao. **Decide por deliberacao, e nao por omissao.** **Nao** resolve o conflito dentro de `FND-04` e **nao** emenda `FND-04`: **`0` bytes**. `RD-99` permanece **ABERTO** |

### 2.2 A declaracao de ciencia — o que ela acrescenta, medido

A declaracao **nao decide**; ela **fecha a porta do desconhecimento**. Alcanca duas coisas,
e as duas sao conferiveis:

| O que o Soberano declarou saber | Estado medido |
|---|---|
| O **ponto de retorno original foi destruido** por `_FAXINA-2-apagar.bat`, e o §4 aponta para o que sobrou, conforme **`RD-103`** | ✅ `_to_delete/` apagado com `rd /s /q`; **`0`** ocorrencias em `E:\LucasIA`. Manifesto `H-A-rollback-pre-escrita.txt` **reproduz** *(`602` linhas, `a44370df…4538`)*, **`0` de `602` ausentes**. Sede vigente do §4 **provada fiel** — reproduz os tres valores da baseline. `RD-103` registrado no catalogo, item **126**, severidade **Alta** |
| **`RD-96`, `RD-97`, `RD-99`, `RD-100`, `RD-101`, `RD-102` e `RD-104`** seguem **abertos com dono e gatilho** | ✅ **`7` nomeados.** Dos sete, **`6` estao inscritos** no catalogo §7 — `RD-96` a `RD-102` menos `RD-98`, que o Soberano **nao** nomeou por estar em outra familia. **`RD-104` e o unico dos sete NAO inscrito**: continua **declarado** em [`PS-2026-017 §4`](../../governance/pacote-soberano-2026-08-02-rd-91.md), e **a declaracao de ciencia nao o inscreve** — inscrever e ato de catalogo, e o Soberano nao o ordenou |

> **O que a declaracao de ciencia NAO faz.** Nao fecha achado, nao muda severidade, nao abre
> missao e **nao inscreve `RD-104`**. Ela impede uma coisa so, e e a que importa: **que
> alguem alegue depois que o ato foi emitido sem que o destroco do rollback e os sete
> achados abertos estivessem a vista.**

## 3. Objetos que o ato alcanca — **4**, com o `H-A` de cada um, medido APOS esta escrita

**Os quatro continuam INTOCADOS.** Medido **depois** de gravado este registro, e nao antes —
a ordem e o que prova que registrar nao aplicou.

| Objeto | Caminho | Versao **hoje** | `H-A` medido agora |
|---|---|---|---|
| **`FND-09`** | `foundation/09-meta-model.md` | **1.5.0** *(nao 1.6.0)* | `191ff367eead695b4a1c2622ea20dfb89d47c40bfe2d5945286bf99e7bbd1952` |
| **`FND-11`** | `foundation/11-framework-specifications.md` | **1.0.0** *(nao 1.1.0)* | `383ee51df8ee8782a693897f07423529bc4dd5a7d866603ad31e61fe06ad7c20` |
| **Carta `DEP-PRD`** | `departments/prd/carta.md` | **1.1.0** *(nao 1.2.0)* | `0e98511630faf9d5bec4c7cb36d8a37fa0bf15506dfde36954f0419e2720fc15` |
| **Carta `DEP-EXE`** | `departments/exe/carta.md` | **1.1.0** *(nao 1.2.0)* | `a75a1ffea140e1f962e97b5b8772df70cf28831df882a25cf804b4e931f17e12` |

**Os quatro candidatos vivem FORA do acervo**, em
`_candidatos-LucaX-Enterprise-OS-2026-08-02-M1.13.5.1/`, e **nao entram por este registro**.

## 4. `H-P` — o que a aplicacao tera de reproduzir, e de onde estes valores vieram

> **Determinacao expressa do Soberano:** *"lendo os `H-P` do proprio arquivo e jamais de
> transcricao"*. **Cumprida por parsing, de DUAS sedes independentes.**

| Objeto | `H-P` — o valor **depois** do `O4` |
|---|---|
| **`FND-09` 1.6.0** | `ea5efd35249c12f9587b7ded68a72d165a14b4adf399fdb2f9dc09dad395a8db` |
| **`FND-11` 1.1.0** | `b2cff9f59e9f0d47034f02322d32438552d122c867ae0e954bb30fc42cd16e08` |
| **Carta `DEP-PRD` 1.2.0** | `b9ac470c9227dd5bc4445d96faf1ff6b1d67c2d6f40ea6d0fd8a4f37180babdd` |
| **Carta `DEP-EXE` 1.2.0** | `a07c765a9134b3f4caad76b2750c38beff53b6f7f2e8659717c42c881c9619e4` |

### 4.1 Procedencia dos quatro valores — `8` de `8` conferem

| Fonte | Metodo | Resultado |
|---|---|---|
| **Item I do §6** do pacote *(o texto assinado)* | Extraidos por `grep` sobre o arquivo | **4** valores |
| **Tabela de §3.1** do pacote *(sede independente)* | Extraidos por `sed`+`grep` sobre o arquivo | **4** valores |
| **Medicao nova dos candidatos** | `sh hashes.sh hp <candidato>` | **4** valores |

**As duas sedes do arquivo concordam entre si e com a medicao nova: `4` × `2` = `8` de `8`.**
**`0` valores foram copiados de transcricao, relatorio ou historico** — nem do meu proprio
relatorio anterior. **Controle positivo exercido antes do uso:** `hashes.sh` rodou sobre si
proprio e devolveu o proprio `sha256` `729cafad…87ec`, de modo que um acerto aqui nao e
acerto de instrumento morto.

> ### ⚠️ O texto assinado contem uma nota SUPERADA, e ela fica declarada, nunca corrigida
>
> A nota ao fim do item I diz que os quatro `H-P` foram ***"RECONFERIDOS DUAS VEZES … em
> 2026-08-02 10:40 e de novo em 2026-08-02 11:41, esta segunda sobre a versao FINAL
> 1.2.0"***. **Quando o ato foi emitido, a versao final ja era a `1.3.0` e as reconferencias
> ja eram TRES** — a terceira em `2026-08-02 13:29`, registrada em §3.4 do pacote, tambem com
> `20` de `20`.
>
> **A nota foi subestimada pelos fatos, e nao contrariada por eles:** ela afirma *menos*
> reconferencias do que houve, e **os quatro valores que ela acompanha reproduzem** — agora
> pela quarta vez. **O ato foi emitido *"integralmente e sem alteracao de termo"*, e por isso
> o termo NAO foi tocado**: corrigir a nota seria alterar texto assinado, que este registro
> nao pode fazer. **Fica declarada aqui**, e nao emendada la — mesma familia de **`RD-101`**,
> *artefato que afirma propriedade que ja nao vale*, com a diferenca de que **esta e inocua
> quanto ao efeito**: o item VI manda reproduzir os `H-P`, nao contar reconferencias.

## 5. O que este REGISTRO nao fez — a fronteira entre emitir e aplicar

| Fronteira | Estado |
|---|---|
| `status` / `ratificacao` dos 4 objetos | **`0` movidos.** §3 mede depois desta escrita |
| Bytes em `FND-09`, `FND-11`, Cartas `DEP-PRD` e `DEP-EXE` | **`0`** |
| Bytes nos 4 candidatos fora do acervo | **`0`** |
| Bytes em `ADR-0032`, `RFC-0027`, `FIT-2026-025`, `PT-2026-018` | **`0`** |
| Bytes em `PS-2026-017` | **`0` — e e obrigatorio que seja `0`:** o ato esta ancorado no `H-A` dele. Tocar o pacote **quebraria a propria ancora** |
| Baselines emitidas | **`0`.** Emitir baseline nova e **do item VI**, nao deste registro |
| `RD-91` | **NAO fechado aqui.** Fecha **pelo ato**, e **parcialmente** — `C0 · T2` segue aberta. A inscricao do fechamento e da aplicacao |
| `RD-104` | **NAO inscrito.** A declaracao de ciencia o nomeia; nomear nao inscreve |
| Missao do item IV | **NAO aberta.** O item VII a proibe antes da aplicacao do item VI |
| Missao ministerial do item VI | **NAO aberta.** Vem em **mensagem separada**, por determinacao expressa |

## 6. Condicoes anteriores de eficacia — conferidas pelo proprio Soberano

O ato declara: *"tendo conferido as condicoes anteriores de eficacia de `PS-2026-017`, versao
1.3.0"*. **A conferencia e do Soberano, e este registro nao a refaz nem a substitui.** O que
este registro faz e **deixar medido o que estava a vista quando ele conferiu**:

| Condicao | Estado no instante do ato |
|---|---|
| Os `20` valores publicados em §3 e §3.1 | **`20` de `20` reproduzem** — terceira reconferencia, `13:29`, §3.4 |
| Os quatro objetos vivos | **intocados**, `H-A` e `H-N` |
| Baseline, pelo instrumento vigente `IR-BL/3` | **`228 · 68.002 · 0b548d81…6f8b`**, `2` execucoes, `EXIT=0` |
| Ponto de retorno do §4 | **provado fiel** — a copia reproduz os tres valores da baseline |
| Achados abertos nomeados na ciencia | **`7`**, dos quais **`6` inscritos** e `RD-104` **declarado** |

## 7. Limites — o que este ato NAO faz

1. **Nao sana `C0 · T2`.** Item V: `RD-91` fecha **so quanto a `C1`**.
2. **Nao emenda `FND-04`.** Item VIII: o conflito entre `§2` bloco `C3` e `AL-01`/`CC-02`
   permanece **aberto em `RD-99`**, com o mesmo gatilho de `RD-18`.
3. **Nao estende a emenda a `PRJ` e `TPL` por si.** Item IV **ordena missao** para redigi-la;
   **`RD-96` e `RD-97` seguem ABERTOS** ate o ato proprio que os sanar.
4. **Nao reclassifica `SPC-001`.** Item III.
5. **Nao levanta o congelamento.** Item VII: **duas frentes, e nenhuma outra**.
6. **Nao corrige a nota superada do item I** — ver §4, aviso.
7. **Nao inscreve `RD-104`** — ver §2.2.

## 8. A missao ministerial que consome este ato — **uma so, e ainda nao aberta**

**DEP-GOV**, pelo item VI. Ordem minima, extraida do proprio item:

1. Mover `status` e `ratificacao` dos **quatro** objetos *(`O4`: `aprovado → ativo`,
   `pendente → ratificada`)*.
2. **Reproduzir os quatro `H-P` de §4.** **Se qualquer um nao reproduzir, a aplicacao PARA** —
   condicao do proprio item VI.
3. Atualizar o **catalogo mestre**, reconciliando as linhas *Artefatos*, *Linhas* e *Baseline
   vigente* de §2, hoje **desatualizadas por declaracao**.
4. **Emitir baseline nova.**
5. Inscrever o **fechamento parcial de `RD-91`**.

> ⚠️ **Quem aplicar deve ler os `H-P` de §4 deste registro ou do §3.1 do pacote — nunca de
> `_missao-1-13-5-1-2026-08-02/evidencia/hashes-candidatos.txt`**, que carrega **`6` valores
> superados de `24`** e faria **`2` de `4`** falharem, **parando uma aplicacao correta**.
> Achado **`RD-101`**, catalogo item **124**.

## 9. Estado do acervo medido nesta emissao

| Medida | Valor |
|---|---|
| Baseline **antes** desta escrita | **`228 · 68.002 · 0b548d81…6f8b`** |
| Instrumento | **`IR-BL/3`**, `sha256` `0d4f1b3d…4ad7`, `2` execucoes, `EXIT=0` |
| Lease | **`fencing_token` 17**, adquirido `15:22:39` **antes da primeira escrita** |
| Ponto de retorno | `_backups/…_pre-ato-rd-91`, **`234`** arquivos, manifesto `c34b84b1…2ed8`, conferido `234` de `234`, **reproduzindo os tres valores** |

**Este registro acrescenta `1` artefato ao acervo — ele proprio.** A contagem e as linhas que
ele move serao reconciliadas pela **aplicacao do item VI**, junto com todo o resto.

## 10. Nao edicao das fontes anteriores

**`0` bytes** em `PS-2026-017` — obrigatorio, pela ancora. **`0` bytes** em `ADR-0032`,
`RFC-0027`, `FIT-2026-025` e `PT-2026-018`. **`0` bytes** em `MSG-2026-0001` a
`MSG-2026-0009`. **`0` bytes** em baseline anterior. **`0` bytes** em `FND-01`–`FND-11`,
Cartas, `TPL` e `CAP`.

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-08-02 | SOBERANO | Criacao. Registra o **decimo ato soberano**, emitido sobre os **itens I a VIII** da minuta de [`PS-2026-017`](../../governance/pacote-soberano-2026-08-02-rd-91.md) **1.3.0**, linhas `571`–`655`, ancorado no `H-A` do pacote **`c48cf443…0298`** e em **`4`** `sha256` de recorte. Os quatro `H-P` foram **extraidos do proprio arquivo, de duas sedes independentes**, e conferidos contra medicao nova: **`8` de `8`**, com controle positivo do instrumento antes do uso — **`0` valores de transcricao**, como o despacho exigiu. §2.2 mede a declaracao de ciencia: dos **`7`** achados nomeados, **`6` inscritos** e **`RD-104` apenas declarado** — **nomear nao inscreve**. §4 declara que a nota do item I do texto assinado ficou **SUPERADA** *(diz `2` reconferencias sobre a `1.2.0`; foram `3`, a terceira sobre a `1.3.0`)* e **NAO a corrige**: o ato foi emitido *"sem alteracao de termo"*, e a nota **subestima** os fatos sem contraria-los. §3 mede os quatro objetos **DEPOIS** desta escrita e os encontra **intocados** — `1.5.0`, `1.0.0`, `1.1.0` e `1.1.0`. **`0` aplicados, `0` ratificados na arvore, `0` baselines emitidas, `0` missoes abertas.** Escrito sob **`fencing_token` 17**, adquirido **antes** da primeira escrita. |
