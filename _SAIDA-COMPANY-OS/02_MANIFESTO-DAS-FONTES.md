> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

# 02 — MANIFESTO DAS FONTES

**Frente:** Programa de Inteligência do Acervo · **Fase 0 — Governança e Inventário**

Registro item a item de todo o acervo externo. Este manifesto **não avalia, não recomenda e não autoriza adoção**. Ele apenas declara o que existe, onde está e em que estado de catalogação se encontra.

---

## Método

- **Origem:** `C:\Users\IA Lucas\OneDrive\Área de Trabalho\POJETOS\Para criar um novo projeto\Mais material`
- **Data da varredura:** 2026-07-29
- **Unidade de catalogação:** item de nível 1 dentro de cada área numerada e item de nível 2 dentro das subpastas agrupadoras (`_construcao-civil`, `_redes-sociais`, `_renda-extra`). Um repositório conta como **um** item, independentemente de quantos arquivos contenha.
- **Fora da unidade de catalogação:** arquivos internos de repositórios. O acervo contém 77.605 arquivos no total; apenas 279 são itens catalogáveis.
- **Hash:** SHA-256, exibido nos 16 primeiros dígitos hexadecimais. Calculado para os 236 arquivos de mídia (`.mp4`, `.png`, `.xlsx`). Diretórios não recebem hash de arquivo único — a coluna traz a contagem de arquivos e a profundidade de aninhamento.
- **Nenhuma fonte foi movida, renomeada, aberta para escrita ou executada.** Todas as operações foram de leitura.

### Colunas

| Coluna | Significado |
|---|---|
| ID | Identificador estável desta frente: `AC-<área>-<tipo>-<sequência>` |
| Caminho | Relativo à pasta da área (o cabeçalho da seção completa o caminho) |
| Tipo | REPO · PRINT · VÍDEO · PLANILHA |
| Tam. | Tamanho em disco (repositório = soma recursiva) |
| SHA-256 | Prefixo de 16 hex; `dir` para repositórios |
| Índice | Presença em `00_COMECE-AQUI/INDICE-COMPLETO.md` — `direta` (nome literal), `série` (coberto por notação de intervalo), `wildcard` (coberto só por padrão agregado) |
| Catálogo | Presença no `_CONTEUDO.md` da própria área |
| Transcr. | Necessidade de transcrição para que o conteúdo seja legível |
| Estado | Ver legenda |

### Legenda de estados

| Estado | Significado nesta fase |
|---|---|
| PENDENTE | Sem descrição prévia de nenhuma natureza |
| JÁ DESCRITO | Existe descrição prévia no catálogo. **Não significa validado, verificado ou aprovado** |
| LACUNA DE TRANSCRIÇÃO | Conteúdo não legível sem transcrição; qualquer afirmação sobre ele seria inferência |
| DUPLICATA EXATA | Hash idêntico ao de outro item do acervo |
| POSSÍVEL DUPLICATA | Sobreposição de conteúdo medida, mas não total |
| INACESSÍVEL | Leitura falhou |
| FORA DE ESCOPO | Excluído do programa — **nenhum item recebeu este estado nesta fase**, porque definir escopo é decisão que a Fase 0 não pode tomar |

**Critério de desempate em duplicata exata:** retém-se o item de nome anterior em ordem alfabética; o posterior recebe DUPLICATA EXATA. O critério é arbitrário e serve apenas para não analisar o mesmo byte duas vezes — não constitui decisão de descarte.

---

## 01_DECIDIR-MODELO-E-ESCOPO

**11 itens** — 0 repositórios · 5 prints · 6 vídeos · 0 planilhas · 0.16 GB

| ID | Caminho | Tipo | Tam. | SHA-256 | Índice | Catálogo | Transcr. | Estado |
|---|---|---|---|---|---|---|---|---|
| AC-01-PRT-001 | `Captura de tela 2026-07-28 155729.png` | PRINT | 833.7 KB | `DC4365C3885D4F35` | direta | direta | não | JÁ DESCRITO |
| AC-01-PRT-002 | `Captura de tela 2026-07-28 163806.png` | PRINT | 212.6 KB | `F4E903F49157D1A6` | direta | direta | não | JÁ DESCRITO |
| AC-01-VID-001 | `Free Claude Code.mp4` | VÍDEO | 57.1 MB | `8E00C68D6B3B30B5` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-01-PRT-003 | `frontend ranking.png` | PRINT | 1.2 MB | `D97296B446732B44` | direta | direta | não | JÁ DESCRITO |
| AC-01-VID-002 | `Gravando 2026-07-28 153846.mp4` | VÍDEO | 7.9 MB | `A1B951B8AE062FB6` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-01-VID-003 | `Gravando 2026-07-28 160504.mp4` | VÍDEO | 7.6 MB | `654D7FBD89519866` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-01-VID-004 | `Gravando 2026-07-28 162512.mp4` | VÍDEO | 6.4 MB | `1671949B009E4C96` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-01-VID-005 | `Gravando 2026-07-28 180226.mp4` | VÍDEO | 58.8 MB | `234C8B7B9B3319A1` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-01-VID-006 | `llms para usar.mp4` | VÍDEO | 26.7 MB | `2C903B644BF6F5E3` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-01-PRT-004 | `melhroes iA 2026.png` | PRINT | 1.7 MB | `C17746D57845EACE` | direta | direta | não | JÁ DESCRITO |
| AC-01-PRT-005 | `ops 5 cenchmark.png` | PRINT | 566.8 KB | `D8E3DB6B322C68A5` | direta | direta | não | JÁ DESCRITO |

---

## 02_PROJETAR-ARQUITETURA

**24 itens** — 1 repositório · 10 prints · 13 vídeos · 0 planilhas · 0.25 GB

| ID | Caminho | Tipo | Tam. | SHA-256 | Índice | Catálogo | Transcr. | Estado |
|---|---|---|---|---|---|---|---|---|
| AC-02-REP-001 | `ai-orchestrator-starter` | REPO | 19.3 KB | dir · 25 arq. · aninhado | direta | direta | não | JÁ DESCRITO |
| AC-02-PRT-001 | `AgenticWOorld.png` | PRINT | 1.3 MB | `93FD2C2D75311F44` | direta | direta | não | JÁ DESCRITO |
| AC-02-PRT-002 | `AI Agent.png` | PRINT | 2.8 MB | `7B1EA2076807A263` | direta | direta | não | JÁ DESCRITO |
| AC-02-VID-001 | `anatomai de projeto.mp4` | VÍDEO | 7.3 MB | `5CB921F03732277F` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-02-PRT-003 | `Captura de tela 2026-07-28 152916.png` | PRINT | 2.2 MB | `CEAA0CEEBF477F85` | direta | direta | não | JÁ DESCRITO |
| AC-02-PRT-004 | `coisas para criar e melhorar .png` | PRINT | 3.1 MB | `884C58983621E0FC` | direta | direta | não | JÁ DESCRITO |
| AC-02-VID-002 | `Data base scalling.mp4` | VÍDEO | 7.1 MB | `5CDAFC52A550F07D` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-02-VID-003 | `data structure.mp4` | VÍDEO | 9.4 MB | `2EBE06451AE24AD0` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-02-VID-004 | `Desgin pattern.mp4` | VÍDEO | 5.2 MB | `53B62E28ED2FE661` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-02-VID-005 | `fundamentais.mp4` | VÍDEO | 86.4 MB | `8357024D553AAE0F` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-02-VID-006 | `Gravando 2026-07-28 162144.mp4` | VÍDEO | 45.6 MB | `E523AFC4EDDF0AA6` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-02-VID-007 | `Gravando 2026-07-28 162729.mp4` | VÍDEO | 6.7 MB | `C3FC42F0EFF959D6` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-02-VID-008 | `Gravando 2026-07-28 163313.mp4` | VÍDEO | 2.6 MB | `C8F33826431AF318` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-02-VID-009 | `Gravando 2026-07-28 204335.mp4` | VÍDEO | 2.1 MB | `FC4086F4B3102370` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-02-VID-010 | `Gravando 2026-07-28 214021.mp4` | VÍDEO | 5.5 MB | `AA4EA39A4E8A8466` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-02-VID-011 | `Gravando 2026-07-29 090647.mp4` | VÍDEO | 7.7 MB | `7396803D345736D6` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-02-VID-012 | `Gravando 2026-07-29 091319.mp4` | VÍDEO | 41.3 MB | `ECF9BF67DE98F5A3` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-02-PRT-005 | `loop0.png` | PRINT | 1.5 MB | `062BBCCF3D2BA4E2` | direta | direta | não | JÁ DESCRITO |
| AC-02-PRT-006 | `loop1.png` | PRINT | 1.5 MB | `1AC57D8A900F703B` | série | direta | não | JÁ DESCRITO |
| AC-02-PRT-007 | `loop2.png` | PRINT | 1.5 MB | `8D0159C96C9C8E7A` | série | direta | não | JÁ DESCRITO |
| AC-02-PRT-008 | `loop3.png` | PRINT | 1.5 MB | `FCE71FCD00DEBCC2` | série | direta | não | JÁ DESCRITO |
| AC-02-PRT-009 | `Rag + IA.png` | PRINT | 1.9 MB | `32D0CE07F68D01D6` | direta | direta | não | JÁ DESCRITO |
| AC-02-PRT-010 | `The agent knwoledge.png` | PRINT | 2.8 MB | `3161859DAD8333A5` | direta | direta | não | JÁ DESCRITO |
| AC-02-VID-013 | `verificar arquitetura.mp4` | VÍDEO | 9 MB | `88FA51513F9BABE9` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |

**Notas de integridade desta área**

- `ai-orchestrator-starter` — **sem arquivo de licença na raiz efetiva**. Situação jurídica indeterminada até verificação.

---

## 03_ORQUESTRACAO-DE-AGENTES

**31 itens** — 10 repositórios · 8 prints · 13 vídeos · 0 planilhas · 1.08 GB

| ID | Caminho | Tipo | Tam. | SHA-256 | Índice | Catálogo | Transcr. | Estado |
|---|---|---|---|---|---|---|---|---|
| AC-03-REP-001 | `codex-plugin-cc-main` | REPO | 374.2 KB | dir · 63 arq. | direta | direta | não | JÁ DESCRITO |
| AC-03-REP-002 | `ECC-main` | REPO | 43.7 MB | dir · 3322 arq. · aninhado | direta | direta | não | JÁ DESCRITO |
| AC-03-REP-003 | `gstack-Ahacad-main` | REPO | 53 MB | dir · 1176 arq. | direta | direta | não | POSSÍVEL DUPLICATA |
| AC-03-REP-004 | `gstack-garrytan-main` | REPO | 53.1 MB | dir · 1171 arq. | direta | direta | não | JÁ DESCRITO |
| AC-03-REP-005 | `hermes-agent-main` | REPO | 134 MB | dir · 6265 arq. · aninhado | direta | direta | não | JÁ DESCRITO |
| AC-03-REP-006 | `openclaw-main` | REPO | 289.3 MB | dir · 23953 arq. · aninhado | direta | direta | não | JÁ DESCRITO |
| AC-03-REP-007 | `orca-main` | REPO | 127.3 MB | dir · 9477 arq. · aninhado | direta | direta | não | JÁ DESCRITO |
| AC-03-REP-008 | `ralph-main` | REPO | 4.9 MB | dir · 31 arq. · aninhado | direta | direta | não | JÁ DESCRITO |
| AC-03-REP-009 | `ruflo-main` | REPO | 74.5 MB | dir · 5116 arq. · aninhado | direta | direta | não | JÁ DESCRITO |
| AC-03-REP-010 | `superpowers-main` | REPO | 1.3 MB | dir · 172 arq. · aninhado | direta | direta | não | JÁ DESCRITO |
| AC-03-PRT-001 | `Captura de tela 2026-07-28 152354.png` | PRINT | 1.8 MB | `C46488B2F372FAA5` | direta | direta | não | JÁ DESCRITO |
| AC-03-PRT-002 | `Captura de tela 2026-07-28 152407.png` | PRINT | 1.2 MB | `CB5FA1539B4798B3` | direta | direta | não | JÁ DESCRITO |
| AC-03-PRT-003 | `Captura de tela 2026-07-28 152418.png` | PRINT | 1.1 MB | `142864ED243780E9` | direta | direta | não | JÁ DESCRITO |
| AC-03-PRT-004 | `Captura de tela 2026-07-28 152428.png` | PRINT | 1.2 MB | `268B1CE65EDB581B` | direta | direta | não | JÁ DESCRITO |
| AC-03-PRT-005 | `Captura de tela 2026-07-28 152439.png` | PRINT | 1.3 MB | `7292AD51C92754CC` | direta | direta | não | JÁ DESCRITO |
| AC-03-PRT-006 | `Captura de tela 2026-07-28 152608.png` | PRINT | 879.7 KB | `DB54B7F918730F27` | direta | direta | não | JÁ DESCRITO |
| AC-03-PRT-007 | `Captura de tela 2026-07-28 152621.png` | PRINT | 966.9 KB | `8D7450D9384F9B3D` | direta | direta | não | JÁ DESCRITO |
| AC-03-PRT-008 | `Captura de tela 2026-07-28 165210.png` | PRINT | 813.4 KB | `7D5EAF262CA86CD5` | direta | direta | não | JÁ DESCRITO |
| AC-03-VID-001 | `ECC.mp4` | VÍDEO | 41 MB | `6434AF4CA455407B` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-03-VID-002 | `Gravando 2026-07-28 153202.mp4` | VÍDEO | 21.5 MB | `397112332ABD593D` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-03-VID-003 | `Gravando 2026-07-28 154123.mp4` | VÍDEO | 50.3 MB | `E09098CF9DF15DAC` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-03-VID-004 | `Gravando 2026-07-28 161341.mp4` | VÍDEO | 75.3 MB | `A08BCBF5DFEF093E` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-03-VID-005 | `Gravando 2026-07-28 162357.mp4` | VÍDEO | 33.9 MB | `E1198B32D4660DBA` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-03-VID-006 | `Gravando 2026-07-28 163546.mp4` | VÍDEO | 11.1 MB | `9317AB60D45D7EAF` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-03-VID-007 | `Gravando 2026-07-28 164919.mp4` | VÍDEO | 6.7 MB | `192C3748B93DDE8B` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-03-VID-008 | `Gravando 2026-07-28 165017.mp4` | VÍDEO | 6.7 MB | `192C3748B93DDE8B` | direta | direta | **necessária** | DUPLICATA EXATA |
| AC-03-VID-009 | `Gravando 2026-07-28 203752.mp4` | VÍDEO | 3.3 MB | `64A5943E3815E957` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-03-VID-010 | `Gravando 2026-07-28 204200.mp4` | VÍDEO | 3.7 MB | `ECA00A613D86A8C2` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-03-VID-011 | `Gravando 2026-07-29 091150.mp4` | VÍDEO | 56.2 MB | `D5DE42134A780823` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-03-VID-012 | `Gravando 2026-07-29 091519.mp4` | VÍDEO | 3.9 MB | `FF4B9F882F4FF0D9` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-03-VID-013 | `Gravando 2026-07-29 091907.mp4` | VÍDEO | 3.8 MB | `6CAB17662ACBADD8` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |

**Notas de integridade desta área**

- `Gravando 2026-07-28 165017.mp4` — DUPLICATA EXATA de `Gravando 2026-07-28 164919.mp4` (mesmo SHA-256, 6.7 MB).
- `gstack-Ahacad-main` — POSSÍVEL DUPLICATA: sobrepoe 99,4% do conteudo de `gstack-garrytan-main`; acrescenta 7 arquivos de empacotamento (plugin.json, hooks, .gitmodules, workflow de upstream).

---

## 04_MEMORIA-E-CONHECIMENTO

**32 itens** — 7 repositórios · 13 prints · 12 vídeos · 0 planilhas · 1.63 GB

| ID | Caminho | Tipo | Tam. | SHA-256 | Índice | Catálogo | Transcr. | Estado |
|---|---|---|---|---|---|---|---|---|
| AC-04-REP-001 | `ai-second-brain-main` | REPO | 579 KB | dir · 10 arq. | direta | direta | não | JÁ DESCRITO |
| AC-04-REP-002 | `claude-mem-main` | REPO | 16.6 MB | dir · 850 arq. · aninhado | direta | direta | não | JÁ DESCRITO |
| AC-04-REP-003 | `codebase-memory-mcp-main` | REPO | 1.23 GB | dir · 1829 arq. · aninhado | direta | direta | não | JÁ DESCRITO |
| AC-04-REP-004 | `markitdown-main` | REPO | 23.7 MB | dir · 163 arq. · aninhado | direta | direta | não | JÁ DESCRITO |
| AC-04-REP-005 | `notebooklm-skill-master` | REPO | 262 KB | dir · 21 arq. | direta | direta | não | JÁ DESCRITO |
| AC-04-REP-006 | `open-notebook-main` | REPO | 5.7 MB | dir · 574 arq. · aninhado | direta | direta | não | JÁ DESCRITO |
| AC-04-REP-007 | `second-brain-skills-main` | REPO | 725 KB | dir · 97 arq. | direta | direta | não | JÁ DESCRITO |
| AC-04-PRT-001 | `Captura de tela 2026-07-28 152727.png` | PRINT | 1.7 MB | `FFDCEE7B2B6B571F` | direta | direta | não | JÁ DESCRITO |
| AC-04-VID-001 | `Gravando 2026-07-28 153509.mp4` | VÍDEO | 19.7 MB | `072AA736BED616CB` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-04-VID-002 | `Gravando 2026-07-28 153951.mp4` | VÍDEO | 38 MB | `60A03F8E7E2BA907` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-04-VID-003 | `Gravando 2026-07-28 160036.mp4` | VÍDEO | 74.4 MB | `4E5BCDA42E08CC58` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-04-VID-004 | `Gravando 2026-07-28 163142.mp4` | VÍDEO | 6.6 MB | `607F24F1952C9EFB` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-04-VID-005 | `Gravando 2026-07-28 163335.mp4` | VÍDEO | 1.7 MB | `214B28CBD48F4AA1` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-04-VID-006 | `Gravando 2026-07-28 203247.mp4` | VÍDEO | 6.2 MB | `CEA0728F4FD810B6` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-04-VID-007 | `Gravando 2026-07-28 213812.mp4` | VÍDEO | 45 MB | `931B1B1D8B4D69A9` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-04-VID-008 | `Gravando 2026-07-28 214526.mp4` | VÍDEO | 10.3 MB | `6D3E3AE21B5A5C6A` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-04-VID-009 | `Gravando 2026-07-29 085933.mp4` | VÍDEO | 6.9 MB | `224277B42AD1F4C6` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-04-VID-010 | `Gravando 2026-07-29 092503.mp4` | VÍDEO | 50.9 MB | `57F4F34055387EC2` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-04-PRT-002 | `Rag + langchain0.png` | PRINT | 1.5 MB | `C8D2EBEB0FED1D6F` | direta | direta | não | JÁ DESCRITO |
| AC-04-PRT-003 | `Rag + langchain1.png` | PRINT | 961.2 KB | `990DD0B0924CBD04` | série | direta | não | JÁ DESCRITO |
| AC-04-PRT-004 | `Rag + langchain10.png` | PRINT | 1.2 MB | `F0C7C9BEB4841876` | série | série | não | JÁ DESCRITO |
| AC-04-PRT-005 | `Rag + langchain11.png` | PRINT | 684.6 KB | `46A8CD100DB728A7` | série | direta | não | JÁ DESCRITO |
| AC-04-PRT-006 | `Rag + langchain2.png` | PRINT | 1.1 MB | `73A4E647F05AF6E7` | série | série | não | JÁ DESCRITO |
| AC-04-PRT-007 | `Rag + langchain3.png` | PRINT | 1.2 MB | `FC85EFBC56F122CF` | série | série | não | JÁ DESCRITO |
| AC-04-PRT-008 | `Rag + langchain4.png` | PRINT | 878.1 KB | `8AC03D7E88BBB6B5` | série | série | não | JÁ DESCRITO |
| AC-04-PRT-009 | `Rag + langchain5.png` | PRINT | 1 MB | `F8D94241C959F564` | série | série | não | JÁ DESCRITO |
| AC-04-PRT-010 | `Rag + langchain6.png` | PRINT | 1.1 MB | `428FAB1581B02D29` | série | série | não | JÁ DESCRITO |
| AC-04-PRT-011 | `Rag + langchain7.png` | PRINT | 1000.1 KB | `3AE7D462D72F47EC` | série | série | não | JÁ DESCRITO |
| AC-04-PRT-012 | `Rag + langchain8.png` | PRINT | 807 KB | `0D30D673BB76C9E8` | série | série | não | JÁ DESCRITO |
| AC-04-PRT-013 | `Rag + langchain9.png` | PRINT | 1.2 MB | `0E0A210948211FA4` | série | série | não | JÁ DESCRITO |
| AC-04-VID-011 | `segundo cérebro.mp4` | VÍDEO | 50.3 MB | `7E78FB9B5FC4D07D` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-04-VID-012 | `segundo cérebro2.mp4` | VÍDEO | 35.3 MB | `A847A783DACBEDD4` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |

**Notas de integridade desta área**

- `second-brain-skills-main` — **sem arquivo de licença na raiz efetiva**. Situação jurídica indeterminada até verificação.

---

## 05_SKILLS-E-PROMPTS

**51 itens** — 6 repositórios · 14 prints · 31 vídeos · 0 planilhas · 0.41 GB

| ID | Caminho | Tipo | Tam. | SHA-256 | Índice | Catálogo | Transcr. | Estado |
|---|---|---|---|---|---|---|---|---|
| AC-05-REP-001 | `agent-skills-main` | REPO | 678.9 KB | dir · 128 arq. · aninhado | direta | direta | não | JÁ DESCRITO |
| AC-05-REP-002 | `andrej-karpathy-skills-main` | REPO | 36.8 KB | dir · 9 arq. · aninhado | direta | direta | não | JÁ DESCRITO |
| AC-05-REP-003 | `CL4R1T4S` | REPO | 3 MB | dir · 99 arq. | direta | direta | não | JÁ DESCRITO |
| AC-05-REP-004 | `claude-skills-main` | REPO | 85.7 MB | dir · 9210 arq. | direta | direta | não | JÁ DESCRITO |
| AC-05-REP-005 | `humanizer-main` | REPO | 49.6 KB | dir · 6 arq. | direta | direta | não | JÁ DESCRITO |
| AC-05-REP-006 | `one-skill-to-rule-them-all-main` | REPO | 3.1 MB | dir · 6 arq. · aninhado | direta | direta | não | JÁ DESCRITO |
| AC-05-PRT-001 | `Captura de tela 2026-07-28 152808.png` | PRINT | 1 MB | `8BE3FEC37285E3E4` | direta | direta | não | JÁ DESCRITO |
| AC-05-PRT-002 | `Captura de tela 2026-07-28 152819.png` | PRINT | 1.1 MB | `A2A5BE57590FD6E0` | direta | direta | não | JÁ DESCRITO |
| AC-05-PRT-003 | `Captura de tela 2026-07-28 152831.png` | PRINT | 1.2 MB | `92B6A7445DEE0307` | direta | direta | não | JÁ DESCRITO |
| AC-05-PRT-004 | `Captura de tela 2026-07-28 152843.png` | PRINT | 933.9 KB | `16B3CDD3E42CA0EE` | direta | direta | não | JÁ DESCRITO |
| AC-05-PRT-005 | `Captura de tela 2026-07-28 152857.png` | PRINT | 978.4 KB | `3864E7243CEB68E1` | direta | direta | não | JÁ DESCRITO |
| AC-05-PRT-006 | `Captura de tela 2026-07-28 153525.png` | PRINT | 1.2 MB | `8E433A47CD76D496` | direta | direta | não | JÁ DESCRITO |
| AC-05-PRT-007 | `Captura de tela 2026-07-28 162742.png` | PRINT | 1.2 MB | `C56ED4F53CB67263` | direta | direta | não | JÁ DESCRITO |
| AC-05-PRT-008 | `Captura de tela 2026-07-28 163430.png` | PRINT | 1.4 MB | `FED037D74B77B593` | direta | direta | não | JÁ DESCRITO |
| AC-05-PRT-009 | `Captura de tela 2026-07-28 164606.png` | PRINT | 1.7 MB | `08E1E400AE020EA8` | direta | direta | não | JÁ DESCRITO |
| AC-05-PRT-010 | `Captura de tela 2026-07-28 164701.png` | PRINT | 1.6 MB | `FB38AD71B33401FB` | direta | direta | não | JÁ DESCRITO |
| AC-05-PRT-011 | `Captura de tela 2026-07-28 214147.png` | PRINT | 2.3 MB | `FB2CEF5393F0DA4F` | direta | direta | não | JÁ DESCRITO |
| AC-05-PRT-012 | `Captura de tela 2026-07-28 214542.png` | PRINT | 1.3 MB | `64D955957B723A23` | direta | direta | não | JÁ DESCRITO |
| AC-05-PRT-013 | `Captura de tela 2026-07-29 091958.png` | PRINT | 1.5 MB | `1044A11EC52B0BD4` | direta | direta | não | JÁ DESCRITO |
| AC-05-VID-001 | `Gravando 2026-07-28 153027.mp4` | VÍDEO | 8.3 MB | `CA913EEE8CD7644E` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-05-VID-002 | `Gravando 2026-07-28 153801.mp4` | VÍDEO | 24.8 MB | `A87774E5780B6B19` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-05-VID-003 | `Gravando 2026-07-28 160257.mp4` | VÍDEO | 12.7 MB | `809A20E24B1589F6` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-05-VID-004 | `Gravando 2026-07-28 161506.mp4` | VÍDEO | 9 MB | `F4F3BD92F2FCA3EF` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-05-VID-005 | `Gravando 2026-07-28 162024.mp4` | VÍDEO | 5.4 MB | `BE600F548366F8D1` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-05-VID-006 | `Gravando 2026-07-28 164328.mp4` | VÍDEO | 6.6 MB | `D06360A42A05B35F` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-05-VID-007 | `Gravando 2026-07-28 164549.mp4` | VÍDEO | 5.4 MB | `9F5062D16EC68D57` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-05-VID-008 | `Gravando 2026-07-28 165153.mp4` | VÍDEO | 5.5 MB | `0257FE2784C05B85` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-05-VID-009 | `Gravando 2026-07-28 165245.mp4` | VÍDEO | 8.9 MB | `A715C1F0DF6D85DC` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-05-VID-010 | `Gravando 2026-07-28 175640.mp4` | VÍDEO | 7.7 MB | `475AC673E874F137` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-05-VID-011 | `Gravando 2026-07-28 180624.mp4` | VÍDEO | 14 MB | `8EF94265F43F568C` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-05-VID-012 | `Gravando 2026-07-28 180710.mp4` | VÍDEO | 5.5 MB | `4983173909FCD1C5` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-05-VID-013 | `Gravando 2026-07-28 180847.mp4` | VÍDEO | 9.1 MB | `FBD65FE10B8A8524` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-05-VID-014 | `Gravando 2026-07-28 181152.mp4` | VÍDEO | 51.1 MB | `81C1F356DB9713F3` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-05-VID-015 | `Gravando 2026-07-28 202743.mp4` | VÍDEO | 5.4 MB | `D229DC339606556B` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-05-VID-016 | `Gravando 2026-07-28 202900.mp4` | VÍDEO | 5.4 MB | `8E440CFA107284FE` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-05-VID-017 | `Gravando 2026-07-28 202959.mp4` | VÍDEO | 3.7 MB | `F07C731CDFD36214` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-05-VID-018 | `Gravando 2026-07-28 203207.mp4` | VÍDEO | 1.8 MB | `D06B6CDF1E34CE9D` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-05-VID-019 | `Gravando 2026-07-28 204235.mp4` | VÍDEO | 2.6 MB | `5AE94BA7BFEE8C9C` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-05-VID-020 | `Gravando 2026-07-28 214332.mp4` | VÍDEO | 42.3 MB | `57B6CA5C5E605C92` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-05-VID-021 | `Gravando 2026-07-29 085150.mp4` | VÍDEO | 3.1 MB | `B462AF4B96CA62F2` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-05-VID-022 | `Gravando 2026-07-29 085445.mp4` | VÍDEO | 4.3 MB | `C56252E953ED728F` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-05-VID-023 | `Gravando 2026-07-29 085518.mp4` | VÍDEO | 2.7 MB | `7146933046EC4399` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-05-VID-024 | `Gravando 2026-07-29 085832.mp4` | VÍDEO | 3 MB | `D1C0058F63ECE613` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-05-VID-025 | `Gravando 2026-07-29 090342.mp4` | VÍDEO | 6.2 MB | `FE16630C688F0476` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-05-VID-026 | `Gravando 2026-07-29 091632.mp4` | VÍDEO | 3 MB | `8E56873E603C3AB3` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-05-VID-027 | `Gravando 2026-07-29 091700.mp4` | VÍDEO | 4.1 MB | `4D02A7BABBEE1CA1` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-05-VID-028 | `Gravando 2026-07-29 091802.mp4` | VÍDEO | 3.4 MB | `52BB9ABD59548E08` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-05-VID-029 | `Gravando 2026-07-29 091836.mp4` | VÍDEO | 5.8 MB | `2E8BA6FDD00F81E5` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-05-VID-030 | `Gravando 2026-07-29 092234.mp4` | VÍDEO | 3.5 MB | `FDAD2FFDAD6AB88D` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-05-PRT-014 | `prompt fable 5.png` | PRINT | 124.7 KB | `5908680A4A034C6E` | direta | direta | não | JÁ DESCRITO |
| AC-05-VID-031 | `SKills que valem.mp4` | VÍDEO | 32.3 MB | `51C22EB17672FAAE` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |

**Notas de integridade desta área**

- `andrej-karpathy-skills-main` — **sem arquivo de licença na raiz efetiva**. Situação jurídica indeterminada até verificação.

---

## 06_CONECTORES-MCP

**40 itens** — 4 repositórios · 13 prints · 23 vídeos · 0 planilhas · 0.42 GB

| ID | Caminho | Tipo | Tam. | SHA-256 | Índice | Catálogo | Transcr. | Estado |
|---|---|---|---|---|---|---|---|---|
| AC-06-REP-001 | `agent-browser-main` | REPO | 6.6 MB | dir · 413 arq. · aninhado | direta | direta | não | JÁ DESCRITO |
| AC-06-REP-002 | `Agent-Reach-main` | REPO | 826.9 KB | dir · 93 arq. · aninhado | direta | direta | não | JÁ DESCRITO |
| AC-06-REP-003 | `context7-master` | REPO | 19.3 MB | dir · 375 arq. · aninhado | direta | direta | não | JÁ DESCRITO |
| AC-06-REP-004 | `last30days-skill-main` | REPO | 13.1 MB | dir · 153 arq. · aninhado | direta | direta | não | JÁ DESCRITO |
| AC-06-PRT-001 | `Captura de tela 2026-07-28 154159.png` | PRINT | 953.6 KB | `73EB85F00A07C3F3` | direta | direta | não | JÁ DESCRITO |
| AC-06-PRT-002 | `Captura de tela 2026-07-28 160157.png` | PRINT | 1.2 MB | `3EBD11C0D9EC87C8` | direta | direta | não | JÁ DESCRITO |
| AC-06-PRT-003 | `Captura de tela 2026-07-28 160340.png` | PRINT | 1.4 MB | `7A7372E11146E56C` | direta | direta | não | JÁ DESCRITO |
| AC-06-PRT-004 | `conectores essenciais.png` | PRINT | 1.9 MB | `2645BF023BC646AE` | direta | direta | não | JÁ DESCRITO |
| AC-06-PRT-005 | `ferramentas.png` | PRINT | 3.2 MB | `FF02C789343A14B5` | direta | direta | não | JÁ DESCRITO |
| AC-06-PRT-006 | `ferramente de voz.png` | PRINT | 1 MB | `52FB83F636338C56` | direta | direta | não | JÁ DESCRITO |
| AC-06-VID-001 | `gemini + higs.mp4` | VÍDEO | 15.3 MB | `908681CB76437C69` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-06-VID-002 | `Gravando 2026-07-28 154542.mp4` | VÍDEO | 38.4 MB | `D459E96B86C3B742` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-06-VID-003 | `Gravando 2026-07-28 162702.mp4` | VÍDEO | 12.6 MB | `F33F44D82D56E6BF` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-06-VID-004 | `Gravando 2026-07-28 162934.mp4` | VÍDEO | 13.1 MB | `67801C74A12B7A31` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-06-VID-005 | `Gravando 2026-07-28 164155.mp4` | VÍDEO | 12.6 MB | `87CFFBA015D41D49` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-06-VID-006 | `Gravando 2026-07-28 164243.mp4` | VÍDEO | 27.1 MB | `5BA3E29ACE6451C1` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-06-VID-007 | `Gravando 2026-07-28 164517.mp4` | VÍDEO | 8.1 MB | `61856E2B8BBCFBEC` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-06-VID-008 | `Gravando 2026-07-28 164648.mp4` | VÍDEO | 14.1 MB | `BAE56116AFDB9262` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-06-VID-009 | `Gravando 2026-07-28 164826.mp4` | VÍDEO | 10.1 MB | `5E60EE16894BA6FC` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-06-VID-010 | `Gravando 2026-07-28 175754.mp4` | VÍDEO | 7.6 MB | `9C413104BD0D0020` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-06-VID-011 | `Gravando 2026-07-28 175840.mp4` | VÍDEO | 12 MB | `CABB3A6508DA4A5A` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-06-VID-012 | `Gravando 2026-07-28 180001.mp4` | VÍDEO | 8 MB | `7DA8C6E5E7A1C06F` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-06-VID-013 | `Gravando 2026-07-28 180429.mp4` | VÍDEO | 31.4 MB | `3F5CCF7CB3C788EE` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-06-VID-014 | `Gravando 2026-07-28 180542.mp4` | VÍDEO | 12.5 MB | `C137535557DFD8DA` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-06-VID-015 | `Gravando 2026-07-28 180747.mp4` | VÍDEO | 8.1 MB | `3F844FA66FED4350` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-06-VID-016 | `Gravando 2026-07-28 180942.mp4` | VÍDEO | 10.6 MB | `C9ACFA036D9674D8` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-06-VID-017 | `Gravando 2026-07-28 181016.mp4` | VÍDEO | 9 MB | `0AEE94B186A0670F` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-06-VID-018 | `Gravando 2026-07-28 203600.mp4` | VÍDEO | 9 MB | `3388A4CF6D502EB8` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-06-VID-019 | `Gravando 2026-07-28 213625.mp4` | VÍDEO | 3.4 MB | `C6E7C78FF5EC4BB8` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-06-VID-020 | `Gravando 2026-07-29 090139.mp4` | VÍDEO | 72.2 MB | `220CB74C92A0D19E` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-06-VID-021 | `Gravando 2026-07-29 091727.mp4` | VÍDEO | 2.2 MB | `6397C8A308AC9CAA` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-06-VID-022 | `Gravando 2026-07-29 092123.mp4` | VÍDEO | 6.6 MB | `C32CFE23278948B9` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-06-VID-023 | `Gravando 2026-07-29 092344.mp4` | VÍDEO | 26.7 MB | `7C9FA64467DCA0AA` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-06-PRT-007 | `mcp0.png` | PRINT | 1.2 MB | `D09356FEB962324D` | série | direta | não | JÁ DESCRITO |
| AC-06-PRT-008 | `mcp1.png` | PRINT | 1.6 MB | `97CBA09DC37D8F23` | série | direta | não | JÁ DESCRITO |
| AC-06-PRT-009 | `mcp2.png` | PRINT | 1.1 MB | `1CA42A848658AFDB` | série | direta | não | JÁ DESCRITO |
| AC-06-PRT-010 | `mcp3.png` | PRINT | 1.1 MB | `74E8A0946CAB7085` | série | direta | não | JÁ DESCRITO |
| AC-06-PRT-011 | `mcp4.png` | PRINT | 1.4 MB | `EBB7DC91258790FE` | série | direta | não | JÁ DESCRITO |
| AC-06-PRT-012 | `mcp5.png` | PRINT | 1.4 MB | `3F7D540DA6F9B8BB` | série | direta | não | JÁ DESCRITO |
| AC-06-PRT-013 | `plugins.png` | PRINT | 3.1 MB | `D6E429573D002B5D` | direta | direta | não | JÁ DESCRITO |

---

## 07_INTERFACE-E-DESIGN

**13 itens** — 5 repositórios · 5 prints · 3 vídeos · 0 planilhas · 0.32 GB

| ID | Caminho | Tipo | Tam. | SHA-256 | Índice | Catálogo | Transcr. | Estado |
|---|---|---|---|---|---|---|---|---|
| AC-07-REP-001 | `excalidraw-master` | REPO | 52.5 MB | dir · 1243 arq. · aninhado | direta | direta | não | JÁ DESCRITO |
| AC-07-REP-002 | `frontend-design-main` | REPO | 9.3 KB | dir · 3 arq. | direta | direta | não | JÁ DESCRITO |
| AC-07-REP-003 | `hyperframes-main` | REPO | 110.4 MB | dir · 4185 arq. · aninhado | direta | direta | não | JÁ DESCRITO |
| AC-07-REP-004 | `impeccable-main` | REPO | 76.1 MB | dir · 2201 arq. · aninhado | direta | direta | não | JÁ DESCRITO |
| AC-07-REP-005 | `ui-ux-pro-max-skill-main` | REPO | 12.8 MB | dir · 484 arq. · aninhado | direta | direta | não | JÁ DESCRITO |
| AC-07-PRT-001 | `dashboard1.png` | PRINT | 1 MB | `AAB6EE531951487E` | direta | direta | não | JÁ DESCRITO |
| AC-07-PRT-002 | `dashboard2.png` | PRINT | 1.4 MB | `E8CAEB562E422E3B` | série | direta | não | JÁ DESCRITO |
| AC-07-PRT-003 | `dashboard3.png` | PRINT | 918.5 KB | `DC4547447569E197` | série | direta | não | JÁ DESCRITO |
| AC-07-PRT-004 | `dashboard4.png` | PRINT | 1.5 MB | `EB6F073D81DC2538` | série | direta | não | JÁ DESCRITO |
| AC-07-PRT-005 | `dashboard5.png` | PRINT | 1.2 MB | `518DCF3E32385DA8` | série | direta | não | JÁ DESCRITO |
| AC-07-VID-001 | `exemplo .mp4` | VÍDEO | 15.2 MB | `D3CCFF036EC70356` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-07-VID-002 | `Gravando 2026-07-28 163723.mp4` | VÍDEO | 49.1 MB | `0D72EF229FB5B1FF` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-07-VID-003 | `Gravando 2026-07-29 092040.mp4` | VÍDEO | 3 MB | `7C4E279C5FF3E0E6` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |

**Notas de integridade desta área**

- `frontend-design-main` — **sem arquivo de licença na raiz efetiva**. Situação jurídica indeterminada até verificação.

---

## 08_CUSTO-E-CONTEXTO

**12 itens** — 3 repositórios · 1 prints · 8 vídeos · 0 planilhas · 0.26 GB

| ID | Caminho | Tipo | Tam. | SHA-256 | Índice | Catálogo | Transcr. | Estado |
|---|---|---|---|---|---|---|---|---|
| AC-08-REP-001 | `caveman-main` | REPO | 831.1 KB | dir · 167 arq. · aninhado | direta | direta | não | JÁ DESCRITO |
| AC-08-REP-002 | `headroom-main` | REPO | 57.1 MB | dir · 1967 arq. · aninhado | direta | direta | não | JÁ DESCRITO |
| AC-08-REP-003 | `pxpipe` | REPO | 31.1 MB | dir · 501 arq. | direta | direta | não | JÁ DESCRITO |
| AC-08-VID-001 | `Caching layers.mp4` | VÍDEO | 13.5 MB | `95C7C2C3E9D2DD3D` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-08-VID-002 | `Gravando 2026-07-28 153711.mp4` | VÍDEO | 44.5 MB | `4779F1249C5D9516` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-08-VID-003 | `Gravando 2026-07-28 155545.mp4` | VÍDEO | 51.3 MB | `6AEFF65BE08979CA` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-08-VID-004 | `Gravando 2026-07-28 163216.mp4` | VÍDEO | 10.1 MB | `66B279D261DBF011` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-08-VID-005 | `Gravando 2026-07-28 163244.mp4` | VÍDEO | 10.1 MB | `66B279D261DBF011` | direta | direta | **necessária** | DUPLICATA EXATA |
| AC-08-VID-006 | `Gravando 2026-07-28 214120.mp4` | VÍDEO | 4.1 MB | `4E9239D2BB085477` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-08-VID-007 | `Gravando 2026-07-29 090249.mp4` | VÍDEO | 3.1 MB | `CB50B41864BC2725` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-08-VID-008 | `handoff.mp4` | VÍDEO | 41.5 MB | `2789E1E271CDE926` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-08-PRT-001 | `Tolkenizaiton.png` | PRINT | 1.6 MB | `EA62DA1C5BDAFF8B` | direta | direta | não | JÁ DESCRITO |

**Notas de integridade desta área**

- `Gravando 2026-07-28 163244.mp4` — DUPLICATA EXATA de `Gravando 2026-07-28 163216.mp4` (mesmo SHA-256, 10.1 MB).

---

## 09_SEGURANCA-E-QUALIDADE

**10 itens** — 1 repositório · 2 prints · 7 vídeos · 0 planilhas · 0.12 GB

| ID | Caminho | Tipo | Tam. | SHA-256 | Índice | Catálogo | Transcr. | Estado |
|---|---|---|---|---|---|---|---|---|
| AC-09-REP-001 | `SkillSpector-main` | REPO | 2.4 MB | dir · 242 arq. · aninhado | direta | direta | não | JÁ DESCRITO |
| AC-09-PRT-001 | `Captura de tela 2026-07-28 152706.png` | PRINT | 1.3 MB | `1C25B7AF0B095587` | direta | direta | não | JÁ DESCRITO |
| AC-09-PRT-002 | `Captura de tela 2026-07-28 163441.png` | PRINT | 1.6 MB | `F77D18CFE628E74F` | direta | direta | não | JÁ DESCRITO |
| AC-09-VID-001 | `erros e correcóes.mp4` | VÍDEO | 41.8 MB | `2EE427F03CFBF5C1` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-09-VID-002 | `Gravando 2026-07-28 164102.mp4` | VÍDEO | 27.9 MB | `DADD32FE83806418` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-09-VID-003 | `Gravando 2026-07-28 203100.mp4` | VÍDEO | 10 MB | `A22DC01AF3A61516` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-09-VID-004 | `Gravando 2026-07-28 203833.mp4` | VÍDEO | 3.4 MB | `87DDC4FDF6612A91` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-09-VID-005 | `Gravando 2026-07-28 204533.mp4` | VÍDEO | 4 MB | `CEFCACDEF936F55C` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-09-VID-006 | `Gravando 2026-07-29 090207.mp4` | VÍDEO | 1.6 MB | `FFA2AA3762397410` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-09-VID-007 | `Gravando 2026-07-29 091447.mp4` | VÍDEO | 28.9 MB | `879770140F9DF65B` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |

---

## 10_APLICACOES-DE-NEGOCIO

**46 itens** — 6 repositórios · 16 prints · 23 vídeos · 1 planilha · 0.8 GB

| ID | Caminho | Tipo | Tam. | SHA-256 | Índice | Catálogo | Transcr. | Estado |
|---|---|---|---|---|---|---|---|---|
| AC-10-REP-001 | `claude-for-legal-main` | REPO | 3 MB | dir · 315 arq. | direta | direta | não | JÁ DESCRITO |
| AC-10-REP-002 | `claude-seo-main` | REPO | 3.8 MB | dir · 364 arq. | direta | direta | não | JÁ DESCRITO |
| AC-10-REP-003 | `financial-services-main` | REPO | 1.8 MB | dir · 372 arq. | direta | direta | não | JÁ DESCRITO |
| AC-10-REP-004 | `marketingskills-main` | REPO | 3.1 MB | dir · 419 arq. | direta | direta | não | JÁ DESCRITO |
| AC-10-REP-005 | `social-media-skills-blacktwist-main` | REPO | 334.7 KB | dir · 56 arq. | direta | direta | não | JÁ DESCRITO |
| AC-10-REP-006 | `social-media-skills-charlie947-main` | REPO | 133.2 KB | dir · 27 arq. | direta | direta | não | POSSÍVEL DUPLICATA |
| AC-10-PRT-001 | `avaliar IA com isso.png` | PRINT | 1.5 MB | `64AA014F7FD3FCD3` | direta | direta | não | JÁ DESCRITO |
| AC-10-PRT-002 | `Captura de tela 2026-07-28 152644.png` | PRINT | 1.1 MB | `F8E8938413A5A370` | direta | direta | não | JÁ DESCRITO |
| AC-10-PRT-003 | `Captura de tela 2026-07-28 162947.png` | PRINT | 1.3 MB | `8D587BBC9BFCA503` | direta | direta | não | JÁ DESCRITO |
| AC-10-PRT-004 | `Captura de tela 2026-07-28 163103.png` | PRINT | 1.3 MB | `64557C795F8383FD` | direta | direta | não | JÁ DESCRITO |
| AC-10-PRT-005 | `Captura de tela 2026-07-28 164440.png` | PRINT | 2 MB | `049C951AEACF45AD` | direta | direta | não | JÁ DESCRITO |
| AC-10-PRT-006 | `Captura de tela 2026-07-28 180038.png` | PRINT | 1.1 MB | `68952CF377C92DA4` | direta | direta | não | JÁ DESCRITO |
| AC-10-PRT-007 | `Captura de tela 2026-07-28 203019.png` | PRINT | 1.8 MB | `2BC80F67A3DDE95F` | direta | direta | não | JÁ DESCRITO |
| AC-10-VID-001 | `Gravando 2026-07-28 154241.mp4` | VÍDEO | 17.7 MB | `06A62BC09DFAB1B8` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-10-VID-002 | `Gravando 2026-07-28 155209.mp4` | VÍDEO | 59 MB | `B11867F9A2EDA07B` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-10-VID-003 | `Gravando 2026-07-28 155428.mp4` | VÍDEO | 106.4 MB | `B1BD4D087C66E41C` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-10-VID-004 | `Gravando 2026-07-28 163030.mp4` | VÍDEO | 13.6 MB | `C505946ECDDA9090` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-10-VID-005 | `Gravando 2026-07-28 165415.mp4` | VÍDEO | 12.6 MB | `FA4BBA01520E2B6B` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-10-VID-006 | `Gravando 2026-07-28 181253.mp4` | VÍDEO | 36 MB | `C962CEC5810B5D23` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-10-VID-007 | `Gravando 2026-07-28 204425.mp4` | VÍDEO | 5.4 MB | `4157EBDAC6BB43A2` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-10-VID-008 | `Gravando 2026-07-28 213549.mp4` | VÍDEO | 26.6 MB | `980922B24450ED62` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-10-VID-009 | `Gravando 2026-07-28 214422.mp4` | VÍDEO | 6.3 MB | `E54754AD9477F830` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-10-VID-010 | `Gravando 2026-07-29 085629.mp4` | VÍDEO | 3.6 MB | `DCB72717037106DE` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-10-VID-011 | `Gravando 2026-07-29 085700.mp4` | VÍDEO | 2.6 MB | `DBE4D7F496C46231` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-10-VID-012 | `Gravando 2026-07-29 091940.mp4` | VÍDEO | 5.7 MB | `454B48A0A2AA19EC` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-10-VID-013 | `Gravando 2026-07-29 092149.mp4` | VÍDEO | 2.7 MB | `1309F595714F3C9E` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-10-VID-014 | `_construcao-civil/3d de planta e alteraçao .mp4` | VÍDEO | 21.4 MB | `ACB7A05027494E80` | wildcard | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-10-VID-015 | `_construcao-civil/Gravando 2026-07-28 160740.mp4` | VÍDEO | 64.1 MB | `458FB3C1F4193FEC` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-10-VID-016 | `_construcao-civil/Gravando 2026-07-28 160920.mp4` | VÍDEO | 54.9 MB | `0A0CC29628F183BC` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-10-VID-017 | `_construcao-civil/Gravando 2026-07-28 161049.mp4` | VÍDEO | 8.1 MB | `B88657D2EAF892CB` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-10-VID-018 | `_construcao-civil/Gravando 2026-07-28 161155.mp4` | VÍDEO | 23.9 MB | `209424B2371FE9EF` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-10-VID-019 | `_construcao-civil/Gravando 2026-07-28 164000.mp4` | VÍDEO | 56.7 MB | `B844787C060DC6A9` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-10-VID-020 | `_construcao-civil/Gravando 2026-07-28 164422.mp4` | VÍDEO | 31.1 MB | `70731C4B988258E0` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-10-PLA-001 | `_construcao-civil/maiscontrole-dossie-jul2026.xlsx` | PLANILHA | 33.7 KB | `9B35BF396C57A0D4` | direta | direta | não | JÁ DESCRITO |
| AC-10-VID-021 | `_redes-sociais/configiraçao para melhorar instagram e coisas a fazer.mp4` | VÍDEO | 48.5 MB | `C49034BE41C61523` | wildcard | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-10-VID-022 | `_redes-sociais/estrategia de 300 dias 100k seguidores  intagram.mp4` | VÍDEO | 97.5 MB | `0F7CC1DE5826EF9C` | wildcard | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-10-PRT-008 | `_redes-sociais/workkflow conteudo0.png` | PRINT | 1.4 MB | `6DAFE579A904D6AB` | direta | direta | não | JÁ DESCRITO |
| AC-10-PRT-009 | `_redes-sociais/workkflow conteudo1.png` | PRINT | 897.9 KB | `CF8563E00B687FEB` | série | série | não | JÁ DESCRITO |
| AC-10-PRT-010 | `_redes-sociais/workkflow conteudo2.png` | PRINT | 1.3 MB | `0D6195AEB9E3E3E0` | série | série | não | JÁ DESCRITO |
| AC-10-PRT-011 | `_redes-sociais/workkflow conteudo3.png` | PRINT | 1.1 MB | `4C2C62E56412FEE8` | série | série | não | JÁ DESCRITO |
| AC-10-PRT-012 | `_redes-sociais/workkflow conteudo4.png` | PRINT | 1.3 MB | `954814C87819562F` | série | série | não | JÁ DESCRITO |
| AC-10-PRT-013 | `_redes-sociais/workkflow conteudo5.png` | PRINT | 998 KB | `C4354993F8570813` | série | série | não | JÁ DESCRITO |
| AC-10-PRT-014 | `_redes-sociais/workkflow conteudo6.png` | PRINT | 1 MB | `5555F0AC7FAF6158` | série | série | não | JÁ DESCRITO |
| AC-10-PRT-015 | `_redes-sociais/workkflow conteudo7.png` | PRINT | 1.2 MB | `7DF45C13DF675E65` | série | direta | não | JÁ DESCRITO |
| AC-10-VID-023 | `_renda-extra/afiliados.mp4` | VÍDEO | 83.4 MB | `6F1014323874CE99` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-10-PRT-016 | `_renda-extra/dores.png` | PRINT | 762.8 KB | `55BA1338BCB6123E` | direta | direta | não | JÁ DESCRITO |

**Notas de integridade desta área**

- `social-media-skills-charlie947-main` — POSSÍVEL DUPLICATA: os 17 SKILL.md sao byte-identicos a 17 dos 31 de `social-media-skills-blacktwist-main`; divergem apenas README, LICENSE, .gitignore, marketplace.json e validate-skills.sh.

---

## 11_FUNDAMENTOS-E-CARREIRA-TECNICA

**9 itens** — 0 repositórios · 6 prints · 3 vídeos · 0 planilhas · 0.1 GB

| ID | Caminho | Tipo | Tam. | SHA-256 | Índice | Catálogo | Transcr. | Estado |
|---|---|---|---|---|---|---|---|---|
| AC-11-PRT-001 | `Captura de tela 2026-07-28 152740.png` | PRINT | 342.8 KB | `F0AD3CC4192BBB67` | direta | direta | não | JÁ DESCRITO |
| AC-11-PRT-002 | `Captura de tela 2026-07-28 153539.png` | PRINT | 546.3 KB | `AA9D8DB70A1F6FF6` | direta | direta | não | JÁ DESCRITO |
| AC-11-PRT-003 | `Captura de tela 2026-07-28 154024.png` | PRINT | 1 MB | `848F5EAFF49EFE76` | direta | direta | não | JÁ DESCRITO |
| AC-11-PRT-004 | `Captura de tela 2026-07-28 162532.png` | PRINT | 1.4 MB | `04B2FAD39774BF53` | direta | direta | não | JÁ DESCRITO |
| AC-11-PRT-005 | `Captura de tela 2026-07-28 162625.png` | PRINT | 1.8 MB | `6DF1867A8C11EB18` | direta | direta | não | JÁ DESCRITO |
| AC-11-PRT-006 | `Captura de tela 2026-07-28 165045.png` | PRINT | 1.1 MB | `562638FD13BC8060` | direta | direta | não | JÁ DESCRITO |
| AC-11-VID-001 | `Gravando 2026-07-28 154434.mp4` | VÍDEO | 76.4 MB | `448A5B87A03BE51E` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-11-VID-002 | `Gravando 2026-07-28 163402.mp4` | VÍDEO | 6.7 MB | `F5750D43ABD33F1A` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |
| AC-11-VID-003 | `Gravando 2026-07-28 164739.mp4` | VÍDEO | 9.6 MB | `5B1824735830D0A4` | direta | direta | **necessária** | LACUNA DE TRANSCRIÇÃO |

---

## Fechamento do manifesto

| Estado | Itens |
|---|---:|
| PENDENTE | 0 |
| JÁ DESCRITO | 135 |
| LACUNA DE TRANSCRIÇÃO | 140 |
| DUPLICATA EXATA | 2 |
| POSSÍVEL DUPLICATA | 2 |
| INACESSÍVEL | 0 |
| FORA DE ESCOPO | 0 |
| **TOTAL** | **279** |

`PENDENTE = 0` não significa que o acervo esteja analisado. Significa que **todo item já chegou com descrição prévia de terceiro**. A Fase 2 deverá tratar os 279 itens como não verificados, independentemente do estado registrado aqui.


