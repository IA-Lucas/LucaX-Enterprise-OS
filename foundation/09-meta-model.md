---
id: FND-09
titulo: Enterprise Meta Model do LucaX Enterprise OS
tipo: fundacao
versao: 1.6.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-08-02
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0001, ADR-0002, ADR-0003, ADR-0004, ADR-0005, ADR-0006, ADR-0008, ADR-0017, ADR-0019, ADR-0032]
ratificacao: ratificada
resumo: Declara o universo fechado de 21 entidades, suas relacoes, estados, autoridade e regras de evolucao.
perfil_contexto: nucleo
confidencialidade: interno
revisor: DEP-QAR
substitui: []
substituido_por: null
---

# Enterprise Meta Model

## Proposito

Definir o universo oficial do LucaX Enterprise OS: quais **tipos de entidade** podem
existir, que atributos minimos cada um possui, que relacionamentos sao permitidos entre
eles, por quais estados passam, quem tem autoridade sobre quem, quais dependencias sao
proibidas e como entidades novas entram sem quebrar compatibilidade.

Este documento e a **gramatica** do sistema. A Taxonomia (FND-03) diz como as coisas se
**chamam**; o Meta Model diz o que pode **existir** e como se **liga**. Nenhum Framework
futuro pode introduzir entidade estrutural sem obedecer a ele.

## Escopo

| Item | Definicao |
|---|---|
| **Inclui** | Estratos, arquetipos, as entidades oficiais e seus atributos minimos, entidades recusadas com destino declarado, modelo de relacionamentos, modelo de ciclo de vida, modelo de autoridade, regras de dependencia, regras de evolucao e o mecanismo de Architecture Fitness Check. |
| **Nao inclui** | Instancias (o catalogo de Capabilities, Cartas, ADRs concretos); nomenclatura e localizacao (FND-03); rito de aprovacao (FND-04); formato de mensagem (FND-05); alocacao de memoria (FND-06); estrutura do registro de decisao (FND-07); conteudo das competencias (FND-08). |
| **Subordinado a** | [FND-01 Constituicao](01-constituicao.md), [FND-03 Taxonomia](03-taxonomia.md), [FND-04 Governanca](04-governanca.md), [FND-08 Capability Framework](08-capability-framework.md). |
| **Consumido por** | Todo Framework, componente e artefato futuro. Entidade fora deste documento nao existe (MT-01). |

## Responsaveis

| Papel | Responsavel |
|---|---|
| Proprietario | DEP-GOV |
| Guardiao normativo | DEP-GOV |
| Verificacao de coerencia e aptidao | DEP-QAR |
| Arbitragem de merito entre entidades | DEP-EXE |
| Custodia do registro na memoria EST | DEP-KMS |
| Aprovador de mudanca | SOBERANO (C3, indelegavel) |

---

## 1. O Que E o Meta Model

### 1.1 A pergunta que ele responde

Cada documento da Fundacao responde a uma pergunta que nenhum outro responde:

| Documento | Pergunta |
|---|---|
| FND-01 Constituicao | Por que existimos e o que nunca se viola? |
| FND-02 Estrutura | Quem responde por que? |
| FND-03 Taxonomia | Como as coisas se chamam e onde vivem? |
| FND-04 Governanca | Como algo nasce, muda e desaparece? |
| FND-05 Comunicacao | Como a informacao circula? |
| FND-06 Memoria | Como a organizacao lembra? |
| FND-07 Decisoes | Como se escolhe e se registra? |
| FND-08 Capabilities | O que a organizacao sabe fazer? |
| **FND-09 Meta Model** | **O que pode existir, e como as coisas se ligam?** |

Antes deste documento, a resposta existia de forma dispersa: FND-03 listava tipos com
prefixo e local; FND-04 listava pre-condicoes de criacao; FND-08 listava relacoes entre
Capabilities. Nenhum documento declarava o **conjunto fechado** de entidades, nem as
relacoes permitidas entre tipos diferentes, nem a autoridade de cada um sobre os demais.

### 1.2 Tres niveis de abstracao

| Nivel | O que e | Onde vive | Exemplo |
|---|---|---|---|
| **M2 — Meta** | As regras sobre os tipos | **Este documento** | "Agente pertence a exatamente um Departamento" |
| **M1 — Tipo** | Os tipos declarados | FND-03 §3, FND-08, este §5 | `AGT`, `CAP`, `MEM` |
| **M0 — Instancia** | Os artefatos concretos | `capabilities/`, `decisions/`, ... | `CAP-engenharia`, `ADR-0002` |

**Regra de leitura:** este documento nunca fala de instancias. Onde ele cita `CAP-*`, cita
o **tipo**, nao uma competencia especifica.

### 1.3 O que o Meta Model **nao** faz

| Nao faz | Porque | Onde vive |
|---|---|---|
| Cria instancia de qualquer entidade | Meta Model define tipos | FND-04 §6 |
| Substitui a Taxonomia | Nomenclatura e local sao de FND-03 | FND-03 |
| Define o rito de aprovacao | Instrumento e classe sao de FND-04 | FND-04 §2 |
| Redefine relacoes entre Capabilities | Ja definidas e incorporadas por referencia | FND-08 §5 |
| Julga o merito de uma entidade concreta | Julga forma e coerencia estrutural | DEP-EXE / dominio |

### 1.4 Posicao na hierarquia normativa

FND-09 e documento fundacional de **nivel 2** (FND-01 §10), com uma precedencia interna
declarada: em conflito entre o Meta Model e outro documento de nivel 2 sobre **existencia
ou relacao de tipos**, prevalece o Meta Model; sobre **conteudo do tipo**, prevalece o
documento especializado. Conflito e sempre registrado, nunca resolvido por conveniencia.

## 2. Principios do Meta Model

| # | Principio | Consequencia |
|---|---|---|
| MT-01 | **Universo fechado.** So existe a entidade declarada em §5. | Framework que precise de entidade nova abre RFC de classe C3 (§9.1). Entidade improvisada e nula (GV-01). |
| MT-02 | **Uma entidade, uma pergunta.** Cada entidade responde a uma pergunta que nenhuma outra responde. | Duas entidades com a mesma pergunta sao a mesma entidade com dois nomes — proibido por LX-07. |
| MT-03 | **Tipo nao e instancia.** | Contar instancias nao justifica criar tipo; contar tipos nao mede a organizacao. |
| MT-04 | **Atributo minimo e obrigatorio.** Ausencia invalida a instancia. | DEP-GOV devolve sem analise de merito. |
| MT-05 | **Relacao e declarada dos dois lados.** | Declaracao unilateral e elo quebrado (herda RL-03). |
| MT-06 | **Sem orfaos.** Toda entidade tem exatamente um dono e, quando contida, exatamente um pai. | Herda ES-01. |
| MT-07 | **Sem ciclo em dependencia dura.** | Herda DP-03 e RL-01. |
| MT-08 | **Um conjunto de estados para todos.** O ciclo documental de FND-03 §5 vale para toda entidade; eixos proprios sao ortogonais e declarados (§7.3). | Nao se inventa estado por tipo. |
| MT-09 | **Autoridade nao se presume.** O que o §8 nao concede, nao existe. | Herda PI-01 e ES-06. |
| MT-10 | **Abstracao antes de multiplicacao.** Antes de criar entidade, verificar se o caso e atributo, classe ou arquetipo de entidade existente. | E o filtro que produziu as treze recusas de §5.8. |
| MT-11 | **Compatibilidade retroativa.** Entidade ou atributo novo nunca invalida instancia ja aprovada. | Se invalidaria, e remocao seguida de criacao (§9.3). |
| MT-12 | **O Meta Model se mede.** Toda mudanca que o toca passa por Architecture Review **e** Architecture Fitness Check (§10). | Arquitetura que nao se mede degrada sem aviso. |

## 3. Estratos

Todo tipo de entidade pertence a **exatamente um** estrato. O estrato responde "de que
natureza e esta entidade" e ordena a direcao permitida das dependencias (§9).

```
  ESTRATO 0  RAIZ            quem e a organizacao e quem tem a palavra final
       ^                     ORG · SOBERANO
       |
  ESTRATO 1  NORMATIVO       o que obriga, o que autoriza, o que registra ato de governanca
       ^                     FND · ADR · RFC · EXC · INC · FIT
       |
  ESTRATO 2  COMPETENCIA     o que a organizacao sabe fazer
       ^                     CAP
       |
  ESTRATO 3  ESTRUTURAL      quem responde e quem executa
       ^                     DEP · AGT · SUB
       |
  ESTRATO 4  EXECUCAO        com que procedimento, sequencia, forma e meio
       ^                     SKL · WFL · TOL · TPL
       |
  ESTRATO 5  VALOR           o que se entrega e sob que definicao
       ^                     PRO · PRJ · SPC
       |
  ESTRATO 6  COGNITIVO       o que se sabe, o que se transferiu
                             MEM · MSG

  Dependencia dura so aponta para BAIXO no desenho acima (para estrato de numero menor)
  ou para o mesmo estrato. Nunca para cima (PD-11).
```

### 3.1 Por que a ordem e esta

O criterio e **estabilidade**: quanto menor o numero do estrato, menos a entidade muda e
mais coisas quebram se ela mudar. A ordem espelha, e nao contraria, a hierarquia normativa
de FND-01 §10 e a estabilidade crescente da memoria de FND-06 §2.

### 3.2 Estrato nao e hierarquia de autoridade

Estar em estrato inferior nao da autoridade sobre o superior. `MEM` (estrato 6) nao manda
em ninguem; `CAP` (estrato 2) nao manda em `DEP` (estrato 3). Autoridade e materia
exclusiva de §8.

## 4. Arquetipos

Arquetipo e **classe abstrata**: nunca e instanciado, existe para declarar uma regra uma
vez em vez de vinte e uma. Uma entidade pode ter mais de um arquetipo.

| # | Arquetipo | Teste de pertencimento | Regras que herda | Entidades |
|---|---|---|---|---|
| **A1** | **ATOR** | Pode ser sujeito de uma relacao de autoridade, emitir e receber mensagem, e responder por resultado | Nivel de autonomia declarado (FND-01 §7.2); nunca se autopromove (LV-07); comunica-se pelos cinco canais (FND-05 §2) | SOBERANO, DEP, AGT, SUB |
| **A2** | **ARTEFATO** | Persiste como documento com frontmatter universal | FND-03 §4 (frontmatter), §5 (estados), §6 (versionamento), §7 (localizacao); DoD de FND-01 §6.1 | Todas, exceto ORG e SOBERANO |
| **A3** | **COMPONENTE** | Da existencia formal a uma parte da organizacao | Carta obrigatoria (PI-12); vinculo a ao menos uma Capability (FND-08 §8); pre-condicoes de criacao (FND-04 §6) | DEP, AGT, SUB, SKL, WFL, TOL, PRO, PRJ |
| **A4** | **INSTRUMENTO** | Registra ou autoriza um ato de governanca, datado e com emissor nomeado | Rastreabilidade de FND-04 §5; emissor ≠ aprovador (PI-05); nunca editado apos eficacia (LV-04) | ADR, RFC, EXC, INC, FIT |

### 4.1 Regras de arquetipo

| # | Regra |
|---|---|
| AQ-01 | Arquetipo **nao e instanciavel**. Nao existe artefato cujo tipo seja "Artefato". |
| AQ-02 | Arquetipo novo e mudanca **C3** (§9.1). |
| AQ-03 | Arquetipo com **um unico membro** e suspeito: ou e a propria entidade disfarcada, ou lhe faltam membros. Sinal verificado no Fitness Check (F3). |
| AQ-04 | Regra que vale para todos os membros de um arquetipo e escrita **no arquetipo**, nunca repetida entidade a entidade (MM-01). |
| AQ-05 | ORG e SOBERANO nao sao Artefato: a organizacao e materializada pela Constituicao, e o Soberano antecede qualquer documento. |

### 4.2 Sobre "Artefato" nao ser entidade

`Artifact` aparecia na lista de candidatos como entidade. Ele **e um arquetipo**, nao uma
entidade: nao ha nada que seja "um artefato" sem ser tambem uma decisao, uma memoria, uma
spec ou uma carta. Instanciar Artefato produziria um documento sem pergunta propria,
violando MT-02. Esta e a primeira aplicacao de MT-10: abstracao antes de multiplicacao.

## 5. Enterprise Entity Model

Vinte e uma entidades oficiais. Cada bloco declara os seis campos exigidos — identidade,
proposito, responsabilidade, autoridade, ciclo de vida e relacionamentos validos — mais os
atributos minimos e o arquetipo.

> **Leitura da coluna Autoridade:** descreve o que a entidade pode fazer **por si**. O que
> pode ser feito **sobre** ela esta em §8.

---

### 5.1 Estrato 0 — Raiz

#### E-01 · Organizacao — `ORG`

| Campo | Definicao |
|---|---|
| **Identidade** | `ORG-<slug>`. Instancia unica: `ORG-lucax`. Materializada pela Constituicao; **nao possui Carta propria** (AQ-05). |
| **Proposito** | Ser o limite do universo: tudo que existe, existe dentro dela. |
| **Responsabilidade** | Sustentar missao, visao, valores e a cadeia de autoridade. |
| **Autoridade** | Nenhuma por si — a Organizacao nao age; agem o Soberano e os Departamentos. |
| **Ciclo de vida** | Perfil P0 (permanente, §7.2). Nao nasce nem se aposenta por decisao interna. |
| **Relacionamentos validos** | `contem` DEP (1→1..n) · `contem` PRO (1→0..n) · `contem` CAP (1→1..n) · `e-governada-por` FND-01 |
| **Atributos minimos** | id, missao, visao, valores, principios imutaveis, linhas vermelhas — todos residentes em FND-01 |
| **Arquetipos** | — |
| **Cardinalidade** | **Exatamente 1.** Segunda instancia e erro conceitual, nao expansao. |

#### E-02 · Soberano — `SOBERANO`

| Campo | Definicao |
|---|---|
| **Identidade** | Identificador reservado literal `SOBERANO`, ja em uso no frontmatter universal. Nao recebe numeracao. |
| **Proposito** | Ser a autoridade final e indelegavel do sistema (PI-01). |
| **Responsabilidade** | Direcao, arbitragem de tradeoff, ratificacao de Tipo 1 e C3, juizo final de qualidade. |
| **Autoridade** | Maxima e irrestrita dentro da Constituicao: cria, ratifica, veta, excepciona e aposenta qualquer entidade. Unico que emenda FND-01. |
| **Ciclo de vida** | Perfil P0 (permanente). Nao tem estado documental. |
| **Relacionamentos validos** | `ratifica` ADR/RFC/EXC · `autoriza` EXC · `dirige` DEP-EXE · `veta` qualquer · `e-titular-de` ORG |
| **Atributos minimos** | Nenhum documental. Sua existencia e pressuposto, nao registro. |
| **Arquetipos** | A1 ATOR |
| **Cardinalidade** | **Exatamente 1.** Nao admite delegacao, substituicao ou presuncao (GV-05). |

---

### 5.2 Estrato 1 — Normativo

#### E-03 · Norma Fundacional — `FND`

| Campo | Definicao |
|---|---|
| **Identidade** | `FND-<NN>`, em `foundation/`. Nove instancias vigentes. |
| **Proposito** | Estabelecer o que obriga permanentemente, acima de qualquer decisao ou instrucao. |
| **Responsabilidade** | Ser a unica fonte oficial de verdade organizacional (PI-02). |
| **Autoridade** | Obriga toda entidade. Prevalece sobre ADR, Carta, spec, memoria e prompt (FND-01 §10). |
| **Ciclo de vida** | Perfil P1 (normativo). Emenda por versao; texto anterior preservado. |
| **Relacionamentos validos** | `governa` toda entidade · `deriva-de` FND-01 · `e-emendada-por` ADR · `e-excepcionada-por` EXC (se nao petrea) |
| **Atributos minimos** | Frontmatter universal + Proposito/Escopo/Responsaveis + Historico de versoes |
| **Arquetipos** | A2 ARTEFATO |
| **Cardinalidade** | 1..n. Criar FND novo e **C3** com ratificacao. |

#### E-04 · Decisao — `ADR`

| Campo | Definicao |
|---|---|
| **Identidade** | `ADR-<NNNN>-<slug>`, em `decisions/`. Numeracao global, atribuida por DEP-GOV, nunca reaproveitada. |
| **Proposito** | Registrar uma escolha ja tomada, com alternativas, criterios, evidencia e plano de reversao. |
| **Responsabilidade** | Ser a prova de que a decisao existiu, por que venceu e o que ela superou (PI-04). |
| **Autoridade** | Vincula todos apos a vigencia, inclusive quem discordou (CD-05). Autoriza a criacao ou alteracao de entidades no escopo aprovado. |
| **Ciclo de vida** | Perfil P2 (instrumento). **Imutavel apos `aprovado`** (LV-04): e superado, nunca editado. |
| **Relacionamentos validos** | `supera` ADR (1→0..1) · `deriva-de` RFC (1→0..1) · `autoriza` criacao/alteracao/aposentadoria de entidade · `emenda` FND · `e-verificada-por` FIT |
| **Atributos minimos** | Universal + `classe_mudanca`, `tipo_decisao`, `supera`, `superado_por` + as 13 secoes de FND-07 §4 |
| **Arquetipos** | A2, A4 |
| **Cardinalidade** | 0..n |

#### E-05 · Proposta — `RFC`

| Campo | Definicao |
|---|---|
| **Identidade** | `RFC-<NNNN>-<slug>`, em `rfcs/`. Numeracao global. |
| **Proposito** | Submeter uma pergunta em aberto a analise antes que ela vire decisao. |
| **Responsabilidade** | Expor alternativas reais, criterios e manifestacoes das areas afetadas. |
| **Autoridade** | Nenhuma vinculante. RFC **pode ser rejeitada** — e resultado valido. |
| **Ciclo de vida** | Perfil P2. Termina em `aprovado` (gera ADR) ou `arquivado` (nunca apagada). |
| **Relacionamentos validos** | `gera` ADR (1→0..1) · `propoe` criacao/alteracao de entidade · `consulta` DEP |
| **Atributos minimos** | Universal + `classe_mudanca`, `prazo_analise` + alternativas + recomendacao do proponente |
| **Arquetipos** | A2, A4 |
| **Cardinalidade** | 0..n |

#### E-06 · Excecao Formal — `EXC`

| Campo | Definicao |
|---|---|
| **Identidade** | `EXC-<AAAA>-<NNN>`, em `governance/exceptions/`. Sequencia por ano. |
| **Proposito** | Autorizar, de forma temporaria e nominal, o descumprimento de norma nao-petrea. |
| **Responsabilidade** | Tornar visivel o que, sem ela, seria improviso. |
| **Autoridade** | Suspende a norma nomeada, apenas no escopo e no prazo declarados. **Somente o Soberano autoriza.** |
| **Ciclo de vida** | Perfil P2 + eixo `vigencia` (§7.3). Expiracao **automatica**; nao ha renovacao tacita. |
| **Relacionamentos validos** | `excepciona` FND/ADR nao-petrea (1→1) · `e-autorizada-por` SOBERANO · `gera` INC se vencer sem regularizacao |
| **Atributos minimos** | Universal + `norma_excepcionada`, `escopo`, `prazo`, `motivo`, `vigencia` |
| **Arquetipos** | A2, A4 |
| **Cardinalidade** | 0..n. Excecao sem prazo e **invalida**. |

#### E-07 · Incidente de Conformidade — `INC`

| Campo | Definicao |
|---|---|
| **Identidade** | `INC-<AAAA>-<NNN>`, em `governance/incidents/`. Sequencia por ano. |
| **Proposito** | Registrar violacao detectada, sua causa, seu efeito e a correcao de ambos. |
| **Responsabilidade** | Converter falha em informacao. Incidente nao e punicao (FND-04 §10). |
| **Autoridade** | **Interrompe a execucao em curso.** Nenhum ator prossegue apos violacao detectada sem INC aberto (LV-11). |
| **Ciclo de vida** | Perfil P2 + eixo `situacao` (§7.3): `aberto` → `contido` → `corrigido` → `fechado`. Fechamento verificado por DEP-QAR. |
| **Relacionamentos validos** | `aponta` FND/ADR violada (1→1..n) · `gera` MEM-APR (1→1, obrigatorio) · `deriva-de` EXC vencida |
| **Atributos minimos** | Universal + `norma_violada`, `severidade`, `efeito`, `causa`, `situacao` |
| **Arquetipos** | A2, A4 |
| **Cardinalidade** | 0..n |

#### E-08 · Avaliacao Arquitetural — `FIT` · `REV`

> Entidade criada por [ADR-0004](../decisions/ADR-0004-adocao-do-architecture-fitness-check.md);
> ampliada por [ADR-0006](../decisions/ADR-0006-adocao-do-enterprise-artifact-framework.md)
> para abranger os **dois tipos documentais** de parecer datado emitido ao encerrar mudanca
> estrutural. Mecanismo de aptidao em §10; contrato dos tipos em FND-10 §4.5.

| Tipo documental | Prefixo | Avalia | Eixo `classe_avaliacao` |
|---|---|---|---|
| Verificacao de Aptidao | `FIT` | Se a arquitetura ficou **mais apta a evoluir** | `aptidao` |
| Revisao Arquitetural | `REV` | Se a arquitetura esta **estruturalmente correta** | `corretude` |

> **Os vereditos permanecem separados.** ADR-0004 §6 recusou fundi-los, e a recusa e
> preservada: sao dois documentos, com perguntas e desfechos distintos. O que se unifica e o
> **tipo de entidade** — mesma natureza, mesmo emissor, mesma imutabilidade, mesmo momento.

| Campo | Definicao |
|---|---|
| **Identidade** | `FIT-<AAAA>-<NNN>-<slug>` em `governance/fitness/`; `REV-<ESCOPO>-<AAAA-MM-DD>` ao lado do que revisa. |
| **Proposito** | Emitir parecer datado e independente ao encerrar mudanca estrutural — de aptidao (`FIT`) ou de corretude (`REV`). |
| **Responsabilidade** | Tornar visivel a degradacao arquitetural incremental, que nenhum portao de corretude detecta. |
| **Autoridade** | Veredito `inapto` **bloqueia o encerramento** da mudanca (veto de DEP-QAR, FT-05). |
| **Ciclo de vida** | Perfil P2 + eixo `veredito`: `apto` \| `apto-com-ressalva` \| `inapto`. |
| **Relacionamentos validos** | `avalia` ADR/RFC (1→1..n) · `avalia` FND alterada · `gera` MEM-APR quando revela causa · `e-executada-por` DEP-QAR |
| **Atributos minimos** | Universal + `objeto_avaliado`, `veredito`, as seis respostas de §10.3 com sinal observavel, ressalvas com dono e gatilho |
| **Arquetipos** | A2, A4 |
| **Cardinalidade** | 0..n. **Uma por mudanca C2 ou C3** (§10.2). |

---

### 5.3 Estrato 2 — Competencia

#### E-09 · Capability — `CAP`

| Campo | Definicao |
|---|---|
| **Identidade** | `CAP-<slug>`, em `capabilities/`. ID imutavel mesmo em transferencia de custodia. |
| **Proposito** | Declarar o que a organizacao sabe fazer, de forma que sobreviva a qualquer reorganizacao. |
| **Responsabilidade** | Ser a espinha dorsal de rastreabilidade: de componente a competencia e de competencia a tudo que a exerce (FND-08 §8.4). |
| **Autoridade** | Nenhuma sobre atores. Capability **habilita e restringe existencia**: componente sem vinculo valido nao e aprovado (VC-01). |
| **Ciclo de vida** | Perfil P1 + eixo `maturidade` (FND-08 §3.3), ortogonal ao `status`. |
| **Relacionamentos validos** | `depende-de`, `habilita`, `consome-saida-de`, `fornece-para`, `especializa`, `verifica`, `coordena` — **entre Capabilities, definidos em FND-08 §5 e incorporados aqui por referencia** · `e-custodiada-por` DEP (1→1) · `e-exercida-por` COMPONENTE (1→0..n) |
| **Atributos minimos** | Universal + os 13 atributos de FND-08 §2 + `dominio`, `classe`, `maturidade`, `custodio`, `exercentes`, `depende_de`, `consumida_por`, `especializa` |
| **Arquetipos** | A2 |
| **Cardinalidade** | 1..n. Criar e **C2 Tipo 1** com ratificacao. |

---

### 5.4 Estrato 3 — Estrutural

#### E-10 · Departamento — `DEP`

| Campo | Definicao |
|---|---|
| **Identidade** | `DEP-<CODIGO>` de tres letras, de lista fechada (FND-03 §2.1). Nove instancias. |
| **Proposito** | Responder por um dominio de responsabilidade exclusivo. |
| **Responsabilidade** | Escopo exclusivo, sem sobreposicao com departamento vizinho (ES-01). |
| **Autoridade** | Decide dentro do escopo; classe Guarda **veta**; classe Comando arbitra Linha; nenhuma classe manda em outra por costume (ES-06). |
| **Ciclo de vida** | Perfil P1. Extincao exige destino explicito de cada responsabilidade **e de cada custodia** (IV-07). |
| **Relacionamentos validos** | `pertence-a` ORG (n→1) · `contem` AGT (1→0..n) · `custodia` CAP (1→0..n) · `exerce` CAP (n→1..n) · `veta` (apenas Guarda) · `handoff` DEP (n→n) |
| **Atributos minimos** | Universal + `classe`, `nivel`, `nivel_autonomia`, `responde_a`, `capabilities`, escopo exclusivo, o que **nao** decide |
| **Arquetipos** | A1, A2, A3 |
| **Cardinalidade** | 1..n. Codigo novo so por ADR que crie departamento. |

#### E-11 · Agente — `AGT`

| Campo | Definicao |
|---|---|
| **Identidade** | `AGT-<DEP>-<papel>`, em `departments/<dep>/agents/`. Papel e substantivo de funcao, nunca verbo. |
| **Proposito** | Executar um papel especializado dentro de exatamente um departamento. |
| **Responsabilidade** | O escopo da propria Carta — e, com igual forca, **o que nao lhe compete**. |
| **Autoridade** | Igual ou inferior a do departamento, nunca superior. Nunca opera acima do `nivel_autonomia_concedido` na mensagem (AG-02). Nunca se autopromove (LV-07). |
| **Ciclo de vida** | Perfil P1. |
| **Relacionamentos validos** | `pertence-a` DEP (n→1) · `contem` SUB (1→0..n) · `exerce` CAP (n→1..n) · `usa` SKL/TOL (n→n) · `participa-de` WFL (n→n) · `emite`/`recebe` MSG |
| **Atributos minimos** | Universal + `departamento`, `nivel_autonomia`, `capabilities`, secao "O que nao me compete" |
| **Arquetipos** | A1, A2, A3 |
| **Cardinalidade** | 0..n. **Nenhuma instancia nesta fase.** |

#### E-12 · Subagente — `SUB`

| Campo | Definicao |
|---|---|
| **Identidade** | `SUB-<DEP>-<papel>`, em `departments/<dep>/agents/sub/`. |
| **Proposito** | Recortar uma parte delimitada do trabalho de um agente, para reduzir o contexto que cada papel precisa carregar (PI-14). |
| **Responsabilidade** | Escopo **estritamente menor** que o do agente pai. |
| **Autoridade** | Sempre menor ou igual a do pai. Comunica-se com o pai, nao com outros departamentos (AG-04). |
| **Ciclo de vida** | Perfil P1. Aposentado obrigatoriamente com o pai. |
| **Relacionamentos validos** | `pertence-a` AGT (n→1, obrigatorio) · `exerce` CAP (n→1..n) · `usa` SKL/TOL |
| **Atributos minimos** | Universal + `agente_pai`, `departamento`, `nivel_autonomia`, `capabilities` |
| **Arquetipos** | A1, A2, A3 |
| **Cardinalidade** | 0..n. **Profundidade maxima 1: subagente nao tem subagente** (IV-04). |

---

### 5.5 Estrato 4 — Execucao

#### E-13 · Skill — `SKL`

| Campo | Definicao |
|---|---|
| **Identidade** | `SKL-<dominio>-<verbo-objeto>`, em `skills/`. Nome sempre e acao. |
| **Proposito** | Tornar reutilizavel um procedimento que produz resultado previsivel. |
| **Responsabilidade** | Pertence a organizacao, nao a um agente. Se so um papel pode usa-la, e procedimento interno da Carta dele, nao Skill. |
| **Autoridade** | Nenhuma. Skill nao decide, nao aprova e nao concede autonomia a quem a invoca. |
| **Ciclo de vida** | Perfil P1. |
| **Relacionamentos validos** | `materializa` CAP (n→1..n) · `e-usada-por` AGT/SUB/WFL (1→0..n) · `usa` TOL (n→n) · `e-acionada-por` gatilho declarado |
| **Atributos minimos** | Universal + `capabilities`, gatilho, entradas, passos, saidas, criterio de verificacao |
| **Arquetipos** | A2, A3 |
| **Cardinalidade** | 0..n. So vira Skill o que se repete **e** tem resultado verificavel. |

#### E-14 · Workflow — `WFL`

| Campo | Definicao |
|---|---|
| **Identidade** | `WFL-<DEP>-<slug>`, em `workflows/`. |
| **Proposito** | Encadear etapas, responsaveis e portoes para produzir um resultado recorrente. |
| **Responsabilidade** | Quando atravessa departamentos, declara **o dono do resultado final** (FND-02 §6). |
| **Autoridade** | Nenhuma propria: o workflow organiza a execucao, nao concede autoridade a nenhuma etapa. |
| **Ciclo de vida** | Perfil P1. |
| **Relacionamentos validos** | `aciona` SKL (1→0..n) · `encadeia` CAP (n→1..n) · `envolve` DEP/AGT (n→n) · `produz` artefato declarado. Portao **nao e entidade**: e ponto de verificacao de FND-01 §6.2, declarado no atributo `portoes` |
| **Atributos minimos** | Universal + `capabilities`, `gatilho`, `portoes`, entradas, etapas com responsavel, saidas, criterio de falha |
| **Arquetipos** | A2, A3 |
| **Cardinalidade** | 0..n |

#### E-15 · Ferramenta — `TOL`

| Campo | Definicao |
|---|---|
| **Identidade** | `TOL-<classe>-<slug>`, em `tools/`. Classes: `mcp`, `api`, `saas`, `local`, `dados`, **`modelo`**. |
| **Proposito** | Registrar uma capacidade **externa** ao sistema, com finalidade, custo, risco e criterio de descarte. |
| **Responsabilidade** | Impedir que qualquer papel improvise acesso externo. |
| **Autoridade** | Nenhuma. Ferramenta e meio, nunca decisor. |
| **Ciclo de vida** | Perfil P1. Descarte exige criterio declarado na adocao. |
| **Relacionamentos validos** | `habilita` CAP (n→1..n) · `e-usada-por` AGT/SUB/SKL · `e-catalogada-por` DEP-TLS (n→1) · `cria` dependencia externa |
| **Atributos minimos** | Universal + `classe`, `dado_trafegado`, `custo`, `criticidade`, `capabilities`, alternativa avaliada, criterio de descarte |
| **Arquetipos** | A2, A3 |
| **Cardinalidade** | 0..n. **Credencial nunca aparece na ficha** — apenas o nome da variavel de ambiente (PI-08). |

#### E-16 · Template — `TPL`

| Campo | Definicao |
|---|---|
| **Identidade** | `TPL-<tipo>`, em `foundation/templates/`. Um template por tipo de artefato recorrente. |
| **Proposito** | Fixar a forma de um tipo de artefato, para que a conformidade seja consequencia do formato e nao de disciplina. |
| **Responsabilidade** | Refletir a taxonomia vigente. Template desatualizado propaga nao conformidade em escala. |
| **Autoridade** | Vincula a **forma** do artefato, nunca o conteudo. |
| **Ciclo de vida** | Perfil P1. |
| **Relacionamentos validos** | `formaliza` um tipo de entidade (1→1) · `e-usado-por` quem produz o tipo · `deriva-de` FND-03 |
| **Atributos minimos** | Universal + instrucoes de uso + bloco-modelo completo |
| **Arquetipos** | A2 |
| **Cardinalidade** | 1..n. **Se um tipo de artefato existe, ele tem template** (FND-03 §3.9). |

---

### 5.6 Estrato 5 — Valor

#### E-17 · Produto — `PRO`

| Campo | Definicao |
|---|---|
| **Identidade** | `PRO-<slug>`, em `products/<slug>/`. |
| **Proposito** | Existir como bem digital com valor, publico e ciclo de vida proprios, alem do esforco que o criou. |
| **Responsabilidade** | Ter criterio de sucesso **e** criterio de encerramento declarados desde a Carta. |
| **Autoridade** | Nenhuma sobre atores. Produto consome competencia; nao a governa. |
| **Ciclo de vida** | Perfil P1. Criacao e encerramento sao **Tipo 1**, decididos pelo Soberano. |
| **Relacionamentos validos** | `pertence-a` ORG (n→1) · `contem` SPC (1→0..n) · `consome` CAP (n→1..n) · `e-operado-por` DEP-OPS · `e-comunicado-por` DEP-GRW |
| **Atributos minimos** | Universal + `capabilities`, publico, problema, proposta de valor, criterio de sucesso, criterio de encerramento |
| **Arquetipos** | A2, A3 |
| **Cardinalidade** | 0..n. **Nenhuma instancia nesta fase.** |

#### E-18 · Projeto — `PRJ`

| Campo | Definicao |
|---|---|
| **Identidade** | `PRJ-<AAAA>-<NNN>`, em `projects/`. Sequencia por ano. |
| **Proposito** | Delimitar um esforco **temporario** com inicio, fim e resultado definidos. |
| **Responsabilidade** | Encerrar. Projeto sem criterio de encerramento nao e aprovado. |
| **Autoridade** | Nenhuma propria: o projeto aloca trabalho, mas a autoridade continua sendo a do departamento responsavel. |
| **Ciclo de vida** | Perfil P1, com termino previsto desde a criacao. **Projeto termina; produto continua.** |
| **Relacionamentos validos** | `produz`/`altera` COMPONENTE (n→n) · `consome` CAP (n→1..n) · `e-alocado-por` DEP-EXE · `e-executado-por` DEP responsavel (n→1) |
| **Atributos minimos** | Universal + `capabilities`, resultado definido, criterio de encerramento, departamento responsavel |
| **Arquetipos** | A2, A3 |
| **Cardinalidade** | 0..n |

#### E-19 · Spec — `SPC`

| Campo | Definicao |
|---|---|
| **Identidade** | `SPC-<NNN>-<slug>`, em `products/<slug>/specs/`. Sequencia por produto. |
| **Proposito** | Definir **o que** deve existir e como se verifica que existe. |
| **Responsabilidade** | Nunca definir o **como**: decisao de arquitetura, tecnologia ou implementacao invalida a spec. |
| **Autoridade** | Vincula o criterio de aceite funcional da entrega (QG-1). |
| **Ciclo de vida** | Perfil P1. |
| **Relacionamentos validos** | `pertence-a` PRO (n→1, obrigatorio) · `define-aceite-de` entrega · `e-verificada-por` DEP-QAR · `deriva-de` MEM-PRD |
| **Atributos minimos** | Universal + `produto`, `criterios_aceite_count`, problema, resultado esperado, escopo negativo, premissas |
| **Arquetipos** | A2 |
| **Cardinalidade** | 0..n. **Nao e Componente:** nao tem Carta e nao declara vinculo a Capability — quem o declara e o Produto que a contem. |

---

### 5.7 Estrato 6 — Cognitivo

#### E-20 · Memoria — `MEM`

| Campo | Definicao |
|---|---|
| **Identidade** | `MEM-<CAMADA>-<NNNN>-<slug>`, em `memory/<camada>/`. Camadas fechadas: EST, PRD, TEC, OPR, APR. |
| **Proposito** | Persistir conhecimento organizacional em exatamente uma camada, com proveniencia. |
| **Responsabilidade** | Um fato, um lugar (MM-01). Registro sem proveniencia e nao confiavel. |
| **Autoridade** | **Nenhuma normativa.** Memoria informa; nao obriga. Em conflito com ADR vigente, o ADR vence (MM-07). |
| **Ciclo de vida** | Perfil P1 para EST/PRD/TEC/APR; **perfil P3 (efemero) para OPR**, onde expirar e o comportamento padrao. |
| **Relacionamentos validos** | `registra` qualquer entidade (n→1) · `promove-para` MEM de camada superior · `refuta`/`e-refutada-por` MEM (APR) · `referencia` ADR |
| **Atributos minimos** | Universal + `origem`, `evidencia`, `confianca`, `ocorrencias`, `ttl`, `aplica_se_a` |
| **Arquetipos** | A2 |
| **Cardinalidade** | 0..n. Promocao para EST **sempre** exige ADR. |

#### E-21 · Mensagem — `MSG`

> Entidade ja operante em FND-05 §3 e ate agora ausente da tabela de identificadores.
> Registrada por [ADR-0003](../decisions/ADR-0003-adocao-do-enterprise-meta-model.md).

| Campo | Definicao |
|---|---|
| **Identidade** | `MSG-<AAAA>-<NNNN>`. Vive na camada de memoria Operacional enquanto vale (FND-05 §9). |
| **Proposito** | Transferir informacao, pedido ou responsabilidade entre atores, com contrato explicito. |
| **Responsabilidade** | Carregar contexto minimo suficiente e criterio de aceite. Mensagem sem campo obrigatorio nao gera obrigacao para o destinatario. |
| **Autoridade** | Apenas a que o canal e o remetente ja possuem. **DIRETIVA** so desce pela cadeia de autoridade; **HANDOFF** so transfere responsabilidade quando aceito (HO-01). |
| **Ciclo de vida** | Perfil P3 (efemero). Mensagem que contem decisao, aprendizado ou fato duravel e **promovida** ao instrumento proprio (FND-05 §9.1) — nao permanece como mensagem. |
| **Relacionamentos validos** | `de`/`para` ATOR (n→1 cada) · `referencia` qualquer entidade por ID · `promove-para` ADR/MEM · `aciona` WFL |
| **Atributos minimos** | Envelope de FND-05 §3 + campos por canal de §3.2 |
| **Arquetipos** | A2 |
| **Cardinalidade** | 0..n. **Silencio nao e mensagem:** nao aprova, nao aceita e nao transfere (CM-07). |

---

### 5.8 Entidades Recusadas

Treze candidatas foram examinadas e **nao** se tornaram entidades. Cada recusa declara onde
a responsabilidade vive hoje e qual sinal reabriria a discussao. Recusa nao e negacao do
problema: e alocacao dele a um instrumento existente (MT-10).

| # | Candidata | Por que nao e entidade | Onde a responsabilidade vive hoje | Gatilho de reabertura |
|---|---|---|---|---|
| X-01 | **Artifact** | E arquetipo, nao entidade: nada e "um artefato" sem ser tambem outra coisa (MT-02) | Arquetipo A2 (§4) | Nunca — abstracao correta |
| X-02 | **Domain** | E eixo de classificacao de Capability, ja fechado em FND-03 §2.4; entidade duplicaria o eixo | Atributo `dominio` de CAP | Se dominio passar a ter dono, ciclo de vida e indicadores proprios |
| X-03 | **Team** | Agrupamento temporario de atores ja tem instrumento: o Projeto | PRJ + alocacao de DEP-EXE | Mesmo conjunto de agentes de 2+ departamentos atuando junto em mais de um projeto, com custo de coordenacao observado |
| X-04 | **Command** | E **forma de acionamento** de Skill ou Workflow, nao coisa distinta (MT-02) | Atributo `gatilho` de SKL e WFL | Superficie de acionamento com ciclo de vida independente do procedimento que aciona |
| X-05 | **Policy** | Regra obrigatoria ja tem instrumento: Norma Fundacional (universal) ou ADR (derivada) | FND + ADR | Primeira regra vigente que nao caiba em FND, ADR nem TPL — abre-se RFC de entidade `Norma Derivada` |
| X-06 | **Standard** | Padrao formal e forma: vive em Template e Taxonomia; padrao tecnico e decisao: vive em ADR | TPL + FND-03 + ADR | Mesmo gatilho de X-05 |
| X-07 | **Prompt** | E a materializacao textual da Carta de um agente ou de uma Skill; instrumento proprio criaria segunda fonte de verdade (MM-01) | Carta de AGT/SUB e corpo de SKL | Nao ha: prompt reutilizado por 2+ componentes **ja e** uma Skill, por definicao |
| X-08 | **Model** | Modelo de IA satisfaz integralmente a ficha de Ferramenta: finalidade, custo, dado trafegado, dependencia, alternativa, descarte | Classe `modelo` de TOL (§5.5) | Se avaliacao de modelo exigir ciclo de vida e indicadores que a ficha de TOL nao comporte |
| X-09 | **Service** | E modo de entrega de um Produto, nao coisa distinta | Atributo do PRO | Algo operado com consumidores e criterio de nivel de servico proprios, sem publico nem roadmap proprios |
| X-10 | **Resource** | Generica demais: reune custo, quota, maquina e credencial — quatro coisas com donos diferentes | TOL (`local`), metrica em MEM-OPR, limite declarado em Carta/ADR, segredo por referencia (PI-08) | Disputa real por capacidade que exija instrumento de alocacao |
| X-11 | **Metric** | E atributo da entidade que ela mede; entidade propria criaria 111 artefatos para 23 Capabilities e fragmentaria o indicador do que ele mede | Indicadores (FND-08 §2, A-12), metricas de saude (FND-01 §6.3); **valores medidos** viram MEM-OPR, promovidos a APR | Mesmo indicador compartilhado por 3+ entidades, obrigando a duplicar a definicao |
| X-12 | **Event** | Fato sem instrumento e fato nao registrado. Os fatos que importam ja tem instrumento | MSG (ALERTA/REPORTE), MEM-OPR, INC, liberacao de portao | Fase de automacao: evento gerado por maquina, em volume, precisando de envelope comum |
| X-13 | **Mission** | E vocabulario operacional para o que a Governanca ja chama de **mudanca C2/C3**; entidade nova violaria LX-07 (um conceito, um nome) | RFC → ADR; PRJ quando houver prazo e alocacao | Se missao passar a ter estado, dono e ciclo distintos dos da mudanca que a origina |

**Regra de recusa (MT-10):** toda recusa acima foi submetida ao Teste de Entidade de §9.1.
Nenhuma falhou por ser irrelevante — todas falharam por **ja ter instrumento**. Recusa sem
destino declarado seria omissao, nao economia.

### 5.9 Sumario do universo

| Estrato | Entidades | Qtd |
|---|---|---|
| 0 Raiz | ORG · SOBERANO | 2 |
| 1 Normativo | FND · ADR · RFC · EXC · INC · FIT | 6 |
| 2 Competencia | CAP | 1 |
| 3 Estrutural | DEP · AGT · SUB | 3 |
| 4 Execucao | SKL · WFL · TOL · TPL | 4 |
| 5 Valor | PRO · PRJ · SPC | 3 |
| 6 Cognitivo | MEM · MSG | 2 |
| **Total** | | **21** |

| Arquetipo | Membros | Qtd |
|---|---|---|
| A1 ATOR | SOBERANO, DEP, AGT, SUB | 4 |
| A2 ARTEFATO | todas menos ORG e SOBERANO | 19 |
| A3 COMPONENTE | DEP, AGT, SUB, SKL, WFL, TOL, PRO, PRJ | 8 |
| A4 INSTRUMENTO | ADR, RFC, EXC, INC, FIT | 5 |

## 6. Relationship Model

### 6.1 As dez relacoes oficiais

Nenhuma outra relacao entre tipos e valida. Relacao inventada em Carta ou spec e elo
invalido e bloqueia aprovacao.

| # | Relacao | Significado | Direcao | Cardinalidade tipica | Dependencia? | Ciclo permitido? |
|---|---|---|---|---|---|---|
| R-01 | `contem` / `pertence-a` | Composicao: o filho nao existe sem o pai | pai → filho | 1 → 0..n | **Sim, dura** | **Nao** |
| R-02 | `exerce` / `e-exercida-por` | O componente materializa uma competencia | componente → CAP | n → 1..n | Sim, de validade | Nao |
| R-03 | `custodia` / `e-custodiada-por` | Zelo por uma competencia, sem monopolio de exercicio | DEP → CAP | 1 → 0..n | **Nao** (§9.4) | Nao |
| R-04 | `depende-de` / `habilita` | Nao opera sem a outra | A → B | n → n | **Sim, dura** | **Nao** (PD-01) |
| R-05 | `consome-saida-de` / `fornece-para` | Usa artefato produzido pela outra | A → B | n → n | Nao | **Sim** |
| R-06 | `verifica` / `e-verificada-por` | Garantia independente sobre a outra | verificador → verificado | n → n | **Proibida** na mesma direcao (PD-04) | Sim, e desejavel |
| R-07 | `coordena` / `e-coordenada-por` | Aloca, prioriza ou arbitra sobre a outra | A → B | 1 → n | Nao | **Nao** |
| R-08 | `supera` / `e-superada-por` | Sucessao temporal de instrumento | novo → antigo | 1 → 0..1 | Nao | **Nao** |
| R-09 | `registra` / `e-registrada-por` | Grava ou transporta fato sobre a outra | MEM/MSG → qualquer | n → 1 | Nao | Sim |
| R-10 | `especializa` / `e-especializada-por` | Recorte mais estreito da entidade mae | filha → mae | n → 1 | Sim, dura | **Nao**; profundidade maxima **1** |

> **Relacoes entre Capabilities** sao as sete de FND-08 §5.1, incorporadas aqui por
> referencia e **nao redefinidas** (C4 de ADR-0002; MM-01). R-04, R-05, R-06, R-07 e R-10
> tem o mesmo nome e a mesma semantica; `contem`, `custodia`, `supera` e `registra` nao se
> aplicam entre Capabilities.

### 6.1.1 Verbos de leitura

Os blocos de §5 usam verbos proximos da linguagem de cada entidade. Todos sao **formas de
leitura das dez relacoes** — nenhum e relacao nova (MT-01). A tabela abaixo e exaustiva:
verbo ausente dela nao existe.

| Verbo usado em §5 | Relacao oficial |
|---|---|
| `pertence-a`, `contem` | R-01 |
| `exerce`, `materializa`, `consome` (componente → CAP), `encadeia` | R-02 |
| `custodia`, `e-custodiada-por` | R-03 |
| `depende-de`, `habilita`, `usa`, `aciona`, `deriva-de`, `implementa`, `cria dependencia` | R-04 |
| `consome-saida-de`, `fornece-para`, `produz`, `consome`, `gera`, `define-aceite-de`, `altera` | R-05 |
| `verifica`, `e-verificada-por`, `avalia`, `valida` | R-06 |
| `coordena`, `dirige`, `e-alocado-por`, `envolve`, `participa-de` | R-07 |
| `supera`, `e-superada-por`, `substitui`, `promove-para`, `refuta` | R-08 |
| `registra`, `referencia`, `aponta`, `evidencia`, `emite`, `recebe`, `de`, `para`, `e-catalogada-por`, `formaliza` | R-09 |
| `especializa`, `e-especializada-por` | R-10 |

**Nao sao relacoes estruturais**, e sim atos ou vinculos de autoridade, regidos por §8:
`ratifica`, `autoriza`, `aprova`, `veta`, `governa`, `restringe`, `e-governada-por`,
`e-emendada-por`, `e-excepcionada-por`, `e-titular-de`, `e-executada-por`. Nao entram no
grafo de dependencia (§9.4).

> **`restringe` em particular.** Subordinacao normativa — a Constituicao restringe tudo — e
> resolvida pela hierarquia de FND-01 §10, nao por aresta. Trata-la como dependencia criaria
> dependencia ascendente universal, violando PD-11 (ADR-0006, FND-10 §7.1).

### 6.2 Pares permitidos por relacao

Par ausente desta tabela e **relacao proibida**.

#### R-01 `contem`

| Pai | Filho | Cardinalidade | Restricao |
|---|---|---|---|
| ORG | DEP | 1 → 1..n | Todo departamento pertence a organizacao |
| ORG | PRO | 1 → 0..n | |
| ORG | CAP | 1 → 1..n | Contencao logica; nao implica dependencia (§9.4) |
| DEP | AGT | 1 → 0..n | Agente pertence a **exatamente um** departamento |
| AGT | SUB | 1 → 0..n | **Profundidade 1**: SUB nao contem SUB (IV-04) |
| PRO | SPC | 1 → 0..n | Spec nao existe sem produto |

#### R-02 `exerce`

| Origem | Destino | Cardinalidade | Restricao |
|---|---|---|---|
| DEP, AGT, SUB, SKL, WFL, TOL, PRO, PRJ | CAP | n → 1..n | **Obrigatoria**: minimo 1, nunca vazia (FND-08 §8) |

Vinculo a Capability inexistente, `proposta` ou `aposentada` e elo quebrado (VC-01).
Vinculo a mais de tres Capabilities e sinal de componente amplo demais (VC-03).

#### R-03 `custodia`

| Origem | Destino | Cardinalidade | Restricao |
|---|---|---|---|
| DEP | CAP | 1 → 0..n | **Custodia unica** (OW-01); dominio `GAR` obrigatoriamente na Guarda (OW-05); classe `nucleo` nunca em departamento de Suporte (OW-04) |

#### R-04 `depende-de`

| Origem | Destino permitido | Restricao |
|---|---|---|
| CAP | CAP | Sem ciclo (RL-01) |
| AGT, SUB | SKL, TOL, WFL | Nunca de agente de outro departamento (PD-12) |
| SKL, WFL | SKL, TOL | Sem ciclo |
| PRO | CAP, TOL | Produto → Produto exige ADR (PD-10) |
| PRJ | CAP, DEP | |
| TOL | TOL externa | Exige alternativa avaliada e criterio de descarte (DP-05) |

Nunca: qualquer entidade → entidade de estrato superior (PD-11). Nunca: FND/ADR →
componente (PD-02). Nunca: CAP → DEP/AGT/TOL/PRO (PD-03).

#### R-05 `consome-saida-de`

| Origem | Destino permitido |
|---|---|
| CAP | CAP |
| AGT, SUB, DEP | qualquer artefato produzido por outro |
| WFL | saida de outro WFL |
| PRO | saida de PRO (sem acoplamento duro) |

#### R-06 `verifica`

| Verificador | Verificado | Restricao |
|---|---|---|
| DEP-GOV | toda entidade, **exceto artefato produzido pelo proprio DEP-GOV** | Forma, conformidade e rastreabilidade (RM-06b) |
| DEP-QAR | toda entidade da Linha e da Plataforma; **artefato produzido por DEP-GOV, como revisor independente da mudanca** | Conteudo, risco e evidencia |
| CAP de dominio `GAR` | CAP verificada | Nunca coexiste com `depende-de` na mesma direcao (RL-05) |
| FIT | ADR, RFC, FND alterada | Executada por DEP-QAR (FT-02) |

#### R-07 `coordena`

| Coordenador | Coordenado |
|---|---|
| SOBERANO | ORG inteira |
| DEP-EXE | DEP de Linha e de Plataforma |
| AGT | SUB proprios |
| WFL | etapas e SKL que aciona |

Guarda **nunca** e coordenada por Linha (ES-02, IV-01).

#### R-08 `supera`

| Origem | Destino | Restricao |
|---|---|---|
| ADR | ADR | Exige explicar **o que mudou** desde a decisao anterior (SU-01) |
| FND vN | FND vN-1 | Texto anterior preservado, nunca apagado |
| CAP nova | CAP fundidas | Fusao gera ID novo (FND-08 §7.3) |
| MEM | MEM refutada | Correcao append-first (MM-09) |

#### R-09 `registra`

| Origem | Destino | Restricao |
|---|---|---|
| MEM | qualquer entidade | Exatamente uma camada por registro (MM-01) |
| MSG | qualquer entidade | Referencia **por ID**, nunca por copia de conteudo (CM-09) |

#### R-10 `especializa`

| Origem | Destino | Restricao |
|---|---|---|
| CAP filha | CAP mae | Profundidade 1 (RL-04) |
| SUB | AGT | Profundidade 1 (IV-04) |
| entidade nova | entidade existente | Especializacao de tipo e **C3** (§9.1) |

### 6.3 Regras de relacionamento

| # | Regra |
|---|---|
| RM-01 | Relacao e declarada nos **dois lados**. Declaracao unilateral e elo quebrado e bloqueia aprovacao (herda RL-03). |
| RM-02 | Relacao entre instancias de tipos cujo par nao consta de §6.2 e **nula**. |
| RM-03 | `contem` implica ciclo de vida acoplado: aposentar o pai obriga destino explicito de cada filho (herda FND-02 §8.3). |
| RM-04 | `exerce` e a **unica** relacao obrigatoria do sistema: todo Componente tem ao menos uma. |
| RM-05 | `custodia` nao e exclusividade de exercicio (OW-02) e nao cria dependencia (§9.4). |
| RM-06 | Uma relacao de `verifica` proibe a relacao inversa `depende-de` no mesmo par (PI-05, ES-02). |
| RM-06b | **`verifica` nao admite par reflexivo: nenhuma entidade verifica a si propria** (LV-03, PI-05). Vale em qualquer estrato e para qualquer entidade. Quando nao houver verificador possivel sem violar RM-06, a verificacao cabe ao **revisor independente da mudanca** (FND-04 §3) e, em materia constitucional, ao Soberano — papeis por mudanca, nao relacao permanente. *(ADR-0005)* |
| RM-07 | Relacao com entidade `depreciada`, `superada` ou `revogada` nao pode ser **criada**; as existentes migram antes da superacao (DP-04). |
| RM-08 | Mudar o tipo de uma relacao existente e mudanca **C2**, com levantamento de dependentes (DP-02). |

## 7. Lifecycle Model

### 7.1 Estados oficiais

Os oito estados de [FND-03 §5](03-taxonomia.md) valem para **toda** entidade e nao sao
redefinidos aqui: `rascunho` · `em-revisao` · `aprovado` · `ativo` · `depreciado` ·
`superado` · `revogado` · `arquivado`.

> **O grafo de transicoes permitidas e proibidas vive em [FND-03 §5.1](03-taxonomia.md), fonte
> unica.** Este documento nao o reproduz (PJ-01, ADR-0008). O que e proprio do Meta Model sao
> os **perfis** de §7.2, que restringem esse grafo sem nunca amplia-lo.

*Correcao aplicada por [ADR-0008](../decisions/ADR-0008-uma-fonte-multiplas-projecoes.md),
fechando a ressalva **R2** de [FIT-2026-001](../governance/fitness/FIT-2026-001-meta-model.md):
o grafo estava reproduzido aqui e em FND-03 §5.1 — segunda fonte de verdade. Nenhuma norma
mudou; mudou onde ela e lida.*

### 7.2 Perfis de ciclo de vida

Toda entidade segue exatamente um perfil — **com uma excecao declarada: `MEM`**, cujo perfil e
determinado pela **camada**: a camada OPR segue **P3**, e as camadas EST, PRD, TEC e APR seguem
**P1**. Nao ha outra entidade com mais de um perfil. O perfil restringe o grafo de §7.1; nunca
o amplia.

*Excecao explicitada em 2026-07-28: a tabela abaixo sempre alocou `MEM` a dois perfis, e a
frase de abertura afirmava perfil unico para toda entidade. Contradicao interna entre regra e
tabela, corrigida em favor da tabela — a alocacao por camada e a intencao vigente desde
FND-06 §3. Achado **C3** da [revisao arquitetural da consolidacao](revisao-arquitetural-consolidacao-2026-07-28.md).*

| Perfil | Quem | Comportamento | Restricao propria |
|---|---|---|---|
| **P0 — Permanente** | ORG, SOBERANO | Nao tem estado documental | Nao nasce nem se aposenta por decisao interna |
| **P1 — Normativo** | FND, CAP, DEP, AGT, SUB, SKL, WFL, TOL, TPL, PRO, PRJ, SPC, MEM (EST/PRD/TEC/APR) | Grafo completo de §7.1 | Entrada em `ativo` exige Carta aprovada e vinculo valido a Capability, quando Componente |
| **P2 — Instrumento** | ADR, RFC, EXC, INC, FIT | Ato datado, com desfecho | **`aprovado` e terminal quanto ao conteudo**: o texto nunca muda (LV-04). Muda apenas o estado e os campos de sucessao |
| **P3 — Efemero** | MSG, MEM da camada OPR | **Expirar e o comportamento padrao** | `ttl` obrigatorio; sobreviver ao ciclo exige promocao explicita ou renovacao justificada |

### 7.3 Eixos ortogonais de estado

`status` descreve o estado do **documento**. Algumas entidades tem, adicionalmente, um eixo
que descreve o estado da **coisa** — independente e simultaneo, nunca substituto.

> **Declaracao de projecao (PJ-02, [ADR-0008](../decisions/ADR-0008-uma-fonte-multiplas-projecoes.md)).**
> **Fonte:** a coluna **Autoridade** de cada linha — FND-08 §3.3, FND-01 §7.2, FND-04 §9,
> FND-04 §10.2, §10.4 deste documento e FND-06 §6.
> **Campos projetados:** apenas a lista de **valores** de cada eixo.
> **Finalidade:** mostrar que os eixos sao ortogonais ao `status` exige ve-los; um indice de
> ponteiros nao demonstra ortogonalidade.
> **Metodo de atualizacao:** pela mesma mudanca que altera a fonte do eixo (CV-04).
> Divergencia e defeito desta tabela (PJ-03). *Reproducao identificada pelo teste preventivo
> de PJ-05 na Missao 1.4 e convertida em projecao declarada — primeiro caso barrado pelo
> instrumento novo.*

| Entidade | Eixo | Valores | Autoridade |
|---|---|---|---|
| CAP | `maturidade` | `proposta` · `experimental` · `emergente` · `estabelecida` · `madura` · `em-depreciacao` · `aposentada` | FND-08 §3.3 |
| DEP, AGT, SUB | `nivel_autonomia` | `A0` · `A1` · `A2` · `A3` | FND-01 §7.2 |
| EXC | `vigencia` | `vigente` · `expirada` · `regularizada` | FND-04 §9 |
| INC | `situacao` | `aberto` · `contido` · `corrigido` · `fechado` | FND-04 §10.2 |
| FIT | `veredito` | `apto` · `apto-com-ressalva` · `inapto` | §10.4 |
| MEM | `confianca` | `alta` · `media` · `baixa` | FND-06 §6 |

> **Exemplo legitimo de combinacao:** `status: ativo` com `maturidade: experimental` — o
> documento vigora, a competencia ainda esta sendo aprendida. Nao e contradicao (FND-08
> §3.4). O mesmo vale para `status: ativo` com `situacao: aberto` em um incidente.

### 7.4 Regras de transicao

| # | Regra |
|---|---|
| LC-01 | Toda transicao e **ato registrado**, com responsavel e data. Transicao silenciosa e nula (GV-01). |
| LC-02 | Quem produziu o artefato nao pode transiciona-lo de `em-revisao` para `aprovado` (PI-05, LV-03). |
| LC-03 | Entrada de Componente em `ativo` exige Carta aprovada **e** vinculo valido a Capability (PI-12, VC-01). |
| LC-04 | Instrumento em `aprovado` tem conteudo imutavel. Corrigir e **superar**, nunca editar (LV-04). |
| LC-05 | `depreciado → superado` exige que **todos** os dependentes ja tenham migrado (FND-04 §7.2). |
| LC-06 | Aposentar entidade contida obriga destino explicito de cada filho e de cada relacao (RM-03, IV-07). |
| LC-07 | Registro P3 que sobrevive ao ciclo sem promocao **expira**, e essa presuncao e desejada (FND-06 §3.4). |
| LC-08 | Eixo ortogonal (§7.3) nunca substitui `status`: os dois sao declarados sempre que ambos existirem. |
| LC-09 | Maturidade, vigencia, situacao e veredito declarados sem evidencia medida sao devolvidos por DEP-QAR (CL-06, DoD-5). |
| LC-10 | Remocao fisica de arquivo que ja esteve em `ativo` e **proibida** (FND-04 §7.2, PI-07). |

### 7.5 Ciclo de vida por evento organizacional

| Evento | Estado resultante | Instrumento |
|---|---|---|
| Entidade proposta | `rascunho` | RFC ou Carta em elaboracao |
| Submetida a revisao independente | `em-revisao` | Parecer de DEP-QAR / DEP-GOV |
| Aceita | `aprovado` | ADR |
| Entra em vigor | `ativo` | Publicacao + atualizacao de indice |
| Substituicao ja decidida | `depreciado` | ADR que anuncia a sucessao |
| Substituida | `superado` | ADR sucessor + `substituido_por` |
| Anulada sem substituto | `revogado` | ADR de revogacao com declaracao do que passa a valer |
| Encerrada sem ter vigorado | `arquivado` | RFC rejeitada, rascunho descartado |

## 8. Authority Model

### 8.1 Os cinco verbos de autoridade

| Verbo | Significa | Regra invariante |
|---|---|---|
| **Criar** | Fazer a entidade passar a existir | Exige instrumento da classe e Carta quando Componente (PI-12) |
| **Alterar** | Mudar conteudo, escopo ou relacoes | Segue a classe do **efeito**, nao do tamanho do texto (AL-01) |
| **Aprovar** | Autorizar a existencia ou a mudanca | **Nunca** por quem propos ou executou (PI-05, LV-03) |
| **Consumir** | Usar, invocar, referenciar, depender | Nao concede autoridade sobre o consumido (MT-09) |
| **Aposentar** | Encerrar a existencia | Exige destino explicito de cada responsabilidade, filho e relacao |

### 8.2 Matriz de autoridade por entidade

Derivada de FND-01 §7.3, FND-04 §2 e §6, e FND-08 §6.3 — **sem redefini-las**. Conflito
entre esta tabela e o documento de origem resolve-se a favor do documento de origem, e o
conflito e registrado como erro deste documento.

**Registro de conflito — linha `SPC`.** A coluna *Aprova* declarava **`DEP-PRD (QG-1)`** e a
coluna *Ratifica* declarava **`—`**, o que **contradizia FND-04 §2** para Spec de classe
**C2** ou **C3**. O conflito e **registrado como erro desta tabela**, na forma que o paragrafo
acima exige, e as duas celulas passam a **remeter a classe** em vez de fixar titular. **Aprovar
o artefato e liberar o portao sao atos distintos** (FND-01 §6.2): `QG-1` e liberado por
**DEP-EXE** e **nao consta desta tabela**. **A classe de uma Spec e a do seu efeito** (AL-01),
com **C1 como piso** (FND-04 §6, linha *Spec*); na duvida prevalece a classificacao mais
restritiva (FND-01 §7.1). **Nenhum titular foi ampliado:** todos os nomes ja constavam de
FND-04 §2.

| Entidade | Propoe / cria | Revisa | Aprova | Ratifica | Aposenta |
|---|---|---|---|---|---|
| ORG | — | — | — | SOBERANO | — |
| SOBERANO | — | — | — | — | — |
| FND | DEP-GOV | DEP-QAR | SOBERANO | **SOBERANO** | SOBERANO |
| ADR | qualquer DEP | revisor independente + DEP-QAR | conforme classe (FND-07 §2.4) | SOBERANO se C3 ou Tipo 1 | nunca — e superado |
| RFC | qualquer DEP | areas afetadas | DEP-GOV valida forma | — | proponente, com registro |
| EXC | quem precisa | DEP-GOV | **SOBERANO** | **SOBERANO** | expira sozinha |
| INC | quem detecta (**obrigatorio**) | DEP-GOV | DEP-GOV registra | — | DEP-QAR fecha |
| FIT | DEP-QAR | DEP-GOV (forma) | DEP-EXE | **—** *(`FT-10`)* | nao se aposenta — e historico |
| CAP | custodio ou qualquer DEP | DEP-GOV + DEP-QAR | SOBERANO | **SOBERANO** | **SOBERANO** |
| DEP | DEP-EXE | DEP-GOV | SOBERANO | **SOBERANO** | SOBERANO |
| AGT | DEP de origem | DEP-GOV + DEP-QAR | DEP-EXE | SOBERANO se Tipo 1 | DEP de origem, com ADR |
| SUB | agente pai | DEP-GOV | DEP-EXE | — | agente pai; compulsorio se o pai for aposentado |
| SKL | qualquer DEP | DEP-GOV + DEP-QAR | DEP-EXE | — | proprietario, com ADR |
| WFL | DEP dono do resultado | DEP-QAR | DEP-EXE | — | DEP dono, com ADR |
| TOL | DEP-TLS | DEP-QAR + DEP-ENG | DEP-EXE | **SOBERANO** (Tipo 1) | DEP-TLS, por criterio declarado |
| TPL | DEP-GOV + dono do tipo | DEP-GOV | DEP-GOV | — | DEP-GOV |
| PRO | DEP-PRD | DEP-QAR | SOBERANO | **SOBERANO** | **SOBERANO** |
| PRJ | DEP-EXE | DEP-GOV | DEP-EXE | SOBERANO se Tipo 1 | DEP-EXE, ao atingir criterio de encerramento |
| SPC | DEP-PRD | DEP-ENG + DEP-QAR | conforme classe (FND-04 §2); em **C1**, **DEP-EXE** | SOBERANO se C3 ou Tipo 1 | DEP-PRD |
| MEM | qualquer DEP | DEP-KMS | DEP-KMS; **DEP-GOV se camada EST** | SOBERANO se EST | DEP-KMS, por TTL ou refutacao |
| MSG | qualquer ATOR | destinatario | destinatario (aceite) | — | expira por TTL |

> **Sobre a linha `FIT`.** `Fitness Check` e `Revisao Arquitetural` sao **pareceres**, nao
> artefatos de decisao, e **nao se ratificam** — regra **`FT-10`** de
> [ADR-0015](../decisions/ADR-0015-fitness-check-e-parecer-nao-decisao.md). A ratificacao
> incide sobre **a mudanca avaliada**, nunca sobre o parecer que a avalia (`FT-11`). O efeito
> do veredito `inapto` e **processual** e independe de ato do Soberano (`FT-14`). **Nenhum
> titular foi ampliado por esta alteracao: uma materia saiu da mesa do ratificador, e nenhuma
> entrou.**

> **Sobre a linha `SPC`, coluna *Aprova*, em `C1`.** Esta celula **nao redefine FND-04 §2**:
> ela **aplica FND-04 §3.1** ao unico caso em que a propria matriz torna o default de §2
> impossivel. Para `SPC`, esta tabela poe **DEP-PRD** como quem **propoe/cria** e como quem
> **aposenta** — logo, proprietario —, e `FND-04 §2` atribui a aprovacao `C1` ao
> **proprietario**. As duas leituras juntas produzem `Proponente = Aprovador`, que
> `FND-04 §3.1` declara **nula** por **`LV-03`**, Linha Vermelha de `FND-01`, **nivel 1** da
> hierarquia normativa. **Entre um default de §2 e uma incompatibilidade absoluta de §3.1,
> prevalece a incompatibilidade** — e o aprovador passa a ser o titular que `FND-04 §2` ja
> nomeia no degrau seguinte: **DEP-EXE**. **Nenhum titular foi ampliado:** `DEP-EXE` ja
> aprova `Spec` `C2` na mesma linha desta tabela. **A classe NAO muda:** `C1` continua `C1`,
> com **Nota de Decisao** como instrumento (`FND-04 §2`, `FND-07 §2.3`), **sem** `RFC`,
> **sem** `ADR`, **sem** `FIT` e **sem** ratificacao. **`C0` NAO e alcancado por esta emenda,
> e o colapso de `C0` permanece declarado** em `RD-91`.

### 8.3 Regras de autoridade

| # | Regra |
|---|---|
| AU-01 | **Nenhuma entidade cria entidade de estrato inferior em numero ao seu.** Agente (3) nao cria Departamento (3, mas por AU-02), nao cria Capability (2) nem Norma (1). |
| AU-02 | Criacao no **mesmo estrato** exige aprovacao no estrato imediatamente superior em autoridade: departamento novo e aprovado pelo Soberano, nao por outro departamento. |
| AU-03 | Ator nunca amplia a propria autoridade, escopo ou permissao (LV-07). |
| AU-04 | Ator nunca opera acima do `nivel_autonomia_concedido` na mensagem, ainda que a Carta permita mais (AG-02). |
| AU-05 | Toda decisao **Tipo 1** exige ratificacao humana explicita, qualquer que seja a classe. Nao ha delegacao que remova a exigencia (PI-06). |
| AU-06 | Instrumento **autoriza**; nao executa. O ADR permite criar o componente; quem o cria e o executor nomeado. |
| AU-07 | Veto de Guarda so cai por decisao registrada do Soberano (LV-09). |
| AU-08 | Consumir nao da autoridade: quem usa uma Skill nao a altera; quem depende de uma Capability nao a governa. |
| AU-09 | Autoridade nao declarada em §8.2 **nao existe** (MT-09). Na duvida, escala-se (EC-01). |
| AU-10 | A cadeia de autoridade termina sempre no Soberano (IV-05). Nenhuma cadeia nova pode ser criada. |

### 8.4 Autoridade sobre o proprio Meta Model

| Materia | Propoe | Aprova | Ratifica | Classe |
|---|---|---|---|---|
| Criar entidade nova | qualquer DEP | DEP-EXE + parecer DEP-GOV | **SOBERANO** | **C3** |
| Criar arquetipo novo | DEP-GOV | DEP-EXE | **SOBERANO** | **C3** |
| Criar relacao nova | qualquer DEP | DEP-EXE | SOBERANO | **C3** |
| Acrescentar par permitido a relacao existente | qualquer DEP | DEP-EXE + DEP-GOV | — | C2 |
| Acrescentar atributo minimo a entidade | dono da entidade | DEP-GOV | — | C2 |
| Acrescentar classe ou valor a eixo existente | dono da entidade | DEP-GOV | — | C2 |
| Remover entidade, arquetipo ou relacao | DEP-GOV | SOBERANO | **SOBERANO** | **C3** |
| Correcao editorial | DEP-GOV | DEP-GOV | — | C0 |

## 9. Dependency Rules

### 9.1 Direcao permitida

> **Regra-mae (PD-11):** dependencia dura aponta para o **mesmo estrato ou para estrato de
> numero menor**. Nunca para cima.

| De → Para | Permitido? | Racional |
|---|---|---|
| Execucao (4) → Competencia (2) | Sim | Skill materializa competencia |
| Valor (5) → Execucao (4) | Sim | Produto usa ferramenta e workflow |
| Cognitivo (6) → qualquer | Sim | Memoria registra tudo |
| Estrutural (3) → Normativo (1) | Sim | Departamento obedece a norma |
| Competencia (2) → Estrutural (3) | **Nao** | Quebraria TC-1, TC-2 e CI-01: competencia deixaria de sobreviver a reorganizacao |
| Normativo (1) → qualquer estrato maior | **Nao** | Norma que depende de quem a executa deixa de ser norma |
| Raiz (0) → qualquer | **Nao** | A organizacao nao depende de suas partes |

### 9.2 Dependencias proibidas

| # | Proibicao | Norma de origem | Consequencia se detectada |
|---|---|---|---|
| PD-01 | Ciclo em `depende-de`, em qualquer estrato | DP-03, RL-01 | RFC obrigatoria para desfazer |
| PD-02 | Norma (FND, ADR) depender de Componente | FND-01 §10 | Inversao de hierarquia — nulo |
| PD-03 | Capability depender de Departamento, Agente, Ferramenta ou Produto | CI-01, TC-1, TC-2 | Carta devolvida por DEP-GOV |
| PD-04 | Verificador depender do verificado | RL-05, PI-05, ES-02 | Elo removido; independencia da Guarda restaurada |
| PD-05 | Subagente depender de outro Subagente, ou ter filho | IV-04 | Componente vetado |
| PD-06 | Criar dependencia sobre entidade `depreciada`, `superada` ou `revogada` | DP-04 | Elo quebrado; bloqueia aprovacao |
| PD-07 | Dependencia dura em Ferramenta externa sem alternativa avaliada e criterio de descarte | DP-05 | Adocao vetada por DEP-QAR |
| PD-08 | Norma ou decisao depender de registro de Memoria | MM-07 | Memoria informa, nao obriga — elo invalido |
| PD-09 | Instrumento depender de instrumento ainda inexistente ou futuro | GV-06 | Registro invalido |
| PD-10 | Produto depender duramente de outro Produto sem ADR | — | Acoplamento de portfolio nao registrado |
| PD-11 | Depender de entidade de estrato de numero maior | §9.1 | Inversao estrutural — nulo |
| PD-12 | Agente depender diretamente de agente de outro departamento | CN-01, AG-04 | Deve passar por Handoff formal ou escalar a DEP-EXE |

### 9.3 Deteccao

| Verificacao | Quando | Executa |
|---|---|---|
| Ciclo em `depende-de` | A cada mudanca C2/C3 e no fechamento de ciclo | DEP-GOV (integridade referencial) |
| Dependencia ascendente (PD-11) | A cada aprovacao de Carta | DEP-GOV |
| Verificador dependente do verificado | A cada mudanca em dominio `GAR` | DEP-QAR |
| Dependencia em entidade nao vigente | Auditoria de integridade referencial | DEP-GOV |
| Dependencia externa sem descarte declarado | QG-4 | DEP-QAR |

### 9.4 Responsabilidade nao e dependencia

Quatro vinculos ligam entidades de estrato alto a entidades de estrato baixo e **nao** sao
dependencia: **custodia**, **autoria**, **execucao** e **ratificacao**. Tratados como
dependencia, todos violariam PD-11 e inverteriam a arquitetura.

| Vinculo | Exemplo | Por que nao e dependencia |
|---|---|---|
| `custodia` | DEP (3) custodia CAP (2) | O custodio troca por ADR sem que uma linha da Carta mude (OW-06, IV-07). Capability sem custodio nao deixa de ser verdadeira: fica **nula para vinculacao** (OW-03) — defeito de governanca, nao de competencia |
| autoria | DEP-GOV (3) escreve ADR (1) | O ADR continua vigente se o departamento autor for extinto. Autoria e proveniencia, nao sustentacao |
| execucao | DEP-QAR (3) executa FIT (1) | O veredito emitido nao deixa de valer se o executor mudar. Quem executa e atributo de rastreabilidade |
| ratificacao | SOBERANO (0) ratifica ADR (1) | Ato datado que confere eficacia, nao elo permanente |

**Criterio geral:** `depende-de` significa que a origem **deixa de operar** sem o destino.
Se o destino desaparecer e a origem continuar valendo, o vinculo e de responsabilidade — e
pertence a §8, nao ao grafo de dependencia.

O mesmo raciocinio, em sentido inverso, vale para `exerce`: o componente depende da
Capability para ser **valido**, mas a Capability nao depende de nenhum componente para
**existir**.

## 10. Architecture Fitness Check

> Mecanismo determinado pelo Soberano em 2026-07-28 e adotado por
> [ADR-0004](../decisions/ADR-0004-adocao-do-architecture-fitness-check.md).

### 10.1 Por que existe

O Architecture Review pergunta **"esta correto?"**: ha duplicacao, sobreposicao, ciclo,
lacuna, dependencia proibida. E uma verificacao de **corretude estrutural**, e o sistema ja
a exigia ao fim de cada mudanca estrutural.

Nenhum portao existente pergunta **"ficou melhor de evoluir?"**. Uma arquitetura pode passar
em todos os testes de corretude e ainda assim degradar: cada mudanca correta acrescenta um
conceito, uma abstracao, um documento a ler — e a soma de mudancas individualmente
defensaveis produz um sistema que ninguem consegue mais mudar barato.

**Fitness Check e a verificacao de aptidao evolutiva.** Ele mede a derivada, nao o estado.

| | Architecture Review | Architecture Fitness Check |
|---|---|---|
| Pergunta | Esta correto? | Ficou mais apto a evoluir? |
| Mede | Estado | Variacao entre antes e depois |
| Falha tipica que detecta | Duplicacao, ciclo, orfao, lacuna | Complexidade sem ganho, abstracao ociosa, custo de contexto crescente |
| Veredito | Achados com severidade | `apto` · `apto-com-ressalva` · `inapto` |
| Bloqueia? | Achado alto bloqueia | `inapto` bloqueia o encerramento |

Os dois sao **obrigatorios e complementares** em C2 e C3. Um nao substitui o outro (FT-01).

### 10.2 Quando e obrigatorio

| Situacao | Fitness Check |
|---|---|
| Mudanca **C3** (constitucional) | **Obrigatorio**, com ratificacao do Soberano |
| Mudanca **C2** (estrutural) | **Obrigatorio** |
| Encerramento de trabalho que produza ou altere artefato da Fundacao, do catalogo de Capabilities ou do Meta Model | **Obrigatorio** |
| Revisao estrutural periodica (FND-02 §9.4) | **Obrigatorio** |
| Mudanca **C1** | Opcional; recomendado em lote ao fim do ciclo |
| Mudanca **C0** | Nao se aplica |

> **Sobre "Missao".** O que o Soberano chama de Missao corresponde, no vocabulario oficial,
> a uma mudanca C2 ou C3 — e, quando tem prazo e alocacao proprios, a um Projeto. Nao e um
> tipo de entidade (X-13). A regra "toda Missao encerra com Fitness Check" e integralmente
> satisfeita pela primeira linha desta tabela.

### 10.3 As seis perguntas

Cada resposta exige **sinal observavel**. Resposta sem sinal e opiniao e a verificacao e
devolvida (FT-03, DoD-5).

| # | Pergunta | Sinal observavel exigido | Interpretacao adversa |
|---|---|---|---|
| **F1** | A complexidade aumentou sem ganho proporcional? | Entidades, regras e artefatos **acrescentados** contra responsabilidades orfas **resolvidas** e regras **removidas ou unificadas** | Acrescimo liquido sem problema nomeado que ele resolva |
| **F2** | Algum conceito foi duplicado? | Varredura de conceitos redefinidos: mesmo conceito com duas definicoes, ou definicao recolada em vez de referenciada (MM-01, LX-07) | Qualquer definicao repetida, mesmo que consistente |
| **F3** | Alguma abstracao ficou desnecessaria? | Arquetipos, classes e eixos introduzidos com **menos de dois membros** ou sem consumidor declarado (AQ-03, RL-06) | Abstracao criada para simetria ou antecipacao |
| **F4** | O sistema continua mais simples de evoluir do que antes? | Numero de documentos que uma mudanca-tipo passa a exigir; numero de aprovacoes no caminho critico | Custo de mudanca crescente sem ganho de seguranca correspondente |
| **F5** | A mudanca reduz ou aumenta o custo de contexto? | Volume de material que um papel precisa carregar para executar corretamente (metrica "Contexto por papel", FND-01 §6.3; FND-06 §9.1) | Contexto crescente e sinal direto de violacao de PI-14 |
| **F6** | Ela favorece reutilizacao? | Definicoes reutilizaveis por Framework futuro contra definicoes especificas do caso; DoD-8 | Solucao que serve apenas a ocorrencia atual |

### 10.4 Veredito e efeito

| Veredito | Quando | Efeito |
|---|---|---|
| `apto` | Nenhuma das seis perguntas revela degradacao | Mudanca pode encerrar |
| `apto-com-ressalva` | Degradacao aceita conscientemente, com **dono e gatilho** declarados | Encerra; a ressalva vira divida declarada, com data de reavaliacao |
| `inapto` | Degradacao sem ganho compensatorio, ou ressalva sem dono | **Bloqueia o encerramento.** A mudanca retorna a etapa [2] do ciclo de FND-04 §4 |

### 10.5 Papeis

| Papel | Quem | Regra |
|---|---|---|
| Executa | **DEP-QAR** | Nunca quem produziu o artefato avaliado (PI-05, LV-03) |
| Verifica a forma | DEP-GOV | Sinal observavel presente em todas as seis respostas |
| Fornece evidencia | DEP-KMS | Metricas de contexto e de reuso a partir da memoria |
| Aprova | DEP-EXE | — |
| Ratifica | **SOBERANO** | Obrigatorio quando o objeto avaliado for C3 |

### 10.6 Regras do Fitness Check

| # | Regra |
|---|---|
| FT-01 | Nao substitui o Architecture Review. Em C2 e C3, **ambos** sao obrigatorios. |
| FT-02 | Executor ≠ produtor do artefato avaliado. Acumulo torna o veredito nulo (LV-03). |
| FT-03 | Resposta sem sinal observavel e devolvida sem analise de merito. |
| FT-04 | **Tres vereditos `apto` sem uma unica ressalva, em sequencia, sao sinal de complacencia** e escalam ao Soberano — simetrico exato de FND-02 §9.4 e de "taxa de reprovacao zero e alerta" (FND-01 §6.3). |
| FT-05 | `inapto` bloqueia o encerramento. Prosseguir apesar do veredito exige excecao formal do Soberano (FND-01 §8.3). |
| FT-06 | Ressalva sem dono e sem gatilho e invalida: vira `inapto`. |
| FT-07 | Fitness Check que revela causa gera registro obrigatorio na camada APR (QG-5). |
| FT-08 | O proprio Meta Model e objeto de Fitness Check: toda mudanca em FND-09 exige FIT com ratificacao do Soberano (MT-12). |
| FT-09 | O FIT e artefato permanente. Nao se apaga, nao se reescreve: um veredito posterior **supera** o anterior (R-08). |

### 10.7 Portao QG-6

O Fitness Check materializa-se como o portao **QG-6 — Aptidao Arquitetural**, acrescentado
a FND-01 §6.2 por ADR-0004:

| Portao | Momento | Pergunta que responde | Quem libera |
|---|---|---|---|
| QG-6 | Ao encerrar mudanca C2 ou C3 | A arquitetura ficou mais apta a evoluir do que estava? | DEP-QAR + DEP-GOV |

Vale a regra geral de portao: **nao pode ser liberado por quem produziu o artefato**, e
portao pulado exige excecao formal registrada, nunca omissao.

## 11. Evolution Rules

### 11.1 Como uma entidade nova entra

#### Teste de Entidade (TE)

Uma candidata so vira entidade se **todas** as respostas forem afirmativas. Uma unica
negativa encerra a analise e indica onde a candidata realmente pertence.

| # | Pergunta | Se "nao" |
|---|---|---|
| TE-1 | Responde a uma pergunta que **nenhuma** entidade existente responde? | E duplicata (MT-02) — reusar a existente |
| TE-2 | Persiste alem do ato que a criou, com identidade propria? | E evento ou estado — vira MSG, MEM ou eixo de §7.3 |
| TE-3 | Tem dono unico e ciclo de vida proprios? | E **atributo** de outra entidade |
| TE-4 | Pode ser instanciada mais de uma vez, com o mesmo formato? | E instancia singular, nao tipo |
| TE-5 | Tem ao menos uma relacao valida de §6.1 com entidade existente? | E ilha — nao pertence ao universo |
| TE-6 | Continua fazendo sentido se todas as instancias atuais desaparecerem? | E descricao de caso concreto, nao tipo |
| TE-7 | Ha **sinal ja observado** que a justifica (PI-14, FND-04 §6.2)? | E antecipacao — recusada (FND-08 §7.1) |

#### Rito

```
 [1] LACUNA        um Framework, componente ou trabalho nao cabe em nenhuma entidade
        |
 [2] TESTE TE      TE-1 a TE-7; falha em qualquer um encerra e realoca a candidata
        |
 [3] RFC           classe C3; declara estrato, arquetipos, atributos minimos,
        |          relacoes permitidas, perfil de ciclo de vida, autoridade
        |
 [4] IMPACTO       instancias existentes afetadas; relacoes a acrescentar;
        |          templates a criar (FND-03 §3.9); documentos a emendar
        |
 [5] REVISAO       DEP-QAR (sobreposicao, amplitude) + DEP-GOV (conformidade)   <-- veto
        |
 [6] ADR           ratificado pelo SOBERANO (C3, Tipo 1)
        |
 [7] EMENDA        FND-09 nova versao MAIOR; FND-03 recebe prefixo, local e template
        |
 [8] FITNESS       QG-6 obrigatorio; `inapto` reabre em [2]
        |
 [9] MEMORIA       registro em EST (QG-5)
```

**Regra dura:** entidade que aparecer em uso sem percorrer este rito e **nula** (MT-01,
GV-01), e seu uso e incidente de conformidade.

### 11.2 Gradacao de instrumento

Nem toda necessidade nova exige entidade nova. A escada abaixo obriga a subir apenas o
degrau que o ganho justifica — simetrica a escada de especializacao de FND-02 §9.1.

```
  degrau 4  ENTIDADE NOVA        tipo proprio, com ID, ciclo de vida e autoridade   C3
     ^
  degrau 3  ARQUETIPO NOVO       regra transversal a varias entidades               C3
     ^
  degrau 2  RELACAO NOVA         forma de ligacao ainda inexistente                 C3
     ^
  degrau 1  CLASSE / EIXO NOVO   valor novo em eixo de entidade existente           C2
     ^
  degrau 0  ATRIBUTO NOVO        campo em entidade existente                        C1/C2
```

Antes de propor qualquer degrau, respondem-se as quatro perguntas de nao-proliferacao
(FND-04 §6.1). Proposta que nao as responde e devolvida sem analise de merito.

### 11.3 Como uma entidade muda

| Mudanca | Classe | Compatibilidade | Exigencia |
|---|---|---|---|
| Acrescentar atributo **opcional** | C1 | Retrocompativel | Registro |
| Acrescentar atributo **obrigatorio** | C2 | **Quebra** instancias existentes | Valor padrao declarado **ou** janela de migracao com prazo (EV-02) |
| Acrescentar par permitido a relacao | C2 | Retrocompativel | Declaracao bilateral (RM-01) |
| Remover par permitido | C3 | **Quebra** | Migracao de todas as relacoes existentes antes da vigencia |
| Acrescentar valor a eixo ortogonal | C2 | Retrocompativel | Criterio de transicao declarado (§7.3) |
| Acrescentar dominio de Capability | **C3** | — | Regra propria de FND-08 §10, preservada |
| Mudar estrato de uma entidade | **C3** | **Quebra** | Reverificacao de todas as dependencias (§9.1) |
| Renomear entidade | **Proibido** | — | ID e imutavel (LX-08); muda-se o titulo, nunca o ID |
| Remover entidade | **C3** | **Quebra** | Destino explicito de cada instancia e de cada relacao (EV-06) |
| Fundir duas entidades | **C3** | **Quebra** | Entidade nova com ID novo; as anteriores viram `superado` (EV-05) |

### 11.4 Regras de compatibilidade

| # | Regra |
|---|---|
| EV-01 | **Entidade ou atributo novo nunca invalida instancia ja aprovada.** Se invalidaria, nao e evolucao: e remocao seguida de criacao, com o rito de ambas. |
| EV-02 | Atributo obrigatorio novo vem com valor padrao declarado **ou** janela de migracao com prazo e dono. Janela vencida vira incidente. |
| EV-03 | Mudanca no Meta Model **nao tem efeito retroativo** sobre decisao ja tomada, salvo declaracao expressa (herda FND-01 §9). |
| EV-04 | Especializacao de entidade tem **profundidade maxima 1** (herda IV-04, RL-04). |
| EV-05 | Fusao produz entidade nova, com ID novo; as fundidas viram `superado` e sao preservadas (herda FND-08 §7.3, MM-09). |
| EV-06 | Remocao exige destino explicito de **cada instancia e cada relacao**. Instancia orfa e tao proibida quanto responsabilidade orfa. |
| EV-07 | Toda mudanca no Meta Model passa por Architecture Review **e** QG-6 (MT-12, FT-08). |
| EV-08 | **Consolidacao e o movimento simetrico e igualmente obrigatorio.** Entidade sem instancia ao longo de um horizonte inteiro, ou arquetipo com um unico membro, obriga proposta de remocao ou fusao — ou registro fundamentado de manutencao (PI-14 regra 5). |
| EV-09 | Todo ADR que altera o Meta Model declara o ganho de PI-14 pretendido e a data em que ele sera reavaliado. Ganho nao confirmado abre proposta de consolidacao. |

### 11.5 Invariantes do Meta Model

Propriedades que **nenhuma evolucao pode quebrar**, nem por emenda que as ignore. Alterar
qualquer uma exige revoga-la explicitamente, com justificativa de por que a protecao deixou
de ser necessaria (FND-01 §9).

| # | Invariante | Herda de |
|---|---|---|
| MI-M01 | O universo de entidades e **fechado**: so existe o que §5 declara. | MT-01 |
| MI-M02 | Toda entidade tem **exatamente um dono**. | ES-01 |
| MI-M03 | Nao existe ciclo em dependencia dura, em nenhum estrato. | DP-03, RL-01 |
| MI-M04 | Profundidade de especializacao permanece **1**. | IV-04, RL-04 |
| MI-M05 | A cadeia de autoridade termina no **Soberano**. | PI-01, IV-05 |
| MI-M06 | Capability **nunca** depende de estrutura, ferramenta ou produto. | CI-01, TC-1 |
| MI-M07 | Verificador **nunca** depende do verificado. | PI-05, ES-02, RL-05 |
| MI-M08 | Todo Componente tem **Carta** e vinculo a ao menos uma **Capability**. | PI-12, FND-08 §8 |
| MI-M09 | Permanecem **exatamente cinco** camadas de memoria. | MI-01 |
| MI-M10 | Instrumento aprovado e **imutavel**: corrige-se superando. | LV-04 |
| MI-M11 | Dependencia dura **nunca aponta para estrato de numero maior**. | §9.1 |
| MI-M12 | Toda mudanca estrutural encerra com **Architecture Review e Fitness Check**. | MT-12, FT-01 |

## 12. Conformidade

| Verificacao | Quando | Executa | Falha resulta em |
|---|---|---|---|
| Entidade usada consta de §5 | QG-0 e a cada aprovacao | DEP-GOV | Entidade nula; uso e incidente de conformidade |
| Atributos minimos presentes | A cada portao | DEP-GOV | Artefato devolvido sem analise de merito |
| Relacao consta dos pares de §6.2 | A cada aprovacao de Carta | DEP-GOV | Relacao nula (RM-02) |
| Relacao declarada dos dois lados | Auditoria de integridade referencial | DEP-GOV | Elo quebrado; bloqueia aprovacao |
| Ausencia de ciclo em `depende-de` | Fechamento de ciclo e toda C2/C3 | DEP-GOV | RFC obrigatoria para desfazer |
| Ausencia de dependencia proibida (§9.2) | A cada aprovacao | DEP-GOV + DEP-QAR | Elo removido; incidente se ja vigorava |
| Perfil de ciclo de vida respeitado | A cada transicao | DEP-GOV | Estado revertido; incidente registrado |
| Autoridade conforme §8.2 | A cada aprovacao | DEP-GOV | Aprovacao **nula** (LV-03) |
| Fitness Check executado em C2/C3 | Ao encerrar a mudanca | DEP-QAR | Mudanca nao encerra (FT-05) |
| Entidade sem instancia por um horizonte | Revisao estrutural | DEP-EXE + DEP-QAR | Proposta de remocao ou registro de manutencao (EV-08) |

---

## Documentos relacionados

| Referencia | Relacao |
|---|---|
| [ADR-0003](../decisions/ADR-0003-adocao-do-enterprise-meta-model.md) | Decisao que adota este Meta Model |
| [ADR-0004](../decisions/ADR-0004-adocao-do-architecture-fitness-check.md) | Decisao que cria o Fitness Check, a entidade `FIT` e o portao QG-6 |
| [RFC-0002](../rfcs/RFC-0002-enterprise-meta-model.md) | Proposta de origem do Meta Model |
| [RFC-0003](../rfcs/RFC-0003-architecture-fitness-check.md) | Proposta de origem do Fitness Check |
| [FND-03](03-taxonomia.md) | Nomenclatura, identificadores, estados e localizacao dos tipos aqui declarados |
| [FND-04](04-governanca.md) | Classes de mudanca e pre-condicoes de criacao |
| [FND-08](08-capability-framework.md) | Relacoes entre Capabilities, incorporadas por referencia (§6.1) |
| [TPL-fitness-check](templates/TPL-fitness-check.md) | Template da verificacao de aptidao |
| [Revisao arquitetural do Meta Model](revisao-arquitetural-meta-model-2026-07-28.md) | Exame critico independente deste documento |

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-GOV | Meta Model inicial: 7 estratos, 4 arquetipos, 21 entidades, 13 recusas registradas, 10 relacoes, 4 perfis de ciclo de vida, matriz de autoridade, 12 dependencias proibidas, regras de evolucao e Architecture Fitness Check. Adotado por ADR-0003 e ADR-0004 — **ratificacao pendente**, ver INC-2026-001. |
| 1.1.0 | 2026-07-28 | DEP-QAR | Emenda C2 por ADR-0005: **RM-06b** proibe par reflexivo de `verifica`; §6.2 R-06 passa a excluir o artefato produzido pelo proprio DEP-GOV e nomeia DEP-QAR como revisor independente. Corrige o achado M1. |
| 1.2.0 | 2026-07-28 | DEP-GOV | Emenda C3 por ADR-0006: **E-08 ampliada** para dois tipos documentais (`FIT` aptidao, `REV` corretude), com vereditos preservados separados; §6.1.1 acrescida dos verbos `implementa`, `consome`, `valida`, `evidencia` e `substitui`; `restringe` declarado ato de autoridade, fora do grafo. **Ratificacao pendente.** |
| 1.3.0 | 2026-07-28 | DEP-QAR | Emenda C2 por **ADR-0008**: §7.1 deixa de reproduzir o grafo de transicoes de FND-03 §5.1 e passa a referencia-lo (PJ-01), fechando a ressalva **R2** de FIT-2026-001; §7.3 declara-se projecao dos eixos ortogonais (PJ-02); §7.2 explicita a excecao de `MEM`, unica entidade com perfil por camada — correcao de contradicao interna entre a regra e a propria tabela. Nenhuma norma alterada em conteudo. **Ratificacao de ADR-0003 e ADR-0006 registrada em INC-2026-001 §11** — campo `ratificacao` atualizado para `ratificada`. |
| 1.4.0 | 2026-07-29 | DEP-GOV | Emenda **C3** por **ADR-0017**, que fecha o achado **RD-09**: a linha `FIT` de **§8.2** deixa de declarar *"Ratifica: SOBERANO se C3"* e passa a **`—`**, alinhando a matriz a regra vigente **`FT-10`** de ADR-0015, e §8.2 recebe **uma nota normativa** que distingue o parecer da mudanca avaliada. **Uma celula e uma nota.** Nenhum titular foi ampliado, nenhum parecer virou norma, nenhum `FIT` historico foi editado (`FT-15`) e nenhuma outra linha da matriz foi tocada. |
| 1.5.0 | 2026-07-29 | DEP-GOV | Emenda **C3** por **ADR-0019**: **§8.2**, linha **`SPC`**, passa *Aprova* de `DEP-PRD (QG-1)` para **`conforme classe (FND-04 §2)`** e *Ratifica* de `—` para **`SOBERANO se C3 ou Tipo 1`**, alinhando a linha ao padrao ja usado pela linha `ADR`; a matriz recebe **uma nota** que **registra o conflito como erro desta tabela**, cumprindo a segunda metade da regra de precedencia do proprio §8.2. Fecha **RD-15**. Declara que **aprovar o artefato e liberar o portao sao atos distintos** e que a classe de uma Spec e a do **efeito** (AL-01), com **C1 como piso** (FND-04 §6). **Nenhum titular ampliado.** **Aplicada sobre a 1.4.0 de ADR-0017, na ordem declarada em PS-2026-008 §5.** |
| 1.6.0 | 2026-08-02 | DEP-GOV | Emenda **C3** por **ADR-0032**, que sana **`RD-91`** na fonte: **§8.2**, linha **`SPC`**, coluna *Aprova*, passa de `conforme classe (FND-04 §2)` para **`conforme classe (FND-04 §2); em C1, DEP-EXE`**, e §8.2 recebe **uma nota** que declara a derivacao. **Uma celula e uma nota.** O defeito era medido e nao lido: para `SPC`, esta tabela poe **DEP-PRD** como quem propoe/cria **e** como quem aposenta *(logo, proprietario)*, e `FND-04 §2` da a aprovacao `C1` ao **proprietario** — de modo que `Proponente = Aprovador`, que `FND-04 §3.1` torna **nula** por **`LV-03`**, Linha Vermelha de **nivel 1**. **Nao redefine `FND-04 §2`: aplica `FND-04 §3.1`**, e por isso a celula continua **derivada**, como o cabecalho de §8.2 e `FND-01 §10` exigem. **Nenhum titular ampliado** — `DEP-EXE` ja aprova `Spec` `C2` nesta mesma linha. **A classe nao muda:** `C1` segue `C1`, com **Nota de Decisao**, sem `RFC`, sem `ADR`, sem `FIT` e sem ratificacao — a segunda `Spec` volta a custar **2** instrumentos contra os **5** da primeira. **`0` entidades, tipos, relacoes, estados ou portoes tocados · `0` outras celulas de §8.2 alteradas · `0` bytes em `FND-04`.** **`C0 · T2` NAO e sanado** e segue declarado em `RD-91`; **as linhas `PRJ` e `TPL` de §8.2 tem o mesmo defeito, foram MEDIDAS nesta missao e NAO sao tocadas** — achados `RD-96` e `RD-97`, com dono e gatilho. **Nao vigora sem ato** (FND-01 §9; `LM-02`). |
