> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

# SÍNTESE — ÁREA 07 — INTERFACE E DESIGN

**Frente:** Programa de Inteligência do Acervo · **Fase 3 — Síntese** (missão **A3**) · **Data:** 2026-07-29 · **Avaliador:** Claude Opus 5 (Fase 3)

**Origem:** external-evidence · **Autoridade:** nenhuma · **Estado:** provisório · **Normativo:** não · **Adoção:** não-decidida

**Pergunta central da área (base de E01):** *como o humano vê e comanda o sistema.*

---

## 1. O que sabemos

A área tem 13 itens — 5 repositórios, 5 prints, 3 vídeos — e é a área mais limpa do acervo: zero disparos de V7, zero V1, zero V3, zero V6, zero rejeitados, zero duplicatas, e os 13 itens reconferem hash (V8 = 0) (`AC-07-REP-001` a `AC-07-VID-003`; fechamento da área 07). Os cinco repositórios estão todos em LV4 (`AC-07-REP-001` a `AC-07-REP-005`); os oito itens de mídia estão em LV3-V, e só um tem LV3-A aproveitável (`AC-07-VID-002`).

Sobre os repositórios:

- `AC-07-REP-001` (`excalidraw-master`) é um whiteboard colaborativo embutível como pacote npm, MIT íntegra, com suíte de testes declarada (`vitest.config.mts`), mas **não é interface de comando do sistema** — o próprio catálogo delimita: "não é ferramenta de agente" (`AC-07-REP-001`, E01 = 2). A criptografia ponta a ponta é **declarada**, não verificada (`AC-07-REP-001`, E06 = 3).
- `AC-07-REP-002` (`frontend-design-main`) é o menor repositório do acervo (3 arquivos, 9,3 KB), uma skill de direção de front-end **sem arquivo de licença na raiz efetiva** — o quarto e último caso I-04 / bloqueio B-02 do acervo — e com o conteúdo de `skills/` não lido (`AC-07-REP-002`). O catálogo o chama de "skill oficial da Anthropic", mas essa oficialidade **não é observável na fonte** (`NC = 2`); o que a fonte mostra são dois autores com endereço `@anthropic.com`, que é indício de origem, não declaração de oficialidade (`AC-07-REP-002`).
- `AC-07-REP-003` (`hyperframes-main`) renderiza HTML em vídeo sem editor, Apache-2.0 íntegra, maturidade 4, mas tem **E10 = 0** — 4.185 arquivos e 110,4 MB, a segunda ocorrência de E10 = 0 no acervo — e nenhuma data de manutenção observada apesar de existir `releases/` (`AC-07-REP-003`).
- `AC-07-REP-004` (`impeccable-main`) é o item de maior NF da área (NF = 4): declara **46 regras determinísticas de detecção que rodam sem LLM e sem chave de API**, 23 comandos, o par `PRODUCT.md` + `DESIGN.md` como contexto, e `tests/` com 394 arquivos incluindo `live-e2e/` e `skill-behavior/` (`AC-07-REP-004`). As contagens (46 regras, 23 comandos) são **conferíveis dentro da fonte mas não foram conferidas** sob o teto de leitura (`AC-07-REP-004`, E15 = 2).
- `AC-07-REP-005` (`ui-ux-pro-max-skill-main`) é um catálogo de estilos com tokens concretos (tipografia, paleta, humor, movimento), MIT íntegra, mas com **E06 = 2** — CLI npm mais Python, diretórios de captura de tela, sem `SECURITY.md` nem escopo declarado — e sem suíte de testes localizada (E13 = ND) (`AC-07-REP-005`). As contagens de badge ("161 reasoning rules", "67 UI styles") são alegações não conferidas (`AC-07-REP-005`, E15 = 2).

Sobre a mídia: os cinco prints de dashboard foram todos inspecionados visualmente pela trilha Codex (relatório `109`) e voltaram **CONFIRMADA**, sem exceção (`AC-07-PRT-001` a `AC-07-PRT-005`). Cada um carrega uma regra de design reproduzível em graus diferentes: token de cor literal (`AC-07-PRT-001`), hierarquia por cor única (`AC-07-PRT-002`), anatomia de cartão de KPI com proporção 3× (`AC-07-PRT-003`), grade consistente sem escala numérica (`AC-07-PRT-004`, o menos reproduzível) e remoção de ruído gráfico (`AC-07-PRT-005`). Dos três vídeos, dois não têm fala aproveitável — `AC-07-VID-001` tem trilha musical, `AC-07-VID-003` tem 1 palavra — e `AC-07-VID-002` é o único com narração, em STT automático **não revisado**, que proíbe citação exata (`AC-07-VID-001`, `AC-07-VID-002`, `AC-07-VID-003`).

Dois fatos estruturais ligam itens entre si: `AC-07-REP-004` declara no próprio README ter partido de `AC-07-REP-002` — primeira relação de linhagem observada na fonte, não afirmada pelo catálogo — e `AC-07-VID-003` lista cinco repositórios dos quais **dois já estão nesta área** (`AC-07-REP-004`, `AC-07-REP-005`), com o titular "Next Level Builder" da licença de `AC-07-REP-005` conferindo com o nome exibido no vídeo (`AC-07-REP-004`, `AC-07-VID-003`).

## 2. Fontes mais fortes e por quê

- **`AC-07-REP-004`** — NF = 4 (maior da área), LV4, apenas 1 ND, nenhuma porta de veto disparada, E13 = 4 com 394 arquivos de teste incluindo verificação de comportamento da skill, e catálogo NC = 3 descrito pela Fase 2 como "uma das descrições mais precisas do acervo". Ressalva registrada: E15 = 2 (contagens não conferidas) e ausência de `SECURITY.md` para uma extensão de navegador (`AC-07-REP-004`).
- **`AC-07-REP-001`** — NF = 3, LV4, 1 ND, nenhum veto, licença MIT íntegra, E13 = 3 com ponto de entrada de teste declarado, catálogo NC = 3. Ressalva: E10 = 1 (1.243 arquivos, 52,5 MB) e E05 = ND (`AC-07-REP-001`).
- **`AC-07-REP-003`** — NF = 3, LV4, 1 ND, nenhum veto, E03 = 4 e E13 = 3, catálogo NC = 3 com todos os detalhes conferidos. Ressalva pesada: E10 = 0 (`AC-07-REP-003`).
- **Os cinco prints como conjunto** — LV3-V com inspeção visual CONFIRMADA em `109` para os cinco, NC = 3 em todos; como evidência de *pixel* são fortes, mas carregam 5 ND cada (autoria, licença, data, segurança, verificação) e V2/V4 disparados (`AC-07-PRT-001` a `AC-07-PRT-005`).

Critério usado: nível de leitura (LV), NF, volume de ND, vetos disparados e NC — nunca popularidade. Badges de download, estrelas e `ADOPTERS.md` foram tratados como P-3 nas próprias fichas e não entram aqui como sinal (`AC-07-REP-001`, `AC-07-REP-003`, `AC-07-REP-005`).

## 3. Padrões recorrentes

- **Verificação determinística em vez de opinião de modelo.** O achado central de `AC-07-REP-004` — 46 regras que rodam sem LLM e sem chave — é o mesmo padrão que `AC-07-REP-005` tenta pelo lado do catálogo de regras/estilos e que `AC-07-VID-002` descreve como método ("especificar tokens, componentes e movimento antes de gerar") (`AC-07-REP-004`, `AC-07-REP-005`, `AC-07-VID-002`).
- **Documento de design como fonte da verdade.** O par `PRODUCT.md` + `DESIGN.md` escrito por `init` (`AC-07-REP-004`), as fichas de estilo com tokens (`AC-07-REP-005`) e o fechamento do catálogo sobre os cinco prints ("cabem num `DESIGN.md`" — juízo do catálogo, não fato) convergem para a mesma forma: capturar decisão visual em artefato legível antes de gerar interface (`AC-07-REP-004`, `AC-07-REP-005`, `AC-07-PRT-005`).
- **Os cinco prints formam um conjunto único**, fechado pelo próprio catálogo num parágrafo só: paleta, hierarquia de cor, anatomia de componente, grade e densidade (`AC-07-PRT-001` a `AC-07-PRT-005`).
- **Mídia sem artefato.** Nenhum dos oito itens de mídia entrega arquivo, repositório ou prompt; todos têm E04 ≤ 3 e os três vídeos têm E04 ≤ 2 — "só a ideia viaja" (`AC-07-VID-001`, `AC-07-VID-003`) (`AC-07-PRT-001` a `AC-07-VID-003`).
- **Manutenção não datada em toda a área.** E05 = ND nos 13 itens, sem exceção (`AC-07-REP-001` a `AC-07-VID-003`).
- **V2 e V4 nos oito itens de mídia**: autoria, licença e superfície de segurança de print/vídeo não são determináveis por inspeção (`AC-07-PRT-001` a `AC-07-VID-003`).

## 4. Conflitos e divergências

- **Catálogo × fonte em `AC-07-REP-002` (NC = 2):** o catálogo afirma "a skill oficial da Anthropic"; o README não usa a palavra "oficial". A síntese usa só a parte confirmada — skill empacotada como plugin, dois autores com endereço `@anthropic.com` — e nomeia a omissão: a oficialidade não é observável na fonte (`AC-07-REP-002`).
- **DEF-13 reincidente:** em `AC-07-REP-003` e `AC-07-REP-005`, PADRÃO A ESTUDAR e EXIGE PESQUISA são simultaneamente satisfeitos e a rubrica não declara precedência; prevaleceu EXIGE PESQUISA pelo critério §3.4. É divergência de classificação da rubrica, não de conteúdo (`AC-07-REP-003`, `AC-07-REP-005`).
- **Catálogo × imagem em alegações estéticas:** os prints confirmam o que está no pixel, mas as alegações de efeito ("melhora acessibilidade de quebra", `AC-07-PRT-002`; "algo que ninguém aponta mas todo mundo sente", `AC-07-PRT-004`) são juízos não medidos — o confirmado é a presença da regra, não o efeito (`AC-07-PRT-001` a `AC-07-PRT-005`).
- Não há divergência de escala, totais não reconciliados nem duplicatas nesta área (fechamento da área 07).

## 5. Candidatos fortes, pilotos e referências

Não há CANDIDATO FORTE na área (fechamento da área 07: 0).

- **PILOTO:** `AC-07-REP-001` (LV4, RP = 3, E06 = 3, E07 = 4, 1 ND, nenhum veto; restrições: E10 = 1, E05 = ND) e `AC-07-REP-004` (LV4, RP = 4, NF = 4, 1 ND, nenhum veto; restrições: E10 = 1, E05 = ND, contagens do README não conferidas, sem `SECURITY.md` para a extensão) (`AC-07-REP-001`, `AC-07-REP-004`).
- **PESQUISAR:** `AC-07-REP-002` (licença ausente — B-02 — e `skills/` não lido), `AC-07-REP-003` (E05 = ND e superfície de 110,4 MB não delimitada), `AC-07-REP-005` (E06 = 2, sem testes localizados, contagens de badge não conferidas) (`AC-07-REP-002`, `AC-07-REP-003`, `AC-07-REP-005`).
- **REFERENCIA:** os oito itens de mídia — `AC-07-PRT-001` a `AC-07-PRT-005` (insumos de consulta visual confirmados em `109`) e `AC-07-VID-001` a `AC-07-VID-003` (RP = 1–2, que fecha qualquer classe de candidato) (`AC-07-PRT-001` a `AC-07-VID-003`).

O registro é por ID, nunca ordenado por prioridade.

## 6. O que não adotar

- **Nenhum item foi rejeitado** nesta área (fechamento da área 07: REJEITADO = 0). O que segue não é rejeição — é registro do que a evidência **não sustenta**:
- As contagens de badge — "46 regras / 23 comandos" (`AC-07-REP-004`), "161 reasoning rules / 67 UI styles" (`AC-07-REP-005`) — não entram como fato: são alegações do autor conferíveis dentro da fonte, ainda não conferidas (`AC-07-REP-004`, `AC-07-REP-005`).
- A "oficialidade" de `AC-07-REP-002` não entra como fato: não é observável na fonte (`AC-07-REP-002`).
- A criptografia ponta a ponta de `AC-07-REP-001` é declarada, não verificada — não entra como propriedade confirmada (`AC-07-REP-001`).
- Os três nomes de repositório fora do acervo citados em `AC-07-VID-003` (`alchaincy/huashu-design`, `Leonxlnx/taste-skill`, `microsoft/playwright`) e a atribuição `pbakaus/impeccable` não foram conferidos — não entram como recomendação (`AC-07-VID-003`).
- As alegações de efeito estético dos prints (acessibilidade, percepção, "dashboard caro") são juízos não medidos — entram como prescrição do autor, não como resultado (`AC-07-PRT-002`, `AC-07-PRT-004`, `AC-07-PRT-005`).
- A fala de `AC-07-VID-002` é STT automático não revisado: "dashboards muito mais rápidos, designs absurdos, 100% customizáveis" e a versão de modelo mencionada **não são citáveis como fato** (`AC-07-VID-002`).

## 7. Riscos e dependências

- **Licença ausente (B-02):** `AC-07-REP-002` não tem arquivo de licença na raiz efetiva; qualquer uso depende de localizar licença e titularidade na origem pública. É pendência de pesquisa externa (`AC-07-REP-002`).
- **Superfície de execução sem controle documentado:** `AC-07-REP-005` roda CLI npm mais Python e captura telas, sem `SECURITY.md` nem escopo declarado — E06 = 2, abaixo do piso das classes de candidato. Delimitar essa superfície estoura o teto de leitura e **depende do proprietário** (`AC-07-REP-005`).
- **Pé de contexto pesado:** três dos cinco repositórios têm E10 ≤ 1 — 52,5 MB (`AC-07-REP-001`), 76,1 MB (`AC-07-REP-004`), 110,4 MB (`AC-07-REP-003`) — e o de `AC-07-REP-003` é E10 = 0 (`AC-07-REP-001`, `AC-07-REP-003`, `AC-07-REP-004`).
- **Extensão de navegador sem política de segurança:** `AC-07-REP-004` inclui extensão e funções em borda sem `SECURITY.md` observado; o que está documentado é que as regras determinísticas não enviam dado (`AC-07-REP-004`).
- **Dependência de terceiros não verificados:** `AC-07-VID-003` instrui a baixar cinco repositórios; três estão fora do acervo e nenhum nome fora do acervo foi confirmado (`AC-07-VID-003`).
- Nenhum item da área tem E06 = 1; não há risco declarado pendente de confirmação nesta área (fechamento da área 07).

## 8. Lacunas

- **E05 = ND nos 13 itens**: nenhuma data de manutenção foi observada em item algum da área (`AC-07-REP-001` a `AC-07-VID-003`).
- **Licença e conteúdo de `AC-07-REP-002`**: sem licença na raiz (B-02) e com `skills/` não lido — o artefato inteiro do item (`AC-07-REP-002`).
- **Superfície efetivamente distribuída de `AC-07-REP-003`**: 110,4 MB não delimitáveis a partir do que foi lido; a verificação (listar `releases/`, inspecionar `files[]` do `package.json`) está escrita e não executada (`AC-07-REP-003`).
- **Escopo de execução, testes e contagens de `AC-07-REP-005`**: leitura de `cli/` e `src/` estoura o teto — depende de autorização do proprietário (`AC-07-REP-005`).
- **Autoria, licença e data dos oito itens de mídia**: E03/E05/E06/E07/E13 = ND em cada um; V2 e V4 disparados nos oito (`AC-07-PRT-001` a `AC-07-VID-003`).
- **Contagens não conferidas**: 46 regras e 23 comandos (`AC-07-REP-004`); 161 regras e 67 estilos (`AC-07-REP-005`) — todas conferíveis dentro da própria fonte, nenhuma conferida (`AC-07-REP-004`, `AC-07-REP-005`).
- **Fala de `AC-07-VID-002` sem revisão humana**: a transcrição automática existe, mas a citação exata permanece proibida; o que a fala acrescenta além do aproximado é desconhecido (`AC-07-VID-002`).
- **Três repositórios citados em vídeo e fora do acervo**: identidade, licença e segurança desconhecidas (`AC-07-VID-003`).

## 9. Decisão provisória

| ID | Classe | Motivo (uma linha, com base na ficha) |
|---|---|---|
| `AC-07-REP-001` | PILOTO | RF = CANDIDATO A PILOTO: LV4, E06 = 3, E07 = 4, RP = 3, 1 ND, sem veto; E10 = 1 registrado |
| `AC-07-REP-002` | PESQUISAR | RF = EXIGE PESQUISA: V2 e V4 disparados — licença ausente (B-02) e `skills/` não lido |
| `AC-07-REP-003` | PESQUISAR | RF = EXIGE PESQUISA: E10 = 0 (110,4 MB) e E05 = ND, com verificação nomeada por fonte primária |
| `AC-07-REP-004` | PILOTO | RF = CANDIDATO A PILOTO: NF = 4, RP = 4, 1 ND, sem veto; E15 = 2 barrou CANDIDATO FORTE |
| `AC-07-REP-005` | PESQUISAR | RF = EXIGE PESQUISA: E06 = 2 abaixo do piso de candidato; verificação estoura o teto — depende do proprietário |
| `AC-07-PRT-001` | REFERENCIA | RF = REFERÊNCIA: insumo de consulta LV3-V confirmado em `109`; 5 ND, V2/V4 |
| `AC-07-PRT-002` | REFERENCIA | RF = REFERÊNCIA: idem; alegação de acessibilidade não medida |
| `AC-07-PRT-003` | REFERENCIA | RF = REFERÊNCIA: idem; o mais reproduzível dos cinco (E02 = 2, proporção 3× exibida) |
| `AC-07-PRT-004` | REFERENCIA | RF = REFERÊNCIA: idem; o menos reproduzível (E02 = 1, sem escala numérica) |
| `AC-07-PRT-005` | REFERENCIA | RF = REFERÊNCIA: idem; regra de remoção confirmada no pixel |
| `AC-07-VID-001` | REFERENCIA | RF = REFERÊNCIA: RP = 1 fecha classes de candidato; sem narração (trilha musical) |
| `AC-07-VID-002` | REFERENCIA | RF = REFERÊNCIA: RP = 2; único com fala aproveitável, STT não revisado proíbe citação exata |
| `AC-07-VID-003` | REFERENCIA | RF = REFERÊNCIA: RP = 2; lista de nomes, três fora do acervo e não conferidos |

Nenhuma classificação equivale a adoção oficial.

## 10. Experimento que poderia validá-la

**Proposta — não é plano aprovado.** A decisão provisória mais carregada da área é PILOTO para `AC-07-REP-004`, ancorada na alegação de que 46 regras determinísticas detectam vícios visuais sem LLM e sem chave. Um experimento possível: (1) contar as regras em `cli/engine/detect-antipatterns.mjs` e os comandos no diretório da skill — fechando E15 sem executar nada; (2) aplicar o detector a um conjunto pequeno de interfaces com vícios conhecidos (gradiente roxo-azul, cards aninhados — os exemplos que o próprio README nomeia) e a interfaces de controle, medindo taxa de acerto e falso positivo com a rubrica desta casa; (3) verificar por inspeção de código que a execução das regras não faz chamada de rede. Critério de sucesso declarado antes de rodar: contagens conferem com o README, detecção acima de um limiar definido, zero tráfego de rede observado. Esse mesmo desenho de contagem serviria, em separado, para `AC-07-REP-005` (161 regras, 67 estilos), cuja pendência, porém, depende de autorização do proprietário por estourar o teto de leitura (`AC-07-REP-004`, `AC-07-REP-005`).

## 11. Confiança da síntese

**Alta para a mídia e para a estrutura da área; média para os repositórios pendentes.** Justificativa rastreável:

- **Cobertura de LV:** 5 itens em LV4 (todos os repositórios) e 8 em LV3-V, um deles com LV3-A — a área inteira tem leitura direta ou inspeção visual confirmada; não há LV2 nem LV1 (`AC-07-REP-001` a `AC-07-VID-003`).
- **Volume de ND:** 48 de 195 células (24,6 %), a menor taxa de ND do acervo até a Fase 2; todos os 48 ND nomeiam o que os resolveria (fechamento da área 07).
- **V7 / NC=0 / EXIGE PESQUISA:** zero itens V7 e zero NC = 0 — nenhuma alegação sem prova sustenta item da área e nenhum catálogo foi contraditado pela inspeção; 3 dos 13 itens estão em EXIGE PESQUISA (`AC-07-REP-002`, `AC-07-REP-003`, `AC-07-REP-005`), e é sobre eles que a confiança cai: o valor declarado existe, mas a verificação que o fecharia não foi executada.
- **Peso específico:** os dois PILOTO e as oito REFERENCIA descansam em inspeção confirmada (LV4 ou `109`); os três PESQUISAR concentram licença ausente, superfície não delimitada e pendência que depende do proprietário (`AC-07-REP-001`, `AC-07-REP-004`, `AC-07-PRT-001` a `AC-07-VID-003`, `AC-07-REP-002`, `AC-07-REP-003`, `AC-07-REP-005`).

## 12. Cobertura

| ID | Tipo | LV | RF da ficha | Decisão provisória |
|---|---|---|---|---|
| `AC-07-REP-001` | REPO | LV4 | CANDIDATO A PILOTO | PILOTO |
| `AC-07-REP-002` | REPO | LV4 | EXIGE PESQUISA | PESQUISAR |
| `AC-07-REP-003` | REPO | LV4 | EXIGE PESQUISA | PESQUISAR |
| `AC-07-REP-004` | REPO | LV4 | CANDIDATO A PILOTO | PILOTO |
| `AC-07-REP-005` | REPO | LV4 | EXIGE PESQUISA | PESQUISAR |
| `AC-07-PRT-001` | PRINT | LV3-V | REFERÊNCIA | REFERENCIA |
| `AC-07-PRT-002` | PRINT | LV3-V | REFERÊNCIA | REFERENCIA |
| `AC-07-PRT-003` | PRINT | LV3-V | REFERÊNCIA | REFERENCIA |
| `AC-07-PRT-004` | PRINT | LV3-V | REFERÊNCIA | REFERENCIA |
| `AC-07-PRT-005` | PRINT | LV3-V | REFERÊNCIA | REFERENCIA |
| `AC-07-VID-001` | VÍDEO | LV3-V | REFERÊNCIA | REFERENCIA |
| `AC-07-VID-002` | VÍDEO | LV3-V + LV3-A | REFERÊNCIA | REFERENCIA |
| `AC-07-VID-003` | VÍDEO | LV3-V | REFERÊNCIA | REFERENCIA |

13 de 13 itens cobertos · 0 IDs faltando · 0 duplicatas · 0 rejeitados.

> Este arquivo é evidência externa, provisória e não normativa. Não autoriza adoção de nada.
