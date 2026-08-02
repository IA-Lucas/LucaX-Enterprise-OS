---
id: FIT-2026-003-consolidacao-baseline
titulo: Aptidao arquitetural da consolidacao da base e da fronteira greenfield/legado
tipo: fitness
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-EXE
proprietario: DEP-QAR
aprovador: DEP-GOV
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0007, ADR-0008]
substitui: []
substituido_por: null
objeto_avaliado: [ADR-0007, ADR-0008, FND-03, FND-09, FND-10, INC-2026-001, INC-2026-002]
classe_mudanca: C2
classe_avaliacao: aptidao
veredito: apto-com-ressalva
resumo: Verifica se a consolidacao da Missao 1.4 deixou a arquitetura mais apta a evoluir; veredito apto-com-ressalva, tres ressalvas.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-GOV
ratificacao: nao-exigida
---

# FIT-2026-003: Consolidacao da base e fronteira greenfield/legado

## Proposito
Verificar se a Missao 1.4 — fronteira, ratificacao, baseline, prevencao de duplicacao,
consistencia, economia de contexto e proveniencia — deixou a arquitetura **mais apta a
evoluir**, e nao apenas mais completa.

## Escopo
| Item | Definicao |
|---|---|
| Objeto avaliado | ADR-0007, ADR-0008 e as emendas em FND-03, FND-09, FND-10, `TPL-documento`, `TPL-fitness-check`, catalogo mestre, INC-2026-001 §11–§12 e INC-2026-002 |
| Estado anterior | **85 artefatos, 18.916 linhas**; FND-10 em `aprovado`; 5 decisoes C3 com ratificacao pendente; 2 ressalvas de duplicacao abertas |
| **Nao** inclui | Corretude estrutural — objeto da [revisao arquitetural](../../foundation/revisao-arquitetural-consolidacao-2026-07-28.md) |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| **Executa** | **DEP-EXE** | FT-02/CV-08: nao produziu nenhum artefato avaliado. **DEP-QAR esta impedido** — propos ADR-0008 |
| Forma | DEP-GOV | |
| Evidencia | DEP-KMS | Medicoes de contexto e de acervo |
| **Aprova** | **DEP-GOV**, como guardiao de forma | DEP-EXE nao pode aprovar o que executou (LV-03). Desvio declarado de FND-10 §10.3 — achado **C5** de REV-CONSOLIDACAO §6.2 |
| Ratifica | **Nao aplicavel** | Objeto avaliado e **C2/Tipo 2**; §10.3 so exige ratificacao para objeto C3 |

> **FT-02 aplicado sem excecao.** O precedente de conflito declarado aberto em FIT-2026-001 e
> encerrado desde FIT-2026-002 e **nao foi invocado**. Onde havia impedimento, o papel mudou.

---

## Sumario

| # | Pergunta | Resposta | Sinal |
|---|---|---|---|
| F1 | Complexidade aumentou sem ganho proporcional? | **Parcialmente** | **+2.402 linhas (12,7%)** contra 2 ressalvas fechadas, 1 incidente encerrado e 5 decisoes ratificadas |
| F2 | Algum conceito foi duplicado? **e** a prevencao foi aplicada? | **Nao · aplicada** | 2 duplicacoes **removidas**, 1 convertida em projecao, 1 barrada antes de escrever |
| F3 | Alguma abstracao ficou desnecessaria? | **Nao** | 0 entidades, 0 tipos, 0 templates, 0 camadas novas |
| F4 | Continua mais simples de evoluir? | **Sim** | Admissao externa: 1 portao. Estado de ratificacao: 1 fonte |
| F5 | Custo de contexto subiu ou desceu? | **Desceu por tarefa, subiu no acervo** | Nucleo **5,1%**; primeira medicao **observada**: **23%** |
| F6 | Favorece reutilizacao? | **Sim** | PJ-01 a PJ-06 e o portao G1–G5 servem a qualquer artefato e a qualquer candidato futuro |

**Veredito:** `apto-com-ressalva` — tres ressalvas, todas com dono e gatilho.

---

## F1 — A complexidade aumentou sem ganho proporcional?

| Medida | Antes | Depois | Variacao |
|---|---|---|---|
| Artefatos | 85 | **93** | **+8** |
| Linhas | 18.916 | **21.318** | **+2.402 (12,7%)** |
| Entidades | 21 | **21** | **0** |
| Tipos documentais | 33 | **33** | **0** |
| Documentos fundacionais | 10 | **10** | **0** |
| Templates | 19 | **19** | **0** — dois emendados, nenhum criado |
| Regras normativas novas | — | **16** *(PJ-01 a PJ-06, FR-01 a FR-10)* | +16 |
| **Regras exercidas nesta missao** | — | **12** *(LM-02 a LM-06, CV-09, CC-01, AC-07, RG-02, RG-03, CE-01, CE-04)* | — |
| Conteudo normativo **removido** por duplicacao | — | **2 blocos** | — |
| Ressalvas **fechadas** | 0 de 7 | **2 de 7** | — |
| Incidentes encerrados | 0 | **1** | — |
| Incidentes abertos | 1 | **1** *(INC-2026-002; o anterior fechou)* | — |
| Decisoes C3 com ratificacao pendente | **5** | **0** | **−5** |
| Arquivos do acervo reescritos | — | **0** | — |
| Arquivos de ADR editados | — | **0** | — |

**Leitura.** O acrescimo de **12,7%** tem contrapartidas verificaveis: cinco decisoes
constitucionais saem de eficacia condicionada, duas ressalvas de missoes anteriores fecham,
dois blocos duplicados desaparecem e nenhuma abstracao nova entra. Pela primeira vez, um ciclo
**fechou** divida em vez de so declarar.

O que **nao** se pode afirmar: que as 16 regras novas sejam a quantidade certa. Dez delas —
FR-01 a FR-10 — nao tem como ser exercidas antes do primeiro candidato do Legacy, que pode
nunca aparecer.

**Resposta:** parcialmente — contrapartida verificavel, proporcao das regras de fronteira nao
comprovada. **→ Ressalva R1.**

## F2 — Algum conceito foi duplicado? E a prevencao foi aplicada?

### F2.a — Ocorrencia

| Conceito | Onde estava | Como a mudanca o trata |
|---|---|---|
| Grafo de estados | FND-03 §5.1 e FND-09 §7.1 | **Removido** de FND-09; referencia a fonte |
| Diretorio por tipo | FND-03 §7 e FND-10 §10.3 | **Removido** de §10.3; §4 declarado projecao |
| Valores dos eixos ortogonais | Cinco fontes e FND-09 §7.3 | **Convertido em projecao declarada** |
| Estado de ratificacao | 4 lugares | **Fonte unica** em INC-2026-001 §11; 3 projecoes declaradas |
| Vocabulario da fronteira | ADR-0007 e FND-03 §8 | Objetos distintos: termo × regra. Sem sobreposicao |

**Nenhuma duplicacao nova foi introduzida.** Verificacao: REV-CONSOLIDACAO §3.

### F2.b — Prevencao

| Verificacao | Evidencia | Resultado |
|---|---|---|
| O autor percorreu cada tabela pelo item de PJ-05? | 75 tabelas nos artefatos novos, percorridas e registradas em REV-CONSOLIDACAO §3.1 | **Sim** |
| Toda exibicao de conteudo de outra fonte declara projecao com as quatro informacoes? | 4 declaracoes: FND-10 §4, FND-10 §10.3, FND-09 §7.3, catalogo §9 | **Sim** |
| Alguma reproducao foi **barrada antes** de ser escrita? | **1** — a matriz FND-10 §10.3 ia receber coluna de proveniencia; virou **RG-06**, que aponta a ADR-0007 §5.5 | **Sim** |
| O teste encontrou algo que a auditoria posterior nao encontrara? | **1** — achado **C4**: FND-09 §7.3 reproduzia valores desde a v1.0.0, atravessou duas auditorias de coerencia interna sem deteccao | **Sim** |

> **Este e o sinal mais forte da missao.** O instrumento novo produziu, na primeira aplicacao,
> um caso barrado **e** um caso descoberto que o instrumento antigo nao achou em duas
> tentativas. E exatamente a hipotese de [MEM-APR-0002](../../memory/aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md),
> confirmada por observacao.

**Resposta:** nao houve duplicacao nova · prevencao **aplicada**, com evidencia.

## F3 — Alguma abstracao ficou desnecessaria?

| Abstracao introduzida | Membros / instancias | Consumidor declarado | Veredito |
|---|---|---|---|
| Tres identidades da fronteira | 3, todas nomeadas; 1 com instancia real *(este sistema)* | FR-01, FND-03 §8 | Justificada — a ausencia de nome e o que produz ambiguidade |
| Portao de admissao G1–G5 | **0 candidatos** | FR-03, FR-06 | **Ociosa hoje, por construcao** |
| 4 classificacoes ADOPT/ADAPT/REWRITE/RETIRE | 0 usos | G3 | Ociosa hoje |
| 5 valores de proveniencia | 1 com membros *(`native`, 93)*; 4 vazios | Catalogo §9 | Justificada — o padrao cobre 100% |
| PJ-01 a PJ-06 | 4 projecoes declaradas, 2 remocoes, 1 barrada | `TPL-documento`, `TPL-fitness-check` | **Justificada e exercida** |
| Baseline `BL-<data>-<NN>` | 1 instancia | RG-07, BL-01 a BL-04 | Justificada com um membro — e a primeira de uma serie por construcao |

**Regra aplicada:** abstracao com menos de dois membros e suspeita (AQ-03).

O portao e as quatro classificacoes **nao tem nenhum membro**, e isso e reconhecido no proprio
ADR-0007 §8 como evidencia ausente. A escolha foi deliberada: a regra existe para chegar
**antes** do caso. Registra-se como divida, nao como acerto.

**Resposta:** nao — nenhuma comprovadamente ociosa por defeito; duas ociosas por antecipacao
deliberada. **→ Ressalva R2.**

## F4 — O sistema continua mais simples de evoluir do que antes?

| Mudanca-tipo | Antes | Depois | Aprovacoes |
|---|---|---|---|
| Saber se um conteudo externo pode entrar | Nao havia regra — decidiria o primeiro caso | 1 portao, 5 condicoes conferiveis | Inalterado |
| Saber o estado de ratificacao de uma decisao | 4 lugares, nenhum declarado fonte | **1 fonte** + projecoes declaradas | Inalterado |
| Saber se uma tabela pode ser copiada | Auditoria, depois de escrita | 1 item de checklist, antes de submeter | Inalterado |
| Saber o estado integro do acervo | Nao havia | 1 baseline com identificador e evidencia | Inalterado |
| Corrigir campo de estado em artefato imutavel | **Impossivel sem violar CC-01** | PJ-04: campo e historico; fonte corrente declarada | Inalterado |
| Encerrar mudanca C2/C3 | Review + Fitness + catalogo | + 1 pergunta em F2 e + 1 recalculo de baseline | **+2 passos** |

**Leitura.** Cinco perguntas antes sem resposta passam a ter uma. O preco sao dois passos a
mais no encerramento, ambos mecanicos. Nenhuma aprovacao nova foi criada — nenhum caminho de
decisao ficou mais longo.

**Resposta:** sim.

## F5 — A mudanca reduz ou aumenta o custo de contexto?

| Papel / tarefa-tipo | Antes | Depois | Direcao |
|---|---|---|---|
| Piso obrigatorio de qualquer tarefa | 5,7% *(calculado)* | **5,1%** *(calculado)* | estavel |
| **Executar uma missao estrutural** | **Indeterminado** | **23% — observado** | **desce, e agora e medido** |
| Descobrir se um artefato e relevante | 1 linha de resumo | 1 linha de resumo | estavel |
| Saber qual pacote carregar por missao | **Nao havia** | 6 pacotes medidos, catalogo §11 | **desce** |
| Acervo total | 18.916 | **21.318** | **sobe 12,7%** |

**Leitura honesta.** O acervo cresceu pela terceira missao consecutiva. O que mudou de
qualidade e a natureza da medicao: pela primeira vez existe um numero **observado**, e nao
apenas a razao entre nucleo declarado e acervo.

**Observacao critica:** uma medicao nao e serie, e a missao medida e atipica — consolidacao
toca mais artefatos que trabalho comum. O numero prova que **e possivel** trabalhar sem
carregar o acervo; nao prova que os perfis estao bem desenhados.

**Resposta:** desce por tarefa, com primeira evidencia observada; sobe no acervo.
**→ Ressalva R3.**

## F6 — Ela favorece reutilizacao?

| Definicao produzida | Reutilizavel por | Especifica do caso? |
|---|---|---|
| PJ-01 a PJ-06 | **Todo artefato com tabela**, presente e futuro | Nao |
| Portao G1–G5 | Toda origem externa — nao so o LucaX Legacy | Nao |
| ADOPT/ADAPT/REWRITE/RETIRE | Toda avaliacao de reuso, inclusive interno | Nao |
| Proveniencia como campo L2 | Todo artefato futuro, sem tocar em nenhum existente | Nao |
| Baseline BL-01 a BL-04 | Todo marco futuro | Nao |
| PJ-04 *(estado em M1)* | Todo campo de estado futuro | Nao |

**Criterio:** DoD-8.

**Evidencia mais forte:** a missao **removeu** conteudo normativo duplicado e **nao criou
nenhum artefato auxiliar, template, entidade ou tipo**. Um ciclo de consolidacao que fecha
mais divida do que abre e a demonstracao do principio que ele institui.

**Resposta:** sim.

---

## Ressalvas

| # | Ressalva | Custo assumido | **Dono** | **Gatilho de reavaliacao** |
|---|---|---|---|---|
| R1 | **Dez regras de fronteira (FR-01 a FR-10) sem nenhuma possibilidade de exercicio hoje** — nao ha candidato, e pode nunca haver | O acervo carrega norma ociosa por tempo indeterminado. Se o Legacy nunca for tocado, ADR-0007 sera custo puro | DEP-EXE | 2a revisao estrutural: sem nenhum candidato submetido, aplicar EV-08 a ADR-0007 e avaliar consolidacao |
| R2 | **Portao e classificacoes com zero membros** — abstracao antecipada, contra AQ-03 | Se o primeiro caso real nao couber em G1–G5, o portao tera de ser refeito **e** a excecao ja tera sido aberta | DEP-GOV | Primeiro candidato do Legacy: verificar se as cinco condicoes bastaram |
| R3 | **Reducao de contexto medida uma unica vez, em missao atipica** — ainda nao ha serie | O numero pode nao representar trabalho comum, e induzir confianca indevida nos perfis | DEP-KMS | Proxima missao: medir de novo e comparar. Duas medicoes formam a primeira serie |

> **R4 de FIT-2026-002 nao e reaberta aqui:** ela permanece **aberta**, com progresso
> registrado. R3 desta verificacao e sua continuidade, nao sua substituta.

## Veredito

| Campo | Conteudo |
|---|---|
| Veredito | **`apto-com-ressalva`** |
| Fundamento | As seis perguntas tem sinal observavel. Duas ressalvas registram antecipacao deliberada de norma sem caso real; uma registra insuficiencia de serie. Nenhuma revela degradacao sem contrapartida, e **pela primeira vez um ciclo fechou mais divida do que abriu** |
| Efeito | **Encerra.** As tres ressalvas viram divida declarada com dono e gatilho (FND-07 §9) |
| Data | 2026-07-28 |
| Executado por | **DEP-EXE** |
| Aprovado por | **DEP-GOV** |
| Ratificado por | **Nao aplicavel** — objeto C2/Tipo 2 |

### Nota sobre FT-04 — vigilancia de complacencia

| Verificacao | Estado |
|---|---|
| Vereditos emitidos | **3** |
| Consecutivos `apto` **sem nenhuma ressalva** | **0** — os tres com ressalvas |
| `inapto` emitidos | **0** |
| Ressalvas anteriores **fechadas** neste ciclo | **2** *(R2 de FIT-2026-001 e R2 de FIT-2026-002)* |

FT-04 exige tres `apto` **sem ressalva** para disparar; nao e o caso. O alarme que
FIT-2026-002 armou — *"se a terceira verificacao tambem terminar em `apto-com-ressalva` sem
que nenhuma ressalva anterior tenha sido fechada, o mecanismo estara produzindo divida em vez
de correcao"* — **nao dispara**: duas ressalvas foram fechadas com evidencia.

Permanece o numero a vigiar: **nenhum `inapto` em tres oportunidades**. Registra-se como
observacao, nao como conclusao.

### Nota de conflito de interesse (PI-10)

| Campo | Conteudo |
|---|---|
| Conflito identificado | DEP-QAR — executor natural do `FIT` — **propos ADR-0008**, um dos objetos avaliados |
| Mitigacao aplicada | A execucao passou a **DEP-EXE**, que nao produziu nenhum objeto avaliado. A aprovacao passou a DEP-GOV, porque DEP-EXE nao pode aprovar o que executou |
| Residuo nao mitigado | DEP-GOV, que aprova, **executou** as emendas em FND-03, FND-09, FND-10 e nos templates. Aprovar o parecer sobre a propria execucao e tensao real, ainda que FND-04 §3.1 nao a proiba nominalmente |
| Consequencia | Registrada como achado **C5** de REV-CONSOLIDACAO §6.2, com dono e gatilho. **Nao se abre precedente:** a proxima ocorrencia deve resolver por regra, nao por deducao |
| Registro | Declarado aqui em vez de omitido (PI-10, LV-05) |

## Aprendizado gerado

| Registro APR | Licao |
|---|---|
| [MEM-APR-0002](../../memory/aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md) | **Confirmada por observacao nesta verificacao.** O teste preventivo barrou um caso e descobriu outro que duas auditorias posteriores nao acharam |
| [MEM-APR-0003](../../memory/aprendizado/MEM-APR-0003-campo-de-estado-em-artefato-imutavel.md) | Gravada nesta missao; exercida imediatamente em INC-2026-002, que **nao** editou os dois `FIT` afetados |
| A gravar por DEP-KMS *(QG-5)* | **Fechar divida e mensuravel; declarar divida nao e.** Tres ciclos declararam ressalvas; o terceiro foi o primeiro a fechar alguma. A metrica que importa nao e quantas ressalvas se registram, e quantas se encerram por ciclo. Acao: o Fitness Check passa a reportar, em FT-04, o numero de ressalvas anteriores fechadas — **ja feito nesta verificacao**, a formalizar na proxima emenda de `TPL-fitness-check`. Dono: DEP-QAR |

## Historico de vereditos sobre este objeto

| FIT | Data | Veredito | Relacao |
|---|---|---|---|
| FIT-2026-003 | 2026-07-28 | `apto-com-ressalva` | Primeiro sobre este objeto |
