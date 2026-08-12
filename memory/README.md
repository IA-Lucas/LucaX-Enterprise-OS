---
id: IDX-memory
titulo: Indice da Memoria Organizacional
tipo: relatorio
versao: 1.3.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-KMS
aprovador: DEP-GOV
criado_em: 2026-07-28
atualizado_em: 2026-07-29
revisao_prevista: null
decisoes_relacionadas: [ADR-0001, ADR-0009, ADR-0010]
substitui: []
substituido_por: null
resumo: Indexa as cinco camadas da memoria, o criterio de alocacao e as regras de curadoria, e aponta onde gravar cada fato.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# Memoria Organizacional

## Proposito
Indexar as cinco camadas da memoria do LucaX e servir de porta de entrada para gravacao e
recuperacao. A arquitetura completa esta em
[FND-06](../foundation/06-arquitetura-memoria.md).

## Escopo
Todo registro persistente de conhecimento organizacional. Nao inclui decisoes (que vivem em
`../decisions/`) — a memoria **referencia** decisoes, nunca as reescreve (MM-07).

## Responsaveis
| Papel | Responsavel |
|---|---|
| Curador de todas as camadas | DEP-KMS |
| Dono do conteudo | varia por camada, ver tabela |
| Auditoria de proveniencia | DEP-GOV |

---

## As cinco camadas

| Camada | Diretorio | Pergunta que responde | Dono | TTL | Autoridade |
|---|---|---|---|---|---|
| **EST** Estrategica | [`estrategica/`](estrategica/) | Por que existimos? Para onde vamos? | DEP-GOV | Permanente | 1 |
| **PRD** Produto | [`produto/`](produto/) | O que construimos e para quem? | DEP-PRD | Vida do produto | 2 |
| **TEC** Tecnica | [`tecnica/`](tecnica/) | Como esta feito e por que assim? | DEP-ENG | Vida do componente | 3 |
| **APR** Aprendizado | [`aprendizado/`](aprendizado/) | O que aprendemos ao fazer? | DEP-KMS | Ate refutacao | **4** |
| **OPR** Operacional | [`operacional/`](operacional/) | O que esta acontecendo agora? | DEP-OPS | 1 ciclo | 5 |

**Autoridade:** em conflito entre registros, vence o de numero menor (MM-03).

> **Correcao de projecao — item de `RD-35`.** Esta coluna declarava **`5`** para **APR**, o mesmo
> valor de **OPR**, e a fonte — [FND-06 §2](../foundation/06-arquitetura-memoria.md) — declara
> **`4`**. Com dois valores iguais, **`MM-03` ficava indeterminado**: *"vence o de numero menor"*
> nao decide entre dois cincos. O proprio
> [`aprendizado/README`](aprendizado/README.md) sempre declarou **`4`**. **Corrigido na
> projecao; a fonte nao foi tocada** (`PJ-03`, `RG-03`, `M3`).

## Onde gravar — criterio de alocacao

A **primeira resposta afirmativa** define a camada (garante MM-01: um fato, um lugar).

```
1. Define quem somos, para onde vamos ou como decidimos?     -> EST
2. Descreve o que construimos, para quem, ou por que vale?   -> PRD
3. Descreve como algo esta feito e por que assim?            -> TEC
4. E licao generalizavel extraida de experiencia vivida?     -> APR
5. Descreve o estado corrente da execucao?                   -> OPR
6. Nenhuma das anteriores  -> NAO E MEMORIA. Descartar ou converter no instrumento certo.
```

Casos ambiguos resolvidos: [FND-06 §4.1](../foundation/06-arquitetura-memoria.md).

## Estado atual

| Camada | Registros | Observacao |
|---|---|---|
| EST | **1** | [MEM-EST-0001](estrategica/MEM-EST-0001-contexto-do-soberano.md) — Contexto do Soberano, **`ativo`**, ratificacao **ratificada** pelo ato soberano de 2026-07-28 ([MSG-2026-0002](operacional/MSG-2026-0002-ato-soberano-cartas-comando-plataforma-e-contexto.md)), com as **11 lacunas `unknown` intactas**. O demais conteudo estrategico vigente e a propria Fundacao (`../foundation/`) |
| PRD | 0 | Nenhum produto criado — fase de fundacao |
| TEC | 0 | Nenhum componente construido — fase de fundacao |
| APR | **8** | [MEM-APR-0001](aprendizado/MEM-APR-0001-ratificacao-por-precedente.md) — ressalva escrita nao neutraliza condicao de validade · [MEM-APR-0002](aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md) — detectar duplicacao nao previne duplicacao · [MEM-APR-0003](aprendizado/MEM-APR-0003-campo-de-estado-em-artefato-imutavel.md) — campo de estado em artefato imutavel · [MEM-APR-0004](aprendizado/MEM-APR-0004-projecao-revela-divergencia-antiga.md) — projecao revela divergencia antiga · [MEM-APR-0005](aprendizado/MEM-APR-0005-medir-a-ausencia-na-fonte-errada.md) — buscar o termo em vez da funcao produz achado de lacuna onde ha titular declarado · [**MEM-APR-0006**](aprendizado/MEM-APR-0006-exercer-o-contador-revela-o-defeito.md) — **exercer o instrumento revela o defeito que ler o instrumento nao revela** · [**MEM-APR-0007**](aprendizado/MEM-APR-0007-plausibilidade-nao-e-verificacao.md) — **plausibilidade nao e verificacao** *(a primeira licao nascida FORA do acervo: convocacao F42 da Oficina, promovida por despacho do Fundador de 2026-08-12)* · [**MEM-APR-0008**](aprendizado/MEM-APR-0008-campo-obrigatorio-com-escape-vazio.md) — **campo obrigatorio com escape vazio e falso cumprimento** |
| OPR | **6** | Os **seis** atos soberanos, de [MSG-2026-0001](operacional/MSG-2026-0001-ato-soberano-ratificacao-cartas-piloto.md) a [**MSG-2026-0006**](operacional/MSG-2026-0006-ato-soberano-aplicacao-integral.md), enumerados em [`operacional/README`](operacional/README.md) — **fonte** desta linha. Em todos, o efeito duravel foi **promovido no mesmo ato** ao instrumento proprio (FND-03 §3.13), de modo que a expiracao por `ttl` nao perde fato algum |

> **Correcao de projecao — item de `RD-35`.** A linha **OPR** declarava **`3`** registros e
> enumerava `MSG-0001` a `MSG-0003`, quando `memory/operacional/` contem **seis** — **tres
> missoes de atraso**, sendo `MSG-2026-0006` o **sexto ato soberano**, cuja aplicacao integral
> sustenta a baseline vigente. A enumeracao foi **substituida por remissao a fonte** (`PJ-01`),
> para que a linha **nao possa envelhecer outra vez**. **Corrigido na projecao; nenhuma fonte
> alterada** (`PJ-03`, `RG-03`, `M3`). **Decima primeira ocorrencia** da familia de
> [MEM-APR-0002](aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md), e a causa
> continua sendo `CV-04`.

## Regras essenciais

| # | Regra |
|---|---|
| MM-01 | **Um fato, um lugar.** Copiar entre camadas e proibido — referencie por ID. |
| MM-02 | Todo registro tem proveniencia: origem, autor, data, evidencia. |
| MM-04 | Promocao exige evidencia, nao repeticao. |
| MM-05 | **Esquecer e funcao.** OPR expira por padrao; memoria sem higiene vira ruido. |
| MM-09 | **Append-first.** Corrige-se acrescentando e superando, nunca apagando. |
| MM-10 | Nenhuma credencial, nenhum dado sensivel (PI-08). |

## Quando consultar e obrigatorio

| Momento | Camadas |
|---|---|
| QG-0 — antes de iniciar qualquer trabalho | APR + camada do dominio |
| Antes de decidir (C2/C3) | EST + APR + camada do dominio |
| Antes de construir | PRD + TEC |
| Antes de aceitar entrega (QG-3) | PRD + APR |
| Antes de comunicar externamente | EST + PRD |
| Antes de especializar (PI-14) | APR |

> "Nao encontrei" e resposta valida e obrigatoria. Inventar memoria e LV-12.

## Regime especial da camada EST

Conhecimento **sobre o Soberano** registrado em EST segue, alem das regras acima, o Contrato de
Conhecimento sobre o Soberano — [ADR-0010 §5](../decisions/ADR-0010-contrato-de-conhecimento-do-soberano.md),
**fonte** das suas regras, remetida por [FND-06 §3.1](../foundation/06-arquitetura-memoria.md) e
nao reproduzida aqui (PJ-01). Em uma linha: **proveniencia por afirmacao, lista fechada de
conteudo proibido, carregamento por pacote e autoridade nenhuma.**

Template: [`TPL-memoria`](../foundation/templates/TPL-memoria.md)

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-GOV | Indice inicial das cinco camadas. |
| 1.1.0 | 2026-07-28 | DEP-GOV | Registra o primeiro artefato da camada EST e remete ao regime especial de [ADR-0010](../decisions/ADR-0010-contrato-de-conhecimento-do-soberano.md). Frontmatter passa a declarar os cinco campos do contrato de artefato (AC-08, **ADR-0009**), fechando o achado C13 quanto a este artefato — e sanando, por **AC-11**, a alteracao nao versionada da Missao 1.4. |
