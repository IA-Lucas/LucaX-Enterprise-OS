---
id: ADR-0028-independencia-de-verificacao-por-fornecedor
titulo: Aferir independencia de verificacao por identidade de executor, tornando revisor diferente de autor pre-condicao necessaria e nunca suficiente
tipo: adr
versao: 1.0.0
status: em-revisao
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-07-31
atualizado_em: 2026-07-31
revisao_prevista: 2027-01-31
decisoes_relacionadas: [ADR-0005, ADR-0006, ADR-0009, ADR-0012, ADR-0015]
substitui: []
substituido_por: null
classe_mudanca: C3
tipo_decisao: 1
supera: []
superado_por: null
resumo: Redefine o criterio de afericao da independencia da verificacao de divergencia de campo para identidade de executor, com a diferenca medida em 131 sobre base de 138.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: pendente
---

# ADR-0028: independencia de verificacao aferida por fornecedor

> **NAO ESTA EM VIGOR.** `status: em-revisao` · `ratificacao: pendente`. `C3`/`Tipo 1` exige
> **ratificacao explicita e datada do Soberano sobre o texto final** (`LM-02`, `CV-09`). Esta
> missao **nao emite ato**.
>
> ### Esta decisao nao se aplica a si mesma
>
> Ela e revisada pelo criterio **VIGENTE** — `AC-03`, `autor` ≠ `revisor`, satisfeito:
> autor **DEP-GOV**, revisor **DEP-QAR**. **Sob o criterio que ela propoe, esta propria decisao
> seria `fornecedor_verificacao: interno`** — e nao seria por isso invalida, porque `AV-4`
> declara que conferencia interna **nao e defeito e nao bloqueia**. **A diferenca esta escrita
> para que ninguem leia esta revisao como independente de fornecedor.**

## Proposito

Registrar a decisao de redefinir **como se afere** a independencia da verificacao: de
divergencia de **campo** para identidade de **executor**.

## Escopo

| Item | Definicao |
|---|---|
| **Inclui** | O criterio de `AC-03` · o campo `fornecedor_verificacao` · as regras `AV-1` a `AV-6` · a linha *Autoverificacao* das evidencias de integridade |
| **Nao inclui** | A **proibicao** de autoverificacao · `RM-06` de `FND-09` · `LV-03` · `PI-05` · `ADR-0005` · invalidacao de artefato algum · correcao de `FIT` emitido |
| **Subordinado a** | [FND-01 §9](../foundation/01-constituicao.md) · [FND-04 §2](../foundation/04-governanca.md) |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| Proponente | **DEP-GOV** | Proprietario de `FND-10`; mediu os dois criterios |
| Revisor independente | **DEP-QAR** | `AC-03` — **criterio vigente** |
| Aprovador · Ratificador | **SOBERANO**, indelegavel | `FND-04 §2`, `C3` |
| Executor | **DEP-GOV** | |

> **DEP-QAR nao propoe.** A materia alcanca o criterio pelo qual **DEP-QAR** verifica, e o
> custodio da competencia afetada nao pode ser proponente — o mesmo desenho de
> `ADR-0005 §Responsaveis`, aplicado ao caso inverso.

---

## 1. Contexto

A proibicao de autoverificacao existe desde
[`ADR-0005`](ADR-0005-proibicao-de-autoverificacao.md) e e solida: `RM-06` de `FND-09 §6.3`
proibe o **par reflexivo** da relacao `verifica`. **O que nao existe e um criterio que a torne
aferivel sobre artefatos.**

O criterio que o acervo usa na pratica e **`AC-03` de `FND-10 §2.5`** — *"`revisor` ≠ `autor`,
sempre"* —, e e ele que a linha *Autoverificacao* de toda evidencia de integridade mede.

### 1.1 Correcao de fato sobre a fonte

A minuta que precede esta decisao — `MINUTA-B-independencia-de-fornecedor.md`, `sha256`
`c1a04768b35cef31bf6309295644533527b50d671fb6696f8a43d61665a9ff88` — declara superar
*"**`ADR-0005`** quanto ao criterio de afericao"*.

**`ADR-0005` nao contem criterio de afericao algum.** Lido integralmente, ele decide quatro
coisas: `RM-06` proibe o par reflexivo; `FND-08 §5.2` recebe ponteiro; corrige-se a redacao de
`capabilities/README §5` e `CAP-governanca.md §9`; e declara-se quem verifica o que DEP-GOV
produz. **Nenhuma delas mede artefato.**

> **O criterio mora em `AC-03` de `FND-10 §2.5`, e e `FND-10` que esta decisao supera — nao
> `ADR-0005`.** A diferenca **muda a classe do rito**: emendar `ADR` seria `C2`; emendar
> **fundacional** e `C3`. **Herdar a classe da minuta teria produzido rito insuficiente.**

## 2. Problema / Pergunta de decisao

O criterio de afericao deve continuar sendo divergencia de campo, ou passar a ser identidade de
executor?

## 3. Criterios de decisao

Herdados de [RFC-0023 §4](../rfcs/RFC-0023-independencia-de-verificacao-por-fornecedor.md):
`K1` *(o numero responde a pergunta)*, `K2` *(nada e invalidado)*, `K3` *(nao para o acervo)*,
`K4` *(a proibicao permanece)*, `K5` *(reversivel)*.

## 4. Alternativas consideradas

[RFC-0023 §5](../rfcs/RFC-0023-independencia-de-verificacao-por-fornecedor.md): **A**
*(redefinir o criterio)*, **B** *(exigir executor distinto)*, **C** *(declarar so nos `FIT`)*,
**Z** *(nao fazer nada)*.

## 5. Decisao

### 5.1 As seis regras

| Regra | Conteudo |
|---|---|
| **`AV-1`** | **Autoverificacao e identidade de FORNECEDOR, nao de campo.** Verificacao e independente quando **quem verifica nao produziu** o objeto verificado — em qualquer papel, sob qualquer sigla |
| **`AV-2`** | **`revisor` ≠ `autor` deixa de ser prova e passa a ser PRE-CONDICAO.** Necessaria, **jamais suficiente**. Igualdade continua tornando a aprovacao **nula** — `AC-03` **nao afrouxa** |
| **`AV-3`** | **Todo artefato declara `fornecedor_verificacao`:** `interno` *(mesmo executor)* · `independente` *(executor distinto)* · `soberano`. Campo **declarado**, nunca inferido |
| **`AV-4`** | **Verificacao com `fornecedor_verificacao: interno` NAO afirma conformidade independente.** Declara **conferencia interna**, com o limite escrito no proprio veredito. **Nao e defeito e nao bloqueia** — e a diferenca entre **conferir** e **atestar** |
| **`AV-5`** | **A linha *Autoverificacao* das evidencias de integridade passa a publicar OS DOIS numeros**, com os dois criterios nomeados. Publicar so o primeiro e o defeito que esta decisao fecha |
| **`AV-6`** | **Nenhum artefato existente e invalidado.** `AV-3` alcanca artefato **criado ou emendado a partir da vigencia** (`AC-08`); o acervo anterior recebe o valor **por curadoria no catalogo**, como a migracao de custo zero de `FND-10 §2.3` |

### 5.2 `AC-07` satisfeita — o campo nasce com valor padrao declarado

`AC-07` proibe campo novo sem valor padrao **ou** janela de migracao com dono e prazo.
**Adota-se o valor padrao:** `fornecedor_verificacao` ausente **le-se `interno`**, que e o valor
verdadeiro para **131 dos 138** artefatos medidos. **`0` arquivos do acervo sao tocados** —
o mesmo mecanismo de `FR-09` de `ADR-0007` e de `FND-10 §2.3`.

### 5.3 Diff literal sobre `FND-10` — o que o ato aplicaria

> **Nao aplicado.** Reproduzido aqui para que o alcance seja conferivel **antes** da decisao,
> como `IR-08` exige do ato.

**`FND-10 §2.2`, tabela *Extensao do contrato* — acrescenta-se UMA linha, apos `projecao_de`:**

```diff
  | `projecao_de` | `<ID> §<secao>`, um por fonte projetada | Artefato cujo conteudo seja **majoritariamente** projecao — indice, catalogo, matriz derivada | **Ausente** = nao e projecao *(§2.6, PJ-02)* |
+ | `fornecedor_verificacao` | `interno` · `independente` · `soberano` | Artefato criado ou emendado **a partir da vigencia de ADR-0028** | **Ausente** = `interno` *(AV-3, AV-6, AC-07)* |
```

**`FND-10 §2.5`, regra `AC-03` — substituida:**

```diff
- | AC-03 | `revisor` ≠ `autor`, sempre. Igualdade torna a aprovacao **nula** (LV-03, PI-05, RM-06b). |
+ | AC-03 | `revisor` ≠ `autor`, sempre. Igualdade torna a aprovacao **nula** (LV-03, PI-05, RM-06b). **Necessaria e nunca suficiente:** a independencia e aferida por `AV-1` (ADR-0028), e a divergencia de campo e apenas a sua pre-condicao. |
```

**`FND-10 §2.5` — acrescentam-se `AV-1` a `AV-6` apos `AC-11`.**

**Alcance total do diff: `2` linhas alteradas ou acrescentadas em `§2.2` e `§2.5`, mais o
bloco `AV`. `0` bytes em `§1`, `§2.1`, `§2.3`, `§2.4`, `§2.6`, `§3` a `§11`.**

> ### Consequencia declarada, e NAO corrigida — `RD-62`
>
> `FND-10 §2.2` intitula *"Extensao do contrato — **cinco** campos novos"* e a tabela **ja tem
> seis linhas** *(achado `RD-62`, aberto)*. **Esta emenda a leva a sete, e portanto agrava o
> achado.**
>
> **`RD-62` NAO e corrigido aqui**, e a razao e de escopo: corrigir achado fora da lista da
> missao seria correcao silenciosa. **O agravamento fica declarado**, com dono **DEP-GOV** e
> gatilho *"o ato que aplicar `ADR-0028`"* — que e o momento em que o titulo tera de ser
> remedido de qualquer forma.

## 6. Justificativa

| # | Fundamento |
|---|---|
| 1 | **A diferenca esta medida, nao argumentada:** `0` contra `131`, base `138`, mesmo acervo, mesmo instante. Um indicador que so pode dar o valor bom nao e indicador |
| 2 | **Nao exige o que a organizacao nao tem.** `AV-1` exige **declarar** o fornecedor, nao **ter** dois. A Alternativa `B` exigiria dois e violaria a propria regra em `131 de 138` no dia da vigencia |
| 3 | **A proibicao sai fortalecida, nao afrouxada.** `AC-03` continua tornando nula a aprovacao com campos iguais; ganha um segundo teste acima dela |
| 4 | **Tradeoff aceito:** o acervo passara a publicar, em toda evidencia de integridade, um numero **alto e desconfortavel** — hoje `131`. **É o proposito.** O numero baixo anterior nao media independencia; media preenchimento de campo |

## 7. Impacto

| Dimensao | Impacto |
|---|---|
| **Fundacionais emendados** | **1 — `FND-10`**, `§2.2` e `§2.5`, versao **`MENOR`** *(acrescimo de campo e de regras, sem remocao)*. **É o que torna esta mudanca `C3`** |
| `ADR-0005` | **`0` bytes.** Nao e superado; permanece integralmente valido |
| Artefatos invalidados | **`0`** — `AV-6`, `EV-03` |
| `FIT` emitidos alcancados | **19** — passariam a declarar conformidade por criterio que a norma nova nao reconhece. **Declarado; nao corrigido, nao reaberto** |
| Evidencias de integridade | **11** *(`§10.2`–`§10.11`)* publicam *Autoverificacao* pelo criterio antigo. Sao **`BL-02`**, **nao editaveis**. A partir da vigencia, `AV-5` alcanca **as novas** |
| Templates | `TPL-documento`, `TPL-adr`, `TPL-fitness-check` e os demais **19** passariam a prever o campo — **cascata `CV-04`, nao executada por esta decisao** |
| Ganho `PI-14` | **Organizacao** — a pergunta que a norma faz passa a ter resposta publicavel |

## 8. Evidencias

| # | Evidencia | Origem | Confianca | O que discrimina |
|---|---|---|---|---|
| `E1` | `C-1` = **`0`** · `C-2` = **`131`** · base **138**, sobre `BL-2026-07-31-02` | `ferramentas/autoverificacao.sh`, Missao 1.13.4.2 | **Alta — medida** | Sustenta `K1`: elimina `Z` |
| `E2` | Os **7** sobreviventes sao `MSG-2026-0001` a `MSG-2026-0007` | idem, lista nominal | **Alta — medida** | Mostra que a unica independencia real do acervo e a do Soberano |
| `E3` | `131 de 138` seriam violacao no dia da vigencia sob a Alternativa `B` | derivado de `E1` | **Alta** | **Elimina `B`** por `K3` |
| `E4` | `ADR-0005` nao contem criterio de afericao | leitura integral | **Alta — verificavel** | **Sustenta `C3` em vez de `C2`**: o criterio mora em fundacional |
| `E5` | A 1.13.4 reportou `0` autoverificacoes tendo construido, corrigido e aplicado o proprio detector | `PS-2026-014 §1.1`; `artifact-registry §10.10` | **Alta — verificavel** | O caso que originou a decisao |
| **`A1`** | **Evidencia ausente, declarada:** **nenhum caso de verificacao independente de fornecedor existe no acervo** para comparar. `AV-4` e desenhada sem membro observado do lado `independente` | `PI-10`, `LV-12` | — | Impede afirmar que o criterio novo produzira verificacao melhor — ele produz **verificacao declarada**, que e outra coisa |

## 9. Riscos e mitigacao

| # | Risco | Prob. | Impacto | Mitigacao |
|---|---|---|---|---|
| `RA-1` | `fornecedor_verificacao: interno` virar carimbo, e `AV-4` virar licenca para nao buscar independencia | **Alta** | **Alto** | `AV-5` obriga a **publicar o numero** em toda evidencia de integridade. Carimbo que aparece em `131 de 138` e visivel; carimbo que aparece em `0` nao |
| `RA-2` | O campo ser inferido em vez de declarado, reintroduzindo o defeito por outro caminho | Media | Alto | `AV-3`, texto expresso: **declarado, nunca inferido** |
| `RA-3` | Os **19** `FIT` emitidos serem lidos como invalidados | Media | Medio | `AV-6` e §7: **`0` invalidados**, regra prospectiva |
| `RA-4` | A cascata de templates ficar pendente indefinidamente | **Media** | Medio | Declarada em §7 como **nao executada**; entra no ato que aplicar |
| `RA-5` | **Esta decisao estar errada** — fornecedor ser criterio grosseiro demais quando houver dois executores | Baixa | Medio | Gatilho de revisao no **primeiro** artefato com `fornecedor_verificacao: independente`, §12 |

## 10. Plano de reversao — **explicito, exigido por `C3`/`Tipo 1`**

`FND-04 §2.2` exige, para `C3`/`Tipo 1`, *"ratificacao do Soberano **+ plano de reversao
explicito**"*.

| Campo | Conteudo |
|---|---|
| Reversivel? | **Sim, mas caro — `Tipo 1`** |
| Como desfazer | `ADR` de retirada (`O9`) superando este; `FND-10` volta por versao **`MENOR`**, com `AC-03` restaurada e o bloco `AV` removido |
| **Custo da reversao — medido, objeto a objeto** | **1** `ADR` novo · **1** emenda `MENOR` a `FND-10` *(fundacional: exige **novo ato do Soberano**)* · **os templates** ja alcancados pela cascata · **todo artefato criado sob a vigencia**, que passa a declarar campo **fora do contrato** — violacao de `AC-01`, corrigivel so por curadoria artefato a artefato |
| O que **nao** se reverte | **As evidencias de integridade publicadas sob `AV-5`.** Sao `BL-02` e nao sao editaveis: ficariam publicando dois numeros sob norma revogada |
| Por que **`Tipo 1`** e nao `Tipo 2` | **Reverter exige um segundo ato soberano** *(emendar fundacional)*, **alcanca artefatos ja criados** e **deixa residuo nao editavel**. Nenhuma das tres condicoes vale para `Tipo 2`, cuja definicao e reversao trivial sem consumidores |
| Janela | Barata enquanto **`0`** artefatos declararem o campo. **Encarece a cada artefato novo** |
| Backup (`PI-07`) | `_backups/LucaX-Enterprise-OS_2026-07-31_pre-missao-1-13-4-2/` |

## 11. Classificacao — **determinada, nao presumida por analogia**

| Campo | Valor |
|---|---|
| Classe de mudanca | **`C3` — Constitucional** |
| Tipo de reversibilidade | **`Tipo 1`** |
| Aprovador | **SOMENTE o SOBERANO**, indelegavel |
| Ratificacao | **Sempre exigida** — `pendente` ate ato explicito e datado sobre o texto final |
| Instrumento | **`RFC` obrigatoria → analise de impacto → `ADR` → ratificacao** — [RFC-0023](../rfcs/RFC-0023-independencia-de-verificacao-por-fornecedor.md) |
| Fitness Check | **Obrigatorio** (`CV-07`) — [FIT-2026-021](../governance/fitness/FIT-2026-021-independencia-de-verificacao-por-fornecedor.md) |

### 11.1 A determinacao, hipotese a hipotese

| Hipotese de `C3` (`FND-04 §2`) | Incide? | Como se sabe |
|---|---|---|
| Altera **principio imutavel** | **Nao** | `PI-05` intacto. O que muda e como se **afere** o que ele exige |
| Altera **linha vermelha** | **Nao** | `LV-03` intacta e **reforcada** por `AV-2` |
| Altera **hierarquia normativa** | **Nao** | Nenhum nivel de `FND-01 §10` se move |
| Altera **direitos de decisao** | **Nao** | Ninguem passa a aprovar o que nao aprovava. `AV-4` **descreve** o alcance de um parecer; nao muda quem o emite |
| **Altera a propria Fundacao** | **SIM** ⟵ | **`FND-10 §2.2` e `§2.5` sao emendadas** — campo novo no contrato universal e `AC-03` redefinida. **Uma hipotese basta** |

**`Tipo 1`, determinado:** `FND-04 §2.2` opoe reversivel a **irreversivel ou caro**. §10 mede
tres custos que `Tipo 2` nao admite — **segundo ato soberano**, **alcance sobre artefatos ja
criados** e **residuo nao editavel em `BL-02`**. **A minuta ja propunha `C3 · Tipo 1`, e a
coincidencia nao e o fundamento:** a classe foi redeterminada a partir de `FND-04 §2`, e o
**objeto superado mudou** — de `ADR-0005` para `FND-10`.

## 12. Revisao

| Campo | Conteudo |
|---|---|
| Gatilho por evento | **Primeiro artefato com `fornecedor_verificacao: independente`** — verificar se o criterio discrimina de fato |
| Gatilho por evento | **Primeira baseline sob `AV-5`** — verificar se publicar dois numeros mudou alguma decisao |
| Gatilho temporal | 2027-01-31 |
| Sinal de que esta decisao deu errado | *(a)* `interno` em `100%` dos artefatos por dois horizontes, sem que ninguem registre o custo; *(b)* `AV-4` sendo citada para dispensar revisao em vez de para qualifica-la |
| Dono | **DEP-QAR** |

## 13. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Origem | [RFC-0023](../rfcs/RFC-0023-independencia-de-verificacao-por-fornecedor.md) |
| Evidencia de origem *(nao norma)* | `MINUTA-B-independencia-de-fornecedor.md`, `sha256` `c1a04768b35cef31bf6309295644533527b50d671fb6696f8a43d61665a9ff88` |
| **Norma superada** | **`FND-10 §2.5`, regra `AC-03`, quanto a SUFICIENCIA — e somente quanto a ela.** `FND-10 §2.2` e **estendida**, nao superada |
| Norma **nao** superada | **`ADR-0005`** *(nao contem criterio)* · `RM-06` de `FND-09` · `LV-03` · `PI-05` |
| Achado agravado e declarado | **`RD-62`** — o titulo *"cinco campos novos"* passa a divergir da tabela em **dois** |
| Verificacao de aptidao | [FIT-2026-021](../governance/fitness/FIT-2026-021-independencia-de-verificacao-por-fornecedor.md) |
| Pacote soberano | [PS-2026-015](../governance/pacote-soberano-2026-07-31-emendas-de-instrumento.md) |

---

## Checklist de validade (FND-07 §4.1)

- [x] `VD-01` — 3 alternativas reais + *"nao fazer nada"* (`RFC-0023 §5`)
- [x] `VD-02` — criterios declarados antes da escolha
- [x] `VD-03` — nenhuma alternativa de palha: `B` e `C` sao as respostas naturais
- [x] `VD-04` — tradeoff aceito explicito (§6, item 4)
- [x] `VD-05` — ausencia declarada (§8, `A1`): **`0`** casos de verificacao independente para comparar
- [x] `VD-06` — reversao **explicita**, exigida por `C3`/`Tipo 1` (§10)
- [x] `VD-07` — impacto em cascata mapeado, **inclusive o nao executado** (§7)
- [x] `VD-08` — data e responsavel presentes
- [x] `VD-09` — gatilhos de revisao definidos (§12)

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-31 | DEP-GOV | Decisao inicial, **`em-revisao` · `ratificacao: pendente`, NAO vigente**. Redefine o criterio de afericao da independencia: `AV-1` a `AV-6`, campo `fornecedor_verificacao` com valor padrao `interno` (`AC-07`). **Diferenca medida nesta missao: `0` contra `131`, base `138`.** Classe **`C3`/`Tipo 1`** determinada percorrendo as cinco hipoteses — incide *"a propria Fundacao"*, porque **o objeto superado e `AC-03` de `FND-10`, nao `ADR-0005`**, que **nao contem criterio de afericao**. Agravamento de **`RD-62`** declarado e **nao corrigido**. |
