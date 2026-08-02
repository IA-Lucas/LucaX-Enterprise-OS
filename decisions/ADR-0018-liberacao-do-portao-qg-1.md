---
id: ADR-0018-liberacao-do-portao-qg-1
titulo: Emenda C3 a FND-01 §6.2 — o portao QG-1 passa a ser liberado por DEP-EXE
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
decisoes_relacionadas: [ADR-0012, ADR-0014]
substitui: []
substituido_por: null
classe_mudanca: C3
tipo_decisao: 2
supera: []
superado_por: null
resumo: Resolve a colisao interna de FND-01 §6.2 fazendo o portao QG-1 ser liberado por DEP-EXE, ja titular da homologacao de escopo de produto em §7.3, e acrescenta nota que distingue liberar portao de aprovar artefato.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: ratificada
---

# ADR-0018: O portao `QG-1` e liberado por `DEP-EXE`

> ## O estado deste ADR e o do seu frontmatter, e nada alem dele
>
> **A fonte corrente do estado e o campo `ratificacao`** (FND-10 §5.4). Enquanto ele disser
> `pendente`, este ADR **nao produz efeito**, e FND-01 permanece em **1.4.0** com `QG-1`
> liberado por `DEP-PRD`. **Nenhuma frase deste texto afirma vigencia** — a licao de **RD-08**,
> aplicada.

## Proposito
Fechar **RD-14** na fonte: fazer com que a **tabela de portoes** de FND-01 §6.2 deixe de
contradizer a **regra de portao** escrita sete linhas abaixo dela.

## Escopo
| Item | Definicao |
|---|---|
| Inclui | **Uma** celula — `QG-1`, coluna *Quem libera* — e **uma** nota normativa em FND-01 §6.2 |
| **Nao** inclui | **RD-15** — [ADR-0019](ADR-0019-aprovador-e-ratificador-de-spec.md), pacote separado · os outros **seis** portoes · **FND-02 §2 e §7**, **FND-09 §8.2**, **FND-10 §10.3** e as **nove Cartas**, cascata **declarada e nao emendada** · `ADR-0014` e qualquer artefato historico *(M1, LV-04)* |
| Origem | [RFC-0014](../rfcs/RFC-0014-liberacao-do-portao-qg-1.md) |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| Propoe | **DEP-GOV** | FND-09 §8.2, linha `FND` |
| Revisor independente | **DEP-QAR** | RM-06b |
| Aprova e **ratifica** | **SOBERANO** | **C3.** Indelegavel |

---

## 1. Contexto
O **teste de consumo por Specs** de [PT-2026-002 §4](../governance/relatorio-transicao-2026-07-29-fechamento.md)
simulou o ciclo completo de uma `SPC` contra as fontes vigentes e encontrou **dois** bloqueios
que **117 verificacoes de contrato** nao encontraram. Este ADR trata do primeiro: **RD-14**.

## 2. Problema
**FND-01 §6.2 contradiz a si propria.** A tabela nomeia **`DEP-PRD`** como liberador de `QG-1`;
a **Regra de portao**, na mesma subsecao, determina que *"portao nao pode ser liberado por quem
produziu o artefato"*. **O artefato e a Spec e quem a produz e `DEP-PRD`** (FND-09 §8.2).

**Nao existe excecao formal registrada:** `governance/exceptions/` tem **0** instancias.

## 3. Criterios de decisao

| # | Criterio |
|---|---|
| **K1** | **Corrigir a fonte**, nao conter o efeito nem descrever o defeito |
| **K2** | **Nao criar titular novo** — nenhum nome que ja nao esteja em FND-01 |
| **K3** | **Nao alterar direito de decisao de §7.3** — DEP-PRD segue decidindo escopo |
| **K4** | **Nao criar excecao formal** — PI-05 nao a admite (FND-01 §8.3) |
| **K5** | **Preservar o veto de DEP-QAR** integralmente (LV-09) |
| **K6** | **Nao emendar Carta em vigor** antes do ato sobre a fonte (IR-01, PJ-03) |

## 4. Alternativas consideradas

### Alternativa A — Passar a liberacao de `QG-1` para **DEP-EXE** *(escolhida)*
Satisfaz K1 a K6. **DEP-EXE ja e o homologador de *escopo e prioridade de produto*** em
FND-01 §7.3 e **ja libera `QG-0`**. **Zero titulares novos.**

### Alternativa B — Passar a liberacao para **DEP-QAR**
**Recusada: falha K2 por concentracao.** DEP-QAR ja e **revisor** da Spec, detem **`QG-3`** e o
**veto**. Acumular o primeiro portao criaria o inverso do problema — um unico ator com revisao,
dois portoes e veto sobre o mesmo objeto. E `QG-1` verifica **completude de escopo**, materia
que FND-01 §7.3 **nao** atribui a DEP-QAR.

### Alternativa C — Passar a liberacao para **DEP-ENG**
**Recusada: vedada por Carta em vigor.** `DEP-PRD §12` determina, sobre o destino de `QG-1`:
*"**Nunca** a DEP-ENG — quem constroi nao define"*. E DEP-ENG e **revisor** da Spec.

### Alternativa D — **Excecao formal** de FND-01 §8.3, autorizando DEP-PRD a liberar o proprio portao
**Recusada: juridicamente impossivel e vedada pelo mandato.** A regra de portao projeta
**PI-05**, e FND-01 §8.3 declara que ***Principios Imutaveis nao admitem excecao***. Alem
disso, excecao tem **prazo** e restaura um *"estado regular"* que **nao existe** aqui, e
**preservaria a redacao defeituosa**.

### Alternativa E — Emendar **FND-09 §8.2** em vez de FND-01 §6.2
**Recusada: falha K1.** FND-09 §8.2 **declara-se derivada** de FND-01 *"sem redefini-las"*.
Corrigir a projecao e deixar a fonte defeituosa e **exatamente o mecanismo que RD-12 nomeou**
e que IC-2 demonstrou: contido em FND-01, **reapareceu** em FND-09 e FND-10.

### Alternativa Z — Nao emendar
**Recusada.** `QG-1` e o **primeiro portao do ciclo de Spec**. Sem liberador legitimo,
**nenhuma Spec pode ser aberta**, e o Specification Framework nao abre.

## 5. Decisao *(depende de ratificacao)*

| # | Conteudo |
|---|---|
| **G1** | Em **FND-01 §6.2**, a coluna *Quem libera* da linha **`QG-1`** passa de **`DEP-PRD`** para **`DEP-EXE`** |
| **G2** | FND-01 §6.2 recebe **uma nota normativa**, apos a *Regra de portao* e antes da nota de `QG-6`, que declara: **liberar portao nao e aprovar artefato**; que liberar e **confirmar presenca e verificabilidade por terceiro** dos tres itens; que aprovar segue a **classe da mudanca** (FND-04 §2); que **DEP-PRD segue decidindo o escopo**; e que o **veto de DEP-QAR permanece integral** |
| **G3** | **FND-01 passa a 1.5.0**, com a linha de historico correspondente |

**Texto integral da nota e diff literal:** [PS-2026-007 §2](../governance/pacote-soberano-2026-07-29-rd-14.md).

### 5.1 O que esta decisao **nao** faz

| # | Nao faz |
|---|---|
| **G4** | **Nao altera nenhum direito de decisao de FND-01 §7.3.** *Escopo e prioridade de produto* continua: **decide DEP-PRD**, homologa DEP-EXE |
| **G5** | **Nao cria titular novo.** `DEP-EXE` ja consta de §6.2 *(QG-0)* e de **cinco** materias de §7.3 |
| **G6** | **Nao toca os outros seis portoes** |
| **G7** | **Nao emenda FND-02, FND-09, FND-10 nem Carta alguma.** A cascata e **declarada** em §7, com dono e gatilho |
| **G8** | **Nao cria excecao formal.** `governance/exceptions/` segue com **0** |
| **G9** | **Nao decide RD-15.** Aprovador e ratificador de Spec sao materia de [ADR-0019](ADR-0019-aprovador-e-ratificador-de-spec.md) |
| **G10** | **Nao altera nivel de autonomia.** `DEP-EXE` libera `QG-0` em **A3**; `QG-1` cabe no mesmo nivel (AU-03, LV-07) |

## 6. Justificativa

**A emenda nao inventa um arranjo: ela faz o portao coincidir com a homologacao que a
Constituicao ja previa.** FND-01 §7.3 declara, para *escopo e prioridade de produto*:
**decide DEP-PRD, homologa DEP-EXE**. `QG-1` pergunta se o escopo esta definido — e a
homologacao do escopo ja tinha titular escrito. **O defeito era a tabela de §6.2 nomear o
decisor onde cabia o homologador.**

**A distincao de G2 e o que impede a emenda de virar transferencia de poder.** Sem ela,
"liberar `QG-1`" poderia ser lido como "aprovar a Spec", e `DEP-EXE` passaria a decidir escopo
— resultado que **RR-2 de RFC-0014** nomeia e que `DEP-EXE §10, I-5` ja proibe.

## 7. Impacto

| Objeto | Efeito | Executado aqui? |
|---|---|---|
| **FND-01 §6.2** | **1 celula + 1 nota**; 1.4.0 → **1.5.0**; **475 → 485 linhas** | **Nao — depende de ato** |
| FND-02 §2 *(dono unico)* e §7 *(diagrama)* | **Cascata.** Ser **dono** do portao permanece compativel com ser **liberado por outro** | **Nao — declarado.** Dono DEP-GOV; gatilho: proxima emenda a FND-02 |
| FND-09 §8.2 *(linha `SPC`)* e FND-10 §10.3 *(linha `Spec`)* | O parentese *"(QG-1)"* na coluna *Aprova* fica **obsoleto** | **Nao — resolvido por [ADR-0019](ADR-0019-aprovador-e-ratificador-de-spec.md)**, que remove o parentese ao corrigir RD-15 |
| `DEP-PRD` §5, §5.2, §8, §10.1 `RP-1`, §12 | Perde a liberacao; `RP-1` deixa de ter objeto | **Nao — Carta ratificada** (IR-01). Dono DEP-EXE; gatilho: **ato sobre esta emenda** |
| `DEP-EXE` §5, §6.3, §10 `I-4` | Passa a liberar **dois** portoes; `I-4` ganha analogo para `QG-1` | idem |
| `DEP-ENG` §6.3 e §7 | Referencia a *"liberacao de QG-1"* muda de emissor | idem |
| **Direitos de decisao de §7.3** | **ZERO alterados** | — |
| **Principios imutaveis · linhas vermelhas · hierarquia normativa** | **ZERO alterados** — PI-05 e **restaurado**, LV-03 **deixa de ter caso permanente** | — |
| Entidades · tipos · camadas · **portoes** · departamentos · classes | **0 criados · 0 removidos** — **7 portoes antes, 7 depois** | — |
| Custo de contexto | **+10 linhas** em FND-01, perfil `nucleo` | — |

## 8. Evidencias

| # | Evidencia | Valor |
|---|---|---|
| **V1** | Colisao **interna** a §6.2 | Tabela linha `QG-1` × *Regra de portao*, **7 linhas** de distancia |
| **V2** | Produtor da Spec | FND-09 §8.2, linha `SPC`, coluna *Propoe / cria*: **DEP-PRD** |
| **V3** | Excecoes formais no acervo | **0** — `governance/exceptions/` |
| **V4** | Reconhecimento previo do fato, sem nomear a colisao | `DEP-PRD §5.2` e `RP-1` — **risco**, impacto **Alto**, mitigacao *"assimetrica"* |
| **V5** | Precedente de leitura correta da regra de portao | `DEP-EXE §10, I-4` — impedimento para autoliberar `QG-0` |
| **V6** | Titular ja existente para a materia | FND-01 §7.3, *escopo e prioridade de produto*: **homologa DEP-EXE** |
| **V7** | Veto vedado a DEP-ENG | `DEP-PRD §12` — *"Nunca a DEP-ENG"* |
| **V8** | Achado nao detectavel por conformidade | **117** verificacoes de contrato passaram; **1** simulacao de seis atos encontrou |
| **V9** | `H-A` do candidato FND-01 1.5.0 | **`2d962616…310d`** — [PS-2026-007 §3](../governance/pacote-soberano-2026-07-29-rd-14.md) |

## 9. Riscos e mitigacao

| # | Risco | Mitigacao |
|---|---|---|
| **RS-1** | `QG-1` vira **gargalo** em DEP-EXE | O portao verifica **presenca e verificabilidade**, nao merito; `DEP-EXE I-5` veda decidir merito |
| **RS-2** | DEP-EXE passa a **decidir escopo** por via de portao | **G2** declara o contrario de forma expressa; violacao vira **verificavel**, nao ambigua |
| **RS-3** | **Cascata aberta** por um ciclo — fonte emendada, Cartas divergentes | Declarada em §7 com dono e gatilho; **PJ-03**: a fonte prevalece sobre a projecao |
| **RS-4** | Ato nao vem | **Nenhuma Spec pode ser aberta** — o bloqueio impede o defeito de produzir efeito |

## 10. Plano de reversao

| Campo | Conteudo |
|---|---|
| **Tipo** | **2 — reversivel** |
| **Como** | ADR que supere este + ato do Soberano, restaurando FND-01 **1.4.0** pelo diff de [PS-2026-007 §2](../governance/pacote-soberano-2026-07-29-rd-14.md), que e **literal e reversivel** |
| **Custo** | Baixo enquanto **nenhuma Spec** tiver sido liberada sob a regra nova |
| **Gatilho** | Evidencia medida de que `QG-1` virou gargalo ou de que o escopo passou a ser decidido por DEP-EXE |

## 11. Classificacao

| Campo | Valor |
|---|---|
| Classe | **C3** — altera **direito de decisao** e a **propria Fundacao** (FND-04 §2) |
| Tipo | **2** — reversivel por emenda revogatoria de mesmo rito |
| Instrumento | **RFC obrigatoria → analise de impacto → ADR → ratificacao do Soberano** (FND-04 §2, C3) |
| Aprovador | **SOBERANO. Indelegavel** |
| Ratificacao | **Sempre** (FND-04 §2.1) |

## 12. Revisao

| Campo | Conteudo |
|---|---|
| Revisor independente | **DEP-QAR** |
| Autor | **DEP-GOV** — **autor ≠ revisor** (ADR-0005, RM-06b, FT-02) |
| Residuo declarado (PI-10) | **DEP-EXE e area alcancada** — recebe a liberacao do portao — **e nao participou da revisao nem da autoria**. **DEP-PRD e area alcancada** — perde a liberacao — e **tambem nao participou**; a Carta `DEP-PRD`, escrita por DEP-EXE, ja declarava o arranjo como risco de impacto **Alto** |
| Duas alternativas reais + nao fazer nada | **Cinco alternativas e a opcao Z** — FND-01 §7.1.4 satisfeito |

## 13. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Achado que fecha | **RD-14** — [PT-2026-002 §5](../governance/relatorio-transicao-2026-07-29-fechamento.md) |
| Ressalva que fecha | **R1** de [FIT-2026-011](../governance/fitness/FIT-2026-011-fechamento-de-autoridade.md) |
| Bloqueio que remove | **B4** de PT-2026-002 §8 |
| RFC de origem | [RFC-0014](../rfcs/RFC-0014-liberacao-do-portao-qg-1.md) |
| Pacote de decisao | [PS-2026-007](../governance/pacote-soberano-2026-07-29-rd-14.md) |
| ADR irmao, **materia separada** | [ADR-0019](ADR-0019-aprovador-e-ratificador-de-spec.md) — RD-15 |
| Regra de integridade | [ADR-0012](ADR-0012-integridade-do-ato-de-ratificacao.md), `IR-01` a `IR-10` |
| Licao aplicada | **RD-08** — o bloco de abertura **remete ao frontmatter** e nao afirma vigencia |
| Emenda constitucional anterior | [ADR-0014](ADR-0014-candidato-emenda-fnd-01-7-3-homologa.md) — **nao editada, nao superada** |

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
| 8 | Nao edita decisao aprovada | ✅ **ADR-0014 intacto** (LV-04) |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-GOV | Emenda **C3** candidata a **FND-01 §6.2** que fecha **RD-14**: a coluna *Quem libera* de **`QG-1`** passa de `DEP-PRD` para **`DEP-EXE`**, e a subsecao recebe **uma nota normativa** que distingue **liberar portao** de **aprovar artefato**. A colisao e **interna a §6.2** — tabela contra a regra de portao escrita **sete linhas abaixo** —, e a correcao pertence a fonte. **Excecao formal recusada por impossibilidade juridica:** a regra de portao projeta **PI-05**, e FND-01 §8.3 declara que **Principios Imutaveis nao admitem excecao**. **Zero titulares novos** — `DEP-EXE` ja e o homologador de *escopo e prioridade de produto* em §7.3 e ja libera `QG-0`. **Zero direitos de decisao de §7.3 alterados**, **zero portoes criados ou removidos**, **zero excecoes formais**, **zero Cartas emendadas** — a cascata em FND-02, FND-09, FND-10 e tres Cartas e **declarada com dono e gatilho**, e o motivo de nao executa-la e normativo (IR-01, PJ-03). **Nao vigora sem ato** (FND-01 §9). |
