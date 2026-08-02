---
id: IDX-atos-superados
titulo: Registro de Atos Superados
tipo: relatorio
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-QAR
criado_em: 2026-07-31
atualizado_em: 2026-07-31
revisao_prevista: null
decisoes_relacionadas: [ADR-0012, ADR-0029]
substitui: []
substituido_por: null
resumo: Registra todo ato soberano superado por evidencia posterior, com data, ato superado por id e H-A, ato superador, condicao contradita e prova por caminho e sha256, conforme SA-6 de ADR-0029. Nasce com o contador em zero.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# Registro de Atos Superados

> **Criado pelo OITAVO ATO SOBERANO**, de 2026-07-31
> ([MSG-2026-0008](../memory/operacional/MSG-2026-0008-ato-soberano-emendas-e1-e-e3.md)), que
> ratificou [ADR-0029](../decisions/ADR-0029-superacao-de-ato-por-evidencia-posterior.md).
> **`SA-6` exige este registro, e ele nasce pelo ato que aplica a decisao — nunca pela decisao
> que o previu** (`ADR-0029 §7`).

## Proposito

Contar e identificar **cada vez que a prova venceu o ato**. `SA-6` existe porque **contar as
superacoes e a unica forma de saber se o portao esta calibrado**: um registro que nunca se move
diz que a regra e teorica; um que se move demais diz que os atos estao sendo emitidos sem prova
suficiente.

## Contador

| Medida | Valor |
|---|---|
| **Atos superados ate hoje** | **`0`** |
| **Atos vigentes superaveis** | **8** — os oito atos soberanos do acervo |
| **Instauracoes abertas** | **`0`** |
| Ultima atualizacao | 2026-07-31, na criacao |

> **Nasce em `0`, e o zero e evidencia — nao ausencia de registro.** `ADR-0029 §A1` declara:
> **nenhum caso real de superacao ocorreu neste acervo**, e a eficacia de `SA-1` a `SA-6` e
> **prevista, nao observada** (`PI-10`). **Enquanto este contador estiver em `0`, reverter a
> emenda custa `1` `ADR` de retirada e os indices `M3`** — a janela barata e agora.

## Registro

| # | Data | Ato superado — `id` e `H-A` | Ato superador | Condicao tecnica contradita *(citada literalmente)* | Prova — caminho e `sha256` | Efeito |
|---|---|---|---|---|---|---|
| — | — | *(nenhum ato superado)* | — | — | — | — |

## O que cada coluna exige — `SA-2`

| Coluna | Exigencia | Se faltar |
|---|---|---|
| **Ato superado** | `id` **e `H-A`** — nunca so o `id`. Sem `H-A` nao se sabe **qual texto** foi superado (`IR-07`) | A superacao e **nula**: afirma sobre objeto que ninguem fixa |
| **Condicao contradita** | **Citada literalmente** do ato original, nunca parafraseada | Vira discordancia de leitura, e **discordancia nao supera ato** (`SA-5`) |
| **Prova** | **Caminho e `sha256`** — evidencia material, **posterior e independente** do ato | `SA-5` reprova: releitura da mesma evidencia **nao** e evidencia posterior |
| **Efeito** | **Prospectivo por padrao.** Efeito retroativo e **expresso, item a item** | Presume-se **prospectivo** — o que o ato ja produziu **permanece valido** (`SA-3`) |

## Rito — quem faz o que

| Papel | Quem | Fundamento |
|---|---|---|
| **Instaurar**, com a prova | **Qualquer departamento** | `SA-4` — direito novo, criado por `ADR-0029` |
| **Decidir a superacao** | **SOMENTE o SOBERANO**, por ato novo | `SA-4`, `PI-01` |
| **Manter este registro** | **DEP-GOV** | `ADR-0029 §7` |
| **Verificar `IR-09` do ato superado** | **DEP-QAR** | `ADR-0012`, pre-condicao de `SA-2` |

> **Instaurar NAO suspende.** O ato instaurado **continua em vigor** ate o ato de superacao —
> `SA-4`. **Nao existe efeito suspensivo automatico**, e nenhum departamento desfaz decisao do
> Soberano.

## O que este registro NAO e

| # | Nao e |
|---|---|
| 1 | **Nao e caminho para editar, apagar ou reescrever ato algum.** O ato superado permanece **byte a byte**, `ativo` no historico, com **`0` bytes tocados** — `SA-1`, `BL-02`, `CC-01`, `LV-04` |
| 2 | **Nao e recurso contra decisao de MERITO.** Alcanca **condicao tecnica contradita por prova**, jamais preferencia revista — `ADR-0029 §5.3` |
| 3 | **Nao alcanca o `SSC+`**, que **nao e acervo** |
| 4 | **Nao e projecao.** E **fonte**: o catalogo e os indices projetam daqui, nunca o contrario |
| 5 | **Nao se apaga.** Se `ADR-0029` for retirado por `O9`, este registro **passa a historico e e preservado** — `FND-04 §7.2` etapa 5 |

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-31 | DEP-GOV | Criacao pelo **oitavo ato soberano** ([MSG-2026-0008](../memory/operacional/MSG-2026-0008-ato-soberano-emendas-e1-e-e3.md) item **II**), que ratificou `ADR-0029` e determinou expressamente que o registro **nascesse com o contador em `0`**. Institui as colunas de `SA-2`, o rito de `SA-4` e os cinco limites. **`0` atos superados, `0` instauracoes abertas, `8` atos vigentes superaveis.** |
