---
id: FIT-2026-006-validacao-interclasses
titulo: Aptidao arquitetural da ativacao dos pilotos e da validacao interclasses
tipo: fitness
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-QAR
proprietario: DEP-QAR
aprovador: DEP-GOV
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0011]
substitui: []
substituido_por: null
objeto_avaliado: [MSG-2026-0001, DEP-QAR, DEP-ENG, DEP-EXE, DEP-KMS, TPL-carta-departamento]
classe_mudanca: C2
classe_avaliacao: aptidao
veredito: apto-com-ressalva
resumo: Verifica se a Missao 1.7 deixou a arquitetura mais apta a evoluir; veredito apto-com-ressalva, quatro ressalvas, abertura da proposta de consolidacao e duas pendencias escaladas ao Soberano.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-GOV
ratificacao: nao-exigida
---

# FIT-2026-006: Ativacao dos pilotos e validacao interclasses

## Proposito
Verificar se a Missao 1.7 — ativacao de `DEP-QAR` e `DEP-ENG` sob o ato soberano, Cartas de
**Comando** e **Plataforma**, oito cenarios interclasses e correcao dos criterios de medicao —
deixou a arquitetura **mais apta a evoluir**, e decidir **GO / ADJUST / STOP** para as **cinco**
Cartas restantes.

## Escopo
| Item | Definicao |
|---|---|
| Objeto avaliado | `MSG-2026-0001` · as **quatro** Cartas · `TPL-carta-departamento` 1.2.0 |
| Estado anterior | **107 artefatos, 26.506 linhas** *(`BL-2026-07-28-03`)*; **2** Cartas, ambas **`em-revisao`**; **13** ressalvas de aptidao abertas; **5** vereditos consecutivos `apto-com-ressalva` |
| **Nao** inclui | Corretude estrutural — objeto de [REV-INTERCLASSES](../../foundation/revisao-arquitetural-validacao-interclasses-2026-07-28.md). As cinco Cartas restantes. O **merito** do ato soberano |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| **Executa** | **DEP-QAR** | FT-02, CV-08 — **nao produziu nenhum artefato avaliado**; autor das Cartas e DEP-EXE |
| Forma | DEP-GOV | |
| Evidencia | DEP-KMS | Medicoes de acervo, de secao, de pacote e de hash |
| **Aprova** | **DEP-GOV** | **Desvio declarado.** A matriz atribui a aprovacao de `FIT` a **DEP-EXE**, que esta **impedido**: produziu dois dos objetos avaliados (`DEP-EXE §10, I-2`). Cenario **CX-3**; precedente **FIT-2026-003** |
| Ratifica | **Nao aplicavel** | Objeto avaliado e **C2/Tipo 2** |

> **Residuo de conflito declarado.** DEP-QAR e **objeto** de um dos pilotos ja ativos, e
> **DEP-GOV** aprova este parecer tendo revisado as quatro Cartas. Os dois residuos estao
> descritos em [REV-INTERCLASSES §4](../../foundation/revisao-arquitetural-validacao-interclasses-2026-07-28.md),
> com as alternativas avaliadas e recusadas. Esta verificacao julga **aptidao da mudanca**, nao
> a autoridade de nenhum departamento.

---

## Regras de medicao corrigidas nesta verificacao

> **Correcao determinada para esta missao.** Duas regras de leitura de ressalva estavam
> produzindo resultado que nao correspondia ao fato. Ambas ja tinham sido diagnosticadas como
> defeito de criterio em [REV-DEPARTAMENTO §6](../../foundation/revisao-arquitetural-cartas-de-departamento-2026-07-28.md),
> achados **DR-1** e **DR-2**, com acao pendente em §10.

### Onde a correcao e aplicada, e por que aqui

| Constatacao | Consequencia |
|---|---|
| A missao determinou corrigir **R1 e R2**. Os dois defeitos descritos — *recorrencia que ignora o dominio* e *regra dependente de `MEM-EST-0001`* — correspondem **literalmente** a **R1 e R2 de FIT-2026-004** *(medicao das 28 regras `CT`; tres abstracoes com zero membros)*, cujos defeitos de criterio sao **DR-1** e **DR-2** | A correcao e aplicada a **R1 e R2 de FIT-2026-004** |
| **R1 e R2 de FIT-2026-005** tem gatilho disparado nesta missao — *"terceira Carta escrita"* e *"primeira Carta de classe Plataforma"* — e a mesma leitura defeituosa as alcanca | A correcao e aplicada **tambem** a **R1 e R2 de FIT-2026-005** |
| **`FIT-2026-004` e `FIT-2026-005` sao classe M1** — imutaveis apos eficacia (FND-10 §6.2). Editar qualquer um repetiria a causa de INC-2026-002 e violaria PJ-04 e MEM-APR-0003 | A correcao vive **neste** `FIT`, que supera a leitura anterior sem tocar os artefatos (LV-04, FT-09) |
| **`FIT` e parecer, nao norma** — *"nenhuma regra vigora por causa de um Fitness Check"* (INC-2026-002 §2) | As duas correcoes valem como **criterio de leitura das ressalvas nomeadas**, que e competencia propria do `FIT` que as reconcilia. **Generaliza-las como regra vinculante de toda avaliacao futura exigiria ADR** — ver §Pendencias |

### Correcao 1 — recorrencia considera escopo e natureza da missao

> **Ausencia fora do dominio aplicavel nao e ocorrencia negativa.** Contar quantas vezes uma
> regra deixou de ser exercida so tem sentido entre missoes **cuja materia a regra alcanca**.
> Missao de outro assunto produz ausencia **esperada**, e registrar essa ausencia como sinal de
> regra ociosa mede a **agenda da missao**, nao a regra.

| Aplicada a | Efeito |
|---|---|
| **R1 de FIT-2026-004** | *"0 de 28 regras `CT` exercidas"* deixa de satisfazer a condicao de consolidacao. Esta missao **nao registrou nenhuma afirmacao sobre o Soberano**: a materia esta fora do dominio. Estado: **`nao-avaliavel`**. Gatilho reformulado: *"segunda missao **que toque a materia** do contrato"* |
| **R1 de FIT-2026-005** | A ausencia de devolucoes de **conteudo** no checklist deixa de ser lida isoladamente: o autor e o mesmo nas quatro Cartas, e a ressalva pergunta se o contrato **barra** o que consegue **produzir**. Estado: **aberta e medida** — §Ressalvas |
| **`PR-1` e `PR-2`** *(0 membros)* | Deixam de ser contadas como abstracao ociosa. Sao regras de **precedencia em conflito**, e **nao houve divergencia** entre Carta de Departamento e Carta de Capability em **quatro** Cartas. **Zero membros e o resultado bom**, e a ausencia esta fora do dominio aplicavel |

### Correcao 2 — regra dependente de `MEM-EST-0001` e `nao-avaliavel`

> **Enquanto a memoria estiver inativa, a regra que depende dela nao conta nem como falha nem
> como aprovacao.** Um teste que nao pode ser executado nao produz resultado; registrar o
> nao-executado como reprovado — ou como aprovado — inventa informacao.

| Aplicada a | Efeito |
|---|---|
| **R2 de FIT-2026-004** | *"tres abstracoes com zero membros"* — as tres recortam `MEM-EST-0001`, que permanece **`aprovado` e nao vigente**, e que o ato de 2026-07-28 **exclui expressamente**. Estado: **`nao-avaliavel`**. Gatilho reformulado: *"primeiro componente criado **apos a entrada em vigor** do registro"* |
| **R2 de FIT-2026-005** | Fechada por outro fundamento — quatro classes exercidas —, e a parcela que dependia dos pacotes de contexto **nao** foi usada no fechamento |
| **`KK-13` da Carta de DEP-KMS** | *"0 de 4 pacotes com consumidor"* fica registrado como **fato medido**, e **nao** como falha de curadoria. A Carta ja o declara assim |
| Toda regra `CT-01` a `CT-28` | **`nao-avaliavel`** enquanto o registro nao entrar em vigor |

**Efeito conjunto: DR-1 e DR-2 fecham.** Os dois achados pediam exatamente estas reformulacoes.
As ressalvas **permanecem abertas**, com o estado corrigido de *falha aparente* para
**`nao-avaliavel`**.

> **O que a correcao evita, concretamente.** Sob o criterio antigo, esta missao mediria **0 de
> 28** pela **segunda vez consecutiva** e abriria proposta de consolidacao contra as 28 regras
> `CT`, tendo como unico fundamento o fato de a missao ter sido **sobre outro assunto**. A
> proposta atingiria um contrato que nunca foi exercido, e a decisao dela decorrente seria
> tomada sobre uma medicao que nao media a coisa avaliada.

> **O que a correcao NAO faz.** Nao declara nenhuma regra boa, util ou justificada. **28 regras
> `CT` continuam sem um unico exercicio**, e as tres abstracoes continuam com **zero** membros.
> A correcao muda o **estado do julgamento** — de *reprovado por ausencia* para *nao julgado* —
> e **nao** o estado do objeto. Confundir as duas coisas seria usar a correcao para fechar
> divida (LM-06).

---

## Sumario

| # | Pergunta | Resposta | Sinal |
|---|---|---|---|
| F1 | Complexidade aumentou sem ganho proporcional? | **Nao** | **+2.460 linhas (9,3%)** contra **2 pilotos ativados**, **2 classes novas exercidas**, **5** ressalvas e achados fechados, **1** correcao nao propagada descoberta e **0** entidades, tipos, camadas ou documentos fundacionais criados |
| F2 | Algum conceito foi duplicado? **e** a prevencao foi aplicada? | **Nao · aplicada** | **3** reproducoes barradas; **6** projecoes declaradas; **1** comparacao nova sem fonte concorrente |
| F3 | Alguma abstracao ficou desnecessaria? | **Nao — e duas sairam da suspeita** | `PR-1` e `PR-2` reclassificadas de *ociosas* para **`nao-avaliaveis`**; **OW-02** ganha exercicio em Carta |
| F4 | Continua mais simples de evoluir? | **Sim** | Quatro classes com resposta verificavel; **nenhuma aprovacao nova** criada |
| F5 | Custo de contexto subiu ou desceu? | **Desceu** — 1a queda da serie | **18,5%**, contra **30,6%** · **33%** · **23%**. **Nao fecha R4 de FIT-2026-002**: um ponto nao e tendencia |
| F6 | Favorece reutilizacao? | **Sim** | **9** propriedades universais isoladas das especificas de classe |

**Veredito:** `apto-com-ressalva` — **quatro** ressalvas, todas com dono e gatilho.
**Decisao de rollout: ADJUST** (§Rollout). **Proposta de consolidacao: ABERTA** (§Consolidacao).
**Duas pendencias escaladas ao SOBERANO** (§Pendencias).

---

## F1 — A complexidade aumentou sem ganho proporcional?

| Medida | Antes | Depois | Variacao |
|---|---|---|---|
| Artefatos | 107 | **112** | **+5** |
| Linhas | 26.506 | **28.966** | **+2.460 (9,3%)** |
| Entidades | 21 | **21** | **0** |
| Arquetipos · relacoes · tipos documentais | 4 · 10 · 33 | **4 · 10 · 33** | **0** |
| Documentos fundacionais | 10 | **10** | **0** |
| Camadas de memoria | 5 | **5** | **0** |
| Templates | 19 | **19** | **0** criados · **1** emendado |
| Portoes de qualidade | 7 | **7** | **0** |
| Departamentos | 9 | **9** | **0** |
| **Departamentos com Carta** | **2** | **4** | **+2** |
| **Cartas em vigor (`ativo`)** | **0** | **2** | **+2** — as primeiras do sistema |
| **Classes exercidas** | **2 de 4** | **4 de 4** | **+2** |
| Regras normativas novas | — | **0** | **0** — nenhuma regra `DC` ou `PR` criada |
| Ressalvas e achados **fechados** | — | **5** | R4 e R2 de FIT-2026-005 · DR-1 · DR-2 · DR-3 · DR-5 · DR-6 |
| Achados **novos** | — | **7** *(IC-1 a IC-7)* | 1 corrigido, 6 com dono e gatilho |
| Correcoes declaradas e **nao propagadas** descobertas | — | **1** *(IC-1)* | Corrigida |
| Arquivos do acervo reescritos por retroatividade | — | **0** | — |
| Artefatos M1 editados | — | **0** | Nenhum `FIT`, `REV`, `INC` ou baseline |
| Cartas de Capability alteradas | — | **0** | — |
| Cartas ratificadas alteradas no **corpo** | — | **0** | Apenas 2 campos de estado por Carta |
| Indices atualizados *(M3 derivado, AC-09)* | — | **8** | — |
| **Propostas de consolidacao abertas** | **0** em 5 ciclos | **1** | **Primeira do sistema** |

**Leitura.** O acrescimo tem contrapartida verificavel: **os dois primeiros artefatos em vigor
do sistema existem**; o contrato passa de **2 para 4 classes exercidas**, fechando o limite
declarado desde ADR-0011 §8 **A2**; **cinco** ressalvas e achados fecham com evidencia; e
**nenhuma regra nova foi criada** — a missao exerceu o contrato existente em vez de amplia-lo,
que e o oposto do padrao dos cinco ciclos anteriores.

**Contrapartida honesta:** **sete achados novos**, e o acervo cresce pelo **sexto** ciclo
consecutivo. O segundo fato dispara R3, tratado em §Consolidacao.

**Resposta:** **nao**.

## F2 — Algum conceito foi duplicado? E a prevencao foi aplicada?

### F2.a — Ocorrencia

| Conceito | Onde ja estava definido | Como a mudanca o trata |
|---|---|---|
| Matriz de interacao entre departamentos | FND-02 §4 | **Barrada** nas duas Cartas novas, que declaram *"a matriz completa vive em FND-02 §4"* e listam **so as proprias linhas** |
| Estrutura, classes e niveis dos 9 departamentos | FND-02 §2.1 e §3 | **Referenciada**, nunca reescrita |
| Os sete portoes | FND-01 §6.2 | **Referenciados.** As duas Cartas declaram *"nenhum portao novo e criado aqui"* |
| Custodia e exercicio | frontmatter das 23 Cartas `CAP` | **Projecao declarada** com as quatro informacoes de PJ-02, em cada Carta |
| Estado de ratificacao das duas Cartas ativas | — | **Fonte unica nova:** `MSG-2026-0001`. Catalogo e indices **referenciam**; nenhum reproduz os hashes |
| **Comparacao das quatro classes** | — | **Nao existia.** Criada em REV-INTERCLASSES §5 como **projecao unica**, com as quatro informacoes de PJ-02 e regra de precedencia |
| Regras `DC` e `PR` | ADR-0011 §5.3 e §5.5 | **Referenciadas.** Nenhuma reescrita, nenhuma criada |

**Nenhuma duplicacao nova introduzida.**

### F2.b — Prevencao *(PJ-06)*

| Verificacao | Evidencia | Resultado |
|---|---|---|
| O autor percorreu cada tabela pelo item de PJ-05? | Todas as tabelas dos artefatos novos e emendados | **Sim** |
| Toda exibicao de conteudo de outra fonte declara projecao? | **6** declaracoes: `DEP-EXE §2` · `DEP-KMS §2` · REV-INTERCLASSES §5 · catalogo §9 e §10 · `MSG-2026-0001 §2` *(vinculo ID×versao×hash, declarado como medicao reproduzivel)* | **Sim** |
| Alguma reproducao foi **barrada antes** de ser escrita? | **3** — a matriz de FND-02 §4 *(duas vezes)* e a lista dos sete portoes | **Sim** |
| O teste encontrou algo que a auditoria posterior nao encontraria? | **1 — IC-1.** Uma auditoria de duplicacao **nao o encontraria**: nao ha duplicacao. O defeito e **ausencia** — uma correcao declarada que nunca chegou ao arquivo | **Sim** |

> **Quarta confirmacao observada de [MEM-APR-0002](../../memory/aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md),
> com alcance ampliado pela terceira vez.** A familia percorreu: *copiar tabela* → *afirmacao
> derivada divergente* → *declarar-se projecao sem ser* (D1) → **agora, declarar correcao
> aplicada sem aplica-la** (IC-1). O mecanismo e o mesmo — **o documento que declara nao e o
> documento que carrega o fato** —, e o objeto mudou de novo. **Registrado como pendencia de
> propagacao ao registro-fonte**, sob o proprio criterio de QG-5 que `DEP-KMS §5.2` acabou de
> materializar (DR-8).

**Resposta:** nao houve duplicacao nova · prevencao **aplicada**, com evidencia.

## F3 — Alguma abstracao ficou desnecessaria?

| Abstracao | Membros antes | **Membros agora** | Veredito |
|---|---|---|---|
| **12 blocos** B1–B12 | 24 | **48** — 12 por Carta, nas quatro | **Justificada e exercida** |
| `DC-01` a `DC-10` | 10 de 10 | **10 de 10**, em **4** classes | **Justificada e exercida** |
| **`PR-1`** — fonte prevalece em divergencia | 0 | **0** | **`nao-avaliavel`** — depende de divergencia, e **nao houve** em 4 Cartas |
| **`PR-2`** — proibido corrigir a fonte | 0 | **0** | **`nao-avaliavel`** — idem |
| `PR-3` — exercente muda na Carta de Capability | 1 | **2** — invocada por `DEP-KMS §10, I-8` | **Justificada** |
| **`OW-02`** — custodia nao e exclusividade | **1**, so na projecao | **1, declarado nas duas Cartas** que o compoem | **Justificada — pela primeira vez em Carta** |
| 8 conteudos proibidos (ADR-0011 §5.4) | 9 barrados | **+8 barrados** — 3 reproducoes, 13 indicadores sem valor, 0 portoes novos, 0 credenciais | **Justificada** |
| Diretorio `departments/` | 2 de 9 | **4 de 9** | Justificada |
| **Tipo documental `Diretiva`** | **0** | **1** — `MSG-2026-0001` | **Justificada** — tipo declarado desde FND-10 §4.6, **primeira instancia**; nenhum tipo criado |
| **Comparacao por classe** | — | **1** — REV-INTERCLASSES §5 | **Justificada** — respondeu perguntas que nenhuma Carta responde sozinha, e produziu **C-6** |

**Regra aplicada:** abstracao com menos de dois membros e suspeita (AQ-03).

**Duas abstracoes continuam com zero membros — e mudam de estado, nao de contagem.** Sob a
**Correcao 1**, `PR-1` e `PR-2` deixam de ser lidas como *ociosas*: sao regras de **precedencia
em conflito**, e a ausencia de conflito em **quatro** Cartas esta **fora do dominio aplicavel**.
Continuam com **0** membros; deixam de ser contadas como falha.

**Resposta:** **nao** — e duas saem da suspeita **sem que nenhum numero tenha melhorado**, o que
esta declarado para que a reclassificacao nao seja lida como progresso.

## F4 — O sistema continua mais simples de evoluir do que antes?

| Mudanca-tipo | Antes | Depois | Aprovacoes |
|---|---|---|---|
| Saber se uma Carta esta **em vigor** | Nao havia Carta em vigor | `status` + `ratificacao` + fonte canonica do ato em `MSG-2026-0001` | Inalterado |
| Saber **o que muda de uma classe para outra** | **Nao havia fonte** — inferia-se de FND-02 §2.1 e §3 | REV-INTERCLASSES §5, com **universal × classe × acidental** separados | Inalterado |
| Saber quem aprova um `FIT` cujo objeto o aprovador produziu | Precedente isolado *(FIT-2026-003)*, sem regra legivel | `DEP-EXE §10, I-2`: impedimento, motivo e **substituto nomeado** | Inalterado |
| Saber se um pedido de contexto deve ser **devolvido** | Julgamento | `DEP-KMS §8.2`: criterio de devolucao declarado **antes** do pedido | Inalterado |
| Saber se um defeito e **incidente** ou **mudanca incompleta** | **Nao havia criterio** | CX-6: *violacao exige norma nomeavel* | Inalterado |
| Medir custo de secao de forma **reproduzivel por terceiro** | Metodo praticado, **nao escrito** | `DEP-KMS §13.2`: os tres passos, incluindo **remedir ate estabilizar** | Inalterado |
| Escrever uma Carta de Departamento | Template 1.1.0, checklist de 16 itens | Template **1.2.0**, checklist de **17** — com **B4 × B9** | **Inalterado** |

**Leitura.** Seis perguntas antes sem resposta verificavel passam a ter uma. **Nenhuma aprovacao
nova foi criada**; nenhum caminho de decisao ficou mais longo; **nenhum papel ganhou veto novo**.
A aprovacao de Carta de Departamento continua sendo a de FND-09 §8.2: o **SOBERANO**.

**Contrapartida:** o checklist ganhou **um** item, e ele existe porque **faltava** — IC-1.

**Resposta:** **sim**.

## F5 — A mudanca reduz ou aumenta o custo de contexto?

| Papel / tarefa-tipo | Antes | Depois | Direcao |
|---|---|---|---|
| Piso obrigatorio de qualquer tarefa | 1.099 linhas | **1.099 linhas** | **inalterado** |
| **Executar uma missao estrutural** | **30,6%** — 3a medicao | **18,5%** — 4a medicao | **desce** — 1a queda da serie |
| Saber se um departamento pode decidir ou aprovar algo | 111–115 linhas *(2 classes)* | **111 · 115 · 139 · 155** *(4 classes)* — mediana **127** | **estavel** |
| Saber o que muda entre classes | **Nao havia fonte** | **1** tabela — REV-INTERCLASSES §5.1 | **desce, a partir do indefinido** |
| Saber o estado de ratificacao de uma Carta | **Nao havia Carta em vigor** | **2 campos** de frontmatter, com fonte canonica referenciada | **desce** |
| Escrever uma Carta de Departamento | 2.347 linhas | **2.347 linhas** — pacote inalterado | **inalterado** |
| Acervo total | 26.506 | **28.966** | **sobe 9,3%** |

**Leitura honesta.** A serie observada e agora **23% · 33% · 30,6% · 18,5%**. **Esta e a primeira
medicao que desce de forma material** — **12,1 pontos** abaixo da anterior e **4,5 pontos** abaixo
da mais baixa ja registrada.

**O mecanismo esta identificado, e e parcialmente atribuivel.** Perguntas que na Missao 1.6
exigiram abrir FND-04, FND-05, FND-08 e quatro templates foram respondidas aqui pelo **recorte
de decisao** das Cartas — **111 a 155 linhas** em vez de documentos inteiros. E exatamente o
efeito que DC-10 pretendia.

**O que a medicao NAO autoriza a dizer.** Que a reducao esta comprovada. Parte da queda vem da
**natureza desta missao**, que exerceu um contrato existente em vez de construir um novo — e
comparar missoes de naturezas distintas foi precisamente a duvida amostral de R3 de FIT-2026-003.
**Um ponto de descida nao e tendencia**, e a serie ja subiu e desceu antes.

**Tratamento de R4 de FIT-2026-002** *(reducao calculada, nao observada)*: **mantida, com
progresso medido pela primeira vez**. O criterio de fechamento passa a exigir **duas descidas
consecutivas**, ou uma descida em missao de natureza **construtiva** — nao de exercicio. Fechar
com um ponto repetiria o erro que a Correcao 1 acabou de corrigir: **concluir a partir de uma
amostra cuja natureza nao foi controlada**.

**O que subiu:** o acervo, pelo sexto ciclo. **O que nao subiu:** o pacote de escrita de Carta,
**identico** ao da missao anterior — o contrato absorveu **duas classes novas sem custar uma
linha a mais** a quem escreve.

**Resposta:** **desceu** na missao medida — pela primeira vez; **subiu** no acervo, pelo sexto
ciclo. **→ Ressalva R3.**

## F6 — Ela favorece reutilizacao?

| Definicao produzida | Reutilizavel por | Especifica do caso? |
|---|---|---|
| **U-1 a U-9** — as nove propriedades universais de REV-INTERCLASSES §5.2 | **Qualquer** Carta de Departamento futura, nas cinco classes restantes | Nao |
| **C-6** — dois desenhos de impedimento *(protege o vizinho × protege o sistema do proprio)* | **Carta de Agente e de Subagente**, que tambem declaram autonomia e impedimento | Nao |
| **U-8** — recorte de decisao entre 29% e 32% | Expectativa verificavel na quinta Carta; **qualquer** artefato com recorte medido | Nao |
| Criterio *"violacao exige norma nomeavel"* (CX-6) | **Qualquer** duvida entre incidente e defeito | Nao |
| Regra de medicao autorreferente em tres passos (`DEP-KMS §13.2`) | **Qualquer** artefato que meca a propria extensao | Nao |
| Criterio de QG-5 *"a licao chegou ao registro-fonte"* | **Todo** encerramento de mudanca | Nao |
| Forma do registro de ato soberano (`MSG-2026-0001`) | **Todo** ato soberano futuro — e havera um por Carta | Nao |
| Correcoes 1 e 2 de medicao | **Toda** reconciliacao de ressalva | Nao — **mas exigem ADR para vincular** |
| A-1 a A-6 — as diferencas **acidentais** | — | **Sim** — descrevem o estado atual, nao a norma |

**Criterio:** DoD-8.

**Evidencia mais forte:** **as nove propriedades universais foram isoladas das especificas de
classe com quatro observacoes** — e a separacao permite que a quinta Carta seja verificada
contra U-1 a U-9 **antes** de ser escrita, em vez de julgada depois. **C-6** e o achado com maior
alcance: mostra que o contrato acomoda **dois desenhos distintos de impedimento** com a mesma
B9, sem regra especial de classe.

**Resposta:** **sim**, com as diferencas acidentais declaradas como tais.

---

## Ressalvas

| # | Ressalva | Custo assumido | **Dono** | **Gatilho de reavaliacao** |
|---|---|---|---|---|
| **R1** | **DEP-EXE e autor de 4 de 4 Cartas, e o contrato nunca foi testado contra autor distinto.** Nas quatro Cartas, **zero** itens de conteudo devolvidos; a unica devolucao veio do **instrumento** — o checklist incompleto de IC-1. **`PR-1` e `PR-2` seguem com 0 membros**, agora como `nao-avaliaveis` | Uma taxa de conformidade de 100% pode estar medindo a autoria. O contrato pode ser incapaz de **barrar** o que consegue **produzir**, e **IC-3** mostra que trocar o autor exige **C3** | **DEP-EXE** | **Primeira Carta escrita por autor distinto de DEP-EXE** — depende de IC-3 resolvido ou da existencia de agentes |
| **R2** | **Cinco de nove departamentos seguem sem Carta, e um deles e DEP-GOV** — revisor de **toda** Carta de Departamento e **unico escritor da camada EST**, papeis exercidos **quatro vezes** nesta missao sem Carta que os declare | Quatro Cartas apontam para um departamento cujos impedimentos **nao estao escritos**. O residuo de §4.2 de REV-INTERCLASSES **so desaparece** quando DEP-GOV tiver Carta | **DEP-EXE** | **Proxima Carta escrita** — e o achado **IC-4** recomenda que seja a de **DEP-GOV** |
| **R3** | **Sexta missao consecutiva de crescimento do acervo: +9,3%**, de 26.506 para **28.966** linhas | O acervo cresce ha seis ciclos. Diferente dos cinco anteriores, **a proposta de consolidacao foi aberta** — mas **nenhuma consolidacao foi executada** | **DEP-EXE** | **Encerramento da proposta EV-08** aberta em §Consolidacao. Se ela fechar sem nenhum artefato fundido, aposentado ou dividido, **escalar ao Soberano** |
| **R4** | **Duas Cartas ja ratificadas contem um defeito conhecido e nao corrigivel sem ato novo.** **IC-5** — a materia de I-6 da Carta de DEP-QAR nomeia apenas a Linha — foi encontrado **depois** da ratificacao | Corrigir exigiria **alterar texto ratificado**, que o ato de 2026-07-28 proibe expressamente. O defeito permanece **vivo e declarado** ate um ato novo. **E o primeiro caso do sistema em que a imutabilidade por ratificacao retem um defeito conhecido** | **DEP-EXE**; ato do **SOBERANO** | **Proxima emenda a Carta de DEP-QAR**, que exige ato novo — ou decisao do Soberano de que o defeito nao justifica emenda |

## Veredito

| Campo | Conteudo |
|---|---|
| Veredito | **`apto-com-ressalva`** |
| Fundamento | As seis perguntas tem sinal observavel. **Os dois primeiros artefatos em vigor do sistema existem**, sob ato soberano cuja condicao de eficacia foi verificada por **tres vias independentes**; o contrato passa de **2 para 4 classes** exercidas, fechando o limite **A2** declarado desde ADR-0011; **cinco** ressalvas e achados fecham com evidencia; **nenhuma regra nova foi criada**; e a validacao interclasses encontrou **dois defeitos que a intraclasse nao encontraria**. Em contrapartida, o autor segue sendo **o mesmo nas quatro Cartas**, **cinco** departamentos seguem sem Carta — inclusive o **revisor de todas** —, o acervo cresce pelo **sexto** ciclo, e uma Carta ja ratificada retem um defeito conhecido. Nao e `inapto` porque nenhuma dessas contrapartidas revela degradacao sem contrapartida verificavel |
| Efeito | **Encerra.** As quatro ressalvas viram divida declarada com dono e gatilho (FND-07 §9) |
| Data | 2026-07-28 |
| Executado por | **DEP-QAR** |
| Aprovado por | **DEP-GOV** — DEP-EXE impedido (CX-3, `DEP-EXE §10 I-2`) |
| Ratificado por | **Nao aplicavel** — objeto C2/Tipo 2 |

## Rollout das cinco Cartas restantes — **ADJUST**

| Campo | Conteudo |
|---|---|
| **Decisao** | **ADJUST** — o rollout prossegue, **nao** em lote |
| Por que nao **GO** | **(a)** O autor e o mesmo em 4 de 4 Cartas, e o contrato nunca foi testado contra autor distinto (R1). **(b)** **DEP-GOV**, revisor de toda Carta, nao tem Carta — e revisaria a propria (R2, IC-4). **(c)** O acervo cresce pelo sexto ciclo e a consolidacao **acaba de ser aberta**, sem resultado ainda (R3) |
| Por que nao **STOP** | Os oito cenarios resolveram **sem ambiguidade**; as quatro classes foram exercidas; os tres defeitos encontrados tem dono e gatilho e **um** foi corrigido; nenhuma norma foi violada; e os dois primeiros artefatos do sistema **entraram em vigor** por ato soberano regular |
| **Condicao 1** | A **quinta** Carta e a de **DEP-GOV**, escrita **sozinha**. E o unico departamento que exerce dois papeis criticos sem Carta, e o unico cuja ausencia produz residuo de segregacao em toda revisao (IC-4, R2) |
| **Condicao 2** | Na quinta Carta, medir **devolucoes de conteudo** — e verificar antes que o **checklist esteja integro**. IC-1 mostrou que zero devolucoes pode significar **regra ausente**, e nao regra frouxa |
| **Condicao 3** | **IC-2** *(colisao do termo "ratifica")* resolvido ou formalmente adiado antes que qualquer artefato registre *"ratificado por DEP-EXE"* |
| **Condicao 4** | A proposta **EV-08** aberta em §Consolidacao **encerrada com resultado** — executada ou recusada com fundamento — antes das quatro ultimas Cartas |
| Quem decide o rollout | **DEP-EXE**, com parecer de DEP-GOV; cada Carta e aprovada e ratificada pelo **SOBERANO** |

## Consolidacao — proposta EV-08 **aberta**

> **Ato exigido por R3 de FIT-2026-005**, cujo gatilho — *"se a sexta tambem crescer sem nenhuma
> consolidacao"* — **disparou**. Abrir a proposta e de **DEP-EXE** (`DEP-EXE §3, X-12`).
> **Esta missao abre a proposta e nao a executa:** fundir, aposentar ou dividir artefato tem
> rito proprio e esta fora do mandato desta missao.

| Campo | Conteudo |
|---|---|
| **Estado** | **ABERTA** — a primeira do sistema em seis ciclos |
| Fundamento | **PI-14 tem dois movimentos e so um esta sendo exercido.** Seis ciclos de especializacao, **zero** consolidacoes (`DEP-EXE §11, KX-8`) |
| **Candidatos, por antiguidade** | **(1)** As **13** ressalvas abertas, das quais **12** dependem da 1a ou 2a revisao estrutural — ver §Pendencias. **(2)** As **28** regras `CT` de ADR-0010, com **0** exercicios — **avaliacao suspensa** pela Correcao 2 ate `MEM-EST-0001` entrar em vigor. **(3)** As **duas** camadas de memoria com **zero** registros — PRD e TEC (`DEP-KMS §11, KK-5`). **(4)** Os **18** tipos documentais sem instancia |
| **Criterio de avaliacao** | **EV-08** — tipo, regra ou abstracao que atravesse **um horizonte inteiro** sem instancia. **Nenhum horizonte se fechou ainda**, e isso e o primeiro fato que a proposta precisa resolver |
| **Nao candidatos, e por que** | As regras `CT` **nao** podem ser avaliadas agora (Correcao 2). Os 18 tipos sem instancia **nao** disparam EV-08, que exige horizonte fechado. Consolidar por contagem, sem o gatilho, repetiria o erro que a Correcao 1 acabou de corrigir |
| **Dono** | **DEP-EXE**, com evidencia de DEP-KMS e parecer de DEP-QAR |
| **Prazo** | Encerramento antes das quatro ultimas Cartas (Condicao 4 do rollout) |

> **O resultado honesto e desconfortavel:** aberta a proposta, **os quatro candidatos mais
> obvios sao inavaliaveis ou nao elegiveis agora** — dois por criterio corrigido nesta mesma
> verificacao, dois por falta de horizonte fechado. **Isso nao invalida a abertura**; mostra que
> o gatilho de R3 media o crescimento sem verificar se havia **objeto consolidavel**. Registrado
> como componente de R3.

## Pendencias para o SOBERANO

> **Escaladas conforme as proprias ressalvas determinam.** Esta secao **informa e pergunta**;
> nao decide, nao presume e nao antecipa (LM-03, LM-06).

| # | Pendencia | Origem | Opcoes |
|---|---|---|---|
| **P1** | **A 1a revisao estrutural nao foi agendada em seis ciclos**, e ela e o gatilho de **12** ressalvas e achados abertos — de FIT-2026-001 R1/R3, FIT-2026-002 R1/R3, FIT-2026-003 R1/R2, e P2 a P8 do catalogo de Capabilities | **R5 de FIT-2026-005**, que determina escalar se nao for agendada | **(a)** Agendar a 1a revisao estrutural como proxima missao; **(b)** fixar o marco que a dispara — fim do 1o horizonte, N Cartas, ou outro; **(c)** manter sem agenda, assumindo que 12 itens permanecam parados |
| **P2** | **`MEM-EST-0001` permanece `aprovado` e nao vigente**, e o ato de 2026-07-28 **o exclui expressamente**. Enquanto isso, **28 regras `CT` e 3 abstracoes ficam `nao-avaliaveis`** — nem falhas nem aprovadas | **R4 de FIT-2026-004**, reescalada; **DR-2** | **(a)** Ratificar o registro; **(b)** recusa-lo, o que tornaria as 28 regras candidatas legitimas a EV-08; **(c)** manter pendente, assumindo que a divida siga suspensa por tempo indeterminado |
| **P3** | **`FIT-2026-001` e `FIT-2026-002` seguem com estado de ratificacao incorreto**, e o ato de 2026-07-28 tambem os exclui expressamente | **INC-2026-002 §7**, `contido` desde a Missao 1.4 | **(a)** Ratificar os dois; **(b)** declarar que `FIT` **nao** exige ratificacao — o que resolve tambem a ambiguidade G1/G2 e vira emenda a FND-10 §10.3 pelo rito; **(c)** manter pendente. **Recomendacao de DEP-GOV registrada em INC-2026-002 §7: opcao (b)** |
| **P4** | **A Carta de DEP-QAR, ja ratificada, contem o defeito IC-5**, encontrado depois do ato. Corrigi-lo exige alterar texto ratificado | **R4** desta verificacao | **(a)** Ato novo ratificando uma versao 1.1.0 corrigida; **(b)** declarar que o defeito nao justifica emenda, mantendo-o registrado; **(c)** manter pendente ate a proxima emenda por outro motivo |

> **P1 e P2 nao sao pedidos de aprovacao — sao pedidos de decisao sobre divida parada.** Doze
> itens dependem de um evento que seis ciclos nao produziram, e trinta e uma regras dependem de
> um registro que o proprio Soberano manteve fora do alcance do ato. Ambas as situacoes sao
> **legitimas**; nenhuma se resolve sozinha.

### Nota sobre FT-04 — vigilancia de complacencia

| Verificacao | Estado |
|---|---|
| Vereditos emitidos | **6** |
| Consecutivos `apto` **sem nenhuma ressalva** | **0** — os seis com ressalvas |
| `inapto` emitidos | **0** |
| Ressalvas anteriores **fechadas neste ciclo** | **2** — R2 e R4 de FIT-2026-005 |
| Achados de revisao **fechados neste ciclo** | **4** — DR-1, DR-2, DR-3, DR-5, DR-6 |
| Ressalvas **reclassificadas** sem melhora de numero | **2** — R1 e R2 de FIT-2026-004, agora `nao-avaliaveis` |
| Achados **novos** | **7** |

FT-04 exige tres `apto` **sem ressalva** para disparar; nao e o caso.

> **O alarme desta verificacao e novo, e aponta para ela propria.** Duas ressalvas mudaram de
> *falha aparente* para **`nao-avaliavel`** por uma correcao de criterio aplicada **na mesma
> verificacao que as reconcilia**. A correcao e legitima e foi determinada externamente — mas o
> mecanismo *"corrigir o criterio que me julga"* e exatamente o que PI-05 vigia. **Mitigacao
> aplicada:** o executor (DEP-QAR) nao propos as correcoes, o aprovador (DEP-GOV) nao as
> aplicou, e **§Regras de medicao declara explicitamente que a correcao nao melhora nenhum
> numero** — 28 regras seguem sem exercicio e 3 abstracoes seguem com zero membros.

Permanece o numero a vigiar: **nenhum `inapto` em seis oportunidades**. Registra-se como
observacao, nao como conclusao.

### Nota de conflito de interesse (PI-10)

| Campo | Conteudo |
|---|---|
| Conflitos identificados | **Dois.** **(1)** DEP-QAR e **objeto** de um dos pilotos ja ativos. **(2)** **DEP-GOV aprova** este parecer tendo **revisado** as quatro Cartas |
| Por que nao invalidam | **(1)** FT-02 exige que o executor **nao tenha produzido** o artefato avaliado; autor e **DEP-EXE**. **(2)** DEP-GOV **nao produziu** nenhum objeto avaliado e **nao e objeto** de nenhuma Carta |
| Desvios aplicados | Blocos B4, B9 e B12 da Carta **DEP-EXE** verificados por **DEP-QAR**; cenarios **CX-1** e **CX-3** executados por **DEP-GOV**; aprovacao transferida de DEP-EXE para DEP-GOV |
| Alternativa recusada | Escalar a aprovacao ao **SOBERANO** — recusada por proporcionalidade: objeto **C2/Tipo 2**, que FND-10 §10.3 nao submete ao Soberano. Escalar criaria precedente de levar parecer C2 a autoridade maxima |
| Residuo | DEP-GOV aprova documento que contem a verificacao do proprio trabalho de revisao. **Declarado em vez de omitido.** Desaparece quando DEP-GOV tiver Carta — achado **IC-4** |

## Aprendizado gerado

| Registro APR | Licao |
|---|---|
| [MEM-APR-0002](../../memory/aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md) | **Quarta confirmacao observada, com alcance ampliado por IC-1:** *declarar uma correcao aplicada* e da mesma familia de *reproduzir tabela* e de *declarar-se projecao sem ser*. O documento que **declara** nao e o documento que **carrega** o fato. **A ocorrencia deve chegar ao registro-fonte** — sob o criterio de QG-5 que `DEP-KMS §5.2` materializou |
| A gravar por DEP-KMS *(QG-5)* | **Validacao interclasses encontra o que a intraclasse nao encontra.** Oito cenarios em quatro classes produziram **dois** defeitos *(IC-4, IC-5)* que **exigem duas classes para aparecer**: um so e visivel quando Comando e Guarda sao lidos juntos; o outro, quando tres classes apontam para um departamento **sem Carta**. Acao: toda validacao de contrato que se aplique a mais de uma classe deve exercer **pares de classes**, nao instancias isoladas. Dono: DEP-QAR |
| A gravar por DEP-KMS *(QG-5)* | **Ratificacao congela o defeito junto com o acerto.** IC-5 foi encontrado **depois** do ato soberano, e corrigi-lo exigiria alterar texto ratificado. O custo da imutabilidade por ratificacao **nao e simetrico**: protege contra alteracao indevida e retem defeito conhecido. Acao: a revisao independente **antes** do ato precisa incluir a leitura cruzada entre Cartas, nao apenas a leitura de cada uma. Dono: DEP-EXE |

## Historico de vereditos sobre este objeto

| FIT | Data | Veredito | Relacao |
|---|---|---|---|
| FIT-2026-005 | 2026-07-28 | `apto-com-ressalva` | Contrato e **dois** pilotos, ambos `em-revisao` |
| **FIT-2026-006** | 2026-07-28 | **`apto-com-ressalva`** | **Supera a leitura** de R1 e R2 de FIT-2026-004 e de FIT-2026-005 quanto ao **criterio**, sem editar nenhum dos dois (M1, LV-04, FT-09) |
