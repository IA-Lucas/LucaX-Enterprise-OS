---
id: SKL-custodia-criar-copia-datada
titulo: Criar copia datada com manifesto sha256 e verificacao arquivo a arquivo antes de acao destrutiva
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
decisoes_relacionadas: [ADR-0033, ADR-0034]
substitui: []
substituido_por: null
resumo: Cria copia datada de uma arvore, com manifesto sha256 e conferencia arquivo a arquivo, e reconfere copia antiga — para que apagar, migrar ou sobrescrever tenha ponto de retorno provado, nao apenas datado.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
capabilities: [CAP-governanca]
gatilho: invocacao por papel, antes de acao destrutiva ou de exposicao — ver §1
---

# Criar copia datada (`SKL-custodia-criar-copia-datada`)

> **Sem copia, nao roda.**

**Copiar nao e o ponto: PROVAR que copiou e.** Uma copia sem manifesto identifica-se pela data e
**nao se confere**; seis meses depois, ninguem sabe se ela ainda carrega os bytes que dizia
carregar.

> ### ⚠️ Dois campos foram escritos A MAO, e a razao esta declarada
>
> `capabilities` e `gatilho` **nao existem no esqueleto de `TPL-skill`** — medido, `0`
> ocorrencias de cada, com controle positivo. Mas **`FND-09 §E-13` os exige** como *atributos
> minimos* de `SKL`, e **`SK-06`** os torna obrigatorios. **Escrever a mao NAO cria campo novo**
> (`AC-07`): sao campos que a norma **ja preve** e que o **template ficou para tras**.
> **Achado `RD-122`, ABERTO — esta ficha o exerce e nao o sana.**

## Escopo

| Item | Definicao |
|---|---|
| **Aplica-se a** | Qualquer arvore de arquivos sob custodia da organizacao, antes de **apagar**, **migrar**, **sobrescrever**, **renomear em massa** ou **expor dado vivo** |
| **NAO se aplica a** | Backup **externo** *(copia na mesma maquina nao protege de perda da maquina)* · versionamento *(nao comprime, nao versiona)* · dependencia reconstruivel *(`.git`, `node_modules`, `__pycache__`, `dist`, `build`, `venv` sao ignorados de proposito)* · **decidir se apaga** — a decisao e de quem invoca, **depois** da copia verde |
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
| **O que dispara** | **Invocacao por papel**, antes de: apagar arvore · migrar dado · sobrescrever artefato · renomear em massa · expor dado a terceiro · **adquirir lease de escrita** |
| **Quem pode disparar** | **Qualquer Departamento** — papel, nunca pessoa. Nao ha papel privilegiado |
| **Pre-condicao** | A arvore de origem **existe** e e legivel; ha **carimbo de data decidido** *(nao gerado sozinho)*; ha destino que **nao esta dentro da origem** |
| **Idempotencia** (`SK-13`) | **NAO IDEMPOTENTE, e a nao-idempotencia e deliberada.** Invocar duas vezes com o mesmo carimbo **RECUSA** na segunda *(saida `1`, "destino ja existe")*. **Copia datada que sobrescreve outra nao e copia: e substituicao**, e apagaria o ponto de retorno que se queria criar |

> **Consequencia de `SK-13` declarada:** por nao ser idempotente com efeito externo, **esta Skill
> nao e elegivel a repeticao automatica**. Falha de invocacao **para** e escala; nao se repete.

## 2. Entradas — `SK-17`

| Entrada | Origem | Obrigatoria? |
|---|---|---|
| Caminho da arvore de origem | quem invoca | **sim** |
| **Carimbo de data** | **decisao de quem invoca** — nunca do relogio | **sim.** Ausente, a Skill **recusa** *(saida `2`)* |
| Rotulo | quem invoca | nao — compoe o nome do destino |
| Caminho de destino | quem invoca | nao — padrao: `backups/` na raiz de Projetos *(ate 2026-08-15: `_backups/` irma da origem; renomeada na reorganizacao)* |
| Modo `--verificar` | quem invoca | nao — reconfere copia **ja existente**, sem copiar |

## 3. Procedimento — `SK-14`, `SK-15`

**Executavel por outro papel sem consultar o autor.** Cada passo declara o que produz.

| # | Passo | Produz |
|---|---|---|
| 1 | Recusar se o **carimbo** nao foi dado | saida `2`, e nada mais ocorre |
| 2 | Recusar se o **destino ja existe** | saida `1` — **protege o ponto de retorno anterior** |
| 3 | Recusar se o **destino esta dentro da origem** | saida `1` — evita o laco que enche o disco |
| 4 | Copiar a arvore, ignorando dependencia reconstruivel | a copia em `<pasta>-<carimbo>[-<rotulo>]` |
| 5 | Calcular `sha256` de **cada** arquivo copiado | `MANIFESTO-DA-COPIA.txt` |
| 6 | **Conferir arquivo a arquivo** origem × copia | veredito `VERIFICADO n/n` ou `DEFEITO: k de n divergente`, **nomeando o arquivo** |

**Modo `--verificar`:** executa **so** o passo 6 contra o manifesto ja gravado — e e o que
descobre **corrupcao silenciosa** antes de a copia ser necessaria.

## 4. Saidas — `SK-17`

| Saida | Destinatario | Formato |
|---|---|---|
| A copia datada | quem invoca | arvore em `<pasta>-<carimbo>[-<rotulo>]` |
| `MANIFESTO-DA-COPIA.txt` | quem for conferir **depois** | `sha256` + caminho, um por linha |
| Veredito | quem invoca | `VERIFICADO n/n` · `DEFEITO: k de n divergente` · `RECUSADO` |
| **Codigo de saida** | automacao que a invoca | `0` integra · `1` divergencia/recusa · `2` erro de uso |

## 5. Criterio de sucesso — `SK-18`

**Metodo de verificacao: `MEDICAO`** *(um dos cinco de `SF-14`)*.

**A copia e boa quando `n` de `n` arquivos conferem `sha256` contra a origem, com `n` medido e
declarado, e o codigo de saida e `0`.** *"Copiou"* nao e criterio; *"4 de 4 conferem, saida `0`"*
e.

## 6. Modos de falha conhecidos — `SK-19`

| Natureza | Como reconhecer | O que fazer |
|---|---|---|
| **Recusa** *(destino existe, destino interno, sem carimbo)* | saida `1` ou `2`, com a razao escrita | **E o portao funcionando, nao falha.** Corrigir a invocacao |
| **Divergencia detectada** | `DEFEITO: k de n divergente`, com o arquivo nomeado | A copia **nao serve** como ponto de retorno. Refazer |
| **Indisponivel** *(origem ilegivel, disco cheio)* | erro do sistema de arquivos | Parar. **Nao prosseguir com a acao destrutiva** |
| ⚠️ **PLAUSIVEL E ERRADA** — **a que `SK-19` obriga declarar** | **Dizer `VERIFICADO` com um arquivo divergente.** E a falha **grave**, porque produz **falsa seguranca**: a acao destrutiva prossegue sobre um ponto de retorno que nao vale | **Como se detecta:** por `TESTE` — corromper 1 arquivo da copia e exigir `DEFEITO`. **Medido: `0` falsos `VERIFICADO` em 5 de 5 cenarios** |

> **Defeito real corrigido na construcao, e ele e do tipo que so aparece rodando:**
> `os.path.commonpath` lanca `ValueError` quando origem e destino estao em **drives diferentes**
> no Windows — copiar de `E:\` para `C:\...\Temp`, **o caso mais comum**, quebrava com traceback
> antes de copiar. Corrigido: drive diferente significa, **por definicao**, destino fora da
> origem.

## 7. Normas aplicaveis — `SK-23`

**Citadas por identificador, nunca reproduzidas.** Em divergencia **prevalece a fonte** (`PJ-03`).

| Norma | O que impoe aqui |
|---|---|
| `RB-01` | Rollback declara **responsavel e custo** |
| `LV-12` | **Fabricar evidencia** — dizer `VERIFICADO` sem conferir e o caso central |
| `PI-07` | Copia datada anterior a edicao |
| `CE-04` | **Proibido estimar** — `n/n` e medido |
| `SF-14` | Os cinco metodos; aqui, `MEDICAO` e `TESTE` |
| `LV-04` | Evidencia historica **nao se reescreve** — por isso o destino nunca e sobrescrito |

## 8. Ganho `PI-14` — `SK-20`

| Campo | Conteudo |
|---|---|
| **Ganho declarado** | Transformar *"copia datada"* de **promessa** em **propriedade verificavel**: o manifesto permite conferir a copia **meses depois**, e o modo `--verificar` a reconfere **sem** refazer |
| **SINAL QUE MOTIVOU, e ele e observado, nunca antecipado** | **`RD-103`, severidade ALTA:** um script de faxina apagou `_to_delete` com `rd /s /q`, **sem lixeira**, levando dentro o **ponto de retorno declarado de um ato `C3` pendente**. **`7` arquivos ficaram sem bytes pre-escrita recuperaveis.** Nao houve como desfazer. **Alem disso:** *"copia datada"* aparece em **`67`** artefatos do acervo, e **`22`** tokens do lease a declaram — **a pratica ja existia e nao tinha instrumento proprio** |
| **Data de reavaliacao** | **2027-02-03** |

## 9. Criterio de descontinuacao — `SK-25`

| Condicao | Sinal observavel | Substituto previsto |
|---|---|---|
| O versionador passar a ser ponto de retorno confiavel | **`RD-104` FECHADO** — hoje o commit que se chama *baseline* nao reproduz `161` de `607` arquivos | `git`, com `.gitattributes` rastreado |
| Backup externo com verificacao equivalente entrar em operacao | Instrumento com manifesto e reconferencia, fora da maquina | Esse instrumento |
| **Se nenhum substituto existir** | — | **A organizacao deixa de ter esta capacidade**, e isso e **decisao**, nao omissao |

## 10. Rastreabilidade — `SK-09`

| Campo | Conteudo |
|---|---|
| **Capability** | [`CAP-governanca`](../capabilities/CAP-governanca.md) — **`ativo`**, custodio **DEP-GOV** *(`SK-07`, `VC-01`)*. **1 de no maximo 3** (`VC-03`) |
| **Consumidores nomeados** | **DEP-GOV** *(missao, lease, ponto de retorno)* · **DEP-KMS** *(custodia de memoria)* · **DEP-OPS** *(migracao e limpeza)*. **Enumerados, nunca *"todos"*** |
| **Origem** | [RFC-0029](../rfcs/RFC-0029-primeira-skill-copia-datada.md) → [ADR-0034](../decisions/ADR-0034-primeira-skill-copia-datada.md) |
| **Framework** | [ADR-0033](../decisions/ADR-0033-framework-de-skills.md) — `SK-01` a `SK-26` |
| **Implementacao** | **FORA do acervo**, e assim permanece: `_arquivo/projetos-parados/LucaX-Enterprise-Research/_fabrica/skills/backup-datado/`. **O canonico recebe a FICHA, nunca o codigo** |
| **Evidencia medida** | **5 de 5** cenarios corretos · **5 de 5** codigos de saida corretos · corrupcao detectada **nomeando o arquivo** · **`0`** falsos `VERIFICADO`. Executada em 2026-08-02 |
| **Custo de contexto** (`SK-24`) | medido em §4 do catalogo mestre, por `wc -l` |

## Historico

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-08-03 | DEP-GOV | **A PRIMEIRA `Skill` do acervo.** Recebe a capacidade `backup-datado`, construida e medida fora do acervo *(5/5 cenarios)*, e a expressa sob `SK-01` a `SK-26`. **O nome mudou por `SK-03`:** `backup-datado` e **substantivo + adjetivo**, e a regra exige **acao** `<dominio>-<verbo>-<objeto>` — dai `custodia-criar-copia-datada`. **`capabilities` e `gatilho` escritos a mao**, porque `TPL-skill` os omite *(`RD-122`, aberto)*. **`0` bytes de codigo entraram no acervo.** |
