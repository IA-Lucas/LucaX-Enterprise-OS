---
id: MEM-APR-0005-medir-a-ausencia-na-fonte-errada
titulo: Buscar o termo em vez da funcao produz achado de lacuna onde ha titular declarado
tipo: memoria
versao: 1.0.0
status: ativo
camada_memoria: aprendizado
autor: DEP-KMS
proprietario: DEP-KMS
aprovador: DEP-KMS
criado_em: 2026-07-29
atualizado_em: 2026-07-29
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0020]
substitui: []
substituido_por: null
origem: PT-2026-005 §5.3 e RFC-0016 §2.4
evidencia: RD-22 declarou promulgacao e ativacao sem titular apos varrer FND-09 §8.1, a palavra promulg e FND-10 §5.2/§5.4; o titular estava declarado em FND-04 §4 [7] e FND-07 §5 [10], nao varridos
confianca: alta
ocorrencias: 3
ttl: permanente
aplica_se_a: [global]
resumo: Registra que varredura por termo encontra prosa e nao titular, que a busca deve ser pela funcao, e como distinguir lacuna real de lacuna de metodo antes de escrever o achado.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# Buscar o termo em vez da funcao produz achado de lacuna onde ha titular declarado

## Proposito
Registrar por que **`RD-22`** — achado de severidade **Alta** que bloqueou `GO-TO-SPECS` por
uma missao inteira — declarou ausencia de titular para `promulgacao` e `ativacao` **enquanto o
titular estava literalmente declarado** em duas fontes vigentes, e qual verificacao impede a
repeticao.

## Escopo
Aplica-se a **toda varredura que conclua ausencia** — de titular, de regra, de campo, de
cobertura. **Nao** se aplica a varredura que conclua **presenca**: achar o termo prova que ele
existe; nao achar o termo **nao** prova que a funcao nao esta atribuida.

## Responsaveis
| Papel | Quem |
|---|---|
| Dono | DEP-KMS |
| Quem deve ler | Todo papel que va **afirmar que algo nao existe no acervo** |
| Verificacao da licao | DEP-QAR |

---

## Situacao

O sexto ato soberano exigiu, em MSG-2026-0006 §IX, titulares identificados *"sem interpretacao
informal"* para **dez** atos, entre eles **promulgacao** e **ativacao**.

A apuracao — [PT-2026-005 §5.3](../../governance/relatorio-transicao-2026-07-29-aplicacao.md) —
mediu **quatro coisas**, todas corretamente:

| O que foi medido | Resultado |
|---|---|
| Os cinco verbos de autoridade de **FND-09 §8.1** | `promulgar` **nao** esta entre eles |
| A palavra **`"promulg"`** em `foundation/`, `departments/`, `decisions/` | **3 ocorrencias**, todas em prosa de `ADR` |
| **FND-10 §5.2** `O4` | Declara operacao, transicao, criterio e rollback — nao o ator |
| **FND-10 §5.4** | Declara a condicao de entrada em `ativo` — nao o ator |

Conclusao registrada: *"Nenhuma fonte do acervo declara titular para nenhum dos dois."*
Severidade **Alta**, dono DEP-GOV, instrumento identificado como **RFC → ADR C3 ou ato
soberano**. `GO-TO-SPECS` **nao autorizado**.

## Observado

A conclusao era **falsa**, e a falsidade e verificavel em duas linhas de texto vigente:

| Fonte **nao** varrida | Texto literal |
|---|---|
| **FND-04 §4 `[7]`** | *"REGISTRO — **DEP-GOV** atribui ID definitivo, **publica** ADR, atualiza indices e contadores"* |
| **FND-07 §5 `[10]`** | *"REGISTRO — **DEP-GOV** atribui numero e **publica** o ADR"* |
| **FND-07 §5 `[13]`** | *"**VIGENCIA** — decisao passa a valer e vincula"* — a **unica** das catorze etapas sem ator, porque vigencia e **efeito** |
| **FND-09 §7.5** | *"Entra em vigor · `ativo` · **Publicacao + atualizacao de indice**"* |
| **FND-09 `AU-06`** | *"Instrumento **autoriza**; nao executa (...) quem o cria e o **executor nomeado**"* |
| **FND-04 §3** | Papel **Executor**: *"Aplica a mudanca aprovada, no escopo aprovado"* |

**Vinte declaracoes convergentes em cinco fontes vigentes**, inventariadas em
[RFC-0016 §2.3](../../rfcs/RFC-0016-regime-ministerial-de-promulgacao-e-ativacao.md). O achado
nao mediu nenhuma delas.

## Causa

**O acervo nunca nomeou a etapa como *promulgacao*. Ele a nomeia `REGISTRO`.**

A varredura procurou o **termo** e encontrou prosa. A funcao — *quem publica o que foi
aprovado* — estava atribuida com nome de departamento, em tabela normativa, em dois documentos
fundacionais. **Buscar por termo tem cobertura igual ao vocabulario do buscador**, e o
vocabulario da exigencia (§IX, redigida pelo Soberano) **nao era o vocabulario do acervo**.

A segunda causa e composicional: `promulgar` e `ativar` foram procurados em **FND-09 §8.2**,
que e a matriz de **autoridade sobre a entidade**. Eles nao estao la porque **§8.1 fecha os
verbos de autoridade em cinco** e nenhum deles e promulgar. **A ausencia estava certa; a
inferencia de que ela significava lacuna estava errada** — `AU-09` rege autoridade, e execucao
nao e autoridade.

## Licao

**Antes de escrever que uma atribuicao nao existe, busque pela funcao em pelo menos duas
formulacoes distintas do acervo, e busque no documento que rege o ciclo, nao apenas no que
rege a autoridade.**

Concretamente, para concluir *"X nao tem titular"*:

| # | Verificacao obrigatoria antes do achado |
|---|---|
| V1 | O termo da pergunta e o termo do acervo? Se nao, **qual e o termo do acervo** para a mesma funcao? |
| V2 | A funcao foi procurada no documento de **ciclo** (FND-04 §4, FND-07 §5) e nao somente no de **autoridade** (FND-09 §8.2)? |
| V3 | A funcao foi procurada nas **Cartas**, na secao *artefatos e registros mantidos*, que atribui papel por tipo documental? |
| V4 | Se a ausencia se confirmar: ela e **lacuna** ou e **consequencia de regra** — como uma lista fechada que deliberadamente nao inclui o item? |

**Corolario:** achado de ausencia deve declarar **o que foi varrido**, com o comando ou a secao.
`RD-22` declarou — e e por isso que foi possivel refuta-lo em uma missao em vez de descobrir o
erro anos depois. **Declarar o metodo e o que torna o achado corrigivel.**

## Condicoes

**Aplica-se quando** — as duas, cumulativas:
1. A conclusao e **negativa** (*nao existe*, *nao esta declarado*, *nao ha cobertura*);
2. O vocabulario da pergunta vem de **fora do acervo** — ato soberano, exigencia externa,
   missao redigida em outro registro.

**Nao se aplica quando:** a conclusao e positiva; ou a pergunta usa o vocabulario canonico de
FND-03 §11 e do Canon Semantico de FND-10 §3, em que termo e funcao coincidem por construcao.

**Sinal de que se esta no caso certo:** a varredura por termo devolve **poucas ocorrencias, todas
em prosa**. Foi exatamente o resultado de `RD-22` — **3 ocorrencias, 3 em prosa de ADR** — e ele
deveria ter sido lido como *"o acervo usa outra palavra"*, nao como *"o acervo nao trata disso"*.

## Ocorrencias — **tres, e a familia e a mesma**

| # | Achado | O que a varredura procurou | Onde a resposta estava |
|---|---|---|---|
| 1 | **`RD-23`** | **Afirmacao em prosa** sobre aprovador de Spec | **Valor em frontmatter** de `TPL-spec` — por isso achou **1** artefato e nao **2** |
| 2 | **`RD-26`** | A distribuicao de perfil **reproduzivel das fontes** | O metodo estava prescrito em **FND-10 §2.3** — *padrao por tipo aplicado por referencia no catalogo*; nao foi lido |
| 3 | **`RD-22`** | O **termo** *"promulg"* e a matriz de **autoridade** | A **funcao** *publicar o aprovado*, no documento de **ciclo** |

**As tres tem a mesma forma: a pergunta foi feita no eixo errado da fonte certa.** E a
contraparte negativa de [MEM-APR-0004](MEM-APR-0004-projecao-revela-divergencia-antiga.md) — la,
mudar o eixo **revelou** oito divergencias reais; aqui, nao mudar o eixo **inventou** duas.

## Acao

| # | O que muda | Dono | Instrumento |
|---|---|---|---|
| A1 | Achado de **ausencia** passa a declarar `V1` a `V4` como parte da propria evidencia | DEP-GOV | `G-7` — auditoria documental |
| A2 | A auditoria de coerencia interna passa a cruzar **documento de ciclo** × **documento de autoridade** antes de registrar lacuna de titular | DEP-QAR | FND-04 §8 |
| A3 | `RD-22` e **fechado por refutacao de premissa**, nao por emenda — e o fechamento declara a premissa refutada | DEP-GOV | [ADR-0020](../../decisions/ADR-0020-regime-ministerial-de-promulgacao-e-ativacao.md) |
| A4 | O `FIT` de missao que registre achado de ausencia responde, em **F1**, se `V1` a `V4` foram aplicados | DEP-QAR | FND-09 §10.3 |

## Confianca

**Alta — tres ocorrencias medidas**, `RD-22`, `RD-23` e `RD-26`, todas na mesma missao e todas
com a mesma forma. A licao deixou de ser hipotese no momento em que a segunda ocorrencia teve a
mesma causa da primeira; a terceira a confirma.

**Contraevidencia declarada:** as tres ocorrencias vem de **um unico ciclo de apuracao**, o que
pode significar tanto uma falha de metodo estavel quanto um ciclo especificamente exigente — §IX
foi a primeira vez que o acervo teve de nomear titular **por ato**. **O que distinguiria:** se a
proxima varredura de ausencia, sob `A1`, nao produzir achado refutado, a licao pegou; se
produzir, a causa e mais profunda que o metodo de busca.

## Proveniencia
| Campo | Conteudo |
|---|---|
| Origem | [PT-2026-005 §5.3](../../governance/relatorio-transicao-2026-07-29-aplicacao.md) — o achado; [RFC-0016 §2.4](../../rfcs/RFC-0016-regime-ministerial-de-promulgacao-e-ativacao.md) — a refutacao |
| Detectado por | DEP-GOV, ao mapear a funcao em vez do termo na Missao 1.12.1 |
| Evidencia | **20** declaracoes convergentes em **5** fontes vigentes, contra **3** ocorrencias do termo, todas em prosa |
| Contraevidencia declarada | `RD-22` **nao foi negligente**: declarou o que varreu, e por isso foi refutavel. A falha e de **cobertura de metodo**, nao de zelo |

## Relacionados
| Referencia | Relacao |
|---|---|
| [ADR-0020](../../decisions/ADR-0020-regime-ministerial-de-promulgacao-e-ativacao.md) | Decisao que fecha `RD-22` pela refutacao aqui registrada |
| [RFC-0016](../../rfcs/RFC-0016-regime-ministerial-de-promulgacao-e-ativacao.md) | Proposta com o inventario das 20 declaracoes |
| [MEM-APR-0004](MEM-APR-0004-projecao-revela-divergencia-antiga.md) | **Mesma familia, sentido inverso** — mudar o eixo revela divergencia real |
| [MEM-APR-0002](MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md) | O ponto cego de auditar projecao contra fonte sem auditar a fonte contra si mesma |
| [PT-2026-006](../../governance/relatorio-transicao-2026-07-29-fechamento-operacional.md) | Relatorio da missao que aplicou a licao |
