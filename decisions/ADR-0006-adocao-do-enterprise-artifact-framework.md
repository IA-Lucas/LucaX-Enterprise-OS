---
id: ADR-0006-adocao-do-enterprise-artifact-framework
titulo: Adotar o Enterprise Artifact Framework como contrato universal do arquetipo Artefato
tipo: adr
versao: 1.0.0
status: aprovado
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0003, ADR-0004, ADR-0005]
substitui: []
substituido_por: null
classe_mudanca: C3
tipo_decisao: 1
supera: []
superado_por: null
ratificacao: pendente
resumo: Adota FND-10, classifica 100% do acervo, resolve IDX e REV sem criar entidade e declara nucleo de contexto de 5,7%.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
---

# ADR-0006: Adotar o Enterprise Artifact Framework

> **Estado `aprovado`, nao `ativo`.** Esta decisao e C3 e Tipo 1: sua eficacia depende de ato
> explicito e datado do Soberano sobre este texto (PI-06, CV-09, LM-02). **Esse ato nao
> ocorreu.** O campo de ratificacao permanece vazio, por determinacao expressa e nao por
> esquecimento — ver §14.

## Proposito

Registrar a decisao de criar o Enterprise Artifact Framework (FND-10): o contrato universal
de atributos, o Canon Semantico, o registro de 33 tipos documentais, as nove operacoes de
ciclo de vida, o controle de mudanca por classe, a linhagem, a economia de contexto medida e
o motor de especializacao de artefatos.

## Escopo

Aplica-se ao arquetipo **A2 ARTEFATO** de FND-09 §4. Nao cria entidade, nao cria ontologia
formal, nao cria agente, skill, comando, workflow, produto, projeto, ferramenta, codigo nem
infraestrutura.

## Responsaveis

| Papel | Quem |
|---|---|
| Proponente | DEP-GOV |
| Revisor independente | **DEP-QAR** (RM-06b, ADR-0005 — DEP-GOV nao revisa o que produz) |
| Consulta de custo de contexto | DEP-KMS |
| Consulta de cadencia | DEP-EXE |
| Aprovador | SOBERANO |
| Ratificador | **SOBERANO** — **pendente** |
| Executor | DEP-GOV |
| Quem registra a ratificacao | **DEP-QAR**, papel distinto do executor (CV-09, LM-05) |

---

## 1. Contexto

Ao abrir esta missao o acervo tinha **76 artefatos e 15.939 linhas**; ao encerra-la, **85 e
18.916** (medicao `wc -l`, 2026-07-28). Nao existe nenhum departamento, agente, skill,
workflow, ferramenta, produto ou projeto.

FND-03 define como as coisas se chamam; FND-09 define o que pode existir. Nenhum documento
define **o que todo artefato deve carregar, custar e obedecer**. Tres consequencias ja
materializadas:

1. **Dez artefatos sem tipo declarado.** Indice (`IDX`, 8 instancias) e Revisao Arquitetural
   (`REV`, 2 instancias) tem ID proprio, sao produzidos rotineiramente e nao constam de
   FND-03 §2 nem de FND-09 §5. Pela regra MT-01, seriam nulos — **13% do acervo**.

2. **Carregamento integral como padrao implicito.** A metrica "Contexto por papel" existe em
   FND-01 §6.3 desde ADR-0001 e nunca foi medida, porque nao havia unidade nem instrumento.

3. **Duas falhas que sobreviveram por nao serem verificaveis por varredura:** a
   autoverificacao de `CAP-governanca` — corrigida por [ADR-0005](ADR-0005-proibicao-de-autoverificacao.md)
   — e a ratificacao inferida em quatro ADRs C3/Tipo 1 —
   [INC-2026-001](../governance/incidents/INC-2026-001-ratificacao-inferida.md). Ambas
   exigiam leitura atenta para serem detectadas.

## 2. Problema / Pergunta de decisao

O LucaX deve adotar um contrato universal de artefato, com registro de tipos documentais,
economia de contexto medida e motor de especializacao, antes de criar componentes?

## 3. Criterios de decisao

> Definidos antes do exame das alternativas (CD-01). Herdados de
> [RFC-0004 §4](../rfcs/RFC-0004-enterprise-artifact-framework.md).

| # | Criterio | Peso | Como se mede |
|---|---|---|---|
| C1 | Classifica **100%** do acervo | **Bloqueante** | Nenhum artefato sem tipo declarado |
| C2 | Nao cria entidade nem ontologia | **Bloqueante** | Universo permanece em 21 entidades |
| C3 | Reduz custo de contexto de forma medida | Alto | Nucleo declarado, em linhas medidas |
| C4 | Nao duplica norma vigente | **Bloqueante** | Estados, relacoes e autoridade referenciados |
| C5 | Custo de migracao proporcional | Alto | Arquivos existentes reescritos |
| C6 | Verificavel por varredura | Alto | Campos que permitem checar LV-03 e ratificacao |

## 4. Alternativas consideradas

### Alternativa A — Framework com contrato em tres camadas e catalogo mestre

| Campo | Conteudo |
|---|---|
| Descricao | FND-10 completo; catalogo mestre unico; `TPL-documento` estendido; 5 campos novos, todos com valor padrao |
| A favor | Unica que satisfaz C1, C3, C5 e C6 juntos; resumo e perfil no catalogo mantem o acervo intocado |
| Contra | Documento fundacional a mais; emenda C3; um catalogo a manter |
| Custo | 1 documento, 1 catalogo, 1 template estendido; **zero arquivo reescrito** |
| Risco | Catalogo desatualizar (R1); contrato virar burocracia (R2) |
| Avaliacao | C1 satisfeito · C2 satisfeito · C3 alto · C4 satisfeito · C5 alto · C6 alto |

### Alternativa B — Estender apenas FND-03 §4 com os cinco campos

| Campo | Conteudo |
|---|---|
| Descricao | Cinco campos novos no frontmatter obrigatorio, sem framework proprio |
| A favor | Custo minimo de norma; resolve resumo, revisor e ratificacao |
| Contra | Nao resolve C1 — `IDX` e `REV` continuam sem tipo. Nao resolve C3 — `perfil_contexto` sem perfis definidos e campo sem semantica. **Falha em C5**: campo obrigatorio sem valor padrao obriga migrar os 76 arquivos (EV-02) |
| Custo | Baixo no papel; 76 arquivos reescritos na pratica |
| Risco | Alto — campos sem uso viram ruido |
| Avaliacao | C1 **falha** · C2 satisfeito · C3 baixo · C4 satisfeito · C5 **falha** · C6 medio |

### Alternativa C — Catalogo mestre apenas, sem contrato normativo

| Campo | Conteudo |
|---|---|
| Descricao | Catalogo descritivo com resumo, tipo e custo; sem normatizar contrato nem tipos |
| A favor | Resolve a classificacao descritivamente; custo baixo; nenhum campo novo |
| Contra | **Falha em C6.** Sem `revisor` e `ratificacao` no frontmatter, LV-03 e a ratificacao permanecem inverificaveis por varredura — que e a causa das duas falhas ja materializadas. Repete a fragilidade de ADR-0002 §6 e ADR-0003 §6: catalogo que nada obriga a manter desatualiza e passa a enganar |
| Custo | Baixo |
| Risco | Medio-alto — documento decorativo |
| Avaliacao | C1 alto · C2 satisfeito · C3 medio · C4 satisfeito · C5 alto · C6 **falha** |

### Alternativa Z — Nao fazer nada

| Campo | Conteudo |
|---|---|
| O que acontece | 13% do acervo permanece sem tipo; carregamento integral segue implicito; ratificacao e revisao seguem inverificaveis |
| Custo real da inacao | Cresce com o acervo. Hoje sao 76 artefatos sem nenhum componente criado; a fase seguinte multiplica |
| Por que nao venceu | A ausencia de tipo ja e violacao de MT-01 em vigor, e a ausencia de verificabilidade ja produziu um incidente de severidade alta |

## 5. Decisao

**Decidimos adotar o Enterprise Artifact Framework**, composto de:

1. **FND-10**, incorporado a Fundacao como documento de nivel 2, em estado `aprovado` ate a
   ratificacao (§14).

2. **Contrato de artefato em tres camadas** (FND-10 §2): L1 declarado, L2 curado no catalogo,
   L3 derivado. Regra **AC-01**: atributo derivavel nao entra no frontmatter.

3. **Cinco campos novos**, todos com valor padrao — `resumo`, `perfil_contexto`,
   `confidencialidade`, `revisor`, `ratificacao`. **Nenhum arquivo do acervo e reescrito.**

4. **Canon Semantico** (FND-10 §3), com quatro termos resolvidos — Fundador, Mission,
   Ontology, Artifact — e tres gatilhos para promocao a ontologia formal, **nenhum observado**.

5. **Registro de 33 tipos documentais sobre 21 entidades** (FND-10 §4), com finalidade,
   entidade, conteudo proibido, local e template. **Seis tipos recusados** com destino
   declarado: Norma Derivada, Command, Prompt, Playbook, Checklist e Evaluation.

6. **Resolucao de `IDX` sem criar entidade:** o indice e o **registro oficial da entidade que
   indexa** — o contador de sequencia que FND-03 §2.3 ja atribui a DEP-GOV. Regras IX-01 e
   IX-02: nao contem informacao original; desatualizado e mudanca incompleta.

7. **Resolucao de `REV` sem criar entidade:** a Revisao Arquitetural passa a ser o **segundo
   tipo documental da entidade `FIT`**, distinguido pelo eixo `classe_avaliacao: corretude |
   aptidao`. Os dois **vereditos permanecem separados**, preservando ADR-0004 §6.

8. **Nove operacoes de ciclo de vida** sobre os oito estados existentes, com criterio
   verificavel e rollback (FND-10 §5). **Nenhum estado novo.**

9. **Ratificacao como condicao de validade** (FND-10 §5.4, LM-02 a LM-06) — correcao de causa
   de INC-2026-001. Sem ato explicito, o artefato permanece `aprovado`.

10. **Tres classes de mutabilidade** (FND-10 §6.2): M1 imutavel, M2 versionavel, M3 derivado.
    **CC-01: ADR historico nunca e editado**, nem para registrar ratificacao posterior.

11. **Nove verbos de linhagem mapeados** as dez relacoes existentes (FND-10 §7.1);
    `restringe` declarado **ato de autoridade**, fora do grafo de dependencia. Bilateralidade
    e do registro, nao do frontmatter (LN-01), com excecao de `substitui` (LN-02).

12. **Quatro perfis de contexto** com custo **medido em linhas** (FND-10 §8). **CE-01 proibe
    carregamento integral por padrao.** Nucleo obrigatorio declarado em **1.087 linhas +
    2 recortes**, contra 18.916 do acervo — **5,7% medido**.

13. **Motor de especializacao de artefato** com sete sinais e quatro movimentos (FND-10 §9).
    **SE-01: ganho previsto nao autoriza divisao. SE-02: um unico sinal nao basta.**

14. **`TPL-documento` estendido a v1.1.0** — nenhum template novo. Os 19 vigentes verificados
    contra os testes T1–T4: **19 de 19 passam**.

15. **Catalogo mestre** em `governance/artifact-registry.md`, classificando **79 de 79
    artefatos**. **RG-05: nenhum arquivo auxiliar por artefato.**

## 6. Justificativa

A Alternativa A vence nos dois criterios bloqueantes e nos tres de maior peso.

A Alternativa B falha em **C5** por uma razao que so aparece ao aplicar EV-02: campo
obrigatorio novo exige valor padrao **ou** janela de migracao. Cinco campos sem valor padrao
significam reescrever 76 arquivos — reescrever o acervo para melhorar sua governanca e
exatamente o custo que a governanca existe para evitar. A Alternativa A o elimina pondo
`resumo` e `perfil_contexto` no catalogo, e nao no frontmatter do acervo antigo.

A Alternativa C falha em **C6**, o criterio ligado as duas falhas ja materializadas. Tanto a
autoverificacao quanto a ratificacao inferida sobreviveram porque **exigiam leitura para
serem detectadas**. Um catalogo descritivo nao muda isso; os campos `revisor` e `ratificacao`
mudam.

Sobre **C2 (bloqueante)**: nenhuma entidade e criada. As duas candidatas naturais foram
resolvidas dentro do universo existente. `IDX` nao passa em TE-2 — o indice nao persiste alem
do que indexa, e seu conteudo e projecao. `REV` passa em TE-1 a TE-7, **e mesmo assim nao
vira entidade**, porque a entidade `FIT` ja responde a mesma pergunta — parecer datado de
DEP-QAR ao encerrar mudanca estrutural. Criar `REV` violaria MT-02.

Sobre **C4 (bloqueante)**: estados vem de FND-03 §5; perfis de ciclo, de FND-09 §7.2;
relacoes, de FND-09 §6.1; autoridade, de FND-09 §8.2 — todos por referencia, com precedencia
declarada da origem.

**Tradeoff aceito (catalogo como L2).** Pondo resumo e perfil no catalogo em vez do
frontmatter, aceita-se que essa informacao viva **fora** do artefato que descreve — e que um
artefato aberto isoladamente nao a carregue. Aceita-se em troca de zero migracao e de fonte
unica: o resumo de 79 artefatos em um lugar so e mais facil de manter coerente do que em 79.

**Tradeoff aceito (custo em linhas).** Linha nao e a unidade de custo real de um modelo de
linguagem. Aceita-se o proxy porque e **medido, verificavel e reproduzivel com uma ferramenta
que ja existe** — enquanto contar tokens exigiria dependencia externa (DP-05). CE-04 e
explicito: metrica sem valor observado e proibida (LV-12).

**Ressalva de DEP-QAR incorporada:** o ganho de contexto e **calculado, nao observado** —
nenhum trabalho foi executado sob os perfis propostos (§8).

**Ressalva de DEP-EXE incorporada:** zero migracao e RG-05 — nenhum arquivo auxiliar por
artefato.

## 7. Impacto

| Dimensao | Impacto |
|---|---|
| Departamentos afetados | DEP-GOV (contrato e catalogo), DEP-KMS (curadoria do resumo e do custo), DEP-QAR (verificacao de ratificacao e de revisor) |
| Componentes afetados | Nenhum existente — nao ha componente criado |
| **Artefatos existentes reescritos** | **Zero.** Os 79 sao classificados por referencia no catalogo |
| Camadas de memoria a atualizar | EST (o framework); OPR (o catalogo) |
| Decisoes superadas | Nenhuma. ADR-0003, ADR-0004 e ADR-0005 sao **complementados** |
| Documentos a atualizar | FND-01 v1.3.0 (§10, §11) · FND-03 v1.3.0 (§2 `IDX`/`REV`, §3.15–3.16, §4.1, §7) · FND-09 v1.2.0 (§5.2 E-08 ampliada, §6.1.1 verbos) · `TPL-documento` v1.1.0 |
| Artefatos criados | FND-10; catalogo mestre; revisao arquitetural; FIT-2026-002 |
| Custo e dependencia criados | Um catalogo a manter sincronizado. **Nenhuma dependencia externa** |
| Ganho PI-14 | **Organizacao:** 100% do acervo com tipo declarado; 13% que era nulo por MT-01 passa a existir formalmente. **Reuso:** contrato, tipos e perfis servem a qualquer artefato futuro. **Reducao de contexto:** nucleo declarado em **5,7%** do acervo, medido — contra acrescimo de **18,7%** no acervo total |

## 8. Evidencias

| # | Evidencia | Origem | Confianca | O que discrimina |
|---|---|---|---|---|
| E1 | 76 artefatos e 15.939 linhas na abertura; 85 e 18.916 no encerramento | `wc -l`, 2026-07-28 | **Alta — medida** | Base de todo o calculo de contexto |
| E2 | 8 indices com id `IDX-*` e 2 revisoes com id `REV-*` nao constam de FND-03 §2 nem de FND-09 §5 | Confronto direto | **Alta — verificavel** | Sustenta P1; elimina Z |
| E3 | FND-09 tem 1.225 linhas — o maior artefato do acervo | `wc -l` | **Alta — medida** | Sustenta o nucleo por recorte, nao integral |
| E4 | A metrica "Contexto por papel" existe desde ADR-0001 e nunca teve valor registrado | FND-01 §6.3; ausencia de serie | **Alta — verificavel** | Sustenta P2 |
| E5 | Duas falhas — autoverificacao e ratificacao inferida — sobreviveram a auditorias por exigirem leitura | ADR-0005 §1; INC-2026-001 §5 | **Alta — verificavel** | Sustenta C6; elimina a Alternativa C |
| E6 | 19 templates verificados contra T1–T4: 19 de 19 passam | FND-10 §10.2 | Alta | Sustenta nao criar template novo |
| E7 | Determinacao do Soberano de que Artifact permanece arquetipo e de que nao se crie ontologia agora | Missao 1.3 | Alta | Elimina alternativas que criariam entidade ou ontologia |

**Evidencia ausente, declarada (VD-05):** **nenhum trabalho foi executado sob os perfis de
contexto propostos.** A reducao a 5,7% e **calculada**, nao observada: e a razao entre o
nucleo declarado e o acervo, nao a medicao de um trabalho real. No mesmo periodo o acervo
**cresceu 18,7%** — as duas coisas sao verdadeiras, e omitir a segunda seria maquiagem. Igualmente, nenhuma varredura
automatizada de `revisor` ou `ratificacao` foi executada — os campos existem, o consumidor
ainda nao. Os ganhos de §7 sao **previstos**, com uma excecao: a classificacao de 100% do
acervo e verificavel hoje, no catalogo.

## 9. Riscos e mitigacao

| # | Risco | Probabilidade | Impacto | Mitigacao |
|---|---|---|---|---|
| R1 | Catalogo mestre desatualizar e passar a enganar | **Alta** | Alto | RG-03: desatualizado e mudanca **incompleta** (CV-04); e vista derivada (M3), reprocessavel da fonte |
| R2 | Contrato virar burocracia | Media | Alto | AC-01 proibe declarar o derivavel; 5 campos, todos com valor padrao; zero migracao |
| R3 | Perfis de contexto ignorados na pratica | **Alta** | Medio | CE-01 proibe carregamento integral; ampliar o nucleo e C2 com Fitness Check |
| R4 | `REV` sob a entidade `FIT` reabrir a fusao que ADR-0004 recusou | Media | Medio | FND-10 §4.5 declara vereditos separados; eixo `classe_avaliacao` distingue |
| R5 | Custo em linhas ser proxy grosseiro | Media | Baixo | Proxy declarado, verificavel e reproduzivel — preferivel a estimativa (CE-04) |
| R6 | O framework aumentar o custo de contexto que se propoe a reduzir | Media | **Alto** | FND-10 tem custo proprio, medido e registrado no catalogo; entra no nucleo apenas por **recorte de secoes** (§2, §4) |
| R7 | **Esta decisao estar errada** — o framework ser peso sem retorno | Media | Alto | EV-08 obriga consolidacao; gatilhos de §12; reversao em §10 |

## 10. Plano de reversao

| Campo | Conteudo |
|---|---|
| Como desfazer | ADR de revogacao superando este; FND-10 passa a `revogado`; emendas em cascata revertidas por nova versao MAIOR; catalogo mestre vai a `arquivado` |
| Custo da reversao | **Muito baixo** — nenhum arquivo do acervo foi alterado para adotar o framework; os cinco campos novos tem valor padrao e nenhum artefato antigo os declara |
| Janela em que ainda e possivel | Encarece a partir do primeiro componente criado sob o contrato. Enquanto o acervo for so normativo, e barata |
| Reversao parcial | **Preferivel e possivel:** manter o catalogo mestre como vista descritiva e revogar apenas o contrato normativo — equivale a recuar da Alternativa A para a C. Igualmente possivel reverter so a economia de contexto (§8), preservando tipos e contrato |
| Quem executa | DEP-GOV, sob ratificacao do Soberano |
| Backup necessario (PI-07) | Copia datada de `foundation/`, `governance/` e `decisions/` antes de qualquer revogacao |

## 11. Classificacao

| Campo | Valor |
|---|---|
| Classe de mudanca | **C3** — acrescenta documento a Fundacao e altera a hierarquia normativa |
| Tipo de reversibilidade | **Tipo 1** — cria contrato vinculante para todo artefato futuro |
| Decisor | SOBERANO |
| Ratificador | SOBERANO |
| Data da decisao | 2026-07-28 |
| Data de vigencia | **Nao vigente** — condicionada a ratificacao (LM-02) |

## 12. Revisao

| Campo | Conteudo |
|---|---|
| Gatilho temporal | 2027-01-28 — revisao semestral da Fundacao |
| Gatilho por evento | **Primeiro trabalho executado carregando apenas o nucleo declarado**: medir se foi suficiente. Confirma C3 |
| Gatilho por evento | Primeira varredura que detecte `revisor` = `autor` ou ratificacao inconsistente **sem leitura humana**. Confirma C6 |
| Gatilho por evento | Primeiro artefato criado ja em conformidade com o contrato completo, sem correcao em revisao |
| Gatilho por sinal de falha | Catalogo mestre divergir da realidade do acervo em qualquer varredura |
| Gatilho por sinal de falha | Custo do nucleo ultrapassar 10% do acervo — sinal de que "nucleo" deixou de ser seletivo |
| Gatilho de consolidacao (EV-08) | Tipo documental sem nenhuma instancia ao fim de um horizonte |
| Sinal de que esta decisao deu errado | Artefatos criados sem consultar FND-10; perfis declarados e ignorados; catalogo mantido por obrigacao e nao por uso; contrato exigindo campos que ninguem le |
| Responsavel pela revisao | DEP-QAR com DEP-KMS; DEP-GOV verifica conformidade |

## 13. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Origem | [RFC-0004](../rfcs/RFC-0004-enterprise-artifact-framework.md), aceita em 2026-07-28 |
| Decisoes superadas | Nenhuma |
| Decisoes relacionadas | [ADR-0003](ADR-0003-adocao-do-enterprise-meta-model.md), [ADR-0004](ADR-0004-adocao-do-architecture-fitness-check.md) e [ADR-0005](ADR-0005-proibicao-de-autoverificacao.md) — complementados |
| Incidente que esta decisao corrige | [INC-2026-001](../governance/incidents/INC-2026-001-ratificacao-inferida.md) — causa F1 e F3 |
| Aprendizado incorporado | [MEM-APR-0001](../memory/aprendizado/MEM-APR-0001-ratificacao-por-precedente.md) → LM-06 |
| Artefatos criados | FND-10; `governance/artifact-registry.md`; revisao arquitetural; FIT-2026-002 |
| Emendas em cascata | FND-01 v1.3.0 · FND-03 v1.3.0 · FND-09 v1.2.0 · `TPL-documento` v1.1.0 |
| Verificacao de aptidao | [FIT-2026-002](../governance/fitness/FIT-2026-002-artifact-framework.md) |
| Registros de memoria | Camada EST — o framework; camada OPR — o catalogo |

---

## Checklist de validade (FND-07 §4.1)
- [x] VD-01 — 3 alternativas reais + "nao fazer nada"
- [x] VD-02 — criterios declarados antes da escolha (herdados da RFC)
- [x] VD-03 — nenhuma alternativa de palha (B e C sao respostas naturais e defensaveis)
- [x] VD-04 — tradeoffs aceitos explicitos (§6: catalogo como L2; custo em linhas)
- [x] VD-05 — ausencia de observacao declarada (§8): o ganho de contexto e calculado
- [x] VD-06 — plano de reversao presente, com duas reversoes parciais (Tipo 1)
- [x] VD-07 — impacto em cascata mapeado e executado (§7)
- [x] VD-08 — data e responsavel presentes
- [x] VD-09 — gatilhos de revisao definidos (§12)

---

## 14. Ratificacao do Soberano — **PENDENTE**

Esta decisao e C3 e Tipo 1. Sua eficacia depende de **ato explicito e datado do Soberano
sobre este texto** (PI-01, PI-06, GV-05, CV-09).

| Campo | Conteudo |
|---|---|
| Ratificado por | *(vazio — nenhum ato ocorreu)* |
| Data | *(vazio)* |
| Forma | *(vazio)* |

### 14.1 Por que este campo esta vazio

Este ADR **rompe deliberadamente** o precedente de ADR-0001 a ADR-0004, que preenchiam esta
secao invocando determinacao generica anterior. Aquele padrao foi registrado como violacao em
[INC-2026-001](../governance/incidents/INC-2026-001-ratificacao-inferida.md), e sua causa
esta corrigida em FND-04 (CV-09) e FND-10 §5.4.

**A determinacao que originou esta missao nao ratifica esta decisao.** Ela pediu que o
framework fosse construido; nao aprovou o texto que resultou. Preencher o campo com essa
determinacao seria repetir exatamente o defeito que esta missao mandou corrigir — e violaria
LV-05, que nao admite excecao.

### 14.2 Escolhas de forma nao determinadas pelo Soberano

Sao atribuiveis a DEP-GOV e devem ser lidas como **proposta**, nao como ordem cumprida:

| # | Escolha | Alternativa recusada |
|---|---|---|
| 1 | `IDX` resolvido como registro oficial da entidade que indexa | Cria-lo como entidade propria (C3) |
| 2 | `REV` como segundo tipo documental de `FIT` | Cria-lo como entidade propria; ou fundir os vereditos |
| 3 | Resumo e perfil no **catalogo**, nao no frontmatter do acervo | Migrar os 79 arquivos |
| 4 | Custo de contexto medido em **linhas** | Tokens, que exigiria dependencia externa |
| 5 | Nucleo obrigatorio em 5,7%, com FND-09 por recorte | Nucleo integral, que custaria 1.225 linhas so de Meta Model |

### 14.3 O que ocorre enquanto a ratificacao nao vier

| Artefato | Estado | Efeito |
|---|---|---|
| Este ADR | `aprovado` | Nao vincula; nao serve de precedente |
| FND-10 | `aprovado` | Revisado e aceito; **nao esta em vigor** |
| Catalogo mestre | `ativo` | Vale como **vista descritiva** — nao depende de ratificacao para descrever o acervo |
| Emendas em cascata | conforme cada documento | FND-01, FND-03 e FND-09 recebem as emendas; sua eficacia herda a mesma pendencia ja registrada em INC-2026-001 |

### 14.4 Ato de ratificacao

Preenchido **por DEP-QAR**, papel distinto do executor (CV-09, LM-05), **somente apos** ato
explicito e datado do Soberano sobre este texto:

| Campo | Conteudo |
|---|---|
| Li o texto final e ratifico? | |
| Data do ato | |
| Forma do ato | |
| Ajustes solicitados | |
| Registrado por (≠ executor) | |
