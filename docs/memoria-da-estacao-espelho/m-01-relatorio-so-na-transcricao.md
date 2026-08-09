---
name: m-01-relatorio-so-na-transcricao
description: "O relatorio da missao M-01 (custo de migrar os setores da fabrica) nunca foi para o disco — vive so na transcricao de sessao, e seus cinco achados estao transcritos aqui"
metadata: 
  node_type: memory
  type: project
  originSessionId: ebf4b3b3-1f86-4ef3-a418-6c39a9df3057
  modified: 2026-08-09T01:31:12.467Z
---

**O relatorio da M-01 nao esta no disco.** Ela reportou tê-lo deixado em
`_missao-m-01-*/`, e esse diretorio **nunca existiu** — `0` ocorrencias em `E:` e
`C:\Users\lucas`, medido em 2026-08-08. Ele existe **exclusivamente** na transcricao
`C:\Users\lucas\.claude\projects\E--LucaX-Enterprise-OS\c333fe55-770b-46f0-b24a-1ee241d27afc.jsonl`
(encerrada 2026-08-08T03:31Z), que nao e artefato, nao e catalogada e ninguem le ao
abrir o repositorio.

**Os cinco achados foram conferidos na fonte pela retomada de 2026-08-08** e ficam
transcritos aqui, porque este e o unico lugar duravel em que couberam:

1. **4 de 6 partes cabem na Carta de Departamento.** `POLITICAS`→B3/B4, `PADRAO`→B10 §8,
   `QUALIDADE`→B8 §11, `NAO FAZ`→B3 §4.
2. **`CARGOS` e `FERRAMENTAS` nao cabem por PROIBICAO, nao por falta de secao** —
   `FND-02 §10` (*"nesta fase nao existem agentes"*, conferido em
   `foundation/02-estrutura-organizacional.md:496`) e `ADR-0011 §5.4`.
3. **O rito nao escala por Departamento: e UM ato, nao nove.** Precedentes medidos —
   `MSG-2026-0004` ratificou 5 Cartas num ato; `MSG-2026-0007` pos 14 objetos em vigor
   num ato.
4. **Custo fixo `1 ADR + 1 RFC + 1 FIT + 1 REV + 1 ato`; marginal `1 artefato` por
   Departamento.** Migrar so os exercidos reduz o marginal, nao o fixo nem o ato.
5. **O no de segregacao:** `DEP-GOV` revisa Carta de Departamento e seu `I-3` o impede de
   revisar a propria; num lote, `DEP-QAR` revisaria a de `DEP-GOV` **com a Carta de
   `DEP-QAR` no mesmo lote**.
6. **A cascata do §13.2:** dobrar o corpo torna os nove perfis de carregamento falsos, e
   `DC-10` obriga remedir todos (`CC-03`, `AL-05`).

⚠️ **A copia longa em `RETOMADA-M-01-2026-08-08.md` tambem nao e duravel** — vive no
scratchpad de sessao. **Nada disto esta gravado no acervo**, e nao deve ser: esta maquina
e espelho de leitura, conforme o bloco no topo de `CLAUDE.md`.

**Pendencia com dono, aberta:** gravar o contrato fabrica↔acervo e `C3` se for para valer
— ver [[contrato-fabrica-acervo-custa-c3]].
