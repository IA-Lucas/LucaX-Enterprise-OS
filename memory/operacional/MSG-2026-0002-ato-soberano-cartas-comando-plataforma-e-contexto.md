---
id: MSG-2026-0002
titulo: Ato Soberano de ratificacao das Cartas DEP-EXE e DEP-KMS, de MEM-EST-0001 e de acolhimento de FIT-2026-001 e FIT-2026-002
tipo: relatorio
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: SOBERANO
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: null
decisoes_relacionadas: [ADR-0010, ADR-0011]
substitui: []
substituido_por: null
canal: DIRETIVA
emissor: SOBERANO
destinatario: DEP-GOV
ttl: 1 ciclo — expira sem perda; o efeito duravel foi promovido no mesmo ato (§6)
resumo: Registra, como fonte canonica unica, o ato soberano de 2026-07-28 que ratifica DEP-EXE, DEP-KMS e MEM-EST-0001, acolhe FIT-2026-001 e FIT-2026-002 como pareceres e determina a Primeira Revisao Estrutural.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# MSG-2026-0002 — Ato Soberano sobre as Cartas de Comando e Plataforma, o Contexto do Soberano e os dois pareceres

## Proposito
Registrar **uma unica vez** o ato soberano de 2026-07-28 que alcanca `DEP-EXE`, `DEP-KMS`,
`MEM-EST-0001`, `FIT-2026-001`, `FIT-2026-002` e `INC-2026-002`, com os IDs, versoes e hashes
que ele vincula. Indices, frontmatters e catalogo **referenciam** esta secao; nenhum a
reproduz (CM-09, PJ-01).

> **Este e o segundo ato soberano registrado, e tem fonte canonica propria.** O primeiro
> — 2026-07-28, sobre `DEP-QAR` e `DEP-ENG` — vive em
> [MSG-2026-0001](MSG-2026-0001-ato-soberano-ratificacao-cartas-piloto.md), que **nao foi
> editado**. Dois atos, duas fontes; nunca uma fonte que acumule (precedente de
> MSG-2026-0001 §6).

## Escopo
| Item | Definicao |
|---|---|
| Inclui | O ato de 2026-07-28 sobre os seis objetos que ele nomeia, seu alcance, suas condicoes de eficacia e os efeitos aplicados |
| **Nao** inclui | Merito dos artefatos ratificados *(objeto de [REV-ESTRUTURAL-I](../../foundation/revisao-estrutural-01-2026-07-28.md))*; qualquer artefato que o ato nao nomeie |
| Instrumento | **Diretiva**, tipo documental de [FND-10 §4.6](../../foundation/10-artifact-framework.md), entidade `MSG`. Nenhum tipo, entidade, camada ou diretorio novo |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| **Emissor** | **SOBERANO** | PI-01 — autoridade final, indelegavel |
| **Registra** | **DEP-GOV** | LM-05, CV-09 — quem registra e papel distinto de quem executou a mudanca |
| **Verifica a eficacia** | **DEP-QAR** | FND-10 §10.5 |
| **Nao participa da verificacao** | **DEP-EXE** | Autor das duas Cartas ratificadas; verificar a propria ratificacao repetiria a causa de [INC-2026-001](../../governance/incidents/INC-2026-001-ratificacao-inferida.md) |
| **Nao participa da verificacao** | **DEP-KMS** | Autor de `MEM-EST-0001` |

---

## 1. O ato

| Campo | Conteudo |
|---|---|
| Emissor | **SOBERANO** (Lucas) |
| Canal | **DIRETIVA** (FND-05 §2) |
| Data do ato | **2026-07-28** |
| Objeto | Quatro determinacoes: ratificacao de `DEP-EXE` e `DEP-KMS`; ratificacao de `MEM-EST-0001`; acolhimento de `FIT-2026-001` e `FIT-2026-002` com autorizacao de encerramento de `INC-2026-002`; determinacao da **Primeira Revisao Estrutural** |
| Natureza | **Aprovacao e ratificacao no mesmo ato** para as Cartas — matriz de FND-09 §8.2, linha `DEP` |
| Condicao de eficacia | Entrada em vigor **apos verificacao independente** de versao, hash SHA-256 integral e integridade, e comprovacao de que **nenhuma alteracao ocorreu entre a revisao e a ratificacao** |
| Limite expresso | Nao aprova futura emenda de `DEP-QAR`; nao ratifica novos ADRs; nao alcanca artefato alterado ou criado posteriormente |

### 1.1 Texto do ato

> ATO SOBERANO DO FUNDADOR — 2026-07-28
>
> Apos revisar os resultados, evidencias, ressalvas e riscos da Missao 1.7:
>
> 1. Aprovo e ratifico expressamente as Cartas DEP-EXE e DEP-KMS, exatamente nas versoes
> submetidas no pacote de ratificacao de FIT-2026-006.
>
> A eficacia deste ato depende da verificacao independente das versoes e dos hashes SHA-256
> integrais. O registro canonico devera anexar esses identificadores e comprovar que nenhuma
> alteracao ocorreu entre a revisao e a ratificacao.
>
> 2. Ratifico MEM-EST-0001 exatamente na versao canonica submetida pela Missao 1.5, incluindo
> as afirmacoes registradas como unknown, que permanecem desconhecidas e nao podem ser
> preenchidas por inferencia.
>
> Sua entrada em vigor depende da verificacao independente de versao, hash e integridade.
>
> 3. Acolho expressamente FIT-2026-001 e FIT-2026-002 como pareceres, sem eleva-los a norma, e
> autorizo o encerramento de INC-2026-002 apos comprovacao independente de que todas as
> condicoes pendentes foram corretamente registradas.
>
> 4. Determino a execucao da Primeira Revisao Estrutural do LucaX Enterprise OS por meio da
> Missao 1.8.
>
> Este ato nao aprova futura emenda de DEP-QAR, nao ratifica novos ADRs e nao alcanca
> artefatos alterados ou criados posteriormente.

> **Transcricao literal.** O texto e reproduzido como emitido (LX-07).

### 1.2 Uma designacao imprecisa, resolvida sem alterar o ato

| Campo | Conteudo |
|---|---|
| **O que o ato diz** | *"nas versoes submetidas no **pacote de ratificacao de FIT-2026-006**"* |
| **Fato verificado** | `FIT-2026-006` **nao contem** pacote de ratificacao. O unico pacote de ratificacao do acervo esta em [REV-INTERCLASSES §6](../../foundation/revisao-arquitetural-validacao-interclasses-2026-07-28.md), produzido pela **mesma missao** que `FIT-2026-006` encerra |
| **O objeto e ambiguo?** | **Nao.** Existe **exatamente um** pacote de ratificacao no acervo; ele nomeia **exatamente** `DEP-EXE` e `DEP-KMS`, com **versao, hash SHA-256 e contagem de linhas**; e os dois artefatos que o ato nomeia sao os dois que o pacote contem. A designacao aponta a **missao** correta e o **conteudo** correto; erra apenas o **arquivo** |
| **Tratamento** | O ato **nao e corrigido nem reinterpretado** (LM-03, LV-05). Registra-se a divergencia de designacao e a fonte real do objeto. A verificacao de §2 e feita contra **REV-INTERCLASSES §6**, e o resultado e conferido contra os artefatos em disco |
| **Alternativa recusada** | Devolver o ato ao Soberano para reemissao — recusada por **proporcionalidade**: o objeto e univocamente determinavel por tres identificadores independentes (ID, versao, hash), e nenhum deles depende de qual arquivo hospeda o pacote. A recusa fica registrada para que a escolha seja auditavel, nao presumida |
| Achado gerado | **RE-01** — [REV-ESTRUTURAL-I §9](../../foundation/revisao-estrutural-01-2026-07-28.md) |

## 2. Objeto vinculado — IDs, versoes e hashes

Cumprimento da instrucao acessoria de §1. Tres hashes distintos, conforme
[ADR-0012](../../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md):
**H-A** hash do arquivo submetido · **H-N** hash do conteudo normativo · **H-P** hash do
arquivo apos a transicao de estado.

### 2.1 Cartas de Departamento

| Artefato | ID | Versao | **H-A — arquivo submetido** | **H-N — conteudo normativo** | **H-P — apos O4** | Linhas |
|---|---|---|---|---|---|---|
| Gabinete Executivo *(Comando)* | **`DEP-EXE`** | **1.0.0** | `437f261467df28d94e519d54c40af33f132a83696892d22abc14db134aa942e1` | `47a499b36fb945ddde1bc6d504cac2c7a2a8e90b647f04e65d22d78dd06ec816` | `fa7a6ae293afd53577c7c37076d8543a01fa187a4d6490dcf2f2a47b940f2bb8` | **481** |
| Conhecimento e Memoria *(Plataforma)* | **`DEP-KMS`** | **1.0.0** | `c261ff93e36688a76c82e5efe5110e946c331accc6fc6f11d1b55c8059e31ac5` | `613ec1a42677787e21cb3aef8fd7c9bfd72eeeedc85d53f3c05577b154bff327` | `a63bb267d15d5d81335a60776ebb130d60dbd5b89e62e0702794a25bc638aacf` | **460** |

**H-A conferido contra:** [REV-INTERCLASSES §6.1 e §6.2](../../foundation/revisao-arquitetural-validacao-interclasses-2026-07-28.md)
— **reproduz exatamente**, nos dois. **Linhas conferidas:** 481 = 481 · 460 = 460.

### 2.2 Registro de memoria estrategica

| Artefato | ID | Versao | **H-A** | **H-N** | **H-P** | Linhas |
|---|---|---|---|---|---|---|
| Contexto do Soberano | **`MEM-EST-0001`** | **1.0.0** | `a3e382cb4a3c20a3156d08047b85dacb4c790d1a7ce003c869d17e879d1fde9f` | `a1e3e81d0e8df17586761c1137db4df831de792ea2353c456762b497ff0b1984` | `7deb5f6d15140e75ecc1453e94d3e4724056568637ccbfe38def3b5bb6304c0d` | **282** |

> **Limite declarado, e nao omitido (PI-10).** **A Missao 1.5 nao registrou hash de
> `MEM-EST-0001`.** Este e o **primeiro** vinculo ID × versao × hash deste registro. Portanto
> **H-A nao pode ser conferido contra um valor anterior** — ele e *medido agora*, e o que se
> comprova por outras vias e a **inexistencia de alteracao** (V3, V5 e V6 de §5). E exatamente
> o mesmo metodo que `MSG-2026-0001 §2` aplicou as duas Cartas piloto, cujo hash tambem foi
> medido no ato e nao antes.

**Reproduzir:** `sha256sum departments/exe/carta.md departments/kms/carta.md memory/estrategica/MEM-EST-0001-contexto-do-soberano.md`
*(os valores em disco apos a aplicacao dos efeitos sao os **H-P**)*.

## 3. Alcance — o que o ato alcanca e o que **nao** alcanca

Ratificacao **nao se estende por analogia** (LM-03).

| Artefato | Alcancado? | Efeito |
|---|---|---|
| **`DEP-EXE` 1.0.0** | **Sim — ratificado** | `em-revisao` → `ativo`; `ratificacao: ratificada` |
| **`DEP-KMS` 1.0.0** | **Sim — ratificado** | `em-revisao` → `ativo`; `ratificacao: ratificada` |
| **`MEM-EST-0001` 1.0.0** | **Sim — ratificado**, incluindo as **11 afirmacoes `unknown`** | `aprovado` → `ativo`; `ratificacao: ratificada` |
| **`FIT-2026-001` · `FIT-2026-002`** | **Sim — acolhidos como pareceres**, **sem** elevacao a norma | Nao sao ratificados. §4 |
| **`INC-2026-002`** | **Sim** — encerramento **autorizado** sob condicao | `contido` → `fechado`, verificado em §5.2 |
| `DEP-QAR` 1.1.0 *(emenda proposta)* | **Nao** — **excluida expressamente** | Permanece proposta; ver [REV-ESTRUTURAL-I §7](../../foundation/revisao-estrutural-01-2026-07-28.md) |
| **ADR-0012** e **RFC-0009** *(criados nesta missao)* | **Nao** — *"nao ratifica novos ADRs"*, e **nao existiam** na data do ato | `ratificacao: nao-exigida` por serem **C2/Tipo 2** — nao por suprimento do ato |
| Qualquer versao futura dos artefatos ratificados | **Nao** | Versao nova exige **ato novo** |
| As cinco Cartas restantes | **Nao** | Nao escritas |

> **O ato nao ratifica a Missao 1.7 nem a 1.8.** Ratifica **tres textos** e acolhe **dois
> pareceres**. Os artefatos avaliativos permanecem `ratificacao: nao-exigida`.

## 4. O que "acolher como parecer" significa — e o que **nao** significa

| Pergunta | Resposta | Fundamento |
|---|---|---|
| Os dois `FIT` foram **ratificados**? | **Nao.** O ato usa *acolho*, e acrescenta *"sem eleva-los a norma"* | Texto do ato; LM-03 |
| Entao qual e o estado correto de ratificacao deles? | **`nao-exigida`** — declarado por **ato explicito do Soberano**, e nao por inferencia. Corresponde a opcao **(b)** de [INC-2026-002 §7](../../governance/incidents/INC-2026-002-ratificacao-declarada-em-fitness-check.md), recomendada por DEP-GOV | Ato; FND-10 §5.4, linha *"Classe nao exige ratificacao"* |
| Isso torna verdadeira a frase *"Ratificado por (C3): SOBERANO"* de FIT-2026-001? | **Nao.** Ela continua **falsa no momento em que foi escrita**, e continua **nao corrigida** — `FIT` e **M1** e nao se edita | M1 (FND-10 §6.2); LV-04; [MEM-APR-0003](../aprendizado/MEM-APR-0003-campo-de-estado-em-artefato-imutavel.md) |
| E o `ratificacao: nao-exigida` do frontmatter de FIT-2026-002? | Ficou **coincidente com o estado correto**, mas **nao foi corretamente derivado** quando escrito. A coincidencia **nao e acerto**, e o registro do defeito e preservado | INC-2026-002 §1 |
| O ato resolve a divergencia **FND-10 §2.2 × §10.3**? | **Nao.** Ele decide **dois casos concretos**; nao emenda norma. A ambiguidade **G1/G2** permanece | INC-2026-002 §5; ato: *"sem eleva-los a norma"* |

> **Esta e a distincao que o Soberano determinou vigiar.** O que foi **resolvido** e a
> *pendencia de decisao* sobre dois artefatos. O que foi **contido, e nao resolvido** e o
> registro incorreto dentro de FIT-2026-001. O que **nao foi tocado** e a causa normativa
> G1/G2, que migra para [RFC-0009](../../rfcs/RFC-0009-integridade-e-alcance-do-ato-de-ratificacao.md)
> com dono e gatilho. **Nenhuma das tres foi renomeada para parecer fechada.**

## 5. Verificacao independente da condicao de eficacia

Executada por **DEP-QAR** e **DEP-GOV**. Nenhum dos dois produziu os artefatos: as Cartas sao
de **DEP-EXE**, o registro e de **DEP-KMS**. Executada **antes** de qualquer edicao desta missao.

| # | O que o ato exigiu | Metodo | Resultado |
|---|---|---|---|
| **V1** | Integridade do **registro** | Reproducao integral da baseline vigente `BL-2026-07-28-04` | **112 artefatos · 28.966 linhas · impressao digital `d411c1bf…d8c43`** — os tres reproduzem o valor registrado |
| **V2** | **Versao** dos objetos | Frontmatter contra o pacote de ratificacao e contra o historico de versoes | **1.0.0** nos tres. Nenhum incremento MAIOR ou MENOR desde a submissao |
| **V3** | **Hash SHA-256 integral** | `sha256sum` das duas Cartas contra [REV-INTERCLASSES §6](../../foundation/revisao-arquitetural-validacao-interclasses-2026-07-28.md) | **Reproduz exatamente** nos dois: `437f2614…42e1` e `c261ff93…1ac5` |
| **V4** | **Inexistencia de alteracao** entre revisao e ratificacao | Contagem de linhas contra o valor registrado no pacote e no [catalogo mestre §4.3.1](../../governance/artifact-registry.md) | **481 = 481** · **460 = 460** · **282 = 282** |
| **V5** | Idem, por via **temporal** | `mtime` dos tres contra o `mtime` do ultimo artefato da Missao 1.7 | `exe` **18:47:42** · `kms` **18:52:02** · `MEM-EST-0001` **16:40:59** · ultimo artefato da Missao 1.7 **19:18:01** — **os tres anteriores**; nenhum tocado apos o encerramento |
| **V6** | Idem, por via **de acervo** | Impressao digital de `BL-04`, que cobre caminho e extensao de **todos** os 112 arquivos | **Reproduz.** Nenhum arquivo acrescentado, removido, renomeado ou alterado em extensao |
| **V7** | Ausencia de **autoverificacao** | Papel de quem verifica × papel de quem produziu | **DEP-QAR** e **DEP-GOV** verificam; **DEP-EXE** e **DEP-KMS** produziram. Zero coincidencia (FT-02, RM-06b) |
| **V8** | Ausencia de **credencial** no objeto ratificado | Varredura dos tres artefatos | **0 ocorrencias** (PI-08, LV-02) |
| **V9** | As **11 afirmacoes `unknown`** permanecem `unknown` | Contagem em `MEM-EST-0001 §5` e conferencia afirmacao a afirmacao | **11 de 11** — AF-06, AF-07, AF-11, AF-21, AF-26, AF-29, AF-30, AF-31, AF-34, AF-37, AF-38. **Zero** convertidas; **zero** afirmacoes `inferred` no registro |

### 5.1 A verificacao decisiva — reconstrucao do texto ratificado

> **O limite que `MSG-2026-0001 §4.1` declarou foi eliminado nesta verificacao.** A impressao
> digital do acervo nao detecta edicao que preserve o numero de linhas. Aqui, a prova nao
> depende dela.

| Campo | Conteudo |
|---|---|
| **Metodo** | Sobre `DEP-QAR` e `DEP-ENG` — ja ratificadas e ja transicionadas em 2026-07-28 — reverteu-se **apenas** os dois campos de ciclo de vida (`status`, `ratificacao`) aos valores anteriores, e mediu-se o SHA-256 do texto reconstruido |
| **`DEP-QAR`** | Reconstruido `fa07f55f5534d8b15166e48388a27007c640dd7d7bc498f83271267cd3d1f286` × ato `fa07f55f…f286` — **identico** |
| **`DEP-ENG`** | Reconstruido `57aebf81a9864586771489ec141ac21de184674ece57acfcc7b3344b1b401a48` × ato `57aebf81…1a48` — **identico** |
| **O que isso prova** | Que a **unica** diferenca entre o texto que o Soberano ratificou em 2026-07-28 e o arquivo em disco hoje sao **exatamente os dois campos de ciclo de vida** — byte a byte, sem residuo. Nenhuma alteracao de corpo, de espaco, de pontuacao ou de qualquer outro campo ocorreu apos o ato |
| **Por que importa aqui** | O mesmo metodo passa a ser a prova permanente de que **alteracao pos-ato nao pode parecer ratificada** — instituido como regra em [ADR-0012](../../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md) |

**Condicao de eficacia: SATISFEITA.** Nove verificacoes passam, mais a reconstrucao de §5.1,
por **cinco vias independentes** — hash de arquivo, hash de conteudo normativo, contagem de
linhas, `mtime` e impressao digital de acervo.

### 5.2 Condicao propria do encerramento de `INC-2026-002`

O ato autoriza o encerramento *"apos comprovacao independente de que **todas as condicoes
pendentes foram corretamente registradas**"* — registradas, nao resolvidas.

| Condicao pendente do incidente | Onde esta registrada apos esta missao | Correta? |
|---|---|---|
| **P1** — decidir sobre a ratificacao dos dois `FIT` | **Decidida pelo ato**; estado corrente projetado por [`governance/fitness/README.md`](../../governance/fitness/README.md), fonte canonica **§4 desta Diretiva** | **Sim** |
| **G1/G2** — ambiguidade FND-10 §2.2 × §10.3 *(causa propria, nao corrigida)* | Migrada para [RFC-0009](../../rfcs/RFC-0009-integridade-e-alcance-do-ato-de-ratificacao.md), **aberta**, dono **DEP-GOV**, com prazo e gatilho | **Sim** |
| **Registro incorreto em FIT-2026-001** *(nao corrigivel — M1)* | Contido permanentemente: projecao em `governance/fitness/README.md` e §4 desta Diretiva | **Sim** |
| Aprendizado | [MEM-APR-0003](../aprendizado/MEM-APR-0003-campo-de-estado-em-artefato-imutavel.md), ja existente | **Sim** |

**Comprovacao: SATISFEITA.** O encerramento e aplicado em §6, E6.

## 6. Efeitos aplicados

| # | Efeito | Onde | Operacao |
|---|---|---|---|
| **E1** | `DEP-EXE`: `status` `em-revisao` → **`ativo`**; `ratificacao` `pendente` → **`ratificada`** | [`departments/exe/carta.md`](../../departments/exe/carta.md) | **O4** (FND-10 §5.2) |
| **E2** | `DEP-KMS`: idem | [`departments/kms/carta.md`](../../departments/kms/carta.md) | **O4** |
| **E3** | `MEM-EST-0001`: `status` `aprovado` → **`ativo`**; `ratificacao` `pendente` → **`ratificada`** | [`memory/estrategica/MEM-EST-0001-…`](../estrategica/MEM-EST-0001-contexto-do-soberano.md) | **O4** |
| **E4** | Estado de ratificacao de `FIT-2026-001` e `FIT-2026-002` passa a **`nao-exigida` por ato**; **nenhum dos dois arquivos e editado** | Projecao em [`governance/fitness/README.md`](../../governance/fitness/README.md) | Projecao (PJ-02) |
| **E5** | Linhas de rastreabilidade e classificacao atualizadas | [catalogo mestre §4.3.1, §4.7 e §6](../../governance/artifact-registry.md) | Projecao (PJ-02) |
| **E6** | `INC-2026-002`: `situacao` `contido` → **`fechado`** | [`governance/incidents/INC-2026-002-…`](../../governance/incidents/INC-2026-002-ratificacao-declarada-em-fitness-check.md) §11 | Fechamento (FND-04 §10) |
| **E7** | Ressalvas **R4 de FIT-2026-004** e **R5 de FIT-2026-005** reconciliadas | [REV-ESTRUTURAL-I §5](../../foundation/revisao-estrutural-01-2026-07-28.md) | Reconciliacao |
| **E8** | Primeira Revisao Estrutural **executada** | [REV-ESTRUTURAL-I](../../foundation/revisao-estrutural-01-2026-07-28.md) e [FIT-2026-007](../../governance/fitness/FIT-2026-007-revisao-estrutural-i.md) | Rito de FND-02 §9.4 |

### 6.1 O efeito duravel foi promovido — por isso o `ttl` desta Diretiva nao ameaca nada

| Fato | Instrumento proprio que passa a guarda-lo | Fonte da regra |
|---|---|---|
| **Estado de ratificacao** de cada artefato | O campo `ratificacao` do proprio frontmatter | FND-10 §5.4 |
| **Vigencia** de cada artefato | O campo `status` do proprio artefato | FND-10 §5.2, O4 |
| **Vinculo ID × versao × H-A/H-N/H-P** | §2 desta Diretiva, referenciada pelo [catalogo mestre §10](../../governance/artifact-registry.md) | FND-10 §10.4; ADR-0012 |
| **Fechamento de `INC-2026-002`** | O campo `situacao` do proprio incidente | FND-04 §10 |

### 6.2 Diff exato aplicado, e os hashes resultantes

**Nenhuma linha de corpo foi alterada em nenhum dos tres artefatos.**

| Artefato | Campo | Antes | Depois | Linhas antes | **Linhas depois** |
|---|---|---|---|---|---|
| `DEP-EXE` | `status` · `ratificacao` | `em-revisao` · `pendente` | **`ativo`** · **`ratificada`** | 481 | **481** |
| `DEP-KMS` | `status` · `ratificacao` | `em-revisao` · `pendente` | **`ativo`** · **`ratificada`** | 460 | **460** |
| `MEM-EST-0001` | `status` · `ratificacao` | `aprovado` · `pendente` | **`ativo`** · **`ratificada`** | 282 | **282** |

> **Contagem identica antes e depois nos tres.** E a prova de que a transicao nao tocou o
> corpo. **H-N e invariante** nos tres — e ele, e nao H-A, que mede o que o ato vinculou
> (ADR-0012, IR-02).

> **Por que a versao permanece 1.0.0 nos tres.** Transicao de estado **nao e emenda**
> ([ADR-0009](../../decisions/ADR-0009-o-que-conta-como-emenda-de-artefato.md), AC-08).
> Incrementar a versao criaria uma versao **nao ratificada** a partir de um ato que ratificou
> a 1.0.0 — o oposto do que o ato determina. Pela mesma razao **nenhuma linha e acrescentada
> ao Historico de versoes** dos tres.

## 7. O que deliberadamente **nao** foi feito

| Nao feito | Norma que o impede | Consequencia assumida |
|---|---|---|
| Editar `FIT-2026-001` ou `FIT-2026-002` para corrigir o campo de ratificacao | **M1** (FND-10 §6.2); LV-04; PJ-04; MEM-APR-0003 | FIT-2026-001 continua afirmando ato inexistente **no seu proprio texto**. O estado corrente vive aqui e no indice de aptidao; o custo e um salto de referencia |
| Editar a nota *"Estado `aprovado`, nao `ativo`"* no corpo de `MEM-EST-0001` | Alterar corpo e **emenda** (ADR-0009) e produziria versao **1.1.0 nao ratificada** | O corpo do registro contradiz o proprio frontmatter ate a proxima emenda. **Declarado como achado RE-02**, com dono e gatilho — nao omitido |
| Editar `MSG-2026-0001` para acrescentar este ato | §2 e §5 daquela Diretiva sao fonte canonica de **outro** ato | Dois atos, duas fontes canonicas |
| Aplicar a emenda **1.1.0** de `DEP-QAR` | Exclusao **expressa** no ato: *"nao aprova futura emenda de DEP-QAR"* | O defeito **IC-5** permanece vivo e declarado. Pacote de ratificacao pronto em REV-ESTRUTURAL-I §7 |
| Emendar **FND-10 §10.3** para generalizar o acolhimento | O ato decide **dois casos**, nao a norma (*"sem eleva-los a norma"*) | G1/G2 permanece aberta, em **RFC-0009** |
| Emendar **FND-01 §7.3** para resolver **IC-2** | Emenda a Constituicao e **C3** e exige ratificacao do Soberano, que este ato **nao** concede | IC-2 **formalmente adiado**, com contencao em ADR-0012 §5.4 |
| Reproduzir os hashes em indices | CM-09, PJ-01 | Indices referenciam **esta secao** |

## 8. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Contrato que exigia o ato sobre as Cartas | [ADR-0011 §5.3, **DC-09**](../../decisions/ADR-0011-contrato-de-carta-de-departamento.md) |
| Contrato que exigia o ato sobre o registro | [ADR-0010 §5.8, **CT-28**](../../decisions/ADR-0010-contrato-de-conhecimento-do-soberano.md) |
| Pendencias que o ato responde | **P1, P2, P3 e P4** de [FIT-2026-006 §Pendencias](../../governance/fitness/FIT-2026-006-validacao-interclasses.md) |
| Ressalvas que o ato desbloqueia | **R4** de FIT-2026-004 · **R5** de FIT-2026-005 |
| Pacote de ratificacao consumido | [REV-INTERCLASSES §6](../../foundation/revisao-arquitetural-validacao-interclasses-2026-07-28.md) |
| Precedente de forma | [MSG-2026-0001](MSG-2026-0001-ato-soberano-ratificacao-cartas-piloto.md) — **uma** fonte canonica, tudo o mais referencia |
| Baseline sobre a qual a integridade foi conferida | **`BL-2026-07-28-04`**, preservada e **nao editada** (BL-02) |
| Regra de integridade instituida a partir deste ato | [ADR-0012](../../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md) |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-GOV *(registro)* · SOBERANO *(emissao)* | Registro canonico do segundo ato soberano de 2026-07-28: ratificacao de `DEP-EXE`, `DEP-KMS` e `MEM-EST-0001`, acolhimento de `FIT-2026-001` e `FIT-2026-002` como pareceres, autorizacao de encerramento de `INC-2026-002` e determinacao da Primeira Revisao Estrutural. Vinculo ID × versao × **tres hashes**; verificacao da condicao de eficacia por **cinco vias independentes**, incluindo a **reconstrucao do texto ratificado**; designacao imprecisa do pacote registrada e resolvida sem alterar o ato. |
