---
id: RFC-0023-independencia-de-verificacao-por-fornecedor
titulo: A independencia da verificacao deve ser aferida por divergencia de campo, como hoje, ou por independencia de fornecedor?
tipo: rfc
versao: 1.0.0
status: aprovado
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-GOV
criado_em: 2026-07-31
atualizado_em: 2026-07-31
revisao_prevista: 2027-01-31
decisoes_relacionadas: [ADR-0005, ADR-0006, ADR-0009, ADR-0015]
substitui: []
substituido_por: null
classe_mudanca: C3
prazo_analise: 2026-08-31
resumo: Submete a decisao de aferir independencia de verificacao por identidade de executor em vez de divergencia de campo, com a diferenca entre os dois criterios medida em numero sobre o acervo vigente.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# RFC-0023: independencia de verificacao — de campo para fornecedor

## Proposito

Submeter a decisao de trocar o **criterio de afericao** da independencia da verificacao: de
`revisor` ≠ `autor` — divergencia de **campo** — para **identidade de executor** — independencia
de **fornecedor**.

## Escopo

| Item | Definicao |
|---|---|
| **Inclui** | O criterio de `AC-03` de [FND-10 §2.5](../foundation/10-artifact-framework.md) · o campo `fornecedor_verificacao` · a linha *Autoverificacao* das evidencias de integridade |
| **Nao inclui** | A **proibicao** de autoverificacao, que permanece integralmente · `RM-06` de `FND-09` · `LV-03` · `PI-05` · a invalidacao de artefato algum |
| **Subordinado a** | [FND-01 §9](../foundation/01-constituicao.md) · [FND-04 §2](../foundation/04-governanca.md) |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| Proponente | **DEP-GOV** | Proprietario de `FND-10`; **mediu** os dois criterios |
| Revisor | **DEP-QAR** | `AC-03`, criterio **vigente** |
| Valida a forma | **DEP-GOV** | `FND-09 §8.2` linha `RFC` |

> ### Nota de independencia, declarada
>
> A materia alcanca o **criterio pelo qual DEP-QAR verifica**. Pelo desenho de `ADR-0005 §Responsaveis`,
> o custodio da competencia afetada **nao propoe**. Aqui o custodio de `CAP-qualidade` e
> **DEP-QAR**, logo **DEP-QAR nao e proponente** — e **DEP-GOV** propoe, na qualidade de
> proprietario de `FND-10`, com **DEP-QAR** revisando. **A separacao e a mesma que `ADR-0005`
> instituiu, aplicada ao caso inverso.**

---

## 1. A evidencia — o instrumento aplicado a si proprio

Na Missao 1.13.4 **o mesmo agente construiu o instrumento de medicao, corrigiu-o depois que a
calibracao o reprovou, aplicou-o a si proprio e reportou 10 de 10 controles conformes com `0`
autoverificacoes.**

| # | Fato | Onde |
|---|---|---|
| 1 | O instrumento **reprovou** na primeira versao, e o defeito era **real** | `PS-2026-014 §1.1` — `FND-03` deu `9e020eda…cf7d` contra o publicado `1004673a…4b4e` |
| 2 | O instrumento corrigido reproduz **10 de 10** controles publicados | `artifact-registry §10.10` |
| 3 | **`0` autoverificacoes** foi reportado **pelo mesmo agente** que construiu, corrigiu e aplicou o detector de autoverificacao | `§10.10`, linha *Autoverificacao* |

> **O item 3 nao contradiz 1 e 2. Ele os torna nao verificaveis por terceiro** — que e
> exatamente o que a proibicao de autoverificacao existe para impedir.

## 2. A diferenca, medida em numero

**Medido por ferramenta sobre os `195` artefatos do acervo vigente, no mesmo instante,
`BL-2026-07-31-02`:**

| Criterio | Definicao | Autoverificacoes | Base |
|---|---|---|---|
| **`C-1` — divergencia de campo** *(vigente, `AC-03`)* | `autor` == `revisor` | **`0`** | **138** artefatos declaram os dois campos |
| **`C-2` — independencia de fornecedor** *(proposto)* | autor e revisor sao papeis do **mesmo executor** | **`131`** | os mesmos **138** |
| **Diferenca** | | **`131`** | |

**Os `7` que sobrevivem a `C-2` sao, todos, atos do Soberano** — `MSG-2026-0001` a
`MSG-2026-0007`, `autor: SOBERANO`, `revisor: DEP-QAR`. **Sao os unicos artefatos do acervo com
autor fora do fornecedor unico**, e mesmo eles tem **revisor** dentro dele.

> ### `0` e `131` medem o mesmo acervo no mesmo instante, e os dois sao verdadeiros
>
> O primeiro diz que **nenhum artefato tem os dois campos iguais** — e e verdade. O segundo diz
> que **131 de 138 artefatos foram revisados por quem os escreveu** — e tambem e verdade.
> **A norma vigente proibe o segundo e mede o primeiro.**
>
> **Medicao propria desta missao, nao herdada.** A Missao 1.13.4.1 mediu **`0` e `130` sobre
> 137**, com **194** artefatos. Os numeros mudaram porque o acervo cresceu em **1** artefato
> que declara os dois campos — `PT-2026-012`. **Reaproveitar o numero alheio seria publicar
> como medido o que foi copiado.**

## 3. A pergunta de decisao

**A independencia da verificacao deve continuar sendo aferida por divergencia de campo, ou
passar a ser aferida por identidade de executor?**

## 4. Criterios de decisao

| # | Criterio | Peso | Como se mede |
|---|---|---|---|
| `K1` | O numero publicado responde a pergunta que a norma faz | **Bloqueante** | Nao existe leitura em que `0` seja resposta a *"quem verificou nao produziu?"* |
| `K2` | Nenhum artefato existente e invalidado | **Bloqueante** | `0` artefatos passam a nao conformes na vigencia |
| `K3` | Nao para o acervo | **Bloqueante** | A organizacao tem **um** executor; regra que exija dois **impede trabalhar** |
| `K4` | A proibicao permanece intacta | **Bloqueante** | `LV-03`, `PI-05` e `RM-06` inalterados |
| `K5` | Reversivel | Medio | §6 |

## 5. Alternativas consideradas

### Alternativa A — Redefinir o criterio: `AC-03` vira pre-condicao, e declara-se `fornecedor_verificacao`

| Campo | Conteudo |
|---|---|
| Descricao | `autor` ≠ `revisor` deixa de ser **prova** e passa a ser **pre-condicao necessaria e nunca suficiente**; todo artefato novo declara `fornecedor_verificacao`; a linha *Autoverificacao* passa a publicar **os dois** numeros |
| A favor | Satisfaz `K1` a `K5`. **Nao exige segundo executor**: exige **declarar** qual foi |
| Contra | Acrescenta campo ao contrato universal — `AC-07` exige valor padrao ou janela de migracao |
| Custo | 1 `RFC` + 1 `ADR` + emenda `MENOR` a `FND-10` + curadoria no catalogo para o acervo anterior |
| Avaliacao | `K1` ✔ · `K2` ✔ · `K3` ✔ · `K4` ✔ · `K5` medio |

### Alternativa B — Exigir executor distinto para toda verificacao

| Campo | Conteudo |
|---|---|
| Descricao | Verificacao so vale se produzida por executor diferente |
| Contra | **Falha em `K3`, e a falha e medida:** a regra seria violada em **131 de 138** artefatos **no dia da vigencia**, e o rito **pararia**. Exigir independencia que a organizacao nao tem nao a produz — apenas torna toda verificacao nula |
| Avaliacao | `K1` ✔ · `K2` **falha** · `K3` **falha** · `K4` ✔ |

### Alternativa C — Declarar o limite so nos `FIT`, sem tocar `AC-03`

| Campo | Conteudo |
|---|---|
| Descricao | Cada Fitness Check passa a declarar que a conferencia foi interna |
| Contra | **Trata o sintoma.** A linha *Autoverificacao* das evidencias de integridade continuaria publicando **`0`** como se fosse prova de independencia, e e **ela** que entra em toda baseline. Corrige onde o defeito aparece, nao onde ele mora |
| Avaliacao | `K1` **falha** · `K2` ✔ · `K3` ✔ · `K4` ✔ |

### Alternativa Z — Nao fazer nada

| Campo | Conteudo |
|---|---|
| O que acontece | O detector continua medindo o campo e reportando `0`. O numero e verdadeiro e a pergunta fica sem resposta |
| Custo real da inacao | **Indefinido no tempo.** Nao ha gatilho que force a revisao: `0` nunca chama atencao, porque `0` e o valor desejado. **O defeito e invisivel exatamente por estar correto** |
| Por que nao venceu | Um indicador que so pode dar o valor bom nao e indicador |

## 6. Recomendacao

**Alternativa A.** `B` falha em dois bloqueantes com numero medido; `C` falha no bloqueante
`K1`; `Z` nao tem gatilho de saida.

## 7. Impacto levantado

| Dimensao | Impacto |
|---|---|
| **Fundacional alcancado** | **`FND-10`** — `§2.2` *(campo novo)* e `§2.5` *(`AC-03` redefinido, `AV-1` a `AV-6` acrescentadas)*. **É o que torna a mudanca `C3`** |
| `ADR-0005` | **Nao superado.** Nao contem criterio de afericao algum: proibe o **par reflexivo** da relacao `verifica` (`RM-06` de `FND-09 §6.3`). **Permanece integralmente valido** |
| Artefatos invalidados | **`0`** — a regra e prospectiva (`AV-6`, `EV-03`) |
| `FIT` emitidos | **19** passariam a declarar conformidade por criterio que a norma nova nao reconhece — **declarado, nao corrigido** |
| Evidencias de integridade `§10.2`–`§10.11` | **11** publicam a linha *Autoverificacao* pelo criterio antigo; sao **`BL-02`** e **nao sao editaveis** |

## 8. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Defeito que trata | Instrumento que a Missao 1.13.4 exerceu contra si e nao pode detectar, porque o detector mede o campo errado |
| Evidencia de origem *(nao norma)* | `_missao-1-13-4-1-2026-07-31/minutas/MINUTA-B-independencia-de-fornecedor.md`, `sha256` `c1a04768b35cef31bf6309295644533527b50d671fb6696f8a43d61665a9ff88` |
| Decisao gerada | [ADR-0028](../decisions/ADR-0028-independencia-de-verificacao-por-fornecedor.md) |
| Verificacao | [FIT-2026-021](../governance/fitness/FIT-2026-021-independencia-de-verificacao-por-fornecedor.md) |

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-31 | DEP-GOV | Proposta inicial. Submete a troca do criterio de afericao, com a diferenca **medida nesta missao**: `C-1` = **`0`**, `C-2` = **`131`**, base **138**, sobre `BL-2026-07-31-02`. Corrige a fonte: **`ADR-0005` nao contem criterio de afericao** — o criterio e `AC-03` de `FND-10 §2.5`. |
