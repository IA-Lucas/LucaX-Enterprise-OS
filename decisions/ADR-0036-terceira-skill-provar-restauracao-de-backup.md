---
id: ADR-0036-terceira-skill-provar-restauracao-de-backup
titulo: A terceira Skill do acervo — provar restauracao de backup — e o PISO DE n de SK-24, medido no primeiro n em que a regra pode disparar
tipo: adr
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-08-03
atualizado_em: 2026-08-03
revisao_prevista: 2027-02-03
decisoes_relacionadas: [ADR-0033, ADR-0034, ADR-0035]
substitui: []
substituido_por: null
classe_mudanca: C2
tipo_decisao: 2
supera: null
superado_por: null
resumo: Cria a terceira Skill do acervo a partir do candidato custodia-provar-restauracao-de-backup, mede o piso de n de SK-24 no primeiro n em que a regra admite solucao, fecha SK-09 e SK-10 como defeitos do Framework por repeticao em materia disjunta, corrige a razao registrada da nao-exercicio de SK-21 e mede o que nascer sob as 26 reduz.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# ADR-0036: A terceira `Skill`

## Contexto

`ADR-0034` e `ADR-0035` criaram as duas primeiras `Skill`s e mediram `SK-01` a `SK-26` **duas
vezes**, sobre materias disjuntas. Tres defeitos ficaram **declarados e nao sanados**, porque
`ADR-0033` e **`M1`** e corrigi-lo exige **`ADR` sucessor**:

| Defeito | Natureza | Estado apos `n = 2` |
|---|---|---|
| **`SK-09`** | ❌ **DEFEITUOSA** — erro de categoria: soma `gatilho`, **atributo de frontmatter**, aos **blocos de corpo** | Sinal **maduro** |
| **`SK-10`** | ⚠️ **INSUFICIENTE** — remete a classe **sem advertir** que `C2` arrasta `RFC` → `ADR` → `FIT` → ficha → contador | Sinal **maduro** |
| **`SK-24`** | ⚠️ **INSUFICIENTE** — falta o **piso de `n`** | ⛔ **Sinal IMATURO: a regra e estruturalmente vazia ate `n = 3`** |

**`PT-2026-022` recomendou ESPERAR a terceira `Skill`**, e o motivo se sustenta: **o sucessor
tambem sera `M1`, e errar nele custa outro sucessor.**

## Decisao

**Criar `SKL-custodia-provar-restauracao-de-backup`** — a **terceira `Skill`** do acervo —,
recebendo o candidato produzido pela **F8** *(fora do acervo, ja sob `SK-01` a `SK-26`)*, cujo
merito e **exercicio real** no `nxtrack`.

## Classe — determinada por norma citada, nunca por analogia

| Variavel | Valor | Fundamento |
|---|---|---|
| **Classe** | **`C2`** | `FND-04 §6`, linha *Skill* — **`C2` e o piso de criacao**; `FND-04 §2.1`: `C2` → **`RFC` → `ADR`** |
| **Tipo** | **`2` — reversivel** | `FND-04 §2.2`. `SKL` e **`M2`** (`FND-10 §6.2`) |
| **Aprovador** | **`DEP-EXE`**, com parecer de **`DEP-GOV`** | `FND-04 §2.2`, celula `C2 × Tipo 2`; `FND-09 §8.2` linha `SKL` |
| **Ratificacao** | **nao exigida** | `FND-09 §8.2` linha `SKL`, coluna *Ratifica* = **`—`**. **`0` atos** |

**Precedente identico, conferido no frontmatter e nao de memoria:** `ADR-0034` e `ADR-0035`.

---

## 1. `SK-24` — o piso de `n`, PROVADO

### 1.1 O enunciado, e o que lhe falta

`SK-24` recebe `CE-05`: *"`Skill` que ultrapasse **o dobro da mediana do seu tipo** e candidata a
especializacao"*. **O enunciado nao declara para qual `n` ele vale.**

### 1.2 O calculo com `n = 3` — medido, nunca estimado

| Grandeza | Valor |
|---|---|
| Instancias, por `wc -l` | **`175`** *(`custodia-criar-copia-datada`)* · **`188`** *(`seguranca-varrer-credencial`)* · **`231`** *(esta)* |
| **Mediana** | **`188`** |
| **Limiar** *(o dobro)* | **`376`** |
| **Maior instancia** | **`231`** — e e **esta** |
| **Veredito** | **`231` > `376` e FALSO — NAO dispara.** **`0`** candidatas a especializacao |

### 1.3 ⭐ O que muda: a regra deixou de ser VAZIA

**Nao disparar em `n = 3` nao e o mesmo fato que nao disparar em `n = 2`**, e a diferenca e
**estrutural, nao quantitativa**. Com instancias ordenadas e positivas:

| `n` | Mediana | Condicao para disparar | Conjunto-solucao |
|---|---|---|---|
| **`1`** | `a` | `a > 2a` ⟺ **`a < 0`** | ⛔ **VAZIO** — impossivel para qualquer valor |
| **`2`** | `(a+b)/2` | `b > a + b` ⟺ **`a < 0`** | ⛔ **VAZIO** — impossivel para qualquer valor |
| **`3`** | `b` | **`c > 2b`** | ✅ **NAO VAZIO** — satisfeito, p. ex., por `(1, 1, 3)` |

> **`n = 3` e o PISO: o primeiro `n` em que `SK-24` pode devolver *"sim"*.** Abaixo dele o teste
> **so podia devolver *"nao"*** — e teste com uma unica resposta possivel **nao esta medindo**.
> **Em `n = 3` a regra virou teste de verdade, e respondeu *"nao"* por propriedade das INSTANCIAS
> — as tres tem tamanho comparavel —, nao mais por impossibilidade algebrica.**

**Concretamente, o que teria disparado:** uma terceira `Skill` com **mais de `376` linhas** — mais
que o **dobro** da mediana, e **`63%`** acima desta, que ja e a maior das tres. **Isso e informacao
sobre a REGRA, nao sobre esta `Skill`.**

### 1.4 O remedio, formulado para o `ADR` sucessor — e NAO aplicado aqui

**`SK-24` precisa declarar o piso:** *o teste de dispersao **nao se aplica** enquanto o tipo tiver
menos de **`3`** instancias; abaixo disso o custo continua **medido** (`CE-02`), e apenas o
**gatilho de especializacao** fica suspenso.*

> ⛔ **Este `ADR` NAO escreve esse remedio.** `ADR-0033` e **`M1`**: corrigir uma virgula exige
> **`ADR` sucessor**. **O que este `ADR` entrega e o SINAL MADURO** — o piso **medido**, e nao mais
> conjecturado.

## 2. `SK-09` e `SK-10` — a TERCEIRA reprovacao, sobre a terceira materia

| Regra | Reprovou? | Como |
|---|---|---|
| **`SK-09`** | ❌ **SIM, IDENTICAMENTE — `3` de `3`** | A ficha materializa o `gatilho` **duas vezes** — campo de frontmatter **e** §1. ⚠️ **E desta vez o autor SABIA:** o candidato dedicou um §0 a separar as categorias — **e o defeito ocorreu assim mesmo**, porque **esta na norma, nao no autor** |
| **`SK-10`** | ⚠️ **SIM, IDENTICAMENTE — `3` de `3`** | Custou os mesmos **`5`** artefatos. ⚠️ **E desta vez o candidato ADVERTIU do custo em §11** — **a advertencia nao reduziu o custo em nada**, o que prova que a insuficiencia e **do enunciado**, nao da ignorancia do leitor |

### 2.1 As tres materias nao compartilham NADA — e por isso a conclusao fecha

| Eixo | `Skill` 1 | `Skill` 2 | `Skill` 3 |
|---|---|---|---|
| **Materia** | custodia de arvore | credencial exposta | **restauracao de backup** |
| **`Capability`** | `CAP-governanca` | `CAP-seguranca` | **`CAP-infraestrutura`** |
| **Custodio da `CAP`** | DEP-GOV | DEP-GOV | **DEP-OPS** |
| **Idempotencia** | ❌ **nao**, deliberada | ✅ sim | ⚖️ **sim, sob recorte declarado** |
| **Efeito** | **escreve** | le | **escreve e destroi o que escreveu** |
| **Falhas plausiveis-e-erradas** | `1` | `2` | **`2`, e uma delas de classe nova** |

> **Defeito que reaparece IDENTICO em tres casos sem eixo comum e defeito da REGRA, nao do caso.**
> Com `n = 1` era indistinguivel de coincidencia; com `n = 2`, provavel; **com `n = 3` sobre
> materias disjuntas — e com o autor CIENTE do defeito —, fechado.**

## 3. `SK-21` — a unica jamais exercida, e o motivo registrado estava ERRADO

`PT-2026-022` registrou que `SK-21` segue sem caso *"porque `0` agentes existem"*. **Medido aqui, a
razao e outra, e e pior.**

| Clausula de `SK-21` | O que exige para ser EXERCIDA | Estado com `n = 3` |
|---|---|---|
| **(a)** *"`Skill` nao depende de agente"* | ao menos **`1` agente** de que depender | **`0` agentes.** Vacuamente satisfeita — **e so isto o registro anterior alcancava** |
| **(b)** *"a cadeia nao tem ciclo"* (`R-04`) | ao menos **`1` DEPENDENCIA entre componentes** | **`0` dependencias.** As tres `Skill`s sao **mutuamente independentes** |

### 3.1 ⚠️ E a terceira `Skill` chega mais perto do que qualquer anterior — sem chegar

**Esta e a primeira ficha do acervo que REFERENCIA outra `Skill`:** o §Escopo remete a
`SKL-custodia-criar-copia-datada` para dizer **o que ela NAO faz**.

> **Referencia de FRONTEIRA nao e aresta de DEPENDENCIA, e a distincao decide.** `R-04` fala de
> componentes que **dependem de** outros — que **precisam** deles para completar. **Esta `Skill`
> nao invoca a outra, nao a consome e completa sem ela.** Delimitar-se **contra** um vizinho e o
> oposto de depender dele.
>
> **`SK-21` (b) continua com `0` arestas, e agora se sabe que nem a citacao mutua a produz.**

### 3.2 A generalizacao — o entregavel para o sucessor

**`SK-21` e `SK-24` nao sao dois defeitos avulsos: sao a MESMA CLASSE** — *regra cujo antecedente
exige uma populacao ou uma aresta que o enunciado nao declara*.

| Regra | Piso real | Declarado no enunciado? |
|---|---|---|
| **`SK-24`** | **`n ≥ 3` instancias do tipo** | ❌ **nao** |
| **`SK-21` (b)** | **`≥ 1` dependencia entre componentes** | ❌ **nao** |

**O remedio do sucessor generaliza:** **toda regra cujo antecedente dependa de populacao ou de
aresta declara o seu piso** — e, abaixo dele, declara-se **INAPLICAVEL**, nunca **satisfeita**.
**A diferenca importa e e operacional:** *"satisfeita"* entra em `FIT` como ✅ e **desaparece**;
*"inaplicavel"* fica visivel e **cobra o piso**.

## 4. O custo do rito — a TERCEIRA medicao, e ela encerra a questao

| Missao | Artefatos | Reducao |
|---|---|---|
| `1.13.11` — primeira `Skill` | **`5`** | — |
| `1.13.12` — segunda `Skill` | **`5`** | **`0`** |
| **`1.13.13` — terceira `Skill`** | **`5`** | **`0`** |

> **Tres medicoes, `0` reducao — e a terceira e a mais conclusiva das tres**, porque desta vez o
> candidato **declarou o custo antes** *(§11 dele)* e **o custo nao mudou**. **Conhecer o preco nao
> o desconta.**
>
> **A causa e normativa, nao operacional: a classe e do EFEITO** (`AL-01`), e o efeito de criar
> `Skill` e o mesmo toda vez. **`FND-04 §6` diz *"alem do rito da classe"***, e **precedente nao
> dispensa instrumento**. **O barato e o ATO — `0` em tres missoes —, nunca o RITO.**

## 5. ⭐ A quinta medicao — nascer sob as `26` reduziu o retrabalho?

**Medido em [`RFC-0031 §6`](../rfcs/RFC-0031-terceira-skill-provar-restauracao-de-backup.md).**
A decisao que este `ADR` registra:

| Grandeza | `Skill` 1 | `Skill` 2 | **`Skill` 3** | Veredito |
|---|---|---|---|---|
| Reprovacoes por regra do Framework | `1` | `1` | ⭐ **`0`** | ✅ **CAIU** |
| Correcoes de merito na transformacao | nome | nome | **`1`** *(valor vencido de `SK-24`)* | ✅ **caiu** |
| Campos escritos a mao (`RD-122`) | `2` | `2` | **`2`** | ❌ **`0` reducao** |
| `gatilho` materializado duas vezes | sim | sim | **sim** | ❌ **`0` reducao** |
| Artefatos do rito | `5` | `5` | **`5`** | ❌ **`0` reducao** |

> **Decisao de leitura, e ela vale mais que os numeros:** **nascer sob as `26` reduz o RETRABALHO DE
> REDACAO a quase zero, e nao reduz o CUSTO DO RITO em nada.**
>
> **Produzir candidato na fabrica VALE — para uma coisa so.** Poupa vaivem e reprovacao de forma.
> **Nao poupa instrumento**, e quem esperar barateamento do rito por essa via **medira `5` de
> novo**. **A distincao entre as duas economias e exatamente a que `SK-10` nao faz, e e o terceiro
> sinal de que ela precisa ser refeita.**

### 5.1 A unica correcao de merito, e por que ela era INEVITAVEL

O candidato declarou `SK-24` com os valores de `n = 2` — mediana `181,5`, teto `363`. **A ficha
mede `n = 3`: mediana `188`, limiar `376`.** Familia de **`RD-101`** *(artefato que afirma
propriedade que ja nao vale)*.

> **Nenhuma disciplina do autor o evitaria: o candidato nao podia conhecer a mediana que ele
> proprio ia mudar.** **Ha uma classe de afirmacao que so pode ser feita no momento da admissao**,
> e o candidato produzido antes **necessariamente** a traz vencida. **Isso e limite do metodo de
> fabrica, nao descuido da F8** — e fica registrado como tal.

## 6. O que este ADR NAO faz

| # | Nao faz | Verificacao |
|---|---|---|
| **N1** | **Nao abre o `ADR` sucessor de `ADR-0033`** | Os tres defeitos seguem **declarados e nao sanados**. §1.4 e §3.2 entregam o **sinal**, nao o remedio |
| **N2** | **Nao promove `ADR-0033` a `FND`** | `C3 · Tipo 1` **com ato** — precedente `ADR-0022` |
| **N3** | **Nao emenda fonte alguma** | **`0` bytes** em `FND-01` a `FND-11` |
| **N4** | **Nao emenda `TPL-skill` nem sana `RD-122`** | **`0` bytes.** `RD-122` **exercido pela TERCEIRA vez** |
| **N5** | **Nao move codigo para o acervo** | **`0` bytes.** A implementacao permanece no `nxtrack`; o canonico recebe a **ficha** |
| **N6** | **Nao admite o segundo candidato da F8** | `CANDIDATO-SKL-engenharia-separar-regra-geral-de-decisao-medida` segue **fora**, **intacto** — *um por missao* |
| **N7** | **Nao escreve no `nxtrack`** | **`0` bytes.** Lido em **somente leitura** |
| **N8** | **Nao cria nem libera portao** | **`GO-TO-SKILLS` continua EXERCIDO e NAO liberado** (`FND-01 §6.2`). Portoes de sequencia por nome: **2 antes, 2 depois**. `QG-0`–`QG-6`: **7 e 7** |
| **N9** | **Nao altera o medidor de baseline** | **`0` bytes em `baseline.sh`**, inclusive diante do `EXIT=2` do portao de raiz sobre a copia datada — **setima** ocorrencia de `RD-53`/`RD-81` |

## 7. Limites declarados

| # | Limite |
|---|---|
| **L1** | **`SK-24` nao disparou.** O que se provou e que **podia** — o piso, nao o disparo |
| **L2** | **`3` instancias ainda sao poucas para mediana estavel.** Uma quarta `Skill` **move o limiar**, e o veredito pode mudar **sem que nenhuma ficha mude** |
| **L3** | **`SK-21` continua NAO exercida**, e agora se sabe que **nao basta criar `Skill`s** nem cita-las entre si |
| **L4** | **A ancoragem do veredito nao tem portao que a imponha** — o modo de falha *"o veredito que viaja"* depende de o consumidor **comparar**. `SK-19` obriga a **declarar**, nao a **impedir** |
| **L5** | **O merito vem de exercicio em UM produto** *(`nxtrack`, `restic`, um banco)*. **A `Skill` e escrita como geral e foi provada como particular** — e a generalidade e **projetada**, nao observada |

## 8. Consequencias

| Para quem | O que muda |
|---|---|
| **DEP-OPS** | Ganha instrumento para o quarto elo de `A3` — *"restaurar e abrir o que voltou"* —, que era o unico dos quatro **sem artefato canonico** |
| **DEP-GOV** | **Ponto de retorno de ato passa a poder ser PROVADO, nao so datado.** E o que `RD-103` mostrou faltar |
| **DEP-QAR** | Ganha base para **veto por continuidade nao provada** |
| **DEP-GOV** *(Framework)* | Recebe o **sinal maduro** dos tres defeitos, mais a **quinta medicao**. **O `ADR` sucessor deixa de estar bloqueado por falta de medicao** |
| **Quem for criar a quarta `Skill`** | **Escrevera `gatilho` e `capabilities` a mao pela QUARTA vez** *(`RD-122`)*, **pagara `5` artefatos** e **movera o limiar de `SK-24`** |

## 9. Rastreabilidade

| Campo | Conteudo |
|---|---|
| **Origem** | [RFC-0031](../rfcs/RFC-0031-terceira-skill-provar-restauracao-de-backup.md) → este ADR |
| **Origem do merito** | Candidato da **F8**, fora do acervo, ja sob `SK-01` a `SK-26`; exercicio real no `nxtrack`, missao **I1**, regra `A3` e prova **(c) `PASSOU`** |
| **Framework** | [ADR-0033](ADR-0033-framework-de-skills.md) — `SK-01` a `SK-26` |
| **Artefato criado** | [`SKL-custodia-provar-restauracao-de-backup`](../skills/SKL-custodia-provar-restauracao-de-backup.md) |
| **Verificacao de aptidao** | [FIT-2026-029](../governance/fitness/FIT-2026-029-terceira-skill.md) |
| **Registro da missao** | [PT-2026-023](../governance/relatorio-transicao-2026-08-03-terceira-skill.md) |
| **Achados que este ADR NAO fecha** | **`RD-122`** *(terceira ocorrencia)* · `RD-53`/`RD-81` *(**setima** da familia)* · **`RD-103`** *(o dano e irreversivel; esta `Skill` reduz repeticao, nao desfaz)* · `RD-116` |
| **Gatilho de revisao** | A **quarta `Skill`** *(move o limiar de `SK-24`)*; **ou** a primeira **dependencia entre componentes** *(exerce `SK-21` (b))*; **ou** a primeira troca de destino de backup *(exerce o modo de falha II)* |
| **Data de reavaliacao** | **2027-02-03** |
