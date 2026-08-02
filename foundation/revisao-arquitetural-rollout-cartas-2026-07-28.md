---
id: REV-ROLLOUT-2026-07-28
titulo: Revisao Arquitetural do rollout das cinco Cartas restantes e da cobertura 9/9
tipo: fitness
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-QAR
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0011, ADR-0012, ADR-0013]
substitui: []
substituido_por: null
objeto_avaliado: [DEP-GOV, DEP-TLS, DEP-PRD, DEP-OPS, DEP-GRW, DEP-QAR, MSG-2026-0003, ADR-0013, ADR-0014, RFC-0010, RFC-0011, IDX-departamentos]
classe_avaliacao: corretude
resumo: Registra a validacao independente das cinco Cartas novas em onze testes cada, a varredura do termo ratificar no acervo e os sete achados da missao.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# REV-ROLLOUT — validacao independente do rollout das cinco Cartas

## Proposito
Verificar, de forma independente e **antes** de qualquer submissao ao Soberano, se as cinco
Cartas produzidas nesta missao cumprem o contrato de
[ADR-0011](../decisions/ADR-0011-contrato-de-carta-de-departamento.md) — e registrar, em **um
unico documento**, o resultado dos onze testes aplicados a cada uma.

> **Esta revisao julga **corretude estrutural**. Nao julga aptidao evolutiva** — objeto de
> [FIT-2026-008](../governance/fitness/FIT-2026-008-rollout-das-cartas.md) — **e nao aprova
> nada**: aprovar Carta de Departamento e ato do **SOBERANO** (DC-09).

## Escopo
| Item | Definicao |
|---|---|
| Inclui | As **cinco** Cartas novas · a Carta **`DEP-QAR` 1.1.0** ratificada nesta missao · os instrumentos de rito produzidos *(`MSG-2026-0003`, `RFC-0010`, `ADR-0013`, `RFC-0011`, `ADR-0014`)* · a projecao comparativa · a varredura do termo *ratificar* |
| **Nao** inclui | **Aptidao evolutiva** *(FIT-2026-008)* · o **merito** do ato soberano · a decisao sobre as cinco Cartas *(pacote soberano)* · o **LucaX Legacy**, nao consultado (ADR-0007 §5.1) |
| Rito aplicado | **FND-04 §8** — Architecture Review. Nenhum rito novo foi desenhado |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| **Proponente das Cartas** | **DEP-EXE** | FND-09 §8.2, linha `DEP`: propoe/cria |
| **Autor desta revisao** | **DEP-GOV** | FND-04 §8; guardiao normativo |
| **Revisor independente** | **DEP-QAR** | AC-03, RM-06b — **nao produziu nenhuma das Cartas nem esta revisao** |
| **Aprova** | **DEP-QAR** | FND-09 §8.2, linha `FIT` *(classe `REV`)*: **desvio declarado — §0.1** |
| **Aprova as Cartas** | **SOBERANO** | DC-09 — **indelegavel, e nao ocorreu** |

### 0.1 Nota de conflito de interesse (PI-10)

| Campo | Conteudo |
|---|---|
| **Fato estrutural** | A matriz de FND-09 §8.2 atribui a aprovacao de `FIT`/`REV` a **DEP-EXE**, que aqui e o **proponente e autor das cinco Cartas avaliadas** — impedido por `DEP-EXE §10, I-2` |
| Desvio aplicado | Aprovacao transferida a **DEP-QAR**, que **nao produziu** nenhum objeto avaliado. Precedente: `FIT-2026-003`, `FIT-2026-006`, `FIT-2026-007` |
| **Residuo, e ele e novo** | Uma das Cartas avaliadas e **`DEP-QAR` 1.1.0**, ratificada nesta missao. **DEP-QAR aprova uma revisao cujo objeto inclui a propria Carta** |
| **Mitigacao aplicada** | A verificacao de `DEP-QAR` 1.1.0 foi executada por **DEP-GOV**, e esta secao a segrega expressamente: **§3 nao avalia `DEP-QAR`**; a Carta emendada e verificada em [MSG-2026-0003 §6](../memory/operacional/MSG-2026-0003-ato-soberano-emenda-qar-e-criterio-de-consolidacao.md), por DEP-GOV, e **nao aqui** |
| **Alternativa recusada** | Escalar a aprovacao ao **SOBERANO** — recusada por **proporcionalidade**: o objeto e `REV`, C2/Tipo 2, e o Soberano ja decide as cinco Cartas no pacote. Sobrecarregar o ato com o parecer que o instrui aproximaria instrutor e decisor |
| **Quando desaparece** | Quando existirem **agentes** *(IC-3)* e a autoria de Carta deixar de ser exclusiva de DEP-EXE *(R1 de FIT-2026-006)*. Antes disso, nao desaparece |
| Achado gerado | **RC-08** — §7 |

---

## 1. Metodo

| # | Elemento | Como foi feito |
|---|---|---|
| 1 | **Instrumento** | Verificador executado sobre as nove Cartas, conferindo os **doze blocos**, os **25 campos** de frontmatter e as regras `DC-01` a `DC-10` |
| 2 | **Validacao do instrumento** | Executado **primeiro sobre as quatro Cartas ja em vigor**, que passaram por validacao em missoes anteriores. **O instrumento acusou falha nas nove, inclusive nas quatro validadas** — e a falha era **do contador**, nao das Cartas: ele somava a propria linha de *Contagem* como se fosse indicador. **Corrigido e reexecutado** |
| 3 | **Por que isso importa** | Um instrumento que reprova o que ja passou esta errado **ou** encontrou algo novo. **Distinguir os dois casos e o trabalho** — e aqui foram os dois: o contador estava errado **e** encontrou **RC-05** e **RC-07**, reais |
| 4 | **Cobertura** | **9 de 9** Cartas verificadas; as quatro em vigor serviram de **grupo de controle** |
| 5 | **Reprodutibilidade** | Todas as contagens desta revisao sao reproduziveis por `grep`+`wc -l` sobre os arquivos, com os intervalos declarados (CE-02) |

## 2. Segregacao de papeis — proponente, autor, executor, revisor, aprovador

> **Verificacao obrigatoria (PI-05, LV-03, GV-04, FND-04 §3.1).** Nenhum papel se acumula com
> outro incompativel **na mesma mudanca**.

| Papel | Quem | Acumula com algum outro? |
|---|---|---|
| **Proponente e autor das cinco Cartas** | **DEP-EXE** | **Sim, com "executor"** — e o mesmo residuo de **R1 de FIT-2026-006**, aberto ha tres ciclos. Declarado, nao sanado |
| **Executor da producao** | **DEP-EXE** | idem |
| **Revisor independente das quatro Cartas de Linha e Plataforma** | **DEP-GOV** | **Nao** — DEP-GOV nao produziu nenhuma delas |
| **Revisor independente da Carta de `DEP-GOV`** | **DEP-QAR** | **Nao** — e o desvio previsto: DEP-GOV e **objeto**, e nao pode revisar o instrumento que define a propria autoridade (`DEP-GOV I-3`) |
| **Autor desta revisao** | **DEP-GOV** | **Nao** quanto as Cartas; **sim** quanto a `DEP-GOV`, e por isso §3 declara `DEP-QAR` como revisor daquela linha |
| **Aprovador desta revisao** | **DEP-QAR** | **Residuo declarado** — §0.1, achado **RC-08** |
| **Aprovador e ratificador das Cartas** | **SOBERANO** | **Nao** — e o unico papel do sistema que nao acumula com nenhum outro (PI-01) |

**Verificacao de autoverificacao (ADR-0005, RM-06b): 0 ocorrencias.** Nenhum departamento
verificou artefato que produziu. **Os dois residuos** — autoria unica de DEP-EXE e aprovacao
por DEP-QAR — sao de **disponibilidade estrutural**, nao de acumulo indevido, e ambos tem dono
e gatilho.

### 2.1 A revisao cruzada, Carta a Carta

| Carta | Autor | **Revisor independente** | Aprovador | Ratificador |
|---|---|---|---|---|
| `DEP-GOV` | DEP-EXE | **DEP-QAR** *(desvio: DEP-GOV e objeto)* | SOBERANO | SOBERANO |
| `DEP-TLS` | DEP-EXE | DEP-GOV | SOBERANO | SOBERANO |
| `DEP-PRD` | DEP-EXE | DEP-GOV | SOBERANO | SOBERANO |
| `DEP-OPS` | DEP-EXE | DEP-GOV | SOBERANO | SOBERANO |
| `DEP-GRW` | DEP-EXE | DEP-GOV | SOBERANO | SOBERANO |

**Nenhuma Carta tem autor igual a revisor. Nenhuma tem revisor igual a aprovador.**

## 3. Os onze testes, Carta a Carta — **registro consolidado de validacao**

> **Um unico registro, nao um arquivo por cenario** (RG-05). Legenda: ✅ **passa** ·
> ⚠️ **passa com observacao** · ❌ **falha estrutural — interrompe o lote**.

| # | Teste | O que se verifica | **GOV** | **TLS** | **PRD** | **OPS** | **GRW** |
|---|---|---|---|---|---|---|---|
| **T1** | **Mandato** | Missao e mandato em uma frase cada; o mandato declara a autoridade que a missao exige **e nada alem** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **T2** | **Autoridade** | Cada linha de B4 traz a coluna **Fonte**; nenhuma autoridade autodeclarada *(DC-04, AU-09)* | ✅ | ✅ | ✅ | ✅ | ✅ |
| **T3** | **Impedimento** | B9 presente, com materia, motivo e **substituto nomeado** *(DC-03)* | ✅ **12** | ✅ **11** | ✅ **11** | ⚠️ **11** | ✅ **13** |
| **T4** | **Custodia × exercicio** | Colunas separadas, com declaracao de projecao *(DC-02, DC-08)*; custodia confere com a fonte | ✅ | ✅ | ✅ | ✅ | ✅ |
| **T5** | **Handoff** | Handoffs emitidos e recebidos, com **criterio de aceite e de devolucao** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **T6** | **Memoria** | Papel declarado nas **cinco** camadas, e o dono declarado confere com FND-06 §2.1 | ✅ | ✅ | ✅ | ✅ | ✅ |
| **T7** | **Incidente** | O papel diante de incidente esta declarado — quem detecta, registra, conduz e fecha | ✅ | ✅ | ✅ | ✅ | ✅ |
| **T8** | **Excecao** | O tratamento de excecao formal e de urgencia esta declarado, e nao dispensa registro | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| **T9** | **Criacao de artefato** | B6 lista **apenas** tipos de FND-10 §4; nenhum tipo novo e criado *(CS-01, MT-01)* | ✅ | ✅ | ✅ | ✅ | ✅ |
| **T10** | **Escalonamento** | Gatilhos com nivel **E0–E4** de FND-05 §7.1, com bloqueio declarado | ✅ | ✅ | ✅ | ✅ | ✅ |
| **T11** | **Contexto minimo** | Pacote minimo declarado e **custo medido**, nunca estimado *(CE-01, DC-10)* | ✅ | ✅ | ✅ | ✅ | ✅ |

**Resultado: 55 testes executados · 53 ✅ · 2 ⚠️ · 0 ❌.**
**Nenhuma falha estrutural. O lote nao e interrompido.**

### 3.1 As duas observacoes, e por que nao sao falhas

| # | Observacao | Por que **passa** | Efeito |
|---|---|---|---|
| **T3 · DEP-OPS** | O impedimento **I-1** — *executar acao destrutiva sem copia verificada* — declara *"Quem me substitui: **Ninguem.** A acao **nao ocorre**"* | **DC-03 exige nomear quem substitui, e "ninguem" e uma resposta**, desde que o efeito esteja declarado. Aqui o efeito e a **nao execucao**, que e a protecao de PI-07 e LV-01 — regras que **nao admitem excecao formal** (FND-01 §8.3). Declarar um substituto seria **criar uma via de contorno** para uma linha vermelha | **Passa.** E o unico impedimento do acervo sem substituto, e a excecao esta fundamentada |
| **T8 · DEP-PRD** | A Carta trata urgencia e excecao **por remissao** *(GV-08 citado em DEP-OPS, nao em DEP-PRD)*, e nao declara linha propria de excecao formal | **Nenhuma norma exige** que a Carta declare excecao formal como bloco: `EXC` e materia de FND-01 §8.3, aprovada pelo **SOBERANO**, e nenhum departamento a concede. As oito outras Cartas tambem nao a declaram como bloco | **Passa.** Registrado como **observacao de uniformidade**, nao como defeito — e a mesma leitura vale para as nove |

### 3.2 Regras `DC` exercidas — a medicao que R1 de FIT-2026-005 exige

> A condicao de FIT-2026-005 R1 e literal: *"menos de **seis** das dez exercidas abre proposta
> de consolidacao"*.

| Regra | Exercida nesta missao? | Onde, nominalmente |
|---|---|---|
| **DC-01** — Capability e estavel; Carta nao a redefine | ✅ **Sim** | **0** Cartas de Capability alteradas nas cinco; §2 de cada uma cita apenas `CAP-` vigentes |
| **DC-02** — custodia e exercicio em colunas separadas | ✅ **Sim** | §2 das cinco; **DEP-TLS e DEP-GOV** com **uma** Capability cada, e mesmo assim as duas colunas |
| **DC-03** — impedimento com substituto nomeado | ✅ **Sim** | **58** impedimentos novos declarados nas cinco; e **DEP-OPS I-1** forcou a leitura de §3.1 |
| **DC-04** — autoridade com fonte | ✅ **Sim** | §5 das cinco; **DEP-GOV** teve de citar `IR-11` para a linha de *homologacao* |
| **DC-05** — fronteiras: entra, sai, fica fora | ✅ **Sim** | §4 e §6 das cinco; **DEP-GRW** declarou **duas** interacoes como **inexistentes por norma** |
| **DC-06** — subdivisao exige sinal observado | ✅ **Sim** | §12.1 das cinco. **DEP-GOV disparou cinco gatilhos** e a decisao foi **manter**, com custo declarado |
| **DC-07** — indicador sem valor e `definido, sem valor` | ✅ **Sim** | **41** indicadores marcados sem valor nas nove; **0** afirmacoes de desempenho sem medida |
| **DC-08** — referencia, nao reproduz | ✅ **Sim** | **5** declaracoes de projecao novas; a matriz de FND-02 §4 **nao** foi reproduzida em nenhuma |
| **DC-09** — Carta nao entra em vigor por si | ✅ **Sim** | As cinco nascem `em-revisao` · `pendente`; e `DEP-QAR` 1.1.0 so entrou em `ativo` **apos** ato |
| **DC-10** — perfil de carregamento medido | ✅ **Sim** | **15** medicoes novas, todas por `sed`+`wc -l`; o metodo **reproduziu exatamente** os valores das quatro Cartas ja em vigor |

**10 de 10 regras `DC` exercidas.** A condicao de abertura de consolidacao de **R1 de
FIT-2026-005** *(menos de seis)* **nao se verifica**.

> **O que ainda nao fecha R1.** A ressalva exige, alem da medicao, **autor distinto de
> DEP-EXE**. As cinco Cartas tem o mesmo autor das quatro anteriores. **R1 permanece aberta**,
> e a medicao acima **nao a fecha** — registra apenas que o criterio de consolidacao nao dispara.

## 4. Coerencia das nove — o que esta revisao verificou, e onde vive

> A **projecao comparativa unica** vive em [`departments/README.md`](../departments/README.md)
> e **nao e reproduzida aqui** (PJ-01, CM-09). Esta secao registra apenas o **resultado** das
> verificacoes que a projecao tornou possiveis.

| # | Verificacao | Resultado |
|---|---|---|
| 1 | **Cobertura 9/9** | ✅ **9 Cartas para 9 departamentos.** Nenhum departamento novo criado |
| 2 | **Quatro classes** | ✅ Comando **1** · Guarda **2** · Linha **4** · Plataforma **2** = **9**, identico a FND-02 §2.1 |
| 3 | **23 Capabilities** | ✅ **23 custodias**, **24** vinculos de exercicio, **0** sem custodio, **0** custodia dupla |
| 4 | **Custodios** | ✅ Cada uma das 23 tem **exatamente um**, e confere com o frontmatter da Carta de Capability (PR-1) |
| 5 | **Exercentes** | ✅ **1** exercicio sem custodia — `CAP-comunicacao` por DEP-KMS. Unico membro de OW-02 *(achado P1, ainda com 1)* |
| 6 | **Fronteiras** | ✅ **0 sobreposicoes de escopo exclusivo** entre as nove secoes 3 |
| 7 | **Interfaces** | ✅ **11 pares verificados, 11 fecham** — `departments/README §4` |
| 8 | **Dependencias** | ✅ **0** declaracoes `DEP → DEP` *(relacao nula, RM-02)*; grafo de Capabilities **sem ciclo**; **0** dependencias ascendentes |
| 9 | **Segregacao** | ✅ **92** impedimentos; **9 de 9** declaram o impedimento de aprovar o proprio produto; **0 violacoes de PI-05** |
| 10 | **Portoes** | ✅ Os **7** de FND-01 §6.2 cobertos; **0** portoes novos; **0** portoes sem dono; **3** departamentos sem portao, com fundamento |
| 11 | **Camadas de memoria** | ✅ As **5** com dono, e os cinco donos **reproduzem FND-06 §2.1 exatamente** |
| 12 | **Lacunas** | ⚠️ **8 declaradas** — `departments/README §6`. **5 determinadas · 3 defeitos** *(RC-01, RC-05, RC-07)* |

## 5. Varredura do termo *ratificar* — `IR-11` exercido e medido

> Determinacao da missao: *"testar o acervo para uso ambiguo de 'ratifica' e manter contencao
> ate decisao"*. A contencao **`IR-11`** de [ADR-0012 §5.4](../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md)
> permanece **integralmente em vigor**.

| Medida | Valor | Metodo |
|---|---|---|
| Ocorrencias do radical *ratific-* no acervo | **1.210** | `grep -roE "[Rr]atific[a-z]*" --include="*.md"` |
| Artefatos que contem o radical | **101** | idem, agrupado por arquivo |
| **Artefatos que registram *"ratificado por"* nome nao-soberano** | **0** | Varredura do padrao `ratificad[oa] por <nome>` |
| Linhas de **FND-01 §7.3** com titular nao-soberano na coluna *Ratifica* | **5** | Leitura coluna a coluna |
| Linhas de **FND-09 §8.2** com titular nao-soberano na coluna *Ratifica* | **0** | Leitura coluna a coluna, **22 linhas** |
| **Ocorrencias novas de *homologacao* introduzidas nesta missao** | **3** | `DEP-GOV §5` · `DEP-PRD §5` · `DEP-OPS §5` |

### 5.1 O que a varredura estabelece

| # | Conclusao | Consequencia |
|---|---|---|
| 1 | **`IR-11` esta funcionando: zero violacoes em 1.210 ocorrencias** | A contencao **impede a propagacao** — e **nao corrige a fonte** |
| 2 | **As tres linhas do acervo em que um departamento confirma decisao usam o termo `homologacao`**, e as tres citam `IR-11` | Primeiro exercicio **positivo** da regra: antes ela so **proibia**; agora ela **nomeia** |
| 3 | **FND-09 §8.2 nunca usou o sentido ambiguo** | O acervo **ja opera** no sentido estrito; falta a Constituicao dize-lo — evidencia central de [RFC-0011](../rfcs/RFC-0011-emenda-constitucional-ratifica-homologa.md) |
| 4 | **A colisao alcanca 5 linhas, nao 4** | **IC-2 estava subcontado.** Achado **RC-03** |
| 5 | **IC-2 permanece ABERTO** | O texto da emenda existe *(RFC-0011, ADR-0014 candidato)*; falta **so o ato**. Ler o silencio do ato de 2026-07-28 como autorizacao seria **LM-03**, e o proprio ato o veda |

## 6. Reconciliacao — ressalvas e achados

> **Tres estados distinguidos:** **RESOLVIDA** — condicao satisfeita com evidencia ·
> **RECLASSIFICADA** — muda o julgamento, nao o objeto · **MANTIDA** — segue aberta, com dono,
> gatilho e custo. **Nenhuma foi fechada por reformulacao de texto.**

| Origem | Gatilho disparou? | **Estado de saida** | Evidencia |
|---|---|---|---|
| **R2 de FIT-2026-007** — criterio de consolidacao | **Sim** — PS-1 decidida | ✅ **RESOLVIDA** | O gatilho literal era *"PS-1 — decisao sobre o que fecha um horizonte"*. **O Soberano decidiu**, e o criterio esta formalizado em [ADR-0013](../decisions/ADR-0013-criterio-de-horizonte-e-consolidacao.md), `HZ-01` a `HZ-08` |
| **R4 de FIT-2026-006** — DEP-QAR retem IC-5 | **Sim** — ato soberano | ✅ **RESOLVIDA** | `DEP-QAR` **1.1.0** em vigor; **IC-5 corrigido**; `IR-09` reproduziu `H-A` exatamente |
| **R2 de FIT-2026-006** — 5 de 9 sem Carta, um deles DEP-GOV | **Sim** — as cinco escritas | ✅ **RESOLVIDA** | **9 de 9** com Carta. **DEP-GOV foi a quinta, escrita sozinha**, cumprindo a Condicao 1 |
| **R1 de FIT-2026-005** — 10 regras `DC` exercidas por construcao | **Sim** — cinco Cartas novas | 🟡 **MANTIDA** | **10 de 10 exercidas** (§3.2), acima do limiar de seis. **Nao fecha**: a ressalva exige **autor distinto de DEP-EXE**, e nao houve |
| **R1 de FIT-2026-006** — DEP-EXE autor de 4 de 4 | **Nao** | 🟡 **MANTIDA e AGRAVADA** | **DEP-EXE agora e autor de 9 de 9.** O sinal cresceu; o movimento corretivo continua exigindo **criar agente**, proibido |
| **R4 de FIT-2026-002** — reducao de contexto nao observada | **Sim** — 6a medicao | 🟡 **MANTIDA** | A medicao itemizada esta em [FIT-2026-008 §F5](../governance/fitness/FIT-2026-008-rollout-das-cartas.md). **Segunda medicao itemizada da serie**; o criterio exige **duas descidas consecutivas** |
| **R3 de FIT-2026-003** · **R2 de FIT-2026-003** | **Nao** — gatilhos sao a **2a** revisao estrutural e o 1o candidato do Legacy | 🟡 **MANTIDAS** | Gatilhos intactos |
| **R2 de FIT-2026-004** — tres abstracoes com zero membros | **Nao** — *"1o componente criado apos a vigencia"* | 🟡 **MANTIDA** | **Nenhum componente foi criado**: Carta de Departamento **nao e componente novo** — os nove existem desde ADR-0001 |
| **R3 de FIT-2026-007** — DEP-QAR revisa e aprova | **Sim** — Carta de DEP-GOV escrita | 🔁 **RECLASSIFICADA** | O gatilho era *"Carta de DEP-GOV, que deve declarar este impedimento em B9"*. **`DEP-GOV I-2` declara**. **Mas o residuo persiste** nesta propria revisao (§0.1) — muda o **registro**, nao o **fato**. Achado **RC-08** |
| **IC-4** — DEP-GOV com dois papeis criticos sem Carta | **Sim** | ✅ **FECHADO** | `DEP-GOV` escrita, com **12 impedimentos**, incluindo **I-2** *(RE-03)* e **I-7** *(RC-02)* |
| **DR-4** — `departments/` sem indice | **Sim** — a quinta Carta | ✅ **FECHADO** | [`departments/README.md`](../departments/README.md) criado, com a projecao comparativa |
| **RE-01** — designacao imprecisa de pacote | **Sim** — proximo ato soberano | ✅ **FECHADO** | O ato de 2026-07-28 identificou o objeto pelo **hash integral** — [MSG-2026-0003 §1.2](../memory/operacional/MSG-2026-0003-ato-soberano-emenda-qar-e-criterio-de-consolidacao.md) |
| **RE-06** — cobertura de EV-08 nunca testavel | **Sim** | ✅ **FECHADO** | `HZ-02` torna o horizonte **avaliavel por duas condicoes verificaveis** |
| **IC-5** — materia de I-6 de DEP-QAR nomeia so a Linha | **Sim** | ✅ **FECHADO** | Corrigido na emenda 1.1.0, e **replicado por simetria** em `DEP-GOV I-6` |
| **P7** — assimetria de custodia de DEP-GOV | **Sim** — dependia da Carta | 🔁 **RECLASSIFICADO** | A Carta o **avalia e decide manter** (§12.1), com custo declarado. **A contagem de P7 estava errada**: sao **11** responsabilidades exclusivas, nao 7 — achado **RC-04** |
| **IC-2** · **Q1** · **Q2** | **Nao** — dependem de ato | 🟠 **CONTIDOS, NAO FECHADOS** | §5. Texto pronto em RFC-0011 e ADR-0014 |
| **IC-3** · **IC-6** · **P1** · **P6** · **P8** · **C5** · **DR-8** · **RE-02** · **RE-08** | **Nao** | 🟡 **MANTIDOS** | Gatilhos intactos: agentes, 3o caso, 2o membro, 2a revisao estrutural |

**Resultado: 7 RESOLVIDAS/FECHADAS com evidencia · 2 RECLASSIFICADAS · 12+ MANTIDAS ·
0 sem destino.**

## 7. Achados novos

| # | Achado | Sev. | Dono | Gatilho |
|---|---|---|---|---|
| **RC-01** | **`DEP-QAR §13.2` declara 386 linhas; o arquivo em vigor tem 387.** A emenda 1.1.0 acrescentou uma linha e nao atualizou a propria medicao, que esta **dentro do conteudo ratificado** | Baixa | DEP-EXE | **Proxima emenda a `DEP-QAR`**. Valor correto — **387** — medido e registrado em MSG-2026-0003 §9 |
| **RC-02** | **`IR-09` atribui a execucao a DEP-QAR sem prever o caso em que o artefato ratificado e a Carta de DEP-QAR** | Media | DEP-GOV | **Declarado em `DEP-GOV I-7`** nesta missao; mitigado por conferencia independente. Fecha quando houver agentes |
| **RC-03** | **A colisao de *"ratifica"* alcanca 5 linhas de FND-01 §7.3 — quatro de `DEP-EXE` e uma de `DEP-GOV`.** IC-2 registrava **quatro** | Baixa | DEP-GOV | **Corrigido na descricao** em [RFC-0011 §3.1](../rfcs/RFC-0011-emenda-constitucional-ratifica-homologa.md). **IC-2 nao fecha por isso** |
| **RC-04** | **DEP-GOV tem 11 responsabilidades exclusivas sobre uma Capability, nao 7.** P7 contava a partir de FND-02 §3; quatro foram atribuidas por norma posterior | Baixa | DEP-GOV | **Registrado em `DEP-GOV §3`**. Nao altera P7 em substancia: **agrava-o** |
| **RC-05** | **`DEP-KMS` nao menciona *incidente* em nenhuma linha.** As outras oito declaram o proprio papel diante de incidente | **Media** | DEP-EXE | **Proxima emenda a `DEP-KMS`**. E Carta **ratificada**: corrigir altera `H-N` e exige **ato novo** |
| **RC-06** | **`DEP-QAR` declara 7 impedimentos e 11 indicadores — os menores do sistema**, contra 12 e 17 de `DEP-GOV`, do mesmo nivel e da mesma classe | Baixa | DEP-EXE | **Diferenca de maturidade do instrumento**, nao de classe: `DEP-QAR` foi a **primeira** Carta escrita. Gatilho: proxima emenda a `DEP-QAR` |
| **RC-07** | **`DEP-ENG` nao declara impedimento sobre a propria Carta.** As outras **oito** declaram | **Media** | DEP-EXE | **Proxima emenda a `DEP-ENG`**. **Efeito nulo** — a autoridade nao existe por AU-09 —, mas a declaracao que DC-03 pede falta |
| **RC-08** | **DEP-QAR aprova esta revisao, cujo objeto inclui a propria Carta 1.1.0** | **Media** | DEP-GOV | §0.1. Mitigado por segregacao: **§3 nao avalia `DEP-QAR`**, e a verificacao daquela Carta foi feita por DEP-GOV em MSG-2026-0003 §6. Fecha com **agentes** *(IC-3)* |

**Achados: 8 · corrigidos nesta missao: 0 · declarados com dono e gatilho: 8 · sem destino: 0.**

> **Cinco dos oito achados sao da mesma familia, e isso e o achado sobre os achados.** RC-01,
> RC-05, RC-06 e RC-07 so aparecem **quando as nove Cartas sao lidas juntas** — nenhum seria
> encontrado revisando uma Carta isoladamente, e nenhum foi encontrado nas missoes 1.6 a 1.8,
> que revisaram **duas e depois quatro**. **A projecao comparativa e o instrumento que os
> revelou**, e e a terceira vez que uma projecao expoe divergencia antiga
> ([MEM-APR-0004](../memory/aprendizado/MEM-APR-0004-projecao-revela-divergencia-antiga.md)).

## 8. Integridade referencial e reconciliacao catalogo-fonte

| Verificacao | Resultado |
|---|---|
| **Links relativos quebrados** | **0** — **1.267** links verificados no acervo inteiro |
| Vinculo a Capability valido (VC-01) | **24** vinculos das nove Cartas, todos a Capability `ativo` |
| Relacao fora dos pares permitidos (RM-02) | **Conforme** — `DEP → DEP` **nao** declarada em nenhuma das nove |
| Ciclo em `depende-de` | **Sem ciclo** — nenhuma Carta de Capability tocada |
| Dependencia ascendente (PD-11) | **Conforme** |
| **Autoverificacao** | **0 ocorrencias** — §2 |
| **Credencial em texto** (PI-08, LV-02) | **0 ocorrencias** |
| **Artefatos M1 editados** | **0** — nenhum `FIT`, `REV`, `ADR` aprovado, `MSG` ou baseline anterior tocado |
| **Texto ratificado alterado** | **0 alem do ato** — `DEP-QAR` mudou **exatamente** pelo diff ratificado, provado por `IR-09`; `DEP-EXE`, `DEP-KMS` e `DEP-ENG` **intactos** |
| Todo artefato novo tem entrada no catalogo (RG-02) | **Verificado em [FIT-2026-008](../governance/fitness/FIT-2026-008-rollout-das-cartas.md)** |
| Baselines `BL-01` a `BL-05` editadas? | **Nao.** `BL-05` teve a integridade **conferida antes** de qualquer edicao — **117 artefatos · 30.947 linhas · `c9a25651…6c8f`**, os tres reproduzem |
| Nova medicao recebeu identidade nova? | **Sim** — `BL-2026-07-28-06` |
| **Copia datada antes das edicoes** | **Sim** — **117** arquivos, tomados antes da primeira escrita (PI-07, AF-35) |

## 9. Veredito da revisao

| Campo | Conteudo |
|---|---|
| **Veredito** | **CONFORME, com oito achados declarados** |
| Fundamento | **55 testes executados sobre as cinco Cartas: 53 passam, 2 passam com observacao fundamentada, 0 falham.** Nenhuma falha estrutural; o lote **nao** foi interrompido. As **10** regras `DC` foram exercidas. A cobertura **9/9** esta verificada nas doze dimensoes de §4. **0** links quebrados, **0** autoverificacao, **0** artefatos M1 editados |
| **O que o veredito nao diz** | Que as Cartas estao **em vigor** — nao estao. Que o desempenho dos departamentos esta comprovado — **nao esta, e nao pode estar**: nenhuma Carta foi exercida em operacao real |
| Efeito | **Habilita a submissao ao Soberano.** Nao aprova, nao ratifica e nao antecipa (AU-06, LM-03) |
| Data | 2026-07-28 |
| Autor | **DEP-GOV** |
| Revisor independente | **DEP-QAR** |
| Aprovado por | **DEP-QAR** — desvio declarado em §0.1, achado **RC-08** |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-GOV | Validacao independente do rollout: **onze testes sobre cinco Cartas = 55 execucoes, 0 falhas estruturais**. Instrumento **validado antes** contra as quatro Cartas em vigor, e **corrigido** quando reprovou o que ja passara. **10 de 10 regras `DC` exercidas.** Varredura de **1.210** ocorrencias do termo *ratificar*: **0** violacoes de `IR-11`, **5** linhas de colisao em FND-01 §7.3. **7 ressalvas e achados fechados**, **2 reclassificados**, **8 achados novos** — cinco deles visiveis **so na leitura conjunta das nove**. |
