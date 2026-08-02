---
id: PS-2026-008
titulo: Pacote de decisao soberana — emenda C3 a FND-09 §8.2 e FND-10 §10.3 que fecha RD-15
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
decisoes_relacionadas: [ADR-0012, ADR-0017, ADR-0019]
substitui: []
substituido_por: null
canal: REPORTE
emissor: DEP-GOV
destinatario: SOBERANO
ttl: ate decisao do Soberano
resumo: Submete ao Soberano a emenda C3 que faz as linhas SPC e Spec remeterem a classe da mudanca e registra o conflito como erro da propria tabela, com diff literal, hashes integrais e a concorrencia com PS-2026-005 declarada.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# PS-2026-008 — Emenda **C3** a FND-09 §8.2 e FND-10 §10.3

> ## Este pacote **informa**. Nao decide, nao aprova, nao promulga e nao edita nada.
>
> **FND-09 permanece em 1.3.0 e FND-10 em 1.2.0.** Os candidatos **1.4.0** e **1.3.0** existem
> como **diff literal + hash**, **fora do acervo**.
>
> **Pacote separado de [PS-2026-007](pacote-soberano-2026-07-29-rd-14.md), por determinacao.**
> **RD-14** e **RD-15** sao materias distintas e **nao se misturam num ato**.
>
> **⚠ Concorrencia declarada com [PS-2026-005](pacote-soberano-2026-07-29-rd-09.md):** os dois
> pacotes emendam **os mesmos dois documentos**, em **celulas disjuntas**, e **reivindicam os
> mesmos numeros de versao**. Achado **RD-19**; regra de resolucao em **§5**.
>
> **Caminho exato:** `governance/pacote-soberano-2026-07-29-rd-15.md` *(RE-01)*.

## Proposito
Levar ao Soberano a emenda que fecha **RD-15**: para Spec **C2** ou **C3**, FND-09 §8.2 e
FND-04 §2 dao **aprovador e ratificador diferentes**, e a **segunda metade** da regra de
precedencia de FND-09 §8.2 — *registrar o conflito como erro desta tabela* — **nunca foi
cumprida**.

## Escopo
| Item | Definicao |
|---|---|
| Inclui | **Um** objeto: `ADR-0019` e a promulgacao de **FND-09 1.4.0** *(fonte)* e **FND-10 1.3.0** *(cascata, CV-04)* |
| **Nao** inclui | **RD-14** — [PS-2026-007](pacote-soberano-2026-07-29-rd-14.md) · **RD-02** — [PS-2026-004](pacote-soberano-2026-07-29-rd-02.md) · **RD-09** — [PS-2026-005](pacote-soberano-2026-07-29-rd-09.md) · `DEP-KMS`/`DEP-ENG` — [PS-2026-006](pacote-soberano-2026-07-29-kms-eng.md) · o **merito das classes** de FND-04 §2, **nao reaberto** · **FND-04 §2.1** *(RD-12)* e **§6** *(RD-18)* · Cartas · qualquer artefato historico |
| Natureza | **Reporte**, entidade `MSG`. **Nenhum** tipo, entidade, camada, template ou diretorio novo |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| **Autor da emenda** | **DEP-GOV** | FND-09 §8.2, linha `FND` |
| **Revisor independente** | **DEP-QAR** | RM-06b |
| **DECIDE** | **SOBERANO** | **C3. Indelegavel.** **Nao ocorreu** |

> **Residuo declarado (PI-10).** **DEP-GOV e proprietario dos dois documentos emendados**, e o
> item **H3** faz um deles **registrar erro proprio**. O residuo e **de posicao contraria ao
> interesse do autor** — a emenda **amplia** a exposicao de quem a escreve —, e por isso e
> declarado sem ser suprido. **DEP-EXE e DEP-PRD sao areas alcancadas** e **nao participaram**
> da autoria nem da revisao.

---

## 1. O que se pede

| # | Objeto | Ato pedido | Se **nao** houver ato |
|---|---|---|---|
| **1** | **`ADR-0019`** + promulgacao de **`FND-09` 1.4.0** e **`FND-10` 1.3.0** | **Aprovacao e ratificacao** | As duas permanecem em 1.3.0 e 1.2.0. **Spec C2 e C3 seguem sem titular unico de aprovacao**, o escalonamento segue **indeterminado** (PT-2026-002 §4.3) e a precedencia segue sendo aplicada **sem o registro que ela propria exige** |

> **Aprovacao parcial e desaconselhada com fundamento.** FND-10 §10.3 **declara-se projecao**
> de FND-09 §8.2; ratificar so a fonte deixaria a projecao contradizendo o documento de que ela
> propria diz derivar — **estado pior que o atual** (RFC-0015 §9, D2).

## 2. Diff literal

### 2.1 `FND-09` 1.3.0 → **1.4.0** — a **fonte**

| # | Local | Antes | Depois |
|---|---|---|---|
| **N1** | frontmatter | `versao: 1.3.0` | `versao: 1.4.0` |
| **N2** | frontmatter | `atualizado_em: 2026-07-28` | `atualizado_em: 2026-07-29` |
| **N3** | frontmatter | `decisoes_relacionadas: [ADR-0001, ..., ADR-0008]` | `[..., ADR-0008, ADR-0019]` |
| **N4** | **§8.2**, linha `SPC`, colunas *Aprova* e *Ratifica* | `DEP-PRD (QG-1)` · `—` | **`conforme classe (FND-04 §2)`** · **`SOBERANO se C3 ou Tipo 1`** |
| **N5** | **§8.2**, **antes** da matriz, apos o paragrafo de precedencia | *(inexistente)* | Nota normativa de **9 linhas** + linha em branco *(texto integral em §2.3)* |
| **N6** | Historico de versoes, ao final | *(inexistente)* | linha `1.4.0`, descrevendo N1 a N5 |

**A linha `SPC`, integral, antes e depois:**

```
antes:  | SPC | DEP-PRD | DEP-ENG + DEP-QAR | DEP-PRD (QG-1) | — | DEP-PRD |
depois: | SPC | DEP-PRD | DEP-ENG + DEP-QAR | conforme classe (FND-04 §2) | SOBERANO se C3 ou Tipo 1 | DEP-PRD |
```

**Colunas *Propoe / cria*, *Revisa* e *Aposenta* inalteradas. Nenhuma outra das 21 linhas
tocada. O paragrafo da regra de precedencia nao e alterado: ele passa a ser cumprido.**
**1.243 → 1.254 linhas *(+11)* · 15 acrescentadas · 4 substituidas · 4 blocos de diff.**

> **A nota de N5 vai *antes* da matriz, e a posicao e deliberada.** [PS-2026-005](pacote-soberano-2026-07-29-rd-09.md)
> insere a sua **depois** da matriz. **Os dois pontos de insercao sao disjuntos**, de modo que
> o rebase de `RD-19` nao disputa nenhum byte.

### 2.2 `FND-10` 1.2.0 → **1.3.0** — a **cascata**

| # | Local | Antes | Depois |
|---|---|---|---|
| **Q1** | frontmatter | `versao: 1.2.0` | `versao: 1.3.0` |
| **Q2** | frontmatter | `atualizado_em: 2026-07-28` | `atualizado_em: 2026-07-29` |
| **Q3** | frontmatter | `decisoes_relacionadas: [ADR-0003, ..., ADR-0009]` | `[..., ADR-0009, ADR-0019]` |
| **Q4** | **§10.3**, linha `Spec`, colunas *Aprova* e *Ratifica* | `DEP-PRD (QG-1)` · `—` | **`conforme classe`** · **`SOBERANO se C3/Tipo 1`** |
| **Q5** | **§10.3**, apos a matriz, antes da nota da coluna *Local* | *(inexistente)* | Nota de **5 linhas** + linha em branco *(texto integral em §2.3)* |
| **Q6** | Historico de versoes, **ao final** | *(inexistente)* | linha `1.3.0`, descrevendo Q1 a Q5 |

**A linha `Spec`, integral, antes e depois:**

```
antes:  | Spec | DEP-PRD (QG-1) | — | M2 | `sob-demanda` |
depois: | Spec | conforme classe | SOBERANO se C3/Tipo 1 | M2 | `sob-demanda` |
```

**Colunas *Mutabilidade* e *Perfil padrao* inalteradas. Nenhum dos outros 24 tipos documentais
tocado.**
**764 → 771 linhas *(+7)* · 11 acrescentadas · 4 substituidas · 4 blocos de diff.**

> **Nota sobre a posicao de Q6.** O historico de FND-10 **ja estava fora de ordem** na versao em
> vigor — `1.1.0` figura **depois** de `1.2.0`. A linha nova foi anexada **ao final**. **A
> desordem preexistente nao foi corrigida:** o texto esta **dentro de `H-N`** de fundacional
> ratificada (IR-01). Achado **RD-13**, ja aberto, **nao reaberto**.

### 2.3 As duas notas, texto integral

**N5 — em FND-09 §8.2, antes da matriz:**

> **Registro de conflito — linha `SPC`.** A coluna *Aprova* declarava **`DEP-PRD (QG-1)`** e a
> coluna *Ratifica* declarava **`—`**, o que **contradizia FND-04 §2** para Spec de classe
> **C2** ou **C3**. O conflito e **registrado como erro desta tabela**, na forma que o paragrafo
> acima exige, e as duas celulas passam a **remeter a classe** em vez de fixar titular. **Aprovar
> o artefato e liberar o portao sao atos distintos** (FND-01 §6.2): `QG-1` e liberado por
> **DEP-EXE** e **nao consta desta tabela**. **A classe de uma Spec e a do seu efeito** (AL-01),
> com **C1 como piso** (FND-04 §6, linha *Spec*); na duvida prevalece a classificacao mais
> restritiva (FND-01 §7.1). **Nenhum titular foi ampliado:** todos os nomes ja constavam de
> FND-04 §2.

**Q5 — em FND-10 §10.3, apos a matriz:**

> **A linha `Spec` acompanha a fonte.** As colunas *Aprova* e *Ratifica* desta matriz sao
> projecao de FND-09 §8.2 (PJ-02); a alteracao ali e **fonte**, e esta e **cascata** (CV-04).
> O fundamento e que **aprovar o artefato e liberar o portao sao atos distintos**: `QG-1` e
> liberado por **DEP-EXE** (FND-01 §6.2) e **nao e** a aprovacao da Spec, que segue a **classe
> da mudanca** (FND-04 §2), com **C1 como piso** (FND-04 §6). **Nenhum titular ampliado.**

> **A nota N5 pressupoe [PS-2026-007](pacote-soberano-2026-07-29-rd-14.md) apenas na frase
> sobre `QG-1`.** Se PS-2026-007 nao for ratificado, a frase permanece **verdadeira quanto ao
> que afirma** — *portao nao consta desta tabela* — e **incorreta quanto ao titular**.
> **Declarado como risco `RS-5` em §6**; a correcao seria uma emenda **C0** posterior.

## 3. Identificadores de integridade

| Objeto | Versao | Linhas | `H-A` | `H-N` |
|---|---|---|---|---|
| **`FND-09` em vigor** | 1.3.0 | **1.243** | `711709a7f6fa71f07818c7f646922f6b4bda1067e844300a4f049f2744ce2ddd` | `093a49626ecd2fbfdfa0e3e21d90e634a66479095f5eb1401e788333f8d36183` |
| **`FND-09` candidato** | **1.4.0** | **1.254** | **`4bb00ff9076845db590de6a8534e0200d55edaf4933b69bf5c86752347ef04ab`** | `7814c04f3cf41556385194a04bb0cac9cf6bef1b07b52b03f442e02383c34eb4` |
| **`FND-10` em vigor** | 1.2.0 | **764** | `acba465671d3fbae08653dd87b478bc576c30a80ada0a93aa6adf5c114f157e3` | `cd1c6d33b200b9769e8515249731fff9ac33194b5b54fe2af9e3e49b59143c9e` |
| **`FND-10` candidato** | **1.3.0** | **771** | **`6012074a2028ca8034bd17ccd5eb011dda83c6aa0e4a218a911770a2c982bd25`** | `297c2efe6d1022b1d8d790813b08a4542ca36028b414fbe3079f364052692adb` |

**`H-P` dos dois fundacionais = `H-A`** — a promulgacao **nao executa O4**.

> **CRLF declarado e conferido.** **`FND-10` usa `CRLF`**, enquanto FND-09 usa `LF`. O candidato
> **preserva `CRLF` em 771 de 771 linhas**, verificado byte a byte, e foi **montado em modo
> binario** — a licao de metodo de PT-2026-002 §7, aplicada na origem e nao apos falha.

> **Caminho dos candidatos preservados, fora do acervo (RD-19).** `E:\LucasIA\Projetos\_candidatos-LucaX-Enterprise-OS-2026-07-29-M1.12\FND-09-1.4.0.md` e
> `E:\LucasIA\Projetos\_candidatos-LucaX-Enterprise-OS-2026-07-29-M1.12\FND-10-1.3.0.md`. **Os arquivos existem** e reproduzem os `H-A` acima — conferidos apos a
> copia. **E a aplicacao, nesta missao, da propria licao que RD-19 registra.**

### 3.1 `ADR-0019` — o objeto que transita de estado

| Campo | Valor |
|---|---|
| Caminho canonico | `decisions/ADR-0019-aprovador-e-ratificador-de-spec.md` |
| Versao · linhas | **1.0.0** · **251** |
| Estado hoje | `em-revisao` · `ratificacao: pendente` |
| **`H-A`** | **`a9ca799bdb0300809357a8e797c971e63817ee2e8e77192ee962083b2073e833`** |
| `H-N` | `18b276a20d43a998393ea03bfc0b9f45c282586b7a57e59294fffca5f0cd0ecb` |
| **`H-P` projetado** *(apos O4)* | **`872ba071418322b816a136344add32c2a7a8fe7b27b1199383cd817ce56f481e`** |
| `H-N` apos O4 | **invariante — verificado** (IR-02, IR-06) |

### 3.2 `RFC-0015` — proposta antecedente

| Campo | Valor |
|---|---|
| Caminho · versao · linhas | `rfcs/RFC-0015-aprovador-e-ratificador-de-spec.md` · **1.0.0** · **241** |
| `H-A` | `25f5a33bb8e1dd5f294a5ad943054370cb7bc3d31a404315c2225f68318cf025` |

### 3.3 Metodo de medicao

Identico ao de [PS-2026-007 §3.3](pacote-soberano-2026-07-29-rd-14.md): `IR-02` e `IR-03`
**reimplementados de forma independente** e **validados contra tres artefatos de controle com
hash ja publicado** — `FND-09` 1.3.0, `FND-10` 1.2.0 e `DEP-QAR` 1.2.0 —, **6 de 6 reproduzindo
digito a digito**, **antes** de qualquer medicao de candidato.

## 4. Impacto — a verificacao que importa

| Verificacao | Resultado | Evidencia |
|---|---|---|
| **Titulares ampliados** | **ZERO** | `DEP-EXE`, `DEP-GOV` e `SOBERANO` ja constam de **FND-04 §2**, origem declarada de FND-09 §8.2 |
| **Nomes que entram na coluna *Aprova*** | **ZERO** — a celula deixa de **nomear** e passa a **remeter** | §2.1 |
| **Nomes que entram na coluna *Ratifica*** | **1 — `SOBERANO`**, e so para **C3 ou Tipo 1** | Ja exigido por **AU-05** e **FND-04 §2.1**, **nao tocados** |
| **Titulares reduzidos** | **1 materia** — `DEP-PRD` deixa de ser aprovador **unico** de toda Spec; segue aprovando **C0 e C1** | §2.1 |
| **Classes de FND-04 alteradas** | **ZERO** — §2, §2.1, §2.2 e §6 **intactas** | — |
| **Regra de precedencia de §8.2** | **Texto inalterado** — passa a ser **cumprida** | §2.1 |
| **`QG-1`** | **Nao determinado aqui** — o parentese sai porque **portao nao e aprovacao** | [PS-2026-007](pacote-soberano-2026-07-29-rd-14.md) |
| **Outras linhas das matrizes** | **20 de 21** em FND-09 · **24 de 25** em FND-10 **inalteradas** | §2 |
| **Cartas alteradas** | **ZERO** | — |
| **Artefatos M1 editados** | **ZERO** | — |
| Entidades · tipos · camadas · portoes · departamentos · classes | **0 criados · 0 alterados** | — |
| Custo de contexto | **+18 linhas** somadas. Os dois sao `nucleo` **por recorte**, e o recorte alcanca §8.2 e §10.3: **+4 de celula, +14 de nota, frontmatter e historico** | §2 |
| Reversibilidade | **Tipo 2** | ADR-0019 §10 |

## 5. `RD-19` — a concorrencia com PS-2026-005, declarada

**Dois pacotes pendentes emendam os mesmos dois documentos.**

| Fato | PS-2026-005 | **PS-2026-008** *(este)* |
|---|---|---|
| Linha de FND-09 §8.2 | **`FIT`** | **`SPC`** |
| Linha de FND-10 §10.3 | **`Fitness Check`** | **`Spec`** |
| Posicao da nota em §8.2 | **apos** a matriz | **antes** da matriz |
| Versao reivindicada | **FND-09 1.4.0 · FND-10 1.3.0** | **FND-09 1.4.0 · FND-10 1.3.0** |
| Base medida | **vigente** — 1.3.0 e 1.2.0 | **vigente** — 1.3.0 e 1.2.0 |
| **Byte disputado** | **NENHUM** — celulas, linhas e pontos de insercao **disjuntos** | idem |

| # | Regra de resolucao |
|---|---|
| **O1** | **Versao e atribuida na promulgacao, nao na candidatura.** Dois candidatos podem propor o mesmo numero enquanto **nenhum vigora** |
| **O2** | **O segundo a ser ratificado e reemitido rebaseado**, com novo numero e **novos hashes**, **antes** de ser aplicado |
| **O3** | O rebase e **mecanico e sem perda** — celulas e insercoes disjuntas; **nenhum merito e reaberto** |
| **O4** | **Ratificar os dois no mesmo ato nao dispensa O2:** o ato alcanca os dois ADR, e a **aplicacao** exige um candidato unico medido |

> **Nao ha ordem preferida, e este pacote nao pede precedencia sobre PS-2026-005.** Os dois sao
> independentes no merito. **O achado e do acervo, nao dos pacotes:** o sistema publica
> candidatos como *diff + hash* **sem arquivo**, e por isso uma emenda posterior sobre o mesmo
> objeto **nao consegue se medir sobre a anterior**. Dono **DEP-GOV**; gatilho: **promulgacao do
> primeiro dos dois pacotes**.

## 6. Risco residual

| # | Risco | Sev. | Mitigacao declarada |
|---|---|---|---|
| **RS-1** | **DEP-EXE aprova Spec C2 e tambem libera `QG-1`** apos PS-2026-007 | Media | **Atos distintos, e a distincao esta escrita.** C2 exige **parecer de DEP-GOV**, que o portao nao exige — **ha contraditorio no ato de aprovacao** |
| **RS-2** | **Classificacao vira o novo ponto de ambiguidade** | Media | **FND-04 §2 ja responde:** classificacao pelo proponente, **validada por DEP-GOV**. Nenhuma regra nova criada |
| **RS-3** | **RD-19** — pacote aplicado sobre base errada | **Alta** | `O1` a `O4` de §5; a base medida esta publicada com `H-A` integral |
| **RS-4** | **RD-18** envelhece — FND-04 §6 e §2 seguem com duas regras geradoras de classe | Media | Declarado; dono **DEP-GOV**; gatilho *"proxima emenda a FND-04"*. **Emendar FND-04 nao foi pedido** (LM-03) |
| **RS-5** | **Sem PS-2026-007**, a nota N5 afirma que `QG-1` e liberado por **DEP-EXE**, e o liberador vigente seria `DEP-PRD` | Media | **Declarado em §2.3.** Corrigivel por emenda **C0** posterior; **nao invalida** as celulas N4, que independem do portao |

## 7. Minuta do ato — **pronta, com os valores verificados**

> ### Esta secao **nao e um ato**. Nada aqui produz efeito.

```
ATO SOBERANO DO FUNDADOR — <data do ato>

Apos revisar governance/pacote-soberano-2026-07-29-rd-15.md, RFC-0015, ADR-0019,
suas evidencias, revisao independente, riscos e ressalvas:

Aprovo e ratifico expressamente:

- ADR-0019, versao 1.0.0,
  SHA-256 a9ca799bdb0300809357a8e797c971e63817ee2e8e77192ee962083b2073e833.

Autorizo a promulgacao das alteracoes correspondentes em:

- FND-09, versao 1.4.0,
  SHA-256 4bb00ff9076845db590de6a8534e0200d55edaf4933b69bf5c86752347ef04ab;
- FND-10, versao 1.3.0,
  SHA-256 6012074a2028ca8034bd17ccd5eb011dda83c6aa0e4a218a911770a2c982bd25,

exatamente no diff literal registrado em PS-2026-008 §2.

A entrada em vigor depende de verificacao independente de identidade, versao, hash
integral, diff literal, revisao e inexistencia de alteracao entre o candidato revisado
e o objeto a ser aplicado. FND-09 1.3.0 e FND-10 1.2.0 deverao permanecer recuperaveis
como versoes historicas substituidas.

Se PS-2026-005 for ratificado antes deste, ou no mesmo ato, o candidato aqui enumerado
devera ser reemitido rebaseado, com novo numero de versao e novos hashes, antes de
qualquer aplicacao, conforme PS-2026-008 §5.

Este ato nao amplia titulares, competencias ou direitos decisorios; nao altera nenhuma
classe de mudanca de FND-04; nao determina quem libera QG-1; nao emenda FND-01, FND-04
nem Carta alguma; nao altera artefatos historicos; nao alcanca RD-14, RD-18, RD-19 nem
qualquer outro achado; e nao alcanca qualquer objeto nao enumerado expressamente.
```

## 8. Recomendacao

| Campo | Conteudo |
|---|---|
| **Recomendacao** | **APROVAR** |
| **Fundamento** | A emenda **nao escolhe titular**: devolve a pergunta a **FND-04 §2**, que a propria FND-09 §8.2 declara ser sua origem *"sem redefini-las"*. **A forma nao e nova** — a linha `ADR` das **duas** tabelas ja usa exatamente `conforme classe` e `SOBERANO se C3/Tipo 1`; **a `SPC` era a excecao**. E **H3 tem valor proprio**: e o **primeiro registro de conflito feito no documento que erra**, cumprindo uma metade de regra **nunca cumprida em nenhum conflito** |
| **Contrapartida honesta** | **RD-18 e RD-19 nascem deste pacote e nao sao fechados por ele.** **RD-19 e de severidade Alta na aplicacao:** sem `O1`–`O4`, um dos dois pacotes seria aplicado sobre base errada. E **RS-5** deixa uma frase da nota N5 dependente de PS-2026-007 |
| **O pacote informa; nao decide** | **Nao decidir e resultado valido.** O efeito de nao decidir esta em §1 |

## 9. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Achado que fecha | **RD-15** — [PT-2026-002 §5](relatorio-transicao-2026-07-29-fechamento.md) |
| Ressalva que fecha | **R2** de [FIT-2026-011](fitness/FIT-2026-011-fechamento-de-autoridade.md) |
| Bloqueio que remove | **B5** de PT-2026-002 §8 |
| Achados que **abre** | **RD-18** *(FND-04 §6 × §2)* · **RD-19** *(pacotes concorrentes)* |
| Achado **nao reaberto** | **RD-13** — desordem do historico de FND-10 |
| RFC → ADR | [RFC-0015](../rfcs/RFC-0015-aprovador-e-ratificador-de-spec.md) → [ADR-0019](../decisions/ADR-0019-aprovador-e-ratificador-de-spec.md) |
| Decisao propagada | [ADR-0012](../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md) |
| **Pacote concorrente**, **nao reaberto e nao editado** | [PS-2026-005](pacote-soberano-2026-07-29-rd-09.md) |
| Pacotes irmaos, **nao alcancados por este** | [PS-2026-004](pacote-soberano-2026-07-29-rd-02.md) · [PS-2026-006](pacote-soberano-2026-07-29-kms-eng.md) · [PS-2026-007](pacote-soberano-2026-07-29-rd-14.md) |
| Relatorio da missao | [PT-2026-003](relatorio-transicao-2026-07-29-fechamento-normativo.md) |
| Verificacao de aptidao | [FIT-2026-012](fitness/FIT-2026-012-fechamento-normativo-final.md) |
| Baseline vigente na submissao | **`BL-2026-07-29-05`** — [catalogo mestre §10](artifact-registry.md) |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-GOV | Pacote da **Missao 1.12**: emenda **C3** a **FND-09 §8.2** *(fonte)* e **FND-10 §10.3** *(cascata)* que fecha **RD-15**, com **diff literal** — **quatro celulas e duas notas, texto integral reproduzido** —, `H-A` e `H-N` **integrais** de base e candidatos, `H-P` **projetado** do ADR e **minuta preenchida**. **Setimo pacote soberano; separado de PS-2026-007 por determinacao.** As linhas `SPC` e `Spec` passam a **remeter a classe**, **no mesmo padrao que a linha `ADR` das duas tabelas ja usa**, e a nota de FND-09 **registra o conflito como erro da propria tabela** — cumprindo a **segunda metade da regra de precedencia**, nunca cumprida em nenhum conflito ate hoje. **Zero titulares ampliados · zero classes de FND-04 alteradas · zero Cartas emendadas · zero artefatos M1 editados.** Declara **RD-19**: este pacote e **PS-2026-005** emendam os **mesmos dois documentos** em **celulas e pontos de insercao disjuntos**, reivindicando os **mesmos numeros de versao**, e propoe `O1` a `O4` para resolver por **rebase mecanico** — **nenhum byte disputado**. Declara tambem **RD-18** e o risco **RS-5**, em que uma frase da nota N5 depende de PS-2026-007. **`CRLF` de FND-10 preservado em 771 de 771 linhas**, montagem em modo binario **na origem**. |
