> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

# SÍNTESE — ÁREA 11 — FUNDAMENTOS E CARREIRA TÉCNICA

**Frente:** Programa de Inteligência do Acervo · **Fase 3 — Síntese** (missão **A3**) · **Data:** 2026-07-29 · **Avaliador:** Claude Opus 5 (Fase 3)

**Origem:** external-evidence · **Autoridade:** nenhuma · **Estado:** provisório · **Normativo:** não · **Adoção:** não-decidida

**Pergunta central da área (base de E01, registrada na ficha da área):** *que base de engenharia de software uma pessoa precisa dominar para construir, avaliar e manter os sistemas do restante do acervo.*

**Universo:** 9 itens — 6 PRINT + 3 VÍDEO — **sem repositório e sem planilha** (fechamento da área 11). É a menor área do acervo e a única sem repositório (fechamento da área 11).

---

## 1. O que sabemos

A área cobre três tipos de material, todos em imagem ou vídeo:

**Mapas e inventários de tecnologia.** `AC-11-PRT-001` é uma árvore de tecnologias web por categoria, sem critério de escolha, sem ordem de aprendizado e sem procedimento (`E02 = 1`). `AC-11-PRT-002` cobre o mesmo terreno com camadas separadas (linguagem, framework, biblioteca nas duas pontas) e acrescenta três eixos que a anterior não tem — ferramentas, conceitos e habilidades, todos nomeados e confirmados pela inspeção `109` (`E02 = 2`, `NC = 3`). `AC-11-PRT-005` lista dez ecossistemas de linguagem com ambientes, frameworks e ferramentas, sem critério nem ordem (`E02 = 1`); o título afirma "mais usadas" sem ranking, fonte, data ou critério — alegação do autor não verificada, explicitamente desarmada pelo próprio catálogo.

**Checklists e trilhas.** `AC-11-PRT-003` contrapõe "prompt → site" a uma pilha operacional nomeada item a item (arquitetura, front end, API, banco, autenticação, hospedagem, CI/CD, versionamento, segurança, limite de taxa, cache, registros, monitoramento, testes, escala), qualificada por `109` como "checklist ilustrativo, não arquitetura completa". É o único item do acervo que contrapõe protótipo a produto (`E14 = 3`). `AC-11-PRT-004` apresenta treze blocos nomeados e ordenados de trilha de engenharia de IA — de fundamentos de modelo a composição de carreira, passando por produção, segurança e avaliação **antes** de fronteira e carreira (`E14 = 3`); o recorte temporal do título e a seleção de ferramentas são alegações do autor não verificadas e datadas por construção.

**Modelo copiável falho.** `AC-11-PRT-006` pretende ser estrutura de pasta de front end copiável, mas a inspeção `109`, recontando nó a nó, encontrou dois defeitos estruturais no próprio original: `src/` desenhado dentro de `public/`, e `package-lock.json` repetido onde `package.json` não aparece. A árvore inteira é ilustração falha, não template copiável (`E02 = 1`); o princípio transfere, a árvore não (`E04 = 2`).

**Prática deliberada e conteúdo canônico.** `AC-11-VID-001` mostra quatro recomendações acionáveis visíveis nos quadros: engenharia reversa de projeto pronto; aprender a conversar com a ferramenta; dez projetos pequenos antes de um grande (prescrição do autor, não medição); **nunca aceitar código sem entender** — registrada na ficha como a única regra do acervo que *limita* o uso da ferramenta. O que a fala acrescenta é desconhecido: `97` registra que "a fala pode conter critérios adicionais", e esta frente não os supre por inferência (resíduo de transcrição, `00` §2.7). `AC-11-VID-002` e `AC-11-VID-003` são infográficos animados sem fala lexical confiável (`117`), com conteúdo canônico de ciência da computação: dez classes de complexidade de tempo pareadas com a estrutura de código que as produz, e quinze padrões de algoritmo nomeados — ambos com `E15 = 3` por **ausência de alegação**, justificativa escrita nas duas fichas para não virar precedente silencioso.

**O que a área não tem.** Nenhum item tem origem, data, canal, autoria ou termos identificáveis, e nenhuma superfície é inspecionável: `E03 · E05 · E06 · E07 · E13 = ND` nos nove itens, 45 de 135 células de eixo (33,3 %), a maior taxa de ND da rodada (fechamento da área 11). Sem repositório, não há artefato instalável, e `V2` e `V4` disparam nos nove itens — consequência direta: os nove caem em `RF = REFERÊNCIA` (fechamento da área 11).

## 2. Fontes mais fortes e por quê

"Forte" aqui é medido pelos dados da ficha — LV, NF, ND, vetos — e todos os nove itens estão no mesmo patamar estrutural: LV3-V (ou LV3-V + LV3-A em `AC-11-VID-001`, soma que não produz LV4), NF = 1 ou 2, 5 ND, `V2` e `V4` disparados. Nenhum é "forte" no sentido de evidência primária verificável; dentro desse teto comum, destacam-se por relevância potencial (`RP = 3`) e por inspeção confirmada:

- **`AC-11-PRT-004`** — `RP = 3 · 3/3`, `NC = 3` (treze blocos confirmados por `109`), `E14 = 3`: é o único item que ordena produção, segurança e avaliação antes de fronteira e carreira. Limite: recorte temporal e seleção de ferramentas não validados externamente (`E15 = 1`).
- **`AC-11-PRT-003`** — `RP = 3 · 3/3`, `NC = 3` (CONFIRMADA), `E14 = 3`: único item que contrapõe protótipo a produto num acervo majoritariamente promocional. Limite: a tese é argumento sem medida (`E15 = 1`).
- **`AC-11-VID-001`** — `RP = 3 · 3/3`, `NC = 5` (título confirmado por `97`), LV3-V + LV3-A: é o item com mais fala aproveitável da área, mas o conteúdo da fala além dos quadros permanece desconhecido. Limite: "dez projetos" é prescrição, não medição (`E15 = 1`).
- **`AC-11-PRT-002`** — `RP = 3 · 3/3`, `NC = 3` (CONFIRMADA): supera `AC-11-PRT-001` no mesmo terreno, com camadas corretas e três eixos adicionais nomeados.

Os demais (`AC-11-PRT-001`, `PRT-005`, `PRT-006`, `VID-002`, `VID-003`) têm `RP = 2`: inventários de nomes, ilustração falha ou referência canônica disponível em qualquer livro-texto (`E14 = 1` nos três últimos).

## 3. Padrões recorrentes

- **Inventário sem critério.** `AC-11-PRT-001`, `AC-11-PRT-005` e `AC-11-PRT-006` têm `E02 = 1`: listagem ou modelo sem critério de escolha, sem ordem, sem procedimento. `AC-11-PRT-005` chega a afirmar ordenação ("mais usadas") sem ranking — alegação desarmada pelo próprio catálogo.
- **Afirmação sem medida.** Nos seis prints, `E15 = 1` sempre pela mesma razão: completude afirmada pela forma (`AC-11-PRT-002`), tese sem dado (`AC-11-PRT-003`), título temporal e ferramentas sem validação (`AC-11-PRT-004`), ordenação sem critério (`AC-11-PRT-005`), boa prática sem justificativa (`AC-11-PRT-006`). Os dois vídeos canônicos invertem o padrão: `E15 = 3` por ausência de alegação (`AC-11-VID-002`, `AC-11-VID-003`).
- **Contra-peso ao viés promocional do acervo.** Três itens fazem o que o resto do acervo não faz: enumeram custo escondido (`AC-11-PRT-003`, `E14 = 3`), ordenam produção antes de fronteira (`AC-11-PRT-004`, `E14 = 3`) e limitam o uso da ferramenta ("nunca aceitar código sem entender", `AC-11-VID-001`).
- **Divergência de catálogo concentrada.** A área tem a maior taxa de discordância por item do acervo: 2 dos 9 itens com descrição de catálogo contestada por inspeção (`AC-11-PRT-001` com `NC = 0`; `AC-11-PRT-006` com `NC = 2`) — ver §4.

## 4. Conflitos e divergências

**`AC-11-PRT-001` — `NC = 0`, natureza distinta: crítica errada, não descrição errada.** O catálogo acusou o original de erro conceitual por posicionar Bootstrap, Tailwind e jQuery como frameworks de back end. A inspeção `109` mostra que o erro é **da leitura do catálogo**: as três tecnologias estão ligadas ao ramo **Front End → Libraries**, não ao back end. **A acusação é removida desta síntese** (`00` §3.1; instrução literal de `109`: "Remover a alegação de erro conceitual baseada nessa leitura"). O que permanece é o fato observado: a árvore de tecnologias por categoria existe na imagem e confere. É a divergência mais instrutiva do acervo, porque uma crítica soa como análise e contaminaria a síntese se repetida (ficha; `00` §3.1). Não é divergência de fonte: o hash confere e `V8` não dispara.

**`AC-11-PRT-006` — `NC = 2`, normalização inconsciente.** O catálogo percebeu que havia erro gráfico ("copie o princípio, não literalmente a árvore"), mas ao transcrever cometeu dois erros próprios: descreveu `public/` e `src/` como irmãos e **listou `package.json` na raiz**, que não está na imagem — completou a árvore com o arquivo que "deveria" estar lá. A omissão muda o sentido porque esconde que o defeito está no **original**, não só na transcrição. Esta síntese usa só a parte confirmada pela inspeção e **preserva os erros gráficos**, conforme instrução de `109` (`00` §3.2).

**Resíduo de transcrição — `AC-11-VID-001`.** A transcrição automática (`117`, 253 palavras, confiança 0,902) não é revisada e é proibida como citação literal; `97` registra que "a fala pode conter critérios adicionais", não supridos por inferência (`00` §2.7). As quatro recomendações citadas nesta síntese vêm dos quadros (LV3-V), não da fala.

**Sem conflito entre itens.** Não há afirmações contraditórias entre os nove itens; as divergências são todas de catálogo, não de fonte (V8 = 0 na área; fechamento da área 11).

## 5. Candidatos fortes, pilotos e referências

**Não há CANDIDATO-FORTE nem PILOTO nesta área** — todos os nove itens receberam `RF = REFERÊNCIA` (fechamento da área 11), mapeado para **REFERENCIA** no vocabulário da Fase 3. A causa é estrutural, não de mérito: sem repositório não há artefato instalável para pilotar, e `V2`/`V4` disparam nos nove por `E06 = ND` e `E07 = ND` (fechamento da área 11). Nenhuma classificação equivale a adoção oficial.

Dentro de REFERENCIA, as fichas registram diferenciais de relevância potencial (sem ordenação de prioridade): `AC-11-PRT-002`, `AC-11-PRT-003`, `AC-11-PRT-004` e `AC-11-VID-001` com `RP = 3`; os demais com `RP = 2` (§2).

## 6. O que não adotar

- **A árvore de `AC-11-PRT-006` como template copiável** — o próprio original tem dois defeitos estruturais confirmados por recontagem nó a nó (`109`): `src/` dentro de `public/` e `package-lock.json` repetido sem `package.json`. Copiar literalmente propagaria os defeitos (`E04 = 2`).
- **A alegação de "erro conceitual" sobre `AC-11-PRT-001`** — contradita por inspeção direta (`109`); removida da síntese (§4).
- **O título "mais usadas" de `AC-11-PRT-005` como ranking** — alegação do autor sem fonte, data ou critério; o próprio catálogo registra "não é ranking nem trilha de aprendizado".
- **O número "dez projetos" de `AC-11-VID-001` como medida** — prescrição do autor, não verificada (`E15 = 1`).
- **A seleção de ferramentas e o recorte temporal de `AC-11-PRT-004` como critério** — alegações do autor, datadas por construção; o catálogo registra "logotipos são exemplos, não requisitos".
- **A fala de `AC-11-VID-001` além dos quadros** — desconhecida até revisão humana da transcrição (§4).

Nenhum item foi REJEITADO na área (fechamento da área 11); esta seção registra exclusões de conteúdo, não rejeição de itens.

## 7. Riscos e dependências

- **`E06 = ND` em todos os nove itens** — nenhuma superfície foi inspecionada procurando dado sensível. É risco **não avaliado**, não risco confirmado nem ausência de risco; `V2` dispara nos nove exatamente por isso (fechamento da área 11). Nenhum item da área tem `E06 = 1` (risco declarado).
- **`E07 = ND` em todos os nove itens** — autoria e termos desconhecidos; `V4` dispara nos nove (fechamento da área 11). Qualquer reúso depende de identificar autoria e licença, o que não é determinável a partir de imagem ou vídeo.
- **Datção por construção em `AC-11-PRT-004`** — a trilha se declara de um ano específico e escolhe ferramentas sem critério exposto; o conteúdo envelhece com o ecossistema que nomeia.
- **Dependência de transcrição em `AC-11-VID-001`** — o valor residual do item (o que a fala acrescenta) depende de revisão humana de áudio, bloqueio `B-01`/`B-05` (`00` §2.7).
- **Área sem repositório** — nada aqui é executável ou verificável por inspeção de código; toda a evidência é LV3 (fechamento da área 11).

## 8. Lacunas

- **Origem e data de todos os nove itens: desconhecida** (`E03 = ND` uniforme; fechamento da área 11).
- **Canal datado: ausente em todos** (`E05 = ND` uniforme).
- **Autoria e termos: desconhecidos em todos** (`E07 = ND` uniforme).
- **Fala de `AC-11-VID-001` além dos quadros: desconhecida** — "a fala pode conter critérios adicionais" (`97`), não supridos por inferência.
- **Critério de seleção de `AC-11-PRT-004` e `AC-11-PRT-005`: desconhecido** — nenhum dos dois expõe como escolheu blocos ou ecossistemas (`E15 = 1` em ambos).
- **Medida de eficácia do método de `AC-11-VID-001` e da tese de `AC-11-PRT-003`: inexistente nas fontes** (`E15 = 1` em ambos).
- **Nenhuma pendência `EXIGE PESQUISA` formal nesta área** — todos os itens estão em REFERÊNCIA (fechamento da área 11); as lacunas acima são de Bloco A, não verificações pendentes nomeadas.

## 9. Decisão provisória

Vocabulário fechado da Fase 3; mapeamento direto do `RF` da ficha (REFERÊNCIA → REFERENCIA). Registro por ID, sem ordenação de prioridade. Nenhuma classificação equivale a adoção oficial.

| ID | Classe | Motivo (uma linha) |
|---|---|---|
| `AC-11-PRT-001` | REFERENCIA | `RF = REFERÊNCIA` (§9 da rubrica): insumo de consulta LV3-V; inventário sem critério (`E02 = 1`, `RP = 2`); acusação do catálogo removida por `109` |
| `AC-11-PRT-002` | REFERENCIA | `RF = REFERÊNCIA`: mapa com camadas corretas e três eixos adicionais confirmados por `109` (`NC = 3`, `RP = 3`) |
| `AC-11-PRT-003` | REFERENCIA | `RF = REFERÊNCIA`: único contraponto protótipo × produto do acervo (`E14 = 3`); tese sem medida (`E15 = 1`) |
| `AC-11-PRT-004` | REFERENCIA | `RF = REFERÊNCIA`: treze blocos confirmados (`NC = 3`), produção antes de fronteira (`E14 = 3`); recorte temporal não validado |
| `AC-11-PRT-005` | REFERENCIA | `RF = REFERÊNCIA`: inventário de dez ecossistemas confirmado (`NC = 3`), sem critério (`E02 = 1`); título "mais usadas" não verificado |
| `AC-11-PRT-006` | REFERENCIA | `RF = REFERÊNCIA`: ilustração falha, não template (`109`); `NC = 2` — usa-se só a parte confirmada, erros gráficos preservados |
| `AC-11-VID-001` | REFERENCIA | `RF = REFERÊNCIA`: quatro regras acionáveis nos quadros (`RP = 3`); fala além dos quadros desconhecida (resíduo `97`/`117`) |
| `AC-11-VID-002` | REFERENCIA | `RF = REFERÊNCIA`: conteúdo canônico (dez classes de complexidade) sem alegação (`E15 = 3`); conveniência sobre livro-texto (`E14 = 1`) |
| `AC-11-VID-003` | REFERENCIA | `RF = REFERÊNCIA`: conteúdo canônico (quinze padrões) sem alegação (`E15 = 3`); mapa de estudo, "não implica adoção" (`97`) |

## 10. Experimento que poderia validá-la

**Proposta, não plano aprovado.** A decisão provisória uniforme (REFERENCIA × 9) decorre de uma causa estrutural — ausência de repositório — e não de mérito avaliado. O que poderia validá-la ou alterá-la:

1. **Teste de utilidade como checklist.** Aplicar a pilha operacional de `AC-11-PRT-003` como checklist de lacunas sobre um sistema real do acervo (por exemplo, um repositório da área 03 ou 10) e registrar quantos itens da pilha o sistema efetivamente cobre. Se a taxa de cobertura discriminasse sistemas de forma útil, o item justificaria reavaliação acima de REFERENCIA; se não discriminasse, confirmaria `RP = 3` como teto. Depende do proprietário (avaliação própria, classe DEPENDE DO PROPRIETÁRIO de `00` §2.2).
2. **Revisão humana da transcrição de `AC-11-VID-001`** (bloqueio `B-01`/`B-05`, `00` §2.7): fecharia a única lacuna de fala da área e determinaria se há critérios adicionais além das quatro regras dos quadros.
3. **Identificação de origem e termos** dos quatro itens com `RP = 3` (`AC-11-PRT-002`, `PRT-003`, `PRT-004`, `VID-001`): resolveria `V2`/`V4` nesses itens (EXIGE PESQUISA EXTERNA, `00` §2.2) e abriria caminho para reavaliação. Sem isso, REFERENCIA é o teto estrutural da área.

## 11. Confiança da síntese

**Média.** Justificativa rastreável:

- **Cobertura de LV:** 9/9 itens em LV3 (8 LV3-V, 1 LV3-V + LV3-A) — cobertura total, mas nenhum item acima de LV3; nenhuma leitura direta de artefato executável (fechamento da área 11).
- **Volume de ND:** 45 de 135 células (33,3 %), a maior taxa da rodada, uniforme por causa única (área sem repositório) — limita qualquer afirmação sobre origem, risco e termos (fechamento da área 11).
- **V7:** zero itens na área (`00` §3.5) — nenhuma alegação sem prova sustenta a relevância de item algum.
- **NC=0 / NC=2:** 1 item com crítica de catálogo contradita (`AC-11-PRT-001`, removida) e 1 parcial (`AC-11-PRT-006`, usado só na parte confirmada) — a maior taxa de discordância por item do acervo, o que recomenda cautela ao citar qualquer descrição de catálogo da área.
- **EXIGE PESQUISA:** zero pendências formais na área (fechamento da área 11).
- **Área pequena:** 9 itens — a menor do acervo. A uniformidade da classificação (9 × REFERENCIA) é fato estrutural, não convergência de mérito, e a amostra pequena impede generalização sobre a pergunta central da área.

A confiança é média porque o que a síntese afirma é integralmente rastreável às fichas e às inspeções `109`/`97`/`117`, mas o teto de evidência (LV3, 33,3 % de ND, zero repositórios) limita o que qualquer síntese desta área pode afirmar.

## 12. Cobertura

Todos os 9 IDs da área, com a decisão provisória de cada um (registro por ID, sem ordenação):

| ID | Tipo | Decisão provisória |
|---|---|---|
| `AC-11-PRT-001` | PRINT | REFERENCIA |
| `AC-11-PRT-002` | PRINT | REFERENCIA |
| `AC-11-PRT-003` | PRINT | REFERENCIA |
| `AC-11-PRT-004` | PRINT | REFERENCIA |
| `AC-11-PRT-005` | PRINT | REFERENCIA |
| `AC-11-PRT-006` | PRINT | REFERENCIA |
| `AC-11-VID-001` | VÍDEO | REFERENCIA |
| `AC-11-VID-002` | VÍDEO | REFERENCIA |
| `AC-11-VID-003` | VÍDEO | REFERENCIA |

**Controle:** 9 de 9 IDs sintetizados · 0 duplicatas · 0 fichas de delta · 0 itens V7 · 1 item NC=0 (acusação removida) · 1 item NC=2 (parte confirmada apenas) · 1 resíduo de transcrição (`AC-11-VID-001`) · 0 fontes originais abertas nesta fase · 0 notas alteradas.

> Este arquivo é evidência externa, provisória e não normativa. Não autoriza adoção de nada.
