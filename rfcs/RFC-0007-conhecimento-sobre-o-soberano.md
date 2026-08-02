---
id: RFC-0007-conhecimento-sobre-o-soberano
titulo: Como registrar conhecimento operacional sobre o Soberano sem transformar preferencia em norma?
tipo: rfc
versao: 1.0.0
status: aprovado
camada_memoria: nao-aplicavel
autor: DEP-KMS
proprietario: DEP-KMS
aprovador: DEP-EXE
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: null
decisoes_relacionadas: [ADR-0002, ADR-0006, ADR-0010]
substitui: []
substituido_por: null
classe_mudanca: C2
prazo_analise: 2026-07-28
resumo: Submete a analise onde registrar conhecimento operacional sobre o Soberano e sob que contrato, sem criar entidade nem elevar preferencia a norma.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# RFC-0007: Conhecimento operacional sobre o Soberano

## Proposito

Submeter a analise **onde** o conhecimento operacional sobre o Soberano deve viver e **sob que
contrato**, de modo que estruturas futuras compreendam visao, criterios, linguagem e forma de
trabalho — sem que biografia, preferencia ou inferencia adquiram forca normativa.

## Escopo

| Item | Definicao |
|---|---|
| **Inclui** | O instrumento que hospeda o contrato; a camada que hospeda o conhecimento; a fronteira de autoridade; as classes de evidencia; a minimizacao de dado pessoal; os perfis de carregamento; as regras de evolucao |
| **Nao inclui** | O **conteudo** do conhecimento — isso e a instancia, produzida sob o contrato; ratificacao de qualquer decisao pendente; criacao de agente, skill, clone, perfil psicologico ou Reasoning Framework; alteracao do termo oficial `SOBERANO` |
| **Subordinado a** | [FND-01](../foundation/01-constituicao.md), [FND-04](../foundation/04-governanca.md), [FND-06](../foundation/06-arquitetura-memoria.md), [FND-09](../foundation/09-meta-model.md), [FND-10](../foundation/10-artifact-framework.md) |

## Responsaveis

| Papel | Quem |
|---|---|
| Proponente | **DEP-KMS** — curador de todas as camadas de memoria (FND-06 §Responsaveis) |
| Areas que devem se manifestar | DEP-GOV (conformidade e dono da camada EST), DEP-QAR (risco, privacidade, independencia) |
| Aprovador | **DEP-EXE**, com parecer de DEP-GOV (FND-04 §2.1, C2) |
| Prazo de manifestacao | 2026-07-28 |

---

## 1. Situacao atual

### 1.1 O que ja existe

| Fato | Onde |
|---|---|
| O Soberano e entidade declarada, **E-02**, cardinalidade exatamente 1, sem atributos documentais | [FND-09 §5.1](../foundation/09-meta-model.md) |
| A camada **EST** ja e declarada como lar de *"restricoes permanentes impostas pelo Soberano"* e de *"padroes duraveis de preferencia do Soberano sobre como o trabalho e feito"* | [FND-06 §3.1](../foundation/06-arquitetura-memoria.md) |
| A camada EST tem **zero** registros formais, e o proprio indice declara que eles *"surgirao quando houver conhecimento estrategico fora"* da Fundacao e do catalogo de Capabilities | [`memory/estrategica/README.md`](../memory/estrategica/README.md) |
| `Fundador` e `Soberano` designam a mesma autoridade; o termo oficial e **`SOBERANO`** | [INC-2026-001 §7.1](../governance/incidents/INC-2026-001-ratificacao-inferida.md), [FND-10 §3.3](../foundation/10-artifact-framework.md) |
| Memoria **nao tem autoridade normativa**: informa, nao obriga; em conflito com ADR vigente, o ADR vence | [FND-09 §5.7, E-20](../foundation/09-meta-model.md); MM-07 |
| "Founder Context" foi explicitamente **nao criado** na Missao 1.4, e o fato foi verificado | [REV-CONSOLIDACAO §1.1](../foundation/revisao-arquitetural-consolidacao-2026-07-28.md) |

### 1.2 O que nao existe

Nenhum artefato registra o que o Soberano decidiu, prefere, recusa ou considera qualidade —
**exceto** de forma dispersa, dentro de instrumentos cujo objeto e outro: evidencias de ADR,
seções de incidente, notas de revisao. Nao ha contrato que diga o que pode ser registrado, com
que evidencia, com que autoridade, por quanto tempo e sob que acesso.

## 2. Problema

**Estruturas futuras vao precisar de criterio, e nao ha lugar legitimo de onde retira-lo.**

Sem contrato, restam dois caminhos, ambos ja demonstradamente ruins:

| Caminho | O que produz | Evidencia de que e ruim |
|---|---|---|
| **Inferir** o criterio do Soberano a partir do que ele instruiu antes | Autoridade construida por proximidade e precedente | [INC-2026-001](../governance/incidents/INC-2026-001-ratificacao-inferida.md): quatro decisoes C3/Tipo 1 trataram **instrucao generica anterior** como ato de autoridade. Severidade alta, violacao de LV-05 |
| **Ignorar** o criterio e pedir direcao a cada passo | Microgestao — a negacao direta da Visao **V1** | [FND-01 §2](../foundation/01-constituicao.md), V1: *"uma intencao bem formulada e condicao suficiente para que a organizacao produza um resultado entregavel, sem microgestao"* |

O problema nao e teorico: **o acervo ja converteu instrucao em autoridade uma vez**, e a causa
corrigida (CV-09, LM-02) trata do **ato de ratificacao** — nao do conhecimento difuso sobre
criterios, que continua sem instrumento.

**Consequencia de nao agir:** o primeiro agente criado herdara criterio por inferencia, sob
pressao de um caso concreto — a mesma ordem de eventos que ADR-0007 recusou para a fronteira
com o Legacy.

## 3. Pergunta de decisao

**Onde deve viver o conhecimento operacional sobre o Soberano, e sob que contrato, para que
oriente escolhas sem nunca obrigar?**

## 4. Criterios de avaliacao

> Declarados antes do exame das opcoes (CD-01, VD-02).

| # | Criterio | Peso | Como se mede |
|---|---|---|---|
| C1 | **Conhecimento sobre o Soberano nunca adquire forca normativa** | **Bloqueante** | Nao existe caminho pelo qual o registro supere Constituicao, Governanca, ADR vigente, evidencia ou seguranca — e a subordinacao e **estrutural**, nao apenas declarada |
| C2 | **Nenhuma entidade, arquetipo, relacao, tipo documental ou camada nova** | **Bloqueante** | 21 entidades · 10 relacoes · 33 tipos · 5 camadas — inalterados. Candidata submetida ao Teste de Entidade (§9) |
| C3 | **Abstracao proporcional a evidencia** | **Bloqueante** | Nenhum artefato normativo novo e criado para dominio com **zero instancias anteriores** (SE-01, SE-02, FND-08 §7.1, AQ-03) |
| C4 | Toda afirmacao rastreavel | Alto | 100% das afirmacoes com fonte, data, classe de evidencia e confianca; ausencia de evidencia registrada como `unknown` |
| C5 | Carregamento minimo por padrao | Alto | Perfis declarados com custo **medido**; carregamento integral proibido (CE-01, CE-02) |
| C6 | Reversivel | Medio | Desfazer nao destroi registro, nao exige migracao e nao toca artefato de terceiros |

## 5. Opcoes

### Opcao A — Contrato por ADR (C2) + instancia na camada EST

| Campo | Conteudo |
|---|---|
| Descricao | Um **ADR** institui o contrato — finalidade, autoridade, custodia, consumidores, acesso, ciclo, limites, classes de evidencia, privacidade, perfis e evolucao. O **conhecimento** vive como registro `MEM-EST` em `memory/estrategica/`, sob `TPL-memoria`. FND-06 §3.1 recebe emenda MENOR remetendo ao contrato; FND-03 §8 recebe o termo oficial |
| A favor | **C1 sai de graca e e estrutural**: `MEM` ja tem autoridade normativa **nenhuma** por declaracao do Meta Model (E-20) e perde para o ADR em conflito (MM-07). Nao se inventa subordinacao — herda-se. **C3**: zero artefato normativo novo; reusa ADR, `MEM`, `TPL-memoria` e a camada que **ja** declara este conteudo como seu. Precedente direto: ADR-0007 instituiu FR-01 a FR-10 e ADR-0008 instituiu PJ-01 a PJ-06, ambos regimes inteiros por ADR C2 |
| Contra | O contrato fica em artefato **M1**, imutavel: evoluir exige ADR que o supere. Um leitor que procure "o framework" em `foundation/` nao o encontra ali |
| Custo / Risco | Custo: 1 ADR, 1 registro `MEM-EST`, 2 emendas MENOR, 1 termo de vocabulario. Risco: M1 tornar a evolucao mais cara que o previsto |
| Quem e afetado | DEP-KMS (curadoria), DEP-GOV (camada EST e conformidade), DEP-QAR (privacidade), consumidores futuros |
| Avaliacao | C1 ✔ · C2 ✔ · C3 ✔ · C4 ✔ · C5 ✔ · C6 ✔ |

### Opcao B — Criar **FND-11**, Framework de Conhecimento sobre o Soberano

| Campo | Conteudo |
|---|---|
| Descricao | Decimo primeiro documento fundacional, hospedando o contrato; a instancia continuaria em `MEM-EST` |
| A favor | E o que o enunciado da missao sugere ao pedir "o framework". Documento **M2**, versionavel — evolui por emenda, nao por superacao. Fica onde um leitor procuraria |
| Contra | **Falha em C3.** Criar o 11o documento fundacional para um dominio com **zero instancias anteriores** e abstracao antecipada — exatamente o defeito ja registrado como divida em [FIT-2026-003 R2](../governance/fitness/FIT-2026-003-consolidacao-baseline.md) *(portao e classificacoes com zero membros)* e vedado por SE-01, SE-02 e FND-08 §7.1. **Tensiona C1**: FND ocupa o **nivel 2** da hierarquia de FND-01 §10, **acima dos ADRs** — hospedar o regime do conhecimento sobre o Soberano em instrumento de nivel superior ao ADR e o oposto estrutural do que o proprio contrato precisa declarar |
| Custo / Risco | Criar FND e **C3 com ratificacao** (FND-09 §5.2, E-03): exige RFC, analise de impacto, ADR, ato explicito do Soberano e emenda de FND-01 §10. Como esta missao **nao ratifica** nada, o framework nasceria em `aprovado` e **nao entraria em vigor** (LM-02) — junto com a instancia que dele dependesse |
| Quem e afetado | FND-01 (hierarquia), FND-03, catalogo, indices, nucleo obrigatorio |
| Avaliacao | C1 **tensiona** · C2 ✔ · C3 **falha** · C4 ✔ · C5 ✔ · C6 **falha** *(reverter exige remover documento fundacional e re-emendar FND-01)* |

### Opcao C — Emendar FND-06 com secao propria

| Campo | Conteudo |
|---|---|
| Descricao | O contrato vira uma secao nova de FND-06, ao lado das cinco camadas |
| A favor | Nenhum artefato novo; mudanca **C2**; fica junto da camada que hospeda o conteudo. Genuinamente o concorrente mais proximo da Opcao A |
| Contra | **Distorce o escopo declarado de FND-06**, que e *"as 5 camadas, criterio de alocacao, formato do registro, ciclo de vida, promocao e rebaixamento, expiracao, resolucao de conflito, recuperacao, higiene e curadoria"* — arquitetura **transversal**, nao contrato de um assunto. Um regime especifico de dominio dentro dele e o caso literal de FND-10 §9.3: *"nao cabe em nenhum existente sem distorce-lo"*. Alem disso, acresce ~120 linhas a um artefato de 517, contra CE-05, e coloca o regime no **nivel 2** da hierarquia — a mesma tensao de C1 da Opcao B |
| Custo / Risco | Custo baixo em arquivos, alto em coerencia. Risco: FND-06 vira o lugar onde cabe o que nao coube em outro lugar |
| Quem e afetado | FND-06 e todo consumidor da arquitetura de memoria |
| Avaliacao | C1 **tensiona** · C2 ✔ · C3 ✔ · C4 ✔ · C5 ✔ · C6 ✔ |

### Opcao Z — Nao fazer nada

| Campo | Conteudo |
|---|---|
| Consequencia de manter o estado atual | O conhecimento sobre criterios do Soberano continua disperso em instrumentos cujo objeto e outro, sem classe de evidencia, sem confianca declarada e sem regra de acesso |
| Custo da inacao | Nao e hipotetico. O acervo **ja** produziu, uma vez, autoridade a partir de instrucao generica ([INC-2026-001](../governance/incidents/INC-2026-001-ratificacao-inferida.md), severidade alta). O primeiro agente criado enfrentara a mesma lacuna, com o mesmo incentivo, e sem instrumento — a diferenca e que dessa vez o defeito ja e **conhecido** |
| Por que nao vence | Manter a lacuna depois de a ter observado e diferente de nunca a ter visto. LV-11 trata omissao de violacao observada como violacao; a analogia nao e literal, mas a logica e a mesma: o custo de nao agir passou a ser escolha |

## 6. Recomendacao do proponente

**Opcao A.**

Ela vence pelos tres criterios bloqueantes, e vence por uma razao que as outras duas nao podem
imitar: **a subordinacao do conhecimento a norma nao precisa ser escrita — ela e herdada.**
`MEM` tem autoridade normativa nenhuma por declaracao do Meta Model, e perde para o ADR em
conflito. As Opcoes B e C precisariam **declarar** essa subordinacao dentro de um instrumento
que, pela hierarquia de FND-01 §10, esta acima dos ADRs — pedindo a norma que se autolimite,
em vez de estruturar o registro onde o limite ja existe.

A objecao legitima a A e a imutabilidade M1 do contrato. Aceita-se: um regime que ainda nao
tem instancia nenhuma **deve** ser caro de mudar por emenda e barato de substituir por inteiro,
porque a probabilidade de estar parcialmente errado e alta. Quando houver evidencia de reuso —
segunda instancia, segundo consumidor ou custo de recuperacao observado —, a promocao a FND-11
passa a ter sinal, e a Opcao B deixa de ser antecipacao para ser especializacao (§7).

## 7. Impacto previsto

| Dimensao | Impacto |
|---|---|
| Departamentos | DEP-KMS (curadoria e captura); DEP-GOV (dono da camada EST, conformidade, acesso); DEP-QAR (privacidade, independencia, verificacao) |
| Componentes | **Nenhum** — nao existe componente, e nenhum e criado |
| Normas afetadas | [FND-06 §3.1](../foundation/06-arquitetura-memoria.md) MENOR *(remissao ao contrato)*; [FND-03 §8](../foundation/03-taxonomia.md) MENOR *(termo oficial)* |
| Camadas de memoria | **EST** recebe seu primeiro registro formal — previsto pelo proprio indice da camada |
| Entidades · relacoes · tipos · camadas novas | **Zero · zero · zero · zero** |
| Ganho PI-14 pretendido e sinal que o comprova | **Reducao de contexto.** Sinal a comprovar: uma missao futura carrega **um perfil**, nao o registro inteiro, e o custo do perfil e medido em linhas. Sinal ja observado que motiva a proposta: a lacuna produziu, uma vez, autoridade por inferencia (INC-2026-001) |
| Gatilho declarado de promocao a FND-11 | Qualquer um: **(a)** segunda instancia `MEM-EST` sobre o Soberano; **(b)** segundo consumidor formal do contrato alem da camada EST; **(c)** custo de recuperacao observado — o registro ser aberto repetidamente so por uma fracao (sinal **S5** de FND-10 §9.2) |

## 8. Riscos

| # | Risco | Impacto | Mitigacao |
|---|---|---|---|
| R1 | **Registro sobre uma pessoa virar norma na pratica**, mesmo sem autoridade formal | **Alto** | Autoridade nenhuma e **estrutural** (E-20, MM-07), nao declarativa; cada afirmacao carrega classe e confianca; o contrato exige escalonamento em conflito |
| R2 | **Inferencia disfarcada de fato** — preencher lacuna com o que "faz sentido" | **Alto** | Classe `unknown` obrigatoria onde falta evidencia; `inferred` nunca vira preferencia oficial sem confirmacao explicita; LV-12 se aplica integralmente |
| R3 | **Dado pessoal indevido** entrar no acervo | **Alto** | Lista fechada de conteudo proibido; classificacao de sensibilidade por afirmacao; PI-08 e MM-10 valem integralmente |
| R4 | O contrato em M1 tornar a evolucao cara | Medio | Aceito e declarado (§6). Superar um ADR e rito conhecido (FND-07 §7); o gatilho de promocao a FND-11 e o caminho previsto |
| R5 | O registro envelhecer sem ninguem notar | Medio | Gatilho de revisao **por afirmacao**, nao so por artefato; `ttl` declarado; poda de nao recuperados (RC-05) |
| R6 | **Fonte fora do acervo** ser tratada como aprovada sem que o Soberano a tenha aprovado | **Alto** | Cada afirmacao declara a fonte **e** se ela e interna ao acervo; o contrato preve **retirada** por ato do Soberano, e afirmacao de fonte externa e a primeira candidata |
| R7 | Esta proposta estar errada quanto ao instrumento | Baixo | Reversao trivial; gatilho de promocao declarado; a Opcao B continua disponivel, e passa a ter sinal em vez de hipotese |

## 9. Perguntas em aberto

### 9.1 "Contexto do Soberano" e entidade nova? — **Teste de Entidade (FND-09 §11.1)**

Submetido conforme determinacao da missao. **Uma negativa encerra a analise** e indica onde a
candidata pertence.

| # | Pergunta | Resposta | Consequencia |
|---|---|---|---|
| TE-1 | Responde a uma pergunta que **nenhuma** entidade existente responde? | **Nao** — `MEM` responde exatamente *"conhecimento organizacional persistente em uma camada, com proveniencia"* | **Encerra.** E duplicata (MT-02): reusar `MEM` |
| TE-2 | Persiste alem do ato que a criou, com identidade propria? | Sim | *(analise ja encerrada em TE-1)* |
| TE-3 | Tem dono unico e ciclo de vida proprios? | Sim, mas **identicos aos de `MEM-EST`**: dono DEP-GOV, curador DEP-KMS, TTL permanente | Reforca TE-1 |
| TE-4 | Pode ser instanciada mais de uma vez, com o mesmo formato? | **Nao** — o Soberano tem cardinalidade **exatamente 1** (FND-09 §5.1, E-02) | Segunda negativa: e instancia singular, nao tipo |
| TE-5 | Tem ao menos uma relacao valida de §6.1 com entidade existente? | Sim — **R-09 `registra`**, `MEM` → `SOBERANO` | — |
| TE-6 | Continua fazendo sentido se todas as instancias atuais desaparecerem? | **Nao** — descreve um caso concreto e unico | Terceira negativa |
| TE-7 | Ha sinal ja observado que a justifica? | Sim, para o **conhecimento**; **nao** para a entidade | — |

> **Resultado: reprovada em TE-1, TE-4 e TE-6.** `Contexto do Soberano` **nao e entidade**: e
> **conteudo** de um registro `MEM` na camada EST, e o nome e **termo de vocabulario**
> (FND-03 §8), como `Soberano`, `Portao` e `LucaX Legacy`. Nenhuma entidade nula e introduzida
> (MT-01). Pela escada de FND-09 §11.2, a proposta nao sobe nenhum degrau: nao cria atributo
> obrigatorio, eixo, relacao, arquetipo nem entidade.

### 9.2 Demais perguntas

| # | Pergunta | Estado |
|---|---|---|
| Q1 | Declaracao do Soberano feita **fora do acervo** — instrucao permanente ao ambiente de execucao — pode ser fonte? | **Respondida com limite declarado.** Pode ser fonte de **evidencia**, nunca de norma: FND-01 §10 situa instrucao e prompt no **nivel 8**, o mais baixo da hierarquia, e FR-04 admite observacao como evidencia com origem declarada. O contrato exige que a afirmacao declare a fonte como externa ao acervo e a submete a **retirada** por ato do Soberano |
| Q2 | O registro precisa de template proprio? | **Nao.** FND-10 §10.2, teste **T3**: o tipo precisa ter ocorrido ao menos **duas** vezes. Ha uma. Usa-se `TPL-memoria` |
| Q3 | Um registro so, ou um por categoria de conhecimento? | **Um so.** Dividir exige **≥ 2 sinais observados** (SE-02); ha zero. Os perfis de carregamento resolvem o custo por **recorte de secoes** — mecanismo ja usado para FND-09 e FND-10 no nucleo obrigatorio |
| Q4 | Quem confirma que o registrado e verdadeiro? | **Somente o Soberano**, e apenas ele pode converter `inferred` em preferencia oficial. Nenhum papel infere no lugar dele (PI-01) |

## 10. Manifestacoes

| Area | Posicao | Fundamento | Data |
|---|---|---|---|
| **DEP-GOV** | **Apoia** | A camada EST ja declara este conteudo como seu desde FND-06 v1.0.0; a Opcao A e a unica que nao cria norma nova para hospedar o que ja tem lugar. Registra objecao parcial: o contrato em M1 exigira superacao para evoluir | 2026-07-28 |
| **DEP-QAR** | **Apoia, com condicao** | C1 so e satisfeito porque `MEM` tem autoridade nenhuma por desenho. **Condicao:** o contrato deve tratar privacidade com lista **fechada** de conteudo proibido, e nao com principio geral — principio geral nao e conferivel sem julgar merito | 2026-07-28 |
| **DEP-KMS** | **Propoe** | — | 2026-07-28 |
| **DEP-EXE** | **Apoia** | A Opcao B entrega um framework que **nao entra em vigor** nesta missao, por depender de ato soberano que a missao expressamente nao produz. Entregar norma inaplicavel e pior que entregar regime aplicavel de menor pretensao | 2026-07-28 |

## 11. Resultado

| Campo | Conteudo |
|---|---|
| Decisao | **Aceita** — Opcao A, com a condicao de DEP-QAR incorporada *(lista fechada de conteudo proibido)* |
| ADR gerado | [ADR-0010](../decisions/ADR-0010-contrato-de-conhecimento-do-soberano.md) |
| Se rejeitada, por que | Nao se aplica |
| Se adiada, ate quando e sob qual condicao | Nao se aplica |
| Data | 2026-07-28 |
| Responsavel | DEP-EXE, com parecer de DEP-GOV |

---

## Linhagem

| Campo | Conteudo |
|---|---|
| Origem | Determinacao do Soberano na abertura da **Missao 1.5** |
| Deriva de | [FND-06 §3.1](../foundation/06-arquitetura-memoria.md) *(a camada EST ja declara este conteudo como seu)*; [FND-09 §5.7](../foundation/09-meta-model.md) *(autoridade de `MEM`)* |
| Gera | [ADR-0010](../decisions/ADR-0010-contrato-de-conhecimento-do-soberano.md) |
| Gatilho de ativacao | Necessidade de registrar criterio do Soberano de forma rastreavel, antes que uma estrutura futura o infira |
| Dependencias minimas | FND-06 §3.1 e §4, FND-09 §5.7 e §11.1, FND-10 §8 |

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-KMS | Proposta inicial: tres opcoes reais e a opcao nula, seis criterios declarados antes das opcoes, Teste de Entidade aplicado e reprovado em TE-1/TE-4/TE-6, recomendacao pela Opcao A. |
