---
id: ADR-0012-integridade-do-ato-de-ratificacao
titulo: Fixar que o ato de ratificacao vincula o conteudo normativo, e como se prova que ele nao foi contornado
tipo: adr
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0006, ADR-0008, ADR-0009, ADR-0011]
substitui: []
substituido_por: null
classe_mudanca: C2
tipo_decisao: 2
supera: []
superado_por: null
resumo: Fixa que o ato de ratificacao vincula o conteudo normativo do artefato, define os tres hashes que o registro canonico deve anexar e contem a colisao terminologica do verbo ratificar.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# ADR-0012: Integridade do ato de ratificacao

## Proposito
Fixar **o que** um ato de ratificacao do Soberano vincula, e **como se prova**, apos o ato,
que o artefato em vigor e exatamente o que foi ratificado.

## Escopo
| Item | Definicao |
|---|---|
| Inclui | O objeto do ato; os tres hashes do registro canonico; a lista fechada de metadados mutaveis de ciclo de vida; a contencao terminologica do verbo *ratificar* |
| **Nao** inclui | **Quem** ratifica *(PI-01, indelegavel)*; **o que** exige ratificacao por classe *(FND-04 §2.1)*; a exigencia sobre `FIT` *(escalada — §5.5)*; a emenda C3 a FND-01 §7.3 *(escalada — §5.4)* |
| Origem | [RFC-0009](../rfcs/RFC-0009-integridade-e-alcance-do-ato-de-ratificacao.md), Opcao C + contencao da Opcao D |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| Autor | **DEP-GOV** | Guardiao normativo |
| Revisor | **DEP-QAR** | AC-03; nao produziu nenhum dos artefatos em causa |
| Aprovador | **DEP-EXE** | FND-04 §2.1, linha C2 |
| Ratificador | **Nao aplicavel** | **C2/Tipo 2.** O ato de 2026-07-28 declara expressamente que *"nao ratifica novos ADRs"*; esta decisao **nao depende** dele para vigorar, e nao se apoia nele |

---

## 1. Contexto

O ato soberano de 2026-07-28 sobre `DEP-QAR` e `DEP-ENG` vinculou o hash `fa07f55f…f286`.
O arquivo em disco, apos a transicao de estado que a **propria ratificacao obriga a fazer**
(operacao **O4**, FND-10 §5.2), hasheia `c591fd62…c311b`.

`MSG-2026-0001` tratou o caso corretamente: registrou os **dois** hashes e o **diff exato**.
Fez isso **sem norma que o obrigasse**. O segundo ato soberano, de 2026-07-28, elevou a
questao a **condicao de eficacia**: exigiu *"comprovar que nenhuma alteracao ocorreu entre a
revisao e a ratificacao"* — exigencia que so e verificavel se o **objeto do ato** estiver
definido.

Diagnostico completo em [RFC-0009 §1 e §2](../rfcs/RFC-0009-integridade-e-alcance-do-ato-de-ratificacao.md).

## 2. Problema / Pergunta de decisao

**O ato de ratificacao vincula o arquivo, o conteudo normativo ou a versao — e como se prova,
depois do ato, que o artefato em vigor e o que foi ratificado?**

Vincular o **arquivo** torna a ratificacao autodestrutiva: aplicar o efeito quebra a prova.
Vincular a **versao** abre a porta: alteracao que nao incremente versao — `C0`, ajuste de
redacao — passaria por ratificada sem nunca ter sido submetida.

## 3. Criterios de decisao

| # | Criterio |
|---|---|
| K1 | A regra nao pode tornar a ratificacao autodestrutiva |
| K2 | Alteracao pos-ato **nao pode parecer ratificada** |
| K3 | Verificavel por terceiro com os instrumentos existentes (CE-02) |
| K4 | Nao altera **quem** ratifica nem **o que** exige ratificacao por classe (PI-01) |
| K5 | Preserva atos historicos **sem edita-los** (LV-04, CC-01) |
| K6 | Nao cria entidade, tipo documental, camada nem framework |

## 4. Alternativas consideradas

Analise integral em [RFC-0009 §5](../rfcs/RFC-0009-integridade-e-alcance-do-ato-de-ratificacao.md).

### Alternativa A — Vincular o arquivo integral
Recusada: **falha K1**. A operacao O4 quebra o hash em toda ratificacao valida; obrigaria a
nunca aplicar o efeito, ou a manter o artefato eternamente fora de `ativo`.

### Alternativa B — Vincular a versao
Recusada: **falha K2**. `C0` e ajuste de redacao nao incrementam versao (ADR-0009) e passariam
por ratificados.

### Alternativa C — Vincular o **conteudo normativo**, com tres hashes declarados *(escolhida)*
Satisfaz K1 a K6. Foi **testada antes de ser adotada**: a reconstrucao do texto ratificado de
`DEP-QAR` e `DEP-ENG` reproduziu os hashes do ato exatamente
([MSG-2026-0002 §5.1](../memory/operacional/MSG-2026-0002-ato-soberano-cartas-comando-plataforma-e-contexto.md)).

### Alternativa Z — Nao fazer nada
Recusada: **falha K2**. Deixa sem metodo a exigencia literal do Soberano.

## 5. Decisao

### 5.1 O ato vincula o **conteudo normativo** — regras `IR`

| # | Regra |
|---|---|
| **IR-01** | O ato de ratificacao vincula o **conteudo normativo** do artefato: todo o arquivo **exceto** os metadados mutaveis de ciclo de vida de **IR-03**. Nao vincula o arquivo integral, nem apenas a versao. |
| **IR-02** | O conteudo normativo e medido por **H-N** = `sha256` do artefato com as linhas de frontmatter de IR-03 **removidas**. **H-N e invariante sob a operacao O4** — e por isso a ratificacao pode ser aplicada sem destruir a propria prova. |
| **IR-03** | **Lista fechada** dos metadados mutaveis de ciclo de vida, excluidos de H-N: `status` · `ratificacao` · `atualizado_em` · `substituido_por` · `situacao` · `vigencia` · `maturidade` · `veredito`. **Nenhum outro campo** e excluido — `versao`, `revisao_prevista`, `resumo`, `revisor`, `aprovador` e todo o corpo **entram** em H-N. |
| **IR-04** | **Alterar a lista de IR-03 e mudanca C2 com ADR.** Lista que cresce sem rito e protecao que se dissolve sem que ninguem decida dissolve-la (risco RR-1 de RFC-0009). |
| **IR-05** | **Divergencia de H-N apos o ato e alteracao nao ratificada**, e abre **incidente de conformidade** (FND-04 §10). Nao e corrigivel por edicao: exige **ato novo** ou reversao registrada (RB-01). |
| **IR-06** | Divergencia **apenas** em campos de IR-03, com o diff registrado no ato, e **transicao de estado regular** — nunca adulteracao. |

### 5.2 O registro canonico anexa **tres** hashes

| # | Regra |
|---|---|
| **IR-07** | Todo registro canonico de ato de ratificacao anexa, ao lado de `id` e `versao`: **H-A** — `sha256` do **arquivo tal como submetido** a decisao; **H-N** — conteudo normativo (IR-02); **H-P** — `sha256` do **arquivo apos** a transicao de estado. |
| **IR-08** | O registro anexa tambem o **diff exato** entre H-A e H-P, campo a campo. Registrar so um dos hashes esconde justamente a diferenca que o ato manda vigiar. |
| **IR-09** | **Teste de reconstrucao.** Com H-A e o diff registrados, o texto ratificado deve ser **reconstruivel** a partir do arquivo corrente, e seu `sha256` deve reproduzir **H-A**. E a prova de que nenhuma alteracao alem do diff ocorreu. Executa **DEP-QAR**; falha abre incidente (IR-05). |
| **IR-10** | Quando o artefato **nao tiver H-A registrado** por ato anterior — porque o instrumento nao existia —, o registro declara que aquele e o **primeiro** vinculo e prova a inexistencia de alteracao por **outras vias independentes** (contagem de linhas registrada, `mtime`, impressao digital de acervo). **A ausencia e declarada, nunca suprida por presuncao** (PI-10, LV-12). |

### 5.3 Aplicacao imediata

| Artefato | Aplicacao |
|---|---|
| `DEP-EXE` · `DEP-KMS` · `MEM-EST-0001` | Os tres hashes registrados em [MSG-2026-0002 §2](../memory/operacional/MSG-2026-0002-ato-soberano-cartas-comando-plataforma-e-contexto.md); diff em §6.2 |
| `MEM-EST-0001` | **IR-10 aplicado e declarado:** a Missao 1.5 nao registrou hash; este e o primeiro vinculo |
| `DEP-QAR` · `DEP-ENG` | **IR-09 executado com sucesso** — reconstrucao reproduz `fa07f55f…f286` e `57aebf81…1a48`. **`MSG-2026-0001` nao e editado:** H-N e calculavel a posteriori a partir do arquivo (K5, LV-04) |

### 5.4 Contencao terminologica — **IC-2 nao fecha aqui**

| # | Regra |
|---|---|
| **IR-11** | **Nenhum artefato novo pode registrar *"ratificado por"* seguido de nome que nao seja o SOBERANO.** O termo oficial para o ato do titular de `FND-01 §7.3` que nao seja o Soberano e **homologacao**. |
| **IR-12** | IR-11 e regra de **redacao de artefato** — dominio de FND-10, classe **C2**. **Nao e emenda a FND-01**, e nao a substitui. |

> **Isto contem o efeito; nao corrige a causa.** A coluna *Ratifica* de `FND-01 §7.3` continua
> nomeando dois institutos, e corrigi-la e **C3** com ratificacao do Soberano (FND-01 §9), que
> este ADR nao tem e nao presume. **O achado IC-2 permanece ABERTO**, com dono **DEP-GOV** e
> gatilho *"proxima emenda a FND-01, ou ato do Soberano sobre Q1 de RFC-0009"*. A **Condicao 3
> do rollout** de FIT-2026-006 e satisfeita na forma *"formalmente adiado"* — **nao** na forma
> *"resolvido"*, e a diferenca esta escrita para que ninguem a leia como fechamento.

### 5.5 O que esta decisao **nao** decide

| Questao | Por que nao e decidida aqui | Onde vive |
|---|---|---|
| **`FIT` exige ratificacao do Soberano?** *(G1/G2)* | A emenda **reduz o que chega ao Soberano**; retirar materia da mesa do ratificador nao e decisao que o rito C2 deva tomar sozinho (PI-01). O ato de 2026-07-28 decidiu **dois casos** e disse *"sem eleva-los a norma"* — ler nele emenda geral seria **LM-03** | **Q2 de RFC-0009**, escalada |
| **Emenda C3 a FND-01 §7.3** | Constituicao so se emenda com ratificacao do Soberano | **Q1 de RFC-0009**, escalada |

## 6. Justificativa

| # | Fundamento |
|---|---|
| 1 | **E a unica alternativa que satisfaz K1 e K2 ao mesmo tempo.** A e B falham cada uma em um dos dois, e a falha e estrutural, nao de calibragem |
| 2 | **Formaliza pratica observada, nao antecipacao.** `MSG-2026-0001 §2` e §5.2 ja registravam dois hashes e o diff. A regra escreve o que funcionou (SE-01, FND-08 §7.1) |
| 3 | **Nasce com membros verificados.** IR-09 foi executado sobre **dois** artefatos antes de virar regra, e passou nos dois. Abstracao com menos de dois membros e suspeita (AQ-03); esta tem dois, medidos |
| 4 | **Separa C2 de C3 em vez de misturar.** O que e integridade de artefato fica aqui; o que toca Constituicao e direito de decisao fica escalado. Decidir tudo aqui seria promover hipotese a norma |
| 5 | **Fecha a porta que o proprio Soberano mandou vigiar** — *"comprovar que nenhuma alteracao ocorreu entre a revisao e a ratificacao"* — com metodo reproduzivel por terceiro |

## 7. Impacto

| Dimensao | Impacto |
|---|---|
| Documentos fundacionais | **0 emendados.** FND-10 §5.4 continua integralmente valida; este ADR acrescenta **como se registra** o ato, nao **quando** ele e exigido |
| Entidades · tipos · camadas · templates | **0** criados |
| Artefatos historicos | **0 editados.** `MSG-2026-0001`, `FIT-2026-001`, `FIT-2026-002` e as Cartas ja ratificadas permanecem intactos |
| Regras novas | **12** — `IR-01` a `IR-12` |
| Custo de contexto | **+1** artefato `missao`. Nenhum entra no nucleo obrigatorio |
| Quem passa a fazer algo novo | **DEP-QAR** executa IR-09 a cada ato de ratificacao; **DEP-GOV** registra os tres hashes |

## 8. Evidencias

| # | Evidencia | Fonte |
|---|---|---|
| E1 | Ato de 2026-07-28 vinculou `fa07f55f…f286`; arquivo em disco hasheia `c591fd62…c311b` | MSG-2026-0001 §2 e §5.2 |
| E2 | A diferenca sao exatamente dois campos de frontmatter, que a propria ratificacao obriga a mudar | FND-10 §5.2, O4 |
| E3 | **Reconstrucao do texto ratificado reproduz H-A exatamente**, em `DEP-QAR` e `DEP-ENG` | MSG-2026-0002 §5.1 |
| E4 | H-N invariante sob O4, medido nos cinco artefatos ratificados | MSG-2026-0002 §2 |
| E5 | O segundo ato soberano elevou a integridade a **condicao de eficacia** | MSG-2026-0002 §1 |
| E6 | Colisao terminologica documentada e nao resolvida ha um ciclo | IC-2, REV-INTERCLASSES §7 |
| **A1** | **Evidencia ausente, declarada:** nenhum caso real de **adulteracao** ocorreu. IR-05 nunca foi disparado, e sua eficacia e **prevista, nao observada** | PI-10 |

## 9. Riscos e mitigacao

| # | Risco | Prob. | Impacto | Mitigacao |
|---|---|---|---|---|
| RA-1 | A lista de IR-03 cresce sem rito | Media | **Alto** | **IR-04** — alterar a lista e C2 com ADR |
| RA-2 | A contencao de IR-11 vira substituta permanente da emenda C3 devida | **Media** | Medio | IC-2 permanece **aberto**, com dono e gatilho; §5.4 declara a diferenca |
| RA-3 | IR-07 a IR-09 viram burocracia | Baixa | Medio | So alcanca artefato que **exija** ratificacao — hoje `DEP` e `MEM-EST`. Nao alcanca C0/C1 |
| RA-4 | H-N calculado com filtro diferente por operadores diferentes | Media | **Alto** | IR-03 e **lista fechada e literal**; o filtro e por chave de frontmatter, sem interpretacao |

## 10. Plano de reversao

| Campo | Conteudo |
|---|---|
| Reversivel? | **Sim — Tipo 2** |
| Como | ADR que supere este. Os hashes ja registrados **permanecem validos como evidencia**; deixam apenas de ser obrigatorios |
| Custo | Baixo. Nenhum artefato precisa ser reescrito |
| O que **nao** se reverte | Os atos soberanos ja registrados. Reverter esta decisao nao desfaz ratificacao nenhuma |

## 11. Classificacao

| Campo | Valor | Justificativa |
|---|---|---|
| Classe | **C2 — estrutural** | Altera um **padrao** de registro de artefato (FND-04 §2, C2). Nao altera principio imutavel, linha vermelha, hierarquia normativa nem direito de decisao — as duas questoes que os alterariam estao **escaladas** em §5.5 |
| Tipo | **2 — reversivel** | §10 |
| Ratificacao | **Nao exigida** | C2/Tipo 2 (FND-04 §2.1). **Nao se apoia** no ato de 2026-07-28, que expressamente nao ratifica ADRs novos |
| Instrumento | **RFC → ADR** | [RFC-0009](../rfcs/RFC-0009-integridade-e-alcance-do-ato-de-ratificacao.md) |
| Fitness Check | **Obrigatorio** | [FIT-2026-007](../governance/fitness/FIT-2026-007-revisao-estrutural-i.md) |

## 12. Revisao

| Campo | Conteudo |
|---|---|
| Gatilho de revisao | **Primeiro disparo real de IR-05** *(divergencia de H-N)*, ou **terceiro ato de ratificacao** registrado sob estas regras |
| O que se mede | Se IR-09 detectou alguma alteracao que as outras vias nao detectariam; quantos campos foram acrescentados a IR-03 e por que |
| Dono | **DEP-QAR** |
| Revisao prevista | 2027-01-28 |

## 13. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Origem | [RFC-0009](../rfcs/RFC-0009-integridade-e-alcance-do-ato-de-ratificacao.md), Opcao C + contencao de D |
| Achados que trata | **IC-2** *(contido, nao fechado)* · **G1/G2** de INC-2026-002 *(migrado, nao resolvido)* |
| Achados que **nao** trata | **Q1** e **Q2** de RFC-0009 — escaladas ao Soberano |
| Aplicado primeiro em | [MSG-2026-0002 §2 e §5.1](../memory/operacional/MSG-2026-0002-ato-soberano-cartas-comando-plataforma-e-contexto.md) |
| Verificado por | [REV-ESTRUTURAL-I §2](../foundation/revisao-estrutural-01-2026-07-28.md) · [FIT-2026-007](../governance/fitness/FIT-2026-007-revisao-estrutural-i.md) |
| Condicao de rollout que satisfaz | **Condicao 3** de FIT-2026-006, na forma **"formalmente adiado"** — §5.4 |

## Checklist de validade (FND-07 §4.1)

| # | Item | Estado |
|---|---|---|
| 1 | Duas alternativas reais mais "nao fazer nada" | ✅ A, B, C, Z |
| 2 | Criterios definidos **antes** da escolha | ✅ §3, herdados de RFC-0009 §4 |
| 3 | Evidencia registrada | ✅ §8, com **A1** ausente declarada |
| 4 | Plano de reversao | ✅ §10 |
| 5 | Proponente ≠ aprovador | ✅ DEP-GOV propoe · DEP-EXE aprova |
| 6 | Revisor ≠ autor | ✅ DEP-QAR revisa |
| 7 | Classificacao justificada | ✅ §11 |
| 8 | Impacto levantado | ✅ §7 |
| 9 | Gatilho de revisao | ✅ §12 |
| 10 | Rastreabilidade | ✅ §13 |
| 11 | Nenhuma entidade ou tipo criado | ✅ §7 |
| 12 | Nenhum artefato M1 editado | ✅ §7 |
| 13 | O que **nao** se decide esta declarado | ✅ §5.5 |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-GOV | Decisao inicial: o ato de ratificacao vincula o **conteudo normativo** (`H-N`), com lista fechada de metadados mutaveis, tres hashes obrigatorios no registro canonico e **teste de reconstrucao** executado por DEP-QAR. Contem a colisao terminologica de *ratificar* sem emendar FND-01. **IC-2 permanece aberto**; **Q1 e Q2 escaladas ao Soberano**. |
