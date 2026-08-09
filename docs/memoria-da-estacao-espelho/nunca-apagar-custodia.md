---
name: nunca-apagar-custodia
description: "Lista NUNCA APAGAR decidida pelo Fundador em 2026-08-08 — o que nenhum agente remove, e a regra de que caminho ausente significa \"esta na principal\""
metadata: 
  node_type: memory
  type: project
  originSessionId: ebf4b3b3-1f86-4ef3-a418-6c39a9df3057
  modified: 2026-08-09T01:43:43.777Z
---

**Decisao do Fundador, 2026-08-08.** Nenhum destes itens sai da lista por medicao de
agente — so por decisao do Fundador, escrita e datada. **Agente que nao encontra um item
registra "esta na principal", nunca "nao existe" e nunca "pode apagar".**

1. **`separacao-2026-08-02`** — 283 MB, **exemplar unico** dos 9 `.db` do `consult`.
   Dado gitignorado **nunca esteve em git**: sem reflog, sem remoto, sem segunda copia.
   E o commit **`85df749`** do `lucaX` removeu **271 arquivos** justificando-se *"backup
   datado de 283 MB cobre"* — **apagar o backup derruba retroativamente a justificativa
   da remocao**. *(Ausente desta maquina: `0` ocorrencias em `E:`.)*
2. **Os 4 backups do `Research`** — `_backups-F11-2026-08-03`, `_backups-F12-2026-08-03`,
   `_fabrica\_backups`, `_fabrica\skills\backup-datado`. Presentes, mas ~0,2 MB: cascas.
3. **Os 2 backups do `SSC-Plus`** — so **1** esta aqui (`06_p1a\evidencias\backups`).
4. **`backup-99freelas` do `lucaX`** — e **arquivo**, nao diretorio:
   `My_WorkSpace\Meus_projetos\operacao-freelancer\perfil\backup-99freelas-antes-perfil-hibrido-2026-07-22.md`.
5. **Qualquer coisa em repositorio vivo com `git status` limpo.**
6. **`E:\$RECYCLE.BIN`** (184 MB) — rede de resgate, nao sobra.
7. **`basckup antigo`** (2.594 MB, fotos e gravacoes de 2024) — em **`DECIDIR`** ate o
   Fundador confirmar se ha outra copia. **`DECIDIR` nao e permissao provisoria para
   apagar: e proibicao provisoria de apagar.** Nenhum dos quatro repositorios o cita, e
   **orfao nao e lixo** — sem outra copia, apagar vira custodia, nao faxina.

⚠️ **`git status` limpo NAO cobre esta lista.** Os itens 1–4 sao gitignorados ou fora de
arvore versionada — existem justamente porque o git nao os protege.

**Sedes.** Lista longa, com os fundamentos: [[nunca-apagar-lista-longa]], nesta mesma
sede de memoria — **fora do recurso fenceado, lida a cada sessao**; ainda **local a esta
maquina**, entao reescrever na principal continua pendente. Destino de backup:
`E:\lucaX\.claude\rules\git-and-backup.md` — principal e a sede; nesta maquina grava em
`.scratch/_backups/`, temporario; **nao repor `_backups\` na raiz de `E:`, porque duas
sedes divergem**.

**✅ Fechado em 2026-08-08, por decisao do Fundador:** a lista saiu de
`.scratch/NUNCA-APAGAR.md` justamente porque `.scratch` **nao esta** em `NAO_ACERVO` (o
`IR-BL/3` pararia com erro na proxima baseline da principal, portao de raiz `RD-53`) e o
repositorio nao tem `.gitignore` (aparecia untracked, colidindo com o item 5 acima).
**Mudou a sede, nao a regra:** `NAO_ACERVO` intacta, nenhum `.gitignore`, `.scratch/`
apagado do acervo.
