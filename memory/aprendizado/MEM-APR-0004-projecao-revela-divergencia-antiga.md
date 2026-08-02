---
id: MEM-APR-0004-projecao-revela-divergencia-antiga
titulo: Projetar a mesma fonte por outro eixo revela divergencia que a leitura habitual nao revela
tipo: memoria
versao: 1.0.0
status: ativo
camada_memoria: aprendizado
autor: DEP-KMS
proprietario: DEP-KMS
aprovador: DEP-KMS
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0008, ADR-0011]
substitui: []
substituido_por: null
origem: FIT-2026-005-cartas-de-departamento
evidencia: A projecao Departamento × Capability produziu 8 achados sobre um catalogo lido por Capability em 5 ciclos consecutivos sem que nenhum deles aparecesse
confianca: media
ocorrencias: 1
ttl: permanente
aplica_se_a: [global]
resumo: Registra que pivotar uma fonte ja auditada por um eixo novo encontra divergencia que a leitura habitual nao encontra, e quando vale pagar por isso.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# Projetar a mesma fonte por outro eixo revela divergencia que a leitura habitual nao revela

## Proposito
Registrar por que a primeira projecao Departamento × Capability encontrou **oito** divergencias
em um catalogo que ja havia passado por uma revisao arquitetural dedicada e por cinco ciclos de
auditoria — e sob que condicao vale a pena construir um eixo de leitura novo.

## Escopo
Aplica-se a **toda fonte estruturada consultada sempre pelo mesmo eixo**: o catalogo de
Capabilities, o catalogo mestre, a matriz de autoridade, o registro de aptidao. **Nao** se
aplica a fonte de leitura unica ou sem estrutura tabular, onde nao ha segundo eixo a pivotar.

## Responsaveis
| Papel | Quem |
|---|---|
| Dono | DEP-KMS |
| Quem deve ler | Todo papel que va auditar catalogo, matriz ou registro ja existente |
| Verificacao da licao | DEP-QAR |

---

## Situacao

O catalogo de Capabilities existe desde a Missao 1.2. Ele foi objeto de uma **revisao
arquitetural dedicada** — [REV-CAP](../../capabilities/revisao-arquitetural-2026-07-28.md), com
7 achados — e atravessou **cinco ciclos** de auditoria de integridade referencial e de coerencia
interna.

Em todos esses ciclos, o catalogo foi lido **por Capability**: para cada competencia, quem e o
custodio, quem exerce, de que depende. E o eixo natural, porque e o eixo em que a fonte esta
escrita — o frontmatter de cada Carta `CAP`.

A Missao 1.6 precisou da pergunta **inversa**: *para cada departamento, o que ele custodia e o
que exerce?* Nenhum artefato respondia isso, e responder exigia abrir 23 arquivos.

## Observado

A projecao foi construida **sem alterar uma linha da fonte** — apenas pivotando os mesmos tres
campos (`custodio`, `exercentes`, `depende_de`) por departamento. Ela produziu **oito achados**,
registrados em [`capabilities/README §10.3`](../../capabilities/README.md):

| Achado | O que a projecao mostrou | Por que o eixo antigo nao mostrava |
|---|---|---|
| **P1** | **22 de 23** Capabilities declaram `exercentes` identico ao `custodio` — OW-02 *("custodia nao e exclusividade de exercicio")* tem **um unico membro observado** | Lida uma a uma, cada Carta parece correta: uma lista de exercentes com um elemento nao chama atencao. **So a contagem transversal revela o padrao** |
| **P2 a P5** | Quatro divergencias entre o catalogo e FND-01, FND-02, FND-05 e FND-06 sobre **quem de fato exerce** | Cada divergencia envolve **dois documentos distintos**. O eixo por Capability nunca cruza a Carta com a norma que atribui a atividade |
| **P6** | **VC-03 dispara em 2 de 9 departamentos** — DEP-ENG com 5 vinculos e DEP-EXE com 4 | VC-03 e uma regra **sobre o componente**. Lendo por Capability, o componente nunca e o sujeito da contagem |
| **P7** | O departamento de **menor** custodia detem a Capability de **maior** alcance de verificacao | E uma relacao entre duas colunas que so existem juntas no eixo novo |
| **P8** | Duas duplas mutuamente expostas — **nao** ciclo proibido, mas fronteira a vigiar | O grafo por Capability e aciclico; a exposicao so aparece ao agrupar por custodio |

**Nenhum dos oito e um defeito da fonte.** A fonte esta internamente consistente: nenhuma
Capability tem dois custodios, nenhuma esta sem custodio, o grafo nao tem ciclo. As cinco
verificacoes classicas — OW-01, OW-03, OW-04, OW-05 e PD-01 — **passaram todas**.

## Causa

**Auditar sempre pelo eixo em que a fonte esta escrita verifica a consistencia interna dela, e
so isso.** Divergencia entre a fonte e **outro documento**, ou entre a fonte e uma **regra sobre
o consumidor**, e invisivel nesse eixo — nao por descuido do auditor, mas porque a pergunta
nunca chega a ser feita.

O eixo de leitura determina o conjunto de perguntas possiveis. Cinco ciclos de auditoria
competente pelo mesmo eixo nao equivalem a um ciclo por um eixo novo.

## Licao

**Quando uma fonte estruturada e consultada sempre pelo mesmo eixo, construir a projecao pelo
eixo inverso e um instrumento de auditoria — nao apenas de conveniencia de leitura.**

A projecao foi pedida para **economizar contexto** (responder sem abrir 23 arquivos). O que ela
entregou de mais valioso foi outra coisa: **oito divergencias**. O ganho de auditoria nao estava
no pedido e apareceu de graca, porque pivotar obriga a colocar lado a lado colunas que nunca se
encontram.

**Corolario:** a pergunta a fazer diante de um catalogo estavel nao e apenas *"ele esta
consistente?"*, mas *"por qual eixo ele nunca foi lido, e o que esse eixo perguntaria?"*.

## Condicoes

**Aplica-se quando** — as tres, cumulativas:
1. A fonte e estruturada e tem **ao menos dois eixos** naturais de leitura;
2. Ha um eixo pelo qual ela **nunca foi lida**;
3. Existe **regra vigente cujo sujeito e o outro eixo** — como VC-03, que fala do componente, em
   um catalogo escrito por competencia.

**Nao se aplica quando:** a fonte tem eixo unico; ou o segundo eixo ja e consultado
rotineiramente; ou a projecao exigiria informacao que a fonte nao carrega — nesse caso seria
**criacao** de informacao, nao projecao, e violaria IX-01 e RG-01.

**Sinal de que se esta no caso certo:** uma regra vigente ha varios ciclos nunca teve sua
condicao **contada**. P1 e o caso puro: OW-02 vale desde a Missao 1.2 e ninguem havia contado
quantas vezes ela e exercida.

**Sinal de alarme, do lado oposto:** se a projecao **corrigir** a fonte para caber nela, o
instrumento virou defeito. Em divergencia, prevalece a fonte (PJ-03), e a projecao e que esta
errada.

## Acao

| # | O que muda | Dono | Instrumento |
|---|---|---|---|
| A1 | A projecao Departamento × Capability passa a existir como **fonte unica do pivo por departamento**, com declaracao de PJ-02 | DEP-EXE | `capabilities/README §10` |
| A2 | Os **oito achados** entram com dono e gatilho; **nenhuma** Carta de Capability foi alterada por eles | DEP-QAR | `capabilities/README §10.3` |
| A3 | Na **revisao estrutural**, a auditoria de cobertura de Capabilities passa a incluir a leitura pelo eixo do componente, alem do eixo da competencia | DEP-QAR + DEP-EXE | FND-04 §8, linha "Cobertura de Capabilities" |
| A4 | `PR-1` a `PR-3` fixam que a projecao **nunca** corrige a fonte | DEP-GOV | ADR-0011 §5.5 |

## Confianca

**Media.** Uma unica ocorrencia, e o resultado — oito achados — pode dever-se tanto ao
instrumento quanto ao fato de este ser o **primeiro** consumidor real do catalogo. Um catalogo
sem consumidor acumula divergencia com a norma sem que ela apareca; o primeiro consumidor
encontraria muita coisa **por qualquer eixo**.

**O que distinguiria as duas explicacoes:** aplicar o mesmo pivo ao **catalogo mestre** — por
tipo documental em vez de por artefato — e ver se tambem produz achados. Se produzir, a licao e
sobre o **eixo**; se nao produzir, era sobre o **primeiro consumidor**. Registrado como o teste
que confirmaria ou refutaria esta licao.

## Proveniencia
| Campo | Conteudo |
|---|---|
| Origem | [FIT-2026-005 §Aprendizado](../../governance/fitness/FIT-2026-005-cartas-de-departamento.md) |
| Detectado por | DEP-EXE, ao construir a projecao exigida pela Missao 1.6 |
| Evidencia | 8 achados em `capabilities/README §10.3`, sobre uma fonte com 5 verificacoes classicas **todas conformes** |
| Contraevidencia declarada | Nenhum dos 8 e defeito **da fonte**; sao divergencias com outros documentos ou com regras sobre o consumidor |

## Relacionados
| Referencia | Relacao |
|---|---|
| [ADR-0011](../../decisions/ADR-0011-contrato-de-carta-de-departamento.md) | Decisao que institui a projecao e as regras PR-1 a PR-3 |
| [ADR-0008](../../decisions/ADR-0008-uma-fonte-multiplas-projecoes.md) | Regime de projecao que torna esta leitura licita em vez de duplicacao |
| [MEM-APR-0002](MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md) | **Mesma familia, sentido inverso:** aquela trata do risco de exibir o que e de outro; esta, do ganho de exibir o mesmo por outro eixo. **Terceira confirmacao** de MEM-APR-0002 registrada em FIT-2026-005 F2.b |
| [REV-CAP](../../capabilities/revisao-arquitetural-2026-07-28.md) | Revisao dedicada que auditou o catalogo pelo eixo da competencia |
| [REV-DEPARTAMENTO](../../foundation/revisao-arquitetural-cartas-de-departamento-2026-07-28.md) | Revisao em que a projecao foi verificada |
