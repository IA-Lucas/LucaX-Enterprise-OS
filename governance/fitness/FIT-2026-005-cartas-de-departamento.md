---
id: FIT-2026-005-cartas-de-departamento
titulo: Aptidao arquitetural do Contrato de Carta de Departamento e dos dois pilotos
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
decisoes_relacionadas: [ADR-0011]
substitui: []
substituido_por: null
objeto_avaliado: [RFC-0008, ADR-0011, TPL-carta-departamento, IDX-capabilities, DEP-QAR, DEP-ENG]
classe_mudanca: C2
classe_avaliacao: aptidao
veredito: apto-com-ressalva
resumo: Verifica se a Missao 1.6 deixou a arquitetura mais apta a evoluir; veredito apto-com-ressalva, cinco ressalvas, e decisao ADJUST para o rollout.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-GOV
ratificacao: nao-exigida
---

# FIT-2026-005: Contrato de Carta de Departamento e pilotos

## Proposito
Verificar se a Missao 1.6 — contrato de Carta de Departamento, projecao Departamento ×
Capability, template emendado e dois pilotos — deixou a arquitetura **mais apta a evoluir**, e
decidir **GO / ADJUST / STOP** para o rollout das sete Cartas restantes.

## Escopo
| Item | Definicao |
|---|---|
| Objeto avaliado | RFC-0008 · ADR-0011 · `TPL-carta-departamento` 1.1.0 · `capabilities/README` 1.1.0 · Cartas **DEP-QAR** e **DEP-ENG** |
| Estado anterior | **100 artefatos, 23.742 linhas** *(`BL-2026-07-28-02`)*; **0** Cartas de Departamento; **12** ressalvas de aptidao abertas; **4** vereditos consecutivos `apto-com-ressalva` |
| **Nao** inclui | Corretude estrutural — objeto de [REV-DEPARTAMENTO](../../foundation/revisao-arquitetural-cartas-de-departamento-2026-07-28.md) |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| **Executa** | **DEP-QAR** | FT-02, CV-08 — **nao produziu nenhum artefato avaliado**; autor das Cartas e DEP-EXE, revisor e DEP-GOV |
| Forma | DEP-GOV | |
| Evidencia | DEP-KMS | Medicoes de acervo, de secao e de pacote |
| **Aprova** | **DEP-EXE** | FND-10 §10.3, matriz normal |
| Ratifica | **Nao aplicavel** | Objeto avaliado e **C2/Tipo 2** |

> **Residuo de conflito declarado.** DEP-QAR e **objeto** de um dos pilotos. Os blocos B4, B9
> e B12 da Carta DEP-QAR foram verificados por **DEP-GOV**, e o residuo esta descrito em
> [REV-DEPARTAMENTO §4](../../foundation/revisao-arquitetural-cartas-de-departamento-2026-07-28.md).
> Esta verificacao julga **aptidao da mudanca**, nao a autoridade de DEP-QAR.

---

## Sumario

| # | Pergunta | Resposta | Sinal |
|---|---|---|---|
| F1 | Complexidade aumentou sem ganho proporcional? | **Nao** | **+2.764 linhas (11,6%)** e **10 regras novas, 10 exercidas**; contra **2** ressalvas fechadas, **1** defeito corrigido antes do rollout e **0** entidades, tipos, camadas ou documentos fundacionais criados |
| F2 | Algum conceito foi duplicado? **e** a prevencao foi aplicada? | **Nao · aplicada** | **200 tabelas** percorridas; **3** reproducoes barradas antes da escrita; **8** projecoes declaradas |
| F3 | Alguma abstracao ficou desnecessaria? | **Sim, duas** | `PR-1` e `PR-2`: **0** membros — e vazias por construcao |
| F4 | Continua mais simples de evoluir? | **Sim** | Seis perguntas antes sem resposta verificavel passam a ter uma; **nenhuma aprovacao nova** criada |
| F5 | Custo de contexto subiu ou desceu? | **Nao subiu** — terceira medicao | **33% → 30,6%**. A alta de 1.5 **nao** se confirmou como tendencia |
| F6 | Favorece reutilizacao? | **Sim** | 10 de 10 regras `DC` servem a qualquer Carta; **7** das 9 servem tambem a Carta de Agente |

**Veredito:** `apto-com-ressalva` — **cinco** ressalvas, todas com dono e gatilho.
**Decisao de rollout: ADJUST** (§Rollout).

---

## F1 — A complexidade aumentou sem ganho proporcional?

| Medida | Antes | Depois | Variacao |
|---|---|---|---|
| Artefatos | 100 | **107** | **+7** |
| Linhas | 23.742 | **26.506** | **+2.764 (11,6%)** |
| Entidades | 21 | **21** | **0** |
| Arquetipos · relacoes · tipos documentais | 4 · 10 · 33 | **4 · 10 · 33** | **0** |
| Documentos fundacionais | 10 | **10** | **0** |
| Camadas de memoria | 5 | **5** | **0** |
| Templates | 19 | **19** | **0** criados · **1** emendado |
| Portoes de qualidade | 7 | **7** | **0** |
| **Componentes com Carta** | **0** | **2** | **+2** — os primeiros do sistema |
| Regras normativas novas | — | **10** *(DC-01 a DC-10)* + 3 *(PR-1 a PR-3)* | +13 |
| **Regras novas exercidas** | — | **11 de 13** | — |
| Ressalvas de aptidao **fechadas** | — | **2** | — |
| Achados de revisao **corrigidos antes do encerramento** | — | **3** *(D1, DR-7, DR-8)* | — |
| Arquivos do acervo reescritos por retroatividade | — | **0** | — |
| Arquivos de ADR editados | — | **0** | — |
| Cartas de Capability alteradas | — | **0** | — |
| Artefatos preexistentes emendados *(MENOR)* | — | **3** | — |
| Indices atualizados *(M3 derivado, AC-09)* | — | **9** | — |

**As 11 regras novas exercidas:** `DC-01` *(duas Cartas citam so `CAP` vigentes; DEP-QAR
recusa corrigir P3/P4)* · `DC-02` *(duas colunas em ambas)* · `DC-03` *(**7** impedimentos em
DEP-QAR, **8** em DEP-ENG)* · `DC-04` *(**8** e **7** linhas de autoridade, todas com fonte)* ·
`DC-05` *(**10** e **11** exclusoes com dono real)* · `DC-06` *(duas decisoes registradas de
**nao** especializar)* · `DC-07` *(**8** indicadores marcados `definido, sem valor`)* ·
`DC-08` *(**3** reproducoes barradas)* · `DC-09` *(duas Cartas retidas em `em-revisao`)* ·
`DC-10` *(**6** custos de recorte medidos)* · `PR-3` *(invocada uma vez, para **nao** acrescentar
exercente unilateralmente)*.

**As 2 nao exercidas:** `PR-1` e `PR-2` — **dependem de uma divergencia entre Carta de
Departamento e Carta de Capability, que nao ocorreu**. Ver F3.

**Leitura.** O acrescimo tem contrapartida verificavel e **medida em quatro frentes**:
as duas primeiras Cartas do sistema existem; **duas** ressalvas abertas ha ciclos fecham;
**um** defeito de contrato foi encontrado e corrigido **antes** do rollout, nao depois de nove
instancias; e a proporcao de regra ociosa caiu de **15 em 32** *(Missao 1.5)* para **2 em 13**.

**Um defeito aberto ha tres ciclos tambem fecha:** `MEM-APR-0002` declarava **2** ocorrencias
com **5** documentadas em tres revisoes distintas — achado **DR-8**, encontrado na propagacao
obrigatoria aos indices, nao por cenario nem por auditoria de duplicacao.

**Resposta:** **nao**.

## F2 — Algum conceito foi duplicado? E a prevencao foi aplicada?

### F2.a — Ocorrencia

| Conceito | Onde ja estava definido | Como a mudanca o trata |
|---|---|---|
| Matriz de interacao entre departamentos | FND-02 §4 | **Barrada.** As duas Cartas declaram *"a matriz completa vive em FND-02 §4 e nao e reproduzida aqui"* e listam **so as proprias linhas** |
| Custodia e exercicio por Capability | frontmatter das 23 Cartas `CAP` | **Projecao declarada** com as quatro informacoes de PJ-02, em tres niveis: catalogo §10, Carta §2, e a regra de precedencia PR-1 |
| Estrutura, classes e niveis dos 9 departamentos | FND-02 §2.1 e §3 | **Referenciada**, nunca reescrita. As Cartas nao redefinem classe nem nivel |
| Os sete portoes de qualidade | FND-01 §6.2 | **Referenciados.** As duas Cartas declaram *"nenhum portao novo e criado aqui"* |
| Matriz de autoridade por entidade | FND-09 §8.2 | **Referenciada** linha a linha, na coluna **Fonte** de B4 |
| Camadas de memoria e seus donos | FND-06 §2.1 | **Referenciadas.** B7 declara o **papel do departamento** por camada, nao a definicao da camada |
| Contrato de Carta em documento fundacional novo | — | **Nao criado.** FND-11 recusado pelos mesmos tres criterios de REV-SOBERANO §6.1 |

**Nenhuma duplicacao nova introduzida.** Verificacao:
[REV-DEPARTAMENTO §2 e §7](../../foundation/revisao-arquitetural-cartas-de-departamento-2026-07-28.md).

### F2.b — Prevencao *(PJ-06)*

| Verificacao | Evidencia | Resultado |
|---|---|---|
| O autor percorreu **cada** tabela pelo item de PJ-05? | **200 tabelas** nos **sete** artefatos novos e nos **tres** emendados, contadas por ferramenta | **Sim** |
| Toda exibicao de conteudo de outra fonte declara projecao? | **8** declaracoes: catalogo §10 · Carta DEP-QAR §2 · Carta DEP-ENG §2 · `projecao_de` do catalogo · e as quatro notas de nao reproducao em §6.3 e §5.2 das duas Cartas | **Sim** |
| Alguma reproducao foi **barrada antes** de ser escrita? | **3** — a matriz de FND-02 §4 *(duas vezes, uma por Carta)* e a lista dos sete portoes de FND-01 §6.2 | **Sim** |
| O teste encontrou algo que a auditoria posterior nao encontraria? | **1** — o defeito **D1**: `projecao_de` declarado em artefato que **nao** e majoritariamente projecao. Uma auditoria de duplicacao nao o encontraria, porque **nao ha duplicacao**: o defeito e de **classificacao** do artefato | **Sim** |

> **Terceira confirmacao observada de [MEM-APR-0002](../../memory/aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md),
> com alcance novamente ampliado.** D1 nao e reproducao nem afirmacao derivada divergente: e
> **declarar-se projecao sem ser**. A familia cresce de "copiar tabela" para "errar a natureza
> do proprio artefato" — mesmo mecanismo, terceiro objeto. Registrado em
> [MEM-APR-0004](../../memory/aprendizado/MEM-APR-0004-projecao-revela-divergencia-antiga.md).

**Resposta:** nao houve duplicacao nova · prevencao **aplicada**, com evidencia.

## F3 — Alguma abstracao ficou desnecessaria?

| Abstracao introduzida | Membros | Consumidor declarado | Veredito |
|---|---|---|---|
| **12 blocos** B1–B12 | **24** — 12 por Carta, todos preenchidos | `TPL-carta-departamento`, checklist | **Justificada e exercida** |
| `DC-01` a `DC-10` | **10 de 10 exercidas**; 60 aplicacoes contadas | As duas Cartas | **Justificada e exercida** |
| **`PR-1`** — fonte prevalece em divergencia | **0** | ADR-0011 §5.5 | **Ociosa hoje, e desejavelmente ociosa**: so ganha membro quando houver divergencia |
| **`PR-2`** — proibido corrigir a fonte para caber na projecao | **0** | ADR-0011 §5.5 | **Ociosa hoje, e desejavelmente ociosa** |
| `PR-3` — acrescentar exercente e mudanca na Carta de Capability | **1** — invocada por DEP-QAR §2 para **nao** corrigir P3/P4 | Carta DEP-QAR | **Justificada** |
| **8 conteudos proibidos** (§5.4) | **9 ocorrencias barradas**: 1 portao, 3 reproducoes, 8 indicadores sem valor *(contadas como uma familia)*; **0** credenciais | As duas Cartas | **Justificada** — 5 dos 8 tipos foram acionados |
| Diretorio `departments/` | **2** de 9 subdiretorios | As duas Cartas | Justificada — nasce com o primeiro artefato do tipo (FND-03 §7.2) |
| Projecao Departamento × Capability | **9** linhas · **8** achados | Carta §2, VC-01, revisao estrutural | **Justificada** — produziu achados que nenhuma leitura por Capability produziria |

**Regra aplicada:** abstracao com menos de dois membros e suspeita (AQ-03).

**Duas abstracoes tem zero membros**, e ambas pela mesma razao: `PR-1` e `PR-2` sao regras de
**precedencia em conflito**, e nao houve conflito. Diferentemente das tres abstracoes vazias de
FIT-2026-004, estas **nao foram criadas por antecipacao de uso**: sao a resposta a pergunta
"quem vence se divergirem?", que precisa ter resposta escrita **antes** da primeira divergencia
— caso contrario a primeira divergencia sera resolvida por hipotese.

**Resposta:** **sim, duas** — ambas vazias por construcao, e o resultado bom e que permanecam
vazias. **→ Ressalva R1.**

## F4 — O sistema continua mais simples de evoluir do que antes?

| Mudanca-tipo | Antes | Depois | Aprovacoes |
|---|---|---|---|
| Saber **o que um departamento custodia e exerce** | Abrir 23 Cartas de Capability | Uma linha do catalogo §10.1 | Inalterado |
| Saber se **um departamento pode aprovar ou verificar** algo | **Nao havia fonte** — inferia-se de FND-02 §3 cruzado com FND-09 §8.2 | Bloco B9 da Carta: impedimento, motivo e **substituto nomeado** | Inalterado |
| Saber se uma Carta esta **correta** | Julgamento | **12 blocos + 10 regras**, verificaveis item a item | Inalterado |
| Saber de onde vem a **autoridade** de um departamento | Implicito | Coluna **Fonte** em cada linha de B4 | Inalterado |
| Saber se um departamento **deve ser dividido** | Contagem isolada de Capabilities | B11 com **sinal observado** e SE-02; decisao de **nao** dividir registrada com custo | Inalterado |
| Saber **quanto custa** consultar um departamento | **Impossivel** — nao havia Carta | 3 recortes medidos por Carta | Inalterado |
| Criar uma Carta de Departamento | RFC + ADR + template de 13 secoes | RFC + ADR + template de 13 secoes **com checklist de 16 itens** | **Inalterado** |

**Leitura.** Seis perguntas antes sem resposta verificavel passam a ter uma. O preco e um
checklist mais longo no momento da escrita. **Nenhuma aprovacao nova foi criada** — nenhum
caminho de decisao ficou mais longo, e **nenhum papel ganhou poder de veto novo**. A autoridade
de aprovar Carta de Departamento continua sendo exatamente a de FND-09 §8.2: o **SOBERANO**.

**Resposta:** **sim**.

## F5 — A mudanca reduz ou aumenta o custo de contexto?

| Papel / tarefa-tipo | Antes | Depois | Direcao |
|---|---|---|---|
| Piso obrigatorio de qualquer tarefa | 1.099 linhas *(4,6%)* | **1.099 linhas (4,1%)** | inalterado em linhas, **desce** em proporcao |
| **Executar uma missao estrutural** | **33%** — segunda medicao | **30,6%** — terceira medicao | **nao subiu** |
| Saber o que um departamento custodia e exerce | **3.718 linhas** *(23 Cartas `CAP`)* | **1 linha** do catalogo §10.1 | **desce** |
| Decidir se DEP-QAR pode verificar algo | Nao havia fonte | **111 linhas**, medido | desce, a partir do indefinido |
| Decidir se DEP-ENG pode decidir algo | Nao havia fonte | **115 linhas**, medido | desce, a partir do indefinido |
| Escrever uma Carta de Departamento | nucleo + FND-02 + FND-08 + template + `capabilities/README` = 2.491 linhas | nucleo + FND-02 + ADR-0011 + template + catalogo §10 = **2.347 linhas** | **sobe** |
| Acervo total | 23.742 | **26.506** | **sobe 11,6%** |

**Leitura honesta.** A terceira medicao observada deu **30,6%**, contra **33%** na Missao 1.5 e
**23%** na Missao 1.4. **A alta nao se confirmou como tendencia** — que era exatamente a
condicao que R3 de FIT-2026-004 fixou. Mas **nao houve reducao**: a terceira medicao continua
**7,4 pontos acima** da primeira, e nenhuma das tres mostra o custo caindo.

**O que subiu de fato:** escrever uma Carta de Departamento passou a custar mais, porque o
contrato acrescentou material obrigatorio ao pacote. **O que desceu:** consultar um
departamento passou de "nao havia fonte" para um recorte medido em **29% da Carta**.

**Resposta:** **nao subiu** na missao medida; **subiu** no acervo. **→ Ressalva R3.**

## F6 — Ela favorece reutilizacao?

| Definicao produzida | Reutilizavel por | Especifica do caso? |
|---|---|---|
| `DC-02` — custodia × exercicio em colunas separadas | Carta de **Agente** e de **Subagente**, que tambem declaram `capabilities` | Nao |
| `DC-03` — impedimento com substituto nomeado | **Qualquer** componente com autoridade: agente, subagente, workflow | Nao |
| `DC-04` — autoridade com fonte declarada | Qualquer Carta; e o mecanismo direto de AU-09 | Nao |
| `DC-06` — subdivisao exige sinal observado | Qualquer componente sujeito a PI-14 | Nao |
| `DC-07` — indicador `definido, sem valor` | **Qualquer artefato com indicador** — inclusive as 23 Cartas de Capability, onde 88 de 111 indicadores estao nessa condicao sem marca | Nao |
| `DC-08` — referencia em vez de reescrita | Qualquer artefato | Nao |
| `DC-09` — nao entra em vigor por si | Qualquer artefato cuja aprovacao seja do Soberano | Nao |
| `DC-10` — perfil de carregamento medido | Qualquer artefato grande; e o mesmo mecanismo do nucleo por recorte e dos pacotes `CT-21` | Nao |
| Projecao Departamento × Capability | Qualquer pivo do catalogo — por dominio, por classe, por maturidade | Nao |
| `DC-01` e `DC-05` | Carta de Departamento | **Sim, parcialmente** — pressupoem escopo exclusivo de dominio |

**Criterio:** DoD-8.

**Evidencia mais forte:** **sete das nove** regras `DC` reutilizaveis servem sem adaptacao a
Carta de Agente, que e o **proximo** tipo constitutivo a ser instanciado — e a missao
deliberadamente **nao** as estendeu a ele, porque nenhum agente existe (FND-08 §7.1). O ganho
esta disponivel sem que a antecipacao tenha sido feita.

**Resposta:** **sim**, com uma excecao declarada.

---

## Ressalvas

| # | Ressalva | Custo assumido | **Dono** | **Gatilho de reavaliacao** |
|---|---|---|---|---|
| **R1** | **As 10 regras `DC` foram exercidas 10 de 10 — mas por construcao.** As duas Cartas foram escritas **sob** o contrato, pelo mesmo autor, na mesma missao. O contrato ainda **nao foi testado contra uma Carta nao conforme escrita por terceiro**. `PR-1` e `PR-2` permanecem com **0** membros | Uma taxa de exercicio de 100% pode estar medindo a autoria, nao a regra. O contrato pode ser incapaz de **barrar** o que consegue **produzir** | **DEP-EXE** | **Terceira Carta escrita** — a primeira fora dos pilotos. Se ela passar no checklist sem nenhum item devolvido, a regra e frouxa ou o autor e o mesmo; ambos exigem resposta |
| **R2** | **Validado em 2 de 4 classes.** Comando e Plataforma ficam sem piloto. Em particular, **DEP-EXE e autor de todas as Cartas** e sera **objeto** da propria — impedimento que nenhum piloto testou | O contrato pode nao comportar a classe Comando, cuja autoridade e de natureza distinta *(arbitra, nao veta nem entrega)*. O impedimento de DEP-EXE nao tem substituto obvio | **DEP-EXE** | **Primeira Carta de classe Plataforma**, que o rollout deve produzir **antes** das demais (§Rollout) |
| **R3** | **Quinta missao consecutiva de crescimento do acervo:** **+11,6%**, de 23.742 para **26.506** linhas. Nenhuma consolidacao ocorreu em nenhum dos cinco ciclos | O acervo cresce monotonicamente ha cinco ciclos e **nenhum artefato foi fundido, aposentado ou dividido** em nenhum deles. PI-14 tem dois movimentos e so um esta sendo exercido | **DEP-EXE** | **Proxima mudanca C2/C3.** Se a sexta tambem crescer **sem nenhuma consolidacao**, aplicar EV-08 aos candidatos mais antigos — e a assimetria deixa de ser circunstancial |
| **R4** | **Os dois pilotos nao estao em vigor.** Ambos permanecem em `em-revisao`, `ratificacao: pendente`. **O rollout das sete Cartas restantes esta bloqueado** por ato que a missao nao pode produzir | O entregavel central existe e **nao orienta ninguem**. E a segunda vez consecutiva que uma missao entrega instancia retida por falta de ato do Soberano — a primeira foi MEM-EST-0001 | **DEP-GOV**; ato do **SOBERANO** | **Ato do Soberano** sobre as duas Cartas — aprovacao e ratificacao no mesmo ato (FND-09 §8.2) |
| **R5** | **Duas ressalvas atravessam cinco ciclos sem que o gatilho dispare.** R1 e R3 de FIT-2026-001 tem gatilho na **1a revisao estrutural**, que nao ocorreu em nenhum dos cinco ciclos | Gatilho que nunca dispara e divida perpetua com aparencia de controle. A 1a revisao estrutural e o gatilho de **6 das 13** ressalvas abertas | **DEP-EXE** com DEP-GOV | **Fim do 1o horizonte, ou a proxima mudanca C2/C3** — o que vier antes. Se a revisao estrutural nao for agendada ate la, **escalar ao Soberano** |

## Veredito

| Campo | Conteudo |
|---|---|
| Veredito | **`apto-com-ressalva`** |
| Fundamento | As seis perguntas tem sinal observavel. **Duas** ressalvas abertas ha ciclos fecham com evidencia reproduzivel; **um** defeito de contrato foi encontrado pela validacao e corrigido **antes** do rollout; **nenhuma** entidade, tipo, camada, template ou documento fundacional foi criado; a proporcao de regra ociosa caiu de 15/32 para 2/13; e o custo de contexto medido **nao subiu**. Em contrapartida, o exercicio das regras e **autoral**, o contrato so viu **2 das 4 classes**, o acervo cresce pelo **quinto** ciclo sem nenhuma consolidacao, e o entregavel central **nao esta em vigor**. Nao e `inapto` porque nenhuma dessas contrapartidas revela degradacao sem contrapartida verificavel |
| Efeito | **Encerra.** As cinco ressalvas viram divida declarada com dono e gatilho (FND-07 §9) |
| Data | 2026-07-28 |
| Executado por | **DEP-QAR** |
| Aprovado por | **DEP-EXE** |
| Ratificado por | **Nao aplicavel** — objeto C2/Tipo 2 |

## Rollout das sete Cartas restantes — **ADJUST**

| Campo | Conteudo |
|---|---|
| **Decisao** | **ADJUST** — o rollout prossegue, **nao** em lote e **nao** agora |
| Por que nao **GO** | **(a)** Os dois pilotos nao estao em vigor (R4): escrever sete Cartas sob contrato cujos pilotos ainda podem ser recusados multiplicaria o retrabalho por sete. **(b)** O contrato so foi exercido em 2 das 4 classes (R2). **(c)** O exercicio das regras e autoral (R1) |
| Por que nao **STOP** | Os seis cenarios de validacao resolveram **sem ambiguidade**; o unico defeito encontrado foi corrigido; nenhuma norma foi violada; e o contrato ja produziu ganho medido — 8 achados na projecao e 8 indicadores que teriam sido afirmados sem medida |
| **Condicao 1** | **Ato do Soberano** aprovando e ratificando as duas Cartas piloto. Sem ele, nenhuma Carta nova e escrita (R4) |
| **Condicao 2** | A **terceira** Carta e de classe **Plataforma** — `DEP-KMS` ou `DEP-TLS` —, escrita **sozinha**, e submetida ao mesmo checklist. So depois dela as demais entram em lote (R2, DR-5) |
| **Condicao 3** | Os achados **DR-3** *(ambiguidade de `departments/<dep>`)* e **DR-6** *(medicao autorreferente)* resolvidos antes da terceira Carta |
| **Condicao 4** | Na terceira Carta, medir quantos itens do checklist foram **devolvidos**. Zero devolucoes reabre R1 como sinal de regra frouxa |
| Quem decide o rollout | **DEP-EXE**, com parecer de DEP-GOV; cada Carta e aprovada e ratificada pelo **SOBERANO** |

### Nota sobre FT-04 — vigilancia de complacencia

| Verificacao | Estado |
|---|---|
| Vereditos emitidos | **5** |
| Consecutivos `apto` **sem nenhuma ressalva** | **0** — os cinco com ressalvas |
| `inapto` emitidos | **0** |
| Ressalvas anteriores **fechadas neste ciclo** | **2** — R3 de FIT-2026-003 e R3 de FIT-2026-004 |
| Ressalvas anteriores **medidas mas nao fechadas** | **2** — R1 e R2 de FIT-2026-004, ambas com defeito de gatilho registrado |
| Achados de revisao **abertos ha 3+ ciclos que fecham** | **1** — DR-8 |

FT-04 exige tres `apto` **sem ressalva** para disparar; nao e o caso.

> **O alarme de FIT-2026-002 esta desarmado, e o de FIT-2026-004 permanece armado.** O
> primeiro vigiava ressalvas que nunca fecham: **duas fecharam**. O segundo vigiava o
> crescimento sem contrapartida: **o acervo cresce pelo quinto ciclo consecutivo e nenhuma
> consolidacao ocorreu em nenhum deles** — convertido na ressalva **R3**, com gatilho na
> proxima mudanca C2/C3.

Permanece o numero a vigiar: **nenhum `inapto` em cinco oportunidades**. Registra-se como
observacao, nao como conclusao.

### Nota de conflito de interesse (PI-10)

| Campo | Conteudo |
|---|---|
| Conflito identificado | **Sim, parcial.** DEP-QAR e **objeto** de um dos pilotos avaliados |
| Por que nao invalida | FT-02 exige que o executor **nao tenha produzido** o artefato avaliado. Autor das Cartas e **DEP-EXE**; revisor, **DEP-GOV**. DEP-QAR nao produziu nenhum dos seis artefatos avaliados |
| Desvio aplicado | Os blocos **B4**, **B9** e **B12** da Carta DEP-QAR foram verificados por **DEP-GOV** (REV-DEPARTAMENTO §4.1) |
| Residuo | DEP-QAR redige o documento que contem a verificacao alheia. Residuo de **forma**, declarado em vez de omitido |
| Alternativa recusada | Trocar o piloto de Guarda por DEP-GOV **agravaria**: DEP-GOV e o revisor previsto de toda Carta de Departamento e revisaria a propria |

## Aprendizado gerado

| Registro APR | Licao |
|---|---|
| [MEM-APR-0004](../../memory/aprendizado/MEM-APR-0004-projecao-revela-divergencia-antiga.md) | **Projecao nova revela divergencia antiga.** Pivotar a mesma fonte por outro eixo produziu **8 achados** que cinco ciclos de leitura por Capability nao produziram — e o mais forte deles, **P1**, mostra que uma regra vigente ha cinco ciclos (OW-02) tem **um unico membro observado** |
| [MEM-APR-0002](../../memory/aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md) | **Terceira confirmacao observada**, com alcance ampliado por **D1**: declarar-se projecao sem ser e da mesma familia de reproduzir tabela. Muda o objeto, nao o mecanismo |
| A gravar por DEP-KMS *(QG-5)* | **Contrato exercido pelo proprio autor mede a autoria, nao a regra.** 10 de 10 regras exercidas nao prova que o contrato barre uma Carta nao conforme. Acao: a terceira Carta mede **devolucoes**, nao exercicio. Dono: DEP-EXE |

## Historico de vereditos sobre este objeto

| FIT | Data | Veredito | Relacao |
|---|---|---|---|
| FIT-2026-005 | 2026-07-28 | `apto-com-ressalva` | Primeiro sobre este objeto |
