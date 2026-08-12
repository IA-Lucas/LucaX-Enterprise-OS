---
id: FIT-2026-031-a-mente-reconhece-o-corpo
titulo: Verificacao de aptidao — a Mente reconhece o Corpo (ADR-0038)
tipo: fitness-check
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: DEP-QAR
proprietario: DEP-QAR
aprovador: DEP-EXE
criado_em: 2026-08-12
atualizado_em: 2026-08-12
revisao_prevista: null
decisoes_relacionadas: [ADR-0007, ADR-0011, ADR-0038]
substitui: []
substituido_por: null
veredito: apto-com-ressalva
---

# FIT-2026-031 — A Mente reconhece o Corpo

**Objeto avaliado:** [`ADR-0038`](../../decisions/ADR-0038-a-mente-reconhece-o-corpo.md)
e [`RFC-0033`](../../rfcs/RFC-0033-a-mente-reconhece-o-corpo.md).
**Portao:** `QG-6`. **Obrigatorio** por ser `C2` (`CV-07`).

> **`FT-02`, `LV-03`:** parecer emitido pelo papel **DEP-QAR**. **`FT-10`:** parecer,
> **nao decisao** — nao se ratifica. Ver `R3`: a sessao unica e declarada, nao escondida.

## Veredito

**`apto-com-ressalva`.** **Tres** ressalvas — `R1` a `R3` —, **nenhuma bloqueia**.

## 1. `QG-6` — a arquitetura ficou mais apta a evoluir?

**Sim, e a prova e por ausencia medida: a fronteira mais exercida do sistema nao tinha sede
normativa.** O lease fenceia a Mente desde 2026-08-01, a Oficina existe desde antes, o Corpo
nasceu em 2026-08-11 — e **nenhum artefato do acervo declarava as camadas nem as regras de
atravessamento**. A membrana vivia so no `CLAUDE.md`/`MENTE.md` do Corpo, lado de fora. O
acervo ja mediu o custo de fronteira escrita so de um lado: a folga do lease foi **exercida**
antes de corrigida (2026-08-02). `ADR-0038` fecha essa classe para a fronteira Mente↔Corpo.

## 2. Conformidade — com sinal observavel

| # | Criterio | Sinal medido | Veredito |
|---|---|---|---|
| `F1` | **Instrumento determinado ANTES de redigir, por norma citada** | `FND-04` linha `C2` (`RFC → ADR`) + `CV-07` (FIT sem valvula). A contradicao com o plano ("1 ADR") foi levada ao Fundador **com a regra exata**, e o rito inteiro foi escolha dele — a dispensa de RFC estava disponivel e nao foi usada | ✅ |
| `F2` | **Materia e de ADR, nao de catalogo** | O precedente de 2026-08-10 (IR-BL/6 sem ADR) definiu o contraste: aquilo era fronteira de **medicao** (0 fato normativo); isto e **regra de atravessamento** — quem pode escrever o que, por qual rito. Regra e norma; norma pede ADR | ✅ |
| `F3` | **Baseline reproduzida ANTES da primeira escrita** | `254 · 74.696 · ceb9f14f… · 31f64326…`, `EXIT=0`, identica digito a digito ao estado pos-inscricao do token 37 — **0 deriva em 2 dias** | ✅ |
| `F4` | **Copia datada provada por CONTEUDO** | `_backups/LucaX-Enterprise-OS_2026-08-12_pre-onda-3`, **`VERIFICADO 650/650, saida 0`**, procedimento de `SKL-custodia-criar-copia-datada` *(quinto uso real)* | ✅ |
| `F5` | **Contadores EXERCIDOS, nao lidos** (`V1` de `MEM-APR-0006`) | Contra a copia datada: `ADR-0037` ✅ existe · `ADR-0038` ✅ NAO existe; `RFC-0032` ✅ existe · `RFC-0033` ✅ NAO existe; `FIT-2026-030` ✅ existe · `FIT-2026-031` ✅ NAO existe. **Os tres contadores estavam defasados** — ver `R2` | ✅ |
| `F6` | **`0` bytes em fonte normativa, codigo e medidor** | Nenhuma Fundacional, nenhum ADR anterior, `0` bytes em `IR-BL/6`, `0` bytes em `_SAIDA-COMPANY-OS/` | ✅ |
| `F7` | **Catalogo reconciliado na MESMA mudanca** (`CC-03`) | Tres linhas novas + versao `2.34.0` + changelog, nesta emissao | ✅ |
| `F8` | **O fato que o ADR reconhece EXISTE e foi provado** | Corpo: 10 commits, 25 testes verdes, pilha Docker do zero com RLS `EXIT=0` como `app_rt`, fluxo approve com trilha — provado em 2026-08-12, antes deste rito | ✅ |
| `F9` | **Numero so entra contado por ferramenta** | A unica transcricao de cabeca da sessao (impressao digital, no lease) **errou digitos e foi corrigida no ato, com nota declarada** — o metodo funcionou ao falhar | ✅ |

## 3. ⚠️ `R1` — o acervo passa a apontar para tres repositorios que nao mede

`ADR-0038 §1` grava caminhos reais de Oficina, Corpo e Legado. A baseline nao os cobre; o
ponteiro **vai** envelhecer (precedente `A-297`: 29 ponteiros mortos). Mitigacao aceita: sede
unica (a tabela do §1) e correcao por sucessor. **Dono do risco: DEP-GOV. Gatilho: qualquer
mudanca de caminho das camadas.**

## 4. ⚠️ `R2` — os TRES contadores de sequencia estavam defasados, quinta ocorrencia da familia

`decisions` dizia proximo `0037` (existia desde 2026-08-03), `rfcs` dizia `0032` (existia),
`fitness` dizia `029` (**dois** atras — `029` e `030` existiam). E a familia de `RD-32`/
`RD-95` (`CV-04`, `SF-32`: criar artefato e incrementar contador sao a mesma mudanca) — a
missao 1.13.14 registrou a nota de exercicio e **nao moveu o cabecalho**. Corrigidos nesta
emissao, com o achado registrado nos tres indices. **O sinal e de reincidencia estrutural:
o contador que se corrige por nota continua errando por cabecalho.**

## 5. ⚠️ `R3` — o rito inteiro correu numa unica sessao, e a separacao e de papel, nao de pessoa

RFC, ADR e FIT sairam da mesma sessao operadora, sob o mesmo token 38. `FT-02` exige que quem
avalia nao tenha produzido o avaliado — aqui a separacao e **por papel** (DEP-QAR avalia o que
DEP-GOV redigiu), como em todo o precedente do acervo, mas o conflito estrutural fica
**declarado em vez de omitido** (mesmo criterio de `FIT-2026-030`, que declarou o proprio).
Mitigacao real: os sinais de `F3`, `F4`, `F5` e `F8` sao **mecanicos** — reproduziveis por
qualquer sessao futura contra a copia datada e o git, sem confiar no autor.
