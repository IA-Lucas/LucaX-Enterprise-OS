---
id: FIT-2026-013-verificacao-de-ratificacao
titulo: Aptidao arquitetural da continuacao da Missao 1.12 — verificacao pre-aplicacao das cinco cadeias, candidato cumulativo e correcao de RD-19
tipo: fitness
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-QAR
proprietario: DEP-QAR
aprovador: SOBERANO
criado_em: 2026-07-29
atualizado_em: 2026-07-29
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0012, ADR-0015, ADR-0018, ADR-0019]
substitui: []
substituido_por: null
objeto_avaliado: [PT-2026-004, candidatos-cumulativos, PS-2026-004, PS-2026-005, PS-2026-006, PS-2026-007, PS-2026-008, artifact-registry]
classe_mudanca: C3
classe_avaliacao: aptidao
veredito: apto-com-ressalva
resumo: Verifica se a continuacao da Missao 1.12 deixou a arquitetura mais apta a evoluir; veredito apto-com-ressalva, uma ressalva nova, uma reclassificacao com correcao de erro proprio e fechamento BLOCKED por ausencia de ato.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-GOV
ratificacao: nao-exigida
---

# FIT-2026-013: Verificacao de ratificacao

## Proposito
Verificar se a **continuacao da Missao 1.12** — busca do ato, mapa de ratificacao, verificacao
pre-aplicacao das cinco cadeias e construcao do candidato cumulativo — deixou a arquitetura
**mais apta a evoluir**.

> **Obrigatorio por QG-6** sobre mudanca **C3** (FND-01 §6.2; FND-09 §10.2).
> **Este `FIT` nao se ratifica** — **`FT-10`**. **Quarto `FIT` emitido sob fundamento normativo.**

## Escopo
| Item | Definicao |
|---|---|
| Objeto avaliado | [PT-2026-004](../relatorio-transicao-2026-07-29-ratificacao.md) · os **candidatos cumulativos** de FND-09 e FND-10 · a **verificacao pre-aplicacao** dos **12** objetos de PS-2026-004 a 008 · catalogo mestre e `BL-2026-07-29-06` |
| Estado anterior | **155 artefatos, 42.785 linhas** *(`BL-2026-07-29-05`)*; **25** ressalvas abertas; **12** vereditos consecutivos `apto-com-ressalva` |
| **Nao** inclui | O **merito** dos cinco pacotes · qualquer objeto **aplicado** — **nenhum foi** · qualquer Spec ou Framework — **nenhum criado** · **FIT-2026-011** e **FIT-2026-012**, **nao editados** |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| **Executa** | **DEP-QAR** | FT-02, CV-08 |
| Forma | **DEP-GOV** | FND-09 §8.2, linha `FIT` |
| Evidencia | **DEP-KMS** | Medicoes de hash, linha, link e acervo |
| **Aprova** | **SOBERANO** | Cascata de `DEP-EXE I-2` no terminus, **terceira vez consecutiva** |
| Ratifica | **Nao aplicavel** | **`FT-10`** |

> **Terceira ocorrencia consecutiva do terminus, e a causa nao mudou:** **DEP-EXE** e area
> alcancada por ADR-0018 e ADR-0019; **DEP-GOV produziu 7 dos 8 objetos avaliados** — todos
> menos os dois arquivos cumulativos, que sao **derivados por ferramenta a partir de candidatos
> de terceiros**. `FT-14` preserva o efeito processual **sem depender de ato**.

---

## Sumario

| # | Pergunta | Resposta | Sinal |
|---|---|---|---|
| F1 | Complexidade aumentou sem ganho proporcional? | **Nao** | **+2 artefatos** contra **12 objetos verificados sem falha** e **a lacuna do cumulativo fechada** |
| F2 | Algum conceito foi duplicado? **e** a prevencao foi aplicada? | **Nao · aplicada** | **6** reproducoes barradas; **0** pacotes editados ou reabertos |
| F3 | Alguma abstracao ficou desnecessaria? | **Nao** | **Zero regras novas.** `O1`–`O4` ganharam **os dois membros que faltavam**, e nenhuma regra entrou em fundacional |
| F4 | Continua mais simples de evoluir? | **Sim** | **O risco tecnico da aplicacao caiu a zero:** antes, ratificar PS-005 **e** PS-008 produziria objeto errado |
| F5 | Custo de contexto subiu ou desceu? | **DESCEU** — **1,4%** contra 6,1% | **11a medicao, 7a itemizada.** ⚠️ **Comparabilidade declarada** — §F5.1 |
| F6 | Favorece reutilizacao? | **Sim** | **Busca por hash** e **candidato cumulativo** viram procedimento |

**Veredito:** `apto-com-ressalva` — **uma** ressalva nova e **uma reclassificacao com correcao
de erro proprio**.
**Fechamento: `BLOCKED`** — por **ausencia de ato**, nao por defeito (§Fechamento).

---

## F1 — A complexidade aumentou sem ganho proporcional?

| Medida | Antes | Depois | Variacao |
|---|---|---|---|
| Artefatos | 155 | **157** | **+2** |
| Linhas | 42.785 | **43.498** | **+713 (+1,6%)** |
| **Documentos fundacionais emendados** | — | **0** | FND-01 **1.4.0**, FND-02 **1.2.0**, FND-09 **1.3.0**, FND-10 **1.2.0** — `H-A` **identicos** a copia datada |
| **Cartas emendadas** | — | **0** | `DEP-KMS` e `DEP-ENG` seguem em **1.0.0** |
| **Pacotes soberanos editados** | — | **0** | PS-2026-004 a 008 **intactos** |
| **Transicoes O4 executadas** | — | **0** | ADR-0016 a ADR-0019 seguem `em-revisao` · `pendente` |
| **Minutas novas** | — | **0** | Vedacao expressa |
| Entidades · tipos · camadas · portoes · departamentos · classes | 21·33·5·7·9·4 | **21·33·5·7·9·4** | **0** |
| **Objetos de ratificacao verificados** | **0** | **12** | **`H-A`, `H-N`, `H-P` e `IR-09`** |
| **Candidatos localizados** que a missao anterior dava por inexistentes | — | **6** | **Erro proprio corrigido** |
| **Candidatos cumulativos construidos** | 0 | **2** | **Fora do acervo**, com caminho declarado |
| Artefatos **M1** editados | — | **0** | — |
| **Achados fechados** | — | **1 metade** | A **lacuna** de `RD-19` |
| Achados **novos** | — | **1** | **RD-21** |

**Leitura.** **O menor acrescimo da serie** — dois artefatos — e o **maior ganho de
confiabilidade por artefato**: **doze objetos submetidos ao Soberano passaram de *"integros
porque o pacote diz"* para *"integros porque foram medidos"***, e **o cumulativo que faltava
existe**.

**Contrapartida honesta:** **um achado novo**, e **a reemissao formal de PS-2026-008 permanece
devida** — bloqueada pela propria vedacao da missao.

**Resposta:** **nao**.

## F2 — Algum conceito foi duplicado? E a prevencao foi aplicada?

| Conceito | Onde ja estava | Como a mudanca o trata |
|---|---|---|
| **A prova de consumo celula a celula** | `PT-2026-003 §4` | **PT-2026-004 §6 declara o resultado e nao reproduz a tabela** |
| **O merito dos cinco pacotes** | PS-2026-004 a 008 | **Referenciado, nao reaberto.** **Zero pacotes editados** |
| **Os diffs literais** | §2 de cada pacote | **PT-2026-004 §2 os referencia por linha alterada**, sem reproduzi-los |
| **Os requisitos que a camada impoe as Specs** | `PT-2026-001 §7` | **Nao reproduzidos** |
| **O registro do ato** | — | **Nenhum criado** — **nao houve ato**, e registrar ausencia como Diretiva criaria um sexto ato inexistente |
| **A regra de rebase `O1`–`O4`** | `PS-2026-008 §5` | **Aplicada, nao reescrita.** PT-2026-004 §4 **executa** `O2` em substancia e declara o que falta |

**6 reproducoes barradas · 0 duplicacoes novas · 0 pacotes reabertos.**

**Resposta:** nao houve duplicacao · prevencao **aplicada**.

## F3 — Alguma abstracao ficou desnecessaria?

| Abstracao | Membros antes | **Membros agora** | Veredito |
|---|---|---|---|
| **`O1` a `O4`** *(rebase de pacotes concorrentes)* | **0 exercidos** | **2 exercidos** — FND-09 e FND-10 | **Justificada e exercida.** Nasceram na missao anterior **sem membro**; agora **produziram objeto medido** |
| **`IR-07`** *(tres hashes)* | 19 artefatos | **19 artefatos** | **Justificada** |
| **`IR-09`** *(reconstrucao)* | 14 artefatos | **20 artefatos** | **Justificada** — **6 de 6** nesta continuacao |
| **`HZ-01` a `HZ-08`** | 0 membros | **0 membros** | ⚠️ **Suspeita mantida — sexto ciclo** |
| **`PV-1` a `PV-4`** | 3 versoes | **3 versoes** | **Inalterada** — nenhuma versao substituida |

**Zero regras normativas criadas.** **Nenhuma entrou em fundacional, Carta ou pacote.**

**Resposta:** **nao**.

## F4 — O sistema continua mais simples de evoluir?

| Mudanca-tipo | Antes | Depois | Aprovacoes |
|---|---|---|---|
| **Aplicar PS-005 e PS-008 no mesmo ato** | **Produziria objeto errado** — dois candidatos `1.4.0` distintos | **Objeto unico, medido, com ordem declarada** | Inalterado |
| **Achar um candidato submetido** | **Falhou na missao anterior** — busca por nome | **Busca por `sha256`; 6 de 6 achados** | Inalterado |
| **Confiar no `H-P` projetado** | Promessa publicada antes de o arquivo existir | **Calculado e conferido — 6 de 6** | Inalterado |
| **Saber se um pacote esta aplicavel** | Leitura do proprio pacote | **12 verificacoes por ferramenta** | Inalterado |
| **Recuperar o candidato lendo so o pacote** | **Impossivel** | **Ainda impossivel** — `RD-19`, metade aberta | Inalterado |

**Nenhuma aprovacao nova; nenhum titular ampliado; nenhum papel ganhou veto.**

**Resposta:** **sim** — e **desta vez sem condicionar ao ato**: as quatro primeiras linhas
**ja valem hoje**, porque sao **metodo**, nao norma.

## F5 — A mudanca reduz ou aumenta o custo de contexto?

### F5.1 A medicao, itemizada — **a setima da serie**

**Pacote minimo medido: 595 linhas sobre 42.785 = 1,4%.**

| Bloco | Linhas |
|---|---|
| **Recortes de pacote** — PS-2026-004 §2 e §3; PS-2026-006 §2, §3 e §4 | **227** |
| **Inspecao dos candidatos** — frontmatter, linhas alteradas e pontos de insercao de FND-09 e FND-10 | **68** |
| **Extracoes por ferramenta** — busca de ato, varredura por hash, verificacao pre-aplicacao, montagem do cumulativo, reconciliacao, C11 | **100** |
| **Indices abertos para propagar (C11)** | **200** |
| **Total** | **595** |

**A serie observada e 23% · 33% · 30,6% · 18,5% · 21,3% · 18,9% · 13,3% · 15,1% · 12,0% ·
6,1% · 1,4%.**

> ### ⚠️ A comparabilidade e limitada, e a limitacao e declarada
> **Esta e uma missao de verificacao, nao de producao.** As dez medicoes anteriores mediram
> missoes que **escreveram norma**; esta **conferiu objetos ja escritos**, e quase todo o
> trabalho foi **criptografico, executado por ferramenta**, nao por leitura.
>
> **A queda e real e a causa e verificavel** — **nenhum pacote foi lido integralmente**,
> **nenhuma Carta foi aberta**, **nenhuma fundacional foi carregada** —, **mas comparar
> 1,4% com os 23% da primeira missao mede coisas diferentes.** **R4 de FIT-2026-002 ja
> fechou** em FIT-2026-012, com duas descidas **de missoes comparaveis**; **esta medicao nao e
> usada para fechar nada**, e esta registrada com a ressalva escrita.
>
> **O piso obrigatorio nao mudou:** **nenhuma fundacional foi emendada**.

**Resposta:** **desceu** — **com comparabilidade declarada como limitada**.

## F6 — Ela favorece reutilizacao?

| Definicao produzida | Reutilizavel por | Especifica do caso? |
|---|---|---|
| **Provar ausencia de arquivo por `sha256`, nunca por nome** | **Toda busca por objeto submetido** | Nao |
| **Construir o candidato cumulativo antes do ato, com ordem declarada** | **Toda fonte com duas emendas pendentes** | Nao |
| **Conferir o `H-P` projetado calculando a transicao** | **Todo pacote com `H-P`** | Nao |
| **Verificacao pre-aplicacao como tabela de 12 objetos × 6 criterios** | **Todo ato futuro** | Nao |
| **Declarar o caminho do candidato no pacote** | **Todo pacote** | Nao |
| **Ensaiar a aplicacao em sandbox fora do acervo, e destrui-lo em seguida** | **Todo pacote antes do ato** | Nao |
| RD-21 | — | **Sim** |

**Evidencia mais forte:** **a varredura por hash**. **4.891 arquivos**, **6 candidatos
achados**, **6 hashes reproduzindo** — e a missao anterior os declarara inexistentes.
**O metodo custou uma execucao e corrigiu um achado de severidade Media.**

**Resposta:** **sim**.

---

## Ressalvas

| # | Ressalva | Custo assumido | **Dono** | **Gatilho** |
|---|---|---|---|---|
| **R1** | **`RD-21` — a reemissao rebaseada de PS-2026-008 e devida e nao foi executada**, por vedacao expressa a produzir minuta. A minuta vigente de [PS-2026-008 §7](../pacote-soberano-2026-07-29-rd-15.md) enumera o candidato **nao cumulativo** | **Ratificar PS-005 e PS-008 pela minuta atual produziria objeto errado.** Mitigado — nao suprido — por [PT-2026-004 §4](../relatorio-transicao-2026-07-29-ratificacao.md), que publica os hashes cumulativos | **DEP-GOV** | **Primeira missao sem a vedacao**, ou **ato que alcance os dois pacotes** |

### A seguinte e **reclassificacao com correcao de erro proprio**, e **nao entra na contagem de abertas**

| # | Ressalva existente | De | **Para** |
|---|---|---|---|
| **R2** | **R1 de FIT-2026-012** *(`RD-19`)* | *"candidatos sao publicados como **diff + hash, sem arquivo**"* — **afirmacao falsa** | 🔁 **RECLASSIFICADA E CORRIGIDA.** Os **6** candidatos **existem e reproduzem os `H-A` publicados**. O defeito real e ***"o pacote nao declara o caminho do arquivo que mede"***. **A metade da lacuna — o cumulativo — FECHA com evidencia** (PT-2026-004 §4); a metade da **declaracao de caminho** permanece. Gatilho novo: **reemissao de PS-004, 005 ou 006** |

**Ressalvas abertas apos este ciclo: 25 + 1 = 26.** **Zero em duplicidade.**

## Veredito

| Campo | Conteudo |
|---|---|
| Veredito | **`apto-com-ressalva`** |
| Fundamento | **Doze objetos submetidos ao Soberano foram medidos e passaram sem uma falha** — `H-A`, `H-N`, `H-P` projetado e **`IR-09` em 6 de 6** —, **a lacuna do candidato cumulativo fechou com objeto medido e ordem declarada**, e **um achado de severidade Media da missao anterior foi corrigido com o erro escrito**. **Zero fundacionais, zero Cartas, zero pacotes e zero artefatos M1 alterados**; **zero regras criadas**. Em contrapartida, **um achado novo** e **a reemissao formal de PS-2026-008 permanece devida**. **Nao e `inapto`** porque nenhuma contrapartida revela degradacao. **Nao e `apto` sem ressalva** porque **26 dividas seguem abertas** e porque **`RD-21` toca a aplicabilidade de um pacote ja na mesa do Soberano** |
| Efeito | **Encerra a verificacao.** A ressalva nova vira divida declarada (FND-07 §9); a reclassificacao **corrige** uma ressalva existente **sem duplica-la** |
| Data | 2026-07-29 |
| Executado por | **DEP-QAR** |
| Aprovado por | **SOBERANO** — **pendente**; cascata de `I-2` no terminus |
| Ratificado por | **Nao aplicavel — `FT-10`** |

## Fechamento — **`BLOCKED`**

| # | Condicao | Estado | Evidencia |
|---|---|---|---|
| **(a)** | **Cobertura 9/9** | ✅ **CUMPRIDA** | **9** Cartas em vigor, **nenhuma alterada** |
| **(b)** | **Autoridade inequivoca** | ❌ **NAO CUMPRIDA — e a causa e so o ato** | **Cinco bloqueios de autoridade, os cinco com pacote integro e verificado.** **Zero instrumentos faltando** |
| **(c)** | **Validacao independente** | ✅ **Cumprida** | **1.924** links com **0** quebrados · **96** artefatos com `autor` e `revisor`, **0** coincidencias · **0** credenciais · **12 objetos verificados, 0 falhas** |
| **(d)** | **Rastreabilidade** | ✅ **Cumprida** | Cadeia **pacote → RFC → ADR → fonte → candidato → `H-A` → diff → ordem → substituida → efeito** fechada nas **cinco** cadeias |
| **(e)** | **Pacote soberano completo** | ✅ **Cumprida** | **Cinco**, os cinco com minuta e **agora com candidato medido** |

### A decisao

| Campo | Conteudo |
|---|---|
| **Decisao** | **`BLOCKED`** |
| **Causa** | **Ausencia de ato** — pre-condicao 5. **Nao e defeito de objeto:** os 12 passaram |
| **Por que nao `GO-TO-SPECS`** | Exige **objetos vigentes**. **Nenhum vigora** |
| **Por que nao `ADJUST`** | Pressupoe **defeito delimitado corrigivel**. **Nao ha defeito a corrigir** — ha ato a aguardar |
| **A camada esta pronta para consumo?** | **NAO — e pela primeira vez nao ha nada a fazer alem de aguardar.** Ha um ciclo faltavam **instrumentos**; depois, **atos**; agora **os instrumentos estao verificados objeto a objeto** |
| **Desempenho** | **Nao exercido, logo nao comprovado.** **41 de 123** indicadores `definido, sem valor`. **Nao bloqueia Specs** |

## Pendencias para o SOBERANO — **seis**

| # | Pendencia | Origem | Se nao houver ato |
|---|---|---|---|
| **PS-5** | `DEP-KMS` 1.1.0 · `DEP-ENG` 1.1.0 | PS-2026-006 | **RC-05 e RC-07 abertos** |
| **PS-6** | `RD-09` | PS-2026-005 | `FT-10` prevalece; divergencia envelhece |
| **PS-7** | `RD-02` | PS-2026-004 | **Quinto ciclo** |
| **PS-9** | `RD-14` | PS-2026-007 | **`QG-1` sem liberador legitimo** |
| **PS-10** | `RD-15` | PS-2026-008 | **Spec C2/C3 sem titular unico** |
| **PS-11** | Aprovacao de **FIT-2026-011, 012 e 013** | Cascata no terminus, **tres vezes** | Vereditos **produzem efeito processual** (`FT-14`); falta o aceite |

### Nota sobre FT-04

| Verificacao | Estado |
|---|---|
| Vereditos emitidos | **13** |
| Consecutivos `apto` **sem ressalva** | **0** |
| `inapto` emitidos | **0** — em **treze** oportunidades |
| Ressalvas e achados fechados neste ciclo | **1 metade** — a lacuna de `RD-19` |
| Achados novos | **1** — `RD-21` |
| **Achados de ciclo anterior corrigidos por erro proprio** | **1** — `RD-19`. **Primeira vez na serie** |

**Permanece o numero a vigiar: nenhum `inapto` em treze oportunidades.** **Em contrapartida,
este ciclo corrigiu um erro da propria serie** — o oposto de complacencia.

## Aprendizado gerado

| Registro APR | Licao |
|---|---|
| A gravar por DEP-KMS *(QG-5)* | **Ausencia de arquivo se prova por hash, nunca por nome de diretorio.** Acao: **"nao existe" exige varredura por conteudo**. Dono: DEP-KMS |
| A gravar por DEP-KMS *(QG-5)* | **Pacote que mede um objeto sem dizer onde ele esta torna o objeto irrecuperavel por quem le so o pacote.** Acao: **todo pacote declara o caminho canonico do candidato medido**. Dono: DEP-GOV |
| A gravar por DEP-KMS *(QG-5)* | **Duas emendas pendentes sobre a mesma fonte exigem cumulativo medido antes do ato.** Acao: **ordem explicita e cumulativo sao condicao de submissao**. Dono: DEP-GOV |
| A gravar por DEP-KMS *(QG-5)* | **Medicao de custo de contexto entre missoes de natureza diferente nao e comparavel sem ressalva.** Acao: **toda medicao declara se a missao foi de producao ou de verificacao**. Dono: DEP-QAR |

## Historico de vereditos sobre este objeto

| FIT | Data | Veredito | Relacao |
|---|---|---|---|
| FIT-2026-011 | 2026-07-29 | `apto-com-ressalva` | Fechamento **`READY-FOR-RATIFICATION`** |
| FIT-2026-012 | 2026-07-29 | `apto-com-ressalva` | Fechamento **`READY-FOR-RATIFICATION`**; abriu `RD-19` |
| **FIT-2026-013** | 2026-07-29 | **`apto-com-ressalva`** | **Nao supera nem edita nenhum anterior** (M1, LV-04, FT-09). **Corrige `RD-19`, aberto por FIT-2026-012** — a correcao vive **aqui**, e o `FIT` anterior **permanece intacto**. Fechamento **`BLOCKED`** por **ausencia de ato**, **nao por regressao**: a condicao **(b)** mantem a causa *"falta ato"* |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-QAR | Verificacao de aptidao da **continuacao da Missao 1.12**: **ato ausente**, **12 objetos das cinco cadeias verificados com ZERO falhas** — `H-A`, `H-N`, `H-P` projetado e **`IR-09` em 6 de 6** —, **candidato cumulativo de FND-09 e FND-10 construido, medido e preservado** com ordem explicita, e **`RD-19` corrigido**: os **6** candidatos que FIT-2026-012 dava por inexistentes **estao em disco e reproduzem os `H-A` publicados**; a causa do erro foi **buscar por nome em vez de por hash**. **Zero fundacionais, zero Cartas, zero pacotes, zero artefatos M1 alterados; zero transicoes O4; zero minutas; zero regras criadas.** **`O1`–`O4` ganharam os dois membros que faltavam.** F5 desce a **1,4%**, **com comparabilidade declarada como limitada** — missao de **verificacao**, nao de producao —, e **nao e usada para fechar nenhuma ressalva**. Uma ressalva nova, **`RD-21`** *(reemissao rebaseada de PS-2026-008, devida e vedada)*, e **uma reclassificacao que corrige erro proprio da serie — a primeira**. Fechamento **`BLOCKED`**, com a condicao **(b)** nao cumprida **apenas por falta de ato**. **Quarto `FIT` sob `FT-10`; terceiro consecutivo com aprovacao no terminus da cascata.** |
