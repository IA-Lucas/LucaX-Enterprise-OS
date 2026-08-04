---
id: ADR-0034-primeira-skill-copia-datada
titulo: Criar a primeira Skill do acervo — copia datada com manifesto e verificacao, sob SK-01 a SK-26
tipo: adr
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-08-03
atualizado_em: 2026-08-03
revisao_prevista: 2027-02-03
decisoes_relacionadas: [ADR-0002, ADR-0033]
substitui: []
substituido_por: null
classe_mudanca: C2
tipo_decisao: 2
supera: null
superado_por: null
resumo: Cria SKL-custodia-criar-copia-datada, a primeira Skill do acervo, recebendo capacidade medida fora dele, e exerce GO-TO-SPECS-seguinte sem libera-lo.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# ADR-0034: A primeira `Skill` do acervo

## Contexto

[`ADR-0033`](ADR-0033-framework-de-skills.md) instituiu `SK-01` a `SK-26` em 2026-08-03 e
declarou, em `L1`, que as **26** regras nasciam **determinadas e nao observadas** — `0`
`Skill`s existiam. **O unico evento capaz de converter isso em observacao e a primeira `Skill`
real**, e e o gatilho de revisao que o proprio `ADR-0033` fixou.

## Decisao

**Criar [`SKL-custodia-criar-copia-datada`](../skills/SKL-custodia-criar-copia-datada.md)**, a
partir da capacidade `backup-datado`, construida e medida **fora do acervo**.

**A escolha e por medicao**, e o fundamento esta em
[`RFC-0029 §2`](../rfcs/RFC-0029-primeira-skill-copia-datada.md): maior sinal observado
*(`67` artefatos contra `22` e `56`)*, **`22`** usos reais registrados no lease, e **a unica
das tres que enderecça achado ABERTO de severidade ALTA** — **`RD-103`**.

## Classe

| Variavel | Valor | Fundamento |
|---|---|---|
| **Classe** | **`C2`** | `FND-04 §6`, linha *Skill* — **a classe do tipo**, e as tres pre-condicoes *(repete · verificavel · mais de um papel)* estao satisfeitas |
| **Instrumento** | **`RFC` → `ADR`** | `FND-04 §2.1`. `FND-04 §6` diz *"**alem** do rito da classe"* — as pre-condicoes **acrescem**, nao substituem |
| **Tipo** | **`2`** | `FND-04 §2.2`. Reversivel: `Skill` aposenta-se por `ADR` (`FND-09 §8.2` linha `SKL`) |
| **Aprova** | **DEP-EXE** | `FND-09 §8.2` linha `SKL` |
| **Ratifica** | **—** | `FND-09 §8.2` linha `SKL`. **`0` atos** |
| **Pre-condicao universal I** | ✅ | `CAP-governanca`, **`ativo`** (`VC-01`, `FND-08 §8`) |
| **Pre-condicao universal II** | ✅ | `SKL` consta do Meta Model — `FND-09 §E-13` |

**Custo do rito: `5` artefatos** — e e **exatamente** o de `SPC-001`, a primeira `Spec`
*(`RFC-0026` → `ADR-0031` → `SPC-001` → `FIT-2026-024` → `PT-2026-017`)*.

> **Correcao de leitura, e ela importa.** Dizer que `Skill` e *"o componente mais barato do
> acervo"* e verdadeiro **quanto a ratificacao** — `FND-09 §8.2` poe `—` em *Ratifica*, e
> **nenhum ato e necessario**. **Nao e verdadeiro quanto a instrumentos:** por ser `C2`, a
> **primeira** `Skill` custa os mesmos **5** que a primeira `Spec`. **O barato e o ato, nao o
> rito.** Registrado como observacao de `SK-10` em [`PT-2026-021 §3`](../governance/relatorio-transicao-2026-08-03-primeira-skill.md).

## O que muda

| # | Muda |
|---|---|
| 1 | **`skills/` passa a existir** — local ja declarado em `FND-03 §7` como *"(fase futura)"* e em `FND-03 §3.5` |
| 2 | **`GO-TO-SKILLS` passa a EXERCIDO** — a primeira `Skill` existe |
| 3 | As **26** regras saem de *determinadas* para **observadas**, e a medicao esta em `PT-2026-021 §4` |
| 4 | O nome da capacidade **muda por norma**: `backup-datado` → `custodia-criar-copia-datada`, por `SK-03` |

## O que este ADR NAO faz

| # | Nao faz | Verificacao |
|---|---|---|
| **N1** | **Nao LIBERA `GO-TO-SKILLS`** | **Exercer nao e liberar.** Liberar portao e **ato de autoridade** (`FND-01 §6.2`); exercer e criar o objeto que o portao guarda. Portoes de sequencia: **`GO-TO-SPECS` e `GO-TO-SKILLS`, 2 antes e 2 depois**, medidos **por nome** |
| **N2** | **Nao move codigo para o acervo** | **`0` bytes** de implementacao. A ficha **cita** o caminho externo; `SK-23` proibe copiar o que tem sede propria |
| **N3** | **Nao cria campo novo** | `capabilities` e `gatilho` sao **atributos minimos** de `FND-09 §E-13`, escritos a mao porque `TPL-skill` os omite (`AC-07`) |
| **N4** | **Nao emenda `TPL-skill` nem sana `RD-122`** | **`0` bytes** em `TPL-skill`. O achado e **exercido** aqui, nao corrigido |
| **N5** | **Nao promove `ADR-0033` a `FND`** | `C3 · Tipo 1` com ato. **O sinal agora existe** — e a decisao continua sendo de quem detem a materia |
| **N6** | **Nao cria entidade, tipo, template, papel nem portao** | `SKL` ja existe. `QG-0`–`QG-6`: **7 antes, 7 depois** |
| **N7** | **Nao admite os outros candidatos** | Seguem fora do acervo, intactos |

## Consequencias

| Para quem | O que muda |
|---|---|
| **Qualquer DEP** | Pode invocar a capacidade **por identificador**, com contrato declarado, antes de acao destrutiva |
| **DEP-GOV** | O ponto de retorno de cada lease passa a ter **instrumento nomeado**, e nao so pratica |
| **`RD-103`** | **NAO fecha.** O dano e irreversivel e o achado tem dono e gatilho proprios. **Esta `Skill` reduz a chance de repeticao; nao desfaz o ocorrido** |
| **`ADR-0033`** | Seu gatilho de revisao **disparou**: a primeira `Skill` existe |

## Rastreabilidade

| Campo | Conteudo |
|---|---|
| **Origem** | [RFC-0029](../rfcs/RFC-0029-primeira-skill-copia-datada.md) |
| **Framework** | [ADR-0033](ADR-0033-framework-de-skills.md) |
| **Objeto criado** | [`SKL-custodia-criar-copia-datada`](../skills/SKL-custodia-criar-copia-datada.md) |
| **Aptidao** | [FIT-2026-027](../governance/fitness/FIT-2026-027-primeira-skill.md) |
| **Registro** | [PT-2026-021](../governance/relatorio-transicao-2026-08-03-primeira-skill.md) |
| **Achados que NAO fecha** | `RD-103` · `RD-122` · `RD-123` · `RD-124` · `RD-116` |
