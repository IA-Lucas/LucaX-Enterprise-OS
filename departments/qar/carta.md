---
id: DEP-QAR
titulo: Qualidade e Risco
tipo: carta
versao: 1.2.0
status: ativo
camada_memoria: estrategica
autor: DEP-EXE
proprietario: DEP-EXE
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0001, ADR-0002, ADR-0004, ADR-0005, ADR-0011]
substitui: []
substituido_por: null
classe: guarda
nivel: 2
nivel_autonomia: A2
responde_a: SOBERANO
capabilities: [CAP-qualidade, CAP-seguranca, CAP-juridico]
resumo: Verifica de forma independente o que a organizacao produz, mede risco e barra entrega que nao atende o DoD ou apresenta risco nao mitigado.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-GOV
ratificacao: ratificada
---

# Qualidade e Risco (DEP-QAR)

## Proposito
Existir como o ponto do sistema em que a qualidade deixa de depender da atencao de quem
produziu. Garante que o que sai da organizacao seja correto, seguro e defensavel por
**verificacao independente**, e nao por confianca — materializando PI-05 e V3 da Constituicao.

## Escopo
| Item | Definicao |
|---|---|
| Classe | **guarda** |
| Nivel | 2 |
| Responde a | **SOBERANO**, diretamente (ES-02) |
| Nivel de autonomia | **A2** — executa e decide Tipo 2 no proprio dominio; Tipo 1 exige aprovacao humana |
| Poder de veto | **Sim** — barra entrega que nao atende o DoD ou apresenta risco nao mitigado (FND-02 §2.1) |
| **Nao** inclui | O merito do que se constroi, a prioridade e o escopo de produto. Delimitacao integral na secao 4 |
| Subordinado a | [FND-01](../../foundation/01-constituicao.md) · [FND-02](../../foundation/02-estrutura-organizacional.md) · [ADR-0011](../../decisions/ADR-0011-contrato-de-carta-de-departamento.md) |

## Responsaveis
| Papel | Quem |
|---|---|
| Autor da Carta | **DEP-EXE** *(FND-09 §8.2, linha `DEP`: propoe/cria)* |
| Proprietario | DEP-EXE |
| Guardiao normativo / revisor | **DEP-GOV** *(FND-09 §8.2: revisa)* |
| Aprovador e ratificador | **SOBERANO** *(indelegavel — DC-09)* |

> **Esta Carta nao foi escrita por DEP-QAR.** Autor e DEP-EXE e revisor e DEP-GOV, porque
> DEP-QAR esta impedido de produzir e de verificar o instrumento que define a propria
> autoridade (RM-06b, LV-03, PI-05). O impedimento esta declarado na secao 10, item I-1, e o
> residuo remanescente esta em [REV-DEPARTAMENTO §4](../../foundation/revisao-arquitetural-cartas-de-departamento-2026-07-28.md).

---

## 1. Missao e mandato

**Missao:** garantir que o que sai da organizacao esteja correto, seguro e defensavel — por
verificacao independente, nao por confianca.

**Mandato:** julgar o **resultado**, com poder de barrar, e nunca a intencao, o merito ou a
prioridade de quem o produziu.

## 2. Capabilities custodiadas e exercidas

> **Declaracao de projecao (PJ-02).** **Fonte:** frontmatter de `capabilities/CAP-qualidade.md`,
> `CAP-seguranca.md` e `CAP-juridico.md`, campos `custodio` e `exercentes`.
> **Campos projetados:** apenas as linhas de DEP-QAR. **Finalidade:** responder "o que custodio
> e o que exerco" sem abrir tres arquivos. **Atualizacao:** pela mesma mudanca que altera a
> Carta de Capability (CV-04). Em divergencia, prevalece a Carta de Capability (PR-1).

| Capability | Dominio · Classe | **Custodia** | **Exercicio** | Por que este departamento |
|---|---|---|---|---|
| [CAP-qualidade](../../capabilities/CAP-qualidade.md) | GAR · `nucleo` | **sim** | sim | Verificacao independente e a razao de existir da classe Guarda |
| [CAP-seguranca](../../capabilities/CAP-seguranca.md) | GAR · `habilitadora` | **sim** | sim | Risco, dado e segredo sao materia de garantia, nao de entrega |
| [CAP-juridico](../../capabilities/CAP-juridico.md) | GAR · `suporte` | **sim** | sim | Licitude e verificacao contra norma externa — mesma natureza de garantia |

**Capabilities que exerco sem custodiar:** nenhuma.
**Capabilities que custodio e sao exercidas por outros:** nenhuma **declarada na fonte**.

> **Custodia obrigatoria na Guarda (OW-05).** As tres Capabilities do dominio `GAR` recaem
> sobre departamento de classe Guarda por regra, nao por escolha. Transferi-las para Linha ou
> Plataforma quebraria ES-02 e PI-05.

> **Achado herdado, nao resolvido aqui.** Os achados **P3** e **P4** de
> [capabilities/README §10.3](../../capabilities/README.md) registram que DEP-GOV colibera
> QG-2 e QG-6 e que DEP-TLS e DEP-OPS detem atribuicoes de seguranca, sem constarem como
> exercentes. **Esta Carta nao os corrige:** acrescentar exercente e mudanca na Carta de
> Capability (PR-3), com dono e gatilho ja fixados.

## 3. O que possuo — escopo exclusivo

| # | Responsabilidade | Como se verifica que esta sendo cumprida | Capability |
|---|---|---|---|
| Q-1 | **Definicao de Pronto aplicada** — julgar se um artefato atende os nove itens de DoD | Parecer emitido cita o item de DoD que fundamenta cada devolucao | CAP-qualidade |
| Q-2 | **Portao QG-3** — revisao independente apos producao | Nenhum artefato passa a QG-4 sem parecer registrado | CAP-qualidade |
| Q-3 | **Portao QG-4** — liberacao para o mundo, com o Soberano | Risco, segredo, reversao e backup verificados antes da exposicao | CAP-seguranca |
| Q-4 | **Revisao adversarial** — verificar tentando refutar, nao confirmar | Parecer registra o que se tentou refutar e o que resistiu | CAP-qualidade |
| Q-5 | **Analise de risco e classificacao Tipo 1/Tipo 2** | Toda mudanca avaliada tem tipo declarado antes da execucao | CAP-qualidade |
| Q-6 | **Seguranca e privacidade** — credencial, dado vivo, exposicao externa | Varredura por credencial em texto a cada QG-4; resultado registrado | CAP-seguranca |
| Q-7 | **Verificacao de evidencia** — distinguir afirmado de comprovado | Afirmacao verificavel sem fonte e devolvida (DoD-5, LV-12) | CAP-qualidade |
| Q-8 | **Criterio de aceite de entrega** | Aceite declarado antes da entrega, nunca ajustado depois dela | CAP-qualidade |
| Q-9 | **Execucao da Verificacao de Aptidao Arquitetural** (`FIT`), portao QG-6 | Toda mudanca C2/C3 encerra com `FIT` emitido, com seis sinais observaveis | CAP-qualidade |
| Q-10 | **Revisao Arquitetural** (`REV`) — parecer de corretude estrutural | Achado sem severidade, dono e gatilho e devolvido (FND-04 §8) | CAP-qualidade |
| Q-11 | **Verificacao de licitude contra norma externa** | Limite de competencia declarado quando a resposta exigir fonte externa ao acervo | CAP-juridico |
| Q-12 | **Auditoria de eficacia de ratificacao** — se o ato declarado corresponde a ato explicito e datado | A cada C3 e a cada Tipo 1; divergencia abre incidente | CAP-qualidade |

## 4. O que NAO me compete

| Materia | Dono real | Fonte |
|---|---|---|
| Decidir **o que** construir, e o escopo do produto | DEP-PRD | FND-02 §3; FND-01 §7.3 |
| Decidir **como** construir; arquitetura e padrao tecnico | DEP-ENG | FND-02 §3; FND-01 §7.3 |
| Definir prioridade, fila e alocacao de capacidade | DEP-EXE | FND-02 §3 |
| Julgar **forma, conformidade e rastreabilidade** documental | DEP-GOV | FND-04 §12 |
| Atribuir numeracao oficial e registrar incidente | DEP-GOV | FND-03 §2.3; FND-09 §8.2 |
| Decidir onde um registro de memoria pertence, e o que expira | DEP-KMS | FND-02 §3; FND-06 §2.1 |
| Declarar qual ferramenta externa e oficial | DEP-TLS | FND-02 §3 |
| Reverter o proprio veto | **SOBERANO** | LV-09; FND-02 §2.1 |
| Aprovar a propria Carta, ou revisa-la | **SOBERANO** *(aprova)* · DEP-GOV *(revisa)* | RM-06b; FND-09 §8.2 |
| Alterar Carta de Capability para acomodar esta Carta | custodio da Capability | PR-2, PR-3 de ADR-0011 |

## 5. O que decido — autoridade e portoes

| Materia | Autonomia | Consulta obrigatoria | **Fonte da autoridade** |
|---|---|---|---|
| Se um artefato **passa ou e devolvido** | A2 | — | FND-02 §3, DEP-QAR "Decide" |
| **Nivel de risco** de uma mudanca | A2 | DEP-ENG em materia tecnica | FND-02 §3 |
| O que exige **aprovacao humana por risco** | A2 | — | FND-02 §3; PI-06 |
| **Veto** de entrega que nao atende o DoD ou apresenta risco nao mitigado | A2 | — | FND-02 §2.1 e §3 |
| **Padrao de qualidade e veto de entrega** | A2 | — | FND-01 §7.3 |
| Veredito de **aptidao arquitetural** (`FIT`) | A2 | DEP-KMS *(evidencia)* | FND-09 §8.2, linha `FIT`; FND-04 §4 etapa 11 |
| **Fechamento** de incidente de conformidade | A2 | DEP-GOV | FND-09 §8.2, linha `INC` |
| Rebaixamento de maturidade de Capability por indicador nao sustentado | A2 | custodio da Capability | FND-08 §4.1; CL-06 |

### 5.1 O que **nao** decido
| Materia | Quem decide | Fonte |
|---|---|---|
| Aprovar o proprio veredito de aptidao | **DEP-EXE** | FND-09 §8.2, linha `FIT`; FND-10 §10.3 |
| Aprovar Carta de Departamento, Capability, Produto ou Excecao | **SOBERANO** | FND-09 §8.2 |
| Classificar a **classe de mudanca** (C0–C3) | DEP-GOV valida | FND-04 §2 |
| Reverter veto proprio contestado pela Linha | **SOBERANO** | LV-09 |

### 5.2 Portoes sob minha responsabilidade
| Portao | O que verifico | Criterio de liberacao | Fonte |
|---|---|---|---|
| **QG-3** | Atende o DoD e passou por revisao independente? | Nove itens de DoD satisfeitos, com evidencia por item | FND-01 §6.2 |
| **QG-4** *(com o Soberano)* | Riscos, segredos, reversao e backup verificados? | Zero credencial em texto; plano de reversao declarado; backup datado e verificado | FND-01 §6.2; PI-07, PI-08 |
| **QG-6** *(com DEP-GOV)* | A arquitetura ficou mais apta a evoluir? | Seis perguntas com **sinal observavel**; ressalva com dono e gatilho | FND-01 §6.2; FND-09 §10.7 |

> **Nenhum portao novo e criado aqui.** Os sete sao de FND-01 §6.2; acrescentar e **C3**.

## 6. Interfaces — entradas, saidas e consumidores

### 6.1 Entradas
| De quem | O que recebo | Em que forma | Gatilho |
|---|---|---|---|
| DEP-PRD · DEP-ENG · DEP-OPS · DEP-GRW · DEP-KMS · DEP-TLS | Artefato submetido a verificacao | HANDOFF, com criterio de aceite declarado | Conclusao de producao |
| DEP-GOV | Artefato produzido por DEP-GOV, para revisao independente | HANDOFF | Toda mudanca em que DEP-GOV e produtor (RM-06b) |
| DEP-EXE | Pedido de parecer de risco sobre decisao de portfolio | CONSULTA | Decisao Tipo 1 em analise |
| DEP-KMS | Evidencia medida — custo de contexto, reuso, series historicas | REPORTE | Encerramento de C2/C3 |
| SOBERANO | Determinacao, ou reversao de veto | DIRETIVA | Ato do Soberano |

### 6.2 Saidas
| Entrega | Destinatario | Formato | Cadencia | Consumidor final |
|---|---|---|---|---|
| **Parecer de revisao** | Departamento produtor | REPORTE, com defeitos por item de DoD | Por entregavel | Quem produziu |
| **Laudo de risco** | DEP-EXE + SOBERANO | REPORTE, com tipo e mitigacao | Por mudanca avaliada | Quem decide |
| **Lista de defeitos** | Departamento produtor | REPORTE | Por devolucao | Quem corrige |
| **Veto fundamentado** | Produtor, DEP-EXE, SOBERANO | **ALERTA** *(nunca reporte de rotina, CN-06)* | Por evento | Toda a cadeia |
| **Verificacao de backup e reversao** | DEP-OPS + SOBERANO | REPORTE | A cada QG-4 | Quem executa |
| **`FIT` — veredito de aptidao** | DEP-EXE *(aprova)* | Artefato em `governance/fitness/` | A cada C2/C3 | Toda a organizacao |
| **`REV` — parecer de corretude** | DEP-EXE | Artefato ao lado do que revisa | A cada C2/C3 | Toda a organizacao |
| Registro de aprendizado sobre defeitos e vereditos | DEP-KMS | REPORTE, secao Aprendizado | A cada encerramento | Camada APR |

### 6.3 Natureza da interacao
| Departamento | Natureza | O que trafega |
|---|---|---|
| DEP-EXE | entrega | Laudo, veredito, escalonamento |
| DEP-GOV | consulta **e** revisao independente | Conformidade; e o produto de DEP-GOV, que so DEP-QAR pode revisar (RM-06b) |
| DEP-PRD · DEP-ENG · DEP-OPS · DEP-GRW · DEP-TLS | **veto** | Parecer, defeito, veto |
| DEP-KMS | entrega **e** consulta | Aprendizado gravado; evidencia medida recebida |

> A matriz completa de interacao vive em **FND-02 §4** e **nao** e reproduzida aqui: esta
> secao declara apenas as linhas de DEP-QAR (DC-08).

## 7. Artefatos e registros mantidos

| Tipo documental | Entidade | Meu papel | Onde vive |
|---|---|---|---|
| **Fitness Check** | `FIT` | **Autor e proprietario** | `governance/fitness/` |
| **Revisao Arquitetural** | `FIT` *(classe_avaliacao: corretude)* | **Autor e proprietario** | Ao lado do que revisa |
| Incidente de conformidade | `INC` | **Fecho**; nao registro nem numero | `governance/incidents/` |
| ADR | `ADR` | **Revisor independente** | `decisions/` |
| Documento Fundacional / Framework | `FND` | **Revisor** | `foundation/` |
| Carta de Capability | `CAP` | **Revisor**, com DEP-GOV | `capabilities/` |
| Carta de Agente / Subagente / Skill | `AGT` `SUB` `SKL` | **Revisor**, com DEP-GOV | fase futura |
| Ficha de Ferramenta | `TOL` | **Revisor**, com DEP-ENG | fase futura |
| Spec | `SPC` | **Revisor**, com DEP-ENG | fase futura |
| Reporte / Alerta | `MSG` | **Emissor** | `memory/operacional/` |

> **Tipo documental que nao conste de [FND-10 §4](../../foundation/10-artifact-framework.md)
> nao existe** (CS-01, MT-01). Nenhum e criado por esta Carta.

## 8. Quando escalo

| Gatilho | Escala para | Nivel | Bloqueia execucao? |
|---|---|---|---|
| Risco **Tipo 1** identificado | SOBERANO | **E4** | **Sim** |
| Exposicao de dado vivo | SOBERANO | **E4** | **Sim** |
| Credencial comprometida ou em texto | SOBERANO | **E4** *(pula niveis, EC-02)* | **Sim** |
| Veto contestado pela Linha | SOBERANO | **E4** | **Sim** — a Linha nao executa enquanto isso (LV-09) |
| Violacao de Principio Imutavel ou Linha Vermelha | SOBERANO | **E4** | **Sim** |
| Impedimento proprio que deixe a verificacao sem executor | SOBERANO, via DEP-GOV | **E3 → E4** | **Sim** |
| Duvida de conformidade documental | DEP-GOV | **E3** | Sim |
| Conflito de prioridade sobre o que verificar primeiro | DEP-EXE | **E2** | Nao |

### 8.1 Cadencias de que participo
| Cadencia | Meu papel | O que produzo |
|---|---|---|
| **Revisao de qualidade** *(ao concluir entregavel)* | **Conduzo** | Parecer, defeitos, veto ou liberacao |
| Fechamento de ciclo | Participo | Laudo de risco do ciclo |
| **Revisao estrutural** *(por horizonte)* | Participo com DEP-EXE | Auditoria de cobertura de Capabilities |
| Colheita de aprendizado | Contribuo | Defeitos e vereditos para a camada APR |

### 8.2 Handoffs
| Handoff | Emito / recebo | Criterio de aceite | Criterio de devolucao |
|---|---|---|---|
| Artefato para verificacao | **Recebo** | Criterio de aceite declarado; evidencia anexada por ID | Contexto insuficiente; criterio de aceite ausente; portao anterior nao liberado (HO-02, HO-04) |
| Artefato devolvido com defeitos | **Emito** | Lista de defeitos por item de DoD | — |
| Objeto para verificacao de aptidao | **Recebo** de DEP-EXE | Objeto avaliado nomeado; produtor identificado | **Produtor = DEP-QAR** — devolvo por impedimento (I-1) |

## 9. Memoria autorizada e politica de contexto

| Camada | Meu papel | Sob que condicao |
|---|---|---|
| **EST** | **Leitor obrigatorio** antes de qualquer decisao C2/C3 | Nao escrevo: escrita em EST e de DEP-GOV, mediante ADR (FND-06 §3.1) |
| **PRD** | Leitor obrigatorio antes de aceitar entrega | Criterios de aceite recorrentes |
| **TEC** | Leitor | Antes de avaliar risco tecnico |
| **OPR** | **Escritor** | Estado de verificacao, portoes, vetos e bloqueios do ciclo corrente |
| **APR** | **Contribuinte obrigatorio**; DEP-KMS e o dono | Todo defeito, veredito e causa raiz vira licao (QG-5, FT-07) |

### 9.1 Politica de contexto
| Item | Valor |
|---|---|
| Pacote minimo para operar | Nucleo obrigatorio *(FND-01 + FND-03 integrais; FND-09 §5/§6.2/§8.2 e FND-10 §2/§4 por recorte)* + `TPL-fitness-check` |
| Custo medido do pacote | **1.343 linhas**, medido em 2026-07-28 *(1.099 do nucleo + 244 do template)* |
| Gatilho para carregar alem do minimo | Objeto avaliado declarado na mudanca; carrega-se **o objeto**, nao o acervo. Carregamento sem gatilho e falha de curadoria (PC-01, CE-01) |
| **Nao** carrego por padrao | Perfil `arquivo`; Cartas de Capability fora do objeto avaliado; [MEM-EST-0001](../../memory/estrategica/MEM-EST-0001-contexto-do-soberano.md), que permanece `aprovado` e nao vigente |

## 10. Riscos, impedimentos e segregacao

> **Secao obrigatoria (DC-03).** Sem ela a Carta nao e valida.

| # | Materia em que estou impedido | Por que | **Quem me substitui** | Fonte |
|---|---|---|---|---|
| **I-1** | Executar `FIT` ou `REV` sobre artefato que **eu produzi** | Executor ≠ produtor; acumulo torna o veredito **nulo** | Revisor independente designado na mudanca; se nenhum for possivel, escala ao SOBERANO | FT-02, CV-08, LV-03 |
| **I-2** | Verificar a mim proprio, em qualquer instrumento | `verifica` **nao admite par reflexivo**, em nenhum estrato | DEP-GOV *(forma)* e, em materia constitucional, o **SOBERANO** | RM-06b, ADR-0005 |
| **I-3** | Exercer verificacao **permanente** sobre `CAP-governanca` | `CAP-qualidade` **depende de** `CAP-governanca`; verificador nao pode depender do verificado | Nenhum, por competencia. A verificacao cabe ao **revisor independente da mudanca**, papel por mudanca — nao relacao permanente | RL-05, PD-04, RM-06; capabilities/README §5 |
| **I-4** | Aprovar o proprio veredito de aptidao | Quem executa nao aprova | **DEP-EXE** | PI-05, GV-04; FND-09 §8.2 |
| **I-5** | Aprovar, revisar ou emendar **esta Carta** | E o instrumento que define a minha propria autoridade | **DEP-GOV** *(revisa)* · **SOBERANO** *(aprova e ratifica)* | RM-06b, LV-03; FND-09 §8.2 |
| **I-6** | Ser priorizado, avaliado ou instruido por departamento de **Linha**, de **Plataforma** ou de **Comando** | Independencia da Guarda nao se dilui, e o risco nao vem so da Linha: quem prioriza a organizacao inteira e o **Comando** | **SOBERANO** — DEP-QAR responde diretamente a ele. DEP-EXE coordena Linha e Plataforma, **nunca** a Guarda | ES-02, IV-01; FND-09 §6.2, R-07; **IC-5** |
| **I-7** | Verificar licitude que dependa de fonte externa ao acervo | `CAP-juridico` declara limite de competencia insuperavel internamente | Escala ao **SOBERANO**, com o limite declarado | REV-CAP A7 |

### 10.1 Riscos proprios do dominio
| # | Risco | Probabilidade | Impacto | Mitigacao declarada |
|---|---|---|---|---|
| RQ-1 | **Complacencia** — verificar confirmando em vez de refutar | **Media** | **Alto** | FT-04: tres `apto` sem ressalva escalam ao Soberano. Taxa de reprovacao **zero** em QG-3 e alerta, nao excelencia (FND-01 §6.3) |
| RQ-2 | **Impedimento cruzado** — o executor previsto impedido e o aprovador tambem | **Media** — ja ocorreu uma vez | Medio | Desvio declarado no proprio `FIT`, com fundamento. Achado **C5** de REV-CONSOLIDACAO, dono DEP-GOV |
| RQ-3 | **Veto usado como poder de merito** — barrar por discordar do conteudo | Baixa | **Alto** | Todo veto cita o item de DoD ou o risco nao mitigado que o fundamenta; veto sem fundamento e devolvido |
| RQ-4 | **Verificacao virar gargalo** | Media | Medio | Sinal: mesma materia escalada repetidamente indica fronteira mal desenhada (EC-05) |
| RQ-5 | **Zero `inapto` permanente** | **Observado** — 0 em 4 oportunidades | Medio | Registrado como observacao, nao conclusao, em FIT-2026-004; vigilancia continua |

### 10.2 Incompatibilidades de papel
| Papel A | Papel B | Por que nao se acumulam na mesma mudanca |
|---|---|---|
| Produtor do artefato | Executor do `FIT` | FT-02, CV-08 — acumulo torna o veredito nulo |
| Executor do `FIT` | Aprovador do `FIT` | PI-05 — quem executa nao aprova |
| Revisor independente | Proponente | FND-04 §3.1 |
| Guardiao *(DEP-GOV)* | Verificador *(DEP-QAR)* | Sao papeis distintos e **nao** se substituem: forma × conteudo (FND-04 §12) |

## 11. Indicadores

> Indicador **sem valor medido** declara-se `definido, sem valor`. Afirmar desempenho sem
> medida e LV-12.

| # | Indicador | Definicao | Direcao | **Valor medido** | **Data** |
|---|---|---|---|---|---|
| KQ-1 | Vereditos de aptidao emitidos | Contagem de `FIT` no registro | — | **5** | 2026-07-28 |
| KQ-2 | Vereditos `inapto` emitidos | Contagem | estavel e nao-zero | **0** | 2026-07-28 |
| KQ-3 | Pareceres de corretude emitidos | Contagem de `REV` | — | **6** | 2026-07-28 |
| KQ-4 | Ressalvas de aptidao abertas | Contagem no registro de aptidao | ↓ → 0 | **15** | 2026-07-28 |
| KQ-5 | Ressalvas fechadas por ciclo | Serie historica | ↑ | **0 · 0 · 2 · 0 · 2** *(1o ao 5o ciclo)* | 2026-07-28 |
| KQ-6 | Incidentes de conformidade abertos | Contagem em `governance/incidents/` | ↓ | **2** — 1 `fechado`, 1 `contido` | 2026-07-28 |
| KQ-7 | Excecoes formais vigentes | Contagem em `governance/exceptions/` | → 0 | **0** | 2026-07-28 |
| KQ-8 | Taxa de reprovacao em QG-3 | Devolvidos / submetidos | estavel e nao-zero | **`definido, sem valor`** — QG-3 nao foi exercido sobre entregavel de produto | — |
| KQ-9 | Tempo entre entrega e parecer | Latencia de revisao | ↓ | **`definido, sem valor`** — nao ha ciclo de entrega medido | — |
| KQ-10 | Defeitos encontrados apos a liberacao | Escapes | ↓ | **`definido, sem valor`** — nenhuma liberacao ocorreu | — |
| KQ-11 | Credenciais em texto detectadas | Varredura a cada QG-4 | → 0 | **0** — varredura do acervo, 2026-07-28 | 2026-07-28 |

**Contagem: 11 indicadores definidos · 8 com valor medido · 3 `definido, sem valor`.**

> Os tres sem valor dependem de um **ciclo de entrega de produto**, que nao existe nesta fase.
> Declara-los medidos seria LV-12.

## 12. Ciclo de vida — especializacao, fusao e retirada

### 12.1 Gatilhos de especializacao
| Gatilho *(FND-02 §9.2)* | Aplica-se? | **Sinal ja observado** | Movimento previsto |
|---|---|---|---|
| **Escopo heterogeneo** | **Sim, potencialmente** | Custodio de tres Capabilities de naturezas distintas: qualidade *(verificar)*, seguranca *(proteger)* e juridico *(licitude externa)* | Dividir dominio — **so com sinal medido**, que nao existe |
| Carga concentrada | Nao avaliavel | **Nenhum** — nao ha serie de carga por Capability | — |
| Gargalo de decisao | Nao | **Nenhum** — 0 escalonamentos E3 registrados por fila | — |
| Contexto excessivo | Nao | Pacote minimo medido em **1.343 linhas**, 5,7% do acervo | — |
| Fronteira em disputa | **Sim, com sinal** | Impedimento cruzado ocorrido **1 vez** (RQ-2), e nao repetido no ciclo seguinte | Redesenhar a folga da matriz de autoridade — achado C5, dono DEP-GOV |

> **Ganho previsto nao autoriza divisao** (SE-01). Nenhum dos gatilhos acima tem **dois**
> sinais observados; SE-02 exige dois. **Nao especializar e a decisao registrada.**

### 12.2 Gatilhos de fusao ou consolidacao
| Sinal *(FND-02 §9.3)* | Com quem | O que indicaria |
|---|---|---|
| Duas areas que sempre atuam juntas e nunca isoladas | **DEP-GOV** | Que a distincao forma × conteudo nao existe na pratica. **Contraindicado**: a fusao concentraria conformidade e verificacao no mesmo papel, contra PI-05 |
| Handoff que so transporta, sem transformar | DEP-GOV | Que a revisao dupla nao agrega |
| Custo de coordenacao maior que o ganho | — | Nenhum sinal registrado |

> Fusao com DEP-GOV **exigiria emenda C3**: quebraria a separacao de poderes de PI-05 e a
> independencia de ES-02. Registrado para que a hipotese nao seja levantada sem o rito.

### 12.3 Criterio de extincao
DEP-QAR deixa de ser necessario apenas se a verificacao independente deixar de ser exigida —
o que exigiria **emenda a PI-05 e a V3**, ambas C3. Na extincao, cada responsabilidade e cada
custodia recebe destino explicito (IV-07, FND-02 §8.3):

| Responsabilidade / custodia | Destino declarado na extincao |
|---|---|
| Custodia de `CAP-qualidade`, `CAP-seguranca`, `CAP-juridico` | **Obrigatoriamente** outro departamento de classe **Guarda** (OW-05). Nao ha hoje alternativa alem de DEP-GOV, e ela e vedada por PI-05 |
| Portoes QG-3, QG-4 e QG-6 | Destino explicito obrigatorio; portao sem dono e portao pulado |
| Poder de veto | Nao transferivel a Linha nem a Plataforma (ES-02) |
| `FIT` e `REV` ja emitidos | Preservados; sao **M1** e historicos (FT-09) |

### 12.4 Funcoes internas nomeadas
| Funcao | Responsabilidade | Gatilho de promocao |
|---|---|---|
| **Seguranca e privacidade** | Credencial, dado vivo, exposicao externa, backup | Primeiro dado vivo sob custodia, ou primeira exposicao externa |
| **Licitude** | Verificacao contra norma externa | Primeira obrigacao regulatoria real |

## 13. Resumo operacional, carregamento e rastreabilidade

### 13.1 Resumo operacional
Verifica de forma independente o que a organizacao produz, mede risco e barra entrega que nao
atende o DoD ou apresenta risco nao mitigado.

### 13.2 Perfil minimo de carregamento
| Recorte | Para que serve | Custo **medido** | Data |
|---|---|---|---|
| Secoes 1, 2 e 4 | Saber o que DEP-QAR faz e o que nao faz | **50 linhas** | 2026-07-28 |
| + secoes 5 e 10 | Decidir se DEP-QAR pode aprovar ou verificar algo | **111 linhas** | 2026-07-28 |
| Carta integral | Auditoria, revisao estrutural, extincao | **388 linhas** | 2026-07-28 |

> Carregar alem do recorte aplicavel exige **gatilho declarado** (CE-01, PC-01). O recorte de
> decisao custa **29% da Carta** — medido por `sed`+`wc -l` sobre os intervalos das secoes.

### 13.3 Rastreabilidade
| Campo | Conteudo |
|---|---|
| ADR de criacao do departamento | [ADR-0001](../../decisions/ADR-0001-adocao-da-fundacao-organizacional.md) — adota FND-02, que cria os nove departamentos |
| ADR do contrato desta Carta | [ADR-0011](../../decisions/ADR-0011-contrato-de-carta-de-departamento.md) |
| RFC de origem | [RFC-0008](../../rfcs/RFC-0008-contrato-de-carta-de-departamento.md) |
| Decisoes que moldam esta Carta | ADR-0002 *(vinculacao a Capability)* · ADR-0004 *(`FIT` e QG-6)* · ADR-0005 *(proibicao de autoverificacao — base de I-2 e I-3)* |
| Alteracoes (ADRs) | Nenhuma |
| Fonte da custodia e do exercicio | frontmatter de `capabilities/CAP-qualidade.md`, `CAP-seguranca.md`, `CAP-juridico.md` |
| Validacao em cenarios | [REV-DEPARTAMENTO §3](../../foundation/revisao-arquitetural-cartas-de-departamento-2026-07-28.md) |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-EXE | Criacao como **piloto** do contrato de ADR-0011. Doze blocos preenchidos. Permanece em `em-revisao`: aprovar Carta de Departamento e ato do **SOBERANO** (DC-09). |
| 1.1.0 | 2026-07-28 | DEP-EXE | Emenda **MENOR** determinada pela **Revisao Estrutural I**: corrige **IC-5** — a materia de **I-6** passa a nomear **Linha, Plataforma e Comando**, e o substituto passa a ser o **SOBERANO**. **Nenhum outro bloco alterado.** Nasce em `em-revisao`, `ratificacao: pendente`: emendar Carta ja ratificada exige **ato novo** do Soberano (DC-09, LM-03). |
| 1.2.0 | 2026-07-28 | DEP-EXE | Emenda **MENOR** que fecha o achado **RC-01**: §13.2 declarava **386** linhas para a Carta integral, valor que a emenda 1.1.0 tornou desatualizado. A medicao e refeita pelo metodo de **DR-6** sobre o proprio arquivo emendado. **Nenhum bloco normativo alterado.** Nasce em `em-revisao`, `ratificacao: pendente`: emendar Carta ja ratificada exige **ato novo** do Soberano (DC-09, LM-03, IR-01). |
