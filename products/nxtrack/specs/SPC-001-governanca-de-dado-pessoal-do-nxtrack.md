---
id: SPC-001-governanca-de-dado-pessoal-do-nxtrack
titulo: O que precisa ser verdadeiro sobre dado pessoal no nXtrack antes de qualquer exposicao a usuario externo
tipo: spec
versao: 1.0.0
status: ativo
camada_memoria: produto
autor: DEP-PRD
proprietario: DEP-PRD
aprovador: DEP-EXE
criado_em: 2026-08-02
atualizado_em: 2026-08-02
revisao_prevista: 2027-02-02
decisoes_relacionadas: [ADR-0031, ADR-0030, ADR-0021]
substitui: []
substituido_por: null
resumo: Fixa o que o nXtrack precisa provar sobre o dado pessoal que ja guarda — inventario, atribuicao, exclusao, informacao e limite de saida — antes de sair do loopback.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
classe_mudanca: C2
tipo_decisao: 2
capabilities: [CAP-juridico]
produto: PRO-nxtrack
criterios_aceite_count: 10
---

# SPC-001: Governanca de dado pessoal do nXtrack

> **Primeira `Spec` do LucaX Enterprise OS.** Ate 2026-08-02 o acervo tinha **`0`** artefatos de
> tipo `spec`, e as **32** regras `SF-01`–`SF-32` eram **determinadas, nao observadas** — limite
> `L1` de [`FND-11 §14`](../../../foundation/11-framework-specifications.md). Este documento e o
> primeiro exercicio delas. **O que o exercicio revelou sobre o proprio Framework nao esta aqui:
> esta em [`PT-2026-017 §6`](../../../governance/relatorio-transicao-2026-08-02-primeira-spec.md)**,
> porque `SF-02` proibe a `Spec` de ser explicacao de si mesma.

> **Esta `Spec` nao e parecer juridico e nao substitui advogado.** Ela declara **o que precisa
> existir** para que uma assessoria humana qualificada possa trabalhar, e **nao afirma
> enquadramento legal de nada** — `0` requisitos qualificam norma externa. A propria
> [`CAP-juridico`](../../../capabilities/CAP-juridico.md) inscreve essa fronteira no seu escopo:
> *"identificar quando o assunto exige assessoria humana qualificada"*.

---

## Bloco 2 · Proposito

Declarar **o que deve ser verdadeiro** sobre o dado pessoal que o nXtrack **ja guarda**, **sob
que condicao** isso e exigivel, e **por qual evidencia** cada exigencia sera aceita — fechando a
lacuna `LM-6(a)`, que o nono ato soberano fixou como materia da primeira `Spec` com prioridade
sobre as demais de `LA-7`.

Ela **nao** diz como construir nada (`SF-02`), **nao** decide (`SF-13`) e **nao** autoriza
exposicao (§ Bloco 14).

## Bloco 3 · Escopo

| Item | Definicao |
|---|---|
| **Produto** | [`PRO-nxtrack`](../carta.md) — `ativo` · `ratificada` |
| **Capability** | [`CAP-juridico`](../../../capabilities/CAP-juridico.md) — `ativo` · `experimental` · **uma so**, por `SF-07` |
| **Departamento custodiante** | **DEP-QAR** — custodio de `CAP-juridico` |
| **Inclui** | O dado pessoal **ja existente** no produto: `usuarios(nome, nome_norm, senha_hash, sal)`, o que a ele se vincula por `usuario_id`, e o **aprendizado coletivo** de `feedback_recomendacao`. Cinco eixos: **inventario**, **atribuicao ao titular**, **exclusao**, **informacao antes da coleta** e **limite de saida a terceiro** |
| **Nao inclui** | Ver **Bloco 14** — obrigatorio por `SF-08` |

## Bloco 4 · Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| Autor | **DEP-PRD** | `FND-09 §8.2`, linha `SPC` — *propoe/cria* |
| Revisores independentes | **DEP-ENG** + **DEP-QAR** | `FND-09 §8.2`, linha `SPC`; `AC-03` — revisor ≠ autor |
| Aprovador | **DEP-EXE**, com parecer de DEP-GOV | **derivado** — Bloco 5 |
| Ratificador | **—** | `C2 · Tipo 2` nao exige (`FND-04 §2.1`) |
| Libera `QG-1` | **DEP-EXE** | `FND-01 §6.2`; `ADR-0018` |
| Executor previsto | **DEP-ENG** *(construcao)* · **DEP-OPS** *(operacao)* | `PRO-nxtrack §Responsaveis` |
| Guardiao | **DEP-GOV** | `FND-04 §3` — valida classe e forma; **nao julga merito** |

## Bloco 5 · Autoridade — classe, tipo e aprovador **derivados**

> `SF-10`: a autoridade sobre uma `Spec` e **derivada, nunca declarada no artefato**. Abaixo esta
> a **derivacao**, nao a declaracao. **Fixar aprovador em texto foi o defeito de `RD-23`.**

| Variavel de `SF-10` | Valor apurado | Fonte |
|---|---|---|
| **(a) classe do efeito** | **`C2`** — elevada do piso `C1` por `FND-01 §7.1.6`, com duvida fundada: no `C1 · T2` de `SF-10`, *Proposta* e *Aprovacao* recaem no mesmo Departamento para o tipo `SPC`, e `FND-04 §3.1` declara **nula** a aprovacao com acumulo de papel (`LV-03`) | `ADR-0031 §6`; achado `RD-91` |
| **(b) reversibilidade** | **`Tipo 2`** — reversao medida em **6 arquivos**, `0` dependentes | `ADR-0031 §10` |
| **(c) materia** | **Escopo de produto** — `DEP-PRD` decide, `DEP-EXE` homologa. **Nao e** *"exposicao de dado vivo ao exterior"*, que segue **integralmente** do SOBERANO | `FND-01 §7.3` |
| **(d) Departamento custodiante** | **DEP-QAR** — custodio de `CAP-juridico` | `FND-02 §3`; `CAP-juridico` |
| **⇒ Aprovador derivado** | **DEP-EXE, com parecer de DEP-GOV** | `FND-04 §2`, linha `C2` |
| **⇒ Ratificacao** | **nao exigida** | `C2 · Tipo 2` |

**Conferencia de `FND-04 §3.1` — as quatro incompatibilidades absolutas:**

| Regra | Confronto | Resultado |
|---|---|---|
| `Proponente ≠ Aprovador` | DEP-PRD ≠ DEP-EXE | ✅ |
| `Proponente ≠ Revisor` | DEP-PRD ≠ DEP-ENG, DEP-QAR | ✅ |
| `Guardiao ≠ Proponente` | DEP-GOV ≠ DEP-PRD | ✅ |
| `Executor ≠ Verificador` | DEP-ENG/DEP-OPS ≠ DEP-QAR | ✅ |

## Bloco 6 · Custodiante

**DEP-QAR**, por ser custodio de `CAP-juridico` (`SF-07`; `FND-08 §6.1`).

> **Concentracao declarada, nao dissolvida — achado `RD-92`.** DEP-QAR e **custodiante da
> materia** e, por `FND-09 §8.2` linha `SPC`, **revisor do tipo**, na mesma mudanca. Os dois
> papeis **nao** constam de `FND-04 §3.1` como incompativeis, e por isso a aprovacao **nao** e
> nula. Mas a independencia e menor do que a tabela sugere, e isto fica **escrito**, com dono
> **DEP-GOV** e gatilho *"segunda `Spec` custodiada por DEP-QAR"*.

## Bloco 7 · Autores

**DEP-PRD.** `FND-09 §8.2`, linha `SPC` — *propoe/cria*. **Nao e escolha:** a matriz atribui a
autoria de `SPC` exclusivamente a DEP-PRD.

## Bloco 8 · Revisores

**DEP-ENG** *(merito tecnico e exequibilidade)* + **DEP-QAR** *(risco, evidencia e reversao)*.
`FND-09 §8.2`, linha `SPC`; `AC-03` — **revisor ≠ autor**, satisfeito.

## Bloco 9 · Aprovadores

**DEP-EXE**, com parecer de **DEP-GOV**. **Derivado no Bloco 5, nunca fixado aqui** (`SF-10`).

## Bloco 10 · Capability

[`CAP-juridico`](../../../capabilities/CAP-juridico.md) — **`status: ativo`**, dominio `GAR`,
classe `suporte`, maturidade `experimental`, custodio **DEP-QAR**. `VC-01` satisfeito: nao e
`proposta` nem `aposentada`. **Exatamente uma**, como `SF-07` exige.

> **Por que `CAP-juridico`, e nao uma das cinco da Carta.** A Carta de `PRO-nxtrack §8` declara,
> em texto proprio, que `CAP-juridico` **nao e consumida** pelo produto porque *"o produto **opera
> sob** politica dessas competencias, e operar sob uma competencia nao e consumi-la como
> Capability"*. **Esta `Spec` E essa politica sendo escrita** — logo ela **exerce** `CAP-juridico`,
> e o vinculo confirma a Carta em vez de contradize-la. As alternativas foram medidas e
> descartadas com fundamento: `CAP-dados` responde por *"confiar nos proprios numeros… integridade
> e linhagem"*, e a materia aqui e **norma externa**; `CAP-seguranca` responde por *"proteger o que
> a organizacao guarda e expoe"*, e alcanca `RQ-5` e `RQ-6` mas **nao** `RQ-1` a `RQ-4`.
> `CAP-juridico` e a **unica** cujo escopo declarado diz *"reconhecer obrigacao externa
> aplicavel"*.

## Bloco 11 · Departamento

**DEP-QAR** *(custodiante da materia)*. Departamentos alcancados: **DEP-ENG** *(constroi)*,
**DEP-OPS** *(opera)*, **DEP-PRD** *(prioriza)*, **DEP-EXE** *(homologa)*.

## Bloco 12 · Consumidores

> `SF-04`: `Spec` sem consumidor nomeado **e devolvida**. No corpo, nunca no frontmatter (`AC-01`).

| Consumidor | O que le aqui, e para agir como |
|---|---|
| **DEP-ENG** | `RQ-1` a `RQ-8` — o que precisa existir antes de construir. Hoje nao tem **contra o que** construir |
| **DEP-QAR** | Bloco 19 — o que verificar e o que reprovar. Hoje nao tem **contra o que** vetar |
| **DEP-OPS** | `RQ-5`, `RQ-7`, `RQ-8` — limite de exposicao, falha de exclusao e alcance dos backups |
| **SOBERANO** | O conjunto — **as condicoes que a decisao de expor dado vivo pressupoe** (`FND-01 §7.3`). Esta `Spec` **nao** toma essa decisao |
| **Assessoria juridica humana** *(quando houver)* | Bloco 18 — o levantamento factual pronto, para nao precisar refaze-lo |

---

## Bloco 13 · Requisitos

### 13.0 Fatos apurados — natureza `FATO` (`SF-13`)

> **Nao obrigam.** Existem porque `SF-12` exige `fonte` por identificador, e estes sao os
> identificadores. Todos medidos em 2026-08-02 sobre o `tree` `b9b36be9324ae2d36ddc4149049ebbff9f40fb4b`,
> **sem abrir banco algum**.

| # | Natureza | Enunciado | Onde se verifica |
|---|---|---|---|
| `F-1` | **FATO** | **`0` ocorrencias** de `LGPD`, `GDPR`, `ANPD`, *"dados pessoais"*, *"politica de privacidade"* e *"termos de uso"* — nos **183** arquivos rastreados **e** nos **262** da arvore de trabalho | Varredura com controle positivo *(`senha_hash` = 11)* aplicado antes |
| `F-2` | **FATO** | `usuarios` guarda **`nome`, `nome_norm`, `senha_hash`, `sal`**; `biblioteca_faixas` e `sessoes` referenciam `usuarios(id)` `ON DELETE CASCADE` | `prototipo/usuarios.py:37-70` |
| `F-3` | **FATO** | **`feedback_recomendacao` nao tem coluna de usuario.** `carregar_feedback` le sem clausula por usuario; `alternar` apaga e insere **globalmente**; a interface, porem, atribui ao titular — *"voce aprovou essa sequencia (seu feedback)"* | `prototipo/feedback.py:29-95`; `prototipo/recomendar.py:103` |
| `F-4` | **FATO** | **`0` caminhos de exclusao de conta** em codigo de producao. `DELETE FROM usuarios` tem **1** ocorrencia, **dentro de um teste** | `prototipo/tests/test_usuarios.py:393` |
| `F-5` | **FATO** | O produto **ja enuncia oito regras de privacidade** em uma frase, **sem criterio de aceite**: *"nao enviar audio completo sem autorizacao; criptografar dados em transito e sensiveis; permitir exclusao de conta/dados; informar quais dados sao usados pra treinamento; oferecer opt-out de treinamento; anonimizar feedback agregado; nao publicar bibliotecas/sets privados; respeitar direitos autorais…"* | `spec-tecnica-v1.md:777` (`§24`) |
| `F-6` | **FATO** | **O backup do banco carrega `senha_hash` e `sal` de todos os titulares**, e o proprio codigo o declara: *"o backup do banco (so do dono) carrega hash+sal de todo mundo — senha curta demais cai em forca bruta offline"* | `prototipo/usuarios.py:73-74` |
| `F-7` | **FATO** | A exposicao esta contida por **configuracao**, nao por norma: `"127.0.0.1:8501:8501"` | `compose.beta.yml:13` |
| `F-8` | **FATO** | O repositorio declara **24** tabelas | Contagem de `CREATE TABLE` sobre a lista fechada dos 183 rastreados |
| `H-1` | **HIPOTESE** *(entra marcada — `SF-13`)* | Satisfazer `RQ-1` a `RQ-8` **basta** para uma assessoria juridica humana concluir a analise de `LM-6(a)` **sem novo levantamento factual** | **Teste que a confirmaria:** submeter o conjunto a assessoria qualificada e medir quantos itens de levantamento adicional ela pede. **`0` pedidos ⇒ confirmada.** **Nao validada; nao apagada se invalidada** (`P-11`, `MM-09`) |

### 13.1 Requisitos — os seis campos de `SF-12`, sem excecao

> **Verbos** (`SF-11`): `MUST` = deve · `SHOULD` = deveria · `MAY` = pode · `MUST NOT` = nao deve.
> **Perfis** (`SF-17`): FUNCIONAL · INTERFACE · DADOS · QUALIDADE · SEGURANCA · OPERACAO · AVALIACAO.
> **Metodos** (`SF-14`): INSPECAO · DEMONSTRACAO · TESTE · ANALISE · MEDICAO.
> Todo criterio abaixo e **verificavel por terceiro sem consultar o autor**.

> **Distribuicao de verbos, declarada e nao acidental: `8` `MUST` · `2` `MUST NOT` · `0` `SHOULD`
> · `0` `MAY`.** Nenhum requisito entrou como *"deveria"*: cada um dos dez **reprova a entrega**
> se descumprido (`SF-11`). Isso **nao** e rigor decorativo — e consequencia de `RQ-5`, que
> condiciona a exposicao ao conjunto: um `SHOULD` dentro desse conjunto tornaria a condicao
> inverificavel. **Se algum destes devesse ser `SHOULD`, a correcao e emenda MENOR** (`SF-27`),
> e o motivo do rebaixamento fica registrado (`SF-11`).

---

#### `RQ-1` — Inventario de dado pessoal

| Campo | Conteudo |
|---|---|
| **Natureza · Verbo · Perfil** | REQUISITO · **MUST** · **DADOS** |
| **Requisito** | O produto **deve** manter, em documento versionado no seu proprio repositorio, o inventario de onde ha dado pessoal: para **cada** tabela declarada, se contem dado pessoal *(sim/nao)* e, quando sim, **quais colunas** |
| **Motivo** | `LM-2` registra o dado pessoal como *"presente por desenho, **NAO quantificado**"*. Sem inventario, nenhuma das exigencias seguintes tem **alcance definido** — nao se exclui, nem se informa, o que nao se sabe onde esta |
| **Fonte** | `F-2`, `F-8`; `LM-2` de `PT-2026-014 §4`; `FG-11` de `PT-2026-014 §3.2` |
| **Criterio de aceite** | Existe um documento no repositorio do produto cujo numero de tabelas listadas **iguala** o numero de tabelas que o repositorio declara, e cada linha traz a marcacao *sim/nao* e, se *sim*, a lista de colunas |
| **Metodo** | **INSPECAO** |
| **Evidencia esperada** | O documento, mais a contagem de `CREATE TABLE` sobre a mesma lista fechada de arquivos. **Quem produz:** DEP-ENG. **Quando:** antes de `RQ-2` |

---

#### `RQ-2` — Atribuicao ao titular

| Campo | Conteudo |
|---|---|
| **Natureza · Verbo · Perfil** | REQUISITO · **MUST** · **DADOS** |
| **Requisito** | Dado o identificador de um titular, o produto **deve** permitir determinar **o conjunto completo** de registros originados por ele, em **todas** as tabelas que `RQ-1` marcar com dado pessoal |
| **Motivo** | `F-3`: hoje a contribuicao ao aprendizado coletivo **nao e atribuivel** — a tabela nao tem coluna de usuario —, enquanto a interface diz ao titular que o feedback e **dele**. `RQ-3` e impossivel sem isto |
| **Fonte** | `F-3`; `R2` da Carta de `PRO-nxtrack §11` *(severidade **Alta**)* |
| **Criterio de aceite** | Para uma conta de teste com atividade conhecida, o procedimento devolve um conjunto, e um terceiro consegue conferir que **nenhum** registro conhecido daquela conta ficou de fora e **nenhum** de outra conta entrou |
| **Metodo** | **DEMONSTRACAO** |
| **Evidencia esperada** | Registro da execucao com a conta de teste, o conjunto devolvido e a conferencia dos dois sentidos. **Quem produz:** DEP-ENG. **Verifica:** DEP-QAR |

> **`RQ-2` nao diz como.** Acrescentar coluna, manter tabela de vinculo, derivar por chave — **e
> escolha de DEP-ENG**, e `SF-02` proibe esta `Spec` de decidi-la.

---

#### `RQ-3` — Caminho de exclusao

| Campo | Conteudo |
|---|---|
| **Natureza · Verbo · Perfil** | REQUISITO · **MUST** · **FUNCIONAL** |
| **Requisito** | O produto **deve** oferecer ao titular um caminho pelo qual ele obtenha a exclusao da propria conta e dos registros que `RQ-2` identifica |
| **Motivo** | `F-4`: **`0`** caminhos existem, e `F-5` mostra que o proprio produto **ja se obrigou** a *"permitir exclusao de conta/dados"* — a regra esta escrita e nao esta implementada |
| **Fonte** | `F-4`, `F-5` *(`spec-tecnica-v1.md §24`)* |
| **Criterio de aceite** | Exercido o caminho sobre uma conta de teste, a consulta de `RQ-2` sobre o mesmo identificador devolve **conjunto vazio**, e a conta deixa de autenticar |
| **Metodo** | **TESTE** |
| **Evidencia esperada** | Procedimento repetivel com resultado registrado: estado antes, execucao, estado depois. **Quem produz:** DEP-ENG. **Verifica:** DEP-QAR |

---

#### `RQ-4` — Informacao antes da coleta

| Campo | Conteudo |
|---|---|
| **Natureza · Verbo · Perfil** | REQUISITO · **MUST** · **INTERFACE** |
| **Requisito** | Antes de concluir a criacao de conta, o produto **deve** apresentar ao titular um texto que declare, no minimo: **(i)** que dados guarda sobre ele; **(ii)** que a reacao dele a recomendacoes **alimenta a recomendacao de outros titulares**; **(iii)** como pedir a exclusao de `RQ-3` |
| **Motivo** | `F-1`: **`0`** ocorrencias de *"termos de uso"* e *"politica de privacidade"*, e o cadastro **e publico** (`POST /sessao/criar`, `LM-5`). O item **(ii)** existe porque `F-3` mede um comportamento que **o titular nao tem como supor** |
| **Fonte** | `F-1`, `F-3`; `LM-5` de `PT-2026-014 §4`; `F-5` *(*"informar quais dados sao usados pra treinamento"*)* |
| **Criterio de aceite** | O fluxo de criacao de conta **nao conclui** sem que o texto tenha sido apresentado, e o texto contem os tres itens — cada um localizavel por um terceiro que leia a tela ou a resposta da interface |
| **Metodo** | **DEMONSTRACAO** |
| **Evidencia esperada** | Registro do fluxo exercido, com o texto apresentado e a marcacao dos tres itens. **Quem produz:** DEP-ENG. **Verifica:** DEP-QAR |

> **`RQ-4` nao exige *"politica de privacidade"* nem *"termos de uso"* como instrumentos.** Exige
> **informacao verificavel**. Nomear e qualificar instrumento juridico e materia de assessoria
> humana — Bloco 14, `EX-2`.

---

#### `RQ-5` — Limite de exposicao *(negativo)*

| Campo | Conteudo |
|---|---|
| **Natureza · Verbo · Perfil** | REQUISITO · **MUST NOT** · **SEGURANCA** |
| **Requisito** | Enquanto `RQ-1` a `RQ-4` nao estiverem satisfeitos **e verificados por `RQ-9`**, o produto **nao deve** ser acessivel de fora do `loopback` |
| **Motivo** | `F-7`: a contencao de hoje e **configuracao**, revertivel por **uma linha** de `compose.beta.yml`, e nao norma. `R2` da Carta *(Alta)* so esta contido por esse acaso |
| **Fonte** | `F-7`; `LM-5`; `R2` e `R6` da Carta de `PRO-nxtrack §11` |
| **Criterio de aceite** | Com o estado de `RQ-1`–`RQ-4` registrado como *nao satisfeito*, a medicao do endereco em que o servico escuta devolve **endereco de `loopback`** |
| **Metodo** | **MEDICAO** *(valor, instrumento e data)* |
| **Evidencia esperada** | Valor medido do bind, instrumento usado e data. **Quem produz:** DEP-OPS. **Verifica:** DEP-QAR |

> **`RQ-5` restringe; nunca autoriza.** Satisfazer esta `Spec` **nao** autoriza expor — Bloco 14,
> `EX-1`. A decisao de expor dado vivo ao exterior e do **SOBERANO** (`FND-01 §7.3`), e uma
> decisao dele **prevalece sobre este requisito**, que entao registra **nao conformidade**, nao
> veto.

---

#### `RQ-6` — Limite de saida a terceiro *(negativo)*

| Campo | Conteudo |
|---|---|
| **Natureza · Verbo · Perfil** | REQUISITO · **MUST NOT** · **SEGURANCA** |
| **Requisito** | O produto **nao deve** enviar dado pessoal de titular a servico externo sem autorizacao explicita **para aquele envio** |
| **Motivo** | `LV-08` e **Linha Vermelha** de `FND-01`, e o produto consome **11** integracoes externas medidas. Hoje **nao ha declaracao escrita** de quais campos trafegam em cada uma |
| **Fonte** | `LV-08` de `FND-01 §8`; `LM-4` de `PT-2026-014 §4`; `PRO-nxtrack §9` |
| **Criterio de aceite** | Existe, para **cada** integracao externa que o produto declara, a lista dos campos que trafegam; e **nenhuma** que trafegue campo marcado como dado pessoal em `RQ-1` opera sem autorizacao explicita registrada para aquele envio |
| **Metodo** | **ANALISE** *(derivacao sobre o inventario de `RQ-1` e a lista de integracoes)* |
| **Evidencia esperada** | Tabela integracao × campos, cruzada com o inventario de `RQ-1`, mais os registros de autorizacao. **Quem produz:** DEP-ENG. **Verifica:** DEP-QAR |

---

#### `RQ-7` — Exclusao parcial *(de falha)*

| Campo | Conteudo |
|---|---|
| **Natureza · Verbo · Perfil** | REQUISITO · **MUST** · **OPERACAO** |
| **Requisito** | Quando a exclusao de `RQ-3` **nao** remover tudo, o produto **deve** registrar o que foi removido e o que **nao** foi, e informar o titular de que a exclusao ficou incompleta |
| **Motivo** | `SF-25` exige requisito **de falha**, e este caminho **tem** falha previsivel: `F-6` mostra que **backups carregam `senha_hash` e `sal` de todos**, e backup nao se apaga por `CASCADE`. Exclusao silenciosamente parcial e pior que exclusao recusada |
| **Fonte** | `F-6`; `SF-25` |
| **Criterio de aceite** | Forcada uma condicao em que ao menos um destino nao pode ser removido, o registro produzido lista **removidos** e **nao removidos**, e a informacao ao titular declara a incompletude |
| **Metodo** | **TESTE** |
| **Evidencia esperada** | Procedimento repetivel com a condicao forcada e o registro resultante. **Quem produz:** DEP-ENG. **Verifica:** DEP-QAR |

---

#### `RQ-8` — Alcance dos backups

| Campo | Conteudo |
|---|---|
| **Natureza · Verbo · Perfil** | REQUISITO · **MUST** · **OPERACAO** |
| **Requisito** | O produto **deve** declarar por escrito **quantas** copias retem dado pessoal, **por quanto tempo**, e **se** a exclusao de `RQ-3` as alcanca; nao alcancando, o limite **deve** estar declarado com o numero |
| **Motivo** | `F-6`, medido no proprio codigo do candidato. As **11** ocorrencias de *"retencao"* no repositorio sao **todas** de retencao de backup — **`0`** falam de titular |
| **Fonte** | `F-6`; varredura de retencao do Item 0, §4 |
| **Criterio de aceite** | Existe declaracao escrita com os tres valores — numero de copias, prazo e alcance da exclusao —, e o numero de copias confere com o que a ferramenta de backup do produto reporta |
| **Metodo** | **INSPECAO** |
| **Evidencia esperada** | A declaracao, mais a saida da ferramenta de backup na mesma data. **Quem produz:** DEP-OPS. **Verifica:** DEP-QAR |

---

#### `RQ-9` — Verificacao independente antes de mudar a exposicao

| Campo | Conteudo |
|---|---|
| **Natureza · Verbo · Perfil** | REQUISITO · **MUST** · **AVALIACAO** |
| **Requisito** | O estado *satisfeito* de `RQ-1` a `RQ-8` **deve** ser verificado por quem **nao** os implementou, e o registro dessa verificacao **deve** anteceder qualquer mudanca no endereco em que o servico escuta |
| **Motivo** | `ADR-0005` proibe autoverificacao e `LV-03` a torna nula. Sem este requisito, `RQ-5` seria auto-atestado por quem tem interesse em publicar |
| **Fonte** | `ADR-0005`; `LV-03` de `FND-01 §8`; `AC-03` |
| **Criterio de aceite** | Existe registro de verificacao **datado**, cujo executor e distinto do produtor de cada requisito verificado, e cuja data **antecede** a do primeiro registro de mudanca do bind |
| **Metodo** | **INSPECAO** |
| **Evidencia esperada** | O registro de verificacao, com executor, data e resultado por requisito. **Quem produz:** DEP-QAR. **Verifica:** DEP-GOV *(forma)* |

---

#### `RQ-10` — Cobertura do inventario *(nao funcional, com numero, instrumento e data)*

| Campo | Conteudo |
|---|---|
| **Natureza · Verbo · Perfil** | REQUISITO · **MUST** · **QUALIDADE** |
| **Requisito** | O inventario de `RQ-1` **deve** cobrir **100%** das tabelas que o repositorio declara — **`0`** tabelas sem linha no inventario |
| **Motivo** | `SF-25` exige requisito **nao funcional com numero**, e cobertura parcial de inventario e o modo classico de a exclusao falhar sem ninguem notar. `CE-04` proibe estimar |
| **Fonte** | `F-8`; `SF-25`; `CE-04` |
| **Criterio de aceite** | `tabelas_no_inventario` ÷ `tabelas_declaradas_no_repositorio` = **1,00** |
| **Metodo** | **MEDICAO** — **valor medido hoje: `24` tabelas declaradas** · **instrumento:** contagem de `CREATE TABLE` sobre a lista fechada dos arquivos rastreados sob o `tree` ancorado · **data: 2026-08-02** |
| **Evidencia esperada** | As duas contagens e a razao entre elas, com a data e o `tree` medido. **Quem produz:** DEP-ENG. **Verifica:** DEP-QAR |

> **O valor `24` e o de hoje, nao um teto.** O criterio e a **razao**, nao o numero: se o
> repositorio passar a declarar 30 tabelas, o inventario precisa de 30 linhas.

### 13.2 Cobertura das quatro categorias (`SF-25`)

| Categoria | Requisitos | Se ausente, o motivo |
|---|---|---|
| **Funcional** | `RQ-1`, `RQ-2`, `RQ-3`, `RQ-4` | — presente |
| **Nao funcional** *(com numero, instrumento e data)* | **`RQ-10`** — `100%`, contagem de `CREATE TABLE`, 2026-08-02 | — presente |
| **Negativo** — o que **nao** deve ocorrer | **`RQ-5`**, **`RQ-6`** | — presente |
| **De falha** — o que ocorre quando o caminho feliz falha | **`RQ-7`** | — presente |

**Quatro de quatro.** Nenhuma ausencia a declarar.

### 13.3 Cobertura dos sete perfis (`SF-17`)

| Perfil | Requisitos | Ausencia declarada |
|---|---|---|
| FUNCIONAL | `RQ-3` | — |
| INTERFACE | `RQ-4` | — |
| DADOS | `RQ-1`, `RQ-2` | — |
| QUALIDADE | `RQ-10` | — |
| SEGURANCA | `RQ-5`, `RQ-6` | — |
| OPERACAO | `RQ-7`, `RQ-8` | — |
| AVALIACAO | `RQ-9` | — |

**Sete de sete, e isso nao cria entidade nem tipo documental** (`SF-18`). **Nao se especializa
perfil algum** (`SF-19`): faltam os **dois sinais observados** de `FND-10 §9.2`, e a decisao de
**nao** especializar fica registrada aqui, como `FND-04 §6.2` manda.

---

## Bloco 14 · Exclusoes — **obrigatorio** (`SF-08`)

> Cada exclusao declara **por que fica de fora** e **sob qual condicao poderia entrar**.

| # | Item | Por que fica de fora | Quando poderia entrar |
|---|---|---|---|
| `EX-1` | **A decisao de expor o produto a usuario externo** | E do **SOBERANO** (`FND-01 §7.3`, *"exposicao de dado vivo ao exterior"*). `SF-03` proibe a `Spec` de criar autoridade. **Satisfazer esta `Spec` NAO autoriza publicar**, e `RQ-5` **restringe** sem nunca permitir | Nunca por `Spec`. So por decisao do SOBERANO |
| `EX-2` | **`LM-6(b)` — direito autoral de catalogo musical** | **Declarado fora por determinacao expressa da missao**, e coerente com `DC-3` do nono ato, que fixou **`(a)`** como a materia da primeira `Spec`. `LM-6(b)` tem objeto distinto — obra de terceiro, nao titular de dado pessoal —, custodia distinta e **`0`** interseccao com `RQ-1`–`RQ-10` | Em `Spec` propria de `PRO-nxtrack`, quando `LM-6(a)` estiver satisfeito ou quando o SOBERANO reordenar `LA-7` |
| `EX-3` | **Enquadramento legal** — dizer **qual** norma se aplica, se se aplica, e o que ela exige | Exige **assessoria humana qualificada**, e a propria `CAP-juridico` inscreve essa fronteira no escopo. Afirmar enquadramento aqui seria `LV-12` — fabricar fonte | Quando houver parecer humano no acervo. **Esta `Spec` produz o levantamento factual que esse parecer consumiria** (`H-1`) |
| `EX-4` | **A implementacao de qualquer requisito** | `SF-02`: `Spec` que detalhe implementacao **e devolvida**. `RQ-2` diz *que* a atribuicao deve ser possivel, e **nao** se por coluna, tabela de vinculo ou derivacao | Nunca em `Spec`. Vive em decisao de DEP-ENG e no codigo |
| `EX-5` | **`RD-71`** *(custodia difusa do repositorio)* e **`RD-74`** *(`VC-03`, cinco Capabilities)* | `LA-7` remete os tres a primeira `Spec`, e o ato **fixou a ordem**: `LM-6(a)` **primeiro**. Tratar os tres aqui inverteria a determinacao soberana | Em `Spec` propria, apos esta. **Seguem abertos, com dono e gatilho** |
| `EX-6` | **Quantos titulares o nXtrack tem** | Exigiria **abrir `nxtrack.db`**, proibido pela missao. **Ausencia de medicao nao e medicao de ausencia** (`PI-10`) | Quando houver missao com autorizacao expressa para abrir dado vivo, e backup datado (`PI-07`, `LV-01`) |
| `EX-7` | **Politica de dado pessoal valida para todo o acervo** | E materia **nao-produto**, e a categoria **nao existe**: `RD-88`, e so `S2` a cria — **DEFERIDA** por decisao do SOBERANO | Se e quando `S2` for exercida |

---

## Bloco 15 · Interfaces

| Tipo | Contraparte | Relacao (`SF-21`) | Dono | Estado |
|---|---|---|---|---|
| Produto | [`PRO-nxtrack`](../carta.md) | **`refina`** *(`R-04 depende-de`)* — detalha `R2` de `§11` **sem contradizer** | DEP-PRD | `ativo` · `ratificada` |
| Decisao | [`ADR-0031`](../../../decisions/ADR-0031-primeira-spec-governanca-de-dado-pessoal-do-nxtrack.md) | **`implementa`** — esta `Spec` satisfaz o que o `ADR` decidiu criar | DEP-PRD | `ativo` |
| Parecer | [`FIT-2026-024`](../../../governance/fitness/FIT-2026-024-primeira-spec.md) | **`verifica`** *(`R-06`)* — a evidencia decide o aceite | DEP-QAR | `ativo` |
| Norma | [`FND-11`](../../../foundation/11-framework-specifications.md) | **`restringe`** — **ato de autoridade, nao aresta** (`FND-10 §7.1`) | DEP-GOV | `ativo` |

**`conflita`: `0`.** Nao ha segunda `Spec` no acervo, logo nao ha conflito possivel — e `SF-22`
determina que conflito **nao entra no grafo**: seria achado, com severidade, dono e gatilho.

## Bloco 16 · Dependencias

| Dependencia | Estado | `LN-03` — pode? |
|---|---|---|
| `PRO-nxtrack` | `ativo` | ✅ nao e `superado`, `revogado` nem `depreciado` |
| `CAP-juridico` | `ativo` | ✅ |
| `ADR-0031` | `ativo` | ✅ |
| `ADR-0030` | `ativo` · `ratificada` | ✅ |
| `FND-11`, `FND-04`, `FND-09`, `FND-10`, `FND-01`, `FND-03` | `ativo` | ✅ |

**`0` dependencias transitivas declaradas no frontmatter** — proibido por `AC-01` e `SF-06`.

## Bloco 17 · Riscos

| # | Risco | Prob. | Impacto | Mitigacao | **Sinal observado** (`LM-01` — risco sem sinal e devolvido) |
|---|---|---|---|---|---|
| `RS-1` | **Os requisitos serem lidos como autorizacao para publicar** | Media | **Alto** | `EX-1` e a nota de `RQ-5`, ambas em texto expresso | **Observado:** o proprio despacho da missao precisou dizer *"a Spec define o que precisa existir, nao substitui advogado"* — o risco de leitura ampliada ja se manifestou **antes** da `Spec` existir |
| `RS-2` | **`RQ-2` ser satisfeito so no papel** — atribuicao que nao alcanca o aprendizado coletivo | Media | **Alto** | Criterio de `RQ-2` exige conferencia **nos dois sentidos**, e `RQ-3` so aceita **conjunto vazio** | **Observado:** `F-3` — a interface **ja** diz *"seu feedback"* sobre dado que **nao** e atribuivel. A afirmacao falsa **existe hoje** |
| `RS-3` | **A exclusao nao alcancar backups** e ninguem notar | **Alta** | Medio | `RQ-7` *(falha declarada)* e `RQ-8` *(alcance escrito com numero)* | **Observado:** `F-6` — o codigo declara, de propria mao, que o backup carrega `hash`+`sal` de todos |
| `RS-4` | **Esta `Spec` estar errada** — exigir o que nao importa e omitir o que importa | Media | Medio | `H-1` e **hipotese marcada**, com teste declarado: assessoria humana pedir **`0`** levantamentos adicionais | **Observado:** `LM-6(a)` foi medido por varredura de **termos**, e a varredura estendida achou `§24` — **prova de que medir termo nao mede materia** |
| `RS-5` | **`RQ-5` ser esvaziado por decisao superior** | Baixa | Baixo | Declarado como funcionamento **correto**: decisao do SOBERANO prevalece e o efeito e **registro de nao conformidade**, nunca veto | **Observado:** `FND-01 §7.3` ja atribui a materia ao SOBERANO — a precedencia **e anterior** a esta `Spec` |

## Bloco 18 · Evidencias

> `SF-15`: evidencia esperada e declarada **antes**, nunca escolhida depois. Indicador sem valor
> medido declara-se `definido, sem valor` (`LM-01`, `CE-04`). **Fabricar evidencia e `LV-12`.**

| # | Evidencia | Estado hoje | Quem produz | Quando |
|---|---|---|---|---|
| `EV-1` | Varredura dos **6** termos de `LM-6(a)` com **controle positivo** | ✅ **produzida** — `0` em 183 e em 262 arquivos, 2026-08-02 | DEP-PRD | ja |
| `EV-2` | Schema de `usuarios`, `sessoes`, `biblioteca_faixas`, `feedback_recomendacao` | ✅ **produzida** — lido em codigo rastreado, `0` bancos abertos | DEP-PRD | ja |
| `EV-3` | Inventario de dado pessoal *(`RQ-1`)* | **definido, sem valor** | DEP-ENG | antes de `RQ-2` |
| `EV-4` | Demonstracao de atribuicao *(`RQ-2`)* | **definido, sem valor** | DEP-ENG | apos `RQ-1` |
| `EV-5` | Teste de exclusao *(`RQ-3`, `RQ-7`)* | **definido, sem valor** | DEP-ENG | apos `RQ-2` |
| `EV-6` | Fluxo de criacao de conta com o texto *(`RQ-4`)* | **definido, sem valor** | DEP-ENG | independente |
| `EV-7` | Medicao do bind *(`RQ-5`)* | ✅ **valor de hoje: `loopback`** — `compose.beta.yml:13`, 2026-08-02 | DEP-OPS | continuo |
| `EV-8` | Tabela integracao × campos *(`RQ-6`)* | **definido, sem valor** | DEP-ENG | apos `RQ-1` |
| `EV-9` | Declaracao de copias e prazo *(`RQ-8`)* | **definido, sem valor** | DEP-OPS | independente |
| `EV-10` | Registro de verificacao independente *(`RQ-9`)* | **definido, sem valor** | DEP-QAR | apos `RQ-1`–`RQ-8` |
| `EV-11` | Contagem de tabelas *(`RQ-10`)* | ✅ **valor de hoje: `24`**, 2026-08-02 | DEP-PRD | ja |

**`3` evidencias produzidas · `8` definidas sem valor.** Nenhuma inventada.

## Bloco 19 · Verificacao

| `RQ` | Metodo (`SF-14`) | Quem verifica | Quando | Evidencia registrada onde |
|---|---|---|---|---|
| `RQ-1` | INSPECAO | DEP-QAR | antes de `RQ-2` | Repositorio do produto |
| `RQ-2` | DEMONSTRACAO | DEP-QAR | apos `RQ-1` | Registro da execucao |
| `RQ-3` | TESTE | DEP-QAR | apos `RQ-2` | Procedimento repetivel |
| `RQ-4` | DEMONSTRACAO | DEP-QAR | independente | Registro do fluxo |
| `RQ-5` | MEDICAO | DEP-QAR | continuo | Valor do bind, com data |
| `RQ-6` | ANALISE | DEP-QAR | apos `RQ-1` | Tabela cruzada |
| `RQ-7` | TESTE | DEP-QAR | apos `RQ-3` | Registro da falha forcada |
| `RQ-8` | INSPECAO | DEP-QAR | independente | Declaracao escrita |
| `RQ-9` | INSPECAO | **DEP-GOV** *(forma)* | antes de mudar o bind | Registro de verificacao |
| `RQ-10` | MEDICAO | DEP-QAR | junto de `RQ-1` | As duas contagens e a razao |

**`10` de `10` com metodo entre os cinco de `SF-14`.** Nenhum criterio depende de consultar o autor.

## Bloco 20 · Vigencia

| Campo | Conteudo |
|---|---|
| **Classe · Tipo** | **`C2 · Tipo 2`** — derivado no Bloco 5 |
| **`QG-1` liberado por** | **DEP-EXE**, 2026-08-02 — `FND-01 §6.2`; `ADR-0018`. *Liberar o portao nao e aprovar o artefato* |
| **Aprovacao — quem e quando** | **DEP-EXE**, com parecer de **DEP-GOV**, 2026-08-02 |
| **Ratificacao** | **Nao exigida** — `C2 · Tipo 2` (`FND-04 §2.1`; `LM-02` alcanca `C3` e `Tipo 1`) |
| **Registro / promulgacao** | **DEP-GOV** — e o registro **precede** a execucao (`CV-02`). Entrada no [catalogo mestre](../../../governance/artifact-registry.md) na **mesma mudanca** (`SF-32`, `CV-04`, `IX-02`) |
| **Vigencia** | **2026-08-02**, `status: ativo` |
| **Gatilho de revisao** | *(a)* primeiro requisito **satisfeito e verificado**; *(b)* qualquer mudanca no bind do servico; *(c)* invalidacao de `H-1`; *(d)* `2027-02-02`, o que vier primeiro |
| **Sucessao prevista** | Nenhuma. `substitui: []`, `substituido_por: null` |

## Bloco 21 · Contexto e evolucao (`SF-27` a `SF-31`)

| Campo | Valor |
|---|---|
| **Classe de mutabilidade** | **`M2`** — versionavel, texto anterior preservado (`FND-10 §6.2`; `SF-27`) |
| **Regra de versao** | **MAIOR** se um `MUST` for criado, removido ou tiver o criterio alterado · **MENOR** se `SHOULD`/`MAY` mudar ou se entrar requisito sem mexer em `MUST` · **CORRECAO** se nada normativo mudar (`SF-27`) |
| **Alteracao silenciosa** | **Nula** (`SF-28`). Nenhum requisito muda de sentido sem incremento de versao e linha de historico |
| **Heranca implicita** | **Proibida** (`SF-28`). Nenhuma `Spec` futura herda `RQ-nn` daqui por proximidade ou por estar no mesmo produto — so por **relacao declarada** e **citacao por `ID`** |
| **Retorno a `rascunho`** | **Impossivel** apos `ativo` (`SF-30`, `RB-02`). Corrige-se **superando** (`O6`) ou **retirando** (`O9`), declarando o que passa a valer |
| **Resumo operacional** | *(o `resumo` do frontmatter — **1 linha, 168 caracteres**, voz ativa, diz o que a `Spec` faz)* |
| **Gatilho de ativacao** | *"Vou construir, operar, verificar ou decidir algo que toca dado de titular do nXtrack"* — no catalogo mestre (`FND-10 §8.3`) |
| **Pacote minimo** | **Esta `Spec` + [`PRO-nxtrack`](../carta.md).** Nada mais. `ADR-0031` so e necessario para discutir **a classe**, nunca para consumir um requisito |
| **Secoes sob demanda** | `perfil_contexto: sob-demanda`. Blocos **rotulados e independentes** (`FND-10 §10.3`) |
| **Custo medido** | **`603` linhas**, por `wc -l`, em **2026-08-02**. **Primeira `Spec` do acervo: nao ha mediana do tipo**, logo `CE-05` **nao pode disparar** — o teste do dobro da mediana e **inaplicavel por ausencia de populacao**, e isso fica declarado, nao presumido satisfeito |
| **Requisito enderecavel** | **`SPC-001 RQ-nn`** carrega o **bloco daquele requisito**, nunca o documento (`SF-31`, `CE-01`, `PC-01`) |

---

## Bloco 1 · Identidade — conferencia do contrato (`SF-05`, `SF-06`)

| Grupo | Campos | Presentes |
|---|---|---|
| **Nucleo universal — `FND-03 §4`** | `id` `titulo` `tipo` `versao` `status` `camada_memoria` `autor` `proprietario` `aprovador` `criado_em` `atualizado_em` `revisao_prevista` `decisoes_relacionadas` `substitui` `substituido_por` | **15 de 15** |
| **Extensao — `FND-10 §2.2`** | `resumo` `perfil_contexto` `confidencialidade` `revisor` `ratificacao` | **5 de 5** |
| **Condicionais — `SF-06`** | `produto` `criterios_aceite_count` `classe_mudanca` `tipo_decisao` `capabilities` | **5 de 5**, todos do esqueleto de `TPL-spec` **1.1.0** |
| **Campos novos criados** | — | **`0`** (`AC-07`, `SF-05`) |
| **Consumidor, relacao, autoridade, custo de contexto, dependencia transitiva no frontmatter** | — | **`0`** — proibidos por `AC-01` e `SF-06`; todos vivem **no corpo** |

**Os 21 blocos de `SF-09`, um a um:** 1 Identidade *(aqui)* · 2 Proposito · 3 Escopo · 4
Responsaveis · 5 Autoridade · 6 Custodiante · 7 Autores · 8 Revisores · 9 Aprovadores · 10
Capability · 11 Departamento · 12 Consumidores · 13 Requisitos · 14 Exclusoes · 15 Interfaces ·
16 Dependencias · 17 Riscos · 18 Evidencias · 19 Verificacao · 20 Vigencia · 21 Contexto e
evolucao. **21 de 21 presentes.**

## Rastreabilidade — a cadeia de nove elos (`SF-20`)

```
objetivo -> Capability -> Departamento -> decisao -> Spec -> requisito -> aceite -> evidencia -> resultado
```

| Elo | Valor | Percorrivel sem consultar pessoa? |
|---|---|---|
| **Objetivo** | Missao **1.13.5** do [roadmap canonico](../../../governance/roadmap-canonico.md) — *"primeira Spec real"*, alvo `LM-6(a)` | ✅ |
| **Capability** | [`CAP-juridico`](../../../capabilities/CAP-juridico.md) — `ativo` | ✅ |
| **Departamento** | **DEP-QAR** *(custodiante)*; DEP-PRD *(autor)* | ✅ |
| **Decisao** | [`ADR-0031`](../../../decisions/ADR-0031-primeira-spec-governanca-de-dado-pessoal-do-nxtrack.md) ← [`RFC-0026`](../../../rfcs/RFC-0026-primeira-spec-governanca-de-dado-pessoal-do-nxtrack.md) | ✅ |
| **Spec** | **`SPC-001`** — este documento | ✅ |
| **Requisitos** | `RQ-1` … `RQ-10` | ✅ |
| **Aceite** | Bloco 13.1, campo *Criterio de aceite* de cada `RQ` | ✅ |
| **Evidencia** | Bloco 18 — `EV-1` a `EV-11` | ✅ |
| **Resultado esperado** | O nXtrack **provando**, por evidencia verificavel por terceiro, o que hoje ele so **declara em prosa** sobre dado de titular — e o SOBERANO com as condicoes que a decisao de expor pressupoe | ✅ |

**`9` de `9`.** Nenhum elo aponta para artefato `superado`, `revogado` ou `depreciado` (`LN-03`).

## Memoria consultada

| Registro | O que informou esta `Spec` |
|---|---|
| [`MSG-2026-0009`](../../../memory/operacional/MSG-2026-0009-ato-soberano-admissao-do-nxtrack.md) | `DC-3` — fixou `LM-6(a)` como materia, **com prioridade** |
| [`PT-2026-014 §4`](../../../governance/relatorio-transicao-2026-08-01-portao-nxtrack.md) | `LM-1` a `LM-7`, e o metodo da varredura de 9 termos |
| [`PT-2026-016 §3`](../../../governance/relatorio-transicao-2026-08-01-fechamento-rd-33.md) | `GO-TO-SPECS` exercivel; `DoR` item (9) passa |
| [`MEM-APR-0006`](../../../memory/aprendizado/MEM-APR-0006-exercer-o-contador-revela-o-defeito.md) | `V3` — *"rodar o `DoR` contra o artefato que ainda nao existe"*, o metodo que abriu `RD-33` e que abriu `RD-91` |

## Perguntas em aberto

| # | Pergunta | Dono da resposta | Bloqueia? |
|---|---|---|---|
| `PA-1` | Ha enquadramento legal aplicavel, e qual? | **Assessoria humana qualificada** | **Nao** — `EX-3`. Os requisitos existem por medicao de fato, nao por norma externa citada |
| `PA-2` | Quantos titulares existem? | Missao com autorizacao para abrir dado vivo | **Nao** — `EX-6`. **`1` titular ja basta** para todos os `RQ` |
| `PA-3` | A colisao `C1` × `FND-04 §3.1` se corrige em `FND-11` ou em `FND-09 §8.2`? | **SOBERANO** | **Nao** — achado `RD-91`. A `Spec` esta em `C2`, e `C2` nao tem a colisao |

---

## Bloco DoR — exercido **antes** da revisao (`SF-23`, nove itens)

> **Exercido, nao afirmado.** Cada linha traz **onde se confere**.

| # | Item | OK | Onde se confere |
|---|---|---|---|
| 1 | Problema definido **antes** da solucao (`P-2`) | ✅ | `RFC-0026 §2` — `PB-1` a `PB-4` escritos **antes** de `§5 Opcoes`. Os `FATO`s `F-1` a `F-8` sao anteriores a qualquer `RQ` |
| 2 | Consumidor nomeado e necessidade demonstrada (`SF-04`) | ✅ | **Bloco 12** — 5 consumidores nomeados. Necessidade: `PB-1`/`PB-2` — DEP-ENG e DEP-QAR **nao tem hoje** contra o que construir e vetar |
| 3 | As **quatro** perguntas de nao-proliferacao respondidas por escrito (`FND-04 §6.1`) | ✅ | **(1)** *Ja existe?* **Nao** — `0` `Spec`s, e `FG-11` mede *"`0` artefato governa dado pessoal"*; `spec-tecnica-v1.md §24` e do **candidato**, fora do acervo, e sem criterio de aceite. **(2)** *Cabe em componente existente?* **Nao** — a Carta e `PRO`, e `FND-10 §4.3` reserva a Carta a existencia formal, nunca a requisito verificavel. **(3)** *Ganho `PI-14` e sinal observado?* **Organizacao e contexto**: requisito enderecavel por `SPC-001 RQ-nn` (`SF-31`); sinal **ja observado** em `PB-1`/`PB-2`. **(4)** *Como se sabe que deixou de ser necessaria?* Bloco Limites, `LI-4` |
| 4 | `Capability` **ativa** vinculada (`VC-01`) | ✅ | **Bloco 10** — `CAP-juridico`, `status: ativo`. **Conferido no arquivo**, nao no indice |
| 5 | Classe e tipo **classificados pelo proponente**, e validados por DEP-GOV (`FND-04 §2`) | ✅ | **Bloco 5** — `C2 · Tipo 2`, com a derivacao das quatro variaveis. Validacao de DEP-GOV registrada em `RFC-0026 §10` |
| 6 | Exclusoes declaradas (`SF-08`) | ✅ | **Bloco 14** — `EX-1` a `EX-7`, cada uma com *por que* e *quando poderia entrar* |
| 7 | **Todo** requisito com os **seis** campos (`SF-12`) | ✅ | **Bloco 13.1** — `10` de `10` com `ID`, motivo, fonte, criterio, metodo e evidencia. **Contagem: 60 campos, 0 ausentes** |
| 8 | Revisores designados, **≠ autor** (`AC-03`) | ✅ | **Bloco 8** — DEP-ENG + DEP-QAR ≠ DEP-PRD |
| 9 | Pre-condicoes de `FND-04 §6` linha *Spec* — inclusive **`Produto existe`** | ✅ | **`Produto existe`**: [`PRO-nxtrack`](../carta.md), `ativo` · `ratificada`. **`problema definido`**: Bloco 13.0 + `RFC-0026 §2`. **`criterios de aceite verificaveis`**: Bloco 13.1, `10` de `10`. **`escopo negativo explicito`**: Bloco 14 |

**9 de 9.** A `Spec` **pode** entrar em `em-revisao` (`O3`).

## Bloco DoD — `QG-1` e encerramento (`SF-24`, dez itens)

| # | Item | OK | Onde se confere |
|---|---|---|---|
| 1 | `QG-1` liberado por **DEP-EXE**, com responsavel e data (`FND-01 §6.2`) | ✅ | Bloco 20 — **DEP-EXE, 2026-08-02** |
| 2 | Revisao independente concluida | ✅ | DEP-ENG + DEP-QAR; parecer independente em [`FIT-2026-024`](../../../governance/fitness/FIT-2026-024-primeira-spec.md) |
| 3 | Aprovacao pela classe (`SF-10`) | ✅ | **DEP-EXE + parecer DEP-GOV**, derivado no Bloco 5 |
| 4 | Ratificacao **se** `C3` ou `Tipo 1` (`LM-02`) | ✅ **n/a declarado** | `C2 · Tipo 2` — **nao exigida**. Nao e omissao: e a regra sendo aplicada |
| 5 | Cadeia de nove elos percorrivel (`SF-20`) | ✅ | Bloco Rastreabilidade — **9 de 9** |
| 6 | Entrada no **catalogo mestre** com custo **medido** (`RG-02`, `CE-02`) | ✅ | [`artifact-registry §4.8`](../../../governance/artifact-registry.md) — **603 linhas**, medidas por `wc -l` |
| 7 | Cobertura das **quatro** categorias (`SF-25`) | ✅ | Bloco 13.2 — **4 de 4**, `0` ausencias a justificar |
| 8 | Suposicoes, limites, **rollback** e **criterio de abandono** (`SF-26`) | ✅ | Bloco Limites — `LI-1` a `LI-4`, **nenhum *"nao aplicavel"* sem motivo** |
| 9 | **`FIT` emitido se `C2` ou `C3`** (`CC-04`, `QG-6`) | ✅ | [`FIT-2026-024`](../../../governance/fitness/FIT-2026-024-primeira-spec.md) — **exigido porque a classe e `C2`** |
| 10 | Indices `M3` atualizados na **mesma** mudanca (`CV-04`, `IX-02`) | ✅ | Catalogo mestre, `README` raiz, `decisions/README`, `rfcs/README`, `governance/README`, `governance/fitness/README`, roadmap |

**10 de 10.** A mudanca **pode** encerrar.

## Bloco Limites declarados (`SF-26`) — quatro, distintas e obrigatorias

| Natureza | Conteudo |
|---|---|
| **`LI-1` SUPOSICAO** — o que se assume sem verificar, e o que muda se for falso | **Assume-se que o schema lido em codigo rastreado descreve o banco em producao.** `0` bancos foram abertos. **Se for falso** — o banco vivo tendo colunas que o codigo nao declara —, `RQ-1` fica **incompleto sem que o criterio acuse**, e `RQ-10` mede `100%` sobre a populacao errada. **Correcao:** `RQ-1` passaria a exigir inventario derivado do **banco**, e nao do codigo, o que exige autorizacao para abrir dado vivo |
| **`LI-2` LIMITE** — o que esta fora da capacidade declarada, **com o numero** | **Esta `Spec` alcanca `1` produto e `0` politicas organizacionais.** Alcanca as **24** tabelas medidas em 2026-08-02 e **`0`** sistemas fora do nXtrack. Nao alcanca **`LM-6(b)`**, nem `RD-71`, nem `RD-74`. **Nao alcanca nenhuma norma externa: `0` requisitos citam lei** |
| **`LI-3` ROLLBACK** — como se desfaz, com responsavel e custo | **Retirada por `O9`** (`SF-30`), declarando o que passa a valer no lugar (`SU-04`). **Responsavel: DEP-PRD** (`FND-09 §8.2`, *aposenta*). **Custo medido: 6 arquivos** — a `Spec`, catalogo, `README` raiz, `products` no medidor, roadmap e baseline nova. **`0` dependentes a migrar** enquanto nenhum componente citar um `RQ-nn` (`LC-05` sem trabalho). A partir do primeiro consumo, o custo passa a incluir plano de migracao (`SF-29`) |
| **`LI-4` ABANDONO** — como se sabe que deixou de ser necessaria | **Tres sinais, qualquer um bastando:** *(a)* o nXtrack deixar de guardar dado pessoal — `usuarios` sem `nome`/`senha_hash`/`sal`, medido pelo mesmo instrumento; *(b)* uma politica organizacional de dado pessoal entrar em vigor por `S2` e **absorver** `RQ-1`–`RQ-10`, caso em que esta `Spec` e **superada** e nao abandonada; *(c)* o produto ser encerrado por qualquer condicao do `§6` da Carta. **Reavaliacao: 2027-02-02** |

---

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-08-02 | DEP-PRD | **Criacao — a primeira `Spec` do LucaX Enterprise OS.** Fecha a lacuna `LM-6(a)` de `PRO-nxtrack`, materia que o **nono ato soberano** fixou com prioridade sobre as demais de `LA-7`. **10 requisitos** com os **seis** campos de `SF-12` *(60 campos, `0` ausentes)*, **4 de 4** categorias de `SF-25`, **7 de 7** perfis de `SF-17`, **5** metodos de `SF-14` exercidos, **9 de 9** elos de `SF-20`, **21 de 21** blocos de `SF-09`, **`DoR` 9 de 9** e **`DoD` 10 de 10** — todos **exercidos com o lugar da conferencia declarado**, nunca afirmados. Classe **`C2 · Tipo 2`** derivada, e a derivacao publicada no Bloco 5. **`0` decisoes embutidas** *(`SF-02`)*, **`0` requisitos que afirmem enquadramento legal**, **`0` requisitos que autorizem exposicao** — `RQ-5` e `RQ-6` **restringem**, e `EX-1` declara que satisfazer esta `Spec` **nao autoriza publicar**. **`0` bytes no repositorio do candidato**, **`0` bancos abertos**, **`0` execucoes**. **`LM-6(b)` declarado fora em `EX-2`.** |
