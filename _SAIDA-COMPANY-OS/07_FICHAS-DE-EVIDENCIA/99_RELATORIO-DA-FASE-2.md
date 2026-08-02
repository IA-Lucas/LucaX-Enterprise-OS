> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

# RELATÓRIO DA FASE 2 — EXTRAÇÃO

**Data de encerramento:** 2026-07-29 · **Avaliador:** Claude Opus 5 (Fase 2)
**Escopo executado:** aplicação de `04_RUBRICA-DE-AVALIACAO.md` aos **279 IDs** de `02_MANIFESTO-DAS-FONTES.md`, com ficha rastreável por item, organizada **por área e por ID**.
**Este relatório é factual.** Não contém ranking, ordenação, recomendação, roadmap, arquitetura, política, nem o debate internalizar × contratar. **Nenhuma classificação aqui autoriza adoção — nem `CANDIDATO FORTE`.**

> **A regra que governou tudo:** o acervo informa o LucaX Enterprise OS, mas **não determina sua arquitetura**.

---

## 1. Cobertura — contagem verificada por ferramenta

| Verificação | Resultado |
|---|---|
| Fichas escritas | **279** |
| IDs únicos nas fichas | **279** |
| IDs do manifesto | **279** |
| IDs no manifesto **sem** ficha | **0** |
| IDs nas fichas **fora** do manifesto | **0** |
| IDs repetidos | **0** |
| Arquivos de ficha | **11**, um por área |
| Índice × contagem física | **coincidem** |

**Método da verificação:** extração dos identificadores dos cabeçalhos `### AC-…` dos onze arquivos, ordenação, remoção de duplicatas e comparação de conjunto com os identificadores do manifesto. Executada em 2026-07-29, após a última ficha.

**Distribuição por tipo** — bate com a linha de base da Fase 0:

| Tipo | Itens |
|---|---:|
| VÍDEO | 142 |
| PRINT | 93 |
| REPO | 43 |
| PLANILHA | 1 |
| **Total** | **279** |

**Critério de conclusão do enunciado:** 279/279 representados · **277 avaliados de forma única** e **2 duplicatas exatas ligadas aos originais** (`AC-03-VID-008` → `AC-03-VID-007`; `AC-08-VID-005` → `AC-08-VID-004`).

---

## 2. Validade das fichas — `04` §13

Os dez critérios de invalidez do §13 foram verificados **por ferramenta sobre as 279 fichas**, não por amostragem:

| Critério §13 | Fichas em falta |
|---|---:|
| 1. Não declara `LV` antes das notas | **0** |
| 2. `LV ≥ 3` sem cobertura exata da leitura | **0** |
| 3. Nota ≠ ND sem evidência citada | **0** |
| 4. `ND` sem registrar o que o resolveria | **0** |
| 5. Valor de bloco sem contagem de ND ao lado | **0** |
| 6. Mistura `NC` em `NF` | **0** |
| 7. Deriva do Codex sem citar ID do item e do handoff | **0** |
| 8. Não registra a reconferência de hash | **0** |
| 9. `RF` sem apontar a regra de §8 ou §9 | **0** |
| 10. Não abre com o bloco de quatro linhas | **0** |

**Duas falhas foram encontradas nessa verificação e corrigidas antes do fecho** — estão em §6, com o que as causou. Nenhuma ficha permaneceu inválida.

---

## 3. Legibilidade — `LV` declarado por ficha

| LV | Fichas | O que significa aqui |
|---|---:|---|
| **LV4** | 43 | Leitura direta, por esta frente, da raiz efetiva do repositório, dentro do teto de `05` §8 |
| **LV3-V + LV3-A** | 42 | Quadros-chave **mais** transcrição automática bruta com fala aproveitável. **A soma não produz LV4** |
| **LV3-V** | 193 | 93 prints e 100 vídeos sem fala aproveitável — inspeção visual pela trilha Codex |
| **LV3** | 1 | A planilha. **Divergência declarada**: `111` atribui LV4; esta frente adotou o inferior (DEF-07) |
| LV0 · LV1 · LV2 · LV5 | **0** | — |
| **Total** | **279** | |

Os **42** itens com fala aproveitável coincidem exatamente com os 42 vídeos com fala narrativa declarados no estado corrente da multimídia. **Nenhum item ficou em `LV ≤ 2`** — por isso **V5 nunca disparou**, e a previsão de `01_ESTADO` §9 item 3 (140 vídeos em `LV1` recebendo `INDETERMINADO`) está **superada e não deve ser reaplicada**.

---

## 4. Resultado final — `RF` por classificação

| Classificação | Fichas | % de 279 |
|---|---:|---:|
| **REFERÊNCIA** | 190 | 68,1 % |
| **EXIGE PESQUISA** | 67 | 24,0 % |
| **CANDIDATO A PILOTO** | 11 | 3,9 % |
| **CANDIDATO FORTE** | 7 | 2,5 % |
| **DUPLICADO** | 2 | 0,7 % |
| **PADRÃO A ESTUDAR** | 1 | 0,4 % |
| **REJEITADO** | 1 | 0,4 % |
| **INDETERMINADO** | **0** | 0 % |
| **Total** | **279** | 100 % |

**Cruzamento com o tipo do item** — sem ordenação, é apenas onde cada classificação caiu:

| Tipo | REFERÊNCIA | EXIGE PESQUISA | PILOTO | FORTE | PADRÃO | DUPLICADO | REJEITADO |
|---|---:|---:|---:|---:|---:|---:|---:|
| REPO (43) | 1 | 22 | 11 | 7 | 1 | 0 | 1 |
| PRINT (93) | 80 | 13 | 0 | 0 | 0 | 0 | 0 |
| VÍDEO (142) | 108 | 32 | 0 | 0 | 0 | 2 | 0 |
| PLANILHA (1) | 1 | 0 | 0 | 0 | 0 | 0 | 0 |

**Leitura factual, não avaliativa:** as classificações de candidatura só ocorreram em REPO, porque as demais condições de entrada de §9 exigem `E06 ≥ 3` e `E07 ≥ 3`, e **nenhum print, vídeo ou planilha permite determinar segurança ou licença por inspeção**. Isso é propriedade do instrumento e do tipo de evidência, não juízo sobre o conteúdo.

**As seis classificações que a calibração nunca havia exercitado (`06` §7) foram exercitadas nesta fase:** CANDIDATO FORTE, CANDIDATO A PILOTO, PADRÃO A ESTUDAR, EXIGE PESQUISA, REJEITADO e DUPLICADO. `INDETERMINADO` **não** foi usado — nenhum item disparou V5, V6 ou V8.

---

## 5. `ND` — o que não foi determinável

**Total: 1.214 células em `ND`, de 4.185 possíveis (279 × 15) = 29,0 %.** Recontado por ferramenta a partir das contagens declaradas em cada bloco de cada ficha.

| Área | Itens | Células | `ND` | % |
|---|---:|---:|---:|---:|
| 01 | 11 | 165 | 55 | 33,3 |
| 02 | 24 | 360 | 117 | 32,5 |
| 03 | 31 | 465 | 111 | 23,9 |
| 04 | 32 | 480 | 133 | 27,7 |
| 05 | 51 | 765 | 235 | 30,7 |
| 06 | 40 | 600 | 183 | 30,5 |
| 07 | 13 | 195 | 48 | 24,6 |
| 08 | 12 | 180 | 46 | 25,6 |
| 09 | 10 | 150 | 45 | 30,0 |
| 10 | 46 | 690 | 196 | 28,4 |
| 11 | 9 | 135 | 45 | 33,3 |
| **Total** | **279** | **4.185** | **1.214** | **29,0** |

**Máximo de `ND` numa única ficha: 5.** O gatilho de V6 são 8. **Nenhuma ficha chegou perto** — e a razão é estrutural: itens de mídia têm exatamente cinco eixos indeterminados (`E03`, `E05`, `E06`, `E07`, `E13`), sempre os mesmos, sempre pela mesma causa.

**Três repositórios fecharam o Bloco A sem nenhum `ND`** — `AC-08-REP-003`, `AC-10-REP-002` e `AC-10-REP-004` —, todos por trazerem licença, versão datada e testes na própria fonte.

**Todos os 1.214 `ND` nomeiam o que os resolveria.** Nenhum `ND` foi tratado como zero; nenhum entrou em mediana.

---

## 6. Defeitos do instrumento e falhas próprias

### 6.1 Defeitos da rubrica — `DEF-06` a `DEF-15`

Registrados em `00_INDICE-DA-FASE-2.md` §4, com a ocorrência que os revelou. Resumo:

| Defeito | Natureza |
|---|---|
| **DEF-06** | Sem mapeamento de `LV` para print inspecionado por outra trilha |
| **DEF-07** | Idem para a planilha — gerou divergência de `LV` com o relatório `111` |
| **DEF-08** | Âncoras do Bloco C pressupõem componente instalável; item de mídia não tem instalação |
| **DEF-09** | V6 foi calibrado supondo itens em `LV1`; com a entrega multimídia, ficou inalcançável |
| **DEF-10** | V4 chama `EXIGE PESQUISA` de "resultado natural", mas `REFERÊNCIA` também cabe no teto |
| **DEF-11** | §9 proíbe `Bloco C = 0` em PILOTO e **não** em FORTE — um `E10 = 0` pode ser FORTE e não pode ser piloto |
| **DEF-12** | Sem classe natural para item que falha **uma única** condição de entrada |
| **DEF-13** | Condições de entrada de §9 não são mutuamente exclusivas e não há precedência. **Quatro ocorrências** |
| **DEF-14** | §13 não exige recontagem do total de `ND` por área a partir das fichas |
| **DEF-15** | §12 não fixa formato de cabeçalho; o modelo compacto permite omitir "cobertura" e a contagem de `ND` do Bloco C |

**Nenhum defeito foi corrigido em silêncio. Nenhum alterou nota já atribuída.** Onde a rubrica não decidia, a decisão foi **declarada antes das notas**, em `00_INDICE-DA-FASE-2.md` §3, e aplicada de forma uniforme às 279 fichas.

### 6.2 Duas falhas desta frente, encontradas por auditoria própria e corrigidas

**Falha 1 — totais de `ND` por área escritos por estimativa.** Os fechamentos das áreas 02 a 06 declaravam totais que **não batiam** com a soma das contagens das próprias fichas.

| Área | Declarado antes | Recontado por ferramenta | Diferença |
|---|---:|---:|---:|
| 02 | 115 | **117** | +2 |
| 03 | 152 | **111** | −41 |
| 04 | 167 | **133** | −34 |
| 05 | 265 | **235** | −30 |
| 06 | 207 | **183** | −24 |

Área 01 conferia. Áreas 07 a 11 foram contadas item a item desde o início e conferem. **Os cinco fechamentos foram corrigidos, com o valor anterior preservado no texto.** A área 03 trazia ainda "145 dos quais em itens de mídia"; a contagem correta é **105 em mídia e 6 nos dez repositórios**. Causa: total de área escrito de cabeça em vez de contado. É `DEF-14`.

**Falha 2 — 31 fichas em formato compacto violavam `04` §13.** Vinte e três fichas de vídeo e oito de print da área 10 reportavam `AA = 4` **sem a contagem de `ND` ao lado** (§13.5), e 31 não nomeavam a **cobertura da leitura** (§13.2). Corrigidas; a validação estrutural passou a ser executada por ferramenta sobre as 279. É `DEF-15`.

**Ambas as falhas foram encontradas antes do fecho, por verificação própria, e não por revisão externa.** Ficam registradas porque um total errado sobrevive à leitura humana e contamina qualquer síntese posterior.

---

## 7. Divergências registradas

### 7.1 Catálogo × fonte — **9 itens com `NC = 0` (DIVERGENTE)**

| ID | O que o catálogo afirma | O que a inspeção mostra |
|---|---|---|
| `AC-02-VID-012` | descrição de conteúdo | contraditada pela análise de quadros |
| `AC-03-REP-003` | descrição de conteúdo | contraditada pela leitura da fonte |
| `AC-04-VID-002` | descrição de conteúdo | contraditada pela análise de quadros |
| `AC-05-PRT-011` | descrição de conteúdo | contraditada pela inspeção visual |
| `AC-08-VID-004` | "**seis níveis**" de redução de custo | `94` enumera **sete**, nomeados |
| `AC-08-VID-005` | idem (duplicata do anterior) | idem — a divergência herda |
| `AC-09-VID-007` | "varredura de segurança de skills" | `94` mostra **busca em catálogo**, sem varredura |
| `AC-10-VID-002` | "agente/chatbot de vendas" | `103` mostra **conversão documental** |
| `AC-11-PRT-001` | acusa o original de **erro conceitual** | `109`: o erro é **da leitura**, não do original |

**Nenhuma dessas divergências disparou V8.** V8 compara **hash**, e os 279 hashes conferem. Divergência de catálogo rebaixa `NC` e fica registrada; **`NC` nunca entra em `NF`** (`04` §12).

**`AC-11-PRT-001` é de natureza distinta das outras oito:** as demais descrevem errado o conteúdo; esta **critica errado** o conteúdo — o catálogo atribuiu ao original um erro que é da própria leitura, e transformou a acusação na conclusão do item.

### 7.2 Catálogo × fonte — **35 itens com `NC = 2` (PARCIAL)**

Padrão observado: o catálogo **estreita, arredonda ou completa** — descreve menos do que a imagem mostra, conta diferente do que a inspeção conta, ou acrescenta um detalhe que não está lá. Dois exemplos medidos:

- `AC-10-PRT-016`: o gráfico tem **17 linhas**; o catálogo transcreveu **9**, e as 9 são as de maior diferença — o recorte reforça a conclusão que ele extrai. `109` nomeou as oito omitidas.
- `AC-11-PRT-006`: o catálogo **listou `package.json`** numa árvore que não o contém, e achatou a hierarquia de `public/` e `src/`. `109` instrui **preservar os erros gráficos** em vez de normalizá-los.

### 7.3 Distribuição completa de `NC`

| `NC` | Fichas | Leitura |
|---|---:|---|
| 5 | 95 | Título pelo conteúdo visível, confirmado pela inspeção |
| 3 | 120 | Detalhe verificável, conferido |
| 2 | 35 | Parcial — detalhe não confirmado (§14.4) |
| 1 | 20 | Assunto pelo título, sem detalhe a conferir |
| 0 | 9 | **Divergente** |
| 4 | **0** | A convenção §3.5 não mapeia nada para 4 |
| **Total** | **279** | |

### 7.4 Divergência de escala com a trilha Codex — **1 item**

`AC-10-PLA-001`: o relatório `111` declara **LV4**; esta frente adotou **LV3**, por `DEF-07` e por **P-1** — não pontuar como leitura direta o que outra trilha leu. **A divergência é de escala, não de conteúdo**, e está escrita na ficha.

### 7.5 Divergências internas da fonte, medidas

`AC-10-PLA-001` traz dois totais que **não reconciliam com as próprias abas**, conferidos por `111`: **131 × 128** rotas e **14/13 × 13/14** integrações. E usa "vulnerabilidades" para designar **brecha comercial**, não falha de segurança.

---

## 8. Portas de veto — o que efetivamente disparou

| Porta | Disparos | Onde |
|---|---:|---|
| **V1** — `E06 = 0` | **1** | `AC-05-REP-003` — injeção de prompt **confirmada por leitura direta**, sob o protocolo de `05` §7. Único `REJEITADO` do acervo |
| **V2** — `E06 = 1` ou `ND` | **244** | 236 itens de mídia e planilha + 8 repositórios (3 com `E06 = 1`, 5 com `ND`) |
| **V3** — `E07 = 0` | **0** | Nenhuma licença encontrada proíbe uso |
| **V4** — `E07 = ND` | **241** | 236 itens de mídia e planilha + 5 repositórios |
| **V5** — `LV ≤ 2` | **0** | Nenhum item ficou abaixo de LV3 |
| **V6** — ≥ 8 `ND` | **0** | Máximo observado: 5 |
| **V7** — `E15 = 0` com relevância dependente | **25** | Itens cuja proposta central repousa em alegação numérica sem fonte |
| **V8** — hash divergente | **0** | **279/279 reconferem** |

**`E06` — distribuição:** `0` em 1 · `1` em 12 · `2` em 9 · `3` em 20 · `4` em 5 · `ND` em 232.
**`E07` — distribuição:** `4` em 36 · `3` em 1 · `2` em 1 · `ND` em 241.

**Os doze itens com `E06 = 1` — risco declarado e não confirmado — não foram rejeitados.** `04` §9 é literal: rejeitado **por evidência**, nunca por ND, nunca por suspeita. São eles: `AC-04-REP-005`, `AC-06-REP-002`, `AC-08-REP-003`, `AC-08-VID-006`, `AC-09-VID-003`, `AC-10-PLA-001`, `AC-10-PRT-001`, `AC-10-VID-006`, `AC-10-VID-010`, `AC-10-VID-016`, `AC-10-VID-017`, `AC-10-VID-020`.

**Cinco repositórios têm `E07 = ND`:** os quatro casos de licença ausente na raiz efetiva registrados em `05` §10 — `AC-02-REP-001`, `AC-04-REP-007`, `AC-05-REP-002`, `AC-07-REP-002` — **mais `AC-03-REP-003`**, a possível duplicata. Todos em `EXIGE PESQUISA`, com a lacuna nomeada: **licença na origem pública**.

---

## 9. Limites desta fase — o que estes números **não** significam

1. **Teto de leitura.** `05` §8: 8 arquivos ou ~40 KB por repositório. `LV4` significa "raiz efetiva lida dentro do teto", **não** "repositório auditado". Nenhum `src/` foi lido por inteiro.
2. **Nada foi executado.** Nenhum repositório foi instalado, rodado ou testado. Nenhum comando exibido em vídeo foi executado. Nenhum alvo indicado por terceiro foi baixado.
3. **STT não autoriza citação.** As 42 fichas com `LV3-A` usam **conteúdo aproximado**. `AC-10-VID-020` é a prova prática: o detector devolveu **khmer** com confiança alta para um vídeo em contexto lusófono. **LV3-V + LV3-A não produz LV4.**
4. **Prints e vídeos foram inspecionados por outra trilha.** As 235 fichas de mídia derivam dos relatórios Codex, citados por ID de item e de handoff. É `LV3-V` por construção — **P-2** proíbe tratar descrição de terceiro como leitura própria.
5. **`E05 = ND` é o esperado, não a exceção.** O acervo é feito de cópias `-main` sem histórico. As duas exceções — `AC-08-REP-003`, que traz `.git/`, e `AC-10-REP-002`/`AC-10-REP-004`, que trazem changelog e versões datadas — são exatamente isso: exceções.
6. **`NC` mede o catálogo, não a fonte.** Um `NC = 0` diz que a descrição diverge do original; **não** diz que o original é ruim.
7. **`REFERÊNCIA` não é endosso.** É onde cai o item que serve para consulta e não pode ser candidato a componente — inclusive o item que só serve para constar.
8. **Nenhuma classificação autoriza adoção.** A adoção depende exclusivamente dos Frameworks oficiais 1.11–1.19, **que não foram acessados**.

---

## 10. O que esta fase não produziu

Nenhuma Carta, Framework, ADR, Spec, Skill, Agente, Command, Workflow, política, arquitetura, organograma, componente canônico, catálogo de candidatos, síntese de área, ranking, roadmap, recomendação ou decisão oficial. O debate internalizar × contratar **não** foi realizado. Os Frameworks 1.11–1.19 **não** foram acessados.

**Nenhuma fonte foi alterada, movida ou renomeada.** Grafias erradas e nomes com espaço duplo foram **preservados**. As pastas alheias `work/` e `output/` **não foram tocadas**. Todo artefato produzido está em `_SAIDA-COMPANY-OS/`.

**Achado de inventário a registrar:** além de `work/` e `output/` (inconsistência **I-06**), observou-se na raiz do acervo a pasta **`_ENTRADA-NOVO-MATERIAL`**, que **não é área numerada e não entra na catalogação**. Registrada aqui como observação factual, **não tocada**, para tratamento na revisão de inventário — não é escopo desta fase.

---

## 11. Próxima ação da Fase 3 — **não iniciada**

**A ação exata, quando a Fase 3 for autorizada:** produzir a **síntese por área** a partir **exclusivamente das 279 fichas** — sem reabrir fontes, sem elevar `LV`, sem transformar repetição em validação —, mantendo `NF`, `NC`, `RP` e `AA` separados e preservando as etiquetas de camada de afirmação.

**Três pendências que a Fase 3 herda e precisa resolver antes de escrever qualquer coisa:**

1. **Colisão de numeração (D-01).** `00_GOVERNANCA` §8 chama as fichas de artefato da "Fase 3" e a síntese de "Fase 4"; o programa em execução chama a extração de **Fase 2**. As fichas foram gravadas em `07_FICHAS-DE-EVIDENCIA/`, conforme a sugestão registrada em `01_ESTADO` §9. **A numeração das fases precisa ser unificada por decisão explícita** — esta frente não a tomou.
2. **Os 67 itens em `EXIGE PESQUISA` têm lacunas nomeadas e endereçáveis.** Várias são resolvíveis **dentro da própria fonte**, sem rede e sem execução — por exemplo, abrir um `VERSIONS.md`, ler `.claude-plugin/marketplace.json`, contar as skills de um diretório. Decidir se essas verificações entram na Fase 3 ou em uma rodada complementar da Fase 2 **é decisão do usuário**.
3. **As 9 divergências de catálogo e os dois totais não reconciliados da planilha** estão registrados por ID. A síntese **não pode** reproduzir a descrição divergente do catálogo sem herdar o erro.

> **A Fase 3 não foi iniciada.** Nenhuma síntese, nenhum catálogo de candidatos e nenhum conflito consolidado foi escrito.

---

> Este relatório é evidência externa, provisória e não normativa. Não autoriza adoção de nada.
