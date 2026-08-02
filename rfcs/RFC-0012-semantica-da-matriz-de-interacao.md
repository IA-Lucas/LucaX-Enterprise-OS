---
id: RFC-0012-semantica-da-matriz-de-interacao
titulo: Semantica da matriz de interacao de FND-02 §4 e alcance do veto da Guarda
tipo: rfc
versao: 1.0.0
status: aprovado
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-GOV
criado_em: 2026-07-29
atualizado_em: 2026-07-29
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0008, ADR-0011, ADR-0012]
substitui: []
substituido_por: null
resumo: Determina por evidencia o sujeito, o objeto, a direcao, o significado de cada codigo, a precedencia e o efeito da matriz de FND-02 §4, testa as 81 celulas e propoe a emenda C3 que fecha o achado RD-02.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# RFC-0012: A semantica da matriz de FND-02 §4, e o alcance do veto da Guarda

## Proposito
Levar **RD-02** da pergunta ao texto. O achado esta aberto ha dois ciclos, e **e o unico que
toca autoridade** — a condicao nomeada de `GO-CONDITIONAL` em
[FIT-2026-010](../governance/fitness/FIT-2026-010-aplicacao-do-ato-soberano.md), R4.

Esta RFC **nao decide**. Determina por evidencia o que a matriz significa, mede as **81**
celulas contra as fontes e entrega o texto que o rito **C3** exige.

## Escopo
| Item | Definicao |
|---|---|
| Inclui | A semantica de **FND-02 §4** — sujeito, objeto, direcao, codigos, precedencia e efeito · o teste das **81** celulas · o alcance do veto da Guarda · o texto proposto |
| **Nao** inclui | **Quem** veta *(FND-02 §2.1 e §3 — nao alterados)* · a matriz de autoridade **por entidade** *(FND-09 §8.2 — objeto separado de [RFC-0013](RFC-0013-harmonizacao-do-regime-do-parecer.md))* · qualquer Carta de Departamento *(ratificadas; §7)* · Spec, agente, skill, workflow, produto, codigo ou infraestrutura, **nenhum criado** |
| Metodo | Toda contagem foi **executada por ferramenta** sobre a fonte nesta missao, com a transcricao da matriz **extraida do arquivo**, nao digitada. Nenhum numero herdado sem reconferencia (CE-04, LV-12) |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| Propoe | **DEP-GOV** | Dono do achado RD-02; guardiao normativo |
| Revisor independente | **DEP-QAR** | RM-06b — DEP-GOV nao revisa o proprio produto |
| Areas afetadas | **as nove** | FND-09 §8.2, linha `RFC`: revisam as areas afetadas |
| Decide | **SOBERANO** | **C3.** Indelegavel (PI-01). **Nao ocorreu** |

---

## 1. O achado, como ele estava escrito

> **RD-02** — *"Os campos `GOV→KMS` e `QAR→KMS` de FND-02 §4 declaram **`E`**; a leitura
> obrigatoria da mesma tabela declara que a Guarda **veta Linha e Plataforma**. As Cartas
> resolvem de **tres** formas distintas."*
> — [PT-2026-001 §10](../governance/relatorio-transicao-2026-07-29-departamentos.md)

**O achado estava certo e era menor do que o problema.** A medicao desta RFC mostra que a
lacuna nao e de **duas** celulas, e sim de **quatro** — e que a causa nao e um erro de
preenchimento, e sim um **defeito de instrumento**.

## 2. Problema / Pergunta de decisao

**A matriz de FND-02 §4 nao consegue expressar a autoridade que o proprio FND-02 §3 constitui.**

| # | Pergunta que a fonte hoje **nao** responde |
|---|---|
| **P1** | A celula `(X, Y)` afirma algo sobre a celula `(Y, X)`? |
| **P2** | Uma celula pode declarar **mais de um** ato? |
| **P3** | O que prevalece quando a **celula** e a **leitura obrigatoria** discordam? |
| **P4** | O veto da Guarda alcanca o **Comando**? E a **Plataforma**? |
| **P5** | Onde se le a autoridade que termina no **SOBERANO**, que nao figura na matriz? |
| **P6** | Como se declara **revisao independente**, que as Cartas usam e a legenda nao tem? |

## 3. A medicao — as 81 celulas

Matriz **extraida do arquivo-fonte** e testada por ferramenta. Distribuicao dos codigos:
**`—` 15 · `C` 24 · `E` 26 · `V` 10 · `A` 6 — soma 81**.

### 3.1 O que passou

| # | Teste | Resultado |
|---|---|---|
| **T1** | Diagonal e `—` em 9 de 9 | ✅ |
| **T2** | Nenhum codigo fora da legenda | ✅ |
| **T3** | **Veto indevido** — `V` emitido por nao-Guarda | ✅ **zero** |
| **T7** | *"Todos consultam GOV"* — coluna GOV | ✅ **8 de 8** |
| **T9** | **Ciclo de veto** — `V` mutuo | ✅ **zero** |
| **T10** | **Dupla aprovacao** — `A` mutuo | ✅ **zero** |
| **T11** | **Conflito de segregacao** — X aprova Y **e** Y veta X | ✅ **zero** |
| **T14** | *"PRD entrega a ENG, nunca o inverso"* — `PRD→ENG` = `E`, `ENG→PRD` = `C` | ✅ |
| **T15** | *"GRW nao instrui ENG"* — `—` nos dois sentidos | ✅ |

### 3.2 O que falhou

| # | Teste | Resultado | Celulas |
|---|---|---|---|
| **T4** | Guarda veta **Linha e Plataforma** *(leitura obrigatoria 3)* | ❌ | `GOV→KMS` e `QAR→KMS` declaram **`E`** — **2** |
| **T5** | Guarda × **Comando** | ❌ **autoridade orfa** | `GOV→EXE` e `QAR→EXE` declaram **`E`**; **nenhuma celula carrega o veto que `DEP-EXE §6.3` declara sofrer** — **2** |
| **T6** | *"Todos entregam a KMS"* *(leitura obrigatoria 1)* | ❌ | `EXE→KMS` declara **`A`**, nao `E` — **1** |
| **T8** | Simetria de `—` sob a redacao *"sem interacao estrutural direta"* | ❌ | `TLS→PRD` e `TLS→GRW` sao `—` enquanto `PRD→TLS` e `GRW→TLS` sao `C` — **2** |
| **T16** | Cardinalidade — relacoes que exigem **dois** codigos | ❌ | **9** declaracoes compostas em **7 das 9 Cartas**, que a celula unica nao comporta |
| **T17** | Cobertura da legenda | ❌ | as Cartas usam **`revisao independente`**, codigo que a legenda **nao tem** — **2** celulas |

### 3.3 A evidencia que decide P4 — **14 afirmacoes, zero excecoes**

Varredura da coluna *"O que trafega"* de **§6.3 das nove Cartas**:

| Quem declara | Quantas afirmacoes | Conteudo |
|---|---|---|
| **DEP-EXE · DEP-PRD · DEP-ENG · DEP-OPS · DEP-GRW · DEP-KMS · DEP-TLS** | **14** — duas por Carta | *"DEP-GOV veta \<eu\>"* e *"DEP-QAR veta \<eu\>"* |
| Departamentos nao-Guarda que **nao** declaram ser vetados | **0 de 7** | — |

> **Os sete departamentos nao-Guarda declaram-se vetados pelas duas Guardas, sem uma unica
> excecao — e a matriz carrega esse veto em 10 celulas, nao em 14.** As **quatro** que faltam
> sao exatamente `GOV→EXE`, `QAR→EXE`, `GOV→KMS` e `QAR→KMS`.

### 3.4 A causa raiz

> **O veto da Guarda incide sobre o OBJETO, nao sobre a CLASSE de quem o produziu.**
>
> `FND-02 §3` define o veto de **DEP-GOV** sobre *"qualquer componente sem Carta, sem
> rastreabilidade ou em violacao de norma"*, e o de **DEP-QAR** sobre *"entrega que nao atende
> o DoD ou apresenta risco nao mitigado"*. **Nenhuma das duas definicoes menciona a classe do
> produtor.** Uma matriz departamento × departamento so consegue representar autoridade
> **objetal** enumerando todos os produtores — e ela enumerou **5 de 7**.
>
> **Isto nao e erro de preenchimento: e o instrumento medindo o que nao sabe medir.** Por isso
> a correcao nao pode ser trocar duas celulas.

## 4. Determinacao da semantica — por evidencia

| # | Pergunta | **Determinacao** | Evidencia |
|---|---|---|---|
| **P1** | Direcao | **Direcional.** A celula `(X, Y)` **nada afirma** sobre `(Y, X)` | O cabecalho e `De \ Para`; os quatro codigos ativos sao atos de X sobre Y. **`TLS→ENG` = `E` e `ENG→TLS` = `C`** ja registram os dois sentidos separadamente: se a leitura fosse relacional, uma das duas seria redundante |
| **P2** | Cardinalidade | **Multivalorada.** Uma celula admite **mais de um** codigo | **9** declaracoes compostas em **7 Cartas em vigor** — `DEP-GOV §6.3` escreve literalmente *"entrega e veto"* |
| **P3** | Precedencia | **A celula e a fonte; a leitura obrigatoria e projecao dela** | ADR-0008, **PJ-03**: projecao se corrige na vista, nunca a fonte pela vista. **Mesmo desenho que FND-09 §8.2 ja declara** sobre si: *"conflito ... resolve-se a favor do documento de origem"* |
| **P4** | Alcance do veto | **Alcanca as quatro classes**, o Comando inclusive; **nenhum departamento veta a Guarda** | §3.3 *(14 de 14)* · FND-02 §3 *(objeto, nao classe)* · §6 *(“Departamento discorda de veto da Guarda ... nao executa”, sem restricao de classe)* · §7 **N3** *(decisao vinculante)* · §3 `DEP-EXE` *(“Escala ao Soberano quando: veto de Guarda que se pretende reverter”)* · `DEP-QAR §10 I-6` *(impedido de ser instruido por **Comando**)* |
| **P5** | O SOBERANO | **Nao figura na matriz.** Le-se em FND-01 §7.3 e FND-09 §8.2 | A matriz tem **9** linhas e **9** colunas, todas departamentais. **`EXE`, `GOV` e `QAR` nao tem nenhum aprovador na matriz** — e a razao e que o aprovador deles esta **fora dela** |
| **P6** | `revisao independente` | **Codigo novo `R`**, bounded a relacao estrutural e permanente | `DEP-QAR §6.3` e `DEP-GOV §6.3` ja o usam; **RM-06b** e **FND-09 §8.2** ja o constituem. O mapa completo por entidade **permanece** em FND-09 §8.2 |

> **P4 nao presume veto por classe nem por posicao — e o oposto disso.** A determinacao e que
> **a classe nao e o criterio**: o criterio e o objeto. A classe explica apenas **quem** tem o
> poder *(so a Guarda, FND-02 §2.1)*, nunca **sobre quem** ele incide.

## 5. Texto proposto

**§4 passa a ter cinco subsecoes.** Diff literal integral em
[PS-2026-004 §2](../governance/pacote-soberano-2026-07-29-rd-02.md); aqui, o que muda:

| Bloco | Antes | Depois |
|---|---|---|
| **§4.1 Legenda** | 2 linhas de prosa, 5 codigos, `—` descrito como *"sem interacao estrutural direta"* | Tabela de **6** codigos com definicao operacional por codigo; `—` redefinido como *"nenhum ato direto de X sobre Y"*; direcao declarada; **celula multivalorada** autorizada |
| **§4.2 A matriz** | 81 celulas monovaloradas | **12** celulas passam a declarar a relacao completa; **69 inalteradas** |
| **§4.3 Regras de leitura** | *(inexistente)* | **MI-01 a MI-06** — precedencia, nao-concessao de autoridade, ausencia do Soberano, efeito de `—`, criterio objetal do veto, limite de `R` |
| **§4.4 Leituras obrigatorias** | 5 leituras, **2** contraditas pelas celulas | 5 leituras, **0** contraditas |
| **§4.5 Exemplos normativos** | *(inexistente)* | **5** exemplos, um por duvida de §2 |

### 5.1 As 12 celulas

| # | Celula | Antes | Depois | Por que |
|---|---|---|---|---|
| **M1** | `EXE → KMS` | `A` | **`A E`** | QG-5 alcanca o Comando; `DEP-EXE §9` declara-se **contribuinte obrigatorio** da camada APR |
| **M2** | `GOV → EXE` | `E` | **`E V`** | §3.3; FND-02 §3, §6 e §7 N3 |
| **M3** | `QAR → EXE` | `E` | **`E V`** | idem |
| **M4** | `GOV → KMS` | `E` | **`E V`** | **RD-02 literal**; `DEP-GOV §6.3` ja escreve *"entrega e veto"* |
| **M5** | `QAR → KMS` | `E` | **`E C V`** | RD-02; `DEP-QAR §5` declara **DEP-KMS como consulta obrigatoria** do veredito `FIT` |
| **M6** | `GOV → QAR` | `C` | **`C R`** | FND-09 §8.2, linha `FIT`: *"Revisa: DEP-GOV (forma)"* |
| **M7** | `QAR → GOV` | `C` | **`C R`** | RM-06b; `DEP-QAR §6.3`; `DEP-GOV §6.3` *("revisao independente recebida")* |
| **M8** | `PRD → GRW` | `E` | **`C E`** | `DEP-PRD §6.3` — *"entrega e consulta"* |
| **M9** | `OPS → ENG` | `E` | **`C E`** | `DEP-OPS §6.3` |
| **M10** | `GRW → PRD` | `C` | **`C E`** | `DEP-GRW §6.3` |
| **M11** | `KMS → QAR` | `E` | **`C E`** | `DEP-KMS §6.3` |
| **M12** | `TLS → ENG` | `E` | **`C E`** | `DEP-TLS §6.3` |

**4 celulas de autoridade *(M2 a M5)* · 2 de revisao *(M6, M7)* · 6 de interface *(M1, M8 a M12)*.**

### 5.2 Versao proposta e classe

| Campo | Valor | Justificativa |
|---|---|---|
| Versao | **FND-02 1.3.0** *(MENOR)* | Acrescimo de subsecoes e de codigo; nenhuma remocao de norma. Precedente: FND-01 1.3.0 → **1.4.0** pela emenda C3 de ADR-0014 |
| Classe | **C3** | Toca **direitos de decisao** (FND-04 §2, C3), ainda que por **declaracao** e nao por concessao — §6 |
| Tipo | **2 — reversivel** | Sem dado vivo, sem exposicao externa, sem migracao |
| Instrumento | **RFC → ADR → ratificacao do SOBERANO** | FND-04 §2, C3 |

## 6. A pergunta dificil — **isto cria autoridade?**

| Verificacao | Resposta | Evidencia |
|---|---|---|
| Algum departamento passa a **ter** veto que nao tinha? | **NAO** | `V` continua exclusivo de **GOV** e **QAR** (FND-02 §2.1). **T3 = zero** antes e depois |
| Algum departamento passa a **sofrer** veto que nao sofria? | **NAO — passa a estar escrito o que ele proprio ja declara sofrer** | As **4** celulas alcancam `DEP-EXE` e `DEP-KMS`, e as Cartas dos dois **ja declaram** o veto (§3.3) |
| Algum **titular de decisao** de FND-01 §7.3 muda? | **NAO** | Nenhuma celula de §7.3 e tocada. A materia *"Padrao de qualidade e veto de entrega"* ja e de **DEP-QAR**, com o **SOBERANO** para reverter |
| A matriz passa a **conceder** autoridade? | **NAO — MI-02 declara o contrario** | A matriz projeta FND-01 §7.3, FND-02 §2.1 e §3 e FND-09 §8.2. Celula divergente e **erro da tabela** |
| Alguma classe muda? Algum portao? Algum departamento? | **NAO** | §2.1, §6.2 de FND-01 e §3 de FND-02 intactos |

> **Entao por que C3, e nao C2?** Porque **declarar** que a Guarda veta o **Comando** e legivel
> como direito de decisao por quem le a tabela, e **FND-04 §2 classifica pela materia, nao pelo
> tamanho do efeito**. Classificar como C2 seria decidir, no rito mais barato, uma leitura que
> o Soberano ainda nao confirmou. **A duvida resolve-se para cima** (PI-01).

## 7. O que esta RFC **nao** corrige, e por que

| Item | Estado | Motivo |
|---|---|---|
| **RD-01** — `DEP-PRD §8.2` cita `—` entre PRD e TLS onde a fonte diz `C` | **Explicado, nao corrigido** | A determinacao de **P1** mostra a origem do erro: leitura **relacional** de tabela **direcional**. Carta **ratificada** — corrigir exige ato (IR-01) |
| **RD-03** — `DEP-KMS §6.3` diz *"entrega a todos"* e *"entrega a sete e consulta dois"*; a linha KMS tem **6 `E`, 2 `C`, 1 `—`** | **Confirmado por ferramenta, nao corrigido** | A **fonte esta certa** e a Carta diverge de si mesma *(7 + 2 = 9 para **8** outros departamentos)*. Corrigir a fonte para acomodar a projecao seria **PJ-03 invertido** |
| **RD-10** *(novo)* — `DEP-TLS §6.3` declara *"sem interacao estrutural direta"* com PRD e GRW e diz que o pedido chega *"por DEP-ENG ou DEP-EXE"*, enquanto `DEP-PRD §6.3` e `DEP-GRW §6.3` declaram **consulta direta** | **Aberto** | Duas Cartas **em vigor** descrevem caminhos operacionais incompativeis. **MI-04 resolve a norma**; as Cartas continuam divergindo entre si. Dono **DEP-EXE**; gatilho *"proxima emenda a `DEP-TLS`"* |
| **RD-11** *(novo)* — 4 celulas passam a declarar mais do que a Carta do proprio emissor: `EXE→KMS`, `GOV→EXE`, `QAR→EXE`, `QAR→KMS` | **Aberto** | Sao **residuos de propagacao** (CV-04) para a proxima emenda de `DEP-EXE`, `DEP-GOV` e `DEP-QAR`. Nenhum e corrigivel aqui: as tres estao **em vigor** |
| As **nove** Cartas | **Nao tocadas** | Todas `ativo` · `ratificada`. **Zero arquivos de Carta alterados por esta RFC** |

## 8. Riscos

| # | Risco | Prob. | Impacto | Mitigacao |
|---|---|---|---|---|
| **RR-1** | A celula multivalorada vira licenca para empilhar codigos sem fonte | Media | **Alto** | **MI-02** — celula sem fonte em FND-01 §7.3 / FND-02 §2.1 e §3 / FND-09 §8.2 e **erro da tabela** |
| **RR-2** | O codigo `R` duplica FND-09 §8.2 | **Media** | Medio | **MI-06** — `R` aqui e so relacao **estrutural e permanente**; o mapa por entidade **nao e reproduzido** (CM-09, PJ-01) |
| **RR-3** | Declarar veto sobre o Comando e lido como subordinacao da Linha 1 a Guarda | Baixa | **Alto** | O veto e **objetal e reversivel pelo Soberano** (LV-09). **ES-02 permanece intacta**: a Guarda continua nao sendo priorizada nem instruida por ninguem |
| **RR-4** | A emenda fecha RD-02 e deixa RD-01, RD-03, RD-10 e RD-11 abertos, dando impressao de fechamento | **Media** | Medio | §7 enumera os **quatro**, com dono e gatilho. **Fechar RD-02 nao fecha nenhum deles**, e esta escrito |

## 9. As decisoes possiveis

| # | Decisao | Estado que produz |
|---|---|---|
| **D1** | **Ratificar ADR-0016** e promulgar FND-02 **1.3.0** | RD-02 **fechado na fonte**. Condicao **(b)** de fechamento da camada passa a **cumprida sem ressalva** |
| **D2** | Ratificar **apenas** as 4 celulas de autoridade *(M2 a M5)*, sem legenda nem MI | RD-02 fechado; **T16 e T17 permanecem** — a celula segue monovalorada e a legenda sem `R`. **Nao recomendado**: repoe a causa |
| **D3** | **Devolver** | RD-02 permanece aberto e **`GO-TO-SPECS` permanece impossivel**. `DEP-EXE` e `DEP-KMS` seguem vetados por Carta e nao pela fonte |
| **D4** | **Nao decidir** | Identico a D3. **Silencio nao e autorizacao** (LM-03) |

**Recomendacao: D1.**

## 10. Manifestacoes

| Area | Manifestacao |
|---|---|
| **DEP-GOV** *(propoe)* | Favoravel. O achado e proprio e esta aberto ha dois ciclos |
| **DEP-QAR** *(revisa)* | **Revisao independente executada.** A determinacao de P4 alcanca o **proprio DEP-QAR** — 2 das 4 celulas sao dele. **Nao ha ganho de autoridade**: `QAR→EXE` e `QAR→KMS` sao veto que `DEP-EXE §6.3` e `DEP-KMS §6.3` **ja declaram sofrer**, e nenhuma celula amplia o objeto do veto |
| **DEP-EXE** *(afetado — M1, M2, M3)* | Passa a figurar como **vetavel** e como **entregador a KMS**. Ambos ja constam de `DEP-EXE §6.3` e `§9`. **Nenhuma prioridade, fila ou alocacao e tocada** |
| **DEP-KMS** *(afetado — M4, M5, M11)* | Passa a figurar como **vetavel** — o que `DEP-KMS §6.3` **ja declara** em duas linhas |
| **Demais areas** | **Sem alteracao de autoridade.** M8 a M12 registram consulta ja declarada nas proprias Cartas |

## 11. Resultado

| Campo | Conteudo |
|---|---|
| Estado | **`aprovado`** — forma validada por DEP-GOV (FND-09 §8.2, linha `RFC`) |
| Instrumento seguinte | [**ADR-0016**](../decisions/ADR-0016-semantica-da-matriz-de-interacao.md) — candidato **C3**, sem vigencia |
| Pacote de decisao | [**PS-2026-004**](../governance/pacote-soberano-2026-07-29-rd-02.md) |
| Achado que fecha, **se ratificada** | **RD-02** |
| Achados que **nao** fecha | RD-01 · RD-03 · **RD-10** · **RD-11** — §7 |
| Verificacao de aptidao | [FIT-2026-011](../governance/fitness/FIT-2026-011-fechamento-de-autoridade.md) |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-GOV | Determina por evidencia a semantica de **FND-02 §4** — direcao, cardinalidade, precedencia, alcance do veto, ausencia do Soberano e o codigo `R` —, testa as **81 celulas** por ferramenta com a matriz **extraida da fonte**, e propoe a emenda **C3** que fecha **RD-02**: legenda de **6 codigos**, celula **multivalorada**, regras **MI-01 a MI-06**, **5 exemplos normativos** e **12 celulas** corrigidas. A causa raiz declarada e que **o veto da Guarda incide sobre o objeto, nao sobre a classe** — e a matriz enumerava **5 de 7** produtores. Evidencia decisiva: **14 afirmacoes de veto em 7 Cartas, zero excecoes**. **Nenhuma autoridade criada, nenhum titular alterado, nenhuma Carta editada.** Dois achados novos — **RD-10** e **RD-11**. |
