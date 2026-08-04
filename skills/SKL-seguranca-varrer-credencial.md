---
id: SKL-seguranca-varrer-credencial
titulo: Varrer texto e codigo atras de credencial exposta antes de commitar, publicar ou colar em contexto
tipo: skill
versao: 1.0.0
status: ativo
camada_memoria: nao-aplicavel
autor: DEP-GOV
proprietario: DEP-KMS
aprovador: DEP-EXE
criado_em: 2026-08-03
atualizado_em: 2026-08-03
revisao_prevista: 2027-02-03
decisoes_relacionadas: [ADR-0033, ADR-0035]
substitui: []
substituido_por: null
resumo: Varre texto e codigo atras de credencial exposta — chave de fornecedor, token, senha em URL, chave privada, JWT — e devolve veredito por achado sem nunca imprimir o segredo inteiro, para que PI-08 e LV-02 deixem de depender de leitura humana.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
capabilities: [CAP-seguranca]
gatilho: invocacao por papel ou etapa de fluxo, antes de commitar, publicar ou expor contexto — ver §1
---

# Varrer credencial (`SKL-seguranca-varrer-credencial`)

> **Credencial vaza por descuido, nao por ataque.**

**`PI-08` e `LV-02` sao absolutos e nao tem instrumento.** Ate aqui, *"nenhuma credencial em texto"*
era afirmacao **conferida por leitura** — e leitura humana e o metodo que falha exatamente onde a
credencial se esconde: dentro de crase, no meio de URL, num `.env` que ninguem abriu.

> ### ⚠️ Dois campos foram escritos A MAO — pela SEGUNDA vez, e a repeticao e o dado
>
> `capabilities` e `gatilho` **continuam ausentes do esqueleto de `TPL-skill`**. Sao exigidos por
> **`FND-09 §E-13`** *(atributos minimos)* e por **`SK-06`**. **Escrever a mao NAO cria campo
> novo** (`AC-07`). **`RD-122`, ABERTO — exercido pela segunda vez e NAO sanado.** Na primeira
> `Skill` isso podia ser peculiaridade do caso; **com duas fichas, e propriedade do template.**

## Escopo

| Item | Definicao |
|---|---|
| **Aplica-se a** | Qualquer arvore de **texto e codigo**, antes de **commitar**, **publicar**, **colar em pacote de contexto**, **anexar a relatorio** ou **revisar diff de terceiro** |
| **NAO se aplica a** | **Binario, PDF e imagem** *(nao ha texto a ler)* · **revogar ou rotacionar** — achou, quem detem a credencial revoga *(`PI-08`)* · **historico do versionador**, que exige varrer os blobs de todos os commits e e invocacao propria · **segredo sem nome e sem formato** — limite declarado em §6 |
| **Quem pode usar** | **Qualquer Departamento.** A capacidade **nao pertence a agente algum** (`SK-02`) |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| Autor | **DEP-GOV** | `FND-09 §8.2` linha `SKL` — *qualquer DEP* |
| Proprietario | **DEP-KMS** | Padrao de `TPL-skill` |
| Revisores | **DEP-GOV + DEP-QAR** | `FND-09 §8.2` linha `SKL`; `AC-03` |
| Aprovador | **DEP-EXE** | `FND-09 §8.2` linha `SKL` |
| Ratificacao | **nunca** | `FND-09 §8.2` linha `SKL`, coluna *Ratifica* = `—` |

## 1. Gatilho — `SK-11`

| Campo | Conteudo |
|---|---|
| **O que dispara** | **Invocacao por papel** — antes de commitar · publicar artefato · colar arquivo de configuracao em pacote de contexto · revisar diff de terceiro — **ou etapa de fluxo** que exija varredura antes de liberar *(`FND-10 §4.8` aloja *"etapa de `WFL`"* entre os acionamentos validos)* |
| **Quem pode disparar** | **Qualquer Departamento** — papel, nunca pessoa. Nao ha papel privilegiado |
| **Pre-condicao** | O alvo **existe** e e legivel; ha ao menos **um** arquivo de extensao de texto ou codigo no escopo — **`0` arquivos e erro de uso** *(saida `2`)*, nunca *"limpo"* |
| **Idempotencia** (`SK-13`) | **IDEMPOTENTE.** Leitura pura: **`0` bytes escritos, `0` efeito externo**. Invocar `n` vezes sobre a mesma arvore devolve o mesmo veredito e o mesmo codigo de saida |

> **Consequencia de `SK-13`, e ela e o oposto da primeira `Skill`:** por ser idempotente e sem
> efeito externo, **esta `Skill` E elegivel a repeticao automatica** — e e o que torna licito
> invoca-la a cada publicacao, sem pergunta. **A idempotencia nao e propriedade do tipo `SKL`:**
> as duas `Skill`s do acervo estao em ramos opostos desta regra.

## 2. Entradas — `SK-17`

| Entrada | Origem | Obrigatoria? |
|---|---|---|
| Caminho do alvo | quem invoca | **sim** |
| Recursao | quem invoca | nao — sem ela, varre so o alvo |
| Filtro *"so defeitos"* | quem invoca | nao — suprime o que nao bloqueia |
| Exibir `PLACEHOLDER` | quem invoca | nao — necessario para **conferir contra gabarito**, e so ai |

**Entrada que a Skill NAO recebe: politica de bloqueio.** O que bloqueia e o que apenas relata **e
decisao de quem invoca**, e vive no consumidor — ver §6 e `SK-16`.

## 3. Procedimento — `SK-14`, `SK-15`

**Executavel por outro papel sem consultar o autor.** Cada passo declara o que produz.

| # | Passo | Produz |
|---|---|---|
| 1 | Coletar os arquivos de **extensao de texto e de codigo** no escopo | a lista de alvos — **vazia ⇒ saida `2`**, nunca *"limpo"* |
| 2 | Para cada linha, casar os **formatos com prefixo publicado pelo fornecedor** | achado **`CREDENCIAL`**, sempre — **recall maximo, por decisao de projeto** |
| 3 | Descartar a linha que **fala sobre** credencial sem conter uma | reducao de ruido de documentacao |
| 4 | Casar **atribuicao a nome sensivel** e classificar o valor | achado **`CREDENCIAL`**, **`SUSPEITA`** ou **`PLACEHOLDER`** |
| 5 | **Ofuscar todo valor** antes de qualquer saida | **prefixo + comprimento**, nunca o valor inteiro |
| 6 | Relatar os achados e devolver o **codigo de saida** | tabela *(caminho, linha, coluna, tipo, prefixo, veredito)* + `0`/`1`/`2` |

**Os tres vereditos, e o que cada um significa:** **`CREDENCIAL`** — formato de fornecedor
reconhecido, **ou** valor sob nome sensivel com comprimento e entropia acima do piso: **bloqueia**.
**`SUSPEITA`** — nome sensivel com valor longo e **baixa** entropia: **olhe**, costuma ser
preenchimento. **`PLACEHOLDER`** — valor que **declara** que ali vai um segredo, ou referencia a
variavel de ambiente ou cofre: **e a forma correta**, e nao e achado.

## 4. Saidas — `SK-17`

| Saida | Destinatario | Formato |
|---|---|---|
| Tabela de achados | quem invoca | caminho · linha · coluna · tipo · **prefixo + comprimento** · veredito |
| **Codigo de saida** | automacao que a invoca | `0` limpo · `1` **ha `CREDENCIAL`** · `2` erro de uso |
| **Nao-saida garantida** | — | **`0` segredos impressos por inteiro, em qualquer circunstancia** — e isto e requisito, nao cortesia (`PI-08`) |

## 5. Criterio de sucesso — `SK-18`

**Metodos de verificacao: `TESTE` e `MEDICAO`** *(dois dos cinco de `SF-14`)*.

**A varredura e boa quando devolve `19` de `19` vereditos corretos contra um corpus rotulado que
contem casos negativos, com `0` falso negativo, `0` falso positivo sobre `PLACEHOLDER` reconhecido
e `0` segredo impresso por inteiro.** *"Nao achou nada"* nao e criterio; *"19 de 19 contra
gabarito, saida `1` porque o corpus tem credencial"* e.

> **O corpus precisa de casos NEGATIVOS, e isso e parte do criterio.** Os tres defeitos corrigidos
> na construcao — nome sensivel sem prefixo passando batido, chave privada classificada como
> preenchimento, e o `_` que impedia o casamento do preenchimento mais comum do mundo — **so
> apareceram porque havia casos que NAO deviam acusar**. Um corpus so de credenciais teria dado
> **`100%`** e escondido os tres.

## 6. Modos de falha conhecidos — `SK-19`

| Natureza | Como reconhecer | O que fazer |
|---|---|---|
| **Erro de uso** *(alvo vazio, ilegivel)* | saida `2` | **E o portao funcionando.** Corrigir a invocacao. **Nunca ler como *"limpo"*** |
| **Falso positivo em documentacao** | `CREDENCIAL` sobre prefixo citado em texto explicativo, **mesmo entre crases** | **Consequencia declarada do recall maximo**, nao defeito. Apontar a varredura para codigo e configuracao |
| ⚠️ **PLAUSIVEL E ERRADA (I) — o falso negativo silencioso** | **Dizer `limpo`, saida `0`, com credencial presente.** Ocorre com **string de alta entropia sem nome sensivel e sem prefixo de fornecedor** | **Como se detecta:** por **`TESTE`** — corpus rotulado com caso negativo obrigatorio. **Medido: `0` falso negativo em `19` de `19`.** **O limite e declarado, nao coberto:** entropia isolada gera falso positivo demais |
| ⚠️ **PLAUSIVEL E ERRADA (II) — o ruido que desliga o portao** | **Relatorio bem-formado, rigoroso na aparencia, com `0` credencial real.** Medido: **`58` achados, `55` bloqueantes, `0` credencial** numa arvore cujo vocabulario de dominio usa `chave`, `token` e `senha` como nomes comuns | **Como se detecta:** por **`MEDICAO`** — contar achados **e** credenciais reais, e comparar. **Portao que grita sem motivo e desligado na terceira vez**, e ai a protecao vale `0`. **Trata-se com politica no consumidor, nunca afrouxando o verificador** |

> **`SK-19` fala da saida plausivel e errada no SINGULAR, e aqui o singular nao bastou.** As duas
> formas sao bem-formadas, as duas passam despercebidas, e **so a primeira e falha de deteccao** —
> a segunda e falha de **adocao**, e destroi a protecao sem nunca errar um veredito.

## 7. Normas aplicaveis — `SK-23`

**Citadas por identificador, nunca reproduzidas.** Em divergencia **prevalece a fonte** (`PJ-03`).

| Norma | O que impoe aqui |
|---|---|
| `PI-08` | **Segredo nunca em texto** — e a materia inteira desta Skill, inclusive o que fazer depois do achado |
| `LV-02` | Credencial em texto claro e **Linha Vermelha**, e **nao admite excecao** |
| `LV-05` | **Reportar como verificado o que nao foi** — dizer *"varrido, limpo"* sem varrer e o caso central |
| `LV-11` | Violacao detectada **exige registro de incidente**; a Skill produz o achado, nao o registro |
| `LV-12` | **Fabricar evidencia** — contagem de achados sem execucao |
| `SF-14` | Os cinco metodos; aqui, **`TESTE`** e **`MEDICAO`** |
| `CE-04` | **Proibido estimar** — `19/19`, `58`, `55`, `476` sao medidos, com instrumento e data |

## 8. Ganho `PI-14` — `SK-20`

| Campo | Conteudo |
|---|---|
| **Ganho declarado** | Transformar *"nenhuma credencial em texto"* de **afirmacao conferida por leitura** em **veredito com codigo de saida** — verificavel por automacao, repetivel sem custo, e **sem nunca expor o proprio segredo que encontra** |
| **SINAL QUE MOTIVOU, e ele e observado, nunca antecipado** | **`14`** tokens deste lease declaram **`0` credenciais** na pos-verificacao — a afirmacao ja e rotina e **nao tinha instrumento proprio**. *"credencial em texto"* aparece em **`22`** artefatos do acervo e *"credencial"* em **`56`**, medidos com **controle positivo** *(`artefato` = `217`)* e **negativo** *(`0`)*. **Fora do acervo:** varredura de historico sobre **`476` blobs** de **`63` commits** em `2` repositorios, e **portao em producao que falha FECHADO**, com **`8/8`** casos — `4` de controle positivo e `2` de negativo |
| **A pergunta que `FND-08 §7.1` obriga** | *"Ha sinal, ou e antecipacao?"* — **ha sinal, e ele e de tres fontes independentes**: o proprio lease, o acervo e um consumidor em producao |
| **Data de reavaliacao** | **2027-02-03** |

## 9. Criterio de descontinuacao — `SK-25`

| Condicao | Sinal observavel | Substituto previsto |
|---|---|---|
| O versionador passar a barrar credencial **antes** do commit, com verificacao equivalente | Portao nativo com corpus rotulado e **falha fechada** | Esse portao |
| A varredura passar a produzir **mais ruido que sinal** de forma irreparavel por politica | Achados reais / achados totais **abaixo do que o consumidor tolera**, medido e nao estimado | Deteccao por formato **apenas**, com a atribuicao nomeada aposentada |
| **Se nenhum substituto existir** | — | **A organizacao volta a conferir `PI-08` por leitura humana**, e isso e **decisao**, nao omissao |

## 10. Rastreabilidade — `SK-09`

| Campo | Conteudo |
|---|---|
| **Capability** | [`CAP-seguranca`](../capabilities/CAP-seguranca.md) — **`ativo`**, custodio **DEP-QAR** *(`SK-07`, `VC-01`)*. **1 de no maximo 3** (`VC-03`) |
| **Consumidores nomeados** | **DEP-QAR** *(veto por credencial em pacote de contexto — `FND-02` caso `EX-2`)* · **DEP-OPS** *(publicacao e deploy)* · **DEP-KMS** *(custodia de memoria e pacote de contexto)* · **DEP-GOV** *(pos-verificacao de missao)*. **Enumerados, nunca *"todos"*** |
| **Origem** | [RFC-0030](../rfcs/RFC-0030-segunda-skill-varrer-credencial.md) → [ADR-0035](../decisions/ADR-0035-segunda-skill-varrer-credencial.md) |
| **Framework** | [ADR-0033](../decisions/ADR-0033-framework-de-skills.md) — `SK-01` a `SK-26` |
| **Implementacao** | **FORA do acervo**, e assim permanece: `_arquivo/projetos-parados/LucaX-Enterprise-Research/_fabrica/skills/secret-scan/`. **O canonico recebe a FICHA, nunca o codigo** |
| **Evidencia medida** | **`19` de `19`** vereditos contra gabarito rotulado · **`0`** falso negativo · **`0`** falso positivo · **`0`** segredo impresso por inteiro *(2026-08-02)*. **`476` blobs** de **`63`** commits varridos no historico de `2` repositorios, **`0`** credencial real *(2026-08-03)*. **`8/8`** casos no portao em producao, com **`4`** controles positivos e **`2`** negativos *(2026-08-03)* |
| **Nao duplica** (`SK-22`) | Conferido no catalogo mestre contra [`SKL-custodia-criar-copia-datada`](SKL-custodia-criar-copia-datada.md): **`0` passos comuns, `0` saidas comuns, `CAP` distintas**. Uma produz **ponto de retorno**; esta produz **veredito sobre exposicao** |
| **Custo de contexto** (`SK-24`) | medido em §4 do catalogo mestre, por `wc -l`. **O teste da regra e calculavel e NAO PODE disparar com `2` instancias** — demonstrado em [`ADR-0035 §4`](../decisions/ADR-0035-segunda-skill-varrer-credencial.md) |

## Historico

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-08-03 | DEP-GOV | **A SEGUNDA `Skill` do acervo.** Recebe a capacidade `secret-scan`, medida fora do acervo *(19/19, 476 blobs, portao em producao 8/8)*, e a expressa sob `SK-01` a `SK-26`. **O nome mudou por `SK-03`, pela SEGUNDA vez consecutiva:** `secret-scan` e ingles e **substantivo + substantivo**, e a regra exige acao `<dominio>-<verbo>-<objeto>` — dai `seguranca-varrer-credencial`. **`capabilities` e `gatilho` escritos a mao**, porque `TPL-skill` os omite *(`RD-122`, aberto, exercido pela segunda vez)*. **`0` bytes de codigo entraram no acervo.** |
