> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

# 03 — RELATÓRIO DO INVENTÁRIO

**Frente:** Programa de Inteligência do Acervo · **Fase 0 — Governança e Inventário**
**Data:** 2026-07-29
**Fonte auditada:** `C:\Users\IA Lucas\OneDrive\Área de Trabalho\POJETOS\Para criar um novo projeto\Mais material`

---

## 1. Resumo executivo

O acervo foi inventariado e auditado contra o próprio índice. **A linha de base declarada está correta em todos os seis números.** Nenhum item declarado está fisicamente ausente; nenhum item físico ficou fora do catálogo local.

O acervo tem **77.605 arquivos e 5,55 GB no total**, dos quais **279 são itens catalogáveis** — a diferença é conteúdo interno de repositórios, fora da unidade de catalogação.

Seis achados de auditoria foram registrados. Quatro são de precisão de catálogo e não são bloqueantes. Dois merecem atenção:

- **4 dos 43 repositórios não têm arquivo de licença na raiz efetiva**, o que deixa sua situação jurídica indeterminada até verificação.
- **Duas pastas alheias (`work/`, `output/`) apareceram na raiz do acervo durante esta auditoria**, criadas por processo externo a esta frente. Nada foi movido ou apagado; o fato está registrado em §9.1. Os 279 itens catalogáveis foram recontados ao final e permanecem intactos.

O bloqueio real do acervo é de outra natureza: **142 vídeos, 2,91 GB, zero transcrições**. Isso é 51% dos itens catalogáveis permanentemente ilegíveis nas condições atuais.

**Nenhuma decisão oficial foi tomada. Nenhuma arquitetura foi proposta. Nenhum componente foi importado. Nenhuma fonte foi modificada por esta frente.**

## 2. Contagem real

### 2.1 Itens catalogáveis por tipo

| Tipo | Contagem física | Volume |
|---|---:|---:|
| Repositórios | 43 | 2,52 GB |
| Capturas de tela (`.png`) | 93 | 0,12 GB |
| Vídeos (`.mp4`) | 142 | 2,91 GB |
| Planilha (`.xlsx`) | 1 | 33,7 KB |
| **Total** | **279** | **5,55 GB** |

### 2.2 Itens catalogáveis por área

| Área | Repos | Prints | Vídeos | Planilha | Total | Volume |
|---|---:|---:|---:|---:|---:|---:|
| 01_DECIDIR-MODELO-E-ESCOPO | 0 | 5 | 6 | 0 | 11 | 0,16 GB |
| 02_PROJETAR-ARQUITETURA | 1 | 10 | 13 | 0 | 24 | 0,25 GB |
| 03_ORQUESTRACAO-DE-AGENTES | 10 | 8 | 13 | 0 | 31 | 1,08 GB |
| 04_MEMORIA-E-CONHECIMENTO | 7 | 13 | 12 | 0 | 32 | 1,63 GB |
| 05_SKILLS-E-PROMPTS | 6 | 14 | 31 | 0 | 51 | 0,41 GB |
| 06_CONECTORES-MCP | 4 | 13 | 23 | 0 | 40 | 0,42 GB |
| 07_INTERFACE-E-DESIGN | 5 | 5 | 3 | 0 | 13 | 0,32 GB |
| 08_CUSTO-E-CONTEXTO | 3 | 1 | 8 | 0 | 12 | 0,26 GB |
| 09_SEGURANCA-E-QUALIDADE | 1 | 2 | 7 | 0 | 10 | 0,12 GB |
| 10_APLICACOES-DE-NEGOCIO | 6 | 16 | 23 | 1 | 46 | 0,80 GB |
| 11_FUNDAMENTOS-E-CARREIRA-TECNICA | 0 | 6 | 3 | 0 | 9 | 0,10 GB |
| **Total** | **43** | **93** | **142** | **1** | **279** | **5,55 GB** |

### 2.3 Estado de catalogação

| Estado | Itens | % |
|---|---:|---:|
| PENDENTE | 0 | 0% |
| JÁ DESCRITO | 135 | 48,4% |
| LACUNA DE TRANSCRIÇÃO | 140 | 50,2% |
| DUPLICATA EXATA | 2 | 0,7% |
| POSSÍVEL DUPLICATA | 2 | 0,7% |
| INACESSÍVEL | 0 | 0% |
| FORA DE ESCOPO | 0 | 0% |

`PENDENTE = 0` **não significa acervo analisado.** Significa que todo item chegou com descrição prévia de terceiro. `INACESSÍVEL = 0` foi verificado: os 236 arquivos de mídia foram lidos com sucesso e todos os 43 repositórios foram enumerados.

`FORA DE ESCOPO = 0` é deliberado. O índice sinaliza `3d de planta e alteraçao .mp4` como *"único item fora do eixo, candidato a descarte"*. Isso é julgamento de escopo, e a Fase 0 não tem autoridade para tomá-lo. A sinalização fica registrada como **alegação do catálogo**, e o item permanece no manifesto.

### 2.4 Arquivos não catalogáveis

O acervo contém 77.605 arquivos. A diferença para os 279 itens é conteúdo interno de repositórios. Amostra do que existe lá dentro e **não** entrou no manifesto: 33.335 `.ts`, 16.412 `.md`, 7.150 `.py`, 3.357 `.json`, 825 `.png` e 219 `.mp4`.

Consequência prática: há **77 arquivos `.mp4` e 732 `.png` dentro de repositórios** que não são itens de evidência do acervo e não devem ser confundidos com os 142 vídeos e 93 prints catalogados.

## 3. Comparação com o índice

### 3.1 Linha de base declarada × medida

| Declarado no índice | Medido fisicamente | Veredito |
|---|---|---|
| 43 repositórios | 43 | **confere** |
| 93 capturas de tela | 93 | **confere** |
| 142 vídeos | 142 | **confere** |
| 1 planilha | 1 | **confere** |
| 279 itens catalogados | 279 | **confere** |
| 11 áreas temáticas | 11 | **confere** |
| Vídeos: 2,91 GiB, nenhum transcrito | 2,91 GiB, zero transcrições | **confere** |
| Planilha de 34 KB, dez abas | 33,7 KB, 10 abas | **confere** |

Abas da planilha, lidas de `xl/workbook.xml`: `01 Resumo`, `02 Planos e Precos`, `03 Modulos`, `04 Mapa Funcional`, `05 Stack Tecnica`, `06 Integracoes`, `07 Vulnerabilidades`, `08 Concorrentes`, `09 Backlog MVP`, `10 Fontes`.

### 3.2 Cobertura bidirecional

**Do físico para o índice** — 279 itens verificados:

| Forma de cobertura | Itens |
|---|---:|
| Nome literal no índice | 246 |
| Notação de série (`loop0-3.png`, `mcp0-5.png`, `Rag + langchain0-11.png`, `dashboard1-5.png`, `workkflow conteudo0-7.png`) | 30 |
| Apenas padrão agregado (`_redes-sociais/*.mp4`, `3d de planta*.mp4`) | 3 |
| **Sem nenhuma cobertura** | **0** |

**Do índice para o físico** — as 279 referências em crase do índice foram extraídas e conferidas. **Nenhuma aponta para item inexistente.** As referências sem correspondente físico direto são todas de natureza esperada: notação de série e wildcard, arquivos internos de repositórios (`CLAUDE.md`, `brand.json`, `prd.json`, `progress.txt`, `PRODUCT.md`, `DESIGN.md`, `skills/last30days/SKILL.md`), nomes de skills e comandos (`/goal`, `/redteam`, `task-observer`, `voice-builder`) e o próprio `_CONTEUDO.md`.

**Do físico para os `_CONTEUDO.md`** — cobertura de **279/279 (100%)**: 264 por nome literal, 15 por descrição de série slide a slide.

### 3.3 Alegações do índice verificadas por amostragem

| Alegação do índice | Verificação | Resultado |
|---|---|---|
| `Gravando 2026-07-28 165017.mp4` é duplicata exata de `164919` | SHA-256 | **confirmada** |
| `Gravando 2026-07-28 163244.mp4` é duplicata exata de `163216` | SHA-256 | **confirmada** |
| `gstack-Ahacad-main` é wrapper de `gstack-garrytan-main` | Comparação de 1.163 × 1.158 arquivos por hash | **confirmada** — 99,4% de sobreposição |
| `social-media-skills-charlie947-main` é subconjunto de `blacktwist` | Comparação por hash | **parcialmente confirmada** — ver §6.2 |
| `charlie947` tem 17 skills | Contagem de `SKILL.md` | **confirmada** — 17 |
| `blacktwist` tem "30+" skills | Contagem de `SKILL.md` | **confirmada** — 31 |
| `ECC-main` tem 3.322 arquivos | Contagem recursiva | **confirmada** — 3.322 |
| Repositórios em profundidade dupla | Inspeção de aninhamento | **confirmada** — 28 dos 43 |

## 4. Taxonomia encontrada

### 4.1 As 11 áreas

| # | Área | Pergunta central (literal do `_CONTEUDO.md`) |
|---|---|---|
| 01 | DECIDIR-MODELO-E-ESCOPO | que modelo usar para cada tipo de tarefa, e até onde levar o sistema |
| 02 | PROJETAR-ARQUITETURA | que forma o sistema tem — quais camadas, em que ordem de construção |
| 03 | ORQUESTRACAO-DE-AGENTES | como os agentes coordenam trabalho entre si — quem decide, quem executa, quem revisa |
| 04 | MEMORIA-E-CONHECIMENTO | como o sistema lembra, indexa e recupera |
| 05 | SKILLS-E-PROMPTS | como a capacidade é empacotada, versionada e instruída |
| 06 | CONECTORES-MCP | como o sistema alcança o mundo externo |
| 07 | INTERFACE-E-DESIGN | como o humano vê e comanda o sistema |
| 08 | CUSTO-E-CONTEXTO | como não estourar o orçamento de token nem a janela de contexto |
| 09 | SEGURANCA-E-QUALIDADE | como saber que o sistema funciona e que é seguro instalar o que se instala |
| 10 | APLICACOES-DE-NEGOCIO | que verticais provar primeiro, e como um sistema de agentes é empacotado por domínio |
| 11 | FUNDAMENTOS-E-CARREIRA-TECNICA | que base de engenharia de software uma pessoa precisa dominar para construir, avaliar e manter os sistemas do restante do acervo |

### 4.2 Pastas que não são áreas temáticas

| Pasta | Natureza | Conteúdo |
|---|---|---|
| `00_COMECE-AQUI` | Metadocumentação | 5 arquivos: `INDICE-COMPLETO.md`, `LEIA-PRIMEIRO.md`, `COMO-ADICIONAR-NOVO-MATERIAL.md` e 2 dumps brutos (`BRUTO-estrutura-dos-repositorios.txt`, `BRUTO-readmes-dos-repositorios.txt`). **Única pasta numerada sem `_CONTEUDO.md`** — esperado, pois não contém itens de evidência |
| `_ENTRADA-NOVO-MATERIAL` | Área de recepção | **Vazia** (0 itens) |

### 4.3 Subpastas agrupadoras

Só a área 10 tem segundo nível. São agrupadores temáticos, não áreas:

| Subpasta | Itens | Composição |
|---|---:|---|
| `_redes-sociais/` | 10 | 8 prints (carrossel) + 2 vídeos |
| `_construcao-civil/` | 8 | 7 vídeos + 1 planilha |
| `_renda-extra/` | 2 | 1 vídeo + 1 print |

### 4.4 Convenções dos `_CONTEUDO.md`

Estrutura recorrente, verificada nos 11 arquivos:

1. Título `# NN — NOME DA ÁREA`
2. Linha `**Pergunta desta pasta:**` — presente em 11/11
3. Seção de repositórios — rotulada `## Código` (áreas 02, 04, 06, 07, 08, 09) ou `## Prioridade alta` / `## Prioridade média` (áreas 03, 05) ou por vertical (área 10)
4. Seção de imagens — rotulada `## Imagens (já descritas — não precisa abrir)` ou nomeada pelo carrossel
5. Seção de vídeos — rotulada com aviso explícito `(NÃO são legíveis por IA)`
6. Seções incrementais por remessa: `## Nova remessa — 28/07/2026` e `## Nova remessa — 29/07/2026`
7. Algumas áreas trazem seção de tensão declarada: `## Divergência a resolver` (01), `## Decisão em aberto nesta pasta` (04), `## Lacuna a preencher (o achado desta pasta)` (09)

**Convenções de referência a séries.** Carrosséis são referenciados por intervalo no índice (`Rag + langchain0-11.png`) e detalhados slide a slide no `_CONTEUDO.md`. Isso é convenção, não omissão — foi tratado como cobertura válida no manifesto.

**Convenção declarada para vídeos.** Os catálogos rotulam a coluna de assunto como *"Título pelo conteúdo visível"*, ou seja, alegam derivar de frame visível, não do nome do arquivo. **Esta alegação não é verificável nesta fase** e fica registrada como alegação do autor do catálogo.

### 4.5 Estrutura dos repositórios

| Característica | Contagem |
|---|---:|
| Total | 43 |
| Em profundidade dupla (`nome-main/nome-main/`) | 28 |
| Com README na raiz efetiva | 43 |
| Com arquivo de licença na raiz efetiva | 39 |
| **Sem arquivo de licença** | **4** |

Repositórios sem licença: `ai-orchestrator-starter` (02), `second-brain-skills-main` (04), `andrej-karpathy-skills-main` (05), `frontend-design-main` (07).

Extremos de tamanho: `codebase-memory-mcp-main` (1,26 GB, 1.829 arquivos) e `openclaw-main` (289 MB, 23.953 arquivos) no topo; `frontend-design-main` (9,5 KB, 3 arquivos) e `ai-orchestrator-starter` (19,3 KB, 25 arquivos) na base.

Dois repositórios usam README em idioma não português/inglês na raiz: `hermes-agent-main` (`README.es.md`) e `open-notebook-main` (`README.dev.md`). O índice também registra `Agent-Reach-main` com README em chinês.

## 5. Integridade dos catálogos

| Verificação | Resultado |
|---|---|
| Itens do índice fisicamente ausentes | **0** |
| Itens físicos fora do índice | **0** (3 cobertos apenas por wildcard — ver §6.3) |
| Itens físicos fora do `_CONTEUDO.md` da área | **0** |
| Arquivos de 0 byte | **0** |
| Arquivos com assinatura de formato inválida | **0** de 236 verificados |
| Arquivos ilegíveis / erro de acesso | **0** de 236 |
| Áreas sem `_CONTEUDO.md` | 1 (`00_COMECE-AQUI`, esperado) |

Assinaturas conferidas nos 12 primeiros bytes: PNG (`89 50 4E 47`) em 93/93, MP4 (`ftyp` no offset 4) em 142/142, ZIP/OOXML (`50 4B`) em 1/1.

## 6. Duplicatas

### 6.1 Duplicatas exatas (SHA-256 idêntico)

| Par | Área | Tamanho |
|---|---|---|
| `Gravando 2026-07-28 164919.mp4` ≡ `Gravando 2026-07-28 165017.mp4` | 03 | 6,73 MB |
| `Gravando 2026-07-28 163216.mp4` ≡ `Gravando 2026-07-28 163244.mp4` | 08 | 10,11 MB |

Ambas já declaradas pelo índice e agora confirmadas por hash. Volume redundante: 16,84 MB.

Fora desses dois pares, **não há nenhum outro arquivo duplicado entre os 236 hasheados**.

### 6.2 Possíveis duplicatas (sobreposição medida, não total)

**`gstack-Ahacad-main` × `gstack-garrytan-main`** — 1.156 arquivos byte-idênticos. Cobertura: 99,4% de Ahacad por garrytan; 99,8% de garrytan por Ahacad.

Ahacad acrescenta 7 arquivos de empacotamento: `.claude-plugin/plugin.json`, `hooks/hooks.json`, `hooks/scripts/ensure-setup.sh`, `.gitmodules`, `.github/workflows/update-upstream.yml`, além de `README.md` e `.gitignore` próprios. Garrytan tem apenas `README.md` e `.gitignore` divergentes.

*Fato observado:* Ahacad é garrytan mais uma camada de empacotamento como plugin. A caracterização do índice está correta.

**`social-media-skills-charlie947-main` × `social-media-skills-blacktwist-main`** — o índice afirma que charlie947 é "subconjunto" de blacktwist.

*Fato observado:* a afirmação vale **no plano das skills, não no plano dos arquivos**. Os 17 `SKILL.md` de charlie947 são byte-idênticos a 17 dos 31 de blacktwist — nenhuma skill é exclusiva de charlie947. Mas 5 arquivos divergem: `README.md`, `LICENSE`, `.gitignore`, `.claude-plugin/marketplace.json` e `validate-skills.sh`. Cobertura de arquivos: 81,5%.

Blacktwist também traz `AGENTS.md`, `tools/REGISTRY.md` e diretórios `evals/` em cada skill, ausentes em charlie947.

**Nenhuma decisão de descarte é tomada aqui.** O registro serve para a Fase 2 não analisar o mesmo conteúdo duas vezes sem saber.

### 6.3 Cobertura apenas por padrão agregado

Três vídeos existem no índice apenas sob wildcard, sem nome individual — os dois de `_redes-sociais/` (`*.mp4`, "2 vídeos 153 MB") e `3d de planta e alteraçao .mp4` (`3d de planta*.mp4`). Todos os três **estão nomeados individualmente** no `_CONTEUDO.md` da área 10. Não é ausência de catalogação; é granularidade menor no índice-resumo.

## 7. Lacunas de transcrição

**142 vídeos. 2,91 GB. Zero transcrições.**

Busca por `.srt`, `.vtt`, `.sbv` e `.transcript` em todo o acervo (77.605 arquivos): **0 resultados**. Não há transcrição nem parcial nem oculta dentro de repositórios.

Distribuição por área:

| Área | Vídeos | % dos itens da área |
|---|---:|---:|
| 05_SKILLS-E-PROMPTS | 31 | 61% |
| 06_CONECTORES-MCP | 23 | 58% |
| 10_APLICACOES-DE-NEGOCIO | 23 | 50% |
| 02_PROJETAR-ARQUITETURA | 13 | 54% |
| 03_ORQUESTRACAO-DE-AGENTES | 13 | 42% |
| 04_MEMORIA-E-CONHECIMENTO | 12 | 38% |
| 08_CUSTO-E-CONTEXTO | 8 | 67% |
| 09_SEGURANCA-E-QUALIDADE | 7 | 70% |
| 01_DECIDIR-MODELO-E-ESCOPO | 6 | 55% |
| 07_INTERFACE-E-DESIGN | 3 | 23% |
| 11_FUNDAMENTOS-E-CARREIRA-TECNICA | 3 | 33% |

Descontando as 2 duplicatas exatas, são **140 vídeos distintos** a transcrever.

As áreas **08 e 09 são as mais comprometidas em proporção** — 67% e 70% do seu conteúdo é ilegível. A área 09 é agravada: tem apenas 1 repositório e 2 prints como material legível.

## 8. Itens não catalogados

**Nenhum.** Todos os 279 itens físicos aparecem no `_CONTEUDO.md` da respectiva área, e 276 aparecem no índice por nome ou notação de série.

Um item merece registro por outro motivo: `_ENTRADA-NOVO-MATERIAL/` está vazia. Não é lacuna — é a área de recepção, corretamente drenada.

## 9. Inconsistências encontradas

Nenhuma foi corrigida. Registro apenas.

| # | Inconsistência | Natureza | Gravidade |
|---|---|---|---|
| I-01 | `estrategia de 300 dias 100k seguidores  intagram.mp4` — o nome físico tem **dois espaços** entre "seguidores" e "intagram"; o índice grafa com **um** (51 vs 52 caracteres) | Divergência de nome entre catálogo e disco | Baixa — quebra busca por nome exato |
| I-02 | Três vídeos cobertos no índice apenas por wildcard, sem nome individual | Granularidade de catálogo | Baixa |
| I-03 | `social-media-skills-charlie947-main` descrito como "subconjunto" de blacktwist; é subconjunto de *skills*, não de *arquivos* (81,5% de sobreposição) | Imprecisão de catálogo | Baixa |
| I-04 | 4 repositórios sem arquivo de licença na raiz efetiva | Lacuna de procedência jurídica | **Média** |
| I-05 | 28 dos 43 repositórios em profundidade dupla (`nome-main/nome-main/`) | Armadilha de navegação — leitura ingênua conclui "repositório vazio" | Baixa (documentada no `LEIA-PRIMEIRO.md`) |
| I-06 | **Duas pastas alheias ao acervo apareceram na raiz durante esta auditoria:** `work/` (criada 2026-07-29 10:35:25, 26 arquivos) e `output/` (criada 10:40:42, 1 arquivo). Conteúdo: documentos de solicitação de farmácia (`.docx`, `.pdf`, `.py`, renders `.png`), sem relação com o acervo de pesquisa | Escrita concorrente por processo externo a esta frente | **Alta** — ver §9.1 |

### 9.1 Sobre I-06 — escrita concorrente no acervo

**Fato observado.** A primeira enumeração da raiz do acervo, feita no início desta auditoria, retornou 13 entradas: `_ENTRADA-NOVO-MATERIAL`, `00_COMECE-AQUI` e as 11 áreas numeradas. Uma reconferência ao final retornou 15 entradas — as mesmas 13 mais `work/` e `output/`, com data de criação **2026-07-29 10:35:25** e **10:40:42**, ou seja, durante a execução desta fase.

O conteúdo dessas pastas (`Solicitacao_Farmacia_*.docx`, `.pdf`, `inspect_inputs.py`, `prepare_unsigned_medical_review.py`, renders de página em `.png`) não tem relação com o acervo de pesquisa.

**Não foram criadas por esta frente.** Esta frente escreveu exclusivamente em `E:\LucasIA\Projetos\LucaX Enterprise OS\_SAIDA-COMPANY-OS\` e em diretório temporário de sessão. Todas as operações sobre o acervo foram de leitura.

**Nada foi movido, renomeado ou apagado.** As duas pastas permanecem onde estão. Corrigir seria alterar o acervo, o que esta fase não pode fazer.

**Efeito sobre as contagens.** A contagem bruta do acervo passou de 77.605 para 77.628 arquivos (+23) entre o início e o fim da auditoria. **A contagem de itens catalogáveis não mudou:** uma recontagem completa ao final confirmou 43 repositórios, 93 prints, 142 vídeos e 1 planilha — 279 itens. As pastas `work/` e `output/` não são áreas numeradas e não entram na unidade de catalogação. O manifesto permanece válido.

**Por que é gravidade alta.** Não pelo conteúdo, mas pela implicação: **o acervo não é um alvo estável**. Um processo externo escreve nele sem coordenação com esta frente. Se isso se repetir sobre uma área numerada, o manifesto e seus hashes ficam desatualizados sem aviso.

---

Erros de grafia nos nomes de arquivo do acervo (`melhroes iA 2026.png`, `ops 5 cenchmark.png`, `The agent knwoledge.png`, `Desgin pattern.mp4`, `Tolkenizaiton.png`, `workkflow conteudo*.png`, `configiraçao...`, `erros e correcóes.mp4`) são numerosos mas **consistentes entre disco e catálogo**. Não constituem inconsistência de inventário e não devem ser corrigidos — renomear quebraria o índice.

## 10. Riscos para as próximas fases

| # | Risco | Base factual | Consequência se ignorado |
|---|---|---|---|
| R-01 | **Metade do acervo é ilegível.** 140 vídeos distintos sem transcrição, 2,91 GB | §7 | A Fase 2 cobre no máximo 49% dos itens. Qualquer síntese de área que se apresente como completa será falsa |
| R-02 | **Cobertura desigual por área.** 09_SEGURANÇA tem 10 itens, dos quais 7 são vídeos ilegíveis; sobra 1 repositório e 2 prints | §7 | Síntese de segurança apoiada em base fina demais. O próprio índice já declara ausência de material sobre eval, tracing e regressão de prompt |
| R-03 | **Procedência jurídica indeterminada em 4 repositórios** | §4.5 | Estudo de material sem licença conhecida. Relevante em qualquer cenário futuro de internalização |
| R-04 | **Volume de leitura desproporcional.** 77.605 arquivos contra 279 itens; `codebase-memory-mcp-main` sozinho tem 1,26 GB | §2.4 | Estouro de contexto e custo na Fase 2 se a extração não for limitada a README, licença, docs, configs, testes e Specs |
| R-05 | **Descrição prévia induz ancoragem.** Todo item chegou com juízo de terceiro embutido, inclusive prioridade em estrelas | §2.3 | A Fase 1 pontua o julgamento alheio em vez da evidência. A rubrica precisa pontuar a fonte, não o catálogo |
| R-06 | **Alegações não verificadas tratadas como fatos.** Ex.: "83% de qualidade, 10× menos tokens" (arXiv:2603.27277), "600+ melhorias", "26,1% de skills com vulnerabilidade", "59–70% de fatura menor" | Índice e `_CONTEUDO.md` | Números de marketing entram na avaliação como se fossem medidos |
| R-07 | **Risco ativo de injeção de prompt.** O índice declara que o README de `05_SKILLS-E-PROMPTS/CL4R1T4S` contém injeção em leetspeak. O repositório é feito de system prompts extraídos | Índice, §05 | Uma IA lendo o repositório na Fase 2 pode ser instruída pelo conteúdo. **Não verificado nesta fase** |
| R-08 | **Títulos de vídeo alegadamente derivados de frame.** Os catálogos afirmam derivar de "conteúdo visível", não do nome | §4.4 | Se a alegação for falsa, os títulos são inferência a partir do nome — exatamente o que a governança proíbe |
| R-09 | **O acervo sofre escrita concorrente.** `work/` e `output/` surgiram na raiz durante esta auditoria, por processo externo | §9.1 | Os 236 hashes do manifesto podem envelhecer sem aviso. A Fase 2 deve reconferir os hashes dos itens que for extrair, antes de extrair |

## 11. Preparação necessária para a Fase 1

A Fase 1 constrói a rubrica de avaliação. O inventário indica quatro ajustes que a rubrica precisa absorver:

1. **Um critério de "legibilidade da evidência".** Metade dos itens não pode ser pontuada em qualidade de evidência porque não pode ser lida. Pontuar um vídeo não transcrito em qualquer eixo é inventar.
2. **O critério de licença precisa acomodar "ausente".** Não é nota 0 em uma escala de permissividade — é indeterminação, categoria diferente.
3. **Separar a nota da fonte da nota do catálogo.** Todo item chega com juízo de terceiro. A rubrica deve pontuar o que a fonte demonstra, não o que o catálogo afirma sobre ela.
4. **Um eixo para alegação não verificada.** Vários itens trazem números fortes sem verificação independente (R-06). A rubrica precisa poder registrar "alta alegação, baixa verificação".

Insumos prontos para a Fase 1, já disponíveis neste diretório:

- `02_MANIFESTO-DAS-FONTES.md` — os 279 itens com ID estável (`AC-<área>-<tipo>-<seq>`), hash, tamanho, estado e cobertura de catálogo
- Estados de duplicidade resolvidos — 4 itens não precisam de avaliação independente (2 duplicatas exatas + 2 possíveis)
- Universo efetivo de avaliação: **277 itens** (279 menos as 2 duplicatas exatas), dos quais **137 legíveis** e **140 bloqueados por transcrição**

## 12. Próxima ação exata

Nenhuma decisão oficial foi tomada nesta fase. Nenhuma arquitetura, Framework, Carta, ADR, Spec, Skill, Agente, Command, Workflow, política ou roadmap foi produzido. Nenhuma fonte foi modificada.

**Próxima ação:** iniciar a **Fase 1 — Rubrica**, criando `03_RUBRICA-DE-AVALIACAO.md` em `_SAIDA-COMPANY-OS/` com os 14 critérios previstos no programa (relevância, qualidade da evidência, maturidade, transferibilidade, manutenção, segurança, licença, integração, custo, impacto em contexto, dependência externa, reversibilidade, testes/evals, diferencial), cada um em escala 0–5 com âncoras descritas, mais os quatro ajustes de §11.

A Fase 1 define a rubrica; **não a aplica**. A aplicação é Fase 2. Os resultados permitidos (candidato forte, candidato a piloto, padrão a estudar, referência, exige pesquisa, rejeitado, duplicado) **não autorizam adoção** — dependem de avaliação pelos Frameworks oficiais 1.11–1.19.
