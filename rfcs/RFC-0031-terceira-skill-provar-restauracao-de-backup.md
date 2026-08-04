---
id: RFC-0031-terceira-skill-provar-restauracao-de-backup
titulo: A terceira Skill do acervo — provar restauracao de backup —, o piso de n de SK-24 e o que muda quando o candidato nasce escrito sob as 26
tipo: rfc
versao: 1.0.0
status: aprovado
camada_memoria: nao-aplicavel
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-08-03
atualizado_em: 2026-08-03
revisao_prevista: null
decisoes_relacionadas: [ADR-0033, ADR-0034, ADR-0035, ADR-0036]
substitui: []
substituido_por: null
classe_mudanca: C2
prazo_analise: 2026-08-03
---

# RFC-0031: A terceira `Skill`

## Proposito

Criar a **terceira `Skill`** do acervo a partir de `custodia-provar-restauracao-de-backup`, e
**medir `SK-24` no primeiro `n` em que a regra pode devolver *"sim"***.

> **A ficha nao e o entregavel principal, e desta vez isso e demonstravel.** `PT-2026-022` provou
> que `SK-24` e **estruturalmente vazia** ate `n = 3`: com uma ou duas instancias, disparar exigiria
> `a < 0`. **Um teste que so pode devolver *"nao"* nao esta medindo nada.** O que falta ao enunciado
> e o **piso de `n`**, e piso so se mede onde o teste **pode** disparar.

**E ha uma quinta medicao que nenhuma missao anterior podia fazer:** este candidato **nasceu
escrito sob `SK-01` a `SK-26`**, sabendo dos **tres defeitos** que as duas primeiras pagaram.
**Reduziu o retrabalho?** §6 responde com contagem.

## Escopo

| Item | Valor |
|---|---|
| **Inclui** | O enquadramento do candidato sob `SK-01` a `SK-26` **antes** de propor, com poder de **PARAR**; a terceira medicao de `SK-09` e `SK-10`; o calculo de `SK-24` com `n = 3`; a resposta medida sobre `SK-21`; e a contagem de retrabalho de §6 |
| **NAO inclui** | Abrir o `ADR` sucessor · promover `ADR-0033` a `FND` · emendar `TPL-skill` · sanar `RD-122` · mover codigo · **admitir o segundo candidato da F8** *(um por missao)* |

---

## 1. Item 0 — o candidato cabe sob as `26`?

**Medido ANTES de propor, com poder de PARAR a missao.** O despacho e explicito sobre a
consequencia: **candidato escrito sob o Framework que o Framework recusa e achado SOBRE o
Framework**, e obrigaria parar em vez de redigir.

**Resultado: nenhuma das `26` recusa.** Uma quase recusou — `SK-22`, §3.

### 1.1 As que passam, com o sinal que as sustenta

| Regra | Veredito | Sinal |
|---|---|---|
| **`SK-01`** | ✅ | As tres condicoes **cumulativas**: o procedimento **se repete** *(a cada instalacao, troca de destino e cadencia)*, o resultado e **verificavel** *(tres vereditos parciais + codigo de saida)*, e e **usavel por mais de um papel** *(4 consumidores nomeados)* |
| **`SK-02`** | ✅ | **Nao depende de quem invoca.** Provar restauracao nao muda com o papel |
| **`SK-03`** | ⭐ **PASSA — e e a PRIMEIRA vez em tres** | `custodia-provar-restauracao-de-backup` **ja e** `<dominio>-<verbo>-<objeto>`. Ver §5 |
| **`SK-04`** | ✅ | **Um papel por execucao**, e os passos `1` e `2` sao **recusas internas**, nao portoes de qualidade — mesma leitura que `RFC-0029` fixou para os passos `1`–`3` da primeira `Skill` |
| **`SK-05`** | ✅ | Nao e `Prompt` nem `Playbook`: ha instrumento executavel, veredito e codigo de saida |
| **`SK-07`** | ✅ | **`CAP-infraestrutura`**, **`ativo`**, custodio **`DEP-OPS`** — **conferido no frontmatter, nao de memoria**. **`1`** de no maximo `3` (`VC-03`) |
| **`SK-13`** | ✅ | **Idempotente quanto ao dado protegido** — `0` bytes na origem, `0` no repositorio. **Terceira forma distinta** de idempotencia no acervo |
| **`SK-14`**, **`SK-15`** | ✅ | `9` passos em ordem, **cada um com produto declarado**; executavel sem consultar o autor |
| **`SK-16`** | ✅ | **Nao decide restaurar em producao** — produz veredito; a decisao e de quem invoca, **depois** |
| **`SK-18`** | ✅ | Criterio por **`MEDICAO`** e **`TESTE`**, com numeros reais ja produzidos |
| **`SK-19`** | ✅ | **Duas** falhas plausiveis-e-erradas, e a segunda e nova no acervo — §4 |
| **`SK-23`** | ✅ | **`7`** normas citadas por identificador, **`0`** reproduzidas |

### 1.2 O que o candidato afirma, CONFERIDO NA FONTE e nao acreditado

| Afirmacao do candidato | Conferencia | Resultado |
|---|---|---|
| `CAP-infraestrutura` e `ativo`, custodio `DEP-OPS` | frontmatter do artefato | ✅ **confere** |
| prova **(c)** `PASSOU`, `16,2 s` | `nxtrack/docs/provas-dos-invariantes-2026-08-03.md` | ✅ **confere** |
| `sha256` `74afde6c…` | idem | ✅ **confere** |
| `15.585` linhas | `nxtrack/docs/INFRA.md` | ✅ **confere** |
| regra `A3`, *"destino novo = backup nao provado"* | `nxtrack/docs/INFRA.md §A3` | ✅ **confere** |
| o instrumento existe | `nxtrack/infra/provas/prova_c_backup_restaura.py` | ✅ **existe** |

> **Candidato que se autodeclara medido nao dispensa a conferencia — a dispensa seria `LV-12`.**
> **`6` de `6` afirmacoes conferidas na fonte, `0` divergentes.**

## 2. `SK-20` — as quatro perguntas de `FND-04 §6.1`, respondidas POR ESCRITO

| Pergunta | Resposta |
|---|---|
| **Ja existe capacidade que faca isto?** | **Nao** — §3 |
| **Ha consumidor nomeado?** | **Sim, `4`:** `DEP-OPS`, `DEP-KMS`, `DEP-GOV`, `DEP-QAR`. **Enumerados, nunca *"todos"*** |
| **Ha necessidade demonstrada?** | **Sim, e de `3` fontes independentes** — abaixo |
| **O ganho e observado ou antecipado?** | **Observado.** `FND-08 §7.1` recusa antecipacao, e **`0`** aqui e antecipado |

| # | Sinal, remedido e nunca herdado | Natureza |
|---|---|---|
| **1** | Prova **(c) `PASSOU`** em `16,2 s`: `74afde6c…` == manifesto · `integrity_check ok` · `4.919.296` B · **`14` tabelas / `15.585` linhas** identicas ao banco vivo · `restic check --read-data` sem erro | **execucao propria, com numero** |
| **2** | **`RD-103`, severidade ALTA** — script apagou o **ponto de retorno declarado de ato `C3` pendente**; **`7`** arquivos sem bytes recuperaveis | **incidente ja ocorrido** |
| **3** | A copia do `nxtrack` — `622` arquivos / `107` MB — esta **em outro disco da MESMA maquina**, e o envio externo esta **retido** | **exposicao corrente** |

## 3. ⚠️ `SK-22` — o enquadramento que QUASE reprovou

**`SK-22` e a regra mais perigosa para este candidato**, e nao por acaso: *"`Skill` quase igual a
outra e sinal de que a diferenca deveria ser **PARAMETRO**, nao artefato novo"*. A primeira `Skill`
do acervo **ja tem modo `--verificar`**, que reconfere uma copia contra o manifesto. **A pergunta
seria: por que isto nao e uma opcao daquela?**

| Eixo | `SKL-custodia-criar-copia-datada` | **Este candidato** |
|---|---|---|
| **Objeto** | arvore de arquivos, na mesma maquina | **repositorio de backup** — cifrado, por snapshot, deduplicado |
| **Contra o que confere** | **o manifesto que ELA MESMA gravou** | manifesto **+ integridade do formato** **+ a ORIGEM VIVA** |
| **O circulo** | ⚠️ **fechado** — copia conferida contra si mesma | ✅ **quebrado pelo passo 7** |
| **Escreve onde** | no destino da copia | **destino descartavel, destruido ao fim** |
| **`Capability`** | `CAP-governanca` | **`CAP-infraestrutura`** |
| **O que produz** | **ponto de retorno** | **veredito sobre a validade de um** |

**Por que NAO e parametro, e o argumento e da propria ficha existente:** **`SKL-custodia-criar-copia-datada`
exclui *"backup externo"* do seu escopo DE PROPRIO PUNHO**. Transformar isto em opcao daquela
**exigiria ampliar o escopo declarado dela** para abranger repositorio cifrado, snapshot, formato de
banco e comparacao com dado vivo — **o que seria `Skill` nova com o nome da antiga**, e nao evita
artefato: **troca criacao por emenda MAIOR** (`SK-25`) de um artefato cujo escopo a exclui.

> **`SK-22` nao reprova, e a distincao que a salva e o passo 7.** Sem ele, as duas conferem *"a
> copia bate com o que se disse dela"*, e **seriam a mesma coisa com dois nomes**. Com ele, uma diz
> *"a copia e coerente"* e a outra diz ***"o dado esta la"***. **Sao afirmacoes diferentes sobre o
> mundo, e e por isso que sao duas `Skill`s.**

## 4. `SK-19` — a segunda falha plausivel e errada e NOVA no acervo

| # | Falha | `Skill` | Natureza |
|---|---|---|---|
| 1 | `VERIFICADO` com arquivo divergente | 1 | falsa **seguranca** |
| 2 | ruido que faz desligarem o portao | 2 | falha de **adocao** |
| 3 | **a copia coerente e VAZIA** | **3** | falsa seguranca — **e os passos 5 e 6 PASSAM** |
| **4** | ⭐ **o veredito que VIAJA** — verde do repositorio `X` lido como prova de `Y` | **3** | **NOVA: a saida esta CORRETA e ENVELHECE** |

**A quarta e de classe diferente das tres anteriores.** Nas outras, ha em algum lugar um
instrumento que errou ou um humano que desligou. **Aqui nao ha erro nenhum:** o veredito era
verdadeiro quando foi emitido, continua verdadeiro sobre o repositorio que o produziu, e **passa a
ser inaplicavel porque o mundo mudou** — trocar o destino e **uma linha de configuracao**.

> **A defesa e estrutural e nao exortativa:** o veredito **carrega o identificador do repositorio e
> a referencia do snapshot**, de modo que **quem consome pode comparar**. **A regra que a sustenta
> ja e da fonte externa: *"destino novo = backup NAO provado"*.**
>
> ⚠️ **Registro para o `ADR` sucessor:** **`SK-19` fala da saida plausivel e errada NO SINGULAR**, e
> em **`2` de `3`** fichas **o singular nao bastou**. Isso e sinal sobre o **enunciado**, nao sobre
> os casos.

## 5. ⭐ `SK-03` — a serie quebra: `3` de `4` reprovados, e o que passou foi o unico escrito sob a regra

| Nome externo | Forma | Veredito | Nome canonico |
|---|---|---|---|
| `backup-datado` | substantivo + adjetivo | ❌ **reprovado** | `custodia-criar-copia-datada` |
| `secret-scan` | ingles, substantivo + substantivo | ❌ **reprovado** | `seguranca-varrer-credencial` |
| **`custodia-provar-restauracao-de-backup`** | **`<dominio>-<verbo>-<objeto>`** | ✅ **PASSA** | **inalterado** |

**`3` de `4` nomes externos reprovados** *(contando as duas primeiras e este)*, **e a excecao nao e
sorte:** e o unico que foi **redigido depois** de `SK-03` existir e ser exercida duas vezes.

> **Isto e o primeiro dado duro da quinta medicao:** a regra que reprovou **`2` de `2`** parou de
> reprovar **exatamente** quando o autor passou a conhece-la. **`SK-03` nao mudou; o candidato
> mudou.**

## 6. ⭐ A quinta medicao — nascer sob as `26` reduziu o retrabalho?

**Sim, e a reducao e de UMA natureza so.** A contagem separa o que caiu do que **nao caiu**.

### 6.1 Os tres defeitos conhecidos, e o que o candidato fez com cada um

| Defeito | O candidato antecipou? | Como | **O defeito sumiu?** |
|---|---|---|---|
| **`SK-09`** *(erro de categoria)* | ✅ **sim** | §0 separa **frontmatter** de **corpo** e satisfaz as duas leituras **sem endossar a soma** | ❌ **NAO.** A ficha **ainda materializa o `gatilho` DUAS vezes** — campo e §1 |
| **`SK-10`** *(nao adverte o custo)* | ✅ **sim** | §11 declara os **`5`** instrumentos **antes** de abrir o rito | ❌ **NAO.** Custou **`5`** artefatos, igual as duas anteriores |
| **`SK-24`** *(sem piso de `n`)* | ✅ **sim** | §11 traz a **aritmetica** de `n = 1, 2, 3` | ⚠️ **parcial** — e trouxe **valores VENCIDOS**, §6.3 |

### 6.2 A contagem, em numeros

| Grandeza | `Skill` 1 | `Skill` 2 | **`Skill` 3** |
|---|---|---|---|
| **Reprovacoes por regra do Framework** | **`1`** *(`SK-03`)* | **`1`** *(`SK-03`)* | ⭐ **`0`** |
| **Correcoes de merito exigidas na transformacao** | nome | nome | **`1`** — o valor vencido de `SK-24` *(§6.3)* |
| **Decisoes de merito deixadas em aberto pelo candidato** | — | — | **`1`**, e **declarada pelo proprio candidato** *(§5 da ficha)* |
| **Campos escritos a mao** *(`RD-122`)* | `2` | `2` | **`2`** — **`0` reducao** |
| **Artefatos do rito** | `5` | `5` | **`5`** — **`0` reducao** |

### 6.3 A unica correcao de merito, isolada

**O candidato declarou `SK-24` com os valores de `n = 2`** — mediana `181,5`, teto `363` — porque
foi escrito **antes** de a terceira instancia existir. **A ficha real mede `n = 3`: mediana `188`,
limiar `376`, propria instancia `231`.**

> **O defeito e da CLASSE que a missao anterior ja nomeou:** *artefato que afirma propriedade que
> ja nao vale* — familia de **`RD-101`**. **E ele e INEVITAVEL neste caso**, e a razao e bonita:
> **o candidato nao podia conhecer a mediana que ele proprio ia mudar.** **Nenhuma quantidade de
> disciplina do autor o evitaria** — so a medicao no momento da admissao.

### 6.4 A conclusao, e ela e mais estreita do que parece

> **Nascer sob as `26` reduz o RETRABALHO DE REDACAO a quase zero — e nao reduz o CUSTO DO RITO em
> nada.**
>
> **`0` reprovacoes por regra, `1` correcao de merito, `1` decisao a tomar** — contra **`1`
> reprovacao de nome** em cada uma das anteriores. **Mas `5` artefatos, `2` campos a mao e `1`
> `gatilho` duplicado permanecem IDENTICOS**, porque **nao dependem do autor: dependem da norma.**
>
> **Produzir candidato na fabrica vale — e vale para uma coisa so.** Poupa a redacao, o vaivem e a
> reprovacao de forma. **Nao poupa instrumento**, e quem esperar reducao de custo do rito por essa
> via **vai medir `5` de novo**, como se mediu aqui pela terceira vez.

## 7. Impacto

| Frente | Efeito |
|---|---|
| **Acervo** | **`+5`** artefatos. **`skills/` passa de `2` para `3`** |
| **`FND-*`, `TPL-skill`, `ADR-0033`** | **`0` bytes.** `RD-122` **exercido pela terceira vez, nao sanado** |
| **Codigo** | **`0` bytes.** A implementacao permanece no `nxtrack`; **o canonico recebe a ficha** |
| **`nxtrack`** | **`0` bytes escritos.** Lido em **somente leitura** |
| **Segundo candidato da F8** | **NAO admitido** — *um por missao*. Segue fora, intacto |
| **Atos** | **`0`** — `FND-09 §8.2` linha `SKL`, *Ratifica* = `—` |

## 8. Riscos

| # | Risco | Severidade | Tratamento |
|---|---|---|---|
| `R1` | **O veredito que viaja** *(§4)* | **Alta** | Ancoragem obrigatoria na saida + a regra *"destino novo = backup nao provado"*. ⚠️ **Nao ha portao que a imponha** — o consumidor precisa comparar |
| `R2` | A `Skill` restaurar sobre dado vivo | **Alta** | Passo `1` recusa destino que **contenha ou seja ancestral de** caminho vivo, **antes** de qualquer escrita |
| `R3` | `0` degradado lido como *"o dado esta la"* | **Alta** | §5 da ficha **decide** a saida e **imprime** a degradacao; §6 declara a leitura obrigatoria |
| `R4` | `SK-24` nao disparar em `n = 3` e isso ser lido como *"regra sa"* | Media | `ADR-0036 §1.3` separa **poder disparar** de **disparar** |
| `R5` | A reducao de retrabalho ser generalizada para *"a fabrica barateia o rito"* | Media | §6.4 mede as duas coisas separadamente e conclui **`0`** de um lado |

## 9. Decisao proposta

**Criar `SKL-custodia-provar-restauracao-de-backup`** por `ADR-0036`, classe **`C2 · Tipo 2`**,
aprovacao **`DEP-EXE`** com parecer **`DEP-GOV`**, **sem ato**.
