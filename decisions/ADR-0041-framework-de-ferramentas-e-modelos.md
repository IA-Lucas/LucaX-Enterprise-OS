---
id: ADR-0041-framework-de-ferramentas-e-modelos
titulo: Tool & Model Framework — institui TF-01 a TF-32, recebendo a entidade TOL e a classe modelo sem criar nada novo
tipo: adr
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-08-13
atualizado_em: 2026-08-13
revisao_prevista: 2027-02-13
decisoes_relacionadas: [ADR-0003, ADR-0021, ADR-0033, ADR-0040]
substitui: []
substituido_por: null
classe_mudanca: C2
tipo_decisao: 2
supera: []
superado_por: null
resumo: Institui o Tool & Model Framework - TF-01 a TF-32 - dentro do proprio ADR, segundo rito do decimo terceiro ato. Recebe TOL de FND-03 §3.12 e a classe modelo de ADR-0003 sem criar entidade, classe, tipo, template, papel ou portao. Os dois defeitos do TPL-ferramenta (AF-1 classe modelo omitida em 2 de 2 enumeracoes; AF-2 bloco de Capabilities habilitadas ausente) foram REMEDIDOS na admissao e CONFIRMAM - registrados abertos com dono, nunca corrigidos aqui por serem rito de TPL. A assimetria declarada - o Framework nao custa ato, toda Ferramenta que ele governar custara (adocao C2 Tipo 1 com ratificacao do Soberano).
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# ADR-0041: O Tool & Model Framework

## Contexto

Segundo rito do Bloco A do **decimo terceiro ato** *(ordem: 1.16 ✅ → **1.14** → 1.17 →
1.18)*. O candidato — `TF-01` a `TF-32`, Missao 1.14 de 2026-08-02, fora do acervo — entra
pelo metodo de `ADR-0033`/`ADR-0040`: **o Framework dentro do ADR**. A premissa do Goal ja
era norma: `FND-03 §3.12` traz a classe `modelo` desde `ADR-0003` — **Model e classe de
Ferramenta, sem framework paralelo**.

## Recepcao do candidato — conferida e REMEDIDA na admissao (2026-08-13)

| Verificacao | Resultado |
|---|---|
| **`H-A` do candidato** | `1cd2403b40ebb9131bb6517fd9bc7d9314b7144069421a8267764a95b4b4fc1d` *(347 linhas)* |
| **`AF-1` — classe `modelo` omitida no `TPL-ferramenta`** | **CONFIRMA hoje:** `modelo` com fronteira de palavra = **1** ocorrencia, e e o **homonimo** da linha 110 *("Modelo de cobranca")*; a classe segue fora das enumeracoes |
| **`AF-2` — bloco `Capabilities habilitadas`** | **CONFIRMA:** `0` ocorrencias no template |
| **`AF-3` — `tools/`** | **CONFIRMA:** inexistente no disco |
| **`L6` — "a ordem da Sequencia nao esta decidida"** | **ENVELHECEU A FAVOR:** a ordem FOI decidida pelo proprio 13º ato — a divergencia registrada do candidato esta **RESOLVIDA pelos fatos** |

## Decisao

**Instituir `TF-01` a `TF-32` como o Tool & Model Framework do acervo**, com o corpo do
candidato transcrito abaixo — **`0` entidades, classes, tipos, templates, papeis, portoes ou
verbos criados** *(§15)*. Classe **`C2 · Tipo 2`, `0` atos** — **e a assimetria fica gravada:
a norma nao custa ato; toda Ferramenta que ela governar custara** *(adocao `C2 · Tipo 1`,
ratificacao do SOBERANO — `FND-04 §6`)*.

---

## 2. O defeito medido no template, antes de qualquer regra

> **Medido por ferramenta em 2026-08-02, com controle positivo aplicado antes de se
> acreditar em qualquer numero** — a licao de `RD-95` e da primeira varredura de `LM-6(a)`.

| Medicao | Instrumento | Resultado |
|---|---|---|
| **Controle positivo** | `grep -oc "mcp"` em `TPL-ferramenta` | **2** — o instrumento esta vivo |
| **Controle positivo** | `grep -oic "ferramenta"` em `TPL-ferramenta` | **11** |
| Classes enumeradas na **fonte** `FND-03 §3.12` | contagem de linhas de tabela | **6** — `mcp`, `api`, `saas`, `local`, `dados`, **`modelo`** |
| Classes enumeradas no **template** `TPL-ferramenta` | leitura das duas enumeracoes | **5**, em **2 de 2** lugares — linha 36 *(instrucoes)* e linha 58 *(frontmatter)* |
| Ocorrencias da palavra `modelo` no template | `grep -nowi` | **1**, e e **homonimo**: linha 110, *"Modelo de cobranca"* |

**O template canonico da Ferramenta omite exatamente a classe de que este Framework
trata.** Hoje, um Modelo **nao e registravel pelo template canonico**: a enumeracao do
frontmatter nao o admite, e a instrucao de uso nao o lista.

**Isto e a familia de `RD-23`** — *template contra a norma* —, o quarto dos quatro achados
que obrigaram a `Spec` a ganhar contrato (`FND-11 §1`). **Aqui ele e o primeiro, e foi
achado por exercicio**, nao por leitura: so aparece quando se tenta usar o template para a
classe `modelo`.

> **A armadilha do homonimo esta declarada de proposito.** Uma varredura por `modelo` sem
> fronteira de palavra e sem inspecao devolve **1** e sugere que a classe consta. Ela nao
> consta: a unica ocorrencia e *"Modelo de cobranca"*, no bloco de custo. **Numero lido sem
> olhar o que ele conta e numero falso** — a mesma armadilha que a Missao 1.13.7 declarou
> para `SLO` e `REST`.

**Este Framework nao corrige o template**, e a razao e de competencia: template e emendado
por `DEP-GOV + dono do tipo`, aprovado por `DEP-GOV` (`FND-09 §8.2` linha `TPL`) — rito
proprio, **`C2`**, e **sem ato**. `TF-05` **exige** a correcao como pre-condicao de uso;
executa-la e mudanca de template. O achado fica **registrado e aberto** (§16, `AF-1`).

---

## 3. O que uma Ferramenta e, e o que nao e — `TF-01` a `TF-04`

| # | Regra |
|---|---|
| **TF-01** | **Uma `Ferramenta` e capacidade EXTERNA ao sistema, e o que a define e a fronteira, nao a tecnologia.** Fundamento: `FND-03 §3.12` — *"capacidade externa ao sistema que a organizacao usa"*. **O teste e um so: existe alguem fora da organizacao de quem essa capacidade depende para continuar existindo?** Se sim, e `TOL`. Se nao, e componente interno e pertence a `SKL`, `WFL` ou codigo. **Capacidade da propria maquina do Soberano e `TOL` de classe `local`** — a fronteira ali nao e de rede, e de custodia. |
| **TF-02** | **Uma `Ferramenta` nao e `Skill`, `Workflow`, `Agente`, `Spec`, decisao nem procedimento.** `SKL` e `WFL` sao **procedimento** (`FND-10 §4.4`); `AGT` e **ator**; `SPC` declara **o que deve ser verdadeiro** (`SF-01`); `ADR` decide. **A Ferramenta e o que o procedimento CHAMA** — ela nao decide quando e chamada, e declarar dentro da ficha quando ela deve ser usada e invadir `SKL`/`WFL`. **Ficha que descreva procedimento e devolvida.** |
| **TF-03** | **A Ferramenta nao cria autoridade e nao se autoriza a si propria.** Nenhuma ficha institui papel, portao, classe ou titular; nenhuma ficha e sua propria aprovadora ou avaliadora de risco (`LV-03`, `AC-03`, `RM-06b`). **A autoridade sobre a Ferramenta vive em `FND-09 §8.2` linha `TOL`**, e declara-la dentro da ficha e proibido por `AC-01` e `FND-10 §2.4`. **Em especial: a ficha nao concede a si mesma autorizacao de exposicao** — `TF-13`. |
| **TF-04** | **Uma Ferramenta nao vale por estar disponivel, e sim por ser consumida por consumidor nomeado.** Ferramenta sem **consumidor nomeado** e sem **necessidade demonstrada** e devolvida pelas **quatro** perguntas de `FND-04 §6.1`. **Disponibilidade nao e justificativa:** *"o provedor oferece"* e `FND-08 §7.1` — antecipacao, recusada. **Adotar Ferramenta para uso futuro provavel e proibido**; o sinal tem de estar **observado** (`PI-14`). |

## 4. Tool Contract — `TF-05` a `TF-09`

> **Declaracao de projecao (`PJ-02`).**
> **Fonte:** `FND-03 §4` *(nucleo universal de 15 campos)* · `FND-03 §3.12` *(4 atributos
> proprios)* · `FND-10 §2.2` *(extensao de 5 campos)* · `FND-10 §2.5` *(`AC-01` a `AC-11`)* ·
> `FND-09 §8.2` linha `TOL` · `FND-04 §6` linha *Ferramenta*.
> **Campos projetados:** apenas **quais blocos a ficha deve conter e onde cada exigencia
> nasce**. **Metodo de atualizacao:** pela mesma mudanca que altera a fonte (`CV-04`), por
> emenda deste Framework (`TF-32`). **Em divergencia prevalece a fonte** (`PJ-03`).

| # | Regra |
|---|---|
| **TF-05** | **O contrato da ficha e o contrato universal do artefato, mais os quatro atributos que `FND-03 §4` ja reserva a Ferramenta, e nenhum campo novo.** Os **15** campos de `FND-03 §4`, os **5** de `FND-10 §2.2` e os **4** proprios — `classe`, `dado_trafegado`, `custo`, `criticidade` — sao **obrigatorios**. **Ausencia = artefato nao conforme = veto de DEP-GOV** (`AC-06`). **Nenhum campo novo e criado por este Framework** (`AC-07`). **O campo `classe` admite os SEIS valores de `FND-03 §3.12`, e a enumeracao do template que admite cinco esta defasada em relacao a fonte** — §2. **Enquanto o template nao for corrigido, ficha de classe `modelo` e criada contra a enumeracao do proprio template**, e por `PJ-03` **prevalece a fonte**. |
| **TF-06** | **Os campos condicionais da Ferramenta sao os quatro de `FND-03 §4`, e nada alem.** **Nao se declara** no frontmatter: consumidor, autorizacao, credencial, provedor, endpoint, limite, custo apurado nem dependencia transitiva. **Consumidor e autorizacao vivem no corpo** (`AC-01`, `FND-10 §2.4`); **credencial nao vive em lugar nenhum da ficha** (`TF-15`). |
| **TF-07** | **A ficha declara as `Capabilities` que a Ferramenta habilita, e exatamente um Departamento responsavel.** Fundamento **literal**: `FND-04 §6` linha *Ferramenta* exige ***"Capabilities habilitadas declaradas"*** entre as pre-condicoes de criacao. **Capability inexistente, `proposta` ou `aposentada` bloqueia a aprovacao** (`VC-01`, `VC-02`); competencia que nao caiba no catalogo exige **RFC de Capability antes**. **O Departamento responsavel e DEP-TLS por `FND-03 §3.12`** — o campo declara **quem consome**, nunca quem e dono. |
| **TF-08** | **A ficha declara `usos nao autorizados` em bloco proprio e obrigatorio.** Escopo negativo ausente e **defeito de ficha**, nao omissao de estilo — a mesma regra que `SF-08` impoe a `Spec`, pelo mesmo fundamento (`PI-09`, ampliacao silenciosa proibida). **Cada uso vedado declara por que fica de fora e sob qual condicao poderia entrar.** **Ficha que so enumere usos autorizados e incompleta:** o que nao esta escrito **nao esta permitido** e o silencio nao concede (`TF-13`). |
| **TF-09** | **Os blocos obrigatorios de corpo da ficha sao dezoito**, e cada um existe porque uma fonte o exige. **Bloco ausente = ficha incompleta**, e ficha incompleta **nao entra em `em-revisao`** (`O3`). |

**Os dezoito blocos, e a fonte de cada exigencia:**

| # | Bloco | Por que e obrigatorio |
|---|---|---|
| 1 | **Identidade** | `id`, `titulo`, `versao`, `status` — `FND-03 §4` |
| 2 | **Proposito** | Bloco obrigatorio de corpo — `FND-10 §2.2` |
| 3 | **Escopo** *(usos autorizados / vedados / quem pode usar)* | `TF-08`; `PI-09` |
| 4 | **Responsaveis** | `FND-09 §8.2` linha `TOL` |
| 5 | **Finalidade** | `FND-04 §6` linha *Ferramenta*, pre-condicao 1 |
| 6 | **Alternativas avaliadas** | `FND-04 §6`, pre-condicao 5; `PI-11` |
| 7 | **Capabilities habilitadas** | `FND-04 §6`, pre-condicao 7 — **literal** |
| 8 | **Dado que trafega** | `FND-04 §6`, pre-condicao 2; `TF-11` |
| 9 | **Autorizacao de exposicao** | `TF-13`; `EX-03`, `LV-08` |
| 10 | **Acesso e segredo** | `TF-15`; `PI-08`, `LV-02` |
| 11 | **Isolamento e sandbox** | `TF-18` a `TF-20` |
| 12 | **Custo** | `FND-04 §6`, pre-condicao 3; `TF-21` |
| 13 | **Limites de uso** | `TF-22`, `TF-23` |
| 14 | **Dependencia e risco** | `FND-04 §6`, pre-condicao 4; `TF-28` |
| 15 | **Comportamento em falha** | `TF-28` |
| 16 | **Observabilidade** | `TF-29` |
| 17 | **Autorizacao por consumidor** | `TF-30` |
| 18 | **Criterio de descarte** | `FND-04 §6`, pre-condicao 6; `DP-05` — **obrigatorio na adocao** |

> **Dezoito, e nao dez.** O template vigente tem **10** secoes de corpo. Os **8**
> acrescimos — escopo negativo, autorizacao de exposicao, isolamento, limites, falha,
> observabilidade, autorizacao por consumidor e Capabilities habilitadas — **nao sao
> invencao deste Framework**: sete deles citam fonte vigente na coluna da direita, e o
> oitavo (`Capabilities habilitadas`) e **exigencia literal** de `FND-04 §6` que o template
> **ja deveria conter e nao contem**. **O template esta defasado em relacao a duas fontes,
> nao a uma** — §2 mede a primeira, este bloco mede a segunda.

## 5. Autoridade e ciclo — `TF-10`

| # | Regra |
|---|---|
| **TF-10** | **A autoridade sobre uma Ferramenta e derivada, nunca declarada na ficha.** Ela e funcao de **quatro** variaveis, nesta ordem: **(a) a classe do efeito** (`AL-01`, com **`C2 · Tipo 1` como piso de ADOCAO** por `FND-04 §6` linha *Ferramenta*); **(b) o tipo de reversibilidade** (`FND-04 §2.2`); **(c) o dado que trafega** (`TF-11` — dado `sensivel` **eleva**); **(d) a criticidade declarada**. **Toda ficha que fixe aprovador em texto e nao conforme** — foi exatamente o defeito de `RD-23` na `Spec`. Na duvida prevalece **a classe mais restritiva** (`FND-01 §7.1`). |

**Mapeamento das dez etapas do ciclo — projecao declarada:**

> **Declaracao de projecao (`PJ-02`).** **Fonte:** `FND-04 §2`, `§2.1`, `§2.2`, `§6` ·
> `FND-09 §8.2` linha `TOL` · `FND-10 §5.2`, `§5.4`, `§6.2` · `ADR-0020` `PA-01` a `PA-14`.
> **Campos projetados:** apenas **etapa × titular**. **A fonte prevalece** (`PJ-03`).

| Etapa | **Adocao — `C2 · T1`** | **Emenda de merito — `C2 · T2`** | **Correcao — `C0`** | **Descarte — `O9`** |
|---|---|---|---|---|
| **Proposta** | **DEP-TLS** | **DEP-TLS** | proprietario | **DEP-TLS** |
| **Autoria** | **DEP-TLS** | **DEP-TLS** | proprietario | **DEP-TLS** |
| **Revisao** | **DEP-QAR + DEP-ENG** | **DEP-QAR + DEP-ENG** | — | **DEP-QAR** |
| **Avaliacao de risco** | **DEP-QAR** | **DEP-QAR** | nao se aplica | **DEP-QAR** |
| **Aprovacao** | **DEP-EXE** | **DEP-EXE** | proprietario | **DEP-EXE** |
| **Ratificacao** | **SOBERANO** — indelegavel | **nao exigida** | **nao exigida** | **SOBERANO** se a adocao foi ratificada |
| **Registro** | **DEP-GOV**, **apos** o ato | **DEP-GOV** | `atualizado_em` | **DEP-GOV** |
| **Vigencia** | **apos** `ratificacao: ratificada` (`LM-02`) | nomeado na emenda | ja `ativo` | — |
| **Emenda** | MAIOR ou MENOR conforme o efeito (`AL-01`) | idem | CORRECAO | — |
| **Retirada** | **DEP-TLS**, com dependentes migrados (`LC-05`) | idem | idem | **DEP-TLS** |

**Quarenta celulas. Nenhum titular novo:** `DEP-TLS`, `DEP-QAR`, `DEP-ENG`, `DEP-EXE`,
`DEP-GOV` e `SOBERANO` **ja constam** de `FND-04 §2` e `FND-09 §8.2`.

> **A coluna que importa e a primeira.** **Adotar Ferramenta e `Tipo 1` — irreversivel na
> pratica —, e por isso leva ato do Soberano.** A razao esta escrita em `TPL-ferramenta`:
> *"cria dependencia"*. **Nao se desfaz uma dependencia externa desfazendo o documento.**

## 6. Dado, exposicao e classificacao — `TF-11` a `TF-14`

| # | Regra |
|---|---|
| **TF-11** | **Quatro niveis de dado, e a ficha declara o MAIOR que pode trafegar, nunca o tipico:** **`nenhum`** *(a Ferramenta nao recebe dado da organizacao)* · **`publico`** *(ja divulgado por decisao propria)* · **`interno`** *(nao divulgado, sem terceiro identificavel)* · **`sensivel`** *(dado pessoal, credencial, financeiro, ou de terceiro identificavel)*. **A enumeracao e a de `TPL-ferramenta` linha 59, recebida e nao alterada.** **Declarar o tipico e nao o maximo e defeito de ficha:** o limite existe para o pior caso, e o pior caso e o que vaza. |
| **TF-12** | **A classificacao do dado e declarada ANTES da adocao e verificada por terceiro.** Fundamento: `FND-04 §6` linha *Ferramenta* poe *"dado que trafega"* entre as pre-condicoes **de criacao**. **Reclassificar para cima e emenda MAIOR e reabre a aprovacao**; reclassificar para baixo exige **evidencia medida**, nunca alegacao do proprietario. **Ferramenta cujo dado nao foi classificado nao e adotavel** — e a pre-condicao nao admite *"a definir"*. |
| **TF-13** | **Enviar dado a Ferramenta externa e ATO DE EXPOSICAO, e exige autorizacao ESPECIFICA — jamais geral.** Fundamento literal, ja vigente e ja impresso no proprio template: *"Envio de dado a servico externo e ato de exposicao: exige autorizacao especifica, nao geral"* (`EX-03`, `LV-08`). **Consequencias que este Framework torna explicitas:** **(a)** autorizacao para dado `interno` **nao** autoriza `sensivel`; **(b)** autorizacao para um consumidor **nao** se estende a outro (`TF-30`); **(c)** autorizacao para um uso **nao** se estende a uso novo, ainda que na mesma Ferramenta; **(d)** **o silencio nao autoriza** — o que a ficha nao lista em usos autorizados esta vedado (`TF-08`). |
| **TF-14** | **Dado `sensivel` eleva a classe e obriga requisito NEGATIVO escrito.** Ferramenta que possa fazer trafegar `sensivel` **nao e adotavel** sem: **(1)** o que **nao** pode ser enviado, enumerado; **(2)** o que acontece se for enviado por engano, com responsavel; **(3)** retencao pelo provedor, **com numero e fonte**, ou a declaracao *"nao informado pelo provedor"* — que **e** informacao e **e** risco. **`nao informado` nao equivale a `nenhum`**, e tratar os dois como iguais e `LV-12`. |

## 7. Credencial e segredo — `TF-15` a `TF-17`

| # | Regra |
|---|---|
| **TF-15** | **Credencial NUNCA aparece na ficha — apenas o NOME da variavel de ambiente.** Fundamento: `PI-08`, `LV-02`, `FND-03 §3.12` *(regra literal do tipo)* e `FND-10`, que lista *"credencial em texto"* como **o risco declarado do tipo `TOL`**. **A proibicao alcanca valor, fragmento, exemplo, valor de teste, valor expirado e valor ofuscado.** **Credencial em ficha e incidente de conformidade**, nao erro de redacao: abre `INC` por `FND-09 §8.2` linha `INC` — *"quem detecta (obrigatorio)"*. |
| **TF-16** | **Toda ficha declara quem pode rotacionar a credencial e o que acontece quando ela e rotacionada.** O template ja pede *"quem pode rotacionar"*; este Framework acrescenta a **consequencia**: que consumidores param, por quanto tempo, e quem os avisa. **Rotacao sem consumidor mapeado e indisponibilidade nao planejada** — e o mapa e `TF-30`. |
| **TF-17** | **Credencial vazada e descarte, nao correcao.** Suspeita de exposicao obriga, nesta ordem: **revogar** · **gerar nova** · **conferir que a antiga nao responde** · **registrar `INC`**. **Trocar o valor sem revogar o anterior nao e remediacao**, e declarar remediado sem a terceira etapa e `LV-12` — evidencia fabricada. |

## 8. Isolamento e sandbox — `TF-18` a `TF-20`

| # | Regra |
|---|---|
| **TF-18** | **A ficha declara o ALCANCE da Ferramenta sobre o ambiente, em tres eixos, e a ausencia de declaracao le-se como alcance TOTAL.** Os eixos: **leitura** *(o que ela pode ler)* · **escrita** *(o que ela pode alterar, criar ou apagar)* · **execucao** *(o que ela pode fazer rodar)*. **A regra de leitura e deliberadamente pessimista:** eixo nao declarado conta como **irrestrito** para efeito de classe (`TF-10`) e de risco, ate ser declarado. **Isto inverte o onus e e proposital** — a alternativa e uma ficha silenciosa parecer mais segura que uma ficha honesta. |
| **TF-19** | **Ferramenta com eixo de ESCRITA ou de EXECUCAO declara o limite espacial desse eixo, com caminho.** Nao basta *"escreve"*: declara-se **onde**. **Ferramenta de classe `local` que escreva fora de um caminho declarado e Ferramenta sem limite**, e sem limite a criticidade e `alta` por construcao, **nao por escolha do proprietario**. |
| **TF-20** | **Isolamento e propriedade DECLARADA e VERIFICADA, nunca presumida do provedor.** *"O provedor roda em sandbox"* e **`HIPOTESE`**, e entra marcada, com o teste que a confirmaria — a mesma regra que `SF-13` impoe a `Spec`. **Alegacao de isolamento sem metodo de verificacao de `SF-14` nao e propriedade da Ferramenta: e material de marketing do provedor**, e o acervo ja proibiu tratar afirmacao de terceiro como fato verificado. |

## 9. Custo e limites — `TF-21` a `TF-23`

| # | Regra |
|---|---|
| **TF-21** | **Custo e MEDIDO com instrumento e data, ou declarado `definido, sem valor` — e proibido estimar.** Fundamento: `CE-04` *(proibido estimar)* e `LM-01` *(indicador sem valor medido nao prova conformidade)*. **`0` nao e resposta valida sem instrumento:** *"gratuito"* declara-se com o **limite do plano gratuito** e **o que acontece ao ultrapassa-lo** — plano gratuito com teto e custo diferido, nao ausencia de custo. |
| **TF-22** | **Todo limite declarado tem tres campos: valor, instrumento que o mede, e consequencia de ultrapassar.** Limite sem consequencia **nao e limite, e expectativa**. **Consequencia declarada como *"avaliar"* e nula** — nomeia-se o que acontece com a chamada seguinte: falha, fila, degradacao ou corte. |
| **TF-23** | **Limite de contexto e limite de USO e declara-se como tal, com a unidade do provedor.** A ficha declara a unidade *(token, requisicao, byte, minuto)*, o teto por chamada, o teto por janela e **quem monitora** — o template ja atribui o monitoramento a `DEP-EXE`, funcao Recursos. **Ultrapassar limite de contexto e falha, e cai em `TF-28`** — nao e caso especial e nao se resolve truncando em silencio. **Truncar sem registrar e perda de dado nao declarada.** |

## 10. Modelo — selecao, roteamento e fallback — `TF-24` a `TF-27`

> **Esta secao nao decide que Modelo se usa, e nao pode.** Ela fixa **como** se decide, o
> que e materia deste Framework; **qual** e materia de cada ficha, sob `C2 · Tipo 1` com
> ato. **`0` provedores sao integrados aqui**, e a exigencia do roadmap — *"sem integrar
> provedor ainda"* — e cumprida por construcao.

| # | Regra |
|---|---|
| **TF-24** | **Modelo e classe de Ferramenta, e nao ha framework paralelo.** **Isto e recebido, nao decidido:** `FND-03 §3.12` ja fixa a classe `modelo` — *"Modelo de IA consumido como capacidade externa"* —, acrescentada por **`ADR-0003`**, que **absorveu a candidata `Model`** de `FND-09 §5.8 X-08`. **Consequencia dura:** toda regra `TF-01` a `TF-23` e `TF-28` a `TF-32` **vale integralmente para Modelo**, sem excecao e sem versao propria. **`TF-25` a `TF-27` nao sao regime separado: sao as tres perguntas que so a classe `modelo` levanta.** |
| **TF-25** | **Selecao de Modelo e por RESULTADO PARA A TAREFA; custo e restricao declarada, nunca criterio dominante.** Fundamento literal, ja vigente e ja impresso no template: `PI-11`. **A ficha responde as tres perguntas do bloco `PI-11` do template com nome de tarefa, nao em abstrato:** *"melhor para qual tarefa"*. **Ficha que selecione por preco e nao conforme com `PI-11`**; ficha que selecione por popularidade nao responde a nenhuma pergunta do acervo. |
| **TF-26** | **Roteamento entre Modelos e declarado como REGRA VERIFICAVEL, com a condicao que o dispara.** Roteamento sem condicao escrita e **decisao tomada em tempo de execucao por criterio nao auditavel** — e o acervo exige que a decisao seja rastreavel ao artefato, **sem consultar pessoa** (`LN-07`). **A condicao e verificavel por um dos cinco metodos de `SF-14`**, ou nao e condicao. **Roteamento que possa enviar dado a Ferramenta de nivel de dado SUPERIOR ao autorizado e vedado** — e a vedacao e absoluta, porque `TF-13` faz a autorizacao ser especifica: **rotear nao herda autorizacao**. |
| **TF-27** | **Fallback e declarado ANTES da falha, com as quatro respostas, ou nao existe.** **(1)** Qual Ferramenta assume · **(2)** sob que condicao exata · **(3)** que diferenca de resultado se aceita · **(4)** **quem e avisado de que o fallback ocorreu**. **Fallback silencioso e proibido:** substituir a Ferramenta sem registrar produz resultado cuja origem nao e rastreavel, e viola a cadeia de rastreabilidade. **O fallback herda o teto de dado do PRIMARIO, nunca o proprio** — se a substituta admite menos, o fallback **nao ocorre** e o caso vira falha (`TF-28`). |

## 11. Falha e observabilidade — `TF-28` a `TF-29`

| # | Regra |
|---|---|
| **TF-28** | **Toda ficha declara o comportamento em falha em quatro naturezas, e nenhuma admite omissao:** **indisponivel** · **lenta alem do limite** · **resposta invalida** · **resposta plausivel e errada**. **A quarta e obrigatoria e e a que se esquece:** Ferramenta que devolve resultado bem-formado e incorreto **nao dispara alarme**, e o acervo ja tem o instrumento para isso — declara-se **como se detecta**, por metodo de `SF-14`. **Ficha sem a quarta natureza e incompleta**, e a incompletude **se declara**, nunca se presume ausencia de risco. |
| **TF-29** | **Observabilidade e o que se REGISTRA a cada chamada, declarado por campo — e credencial e conteudo sensivel nunca entram no registro.** A ficha declara: **o que se registra** *(no minimo: quando, quem chamou, resultado, custo apurado)*, **onde**, **por quanto tempo** e **quem le**. **Registro que carregue `sensivel` transforma o log em segunda superficie de exposicao** e recai em `TF-13` — **exige autorizacao propria**, porque a autorizacao de chamar **nao** autoriza guardar. |

## 12. Autorizacao por Departamento, Skill e Agente — `TF-30`

| # | Regra |
|---|---|
| **TF-30** | **A autorizacao de uso e por CONSUMIDOR NOMEADO, e a lista vive na ficha.** Cada consumidor autorizado — Departamento, `SKL`, `WFL`, `AGT` ou `SUB` — e **enumerado**, com o **uso** e o **nivel de dado** que lhe cabe. **Tres regras duras:** **(a)** *"todos os Departamentos"* **nao e enumeracao** e e devolvido — `SF-29` ja proibiu *"todos"* como declaracao de dependentes, e a razao e a mesma: nao se migra nem se revoga o que nao foi nomeado; **(b)** **autorizacao nao se herda por composicao** — `SKL` autorizada nao autoriza o `AGT` que a invoca, porque `FND-09` proibe que agente de um departamento use componente de outro (`PD-12`), e herdar por invocacao contornaria a proibicao; **(c)** o nivel de dado do consumidor e **o menor** entre o dele e o da Ferramenta, nunca o maior. |

## 13. Mudanca, versionamento e descarte — `TF-31`

| # | Regra |
|---|---|
| **TF-31** | **`TOL` e `M2` — versionavel, com texto anterior preservado** (`FND-10 §6.2`). **A versao segue o efeito, nao o tamanho do texto** (`AL-01`): **MAIOR** quando muda o nivel de dado para cima, o alcance de `TF-18`, o teto de `TF-22` ou a lista de `TF-30`; **MENOR** quando se acrescenta consumidor ou limite sem alterar os anteriores; **CORRECAO** quando nada normativo muda. **Alteracao silenciosa e nula** (`AC-11`, `GV-01`). **O criterio de descarte e obrigatorio na adocao** (`DP-05`) e declara **condicao**, **sinal observavel** e **substituto previsto** — descarte sem substituto declara **o que passa a valer no lugar**, inclusive *"a organizacao deixa de ter esta capacidade"*, que **e** resposta valida e **e** decisao. |

## 14. Template, registro e regime deste Framework — `TF-32`

| # | Regra |
|---|---|
| **TF-32** | **Um template canonico, um registro mestre, e nenhum registro novo.** **Template:** `TPL-ferramenta`, unico, mantido por `DEP-GOV + DEP-TLS` e aprovado por `DEP-GOV` (`FND-09 §8.2` linha `TPL`) — **e ele precisa da correcao de §2 antes do primeiro uso na classe `modelo`**. **Registro mestre:** o catalogo mestre, que e o **contador oficial** da sequencia `TOL` e o **indice** do diretorio. **Nenhum registro novo de Ferramentas e criado por este Framework:** criar um segundo seria proliferacao (`FND-04 §6.1`) e arquivo satelite por artefato, proibido por `RG-05`. **Adotar Ferramenta e incrementar o contador sao a mesma mudanca** (`CV-04`, `IX-02`). **Este Framework e `M2`**: emenda-se por versao, pela classe do efeito, e **como `C2 · Tipo 2` a emenda NAO exige ato** — ao contrario de `FND-11 SF-32`, cuja sede fundacional obriga ratificacao (`LM-02`). **A diferenca e de sede, nao de merito**, e §15 declara o tradeoff. |

## 15. O que este Framework NAO faz

| # | Nao faz | Verificacao |
|---|---|---|
| **N1** | **Nao cria entidade.** `TOL` ja existe | `FND-03 §3.12`, `FND-09 §8.2` — `0` linhas acrescentadas a matriz |
| **N2** | **Nao cria classe.** `modelo` ja existe desde `ADR-0003` | `FND-03 §3.12` — **6** classes antes, **6** depois |
| **N3** | **Nao cria tipo documental, template, diretorio, papel, portao nem verbo de autoridade** | `FND-09 §11.1`; `FND-10 §1.3`; `MT-01`, `CS-01`. **Medido nas duas familias de portao, que sao distintas e nao se somam:** os **7** portoes de qualidade de `FND-01 §6.2` — `QG-0` a `QG-6` — **7 antes, 7 depois**; e os portoes de sequencia `GO-TO-*`, **2** no acervo normativo *(`GO-TO-SPECS`, `GO-TO-SKILLS`)* — **2 antes, 2 depois** |
| **N4** | **Nao altera a matriz de `FND-09 §8.2`** | `0` celulas tocadas. `TF-10` **remete**, nao decide |
| **N5** | **Nao altera as pre-condicoes de `FND-04 §6`** linha *Ferramenta* | As **7** continuam as mesmas; `TF-07` a `TF-09` **as projetam** |
| **N6** | **Nao adota Ferramenta, nao integra provedor, nao cria `tools/`** | **`0`** `TOL` · `tools/` **permanece inexistente** |
| **N7** | **Nao corrige `TPL-ferramenta`** — apenas **mede** o defeito e o registra | §2; `AF-1` em §16. Correcao e rito de `TPL`, `C2`, sem ato |
| **N8** | **Nao promove a si mesmo a `FND`** | Promover e `C3 · Tipo 1` com ato — foi o que `ADR-0022` custou a `FND-11` |
| **N9** | **Nao decide a ordem da Sequencia do roadmap** nem libera portao algum | Portao e ato de autoridade (`FND-01 §6.2`), e este texto nao e autoridade |

> **O tradeoff de sede, declarado no sentido correto.** Como `ADR`, este Framework **custa
> menos** — `C2 · Tipo 2`, sem ato — e **protege menos**: vive em artefato `M1`, que por
> `AC-10` e `CC-01` **nunca se emenda**, e corrigir uma virgula exigiria **ADR sucessor**.
> **Foi exatamente o custo que `ADR-0021` pagou e que `FND-11` depois desfez**, com ato, em
> `ADR-0022`. **A escolha de nascer `ADR` e deliberada:** nascer `FND` exigiria ato **antes**
> de a norma ter sido exercida uma unica vez — e o acervo ja mediu, em `L1` de `FND-11 §14`
> e em `RD-107`, o que custa canonizar o que ainda nao foi observado.

## 16. Limites declarados — **determinado, nao observado**

| # | Limite | Fundamento |
|---|---|---|
| **L1** | **Nenhuma `Ferramenta` real existe.** As **32** regras sao **determinadas, nao observadas** — `tools/` nao existe e `0` `TOL` foram adotadas | Medido em 2026-08-02; mesma forma de `L1` de `FND-11 §14` |
| **L2** | **`TF-09` institui 18 blocos obrigatorios sem custo medido.** `CE-04` proibe estimar, e **nada foi estimado**: o valor sera medido na **primeira ficha** | `CE-04`; ressalva `R2` de `FIT-2026-015`, aplicada por analogia de metodo |
| **L3** | **Nenhum fallback real ocorreu.** `TF-27` e determinado, nao observado | `PI-10` |
| **L4** | **Nenhuma falha de quarta natureza — *plausivel e errada* — foi observada.** `TF-28` e a regra menos testada do conjunto | `PI-10` |
| **L5** | **O defeito de template de §2 esta MEDIDO e NAO CORRIGIDO**, e a correcao e pre-condicao de uso da classe `modelo` | `AF-1`; `PJ-03` |
| **L6** | **A ordem da Sequencia nao esta decidida.** O acervo nomeia `GO-TO-SKILLS` **4 vezes** como *"o portao seguinte"* a `GO-TO-SPECS`, e o roadmap vai de 1.13.5 direto a 1.14 | Primeira DIVERGENCIA REGISTRADA do roadmap, **aberta**, decisao do Fundador |

## 17. Achados que este candidato ABRE

| # | Achado | Severidade | Dono | Gatilho |
|---|---|---|---|---|
| **AF-1** | **`TPL-ferramenta` 1.0.0 omite a classe `modelo` em 2 de 2 enumeracoes** *(linhas 36 e 58)*, enquanto `FND-03 §3.12` declara 6 classes. Familia de `RD-23`. A unica ocorrencia de *"Modelo"* e homonimo *("Modelo de cobranca")* | **Media** | `DEP-GOV + DEP-TLS` *(dono do tipo `TPL`)* | Primeira ficha de classe `modelo` |
| **AF-2** | **`TPL-ferramenta` nao contem bloco de `Capabilities habilitadas`**, que `FND-04 §6` linha *Ferramenta* exige **literalmente** como pre-condicao de criacao. **Ficha produzida pelo template vigente nasce sem cumprir uma das 7 pre-condicoes** | **Media** | `DEP-GOV + DEP-TLS` | Primeira adocao de Ferramenta |
| **AF-3** | **`tools/` nao existe no disco**, embora `FND-03 §7` **ja o declare** na estrutura canonica, marcado *"(fase futura)"*. **O obstaculo NAO e o diretorio** — e `LV-06`: ***"criar agente, produto, workflow ou ferramenta sem Carta aprovada"*** e violacao. **A ficha `TOL` E a Carta da Ferramenta**, e ela so vale aprovada, o que em `C2 · Tipo 1` significa **com ratificacao do SOBERANO** | **Media** | `SOBERANO` | Primeira adocao de Ferramenta |

## 18. Rastreabilidade e revisao

| Campo | Conteudo |
|---|---|
| **Origem da entidade** | `FND-03 §3.12` · `FND-09 §8.2` linha `TOL` — **recebidas, nao alteradas** |
| **Origem da classe `modelo`** | **`ADR-0003`**, que absorveu a candidata `Model` de `FND-09 §5.8 X-08` |
| **Fontes que este Framework projeta** | §4 *(Tool Contract, 18 blocos)* e §5 *(ciclo, 40 celulas)*, ambas com `PJ-02`. **Em divergencia prevalece a fonte** (`PJ-03`) |
| **Fontes que este Framework NAO altera** | `FND-03 §3.12` · `FND-04 §6` · `FND-09 §8.2` · `FND-10 §4`, `§6.2` · `TPL-ferramenta` |
| **Metodo** | O de `ADR-0021` para a `Spec`: **instituir contrato em ADR `C2 · Tipo 2`, sem emendar fonte alguma** |
| **Gatilho de revisao** | A **primeira Ferramenta real** — o unico evento que transforma `TF-*` de determinado em observado (`L1`); **ou** o primeiro **fallback real** (`L3`); **ou** a primeira falha *plausivel e errada* (`L4`) |
| **O que se mede na revisao** | Quantas fichas foram **devolvidas**, e por qual regra; **linhas medidas** da primeira ficha; quantas vezes `TF-13` recusou uma exposicao; quantas vezes o alcance nao declarado de `TF-18` foi lido como total |

---

## Rito e rastreabilidade da admissao

Cadeia: [RFC-0036](../rfcs/RFC-0036-framework-de-ferramentas-e-modelos.md) → este ADR →
[FIT-2026-034](../governance/fitness/FIT-2026-034-framework-de-ferramentas-e-modelos.md).
Os achados `AF-1` a `AF-3` entram **abertos**, com donos e gatilhos do candidato — e `AF-1`/
`AF-2` sao **pre-condicao de uso**: a primeira ficha de classe `modelo` e a primeira adocao
de Ferramenta **esbarram neles por desenho**. **Gatilho de revisao:** a primeira Ferramenta
real, ou o primeiro fallback real, ou a primeira falha *plausivel e errada*.
