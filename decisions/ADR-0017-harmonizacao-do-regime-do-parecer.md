---
id: ADR-0017-harmonizacao-do-regime-do-parecer
titulo: Emenda C3 a FND-09 §8.2 e FND-10 §10.3 para alinhar a linha Fitness Check ao regime do parecer
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
decisoes_relacionadas: [ADR-0012, ADR-0015]
substitui: []
substituido_por: null
classe_mudanca: C3
tipo_decisao: 2
supera: []
superado_por: null
resumo: Alinha a linha Fitness Check de FND-09 §8.2 e FND-10 §10.3 a regra vigente FT-10, sem ampliar titulares, sem converter parecer em norma e sem editar Fitness Check historico.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: ratificada
---

# ADR-0017: A linha `Fitness Check` alinhada ao regime do parecer

> ## O estado deste ADR e o do seu frontmatter, e nada alem dele
>
> **A fonte corrente do estado e o campo `ratificacao`** (FND-10 §5.4). Enquanto ele disser
> `pendente`, este ADR **nao produz efeito**, e FND-09 permanece em **1.3.0** e FND-10 em
> **1.2.0**. **Nenhuma frase deste texto afirma vigencia** — a licao de **RD-08**, aplicada.

## Proposito
Fechar **RD-09** na fonte: fazer com que **FND-09 §8.2** e **FND-10 §10.3** digam o que
**`FT-10`** ja determina.

## Escopo
| Item | Definicao |
|---|---|
| Inclui | **Duas** celulas e **duas** notas — `FIT` em FND-09 §8.2 *(fonte)* e `Fitness Check` em FND-10 §10.3 *(cascata, CV-04)* |
| **Nao** inclui | O **merito** de `FT-10`, decidido em [ADR-0015](ADR-0015-fitness-check-e-parecer-nao-decisao.md) · `Revisao Arquitetural` · qualquer outra linha das duas matrizes · **FND-04 §2.1** *(RD-12)* · **FND-02 §4** *(ADR-0016, pacote separado)* · qualquer `FIT` historico *(`FT-15`)* |
| Origem | [RFC-0013](../rfcs/RFC-0013-harmonizacao-do-regime-do-parecer.md) |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| Propoe | **DEP-GOV** | FND-09 §8.2, linha `FND` |
| Revisor independente | **DEP-QAR** | RM-06b |
| Aprova e **ratifica** | **SOBERANO** | **C3.** Indelegavel |

---

## 1. Contexto
O ato de 2026-07-29 determinou o regime do `Fitness Check` e mandou **formalizar pelo rito
aplicavel**. ADR-0015 formalizou em `FT-10` a `FT-15` e **declarou** — sem corrigir — que duas
fundacionais seguiam divergentes, porque **o ato nao as mencionava**. Este ADR e o rito devido.

## 2. Problema
Duas fundacionais **em vigor** declaram *"Ratifica: SOBERANO se C3"* para `Fitness Check`.
A regra vigente e `FT-10`: **parecer nao se ratifica.**

## 3. Criterios de decisao

| # | Criterio |
|---|---|
| **K1** | Alinhar **a fonte**, nao conter o efeito |
| **K2** | **Nao ampliar titular** — nenhum nome entra na coluna *Ratifica* |
| **K3** | **Nao converter parecer em norma** |
| **K4** | **Nao editar `FIT` historico** |
| **K5** | Nao presumir que o ato anterior alcance texto que ele nao nomeou |

## 4. Alternativas consideradas

### Alternativa A — Emendar as duas, fonte e cascata *(escolhida)*
Satisfaz K1 a K5.

### Alternativa B — Emendar **so** FND-09 §8.2
**Recusada: falha K1 por metade.** FND-10 §10.3 **declara-se projecao** de FND-09 §8.2;
corrigir so a fonte deixaria a projecao contradizendo o documento de que ela propria diz derivar
— pior que o estado atual.

### Alternativa C — Manter o texto e conter por regra de redacao, como `IR-11` fez com IC-2
**Recusada: falha K1**, e a evidencia e recente. **IC-2 ficou contido por quatro ciclos e a
colisao reapareceu em outros dois documentos** — o proprio RD-09. Contencao adia; nao fecha.

### Alternativa D — Emendar **FND-04 §2.1**, atacando a regra que gerou o defeito
**Recusada aqui, mantida viva.** E a correcao mais profunda e **nao foi pedida nem ratificada**.
Vira **RD-12**, com dono e gatilho (RFC-0013 §6). **Recusar sem descartar e a diferenca entre
conter e esconder.**

### Alternativa Z — Nao emendar
**Recusada: falha K1.** RD-09 envelhece com `FT-10` prevalecendo sobre texto fundacional
desatualizado.

## 5. Decisao *(depende de ratificacao)*

| # | Alteracao | Documento |
|---|---|---|
| **H1** | Linha `FIT`, coluna *Ratifica*: `SOBERANO se C3` → **`—` *(`FT-10`)*** | **FND-09 §8.2** — **fonte** |
| **H2** | Nota normativa apos a matriz, citando `FT-10`, `FT-11` e `FT-14` | **FND-09 §8.2** |
| **H3** | Linha `Fitness Check`, coluna *Ratifica*: `SOBERANO se C3` → **`—` *(`FT-10`)*** | **FND-10 §10.3** — **cascata** (CV-04) |
| **H4** | Nota declarando a relacao fonte → projecao e que `Revisao Arquitetural` **nao muda** | **FND-10 §10.3** |

**Versoes propostas:** **FND-09 1.3.0 → 1.4.0** · **FND-10 1.2.0 → 1.3.0**.
Diff literal, `H-A`, `H-N` e **`H-P` projetado** em
[PS-2026-005](../governance/pacote-soberano-2026-07-29-rd-09.md).

### 5.1 O que esta decisao **nao** faz

| Nao faz | Norma que o impede |
|---|---|
| **Nao** amplia titular — **zero** nomes entram | K2; a alteracao **retira** materia da mesa do ratificador, e nao acrescenta |
| **Nao** converte parecer em norma | **`FT-12`** |
| **Nao** retira efeito ao veredito `inapto` | **`FT-14`** — efeito **processual**, independente de ato |
| **Nao** edita nenhum `FIT` historico | **`FT-15`** — vedacao expressa do ato de 2026-07-29 |
| **Nao** toca `Revisao Arquitetural` | Ja declara `—`; **nao consta** de FND-09 §8.2 |
| **Nao** emenda **FND-04 §2.1** | Nao pedido, nao ratificado — **RD-12** |
| **Nao** alcanca FND-02 §4 | **ADR-0016**, pacote separado |

## 6. Justificativa

| # | Fundamento |
|---|---|
| 1 | **Fecha a divergencia na fonte**, e nao por contencao — a alternativa C ja falhou uma vez, medida em quatro ciclos |
| 2 | **O merito ja foi decidido.** Este ADR nao redecide `FT-10`: **propaga-o** ao texto que o contradiz (CV-04) |
| 3 | **A cascata ja estava declarada como devida** em ADR-0015 §5.3. Este ADR pede a autorizacao que faltava |
| 4 | **Movimento verificado no sentido conservador:** **uma** materia sai da mesa do ratificador e **nenhuma** entra — e por isso vai ao **C3**, e nao ao C2 |
| 5 | **Declara o que nao resolve.** RD-12 nomeia a regra geradora em FND-04 §2.1 — aplicacao literal da licao de FIT-2026-010 sobre fechar colisao sem varrer as projecoes |

## 7. Impacto

| Dimensao | Impacto |
|---|---|
| Titulares ampliados | **ZERO** |
| Titulares reduzidos | **1 materia** — `FIT` sai da coluna *Ratifica*, por determinacao do proprio Soberano |
| `FIT` que mudam de valor no campo `ratificacao` | **ZERO** — os **dez** ja declaram `nao-exigida` |
| `FIT` historicos editados | **ZERO** (`FT-15`) |
| Documentos fundacionais emendados | **2** — FND-09 e FND-10. FND-01 a FND-08 **intactas** |
| Cartas alteradas | **0** |
| Entidades · tipos · camadas · portoes | **0** criados |
| Linhas | FND-09 **1.243 → 1.252** *(+9)* · FND-10 **764 → 771** *(+7)* |
| Custo de contexto | **+16 linhas**. **FND-09 e FND-10 sao `nucleo` por recorte** — o piso obrigatorio sobe **apenas se o recorte alcancar §8.2 ou §10.3**, e alcanca: **+2 linhas de matriz e +11 de nota** |
| Reversibilidade | **Tipo 2** |

## 8. Evidencias

| # | Evidencia | Fonte |
|---|---|---|
| **E1** | FND-09 §8.2, linha `FIT`, declara `SOBERANO se C3` | `foundation/09-meta-model.md` |
| **E2** | FND-10 §10.3, linha `Fitness Check`, declara `SOBERANO se C3` | `foundation/10-artifact-framework.md` |
| **E3** | FND-10 §10.3 **declara-se projecao** de FND-09 §8.2, com precedencia da fonte | idem, nota PJ-02 |
| **E4** | `FT-10` a `FT-15` em vigor | [ADR-0015 §5.1](ADR-0015-fitness-check-e-parecer-nao-decisao.md) |
| **E5** | A cascata **declarada devida e nao autorizada** | [ADR-0015 §5.3](ADR-0015-fitness-check-e-parecer-nao-decisao.md) |
| **E6** | **10 de 10** `FIT` do acervo declaram `ratificacao: nao-exigida` — a pratica nunca seguiu o texto | `governance/fitness/` |
| **A1** | **Evidencia ausente, declarada:** **nenhum `FIT` foi jamais submetido a ratificacao**, nem sob o texto antigo. A eficacia da correcao e **prevista, nao observada** (PI-10) | KQ-1 de `DEP-QAR §11` |

## 9. Riscos e mitigacao

| # | Risco | Prob. | Impacto | Mitigacao |
|---|---|---|---|---|
| **RA-1** | Ler como *"parecer perdeu forca"* | **Media** | Medio | `FT-14` citado **dentro** da nota H2 |
| **RA-2** | O mecanismo sobrevive em FND-04 §2.1 | **Media** | Medio | **RD-12**, declarado com dono e gatilho |
| **RA-3** | Emendar `nucleo` sobe o piso de todo carregamento | Baixa | Baixo | **+16 linhas**, das quais **2** de matriz. Declarado, nao dissimulado — licao de FIT-2026-010 |

## 10. Plano de reversao

| Campo | Conteudo |
|---|---|
| Reversivel? | **Sim — Tipo 2** |
| Como | ADR que supere este + ato, restaurando 1.3.0 e 1.2.0 pelo diff **literal e reversivel** de PS-2026-005 §2 |
| Custo | **Baixo.** Nenhum `FIT`, nenhuma Carta e nenhum indice precisa mudar para reverter |
| Copia datada | **137** arquivos, fora do acervo (PI-07, AF-35) |

## 11. Classificacao

| Campo | Valor | Justificativa |
|---|---|---|
| Classe | **C3** | Emenda a **Fundacao** e altera a coluna *Ratifica* — materia de **direitos de decisao** (FND-04 §2). **A missao a classificou C3, e a classificacao e confirmada pela materia** |
| Tipo | **2** | §10 |
| Ratificacao | **EXIGIDA — SOBERANO** | FND-09 §8.2, linha `FND` |
| Instrumento | **RFC → ADR → ratificacao** | [RFC-0013](../rfcs/RFC-0013-harmonizacao-do-regime-do-parecer.md) |
| Fitness Check | **Obrigatorio** | [FIT-2026-011](../governance/fitness/FIT-2026-011-fechamento-de-autoridade.md) |

## 12. Revisao

| Campo | Conteudo |
|---|---|
| Revisor independente | **DEP-QAR** — nao produziu o texto |
| Residuo declarado | **DEP-QAR e autor de todo `FIT`**, logo objeto da linha alterada. **Nao ha ganho nem perda de autoridade para ele**: os dez `FIT` ja declaram `nao-exigida` e `FT-14` preserva o efeito do veredito. O residuo e **de posicao, nao de interesse**, e fica declarado (PI-10) |
| Gatilho de reavaliacao | **Primeiro `FIT` contestado** sob `FT-13` |

## 13. Rastreabilidade

| Campo | Conteudo |
|---|---|
| RFC de origem | [RFC-0013](../rfcs/RFC-0013-harmonizacao-do-regime-do-parecer.md) |
| Achado que fecha | **RD-09** — [MSG-2026-0004 §8](../memory/operacional/MSG-2026-0004-ato-soberano-cartas-emenda-constitucional-e-regime-do-fitness-check.md) |
| Ressalva que fecha | **R1** de [FIT-2026-010](../governance/fitness/FIT-2026-010-aplicacao-do-ato-soberano.md) |
| Achado que **abre** | **RD-12** — FND-04 §2.1 |
| Decisao que este ADR **propaga** | [ADR-0015](ADR-0015-fitness-check-e-parecer-nao-decisao.md), `FT-10` |
| Pacote de decisao | [PS-2026-005](../governance/pacote-soberano-2026-07-29-rd-09.md) |
| Documentos emendados | **FND-09** 1.3.0 → **1.4.0** · **FND-10** 1.2.0 → **1.3.0** |
| Documentos **nao** emendados | FND-01 a FND-08 · as nove Cartas · os dez `FIT` |

## Checklist de validade (FND-07 §4.1)

| # | Item | Estado |
|---|---|---|
| 1 | Problema declarado antes da solucao | ✅ §2 |
| 2 | Alternativas reais, incluindo nao fazer | ✅ §4 — **cinco** |
| 3 | Criterios declarados antes da escolha | ✅ §3 |
| 4 | Impacto medido | ✅ §7 |
| 5 | Evidencia por ID | ✅ §8, com **A1** ausente declarada |
| 6 | Riscos com mitigacao | ✅ §9 |
| 7 | Plano de reversao | ✅ §10 |
| 8 | Classe e tipo justificados | ✅ §11 |
| 9 | Revisor ≠ autor | ✅ §12 |
| 10 | Rastreabilidade fechada | ✅ §13 |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-GOV | Emenda **C3** proposta a **FND-09 §8.2** *(fonte)* e **FND-10 §10.3** *(cascata, CV-04)*, fechando **RD-09**: a linha `Fitness Check` passa de *"Ratifica: SOBERANO se C3"* a **`—`**, com **duas notas normativas** citando `FT-10`, `FT-11` e `FT-14`. **Zero titulares ampliados · zero pareceres convertidos em norma · zero `FIT` historicos editados · zero `FIT` com valor alterado.** Abre **RD-12**: a regra geradora vive em **FND-04 §2.1** e **nao** e corrigida aqui. Nasce em `em-revisao` · `ratificacao: pendente`. |
