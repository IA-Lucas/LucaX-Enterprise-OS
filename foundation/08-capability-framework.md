---
id: FND-08
titulo: Enterprise Capability Framework
tipo: fundacao
versao: 1.2.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-EXE
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0001, ADR-0002, ADR-0003, ADR-0005]
ratificacao: ratificada
substitui: []
substituido_por: null
---

# Enterprise Capability Framework

## Proposito

Definir a camada de **Capabilities** do LucaX Enterprise OS: o que a organizacao sabe
fazer, de forma permanente e independente de departamentos, agentes, pessoas ou
tecnologias. Estabelece a taxonomia, o ciclo de vida, as relacoes, a propriedade e as
regras de evolucao das Capabilities.

Esta e a camada intermediaria entre a Constituicao (por que existimos) e a estrutura
operacional futura (quem executa o que): **as Capabilities dizem o que a empresa e capaz
de fazer, e sobrevivem a qualquer reorganizacao.**

## Escopo

| Item | Definicao |
|---|---|
| **Inclui** | Definicao de Capability, atributos obrigatorios, taxonomia (dominio, classe, maturidade), ciclo de vida, tipos de relacao, regras de propriedade, criterios de evolucao, regra de vinculacao obrigatoria. |
| **Nao inclui** | O catalogo em si (vive em [`../capabilities/`](../capabilities/)), departamentos, agentes, skills, workflows, codigo, infraestrutura. |
| **Subordinado a** | [FND-01 Constituicao](01-constituicao.md), [FND-03 Taxonomia](03-taxonomia.md), [FND-04 Governanca](04-governanca.md). |
| **Consumido por** | Toda fase futura. Nenhum componente pode ser criado sem vinculo a Capability (§8). |

## Responsaveis

| Papel | Responsavel |
|---|---|
| Proprietario do framework | DEP-EXE |
| Guardiao normativo | DEP-GOV |
| Custodia do catalogo | DEP-KMS |
| Verificacao de sobreposicao e lacuna | DEP-QAR |
| Ratificador de criacao e aposentadoria | SOBERANO |

---

## 1. O Que E Uma Capability

> **Capability e uma competencia permanente da organizacao: algo que a empresa sabe fazer,
> descrito de forma que continue verdadeiro mesmo que mudem os departamentos, os agentes,
> as ferramentas e a tecnologia.**

### 1.1 Teste de Capability

Uma competencia so e Capability se **todas** as respostas forem afirmativas:

| # | Pergunta | Se a resposta for "nao" |
|---|---|---|
| TC-1 | Continua verdadeira se todos os departamentos forem reorganizados? | E estrutura, nao capability |
| TC-2 | Continua verdadeira se a tecnologia mudar completamente? | E implementacao, nao capability |
| TC-3 | Descreve **o que** a empresa sabe fazer, e nao **como** nem **quem**? | E processo ou papel |
| TC-4 | A empresa deixaria de conseguir algo relevante se ela desaparecesse? | E atividade, nao competencia |
| TC-5 | Pode ser exercida por mais de um arranjo organizacional possivel? | E cargo disfarcado |
| TC-6 | E descritivel sem citar nenhum produto especifico? | E requisito de produto |

### 1.2 O que Capability **nao** e

| Nao e | Diferenca | Onde vive |
|---|---|---|
| **Departamento** | Departamento e **quem responde**; Capability e **o que se sabe fazer** | FND-02 |
| **Agente** | Agente e **quem executa** | FND-03 §3.3 |
| **Skill** | Skill e **um procedimento reutilizavel**; Capability e o campo de competencia que o contem | FND-03 §3.5 |
| **Workflow** | Workflow e **uma sequencia de etapas** | FND-03 §3.10 |
| **Produto** | Produto e **um resultado com publico proprio** | FND-03 §3.1 |
| **Ferramenta** | Ferramenta e **um meio externo** | FND-03 §3.12 |
| **Norma** | Norma diz **o que e obrigatorio**; Capability diz **o que se sabe fazer** | FND-01, FND-04 |

### 1.3 Relacao com a estrutura

```
  CONSTITUICAO          por que existimos e o que nunca se viola
        |
  CAPABILITIES          o que a organizacao sabe fazer          <-- esta camada
        |
  ESTRUTURA             quem responde por cada competencia
   (departamentos)
        |
  EXECUCAO              quem faz, com que procedimento e ferramenta
   (agentes, skills, workflows, ferramentas)
```

**Capabilities sao mais estaveis que a estrutura.** Um departamento pode ser criado,
dividido ou extinto sem que a Capability correspondente deixe de existir — ela apenas passa
a ter outro custodio. O inverso nao vale: aposentar uma Capability significa que a
organizacao **deixou de saber fazer aquilo**, o que e um evento estrategico.

## 2. Atributos Obrigatorios de uma Capability

Toda Capability declara os treze atributos abaixo. Atributo ausente invalida a Carta e
DEP-GOV a devolve sem analise de merito.

| # | Atributo | O que declara | Regra |
|---|---|---|---|
| A-01 | **Identidade** | ID `CAP-<slug>`, nome, dominio, classe, maturidade | ID imutavel (LX-08) |
| A-02 | **Proposito** | Por que esta competencia existe na organizacao | Ate 3 frases |
| A-03 | **Missao** | O resultado permanente pelo qual responde | Uma frase |
| A-04 | **Escopo** | O que esta competencia abrange | Descrito sem citar produto |
| A-05 | **Limites** | O que ela deliberadamente **nao** abrange, e de quem e | Obrigatorio — impede sobreposicao |
| A-06 | **Responsabilidades** | O que a organizacao consegue fazer por possuir isto | Verbos de competencia, nao de tarefa |
| A-07 | **Entradas** | O que ela consome, e de onde | Origem por CAP-id ou externa |
| A-08 | **Saidas** | O que ela produz para outros | Consumivel por outra Capability |
| A-09 | **Artefatos produzidos** | Tipos de artefato que materializam a competencia | Por tipo da taxonomia (FND-03) |
| A-10 | **Dependencias** | De quais Capabilities ela precisa | Por CAP-id, com tipo de relacao (§5) |
| A-11 | **Consumidores** | Quais Capabilities dependem dela | Espelho de A-10 dos outros |
| A-12 | **Indicadores** | Como se sabe que a competencia existe e esta saudavel | Verificavel, nao declarativo |
| A-13 | **Criterios de evolucao** | O que dispara especializacao, fusao, depreciacao | Vinculado a PI-14 (§7) |

### 2.1 Regra dos Limites (A-05)
Limites sao o instrumento que impede sobreposicao entre Capabilities. Cada limite nomeia
**a Capability que de fato possui aquilo**. Limite generico ("nao cuida de outras coisas")
e devolvido: nao delimita nada.

### 2.2 Regra dos Indicadores (A-12)
Indicador de Capability mede **existencia e saude da competencia**, nao volume de trabalho.

| Bom indicador | Mau indicador |
|---|---|
| "Decisao arquitetural produzida sem retrabalho posterior" | "Numero de ADRs escritos" |
| "Tempo entre incidente e causa identificada" | "Numero de incidentes" |
| "Reuso de spec entre produtos" | "Numero de specs" |

## 3. Capability Taxonomy

Toda Capability e classificada em **tres eixos independentes e simultaneos**.

### 3.1 Eixo 1 — Dominio (agrupamento por natureza)

| Codigo | Dominio | Natureza da competencia |
|---|---|---|
| `DIR` | **Direcao** | Decidir para onde ir e manter a organizacao integra |
| `VAL` | **Descoberta e Valor** | Descobrir o que vale a pena existir e defini-lo |
| `REA` | **Realizacao** | Transformar definicao em coisa que funciona |
| `GAR` | **Garantia** | Assegurar que o que sai e correto, seguro e licito |
| `SUS` | **Sustentacao** | Manter funcionando o que ja existe |
| `MER` | **Mercado e Recursos** | Levar ao publico e sustentar economicamente |
| `COG` | **Cognicao Organizacional** | Fazer a organizacao saber, lembrar e aprender |

Dominio e **agrupamento**, nao hierarquia: nenhum dominio manda em outro.

### 3.2 Eixo 2 — Classe estrategica

| Classe | Definicao | Teste | Consequencia |
|---|---|---|---|
| **`nucleo`** (Core) | Se a organizacao for medíocre nisto, a proposta inteira falha | "Isto e o que nos torna capazes do que prometemos?" | Nunca terceirizada; investimento prioritario; aposentadoria exige emenda C3 |
| **`habilitadora`** (Enabling) | Necessaria para o nucleo funcionar, mas nao diferencia | "Sem isto o nucleo trava?" | Pode ser padronizada; busca-se eficiencia |
| **`suporte`** (Supporting) | Obrigacao ou higiene; ausencia gera dano, presenca nao gera vantagem | "Isto evita dano, mas nao cria vantagem?" | Minimo suficiente; candidata a externalizacao |

**Regra:** classe nao e permanente — ela e reavaliada a cada revisao estrategica. Uma
Capability `habilitadora` pode virar `nucleo` quando a estrategia muda, e vice-versa.
Mudanca de classe e decisao **C2** com registro.

### 3.3 Eixo 3 — Maturidade

| Maturidade | Significado | A organizacao... |
|---|---|---|
| `proposta` | Identificada, ainda nao aprovada | ...ainda nao possui |
| `experimental` | Aprovada, sendo exercida pela primeira vez | ...esta descobrindo se sabe |
| `emergente` | Exercida com resultado inconsistente | ...sabe as vezes |
| `estabelecida` | Exercida com resultado previsivel | ...sabe |
| `madura` | Exercida com previsibilidade e reuso comprovado entre contextos | ...sabe e compoe |
| `em-depreciacao` | Deixando de ser exercida deliberadamente | ...esta desistindo |
| `aposentada` | Nao mais exercida | ...deixou de saber |

### 3.4 Ortogonalidade com o estado documental

> **Atencao a confusao comum.** `maturidade` (este documento) e `status` (FND-03 §5) sao
> atributos **independentes** e coexistem no mesmo frontmatter.

| Atributo | Descreve | Valores |
|---|---|---|
| `status` | O estado do **documento** | `rascunho`, `em-revisao`, `aprovado`, `ativo`, `depreciado`, `superado`, `revogado`, `arquivado` |
| `maturidade` | O estado da **competencia** | `proposta` … `aposentada` |

Exemplo legitimo: uma Carta com `status: ativo` (documento em vigor) e
`maturidade: experimental` (a organizacao ainda esta aprendendo a exercer aquilo). Isso nao
e contradicao — sao dimensoes distintas.

### 3.5 Combinacoes proibidas

| Combinacao | Por que e invalida |
|---|---|
| `nucleo` + `proposta` | Nao se declara nucleo o que a organizacao ainda nao aprovou possuir |
| `nucleo` + `aposentada` | Aposentar nucleo exige antes rebaixar a classe, via C3 |
| `suporte` + investimento prioritario | Contradiz a definicao da classe |
| `madura` sem indicador medido | Maturidade e afirmacao verificavel, nao autoavaliacao (VD-05, PI-10) |

## 4. Capability Lifecycle

```
  [1] IDENTIFICACAO      lacuna observada ou competencia ja exercida sem nome
        |
  [2] PROPOSTA           RFC: e mesmo Capability? passa no teste TC-1..TC-6?
        |                        |
        |                        +--> recusada -> arquivada (nunca apagada)
        |
  [3] APROVACAO          ADR + ratificacao do Soberano  ->  maturidade: experimental
        |
  [4] EXERCICIO          a organizacao passa a exerce-la; indicadores comecam a medir
        |                        |
        |                        +--> nao se sustenta -> volta a [2] ou aposenta
        |
  [5] EMERGENTE          exercida, resultado ainda inconsistente
        |
  [6] ESTABELECIDA       resultado previsivel; indicadores dentro do esperado
        |
  [7] MADURA             reuso comprovado entre contextos distintos
        |
        +----> ESPECIALIZACAO  divide-se em Capabilities filhas (§7.2)
        +----> FUSAO           reune-se a outra (§7.3)
        +----> DEPRECIACAO     deixa de ser exercida (§7.4)
        |
  [8] EM-DEPRECIACAO     custodio nomeado para o desligamento; consumidores migrados
        |
  [9] APOSENTADA         nao mais exercida; Carta preservada, nunca apagada
```

### 4.1 Criterios de transicao

| Transicao | Criterio obrigatorio | Instrumento | Quem decide |
|---|---|---|---|
| identificacao → proposta | Lacuna descrita e teste TC aplicado | RFC | Qualquer departamento |
| proposta → experimental | Passa nos 6 testes TC; sem sobreposicao com catalogo; custodio aceito | **ADR** | SOBERANO (Tipo 1) |
| experimental → emergente | Exercida ao menos uma vez com resultado registrado | Nota de Decisao | Custodio + DEP-QAR |
| emergente → estabelecida | Resultado previsivel em **≥ 2 ocorrencias**; indicadores medidos | Nota de Decisao | Custodio + DEP-QAR |
| estabelecida → madura | Reuso comprovado em **≥ 2 contextos distintos**; artefatos reaproveitados | **ADR** | DEP-EXE |
| qualquer → em-depreciacao | Criterio de evolucao (A-13) disparado; consumidores mapeados | **ADR** | DEP-EXE; SOBERANO se `nucleo` |
| em-depreciacao → aposentada | Todos os consumidores migrados; artefatos arquivados; APR gravado | **ADR** | SOBERANO |
| rebaixamento de maturidade | Indicadores deixaram de se sustentar | Nota de Decisao + registro APR | Custodio + DEP-QAR |

### 4.2 Regras do ciclo

| # | Regra |
|---|---|
| CL-01 | **Nao se pula estagio.** De `proposta` nao se vai a `estabelecida`, ainda que a competencia pareca obvia. |
| CL-02 | **Rebaixamento e legitimo e esperado.** Maturidade que nao se sustenta desce, com registro APR. Nao ha vergonha em descer. |
| CL-03 | **Aposentar nao apaga.** A Carta e preservada em `aposentada` — saber o que a organizacao deixou de saber tem valor proprio (MM-09). |
| CL-04 | **Nenhuma Capability e aposentada com consumidor ativo.** Migrar consumidores precede o desligamento. |
| CL-05 | Capability `nucleo` nao entra em depreciacao sem antes ser rebaixada de classe, por decisao registrada. |
| CL-06 | Maturidade declarada sem indicador medido e devolvida por DEP-QAR (§3.5). |

## 5. Capability Relationships

### 5.1 Tipos oficiais de relacao

| Relacao | Significado | Direcao | Ciclo permitido? |
|---|---|---|---|
| `depende-de` | Nao consegue operar sem a outra | A → B | **Nao** |
| `habilita` | Torna a outra possivel ou melhor; inverso de `depende-de` | A → B | Nao (espelho) |
| `consome-saida-de` | Usa artefato produzido pela outra | A → B | Sim |
| `fornece-para` | Espelho de `consome-saida-de` | A → B | Sim |
| `especializa` | E recorte mais estreito de uma Capability mae | filha → mae | Nao |
| `verifica` | Exerce garantia independente sobre a outra | A → B | Sim, e desejavel |
| `coordena` | Aloca, prioriza ou arbitra sobre a outra | A → B | Nao |

### 5.2 Regras de relacao

| # | Regra |
|---|---|
| RL-01 | **Dependencia circular dura e proibida.** `depende-de` nao pode formar ciclo (herda DP-03). Detectado, exige RFC para desfazer. |
| RL-02 | `consome-saida-de` **pode** ser mutuo — troca de artefatos nao e dependencia estrutural. |
| RL-03 | Toda relacao e declarada nos **dois lados** (A-10 e A-11). Declaracao unilateral e elo quebrado. |
| RL-04 | `especializa` tem profundidade maxima **1**: Capability filha nao tem filha (herda IV-04). |
| RL-05 | `verifica` nunca coexiste com `depende-de` no mesmo par e direcao — quem verifica nao pode depender do verificado (PI-05, ES-02). |
| RL-05b | `verifica` **nao admite par reflexivo**. A regra e universal e esta escrita uma unica vez em [FND-09 §6.3, RM-06b](09-meta-model.md) — aqui apenas referenciada (MM-01). *(ADR-0005)* |
| RL-06 | Capability sem nenhum consumidor por um horizonte inteiro e candidata a depreciacao (§7.4). |
| RL-07 | Capability da qual **tudo** depende e sinal de escopo amplo demais — avaliar especializacao (§7.2). |

### 5.3 Mapa de dependencias
O mapa oficial e mantido em [`../capabilities/README.md`](../capabilities/README.md) e
atualizado a cada mudanca de catalogo. Mapa desatualizado apos mudanca aprovada e mudanca
incompleta (CV-04).

## 6. Capability Ownership

### 6.1 Os quatro papeis

| Papel | Quem | Faz | Nao pode |
|---|---|---|---|
| **Custodio** | Exatamente **um** departamento | Mantem a Carta, os indicadores e a saude da competencia | Impedir que outros exercam a competencia |
| **Exercentes** | Um ou mais departamentos | Exercem a competencia no seu dominio | Alterar a Carta |
| **Autoridade de evolucao** | Custodio, com parecer de DEP-GOV | Propoe criacao, especializacao, fusao, depreciacao | Aprovar a propria proposta (PI-05) |
| **Ratificador** | SOBERANO | Da eficacia a criacao e a aposentadoria | Ser presumido ou tacito (GV-05) |

### 6.2 Regras de propriedade

| # | Regra |
|---|---|
| OW-01 | **Custodia e unica** (ES-01). Duas custodias sobre a mesma Capability e defeito de desenho. |
| OW-02 | **Custodia nao e exclusividade de exercicio.** O custodio zela pela competencia; nao monopoliza sua pratica. |
| OW-03 | Capability sem custodio e **nula**: nao pode ser vinculada a nenhum componente (GV-01). |
| OW-04 | Custodia de Capability `nucleo` nao pode recair sobre departamento de classe Suporte. |
| OW-05 | Custodia de Capability de dominio `GAR` (Garantia) recai obrigatoriamente sobre departamento de classe **Guarda** — preserva ES-02 e PI-05. |
| OW-06 | Transferencia de custodia e mudanca **C2**, com ADR. O ID da Capability **nao muda** (LX-08). |
| OW-07 | Um departamento pode ser custodio de varias Capabilities; uma Capability tem um custodio so. |

### 6.3 Autoridade sobre a Capability

| Materia | Decide | Consulta | Ratifica |
|---|---|---|---|
| Criar Capability | SOBERANO | DEP-EXE, DEP-GOV, DEP-QAR | SOBERANO |
| Alterar escopo ou limites | Custodio | DEP-GOV, Capabilities vizinhas | DEP-EXE |
| Mudar classe estrategica | DEP-EXE | Custodio | SOBERANO se envolver `nucleo` |
| Promover maturidade | Custodio | DEP-QAR (verifica indicadores) | DEP-EXE se → `madura` |
| Especializar ou fundir | Custodio propoe | DEP-GOV, DEP-QAR | SOBERANO |
| Transferir custodia | DEP-EXE | Custodio atual e futuro | SOBERANO se `nucleo` |
| Aposentar | DEP-EXE propoe | Todos os consumidores | **SOBERANO** |

## 7. Capability Evolution

Esta secao aplica PI-14 (evolucao continua por especializacao) a camada de Capabilities.
Vale integralmente a regra-mae: **evidencia autoriza, suposicao nao.**

### 7.1 Quando **criar** uma Capability

Criar exige **todas** as condicoes:

1. Passa nos seis testes TC (§1.1).
2. A competencia nao esta contida no escopo de nenhuma Capability existente.
3. Se hoje ela e exercida, e exercida sem nome — ou existe lacuna comprovada por falha real.
4. Ha departamento disposto e apto a ser custodio.
5. Ha ao menos um indicador que dira se a organizacao passou a possui-la.

**Antipadrao de criacao:** criar Capability por simetria ("as outras areas tem, esta
tambem deveria"), por antecipacao ("vamos precisar disso") ou por espelhamento de
departamento ("cada departamento tem a sua"). Os tres sao recusados por DEP-GOV.

### 7.2 Quando **especializar** (dividir)

| Gatilho | Sinal observavel | Ganho PI-14 |
|---|---|---|
| Escopo heterogeneo | A Capability e invocada por motivos que nao se parecem | Organizacao |
| Limites em disputa | Duas Capabilities discutem a mesma fronteira repetidamente | Organizacao |
| Indicadores incompativeis | Um mesmo indicador nao consegue medir tudo o que ela cobre | Organizacao |
| Consumo assimetrico | Um subconjunto e consumido por quase todos; o resto, por quase ninguem | Reuso |
| Contexto excessivo | Exerce-la exige carregar material que a maior parte dos casos nao usa | Reducao de contexto |
| Dependencia universal | Tudo depende dela (RL-07) | Organizacao |

Regras: a divisao usa `especializa`, profundidade maxima 1 (RL-04); **cada responsabilidade
da Capability mae recebe destino explicito** — especializacao nao cria orfaos (PI-14,
regra 3); o ganho declarado tem data de reavaliacao.

### 7.3 Quando **fundir**

| Gatilho | Interpretacao |
|---|---|
| Duas Capabilities sempre exercidas juntas, nunca isoladas | A fronteira entre elas nao existe de fato |
| Limites que ninguem consegue enunciar sem ambiguidade | A distincao e nominal |
| Consumidores identicos e saidas indistinguiveis | Sao a mesma competencia com dois nomes |
| Custo de coordenar maior que o ganho declarado na divisao | O ganho previsto nao se confirmou |

A fusao produz **uma Capability nova**, com ID novo, que `substitui` as duas anteriores.
As Cartas originais passam a `superado` e sao preservadas (MM-09). Fundir e o movimento
simetrico de especializar — e igualmente obrigatorio quando o gatilho aparece.

### 7.4 Quando **depreciar e aposentar**

| Gatilho | Sinal |
|---|---|
| Sem consumidor por um horizonte inteiro | RL-06 |
| A estrategia deixou de exigir a competencia | Decisao de portfolio registrada |
| A competencia foi absorvida por outra | Fusao ja ocorreu de fato |
| A competencia passou a ser adquirida externamente | Decisao de externalizacao (so classe `suporte`) |

Regras: CL-04 (nenhum consumidor ativo), CL-05 (`nucleo` rebaixa antes de depreciar),
registro APR obrigatorio sobre **por que a organizacao deixou de precisar saber aquilo**.

### 7.5 Reavaliacao periodica
A cada revisao estrutural (FND-02 §9.4), DEP-EXE e DEP-QAR revisam o catalogo inteiro:
gatilhos de §7.2 a §7.4, classes estrategicas, maturidades declaradas versus indicadores
medidos, e lacunas. **Revisao que conclui "manter tudo" tres vezes seguidas escala ao
Soberano** (herda FND-02 §9.4).

## 8. Regra de Vinculacao Obrigatoria

> **Nenhum Departamento, Agente, Subagente, Skill, Workflow, Produto, Projeto ou Ferramenta
> pode existir sem estar vinculado a pelo menos uma Capability.**

> **Alcance estendido por ADR-0003.** A versao 1.0.0 alcancava seis tipos. A analise de
> RFC-0002 constatou que PI-12 exige Carta para **oito** — os mesmos seis mais Projeto e
> Ferramenta —, e que a divergencia deixava dois tipos fora da espinha dorsal de
> rastreabilidade de §8.4. Os dois alcances passam a coincidir, e o arquetipo COMPONENTE de
> [FND-09 §4](09-meta-model.md) torna-se uniforme. Custo de migracao na data da emenda:
> **zero** — nao existia nenhuma instancia de Projeto nem de Ferramenta.

### 8.1 Como o vinculo se declara
Todo componente dos tipos acima declara no frontmatter:

```yaml
capabilities: [CAP-<slug>, ...]   # ao menos uma; nunca vazio
```

### 8.2 Semantica do vinculo por tipo

| Componente | O vinculo significa |
|---|---|
| **Departamento** | As Capabilities de que e custodio ou exercente |
| **Agente / Subagente** | As Capabilities que exerce ao atuar |
| **Skill** | A Capability que o procedimento materializa |
| **Workflow** | As Capabilities encadeadas pela sequencia |
| **Produto** | As Capabilities que sua existencia consome |
| **Projeto** | As Capabilities que o esforco consome enquanto durar |
| **Ferramenta** | As Capabilities que ela habilita ao ser adotada |

### 8.3 Regras de vinculacao

| # | Regra |
|---|---|
| VC-01 | Vinculo a Capability inexistente, `proposta` ou `aposentada` e **elo quebrado** — bloqueia aprovacao (FND-04 §5.1). |
| VC-02 | Componente cuja competencia nao cabe em nenhuma Capability existente **revela lacuna**: abre-se RFC de Capability antes de criar o componente. |
| VC-03 | Vincular a muitas Capabilities (mais de tres) e sinal de componente amplo demais — avaliar especializacao do componente, nao criacao de Capability. |
| VC-04 | O vinculo e verificado por DEP-GOV no portao QG-0 e na auditoria de integridade referencial. |
| VC-05 | Aposentar Capability com componente vinculado ativo e proibido (CL-04). |

### 8.4 Consequencia arquitetural
Esta regra torna o catalogo de Capabilities a **espinha dorsal de rastreabilidade** do
sistema: de qualquer componente e possivel subir ate a competencia que ele materializa, e
de qualquer competencia e possivel descer ate tudo que a exerce.

Com o alcance unificado em oito tipos, a espinha vale **sem excecao**: nao ha componente com
Carta que escape do catalogo, nem competencia cujo conjunto de exercentes esteja incompleto.

## 9. Carta de Capability

Toda Capability existe por meio de uma Carta, gravada em `capabilities/CAP-<slug>.md`,
produzida com [`TPL-capability`](templates/TPL-capability.md).

### 9.1 Frontmatter proprio
Alem do frontmatter universal (FND-03 §4), a Carta declara:

```yaml
dominio: <DIR|VAL|REA|GAR|SUS|MER|COG>
classe: <nucleo|habilitadora|suporte>
maturidade: <proposta|experimental|emergente|estabelecida|madura|em-depreciacao|aposentada>
custodio: <DEP-xxx>
exercentes: [<DEP-xxx>, ...]
depende_de: [<CAP-slug>, ...]
consumida_por: [<CAP-slug>, ...]
especializa: <CAP-slug | null>
```

> **O frontmatter carrega apenas dependencia dura.** `depende_de` e `consumida_por` listam
> exclusivamente relacoes do tipo `depende-de` — as unicas que nao admitem ciclo (RL-01) e
> que, portanto, definem a ordem estrutural do catalogo. As demais relacoes
> (`consome-saida-de`, `fornece-para`, `verifica`, `coordena`) sao declaradas nas secoes 8
> e 9 da Carta e no mapa oficial, **nao** no frontmatter.
>
> Consequencia pratica: `consumida_por: []` nao significa que ninguem usa a Capability —
> significa que ninguem **trava** sem ela. Para RL-06 (candidata a depreciacao), o que
> conta e a ausencia de consumidor de **qualquer** tipo, verificada no mapa.

### 9.2 Conformidade
| Verificacao | Falha resulta em |
|---|---|
| Treze atributos presentes (§2) | Carta devolvida por DEP-GOV |
| Limites nomeando a Capability dona (§2.1) | Carta devolvida |
| Indicador de saude, nao de volume (§2.2) | Carta devolvida por DEP-QAR |
| Custodio unico e apto (OW-01, OW-04, OW-05) | Carta vetada |
| Relacoes declaradas dos dois lados (RL-03) | Elo quebrado; bloqueia aprovacao |
| Combinacao de eixos valida (§3.5) | Carta devolvida |
| Maturidade sustentada por indicador (CL-06) | Rebaixamento compulsorio |

## 10. Evolucao Deste Framework

| Mudanca | Classe |
|---|---|
| Criar, especializar, fundir ou aposentar Capability | C2 (Tipo 1) |
| Alterar escopo, limites ou indicadores de uma Capability | C2 |
| Alterar classe estrategica | C2 |
| Alterar maturidade | C1, salvo → `madura` (C2) |
| Acrescentar dominio ao eixo 1 | **C3** — o conjunto de dominios e parte da identidade da arquitetura |
| Acrescentar classe ao eixo 2 ou maturidade ao eixo 3 | **C3** |
| Alterar a regra de vinculacao obrigatoria (§8) | **C3** |

### 10.1 Invariantes

| # | Invariante que nenhuma evolucao pode quebrar |
|---|---|
| CI-01 | Capability descreve **o que se sabe fazer**, nunca quem faz nem como (TC-1 a TC-6). |
| CI-02 | Custodia unica por Capability (OW-01, herda ES-01). |
| CI-03 | Profundidade de especializacao permanece 1 (RL-04, herda IV-04). |
| CI-04 | Sem dependencia circular dura (RL-01, herda DP-03). |
| CI-05 | Capabilities de Garantia sao custodiadas pela Guarda (OW-05, herda ES-02 e PI-05). |
| CI-06 | Todo componente permanece vinculado a ao menos uma Capability (§8). |
| CI-07 | Capability aposentada nunca e apagada (CL-03, herda MM-09). |

---

## Documentos relacionados

| Referencia | Relacao |
|---|---|
| [ADR-0002](../decisions/ADR-0002-adocao-da-camada-de-capabilities.md) | Decisao que adota esta camada |
| [RFC-0001](../rfcs/RFC-0001-camada-de-capabilities.md) | Proposta que originou |
| [`../capabilities/`](../capabilities/) | O catalogo e o mapa de dependencias |
| [TPL-capability](templates/TPL-capability.md) | Template da Carta |
| [FND-02 §9](02-estrutura-organizacional.md) | Escada de especializacao — Capability e a camada acima do degrau 5 |
| [FND-04 §6.2](04-governanca.md) | Teste de Especializacao aplicado tambem a Capabilities |

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-GOV | Framework inicial: 13 atributos, 3 eixos, 7 dominios, ciclo de 9 estagios, 7 tipos de relacao, vinculacao obrigatoria. Ratificado por ADR-0002. |
| 1.1.0 | 2026-07-28 | DEP-GOV | Emenda por ADR-0003: vinculacao obrigatoria estendida a **Projeto e Ferramenta**, unificando o alcance com PI-12; semantica do vinculo declarada para os dois tipos; consequencia arquitetural de §8.4 passa a valer sem excecao. |
| 1.2.0 | 2026-07-28 | DEP-QAR | Emenda C2 por ADR-0005: **RL-05b** — `verifica` nao admite par reflexivo; regra referenciada de FND-09 §6.3, nao reescrita. |
