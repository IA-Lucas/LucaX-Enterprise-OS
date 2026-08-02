---
id: RFC-0004-enterprise-artifact-framework
titulo: Introduzir o Enterprise Artifact Framework como contrato universal do arquetipo Artefato
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
decisoes_relacionadas: [ADR-0006]
substitui: []
substituido_por: null
classe_mudanca: C3
prazo_analise: 2026-07-28
resumo: Propoe o contrato universal de artefato, o registro de tipos documentais e a economia de contexto, sem criar entidade nem ontologia.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
---

# RFC-0004: Enterprise Artifact Framework

## Proposito
Propor o contrato universal de tudo que a organizacao cria, governa, consulta, evolui e
aposenta — atributos, tipos documentais, ciclo, autoridade, linhagem, economia de contexto e
regras de especializacao —, mantendo `Artefato` como **arquetipo** do Meta Model.

## Escopo
Abrange o arquetipo A2 de FND-09 §4. Nao cria entidade, nao cria ontologia formal, nao cria
agente, skill, comando, workflow, produto, codigo nem infraestrutura.

## Responsaveis
| Papel | Quem |
|---|---|
| Proponente | DEP-GOV |
| Areas que devem se manifestar | DEP-QAR (coerencia e aptidao), DEP-KMS (custo de contexto e curadoria), DEP-EXE (custo de cadencia) |
| Aprovador | SOBERANO |
| Prazo de manifestacao | 2026-07-28 |

---

## 1. Situacao atual

Dez documentos normativos, 23 Capabilities, 6 decisoes, 4 propostas, 19 templates e 8 indices
— **76 artefatos e 15.939 linhas** na abertura desta proposta (medicao `wc -l`, 2026-07-28).

O que ja existe sobre artefatos esta correto e incompleto:

| Onde | O que ja diz | O que nao diz |
|---|---|---|
| FND-03 §4 | 15 campos obrigatorios de frontmatter | Resumo, perfil de contexto, confidencialidade, revisor, ratificacao |
| FND-03 §3 | Definicao canonica de 14 componentes | Que **formas documentais** cada entidade admite |
| FND-09 §4 | `Artefato` e arquetipo A2, com 19 membros | O que o arquetipo **obriga** alem do frontmatter |
| FND-09 §5 | 21 entidades | Onde encaixam indice, revisao arquitetural, playbook, checklist |
| FND-01 §6.3 | Metrica "Contexto por papel" | Como se mede, e quem a le |

## 2. Problema

| # | Defeito | Consequencia |
|---|---|---|
| P1 | **Tipos documentais nao declarados.** Indice (`IDX`, 8 instancias) e Revisao Arquitetural (`REV`, 2 instancias) existem, tem ID proprio e **nao constam de FND-03 §2 nem de FND-09 §5**. | 10 artefatos — 13% do acervo — sem tipo declarado. Pela regra MT-01, seriam nulos. Sao, na pratica, os contadores oficiais de sequencia e os pareceres de corretude do sistema. |
| P2 | **Carregamento integral e o padrao implicito.** Nada declara o que precisa ser lido para executar uma tarefa. | Ler a Fundacao inteira custa 15.939 linhas. A metrica "Contexto por papel" de FND-01 §6.3 nunca foi medida porque nao ha unidade nem instrumento. |
| P3 | **Sem contrato de resumo.** Nenhum artefato declara em uma linha o que faz. | Decidir se um artefato e relevante exige abri-lo — o que e exatamente o custo que se quer evitar. |
| P4 | **Independencia de revisao nao e verificavel por varredura.** `autor` e `aprovador` existem; `revisor` nao. | Verificar LV-03 exige leitura, nao varredura. Foi assim que o achado M1 — autoverificacao de `CAP-governanca` — sobreviveu a duas auditorias. |
| P5 | **Ratificacao sem estado.** Nao havia campo que distinguisse "ratificada" de "declarada". | Quatro ADRs C3/Tipo 1 registraram ratificacao inferida ([INC-2026-001](../governance/incidents/INC-2026-001-ratificacao-inferida.md)). |

## 3. Pergunta de decisao

O LucaX deve adotar um contrato universal de artefato, com registro de tipos documentais,
economia de contexto medida e motor de especializacao, antes de criar componentes?

## 4. Criterios de avaliacao

| # | Criterio | Peso | Como se mede |
|---|---|---|---|
| C1 | Classifica **100%** do acervo existente | **Bloqueante** | Nenhum artefato sem tipo declarado |
| C2 | Nao cria entidade nem ontologia | **Bloqueante** | Universo permanece em 21 entidades; nenhum modelo formal |
| C3 | Reduz custo de contexto de forma medida | Alto | Nucleo obrigatorio declarado, em linhas medidas |
| C4 | Nao duplica norma vigente | **Bloqueante** | Estados, relacoes e autoridade referenciados, nunca reescritos |
| C5 | Custo de migracao proporcional | Alto | Numero de arquivos existentes que precisam ser reescritos |
| C6 | Torna verificavel por varredura o que hoje exige leitura | Alto | Campos que permitem checagem automatica de LV-03 e de ratificacao |

## 5. Opcoes

### Opcao A — Framework com contrato em tres camadas e catalogo mestre

| Campo | Conteudo |
|---|---|
| Descricao | FND-10 com contrato L1/L2/L3, Canon Semantico, 33 tipos documentais, 9 operacoes de ciclo, 3 classes de mutabilidade, 4 perfis de contexto com custo medido, motor de especializacao. Catalogo mestre unico; `TPL-documento` estendido |
| A favor | Unica que satisfaz C1, C3, C5 e C6 juntos. O resumo e o perfil vivem no catalogo para o acervo existente — **zero arquivo reescrito** |
| Contra | Acrescenta documento fundacional e emenda C3 a hierarquia; cria um artefato de catalogo a manter |
| Custo | 1 documento normativo, 1 catalogo, 1 template estendido, 5 campos novos com valor padrao |
| Risco | Catalogo desatualizar; contrato virar burocracia |

### Opcao B — Estender apenas FND-03 §4 com os cinco campos

| Campo | Conteudo |
|---|---|
| Descricao | Acrescentar `resumo`, `perfil_contexto`, `confidencialidade`, `revisor` e `ratificacao` ao frontmatter obrigatorio, sem framework proprio |
| A favor | Custo minimo; nenhum documento novo; resolve P3, P4 e P5 |
| Contra | **Nao resolve C1** — os tipos `IDX` e `REV` continuam sem declaracao. **Nao resolve C3** — sem perfis nem custo medido, `perfil_contexto` seria campo sem semantica. E **exigiria migrar 76 arquivos**, falhando C5: cada campo obrigatorio novo sem valor padrao obriga tocar todo o acervo (EV-02) |
| Custo | Baixo no papel; 76 arquivos reescritos na pratica |
| Risco | Alto — campos declarados sem uso viram ruido |

### Opcao C — Catalogo mestre apenas, sem contrato normativo

| Campo | Conteudo |
|---|---|
| Descricao | Criar o catalogo com resumo, tipo e custo de cada artefato; nao normatizar contrato nem tipos |
| A favor | Resolve P1 e P3 descritivamente; custo baixo; nenhum campo novo |
| Contra | **Nao resolve C6** — sem `revisor` e `ratificacao` no frontmatter, LV-03 e a ratificacao continuam inverificaveis por varredura, que e a causa de P4 e P5. E repete a fragilidade ja identificada em ADR-0002 §6 e ADR-0003 §6: catalogo que nada obriga a manter desatualiza e passa a enganar |
| Custo | Baixo |
| Risco | Medio-alto — documento decorativo |

### Opcao Z — Nao fazer nada

| Campo | Conteudo |
|---|---|
| O que acontece | 10 artefatos permanecem sem tipo; o carregamento integral continua sendo o padrao; ratificacao e revisao continuam inverificaveis por varredura |
| Custo real da inacao | Cresce com cada artefato: hoje sao 76 e 15.939 linhas, sem departamento, agente ou produto criado. A fase seguinte multiplica o acervo |
| Por que nao venceu | P1 ja e violacao de MT-01 em 13% do acervo, e P5 ja produziu um incidente de severidade alta |

## 6. Recomendacao do proponente

**Opcao A.**

A Opcao B falha em C5 por um motivo que so aparece quando se le EV-02: campo obrigatorio novo
exige **valor padrao declarado ou janela de migracao**. Cinco campos sem valor padrao
significam 76 arquivos reescritos — e reescrever o acervo para melhorar sua governanca e
precisamente o tipo de custo que a governanca deveria evitar. A Opcao A resolve isso pondo
resumo e perfil no **catalogo**, nao no frontmatter do acervo antigo.

A Opcao C falha em C6, que e o criterio ligado as duas falhas ja materializadas: a
autoverificacao que sobreviveu a duas auditorias (P4) e a ratificacao inferida (P5). Ambas
sobreviveram porque **nao eram verificaveis por varredura**. Um catalogo descritivo nao
corrige isso.

Sobre **C2 (bloqueante):** nenhuma entidade e criada. `IDX` e resolvido como **registro
oficial da entidade que indexa** — o contador de sequencia que FND-03 §2.3 ja atribui a
DEP-GOV. `REV` e resolvido como **segundo tipo documental da entidade `FIT`**, preservando a
separacao de vereditos que ADR-0004 §6 exigiu. Playbook, Checklist, Command, Prompt e Norma
Derivada sao recusados com destino declarado. O universo permanece em 21 entidades.

Sobre **C4 (bloqueante):** estados vem de FND-03 §5; perfis de ciclo, de FND-09 §7.2;
relacoes, de FND-09 §6.1; autoridade, de FND-09 §8.2 — todos por referencia, com regra
explicita de precedencia da origem.

## 7. Impacto previsto

| Dimensao | Impacto |
|---|---|
| Documentos afetados | FND-01 (§10, §11), FND-03 (§2 `IDX`/`REV`, §4 contrato, §7 arvore), FND-09 (§5.2 E-08 ampliada, §6.1.1 verbos), `TPL-documento` v1.1.0 |
| Artefatos existentes reescritos | **Zero** — o acervo e classificado por referencia no catalogo |
| Artefatos criados | FND-10; catalogo mestre; RFC e ADR desta mudanca; revisao arquitetural; Fitness Check |
| Camadas de memoria | EST (o framework); OPR (o catalogo, como vista derivada) |
| Ganho PI-14 pretendido | **Organizacao:** 100% do acervo com tipo declarado. **Reuso:** contrato e tipos servem a qualquer artefato futuro. **Reducao de contexto:** nucleo obrigatorio declarado em 1.087 linhas contra 18.916 do acervo — 5,7% medido |
| Sinal que comprovara o ganho | Primeiro trabalho executado carregando apenas o nucleo declarado; primeira varredura que detecte `revisor` = `autor` sem leitura humana |

## 8. Riscos

| # | Risco | Probabilidade | Impacto | Mitigacao |
|---|---|---|---|---|
| R1 | Catalogo mestre desatualizar e passar a enganar | **Alta** | Alto | RG-03: catalogo desatualizado e mudanca **incompleta** (CV-04), nao norma nova; e vista derivada (M3), reprocessavel da fonte |
| R2 | Contrato virar burocracia | Media | Alto | AC-01 proibe declarar o derivavel; 5 campos novos, todos com valor padrao; zero migracao |
| R3 | Perfis de contexto ignorados na pratica | **Alta** | Medio | CE-01 proibe carregamento integral; nucleo declarado e ampliavel so por C2 com Fitness Check |
| R4 | `REV` sob a entidade `FIT` reabrir a fusao que ADR-0004 recusou | Media | Medio | §4.5 declara que os vereditos permanecem separados; o eixo `classe_avaliacao` distingue |
| R5 | Custo medido em linhas ser proxy grosseiro | Media | Baixo | E proxy declarado, verificavel e reproduzivel — preferivel a estimativa (CE-04, LV-12) |
| R6 | **Esta proposta estar errada** — o framework ser peso sem retorno | Media | Alto | EV-08 obriga consolidacao se o ganho nao se confirmar; gatilhos no ADR |

## 9. Perguntas em aberto

| Pergunta | Dono da resposta | Bloqueia? |
|---|---|---|
| `IDX` deve virar entidade propria? | Esta RFC recomenda **nao** — e o registro oficial da entidade que indexa | Nao — decidido no ADR |
| `REV` e `FIT` devem ser a mesma entidade? | Esta RFC recomenda **sim**, com vereditos separados | Nao — decidido no ADR |
| O nucleo obrigatorio esta correto em 5,7%? | DEP-KMS, apos o primeiro trabalho executado sob perfis | **Nao** — ampliar e C2 |
| Custo em linhas ou em tokens? | DEP-KMS | Nao — linhas sao medidas hoje; tokens exigiriam ferramenta (dependencia externa) |

## 10. Manifestacoes

| Area | Posicao | Fundamento | Data |
|---|---|---|---|
| DEP-GOV | Propoe | 13% do acervo sem tipo declarado e violacao de MT-01 em vigor. Exige tratamento como **C3** por acrescentar documento a Fundacao e alterar a hierarquia (FND-01 §10) | 2026-07-28 |
| DEP-QAR | Apoia com ressalva | Aceita a analise. Registra que o ganho de contexto e **calculado, nao observado**: nenhum trabalho foi executado sob os perfis propostos. Exige Fitness Check e gatilho de confirmacao | 2026-07-28 |
| DEP-KMS | Apoia | O custo medido em linhas e a primeira unidade verificavel para "Contexto por papel", declarada em FND-01 §6.3 e nunca medida. Aceita a custodia do resumo no catalogo | 2026-07-28 |
| DEP-EXE | Apoia com ressalva | Aceita, desde que o contrato **nao exija migracao do acervo** e que nenhum arquivo auxiliar por artefato seja criado (RG-05) | 2026-07-28 |

## 11. Resultado

| Campo | Conteudo |
|---|---|
| Decisao | **aceita** |
| ADR gerado | [ADR-0006](../decisions/ADR-0006-adocao-do-enterprise-artifact-framework.md) |
| Ressalvas incorporadas | Classe **C3, Tipo 1** (DEP-GOV); gatilhos de confirmacao e Fitness Check (DEP-QAR); zero migracao e RG-05 (DEP-EXE) |
| Data | 2026-07-28 |
| Responsavel | DEP-GOV |
