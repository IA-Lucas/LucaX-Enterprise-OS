---
id: FIT-2026-008-rollout-das-cartas
titulo: Aptidao arquitetural do rollout das cinco Cartas e da cobertura 9/9
tipo: fitness
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-QAR
proprietario: DEP-QAR
aprovador: DEP-GOV
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0011, ADR-0012, ADR-0013]
substitui: []
substituido_por: null
objeto_avaliado: [DEP-GOV, DEP-TLS, DEP-PRD, DEP-OPS, DEP-GRW, MSG-2026-0003, RFC-0010, ADR-0013, RFC-0011, ADR-0014, IDX-departamentos, PS-2026-002]
classe_mudanca: C2
classe_avaliacao: aptidao
veredito: apto-com-ressalva
resumo: Verifica se a Missao 1.9 deixou a arquitetura mais apta a evoluir; veredito apto-com-ressalva, quatro ressalvas e a decisao de fechamento da camada.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-GOV
ratificacao: nao-exigida
---

# FIT-2026-008: Rollout das cinco Cartas e cobertura 9/9

## Proposito
Verificar se a **Missao 1.9** — ratificacao de `DEP-QAR` 1.1.0, formalizacao do criterio de
consolidacao, pacote da emenda constitucional e as **cinco** Cartas restantes — deixou a
arquitetura **mais apta a evoluir**, e decidir o **criterio de fechamento** da camada.

> **Obrigatorio por QG-6** sobre mudanca **C2** (FND-01 §6.2; FND-09 §10.2).

## Escopo
| Item | Definicao |
|---|---|
| Objeto avaliado | As **cinco** Cartas novas · `MSG-2026-0003` · `RFC-0010` + `ADR-0013` · `RFC-0011` + `ADR-0014` · `IDX-departamentos` · `PS-2026-002` |
| Estado anterior | **117 artefatos, 30.947 linhas** *(`BL-2026-07-28-05`)*; **4 de 9** Cartas; **13** ressalvas abertas; **7** vereditos consecutivos `apto-com-ressalva` |
| **Nao** inclui | **Corretude estrutural** — objeto de [REV-ROLLOUT](../../foundation/revisao-arquitetural-rollout-cartas-2026-07-28.md). O **merito** do ato soberano. As Cartas **em vigor** — nao estao |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| **Executa** | **DEP-QAR** | FT-02, CV-08 — **nao produziu nenhum dos objetos avaliados** |
| Forma | DEP-GOV | |
| Evidencia | DEP-KMS | Medicoes de acervo, de secao, de pacote e de hash |
| **Aprova** | **DEP-GOV** | **Desvio declarado.** A matriz atribui a aprovacao de `FIT` a **DEP-EXE**, impedido por ser **autor das cinco Cartas avaliadas** (`DEP-EXE §10, I-2`). Cenario **CX-3**; precedentes FIT-2026-003, FIT-2026-006, FIT-2026-007 |
| Ratifica | **Nao aplicavel** | Objeto **C2/Tipo 2** — e a questao **Q2**, escalada |

> **Residuo declarado (PI-10).** **DEP-GOV aprova este `FIT` tendo sido autor da forma de
> REV-ROLLOUT**, e **DEP-QAR o executa tendo tido a propria Carta ratificada nesta missao**. O
> objeto deste `FIT` **nao inclui `DEP-QAR` 1.1.0** nem `REV-ROLLOUT`. Registrado como ressalva
> **R3** e achado **RC-08**.

---

## Sumario

| # | Pergunta | Resposta | Sinal |
|---|---|---|---|
| F1 | Complexidade aumentou sem ganho proporcional? | **Nao** | **+4.754 linhas (15,4%)** contra **cobertura 9/9**, **8 ressalvas e achados fechados**, **1 emenda ratificada**, **1 pendencia soberana respondida** e **0** entidades, tipos, camadas ou fundacionais criados |
| F2 | Algum conceito foi duplicado? **e** a prevencao foi aplicada? | **Nao · aplicada** | **6** reproducoes barradas; **6** projecoes declaradas; **0** fundacionais emendados |
| F3 | Alguma abstracao ficou desnecessaria? | **Nao — e uma nasce com zero membros, declarada** | `DC` sai da suspeita com **10 de 10** exercidas; **`HZ` nasce com 0** |
| F4 | Continua mais simples de evoluir? | **Sim** | **Seis** perguntas antes sem resposta verificavel passam a ter uma; **nenhuma aprovacao nova** criada |
| F5 | Custo de contexto subiu ou desceu? | **DESCEU** — 18,9% contra 21,3% | **6a medicao, e a 2a itemizada.** **Primeira descida comparavel da serie** |
| F6 | Favorece reutilizacao? | **Sim** | **8 regras `HZ`** aplicaveis a toda revisao futura; **1 projecao** que revelou **4 achados** invisiveis Carta a Carta |

**Veredito:** `apto-com-ressalva` — **quatro** ressalvas, todas com dono e gatilho.
**Fechamento da camada: `READY-FOR-RATIFICATION`** (§Fechamento).

---

## F1 — A complexidade aumentou sem ganho proporcional?

| Medida | Antes | Depois | Variacao |
|---|---|---|---|
| Artefatos | 117 | **131** | **+14** |
| Linhas | 30.947 | **35.701** | **+4.754 (15,4%)** |
| Entidades declaradas · instanciadas | 21 · 10 | **21 · 10** | **0** |
| Tipos documentais · com instancia | 33 · 16 | **33 · 17** | **+1 com instancia** — `Reporte`, sem criar tipo |
| Documentos fundacionais | 10 | **10** | **0** — **e o numero mais importante desta tabela** |
| Camadas de memoria · templates · portoes · departamentos | 5 · 19 · 7 · 9 | **5 · 19 · 7 · 9** | **0** |
| **Departamentos com Carta** | **4** | **9** | **+5 — cobertura 9/9** |
| **Cartas em vigor** | 4 | **4** | **0** — as cinco dependem de ato |
| Cartas **emendadas e ratificadas** | 0 | **1** | **+1** — `DEP-QAR` 1.1.0 |
| Regras normativas novas | — | **8** *(`HZ-01` a `HZ-08`)* | **+8** |
| **Ressalvas e achados fechados** | — | **8** | R2/R4/R2 de FIT-2026-006 e 007 · IC-4 · IC-5 · DR-4 · RE-01 · RE-06 |
| Achados **novos** | — | **8** *(RC-01 a RC-08)* | **0** corrigidos; **8** com dono e gatilho |
| **Pendencias soberanas respondidas** | — | **1** | **PS-1** |
| Artefatos **M1** editados | — | **0** | Nenhum `FIT`, `REV`, `ADR` aprovado, `MSG` ou baseline anterior |
| **Documentos fundacionais emendados** | — | **0** | `HZ-07`, verificavel por `diff` |
| Cartas de Capability alteradas | — | **0** | — |
| Agentes, skills, workflows, produtos, codigo, infra, ontologia | — | **0** | Conforme determinacao |
| **Consolidacoes executadas** | 0 em 7 ciclos | **0** | **8o ciclo** — §Ressalvas R2 |
| Indices atualizados *(M3 derivado)* | — | **9** | — |

**Leitura.** O acrescimo e **o maior da serie em termos absolutos** — 4.754 linhas —, e tem a
contrapartida mais concreta ate agora: **a cobertura documental sai de 4/9 para 9/9**, uma
pendencia soberana e respondida e **oito** ressalvas e achados fecham. **Nenhum tipo, entidade,
camada ou documento fundacional foi criado, e nenhuma fundacional foi emendada** — o criterio
de consolidacao, que poderia ter ido para dentro de FND-09, ficou **fora** dela por decisao
declarada em [RFC-0010 §4](../../rfcs/RFC-0010-criterio-de-horizonte-avaliavel.md).

**Contrapartida honesta:** **oito** regras novas com **zero** membros observados, **oitavo**
ciclo consecutivo de crescimento, e **cinco Cartas que nao entram em vigor por este trabalho**.

**Resposta:** **nao**.

## F2 — Algum conceito foi duplicado? E a prevencao foi aplicada?

### F2.a — Ocorrencia

| Conceito | Onde ja estava | Como a mudanca o trata |
|---|---|---|
| Ato soberano de 2026-07-28 sobre `DEP-QAR` | — | **Fonte canonica propria:** `MSG-2026-0003`. `MSG-2026-0001` e `MSG-2026-0002` **nao editadas** |
| Diff da emenda `DEP-QAR` 1.1.0 | REV-ESTRUTURAL-I §7.2 | **Referenciado**, nao recopiado. `MSG-2026-0003 §7.2` registra o **efeito**, nao o texto |
| Criterio de consolidacao | Ato soberano | **Um** instrumento: `ADR-0013`. **Nao** escrito em FND-09 §12 **nem** em FND-02 §9.3 — a duplicacao que a Alternativa A produziria |
| Diff da emenda constitucional | — | **Um** lugar: `RFC-0011 §3.2`. `ADR-0014` o **referencia** e nao o reproduz |
| Matriz de interacao de FND-02 §4 | FND-02 §4 | **Barrada nas cinco Cartas.** Cada uma declara **so as proprias linhas** (DC-08) |
| Matriz Departamento × Capability | `capabilities/README §10` | **`departments/README §3` declara-se projecao de segunda ordem** e aponta a primaria |
| Onze testes de validacao | — | **Um** registro consolidado, **nao** um arquivo por cenario (RG-05) |

**Nenhuma duplicacao nova introduzida.**

### F2.b — Prevencao *(PJ-06)*

| Verificacao | Evidencia | Resultado |
|---|---|---|
| O autor percorreu cada tabela pelo item de PJ-05? | Todas as tabelas dos 14 artefatos novos | **Sim** |
| Toda exibicao de conteudo de outra fonte declara projecao? | **6** declaracoes novas: as **cinco** secoes 2 das Cartas + `departments/README` | **Sim** |
| Alguma reproducao foi **barrada antes** de ser escrita? | **6** — a matriz de FND-02 §4, o diff da emenda, o criterio em FND-09, o diff constitucional, a matriz de Capability e o texto das 28 regras `CT` | **Sim** |
| O teste encontrou algo que a auditoria posterior nao encontraria? | **4 — RC-01, RC-04, RC-05 e RC-07.** Nenhum e projecao contra fonte: os quatro sao **assimetrias entre fontes irmas**, visiveis so na leitura conjunta | **Sim** |

> **Sexta confirmacao de [MEM-APR-0002](../../memory/aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md),
> e a familia cresceu de novo.** Ate a missao anterior o mecanismo chegara a *documento que
> diverge de si proprio*. Agora chega a **fontes irmas que divergem entre si**: nove Cartas do
> mesmo contrato, quatro das quais declaram algo que uma nao declara. **A varredura C11 nao
> alcanca isso, e a auditoria de uma Carta isolada tampouco.** O instrumento que alcanca e a
> **projecao comparativa** — terceira confirmacao de
> [MEM-APR-0004](../../memory/aprendizado/MEM-APR-0004-projecao-revela-divergencia-antiga.md).

**Resposta:** nao houve duplicacao nova · prevencao **aplicada**, com evidencia.

## F3 — Alguma abstracao ficou desnecessaria?

| Abstracao | Membros antes | **Membros agora** | Veredito |
|---|---|---|---|
| **`DC-01` a `DC-10`** *(contrato de Carta)* | 10 regras, exercicio limitado a 4 Cartas | **10 de 10 exercidas**, sobre **9** Cartas | **Justificada — sai da suspeita.** R1 de FIT-2026-005 exigia **seis**; houve **dez** |
| **`IR-01` a `IR-12`** *(integridade do ato)* | 5 artefatos, 2 com `IR-09` | **6 artefatos**, **3** com `IR-09` executado | **Justificada e crescendo** |
| **`HZ-01` a `HZ-08`** *(criterio de horizonte)* | — | **0 membros observados** | ⚠️ **Suspeita declarada, nao dissimulada.** `HZ-02` nunca disparou e `HZ-04` tambem nao. **A1 e A2 de ADR-0013 §8** declaram isso antes de qualquer uso |
| **Classe `inferred` · classe 4 de autoridade** | 0 · 0 | **0** — e sao **o mesmo objeto** | **Mantida.** Zero e o resultado bom |
| Os **4 pacotes** de contexto `CT` | 0 consumidores elegiveis | **0** | **Mantida** — nenhum componente criado |
| **`PR-1` · `PR-2`** *(fonte prevalece sobre projecao)* | 0 · 0 | **0 · 0** | **Mantidas.** **Nenhuma divergencia Carta × Carta de Capability ocorreu** nas cinco novas — e isso e o resultado bom, nao ausencia de uso |
| **Arquetipo `A2`** · **classe `M3`** | 2 · 1 membro, 4 usos | **2 · 1 membro, 6 usos** | **Justificadas** — `M3` decidiu tambem `departments/README` e a correcao de P7 |
| **Portao de admissao** de ADR-0007 | 0 | **0** | **Mantido** — nenhum candidato do Legacy; **nao consultado** |

**Regra aplicada:** abstracao com menos de dois membros e suspeita (AQ-03).

**Resposta:** **nao** — e a unica suspeita nova, `HZ`, **nasce declarada como tal**. E o quinto
ciclo consecutivo instituindo regime preventivo inteiro *(FR, PJ, CT, DC, IR, agora HZ)*, e o
padrao esta nomeado em **RH-3 de ADR-0013**.

## F4 — O sistema continua mais simples de evoluir?

| Mudanca-tipo | Antes | Depois | Aprovacoes |
|---|---|---|---|
| Saber **quando um horizonte pode ser avaliado** | **Nao havia resposta** — e nenhum se fechou em 7 ciclos | `HZ-02`: **duas condicoes verificaveis** | Inalterado |
| Saber se *"nada a consolidar"* e falha | Julgamento — e a revisao anterior precisou justificar-se | `HZ-01` e `HZ-05`: **e resultado valido, com evidencia individual** | Inalterado |
| Saber **o que distingue um departamento do outro** | Abrir **nove** arquivos | **Uma** tabela: `departments/README §2` | Inalterado |
| Saber **quem substitui quem** em cada impedimento | Disperso em quatro Cartas | **92** impedimentos mapeados por materia | Inalterado |
| Saber se a Constituicao usa *ratificar* em dois sentidos | Afirmado por IC-2, **sem contagem** | **Medido: 5 linhas em FND-01 §7.3, 0 em FND-09 §8.2** | Inalterado |
| Emendar a Constituicao para corrigir IC-2 | **Nao havia texto** | **8 alteracoes literais**, prontas em RFC-0011 | Inalterado — **falta so o ato** |

**Leitura.** **Seis** perguntas antes sem resposta verificavel passam a ter uma. **Nenhuma
aprovacao nova foi criada**; nenhum caminho de decisao ficou mais longo; **nenhum papel ganhou
veto novo**; **nenhuma fundacional foi emendada**.

**Contrapartida:** **oito** regras novas a carregar, e **tres** questoes continuam dependendo
do Soberano — as cinco Cartas, Q1 e Q2.

**Resposta:** **sim**.

## F5 — A mudanca reduz ou aumenta o custo de contexto?

| Papel / tarefa-tipo | Antes | Depois | Direcao |
|---|---|---|---|
| **Piso obrigatorio de qualquer tarefa** | 1.099 linhas | **1.099 linhas** | **inalterado** |
| **Executar uma missao estrutural** | **21,3%** — 5a medicao | **18,9%** — 6a medicao | **DESCE** |
| **Saber o que distingue os nove departamentos** | **9 arquivos = 3.918 linhas** | **`departments/README §2` = 1 tabela, 16 linhas** | **desce 99,6%** |
| **Decidir se um departamento pode aprovar algo** | Recorte de Carta, 111–155 linhas | **Inalterado** — 111 a 155 nas nove | **inalterado** |
| Consultar o criterio de consolidacao | **Inexistente** | `ADR-0013 §5.1` — **8 regras, 10 linhas** | **desce, a partir do indisponivel** |
| Acervo total | 30.947 | **35.701** | **sobe 15,4%** |

### F5.1 A medicao, itemizada — **a segunda da serie**

**Pacote minimo medido: 5.848 linhas sobre 30.947 = 18,9%.** Composicao **itemizada**:

| Bloco | Linhas |
|---|---|
| **Artefatos integrais** — FND-01, FND-02, FND-06, ADR-0011, ADR-0012, `TPL-carta-departamento`, REV-ESTRUTURAL-I, FIT-2026-007, README raiz, `DEP-QAR`, `DEP-ENG`, MSG-2026-0002 | **4.779** |
| **Recortes normativos** — RFC-0009 §5–§11, `capabilities/README` §4.1–§11, FND-09 §5.4/§7/§8/§11.5–§12, FND-10 §2.2/§5.4/§10.3, FND-04 §1–§2/§6–§7, FND-05 §2/§7.1/§8 | **782** |
| **Extracoes por ferramenta** — frontmatter das 23 Cartas de Capability; recortes de `DEP-EXE` e `DEP-KMS` | **267** |
| **Indices abertos para propagar (C11)** | **20** *(o restante ja consta dos integrais)* |
| **Total** | **5.848** |

**A serie observada e 23% · 33% · 30,6% · 18,5% · 21,3% · 18,9%.**

> ### O que esta medicao estabelece — e o que ela ainda **nao** fecha
> **E a segunda medicao itemizada da serie, e a primeira que pode ser comparada a outra.** A
> quinta media **21,3%** com composicao declarada; esta mede **18,9%** com composicao declarada.
> **A comparacao e valida** — e o achado **RE-08** ficou satisfeito quanto ao **metodo**.
>
> **Resultado: primeira descida comparavel da serie — 2,4 pontos.**
>
> **R4 de FIT-2026-002 permanece aberta**, e o criterio endurecido diz por que: exige **duas
> descidas consecutivas com composicao itemizada**, e esta e **a primeira**. Fechar agora seria
> exatamente o que o endurecimento existe para impedir.
>
> **Por que desceu, medido:** a missao anterior abriu **1.230 linhas de indices** para propagar
> correcoes por todo o acervo; esta abriu **20**, porque as correcoes sao **acrescimos
> localizados** e nao reconciliacoes globais. **A diferenca de 1.210 linhas explica sozinha a
> descida** — e isso significa que **o custo caiu por natureza da missao, nao por ganho
> estrutural**. Declarado para que a descida nao seja lida como melhora de arquitetura.

**Resposta:** **desceu** — **e a queda esta explicada por composicao, nao atribuida a merito.**
**→ R4 de FIT-2026-002 permanece aberta**, com **uma** das duas descidas exigidas.

## F6 — Ela favorece reutilizacao?

| Definicao produzida | Reutilizavel por | Especifica do caso? |
|---|---|---|
| **`HZ-01` a `HZ-08`** — quando um horizonte e avaliavel | **Toda revisao de consolidacao futura**, e havera uma por horizonte | Nao |
| **`HZ-05`** — *"nenhum candidato elegivel"* com evidencia individual | **Toda** proposta de consolidacao, retroativamente legitimada | Nao |
| **A projecao comparativa** de `departments/README §2` | **Toda** pergunta *"o que distingue X de Y"* — e revelou **4** achados que nenhuma Carta revelaria | Nao |
| **Os onze testes** de REV-ROLLOUT §3 | **Toda** Carta futura, inclusive **Carta de Agente** quando existir | Nao |
| **O instrumento de validacao, e a licao de valida-lo contra o que ja passou** | **Toda** verificacao automatizada futura | Nao |
| **Homologacao × ratificacao**, exercido em 3 linhas | **Toda** Carta que declare confirmacao por titular nao-soberano | Nao |
| **Preservacao de versao por hash + diff reversivel** *(MSG-2026-0003 §2.1)* | **Toda** emenda a artefato ratificado | Nao |
| RC-01 a RC-08 | — | **Sim** — descrevem o estado atual |

**Criterio:** DoD-8.

**Evidencia mais forte:** **a projecao comparativa encontrou quatro achados em Cartas que ja
haviam passado por validacao individual** — RC-01, RC-04, RC-05 e RC-07. Duas delas estao **em
vigor desde a Missao 1.7**. **Nenhum instrumento anterior os alcancava.**

**Resposta:** **sim**.

---

## Ressalvas

| # | Ressalva | Custo assumido | **Dono** | **Gatilho de reavaliacao** |
|---|---|---|---|---|
| **R1** | **As oito regras `HZ` nascem com zero membros observados.** `HZ-02` nunca disparou; `HZ-04` tambem nao. E o **quinto** ciclo consecutivo instituindo regime preventivo inteiro | O criterio que resolve PS-1 **ainda nao foi exercido nenhuma vez**. Se `HZ-02` nunca disparar, o criterio novo repete por outro caminho o defeito que substituiu | **DEP-EXE** | **Duas revisoes estruturais consecutivas** sem que `HZ-02` nem nenhum `HZ-04` dispare *(ADR-0013 §12, gatilho b)* |
| **R2** | **Oitavo ciclo consecutivo de crescimento, e o maior acrescimo absoluto da serie: +4.754 linhas.** Zero consolidacoes em oito ciclos | O acervo cresce **15,4%** em uma missao. **`HZ-01` retira a leitura de que isso e falha**, e **nao** retira o fato | **DEP-EXE** | **Primeiro horizonte avaliavel sob `HZ-02`** |
| **R3** | **A segregacao de papeis opera de novo no limite, e de forma nova.** DEP-QAR executa este `FIT` tendo tido a propria Carta ratificada nesta missao; DEP-GOV o aprova tendo sido autor da forma de REV-ROLLOUT; e **DEP-EXE e autor de 9 de 9 Cartas** | **R1 de FIT-2026-006 nao fecha** e **agrava-se**: o contrato de Carta nunca foi testado contra autor distinto. A estrutura **nao comporta** segregacao completa sem agentes | **DEP-GOV** | **Primeiro agente criado**, ou **IC-3** resolvido. Achado **RC-08** |
| **R4** | **Tres achados estao em Cartas ja ratificadas e nao podem ser corrigidos sem ato novo.** RC-01 *(`DEP-QAR` declara 386 linhas, tem 387)*, RC-05 *(`DEP-KMS` nao trata incidente)* e RC-07 *(`DEP-ENG` nao declara impedimento sobre a propria Carta)* | **Segunda vez** que a imutabilidade por ratificacao retem defeito conhecido — a primeira foi IC-5, agora corrigido. **Os tres tem efeito nulo ou local**, e por isso **nao** foram levados ao pacote soberano | **DEP-EXE** | **Proxima emenda a cada uma das tres Cartas**, por qualquer motivo |

## Veredito

| Campo | Conteudo |
|---|---|
| Veredito | **`apto-com-ressalva`** |
| Fundamento | As seis perguntas tem sinal observavel. **A cobertura documental vai de 4/9 a 9/9**; **uma pendencia soberana e respondida e formalizada sem emendar nenhuma fundacional**; **oito** ressalvas e achados fecham com evidencia; **o custo de contexto desce pela primeira vez de forma comparavel**; e **10 de 10 regras `DC` sao exercidas**, tirando o contrato de Carta da suspeita de AQ-03. Em contrapartida, o acervo cresce **15,4%** — o maior salto absoluto da serie —, **oito** regras novas nascem com **zero** membros, **tres** achados ficam retidos em Cartas ratificadas, e a segregacao de papeis opera **no limite do possivel pela terceira missao seguida**. **Nao e `inapto`** porque nenhuma contrapartida revela degradacao sem contrapartida verificavel, e **nenhuma divida foi fechada por renomeacao**. **Nao e `apto` sem ressalva** porque quatro dividas seguem abertas, com dono e gatilho |
| Efeito | **Encerra a mudanca C2.** As quatro ressalvas viram divida declarada (FND-07 §9) |
| Data | 2026-07-28 |
| Executado por | **DEP-QAR** |
| Aprovado por | **DEP-GOV** — DEP-EXE impedido (CX-3) |
| Ratificado por | **Nao aplicavel** — objeto C2/Tipo 2. **Se isso e correto e a questao Q2**, escalada |

## Fechamento da camada — **`READY-FOR-RATIFICATION`**

> **Criterio de fechamento, declarado antes da avaliacao** (entregavel 8 da missao): a camada e
> **pronta para consumo** somente quando houver **(a)** cobertura 9/9, **(b)** autoridade
> inequivoca, **(c)** validacao independente, **(d)** rastreabilidade e **(e)** pacote soberano
> completo.

| # | Condicao | Estado | Evidencia |
|---|---|---|---|
| **(a)** | **Cobertura 9/9** | ✅ **Cumprida** — documentalmente | **9** Cartas para **9** departamentos; **23** custodias; **0** Capabilities sem custodio. `departments/README §1` |
| **(b)** | **Autoridade inequivoca** | ⚠️ **Cumprida com ressalva** | **0** autoridades autodeclaradas nas nove *(DC-04, AU-09)*; **92** impedimentos com substituto nomeado. **A ressalva e IC-2**: o termo *ratificar* ainda nomeia **dois institutos** em FND-01 §7.3, contido por `IR-11` com **0** violacoes medidas |
| **(c)** | **Validacao independente** | ✅ **Cumprida** | **55 testes sobre as cinco Cartas: 53 ✅, 2 ⚠️, 0 ❌.** Revisor distinto do autor em **9 de 9**; **0** ocorrencias de autoverificacao |
| **(d)** | **Rastreabilidade** | ✅ **Cumprida** | **0** links quebrados em **1.267** verificados; **0** artefatos M1 editados; cadeia **ato → versao → conteudo → estado** fechada por `H-A`, `H-N`, `H-P` e `IR-09` |
| **(e)** | **Pacote soberano completo** | ✅ **Cumprida** | [PS-2026-002](../pacote-soberano-2026-07-28-cartas.md) — **5** Cartas com ID, versao, dois hashes, Capability, revisao, riscos e recomendacao; emenda **C3 separada**; caminho exato anexado *(RE-01)* |

### A decisao, e por que nao e `GO`

| Campo | Conteudo |
|---|---|
| **Decisao** | **`READY-FOR-RATIFICATION`** |
| **O que significa** | **Tudo o que esta missao podia produzir esta produzido e verificado.** O que resta **nao e trabalho: e ato do Soberano** |
| **Por que nao `ADJUST`** | Nenhuma correcao delimitada resta pendente **dentro do mandato desta missao**. Os tres achados retidos *(R4)* **nao sao corrigiveis** sem ato novo, e nao bloqueiam nada |
| **Por que nao `STOP`** | Nenhuma falha estrutural foi encontrada: **0 ❌** em 55 testes; **0** sobreposicoes de escopo; **0** relacoes nulas; **0** ciclos |
| **Por que nao `BLOCKED`** | A pre-condicao 1 **foi satisfeita**: o ato soberano sobre `DEP-QAR` 1.1.0 chegou, e ID, versao, hash, diff e integridade foram **verificados por dez vias**, com `IR-09` reproduzindo `H-A` exatamente |
| **A camada esta pronta para consumo?** | **NAO — e a distincao e o produto desta secao.** A camada esta pronta para **ratificacao**. **Cinco das nove Cartas nao estao em vigor**, e Carta que nao vigora **nao pode ser consumida** (LM-02). A cobertura **documental** e 9/9; a cobertura **vigente** e **4/9** |
| **Desempenho** | **Nao exercido, logo nao comprovado.** **41 de 123** indicadores estao marcados `definido, sem valor`, e os **82** medidos descrevem **o acervo**, nao o desempenho de nenhum departamento. Nenhuma Carta foi exercida em operacao real |

## Pendencia para o SOBERANO — **tres, em um unico pacote**

> Esta secao **informa e pergunta**; nao decide, nao presume e nao antecipa (LM-03, LM-06).
> Tudo esta em [PS-2026-002](../pacote-soberano-2026-07-28-cartas.md).

| # | Pendencia | Origem | Se nao houver ato |
|---|---|---|---|
| **PS-2** | **As cinco Cartas em `em-revisao`** — GOV, TLS, PRD, OPS, GRW | DC-09; FND-09 §8.2, linha `DEP` | Cobertura vigente permanece **4/9**. Nada quebra; a camada **nao fecha** |
| **PS-3** | **Emenda C3 a FND-01 §7.3** — separar ratificacao de homologacao | **Q1** de RFC-0009; ADR-0014 candidato | **IC-2 permanece contido** por `IR-11`, quinto ciclo. **0** violacoes medidas |
| **PS-4** | **`FIT` exige ratificacao do Soberano?** | **Q2** de RFC-0009; G1/G2 de INC-2026-002 | **G1/G2 permanece aberta.** `FIT-2026-001` segue com registro incorreto **contido, nao corrigido** — e **este proprio `FIT`** declara `nao-exigida` sob a leitura que Q2 questiona |

> **PS-1 nao consta: foi respondida** pelo ato de 2026-07-28 e formalizada em
> [ADR-0013](../../decisions/ADR-0013-criterio-de-horizonte-e-consolidacao.md).

### Nota sobre FT-04 — vigilancia de complacencia

| Verificacao | Estado |
|---|---|
| Vereditos emitidos | **8** |
| Consecutivos `apto` **sem nenhuma ressalva** | **0** — os oito com ressalvas |
| `inapto` emitidos | **0** |
| Ressalvas e achados fechados neste ciclo | **8** |
| Achados novos | **8** |
| **Recomendacoes de APROVAR no pacote soberano** | **5 de 5** — **nenhuma de DEVOLVER** |
| Revisoes estruturais que concluiram "manter" | **1 de 3** antes da escalada obrigatoria (FND-02 §9.4) — **inalterado**: esta missao **nao** e revisao estrutural |

FT-04 exige tres `apto` **sem ressalva** para disparar; nao e o caso.

> **O alarme desta verificacao e novo, e nao e o numero de ressalvas fechadas.** E que **cinco
> de cinco Cartas foram recomendadas para aprovacao, por quem as escreveu ter sido o mesmo
> departamento em todas as nove**. **Mitigacao verificada:** o instrumento de validacao foi
> executado **primeiro** sobre as quatro Cartas ja em vigor e **acusou falha nelas**; a
> distincao entre defeito do instrumento e defeito da Carta produziu **RC-05** e **RC-07**,
> ambos em Cartas **ratificadas**, e **nenhum foi suprimido** por piorar o relatorio. **Um lote
> sem devolucoes e um lote a auditar** — e o auditor registrou que o auditou.

Permanece o numero a vigiar: **nenhum `inapto` em oito oportunidades**.

### Nota de conflito de interesse (PI-10)

| Campo | Conteudo |
|---|---|
| Conflitos identificados | **Tres.** **(1)** DEP-EXE e autor de **9 de 9** Cartas. **(2)** DEP-QAR executa este `FIT` tendo tido a propria Carta ratificada na missao. **(3)** DEP-GOV aprova este parecer tendo sido autor da forma de REV-ROLLOUT |
| Por que nao invalidam | **(1)** DEP-EXE **nao verifica, nao revisa e nao aprova** nada aqui — e o impedimento `DEP-EXE I-2` foi aplicado. **(2)** O objeto deste `FIT` **nao inclui** `DEP-QAR` 1.1.0. **(3)** O objeto **nao inclui** REV-ROLLOUT |
| Desvios aplicados | Aprovacao transferida de DEP-EXE para DEP-GOV (CX-3); revisao da Carta de `DEP-GOV` transferida de DEP-GOV para DEP-QAR; verificacao da emenda `DEP-QAR` executada por DEP-GOV, **fora** desta cadeia |
| Alternativa recusada | Escalar a aprovacao deste `FIT` ao **SOBERANO** — recusada por proporcionalidade *(C2/Tipo 2)* e porque sobrecarregaria o mesmo ato que decide as cinco Cartas |
| **Residuo** | A estrutura **nao comporta** segregacao completa com **um unico autor de Carta** e **zero agentes**. **Declarado em vez de omitido**, em R3 e RC-08. Desaparece quando existirem agentes |

## Aprendizado gerado

| Registro APR | Licao |
|---|---|
| [MEM-APR-0002](../../memory/aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md) | **Sexta confirmacao, com alcance ampliado pela quinta vez:** o mecanismo chegou a **fontes irmas que divergem entre si** — nove Cartas do mesmo contrato, quatro achados que so aparecem na leitura conjunta. Acao: **todo conjunto de artefatos do mesmo contrato exige projecao comparativa antes de fechar a serie**. Dono: DEP-GOV |
| [MEM-APR-0004](../../memory/aprendizado/MEM-APR-0004-projecao-revela-divergencia-antiga.md) | **Terceira confirmacao:** a projecao comparativa revelou **RC-01, RC-04, RC-05 e RC-07**, dois deles em Cartas **em vigor desde a Missao 1.7**. Acao: **projecao nao e vista de conveniencia; e instrumento de auditoria**. Dono: DEP-KMS |
| A gravar por DEP-KMS *(QG-5)* | **Instrumento de verificacao valida-se contra o que ja passou, antes de julgar o que e novo.** O verificador desta missao reprovou as **nove** Cartas, inclusive as quatro validadas em missoes anteriores; a falha era do contador. **Se ele tivesse sido executado so nas cinco novas, teriam sido "corrigidas" para satisfazer um instrumento errado.** Acao: **todo verificador novo roda primeiro sobre um grupo de controle ja aprovado**. Dono: DEP-QAR |
| A gravar por DEP-KMS *(QG-5)* | **Queda de custo de contexto pode ser da missao, nao da arquitetura.** A descida de 21,3% para 18,9% e explicada por **1.210 linhas de indices** que esta missao nao precisou abrir. Acao: **toda medicao de custo declara a natureza da missao ao lado do numero**. Dono: DEP-KMS |

## Historico de vereditos sobre este objeto

| FIT | Data | Veredito | Relacao |
|---|---|---|---|
| FIT-2026-005 | 2026-07-28 | `apto-com-ressalva` | Contrato de Carta; **R1** exigia 6 de 10 regras `DC` — **fechada quanto a medicao** aqui, **mantida** quanto a autor distinto |
| FIT-2026-006 | 2026-07-28 | `apto-com-ressalva` | Validacao interclasses; **R2** *(5 de 9 sem Carta)* **fecha aqui**; **R1** *(autor unico)* **agrava-se** |
| FIT-2026-007 | 2026-07-28 | `apto-com-ressalva` | Revisao estrutural; **R2** *(criterio de consolidacao)* **fecha aqui** |
| **FIT-2026-008** | 2026-07-28 | **`apto-com-ressalva`** | **Nao supera nem edita nenhum anterior** (M1, LV-04, FT-09). Fecha **tres** ressalvas de tres `FIT` distintos **pelo texto que elas proprias escreveram** |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-QAR | Verificacao de aptidao da **Missao 1.9**: seis perguntas com sinal observavel; **cobertura documental 9/9**; **8 ressalvas e achados fechados**; **F5 desce a 18,9%** na **2a medicao itemizada** — primeira descida comparavel da serie, com a causa declarada; **10 de 10 regras `DC` exercidas**, tirando o contrato de Carta da suspeita de AQ-03; **8 regras `HZ` nascem com zero membros**, declarado; **4 ressalvas** novas; fechamento **`READY-FOR-RATIFICATION`** e **3** pendencias em um unico pacote soberano. |
