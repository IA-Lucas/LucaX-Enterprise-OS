---
id: FIT-2026-028-segunda-skill
titulo: Verificacao de aptidao — a segunda Skill do acervo (ADR-0035)
tipo: fitness-check
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: DEP-QAR
proprietario: DEP-QAR
aprovador: DEP-EXE
criado_em: 2026-08-03
atualizado_em: 2026-08-03
revisao_prevista: null
decisoes_relacionadas: [ADR-0033, ADR-0034, ADR-0035]
substitui: []
substituido_por: null
veredito: apto-com-ressalva
---

# FIT-2026-028 — A segunda `Skill`

**Objeto avaliado:** [`ADR-0035`](../../decisions/ADR-0035-segunda-skill-varrer-credencial.md) e
[`SKL-seguranca-varrer-credencial`](../../skills/SKL-seguranca-varrer-credencial.md).
**Portao:** `QG-6`. **Obrigatorio** por ser `C2`.

> **`FT-02`, `LV-03`:** executado por **DEP-QAR**, que **nao** produziu o avaliado.
> **`FT-10`:** parecer, nao decisao — nao se ratifica.

## Veredito

**`apto-com-ressalva`.** Tres ressalvas, **nenhuma bloqueia**: `R1`, `R2` e `R3`.

## 1. `QG-6` — a arquitetura ficou mais apta a evoluir?

**Sim, e por um motivo diferente do da primeira vez.** `FIT-2026-027` registrou que *"Framework so
se prova sendo usado"*. **Este parecer registra o passo seguinte: Framework so se DIAGNOSTICA sendo
usado DUAS vezes.** Com `n = 1` os tres defeitos eram **hipoteses sobre a regra**; com `n = 2` sao
**propriedades medidas**, porque reapareceram identicos em capacidade sem nada em comum com a
primeira.

**E a cobertura do proprio Framework subiu de forma que so a segunda instancia permite:** **`25`
das `26`** regras ja foram exercidas em ao menos uma das duas fichas.

## 2. Conformidade — com sinal observavel

| # | Verificacao | Sinal | Resultado |
|---|---|---|---|
| `F1` | **O candidato cabe sob `SK-01` a `SK-26`** | Testado **antes** de propor, com poder de PARAR a missao. **Nenhuma das 26 recusa**; `SK-03` reprovou o **nome** e o corrigiu | ✅ |
| `F2` | **Pre-condicoes de `FND-04 §6` linha *Skill*** | repete ✓ · verificavel ✓ · mais de um papel ✓ — **3 de 3** | ✅ |
| `F3` | **Pre-condicao universal I** | `CAP-seguranca`, **`ativo`**, custodio DEP-QAR — **conferido no frontmatter, nao de memoria** (`VC-01`) | ✅ |
| `F4` | **Pre-condicao universal II** | `SKL` consta do Meta Model — `FND-09 §E-13` | ✅ |
| `F5` | **Rito da classe cumprido** | `C2` → `RFC-0030` → `ADR-0035`, aprova `DEP-EXE` | ✅ |
| `F6` | **Sinal de `SK-20` observado, nunca antecipado** | **`14`** tokens do lease · **`22`**/**`56`** artefatos, com **controle positivo `217`** e **negativo `0`** · **`476`** blobs · portao em producao **`8/8`** | ✅ |
| `F7` | **`0` campos novos** | `capabilities` e `gatilho` sao **atributos minimos** de `FND-09 §E-13` (`AC-07`) | ✅ |
| `F8` | **`0` bytes de codigo no acervo** | A ficha **cita** o caminho externo; nada foi movido | ✅ |
| `F9` | **Autoverificacao** | `autor` DEP-GOV · `revisor` DEP-QAR · `aprovador` DEP-EXE — distintos (`AC-03`) | ✅ |
| `F10` | **`SK-22` — nao e duplicata** | Conferido no catalogo contra a `Skill` existente: **`0` passos comuns, `0` saidas comuns, `CAP` distintas** | ✅ |
| `F11` | **`GO-TO-SKILLS` nao LIBERADO** | Portoes de sequencia medidos **por nome**: **2 antes, 2 depois**. `QG-0`–`QG-6`: **7 e 7** | ✅ |
| `F12` | **A reavaliacao das 26 com `n = 2` foi produzida** | `PT-2026-022 §4`: **22 / 1 / 2 / 1** | ✅ |
| `F13` | **`SK-24` foi CALCULADA, e nao apenas declarada calculavel** | Mediana **181,5**, limiar **363**, maior instancia **188** — mais a demonstracao algebrica de que **nenhum valor dispara em `n = 2`** | ⚠️ **`R1`** |
| `F14` | **Os defeitos sao do Framework ou do caso?** | **Do Framework** — `SK-09` e `SK-10` reprovaram **identicamente** em capacidade sem materia comum | ⚠️ **`R2`** |
| `F15` | **`TPL-skill` produz ficha conforme?** | **Nao** — omite `capabilities` e `gatilho` pela **segunda** vez | ⚠️ **`R3`** |
| `F16` | **O custo do rito caiu com a repeticao?** | **Nao.** **`5` artefatos**, identico ao da primeira | ✅ *(medido; a leitura esta em `R2`)* |

## 3. `R1` — `SK-24` esta pior do que o parecer anterior disse, e DEP-QAR corrige o proprio registro

**`FIT-2026-027 §4`, de autoria deste mesmo Departamento, classificou `SK-24` como insuficiente
por ser *"incalculavel com 1 instancia"*. A palavra estava errada.** A mediana de um conjunto de um
elemento **e** esse elemento; o teste sempre foi calculavel. **O que ele nao era — e continua nao
sendo em `n = 2` — e capaz de disparar.**

`ADR-0035 §1.2` demonstra: com duas instancias `a ≤ b`, o limiar e `a + b`, e `b > a + b` exigiria
`a < 0`. **Um teste que so pode devolver *"nao"* nao esta medindo nada.**

**DEP-QAR registra a correcao em vez de emenda-la em silencio** — emendar seria a familia de
`RD-101` dentro de um parecer. **A conclusao operacional de `FIT-2026-027` sobrevive intacta: `SK-24`
so decide a partir da terceira `Skill`.** O que muda e o fundamento, que passou de conjectura a
demonstracao.

**Nao bloqueia:** a `Skill` avaliada **cumpre** `SK-24` no que a regra realmente exige — custo de
contexto **medido**, e ficha **escrita em blocos rotulados e independentes**, carregaveis em parte.

## 4. `R2` — os tres defeitos sao do Framework, e agora isso e medido

| Regra | Primeira `Skill` | Segunda `Skill` | Veredito de DEP-QAR |
|---|---|---|---|
| **`SK-09`** | ❌ defeituosa — erro de categoria | ❌ **defeituosa, identicamente** | **Do Framework.** O enunciado soma atributo de frontmatter com blocos de corpo; **as duas fichas tiveram de materializar o gatilho duas vezes** |
| **`SK-10`** | ⚠️ insuficiente | ⚠️ **insuficiente, e agora com prova de custo** | **Do Framework.** A segunda custou os mesmos **`5`** artefatos; a leitura *"Skill e barata"* **sobreviveu ao segundo uso** |
| **`SK-24`** | ⚠️ insuficiente *(por motivo errado)* | ⚠️ **insuficiente, natureza corrigida** | **Do Framework.** Falta o **piso de `n`** no enunciado |

**As duas capacidades nao compartilham materia, `Capability`, consumidor, idempotencia nem modo de
falha.** Defeito que reaparece igual em casos disjuntos **e da regra**.

**Nao bloqueia, e a razao continua sendo de sede:** `ADR-0033` e **`M1`** — corrigi-los exige `ADR`
sucessor, **rito proprio**, que o despacho desta missao expressamente nao autorizou.

**Comparacao que DEP-QAR registra:** `SPC-001` achou **5 em 32 (15,6%)**; a primeira `Skill`,
**3 em 26 (11,5%)**; **esta, os mesmos 3 em 26** — e o dado novo e que **`0` defeitos novos
apareceram no segundo uso**. **A taxa nao subiu; o diagnostico ficou firme.**

## 5. `R3` — o template continua para tras, e a repeticao muda a natureza do achado

**`RD-122`, ABERTO, exercido pela SEGUNDA vez.** Com `1` ficha, escrever `capabilities` e `gatilho`
a mao podia ser peculiaridade daquele caso. **Com `2` fichas independentes, e propriedade do
template:** `TPL-skill` **nao produz `Skill` conforme**, e **toda** `Skill` futura pagara o mesmo
atrito ate o achado ser sanado.

**Nao bloqueia:** os campos sao exigidos pela norma e escreve-los a mao **nao cria campo novo**
(`AC-07`). **O custo e de atrito e de risco de omissao futura**, e ele agora tem **duas ocorrencias
medidas** em vez de uma.

## 6. Recomendacao

**`QG-6` LIBERADO.**

**Sobre o `ADR` sucessor, DEP-QAR recomenda ESPERAR a terceira `Skill` — e a recomendacao mudou de
fundamento desde `FIT-2026-027`.** Os tres defeitos estao **confirmados**, e dois deles
(`SK-09`, `SK-10`) ja poderiam ser redigidos hoje. **`SK-24` nao pode:** o piso de `n` que falta ao
enunciado **so se mede quando o teste puder disparar**, e isso ocorre **na terceira instancia**.
Abrir o sucessor agora **corrigiria dois com sinal maduro e um com sinal cego**, e `ADR-0033` e
`M1` — **o sucessor tambem sera `M1`, e errar nele custa outro sucessor**.

**DEP-QAR NAO abre o sucessor**, porque abrir missao nao e materia de parecer (`FT-10`).

**DEP-QAR NAO recomenda liberar `GO-TO-SKILLS`:** liberar portao e **ato de autoridade**
(`FND-01 §6.2`). **Exercer duas vezes continua nao sendo liberar.**
