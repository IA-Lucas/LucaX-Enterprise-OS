---
id: RFC-0013-harmonizacao-do-regime-do-parecer
titulo: Harmonizacao de FND-09 §8.2 e FND-10 §10.3 ao regime do parecer fixado em FT-10
tipo: rfc
versao: 1.0.0
status: aprovado
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-GOV
criado_em: 2026-07-29
atualizado_em: 2026-07-29
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0012, ADR-0015]
substitui: []
substituido_por: null
resumo: Propoe alinhar a linha Fitness Check de FND-09 §8.2 e de FND-10 §10.3 a regra vigente FT-10, sem ampliar titulares e sem converter parecer em norma.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# RFC-0013: Harmonizar duas fundacionais ao regime do parecer

## Proposito
Fechar **RD-09**. Duas fundacionais em vigor continuam declarando *"Ratifica: SOBERANO se C3"*
para `Fitness Check`, e a regra vigente — **`FT-10`** de
[ADR-0015](../decisions/ADR-0015-fitness-check-e-parecer-nao-decisao.md) — diz o contrario.

Esta RFC **nao decide** e **nao edita**: entrega o texto que o rito **C3** exige.

## Escopo
| Item | Definicao |
|---|---|
| Inclui | **Uma** celula de **FND-09 §8.2** *(linha `FIT`, coluna Ratifica)* · **uma** celula de **FND-10 §10.3** *(linha `Fitness Check`, coluna Ratifica)* · **duas** notas normativas |
| **Nao** inclui | O **merito** de `FT-10`, ja decidido em ADR-0015 · `Revisao Arquitetural`, que **ja declara `—`** · qualquer outra linha das duas matrizes · **FND-04 §2.1** *(§6 — limite declarado)* · nenhum `FIT` historico *(`FT-15`)* · **FND-02 §4** *(objeto de [RFC-0012](RFC-0012-semantica-da-matriz-de-interacao.md), pacote separado)* |
| Metodo | Diff medido por ferramenta sobre a fonte, nesta missao |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| Propoe | **DEP-GOV** | Dono de RD-09; FND-09 §8.2, linha `FND` |
| Revisor independente | **DEP-QAR** | RM-06b |
| Decide | **SOBERANO** | **C3.** Indelegavel. **Nao ocorreu** |

---

## 1. Contexto

| Marco | O que ficou |
|---|---|
| Ato soberano de **2026-07-29**, item 4 | *"Fitness Checks permanecem pareceres M1 ... nao sao ratificados"*, com determinacao de **formalizar pelo rito aplicavel** |
| **ADR-0015** | Formaliza em **`FT-10` a `FT-15`**. **Nao edita** FND-09 nem FND-10 — *"o ato nao as menciona"*, e ler autorizacao no silencio seria **LM-03** |
| **RD-09** | A divergencia **declarada em vez de corrigida**. R1 de FIT-2026-010, dono DEP-GOV, gatilho *"proximo ato soberano que alcance FND-09 ou FND-10"* |

> **Este e o gatilho.** A missao consome ato soberano expresso e traz a materia ao rito — sem
> presumir que o ato de ontem alcance o texto de hoje.

## 2. Problema

| Fonte | Linha | Declara hoje | Regra vigente |
|---|---|---|---|
| **FND-09 §8.2** | `FIT` | Ratifica: **SOBERANO se C3** | **`FT-10`** — parecer **nao** se ratifica |
| **FND-10 §10.3** | `Fitness Check` | Ratifica: **SOBERANO se C3** | idem |

**Dez `FIT` emitidos declaram `ratificacao: nao-exigida`.** Nenhum foi ratificado, e a pratica
nunca seguiu o texto — o defeito e de **redacao da fonte**, nao de conduta.

## 3. A relacao entre as duas — fonte e projecao

**FND-10 §10.3 declara-se projecao de FND-09 §8.2:**

> *"As colunas **Aprova** e **Ratifica** sao projecao de FND-09 §8.2; em conflito, prevalece a
> fonte (§6.1, PJ-03)."*

| Documento | Papel | Natureza da alteracao |
|---|---|---|
| **FND-09 §8.2** | **FONTE** | Alteracao **substantiva** |
| **FND-10 §10.3** | **PROJECAO** | **Cascata** (CV-04) — devida pela mesma mudanca |

> **A cascata ja estava declarada como devida** em [ADR-0015 §5.3](../decisions/ADR-0015-fitness-check-e-parecer-nao-decisao.md):
> *"A cascata de CV-04 e devida, e nao e autorizada por este ato."* **Esta RFC pede a autorizacao.**

## 4. Texto proposto — **duas celulas e duas notas**

Diff literal em [PS-2026-005 §2](../governance/pacote-soberano-2026-07-29-rd-09.md).

| # | Local | Antes | Depois |
|---|---|---|---|
| **H1** | **FND-09 §8.2**, linha `FIT`, coluna *Ratifica* | `SOBERANO se C3` | **`—` *(`FT-10`)*** |
| **H2** | **FND-09 §8.2**, apos a matriz | *(inexistente)* | Nota de **6 linhas**: parecer nao se ratifica (`FT-10`); a ratificacao incide sobre a mudanca avaliada (`FT-11`); o efeito de `inapto` e processual (`FT-14`); **nenhum titular ampliado** |
| **H3** | **FND-10 §10.3**, linha `Fitness Check`, coluna *Ratifica* | `SOBERANO se C3` | **`—` *(`FT-10`)*** |
| **H4** | **FND-10 §10.3**, apos a matriz | *(inexistente)* | Nota de **5 linhas**: declara a relacao **fonte → cascata** e registra que `Revisao Arquitetural` **ja** declarava `—` e nao muda |

**Mais, em cada arquivo:** `versao`, `atualizado_em`, `decisoes_relacionadas` e a linha de
historico que a promulgacao obriga (AL-04).

| Arquivo | De → Para | Linhas | Blocos de diff |
|---|---|---|---|
| **FND-09** | 1.3.0 → **1.4.0** | **1.243 → 1.252** *(+9)* | **6** |
| **FND-10** | 1.2.0 → **1.3.0** | **764 → 771** *(+7)* | **6** |

## 5. A verificacao que importa — **isto amplia titular?**

| Verificacao | Resposta | Evidencia |
|---|---|---|
| Algum titular **entra** na coluna *Ratifica*? | **NAO — zero** | Nenhuma linha ganha titular. **Uma materia sai da mesa do ratificador; nenhuma entra** |
| Algum parecer vira **norma**? | **NAO** | **`FT-12`** ja proibe: acolher um `FIT` nao o transforma em norma |
| Algum `FIT` historico e editado? | **NAO — zero** | **`FT-15`**, vedacao expressa do ato de 2026-07-29 |
| Algum `FIT` muda de valor no campo `ratificacao`? | **NAO** | Os **dez** ja declaram `nao-exigida`. Muda o **fundamento**, nao o valor |
| O veredito `inapto` perde efeito? | **NAO** | **`FT-14`** — o efeito e **processual** e independe de ato |
| `Revisao Arquitetural` e tocada? | **NAO** | Ja declara `—` em FND-10 §10.3, e **nao consta** de FND-09 §8.2 |

> **O sentido do movimento e o ponto.** [ADR-0012 §5.5](../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md)
> registrou que *"retirar materia da mesa do ratificador nao e decisao que o rito C2 deva tomar
> sozinho"*. **Esta RFC nao a toma sozinha: leva ao C3.** E por isso que uma correcao de duas
> celulas percorre o rito mais caro do sistema.

## 6. O limite declarado — o que esta RFC **nao** resolve

**De onde veio o texto errado?** FND-09 §8.2 declara-se derivada de FND-01 §7.3, FND-04 §2 e §6
*"sem redefini-las"*. A celula `FIT · Ratifica · SOBERANO se C3` e **aplicacao da regra geral de
FND-04 §2.1** — *toda mudanca C3 exige ratificacao* — a uma entidade que **nao e artefato de
decisao**.

| Questao | Estado | Onde vive |
|---|---|---|
| **FND-04 §2.1 deveria distinguir artefato de decisao de parecer?** | **NAO resolvida aqui** | **Achado RD-12**, novo. Dono **DEP-GOV**; gatilho *"proxima emenda a FND-04"* |

> **Corrigir a projecao sem tocar a regra que a gerou deixa o mecanismo vivo** — e e exatamente
> a licao que FIT-2026-010 gravou ao ver IC-2 fechar em FND-01 e **reaparecer** em FND-09 e
> FND-10. **A licao esta aplicada aqui na forma de achado declarado, nao de correcao
> silenciosa:** emendar FND-04 **nao foi pedido, nao foi ratificado e nao sera presumido.**

## 7. Riscos

| # | Risco | Prob. | Impacto | Mitigacao |
|---|---|---|---|---|
| **RS-1** | Ler a alteracao como *"parecer perdeu forca"* | **Media** | Medio | **`FT-14`** citado **na propria nota** de FND-09: `inapto` bloqueia QG-6 sem depender de ato |
| **RS-2** | O mecanismo que gerou o defeito sobrevive em FND-04 §2.1 | **Media** | Medio | **RD-12** declarado em §6, com dono e gatilho — **nao fechado por renomeacao** |
| **RS-3** | Emendar duas fundacionais no mesmo ato de RD-02 confunde os objetos | Baixa | Medio | **Pacotes separados** — PS-2026-004 e PS-2026-005 —, por determinacao da missao |

## 8. As decisoes possiveis

| # | Decisao | Estado que produz |
|---|---|---|
| **D1** | **Ratificar ADR-0017** e promulgar FND-09 **1.4.0** e FND-10 **1.3.0** | **RD-09 fechado na fonte.** R1 de FIT-2026-010 fecha |
| **D2** | Ratificar **so FND-09** *(fonte)* | Fonte corrigida e **projecao divergente** — pior que o estado atual, porque FND-10 passaria a contradizer FND-09 declarando-se projecao dela |
| **D3** | **Devolver** ou **nao decidir** | RD-09 envelhece. **`FT-10` prevalece** e as duas fundacionais seguem desatualizadas |

**Recomendacao: D1.** **D2 e desaconselhada com fundamento**, e nao apenas nao recomendada.

## 9. Manifestacoes

| Area | Manifestacao |
|---|---|
| **DEP-GOV** *(propoe)* | Favoravel. Dono do achado |
| **DEP-QAR** *(revisa)* | **Revisao independente executada.** DEP-QAR e **autor de todo `FIT`** e, portanto, **objeto da linha alterada**. O que muda para DEP-QAR e **nada**: os dez `FIT` ja declaram `nao-exigida`, e `FT-14` preserva integralmente o efeito do veredito. **Nenhum ganho e nenhuma perda de autoridade** |
| **DEP-EXE** | Continua **aprovando** `FIT` (coluna *Aprova* inalterada) |
| **SOBERANO** | **Perde** uma materia da coluna *Ratifica* — por determinacao propria do ato de 2026-07-29, item 4 |

## 10. Resultado

| Campo | Conteudo |
|---|---|
| Estado | **`aprovado`** — forma validada por DEP-GOV |
| Instrumento seguinte | [**ADR-0017**](../decisions/ADR-0017-harmonizacao-do-regime-do-parecer.md) — candidato **C3**, sem vigencia |
| Pacote de decisao | [**PS-2026-005**](../governance/pacote-soberano-2026-07-29-rd-09.md) — **separado de RD-02** |
| Achado que fecha, **se ratificada** | **RD-09** |
| Achado **novo** | **RD-12** — FND-04 §2.1 nao distingue parecer de artefato de decisao |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-GOV | Propoe a emenda **C3** que fecha **RD-09**: **duas celulas** — `FIT` em FND-09 §8.2 e `Fitness Check` em FND-10 §10.3 — passam de *"SOBERANO se C3"* a **`—`**, com **duas notas normativas** que citam `FT-10`, `FT-11` e `FT-14`. Declara a relacao **fonte × cascata** entre os dois documentos e verifica, item a item, que **nenhum titular e ampliado, nenhum parecer vira norma e nenhum `FIT` historico e editado**. Declara o limite: a regra que **gerou** o defeito vive em **FND-04 §2.1** e **nao** e corrigida aqui — achado **RD-12**, com dono e gatilho. |
