---
id: ADR-0007-fronteira-greenfield-legado
titulo: Declarar a fronteira entre o LucaX Enterprise OS e o LucaX Legacy, e o portao unico de admissao de origem externa
tipo: adr
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0001, ADR-0003, ADR-0006]
substitui: []
substituido_por: null
classe_mudanca: C2
tipo_decisao: 2
supera: []
superado_por: null
resumo: Declara o sistema como greenfield e unica fonte normativa, nega autoridade automatica ao sistema preexistente e fixa o portao de admissao de qualquer conteudo externo.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# ADR-0007: Fronteira greenfield / legado

## Proposito

Registrar a decisao de declarar tres identidades distintas — o sistema atual, o sistema
preexistente e o eventual esforco de migracao — e de submeter **toda** entrada de conteudo
externo a um portao unico, definido antes do primeiro candidato existir.

## Escopo

| Item | Definicao |
|---|---|
| **Inclui** | Identidade e autoridade dos tres termos; proibicao de importacao direta; condicoes de admissao futura; vocabulario de proveniencia e seu valor padrao |
| **Nao inclui** | O conteudo do LucaX Legacy — **nao consultado, nao inventariado, nao copiado**; o merito de qualquer candidato futuro; a criacao do Programa de Migracao |
| **Subordinado a** | [FND-01](../foundation/01-constituicao.md), [FND-03](../foundation/03-taxonomia.md), [FND-04](../foundation/04-governanca.md), [FND-09](../foundation/09-meta-model.md), [FND-10](../foundation/10-artifact-framework.md) |

## Responsaveis

| Papel | Quem |
|---|---|
| Proponente | DEP-GOV |
| Revisor independente | **DEP-QAR** |
| Aprovador | **DEP-EXE**, com parecer de DEP-GOV (FND-04 §2.1, C2) |
| Ratificador | **Nao aplicavel** — C2/Tipo 2 (§11) |
| Executor | DEP-GOV |

---

## 1. Contexto

O acervo tem **85 artefatos e 18.916 linhas**, integralmente produzidos dentro deste sistema.
Existe, fora dele, um **LucaX anterior**. Este sistema nunca o consultou.

A unica norma vigente sobre origem externa e FND-03 §9: *"Artefato importado de fora recebe
ID novo do sistema e declara a origem em `origem`."* Ela governa a **forma** da importacao e
e silenciosa sobre a **admissao** — quem decide, contra o que se valida, e com que autoridade
o conteudo passa a valer.

O acervo ja produziu, uma vez, o defeito exato que essa lacuna permite:
[INC-2026-001](../governance/incidents/INC-2026-001-ratificacao-inferida.md) registra quatro
decisoes C3/Tipo 1 que trataram **precedente** como ato de autoridade. Um sistema que ja
converteu precedente interno em norma tem risco demonstrado — nao presumido — de converter
conteudo externo em norma pelo mesmo caminho.

**Se nada mudar:** o primeiro contato com o sistema anterior definira a regra por precedente,
com o conteudo ja a vista e sob pressao de um caso concreto.

## 2. Problema / Pergunta de decisao

O sistema deve declarar agora a fronteira entre si e o LucaX preexistente, com portao de
admissao definido — ou tratar a questao quando o primeiro candidato aparecer?

## 3. Criterios de decisao

> Declarados antes do exame das alternativas (CD-01).

| # | Criterio | Peso | Como se mede |
|---|---|---|---|
| C1 | Nenhuma origem externa recebe autoridade automatica | **Bloqueante** | Nao existe caminho normativo que faca conteudo externo valer sem decisao formal deste sistema |
| C2 | Nao cria entidade, tipo documental, departamento, programa nem inventario | **Bloqueante** | Universo permanece em 21 entidades; nenhum artefato descreve o legado |
| C3 | Custo zero para o acervo existente | Alto | Arquivos reescritos = 0 |
| C4 | Portao verificavel **antes** da entrada | Alto | Lista fechada de condicoes conferiveis por DEP-GOV sem julgar merito |
| C5 | Reversivel | Medio | Desfazer nao destroi nada nem exige migracao |

## 4. Alternativas consideradas

### Alternativa A — Declarar as tres identidades e o portao, sem tocar no legado

| Campo | Conteudo |
|---|---|
| Descricao | Tres termos oficiais; proibicao de importacao direta; cinco condicoes de admissao; proveniencia como campo **curado no catalogo**, padrao `native` |
| A favor | Satisfaz C1 a C5. A regra passa a existir **antes** do primeiro caso — a unica ordem que impede o precedente |
| Contra | Escreve norma sobre situacao ainda nao ocorrida |
| Custo | 1 ADR, 2 termos de vocabulario, 1 coluna de catalogo, 0 arquivos reescritos |
| Risco | A regra nao caber no primeiro caso real (R1) |
| Avaliacao | C1 ✔ · C2 ✔ · C3 ✔ · C4 ✔ · C5 ✔ |

### Alternativa B — Estender apenas FND-03 §9 com a regra de `origem`

| Campo | Conteudo |
|---|---|
| Descricao | Acrescentar que artefato importado declara `origem` e segue o rito da sua classe |
| A favor | Custo minimo; usa instrumento existente; nenhuma norma nova |
| Contra | **Falha em C1 e C4.** Governa como se registra o que ja entrou; nao governa se pode entrar. A autoridade do conteudo importado continuaria indefinida — que e precisamente o vazio que produz autoridade por proximidade |
| Custo | 3 linhas |
| Risco | Falsa sensacao de cobertura: a regra existe, e nao responde a pergunta |
| Avaliacao | C1 **falha** · C2 ✔ · C3 ✔ · C4 **falha** · C5 ✔ |

### Alternativa C — Criar o Migration Framework e o Programa de Migracao agora

| Campo | Conteudo |
|---|---|
| Descricao | Documento fundacional de migracao, inventario do legado, matriz de equivalencia, programa em fases |
| A favor | Trataria o assunto inteiro de uma vez |
| Contra | **Falha em C2 e C5.** Cria camada conceitual sem lacuna observada e sem um unico candidato — contrario a FND-04 §6.1 (regra de nao-proliferacao) e a SE-01 (sinal observado obrigatorio). Exige inventariar o legado **antes** de decidir o que fazer com ele, criando acervo paralelo sem tipo, sem dono e fora do catalogo |
| Custo | 1 documento fundacional + 1 programa + inventario de tamanho desconhecido |
| Risco | Alto: abstracao construida sobre suposicoes a respeito de um sistema nao examinado |
| Avaliacao | C1 ✔ · C2 **falha** · C3 ✔ · C4 ✔ · C5 **falha** |

### Alternativa Z — Nao fazer nada

| Campo | Conteudo |
|---|---|
| O que acontece se mantivermos o estado atual | A fronteira permanece implicita. Nada quebra hoje, porque nada foi importado |
| Custo real da inacao | O custo aparece inteiro no primeiro contato, na pior forma possivel: decisao tomada com o conteudo a vista, sob pressao de um caso concreto. Foi assim que ADR-0001 estabeleceu o precedente que INC-2026-001 teve de conter |
| Por que nao venceu | O momento em que a regra e barata e exatamente o momento em que ela parece desnecessaria |

## 5. Decisao

**Decidimos declarar a fronteira entre o LucaX Enterprise OS e o sistema preexistente, e
submeter toda entrada de conteudo externo a um portao unico**, nos seguintes termos.

### 5.1 As tres identidades

| Termo oficial | O que e | Autoridade | Estado hoje |
|---|---|---|---|
| **LucaX Enterprise OS** | Este sistema. Greenfield: nasce sem heranca, e sua arquitetura-alvo e a que este repositorio declara | **Unica fonte normativa.** Norma valida e a que consta deste acervo (ADR-0001) | Vigente |
| **LucaX Legacy** | O sistema preexistente, externo a este repositorio | **Nenhuma.** Nao e norma, nao e precedente, nao e excecao. Pode vir a ser **fonte de evidencia e de candidatos** | Externo; nao consultado, nao inventariado |
| **Programa de Migracao** | Eventual esforco temporario de avaliar e trazer conteudo do Legacy | Nenhuma — nao existe | **Nao iniciado.** Sem dono, sem prazo, sem artefato |

> **FR-01.** `LucaX Enterprise OS`, `LucaX Legacy` e `Programa de Migracao` sao **termos
> oficiais** (FND-03 §8). Usar "LucaX" sem qualificacao em documento normativo, quando os dois
> sistemas estiverem em jogo, e erro de conformidade por ambiguidade (LX-07).

> **FR-02.** O **greenfield e a natureza declarada deste sistema**, nao uma fase. Ele nao
> deixa de ser greenfield quando admitir conteudo externo: o que entra pelo portao entra como
> artefato **deste** sistema, com ID proprio e autoridade derivada da decisao que o admitiu —
> nunca da sua origem.

### 5.2 Proibicao de importacao direta

> **FR-03.** **Nenhum conteudo do LucaX Legacy entra neste sistema por copia, referencia
> normativa, adaptacao informal ou analogia.** Nao ha caminho de entrada fora do portao de
> §5.3. Conteudo que entrar por fora do portao e **nulo** (MT-01, RG-02) e sua presenca e
> incidente de conformidade.

> **FR-04.** **Consultar nao e importar.** Observar o Legacy para produzir evidencia — "este
> problema ja ocorreu", "este volume e real" — e legitimo e desejavel, e a evidencia entra
> pelo campo `evidencia` do instrumento que a invoca (FND-07 §4), com origem declarada.
> Proibido e **derivar norma** do que se observou sem passar pelo portao.

> **FR-05.** **Funcionar no Legacy nao e argumento de autoridade.** E, quando muito, evidencia
> de viabilidade — de confianca declarada, como qualquer outra (LV-12).

### 5.3 O portao de admissao — cinco condicoes cumulativas

Quando houver um candidato real, **todas** devem ser verdadeiras antes da admissao. Sao
condicoes de **admissibilidade**, nao criterios de merito: DEP-GOV as confere sem julgar
conteudo (FND-04 §12).

| # | Condicao | O que se verifica | Quem |
|---|---|---|---|
| G1 | **Proveniencia declarada** | De onde veio, o que e, quem o produziu no Legacy, em que data foi observado | Proponente |
| G2 | **Fit-gap contra o vigente** | O que este sistema ja tem que responde a mesma pergunta, e onde o candidato diverge. Sem isso, nao se sabe se e reuso ou duplicacao (FND-04 §6.1) | Proponente, conferido por DEP-GOV |
| G3 | **Classificacao declarada** | Exatamente uma de **ADOPT · ADAPT · REWRITE · RETIRE** (§5.4) | Proponente |
| G4 | **Validacao independente** | Verificacao por papel distinto de quem propos, contra a norma vigente — nao contra a pratica do Legacy | DEP-QAR |
| G5 | **Decisao formal** | Instrumento da classe da mudanca (FND-04 §2). Sem ADR, nada entra em `ativo` | Aprovador da classe |

> **FR-06.** Condicao ausente **bloqueia a admissao**; nao gera ressalva. Ressalva nao
> neutraliza condicao de validade ([MEM-APR-0001](../memory/aprendizado/MEM-APR-0001-ratificacao-por-precedente.md)).

> **FR-07.** O portao **nao autoriza inventariar o Legacy**. Ele opera sobre **um candidato
> por vez**, nomeado. Levantamento amplo previo e proibido: produziria acervo paralelo sem
> tipo, sem dono e fora do catalogo (RG-02, MT-01). Se o inventario se mostrar necessario,
> ele proprio e uma mudanca C2 com ADR — nao um preparativo informal.

### 5.4 As quatro classificacoes

| Classificacao | Significa | Efeito sobre o acervo | Proveniencia resultante |
|---|---|---|---|
| **ADOPT** | O candidato serve como esta | Entra como artefato novo, com ID deste sistema | `migrated` |
| **ADAPT** | Serve com alteracao para caber na norma vigente | Entra alterado, com a alteracao declarada no ADR | `adapted` |
| **REWRITE** | O problema e real, a solucao do Legacy nao serve | **Nada entra.** Produz-se artefato **native** que resolve o mesmo problema | `native` |
| **RETIRE** | Nem o problema nem a solucao se aplicam a este sistema | Nada entra. Registra-se a recusa para nao ser reexaminada sem fato novo | `rejected` |

> **FR-08.** REWRITE e RETIRE sao **resultados de sucesso** do portao, nao falhas. Um portao
> cujo unico desfecho previsto e a entrada nao e portao.

### 5.5 Proveniencia — campo curado, nao frontmatter

| Campo | Onde vive | Camada | Valor padrao |
|---|---|---|---|
| `proveniencia` | [Catalogo mestre](../governance/artifact-registry.md), coluna propria | **L2 — curado** (FND-10 §2.1) | **`native`** |

| Valor | Significa |
|---|---|
| `native` | Produzido dentro deste sistema. **Padrao de todo o acervo** |
| `legacy-candidate` | Nomeado como candidato; ainda **nao** admitido. Nao e artefato do acervo |
| `adapted` | Admitido por ADAPT |
| `migrated` | Admitido por ADOPT |
| `rejected` | Examinado e recusado por RETIRE |

> **FR-09.** Proveniencia e **L2 curado**, nunca frontmatter: declara-la em 85 arquivos
> contrariaria a promessa de migracao zero de FND-10 §2.3 e criaria trabalho manual por
> artefato (AC-01, RG-05). O valor padrao `native` satisfaz **AC-07** — campo novo com valor
> padrao declarado —, e por isso **nenhum arquivo do acervo e tocado**.

> **FR-10.** `legacy-candidate` **nao e estado de artefato deste acervo**. Um candidato nao
> tem ID, nao entra no catalogo e nao ocupa numero de sequencia enquanto nao for admitido. O
> valor existe para nomear o objeto do portao, nao para hospeda-lo.

## 6. Justificativa

A Alternativa A vence pelos cinco criterios; B falha nos dois bloqueantes de admissao; C falha
no bloqueante de nao-proliferacao.

**Por que a regra vem antes do caso.** A objecao correta a A — escrever norma sobre o que nao
ocorreu — perde forca porque o portao lista **condicoes de admissibilidade**, nao criterios de
conteudo. Saber de onde veio, contra o que foi comparado, que classificacao recebeu, quem
validou e quem decidiu sao exigencias que independem inteiramente do que exista no Legacy.
Nenhuma delas antecipa merito.

**Por que C e o risco maior, nao o menor.** Construir Migration Framework agora exigiria
descrever um sistema nao examinado. Toda abstracao que dai saisse seria hipotese promovida a
norma — exatamente o que a missao que originou este ADR proibe.

**Tradeoff aceito:** o sistema fica com uma norma que **nao produzira nenhum efeito observavel
enquanto nao houver candidato**. Aceita-se carregar regra ociosa por tempo indeterminado em
troca de nao decidir a fronteira sob pressao de um caso concreto. O custo e conhecido: ~130
linhas no acervo e um gatilho de revisao aberto (§12). O custo da alternativa e desconhecido
por natureza, o que e pior.

## 7. Impacto

| Dimensao | Impacto |
|---|---|
| Departamentos afetados | DEP-GOV (guarda da fronteira e conferencia do portao); DEP-QAR (G4); DEP-KMS (curadoria da proveniencia) |
| Componentes afetados | **Nenhum** — nao existe componente |
| Entidades novas | **Zero** — universo permanece em 21 (FND-09 §5) |
| Tipos documentais novos | **Zero** — universo permanece em 33 (FND-10 §4) |
| Camadas de memoria a atualizar | EST (fronteira e identidade) |
| Decisoes superadas | **Nenhuma.** ADR-0001 e **complementado**: ele declarou a Fundacao como fonte oficial de verdade; este declara que nada de fora entra nela sem rito |
| Documentos a atualizar | FND-03 §8 (3 termos de vocabulario) · FND-10 §10.4 (1 regra) · catalogo mestre (§5 proveniencia) · `README.md` da raiz |
| Arquivos do acervo reescritos | **Zero** |
| Custo e dependencia criados | Nenhuma dependencia externa. Custo: as condicoes G1–G5 tornam qualquer admissao futura mais cara que uma copia — deliberadamente |
| Ganho PI-14 | **Organizacao** — a decisao de admissao passa a ter lugar unico, anterior ao caso e conferivel sem julgar merito |

## 8. Evidencias

| # | Evidencia | Origem (ID) | Confianca | O que ela discrimina |
|---|---|---|---|---|
| E1 | Quatro decisoes C3/Tipo 1 trataram precedente como ato de autoridade | [INC-2026-001](../governance/incidents/INC-2026-001-ratificacao-inferida.md) §1 e §5 | **Alta — verificavel** | Mostra que P1 e defeito **observado** neste acervo, nao risco teorico. Elimina a Alternativa Z |
| E2 | A unica norma sobre origem externa governa forma, nao admissao | FND-03 §9 | **Alta — verificavel** | Elimina a Alternativa B |
| E3 | Regra de nao-proliferacao exige ganho com sinal **ja observado** | FND-04 §6.1, SE-01 | **Alta** | Elimina a Alternativa C |
| E4 | FND-04 §2 define C2 como mudanca que muda *"escopo, **fronteira**, interface ou padrao"* | FND-04 §2 | **Alta — verificavel** | Sustenta a classificacao de §11 |
| E5 | Acervo integralmente produzido neste sistema: 85 artefatos, 18.916 linhas | `wc -l`, 2026-07-28; [catalogo mestre §2](../governance/artifact-registry.md) | **Alta — medida** | Sustenta `native` como padrao e a migracao zero |

**Evidencia ausente, declarada (VD-05):** **nao ha nenhum candidato real, nenhum dado sobre o
conteudo do LucaX Legacy e nenhuma tentativa de importacao observada.** Esta decisao e
integralmente preventiva. Nao existe medicao possivel do seu ganho antes do primeiro
candidato, e apresenta-la como ganho ja realizado seria maquiagem (PI-10).

## 9. Riscos e mitigacao

| # | Risco | Probabilidade | Impacto | Mitigacao prevista |
|---|---|---|---|---|
| R1 | O portao nao caber no primeiro caso real | Media | Baixo | C2 reversivel; o primeiro candidato e gatilho de revisao declarado (§12). Ajustar cinco condicoes e barato |
| R2 | FR-03 ser lido como proibicao de **olhar** o Legacy | Media | Medio | FR-04 e FR-05 distinguem consultar de importar, em texto expresso |
| R3 | `Programa de Migracao`, por estar nomeado, gerar expectativa de existencia | Baixa | Baixo | Declarado **nao iniciado**, sem dono, sem prazo e sem artefato. Nomear e o que impede que seja inventado depois com outro nome |
| R4 | Proveniencia curada divergir do acervo por falta de automacao | Media | Baixo | Mesma mitigacao de A4 de REV-ARTIFACT: RG-03 e verificacao a cada C2/C3 |
| R5 | **Esta decisao estar errada** — a fronteira ser rigida demais e barrar reuso legitimo | Baixa | Medio | ADOPT existe justamente para o reuso integral. O portao encarece a copia, nao o reuso decidido |

## 10. Plano de reversao

| Campo | Conteudo |
|---|---|
| Como desfazer | ADR de revogacao superando este; os tres termos saem de FND-03 §8 por versao MENOR; a coluna de proveniencia sai do catalogo |
| Custo da reversao | **Trivial** |
| Por que a reversao e trivial (Tipo 2) | Nao cria componente, nao cria entidade, nao cria dependencia externa, nao altera nenhum artefato existente e nao tem consumidor — nada foi construido sobre esta decisao |
| Janela | Permanente enquanto nao houver admissao pelo portao. Apos a primeira admissao, reverter exige tratar o artefato admitido (EV-06) |
| Quem executa | DEP-GOV, sob aprovacao de DEP-EXE |
| Backup necessario (PI-07) | Nenhum — nenhum dado vivo e tocado |

## 11. Classificacao

| Campo | Valor |
|---|---|
| Classe de mudanca | **C2 — Estrutural** |
| Tipo de reversibilidade | **Tipo 2** — reversao trivial, sem consumidores |
| Decisor | DEP-EXE, com parecer de DEP-GOV |
| Ratificador | **Nao aplicavel** — C2/Tipo 2 nao exige ratificacao (FND-04 §2.2, FND-07 §2.3) |
| Data da decisao | 2026-07-28 |
| Data de vigencia | 2026-07-28 |

> **Por que C2 e nao C3.** FND-04 §2 define C2 como a mudanca que *"muda escopo, **fronteira**,
> interface ou padrao"* — a hipotese literal desta decisao. C3 exige alterar principio
> imutavel, linha vermelha, **hierarquia normativa**, direitos de decisao ou a propria
> Fundacao. Este ADR nao altera a hierarquia de FND-01 §10: declara que uma origem **externa**
> nao esta nela, e nao move nenhum nivel interno. Nao altera direitos de decisao: quem aprova
> cada classe continua o mesmo. GV-03 — na duvida, a classe mais alta — foi considerado e nao
> se aplica, porque nao ha duvida a resolver: a hipotese de C2 nomeia "fronteira"
> explicitamente. A analise fica registrada para que a classificacao seja auditavel, e nao
> apenas afirmada.

## 12. Revisao

| Campo | Conteudo |
|---|---|
| Gatilho por evento | **Primeiro candidato real** submetido ao portao — reavaliar se G1–G5 sao suficientes e conferiveis na pratica |
| Gatilho por evento | **Inicio do Programa de Migracao** — reavaliar se ADR proprio basta ou se o esforco exige `PRJ` |
| Gatilho temporal | 2027-01-28 — revisao semestral da Fundacao |
| Sinal de que esta decisao deu errado | (a) O portao ser cumprido formalmente e admitir conteudo que duplica artefato vigente — sinal de que G2 nao discrimina; (b) nenhum candidato submetido ate a segunda revisao estrutural, com o Legacy em uso — sinal de que o portao esta sendo contornado, nao respeitado |
| Responsavel pela revisao | DEP-QAR |

## 13. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Origem | [RFC-0005](../rfcs/RFC-0005-fronteira-greenfield-legado.md) |
| Decisoes superadas | Nenhuma |
| Decisoes relacionadas | [ADR-0001](ADR-0001-adocao-da-fundacao-organizacional.md) — complementado; [ADR-0003](ADR-0003-adocao-do-enterprise-meta-model.md) — universo fechado preservado; [ADR-0006](ADR-0006-adocao-do-enterprise-artifact-framework.md) — contrato de artefato, do qual FR-09 deriva |
| Artefatos alterados | FND-03 v1.3.0 (§8) · FND-10 v1.1.0 (§10.4, RG-06) · [catalogo mestre](../governance/artifact-registry.md) §5 · `README.md` da raiz |
| Registros de memoria gerados | Camada EST — identidade e fronteira (via este ADR; nenhum registro `MEM` separado, para nao duplicar fonte) |
| Verificacao de aptidao | [FIT-2026-003](../governance/fitness/FIT-2026-003-consolidacao-baseline.md) (QG-6, CV-07) |

---

## Checklist de validade (FND-07 §4.1)
- [x] VD-01 — 3 alternativas reais + "nao fazer nada"
- [x] VD-02 — criterios declarados antes da escolha (§3 antes de §4)
- [x] VD-03 — nenhuma alternativa de palha: B e a norma vigente estendida, C e a solucao completa
- [x] VD-04 — tradeoff aceito explicito (§6)
- [x] VD-05 — ausencia de evidencia sobre o Legacy declarada (§8)
- [x] VD-06 — reversao declarada trivial, com justificativa (Tipo 2)
- [x] VD-07 — impacto em cascata mapeado e executado (§7)
- [x] VD-08 — data e responsavel presentes
- [x] VD-09 — gatilhos de revisao definidos (§12)
