---
id: RFC-0029-primeira-skill-copia-datada
titulo: Qual capacidade vira a primeira Skill do acervo, e por que as outras duas nao agora
tipo: rfc
versao: 1.0.0
status: aprovado
camada_memoria: nao-aplicavel
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-08-03
atualizado_em: 2026-08-03
revisao_prevista: null
decisoes_relacionadas: [ADR-0033, ADR-0034]
substitui: []
substituido_por: null
classe_mudanca: C2
prazo_analise: 2026-08-03
---

# RFC-0029: A primeira `Skill`

## Proposito

Escolher, **por medicao**, qual de tres capacidades construidas fora do acervo vira a **primeira
`Skill`** — e declarar por que as outras duas **nao agora**.

## Escopo

| Item | Definicao |
|---|---|
| **Inclui** | A escolha entre `backup-datado`, `secret-scan` e `kernel-de-evidencia`; o enquadramento da escolhida sob `SK-01` a `SK-26`; o local canonico `skills/` |
| **NAO** inclui | **Mover codigo para o acervo** — o canonico recebe a **ficha**, nunca a implementacao · emendar `TPL-skill` ou sanar `RD-122` · promover `ADR-0033` a `FND` · liberar portao |

## 1. Criterio, e ele foi fixado antes de olhar as tres

**`SK-20` e `PI-14`: o ganho declara-se com o SINAL QUE O MOTIVOU, e sinal antecipado nao
serve** (`FND-08 §7.1`). O despacho fixou o desempate: **capacidade com uso real registrado
vence capacidade so testada.**

## 2. As tres, medidas contra o acervo

| Capacidade | Teste declarado | Sinal no acervo *(medido)* | Uso real registrado | Achado aberto que enderecaria |
|---|---|---|---|---|
| **`backup-datado`** | **5/5** cenarios | ***"copia datada"* em `67` artefatos** | **`22` tokens do lease declaram `copia_datada`** | ⚠️ **`RD-103`, severidade ALTA** |
| `secret-scan` | 19/19 | *"credencial em texto"* em `22` artefatos | sim — toda missao declara `0` credenciais | **nenhum aberto** — materia ja coberta por `PI-08`/`LV-02` |
| `kernel-de-evidencia` | 17/17, `0` FP, `0` FN | `LV-12` em `56` artefatos | **nao** — testada, sem uso real registrado | — |

## 3. Recomendacao — **`backup-datado`**

**Vence nos tres eixos que o criterio mede**, e nao por pouco:

1. **Maior sinal observado** — `67` artefatos contra `22` e `56`.
2. **Uso real registrado no instrumento de governanca** — `22` tokens do lease.
3. **E a unica das tres que enderecça um achado ABERTO de severidade ALTA:** **`RD-103`**, em
   que um script de faxina apagou, com `rd /s /q` e **sem lixeira**, o **ponto de retorno
   declarado de um ato `C3` pendente**, deixando **`7`** arquivos sem bytes pre-escrita
   recuperaveis. **Nao houve como desfazer.**

**O ponto decisivo:** as outras duas resolvem problemas que a norma **ja cobre**; esta resolve
um que o acervo **ja sofreu, ja mediu e ja registrou como Alta**.

## 4. Por que as outras duas nao agora

| Capacidade | Por que nao agora |
|---|---|
| **`secret-scan`** | **Nao e recusa de merito — e ordem.** Tem sinal real *(`22`)* e uso real, mas sua materia ja tem norma vigente *(`PI-08`, `LV-02`)* e **nenhum achado aberto** a pressionando. **Fica como candidata natural a segunda `Skill`** |
| **`kernel-de-evidencia`** | **Duas razoes, e a segunda e a que pesa.** *(a)* E **testada e nao usada** — perde pelo criterio declarado. *(b)* Sua materia — classificar `alegado`/`observado`/`medido` — **coincide com `EA-01` a `EA-05` do candidato de 1.18**, que **NAO foi admitido**. Criar `Skill` sobre materia de framework nao admitido seria **antecipar decisao do Fundador** |

## 5. Enquadramento sob `SK-01` a `SK-26` — testado antes de propor

| Regra | Verificacao |
|---|---|
| **`SK-01`** | Repete-se *(`22` usos)* · resultado **verificavel** *(`n/n` por `sha256`)* · usavel por **mais de um papel** *(DEP-GOV, DEP-KMS, DEP-OPS)*. **Tres de tres** |
| **`SK-02`** | Pertence a organizacao: **nenhum agente e dono**, e nenhum existe |
| **`SK-03`** | ⚠️ **O nome externo REPROVA.** `backup-datado` e substantivo + adjetivo; a regra exige **acao** `<dominio>-<verbo>-<objeto>`. **Renomeado para `custodia-criar-copia-datada`** |
| **`SK-04`** | Executada por **um papel de cada vez**, **sem portao** → e `SKL`, nao `WFL` |
| **`SK-06`** | Exige `capabilities` e `gatilho`, que **`TPL-skill` omite** — escritos a mao, **sem criar campo novo** (`AC-07`) |
| **`SK-13`** | **NAO idempotente**, e a nao-idempotencia e **deliberada**: repetir com o mesmo carimbo **recusa**, protegendo o ponto de retorno anterior |

## 6. Impacto

| O que muda | Medida |
|---|---|
| Artefatos criados | **5** — `RFC-0029`, `ADR-0034`, a `Skill`, `FIT-2026-027`, `PT-2026-021` |
| Diretorio | **`skills/` passa a existir** — ja declarado em `FND-03 §7` como *"(fase futura)"* |
| Bytes de **codigo** no acervo | **`0`** — a implementacao **nao se move** |
| `GO-TO-SKILLS` | **EXERCIDO** — a primeira `Skill` existe. **Exercer nao e liberar** |

## 7. Riscos

| # | Risco | Mitigacao |
|---|---|---|
| `R1` | A ficha descreve capacidade cujo **codigo vive fora** e pode divergir | Declarado em §10 da ficha; `SK-23` proibe copiar a norma, e o mesmo vale para o codigo |
| `R2` | `TPL-skill` nao produz ficha conforme | **Exercido e declarado**: dois campos a mao. `RD-122` **aberto** |
| `R3` | Ler *"primeira Skill"* como liberacao de `GO-TO-SKILLS` | `ADR-0034` declara: **exercer o portao nao e libera-lo** |
