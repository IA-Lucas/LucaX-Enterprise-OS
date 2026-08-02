---
id: FIT-2026-004-conhecimento-do-soberano
titulo: Aptidao arquitetural do Contrato de Conhecimento sobre o Soberano e do fechamento de C13
tipo: fitness
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-QAR
proprietario: DEP-QAR
aprovador: DEP-EXE
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0009, ADR-0010]
substitui: []
substituido_por: null
objeto_avaliado: [ADR-0009, ADR-0010, FND-03, FND-06, FND-10, MEM-EST-0001]
classe_mudanca: C2
classe_avaliacao: aptidao
veredito: apto-com-ressalva
resumo: Verifica se a Missao 1.5 deixou a arquitetura mais apta a evoluir; veredito apto-com-ressalva, quatro ressalvas.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-GOV
ratificacao: nao-exigida
---

# FIT-2026-004: Conhecimento sobre o Soberano e fechamento de C13

## Proposito
Verificar se a Missao 1.5 — contrato sobre o Soberano, registro canonico e fechamento de C13 —
deixou a arquitetura **mais apta a evoluir**, e nao apenas mais completa.

## Escopo
| Item | Definicao |
|---|---|
| Objeto avaliado | ADR-0009, ADR-0010, MEM-EST-0001 e as emendas em FND-03, FND-06 e FND-10 |
| Estado anterior | **93 artefatos, 21.318 linhas**; C13 aberto; camada EST com **zero** registros; 8 ressalvas de aptidao abertas |
| **Nao** inclui | Corretude estrutural — objeto da [revisao arquitetural](../../foundation/revisao-arquitetural-conhecimento-do-soberano-2026-07-28.md) |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| **Executa** | **DEP-QAR** | FT-02/CV-08 — **nao produziu nenhum artefato avaliado**. Nenhum desvio necessario |
| Forma | DEP-GOV | |
| Evidencia | DEP-KMS | Medicoes de acervo e de pacote |
| **Aprova** | **DEP-EXE** | [FND-10 §10.3](../../foundation/10-artifact-framework.md), matriz normal |
| Ratifica | **Nao aplicavel** | Objeto avaliado e **C2/Tipo 2**; §10.3 so exige ratificacao para objeto C3 |

> **A matriz de autoridade operou sem folga nesta missao.** O achado **C5** de
> REV-CONSOLIDACAO registrou impedimento cruzado na Missao 1.4 e perguntou se ele era
> estrutural. Esta verificacao e evidencia de que era **situacional**: com o produtor fora de
> DEP-QAR, executor e aprovador voltaram aos papeis previstos.

---

## Sumario

| # | Pergunta | Resposta | Sinal |
|---|---|---|---|
| F1 | Complexidade aumentou sem ganho proporcional? | **Parcialmente** | **+2.424 linhas (11,4%)** e **32 regras novas**, das quais **17 exercidas**; contra 1 achado fechado e 1 lacuna estrutural coberta |
| F2 | Algum conceito foi duplicado? **e** a prevencao foi aplicada? | **Nao · aplicada** | 133 tabelas percorridas; **1 reproducao barrada antes da escrita**; **3** contagens divergentes corrigidas |
| F3 | Alguma abstracao ficou desnecessaria? | **Sim, tres — por antecipacao deliberada** | Classe `inferred`: **0 membros**. Classe 4 de autoridade: **0 membros**. Quatro pacotes: **0 consumidores** |
| F4 | Continua mais simples de evoluir? | **Sim** | Quatro perguntas antes sem resposta passam a ter uma; **nenhuma aprovacao nova** criada |
| F5 | Custo de contexto subiu ou desceu? | **Subiu** — no acervo **e** na missao medida | Segunda medicao observada: **23% → 33%**. So desce onde antes nao havia fonte |
| F6 | Favorece reutilizacao? | **Sim, com uma excecao** | AC-08 a AC-11 e CT-06/CT-14 servem a qualquer artefato; CT-15 e especifica |

**Veredito:** `apto-com-ressalva` — **quatro** ressalvas, todas com dono e gatilho.

---

## F1 — A complexidade aumentou sem ganho proporcional?

| Medida | Antes | Depois | Variacao |
|---|---|---|---|
| Artefatos | 93 | **100** | **+7** |
| Linhas | 21.318 | **23.742** | **+2.424 (11,4%)** |
| Entidades | 21 | **21** | **0** |
| Arquetipos · relacoes · tipos documentais | 4 · 10 · 33 | **4 · 10 · 33** | **0** |
| Documentos fundacionais | 10 | **10** | **0** |
| Camadas de memoria | 5 | **5** | **0** |
| Templates | 19 | **19** | **0** — nenhum criado, nenhum emendado |
| Regras normativas novas | — | **32** *(AC-08 a AC-11, CT-01 a CT-28)* | +32 |
| **Regras novas exercidas nesta missao** | — | **17** | — |
| Regras **preexistentes** exercidas | — | **15** | — |
| Registros na camada EST | 0 | **1** | +1 |
| Achados de revisao **fechados** | — | **1** *(C13)* | — |
| Ressalvas de aptidao **fechadas** | — | **0** | — |
| Arquivos do acervo reescritos por retroatividade | — | **0** | — |
| Arquivos de ADR editados | — | **0** | — |

**As 17 regras novas exercidas:** `AC-08` *(cinco artefatos)* · `AC-09` *(indices atualizados
sem disparar a obrigacao)* · `AC-10` *(duas revisoes M1 identificadas como fora de alcance)* ·
`AC-11` *(uma alteracao nao versionada sanada)* · `CT-05` · `CT-06` *(45 afirmacoes)* ·
`CT-07` *(11 lacunas)* · `CT-11` *(duas fontes externas declaradas)* · `CT-14` *(uma reproducao
barrada)* · `CT-15` *(varredura, zero ocorrencias)* · `CT-21` · `CT-22` · `CT-23` · `CT-24` ·
`CT-25` · `CT-26` · `CT-28`.

**As 15 nao exercidas:** `CT-01` a `CT-04`, `CT-08` a `CT-10`, `CT-12`, `CT-13`, `CT-16` a
`CT-20`, `CT-27`. **Todas dependem de algo que nao existe**: um consumidor, uma segunda
afirmacao, uma tentativa de uso indevido a barrar, um conflito real.

**Leitura.** O acrescimo tem contrapartida verificavel: um achado de revisao aberto desde a
missao anterior **fecha**; a camada EST — vazia desde a fundacao — recebe seu primeiro
registro; e a lacuna que produziu [INC-2026-001](../incidents/INC-2026-001-ratificacao-inferida.md)
passa a ter instrumento. **O que nao se pode afirmar** e que 32 regras sejam a quantidade
certa: quase metade nao tem como ser exercida antes do primeiro componente.

**Resposta:** parcialmente. **→ Ressalva R1.**

## F2 — Algum conceito foi duplicado? E a prevencao foi aplicada?

### F2.a — Ocorrencia

| Conceito | Risco | Como a mudanca o trata |
|---|---|---|
| Escala de sensibilidade | Tres valores proprios ao lado dos quatro de FND-10 §2.2 | **Barrado antes da escrita.** Virou **CT-14**, que reusa a escala vigente e declara o mapeamento |
| Principios, valores, DoD e portoes | Poderiam ser listados no registro sobre o Soberano | **Referenciados por secao**, nunca reproduzidos (CT-05) |
| Regras de evolucao do contrato | Poderiam ser repetidas no registro | §6 do registro **remete** a ADR-0010 §5.6 |
| Equivalencia `Fundador` = `SOBERANO` | Ja resolvida em duas fontes | AF-02 referencia; nao redefine |
| Regime de conhecimento sobre o Soberano | Tres indices poderiam repeti-lo | Os tres **remetem** a ADR-0010 §5 |

**Nenhuma duplicacao nova introduzida.** Verificacao: [REV-SOBERANO §3](../../foundation/revisao-arquitetural-conhecimento-do-soberano-2026-07-28.md).

### F2.b — Prevencao *(PJ-06)*

| Verificacao | Evidencia | Resultado |
|---|---|---|
| O autor percorreu cada tabela pelo item de PJ-05? | **133 tabelas** nos sete artefatos novos, contadas por ferramenta e registradas em REV-SOBERANO §3.1 | **Sim** |
| Toda exibicao de conteudo de outra fonte declara projecao? | **2** declaracoes: ADR-0009 §3 e ADR-0010 §3–§4, ambas nomeando a RFC de origem | **Sim** |
| Alguma reproducao foi **barrada antes** de ser escrita? | **1** — a escala de sensibilidade, convertida em CT-14 | **Sim** |
| O teste encontrou algo que a auditoria posterior nao encontraria? | **1**, de familia vizinha — achado **D8**: dois numeros afirmados divergiam da tabela que os sustenta, corrigidos **antes da submissao** | **Sim** |

> **Segunda confirmacao observada de [MEM-APR-0002](../../memory/aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md).**
> Na Missao 1.4 o teste preventivo barrou um caso e descobriu outro. Aqui repete-se o padrao,
> e o achado D8 amplia o alcance da licao: **afirmacao derivada que deixa de conferir com a
> tabela que a sustenta** e da mesma familia da reproducao — muda o objeto, nao o mecanismo.

**Resposta:** nao houve duplicacao nova · prevencao **aplicada**, com evidencia.

## F3 — Alguma abstracao ficou desnecessaria?

| Abstracao introduzida | Membros | Consumidor declarado | Veredito |
|---|---|---|---|
| Classe `stated` | **31** afirmacoes | CT-06 | Justificada |
| Classe `observed` | **3** afirmacoes | CT-06 | Justificada — no limite de AQ-03 |
| Classe **`inferred`** | **0** | CT-08 | **Ociosa hoje, por construcao** |
| Classe `unknown` | **11** afirmacoes | CT-07 | Justificada, e a mais exercida |
| Classe 1 de autoridade — ato soberano | **1** *(o ato de 2026-07-28)* | CT-12 | Justificada com um membro; e a classe que nomeia o defeito de INC-2026-001 |
| Classe 2 — decisao via rito | **10** ADRs | CT-12 | Justificada |
| Classe 3 — preferencia operacional | **34** afirmacoes | CT-12 | Justificada |
| Classe **4 — hipotese** | **0** | CT-08, CT-12 | **Ociosa hoje** |
| Quatro pacotes de contexto | 4 definidos, **0 consumidores reais** | CT-21 a CT-24 | **Ociosos hoje** |
| Lista fechada CT-15 | 8 itens, **0 ocorrencias barradas** | CT-15 | Ociosa **e desejavelmente ociosa**: zero ocorrencias e o resultado bom |
| AC-08 a AC-11 | **5** artefatos alcancados + 2 M1 identificados | FND-10 §2.5 | **Justificada e exercida** |

**Regra aplicada:** abstracao com menos de dois membros e suspeita (AQ-03).

**Tres abstracoes tem zero membros**, e a razao de cada uma difere. `inferred` e a classe 4 sao
**vazias por escolha correta**: a missao proibiu preencher lacuna por inferencia, e o registro
obedeceu — a existencia da classe e o que torna a proibicao verificavel, mas o custo de
carrega-la vazia e real. Os quatro pacotes sao vazios porque **nao ha componente que os
consuma**, e nao havera antes da proxima fase.

**Resposta:** sim, tres — todas por antecipacao deliberada, nenhuma por defeito.
**→ Ressalva R2.**

## F4 — O sistema continua mais simples de evoluir do que antes?

| Mudanca-tipo | Antes | Depois | Aprovacoes |
|---|---|---|---|
| Saber se um artefato antigo deve declarar os 5 campos | **Duvida aberta**, registrada como C13 | 1 regra binaria, conferivel no Historico de versoes | Inalterado |
| Saber o que o Soberano considera qualidade | Disperso em evidencias de ADR e secoes de incidente | 1 registro, com fonte por afirmacao | Inalterado |
| Saber o que **nao** se sabe sobre o Soberano | **Impossivel** — a ausencia nao estava em lugar nenhum | 11 lacunas nomeadas, cada uma com gatilho | Inalterado |
| Distinguir ato soberano de preferencia | **Ambiguo** — foi a causa de INC-2026-001 | 4 classes, com efeito e expiracao declarados | Inalterado |
| Registrar conhecimento sobre pessoa | Sem regra; nada impedia registrar o que nao devia | Lista fechada de 8 proibicoes | Inalterado |
| Encerrar mudanca C2/C3 | Review + Fitness + catalogo + baseline + varredura C11 | + medir os pacotes que a missao usou | **+1 passo** |

**Leitura.** Cinco perguntas antes sem resposta passam a ter uma. O preco e um passo mecanico a
mais no encerramento. **Nenhuma aprovacao nova foi criada** — nenhum caminho de decisao ficou
mais longo, e nenhum papel ganhou poder de veto novo.

**Resposta:** sim.

## F5 — A mudanca reduz ou aumenta o custo de contexto?

| Papel / tarefa-tipo | Antes | Depois | Direcao |
|---|---|---|---|
| Piso obrigatorio de qualquer tarefa | 1.093 linhas *(5,1%)* | **1.099 linhas (4,6%)** | sobe em linhas, desce em proporcao |
| **Executar uma missao estrutural** | **23%** — uma medicao | **33%** — segunda medicao | **SOBE** |
| Consultar o criterio do Soberano | **Nao havia fonte** — inferia-se | **P1 = 28 linhas** | desce, a partir do indefinido |
| Decidir C2/C3 com criterio do Soberano | Nao havia | **P2 = 52 linhas** | — |
| Acervo total | 21.318 | **23.742** | **sobe 11,4%** |

**Leitura honesta — o numero piorou.** A segunda medicao observada de uma missao executada deu
**33%**, contra 23% na Missao 1.4. **A serie que se acabou de formar aponta para cima**, e
seria desonesto apresenta-la de outro modo.

Duas ressalvas a leitura, ambas declaradas e nenhuma delas uma desculpa suficiente:
**(a)** as duas missoes tem naturezas distintas — consolidacao contra construcao sobre os dez
documentos fundacionais; **(b)** o denominador cresceu, o que **atenua** a proporcao em vez de
agrava-la, de modo que o numerador subiu ainda mais do que a razao sugere.

**O que de fato melhorou** e local e verificavel: consultar o criterio do Soberano deixou de
custar *"ler o acervo e inferir"* e passou a custar **28 linhas**. Isso nao compensa o
agregado — apenas mostra onde o mecanismo funciona.

**Resposta:** **subiu**, no acervo e na missao medida. **→ Ressalva R3.**

## F6 — Ela favorece reutilizacao?

| Definicao produzida | Reutilizavel por | Especifica do caso? |
|---|---|---|
| AC-08 a AC-11 | **Todo artefato do acervo**, presente e futuro | Nao |
| CT-06 — proveniencia por afirmacao | Qualquer registro de memoria, em qualquer camada | Nao |
| CT-14 — escala unica de sensibilidade | Qualquer eixo que ja tenha vocabulario vigente | Nao |
| Quatro classes de autoridade | Qualquer ator com autoridade, nao so o Soberano | Nao |
| Pacotes de contexto por recorte de secoes | Qualquer artefato grande — e o mesmo mecanismo do nucleo por recorte | Nao |
| CT-25 — fato duravel × estado de missao | Toda escrita em memoria | Nao |
| **CT-15 — lista fechada de conteudo proibido** | Conhecimento sobre pessoas | **Sim, parcialmente** |

**Criterio:** DoD-8.

**Evidencia mais forte:** a missao **nao criou** template, entidade, tipo documental, camada
nem documento fundacional, e resolveu um achado aberto reusando um sinal que ja existia — a
linha do Historico de versoes. **A abstracao que ela mais deliberadamente recusou criar
(FND-11) tem gatilho de reabertura declarado**, o que converte a recusa em decisao revisavel em
vez de posicao fixa.

**Resposta:** sim, com uma excecao declarada.

---

## Ressalvas

| # | Ressalva | Custo assumido | **Dono** | **Gatilho de reavaliacao** |
|---|---|---|---|---|
| **R1** | **32 regras novas; 15 sem nenhuma possibilidade de exercicio hoje** — dependem de consumidor, segunda afirmacao ou conflito real, nenhum dos quais existe | O acervo carrega norma ociosa por tempo indeterminado. E a **terceira** vez que um ciclo institui regime preventivo inteiro (FR-01 a FR-10, PJ-01 a PJ-06, agora CT) | DEP-EXE | **Segunda missao sob o contrato:** medir quantas das 28 regras `CT` foram exercidas. Menos de um terco abre proposta de consolidacao (EV-08) |
| **R2** | **Tres abstracoes com zero membros** — classe `inferred`, classe 4 de autoridade e os quatro pacotes de contexto | Se o primeiro consumidor real nao couber nos pacotes, eles terao de ser refeitos **depois** de ja terem sido declarados. `inferred` e a classe 4 podem nunca ganhar membro — e, nesse caso, terao custado sem nunca terem servido | DEP-GOV | **Primeiro componente criado** — verificar se os pacotes servem a um consumidor que nao seja a propria execucao de missao |
| **R3** | **Quarta missao consecutiva de crescimento**, primeira em que **nenhuma ressalva anterior foi fechada**, e primeira em que o **custo de contexto medido subiu** — de 23% para 33% | A divida declarada acumula, e a unica metrica observada de PI-14 aponta na direcao errada. FIT-2026-003 fechou duas ressalvas; este fecha zero | DEP-EXE | **Proxima mudanca C2/C3:** terceira medicao. Se tambem subir, a serie deixa de ser ruido e vira tendencia — aplicar EV-08 as ressalvas mais antigas (R1 e R3 de FIT-2026-001 atravessam quatro ciclos) |
| **R4** | **O entregavel central nao esta em vigor.** MEM-EST-0001 permanece `aprovado`, com `ratificacao: pendente`, pela divergencia reincidente FND-10 §2.2 × §10.3 | O contrato vale; o **conteudo** que ele governa ainda nao orienta ninguem. Um leitor pode concluir que a missao entregou norma sem objeto | DEP-GOV; ato do **SOBERANO** | **Ato do Soberano** sobre o registro, **ou** resolucao do achado C2 pelo seu proprio gatilho — o que vier antes |

> **R4 nao e defeito de execucao.** E o resultado correto de aplicar GV-03 a uma divergencia
> que a missao **nao podia** resolver: pre-correcao 3 proibiu produzir ratificacao, e o achado
> C2 tem dono e gatilho fixados por outra revisao. Registrar a consequencia e obrigatorio
> (PI-10); resolve-la aqui teria sido usurpar o dono declarado.

## Veredito

| Campo | Conteudo |
|---|---|
| Veredito | **`apto-com-ressalva`** |
| Fundamento | As seis perguntas tem sinal observavel. Um achado de revisao aberto desde a missao anterior **fecha**; nenhuma entidade, tipo, camada, template ou documento fundacional e criado; a duplicacao foi barrada antes de existir. Em contrapartida, **quase metade das regras novas nao tem como ser exercida**, tres abstracoes nascem vazias, **nenhuma ressalva anterior foi fechada** e **o custo de contexto medido subiu**. O veredito nao e `inapto` porque nenhuma dessas contrapartidas revela degradacao **sem contrapartida verificavel**; e o mais proximo de `inapto` dos quatro emitidos |
| Efeito | **Encerra.** As quatro ressalvas viram divida declarada com dono e gatilho (FND-07 §9) |
| Data | 2026-07-28 |
| Executado por | **DEP-QAR** |
| Aprovado por | **DEP-EXE** |
| Ratificado por | **Nao aplicavel** — objeto C2/Tipo 2 |

### Nota sobre FT-04 — vigilancia de complacencia

| Verificacao | Estado |
|---|---|
| Vereditos emitidos | **4** |
| Consecutivos `apto` **sem nenhuma ressalva** | **0** — os quatro com ressalvas |
| `inapto` emitidos | **0** |
| Ressalvas anteriores **fechadas neste ciclo** | **0** |
| Ressalvas anteriores **com progresso medido** | **3** — R1 e R3 de FIT-2026-003 e R4 de FIT-2026-002 |

FT-04 exige tres `apto` **sem ressalva** para disparar; nao e o caso.

> **O alarme armado por FIT-2026-002 volta a ficar relevante.** Aquele documento escreveu: *"se
> a terceira verificacao tambem terminar em `apto-com-ressalva` sem que nenhuma ressalva
> anterior tenha sido fechada, o mecanismo estara produzindo divida em vez de correcao"*. A
> terceira **fechou duas** e desarmou o alarme. **A quarta fecha zero.** Nao dispara a regra
> literal — que fala da terceira —, mas restaura exatamente a condicao que ela vigiava.
> Registrado aqui, e convertido na ressalva **R3** com gatilho na proxima mudanca C2/C3.

Permanece o numero a vigiar: **nenhum `inapto` em quatro oportunidades**. Registra-se como
observacao, nao como conclusao.

### Nota de conflito de interesse (PI-10)

| Campo | Conteudo |
|---|---|
| Conflito identificado | **Nenhum.** DEP-QAR nao produziu nenhum artefato avaliado, nem revisou o proprio produto |
| Residuo | DEP-QAR foi **revisor independente** de ADR-0009 e ADR-0010 e **autor** da revisao arquitetural. Sao a mesma funcao de verificacao, exercida em dois instrumentos — nao ha acumulo de producao com verificacao (FND-04 §3.1) |
| Comparacao com o ciclo anterior | FIT-2026-003 exigiu desvio duplo, por impedimento de DEP-QAR. **Aqui nenhum desvio foi necessario** — dado favoravel ao achado C5 |
| Registro | Declarado em vez de omitido |

## Aprendizado gerado

| Registro APR | Licao |
|---|---|
| [MEM-APR-0002](../../memory/aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md) | **Segunda confirmacao observada**, com alcance ampliado: o achado **D8** mostra que numero afirmado divergente da tabela que o sustenta e da mesma familia da reproducao de tabela |
| A gravar por DEP-KMS *(QG-5)* | **Registrar o que nao se sabe e entregavel, nao lacuna do entregavel.** Das 45 afirmacoes do primeiro registro sobre o Soberano, **11 sao `unknown`** — inclusive o significado dos dois termos que a determinacao **nomeou expressamente**. A alternativa — defini-los por analogia com a Definicao de Pronto — teria produzido um documento mais completo e **falso**. Acao: a estrutura de registro passa a exigir que a lacuna tenha gatilho proprio, como ja exige CT-07 e a regra **L-4** do registro. Dono: DEP-KMS |

## Historico de vereditos sobre este objeto

| FIT | Data | Veredito | Relacao |
|---|---|---|---|
| FIT-2026-004 | 2026-07-28 | `apto-com-ressalva` | Primeiro sobre este objeto |
