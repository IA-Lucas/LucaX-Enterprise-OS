---
id: RFC-0033-a-mente-reconhece-o-corpo
titulo: A Mente reconhece o Corpo — onde vive o runtime executavel do lucaX Enterprise, e como a Mente o governa sem que producao escreva na norma
tipo: rfc
versao: 1.0.0
status: aprovado
camada_memoria: nao-aplicavel
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-08-12
atualizado_em: 2026-08-12
revisao_prevista: null
decisoes_relacionadas: [ADR-0007, ADR-0011]
substitui: []
substituido_por: null
classe_mudanca: C2
prazo_analise: 2026-08-12
---

# RFC-0033: A Mente reconhece o Corpo

## Proposito

**Registrar em norma a fronteira que ja existe em fato.** Em 2026-08-11 nasceu, por mandato
direto do Fundador, o repositorio `lucax-enterprise` — o **runtime executavel** da plataforma
(FastAPI + LangGraph, Docker, Policy Engine, bilhetagem por tenant) —, e ele vive **fora** deste
acervo. A pergunta desta RFC: **onde essa fronteira fica escrita, e com que regras de
atravessamento?**

> **O sinal que motiva e MEDIDO, nao hipotetico:** este acervo ja pagou duas vezes por fronteira
> nao escrita — a regra de lease mais estreita que o fence foi **exercida** por sessao alheia
> antes de ser corrigida (QUARTO DESPACHO de 2026-08-02), e a familia `RD-101` e inteira feita de
> afirmacoes que valiam de um lado da fronteira e nao do outro. **Fronteira sem texto e porta
> aberta com aparencia de porta fechada.**

## Escopo

| Item | Definicao |
|---|---|
| **Entra** | O reconhecimento das **4 camadas** (Mente, Oficina, Corpo, Legado) com caminhos reais · a **membrana** Mente↔Corpo (quem escreve o que, por qual rito) · a relacao entre a Policy Engine do Corpo e `FND-04` |
| **NAO entra** | A migracao dos setores *(Onda 5, decisoes ja tomadas no pacote M-02 tarefa 5)* · promocao de coisa alguma a `FND` · o cutover do Legado *(Onda 7)* · specs de produto do Corpo *(Spec Framework, quando houver Produto)* · qualquer emenda Fundacional |
| **Fronteira** | Esta RFC nao poe **um byte** de codigo no acervo: reconhece o que vive fora e escreve as regras de atravessamento |

## 1. As alternativas, analisadas antes de escolher

| # | Alternativa | Analise | Veredito |
|---|---|---|---|
| **(a)** | **Runtime DENTRO do acervo** | `ADR-0007` separa acervo de producao; a baseline (`IR-BL/6`) mede **so `.md`** — codigo executavel dentro do fence seria massa nao-medida dentro do recurso medido, a receita exata de `RD-53` | ❌ |
| **(b)** | **Runtime fora, SEM reconhecimento formal** | E o estado de 2026-08-11 a 2026-08-12. A fronteira fica em `CLAUDE.md`/`MENTE.md` do proprio Corpo — **texto que a Mente nao le e nao versiona**. Repetiria a folga medida do lease: regra escrita so de um lado | ❌ |
| **(c)** | ⭐ **Runtime fora, reconhecido por ADR com membrana declarada** | A fronteira nasce com sede canonica, rito de mudanca (`RFC → ADR`) e regras de atravessamento nos dois sentidos | ✅ **escolhida** |

## 2. Pergunta clara

**Fica decidido que o lucaX Enterprise opera em 4 camadas — Mente (este acervo), Oficina
(`LucaX-Enterprise-Research`), Corpo (`lucax-enterprise`) e Legado (`lucaX`) — com a membrana
declarada no ADR-0038?**

## 3. Prazo e desfecho

Analise no proprio dia — o Fundador escolheu, entre tres opcoes apresentadas com a regra exata
(`FND-04` linha C2 + `CV-07`), o **rito inteiro** `RFC → ADR → FIT`. Desfecho: **aprovada**;
a decisao esta em [`ADR-0038`](../decisions/ADR-0038-a-mente-reconhece-o-corpo.md), avaliada por
[`FIT-2026-031`](../governance/fitness/FIT-2026-031-a-mente-reconhece-o-corpo.md).
