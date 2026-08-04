---
id: PT-2026-023-terceira-skill
titulo: Relatorio de transicao — Missao 1.13.13, a terceira Skill do acervo e o piso de n de SK-24
tipo: relatorio-de-transicao
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-08-03
atualizado_em: 2026-08-03
revisao_prevista: null
decisoes_relacionadas: [ADR-0033, ADR-0034, ADR-0035, ADR-0036]
substitui: []
substituido_por: null
resumo: Cria a terceira Skill do acervo e mede o que so a terceira instancia alcanca — o piso de n de SK-24 provado em 3, SK-09 e SK-10 fechados como defeito do Framework com a hipotese de defeito de leitor eliminada, a razao de SK-21 corrigida, custo do rito confirmado em 5 pela terceira vez, e a primeira medicao do que nascer sob as 26 reduz.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# PT-2026-023 — A terceira `Skill`

**Decisao: `CRIADA`.**

## 1. O despacho foi SUBSTITUIDO em curso de missao, e o registro fica

**Esta missao correu sob dois despachos**, e o registro existe porque apagar o primeiro seria
apagar trabalho medido.

| Despacho | Item 0 | O que esta sessao fez sob ele |
|---|---|---|
| **Original** | *"escolher"* entre `kernel-de-evidencia` e tres alternativas da fabrica | Mediu os **quatro**, **reprovou tres** e escolheu `medidor-de-token`; chegou a redigir `RFC-0031`, `ADR-0036`, `FIT-2026-029` e uma ficha |
| **Substituto** | **candidato FIXADO:** `custodia-provar-restauracao-de-backup`, da **F8** | Retirou a ficha anterior, reescreveu os tres instrumentos sobre o candidato novo |

**O que foi retirado:** `skills/SKL-contexto-estimar-custo-em-token.md`, **criado e apagado dentro
do mesmo `fencing_token` 28, antes de qualquer baseline**. O caminho **volta ao estado do `H-A`**,
onde ele nao existe. `RFC-0031`, `ADR-0036` e `FIT-2026-029` **mantem os identificadores**, porque
**nenhum deles foi publicado em baseline** — nao ha o que superar.

> **O que NAO foi descartado: a medicao.** A algebra de `SK-24`, a analise de `SK-09`/`SK-10` e a
> decomposicao de `SK-21` **independem do candidato** — sao propriedades da **regra**. Foram
> produzidas sob o despacho antigo e **valem sob o novo**.
>
> **E uma medicao do despacho antigo mudou o proprio despacho novo:** esta sessao **contou** a
> familia `RD-53`/`RD-81` e achou **SETIMA**, contra a *"sexta"* que o despacho original enunciava.
> **O despacho substituto ja chegou dizendo *"setima"***. A correcao foi medida **antes** de
> chegar, e nao depois.

## 2. Pre-condicoes — todas verdes, e provadas por conteudo

| # | Pre-condicao | Resultado |
|---|---|---|
| `CV-1` | **Baseline reproduzida ANTES da primeira escrita** | ✅ **`244` · `71.675` · manifesto `055849fe…` · impressao `d07c2994…`**, `IR-BL/5` conferido por `sha256` antes de rodar, **`2`** execucoes, `EXIT=0` nas duas |
| `CV-2` | **`0` deriva desde o token 27** | ✅ **`244/244`** arquivo a arquivo contra o `H-B` do token 27, **diff vazio** |
| `CV-3` | **Copia datada pela PRIMEIRA `Skill`** | ✅ **`625/625`** `sha256` identicos, saida `0`. **Terceiro uso real dela, segundo depois de ser artefato** |
| `CV-4` | **Copia provada por CONTEUDO** | ✅ **`244/244`** contra o `H-A`, diff vazio |
| `CV-5` | **Ponto de retorno por `H-A`** | ✅ `_missao-1-13-13-2026-08-03/evidencia/H-A-ponto-de-partida.txt`, `244` linhas |
| `CV-6` | **Lease antes da primeira escrita** | ✅ **`fencing_token: 28`** |

### 2.1 ⚠️ Precisao sobre `BL-2026-08-03-04`, porque o despacho pede reproduzi-la

**Dos quatro valores publicados, TRES reproduzem direto da arvore viva** — `244`, `71.675` e o
manifesto `055849fe…`. **O quarto — a impressao `f460609b…7ca4` — e por construcao IRREPRODUZIVEL
da arvore viva**, porque foi medido com os quatro campos em **placeholder** (`RD-109`, receita
declarada em §10.27 do catalogo).

> **Nao se afirma aqui que ele reproduziu.** Afirma-se **o que foi medido**: a arvore reproduz
> **exatamente** o `estado_no_fechamento` do token 27, que e o estado de partida declarado — e a
> prova forte nao e a impressao agregada, e sim o **diff vazio de `244` hashes**, que **nomearia o
> arquivo divergente se houvesse**.

### 2.2 O portao de raiz recusou medir a copia — SETIMA ocorrencia, CONTADA

`IR-BL/5` sobre a copia datada: **`EXIT=2`**, *"entrada nao declarada na raiz do acervo:
`MANIFESTO-DA-COPIA.txt`"* — arquivo que **a propria primeira `Skill`** deixa na raiz.

| # | Ocorrencia | Onde |
|---|---|---|
| 1–3 | anteriores *(`_candidatos/`, `products/`, …)* | historico |
| 4 | `.git` / `.gitattributes` na raiz | `PS-2026-017` |
| 5 | `skills/` nascendo | Missao 1.13.11 |
| 6 | `MANIFESTO-DA-COPIA.txt` | Missao 1.13.12 |
| **7** | **`MANIFESTO-DA-COPIA.txt`, de novo** | **esta missao** |

**O instrumento NAO foi alterado para caber** — **`0` bytes em `baseline.sh`** —, e a fidelidade foi
provada por **diff de conteudo**, que e prova mais forte. **A recusa e o portao FUNCIONANDO.**

## 3. Item 0 — o candidato cabe sob as `26`

**Nenhuma das `26` recusa.** Medido **antes** de propor, com poder de **PARAR** — e o despacho e
explicito: candidato escrito sob o Framework que o Framework recusa seria **achado sobre o
Framework**.

**`SK-22` foi o unico que quase reprovou**, isolado em [`RFC-0031 §3`](RFC-0031-terceira-skill-provar-restauracao-de-backup.md):
a primeira `Skill` ja tem modo `--verificar`, e a pergunta seria *"por que isto nao e um
parametro dela?"*. **Nao reprovou, e o que a salva e o passo 7** — comparar com a **origem viva**.
Sem ele, as duas dizem *"a copia bate com o que se disse dela"*; com ele, uma diz *"a copia e
coerente"* e a outra diz **"o dado esta la"**.

**`6` de `6` afirmacoes do candidato conferidas na FONTE**, `0` divergentes — porque candidato que
se autodeclara medido **nao dispensa conferencia**, e dispensa-la seria `LV-12`.

## 4. AS CINCO MEDICOES

### 4.1 — `SK-24` dispara com `n = 3`? **NAO. E pela primeira vez, PODERIA.**

| Grandeza | Valor |
|---|---|
| Instancias | `175` · `188` · **`231`** |
| Mediana | **`188`** |
| Limiar | **`376`** |
| Maior | **`231`** |
| **Veredito** | **nao dispara.** `0` candidatas a especializacao |

**E a diferenca com as duas medicoes anteriores e ESTRUTURAL, nao quantitativa:**

| `n` | Condicao para disparar | Conjunto-solucao |
|---|---|---|
| `1` e `2` | ⟺ **`a < 0`** | ⛔ **VAZIO** |
| **`3`** | **`c > 2b`** | ✅ **NAO VAZIO** |

> **O piso de `n` e `3`, PROVADO** — o primeiro `n` em que a regra pode devolver *"sim"*. **Os dois
> *"nao"* anteriores e este nao sao o mesmo *"nao"*:** aqueles eram impossibilidade algebrica, este
> e **propriedade das instancias**. **A serie util tem `1` elemento**, e esta e a primeira medicao
> informativa de `SK-24` na historia do acervo. **O defeito NAO e *"outro e maior"*: e exatamente o
> previsto, e agora esta medido.**

### 4.2 — `SK-09` e `SK-10` reprovam pela terceira vez? **AS DUAS, E COM A PROVA MAIS FORTE POSSIVEL**

| Regra | `3` de `3` | O que muda nesta |
|---|---|---|
| **`SK-09`** | ❌ | O `gatilho` foi materializado **duas vezes** — **e o autor SABIA**: o candidato escreveu um **§0** so para separar frontmatter de corpo |
| **`SK-10`** | ⚠️ | Custou **`5`** artefatos — **e o candidato ADVERTIU do custo em §11**, e o custo **nao mudou** |

**As tres materias nao compartilham eixo algum** — `CAP` distintas *(`governanca`, `seguranca`,
**`infraestrutura`**)*, custodios distintos, idempotencias distintas, efeitos distintos.

> ### ⭐ Por que a terceira prova mais que a segunda
>
> **Nas duas primeiras, restava a hipotese de defeito de LEITOR** — alguem que nao entendeu `SK-09`,
> alguem que nao percebeu o custo de `C2`. **Aqui o autor conhecia os dois, escreveu contra os dois,
> e os dois ocorreram assim mesmo.**
>
> **Conhecimento nao corrigiu o defeito. Isso elimina a hipotese de leitor e deixa so a de
> ENUNCIADO** — que e precisamente o que o `ADR` sucessor precisa saber para nao errar o remedio.

### 4.3 — `SK-21` e alcancavel? **NAO — e a razao registrada estava incompleta**

| Clausula | Exige | Estado |
|---|---|---|
| **(a)** nao depende de agente | `≥ 1` agente | **`0` agentes** — vacuamente satisfeita |
| **(b)** a cadeia nao tem ciclo | **`≥ 1` DEPENDENCIA entre componentes** | **`0` dependencias** |

**`PT-2026-022` nomeou UM bloqueio onde ha DOIS.** A clausula **(b)** **nao espera agentes: espera
a primeira ARESTA**, e continuaria vazia com `n = 10` se as dez `Skill`s fossem independentes.

⚠️ **E a terceira `Skill` chega mais perto que qualquer anterior sem chegar:** e a **primeira ficha
do acervo que referencia outra `Skill`**, no §Escopo, para dizer o que **nao** faz.
**Referencia de fronteira NAO e aresta de dependencia** — delimitar-se **contra** um vizinho e o
oposto de depender dele.

### 4.4 — Custo em artefatos: **`5` · `5` · `5`. `0` reducao, pela terceira vez**

**E a terceira medicao e a conclusiva**, porque desta vez o candidato **declarou o preco antes** —
e **conhecer o preco nao o desconta**. A causa e normativa: **a classe e do EFEITO** (`AL-01`), e
`FND-04 §6` diz ***"alem do rito da classe"***. **O barato e o ATO — `0` em tres missoes —, nunca o
RITO.**

### 4.5 — ⭐ Nascer sob as `26` reduziu o retrabalho? **SIM, e de UMA natureza so**

| Grandeza | `Skill` 1 | `Skill` 2 | **`Skill` 3** | Veredito |
|---|---|---|---|---|
| **Reprovacoes por regra** | `1` | `1` | ⭐ **`0`** | ✅ **CAIU** |
| Correcoes de merito na transformacao | nome | nome | **`1`** | ✅ caiu |
| Decisoes deixadas em aberto pelo candidato | — | — | **`1`**, e **declarada por ele** | — |
| **Campos a mao** (`RD-122`) | `2` | `2` | **`2`** | ❌ **`0`** |
| **`gatilho` duplicado** | sim | sim | **sim** | ❌ **`0`** |
| **Artefatos do rito** | `5` | `5` | **`5`** | ❌ **`0`** |

**`SK-03` passou pela primeira vez em tres:** `custodia-provar-restauracao-de-backup` **ja e**
`<dominio>-<verbo>-<objeto>`. **`3` de `4` nomes externos reprovados, e o que passou e o unico
escrito sob a regra.** **`SK-03` nao mudou; o candidato mudou.**

**A unica correcao de merito, e ela era INEVITAVEL:** o candidato declarou `SK-24` com os valores de
`n = 2` *(mediana `181,5`, teto `363`)*, porque foi escrito **antes de a terceira instancia
existir**. Familia de **`RD-101`**.

> **Nenhuma disciplina do autor o evitaria: o candidato nao podia conhecer a mediana que ele proprio
> ia mudar.** **Ha uma classe de afirmacao que so pode ser feita no momento da admissao** — e
> `FIT-2026-029 §7` tira a consequencia de portao: **remedir mediana, contador e baseline na
> admissao deve ser passo do RITO, nao zelo do autor.**

> ### A conclusao, mais estreita do que parece
>
> **Produzir candidato na fabrica VALE — e vale para uma coisa so.** Poupa redacao, vaivem e
> reprovacao de forma. **Nao poupa instrumento.** Quem esperar barateamento do rito por essa via
> **medira `5` de novo.** **A distincao entre as duas economias e exatamente a que `SK-10` nao faz.**

## 5. Cobertura das `26` — acumulada

**Contadas regra a regra sobre ESTA ficha, nunca derivadas da contagem anterior.**

| Estado | `n=1` | `n=2` | **`n=3`** | Quais, em `n=3` |
|---|---|---|---|---|
| ✅ Exercidas | `19` | `22` | **`21`** | `SK-01`–`SK-08`, `SK-11`, `SK-13`–`SK-20`, `SK-22`, `SK-23`, `SK-25`, `SK-26` |
| ⚪ Nao aplicadas | `4` | `1` | **`2`** | **`SK-12`** *(nenhuma tentativa de dar ciclo proprio ao gatilho — satisfeita sem ser testada)* · **`SK-21`** |
| ⚠️ Insuficientes | `2` | `2` | **`2`** | `SK-10` · `SK-24` |
| ❌ Defeituosa | `1` | `1` | **`1`** | `SK-09` |
| **Conferencia** | `26` | `26` | **`21+2+2+1 = 26`** | ✅ |

> ⚠️ **A contagem de exercidas CAIU de `22` para `21`, e o motivo nao e regressao:** `SK-12` foi
> **ativamente observada** na segunda `Skill`, que tinha consumidor com `3` dos `4` marcadores de
> ciclo proprio. **Esta ficha nao produz tentativa alguma de cruzar a linha**, e por isso `SK-12`
> aqui e **satisfeita sem ser testada** — que e `nao aplicada`, nao `exercida`. **Contar como
> exercida seria transportar prova de outro caso.**

**Cobertura ACUMULADA nos tres usos: `25` de `26`. `SK-21` continua a unica JAMAIS exercida** — e
agora se sabe **por que**, e o motivo nao se resolve criando `Skill`s. **`0` defeitos NOVOS no
terceiro uso.**

## 6. Observacoes que NAO viram achado novo

| # | Observacao | Por que nao e achado de artefato |
|---|---|---|
| `1` | **`SK-19` fala da saida plausivel-e-errada NO SINGULAR**, e em **`2` de `3`** fichas o singular nao bastou | Materia do **`ADR` sucessor** — `ADR-0033` e `M1` |
| `2` | **A quarta falha plausivel-e-errada e de classe nova:** *o veredito que viaja* — **a saida esta correta e ENVELHECE** | Idem. Nenhum instrumento errou |
| `3` | **Setima ocorrencia de `RD-53`/`RD-81`** | O portao **funcionou**. Instrumento intacto |
| `4` | **`RD-122` exercido pela terceira vez**, agora com autor ciente | Achado **ja inscrito e ABERTO** |
| `5` | **O `H-B` do token 27 foi gravado em ordenacao diferente da do instrumento** *(`02a8c1b7…`, contra a impressao `d07c2994…`)* | **Conteudo identico**, `244/244`. Observacao sobre a **evidencia**, nao sobre o acervo |

## 7. Conferido e NAO corrigido — o numero *"109 itens"*

O despacho manda corrigir *"se estiver la"*. **Nao esta.**

| Medicao | Valor | Instrumento |
|---|---|---|
| *"109 itens"* no acervo | **`0`** | `grep -rn --include=*.md` |
| Qualquer `109` no roadmap | **`0`** | `grep -c` |
| **Controle positivo** — *"itens"* no roadmap | **`6`** | idem — **o instrumento acha o que existe** |
| `109` no catalogo mestre | `18`, e **todas** sao `RD-109`, contagens historicas de `BL-2026-07-29-09` ou numero de linha de achado | inspecao |

> **Zero conferido com controle positivo, nao zero de instrumento morto.** O numero deve ter vivido
> em documento da **F8**, fora do acervo — **e la esta missao nao escreve**.

## 8. O que a missao NAO fez

**`0`** atos · **`0`** Fundacionais emendadas · **`0`** bytes em `TPL-skill` · **`0`** bytes em
`ADR-0033` · **`0`** bytes de codigo no acervo · **`0`** bytes em `baseline.sh` · **`0`** bytes
escritos no `nxtrack` · **`0`** achados novos inscritos · **`ADR` sucessor NAO aberto** ·
**`ADR-0033` NAO promovido a `FND`** · **segundo candidato da F8 NAO admitido** ·
**`GO-TO-SKILLS` EXERCIDO pela terceira vez e NAO liberado** *(`FND-01 §6.2` — exercer nao e
liberar; portoes de sequencia por nome: **2 antes, 2 depois**)*.

## 9. Recomendacao sobre o `ADR` sucessor — **ELA MUDA: ABRIR AGORA**

`PT-2026-022` recomendou **esperar a terceira `Skill`**. **A terceira existe, e a espera acabou.**

| Sinal | Estado |
|---|---|
| `SK-09` | ✅ **maduro** — `3` de `3`, e **sem a hipotese de defeito de leitor** |
| `SK-10` | ✅ **maduro** — `5` · `5` · `5`, com o preco declarado antes na terceira |
| **`SK-24`** | ✅ **MADURO** — **o piso e `3`, provado**, e era **so isto** que faltava |
| **`SK-21`** | ✅ **maduro por tabela** — mesma classe de defeito, remedio comum |
| `SK-19` | ✅ maduro — singular insuficiente em `2` de `3` |

**⛔ E NAO esperar a quarta `Skill`.** Ela **move o limiar** de `SK-24`, mas **nao acrescenta classe
de sinal**: `SK-09`, `SK-10` e o custo repetiram **tres vezes com `0` variacao**, e o terceiro uso
ja produziu a evidencia que a quarta nao produziria — **o autor ciente que erra assim mesmo**.

**O remedio deve ser escrito na forma GERAL**, porque cobre `SK-24` e `SK-21` de uma vez:

> **Toda regra cujo antecedente dependa de POPULACAO ou de ARESTA declara o seu piso; abaixo dele,
> declara-se INAPLICAVEL, nunca satisfeita.** *(A diferenca e operacional: *"satisfeita"* entra em
> `FIT` como ✅ e **desaparece**; *"inaplicavel"* fica visivel e **cobra o piso**.)*

**Acrescentar `SK-19` no plural** e a terceira correcao, medida em `2` de `3` fichas.

⛔ **E o sucessor NAO promove `ADR-0033` a `FND`** — promover e **`C3 · Tipo 1` com ato**, materia do
Fundador.

## 10. Decisao

**`CRIADA`.** A **terceira `Skill`** do acervo existe desde 2026-08-03:
[`SKL-custodia-provar-restauracao-de-backup`](../skills/SKL-custodia-provar-restauracao-de-backup.md),
`C2 · Tipo 2`, **`0` atos**, **`5`** artefatos, sob **`fencing_token` 28**.
