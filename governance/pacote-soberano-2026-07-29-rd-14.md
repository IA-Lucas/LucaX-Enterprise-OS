---
id: PS-2026-007
titulo: Pacote de decisao soberana — emenda C3 a FND-01 §6.2 que fecha RD-14
tipo: relatorio
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-07-29
atualizado_em: 2026-07-29
revisao_prevista: null
decisoes_relacionadas: [ADR-0012, ADR-0014, ADR-0018]
substitui: []
substituido_por: null
canal: REPORTE
emissor: DEP-GOV
destinatario: SOBERANO
ttl: ate decisao do Soberano
resumo: Submete ao Soberano a emenda C3 que passa o liberador do portao QG-1 de DEP-PRD para DEP-EXE e acrescenta nota que distingue liberar portao de aprovar artefato, com diff literal, hashes integrais e verificacao de que nenhum titular e criado.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# PS-2026-007 — Emenda **C3** a FND-01 §6.2

> ## Este pacote **informa**. Nao decide, nao aprova, nao promulga e nao edita nada.
>
> **FND-01 permanece em 1.4.0.** O candidato **1.5.0** existe como **diff literal + hash**,
> **fora do acervo**.
>
> **Pacote separado de [PS-2026-008](pacote-soberano-2026-07-29-rd-15.md), por determinacao.**
> **RD-14** e **RD-15** sao materias distintas e **nao se misturam num ato**.
>
> **Caminho exato:** `governance/pacote-soberano-2026-07-29-rd-14.md` *(RE-01)*.

## Proposito
Levar ao Soberano a emenda que fecha **RD-14**: **FND-01 §6.2 contradiz a si propria** —
a tabela nomeia `DEP-PRD` como liberador de `QG-1`, e a **regra de portao**, sete linhas
abaixo, proibe que o portao seja liberado por quem produziu o artefato.

## Escopo
| Item | Definicao |
|---|---|
| Inclui | **Um** objeto: `ADR-0018` e a promulgacao de **FND-01 1.5.0** |
| **Nao** inclui | **RD-15** — [PS-2026-008](pacote-soberano-2026-07-29-rd-15.md) · **RD-02** — [PS-2026-004](pacote-soberano-2026-07-29-rd-02.md) · **RD-09** — [PS-2026-005](pacote-soberano-2026-07-29-rd-09.md) · `DEP-KMS`/`DEP-ENG` — [PS-2026-006](pacote-soberano-2026-07-29-kms-eng.md) · **FND-02 §2 e §7**, **FND-09 §8.2**, **FND-10 §10.3** e as **nove Cartas**, cascata **declarada e nao emendada** · `ADR-0014` e qualquer artefato historico *(M1, LV-04)* |
| Natureza | **Reporte**, entidade `MSG`. **Nenhum** tipo, entidade, camada, template ou diretorio novo |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| **Autor da emenda** | **DEP-GOV** | FND-09 §8.2, linha `FND` |
| **Revisor independente** | **DEP-QAR** | RM-06b |
| **DECIDE** | **SOBERANO** | **C3. Indelegavel.** **Nao ocorreu** |

> **Residuo declarado (PI-10).** **DEP-EXE e DEP-PRD sao as duas areas alcancadas** — uma
> recebe a liberacao de `QG-1`, a outra a perde — e **nenhuma das duas participou da autoria
> ou da revisao**. `DEP-PRD §10.1, RP-1` ja declarava o arranjo atual como risco de impacto
> **Alto**, com mitigacao *"assimetrica e declarada como tal"*. Residuo **de posicao, nao de
> interesse** — declarado, nao suprido.

---

## 1. O que se pede

| # | Objeto | Ato pedido | Se **nao** houver ato |
|---|---|---|---|
| **1** | **`ADR-0018`** + promulgacao de **`FND-01` 1.5.0** | **Aprovacao e ratificacao** | FND-01 permanece em **1.4.0**. `QG-1` segue **liberado por quem produz a Spec**, contra a regra da propria §6.2 e contra **PI-05** e **LV-03**, **sem excecao formal**. **Nenhuma Spec pode ser aberta** |

> **Nao ha aprovacao parcial util.** A celula sem a nota deixaria `QG-1` com liberador novo e
> **sem a distincao que impede a leitura de que DEP-EXE passou a decidir escopo** — o risco
> `RR-2` de RFC-0014. A nota sem a celula **descreveria** a colisao em vez de resolve-la.

## 2. Diff literal — `FND-01` 1.4.0 → **1.5.0**

| # | Local | Antes | Depois |
|---|---|---|---|
| **C1** | frontmatter | `versao: 1.4.0` | `versao: 1.5.0` |
| **C2** | frontmatter | `decisoes_relacionadas: [ADR-0001, ADR-0002, ADR-0003, ADR-0004, ADR-0006]` | `[..., ADR-0006, ADR-0018]` |
| **C3** | **§6.2**, tabela, linha `QG-1`, coluna *Quem libera* | `DEP-PRD` | **`DEP-EXE`** |
| **C4** | **§6.2**, apos a *Regra de portao*, antes da nota de `QG-6` | *(inexistente)* | Nota normativa de **8 linhas** + linha em branco *(texto integral em §2.2)* |
| **C5** | Historico de versoes, ao final | *(inexistente)* | linha `1.5.0`, descrevendo C1 a C4 |

**`atualizado_em` nao muda:** ja declara `2026-07-29`, a data do proprio candidato.

**A linha `QG-1`, integral, antes e depois:**

```
antes:  | QG-1 | Apos especificar | A spec define resultado, criterio de aceite e o que esta fora? | DEP-PRD |
depois: | QG-1 | Apos especificar | A spec define resultado, criterio de aceite e o que esta fora? | DEP-EXE |
```

**As outras seis linhas da tabela de portoes — `QG-0`, `QG-2`, `QG-3`, `QG-4`, `QG-5` e
`QG-6` — nao sao tocadas. A *Regra de portao* nao e alterada: ela passa a ser cumprida.**
**475 → 485 linhas *(+10)* · 13 acrescentadas · 3 substituidas · 5 blocos de diff.**

### 2.1 O que o diff **nao** contem

| Nao contem | Verificacao |
|---|---|
| Alteracao em **§7.3** | **Zero linhas tocadas.** *Escopo e prioridade de produto* segue: **decide DEP-PRD** |
| Alteracao em **§4** *(Principios Imutaveis)* | **Zero** — **PI-05 e restaurado, nao tocado** |
| Alteracao em **§8** *(Linhas Vermelhas)* | **Zero** — **LV-03 deixa de ter caso permanente, e o texto nao muda** |
| Alteracao em **§10** *(Hierarquia Normativa)* | **Zero** |
| Alteracao na **Regra de portao** | **Zero** — o texto permanece **literalmente identico** |
| Portao criado ou removido | **Zero** — **7 antes, 7 depois** |
| Excecao formal | **Zero** — `governance/exceptions/` permanece **vazio** |

### 2.2 A nota, texto integral — **C4**

> **Sobre QG-1 e a regra de portao.** `QG-1` verifica a **Spec**, e a Spec e produzida por
> **DEP-PRD** (FND-09 §8.2, linha `SPC`). **Liberar o portao nao e aprovar o artefato:**
> liberar e confirmar que os tres itens exigidos estao presentes e verificaveis por terceiro;
> aprovar o conteudo segue a **classe da mudanca** (FND-04 §2). O liberador de `QG-1` e
> **DEP-EXE**, ja titular da **homologacao** de *escopo e prioridade de produto* em §7.3 e ja
> liberador de `QG-0`. **Nenhum titular novo foi criado** — o nome ja constava de §7.3.
> **DEP-PRD segue decidindo o escopo**, e o veto de **DEP-QAR** sobre criterio de aceite nao
> verificavel permanece integral (LV-09).

## 3. Identificadores de integridade

| Objeto | Versao | Linhas | `H-A` | `H-N` |
|---|---|---|---|---|
| **`FND-01` em vigor** | 1.4.0 | **475** | `1d70efa9b39372f98a92b466c30405eb08393c6ad8a152facd2ce76cb95e1def` | `a4048ee4cdd2f000662bae6e2d6da1332ce4022ba85009f0d4d7f410bb86e253` |
| **`FND-01` candidato** | **1.5.0** | **485** | **`2d962616ebd1b1e952eac1f3c98873385d32d26160d7e8f3f9e2c82de7ac310d`** | `fcb6e4bd5dd2e8d59c5f8038d0f85b2fdc1239fe78f7be5439bf640779536198` |

**`H-P` do fundacional = `H-A`** — a promulgacao **nao executa O4** sobre FND-01, que ja esta
`ativo` e `ratificada`.

**Terminadores:** `FND-01` usa **`LF`**, e o candidato **preserva `LF` em 485 de 485 linhas**,
conferido byte a byte. **Montado em modo binario** — a licao de metodo de PT-2026-002 §7.

> **Caminho do candidato preservado, fora do acervo — aplicacao de `RD-19`.**
> `E:\LucasIA\Projetos\_candidatos-LucaX-Enterprise-OS-2026-07-29-M1.12\FND-01-1.5.0.md`.
> **O arquivo existe e reproduz o `H-A` acima**, conferido apos a copia. **A pratica e nova:** os
> candidatos anteriores do acervo vivem **apenas** como *diff + hash*, e e exatamente isso que
> **RD-19** nomeia. **A licao e aplicada na mesma missao que a registra.**

### 3.1 `ADR-0018` — o objeto que transita de estado

| Campo | Valor |
|---|---|
| Caminho canonico | `decisions/ADR-0018-liberacao-do-portao-qg-1.md` |
| Versao · linhas | **1.0.0** · **243** |
| Estado hoje | `em-revisao` · `ratificacao: pendente` |
| **`H-A`** | **`8a89701caca39d8494c26a78919f740a576b161ba247ddca6fd15ff612305ebe`** |
| `H-N` | `9fb2fdf46d324dd4aed9ec7a801443d1144fefa7627a1b1700567f926237b3ad` |
| **`H-P` projetado** *(apos O4)* | **`e9912dd2096d08b1d63f52be715f9277c9765baadfa260b65f85456409e23e45`** |
| `H-N` apos O4 | **invariante — verificado** (IR-02, IR-06) |

### 3.2 `RFC-0014` — proposta antecedente

| Campo | Valor |
|---|---|
| Caminho · versao · linhas | `rfcs/RFC-0014-liberacao-do-portao-qg-1.md` · **1.0.0** · **226** |
| `H-A` | `fce49855f20763b2fd2eafd80dd1de606bff1de1e16ae7c6e48edf39041db129` |

### 3.3 Metodo de medicao — **reimplementacao validada antes do uso**

`IR-02` e `IR-03` foram **reimplementados de forma independente** e **validados primeiro
contra artefatos com hash ja publicado**, antes de medir qualquer candidato:

| Artefato de controle | `H-A` reproduz? | `H-N` reproduz? | Fonte do valor esperado |
|---|---|---|---|
| `FND-09` 1.3.0 | ✅ | ✅ | [PS-2026-005 §3](pacote-soberano-2026-07-29-rd-09.md) |
| `FND-10` 1.2.0 | ✅ | ✅ | idem |
| `DEP-QAR` 1.2.0 | ✅ *(reproduz o `H-P` publicado)* | ✅ | [MSG-2026-0005 §2](../memory/operacional/MSG-2026-0005-ato-soberano-aplicacao-dep-qar.md) |

**6 de 6 reproduzem, digito a digito.** A medicao dos candidatos so ocorreu **depois**.

## 4. Impacto — a verificacao que importa

| Verificacao | Resultado | Evidencia |
|---|---|---|
| **Titulares criados** | **ZERO** | `DEP-EXE` ja consta de §6.2 *(`QG-0`)* e de **cinco** materias de §7.3 |
| **Materias que mudam de titular** | **1** — a liberacao de `QG-1` | §2, C3 |
| **Direitos de decisao de §7.3 alterados** | **ZERO** | §2.1 |
| **Principios Imutaveis alterados** | **ZERO** — **PI-05 e restaurado** | §2.1 |
| **Linhas Vermelhas alteradas** | **ZERO** — **LV-03 perde um caso permanente** | §2.1 |
| **Hierarquia normativa** | **ZERO niveis alterados** | §2.1 |
| **Niveis de autonomia** | **ZERO** — `DEP-EXE` libera `QG-0` em **A3**; `QG-1` cabe no mesmo nivel | AU-03, LV-07 |
| **Veto de DEP-QAR** | **Inalterado** | LV-09 |
| **Portoes** | **7 antes · 7 depois · 0 criados · 0 removidos** | §2.1 |
| **Excecoes formais** | **ZERO criadas** — o diretorio permanece **vazio** | §2.1 |
| **Cartas alteradas** | **ZERO** | §5 |
| **Artefatos M1 editados** | **ZERO** | — |
| Outras linhas da tabela de portoes | **6 de 7 inalteradas** | §2 |
| Custo de contexto | **+10 linhas** em FND-01, perfil `nucleo`: **+2 de frontmatter, +1 de celula, +9 de nota, +1 de historico, −3 substituidas** | §2 |
| Reversibilidade | **Tipo 2** | ADR-0018 §10 |

## 5. A cascata **declarada e nao executada**

**Emendar a fonte nao emenda as projecoes, e executa-las aqui seria o defeito, nao o zelo.**

| Artefato | O que passa a divergir | Por que **nao** e emendado aqui | Dono | Gatilho |
|---|---|---|---|---|
| **FND-02 §2** e **§7** | *"dono unico de [...] portao QG-1"* e o diagrama | **Nao diverge de fato:** ser **dono** do portao e compativel com ser **liberado por outro**, e a nota de §6.2 desambigua. Alem disso, FND-02 tem **candidato 1.3.0 pendente** em PS-2026-004 — emendar aqui criaria **terceira versao concorrente** | DEP-GOV | Proxima emenda a FND-02 |
| **FND-09 §8.2**, linha `SPC` | O parentese *"(QG-1)"* na coluna *Aprova* | **Resolvido por [PS-2026-008](pacote-soberano-2026-07-29-rd-15.md)**, que remove o parentese ao corrigir RD-15 | DEP-GOV | Ato sobre PS-2026-008 |
| **FND-10 §10.3**, linha `Spec` | idem | idem | DEP-GOV | idem |
| **`DEP-PRD`** §5, §5.2, §8, §10.1 `RP-1`, §12 | Declara liberar `QG-1`; `RP-1` perde objeto | **Carta ratificada.** Emenda-la antes do ato sobre a fonte e **alteracao nao ratificada** (IR-01, IR-05) e inverte a ordem *fonte → projecao* (PJ-03) | DEP-EXE | **Ato sobre este pacote** |
| **`DEP-EXE`** §5, §6.3, §10 `I-4` | Passa a liberar **dois** portoes | idem | DEP-EXE | idem |
| **`DEP-ENG`** §6.3 e §7 | Emissor da liberacao de `QG-1` muda | idem | DEP-EXE | idem |

**Cartas alteradas por este pacote: ZERO. Fundacionais alteradas: ZERO — o candidato vive
fora do acervo.**

## 6. Risco residual

| # | Risco | Sev. | Mitigacao declarada |
|---|---|---|---|
| **RS-1** | `QG-1` vira **gargalo** em DEP-EXE | Media | Portao verifica **presenca e verificabilidade**, nao merito; `DEP-EXE I-5` veda decidir merito |
| **RS-2** | DEP-EXE passa a **decidir escopo** por via de portao | **Alta se a nota nao for ratificada; Baixa com ela** | A nota **C4** declara o contrario expressamente. **Sem a nota, este risco nao tem mitigacao** |
| **RS-3** | **Cascata aberta** por um ciclo | Media | §5, com dono e gatilho. **PJ-03**: fonte prevalece sobre projecao |
| **RS-4** | **Sem ato**, nenhuma Spec pode ser aberta | **Alta** | E o proprio bloqueio: impede o defeito de produzir efeito |

## 7. Minuta do ato — **pronta, com os valores verificados**

> ### Esta secao **nao e um ato**. Nada aqui produz efeito.

```
ATO SOBERANO DO FUNDADOR — <data do ato>

Apos revisar governance/pacote-soberano-2026-07-29-rd-14.md, RFC-0014, ADR-0018,
suas evidencias, revisao independente, riscos e ressalvas:

Aprovo e ratifico expressamente:

- ADR-0018, versao 1.0.0,
  SHA-256 8a89701caca39d8494c26a78919f740a576b161ba247ddca6fd15ff612305ebe.

Autorizo a promulgacao das alteracoes correspondentes em:

- FND-01, versao 1.5.0,
  SHA-256 2d962616ebd1b1e952eac1f3c98873385d32d26160d7e8f3f9e2c82de7ac310d,

exatamente no diff literal registrado em PS-2026-007 §2.

A entrada em vigor depende de verificacao independente de identidade, versao, hash
integral, diff literal, revisao e inexistencia de alteracao entre o candidato revisado
e o objeto a ser aplicado. FND-01 1.4.0 devera permanecer recuperavel como versao
historica substituida.

Este ato nao cria titular novo; nao altera direito de decisao de FND-01 §7.3, principio
imutavel, linha vermelha ou nivel da hierarquia normativa; nao cria nem remove portao;
nao autoriza excecao formal; nao emenda FND-02, FND-09, FND-10 nem Carta alguma; nao
altera artefatos historicos; nao alcanca RD-15 nem qualquer outro achado; e nao alcanca
qualquer objeto nao enumerado expressamente.
```

## 8. Recomendacao

| Campo | Conteudo |
|---|---|
| **Recomendacao** | **APROVAR** |
| **Fundamento** | A colisao e **interna a uma unica subsecao** e **verificavel em duas leituras**; a correcao e de **uma celula e uma nota**; **nenhum titular e criado** — o nome ja estava em §7.3; **nenhum direito de decisao muda**; e a emenda **restaura PI-05** em vez de excepciona-lo. **A excecao formal, unica alternativa que preservaria o texto, e juridicamente impossivel:** FND-01 §8.3 declara que Principios Imutaveis **nao admitem excecao** |
| **Contrapartida honesta** | A **cascata em tres Cartas ratificadas fica devida** por pelo menos um ciclo, e **RS-2** so tem mitigacao **se a nota for ratificada junto com a celula** |
| **O pacote informa; nao decide** | **Nao decidir e resultado valido.** O efeito de nao decidir esta em §1 |

## 9. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Achado que fecha | **RD-14** — [PT-2026-002 §5](relatorio-transicao-2026-07-29-fechamento.md) |
| Ressalva que fecha | **R1** de [FIT-2026-011](fitness/FIT-2026-011-fechamento-de-autoridade.md) |
| Bloqueio que remove | **B4** de PT-2026-002 §8 |
| Pendencia soberana que fecha | **Nenhuma anterior** — RD-14 nasceu na Missao 1.11 e **nao tinha pacote** |
| RFC → ADR | [RFC-0014](../rfcs/RFC-0014-liberacao-do-portao-qg-1.md) → [ADR-0018](../decisions/ADR-0018-liberacao-do-portao-qg-1.md) |
| Regra de integridade | [ADR-0012](../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md), `IR-01` a `IR-10` |
| Emenda constitucional anterior, **nao editada** | [ADR-0014](../decisions/ADR-0014-candidato-emenda-fnd-01-7-3-homologa.md) |
| Pacotes irmaos, **nao alcancados por este** | [PS-2026-004](pacote-soberano-2026-07-29-rd-02.md) · [PS-2026-005](pacote-soberano-2026-07-29-rd-09.md) · [PS-2026-006](pacote-soberano-2026-07-29-kms-eng.md) · [PS-2026-008](pacote-soberano-2026-07-29-rd-15.md) |
| Relatorio da missao | [PT-2026-003](relatorio-transicao-2026-07-29-fechamento-normativo.md) |
| Verificacao de aptidao | [FIT-2026-012](fitness/FIT-2026-012-fechamento-normativo-final.md) |
| Baseline vigente na submissao | **`BL-2026-07-29-05`** — [catalogo mestre §10](artifact-registry.md) |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-GOV | Pacote da **Missao 1.12**: emenda **C3** a **FND-01 §6.2** que fecha **RD-14**, com **diff literal** — **uma celula e uma nota de oito linhas, texto integral reproduzido** —, `H-A` e `H-N` **integrais** de base e candidato, `H-P` **projetado** do ADR e **minuta preenchida**. **Sexto pacote soberano; separado de PS-2026-008 por determinacao.** Registra que a colisao e **interna a §6.2** e que a **excecao formal e juridicamente impossivel** porque a regra de portao projeta **PI-05**, e FND-01 §8.3 veda excecao a Principio Imutavel. **Zero titulares criados · zero direitos de decisao alterados · zero principios ou linhas vermelhas tocados · zero portoes criados ou removidos · zero excecoes · zero Cartas emendadas.** Declara a **cascata nao executada** em FND-02, FND-09, FND-10 e **tres Cartas ratificadas**, com dono, gatilho e o motivo normativo de nao executa-la. §3.3 registra que `IR-02` e `IR-03` foram **reimplementados e validados contra tres artefatos de controle** — **6 de 6 reproduzem** — **antes** de medir qualquer candidato. |
