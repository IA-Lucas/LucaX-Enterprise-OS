---
id: ADR-0027-classe-de-admissao-de-existencia-no-portao-de-origem-externa
titulo: Acrescentar a condicao G0 e a classificacao RECOGNIZE ao portao de origem externa, superando ADR-0007 5.3 e 5.4 quanto a lista de classificacoes
tipo: adr
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-07-31
atualizado_em: 2026-07-31
revisao_prevista: 2027-01-31
decisoes_relacionadas: [ADR-0007, ADR-0009, ADR-0010, ADR-0026]
substitui: []
substituido_por: null
classe_mudanca: C2
tipo_decisao: 2
supera: [ADR-0007]
superado_por: null
resumo: Acrescenta ao portao de origem externa a condicao G0, que declara o objeto da admissao, e a classificacao RECOGNIZE, que admite existencia sem avaliar conteudo algum.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# ADR-0027: `G0` e `RECOGNIZE` no portao de origem externa

> **NAO ESTA EM VIGOR.** `status: em-revisao`. A decisao so produz efeito quando o aprovador
> da classe a autorizar — **DEP-EXE, com parecer de DEP-GOV** (`FND-04 §2.1`, `C2`). Esta
> missao **nao aplica, nao ativa e nao emite ato**.

## Proposito

Registrar a decisao de acrescentar ao portao de admissao de origem externa a condicao **`G0`**
— que declara **o objeto** da admissao — e a classificacao **`RECOGNIZE`** — que descreve
admitir a existencia de algo externo sem avaliar, adotar ou recusar conteudo algum.

## Escopo

| Item | Definicao |
|---|---|
| **Inclui** | `G0` · `RECOGNIZE` · a regra de reclassificacao `RC-1` a `RC-4` do registro gravado pela Missao 1.13.4 |
| **Nao inclui** | O merito de candidato algum · admissao de Produto · criacao de `Spec` · alteracao de `G1`, `G2`, `G4` ou `G5` · edicao de qualquer artefato historico |
| **Subordinado a** | [FND-01](../foundation/01-constituicao.md) · [FND-04](../foundation/04-governanca.md) · [FND-07](../foundation/07-framework-decisoes.md) · [FND-09](../foundation/09-meta-model.md) |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| Proponente | **DEP-GOV** | Proprietario de `ADR-0007` |
| Revisor independente | **DEP-QAR** | `FND-09 §8.2` linha `ADR`; `AC-03` |
| Aprovador | **DEP-EXE**, com parecer de DEP-GOV | `FND-04 §2.1`, `C2` |
| Ratificador | **Nao aplicavel** — `C2`/`Tipo 2` | §11 |
| Executor | **DEP-GOV** | |

---

## 1. Contexto

O portao de `ADR-0007 §5.3` existiu **tres dias sem candidato** e foi exercido **uma vez**, na
Missao 1.13.4. O exercicio revelou duas lacunas — `RD-54` e `RD-55` — que a leitura nao
revelara em nenhuma das revisoes anteriores.

**A ordem importa e esta registrada:** o portao foi escrito **antes** do primeiro caso, que era
o objetivo declarado de `ADR-0007 §6`; e foi o **primeiro caso** que mostrou onde ele nao
cabia. `R1` de `ADR-0007 §9` previu exatamente isto — *"o portao nao caber no primeiro caso
real"* — e `§12` fixou o gatilho: *"primeiro candidato real submetido ao portao"*. **Este ADR
e o gatilho disparando, nao uma surpresa.**

## 2. Problema / Pergunta de decisao

O portao deve distinguir **admitir identidade** de **admitir conteudo**, e ganhar a
classificacao que descreve a primeira — ou as duas lacunas devem permanecer declaradas?

## 3. Criterios de decisao

Herdados de [RFC-0022 §3](../rfcs/RFC-0022-classe-de-admissao-de-existencia-no-portao-de-origem-externa.md),
declarados antes do exame das alternativas.

| # | Criterio | Peso |
|---|---|---|
| `K1` | Nenhum registro futuro do portao nasce com afirmacao falsa | **Bloqueante** |
| `K2` | Nenhum artefato historico e editado | **Bloqueante** |
| `K3` | Nao amplia entidades nem tipos documentais | Alto |
| `K4` | Nao altera quem decide | **Bloqueante** |
| `K5` | Reversivel | Alto |

## 4. Alternativas consideradas

Analisadas em [RFC-0022 §4](../rfcs/RFC-0022-classe-de-admissao-de-existencia-no-portao-de-origem-externa.md):
**A** *(`G0` + `RECOGNIZE`)*, **B** *(redefinir `REWRITE`)*, **C** *(`G0` sem `RECOGNIZE`)* e
**Z** *(manter declarado)*. **B** e **C** falham no bloqueante `K1` por caminhos opostos; **Z**
adia o custo para o momento em que ele dobra.

## 5. Decisao

**Decidimos acrescentar `G0` e `RECOGNIZE` ao portao**, nos termos abaixo.

### 5.1 `G0` — o objeto da admissao

> Condicao **anterior** a `G1`, que declara **o que se esta pedindo para admitir**.

| Valor de `G0` | Definicao | O que entra no acervo |
|---|---|---|
| **`IDENTIDADE`** | A **existencia formal** de algo externo, como entidade deste acervo | **`0` bytes do externo.** Nasce artefato `native` que **nomeia** o externo |
| **`CONTEUDO`** | Bytes, arquivos, schemas, textos ou estruturas do externo | O que `G3` autorizar, com proveniencia declarada |
| **`AMBOS`** | Identidade **e** conteudo, na mesma admissao | Os dois, com classificacao propria para cada um |

> **`GA-01`.** `G0` e declarado **antes** de `G1` e **determina qual lista de `G3` se aplica**.
> Admissao que nao declara `G0` e **inadmissivel** — nao por rigor, mas porque sem ela `G3`
> nao tem lista definida.

> **`GA-02`.** Quem declara `G0` e o **Proponente**, e quem confere e **DEP-GOV**, sem julgar
> merito — exatamente como `G3` hoje. **Nenhum titular novo, nenhum direito de decisao movido.**

### 5.2 `RECOGNIZE` — a classe que falta em `G3`

A lista de `G3` passa a ter **cinco** classificacoes, e cada uma declara **em que valor de
`G0`** e aplicavel:

| Classificacao | `G0` aplicavel | Significa | Efeito | Proveniencia |
|---|---|---|---|---|
| **ADOPT** | `CONTEUDO` · `AMBOS` | O candidato serve como esta | Entra como artefato novo | `migrated` |
| **ADAPT** | `CONTEUDO` · `AMBOS` | Serve com alteracao para caber na norma | Entra alterado | `adapted` |
| **REWRITE** | `CONTEUDO` · `AMBOS` | **O problema e real, e a solucao externa FOI AVALIADA e nao serve** | Nada entra; produz-se artefato `native` | `native` |
| **RETIRE** | qualquer | Nem o problema nem a solucao se aplicam | Nada entra; registra-se a recusa | `rejected` |
| **`RECOGNIZE`** ⟵ **nova** | **`IDENTIDADE`, e somente ela** | **A existencia e admitida; nenhum conteudo e avaliado, adotado ou recusado — porque nenhum foi submetido** | **`0` bytes admitidos, por definicao da classe e nao por escolha do executor** | `native` |

> **`GA-03`.** `RECOGNIZE` **nao afirma nada sobre o merito do externo.** É a diferenca que
> faltava: `REWRITE` **afirma que avaliou e recusou**; `RECOGNIZE` **declara que nao avaliou**,
> e diz por que — porque nao foi submetido. **A classe existe para que nao se precise mentir
> por eliminacao.**

> **`GA-04`.** **`FR-08` de `ADR-0007` continua valendo e passa a alcancar cinco classes:**
> `REWRITE`, `RETIRE` e `RECOGNIZE` sao **resultados de sucesso** do portao, nao falhas.

### 5.3 O que exatamente e superado — e o que nao e

| Objeto | Estado apos esta decisao |
|---|---|
| **`ADR-0007 §5.3`, linha `G3`** | **SUPERADA quanto a lista**: *"exatamente uma de ADOPT · ADAPT · REWRITE · RETIRE"* passa a ler-se **"exatamente uma da lista de `§5.2` deste ADR, compativel com o `G0` declarado"* |
| **`ADR-0007 §5.4`** | **SUPERADA quanto a completude da tabela**: as quatro linhas **permanecem validas e com o mesmo significado**; acrescenta-se a quinta |
| `ADR-0007 §5.3`, condicoes `G1`, `G2`, `G4`, `G5` | **Intactas** |
| `ADR-0007 §5.1`, `§5.2`, `§5.5`, `FR-01` a `FR-07`, `FR-09`, `FR-10` | **Intactos** |
| **O arquivo `ADR-0007`** | **`0` bytes.** `AL-02` de `FND-04 §7.1` e `LV-04`: *"ADR aprovado nunca e alterado — e superado por novo ADR"*. O campo `superado_por` de `ADR-0007` **nao e preenchido**, pelo precedente literal de `ADR-0022`, que declara `supera: [ADR-0021]` com o `superado_por` de `ADR-0021` **em `null`** |

> **A minuta de origem media este custo como *"1 linha de `ADR-0007`"*. Sao DUAS secoes, e
> nenhuma delas e editada.** A correcao esta aqui porque medir errado o alcance de uma emenda
> e o defeito que `RD-48` nomeia: reversao dada por limpa sem remedir.

### 5.4 Regra de reclassificacao do registro da 1.13.4

> **Esta e a parte que exige mais cuidado, e ela so vale quando esta decisao entrar em vigor.**

| Regra | Conteudo |
|---|---|
| **`RC-1`** | A classificacao `G3 = REWRITE` registrada na Missao 1.13.4 para o candidato `medAlly` **passa a ler-se `G3 = RECOGNIZE`, com `G0 = IDENTIDADE`** — **a partir da vigencia desta decisao, nunca antes** |
| **`RC-2`** | **`PS-2026-014`, `PT-2026-011`, `FIT-2026-019`, `ADR-0026` e `RFC-0021` NAO sao editados.** A reclassificacao vive **aqui**, e quem ler aqueles artefatos encontra o vinculo por esta regra — nunca por reescrita (`CC-01`, `LV-04`, `BL-02`) |
| **`RC-3`** | **O efeito registrado nao muda: `0` bytes admitidos, proveniencia `native`.** A reclassificacao corrige **o nome e a afirmacao**, jamais o resultado. **Nenhum hash muda, nenhuma baseline e reaberta** |
| **`RC-4`** | A reclassificacao **nao revalida o candidato**. `PS-2026-014` continua **submetido e nao aplicado**, e **`Q1` continua bloqueando** |
| **`RC-5`** | **`RC-1` nao entra em vigor com esta decisao redigida.** Enquanto `status` for diferente de `ativo`, o registro da 1.13.4 continua lendo-se `REWRITE`, **com a imprecisao declarada em `RD-55`** |

## 6. Justificativa

| # | Fundamento |
|---|---|
| 1 | **É o gatilho de `ADR-0007 §12` disparando.** O proprio ADR previu que o primeiro caso real testaria se `G1`–`G5` bastam. Bastaram em quatro; faltou em um |
| 2 | **Corrige a causa, nao a ocorrencia.** `FND-04 §10.2` etapa 5 exige *"correcao do efeito **e** correcao da causa"*. Manter declarado corrige nenhuma das duas |
| 3 | **Nasce com membro verificado.** `RECOGNIZE` nao e abstracao especulativa: existe **um** caso medido que nenhuma das quatro classes descrevia. `AQ-03` suspeita de abstracao com menos de dois membros — e por isso `RC-1` e **regra de reclassificacao de um caso nomeado**, nao generalizacao |
| 4 | **Tradeoff aceito:** o portao fica com **cinco** classes onde tinha quatro, e a quinta so e aplicavel num unico valor de `G0`. Aceita-se a assimetria porque a alternativa — uma classe generica que sirva a tudo — e exatamente o que produziu a escolha por eliminacao |

## 7. Impacto

| Dimensao | Impacto |
|---|---|
| Departamentos afetados | **DEP-GOV** *(confere `G0` e `G3`)*; **DEP-QAR** *(`G4`)*; **DEP-PRD** *(proponente tipico)* |
| Componentes afetados | **Nenhum** — `0` Produtos, `0` `Spec`s, `0` componentes existem |
| Entidades novas | **`0`** — universo permanece em **21** (`FND-09 §5`) |
| Tipos documentais novos | **`0`** — universo permanece em **33** (`FND-10 §4`) |
| **Fundacionais emendados** | **`0` — MEDIDO, nao presumido.** Varredura sobre as tres arvores: as quatro classificacoes **nao ocorrem em `FND` algum**. Fora de `ADR-0007`, as ocorrencias sao `ADR-0010 CT-09`, `ADR-0026`, `FIT-2026-003` e projecoes `M3` |
| Artefatos historicos editados | **`0`** |
| Documentos a atualizar | Catalogo `§7` *(`RD-54`, `RD-55`)*; indices `M3` |
| Custo e dependencia criados | **Nenhuma dependencia externa.** Custo: `G0` torna toda admissao futura **uma declaracao mais cara** — deliberadamente |
| Ganho `PI-14` | **Organizacao** — a admissao deixa de precisar escolher entre classes que nao a descrevem |

## 8. Evidencias

| # | Evidencia | Origem | Confianca | O que discrimina |
|---|---|---|---|---|
| `E1` | O portao foi exercido **uma vez** e produziu **duas** lacunas | [PT-2026-011 §3.1](../governance/relatorio-transicao-2026-07-31-admissao-medally.md) | **Alta — verificavel** | Elimina a Alternativa Z: o defeito e **observado**, nao previsto |
| `E2` | `ADR-0026 §5.2` escolhe `REWRITE` **por eliminacao declarada** | [ADR-0026 §5.2](ADR-0026-admissao-do-medally-como-primeiro-produto.md) | **Alta — literal** | Prova que a escolha nao descreveu o ato |
| `E3` | `ADR-0007 §5.4` define `REWRITE` como *"a solucao do Legacy nao serve"* | [ADR-0007 §5.4](ADR-0007-fronteira-greenfield-legado.md) | **Alta — literal** | Sustenta que a afirmacao implicita e falsa |
| `E4` | As quatro classificacoes **nao constam de nenhum fundacional** | Varredura das tres arvores, 2026-07-31 | **Alta — medida** | **Sustenta a classe `C2` de §11**: nao ha hipotese *"a propria Fundacao"* |
| `E5` | `ADR-0022` declara `supera: [ADR-0021]` **sem** preencher `superado_por` em `ADR-0021` | Frontmatter dos dois | **Alta — medida** | Sustenta o metodo de superacao sem tocar o superado |
| `E6` | `ADR-0025` e precedente de `C2` **sem RFC** | [ADR-0025](ADR-0025-extensao-da-propagacao-de-qg-1-as-cartas-restantes.md) | Alta | **Citado e NAO usado** — §11.1 explica por que esta decisao tem `RFC` |
| **`A1`** | **Evidencia ausente, declarada (`VD-05`):** **nenhuma segunda admissao ocorreu.** A eficacia de `RECOGNIZE` e **prevista, nao observada** — ha **um** caso, e ele e retrospectivo | `PI-10` | — | Impede ler `RC-1` como validacao empirica da classe |

## 9. Riscos e mitigacao

| # | Risco | Prob. | Impacto | Mitigacao |
|---|---|---|---|---|
| `RA-1` | `RECOGNIZE` virar porta de entrada barata: admite-se identidade hoje e conteudo depois, sem portao novo | **Media** | **Alto** | `GA-01` — `G0` e declarado **por admissao**, e `FR-07` de `ADR-0007` continua valendo: **um candidato por vez, portao proprio a cada vez**. Admitir conteudo depois e **nova** passagem pelo portao, com `G0` novo |
| `RA-2` | `RC-1` ser lido como revalidacao do candidato medAlly | **Media** | **Alto** | `RC-4` e `RC-5`, em texto expresso. **`Q1` continua bloqueando** e esta decisao **nao a toca** |
| `RA-3` | A quinta classe tornar `G3` ambiguo para quem so leu `ADR-0007` | Media | Medio | `§5.3` declara **exatamente** o que foi superado; o catalogo `§7` registra o par |
| `RA-4` | **Esta decisao estar errada** — a distincao identidade/conteudo nao se sustentar no segundo caso | Baixa | Medio | Reversao `Tipo 2`, §10. Gatilho de revisao na **segunda** admissao, §12 |

## 10. Plano de reversao

| Campo | Conteudo |
|---|---|
| Reversivel? | **Sim — `Tipo 2`** |
| Como desfazer | `ADR` de retirada (`O9`) superando este. `G3` volta as quatro classificacoes; `G0` deixa de ser exigido; `RC-1` cai |
| **Custo da reversao — MEDIDO, objeto a objeto** | **1** `ADR` novo *(`O9`)* · **1** entrada de catalogo `§7` · **os indices `M3`** *(`decisions/README`, `rfcs/README`, `artifact-registry`, `governance/README`, `README` da raiz)* · **`0`** artefatos historicos · **`0`** fundacionais · **`0`** artefatos normativos migrados |
| O que **nao** se reverte | **Nada** — `0` admissoes foram feitas sob esta norma. Se houver admissao `RECOGNIZE` antes da reversao, ela passa a exigir tratamento do artefato admitido (`EV-06`), e a reversao deixa de ser trivial |
| Janela | **Permanente enquanto nao houver admissao sob `RECOGNIZE`.** Hoje: **`0`** |
| Quem executa | DEP-GOV, sob aprovacao de DEP-EXE |
| Backup (`PI-07`) | Cópia datada `_backups/LucaX-Enterprise-OS_2026-07-31_pre-missao-1-13-4-2/` |

## 11. Classificacao — **determinada, nao presumida por analogia**

| Campo | Valor |
|---|---|
| Classe de mudanca | **`C2` — Estrutural** |
| Tipo de reversibilidade | **`Tipo 2`** |
| Decisor | **DEP-EXE**, com parecer de DEP-GOV |
| Ratificador | **Nao aplicavel** — `C2`/`Tipo 2` (`FND-04 §2.2`, `FND-07 §2.3`) |
| Instrumento | **`RFC` → `ADR`** — [RFC-0022](../rfcs/RFC-0022-classe-de-admissao-de-existencia-no-portao-de-origem-externa.md) |
| Fitness Check | **Obrigatorio** (`CV-07`) — [FIT-2026-020](../governance/fitness/FIT-2026-020-emenda-do-portao-de-origem-externa.md) |

### 11.1 A determinacao, hipotese a hipotese

> **A classe nao foi herdada de `ADR-0007`.** Que `ADR-0007` seja `C2` **nao torna** `C2` a
> emenda dele: `AL-01` manda classificar pelo **efeito**, nao pelo objeto alterado. As cinco
> hipoteses de `C3` em `FND-04 §2` foram percorridas uma a uma.

| Hipotese de `C3` (`FND-04 §2`) | Incide? | Como se sabe |
|---|---|---|
| Altera **principio imutavel** | **Nao** | Nenhum `PI-01`–`PI-14` e tocado. `PI-10` e `LV-12` sao **invocados** por esta decisao, nao alterados |
| Altera **linha vermelha** | **Nao** | Nenhuma `LV` e criada, removida ou redefinida |
| Altera **hierarquia normativa** | **Nao** | `FND-01 §10` intacta. Origem **externa** continua **fora** da hierarquia — nenhum nivel interno se move. É o mesmo fundamento de `ADR-0007 §11`, **reverificado, nao copiado** |
| Altera **direitos de decisao** | **Nao** | `GA-02`: quem declara `G0` e o Proponente, quem confere e DEP-GOV, quem valida e DEP-QAR (`G4`), quem decide e o aprovador da classe (`G5`). **Os quatro sao os de hoje** |
| Altera **a propria Fundacao** | **Nao — MEDIDO** | As quatro classificacoes **nao ocorrem em nenhum `FND`** *(evidencia `E4`)*. **Nenhum fundacional precisa de emenda em cascata** (`CV-04`) |

**Hipotese de `C2` que incide, literal:** *"Cria, altera ou remove um componente ou muda
escopo, **fronteira**, interface ou **padrao**"*. Esta decisao muda o **padrao de classificacao**
de um portao de **fronteira**. **Duas palavras da hipotese, nomeadas.**

**`GV-03` — na duvida, a classe mais alta — foi considerado.** **Nao ha duvida a resolver:** as
cinco hipoteses de `C3` foram percorridas e **nenhuma incide**, cada uma com o teste que a
descarta. `GV-03` opera sobre duvida, e a duvida foi eliminada por medicao — nao por
preferencia.

**`Tipo 2`, determinado:** `FND-04 §2.2` opoe `Tipo 2` *(reversivel)* a `Tipo 1`
*(irreversivel/caro)*. O custo de reversao esta **medido objeto a objeto** em §10 e alcanca
**1 `ADR` + 1 entrada de catalogo + os indices**, com **`0`** artefatos migrados e **`0`**
consumidores — porque **`0`** admissoes existem sob esta norma. **Reversivel por medicao, nao
por analogia com `ADR-0007`.**

### 11.2 Por que esta decisao tem `RFC`, e `ADR-0025` nao teve

`FND-04 §2` permite dispensar a `RFC` em `C2` *"se a alternativa unica for obvia **e** DEP-GOV
concordar por escrito"*. **A alternativa nao e unica nem obvia:** `RFC-0022 §4` analisa **tres**
respostas reais ao mesmo defeito, e **duas delas** — redefinir `REWRITE`, criar `G0` sem
`RECOGNIZE` — sao respostas naturais que exigiram argumento para serem descartadas. **Onde ha
tres candidatas defensaveis, a dispensa nao esta disponivel**, e `ADR-0025` **nao e precedente
aplicavel**: la a alternativa era unica.

## 12. Revisao

| Campo | Conteudo |
|---|---|
| Gatilho por evento | **Segunda admissao pelo portao** — verificar se `G0` foi declarado sem esforco e se `RECOGNIZE` descreveu o ato |
| Gatilho por evento | **Primeira admissao com `G0 = AMBOS`** — verificar se duas classificacoes na mesma admissao sao operaveis |
| Gatilho temporal | 2027-01-31 |
| Sinal de que esta decisao deu errado | *(a)* `RECOGNIZE` ser escolhida em admissao que **avaliou** conteudo — sinal de que a classe virou atalho; *(b)* `G0` ser declarado sempre `IDENTIDADE` por conveniencia, sem que nenhuma admissao de conteudo ocorra |
| Dono | **DEP-QAR** |

## 13. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Origem | [RFC-0022](../rfcs/RFC-0022-classe-de-admissao-de-existencia-no-portao-de-origem-externa.md) |
| Evidencia de origem *(nao norma)* | `_missao-1-13-4-1-2026-07-31/minutas/MINUTA-A-classe-de-admissao-de-existencia-em-G3.md`, `sha256` `76eb131918c63e34228ceceb07b4bf8604a76c1fb418f2695e3c6dc7544552d5` |
| Achados que fecha | **`RD-54`** · **`RD-55`** — **na vigencia**, nao na redacao |
| Decisoes superadas | **[ADR-0007](ADR-0007-fronteira-greenfield-legado.md), parcialmente** — `§5.3` linha `G3` e `§5.4`, **quanto a lista de classificacoes** e **somente quanto a ela** |
| Decisoes relacionadas | [ADR-0010](ADR-0010-contrato-de-conhecimento-do-soberano.md) `CT-09` *(vocabulario em ingles — precedente estendido, nao alterado)*; [ADR-0026](ADR-0026-admissao-do-medally-como-primeiro-produto.md) *(alcancado por `RC-1`, **nao editado**)* |
| Questao do Soberano | **`Q2`** de [PS-2026-014 §7](../governance/pacote-soberano-2026-07-31-medally.md) |
| Verificacao de aptidao | [FIT-2026-020](../governance/fitness/FIT-2026-020-emenda-do-portao-de-origem-externa.md) |
| Pacote soberano | [PS-2026-015](../governance/pacote-soberano-2026-07-31-emendas-de-instrumento.md) |

---

## Checklist de validade (FND-07 §4.1)

- [x] `VD-01` — 3 alternativas reais + *"nao fazer nada"* (`RFC-0022 §4`)
- [x] `VD-02` — criterios declarados antes da escolha (§3 antes de §4)
- [x] `VD-03` — nenhuma alternativa de palha: `B` e `C` sao respostas naturais ao mesmo defeito
- [x] `VD-04` — tradeoff aceito explicito (§6, item 4)
- [x] `VD-05` — ausencia de segunda admissao declarada (§8, `A1`)
- [x] `VD-06` — reversao declarada e **medida objeto a objeto** (§10)
- [x] `VD-07` — impacto em cascata mapeado; **`0` fundacionais alcancados, medido** (§7)
- [x] `VD-08` — data e responsavel presentes
- [x] `VD-09` — gatilhos de revisao definidos (§12)

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-31 | DEP-GOV | Decisao inicial, **`em-revisao`, NAO vigente**. Acrescenta `G0` *(objeto da admissao)* e `RECOGNIZE` *(quinta classificacao de `G3`)*, superando **`ADR-0007 §5.3` linha `G3` e `§5.4`** quanto a lista — e **somente quanto a ela**, com **`0` bytes** em `ADR-0007`. Regras `GA-01` a `GA-04` e `RC-1` a `RC-5`. Classe **`C2`/`Tipo 2`** determinada percorrendo **as cinco hipoteses de `C3`** uma a uma, com a hipotese *"a propria Fundacao"* **descartada por medicao**. Corrige a fonte: a quarta classe e **`RETIRE`**, nao `REJECT`. |
