---
id: INC-2026-002-ratificacao-declarada-em-fitness-check
titulo: FIT-2026-001 declara ratificacao do Soberano que nao ocorreu, e FIT-2026-002 declara nao-exigida uma ratificacao que a norma exige
tipo: relatorio
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: null
decisoes_relacionadas: [ADR-0004, ADR-0006]
substitui: []
substituido_por: null
norma_violada: [LV-05, GV-05, CV-09]
severidade: media
efeito: Duas verificacoes de aptidao sobre mudancas C3 registram estado de ratificacao incorreto — uma afirmando ato inexistente, outra negando exigencia vigente
causa: Mesma raiz de INC-2026-001, agravada por divergencia entre FND-10 §2.2 e §10.3 sobre se `FIT` exige ratificacao
situacao: fechado
resumo: Registra e contem o estado incorreto de ratificacao declarado em FIT-2026-001 e FIT-2026-002, sem editar artefato imutavel; fechado pelo ato soberano de 2026-07-28.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-EXE
ratificacao: nao-exigida
---

# INC-2026-002: Ratificacao declarada em Fitness Check

## Proposito
Registrar que duas verificacoes de aptidao sobre mudancas C3 declaram estado de ratificacao
que nao corresponde ao fato — e conter o efeito sem editar registro imutavel.

## Escopo
| Item | Definicao |
|---|---|
| Inclui | [FIT-2026-001](../fitness/FIT-2026-001-meta-model.md) e [FIT-2026-002](../fitness/FIT-2026-002-artifact-framework.md) |
| Nao inclui | O **merito** de qualquer dos dois vereditos, que permanece integro; ADR-0001 a ADR-0006, ja regularizados por [INC-2026-001 §11](INC-2026-001-ratificacao-inferida.md) |
| Instrumento | Incidente de conformidade, FND-04 §10 |

## Responsaveis
| Papel | Quem |
|---|---|
| Detectado por | **DEP-GOV**, na auditoria de consistencia normativa da Missao 1.4 |
| Registra | DEP-GOV |
| Verifica o fechamento | **DEP-EXE** — nao DEP-QAR, que **produziu** os dois artefatos afetados (PI-05, ADR-0005) |
| Unico que pode encerrar a pendencia | **SOBERANO** |

---

## 1. Fato

| Artefato | O que declara | Fato |
|---|---|---|
| FIT-2026-001 §Veredito | *"Ratificado por (C3): **SOBERANO**"* | **Nenhum ato de ratificacao sobre esta verificacao ocorreu.** O ato soberano de 2026-07-28 nomeia ADR-0001 a ADR-0004 e ADR-0006 — nenhum `FIT` |
| FIT-2026-002 frontmatter | `ratificacao: nao-exigida` | FND-10 §10.3 exige ratificacao do Soberano para `FIT` cujo objeto seja **C3**, e o objeto declarado e C3. O proprio corpo de FIT-2026-002 contradiz o frontmatter, registrando *"Ratificado por (C3): **Pendente**"* |

## 2. Norma violada

| Norma | Como foi contrariada |
|---|---|
| **LV-05** | FIT-2026-001 afirma como ocorrido um ato que nao ocorreu. A linha vermelha nao admite excecao (FND-01 §8.3) |
| **GV-05** | Aprovacao — e ratificacao — e ato explicito e datado. Nenhum foi registrado |
| **CV-09** | Quem registra a ratificacao e papel diverso do executor. Em FIT-2026-001, o proprio DEP-QAR preencheu o campo do artefato que produziu |

> **Severidade `media`, nao `alta`.** Diferente de INC-2026-001, aqui **nao ha corpo normativo
> em risco**: `FIT` e parecer, nao norma. Nenhuma regra vigora por causa de um Fitness Check,
> e os dois vereditos permanecem validos como avaliacao independente. O que esta incorreto e
> o registro do estado de ratificacao, nao o julgamento.

## 3. Efeito atual

| Artefato | Veredito | Eficacia do veredito | Registro de ratificacao |
|---|---|---|---|
| FIT-2026-001 | `apto-com-ressalva` | **Integra** — executada por papel independente do produtor do objeto | **Incorreto** — afirma ato inexistente |
| FIT-2026-002 | `apto-com-ressalva` | **Integra** | **Incorreto** — declara `nao-exigida` onde §10.3 exige |
| FIT-2026-003 | *(desta missao)* | — | **Correto** — objeto e C2, ratificacao `nao-exigida` de fato |

**Nenhuma decisao foi tomada com base no campo incorreto**, e nenhum componente existe. O
efeito esta contido ao registro.

## 4. Contencao aplicada

| # | Medida | Onde |
|---|---|---|
| C1 | Registro deste incidente, com a fonte corrente do estado real de ratificacao dos dois `FIT` | Este documento, §7 |
| C2 | **Nenhum dos dois arquivos e editado** — `FIT` e classe **M1** (FND-10 §6.2), e PJ-04 determina que campo de estado em M1 registra o estado *no ato* | — |
| C3 | O indice de aptidao passa a projetar o estado real | [`governance/fitness/README.md`](../fitness/README.md) |
| C4 | A divergencia normativa que concorreu para o defeito e registrada como achado, **sem ser corrigida por hipotese** (§6) | [REV-CONSOLIDACAO](../../foundation/revisao-arquitetural-consolidacao-2026-07-28.md) |

## 5. Causa

**Causa raiz: a mesma de [INC-2026-001](INC-2026-001-ratificacao-inferida.md)** — o executor
preencheu a propria secao de ratificacao (F3) —, com um agravante proprio:

| # | Fator | Natureza |
|---|---|---|
| G1 | FND-10 **§2.2** exige o campo `ratificacao` em *"artefato de decisao C3 ou Tipo 1"*; `FIT` **nao e artefato de decisao** | Ambiguidade de **norma** |
| G2 | FND-10 **§10.3** exige, na mesma pagina, ratificacao do Soberano para `FIT` de objeto C3 | Ambiguidade de **norma** |
| G3 | Diante da divergencia, cada verificacao resolveu de um jeito — uma afirmou o ato, outra negou a exigencia | Efeito de G1 e G2 |

> As correcoes de causa de INC-2026-001 — **LM-02 a LM-06**, a auditoria de eficacia de
> ratificacao (FND-04 §8) e **CV-09** — ja alcancam este caso: e a auditoria criada la que
> encontrou este defeito aqui. O que **nao** estava coberto e a ambiguidade G1/G2.

## 6. Correcao

### 6.1 Correcao do efeito
Contencao de §4. O efeito so e integralmente corrigido pelo ato do Soberano (§7).

### 6.2 Correcao da causa

| Causa | Correcao | Estado |
|---|---|---|
| F3 (herdada) | CV-09 separa obter de registrar; LM-05 exige papel distinto | **Feito** em INC-2026-001 |
| G1/G2 ambiguidade | **Nao corrigida nesta missao, deliberadamente.** Resolver exigiria decidir se `FIT` exige ratificacao — pergunta de merito normativo com duas respostas defensaveis. Promover uma delas a norma sem RFC seria **promover hipotese a norma** | **Registrada como achado com dono e gatilho** |

| Campo | Conteudo |
|---|---|
| Achado | Divergencia FND-10 §2.2 × §10.3 quanto a exigencia de ratificacao de `FIT` |
| **Dono** | DEP-GOV |
| **Gatilho** | Ato do Soberano sobre §7, **ou** a proxima verificacao de aptidao sobre objeto C3 — o que ocorrer primeiro |
| **Custo assumido** | Enquanto a ambiguidade existir, cada `FIT` de objeto C3 pode resolve-la de novo, de maneira propria. O custo e reincidencia, e esta declarado |

## 7. Pendencia para o Soberano

| # | Decisao pendente | Opcoes |
|---|---|---|
| P1 | **Ratificar, dispensar ou declarar nao exigida** a ratificacao de FIT-2026-001 e FIT-2026-002 | (a) ratificar os dois em ato unico e datado; (b) declarar que `FIT` **nao** exige ratificacao — o que resolve tambem G1/G2 e vira emenda a FND-10 §10.3 pelo rito; (c) manter pendente |

> **Recomendacao de DEP-GOV:** opcao **(b)**. Um parecer de aptidao existe para ser
> **independente**; exigir que a autoridade maxima o ratifique aproxima o ratificador do
> verificador e enfraquece justamente o que o instrumento protege (PI-05, FT-02). A
> recomendacao e registrada como recomendacao — **nao** executada.

## 8. Aprendizado

| Registro | Conteudo |
|---|---|
| [MEM-APR-0003](../../memory/aprendizado/MEM-APR-0003-campo-de-estado-em-artefato-imutavel.md) | Campo de estado em artefato M1 so registra o estado **no ato**. Vale integralmente aqui: por isso nenhum dos dois `FIT` e editado |

> Nao se cria registro APR proprio: a licao ja existe e cobre este caso. Duplicar aprendizado
> e o mesmo defeito de duplicar norma (MM-01, PJ-01).

## 9. Fechamento

| Campo | Conteudo |
|---|---|
| Situacao | **`contido`** — efeito isolado; causa herdada ja corrigida; causa propria (G1/G2) registrada com dono e gatilho |
| O que falta para `corrigido` | Ato do Soberano sobre P1 |
| O que falta para `fechado` | Verificacao de **DEP-EXE** de que causa e efeito foram tratados |
| Quem fecha | DEP-EXE — **nao DEP-QAR**, que produziu os artefatos afetados |
| Prazo | Sem prazo fixado. **Nao expira** |

## 10. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Origem | Auditoria de consistencia normativa da Missao 1.4, executada sob a auditoria de **eficacia de ratificacao** criada por INC-2026-001 (FND-04 §8) |
| Artefatos afetados | FIT-2026-001, FIT-2026-002 |
| Artefatos alterados | `governance/fitness/README.md`; `governance/incidents/README.md`; catalogo mestre |
| Artefatos **nao** alterados | FIT-2026-001 e FIT-2026-002 — classe M1 (LV-04, CC-01, PJ-04) |
| Incidente relacionado | [INC-2026-001](INC-2026-001-ratificacao-inferida.md) — mesma causa raiz, escopo distinto |

---

## 11. Encerramento pelo ato soberano de 2026-07-28

> **Secao acrescentada ao encerrar o incidente.** Um incidente so e **M1 depois de fechado**
> (FND-10 §6.2); acrescentar a secao de fechamento e o ato que o torna imutavel, nao uma
> edicao de artefato imutavel. Mesma forma de [INC-2026-001 §11](INC-2026-001-ratificacao-inferida.md).

### 11.1 O ato

O Soberano decidiu **P1** de §7 em ato explicito e datado de **2026-07-28**:

> *"Acolho expressamente FIT-2026-001 e FIT-2026-002 como pareceres, sem eleva-los a norma, e
> autorizo o encerramento de INC-2026-002 apos comprovacao independente de que todas as
> condicoes pendentes foram corretamente registradas."*

**Fonte canonica unica do ato:**
[**MSG-2026-0002**](../../memory/operacional/MSG-2026-0002-ato-soberano-cartas-comando-plataforma-e-contexto.md).
Esta secao **referencia**; nao reproduz o registro (CM-09, PJ-01).

### 11.2 O que o ato decidiu — e o que ele **nao** decidiu

| # | Questao | Resultado |
|---|---|---|
| 1 | A pendencia **P1** foi decidida? | **SIM.** O Soberano escolheu **acolher como parecer, sem elevar a norma** — em substancia, a opcao **(b)** de §7, recomendada por DEP-GOV |
| 2 | Os dois `FIT` foram **ratificados**? | **NAO.** *Acolher* nao e *ratificar*. O estado de ratificacao correto passa a ser **`nao-exigida` por ato**, e nao por inferencia |
| 3 | A frase *"Ratificado por (C3): SOBERANO"* de FIT-2026-001 ficou **verdadeira**? | **NAO.** Ela era falsa quando escrita e **continua nao corrigida**: `FIT` e **M1** (LV-04, PJ-04, MEM-APR-0003). O efeito segue **contido**, nao sanado |
| 4 | A causa **G1/G2** — divergencia FND-10 §2.2 × §10.3 — foi resolvida? | **NAO.** O ato decidiu **dois casos concretos** e disse expressamente *"sem eleva-los a norma"*. Ler nele uma emenda geral seria **LM-03** |

### 11.3 Comprovacao independente exigida pelo ato

O ato condiciona o encerramento a comprovar que as condicoes pendentes estao **corretamente
registradas** — registradas, nao resolvidas.

| Condicao pendente | Onde passa a viver | Dono | Correta? |
|---|---|---|---|
| **P1** — decisao sobre os dois `FIT` | **Decidida.** Estado corrente projetado em [`governance/fitness/README.md`](../fitness/README.md); fonte canonica **MSG-2026-0002 §4** | DEP-GOV | **Sim** |
| **G1/G2** — ambiguidade normativa *(causa propria, nao corrigida)* | **Migrada** para [RFC-0009 §9, Q2](../../rfcs/RFC-0009-integridade-e-alcance-do-ato-de-ratificacao.md) — **aberta**, com opcoes, criterios e escalada ao Soberano | **DEP-GOV** | **Sim** |
| **Registro incorreto em FIT-2026-001** *(nao corrigivel — M1)* | **Contido permanentemente:** projecao em `governance/fitness/README.md` e MSG-2026-0002 §4 | DEP-GOV | **Sim** |
| **Aprendizado** | [MEM-APR-0003](../../memory/aprendizado/MEM-APR-0003-campo-de-estado-em-artefato-imutavel.md), ja existente e aplicado nesta missao | DEP-KMS | **Sim** |

**Verificado por:** **DEP-EXE**, conforme §9 determina — **nao** DEP-QAR, que produziu os dois
artefatos afetados. **DEP-EXE nao produziu** `FIT-2026-001` nem `FIT-2026-002`.

### 11.4 Por que o incidente pode fechar sem que a causa esteja corrigida

| Campo | Conteudo |
|---|---|
| Regra | FND-04 §10: o incidente fecha quando **efeito** e **causa** estao **tratados** — nao necessariamente **eliminados** |
| **Efeito** | **Corrigido.** O estado de ratificacao dos dois `FIT` esta decidido por ato do Soberano e projetado na fonte corrente |
| **Causa herdada** (F3) | **Corrigida** em INC-2026-001: LM-02 a LM-06, CV-09 e a auditoria de eficacia de ratificacao |
| **Causa propria** (G1/G2) | **Tratada, nao eliminada.** Migrada para instrumento **vivo** — uma RFC aberta com dono, opcoes e escalada —, em vez de permanecer como nota dentro de um incidente que ninguem reabre |
| **Por que isso nao e fechar divida por renomeacao** | Um incidente `fechado` e **M1**: nao recebe atualizacao. Manter G1/G2 dentro dele **congelaria** a divida num documento imutavel. Move-la para uma RFC aberta **aumenta** a chance de resolucao, e o fechamento fica condicionado a essa migracao ter ocorrido — o que §11.3 comprova |
| O que **ainda falta**, e nao esta escondido | **Q2 de RFC-0009** permanece **aberta** e depende de ato do Soberano. **Nenhuma linha desta missao afirma que a ambiguidade foi resolvida** |

### 11.5 Estado final

| Campo | Conteudo |
|---|---|
| Situacao | **`fechado`** |
| Data | 2026-07-28 |
| Fundamento | Ato soberano de 2026-07-28 (MSG-2026-0002) + comprovacao independente de §11.3 |
| Fecha | **DEP-EXE** |
| Verificacao independente da comprovacao | **DEP-QAR** e **DEP-GOV** — [REV-ESTRUTURAL-I §1](../../foundation/revisao-estrutural-01-2026-07-28.md) |
| Artefatos **nao** alterados | `FIT-2026-001` e `FIT-2026-002` — classe **M1** (LV-04, CC-01, PJ-04). **Zero edicoes** |
| Divida remanescente, declarada | **Q2 de RFC-0009** — *"`FIT` exige ratificacao do Soberano?"* |

> **Incidente fechado sem correcao de causa nao esta fechado** (FND-04 §10). Este fecha com a
> causa herdada **corrigida** e a causa propria **migrada para instrumento vivo** — nao
> eliminada, e declarada como tal. **Versao permanece 1.0.0:** acrescentar a secao de
> fechamento e o ato que completa o ciclo do incidente, nao emenda de conteudo (ADR-0009,
> AC-08). Mesma forma de INC-2026-001.
