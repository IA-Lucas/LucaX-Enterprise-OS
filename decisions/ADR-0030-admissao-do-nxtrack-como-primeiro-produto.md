---
id: ADR-0030-admissao-do-nxtrack-como-primeiro-produto
titulo: Admitir a existencia do nXtrack pelo portao de origem externa com G0 IDENTIDADE e G3 RECOGNIZE, e criar o Produto PRO-nxtrack
tipo: adr
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-PRD
proprietario: DEP-PRD
aprovador: SOBERANO
criado_em: 2026-08-01
atualizado_em: 2026-08-01
revisao_prevista: 2027-02-01
decisoes_relacionadas: [ADR-0007, ADR-0027, ADR-0002, ADR-0003, ADR-0021, ADR-0026]
substitui: []
substituido_por: null
classe_mudanca: C2
tipo_decisao: 1
supera: []
superado_por: null
resumo: Admite a existencia formal do nXtrack como entidade deste acervo, com zero bytes do candidato, e cria o Produto PRO-nxtrack sujeito a ato do Soberano.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: ratificada
---

# ADR-0030: admissao do nXtrack e criacao de `PRO-nxtrack`

> **NAO ESTA EM VIGOR.** `status: em-revisao` · `ratificacao: pendente`. Criar Produto e
> **`C2` · `Tipo 1`** (`FND-04 §6`, linha **Produto**), e `Tipo 1` **exige ratificacao do
> Soberano** (`FND-04 §2.2`; `PI-06`). **Esta missao nao admite Produto, nao emite ato, nao
> cria `Spec` e nao fecha `RD-33`.** Enquanto nao houver ato, `products/` **nao existe** e o
> nXtrack permanece **`legacy-candidate`**.

## Proposito

Registrar a decisao de **admitir a existencia formal** do nXtrack neste acervo, pelo portao de
[ADR-0007 §5.3](ADR-0007-fronteira-greenfield-legado.md) com a condicao `G0` e a classificacao
`RECOGNIZE` de [ADR-0027](ADR-0027-classe-de-admissao-de-existencia-no-portao-de-origem-externa.md),
e de criar o Produto **`PRO-nxtrack`** — **sem admitir um unico byte** do candidato.

## Escopo

| Item | Definicao |
|---|---|
| **Inclui** | A **identidade** do nXtrack · a Carta `PRO-nxtrack` · custodia, interfaces e limites declarados · a entrada de `legacy-candidate` no catalogo `§9` |
| **Nao inclui** | **Codigo, schema, dado, texto ou qualquer byte do candidato** · `Spec` · fechamento de `RD-33` · decisao sobre `E2` · alteracao do repositorio do candidato · **o merito tecnico do produto** |
| **Subordinado a** | [FND-01](../foundation/01-constituicao.md) · [FND-04](../foundation/04-governanca.md) · [FND-08](../foundation/08-capability-framework.md) · [FND-09](../foundation/09-meta-model.md) |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| Proponente | **DEP-PRD** | Custodio de `CAP-produto` |
| Confere o portao | **DEP-GOV** | `ADR-0007 §5.3`; sem julgar merito (`FND-04 §12`) |
| Revisor independente | **DEP-QAR** | `AC-03`; `G4` |
| Aprovador | **SOBERANO** | `FND-04 §6`, linha **Produto** |
| Ratificador | **SOBERANO** | `C2`/**`Tipo 1`** — `FND-04 §2.2` |
| Executor | **DEP-GOV** | |

---

## 1. Contexto

`ADR-0007` instituiu, em 2026-07-28, o portao unico de origem externa **antes de existir
candidato**. Ele foi exercido **uma vez**, na Missao 1.13.4, e o exercicio revelou duas lacunas
que `ADR-0027` fechou em 2026-07-31, criando `G0` e `RECOGNIZE`.

**Este e o segundo exercicio do portao — e o primeiro sob a norma emendada.** É tambem o
gatilho de revisao que `ADR-0027 §12` declarou: *"segunda admissao pelo portao — verificar se
`G0` foi declarado sem esforco e se `RECOGNIZE` descreveu o ato"*.

O Soberano decidiu a via em `PT-2026-009 §1`, decisao **7**: *"Via futura e `S1` com Produto
real (`nXtrack`); `S2` deferida"*. A decisao foi **registrada e nao executada**, e `RD-33`
segue bloqueante desde entao.

## 2. Problema / Pergunta de decisao

A existencia do nXtrack deve ser admitida agora, com que valor de `G0` e que classificacao de
`G3` — ou a admissao deve esperar a ressalva comercial de `PS-2026-013 §7`?

## 3. Criterios de decisao

Herdados de [RFC-0025 §3](../rfcs/RFC-0025-admissao-do-nxtrack-como-primeiro-produto.md),
declarados antes do exame das alternativas.

| # | Criterio | Peso |
|---|---|---|
| `K1` | Nenhum byte do candidato entra sem portao proprio | **Bloqueante** |
| `K2` | Nenhuma afirmacao da admissao nasce falsa | **Bloqueante** |
| `K3` | A custodia e declarada como e, nao como se gostaria | **Bloqueante** |
| `K4` | Nao cria entidade nem tipo documental novo | Alto |
| `K5` | Reversivel a custo medido | Alto |
| `K6` | Nao antecipa `Spec` nem fecha `RD-33` | **Bloqueante** |

## 4. Alternativas consideradas

Analisadas em [RFC-0025 §4](../rfcs/RFC-0025-admissao-do-nxtrack-como-primeiro-produto.md):
**A** *(`IDENTIDADE` + `RECOGNIZE`)*, **B** *(`AMBOS`, trazendo a especificacao tecnica)*,
**C** *(adiar pela ressalva comercial)* e **Z** *(nao fazer nada)*. **B** falha em `K1`, `K2` e
`K5`; **C** falha em `K6` por inversao — o adiamento **nao tem gatilho observavel**.

## 5. Decisao

**Decidimos admitir a existencia do nXtrack e criar `PRO-nxtrack`**, nos termos abaixo.

### 5.1 `G0` — o objeto da admissao: **`IDENTIDADE`**

> **`G0` e declarado ANTES de `G1` e determina qual lista de `G3` se aplica** — `GA-01` de
> `ADR-0027 §5.1`. Quem declara e o **Proponente** (DEP-PRD); quem confere e **DEP-GOV**, sem
> julgar merito (`GA-02`).

| Campo | Valor |
|---|---|
| **`G0` declarado** | **`IDENTIDADE`** |
| Definicao aplicada, literal | *"A **existencia formal** de algo externo, como entidade deste acervo"* — `ADR-0027 §5.1` |
| O que entra no acervo | *"**`0` bytes do externo.** Nasce artefato `native` que **nomeia** o externo"* — idem |
| **Por que nao `CONTEUDO` nem `AMBOS`** | Porque **nenhum conteudo foi submetido**. O objeto da admissao e a existencia; o codigo **permanece no repositorio operacional**, e cada peca dele que um dia queira entrar tera **portao proprio** (`FR-07`) |

### 5.2 `G3` — a classificacao: **`RECOGNIZE`**, determinada e nao presumida

> **A lista de `G3` nao e a mesma para todo `G0`.** `ADR-0027 §5.2` declara, coluna a coluna,
> em que valor de `G0` cada classificacao e aplicavel. Com `G0 = IDENTIDADE`, a lista tem
> **exatamente dois membros** — e a determinacao e feita **entre eles**, com fundamento
> positivo para o escolhido.

| Classificacao | Aplicavel a `IDENTIDADE`? | Fundamento literal | Incide aqui? |
|---|---|---|---|
| **ADOPT** | **Nao** — `CONTEUDO`·`AMBOS` | `ADR-0027 §5.2` | **Fora da lista** |
| **ADAPT** | **Nao** — `CONTEUDO`·`AMBOS` | idem | **Fora da lista** |
| **REWRITE** | **Nao** — `CONTEUDO`·`AMBOS` | idem | **Fora da lista** |
| **RETIRE** | **Sim** — *"qualquer"* | idem | **NAO.** Ver §5.2.1 |
| **`RECOGNIZE`** | **Sim** — *"`IDENTIDADE`, e somente ela"* | idem | **SIM.** Ver §5.2.2 |

#### 5.2.1 Por que **nao** e `RETIRE` — por fato positivo, nao por preferencia

`RETIRE` significa, literalmente, *"nem o problema nem a solucao se aplicam a este sistema"*
(`ADR-0007 §5.4`; `ADR-0027 §5.2`). **O Soberano decidiu o contrario, em texto literal:** a via
futura e `S1` **com Produto real, nomeando o nXtrack** — `PT-2026-009 §1`, decisao 7.
**Registrar `RETIRE` contradiria uma decisao vigente do Nivel 0.** O descarte e por **fato
citado**, nao por juizo do executor.

#### 5.2.2 Por que **e** `RECOGNIZE` — os tres elementos da definicao, verificados um a um

`ADR-0027 §5.2` define `RECOGNIZE` como: *"A existencia e admitida; nenhum conteudo e avaliado,
adotado ou recusado — porque nenhum foi submetido"*, com efeito *"`0` bytes admitidos, **por
definicao da classe e nao por escolha do executor**"*.

| Elemento da definicao | Verificacao |
|---|---|
| *"A existencia e admitida"* | ✅ É **exatamente** o objeto: `G0 = IDENTIDADE`, §5.1 |
| *"nenhum conteudo foi submetido"* | ✅ **Medido:** arquivos do candidato propostos para entrada = **`0`**. A Carta e escrita **neste sistema, do zero** |
| *"`0` bytes admitidos"* | ✅ **Medido:** bytes do candidato copiados para o acervo = **`0`** |

> ### `GA-03` levado a serio — a fronteira entre **consultar** e **avaliar**
>
> `ADR-0027 §12` declara que a classe deu errado se *"`RECOGNIZE` for escolhida em admissao que
> **avaliou** conteudo — sinal de que a classe virou atalho"*. A distincao e feita aqui **de
> propria mao**, e nao por conveniencia:
>
> | O que foi feito | Como se qualifica |
> |---|---|
> | **17 fontes do candidato foram lidas**, congeladas por hash e citadas | **Consulta** — `FR-04` de `ADR-0007`: *"Consultar nao e importar. Observar (…) para produzir evidencia e legitimo e desejavel"*. E **`G1` e `G2` a exigem**: sem ler, nao ha proveniencia nem fit-gap |
> | Fatos medidos do candidato entraram na Carta e no portao | **Evidencia** — entra *"pelo campo `evidencia` do instrumento que a invoca"* (`FR-04`) |
> | **Nenhum arquivo do candidato foi proposto como artefato** | **Por isso nenhum foi avaliado como ADOPT, ADAPT, REWRITE ou RETIRE** |
>
> **`RECOGNIZE` nao afirma que o nXtrack e bom, nem que e ruim.** Afirma que **a existencia foi
> admitida e o conteudo nao foi julgado — porque nao foi submetido**. Esta e a afirmacao
> verdadeira, e e por ela que a classe existe: *"para que nao se precise mentir por eliminacao"*
> (`GA-03`).

### 5.3 O Produto que nasce

| Campo | Valor |
|---|---|
| Identidade | **`PRO-nxtrack`**, em `products/nxtrack/carta.md` (`FND-09 E-17`) |
| Proveniencia do **artefato** | **`native`** — a Carta e escrita neste sistema |
| Proveniencia do **candidato** | **`legacy-candidate`** enquanto nao houver ato; **permanece assim depois dele**, porque `RECOGNIZE` **nao migra nada** |
| Capabilities consumidas | `CAP-produto` · `CAP-inteligencia-artificial` · `CAP-dados` · `CAP-engenharia` · `CAP-operacoes` — **5**, com `VC-03` disparado e declarado (`RD-74`) |
| Estagio | `construcao` |
| Carta candidata | `_missao-1-13-4-4-2026-08-01/candidatos/carta-pro-nxtrack-1.0.0.md`, `H-A` `4d4c12e0…75c5` — **fora do acervo**, por `FR-10` |

> **`AD-01`.** O ato do Soberano **cria** `products/nxtrack/carta.md` a partir do candidato de
> `H-A` `4d4c12e0…75c5`, e **nao antes**. Ate la, `products/` **nao existe** — e afirmar o
> contrario seria admitir Produto sem ato.

> **`AD-02` — o que a admissao NAO autoriza.** Admitir identidade **nao** autoriza: copiar
> codigo, inventariar o repositorio do candidato (`FR-07`), criar `Spec` (`RD-33`), executar o
> produto, abrir os bancos com dado real, nem commitar no repositorio hospedeiro. **Admitir
> conteudo depois e passagem NOVA pelo portao, com `G0` novo** — `RA-1` de `ADR-0027 §9`.

## 6. Justificativa

| # | Fundamento |
|---|---|
| 1 | **Executa decisao vigente do Soberano.** `PT-2026-009 §1` decisao 7 nomeia o nXtrack em texto literal. Nao executa-la mantem `Q1` respondida e ociosa, e `RD-33` travado |
| 2 | **Usa a classe criada exatamente para este caso.** `ADR-0027` nasceu com **um** membro retrospectivo (`RC-1`, medAlly). Esta e a **primeira aplicacao prospectiva** de `RECOGNIZE` — e o gatilho de `§12` disparando |
| 3 | **Custo de entrada zero, medido.** `0` bytes do candidato, `0` fundacionais emendados, `0` artefatos historicos editados |
| 4 | **Tradeoff aceito, e desconfortavel:** o acervo passa a ter um Produto cuja **custodia real esta fora dele**, em subarvore de repositorio de terceiro com 758 caminhos sem commit. Aceita-se porque a alternativa era **nao ter Produto**, e porque a assimetria fica **escrita** (`RD-71`) em vez de descoberta depois |

## 7. Impacto

| Dimensao | Impacto |
|---|---|
| Departamentos afetados | **DEP-PRD** *(proprietario)*; **DEP-ENG** *(construcao)*; **DEP-OPS** *(operacao)*; **DEP-GRW** *(comunicacao)*; **DEP-GOV** *(confere o portao)*; **DEP-QAR** *(`G4`)* |
| Componentes afetados | **Nenhum existente** — este seria o **primeiro** |
| Entidades novas | **`0`** — `PRO` ja e `E-17`. Universo permanece em **21** |
| Tipos documentais novos | **`0`** — universo permanece em **33** |
| **Fundacionais emendados** | **`0` — MEDIDO.** Nenhum `FND` e tocado; `FND-09 E-17` ja preve `PRO` com `Cardinalidade 0..n` |
| Artefatos historicos editados | **`0`** |
| **Bytes do candidato admitidos** | **`0`** — por definicao de `RECOGNIZE` |
| Capabilities vinculadas | **5** — as cinco `vigentes`; `VC-01` satisfeito, `VC-03` **disparado e declarado** |
| Documentos a atualizar | Catalogo `§2`, `§4`, `§7`, `§9`, `§10` · indices `M3` · `README` da raiz |
| Ganho `PI-14` | **Organizacao** — o acervo deixa de ter `0` Produtos com uma decisao de Produto ja tomada e nao executada |

## 8. Evidencias

| # | Evidencia | Origem | Confianca | O que discrimina |
|---|---|---|---|---|
| `E1` | O Soberano nomeia o nXtrack em texto literal, **sem ressalva nesse documento** | [PT-2026-009 §1](../governance/relatorio-transicao-2026-07-30-convergencia.md), decisao 7 | **Alta — literal** | Elimina `RETIRE` e a Alternativa Z |
| `E2` | A ressalva *"primeiro produto comercial"* mora em **outro** artefato; `comercial` tem **`0`** ocorrencias em `PT-2026-009` | [PS-2026-013 §7](../governance/pacote-soberano-2026-07-30-consolidado.md); varredura | **Alta — medida** | Sustenta tratar os dois como **documentos distintos** (`RD-64`) e transformar a ressalva em `Q2` |
| `E3` | `RECOGNIZE` e aplicavel **somente** a `G0 = IDENTIDADE`; `RETIRE`, a *"qualquer"* | [ADR-0027 §5.2](ADR-0027-classe-de-admissao-de-existencia-no-portao-de-origem-externa.md) | **Alta — literal** | Sustenta que a lista tem **dois** membros, nao um — e que a escolha e determinacao, nao unica opcao |
| `E4` | A subarvore do candidato tem **`0`** caminhos sem commit em 183 rastreados; o hospedeiro tem **758** | `git status --porcelain`, 2026-08-01 | **Alta — medida** | Sustenta `G1` e o achado `RD-71` |
| `E5` | A subarvore esta **congelada desde 2026-07-27T18:20:33**: mesmo objeto `tree` em dois commits distintos | `git rev-parse HEAD:<sub>` e `a7fc0946:<sub>` | **Alta — medida** | Sustenta que a fonte nao mudou durante o julgamento |
| `E6` | O candidato **redistribui** a fonte `Anton` sob **SIL OFL** | `assets/brand/source/OFL-Anton.txt` | **Alta — literal** | Sustenta a **unica** obrigacao regulatoria medida |
| `E7` | `0` cobranca implementada; `0` exposicao publica *(porta em `127.0.0.1`)*; `0` politica de privacidade | `compose.beta.yml`; varredura de 9 termos de cobranca e 9 de regulacao | **Alta — medida** | Sustenta os limites de §Limites do pacote — **medidos, nao presumidos** |
| **`A1`** | **Evidencia ausente, declarada (`VD-05`):** **os bancos com dado real NAO foram abertos** — a missao proibe PII. **O numero de usuarios reais nao foi contado**, e nao e afirmado em lugar algum | `PI-10` | — | Impede ler *"1 usuario"* como medicao |
| **`A2`** | **Evidencia ausente, declarada:** **nenhuma entrevista com DJ, nenhum ensaio em CDJ e nenhuma taxa de aceitacao medida.** A hipotese central `H1` esta **aberta** | `spec-tecnica-v1.md §33` | — | Impede ler a admissao como validacao de merito |

## 9. Riscos e mitigacao

| # | Risco | Prob. | Impacto | Mitigacao |
|---|---|---|---|---|
| `RA-1` | **`RECOGNIZE` virar porta de entrada barata**: admite-se identidade hoje e conteudo depois sem portao novo | Media | **Alto** | `AD-02` em texto expresso + `FR-07` *(um candidato por vez, portao proprio a cada vez)*. Admitir conteudo depois **exige `G0` novo** |
| `RA-2` | A admissao ser lida como **aprovacao tecnica** do produto | **Media** | **Alto** | `GA-03` e a evidencia `A2`: `RECOGNIZE` **declara que nao avaliou**. Nenhum controle de merito foi aplicado, e isso esta escrito |
| `RA-3` | O Soberano entender que a ressalva de `PS-2026-013 §7` condiciona o ato | **Media** | Medio | A ressalva vira **`Q2`** do pacote — pergunta explicita, nao pressuposto. O ato pode ser assinado com ou sem ela |
| `RA-4` | A custodia fora do acervo produzir Produto que ninguem consegue governar | **Media** | **Alto** | `RD-71` registrado com dono e gatilho; a fronteira de custodia e **requisito da primeira `Spec`**, nao desta admissao |
| `RA-5` | **Esta decisao estar errada** — o nXtrack nao ser o produto que a organizacao quer | Baixa | Medio | Reversao `Tipo 2` na pratica *(§10)*, ainda que a **mudanca** seja `Tipo 1`: `0` consumidores, `0` `Spec`s, `0` artefatos migrados |

## 10. Plano de reversao

| Campo | Conteudo |
|---|---|
| Reversivel? | **Sim** — a mudanca e `Tipo 1` por **classe** (`FND-04 §6`, Produto), e o **custo medido** de desfazer e trivial enquanto nao houver `Spec` |
| Como desfazer | `ADR` de retirada (`O9`) superando este · `products/nxtrack/` removido · catalogo `§9` volta o nXtrack a `legacy-candidate` **nao admitido** · indices `M3` reconciliados |
| **Custo da reversao — MEDIDO, objeto a objeto** | **1** `ADR` novo · **1** Carta removida · **1** entrada de catalogo `§9` · **5** indices `M3` · **`0`** artefatos historicos · **`0`** fundacionais · **`0`** artefatos migrados *(porque `RECOGNIZE` nao migra nada)* · **`0`** `Spec`s *(nenhuma existe)* · **`0`** consumidores |
| O que **nao** se reverte | **Nada — hoje.** Se existir `Spec` derivada antes da reversao, ela passa a exigir tratamento proprio (`EV-06`), e a reversao deixa de ser trivial. **Janela: enquanto `RD-33` nao fechar** |
| Quem executa | DEP-GOV, sob ato do Soberano |
| Backup (`PI-07`) | Copia datada `_backups/LucaX-Enterprise-OS_2026-08-01_pre-missao-1-13-4-4/` **(586 arquivos, baseline reconferida NA COPIA)** |

## 11. Classificacao — **determinada, nao presumida por analogia**

| Campo | Valor |
|---|---|
| Classe de mudanca | **`C2` — Estrutural** |
| Tipo de reversibilidade | **`Tipo 1`** |
| Decisor | **SOBERANO** |
| Ratificador | **SOBERANO** — `C2`/`Tipo 1` (`FND-04 §2.2`) |
| Instrumento | **`RFC` → `ADR`** — [RFC-0025](../rfcs/RFC-0025-admissao-do-nxtrack-como-primeiro-produto.md) |
| Fitness Check | **Obrigatorio** (`CV-07`) — [FIT-2026-023](../governance/fitness/FIT-2026-023-admissao-do-nxtrack.md) |

### 11.1 A determinacao, hipotese a hipotese

> **A classe nao foi herdada de `ADR-0007` nem de `ADR-0026`.** `AL-01` manda classificar pelo
> **efeito**. `FND-04 §6` ja **nomeia** a linha aplicavel — **Produto: `C2` (`Tipo 1`)** —, e a
> determinacao abaixo confirma que nenhuma hipotese de `C3` incide.

| Hipotese de `C3` (`FND-04 §2`) | Incide? | Como se sabe |
|---|---|---|
| Altera **principio imutavel** | **Nao** | Nenhum `PI-01`–`PI-14` e tocado. `PI-09` e `PI-10` sao **invocados**, nao alterados |
| Altera **linha vermelha** | **Nao** | Nenhuma `LV` criada, removida ou redefinida |
| Altera **hierarquia normativa** | **Nao** | `FND-01 §10` intacta. O Produto **consome** competencia e **nao governa** ninguem — `FND-09 E-17`, campo **Autoridade**: *"Nenhuma sobre atores"* |
| Altera **direitos de decisao** | **Nao** | Quem aprova Produto ja e o Soberano (`FND-04 §6`); quem confere o portao ja e DEP-GOV; quem valida ja e DEP-QAR |
| Altera **a propria Fundacao** | **Nao — MEDIDO** | **`0`** fundacionais emendados. `FND-09 E-17` ja preve `PRO` com `Cardinalidade 0..n`; a primeira instancia **usa** a norma, nao a muda |

**Hipotese de `C2` que incide, literal:** `FND-04 §2`, `C2` — *"**Cria**, altera ou remove **um
componente**"*, com exemplo textual *"**criar produto**"*. **Nao ha interpretacao a fazer: a
hipotese nomeia o ato.**

**`Tipo 1`, determinado e NAO negociado.** `FND-09 E-17` declara: *"Perfil `P1`. **Criacao e
encerramento sao `Tipo 1`, decididos pelo Soberano**"*. `FND-04 §6` repete na linha **Produto**.
**Aqui a norma fixa o tipo por regra, e a medicao de custo de reversao de §10 nao o rebaixa** —
custo baixo **nao** converte `Tipo 1` em `Tipo 2` quando a norma o atribui por natureza do
componente. **`GV-03` nao foi necessario:** nao ha duvida a resolver.

### 11.2 Por que esta decisao tem `RFC`

`FND-04 §2` permite dispensar a `RFC` em `C2` *"se a alternativa unica for obvia **e** DEP-GOV
concordar por escrito"*. **A alternativa nao e unica nem obvia:** `RFC-0025 §4` analisa **tres**
respostas reais — admitir identidade, admitir tambem conteudo, adiar pela ressalva comercial —,
e **a terceira e defensavel o bastante para exigir argumento medido**. Onde ha alternativa
defensavel, a dispensa **nao esta disponivel**.

## 12. Revisao

| Campo | Conteudo |
|---|---|
| Gatilho por evento | **Primeira `Spec` do `PRO-nxtrack`** — verificar se a Carta descreve o produto que a `Spec` encontra |
| Gatilho por evento | **Primeira admissao com `G0 = CONTEUDO`** sobre o nXtrack — verificar se `AD-02` conteve a entrada barata |
| Gatilho por evento | **Publicacao publica do produto** — reabrir os limites de dado real, usuario externo e obrigacao regulatoria |
| Gatilho temporal | 2027-02-01 |
| Sinal de que esta decisao deu errado | *(a)* a Carta virar ficcao: o produto evoluir e ninguem emendar; *(b)* `RECOGNIZE` ser invocada depois para admitir conteudo sem portao novo; *(c)* a admissao ser citada como aprovacao tecnica do produto |
| Dono | **DEP-QAR** |

## 13. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Origem | [RFC-0025](../rfcs/RFC-0025-admissao-do-nxtrack-como-primeiro-produto.md) |
| Decisao do Soberano que a fundamenta | [PT-2026-009 §1](../governance/relatorio-transicao-2026-07-30-convergencia.md), decisao **7** |
| Portao aplicado | [PT-2026-014 §3](../governance/relatorio-transicao-2026-08-01-portao-nxtrack.md) — `G0` a `G5` |
| Evidencia de proveniencia *(nao norma)* | `_missao-1-13-4-4-2026-08-01/evidencia/ITEM-0-proveniencia-nxtrack.md` |
| Carta candidata *(nao norma, fora do acervo)* | `_missao-1-13-4-4-2026-08-01/candidatos/carta-pro-nxtrack-1.0.0.md`, `H-A` `4d4c12e0403344535ec410f4ff71353c1e7feaad6230bc33343f42018cea75c5` |
| Decisoes superadas | **Nenhuma** |
| Decisoes relacionadas | [ADR-0007](ADR-0007-fronteira-greenfield-legado.md) *(portao aplicado, nao emendado — **`0` bytes**)*; [ADR-0027](ADR-0027-classe-de-admissao-de-existencia-no-portao-de-origem-externa.md) *(`G0` e `RECOGNIZE` aplicados pela primeira vez de forma prospectiva)*; [ADR-0026](ADR-0026-admissao-do-medally-como-primeiro-produto.md) *(**`em-revisao`, nao vigente** — **nada dele foi reaproveitado**: este portao foi corrido do zero)* |
| Achados abertos | `RD-71` · `RD-72` · `RD-73` · `RD-74` — **com dono e gatilho, sem missao** |
| Achado invocado | `RD-64` |
| Verificacao de aptidao | [FIT-2026-023](../governance/fitness/FIT-2026-023-admissao-do-nxtrack.md) |
| Pacote soberano | [PS-2026-016](../governance/pacote-soberano-2026-08-01-nxtrack.md) |

---

## Checklist de validade (FND-07 §4.1)

- [x] `VD-01` — 3 alternativas reais + *"nao fazer nada"* (`RFC-0025 §4`)
- [x] `VD-02` — criterios declarados antes da escolha (§3 antes de §4)
- [x] `VD-03` — nenhuma alternativa de palha: `B` e `C` sao respostas naturais, e `C` e a mais forte
- [x] `VD-04` — tradeoff aceito explicito (§6, item 4)
- [x] `VD-05` — **duas** ausencias declaradas (§8, `A1` e `A2`)
- [x] `VD-06` — reversao declarada e **medida objeto a objeto** (§10)
- [x] `VD-07` — impacto em cascata mapeado; **`0` fundacionais alcancados, medido** (§7)
- [x] `VD-08` — data e responsavel presentes
- [x] `VD-09` — gatilhos de revisao definidos (§12)

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-08-01 | DEP-PRD | Decisao inicial, **`em-revisao`, NAO vigente**. Admite a existencia do nXtrack com **`G0 = IDENTIDADE`** e **`G3 = RECOGNIZE`** — a lista aplicavel tem **dois** membros (`RECOGNIZE` e `RETIRE`), e `RETIRE` e descartada por **fato citado** *(decisao 7 de `PT-2026-009`)*, nunca por eliminacao. Cria `PRO-nxtrack` sujeito a ato do Soberano. Classe **`C2`/`Tipo 1`** determinada percorrendo as cinco hipoteses de `C3`, com o `Tipo 1` **fixado por norma** (`FND-09 E-17`) e nao pelo custo medido. Regras `AD-01` e `AD-02`. **`0` bytes do candidato, `0` fundacionais, `0` historicos editados.** |
