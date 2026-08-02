---
id: REV-INTERCLASSES-2026-07-28
titulo: Revisao arquitetural da validacao interclasses do Contrato de Carta de Departamento
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
classe_avaliacao: corretude
resumo: Examina a ativacao dos dois pilotos sob o ato soberano, a corretude das Cartas de Comando e Plataforma, e valida o contrato nas quatro classes por oito cenarios interclasses.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-GOV
ratificacao: nao-exigida
---

# REV-INTERCLASSES-2026-07-28

## Proposito
Examinar a **corretude estrutural** da ativacao de `DEP-QAR` e `DEP-ENG` sob o ato soberano de
2026-07-28, das duas Cartas novas — `DEP-EXE` *(Comando)* e `DEP-KMS` *(Plataforma)* — e
submeter o contrato de ADR-0011 a **oito cenarios interclasses** nas **quatro** classes.

## Escopo
| Item | Definicao |
|---|---|
| Inclui | [MSG-2026-0001](../memory/operacional/MSG-2026-0001-ato-soberano-ratificacao-cartas-piloto.md) · as **quatro** Cartas · `TPL-carta-departamento` 1.2.0 · os oito cenarios · a comparacao das quatro classes · o pacote de ratificacao · a reconciliacao de achados e ressalvas · a varredura C11 · a integridade referencial |
| **Nao** inclui | **Aptidao evolutiva** — objeto de [FIT-2026-006](../governance/fitness/FIT-2026-006-validacao-interclasses.md). As **cinco** Cartas restantes. Qualquer alteracao em Carta de Capability. O **merito** do ato soberano, que nao se revisa |
| Metodo | Confronto com FND-01 a FND-10 e ADR-0011; execucao dos oito cenarios usando **apenas** as quatro Cartas e as normas que elas citam; varredura de links relativos sobre **todos** os `.md`; varredura **C11** dos indices contra as fontes; medicao por `wc -l`, `sed`+`wc -l` e `sha256sum` |

## Responsaveis — validacao independente
> **Exigencia da missao:** o autor do contrato ou de uma Carta **nao pode, sozinho**, desenhar
> os testes, executar todos os cenarios e avaliar o resultado.

| Papel | Quem | Fundamento | Impedimento respeitado |
|---|---|---|---|
| **Proponente** dos dois novos pilotos | **DEP-EXE** | FND-09 §8.2, linha `DEP` — **unico** papel que pode propor | — |
| **Autor** das quatro Cartas e do contrato (ADR-0011) | **DEP-EXE** | Idem | **Nao desenha, nao executa e nao avalia** nenhum cenario |
| **Desenhista dos cenarios** | **DEP-QAR** | Nao e autor do contrato nem de nenhuma Carta | Nao desenhou CX-1 nem CX-3, em que e parte — §3.0 |
| **Executor dos cenarios** | **DEP-QAR**, exceto onde e objeto | FT-02, CV-08 | **CX-1 e CX-3 executados por DEP-GOV** |
| **Revisor independente** das Cartas | **DEP-GOV** | FND-09 §8.2, linha `DEP`: revisa | Nao e objeto de nenhuma Carta desta missao |
| **Verificador dos blocos impedidos** da Carta DEP-EXE | **DEP-QAR** | FND-09 §6.2, R-06 | §4.1 |
| **Verificador dos blocos impedidos** da Carta DEP-QAR *(ja ativa)* | **DEP-GOV** | REV-DEPARTAMENTO §4.1 — desvio ja aplicado | Inalterado |
| **Aprovador desta revisao** | **DEP-GOV** | **Desvio declarado** — §4.2 | DEP-EXE **impedido** (I-2): produziu dois dos objetos avaliados |
| **Autoridade decisoria** sobre as Cartas | **SOBERANO** | FND-09 §8.2; **DC-09** | Indelegavel |

> **Tres papeis distintos em tres etapas distintas.** Quem **propos e escreveu** (DEP-EXE) nao
> desenhou, nao executou e nao avaliou. Quem **desenhou e executou** (DEP-QAR) nao escreveu e
> nao aprova. Quem **aprova** (DEP-GOV) nao escreveu e nao executou. **A autoridade decisoria
> sobre o objeto (SOBERANO) nao participa de nenhuma das tres.**

---

## 0. Divergencias corrigidas durante esta revisao

| # | Divergencia | Correcao aplicada |
|---|---|---|
| **IC-1** | **A correcao M1 foi declarada aplicada e nunca chegou ao arquivo.** [REV-DEPARTAMENTO §3.7](revisao-arquitetural-cartas-de-departamento-2026-07-28.md) registra: *"Checklist do template passa a exigir a conferencia cruzada B4 × B9"*. O checklist de `TPL-carta-departamento` **1.1.0** nao continha nenhum item de conferencia cruzada — verificado por varredura do padrao `B4.*B9` em todo o acervo: **cinco ocorrencias, nenhuma no template** | Item acrescentado ao checklist; template a **1.2.0**. **Nao e decisao nova**: e mudanca de ADR-0011 sendo **completada** (CV-04, RG-03) |

> **IC-1 e da mesma familia de DR-8, e o alcance cresce de novo.** DR-8 era *licao declarada que
> nao chega ao registro-fonte*; IC-1 e **correcao declarada que nao chega ao artefato corrigido**.
> O mecanismo e identico — **declarar e propagar sao atos distintos, e so o primeiro deixa
> rastro no documento que declara**. A diferenca de objeto importa: uma licao nao propagada
> subconta ocorrencias; uma **correcao** nao propagada deixa o defeito **vivo** enquanto o
> registro afirma que ele foi corrigido. **Duas Cartas foram escritas sob um checklist que se
> acreditava corrigido e nao estava.**

## 1. Os entregaveis foram cumpridos?

| # | Entregavel exigido | Onde esta | Veredito |
|---|---|---|---|
| 1 | **Ativacao dos pilotos existentes** apos ato valido, sem editar atos historicos | [MSG-2026-0001](../memory/operacional/MSG-2026-0001-ato-soberano-ratificacao-cartas-piloto.md) §4 e §5; verificacao em §2 desta revisao | **Cumprido** |
| 2 | **Pilotos das classes faltantes**, pelo template vigente, em `em-revisao` | [`DEP-EXE`](../departments/exe/carta.md) *(Comando)* e [`DEP-KMS`](../departments/kms/carta.md) *(Plataforma)*; justificativa da amostra em §2.3 | **Cumprido** |
| 3 | **Validacao independente** com papeis segregados | Bloco Responsaveis desta revisao; §4 | **Cumprido** |
| 4 | **Cenarios interclasses** nos quatro pilotos | §3 — **oito** cenarios, com entrada, regra, saida, evidencia, falha e decisao | **Cumprido** |
| 5 | **Comparacao das quatro classes**, separando regra universal, especifica e diferenca acidental | §5 — **projecao unica**, nao duplicada em nenhum outro artefato | **Cumprido** |
| 6 | **Pacote de ratificacao** dos dois novos pilotos | §6 — informa; **nao produz nem registra ato soberano** | **Cumprido** |
| 7 | **Divida e consistencia** reconciliadas | §7 *(achados)* · §8 *(ressalvas)* · §9 *(C11)* · §10 *(catalogo-fonte)* | **Cumprido** |
| 8 | Correcao das duas regras de medicao | [FIT-2026-006 §Regras de medicao](../governance/fitness/FIT-2026-006-validacao-interclasses.md) — **um `FIT` emitido e M1 e nao se edita** | **Cumprido, no instrumento correto** |

### 1.1 O que a missao **nao** criou, e devia nao criar

| Nao criado | Verificacao |
|---|---|
| **As cinco Cartas restantes** | `departments/` tem **4** subdiretorios: `qar`, `eng`, `exe`, `kms` |
| Documento fundacional | `foundation/` continua com **10** documentos normativos |
| Entidade, tipo documental, camada de memoria | **21** · **33** · **5** — inalterados |
| Template novo | **19** templates; **um** emendado *(1.1.0 → 1.2.0)*, nenhum criado |
| Agente, subagente, skill, workflow, produto, projeto, ferramenta | **0** de cada |
| Codigo, banco, infraestrutura, migracao do Legacy | **0**; proveniencia permanece **100% `native`** |
| Departamento novo | **9** — os mesmos desde ADR-0001. As duas Cartas novas descrevem departamentos **que ja existiam** |
| **Ratificacao produzida pela missao** | **Nenhuma.** O unico ato e o do Soberano, **recebido** e registrado — nao inferido, nao presumido, nao declarado por esta missao |
| Aprovacao dos novos pilotos | **Nenhuma.** Ambos em `em-revisao`, `ratificacao: pendente` |

> **`LucaX Legacy` nao foi consultado nem importado**, e nenhum conhecimento do Fundador ainda
> nao ativo foi usado: `MEM-EST-0001` permanece `aprovado` e **nao vigente**, e nenhum dos seus
> quatro pacotes foi carregado nesta missao (ADR-0007 §5.1; CT-21).

## 2. Verificacao da ativacao dos dois pilotos

> **Esta secao verifica o cumprimento da condicao que o proprio ato impos**, e nao o merito do
> ato. O merito de um ato soberano nao se revisa (PI-01).

### 2.1 Autoridade, segregacao e custodia

| Verificacao | Metodo | Resultado |
|---|---|---|
| A aprovacao veio de quem a matriz exige? | FND-09 §8.2, linha `DEP`, coluna *Aprova* e *Ratifica* | **SOBERANO** nos dois campos. **Conforme** |
| Quem **registrou** a ratificacao e distinto de quem **executou** a mudanca? | LM-05, CV-09 | Registrou **DEP-GOV**; executou **DEP-EXE**. **Conforme** |
| Quem **verificou** e distinto de quem **produziu**? | FT-02, RM-06b | Verificaram **DEP-QAR** e **DEP-GOV**; produziu **DEP-EXE**. **Zero coincidencia** |
| O ato foi **explicito e datado sobre o texto final**? | LM-02, LM-03, LM-04 | **Sim** — texto transcrito em MSG-2026-0001 §1.1, data **2026-07-28**, objeto nominal |
| Houve **inferencia** de ratificacao em algum ponto? | LM-03, LM-04, LV-05 | **Nao.** O alcance esta em MSG-2026-0001 §3, com **cinco** exclusoes expressas |
| A **custodia** declarada nas duas Cartas confere com a fonte? | frontmatter das 23 Cartas `CAP` × §2 de cada Carta | **8 vinculos**, todos conformes. Nenhuma Carta de Capability alterada |
| Algum artefato historico foi editado? | `FIT-2026-005`, `REV-DEPARTAMENTO`, `INC-2026-001`, baselines `BL-01` e `BL-02` | **Nenhum.** Todos M1 ou preservados (MSG-2026-0001 §6) |

### 2.2 Inexistencia de alteracao entre a versao revisada e a ratificada

| Via | Evidencia | Resultado |
|---|---|---|
| **Conteudo** | `sha256sum` do texto submetido, medido **antes** de qualquer edicao desta missao | `DEP-QAR` `fa07f55f…f286` · `DEP-ENG` `57aebf81…1a48` |
| **Extensao** | Contagem de linhas × valor registrado no catalogo §4.3.1 ao encerramento da Missao 1.6 | **386 = 386** · **400 = 400** |
| **Acervo** | Impressao digital de `BL-2026-07-28-03` | **`541ed5b6…d6b1`** — reproduz exatamente |
| **Temporal** | `mtime` das Cartas × `mtime` do ultimo artefato da Missao 1.6 | **17:58:44** e **17:21:16** contra **17:59:12** — ambas anteriores |
| **Pos-transicao** | Diff aplicado | **2 campos de frontmatter por Carta; 0 linhas de corpo.** Contagem identica: 386 e 400 |

**Tres vias independentes convergem.** Nenhuma delas bastaria sozinha, e o limite de cada uma
esta declarado em MSG-2026-0001 §4.1 (PI-10, LV-12).

**Veredito da ativacao: CONFORME.** A condicao de eficacia que o ato impos esta satisfeita.

### 2.3 Justificativa da amostra dos dois novos pilotos

| Criterio | **DEP-EXE** *(Comando)* | **DEP-KMS** *(Plataforma)* |
|---|---|---|
| **Por que esta classe** | Classe **sem piloto**; limite declarado em **A2** de ADR-0011 §8 e em **R2**/**DR-5** | Idem; e a classe que o rollout de FIT-2026-005 **Condicao 2** manda exercer **antes** das demais |
| **Por que este departamento** | **Nao ha escolha:** DEP-EXE e o **unico** departamento de Comando (FND-02 §2.1) | **Escolha real entre DEP-KMS e DEP-TLS** — fundamentada abaixo |
| **Contraste** | **A3**, o unico nivel de autonomia mais alto do sistema; **nivel 1**, o unico acima de 2; **decide e arbitra**, nao veta nem entrega | **A2**, **nivel 2**; **serve todos e nao decide por ninguem** (ES-07) — o oposto exato do Comando na mesma tabela |
| **Risco** | O impedimento **mais dificil do contrato**: autor de **todas** as Cartas e objeto da propria (R2, DR-5). **Dispara VC-03** (4 > 3, achado P6) | Custodia `CAP-conhecimento`, **unica Capability de nivel 0** do grafo: falha nela propaga para as 22 demais. **Curador de cinco camadas, dono de uma** (P2) |
| **Cobertura** | Declara a custodia de `CAP-comunicacao` **exercida por outro** — lado **custodio** do unico membro de OW-02 | Declara `CAP-comunicacao` **exercida sem custodiar** — lado **exercente** do mesmo membro; **unica linha do acervo** |
| Sinal que a escolha expoe | Autoridade que **homologa** sem dar vigencia; coordenacao que **nao alcanca a Guarda**; aprovacao de `FIT` sobre objeto proprio | Autoridade que **mede** sem poder **agir** sobre o que mede; portao **QG-5**; a unica Carta com **quatro** papeis distintos e **zero** residuo de segregacao |

> **Por que DEP-KMS e nao DEP-TLS.** DEP-TLS custodia **uma** Capability (`CAP-integracao`), com
> `exercentes` **identico** ao `custodio` — o mesmo padrao ja exercido por DEP-QAR e DEP-ENG.
> Escolhe-lo repetiria o que dois pilotos ja testaram. **DEP-KMS e o unico departamento do acervo
> com exercicio sem custodia**, e emparelhado com DEP-EXE fecha os **dois lados** de OW-02 —
> regra vigente ha cinco ciclos com **um unico membro observado** (achado P1) e **nenhuma Carta
> que a demonstrasse**. A escolha e por **cobertura de regra nao exercida**, nao por conveniencia.

> **Limite declarado desta amostra.** Com as quatro classes exercidas, permanecem **sem Carta**
> cinco departamentos: **DEP-GOV** *(Guarda)*, **DEP-PRD**, **DEP-OPS**, **DEP-GRW** *(Linha)* e
> **DEP-TLS** *(Plataforma)*. **DEP-GOV e a ausencia mais significativa** — e o **revisor de toda
> Carta de Departamento** e o **unico escritor da camada EST**, e ambos os papeis sao exercidos
> nesta missao **sem que exista Carta que os declare**. Registrado como achado **IC-4**.

## 3. Validacao interclasses — oito cenarios

**Metodo:** cada cenario e uma pergunta real, respondida **usando apenas as quatro Cartas e as
normas que elas citam**. Registram-se **entrada, regra, saida, evidencia, falha e decisao**.
Ambiguidade nao resolvida e defeito do contrato e obriga correcao **antes** do rollout.

### 3.0 Segregacao na execucao dos cenarios

| Cenario | Objeto | Desenhado por | **Executado por** | Motivo |
|---|---|---|---|---|
| CX-1 | DEP-EXE × **DEP-QAR** | DEP-GOV | **DEP-GOV** | DEP-QAR e **parte** no conflito |
| CX-3 | Aprovacao de `FIT` cujo objeto inclui a Carta de DEP-EXE | DEP-GOV | **DEP-GOV** | DEP-QAR **executa** o `FIT` avaliado |
| CX-2 · CX-4 · CX-5 · CX-6 · CX-7 · CX-8 | DEP-EXE · DEP-KMS · DEP-ENG | DEP-QAR | **DEP-QAR** | DEP-QAR nao e parte nem produtor |

---

### CX-1 — Conflito de autoridade e escalonamento

| Campo | Conteudo |
|---|---|
| **Entrada** | DEP-EXE precisa acelerar a fila e **determina a DEP-QAR** que priorize a verificacao de um item, alterando a ordem que DEP-QAR seguia. |
| **Regra** | [DEP-EXE §10, **I-3**](../departments/exe/carta.md): impedido de *"priorizar, avaliar, instruir ou alocar DEP-GOV e DEP-QAR"*; substituto: **ninguem** — a Guarda responde ao Nivel 0. [DEP-EXE §4](../departments/exe/carta.md): *"Priorizar, avaliar ou instruir a Guarda → dono real: **Ninguem**"*. [DEP-QAR §10, **I-6**](../departments/qar/carta.md): impedido de *"ser priorizado, avaliado ou instruido por departamento de **Linha**"*. Fontes: **ES-02**, **IV-01**, FND-02 §2.1, FND-09 §6.2 R-07. |
| **Saida** | **A determinacao e nula.** DEP-QAR mantem a propria ordem. DEP-EXE pode **reportar ao Soberano** que a fila esta bloqueada — E4 —, e **nao** pode instruir. |
| **Evidencia** | R-07 de FND-09 §6.2 lista o coordenado de DEP-EXE: *"DEP de Linha e de Plataforma"* — a Guarda **nao consta**. A ausencia e a prova. |
| **Falha testada** | Se DEP-QAR fosse instruido e obedecesse, ES-02 e IV-01 estariam violados e o veto perderia independencia — a hipotese que **LV-09** protege. |
| **Decisao** | **Resolvido sem ambiguidade** — e **com um defeito de legibilidade encontrado.** |

> **Defeito encontrado — IC-5.** A materia de **I-6** da Carta de DEP-QAR nomeia apenas
> *"departamento de **Linha**"*. **DEP-EXE e Comando, nao Linha.** A protecao contra o Comando
> aparece so na coluna *quem me substitui* — *"DEP-EXE coordena Linha e Plataforma, nunca a
> Guarda"* — e na Carta de DEP-EXE, escrita **depois**. Quem consultar **apenas** o recorte de
> decisao de DEP-QAR, lendo a coluna de materia, **nao encontra o Comando**. A resposta correta
> exige **duas** Cartas. Severidade **media**; dono **DEP-EXE**; gatilho **primeira emenda a
> Carta de DEP-QAR**. **Nao corrigido aqui:** a Carta de DEP-QAR esta `ativo` e **ratificada**, e
> emenda-la exigiria **ato novo do Soberano** (MSG-2026-0001 §3). Corrigi-la nesta missao
> **alteraria texto ratificado** — exatamente o que o ato proibe.

> **O cenario produziu a evidencia mais forte a favor de DC-03 e DC-04 juntas.** As duas Cartas
> convergem **sem se citarem**, porque ambas citam a **mesma fonte** (ES-02). E o efeito
> pretendido por DC-04. Mas a convergencia so e **verificavel** lendo as duas — e e isso que
> IC-5 registra.

---

### CX-2 — Custodia versus exercicio de Capability

| Campo | Conteudo |
|---|---|
| **Entrada** | DEP-KMS, que **exerce** `CAP-comunicacao` **sem custodiar**, conclui que o envelope de mensagem deve mudar e quer alterar o escopo da Capability. |
| **Regra** | [DEP-KMS §10, **I-8**](../departments/kms/carta.md): impedido de alterar `CAP-comunicacao`; substituto **DEP-EXE**, custodio, pelo rito de FND-08 §6.3. [DEP-EXE §2](../departments/exe/carta.md) declara a custodia e o exercicio alheio. **PR-3** de ADR-0011: acrescentar ou alterar exercente e mudanca na **Carta de Capability**, nunca declaracao unilateral. **RL-03**, **RM-01**, **RM-05**. |
| **Saida** | DEP-KMS **propoe** a DEP-EXE. DEP-EXE, como custodio, **propoe** a alteracao na Carta de Capability; revisam **DEP-GOV + DEP-QAR**; aprova e ratifica o **SOBERANO** (FND-09 §8.2, linha `CAP`). |
| **Evidencia** | E a **primeira vez** que OW-02 e exercida **dos dois lados** por Cartas: o custodio declara *"exercida por outros"* e o exercente declara *"exerco sem custodiar"*. Antes destas duas Cartas, a regra tinha **um membro na projecao e nenhum na Carta**. |
| **Falha testada** | Se DEP-KMS alterasse a Carta de Capability por conta propria, violaria **PR-3** e **RL-03**, e criaria **segunda fonte** da competencia — o risco **R3** de ADR-0011 §9. |
| **Decisao** | **Resolvido sem ambiguidade.** **DC-02 exercido com membro real**, e nao apenas com colunas vazias. |

> **O que este cenario prova, e que os pilotos anteriores nao podiam provar.** Em `DEP-QAR` e
> `DEP-ENG` as duas linhas finais de §2 sao *"nenhuma"* e *"nenhuma"* — a regra estava
> **declarada e nao exercida**. Aqui as duas linhas tem **conteudo**, e em Cartas diferentes,
> **apontando uma para a outra**. O achado **P1** *(22 de 23 Capabilities com `exercentes` =
> `custodio`)* **permanece aberto**: um membro continua abaixo dos dois de AQ-03. O que mudou e
> que ele deixou de ser invisivel fora da projecao.

---

### CX-3 — Criacao, revisao e aprovacao de artefato

| Campo | Conteudo |
|---|---|
| **Entrada** | O `FIT` desta missao avalia, entre outros objetos, a **Carta de DEP-EXE — produzida por DEP-EXE**. A matriz atribui a aprovacao de `FIT` a **DEP-EXE**. Quem aprova? |
| **Regra** | [DEP-EXE §10, **I-2**](../departments/exe/carta.md): impedido de *"aprovar `FIT` ou `REV` cujo objeto avaliado eu tenha produzido"*; substituto **DEP-GOV**; se tambem impedido, **SOBERANO**. **PI-05**, **GV-04**, **FT-02**. [DEP-QAR §10, **I-4**](../departments/qar/carta.md): DEP-QAR nao aprova o proprio veredito. |
| **Saida** | **FIT-2026-006 e esta revisao sao aprovados por DEP-GOV, nao por DEP-EXE.** Executor permanece **DEP-QAR** (que nao produziu nenhum objeto avaliado). |
| **Evidencia** | **Precedente identico, ja ocorrido:** `FIT-2026-003` tem `aprovador: DEP-GOV` — medido por `grep` no frontmatter dos 11 artefatos avaliativos. **8 de 11** sao aprovados por DEP-EXE; **1** por DEP-GOV, exatamente por este impedimento; **2** pelo SOBERANO. |
| **Falha testada** | Se DEP-EXE aprovasse, o produtor aprovaria o parecer sobre o proprio produto — **PI-05**. O veredito nao seria nulo por FT-02 *(o executor e independente)*, mas a **aprovacao** seria. |
| **Decisao** | **Resolvido sem ambiguidade, e com consequencia real nesta missao:** a mudanca de aprovador foi **aplicada**, nao apenas descrita. |

> **Este cenario e o unico dos oito cuja resposta alterou um artefato desta missao.** Os demais
> validam; este **decidiu**. E o exercicio mais forte de **DC-03**: o impedimento foi lido antes
> do ato, e nao depois — que e precisamente a funcao de B9.

> **Residuo declarado.** O impedimento cruzado **RX-3 / RQ-2** — achado **C5** de
> REV-CONSOLIDACAO, dono DEP-GOV — permanece aberto: a Carta nomeia o achado em vez de
> improvisar substituto. **Segunda ocorrencia registrada** da familia; a primeira foi
> FIT-2026-003.

---

### CX-4 — Handoff e Pacote de Contexto

| Campo | Conteudo |
|---|---|
| **Entrada** | DEP-EXE emite briefing para escrever a **terceira** Carta e pede a DEP-KMS o pacote de contexto. O pedido chega **sem gatilho declarado**, com o texto *"manda tudo sobre departamentos"*. |
| **Regra** | [DEP-KMS §8.2](../departments/kms/carta.md): pacote emitido com *"recorte por ID, com custo medido em linhas e data"*; criterio de devolucao: *"pedido **sem gatilho declarado** — carregamento sem gatilho e falha de curadoria"* (**PC-01**, **CE-01**). [DEP-EXE §8.2](../departments/exe/carta.md): briefing aceito exige *"item priorizado, dono nomeado, autonomia concedida declarada, vinculo a Capability valido"*. **HO-01**, **HO-02**, **HO-04**. |
| **Saida** | **DEP-KMS devolve o pedido.** Reformulado com gatilho — *"escrever Carta de Departamento"* —, o pacote entregue e o da linha correspondente do catalogo §11: nucleo + FND-02 + ADR-0011 + `TPL-carta-departamento` + `capabilities/README §10`, **2.347 linhas medidas**. |
| **Evidencia** | O custo esta medido no [catalogo mestre §11](../governance/artifact-registry.md) desde a Missao 1.6 e foi **efetivamente o pacote usado** para escrever as duas Cartas desta missao. **8,9%** do acervo, contra os **100%** que *"tudo sobre departamentos"* implicaria. |
| **Falha testada** | Se DEP-KMS atendesse o pedido literal, entregaria o acervo inteiro — violando **CE-01** por acao de quem **cura** CE-01, o risco declarado em DEP-KMS §9.1. |
| **Decisao** | **Resolvido sem ambiguidade.** **A devolucao do handoff e o comportamento correto**, e ela e verificavel porque B10 declara o criterio de devolucao **antes** do pedido chegar. |

---

### CX-5 — Leitura e escrita em memoria

| Campo | Conteudo |
|---|---|
| **Entrada** | DEP-KMS conclui, a partir desta missao, que *"toda Carta deve declarar impedimento sem substituto quando ele nao existir"* e quer gravar a conclusao como **norma**, na camada **EST**. |
| **Regra** | [DEP-KMS §10, **I-1**](../departments/kms/carta.md): *"escrever na camada EST"* — impedido; substituto **DEP-GOV**, **mediante ADR** (**FND-06 §3.1**). [DEP-KMS §10, **I-3**](../departments/kms/carta.md): *"transformar registro em norma"* — impedido; **MM-07**: memoria **informa, nao obriga**. Criterio de alocacao de FND-06 §4: licao generalizavel → camada **APR**, dono **DEP-KMS**. |
| **Saida** | **Tres negativas e um destino.** Nao escreve em EST; nao vira norma por registro; **grava em APR**, camada de que e dono; para virar norma, **ADR** pelo rito. |
| **Evidencia** | As **quatro** Cartas declaram o mesmo papel em EST — *"leitor obrigatorio, nao escrevo"* —, e as quatro apontam para **DEP-GOV**. Verificado nas quatro §9. |
| **Falha testada** | Se a conclusao fosse gravada em EST, uma licao viraria norma **sem ADR** — o mecanismo que **MM-07** existe para impedir, e a causa da familia de INC-2026-001. |
| **Decisao** | **Resolvido sem ambiguidade** — e **com uma lacuna de cobertura encontrada.** |

> **Lacuna encontrada — IC-4.** Quatro Cartas declaram que a escrita em EST e de **DEP-GOV**, e
> **DEP-GOV nao tem Carta**. A regra e verificavel **apenas** contra FND-06 §3.1, e nao contra a
> Carta do departamento que a exerce. O mesmo vale para o papel de **revisor de toda Carta de
> Departamento**, exercido por DEP-GOV **quatro vezes** nesta missao. Severidade **media**; dono
> **DEP-EXE**; gatilho **proxima Carta escrita** — que, pela Condicao 2 de FIT-2026-005 e por
> este achado, deveria ser a de **DEP-GOV**.

---

### CX-6 — Incidente e excecao

| Campo | Conteudo |
|---|---|
| **Entrada** | Descobre-se **IC-1**: a correcao M1 foi declarada aplicada em REV-DEPARTAMENTO §3.7 e **nunca chegou ao template**. Duas Cartas foram escritas sob checklist que se acreditava corrigido. **Isto e incidente de conformidade?** |
| **Regra** | FND-04 §10 e [FND-10 §4.2](10-artifact-framework.md): **Incidente** = *"violacao detectada, causa e correcao"*; conteudo proibido: *"fechamento sem correcao de causa"*. **CV-04** e **RG-03**: artefato desatualizado apos mudanca aprovada e **mudanca incompleta**, **nao norma nova**. FND-09 §8.2, linha `INC`: propoe **quem detecta (obrigatorio)** · revisa e registra **DEP-GOV** · fecha **DEP-QAR**. [DEP-QAR §7](../departments/qar/carta.md): *"Incidente — **Fecho**; nao registro nem numero"*. |
| **Saida** | **Nao se abre incidente.** Nenhuma norma foi contrariada: a decisao M1 **existia e era valida**, e faltou **propagacao**. O tratamento correto e **completar a mudanca** (CV-04) e registrar o achado com dono e gatilho — feito em §0 e §7. **Nenhuma excecao formal e necessaria**: nada precisou operar fora da norma. |
| **Evidencia** | `governance/exceptions/` tem **0** registros; `governance/incidents/` tem **2**, ambos por **violacao** — LV-05, GV-05, CV-09 em INC-2026-001 e INC-2026-002. IC-1 **nao viola nenhuma norma nomeavel**. |
| **Falha testada** | Abrir incidente sem norma violada **inflaria** o instrumento e tornaria "incidente" sinonimo de "defeito" — e o registro perderia poder de sinalizar violacao real. O erro simetrico — **nao registrar nada** — deixaria o defeito vivo com o registro afirmando que foi corrigido. |
| **Decisao** | **Resolvido sem ambiguidade.** **Achado com dono e gatilho, correcao aplicada, sem incidente e sem excecao.** |

> **A pergunta que este cenario responde e nova no acervo:** *qual e a fronteira entre **defeito
> de propagacao** e **violacao de norma**?* A resposta — *violacao exige norma nomeavel* — nao
> estava escrita em lugar nenhum, e agora esta, com dois casos concretos de cada lado.

---

### CX-7 — Especializacao e fusao

| Campo | Conteudo |
|---|---|
| **Entrada** | **DEP-EXE** dispara VC-03 *(4 > 3)*; **DEP-ENG** tambem *(5 > 3)*; **DEP-KMS nao** *(2 < 3)*; **DEP-QAR** esta no limite *(3)*. Dividir algum? E, simetricamente: **consolidar** algo? |
| **Regra** | **SE-01**: ganho previsto nao autoriza divisao. **SE-02**: exige **dois** sinais observados. **ES-03**/**ES-04**: departamento nao nasce por volume, e funcao nova vive dentro de area existente ate provar fronteira propria. **PI-14 regra 2**: adiar a divisao obriga registrar motivo e custo. **SE-05**/**EV-08**: fusao e o movimento **simetrico e igualmente obrigatorio**. |
| **Saida** | **Nao especializar nenhum dos quatro** — quatro decisoes registradas, cada uma com **um** sinal observado e o custo declarado. **E abrir a proposta de consolidacao**, porque o gatilho de **R3** de FIT-2026-005 disparou. |
| **Evidencia** | Sinais medidos: DEP-EXE **1** *(contagem VC-03)*; DEP-ENG **1** *(contagem)*; DEP-QAR **1** *(fronteira, impedimento cruzado ocorrido 1 vez)*; DEP-KMS **1** *(fronteira P2)*. **Nenhum atinge 2.** Do lado da consolidacao: [DEP-EXE §11, **KX-8**](../departments/exe/carta.md) mede **0** propostas EV-08 abertas em **5** ciclos, e DEP-EXE **tem a autoridade** de abri-las (X-12). |
| **Falha testada** | Dividir DEP-EXE hoje promoveria **FIN**, funcao com carga medida **zero** (KX-13) — criaria area para responsabilidade sem volume, violando **ES-03**. Nao abrir a consolidacao deixaria **PI-14 exercido pela metade** pelo sexto ciclo. |
| **Decisao** | **Resolvido sem ambiguidade, e nos dois sentidos.** **DC-06 impediu quatro divisoes**; e a simetria de PI-14 **obrigou** o movimento inverso, registrado em §8 e em [FIT-2026-006](../governance/fitness/FIT-2026-006-validacao-interclasses.md). |

> **A informacao mais util do cenario e a excecao:** **DEP-KMS e o unico dos quatro que nao
> dispara VC-03**. O sinal de amplitude **nao e universal entre classes** — e a Plataforma pode
> ser a classe de escopo naturalmente estreito. Com **quatro** observacoes, e sinal, nao
> conclusao.

---

### CX-8 — Carregamento minimo de contexto

| Campo | Conteudo |
|---|---|
| **Entrada** | Pergunta operacional real desta missao: *"DEP-EXE pode aprovar o `FIT` que avalia a propria Carta?"* — **quantas linhas custa responder?** |
| **Regra** | **DC-10**: o perfil minimo e **medido**, nunca estimado. **CE-01**/**PC-01**: carregar alem do recorte exige gatilho declarado. **CE-02**/**CE-04**: medicao reproduzivel, com data. |
| **Saida** | **155 linhas** — o recorte de decisao de `DEP-EXE`, secoes 1, 2, 4, 5 e 10. A resposta esta em **I-2**, uma linha da secao 10. |
| **Evidencia** | Recortes de decisao medidos por `sed`+`wc -l` nas quatro Cartas: **`DEP-QAR` 111** · **`DEP-ENG` 115** · **`DEP-KMS` 139** · **`DEP-EXE` 155**. Mediana **127**. Proporcao da Carta: **29% · 29% · 30% · 32%**. Custo em relacao ao acervo: **0,4% a 0,6%**. |
| **Falha testada** | Sem as Cartas, responder exigiria cruzar **FND-02 §3** *(479 linhas)*, **FND-09 §8.2** *(recorte de 1.243)* e **FND-01 §7.3** *(468 linhas)* — e ainda assim **nenhuma das tres declara o impedimento**, que so existe porque B9 o declarou. **A pergunta era irrespondivel antes das Cartas**, nao apenas cara. |
| **Decisao** | **Resolvido sem ambiguidade.** **DC-10 exercido nas quatro classes**, com a proporcao estavel entre 29% e 32%. |

> **A estabilidade da proporcao e o achado.** Quatro Cartas de **quatro classes distintas**, com
> tamanhos entre 386 e 481 linhas, concentram a informacao de decisao em **29–32%** do texto. A
> faixa e estreita o bastante para virar expectativa verificavel na quinta Carta: **recorte fora
> de 25–35% e sinal de que B4/B9 estao sub ou superdimensionados.** Registrado como criterio
> derivado, nao como norma — vira norma so por ADR.

### 3.9 Sintese da validacao

| Cenario | Classes exercidas | Ambiguidade nao resolvida? | Defeito encontrado |
|---|---|---|---|
| CX-1 Conflito de autoridade | **Comando × Guarda** | Nao | **Sim — IC-5** *(materia de I-6 nomeia so a Linha)* |
| CX-2 Custodia × exercicio | **Comando × Plataforma** | Nao | Nao |
| CX-3 Criacao/revisao/aprovacao | **Comando × Guarda** | Nao | Nao — **mas alterou o aprovador desta missao** |
| CX-4 Handoff e Pacote de Contexto | **Comando × Plataforma** | Nao | Nao |
| CX-5 Memoria | **Plataforma × Guarda** *(+ DEP-GOV ausente)* | Nao | **Sim — IC-4** *(DEP-GOV exerce sem Carta)* |
| CX-6 Incidente e excecao | **Guarda × Comando** | Nao | **Sim — IC-1**, corrigido em §0 |
| CX-7 Especializacao e fusao | **as quatro** | Nao | Nao — **mas disparou a consolidacao** |
| CX-8 Carregamento minimo | **as quatro** | Nao | Nao |

**Oito cenarios · quatro classes exercidas · zero ambiguidades nao resolvidas · tres defeitos
encontrados**, dos quais **um corrigido** *(IC-1)* e **dois abertos com dono e gatilho**
*(IC-4, IC-5)*.

> **Comparacao com a validacao anterior.** REV-DEPARTAMENTO executou **seis** cenarios em **duas**
> classes e encontrou **dois** defeitos. Esta executou **oito** em **quatro** e encontrou
> **tres** — dois deles **so visiveis entre classes**: IC-5 exige Comando **e** Guarda; IC-4
> aparece quando tres classes apontam para um departamento **sem Carta**. **A validacao
> interclasses encontrou o que a intraclasse nao encontraria**, e essa e a evidencia direta a
> favor de A2 de ADR-0011 §8 ter sido tratada como limite real, e nao como formalidade.

## 4. Segregacao — residuos desta missao

### 4.1 Verificacao de DEP-QAR sobre os blocos impedidos da Carta DEP-EXE

> DEP-EXE esta impedido de verificar a propria Carta (I-1). Os blocos em que ele julgaria a
> propria autoridade foram verificados por **DEP-QAR**, com forma por DEP-GOV. Mesmo instrumento
> do desvio de REV-DEPARTAMENTO §4.1, **com os papeis invertidos**.

| Bloco | O que DEP-QAR verificou | Resultado |
|---|---|---|
| **B4** — autoridade | Cada uma das **13** linhas de §5 tem coluna **Fonte** preenchida, e cada fonte foi conferida no documento citado | **Conforme.** Nenhuma autoridade autodeclarada |
| **B4** — o que nao decide | **7** linhas em §5.1, todas com dono e fonte | **Conforme** |
| **B4** — ampliacao de autoridade | Comparacao linha a linha entre §5 da Carta, FND-02 §3 e FND-01 §7.3 | **Nenhuma ampliacao.** A Carta **restringe** em um ponto relevante: renomeia *"ratifica"* de FND-01 §7.3 para **"homologar"**, para **nao** sugerir poder de dar vigencia |
| **B9** — impedimentos | **9** impedimentos, todos com materia, motivo, substituto e fonte | **Conforme.** **I-1 declara substituto parcial** — ninguem pode propor Carta alem de DEP-EXE — e o declara **como limite**, em vez de omiti-lo |
| **B12** — carregamento | Numeros de §13.2 reproduzidos por DEP-QAR com `sed`+`wc -l`: **63**, **155** e **481** | **Conforme** — os tres valores conferem |
| **Conferencia cruzada B4 × B9** *(M1, agora no checklist)* | Cada linha de §5 lida contra o impedimento correspondente de §10 | **Conforme.** As 13 linhas de autoridade tem impedimento vizinho declarado; a mais critica — *"aprovar o veredito de aptidao"* — tem **I-2** exatamente ao lado |

### 4.2 Residuo: DEP-GOV aprova esta revisao e a Carta que ela examina o nomeia

| Campo | Conteudo |
|---|---|
| **Conflito identificado** | **Sim, parcial.** DEP-GOV **aprova** esta revisao e o `FIT` desta missao, por impedimento de DEP-EXE (CX-3). E, simultaneamente, DEP-GOV e o **revisor** das quatro Cartas |
| **O que nao e conflito** | DEP-GOV **nao produziu** nenhum artefato avaliado, e **nao e objeto** de nenhuma das quatro Cartas — nao tem Carta. FT-02 e RM-06b estao satisfeitos quanto a producao |
| **O que e conflito** | DEP-GOV aprova o parecer que **avalia a propria revisao**: revisou as Cartas e aprova o documento que julga se elas estao corretas |
| **Desvio aplicado** | A **execucao** dos cenarios e do exame permanece com **DEP-QAR**, que nao revisou as Cartas. DEP-GOV **aprova**, e nao executa nem julga o merito |
| **Alternativa avaliada e recusada** | Manter DEP-EXE como aprovador **agrava**: ele **produziu** dois dos objetos avaliados, e o conflito passaria de forma a merito. Escalar a aprovacao ao SOBERANO foi considerado e **recusado por proporcionalidade**: o objeto e **C2/Tipo 2**, e FND-10 §10.3 nao exige o Soberano; escalar criaria precedente de submeter parecer C2 a autoridade maxima |
| **Residuo remanescente** | DEP-GOV aprova documento que contem a verificacao do proprio trabalho de revisao. **Declarado em vez de omitido** (PI-10). O residuo **so desaparece quando DEP-GOV tiver Carta** e o impedimento estiver escrito — que e **IC-4** |

## 5. Comparacao das quatro classes

> **Projecao unica (PJ-02).** **Fonte:** as quatro Cartas e FND-02 §2.1 e §3. **Campos
> projetados:** mandato, autoridade, interfaces, artefatos, memoria, riscos e incompatibilidades,
> pivotados **por classe**. **Finalidade:** responder *"o que muda de uma classe para outra?"* —
> pergunta que nenhuma Carta responde sozinha e que a matriz de FND-02 §4 nao responde, por ser
> orientada a **par de departamentos**, nao a **classe**. **Atualizacao:** pela mesma mudanca que
> altera uma das Cartas (CV-04). **Esta e a unica comparacao por classe do acervo**; em
> divergencia, prevalecem as Cartas (PJ-03).

### 5.1 A comparacao

| Dimensao | **Comando** *(DEP-EXE)* | **Guarda** *(DEP-QAR)* | **Linha** *(DEP-ENG)* | **Plataforma** *(DEP-KMS)* |
|---|---|---|---|---|
| **Pergunta que responde** | Isto vem antes ou depois, e por quem? | Isto pode passar? | Como isto se faz? | Com o que voces contam? |
| **Mandato** | Converter direcao em prioridade executavel | Verificar de forma independente | Construir a solucao mais simples defensavel | Fazer a organizacao lembrar |
| **Nivel · autonomia** | **1** · **A3** | 2 · A2 | 2 · A2 | 2 · A2 |
| **Responde a** | **SOBERANO** | **SOBERANO** *(ES-02)* | DEP-EXE | DEP-EXE |
| **Verbo de autoridade** | **decide e arbitra** | **veta** | **entrega** | **serve** |
| **Poder de veto** | Nao | **Sim** | Nao | Nao |
| **Portao proprio** | **QG-0** | **QG-3, QG-4, QG-6** | QG-2 *(com GOV)* | **QG-5** |
| **Capabilities custodiadas** | 4 | 3 | 5 | 2 |
| **VC-03 dispara?** | **Sim** *(4>3)* | Nao *(=3)* | **Sim** *(5>3)* | **Nao** *(2<3)* |
| **Exercicio sem custodia** | nenhum | nenhum | nenhum | **1 — unico do acervo** |
| **Custodia exercida por outro** | **1 — unico do acervo** | nenhuma | nenhuma | nenhuma |
| **Artefato de que e autor** | Carta de Departamento | `FIT` e `REV` | ADR tecnico, RFC | registro APR, indice, baseline |
| **Artefato que aprova** | `FIT`, `AGT`, `SUB`, `SKL` | **nenhum** — fecha `INC` | nenhum | nenhum |
| **Camada de memoria de que e dono** | nenhuma | nenhuma | **TEC** | **APR** |
| **Escreve em EST?** | **Nao** | **Nao** | **Nao** | **Nao** — as quatro apontam para DEP-GOV |
| **Impedimentos declarados (B9)** | **9** | 7 | 8 | **10** |
| **Risco caracteristico** | Coordenacao virar merito | Complacencia na verificacao | Amplitude e divida invisivel | Curador sem propriedade |
| **Incompatibilidade que a define** | Arbitro × parte | Produtor × verificador | Produtor × aprovador | Curador × autor do conteudo |
| **Recorte de decisao** | **155** linhas *(32%)* | **111** *(29%)* | **115** *(29%)* | **139** *(30%)* |

### 5.2 Regra universal, regra de classe e diferenca acidental

A separacao exigida pela missao. **Universal** = vale nas quatro e valeria numa quinta.
**De classe** = decorre da natureza da classe. **Acidental** = decorre do estado atual do
sistema e mudaria sem que nenhuma norma mudasse.

| # | Propriedade observada | Natureza | Fundamento |
|---|---|---|---|
| U-1 | Toda Carta declara os **doze blocos**, e bloco vazio a torna nao conforme | **Universal** | ADR-0011 §5.2; AC-06 |
| U-2 | Toda autoridade de B4 cita **fonte**; autoridade nao declarada **nao existe** | **Universal** | DC-04, AU-09 |
| U-3 | Todo departamento declara **impedimento com substituto nomeado** | **Universal** | DC-03 |
| U-4 | Nenhum departamento **escreve em EST** | **Universal** — nas quatro | FND-06 §3.1 |
| U-5 | Nenhum departamento **aprova a propria Carta**; o aprovador e o **SOBERANO** | **Universal** | DC-09; FND-09 §8.2 |
| U-6 | Nenhum departamento **cria portao**; os sete sao de FND-01 §6.2 | **Universal** | FND-01 §6.2 |
| U-7 | Todo departamento e **contribuinte obrigatorio de APR** e **escritor de OPR** | **Universal** | QG-5; FND-06 §2.1 |
| U-8 | O recorte de decisao custa **29–32%** da Carta | **Universal — observado**, nao normativo | Medicao CX-8; **quatro** observacoes |
| U-9 | Toda Carta **projeta** a custodia e **nunca** a redefine | **Universal** | DC-01, DC-08, PR-1 a PR-3 |
| **C-1** | **So a Guarda veta**; so ela responde ao Nivel 0 sem coordenacao | **De classe** | FND-02 §2.1; ES-02, IV-01 |
| **C-2** | **So o Comando arbitra** entre areas, e **so ele nao e coordenado por ninguem** alem do Soberano | **De classe** | FND-02 §3; R-07 |
| **C-3** | **So a Linha e avaliada em QG-3** e nunca avalia | **De classe** | FND-02 §5; QG-3 |
| **C-4** | **So a Plataforma entrega a todos sem autoridade sobre nenhum** | **De classe** | **ES-07**; FND-02 §4 |
| **C-5** | **So o Comando homologa** decisao de outro departamento sem dar vigencia | **De classe** | FND-01 §7.3 |
| **C-6** | **A Guarda e a unica classe cujo impedimento central e sobre si mesma** *(nao se verifica)*; nas outras tres o impedimento central e **sobre o vizinho** | **De classe** | RM-06b × MT-09, ES-07, PI-05 |
| **A-1** | DEP-EXE e o **unico** departamento de Comando | **Acidental** | FND-02 §2.1 — um segundo Comando seria mudanca estrutural, nao contradicao |
| **A-2** | DEP-ENG custodia **5** e DEP-KMS **2** | **Acidental** | Distribuicao atual do catalogo; muda com uma Carta de Capability |
| **A-3** | **Um unico** exercicio sem custodia no acervo inteiro | **Acidental** | Achado P1 — a regra OW-02 admite n; o acervo tem 1 |
| **A-4** | DEP-EXE e autor de **4 de 4** Cartas | **Acidental — e sob correcao** | FND-09 §8.2 fixa o proponente; a **concentracao** e da fase, nao da norma |
| **A-5** | Nenhuma Carta tem indicador de **desempenho** medido; so de **estado** | **Acidental** | Nao ha ciclo de entrega; DC-07 obriga a marca `definido, sem valor`, e ela foi usada **13** vezes nas quatro |
| **A-6** | **Cinco** departamentos sem Carta, entre eles **DEP-GOV** | **Acidental — e e o achado IC-4** | Rollout incompleto por decisao, nao por norma |

> **A distincao que mais importa e C-6, e ela so aparece com as quatro classes na mesma tabela.**
> Em Comando, Linha e Plataforma, o impedimento central protege **o vizinho** do departamento —
> nao decidir merito alheio (**MT-09**), nao decidir pela Linha (**ES-07**), nao aprovar a propria
> entrega (**PI-05**). Na Guarda, o impedimento central protege **o sistema do proprio
> departamento**: `verifica` nao admite par reflexivo (**RM-06b**). **Sao dois desenhos de
> impedimento, nao um so** — e o contrato de ADR-0011 acomoda ambos com a mesma B9, sem regra
> especial de classe. **E a evidencia mais forte desta missao a favor da suficiencia do
> contrato.**

### 5.3 Incompatibilidades entre classes

| Par | Compativel? | Fundamento |
|---|---|---|
| Comando **coordena** Guarda | **Nao** | **ES-02, IV-01**; R-07 nao lista a Guarda |
| Comando **decide merito** de qualquer classe | **Nao** | MT-09; FND-01 §7.3 |
| Guarda **produz** o que verifica | **Nao** | PI-05, FT-02, LV-03 |
| Guarda **e priorizada** por Comando ou Linha | **Nao** | ES-02 |
| Linha **aprova** a propria entrega | **Nao** | PI-05; QG-3 |
| Linha **instrui** Guarda | **Nao** | FND-02 §4 |
| Plataforma **decide** pela Linha | **Nao** | ES-07 |
| Plataforma **julga merito** do que cura | **Nao** | FND-02 §3 |
| Comando **funde-se** a qualquer classe | **Nao** — exigiria **C3** | DEP-EXE §12.2 |
| Guarda **funde-se** a Guarda *(QAR+GOV)* | **Nao** — exigiria **C3** | DEP-QAR §12.2; PI-05 |
| **Plataforma funde-se a Plataforma** *(KMS+TLS)* | **Sem impedimento normativo** — falta **sinal** | DEP-KMS §12.2 |

> **A ultima linha e a unica fusao do sistema que nenhuma norma proibe.** Ela nao ocorre por
> falta de **sinal observado**, nao por vedacao. Registrado para que a distincao entre *"proibido"*
> e *"ainda sem sinal"* fique escrita — sao coisas diferentes e o acervo nao as separava.

## 6. Pacote de ratificacao — os dois novos pilotos

> **Este pacote informa. Nao produz, nao registra e nao antecipa ato soberano.** A decisao e do
> **SOBERANO** e nao esta contida aqui (DC-09, LM-03).

### 6.1 `DEP-EXE` — Gabinete Executivo *(Comando)*

| Campo | Conteudo |
|---|---|
| **ID** | `DEP-EXE` |
| **Versao** | **1.0.0** |
| **Hash SHA-256** | `437f261467df28d94e519d54c40af33f132a83696892d22abc14db134aa942e1` |
| **Linhas** | **481** |
| **Local** | [`departments/exe/carta.md`](../departments/exe/carta.md) |
| **Estado** | **`em-revisao`** · `ratificacao: pendente` |
| **Capabilities vinculadas** | `CAP-estrategia` *(nucleo)* · `CAP-coordenacao` · `CAP-financeiro` · `CAP-comunicacao` — **4 custodiadas**, todas `ativo`; VC-01 satisfeito |
| **Revisao independente** | Autor **DEP-EXE** · revisor **DEP-GOV** · blocos B4, B9 e B12 verificados por **DEP-QAR** (§4.1) · executor dos cenarios **DEP-GOV** nos que envolvem DEP-EXE (§3.0) |
| **Conformidade** | **12 de 12 blocos** preenchidos · **13** linhas de autoridade com fonte · **9** impedimentos com substituto · **14** indicadores, **9** medidos e **5** marcados `definido, sem valor` · conferencia cruzada **B4 × B9** conforme |
| **Desvios** | **(1)** Autor e objeto da propria Carta — sem substituto possivel na **proposicao** (I-1, achado **IC-3**). **(2)** DEP-EXE nao aprova o `FIT` desta missao; aprova **DEP-GOV** (CX-3) |
| **Riscos residuais** | **RX-3** impedimento cruzado *(achado C5, dono DEP-GOV, 2a ocorrencia)* · **RX-4** VC-03 disparado *(achado P6, avaliado, decisao de nao dividir com custo declarado)* · **RX-6** zero consolidacoes em 5 ciclos *(R3, escalada em §8)* · **RX-7** autoria concentrada em 4 de 4 Cartas *(R1)* |
| **Achados que abre** | **IC-2** *(colisao do termo "ratifica" em FND-01 §7.3)* · **IC-3** *(impedimento sem substituto na proposicao)* |
| **Recomendacao** | **APROVAR** |
| **Fundamento da recomendacao** | O contrato foi cumprido integralmente, os desvios sao **estruturais e declarados** — decorrem da matriz de FND-09 §8.2, nao de escolha do autor —, e a verificacao dos blocos impedidos foi feita por departamento independente que **nao produziu** a Carta. Os quatro riscos residuais **ja tinham dono e gatilho antes desta Carta**; nenhum e criado por ela |
| **O que a aprovacao nao alcanca** | Nao resolve IC-3, que exige **emenda C3** a FND-09 §8.2. Nao autoriza as cinco Cartas restantes |

### 6.2 `DEP-KMS` — Conhecimento e Memoria *(Plataforma)*

| Campo | Conteudo |
|---|---|
| **ID** | `DEP-KMS` |
| **Versao** | **1.0.0** |
| **Hash SHA-256** | `c261ff93e36688a76c82e5efe5110e946c331accc6fc6f11d1b55c8059e31ac5` |
| **Linhas** | **460** |
| **Local** | [`departments/kms/carta.md`](../departments/kms/carta.md) |
| **Estado** | **`em-revisao`** · `ratificacao: pendente` |
| **Capabilities vinculadas** | `CAP-conhecimento` *(nucleo)* · `CAP-aprendizado-organizacional` *(nucleo)* **custodiadas** · `CAP-comunicacao` **exercida sem custodiar** — 3 vinculos, todos `ativo`; VC-01 satisfeito |
| **Revisao independente** | Autor **DEP-EXE** · revisor **DEP-GOV** · verificacao adversarial **DEP-QAR** · executor dos cenarios **DEP-QAR**. **Quatro papeis distintos; nenhum e o objeto** |
| **Conformidade** | **12 de 12 blocos** · **8** linhas de autoridade com fonte · **10** impedimentos com substituto — **o maior numero das quatro Cartas** · **16** indicadores, **13** medidos e **3** `definido, sem valor` · conferencia cruzada **B4 × B9** conforme |
| **Desvios** | **Nenhum.** E a **unica das quatro Cartas sem residuo de segregacao a declarar** |
| **Riscos residuais** | **MK-1** licao que nao chega a fonte *(DR-8, **mitigado** como criterio de QG-5)* · **MK-2** medicao autorreferente *(DR-6, **regra escrita** em §13.2)* · **MK-4** curador de cinco camadas e dono de uma *(P2, declarado, nao resolvido)* · **MK-6** pacotes sem consumidor *(R2/DR-2, **nao-avaliavel** — §8)* · **MK-7** crescimento medido sem consolidacao *(R3)* |
| **Achados que fecha ou materializa** | **DR-6** — regra de medicao autorreferente **escrita** *(§13.2)* · **DR-8** — verificacao de chegada a fonte vira **criterio de liberacao de QG-5** *(§5.2)* |
| **Recomendacao** | **APROVAR** |
| **Fundamento da recomendacao** | Zero desvios de segregacao; **dois achados abertos ha ciclos sao materializados** em criterio verificavel, e nao apenas descritos; e a Carta cobre a unica linha *"exerce sem custodiar"* do acervo, dando a OW-02 o exercicio que faltava. Os riscos residuais sao **declarados com dono e gatilho**, e **MK-4** e explicitamente **nao resolvido** aqui por pertencer a outro rito |
| **O que a aprovacao nao alcanca** | Nao resolve **P2**, que exige decidir se ser dono de camada e exercer `CAP-conhecimento` — altera o catalogo **ou** FND-06. Nao autoriza as cinco Cartas restantes |

### 6.3 O que este pacote deliberadamente **nao** faz

| Nao faz | Norma |
|---|---|
| Nao aprova, nao ratifica e nao antecipa vigencia | DC-09; LM-02 a LM-06 |
| Nao interpreta silencio como aprovacao | LM-03; CM-07 |
| Nao estende a ratificacao de 2026-07-28 as duas Cartas novas | LM-03 — **elas nao existiam na data do ato** |
| Nao altera as Cartas ja ratificadas para acomodar achados desta missao | **IC-5 permanece aberto** por isso mesmo (CX-1) |
| Nao decide o rollout das cinco restantes | FIT-2026-006 §Rollout |

## 7. Achados

| # | Achado | Severidade | Dono | Gatilho |
|---|---|---|---|---|
| **IC-1** | **Correcao M1 declarada aplicada e nunca propagada ao template.** Duas Cartas foram escritas sob checklist que se acreditava corrigido | **Media** | DEP-GOV | ✅ **Corrigido nesta revisao** — §0; template **1.2.0** |
| **IC-2** | **Colisao terminologica de "ratifica".** FND-01 §7.3 usa *Ratifica: DEP-EXE* em quatro materias; LM-02 e DC-09 reservam *ratificacao* ao ato do Soberano que da vigencia. **Dois institutos, um nome** | **Media** | DEP-GOV | Proxima emenda a FND-01, **ou** primeira vez que um artefato registrar "ratificado por DEP-EXE" |
| **IC-3** | **Impedimento sem substituto na proposicao.** Ninguem alem de DEP-EXE pode propor Carta de Departamento; o impedimento de I-1 alcanca revisao, verificacao e aprovacao, e **nao alcanca a autoria**. Resolver exige **C3** | **Media** | DEP-GOV | Primeira Carta de Departamento apos a existencia de agentes |
| **IC-4** | **DEP-GOV exerce dois papeis criticos sem Carta:** revisor de **toda** Carta de Departamento *(4 vezes nesta missao)* e **unico escritor da camada EST** *(apontado pelas quatro Cartas)* | **Media** | DEP-EXE | **Proxima Carta escrita** — e ela deveria ser a de DEP-GOV |
| **IC-5** | **A materia de I-6 da Carta de DEP-QAR nomeia apenas a Linha**, e o risco real inclui o **Comando**. A protecao existe, mas exige ler **duas** Cartas | **Media** | DEP-EXE | **Primeira emenda a Carta de DEP-QAR** — que exige **ato novo do Soberano**, por estar ratificada |
| **IC-6** | **A fronteira entre defeito de propagacao e violacao de norma nao estava escrita.** CX-6 a estabeleceu — *violacao exige norma nomeavel* —, e ela vive **apenas nesta revisao** | Baixa | DEP-GOV | Terceiro caso da familia, **ou** primeira duvida real sobre abrir incidente |
| **IC-7** | **Fusao DEP-KMS + DEP-TLS e a unica do sistema que nenhuma norma proibe**, e falta apenas sinal. O acervo nao separava *"proibido"* de *"ainda sem sinal"* | Baixa | DEP-EXE | 1a revisao estrutural |
| **IC-8** | **Divergencia aritmetica preexistente no catalogo mestre §5.** A linha Cognitiva declara **9** tipos e enumera **10**; o total por enumeracao da **34**, contra os **33** de FND-10 §4. E `Memoria EST` constava **sem instancia** embora MEM-EST-0001 esteja listado em §4.7 do **mesmo** catalogo | **Media** | DEP-GOV | ✅ **Parcialmente corrigido** — `Memoria EST` movida para com-instancia. A aritmetica **permanece aberta**: gatilho na proxima emenda a FND-10 §4, ou 1a instancia de `Handoff`, `Reporte`, `Consulta` ou `Alerta` |

**Achados: 8 · corrigidos nesta revisao: 1 · parcialmente corrigidos: 1 · abertos com dono e
gatilho: 6 · sem destino: 0.**

> **IC-8 nao foi encontrado por nenhum cenario nem pela varredura C11** — apareceu ao
> **atualizar o catalogo** para registrar a primeira instancia de `Diretiva`. **Terceira missao
> seguida em que o defeito de maior alcance vem de executar a propagacao, e nao de auditar**:
> DR-8 veio da propagacao aos indices, IC-1 de abrir o template, IC-8 de somar a tabela de
> cobertura. Registrado como sinal: **a auditoria por varredura tem um ponto cego sistematico —
> ela confere projecao contra fonte, e nao confere a fonte contra si mesma.**

> **IC-1 e o achado mais significativo, e ele nao foi encontrado por nenhum cenario.** Apareceu
> ao **abrir o template para escrever a terceira Carta** — a mesma origem de DR-8, que apareceu
> na propagacao aos indices. **Duas missoes seguidas, o defeito mais grave veio de executar a
> propagacao, nao de auditar.**

## 8. Reconciliacao de ressalvas e achados abertos

> Todas as ressalvas de aptidao abertas e todos os achados de Departamento sao reconciliados:
> fechados com evidencia, mantidos com dono, gatilho e custo, ou escalados.

| Origem | Ressalva / achado | Gatilho disparou? | **Tratamento** |
|---|---|---|---|
| **FIT-2026-005 R4** | Os dois pilotos nao estao em vigor | **Sim** — ato do Soberano | ✅ **FECHADA** — §8.1 |
| **FIT-2026-005 R2** | Validado em 2 de 4 classes | **Sim** — 1a Carta de Plataforma | ✅ **FECHADA** — §8.2 |
| **FIT-2026-005 R1** | 10 de 10 regras exercidas, mas **por construcao** | **Sim** — terceira Carta escrita | **Mantida, medida e com o criterio corrigido** — §8.3 |
| **FIT-2026-005 R3** | 5o ciclo de crescimento sem consolidacao | **Sim** — proxima mudanca C2/C3 | **Mantida e ESCALADA** — §8.4 |
| **FIT-2026-005 R5** | Duas ressalvas atravessam 5 ciclos sem gatilho disparar | **Sim** — proxima mudanca C2/C3 | **Mantida e ESCALADA ao SOBERANO** — §8.5 |
| **FIT-2026-004 R1** | 32 regras novas; 15 sem exercicio possivel | **Nao** — sob o criterio corrigido | **Nao-avaliavel** — §8.6 |
| **FIT-2026-004 R2** | Tres abstracoes com zero membros | **Nao** — sob o criterio corrigido | **Nao-avaliavel** — §8.6 |
| **FIT-2026-004 R4** | MEM-EST-0001 permanece `aprovado` | **Nao** — o ato de 2026-07-28 **o exclui expressamente** | **Mantida e reescalada ao SOBERANO** |
| FIT-2026-001 R1 · R3 · FIT-2026-002 R1 · R3 · FIT-2026-003 R1 · R2 | Diversas | **Nao** — gatilho e a 1a ou 2a revisao estrutural | **Mantidas.** Donos inalterados; incluidas na escalada de §8.5 |
| **FIT-2026-002 R4** | Reducao de contexto calculada, nao observada | **Sim** — quarta medicao | **Mantida, com progresso medido pela 1a vez:** a 4a medicao **desce** — 18,5% contra 30,6%. **Nao fecha:** um ponto nao e tendencia, e parte da queda vem da natureza da missao (FIT-2026-006 §F5) |
| **DR-1** | Gatilho de R1 de FIT-2026-004 produz falso positivo | **Sim** | ✅ **CORRIGIDO** — regra de medicao 1, §8.6 |
| **DR-2** | R2 e R4 de FIT-2026-004 acopladas | **Sim** | ✅ **CORRIGIDO** — regra de medicao 2, §8.6 |
| **DR-3** | `departments/<dep>` ambiguo em FND-03 §7 | **Sim** — terceira Carta | ✅ **FECHADO** — §8.7 |
| **DR-6** | Medicao autorreferente sem regra escrita | **Sim** — terceira Carta | ✅ **FECHADO** — regra escrita em `DEP-KMS §13.2` |
| **DR-4** | `departments/` sem indice | **Nao** — gatilho e a **quinta** Carta; ha **quatro** | **Mantido.** Dono DEP-GOV |
| **DR-5** | Contrato validado em 2 de 4 classes | **Sim** | ✅ **FECHADO** — quatro classes exercidas (§3) |
| **DR-8** | Licao declarada que nao chega ao registro-fonte | **Sim** — a cada `FIT` | **Mantido, e materializado** como criterio de QG-5 em `DEP-KMS §5.2` |
| **P1** | Um unico membro de OW-02 | **Sim** — 3a Carta | **Mantido, com o membro agora declarado dos dois lados** (CX-2) |
| **P6** | VC-03 dispara em DEP-ENG e DEP-EXE | **Sim** — Carta de DEP-EXE | **Mantido, com a avaliacao feita** — `DEP-EXE §12.1`, decisao de **nao** dividir |
| **P2** | Divergencia aparente na camada de memoria | **Nao** — 1a revisao estrutural | **Mantido**, e agora **declarado na Carta do dono** (`DEP-KMS §2` e §9) |
| P3 · P4 · P5 · P7 · P8 | Divergencias aparentes e assimetrias | **Nao** | **Mantidos.** Donos e gatilhos inalterados |
| **C5** de REV-CONSOLIDACAO | Impedimento cruzado | **Sim** — **2a ocorrencia** (CX-3) | **Mantido e reforcado**: a 2a ocorrencia esta registrada; dono DEP-GOV |

**Resultado: 5 fechadas ou corrigidas · 2 declaradas nao-avaliaveis · 3 escaladas · as demais
mantidas com dono, gatilho e custo. Nenhuma ficou sem destino.**

### 8.1 FIT-2026-005 R4 — **fechada**

| Campo | Conteudo |
|---|---|
| Texto | *"Os dois pilotos nao estao em vigor. O rollout esta bloqueado por ato que a missao nao pode produzir"* |
| Gatilho | *"Ato do Soberano sobre as duas Cartas — aprovacao e ratificacao no mesmo ato"* — **disparado** |
| **Evidencia** | [MSG-2026-0001](../memory/operacional/MSG-2026-0001-ato-soberano-ratificacao-cartas-piloto.md): ato explicito, datado, nominal, com condicao de eficacia **verificada por tres vias** (§2.2). Ambas as Cartas em `ativo`, `ratificacao: ratificada` |
| **O que nao fecha com ela** | A retencao de **MEM-EST-0001**, que o ato **exclui expressamente** — R4 de FIT-2026-004 permanece aberta. Fecha-se a ressalva sobre **as Cartas**, nao sobre a familia |
| Dono | DEP-GOV |

### 8.2 FIT-2026-005 R2 — **fechada**

| Campo | Conteudo |
|---|---|
| Texto | *"Validado em 2 de 4 classes. Comando e Plataforma ficam sem piloto. DEP-EXE e autor de todas as Cartas e sera objeto da propria — impedimento que nenhum piloto testou"* |
| Gatilho | *"Primeira Carta de classe Plataforma"* — **disparado** |
| **Evidencia** | **Quatro** classes exercidas em **oito** cenarios (§3.9). O impedimento de DEP-EXE foi **exercido**, nao descrito: CX-3 **mudou o aprovador desta missao**. A validacao interclasses encontrou **dois defeitos que a intraclasse nao encontraria** — IC-4 e IC-5 |
| **O que nao fecha com ela** | A **cobertura por departamento**: 4 de 9 tem Carta, e **DEP-GOV** — o revisor de todas — nao tem. Isso e o achado **IC-4**, novo, e nao se herda a ressalva antiga para parecer que o problema sumiu |
| Dono | DEP-EXE |

### 8.3 FIT-2026-005 R1 — mantida, medida, criterio corrigido

| Campo | Conteudo |
|---|---|
| Gatilho | *"Terceira Carta escrita. Se ela passar no checklist sem nenhum item devolvido, a regra e frouxa ou o autor e o mesmo"* — **disparado duas vezes** |
| **Medicao de devolucoes** | **1 item devolvido** — a conferencia cruzada **B4 × B9**, que **nao existia no checklist** por causa de IC-1 e teve de ser acrescentada antes de as Cartas serem verificaveis. Nas quatro Cartas, **zero** itens de conteudo devolvidos |
| A condicao literal foi atingida? | **Parcialmente.** Zero devolucoes de **conteudo**; **uma** devolucao de **instrumento** |
| **Por que nao fecha** | **O autor continua sendo o mesmo** — DEP-EXE escreveu 4 de 4. A ressalva pergunta se o contrato **barra** o que consegue **produzir**, e isso permanece sem resposta: nenhuma Carta foi escrita por terceiro |
| **Achado sobre o proprio gatilho** | O gatilho mede **devolucoes**, e supoe que devolucao venha do **conteudo**. A unica devolucao real veio do **instrumento de verificacao** — IC-1. Um checklist incompleto produz **zero devolucoes** e parece regra frouxa, quando e **regra ausente**. Registrado como componente de IC-1 |
| Tratamento | **Mantida.** Dono **DEP-EXE**; gatilho reformulado: *"primeira Carta escrita por autor distinto de DEP-EXE"* — que exige **IC-3** resolvido ou a existencia de agentes |

### 8.4 FIT-2026-005 R3 — mantida e **escalada**: a consolidacao e aberta

| Campo | Conteudo |
|---|---|
| Texto | *"Quinta missao consecutiva de crescimento. Nenhuma consolidacao ocorreu em nenhum dos cinco ciclos"* |
| Gatilho | *"Proxima mudanca C2/C3. **Se a sexta tambem crescer sem nenhuma consolidacao, aplicar EV-08 aos candidatos mais antigos**"* — **disparado** |
| **Medicao** | Esta e a **sexta** missao consecutiva de crescimento. Numeros em [FIT-2026-006 §F1](../governance/fitness/FIT-2026-006-validacao-interclasses.md) |
| **Consolidacoes ocorridas em seis ciclos** | **0** — medido em `DEP-EXE §11, KX-8` |
| **A condicao foi atingida?** | **Sim, integralmente** |
| **Acao** | **A proposta de consolidacao (EV-08) e ABERTA**, e nao adiada. Quem a abre e **DEP-EXE** (X-12), e a autoridade esta declarada na Carta que esta missao escreveu. Candidatos e criterio em [FIT-2026-006 §Consolidacao](../governance/fitness/FIT-2026-006-validacao-interclasses.md) |
| **O que esta missao NAO faz** | **Nao executa** a consolidacao. Fundir, aposentar ou dividir artefato e mudanca com rito proprio e **fora do escopo desta missao**. Abrir a proposta e o ato que R3 exige; executa-la seria exceder o mandato |
| Dono | DEP-EXE |

### 8.5 FIT-2026-005 R5 — mantida e **escalada ao SOBERANO**

| Campo | Conteudo |
|---|---|
| Texto | *"Duas ressalvas atravessam cinco ciclos sem que o gatilho dispare. A 1a revisao estrutural e o gatilho de 6 das 13 ressalvas abertas"* |
| Gatilho | *"Fim do 1o horizonte, ou a proxima mudanca C2/C3 — o que vier antes. **Se a revisao estrutural nao for agendada ate la, escalar ao Soberano**"* — **disparado** |
| **Medicao** | A 1a revisao estrutural **nao foi agendada** em **seis** ciclos. Ressalvas e achados cujo gatilho e a 1a ou 2a revisao estrutural: **FIT-2026-001 R1 e R3 · FIT-2026-002 R1 e R3 · FIT-2026-003 R1 e R2 · P2 · P3 · P4 · P5 · P7 · P8** |
| **A condicao foi atingida?** | **Sim** |
| **Acao** | **ESCALADO AO SOBERANO**, conforme a propria ressalva determina. O ponto de decisao esta em [FIT-2026-006 §Pendencias para o Soberano](../governance/fitness/FIT-2026-006-validacao-interclasses.md) |
| **Por que isto importa** | **Gatilho que nunca dispara e divida perpetua com aparencia de controle.** Doze itens dependem de um evento que seis ciclos nao produziram. A escalada nao pede que a revisao ocorra agora: pede **decisao sobre quando** |
| Dono | DEP-EXE com DEP-GOV; **decisao: SOBERANO** |

### 8.6 R1 e R2 de FIT-2026-004 — **nao-avaliaveis** sob as regras corrigidas

> As duas correcoes determinadas para esta missao sao **instituidas** em
> [FIT-2026-006 §Regras de medicao](../governance/fitness/FIT-2026-006-validacao-interclasses.md)
> — **e nao aqui**, porque `FIT-2026-005` e `FIT-2026-004` sao **M1** e nao se editam
> (FND-10 §6.2; MEM-APR-0003). Corrigir a regra no **novo** `FIT` e o unico caminho conforme.

| Ressalva | Sob a regra antiga | **Sob a regra corrigida** |
|---|---|---|
| **R1** — *"medir quantas das 28 regras `CT` foram exercidas; menos de um terco abre consolidacao"* | **0 de 28** → condicao literal atingida → falso positivo, **como DR-1 previu** | **Nao-avaliavel.** Esta missao **nao registra afirmacao sobre o Soberano**; a materia esta **fora do dominio aplicavel**, e ausencia fora do dominio **nao e ocorrencia negativa** |
| **R2** — *"tres abstracoes com zero membros; gatilho: primeiro componente criado"* | **0 consumidores** → parece abstracao inutil | **Nao-avaliavel.** As tres dependem de `MEM-EST-0001`, que o ato de 2026-07-28 **exclui expressamente** e que permanece **inativo**. Regra dependente de memoria inativa nao conta **nem como falha nem como aprovacao** |

**Efeito:** **DR-1 e DR-2 fecham** — os dois achados pediam exatamente esta reformulacao. As
ressalvas **permanecem abertas**, com o estado corrigido de *"falha aparente"* para
**`nao-avaliavel`**, e gatilho reformulado para *"primeira missao que **toque a materia**"* (R1) e
*"primeiro componente criado **apos a entrada em vigor** do registro"* (R2).

> **O que a correcao evita, concretamente.** Sob a regra antiga, esta missao mediria **0 de 28**
> pela **segunda vez consecutiva** e abriria proposta de consolidacao contra as 28 regras `CT`
> — usando como fundamento o fato de a missao ter sido **sobre outro assunto**. A proposta
> mediria a coisa errada, e a decisao dela decorrente atingiria um contrato que nunca foi
> exercido.

### 8.7 DR-3 — **fechado**

| Campo | Conteudo |
|---|---|
| Achado | *"`departments/<dep>` e ambiguo em FND-03 §7: nao diz se `<dep>` e o codigo em minusculas ou o ID completo"* |
| Gatilho | *"Terceira Carta, ou primeira Carta de agente"* — **disparado** |
| **Evidencia do fechamento** | **Quatro** instancias, **100%** consistentes: `qar`, `eng`, `exe`, `kms` — codigo em minusculas, nunca o ID completo. A regra ja estava escrita em `TPL-carta-departamento` §Instrucoes de uso, item 1: *"`<dep>` e o **codigo do departamento em minusculas**"* |
| **Por que fecha** | O achado apontava ambiguidade **sem decisao registrada**. A decisao **esta registrada no template**, que e o instrumento que a materializa, e **quatro** instancias a confirmam sem excecao |
| **O que nao fecha com ele** | **DR-4** — se `departments/` recebe indice — permanece aberto; sao perguntas distintas |
| Dono | DEP-GOV |

## 9. Varredura C11 — os indices contra as fontes

Acao **C11** de REV-CONSOLIDACAO §10: *"varredura de todos os indices contra as fontes que
projetam, a cada encerramento de C2/C3"*. Dono DEP-GOV.

| # | Indice | Indexa | Conferido contra | Resultado |
|---|---|---|---|---|
| 1 | `README.md` *(raiz)* | o acervo | Contagens e catalogo mestre | **Atualizado** — 4 Cartas, estado dos pilotos |
| 2 | `foundation/README.md` | `FND` e `TPL` | 10 `FND` + 19 `TPL` em disco | **Conforme, sem alteracao** — nao lista versao de template nem revisao arquitetural; nada a atualizar |
| 3 | `decisions/README.md` | `ADR` | 11 arquivos `ADR-*` | **Conforme, sem alteracao** — nenhum ADR novo |
| 4 | `rfcs/README.md` | `RFC` | 8 arquivos `RFC-*` | **Conforme, sem alteracao** |
| 5 | `capabilities/README.md` | `CAP` | 23 arquivos; frontmatter conferido | **Conforme** — §10 inalterada; **nenhuma Carta de Capability tocada** |
| 6 | `governance/README.md` | `EXC` `INC` `FIT` | 0 · 2 · 12 | **Atualizado** |
| 7 | `governance/exceptions/README.md` | `EXC` | 0 arquivos | **Conforme** — nenhuma excecao vigente (CX-6) |
| 8 | `governance/incidents/README.md` | `INC` | 2 arquivos | **Conforme** — **nenhum incidente aberto nesta missao** (CX-6) |
| 9 | `governance/fitness/README.md` | `FIT` | 6 `FIT` + 7 `REV` | **Atualizado** — FIT-2026-006, contador **006** |
| 10 | `governance/artifact-registry.md` | o acervo | Arquivo a arquivo | **Atualizado** — v1.4.0, baseline `BL-2026-07-28-04` |
| 11 | `memory/README.md` | as 5 camadas | **7** registros — 1 EST + 1 OPR + 4 APR + 1 MSG | **Atualizado** |
| 12 | `memory/operacional/README.md` | `OPR` | **1** registro — MSG-2026-0001 | **Atualizado** — primeira instancia da camada |
| 13 | `memory/aprendizado/README.md` | `APR` | 4 arquivos | **Conforme** — nenhum registro APR novo criado |
| 14 | `memory/estrategica/README.md` | `EST` | 1 registro | **Conforme** — MEM-EST-0001 inalterado |
| 15 | `memory/produto/README.md` | `PRD` | 0 registros | **Conforme** |
| 16 | `memory/tecnica/README.md` | `TEC` | 0 registros | **Conforme** |
| 17 | `departments/` | `DEP` | 4 subdiretorios | **Sem indice, por decisao** — DR-4 aberto, gatilho na **quinta** Carta |

**17 varridos · 8 atualizados como parte desta mudanca** (IX-02, CV-04).

**Nenhuma divergencia indice × fonte encontrada.** A unica divergencia da missao — **IC-1** — nao
e indice contra fonte: e **correcao declarada contra artefato corrigido**, e por isso a varredura
C11 **nao a encontraria**. Registrado: C11 cobre projecao, **nao cobre propagacao de correcao**.

### 9.1 Integridade referencial

| Verificacao | Metodo | Resultado |
|---|---|---|
| Links relativos quebrados | Varredura por ferramenta sobre **todos** os `.md`, resolvendo cada caminho contra o disco | **0 quebrados** em **1.008** links verificados |
| Vinculo a Capability valido (VC-01) | `capabilities` das quatro Cartas contra o catalogo | **15 vinculos**, todos a Capability `ativo`; nenhuma `proposta` ou `aposentada` |
| Relacao fora dos pares permitidos (RM-02) | `custodia` e `exerce` DEP→CAP contra FND-09 §6.2 | **Conforme.** `DEP → DEP` **nao** declarado como relacao |
| Ciclo em `depende-de` | Grafo de Capabilities | **Sem ciclo** — nenhuma Carta de Capability tocada |
| Dependencia ascendente (PD-11) | Estrato 3 *(DEP)* → estrato 2 *(CAP)* | **Conforme** |
| **Autoverificacao** | Papel de executor × produtor, em cada artefato desta missao | **0 ocorrencias** — §4 |
| Credencial em texto (PI-08, LV-02) | Varredura dos artefatos novos e alterados | **0 ocorrencias** |

## 10. Reconciliacao catalogo-fonte

| Verificacao | Resultado |
|---|---|
| Todo artefato novo tem entrada no catalogo mestre (RG-02) | **4 de 4** — MSG-2026-0001, DEP-EXE, DEP-KMS, REV-INTERCLASSES, FIT-2026-006 |
| Todo artefato alterado tem a linha atualizada | **3 de 3** — `TPL-carta-departamento`, `DEP-QAR`, `DEP-ENG` |
| Contagem do catalogo × contagem em disco | Conferida em [FIT-2026-006 §F1](../governance/fitness/FIT-2026-006-validacao-interclasses.md) |
| Estado de ratificacao × fonte canonica | Projecao do catalogo conferida contra **MSG-2026-0001**, fonte unica (PJ-03) |
| Proveniencia | **100% `native`** — nenhum conteudo externo admitido |
| Baselines `BL-01`, `BL-02`, `BL-03` editadas? | **Nao.** `BL-03` teve a integridade **conferida antes** de qualquer edicao desta missao, e nao foi tocada depois (BL-02) |
| Nova medicao recebeu identidade nova? | **Sim** — `BL-2026-07-28-04` |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-QAR | Revisao inicial: verificacao da ativacao dos dois pilotos sob o ato soberano por **tres vias independentes**; **oito** cenarios interclasses nas **quatro** classes, com **3** defeitos encontrados *(1 corrigido)*; comparacao unica das quatro classes separando regra universal, de classe e diferenca acidental; pacote de ratificacao dos dois novos pilotos com recomendacao **APROVAR** para ambos; **8** achados; reconciliacao com **5** fechamentos, **2** ressalvas declaradas `nao-avaliaveis` e **3** escaladas; varredura C11 de **17** indices; **0** links quebrados; **0** autoverificacoes. Aprovada por **DEP-GOV** por impedimento declarado de DEP-EXE. |
