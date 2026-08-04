---
id: RFC-0030-segunda-skill-varrer-credencial
titulo: A segunda Skill do acervo — varrer credencial —, e o que so a segunda instancia mede
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
decisoes_relacionadas: [ADR-0033, ADR-0034, ADR-0035]
substitui: []
substituido_por: null
classe_mudanca: C2
prazo_analise: 2026-08-03
---

# RFC-0030: A segunda `Skill`

## Proposito

Criar a **segunda `Skill`** do acervo a partir de `secret-scan`, a capacidade que
[`RFC-0029 §4`](RFC-0029-primeira-skill-copia-datada.md) declarou **segunda por medicao** — e
**medir o que so a segunda instancia alcanca**.

> **A ficha nao e o entregavel principal desta proposta.** `n = 1` nao produz mediana, nao
> produz duplicata e nao distingue **defeito do Framework** de **defeito do caso**. `n = 2`
> produz as tres coisas.

## Escopo

| Item | Definicao |
|---|---|
| **Inclui** | O enquadramento de `secret-scan` sob `SK-01` a `SK-26`; o local canonico `skills/`; a reavaliacao das **26** regras com **duas** instancias |
| **NAO** inclui | **Mover codigo para o acervo** — o canonico recebe a **ficha** · abrir o `ADR` sucessor de `ADR-0033` · promover `ADR-0033` a `FND` · emendar `TPL-skill` ou sanar `RD-122` · liberar portao · admitir os outros candidatos |

## 1. Item 0 — o candidato cabe sob `SK-01` a `SK-26`?

**Medido ANTES de propor, e o teste tinha poder de PARAR a missao:** `Skill` que nao cabe no
proprio Framework e **achado sobre o Framework**, nao ficha a redigir.

| Regra decisiva | Verificacao | Resultado |
|---|---|---|
| **`SK-01`** — tres condicoes cumulativas | **repete** *(19/19 no corpus; 476 blobs na F5; portao em producao no `nxtrack`)* · **verificavel** *(codigo de saida `0`/`1`/`2` contra gabarito rotulado)* · **mais de um papel** *(DEP-QAR, DEP-OPS, DEP-KMS, DEP-GOV)* | ✅ **3 de 3** |
| **`SK-02`** — pertence a organizacao | O procedimento **nao depende de quem invoca**: a mesma arvore devolve o mesmo veredito para qualquer DEP | ✅ |
| **`SK-03`** — nome e acao | ⚠️ **O nome externo REPROVA.** `secret-scan` e **ingles** e **substantivo + substantivo**; a regra exige **`<dominio>-<verbo>-<objeto>`**. **Renomeado para `seguranca-varrer-credencial`** | ⚠️ **reprovou e corrigiu** |
| **`SK-04`** — `SKL` × `WFL` | **O caso mais dificil do enquadramento, e por isso esta isolado em §3** | ✅ **`SKL`** |
| **`SK-05`** — nao e `Prompt` nem `Playbook` | A forma externa **e** um arquivo de prompt com frases-gatilho — e **`FND-10 §4.8` resolve sozinho**: *"prompt reusado por 2+ componentes JA E Skill"*. **Reusado por 2:** o agente que o carrega e o `gate_segredo.py` do `nxtrack` | ✅ **e `SKL`, nao tipo novo** |
| **`SK-07`** — Capability, minimo 1 | **`CAP-seguranca`**, `status: ativo`, custodio **DEP-QAR** — conferido no frontmatter | ✅ **1 de no maximo 3** |
| **`SK-16`** — nao decide | **Nao revoga, nao rotaciona, nao apaga.** Achou, quem invoca revoga — e revogar e decisao de quem detem a credencial | ✅ |
| **`SK-22`** — duplicata | **Verificado no catalogo mestre contra a unica `Skill` existente:** `SKL-custodia-criar-copia-datada` produz **ponto de retorno**; esta produz **veredito sobre exposicao**. **`0` passos comuns, `0` saidas comuns, `CAP` distintas** | ✅ **nao e duplicata** |

**Veredito do Item 0: CABE.** Nenhuma das 26 recusa o candidato; **uma** — `SK-03` — reprovou o
**nome** e o corrigiu, e essa e a segunda vez consecutiva que ela faz exatamente isso.

## 2. O criterio de escolha ja estava decidido, e nao se remede aqui

**`RFC-0029 §4` declarou:** *"`secret-scan` **nao e recusa de merito — e ordem**. […] **Fica como
candidata natural a segunda `Skill`."*** O que esta `RFC` acrescenta e o **sinal medido hoje**,
porque `SK-20` exige sinal **observado**, nunca herdado de outro documento.

| Eixo | Medida **desta missao** | Metodo |
|---|---:|---|
| Sinal no acervo — *"credencial em texto"* | **22** artefatos | `grep -rl` sobre a lista fechada, com **controle positivo** *(`artefato` = **217**)* e **negativo** *(termo inexistente = **0**)* |
| Sinal no acervo — *"credencial"* | **56** artefatos | idem |
| **Uso real registrado no lease** | **14** tokens declaram **`0` credenciais** na pos-verificacao | `grep -c` no instrumento de lease |
| **Uso real fora do acervo — varredura de historico** | **476 blobs** de **63 commits** em **2** repositorios *(`nxtrack` 39/278 · `consult` 24/198)*, **`0` credencial real** | missao `F5-PREPARAR-REMOTE`, tabela da Ordem 1 |
| **Uso real em producao** | `infra/scripts/gate_segredo.py` **invoca** o verificador antes de publicar — **8/8** casos, **4** de controle **positivo** e **2** de controle **negativo** | `docs/provas-dos-invariantes-2026-08-03.md`, invariante (a) |

> **O que mudou desde `RFC-0029` e a natureza do sinal, nao o numero.** Em 2026-08-03 a
> capacidade deixou de ser *"19/19 em corpus"* e passou a ter **portao em producao que falha
> FECHADO** e **historico varrido**. `SK-20` recusa antecipacao; **nada aqui e antecipado**.

## 3. `SK-04` — o unico enquadramento que quase reprovou, e por que nao reprovou

**A regra:** *"`SKL` se um papel; `WFL` se atravessa papeis **ou tem portao**"*. E o consumidor
mais forte desta capacidade **e literalmente um portao** — `gate_segredo.py`, com codigo de saida
proprio e **falha fechada**.

**O teste, aplicado a letra:**

| Pergunta de `SK-04` | Resposta medida |
|---|---|
| O **procedimento** precisa de **dois papeis** para completar? | **Nao.** Um papel invoca, recebe veredito, termina |
| O **procedimento** contem portao? | **Nao.** Ele **relata**; nao aprova, nao barra, nao entrega a ninguem |
| Entao de quem e o portao? | **Do consumidor.** O portao de publicacao e etapa do fluxo de deploy **do produto**, e ele **usa** esta capacidade como passo |

**`FND-10 §4.8` prevê exatamente este arranjo** ao alojar o acionamento no atributo `gatilho`,
listando *"etapa de `WFL`"* entre o que dispara uma `SKL`. **`SKL` consumida por portao alheio e
o caso modelado, nao a excecao** — e e a distincao que a primeira `Skill` **nao teve como
exercer**, porque nada perto de um portao a consumia.

## 4. `SK-12` — a regra que nasceu sem experiencia, e a primeira observacao real

`ADR-0033 §L3` declarou: *"`SK-12` declara a linha que o gatilho nao cruza **SEM ter observado
nenhuma tentativa de cruza-la**"*. **Esta missao produz a primeira observacao**, e ela e um
**quase-cruzamento medido**.

| Marcador de `SK-12` — *"ciclo de vida independente"* | `gate_segredo.py` tem? |
|---|---|
| **Identificador proprio** | ✅ sim — nome, caminho, codigos de saida proprios *(`3` = fabrica ausente)* |
| **Citabilidade externa** | ✅ sim — citado em `INFRA.md`, no procedimento de deploy e no script de publicacao |
| **Autoridade propria** | ✅ sim — **recusa publicar**, e a recusa e dele, nao do verificador |
| **Versao propria** | ➖ nao no sentido da regra — ele **imprime o `sha256` do verificador**, e nao versiona a si mesmo |

**Tres de quatro marcadores presentes — e `SK-12` nao e violada, porque nada disso esta no
`gatilho` da `Skill`.** A superficie vive **no consumidor, fora do acervo**, que e onde `SK-12`
manda que fique. **O gatilho de reabertura de `Command` segue NAO satisfeito** — e agora isso e
**observado**, nao derivado.

## 5. Enquadramento das demais — sem novidade

| Regra | Verificacao |
|---|---|
| **`SK-06`** | Exige `capabilities` e `gatilho`; **`TPL-skill` continua sem os dois**. Escritos a mao, **sem criar campo novo** (`AC-07`). **`RD-122` exercido pela SEGUNDA vez** |
| **`SK-08`** | *"Quando NAO usar"* com **6** exclusoes reais, entre elas **nao substitui rotacao** e **nao le binario** |
| **`SK-13`** | **IDEMPOTENTE** — leitura pura, `0` efeito externo. **E o ramo OPOSTO ao da primeira `Skill`**, e por isso esta e **elegivel a repeticao automatica**, que e o que permite o portao rodar a cada deploy |
| **`SK-17`** | 4 entradas com origem e obrigatoriedade; 4 saidas com destinatario e formato |
| **`SK-18`** | `MEDICAO` + `TESTE` — *"`19` de `19` vereditos contra gabarito rotulado, `0` falso negativo"* |
| **`SK-19`** | A falha **plausivel e errada** e **dupla** aqui, e as duas estao medidas — ver §6 |
| **`SK-23`** | **7** normas citadas por identificador, **`0`** reproduzidas. **`PI-08` e `LV-02` NAO tem o texto copiado** |
| **`SK-25`** | Criterio de descontinuacao com **3** condicoes, sinal observavel e substituto |

## 6. `SK-19` — a falha plausivel e errada, em duas formas

**A regra exigiu declarar a saida bem-formada e incorreta. Nesta capacidade ha DUAS, e ambas
foram medidas fora do acervo antes desta proposta:**

| Forma | Como se manifesta | Evidencia medida |
|---|---|---|
| **Falso negativo silencioso** | Dizer *"limpo, saida `0`"* com credencial presente. **String de alta entropia sem nome sensivel e sem prefixo de fornecedor passa** — limite declarado, nao esquecido | Declarado no gabarito; a decisao de projeto e **recall maximo por prefixo**, aceitando falso positivo em documentacao |
| **Ruido que ensina a ignorar o portao** | **58 achados, 55 bloqueantes, `0` credencial real** numa arvore. Um portao que grita sem motivo **e desligado na terceira vez** — e ai a protecao vale `0` | Medido no `nxtrack` em 2026-08-03; a causa e vocabulario do dominio *(`chave` e tonalidade Camelot; `token` e gerado, nao embutido)* |

> **A segunda forma e a que a primeira `Skill` nao tinha como revelar.** Copia datada falha
> **ruidosamente**; varredura falha **por fadiga de alarme**. `SK-19` exige *"a saida plausivel e
> errada"* no singular, e aqui **o singular nao bastou**.

## 7. Impacto

| O que muda | Medida |
|---|---|
| Artefatos criados | **5** — `RFC-0030`, `ADR-0035`, a `Skill`, `FIT-2026-028`, `PT-2026-022`. **IDENTICO ao custo da primeira** |
| `Skill`s no acervo | **1 → 2** |
| Bytes de **codigo** no acervo | **`0`** — a implementacao **nao se move** |
| `GO-TO-SKILLS` | **Continua EXERCIDO.** Exercer duas vezes nao e liberar |
| `ADR-0033` | **`0` bytes.** Os tres defeitos ficam **declarados e nao sanados** |

## 8. Riscos

| # | Risco | Mitigacao |
|---|---|---|
| `R1` | A ficha descreve capacidade cujo **codigo vive fora** e pode divergir | Declarado na ficha; o consumidor em producao **imprime o `sha256`** do verificador a cada execucao, e divergencia aparece no log |
| `R2` | Ler *"o portao e do consumidor"* como licenca para engordar o `gatilho` | §4 mede os marcadores de `SK-12` e declara onde a linha esta |
| `R3` | Ler a idempotencia desta como propriedade do tipo `SKL` | **Nao e.** As duas `Skill`s existentes estao em **ramos opostos** de `SK-13`, e isso e o que `n = 2` mostrou |
| `R4` | Ler *"`SK-24` agora e calculavel"* como *"`SK-24` agora decide"* | **Nao decide.** [`ADR-0035 §4`](../decisions/ADR-0035-segunda-skill-varrer-credencial.md) demonstra que em `n = 2` o teste **nao pode disparar para valor nenhum** |
