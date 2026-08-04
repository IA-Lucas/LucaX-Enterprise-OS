---
id: FND-10
titulo: Enterprise Artifact Framework do LucaX Enterprise OS
tipo: fundacao
versao: 1.5.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-30
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0003, ADR-0005, ADR-0006, ADR-0007, ADR-0008, ADR-0009, ADR-0017, ADR-0019, ADR-0024]
substitui: []
substituido_por: null
ratificacao: ratificada
resumo: Contrato universal de todo artefato — atributos, tipos, ciclo, autoridade, linhagem, economia de contexto e regras de especializacao.
perfil_contexto: nucleo
confidencialidade: interno
revisor: DEP-QAR
---

# Enterprise Artifact Framework

> **Em vigor desde 2026-07-28.** A ratificacao explicita do Soberano sobre ADR-0006 esta
> registrada em [INC-2026-001 §11](../governance/incidents/INC-2026-001-ratificacao-inferida.md),
> fonte canonica unica do ato. A transicao `aprovado` → `ativo` e a operacao **O4** (§5.2),
> autorizada pela satisfacao da condicao de validade de **LM-02** (§5.4) — a primeira
> aplicacao completa da regra que este framework instituiu.

## Proposito

Definir o contrato universal de tudo que a organizacao cria, governa, consulta, evolui e
aposenta: que atributos todo artefato carrega, que tipos documentais existem, por que estados
passam, quem manda em cada classe, como se ligam, quanto contexto custam e quando devem ser
divididos, fundidos ou retirados.

**`Artefato` permanece arquetipo do Meta Model (FND-09 §4, A2) — este documento governa o
arquetipo, nao cria entidade.**

## Escopo

| Item | Definicao |
|---|---|
| **Inclui** | Contrato de atributos, Canon Semantico de tipos, registro de tipos documentais, operacoes de ciclo de vida sobre os estados oficiais, controle de mudanca por classe, linhagem, economia de contexto, motor de especializacao, templates e catalogo mestre. |
| **Nao inclui** | Nomenclatura e identificadores (FND-03); entidades, relacoes e matriz de autoridade (FND-09); classes de mudanca e rito (FND-04); formato de mensagem (FND-05); alocacao de memoria (FND-06); estrutura do ADR (FND-07); competencias (FND-08). |
| **Subordinado a** | [FND-01](01-constituicao.md), [FND-03](03-taxonomia.md), [FND-04](04-governanca.md), [FND-09](09-meta-model.md). |
| **Consumido por** | Todo artefato do sistema, presente e futuro. |

## Responsaveis

| Papel | Responsavel |
|---|---|
| Proprietario | DEP-GOV |
| Revisor independente | **DEP-QAR** (RM-06b — DEP-GOV nao revisa o que produz) |
| Custodia do catalogo mestre | DEP-GOV, com curadoria de DEP-KMS |
| Verificacao de aptidao | DEP-QAR |
| Aprovador de mudanca | SOBERANO (C3, indelegavel) |

---

## 1. O Que Este Framework E

### 1.1 A pergunta que ele responde

| Documento | Pergunta |
|---|---|
| FND-03 Taxonomia | Como as coisas se **chamam** e onde vivem? |
| FND-09 Meta Model | O que pode **existir** e como se liga? |
| **FND-10 Artifact Framework** | **O que todo artefato deve carregar, custar e obedecer?** |

A distincao e material. FND-09 declara que a entidade `SKL` existe e se relaciona com `CAP`.
FND-10 declara que **todo** artefato — uma Skill, um ADR, um indice — carrega resumo
operacional, perfil de contexto, revisor de papel distinto e linhagem verificavel.

### 1.2 O que ele **nao** faz

| Nao faz | Porque | Onde vive |
|---|---|---|
| Cria entidade | `Artefato` e arquetipo, nao entidade (MT-10, FND-09 §4.2) | FND-09 §5 |
| Cria ontologia formal | Nao ha evidencia de ambiguidade, consulta relacional nem automacao que a exija (§3.4) | — |
| Redefine estados | Reutiliza os oito de FND-03 §5 | FND-03 §5 |
| Redefine a matriz de autoridade | Deriva de FND-09 §8.2, com precedencia declarada | FND-09 §8.2 |
| Transforma tipo documental em entidade | Tipos sao formas de um mesmo tipo de entidade (§3.2) | §4 |

### 1.3 Tipo documental nao e entidade

Um mesmo tipo de entidade admite **varias formas documentais**. `FND` e uma entidade; a
Constituicao, um Framework e o Meta Model sao tres formas dela, com finalidades e autoridade
distintas — e nenhuma delas e entidade nova.

```
  ENTIDADE (FND-09 §5)        21, universo fechado, alterar e C3
       |
       +-- TIPO DOCUMENTAL    forma que a entidade assume, com finalidade propria
       |                      acrescentar e C2 (FND-09 §11.2, degrau 1)
       |
       +-- INSTANCIA          o artefato concreto
```

**Regra de leitura:** se uma "nova coisa" responde a mesma pergunta de uma entidade existente
e difere apenas em finalidade, conteudo ou publico, ela e **tipo documental** — nao entidade.
Foi assim que Constituicao, Framework, Playbook, Checklist e Handoff foram resolvidos sem
ampliar o universo.

## 2. Artifact Contract

### 2.1 Principio: declarar o minimo, derivar o resto

O contrato tem tres camadas. Confundi-las produz burocracia: exigir que cada artefato declare
o que pode ser computado transforma manutencao em trabalho manual e cria segunda fonte de
verdade (MM-01).

| Camada | O que e | Onde vive | Quem mantem |
|---|---|---|---|
| **L1 — Declarado** | Fatos que so o autor sabe | Frontmatter do proprio artefato | Autor |
| **L2 — Curado** | Fatos sobre o artefato, uteis a quem ainda nao o abriu | [Catalogo mestre](../governance/artifact-registry.md) | DEP-GOV + DEP-KMS |
| **L3 — Derivado** | Fatos computaveis a partir de L1 e L2 | **Nao se declara** | Ninguem — calcula-se |

> **Regra AC-01.** Atributo derivavel **nao** entra no frontmatter. Declara-lo cria segunda
> fonte de verdade e obriga manutencao dupla.

### 2.2 L1 — Atributos declarados

#### Nucleo universal — sem alteracao

Os quinze campos de [FND-03 §4](03-taxonomia.md) permanecem exatamente como estao:
`id` · `titulo` · `tipo` · `versao` · `status` · `camada_memoria` · `autor` ·
`proprietario` · `aprovador` · `criado_em` · `atualizado_em` · `revisao_prevista` ·
`decisoes_relacionadas` · `substitui` · `substituido_por`.

Mais os blocos obrigatorios de corpo: `## Proposito`, `## Escopo`, `## Responsaveis`.

#### Extensao do contrato — cinco campos novos

| Campo | Valores | Obrigatorio em | Valor padrao |
|---|---|---|---|
| `resumo` | Uma linha, ate 200 caracteres, em voz ativa | Artefato criado ou emendado **a partir da vigencia deste framework** | Curado no catalogo mestre para os anteriores (§2.3) |
| `perfil_contexto` | `nucleo` · `missao` · `sob-demanda` · `arquivo` | Idem | **Padrao por tipo**, na matriz §10.3 |
| `confidencialidade` | `publico` · `interno` · `restrito` · `soberano` | Idem | `interno` |
| `revisor` | `DEP-xxx` de papel distinto do `autor` | Todo artefato que exija revisao independente | — |
| `ratificacao` | `nao-exigida` · `pendente` · `ratificada` | Todo artefato de decisao **C3 ou Tipo 1** | `nao-exigida` |
| `projecao_de` | `<ID> §<secao>`, um por fonte projetada | Artefato cujo conteudo seja **majoritariamente** projecao — indice, catalogo, matriz derivada | **Ausente** = nao e projecao *(§2.6, PJ-02)* |

#### Campos condicionais, ja existentes

`capabilities` (Componentes) · `maturidade` (CAP) · `vigencia` (EXC) · `situacao` (INC) ·
`veredito` (FIT) · `origem`, `evidencia`, `confianca`, `ttl` (MEM) · `classe_mudanca`,
`tipo_decisao`, `supera`, `superado_por` (ADR) — todos definidos em FND-03 §4.1.

### 2.3 Migracao — custo zero para o acervo existente

EV-02 exige valor padrao declarado **ou** janela de migracao. Adota-se o valor padrao, e os
**76 artefatos existentes nao sao tocados**.

> **A data de corte e a vigencia, nao a criacao deste texto.** Como todo o acervo foi criado
> em 2026-07-28, fixar a obrigacao nessa data tornaria os 76 artefatos anteriores nao
> conformes — contradizendo a propria promessa de migracao zero. A obrigacao passa a valer
> para o artefato criado ou emendado **depois** que FND-10 entrar em vigor, o que so ocorre
> com a ratificacao (§5.4). Os artefatos desta missao ja declaram os campos **por
> demonstracao**, nao por obrigacao *(REV-ARTIFACT-2026-07-28 §0, D2)*.

| Campo | Como o acervo existente e atendido |
|---|---|
| `resumo` | Curado no catalogo mestre, uma linha por artefato — **sem reescrever conteudo nem criar arquivo auxiliar** |
| `perfil_contexto` | Padrao por tipo (§10.3), aplicado por referencia no catalogo |
| `confidencialidade` | Padrao `interno` para todo o acervo, declarado uma unica vez aqui |
| `revisor` | Nao retroativo (EV-03). Exigido de artefato novo e de emenda |
| `ratificacao` | Aplicado apenas onde ha C3/Tipo 1 — ja feito em FND-04, FND-08, FND-09, FND-10 |

> **Quando a obrigacao nasce.** O termo "emendado" e definido por **AC-08 a AC-11** (§2.5),
> instituidas por [ADR-0009](../decisions/ADR-0009-o-que-conta-como-emenda-de-artefato.md)
> como correcao do achado C13 de
> [REV-CONSOLIDACAO §10](revisao-arquitetural-consolidacao-2026-07-28.md).

### 2.4 L3 — O que **nao** se declara

| Atributo | Como se obtem | Por que nao se declara |
|---|---|---|
| **Consumidores** | Espelho de `dependencias` e das relacoes registradas | Declaracao dupla desatualiza de um lado so (RM-01 exige bilateralidade **no registro**, nao no frontmatter de cada um) |
| **Relacoes** | Grafo montado a partir de L1 + catalogo | Repetir a relacao em ambos os lados do frontmatter e a causa classica de elo quebrado |
| **Autoridade** | Funcao do tipo, em FND-09 §8.2 | Declarar por artefato permitiria divergencia da norma |
| **Custo de contexto** | Medido: linhas do arquivo | Metrica declarada e opiniao; metrica medida e fato (§8.4) |
| **Dependencias transitivas** | Fecho do grafo de `depende-de` | Explosao combinatoria; computa-se sob demanda |

### 2.5 Regras do contrato

| # | Regra |
|---|---|
| AC-01 | Atributo derivavel nao entra no frontmatter (§2.4). |
| AC-02 | `resumo` diz **o que o artefato faz**, nao o que ele e. "Contrato universal de todo artefato" serve; "documento sobre artefatos" nao. |
| AC-03 | `revisor` ≠ `autor`, sempre. Igualdade torna a aprovacao **nula** (LV-03, PI-05, RM-06b). |
| AC-04 | `ratificacao: ratificada` so e preenchido por papel distinto do executor, apos ato explicito e datado (CV-09). |
| AC-05 | `confidencialidade: soberano` implica que o artefato nao e citado em comunicacao externa nem em pacote de contexto sem autorizacao especifica (LV-08). |
| AC-06 | Campo obrigatorio ausente = artefato nao conforme = veto de DEP-GOV (FND-03 §10). |
| AC-07 | Nenhum campo novo pode ser acrescentado ao contrato sem valor padrao declarado ou janela de migracao com dono e prazo (EV-02). |
| **AC-08** | **"Emendado" (§2.2, §2.3) e a alteracao que incrementa MAIOR ou MENOR** do proprio artefato (FND-03 §6). A partir dela, os cinco campos sao obrigatorios **no artefato**, e sua ausencia e nao conformidade (AC-06). |
| **AC-09** | **`CORRECAO` nao dispara a obrigacao**, e **atualizacao derivada de artefato M3** pela mudanca que o afeta (CV-04, RG-03) tambem nao. Do contrario §2.3 se anularia primeiro nos artefatos mais mantidos — os indices, obrigados a acompanhar toda mudanca (IX-02). Mudanca de **estrutura ou escopo** do proprio indice incrementa MENOR e dispara AC-08. |
| **AC-10** | **Artefato M1 nunca e emendado** (§6.2), logo AC-08 nunca o alcanca. Corrige-se **superando**, e o sucessor ja nasce sob o contrato por ser artefato novo. |
| **AC-11** | **Alteracao de conteudo sem incremento de versao e nao conformidade a FND-03 §6**, nao terceira natureza de mudanca. Corrige-se declarando a versao devida no ato; a obrigacao decorre da versao corrigida, **nunca de efeito retroativo** (FND-01 §9, EV-03). |

### 2.6 Uma fonte, multiplas projecoes

> Instituida por [ADR-0008](../decisions/ADR-0008-uma-fonte-multiplas-projecoes.md), como
> correcao de **causa** de duas ressalvas consecutivas — R2 de FIT-2026-001 e R2 de
> FIT-2026-002. AC-01 proibe **declarar** o derivavel; esta secao governa o caso vizinho:
> **exibir** o que pertence a outro documento.

| # | Regra |
|---|---|
| **PJ-01** | **Tabela, matriz ou diagrama normativo vive em exatamente uma fonte.** Todo outro documento referencia, filtra ou projeta — nunca reproduz. Reproducao consistente hoje ja e defeito: o defeito e a segunda fonte de verdade, nao a divergencia (MM-01, FND-03 §7.1). |
| **PJ-02** | **Toda projecao se declara**, com quatro informacoes: **fonte** (ID e secao), **campos** projetados, **finalidade** (por que projetar em vez de linkar) e **metodo de atualizacao** (quem atualiza, sob que gatilho). Tabela derivada sem as quatro e reproducao, nao projecao. O campo opcional `projecao_de` no frontmatter torna a projecao detectavel por varredura; ausente = o artefato nao e projecao. |
| **PJ-03** | **Em divergencia, a fonte prevalece**, e o defeito e da projecao. Corrigir a fonte para caber na projecao e proibido — M3 (§6.2) generalizado a todo artefato. |
| **PJ-04** | **Campo de estado em artefato M1 registra o estado no ato, nunca o estado corrente.** Como o conteudo de M1 nunca muda (CC-01, LV-04), o estado corrente vive na fonte declarada. Aplica-se a `ratificacao` em ADR, ao `status` de instrumento e a todo campo futuro de mesma natureza. |
| **PJ-05** | **A verificacao de reproducao e do autor, antes da submissao** — item obrigatorio do checklist de [`TPL-documento`](templates/TPL-documento.md). A auditoria de coerencia interna (FND-04 §8) permanece como **segunda** barreira. Deteccao posterior nao substitui prevencao. |
| **PJ-06** | **O Fitness Check verifica a prevencao, nao so a ocorrencia.** F2 exige duas respostas: houve duplicacao? **e** o teste preventivo foi aplicado, com evidencia? |

**Aplicacao imediata de PJ-04.** O campo `ratificacao` dos ADRs C3/Tipo 1 permanece congelado
no valor que tinha na aprovacao. A fonte corrente do estado de ratificacao e
[INC-2026-001 §11](../governance/incidents/INC-2026-001-ratificacao-inferida.md); o indice de
decisoes a projeta.

## 3. Canon Semantico

### 3.1 O que e, e por que nao e ontologia

O Canon Semantico fixa **o significado de cada tipo documental** e o mapeia a exatamente uma
entidade do Meta Model. E vocabulario controlado com mapeamento — nao um modelo formal de
conceitos, propriedades e inferencia.

| | Canon Semantico *(adotado)* | Ontologia formal *(nao adotada)* |
|---|---|---|
| Objeto | Tipos documentais e seu mapeamento a entidades | Conceitos, propriedades, axiomas, inferencia |
| Forma | Tabela normativa em documento | Grafo com esquema e motor de consulta |
| Serve para | Eliminar ambiguidade de nome (LX-07) | Consulta relacional e deducao automatica |
| Custo | Uma secao | Modelo, ferramenta, manutencao, dependencia externa |

### 3.2 Regra do canon

> **CS-01.** Todo tipo documental mapeia a **exatamente uma** entidade de FND-09 §5. Tipo que
> nao mapeia nao existe (MT-01): ou e forma de um tipo existente, ou e secao de artefato, ou
> e projecao — nunca coisa nova.

> **CS-02.** Dois tipos documentais da mesma entidade diferem por **finalidade, conteudo
> permitido ou autoridade** — nunca apenas por nome. Diferenca so de nome e sinonimo,
> proibido por LX-07.

### 3.3 Termos resolvidos nesta missao

| Termo usado | Termo oficial | Regra |
|---|---|---|
| **Fundador** | `SOBERANO` | Designam a mesma autoridade. O termo oficial e SOBERANO (FND-01 §11); mudar exigiria emenda C3. Registrado em INC-2026-001 §7.1 |
| **Mission** | Mudanca **C2/C3**, ou `PRJ` quando houver prazo e alocacao | FND-09 §5.8, X-13 |
| **Ontology** | Canon Semantico (§3) | Esta secao; gatilho de promocao em §3.4 |
| **Artifact** | Arquetipo **A2**, nao entidade | FND-09 §4.2 |

### 3.4 Gatilho para promover o Canon a ontologia formal

A promocao exige **sinal observado**, nunca antecipacao (FND-08 §7.1). Qualquer um dos tres
abre RFC:

| # | Gatilho | Sinal verificavel |
|---|---|---|
| G1 | **Ambiguidade real** | Dois artefatos aprovados usando o mesmo termo com significados incompativeis, apos o Canon vigente |
| G2 | **Consulta relacional** | Pergunta recorrente que exige percorrer 3+ saltos de relacao e nao e respondivel pelo catalogo mestre |
| G3 | **Automacao real** | Existir consumidor programatico do grafo — nao a intencao de ter um |

**Estado em 2026-07-28:** nenhum dos tres observado. G3 e impossivel: nao existe codigo nem
infraestrutura. Registrado como decisao de nao decidir (FND-07 §9), com custo declarado: se a
ambiguidade surgir antes do reconhecimento, sera resolvida caso a caso ate o gatilho disparar.

## 4. Artifact Type Registry

Trinta e tres tipos documentais sobre 21 entidades. Coluna **Entidade** e o mapeamento CS-01.

> **Declaracao de projecao (PJ-02, [ADR-0008](../decisions/ADR-0008-uma-fonte-multiplas-projecoes.md)).**
> **Fonte:** [FND-03 §7](03-taxonomia.md), arvore canonica de diretorios.
> **Campos projetados:** apenas a coluna **Local**.
> **Finalidade:** o registro de tipos responde "que tipo e este, e onde vive" em uma leitura;
> exigir um salto por linha inviabilizaria o instrumento.
> **Metodo de atualizacao:** pela mesma mudanca que altera a arvore em FND-03 §7 (CV-04).
> Divergencia e defeito desta tabela, nunca da fonte (PJ-03). **Esta e a unica projecao da
> localizacao neste documento.**

### 4.1 Classe Normativa — o que obriga

| Tipo documental | Entidade | Finalidade | Conteudo proibido | Local | Template |
|---|---|---|---|---|---|
| **Constituicao** | `FND` | Lei fundamental; principios imutaveis e linhas vermelhas | Detalhe operacional; procedimento | `foundation/01-constituicao.md` | — *(instancia unica)* |
| **Documento Fundacional** | `FND` | Norma organizacional derivada da Constituicao | Contradicao com FND-01; instancia concreta | `foundation/NN-*.md` | `TPL-documento` |
| **Meta Model** | `FND` | Universo de entidades, relacoes e autoridade | Instancias; conteudo de tipo | `foundation/09-meta-model.md` | — *(instancia unica)* |
| **Framework** | `FND` | Norma que estrutura um dominio inteiro e e consumida por todos | Decisao pontual *(isso e ADR)* | `foundation/NN-*.md` | `TPL-documento` |
| ~~Norma Derivada~~ | — | **Recusada** — X-05/X-06 de FND-09 §5.8. Slot nomeado, sem instancia | — | — | — |

> **Constituicao, Meta Model e Framework sao a mesma entidade `FND`** com autoridade
> diferente: a primeira prevalece sobre tudo (FND-01 §10, nivel 1); as demais ocupam o
> nivel 2, e o Meta Model tem precedencia parcial sobre os pares (FND-09 §1.4).

### 4.2 Classe Decisoria — o que resolve

| Tipo documental | Entidade | Finalidade | Conteudo proibido | Local | Template |
|---|---|---|---|---|---|
| **ADR** | `ADR` | Decisao tomada, com alternativas e reversao | Edicao apos aprovado (LV-04) | `decisions/` | `TPL-adr` |
| **RFC** | `RFC` | Pergunta em aberto submetida a analise | Decisao ja tomada | `rfcs/` | `TPL-rfc` |
| **Nota de Decisao** | `MEM` *(OPR)* | Escolha C1/Tipo 2 de escopo local | Precedente — vira ADR | `memory/operacional/` | `TPL-nota-decisao` |
| **Excecao Formal** | `EXC` | Autorizacao temporaria e nominal do Soberano | Prazo ausente *(invalida)* | `governance/exceptions/` | `TPL-excecao` |
| **Incidente** | `INC` | Violacao detectada, causa e correcao | Fechamento sem correcao de causa | `governance/incidents/` | `TPL-incidente` |

### 4.3 Classe Constitutiva — o que da existencia

| Tipo documental | Entidade | Finalidade | Conteudo proibido | Local | Template |
|---|---|---|---|---|---|
| **Carta de Capability** | `CAP` | Competencia permanente, 13 atributos | Citar produto especifico (TC-6) | `capabilities/` | `TPL-capability` |
| **Carta de Departamento** | `DEP` | Dominio de responsabilidade exclusivo | Escopo sobreposto a area vizinha | `departments/<dep>/` | `TPL-carta-departamento` |
| **Carta de Agente** | `AGT` | Papel executor, com autonomia declarada | Omitir "o que nao me compete" | `departments/<dep>/agents/` | `TPL-carta-agente` |
| **Carta de Subagente** | `SUB` | Recorte estreito dentro de um papel | Subagente proprio (profundidade 1) | `.../agents/sub/` | `TPL-carta-agente` |
| **Carta de Produto** | `PRO` | Bem digital com publico e ciclo proprios | Criterio de encerramento ausente | `products/<slug>/` | `TPL-carta-produto` |
| **Carta de Projeto** | `PRJ` | Esforco temporario com resultado definido | Criterio de encerramento ausente | `projects/<PRJ-id>/` | `TPL-carta-projeto` |
| **Ficha de Ferramenta** | `TOL` | Capacidade externa, com custo e descarte | **Credencial em texto** (PI-08) | `tools/` | `TPL-ferramenta` |

### 4.4 Classe Executavel — o que se faz

| Tipo documental | Entidade | Finalidade | Conteudo proibido | Local | Template |
|---|---|---|---|---|---|
| **Spec** | `SPC` | O que deve existir e como se verifica | Arquitetura, tecnologia, implementacao | `products/<slug>/specs/` | `TPL-spec` |
| **Skill** | `SKL` | Procedimento reutilizavel com resultado verificavel | Procedimento de um unico papel | `skills/` | `TPL-skill` |
| **Workflow** | `WFL` | Sequencia com etapas, responsaveis e portoes | Etapa unica sem portao *(e Skill)* | `workflows/` | `TPL-workflow` |
| **Template** | `TPL` | Forma de um tipo documental | Conteudo normativo proprio | `foundation/templates/` | *(e o proprio)* |

### 4.5 Classe Avaliativa — o que julga

| Tipo documental | Entidade | Finalidade | Conteudo proibido | Local | Template |
|---|---|---|---|---|---|
| **Fitness Check** | `FIT` | Veredito de **aptidao evolutiva** de uma mudanca | Resposta sem sinal observavel (FT-03) | `governance/fitness/` | `TPL-fitness-check` |
| **Revisao Arquitetural** | `FIT` | Parecer de **corretude estrutural** de uma camada | Achado sem severidade, dono e gatilho | Ao lado do que revisa | `TPL-documento` |

> **Por que os dois compartilham a entidade `FIT` (ADR-0006).** Sao a mesma natureza: parecer
> datado, emitido por DEP-QAR ao encerrar mudanca estrutural, imutavel e superavel. O que
> ADR-0004 §6 proibiu foi **fundir os vereditos** — e eles permanecem em documentos separados,
> com vereditos separados. O que se unifica e o tipo de entidade, distinguido pelo eixo
> `classe_avaliacao: corretude | aptidao`. O ID `FIT` e preservado (LX-08); a Revisao usa
> prefixo proprio `REV`, registrado em FND-03 §2.

### 4.6 Classe Cognitiva — o que se sabe e se transfere

| Tipo documental | Entidade | Finalidade | Conteudo proibido | Local | Template |
|---|---|---|---|---|---|
| **Memoria EST / PRD / TEC / OPR / APR** | `MEM` | Conhecimento persistente em uma camada | Registro em duas camadas (MM-01) | `memory/<camada>/` | `TPL-memoria` |
| **Handoff** | `MSG` | Transferencia de trabalho e responsabilidade | Transferir sem aceite (HO-01) | `memory/operacional/` | `TPL-handoff` |
| **Reporte** | `MSG` | Estado, resultado ou conclusao | Reporte sem **Evidencia** (RP-01) | `memory/operacional/` | `TPL-reporte` |
| **Diretiva / Consulta / Alerta** | `MSG` | Determinar · obter parecer · comunicar risco | Mais de um pedido (CM-05) | `memory/operacional/` | envelope FND-05 §3 |

### 4.7 Classe de Registro — o que indexa

| Tipo documental | Entidade | Finalidade | Conteudo proibido | Local | Template |
|---|---|---|---|---|---|
| **Indice / Catalogo** | *a entidade que indexa* | Registro oficial e contador de uma sequencia | **Informacao original** — conteudo e 100% derivado | `README.md` do diretorio da entidade | `TPL-documento` |

> **Por que o Indice nao e entidade.** Ele e o **registro oficial da entidade que indexa**:
> `decisions/README.md` e o contador da sequencia `ADR`, e FND-03 §2.3 ja atribui esse
> contador a DEP-GOV. O indice materializa uma funcao da entidade, nao uma coisa nova.
> **Regra IX-01:** indice que contenha informacao inexistente na fonte esta em defeito —
> a informacao deve ser movida para a fonte e referenciada. **Regra IX-02:** indice
> desatualizado apos mudanca aprovada e **mudanca incompleta** (CV-04), nao norma nova.
> **Regra IX-03:** um indice pode indexar **mais de uma sequencia** quando elas sao
> co-localizadas — `governance/README.md` indexa `EXC`, `INC` e `FIT`; o `README.md` da raiz
> indexa o acervo. Nesse caso a entidade e o **conjunto** indexado, e o contador oficial de
> cada sequencia permanece unico e nao duplicado *(REV-ARTIFACT-2026-07-28 §0)*.

### 4.8 Tipos recusados

| Candidato | Por que nao e tipo | Onde vive | Gatilho de reabertura |
|---|---|---|---|
| **Norma Derivada** | Sem instancia: nao existe regra vigente que nao caiba em `FND`, `ADR` ou `TPL` | FND + ADR + TPL | Primeira regra vigente que nao caiba nos tres |
| **Command** | Forma de acionamento, nao artefato | Atributo `gatilho` de `SKL`/`WFL` | Superficie com ciclo de vida independente do procedimento |
| **Prompt** | Materializacao textual de Carta de agente ou corpo de Skill | Carta `AGT`/`SUB`; corpo de `SKL` | Nenhum — prompt reusado por 2+ componentes **ja e** Skill |
| **Playbook** | Nome de uso para procedimento recorrente | `SKL` se um papel; `WFL` se atravessa papeis ou tem portao | Procedimento com ramificacao condicional que nenhum dos dois comporte |
| **Checklist** | **Secao** de artefato, nao artefato. Tres instancias observadas, todas como secao | Secao de `TPL`, `ADR` e `FIT` | Checklist reusado por 3+ tipos, com versao propria |
| **Evaluation** | Nome guarda-chuva de Fitness Check e Revisao Arquitetural | Entidade `FIT`, dois tipos documentais (§4.5) | — |

## 5. Lifecycle e Maturity

### 5.1 Nenhum estado novo

Os oito estados de [FND-03 §5](03-taxonomia.md) e os quatro perfis de
[FND-09 §7.2](09-meta-model.md) valem integralmente e **nao sao redefinidos aqui**. Este
framework define as **operacoes** que produzem transicoes entre eles.

### 5.2 As nove operacoes

| # | Operacao | Transicao | Criterio verificavel | Rollback |
|---|---|---|---|---|
| O1 | **Criacao** | — → `rascunho` | Pre-condicoes do tipo (FND-04 §6); tipo consta de §4 | Descartar: vai a `arquivado`, numero nao retorna |
| O2 | **Experimento** | `rascunho` → `rascunho` | Uso real do artefato antes de submete-lo, com resultado registrado | Nenhum — nao vincula ninguem |
| O3 | **Validacao** | `rascunho` → `em-revisao` | Revisor de papel distinto designado (`revisor` ≠ `autor`) | Volta a `rascunho` |
| O4 | **Promocao** | `em-revisao` → `aprovado` → `ativo` | Revisao concluida **e** — se C3/Tipo 1 — **ratificacao explicita** (§5.4) | `aprovado` → `arquivado`; `ativo` exige superacao |
| O5 | **Revisao** | `ativo` → `ativo` | Gatilho temporal ou por evento disparado; resultado registrado | Nenhum — a revisao e ato, nao estado |
| O6 | **Superacao** | `ativo`/`depreciado` → `superado` | Sucessor `ativo`; **todos** os dependentes migrados (LC-05) | Novo artefato superando o sucessor; o original **nao** volta |
| O7 | **Depreciacao** | `ativo` → `depreciado` | Substituicao ja decidida e nomeada | Volta a `ativo` por ADR, se a substituicao for cancelada |
| O8 | **Arquivamento** | `rascunho`/`em-revisao` → `arquivado` | Encerrado sem ter vigorado | Novo artefato com **novo ID** |
| O9 | **Retirada** | `ativo`/`depreciado` → `revogado` | Anulado sem substituto; declara-se o que passa a valer no lugar (SU-04) | Novo artefato com **novo ID** — revogado nunca retorna |

### 5.3 Maturidade e ortogonal ao estado

`status` descreve o **documento**; `maturidade` descreve a **coisa**. Os eixos ortogonais
estao em [FND-09 §7.3](09-meta-model.md) e nao sao reproduzidos aqui.

> **LM-01.** Maturidade declarada sem indicador medido e devolvida (CL-06, LC-09). Vale para
> `maturidade`, `veredito`, `situacao` e `vigencia`.

### 5.4 Ratificacao e condicao de entrada em `ativo`

> **LM-02 — correcao de causa de [INC-2026-001](../governance/incidents/INC-2026-001-ratificacao-inferida.md).**
> Para artefato de decisao **C3 ou Tipo 1**, a ratificacao explicita do Soberano e
> **condicao de validade**, nao ressalva. Sem ato explicito e datado **sobre o texto final**,
> o artefato permanece em `aprovado` e **nao entra em `ativo`**.

| Situacao | `ratificacao` | `status` maximo |
|---|---|---|
| Classe nao exige ratificacao | `nao-exigida` | `ativo` |
| Exige, e o ato ocorreu | `ratificada` | `ativo` |
| Exige, e o ato nao ocorreu | **`pendente`** | **`aprovado`** |

| # | Regra |
|---|---|
| LM-03 | Instrucao generica anterior, determinacao originadora, precedente e silencio **nao ratificam** (PI-01, PI-06, GV-05, CM-07). |
| LM-04 | Preencher a secao de ratificacao com inferencia, ainda que fundamentada e com ressalva, e violacao de **LV-05** e torna o registro nulo. |
| LM-05 | Quem registra a ratificacao e papel **distinto** de quem executou a mudanca (CV-09). |
| LM-06 | **Ressalva nao neutraliza condicao de validade** ([MEM-APR-0001](../memory/aprendizado/MEM-APR-0001-ratificacao-por-precedente.md)). Descrever com precisao por que a condicao pode nao estar satisfeita nao a satisfaz. |

### 5.5 Rollback

| # | Regra |
|---|---|
| RB-01 | Rollback e transicao registrada, com responsavel e data — nunca reversao silenciosa (LC-01). |
| RB-02 | Artefato que ja esteve em `ativo` **nunca volta** a `rascunho` (FND-03 §5.1). Corrigir e **superar**. |
| RB-03 | Instrumento em `aprovado` tem conteudo imutavel: rollback altera estado, nunca texto (LV-04). |
| RB-04 | Rollback de O6 exige que os dependentes ja migrados sejam remigrados — e parte da mesma mudanca (CV-04). |
| RB-05 | **Remocao fisica de arquivo que ja esteve em `ativo` e proibida** (FND-04 §7.2, PI-07). |

## 6. Authority e Change Control

### 6.1 Quem manda: derivado, nao redefinido

A matriz de autoridade por entidade esta em [FND-09 §8.2](09-meta-model.md) e **nao e
reproduzida aqui**. Em conflito, prevalece FND-09; a divergencia e erro deste documento.

Este framework acrescenta apenas o que e proprio do artefato como **documento**:

| Ato | Quem | Regra propria |
|---|---|---|
| **Propor** | Qualquer departamento no escopo | Proponente ≠ Aprovador (PI-05) |
| **Criar** | Autor designado | Pre-condicoes do tipo (FND-04 §6) |
| **Revisar** | `revisor`, papel distinto do `autor` | AC-03; nunca o proprio produtor (RM-06b) |
| **Aprovar** | Conforme FND-09 §8.2 | Nunca quem propos ou executou (LV-03) |
| **Ratificar** | **SOBERANO**, indelegavel | §5.4; ato explicito sobre o texto final |
| **Alterar** | Proprietario | §6.2 — depende da classe de mutabilidade |
| **Superar** | Autor do sucessor | Explicar **o que mudou** (SU-01) |
| **Aposentar** | Conforme FND-09 §8.2 | Destino explicito de cada dependente (EV-06) |

### 6.2 Tres classes de mutabilidade

| Classe | Tipos | Regra | Correcao se houver erro |
|---|---|---|---|
| **M1 — Imutavel apos eficacia** | ADR, RFC decidida, EXC, INC fechado, FIT, REV | O texto **nunca** muda. Muda apenas o estado e os campos de sucessao | **Superar** com novo artefato que o referencia (LV-04) |
| **M2 — Versionavel** | FND, CAP, Cartas, SPC, SKL, WFL, TOL, TPL, MEM | Emenda por versao; texto anterior preservado no historico | Nova versao MAIOR ou MENOR, conforme o efeito (AL-01) |
| **M3 — Derivado** | Indice, catalogo | Atualizado como parte da mudanca que o afeta | Reprocessar a partir da fonte; **nunca** editar a fonte para caber no indice |

> **CC-01.** ADR historico **nunca e editado** — nem para corrigir erro, nem para completar
> campo, nem para registrar ratificacao posterior. A ratificacao superveniente e registrada
> no indice e no incidente correspondente, e o ADR permanece intacto.

### 6.3 Regras de controle de mudanca

| # | Regra |
|---|---|
| CC-02 | Alteracao segue a classe do **efeito**, nao do tamanho do texto (AL-01). |
| CC-03 | Alteracao em cascata e parte da mesma mudanca. Artefato dependente desatualizado = mudanca **incompleta** (CV-04). |
| CC-04 | Mudanca C2/C3 nao encerra sem Fitness Check emitido (CV-07, QG-6). |
| CC-05 | Mudanca em documento fundacional passa por auditoria de **coerencia interna**: tabela ou diagrama reproduzido de outro documento e defeito (FND-04 §8). |
| CC-06 | Artefato M1 com erro material gera **novo artefato** e, quando o erro tiver causa relevante, registro APR. |

## 7. Lineage e Relationships

### 7.1 Vocabulario: nove verbos, dez relacoes

Os verbos pedidos pela missao **nao sao relacoes novas**: sao leituras das dez relacoes de
[FND-09 §6.1](09-meta-model.md), registradas na tabela de verbos de §6.1.1 daquele documento.

| Verbo de linhagem | Relacao oficial | Bilateral? | Ciclo? |
|---|---|---|---|
| `deriva-de` | R-04 `depende-de` | Sim | **Nao** |
| `implementa` | R-04 `depende-de` | Sim | **Nao** |
| `depende-de` | R-04 | Sim | **Nao** |
| `consome` | R-05 `consome-saida-de` | Sim | Sim |
| `produz` | R-05 `fornece-para` | Sim | Sim |
| `valida` | R-06 `verifica` | Sim | Sim, **exceto reflexivo** (RM-06b) |
| `evidencia` | R-09 `registra` | Nao — o registro aponta a fonte | Sim |
| `substitui` | R-08 `supera` | Sim | **Nao** |
| `restringe` | **Ato de autoridade**, nao relacao estrutural | — | — |

> **`restringe` nao entra no grafo.** Subordinacao normativa — a Constituicao restringe tudo —
> e resolvida pela hierarquia de FND-01 §10 e pela matriz de FND-09 §8, nao por aresta de
> dependencia. Trata-la como relacao criaria dependencia ascendente universal, violando PD-11.

### 7.2 Regras de linhagem

| # | Regra |
|---|---|
| LN-01 | **Bilateralidade e do registro, nao do frontmatter.** A relacao e declarada uma vez, na fonte, e o espelho e derivado (AC-01, §2.4). Exigir declaracao nos dois frontmatters e a causa classica de elo quebrado. |
| LN-02 | Excecao a LN-01: `substitui`/`substituido_por` **sao** declarados nos dois lados, porque a sucessao precisa ser legivel sem consultar o catalogo. |
| LN-03 | Relacao com artefato `depreciado`, `superado` ou `revogado` nao pode ser **criada** (DP-04, RM-07). |
| LN-04 | Par origem-destino fora de FND-09 §6.2 e **nulo** (RM-02). |
| LN-05 | Ciclo em `deriva-de`, `implementa`, `depende-de` e `substitui` e **proibido** (PD-01). Em `consome`, `produz`, `valida` e `evidencia` e permitido. |
| LN-06 | `valida` **nao admite reflexivo**: nenhum artefato valida a si proprio (RM-06b, LV-03, ADR-0005). |

### 7.3 Cadeia de rastreabilidade obrigatoria

Todo artefato deve permitir percorrer, sem consultar pessoa:

```
  ORIGEM            ->  ESTADO            ->  SUBSTITUICAO
  RFC / ADR / INC       status +              substitui /
  que o autorizou       ratificacao           substituido_por
        |                    |                      |
   decisoes_             frontmatter           frontmatter
   relacionadas                                 + indice
```

| # | Regra |
|---|---|
| LN-07 | Artefato sem **origem** identificavel e nao confiavel ate ser saneado (PI-03). |
| LN-08 | Artefato cuja **substituicao** nao seja legivel a partir dele proprio quebra a cadeia — LN-02 existe por isso. |
| LN-09 | A cadeia e verificada na auditoria de integridade referencial (FND-04 §8). |

## 8. Context Economy

### 8.1 O problema

O acervo tem **18.916 linhas em 85 artefatos** (medicao de 2026-07-28, `wc -l`). Carregar
tudo para executar qualquer tarefa e inviavel e contraria PI-14, que manda **reduzir** o
contexto necessario por papel.

### 8.2 Quatro perfis de carregamento

| Perfil | Quando carrega | Quem carrega | Regra |
|---|---|---|---|
| `nucleo` | **Sempre** | Todo papel, em toda tarefa | Conjunto minimo, deliberadamente pequeno. Ampliar exige **C2** |
| `missao` | Quando a tarefa e do dominio do artefato | O papel designado | Declarado no pacote de contexto da missao |
| `sob-demanda` | Quando o gatilho de ativacao dispara | Quem precisa, no momento em que precisa | Referenciado por ID; conteudo so se o gatilho ocorrer |
| `arquivo` | Nunca por padrao | Auditoria e investigacao historica | `superado`, `revogado`, `arquivado` |

> **CE-01 — proibicao de carregamento integral.** Nenhum papel carrega o acervo por padrao.
> Carregar artefato fora do perfil exige gatilho declarado. Violar isto e falha de curadoria,
> nao zelo (PC-01).

### 8.3 O que substitui o carregamento

| Instrumento | O que entrega | Onde vive |
|---|---|---|
| **Resumo operacional** | Uma linha: o que o artefato faz | `resumo` no frontmatter; curado no catalogo para o acervo anterior |
| **Gatilho de ativacao** | A condicao que torna o artefato necessario | Catalogo mestre, coluna Gatilho |
| **Dependencias minimas** | O que precisa vir junto, e so isso | Catalogo mestre |
| **Custo medido** | Linhas do arquivo | Catalogo mestre, medido |

### 8.4 Custo de contexto: medido, nunca estimado

| # | Regra |
|---|---|
| CE-02 | O custo de um artefato e o **numero de linhas do arquivo**, medido. Nao se estima, nao se declara, nao se arredonda. |
| CE-03 | O custo de um perfil e a soma dos custos dos artefatos nele. |
| CE-04 | Metrica sem fonte e sem valor observado nao entra em nenhum artefato (LV-12). "Reducao esperada de 40%" e proibido; "1.205 linhas, medido em 2026-07-28" e obrigatorio. |
| CE-05 | Artefato que ultrapasse **o dobro da mediana do seu tipo** e candidato a especializacao (§9), nao por estetica, mas porque o custo de carrega-lo passou a ser desproporcional. |

### 8.5 Nucleo obrigatorio vigente

Definido por exclusao: e o que um papel precisa para **nao violar norma**, nao o que seria
util saber.

| Artefato | Custo medido em `BL-2026-07-29-10` | Por que e nucleo |
|---|---|---|
| FND-01 Constituicao | 485 | Principios imutaveis e linhas vermelhas |
| FND-03 Taxonomia | 631 | Nomear e localizar qualquer coisa |
| FND-09 §5, §6.2, §8.2 | *parcial* | O tipo existe? que relacao vale? quem aprova? |
| FND-10 §2, §4 | *parcial* | Que contrato o artefato deve cumprir |

**Custo do nucleo: 1.116 linhas integrais + dois recortes parciais**, contra 51.698 do acervo
— **2,2% medido**. **Os quatro valores acima sao os da baseline `BL-2026-07-29-10` e so se leem
contra ela**: numerador e denominador vem da **mesma** medicao, e **nenhum dos dois e perene**.
A cada baseline nova, **remede-se ou cita-se a baseline em que o valor vale** — nunca se deixa o
numero solto. **Foi a ausencia desta regra de leitura que manteve os valores de 2026-07-28
vigorando como se fossem correntes** — achado `RD-27`, item *(c)*, e `RD-46`, que mediu **cinco**
valores defasados nesta secao onde `RD-27` contara **tres**. Ampliar o nucleo e mudanca **C2**, com
Fitness Check obrigatorio.

> FND-09 tem **1.263 linhas** — o maior artefato do acervo, e a razao pela qual entra no
> nucleo por **recorte de secoes**, nao integralmente. Registrado como sinal de CE-05 na
> revisao arquitetural desta missao.

## 9. Specialization Engine

### 9.1 Delimitacao — quatro motores, quatro objetos

Nao ha duplicacao com os testes existentes: cada um age sobre objeto distinto.

| Motor | Objeto | Onde |
|---|---|---|
| Teste de Especializacao | **Componente** (departamento, agente, skill...) | FND-04 §6.2 |
| Criterios de evolucao de Capability | **Competencia** | FND-08 §7 |
| Teste de Entidade | **Tipo de entidade** | FND-09 §11.1 |
| **Motor de Especializacao de Artefato** | **Documento** | **§9 deste framework** |

### 9.2 Os sete sinais

Nenhum autoriza sozinho. Cada um exige **valor observado**, nunca previsto.

| # | Sinal | Como se verifica | Ganho PI-14 |
|---|---|---|---|
| S1 | **Responsabilidades independentes** | O artefato e alterado por motivos que nao se parecem entre si | Organizacao |
| S2 | **Cadencias distintas** | Duas partes mudam em ritmos diferentes; uma versiona sozinha repetidamente | Organizacao |
| S3 | **Reuso** | Uma parte e citada por consumidores que ignoram o resto | Reuso |
| S4 | **Propriedade diferente** | Duas partes tem `proprietario` de fato distinto | Organizacao |
| S5 | **Baixa precisao de recuperacao** | Consultas ao artefato quase sempre usam a mesma fracao dele | Reducao de contexto |
| S6 | **Conflito de autoridade** | Duas partes exigem aprovadores diferentes | Organizacao |
| S7 | **Custo de contexto** | Ultrapassa o dobro da mediana do tipo (CE-05) | Reducao de contexto |

### 9.3 Os quatro movimentos

| Movimento | Condicao | Instrumento |
|---|---|---|
| **Criar** | Ha responsabilidade documental sem artefato; nao cabe em nenhum existente sem distorce-lo | Pre-condicoes do tipo (FND-04 §6) |
| **Dividir** | **≥ 2 sinais observados**, e cada parte resultante tem proprietario, consumidor e cadencia proprios | C2 + destino explicito de cada secao |
| **Fundir** | Duas partes sempre alteradas juntas; consumidores identicos; fronteira que ninguem enuncia sem ambiguidade | C2; artefato novo com ID novo; os anteriores viram `superado` |
| **Aposentar** | Sem recuperacao ao longo de um horizonte inteiro (RC-05); ou o objeto que descreve deixou de existir | C2 + destino de cada dependente |

### 9.4 Regras do motor

| # | Regra |
|---|---|
| SE-01 | **Ganho previsto nao autoriza divisao.** Sinal observado e obrigatorio; a proposta declara qual, com valor medido e data (PI-14 regra 1). |
| SE-02 | Um unico sinal nao basta para dividir. Dividir com um sinal e fragmentacao. |
| SE-03 | **Divisao nao cria orfaos:** cada secao do original recebe destino explicito (PI-14 regra 3). |
| SE-04 | Todo ADR que divide declara o ganho e a **data de reavaliacao**. Ganho nao confirmado abre proposta de fusao (EV-08). |
| SE-05 | **Fusao e o movimento simetrico e igualmente obrigatorio.** Nao se mantem divisao por inercia. |
| SE-06 | Nao especializar tambem e decisao: constatado o sinal e adiada a divisao, registra-se o adiamento com motivo e custo (FND-07 §9). |
| SE-07 | Especializacao de artefato **nunca cria entidade nem tipo documental novo** por efeito colateral. Se criar, e mudanca C2/C3 propria (§4, FND-09 §11). |

## 10. Templates e Registro

### 10.1 Template universal: estender, nao criar

Existe `TPL-documento`, com a estrutura minima de qualquer documento. **Criar um segundo
template universal seria duplicacao** — exatamente o que este framework proibe.

`TPL-documento` passa a **versao 1.1.0**, incorporando os cinco campos do contrato estendido
(§2.2) e o bloco de linhagem. Nenhum template especializado e criado nesta missao.

### 10.2 Quando um template especializado se justifica

| # | Teste | Se falhar |
|---|---|---|
| T1 | O tipo tem campos obrigatorios que `TPL-documento` nao comporta? | Use `TPL-documento` |
| T2 | O tipo tem estrutura de corpo propria e recorrente? | Use `TPL-documento` |
| T3 | O tipo ja ocorreu ao menos **duas vezes**? | Espere a segunda ocorrencia |
| T4 | A ausencia do template ja produziu artefato nao conforme? | Sinal ausente — nao crie |

Os 19 templates vigentes foram verificados contra T1–T4 nesta missao: **19 de 19 passam**.

### 10.3 Matriz tipo × autoridade × ciclo × perfil

Perfil de contexto padrao por tipo, aplicavel por referencia ao acervo (§2.3).

> **Declaracao de projecao (PJ-02).** As colunas **Aprova** e **Ratifica** sao projecao de
> [FND-09 §8.2](09-meta-model.md); em conflito, prevalece a fonte (§6.1, PJ-03). A
> **localizacao** de cada tipo **nao e reproduzida aqui**: vive em [FND-03 §7](03-taxonomia.md)
> e esta declarada na coluna Local de §4.1 a §4.7, que e a unica projecao dela neste
> documento. Finalidade da matriz: responder, em uma leitura, quem manda e quanto custa
> carregar cada tipo. Atualizacao: pela mesma mudanca que altera a fonte (CV-04).

| Tipo documental | Aprova | Ratifica | Mutabilidade | Perfil padrao |
|---|---|---|---|---|
| Constituicao | SOBERANO | SOBERANO | M2 | `nucleo` |
| Documento Fundacional | SOBERANO | SOBERANO | M2 | `missao` |
| Meta Model | SOBERANO | SOBERANO | M2 | `nucleo` *(por recorte)* |
| Framework | SOBERANO | SOBERANO | M2 | `missao` |
| ADR | conforme classe | SOBERANO se C3/Tipo 1 | **M1** | `sob-demanda` |
| RFC | DEP-GOV valida forma | — | **M1** | `sob-demanda` |
| Nota de Decisao | Proprietario + revisor | — | M2 | `sob-demanda` |
| Excecao Formal | SOBERANO | SOBERANO | **M1** | `missao` |
| Incidente | DEP-GOV registra | — | **M1** *(apos fechado)* | `missao` |
| Carta de Capability | SOBERANO | SOBERANO | M2 | `sob-demanda` |
| Carta de Departamento | SOBERANO | SOBERANO | M2 | `missao` |
| Carta de Agente / Subagente | DEP-EXE | SOBERANO se Tipo 1 | M2 | `sob-demanda` |
| Carta de Produto / Projeto | SOBERANO / DEP-EXE | SOBERANO | M2 | `sob-demanda` |
| Ficha de Ferramenta | DEP-EXE | SOBERANO | M2 | `sob-demanda` |
| Spec | conforme classe | SOBERANO se C3/Tipo 1 | M2 | `sob-demanda` |
| Skill | DEP-EXE | — | M2 | `sob-demanda` |
| Workflow | DEP-EXE | — | M2 | `sob-demanda` |
| Template | DEP-GOV | — | M2 | `sob-demanda` |
| Fitness Check | DEP-EXE | **—** *(`FT-10`)* | **M1** | `missao` |
| Revisao Arquitetural | DEP-EXE | — | **M1** | `missao` |
| Memoria EST | DEP-GOV | SOBERANO | M2 | `missao` |
| Memoria PRD / TEC / APR | DEP-KMS | — | M2 | `sob-demanda` |
| Memoria OPR | DEP-KMS | — | M2 | `missao` |
| Mensagem | destinatario (aceite) | — | **M1** | `missao` |
| Indice / Catalogo | DEP-GOV | — | **M3** | `sob-demanda` |

> **A linha `Fitness Check` acompanha a fonte.** A coluna **Ratifica** desta matriz e projecao
> de [FND-09 §8.2](09-meta-model.md) (PJ-02); a alteracao ali e **fonte**, e esta e **cascata**
> (CV-04). O fundamento e **`FT-10`** de
> [ADR-0015](../decisions/ADR-0015-fitness-check-e-parecer-nao-decisao.md): parecer nao se
> ratifica. `Revisao Arquitetural` **ja** declarava `—` e **nao muda**.

**A linha `Spec` acompanha a fonte.** As colunas *Aprova* e *Ratifica* desta matriz sao
projecao de FND-09 §8.2 (PJ-02); a alteracao ali e **fonte**, e esta e **cascata** (CV-04).
O fundamento e que **aprovar o artefato e liberar o portao sao atos distintos**: `QG-1` e
liberado por **DEP-EXE** (FND-01 §6.2) e **nao e** a aprovacao da Spec, que segue a **classe
da mudanca** (FND-04 §2), com **C1 como piso** (FND-04 §6). **Nenhum titular ampliado.**

*Coluna Local removida por [ADR-0008](../decisions/ADR-0008-uma-fonte-multiplas-projecoes.md),
fechando a ressalva **R2** de [FIT-2026-002](../governance/fitness/FIT-2026-002-artifact-framework.md)
e a acao **A7** de REV-ARTIFACT §10.*

### 10.4 Catalogo mestre

O catalogo vive em [`governance/artifact-registry.md`](../governance/artifact-registry.md) e
e o unico lugar onde o acervo inteiro e listado com resumo, tipo, entidade, perfil e custo
medido.

| # | Regra |
|---|---|
| RG-01 | O catalogo e **vista derivada** (M3): nao contem informacao original. Toda linha aponta ao artefato-fonte. |
| RG-02 | Artefato criado sem entrada no catalogo e **nao localizavel** — falha DoD-7. |
| RG-03 | Catalogo desatualizado apos mudanca aprovada e **mudanca incompleta** (CV-04), nao norma nova. |
| RG-04 | O catalogo **nao** substitui os indices por diretorio: aqueles sao contadores oficiais de sequencia (FND-03 §2.3); este e a visao transversal do acervo. |
| RG-05 | **Nenhum arquivo auxiliar por artefato.** A classificacao vive no catalogo, por referencia e metadado — nunca em um arquivo satelite por documento. |
| RG-06 | O catalogo carrega a **proveniencia** de cada artefato como campo **curado (L2)**, com valor padrao `native` — nunca no frontmatter. Vocabulario e portao de admissao em [ADR-0007 §5.5](../decisions/ADR-0007-fronteira-greenfield-legado.md); esta e a fonte, e a coluna do catalogo e projecao dela (PJ-02). |
| RG-07 | O catalogo materializa a **baseline** do acervo: identificador, data, contagem e evidencia de integridade medida. A baseline e **projecao do catalogo**, nao entidade nova, e nunca gera arquivo por artefato (RG-05). |

## 11. Conformidade

| Verificacao | Quando | Executa | Falha resulta em |
|---|---|---|---|
| Contrato L1 completo | A cada portao | DEP-GOV | Artefato nao conforme; veto |
| `revisor` ≠ `autor` | A cada aprovacao | DEP-GOV | Aprovacao **nula** (LV-03) |
| `ratificacao` coerente com a classe | A cada C3/Tipo 1 | **DEP-QAR** | Artefato retido em `aprovado` (LM-02) |
| Tipo documental consta de §4 | A cada criacao | DEP-GOV | Tipo nulo (CS-01, MT-01) |
| Atributo derivavel declarado no frontmatter | Auditoria de coerencia | DEP-GOV | Campo removido; fonte unica restaurada (AC-01) |
| Cadeia origem → estado → substituicao percorrivel | Auditoria de integridade referencial | DEP-GOV | Elo quebrado; bloqueia aprovacao (LN-07) |
| Custo de contexto medido, nao estimado | A cada entrada no catalogo | DEP-KMS | Entrada devolvida (CE-04) |
| Entrada no catalogo mestre presente | A cada criacao | DEP-GOV | Artefato nao localizavel (RG-02) |
| Divisao com menos de dois sinais observados | A cada proposta de especializacao | DEP-QAR | Proposta devolvida (SE-02) |
| **Tabela reproduzida de outra fonte sem declaracao de projecao** | **Pelo autor, antes da submissao** | Autor; conferido por DEP-GOV | Tabela substituida por referencia ou declarada como projecao (PJ-01, PJ-02) |
| **Teste preventivo de projecao aplicado, com evidencia** | A cada Fitness Check de C2/C3 | DEP-QAR | Resposta F2 incompleta; verificacao devolvida (PJ-06) |
| **Conteudo de origem externa admitido fora do portao** | A cada criacao | DEP-GOV | Artefato **nulo**; incidente de conformidade (FR-03, ADR-0007) |
| **Alteracao de conteudo sem incremento de versao** | Auditoria de conformidade de artefato | DEP-GOV | Versao devida declarada no ato; a obrigacao de §2.2 passa a incidir (AC-11) |

---

## Documentos relacionados

| Referencia | Relacao |
|---|---|
| [ADR-0006](../decisions/ADR-0006-adocao-do-enterprise-artifact-framework.md) | Decisao que adota este framework |
| [ADR-0009](../decisions/ADR-0009-o-que-conta-como-emenda-de-artefato.md) | Define "emendado" para efeito de §2.2 e §2.3 — AC-08 a AC-11 |
| [ADR-0005](../decisions/ADR-0005-proibicao-de-autoverificacao.md) | Proibicao de autoverificacao, aplicada em LN-06 |
| [RFC-0004](../rfcs/RFC-0004-enterprise-artifact-framework.md) | Proposta de origem |
| [INC-2026-001](../governance/incidents/INC-2026-001-ratificacao-inferida.md) | Incidente cuja causa §5.4 corrige |
| [MEM-APR-0001](../memory/aprendizado/MEM-APR-0001-ratificacao-por-precedente.md) | Aprendizado que sustenta LM-06 |
| [Catalogo mestre](../governance/artifact-registry.md) | Classificacao do acervo |
| [FND-09](09-meta-model.md) | Entidades, relacoes, autoridade e ciclo — nao redefinidos aqui |
| [TPL-documento](templates/TPL-documento.md) | Template universal, estendido por este framework |

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-GOV | Framework inicial: contrato em 3 camadas com 5 campos novos e migracao de custo zero; Canon Semantico com 4 termos resolvidos e 3 gatilhos de ontologia; 33 tipos documentais sobre 21 entidades e 6 tipos recusados; 9 operacoes de ciclo com rollback; ratificacao como condicao de validade; 3 classes de mutabilidade; 9 verbos de linhagem mapeados; 4 perfis de contexto com custo medido; motor de especializacao com 7 sinais. **Ratificacao pendente.** |
| — | 2026-07-28 | DEP-KMS | **Transicao de estado, nao versao.** `aprovado` → `ativo` (operacao O4), pela ratificacao explicita de ADR-0006 registrada em [INC-2026-001 §11](../governance/incidents/INC-2026-001-ratificacao-inferida.md). Conteudo inalterado; `ratificacao` passa a `ratificada`. |
| 1.2.0 | 2026-07-28 | DEP-GOV | Emenda C2 por **ADR-0009**: §2.5 recebe **AC-08 a AC-11**, que definem "emendado" como a alteracao que incrementa MAIOR ou MENOR, isentam `CORRECAO` e atualizacao derivada de M3, declaram que M1 nunca e emendado e tratam alteracao sem incremento de versao como nao conformidade a FND-03 §6; §2.3 remete a elas; §11 recebe uma verificacao. Fecha o achado **C13** de REV-CONSOLIDACAO §10. |
| 1.1.0 | 2026-07-28 | DEP-GOV | Emendas C2 por **ADR-0007** e **ADR-0008**: §2.6 institui *uma fonte, multiplas projecoes* (PJ-01 a PJ-06) e o campo opcional `projecao_de`; §4 declara-se projecao de FND-03 §7; §10.3 perde a coluna Local, fechando R2 de FIT-2026-002 e a acao A7; §10.4 recebe **RG-06** (proveniencia curada) e **RG-07** (baseline como projecao); §11 recebe tres verificacoes novas. |
| 1.3.0 | 2026-07-29 | DEP-GOV | Emenda **C3** por **ADR-0017**, em **cascata** (CV-04) sobre a alteracao de **FND-09 §8.2**: a linha `Fitness Check` de **§10.3** deixa de declarar *"Ratifica: SOBERANO se C3"* e passa a **`—`**, e §10.3 recebe **uma nota** que declara a relacao fonte-projecao. **Uma celula e uma nota.** `Revisao Arquitetural` ja declarava `—` e nao muda; nenhum outro tipo documental foi tocado; nenhum titular ampliado. Fecha **RD-09** com FND-09 1.4.0. |
| 1.4.0 | 2026-07-29 | DEP-GOV | Emenda **C3** por **ADR-0019**, em **cascata** de FND-09 §8.2 (CV-04): **§10.3**, linha **`Spec`**, passa *Aprova* de `DEP-PRD (QG-1)` para **`conforme classe`** e *Ratifica* de `—` para **`SOBERANO se C3/Tipo 1`**, alinhando a linha ao padrao ja usado pela linha `ADR`; a matriz recebe **uma nota** de cascata, posicionada **apos** a nota de ADR-0017. Fecha a projecao de **RD-15**. **Nenhum dos outros 24 tipos documentais foi tocado.** A desordem preexistente deste historico — `1.1.0` apos `1.2.0` — **nao foi corrigida** (achado **RD-13**). **Aplicada sobre a 1.3.0 de ADR-0017, na ordem declarada em PS-2026-008 §5.** |
| 1.5.0 | 2026-07-30 | DEP-GOV | Emenda **C3** por **ADR-0024**: **§8.5** deixa de declarar valores medidos em **2026-07-28** como se fossem correntes. **Cinco valores corrigidos, nao tres:** `FND-01` **468 → 485**, `FND-03` **619 → 631**, o total **1.087 → 1.116**, o denominador do acervo **18.916 → 51.698** e o percentual derivado **5,7% → 2,2%**; a nota de `CE-05` passa de **1.225** para **1.263** linhas em `FND-09`. **`RD-27` item *(c)* caracterizara apenas os tres primeiros** — os outros tres sao o achado **`RD-46`**. **A correcao de causa esta na secao, nao so nos numeros:** o cabecalho da tabela e a nota de leitura passam a **vincular cada valor a baseline em que ele vale** (`BL-2026-07-29-10`), de modo que o valor envelheca como **historico datado** em vez de virar **afirmacao falsa** — `CE-04`, `LV-12`. **Nenhuma regra `AC-*`, `PJ-*`, `CE-*`, `IR-*` ou `RG-*` foi criada, removida ou alterada; `0` bytes em §1 a §8.4 e em §9 a §11; o nucleo obrigatorio continua sendo exatamente os mesmos quatro artefatos — ampliá-lo seria `C2` com Fitness Check, e isto nao o amplia.** |
