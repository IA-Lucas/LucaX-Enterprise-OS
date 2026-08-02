> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

# SÍNTESE — ÁREA 08 — CUSTO E CONTEXTO

**Frente:** Programa de Inteligência do Acervo · **Fase 3 — Síntese** (missão **A3**) · **Data:** 2026-07-29 · **Avaliador:** Claude Opus 5 (Fase 3)

**Origem:** external-evidence · **Autoridade:** nenhuma · **Estado:** provisório · **Normativo:** não · **Adoção:** não-decidida

**Base:** 12 fichas de `07_FICHAS-DE-EVIDENCIA/08_CUSTO-E-CONTEXTO.md` — 3 REPO (LV4), 1 PRINT e 8 VÍDEO (LV3), incluindo 1 duplicata exata. Pergunta central da área: *como não estourar o orçamento de token nem a janela de contexto.*

---

## 1. O que sabemos

**A área tem três artefatos reais e inspecionáveis (LV4), e eles se dividem pela ponta do consumo que atacam** — distinção feita pela própria Fase 2:

- **Compressão de saída:** `AC-08-REP-001` (`caveman-main`) é instrução de estilo que faz o agente responder em estilo telegráfico, com a alegação do autor de "mesmas respostas, 65% menos tokens de saída" — **alegação não conferida**, embora a fonte traga o instrumento (`benchmarks/`, `evals/`) e o resultado não tenha sido lido (E15 = 2). É o segundo menor repositório do acervo (167 arquivos, 831,1 KB — E10 = 4), MIT, com `SECURITY.md`, `skills-lock.json` e testes nomeados sobre o próprio risco (`test_compress_safety.py`, `test_hooks.py`).
- **Compressão de entrada com consciência de tipo:** `AC-08-REP-002` (`headroom-main`) declara "60–95% menos token em dados JSON" e "15–20% em agentes de código" — **intervalos não conferidos**, conferíveis dentro da fonte (`compression_benchmark.py`, `comprehensive_eval.py`). A alegação crítica é a **reversibilidade** da compressão, também não verificada (E15 = 2). Tem o conjunto de controles de segurança mais completo do acervo até a Fase 2 (E06 = 4: gitleaks, gitguardian, `deny.toml`, `sbom/`), mas pesa 1.967 arquivos / 57,1 MB (E10 = 1) e exige pilha Python + Rust (E08 = 3).
- **Contexto como imagem:** `AC-08-REP-003` (`pxpipe`) é proxy local que converte texto em imagem, com alegação de "~59–70% de fatura menor" — **não conferida**, dependente de preço de tabela externo. É o primeiro item do acervo com Bloco A integralmente determinado (0 ND em 7 eixos) e o primeiro com `.git/` real, confirmando a origem por `.git/logs/HEAD`. O próprio autor qualifica o número: "o número durável é o corte de token medido por requisição contra um contrafactual gratuito" — método declarado, não prova. Sobre ele pesa **risco declarado por terceiro e não confirmado por inspeção** (E06 = 1, porta V2): conversão para imagem "pode reduzir fidelidade, acessibilidade, capacidade de busca, auditabilidade e proteção contra injeção".

**Os três são somáveis, não concorrentes** — registro do próprio catálogo, preservado na ficha de `AC-08-REP-001` (E14 = 3): `AC-08-REP-002` e `AC-08-REP-003` comprimem a entrada; `AC-08-REP-001` corta a saída.

**Existe uma taxonomia de controles de custo, e ela tem SETE níveis, não seis.** `AC-08-VID-004` (NC = 0 — o catálogo diz "seis níveis" duas vezes; a inspeção `94` enumera **sete**, nomeados): *Meter* (auditar a conversa e apontar os três maiores desperdícios), *Budget* (impor formato e limite de resposta), *Route* (classificar e rotear tarefa simples), *Compact* (handoff antes de saturar), *Prune* (podar instruções e conectores ociosos), *Delegate* (delegar leitura a subagente), *Batch* (agrupar em lote). É o único item que organiza os controles em taxonomia ordenada (E14 = 3). **Todos os números exibidos nele são alegações não conferidas**: 75–85% por roteamento, 40–50% da janela como momento de compactar, 6.100→420 tokens em delegação, lote a −50%, cache a −90% (E15 = 1) — `94` já registra que servem "nunca como meta oficial sem benchmark local".

**Existe um protocolo de passagem de contexto entre sessões com estrutura transferível.** `AC-08-VID-008` exibe um arquivo de handoff com **cinco campos nomeados** — objetivo, estado atual, o que mudou, tentativas que falharam, próximos passos — registrado como **fato observado** (estrutura exibida em quadro). Em contraste, o gráfico de qualidade contra preenchimento da janela com limiares de 65% e 80% é **alegação sem método, sem eixo medido e sem amostra** (E15 = 1), e a superioridade sobre compactação automática é comparativa não medida.

**O restante da área é material de referência com evidência fraca.** `AC-08-VID-001` trata de cache de infraestrutura (CDN, Redis, banco), genérico frente à pergunta da área (E01 = 2, RP = 1); `AC-08-VID-002` mostra a replicação de contexto por ramo de subagente em diagrama; `AC-08-VID-003` mostra troca de modelo caro por barato como procedimento observável; `AC-08-VID-007` lista cinco táticas voláteis ("até 80%", "22% mais barato sem perda de qualidade", "109 subagentes" — todas não verificadas, E15 = 1); `AC-08-VID-006` é carrossel sobre o `pxpipe` que o acervo já possui inteiro como repositório (E14 = 1, sobrepõe `AC-08-REP-003` com evidência estritamente inferior); `AC-08-PRT-001` é card didático de tokenização cujos IDs de exemplo dependem de tokenizador não nomeado (E15 = 1).

## 2. Fontes mais fortes e por quê

Pelos dados da ficha — LV, NF, ND, vetos — e não por popularidade:

- **`AC-08-REP-003` (pxpipe)** — a fonte mais completa da área: LV4, NF = 4 com **0 ND em 7 eixos** (único do acervo), `eval/` com 332 arquivos sobre benchmarks públicos reconhecíveis (`swe-bench`, `gsm8k`, `needle-haystack`), changelog datado (0.9.0 — 2026-07-14, quinze dias antes da avaliação, E05 = 3) e histórico de repositório na própria fonte. Paradoxalmente, é também o item que **não pode ser candidato**: V2 disparada por E06 = 1.
- **`AC-08-REP-002` (headroom)** — LV4, NF = 4 (6/7, 1 ND), RP = 4. O ND de E05 é um detalhe de leitura (changelog lido só na seção `Unreleased`, sem data), não ausência de changelog. Aparato de verificação extenso: 28 arquivos de benchmark, incluindo **testes adversariais** e avaliação de relevância — que medem preservação de informação, o risco correto da técnica (E13 = 4).
- **`AC-08-REP-001` (caveman)** — LV4, NF = 4 (6/7, 1 ND), RP = 4, AA = 4 (único da área com atrito 4). Três camadas separadas de verificação (`tests/` com 32 arquivos, `evals/`, `benchmarks/`). O ND de E05 não é resolvível dentro da fonte (badge sem data).
- **`AC-08-VID-008` (handoff)** — entre os vídeos, o mais estruturado (registro da própria ficha, E02 = 2): procedimento completo exibido e os cinco campos como fato observado. Ainda assim NF = 1 com 5 ND e LV3.

Os três repositórios têm NC = 3 (catálogo fiel, detalhe conferido); os vídeos fortes em descrição de catálogo (`NC = 5`: VID-002, 003, 006, 007) permanecem com NF = 1 — título confirmado não eleva evidência.

## 3. Padrões recorrentes

1. **Número sem método.** O padrão dominante da área: alegação numérica forte sem método, amostra ou contrafactual — `AC-08-VID-004` (cinco números, E15 = 1), `AC-08-VID-007` ("até 80%", "22% sem perda de qualidade", E15 = 1), `AC-08-VID-008` (limiares 65%/80% sem eixo medido), `AC-08-VID-001` ("3 de 1.000" não demonstrado), `AC-08-VID-006` (59–70% sem a autoqualificação do README). Nos repositórios o mesmo padrão aparece atenuado: número forte, mas **com instrumento de verificação dentro da fonte** (`AC-08-REP-001`, `AC-08-REP-002`, `AC-08-REP-003`, todos E15 = 2).
2. **Repetição temática sem confirmação.** As mesmas táticas reaparecem entre itens: roteamento de modelo em `AC-08-VID-003`, `AC-08-VID-004` (nível *Route*) e `AC-08-VID-007`; delegação a subagente em `AC-08-VID-002` e `AC-08-VID-004` (nível *Delegate*); verbosidade em `AC-08-VID-007` e como artefato em `AC-08-REP-001`. A Fase 2 tratou cada reaparição como redução de E14, nunca como verificação (regra P-3) — esta síntese mantém.
3. **Volatilidade declarada.** Vários itens dependem de nomes, preços e planos de fornecedor que o próprio material trata como instáveis: `AC-08-VID-003` (E04 = 2), `AC-08-VID-007` (E15 = 1, "voláteis por natureza"), `AC-08-REP-003` (número de fatura depende de preço de tabela; E11 = 2 por calibração por modelo).
4. **Vídeo sem fala aproveitável.** Cinco dos oito vídeos não têm fala lexical confiável (`AC-08-VID-001`, `004`, `005`, `006`, `007` — confiança STT de 0,130 a 0,751 com 1 palavra); nos três com LV3-A (`AC-08-VID-002`, `003`, `008`), a transcrição é automática e não revisada — **proibida como citação exata**. Todo o conteúdo avaliável dos vídeos vem de quadros (LV3-V).
5. **Risco nomeado por terceiro, não por inspeção.** Os dois únicos E06 = 1 do acervo estão nesta área (`AC-08-REP-003`, `AC-08-VID-006`), pelo **mesmo risco declarado** na trilha Codex `94`, com a mesma nota por decisão deliberada de coerência entre as fichas. Nenhum dos dois tem risco confirmado.

## 4. Conflitos e divergências

- **"Seis" contra "sete" níveis** — a divergência de catálogo da área (NC = 0): o catálogo afirma "seis níveis" duas vezes em `AC-08-VID-004` e herda o erro em `AC-08-VID-005`; a inspeção `94` enumera sete, nomeados, e o título da própria seção de `94` é "sete níveis de redução de custo". O catálogo também resume o conteúdo como "medir, compactar e delegar", omitindo orçamento, roteamento, poda e lote. **A síntese usa sete.** A divergência é de catálogo, não de fonte: o hash reconferido confere (V8 não dispara); NC não entra em NF.
- **Carrossel contra fonte primária** — `AC-08-VID-006` apresenta os números do `pxpipe` (3,1 caracteres/token de imagem; 59–70%) **como resultado**, enquanto o README de `AC-08-REP-003` os apresenta **como estimativa a medir**, com qualificação explícita do autor. A mesma alegação, duas forças retóricas diferentes; a síntese registra a forma da fonte primária.
- **Autoqualificação rara contra alegação nua** — `AC-08-REP-003` é o único item da área em que o autor desqualifica o próprio número ("prices move and workloads differ"), contrastando com `AC-08-VID-007`, onde "sem perda de qualidade" é "a alegação mais forte e a menos sustentada" (registro da ficha).
- **Nenhum conflito de hash**: os 12 itens reconferem, incluindo a identidade binária do par 004/005 (V8 = 0 divergências).

## 5. Candidatos fortes, pilotos e referências

**Candidatos fortes:** nenhum. Os dois pilotos falham na mesma condição — "nenhum eixo do Bloco A abaixo de 3" — por E15 = 2 (`AC-08-REP-001` e `AC-08-REP-002`, registro explícito das duas fichas); `AC-08-REP-003`, apesar de NF = 4 e Bloco A completo, é fechado antes pela porta V2.

**Pilotos (RF = CANDIDATO A PILOTO):**
- `AC-08-REP-001` — LV4, NF = 4, RP = 4, AA = 4, 1 ND, nenhum eixo do Bloco C em 0. Restrições registradas: os 65% não conferidos apesar de o instrumento existir na fonte; E05 = ND; a ressalva do catálogo (estilo telegráfico degrada saída para humano) sem evidência a favor ou contra.
- `AC-08-REP-002` — LV4, NF = 4, RP = 4, AA = 3, 1 ND. Restrições: intervalos de economia não conferidos; **reversibilidade** — o argumento central — não verificada; E08 = 3 (duas pilhas de runtime); E10 = 1 (57,1 MB).

**Referências (RF = REFERÊNCIA, 8 itens):** `AC-08-PRT-001` (conceito de tokenização, sem números viajáveis), `AC-08-VID-001` (cache de infraestrutura, genérico), `AC-08-VID-002` (replicação de contexto por subagente), `AC-08-VID-003` (roteamento caro/barato), `AC-08-VID-004` (taxonomia de sete níveis — conteúdo mais reutilizável entre as referências, E14 = 3), `AC-08-VID-006` (ponte fraca para `AC-08-REP-003`), `AC-08-VID-007` (táticas voláteis), `AC-08-VID-008` (protocolo de handoff com cinco campos observados).

**Pesquisa (RF = EXIGE PESQUISA):** `AC-08-REP-003` — fechado como candidato por V2 apesar de NF = 4, RP = 4 e Bloco A completo: **relevância alta não compensa risco declarado** (§8.2, caso mais nítido do acervo, registro da ficha).

## 6. O que não adotar

Nada nesta seção é adoção nem rejeição formal — é o registro do que a evidência **não sustenta**:

- **Os números de `AC-08-VID-004` como meta** — cinco percentuais sem método; o próprio relatório `94` os veda como meta oficial sem benchmark local.
- **As táticas de `AC-08-VID-007` como fato** — "22% mais barato sem perda de qualidade" não tem medição de qualidade alguma; preços e versões são voláteis e não verificados.
- **`AC-08-VID-006` como via para o `pxpipe`** — sobrepõe `AC-08-REP-003` com evidência estritamente inferior (RP = 1, E14 = 1) e ainda apresenta como resultado o que a fonte primária apresenta como estimativa.
- **`AC-08-VID-001` para esta área** — cache de infraestrutura (CDN/Redis/banco) não endereça orçamento de token nem janela de contexto (E01 = 2, RP = 1).
- **Os IDs de tokenização de `AC-08-PRT-001`** — dependem de tokenizador que o card não nomeia; não verificados externamente.
- **O proxy `AC-08-REP-003` no caminho de toda requisição** antes de fechada a lacuna nomeada: preservação semântica e da defesa contra injeção não demonstradas — risco **declarado**, não confirmado; a verificação existe dentro da fonte e não foi feita.
- **Qualquer fala dos vídeos como citação** — cinco itens sem fala lexical confiável; três com STT automático não revisado. Nomes de modelo ditos em `AC-08-VID-003` são não conferíveis ("STT troca nomes", registro de `94`).

## 7. Riscos e dependências

- **Risco declarado, não confirmado (E06 = 1):** `AC-08-REP-003` e `AC-08-VID-006` — conversão de texto em imagem "pode reduzir fidelidade, acessibilidade, capacidade de busca, auditabilidade e proteção contra injeção" (alegação de terceiro em `94`). Nenhum dos dois tem risco confirmado por inspeção; nenhum foi rejeitado (V1 exige confirmação). A superfície concreta de `AC-08-REP-003` é observada: proxy local que intercepta e reescreve toda requisição, sem `SECURITY.md` na raiz (procurado, ausente).
- **Dependência de fornecedor:** `AC-08-REP-003` depende do canal de visão e de perfis calibrados por modelo — trocar de fornecedor exige recalibrar (E11 = 2). `AC-08-REP-002` tem desempenho declarado ligado a modelo próprio publicado pelo autor (E11 = 3).
- **Dependência de autorização do proprietário:** a verificação de `AC-08-REP-003` (abrir `eval/results`, `FINDINGS.md`, testes `abstention`/`gist-recall`/`needle-haystack` — todos existentes na fonte) estoura o teto de leitura de `05` §8; é resolvível na própria fonte, mas depende de autorização explícita. Igual dependência para o ND de E05 de `AC-08-REP-001` (commits na origem pública — pesquisa externa).
- **Atrito de runtime:** `AC-08-REP-002` exige Python + Rust (E08 = 3) e 57,1 MB de insumo (E10 = 1); `AC-08-REP-003` exige Node/pnpm e posição de proxy na rede (E08 = 3).
- **Volatilidade:** os números de economia de `AC-08-VID-003`, `AC-08-VID-007` e a fatura de `AC-08-REP-003` dependem de preços e nomenclaturas de fornecedor fora do acervo.

## 8. Lacunas

- **Preservação semântica e anti-injeção do `pxpipe`** — a lacuna nomeada de `AC-08-REP-003`, precisa e única: nenhuma demonstração de que o contexto-imagem preserva informação nem a defesa contra injeção. Verificação escrita, interna à fonte, pendente de autorização.
- **Nenhum número da área foi conferido** — os três repositórios trazem instrumento de medição na própria fonte e nenhum resultado foi lido (`AC-08-REP-001`: `benchmarks/results` não aberto; `AC-08-REP-002`: resultados não lidos; `AC-08-REP-003`: `eval/results` e `FINDINGS.md` não abertos). **Toda economia de token desta área é, neste estado, alegação.**
- **Manutenção dos dois pilotos** — E05 = ND em `AC-08-REP-001` (badge sem data; exige origem pública) e `AC-08-REP-002` (changelog lido sem data; leitura curta dentro da fonte provavelmente resolve).
- **A fala de oito vídeos permanece desconhecida no que acrescenta** — bloqueio B-01: cinco sem fala confiável, três com STT automático não revisado. O que a fala adiciona aos quadros é **desconhecido**.
- **Autoria, licença e origem de todos os itens de mídia** — E06/E07 = ND no PRINT e nos oito vídeos (portas V2 e V4 disparadas em todos eles por ND, não por evidência de risco).
- **A ressalva do estilo telegráfico** — "degrada resposta destinada a humano" (`AC-08-REP-001`, alegação do catálogo) sem evidência a favor ou contra.

## 9. Decisão provisória

Vocabulário fechado; registro por ID, sem ordenação. Nenhuma classe equivale a adoção.

| ID | Classe | Motivo (uma linha, citando a ficha) |
|---|---|---|
| `AC-08-REP-001` | PILOTO | RF = CANDIDATO A PILOTO: LV4, NF = 4, RP = 4, AA = 4, 1 ND; barrado de CANDIDATO FORTE só por E15 = 2 (65% não conferido, conferível na fonte). |
| `AC-08-REP-002` | PILOTO | RF = CANDIDATO A PILOTO: LV4, NF = 4, RP = 4, AA = 3; E15 = 2 — intervalos e reversibilidade não verificados. |
| `AC-08-REP-003` | PESQUISAR | RF = EXIGE PESQUISA por V2 (E06 = 1, risco declarado não confirmado); lacuna nomeada, verificação interna pendente de autorização. |
| `AC-08-PRT-001` | REFERENCIA | RF = REFERÊNCIA: LV3, NF = 1 com 5 ND; conceito base, números dependentes de tokenizador não nomeado. |
| `AC-08-VID-001` | REFERENCIA | RF = REFERÊNCIA: LV3-V, RP = 1 — cache de infraestrutura, genérico frente à pergunta da área. |
| `AC-08-VID-002` | REFERENCIA | RF = REFERÊNCIA: LV3-V+LV3-A, NF = 1, 5 ND; diagrama de replicação sem medição. |
| `AC-08-VID-003` | REFERENCIA | RF = REFERÊNCIA: LV3-V+LV3-A, NF = 1; procedimento observável, nomes e economia não conferíveis. |
| `AC-08-VID-004` | REFERENCIA | RF = REFERÊNCIA: LV3-V, NF = 1; taxonomia de sete níveis (NC = 0 — inspeção prevalece sobre o "seis" do catálogo); números sem método. |
| `AC-08-VID-005` | DUPLICATA | RF = DUPLICADO: SHA-256 idêntico a `AC-08-VID-004`; conteúdo conta uma vez, no original; herda a divergência NC = 0. |
| `AC-08-VID-006` | REFERENCIA | RF = REFERÊNCIA: LV3-V, RP = 1, V2+V4; carrossel que sobrepõe `AC-08-REP-003` com evidência inferior. |
| `AC-08-VID-007` | REFERENCIA | RF = REFERÊNCIA: LV3-V, NF = 1; cinco táticas voláteis, números não verificados. |
| `AC-08-VID-008` | REFERENCIA | RF = REFERÊNCIA: LV3-V+LV3-A, NF = 1; cinco campos do handoff como fato observado; limiares sem método. |

## 10. Experimento que poderia validá-la

**Proposta — não é plano aprovado.** Um único experimento desdobrado em três braços mediria o que a área inteira deixou por medir, usando apenas instrumentos que as próprias fontes declaram:

1. **Braço interno (leitura, sem execução):** autorizar o estouro do teto de `05` §8 para abrir `eval/results`, `FINDINGS.md` e os testes `abstention`/`gist-recall`/`needle-haystack` de `AC-08-REP-003`, mais `benchmarks/results` de `AC-08-REP-001` e os resultados de `AC-08-REP-002` — fechando as três lacunas de E15 sem executar nada.
2. **Braço de medição própria (depende do proprietário):** aplicar o método que o próprio autor de `AC-08-REP-003` declara — corte de token por requisição contra um contador contrafactual gratuito, gravado em arquivo local — a uma carga de trabalho desta casa, medindo separadamente entrada (`AC-08-REP-002`, `AC-08-REP-003`) e saída (`AC-08-REP-001`), já que as fichas registram os três como somáveis.
3. **Braço de risco:** sobre o braço 2, incluir os testes de preservação que as fontes já nomeiam — agulha-em-palheiro e abstenção (`AC-08-REP-003`), relevância e adversariais (`AC-08-REP-002`) — para converter o risco **declarado** de injeção/fidelidade em confirmado ou refutado, que é o que destrava ou encerra `AC-08-REP-003`.

O que o experimento **não** validaria: os números dos vídeos (`AC-08-VID-004`, `007`, `008`), que permanecem alegação de fornecedor sem método — para esses, a validação seria outra (benchmark local contra os percentuais exibidos), e `94` já os veda como meta sem ela.

## 11. Confiança da síntese

**Média**, com distribuição interna desigual — alta para os repositórios, baixa para a mídia:

- **A favor:** 3 dos 12 itens são LV4 com leitura direta e NF = 4, incluindo um com 0 ND (`AC-08-REP-003`); todos os 12 hashes reconferem (V8 = 0); a área tem **zero disparos de V7** (nenhuma alegação sem prova sustentando relevância); o fechamento da área contou 46 ND nomeados, todos com o que os resolveria; a única divergência de catálogo (NC = 0 em `AC-08-VID-004`/`005`) é de contagem e está resolvida pela inspeção (sete níveis nomeados).
- **Contra:** 8 dos 12 itens (67%) são vídeo/print em LV3 com NF = 1 e 4–5 ND cada — E06 e E07 indeterminados em todos eles; 46/180 células de eixo são ND (25,6%); cinco vídeos sem fala confiável e três com STT não revisado (B-01 aberto); **nenhum número de economia da área foi conferido**, mesmo nos itens fortes; 1 item em EXIGE PESQUISA com verificação interna pendente de autorização; 2 itens com risco declarado não confirmado.
- **Síntese:** o que esta área afirma sobre **estrutura** (três mecanismos somáveis, taxonomia de sete níveis, protocolo de cinco campos) é rastreável e estável; o que afirma sobre **magnitude** (qualquer percentual) é alegação não conferida. A confiança média reflete exatamente essa divisão.

## 12. Cobertura

| ID | Tipo | LV | RF da ficha | Decisão provisória |
|---|---|---|---|---|
| `AC-08-REP-001` | REPO | LV4 | CANDIDATO A PILOTO | PILOTO |
| `AC-08-REP-002` | REPO | LV4 | CANDIDATO A PILOTO | PILOTO |
| `AC-08-REP-003` | REPO | LV4 | EXIGE PESQUISA | PESQUISAR |
| `AC-08-PRT-001` | PRINT | LV3-V | REFERÊNCIA | REFERENCIA |
| `AC-08-VID-001` | VÍDEO | LV3-V | REFERÊNCIA | REFERENCIA |
| `AC-08-VID-002` | VÍDEO | LV3-V + LV3-A | REFERÊNCIA | REFERENCIA |
| `AC-08-VID-003` | VÍDEO | LV3-V + LV3-A | REFERÊNCIA | REFERENCIA |
| `AC-08-VID-004` | VÍDEO | LV3-V | REFERÊNCIA | REFERENCIA |
| `AC-08-VID-005` | VÍDEO | LV3-V (herdado) | DUPLICADO | DUPLICATA → `AC-08-VID-004` |
| `AC-08-VID-006` | VÍDEO | LV3-V | REFERÊNCIA | REFERENCIA |
| `AC-08-VID-007` | VÍDEO | LV3-V | REFERÊNCIA | REFERENCIA |
| `AC-08-VID-008` | VÍDEO | LV3-V + LV3-A | REFERÊNCIA | REFERENCIA |

**Totais:** 12 IDs · CANDIDATO-FORTE 0 · PILOTO 2 · ADAPTAR-PADRAO 0 · REFERENCIA 8 · PESQUISAR 1 · REJEITAR 0 · DUPLICATA 1.

> Este arquivo é evidência externa, provisória e não normativa. Não autoriza adoção de nada.
