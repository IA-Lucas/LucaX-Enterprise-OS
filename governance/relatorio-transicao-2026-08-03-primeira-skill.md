---
id: PT-2026-021
titulo: Missao 1.13.11 — a PRIMEIRA Skill do acervo, e a avaliacao das 26 regras no primeiro uso real
tipo: reporte
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-08-03
atualizado_em: 2026-08-03
revisao_prevista: null
decisoes_relacionadas: [ADR-0033, ADR-0034]
substitui: []
substituido_por: null
resumo: Cria a primeira Skill do acervo e mede as 26 regras de ADR-0033 no primeiro uso real — 19 exercidas sem ressalva, 4 nao aplicadas, 2 insuficientes e 1 defeituosa.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
---

# PT-2026-021 — A primeira `Skill`

**Decisao: `CRIADA`.**

## 1. Item 0 — a escolha, medida

**Escolhida: `backup-datado`.** Fundamento em [`RFC-0029 §2`](RFC-0029-primeira-skill-copia-datada.md),
e os numeros sao do acervo, nao do despacho:

| Capacidade | Sinal no acervo | Uso real registrado | Achado ABERTO que enderecça |
|---|---|---|---|
| **`backup-datado`** | ***"copia datada"* em `67` artefatos** | **`22` tokens do lease** | ⚠️ **`RD-103` — ALTA** |
| `secret-scan` | `22` artefatos | sim | **nenhum** |
| `kernel-de-evidencia` | `56` artefatos *(`LV-12`)* | **nao — so testada** | — |

**Venceu nos tres eixos**, e o decisivo e o terceiro: **e a unica das tres que enderecça um
achado aberto de severidade Alta.** As outras duas resolvem o que a norma **ja cobre**; esta
resolve o que o acervo **ja sofreu, mediu e registrou**.

**Por que as outras nao agora.** `secret-scan` **nao foi recusada por merito** — e ordem, e ela
e a candidata natural a segunda. `kernel-de-evidencia` perde pelo criterio *(testada, nao
usada)* **e** porque sua materia coincide com `EA-01`–`EA-05` do candidato de **1.18, que nao
foi admitido**: cria-la seria antecipar decisao do Fundador.

## 2. O que foi criado

**[`SKL-custodia-criar-copia-datada`](../skills/SKL-custodia-criar-copia-datada.md)** — a
primeira `Skill` do acervo. **`skills/` passa a existir.**

**O nome mudou por norma.** `backup-datado` e **substantivo + adjetivo**; `SK-03` exige **acao**,
`<dominio>-<verbo>-<objeto>`. **A regra reprovou o nome externo e o corrigiu** — e este e o
primeiro caso registrado de uma regra do Framework alterando o objeto que recebia.

**`0` bytes de codigo entraram no acervo.** A implementacao permanece em
`_arquivo/projetos-parados/.../\_fabrica/skills/backup-datado/`. **O canonico recebeu a ficha.**

**Dois campos escritos a mao:** `capabilities` e `gatilho` — **exigidos por `FND-09 §E-13` e por
`SK-06`**, e **ausentes de `TPL-skill`** *(`0` ocorrencias de cada, controle positivo
`proprietario` = 1)*. **Nao cria campo novo** (`AC-07`). **`RD-122` foi EXERCIDO, nao sanado.**

## 3. O custo, e uma correcao de leitura que ele obriga

**`5` artefatos** — `RFC-0029`, `ADR-0034`, a `Skill`, `FIT-2026-027` e este `PT`. **Exatamente
o custo de `SPC-001`**, a primeira `Spec`.

> **Dizer que `Skill` e *"o componente mais barato do acervo"* e verdadeiro quanto a
> RATIFICACAO e falso quanto a INSTRUMENTOS.** `FND-09 §8.2` linha `SKL` poe **`—`** em
> *Ratifica*: **`0` atos**, e isso e real. Mas `FND-04 §6` classifica a criacao como **`C2`**, e
> `FND-04 §6` diz *"**alem** do rito da classe"* — de modo que `FND-04 §2.1` impoe
> **`RFC` → `ADR`**. **O barato e o ato, nao o rito.** Registrado como insuficiencia de `SK-10`
> em §4.

## 4. ⭐ A AVALIACAO DAS 26 REGRAS NO PRIMEIRO USO REAL

> **Este e o entregavel que so a primeira `Skill` produz.** Mesma medicao que `SPC-001` fez
> sobre as **32** regras do Framework de Specifications, e que rendeu **4 insuficientes e 1
> defeituosa**.

| # | Regra | Veredito | O que se observou |
|---|---|---|---|
| `SK-01` | reutilizavel, 3 condicoes | ✅ **exercida** | As tres cumpriram: repete *(`22` usos)*, verificavel *(`n/n` por `sha256`)*, mais de um papel *(3 nomeados)* |
| `SK-02` | pertence a organizacao | ✅ **exercida** | Nenhum agente e dono — e **`0` agentes existem**, de modo que o caso discriminante nao apareceu |
| `SK-03` | nome e acao | ✅ **exercida — e REPROVOU** | `backup-datado` **falhou** e foi renomeado. **A regra funcionou contra o objeto, e e o sinal mais forte do conjunto** |
| `SK-04` | `SKL` × `WFL` | ✅ **exercida** | Um papel de cada vez, sem portao → `SKL` |
| `SK-05` | nao e Prompt/Playbook | ➖ **nao se aplicou** | Nenhuma confusao surgiu |
| `SK-06` | contrato + atributos minimos | ✅ **exercida — e revelou defeito de TEMPLATE** | Exigiu `capabilities` e `gatilho`; `TPL-skill` **nao os tem**. **A regra estava certa; o template esta defasado** — `RD-122` |
| `SK-07` | Capability 1..3 | ✅ **exercida** | `CAP-governanca`, `ativo`. **1 de 3** |
| `SK-08` | *"Quando NAO usar"* | ✅ **exercida** | Produziu **5** exclusoes reais, entre elas *"nao substitui backup externo"* |
| `SK-09` | **12 blocos** | ⚠️ **DEFEITUOSA** | **Conflaciona categorias.** Diz *"os ONZE do template **mais o gatilho**: doze"* — mas os 11 sao **blocos de CORPO** e `gatilho` e **atributo de FRONTMATTER** (`FND-09 §E-13`, `SK-06`). **Somar os dois numa contagem unica e erro de categoria**, e obrigou a ficha a materializar o gatilho **duas vezes** — campo e secao — para satisfazer as duas leituras |
| `SK-10` | autoridade derivada | ⚠️ **INSUFICIENTE** | Remete corretamente a classe, **mas nao adverte que `C2` arrasta `RFC` → `ADR`**. Quem ler *"`Skill` nunca ratifica"* conclui *"barata"*, e a primeira custou **5** artefatos — os mesmos da primeira `Spec`. **Falta a advertencia; a remissao esta certa** |
| `SK-11` | gatilho, 3 campos | ✅ **exercida** | Os tres preenchidos, com papel e nao pessoa |
| `SK-12` | gatilho nao cria superficie | ➖ **nao exercida** | Nenhuma tentativa de dar ciclo de vida proprio ao gatilho. **Continua determinada** |
| `SK-13` | idempotencia | ✅ **exercida** | Declarada **NAO idempotente**, e a nao-idempotencia e **deliberada e protetiva**: repetir recusa, preservando o ponto de retorno |
| `SK-14` | executavel sem o autor | ✅ **exercida** | 6 passos, cada um com saida |
| `SK-15` | passo produz | ✅ **exercida** | **`0`** passos sem saida declarada |
| `SK-16` | nao decide | ✅ **exercida** | A Skill **nao apaga**: apagar e decisao de quem invoca, depois da copia verde |
| `SK-17` | entradas e saidas | ✅ **exercida** | 5 entradas com origem e obrigatoriedade; 4 saidas com destinatario |
| `SK-18` | criterio por `SF-14` | ✅ **exercida** | `MEDICAO` — *"`n` de `n` conferem, saida `0`"* |
| `SK-19` | falha **plausivel e errada** | ✅ **exercida — e foi o bloco mais util** | Nomeou a falha grave: **dizer `VERIFICADO` com arquivo divergente**. Sem a regra, a ficha teria listado so as 3 falhas obvias |
| `SK-20` | 4 perguntas + sinal observado | ✅ **exercida** | Sinal = **`RD-103`, Alta**, mais `67` artefatos e `22` tokens. **Nada antecipado** |
| `SK-21` | nao depende de agente | ➖ **nao se aplicou** | **`0` agentes existem** |
| `SK-22` | duplicata | ➖ **nao se aplicou** | **`1`** `Skill` no acervo; nada a duplicar. O catalogo **foi consultado antes**, como a regra manda |
| `SK-23` | normas por identificador | ✅ **exercida** | **6** normas citadas, **`0`** reproduzidas |
| `SK-24` | custo medido, blocos independentes | ⚠️ **INSUFICIENTE** | O custo foi medido, **mas o teste que a regra define e incalculavel**: *"o dobro da mediana do seu tipo"* exige **mediana**, e com **`1`** instancia nao ha mediana. **A regra so passa a decidir a partir da terceira `Skill`** |
| `SK-25` | `M2`, versao pelo efeito, descontinuacao | ✅ **exercida** | Criterio de descontinuacao com **3** condicoes, sinal observavel e substituto — inclusive *"a organizacao deixa de ter esta capacidade"* |
| `SK-26` | template, registro, contador | ✅ **exercida** | Contador incrementado **na mesma mudanca** (`CV-04`, `IX-02`) |

### Contagem — e ela fecha

| Veredito | Quantas | Quais |
|---|---:|---|
| ✅ **Exercidas sem ressalva** | **19** | `SK-01`–`SK-04`, `SK-06`–`SK-08`, `SK-11`, `SK-13`–`SK-20`, `SK-23`, `SK-25`, `SK-26` |
| ➖ **Nao se aplicaram / nao exercidas** | **4** | `SK-05`, `SK-12`, `SK-21`, `SK-22` |
| ⚠️ **Insuficientes** | **2** | **`SK-10`**, **`SK-24`** |
| ❌ **Defeituosa** | **1** | **`SK-09`** |
| | **26** | |

**Comparacao com o precedente, medida:** `SPC-001` avaliou **32** regras e achou **4
insuficientes e 1 defeituosa** — **5 de 32 = 15,6%**. Aqui: **3 de 26 = 11,5%**. **O Framework
de Skills chegou ao primeiro uso com menos defeito por regra que o de Specifications** — e a
razao provavel esta declarada em `ADR-0033`: **23 das 26 sao recepcao**, e regra recebida ja
passou por uso alheio.

**Nenhum dos tres se corrige aqui.** `ADR-0033` e **`M1`**: corrigir `SK-09`, `SK-10` ou `SK-24`
exige **`ADR` sucessor** — e e o custo que `ADR-0033` declarou ao escolher a sede.

## 5. Reconciliacao

| O que | Estado |
|---|---|
| Catalogo mestre — §2, §4, contadores, §10 | ✅ **mesma mudanca** (`CV-04`, `IX-02`) |
| Indices `M3` — `rfcs`, `decisions`, `fitness` | ✅ mesma mudanca |
| Baseline | ✅ **`BL-2026-08-03-03`**, `IR-BL/4`, **2** execucoes |

## 6. O que esta missao NAO fez

- **Nao LIBEROU `GO-TO-SKILLS`** — **exercer nao e liberar**. Liberar e ato de autoridade (`FND-01 §6.2`).
- **Nao moveu codigo** — `0` bytes de implementacao no acervo.
- **Nao emendou `TPL-skill`** nem sanou `RD-122`, que foi **exercido**.
- **Nao promoveu `ADR-0033` a `FND`** — **o sinal agora existe**, e a decisao continua sendo de quem detem a materia.
- **Nao admitiu os outros candidatos · nao emendou Fundacional · nao decidiu `RD-116` · `0` atos.**
- **Nao fechou `RD-103`** — o dano e irreversivel; a `Skill` reduz repeticao, nao desfaz.

## 7. Achados

**`0` novos inscritos.** **`3` observacoes sobre o proprio Framework** — `SK-09` defeituosa,
`SK-10` e `SK-24` insuficientes —, **registradas aqui e nao no catalogo**, porque sao **materia
de `ADR` sucessor** e nao defeito de artefato. **`RD-122` exercido e confirmado.**

## 8. Decisao

**`CRIADA`.** A primeira `Skill` do acervo existe desde 2026-08-03. **`GO-TO-SKILLS` passa de
EXERCIVEL a EXERCIDO.** As **26** regras saem de *determinadas* para **observadas**.
