---
id: FIT-2026-022
titulo: Verificacao de aptidao do caminho de superacao de ato por evidencia posterior
tipo: fitness-check
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: DEP-QAR
proprietario: DEP-QAR
aprovador: DEP-EXE
criado_em: 2026-07-31
atualizado_em: 2026-07-31
revisao_prevista: null
decisoes_relacionadas: [ADR-0012, ADR-0015, ADR-0029]
substitui: []
substituido_por: null
veredito: apto-com-ressalva
resumo: Verifica a aptidao do caminho de superacao de ato por evidencia posterior, com C11 conforme em 13 de 13 e quatro ressalvas, uma delas sobre irreversibilidade certa.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-GOV
ratificacao: nao-exigida
---

# FIT-2026-022: superacao de ato por evidencia posterior

> **Parecer, nao decisao** (`ADR-0015`, `FT-10`). O objeto avaliado esta **`em-revisao` ·
> `ratificacao: pendente`** e **nao esta em vigor**. **`0` atos foram superados.**

## Proposito

Emitir a Verificacao de Aptidao exigida por `CV-07` sobre a mudanca `C3`/`Tipo 1` registrada em
[ADR-0029](../../decisions/ADR-0029-superacao-de-ato-por-evidencia-posterior.md).

## Escopo

| Item | Definicao |
|---|---|
| Avaliado | O rito `RFC-0024` → `ADR-0029` · a determinacao da classe · a relacao com `ADR-0012` · o tratamento da irreversibilidade · `C11` |
| **Nao** avaliado | Nenhum ato concreto · o corpus do `SSC+`, que **nao e acervo e nao foi reconferido** · as emendas 1 e 2 |

## Responsaveis

| Papel | Quem |
|---|---|
| Emite | **DEP-QAR** · Revisa a forma **DEP-GOV** · Aprova **DEP-EXE** · Ratifica **—** (`FT-10`) |

> ### Independencia — criterio VIGENTE
>
> **`AC-03` satisfeito:** este parecer, autor **DEP-QAR** / revisor **DEP-GOV**; o objeto,
> autor **DEP-GOV** / revisor **DEP-QAR**.
>
> **`ADR-0028` NAO esta em vigor e NAO se aplica a este parecer.** Sob o criterio que ela
> propoe, esta verificacao seria **`fornecedor_verificacao: interno`**.

## 1. Controles obrigatorios

| # | Controle | Fonte | Resultado |
|---|---|---|---|
| `F1` | Classe determinada, **nao presumida por analogia** | `FND-04 §2` | ✅ Cinco hipoteses percorridas; incide ***"direitos de decisao"***, porque `SA-4` cria o direito de **instaurar** — `ADR-0029 §11.1` |
| `F2` | **A classe NAO foi herdada de `ADR-0012`** | `AL-01` | ✅ `ADR-0012` e `C2`/`Tipo 2` **sobre o mesmo objeto**, e a diferenca esta explicada: ele **protege** o ato, este **cria caminho que o alcanca** |
| `F3` | Lacuna comprovada **por medicao**, nao por leitura | `PI-10` | ✅ **`0`** ocorrencias de caminho de superacao de ato em norma vigente; **7 de 7** atos `ativo`, `substituido_por: null` |
| `F4` | Norma revogada **nomeada** | `SU-04` | ✅ **Nenhuma** — lacuna de **omissao**, e a afirmacao esta **medida**, nao presumida |
| `F5` | `ADR-0012` preservado e reposicionado | `CC-01`, `LV-04` | ✅ **`0` bytes**; `IR-07`, `IR-09`, `IR-05` e `IR-10` tornam-se **pre-condicao** — `ADR-0029 §5.2` |
| `F6` | **Plano de reversao explicito** — `C3`/`Tipo 1` | `FND-04 §2.2` | ✅ `§10`, **com a irreversibilidade da superacao consumada declarada como CERTA** |
| `F7` | O ato original preservado byte a byte | `SA-1`, `BL-02` | ✅ regra expressa; **`0`** atos alcancados hoje |
| `F8` | Decisao reservada ao Soberano | `PI-01`, `PI-06` | ✅ `SA-4` — instaurar ≠ decidir; **instauracao nao suspende** |
| `F9` | Efeito retroativo **nunca presumido** | `FND-01 §9`, `EV-03` | ✅ `SA-3` — prospectivo por padrao, retroativo **expresso e item a item** |
| `F10` | Contencao contra recurso permanente | `K3` de `RFC-0024` | ✅ `SA-5` — prova **posterior e independente**; releitura e discordancia |
| `F11` | `RFC` obrigatoria produzida | `FND-04 §2`, `C3` | ✅ [RFC-0024](../../rfcs/RFC-0024-superacao-de-ato-por-evidencia-posterior.md) — **4 alternativas + Z** |
| `F12` | Evidencia externa com **limite e confianca declarados** | `LV-12`, `FR-04` | ✅ `SSC+` **nao e acervo**, confianca **Media**, **nao reconferida** por esta missao |
| `F13` | Objeto **nao aplicado** | limite da missao | ✅ `em-revisao` · `pendente`; **`0`** superacoes; registro de `SA-6` **nao criado** |

## 2. `C11` — conformidade de [FND-10 §11](../../foundation/10-artifact-framework.md)

**13 de 13 conformes**, sobre `RFC-0024`, `ADR-0029` e este parecer.

| # | Verificacao | Resultado |
|---|---|---|
| 1 | Contrato `L1` completo | ✅ nos tres |
| 2 | `revisor` ≠ `autor` | ✅ `RFC-0024` GOV/QAR · `ADR-0029` GOV/QAR · este QAR/GOV |
| 3 | `ratificacao` coerente com a classe | ✅ `C3`/`Tipo 1` → **`pendente`**; `status` **nao** entra em `ativo` |
| 4 | Tipo documental consta de `§4` | ✅ |
| 5 | Atributo derivavel no frontmatter | ✅ **nenhum** |
| 6 | Cadeia percorrivel | ✅ `RFC-0024` → `ADR-0029` → `FIT-2026-022` → `PS-2026-015` |
| 7 | Custo de contexto medido | ✅ catalogo `§4` |
| 8 | Entrada no catalogo presente | ✅ |
| 9 | Divisao com menos de dois sinais | ✅ **nao aplicavel** — nenhuma entidade nova |
| 10 | Tabela reproduzida sem declaracao de projecao | ✅ **`0`** — `§5.2` **referencia** `ADR-0012` em vez de reproduzir suas regras |
| 11 | Teste preventivo de projecao aplicado | ✅ §2 |
| 12 | Origem externa fora do portao | ✅ **`0` bytes** do `SSC+` entraram; ele foi **lido**, nunca importado (`FR-04`) |
| 13 | Alteracao sem incremento de versao | ✅ **`0`** — objetos novos, `1.0.0`; **`0` bytes** em `ADR-0012` e nos 7 `MSG` |

## 3. Ressalvas

| # | Ressalva | Dono | Gatilho |
|---|---|---|---|
| `RA-1` | **A irreversibilidade e CERTA, nao provavel.** Uma superacao consumada **nao se desfaz** retirando a norma que a permitiu. `SA-5` encarece a entrada e `SA-1` preserva o texto, **mas nenhum dos dois devolve vigencia** | **SOBERANO** | Primeira instauracao |
| `RA-2` | **`SA-5` nunca foi exercida.** A fronteira entre *"prova posterior"* e *"releitura da mesma evidencia"* **nao tem caso**, e e ela que separa o caminho de um recurso permanente | **DEP-QAR** | Primeira instauracao |
| `RA-3` | **`SA-6` nascera com o contador em `0`**, e um registro vazio nao calibra portao algum. A utilidade da metrica so aparece depois do terceiro caso | **DEP-GOV** | Terceira instauracao |
| `RA-4` | **A evidencia central e externa e nao foi reconferida.** O caso do `SSC+` sustenta a **forma** do defeito, e esta missao **nao remediu** aquele corpus. **A ausencia esta declarada, nao suprida** | **DEP-QAR** | Ato que aplicar `ADR-0029` |

## 4. Evidencia ausente, declarada — `PI-10`

| # | Ausencia |
|---|---|
| 1 | **`0`** superacoes de ato ocorreram neste acervo. `SA-1`–`SA-6` sao **previstos, nunca observados** |
| 2 | **`0`** atos superaveis hoje: os 7 estao consumidos e **sem contradicao de prova conhecida** |
| 3 | **A fronteira de `SA-5` nao foi testada** contra nenhum caso concreto |
| 4 | **O corpus do `SSC+` nao foi reconferido** por esta missao — confianca **Media**, herdada |

## 5. Veredito

**`apto-com-ressalva`.**

A mudanca e **apta**: o rito `C3` esta completo, a classe foi **determinada e explicitamente
nao herdada** de `ADR-0012` — que trata do mesmo objeto e tem classe menor —, a lacuna esta
**medida** e nao suposta, **nenhuma norma e revogada**, `ADR-0012` sai **integro e
reposicionado como pre-condicao**, e o plano de reversao **nomeia o que nao se reverte** em vez
de omiti-lo.

As **quatro** ressalvas tem dono e gatilho. **`RA-1` nao e mitigavel** — e propriedade do
instrumento, nao defeito dele —, e por isso a classe e `Tipo 1` e a decisao e **indelegavelmente
do Soberano**.

> **Este parecer nao ratifica**, e o instrumento que ele avalia **so pode nascer de um ato**:
> um caminho que alcanca atos soberanos, instituido sem ato soberano, seria a propria
> contradicao que `SA-4` existe para impedir.

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-31 | DEP-QAR | Parecer inicial sobre `ADR-0029`. **`C11` 13 de 13**; **13** controles conformes. Registra que a classe **nao foi herdada de `ADR-0012`** *(`C2`/`Tipo 2`, mesmo objeto)* e que a lacuna esta **medida**: `0` caminhos em norma vigente, `7 de 7` atos `ativo`. **Quatro** ressalvas — `RA-1`, irreversibilidade **certa**, **nao mitigavel** — e **quatro** ausencias declaradas. Veredito **`apto-com-ressalva`**. |
