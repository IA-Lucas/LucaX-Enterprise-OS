---
name: pacote-para-a-principal-m02
description: "As cinco tarefas que só a máquina PRINCIPAL pode executar (M-02, 2026-08-08) — o que fazer, por quê, e como conferir; escrito para quem não viu a sessão que as levantou"
metadata:
  node_type: memory
  type: project
---

# PACOTE PARA A MÁQUINA PRINCIPAL — 2026-08-08

**Para quem executa:** você não precisa ter visto nenhuma sessão anterior. Cada
bloco abaixo é autocontido. Faça na ordem — a ordem é de consequência, não de
esforço.

**De onde isto vem.** Levantado na máquina **espelho de leitura** (`E:\lucaX`,
secundária) em 2026-08-08. Ela **não tem** os objetos que estas tarefas tocam, e
por isso nenhuma delas foi resolvida lá — foram escritas.

**Regra de leitura, vale para o documento inteiro:** *caminho ausente no espelho
significa **"está na principal"**, nunca "perdido"*. Todo número marcado
**`A VERIFICAR`** não foi medido nesta máquina e **não é fato** — medir antes de
usar.

**Classificação:** duas destas cinco são **incidente** (dano com data, não pendência
de agenda) — as tarefas **1** e **2**. Não são o mesmo tipo de incidente:

- **Tarefa 1 — perda possivelmente CONSUMADA e ainda aberta.** 271 arquivos removidos
  em 2026-08-05 sobre uma justificativa cujo objeto ninguém localiza. Se o objeto não
  estiver na principal, não há o que "fazer": houve perda, e o que resta é a decisão
  do Fundador entre restaurar do commit anterior ou assumi-la. **Não a trate como
  tarefa de localizar.**
- **Tarefa 2 — incidente de vigilância, com causa medida em 2026-08-08 e corrigido no
  espelho.** O sensor de custo morria no import desde o nascimento deste clone
  (2026-08-06) e, por morrer, não parecia falha de conformidade. Corrigido aqui; a
  principal é outro ambiente e não foi medida. **Trouxe junto um achado maior** (2b):
  o teto por arquivo nunca reprovou, em nenhuma versão.

**Atualizado em 2026-08-08 pela missão M-03** — tarefas 2 (causa medida + correção),
3b (arquivo resgatado do `%TEMP%`) e 4a (o git não tem as cópias da época).

**ATUALIZADO EM 2026-08-12 PELA MAQUINA PRINCIPAL — o pacote FECHA, menos o que e decisao:**

| Tarefa | Estado na principal, medido em 2026-08-12 |
|---|---|
| **1** | ✅ **ACHADO:** `E:\LucasIA\_backups\separacao-2026-08-02` existe. **12.783 arquivos / 273.195.090 B** *(registro: 12.782 / 271.809.829 — **os dois ficam**)*. `.db`: **8** `consult/` + **16** `nxtrack/` *(fundamento dizia 9 — os dois ficam)*. Entrada 1 da lista NUNCA-APAGAR atualizada com o caminho real |
| **2** | ✅ sensor **vivo** na principal: `auditar_custo.py` roda sem traceback, `EXIT=0`. ⚠️ **2b/2c seguem DECISAO DO FUNDADOR:** `--relatorio` mostra `🔴 663/660` no `CLAUDE.md` do lucaX; o teto por arquivo segue decorativo; a ordem recomendada nao muda *(corte 2c antes da trava 2b)* |
| **2-fecho** | ✅ **2b e 2c CANCELADOS em 2026-08-12, por decisao do Fundador:** o lucaX vai deixar de existir ("robo sendo desmontado") - manutencao nele nao se paga. O CONCEITO migrou como peca boa: **teto inteligente E4.T no Corpo** *(margem de 5%, sentinela anti-repeticao, reprovacao provada por teste)* |
| **3** | ✅ **FECHADA:** os tres registros vivem em `docs/memoria-da-estacao-espelho/`, commitados e **publicados** *(push do Fundador, 2026-08-12, `origin/master = a258fe5`)*. `docs/` **deixa de ser exemplar unico** |
| **4a** | ✅ **IRRECONCILIAVEL, declarado:** git com **1** unico commit *(`a929d46`, nasce com 322 linhas)*; as **4** copias existentes na maquina tem **322**; **nenhuma fonte de 190 nem de 130 existe**. Os dois enunciados **perderam a fonte** — escolher um seria inventar reconciliacao, e uma linha declarando FECHA *(regra do proprio bloco 4a)* |
| **4b** | ✅ **FECHADA por redacao:** **1 pasta / 5 arquivos / 2 assuntos** *(prova_central 1 + tiers_declarados 4)* — a H2 contou **assuntos**, nao pastas |
| **4c** | ✅ **FECHADA por medicao de contexto:** na principal `E:\LucasIA\Projetos\lucaX` e caminho **VIVO** *(e o proprio repo)*; **`0`** ponteiros para `E:\lucaX` *(caminho do espelho)* nos `.md` do lucaX; o numero **29 nunca teve fonte reproduzivel** e fica declarado como tal |
| **5** | ⏳ segue esperando os vinte setores — **por desenho, nao por pendencia** |

---

## TAREFA 1 — ACHAR O `separacao-2026-08-02` 🔴 INCIDENTE

**O que fazer.** Localizar na máquina principal o diretório
`separacao-2026-08-02`. Medir **tamanho em bytes** e **contagem de arquivos**.
Escrever o **caminho real** na entrada 1 da lista NUNCA-APAGAR (ver tarefa 3, que
diz onde essa lista deve passar a morar).

**Por quê.** O commit **`85df749`** do repositório `lucaX` (2026-08-05, *"higiene:
remove copias velhas de consult e nxtrack"*) **removeu 271 arquivos** justificando-se
com a frase *"backup datado de 283 MB cobre 0 ausentes"*. Esse backup é o
**exemplar único** dos 9 arquivos `.db` do `consult` — dado gitignorado, que
**nunca esteve em git**: não há reflog, não há remoto, não há segunda cópia. Se ele
não existir, os 271 arquivos foram removidos sobre uma justificativa vazia.

**O caminho registrado está morto.** O registro diz
`E:\LucasIA\_backups\separacao-2026-08-02\` (12.782 arquivos / 271.809.829 B,
handoff `docs/handoffs/2026-08-02-separacao-consult-nxtrack-a3-04.md`). Mas
`E:\LucasIA\` **não existe mais** — é o caminho morto do acervo **A-297**.
Procure pelo **nome do diretório**, não pelo caminho antigo.

**Como conferir que deu certo.**
- Achou: a linha da lista tem caminho absoluto que abre, mais tamanho e contagem
  **medidos**, mais a data da medição. Compare com os números registrados acima —
  se divergirem, registre os dois, não escolha um.
- **Não achou em lugar nenhum:** pare e escreva o incidente. Não é "pendência de
  localizar" — é *271 arquivos removidos sem cobertura*, e a decisão do que fazer
  (restaurar do commit anterior a `85df749`, ou assumir a perda) é **do Fundador**.

---

## TAREFA 2 — O SENSOR DE CUSTO MORTO 🔴 INCIDENTE (causa medida em 2026-08-08)

> **Estado no espelho: RESOLVIDO em 2026-08-08 pela M-03.** O bloco continua aqui
> porque a **principal não foi medida** e a causa é de ambiente, não de código —
> cada máquina tem a sua. Confira lá antes de concluir qualquer coisa.

### 2a · A causa, medida (não mais suposta)

O hook `PostToolUse(Edit|Write)` chama `python scripts/auditar_custo.py`
(`.claude/settings.json`). Rodado sem argumento — que é exatamente como o hook o
chama — ele morria antes de avaliar qualquer teto:

```
scripts/auditar_custo.py:193 → scripts/medir_contexto_residente.py:15
ModuleNotFoundError: No module named 'jsonschema'
```

**A pergunta era: ausente, ou presente e não resolvendo? Resposta medida: AUSENTE.**
Nesta máquina há **um único interpretador** — `where python` devolve só
`C:\Users\lucas\AppData\Local\Microsoft\WindowsApps\python.exe`
(PythonSoftwareFoundation 3.11.9), **não existe `.venv`** em `E:\lucaX` nem em
`E:\LucaX-Enterprise-OS`, `pip list` não trazia `jsonschema` e o **cache do pip
estava vazio** dele — ou seja, nenhum sinal de que já tenha sido instalado aqui.
Não é problema de resolução: é pacote que nunca esteve na máquina.

**Desde quando.** `git reflog` mostra que este clone nasceu em
**2026-08-06 15:33** (`clone: from https://github.com/IA-Lucas/lucaX`). O
acoplamento `auditar_custo → medir_contexto_residente → jsonschema` entrou em
**2026-07-26** (commit `927969b`), portanto já vinha no histórico clonado.
**Conclusão: morto desde o primeiro minuto deste clone — 2026-08-06 — e nunca
funcionou nesta máquina.** Na principal a data é outra e não foi medida.

**Por que ninguém viu, e isto é o que importa.** `requirements.txt` já **declara**
`jsonschema>=4` desde 2026-07-26 (A-242 / ADR-089 — descoberto quando a suíte rodou
em Docker pela 1ª vez e deu 16 vermelhas; estava instalada na máquina do CEO *por
arrasto de outro pacote*). Mas **ninguém instala esse arquivo**: a única referência
executável a `requirements.txt` no repo está em `.github/workflows/` — **o CI
instala, a máquina não**. Declarar dependência não a instala. E falha de import
**não se parece com falha de conformidade**: o hook cuspia traceback e saía com
código ≠ 2, então nada bloqueava e ninguém lia.

**A correção aplicada no espelho, e em qual interpretador.**
`python -m pip install "jsonschema>=4"` → `jsonschema-4.26.0` no interpretador
**global do usuário** (`…WindowsApps\PythonSoftwareFoundation.Python.3.11…`),
**não em venv** — deliberadamente: o hook invoca `python` pelo PATH, então um
`.venv` do repositório **não conserta o hook**. Isso repõe conformidade com uma
dependência já declarada; não é decisão nova nem custo novo.

**Reversão vermelha provada:** `pip uninstall -y jsonschema` → o sensor volta a
morrer no mesmo `ModuleNotFoundError`. Reinstalado → roda limpo.
**Controle positivo:** raiz de teste com espinha abaixo do teto → `exit 0`.
**Controle vermelho:** raiz de teste com espinha de 30.012 tok → `🔴 ESPINHA
ESTOUROU: 30012 > 10000`, `exit 2`.

**Alcance do silêncio.** O import é de topo em **3** scripts, que morriam inteiros:
`medir_contexto_residente.py`, `sensor_cadastro_projetos.py`, `validar_cadeira.py`
— os três voltaram a rodar. Outros 4 (`hub_portfolio`, `sensor_conselho`,
`sensor_memoria_camadas`, `sensor_observabilidade`) importam **tarde, dentro de
`try`**: degradavam em silêncio, sem traceback. O `auditar_custo` varre **1.634
arquivos** (13 `custo: espinha`, 22 com `teto:` declarado).

### 2b · ACHADO NOVO E MAIOR — o `teto:` por arquivo **nunca** reprovou

**Consertar o import não devolveu a vigilância que se supunha existir.** Medido em
2026-08-08, com `jsonschema` já instalado:

```
$ python scripts/auditar_custo.py --raiz <copia-do-CLAUDE.md>            # modo HOOK
EXIT=0
$ python scripts/auditar_custo.py --raiz <mesma copia> --relatorio
  🔴   663 tok  (teto  660)  CLAUDE.md
  ✅ Espinha dentro do teto (663/10000)
```

O `🔴` é **glifo de tabela**, calculado em `sinal = "✓" if (teto == 0 or real <=
teto) else "🔴"` — e o modo `--relatorio` **é o único que imprime a tabela, e o
hook nunca o usa**. O caminho de saída do script só reprova por: `contradiz`
(classe inválida / pasta negada), `total > 10.000` (teto duro da espinha inteira),
`memoria_longa` (`CLAUDE.md`/`AGENTS.md` > 200 linhas) e os `problemas` do T1.
**O campo `teto:` do frontmatter não aparece em nenhum deles.** Baixei o teto da
cópia de teste para `100` — estouro de 6× — e o modo hook continuou `exit 0`.

Isto **nunca funcionou**: `git log -S"real <= teto"` devolve um único commit,
`7380a4a` (2026-07-12), o mesmo que criou o script. Não é regressão; é vigilância
que nasceu decorativa. Pior, há documentação afirmando o contrário —
`scripts/sensor_deriva_orcamento.py:28` diz que o `teto:` é *"cobrado por
`auditar_custo.py`"*, e `.claude/rules/token-economy.md` diz que o sensor *"QUEBRA
acima disso"* citando **2.000 tok**, quando `TETO_DURO` no código é **10.000**.

**Acima do teto declarado hoje, e ninguém viu — 3 de 22:**

| tokens | teto | excesso | classe | arquivo |
|---:|---:|---:|---|---|
| 1320 | 400 | +230% | demanda | `My_WorkSpace/Meus_projetos/redes-sociais/CLAUDE.md` |
| 663 | 660 | +0,5% | espinha | `CLAUDE.md` |
| 663 | 660 | +0,5% | espinha | `AGENTS.md` |

**O `AGENTS.md` é achado colateral:** o script o pula de propósito na soma (espelho
do Codex, não carrega no Claude Code), então estoura o próprio teto sem aparecer
nem na tabela.

**DECISÃO DO FUNDADOR, não deste pacote.** Fazer o `teto:` reprovar é uma linha —
mas com `CLAUDE.md` em 663/660 o hook passaria a **bloquear todo `Edit`/`Write` do
repositório** até o arquivo caber, e `CLAUDE.md` está na deny list. **A ordem
correta é: aplicar o corte da 2c primeiro, ligar a trava depois.** Ligar antes
trava a casa.

### 2c · O `CLAUDE.md` em 663 tokens — proposta de corte (não aplicada)

`CLAUDE.md` está na **deny list** (`.claude/settings.json` — `Edit(/CLAUDE.md)`): a
edição é do Fundador. Proposta medida pela **métrica do próprio sensor**
(palavras × 1,5), com o critério de `.claude/rules/README.md:18` — *"A espinha
aponta, nunca copia"*. **Toda linha proposta para corte já está escrita, com mais
detalhe, num arquivo de `.claude/rules/` que também é residente** — hoje o repo
paga as duas.

| linha | texto | economia | onde a regra sobrevive |
|---|---|---:|---|
| **75** | `- **Nada nasce por especulação** — só de despacho ou dor escrita em meta/quadro.md` | 21 | `human-in-the-loop.md:7-8` (com o "repetiu 2×") |
| **41** | `- **Ambíguo, ou sessão não bate com o tipo?** Pergunte — não assuma.` | 19 | `model-routing.md:22` (com o ADR-012) |
| **74** | `- **Todo subagente declara \`tools:\` mínimo.**` | 9 | `subagents.md:17` (com o custo de 12–15K) |
| **36** | `**Escolha ANTES do despacho. Trocar no meio invalida o cache.**` | 15 | `model-routing.md:22` + `context-engineering.md:21` |

```
663 atual
642  cortando 75            margem 18
633  + 74                   margem 27
613  + 41                   margem 47
598  + 36                   margem 62   ← recomendado
```

**Recomendo os quatro (→ 598, margem 62).** Cortar só o suficiente para os 3
tokens deixa margem zero e o próximo ajuste reabre o mesmo incidente. As duas
linhas mais seguras sozinhas (75 + 41) já resolvem: **622, margem 38**. A 36 é a
mais discutível — some a única frase operativa do topo do ROTEAMENTO, sobrando a
grade; sobrevive em dois arquivos residentes, mas é a que mais muda a leitura.
**Alternativa que não corta nada: subir o `teto:`** — decisão do Fundador, e o
precedente **A-174** é contra (a espinha já estourou uma vez por expandir a Lei 9
em seis linhas).

**Como conferir que deu certo (na principal).**
1. `python scripts/auditar_custo.py` roda **sem traceback**. Se der
   `ModuleNotFoundError`, `python -m pip install "jsonschema>=4"` **no
   interpretador que o PATH resolve** — venv não serve para o hook.
2. `python scripts/auditar_custo.py --relatorio` mostra `✓` no `CLAUDE.md`, não `🔴`.
3. Um `Edit`/`Write` qualquer termina sem o hook quebrar.
4. **Não conclua nada do `exit 0` do modo hook** enquanto a 2b não for decidida:
   hoje ele sai 0 mesmo com o teto por arquivo estourado.

---

## TAREFA 3 — REESCREVER OS TRÊS REGISTROS FRÁGEIS

**O que fazer.** Três registros existentes **não sobrevivem**. Cada um precisa
**nascer de novo na principal**, em sede durável e versionada.

| # | Registro | Onde está hoje | Por que não dura |
|---|---|---|---|
| a | **Relatório da M-01** (custo de migrar os setores) | só na transcrição `C:\Users\lucas\.claude\projects\E--LucaX-Enterprise-OS\c333fe55-770b-46f0-b24a-1ee241d27afc.jsonl` | transcrição **não é artefato**, não é catalogada, e ninguém a lê ao abrir o repositório. O diretório `_missao-m-01-*/` que ela diz ter usado **nunca existiu** |
| b | **`RETOMADA-M-01-2026-08-08.md`** (12.713 B) | ~~`%TEMP%\claude\…\scratchpad\`~~ → **resgatado em 2026-08-08** para `C:\Users\lucas\.claude\projects\E--LucaX-Enterprise-OS\memory\retomada-m-01-2026-08-08.md` | saiu do temporário do sistema (já não some numa faxina), mas a sede de memória **não é versionada e é de uma máquina só** — continua exemplar único |
| c | **`NUNCA-APAGAR.md`** (lista de custódia) | `E:\lucaX\.scratch\NUNCA-APAGAR.md` + cópia na sede de memória local | `.scratch/` está **fora do git**; a sede de memória é `C:\Users\lucas\.claude\` e **a principal não a lê**. Exemplar único, numa máquina só |

**Por quê.** Os três descrevem trabalho já feito e decisões já tomadas. Perdê-los não
perde código — perde a **justificativa** do código. E a lista `NUNCA-APAGAR` é o caso
agudo: ela existe para impedir que algo seja apagado, e ela mesma está **a uma faxina
de distância** de se perder.

**O que já foi decidido, e não se reabre.** A lista **saiu** de
`.scratch/NUNCA-APAGAR.md` do repositório `LucaX-Enterprise-OS` por determinação do
Fundador, porque a raiz do acervo era sede errada — `.scratch` não está em
`NAO_ACERVO` (pararia o `IR-BL/3` com erro na próxima baseline, portão de raiz
`RD-53`) e o repositório não tem `.gitignore` (aparecia untracked, colidindo com o
item 5 da própria lista). **Mudou a sede, não a regra:** `NAO_ACERVO` intacta, nenhum
`.gitignore` criado. **Não reabrir essa discussão** — a sede nova é que ainda falta.

**O conteúdo a reescrever já está salvo e legível**, na sede de memória desta máquina:
`C:\Users\lucas\.claude\projects\E--LucaX-Enterprise-OS\memory\` →
[[m-01-relatorio-so-na-transcricao]] (os 6 achados da M-01 conferidos na fonte),
[[nunca-apagar-lista-longa]] (os 7 itens com fundamento medido),
[[nunca-apagar-custodia]] (a versão curta) e
[[contrato-fabrica-acervo-custa-c3]]. **Copie de lá, não da transcrição.**

**Como conferir que deu certo.** Os três conteúdos abrem por caminho versionado, e
`git log` mostra o commit que os criou. Enquanto um deles só existir em `%TEMP%`, em
`.scratch/` ou em `.jsonl` de sessão, a tarefa **não está feita**.

---

## TAREFA 4 — RECONCILIAR TRÊS NÚMEROS QUE DIVERGEM

**O que fazer.** Três divergências que **exigem as duas cópias na mão** e por isso não
fecham no espelho. Fechar cada uma e escrever o número único, ou declarar por escrito
que os dois enunciados descrevem eventos diferentes.

**Por quê.** Nenhum dos três é grave sozinho. Juntos são o sintoma de duas sedes — que
é exatamente o defeito que a regra de backup proíbe criar de novo.

### 4a · `sensor_lei5_juiz.py` — 190 contra 130, ou "60 de diferença"

Dois enunciados do mesmo evento, gravados lado a lado por decisão do Fundador
(2026-08-08): a lista longa diz **190 linhas de um lado e 130 do outro**; a regra
`.claude/rules/git-and-backup.md` do `lucaX` registra o mesmo defeito como
**divergência de 60 linhas entre duas cópias**. Nenhum foi descartado, porque escolher
um sem ter as duas cópias seria **inventar reconciliação**.

⚠️ **Complicação medida em 2026-08-08 no espelho:** o arquivo hoje tem
**322 linhas** (`E:\lucaX\scripts\sensor_lei5_juiz.py`, exemplar único nesta máquina).
**Nenhum dos dois enunciados descreve o arquivo atual** — ele cresceu desde então.
Isso significa que **o arquivo de hoje não reconcilia nada**: comparar contra as 322
produziria um **terceiro valor**, não uma reconciliação. As cópias que interessam são
as **da época**.

🔴 **E o git não as tem. Medido em 2026-08-08, e isto muda a tarefa:**

```
$ git -C E:\lucaX log --format=%h -- scripts/sensor_lei5_juiz.py
a929d46      2026-08-05   322 linhas   "fix(ci): o CI media a maquina, nao o produto"
```

**Um único commit em toda a história, e o arquivo já nasce ali com 322 linhas.** Não
há revisão de 190 nem de 130 para recuperar com `git show`. E no outro repositório
(`E:\LucaX-Enterprise-OS`, remoto `IA-Lucas/LucaX-Enterprise-OS`) **o arquivo não
existe, em nenhum commit**. Como os dois clones compartilham remoto com a principal,
a história lá é a mesma — salvo commit local ainda não empurrado.

**Portanto, na principal, a ordem é esta e não outra:**
1. `git log --follow --format='%h %ad %s' -- scripts/sensor_lei5_juiz.py` — se
   devolver **mais de um commit**, há história local não empurrada: use
   `git show <commit>:scripts/sensor_lei5_juiz.py | wc -l` em cada uma e feche o
   número. Se devolver **só `a929d46`**, o git está descartado como fonte.
2. Descartado o git, a única fonte restante é uma **cópia datada de backup** com o
   arquivo dentro. Procure por nome de diretório (o caminho `E:\LucasIA\` está morto —
   A-297).
3. **Sem nenhuma das duas: declare irreconciliável, por escrito, com esta medição
   junto.** Não escolha 190 nem 130 — escolher sem as cópias é inventar
   reconciliação, que é exatamente o que a decisão do Fundador de 2026-08-08 proibiu
   ao mandar gravar os dois enunciados lado a lado. Uma linha dizendo *"os dois
   enunciados perderam a fonte em tal data"* **fecha** a divergência; um número
   escolhido no chute a **perpetua**.

### 4b · Backups do `SSC-Plus` — 2 ou 1?

O levantamento H2 fala em **2** backups. No espelho há **1 pasta**
(`E:\SSC-Plus\06_p1a\evidencias\backups\`, 48 KB, 5 arquivos), com **dois assuntos**
dentro: `prova_central-*` (1 arquivo) e `tiers_declarados-*` (4 arquivos). Não há
segunda pasta de backup no repositório.

**Hipótese a testar na principal:** a H2 contou *assuntos*, não *pastas*. Se for isso,
não há divergência — há enunciado ambíguo, e o que se corrige é a redação.

### 4c · Os **29 ponteiros** para a sede antiga

`A VERIFICAR` — o número **29 não foi reproduzido nesta máquina**. São ponteiros para o
caminho antigo do vault (`E:\LucasIA\Projetos\lucaX`), que **na principal é o caminho
certo** — por isso não se corrigem daqui: corrigi-los aqui quebraria a principal.

Medições feitas no espelho em 2026-08-08, **que não são a mesma coisa que os 29** e
estão aqui só como ponto de partida:

| Escopo (`.md`) | Arquivos | Ocorrências |
|---|---:|---:|
| `E:\LucaX-Enterprise-OS` — string `LucasIA` | 23 | 36 |
| `E:\lucaX` — string `LucasIA` | 135 | 294 |
| `E:\lucaX` — linhas com `Projetos\lucaX` | — | 91 |

**Precedente que dá o método:** A-297 corrigiu **17** ocorrências operacionais em
runbooks do medAlly — em bytes (`.replace` sobre `read_bytes`, **nunca `sed -i`**,
precedente A-295), conferindo `git diff --numstat` contra `--ignore-cr-at-eol`. E
deixou `docs/SEPARACAO-EXECUTADA.md` **intacto de propósito**: é relatório histórico, o
caminho lá é o fato do dia (Lei 6), e corrigi-lo apagaria a prova de onde o repositório
perdido estava. **Aplique o mesmo critério:** ponteiro operacional se corrige, registro
histórico não.

**Como conferir que deu certo.** Cada um dos três tem, ao final, **um número com data e
método** — ou uma linha escrita dizendo por que continuam sendo dois. Empate silencioso
não fecha.

---

## TAREFA 5 — A MIGRAÇÃO DOS SETORES (só quando os vinte estiverem escritos)

**O que fazer.** **Nada ainda.** Esta tarefa **espera os vinte setores estarem
escritos**. O bloco existe para que, quando a hora chegar, as decisões já tomadas
estejam na mão e não sejam redecididas.

**As decisões já tomadas — não reabrir:**

1. **Esperar os vinte.** Migrar em lote parcial não reduz o custo fixo nem o ato.
2. **O nó de segregação, resolvido pela saída (b):** `DEP-GOV` revisa Carta de
   Departamento e seu `I-3` o impede de revisar a própria; num lote, `DEP-QAR`
   revisaria a de `DEP-GOV` **com a Carta de `DEP-QAR` no mesmo lote**. Saída
   escolhida: **exceção declarada no próprio ato**.
3. **Custo:** fixo `1 ADR + 1 RFC + 1 FIT + 1 REV + 1 ato`; marginal `1 artefato` por
   Departamento. Migrar só os exercidos reduz o marginal — **não** o fixo, **não** o ato.

**Contexto medido que sustenta isso** (conferido na fonte pela retomada de 2026-08-08,
detalhe em [[m-01-relatorio-so-na-transcricao]]):
- **4 de 6 partes cabem na Carta de Departamento:** `POLITICAS`→B3/B4, `PADRAO`→B10 §8,
  `QUALIDADE`→B8 §11, `NAO FAZ`→B3 §4.
- **`CARGOS` e `FERRAMENTAS` não cabem por PROIBIÇÃO**, não por falta de seção —
  `FND-02 §10` (*"nesta fase não existem agentes"*,
  `foundation/02-estrutura-organizacional.md:496`) e `ADR-0011 §5.4`.
- **O rito é UM ato, não nove:** `MSG-2026-0004` ratificou 5 Cartas num ato;
  `MSG-2026-0007` pôs 14 objetos em vigor num ato.
- **Cascata do §13.2:** dobrar o corpo torna os nove perfis de carregamento falsos, e
  `DC-10` obriga remedir todos (`CC-03`, `AL-05`).

**Economia disponível:** o rito `C3` do contrato fábrica↔acervo bate **exatamente** com
esse custo fixo — **o contrato e a migração cabem no mesmo ato**. Ver
[[contrato-fabrica-acervo-custa-c3]] antes de abrir o RFC.

**Como conferir que deu certo.** Os vinte setores escritos; um único ato; a exceção de
segregação **declarada dentro dele**; e os nove perfis de carregamento **remedidos**, não
herdados.

---

## O QUE ESTE DOCUMENTO NÃO DIZ

Nada aqui depende de medição feita no espelho para valer como fato. Onde a máquina não
podia medir, está escrito **`A VERIFICAR`** ou **"medir lá"** — nunca um número
inventado. Em particular: o **tamanho do `separacao-2026-08-02` não foi conferido**
(o objeto não está aqui), e os **29 ponteiros não foram reproduzidos**.

**O que foi medido nesta máquina em 2026-08-08, e é fato:** os 663 tokens do
`CLAUDE.md`; o `ModuleNotFoundError: jsonschema` do `auditar_custo.py`; as 322 linhas
atuais do `sensor_lei5_juiz.py`; os 12.713 B do `RETOMADA-M-01`; a pasta única de
backups do `SSC-Plus`; as contagens de `LucasIA` da tabela 4c.

**Acrescentado pela M-03, também medido aqui e também fato:** `jsonschema` **ausente**
do único interpretador da máquina (sem `.venv`, cache do pip vazio), instalado em
2026-08-08 com reversão vermelha provada; clone nascido em **2026-08-06 15:33** por
`git reflog`, com o acoplamento a `jsonschema` já no histórico desde `927969b`
(2026-07-26); o `teto:` por arquivo **nunca** compôs o código de saída
(`git log -S"real <= teto"` → só `7380a4a`, o commit que criou o script), com **3 de
22** arquivos acima do teto declarado hoje; e `scripts/sensor_lei5_juiz.py` com
**um único commit** em `E:\lucaX` e **nenhum** em `E:\LucaX-Enterprise-OS`.

**Sedes deste documento.** Original aqui (sede de memória, local a esta máquina).
Cópia **não durável** em `E:\lucaX\.scratch\PACOTE-PARA-A-PRINCIPAL-2026-08-08.md`.
Ponteiro na regra viva `E:\lucaX\.claude\rules\git-and-backup.md`.
**Esta sede também é de uma máquina só** — reescrevê-la na principal faz parte da
tarefa 3.

Relacionados: [[nunca-apagar-custodia]] · [[nunca-apagar-lista-longa]] ·
[[m-01-relatorio-so-na-transcricao]] · [[contrato-fabrica-acervo-custa-c3]] ·
[[retomada-m-01-2026-08-08]]
