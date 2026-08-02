---
id: REV-META-2026-07-28
titulo: Revisao Arquitetural do Enterprise Meta Model
tipo: relatorio
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-QAR
proprietario: DEP-QAR
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0003, ADR-0004]
substitui: []
substituido_por: null
---

# Revisao Arquitetural do Enterprise Meta Model

## Proposito
Submeter o Meta Model (FND-09) a exame critico e independente, respondendo as oito perguntas
obrigatorias da missao e registrando cada achado com severidade, gatilho e correcao proposta.

## Escopo
| Item | Definicao |
|---|---|
| Inclui | Duplicacao, generalidade, abstracao, circularidade, dependencia proibida, capacidade de crescimento, entidades removiveis, candidatas a norma constitucional |
| Nao inclui | Aptidao evolutiva — isso e objeto do Fitness Check [FIT-2026-001](../governance/fitness/FIT-2026-001-meta-model.md); merito de cada entidade isolada; criacao de instancias |
| Metodo | Confronto de FND-09 com FND-01 a FND-08, com o catalogo de Capabilities e com o Teste de Entidade TE-1 a TE-7 aplicado as 21 entidades e as 13 recusas |

## Responsaveis
| Papel | Responsavel |
|---|---|
| Executa a revisao | DEP-QAR *(independente de DEP-GOV, que propos o Meta Model — PI-05)* |
| Conformidade | DEP-GOV |
| Merito estrutural | DEP-EXE |
| Decide sobre os achados | SOBERANO |

---

## Sumario dos achados

| # | Achado | Severidade | Acao |
|---|---|---|---|
| M1 | `CAP-governanca` declara verificar **todas** as Capabilities — inclusive a si propria: autoverificacao formal | **Alta** | Corrigir leitura no catalogo; verificacao de DEP-GOV cabe a DEP-QAR |
| M2 | 13 das 21 entidades **nao tem nenhuma instancia**: o Meta Model e declarado, nao comprovado | **Alta** *(esperada)* | Aceito para a fase; gatilho EV-08 armado |
| M3 | `ORG` e `SOBERANO` sao entidades de instancia unica e sem artefato proprio — tensionam TE-4 | Media | Mantidas com justificativa; reavaliar na 1a revisao estrutural |
| M4 | Arquetipo A2 ARTEFATO reune 19 de 21 entidades — pouco discriminante | Media | Monitorar; consolidar se nunca for usado para discriminar |
| M5 | `AGT` × `SUB` e a fronteira mais fina do modelo | Media | Gatilho de fusao declarado |
| M6 | Universo fechado pode gerar excecao formal recorrente como via de escape | Media | Metrica de vigilancia definida |
| M7 | `SKL` × `WFL`: workflow de etapa unica e, de fato, uma Skill | Baixa | Regra de desempate proposta |
| M8 | As 13 recusas concentram risco em `Policy` e `Standard` | Baixa | Gatilho e porta de entrada ja nomeados |

**Correcoes aplicadas durante esta revisao:** tres divergencias internas foram detectadas e
corrigidas antes da aprovacao — §0 abaixo.

---

## 0. Divergencias corrigidas durante a revisao

| # | Divergencia detectada | Correcao aplicada |
|---|---|---|
| D1 | Os blocos de §5 usavam **38 verbos de relacionamento**, contra as 10 relacoes oficiais de §6.1 — violando a propria RM-02, que declara nula relacao fora dos pares permitidos | Acrescentada §6.1.1 "Verbos de leitura": tabela exaustiva mapeando cada verbo a uma das 10 relacoes, e separando os que sao **atos de autoridade** (§8) e nao relacoes estruturais |
| D2 | §9.4 justificava apenas `custodia` como nao-dependencia. **Autoria, execucao e ratificacao** ligam igualmente estrato alto a estrato baixo e violariam PD-11 se lidas como dependencia — a entidade `FIT` (estrato 1) e executada por DEP-QAR (estrato 3) | §9.4 generalizada: quatro vinculos de responsabilidade declarados, com criterio unico — se o destino desaparecer e a origem continuar valendo, o vinculo nao e dependencia |
| D3 | O bloco de `WFL` listava `atravessa QG` entre relacionamentos validos, tratando **portao como entidade** — o que contraria MT-01, ja que QG nao consta de §5 | Substituido por referencia ao atributo `portoes`, com nota explicita de que portao nao e entidade |

> As tres seriam invisiveis a auditoria de conformidade vigente: nenhuma verifica coerencia
> **interna** de um documento normativo. Registrado como sinal para a auditoria de coerencia
> normativa de FND-04 §8.

---

## 1. Existe entidade duplicada?

**Nao — nenhuma duplicacao de definicao. Tres pares exigiram exame individual.**

### 1.1 Metodo
Aplicado MT-02 a todos os 210 pares possiveis entre as 21 entidades: *duas entidades que
respondem a mesma pergunta sao a mesma entidade com dois nomes* (LX-07). Tres pares nao se
resolveram por leitura direta.

### 1.2 `AGT` × `SUB` — achado M5

| Aspecto | Agente | Subagente |
|---|---|---|
| Pergunta | Que papel executa isto? | Que recorte deste papel pode ser isolado? |
| Existencia | Autonoma dentro do departamento | **Nao existe sem o pai** (R-01) |
| Autonomia | Ate a do departamento | Sempre ≤ a do pai |
| Comunicacao | Cinco canais, com qualquer area | So com o agente pai (AG-04) |

**Por que a separacao se sustenta hoje:** as duas falham de formas diferentes. Agente mal
desenhado produz papel com fronteira errada; subagente mal desenhado produz contexto
carregado a toa. E o subagente existe precisamente para materializar o terceiro ganho de
PI-14 — reducao de contexto —, que nao teria instrumento se fosse apenas um atributo.

**Risco residual:** se todo agente vier a ter exatamente um subagente, a distincao vira
nominal.

**Gatilho de fusao declarado:** apos os cinco primeiros agentes, se **nenhum** subagente
tiver sido criado, ou se a razao subagente/agente for 1:1, propor que `SUB` deixe de ser
entidade e passe a atributo `escopo_reduzido` de `AGT` (rito de EV-05).

### 1.3 `SKL` × `WFL` — achado M7

| Aspecto | Skill | Workflow |
|---|---|---|
| Pergunta | Como se faz isto? | Em que ordem, por quem, com que portoes? |
| Atravessa departamentos | Nao necessariamente | Frequentemente — e declara o dono do resultado |
| Portoes | Nao possui | Declara `portoes` |

**Risco real:** um workflow de **uma unica etapa**, sem portao e sem travessia de area, e
indistinguivel de uma Skill. Nada no modelo impede que seja criado.

**Regra de desempate proposta** (C1, para a proxima revisao de FND-09): *sequencia com uma
unica etapa, sem portao e sem travessia de departamento, e Skill — nao Workflow.* Recusada
por DEP-GOV na aprovacao, se proposta como Workflow.

### 1.4 `FND` × `ADR`

| Aspecto | Norma Fundacional | Decisao |
|---|---|---|
| Pergunta | O que obriga permanentemente? | O que foi escolhido, e por que? |
| Mutabilidade | Emendada por versao | **Imutavel**; superada, nunca editada |
| Perfil de ciclo de vida | P1 normativo | P2 instrumento |

Sao entidades distintas por natureza, nao por convencao: a primeira e continua, a segunda e
pontual. **Sem duplicacao.**

### 1.5 Duplicacao com a Fundacao (criterio bloqueante C4 de ADR-0003)

| Conceito | Onde ja estava definido | Como FND-09 evita duplicar |
|---|---|---|
| Estados e transicoes | FND-03 §5 e §5.1 | §7.1 **reproduz o grafo por referencia** e declara que nao redefine; acrescenta apenas perfis que **restringem**, nunca ampliam |
| Relacoes entre Capabilities | FND-08 §5.1 | §6.1 incorpora por referencia, com nota explicita |
| Classes de mudanca | FND-04 §2 | Citadas por nome; nenhuma tabela de classes reproduzida |
| Niveis de autonomia | FND-01 §7.2 | Citados como eixo ortogonal; valores nao redefinidos |
| Autoridade por materia | FND-01 §7.3, FND-04, FND-08 §6.3 | §8.2 e **derivacao**, com regra declarada de que em conflito prevalece a origem e o conflito e erro do Meta Model |

**Verificacao aplicada:** FND-09 nao contem tabela de classes de mudanca, de camadas de
memoria, de portoes ou de dominios de Capability. MM-01 preservado.

---

## 2. Existe entidade generica demais?

**Duas merecem registro. Nenhuma exige divisao agora.**

### 2.1 `MEM` — a de maior amplitude aparente
Cobre cinco camadas com donos, volatilidades e TTLs distintos. Pelo criterio "e invocada por
motivos que nao se parecem entre si", pareceria candidata a divisao.

**Por que nao se divide:** ela **ja e particionada internamente**, por norma anterior. MI-01
de FND-06 determina que a sub-particao ocorra **dentro** da camada, nunca criando uma sexta.
Transformar cada camada em entidade produziria cinco entidades onde a arquitetura de memoria
exige exatamente uma com cinco divisoes — e quebraria MI-M09.

E o mesmo argumento aceito para `CAP-conhecimento` na revisao anterior: fan-out estrutural,
nao acidental.

### 2.2 `TOL` — ampliada nesta decisao
Passou a incluir a classe `modelo`, absorvendo a candidata `Model`. Cobre agora MCP, API,
SaaS, recurso local, fonte de dados e modelo de IA.

**Analise:** a ficha exigida — finalidade, dado trafegado, custo, criticidade, dependencia,
alternativa avaliada, criterio de descarte — e **identica** para as seis classes. Enquanto os
atributos nao divergirem, a amplitude e nominal, nao estrutural.

**Gatilho de especializacao declarado:** se a avaliacao de modelo passar a exigir atributos
que as demais classes nao usam — por exemplo, criterio de avaliacao de saida ou calibracao —
extrai-se `modelo` como entidade propria, pelo rito de §11.1.

### 2.3 Verificacao nas demais
Aplicado o teste de escopo heterogeneo as 21 entidades: **19 passaram sem ressalva.** As duas
acima ficam sob observacao com gatilho declarado.

---

## 3. Alguma entidade deveria ser abstraida?

**Sim — quatro ja foram, e o resultado esta correto. Duas abstracoes merecem vigilancia.**

### 3.1 Abstracoes realizadas
| Candidata | Virou | Justificativa |
|---|---|---|
| `Artifact` | Arquetipo A2 | Nada e "um artefato" sem ser tambem outra coisa (MT-02) |
| `Policy` + `Standard` | Nenhuma entidade; slot `Norma Derivada` nomeado | Sem sinal observado, criar seria antecipacao (FND-08 §7.1) |
| `Metric` | Atributo da entidade que mede | Entidade produziria 111 artefatos e separaria o indicador do que ele mede |
| `Model` | Classe de `TOL` | Satisfaz integralmente a ficha existente |

### 3.2 Achado M4 — o arquetipo A2 e pouco discriminante
`ARTEFATO` reune **19 das 21 entidades**. Um arquetipo que abrange 90% do universo classifica
pouco: excluir apenas `ORG` e `SOBERANO` poderia ser feito por uma frase, sem abstracao.

**Contra-argumento aceito:** A2 nao existe para discriminar, e sim para **carregar** as
regras de frontmatter, estado, versionamento e localizacao uma unica vez, em vez de
dezenove. AQ-04 e o proposito declarado, e ele se cumpre.

**Recomendacao:** manter, e verificar na primeira revisao estrutural se A2 foi alguma vez
invocado para **decidir** algo. Se nunca, converte-se em regra geral e o arquetipo e
consolidado (EV-08).

### 3.3 Achado M3 — `ORG` e `SOBERANO` tensionam o proprio Teste de Entidade
TE-4 exige que uma entidade possa ser instanciada **mais de uma vez**. As duas tem
cardinalidade fixa em 1, e nenhuma possui artefato proprio: a Organizacao e materializada
pela Constituicao, e o Soberano antecede qualquer documento.

Pelo criterio literal, seriam atributos de FND-01, nao entidades.

**Por que foram mantidas:** o Authority Model precisa do Soberano como **sujeito** de
relacao — sem ele, a cadeia de AU-10 nao tem termino declarado —, e o grafo de contencao
precisa de raiz. Remove-las tornaria §8 e §6.2 incompletos.

**Ressalva registrada (PI-10):** a manutencao e uma **excecao consciente a TE-4**, e nao uma
aplicacao dele. O Meta Model deveria dize-lo no proprio TE-4.

**Correcao proposta** (C1, proxima revisao de FND-09): acrescentar a TE-4 a ressalva
*"salvo entidade de estrato 0, cuja cardinalidade unica e propriedade da arquitetura, nao
defeito de tipagem"*.

---

## 4. Existe relacionamento circular?

**Nao em relacoes que o proibem. Sim — e desejavel — nas que o admitem.**

### 4.1 `contem` (R-01) — ordem topologica verificada

```
NIVEL 0   ORG
NIVEL 1   DEP  <- ORG          PRO  <- ORG          CAP  <- ORG
NIVEL 2   AGT  <- DEP          SPC  <- PRO
NIVEL 3   SUB  <- AGT
```

Tres niveis, sem retorno. **Sem ciclo.** Profundidade maxima de `SUB` confirmada em 1
(IV-04, MI-M04).

### 4.2 `depende-de` (R-04) — verificado por construcao
A regra-mae PD-11 torna o ciclo **estruturalmente impossivel entre estratos**: dependencia so
aponta para o mesmo estrato ou para numero menor. Restam apenas ciclos **intra-estrato**, e
sao cobertos:

| Estrato | Ciclo possivel? | Barreira |
|---|---|---|
| 2 Competencia | Entre Capabilities | RL-01, ja verificada por ordem topologica de 8 niveis no catalogo |
| 3 Estrutural | AGT ↔ AGT de outro departamento | **PD-12 proibe** — exige Handoff formal |
| 4 Execucao | SKL ↔ SKL, WFL ↔ SKL | PD-01; verificacao de DEP-GOV a cada C2 |
| 5 Valor | PRO ↔ PRO | PD-10 exige ADR para o acoplamento |

### 4.3 `especializa` (R-10)
Profundidade maxima 1 impede ciclo por construcao: filha nao tem filha.

### 4.4 `supera` (R-08)
Sucessao temporal e monotonica: um instrumento so supera outro **anterior**. PD-09 proibe
dependencia de instrumento futuro. **Sem ciclo possivel.**

### 4.5 Ciclos permitidos e desejaveis
| Relacao | Ciclo | Por que e correto |
|---|---|---|
| `consome-saida-de` (R-05) | Sim | Troca de artefatos nao e dependencia estrutural (RL-02) |
| `verifica` (R-06) | Sim | Verificacao mutua entre verificadores independentes e a propria separacao de poderes |
| `registra` (R-09) | Sim | Uma memoria pode registrar outra memoria |

### 4.6 Achado M1 — o unico ciclo problematico encontrado

O catalogo declara, em [`capabilities/README.md` §5](../capabilities/README.md):

> `CAP-governanca` | **todas** — forma, conformidade e rastreabilidade

Lido literalmente, **"todas" inclui `CAP-governanca`**: um `verifica` refletivo. Formalmente,
autoverificacao — o que PI-05 e LV-03 proibem para o mesmo artefato.

| Campo | Conteudo |
|---|---|
| Severidade | **Alta** — toca principio imutavel, ainda que por ambiguidade de redacao e nao por pratica |
| Pratica real observada | **Nao houve autoverificacao.** ADR-0002 foi proposto por DEP-EXE e revisado por DEP-QAR; FND-09 foi proposto por DEP-GOV e revisado por DEP-QAR nesta revisao. A separacao foi respeitada de fato |
| Causa | Redacao do catalogo, nao desenho do modelo. RM-06 e RL-05 impedem o par `verifica` + `depende-de`, mas nenhuma regra vigente proibia explicitamente o **auto-loop** |
| Correcao proposta | Ler e escrever *"todas as demais"*; declarar no catalogo que a conformidade dos artefatos de DEP-GOV e verificada por **DEP-QAR** |
| Correcao estrutural proposta | Acrescentar a RM-06, na proxima revisao de FND-09: *"`verifica` nao admite auto-loop: nenhuma entidade verifica a si propria (LV-03)"* |
| Dono | DEP-GOV (catalogo) e DEP-QAR (regra) |
| Prazo | Proxima mudanca C2 que toque o catalogo, ou 1a revisao estrutural — o que vier antes |

> Nao foi corrigido nesta missao por estar **fora do escopo declarado**: alterar o catalogo
> de Capabilities e mudanca C2 propria, com rito proprio (PI-09). Registrado com dono, prazo
> e correcao — nao como observacao sem destino (FND-04 §8).

---

## 5. Existe dependencia proibida?

**Nenhuma vigente. Uma foi eliminada durante a revisao (D2).**

Verificacao das doze proibicoes de §9.2 contra o modelo como aprovado:

| # | Proibicao | Resultado | Verificacao |
|---|---|---|---|
| PD-01 | Ciclo em `depende-de` | ✓ | §4.2 |
| PD-02 | Norma depender de Componente | ✓ | Nenhuma entidade de estrato 1 declara `depende-de` para estrato ≥ 3 |
| PD-03 | Capability depender de estrutura | ✓ | `CAP` declara apenas relacoes com `CAP`; `custodia` e responsabilidade (§9.4) |
| PD-04 | Verificador depender do verificado | ✓ | `FIT` nao declara dependencia dos ADRs que avalia; DEP-QAR nao depende da Linha (ES-02) |
| PD-05 | Subagente com filho ou dependente de subagente | ✓ | Profundidade 1 declarada em tres pontos |
| PD-06 | Dependencia sobre entidade nao vigente | ✓ | Nenhuma referencia de FND-09 aponta a artefato `superado` ou `revogado` |
| PD-07 | Ferramenta externa sem alternativa e descarte | ✓ | Nenhuma ferramenta existe |
| PD-08 | Norma depender de memoria | ✓ | FND-09 referencia memoria como destino de registro, nunca como fundamento |
| PD-09 | Dependencia de instrumento futuro | ✓ | FND-09 referencia ADR-0003 e ADR-0004, **simultaneos** e nao futuros |
| PD-10 | Produto depender de produto | n/a | Nenhum produto existe |
| PD-11 | Dependencia ascendente | ✓ **apos D2** | Era violada pela leitura de autoria e execucao como dependencia; corrigida em §9.4 |
| PD-12 | Agente depender de agente de outro departamento | n/a | Nenhum agente existe |

### 5.1 Verificacao adicional: FND-09 depende de que?
O proprio documento depende de FND-01, FND-03, FND-04 e FND-08 — todos **estrato 1**,
mesmo estrato. Dependencia lateral e permitida. **Sem inversao.**

### 5.2 Verificacao da autoridade
As 21 linhas da matriz de §8.2 foram confrontadas com FND-01 §7.3, FND-04 §2 e §6 e FND-08
§6.3. **Nenhuma divergencia encontrada.** Onde a origem era omissa — `SPC`, `TPL`, `MSG` — a
matriz declara a autoridade pela primeira vez, e isso e acrescimo, nao conflito.

---

## 6. O Meta Model suporta crescimento da plataforma?

**Sim, com uma ressalva de severidade media (M6).**

### 6.1 Tres mecanismos de crescimento verificados

| Mecanismo | Onde | Verificacao |
|---|---|---|
| Entidade nova | §11.1 — Teste TE-1..TE-7 + rito de 9 etapas | Rito completo, com veto em [5] e Fitness em [8] |
| Crescimento sem entidade nova | §11.2 — gradacao de 5 degraus | Atributo novo permanece C1; classe nova, C2. **So entidade, arquetipo e relacao sao C3** |
| Compatibilidade | §11.4 — EV-01 a EV-09 | EV-01 impede que evolucao invalide instancia existente; EV-02 exige janela de migracao com dono |

### 6.2 Teste de esforco: as 13 recusas entrariam sem redesenho?

Simulacao de entrada de cada recusa pelo rito de §11.1, verificando se exigiria mudar o
modelo ou apenas acrescentar:

| Recusa | Entraria como | Exige redesenho? |
|---|---|---|
| `Policy` / `Standard` | Entidade `Norma Derivada`, estrato 1, arquetipo A2 | **Nao** — o slot esta nomeado; hierarquia normativa ganha nivel entre ADR e Carta |
| `Team` | Entidade estrato 3, arquetipo A1+A3 | **Nao** — `contem` ganha par DEP→TEAM→AGT |
| `Service` | Classe de `PRO` (degrau 1, C2) | **Nao** |
| `Event` | Entidade estrato 6, perfil P3 | **Nao** — o perfil efemero ja existe |
| `Metric` | Entidade estrato 6 | **Nao** |
| `Command` | Classe de `SKL` (degrau 1, C2) | **Nao** |

**Seis de seis entrariam por acrescimo.** Nenhuma exigiria alterar estratos, arquetipos ou
relacoes existentes. E a evidencia mais forte de que o modelo suporta crescimento.

### 6.3 Achado M6 — o risco do universo fechado

Universo fechado com entidade nova em **C3** cria pressao: quando um Framework futuro
precisar de um tipo e o rito parecer caro, a saida mais barata sera pedir **excecao formal**
(FND-01 §8.3) em vez de abrir RFC.

| Campo | Conteudo |
|---|---|
| Severidade | Media |
| Por que e real | Excecao e autorizada pelo Soberano e tem prazo; RFC exige analise, manifestacoes e ratificacao. A assimetria de esforco favorece o atalho |
| Mitigacao ja existente | Excecao sem prazo e invalida; excecao vencida sem regularizacao vira incidente automatico |
| **Metrica de vigilancia proposta** | *Numero de excecoes formais que tocam MT-01 por horizonte.* Direcao desejada: **0**. Duas ou mais indicam que o rito de entidade nova esta caro demais e deve ser reclassificado de C3 para C2 |
| Dono | DEP-GOV |
| Gatilho | 1a revisao estrutural |

### 6.4 Achado M2 — o modelo e declarado, nao comprovado

| Medida | Valor |
|---|---|
| Entidades declaradas | 21 |
| Com instancia registrada em artefato | **6** — FND (9), ADR (4), RFC (3), CAP (23), TPL (19), FIT (1) |
| De instancia unica, sem artefato proprio | **2** — ORG, SOBERANO *(achado M3)* |
| **Sem nenhuma instancia** | **13** — EXC, INC, DEP, AGT, SUB, SKL, WFL, TOL, PRO, PRJ, SPC, MEM, MSG |
| Relacoes com uso real observado | 4 de 10 — `supera`, `custodia`, `exerce`, `verifica` |
| Perfis de ciclo de vida exercitados | 2 de 4 — P1 e P2; P0 e P3 nunca documentados |

**Leitura:** treze das vinte e uma entidades — quase dois tercos — nunca foram instanciadas,
e `MEM` esta entre elas apesar de a estrutura das cinco camadas estar pronta. O Meta Model
descreve o que a plataforma **admite** existir, e nao o que ela ja e. E legitimo — ADR-0003
§8 declara os ganhos como previstos e nao observados — mas exige que ninguem trate FND-09
como descricao de um sistema em operacao.

**Recomendacao:** que a primeira revisao estrutural verifique **entidade por entidade** se a
ausencia de instancia se manteve, e aplique EV-08 sem cerimonia. Entidade que atravesse um
horizonte inteiro sem instancia deve ser proposta para remocao ou ter sua manutencao
justificada por escrito.

---

## 7. Alguma entidade deveria ser removida?

**Nenhuma agora. Quatro com gatilho de remocao armado.**

Aplicado EV-08 — entidade sem instancia ao longo de um horizonte obriga proposta de remocao
ou registro fundamentado de manutencao. Como **nenhum horizonte se encerrou**, o gatilho
ainda nao disparou para nenhuma.

| Entidade | Argumento para remover | Por que foi mantida | Gatilho de remocao |
|---|---|---|---|
| `SUB` | Poderia ser atributo de `AGT` (M5) | E o unico instrumento que materializa reducao de contexto, o terceiro ganho de PI-14 | 5 agentes criados sem nenhum subagente, ou razao 1:1 |
| `ORG` | Instancia unica, sem artefato proprio (M3) | O grafo de contencao precisa de raiz declarada | Se `contem` nunca for consultado a partir da raiz em um horizonte |
| `SOBERANO` | Nao e artefato; poderia ser atributo de FND-01 | O Authority Model precisa dele como sujeito; AU-10 sem ele nao tem termino | **Nenhum** — remove-lo exigiria emendar PI-01 |
| `SPC` | Poderia ser secao da Carta de Produto | Tem dono, portao (QG-1) e ciclo proprios; passa em TE-3 | Se toda spec vier a ter exatamente um produto e nunca for versionada isoladamente |

**Conclusao:** remover qualquer uma nesta data seria simetrica da criacao por antecipacao —
**remocao por antecipacao**, igualmente sem sinal observado. Nao remover e, aqui, a decisao
correta, e ela propria fica registrada (PI-14, regra 2).

---

## 8. Alguma regra deve virar norma constitucional?

**Uma ja virou nesta missao. Uma e candidata e o adiamento esta registrado.**

### 8.1 Ja elevada — QG-6
O portao **QG-6 — Aptidao Arquitetural** foi acrescentado a FND-01 §6.2 por ADR-0004. Era
condicao para o mecanismo poder **bloquear**: portao e o unico instrumento constitucional que
exige liberacao registrada por quem nao produziu.

### 8.2 Candidata — MT-01, universo fechado

| Campo | Conteudo |
|---|---|
| Regra | *Nenhuma entidade estrutural existe fora do Meta Model.* |
| Por que mereceria | E a regra que sustenta toda a missao. Hoje esta protegida por MI-M01 e pela classe C3 de §11.1 — protecao **normativa**, nao **constitucional**. Um FND-09 revogado levaria a regra consigo |
| Como seria | Principio Imutavel **PI-15 — Universo Declarado**, com o mesmo estatuto de PI-12 (nenhum componente sem Carta) |
| **Por que nao agora** | PI-12 e PI-14 foram escritos apos pratica observada. MT-01 **nunca foi exercido**: nenhuma entidade candidata foi recusada por ele em uso real. Eleva-lo hoje seria transformar hipotese em clausula petrea — exatamente o que MM-04 proibe para promocao a camada EST, e o que FND-08 §7.1 chama de antecipacao |
| Custo assumido pelo adiamento | Se FND-09 for revogado antes da elevacao, a protecao do universo fechado desaparece junto. Risco baixo: revogacao de FND-09 e C3 e exige ratificacao |
| Prazo do adiamento | **1a revisao da Fundacao (2027-01-28)** |
| Gatilho de elevacao | Primeira entidade candidata efetivamente recusada por MT-01, **ou** duas excecoes formais que o tenham contornado (metrica de M6) |
| Dono | DEP-GOV |

> Registrado como **decisao de nao decidir** (FND-07 §9): o custo esta declarado, com prazo,
> gatilho e dono. Nao e omissao.

### 8.3 Candidatas examinadas e recusadas

| Regra | Por que **nao** deve virar constitucional |
|---|---|
| PD-11 — dependencia nunca sobe de estrato | Deriva de estratos, que sao construcao de FND-09. Elevar amarraria a Constituicao a uma taxonomia especifica de estratos, reduzindo a liberdade de reorganiza-los |
| MI-M07 — verificador nunca depende do verificado | **Ja e constitucional**: e PI-05 aplicado. Elevar duplicaria norma (LX-07) |
| FT-04 — complacencia escala ao Soberano | E regra de operacao de um mecanismo novo. Elevar antes de tres execucoes seria o mesmo erro apontado em §8.2 |
| MI-M08 — todo Componente com Carta e Capability | **Ja e constitucional**: PI-12 mais ADR-0002. FND-09 apenas unifica o alcance |

---

## 9. Conclusao da revisao

| Criterio de conclusao da missao | Resultado |
|---|---|
| Meta Model organizacional consistente | ✓ 21 entidades, 4 arquetipos, 10 relacoes, 4 perfis, 12 dependencias proibidas; 3 divergencias internas detectadas e corrigidas (§0) |
| Versionavel | ✓ Perfil P1, versionamento semantico, historico proprio; regras de compatibilidade EV-01 a EV-09 |
| Extensivel | ✓ Rito de entidade nova com Teste TE; gradacao de 5 degraus; 6 de 6 recusas simuladas entrariam por acrescimo (§6.2) |
| Sustenta Frameworks futuros sem redefinir conceitos | ✓ Nenhuma definicao existente reescrita; C4 bloqueante verificado item a item (§1.5) |
| Universo oficial declarado | ✓ MT-01, com 13 recusas registradas com destino e gatilho |

**Parecer de DEP-QAR:** o Meta Model esta apto a servir de base para a fase seguinte. Os oito
achados sao registrados com severidade, dono e gatilho; **nenhum bloqueia a adocao**. O
achado M1 exige acao em mudanca propria, ja escalada com prazo.

**Ressalva registrada (PI-10):** este documento descreve o que a plataforma **admite**
existir. Com 13 das 21 entidades sem nenhuma instancia, 6 das 10 relacoes sem uso observado e
2 dos 4 perfis de ciclo de vida nunca exercitados, ele **nao** e evidencia de que o modelo
funcione na pratica. A aptidao evolutiva desta mudanca e avaliada separadamente em
[FIT-2026-001](../governance/fitness/FIT-2026-001-meta-model.md).

---

## 10. Achados que geram acao futura

| # | Acao | Quando | Responsavel |
|---|---|---|---|
| M1 | Corrigir "todas" para "todas as demais" no catalogo; acrescentar proibicao de auto-loop a RM-06 | Proxima C2 que toque o catalogo, ou 1a revisao estrutural | DEP-GOV + DEP-QAR |
| M2 | Verificar entidade por entidade a ausencia de instancia e aplicar EV-08 | Fim do 1o horizonte | DEP-EXE + DEP-QAR |
| M3 | Acrescentar a TE-4 a ressalva sobre entidades de estrato 0 | 1a revisao de FND-09 | DEP-GOV |
| M4 | Verificar se A2 foi alguma vez invocado para decidir; consolidar se nunca | 1a revisao estrutural | DEP-GOV |
| M5 | Reavaliar fronteira `AGT` × `SUB` | Apos 5 agentes criados | DEP-ENG + DEP-QAR |
| M6 | Medir excecoes formais que tocam MT-01; reclassificar rito para C2 se ≥ 2 | 1a revisao estrutural | DEP-GOV |
| M7 | Acrescentar regra de desempate `SKL` × `WFL` | 1a revisao de FND-09 | DEP-GOV |
| M8 | Avaliar elevacao de MT-01 a PI-15 | 1a revisao da Fundacao (2027-01-28) | DEP-GOV + SOBERANO |
