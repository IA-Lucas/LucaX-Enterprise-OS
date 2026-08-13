---
id: IDX-mem-operacional
titulo: Camada Operacional da Memoria
tipo: relatorio
versao: 1.5.0
status: ativo
camada_memoria: operacional
autor: DEP-GOV
proprietario: DEP-OPS
aprovador: DEP-KMS
criado_em: 2026-07-28
atualizado_em: 2026-08-01
revisao_prevista: null
decisoes_relacionadas: [ADR-0001]
substitui: []
substituido_por: null
---

# Camada OPR — Memoria Operacional

## Proposito
Guardar o estado corrente da execucao: o que esta em curso, o que esta bloqueado, o que
acabou de acontecer. Definicao completa em
[FND-06 §3.4](../../foundation/06-arquitetura-memoria.md).

## Escopo
| Item | Definicao |
|---|---|
| Pergunta que responde | O que esta acontecendo agora? |
| Volatilidade | **Alta** — unica camada projetada para ser efemera |
| TTL | **1 ciclo**, renovavel enquanto o item estiver ativo. `ttl` e campo obrigatorio (FM-02). |
| Autoridade em conflito | 5 — a mais baixa |

## Responsaveis
| Papel | Responsavel |
|---|---|
| Dono | DEP-OPS |
| Escreve | **Todos** os departamentos |
| Le | DEP-EXE para priorizar; todos para saber onde estao |
| Curador | DEP-KMS (expiracao e promocao a cada fechamento de ciclo) |

---

## Pertence a esta camada
- Trabalho em curso, fila e alocacao vigente
- Estado de portoes, handoffs pendentes, bloqueios
- Runbooks e procedimentos operacionais correntes
- Incidentes operacionais abertos e recentes
- Registro de backups, verificacoes e execucoes de rotina
- Consumo, custo e limites do ciclo corrente
- Excecoes formais vigentes e seus prazos
- Notas de Decisao (C1, Tipo 2, escopo local)

## **Nao** pertence
| Conteudo | Vai para |
|---|---|
| Qualquer coisa que precise sobreviver ao ciclo sem ser promovida | a camada correspondente |
| Decisao relevante | ADR (`../../decisions/`) |
| Licao | APR |
| Fato duravel sobre o produto | PRD |
| Fato duravel sobre o sistema | TEC |

## Regra de escrita
> Esta e a unica camada onde **expiracao e o comportamento padrao**.

| Ao fim do ciclo | Acao |
|---|---|
| Item ainda importa | **Promover** (FND-06 §5) ou renovar com justificativa |
| Item nao promovido | **Expira.** Presume-se irrelevante — e essa presuncao e desejada. |

> Sem TTL agressivo aqui, a memoria vira log; log vira ruido; ruido aumenta contexto e
> derruba a qualidade de todo o resto (MM-05, PI-14).

## Higiene obrigatoria

| Rotina | Frequencia | Executa |
|---|---|---|
| Expiracao de TTL vencido | Fim de cada ciclo | DEP-KMS |
| Promocao do que sobreviveu | Fim de cada ciclo | DEP-KMS + dono da camada de destino |
| Verificacao de excecoes vencidas | Fim de cada ciclo | DEP-GOV |

## Registros

| ID | Titulo | TTL | Status |
|---|---|---|---|
| [MSG-2026-0001](MSG-2026-0001-ato-soberano-ratificacao-cartas-piloto.md) | **Ato Soberano** de aprovacao e ratificacao das Cartas DEP-QAR e DEP-ENG | 1 ciclo — **expira sem perda** | `ativo` |
| [**MSG-2026-0002**](MSG-2026-0002-ato-soberano-cartas-comando-plataforma-e-contexto.md) | **Ato Soberano** de ratificacao de DEP-EXE, DEP-KMS e MEM-EST-0001, acolhimento de FIT-2026-001/002 e determinacao da Primeira Revisao Estrutural | 1 ciclo — **expira sem perda** | `ativo` |
| [**MSG-2026-0003**](MSG-2026-0003-ato-soberano-emenda-qar-e-criterio-de-consolidacao.md) | **Ato Soberano** de ratificacao da emenda **DEP-QAR 1.1.0** e determinacao do **criterio de consolidacao** que responde a PS-1 | 1 ciclo — **expira sem perda** | `ativo` |
| [**MSG-2026-0004**](MSG-2026-0004-ato-soberano-cartas-emenda-constitucional-e-regime-do-fitness-check.md) | **Ato Soberano** de ratificacao das **cinco** Cartas de Departamento, de **ADR-0014** com promulgacao de **FND-01 1.4.0**, e determinacao do **regime do `Fitness Check`** | 1 ciclo — **expira sem perda** | `ativo` |
| [**MSG-2026-0005**](MSG-2026-0005-ato-soberano-aplicacao-dep-qar.md) | **Ato Soberano** de liberacao da **aplicacao** de `DEP-QAR` **1.2.0**, manutencao de `DEP-KMS` e `DEP-ENG` **sem ratificacao** e determinacao da **Missao 1.11** | 1 ciclo — **expira sem perda** | `ativo` |
| [**MSG-2026-0006**](MSG-2026-0006-ato-soberano-aplicacao-integral.md) | **Ato Soberano** de ratificacao de **ADR-0016 a ADR-0019**, promulgacao de **FND-01 1.5.0**, **FND-02 1.3.0**, **FND-09 1.5.0 cumulativa** e **FND-10 1.4.0 cumulativa**, e ratificacao e **ativacao** de `DEP-KMS` **1.1.0** e `DEP-ENG` **1.1.0** — **dez objetos**, com ordem obrigatoria de aplicacao e prova final determinada | 1 ciclo — **expira sem perda** | `ativo` |
| [**MSG-2026-0007**](MSG-2026-0007-ato-soberano-vigencia-do-framework-de-specifications.md) | **Ato Soberano** de ratificacao de **ADR-0022** e **ADR-0024**, aprovacao de **ADR-0023** e **ADR-0025**, promulgacao de **FND-11 1.0.0** *(criacao)*, **FND-01 1.7.0 cumulativa**, **FND-02 1.4.0**, **FND-03 1.6.0** e **FND-10 1.5.0**, e ativacao das **cinco** Cartas **1.1.0** — **catorze objetos, o maior ato do acervo** | 1 ciclo — **expira sem perda** | `ativo` |
| [**MSG-2026-0008**](MSG-2026-0008-ato-soberano-emendas-e1-e-e3.md) | **Ato Soberano** de resposta a **`Q2`** *(**emendar `ADR-0007` agora**)*, autorizacao a **DEP-EXE** para aprovar **`ADR-0027`** no rito `C2`, **ratificacao de `ADR-0029`** e **adiamento expresso de `E2`** — **ancorado no `H-A` da minuta `PS-2026-015` 1.2.0**, e o **primeiro ato do acervo registrado ANTES da aplicacao** | 1 ciclo — **expira sem perda** | `ativo` |
| [**MSG-2026-0009**](MSG-2026-0009-ato-soberano-admissao-do-nxtrack.md) | **Ato Soberano** de **ratificacao de `ADR-0030`**, **aprovacao de `RFC-0025`** e **criacao do Produto `PRO-nxtrack`** pelo portao de origem externa, com `G0` = `IDENTIDADE` e `G3` = `RECOGNIZE` — **ancorado no `H-A` do pacote `PS-2026-016` 1.2.0**, itens **I a VII**, linhas **185–328**. Grava **`Q2` como artefato pela primeira vez**. **Segundo ato registrado ANTES da aplicacao** | 1 ciclo — **expira sem perda** | `ativo` |

> **Nove atos, nove fontes canonicas — nunca uma fonte que acumule.** `MSG-2026-0001` **nao foi
> editado** para receber o segundo ato. Cada Diretiva guarda **um** ato, e os indices
> referenciam a secao correspondente (CM-09, PJ-01).

> **Primeira instancia desta camada, e a primeira do tipo documental `Diretiva`** (FND-10 §4.6).
> Nenhum tipo, entidade ou diretorio foi criado: `MSG` e entidade desde ADR-0003 e o tipo
> consta de FND-10 §4.6 desde a fundacao.

> **Por que um ato soberano pode viver na camada efemera.** FND-03 §3.13 determina que mensagem
> portadora de **fato duravel** seja **promovida ao instrumento proprio** (FND-05 §9.1). A
> promocao ocorreu **no mesmo ato**: o estado de ratificacao vive no campo `ratificacao` de cada
> Carta (FND-10 §5.4), a vigencia no campo `status`, e o vinculo ID × versao × hash no
> [catalogo mestre §10](../../governance/artifact-registry.md). **Se este registro expirar,
> nenhum fato duravel se perde** — o que ele guarda e o **ato**, transcrito para que a fonte
> permaneca percorrivel (LN-07).

> **Contador `MSG-2026-NNNN`: ultimo atribuido `0014`; proximo `0015`** (FND-03 §2.3).
>
> **Contador exercido (2026-08-12, decimo segundo ato):** `0011` ✅ existe · `0012` ✅ NAO existia — `V1`; movido na mesma mudanca.
>
> **⚠️ Contador exercido — e estava DEFASADO EM DOIS (2026-08-12, aplicacao do PS-2026-018), familia de `RD-32`, SEXTA ocorrencia:** dizia `0009/0010` com `MSG-2026-0010` existindo desde 2026-08-02. Antes de atribuir **`0011`**: **`0010` ✅ existe · `0011` ✅ NAO existe** contra a copia datada *(`_backups/LucaX-Enterprise-OS_2026-08-12_pre-aplicacao-ps018-t44/`)* — `V1` de MEM-APR-0006. Corrigido aqui.
> **`RD-68` — o gatilho DISPAROU nesta emissao, e o contador estava CERTO.** O gatilho registrado
> era *"proxima emissao de `MSG`"*; ela ocorreu, e o contador declarava *"ultimo `0008`; proximo
> `0009`"* **enquanto a tabela acima listava `MSG-2026-0008`** — **concordam**. `MSG-2026-0009` foi
> numerado por esse valor, e o incremento acompanha a criacao na **mesma mudanca** (`SF-32`).
> **Primeira vez que o contador e exercido e nao reprova.** **A CAUSA permanece ABERTA:** `CV-04`
> continua **sem gatilho automatico** neste indice, e a correcao de uma emissao **nao instala
> mecanismo** — dono **DEP-GOV**, gatilho *"proxima emissao de `MSG`"*.
>
> **`RD-68`, enunciado original — o contador estava UMA emissao atras.** Declarava *"ultimo `0006`; proximo `0007`"*
> **enquanto a tabela acima ja listava `MSG-2026-0007`**, de 2026-07-30. **Encontrado ao EXERCER o
> contador** para numerar `MSG-2026-0008` — nao ao le-lo. **O valor foi corrigido aqui por obrigacao de
> `SF-32`**, e a **causa fica ABERTA**, sem missao designada: dono **DEP-GOV**, gatilho *"proxima emissao
> de `MSG`"*. **Setima ocorrencia** da familia de
> [MEM-APR-0006](../aprendizado/MEM-APR-0006-exercer-o-contador-revela-o-defeito.md) e `RD-32`.
> **O contador estava parado em `0001` desde a criacao deste indice**, enquanto cinco atos ja
> haviam sido numerados — divergencia **de projecao, nunca de fonte** (RG-03, PJ-03), corrigida
> aqui na reconciliacao determinada por §X.7 do ato de 2026-07-29. **Nenhum numero foi
> reaproveitado** e nenhuma Diretiva foi renumerada.

> **Correcao `C0` aplicada em 2026-07-29 — versao `1.2.1`, achado `RD-29`.** Este indice
> declarava `atualizado_em: 2026-07-28` **enquanto ja listava `MSG-2026-0006`**, de 2026-07-29:
> a atualizacao derivada foi feita **sem registrar a data**, e a data de um indice e evidencia de
> atualidade. Corrigido como **editorial** — `atualizado_em` + incremento de **CORRECAO** (FND-04
> §2, C0) —, o que **nao dispara** a obrigacao dos cinco campos do contrato (`AC-09`, `AC-11`).
> Registro em [PT-2026-006 §7.2](../../governance/relatorio-transicao-2026-07-29-fechamento-operacional.md).

Template: [`TPL-memoria`](../../foundation/templates/TPL-memoria.md) ·
Nota de decisao: [`TPL-nota-decisao`](../../foundation/templates/TPL-nota-decisao.md)
