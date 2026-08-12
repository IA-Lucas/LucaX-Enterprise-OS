---
id: PS-2026-018
titulo: Pacote de decisao soberana — o ato C3 que grava o contrato fabrica-acervo e migra os dez setores CONVOCADOS da F34
tipo: relatorio
versao: 1.1.0
status: ativo
camada_memoria: operacional
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-08-12
atualizado_em: 2026-08-12
revisao_prevista: null
decisoes_relacionadas: [ADR-0007, ADR-0011, ADR-0038]
substitui: []
substituido_por: null
canal: REPORTE
emissor: DEP-GOV
destinatario: SOBERANO
ttl: ate decisao do Soberano
resumo: Submete ao Soberano a minuta do ato C3 unico que grava o contrato fabrica-acervo (F35 §2.2, copia literal) com forca normativa e migra os dez setores CONVOCADOS da F34 as Cartas dos Departamentos que os amparam, com a excecao de segregacao declarada no proprio ato, a aresta CAP-estrategia, a emenda da Carta PRO-nxtrack, as correcoes V1-V3 do F44 e a remedicao dos nove perfis de carregamento. Custo fixo do rito na execucao - 1 RFC, 1 ADR, 1 FIT, 1 REV e este ato - e marginal de 1 artefato por Departamento alcancado. Segue NAO emitida, NAO assinada e NAO aplicada.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
---

# PS-2026-018 — O ato **C3** da migracao e do contrato

> ## Este pacote **informa**. Nao decide, nao aprova, nao promulga e nao edita nada.
>
> A assinatura e do **SOBERANO, indelegavel** (`FND-04 §2`, linha C3). Enquanto nao assinado,
> **`0` bytes** mudam em Carta, Capability, Fundacional ou catalogo por causa deste pacote.
> Ao assinar, o ato entra como a proxima `MSG` da sequencia *(contador exercido na emissao,
> nunca lido — `V1` de `MEM-APR-0006`)* e a missao de aplicacao executa o rito completo.

## §1 — Por que UM ato, e o que ele custa

**A economia foi medida antes de ser proposta** *(2026-08-08, M-01; conferida em 2026-08-12)*:
o rito `C3` do contrato e o custo fixo da migracao **sao o mesmo rito** — `RFC` → analise de
impacto → `ADR` → ratificacao do SOBERANO + plano de reversao + `FIT` (`CV-07`) + `REV`.
Dois atos pagariam o fixo duas vezes; **um ato o paga uma**.

| Custo | Valor | Natureza |
|---|---|---|
| Fixo | **1 `RFC` + 1 `ADR` + 1 `FIT` + 1 `REV` + este ato** | medido no precedente (M-01) |
| Marginal | **1 artefato por Departamento alcancado** | derivado; o mapa do item II fixa o numero na aplicacao |
| Cascata | **os 9 perfis de carregamento REMEDIDOS** (item VII) | obrigacao de `DC-10`/`CC-03`/`AL-05`, nunca herdada |

## §2 — O TEXTO do contrato, copia literal de `F35 §2.2`

**Regra da fonte (§2.1 da F35): nao reacentuar, nao reescrever, nao renumerar.** O bloco entra
como esta — divergencia de caractere seria parafrase, nao copia:

```
CONTRATO ENTRE FABRICA E ACERVO
Decisao do Fundador, 2026-08-08. Texto identico nos dois lados.

1. A fabrica escreve o setor barato, sem ato, sem rito, sem baseline.
2. O setor e EXERCIDO antes de migrar. Setor nunca acionado nao tem o que
   migrar — migraria a descricao de um papel que ninguem exerceu.
3. O Enterprise recebe o setor como executor do Departamento que ja o ampara,
   quando ele passar no exercicio.
4. Enquanto nao migra, o setor vive na fabrica e a autoridade continua no
   acervo. A fabrica obedece a norma sem morar nela — a F21 citou
   CAP-engenharia §3 linha 77 literal, a F22 descobriu que a CAP-financeiro
   recusa duas das tres areas por escrito.
5. O gatilho de migracao e a F34, o exercicio de convocacao, que roda no fim
   da esteira com os dezenove escritos.
```

**Contexto FORA do bloco** *(quem o colar dentro introduz a divergencia que a regra impede)*:
a linha `5` diz *"dezenove"* — numero vigente no dia da gravacao —, **superado pela decisao `2`
do Fundador do mesmo dia** (*"a F34 roda com 20"*, `F36` BLOCO 0; reconciliacao integral no
handoff de 2026-08-12 da Oficina). **O gatilho DISPAROU e foi exercido:** a F34 fechou
**20/20** em 2026-08-12 — `10 CONVOCADO · 10 NAO CONVOCADO` *(F42–F46)*.

## §3 — A MINUTA DO ATO (os itens que o Soberano assina)

**I. GRAVA** o contrato fabrica↔acervo como norma do acervo, pelo veiculo que o rito emite na
aplicacao *(`RFC` → `ADR`, com o bloco de §2 como copia literal e o contexto fora do bloco)*.
Fundamento do `C3`, medido: as hipoteses de `FND-04 §2` incidem tres vezes — hierarquia
normativa *(linhas 1 e 4)*, direitos de decisao *(linha 5 poe o gatilho fora do acervo)* e a
propria Fundacao *(linha 3 pede executor que `FND-02 §10` proibe nesta fase — o ADR grava a
leitura compativel: "executor" = o Departamento que ampara, nunca agente novo)*.

**II. MIGRA os DEZ setores `CONVOCADO` da F34** — `aprendizado · agentops · qualidade ·
conhecimento · cio · financeiro · gente · coo · estrategia · dados` — para as Cartas dos
Departamentos que os amparam *(linha 3 do contrato)*:
- **Entram as 4 partes que cabem** *(medicao M-01)*: `POLITICAS`→B3/B4 · `PADRAO`→B10 §8 ·
  `QUALIDADE`→B8 §11 · `NAO FAZ`→B3 §4.
- **NAO entram `CARGOS` e `FERRAMENTAS`** — proibicao, nao lacuna: `FND-02 §10` *("nesta fase
  nao existem agentes")* e `ADR-0011 §5.4`.
- **O mapa setor→Carta e produzido na missao de aplicacao POR CUSTODIA DECLARADA** *(a
  Capability que o setor exerce aponta o custodio; conferencia de DEP-QAR)* — **nunca por
  juizo**. Setor cuja custodia nao estiver declarada na fonte *(candidatos ja visiveis:
  `financeiro` e `gente`, sem Departamento dedicado)* **VOLTA ao Soberano em lista nominal**,
  e nao se inventa sede.
- **Os DEZ `NAO CONVOCADO` nao migram** — linha 2 do contrato; cada um ja tem missao-teste
  definida a espera do objeto externo.
- **A ORIGEM recebe carimbo `MIGRADO` no mesmo lote** *(acrescentado na reemissao 1.1.0)*: cada
  documento de setor migrado, na Oficina, ganha carimbo externo apontando a Carta que passou a
  ser a sede — **texto original intacto, sob o lease de la** —, para que o setor **nunca viva em
  duas sedes com cara de fonte** *(a familia `RD-101`)*. Enquanto o carimbo nao existe, vale a
  linha 4 do contrato: a autoridade esta no acervo.

**III. DECLARA a excecao de segregacao, valida SO para este lote** *(decisao do Fundador de
2026-08-08, gravada para nao ser redecidida)*: `DEP-GOV` revisa Carta de Departamento e seu
`I-3` o impede de revisar a propria; neste lote, `DEP-QAR` revisa a Carta de `DEP-GOV` tendo a
propria Carta no mesmo lote. **A excecao nao cria precedente** e expira com a aplicacao.

**IV. FORMALIZA a aresta `CAP-estrategia` ← `aprendizado`** *(decisao D5 de 2026-08-12, dono
`DEP-EXE`)*: a fonte da Capability passa a declarar a consumidora que hoje a cita `0` vezes.

**V. EMENDA a Carta `PRO-nxtrack`** *(fecha o residuo do token 33 / `MSG-2026-0009`)*: a
afirmacao do hospedeiro sai do presente falso — o caminho `lucaX/My_WorkSpace/...` esta
**morto**, o repositorio proprio **existe** (`E:/LucasIA/Projetos/nxtrack`), e a ancora de
conteudo `tree b9b36be9…fb4b` esta **custodiada em bundle restauravel** nas duas sedes
*(recibo com sha256 `4c160d3e…e680735`)*.

**VI. ORDENA as tres correcoes do laudo F44** *(auditoria dos 31 `FIT` por independencia,
confirmada por reconto externo — `28·3·0`)*, nos gates que o proprio laudo fixa: **V1**
reavaliacao de `ADR-0004` por papel ≠ `DEP-QAR` *(gate `P6`)* · **V2** reavaliacao de
`ADR-0005` + correcao da nota `PI-10` que nega o conflito por omissao *(gate: a aplicacao
deste ato)* · **V3** autoria dos indices `M3` transferida a `DEP-GOV` ou regra que exclua
projecoes de `objeto_avaliado` *(gate: proxima emenda dos indices)*.

**VII. REMEDE os nove perfis de carregamento** *(`§13.2`)* apos a aplicacao — **remedidos,
nunca herdados** *(`DC-10`, `CC-03`, `AL-05`)*: dobrar o corpo das Cartas torna os perfis
falsos, e o numero novo entra contado por ferramenta.

**VIII. FIXA o plano de reversao** *(`RB-01`)*: copia datada verificada ANTES da primeira
escrita *(procedimento da primeira `Skill`)* · aplicacao em commits atomicos por item ·
reversao = `git revert` do(s) commit(s) de aplicacao + baseline remedida + declaracao no
lease. **Responsavel pela reversao: DEP-GOV; custo: 1 sessao.**

## §4 — O que este pacote NAO propoe

Migrar `NAO CONVOCADO` *(linha 2 do contrato veta)* · criar agente ou cargo executavel
*(`FND-02 §10`)* · promover qualquer coisa a `FND` · desligar o lucaX *(desmonte e a Onda 7,
com a custodia da ancora ja feita)* · emitir baseline por este pacote.

## §5 — Condicoes de parada da aplicacao

A missao de aplicacao **PARA e devolve ao Soberano** se: (a) a custodia declarada nao cobrir
algum setor do item II *(lista nominal volta, nada se inventa)*; (b) qualquer `H-P` de Carta
emendada nao reproduzir; (c) a baseline nao reproduzir antes da primeira escrita; (d) o
secret-scan acusar em qualquer candidato.

---

## Reemissoes

| Versao | Data | O que mudou |
|---|---|---|
| 1.1.0 | 2026-08-12 | **Revisao pedida pelo Fundador** *("revise e confirme que esta completa")*: o item II ganha a provisao do **carimbo `MIGRADO` na origem** — a revisao confrontou o §3 contra todas as decisoes fixadas e esta era a unica lacuna real *(dupla sede pos-migracao)*. Falso alarme descartado com medicao: o padrao de orcamento do legado e exclusao do DESMONTE *(F45 A3)*, nao das 4 partes que migram. `0` itens removidos, `0` decisoes reabertas |
| 1.0.0 | 2026-08-12 | Emissao original, sob token 42 |

---

**Assinatura:** ⬜ **NAO ASSINADO.** Para assinar, o Soberano despacha sobre este pacote
*(o despacho e o ato; a missao de aplicacao o registra como a proxima `MSG` e executa o rito
completo — `RFC` + `ADR` + `FIT` + `REV` — sob lease, com este §3 como letra)*.
