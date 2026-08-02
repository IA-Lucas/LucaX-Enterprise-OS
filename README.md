---
id: IDX-raiz
titulo: LucaX Enterprise OS — Indice Mestre
tipo: relatorio
versao: 1.22.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-08-01
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0001, ADR-0002, ADR-0003, ADR-0004, ADR-0005, ADR-0006, ADR-0009, ADR-0010, ADR-0011, ADR-0012, ADR-0013, ADR-0021]
substitui: []
substituido_por: null
resumo: Serve de porta de entrada do sistema: o que existe, o que nao existe por decisao e por onde comecar a ler.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# LucaX Enterprise OS

> Empresa digital operada por agentes de IA, sob soberania de um unico humano.

## Proposito
Servir de porta de entrada do sistema: onde comecar a ler, o que existe hoje, e o que ainda
nao existe por decisao deliberada.

## Escopo
Todo o repositorio. Este documento **indexa**; nao normatiza. A norma esta em
[`foundation/`](foundation/).

## Responsaveis
| Papel | Responsavel |
|---|---|
| Soberano | Lucas (humano) — autoridade final e indelegavel |
| Guardiao normativo | DEP-GOV |
| Proprietario deste indice | DEP-GOV |

---

## Estado atual

**Fases concluidas:** Fundacao Organizacional, Enterprise Capability Framework, Enterprise
Meta Model, Enterprise Artifact Framework, Consolidacao da Base, Conhecimento sobre o Soberano,
Contrato de Carta de Departamento com dois pilotos, ativacao dos pilotos com validacao
interclasses nas quatro classes, a **Primeira Revisao Estrutural**, e o **rollout das cinco
Cartas restantes — cobertura documental 9/9**, e a **aplicacao integral do sexto ato
soberano**, que poe em vigor **dez objetos** e emenda **quatro documentos fundacionais**.
**Decisoes:** [ADR-0001](decisions/ADR-0001-adocao-da-fundacao-organizacional.md) a
[**ADR-0023**](decisions/ADR-0023-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md) **escritas** —
`ADR-0016` a `ADR-0019` ratificadas pelo **sexto ato soberano** de 2026-07-29
([MSG-2026-0006](memory/operacional/MSG-2026-0006-ato-soberano-aplicacao-integral.md)) e
**`ADR-0020` e `ADR-0021` em vigor como `C2 · Tipo 2`, que nao exige ratificacao**.
**`ADR-0022` a `ADR-0025` ESTAO EM VIGOR**, ratificadas ou aprovadas pelo **setimo ato soberano**
de 2026-07-30
([MSG-2026-0007](memory/operacional/MSG-2026-0007-ato-soberano-vigencia-do-framework-de-specifications.md)).
**A fila de artefatos retidos foi a zero.** A **Missao 1.13.3** consumiu o ato e poe em vigor os
**catorze** objetos de [PS-2026-013](governance/pacote-soberano-2026-07-30-consolidado.md):
os quatro `ADR`, **`FND-11` 1.0.0** *(criacao — `foundation/` passa a ter **onze** documentos)*,
`FND-01` **1.7.0 cumulativa**, `FND-02` **1.4.0**, `FND-03` **1.6.0**, `FND-10` **1.5.0** e as
**cinco** Cartas **1.1.0**. **`RD-27`, `RD-31` e `RD-37` FECHADOS.**
**A prova:** `H-P` reproduzido em **14 de 14**, `H-N` **invariante** nas **10** transicoes `O4`,
`IR-09` reconstruindo `H-A` nos **10**, identidade binaria nos **4** sem `O4`, e **`0` bytes fora
dos diffs autorizados**. Decisao **`SPEC-FRAMEWORK-IN-FORCE`**
([PT-2026-010](governance/relatorio-transicao-2026-07-30-vigencia.md) ·
[FIT-2026-018](governance/fitness/FIT-2026-018-vigencia-do-framework-de-specifications.md)).
**Baseline vigente:** `BL-2026-08-02-02` — [catalogo mestre §10.0](governance/artifact-registry.md),
com a evidencia de integridade em **§10.22**.
As anteriores, de `BL-2026-07-28-01` a `BL-2026-08-02-01`, estao **preservadas e nao editadas** (`BL-02`).

**A Missao 1.13.4 exerceu, pela primeira vez, o portao de origem externa de
[ADR-0007 §5.3](decisions/ADR-0007-fronteira-greenfield-legado.md)**, sobre **um** candidato
nomeado — o **medAlly**. `G1`–`G4` **comprovados**, `G5` **preparado**, **`G3` = `REWRITE`**,
**`0` bytes admitidos** e **`0` bytes escritos** no repositorio de origem. **Dois** objetos
foram submetidos em [PS-2026-014](governance/pacote-soberano-2026-07-31-medally.md) —
[`ADR-0026`](decisions/ADR-0026-admissao-do-medally-como-primeiro-produto.md) e a **Carta
candidata `PRO-medally`**, esta ultima **fora do acervo**. **NENHUM Produto entrou em vigor por
aquela missao**, e o medAlly **segue nao admitido ate hoje**: `ADR-0026` esta **`em-revisao`**,
aguardando ato
([PT-2026-011](governance/relatorio-transicao-2026-07-31-admissao-medally.md) ·
[FIT-2026-019](governance/fitness/FIT-2026-019-admissao-do-medally.md)).

**A Missao 1.13.4.1 consertou os instrumentos que o primeiro exercicio real do portao
revelou defeituosos, e nao julgou nada.** O **comando de reproducao da baseline foi corrigido** —
lista fechada positiva, portao de raiz e portao de split — e **`BL-2026-07-30-01` voltou a
reproduzir nos 64 digitos** sobre a copia datada em que o comando publicado dava **198**: **o
defeito era do instrumento, nunca da baseline**, e nenhuma verificacao a jusante era nominal
(`RD-53`, ✅ **FECHADO**). Fecharam tambem **`RD-56`** *(`TPL-carta-produto` **1.1.0**, com
`capabilities`, os cinco campos de `FND-10 §2.2`, Capabilities consumidas e interfaces)*,
**`RD-57`** e **`RD-58`**. **`RD-49`** foi corrigido em **tres Cartas candidatas medidas e NAO
aplicadas** — emendar Carta ratificada exige ato novo. Os **19** caminhos que mudaram no
repositorio externo durante a janela da 1.13.4 foram **atribuidos a processo e horario, 19 de
19**, com **`0`** escritores concorrentes no acervo. **Tres minutas** — classe de admissao de
existencia em `G3`, independencia de fornecedor, superacao de ato por evidencia posterior —
estao **preparadas e nao aplicadas**, fora do acervo. **Nenhum ato foi emitido, nada foi
ratificado e o pacote da 1.13.4 nao foi alterado — `0` bytes.** **Decisao `BLOCKED`:** o Item 0 reprova — dos **19** caminhos que mudaram no repositorio externo na janela da 1.13.4, **14** estao atribuidos a processo nomeado e **5 sao NAO ATRIBUIVEL**, porque **nenhuma das mudancas foi commitada**. **Nao ha escritor concorrente no acervo**, e **nenhum instrumento das tres minutas esta consertado ate ato do Fundador**
([PT-2026-012](governance/relatorio-transicao-2026-07-31-manutencao-instrumentos.md)).

**A Missao 1.13.4.2 submeteu as tres emendas de instrumento e corrigiu `CA-2` antes da assinatura**, e a
**Missao 1.13.4.3 APLICOU o oitavo ato soberano**
([MSG-2026-0008](memory/operacional/MSG-2026-0008-ato-soberano-emendas-e1-e-e3.md)): **`ADR-0027` esta
`ativo`** *(aprovado por **DEP-EXE** no rito `C2`; `ratificacao` **nao-exigida** e nao criada)* e
**`ADR-0029` esta `ativo` e `ratificada`**, com **`H-P` 2 de 2**, **`H-N` invariante 2 de 2**, **`IR-09`
2 de 2** e **`atualizado_em` nao tocado**. Nasce o **registro de atos superados** de `SA-6`
([atos-superados](governance/atos-superados.md)), **com o contador em `0`**. **`E2` — a independencia de
verificacao por fornecedor — fica ADIADA e nao rejeitada**, com `RFC-0023`, `ADR-0028` e `FIT-2026-021`
**intactos**. **`0` Produtos**, **`0` `Spec`s** e `products/` **continua inexistente**.

**A Missao 1.13.4.4 exerceu o portao de origem externa pela SEGUNDA vez — e a segunda foi a
primeira sob a norma emendada.** O candidato e o **nXtrack**, por decisao do Fundador:
**`Q1` esta RESPONDIDA**, e o fundamento e que **`PT-2026-009` e `PS-2026-013` sao artefatos
distintos** — a decisao **7** de `PT-2026-009 §1` nomeia o nXtrack **sem ressalva**, e a
palavra `comercial` tem **`0`** ocorrencias naquele arquivo *(`RD-64`)*. **`G0` = `IDENTIDADE`**,
declarado **antes** de `G1` como `GA-01` exige, e **`G3` = `RECOGNIZE`** — **primeira aplicacao
prospectiva** da classe que `ADR-0027` criou. **`G1` FECHA por medicao, e o Item 0 nao foi
presumido:** o nXtrack **nao tem repositorio proprio** *(e subarvore de `lucaX`, achado
`RD-71`)*, tem **`0`** caminhos sem commit em **183** rastreados contra **758** no hospedeiro,
e **17 de 17** fontes consumidas tem autoria e data, congeladas no objeto `tree`
`b9b36be9…fb4b` — **ancora que sobrevive ao repositorio vivo porque e objeto de commit, nao
hash de copia**. **`0` bytes do candidato entraram**, medido por **`0` colisoes** de hash.
Quatro objetos foram submetidos em [PS-2026-016](governance/pacote-soberano-2026-08-01-nxtrack.md),
mais a **Carta candidata `PRO-nxtrack`**, **fora do acervo** por `FR-10`. **Aquela missao NAO
admitiu Produto algum**: nao emitiu ato, deixou `ADR-0030` em **`em-revisao`** e `S1`
**preparada e nao consumida** — o ato veio depois, e a aplicacao depois dele
([PT-2026-014](governance/relatorio-transicao-2026-08-01-portao-nxtrack.md) ·
[FIT-2026-023](governance/fitness/FIT-2026-023-admissao-do-nxtrack.md)).

**O NONO ATO SOBERANO foi EMITIDO e NAO consumido**
([MSG-2026-0009](memory/operacional/MSG-2026-0009-ato-soberano-admissao-do-nxtrack.md)), sobre os
**itens I a VII** da minuta de
[PS-2026-016 §6](governance/pacote-soberano-2026-08-01-nxtrack.md) **1.2.0**, linhas **185–328**,
**ancorado no `H-A` do pacote `e6fa26e8…44ae` — medido no arquivo, nunca lido da transcricao**.
O ato **RATIFICA `ADR-0030`**, **APROVA `RFC-0025`** e **CRIA o Produto `PRO-nxtrack`**, com
**`G0` = `IDENTIDADE`** e **`G3` = `RECOGNIZE`**. **`CA-1` a `CA-6` fecham em 6 de 6**, porque
**`Q2` foi respondida e, pela primeira vez, GRAVADA COMO ARTEFATO**: a ressalva de
`PS-2026-013 §7` **nao condiciona** o ato. A prova acompanha o registro — **`H-A` 5 de 5**,
**`H-P` 2 de 2** *(o de `RFC-0025` pela variante declarada, porque o ciclo de `RFC` termina em
`aprovado`)* e **`H-N` invariante 2 de 2**. **Emitir e aplicar sao atos distintos**, e o Fundador
os separou expressamente pela **segunda** vez no acervo. O ato declara ainda que
**`RECOGNIZE` nao afirma merito tecnico**, que
as **quatro** ressalvas de `FIT-2026-023` seguem **abertas**, e que **`LM-6(a)`** — **`0`**
ocorrencias de `LGPD`, `GDPR`, `ANPD`, *"dados pessoais"*, *"politica de privacidade"* e *"termos
de uso"*, num produto com nome, `senha_hash` e sal por conta — e **materia da primeira `Spec`,
com prioridade** sobre as demais de `LA-7`.

**A Missao 1.13.4.5 CONSUMIU o nono ato, e o acervo tem o seu PRIMEIRO PRODUTO.** Missao
**ministerial** — executa o ato, nao o interpreta —, na ordem de
[PS-2026-016 §6.2](governance/pacote-soberano-2026-08-01-nxtrack.md):
[**`ADR-0030`**](decisions/ADR-0030-admissao-do-nxtrack-como-primeiro-produto.md) esta **`ativo` ·
`ratificada`**, [**`RFC-0025`**](rfcs/RFC-0025-admissao-do-nxtrack-como-primeiro-produto.md) esta
**`aprovado`** *(pela **variante**, jamais pelo instrumento padrao, que poria `ativo`)*, e
[**`PRO-nxtrack`**](products/nxtrack/carta.md) existe em `products/nxtrack/carta.md`, com **`H-A`
do arquivo aplicado `fca656a9…39e2`** — **distinto do `H-A` do candidato**, que **nao e artefato**
e permanece intacto. **`products/` nasce como raiz do acervo**, e com ela estreiam a entidade
**`PRO`** e o tipo **`Carta de Produto`**. **A prova:** `H-P` **2 de 2**, `H-N` invariante **2 de
2**, `IR-09` **3 de 3**, `atualizado_em` **nao tocado**, **`0` bytes fora do conjunto autorizado**
— provado **arquivo a arquivo** contra a copia datada — e o candidato **intacto**, `tree`
`b9b36be9…fb4b` identico antes e depois. **Baseline nova: `BL-2026-08-01-02`**, reproduzida em
**duas** execucoes, com o medidor declarando **`products`** e **`CLAUDE.md`** *(achado `RD-81`,
✅ **FECHADO pelo proprio dono**, o Soberano)*. **`RD-33` foi FECHADO na sequencia, pela Missao
1.13.4.6** — a **missao propria** que o item **VII** e `LA-3` reservaram —, por rito
**ministerial** e com **`0` atos emitidos**. **`0` `Spec`s, `0` atos emitidos, `Q3` e `Q4`
seguem sem resposta.** Quatro achados novos, **`RD-83`** a **`RD-86`**, e mais **`RD-87`** — todos
**abertos, com dono e gatilho, sem missao**
([PT-2026-015](governance/relatorio-transicao-2026-08-01-aplicacao-nxtrack.md)).

> ### ✅ `GO-TO-SPECS` LIBERADO — **8 de 8** condicoes de §X do sexto ato soberano
> **O bloqueio deixou de existir sem que nenhuma fonte fosse emendada e sem novo ato.** O unico
> achado que impedia a condicao 6 — **`RD-22`**, *"promulgacao e ativacao sem titular declarado"*
> — **era falso**: os titulares estavam declarados em **`FND-04 §4 [7]`** e **`FND-07 §5 [10]`**,
> e a varredura mediu o **termo** *"promulg"* em vez da **funcao** *"quem publica o que foi
> aprovado"*. Formalizado por
> [**ADR-0020**](decisions/ADR-0020-regime-ministerial-de-promulgacao-e-ativacao.md) — **`C2 ·
> Tipo 2`, o menor instrumento competente**, com **0 fontes emendadas, 0 titulares criados e 0
> atos exigidos**.
>
> **`RD-26` reconciliado:** a distribuicao de perfil de contexto passa a **reproduzir o total do
> acervo**, pelo metodo que `FND-10 §2.3` sempre prescreveu — cobertura **100%**, **0 nao
> classificados**, **0 preenchimentos por inferencia**.
>
> ✅ **A pre-correcao obrigatoria FECHOU, e era maior do que estava declarada.** **`RD-23`**
> apontava **dois** defeitos em [`TPL-spec`](foundation/templates/TPL-spec.md); a medicao campo a
> campo encontrou **cinco**, e os cinco estao corrigidos em **1.1.0**, com diff literal e
> reversivel — [ADR-0021 §5.11](decisions/ADR-0021-framework-de-specifications.md).
> **O aprovador passou a ser derivado da classe**, e **nao mais fixado no esqueleto**.

> ### ✅ Framework de Specifications INSTITUIDO — **`SF-01` a `SF-32`**
> **A norma da `Spec` ganhou sede sem custo normativo.**
> [**ADR-0021**](decisions/ADR-0021-framework-de-specifications.md) — **`C2 · Tipo 2`** — institui
> o contrato de **21 blocos**, a semantica normativa *(`MUST`/`SHOULD`/`MAY`, **6** campos por
> requisito, **6** naturezas de enunciado, **5** metodos de verificacao, **10** adjetivos vedados
> por nome)*, **7 perfis** que **nao viram tipo**, a matriz de **50 celulas** `C0`–`C3` ×
> `Tipo 1/2`, a cadeia de **9 elos**, **`DoR` de 9** e **`DoD` de 10**, o regime de mudanca e a
> economia de contexto — com **`0` arquivos de `foundation/` alterados**, medido por `cmp`, e
> **`0` entidades, tipos documentais, portoes, papeis ou verbos de autoridade criados**.
> **Testado em 12 casos: 11 coerentes e 1 divergente, que virou achado em vez de ser contornado.**
> Verificacao independente: [FIT-2026-015](governance/fitness/FIT-2026-015-framework-de-specifications.md),
> `apto-com-ressalva`, **3 ressalvas**, **`C11` 13 de 13**.

> ### ✅ `RD-33` — FECHADO em 2026-08-01, e era a unica pendencia bloqueante do acervo
> **O acervo fica SEM PENDENCIA BLOQUEANTE pela primeira vez desde 2026-07-29.** Tres fontes
> vigentes vinculam a `Spec` a `Produto` — **`FND-04 §6`** *(pre-condicao **"Produto existe"**, e
> *"todas precisam ser verdadeiras"*)*, **`FND-03 §3.6`** e **`FND-10 §4.4`** —, e **as tres
> continuam intactas: `0` bytes.** O vinculo **nao foi removido nem afrouxado — foi SATISFEITO**,
> porque ha **`1` Produto em vigor**, [`PRO-nxtrack`](products/nxtrack/carta.md).
>
> **Quem fechou, e com que rito.** A **Missao 1.13.4.6**, por rito **MINISTERIAL**, com **`0`
> atos emitidos** e **`0` fontes emendadas** — [PT-2026-016](governance/relatorio-transicao-2026-08-01-fechamento-rd-33.md).
> A autoridade **ja fora exercida** em `S1`, o nono ato; o que faltava era **registro**, e
> registrar e etapa `[7]` de `FND-04 §4`, de **DEP-GOV** — `PA-01`, `PA-03`, `PA-07` e **`PA-13`**
> *(*"o SOBERANO nao e executor ministerial"*)* de `ADR-0020`. **A reserva do item VII e de `LA-3`
> era TEMPORAL *(«apos a vigencia»)* e DE SEDE *(«missao propria»)*, nunca de classe de rito.**
>
> **A prova e por EXERCICIO, o mesmo metodo que abriu o achado:** o `DoR` de `SF-23` foi
> reexercido, e o item **(9)** — *"Produto existe"* — **PASSA**. **`GO-TO-SPECS` deixa de estar
> *liberado e nao exercivel* e passa a EXERCIVEL.**
>
> **O que NAO fechou junto, e continua aberto:** a `Spec` sobre materia **nao-produto** nao existe
> como categoria, so **`S2`** a cria, e `S2` esta **deferida** por decisao soberana — achado
> **`RD-88`**, ABERTO, com dono e gatilho. **As duas Specs piloto pedidas pela Missao 1.13
> seguem `PILOTO-DEFERIDO`**, e as duas saidas faceis — escrever em outro diretorio *(artefato
> nulo por `MT-01`)* ou criar `products/` *(`LV-06`, `LV-07`)* — **continuam recusadas com norma
> citada**.
>
> **Duas saidas legitimas, disjuntas, ambas do Soberano:** **`S1`** — ato que crie o primeiro
> Produto, habilitando a Spec **de produto**; **`S2`** — `RFC C3 → ADR C3 → ato` ampliando a
> `Spec` a materia nao-produto, habilitando a **interdepartamental**. **Cada piloto pedido depende
> de uma saida diferente**, e a escolha nao pode ser suprida por Departamento algum.
>
> **Sete pendencias para o Soberano, e uma bloqueia:** **`S1` ou `S2`** *(bloqueia)* ·
> **[PS-2026-009](governance/pacote-soberano-2026-07-29-fnd-11.md)** *(`FND-11`, `FND-01` 1.6.0,
> `FND-03` 1.6.0)* · **[PS-2026-010](governance/pacote-soberano-2026-07-29-rd-31.md)** *(as duas
> Cartas — **`RD-31`**, agora com candidato medido)* · a **variante de `FND-01`** *(`V1` estrita
> ou `V2`, que fecha **`RD-27`** quanto a `FND-01`)* · a **extensao a `RD-37`** *(3 Cartas nao
> corrigidas)* · o **tipo** de `ADR-0022` · e **gravar ou nao `superado_por` em `ADR-0021`**,
> que **altera o `H-N`** de um artefato `M1` — **`RD-43`**.
> **A classe de `ADR-0020` e a de `ADR-0021` permanecem pendencias anteriores, nao reabertas.**
> [PT-2026-007](governance/relatorio-transicao-2026-07-29-specifications.md) ·
> [FIT-2026-015](governance/fitness/FIT-2026-015-framework-de-specifications.md) ·
> [PT-2026-006](governance/relatorio-transicao-2026-07-29-fechamento-operacional.md) ·
> [FIT-2026-014](governance/fitness/FIT-2026-014-regime-ministerial-e-cobertura-de-contexto.md).

> ### 📋 Historico dos atos soberanos — **a fila de artefatos retidos esta em `0`**
> ⚠️ **Este bloco descreve o estado da Missao 1.9 e foi mantido como registro, nao como estado
> corrente — item de `RD-35`.** O titulo declarava *"seis artefatos aguardam decisao do
> Soberano"*, e a fila **zerou** com o sexto ato soberano: o [catalogo mestre §2](governance/artifact-registry.md)
> — **fonte** — declara **`0` artefatos retidos por falta de ato**, e as **nove Cartas** e os
> **quatro `ADR`** entao pendentes estao **em vigor**. **O estado corrente do sistema e o dos tres
> blocos acima.** O que segue permanece porque **registra como cada ato foi recebido e verificado**,
> e isso nao envelhece.
>
> **Tres atos soberanos**, todos de 2026-07-28, cada um com **fonte canonica propria e nao
> acumulada**: [MSG-2026-0001](memory/operacional/MSG-2026-0001-ato-soberano-ratificacao-cartas-piloto.md)
> sobre `DEP-QAR` e `DEP-ENG`; [MSG-2026-0002](memory/operacional/MSG-2026-0002-ato-soberano-cartas-comando-plataforma-e-contexto.md)
> sobre `DEP-EXE`, `DEP-KMS` e `MEM-EST-0001`; e
> [**MSG-2026-0003**](memory/operacional/MSG-2026-0003-ato-soberano-emenda-qar-e-criterio-de-consolidacao.md)
> sobre a **emenda `DEP-QAR` 1.1.0** e o **criterio de consolidacao**.
>
> **`DEP-QAR` esta em 1.1.0, e o defeito IC-5 foi corrigido** — a primeira emenda ratificada do
> sistema. **`DEP-QAR` 1.0.0 esta preservada** por hash, diff reversivel e copia datada.
>
> **O que aguarda decisao:** as **cinco Cartas novas** e a **emenda constitucional candidata**,
> reunidas em [**PS-2026-002**](governance/pacote-soberano-2026-07-28-cartas.md). **Nenhuma
> delas retem correcao urgente**; retem **vigencia**.
>
> **Nenhuma ratificacao foi produzida por esta missao:** o ato foi **recebido**, e sua condicao
> de eficacia verificada por **dez verificacoes em cinco vias independentes**, incluindo o
> **diff literal** que o proprio ato exigiu e a **reconstrucao `IR-09`**.

> ### ⚠️ O que fechou, e o que **nao** fechou
> O rollout fechou **8 ressalvas e achados** com evidencia — entre eles **IC-4**, **IC-5**,
> **DR-4**, **RE-01** e **RE-06**. **Tres** coisas **nao** fecharam, e estao escritas como tais:
>
> **(1)** A colisao do termo *"ratifica"* em **FND-01 §7.3** permanece **aberta** — e agora
> **medida**: sao **cinco** linhas, nao quatro, e **FND-09 §8.2 nunca usou o sentido ambiguo**.
> O texto da emenda existe em [RFC-0011](rfcs/RFC-0011-emenda-constitucional-ratifica-homologa.md);
> **falta so o ato**. A contencao `IR-11` segue com **0 violacoes em 1.210 ocorrencias medidas**.
> **(2)** A ambiguidade **FND-10 §2.2 × §10.3** sobre `FIT` continua **escalada** — decidi-la por
> rito C2 retiraria materia da mesa do ratificador.
> **(3)** **Tres achados novos estao presos em Cartas ja ratificadas** — `DEP-QAR` declara 386
> linhas e tem 387; `DEP-KMS` nao trata incidente; `DEP-ENG` nao declara impedimento sobre a
> propria Carta. **Corrigir qualquer um exige ato novo**, e os tres tem efeito nulo ou local.
>
> **A pendencia escalada na missao anterior foi respondida.** O Soberano fixou o **criterio de
> consolidacao**, formalizado em [ADR-0013](decisions/ADR-0013-criterio-de-horizonte-e-consolidacao.md)
> **sem emendar nenhum documento fundacional**.

> ### O que a organizacao sabe sobre quem a dirige
> O **Contexto do Soberano** registra visao, criterios, linguagem e forma de trabalho — com
> **fonte, data, classe de evidencia e confianca por afirmacao**, e com **11 lacunas nomeadas**
> onde nao ha prova. Ele **orienta, nunca obriga**: memoria nao tem autoridade normativa
> (FND-09 §5.7), e cede diante da Constituicao, da Governanca e de ADR vigente. Carrega-se
> **por pacote**, nunca inteiro — o piso custa **28 linhas** (CT-22).

> ### As nove Cartas de Departamento, e as quatro classes
> O **Contrato de Carta de Departamento** ([ADR-0011](decisions/ADR-0011-contrato-de-carta-de-departamento.md))
> fixa **doze blocos obrigatorios** e **dez regras de desenho**. Foi validado em **seis cenarios**
> sobre **DEP-QAR** (Guarda) e **DEP-ENG** (Linha), e depois em **oito cenarios interclasses**
> com **DEP-EXE** (Comando) e **DEP-KMS** (Plataforma) — **as quatro classes exercidas**. A Carta
> declara o que o departamento **custodia** e o que **exerce**, de onde vem cada autoridade, e
> **em que materia ele esta impedido de aprovar ou verificar**. Nenhum departamento novo foi
> criado: os nove existem desde ADR-0001.
>
> **As nove existem, e a leitura conjunta delas encontrou o que nenhuma revisao individual
> encontraria:** quatro achados so aparecem quando **as nove** sao comparadas — inclusive **dois
> em Cartas em vigor desde a Missao 1.7**. A projecao comparativa unica vive em
> [`departments/README §2`](departments/README.md), e responde *"o que distingue um departamento
> do outro"* em **16 linhas**, no lugar de **3.918**.
>
> **Cobertura documental 9/9; cobertura vigente 4/9.** Carta que nao vigora nao pode ser
> consumida (LM-02) — e a distincao esta escrita para que 9/9 nao seja lido como camada pronta.
>
> ### Fronteira greenfield / legado
> Este repositorio e o **LucaX Enterprise OS**: greenfield, arquitetura-alvo e **unica fonte
> normativa**. O **LucaX Legacy** e sistema **externo**, sem autoridade — pode vir a ser fonte
> de evidencia e de candidatos, nunca de norma. O **Programa de Migracao** existe apenas como
> nome: **nao iniciado**. Importacao direta e **proibida**; entrada futura passa pelo portao de
> cinco condicoes de [ADR-0007 §5.3](decisions/ADR-0007-fronteira-greenfield-legado.md).
> Nesta data, **213 de 213 artefatos sao `native`**, e ha **`2` `legacy-candidate`
> nomeados e `0` admitidos**. **O portao foi EXERCIDO pela SEGUNDA vez em 2026-08-01**, sobre o
> **nXtrack**, com **`G0` = `IDENTIDADE`** e **`G3` = `RECOGNIZE`** — **primeira aplicacao
> prospectiva da classe**. **`0` bytes admitidos**, medido por **`0` colisoes** de hash entre
> os 179 hashes distintos do candidato e o acervo inteiro. **Nenhum Produto foi admitido:**
> `ADR-0030` esta `em-revisao` e nenhum ato foi emitido —
> [PT-2026-014](governance/relatorio-transicao-2026-08-01-portao-nxtrack.md).
> **O portao foi EXERCIDO pela primeira vez em
> 2026-07-31**, sobre **um** candidato nomeado — o **medAlly** —, e o resultado foi **`REWRITE`**:
> **`0` bytes entraram**. **Desde 2026-07-31 esse registro le-se `G3` = `RECOGNIZE`, com
> `G0` = `IDENTIDADE`** — regra `RC-1` de
> [ADR-0027](decisions/ADR-0027-classe-de-admissao-de-existencia-no-portao-de-origem-externa.md),
> **em vigor pelo oitavo ato soberano**. **O efeito nao muda** (`RC-3`): seguem **`0` bytes
> admitidos**, e os **cinco** artefatos da 1.13.4 **nao foram editados** (`RC-2`). O conteudo do repositorio permanece **`legacy-candidate` e nao
> admitido**, e cada peca dele que um dia queira entrar tera **portao proprio** (`FR-07`).
> **`FR-08` cumprido de propria mao:** um portao cujo unico desfecho previsto fosse a entrada
> nao seria portao. Antes disso, a Missao 1.13 **leu** evidencia externa da `A4` — **236 de
> 33.676 linhas, `0,70%`** — e **nao admitiu nenhuma**. `FR-04` distingue **consultar** de
> **importar**.

| O que existe | O que **ainda nao** existe — por decisao |
|---|---|
| **11** documentos fundacionais | Agentes e subagentes |
| **23 Capabilities em 7 dominios** | Workflows e automacoes |
| **21 entidades em 7 estratos — universo fechado; 10 instanciadas** | Produtos e projetos |
| **33 tipos documentais, 17 instanciados; 169 artefatos classificados** | Codigo, infraestrutura, banco de dados |
| 19 templates, 1 deles universal | Skills e ferramentas adotadas |
| **9 departamentos, 9 com Carta e 9 em vigor**; as 4 classes exercidas | Skills, Commands e Workflows |
| 5 camadas de memoria com dono, **13 registros** | Ontologia formal *(sem gatilho observado)* |
| 7 portoes de qualidade | Inventario do LucaX Legacy *(proibido antes de decisao)* |
| **21 decisoes e 17 propostas registradas** | Programa de Migracao |
| **15** verificacoes de aptidao, **9** revisoes arquiteturais, **1 revisao estrutural** | Clone, persona ou perfil do Soberano *(proibido, CT-15)* |
| **O Framework de Specifications — `SF-01` a `SF-32`, agora EXERCIDO** | **`Spec` de materia nao-produto** — continua **nao sendo criavel**, e so `S2` a habilita *(`RD-88`, aberto)*. A de **produto** existe desde 2026-08-02 |
| **`SPC-001` — a PRIMEIRA `Spec` do acervo**, sobre `LM-6(a)` do nXtrack: **10** requisitos, `DoR` **9/9**, `DoD` **10/10** | **Parecer juridico** — a `Spec` diz o que precisa existir e **nao substitui advogado** *(`EX-3`)*; e **autorizacao para expor dado vivo**, que segue **integralmente do SOBERANO** *(`EX-1`, `FND-01 §7.3`)* |
| **1 registro do Contexto do Soberano em vigor**, com 11 lacunas nomeadas e intactas | Documento fundacional sobre o Soberano *(sem sinal — gatilho em CT-27)* |

> Nada da coluna direita pode ser criado sem passar pelo rito de
> [governanca](foundation/04-governanca.md), **sem vinculo a ao menos uma Capability**,
> **sem que seu tipo conste do Meta Model** e **sem cumprir o contrato de artefato**. Essa
> restricao e o resultado da fase, nao uma pendencia dela.

## Por onde comecar

| Se voce quer... | Leia |
|---|---|
| Entender o que nunca pode ser violado | [FND-01 Constituicao](foundation/01-constituicao.md) |
| Saber quem responde por que | [FND-02 Estrutura](foundation/02-estrutura-organizacional.md) |
| Nomear ou localizar qualquer coisa | [FND-03 Taxonomia](foundation/03-taxonomia.md) |
| Criar ou mudar um componente | [FND-04 Governanca](foundation/04-governanca.md) |
| Trocar informacao entre areas | [FND-05 Comunicacao](foundation/05-framework-comunicacao.md) |
| Gravar ou recuperar conhecimento | [FND-06 Memoria](foundation/06-arquitetura-memoria.md) |
| Decidir e registrar | [FND-07 Decisoes](foundation/07-framework-decisoes.md) |
| Saber o que a organizacao sabe fazer | [FND-08 Capabilities](foundation/08-capability-framework.md) |
| Saber o que pode existir e como se liga | [FND-09 Meta Model](foundation/09-meta-model.md) |
| Saber o que todo artefato deve carregar | [FND-10 Artifact Framework](foundation/10-artifact-framework.md) |
| Saber o que toda Carta de Departamento deve declarar | [ADR-0011 Contrato de Carta](decisions/ADR-0011-contrato-de-carta-de-departamento.md) |
| Saber o que cada departamento custodia e exerce | [Matriz Departamento × Capability](capabilities/README.md) §10 |
| Comparar os nove departamentos em uma leitura | [Indice e projecao das Cartas](departments/README.md) §2 |
| Saber quando um horizonte pode ser avaliado | [ADR-0013](decisions/ADR-0013-criterio-de-horizonte-e-consolidacao.md) §5.1 |
| Ver o que depende de decisao do Soberano | [Pacote soberano PS-2026-002](governance/pacote-soberano-2026-07-28-cartas.md) |
| Achar qualquer artefato pelo resumo | [Catalogo mestre](governance/artifact-registry.md) |
| Saber o que pode entrar de fora, e como | [ADR-0007 Fronteira](decisions/ADR-0007-fronteira-greenfield-legado.md) |
| Saber quando um artefato antigo passa a dever o contrato | [ADR-0009](decisions/ADR-0009-o-que-conta-como-emenda-de-artefato.md) |
| Saber como se registra conhecimento sobre o Soberano | [ADR-0010 Contrato](decisions/ADR-0010-contrato-de-conhecimento-do-soberano.md) |
| Saber o que o Soberano ja declarou — e o que nao se sabe | [Contexto do Soberano](memory/estrategica/MEM-EST-0001-contexto-do-soberano.md) |
| Saber quanto contexto uma missao custa | [Catalogo mestre §11](governance/artifact-registry.md) |
| Ver o catalogo de competencias | [Enterprise Capability Model](capabilities/README.md) |
| Verificar se a arquitetura segue sadia | [Registro de aptidao](governance/fitness/README.md) |
| Uma visao geral rapida | [Indice da Fundacao](foundation/README.md) |

## Mapa do repositorio

| Diretorio | Conteudo | Estado |
|---|---|---|
| [`foundation/`](foundation/) | Os **11** documentos normativos + 19 templates + **7** revisoes arquiteturais + **1 revisao estrutural** | **Completo** — **quatro fundacionais emendadas e uma criada** pelo ato de 2026-07-30: `FND-01` **1.7.0**, `FND-02` **1.4.0**, `FND-03` **1.6.0**, `FND-10` **1.5.0** e **`FND-11` 1.0.0** |
| [`capabilities/`](capabilities/) | 23 Capabilities + catalogo + **matriz Departamento × Capability** + revisao | **Completo** |
| [`decisions/`](decisions/) | ADRs — decisoes tomadas | **30** registros — **27 `ativo`** *(`+1`: `ADR-0030`, aplicado)*, **1 `aprovado`** *(`ADR-0006`)* e **2 `em-revisao`**, ambos **retidos por falta de ato** *(`ADR-0026`, `ADR-0028`)*. **A fila de retidos por falta de APLICACAO zerou** |
| [`rfcs/`](rfcs/) | RFCs — propostas em analise | **25** registros — **25 `aprovado`**, **`0` em outro estado**. `RFC-0025` foi aplicada pela **variante**: o ciclo de `RFC` termina em `aprovado` |
| [`memory/`](memory/) | Memoria organizacional, 5 camadas | **6** na APR, **1** na EST *(em vigor)*, **9** na OPR — os **nove atos soberanos** |
| [`governance/`](governance/) | Catalogo mestre, baseline, excecoes, incidentes, aptidao, **pacote soberano** e **roadmap** | **23** `FIT`, **15** `PS`, **15** `PT` *(`+1`: `PT-2026-015`)*, 2 `INC` *(ambos `fechado`)*, 0 `EXC`, **1** roadmap |
| [`departments/`](departments/) | **Indice e projecao comparativa** + as Cartas de departamento | **9 de 9 escritas e 9 de 9 em vigor** — `0` em `em-revisao`. **Cinco em 1.1.0** pelo ato de 2026-07-30 |
| [`CLAUDE.md`](CLAUDE.md) | **Instrucoes permanentes de trabalho** — a regra do roadmap. **NAO e artefato:** sem `id`, sem versao de sequencia, sem entrada de catalogo | **Fora da lista fechada do medidor** — o portao de raiz **recusa medir** ate o Fundador declarar o lado. Achado **`RD-81`** |
| [`governance/roadmap-canonico.md`](governance/roadmap-canonico.md) | **Registro de acompanhamento** — Epicos e Goals, com `[ ]` `[x]` `[~]` `[!]`. **Autoridade nenhuma, nao normativo**; atualizar nao exige ADR, hash, baseline nem ato | **Vive DENTRO da raiz medida** e por isso **conta como artefato**, sem ter entrada no catalogo. Achado **`RD-80`** |
| [`products/`](products/) | **Produtos** — Cartas de Produto, entidade `PRO` | **EXISTE desde 2026-08-01**, criada pelo **item III do nono ato**. **1** Produto: [`PRO-nxtrack`](products/nxtrack/carta.md), `ativo` · `ratificada`, **263** linhas, **5** Capabilities. **Sem indice de diretorio** — achado `RD-85`, aberto |
| `projects/` | Projetos | fase futura |
| `skills/` · `workflows/` · `tools/` | Capacidades, sequencias e ferramentas | fase futura |

Diretorios de fase futura **nascem quando o primeiro artefato do tipo for aprovado**
(FND-03 §7.2) — nao antes.

> **Os contadores de `decisions/`, `rfcs/`, `memory/` e `governance/` estavam para tras, e foram
> corrigidos NA PROJECAO nesta emissao** — `RG-03`, `PJ-03`, `M3`; **nenhuma fonte alterada**.
> Declaravam **25 `ADR`**, **20 `RFC`**, **7** registros na `OPR` e **18 `FIT` · 12 `PS` · 10
> `PT`**, contra **30 · 25 · 9** e **23 · 15 · 14** contados por ferramenta. Achado **`RD-82`**,
> registrado no [catalogo §7](governance/artifact-registry.md).

## O sistema em quinze linhas

**Autoridade.** O Soberano decide; o Gabinete (DEP-EXE) prioriza; Guarda (DEP-GOV, DEP-QAR)
verifica e pode vetar; Linha (PRD, ENG, OPS, GRW) entrega; Plataforma (KMS, TLS) habilita.

**Competencia.** 23 Capabilities dizem o que a organizacao sabe fazer, independentemente de
quem a compoe. Cada uma tem um custodio, mas nenhum monopoliza seu exercicio. Nenhum
componente existe sem vinculo a ao menos uma delas.

**Universo.** 21 entidades em 7 estratos dizem o que pode existir. A lista e fechada: tipo
novo exige RFC, ADR e ratificacao do Soberano. Dependencia dura nunca aponta para estrato
superior, e toda relacao entre tipos consta de uma tabela — o que nao consta, e nulo.

**Estrutura operacional.** Departamento e estrutura **mutavel** que custodia ou exerce
Capabilities — nao e competencia, agente nem equipe. Sua Carta declara doze blocos: o que
custodia e o que exerce, de onde vem cada autoridade, o que **nao** lhe compete, e **em que
materia esta impedido de aprovar ou verificar**. Indicador sem valor medido nao prova
desempenho, e Carta nao entra em vigor por si.

**Mudanca.** Classifica-se por impacto (C0–C3) e reversibilidade (Tipo 1/2). Irreversivel
sempre passa pelo humano. Quem propoe nao aprova.

**Decisao.** Precisa de duas alternativas reais mais "nao fazer nada", criterios definidos
antes da escolha, evidencia e plano de reversao. Aprovada, nunca e editada — e superada.

**Memoria.** Cinco camadas, um fato em um lugar so. O operacional expira por padrao; o
aprendizado sobe quando se confirma; o estrategico so muda por ADR.

**Contexto do Soberano.** O que se sabe sobre quem dirige a empresa vive na memoria
estrategica, com fonte e classe de evidencia por afirmacao, e o que **nao** se sabe fica
escrito como lacuna com gatilho. Orienta onde a norma admite escolha; **nunca** supera norma,
evidencia ou seguranca. Inferencia nao vira preferencia oficial sem ato do Soberano.

**Comunicacao.** Cinco canais, envelope padrao, contexto minimo suficiente. Silencio nao
aprova, nao aceita e nao transfere responsabilidade.

**Evolucao.** A arquitetura se especializa sempre que houver ganho comprovado de
organizacao, reuso ou reducao de contexto — e se consolida de volta quando o ganho nao se
confirma. Ambos os movimentos exigem evidencia (PI-14).

**Aptidao.** Toda mudanca estrutural encerra respondendo se a arquitetura ficou mais simples
de evoluir: complexidade, duplicacao, abstracao ociosa, custo de contexto e reuso. Veredito
negativo bloqueia o encerramento (QG-6).

**Artefato.** Todo documento carrega o mesmo contrato: resumo em uma linha, perfil de
contexto, confidencialidade, revisor distinto do autor e estado de ratificacao. A obrigacao
nasce quando o artefato e **emendado** — alteracao que incrementa MAIOR ou MENOR —, nunca por
retroatividade. O que e derivavel nao se declara. Ninguem carrega o acervo por padrao: o
nucleo obrigatorio custa **6,81% do acervo, medido e reproduzivel** — [catalogo
§2.1](governance/artifact-registry.md), cuja base de medicao **deixou de ser lacuna**: `RD-26`
esta **reconciliado**, com cobertura de **100%** e o metodo declarado em duas regras. **A
ausencia do campo no frontmatter nao e defeito para o acervo anterior a vigencia de FND-10** —
e a migracao de custo zero que §2.3 prescreve.

**Fonte unica.** Tabela normativa vive em um lugar so. Todo documento que exibe conteudo de
outro **declara projecao**: fonte, campos, finalidade e metodo de atualizacao. Quem escreve
verifica antes de submeter — nao so o auditor, depois.

**Fronteira.** O que nasce aqui e `native`. O que vem de fora nao tem autoridade por existir:
passa por proveniencia, fit-gap, classificacao, validacao independente e decisao formal — ou
nao entra.

## Proxima fase

> **✅ SUPERADO em 2026-08-02 pela Missao 1.13.5 — a primeira `Spec` EXISTE.** [`SPC-001`](products/nxtrack/specs/SPC-001-governanca-de-dado-pessoal-do-nxtrack.md)
> foi criada pelo rito `RFC-0026` → `ADR-0031` → `SPC-001` → `FIT-2026-024`, em classe
> **`C2 · Tipo 2`** — **elevada do piso `C1`** porque a coluna `C1 · T2` de `SF-10` poe
> *Proposta* e *Aprovacao* no mesmo Departamento para o tipo `SPC`, e `FND-04 §3.1` declara
> **nula** a aprovacao com acumulo de papel. **Achado `RD-91`, dono SOBERANO: enquanto ele nao
> for sanado, toda `Spec` do acervo tera de nascer em `C2` para nao nascer nula.**
> O texto abaixo e **historico e preservado**.

> **O que a proxima missao precisa saber, em tres linhas.** O **Framework de Specifications
> existe** e a **primeira `Spec` nao e criavel**: o proximo passo **nao e trabalho de
> Departamento, e um ato do Soberano** — **`S1`** *(criar o primeiro Produto)* ou **`S2`**
> *(ampliar a `Spec` a materia nao-produto, C3)*. **Nenhuma `Spec` deve ser criada antes dessa
> escolha:** criar uma agora produz artefato **nulo** (`MT-01`, `AC-06`) e **incidente de
> conformidade** (`LV-11`). Decisao da Missao 1.13: **`ADJUST`** —
> [PT-2026-007](governance/relatorio-transicao-2026-07-29-specifications.md).

> **✅ ATUALIZADO em 2026-08-01 — a escolha foi feita, o ato foi emitido, e a APLICACAO ESTA
> FEITA.** O Soberano escolheu **`S1`** e emitiu o ato que cria `PRO-nxtrack`
> ([MSG-2026-0009](memory/operacional/MSG-2026-0009-ato-soberano-admissao-do-nxtrack.md), item
> **III**); a **Missao 1.13.4.5** o **consumiu** na ordem de
> [`PS-2026-016 §6.2`](governance/pacote-soberano-2026-08-01-nxtrack.md), **passo a passo**:
> `O4` em `RFC-0025` *(pela variante)* e em `ADR-0030`; `products/nxtrack/carta.md` criado com o
> `H-A` **do arquivo aplicado** publicado; catalogo e indices reconciliados **na mesma mudanca**;
> **`products`** e **`CLAUDE.md`** declarados no medidor *(`RD-81` ✅ **FECHADO**)*; e
> **`BL-2026-08-01-02`** reproduzida em **duas** execucoes.
> **A Missao 1.13.4.6 fechou `RD-33`** — a **missao propria** que o ato reservou —, por rito
> **ministerial**, com **`0` atos emitidos** e **`0` fontes emendadas**, e emitiu
> **`BL-2026-08-01-03`**.
> **O PROXIMO PASSO E A `1.13.5` — A PRIMEIRA `Spec`**, cuja materia o ato ja fixou:
> **`LM-6(a)`**, com **prioridade** sobre as demais de `LA-7`. **Ela nasce com `GO-TO-SPECS`
> EXERCIVEL** — o que nenhuma missao anterior teve.

Nenhum agente, workflow ou produto foi criado — conforme determinado. A **condicao unica de
saida** do rollout de FIT-2026-007 foi cumprida: **a quinta Carta e a de DEP-GOV**, escrita
sozinha, e ela **declara em B9 o impedimento que RE-03 exigia**.

**Decisao de fechamento da camada de Cartas: `READY-FOR-RATIFICATION`** —
[FIT-2026-008 §Fechamento](governance/fitness/FIT-2026-008-rollout-das-cartas.md). **Esta tabela
avalia a camada de Cartas, e o estado dela nao mudou.** O **estado corrente do sistema** e outro,
e vive acima: **`GO-TO-SPECS` liberado**, com as nove Cartas **em vigor** desde
[MSG-2026-0004](memory/operacional/MSG-2026-0004-ato-soberano-cartas-emenda-constitucional-e-regime-do-fitness-check.md)
e as emendas `DEP-KMS` e `DEP-ENG` **1.1.0** desde
[MSG-2026-0006](memory/operacional/MSG-2026-0006-ato-soberano-aplicacao-integral.md). A ressalva
**b** — `IC-2` — permanece contida por `IR-11` e **fechada quanto ao texto** por `ADR-0014`,
ratificado.

| # | Condicao de fechamento da camada | Estado |
|---|---|---|
| a | **Cobertura 9/9** | ✅ **Cumprida documentalmente** — 9 Cartas, 23 custodias, 0 Capabilities sem custodio |
| b | **Autoridade inequivoca** | ⚠️ **Cumprida com ressalva** — 0 autoridades autodeclaradas, 92 impedimentos com substituto. A ressalva e **IC-2**, contido por `IR-11` |
| c | **Validacao independente** | ✅ **55 testes, 53 ✅, 2 ⚠️, 0 ❌** — revisor distinto do autor em 9 de 9 |
| d | **Rastreabilidade** | ✅ **0 links quebrados** em 1.267; **0** artefatos M1 editados; cadeia ato → versao → conteudo → estado fechada |
| e | **Pacote soberano completo** | ✅ [**PS-2026-002**](governance/pacote-soberano-2026-07-28-cartas.md), com o **caminho exato anexado** |

**Tres pendencias, em um unico pacote:** as **cinco Cartas** em `em-revisao`, a **emenda C3** a
FND-01 §7.3 e a questao sobre **ratificacao de `FIT`**.

> **A camada esta pronta para ratificacao, e nao para consumo — e a distincao e deliberada.**
> Cinco das nove Cartas **nao estao em vigor**, e **desempenho nao exercido permanece nao
> comprovado**: **41 de 123** indicadores estao marcados `definido, sem valor`, e nenhuma Carta
> foi exercida em operacao real. **Chamar isso de camada pronta seria afirmar o que nao foi
> medido.**

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.22.0 | 2026-08-01 | DEP-GOV | Estado apos o **FECHAMENTO DE `RD-33` — Missao 1.13.4.6, ministerial**, e **o acervo fica SEM PENDENCIA BLOQUEANTE pela primeira vez desde 2026-07-29**. **O rito foi DETERMINADO antes de exercido, e nao presumido por analogia:** **`0`** regras de rito de fechamento de achado existem no acervo *(varredura declarada)*, e o rito veio de **`PA-01`, `PA-03`, `PA-07` e `PA-13`** de [ADR-0020](decisions/ADR-0020-regime-ministerial-de-promulgacao-e-ativacao.md), **`AU-06`**, **`FND-04 §4 [7]`** e **`RG-01`/`RG-03`/`RG-04`/`AC-09`** de `FND-10`, com **cinco precedentes medidos**. **A reserva do item VII do nono ato e de `LA-3` e TEMPORAL *(«apos a vigencia»)* e DE SEDE *(«missao propria»)*, jamais de classe de rito** — as palavras *ato*, *ratificacao*, *`C3`* e *`1.13.5`* tem **`0`** ocorrencias nela, e [`MSG-2026-0009 §8`](memory/operacional/MSG-2026-0009-ato-soberano-admissao-do-nxtrack.md) poe *"`RD-33` destravado"* **ANTES** de 1.13.5. **A leitura divergente de `PT-2026-015 §10` e do roadmap foi declarada e nenhum dos dois foi editado**, e **`READY-FOR-RATIFICATION` foi construida e descartada com prova**, hipotese por hipotese. **Prova por EXERCICIO**, o mesmo metodo que abriu o achado: `DoR` de `SF-23` reexercido, item **(9)** **PASSA**, item **(4)** em **5 de 5** `Capabilities` ativas — **`GO-TO-SPECS` passa de *liberado e nao exercivel* a EXERCIVEL**. **`0` bytes nas tres fontes do vinculo `Spec` × `Produto`: ele foi SATISFEITO, nunca removido.** **O fechamento e PARCIAL POR CONSTRUCAO** — a `Spec` de materia **nao-produto**, que so `S2` cria e que segue **deferida**, **migra para `RD-88`**, ABERTO. Achados novos **`RD-88`**, **`RD-89`** *(duas entradas de §7 do catalogo na mesma linha fisica; ✅ corrigido na projecao)* e **`RD-90`** *(**26 de 31** ponteiros de sucessao entre baselines apontam para a subsecao errada, medido por ferramenta; **ABERTO e deliberadamente nao varrido**, por `BL-02` e pelo congelamento)*. **`RD-80` e `RD-83` a `RD-87` declarados, e NENHUM fechado.** **`0` atos emitidos, `0` `Spec`s criadas, `0` bytes em `products/`, `0` bytes em fundacional e `0` historicos editados.** Baseline **`BL-2026-08-01-03`**, reproduzida em **duas** execucoes. |
| 1.21.0 | 2026-08-01 | DEP-GOV | Estado apos a **APLICACAO do nono ato — Missao 1.13.4.5, ministerial**, e **o acervo tem o seu PRIMEIRO PRODUTO**. [**`PRO-nxtrack`**](products/nxtrack/carta.md) existe em `products/nxtrack/carta.md`, `ativo` · `ratificada`, **`H-A` do aplicado `fca656a9…39e2`** — **distinto do `H-A` do candidato**, que nao e artefato e ficou intacto. **`ADR-0030` `ativo` · `ratificada`** e **`RFC-0025` `aprovado`** *(pela variante; o ciclo de `RFC` termina em `aprovado`)*. **`products/` nasce como raiz do acervo**, e estreiam a entidade **`PRO`** e o tipo **`Carta de Produto`** — §2 vai a **11 de 21** entidades e **18 de 33** tipos. **Baseline `BL-2026-08-01-02`**, reproduzida em **duas** execucoes, com o medidor declarando **`products`** *(`OA-1`)* e **`CLAUDE.md`** — achado **`RD-81` ✅ FECHADO pelo proprio dono**, o Soberano, no despacho de abertura. **`H-P` 2/2, `H-N` invariante 2/2, `IR-09` 3/3, `atualizado_em` nao tocado, `0` bytes fora do conjunto autorizado** provados **arquivo a arquivo** contra a copia datada; **candidato intacto** por objeto de commit. **`RD-33` NAO fecha** — a condicao de fato caiu, mas o item **VII** do ato e `LA-3` **reservam** o fechamento a missao propria. **`0` `Spec`s, `0` atos emitidos, `Q3` e `Q4` sem resposta.** Achados novos **`RD-83`** *(ancora `HEAD` de `CA-5` mede a arvore de terceiro e ja nao reproduz; o `tree` da subarvore reproduz)*, **`RD-84`** *(agregados de §2 divergem do que enumeram)*, **`RD-85`** *(`products/` sem indice)*, **`RD-86`** *(o candidato exigiu 5 ajustes onde o ato ordenou 2)* e **`RD-87`** *(tres indices emendados sem `versao` nova)* — **todos com dono e gatilho, nenhum gera missao**. |
| 1.20.0 | 2026-08-01 | DEP-GOV | Estado apos o **NONO ATO SOBERANO, emitido e NAO consumido** — [MSG-2026-0009](memory/operacional/MSG-2026-0009-ato-soberano-admissao-do-nxtrack.md), ancorado no `H-A` `e6fa26e8…44ae` do pacote [PS-2026-016](governance/pacote-soberano-2026-08-01-nxtrack.md) **1.2.0**, itens **I a VII**, linhas **185–328**. **RATIFICA `ADR-0030`**, **APROVA `RFC-0025`** e **CRIA o Produto `PRO-nxtrack`** com `G0` = `IDENTIDADE` e `G3` = `RECOGNIZE`. **`CA-1` a `CA-6` em 6 de 6**, porque **`Q2` foi gravada como artefato pela primeira vez**: a ressalva de `PS-2026-013 §7` **nao condiciona** o ato. **`H-A` 5/5, `H-P` 2/2** *(o de `RFC-0025` pela variante declarada)* **e `H-N` invariante 2/2**, remedidos na emissao. **NADA APLICADO:** `0` transicoes `O4`, `products/` inexistente, **`0` Produtos**, **`0` `Spec`s**, **`0` baselines emitidas**, `RD-33` **BLOQUEANTE** por declaracao do proprio ato. **Segundo ato do acervo registrado ANTES da aplicacao.** `Q3` e `Q4` **nao respondidas**. Nasce [`CLAUDE.md`](CLAUDE.md) com a **regra permanente do roadmap**, e o **Mapa do repositorio** e reconciliado com valores **contados por ferramenta**. Achados novos **`RD-80`** *(roadmap medido sem entrada de catalogo)*, **`RD-81`** *(`CLAUDE.md` faz o portao de raiz recusar medir)* e **`RD-82`** *(Mapa quatro linhas atras)*; **`RD-78`** e **`RD-79`** projetados no catalogo §7, onde faltavam. **Todos abertos, com dono e gatilho, e sem missao designada.** |
| 1.19.0 | 2026-08-01 | DEP-GOV | Estado apos a **Missao 1.13.4.4 — portao `ADR-0007` sobre o nXtrack**: **213** artefatos *(**`+5`**)*, baseline **`BL-2026-08-01-01`**, decisao **`READY-FOR-RATIFICATION`**. **O portao de origem externa foi exercido pela SEGUNDA vez, e a segunda foi a primeira sob a norma emendada:** `G0` = `IDENTIDADE`, `G3` = `RECOGNIZE` — **primeira aplicacao prospectiva da classe**. **`Q1` RESPONDIDA** *(o nXtrack; `PT-2026-009` e `PS-2026-013` sao artefatos distintos)*. **`G1` fecha por medicao:** 17 de 17 fontes atribuiveis, `0` sem commit em 183 rastreados, `758` no hospedeiro, `tree` `b9b36be9…fb4b` congelado. **`0`** Produtos admitidos, **`0`** atos emitidos, **`0`** bytes do candidato no acervo, **`0`** fundacionais e **`0`** historicos alterados. **`RD-33` segue bloqueante**; `S1` **preparada e nao consumida**. **7** achados novos *(`RD-71` a `RD-77`)*, **nenhum gera missao**. |
| 1.18.0 | 2026-07-31 | DEP-GOV | Estado apos as **Missoes 1.13.4.2 e 1.13.4.3**: **208** artefatos, baseline **`BL-2026-07-31-08`**, decisao **`APLICADO`**. **O OITAVO ATO SOBERANO foi emitido e CONSUMIDO** — [MSG-2026-0008](memory/operacional/MSG-2026-0008-ato-soberano-emendas-e1-e-e3.md), ancorado no `H-A` da minuta [PS-2026-015](governance/pacote-soberano-2026-07-31-emendas-de-instrumento.md) **1.2.0**. **`ADR-0027` `ativo`** *(DEP-EXE, `C2`)* e **`ADR-0029` `ativo` · `ratificada`**, com `H-P` **2/2**, `H-N` invariante **2/2** e `IR-09` **2/2**. Nasce [atos-superados](governance/atos-superados.md), registro de `SA-6`, **contador em `0`**. **`RC-1` em vigor**: o `REWRITE` da 1.13.4 **le-se `RECOGNIZE`**, **sem editar os cinco artefatos** (`RC-2`) e **sem mudar hash algum** (`RC-3`). Antes disso, `CA-2` da minuta passou de **bloqueante a informativo** — **insatisfazivel por construcao**, porque o pacote mora dentro do acervo que media. **`E2` ADIADA e intacta**; **`Q1` e `RD-33` bloqueantes**; **`0` Produtos, `0` `Spec`s**; achados novos **`RD-68`**, **`RD-69`** e **`RD-70`**, todos **abertos, com dono e gatilho, e sem missao designada**. |
| 1.17.0 | 2026-07-31 | DEP-GOV | Estado apos a **Missao 1.13.4.2 — as tres emendas de instrumento**: **206** artefatos, baseline **`BL-2026-07-31-03`**, decisao **`READY-FOR-RATIFICATION`**. **Nove objetos criados e NENHUM em vigor** — `RFC-0022` a `RFC-0024`, `ADR-0027` a `ADR-0029`, `FIT-2026-020` a `FIT-2026-022` —, mais [PS-2026-015](governance/pacote-soberano-2026-07-31-emendas-de-instrumento.md), com **minuta de ato redigida e NAO emitida**. **A dependencia entre as tres emendas foi MEDIDA em `0`**, e por isso elas sao **tres unidades independentes**, sem conjunto atomico. **Classes determinadas percorrendo as cinco hipoteses de `C3`**, nunca presumidas. Autoverificacao **remedida pelos dois criterios: `0` e `131`**, base **138**. Achado novo **`RD-65`**. **`0` bytes** em `ADR-0005`, `ADR-0007`, `ADR-0012`, `FND-10` e no pacote da 1.13.4; **`0` atos emitidos**; **`Q1` e `RD-33` continuam bloqueantes**. |
| 1.16.0 | 2026-07-31 | DEP-GOV | Estado apos a **Missao 1.13.4.1 — manutencao dos instrumentos**: **195** artefatos, baseline **`BL-2026-07-31-02`**, decisao **`BLOCKED`** — o Item 0 reprova com **5 de 19** caminhos **NAO ATRIBUIVEL**. **`RD-53` fechado por instrumento novo** — o defeito era do comando, e `BL-2026-07-30-01` **reproduz nos 64 digitos**. **`RD-56`, `RD-57` e `RD-58` fechados**; **`RD-49`** corrigido em tres candidatos **nao aplicados**; **Item 0 em 19 de 19**; **tres minutas** preparadas e **`0`** aplicadas; autoverificacao medida pelos **dois** criterios *(`0` e `130`)*; **cinco** achados novos *(`RD-60` a `RD-64`)*. **`0` bytes** no pacote da 1.13.4, nas fundacionais, nos `ADR`, `MSG`, `FIT`, `PT` historicos e nas baselines. |
| 1.15.0 | 2026-07-31 | DEP-GOV | Estado apos a **Missao 1.13.4 — S1, a admissao canonica do medAlly**: **194** artefatos, baseline **`BL-2026-07-31-01`**, decisao **`READY-FOR-RATIFICATION`** com **uma questao bloqueante**. **O portao de origem externa de `ADR-0007` foi EXERCIDO PELA PRIMEIRA VEZ** — `G1`–`G4` comprovados, `G5` preparado, **`G3` = `REWRITE`**, **`0` bytes admitidos**, **`0` bytes escritos no candidato**. **Dois** objetos submetidos em `PS-2026-014`, com `H-N` invariante **2 de 2** e `IR-09` **2 de 2**, apos o instrumento reproduzir **10 de 10** controles publicados. **`0` Produtos em vigor · `products/` inexistente · `0` `Spec`s · `RD-33` BLOQUEANTE.** **Seis** achados novos — `RD-53` a `RD-58`. **`Q1`:** a decisao **7** fixou o nXtrack como primeiro produto **comercial** ou como primeiro Produto **do acervo**? **Sob a segunda leitura, `PS-2026-014` e inadmissivel.** |
| 1.14.0 | 2026-07-30 | DEP-GOV | Estado apos a **Missao 1.13.3 — vigencia do Framework de Specifications**: **189** artefatos, baseline **`BL-2026-07-30-02`**, decisao **`SPEC-FRAMEWORK-IN-FORCE`**. **O setimo ato soberano foi consumido** ([MSG-2026-0007](memory/operacional/MSG-2026-0007-ato-soberano-vigencia-do-framework-de-specifications.md)) e os **catorze** objetos entraram em vigor: `ADR-0022` a `ADR-0025`, **`FND-11` 1.0.0** *(criacao — `foundation/` passa a **onze** documentos)*, `FND-01` **1.7.0 cumulativa**, `FND-02` **1.4.0**, `FND-03` **1.6.0**, `FND-10` **1.5.0** e as **cinco** Cartas **1.1.0**. `H-P` **14/14**, `H-N` invariante **10/10**, `IR-09` **10/10**, **`0`** bytes fora dos diffs autorizados. **`RD-27`, `RD-31` e `RD-37` FECHADOS**; **`RD-49`** a **`RD-52`** abertos, tres deles ja corrigidos. **Nenhum Produto, Projeto ou `Spec` criado — `RD-33` permanece bloqueante.** |
| 1.13.0 | 2026-07-30 | DEP-GOV | Estado apos a **Missao 1.13.2 — convergencia pre-ratificacao**: **185** artefatos, baseline **`BL-2026-07-30-01`**, decisao **`READY-FOR-RATIFICATION`**. **Dois ritos completos, uma coordenacao, uma consolidacao e nada aplicado.** [ADR-0024](decisions/ADR-0024-conformidade-de-contrato-das-fundacionais.md) *(`C3 · Tipo 2`)* **fecha `RD-27` integralmente** — backfill de `AC-08` em `FND-01` e `FND-02` e correcao de `FND-10 §8.5` —, com **`0` bytes de corpo alterados nos tres**, medido por `diff`; [ADR-0025](decisions/ADR-0025-extensao-da-propagacao-de-qg-1-as-cartas-restantes.md) *(`C2 · Tipo 2`, **primeira dispensa de RFC do acervo**, com as duas condicoes de `FND-04 §2` verificadas e concordancia escrita entre partes distintas)* **fecha `RD-37`**, e a familia das **nove** Cartas vai de **11 afirmacoes falsas em 4** para **`0` em `0`**, com **5 de 5 caminhos coerentes**. **As duas colisoes que a missao existia para eliminar foram eliminadas e medidas:** `FND-01` sai de **duas variantes vivas para uma** — a **1.7.0 cumulativa** — e a **sobreposicao de diff entre objetos do ato vai de 1 para `0`**, com **14 objetos sobre 14 arquivos**. **A pergunta que a missao mandou responder tem resposta NAO:** `V2` **nao** e byte a byte o candidato cumulativo, e a diferenca **nao e cosmetica** — ele atribui a `ADR-0022` o backfill que o **escopo literal de `ADR-0022` exclui**, e `ADR-0022` e **`M1`**: achado **`RD-45`**. **Quatro achados novos, `RD-45` a `RD-48`, e nenhum foi encontrado lendo** — um por **construir**, um por **contar a secao inteira**, um por **montar dois tipos lado a lado** e um por **remedir**. **`RD-48` mede que o custo de reversao de `ADR-0020` acertou no que contou** *(6 indices `M3`, ainda 6)* **e envelheceu no que nao entrou na conta** *(referencias `M1` nao corrigiveis, de 4 a 12)* — **sem que isso o reclassifique**. **`0` objetos em vigor · `0` de 73 fontes normativas alteradas, por `cmp` · `0` artefatos `M1` editados · `0` candidatos historicos tocados · `0` credenciais · `20 de 20` controles de integridade reproduzem.** **Quatro pendencias ao Soberano, e uma bloqueia — `RD-33`, que continua sendo a unica.** |
| 1.12.0 | 2026-07-29 | DEP-GOV | Estado apos a **Missao 1.13.1 — canonizacao de Specifications e correcao de `RD-31`**: **177** artefatos, baseline **`BL-2026-07-29-10`**, decisao **`READY-FOR-RATIFICATION`**. **Dois ritos completos e nada aplicado.** [ADR-0022](decisions/ADR-0022-sede-canonica-do-framework-de-specifications.md) *(`C3 · Tipo 1`)* submete **`FND-11`** — sede fundacional de `SF-01` a `SF-32` — e as emendas a **`FND-01` 1.6.0** e **`FND-03` 1.6.0`**; [ADR-0023](decisions/ADR-0023-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md) *(`C2 · Tipo 2`)* propaga `ADR-0018` e `ADR-0019` as Cartas de `DEP-PRD` e `DEP-EXE`. **A migracao das 32 regras foi provada por ferramenta:** **14** blocos de `diff`, **`0`** nas outras **30** regras, **`0` de 32** identificadores renumerados, e **uma unica alteracao de merito** — `SF-32`, de `M1` para `M2` —, cujo tradeoff esta declarado no sentido correto: **promover a norma protege e encarece a correcao**. **`RD-31` medido:** afirmacoes falsas em `DEP-PRD` **8 → 0**; `QG-1` na Carta de `DEP-EXE` **0 → 22 ocorrencias**; Cartas com titular do portao **0 de 9 → 2 de 9**. **`PILOTO-DEFERIDO` formalizado**, com as duas condicoes de desbloqueio e o que a ausencia dos pilotos **nao** autoriza. **Oito achados novos:** `RD-37` *(Media — **3 Cartas ratificadas** nunca enumeradas afirmam que `DEP-PRD` libera `QG-1`; o defeito estava em **4** Cartas e **11** afirmacoes, e o acervo sai de **11 em 4** para **3 em 3** — melhora medida, **nao fechamento**)*, `RD-38`, `RD-39`, `RD-40`, `RD-41`, `RD-42`, `RD-43` *(Media — **`IR-03` nao exclui `superado_por` de `H-N`**, logo o unico campo de sucessao de um `ADR` **altera o proprio `H-N`**; encontrado **por medir, nao por ler**)* e `RD-44` *(Media — `ADR-0021` **nunca recebeu linha** na tabela de `decisions/README`)*. **Duas colisoes de norma foram declaradas em vez de resolvidas em silencio** (`PI-13`), e nas duas o Soberano recebeu **variantes medidas com hash** em lugar de uma escolha tacita. **`0` fontes normativas alteradas · `0` artefatos `M2` emendados · `0` bytes em `ADR-0021` · `0` artefatos `M1` editados · `0` linhas de evidencia externa lidas.** **Sete pendencias ao Soberano, e uma bloqueia.** |
| 1.11.0 | 2026-07-29 | DEP-GOV | Estado apos a **Missao 1.13 — Framework de Specifications**: **169** artefatos, baseline **`BL-2026-07-29-09`**. **`SF-01` a `SF-32` instituidos** por [ADR-0021](decisions/ADR-0021-framework-de-specifications.md), **`C2 · Tipo 2`**, com **`0` arquivos de `foundation/` alterados** *(por `cmp`)* e **`0` entidades, tipos documentais, portoes, papeis ou verbos de autoridade criados** — contrato de **21 blocos**, semantica normativa, **7 perfis**, matriz de **50 celulas**, cadeia de **9 elos**, `DoR`/`DoD`, mudanca e economia de contexto. **`RD-23` FECHADA, e maior do que estava declarada:** **5** defeitos em `TPL-spec` onde o achado citava **2**, corrigidos em **1.1.0**, com **hash antes e depois** e diff literal reversivel. **Testado em 12 casos — 11 coerentes e 1 divergente**, e a divergencia **virou achado**. **⛔ Nenhuma `Spec` e criavel:** tres fontes vigentes a vinculam a `Produto` e **`0` produtos existem** — **`RD-33`**, a **unica pendencia bloqueante do acervo**; **as duas Specs piloto nao foram criadas**, e as duas saidas faceis foram **recusadas com norma citada**. **Seis achados novos:** `RD-31` *(Alta — a Carta de `DEP-PRD` tem **8** afirmacoes falsas e **`DEP-EXE` nao declara `QG-1` em nenhuma linha**: o portao da `Spec` **nao tem titular em Carta alguma**)*, `RD-32` *(Media — **4** contadores oficiais defasados em **8** valores, com risco de **colisao de identificador**; corrigidos, e a causa **codificada em `SF-32`**)*, `RD-33` *(Alta, bloqueante)*, `RD-34` *(Baixa — **19 de 19** `TPL`)* `RD-35` *(Media — **2** agregados; corrigidos)* e `RD-36` *(Media — **o razao de ressalvas nao fecha**; cascata devida executada, **reconciliacao integral nao executada**, com o limite declarado)*. **Evidencia externa `A4` avaliada e NAO adotada** — **236 de 33.676 linhas, `0,70%`**, **0 formatos importados**. **`RC-02`: `DEP-GOV` nao e autor de nenhum instrumento normativo desta missao — primeira vez em quinze.** Decisao: **`ADJUST`**; **cinco pendencias ao Soberano, e uma bloqueia**. |
| 1.8.0 | 2026-07-28 | DEP-GOV | Estado apos a **Missao 1.9** — **rollout das cinco Cartas restantes**. Terceiro ato soberano ([MSG-2026-0003](memory/operacional/MSG-2026-0003-ato-soberano-emenda-qar-e-criterio-de-consolidacao.md)): **`DEP-QAR` 1.1.0 em vigor**, com **IC-5 corrigido** e a 1.0.0 preservada; e o **criterio de consolidacao** determinado, formalizado em **ADR-0013** **sem emendar nenhuma fundacional**. **Cobertura documental 9/9**; as cinco novas em `em-revisao`. **RFC-0011 e ADR-0014** levam a emenda **C3** de pergunta a texto, **sem vigencia**. **8 ressalvas e achados fechados**; **8 achados novos**, tres deles retidos em Cartas ratificadas. Baseline **`BL-06`**, **131** artefatos. Fechamento **READY-FOR-RATIFICATION**; **3** pendencias em um pacote. |
| 1.7.0 | 2026-07-28 | DEP-GOV | Estado apos a **Missao 1.8** — **Primeira Revisao Estrutural**. Segundo ato soberano ([MSG-2026-0002](memory/operacional/MSG-2026-0002-ato-soberano-cartas-comando-plataforma-e-contexto.md)): **`DEP-EXE`, `DEP-KMS` e `MEM-EST-0001` em vigor**; `FIT-2026-001` e `FIT-2026-002` **acolhidos como pareceres**; **INC-2026-002 `fechado`**. **ADR-0012** e **RFC-0009** instituem a integridade do ato de ratificacao. **IC-8 resolvido a partir da fonte**, sem emendar FND-10. **7 ressalvas e 7 achados fechados**; **EV-08 encerrada como `AJUSTAR`**. Baseline **`BL-05`**, **117** artefatos. Rollout **GO-CONDITIONAL**; **1** pendencia ao Soberano. **Corrige RE-07:** o frontmatter declarava `1.5.0` enquanto o historico ja registrava `1.6.0`. |
| 1.6.0 | 2026-07-28 | DEP-GOV | Estado apos a **Missao 1.7**: **ativacao de `DEP-QAR` e `DEP-ENG`** por ato soberano de 2026-07-28 ([MSG-2026-0001](memory/operacional/MSG-2026-0001-ato-soberano-ratificacao-cartas-piloto.md)), Cartas de **Comando** (`DEP-EXE`) e **Plataforma** (`DEP-KMS`) em `em-revisao`, **oito cenarios interclasses** nas quatro classes, `TPL-carta-departamento` **1.2.0**. Baseline **`BL-04`**, **112** artefatos. Rollout **ADJUST**; consolidacao **EV-08 aberta**; **4** pendencias ao Soberano. |
| 1.5.0 | 2026-07-28 | DEP-GOV | Estado apos a **Missao 1.6**: Contrato de Carta de Departamento (**ADR-0011**), matriz Departamento × Capability, `TPL-carta-departamento` **1.1.0** e as **duas primeiras Cartas** — `DEP-QAR` e `DEP-ENG`, ambas em `em-revisao`. Baseline **`BL-03`**, **107** artefatos. Decisao de rollout **ADJUST**. |
| 1.10.0 | 2026-07-29 | DEP-GOV | Estado apos o **fechamento operacional**: **164** artefatos, baseline **`BL-2026-07-29-08`**. **`GO-TO-SPECS` LIBERADO — 8 de 8 condicoes de §X**, e **pela primeira vez o fechamento nao depende de nenhum ato pendente**. **`RD-22` fechado por refutacao de premissa** — os titulares de promulgacao e ativacao estavam declarados em `FND-04 §4 [7]` e `FND-07 §5 [10]`, e a varredura media o **termo** em vez da **funcao** ([MEM-APR-0005](memory/aprendizado/MEM-APR-0005-medir-a-ausencia-na-fonte-errada.md)) —, formalizado por **ADR-0020**, **`C2 · Tipo 2`**, com **0 fontes emendadas, 0 titulares criados e 0 atos exigidos**. **`RD-26` reconciliado:** a distribuicao de perfil passa a reproduzir **o total do acervo**, cobertura **100%**, **0 nao classificados**. **Quatro achados novos** — `RD-27` *(Media, aberto: backfill que altera `H-N`)*, `RD-28` *(Media, corrigido: **10** valores de projecao, **9** anteriores)*, `RD-29` *(Baixa, corrigido)* e `RD-30` *(Baixa, atendido em `BL-08`)*. **Zero fontes normativas alteradas**, medido por `cmp`; **os dez objetos do sexto ato rehasheados, 10 de 10 nos 64 digitos.** **Pre-correcao obrigatoria antes da 1a Spec: `RD-23`.** |
| 1.9.0 | 2026-07-29 | DEP-GOV | Estado apos a **aplicacao do sexto ato soberano**: **159** artefatos, baseline **`BL-2026-07-29-07`**. **FND-01 1.5.0**, **FND-02 1.3.0**, **FND-09 1.5.0** e **FND-10 1.4.0** promulgadas; **ADR-0001 a ADR-0019 vigentes**, sem nenhum retido; **9 de 9 Cartas em vigor**, com `DEP-KMS` e `DEP-ENG` em **1.1.0**. Esta projecao estava **quatro missoes atrasada** — declarava `BL-2026-07-28-06`, **117** artefatos e **4** Cartas em vigor —, e foi reconciliada por ferramenta *(achado **RD-25**)*. A afirmacao de custo do nucleo passou a **remeter ao catalogo §2.1**, cuja base de medicao esta **sob achado `RD-26`**: **61 de 159 artefatos nao declaram `perfil_contexto`**, e por isso o percentual **nao foi reescrito com numero novo**. |
| 1.4.0 | 2026-07-28 | DEP-GOV | Estado apos a **Missao 1.5**: Contexto do Soberano, ADR-0009 e ADR-0010, baseline **`BL-02`**, 100 artefatos. Frontmatter passa a declarar os cinco campos do contrato de artefato (AC-08, **ADR-0009**), fechando o achado C13 quanto a este artefato. |
| 1.3.0 | 2026-07-28 | DEP-GOV | Estado apos a Missao 1.4: fronteira, ratificacao concluida e baseline `BL-01`. |
