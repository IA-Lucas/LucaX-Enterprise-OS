# `docs/` — sede de resgate da estacao espelho

> **Isto NAO e artefato do acervo.** Nada aqui tem `id`, versao de sequencia, entrada no
> catalogo ou autoridade normativa. E registro operacional resgatado de uma maquina que
> deixou de existir.

## Por que esta pasta nasceu

A estacao **espelho de leitura** (secundaria) foi encerrada em **2026-08-09**. Ate esse
dia, um conjunto de registros vivia **so** em `C:\Users\lucas\.claude\` — a sede de
memoria local do agente — e em `%TEMP%`. **Nenhum dos dois viaja para a maquina
principal.** Por decisao do Fundador no fechamento da estacao, o conteudo foi copiado
para ca e commitado, porque o repositorio e o unico caminho que atravessa a troca de
maquina.

O conteudo esta em [`memoria-da-estacao-espelho/`](memoria-da-estacao-espelho/), **copia
byte-identica** do original, com um indice em
[`memoria-da-estacao-espelho/INDICE.md`](memoria-da-estacao-espelho/INDICE.md). Os
handoffs ficam em [`handoffs/`](handoffs/).

## ⚠️ O custo que esta pasta cria, e ele e real

**`docs/` e entrada de raiz NAO declarada.** O instrumento de baseline vigente,
**`IR-BL/3`**, mede por **lista fechada positiva** e **para com erro** diante de entrada
de raiz que nao conheca — e o portao de raiz e o achado **`RD-53`**. A lista `NAO_ACERVO`
vigente e `.obsidian` · `_SAIDA-COMPANY-OS` · `CLAUDE.md` · `.git` · `.gitattributes`, e
`docs` **nao esta nela**.

**Consequencia declarada:** enquanto `docs` nao entrar na lista, `baseline.sh` **vai
parar com erro** na proxima medicao da principal. **Isso e o portao funcionando, nao
falha** — e a primeira tarefa da principal e declarar `docs` em `NAO_ACERVO` e reemitir
a baseline.

**Este custo ja era conhecido, e foi assumido de olhos abertos.** Em **2026-08-08** o
Fundador enfrentou exatamente esta questao com `.scratch/NUNCA-APAGAR.md` e decidiu
**mudar a sede, nao a regra**: a lista saiu do acervo, `NAO_ACERVO` ficou intacta,
nenhum `.gitignore` foi criado. **A decisao de 2026-08-09 e diferente porque o fato
mudou** — naquele dia a sede de memoria continuaria existindo; neste dia a maquina
inteira acaba. Entre **quebrar um portao que avisa alto** e **perder o conteudo em
silencio**, o Fundador escolheu quebrar o portao. A escolha esta registrada aqui para
que ninguem a leia depois como descuido.

Escolheu-se `docs/` e nao `.scratch/` por dois motivos: cria **uma** entrada de raiz nova
em vez de reabrir uma decisao ja fechada, e a quebra e **ruidosa** — a baseline para e
avisa. Guardar sob um diretorio ja declarado (`memory/`, por exemplo) esconderia
nao-artefatos dentro do acervo e mudaria contagem de artefato e de linha **em silencio**,
que e pior.

## O que fazer com isto na principal

Nao adotar como sede definitiva. O conteudo de `memoria-da-estacao-espelho/` e **material
de origem** para a **tarefa 3** do
[`pacote-para-a-principal-m02.md`](memoria-da-estacao-espelho/pacote-para-a-principal-m02.md)
— reescrever os tres registros frageis em sede duravel e catalogada. Quando essa tarefa
fechar, esta pasta vira historico e pode ser reavaliada.

Ate la, **ela e o unico exemplar** de tudo que contem.
