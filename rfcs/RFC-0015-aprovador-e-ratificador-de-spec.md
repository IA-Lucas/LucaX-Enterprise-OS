---
id: RFC-0015
titulo: Aprovador e ratificador de Spec — harmonizar FND-09 §8.2 e FND-10 §10.3 com FND-04 §2 e §6
tipo: rfc
versao: 1.0.0
status: aprovado
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-GOV
criado_em: 2026-07-29
atualizado_em: 2026-07-29
revisao_prevista: null
decisoes_relacionadas: [ADR-0019]
substitui: []
substituido_por: null
resumo: Propoe fechar RD-15 fazendo a linha SPC de FND-09 §8.2 e a linha Spec de FND-10 §10.3 remeterem a classe da mudanca em vez de fixar titular, e registrar o conflito como erro da propria tabela.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# RFC-0015: Aprovador e ratificador de uma `Spec`

## Proposito
Levar ao rito o achado **RD-15**: para Spec de classe **C2** ou **C3**, as fontes vigentes dao
**aprovadores diferentes** e **ratificadores diferentes**.

## Escopo
| Item | Definicao |
|---|---|
| Inclui | **Duas** celulas de FND-09 §8.2 *(linha `SPC`, colunas Aprova e Ratifica)*, **duas** de FND-10 §10.3 *(linha `Spec`)* e **duas** notas |
| **Nao** inclui | **RD-14**, materia separada — [RFC-0014](RFC-0014-liberacao-do-portao-qg-1.md) · o **merito** das classes de FND-04 §2, **nao reaberto** · **FND-04 §2.1** *(RD-12)* · as demais **20** linhas de FND-09 §8.2 e **24** de FND-10 §10.3 · qualquer Spec — **nenhuma criada** |
| Origem | **RD-15**, aberto por [PT-2026-002 §5](../governance/relatorio-transicao-2026-07-29-fechamento.md); ressalva **R2** de [FIT-2026-011](../governance/fitness/FIT-2026-011-fechamento-de-autoridade.md) |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| Propoe | **DEP-GOV** | FND-09 §8.2, linha `RFC` e linha `FND` |
| Revisor independente | **DEP-QAR** | RM-06b |
| **Decide** | **SOBERANO** | **C3.** Indelegavel |

---

## 1. Contexto

O mesmo teste de consumo que expos **RD-14** expos **RD-15**, e os dois sao independentes:
**RD-14 e sobre o portao; RD-15 e sobre o artefato.** Um pode ser ratificado sem o outro.

## 2. Problema — e ele e **maior do que o achado registrado**

PT-2026-002 §5 registrou RD-15 como divergencia entre **duas** fontes. **A medicao por
ferramenta encontrou tres.**

| # | Fonte vigente | O que declara sobre aprovar uma Spec |
|---|---|---|
| **F1** | **FND-09 §8.2**, linha `SPC` | *Aprova:* **`DEP-PRD (QG-1)`** · *Ratifica:* **`—`** |
| **F2** | **FND-04 §2** e §2.1/§2.2 | *Aprova:* **conforme a classe** — C0 proprietario · C1 proprietario + revisor · **C2 DEP-EXE + parecer DEP-GOV** · **C3 SOBERANO**; *Ratifica:* **SOBERANO se C3 ou Tipo 1** |
| **F3** | **FND-04 §6**, linha *Spec* | **Classe `C1`** para a criacao de uma Spec |
| **F4** | **FND-10 §10.3**, linha `Spec` *(projecao de F1)* | *Aprova:* **`DEP-PRD (QG-1)`** · *Ratifica:* **`—`** |

> ### O terceiro achado: **F3 nunca entrou na conta**
> **PT-2026-002 §4.2 mapeou a Spec por classe de efeito e nao consultou FND-04 §6**, que
> atribui a **criacao** de uma Spec a classe **C1**. Isso muda a leitura de RD-15: **F1 nao e
> arbitraria** — ela e **coerente com F3** e incoerente com **F2**. O conflito real e entre
> **classe por tipo de componente** *(F3)* e **classe por efeito** *(F2 + AL-01)*.
>
> **Registrado como achado proprio: `RD-18`**, severidade **Media**, dono **DEP-GOV**.
> **O achado registrado era menor que o defeito** — segunda ocorrencia da licao de
> FIT-2026-011, apos RD-02.

### 2.1 A segunda metade da regra de precedencia

FND-09 §8.2 declara sobre si propria: *"Conflito entre esta tabela e o documento de origem
resolve-se a favor do documento de origem, **e o conflito e registrado como erro deste
documento**."*

| Metade | Estado |
|---|---|
| **Primeira** — resolver a favor da origem | ✅ **Executavel hoje.** Prevalece FND-04 §2 |
| **Segunda** — **registrar o conflito como erro desta tabela** | ❌ **Nunca cumprida em nenhum conflito.** PT-2026-002 §4.2 a cumpriu **num relatorio**; a regra exige o registro **no proprio documento** |

**A precedencia contem o conflito. Ela nao corrige a fonte, e nao se substitui a correcao.**

## 3. O mapa completo — **C0 a C3 × Tipo 1 e 2**

Fonte: FND-04 §2, §2.1, §2.2 e §6 · FND-01 §6.2 e §7.1 · FND-09 §8.2 · FND-10 §5.2 e §10.3.
**Estado proposto** — apos RFC-0014 *(portao)* e esta RFC *(artefato)*.

| Ato | **C0 / T2** | **C1 / T2** | **C2 / T2** | **C2 / T1** | **C3 / T1 ou T2** |
|---|---|---|---|---|---|
| **Propoe** | DEP-PRD | DEP-PRD | DEP-PRD | DEP-PRD | DEP-PRD |
| **Escreve** | DEP-PRD | DEP-PRD | DEP-PRD | DEP-PRD | DEP-PRD |
| **Revisa** | DEP-ENG + DEP-QAR | DEP-ENG + DEP-QAR | DEP-ENG + DEP-QAR | DEP-ENG + DEP-QAR | DEP-ENG + DEP-QAR |
| **Libera `QG-1`** | DEP-EXE | DEP-EXE | DEP-EXE | DEP-EXE | DEP-EXE |
| **Aprova** | proprietario *(DEP-PRD)* | proprietario + revisor | **DEP-EXE** + parecer DEP-GOV | **DEP-EXE** + parecer DEP-GOV | **SOBERANO** |
| **Veta** | DEP-QAR | DEP-QAR | DEP-QAR | DEP-QAR | DEP-QAR |
| **Ratifica** | — | — | — | **SOBERANO** | **SOBERANO** |
| **Promulga** | DEP-PRD | DEP-PRD | DEP-EXE | DEP-GOV, apos o ato | DEP-GOV, apos o ato |
| **Ativa** | `status: ativo` | `status: ativo` | `status: ativo` | `status: ativo` **apos ratificacao** | idem |
| **Supera** | nova versao | Nota de Decisao | ADR que supere | ADR + ato | ADR + ato |
| **Registra** | `atualizado_em` + CORRECAO | Nota de Decisao + MEM OPR | ADR + artefatos afetados | ADR + `MSG` do ato | ADR + `MSG` do ato |

**`C1 / T1` nao existe como celula:** FND-04 §2.2 determina que **C1 Tipo 1 escala e vira C2**.

> **Nenhum nome nesta tabela e novo.** Todos vem de FND-04 §2 *(aprovador e ratificador)*,
> FND-09 §8.2 *(propoe, revisa, aposenta)*, FND-01 §6.2 *(portao)* e FND-10 §5.2 *(vigencia)*.

### 3.1 Onde a classe de uma Spec e fixada

| # | Regra proposta |
|---|---|
| **W1** | A classe de uma Spec e a do **efeito** da mudanca que ela produz (**AL-01**), nunca a do tamanho do texto |
| **W2** | **C1 e o piso**, por FND-04 §6, linha *Spec* — nenhuma Spec e menos que C1 ao ser criada |
| **W3** | Spec que **cria componente ou muda fronteira, interface ou padrao** e **C2** (FND-04 §2) |
| **W4** | Spec que toca **dado vivo ou exposicao externa** e **Tipo 1**, e exige ratificacao do Soberano em qualquer classe (FND-01 §7.1.2, **AU-05**) |
| **W5** | Spec que alterasse **direito de decisao** seria **C3** — e FND-04 §2 ja determina **SOBERANO** |
| **W6** | Na duvida entre duas classes, **prevalece a mais restritiva** (FND-01 §7.1.6) |

**W1 a W6 nao sao regras novas: sao as regras existentes, aplicadas a `SPC`.** Nenhuma delas
precisa entrar no texto emendado — a celula que **remete a classe** ja as convoca.

## 4. Texto proposto — **quatro celulas e duas notas**

### 4.1 `FND-09 §8.2` — a **fonte**

```
antes:  | SPC | DEP-PRD | DEP-ENG + DEP-QAR | DEP-PRD (QG-1) | — | DEP-PRD |
depois: | SPC | DEP-PRD | DEP-ENG + DEP-QAR | conforme classe (FND-04 §2) | SOBERANO se C3 ou Tipo 1 | DEP-PRD |
```

**A linha `ADR`, da mesma tabela, ja usa exatamente este padrao:**
`conforme classe (FND-07 §2.4)` · `SOBERANO se C3 ou Tipo 1`. **A emenda nao cria forma nova —
ela aplica a `SPC` a forma que a tabela ja usa.**

### 4.2 `FND-10 §10.3` — a **cascata**

```
antes:  | Spec | DEP-PRD (QG-1) | — | M2 | `sob-demanda` |
depois: | Spec | conforme classe | SOBERANO se C3/Tipo 1 | M2 | `sob-demanda` |
```

**A linha `ADR` de FND-10 §10.3 ja diz** `conforme classe` · `SOBERANO se C3/Tipo 1`.

### 4.3 As duas notas — texto integral em [PS-2026-008 §2.3](../governance/pacote-soberano-2026-07-29-rd-15.md)

A nota de **FND-09** cumpre a **segunda metade** da regra de precedencia: registra o conflito
**como erro da propria tabela**, no proprio documento. A de **FND-10** declara-se **cascata**.

## 5. A verificacao que importa — isto amplia titular?

| Verificacao | Resultado | Evidencia |
|---|---|---|
| **Titulares novos** | **ZERO** | `DEP-EXE`, `DEP-GOV` e `SOBERANO` ja constam de **FND-04 §2**, que a propria FND-09 §8.2 declara ser sua origem |
| **Nomes que entram na coluna *Aprova*** | **ZERO** — a celula deixa de **nomear** e passa a **remeter** | §4.1 |
| **Nomes que entram na coluna *Ratifica*** | **1 — `SOBERANO`**, e apenas **para C3 ou Tipo 1** | Ja exigido por **AU-05** e **FND-04 §2.1**, que **nao sao tocados** |
| **Titulares reduzidos** | **1 materia** — `DEP-PRD` deixa de ser aprovador **unico** de toda Spec | Passa a se-lo em **C0 e C1**, que sao a maioria |
| **`QG-1` afetado** | **Nao por esta RFC** — o parentese *"(QG-1)"* **sai** da coluna *Aprova* porque **portao nao e aprovacao**; quem libera e materia de [RFC-0014](RFC-0014-liberacao-do-portao-qg-1.md) | §4.1 |
| **Classes de FND-04 alteradas** | **ZERO** — §2, §2.1, §2.2 e §6 **intactas** | — |
| **Outras linhas das matrizes** | **20 de 21** em FND-09 · **24 de 25** em FND-10 **inalteradas** | §4 |
| **Cartas alteradas** | **ZERO** | — |
| Custo de contexto | **+11 linhas** em FND-09 e **+7** em FND-10, ambas `nucleo` | PS-2026-008 §4 |

## 6. O limite declarado — o que esta RFC **nao** resolve

| Achado | Descricao | Sev. | Dono | Gatilho |
|---|---|---|---|---|
| **RD-12** | **FND-04 §2.1 nao distingue artefato de decisao de parecer** — ja aberto por PS-2026-005 | Media | DEP-GOV | Proxima emenda a FND-04 |
| **RD-18** | **FND-04 §6 atribui classe `C1` a criacao de Spec**, e FND-04 §2 atribui classe **pelo efeito**. As duas convivem por **AL-01** e **FND-01 §7.1.6**, mas o texto **nao declara qual prevalece**. A emenda **remete a §2** e deixa §6 como **piso** — sem emendar §6 | **Media** | DEP-GOV | Proxima emenda a **FND-04** |
| **RD-19** | **PS-2026-005 e PS-2026-008 propoem versoes concorrentes de FND-09 e FND-10** — os dois pacotes partem da **mesma base vigente** e cada um reivindica `1.4.0` e `1.3.0` | **Media** | DEP-GOV | **Promulgacao do primeiro dos dois pacotes** — §7 |

> **Emendar FND-04 §2.1 ou §6 nao foi pedido, nao foi ratificado e nao sera presumido**
> (LM-03). Corrigir a projecao sem tocar a regra geradora **deixa o mecanismo vivo**, e isso
> esta escrito como achado, **nao como correcao silenciosa** — a licao que PS-2026-005 gravou.

## 7. `RD-19` — concorrencia entre pacotes, e como resolve-la

| Fato | Estado |
|---|---|
| **PS-2026-005** *(ADR-0017)* emenda FND-09 §8.2 **linha `FIT`** e FND-10 §10.3 **linha `Fitness Check`**, propondo **1.4.0** e **1.3.0** | Aguarda ato |
| **PS-2026-008** *(este)* emenda FND-09 §8.2 **linha `SPC`** e FND-10 §10.3 **linha `Spec`**, propondo **1.4.0** e **1.3.0** | Aguarda ato |
| **As celulas sao disjuntas** | ✅ **Linhas diferentes, colunas diferentes.** Nenhum byte disputado |
| **As notas ocupam locais diferentes** | ✅ PS-2026-005 insere **apos** a matriz de §8.2; PS-2026-008 insere **antes** dela |
| **Os numeros de versao colidem** | ❌ **Sim** — os dois partem da base vigente |

| # | Regra proposta |
|---|---|
| **O1** | **Versao e atribuida na promulgacao, nao na candidatura.** Dois candidatos podem propor o mesmo numero enquanto nenhum vigora |
| **O2** | **O segundo pacote a ser ratificado e reemitido rebaseado**, com novo numero de versao e **novos hashes**, antes de ser aplicado |
| **O3** | O rebase e **mecanico e sem perda**, porque as celulas e as notas sao **disjuntas** — nenhuma decisao de merito e reaberta |
| **O4** | **Ratificar os dois no mesmo ato nao dispensa O2:** o ato alcanca os dois ADR, e a **aplicacao** exige um candidato unico medido |

> **Nao ha ordem preferida.** Os dois pacotes sao independentes no merito, e **nao decidir e
> resultado valido em cada um**.

## 8. Riscos

| # | Risco | Prob. | Impacto | Mitigacao |
|---|---|---|---|---|
| **RR-1** | **Aprovador de Spec C2 vira DEP-EXE**, que tambem libera `QG-1` apos RFC-0014 | **Alta** | Medio | **Sao atos distintos e a distincao esta escrita** (FND-01 §6.2, nota de ADR-0018). Alem disso, C2 exige **parecer de DEP-GOV**, que `QG-1` nao exige — **ha contraditorio no ato de aprovacao** |
| **RR-2** | **Classificacao vira o novo ponto de ambiguidade** — quem decide se a Spec e C1 ou C2? | Media | Medio | **FND-04 §2 ja responde:** *"A classificacao e feita pelo proponente e **validada por DEP-GOV**"*. Nenhuma regra nova e necessaria |
| **RR-3** | **RD-19 nao e tratado** e um dos dois pacotes e aplicado sobre base errada | Media | **Alto** | **O1 a O4** de §7, e o pacote declara a base medida com `H-A` integral |
| **RR-4** | Ratificar **so a fonte** e deixar FND-10 divergente | Baixa | Medio | **Desaconselhado com fundamento:** FND-10 §10.3 **declara-se projecao** de FND-09 §8.2 |

## 9. As decisoes possiveis

| # | Decisao | Efeito |
|---|---|---|
| **D1** | **Aprovar e ratificar** as quatro celulas e as duas notas | **RD-15 fecha.** `B5` sai do mapa. **RD-18 e RD-19 permanecem**, declarados |
| **D2** | **Aprovar so FND-09** | **Desaconselhada:** deixa a projecao contradizendo a fonte de que ela diz derivar |
| **D3** | **Devolver** por preferir emendar **FND-04 §6** em vez de remeter a §2 | Legitimo — e o que **RD-18** nomeia. Exige RFC propria sobre FND-04 |
| **D4** | **Nao decidir** | **RD-15 permanece.** Spec **C2 e C3 seguem sem titular unico**, e a precedencia continua sendo aplicada **sem o registro que ela propria exige** |

## 10. Manifestacoes

| Area | Manifestacao |
|---|---|
| **DEP-PRD** | **Area alcancada** — deixa de ser aprovador unico de toda Spec; **permanece** aprovador em **C0 e C1**, propositor, autor e aposentador em **todas** |
| **DEP-EXE** | **Area alcancada** — passa a aprovar Spec **C2**, materia que FND-04 §2 **ja lhe atribuia** |
| **DEP-GOV** | Propoe; **valida a classificacao** (FND-04 §2) e emite **parecer** em C2; **nao aprova nem ratifica** a emenda |
| **DEP-QAR** | **Revisor da Spec e veto inalterados**; revisor independente desta RFC |
| **SOBERANO** | Passa a **ratificar** Spec **C3 ou Tipo 1** — exigencia que **AU-05 e FND-04 §2.1 ja faziam** e que a tabela negava |

## 11. Resultado

| Campo | Conteudo |
|---|---|
| Resultado | **ADR candidato emitido** — [ADR-0019](../decisions/ADR-0019-aprovador-e-ratificador-de-spec.md) |
| Classe | **C3** *(direitos de decisao)* · **Tipo 2** |
| Estado | **Candidato. Nao vigora sem ato** (FND-01 §9) |
| Pacote | [PS-2026-008](../governance/pacote-soberano-2026-07-29-rd-15.md) |
| Achado que fecha | **RD-15** · ressalva **R2** de FIT-2026-011 · bloqueio **B5** de PT-2026-002 §8 |
| Achados que **abre** | **RD-18** *(FND-04 §6 × §2)* · **RD-19** *(pacotes concorrentes)* |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-GOV | Proposta da **Missao 1.12** para fechar **RD-15**. **A medicao encontrou tres fontes onde o achado registrava duas:** **FND-04 §6** atribui classe **`C1`** a criacao de Spec e **nunca entrara na conta** — achado **RD-18**, segunda ocorrencia da licao *"o achado registrado pode ser menor que o defeito"*. Entrega o **mapa completo C0–C3 × Tipo 1/2** para **onze atos**, com **zero nomes novos**, e registra que **`C1 / T1` nao existe** porque escala para C2. Propoe **quatro celulas e duas notas**: as linhas `SPC` e `Spec` passam a **remeter a classe**, no **mesmo padrao que a linha `ADR` das duas tabelas ja usa**, e a nota de FND-09 cumpre a **segunda metade da regra de precedencia** — registrar o conflito como erro da propria tabela —, **nunca cumprida em nenhum conflito ate hoje**. Abre **RD-19**: PS-2026-005 e PS-2026-008 propoem **versoes concorrentes** de FND-09 e FND-10, com celulas **disjuntas** e numeros de versao **colidentes**, e propoe `O1` a `O4` para resolver por **rebase mecanico**. |
