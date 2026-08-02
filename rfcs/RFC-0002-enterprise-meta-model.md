---
id: RFC-0002-enterprise-meta-model
titulo: Introduzir o Enterprise Meta Model como definicao fechada das entidades da plataforma
tipo: rfc
versao: 1.0.0
status: aprovado
camada_memoria: nao-aplicavel
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: null
decisoes_relacionadas: [ADR-0003]
substitui: []
substituido_por: null
classe_mudanca: C3
prazo_analise: 2026-07-28
---

# RFC-0002: Enterprise Meta Model

## Proposito
Propor a criacao do **Enterprise Meta Model** — documento normativo que declara o conjunto
fechado de entidades do LucaX Enterprise OS, os relacionamentos permitidos entre elas, seus
estados, sua autoridade, suas dependencias proibidas e as regras de introducao de entidades
novas.

## Escopo
Abrange a camada de **tipos** (M1) e as regras sobre tipos (M2). Nao abrange instancias:
nao cria departamento, agente, skill, workflow, produto, codigo nem infraestrutura.

## Responsaveis
| Papel | Quem |
|---|---|
| Proponente | DEP-GOV |
| Areas que devem se manifestar | DEP-EXE (merito e amplitude), DEP-QAR (sobreposicao e lacuna), DEP-KMS (impacto na memoria) |
| Aprovador | SOBERANO |
| Prazo de manifestacao | 2026-07-28 |

---

## 1. Situacao atual

A Fundacao vigente (FND-01 a FND-08, ratificada por ADR-0001 e ADR-0002) responde por que a
organizacao existe, quem responde por que, como as coisas se chamam, como mudam, como se
comunicam, como se lembram, como se decide e o que a organizacao sabe fazer.

A informacao sobre **quais coisas podem existir** esta presente, mas **dispersa e
incompleta**:

| Onde | O que ja diz | O que nao diz |
|---|---|---|
| FND-03 §2 | Prefixo, formato e largura de 17 identificadores | Se a lista e fechada; que relacoes sao permitidas entre tipos |
| FND-03 §3 | Definicao canonica de 13 componentes | Autoridade de cada um; dependencias proibidas |
| FND-04 §6 | Pre-condicoes de criacao por tipo | Como um **tipo novo** entra |
| FND-08 §5 | Sete relacoes — **apenas entre Capabilities** | Relacoes entre tipos diferentes |
| FND-01 §10 | Hierarquia normativa de 8 niveis | Que dependencia estrutural e proibida |

## 2. Problema

| # | Defeito | Consequencia |
|---|---|---|
| P1 | **Universo aberto.** Nenhum documento declara que a lista de tipos e fechada. | Qualquer Framework futuro pode introduzir uma entidade estrutural por conveniencia. A plataforma passa a ter conceitos concorrentes para a mesma pergunta, violando LX-07 sem que nenhuma norma seja formalmente descumprida. |
| P2 | **Relacoes nao declaradas entre tipos diferentes.** FND-08 §5 cobre Capability↔Capability; nada cobre Agente↔Skill, Produto↔Spec, Memoria↔Decisao. | Relacoes sao improvisadas em cada Carta. Nao ha como verificar elo quebrado, ciclo ou dependencia invertida fora do catalogo de Capabilities. |
| P3 | **Autoridade dispersa.** Quem cria, aprova e aposenta cada tipo esta espalhado por FND-01 §7.3, FND-04 §2 e §6, e FND-08 §6.3. | Responder "quem pode aposentar um Agente?" exige varrer tres documentos. Autoridade dificil de consultar e autoridade que se presume — exatamente o que PI-01 proibe. |
| P4 | **Sem regra de compatibilidade.** Nada define como um tipo novo entra sem invalidar instancias existentes. | O primeiro tipo novo criado depois de existirem agentes e produtos custara revisitar tudo que ja existe. |
| P5 | **Lacunas ja materializadas.** `MSG` tem esquema de ID em FND-05 §3 e **nao consta** da tabela de identificadores de FND-03 §2. A obrigacao de Carta (PI-12) alcanca oito tipos; a de vinculo a Capability (FND-08 §8), apenas seis. | Sao inconsistencias reais, hoje, com custo de correcao praticamente nulo — e estritamente crescente a partir do primeiro componente criado. |

**Evidencia:** a divergencia PI-12 × FND-08 §8 e verificavel por leitura direta dos dois
textos; a ausencia de `MSG` em FND-03 §2 tambem. Nenhuma das duas foi detectada pelas
auditorias existentes, porque nenhuma auditoria verifica **coerencia entre tipos** — so
conformidade de instancias.

## 3. Pergunta de decisao

O LucaX deve adotar um Meta Model normativo, com universo fechado de entidades,
relacionamentos permitidos, modelo de autoridade e regras de evolucao, **antes** de criar
departamentos, agentes e produtos?

## 4. Criterios de avaliacao

> Declarados antes do exame das opcoes (CD-01).

| # | Criterio | Peso | Como se mede |
|---|---|---|---|
| C1 | Fecha o universo de entidades de forma verificavel | Alto | Existe lista unica e exaustiva; entidade fora dela e nula |
| C2 | Torna as relacoes entre tipos verificaveis por varredura | Alto | Par origem-destino permitido e declarado; par ausente e proibido |
| C3 | Consolida a autoridade em consulta unica, sem redefini-la | Alto | Matriz derivada das normas de origem, com regra de precedencia declarada |
| C4 | **Nao duplica definicao existente na Fundacao** | **Bloqueante** | Nenhuma secao reescreve FND-01 a FND-08; conceitos existentes sao referenciados por ID |
| C5 | Suporta crescimento sem quebrar compatibilidade | Alto | Rito de entidade nova + regras de compatibilidade retroativa |
| C6 | Custo de manutencao proporcional | Medio | Um documento normativo; nenhum artefato por instancia |

## 5. Opcoes

### Opcao A — Meta Model normativo com universo fechado

| Campo | Conteudo |
|---|---|
| Descricao | FND-09 declara estratos, arquetipos, entidades oficiais com atributos minimos, relacoes permitidas por par, perfis de ciclo de vida, matriz de autoridade, dependencias proibidas e rito de entidade nova (C3) |
| A favor | Unica que satisfaz C1, C2, C3 e C5 juntos. Torna verificavel por varredura o que hoje depende de leitura atenta. Fecha P1 a P5 |
| Contra | Acrescenta um documento fundacional e uma emenda C3 a hierarquia normativa. Universo fechado torna entidade nova cara — deliberadamente |
| Custo | 1 documento normativo, emendas em cascata, nenhum artefato por instancia |
| Risco | Rigidez excessiva; Meta Model virar copia da Taxonomia |

### Opcao B — Ampliar FND-03 (Taxonomia) com as regras faltantes

| Campo | Conteudo |
|---|---|
| Descricao | Acrescentar a FND-03 secoes de relacoes, autoridade e evolucao de tipos |
| A favor | Nenhum documento novo; custo menor; sem emenda a hierarquia |
| Contra | **Confunde duas perguntas distintas.** FND-03 responde "como se chama e onde vive"; as regras propostas respondem "o que pode existir e como se liga". Fundi-las cria documento que responde a duas perguntas — exatamente o gatilho de especializacao "escopo heterogeneo" (FND-02 §9.2), que obrigaria a divisao logo depois. FND-03 ja tem 10 secoes e e o documento mais consultado do sistema; ampliar aumenta o custo de contexto de todos (PI-14) |
| Custo | Baixo agora; alto na primeira divisao |
| Risco | Alto — cria o defeito que PI-14 manda evitar |

### Opcao C — Meta Model descritivo, sem universo fechado

| Campo | Conteudo |
|---|---|
| Descricao | Documento que descreve as entidades existentes e suas relacoes, sem declarar a lista fechada nem exigir C3 para tipo novo |
| A favor | Resolve C2 e C3; custo menor; nao engessa Frameworks futuros |
| Contra | **Nao resolve C1**, que e o problema declarado na missao: "nenhum Framework podera introduzir uma entidade estrutural sem obedecer ao Meta Model". Sem universo fechado, o documento descreve o passado e nao restringe o futuro — e desatualiza no primeiro Framework que o ignorar. Repete exatamente a fragilidade que ADR-0002 §6 identificou na Alternativa C daquela decisao: documento que nada obriga a manter atualizado passa a enganar quem o consulta |
| Custo | Medio |
| Risco | Medio-alto — vira documento decorativo |

### Opcao Z — Nao fazer nada

| Campo | Conteudo |
|---|---|
| O que acontece | A estrutura operacional e construida sem definicao de universo. P1 a P5 se materializam |
| Custo real da inacao | As duas inconsistencias ja detectadas (P5) custam **zero** para corrigir hoje, porque nao existe nenhuma instancia de Projeto, Ferramenta ou Mensagem. Cada componente criado a partir daqui aumenta esse custo. E a mesma assimetria aceita como argumento em ADR-0001 §6 e ADR-0002 §4 |
| Por que nao venceu | O custo de adiar e estritamente crescente, e a fase seguinte — Cartas de departamento — ja comeca a acumula-lo |

## 6. Recomendacao do proponente

**Opcao A.**

A Opcao B falha no criterio que a propria arquitetura considera decisivo: fundir duas
perguntas em um documento e o gatilho de especializacao que FND-02 §9.2 manda evitar, e o
faria no documento mais consultado do sistema.

A Opcao C falha em C1, que e o proposito declarado da missao. Um Meta Model que descreve mas
nao restringe nao impede que o proximo Framework introduza entidade concorrente — e o
problema P1 permanece integralmente.

Sobre **C4 (bloqueante)**: o Meta Model nao redefine nada. Estados vem de FND-03 §5 por
referencia; relacoes entre Capabilities vem de FND-08 §5 por referencia; classes de mudanca
vem de FND-04 §2 por referencia; a matriz de autoridade e **derivada** de FND-01 §7.3,
FND-04 e FND-08 §6.3, com regra explicita de que, em conflito, prevalece o documento de
origem e o conflito e registrado como erro do Meta Model. Onde ha risco de duplicacao, ha
link, nunca copia (MM-01, FND-03 §7.1).

### 6.1 Sobre as treze entidades recusadas

A missao ofereceu 25 candidatas como exemplo. A analise aceita 13 delas e recusa 12, e
recusa ainda "Mission" como entidade. **Recusa nao e negacao do problema:** cada uma foi
alocada a um instrumento existente, com gatilho declarado de reabertura.

O criterio foi MT-10 — abstracao antes de multiplicacao — e o Teste de Entidade (TE-1 a
TE-7). Aceitar todas as 25 teria produzido oito entidades sem pergunta propria (`Artifact`,
`Domain`, `Metric`, `Event`, `Resource`, `Command`, `Prompt`, `Model`), violando MT-02 e o
antipadrao de antecipacao de FND-08 §7.1 — que recusa criacao por simetria ou por
espelhamento.

**Ressalva registrada:** recusar `Policy` e `Standard` deixa a plataforma sem instrumento
para regra vigente que nao seja constitucional, nem decisao, nem forma. Hoje isso nao e
lacuna — nao existe nenhuma regra nessas condicoes. A partir do primeiro padrao tecnico
adotado, pode passar a ser. O gatilho esta declarado em FND-09 §5.8 (X-05, X-06) e o
arquetipo de entrada — `Norma Derivada` — esta nomeado, para que a entrada futura seja
acrescimo e nao redesenho.

## 7. Impacto previsto

| Dimensao | Impacto |
|---|---|
| Documentos afetados | FND-01 (§10 hierarquia, §11 glossario), FND-02 (§9 evolucao, §9.5 invariantes), FND-03 (§2 identificadores, §3 componentes, §4 frontmatter, §7 diretorios, §8 vocabulario, §10 conformidade), FND-04 (§6 pre-condicoes, §8 auditoria), FND-06 (§3.1 e §8.1), FND-08 (§8 vinculacao) |
| Componentes afetados | Todos os futuros: passam a existir apenas se o tipo constar de FND-09 §5 |
| Correcoes de coerencia | `MSG` registrada em FND-03; vinculo obrigatorio a Capability estendido a Projeto e Ferramenta, unificando PI-12 e FND-08 §8 |
| Camadas de memoria | EST — o Meta Model e conhecimento estrategico permanente |
| Artefatos criados | FND-09; nenhum artefato por instancia |
| Ganho PI-14 pretendido | **Organizacao:** o universo deixa de ser implicito. **Reuso:** relacoes, estados e autoridade declarados uma vez servem a qualquer Framework futuro. **Reducao de contexto:** responder "isso pode existir? como se liga?" passa a exigir um documento em vez de cinco |
| Sinal que comprovara o ganho | Primeiro Framework futuro construido sem redefinir conceito fundamental; primeira entidade candidata recusada pelo Teste de Entidade antes de virar artefato |

## 8. Riscos

| # | Risco | Probabilidade | Impacto | Mitigacao |
|---|---|---|---|---|
| R1 | Meta Model vira copia da Taxonomia | Media | Alto | C4 bloqueante; FND-09 §1.3 declara explicitamente o que nao faz; verificado na revisao arquitetural |
| R2 | Universo fechado engessa Frameworks futuros | **Alta** | Medio | Gradacao de instrumento (§11.2): atributo novo e C1, classe nova e C2; so entidade, arquetipo e relacao sao C3 |
| R3 | Matriz de autoridade diverge das normas de origem ao longo do tempo | Media | **Alto** | Regra de precedencia declarada (§8.2): em conflito, vence a origem, e o conflito e erro do Meta Model; auditoria de coerencia normativa a cada C2/C3 |
| R4 | Treze recusas registradas viram lacunas reais | Media | Medio | Cada recusa declara onde a responsabilidade vive hoje e o gatilho de reabertura (§5.8) |
| R5 | Estender vinculo obrigatorio a Projeto e Ferramenta gera atrito sem ganho | Baixa | Baixo | Custo zero hoje (nenhuma instancia); reversivel por ADR sem migracao |
| R6 | **Esta decisao estar errada** — o Meta Model ser peso sem retorno | Media | Alto | EV-08 obriga consolidacao quando o ganho nao se confirma; gatilhos em ADR-0003 §12 |

## 9. Perguntas em aberto

| Pergunta | Dono da resposta | Bloqueia? |
|---|---|---|
| `Policy` e `Standard` devem entrar como entidade `Norma Derivada`? | DEP-GOV, no primeiro padrao tecnico adotado | **Nao** — gatilho declarado em §5.8 |
| `Team` sera necessario quando houver agentes? | DEP-EXE, apos os primeiros cinco agentes | **Nao** — Projeto cobre o caso hoje |
| A obrigacao de Carta (PI-12) e a de vinculo (FND-08 §8) devem ser unificadas? | Esta RFC recomenda **sim** | Nao — decidido no ADR |
| O Meta Model deve ter precedencia sobre outros FND? | DEP-GOV | Nao — resolvido: precedencia parcial e declarada em §1.4 |

## 10. Manifestacoes

| Area | Posicao | Fundamento | Data |
|---|---|---|---|
| DEP-GOV | Propoe | A dispersao das regras sobre tipos ja produziu duas inconsistencias verificaveis (P5). Exige que a mudanca seja tratada como **C3**, por acrescentar documento a Fundacao e alterar a hierarquia normativa (FND-01 §10) | 2026-07-28 |
| DEP-EXE | Apoia | O universo fechado protege a fase seguinte: Cartas de departamento nascerao dentro de um modelo declarado, e nao o definindo por precedente | 2026-07-28 |
| DEP-QAR | Apoia com ressalva | Aceita a analise, mas registra que **os ganhos sao previstos, nao observados**: nao ha Framework futuro construido sobre o Meta Model que comprove C5. Exige gatilhos de confirmacao no ADR e Fitness Check no encerramento | 2026-07-28 |
| DEP-KMS | Apoia | O Meta Model pertence a camada EST; consulta obrigatoria antes de criar componente e compativel com FND-06 §8.1 | 2026-07-28 |

## 11. Resultado

| Campo | Conteudo |
|---|---|
| Decisao | **aceita** |
| ADR gerado | [ADR-0003](../decisions/ADR-0003-adocao-do-enterprise-meta-model.md) |
| Ressalvas incorporadas | Classificada como **C3, Tipo 1** (DEP-GOV); gatilhos de confirmacao e Fitness Check obrigatorio (DEP-QAR) |
| Data | 2026-07-28 |
| Responsavel | DEP-GOV |
