---
id: ADR-0032-separacao-de-proponente-e-aprovador-na-spec-c1
titulo: Emenda C3 que sana RD-91 — para Spec de classe C1, aprova DEP-EXE, porque FND-04 §3.1 veda ao proponente aprovar a si proprio
tipo: adr
versao: 1.0.0
status: aprovado
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-08-02
atualizado_em: 2026-08-02
revisao_prevista: 2027-02-02
decisoes_relacionadas: [ADR-0018, ADR-0019, ADR-0021, ADR-0022, ADR-0023, ADR-0031]
substitui: []
substituido_por: null
classe_mudanca: C3
tipo_decisao: 2
supera: []
superado_por: null
resumo: Faz a aprovacao de Spec C1 passar do proprietario para DEP-EXE em FND-09 §8.2, com cascata em FND-11 §5 e propagacao a duas Cartas, tornando utilizavel o piso C1 que RD-91 provou nulo.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: pendente
---

# ADR-0032: Para `Spec` de classe `C1`, aprova `DEP-EXE`

> **Este ADR depende de ratificacao e NAO esta em vigor.** `status: aprovado` ·
> `ratificacao: pendente`. Enquanto o campo disser `pendente`, **nada aqui produz efeito**
> (`LM-02`; `FND-10 §5.4`), e as quatro versoes candidatas vivem **fora do acervo**, como
> diff literal e hash, em [PS-2026-017](../governance/pacote-soberano-2026-08-02-rd-91.md).

## Proposito

Sanar **`RD-91`** na **fonte**: separar quem propoe de quem aprova uma `Spec` de classe `C1`,
de modo que o piso que [FND-04 §6](../foundation/04-governanca.md) fixa volte a ser
utilizavel — **sem** encarecer a `Spec`, **sem** tocar regra de conteudo e **sem**
reclassificar `SPC-001`.

## Escopo

| Item | Definicao |
|---|---|
| **Inclui** | `FND-09 §8.2`, linha `SPC`, coluna *Aprova* *(fonte)* · `FND-11 §5`, matriz de `SF-10`, celula *Aprovacao* × `C1 · T2` *(cascata)* · Cartas de **DEP-PRD** e **DEP-EXE** *(propagacao obrigatoria, `CV-04`)* |
| **Nao** inclui | `DoR` (`SF-23`), `DoD` (`SF-24`), criterio de aceite, semantica normativa, perfis, rastreabilidade, mudanca e economia de contexto — **`SF-01` a `SF-09` e `SF-11` a `SF-32` ficam com `0` bytes alterados** · a celula **`C0 · T2`** · as linhas **`PRJ`** e **`TPL`** de `FND-09 §8.2` · a **classe de `SPC-001`** · `FND-04` *(`0` bytes)* · `E2`, `Q3`, `Q4`, `RD-88`, `RD-90` · criar `Spec`, `Produto` ou `Capability` |
| **Subordinado a** | [FND-01](../foundation/01-constituicao.md) *(nivel 1 — `PI-05`, `LV-03`, `§10`)* · [FND-04](../foundation/04-governanca.md) *(que este ADR **aplica** e nao altera)* |
| Origem | [RFC-0027](../rfcs/RFC-0027-separacao-de-proponente-e-aprovador-na-spec-c1.md) → este ADR |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| **Propoe / autor** | **DEP-GOV** | FND-09 §8.2, linha `FND` — *propoe/cria*. Residuo `RD-39` declarado em `RFC-0027 §Responsaveis` |
| **Materia** | **DEP-PRD** e **DEP-EXE** | Consulta obrigatoria — sao as duas Cartas emendadas. Manifestacoes em `RFC-0027 §10` |
| **Revisor** | **DEP-QAR** | FND-09 §8.2, linha `FND` — *revisa*; `AC-03` |
| **Aprova e ratifica** | **SOBERANO** | **C3**, indelegavel (FND-04 §2; FND-09 §8.2, linha `FND`; `SF-32`; `LM-02`) |

## 1. Contexto

A **primeira `Spec` real do acervo** exerceu a matriz de autoridade em vez de le-la, e a
matriz quebrou. `SPC-001` nasceu em **`C2 · Tipo 2`**, uma classe acima do piso, porque em
`C1` a aprovacao seria **nula**. O contorno funcionou e custou **3 artefatos que nao vieram
da materia** — `RFC-0026`, `ADR-0031` e `FIT-2026-024`.

**O achado foi registrado como defeito de `FND-11 §5`.** A medicao desta missao mostra que a
sede e outra, e a diferenca decide onde se emenda.

## 2. Problema

**Tres fontes vigentes, e a composicao delas e nula.**

| Fonte | O que diz | Efeito para `SPC` |
|---|---|---|
| [`FND-09 §8.2`](../foundation/09-meta-model.md), linha `SPC` | *Propoe/cria* = **DEP-PRD**; *Aposenta* = **DEP-PRD** | DEP-PRD e **proponente** e **proprietario** |
| [`FND-04 §2`](../foundation/04-governanca.md), bloco `C1` e `§2.1` | *Aprovador* = **proprietario do artefato**, com revisor de papel distinto | O aprovador **e o proponente** |
| [`FND-04 §3.1`](../foundation/04-governanca.md) | *"`Proponente ≠ Aprovador` (PI-05)"* · *"Acumulo indevido de papeis torna a aprovacao **nula** (`LV-03`)"* | **A aprovacao e nula** |

**E a celula que o achado nomeia nao e sede de nada.** Confronto literal, feito por
ferramenta:

| Metade da colisao | `FND-11 §5` | Fonte | Veredito |
|---|---|---|---|
| Quem propoe | `**DEP-PRD**` | `FND-09 §8.2` linha `SPC`, *Propoe/cria*: `DEP-PRD` | **reproducao literal** |
| Quem aprova | `proprietario **+ revisor**` | `FND-04 §2.1` linha `C1`, *Aprova*: `Proprietario + revisor` | **reproducao literal** |

`FND-11 §5` declara-se **projecao** (`PJ-02`). `PJ-03` poe *"em divergencia, a fonte prevalece,
e o defeito e da projecao"*, e `FND-01 §10` poe *"sobre autoridade, prevalece sempre o
documento de origem"*. **Logo: emendar so `FND-11` nao sanaria — criaria divergencia.**

## 3. Criterios de decisao

Os **sete** de [RFC-0027 §4](../rfcs/RFC-0027-separacao-de-proponente-e-aprovador-na-spec-c1.md):
`K1` sanar na fonte · `K2` nao ampliar titular · `K3` nao reabrir o merito das classes ·
`K4` nao encarecer a `Spec` · `K5` nao tocar regra de conteudo · `K6` propagar na mesma
mudanca · `K7` nao emendar fundacional alem do necessario.

## 4. Alternativas consideradas

As **quatro mais `Z`** de [RFC-0027 §5](../rfcs/RFC-0027-separacao-de-proponente-e-aprovador-na-spec-c1.md).
**`A`** *(so `FND-11`)* falha `K1` **por medicao**, nao por preferencia. **`C`** *(regra
generica de `FND-04 §2`)* falha `K3` e `K7`. **`D`** *(elevar o piso a `C2`)* falha `K4` —
compra a correcao pelo preco que a missao existe para evitar. **`Z`** deixa o piso
inutilizavel. **Vence `B`.**

## 5. Decisao *(depende de ratificacao)*

| # | Conteudo |
|---|---|
| **`H1`** | Em **`FND-09 §8.2`**, linha `SPC`, coluna *Aprova*: de `conforme classe (FND-04 §2)` para **`conforme classe (FND-04 §2); em **C1**, **DEP-EXE**`** |
| **`H2`** | **`FND-09 §8.2`** recebe **uma nota** que declara a derivacao: a celula **nao redefine `FND-04 §2`** — **aplica `FND-04 §3.1`** ao unico caso em que a propria matriz torna o default de `§2` impossivel |
| **`H3`** | Em **`FND-11 §5`**, matriz de `SF-10`, linha *Aprovacao*, coluna `C1 · T2`: de `proprietario **+ revisor**` para **`**DEP-EXE** + revisor`** — **cascata**, na mesma mudanca (`CV-04`; `ADR-0019 §4`, Alternativa E) |
| **`H4`** | A declaracao **`PJ-02`** de `FND-11 §5` acrescenta **`FND-04 §3.1`** a lista de fontes, porque o valor projetado passa a derivar tambem dela |
| **`H5`** | **`FND-11 §2`** recebe **nota de alcance temporal**: §2.1 e §2.2 descrevem a **recepcao em `1.0.0`**; a partir de `1.1.0` a matriz difere em **1** celula da copia de `ADR-0021 §5.3` — **prevalece `FND-11`**, por `ADR-0022 §5.4` |
| **`H6`** | **Carta de DEP-PRD 1.1.0 → 1.2.0**: `§4`, `§5`, `§5.1` e `§7` — a aprovacao de `Spec` como proprietario passa de `C0` **ou** `C1` para **`C0`** apenas |
| **`H7`** | **Carta de DEP-EXE 1.1.0 → 1.2.0**: `§5` e `§7` — a aprovacao de `Spec` passa de `C2` para **`C1` ou `C2`**, e a nota `"C0/C1: o proprietario"` passa a `"C0: o proprietario"` |
| **`H8`** | Versoes: **`FND-09` 1.6.0**, **`FND-11` 1.1.0**, **`DEP-PRD` 1.2.0**, **`DEP-EXE` 1.2.0**, com as linhas de historico correspondentes |

**Diff literal, hashes integrais e minuta do ato:**
[PS-2026-017](../governance/pacote-soberano-2026-08-02-rd-91.md) §2 e §3.

### 5.1 O que esta decisao **nao** faz

| # | Nao faz |
|---|---|
| **`H9`** | **Nao altera `FND-04`.** `§2`, `§2.1`, `§2.2`, `§3.1` e `§6` ficam com **`0` bytes**. A classe `C1` continua sendo o que `FND-04 §2` diz que ela e |
| **`H10`** | **Nao encarece a `Spec`.** `C1` segue com **Nota de Decisao** como instrumento, **sem** `RFC`, **sem** `ADR`, **sem** `FIT` e **sem** ratificacao. Muda **quem assina**, nunca **o que se exige** |
| **`H11`** | **Nao cria titular.** `DEP-EXE` ja aprova `Spec` `C2` na mesma linha de `FND-09 §8.2` e na mesma matriz de `SF-10`. **`0` nomes novos** (`AU-03`, `K2`) |
| **`H12`** | **Nao toca regra de conteudo de `Spec`.** `SF-01` a `SF-09` e `SF-11` a `SF-32`: **`0` bytes**. `DoR` de 9 e `DoD` de 10 **intactos** — foi dali que veio o rigor de `SPC-001` |
| **`H13`** | **Nao reclassifica `SPC-001`.** Ela nasceu `C2 · Tipo 2` **validamente**, sob a norma vigente a epoca; a emenda **nao retroage** (`LC-01`, `GV-01`) |
| **`H14`** | **Nao sana `C0 · T2`**, que colapsa pela identica razao e **permanece declarado** em `RD-91` |
| **`H15`** | **Nao sana as linhas `PRJ` e `TPL`** de `FND-09 §8.2`, que tem o mesmo defeito, foram **medidas nesta missao** e ficam em `RD-96` e `RD-97`, com dono e gatilho |
| **`H16`** | **Nao determina quem libera `QG-1`.** Segue materia de [ADR-0018](ADR-0018-liberacao-do-portao-qg-1.md): **DEP-EXE**, e **liberar nao e aprovar** (`FND-01 §6.2`; `ADR-0019 H3`) |

## 6. Justificativa

**Por que `DEP-EXE`, e nao outro nome.** `FND-04 §2` ja o nomeia como aprovador no degrau
seguinte (`C2`). Escolher qualquer outro criaria titular — `K2`, `AU-03`. Escolher o revisor
violaria `PI-05` de novo *(Proponente ≠ Revisor, e o revisor nao aprova)*. Escolher o SOBERANO
seria `C3` para toda `Spec`, que e `D` com outro nome.

**Por que a reserva nao reabre `K3`.** `ADR-0019` recusou fixar `DEP-EXE` **na celula inteira**
porque *"tornaria toda Spec `C2`, inclusive as `C0` e `C1`"*. Aqui a **remissao a classe
permanece**, `C0` **nao e tocado**, e `C1` **continua `C1`**. A objecao era ao excesso; esta
reserva e ao exato — e ela **nao inventa criterio**: `FND-04 §3.1` ja vedava o resultado, e a
matriz e que nao tinha percebido.

**O tradeoff aceito, declarado no sentido correto.** Ganha-se um piso utilizavel e a segunda
`Spec` volta a custar **2** instrumentos. Paga-se com **duas Cartas ratificadas emendadas** —
o que exige **ato** — e com **um papel a menos para DEP-PRD**, que era um papel que `LV-03` ja
lhe vedava de fato. **A alternativa barata (`A`) e barata porque nao funciona.**

## 7. Impacto

| Dimensao | Impacto |
|---|---|
| Departamentos afetados | **DEP-PRD** *(perde a aprovacao `C1`)* · **DEP-EXE** *(recebe)* · DEP-GOV *(registra)* · DEP-QAR *(revisa)* |
| Componentes afetados | `FND-09` · `FND-11` · Carta `DEP-PRD` · Carta `DEP-EXE`. **Nada mais** |
| Camadas de memoria a atualizar | Estrategica *(as quatro)*; Operacional *(este registro e o ato)* |
| Decisoes superadas | **Nenhuma.** `ADR-0019` permanece `ativo` e **integro**: seus `H1`–`H8` continuam valendo, e `H1` e **especializado**, nao revogado |
| Documentos a atualizar | Catalogo mestre · indices de `decisions/`, `rfcs/`, `governance/fitness/` · roadmap |
| Custo e dependencia criados | **`0` entidades, tipos, relacoes, estados, portoes, papeis ou classes.** Dependencia: **ato do Soberano** |
| Ganho de `PI-14` | **Reducao de contexto e de custo:** a `Spec` de rotina volta a **2** artefatos contra **5**. Sinal ja observado: `SPC-001` custou os 5, medidos |

## 8. Evidencias

| # | Evidencia | Grau |
|---|---|---|
| `E1` | **Confronto literal** das tres tabelas — a celula de `FND-11 §5` reproduz `FND-09 §8.2` e `FND-04 §2.1` **palavra por palavra** | **Alta.** Reproduzivel por terceiro com `grep`, sem consultar o autor |
| `E2` | `SPC-001` declara `proprietario: DEP-PRD` e `autor: DEP-PRD` no proprio frontmatter — o proprietario **e** o proponente, medido no artefato real | **Alta** |
| `E3` | **6 linhas em 2 Cartas ratificadas** afirmam que `C0`/`C1` e do proprietario — enumeradas uma a uma em `PS-2026-017 §2` | **Alta** |
| `E4` | `ADR-0019 §4` recusou `B` *(fixar DEP-EXE)*, `D` *(emendar `FND-04 §6`)* e `E` *(emendar so a fonte)* — os tres com o motivo escrito | **Alta** |
| `E5` | **`PRJ` e `TPL`** de `FND-09 §8.2` tem o mesmo colapso, lido direto da tabela | **Alta.** `0` achados anteriores o registravam |
| `E6` | Custo da primeira `Spec`: **5** artefatos, **1.580** linhas, por `wc -l` em 2026-08-02 | **Alta**, medida |

**Ausencia de evidencia, declarada:** **nenhuma `Spec` foi criada em `C1` ate hoje** — o
piso nunca foi exercido, porque nasceu nulo. O ganho de `2` contra `5` e **derivado da norma**,
nao observado; o sinal que o confirmaria e **a segunda `Spec` real**.

## 9. Riscos e mitigacao

Os **quatro** de [RFC-0027 §8](../rfcs/RFC-0027-separacao-de-proponente-e-aprovador-na-spec-c1.md),
com `R4` **certo e assumido**: a partir de `FND-11 1.1.0` a matriz difere em 1 celula da copia
de `ADR-0021 §5.3`, que e `M1` e **nunca se emenda** — declarado em `H5` e em `RD-98`.

**O risco de esta decisao estar errada.** Se a leitura de que `FND-04 §3.1` **desloca** o
default de `§2` estiver errada, a emenda tera criado autoridade em `FND-09 §8.2`, que se
declara derivada — e o defeito passaria a ser desta decisao. **O sinal e verificavel:** alguem
citar `FND-09 §8.2` como **fonte** de classe ou de aprovador, em vez de `FND-04 §2`. A nota de
`H2` existe exatamente para tornar esse erro detectavel.

## 10. Plano de reversao

**Tipo 2, e a reversao e barata porque nada foi executado.** Enquanto `ratificacao: pendente`,
**basta nao emitir o ato**: os quatro candidatos vivem fora do acervo e **`0` bytes** foram
escritos nos arquivos vivos. Depois do ato, reverte-se por **emenda revogatoria de mesmo
rito** (`FND-04 §2`, C3), restaurando os quatro `H-A` *vigentes* publicados em
`PS-2026-017 §3` — que sao o ponto de retorno **exato**, arquivo a arquivo.

## 11. Classificacao

| Campo | Valor |
|---|---|
| Classe de mudanca | **C3** — *"altera direitos de decisao"* e emenda **a propria Fundacao** (`FND-04 §2`, bloco `C3`) |
| Tipo de reversibilidade | **2** — emenda revogatoria de mesmo rito, sem execucao a desfazer |
| Decisor | **SOBERANO**, indelegavel (`FND-04 §2`; `FND-09 §8.2` linha `FND`) |
| Ratificador | **SOBERANO** (`LM-02`; `SF-32`) |
| Data da decisao | 2026-08-02 |
| Data de vigencia | **na data do ato** — nao antes |

> **A classe foi determinada por norma citada, nunca por analogia com outra emenda.** Quatro
> fundamentos independentes, e os quatro dizem `C3`: **(1)** `FND-04 §2`, bloco `C3`
> — *"altera ... direitos de decisao ou a propria Fundacao"*; **(2)** `FND-09 §8.2`, linha
> `FND` — *Aprova* **SOBERANO**, *Ratifica* **SOBERANO**; **(3)** `SF-32` — a emenda de
> `FND-11` *"so vigora com aprovacao e ratificacao do SOBERANO"*; **(4)** `LM-02` — `FND` nao
> vigora sem ratificacao. **O `Tipo 2` vem de `FND-04 §2`, bloco `C3`, campo *Reversao***
> — *"emenda revogatoria, com mesmo rito"* —, e `FND-04 §2.2` confirma que `C3` termina em
> ratificacao **em qualquer tipo**, de modo que a distincao **nao afrouxa nada**.

---

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-08-02 | DEP-GOV | Criacao. Decide, **na fonte**, que a aprovacao de `Spec` de classe **`C1`** passa do **proprietario** para **DEP-EXE**, sanando **`RD-91`** — a colisao que tornava **nula** (`LV-03`) a aprovacao de toda `Spec` `C1` e **inutilizavel** o piso de `FND-04 §6`. **Emenda `1` celula de `FND-09 §8.2`** *(de 126)*, **`1` celula da matriz de `SF-10`** *(de 50)* em cascata, e **`6` linhas em `2` Cartas ratificadas**, todas medidas uma a uma. **A celula que `RD-91` nomeava nao era sede:** reproduz **literalmente** `FND-09 §8.2` linha `SPC` e `FND-04 §2.1` linha `C1`, e por `PJ-03` e `FND-01 §10` emendar so a projecao **nao sanaria**. **`0` bytes em `FND-04` · `0` titulares criados · `0` regras de conteudo de `Spec` tocadas** *(`DoR` 9 e `DoD` 10 intactos)* **· `0` entidades, tipos, portoes, papeis ou classes · `SPC-001` NAO reclassificada.** Declara e **nao** corrige: **`C0 · T2`** *(`RD-91`)*, **linha `PRJ`** *(`RD-96`)*, **linha `TPL`** *(`RD-97`)*, a divergencia com `ADR-0021 §5.3` *(`RD-98`)* e o conflito *versao MAIOR × `AL-01`* de `FND-04 §2` *(`RD-99`)*. **`3` alternativas reais + `Z`**, das quais **`A` cai por medicao**. **Nao vigora sem ato** (`LM-02`). |
