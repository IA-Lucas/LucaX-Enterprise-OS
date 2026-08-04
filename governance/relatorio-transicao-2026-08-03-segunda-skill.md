---
id: PT-2026-022
titulo: Missao 1.13.12 — a SEGUNDA Skill do acervo, e as quatro medicoes que so a segunda instancia permite
tipo: reporte
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-08-03
atualizado_em: 2026-08-03
revisao_prevista: null
decisoes_relacionadas: [ADR-0033, ADR-0034, ADR-0035]
substitui: []
substituido_por: null
resumo: Cria a segunda Skill do acervo e mede o que n=1 nao alcanca — SK-24 calculada e provada vazia ate n=3, SK-09 e SK-10 confirmadas como defeito do Framework e nao do caso, 3 regras exercidas pela primeira vez, e custo de rito inalterado em 5 artefatos.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
---

# PT-2026-022 — A segunda `Skill`

**Decisao: `CRIADA`.**

## 1. Item 0 — o candidato cabe sob `SK-01` a `SK-26`?

**CABE.** O teste foi feito **antes de propor** e tinha poder de **PARAR a missao**: `Skill` que
nao cabe no proprio Framework e **achado sobre o Framework**.

**Nenhuma das 26 recusou o candidato.** **Uma reprovou o nome:** `SK-03` exige acao
`<dominio>-<verbo>-<objeto>`, e `secret-scan` e **ingles** e **substantivo + substantivo** — dai
**`seguranca-varrer-credencial`**. **Segunda vez consecutiva que `SK-03` reprova e corrige o nome
externo do objeto que recebia** — em `2` de `2` candidatos.

**O enquadramento que quase reprovou foi `SK-04`**, porque o consumidor mais forte da capacidade
**e literalmente um portao**. Nao reprovou: o portao e **do consumidor**, o procedimento em si nao
exige dois papeis nem contem portao, e `FND-10 §4.8` preve *"etapa de `WFL`"* entre os
acionamentos validos de uma `SKL`.

## 2. O sinal, medido nesta missao e nao herdado

`SK-20` recusa sinal herdado de outro documento. Medido com **controle positivo** *(`artefato` =
**217** artefatos)* e **negativo** *(termo inexistente = **0**)* — porque zero de instrumento morto
e indistinguivel de zero real:

| Eixo | Medida | Onde |
|---|---:|---|
| *"credencial em texto"* no acervo | **22** artefatos | lista fechada, `grep -rl` |
| *"credencial"* no acervo | **56** artefatos | idem |
| **Uso real no instrumento de governanca** | **14** tokens do lease declaram `0` credenciais | `_leases/LucaX-Enterprise-OS.lease` |
| **Uso real — historico varrido** | **476 blobs** de **63 commits** em **2** repositorios, **`0`** credencial real | missao `F5-PREPARAR-REMOTE`, Ordem 1 |
| **Uso real — producao** | portao que **falha FECHADO** invoca o verificador antes de publicar; **8/8** casos, **4** controles positivos e **2** negativos | `nxtrack`, invariante (a), 2026-08-03 |

## 3. O que foi criado

**[`SKL-seguranca-varrer-credencial`](../skills/SKL-seguranca-varrer-credencial.md)** — a segunda
`Skill` do acervo. **`0` bytes de codigo entraram**: a implementacao permanece em
`_arquivo/projetos-parados/.../_fabrica/skills/secret-scan/`. **O canonico recebeu a ficha.**

**`capabilities` e `gatilho` escritos a mao pela SEGUNDA vez**, porque `TPL-skill` os omite.
**`RD-122` exercido, nao sanado** — e a repeticao muda a natureza do achado: com `1` ficha era
peculiaridade possivel do caso; **com `2` fichas disjuntas, e propriedade do template.**

---

## 4. ⭐ AS QUATRO MEDICOES QUE SO A SEGUNDA INSTANCIA PERMITE

### 4.1 — `SK-24` ficou calculavel? **SIM. E o resultado nao e nenhum dos dois esperados.**

**Calculada, com os valores medidos por `wc -l` em 2026-08-03:**

| | Linhas |
|---|---:|
| `SKL-custodia-criar-copia-datada` | **175** |
| `SKL-seguranca-varrer-credencial` | **188** |
| **Mediana do tipo `SKL`** | **181,5** |
| **Limiar de `SK-24` — o dobro** | **363** |
| **Maior instancia** | **188** |
| **Dispara?** | **NAO** — `188 < 363` |

**E o `NAO` nao depende destes numeros.** Com duas instancias `a ≤ b`, a mediana e `(a+b)/2` e o
limiar e `a + b`. Disparar exigiria **`b > a + b`**, isto e **`a < 0`**. **Tamanho de artefato e
positivo: o teste nao pode disparar para valor nenhum.**

| `n` | Mediana existe? | Pode disparar? |
|---:|---|---|
| **1** | **sim** — mediana de `{v}` e `v` | **nao** — exigiria `v < 0` |
| **2** | **sim** | **nao** — exigiria `a < 0` |
| **3** | sim | **sim** — `c > 2b` e possivel |

> **O despacho previu dois desfechos — *calculavel* ou *incalculavel, logo defeituosa*. A medicao
> caiu num terceiro, e ele e o mais informativo:** `SK-24` e **calculavel desde `n = 1`** e
> **estruturalmente VAZIA ate `n = 3`**. Um teste que so pode devolver *"nao"* **nao esta medindo
> nada**, ainda que calcule.
>
> **Isso corrige o proprio registro anterior.** `PT-2026-021 §4` e `FIT-2026-027 §4` disseram
> *"incalculavel com 1 instancia"* — **a palavra estava errada**, porque a mediana de um elemento
> e esse elemento. **A conclusao — *"so decide a partir da terceira"* — estava CERTA, e agora esta
> PROVADA em vez de conjecturada.** Corrigir em silencio seria a familia de `RD-101`.

**Classificacao mantida: `SK-24` INSUFICIENTE, com a natureza corrigida.** Nao e regra errada — e
regra que **nao declara o piso de `n` abaixo do qual seu proprio teste nao vale**.

### 4.2 — `SK-09` e `SK-10` reprovam de novo? **AS DUAS, IDENTICAMENTE. O defeito e do Framework.**

| Regra | Reprovou de novo? | O que a repeticao decide |
|---|---|---|
| **`SK-09`** | ✅ **sim, identicamente** | Obrigou **esta** ficha a materializar o gatilho **duas vezes** — campo de frontmatter e §1 —, exatamente como a primeira. **O erro de categoria esta no enunciado** |
| **`SK-10`** | ✅ **sim, com prova nova** | A segunda `Skill` custou os mesmos **`5`** artefatos. **A leitura *"Skill e barata"* sobreviveu intacta ao segundo uso**, porque nada no enunciado a contradiz |

**As duas capacidades nao compartilham materia, `Capability`, consumidor, idempotencia nem modo de
falha.** Defeito que reaparece igual em casos disjuntos **e da regra, nao do caso** — e essa
separacao era **inalcancavel com `n = 1`**.

### 4.3 — Quantas regras esta exerceu que a primeira nao exerceu? **TRES, e uma quarta foi calculada.**

| Regra | Na primeira | Nesta | O que so a segunda instancia alcanca |
|---|---|---|---|
| **`SK-05`** | ➖ nao se aplicou | ✅ **exercida** | A forma externa **e** um arquivo de prompt com frases-gatilho, **reusado por `2` consumidores** — e `FND-10 §4.8` resolve sozinho: *"prompt reusado por 2+ componentes JA E Skill"*. **`0` tipos novos** |
| **`SK-12`** | ➖ nao exercida | ✅ **exercida — primeira observacao real** | Existe consumidor com **`3` dos `4`** marcadores de *"ciclo de vida independente"*: identificador, citabilidade e autoridade proprios. **A regra nao e violada, porque a superficie vive no CONSUMIDOR** — que e onde ela manda. **`L3` de `ADR-0033` deixa de ser derivacao sem experiencia** |
| **`SK-22`** | ➖ nao se aplicou | ✅ **exercida** | Havia **o que** comparar. **`0` passos comuns, `0` saidas comuns, `CAP` distintas** |
| **`SK-24`** | ⚠️ *"incalculavel"* | ⚠️ **calculada** | §4.1 |

**Dois ramos de regra tambem foram cobertos pela primeira vez:**

- **`SK-13`** — a primeira `Skill` e **NAO idempotente** *(repetir recusa, protegendo o ponto de
  retorno)*; esta e **IDEMPOTENTE** *(leitura pura)*. **Os dois ramos estao exercidos, e a
  consequencia da regra tambem: aquela NAO e elegivel a repeticao automatica, esta E.** **A
  idempotencia nao e propriedade do tipo `SKL`** — e `n = 1` nao podia mostrar isso.
- **`SK-19`** — a primeira declarou **uma** saida plausivel e errada; esta declarou **duas**, e a
  segunda **nao e falha de deteccao, e de ADOCAO**: relatorio bem-formado com `58` achados, `55`
  bloqueantes e **`0`** credencial real desliga o portao sem nunca errar um veredito.

**Cobertura acumulada do Framework: `25` das `26` regras ja foram exercidas em ao menos uma das
duas fichas.** **A unica nunca exercida e `SK-21`** — *"Skill nao depende de agente"* —, e ela
continua sem caso discriminante porque **`0` agentes existem**. *(Sua clausula *"sem ciclo"* passou
a ser verificavel e passa: `2` `Skill`s, `0` dependencias entre elas, `0` ciclos.)*

### 4.4 — O custo caiu? **NAO. `5` contra `5`. O custo e do RITO, nao da novidade.**

| Missao | `Skill` | Artefatos |
|---|---|---:|
| 1.13.11 | primeira | **5** |
| **1.13.12** | **segunda** | **5** |

**`0` reducao, e nenhuma parte do rito era dispensavel por precedente.** `FND-04 §6` diz *"alem do
rito da classe"*, e a classe e do **efeito** (`AL-01`) — que e o mesmo na primeira e na segunda.
`RFC` → `ADR` por `FND-04 §2.1`; `FIT` obrigatorio por `QG-6`; a ficha; o registro.

> **Isso confirma `SK-10` pelo lado da MEDICAO, e nao so pelo da leitura.** Se o rito aprendesse
> com a repeticao, a insuficiencia de `SK-10` seria transitoria. **Nao aprende.** Barganhar o rito
> por familiaridade seria decidir por economia — o que `ADR-0033` recusou ao escolher a sede.

---

## 5. A reavaliacao das 26 regras com `n = 2`

| # | Regra | Veredito | O que se observou |
|---|---|---|---|
| `SK-01` | reutilizavel, 3 condicoes | ✅ **exercida** | repete *(19/19, 476 blobs, portao em producao)* · verificavel *(codigo de saida contra gabarito)* · **4** papeis nomeados |
| `SK-02` | pertence a organizacao | ✅ **exercida** | O veredito **nao depende de quem invoca** — mesma arvore, mesma saida, qualquer DEP |
| `SK-03` | nome e acao | ✅ **exercida — e REPROVOU** | `secret-scan` **falhou** *(ingles, substantivo + substantivo)* e foi renomeado. **`2` de `2` nomes externos reprovados** |
| `SK-04` | `SKL` × `WFL` | ✅ **exercida contra portao real** | O portao e **do consumidor**; o procedimento nao exige dois papeis nem contem portao → `SKL` |
| `SK-05` | nao e Prompt/Playbook | ✅ **exercida — NOVA** | Prompt reusado por `2` componentes **ja e Skill** (`FND-10 §4.8`). `0` tipos novos |
| `SK-06` | contrato + atributos minimos | ✅ **exercida — revelou o mesmo defeito de template** | `capabilities` e `gatilho` a mao, **segunda vez**. `RD-122` |
| `SK-07` | Capability 1..3 | ✅ **exercida** | `CAP-seguranca`, `ativo`, custodio DEP-QAR. **1 de 3** |
| `SK-08` | *"Quando NAO usar"* | ✅ **exercida** | **6** exclusoes reais, entre elas *"nao substitui rotacao"* e *"nao le binario"* |
| `SK-09` | **12 blocos** | ❌ **DEFEITUOSA — de novo** | Mesmo erro de categoria, mesmo efeito: gatilho materializado **duas vezes**. **Do Framework** |
| `SK-10` | autoridade derivada | ⚠️ **INSUFICIENTE — de novo** | Nao adverte que `C2` arrasta `RFC` → `ADR`. **A segunda custou os mesmos `5`** |
| `SK-11` | gatilho, 3 campos | ✅ **exercida** | Os tres, com papel e nao pessoa; acionamento por papel **ou etapa de fluxo** |
| `SK-12` | gatilho nao cria superficie | ✅ **exercida — NOVA** | **3 de 4** marcadores presentes **no consumidor**, fora do acervo. `Command` segue **nao reaberto**, e agora por observacao |
| `SK-13` | idempotencia | ✅ **exercida — ramo oposto** | **IDEMPOTENTE**, `0` efeito externo → **elegivel a repeticao automatica** |
| `SK-14` | executavel sem o autor | ✅ **exercida** | 6 passos, cada um com saida |
| `SK-15` | passo produz | ✅ **exercida** | **`0`** passos sem saida declarada |
| `SK-16` | nao decide | ✅ **exercida** | **Nao revoga e nao rotaciona** — quem detem a credencial decide, depois do achado |
| `SK-17` | entradas e saidas | ✅ **exercida** | 4 entradas com origem e obrigatoriedade; 3 saidas + **1 nao-saida garantida** *(`0` segredos impressos)* |
| `SK-18` | criterio por `SF-14` | ✅ **exercida** | **Dois** dos cinco metodos — `TESTE` **e** `MEDICAO` |
| `SK-19` | falha **plausivel e errada** | ✅ **exercida — e o singular nao bastou** | **Duas** formas: falso negativo silencioso **e** ruido que desliga o portao. A regra pede o minimo *("incluem obrigatoriamente")*, e o minimo foi superado |
| `SK-20` | 4 perguntas + sinal observado | ✅ **exercida** | Sinal de **3** fontes independentes: lease, acervo e producao. **Nada antecipado** |
| `SK-21` | nao depende de agente | ➖ **nao se aplicou** | **`0` agentes existem.** A clausula *"sem ciclo"* passou a ser verificavel e passa: `2` Skills, `0` dependencias |
| `SK-22` | duplicata | ✅ **exercida — NOVA** | Havia o que comparar. **`0` passos comuns, `0` saidas comuns** |
| `SK-23` | normas por identificador | ✅ **exercida** | **7** normas citadas, **`0`** reproduzidas — inclusive `PI-08` e `LV-02`, cujo texto **nao** foi copiado |
| `SK-24` | custo medido, blocos independentes | ⚠️ **INSUFICIENTE — natureza corrigida** | **Calculada:** mediana `181,5`, limiar `363`, maior `188`. **Nao pode disparar em `n = 2`, para valor nenhum.** Falta o **piso de `n`** no enunciado |
| `SK-25` | `M2`, versao pelo efeito, descontinuacao | ✅ **exercida** | **3** condicoes, com sinal observavel e substituto — inclusive *"a organizacao volta a conferir por leitura humana"* |
| `SK-26` | template, registro, contador | ✅ **exercida** | Contador incrementado **na mesma mudanca** (`CV-04`, `IX-02`) |

### Contagem — e ela fecha

| Veredito | 1ª `Skill` | **2ª `Skill`** | Quais, nesta |
|---|---:|---:|---|
| ✅ **Exercidas sem ressalva** | 19 | **22** | `SK-01`–`SK-08`, `SK-11`–`SK-20`, `SK-22`, `SK-23`, `SK-25`, `SK-26` |
| ➖ **Nao se aplicaram** | 4 | **1** | `SK-21` |
| ⚠️ **Insuficientes** | 2 | **2** | `SK-10`, `SK-24` |
| ❌ **Defeituosa** | 1 | **1** | `SK-09` |
| | **26** | **26** | |

**`0` defeitos NOVOS no segundo uso.** A taxa nao subiu — **`3` em `26` (11,5%)** nas duas —, e o
que mudou e a **firmeza do diagnostico**: com `n = 1` os tres eram hipoteses sobre a regra; com
`n = 2` sao propriedades medidas.

**Comparacao com o precedente:** `SPC-001` achou **5 em 32 (15,6%)** e **nunca teve segunda
instancia**. **O Framework de Skills e o primeiro do acervo a ser medido duas vezes** — e a segunda
medicao e a que distingue defeito de regra de defeito de caso.

## 6. Reconciliacao

| O que | Estado |
|---|---|
| Catalogo mestre — §2, §4.2, §4.5, §4.6, §4.8, §7, §10 | ✅ **mesma mudanca** (`CV-04`, `IX-02`) |
| Indices `M3` — `rfcs`, `decisions`, `fitness` | ✅ mesma mudanca |
| Roadmap canonico | ✅ assinalado **na mesma sessao** |
| Baseline | ✅ **`BL-2026-08-03-04`**, `IR-BL/5`, **2** execucoes |

**Observacao medida sobre a PRIMEIRA `Skill`, e ela e do tipo que so o uso revela.** A copia datada
desta missao foi criada **invocando `SKL-custodia-criar-copia-datada`** — `620/620` verificados,
saida `0`. **Rodar o `IR-BL/5` sobre essa copia RECUSA com `EXIT=2`:** *"entrada nao declarada na
raiz: `MANIFESTO-DA-COPIA.txt`"*. **A saida da `Skill` cai na raiz da copia, e o portao de raiz do
medidor a rejeita** — **sexta ocorrencia da familia `RD-53`/`RD-81`, e a recusa E O PORTAO
FUNCIONANDO**. **O instrumento NAO foi alterado para caber:** a fidelidade foi provada por **diff
de conteudo contra o `H-A`** — **`239/239` identicos, diff vazio** —, que e prova mais forte que a
reproducao de uma impressao agregada. **`0` bytes em `baseline.sh`.**

## 7. O que esta missao NAO fez

- **Nao abriu o `ADR` sucessor de `ADR-0033`** — os **3** defeitos ficam **declarados e nao sanados**.
- **Nao promoveu `ADR-0033` a `FND`** — `C3 · Tipo 1` com ato. **O sinal dobrou; a decisao continua sendo de quem detem a materia.**
- **Nao emendou `TPL-skill`** nem sanou **`RD-122`**, que foi **exercido pela segunda vez**.
- **Nao moveu codigo** — **`0` bytes** de implementacao no acervo.
- **Nao LIBEROU `GO-TO-SKILLS`** — **exercer duas vezes nao e liberar** (`FND-01 §6.2`). Portoes de sequencia **por nome: 2 antes, 2 depois**.
- **Nao alterou o instrumento de medicao** — **`0` bytes** em `baseline.sh`, mesmo diante de `EXIT=2`.
- **Nao admitiu os outros candidatos · nao emendou Fundacional · nao decidiu `RD-116` · `0` atos.**
- **Nao fechou `RD-103`** — nem e materia desta.

## 8. Achados

**`0` novos inscritos.** As observacoes desta missao sao **sobre o proprio Framework** e **sobre um
registro anterior**, e nenhuma e defeito de artefato:

1. **`SK-09` e `SK-10` confirmados como defeito do FRAMEWORK**, por reaparecerem identicos em caso
   disjunto — **materia de `ADR` sucessor**, porque `ADR-0033` e `M1`.
2. **`SK-24` reclassificada na natureza**: nao *"incalculavel"*, e sim **calculavel e vazia ate
   `n = 3`**. **Corrige `PT-2026-021 §4` e `FIT-2026-027 §4`, em declaracao aberta** — deixar a
   palavra errada seria a familia de `RD-101` dentro do proprio registro.
3. **`RD-122` exercido pela segunda vez** e **confirmado como propriedade do template**, nao do caso.
4. **Sexta ocorrencia da familia `RD-53`/`RD-81`** — §6. **Nao inscrita como achado novo:** o portao
   funcionou, o alvo era uma **copia**, e o acervo nao foi afetado.

## 9. Decisao

**`CRIADA`.** A segunda `Skill` do acervo existe desde 2026-08-03. **`GO-TO-SKILLS` continua
EXERCIDO e nao liberado.** **As 26 regras passam de *observadas* a *observadas em serie*, e a serie
e o que distingue defeito de regra de defeito de caso.**

**Recomendacao sobre o `ADR` sucessor: ESPERAR a terceira `Skill`.** `SK-09` e `SK-10` ja tem sinal
maduro; **`SK-24` nao** — o piso de `n` que falta ao enunciado **so se mede quando o teste puder
disparar**, e isso ocorre em `n = 3`. **O sucessor tambem sera `M1`**, e corrigi-lo custaria outro
sucessor: **escrever hoje seria corrigir dois com sinal maduro e um com sinal cego.**
