---
id: ADR-0035-segunda-skill-varrer-credencial
titulo: Criar a segunda Skill do acervo — varrer credencial —, e medir o que so a segunda instancia mede
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
decisoes_relacionadas: [ADR-0002, ADR-0033, ADR-0034]
substitui: []
substituido_por: null
classe_mudanca: C2
tipo_decisao: 2
supera: null
superado_por: null
resumo: Cria SKL-seguranca-varrer-credencial, a segunda Skill do acervo, e demonstra que SK-24 e calculavel e incapaz de disparar com duas instancias, que SK-09 e SK-10 reprovam de novo por causa do Framework e nao do caso, e que o custo do rito nao cai.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# ADR-0035: A segunda `Skill` do acervo

## Contexto

[`ADR-0034`](ADR-0034-primeira-skill-copia-datada.md) criou a primeira `Skill` em 2026-08-03 e
converteu as **26** regras de *determinadas* em **observadas**. A observacao devolveu **3
defeitos** — `SK-09` **defeituosa**, `SK-10` e `SK-24` **insuficientes** — e **`n = 1` nao
distingue defeito do Framework de defeito do caso**.

**Tres coisas sao estruturalmente inalcancaveis com uma instancia:** a **mediana** que `SK-24`
exige, a **duplicata** que `SK-22` verifica, e a **repeticao** que separa regra defeituosa de
caso infeliz.

## Decisao

**Criar [`SKL-seguranca-varrer-credencial`](../skills/SKL-seguranca-varrer-credencial.md)**, a
partir da capacidade `secret-scan`, construida e medida **fora do acervo**.

**O candidato ja estava escolhido:** [`RFC-0029 §4`](../rfcs/RFC-0029-primeira-skill-copia-datada.md)
declarou que `secret-scan` **nao foi recusada por merito — foi ordem**, e a fixou como *"candidata
natural a segunda `Skill`"*. O que [`RFC-0030 §2`](../rfcs/RFC-0030-segunda-skill-varrer-credencial.md)
acrescenta e o **sinal medido hoje**, porque `SK-20` recusa sinal herdado de outro documento.

## Classe — e ela e IDENTICA a da primeira, o que ja e uma medicao

| Variavel | Valor | Fundamento |
|---|---|---|
| **Classe** | **`C2`** | `FND-04 §6`, linha *Skill* — **a classe do tipo** |
| **Instrumento** | **`RFC` → `ADR`** | `FND-04 §2.1`. `FND-04 §6` diz *"**alem** do rito da classe"* |
| **Tipo** | **`2`** | `FND-04 §2.2`. Reversivel |
| **Aprova** | **DEP-EXE** | `FND-09 §8.2` linha `SKL` |
| **Ratifica** | **—** | `FND-09 §8.2` linha `SKL`. **`0` atos** |
| **Pre-condicao universal I** | ✅ | `CAP-seguranca`, **`ativo`**, custodio DEP-QAR (`VC-01`, `FND-08 §8`) |
| **Pre-condicao universal II** | ✅ | `SKL` consta do Meta Model — `FND-09 §E-13` |

**Custo do rito: `5` artefatos.** **Exatamente o mesmo da primeira**, e o mesmo de `SPC-001`.
**Ver §5 — e o custo e a quarta medicao desta decisao.**

## 1. `SK-24` — a medicao que so a segunda instancia permite, e o resultado nao e o esperado

**`SK-24`** manda que *"`Skill` que ultrapasse **o dobro da mediana do seu tipo** e candidata a
especializacao"*. `FIT-2026-027 §4` e `PT-2026-021 §4` a classificaram **insuficiente** por ser
*"incalculavel com `1` instancia"*, decidindo *"so a partir da terceira"*. **Com `n = 2`, o teste
foi calculado. O resultado corrige o diagnostico e mantem a conclusao.**

### 1.1 O calculo, com os valores medidos

| `Skill` | Linhas *(`wc -l`, 2026-08-03)* |
|---|---:|
| `SKL-custodia-criar-copia-datada` | **175** |
| `SKL-seguranca-varrer-credencial` | **188** |
| **Mediana do tipo `SKL`** | **181,5** |
| **Dobro da mediana — o limiar de `SK-24`** | **363** |
| **Maior instancia** | **188** |
| **Alguma ultrapassa?** | **Nao.** `188 < 363` |

### 1.2 E a demonstracao de que o `Nao` acima **nao depende destes numeros**

**Sejam `a ≤ b` os tamanhos das duas unicas instancias, ambos positivos.** A mediana e
`m = (a + b) / 2`, logo `2m = a + b`. O teste dispara se `b > 2m`, isto e, se **`b > a + b`** —
o que exige **`a < 0`**. **Tamanho de artefato e positivo. O teste nao pode disparar para valor
nenhum.**

| `n` | A mediana existe? | O teste pode disparar? | Por que |
|---:|---|---|---|
| **1** | **Sim** — mediana de `{v}` e `v` | **Nao** | `v > 2v` exige `v < 0` |
| **2** | **Sim** — `(a+b)/2` | **Nao** | `b > a+b` exige `a < 0` |
| **3** | Sim — `b` | **Sim** | `c > 2b` e possivel *(ex.: `10, 10, 30`)* |

### 1.3 O que isto muda no diagnostico anterior — e o que nao muda

> **`SK-24` nunca foi *incalculavel*.** A mediana de um conjunto de um elemento **e** esse
> elemento; o teste era calculavel desde a primeira `Skill`. **O defeito e outro, e e maior: o
> teste e VAZIO por construcao ate `n = 3`** — devolve *"nao"* para qualquer entrada, e um teste
> que so pode devolver uma resposta **nao esta medindo nada**.
>
> **A conclusao de `PT-2026-021` — *"so decide a partir da terceira `Skill`"* — estava CERTA, e
> agora esta PROVADA em vez de conjecturada.** A justificativa e que estava imprecisa.
>
> **Corrigir o diagnostico em silencio seria a familia de `RD-101`.** Fica declarado aqui.

**Consequencia normativa, e ela e do Framework e nao do caso:** `SK-24` **nao declara o piso de
`n` abaixo do qual seu proprio teste nao vale**. Uma regra que se aplica a **todo o tipo** desde a
primeira instancia, e que **so passa a discriminar na terceira**, esta **incompleta no enunciado**.
**Materia de `ADR` sucessor — que esta decisao NAO abre.**

## 2. `SK-09` e `SK-10` — o defeito e do Framework, nao do caso

**O teste e simples e so `n = 2` o permite: o defeito reaparece num caso sem nenhuma relacao com o
primeiro?**

| Regra | Reprovou de novo? | O que isso decide |
|---|---|---|
| **`SK-09`** — *"os ONZE do template **mais o gatilho**: doze"* | ✅ **sim, identicamente** | O erro de categoria **esta no enunciado**: `gatilho` e **atributo de frontmatter** (`FND-09 §E-13`, `SK-06`) e os `11` sao **blocos de corpo**. Esta ficha **tambem** teve de materializar o gatilho **duas vezes** — campo e §1. **Duas capacidades sem nada em comum, mesmo efeito: o defeito e da REGRA** |
| **`SK-10`** — autoridade derivada, **sem advertir** que `C2` arrasta `RFC` → `ADR` | ✅ **sim, e o custo comprova** | A segunda `Skill` custou **`5`** artefatos, os mesmos da primeira. **A leitura *"Skill e barata"* sobrevive intacta ao segundo uso**, porque nada no enunciado a contradiz |
| **`RD-122`** — `TPL-skill` sem `capabilities` e `gatilho` | ✅ **exercido pela segunda vez** | Com `1` ficha era peculiaridade possivel; **com `2`, e propriedade do template**. **Continua ABERTO e NAO sanado aqui** |

**Nenhum dos tres era defeito do caso.** `backup-datado` e `secret-scan` nao compartilham materia,
`Capability`, consumidor, idempotencia nem modo de falha — e os tres defeitos reapareceram iguais.

## 3. O que a segunda instancia exerceu e a primeira nao pôde

| Regra | Na primeira | Nesta | O que so `n = 2` alcanca |
|---|---|---|---|
| **`SK-05`** | ➖ *"nenhuma confusao surgiu"* | ✅ **exercida** | A forma externa **e** um arquivo de prompt com frases-gatilho, **reusado por `2` consumidores** — e `FND-10 §4.8` resolve: *"prompt reusado por 2+ componentes JA E Skill"*. **`0` tipos novos** |
| **`SK-12`** | ➖ *"nenhuma tentativa de cruzar a linha"* | ✅ **exercida — primeira observacao real** | Existe um consumidor com **`3` dos `4`** marcadores de *"ciclo de vida independente"* — identificador, citabilidade e autoridade proprios. **E `SK-12` nao e violada, porque a superficie vive no CONSUMIDOR**, que e onde a regra manda. **`L3` de `ADR-0033` deixa de ser derivacao sem experiencia** |
| **`SK-22`** | ➖ *"`1` Skill, nada a duplicar"* | ✅ **exercida** | Havia **o que** comparar. Conferido no catalogo: **`0` passos comuns, `0` saidas comuns, `CAP` distintas** |
| **`SK-24`** | ⚠️ insuficiente, *"incalculavel"* | ✅ **calculada** | §1 — e o resultado corrige o diagnostico |
| **`SK-13`** | exercida no ramo **NAO idempotente** | exercida no ramo **IDEMPOTENTE** | **Os dois ramos da regra estao cobertos.** A idempotencia **nao e propriedade do tipo `SKL`** — e o que `n = 1` nao podia mostrar |
| **`SK-04`** | exercida sem tensao | exercida **contra um portao real** | O consumidor mais forte **e literalmente um portao**, e a regra ainda assim classifica `SKL` — porque o portao e **do consumidor**, e `FND-10 §4.8` preve *"etapa de `WFL`"* como acionamento |
| **`SK-19`** | uma falha plausivel e errada | **duas** | A segunda — **ruido que faz desligar o portao** — **nao e falha de deteccao, e de adocao**, e destroi a protecao sem errar um veredito |

**`SK-21` continua parcialmente nao exercida:** **`0` agentes existem**, de modo que a clausula
*"nao depende de agente"* segue sem caso discriminante. **A clausula *"sem ciclo"* passa a ser
verificavel** e passa: **`2` `Skill`s, `0` dependencias entre elas, `0` ciclos**.

## 4. O custo nao caiu — e a conclusao e sobre o rito

| Missao | `Skill` | Artefatos do rito |
|---|---|---:|
| 1.13.11 | primeira | **5** |
| **1.13.12** | **segunda** | **5** |

**`0` reducao.** O rito de `C2` — `RFC` → `ADR`, mais a ficha, mais `FIT` obrigatorio por `QG-6`,
mais o registro — **nao aprende com a repeticao**, porque nenhuma de suas partes e funcao da
novidade. **O custo e do RITO, nao da novidade** — e isso confirma `SK-10` pelo lado da medicao,
nao so pelo da leitura.

> **O que poderia ter caido e nao caiu:** nada no rito e dispensavel por precedente. `FND-04 §6`
> diz *"alem do rito da classe"*, e a classe e do **efeito** (`AL-01`), que e o mesmo na primeira e
> na segunda. **Barganhar o rito por familiaridade seria decidir por economia**, e e exatamente o
> que `ADR-0033` recusou ao escolher a sede.

## 5. O que este ADR NAO faz

| # | Nao faz | Verificacao |
|---|---|---|
| **N1** | **Nao abre o `ADR` sucessor de `ADR-0033`** | Os **3** defeitos ficam **declarados e nao sanados**. `SK-24` so agora ficou medida, e **corrigir com o primeiro sinal e corrigir sem serie** |
| **N2** | **Nao promove `ADR-0033` a `FND`** | `C3 · Tipo 1` **com ato** — precedente `ADR-0022`. **O sinal dobrou; a decisao continua sendo de quem detem a materia** |
| **N3** | **Nao emenda `TPL-skill` nem sana `RD-122`** | **`0` bytes** em `TPL-skill`. O achado e **exercido pela segunda vez**, nao corrigido |
| **N4** | **Nao move codigo para o acervo** | **`0` bytes** de implementacao. A ficha **cita** o caminho externo |
| **N5** | **Nao cria campo novo** | `capabilities` e `gatilho` sao **atributos minimos** de `FND-09 §E-13` (`AC-07`) |
| **N6** | **Nao LIBERA `GO-TO-SKILLS`** | **Exercer duas vezes nao e liberar.** Liberar portao e ato de autoridade (`FND-01 §6.2`). Portoes de sequencia medidos **por nome**: `GO-TO-SPECS` e `GO-TO-SKILLS` — **2 antes, 2 depois** |
| **N7** | **Nao cria entidade, tipo, template, diretorio, papel nem portao** | `SKL` e `skills/` ja existem. `QG-0`–`QG-6`: **7 antes, 7 depois** |
| **N8** | **Nao reabre o tipo `Command`** | §3: a superficie com marcadores de ciclo proprio vive **no consumidor, fora do acervo**. O gatilho de `FND-10 §4.8` segue **nao satisfeito** — e agora isso e **observado** |
| **N9** | **Nao admite os outros candidatos** | `kernel-de-evidencia` e os demais seguem fora do acervo, intactos |

## Consequencias

| Para quem | O que muda |
|---|---|
| **Qualquer DEP** | `PI-08` e `LV-02` passam a ter **instrumento nomeado** com codigo de saida, em vez de conferencia por leitura |
| **DEP-QAR** | O veto por credencial em pacote de contexto (`FND-02`, caso `EX-2`) passa a ter **metodo** |
| **`ADR-0033`** | **`0` bytes**, e **`3` defeitos confirmados como do Framework**. Seu gatilho de revisao segue disparado, agora com serie de `2` |
| **`SK-24`** | Deixa de ser *"insuficiente por incalculavel"* e passa a **defeito de dominio declarado**: o enunciado nao fixa o piso de `n` abaixo do qual nao vale |
| **Quem for criar a terceira `Skill`** | **Sera a primeira em que `SK-24` pode devolver *"sim"***, e a primeira medicao real de dispersao do tipo |

## Rastreabilidade

| Campo | Conteudo |
|---|---|
| **Origem** | [RFC-0030](../rfcs/RFC-0030-segunda-skill-varrer-credencial.md) |
| **Framework** | [ADR-0033](ADR-0033-framework-de-skills.md) |
| **Precedente de rito** | [ADR-0034](ADR-0034-primeira-skill-copia-datada.md) — mesmo custo, mesma classe |
| **Objeto criado** | [`SKL-seguranca-varrer-credencial`](../skills/SKL-seguranca-varrer-credencial.md) |
| **Aptidao** | [FIT-2026-028](../governance/fitness/FIT-2026-028-segunda-skill.md) |
| **Registro** | [PT-2026-022](../governance/relatorio-transicao-2026-08-03-segunda-skill.md) |
| **Achados que NAO fecha** | `RD-122` · `RD-123` · `RD-124` · `RD-116` · `RD-103` |
