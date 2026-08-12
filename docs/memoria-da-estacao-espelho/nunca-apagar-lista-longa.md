---
name: nunca-apagar-lista-longa
description: Lista NUNCA APAGAR com os fundamentos medidos de cada item (decisoes do Fundador de 2026-08-08) — versao longa da custodia resumida em nunca-apagar-custodia
metadata: 
  node_type: memory
  type: project
  originSessionId: 4f36ccd0-395f-40d8-99ad-aec9e6ec605f
  modified: 2026-08-09T01:43:32.658Z
---

# NUNCA APAGAR — lista viva, decisoes do Fundador de 2026-08-08

> ## Sede desta lista, corrigida em 2026-08-08
>
> Nasceu em `.scratch/NUNCA-APAGAR.md` do `LucaX-Enterprise-OS` e **saiu de la por
> determinacao do Fundador**, porque a raiz do acervo era sede errada: `.scratch` nao
> esta em `NAO_ACERVO`, entao pararia o `IR-BL/3` na proxima baseline da principal, e o
> repositorio nao tem `.gitignore`, entao aparecia untracked e colidia com o item 5 da
> propria lista. **Emendar `NAO_ACERVO` ou criar `.gitignore` eram escritas no acervo, e
> a dispensa desta maquina nao as cobre** — por isso a lista mudou de sede em vez de o
> acervo mudar de regra. Vive agora na sede de memoria, **fora do recurso fenceado** e
> **lida a cada sessao**.
>
> ⚠️ **Continua sendo copia de uma maquina so.** A sede de memoria e local
> (`C:\Users\lucas\.claude\`): a maquina PRINCIPAL nao a le. Enquanto esta for a unica
> copia, a lista segue a uma faxina de distancia de se perder — que e exatamente o risco
> que ela existe para cobrir. **Reescrever na principal continua pendente.**

**Regra de leitura, valida para tudo abaixo:** *caminho ausente significa **"esta na
principal"**, nunca "perdido"* (`CLAUDE.md`, topo). Vario item desta lista **nao esta
na maquina espelho**, e isso **nao os desqualifica** — os desqualificaria apagar por nao
ver.

---

## 1. OS 283 MB FICAM — `separacao-2026-08-02`

**DECISAO DO FUNDADOR, 2026-08-08: NUNCA APAGAR.**

**Fundamento, escrito porque sem ele a decisao vira preferencia:**

1. **E exemplar unico dos 9 `.db` do `consult`.** Dado gitignorado **nunca esteve em
   git** — nao ha reflog, nao ha objeto pendurado, nao ha remoto. Apagar aqui e apagar
   em definitivo, e nao existe segunda copia para reconciliar.
2. **Ele e a justificativa de uma remocao ja executada.** O commit **`85df749`** do
   `lucaX` removeu **271 arquivos** justificando-se *"backup datado de 283 MB cobre"*.
   **Apagar o backup derruba retroativamente a justificativa da remocao** — os 271
   arquivos deixariam de estar cobertos por algo, depois de terem sido removidos por
   estarem.

⚠️ **Medido no espelho em 2026-08-08:** `separacao-2026-08-02` tem **`0` ocorrencias
em `E:`**, arquivo ou diretorio; **`0`** `.db` sob caminho `consult`. **Esta na
principal.** Registrado justamente porque **quem so olha esta maquina nao o ve** — e o
que nao se ve e o que se apaga sem perceber.

✅ **ACHADO E MEDIDO NA PRINCIPAL, 2026-08-12 (tarefa 1 do pacote M-02):** caminho real
**`E:\LucasIA\_backups\separacao-2026-08-02`** — abre. Medido por ferramenta:
**12.783 arquivos / 273.195.090 B**. O registro de 2026-08-02 dizia **12.782 / 271.809.829**:
**os dois pares ficam registrados**, divergencia de `+1` arquivo / `+1.385.261 B` **nao
reconciliada** — nao se escolheu um numero. `.db` medidos: **8 sob `consult/` + 16 sob
`nxtrack/` = 24**; o fundamento desta entrada diz **9 do consult** — **os dois ficam**, e
apagar continua proibido.

## 2. `basckup antigo` — fica em **DECIDIR**, nao em NUNCA APAGAR, nao em apagavel

**DECISAO DO FUNDADOR, 2026-08-08: aguarda confirmacao de outra copia.**

| Item | Medido em 2026-08-08 |
|---|---|
| Caminho | `E:\basckup antigo` |
| Tamanho | **2.594 MB** — reproduz exatamente o numero do despacho |
| Conteudo | Fotos e gravacoes de celular de 2024 (`DCIM`, `Pictures`, `Movies`, `Recordings`, `Ringtones`, `Music`, `Download`…) |
| Citado por algum dos quatro repositorios | **Nao. `0` ocorrencias** |

**O fundamento, e ele e o que impede a faxina apressada:** nao ser citado por nenhum
repositorio **nao o torna lixo** — torna-o **orfao**. Se nao houver outra copia,
**apagar deixa de ser faxina e vira custodia**: destruicao de acervo pessoal
insubstituivel sob pretexto de limpeza de disco.

**Dono da decisao: o Fundador.** Enquanto estiver em `DECIDIR`, vale como **NUNCA
APAGAR** (item 7 da lista abaixo). **`DECIDIR` nao e permissao provisoria para apagar —
e proibicao provisoria de apagar.**

## 3. Destino novo do backup — gravado onde a regra vive

**DECISAO DO FUNDADOR, 2026-08-08.** Gravada em
**`E:\lucaX\.claude\rules\git-and-backup.md`**, no paragrafo do destino, logo apos a
linha 9 que ja dizia *"o destino se CONFERE antes de usar — `E:\LucasIA\` nao existe
mais"*.

- **O destino fica na maquina PRINCIPAL.**
- No espelho, a copia datada grava em **`.scratch/_backups/` do proprio repositorio**,
  **declarado TEMPORARIO**.
- **Nao repor `_backups\` na raiz de `E:`** — segunda sede diverge.

**O precedente que sustenta a proibicao, e ele e medido — e os dois enunciados ficam
lado a lado, por decisao do Fundador em 2026-08-08:**

- `sensor_lei5_juiz.py` ficou com **190 linhas de um lado e 130 do outro** por ter duas
  sedes.
- A propria regra do `lucaX` registra o mesmo defeito como **divergencia de 60 linhas
  entre duas copias**.

**Provavelmente descrevem o mesmo evento, e os numeros nao coincidem. Nenhum dos dois
foi descartado:** reconciliar exige as duas copias, e elas nao estao no espelho.
**Escolher um sem elas seria inventar reconciliacao.** A reconciliacao e trabalho para a
maquina PRINCIPAL.

---

## A LISTA DO NUNCA APAGAR

| # | Item | Estado no espelho, medido 2026-08-08 |
|---|---|---|
| 1 | **`separacao-2026-08-02`** — 283 MB, exemplar unico dos 9 `.db` do `consult` | **Ausente → na principal** |
| 2 | **Os 4 backups do `Research`** | ✅ **Presentes, e sao 4:** `_backups-F11-2026-08-03` · `_backups-F12-2026-08-03` · `_fabrica\_backups` · `_fabrica\skills\backup-datado`. ⚠️ Somam **~0,2 MB** aqui — sao cascas, nao o volume |
| 3 | **Os 2 backups do `SSC-Plus`** | ⚠️ **Achei 1:** `06_p1a\evidencias\backups`. **O segundo esta na principal** — nao procurar aqui e concluir que nao existe |
| 4 | **`backup-99freelas` do `lucaX`** | ✅ **Presente**, e e **arquivo**, nao diretorio: `My_WorkSpace\Meus_projetos\operacao-freelancer\perfil\backup-99freelas-antes-perfil-hibrido-2026-07-22.md` |
| 5 | **Qualquer coisa em repositorio vivo com `git status` limpo** | `LucaX-Enterprise-OS`, `Research`, `SSC-Plus`, `lucaX` |
| 6 | **`E:\$RECYCLE.BIN`** | ✅ Presente — **184 MB**. E rede de resgate, nao sobra |
| 7 | **`basckup antigo`** — enquanto estiver em `DECIDIR` | ✅ Presente — **2.594 MB** |

**Regra que atravessa a lista inteira:** **nenhum item sai daqui por medicao de agente.**
Sai por **decisao do Fundador**, escrita e datada. Um agente que nao encontra um item
**registra "esta na principal"** — nunca "nao existe", nunca "pode apagar".

### ⚠️ Achado que esta lista produz, e que nao e dela

**`git status` limpo nao cobre o que esta nesta lista.** Os itens 1, 2 e parte do 4 sao
**gitignorados ou fora de arvore versionada** — a regra do `lucaX` ja diz
*"o que o git nao alcanca nao viaja por ele"*. O item 5 protege o versionado; **os
itens 1–4, 6 e 7 existem precisamente porque o git nao os protege**.

---

## Custo da sede anterior — ✅ fechado ao mudar de sede

O `.scratch/` na raiz do `LucaX-Enterprise-OS` adicionava **entrada de raiz nao
declarada**: o `IR-BL/3` mede por lista fechada positiva e **para com erro** diante dela
(portao de raiz, `RD-53`), e a lista `NAO_ACERVO` vigente e `.obsidian` ·
`_SAIDA-COMPANY-OS` · `CLAUDE.md` · `.git` · `.gitattributes`. Agravava que o
repositorio **nao tem `.gitignore`**, entao `.scratch/` aparecia **untracked** e colidia
com o item 5 desta lista.

**Fechado pela saida que o Fundador escolheu: mudar a sede, nao a regra.** `NAO_ACERVO`
ficou intacta, nenhum `.gitignore` foi criado, `.scratch/NUNCA-APAGAR.md` foi apagado e
o `.scratch/` vazio removido — o acervo voltou ao estado anterior a esta sessao.
Ver [[nunca-apagar-custodia]].
