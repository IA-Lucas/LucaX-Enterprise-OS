---
id: ADR-0011-contrato-de-carta-de-departamento
titulo: Adotar o Contrato de Carta de Departamento, instituído por ADR e materializado no template vigente
tipo: adr
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-EXE
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0001, ADR-0002, ADR-0003, ADR-0005, ADR-0006, ADR-0008, ADR-0009]
substitui: []
substituido_por: null
classe_mudanca: C2
tipo_decisao: 2
supera: []
superado_por: null
resumo: Institui o contrato de conteúdo mínimo e limites da Carta de Departamento, com dez regras de desenho, e autoriza dois pilotos de validação.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-GOV
ratificacao: nao-exigida
---

# ADR-0011: Contrato de Carta de Departamento

## Proposito
Fixar o que toda Carta de Departamento deve declarar, o que ela nao pode conter e sob que
regras de desenho e julgada — sem criar documento fundacional, entidade, tipo documental
nem camada conceitual nova.

## Escopo
| Item | Definicao |
|---|---|
| **Aplica-se a** | Toda Carta de Departamento, presente e futura — o tipo documental de [FND-10 §4.3](../foundation/10-artifact-framework.md), mapeado a entidade `DEP` de [FND-09 §5.4](../foundation/09-meta-model.md). |
| **Nao se aplica a** | Carta de Agente, Subagente, Produto, Projeto, Capability ou Ficha de Ferramenta. Nao cria, altera nem extingue departamento. Nao altera FND-02, FND-09 §8.2 nem a hierarquia normativa. |
| **Subordinado a** | FND-01 · FND-02 · FND-04 · FND-06 · FND-08 · FND-09 · FND-10. Em conflito, prevalece a fonte; a divergencia e defeito deste ADR. |

## Responsaveis
| Papel | Quem |
|---|---|
| Proponente | **DEP-EXE** — FND-09 §8.2, linha `DEP`: propoe/cria |
| Revisor independente | **DEP-GOV** — FND-09 §8.2, linha `DEP`: revisa |
| Aprovador | **DEP-EXE** — FND-04 §2.1, C2/Tipo 2, com parecer de DEP-GOV |
| Ratificador | **Nao aplicavel** — C2/Tipo 2 (§11). A ratificacao incide sobre **cada Carta**, nao sobre este contrato |
| Executor | DEP-EXE *(Cartas)* · DEP-GOV *(template, indices)* · DEP-KMS *(catalogo, medicao)* |

---

## 1. Contexto

Os nove departamentos existem e vinculam desde ADR-0001, mas **nenhum tem Carta**. FND-02 §3
declara que cada um "tera Carta completa em fase futura, seguindo `TPL-carta-departamento`",
e o [README da raiz](../README.md) registra "Cartas de departamento" na coluna do que **ainda
nao existe**. OB-H2.1 da Constituicao — *"cada departamento com Carta aprovada e escopo nao
sobreposto"* — e o primeiro objetivo do horizonte H2.

O template existe desde ADR-0001 e nunca foi exercido. Ele basta para **produzir** uma Carta
e nao basta para **julga-la**: nao distingue custodia de exercicio, nao exige declarar
impedimento, nao separa indicador definido de medido, nao trata memoria autorizada e nao tem
resumo operacional nem perfil de carregamento. As cinco lacunas estao levantadas em
[RFC-0008 §2](../rfcs/RFC-0008-contrato-de-carta-de-departamento.md), cada uma constatada por
confronto do template com a norma vigente — nenhuma depende de instancia futura.

**Se nada mudar:** as nove Cartas nascem sob um template que nao verifica as cinco lacunas, e
o primeiro defeito aparece depois de nove instancias — nove correcoes em vez de uma.

## 2. Problema / Pergunta de decisao

> **Onde vive o contrato de Carta de Departamento, e o que ele exige, para que a pergunta
> "esta Carta esta correta?" tenha resposta verificavel antes da primeira instancia?**

## 3. Criterios de decisao

> Preenchidos **antes** de examinar as alternativas (CD-01, FND-07).

| # | Criterio | Peso | Como se mede |
|---|---|---|---|
| C1 | **Nao amplia o universo sem gatilho observado** | Alto | Entidades, tipos documentais, camadas e documentos fundacionais criados. Meta: **0** |
| C2 | **Entra em vigor nesta missao** | Alto | O instrumento alcanca `ativo` sem depender de ato do Soberano que a missao nao pode produzir (LM-02, CV-09) |
| C3 | **Validado antes do rollout** | Alto | Instancias reais testadas em cenario antes das sete Cartas restantes |
| C4 | **Custo de contexto** | Medio | Linhas acrescidas ao acervo e ao pacote de quem escreve uma Carta, **medidas** (CE-02, CE-04) |
| C5 | **Reversibilidade** | Medio | O que e preciso desfazer se o contrato se mostrar errado |

## 4. Alternativas consideradas

### Alternativa A — FND-11 "Department Framework"

| Campo | Conteudo |
|---|---|
| Descricao | Documento fundacional novo no nivel 2 da hierarquia normativa, com o contrato completo. |
| A favor | Lugar obvio para quem procura; simetria com FND-08, FND-09 e FND-10. |
| Contra | **Zero instancias anteriores, zero consumidores, zero regimes concorrentes** — os tres criterios que REV-SOBERANO §6.1 usou para recusar FND-11 na missao anterior permanecem inalterados. |
| Custo | **C3 com ratificacao indelegavel do Soberano**, mais emenda a FND-01 §10 e a todo documento que lista a hierarquia. |
| Risco | Como esta missao nao produz ratificacao, FND-11 nasceria `aprovado` e **nao entraria em vigor** (LM-02) — e as Cartas nasceriam sob norma sem eficacia. |
| Avaliacao | **C1 falha** *(cria documento fundacional sem gatilho)* · **C2 falha** *(nao vigora)* · C3 neutro · C4 falha · C5 falha *(reverter exige emenda C3)*. |

### Alternativa B — Contrato em ADR, materializado no template vigente

| Campo | Conteudo |
|---|---|
| Descricao | Este ADR institui o contrato — doze blocos obrigatorios, limites e dez regras de desenho — e emenda `TPL-carta-departamento` para materializa-lo. A projecao Departamento × Capability entra no catalogo de Capabilities. Dois pilotos de classes distintas validam o contrato em seis cenarios. |
| A favor | Reusa o precedente **exato** de [ADR-0010](ADR-0010-contrato-de-conhecimento-do-soberano.md): contrato em ADR, instancia em artefato proprio, nenhum documento fundacional criado. Nao toca hierarquia, entidade nem tipo documental. |
| Contra | O contrato fica em **M1** (FND-10 §6.2): evoluir exige superar este ADR, nao versiona-lo. |
| Custo | **C2 / Tipo 2.** Emenda MENOR em dois artefatos; nenhuma norma alterada. |
| Risco | Dez regras novas com exercicio limitado a dois pilotos — o padrao ja registrado em R1 de FIT-2026-002 e R1 de FIT-2026-004. Mitigado por medicao obrigatoria no Fitness Check (§9, R1). |
| Avaliacao | **C1 passa** *(0/0/0/0)* · **C2 passa** *(C2/Tipo 2 alcanca `ativo`)* · **C3 passa** *(dois pilotos, seis cenarios)* · C4 aceitavel *(medido em §7)* · **C5 passa** *(reversao documental, §10)*. |

### Alternativa C — Emendar o template, sem ADR

| Campo | Conteudo |
|---|---|
| Descricao | Levar o contrato inteiro para dentro de `TPL-carta-departamento`, sem instrumento decisorio. |
| A favor | O menor acrescimo possivel ao acervo. |
| Contra | **Template vincula a forma, nunca o conteudo** (FND-09 §5.4, E-16). Custodia unica, impedimento e indicador medido sao conteudo normativo. Alem disso, alterar template e **C2 e exige ADR** (FND-04 §6) — a alternativa e internamente inconsistente. |
| Custo | Baixo em linhas, alto em rastreabilidade: a regra ficaria sem origem identificavel (LN-07). |
| Risco | Norma vivendo em artefato sem autoridade para carrega-la. |
| Avaliacao | C1 passa · C2 passa · **C3 falha** · C4 passa · **C5 falha** *(sem ADR nao ha plano de reversao nem gatilho de reavaliacao)*. |

### Alternativa Z — Nao fazer nada

| Campo | Conteudo |
|---|---|
| O que acontece se mantivermos o estado atual | As nove Cartas sao escritas sob o template v1.0.0, que nao verifica L1 a L5 de RFC-0008 §2. |
| Custo real da inacao | OB-H2.1 fica sem criterio de aceite. O defeito de desenho aparece **depois** de nove instancias. O catalogo de Capabilities ja demonstra o custo desse padrao: **88 de 111 indicadores sem valor medido** (REV-CAP A6) porque o criterio "indicador medido" nao era verificado na producao. |
| Por que nao venceu | Falha em C3 por definicao, e transfere para o rollout um custo que a validacao com dois pilotos resolve por **um** exercicio. |

## 5. Decisao

**Decidimos instituir o Contrato de Carta de Departamento neste ADR, materializa-lo em
`TPL-carta-departamento` v1.1.0, projetar a matriz Departamento × Capability no catalogo de
Capabilities, e valida-lo em dois pilotos de classes distintas — sem criar documento
fundacional, entidade, tipo documental ou camada conceitual.**

### 5.1 O que a Carta de Departamento e

> A Carta de Departamento e o **documento constitutivo** de uma estrutura operacional
> mutavel que **custodia ou exerce** Capabilities. Ela declara fronteira, autoridade,
> interface e ciclo de vida de um dominio de responsabilidade — e **nao** e Capability,
> agente, equipe nem agrupamento documental.

| A Carta **e** | A Carta **nao e** | Onde vive a diferenca |
|---|---|---|
| Documento constitutivo do dominio de responsabilidade | A competencia em si | FND-08 §1.2 |
| Declaracao de quem responde | Declaracao do que a organizacao sabe fazer | FND-08 §1.3 |
| Estrutura **reorganizavel** | Camada estavel | FND-02 §9.1, degrau 5 × degrau 6 |
| Vinculo a Capabilities existentes | Criacao de Capability | FND-08 §7.1, VC-02 |
| Papel de dominio | Papel executor | FND-09 §5.4, E-10 × E-11 |

### 5.2 Conteudo minimo — os doze blocos obrigatorios

Bloco ausente ou vazio torna a Carta **nao conforme**; DEP-GOV a devolve sem analise de
merito (AC-06, FND-03 §10).

| # | Bloco | O que declara | Norma de origem |
|---|---|---|---|
| **B1** | **Identidade, classe e mandato** | `id`, nome, classe, nivel, `nivel_autonomia`, `responde_a`, proposito e a frase unica de mandato pela qual o departamento responde | FND-02 §2.1 e §3; FND-09 §5.4 |
| **B2** | **Capabilities custodiadas e exercidas** | Tabela com **as duas colunas separadas**: o que custodia (zelo, unico) e o que exerce (pratica, nao exclusiva) | FND-08 §6.1, OW-01, OW-02; FND-09 R-02, R-03, RM-05 |
| **B3** | **Responsabilidades e exclusoes** | O escopo exclusivo, com verificacao por item; e **o que nao lhe compete**, nomeando o dono real de cada item | ES-01, ES-05; FND-04 §6 |
| **B4** | **Autoridade, decisoes permitidas e portoes** | O que decide, com a **fonte** de cada autoridade; o que nao decide; os portoes QG sob sua responsabilidade e o criterio de liberacao | FND-01 §6.2 e §7.3; FND-09 §8.2, AU-09 |
| **B5** | **Interfaces — entradas, saidas e consumidores** | O que recebe, de quem; o que entrega, a quem, em que formato e cadencia; e quem consome cada saida | FND-02 §4; FND-05 §2 e §4 |
| **B6** | **Artefatos e registros mantidos** | Os tipos documentais que produz e os registros de que e proprietario, por ID de tipo | FND-10 §4 |
| **B7** | **Memoria autorizada e politica de contexto** | Em que camadas escreve, le e e dono; e qual pacote minimo de contexto sua operacao exige | FND-06 §2.1 e §3; FND-05 §5; CE-01 |
| **B8** | **Indicadores — definido × medido** | Cada indicador com **valor medido e data**, ou declarado explicitamente como `definido, sem valor` | LM-01, CL-06, CE-04, LV-12, DoD-5 |
| **B9** | **Riscos, incompatibilidades e segregacao** | Os impedimentos do departamento: em que materia ele **nao** pode aprovar nem verificar, e quem o substitui | PI-05, LV-03; RM-06, RM-06b; FT-02; FND-04 §3.1 |
| **B10** | **Escalonamento, cadencias e handoffs** | Gatilhos de escalonamento com nivel E0–E4; cadencias de que participa; handoffs que emite e recebe, com criterio de devolucao | FND-05 §4, §7.1 e §8 |
| **B11** | **Ciclo de vida e gatilhos** | O que dispara especializacao, fusao ou retirada deste departamento, e o destino de cada responsabilidade e de cada custodia na extincao | FND-02 §8.3, §9.2 e §9.3; IV-07; PI-14 |
| **B12** | **Rastreabilidade, resumo operacional e perfil minimo de carregamento** | Origem, decisoes relacionadas, o `resumo` de uma linha e o custo **medido** em linhas do recorte minimo da Carta | LN-07; FND-10 §2.2 e §8.3; CE-02 |

### 5.3 As dez regras de desenho

| # | Regra | Fundamento | Como se verifica na Carta |
|---|---|---|---|
| **DC-01** | **Capability e estavel; Departamento e reorganizavel.** A Carta declara vinculo a Capabilities existentes e **nunca** redefine, cria, divide nem aposenta competencia. | FND-08 §1.3, CI-01, TC-1; FND-02 §9.1 | B2 cita apenas `CAP-` ja vigentes; nenhuma definicao de competencia e reescrita |
| **DC-02** | **Cada Capability possui exatamente um custodiante e pode ter varios exercentes.** A Carta declara as duas listas separadamente; declarar so uma e elo incompleto. | OW-01, OW-02, OW-07; RM-05 | B2 tem duas colunas; a custodia declarada confere com a fonte (§5.5) |
| **DC-03** | **Departamento nao aprova nem verifica materia em que esteja impedido.** A Carta nomeia seus impedimentos e quem o substitui em cada um. | PI-05, LV-03; RM-06, RM-06b; FT-02; CV-08 | B9 lista impedimento, materia e substituto; ausencia de B9 devolve a Carta |
| **DC-04** | **Nenhum Departamento cria autoridade por autodeclaracao.** Toda linha de B4 cita a fonte da autoridade. Autoridade que nao conste da fonte **nao existe**. | AU-03, AU-09, AU-10; LV-07; FND-01 §7.3 | Cada linha de B4 traz a coluna Fonte; linha sem fonte e removida, nao aceita |
| **DC-05** | **Fronteiras declaram o que entra, o que sai e o que fica fora.** As tres sao obrigatorias; o "fica fora" nomeia o dono real. | ES-01, ES-05; FND-04 §6.1 | B3 e B5 completos; exclusao generica *("nao cuida do resto")* e devolvida |
| **DC-06** | **Subdivisao exige sinal observado.** A Carta declara os gatilhos de especializacao aplicaveis e **o que ja foi observado**, com valor e data. Ganho previsto nao autoriza. | PI-14 regra 1; FND-02 §9.2; FND-04 §6.2; SE-01, SE-02 | B11 distingue *gatilho declarado* de *sinal ja observado*; sinal sem valor medido nao conta |
| **DC-07** | **Indicador sem valor nao prova desempenho.** Todo indicador de B8 traz valor medido e data, ou a marca explicita `definido, sem valor`. | LM-01, CL-06, CE-04, LV-12 | Contagem de B8: quantos definidos, quantos medidos. Maturidade afirmada sem medida e rebaixada |
| **DC-08** | **A Carta referencia normas; nao as reescreve.** Tabela que exiba conteudo de outra fonte declara **projecao** com as quatro informacoes de PJ-02, ou vira referencia. | PJ-01 a PJ-03, PJ-05; MM-01; LX-07 | Teste preventivo do checklist de `TPL-documento` aplicado tabela a tabela, antes da submissao |
| **DC-09** | **A Carta nao entra em vigor por si.** `aprovado` e `ativo` de Carta de Departamento dependem de **ato explicito e datado do Soberano**; ate la a Carta permanece em `em-revisao`. Precedente, instrucao generica e silencio nao aprovam. | FND-09 §8.2 *(linha `DEP`)*; FND-10 §10.3 e §5.4; CV-09; LM-02 a LM-06 | `status` e `ratificacao` conferidos contra a fonte do ato; ausencia de ato mantem `em-revisao` |
| **DC-10** | **O perfil minimo de carregamento e medido, nunca estimado.** B12 declara o custo em linhas do recorte minimo, com data. | CE-02, CE-04; CT-23 *(mesmo mecanismo, outro objeto)* | Numero reproduzivel por `sed`+`wc -l`; valor sem data nao entra |

### 5.4 Limites — o que a Carta **nao** pode conter

| Conteudo proibido | Por que | Consequencia |
|---|---|---|
| Definicao de Capability, ou alteracao de escopo/limite de Capability | DC-01; a Carta de Capability e a fonte (FND-08 §9) | Carta devolvida por DEP-GOV |
| Autoridade nao declarada em FND-01 §7.3 ou FND-09 §8.2 | DC-04, AU-09 | Linha nula; nao vincula ninguem |
| Escopo sobreposto a departamento vizinho | ES-01; FND-10 §4.3 declara a sobreposicao como conteudo proibido do tipo | Carta vetada |
| Criacao de agente, subagente, skill, workflow, produto, projeto ou ferramenta | PI-12; cada um tem rito proprio (FND-04 §6) | Ato nulo; incidente de conformidade |
| Portao de qualidade novo | Os sete portoes sao de FND-01 §6.2; acrescentar e **C3** | Carta devolvida |
| Reproducao de tabela normativa de outro documento sem declaracao de projecao | DC-08, PJ-01 | Tabela substituida por referencia |
| Indicador afirmado como medido sem valor e data | DC-07, LV-12 | Rebaixamento compulsorio; possivel incidente |
| Credencial, segredo ou dado sensivel em texto | PI-08, LV-02 | Incidente critico; rotacao obrigatoria |

### 5.5 Fonte canonica da custodia e do exercicio

> A fonte e o **frontmatter das 23 Cartas de Capability** (`custodio`, `exercentes`), em
> `capabilities/CAP-<slug>.md`. A matriz Departamento × Capability e **projecao** dela,
> mantida em [`capabilities/README.md §10`](../capabilities/README.md), e a Carta de
> Departamento e **segunda projecao**, restrita as linhas do proprio departamento.

| # | Regra |
|---|---|
| **PR-1** | Em divergencia entre a Carta de Departamento e o frontmatter da Carta de Capability, **prevalece a Carta de Capability** (PJ-03). O defeito e da Carta de Departamento. |
| **PR-2** | Corrigir a Carta de Capability para caber na Carta de Departamento e **proibido** (PJ-03, M3 generalizado). |
| **PR-3** | Acrescentar exercente e mudanca na **Carta de Capability**, com o rito de FND-08 §6.3 — nunca declaracao unilateral na Carta de Departamento (RL-03, RM-01). |

### 5.6 Instancias autorizadas por este ADR

Autorizam-se **duas** Cartas, e apenas duas:

| Carta | Classe | Local | Estado ao fim desta decisao |
|---|---|---|---|
| `DEP-QAR` — Qualidade e Risco | **Guarda** | `departments/qar/carta.md` | **`em-revisao`**, `ratificacao: pendente` |
| `DEP-ENG` — Engenharia | **Linha** | `departments/eng/carta.md` | **`em-revisao`**, `ratificacao: pendente` |

**As sete Cartas restantes nao sao autorizadas por este ADR.** O rollout depende do ato do
Soberano sobre os dois pilotos e da decisao GO/ADJUST/STOP de
[FIT-2026-005](../governance/fitness/FIT-2026-005-cartas-de-departamento.md).

### 5.7 O que este contrato **nao** faz

| Nao faz | Por que |
|---|---|
| Nao cria documento fundacional | Zero instancias anteriores, zero consumidores, zero regimes concorrentes — os tres criterios de REV-SOBERANO §6.1 permanecem nao satisfeitos |
| Nao cria entidade nem tipo documental | `DEP` ja e entidade (FND-09 §5.4) e `Carta de Departamento` ja e tipo documental (FND-10 §4.3). CS-01 e MT-01 satisfeitos sem acrescimo |
| Nao cria departamento, agente, subagente, skill, workflow, produto, projeto ou ferramenta | PI-12 exige Carta e rito proprio para cada um; nenhum e criado |
| Nao altera FND-02 | A estrutura, as classes e a matriz de interacao permanecem exatamente como estao; a Carta as **referencia** (DC-08) |
| Nao altera a matriz de autoridade | FND-09 §8.2 e a fonte; este ADR a cita e nao a redefine (§6.1 de FND-10) |
| Nao amplia o nucleo obrigatorio de contexto | `TPL-carta-departamento` permanece `sob-demanda`; ampliar o nucleo seria C2 propria (CE-01) |
| Nao aprova nem ratifica nada | Aprovar Carta de Departamento e ato do **SOBERANO** (DC-09). Este ADR autoriza a **producao**, nunca a vigencia (AU-06) |
| Nao alcanca Carta de Agente | Nenhum agente existe; alcancar dois tipos com um exercicio seria antecipacao (FND-08 §7.1) |

## 6. Justificativa

A Alternativa B vence porque e a unica que satisfaz **C1, C2 e C3 ao mesmo tempo**.

**C1 — nao amplia o universo.** O contrato nao cria entidade, tipo documental, camada nem
documento fundacional: usa `DEP` e `Carta de Departamento`, ambos ja declarados. A
Alternativa A falharia aqui, e falharia pelo mesmo fundamento que ja recusou FND-11 uma vez.

**C2 — vigora agora.** C2/Tipo 2 alcanca `ativo` sem ratificacao (FND-10 §10.3). A
Alternativa A nasceria `aprovado` e nao entraria em vigor — o contrato existiria sem eficacia
e as Cartas nasceriam sob norma inaplicavel.

**C3 — validado antes do rollout.** Dois pilotos de classes distintas, testados em seis
cenarios, custam **um** exercicio; nove Cartas sob template nao verificado custariam nove
correcoes. O catalogo de Capabilities e a evidencia direta desse custo: 88 de 111 indicadores
sem valor medido, porque o criterio nao era verificado na producao (REV-CAP A6).

**Tradeoff aceito:** o contrato fica em **M1** — imutavel apos eficacia. Corrigi-lo exige
**superar este ADR** com outro, nao versiona-lo. Aceita-se o custo porque a alternativa que
permitiria versionar (documento fundacional, M2) e exatamente a que falha em C1 e C2. O
gatilho que forca a reavaliacao esta em §12: **terceira Carta escrita**.

**Segundo tradeoff, declarado:** dez regras novas com exercicio limitado a dois pilotos. E o
terceiro ciclo consecutivo em que se institui regime preventivo inteiro (FR, PJ, CT, agora
DC). O risco esta nomeado em §9 R1 e a medicao e obrigatoria no Fitness Check — nao se
declara ganho de proporcao sem contar.

## 7. Impacto

| Dimensao | Impacto |
|---|---|
| Departamentos afetados | **DEP-EXE** autor das Cartas · **DEP-GOV** revisor e guardiao do template · **DEP-QAR** objeto de um piloto e executor do Fitness Check · **DEP-ENG** objeto do outro piloto · **DEP-KMS** medicao e catalogo |
| Componentes afetados | **2** Cartas de Departamento em `em-revisao`. Nenhum agente, skill, workflow, produto, projeto ou ferramenta |
| Camadas de memoria a atualizar | **APR** — [MEM-APR-0004](../memory/aprendizado/MEM-APR-0004-projecao-revela-divergencia-antiga.md), QG-5 |
| Decisoes superadas | **Nenhuma** |
| Documentos a atualizar | `TPL-carta-departamento` **1.0.0 → 1.1.0** *(MENOR)* · `capabilities/README` **1.0.0 → 1.1.0** *(MENOR)* · catalogo mestre · indices de decisoes, RFCs, aptidao, governanca e raiz |
| Custo e dependencia criados | Dez regras `DC` a manter. Nenhuma dependencia externa. Nenhum arquivo auxiliar por artefato (RG-05) |
| Ganho PI-14 | **Organizacao** — a pergunta "esta Carta esta correta?" passa de julgamento a lista de doze blocos e dez regras verificaveis. **Reducao de contexto** — o perfil minimo de carregamento da Carta e medido em linhas (DC-10), e quem consulta um departamento carrega o recorte, nao a Carta inteira |

## 8. Evidencias

| # | Evidencia | Origem (ID) | Confianca | O que ela discrimina |
|---|---|---|---|---|
| E1 | **9 departamentos definidos, 0 Cartas** | [README §Estado atual](../README.md); [catalogo mestre §5](../governance/artifact-registry.md) — Constitutiva: 7 tipos, 1 com instancia | **Alta** | Que a lacuna e real e nao antecipada |
| E2 | **22 de 23 Capabilities declaram `exercentes` identico ao `custodio`** | Frontmatter das 23 Cartas em `capabilities/`, lido por ferramenta em 2026-07-28 | **Alta** | Que OW-02 *("custodia nao e exclusividade")* tem **1** membro observado — a regra existe e quase nao e exercida |
| E3 | **88 de 111 indicadores do catalogo de Capabilities sem valor medido** | [capabilities/README §9](../capabilities/README.md); REV-CAP A6 | **Alta** | Que DC-07 corrige um defeito **ja observado**, nao hipotetico |
| E4 | **DEP-ENG vincula-se a 5 Capabilities; DEP-EXE a 4** | Projecao de §5 do catalogo de Capabilities | **Alta** | Que VC-03 *(mais de tres = componente amplo demais)* dispara em **2 de 9** departamentos antes da primeira Carta |
| E5 | **Precedente estrutural completo:** ADR-0010 instituiu contrato por ADR, autorizou uma instancia, e a instancia ficou em `aprovado` aguardando ato do Soberano | [ADR-0010 §5.8, CT-28](ADR-0010-contrato-de-conhecimento-do-soberano.md) | **Alta** | Que a Alternativa B ja funcionou uma vez, com o mesmo desenho |
| E6 | **Impedimento cruzado ja ocorreu uma vez** na matriz de autoridade de `FIT` | [FIT-2026-003](../governance/fitness/FIT-2026-003-consolidacao-baseline.md); achado C5 de REV-CONSOLIDACAO | **Media** — uma ocorrencia, com uma nao ocorrencia posterior | Que DC-03 trata risco observado, e nao teorico |
| **A1** | **Evidencia ausente, declarada:** nao ha nenhuma Carta de Departamento anterior no acervo — **zero** exercicios previos do template | Varredura do acervo, 2026-07-28 | — | Que o contrato e desenhado **antes** de haver serie historica. E a razao do gatilho de §12 |
| **A2** | **Evidencia ausente, declarada:** as classes **Comando** e **Plataforma** ficam sem piloto | §5.6 | — | Que o contrato so tera sido exercido em 2 das 4 classes quando o rollout for decidido |

## 9. Riscos e mitigacao

| # | Risco | Probabilidade | Impacto | Mitigacao prevista |
|---|---|---|---|---|
| R1 | **Dez regras novas com exercicio insuficiente** — terceiro ciclo consecutivo instituindo regime preventivo inteiro | **Alta** | Medio | Medicao obrigatoria no Fitness Check: quantas das dez foram exercidas pelos dois pilotos, nominalmente. Menos de **seis** abre proposta de consolidacao (EV-08) |
| R2 | **Dois pilotos nao cobrem Comando nem Plataforma** | Alta *(certa)* | Medio | Declarado como limite em A2; o rollout comeca por uma Carta de **Plataforma**, para expor o contrato a classe mais distante das testadas |
| R3 | **A projecao Departamento × Capability virar segunda fonte** da custodia | Media | **Alto** | PR-1 a PR-3 (§5.5); declaracao de projecao com as quatro informacoes de PJ-02 no proprio catalogo |
| R4 | **Os pilotos ficarem indefinidamente em `em-revisao`** | Media | Medio | Declarado; o desbloqueio e um unico ato do Soberano sobre as duas Cartas. Enquanto nao ocorrer, as sete restantes **nao** sao escritas |
| R5 | **Esta decisao estar errada** — o conteudo minimo ser excessivo para departamentos pequenos | Media | Medio | Sinal de erro em §12: se a Carta de um departamento de custodia unica exigir bloco vazio ou preenchido por formalidade, o contrato esta grande demais e cabe consolidacao |

## 10. Plano de reversao

| Campo | Conteudo |
|---|---|
| Como desfazer | **(1)** Novo ADR superando este, com o que mudou (SU-01). **(2)** `TPL-carta-departamento` volta ao conteudo de 1.0.0 por nova versao — o texto anterior permanece no historico (AL-04). **(3)** A secao de projecao sai de `capabilities/README`, que e **M3** e se reprocessa da fonte. **(4)** As duas Cartas vao a `arquivado` pela operacao **O8** — legitima porque **nunca estiveram em `ativo`** (FND-10 §5.2). |
| Custo da reversao | **Documental integral.** Nenhum dado vivo, nenhuma exposicao externa, nenhuma migracao, nenhuma credencial. Nenhum arquivo e apagado (PI-07, RB-05) |
| Janela em que ainda e possivel | **Permanente enquanto as Cartas nao entrarem em `ativo`.** Depois disso, corrigir e superar, nao reverter (RB-02) |
| Quem executa | DEP-GOV *(template e indices)* · DEP-EXE *(Cartas)* · DEP-KMS *(catalogo)* |
| Backup necessario (PI-07) | **Nenhum dado vivo e tocado.** A integridade do estado anterior esta materializada na baseline **`BL-2026-07-28-02`**, preservada e nao editada (BL-02) |

## 11. Classificacao

| Campo | Valor |
|---|---|
| Classe de mudanca | **C2** — cria componentes e altera padrao documental (FND-04 §2) |
| Tipo de reversibilidade | **Tipo 2** — reversao documental integral, sem dado vivo, sem exposicao externa, sem migracao (§10) |
| Decisor | **DEP-EXE**, com parecer de DEP-GOV (FND-04 §2.1) |
| Ratificador | **Nao aplicavel a este ADR.** A ratificacao incide sobre **cada Carta**, e e do SOBERANO (DC-09) |
| Data da decisao | 2026-07-28 |
| Data de vigencia | 2026-07-28 |

> **Por que Tipo 2, e nao Tipo 1.** FND-04 §6 classifica **criar departamento** como
> C2/Tipo 1. Este ADR **nao cria departamento**: os nove existem e vinculam desde ADR-0001,
> ratificado. O que se cria e o **contrato documental** e duas Cartas que **nunca entram em
> `ativo` por este ato**. Todo efeito e reversivel por superacao e reprocessamento (§10).
> A irreversibilidade que Tipo 1 protege — dado vivo, exposicao externa, migracao — **nao
> esta presente em nenhum ponto**. A exigencia de ato do Soberano permanece integral, mas
> incide sobre a **Carta** (DC-09), nao sobre este contrato.

## 12. Revisao

| Campo | Conteudo |
|---|---|
| Gatilho de reavaliacao | **Evento** — cumulativo, o que vier primeiro |
| Detalhe do gatilho | **(a)** **Terceira Carta escrita** — primeira instancia fora dos pilotos, e o momento de medir se o contrato serviu sem adaptacao. **(b)** **Primeira Carta de classe Comando ou Plataforma**, que testa o contrato nas duas classes sem piloto (R2). **(c)** **Menos de seis** das dez regras `DC` exercidas na medicao do Fitness Check — abre proposta de consolidacao (EV-08, R1) |
| Sinal de que esta decisao deu errado | Bloco obrigatorio preenchido por formalidade em duas Cartas seguidas; ou regra `DC` que nenhuma Carta consiga satisfazer sem excecao formal; ou divergencia entre Carta e Carta de Capability resolvida em favor da Carta de Departamento — que seria violacao de PR-2 |
| Responsavel pela revisao | **DEP-GOV** *(forma)* com **DEP-EXE** *(merito)* e **DEP-QAR** *(aptidao)* |

## 13. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Origem | [RFC-0008](../rfcs/RFC-0008-contrato-de-carta-de-departamento.md) — aceita com ajuste |
| Decisoes superadas | Nenhuma |
| Decisoes relacionadas | **ADR-0001** *(cria departamentos e o template)* · **ADR-0002** *(vinculacao obrigatoria a Capability)* · **ADR-0003** *(Meta Model; entidade `DEP`)* · **ADR-0005** *(proibicao de autoverificacao — base de DC-03)* · **ADR-0006** *(contrato de artefato)* · **ADR-0008** *(uma fonte, multiplas projecoes — base de DC-08 e §5.5)* · **ADR-0009** *(o que conta como emenda — dispara a obrigacao nos dois artefatos emendados)* |
| Registros de memoria gerados | [MEM-APR-0004](../memory/aprendizado/MEM-APR-0004-projecao-revela-divergencia-antiga.md) |
| Verificacao de aptidao | [FIT-2026-005](../governance/fitness/FIT-2026-005-cartas-de-departamento.md) |
| Revisao arquitetural | [REV-DEPARTAMENTO-2026-07-28](../foundation/revisao-arquitetural-cartas-de-departamento-2026-07-28.md) |

---

## Checklist de validade (FND-07 §4.1)
- [x] **VD-01** — 3 alternativas reais (A, B, C) + "nao fazer nada" (Z)
- [x] **VD-02** — criterios C1–C5 declarados em §3, antes de §4
- [x] **VD-03** — nenhuma alternativa de palha: A e o desenho natural da missao, C e o mais barato
- [x] **VD-04** — tradeoff explicito em §6: contrato em M1, e regime preventivo com exercicio limitado
- [x] **VD-05** — evidencia ausente declarada como ausente: **A1** e **A2** em §8
- [x] **VD-06** — plano de reversao em §10 *(nao obrigatorio em Tipo 2; produzido assim mesmo)*
- [x] **VD-07** — impacto em cascata mapeado em §7, com os dois artefatos emendados nomeados
- [x] **VD-08** — data e responsaveis presentes em §11 e no bloco Responsaveis
- [x] **VD-09** — gatilho de revisao definido em §12, com tres condicoes e sinal de erro
