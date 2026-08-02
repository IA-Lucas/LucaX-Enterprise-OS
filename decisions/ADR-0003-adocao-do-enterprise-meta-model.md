---
id: ADR-0003-adocao-do-enterprise-meta-model
titulo: Adotar o Enterprise Meta Model como definicao fechada das entidades, relacoes e autoridade da plataforma
tipo: adr
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0001, ADR-0002, ADR-0004]
substitui: []
substituido_por: null
classe_mudanca: C3
tipo_decisao: 1
supera: []
superado_por: null
---

# ADR-0003: Adotar o Enterprise Meta Model

## Proposito

Registrar a decisao de criar o Enterprise Meta Model do LucaX Enterprise OS — o documento
normativo FND-09, o universo fechado de 21 entidades, os 4 arquetipos, as 10 relacoes
permitidas, os 4 perfis de ciclo de vida, a matriz de autoridade, as 12 dependencias
proibidas e o rito de introducao de entidade nova — e as emendas em cascata que ela exige.

## Escopo

Aplica-se a camada de **tipos** da plataforma. Nao cria departamento, agente, subagente,
skill, workflow, produto, projeto, ferramenta, codigo nem infraestrutura.

## Responsaveis

| Papel | Quem |
|---|---|
| Proponente | DEP-GOV |
| Revisor independente | DEP-QAR |
| Consulta de merito | DEP-EXE |
| Aprovador | SOBERANO |
| Ratificador | **SOBERANO** (C3 e Tipo 1) |
| Executor | DEP-GOV |

---

## 1. Contexto

ADR-0001 estabeleceu a Fundacao (FND-01 a FND-07). ADR-0002 acrescentou a camada de
Capabilities (FND-08) e a regra de vinculacao obrigatoria.

O sistema resultante sabe **por que existe**, **quem responde por que**, **como as coisas se
chamam**, **como mudam**, **como se comunicam**, **como lembra**, **como decide** e **o que
sabe fazer**. Nao sabe declarar **o que pode existir**.

A informacao esta dispersa: FND-03 §2 lista 17 identificadores sem declarar que a lista e
fechada; FND-03 §3 define 13 componentes sem declarar suas relacoes; FND-08 §5 define sete
relacoes que valem apenas entre Capabilities; a autoridade sobre cada tipo esta espalhada
por FND-01 §7.3, FND-04 §2 e §6 e FND-08 §6.3.

O momento importa pelo mesmo motivo de ADR-0002: a fase seguinte cria Cartas de
departamento e, depois, agentes. Cada componente criado sem modelo declarado transforma
precedente em norma de fato, e o custo de extrair o modelo depois cresce com cada um.

Alem disso, a analise de RFC-0002 detectou **duas inconsistencias reais** hoje existentes:

1. `MSG` possui esquema de identificador operante em FND-05 §3 e nao consta da tabela de
   identificadores de FND-03 §2.
2. PI-12 exige Carta para oito tipos de componente; FND-08 §8 exige vinculo a Capability
   para apenas seis — deixando Projeto e Ferramenta fora da espinha dorsal de
   rastreabilidade descrita em FND-08 §8.4.

Nenhuma auditoria vigente detectaria essas duas, porque todas verificam conformidade de
**instancias**, e nenhuma verifica coerencia entre **tipos**.

## 2. Problema / Pergunta de decisao

O LucaX deve adotar um Meta Model normativo, com universo fechado de entidades,
relacionamentos permitidos, modelo de autoridade e regras de evolucao, antes de construir a
estrutura operacional?

## 3. Criterios de decisao

> Definidos antes do exame das alternativas (CD-01). Herdados de
> [RFC-0002 §4](../rfcs/RFC-0002-enterprise-meta-model.md).

| # | Criterio | Peso | Como se mede |
|---|---|---|---|
| C1 | Fecha o universo de entidades de forma verificavel | Alto | Lista unica e exaustiva; entidade fora dela e nula |
| C2 | Torna as relacoes entre tipos verificaveis por varredura | Alto | Par origem-destino declarado; par ausente e proibido |
| C3 | Consolida a autoridade em consulta unica, sem redefini-la | Alto | Matriz derivada, com regra de precedencia declarada |
| C4 | Nao duplica definicao existente na Fundacao | **Bloqueante** | Nenhuma secao reescreve FND-01 a FND-08 |
| C5 | Suporta crescimento sem quebrar compatibilidade | Alto | Rito de entidade nova + regras de compatibilidade |
| C6 | Custo de manutencao proporcional | Medio | Um documento; nenhum artefato por instancia |

## 4. Alternativas consideradas

### Alternativa A — Meta Model normativo com universo fechado

| Campo | Conteudo |
|---|---|
| Descricao | FND-09 com estratos, arquetipos, entidades, relacoes por par, perfis de ciclo de vida, autoridade, dependencias proibidas e rito C3 para tipo novo |
| A favor | Unica que satisfaz C1, C2, C3 e C5 juntos; torna verificavel por varredura o que hoje depende de leitura atenta |
| Contra | Documento fundacional a mais; emenda C3; entidade nova passa a ser cara |
| Custo | 1 documento normativo + 6 emendas em cascata; nenhum artefato por instancia |
| Risco | Rigidez (R2); virar copia da Taxonomia (R1) |
| Avaliacao | C1 alto · C2 alto · C3 alto · C4 satisfeito · C5 alto · C6 medio |

### Alternativa B — Ampliar FND-03 com as regras faltantes

| Campo | Conteudo |
|---|---|
| Descricao | Acrescentar secoes de relacao, autoridade e evolucao de tipos a Taxonomia |
| A favor | Nenhum documento novo; sem emenda a hierarquia; custo imediato menor |
| Contra | Funde duas perguntas distintas em um documento — o gatilho "escopo heterogeneo" de FND-02 §9.2, que obrigaria a divisao logo em seguida. Fa-lo-ia no documento mais consultado do sistema, aumentando o custo de contexto de todos os papeis (PI-14) |
| Custo | Baixo agora; alto na divisao subsequente |
| Risco | Alto — cria deliberadamente o defeito que PI-14 manda evitar |
| Avaliacao | C1 medio · C2 medio · C3 medio · C4 satisfeito · C5 baixo · C6 alto |

### Alternativa C — Meta Model descritivo, sem universo fechado

| Campo | Conteudo |
|---|---|
| Descricao | Documento que descreve entidades e relacoes existentes, sem lista fechada nem exigencia de C3 para tipo novo |
| A favor | Resolve C2 e C3; menor custo; nao engessa Frameworks futuros |
| Contra | **Nao resolve C1.** Sem universo fechado, o documento descreve o passado e nao restringe o futuro; desatualiza no primeiro Framework que o ignorar. E a mesma fragilidade identificada na Alternativa C de ADR-0002: documento que nada obriga a manter atualizado passa a enganar quem o consulta |
| Custo | Medio |
| Risco | Medio-alto — documento decorativo |
| Avaliacao | C1 **baixo** · C2 alto · C3 alto · C4 satisfeito · C5 baixo · C6 medio |

### Alternativa Z — Nao fazer nada

| Campo | Conteudo |
|---|---|
| O que acontece | A estrutura operacional e construida sem universo declarado; as duas inconsistencias detectadas permanecem e se propagam |
| Custo real da inacao | Hoje as correcoes custam **zero**: nao existe nenhuma instancia de Projeto, Ferramenta ou Mensagem para migrar. A partir do primeiro componente criado, cada uma passa a exigir revisitacao |
| Por que nao venceu | Assimetria de custo estritamente crescente, ja aceita como argumento em ADR-0001 §6 e ADR-0002 §4 |

## 5. Decisao

**Decidimos adotar o Enterprise Meta Model do LucaX Enterprise OS**, composto de:

1. **FND-09 — Enterprise Meta Model**, incorporado a Fundacao como documento de nivel 2 da
   hierarquia normativa, com precedencia parcial declarada (FND-09 §1.4): em conflito sobre
   **existencia ou relacao de tipos**, prevalece o Meta Model; sobre **conteudo do tipo**,
   prevalece o documento especializado.

2. O **universo fechado de 21 entidades** em 7 estratos (FND-09 §5), com identidade,
   proposito, responsabilidade, autoridade, ciclo de vida, relacionamentos validos e
   atributos minimos declarados para cada uma.

3. Os **4 arquetipos** — ATOR, ARTEFATO, COMPONENTE, INSTRUMENTO (FND-09 §4) — como classes
   abstratas nao instanciaveis, para que regras transversais sejam escritas uma vez.

4. As **13 recusas registradas** (FND-09 §5.8): `Artifact`, `Domain`, `Team`, `Command`,
   `Policy`, `Standard`, `Prompt`, `Model`, `Service`, `Resource`, `Metric`, `Event` e
   `Mission` **nao** sao entidades. Cada recusa declara onde a responsabilidade vive hoje e
   qual sinal reabre a discussao.

5. As **10 relacoes oficiais** com pares permitidos, cardinalidade e restricoes (FND-09 §6);
   as relacoes entre Capabilities permanecem definidas em FND-08 §5 e sao incorporadas por
   referencia, nunca reescritas.

6. Os **4 perfis de ciclo de vida** (P0 permanente, P1 normativo, P2 instrumento, P3
   efemero) e os **eixos ortogonais de estado** (FND-09 §7), que dao nome a dimensoes ate
   agora implicitas: `vigencia` de excecao, `situacao` de incidente, `veredito` de
   verificacao de aptidao.

7. A **matriz de autoridade** por entidade (FND-09 §8.2), **derivada** de FND-01 §7.3,
   FND-04 e FND-08 §6.3, com a regra explicita de que, em conflito, prevalece o documento de
   origem e o conflito e registrado como erro do Meta Model.

8. As **12 dependencias proibidas** e a regra-mae de direcao (FND-09 §9): dependencia dura
   aponta para o mesmo estrato ou para estrato de numero menor, **nunca para cima**.

9. O **rito de entidade nova** (FND-09 §11.1), com Teste de Entidade TE-1 a TE-7 e classe
   **C3** obrigatoria, e a **gradacao de instrumento** (§11.2), que mantem atributo novo em
   C1 e classe nova em C2.

10. As **12 invariantes do Meta Model** (FND-09 §11.5), que nenhuma evolucao pode quebrar
    sem revoga-las explicitamente.

**Decidimos ainda, como correcoes de coerencia:**

11. **Registrar `MSG` como entidade oficial** e acrescenta-la a tabela de identificadores de
    FND-03 §2, com definicao canonica em FND-03 §3.13. A entidade ja operava em FND-05 §3
    sem constar da taxonomia.

12. **Estender a vinculacao obrigatoria a Capability a Projeto e Ferramenta**, unificando o
    alcance de PI-12 (Carta obrigatoria para oito tipos) e de FND-08 §8 (vinculo obrigatorio
    para seis). Passam a ser oito em ambas, e o arquetipo COMPONENTE torna-se uniforme.

13. **Registrar `modelo` como classe de Ferramenta** em FND-03 §3.12, absorvendo a candidata
    `Model` sem criar entidade.

## 6. Justificativa

A Alternativa A vence pelos quatro criterios de maior peso. O ponto decisivo esta em **C1**,
onde A e C divergem: um Meta Model que descreve mas nao restringe **nao impede** que o
proximo Framework introduza entidade concorrente. O proposito declarado — "nenhum Framework
podera introduzir uma entidade estrutural sem obedecer ao Meta Model" — exige universo
fechado. Sem ele, a decisao seria apenas documental.

A Alternativa B foi descartada por razao interna a propria arquitetura: fundir "como se
chama" com "o que pode existir" e o gatilho de escopo heterogeneo que FND-02 §9.2 obriga a
evitar, e o faria no documento de maior consumo do sistema. Aceitar B seria violar PI-14 por
economia de curto prazo.

Sobre **C4 (bloqueante)**, o teste foi aplicado item a item: estados vem de FND-03 §5 por
referencia; classes de mudanca, de FND-04 §2; relacoes entre Capabilities, de FND-08 §5;
niveis de autonomia, de FND-01 §7.2. A matriz de autoridade e derivacao com precedencia
declarada, nao redefinicao. Onde havia risco de duplicacao, ha link (MM-01, FND-03 §7.1).

**Sobre as recusas.** Aceitar as 25 candidatas oferecidas produziria oito entidades sem
pergunta propria — `Artifact`, `Domain`, `Metric`, `Event`, `Resource`, `Command`, `Prompt`
e `Model` — violando MT-02 e o antipadrao de antecipacao de FND-08 §7.1, que recusa criacao
por simetria ou espelhamento. `Metric` como entidade produziria 111 artefatos para os
indicadores ja definidos nas 23 Capabilities, fragmentando cada indicador do que ele mede.
As recusas nao negam os problemas: cada uma nomeia o instrumento que ja os resolve e o
gatilho que reabre a discussao.

**Tradeoff aceito (universo fechado).** Introduzir entidade nova passa a exigir RFC, ADR e
ratificacao do Soberano — deliberadamente caro. Aceita-se perder agilidade na criacao de
tipos em troca de que o vocabulario estrutural da plataforma nao possa ser ampliado por
conveniencia de um Framework isolado. A gradacao de FND-09 §11.2 preserva a agilidade onde
ela importa: atributo novo continua sendo C1, classe nova continua sendo C2.

**Tradeoff aceito (item 12).** Estender o vinculo obrigatorio a Projeto e Ferramenta
acrescenta um campo obrigatorio a dois tipos. O custo hoje e **zero** — nao existe nenhuma
instancia de nenhum dos dois — e cresce a partir do primeiro. Em troca, a espinha dorsal de
rastreabilidade de FND-08 §8.4 passa a valer sem excecao: de qualquer componente se sobe ate
a competencia, e de qualquer competencia se desce ate tudo que a exerce.

**Ressalva de DEP-GOV incorporada:** a mudanca e **C3**, e nao C2, por acrescentar documento
a Fundacao e alterar a hierarquia normativa (FND-01 §10). Tratar como C2 seria irregular.

**Ressalva de DEP-QAR incorporada:** os ganhos sao **previstos, nao observados** (§8), e o
encerramento desta decisao exige Fitness Check (§12).

## 7. Impacto

| Dimensao | Impacto |
|---|---|
| Departamentos afetados | Os nove — todo componente futuro nasce dentro do universo declarado |
| Componentes afetados | Todos os futuros. **Nenhum existente**: nao ha departamento, agente, skill, workflow, produto, projeto ou ferramenta criado nesta data |
| Camadas de memoria a atualizar | **EST** — o Meta Model e conhecimento estrategico permanente |
| Decisoes superadas | Nenhuma. ADR-0001 e ADR-0002 sao **complementados**, nao superados |
| Documentos a atualizar | FND-01 v1.2.0 (§10 hierarquia, §11 glossario) · FND-02 v1.2.0 (§9.1 nota, §9.5 invariante IV-09) · FND-03 v1.2.0 (§2 identificadores, §2.3 sequencias, §3.12 classe `modelo`, §3.13 Mensagem, §4.1 frontmatter, §7 diretorios, §8 vocabulario, §10 conformidade) · FND-04 v1.2.0 (§6 pre-condicoes, §8 auditoria) · FND-06 v1.2.0 (§3.1 conteudo EST, §8.1 consulta obrigatoria) · FND-08 v1.1.0 (§8 vinculacao estendida) |
| Artefatos criados | FND-09; revisao arquitetural do Meta Model |
| Custo e dependencia criados | Manutencao de um documento normativo; um campo obrigatorio a mais em dois tipos ainda sem instancia. **Nenhuma dependencia externa** |
| Ganho PI-14 | **Organizacao:** o universo deixa de ser implicito e ganha fronteira verificavel. **Reuso:** relacoes, estados e autoridade declarados uma vez servem a qualquer Framework futuro sem redefinicao. **Reducao de contexto:** responder "isso pode existir? como se liga? quem aprova?" passa a exigir um documento em vez de cinco |

## 8. Evidencias

| # | Evidencia | Origem | Confianca | O que discrimina |
|---|---|---|---|---|
| E1 | Nenhum documento da Fundacao declara que a lista de tipos e fechada | Leitura de FND-01 a FND-08, 2026-07-28 | Alta | Elimina Z; confirma que o Meta Model nao duplica |
| E2 | FND-08 §5 define relacoes **apenas** entre Capabilities; nao ha norma sobre relacoes entre tipos diferentes | FND-08 §5.1 | Alta | Sustenta o problema P2 |
| E3 | `MSG` tem esquema de ID operante em FND-05 §3 e nao consta de FND-03 §2 | Confronto direto dos dois textos | **Alta — verificavel** | Prova que a dispersao ja produziu lacuna real |
| E4 | PI-12 alcanca 8 tipos; FND-08 §8 alcanca 6 | Confronto de FND-01 §4 com FND-08 §8 | **Alta — verificavel** | Prova a segunda inconsistencia; sustenta o item 12 da decisao |
| E5 | A assimetria de custo por adiamento foi aceita como argumento em ADR-0001 §6 e ADR-0002 §4 | ADRs anteriores | Alta | Sustenta decidir agora |
| E6 | Determinacao do Soberano de que o Meta Model passa a ser referencia oficial e de que nenhum Framework introduza entidade sem obedece-lo | Instrucao direta, 2026-07-28 | Alta | Elimina a Alternativa C |

**Evidencia ausente, declarada (VD-05):** nao existe, nesta data, **nenhum Framework
construido sobre o Meta Model**, nem entidade candidata recusada por ele em uso real. Os
ganhos declarados em §7 sao **previstos, nao observados** — mesma fragilidade de ADR-0001 e
ADR-0002, e a razao pela qual §12 fixa gatilhos de confirmacao. As duas evidencias E3 e E4
sao verificaveis hoje e sustentam o **problema**, nao a eficacia da solucao.

## 9. Riscos e mitigacao

| # | Risco | Probabilidade | Impacto | Mitigacao |
|---|---|---|---|---|
| R1 | Meta Model vira copia da Taxonomia | Media | Alto | C4 bloqueante; FND-09 §1.3 delimita explicitamente o que ele nao faz; verificado na revisao arquitetural |
| R2 | Universo fechado engessa Frameworks futuros | **Alta** | Medio | Gradacao de instrumento (FND-09 §11.2): so entidade, arquetipo e relacao sao C3; atributo e classe permanecem C1/C2 |
| R3 | Matriz de autoridade diverge das normas de origem | Media | **Alto** | Regra de precedencia declarada (§8.2): em conflito vence a origem; auditoria de coerencia normativa a cada C2/C3 |
| R4 | As 13 recusas viram lacunas reais | Media | Medio | Cada recusa declara instrumento atual e gatilho de reabertura; `Norma Derivada` ja nomeada como porta de entrada |
| R5 | Estender vinculo a Projeto e Ferramenta gera atrito sem ganho | Baixa | Baixo | Custo zero hoje; reversivel por ADR sem migracao |
| R6 | Perfis de ciclo de vida nao cobrirem tipo futuro | Media | Medio | Perfil novo e mudanca C2 (§11.3); eixos ortogonais absorvem estados proprios sem criar estado novo |
| R7 | **Esta decisao estar errada** — o Meta Model ser peso sem retorno | Media | Alto | EV-08 obriga proposta de consolidacao quando o ganho nao se confirma; gatilhos de §12; reversao detalhada em §10 |

## 10. Plano de reversao

| Campo | Conteudo |
|---|---|
| Como desfazer | ADR de revogacao superando este; FND-09 passa a `revogado`; emendas em cascata revertidas por nova versao MAIOR de cada documento afetado |
| Custo da reversao | **Baixo nesta data** — nenhum componente foi criado sob o Meta Model, logo nenhum vinculo, relacao ou estado precisa ser migrado |
| Janela em que ainda e possivel | Encarece a cada componente criado sob o modelo. Enquanto nao houver Cartas de departamento, e barata |
| Reversao parcial | **Preferivel e possivel:** manter FND-09 como referencia descritiva e remover apenas o universo fechado (MT-01) e a exigencia de C3 para entidade nova — equivale a recuar da Alternativa A para a C. Igualmente possivel reverter apenas o item 12 sem tocar no restante |
| Quem executa | DEP-GOV, sob ratificacao do Soberano |
| Backup necessario (PI-07) | Copia datada de `foundation/`, `capabilities/`, `decisions/` e `rfcs/` antes de qualquer revogacao |

## 11. Classificacao

| Campo | Valor |
|---|---|
| Classe de mudanca | **C3** — acrescenta documento a Fundacao e altera a hierarquia normativa |
| Tipo de reversibilidade | **Tipo 1** — cria regra vinculante para todo tipo e componente futuro |
| Decisor | SOBERANO |
| Ratificador | SOBERANO |
| Data da decisao | 2026-07-28 |
| Data de vigencia | 2026-07-28 |

## 12. Revisao

| Campo | Conteudo |
|---|---|
| Gatilho temporal | 2027-01-28 — revisao semestral da Fundacao (FND-04 §8) |
| Gatilho por evento | Primeiro Framework construido sobre o Meta Model: verificar se **nenhum conceito fundamental precisou ser redefinido** (confirma C5) |
| Gatilho por evento | Primeira entidade candidata recusada pelo Teste de Entidade antes de virar artefato (confirma C1) |
| Gatilho por evento | Primeira relacao invalida detectada por varredura, e nao por leitura (confirma C2) |
| Gatilho por confirmacao de ganho PI-14 | Na revisao estrutural, medir se o Meta Model reduziu o numero de documentos consultados para criar um componente |
| Gatilho de consolidacao (EV-08) | Entidade sem nenhuma instancia ao fim de um horizonte inteiro obriga proposta de remocao ou registro fundamentado de manutencao |
| Sinal de que esta decisao deu errado | Cartas nascem sem consultar FND-09; relacoes sao improvisadas apesar de §6.2; a matriz de autoridade diverge das origens sem ser corrigida; o universo fechado passa a ser contornado por excecao formal recorrente |
| Responsavel pela revisao | DEP-GOV com DEP-QAR; DEP-EXE arbitra merito |

## 13. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Origem | [RFC-0002](../rfcs/RFC-0002-enterprise-meta-model.md), aceita em 2026-07-28 |
| Decisoes superadas | Nenhuma |
| Decisoes relacionadas | [ADR-0001](ADR-0001-adocao-da-fundacao-organizacional.md) e [ADR-0002](ADR-0002-adocao-da-camada-de-capabilities.md) — complementadas; [ADR-0004](ADR-0004-adocao-do-architecture-fitness-check.md) — cria a entidade `FIT` registrada em FND-09 §5.2 |
| Artefatos criados | FND-09; revisao arquitetural do Meta Model |
| Emendas em cascata | FND-01 v1.2.0 · FND-02 v1.2.0 · FND-03 v1.2.0 · FND-04 v1.2.0 · FND-06 v1.2.0 · FND-08 v1.1.0 |
| Verificacao de aptidao | [FIT-2026-001](../governance/fitness/FIT-2026-001-meta-model.md) |
| Registros de memoria | Camada EST — o Meta Model integralmente |

---

## Checklist de validade (FND-07 §4.1)
- [x] VD-01 — 3 alternativas reais + "nao fazer nada"
- [x] VD-02 — criterios declarados antes da escolha (herdados da RFC)
- [x] VD-03 — nenhuma alternativa de palha (B e C sao praticas correntes e defensaveis)
- [x] VD-04 — tradeoffs aceitos explicitos (§6: universo fechado e item 12)
- [x] VD-05 — ausencia de evidencia empirica declarada (§8)
- [x] VD-06 — plano de reversao presente, com reversao parcial (Tipo 1)
- [x] VD-07 — impacto em cascata mapeado e executado (§7)
- [x] VD-08 — data e responsavel presentes
- [x] VD-09 — gatilhos de revisao definidos (§12)

---

## Ratificacao do Soberano

Esta decisao e C3 e Tipo 1: exige ato explicito do Soberano (PI-01, PI-06).

| Campo | Conteudo |
|---|---|
| Ratificado por | SOBERANO (Lucas) |
| Data | 2026-07-28 |
| Forma | Determinacao direta e escrita, na abertura desta fase |
| Texto invocado | *"Nenhum novo Framework podera introduzir uma entidade estrutural sem obedecer ao Meta Model. Este documento passa a ser a referencia oficial para toda a arquitetura organizacional."* |

### Observacao de conformidade (DEP-GOV)

A determinacao invocada e ato soberano real e datado, e ela propria estabelece o universo
fechado — nucleo desta decisao. Mas antecede o texto final aqui ratificado.

Vale a mesma ressalva de ADR-0001 e ADR-0002: discordando o Soberano de qualquer definicao
adotada — inclusive de qualquer uma das treze recusas de FND-09 §5.8 —, esta ADR deve ser
**superada** pelo rito de FND-07 §7, nunca editada (LV-04). Ate la, o Meta Model vigora
integralmente.

| Campo | Conteudo |
|---|---|
| Confirmado apos leitura? | |
| Data | |
| Ajustes solicitados | |
