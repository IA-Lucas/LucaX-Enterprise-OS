> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

# 03 — MATRIZ TRANSVERSAL

**Frente:** Programa de Inteligência do Acervo · **Fase 3 — Síntese** (missão **A3**)
**Data:** 2026-07-29 · **Avaliador:** Claude Opus 5 (Fase 3)
**Entrada:** as onze sínteses de `01_AREAS/`, as pré-correções de `00_PRE-CORRECOES-E-CORRESPONDENCIA.md` e o registro de `04_REGISTRO-DE-DECISOES-PROVISORIAS.md`.

**Origem:** external-evidence · **Autoridade:** nenhuma · **Estado:** provisório · **Normativo:** não · **Adoção:** não-decidida

> Esta matriz consolida o que se repete, o que conflita e o que falta **entre** áreas. Nada aqui cria capacidade oficial, ordena prioridades ou autoriza adoção. Toda linha cita IDs de fichas.

---

## 1. Padrões presentes em várias áreas

| # | Padrão | Áreas onde aparece | Evidência (IDs) |
|---|---|---|---|
| T-01 | **Número forte sem método** — percentuais, contagens e prova social apresentados sem corpus, método ou contrafactual | 01, 03, 05, 06, 08, 09, 10, 11 | 25 itens com `V7` (`00` §3.5); badges tratados por `P-3` em `AC-03-REP-001`/`009`, `AC-05-VID-008`–`028`, `AC-06-VID-007`–`022`, `AC-09-PRT-001`, `AC-10-VID-019` |
| T-02 | **Portão humano antes do irreversível** — spec antes de código, aprovação antes de efeito externo | 03, 05, 06, 10 | `AC-03-REP-010` (portão spec→código), `AC-05-REP-001` (portão antes de avançar), `AC-06-VID-023` (gateway sem confirmação nem limite declarado), `AC-10-REP-003` (observado), `AC-10-REP-001` (só alegado) |
| T-03 | **Memória/instrução persistente em arquivo versionável** — `CLAUDE.md`, `AGENTS.md`, `SKILL.md`, `PRODUCT.md`/`DESIGN.md`, `progress.txt` | 02, 03, 04, 05, 07, 10 | `AC-02-VID-012` (inspeção, não o catálogo), `AC-02-VID-010`, `AC-03-VID-011`, `AC-04-VID-010`, `AC-07-REP-004`, `AC-10-REP-004` |
| T-04 | **Laço avaliador com critério de parada** como mecanismo de qualidade | 02, 03, 08, 09 | `AC-02-PRT-006`/`008`, `AC-03-VID-006`, `AC-08-VID-008`, `AC-09-VID-001` |
| T-05 | **Separação planejador caro × executor barato** | 01, 03, 08 | `AC-01-VID-002` (não medido — V7), `AC-03-VID-005`, `AC-08-VID-003`, `AC-08-VID-007` |
| T-06 | **Verificação determinística** (sem LLM/chave) em vez de opinião de modelo | 07, 09 | `AC-07-REP-004`, `AC-09-REP-001` |
| T-07 | **Repetição promocional tomada por evidência** — clusters que repetem a mesma afirmação | 05, 06 (ecos em 02, 04, 10) | cluster de 15 fichas (`00` §4.3): 9 em 05, 6 em 06; lacuna de identidade contada uma vez em `AC-05-VID-009`. **Repetir não verifica (P-3).** |
| T-08 | **Assimetria leitura × escrita** — leitura ampla declarada, escrita com portão | 06, 10 | princípio em prints (`AC-06-PRT-*`); ausente como implementação nos vídeos; `AC-10-REP-003` |
| T-09 | **Descoberta ≠ verificação** — busca em catálogo confundida com varredura de segurança | 05, 09 | `AC-09-VID-007` (NC=0: busca, não varredura) × `AC-09-REP-001` (scanner real); `AC-05-VID-018` |
| T-10 | **"O padrão transfere, o artefato não"** — `E04` baixo recorrente em mídia | 01, 05, 07, 11 | padrão medido nas fichas de prints/vídeos das quatro áreas |
| T-11 | **Auto-instalação × inspeção prévia** de skills de terceiro | 05, 09 | `AC-05-REP-003` (contra-exemplo, V1 confirmada), `AC-09-REP-001`, `AC-09-VID-007` |
| T-12 | **Compressão/roteamento de contexto com medição ausente** — técnicas nomeadas, economia jamais conferida | 01, 03, 08 | sete níveis de `AC-08-VID-004` (inspeção: Meter, Budget, Route, Compact, Prune, Delegate, Batch); nenhum número verificado |

## 2. Ferramentas e repositórios candidatos

Sem ordenação de prioridade. Classe completa e motivos por ID: `04_REGISTRO-DE-DECISOES-PROVISORIAS.md` e síntese da área.

| Decisão provisória | IDs |
|---|---|
| CANDIDATO-FORTE (7) | `AC-03-REP-001`, `AC-03-REP-004`, `AC-03-REP-005`, `AC-03-REP-010`, `AC-04-REP-002`, `AC-04-REP-004`, `AC-04-REP-006` |
| PILOTO (11) | `AC-03-REP-002`, `AC-03-REP-008`, `AC-05-REP-001`, `AC-06-REP-003`, `AC-07-REP-001`, `AC-07-REP-004`, `AC-08-REP-001`, `AC-08-REP-002`, `AC-09-REP-001`, `AC-10-REP-002`, `AC-10-REP-003` |
| ADAPTAR-PADRAO (1) | `AC-03-REP-007` |

Leituras transversais sobre esse conjunto:

- **Os 7 CANDIDATO-FORTE estão em apenas 2 áreas** (03 e 04) e todos são repositórios com licença lida e `LV4` — a força vem da inspeção, não do conteúdo temático.
- **Bloco A integralmente determinado existe em 3 repositórios do acervo inteiro** (`AC-08-REP-003`, `AC-10-REP-002`, `AC-10-REP-004`), sempre pela mesma causa: licença + versão datada + testes presentes na fonte.
- **Nenhum candidato tem medição de eficácia lida por esta frente** — o que existe é instrumento de medição na própria fonte, não aberto (teto de `05` §8): `AC-08-REP-003` (`eval/results`, `FINDINGS.md`, testes `abstention`/`gist-recall`/`needle-haystack`).
- `AC-03-REP-006` tem superfície efetiva não delimitável (23.953 arquivos / 289,3 MB sem manifesto de distribuição) — é PESQUISAR, não candidato.

## 3. Capacidades sugeridas — sem criá-las oficialmente

Padrões do acervo que **se candidatam** a futura avaliação pelos Frameworks oficiais. Isto **não** cria `capabilities/`, não nomeia componente e não define arquitetura.

| Sugestão de capacidade (provisória) | Base de evidência |
|---|---|
| Roteamento de modelo por custo/tarefa | T-05 — `AC-01-VID-002`, `AC-08-VID-003`/`007`, `AC-03-VID-005` |
| Memória persistente em arquivo versionável, lida por todas as skills | T-03 — `AC-02-VID-012`, `AC-04-VID-010`, `AC-10-REP-004`, `AC-07-REP-004` |
| Portões humanos antes de efeitos irreversíveis | T-02 — `AC-03-REP-010`, `AC-05-REP-001`, `AC-10-REP-003` |
| Laços avaliadores com critério de parada explícito | T-04 — `AC-09-VID-001`, `AC-03-VID-006`, `AC-08-VID-008` |
| Compressão de contexto medida (meter → budget → route → compact → prune → delegate → batch) | T-12 — `AC-08-VID-004`, `AC-08-REP-001`/`002`/`003` |
| Verificação determinística de skills antes da instalação | T-06/T-09 — `AC-09-REP-001`, `AC-07-REP-004` |
| Deliberação por papéis com rubrica própria | `AC-03-PRT-007` (hipótese não medida — V7) |

## 4. Conflitos entre fontes

| # | Conflito | Lados | Estado |
|---|---|---|---|
| C-01 | **Enchimento de janela de contexto** | `AC-04-VID-010` ("quanto mais contexto, melhor") × `AC-08-VID-008` (queda de qualidade com enchimento) | **aberto** — nenhum dos dois mede; a síntese não escolhe |
| C-02 | **Via de memória** | markdown puro × RAG próprio × RAG hospedado (área 04, §4 da síntese) | **aberto, declarado** |
| C-03 | **Novidade alegada × artefato existente** | `AC-03-VID-005` vende como novidade (com "80%" não verificado, V7) o acoplamento que `AC-03-REP-001` entrega como artefato oficial com licença lida | registrado; prevalece o inspecionável |
| C-04 | **Estimativa apresentada como resultado** | `AC-08-VID-006` apresenta como medido números que a fonte primária `AC-08-REP-003` declara estimativa a medir | a síntese adota a forma da fonte primária |
| C-05 | **Contagens do mesmo artefato** | `AC-03-VID-001` × `AC-03-REP-002`: 181 skills/47 subagentes/78 comandos × estrelas 50 mil × 211,9 mil+ | **não reconciliado** — nenhum número citado como fato |
| C-06 | **Contradições internas de fonte** | `AC-03-REP-009` ("100+" × "60+" agentes; v3.25.6 × v3.5.0); `AC-06-REP-002` (v1.5.0 manifesto × v1.3.1 changelog); `AC-06-REP-004` (portão de 84% declarado × `tests/` ausente); `AC-05-REP-004` (345 × 355; `tests/` ausente) | registrados; nenhum lado adotado |
| C-07 | **"Único blueprint executável"** | catálogo de `AC-02-REP-001` × repositórios executáveis das áreas 03 e 08 | alegação do catálogo descartada da síntese |
| C-08 | **Mandato de descarte de terceiro** | índice do acervo mandou descartar `AC-10-VID-014`; Fase 2 não descartou (`05` §10) e o próprio catálogo se retratou | decisões de escopo de terceiro não são obedecidas (`04` §14.5) |
| C-09 | **Fronteira de dados em direções opostas** | auto-hospedagem como mudança de fronteira (`AC-06-REP-*`) × envio de conversa a plataforma hospedada de terceiro (`AC-04-VID-002`, `AC-04-REP-005`) | **aberto** — debate internalizar × contratar explicitamente adiado (`01_ESTADO` §7) |
| C-10 | **Totais internos de `AC-10-PLA-001`** | rotas 131 × 128; integrações 14/13 × 13/14 | **não reconciliado** — registrada só a existência da inconsistência |

## 5. Dependências e lock-in

| Dependência | IDs | Natureza |
|---|---|---|
| Plataforma hospedada de memória recebe conversas do usuário | `AC-04-VID-002`, `AC-04-REP-005` | termos de tratamento de dado não lidos — depende do proprietário |
| Gateways/roteadores entre agente e provedores | `AC-01-VID-001` ("OmniRoute", custódia de chave de API não inspecionada), `AC-06-VID-023` (~40 ferramentas, escopo parcialmente falado) | superfície de segurança e efeito externo irreversível sem limite declarado |
| Catálogos de terceiro como porta de instalação | `AC-09-VID-007`, `AC-05-VID-009` (cluster), `AC-06-VID-011` | identidade/licença dos artefatos desconhecida |
| Pé de contexto pesado | `AC-07-REP-003` (`E10 = 0`, 110,4 MB), `AC-03-REP-006` (289,3 MB) | custo de contexto medido na ficha; adoção travaria orçamento de contexto |
| Formato aberto como redutor de lock-in | `E11 = 5` recorrente em mídia local (PNG/MP4) — ex.: `AC-01-PRT-001` | consumo não depende de fornecedor; não se estende aos artefatos executáveis |

## 6. Riscos de segurança e licença

**Confirmado (1):** `AC-05-REP-003` (`CL4R1T4S`) — injeção de prompt confirmada por leitura direta (`V1`), decisão provisória **REJEITAR**. É o único risco confirmado do acervo.

**Declarados, não confirmados (`E06 = 1`, 12 itens):** `AC-04-REP-005`, `AC-06-REP-002`, `AC-08-REP-003`, `AC-08-VID-006`, `AC-09-VID-003`, `AC-10-PLA-001`, `AC-10-PRT-001`, `AC-10-VID-006`, `AC-10-VID-010`, `AC-10-VID-016`, `AC-10-VID-017`, `AC-10-VID-020`. Nenhum rejeitado — rejeita-se por evidência, nunca por suspeita (`04_RUBRICA` §9). Risco declarado nunca é escrito como confirmado.

**Jurídicos (3, não se resolvem por leitura de código):** `AC-04-REP-005` (modo anti-detecção × termos de terceiro), `AC-06-REP-002` (contorno de controle de plataforma e reúso de login), `AC-06-REP-004` (reúso de sessão autenticada). Dependem do proprietário.

**Licença ausente na raiz efetiva (B-02, 4):** `AC-02-REP-001`, `AC-04-REP-007`, `AC-05-REP-002`, `AC-07-REP-002` — porta `V4`: nenhum pode chegar a CANDIDATO-FORTE ou PILOTO. **Titularidade ambígua (1):** `AC-03-REP-003` (LICENSE do upstream nomeia outro titular).

**Outros vetores registrados:** instrução hostil potencial em 419 + 56 arquivos de `AC-10-REP-004`/`AC-10-REP-005` não varridos (teto de leitura); ocultação de autoria como finalidade declarada (`AC-05-REP-005`, `AC-05-VID-015`, `AC-05-VID-025`); `AC-10-PLA-001` contém engenharia reversa e dado pessoal, e usa "vulnerabilidades" para **brecha comercial**; alucinação de STT documentada (`AC-10-VID-020`, idioma khmer em contexto lusófono).

## 7. Custo e impacto de contexto

- **Nenhum número de economia de custo do acervo foi conferido.** Os três repositórios da área 08 trazem o instrumento de medição na própria fonte; nenhum resultado foi lido (teto de `05` §8). Toda magnitude é alegação (`AC-08-VID-001`–`008`, `AC-08-REP-001`–`003`).
- O único framework de redução de custo confirmado por inspeção é o de **sete níveis** de `AC-08-VID-004` (Meter, Budget, Route, Compact, Prune, Delegate, Batch) — o catálogo dizia "seis" (NC=0); a duplicata `AC-08-VID-005` herda e conta uma vez.
- Impacto de contexto medido nas fichas: `E10 = 0` em `AC-07-REP-003`; `E10 ≤ 1` em três dos cinco repositórios da área 07; 289,3 MB em `AC-03-REP-006`.
- A tensão C-01 (mais contexto × degradação) é o ponto onde custo e qualidade se cruzam — **aberta, não medida por nenhuma fonte**.

## 8. Oportunidades de experimento

Todas **dependem do proprietário** (`00` §2.5) e nenhuma foi executada nesta fase. São propostas, não plano aprovado.

| Experimento | Fecha a lacuna de |
|---|---|
| Benchmark local: planejador caro + executor barato × modelo único | `AC-01-VID-002` |
| Resposta única × deliberação por papéis, com rubrica desta casa | `AC-03-PRT-007` |
| Chunk/overlap/k sobre corpus próprio (duas fichas, um experimento) | `AC-04-PRT-004` + `AC-04-PRT-007` |
| Conjunto de perguntas de resposta conhecida ("zero alucinação") | `AC-04-VID-004` |
| Medição de consumo da persistência entre sessões | `AC-04-VID-002` |
| Medição do retorno das seis práticas | `AC-05-PRT-013` |
| Gerar skill pelo fluxo e conferir rastreabilidade à fonte, regra a regra | `AC-05-VID-027` |
| Definir medida de sucesso observável para uma das sete promessas | `AC-05-VID-004` |
| Abrir os instrumentos de eval já existentes nas fontes (`AC-08-REP-003`, `AC-03-REP-009`, `AC-06-REP-001`, `AC-10-REP-004`/`005`, `AC-07-REP-005`) | 7 verificações internas que estouram o teto (`00` §2.4) |

## 9. Lacunas críticas

| # | Lacuna | Dimensão | IDs-âncora |
|---|---|---|---|
| L-01 | **142 vídeos sem transcrição revisada** (B-01) | 50,2% dos itens; áreas 08 (67%) e 09 (70%) as mais atingidas; 6 fichas com resíduo declarado de fala | `AC-01-VID-005`/`006`, `AC-06-VID-023`, `AC-10-VID-021`/`022`, `AC-11-VID-001` |
| L-02 | **Identidade de clusters inteiros** | série "conselho de IAs" (7 fichas, `AC-03-PRT-001`); cluster promocional (15 fichas, `AC-05-VID-009`); "Graphify" (`AC-04-VID-008` + `AC-02-VID-009`/`011`); listas open source (`AC-06-VID-011`) | lacunas de família contadas uma vez cada |
| L-03 | **Procedência jurídica** | 4 licenças ausentes + 1 titularidade ambígua + 3 avaliações jurídicas + 1 planilha com dado pessoal | §6 acima |
| L-04 | **Zero medição de eficácia lida** | o acervo descreve forma; nenhuma fonte lida mede resultado; `E13 = ND` quase universal | sínteses das áreas 05, 08, 09 |
| L-05 | **Manutenção não datada** | `E05 = ND` em áreas inteiras (ex.: 13/13 na área 07) | `AC-07-*` |
| L-06 | **Fala citada por nome de produto grafado errado** | motor de STT grafou nomes errado; identificação inequívoca depende de revisão | `AC-01-VID-005` |

## 10. Defeitos de instrumento encontrados nesta fase — registrados, não corrigidos em silêncio

Esta frente registra, não corrige (`01_ESTADO` §5). Encontrados durante a síntese, por auditoria das áreas:

| # | Defeito | Onde | Tratamento na síntese |
|---|---|---|---|
| F3-01 | **Totais de fechamento de área não batem com a soma ficha a ficha** — área 04 declara 9/20, a soma dá 10/19; área 05 declara 14/35, a soma dá 15/34; área 06 declara 9/30, a soma dá 11/28 (`EXIGE PESQUISA`/`REFERÊNCIA`) | fechamentos dos arquivos de ficha 04, 05, 06 | **prevalece o RF de cada ficha** — a soma por ficha reconcilia exata com `01_ESTADO` §11 (67/190); divergência registrada nas sínteses §4 |
| F3-02 | **`DEF-13` reincidente sem regra de precedência** — 5 itens satisfazem PADRÃO A ESTUDAR e EXIGE PESQUISA simultaneamente | `AC-04-REP-003`, `AC-05-REP-004`, `AC-05-REP-005`, `AC-07-REP-003`, `AC-07-REP-005` | prevaleceu EXIGE PESQUISA → PESQUISAR, declarado em cada síntese; a rubrica precisa de regra de precedência (registro para futura calibração) |
| F3-03 | Fechamento da área 05 declara "7 parciais" listando 8 IDs com NC=2; fechamento da área 04 declara "4 parciais" com 3 IDs + 1 atributo | fechamentos 04 e 05 | registrado; fichas prevalecem |

Nenhum defeito alterou nota, classe ou contagem já atribuída. A correção de F3-01/F3-03 cabe a futura rodada de manutenção do instrumento; a de F3-02 cabe à rubrica (`04_RUBRICA` §14), fora desta fase.

---

> Este arquivo é evidência externa, provisória e não normativa. Não autoriza adoção de nada.
