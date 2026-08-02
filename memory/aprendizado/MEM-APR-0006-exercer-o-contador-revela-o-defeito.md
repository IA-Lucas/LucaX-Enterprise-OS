---
id: MEM-APR-0006-exercer-o-contador-revela-o-defeito
titulo: Exercer o instrumento revela o defeito que ler o instrumento nao revela
tipo: memoria
versao: 1.0.0
status: ativo
camada_memoria: aprendizado
autor: DEP-KMS
proprietario: DEP-KMS
aprovador: DEP-KMS
criado_em: 2026-07-29
atualizado_em: 2026-07-29
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0021]
substitui: []
substituido_por: null
origem: RFC-0017 §3.5, ADR-0021 §9 caso T-12 e FIT-2026-015 §F6
evidencia: Tres achados da Missao 1.13 nasceram de exercer instrumentos que quinze missoes de auditoria por leitura nao alcancaram — RD-32 ao pedir o numero da decisao ao contador, RD-31 ao simular o consumo pelo caminho errado, RD-33 ao rodar o DoR antes de criar
confianca: alta
ocorrencias: 1
ttl: permanente
aplica_se_a: [global]
resumo: Registra que auditoria por leitura confirma o que o artefato afirma, que so o uso do instrumento revela o defeito, e fixa quatro verificacoes que substituem a leitura.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# Exercer o instrumento revela o defeito que ler o instrumento nao revela

## Proposito
Registrar por que **tres achados** da Missao 1.13 — **`RD-31`**, **`RD-32`** e **`RD-33`** —
apareceram no primeiro ciclo em que os instrumentos foram **usados** em vez de lidos, embora
**quinze missoes** de auditoria documental tivessem passado pelos mesmos arquivos.

## Escopo
Aplica-se a **todo instrumento que existe para ser usado** — contador de sequencia, portao,
matriz de autoridade, checklist, `DoR`, `DoD`, template. **Nao** se aplica a verificacao de
**conteudo declarativo**, onde a leitura e o metodo correto e continua sendo insubstituivel.

## Responsaveis
| Papel | Quem |
|---|---|
| Dono do registro | **DEP-KMS** |
| Autor da licao | **DEP-PRD** — produziu os tres achados |
| Verificacao independente | **DEP-QAR** — [FIT-2026-015 §F6](../../governance/fitness/FIT-2026-015-framework-de-specifications.md) |
| Aplicacao obrigatoria | **DEP-GOV**, na auditoria de coerencia interna (FND-04 §8) |

---

## Situacao

A Missao 1.13 recebeu o acervo em `GO-TO-SPECS`, com **8 de 8** condicoes de §X apuradas, uma
baseline que **reproduziu nos 64 digitos** antes de qualquer escrita, **`0` links quebrados**,
**`0` autoverificacoes** e **uma** pre-correcao declarada (`RD-23`).

**Todas as verificacoes anteriores tinham sido feitas por leitura:** comparar projecao contra
fonte, somar coluna, conferir campo a campo, medir hash. Esse metodo produziu **sete** achados
reais nas missoes 1.10 a 1.12.1 — `RD-04`, `RD-06`, `RD-16`, `RD-20`, `RD-24`, `RD-25` e `RD-28`.

Nesta missao, pela primeira vez, tres instrumentos foram **exercidos**: pediu-se um numero ao
contador oficial, simulou-se o consumo da matriz de autoridade e rodou-se o `DoR` de criacao.

## Observado

| Achado | Instrumento | O que a **leitura** dizia | O que o **uso** revelou |
|---|---|---|---|
| **`RD-32`** | Contador oficial de sequencia (`FND-03 §2.3`, `RG-04`) | A tabela de decisoes estava **correta e completa** — `ADR-0020` listado, com classe, tipo, status e data | **Ao pedir o proximo numero**, o contador respondeu **`0020`** — um numero **que ja existe**. **4** contadores defasados, **8** valores, risco de **colisao de identificador** |
| **`RD-31`** | Matriz de autoridade × Cartas | `FND-01 §6.2` **fora emendada** por `ADR-0018`, e a cascata para a Carta de `DEP-PRD` **fora declarada devida** em `PT-2026-004 §3.1`, com **4** afirmacoes enumeradas | **Ao resolver *"quem libera `QG-1`?"* pelas Cartas**, a resposta foi **`DEP-PRD`** — errada. A contagem deu **8** afirmacoes falsas, nao 4, e **`DEP-EXE` nao declara o portao em nenhuma linha** |
| **`RD-33`** | `DoR` de criacao de Spec (`FND-04 §6`) | O acervo estava **`GO-TO-SPECS`**, com **8 de 8** condicoes e nenhuma pendencia bloqueante | **Ao rodar o `DoR` contra a Spec que ainda nao existia**, o item *"Produto existe"* **falhou**, e falha em **tres** fontes vigentes. **Nenhuma Spec e criavel** |

**Um quarto achado nasceu de um metodo vizinho:** ao encontrar `aprovador: SOBERANO` divergente
em `TPL-spec`, extraiu-se o campo dos **19** templates — **19 de 19 declaram o mesmo valor**.
Corrigir **um** criaria defeito novo. Achado **`RD-34`**, e a extracao **barrou** a correcao.

## Causa

**Auditoria por leitura verifica se o artefato e coerente consigo mesmo, e instrumento
defeituoso pode ser perfeitamente coerente.**

| # | Causa | Onde apareceu |
|---|---|---|
| **1** | **O contador e uma afirmacao sobre o futuro.** *"Proximo numero disponivel: 0020"* nao contradiz nada no documento — contradiz a realidade **no instante em que alguem o usa** | `RD-32` |
| **2** | **A Carta descreve um mundo, e o mundo mudou fora dela.** Nenhuma frase de `DEP-PRD` e internamente incoerente; **todas eram verdadeiras quando escritas** | `RD-31` |
| **3** | **A pre-condicao ausente e invisivel enquanto ninguem tenta cumpri-la.** *"Produto existe"* estava escrito, vigente, e **nunca havia sido avaliado contra o disco** | `RD-33` |
| **4** | **Corrigir o valor nao corrige o gatilho.** [`governance/README`](../../governance/README.md) documenta, em nota propria, a correcao de um contador *"um numero atras do real desde a Missao 1.3"*, fechada como achado `C11` de REV-CONSOLIDACAO. **O mesmo defeito reapareceu em quatro contadores**, porque a correcao atingiu **o numero** e nao o **`CV-04`** | `RD-32`, **segunda ocorrencia** |

## Licao

**Ler um instrumento prova que ele esta escrito. Somente usa-lo prova que ele funciona.**

Auditoria documental e **verificacao de coerencia**; exercicio de instrumento e **verificacao de
eficacia**. Sao metodos distintos, medem coisas distintas, e **nenhum dos dois substitui o
outro** — a prova esta nas duas listas: sete achados que so a leitura encontrou, tres que so o
uso encontrou.

**Corolario, e ele e o mais caro:** correcao que atinge o **valor** e nao o **gatilho** garante
reincidencia. O contador foi corrigido uma vez, sem que `CV-04` fosse tornado obrigatorio na
criacao — e reincidiu em quatro lugares.

## Condicoes

**Aplica-se quando:**
- a missao **cria artefato de sequencia** — `ADR`, `RFC`, `FIT`, `INC`, `EXC`, `MSG`, `MEM`, `SPC`;
- a missao **resolve pergunta de autoridade** que tenha fonte fundacional **e** Carta;
- a missao **cria artefato com pre-condicao declarada** em `FND-04 §6`;
- a missao **encontra defeito em um membro de uma familia** de artefatos irmaos.

**NAO se aplica quando:**
- a verificacao e de **coerencia interna de projecao** — soma de coluna, ordinal, contagem de
  linha. Ali a leitura e o metodo, e foi ela que produziu `RD-20`, `RD-25` e `RD-28`;
- a verificacao e de **integridade criptografica** — `H-A`, `H-N`, `H-P`, impressao digital de
  acervo. Ali o instrumento **e** a medicao;
- **nao ha instrumento a exercer**, apenas conteudo declarativo a conferir.

## Acao

**Quatro verificacoes obrigatorias, com dono e gatilho. Executar todas as quatro sempre que uma
das condicoes acima for verdadeira.**

| # | Verificacao | Como se executa | Falha resulta em | Dono |
|---|---|---|---|---|
| **V1** | **Peca ao contador, nao o leia.** Antes de criar artefato de sequencia, obtenha o proximo numero **pelo contador oficial** e **teste se o arquivo com aquele nome ja existe** | Contador → nome de arquivo → teste de existencia | Achado de contador defasado; **corrija o contador na mesma mudanca** (`CV-04`, `IX-02`) | **DEP-GOV** |
| **V2** | **Resolva a pergunta de autoridade pelos dois caminhos, e compare.** Uma vez pela **fonte** (`FND-01`, `FND-04 §2`, `FND-09 §8.2`) e uma vez pelas **Cartas** | Duas resolucoes independentes da mesma celula | Divergencia = achado; instrumento **RFC + ADR + pacote + ato** | **DEP-EXE** *(propoe emenda de Carta)* |
| **V3** | **Rode o `DoR` contra o artefato que ainda nao existe.** Toda pre-condicao de `FND-04 §6` e avaliada **contra o disco**, nao contra a intencao | Item a item, com o comando que o mede | Pre-condicao insatisfeita = **`O1` bloqueada**. **Nao se cria mesmo assim** (`MT-01`, `AC-06`, `LV-11`) | **quem propoe o artefato** |
| **V4** | **Compare entre iguais antes de corrigir um.** Ao achar defeito em um membro de uma familia, **extraia o campo de todos os membros** | Extracao de frontmatter da familia inteira | Se **todos** divergem, corrigir **um** cria defeito novo — registre a familia, nao o membro | **DEP-GOV** |

**Regras que passam a codificar isto, para que a licao nao dependa de memoria:**

| Regra | Onde | O que obriga |
|---|---|---|
| **`SF-32`** | [ADR-0021 §5.10](../../decisions/ADR-0021-framework-de-specifications.md) | *"Criar Spec e incrementar o contador sao a mesma mudanca"* — codifica **`V1`** |
| **`SF-23`**, item 9 | [ADR-0021 §5.7](../../decisions/ADR-0021-framework-de-specifications.md) | O `DoR` inclui as pre-condicoes de `FND-04 §6`, inclusive *"Produto existe"* — codifica **`V3`** |

## Confianca

**alta**, e a fundamentacao esta em como os achados foram obtidos, nao em quantas vezes se
repetiram.

| Base | Valor |
|---|---|
| Ocorrencias desta licao | **1** — a Missao 1.13 |
| Achados que ela produziu | **4** — `RD-31`, `RD-32`, `RD-33`, `RD-34` |
| Achados **medidos por ferramenta**, nao inferidos | **4 de 4** |
| Contra-evidencia | **Nenhuma** — e a licao **declara os sete achados que a leitura encontrou e o uso nao encontraria**, em `## Condicoes` |
| Reincidencia comprovada de uma das causas | **`RD-32` e a segunda ocorrencia** do defeito de contador; a primeira esta documentada em nota de `governance/README` |

> **Confianca alta com uma ocorrencia exige justificativa, e esta e ela:** a licao **nao e
> estatistica, e mecanica**. Nao se afirma que exercer instrumentos *costuma* achar defeitos;
> afirma-se que **estes quatro defeitos existiam e eram inalcancaveis por leitura**, e isso e
> verificavel relendo os arquivos. **Promocao a EST exige `≥ 2` ocorrencias independentes**
> (FND-06 §5.2) — **nao pedida aqui**.

## Proveniencia

| Campo | Conteudo |
|---|---|
| **Origem** | [RFC-0017 §3.5](../../rfcs/RFC-0017-framework-de-specifications.md) · [ADR-0021 §9](../../decisions/ADR-0021-framework-de-specifications.md), caso **`T-12`** · [FIT-2026-015 §F6](../../governance/fitness/FIT-2026-015-framework-de-specifications.md) |
| Relatorio | [PT-2026-007](../../governance/relatorio-transicao-2026-07-29-specifications.md) |
| Portao | **QG-5** — nenhum trabalho encerra sem registro nesta camada |
| Metodo de obtencao | **Uso do instrumento**, com o resultado medido por ferramenta em 2026-07-29 |

## Relacionados

| Registro | Relacao |
|---|---|
| [MEM-APR-0005](MEM-APR-0005-medir-a-ausencia-na-fonte-errada.md) | **Vizinha, e a diferenca importa.** Aquela e sobre **onde** medir — buscar a **funcao**, nao o termo. Esta e sobre **como**: **usar em vez de ler.** As duas tratam de achado que a medicao errada produz ou esconde |
| [MEM-APR-0002](MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md) | *Detectar nao previne.* **Mesma estrutura de causa** que a causa **4** desta licao: o controle existia, e o que faltava era o **gatilho** |
| [MEM-APR-0004](MEM-APR-0004-projecao-revela-divergencia-antiga.md) | *Projetar por outro eixo revela divergencia antiga.* **Complementar:** ali o metodo novo e **projetar**; aqui e **exercer** |
| **Achados** | `RD-31` *(Alta)* · `RD-32` *(Media)* · `RD-33` *(Alta)* · `RD-34` *(Baixa)* — [catalogo §7](../../governance/artifact-registry.md) |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-KMS | Registro do aprendizado da Missao 1.13. **Tres achados nasceram de exercer instrumentos que quinze missoes de auditoria por leitura nao alcancaram:** **`RD-32`** ao **pedir** o proximo numero ao contador oficial — que devolveu um numero **que ja existia**, em **4** contadores e **8** valores, com risco de colisao de identificador; **`RD-31`** ao **resolver pelas Cartas** a pergunta *"quem libera `QG-1`"*, obtendo **`DEP-PRD`** onde `FND-01 §6.2` diz **`DEP-EXE`**, com **8** afirmacoes falsas e **0** ocorrencias do portao na Carta de quem o detem; **`RD-33`** ao **rodar o `DoR` contra o artefato que ainda nao existia**, encontrando que **tres** fontes vigentes exigem *"Produto existe"* e **nao existe produto**. Um quarto, **`RD-34`**, nasceu de **comparar entre iguais** — **19 de 19** templates com o mesmo valor divergente, o que **barrou** a correcao de um so. Fixa **`V1` a `V4`** com dono e gatilho, e registra as duas regras que passam a codifica-las: **`SF-32`** e **`SF-23`** item 9 de ADR-0021. **Declara os limites:** a auditoria por leitura encontrou **sete** achados que o uso nao encontraria, os dois metodos sao **complementares**, e **nenhum substitui o outro**. Registra a **segunda ocorrencia** do defeito de contador, cuja primeira correcao — documentada em nota de `governance/README` — **atingiu o valor e nao o gatilho `CV-04`**. **Confianca `alta` com uma unica ocorrencia, justificada:** a licao e **mecanica, nao estatistica**, e os quatro achados foram **medidos por ferramenta**. **Promocao a EST nao e pedida** — `FND-06 §5.2` exige duas ocorrencias independentes. |
