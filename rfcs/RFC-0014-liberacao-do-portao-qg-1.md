---
id: RFC-0014
titulo: Quem libera o portao QG-1 — resolver a colisao interna de FND-01 §6.2
tipo: rfc
versao: 1.0.0
status: aprovado
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-GOV
criado_em: 2026-07-29
atualizado_em: 2026-07-29
revisao_prevista: null
decisoes_relacionadas: [ADR-0018]
substitui: []
substituido_por: null
resumo: Propoe fechar RD-14 corrigindo a colisao interna de FND-01 §6.2 — a tabela nomeia DEP-PRD como liberador de QG-1 e a regra imediatamente abaixo proibe que o portao seja liberado por quem produziu o artefato.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# RFC-0014: Quem libera o portao `QG-1`

## Proposito
Levar ao rito o achado **RD-14**: **`QG-1` e liberado por quem produz a Spec**, e isso colide
com a **regra de portao** da propria [FND-01 §6.2](../foundation/01-constituicao.md).

## Escopo
| Item | Definicao |
|---|---|
| Inclui | **Uma** celula de FND-01 §6.2 — a coluna *Quem libera* da linha `QG-1` — e **uma** nota normativa que distingue **liberar portao** de **aprovar artefato** |
| **Nao** inclui | **RD-15**, materia separada — [RFC-0015](RFC-0015-aprovador-e-ratificador-de-spec.md) · os demais **seis** portoes · **FND-02 §2 e §7**, **FND-10 §10.3** e as **nove Cartas**, que sao **cascata declarada e nao emendada** aqui · qualquer Spec — **nenhuma criada** |
| Origem | **RD-14**, aberto por [PT-2026-002 §5](../governance/relatorio-transicao-2026-07-29-fechamento.md); ressalva **R1** de [FIT-2026-011](../governance/fitness/FIT-2026-011-fechamento-de-autoridade.md) |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| Propoe | **DEP-GOV** | FND-09 §8.2, linha `RFC` e linha `FND` |
| Valida forma | **DEP-GOV** | FND-09 §8.2, linha `RFC` |
| Revisor independente | **DEP-QAR** | RM-06b |
| **Decide** | **SOBERANO** | **C3.** Indelegavel (FND-04 §2) |

---

## 1. Contexto

**RD-14 nao foi encontrado por verificacao de conformidade.** As **117** verificacoes de
contrato executadas sobre as nove Cartas na Missao 1.10 passaram; foi a **simulacao do ciclo de
consumo** de [PT-2026-002 §4](../governance/relatorio-transicao-2026-07-29-fechamento.md) — seis
atos encadeados — que expos o bloqueio. **Conformidade e consumo medem coisas diferentes.**

`QG-1` e o **primeiro portao do ciclo de uma Spec**. Enquanto ele nao puder ser liberado
legitimamente, **nenhuma Spec pode existir** — e o Specification Framework nao abre.

## 2. Problema

**A colisao esta dentro de uma unica subsecao, entre duas afirmacoes separadas por sete linhas.**

| Onde | O que diz |
|---|---|
| FND-01 §6.2, tabela, linha `QG-1`, coluna *Quem libera* | **`DEP-PRD`** |
| FND-01 §6.2, **Regra de portao**, logo abaixo da mesma tabela | *"portao nao pode ser liberado por quem produziu o artefato"* |
| FND-09 §8.2, linha `SPC`, coluna *Propoe / cria* | **`DEP-PRD`** |

**O artefato verificado por `QG-1` e a Spec. Quem a produz e DEP-PRD. Quem libera o portao e
DEP-PRD.** A tabela e a regra que a acompanha **nao podem ser as duas verdadeiras**.

## 3. Reconstrucao do fluxo de `QG-1`, ato a ato

Fonte: FND-01 §6.2 e §7.3 · FND-09 §8.2 *(linha `SPC`)* · FND-04 §2 e §6 · `DEP-PRD` §5, §5.2,
§8, §10 · `DEP-ENG` §6.3 e §7 · `DEP-QAR` §8.

| Elemento | Quem / o que | Fundamento | Colide? |
|---|---|---|---|
| **Objeto do portao** | A **Spec** (`SPC`) | FND-01 §6.2, linha `QG-1` | — |
| **Pergunta do portao** | *Define resultado, criterio de aceite e o que esta fora?* | idem | — |
| **Produtor do objeto** | **DEP-PRD** | FND-09 §8.2, linha `SPC`; `DEP-PRD` §8 | — |
| **Revisores do objeto** | **DEP-ENG + DEP-QAR** | FND-09 §8.2; `DEP-PRD` §10, `I-2` | Nao — **nenhum e DEP-PRD** |
| **Liberador do portao** | **DEP-PRD** | FND-01 §6.2; `DEP-PRD` §5 | ❌ **SIM** |
| **Aprovador do artefato** | **DEP-PRD** *(por FND-09 §8.2)* · **conforme classe** *(por FND-04 §2)* | — | ❌ **SIM — mas isso e RD-15** |
| **Veto** | **DEP-QAR**, sobre criterio de aceite nao verificavel | LV-09; FND-02 §6; `DEP-QAR` §8 | Nao — **integro e independente** |
| **Impedimento declarado** | `DEP-PRD` `I-1` *(verificar entrega)*, `I-2` *(revisar a propria Spec)* | `DEP-PRD` §10 | ⚠️ **Nenhum impedimento sobre liberar `QG-1`** |
| **Reconhecimento do fato** | `DEP-PRD` §5.2 — *"`QG-1` e o unico portao que DEP-PRD libera sozinho"* · `RP-1` — **risco** | `DEP-PRD` §10.1 | ⚠️ **Declarado como risco, nunca como colisao normativa** |
| **Excecao formal** | **Nenhuma** — `governance/exceptions/` tem **0** instancias | FND-01 §8.3 | ❌ **Portao liberado contra a regra, sem excecao** |

> ### O que a reconstrucao mostra que o achado nao dizia
> **`DEP-EXE` ja resolveu o mesmo problema para si.** `DEP-EXE §10, I-4` declara impedimento
> para *"liberar `QG-0` sobre pedido que eu mesmo formulei sem registro do motivo"*, com
> substituto nomeado e fundamento **na propria regra de portao de FND-01 §6.2**.
> **`DEP-PRD` nao tem o equivalente** — e a diferenca nao e de redacao de Carta: `DEP-EXE`
> **pode** declarar o impedimento porque a Constituicao **nao o nomeia** como produtor do
> pedido; `DEP-PRD` **nao pode**, porque a Constituicao **o nomeia** como liberador de `QG-1`.
> **A Carta nao consegue corrigir o que a Constituicao determina.**

## 4. Onde ocorre a colisao — determinacao

| Hipotese avaliada | Veredito | Motivo |
|---|---|---|
| A colisao e entre **FND-01 e FND-09** | ❌ **Nao** | FND-09 §8.2 **declara-se derivada** de FND-01 §7.3, FND-04 §2 e §6, *"sem redefini-las"*. Ela **reproduz** o defeito; nao o cria |
| A colisao e entre **FND-01 e a Carta `DEP-PRD`** | ❌ **Nao** | `DEP-PRD` §5 cita **FND-01 §6.2** como fundamento. A Carta **obedece** a fonte |
| A colisao e entre **FND-01 §6.2 e FND-02 §2** | ❌ **Nao** | FND-02 §2 declara `QG-1` entre os itens de que DEP-PRD e *dono unico*. **Ser dono do portao nao e liberar o portao** — a distincao e justamente a que falta |
| **A colisao e interna a FND-01 §6.2** | ✅ **SIM** | A **tabela** e a **regra de portao** que a acompanha, na **mesma subsecao**, dizem coisas incompativeis sobre o mesmo portao |

**Determinacao: a colisao e interna a FND-01 §6.2, e a correcao pertence a FND-01 §6.2.**
Toda outra ocorrencia — FND-02 §2, FND-09 §8.2, FND-10 §10.3, `DEP-PRD`, `DEP-ENG`, `DEP-EXE` —
e **projecao fiel de uma fonte defeituosa** (PJ-02, PJ-03).

### 4.1 Por que **nao** e excecao formal

| # | Fundamento |
|---|---|
| **E1** | A regra de portao e projecao de **PI-05 — Separacao de Poderes**, principio imutavel. FND-01 §8.3 declara: ***"Principios Imutaveis (PI) [...] nao admitem excecao."*** |
| **E2** | Excecao de FND-01 §8.3 tem **prazo de validade** e *"ao fim do prazo [...] o estado regular e restaurado"*. **Nao ha estado regular a restaurar** — o defeito e permanente |
| **E3** | Excecao **preservaria a redacao defeituosa**, que e exatamente o que o mandato desta missao veda |
| **E4** | `LV-03` — *"Aprovar o proprio trabalho"* — **admite** excecao formal; **PI-05 nao**. Uma excecao a LV-03 nao alcanca a colisao, que e com o principio |

## 5. Texto proposto — **uma celula e uma nota**

### 5.1 A celula

```
antes:  | QG-1 | Apos especificar | A spec define resultado, criterio de aceite e o que esta fora? | DEP-PRD |
depois: | QG-1 | Apos especificar | A spec define resultado, criterio de aceite e o que esta fora? | DEP-EXE |
```

### 5.2 A nota, texto integral — inserida apos a **Regra de portao**, antes da nota de `QG-6`

> **Sobre QG-1 e a regra de portao.** `QG-1` verifica a **Spec**, e a Spec e produzida por
> **DEP-PRD** (FND-09 §8.2, linha `SPC`). **Liberar o portao nao e aprovar o artefato:**
> liberar e confirmar que os tres itens exigidos estao presentes e verificaveis por terceiro;
> aprovar o conteudo segue a **classe da mudanca** (FND-04 §2). O liberador de `QG-1` e
> **DEP-EXE**, ja titular da **homologacao** de *escopo e prioridade de produto* em §7.3 e ja
> liberador de `QG-0`. **Nenhum titular novo foi criado** — o nome ja constava de §7.3.
> **DEP-PRD segue decidindo o escopo**, e o veto de **DEP-QAR** sobre criterio de aceite nao
> verificavel permanece integral (LV-09).

## 6. Por que **DEP-EXE**, e nao outro

| Candidato | Veredito | Motivo |
|---|---|---|
| **DEP-EXE** | ✅ **Escolhido** | **Ja e o titular da homologacao de *escopo e prioridade de produto*** em FND-01 §7.3 — a materia exata de que a Spec trata. **Ja libera `QG-0`.** **Nao produz a Spec.** **Zero titulares novos** |
| **DEP-ENG** | ❌ Recusado | `DEP-PRD` §12 veda expressamente: *"**Nunca** a DEP-ENG — quem constroi nao define"*. E `DEP-ENG` e **revisor** da Spec: liberar o portao acumularia revisao e liberacao |
| **DEP-QAR** | ❌ Recusado | Ja e **revisor** da Spec e ja detem `QG-3` e o **veto**. Concentraria revisao, portao e veto no mesmo ator, e `QG-1` verifica **completude de escopo**, nao qualidade de entrega |
| **DEP-GOV** | ❌ Recusado | `QG-1` e portao de **produto**, nao de norma. Nenhuma materia de FND-01 §7.3 atribui escopo de produto a DEP-GOV |
| **SOBERANO** | ❌ Recusado | Transformaria o Soberano em **liberador de portao recorrente**, contra a economia de PI-01 e o proprio mandato |

> **O criterio nao foi escolher um nome novo, e sim descobrir que o nome ja estava escrito.**
> FND-01 §7.3 ja diz, sobre *escopo e prioridade de produto*: **decide DEP-PRD, homologa
> DEP-EXE**. A emenda faz `QG-1` **coincidir com a homologacao que a Constituicao ja previa**.

## 7. A verificacao que importa — isto amplia titular?

| Verificacao | Resultado |
|---|---|
| **Titulares novos criados** | **ZERO** — `DEP-EXE` ja consta de FND-01 §6.2 *(QG-0)* e §7.3 *(cinco materias)* |
| **Materias que mudam de titular** | **1** — a liberacao de `QG-1`, de `DEP-PRD` para `DEP-EXE` |
| **Direitos de decisao de §7.3 alterados** | **ZERO** — **DEP-PRD segue decidindo escopo e prioridade de produto** |
| **Principios imutaveis alterados** | **ZERO** — a emenda **restaura** PI-05, nao o toca |
| **Linhas vermelhas alteradas** | **ZERO** — a emenda **retira** um caso permanente de LV-03 |
| **Veto de DEP-QAR** | **Inalterado** — LV-09 intacto |
| **Niveis de autonomia** | **ZERO** — `DEP-EXE` libera `QG-0` em **A3**; `QG-1` cabe no mesmo nivel sem promocao (AU-03, LV-07) |
| **Outros portoes** | **6 de 7 inalterados** |
| **Excecoes formais criadas** | **ZERO** — `governance/exceptions/` permanece com **0** |
| Custo de contexto | **+10 linhas** em FND-01, que e `nucleo`: **+1 de frontmatter, +1 de celula, +9 de nota e historico** |

## 8. O limite declarado — o que esta RFC **nao** resolve

| Objeto | Estado | Dono | Gatilho |
|---|---|---|---|
| **FND-02 §2** — *"dono unico de [...] portao QG-1"* e o diagrama de §7 | **Cascata nao emendada.** Ser **dono** do portao e compativel com ser **liberado por outro**; a nota de §6.2 basta para desambiguar | DEP-GOV | Proxima emenda a FND-02 — **hoje ha candidato 1.3.0 pendente em PS-2026-004** |
| **`DEP-PRD` §5, §5.2, §8, §10.1 `RP-1`, §12** | **Cascata nao emendada** — Carta **ratificada**, alteravel so por ato (IR-01) | DEP-EXE | **Ato sobre esta emenda**; a Carta e reemitida **depois**, nunca antes |
| **`DEP-ENG` §6.3 e §7** | idem | DEP-EXE | idem |
| **`DEP-EXE` §5 e §6.3** | idem — passa a liberar **dois** portoes | DEP-EXE | idem |
| **RD-15** | **Materia separada, por determinacao** | DEP-GOV | [RFC-0015](RFC-0015-aprovador-e-ratificador-de-spec.md) |

> **A cascata nao e executada aqui, e a razao e normativa, nao de escopo.** As Cartas estao
> **em vigor por ato soberano**; emenda-las antes do ato sobre a fonte seria **alteracao nao
> ratificada** (IR-05) e inverteria a ordem *fonte → projecao* (PJ-03). **Declarar e o
> tratamento correto; executar seria o defeito.**

## 9. Riscos

| # | Risco | Prob. | Impacto | Mitigacao |
|---|---|---|---|---|
| **RR-1** | **`QG-1` vira gargalo em DEP-EXE**, que ja conduz abertura de ciclo e libera `QG-0` | Media | Medio | `QG-1` verifica **presenca e verificabilidade por terceiro** de tres itens, nao merito. `DEP-EXE §10, I-5` **veda** decidir merito — o portao **nao** transfere escopo |
| **RR-2** | **DEP-EXE passa a decidir escopo de produto na pratica**, por via de portao | Media | **Alto** | A nota declara expressamente que **DEP-PRD segue decidindo o escopo**, e `I-5` de `DEP-EXE` ja proibe decidir merito de produto. **Se ocorrer, e violacao verificavel — nao ambiguidade** |
| **RR-3** | **Cascata fica aberta**: fonte emendada, Cartas dizendo o contrario por um ciclo | **Alta** | Baixo | Estado **declarado** em §8, com dono e gatilho. Precedencia resolve: **a fonte prevalece sobre a projecao** (PJ-03) |
| **RR-4** | O ato nao vem, e **RD-14 envelhece** | Media | **Alto** | **Nenhuma Spec pode ser criada ate la** — e o proprio bloqueio e a mitigacao, porque impede que o defeito produza efeito |

## 10. As decisoes possiveis

| # | Decisao | Efeito |
|---|---|---|
| **D1** | **Aprovar e ratificar** — celula e nota | **RD-14 fecha.** `B4` sai do mapa de bloqueios. Cascata em Cartas fica devida |
| **D2** | **Aprovar so a nota**, mantendo `DEP-PRD` na celula | **Recusada com fundamento:** a nota passaria a **descrever** a colisao em vez de resolve-la, e `QG-1` seguiria liberado pelo produtor |
| **D3** | **Devolver** por escolha de titular | Legitimo. **DEP-QAR** e o unico outro candidato que nao produz a Spec; §6 registra por que foi recusado |
| **D4** | **Nao decidir** | **RD-14 permanece.** `QG-1` segue sem liberador legitimo, e **nenhuma Spec pode ser aberta** |

## 11. Manifestacoes

| Area | Manifestacao |
|---|---|
| **DEP-PRD** | **Area alcancada — perde a liberacao de `QG-1`.** `RP-1` da propria Carta ja declarava o arranjo como risco de impacto **Alto** com mitigacao *"assimetrica e declarada como tal"*. **A emenda substitui a mitigacao assimetrica pelo contraditorio previo** |
| **DEP-EXE** | **Area alcancada — recebe a liberacao.** Ja opera o mesmo instituto em `QG-0`, e `I-4` da propria Carta mostra que a regra de portao ja e lida ali |
| **DEP-ENG** | Recebe a Spec **apos** `QG-1`; `HO-02` e `HO-04` de devolucao permanecem |
| **DEP-QAR** | **Veto e `QG-3` inalterados**; segue revisor da Spec |
| **DEP-GOV** | Propoe; **nao aprova nem ratifica** |

## 12. Resultado

| Campo | Conteudo |
|---|---|
| Resultado | **ADR candidato emitido** — [ADR-0018](../decisions/ADR-0018-liberacao-do-portao-qg-1.md) |
| Classe | **C3** *(FND-04 §2 — direitos de decisao e a propria Fundacao)* · **Tipo 2** *(reversivel por emenda revogatoria de mesmo rito)* |
| Estado | **Candidato. Nao vigora sem ato do Soberano** (FND-01 §9) |
| Pacote | [PS-2026-007](../governance/pacote-soberano-2026-07-29-rd-14.md) |
| Achado que fecha | **RD-14** · ressalva **R1** de FIT-2026-011 · bloqueio **B4** de PT-2026-002 §8 |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-GOV | Proposta da **Missao 1.12** para fechar **RD-14**. Reconstroi o fluxo de `QG-1` em **dez elementos** e determina que a colisao e **interna a FND-01 §6.2** — entre a tabela e a regra de portao que a acompanha —, e **nao** entre fundacionais, entre fundacional e Carta, ou com FND-02. Recusa a **excecao formal** por quatro fundamentos, o primeiro deles literal: **PI-05 e principio imutavel e FND-01 §8.3 nao admite excecao a PI**. Propoe **uma celula e uma nota**: liberador de `QG-1` passa a **DEP-EXE**, ja titular da **homologacao de escopo e prioridade de produto** em §7.3 e ja liberador de `QG-0` — **zero titulares novos**. Declara a **cascata nao executada** em FND-02, FND-10 e tres Cartas, com dono e gatilho, e o motivo normativo de nao executa-la. |
