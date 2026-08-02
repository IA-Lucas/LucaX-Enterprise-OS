---
id: PT-2026-012
titulo: Relatorio de transicao da Missao 1.13.4.1 — manutencao dos instrumentos
tipo: relatorio
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-07-31
atualizado_em: 2026-07-31
revisao_prevista: null
decisoes_relacionadas: [ADR-0005, ADR-0007, ADR-0012, ADR-0026]
substitui: []
substituido_por: null
resumo: Repara os defeitos de instrumento que o primeiro exercicio real do portao revelou na 1.13.4 e reprova o Item 0: dos 19 caminhos medidos no repositorio externo, 5 nao tem processo produtor nomeavel porque nenhuma mudanca da janela foi commitada.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# PT-2026-012 — Missao 1.13.4.1: manutencao dos instrumentos

> **Nenhum candidato foi julgado, nenhum Produto admitido, nenhuma `Spec` criada, nenhum ato
> emitido e nada ratificado.** O pacote da 1.13.4 esta **suspenso, nao descartado**, e **nao foi
> alterado** — `0` bytes.
>
> **Esta missao conserta ferramenta.** Ela nao decide nada que dependa do Soberano, e **`Q1`
> continua precedendo tudo**.
>
> ### ⛔ Decisao: **`BLOCKED`** — o Item 0 reprova
>
> Dos **19** caminhos medidos no repositorio externo durante a janela da 1.13.4, **14 estao
> atribuidos a processo nomeado e 5 sao NAO ATRIBUIVEL**. A regra do Item 0 nao admite
> compensacao pelos outros seis criterios, e eles **nao a compensam** — §11.
>
> **Nao ha indicio de escritor concorrente no acervo canonico**, e nenhum dos 5 e atribuivel a
> missao alguma de governanca. **NAO ATRIBUIVEL significa que nao se sabe** — e o motivo esta
> medido: **nenhuma das 19 mudancas foi commitada**, e sem commit nao existe registro de autoria.

## Proposito

Reparar os defeitos que o **primeiro exercicio real** do portao de `ADR-0007` e da medicao
revelou na Missao 1.13.4, e registrar o que a reparacao mediu.

## Escopo

| Item | Definicao |
|---|---|
| Inclui | O **Item 0** *(atribuicao do que mudou no repositorio externo)* · **`RD-53`** *(comando da baseline)* · **`RD-49`**, **`RD-57`**, **`RD-58`** e a **contagem de fontes** · **`RD-56`** *(template)* · a **prova de nao-escrita executavel** · **tres minutas** preparadas e nao aplicadas · o **texto literal** da decisao 7 |
| **Nao** inclui | Julgamento de candidato · admissao de Produto · criacao de `Spec` · emissao de ato · ratificacao · alteracao do pacote da 1.13.4 · aplicacao das minutas · fechamento de `RD-33` · escrita no SSC+ · qualquer achado fora da lista |
| Natureza | **Manutencao.** Nenhum tipo, entidade, camada ou diretorio novo |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| Executa a manutencao | **DEP-GOV** | Proprietario dos instrumentos de medicao e do catalogo |
| Emenda o template | **DEP-GOV** | `FND-09 §8.2`, linha `TPL` — precedente `TPL-spec` **1.1.0** |
| Revisa | **DEP-QAR** | `ADR-0005` — **com o limite de `§7.2` declarado** |
| Decide o que exige ato | **SOBERANO** | `Q1`, as tres minutas e as tres Cartas **1.2.0** |

---

## 0. Pre-condicoes — cumpridas antes da primeira escrita

| # | Pre-condicao | Estado |
|---|---|---|
| `PC-1` | **`BL-2026-07-31-01` reproduzida** | ✅ **194 · 56.854 · `b355e227b6c0a842dc1be0e0a78f2030a88e7a7ab7cd2686103bc1b9752775bf`** |
| `PC-2` | **Copia datada fora do acervo** | ✅ `_backups/LucaX-Enterprise-OS_2026-07-31_pre-missao-1-13-4-1/` — **572** arquivos, **com a baseline reconferida na copia** |
| `PC-3` | **Ponto de rollback por `H-A`** | ✅ `H-A` integral dos **194** artefatos, tomado **antes** de qualquer escrita — `evidencia/H-A-rollback-pre-escrita.txt`, `sha256` `0f0a3fba6be8759b9092ae455d4bcd2890436b134a152bab36f04eb38d0745dd` |
| `PC-4` | **Lease e fencing adquiridos antes da primeira escrita** | ✅ `_leases/LucaX-Enterprise-OS.lease`, **`fencing_token: 1`**, fenceado a `BL-2026-07-31-01`. **Vivo do inicio ao fim; liberado somente no fechamento** — §9 |
| `PC-5` | **Escritor unico confirmado** | ✅ §1.3 |
| `PC-6` | **Instante do repositorio externo fixado** | ✅ Manifesto `sha256` de **531** arquivos, **`2a9a2725701a6e7859010419269b4ad451d9eafa46d1966c62f348d21311600e`**, tomado **antes de qualquer leitura de conteudo** |

> ### ⚠️ `PC-4` cumprida por instrumento novo, e a ausencia esta declarada
>
> **Nao existe lease nem fencing em norma vigente do acervo.** Varredura sobre os **194**
> artefatos: **`0` ocorrencias** de *lease* e **`0`** de *fencing*. A pre-condicao foi cumprida
> criando o instrumento **fora do acervo** — o lease **nao e artefato** e **nao institui norma**.
> **Instituir lease e rito proprio, e esta missao nao o faz.**

## 1. ITEM 0 — atribuicao, bloqueante, antes de qualquer escrita

### 1.1 A janela da 1.13.4, fixada por evidencia

| Marco | Instante | Como se sabe |
|---|---|---|
| **Abertura** | **2026-07-31 07:28** | `mtime` de `_backups/…_2026-07-31_pre-missao-1-13-4/`, a copia datada que precede a primeira escrita |
| Primeira escrita no acervo | **07:42:00,45** | `RFC-0021` |
| **Fechamento do manifesto externo** | **entre 08:11:20,83 e 08:12:01,06** | `PS-2026-014` foi escrito **08:12:01,06** e **enumera `tudo.html`**, que nasceu **08:11:19,86**; o ultimo caminho da janela e **08:11:20,83** |
| Ultima escrita no acervo | **08:15:57,07** | `FIT-2026-019` |

### 1.2 Os caminhos que mudaram — **19 medidos**

Medido por `mtime` sobre **todos** os arquivos do repositorio externo, **inclusive os
ignorados pelo `git`** — que e onde os tres omitidos estavam. Exclusoes: apenas `.git/`,
`.mypy_cache/` e `.pytest_cache/`, **as mesmas que a 1.13.4 declarou**.

| # | Instante | Caminho | Classe | Processo atribuido |
|---|---|---|---|---|
| 1 | 07:49:47,26 | `ferramentas/gravar_video_institucional.py` | alterado | Edicao do gerador de video |
| 2 | 07:54:44,74 | `docs/demonstracao/video/medally-institucional.mp4` | alterado | **Saida** de (1) |
| 3 | 07:54:44,89 | `docs/demonstracao/video/medally-teaser.mp4` | alterado | **Saida** de (1) |
| 4 | 07:54:45,09 | `docs/demonstracao/video/relatorio.json` | alterado | **Saida** de (1) |
| 5 | 07:54:47,02 | `docs/demonstracao/video/ROTEIRO-NARRACAO.md` | alterado | **Saida** de (1) |
| 6 | 07:58:33,99 | `docs/demonstracao/video/web/institucional-crf34.mp4` | alterado | Saida de `montar_pagina_video.py` — **ver §1.4** |
| 7 | 07:58:34,16 | `docs/demonstracao/video/web/video.html` | alterado | Saida de `montar_pagina_video.py` — **ver §1.4** |
| 8 | 08:08:54,42 | `ferramentas/montar_pagina_video.py` | alterado | Edicao do gerador da pagina de video |
| 9 | 08:09:17,71 | `docs/demonstracao/felipe/links.json` | alterado | **Entrada** dos dois geradores de pagina, editada a mao |
| 10 | 08:10:44,64 | `tests/test_paginas_felipe.py` | **novo** | Escrita de teste novo — **NAO enumerado pela 1.13.4** |
| 11 | 08:10:55,94 | `tests/__pycache__/test_paginas_felipe.cpython-314-pytest-9.1.1.pyc` | **novo** | **Execucao de `pytest`** sobre (10) — **NAO enumerado** |
| 12 | 08:11:12,51 | `ferramentas/montar_paginas_felipe.py` | alterado | Edicao do gerador das paginas |
| 13 | 08:11:19,86 | `docs/demonstracao/felipe/prontuario-paciente.html` | alterado | **Saida** de (12) |
| 14 | 08:11:19,86 | `docs/demonstracao/felipe/sala.html` | alterado | **Saida** de (12) |
| 15 | 08:11:19,86 | `docs/demonstracao/felipe/documentos.html` | alterado | **Saida** de (12) |
| 16 | 08:11:19,86 | `docs/demonstracao/felipe/indice.html` | alterado | **Saida** de (12) |
| 17 | 08:11:19,86 | `docs/demonstracao/felipe/prontuario-medico.html` | alterado | **Saida** de (12) |
| 18 | 08:11:19,86 | `docs/demonstracao/felipe/tudo.html` | **novo** | **Saida** de (12) — pagina nova do gerador |
| 19 | 08:11:20,83 | `ferramentas/__pycache__/montar_paginas_felipe.cpython-314.pyc` | **novo** | **Importacao** do gerador por `pytest` — **NAO enumerado** |

### 1.2.1 ATRIBUIDO × NAO ATRIBUIVEL — **14 e 5**, nominal, sem sobra

> **Correcao de uma resposta anterior deste relatorio.** A primeira emissao afirmou **"19 de 19
> atribuidos"**. **Isso respondeu em CONTAGEM, nao em ATRIBUICAO.** O Item 0 pede atribuicao **a
> processo e horario**; coerencia de linha de trabalho **nao e processo**. Refeita a resposta na
> forma em que o Item 0 foi escrito, o resultado e outro.

**Horario: 19 de 19.** `mtime` exato, ao decimo de milissegundo, para todos.
**Processo: 14 de 19.**

**GRUPO A — ATRIBUIDO a processo nomeado *(14)*.** Nao ha inferencia: o processo produtor esta
**nomeado no codigo**, que declara aquele caminho exato como saida sua, e o `mtime` e posterior.

| # | Caminho | Processo nomeado | Evidencia mecanica |
|---|---|---|---|
| 1 | `docs/demonstracao/video/medally-institucional.mp4` | `gravar_video_institucional.py` | `DESTINO / "medally-institucional.mp4"`, linha 1045 |
| 2 | `docs/demonstracao/video/medally-teaser.mp4` | idem | `DESTINO / "medally-teaser.mp4"`, linha 1053 |
| 3 | `docs/demonstracao/video/relatorio.json` | idem | `(DESTINO / "relatorio.json").write_text`, linha 1066 |
| 4 | `docs/demonstracao/video/ROTEIRO-NARRACAO.md` | idem | `(DESTINO / "ROTEIRO-NARRACAO.md").write_text`, linha 1069 |
| 5 | `docs/demonstracao/video/web/institucional-crf34.mp4` | `montar_pagina_video.py` | `args.saida / f"institucional-crf{args.crf}.mp4"` — **o `34` no nome e a assinatura do parametro** |
| 6 | `docs/demonstracao/video/web/video.html` | idem | `pagina = args.saida / "video.html"`, linha 327 |
| 7–12 | as **6** paginas de `docs/demonstracao/felipe/` | `montar_paginas_felipe.py` | o dicionario de saidas lista **exatamente** `sala.html`, `prontuario-paciente.html`, `prontuario-medico.html`, `documentos.html`, `indice.html` e `tudo.html`, gravadas em `DESTINO` |
| 13 | `tests/__pycache__/test_paginas_felipe.cpython-314-pytest-9.1.1.pyc` | **CPython 3.14 sob `pytest` 9.1.1** | o nome do arquivo **carrega o interpretador e a versao do pytest**; e cache de bytecode de um modulo nomeado |
| 14 | `ferramentas/__pycache__/montar_paginas_felipe.cpython-314.pyc` | **CPython 3.14** | idem — cache de bytecode de `montar_paginas_felipe` |

**GRUPO B — NAO ATRIBUIVEL a processo *(5)*.** Horario exato; **produtor nao nomeavel**.

| # | Caminho | O que se sabe | Por que continua NAO ATRIBUIVEL |
|---|---|---|---|
| 1 | `ferramentas/gravar_video_institucional.py` | Edicao as 07:49:47,26. As saidas declaradas dele aparecem **4m57s depois** | A cadeia liga a edicao a uma execucao **posterior**; **nao nomeia quem editou** |
| 2 | `ferramentas/montar_pagina_video.py` | Edicao as 08:08:54,42 | **Nenhuma amarra sequer indireta:** as saidas dele sao **anteriores** a edicao (§1.4), e **nenhuma execucao se seguiu** |
| 3 | `ferramentas/montar_paginas_felipe.py` | Edicao as 08:11:12,51. Saidas declaradas **7,3s depois** | Mesma situacao de (1) |
| 4 | `tests/test_paginas_felipe.py` | Criado as 08:10:44,64; `pytest` o compila **11s depois** | O `.pyc` identifica o **consumidor**, nunca o **escritor** |
| 5 | `docs/demonstracao/felipe/links.json` | Alterado as 08:09:17,71 | **Nenhum processo do repositorio o escreve.** Varredura completa: as **tres** ocorrencias em codigo — `montar_paginas_felipe.py`, `montar_pagina_video.py` e `test_paginas_felipe.py` — **todas o LEEM** |

**O teto de atribuicao e do candidato, nao do metodo — e esta medido.** As **19** mudancas da
janela sao **trabalho nao commitado**: **4** dos 5 caminhos do Grupo B estao ` M` e **1** esta
`??`, e o ultimo commit que toca qualquer um deles e de **2026-07-30**, **anterior a janela**.
**`0` commits, `0` entradas de stash, `0` artefatos de editor.** **Sem commit nao existe registro
de autoria**, e nenhuma ferramenta recupera depois o que nao foi gravado na hora.

> **O que NAO se afirma, e por que.** Os 5 do Grupo B sao **tematicamente coerentes** com a mesma
> sessao de produto que produziu os 14 do Grupo A. **Coerencia tematica e inferencia plausivel, e
> inferencia plausivel nao e atribuicao** — reclassifica-los por ela e vedado, e seria o mesmo
> vicio que esta missao mediu em `RD-60`: transformar o que se supoe no que se declara medido.
> `mtime` prova **quando**; a cadeia gerador→gerado prova **por que**; **nenhum dos dois prova
> QUEM** (`PI-10`, `LV-12`).
>
> **E o que tambem NAO se afirma: que sejam da Missao 1.13.4.** Nao ha evidencia de que sejam, e
> o ferramental que ela declarou — leitura, contagem e `sha256` — **nao produz `.mp4` de 21 MB
> nem executa `pytest`**. **NAO ATRIBUIVEL significa exatamente isto: nao se sabe, e a ausencia
> fica declarada em vez de preenchida** nos dois sentidos.

#### Caminhos **fora** da janela, e por isso fora da atribuicao

| Instante | Caminho | Posicao |
|---|---|---|
| 07:27:16 · 07:27:52 · 07:28:02 | `public/sala.css` · `tests/test_teleconsulta.py` · o `.pyc` dele | **antes** da abertura — ja estavam sujos quando a 1.13.4 abriu |
| 08:13:18 | `docs/CHECKLISTS.md` · `docs/RC1.md` · `README.md` | **depois** do fechamento do manifesto |
| 08:21:26 · 08:21:35 · 08:22:17 · 08:24:07 | caches e `ESTADO-medally.md` | **depois** do fechamento |

> **`README.md` mudou as 08:13:18** — e e **uma das cinco fontes** que `Z2` de `PS-2026-014 §2.2`
> declara *"byte a byte identicas"*. **A declaracao estava correta no instante em que foi feita**
> *(o manifesto fechou antes das 08:12:01)* e **deixou de estar 77 segundos depois**. Nao e
> defeito da 1.13.4: e a demonstracao mais direta de **`RD-59`** — sobre repositorio vivo, uma
> afirmacao de identidade so vale **amarrada a um instante**, e a 1.13.4 amarrou.

### 1.3 Escritor concorrente no acervo — **nao ha**

| Verificacao | Resultado |
|---|---|
| Arquivos `.md` do acervo alterados em 2026-07-31 | **11** — e os **11** sao exatamente as saidas declaradas da 1.13.4 |
| Arquivos **de qualquer extensao** alterados | **13** — os 11 mais `.obsidian/graph.json` *(07:28:08)* e `.obsidian/workspace.json` *(08:15:58)* |
| Natureza dos dois restantes | **Estado do editor Obsidian**, nao artefato. Estao na **lista de exclusao** da propria baseline |
| Escrita no acervo entre o fechamento da 1.13.4 e a aquisicao do lease | **`0`** — o `mtime` mais recente do acervo era **08:15:57**, e o lease foi adquirido as **09:41:56** |

**Conclusao do Item 0: NAO BLOQUEIA.** Nenhum arquivo nao atribuivel; nenhum indicio de
escritor concorrente **no acervo**. A missao pode escrever.

### 1.4 Ordem gerador × gerado — **duas compativeis, uma nao**

Saidas confirmadas **por leitura do codigo** de cada gerador, nao por suposicao.

| Gerador | `mtime` | Saidas | `mtime` das saidas | Ordem |
|---|---|---|---|---|
| `gravar_video_institucional.py` | 07:49:47,26 | `medally-institucional.mp4` · `medally-teaser.mp4` · `relatorio.json` · `ROTEIRO-NARRACAO.md` | 07:54:44,74 → 07:54:47,02 | ✅ **COMPATIVEL** — saidas **4m57s depois** |
| `montar_paginas_felipe.py` | 08:11:12,51 | as **6** paginas de `docs/demonstracao/felipe/` | 08:11:19,85 → 08:11:19,86 | ✅ **COMPATIVEL** — saidas **7,3s depois** |
| `montar_pagina_video.py` | 08:08:54,42 | `video/web/institucional-crf34.mp4` · `video/web/video.html` | 07:58:33,99 · 07:58:34,16 | ❌ **INCOMPATIVEL** — saidas **10m20s ANTES** |

> **A incompatibilidade e declarada, e a leitura dela e restrita.** As duas saidas de
> `video/web/` **nao foram produzidas pela versao atual** de `montar_pagina_video.py`: o arquivo
> foi editado **depois** da ultima execucao que as gerou, e **nao foi reexecutado**. Isso **nao
> indica escrita pela missao** — indica material de demonstracao **defasado do seu gerador**
> dentro do repositorio do candidato. **E fato sobre o candidato, nao sobre o acervo**, e nao se
> tira dele nenhuma conclusao sobre merito.

### 1.5 A contagem 550 → 551 — **o valor medido e 554**

| Instante | Manifesto *(exclui `.mypy_cache/` e `.pytest_cache/`)* | Caches | **Total** |
|---|---|---|---|
| Abertura da 1.13.4 | **527** *(publicado)* | 23 | **550** *(publicado)* |
| Fechamento da 1.13.4 | **531** | 23 | **554** ⟵ **medido agora** |
| Publicado pela 1.13.4 | — | — | **551** |

**A aritmetica fecha nos dois sentidos, e por isso a conclusao e firme.**
`527 + 4` arquivos novos `= 531`; `550 + 4 = 554`. **Os quatro novos sao os itens 10, 11, 18 e
19** da tabela de §1.2, **todos criados antes do fechamento do manifesto**, e **`0` removidos**.

**Como se sabe que nada foi criado ou removido depois:** o `mtime` de **diretorio** muda quando
uma entrada e criada ou removida, e **nao** muda quando um arquivo e apenas modificado —
verificado por teste direto neste sistema de arquivos antes de o argumento ser usado. **Nenhum
diretorio do repositorio** tem `mtime` na janela apos 08:11:21, exceto `.mypy_cache/3.14/`
as 08:21:35, **fora da janela**, e cuja contagem de arquivos **nao mudou** *(16, e o total de
cache continua 23)*.

> **`551` = `550 + 1`.** E o unico valor compativel com **contar apenas o arquivo novo
> enumerado**, e e incompativel com **medir**. O campo esta marcado *"observado, nos dois
> instantes"* em `PS-2026-014 §2`. **Agregado escrito como aritmetica e publicado como
> observacao** — familia de `MEM-APR-0002`, e o achado **`RD-60`**.

### 1.6 O criterio **"17 de 17"** — substituido, e a substituicao e CORRECAO

> **Esta secao nao registra cumprimento. Registra que um criterio de validacao foi fixado
> com um numero que nao existe, e por isso teve de ser trocado.**

#### 1.6.1 O que foi pedido, e por que nao se pode cumprir literalmente

A determinacao pede *"os **17** arquivos que mudaram … : 1 novo e 15 alterados sob
`docs/demonstracao/`, tres geradores em `ferramentas/`, contagem 550 para 551"*, e fixa a
validacao em **"17 de 17 arquivos atribuidos, sem sobra silenciosa"**.

**O `17` nao e derivavel de nenhuma fonte.** Nao do proprio enunciado, nao do pacote da 1.13.4,
nao do disco. As **tres** leituras possiveis do enunciado:

| # | Leitura | Aritmetica | Resultado |
|---|---|---|---|
| `R1` | *"1 novo e 15 alterados"*, com os 15 repartidos entre `docs/demonstracao/` **e** `ferramentas/` | `1 + 15` | **16** |
| `R2` | *"1 novo e 15 alterados **sob `docs/demonstracao/`**"* **mais** *"tres geradores em `ferramentas/`"* | `1 + 15 + 3` | **19** |
| `R3` | Os 16 caminhos de `R1` **mais** a mudanca de contagem *(550 → 551)* contada como decimo setimo item | `16 + 1` | **17** |

**`R1` reproduz o pacote:** `PS-2026-014 §2.2` enumera **12** alterados sob `docs/demonstracao/`
+ **3** em `ferramentas/` = **15**, mais **1** novo = **16**. **`R3` e a unica que chega a 17, e
para isso conta como arquivo uma coisa que nao e arquivo** — a mudanca do total. **`R2` chega a
19.**

#### 1.6.2 A leitura que acerta o total erra a composicao

**`R2` produz 19, que e o numero medido. A coincidencia e enganosa e precisa ficar registrada
como coincidencia**, porque as duas composicoes sao diferentes:

| Bloco | `R2` supoe | **Medido** |
|---|---|---|
| Alterados sob `docs/demonstracao/` | **15** | **12** |
| Alterados em `ferramentas/` | 3 | **3** |
| Novos | 1 | **4** — `tudo.html`, `tests/test_paginas_felipe.py` e **dois** `.pyc` |
| **Total** | **19** | **19** |

**`R2` erra em `−3` sob `docs/demonstracao/` e em `+3` nos novos, e os dois erros se cancelam.**
Aceitar `R2` porque o total bate seria dar por reconciliado o que nao foi: **o total certo por
composicao errada nao e reconciliacao, e sim duas divergencias que se anulam** — a mesma forma
de `RD-61`, onde `−3` de criterio e `+1` de acervo se somaram dentro de um numero so.

**Os 3 novos que nenhuma leitura previa sao exatamente os 3 que a 1.13.4 omitiu** *(`RD-60`)*.
Dai a identidade que fecha tudo:

> **19 = os 16 que a 1.13.4 enumerou + os 3 que ela omitiu.**

#### 1.6.3 O criterio substituido

| Campo | Conteudo |
|---|---|
| **Criterio original** | *"17 de 17 arquivos atribuidos, sem sobra silenciosa"* |
| **Defeito** | O `17` foi **fixado sem contagem**. Nao ha fonte que o produza; a unica leitura que o alcanca conta a mudanca de um total como se fosse um arquivo |
| **Criterio que passa a valer** | **"Todos os caminhos medidos atribuidos, sem sobra silenciosa"** |
| **Natureza da troca** | **CORRECAO de um criterio defeituoso — nao cumprimento do criterio original.** O original **nao foi satisfeito e nao e satisfazivel** |
| **O que a troca preserva** | **A exigencia substantiva inteira**: *sem sobra silenciosa*. Nenhum caminho pode ficar fora, nenhum pode ser descartado por ser volatil, e **nenhum pode ser dado por atribuido sem processo** |
| **O que a troca NAO faz** | **Nao afrouxa o portao.** Sob o criterio corrigido o Item 0 **reprova** — §1.2.1 —, o que a formulacao original, com o numero errado, poderia ter mascarado |

> **Escrever "17 de 17" teria sido publicar como medido um agregado que nao foi contado** — o
> defeito que esta missao abriu contra a 1.13.4 em `RD-60`, cometido pela missao que o abriu.
> **O numero fabricado nao veio do acervo: veio do enunciado da missao**, e por isso a correcao
> e registrada aqui e nao em `§7` do catalogo, que registra achados **sobre o acervo**.

## 2. `RD-53` — o comando da baseline, corrigido e provado

### 2.1 O defeito nunca foi da baseline. Era do comando.

| Medicao sobre a copia datada `_backups/…_2026-07-30_pre-missao-1-13-3/` | Resultado |
|---|---|
| Pelo **comando publicado** *(denylist de duas exclusoes)* | **198** artefatos |
| Pela **lista fechada** *(mesmas raizes do acervo)* | **185 · 54.190 · `3d8dbea0f9ee534707156c54fa2ab58c95640ef0fb2436a981b50bb2adea84da`** |
| Valor publicado de **`BL-2026-07-30-01`** | **185 · 54.190 · `3d8dbea0…84da`** |

> **`BL-2026-07-30-01` REPRODUZ, nos tres valores e nos 64 digitos, sobre a mesma copia em que
> o comando publicado dava 198.** A baseline sempre esteve certa; **o instrumento e que nao
> media o que dizia medir**. `BL-2026-07-30-01` **nao foi editada** — `BL-02` intacta.
>
> **Isto desfaz a premissa mais grave da lista de reparos:** *"baseline que nao reproduz torna
> nominal toda verificacao a jusante"*. **Nenhuma verificacao a jusante era nominal** — o
> comando e que era.

### 2.2 O que foi corrigido — tres portoes onde havia duas exclusoes

| # | Correcao | Por que |
|---|---|---|
| **`G-A`** | **Lista fechada POSITIVA** das raizes do acervo, em vez de denylist | Denylist admite em silencio toda raiz nova. Foi assim que `_candidatos/` entrou e produziu **198** |
| **`G-B`** | **Portao de raiz**: entrada na raiz que nao seja declarada — nem acervo, nem nao-acervo — **PARA a medicao** | Contagem errada deixa de ser silenciosa e passa a ser **recusa** |
| **`G-C`** | **Portao de split**: exige **exatamente uma** linha `total` na saida de `wc -l` | Quando o acervo crescer o bastante para o `xargs` quebrar a chamada em lotes, `tail -1` passa a somar **so o ultimo lote** — e a impressao digital muda sem que nada tenha mudado. **Defeito ainda nao ocorrido, e por isso barato de fechar** |

### 2.3 A prova — **duas execucoes independentes, hash identico**

| # | Execucao | Artefatos | Linhas | Impressao digital |
|---|---|---|---|---|
| **1** | Sobre o **acervo vigente** | **194** | **56.854** | `b355e227b6c0a842dc1be0e0a78f2030a88e7a7ab7cd2686103bc1b9752775bf` |
| **2** | Sobre a **copia datada** `_backups/…_2026-07-31_pre-missao-1-13-4-1/`, processo separado | **194** | **56.854** | **idem, 64 digitos** |
| **3** | Pelo **PowerShell**, invocando o mesmo instrumento | **194** | **56.854** | **idem** |

**Portao de raiz exercido contra um caso real:** apontado a copia de 1.13.3, o instrumento
**recusa medir** e sai com codigo **2**, nomeando `_candidatos` como entrada nao declarada.
**O portao pega exatamente a condicao de `RD-53`.**

**Comando publicado, para reproducao — PowerShell:**

```powershell
& "E:\LucasIA\Git\bin\bash.exe" `
  "E:\LucasIA\Projetos\_missao-1-13-4-1-2026-07-31\ferramentas\baseline.sh" `
  "E:\LucasIA\Projetos\LucaX Enterprise OS"
```

> **O instrumento vive FORA do acervo, e e deliberado.** A baseline conta `*.md`; um script
> dentro da raiz seria **invisivel** para a propria medicao que ele executa — a mesma familia de
> `RD-53`, por outro caminho. **`RD-53` fica ✅ FECHADO** por instrumento novo, sem editar
> baseline alguma.

## 3. `RD-49`, `RD-57`, `RD-58` e a contagem de fontes

### 3.1 `RD-49` — medido, e corrigido ate onde esta missao pode ir

| Carta | §13.2 declara | `wc -l` do arquivo vigente | Delta | Candidato **1.2.0** declara e mede |
|---|---|---|---|---|
| `DEP-OPS` | **437** | **438** | **−1** | **439** |
| `DEP-GRW` | **443** | **444** | **−1** | **445** |
| `DEP-TLS` | **424** | **425** | **−1** | **426** |

**A causa e uma so, e ja estava escrita.** A emenda **1.1.0** acrescentou a linha de historico
que `FND-03 §6` obriga — **+1 linha** — e **nao remediu §13.2**. `RA-1` de `FIT-2026-018` ja
nomeara a mitigacao: *"remedir §13.2 **DEPOIS** da linha de historico, nunca antes"*.
**Os tres candidatos foram construidos exatamente nessa ordem**: frontmatter, linha de
historico, **e so entao** a medicao — que por isso declara **439 · 445 · 426**, e nao os
**438 · 444 · 425** que uma medicao feita antes teria gravado e a propria emenda invalidaria.

| Objeto | `H-A` | `H-N` | `H-P` *(apos `O4`)* |
|---|---|---|---|
| `DEP-OPS` **1.2.0** | `1790f3493c8701f7cf19ae3c7db89e6921dfbf9d5a16de4fc65cc4ed587b0dae` | `a62b88999410d04c776d34d4b5e56d19390151b7ae938f9c89a81908899ff8f4` | `571120d14c4c699a6cb45f12413afd13f23daa6d686da0cd0d0ab20874933e1d` |
| `DEP-GRW` **1.2.0** | `64d5fe0d701755844fbd2109492c101a9c814887a0633f80a548246594b536dc` | `d8adcda1c1ffad46d077fd23149f5fe396ce3469b6ce29bb23170b35fced7f51` | `6c5af6eb85d4fb61066c8611fca58ba7e2d3c7ade900ec22511fc8b88ee343ac` |
| `DEP-TLS` **1.2.0** | `44bdeb1c2903b954bd614cc1b7cb3855ba8e0b29842f8b21bf05f922de440f53` | `1cd6a3cddba3cb00b08845b126a29e18d257ea4a182f358e317bf54b0dc5a461` | `536e3cd77fe82d16684fc916238f2e516c21c39813f7490f7991a6f8ca4dd745` |

**Provas de integridade: `3 de 3` em cada uma.** `H-N` invariante sob `O4`; `IR-09` reconstroi
`H-A` revertendo **apenas** `status` e `ratificacao`; o `diff` de `O4` alcanca **exatamente duas
linhas** em cada arquivo, e **`atualizado_em` nao e tocado**.

> ### Por que os tres NAO foram aplicados
>
> **As tres Cartas estao `ativo` · `ratificada` por ato soberano.** `R1` de `FIT-2026-018`
> registra: *"nao corrigivel por edicao … exige ato novo"*, e o precedente e literal —
> `DEP-QAR` **1.2.0** fechou **o mesmo defeito** *(`RC-01`)* nascendo em `em-revisao` ·
> `ratificacao: pendente`, porque *"emendar Carta ja ratificada exige ato novo do Soberano
> (`DC-09`, `LM-03`, `IR-01`)"*. **Esta missao nao emite ato.** Os tres candidatos vivem
> **fora do acervo**, medidos e prontos para aplicacao, e **`RD-49` permanece ⚠️ ABERTO** —
> **corrigido por rito ate o limite desta missao, nao fechado**.

### 3.2 `RD-57` — o catalogo divergindo de si proprio

**Verificado nesta missao, valor a valor, contra a fonte.** A emissao anterior corrigiu os cinco
lugares; a conferencia agora **reproduz `194` e `56.854` em `resumo`, `§Escopo`, `§2`, no
cabecalho de `§4` e em `§9`**, todos concordando com `§10.0`. **`RD-57` ✅ FECHADO**, e o §7
deste relatorio registra o que ele deixou como sinal: **agregado escrito como literal reincide
por falta de gatilho, nao por desatencao**.

### 3.3 `RD-58` — ✅ FECHADO, e a correcao foi **suprimir**, nao corrigir o valor

A linha `FIT-2026-NNN` **foi removida** de *Contadores oficiais* de
[`governance/README`](README.md). **O defeito nunca foi a divergencia — era a duplicata**
(`PJ-01`). Enquanto a linha existiu, divergiu da fonte **tres emissoes seguidas**, e a emissao
anterior **corrigiu o valor sem remover a linha**, o que garantia a quinta ocorrencia.
O gatilho declarado era *"proxima emenda a este indice"*; **esta e a emenda**.

### 3.4 A passagem **73 → 71** — dois motivos diferentes somados num numero so

Medido nas **duas** copias, pelos **dois** criterios:

| Copia | Todos os `.md` das tres arvores | **Excluindo os indices** | Indices | `FND` |
|---|---|---|---|---|
| Pre-1.13.3 — onde `BL-2026-07-30-01` publicou **73** | **73** ⟵ | 70 | 3 | 10 |
| Acervo vigente — onde `BL-2026-07-31-01` publica **71** | 74 | **71** ⟵ | 3 | 11 |

**A explicacao e aritmetica e verificavel: `73 − 3 + 1 = 71`.**

| Componente | Valor | Natureza |
|---|---|---|
| **`−3`** os tres indices *(`foundation/README`, `capabilities/README`, `departments/README`)* | **mudanca de CRITERIO** | `BL-2026-07-30-01` contou-os; `BL-2026-07-30-02` passou a escrever *"excluidos os indices"* e **nao contou** |
| **`+1`** `foundation/11-framework-specifications.md` | **mudanca de ACERVO** | `FND-11` foi criada e entrou em vigor pelo ato de 2026-07-30 |

> **Nenhuma das duas baselines declarou que o criterio mudou.** O numero caiu de 73 para 71
> enquanto o acervo **crescia**, e as duas causas — uma de metodo, uma de conteudo — foram
> **somadas dentro de um unico valor**, com sinais opostos, o que as tornou mutuamente
> invisiveis. **`0` fontes normativas foram alteradas em qualquer das duas medicoes**, e essa
> parte sempre esteve certa. Achado **`RD-61`**.

## 4. `RD-56` — `TPL-carta-produto` **1.1.0**, ✅ FECHADO

| O que faltava | O que a emenda faz |
|---|---|
| `capabilities` no frontmatter da instancia | **Acrescentado** — `FND-09` E-17 o declara **atributo minimo** de `PRO`, e `FND-04 §6` faz do vinculo **pre-condicao universal I** |
| Os **cinco** campos de `FND-10 §2.2` | **Acrescentados** na instancia *(e no proprio template)*: `resumo` · `perfil_contexto` · `confidencialidade` · `revisor` · `ratificacao` |
| Secao de **Capabilities consumidas** | **Criada** — §8, com a regra de que frontmatter e secao **nao podem divergir** |
| Secao de **interfaces** | **Criada** — §9, com direcao, contraparte e natureza da evidencia |

**Rito: `C2`, aprovador `DEP-GOV`** por `FND-09 §8.2`, linha `TPL`, `ratificacao` **nao exigida**
— **precedente literal `TPL-spec` 1.0.0 → 1.1.0**, aplicado no acervo pelo mesmo fundamento.
**133 → 183 linhas**, secoes contiguas **1 a 14**, `sha256`
`d77682c6b3b525248af347b747b734e9af14a7341398de0a37b91da99ff34964`.

> **A emenda converge com a Carta candidata `PRO-medally`, que ja trazia §8 e §9 com esses
> nomes** — a Carta *"excedia o template"* porque o template e que estava aquem da norma.
> **Nenhuma Carta de Produto existente e alcancada: `0` existem.**

## 5. Prova de nao-escrita — manifesto que reproduz, **calculado e nao redigido**

| Item | Estado |
|---|---|
| **Manifesto de abertura** | **531** arquivos · `2a9a2725701a6e7859010419269b4ad451d9eafa46d1966c62f348d21311600e` · tomado **antes de qualquer leitura de conteudo** |
| **Calibracao do instrumento, antes do uso** | ✅ **4 de 4** contra um delta **fabricado** sobre controle conhecido: **novo de conteudo**, **novo volatil**, **alterado** e **removido** — cada um detectado e **classificado** corretamente. **`0` escritas no repositorio externo para calibrar** |
| **Manifesto de fechamento** | **531** arquivos · `48c5e92e62b6d49ffa4f56f9e7ae983d6a58467eb4a4183030d905b615e2d26c` · **delta de 52 caminhos, calculado e atribuido** — §9.1 |
| **Executavel sobre o repositorio externo** | ✅ `ferramentas/manifesto.sh tomar` e `comparar` — somente `find` e `sha256sum`; **nenhum `git`, nenhum script do repositorio, nenhuma escrita** |

**O que o instrumento corrige, em relacao a 1.13.4:**

| # | Defeito do recorte | Correcao |
|---|---|---|
| 1 | **A prova deixou de ser o manifesto e virou lista escrita a mao** — e a lista omitiu **3 de 4** arquivos novos | O delta e **calculado**. Nao ha passo em que alguem redija a lista |
| 2 | **`__pycache__/` e `*.pyc` nao estavam nem incluidos nem excluidos** — caiam num limbo sem declaracao | Entram no manifesto e no delta, e sao **CLASSIFICADOS como volateis**. **Classificar nao e descartar** |
| 3 | A comparacao ingenua levava minutos e **convidava a desistir da prova** | Passe unico em `awk`; o delta de **531** caminhos sai em segundos |

> **O instrumento separa o que a 1.13.4 misturou:** o manifesto prova **o que** mudou; **quem** e
> **por que** sao o passo de atribuicao de §1.2, que usa `mtime` e cadeia gerador→gerado. **Sao
> duas provas, e cada uma diz o que sabe.**

## 6. As tres minutas — **preparadas e NAO aplicadas**

Vivem em `_missao-1-13-4-1-2026-07-31/minutas/`, **fora do acervo** — candidato dentro da raiz
quebra a reproducao da baseline, que e `RD-53`. **Nenhuma tem numero de `RFC` ou `ADR`
atribuido**: reservar numero sem aplicar abre buraco no contador oficial, defeito da familia de
`RD-32`.

| Minuta | Fecha | Classe do rito | Norma superada | Custo de reversao |
|---|---|---|---|---|
| **A** — classe de admissao de existencia em `G3` | **`RD-54`** e **`RD-55`** | **`C2 · Tipo 2`** | `ADR-0007 §5.3`, condicao `G3`, **so quanto a lista de classificacoes** | **Baixo, medido:** 1 `ADR` *(`O9`)* · 1 linha de `ADR-0007` · a regra de reclassificacao · 1 entrada em `§7` · os indices `M3`. **`0` artefatos historicos editados** |
| **B** — independencia de fornecedor | O critério de aferição de `ADR-0005` | **`C3 · Tipo 1`** | `ADR-0005` **quanto ao criterio**, nunca quanto a proibicao; alcanca `AC-03` e a linha *Autoverificacao* de `§10.x` | **Alto:** **19** `FIT` passariam a declarar conformidade por criterio que a norma nova nao reconhece; **`0` artefatos invalidados** *(a regra e prospectiva)* |
| **C** — superacao de ato por evidencia posterior | A ausencia de caminho de revisao de ato | **`C3 · Tipo 1`** | **Nenhuma revogada** — a lacuna e de **omissao**. `ADR-0012` permanece integro e vira **pre-condicao** do caminho | **Medio e assimetrico:** reverter a emenda custa 1 `ADR`; **reverter uma superacao ja feita e impossivel** — dai `SA-5`. **`0` atos superaveis hoje** |

### 6.1 A autoverificacao, medida **pelos dois criterios** — minuta B

Medido por ferramenta sobre os **194** artefatos:

| Criterio | Definicao | Autoverificacoes | Base |
|---|---|---|---|
| **C-1** — divergencia de campo *(vigente)* | `autor` ≠ `revisor` | **`0`** | **137** artefatos declaram os dois |
| **C-2** — independencia de fornecedor *(proposto)* | autor e revisor sao papeis do **mesmo executor** | **`130`** | os mesmos **137** |
| **Diferenca** | | **`130`** | |

**Os `7` que sobrevivem ao criterio C-2 sao os sete atos do Soberano** — `MSG-2026-0001` a
`MSG-2026-0007`, `autor: SOBERANO`. **Sao os unicos artefatos do acervo com autor fora do
fornecedor unico**, e mesmo eles tem **revisor** dentro dele.

> **`0` e `130` medem o mesmo acervo no mesmo instante, e os dois numeros sao verdadeiros.**
> `ADR-0005` **proibe o segundo e mede o primeiro** — e foi por isso que a 1.13.4 pode reportar
> **`0` autoverificacoes** numa missao em que o mesmo agente construiu o instrumento, corrigiu-o
> apos a reprovacao e aplicou-o a si mesmo, com **10 de 10** controles conformes. **As tres
> coisas sao verdadeiras ao mesmo tempo; a terceira torna as duas primeiras nao verificaveis por
> terceiro.**

## 7. `Q1` — o texto literal, extraido e nao interpretado

> **Esta secao nao escolhe entre `L1` e `L2`, nao recomenda e nao pondera. `Q1` e decisao do
> Fundador.**

### 7.1 O texto literal da decisao 7 de `PT-2026-009 §1`

Linha integral da tabela *"As sete decisoes fixadas, e o que cada uma produziu"*:

> | **7** | Via futura e **`S1` com Produto real** *(`nXtrack`)*; **`S2` deferida** | **Registrado e NAO executado.** A minuta declara em `VII` que **nenhum Produto ou `Spec` e criado ou tornado criavel**. **`RD-33` segue bloqueante** | [PS-2026-013 §7](pacote-soberano-2026-07-30-consolidado.md) |

**Contexto imediato — a decisao que a precede na mesma tabela:**

> | **6** | Estender `RD-37` a `DEP-OPS`, `DEP-GRW`, `DEP-TLS` **antes do ato** | **Feito**, no **menor rito competente**: `ADR-0025` `C2` **sem RFC**, com as duas condicoes de `FND-04 §2` verificadas | [PS-2026-012](pacote-soberano-2026-07-30-rd-37.md) |

### 7.2 Fato medido: **a condicao nao esta em `PT-2026-009 §1`**

**A palavra `comercial` NAO ocorre em `governance/relatorio-transicao-2026-07-30-convergencia.md`
— `0` ocorrencias no arquivo inteiro.** A oracao condicional que gera `Q1` esta em **outro
documento**, que a linha 7 aponta como destino:

**`PS-2026-013 §7`, linha `S1`/`S2`, texto literal:**

> | **`S1`** / **`S2`** | **Via decidida, execucao deferida** | O Soberano fixou **`S1`, com Produto real — `nXtrack`, se seguir sendo o primeiro produto comercial** — e **`S2` deferida** ate surgir necessidade observada de `Spec` nao vinculada a Produto. **Este ato nao cria Produto**, e a missao proibe cria-lo |

### 7.3 Onde cada artefato atribui a citacao

| Artefato | Atribui a | Confere? |
|---|---|---|
| `ADR-0026` `E8` | **`PS-2026-013 §7`** | ✅ |
| `RFC-0021` §5 | **`PS-2026-013 §7`**, decisao 7 de `PT-2026-009 §1` | ✅ **as duas fontes nomeadas** |
| `PS-2026-014`, bloco de abertura | **`PT-2026-009 §1`**, *"registrada em `PS-2026-013 §7`"* | ⚠️ a oracao citada esta **so** na segunda |
| `PS-2026-014 §7` `Q1` · `PT-2026-011 §4` · `artifact-registry §2` · `governance/README` | **`PT-2026-009 §1`** | ⚠️ **quatro atribuicoes a um texto que nao esta la** |

> **Isto nao decide `Q1` e nao move a questao em direcao a `L1` ou a `L2`.** A oracao existe, foi
> escrita, e esta registrada num pacote soberano submetido ao Fundador. O que se registra e
> **onde ela esta** — porque `Q1` pergunta como ler **um texto**, e quatro artefatos apontam
> para o lugar errado ao busca-lo. Achado **`RD-64`**.

## 8. Achados novos desta missao

| # | Achado | Severidade | Estado |
|---|---|---|---|
| **`RD-60`** | **O recorte enumerado de `PS-2026-014 §2.2` ficou 3 caminhos curto, e o total de fechamento nao foi medido.** Mudaram **19** caminhos na janela; o pacote enumerou **16**. **Os 15 alterados batem exatamente**; dos **4** arquivos novos so **1** foi enumerado. Os omitidos: `tests/test_paginas_felipe.py`, `tests/__pycache__/test_paginas_felipe…pyc` e `ferramentas/__pycache__/montar_paginas_felipe…pyc`. E o total de fechamento **medido e 554**, contra **551** publicado como *"observado"* — `551 = 550 + 1` e aritmetica sobre o unico novo enumerado | **Media** | ⚠️ **ABERTO.** **A conclusao do pacote sobrevive**: os 3 omitidos pertencem a **mesma** linha de trabalho paralela, **`0`** lidos ou executados pela missao, e **`0` bytes** continuam atribuiveis a ela. **O que nao sobrevive e a completude da enumeracao.** Corrigivel **so por ato ou instrumento novo** — `PS-2026-014` **nao e editavel** por esta missao. **Instrumento novo entregue:** §5 |
| **`RD-61`** | **A passagem `73 → 71` fontes normativas soma duas mudancas de naturezas opostas num unico numero:** **`−3`** por **mudanca de criterio** *(os tres indices deixaram de ser contados)* e **`+1`** por **mudanca de acervo** *(`FND-11` criada)*. **Nenhuma das duas baselines declarou a mudanca de criterio**, e os sinais opostos tornaram as duas causas mutuamente invisiveis | Baixa | ✅ **EXPLICADO com evidencia** *(§3.4, medido nas duas copias pelos dois criterios)*. **As baselines NAO foram editadas** (`BL-02`). Dono **DEP-GOV**; gatilho *"proxima baseline"*: declarar o **criterio** ao lado do numero |
| **`RD-62`** | **`FND-10 §2.2` intitula *"Extensao do contrato — cinco campos novos"* e a tabela imediatamente abaixo tem SEIS linhas** — `resumo`, `perfil_contexto`, `confidencialidade`, `revisor`, `ratificacao` e **`projecao_de`**. Todo o acervo cita *"os cinco campos"*, e a leitura sobrevive porque `projecao_de` e **condicional**; mas o titulo e a tabela **nao concordam** | Baixa | ⚠️ **ABERTO e NAO corrigido.** `FND-10` e **fundacional em vigor**: editar altera `H-N` e **exige ato** (`LV-04`, `IR-01`). **Fora da lista desta missao** — declarado, nunca corrigido em silencio. Familia de `RD-46` |
| **`RD-63`** | **Os 19 templates declaram `aprovador: SOBERANO` no proprio frontmatter, e `FND-09 §8.2`, linha `TPL`, declara `DEP-GOV`.** A pratica do acervo segue a **norma**, nao o campo: `TPL-spec` **1.1.0** foi emendado e aplicado *"aprovado por DEP-GOV (`FND-09 §8.2` linha `TPL`)"*, e esta missao emendou `TPL-carta-produto` pelo mesmo fundamento | Baixa | ⚠️ **ABERTO e NAO corrigido.** Corrigir alcanca **19 arquivos** e e rito proprio; **fora da lista**. **Declarado aqui porque esta missao exerceu a norma contra o campo**, e exercer sem declarar seria o defeito |
| **`RD-64`** | **A oracao condicional que gera `Q1` — *"se seguir sendo o primeiro produto comercial"* — nao esta em `PT-2026-009 §1`.** Ela esta em **`PS-2026-013 §7`**. **`0` ocorrencias** da palavra `comercial` no arquivo de `PT-2026-009`. **Quatro** artefatos vigentes atribuem a citacao a `PT-2026-009 §1`; `ADR-0026` e `RFC-0021` atribuem corretamente | **Media** | ⚠️ **ABERTO.** **Nao altera `Q1` nem o seu merito** — o texto existe e esta num pacote submetido. Alcanca `PS-2026-014`, `PT-2026-011` *(nao editaveis por esta missao)* e duas projecoes `M3`. Dono **DEP-GOV**; gatilho *"ato que resolver `Q1`"* |

## 9. Provas de fechamento

| # | Prova | Resultado |
|---|---|---|
| `F1` | **Baseline anterior reproduzida antes da escrita** | ✅ **194 · 56.854 · `b355e227…75bf`**, e **reconferida na copia datada** |
| `F2` | **Comando corrigido reproduz em execucoes independentes** | ✅ **3 de 3**, hash identico nos 64 digitos |
| `F3` | **`BL-2026-07-30-01` reproduz pelo comando corrigido** | ✅ **185 · 54.190 · `3d8dbea0…84da`**, sobre a copia em que o comando publicado dava **198** |
| `F4` | **Item 0 — arquivos atribuidos a PROCESSO** | ❌ **14 de 19.** **5 NAO ATRIBUIVEL** — horario exato, produtor nao nomeavel. `0` sobra silenciosa: os 19 estao classificados. §1.2.1 |
| `F5` | **Escritor concorrente no acervo** | ✅ **nenhum** |
| `F6` | **Instrumento de `H-A`/`H-N`/`H-P` calibrado antes do uso** | ✅ **8 de 8** controles publicados reproduzem |
| `F7` | **Instrumento de manifesto calibrado antes do uso** | ✅ **4 de 4** classes de delta detectadas e classificadas |
| `F8` | **Cartas candidatas — `H-N` invariante · `IR-09` · `O4` de dois campos** | ✅ **3 de 3** em cada prova |
| `F9` | **Bytes escritos no repositorio externo, atribuiveis a esta missao** | ✅ **`0`** — e o manifesto **NAO reproduz**: **52** caminhos alterados, **`0`** novos, **`0`** removidos, **52 de 52 atribuidos** a execucao de `explorar.py` e a uma sessao de desenvolvimento. §9.1 |
| `F10` | **Bytes do repositorio externo admitidos no acervo** | ✅ **`0`** |
| `F11` | **Fundacionais, `ADR`, `MSG`, `FIT`, `PT`, historicos e baselines editados** | ✅ **`0`** — §9.2 |
| `F12` | **Pacote da 1.13.4 alterado** | ✅ **`0` bytes** — §9.2 |
| `F13` | **Minutas aplicadas** | ✅ **`0` de 3** |
| `F14` | **Nova baseline reproduzivel** | ✅ **`BL-2026-07-31-02`** — [catalogo §10.11](artifact-registry.md) |
| `F15` | **Lease vivo do inicio ao fim** | ✅ `fencing_token: 1`, adquirido antes da primeira escrita, liberado no fechamento |

### 9.1 O manifesto do repositorio externo — **o instrumento reproduz; o repositorio, nao**

| Campo | Valor |
|---|---|
| Arquivos no manifesto | **531** nos **dois** instantes *(exclui `.git/`, `.mypy_cache/` e `.pytest_cache/`, **declarado**)* |
| `sha256` do manifesto de **abertura** | `2a9a2725701a6e7859010419269b4ad451d9eafa46d1966c62f348d21311600e` |
| `sha256` do manifesto de **fechamento** | `48c5e92e62b6d49ffa4f56f9e7ae983d6a58467eb4a4183030d905b615e2d26c` |
| **Delta abertura → fechamento** | **52 caminhos: `0` novos · 52 alterados · `0` removidos** |
| Total de arquivos | **554 → 554** — coerente com `0` novos e `0` removidos |
| Veredito do instrumento | **manifesto NAO reproduz**, e o delta esta **calculado** |

> **A distincao que a 1.13.4 nao tinha, e que muda o significado da prova.** O que se restaura
> **nao e um manifesto identico** — sobre repositorio vivo isso nao existe, e persegui-lo foi o
> que empurrou a 1.13.4 para a lista escrita a mao. **O que reproduz e o INSTRUMENTO**: mesma
> regra de exclusao declarada, mesmo calculo, mesma classificacao, executavel por qualquer um a
> qualquer momento, e **calibrado contra controle conhecido antes do uso**. **O delta e a saida,
> nao o fracasso.**

#### 9.1.1 Os 52 caminhos, atribuidos

| Bloco | Qtd | Janela | Processo atribuido |
|---|---|---|---|
| `sessoes-convidado/**` — dados de sessao, auditoria, transcricao, veredito, credenciais | **44** | **10:01:58 → 10:03:39** | **Execucao de `ferramentas/explorar.py`.** O primeiro caminho a mudar e o marcador `sessoes-convidado/.exploracao`, cujo texto literal e *"Pasta descartavel criada por `ferramentas/explorar.py`. Tudo sintetico."* |
| `nucleo/teleconsulta.py` · `nucleo/rotas.py` · `ferramentas/servidor.py` · `public/sala.html` · `public/sala.js` · `public/sala.css` · `tests/test_teleconsulta.py` | **7** | **10:10:40 → 10:17:01** | **Sessao de desenvolvimento de produto**, em ordem sequencial: nucleo → rotas → servidor → front → teste |
| `nucleo/__pycache__/teleconsulta.cpython-314.pyc` | **1** *(volatil)* | 10:11:59 | **Importacao** de `nucleo/teleconsulta.py`, 79s apos a edicao dele |

**`0` caminhos nao atribuiveis.** Nenhum dos 52 e atribuivel a esta missao: **`0` scripts do
repositorio foram executados por ela**, e as suas unicas acoes ali foram `find`, `sha256sum`,
`stat`, `ls`, `grep` e `git --no-optional-locks` — **todas de leitura**. **A suite nao foi
rodada** — rodar e escrever. **O SSC+ tambem foi apenas lido**, e so para medir o caso vivo da
minuta C.

> **O limite continua declarado:** `mtime` e a cadeia de dependencia provam **quando** e **por
> que**; **nao provam QUEM** (`PI-10`, `LV-12`).
>
> **E o repositorio continuou mudando depois do manifesto de fechamento** — medido: mais
> caminhos com `mtime` posterior, ja fora da janela. **Perseguir a arvore viva e a armadilha que
> `RD-59` nomeia**, e a resposta correta e a que a 1.13.4 acertou: **fixar o instante e declarar
> o delta**, nao reeditar objetos ja medidos. **Segunda missao consecutiva em que o candidato se
> move dentro da propria missao** — a evidencia empirica de `RD-59` deixa de ser um caso e passa
> a ser um padrao.

### 9.2 O conjunto de mudanca no acervo — enumerado, nao afirmado

**Alterados — 4:**

| Artefato | Natureza da mudanca |
|---|---|
| `foundation/templates/TPL-carta-produto.md` | **Fonte normativa** — emenda `C2`, `1.0.0 → 1.1.0`, achado `RD-56`. **A unica fonte normativa alterada** |
| `governance/artifact-registry.md` | **Projecao `M3`** — reconciliacao `CV-04`/`RG-03`: §2, §4, §7, §9, §10 e o historico |
| `governance/README.md` | **Projecao `M3`** — supressao da duplicata de `RD-58`, baseline e pendencias |
| `README.md` | **Projecao `M3`** — estado, baseline e historico |

**Criados — 1:**

| Artefato | Natureza |
|---|---|
| `governance/relatorio-transicao-2026-07-31-manutencao-instrumentos.md` | **Este relatorio** — o registro que `CV-04` exige da propria mudanca |

**Removidos: `0`.** Nenhum outro arquivo do acervo foi tocado — conferido por `sha256`
**arquivo a arquivo** contra a copia datada, e nao por agregado.

## 10. O que esta missao NAO fez

| # | Nao feito | Por que |
|---|---|---|
| 1 | **Nenhum candidato julgado, nenhum Produto admitido, nenhuma `Spec` criada** | Limite expresso. **`RD-33` permanece bloqueante** e **`Q1` continua precedendo o ato** |
| 2 | **Nenhum ato emitido, nada ratificado** | Limite expresso |
| 3 | **Pacote da 1.13.4 nao alterado** | Limite expresso. Ele fica **suspenso, nao descartado** — e `RD-60` e `RD-64` sao registrados **fora dele** |
| 4 | **`ADR-0007` nao emendado; `ADR-0005` nao emendado; nenhum caminho de superacao de ato instituido** | As tres sao **minutas**, e aplicar minuta e vedado |
| 5 | **As tres Cartas `1.2.0` nao aplicadas** | Emendar Carta ratificada **exige ato novo** — `R1` de `FIT-2026-018`, precedente `DEP-QAR` 1.2.0 |
| 6 | **`RD-62`, `RD-63` e o `aprovador` dos 19 templates nao corrigidos** | **Fora da lista.** Correcao silenciosa e proibida, e corrigir achado nao listado seria exatamente isso |
| 7 | **Nada escrito no SSC+** | Limite expresso — **somente leitura**, e so para medir o caso vivo da minuta C |
| 8 | **`RD-33`, `RD-47`, `RD-48`, `RD-43`, `RD-13`, `RD-36` mantidos abertos** | Fora do escopo — nao se fecham por inferencia |
| 9 | **Nenhum contador de `RFC`/`ADR` incrementado** | As minutas **nao tem numero**. Reservar sem aplicar abriria buraco no contador |

## 11. Decisao

**`BLOCKED`.**

**O Item 0 reprova.** Dos **19** caminhos medidos, **14** estao atribuidos a processo nomeado e
**5 sao NAO ATRIBUIVEL** — §1.2.1. A regra do Item 0 e literal e nao admite compensacao:
*"Arquivo NAO ATRIBUIVEL … encerra em BLOCKED"*.

| Grupo | Qtd | Caminhos |
|---|---|---|
| **ATRIBUIDO** | **14** | 4 saidas de `gravar_video_institucional.py` · 2 de `montar_pagina_video.py` · 6 de `montar_paginas_felipe.py` · 2 caches de bytecode do CPython |
| **NAO ATRIBUIVEL** | **5** | `ferramentas/gravar_video_institucional.py` · `ferramentas/montar_pagina_video.py` · `ferramentas/montar_paginas_felipe.py` · `tests/test_paginas_felipe.py` · `docs/demonstracao/felipe/links.json` |

**Os outros seis criterios NAO compensam, e estao listados aqui apenas para que o Fundador saiba
o que ja existe e o que teria de ser refeito**, nunca para atenuar o `BLOCKED`:

| # | Criterio | Estado |
|---|---|---|
| 2 | Baseline reproduzindo em duas execucoes com hash identico | ✅ **3 execucoes**, 64 digitos identicos |
| 3 | Divergencias de catalogo e contagem explicadas por evidencia | ✅ `RD-49` · `RD-57` · `RD-58` · **73 → 71** decomposto |
| 4 | Cada minuta com norma superada, custo de reversao e classe do rito | ✅ **3 de 3** |
| 5 | Autoverificacao pelos dois criterios, com a diferenca em numero | ✅ **`0`** e **`130`**, diferenca **`130`** |
| 6 | Lease vivo do inicio ao fim | ✅ tokens **1 → 2 → 3**, cada reabertura com token maior |
| 7 | Nova baseline reproduzivel | ✅ `BL-2026-07-31-02` |
| 1 | **Todos os caminhos medidos atribuidos, sem sobra silenciosa** | ❌ **REPROVA — 5 NAO ATRIBUIVEL** |

### 11.1 Por que o veredito mudou duas vezes, e o que cada mudanca corrigiu

**Este relatorio decidiu tres vezes. As duas primeiras estavam erradas, por motivos diferentes, e
ficam registradas em vez de apagadas.**

| Emissao | Veredito | O que estava errado |
|---|---|---|
| 1ª | **`ADJUST`** | **Erro de classificacao.** Tratou `RD-49`, as tres minutas e `Q1` como *"impedimentos"*. Os tres sao **desfechos projetados**: a determinacao pediu as minutas *"preparadas e nao aplicadas"*, o rito de `RD-49` termina em candidato aguardando ato *(precedente `DEP-QAR` 1.2.0)*, e `Q1` e do Fundador por definicao. **Tratar ponto de parada obrigatorio como trabalho inacabado confunde obediencia com falha** |
| 2ª | **`READY-FOR-RATIFICATION`** | **Erro de forma da resposta ao Item 0.** Afirmou *"19 de 19 atribuidos"* — mas isso respondia em **CONTAGEM**. O Item 0 pede **ATRIBUICAO a processo e horario**, e coerencia de linha de trabalho **nao e processo**. Os **5** do Grupo B tinham horario e **nao tinham produtor nomeavel** |
| **3ª** | **`BLOCKED`** | — |

**O que a segunda emissao acertou e continua valendo:** `ADJUST` era mesmo o veredito errado, e
pelo motivo que ela deu. **O `BLOCKED` nao restaura o `ADJUST`** — ele reprova por um portao
diferente, que a segunda emissao havia dado por vencido sem te-lo exercido na forma escrita.

**Por que os 5 nao podem ser reclassificados.** Sao **tematicamente coerentes** com a mesma
sessao de produto que produziu os 14 do Grupo A. **Coerencia tematica e inferencia plausivel**, e
a determinacao veda explicitamente converte-la em atribuicao. Converter seria repetir, dentro da
missao que o mediu, o vicio de `RD-60`: publicar como medido o que foi suposto.

**E o teto nao e do metodo — e do candidato, medido:** as 19 mudancas da janela sao **trabalho
nao commitado** *(4 em ` M`, 1 em `??`, ultimo commit que as toca de **2026-07-30**, anterior a
janela)*, com **`0` stash e `0` artefato de editor**. **Sem commit nao existe registro de
autoria**, e nenhuma ferramenta recupera depois o que nao foi gravado na hora. **Nenhuma missao
futura consegue atribuir esses 5 sem que o candidato passe a commitar** — o que faz do
`BLOCKED` um fato sobre a evidencia disponivel, nao sobre o esforco empregado.

### 11.2 O que `READY-FOR-RATIFICATION` teria significado — e que instrumento nenhum esta consertado

**Declarado a pedido do Fundador, e vale mesmo com o veredito em `BLOCKED`**, porque a segunda
emissao usou o termo sem defini-lo e isso e uma divida propria:

> **`READY-FOR-RATIFICATION`, nesta missao, significaria exatamente duas coisas: diagnostico
> completo e minutas redigidas. Nada alem disso.**

**Minuta redigida nao e norma.** Enquanto nao houver ato do Fundador:

| Instrumento | Estado real, hoje |
|---|---|
| **`G3` do `ADR-0007`** | **Segue sem a classe.** Continuam as quatro classificacoes de conteudo; **nao existe `G0`, nao existe `RECOGNIZE`**, e o proximo candidato tera de sair por eliminacao outra vez, com o mesmo registro falso. **`RD-54` e `RD-55` abertos** |
| **Metrica de independencia** | **Segue a antiga.** `ADR-0005` continua aferindo por **divergencia de campo**, e a linha *Autoverificacao* continua podendo publicar **`0`** onde a medicao por fornecedor da **`130`**. **A medicao dos dois criterios existe; a norma que a exige, nao** |
| **Superacao de ato** | **Segue sem caminho.** Ato emitido continua sem mecanismo de revisao quando a prova o contradiz. **`SA-1` a `SA-6` sao texto numa pasta fora do acervo** |

**O que ESTA consertado e em vigor** — porque dependia so de `DEP-GOV` e nao de ato: **`RD-53`**
*(comando da baseline, com os tres portoes, provado em 3 execucoes)*, **`RD-56`**
*(`TPL-carta-produto` **1.1.0**, `C2`, `ratificacao` nao exigida, precedente `TPL-spec` 1.1.0)*,
**`RD-57`** e **`RD-58`**. **`RD-49` NAO esta consertado:** os tres candidatos estao medidos e
**a norma vigente continua declarando 437 · 443 · 424**.

> **O pacote da 1.13.4 continua suspenso e intacto — `0` bytes.** O que este `BLOCKED` diz e que
> **a cadeia de custodia do primeiro exercicio do portao nao fecha**: cinco caminhos mudaram no
> candidato durante a janela e **nao ha como dizer o que os escreveu**. Isso **nao acusa a 1.13.4
> de ter escrito** — nao ha evidencia disso, e o ferramental dela nao produz aqueles arquivos.
> **Diz que a pergunta ficou sem resposta**, e o Item 0 foi escrito exatamente para que ficar sem
> resposta tivesse consequencia.

### 11.3 O que desbloqueia

| # | Caminho | Quem |
|---|---|---|
| 1 | **Declarar, por ato, o que produziu os 5 caminhos** — o unico com autoridade para converter o que nao esta gravado em fato do registro | **SOBERANO** |
| 2 | **Aceitar o `BLOCKED` e exigir do candidato que passe a commitar antes da proxima admissao**, tornando a atribuicao possivel por `git` em vez de por `mtime` | **SOBERANO** |
| 3 | **Emendar o Item 0** para distinguir *atribuir a processo* de *atribuir a linha de trabalho*, fixando qual dos dois o portao exige | **SOBERANO** |

**`Q1` continua bloqueante e intacta. `RD-33` continua bloqueante. Nenhuma minuta foi aplicada.**

## 12. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Missao anterior | [PT-2026-011](relatorio-transicao-2026-07-31-admissao-medally.md) — **suspensa, nao descartada** |
| Pacote suspenso | [PS-2026-014](pacote-soberano-2026-07-31-medally.md) — **`0` bytes alterados** |
| Achados fechados | **`RD-53`** · **`RD-56`** · **`RD-57`** · **`RD-58`** |
| Achados corrigidos ate o limite da missao | **`RD-49`** — tres candidatos `1.2.0` medidos, **nao aplicados** |
| Achados novos | **`RD-60`** · **`RD-61`** · **`RD-62`** · **`RD-63`** · **`RD-64`** — [catalogo §7](artifact-registry.md) |
| Minutas | `_missao-1-13-4-1-2026-07-31/minutas/` — **A**, **B** e **C**, **fora do acervo** |
| Instrumentos | `_missao-1-13-4-1-2026-07-31/ferramentas/` — `baseline.sh` · `manifesto.sh` · `hashes.sh` |
| Baseline de abertura | `BL-2026-07-31-01` — **reproduzida** |
| Baseline de fechamento | **`BL-2026-07-31-02`** — [catalogo §10.11](artifact-registry.md) |

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-31 | DEP-GOV | Relatorio da **Missao 1.13.4.1**. **Item 0 REPROVA: 14 de 19 caminhos atribuidos a processo nomeado, 5 NAO ATRIBUIVEL** — nenhuma mudanca da janela foi commitada, e sem commit nao ha registro de autoria. **`0` escritores concorrentes no acervo.** **`RD-53` fechado por instrumento novo** — o defeito era do comando, e `BL-2026-07-30-01` **reproduz nos 64 digitos**. **`RD-56`, `RD-57` e `RD-58` fechados**; **`RD-49`** corrigido em tres candidatos **nao aplicados**. **Tres minutas** preparadas e **`0`** aplicadas — **nenhum instrumento delas esta consertado ate ato**. Autoverificacao pelos **dois** criterios *(`0` e `130`)*. **Cinco achados novos** — `RD-60` a `RD-64`. O criterio **"17 de 17"** foi **substituido por correcao** *(§1.6)*: o `17` nao e derivavel de fonte alguma. Decisao **`BLOCKED`** — §11 registra as **tres** emissoes do veredito e por que as duas primeiras estavam erradas. |
