---
id: ADR-0019-aprovador-e-ratificador-de-spec
titulo: Emenda C3 a FND-09 §8.2 e FND-10 §10.3 — a Spec passa a ter aprovador e ratificador conforme a classe
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
decisoes_relacionadas: [ADR-0012, ADR-0017]
substitui: []
substituido_por: null
classe_mudanca: C3
tipo_decisao: 2
supera: []
superado_por: null
resumo: Faz as linhas SPC e Spec de FND-09 §8.2 e FND-10 §10.3 remeterem a classe da mudanca em vez de fixar titular, e registra o conflito com FND-04 §2 como erro da propria tabela, sem ampliar titulares.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: ratificada
---

# ADR-0019: Aprovador e ratificador de `Spec` **conforme a classe**

> ## O estado deste ADR e o do seu frontmatter, e nada alem dele
>
> **A fonte corrente do estado e o campo `ratificacao`** (FND-10 §5.4). Enquanto ele disser
> `pendente`, este ADR **nao produz efeito**, e FND-09 permanece em **1.3.0** e FND-10 em
> **1.2.0**, com as linhas `SPC` e `Spec` inalteradas. **Nenhuma frase deste texto afirma
> vigencia** — a licao de **RD-08**, aplicada.

## Proposito
Fechar **RD-15** na fonte: fazer com que **FND-09 §8.2** e **FND-10 §10.3** deixem de dar,
para Spec **C2** e **C3**, aprovador e ratificador diferentes dos de **FND-04 §2**.

## Escopo
| Item | Definicao |
|---|---|
| Inclui | **Quatro** celulas — `SPC` *(Aprova, Ratifica)* em FND-09 §8.2 e `Spec` *(Aprova, Ratifica)* em FND-10 §10.3 — e **duas** notas |
| **Nao** inclui | **RD-14** — [ADR-0018](ADR-0018-liberacao-do-portao-qg-1.md), pacote separado · o **merito das classes** de FND-04 §2, **nao reaberto** · **FND-04 §2.1** *(RD-12)* e **§6** *(RD-18)* · as demais **20** e **24** linhas das matrizes · Cartas · qualquer artefato historico |
| Origem | [RFC-0015](../rfcs/RFC-0015-aprovador-e-ratificador-de-spec.md) |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| Propoe | **DEP-GOV** | FND-09 §8.2, linha `FND` |
| Revisor independente | **DEP-QAR** | RM-06b |
| Aprova e **ratifica** | **SOBERANO** | **C3.** Indelegavel |

---

## 1. Contexto
O **teste de consumo por Specs** encontrou **dois** bloqueios. **RD-14** e do portao;
**RD-15**, tratado aqui, e do artefato. **Os dois sao independentes e nao se ratificam juntos
por necessidade.**

## 2. Problema
**Tres fontes vigentes, tres respostas.**

| Fonte | Aprova uma Spec C2 | Ratifica uma Spec C2 Tipo 1 |
|---|---|---|
| **FND-09 §8.2**, linha `SPC` | **DEP-PRD (QG-1)** | **`—`** |
| **FND-04 §2** | **DEP-EXE** + parecer DEP-GOV | **SOBERANO** |
| **FND-04 §6**, linha *Spec* | classe **C1** → **proprietario + revisor** | **`—`** |

E a **regra de precedencia** de FND-09 §8.2 exige duas coisas: resolver a favor da origem
**e registrar o conflito como erro da propria tabela**. **A segunda nunca foi cumprida.**

## 3. Criterios de decisao

| # | Criterio |
|---|---|
| **K1** | **Corrigir a fonte**, nao apenas invocar a precedencia |
| **K2** | **Nao ampliar titular** — nenhum nome que ja nao esteja em FND-04 §2 |
| **K3** | **Nao reabrir o merito das classes** de FND-04 §2 |
| **K4** | **Cumprir a segunda metade da regra de precedencia**, no proprio documento |
| **K5** | **Separar aprovar artefato de liberar portao** |
| **K6** | **Nao emendar FND-04** — nao foi pedido nem ratificado (LM-03) |

## 4. Alternativas consideradas

### Alternativa A — As celulas **remetem a classe** e a matriz recebe nota de conflito *(escolhida)*
Satisfaz K1 a K6. **Aplica a `SPC` a forma que a linha `ADR` da mesma tabela ja usa** —
`conforme classe` · `SOBERANO se C3 ou Tipo 1`. **Nenhuma forma nova; nenhum nome novo.**

### Alternativa B — Fixar **DEP-EXE** na celula *Aprova*
**Recusada: falha K3 e erra por excesso.** Fixar DEP-EXE tornaria **toda** Spec C2, inclusive
as **C0 e C1**, que sao a maioria e cujo aprovador FND-04 §2 atribui ao **proprietario**.

### Alternativa C — Manter o texto e confiar na **regra de precedencia**
**Recusada: falha K1 e K4.** A precedencia **contem** o conflito; nao o corrige. E a evidencia
e do proprio acervo: **IC-2 ficou contido por quatro ciclos e reapareceu em dois documentos**.
Alem disso, a regra **exige** o registro do erro, que so o texto emendado pode fazer.

### Alternativa D — Emendar **FND-04 §6**, alinhando a classe da Spec ao efeito
**Recusada: falha K6.** Emendar FND-04 **nao foi pedido**. Fica registrado como **RD-18**,
com dono e gatilho — **declarado, nao corrigido em silencio**.

### Alternativa E — Emendar **so FND-09 §8.2**
**Recusada: falha K1 por metade.** FND-10 §10.3 **declara-se projecao** de FND-09 §8.2;
corrigir so a fonte deixaria a projecao contradizendo o documento de que ela diz derivar.

### Alternativa Z — Nao emendar
**Recusada.** Spec **C2 e C3** ficam **sem titular unico de aprovacao**, e o proprio teste de
consumo mostrou que o escalonamento se torna **indeterminado** (PT-2026-002 §4.3).

## 5. Decisao *(depende de ratificacao)*

| # | Conteudo |
|---|---|
| **H1** | Em **FND-09 §8.2**, linha `SPC`: *Aprova* passa de `DEP-PRD (QG-1)` para **`conforme classe (FND-04 §2)`** |
| **H2** | Em **FND-09 §8.2**, linha `SPC`: *Ratifica* passa de `—` para **`SOBERANO se C3 ou Tipo 1`** |
| **H3** | **FND-09 §8.2** recebe **uma nota** que **registra o conflito como erro desta tabela**, cumprindo a segunda metade da propria regra de precedencia, e declara que **aprovar o artefato e liberar o portao sao atos distintos** |
| **H4** | Em **FND-10 §10.3**, linha `Spec`: *Aprova* passa a **`conforme classe`** e *Ratifica* a **`SOBERANO se C3/Tipo 1`**, com **nota de cascata** |
| **H5** | **FND-09 passa a 1.4.0** e **FND-10 a 1.3.0**, com as linhas de historico correspondentes |

**Texto integral das notas e diff literal:** [PS-2026-008 §2](../governance/pacote-soberano-2026-07-29-rd-15.md).

### 5.1 O que esta decisao **nao** faz

| # | Nao faz |
|---|---|
| **H6** | **Nao altera nenhuma classe de FND-04.** §2, §2.1, §2.2 e §6 permanecem **intactas** |
| **H7** | **Nao cria titular novo.** `DEP-EXE`, `DEP-GOV` e `SOBERANO` ja constam de FND-04 §2, origem declarada de FND-09 §8.2 |
| **H8** | **Nao determina quem libera `QG-1`.** O parentese *"(QG-1)"* sai da coluna *Aprova* **porque portao nao e aprovacao**; o liberador e materia de [ADR-0018](ADR-0018-liberacao-do-portao-qg-1.md) |
| **H9** | **Nao toca as outras 20 linhas** de FND-09 §8.2 nem as outras **24** de FND-10 §10.3 |
| **H10** | **Nao emenda Carta alguma** |
| **H11** | **Nao resolve RD-18 nem RD-19** — os dois ficam **declarados**, com dono e gatilho |
| **H12** | **Nao cria regra de classificacao nova.** `W1` a `W6` de RFC-0015 §3.1 sao **leitura das regras existentes**, e **nao entram no texto emendado** |

## 6. Justificativa

**A emenda nao escolhe um titular: ela devolve a pergunta a quem a Constituicao ja mandou
responder.** FND-09 §8.2 declara-se derivada de FND-04 §2 *"sem redefini-las"* — e a linha
`SPC` **redefinia**. Fazer a celula **remeter** em vez de **nomear** e a unica forma de a
tabela cumprir o que ela propria diz ser.

**A prova de que a forma e a certa esta na mesma tabela:** a linha `ADR` ja resolve o mesmo
problema exatamente assim. **A `SPC` era a excecao, nao a novidade.**

**H3 tem valor proprio, independente de H1 e H2.** A regra de precedencia de FND-09 §8.2 tem
duas metades, e **a segunda nunca foi cumprida em nenhum conflito**. Este e o primeiro registro
de erro feito **no documento que erra**.

## 7. Impacto

| Objeto | Efeito | Executado aqui? |
|---|---|---|
| **FND-09 §8.2** | **2 celulas + 1 nota**; 1.3.0 → **1.4.0**; **1.243 → 1.254 linhas** | **Nao — depende de ato** |
| **FND-10 §10.3** | **2 celulas + 1 nota**; 1.2.0 → **1.3.0**; **764 → 771 linhas** | **Nao — depende de ato** |
| **FND-04 §2, §2.1, §2.2, §6** | **ZERO alteradas** | — |
| **Titulares ampliados** | **ZERO** | — |
| **Titulares reduzidos** | **1 materia** — `DEP-PRD` deixa de ser aprovador **unico**; segue aprovando **C0 e C1** | — |
| **Nomes que entram em *Ratifica*** | **1 — `SOBERANO`**, e so para **C3 ou Tipo 1**, ja exigido por **AU-05** | — |
| **`QG-1`** | **Nao determinado aqui.** O parentese sai; o liberador e de ADR-0018 | — |
| **Cartas** | **ZERO alteradas** | — |
| Entidades · tipos · camadas · portoes · departamentos · classes | **0 criados · 0 alterados** | — |
| Custo de contexto | **+18 linhas** somadas, em dois documentos `nucleo` | — |
| **Concorrencia com PS-2026-005** | **Declarada** — achado **RD-19**, com regras `O1` a `O4` | RFC-0015 §7 |

## 8. Evidencias

| # | Evidencia | Valor |
|---|---|---|
| **V1** | Terceira fonte, nao registrada no achado | **FND-04 §6**, linha *Spec*, classe **C1** → **RD-18** |
| **V2** | Padrao ja existente na propria tabela | Linha `ADR` de FND-09 §8.2: `conforme classe (FND-07 §2.4)` · `SOBERANO se C3 ou Tipo 1` |
| **V3** | Padrao ja existente na projecao | Linha `ADR` de FND-10 §10.3: `conforme classe` · `SOBERANO se C3/Tipo 1` |
| **V4** | Segunda metade da precedencia nunca cumprida | **0** conflitos registrados como erro em FND-09 §8.2 desde 1.0.0 |
| **V5** | Escalonamento indeterminado hoje | PT-2026-002 §4.3 — *"Spec C2 ou C3 chega a aprovacao → indeterminado"* |
| **V6** | Contencao nao fecha | **IC-2** contido por **quatro** ciclos e reaparecido em **dois** documentos |
| **V7** | `H-A` do candidato FND-09 1.4.0 | **`4bb00ff9…04ab`** — [PS-2026-008 §3](../governance/pacote-soberano-2026-07-29-rd-15.md) |
| **V8** | `H-A` do candidato FND-10 1.3.0 | **`6012074a…bd25`** — idem |
| **V9** | Terminadores preservados | **FND-10 `CRLF` em 771 de 771 linhas**, conferido byte a byte |

## 9. Riscos e mitigacao

| # | Risco | Mitigacao |
|---|---|---|
| **RS-1** | **DEP-EXE aprova Spec C2 e tambem libera `QG-1`** apos ADR-0018 | **Atos distintos, e a distincao esta escrita.** C2 exige **parecer de DEP-GOV**, que o portao nao exige |
| **RS-2** | **Classificacao vira o novo ponto de ambiguidade** | **FND-04 §2 ja responde:** classificacao pelo proponente, **validada por DEP-GOV**. Nenhuma regra nova |
| **RS-3** | **RD-19** — pacote aplicado sobre base errada | `O1` a `O4` de RFC-0015 §7; o pacote publica a **base medida** com `H-A` integral |
| **RS-4** | Ratificar so a fonte | **Desaconselhado com fundamento** — FND-10 §10.3 declara-se projecao |
| **RS-5** | **RD-18 envelhece** e a classe de Spec segue com duas regras geradoras | Declarado com dono **DEP-GOV** e gatilho *"proxima emenda a FND-04"* |

## 10. Plano de reversao

| Campo | Conteudo |
|---|---|
| **Tipo** | **2 — reversivel** |
| **Como** | ADR que supere este + ato do Soberano, restaurando **FND-09 1.3.0** e **FND-10 1.2.0** pelo diff de [PS-2026-008 §2](../governance/pacote-soberano-2026-07-29-rd-15.md), que e **literal e reversivel** |
| **Custo** | Baixo enquanto **nenhuma Spec C2 ou C3** tiver sido aprovada sob a regra nova |
| **Gatilho** | Evidencia medida de que a remissao a classe produziu indeterminacao maior que a que ela removeu |

## 11. Classificacao

| Campo | Valor |
|---|---|
| Classe | **C3** — altera **direitos de decisao** (FND-04 §2) |
| Tipo | **2** — reversivel |
| Instrumento | **RFC obrigatoria → analise de impacto → ADR → ratificacao do Soberano** |
| Aprovador | **SOBERANO. Indelegavel** |
| Ratificacao | **Sempre** |

## 12. Revisao

| Campo | Conteudo |
|---|---|
| Revisor independente | **DEP-QAR** |
| Autor | **DEP-GOV** — **autor ≠ revisor** (ADR-0005, RM-06b, FT-02) |
| Residuo declarado (PI-10) | **DEP-EXE e DEP-PRD sao areas alcancadas** — um recebe a aprovacao de Spec C2, o outro deixa de ser aprovador unico — e **nenhum dos dois participou da autoria ou da revisao**. **DEP-GOV e area alcancada em H3**, que registra erro de um documento de que DEP-GOV e proprietario: o registro **amplia a exposicao do proprio autor**, e por isso o residuo e **de posicao contraria ao interesse**, declarado e nao suprido |
| Duas alternativas reais + nao fazer nada | **Cinco alternativas e a opcao Z** — FND-01 §7.1.4 satisfeito |

## 13. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Achado que fecha | **RD-15** — [PT-2026-002 §5](../governance/relatorio-transicao-2026-07-29-fechamento.md) |
| Ressalva que fecha | **R2** de [FIT-2026-011](../governance/fitness/FIT-2026-011-fechamento-de-autoridade.md) |
| Bloqueio que remove | **B5** de PT-2026-002 §8 |
| Achados que **abre** | **RD-18** *(FND-04 §6 × §2)* · **RD-19** *(pacotes concorrentes)* |
| RFC de origem | [RFC-0015](../rfcs/RFC-0015-aprovador-e-ratificador-de-spec.md) |
| Pacote de decisao | [PS-2026-008](../governance/pacote-soberano-2026-07-29-rd-15.md) |
| ADR irmao, **materia separada** | [ADR-0018](ADR-0018-liberacao-do-portao-qg-1.md) — RD-14 |
| Pacote **concorrente** sobre os mesmos documentos | [PS-2026-005](../governance/pacote-soberano-2026-07-29-rd-09.md) — celulas **disjuntas**, versoes **colidentes** |
| Regra de integridade | [ADR-0012](ADR-0012-integridade-do-ato-de-ratificacao.md) |
| Licao aplicada | **RD-08** — o bloco de abertura **remete ao frontmatter** |

## Checklist de validade (FND-07 §4.1)

| # | Item | Estado |
|---|---|---|
| 1 | Decisao ja tomada e registrada | ✅ *(candidata — depende de ato)* |
| 2 | ≥2 alternativas reais + "nao fazer nada" | ✅ **5 + Z** |
| 3 | Impacto mapeado | ✅ §7 |
| 4 | Classe declarada e validada por DEP-GOV | ✅ **C3 · Tipo 2** |
| 5 | Revisor de papel distinto | ✅ **DEP-QAR** |
| 6 | Plano de reversao | ✅ §10 |
| 7 | Rastreabilidade fechada | ✅ §13 |
| 8 | Nao edita decisao aprovada | ✅ **ADR-0017 intacto**; PS-2026-005 **nao reaberto** |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-GOV | Emenda **C3** candidata a **FND-09 §8.2** *(fonte)* e **FND-10 §10.3** *(cascata)* que fecha **RD-15**: as linhas **`SPC`** e **`Spec`** passam a **remeter a classe** — `conforme classe (FND-04 §2)` e `SOBERANO se C3 ou Tipo 1` —, **no mesmo padrao que a linha `ADR` das duas tabelas ja usa**, e a matriz de FND-09 recebe nota que **registra o conflito como erro da propria tabela**, cumprindo a **segunda metade da regra de precedencia**, nunca cumprida em nenhum conflito ate hoje. **A medicao encontrou tres fontes onde o achado registrava duas** — FND-04 §6 atribui **C1** a criacao de Spec —, e isso vira o achado **RD-18**. Abre tambem **RD-19**: este pacote e **PS-2026-005** propoem versoes **concorrentes** de FND-09 e FND-10, com celulas **disjuntas** e numeros **colidentes**, resolviveis por **rebase mecanico** (`O1` a `O4`). **Zero titulares ampliados · zero classes de FND-04 alteradas · zero Cartas emendadas · zero artefatos historicos tocados.** **Nao vigora sem ato.** |
