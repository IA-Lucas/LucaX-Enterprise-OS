---
id: INC-2026-001-ratificacao-inferida
titulo: Ratificacao C3/Tipo 1 registrada por inferencia a partir de instrucao generica em ADR-0001 a ADR-0004
tipo: relatorio
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-QAR
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: null
decisoes_relacionadas: [ADR-0001, ADR-0002, ADR-0003, ADR-0004, ADR-0006]
substitui: []
substituido_por: null
norma_violada: [PI-01, PI-06, GV-05, CM-07, LV-05]
severidade: alta
efeito: Quatro decisoes C3/Tipo 1 registram ratificacao do Soberano que nao ocorreu como ato explicito sobre o texto ratificado
causa: Precedente estabelecido em ADR-0001 e replicado nos tres ADRs seguintes
situacao: fechado
resumo: Registra, contem e encerra a ratificacao inferida em ADR-0001 a ADR-0004, e guarda o ato soberano de 2026-07-28 que a regularizou.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# INC-2026-001: Ratificacao inferida em ADR-0001 a ADR-0004

## Proposito
Registrar que os quatro ADRs de classe C3 e Tipo 1 vigentes declaram ratificacao do Soberano
apoiada em **instrucao generica anterior**, e nao em ato explicito sobre o texto ratificado —
e conter o efeito sem editar registro historico.

## Escopo
| Item | Definicao |
|---|---|
| Inclui | ADR-0001, ADR-0002, ADR-0003 e ADR-0004; os documentos fundacionais cuja eficacia deles depende |
| Nao inclui | ADR-0005 (C2/Tipo 2 — nao exige ratificacao); o merito de qualquer decisao |
| Instrumento | Incidente de conformidade, FND-04 §10 |

## Responsaveis
| Papel | Quem |
|---|---|
| Detectado por | **SOBERANO**, na abertura da Missao 1.3 |
| Registra | DEP-GOV |
| Verifica o fechamento | **DEP-QAR** — independente de DEP-GOV (RM-06b, ADR-0005) |
| Grava o aprendizado | DEP-KMS |
| Unico que pode encerrar | **SOBERANO** — so o ato de ratificacao regulariza |

---

## 1. Fato

Os quatro ADRs de classe C3 e Tipo 1 vigentes contem secao "Ratificacao do Soberano"
preenchida com data, forma e texto invocado. Em todos, a forma declarada e
*"determinacao direta e escrita"* anterior ao texto ratificado.

| ADR | Texto invocado como ratificacao | Momento do ato invocado |
|---|---|---|
| ADR-0001 | *"Os documentos produzidos passarao a ser a unica fonte oficial de verdade para as proximas fases da transformacao."* | **Antes** da producao dos documentos |
| ADR-0002 | *"Nenhum Departamento, Agente, Skill, Workflow ou Produto podera existir sem estar vinculado a pelo menos uma Capability."* | **Antes** do catalogo e de FND-08 |
| ADR-0003 | *"Nenhum novo Framework podera introduzir uma entidade estrutural sem obedecer ao Meta Model."* | **Antes** de FND-09 |
| ADR-0004 | *"Alem do Architecture Review, cada Mission encerraria com uma verificacao de saude da arquitetura."* | **Antes** do mecanismo, do portao e do veredito |

Os quatro reconhecem a fragilidade em "Observacao de conformidade (DEP-GOV)" e mantem o
campo **"Confirmado apos leitura?"** em branco — nos quatro, ate esta data.

## 2. Norma violada

| Norma | Texto | Como foi contrariada |
|---|---|---|
| **PI-06** | Mudanca Tipo 1 exige aprovacao humana explicita e plano de reversao **antes** da execucao | A aprovacao humana sobre o texto executado nao ocorreu |
| **PI-01** | Nenhum agente pode interpretar silencio como aprovacao | Instrucao generica anterior foi tratada como aprovacao do texto especifico |
| **GV-05** | Aprovacao e ato explicito e datado. **Silencio nunca aprova** | A data registrada e a da instrucao originadora, nao a de um ato sobre o resultado |
| **CM-07** | Ausencia de resposta nunca significa aceite | O campo "Confirmado apos leitura?" em branco foi tratado como ressalva, nao como ausencia de ratificacao |
| **LV-05** | Reportar como concluido ou verificado algo que nao foi | Os ADRs afirmam **"Ratificado por: SOBERANO"** — afirmacao de fato que nao se sustenta |

> A violacao mais grave e **LV-05**, que nao admite excecao (FND-01 §8.3). O campo
> "Ratificado por" nao registra ressalva: registra fato. E o fato nao ocorreu na forma
> declarada.

## 3. Efeito atual

| Artefato | Estado documental | Eficacia |
|---|---|---|
| ADR-0001 a ADR-0004 | `ativo` | **Condicionada** — ratificacao pendente |
| FND-01 a FND-10 | `ativo` / `aprovado` | Vigoram de fato; eficacia herda a pendencia |
| 23 Cartas de Capability | `ativo` | Vigoram de fato; eficacia herda a pendencia de ADR-0002 |
| ADR-0005 | `ativo` | **Integra** — C2/Tipo 2, nao exige ratificacao |

**Nenhum componente foi criado** sob essas decisoes: nao ha departamento, agente, subagente,
skill, workflow, ferramenta, produto nem projeto. O efeito pratico da pendencia esta,
portanto, contido ao corpo normativo.

## 4. Contencao aplicada

FND-04 §10.2 etapa 3 admite **isolar quando reverter nao for possivel**. Reverter significaria
revogar toda a Fundacao — desproporcional, destrutivo e vedado sem copia datada (PI-07,
LV-01). Aplica-se isolamento:

| # | Medida | Onde |
|---|---|---|
| C1 | Campo `ratificacao: pendente` acrescentado ao frontmatter dos **documentos fundacionais** afetados | FND-08, FND-09, FND-10 |
| C2 | Coluna **Ratificacao** acrescentada ao indice oficial de decisoes | `decisions/README.md` |
| C3 | **Proibicao de nova inferencia**: nenhum ADR futuro registra ratificacao sem ato explicito sobre o texto final | FND-10 §5.4 e este registro |
| C4 | FND-10, produzido nesta missao, nasce em estado `aprovado` — **nao** `ativo` — aguardando ratificacao | `foundation/10-artifact-framework.md` |
| C5 | **ADR historico nao e editado** (LV-04, e determinacao expressa do Soberano na Missao 1.3) | — |

### 4.1 O que **nao** foi feito, e por que

| Nao feito | Motivo |
|---|---|
| Editar a secao "Ratificacao" dos quatro ADRs | LV-04 proibe alterar registro de decisao aprovado; o Soberano determinou expressamente "sem editar ADR historico" |
| Alterar `status` de `ativo` para `aprovado` nos quatro ADRs | Seria tecnicamente correto — `aprovado` significa "aceito, aguarda entrada em vigor" —, mas exige tocar o arquivo historico. **Decisao do Soberano**, registrada em §7 como pendencia |
| Suspender a Fundacao | Desproporcional; nenhum componente foi criado; o dano potencial e menor que o da suspensao |

## 5. Causa

**Causa raiz: precedente normativo replicado sem reexame.**

```
ADR-0001  estabelece o padrao "ratificacao apoiada em determinacao originadora"
    |     e registra a fragilidade como ressalva, nao como impedimento
    v
ADR-0002  copia o padrao e a ressalva
    v
ADR-0003  copia o padrao e a ressalva
    v
ADR-0004  copia o padrao, a ressalva e acrescenta uma segunda ressalva
          (escolhas de forma nao determinadas pelo Soberano)
```

Tres fatores concorreram:

| # | Fator | Natureza |
|---|---|---|
| F1 | A ressalva escrita em ADR-0001 **descrevia corretamente o problema** e mesmo assim concluia pela eficacia — tratou uma condicao de validade como observacao | Falha de **compreensao** da norma |
| F2 | Nenhuma auditoria vigente verifica se a ratificacao declarada corresponde a ato real | Falha de **instrumento** |
| F3 | O executor produziu o ADR **e** preencheu a propria secao de ratificacao — nao ha etapa em que outro papel confirme o ato do Soberano | Falha de **norma**: o rito de FND-04 §4 nao separa "registrar a ratificacao" de "obter a ratificacao" |

> Pela taxonomia de FND-04 §10.2 etapa 4, a causa e simultaneamente de **norma**, de
> **instrumento** e de **compreensao**. Corrigir apenas a compreensao — "nao fazer de novo" —
> deixaria F2 e F3 intactos, e o incidente se repetiria.

## 6. Correcao

### 6.1 Correcao do efeito
Isolamento aplicado em §4. O efeito so e integralmente corrigido pelo ato do Soberano (§7).

### 6.2 Correcao da causa

| Causa | Correcao | Onde | Estado |
|---|---|---|---|
| F1 compreensao | Declarar que ratificacao ausente e **impedimento**, nao ressalva: sem ato explicito, a decisao permanece `aprovado` e nao entra em `ativo` | FND-10 §5.4 | **Feito** |
| F2 instrumento | Nova verificacao de auditoria: *"Ratificacao declarada corresponde a ato explicito sobre o texto final?"* | FND-04 §8 | **Feito** |
| F3 norma | Etapa [6] do ciclo de mudanca passa a distinguir **obter** de **registrar** a ratificacao; o registro e feito por papel distinto do executor | FND-04 §4 e §4.1 (CV-09) | **Feito** |

## 7. Pendencia para o Soberano

Duas decisoes cabem exclusivamente ao Soberano, e **nao** foram presumidas:

| # | Decisao pendente | Opcoes |
|---|---|---|
| P1 | **Ratificar ou recusar** ADR-0001 a ADR-0004 | (a) ratificar os quatro em ato unico e datado; (b) ratificar alguns; (c) recusar — cada recusado e **superado** pelo rito de FND-07 §7, nunca editado |
| P2 | **Estado documental** dos quatro enquanto a ratificacao nao ocorrer | (a) manter `ativo` com pendencia declarada — situacao atual; (b) rebaixar a `aprovado`, o que exige tocar o frontmatter dos ADRs historicos |

> **Recomendacao de DEP-GOV para P2:** manter `ativo` (opcao a). Rebaixar exigiria editar
> arquivo historico, e o ganho seria simbolico: a pendencia ja esta visivel no indice, no
> frontmatter dos documentos fundacionais e neste registro.

> **Recomendacao de DEP-QAR para P1:** ratificar em **ato unico**, referenciando este
> incidente pelo ID. Ratificacao dispersa em quatro atos reabriria a duvida sobre qual texto
> foi lido.

### 7.1 Sobre o termo "Fundador"

A Missao 1.3 usa **Fundador** onde a Constituicao usa **Soberano**. LX-07 proibe sinonimo em
documento normativo. Registra-se: os dois designam a mesma autoridade — Lucas —, e o termo
oficial permanece `SOBERANO` (FND-01 §11). Alterar o termo oficial seria emenda **C3**.

## 8. Aprendizado

| Registro | Conteudo |
|---|---|
| [MEM-APR-0001](../../memory/aprendizado/MEM-APR-0001-ratificacao-por-precedente.md) | **Ressalva escrita nao neutraliza condicao de validade.** Um documento que descreve corretamente por que pode estar irregular e ainda assim se declara valido propaga o defeito com aparencia de rigor |

## 9. Fechamento

| Campo | Conteudo |
|---|---|
| Situacao | **`fechado`** — efeito corrigido pelo ato de §11; causa corrigida em tres frentes (§6.2) |
| Como chegou a `corrigido` | Ato soberano explicito e datado de 2026-07-28, registrado em **§11** |
| Como chegou a `fechado` | Verificacao independente de DEP-QAR em **§12** (FND-04 §10.2 etapa 7) |
| Quem fechou | DEP-QAR, em 2026-07-28 |
| Prazo | Nao se aplica — encerrado |

> **Trilha da situacao:** `aberto` → `contido` (2026-07-28, §4) → `corrigido` (2026-07-28,
> §11) → `fechado` (2026-07-28, §12). Cada transicao e ato registrado com responsavel e data
> (LC-01). A partir do fechamento este registro e **imutavel** (M1, FND-10 §6.2).

> **Incidente nao e punicao — e informacao** (FND-04 §10). Este registro existe porque a
> alternativa — corrigir em silencio — seria ela propria violacao de LV-11.

## 10. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Origem | Determinacao do Soberano na abertura da Missao 1.3: *"Ratificacao C3/Tipo 1 nao pode ser inferida de instrucao generica"* |
| Artefatos afetados | ADR-0001, ADR-0002, ADR-0003, ADR-0004 e todos os documentos fundacionais deles derivados |
| Artefatos alterados | `decisions/README.md`; frontmatter de FND-08, FND-09, FND-10; FND-04 §4 e §8 |
| Artefatos alterados no encerramento (Missao 1.4) | `decisions/README.md` (coluna Ratificacao); frontmatter de FND-01, FND-03, FND-04, FND-08, FND-09 e FND-10; `status` de FND-10; `README.md` da raiz; catalogo mestre §6. **Nenhum arquivo de ADR foi tocado** |
| Decisao relacionada | [ADR-0006](../../decisions/ADR-0006-adocao-do-enterprise-artifact-framework.md) — nasce com ratificacao **declaradamente pendente**, aplicando a correcao F1 |
| Aprendizado | [MEM-APR-0001](../../memory/aprendizado/MEM-APR-0001-ratificacao-por-precedente.md) · [MEM-APR-0003](../../memory/aprendizado/MEM-APR-0003-campo-de-estado-em-artefato-imutavel.md) |

---

## 11. Ato de ratificacao do Soberano — fonte canonica

> **Esta secao e o registro unico do ato.** Indices, frontmatters e catalogo **referenciam**
> `INC-2026-001 §11`; nenhum deles reproduz o texto do ato (ADR-0008, regra PJ-01). Registrar
> em mais de um lugar criaria segunda fonte de verdade sobre um fato soberano.

### 11.1 O ato

| Campo | Conteudo |
|---|---|
| Autoridade | **SOBERANO** (Lucas) — indelegavel (FND-04 §3, papel Ratificador) |
| Forma | **Ato escrito, explicito e datado**, emitido diretamente ao sistema |
| Data do ato | **2026-07-28** |
| Objeto | O **texto final** de ADR-0001, ADR-0002, ADR-0003, ADR-0004 e ADR-0006 |
| Instrucao acessoria | Registro na fonte canonica aplicavel, **sem edicao retroativa dos ADRs historicos** |
| Autorizacao acessoria | Encerramento deste incidente **apos verificacao independente** do registro |

**Texto integral do ato, transcrito sem edicao:**

> ATO SOBERANO DO FUNDADOR — 2026-07-28
>
> Ratifico expressamente os ADR-0001, ADR-0002, ADR-0003, ADR-0004 e ADR-0006, reconhecendo
> seus conteudos, efeitos, ressalvas e consequencias normativas.
>
> Determino que esta ratificacao seja registrada na fonte canonica aplicavel, sem edicao
> retroativa dos ADRs historicos.
>
> Autorizo o encerramento do INC-2026-001 apos verificacao independente de que a ratificacao
> foi corretamente registrada e referenciada.

> **Sobre o termo "Fundador".** O ato usa `Fundador`; o termo oficial e `SOBERANO`
> (FND-01 §11). Designam a mesma autoridade — questao ja resolvida em §7.1. A transcricao
> preserva o termo usado pelo emissor; o registro normativo usa o termo oficial (LX-07).

### 11.2 Alcance — o que o ato ratifica e o que nao alcanca

| Decisao | Classe | Ratificada por este ato? | Efeito |
|---|---|---|---|
| ADR-0001 | C3 / Tipo 1 | **Sim** | Eficacia deixa de ser condicionada |
| ADR-0002 | C3 / Tipo 1 | **Sim** | Idem; alcanca as 23 Cartas de Capability que dele derivam |
| ADR-0003 | C3 / Tipo 1 | **Sim** | Idem; alcanca FND-09 |
| ADR-0004 | C3 / Tipo 1 | **Sim** | Idem; alcanca o portao QG-6 e a entidade `FIT` |
| ADR-0005 | C2 / Tipo 2 | Nao se aplica | **`nao-exigida`** desde a origem — nunca esteve pendente (§3) |
| ADR-0006 | C3 / Tipo 1 | **Sim** | Condicao de validade de LM-02 satisfeita; **FND-10 entra em vigor** |

**Nao alcanca**, por nao constar do ato: nenhuma outra decisao, nenhum artefato futuro e
nenhuma ratificacao antecipada. Ratificacao nao se estende por analogia (LM-03).

### 11.3 Efeitos aplicados

| # | Efeito | Onde | Observacao |
|---|---|---|---|
| E1 | Coluna **Ratificacao** passa de `pendente` a `ratificada` nas cinco decisoes | [`decisions/README.md`](../../decisions/README.md) | Projecao declarada desta secao |
| E2 | Campo `ratificacao: ratificada` em FND-01, FND-03, FND-04, FND-08, FND-09 e FND-10 | frontmatter | Artefatos **M2**, versionaveis — alteracao permitida |
| E3 | **FND-10 transita de `aprovado` para `ativo`** (operacao O4, FND-10 §5.2) | `foundation/10-artifact-framework.md` | Condicao de LM-02 satisfeita |
| E4 | Aviso de ratificacao pendente removido do indice mestre | [`README.md`](../../README.md) | O aviso descrevia estado que deixou de existir |
| E5 | Linha de rastreabilidade do catalogo atualizada | [catalogo mestre §6](../artifact-registry.md) | RG-03: catalogo desatualizado = mudanca incompleta |

### 11.4 O que deliberadamente **nao** foi feito

| Nao feito | Norma que o impede | Consequencia assumida |
|---|---|---|
| Editar `ratificacao` ou `status` no frontmatter dos **seis ADRs** | **CC-01** (FND-10 §6.2) e determinacao expressa do ato: *"sem edicao retroativa dos ADRs historicos"* | O frontmatter de cada ADR permanece **congelado no ato de aprovacao**. ADR-0006 continua declarando `aprovado` / `pendente` no proprio arquivo |
| Editar a secao "Ratificacao do Soberano" de ADR-0001 a ADR-0004 | **LV-04**, CC-01 | Os quatro continuam registrando a inferencia original. O registro correto e este §11, que os supera em fe publica |
| Presumir ratificacao de ADR-0005 | LM-03 | Nenhuma — ADR-0005 e `nao-exigida` desde a origem |

> **Defeito estrutural revelado por E2/E3 e por esta tabela.** `ratificacao` e um campo de
> **estado**, mas foi declarado obrigatorio em artefatos de classe **M1**, cujo conteudo nunca
> muda. Um campo de estado que nao pode ser atualizado no proprio artefato so pode ser lido
> como *estado no ato*, nunca como *estado corrente*. A regra que resolve isso — fonte unica e
> projecoes declaradas — foi instituida por [ADR-0008](../../decisions/ADR-0008-uma-fonte-multiplas-projecoes.md)
> e o aprendizado esta em [MEM-APR-0003](../../memory/aprendizado/MEM-APR-0003-campo-de-estado-em-artefato-imutavel.md).
> **A fonte corrente do estado de ratificacao e esta secao.**

### 11.5 Quem registrou

| Papel | Quem | Fundamento |
|---|---|---|
| Obteve a ratificacao | **SOBERANO**, por ato proprio | Ato indelegavel (FND-04 §3) |
| **Registrou** | **DEP-KMS** — Curador | CV-09 e LM-05: quem registra e papel **diverso do executor**. O executor das mudancas de FND-04, FND-08, FND-09, FND-10 e do proprio incidente foi **DEP-GOV** |
| Verificou | **DEP-QAR** — §12 | FND-04 §3.1: Executor ≠ Verificador |

> **Desvio deliberado da acao A1 de [REV-ARTIFACT-2026-07-28](../../foundation/revisao-arquitetural-artifact-framework-2026-07-28.md) §10.**
> Aquela revisao previa *"registro por DEP-QAR"*. Cumprir isso faria DEP-QAR **verificar o
> proprio registro** — precisamente o que ADR-0005 e PI-05 proibem. O registro passa a
> DEP-KMS, e DEP-QAR preserva a independencia da verificacao. Desvio registrado aqui em vez de
> executado em silencio (LV-11).

---

## 12. Verificacao independente de fechamento (DEP-QAR)

Executada por **DEP-QAR**, que **nao** produziu o registro de §11 (feito por DEP-KMS) nem as
correcoes de causa (feitas por DEP-GOV). FND-04 §10.2 etapa 7.

### 12.1 O efeito foi corrigido?

| # | Verificacao | Evidencia | Resultado |
|---|---|---|---|
| V1 | Existe ato **explicito** do Soberano? | §11.1, texto integral transcrito | **Sim** |
| V2 | O ato e **datado**? | 2026-07-28, declarado no proprio ato | **Sim** |
| V3 | O ato incide sobre o **texto final**, nao sobre instrucao generica anterior? | O ato nomeia as cinco decisoes por ID e declara reconhecer *"conteudos, efeitos, ressalvas e consequencias normativas"* — posterior a producao dos textos | **Sim** |
| V4 | O registro foi feito por papel **distinto do executor**? | DEP-KMS registrou; DEP-GOV executou (§11.5) | **Sim** (CV-09, LM-05) |
| V5 | O registro esta em **fonte unica**? | §11; demais artefatos referenciam por ID | **Sim** (PJ-01) |
| V6 | Nenhum ADR historico foi editado? | Verificado arquivo a arquivo: os seis ADRs mantem conteudo e frontmatter originais | **Sim** (LV-04, CC-01) |
| V7 | A ratificacao foi **referenciada** onde a pendencia era visivel? | `decisions/README.md`, `README.md` raiz, frontmatter dos seis FND, catalogo §6 | **Sim** (CV-04) |
| V8 | Alguma ratificacao foi **presumida** alem do ato? | Alcance conferido contra o texto: cinco decisoes nomeadas, nenhuma a mais | **Nao** (LM-03) |

### 12.2 A causa foi corrigida?

| Causa | Correcao | Exercida? | Verificacao |
|---|---|---|---|
| F1 — compreensao | LM-02 a LM-06 (FND-10 §5.4) | **Sim** | ADR-0006 permaneceu em `aprovado` ate o ato; a condicao de validade funcionou como impedimento, nao como ressalva |
| F2 — instrumento | Auditoria de eficacia de ratificacao (FND-04 §8) | **Sim** | Esta verificacao **e** a primeira execucao dessa auditoria |
| F3 — norma | CV-09 separa obter de registrar | **Sim** | §11.5: obtencao pelo Soberano, registro por DEP-KMS, verificacao por DEP-QAR — tres papeis distintos |

> **Primeira ratificacao efetiva registrada sob CV-09.** Isso dispara o gatilho da acao **A8**
> de REV-ARTIFACT §10: avaliar a elevacao de **LM-02** a norma constitucional. Avaliado na
> revisao arquitetural desta missao — mantida a recomendacao de **nao elevar**, por uma unica
> ocorrencia bem-sucedida nao ser serie.

### 12.3 Veredito de fechamento

| Campo | Conteudo |
|---|---|
| Efeito | **Corrigido** — as cinco decisoes tem ratificacao explicita, datada e registrada |
| Causa | **Corrigida e exercida** nas tres frentes |
| Residuo declarado | O frontmatter dos seis ADRs permanece congelado no ato de aprovacao (§11.4). Nao e defeito: e CC-01 aplicado, com fonte corrente declarada em §11 |
| **Situacao final** | **`fechado`** |
| Data | 2026-07-28 |
| Verificado por | **DEP-QAR** |
| Registrado por | **DEP-KMS** |

> **Incidente fechado sem correcao de causa nao esta fechado** (FND-04 §10). Este fecha com
> causa corrigida **e** exercida — a diferenca entre regra escrita e regra testada.
