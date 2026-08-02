---
id: ADR-0016-semantica-da-matriz-de-interacao
titulo: Emenda C3 a FND-02 §4 para fixar a semantica da matriz de interacao e o alcance do veto da Guarda
tipo: adr
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-07-29
atualizado_em: 2026-07-29
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0008, ADR-0011, ADR-0012]
substitui: []
substituido_por: null
classe_mudanca: C3
tipo_decisao: 2
supera: []
superado_por: null
resumo: Fixa a semantica de FND-02 §4 — direcao, cardinalidade, precedencia e alcance do veto da Guarda —, acrescenta o codigo R e corrige doze celulas, sem criar autoridade nem alterar titular de decisao.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: ratificada
---

# ADR-0016: A semantica da matriz de FND-02 §4

> ## O estado deste ADR e o do seu frontmatter, e nada alem dele
>
> **A fonte corrente do estado e o campo `ratificacao`** (FND-10 §5.4). Enquanto ele disser
> `pendente`, este ADR **nao produz efeito** e FND-02 permanece em **1.2.0**; quando disser
> `ratificada`, produz. **Nenhuma frase deste texto afirma vigencia**, para que a ratificacao
> nao torne o proprio documento falso — que e o defeito **RD-08**, registrado em
> [MSG-2026-0004 §8](../memory/operacional/MSG-2026-0004-ato-soberano-cartas-emenda-constitucional-e-regime-do-fitness-check.md)
> e vivo em `ADR-0014`.

## Proposito
Fechar **RD-02** na fonte: fixar o que a matriz de **FND-02 §4** significa e fazer com que ela
consiga expressar o veto que **FND-02 §3** ja constitui.

## Escopo
| Item | Definicao |
|---|---|
| Inclui | A emenda **C3** a **FND-02 §4**: legenda, cardinalidade, precedencia, **12** celulas, **MI-01 a MI-06** e **5** exemplos normativos |
| **Nao** inclui | **Quem** tem veto *(FND-02 §2.1 — intacta)* · o **objeto** do veto *(§3 — intacta)* · FND-01 §7.3 · FND-09 §8.2 *(objeto de [ADR-0017](ADR-0017-harmonizacao-do-regime-do-parecer.md))* · qualquer Carta · qualquer entidade, tipo, camada, portao ou departamento novo — **nenhum criado** |
| Origem | [RFC-0012](../rfcs/RFC-0012-semantica-da-matriz-de-interacao.md) |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| Propoe | **DEP-GOV** | FND-09 §8.2, linha `FND` |
| Revisor independente | **DEP-QAR** | RM-06b |
| Aprova e **ratifica** | **SOBERANO** | **C3.** Indelegavel (PI-01, FND-04 §2) |

---

## 1. Contexto

**RD-02** nasceu na Missao 1.10 e sobreviveu a um ato soberano que expressamente **nao o
alcancou** (MSG-2026-0004 §4). E a **condicao nomeada** do fechamento `GO-CONDITIONAL` de
FIT-2026-010, e o **unico achado aberto que toca autoridade**.

## 2. Problema

A matriz de FND-02 §4 e **departamento × departamento e monovalorada**. O veto da Guarda,
definido em §3, incide sobre o **objeto**. Autoridade objetal so cabe numa matriz departamental
se **todos** os produtores forem enumerados — e a tabela enumerou **5 de 7**.

## 3. Criterios de decisao

| # | Criterio |
|---|---|
| **K1** | Fechar a ambiguidade **na fonte**, nao por contencao |
| **K2** | **Nao criar autoridade**: so declarar a que ja existe, com a fonte citada |
| **K3** | Nao alterar nenhum titular de decisao de FND-01 §7.3 |
| **K4** | Nao editar Carta em vigor |
| **K5** | Deixar a tabela capaz de expressar o que as nove Cartas **ja** declaram |

## 4. Alternativas consideradas

### Alternativa A — Corrigir apenas as duas celulas de RD-02
Trocar `GOV→KMS` e `QAR→KMS` de `E` para `V`. **Recusada: falha K1 e K5.** Deixa `GOV→EXE` e
`QAR→EXE` sem veto, perde a entrega que `E` registrava, e a celula segue monovalorada.

### Alternativa B — Corrigir a leitura obrigatoria, mantendo as celulas
Reescrever *"vetam a Linha e a Plataforma"* para *"vetam a Linha e DEP-TLS"*. **Recusada:
falha K2 por inversao** — retiraria de `DEP-KMS` e `DEP-EXE` um veto que as **proprias Cartas
declaram sofrer**, o que e alterar autoridade por reducao.

### Alternativa C — Emendar §4 integralmente *(escolhida)*
Legenda direcional de 6 codigos, celula multivalorada, `MI-01` a `MI-06`, 12 celulas e 5
exemplos. **Satisfaz K1 a K5.**

### Alternativa D — Substituir a matriz por uma tabela objeto × autoridade
**Recusada:** criaria instrumento novo (MT-01, CS-01) e obrigaria a reescrever §6.3 das nove
Cartas em vigor — **falha K4**, e por larga margem.

### Alternativa Z — Nao emendar
**Recusada: falha K1.** RD-02 entra no terceiro ciclo e `GO-TO-SPECS` permanece impossivel.

## 5. Decisao *(depende de ratificacao)*

| # | Regra que passa a existir em FND-02 §4.3 |
|---|---|
| **MI-01** | **A celula e a fonte; as leituras obrigatorias sao projecao dela.** Em conflito, prevalece a celula, e a correcao e **na leitura** (ADR-0008, PJ-03) |
| **MI-02** | **A matriz nao concede autoridade: projeta FND-01 §7.3, FND-02 §2.1 e §3 e FND-09 §8.2.** Celula divergente e **erro da tabela** |
| **MI-03** | **O SOBERANO nao figura na matriz.** Autoridade que nele termina le-se em FND-01 §7.3 e FND-09 §8.2 |
| **MI-04** | **Ausencia nao cria nem retira autoridade.** `—` e ausencia de ato **de X sobre Y** |
| **MI-05** | **O veto da Guarda incide sobre o objeto, nao sobre a classe do produtor** — por isso alcanca as quatro classes |
| **MI-06** | **`R` declara apenas revisao estrutural e permanente entre dois departamentos**; o mapa por entidade permanece em FND-09 §8.2 |

**Legenda:** seis codigos — `E` `C` `V` `A` **`R`** `—` —, com definicao operacional por codigo,
direcao declarada e **celula multivalorada** autorizada.
**Matriz:** **12** celulas alteradas, **69** inalteradas — diff literal em
[PS-2026-004 §2](../governance/pacote-soberano-2026-07-29-rd-02.md), item a item.
**Leituras obrigatorias:** duas corrigidas, tres inalteradas.
**Exemplos normativos:** **5** — `EX-1` a `EX-5`.

### 5.1 Versao proposta
**FND-02 1.2.0 → 1.3.0** *(MENOR)*. `H-A`, `H-N` e **`H-P` projetado** em PS-2026-004 §3.

### 5.2 O que esta decisao **nao** faz

| Nao faz | Norma que o impede |
|---|---|
| **Nao** da veto a nenhum departamento novo | FND-02 §2.1 — `V` segue exclusivo de GOV e QAR |
| **Nao** altera titular de decisao | FND-01 §7.3 **nao e tocada** |
| **Nao** edita nenhuma das nove Cartas | Todas `ativo` · `ratificada`; emendar exige ato proprio (IR-01, DC-09) |
| **Nao** cria entidade, tipo, camada, portao, departamento ou diretorio | CS-01, MT-01, PI-12 |
| **Nao** fecha RD-01, RD-03, RD-10 nem RD-11 | RFC-0012 §7 — os quatro seguem com dono e gatilho |
| **Nao** alcanca FND-09 §8.2 nem FND-10 §10.3 | Objeto de **ADR-0017**, pacote separado |

## 6. Justificativa

| # | Fundamento |
|---|---|
| 1 | **A determinacao e leitura da fonte, nao escolha.** Cada uma das seis perguntas de RFC-0012 §4 tem evidencia citada em documento em vigor |
| 2 | **A evidencia mais forte e unanime: 14 afirmacoes de veto em 7 Cartas, zero excecoes.** A matriz carregava **10** |
| 3 | **Nasce com membros verificados.** A celula multivalorada tem **9** membros observados em **7** Cartas antes de virar regra — AQ-03 exige dois |
| 4 | **A precedencia nao e invencao: e o desenho que FND-09 §8.2 ja aplica a si proprio**, e que ADR-0008 ja fixou para toda projecao |
| 5 | **Fecha a causa, nao o efeito.** Trocar duas celulas fecharia RD-02 e deixaria o instrumento incapaz de expressar a proxima relacao composta |

## 7. Impacto

| Dimensao | Impacto |
|---|---|
| Autoridade criada | **ZERO** — MI-02 declara a matriz projecao |
| Titulares alterados | **ZERO** — FND-01 §7.3 intacta |
| Departamentos com veto | **2 antes · 2 depois** — GOV e QAR |
| Departamentos vetaveis | **5 declarados na tabela antes · 7 depois** — e **7 ja declarados nas Cartas** desde o rollout |
| Documentos fundacionais emendados | **1** — FND-02. FND-01 e FND-03 a FND-10 **intactas** |
| Cartas alteradas | **0** |
| Entidades · tipos · camadas · portoes · departamentos | **0** criados |
| Linhas | FND-02 **479 → 518** *(+39)* |
| Custo de contexto | **+39 linhas** em artefato `missao`. **FND-02 nao e `nucleo`**, mas integra o pacote minimo de `DEP-EXE` — o piso dele sobe **39 linhas** |
| Reversibilidade | **Tipo 2** — §10 |

## 8. Evidencias

| # | Evidencia | Fonte |
|---|---|---|
| **E1** | 81 celulas medidas com a matriz **extraida do arquivo**; distribuicao `—`15 · `C`24 · `E`26 · `V`10 · `A`6 | RFC-0012 §3 |
| **E2** | **14** afirmacoes *"GOV/QAR veta \<eu\>"* em **7** Cartas nao-Guarda; **0** excecoes | §6.3 das nove Cartas |
| **E3** | **9** declaracoes compostas em **7** Cartas que a celula monovalorada nao comporta | §6.3 das nove Cartas |
| **E4** | `DEP-GOV §6.3` escreve literalmente *"entrega e veto"* para DEP-KMS | `departments/gov/carta.md` |
| **E5** | `DEP-EXE §9` declara-se **contribuinte obrigatorio** da camada APR — sustenta M1 | `departments/exe/carta.md` |
| **E6** | `DEP-QAR §5` declara **DEP-KMS consulta obrigatoria** do veredito `FIT` — sustenta o `C` de M5 | `departments/qar/carta.md` |
| **E7** | Precedencia fonte × projecao ja exercida por FND-09 §8.2 sobre si propria | `foundation/09-meta-model.md` §8.2 |
| **A1** | **Evidencia ausente, declarada:** **nenhum veto real** foi exercido no acervo — sobre nenhuma classe. O alcance e **determinado por norma, nunca observado em operacao** (PI-10, LV-12) | KQ-8 de `DEP-QAR §11` |

## 9. Riscos e mitigacao

| # | Risco | Prob. | Impacto | Mitigacao |
|---|---|---|---|---|
| **RA-1** | Celula multivalorada vira empilhamento sem fonte | Media | **Alto** | **MI-02** |
| **RA-2** | `R` duplica FND-09 §8.2 | **Media** | Medio | **MI-06** + CM-09 |
| **RA-3** | Veto sobre o Comando lido como subordinacao | Baixa | **Alto** | Veto e **objetal** e so o Soberano o reverte (LV-09); **ES-02 intacta** |
| **RA-4** | Os 4 residuos de Carta (RD-11) envelhecem sem gatilho | **Media** | Medio | Gatilho literal: *"proxima emenda a `DEP-EXE`, `DEP-GOV` e `DEP-QAR`"*. Registrado em RFC-0012 §7 e no catalogo |

## 10. Plano de reversao

| Campo | Conteudo |
|---|---|
| Reversivel? | **Sim — Tipo 2** |
| Como | ADR que supere este + ato do Soberano, restaurando FND-02 **1.2.0** pelo diff de PS-2026-004 §2, que e **literal e reversivel** |
| Custo | Baixo. **Nenhuma Carta, nenhum indice e nenhum outro fundacional precisa mudar para reverter** |
| O que **nao** se reverte | Os atos soberanos ja registrados |
| Copia datada | **137** arquivos, fora do acervo, anterior a qualquer edicao desta missao (PI-07, AF-35) |

## 11. Classificacao

| Campo | Valor | Justificativa |
|---|---|---|
| Classe | **C3 — constitucional** | Materia **direitos de decisao** (FND-04 §2). O efeito e declaratorio e o **enquadramento segue a materia, nao o tamanho do efeito** |
| Tipo | **2 — reversivel** | §10 |
| Ratificacao | **EXIGIDA — SOBERANO** | C3; FND-09 §8.2, linha `FND` |
| Instrumento | **RFC → ADR → ratificacao** | [RFC-0012](../rfcs/RFC-0012-semantica-da-matriz-de-interacao.md) |
| Fitness Check | **Obrigatorio** | [FIT-2026-011](../governance/fitness/FIT-2026-011-fechamento-de-autoridade.md) |

## 12. Revisao

| Campo | Conteudo |
|---|---|
| Revisor independente | **DEP-QAR** — nao produziu o texto |
| Residuo declarado | **DEP-QAR e objeto de 2 das 12 celulas** *(M5, M7)* e de 2 das 4 de autoridade. A revisao de **merito** foi executada por **DEP-QAR sobre texto de DEP-GOV**; o que DEP-QAR **nao** faz e julgar a propria autoridade — e o julgamento e do **SOBERANO** (I-5, RM-06b). **Quarta ocorrencia da familia de RC-02**; permanece **declarado, nao resolvido** |
| Gatilho de reavaliacao | Primeiro **veto real** sobre departamento de Comando ou de Plataforma |

## 13. Rastreabilidade

| Campo | Conteudo |
|---|---|
| RFC de origem | [RFC-0012](../rfcs/RFC-0012-semantica-da-matriz-de-interacao.md) |
| Achado que fecha | **RD-02** — [PT-2026-001 §10](../governance/relatorio-transicao-2026-07-29-departamentos.md) |
| Ressalva que fecha | **R4** de [FIT-2026-010](../governance/fitness/FIT-2026-010-aplicacao-do-ato-soberano.md) |
| Pacote de decisao | [PS-2026-004](../governance/pacote-soberano-2026-07-29-rd-02.md) |
| Regra de integridade aplicada | [ADR-0012](ADR-0012-integridade-do-ato-de-ratificacao.md), `IR-01` a `IR-10` |
| Precedente de forma | [ADR-0014](ADR-0014-candidato-emenda-fnd-01-7-3-homologa.md) ← [RFC-0011](../rfcs/RFC-0011-emenda-constitucional-ratifica-homologa.md) |
| Documento emendado | **FND-02** 1.2.0 → **1.3.0**, §4 |
| Documentos **nao** emendados | FND-01 · FND-03 a FND-10 · as nove Cartas · as 23 Cartas de Capability |

## Checklist de validade (FND-07 §4.1)

| # | Item | Estado |
|---|---|---|
| 1 | Problema declarado antes da solucao | ✅ §2 |
| 2 | Alternativas reais consideradas, incluindo nao fazer | ✅ §4 — **cinco**, com o motivo da recusa |
| 3 | Criterios de decisao declarados antes da escolha | ✅ §3 |
| 4 | Impacto medido, nao estimado | ✅ §7 — contagens por ferramenta |
| 5 | Evidencia citada por ID | ✅ §8 — inclusive **A1**, evidencia **ausente** |
| 6 | Riscos com mitigacao nomeada | ✅ §9 |
| 7 | Plano de reversao | ✅ §10 |
| 8 | Classe e tipo declarados com justificativa | ✅ §11 |
| 9 | Revisor independente ≠ autor | ✅ §12, com residuo declarado |
| 10 | Rastreabilidade fechada | ✅ §13 |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-GOV | Emenda **C3** proposta a **FND-02 §4**, fechando **RD-02**: legenda direcional de **6 codigos** com `R`, **celula multivalorada**, regras **MI-01 a MI-06**, **5 exemplos normativos** e **12 celulas** corrigidas — **4 de autoridade**, 2 de revisao, 6 de interface. Fundamento: **o veto da Guarda incide sobre o objeto, nao sobre a classe**, e a tabela enumerava **5 de 7** produtores contra **14 afirmacoes** unanimes das Cartas. **Zero autoridades criadas · zero titulares alterados · zero Cartas editadas · zero entidades, tipos, camadas ou portoes novos.** Nasce em `em-revisao` · `ratificacao: pendente`: **C3 so existe com ato do Soberano** (FND-01 §9, FND-04 §2). |
