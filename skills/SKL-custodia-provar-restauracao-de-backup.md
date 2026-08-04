---
id: SKL-custodia-provar-restauracao-de-backup
titulo: Provar que um backup restaura — restaurar em destino descartavel e conferir contra o manifesto E contra a origem viva, antes de acreditar na copia
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
decisoes_relacionadas: [ADR-0033, ADR-0036]
substitui: []
substituido_por: null
resumo: Restaura um snapshot de backup num destino descartavel e devolve veredito por conferencia — sha256 contra o manifesto, integridade do arquivo restaurado e contagem por unidade contra a ORIGEM VIVA — para que "temos backup" deixe de ser afirmacao sobre uma copia que ninguem nunca abriu.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
capabilities: [CAP-infraestrutura]
gatilho: invocacao por papel ou etapa de fluxo, apos instalar backup, apos trocar de destino, e em cadencia declarada — ver §1
---

# Provar restauracao de backup (`SKL-custodia-provar-restauracao-de-backup`)

> **Copiar nao e backup. Backup e a copia da qual se conseguiu voltar.**

**O quarto elo e o que quase nunca e exercido.** Snapshot, manifesto e repositorio cifrado sao
trabalho visivel; **restaurar e abrir o que voltou** e trabalho que so parece necessario depois que
ja nao adianta. Ate aqui, *"temos backup"* era afirmacao sobre um arquivo que **ninguem tinha
aberto**.

> ### ⚠️ Dois campos escritos A MAO pela TERCEIRA vez — e desta vez o autor ja sabia
>
> `capabilities` e `gatilho` **continuam ausentes do esqueleto de `TPL-skill`**, e sao exigidos por
> **`FND-09 §E-13`** *(atributos minimos)* e por **`SK-06`**. **Escrever a mao NAO cria campo
> novo** (`AC-07`). **`RD-122`, ABERTO — exercido pela TERCEIRA vez e NAO sanado.**
>
> **A diferenca desta ficha esta em outro lugar, e e o dado da missao:** o candidato que a originou
> **ja nasceu com os dois campos preenchidos**, porque foi escrito **depois** de as duas primeiras
> pagarem o custo. **O template continua para tras; o autor e que deixou de ser surpreendido.**

> ### ⚠️ `SK-09` — as duas categorias, satisfeitas sem endossar a soma
>
> `SK-09` conta *"doze blocos obrigatorios"* somando **`gatilho`** — que e **atributo de
> frontmatter** — aos **onze blocos de CORPO** do template. **Sao duas categorias, e soma-las e
> erro de categoria**, medido em `ADR-0034` e reconfirmado em `ADR-0035`.
>
> | Categoria | Itens desta ficha |
> |---|---|
> | **Frontmatter** — `FND-03 §4` + `FND-10 §2.2` + os minimos de `FND-09 §E-13` | os universais, mais **`capabilities`** e **`gatilho`** |
> | **Corpo** — os onze blocos do template vigente | Escopo · Responsaveis · §1 a §10 |
>
> **`ADR-0033` e `M1` e nao se emenda:** esta ficha **satisfaz as duas leituras** e **nao repete o
> erro**, mas **nao o corrige** — corrigir exige `ADR` sucessor.

## Escopo

| Item | Definicao |
|---|---|
| **Aplica-se a** | Qualquer **repositorio de backup** de dado sob custodia da organizacao: apos instalar o backup pela primeira vez · **apos trocar de destino** · apos mudar retencao, cifra ou esquema · e na **cadencia que quem custodia declarar** |
| **NAO se aplica a** | **Criar a copia** — quem cria e [`SKL-custodia-criar-copia-datada`](SKL-custodia-criar-copia-datada.md) · **restaurar em producao** — restaura em destino **descartavel** e **RECUSA** destino que contenha dado vivo · **decidir se restaura de verdade** — a decisao e de quem invoca, **depois** do veredito · **provar o agendamento** — que o timer disparou, so o servidor prova · **custodiar o segredo do repositorio** — sem ele o backup e lixo cifrado, e a custodia e ato de quem detem, nunca da `Skill` · **replica e alta disponibilidade** — uma copia provada **nao e um segundo sitio** |
| **Quem pode usar** | **Qualquer Departamento.** A capacidade **nao pertence a agente algum** (`SK-02`) |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| Autor | **DEP-GOV** | `FND-09 §8.2` linha `SKL` — *qualquer DEP* |
| Proprietario | **DEP-KMS** | Padrao de `TPL-skill` |
| Revisores | **DEP-GOV + DEP-QAR** | `FND-09 §8.2` linha `SKL`; `AC-03` |
| Aprovador | **DEP-EXE** | `FND-09 §8.2` linha `SKL` |
| Ratificacao | **nunca** | `FND-09 §8.2` linha `SKL`, coluna *Ratifica* = `—` |

> **`SK-10`: esta tabela e DERIVADA, nunca constitutiva.** Nenhuma celula decide autoridade — todas
> citam a fonte que decide. **`Skill` que fixe aprovador em texto e nao conforme** *(o defeito de
> `RD-23`)*, e o que a torna conforme e a coluna *Fundamento*, nao a coluna *Quem*.

## 1. Gatilho — `SK-11`

| Campo | Conteudo |
|---|---|
| **O que dispara** | **Invocacao por papel** — apos instalar backup · **apos trocar o destino do repositorio** · apos mudar retencao, cifra ou esquema · antes de confiar numa copia para autorizar acao destrutiva — **ou etapa de fluxo** que exija prova de restauracao antes de liberar |
| **Quem pode disparar** | **Qualquer Departamento** — papel, nunca pessoa. Nao ha papel privilegiado |
| **Pre-condicao** | O repositorio **existe** e o segredo que o abre esta acessivel ao invocador · ha **destino descartavel** fora de qualquer caminho de dado vivo · ha **origem viva legivel** para a conferencia cruzada. **Faltando a origem viva, a `Skill` DEGRADA e DECLARA** — §5 e §6 |
| **Idempotencia** (`SK-13`) | ✅ **IDEMPOTENTE QUANTO AO DADO PROTEGIDO — e a qualificacao nao e ressalva, e o conteudo da regra.** **`0` bytes escritos na origem, `0` no repositorio.** Escreve **somente** no destino descartavel, que **destroi ao terminar**. Invocar `n` vezes sobre o mesmo snapshot devolve o mesmo veredito e o mesmo codigo de saida. ⚠️ **Destino descartavel ja ocupado e RECUSA** *(saida `2`)*, nunca sobrescrita — de modo que **execucao anterior interrompida NAO e repetida em silencio** |

> **Consequencia de `SK-13` declarada:** por ser idempotente **quanto ao dado protegido** e sem
> efeito sobre ele, **e elegivel a repeticao automatica** — e e isso que torna licito **agenda-la**.
> **A leitura oposta seria fatal:** `Skill` de restauracao que escrevesse na origem **nao poderia
> ser repetida jamais**, e a distancia entre as duas e **uma linha de destino**.
>
> **Terceira forma de idempotencia registrada no acervo, e as tres sao diferentes:** a primeira
> `Skill` e **NAO idempotente de proposito**; a segunda e **idempotente sem qualificacao**; esta e
> **idempotente sob um recorte declarado**. **A idempotencia nao e propriedade do tipo `SKL`, e
> nem sequer e binaria.**

## 2. Entradas — `SK-17`

| Entrada | Origem | Obrigatoria? |
|---|---|---|
| Identificador do repositorio de backup | quem invoca | **sim** |
| Referencia do snapshot | quem invoca | nao — padrao: **o mais recente** |
| **Destino descartavel** | quem invoca | **sim.** Ausente, a `Skill` **recusa** *(saida `2`)* — **destino padrao seria destino adivinhado** |
| Caminho da origem viva, para conferencia cruzada | quem invoca | nao — **ausente DEGRADA o veredito, e a degradacao e impressa** |
| Manifesto de referencia | o proprio repositorio | **sim**, e e **conferido, nunca acreditado** |

> ⛔ **Entrada que esta `Skill` NAO recebe: o segredo do repositorio.** Ela usa a **referencia** ao
> arquivo de segredo que o ambiente ja expoe, e **nunca recebe valor de credencial por parametro**,
> porque **parametro vaza em `ps` e em log** (`PI-08`, `LV-02`).

## 3. Procedimento — `SK-14`, `SK-15`

**Executavel por outro papel sem consultar o autor.** Cada passo declara o que produz.

| # | Passo | Produz |
|---|---|---|
| 1 | Recusar se o destino descartavel **contiver ou for ancestral de** caminho de dado vivo | saida `2` — **e este passo e o que impede a `Skill` de causar a perda que existe para evitar** |
| 2 | Recusar se o destino descartavel **ja existir e nao estiver vazio** | saida `2` |
| 3 | Listar os snapshots e **imprimir o identificador do repositorio** | a evidencia de **QUAL** repositorio foi provado — sem ela o veredito **nao se ancora** |
| 4 | Restaurar o snapshot escolhido no destino descartavel | a arvore restaurada |
| 5 | Conferir `sha256` e tamanho do restaurado **contra o manifesto** | veredito parcial **`A`** |
| 6 | Abrir o restaurado e rodar a **verificacao de integridade do formato** | veredito parcial **`B`** |
| 7 | Contar por unidade *(tabela, colecao, arquivo)* e comparar **com a ORIGEM VIVA** | veredito parcial **`C`** — ou **`C = DEGRADADO`**, impresso, se a origem nao foi dada |
| 8 | Destruir o destino descartavel e **confirmar a destruicao** | ambiente no estado anterior, com **confirmacao impressa** |
| 9 | Emitir veredito e codigo de saida | os tres vereditos parciais + `0` / `1` / `2` |

> **O passo 7 e o que separa esta `Skill` de um `restore` bem-sucedido.** Os passos 5 e 6 conferem a
> copia **contra si mesma**: **um snapshot vazio, gerado por um backup quebrado, tem manifesto
> coerente e integridade impecavel**. **So a comparacao com a origem viva quebra o circulo.**

## 4. Saidas — `SK-17`

| Saida | Destinatario | Formato |
|---|---|---|
| Veredito por conferencia | quem invoca | tres linhas: `sha256+tamanho` · `integridade` · `contagem × origem viva` |
| **Ancoragem** | quem for reusar o veredito | **identificador do repositorio + referencia do snapshot + data**, sempre |
| **Codigo de saida** | automacao que a invoca | `0` restauracao provada · `1` **divergencia — a copia nao serve** · `2` erro de uso ou recusa |
| **Nao-saida garantida** | — | **`0` bytes escritos na origem · `0` no repositorio · `0` valores de credencial impressos** |

## 5. Criterio de sucesso — `SK-18`

**Metodos de verificacao: `MEDICAO` e `TESTE`** *(dois dos cinco de `SF-14`)*.

**A restauracao esta provada quando as tres conferencias sao verdes NA MESMA EXECUCAO — `sha256` e
tamanho batem com o manifesto, o restaurado abre e passa na verificacao de integridade, e a
contagem por unidade e identica a da origem viva — com os numeros impressos, o repositorio nomeado
e codigo de saida `0`.**

*"O restore rodou sem erro"* **nao e criterio**; *"restaurado `74afde6c…` == manifesto,
`integrity_check ok`, `4.919.296` B, `14` tabelas / `15.585` linhas identicas a origem, repositorio
`nxtrack-restic`, saida `0`"* **e**.

> ### A decisao que o candidato deixou em aberto, e que esta ficha TOMA
>
> **Duas conferencias verdes e uma degradada** — sem origem viva para comparar — **nao e sucesso, e
> tambem nao e falha.** O candidato apresentou as duas saidas possiveis e **recomendou** uma. **Esta
> ficha decide: saida `0`, com a degradacao IMPRESSA em toda saida.**
>
> **Fundamento:** tratar ausencia de origem viva como **falha** tornaria a `Skill` inutil
> **exatamente no caso em que ela mais serve — quando a origem ja morreu**, que e a hipotese para a
> qual o backup existe. **E o custo dessa escolha esta declarado e nao escondido:** um `0`
> degradado le-se **sempre** como *"a copia e coerente consigo mesma"*, **jamais** como *"o dado
> esta la"* — e quem consumir o veredito sem ler a marca cai no modo de falha **(I)** de §6.

## 6. Modos de falha conhecidos — `SK-19`

| Natureza | Como reconhecer | O que fazer |
|---|---|---|
| **Recusa** *(destino ocupado, destino sobre dado vivo, sem destino)* | saida `2`, com a razao escrita | **E o portao funcionando, nao falha.** Corrigir a invocacao |
| **Divergencia real** | `sha256`, integridade ou contagem discordam | **A copia nao serve.** **Nao autorizar acao destrutiva.** Refazer o backup e provar de novo |
| **Degradacao declarada** | `C = DEGRADADO` — nao havia origem viva para comparar | Le-se como ***"a copia e coerente consigo mesma"***, **jamais** como *"o dado esta la"* |
| ⚠️ **PLAUSIVEL E ERRADA (I) — a copia coerente e VAZIA** | **Veredito verde sobre snapshot que nao contem o dado.** Backup quebrado que gerou snapshot vazio produz **manifesto coerente** e **integridade `ok`**: **os passos 5 e 6 PASSAM** | **Como se detecta:** por **`MEDICAO`** — a contagem por unidade contra a **origem viva**, passo 7. **E por isso que o passo 7 nao e opcional e a sua ausencia e IMPRESSA.** **Exercido:** `14` tabelas / `15.585` linhas conferidas contra o banco vivo |
| ⚠️ **PLAUSIVEL E ERRADA (II) — o veredito que VIAJA** | **Veredito verde do repositorio `X` lido como prova do repositorio `Y`.** E a mais provavel na pratica: **trocar o destino e uma linha de configuracao**, e o veredito antigo continua no relatorio — **verdadeiro e inaplicavel** | **Como se detecta:** por **`MEDICAO`** — o veredito **carrega o identificador do repositorio**, e quem o consome **compara**. **Regra que o sustenta: destino novo = backup NAO provado.** Sem a ancoragem, esta `Skill` produz **exatamente a falsa seguranca que existe para destruir** |

> **`SK-19` fala da saida plausivel e errada NO SINGULAR; aqui foram duas, como na segunda `Skill`.**
> **Em `2` de `3` fichas o singular nao bastou** — e a segunda forma, o **veredito que viaja**, nao
> e defeito do instrumento: **a saida esta correta e envelhece**. Achado do Framework, nao do caso.

## 7. Normas aplicaveis — `SK-23`

**Citadas por identificador, nunca reproduzidas.** Em divergencia **prevalece a fonte** (`PJ-03`).

| Norma | O que impoe aqui |
|---|---|
| `LV-12` | **Fabricar evidencia** — dizer *"backup provado"* sem restaurar e o caso central |
| `LV-05` | **Reportar como verificado o que nao foi** — o veredito que viaja de repositorio *(§6-II)* |
| `RB-01` | Rollback declara **responsavel e custo** — este veredito e o **insumo** dessa declaracao |
| `CE-04` | **Proibido estimar** — contagem e `sha256` sao **medidos** |
| `SF-14` | Os cinco metodos; aqui, **`MEDICAO`** e **`TESTE`** |
| `PI-08` · `LV-02` | O segredo do repositorio **nunca** entra por parametro |
| `LV-04` | Evidencia historica **nao se reescreve** — a `Skill` **le** o repositorio, nunca o poda |

## 8. Ganho `PI-14` — `SK-20`

| Campo | Conteudo |
|---|---|
| **Ganho declarado** | Transformar *"temos backup"* de **afirmacao sobre uma copia nunca aberta** em **veredito com codigo de saida, ancorado no repositorio que o produziu** |
| **SINAL QUE MOTIVOU — observado, nunca antecipado, e de TRES fontes independentes** | **(1) Exercicio real, 2026-08-03**, conferido na fonte e nao de memoria: prova **(c) `PASSOU` em `16,2 s`** — restaurado `74afde6c…` == manifesto, `integrity_check ok`, `4.919.296` B, **`14` tabelas / `15.585` linhas** identicas ao banco vivo, `restic check --read-data` sem erro. **(2) `RD-103`, severidade ALTA:** um script apagou o **ponto de retorno declarado de um ato `C3` pendente**, e **`7`** arquivos ficaram sem bytes recuperaveis. **(3) O que continua ABERTO:** a copia do `nxtrack` — `622` arquivos / `107` MB — esta **em outro disco da MESMA maquina**, e o envio ao destino externo esta **retido** enquanto a decisao sobre dado pessoal de terceiro estiver aberta |
| **`FND-08 §7.1` — *"ha sinal, ou e antecipacao?"*** | **Ha sinal, e um deles e execucao propria com numero.** **`0`** antecipado |
| **`FND-04 §6.1` — *"ja existe capacidade que faca isto?"*** | **Nao** — conferido contra as duas `Skill`s existentes, §10 |
| **Data de reavaliacao** | **2027-02-03** |

## 9. Criterio de descontinuacao — `SK-25`

| Condicao | Sinal observavel | Substituto previsto |
|---|---|---|
| A ferramenta de backup provar a restauracao **por construcao** | Verificacao nativa que compare **com o dado vivo**, nao so com o proprio manifesto | Essa verificacao |
| A organizacao deixar de ter dado com **origem viva comparavel** | Todo dado sob custodia passa a ser imutavel e autoverificavel | Verificacao de integridade apenas |
| **Se nenhum substituto existir** | — | **A organizacao volta a acreditar na copia sem abrir**, e isso e **decisao**, nao omissao |

## 10. Rastreabilidade — `SK-09`

| Campo | Conteudo |
|---|---|
| **Capability** | [`CAP-infraestrutura`](../capabilities/CAP-infraestrutura.md) — **`ativo`**, custodio **DEP-OPS**, **conferido no frontmatter e nao de memoria** *(`SK-07`, `VC-01`)*. **1 de no maximo 3** (`VC-03`) |
| **Consumidores nomeados** | **DEP-OPS** *(operacao e deploy)* · **DEP-KMS** *(custodia)* · **DEP-GOV** *(ponto de retorno de ato)* · **DEP-QAR** *(veto por continuidade nao provada)*. **Enumerados, nunca *"todos"*** |
| **Origem** | [RFC-0031](../rfcs/RFC-0031-terceira-skill-provar-restauracao-de-backup.md) → [ADR-0036](../decisions/ADR-0036-terceira-skill-provar-restauracao-de-backup.md) |
| **Origem do merito** | Candidato redigido **fora do acervo** pela **F8**, ja sob `SK-01` a `SK-26`; merito de exercicio real no `nxtrack`, missao **I1**, regra **`A3`** de `docs/INFRA.md` e prova **(c)**. **Lido em somente leitura — `0` bytes escritos la** |
| **Framework** | [ADR-0033](../decisions/ADR-0033-framework-de-skills.md) — `SK-01` a `SK-26` |
| **Implementacao** | **FORA do acervo**, e assim permanece: `nxtrack/infra/provas/prova_c_backup_restaura.py` e `infra/scripts/backup_external.sh`. **O canonico recebe a FICHA, nunca o codigo** |
| **Nao duplica** (`SK-22`) | **Este foi o enquadramento que quase reprovou** — ver [`RFC-0031 §3`](../rfcs/RFC-0031-terceira-skill-provar-restauracao-de-backup.md). Contra [`SKL-custodia-criar-copia-datada`](SKL-custodia-criar-copia-datada.md): **a ficha dela exclui *"backup externo"* do escopo DE PROPRIO PUNHO**, e o `--verificar` dela reconfere **contra o manifesto que ela mesma gravou** — **o circulo que o passo 7 desta quebra**. Uma produz **ponto de retorno**; esta produz **veredito sobre a validade de um**. Contra `SKL-seguranca-varrer-credencial`: **`0`** passos comuns, **`0`** saidas comuns, `CAP` distintas |
| **Custo de contexto** (`SK-24`) | **`231`** linhas, por `wc -l` — `CE-02`, **medido, nunca estimado**. **Mediana do tipo `188`** *(`175`, `188`, `231`)*, limiar **`376`**: **`231` NAO ultrapassa** — **`0`** candidatas a especializacao. ⚠️ **E a MAIOR das tres, e a mais proxima do limiar que o acervo ja teve.** ⭐ **Esta e a instancia que torna `SK-24` capaz de disparar pela primeira vez** — ver [`ADR-0036 §1`](../decisions/ADR-0036-terceira-skill-provar-restauracao-de-backup.md) |

## Historico

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-08-03 | DEP-GOV | **A TERCEIRA `Skill` do acervo — e a primeira nascida de candidato JA ESCRITO sob `SK-01` a `SK-26`.** Recebe a capacidade provada por exercicio real no `nxtrack` *(prova **(c) `PASSOU`**, `16,2 s`)*. **⭐ `SK-03` NAO reprovou o nome pela primeira vez em tres:** `custodia-provar-restauracao-de-backup` ja e `<dominio>-<verbo>-<objeto>`, contra `backup-datado` e `secret-scan`, ambos reprovados — **`3` de `4` nomes externos reprovados, e o que passou foi o unico escrito sob a regra**. **`capabilities` e `gatilho` vieram preenchidos do candidato**, e ainda assim **escritos a mao** *(`RD-122`, terceira ocorrencia, nao sanada)*. **A UNICA decisao de merito que o candidato deixou em aberto foi tomada aqui: §5, `0` com degradacao impressa.** **`0` bytes de codigo entraram no acervo.** |
