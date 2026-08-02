> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

# SÍNTESE — ÁREA 01 — MODELOS E ESCOPO

**Frente:** Programa de Inteligência do Acervo · **Fase 3 — Síntese** (missão **A3**) · **Data:** 2026-07-29 · **Avaliador:** Claude Opus 5 (Fase 3)

**Origem:** external-evidence · **Autoridade:** nenhuma · **Estado:** provisório · **Normativo:** não · **Adoção:** não-decidida

**Pergunta central da área:** *que modelo usar para cada tipo de tarefa, e até onde levar o sistema.*

**Universo sintetizado:** 11 itens — 0 REPO · 5 PRINT · 6 VÍDEO · 0 PLANILHA (`07_FICHAS-DE-EVIDENCIA/01_DECIDIR-MODELO-E-ESCOPO.md`, cabeçalho). Sem NC=0, sem duplicatas, sem fichas de delta nesta área.

---

## 1. O que sabemos

O que a área oferece, com a força que a evidência permite:

- A área **não contém nenhum artefato executável**: os 11 itens são documentais (prints e vídeos), todos em `LV3` (visual, ou visual + áudio bruto), nenhum em `LV4` (AC-01-PRT-001 … AC-01-VID-006, campo `LV` de cada ficha).
- A pergunta "até onde levar o sistema" é endereçada por **um** item: o infográfico de maturidade de AC-01-PRT-001, que decompõe adoção em camadas (superfície → combinação de ferramentas por função → sistemas que substituem workflows) — conteúdo visual confirmado pela inspeção (`NC = 3`, CONFIRMADA em `105`), sem números decisivos (`E15 = 3`).
- A pergunta "que modelo para que tarefa" é endereçada por dois subconjuntos:
  - **Comparações quantitativas**: AC-01-PRT-003 (placar Elo de frontend, fonte citada mas não conferida, `E15 = 1`), AC-01-PRT-005 (tabela de nove famílias de benchmark nomeadas, números não verificáveis, `E15 = 1`), AC-01-VID-001 (gateway de modelos com alegações numéricas sem fonte, `E15 = 0` → `V7`), AC-01-VID-002 (padrão orquestrador/executor com dois percentuais sem fonte, `E15 = 0` → `V7`), AC-01-VID-004 (posição de um modelo aberto em arenas, `E15 = 1`). **Nenhum número desses cinco itens é fato para esta síntese** — todos são alegações do autor não verificadas.
  - **Inventários opinativos por categoria**: AC-01-PRT-002 (meme, `RP = 1`), AC-01-PRT-004 (pirâmide de ferramentas por categoria, sem critério), AC-01-VID-003 (ranking por categoria, sem rubrica), AC-01-VID-005 (ranking em faixas subjetivas), AC-01-VID-006 (qualificação adjetival por categoria). Os cinco são preferência de autor, declarada como tal nas próprias fichas (`E02 = 1` em todos; AC-01-VID-003: "o ranking não tem rubrica nem teste reproduzível").
- O padrão recorrente com algum conteúdo arquitetural é a **separação planejador/executor por custo** (AC-01-VID-002, `E04 = 3` — "a separação planejador/executor não depende de ambiente do autor; os nomes de modelo, sim") e a **camada de roteamento entre agente e provedores** (AC-01-VID-001, `E04 = 2` — "o padrão é transferível; a implementação demonstrada depende de conta, chave e painel de terceiro"). Ambos são padrões, não produtos avaliados.
- **33,3% dos eixos da área estão em `ND`** (55 de 165, fechamento da área 01), concentrados em `E03`, `E05`, `E06`, `E07`, `E13` — maturidade, manutenção, segurança, licença e testes são **desconhecidos** em todos os 11 itens.
- Onde a fala existe sem revisão humana, ela permanece desconhecida: AC-01-VID-005 (nomes de produto grafados errado pelo STT — "Chate a PT", "X-Filge", "Manos", "notebook LLM", "BigView" — identificação inequívoca depende de revisão) e AC-01-VID-006 (a fala provável **não nomeia** as ferramentas — "esse aqui" — e nenhum nome foi inferido).

## 2. Fontes mais fortes e por quê

Justificativa exclusivamente pelos dados das fichas (LV, NF, ND, vetos):

- **AC-01-PRT-001** é a fonte mais sólida da área em termos relativos: `NF = 2` (a maior nota de fonte da área), `NC = 3` (descrição confirmada contra os pixels em `105`), `E15 = 3` (nenhum número em jogo, portanto nada a desmentir) e conteúdo que endereça metade da pergunta central (`E01 = 3`). Permanece fraca em absoluto: 5 dos 15 eixos em `ND`, incluindo segurança e licença (`V2` e `V4` disparadas).
- **AC-01-VID-002** tem a **relevância potencial mais alta da área** (`RP = 3`, único item com `E04 = 3`) e o catálogo mais confiável (`NC = 5`, método declarado e confirmado pelos quadros) — mas é também o item com a **fonte mais fraca da área** (`NF = 0`, único), porque sua proposta depende de dois números sem fonte (`E15 = 0` → `V7`). Os números não entram como fato; o que sobrevive é o padrão qualitativo separação planejador/executor, que o próprio acervo repete em AC-08-VID-003, AC-08-VID-007 e AC-03-VID-005 (E14 da ficha).
- As demais nove fontes têm `NF = 1` (AC-01-PRT-002 … AC-01-VID-006 exceto as duas acima): evidência isolada, não reprodutível, sem insumo nem procedimento.
- **Nenhuma fonte da área é forte em sentido absoluto**: todas têm `LV = 3`, todas têm `V2` e `V4` disparadas (`E06 = ND` e `E07 = ND` nos 11 itens), e todas carregam 5 ND de 15 eixos.

## 3. Padrões recorrentes

- **Escolha por tarefa, não por modelo único**: aparece como padrão transferível em AC-01-PRT-003 (`E04 = 2`, "escolher modelo por tarefa medindo distância de desempenho"), AC-01-PRT-005 (`E04 = 2`, "matriz benchmark × modelo para decidir roteamento") e, na forma de inventário por categoria, em AC-01-PRT-004, AC-01-VID-003, AC-01-VID-005 e AC-01-VID-006. A recorrência **não verifica** a afirmação — é agregação de material público (`E14 = 2` ou `1` em todos).
- **Separação de papéis por custo** (planejador caro + executor barato, e o inverso executor barato + consultor sob demanda): AC-01-VID-002; a ficha registra que o mesmo padrão reaparece dentro do acervo em AC-08-VID-003, AC-08-VID-007 e AC-03-VID-005.
- **Camada de roteamento/agregação entre agente e provedores de modelo**: AC-01-VID-001 (`E04 = 2`), com remissão do próprio material a um equivalente conhecido (OpenRouter, `E14`).
- **Inventário como alternativa a construir**: AC-01-PRT-004 (alegação do catálogo: "mapear candidatos a integrar em vez de construir… trate como inventário, não como ranking" — não verificada) e AC-01-PRT-001 (camada "combinação por função").
- **Databilidade como fraqueza comum**: números e seleções são "do contexto e da data do autor" (AC-01-PRT-003, AC-01-PRT-004, AC-01-PRT-005, AC-01-VID-005 — `E04`/`E15` das fichas).

## 4. Conflitos e divergências

- **Catálogo × fonte, duas divergências parciais (`NC = 2`) que mudam o sentido**:
  - AC-01-PRT-003: o catálogo omite as posições intermediárias 6–8, 11 e 14 do placar e simplifica a ordem; a síntese usa apenas a parte confirmada (top 5 e famílias seguintes, conforme `105`) e nomeia a omissão.
  - AC-01-PRT-005: o catálogo afirma 13 linhas e transcreve 10 (omite reasoning multidisciplinar sem/com ferramentas e Biology) e **normaliza para "Fable 5" uma célula cujo texto observado é "Mythos 5"**; a identidade de "Mythos 5" está entre as lacunas nomeadas.
- **Prescrição de terceiro detectada e não obedecida**: AC-01-PRT-005 contém a instrução "a arquitetura deve prever roteamento de modelo por tipo de tarefa", classificada na ficha como `DECISÃO DE ESCOPO DE TERCEIRO` — "instrução não obedecida (§14.5)". Esta síntese registra a existência da instrução; não a adota.
- **Divergência de transcrição automática**: AC-01-VID-001 (STT grafou "OmniRoot"/"Cloud Code"; o visual grafa "OmniRoute"/"Claude Code") e AC-01-VID-005 (cinco nomes de produto grafados errado). Nenhum texto bruto foi corrigido (`117`, regra de uso).
- **Convergência sem verificação**: o padrão planejador/executor aparece em quatro itens do acervo (AC-01-VID-002 + três das áreas 03 e 08) — é repetição temática, não confirmação (regra `P-3`).

## 5. Candidatos fortes, pilotos e referências

- **Candidatos fortes: nenhum.** `V4` (`E07 = ND`) disparada nos 11 itens impede `CANDIDATO FORTE` e `CANDIDATO A PILOTO` em toda a área (tabelas de veto de AC-01-PRT-001 a AC-01-VID-006).
- **Pilotos: nenhum**, pelo mesmo motivo.
- **Padrões a estudar: nenhum classificado como tal** — nenhum RF da área é `PADRÃO A ESTUDAR`. Os padrões qualitativos existentes (AC-01-VID-001, AC-01-VID-002) estão sob teto `EXIGE PESQUISA` por `V7`.
- **Referências (insumos de consulta, `LV ≥ 3`, sem número decisivo em jogo)**: AC-01-PRT-001 (mapa de maturidade), AC-01-PRT-002 (percepção social, `RP = 1`), AC-01-PRT-004 (inventário por categoria), AC-01-VID-003 (ranking opinativo por categoria), AC-01-VID-005 (ranking em faixas, com resíduo de STT), AC-01-VID-006 (qualificação adjetival, fala que não nomeia ferramentas).

## 6. O que não adotar

Registro do que a evidência **não sustenta**, sem que isso constitua rejeição formal (nenhum item da área recebeu `RF = REJEITADO`):

- **Nenhum número como fato**: os Elos de AC-01-PRT-003, os percentuais de AC-01-PRT-005, os números de gateway de AC-01-VID-001, os dois percentuais de AC-01-VID-002 e as posições de arena de AC-01-VID-004 são todos `NÃO VERIFICADA` nas fichas — não servem de base para roteamento, compra ou escolha de modelo.
- **Rankings opinativos como critério**: AC-01-PRT-002 ("não deve orientar roteamento nem compra", alegação do catálogo), AC-01-VID-003 (sem rubrica nem teste), AC-01-VID-005 e AC-01-VID-006 (preferência pessoal declarada).
- **A ferramenta retratada em AC-01-VID-001**: a ficha não pontuou a ferramenta (E08, nota literal) e a superfície de segurança é declarada e não inspecionada — "o material demonstra colar chave de agregador em painel de terceiro" (`E06 = ND`, superfície declarada, **não** risco confirmado).
- **A instrução arquitetural de terceiro** em AC-01-PRT-005 (§14.5 — não obedecida na Fase 2, não adotada nesta síntese).
- **Nomes de produto vindos do STT bruto** de AC-01-VID-005 e a identidade das ferramentas de AC-01-VID-006 — permanecem desconhecidos.

## 7. Riscos e dependências

- **Superfície de segurança declarada, não confirmada**: AC-01-VID-001 (`E06 = ND`) — custódia de chave de API, destino do tráfego e escopo de permissão do gateway são desconhecidos; a verificação escrita na ficha exige leitura da documentação primária, sem instalar.
- **Licença desconhecida em 11 de 11 itens** (`E07 = ND`, `V4` em todas as fichas): nenhum conteúdo da área tem autoria e termos identificados.
- **Dependência de verificação externa**: 4 itens exigem pesquisa fora do acervo (AC-01-PRT-003 — metodologia do placar; AC-01-PRT-005 — origem dos benchmarks e identidade de "Mythos 5"; AC-01-VID-001 — identidade, licença e custódia de chave do produto; AC-01-VID-004 — licença de pesos e metodologia da arena).
- **Dependência do proprietário**: AC-01-VID-002 — a verificação escrita na ficha é um benchmark local próprio (planejador caro + executor barato × modelo único), que só o proprietário pode autorizar; a Fase 3 não a executou.
- **Dependência de revisão humana de áudio**: AC-01-VID-005 e AC-01-VID-006 (resíduos de transcrição; o bloqueio `B-01` permanece aberto).
- **Databilidade**: toda seleção de produtos da área é datada (AC-01-PRT-004, AC-01-VID-003, AC-01-VID-005, AC-01-VID-006) — o valor de consulta decai com o tempo e não há como medir esse decaimento com o material disponível.

## 8. Lacunas

- **AC-01-VID-002 (depende do proprietário)**: procedência e método dos dois percentuais exibidos e identidade/versão dos modelos do carrossel; a verificação é um benchmark local que esta fase não executou.
- **AC-01-PRT-003 (pesquisa externa)**: data, versão, amostragem e metodologia do placar, mais as posições 6–8, 11 e 14 omitidas pelo catálogo.
- **AC-01-PRT-005 (pesquisa externa)**: origem, data, versão e metodologia das nove famílias de benchmark; identidade de "Mythos 5"; as três linhas omitidas pelo catálogo.
- **AC-01-VID-001 (pesquisa externa)**: identidade, repositório, licença, modelo de custódia de chave e termos de serviço do produto; verificação dos números alegados (que permanecem fora da síntese como fato).
- **AC-01-VID-004 (pesquisa externa)**: identidade, procedência dos pesos, licença de uso comercial e requisitos de hardware do modelo divulgado; data e metodologia da arena citada.
- **AC-01-VID-005 e AC-01-VID-006 (revisão de áudio)**: nomes de produto e identidade das ferramentas permanecem desconhecidos.
- **Estrutural**: `E03`, `E05`, `E06`, `E07`, `E13` são `ND` nos 11 itens — maturidade, manutenção, segurança, licença e testes são desconhecidos em toda a área.
- **Ausência de artefato**: a área não contém nenhum repositório, código ou configuração inspecionável — não há evidência de implementação para a pergunta "até onde levar o sistema" além do mapa conceitual de AC-01-PRT-001.

## 9. Decisão provisória

Nenhuma classificação equivale a adoção oficial. Registro por ID, sem ordenação por prioridade.

| ID | Classe | Motivo (uma linha, citando a ficha) |
|---|---|---|
| AC-01-PRT-001 | REFERENCIA | `RF = REFERÊNCIA` — mapa de maturidade confirmado (`NC = 3`), sem número em jogo (`E15 = 3`), sob teto `V2`/`V4` |
| AC-01-PRT-002 | REFERENCIA | `RF = REFERÊNCIA` — meme opinativo (`E02 = 1`, `RP = 1`); consulta sem peso decisório |
| AC-01-PRT-003 | PESQUISAR | `RF = EXIGE PESQUISA` — Elo forte não conferido (`E15 = 1`) + omissões do catálogo (`NC = 2`); lacuna endereçável |
| AC-01-PRT-004 | REFERENCIA | `RF = REFERÊNCIA` — inventário por categoria sem critério (`E02 = 1`); uso como mapa, não como ranking |
| AC-01-PRT-005 | PESQUISAR | `RF = EXIGE PESQUISA` — números não verificáveis (`E15 = 1`), `NC = 2` com normalização indevida ("Mythos 5") |
| AC-01-VID-001 | PESQUISAR | `RF = EXIGE PESQUISA` — `V7` (`E15 = 0`): proposta depende de números sem fonte; sem conteúdo avaliável além do próprio texto e dos quadros |
| AC-01-VID-002 | PESQUISAR | `RF = EXIGE PESQUISA` — `V7` (`E15 = 0`, `NF = 0`): padrão relevante (`RP = 3`), números proibidos como fato; verificação depende do proprietário |
| AC-01-VID-003 | REFERENCIA | `RF = REFERÊNCIA` — ranking opinativo sem rubrica (`E02 = 1`); `NC = 5` confirma o assunto, não o mérito |
| AC-01-VID-004 | PESQUISAR | `RF = EXIGE PESQUISA` — posição em arena não conferida (`E15 = 1`); licença de pesos desconhecida |
| AC-01-VID-005 | REFERENCIA | `RF = REFERÊNCIA` — classificação subjetiva (`E02 = 1`); nomes de produto permanecem desconhecidos (resíduo STT) |
| AC-01-VID-006 | REFERENCIA | `RF = REFERÊNCIA` — qualificação adjetival (`E02 = 1`); fala provável não nomeia ferramentas |

**Distribuição:** REFERENCIA 6 · PESQUISAR 5 · CANDIDATO-FORTE 0 · PILOTO 0 · ADAPTAR-PADRAO 0 · REJEITAR 0 · DUPLICATA 0.

## 10. Experimento que poderia validá-la

**Proposta — não é plano aprovado.** A decisão provisória dominante da área (5 de 11 em PESQUISAR) repousa sobre números de terceiros não verificáveis. O experimento que a validaria é o que a própria ficha de AC-01-VID-002 escreve como verificação: **um benchmark local, com tarefas e critérios definidos por esta casa, comparando a configuração planejador caro + executor barato contra modelo único**, medindo custo e desempenho no corpus real da casa. Se o padrão se sustentar sob medição própria, a tese "escolha por tarefa" (AC-01-PRT-003, AC-01-PRT-005) passa de alegação agregada a observação local; se não se sustentar, as cinco pendências de pesquisa perdem relevância prática. O experimento depende de autorização do proprietário e está fora do escopo desta frente.

## 11. Confiança da síntese

**Média-baixa**, com justificativa rastreável:

- **Cobertura de LV**: 11 de 11 itens em `LV3` (visual ou visual + áudio bruto), **zero** em `LV4` — a área inteira repousa sobre inspeção indireta (quadros e relatórios `95`/`105`), não sobre leitura direta da fonte por esta frente.
- **Volume de ND**: 55 de 165 eixos em `ND` (33,3%, fechamento da área 01) — um terço do espaço de avaliação é desconhecido, e os cinco eixos desconhecidos são sempre os mesmos (maturidade, manutenção, segurança, licença, testes).
- **Itens V7**: 2 de 11 (AC-01-VID-001, AC-01-VID-002) — incluindo o item de maior relevância potencial da área, cuja fonte tem `NF = 0`.
- **Itens NC=2**: 2 de 11 (AC-01-PRT-003, AC-01-PRT-005), ambos com omissões que mudam o sentido e ambos na classe PESQUISAR.
- **Itens EXIGE PESQUISA**: 5 de 11 (45%) — quase metade da área está pendente de verificação que esta fase não executou.
- **Pontos que sustentam alguma confiança**: 11/11 hashes reconferidos sem divergência; zero itens NC=0; nenhuma descrição de catálogo contraditada por inspeção; as fichas nomeiam explicitamente o que é opinião e o que é alegação.

## 12. Cobertura

| ID | Tipo | RF da ficha | Decisão provisória |
|---|---|---|---|
| AC-01-PRT-001 | PRINT | REFERÊNCIA | REFERENCIA |
| AC-01-PRT-002 | PRINT | REFERÊNCIA | REFERENCIA |
| AC-01-PRT-003 | PRINT | EXIGE PESQUISA | PESQUISAR |
| AC-01-PRT-004 | PRINT | REFERÊNCIA | REFERENCIA |
| AC-01-PRT-005 | PRINT | EXIGE PESQUISA | PESQUISAR |
| AC-01-VID-001 | VÍDEO | EXIGE PESQUISA | PESQUISAR |
| AC-01-VID-002 | VÍDEO | EXIGE PESQUISA | PESQUISAR |
| AC-01-VID-003 | VÍDEO | REFERÊNCIA | REFERENCIA |
| AC-01-VID-004 | VÍDEO | EXIGE PESQUISA | PESQUISAR |
| AC-01-VID-005 | VÍDEO | REFERÊNCIA | REFERENCIA |
| AC-01-VID-006 | VÍDEO | REFERÊNCIA | REFERENCIA |

**11 de 11 IDs sintetizados.** Nenhum item fora da tabela; nenhuma classe fora do vocabulário fechado.

> Este arquivo é evidência externa, provisória e não normativa. Não autoriza adoção de nada.
