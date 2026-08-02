---
id: ADR-0010-contrato-de-conhecimento-do-soberano
titulo: Adotar o Contrato de Conhecimento sobre o Soberano, com registro na camada EST e sem autoridade normativa
tipo: adr
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-KMS
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0001, ADR-0006, ADR-0007, ADR-0008, ADR-0009]
substitui: []
substituido_por: null
classe_mudanca: C2
tipo_decisao: 2
supera: []
superado_por: null
resumo: Institui o contrato que governa como conhecimento sobre o Soberano e capturado, evidenciado, classificado, acessado, carregado e aposentado, sem nunca obrigar.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# ADR-0010: Contrato de Conhecimento sobre o Soberano

## Proposito

Registrar a decisao de instituir o **Contrato de Conhecimento sobre o Soberano** — o regime que
governa como conhecimento operacional sobre o Soberano e capturado, evidenciado, classificado,
acessado, carregado, revisado e retirado — e de hospedar esse conhecimento na camada **EST** da
memoria, onde ele **orienta sem obrigar**.

## Escopo

| Item | Definicao |
|---|---|
| **Inclui** | Finalidade, autoridade, custodia, consumidores, acesso, ciclo e limites do contrato; classes de evidencia; fronteira de autoridade; privacidade e minimizacao; pacotes de contexto com custo medido; regras de evolucao; autorizacao da primeira instancia |
| **Nao inclui** | O **conteudo** do conhecimento — vive em [MEM-EST-0001](../memory/estrategica/MEM-EST-0001-contexto-do-soberano.md); ratificacao de qualquer decisao pendente; alteracao do termo oficial `SOBERANO` (C3); criacao de agente, subagente, skill, comando, workflow, produto, codigo, banco, ontologia, Reasoning Framework ou programa de migracao; perfil psicologico ou diagnostico de qualquer natureza |
| **Subordinado a** | [FND-01](../foundation/01-constituicao.md), [FND-04](../foundation/04-governanca.md), [FND-06](../foundation/06-arquitetura-memoria.md), [FND-07](../foundation/07-framework-decisoes.md), [FND-09](../foundation/09-meta-model.md), [FND-10](../foundation/10-artifact-framework.md) |

## Responsaveis

| Papel | Quem |
|---|---|
| Proponente | **DEP-KMS** |
| Revisor independente | **DEP-QAR** |
| Aprovador | **DEP-EXE**, com parecer de DEP-GOV (FND-04 §2.1, C2) |
| Ratificador | **Nao aplicavel** — C2/Tipo 2 (§11) |
| Executor | DEP-GOV |

---

## 1. Contexto

O sistema tem dez documentos fundacionais, 21 entidades, 23 Capabilities e **nenhum
componente**. A fase seguinte cria Cartas de departamento e, depois, agentes — papeis que
executarao trabalho sob criterios que hoje **nao estao escritos em lugar nenhum**.

A camada **EST** ja declara como seu, desde a v1.0.0 de [FND-06 §3.1](../foundation/06-arquitetura-memoria.md),
exatamente este conteudo: *"restricoes permanentes impostas pelo Soberano"* e *"padroes
duraveis de preferencia do Soberano sobre como o trabalho e feito"*. A camada tem **zero**
registros formais, e seu proprio indice declara que eles surgirao quando houver conhecimento
estrategico **fora** da Fundacao e do catalogo de Capabilities.

O risco de nao ter esse registro nao e hipotetico. [INC-2026-001](../governance/incidents/INC-2026-001-ratificacao-inferida.md)
documenta quatro decisoes C3/Tipo 1 que trataram **instrucao generica anterior** como ato de
autoridade — severidade alta, violacao de LV-05. A causa foi corrigida para o **ato de
ratificacao** (CV-09, LM-02), mas nada foi corrigido quanto ao **criterio difuso**: quando um
papel precisar saber o que o Soberano considera qualidade, continuara sem instrumento e com o
mesmo incentivo a inferir.

**Se nada mudar:** o primeiro agente herdara criterio por inferencia, sob pressao de um caso
concreto — a mesma ordem de eventos que [ADR-0007](ADR-0007-fronteira-greenfield-legado.md)
recusou para a fronteira com o Legacy.

## 2. Problema / Pergunta de decisao

**Onde deve viver o conhecimento operacional sobre o Soberano, e sob que contrato, para que
oriente escolhas sem nunca obrigar?**

## 3. Criterios de decisao

> Declarados antes do exame das alternativas (CD-01, VD-02). Fonte:
> [RFC-0007 §4](../rfcs/RFC-0007-conhecimento-sobre-o-soberano.md).

| # | Criterio | Peso |
|---|---|---|
| C1 | Conhecimento sobre o Soberano **nunca** adquire forca normativa, e a subordinacao e **estrutural** | **Bloqueante** |
| C2 | Nenhuma entidade, arquetipo, relacao, tipo documental ou camada nova | **Bloqueante** |
| C3 | Abstracao proporcional a evidencia — nenhum artefato normativo novo para dominio com zero instancias | **Bloqueante** |
| C4 | Toda afirmacao rastreavel, com classe e confianca | Alto |
| C5 | Carregamento minimo por padrao, com custo medido | Alto |
| C6 | Reversivel | Medio |

## 4. Alternativas consideradas

Analise completa em [RFC-0007 §5](../rfcs/RFC-0007-conhecimento-sobre-o-soberano.md). Sintese:

### Alternativa A — Contrato por ADR + instancia na camada EST *(escolhida)*

| Campo | Conteudo |
|---|---|
| Descricao | ADR institui o regime; o conhecimento vive como `MEM-EST` sob `TPL-memoria`; FND-06 §3.1 e FND-03 §8 recebem emendas MENOR |
| A favor | A subordinacao a norma e **herdada**, nao declarada: `MEM` tem autoridade normativa **nenhuma** (FND-09 §5.7, E-20) e perde para o ADR (MM-07). Zero artefato normativo novo. Precedente direto: ADR-0007 (FR-01 a FR-10) e ADR-0008 (PJ-01 a PJ-06), regimes inteiros por ADR C2 |
| Contra | Contrato em **M1**: evoluir exige superacao, nao emenda |
| Custo | 1 ADR · 1 registro `MEM-EST` · 2 emendas MENOR · 1 termo de vocabulario |
| Risco | M1 encarecer a evolucao (R4) |
| Avaliacao | C1 ✔ · C2 ✔ · C3 ✔ · C4 ✔ · C5 ✔ · C6 ✔ |

### Alternativa B — Criar FND-11

| Campo | Conteudo |
|---|---|
| Descricao | Decimo primeiro documento fundacional para hospedar o contrato |
| A favor | Documento **M2**, versionavel; e onde um leitor procuraria "o framework" |
| Contra | **Falha em C3:** criar documento fundacional para dominio com **zero instancias anteriores** e antecipacao, vedada por SE-01, SE-02 e FND-08 §7.1, e ja registrada como divida em [FIT-2026-003 R2](../governance/fitness/FIT-2026-003-consolidacao-baseline.md). **Tensiona C1:** `FND` ocupa o **nivel 2** de FND-01 §10, **acima dos ADRs** — hospedar este regime acima da fonte das decisoes e o oposto do que ele precisa declarar |
| Custo | **C3 com ratificacao** (FND-09 §5.2, E-03): RFC, impacto, ADR, ato do Soberano e emenda de FND-01 §10 |
| Risco | Como esta missao **nao ratifica**, o framework nasceria em `aprovado` e **nao entraria em vigor** (LM-02) — e a instancia herdaria a pendencia |
| Avaliacao | C1 **tensiona** · C2 ✔ · C3 **falha** · C4 ✔ · C5 ✔ · C6 **falha** |

### Alternativa C — Emendar FND-06 com secao propria

| Campo | Conteudo |
|---|---|
| Descricao | O contrato vira secao de FND-06 |
| A favor | Nenhum artefato novo; C2; fica junto da camada que hospeda o conteudo |
| Contra | **Distorce o escopo declarado de FND-06** — arquitetura transversal das cinco camadas, nao contrato de um assunto (FND-10 §9.3). Acresce ~120 linhas a um artefato de 517 (CE-05) e coloca o regime no nivel 2 da hierarquia, com a mesma tensao de C1 da Alternativa B |
| Custo | Baixo em arquivos, alto em coerencia |
| Risco | FND-06 virar o lugar do que nao coube em outro lugar |
| Avaliacao | C1 **tensiona** · C2 ✔ · C3 ✔ · C4 ✔ · C5 ✔ · C6 ✔ |

### Alternativa Z — Nao fazer nada

| Campo | Conteudo |
|---|---|
| O que acontece se mantivermos o estado atual | O criterio do Soberano segue disperso em instrumentos cujo objeto e outro, sem classe de evidencia, sem confianca e sem regra de acesso |
| Custo real da inacao | Ja observado: o acervo converteu instrucao generica em autoridade uma vez (INC-2026-001, severidade alta). O primeiro agente enfrentara a mesma lacuna com o mesmo incentivo — e agora o defeito e **conhecido** |
| Por que nao venceu | Manter lacuna ja observada e escolha, nao inercia |

## 5. Decisao

**Decidimos instituir o Contrato de Conhecimento sobre o Soberano nos termos abaixo, e
autorizar a primeira instancia na camada EST.**

### 5.1 O contrato

| Dimensao | Conteudo |
|---|---|
| **Finalidade** | Permitir que estruturas futuras compreendam visao, criterios, linguagem e forma de trabalho do Soberano **sem inferir** e **sem microgestao** (Visao V1) |
| **Autoridade** | **Nenhuma normativa.** O Contexto do Soberano **orienta escolhas apenas onde a norma admite escolha**. Nunca supera Constituicao, Governanca, ADR vigente, evidencia verificavel ou seguranca |
| **Custodia** | Dono da camada: **DEP-GOV** (FND-06 §3.1). Curador: **DEP-KMS**. Verificacao independente: **DEP-QAR**. **Unica autoridade que confirma o conteudo: o SOBERANO** |
| **Consumidores** | Qualquer papel, no momento e na medida do pacote aplicavel (§5.5). Hoje **nao existe componente**: o unico consumidor real e a propria execucao de missao |
| **Acesso** | Por pacote e por sensibilidade (§5.4). Acesso integral por padrao e **proibido** |
| **Ciclo** | Captura → validacao → registro → revisao → substituicao, expiracao ou retirada (§5.6) |
| **Limites** | §5.7 |

| # | Regra |
|---|---|
| **CT-01** | **Contexto do Soberano orienta; nunca obriga.** Em conflito com Constituicao, Governanca, ADR vigente, evidencia verificavel ou seguranca, **o Contexto cede** — e o conflito e registrado, nunca resolvido em silencio (MM-07, FND-06 §7.1). |
| **CT-02** | **A subordinacao de CT-01 e estrutural, nao declarativa.** Ela decorre de `MEM` ter autoridade normativa nenhuma ([FND-09 §5.7](../foundation/09-meta-model.md), E-20). Nenhuma regra deste contrato pode ser lida como criando autoridade que a entidade nao tem (PI-01). |
| **CT-03** | **Conflito exige escalonamento**, no caminho de FND-06 §7.1: DEP-KMS → dono da camada (DEP-GOV) → SOBERANO. Papel que resolve conflito por conta propria produz ato **nulo** (GV-01). |
| **CT-04** | **Preferencia nao vira principio.** Elevar qualquer afirmacao a norma exige o rito da classe — e, se for principio imutavel ou linha vermelha, **C3 com ratificacao** (FND-04 §2, FND-01 §9). Registro em EST **nao** e degrau de promocao a norma. |
| **CT-05** | **O Contexto referencia decisoes; nao as reescreve.** Fonte de decisao e o ADR (PI-04, MM-07). Afirmacao que reproduza conteudo decisorio e projecao indevida e deve virar referencia por ID (PJ-01). |

### 5.2 Classes de evidencia e proveniencia por afirmacao

> **CT-06.** Toda afirmacao registrada declara **oito** informacoes, sem excecao: **fonte**
> (ID ou origem nomeada) · **data** · **contexto** (em que circunstancia a fonte se produziu) ·
> **classe** · **confianca** · **sensibilidade** · **validade** (`ttl`) · **gatilho de revisao**.
> Afirmacao com qualquer uma ausente e **nao conforme** e nao pode ser consumida (MM-02, FM-04).

| Classe | Significa | Efeito |
|---|---|---|
| `stated` | O Soberano **declarou** — ha texto atribuivel a ele, com data | Orienta, nos limites de CT-01 |
| `observed` | Padrao **constatado** em atos registrados do Soberano, sem declaracao correspondente | Orienta com confianca reduzida; sempre citavel a evidencia |
| `inferred` | **Hipotese** derivada de outras afirmacoes | **Nao orienta.** Serve apenas para formular a pergunta a fazer ao Soberano |
| `unknown` | Nao ha evidencia | **Registrado como lacuna**, nunca preenchido |

| # | Regra |
|---|---|
| **CT-07** | **Lacuna registra-se como `unknown`.** Preencher por inferencia, plausibilidade ou analogia e **LV-12**. Nao registrar a lacuna e omissao (PI-10). |
| **CT-08** | **`inferred` nunca vira preferencia oficial sem confirmacao explicita do Soberano.** Sem ela, a afirmacao permanece `inferred` ou **expira**. Nenhum papel confirma no lugar dele (PI-01, LM-03 por analogia direta). |
| **CT-09** | **Vocabulario de classes em ingles, deliberadamente.** Segue o precedente ja vigente de `native` · `legacy-candidate` · `adapted` · `migrated` · `rejected` ([ADR-0007 §5.5](ADR-0007-fronteira-greenfield-legado.md)) e de `ADOPT/ADAPT/REWRITE/RETIRE`. Nao e excecao a LX-05: e o mesmo tratamento ja dado a vocabulario de valor controlado. |
| **CT-10** | **Mudanca registra-se por substituicao, nunca por apagamento** (MM-09). A afirmacao anterior passa a `superado`, apontando para a que a substituiu, e o motivo fica legivel. |
| **CT-11** | **Fonte externa ao acervo declara-se como tal.** Declaracao do Soberano feita fora deste repositorio — instrucao permanente ao ambiente de execucao, mensagem, determinacao de missao — e **evidencia**, nunca norma: FND-01 §10 a situa no **nivel 8**, o mais baixo da hierarquia. A afirmacao dela derivada nomeia a fonte e fica sujeita a **retirada** por ato do Soberano (§5.6). |

### 5.3 Fronteira de autoridade — quatro classes

> **Distinguir estas quatro e a razao pela qual este contrato existe.** Confundi-las e
> exatamente o defeito de INC-2026-001.

| Classe | Instrumento | Efeito | Pode ser contestada? | Expira? |
|---|---|---|---|---|
| **1 — Ato soberano formal** | Ato explicito e datado, registrado em fonte canonica *(modelo: [INC-2026-001 §11](../governance/incidents/INC-2026-001-ratificacao-inferida.md))* | **Obriga** | **Nao** — apenas o Soberano o revê | **Nao** |
| **2 — Decisao empresarial via rito** | ADR vigente | **Obriga** no escopo aprovado, inclusive quem discordou (CD-05) | **Sim** — por superacao (FND-07 §7) | Nao; vale ate ser superada |
| **3 — Preferencia operacional** | Afirmacao `stated` ou `observed` em `MEM-EST` | **Orienta** onde a norma admite escolha | **Sim** — por evidencia contraria ou ato do Soberano | **Sim** — `ttl` e gatilho de revisao proprios |
| **4 — Hipotese sobre o Soberano** | Afirmacao `inferred` | **Nao orienta nem obriga.** Serve para formular a pergunta | **Sim** — por qualquer papel, sem onus | **Sim** — expira se nao confirmada |

| # | Regra |
|---|---|
| **CT-12** | **Nenhuma classe sobe de nivel por acumulo, repeticao ou precedente.** Classe 3 nao vira classe 2 por ser util; classe 4 nao vira classe 3 por ser plausivel. A subida exige o instrumento da classe de destino (CT-04). |
| **CT-13** | **Instrucao generica anterior, determinacao originadora, precedente e silencio nao produzem nenhuma das quatro classes** (LM-03, GV-05, CM-07). Produzem, no maximo, evidencia — que ainda precisa ser classificada. |

### 5.4 Privacidade e minimizacao

> **CT-14 — vocabulario unico de sensibilidade.** A sensibilidade de cada afirmacao usa a
> **mesma** escala do campo `confidencialidade` de [FND-10 §2.2](../foundation/10-artifact-framework.md) —
> `publico` · `interno` · `restrito` · `soberano` —, e **nao** uma escala paralela. Criar
> segunda escala para o mesmo eixo seria segunda fonte de verdade (MM-01, LX-07) e duplicacao
> vedada por PJ-01. *Leitura: o grau "confidencial" corresponde a `restrito`; o grau mais
> fechado corresponde a `soberano`, ao qual **AC-05** ja aplica a proibicao de citacao em
> comunicacao externa e em pacote de contexto sem autorizacao especifica (LV-08).*

#### Conteudo proibido — lista fechada

> **CT-15.** As afirmacoes abaixo **nao entram no acervo**, sob nenhuma classificacao,
> classe de evidencia ou justificativa de utilidade. Lista **fechada**: acrescentar item e C2;
> remover item e **C3**.

| # | Proibido |
|---|---|
| 1 | Credencial, chave, token, senha ou segredo, em qualquer forma (**PI-08**, LV-02, MM-10) |
| 2 | Dado biometrico |
| 3 | Dado medico ou de saude |
| 4 | Dado financeiro pessoal |
| 5 | Documento de identificacao, endereco residencial e contato pessoal |
| 6 | Dado sobre terceiros — familiares, parceiros, clientes — que nao sejam parte declarada do sistema |
| 7 | Detalhe da vida privada sem **necessidade operacional demonstrada, consentimento explicito e acesso formal** — as tres, cumulativas |
| 8 | Avaliacao psicologica, diagnostico, tracos de personalidade ou juizo sobre carater |

| # | Regra |
|---|---|
| **CT-16** | **Minimizacao.** Registra-se o **minimo que torna a afirmacao acionavel**. Afirmacao que so seria util com detalhe pessoal a mais **nao e registrada** — a utilidade nao autoriza o detalhe (PI-11 nao se aplica aqui: o criterio de qualidade nao supera a proibicao). |
| **CT-17** | **Correcao** — afirmacao incorreta e substituida (CT-10), nunca apagada. **Excecao unica:** conteudo do §CT-15 e **removido imediatamente**, com incidente de conformidade aberto em seu lugar (FND-06 §7.3). |
| **CT-18** | **Ocultacao** — afirmacao `restrito` ou `soberano` e **omitida** dos pacotes de contexto por padrao, e sua existencia e visivel como linha sem conteudo, para que a omissao seja auditavel e nao invisivel (PI-10). |
| **CT-19** | **Retirada** — o Soberano pode determinar a retirada de qualquer afirmacao, **sem motivar**. A afirmacao passa a `superado` com o motivo `retirada por ato do Soberano`; se o conteudo nao puder permanecer, aplica-se CT-17. |
| **CT-20** | **Auditoria de acesso** — todo carregamento de pacote acima do minimo declara, no artefato que o consome, **qual pacote** foi carregado e **sob que gatilho**. Carregamento nao declarado e falha de curadoria (CE-01, PC-01). |

### 5.5 Economia de contexto — quatro pacotes

> **CT-21.** O registro tem `perfil_contexto: sob-demanda` (vocabulario de FND-10 §8.2, nao
> alterado). Os quatro **pacotes de contexto** abaixo governam **quais secoes** sao carregadas
> quando o registro e aberto. Sao **recortes**, pelo mesmo mecanismo ja usado para FND-09 e
> FND-10 no nucleo obrigatorio — nao valores novos de `perfil_contexto`.

| Pacote | Gatilho | Consumidor | Fonte *(secoes do registro)* | Custo |
|---|---|---|---|---|
| **P1 — minimo** | **Sempre**, quando o Contexto for consultado | Qualquer papel | §1 e §7 do registro | medido em [MEM-EST-0001 §9](../memory/estrategica/MEM-EST-0001-contexto-do-soberano.md) |
| **P2 — estrategico** | Decisao **C2 ou C3**; priorizacao; arbitragem de tradeoff | DEP-EXE, DEP-GOV | P1 + §2 e §3 | idem |
| **P3 — dominio** | Trabalho no dominio da afirmacao — produto, engenharia, design, comunicacao | O papel do dominio | P1 + a **subsecao** aplicavel de §4 | idem |
| **P4 — sob demanda** | Gatilho nomeado no proprio registro | Quem o gatilho nomear | A afirmacao especifica, por ID | idem |

| # | Regra |
|---|---|
| **CT-22** | **Carregamento integral e proibido por padrao** (CE-01). Carregar alem do pacote aplicavel exige **gatilho declarado**, e o gatilho e registrado (CT-20). |
| **CT-23** | **O custo de cada pacote e medido em linhas, nunca estimado** (CE-02, CE-04). Pacote sem custo medido nao entra em vigor. |
| **CT-24** | **O resumo operacional e projecao, nunca fonte.** O `resumo` do registro e a linha do catalogo mestre projetam o registro; em divergencia, prevalece o registro (PJ-02, PJ-03). Nenhuma afirmacao existe apenas no resumo (RG-01, IX-01). |

### 5.6 Evolucao

| Etapa | Regra |
|---|---|
| **Captura** | Qualquer papel propoe a DEP-KMS, com fonte, data e contexto. Proposta sem os tres e devolvida sem analise (MM-02) |
| **Validacao** | DEP-KMS classifica; **DEP-QAR verifica** classe, sensibilidade e conformidade a CT-15; DEP-GOV aprova a escrita em EST. Escrita em EST **sempre** exige ADR (FND-06 §3.1, MI-04) — este ADR autoriza a instancia inicial; afirmacao nova exige o instrumento da sua classe |
| **Revisao** | Por afirmacao, no gatilho declarado; e por artefato, na revisao estrutural. Revisao vencida e nao feita e achado de auditoria (FND-07 §8.1) |
| **Conflito** | CT-03. Entre afirmacoes, vence a de melhor evidencia; empate escala (FND-06 §7.1) |
| **Substituicao** | CT-10, append-first. O texto anterior nunca desaparece |
| **Expiracao** | `ttl` vencido sem renovacao expira a afirmacao. `inferred` nao confirmada expira por CT-08. Registro nunca recuperado ao longo de um horizonte e candidato a poda (RC-05) |
| **Retirada** | CT-19 |

| # | Regra |
|---|---|
| **CT-25** | **Fato duravel e estado de projeto nao se misturam.** O registro em EST guarda o que sobrevive ao projeto da semana; estado corrente vive em **OPR** e expira por padrao (FND-06 §3.4, §4). Afirmacao com prazo curto e erro de camada, nao registro valido. |
| **CT-26** | **Dividir em novos artefatos exige ≥ 2 sinais observados** (SE-02), entre: reuso por consumidor que ignora o resto (S3), autoridade distinta (S6), baixa precisao de recuperacao (S5) ou custo de contexto acima do dobro da mediana do tipo (S7, CE-05). **Ganho previsto nao autoriza divisao** (SE-01). |
| **CT-27** | **Promocao deste contrato a documento fundacional** tem gatilho declarado e e **C3**: (a) segunda instancia `MEM-EST` sobre o Soberano; (b) segundo consumidor formal do contrato; ou (c) sinal S5 observado. Ate la, promover seria antecipacao (FND-08 §7.1). |

### 5.7 Limites — o que este contrato **nao** faz

| Nao faz | Por que |
|---|---|
| Nao cria entidade | Reprovado no Teste de Entidade em TE-1, TE-4 e TE-6 ([RFC-0007 §9.1](../rfcs/RFC-0007-conhecimento-sobre-o-soberano.md)). `Contexto do Soberano` e **conteudo** de `MEM` e **termo** de FND-03 §8 |
| Nao cria clone, persona ou representacao do Soberano | Nao ha entidade, Carta nem autonomia; `MEM` nao age (E-20) |
| Nao cria agente, subagente, skill, comando, workflow, produto, projeto ou ferramenta | PI-12 exige Carta; nenhuma e criada |
| Nao cria codigo, banco, ontologia, Reasoning Framework nem programa de migracao | Nenhum gatilho observado; G1–G3 de FND-10 §3.4 reexaminados e **nenhum disparado** |
| Nao faz perfil psicologico nem diagnostico | **CT-15 item 8**, proibicao expressa |
| Nao transforma preferencia em principio | CT-04, CT-12 |
| Nao substitui o ADR como fonte de decisao | CT-05 |
| Nao ratifica nada | Ratificacao exige ato explicito e datado do Soberano (CV-09, LM-02 a LM-06). Este ADR e C2/Tipo 2 e **nao carrega** ratificacao de nenhuma outra decisao |

### 5.8 Instancia autorizada

Autoriza-se **um** registro: [`MEM-EST-0001-contexto-do-soberano`](../memory/estrategica/MEM-EST-0001-contexto-do-soberano.md),
em `memory/estrategica/`, sob `TPL-memoria`. **Um**, e nao um por categoria: dividir exigiria
dois sinais observados e ha **zero** (CT-26, SE-02).

> **CT-28 — o registro nasce em `aprovado`, nao em `ativo`.** [FND-10 §10.3](../foundation/10-artifact-framework.md)
> atribui ao **SOBERANO** a ratificacao de Memoria EST, enquanto §2.2 exige o campo
> `ratificacao` apenas de artefato **de decisao** C3/Tipo 1 — a mesma divergencia registrada
> como achado **C2** de [REV-CONSOLIDACAO §2](../foundation/revisao-arquitetural-consolidacao-2026-07-28.md),
> agora reincidente sobre um **segundo** tipo. Autorizar a criacao **nao** e autorizar a
> entrada em vigor: aplica-se **GV-03** — na duvida, a classe mais alta —, e o registro
> permanece `aprovado` com `ratificacao: pendente` ate ato explicito e datado do Soberano.
> **Nao se escolhe uma leitura da divergencia**: adota-se a mais restritiva, e C2 continua a
> ser resolvida pelo seu proprio dono e gatilho. Estado `aprovado` **pode ser referenciado**
> (FND-03 §5) — os pacotes de §5.5 e seus custos medidos valem desde ja.

## 6. Justificativa

A Alternativa A vence pelos tres criterios bloqueantes; B falha em C3 e C6; C distorce o escopo
de FND-06.

**Por que a autoridade herdada vale mais que a declarada.** As Alternativas B e C precisariam
**escrever** que o Contexto nao supera a norma, dentro de um instrumento que — pela hierarquia
de FND-01 §10 — esta acima dos ADRs. Seria pedir a norma que se autolimite. A Alternativa A
coloca o conhecimento onde o limite **ja existe por construcao**: `MEM` nao obriga, e perde
para o ADR em conflito. **Uma regra que nao precisa ser obedecida para valer e melhor que uma
que precisa.**

**Por que nao criar FND-11 agora, apesar de a missao pedir "o framework".** Aponta-se a norma
exata, como PI-13 obriga: criar documento fundacional para dominio com **zero instancias
anteriores** contraria **SE-01** e **SE-02** (sinal observado obrigatorio, um sinal nao basta),
**FND-08 §7.1** (evolucao exige sinal, nao antecipacao) e **AQ-03** (abstracao com menos de
dois membros e suspeita) — e repetiria o defeito que **FIT-2026-003 R2** ja registrou como
divida. O tradeoff esta declarado, e o caminho de volta tambem: **CT-27** fixa tres gatilhos
que convertem a promocao de antecipacao em especializacao legitima.

**Tradeoff aceito, explicito.** O contrato fica em artefato **M1**: corrigi-lo exige ADR que o
supere, nao emenda de versao. Aceita-se porque um regime **sem nenhuma instancia anterior** tem
alta probabilidade de estar parcialmente errado — e, nesse estado, e melhor que seja barato
substituir por inteiro do que confortavel remendar por partes. O custo e conhecido: um rito de
superacao (FND-07 §7). O beneficio e que nenhuma versao intermediaria mal justificada se
acumula no acervo.

## 7. Impacto

| Dimensao | Impacto |
|---|---|
| Departamentos afetados | **DEP-GOV** (dono da camada EST, conformidade, acesso) · **DEP-KMS** (captura e curadoria) · **DEP-QAR** (verificacao de classe, sensibilidade e CT-15) |
| Componentes afetados | **Nenhum** — nao existe componente, e nenhum e criado |
| Entidades · arquetipos · relacoes · tipos documentais · camadas novas | **Zero · zero · zero · zero · zero** |
| Camadas de memoria a atualizar | **EST** — primeiro registro formal, previsto pelo indice da propria camada |
| Decisoes superadas | **Nenhuma** |
| Documentos a atualizar | [FND-06](../foundation/06-arquitetura-memoria.md) v1.3.0 (§3.1) · [FND-03](../foundation/03-taxonomia.md) v1.5.0 (§8) · [`memory/README.md`](../memory/README.md) · [`memory/estrategica/README.md`](../memory/estrategica/README.md) · catalogo mestre · `README.md` da raiz |
| Custo e dependencia criados | 27 regras · 1 registro · 0 dependencias externas · 0 arquivos do acervo reescritos alem dos emendados |
| Ganho PI-14 | **Reducao de contexto** — a comprovar por medicao de pacote; e **organizacao**, ja verificavel: quatro classes de autoridade que hoje se confundem passam a ter fronteira escrita |

## 8. Evidencias

| # | Evidencia | Origem (ID) | Confianca | O que ela discrimina |
|---|---|---|---|---|
| E1 | A camada EST **ja** declara como seu conteudo *"padroes duraveis de preferencia do Soberano"* e *"restricoes permanentes impostas pelo Soberano"*, desde a v1.0.0 | [FND-06 §3.1](../foundation/06-arquitetura-memoria.md) | **Alta — verificavel** | Elimina B e C: o lugar ja existe, e nao precisa ser criado |
| E2 | `MEM` tem autoridade normativa **nenhuma**; em conflito com ADR vigente, o ADR vence | [FND-09 §5.7, E-20](../foundation/09-meta-model.md); MM-07 | **Alta — verificavel** | Sustenta C1 de forma **estrutural**; e a razao pela qual A vence |
| E3 | O acervo converteu instrucao generica em autoridade **uma vez**, com severidade alta | [INC-2026-001 §1, §2](../governance/incidents/INC-2026-001-ratificacao-inferida.md) | **Alta — verificavel** | Elimina a Alternativa Z: o risco e observado, nao teorico |
| E4 | Abstracao com menos de dois membros ja foi registrada como divida neste acervo | [FIT-2026-003 §F3 e R2](../governance/fitness/FIT-2026-003-consolidacao-baseline.md) | **Alta — verificavel** | Elimina B pelo criterio bloqueante C3 |
| E5 | Regime normativo inteiro instituido por ADR C2 tem precedente **duplo e vigente** | [ADR-0007 §5](ADR-0007-fronteira-greenfield-legado.md) *(FR-01 a FR-10)*; [ADR-0008](ADR-0008-uma-fonte-multiplas-projecoes.md) *(PJ-01 a PJ-06)* | **Alta — verificavel** | Sustenta a forma escolhida e a classificacao C2 |
| E6 | A camada EST tem **zero** registros formais, e seu indice declara que surgirao quando houver conhecimento fora da Fundacao | [`memory/estrategica/README.md`](../memory/estrategica/README.md) | **Alta — verificavel** | Confirma que a instancia nao duplica nada existente (MM-01) |

**Evidencia ausente, declarada (VD-05).** Tres ausencias, nenhuma omitida:

| # | O que **nao** se sabe | Por que nao se pode saber hoje |
|---|---|---|
| A1 | Se os quatro pacotes de §5.5 sao o recorte certo | **Nao ha consumidor real.** Nenhum componente existe. O primeiro carregamento por um papel que nao seja a propria execucao de missao ainda nao ocorreu |
| A2 | Se as 27 regras sao a quantidade certa | Nenhuma foi exercida por terceiro. A mesma ressalva que [FIT-2026-002 R1](../governance/fitness/FIT-2026-002-artifact-framework.md) mantem aberta sobre 40 regras anteriores |
| A3 | Se o conhecimento registrado e **suficiente** para orientar uma decisao real | So se observa quando uma decisao for tomada com ele. Afirmar suficiencia agora seria LV-05 |

## 9. Riscos e mitigacao

| # | Risco | Probabilidade | Impacto | Mitigacao prevista |
|---|---|---|---|---|
| R1 | Registro sobre uma pessoa **virar norma na pratica**, apesar de nao ter autoridade | Media | **Alto** | CT-01 a CT-05 e CT-12; a subordinacao e estrutural (E-20), nao declarativa. Gatilho de revisao: primeira vez que uma afirmacao for invocada como fundamento de decisao |
| R2 | **Inferencia disfarcada de fato** | Media | **Alto** | CT-07 e CT-08; `unknown` obrigatorio; `inferred` nao orienta e expira sem confirmacao |
| R3 | **Dado sensivel indevido** entrar no acervo | Baixa | **Alto** | CT-15, lista **fechada**, verificada por DEP-QAR; CT-17 remove imediatamente e abre incidente |
| R4 | Contrato em M1 encarecer a evolucao | Media | Medio | Aceito e declarado (§6). CT-27 declara o caminho de promocao |
| R5 | Pacotes mal desenhados fazerem todo mundo carregar tudo | Media | Medio | CT-20 torna o carregamento **declarado e auditavel**; A1 esta declarada como evidencia ausente, e o gatilho de revisao e o primeiro consumidor real |
| R6 | Afirmacao de **fonte externa ao acervo** ser tratada como aprovada sem que o Soberano a tenha aprovado | **Media** | **Alto** | CT-11 obriga a declarar a fonte como externa; CT-19 permite retirada sem motivacao; o registro marca essas afirmacoes de forma distinguivel. **Residuo declarado em §12** |
| R7 | **Esta decisao estar errada** — o instrumento ser insuficiente e o regime precisar mesmo ser fundacional | Baixa | Medio | Reversao trivial (§10); CT-27 converte a promocao em movimento previsto, com sinal em vez de hipotese |
| R8 | O registro envelhecer sem que ninguem note | Media | Baixo | Gatilho de revisao **por afirmacao**; `ttl`; poda de nao recuperados (RC-05) |

## 10. Plano de reversao

| Campo | Conteudo |
|---|---|
| Como desfazer | ADR de revogacao superando este; [MEM-EST-0001](../memory/estrategica/MEM-EST-0001-contexto-do-soberano.md) passa a `revogado` **sem ser apagado** (MM-09, RB-05); as duas emendas MENOR saem de FND-06 §3.1 e FND-03 §8 |
| Custo da reversao | **Trivial** |
| Por que a reversao e trivial (Tipo 2) | Nao cria componente, entidade, arquetipo, relacao, tipo documental, camada, template nem dependencia externa. **Nao ha consumidor construido sobre a decisao** — nenhum componente existe. Nenhum artefato de terceiro precisa ser migrado |
| Janela | Permanente enquanto nao houver componente consumindo o Contexto. Apos o primeiro consumidor, reverter exige destino explicito para ele (EV-06) |
| Quem executa | DEP-GOV, sob aprovacao de DEP-EXE |
| Backup necessario (PI-07) | Nenhum — nenhum dado vivo e tocado, nenhum arquivo removido ou sobrescrito |

## 11. Classificacao

| Campo | Valor |
|---|---|
| Classe de mudanca | **C2 — Estrutural** |
| Tipo de reversibilidade | **Tipo 2** |
| Decisor | DEP-EXE, com parecer de DEP-GOV |
| Ratificador | **Nao aplicavel** — C2/Tipo 2 (FND-04 §2.2, FND-07 §2.3) |
| Data da decisao | 2026-07-28 |
| Data de vigencia | 2026-07-28 |

> **Por que C2 e nao C3.** C3 exige alterar principio imutavel, linha vermelha, hierarquia
> normativa, direitos de decisao ou **a propria Fundacao**. Nenhum ocorre: os dez documentos
> fundacionais permanecem dez, FND-01 §10 nao muda, e os direitos de decisao de FND-01 §7.3
> ficam **exatamente** como estao — o contrato os **referencia**, e CT-04 proibe expressamente
> que preferencia vire principio sem o rito da classe. A hipotese de C2 e literal: muda-se
> **padrao** (FND-04 §2). **GV-03 foi aplicado e nao alterou o resultado**: a duvida existiria
> se algum documento entrasse ou saisse da Fundacao, e a Alternativa B — a unica que o faria —
> foi recusada por outro motivo, em §4.
>
> **Por que Tipo 2 e nao Tipo 1.** Dois indicadores de FND-07 §2.1 foram examinados, nao
> ignorados. *"Mudanca de norma"*: presente, mas as duas emendas sao **MENOR e remissivas** —
> revoga-las nao obriga a migrar nada. *"Qualquer coisa que outros passarao a assumir como
> dado"*: e o indicador que mais pesa, e a mitigacao e estrutural — **cada afirmacao carrega
> classe e confianca** (CT-06), de modo que nada e consumido sem sua proveniencia, e
> `inferred` **nao orienta**. Alem disso, **nao existe nenhum "outro"**: zero componentes no
> sistema (verificado em [REV-CONSOLIDACAO §1.1](../foundation/revisao-arquitetural-consolidacao-2026-07-28.md)).
> O indicador **passa a valer no primeiro componente criado**, e por isso a criacao do primeiro
> componente e gatilho de revisao declarado (§12).

## 12. Revisao

| Campo | Conteudo |
|---|---|
| Gatilho por evento | **Primeiro componente criado** — reavaliar a classificacao Tipo 2 e verificar se os quatro pacotes servem a um consumidor que nao seja a propria execucao de missao (A1, R5) |
| Gatilho por evento | **Primeira vez que uma afirmacao for invocada como fundamento de decisao** — verificar se CT-01 foi respeitada, ou se o Contexto operou como norma (R1) |
| Gatilho por evento | **Primeira afirmacao `inferred` registrada** — verificar se CT-08 impediu a promocao sem confirmacao (R2) |
| Gatilho por evento | Qualquer gatilho de **CT-27** — avaliar promocao a documento fundacional |
| Gatilho temporal | 2027-01-28 — revisao semestral da Fundacao |
| Sinal de que esta decisao deu errado | (a) Uma afirmacao de classe 3 ou 4 aparecer citada como fundamento vinculante em qualquer artefato — o contrato tera falhado no seu unico proposito; (b) o registro ser sempre carregado inteiro, tornando os quatro pacotes decorativos; (c) `unknown` desaparecer do registro sem que nenhuma evidencia nova tenha entrado — sinal de preenchimento por inferencia |
| **Residuo declarado** | **R6 nao esta integralmente mitigado.** Afirmacoes de fonte externa ao acervo — instrucao permanente do Soberano ao ambiente de execucao — sao registradas como `stated` com a fonte declarada, mas **este ADR nao pode, por si, tornar essa fonte "aprovada"**. Ate ato do Soberano em contrario, elas valem como evidencia de nivel 8 (FND-01 §10) e permanecem candidatas preferenciais a retirada (CT-19). Registrado aqui em vez de omitido (PI-10) |
| Responsavel pela revisao | DEP-QAR |

## 13. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Origem | [RFC-0007](../rfcs/RFC-0007-conhecimento-sobre-o-soberano.md); determinacao do Soberano na abertura da **Missao 1.5** |
| Decisoes superadas | Nenhuma |
| Decisoes relacionadas | [ADR-0001](ADR-0001-adocao-da-fundacao-organizacional.md) — a Fundacao permanece a unica fonte normativa · [ADR-0006](ADR-0006-adocao-do-enterprise-artifact-framework.md) — contrato de artefato aplicado ao registro · [ADR-0007](ADR-0007-fronteira-greenfield-legado.md) — forma de regime por ADR C2; FR-04 sustenta CT-11 · [ADR-0008](ADR-0008-uma-fonte-multiplas-projecoes.md) — CT-24 aplica PJ-02 e PJ-03 · [ADR-0009](ADR-0009-o-que-conta-como-emenda-de-artefato.md) — AC-08 rege as emendas desta missao |
| Artefatos criados | [MEM-EST-0001](../memory/estrategica/MEM-EST-0001-contexto-do-soberano.md) |
| Artefatos alterados | FND-06 v1.3.0 · FND-03 v1.5.0 · `memory/README.md` · `memory/estrategica/README.md` · catalogo mestre · `README.md` da raiz · indices |
| Registros de memoria gerados | **EST** — [MEM-EST-0001](../memory/estrategica/MEM-EST-0001-contexto-do-soberano.md). Nenhum registro APR: esta decisao nao decorre de falha vivida |
| Verificacao de aptidao | [FIT-2026-004](../governance/fitness/FIT-2026-004-conhecimento-do-soberano.md) (QG-6, CV-07) |
| Revisao arquitetural | [REV-SOBERANO-2026-07-28](../foundation/revisao-arquitetural-conhecimento-do-soberano-2026-07-28.md) (FT-01) |

---

## Checklist de validade (FND-07 §4.1)
- [x] VD-01 — 3 alternativas reais + "nao fazer nada"
- [x] VD-02 — criterios declarados antes das alternativas (§3 antes de §4)
- [x] VD-03 — nenhuma alternativa de palha: B e o que a missao literalmente sugeriu; C e a solucao de menor custo aparente
- [x] VD-04 — tradeoff aceito explicito (§6)
- [x] VD-05 — tres ausencias de evidencia declaradas (§8)
- [x] VD-06 — reversao declarada trivial, com justificativa (Tipo 2)
- [x] VD-07 — impacto em cascata mapeado e executado (§7)
- [x] VD-08 — data e responsavel presentes
- [x] VD-09 — gatilhos de revisao definidos, com residuo declarado (§12)

## Checklist de projecao (PJ-05, `TPL-documento`)
Percorridas **28** tabelas deste ADR. Nenhuma reproduz tabela normativa de outra fonte:
§3 e §4 sao sintese declarada de [RFC-0007](../rfcs/RFC-0007-conhecimento-sobre-o-soberano.md)
§4 e §5, com a fonte nomeada no cabecalho de cada uma; §5.3, §5.4 e §5.5 sao **conteudo
original deste ADR**, e as normas que invocam entram por **referencia**, nunca por copia.
Uma reproducao foi **barrada antes da escrita**: a escala de sensibilidade de §5.4 ia receber
vocabulario proprio de tres valores; virou **CT-14**, que reusa a escala de FND-10 §2.2.
