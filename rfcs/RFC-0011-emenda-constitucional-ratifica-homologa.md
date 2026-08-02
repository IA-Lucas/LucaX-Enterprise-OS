---
id: RFC-0011-emenda-constitucional-ratifica-homologa
titulo: Emenda C3 a FND-01 §7.3 para separar ratificacao de homologacao, e harmonizacao de FND-10 §10.3 quanto a Fitness Check
tipo: rfc
versao: 1.0.0
status: aprovado
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-GOV
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0006, ADR-0009, ADR-0012]
substitui: []
substituido_por: null
resumo: Leva Q1 e Q2 de RFC-0009 da pergunta ao texto: propoe a emenda C3 que separa ratificacao de homologacao em FND-01 §7.3 e a harmonizacao de FND-10 §10.3 quanto a Fitness Check.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# RFC-0011: Separar *ratificacao* de *homologacao* — a emenda que IC-2 exige

## Proposito
Levar **Q1** e **Q2** de [RFC-0009](RFC-0009-integridade-e-alcance-do-ato-de-ratificacao.md) do
estado de *pergunta escalada* ao estado de **texto pronto para decisao**: com texto atual, texto
proposto, justificativa e analise de impacto, como exige [FND-01 §9](../foundation/01-constituicao.md),
etapas 1 a 3.

> **Esta RFC nao emenda nada e nao pede que nada entre em vigor.** A etapa 4 de FND-01 §9 —
> ratificacao do Soberano — **nao ocorreu**, e o ato de 2026-07-28 declara expressamente que
> **nao ratifica futura emenda C3**. O produto desta RFC e o **pacote de decisao**, nao a emenda.

## Escopo
| Item | Definicao |
|---|---|
| Inclui | **Q1** — a colisao do verbo *ratificar* em FND-01 §7.3, com texto atual e proposto · **Q2** — a divergencia FND-10 §2.2 × §10.3 quanto a `FIT` · o mapa de impacto de ambas · a medicao do uso do termo no acervo |
| **Nao** inclui | **Vigencia.** Nenhuma linha de FND-01 ou FND-10 e alterada por esta RFC. A contencao `IR-11` permanece integralmente em vigor ate decisao |
| Instrumento | RFC de classe **C3** para Q1 *(FND-01 §9, etapa 1)*; RFC de classe **C2 escalada** para Q2 |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| Proponente | **DEP-GOV** | Guardiao da Constituicao; dono de **IC-2** e de **G1/G2** |
| Revisor independente | **DEP-QAR** | AC-03; RFC-0009 §10 registra que DEP-QAR **insistiu** em que Q1 e Q2 ficassem escaladas |
| Aprova a **forma** | **DEP-GOV** | FND-09 §8.2, linha `RFC` |
| **Decide o merito** | **SOBERANO** | FND-01 §9, etapa 4 — **indelegavel** (PI-01) |

---

## 1. Contexto — e o que mudou desde RFC-0009

**IC-2** esta aberto ha tres ciclos. `ADR-0012 §5.4` instituiu a contencao **`IR-11`** —
*nenhum artefato novo registra "ratificado por" nome que nao seja o SOBERANO; o termo oficial e
homologacao* — e declarou, no mesmo lugar, que **isso contem o efeito e nao corrige a causa**.

**O que esta RFC acrescenta a RFC-0009:** RFC-0009 formulou a pergunta. Esta traz **tres coisas
que ela nao tinha**:

| # | Novidade | Efeito |
|---|---|---|
| 1 | **O texto proposto, literal** | A etapa 1 de FND-01 §9 exige *"texto atual, texto proposto e justificativa"*. RFC-0009 tinha os dois primeiros itens de forma descritiva; aqui o diff e **aplicavel** |
| 2 | **A contagem correta da colisao** | IC-2 registra *"Ratifica: DEP-EXE em **quatro** materias"*. A varredura desta missao encontrou **cinco** linhas com titular nao-soberano — **quatro** com DEP-EXE e **uma** com **DEP-GOV**. Achado **RC-03** |
| 3 | **A medicao do risco real** | `IR-11` foi exercido: **zero** violacoes no acervo inteiro (§4). A contencao **esta funcionando** — e e exatamente por isso que ha risco de ela ser tomada por solucao (RR-3 de RFC-0009) |

## 2. Problema / Pergunta de decisao

> **Q1.** A coluna *Ratifica* de FND-01 §7.3 nomeia **dois institutos diferentes** com **um
> nome**: o ato do Soberano que da **vigencia** (LM-02, DC-09) e o ato de um departamento que
> **confirma uma decisao dentro do proprio rito**. Deve a Constituicao separa-los?
>
> **Q2.** FND-10 **§2.2** exige `ratificacao` de *"todo artefato de **decisao** C3 ou Tipo 1"*;
> FND-10 **§10.3** atribui a `Fitness Check` — que e **parecer**, nao decisao — *"Ratifica:
> SOBERANO se C3"*. Qual das duas prevalece?

## 3. Q1 — a emenda C3 a FND-01 §7.3

### 3.1 Texto atual *(FND-01 1.3.0, §7.3)*

Cabecalho: `| Materia | Decide | Consulta obrigatoria | **Ratifica** |`

As **cinco** linhas cujo titular **nao** e o Soberano — transcritas literalmente, apenas a
primeira e a ultima coluna:

| Materia | **Ratifica** *(texto atual)* |
|---|---|
| Escopo e prioridade de produto | `DEP-EXE` |
| Arquitetura tecnica | `DEP-EXE` |
| Rotina operacional e runbooks | `DEP-EXE` |
| Estrutura da memoria e taxonomia de registro | **`DEP-GOV`** |
| Adocao de ferramenta ou integracao | `DEP-EXE` |

> **A quinta linha e nova em relacao a IC-2**, que so registrava as quatro de DEP-EXE. A
> colisao alcanca **dois** departamentos, nao um — achado **RC-03**.

### 3.2 Texto proposto — **sete** alteracoes, e nada alem

| # | Local | Antes | Depois |
|---|---|---|---|
| 1 | §7.3, **cabecalho** da 4a coluna | `Ratifica` | **`Ratifica / Homologa`** |
| 2 | §7.3, linha *Escopo e prioridade de produto* | `DEP-EXE` | **`DEP-EXE` *(homologa)*** |
| 3 | §7.3, linha *Arquitetura tecnica* | `DEP-EXE` | **`DEP-EXE` *(homologa)*** |
| 4 | §7.3, linha *Rotina operacional e runbooks* | `DEP-EXE` | **`DEP-EXE` *(homologa)*** |
| 5 | §7.3, linha *Estrutura da memoria e taxonomia de registro* | `DEP-GOV` | **`DEP-GOV` *(homologa)*** |
| 6 | §7.3, linha *Adocao de ferramenta ou integracao* | `DEP-EXE` | **`DEP-EXE` *(homologa)*** |
| 7 | §7.3, **nota normativa nova** logo abaixo da tabela | — | *"**Ratificacao** e ato exclusivo do Soberano e **condicao de vigencia** do artefato (FND-10 §5.4, LM-02). **Homologacao** e o ato pelo qual o titular da materia confirma a decisao **dentro do rito**, e **nao** da vigencia a artefato que dependa de ratificacao. Onde esta coluna nomeia departamento, o instituto e **homologacao**."* |
| **8** | §11, **Glossario**, entrada nova | — | **`Homologacao`** — *"Ato pelo qual o titular de uma materia confirma a decisao dentro do rito. Nao e ratificacao: nao da vigencia a artefato que exija ato do Soberano (FND-01 §7.3; FND-10 §5.4)."* |

**Nenhuma outra linha, tabela, principio, linha vermelha ou secao e alterada.** Os titulares
**nao mudam**: quem homologa hoje continua homologando, com o mesmo alcance.

### 3.3 Versao proposta e classe

| Campo | Proposta | Fundamento e **duvida declarada** |
|---|---|---|
| Versao de FND-01 | **1.4.0** *(MENOR)* | A emenda **nao altera direito de decisao**: nenhum titular muda, nenhum alcance muda. Altera **nome de instituto** e acrescenta glossario |
| **Duvida declarada (PI-10)** | **Pode ser 2.0.0** | FND-01 §9 manda incrementar **MAIOR** para *"emenda de principio"*. §7.3 e *Direitos de decisao por materia*, e **FND-04 §2 classifica alteracao de direitos de decisao como C3**. Se o Soberano entender que **nomear corretamente o instituto altera o direito**, a versao correta e **2.0.0**. **A escolha e dele**, e esta RFC nao a antecipa (LM-03) |
| Classe | **C3** | Emenda a Constituicao (FND-01 §9; FND-04 §2). **Sem duvida quanto a classe** — apenas quanto ao incremento de versao |
| Instrumento | RFC → analise de impacto → **ADR** → **ratificacao do Soberano** | FND-01 §9 |
| ADR candidato | [ADR-0014](../decisions/ADR-0014-candidato-emenda-fnd-01-7-3-homologa.md) — **`proposto`, sem vigencia** | Etapas 1 a 3 cumpridas; etapa 4 **nao** |

## 4. A medicao — `IR-11` exercido, e o que ela mostra

Varredura do acervo inteiro, **117 artefatos**, em 2026-07-28.

| Medida | Valor | Metodo |
|---|---|---|
| Ocorrencias do radical *ratific-* no acervo | **1.210** | `grep -roE "[Rr]atific[a-z]*" --include="*.md"` |
| Artefatos que contem o radical | **101 de 117** | idem, por arquivo |
| **Artefatos que registram *"ratificado por"* nome nao-soberano** | **0** | Varredura do padrao `ratificad[oa] por <nome>` |
| Linhas de **FND-01 §7.3** com titular nao-soberano na coluna *Ratifica* | **5** | Leitura coluna a coluna |
| Linhas de **FND-09 §8.2** com titular nao-soberano na coluna *Ratifica* | **0** | Leitura coluna a coluna — **todas** dizem `SOBERANO`, `SOBERANO se …` ou `—` |
| Templates que propagam campo *"Ratificado por"* | **1** — `TPL-fitness-check`, que diz **`SOBERANO`** | `grep` nos 19 templates |

### 4.1 O que a medicao discrimina

| Achado | Leitura |
|---|---|
| **`IR-11` esta funcionando: zero violacoes em 1.210 ocorrencias** | A contencao **impede a propagacao**. Ela **nao** corrige a fonte |
| **FND-09 §8.2 ja usa o termo no sentido estrito** — so o Soberano ratifica | O Meta Model, que se declara *derivado* de FND-01 §7.3 *"sem redefini-las"*, **ja resolveu a ambiguidade na pratica** — e a resolveu no sentido que Q1 propoe. **O acervo ja escolheu; falta a Constituicao dizer** |
| **A colisao esta confinada a FND-01 §7.3** | O impacto da emenda e **local**: 5 celulas, 1 cabecalho, 1 nota, 1 glossario. **Nenhum artefato precisa ser reescrito** |
| **A colisao alcanca DEP-GOV, e IC-2 nao registrava isso** | Achado **RC-03**. Corrigir a contagem **nao** fecha IC-2 — apenas o descreve corretamente |

> **Este e o argumento mais forte a favor da emenda, e ele e empirico:** a coluna *Ratifica* de
> **FND-09 §8.2** — a projecao de FND-01 §7.3 — **nao reproduz nenhum dos cinco titulares
> departamentais**. Ou a projecao esta errada ha tres ciclos, ou a fonte usa duas acepcoes.
> **A segunda hipotese e a que todos os artefatos do acervo assumem na pratica.**

## 5. Q2 — `Fitness Check` exige ratificacao?

### 5.1 A divergencia, literal

| Fonte | Texto | Consequencia |
|---|---|---|
| **FND-10 §2.2** | `ratificacao` obrigatorio em *"Todo artefato de **decisao** C3 ou Tipo 1"* | `FIT` **nao** e artefato de decisao: e **parecer** (`classe_avaliacao`), e o veredito **nao decide** — bloqueia ou libera o encerramento |
| **FND-10 §10.3** | Linha `Fitness Check`: *"Ratifica: **SOBERANO se C3**"* | Trata a **classe do objeto avaliado** como se fosse a classe do parecer |
| **FND-09 §8.2**, linha `FIT` | *"Ratifica: SOBERANO se C3"* | **Reproduz a mesma leitura** — a divergencia esta nas **duas** projecoes, nao so em FND-10 |

**Custo ja pago:** [INC-2026-002](../governance/incidents/INC-2026-002-ratificacao-declarada-em-fitness-check.md)
nasceu exatamente daqui, e `FIT-2026-001` **continua afirmando no proprio texto** uma ratificacao
que nunca ocorreu — artefato **M1**, nao editavel.

### 5.2 Texto proposto — **duas** alteracoes

| # | Local | Antes | Depois |
|---|---|---|---|
| 1 | **FND-10 §10.3**, linha `Fitness Check`, coluna *Ratifica* | `SOBERANO se C3` | **`—`** |
| 2 | **FND-10 §10.3**, nota abaixo da matriz | — | *"**`Fitness Check` e `Revisao Arquitetural` sao pareceres, nao artefatos de decisao** (§2.2). A ratificacao incide sobre a **mudanca avaliada**, nunca sobre o parecer que a avalia. Veredito `inapto` **bloqueia** o encerramento (QG-6) sem depender de ato do Soberano."* |

**Alteracao em cascata obrigatoria (CV-04):** **FND-09 §8.2**, linha `FIT`, coluna *Ratifica*,
de `SOBERANO se C3` para `—`, pela mesma decisao. Sem isso, a divergencia apenas troca de lugar.

### 5.3 Classe de Q2, e por que ela permanece escalada

| Campo | Conteudo |
|---|---|
| Classe **formal** | **C2** — FND-10 e FND-09 ja foram emendadas por C2 *(ADR-0009 e ADR-0008)* |
| **Por que nao se decide por C2** | **A emenda reduz o que chega ao Soberano.** `ADR-0012 §5.5` ja decidiu que *"retirar materia da mesa do ratificador nao e decisao que o rito C2 deva tomar sozinho"* (PI-01), e `RFC-0009 §10` registra que **DEP-QAR insistiu** nesse ponto. **Esta RFC nao reabre decisao vigente** |
| **O que se faz, entao** | Exatamente o que o limite da autoridade permite: **produzir o texto**, medir o impacto e **entregar pronto**. A decisao continua sendo do Soberano — e agora ela custa **um sim ou um nao**, nao um trabalho |
| **Por que sem ADR candidato** | Um ADR C2 candidato sugeriria que **DEP-EXE** poderia aprova-lo, que e precisamente o que ADR-0012 §5.5 vedou. O texto de §5.2 e o objeto da decisao; o ADR nasce **depois** dela |

## 6. Impacto — Q1 e Q2

| Dimensao | **Q1** *(C3)* | **Q2** *(C2 escalada)* |
|---|---|---|
| Documentos alterados | **FND-01** §7.3 e §11 | **FND-10** §10.3 · **FND-09** §8.2 |
| Celulas / linhas alteradas | **8** | **3** |
| Principios imutaveis alterados | **0** | **0** |
| Linhas vermelhas alteradas | **0** | **0** |
| Hierarquia normativa alterada | **0** | **0** |
| **Titulares de decisao alterados** | **0** — quem homologa hoje continua homologando | **0** |
| Entidades · tipos · camadas · templates criados | **0** | **0** |
| Artefatos existentes a reescrever | **0** — `IR-11` ja impediu propagacao; **zero** artefatos registram o termo no sentido antigo | **0** — `FIT-2026-001` e **M1** e permanece contido, **nao** corrigido |
| Artefatos que passam a ficar **coerentes** | FND-09 §8.2, que ja usava o sentido estrito | `FIT-2026-002` a diante: `nao-exigida` passa a ser **derivado**, e nao coincidencia |
| Achados que fecham | **IC-2** *(causa)* · **RC-03** *(contagem)* | **G1/G2** de INC-2026-002 |
| Ressalva que fecha | **R4** de FIT-2026-007 *(as duas juntas)* | idem |
| Reversibilidade | **Tipo 2** — emenda revogatoria pelo mesmo rito; nenhum dado vivo | **Tipo 2** |

## 7. Riscos

| # | Risco | Prob. | Impacto | Mitigacao |
|---|---|---|---|---|
| RS-1 | **A contencao `IR-11` virar solucao permanente** e a emenda nunca ocorrer | **Media** | Medio | E o risco **RR-3** de RFC-0009, agora com **quarto** ciclo. Esta RFC o reduz ao minimo: o que faltava era **texto**, e ele existe |
| RS-2 | A emenda ser lida como **alteracao de direito de decisao** e exigir 2.0.0 | **Media** | Baixo | **Declarado em §3.3.** A escolha da versao e do Soberano, e nenhuma das duas altera titular |
| RS-3 | Q2 ser decidida **por analogia** ao acolhimento de 2026-07-28 | Baixa | **Alto** | O ato de 2026-07-28 disse *"sem eleva-los a norma"*; ler nele emenda geral e **LM-03**. Repetido aqui para que nao seja repetido em outro lugar |
| RS-4 | Emendar §7.3 sem emendar §10.3 e §8.2 deixar a colisao **pela metade** | Media | Medio | Q1 e Q2 sao **independentes** e podem ser decididas separadamente — §8 declara as quatro combinacoes possiveis e o estado resultante de cada uma |

## 8. As quatro decisoes possiveis, e o estado que cada uma produz

> **Q1 e Q2 sao independentes.** O Soberano pode decidir uma, outra, as duas ou nenhuma.

| Cenario | Q1 | Q2 | Estado resultante |
|---|---|---|---|
| **1** | **Aprovar** | **Aprovar** | **IC-2 fecha** · **G1/G2 fecha** · **R4 de FIT-2026-007 fecha** · `IR-11` deixa de ser contencao e vira **redundancia benigna** |
| **2** | Aprovar | Devolver | IC-2 fecha; **G1/G2 permanece**, e `FIT` continua com exigencia que §2.2 nao sustenta |
| **3** | Devolver | Aprovar | G1/G2 fecha; **IC-2 permanece contido por `IR-11`**, quinto ciclo |
| **4** | Devolver | Devolver | **Estado atual preservado.** `IR-11` continua sendo a unica protecao, e a divida permanece **declarada**, nao renomeada |

> **O cenario 4 e legitimo e nao e falha.** A contencao funciona — **zero** violacoes em 1.210
> ocorrencias. O que ele custa esta escrito: a Constituicao continua nomeando dois institutos
> com um nome, e a protecao continua dependendo de uma regra de **redacao**, que alcanca
> artefato **novo** e nao alcanca leitor de boa-fe do texto constitucional.

## 9. Manifestacoes

| Departamento | Posicao | Observacao |
|---|---|---|
| **DEP-GOV** *(proponente)* | Recomenda **aprovar Q1 e Q2** — cenario 1 | Dono de IC-2 ha tres ciclos. Registra que **produzir o texto era o que lhe cabia**, e que decidir **nao** lhe cabe |
| **DEP-QAR** *(revisor)* | **De acordo com o texto de Q1.** Quanto a **Q2**, mantem a posicao de RFC-0009 §10: **nao decidir por C2** | Verificou a varredura de §4 de forma independente; as duas contagens coincidem |
| **DEP-EXE** | **Nao se manifesta sobre o merito de Q1** | E o **titular nomeado** em quatro das cinco linhas em questao. Manifestar-se sobre o nome do proprio ato seria juiz em causa propria (PI-05, RM-06b). **Impedimento declarado, nao omitido** |
| **DEP-KMS** *(evidencia)* | Sem objecao | Forneceu a contagem por artefato |

## 10. Resultado

| Campo | Conteudo |
|---|---|
| Estado | **Aberta — escalada ao SOBERANO** |
| O que esta pronto | **Q1**: texto atual, texto proposto *(8 alteracoes)*, justificativa, impacto e [ADR-0014](../decisions/ADR-0014-candidato-emenda-fnd-01-7-3-homologa.md) **candidato, sem vigencia**. **Q2**: texto proposto *(3 alteracoes, incluindo a cascata em FND-09)* e impacto |
| O que **falta** | **Somente a etapa 4 de FND-01 §9** — decisao explicita e datada do Soberano |
| Contencao vigente ate la | **`IR-11`** de ADR-0012, integralmente. **Zero** violacoes medidas |
| Data | 2026-07-28 |
| Forma aprovada por | **DEP-GOV** *(FND-09 §8.2, linha `RFC`)*, com revisao de **DEP-QAR** |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-GOV | Proposta inicial: leva **Q1** e **Q2** de RFC-0009 de pergunta a texto. Q1 — emenda **C3** a FND-01 §7.3 e §11, **8 alteracoes**, com ADR-0014 candidato **sem vigencia**. Q2 — harmonizacao de FND-10 §10.3 com §2.2 e cascata em FND-09 §8.2, **3 alteracoes**, mantida **escalada** por PI-01. Varredura de **1.210 ocorrencias** do termo em **117** artefatos: **zero** violacoes de `IR-11`; **cinco** linhas de colisao em FND-01 §7.3 — uma a mais do que IC-2 registrava (achado **RC-03**). Quatro cenarios de decisao declarados. |
