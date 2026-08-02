---
id: ADR-0015-fitness-check-e-parecer-nao-decisao
titulo: Formalizar que Fitness Check e Revisao Arquitetural sao pareceres M1 e nao se ratificam
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
decisoes_relacionadas: [ADR-0004, ADR-0006, ADR-0012, ADR-0014]
substitui: []
substituido_por: null
classe_mudanca: C2
tipo_decisao: 2
supera: []
superado_por: null
resumo: Formaliza a determinacao soberana de 2026-07-29 de que Fitness Check e Revisao Arquitetural sao pareceres M1, podem ser acolhidos, contestados ou superados, e nao adquirem autoridade normativa por ratificacao.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# ADR-0015: `Fitness Check` e parecer, nao decisao — e por isso nao se ratifica

## Proposito
Cumprir a determinacao do **item 4** do ato soberano de **2026-07-29**, que ordena registrar e
formalizar, **pelo rito aplicavel**, o entendimento de que `Fitness Check` e `Revisao
Arquitetural` sao **pareceres M1** — acolhiveis, contestaveis e superaveis — e **nao** adquirem
autoridade normativa por ato soberano.

## Escopo
| Item | Definicao |
|---|---|
| Inclui | O **regime** de `FIT` e `REV` quanto a ratificacao; a classificacao dos dois como **parecer**, nao artefato de decisao; e o que decorre disso para o encerramento de mudanca em **QG-6** |
| **Nao** inclui | **A edicao de FND-10 §10.3 e de FND-09 §8.2** — §5.3, e a diferenca mais importante deste ADR · o **merito** de qualquer `FIT` ja emitido · a **edicao retroativa** de `FIT` historicos, **expressamente vedada pelo ato** |
| Origem | **Item 4** do ato soberano de 2026-07-29 · **Q2** de [RFC-0009](../rfcs/RFC-0009-integridade-e-alcance-do-ato-de-ratificacao.md) · texto proposto em [RFC-0011 §5](../rfcs/RFC-0011-emenda-constitucional-ratifica-homologa.md) |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| **Determina** | **SOBERANO** | Item 4 do ato de 2026-07-29. **A materia era escalada e voltou decidida** |
| Registra e formaliza | **DEP-GOV** | Guardiao normativo; LM-05, CV-09 |
| Revisor independente | **DEP-QAR** | AC-03 |
| Aprovador | **SOBERANO**, pela propria determinacao | Nao ha aprovacao departamental a dar sobre materia que o Soberano ja decidiu |
| Ratificador | **Nao aplicavel** | C2/Tipo 2 (FND-04 §2.1). **E este ADR nao se ratifica a si proprio pelo mesmo fundamento que declara** |

> **Residuo declarado (PI-10).** **DEP-QAR e o autor de todo `FIT` do acervo**, e este ADR
> decide o regime dos artefatos que ele produz. A revisao independente **nao lhe retira o
> interesse**: o efeito da decisao e **reduzir** o alcance formal do proprio produto, nao
> amplia-lo. O sentido do interesse esta declarado para que o leitor o pese.

---

## 1. Contexto

**Q2 esta aberta ha dois ciclos.** [FND-10 §2.2](../foundation/10-artifact-framework.md) exige
`ratificacao` de *"todo artefato de **decisao** C3 ou Tipo 1"*; **FND-10 §10.3** atribui a
`Fitness Check` *"Ratifica: SOBERANO se C3"*, tratando a classe do **objeto avaliado** como se
fosse a do parecer. **FND-09 §8.2 reproduz a mesma leitura**, na linha `FIT`.

**Custo ja pago:** [INC-2026-002](../governance/incidents/INC-2026-002-ratificacao-declarada-em-fitness-check.md)
nasceu daqui, e `FIT-2026-001` **continua afirmando no proprio texto** uma ratificacao que nunca
ocorreu — artefato **M1**, nao editavel.

[ADR-0012 §5.5](ADR-0012-integridade-do-ato-de-ratificacao.md) recusou decidir a questao por
rito C2 sozinho: *"retirar materia da mesa do ratificador nao e decisao que o rito C2 deva tomar
sozinho"* (PI-01). **A materia foi escalada, e o ato de 2026-07-29 a devolveu decidida.**

## 2. Problema / Pergunta de decisao

> **`Fitness Check` exige ratificacao do Soberano?** E, se nao exige, **onde essa regra passa a
> viver**, sem que a formalizacao ultrapasse o que o ato autoriza?

## 3. Criterios de decisao

| # | Criterio |
|---|---|
| K1 | Reproduz **literalmente** o que o ato determinou, sem ampliar nem reduzir |
| K2 | **Nao edita** documento fundacional que o ato nao autorizou a editar |
| K3 | **Nao edita retroativamente** nenhum `FIT` — vedacao expressa do ato |
| K4 | Nao cria entidade, tipo documental, camada nem documento fundacional |
| K5 | Deixa **visivel** o que continua divergente, com dono e gatilho |

## 4. Alternativas consideradas

### Alternativa A — Formalizar em ADR e **nao** tocar as fundacionais *(escolhida)*
O ADR carrega a regra; FND-10 §10.3 e FND-09 §8.2 permanecem como estao, com a divergencia
**declarada** e endereçada a um ato futuro. **Precedente exato:**
[ADR-0013](ADR-0013-criterio-de-horizonte-e-consolidacao.md), que formalizou uma determinacao
soberana **sem emendar FND-09 §12**, porque o ato dizia *"nao edita diretamente FND-09"*.

### Alternativa B — Aplicar ja as alteracoes de RFC-0011 §5.2 a FND-10 e a cascata a FND-09
| Campo | Conteudo |
|---|---|
| A favor | Elimina a divergencia na fonte, de uma vez |
| **Contra** | **Falha K2.** Emendar `FND` exige, por [FND-09 §8.2](../foundation/09-meta-model.md) linha `FND`, **aprovacao e ratificacao do SOBERANO**. O ato de 2026-07-29 autorizou expressamente a promulgacao de **FND-01 1.4.0** *(item 3)* e **nao** mencionou FND-10 nem FND-09. Ler autorizacao no silencio e **LM-03** |
| Veredito | **Recusada** |

### Alternativa C — Tratar a determinacao como auto-executavel, sem instrumento
| Campo | Conteudo |
|---|---|
| **Contra** | O ato manda **registrar e formalizar pelo rito**. Determinacao sem instrumento vive so na Diretiva, que tem `ttl` — e expira sem que a regra tenha dono |
| Veredito | **Recusada** — contraria o proprio ato |

### Alternativa Z — Nao fazer nada
Recusada: **descumpre o item 4**, que e determinacao, nao sugestao.

## 5. Decisao

### 5.1 O regime — regras `FT`

| # | Regra |
|---|---|
| **FT-10** | **`Fitness Check` e `Revisao Arquitetural` sao pareceres**, nao artefatos de decisao. A exigencia de `ratificacao` de FND-10 §2.2 alcanca **artefato de decisao** C3 ou Tipo 1, e **nao os alcanca**. |
| **FT-11** | **A ratificacao incide sobre a mudanca avaliada, nunca sobre o parecer que a avalia.** Um `FIT` sobre mudanca C3 **nao** herda a exigencia de ratificacao do objeto que avalia. |
| **FT-12** | **Parecer nao adquire autoridade normativa por ato soberano.** Acolher um `FIT` **nao** o transforma em norma; o que vira norma percorre o rito de FND-04 §6. |
| **FT-13** | **`FIT` pode ser acolhido, contestado ou superado.** Veredito posterior **supera** o anterior (FT-09); nenhum `FIT` e editado para acomodar contestacao (M1, LV-04). |
| **FT-14** | **Veredito `inapto` bloqueia o encerramento em QG-6 sem depender de ato do Soberano.** O efeito do parecer e processual, e independe de ratificacao. |
| **FT-15** | **Nenhum `FIT` historico e editado por esta decisao** — vedacao expressa do ato de 2026-07-29. `FIT-2026-001` permanece com o registro incorreto **contido, nao corrigido**. |

### 5.2 O que muda no campo `ratificacao` de um `FIT` novo

| Antes | Depois |
|---|---|
| `nao-exigida` derivado por leitura, com duvida declarada | `nao-exigida` **por regra**, com fundamento em `FT-10` |

**Nenhum `FIT` do acervo muda de valor.** Os oito emitidos ja declaram `nao-exigida`; o que muda
e **o fundamento**, que deixa de ser inferencia e passa a ser norma.

### 5.3 O que esta decisao **nao** faz — e por que isso e o ponto

| Nao faz | Por que |
|---|---|
| **Nao edita FND-10 §10.3** | Emendar `FND` exige **aprovacao e ratificacao do SOBERANO** (FND-09 §8.2, linha `FND`). O ato autorizou a promulgacao de **FND-01** e **nao** mencionou FND-10 |
| **Nao edita FND-09 §8.2**, linha `FIT` | Mesmo fundamento. A cascata de CV-04 **e devida**, e **nao e autorizada por este ato** |
| Nao edita nenhum `FIT` historico | Vedacao expressa do ato; e M1 (LV-04, FT-09) |
| Nao altera o rito de QG-6 | `FIT` continua obrigatorio em C2 e C3 (CV-07) |
| Nao cria entidade, tipo, camada nem fundacional | `FIT` ja e tipo documental (FND-10 §4) e `FIT` ja e entidade (FND-09 §5) |

> **A divergencia permanece viva, e esta e a informacao mais importante deste ADR.**
> **FND-10 §10.3** e **FND-09 §8.2** continuam dizendo *"Ratifica: SOBERANO se C3"* na linha
> `Fitness Check`. **A regra vigente e `FT-10`; o texto das duas fundacionais diverge dela.**
> Achado **RD-09**, dono **DEP-GOV**, gatilho **proximo ato soberano que alcance FND-09 ou
> FND-10**. **Declarado em vez de corrigido por conta propria** — que e exatamente o que
> ADR-0012 §5.5 mandou nao fazer.

## 6. Justificativa

| # | Fundamento |
|---|---|
| 1 | **A alternativa A e a unica que satisfaz K1 e K2 ao mesmo tempo.** B corrige mais do que o ato autoriza; C formaliza menos do que ele manda |
| 2 | **Reproduz o precedente que ja funcionou.** ADR-0013 formalizou determinacao soberana sem emendar a fundacional que o ato excluiu — e **zero** fundacionais foram emendadas naquela missao |
| 3 | **Fecha a causa de INC-2026-002 no plano normativo**, sem tocar o artefato M1 que a exibe |
| 4 | **O sentido da decisao reduz poder formal, nao amplia.** Um parecer que nao se ratifica alcanca **menos**, nao mais — e por isso o residuo de interesse de DEP-QAR nao a compromete |

## 7. Impacto

| Dimensao | Impacto |
|---|---|
| Documentos fundacionais | **0 emendados** — e **2 declarados divergentes** (§5.3) |
| Entidades · tipos · camadas · templates | **0** criados |
| Artefatos M1 editados | **0** |
| `FIT` que mudam de estado | **0** — os oito ja declaravam `nao-exigida` |
| Regras novas | **6** — `FT-10` a `FT-15` |
| Achados que fecha | **Q2** de RFC-0009 · **G1/G2** de INC-2026-002, **no plano normativo** |
| Achados que abre | **RD-09** — as duas fundacionais divergem da regra vigente |
| Custo de contexto | **+1** artefato `missao`. Nenhum entra no nucleo obrigatorio |

## 8. Evidencias

| # | Evidencia | Fonte |
|---|---|---|
| E1 | **Item 4 do ato de 2026-07-29**, literal: *"Determino que Fitness Checks permanecam pareceres M1... nao sao ratificados nem adquirem autoridade normativa por ato soberano"* | [MSG-2026-0004](../memory/operacional/MSG-2026-0004-ato-soberano-cartas-emenda-constitucional-e-regime-do-fitness-check.md) §1.1 |
| E2 | **FND-10 §2.2 alcanca artefato de decisao; `FIT` e parecer** — `classe_avaliacao`, nao `classe_mudanca` | FND-10 §2.2 e §4 |
| E3 | **A divergencia esta em duas projecoes, nao em uma** — FND-10 §10.3 e FND-09 §8.2 | RFC-0011 §5.1 |
| E4 | **Os oito `FIT` do acervo ja declaram `nao-exigida`** | `governance/fitness/README` |
| **A1** | **Evidencia ausente, declarada:** nenhum `FIT` foi **contestado** ate hoje. `FT-13` autoriza contestacao **sem membro observado** | PI-10 |

## 9. Riscos e mitigacao

| # | Risco | Prob. | Impacto | Mitigacao |
|---|---|---|---|---|
| RF-1 | **A divergencia de §5.3 ser lida como erro deste ADR**, e nao das fundacionais | Media | Medio | §5.3 declara qual regra vige e por que as fundacionais nao foram tocadas. Achado **RD-09** com dono e gatilho |
| RF-2 | *"Parecer nao se ratifica"* virar *"parecer nao vincula"* | Baixa | **Alto** | **`FT-14`**: `inapto` **bloqueia** o encerramento. Nao se ratificar **nao** e nao ter efeito |
| RF-3 | Seis regras novas com exercicio limitado | Media | Baixo | Cinco das seis **descrevem pratica ja observada** em oito `FIT`; so `FT-13` nasce sem membro, e esta declarada em **A1** |
| RF-4 | A cascata devida a FND-09 e FND-10 ser esquecida | **Media** | Medio | **RD-09**, com gatilho no proximo ato que alcance as duas |

## 10. Plano de reversao

| Campo | Conteudo |
|---|---|
| Reversivel? | **Sim — Tipo 2** |
| Como | ADR que supere este, ou nova determinacao do Soberano em sentido contrario |
| Custo | **Documental integral.** Nenhum `FIT` foi editado; nenhuma fundacional foi tocada; nada a desfazer alem deste arquivo |
| O que **nao** se reverte | O ato de 2026-07-29, que e historico |
| Backup (PI-07) | Copia datada de **134** arquivos, tomada antes das edicoes deste ato |

## 11. Classificacao

| Campo | Valor | Justificativa |
|---|---|---|
| Classe | **C2 — estrutural** | Altera um **padrao** de artefato (FND-04 §2). **Nao** altera principio, linha vermelha, hierarquia nem direito de decisao |
| Tipo | **2 — reversivel** | §10 |
| Ratificacao | **Nao exigida** | C2/Tipo 2. **E o proprio `FT-10` explica por que um parecer sobre este ADR tambem nao se ratificaria** |
| Instrumento | **Determinacao soberana → ADR** | Item 4 do ato; texto antecedente em [RFC-0011 §5](../rfcs/RFC-0011-emenda-constitucional-ratifica-homologa.md) |
| Fitness Check | **Obrigatorio** | [FIT-2026-010](../governance/fitness/FIT-2026-010-aplicacao-do-ato-soberano.md) |

## 12. Revisao

| Campo | Conteudo |
|---|---|
| Gatilho | **Primeira contestacao real de um `FIT`** *(exercicio de `FT-13`)*, ou **ato que alcance FND-09/FND-10** *(RD-09)* |
| O que se mede | Se `FT-14` foi exercido — quantos `inapto` bloquearam encerramento; e se a divergencia de §5.3 gerou leitura errada |
| Dono | **DEP-GOV** |

## 13. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Origem | **Item 4** do ato soberano de 2026-07-29 — [MSG-2026-0004](../memory/operacional/MSG-2026-0004-ato-soberano-cartas-emenda-constitucional-e-regime-do-fitness-check.md) |
| Questao que responde | **Q2** de [RFC-0009](../rfcs/RFC-0009-integridade-e-alcance-do-ato-de-ratificacao.md); texto proposto em [RFC-0011 §5.2](../rfcs/RFC-0011-emenda-constitucional-ratifica-homologa.md) |
| Decisao que escalou a materia | [ADR-0012 §5.5](ADR-0012-integridade-do-ato-de-ratificacao.md) |
| Incidente cuja causa trata | [INC-2026-002](../governance/incidents/INC-2026-002-ratificacao-declarada-em-fitness-check.md) — causa tratada **no plano normativo**; o artefato M1 permanece intacto |
| Precedente de forma | [ADR-0013](ADR-0013-criterio-de-horizonte-e-consolidacao.md) — determinacao formalizada **sem emendar a fundacional** |
| Achado que abre | **RD-09** |

---

## Checklist de validade (FND-07 §4.1)
- [x] **VD-01** — 3 alternativas reais (A, B, C) + "nao fazer nada" (Z)
- [x] **VD-02** — criterios K1–K5 em §3, antes de §4
- [x] **VD-03** — nenhuma alternativa de palha: **B e a mais completa**, e foi recusada por ultrapassar o ato
- [x] **VD-04** — tradeoff explicito em §5.3: a divergencia permanece viva
- [x] **VD-05** — evidencia ausente declarada: **A1**
- [x] **VD-06** — plano de reversao em §10
- [x] **VD-07** — impacto em cascata mapeado: **devido e nao autorizado**, achado RD-09
- [x] **VD-08** — data e responsaveis presentes
- [x] **VD-09** — gatilho de revisao em §12
- [x] **Interesse do revisor declarado** — bloco Responsaveis

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-GOV | Formalizacao do **item 4** do ato soberano de 2026-07-29: `Fitness Check` e `Revisao Arquitetural` sao **pareceres M1** e **nao se ratificam** — regras **`FT-10` a `FT-15`**. **Responde Q2 de RFC-0009**, aberta ha dois ciclos, e trata a causa de **INC-2026-002** no plano normativo. **Zero fundacionais emendadas** e **zero `FIT` editados**: a divergencia de **FND-10 §10.3** e **FND-09 §8.2** permanece **declarada, nao corrigida** — achado **RD-09**, porque emendar `FND` exige ato que este nao concede. |
