---
id: DEP-GOV
titulo: Governanca e Conformidade
tipo: carta
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-EXE
proprietario: DEP-EXE
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0001, ADR-0002, ADR-0005, ADR-0008, ADR-0009, ADR-0011, ADR-0012, ADR-0013]
substitui: []
substituido_por: null
classe: guarda
nivel: 2
nivel_autonomia: A2
responde_a: SOBERANO
capabilities: [CAP-governanca]
resumo: Mantem a integridade normativa do sistema e barra o que exista sem rastreabilidade, sem responsavel ou em violacao de norma vigente.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: ratificada
---

# Governanca e Conformidade (DEP-GOV)

## Proposito
Existir como o ponto em que a norma deixa de depender da boa vontade de quem a aplica.
Mantem a integridade normativa do sistema e garante que **nada exista sem rastreabilidade e
sem responsavel** — julgando **forma**, nunca merito, e materializando PI-02, PI-03 e V4 da
Constituicao.

## Escopo
| Item | Definicao |
|---|---|
| Classe | **guarda** |
| Nivel | 2 |
| Responde a | **SOBERANO**, diretamente (ES-02) |
| Nivel de autonomia | **A2** — executa e decide Tipo 2 no proprio dominio; Tipo 1 exige aprovacao humana |
| Poder de veto | **Sim** — bloqueia qualquer componente sem Carta, sem rastreabilidade ou em violacao de norma (FND-02 §2.1 e §3) |
| **Nao** inclui | O merito tecnico, o escopo de produto, a prioridade e o julgamento de qualidade do resultado. Delimitacao integral na secao 4 |
| Subordinado a | [FND-01](../../foundation/01-constituicao.md) · [FND-02](../../foundation/02-estrutura-organizacional.md) · [ADR-0011](../../decisions/ADR-0011-contrato-de-carta-de-departamento.md) |

## Responsaveis
| Papel | Quem |
|---|---|
| Autor da Carta | **DEP-EXE** *(FND-09 §8.2, linha `DEP`: propoe/cria)* |
| Proprietario | DEP-EXE |
| Guardiao normativo / revisor | **DEP-QAR** *(desvio declarado — ver nota)* |
| Aprovador e ratificador | **SOBERANO** *(indelegavel — DC-09)* |

> **Esta Carta nao foi escrita nem revisada por DEP-GOV — e o desvio e o motivo de ela ser a
> quinta.** A matriz de FND-09 §8.2 atribui a **revisao** de `DEP` a DEP-GOV; aqui DEP-GOV e o
> **objeto**, e revisar o instrumento que define a propria autoridade e vedado (RM-06b, LV-03,
> PI-05). A revisao independente cabe a **DEP-QAR**, unico departamento de Guarda que nao e
> objeto desta Carta. O impedimento esta declarado na secao 10, itens **I-3** e **I-7**, e o
> residuo que ele fecha e o achado **RE-03** de
> [REV-ESTRUTURAL-I §9](../../foundation/revisao-estrutural-01-2026-07-28.md).

---

## 1. Missao e mandato

**Missao:** manter a integridade normativa do sistema e garantir que nada exista sem
rastreabilidade e sem responsavel.

**Mandato:** julgar **forma, conformidade e rastreabilidade**, com poder de barrar — e nunca o
merito, a prioridade nem a qualidade do resultado, que pertencem a outros.

## 2. Capabilities custodiadas e exercidas

> **Declaracao de projecao (PJ-02).** **Fonte:** frontmatter de
> `capabilities/CAP-governanca.md`, campos `custodio` e `exercentes`.
> **Campos projetados:** apenas as linhas de DEP-GOV. **Finalidade:** responder "o que custodio
> e o que exerco" sem abrir o arquivo da Capability. **Atualizacao:** pela mesma mudanca que
> altera a Carta de Capability (CV-04). Em divergencia, prevalece a Carta de Capability (PR-1).

| Capability | Dominio · Classe | **Custodia** | **Exercicio** | Por que este departamento |
|---|---|---|---|---|
| [CAP-governanca](../../capabilities/CAP-governanca.md) | DIR · **`nucleo`** | **sim** | sim | Conformidade, rastreabilidade e integridade normativa sao a razao de existir da classe Guarda de forma |

**Capabilities que exerco sem custodiar:** nenhuma.
**Capabilities que custodio e sao exercidas por outros:** nenhuma **declarada na fonte**.

> **A assimetria e conhecida, medida e nao resolvida aqui — achado P7.** DEP-GOV custodia
> **uma** Capability, e ela **verifica as outras 22** (`capabilities/README §5`) e e
> **dependencia dura de quatro**. O maior alcance de verificacao do catalogo esta no
> departamento de **menor** custodia. O gatilho de P7 — *1a revisao estrutural* — **disparou e
> foi confirmado** como sinal de **escopo heterogeneo**
> ([REV-ESTRUTURAL-I §3.1](../../foundation/revisao-estrutural-01-2026-07-28.md)), e a
> resolucao dependia desta Carta. **A avaliacao esta em §12.1, e a decisao e nao dividir**,
> com custo declarado.

> **Custodia obrigatoria na Guarda (OW-05, OW-04).** `CAP-governanca` e `nucleo` do dominio
> `DIR`. Transferi-la para Linha ou Plataforma quebraria ES-02 e PI-05; transferi-la para
> departamento de Suporte violaria OW-04.

## 3. O que possuo — escopo exclusivo

| # | Responsabilidade | Como se verifica que esta sendo cumprida | Capability |
|---|---|---|---|
| G-1 | **Custodia da Constituicao e da Fundacao** — os 10 documentos normativos | Toda emenda tem instrumento, versao nova e versao anterior preservada (AL-04) | CAP-governanca |
| G-2 | **Taxonomia** — nomes, identificadores, estados e localizacao | Artefato fora do padrao e devolvido sem analise de merito (AC-06) | CAP-governanca |
| G-3 | **Registro e numeracao oficial de ADRs e RFCs** | Nenhum identificador duplicado; contador conferido contra os arquivos em disco | CAP-governanca |
| G-4 | **Cadastro de Cartas** — de Capability, Departamento, Agente, Produto e Projeto | Toda Carta existente consta do catalogo mestre (RG-02, DoD-7) | CAP-governanca |
| G-5 | **Registro de excecoes formais** | Toda excecao tem id, motivo, escopo, prazo e expiracao verificada (FND-01 §8.3) | CAP-governanca |
| G-6 | **Incidentes de conformidade** — deteccao, registro e numeracao | Violacao detectada gera incidente **antes** de a execucao prosseguir (LV-11) | CAP-governanca |
| G-7 | **Auditoria documental** — varredura de indices contra fontes | Divergencia encontrada vira achado com dono e gatilho, nunca ajuste silencioso (PJ-03, RG-03) | CAP-governanca |
| G-8 | **Catalogo mestre e baseline** — a projecao do acervo e sua impressao digital | Baseline emitida com evidencia reproduzivel; nova medicao recebe **identidade nova** (BL-02, BL-03) | CAP-governanca |
| G-9 | **Camada de memoria EST** — dono do conteudo | Escrita em EST **sempre** mediante ADR aprovado (FND-06 §3.1, MI-04) | CAP-governanca |
| G-10 | **Registro canonico do ato de ratificacao** — os tres hashes e o diff | Todo ato registra `H-A`, `H-N`, `H-P` e o diff exato (IR-07, IR-08) | CAP-governanca |
| G-11 | **Guarda dos templates** — a forma obrigatoria de cada tipo | Template alterado por C2 com ADR; forma nunca vincula conteudo normativo (E-16) | CAP-governanca |

> **Sao onze responsabilidades exclusivas sobre uma unica Capability.** FND-02 §3 declarava
> **sete**; a diferenca sao G-8, G-9, G-10 e G-11, todas atribuidas a DEP-GOV por norma
> posterior — ADR-0008, FND-06 §3.1, ADR-0012 e FND-09 §8.2 respectivamente. **A contagem de
> P7 esta desatualizada para menos**, e o registro fica aqui como achado **RC-04**.

## 4. O que NAO me compete

| Materia | Dono real | Fonte |
|---|---|---|
| Julgar **merito tecnico**, arquitetura ou padrao de implementacao | DEP-ENG | FND-02 §3; FND-01 §7.3 |
| Decidir **o que** construir e o escopo do produto | DEP-PRD | FND-02 §3; FND-01 §7.3 |
| Julgar se a entrega **passa** ou e devolvida; medir risco | DEP-QAR | FND-02 §3; QG-3 |
| Definir prioridade, fila, alocacao e cadencia | DEP-EXE | FND-02 §3 |
| Decidir **onde um registro pertence** e o que expira | DEP-KMS | FND-02 §3; FND-06 §2.1 |
| Declarar qual **ferramenta externa** e oficial | DEP-TLS | FND-02 §3 |
| Executar a **rotina operacional** e responder por incidente **operacional** | DEP-OPS | FND-02 §3 |
| Comunicar externamente em nome do sistema | DEP-GRW, com o SOBERANO | FND-02 §3; LV-08 |
| **Aprovar a propria Carta, ou revisa-la** | **SOBERANO** *(aprova)* · **DEP-QAR** *(revisa)* | RM-06b; FND-09 §8.2 |
| Reverter o proprio veto | **SOBERANO** | LV-09; FND-02 §2.1 |
| Alterar Carta de Capability para acomodar esta Carta | custodio da Capability | PR-2, PR-3 de ADR-0011 |
| **Emendar a Constituicao** — propor, sim; emendar, nao | **SOBERANO** | FND-01 §9, etapa 4 |

## 5. O que decido — autoridade e portoes

| Materia | Autonomia | Consulta obrigatoria | **Fonte da autoridade** |
|---|---|---|---|
| Se um artefato esta em **conformidade** | A2 | — | FND-02 §3, DEP-GOV "Decide" |
| **Qual instrumento** uma mudanca exige | A2 | DEP-EXE | FND-02 §3; FND-04 §2 |
| Se uma proposta **contraria norma vigente** | A2 | — | FND-02 §3 |
| **Veto** de componente sem Carta, sem rastreabilidade ou em violacao | A2 | — | FND-02 §2.1 e §3 |
| **Taxonomia e governanca** | A2 | DEP-EXE | FND-01 §7.3, "Taxonomia e governanca" |
| **Validar a classe de mudanca** (C0–C3) proposta | A2 | proponente | FND-04 §2 |
| **Numeracao oficial** de decisoes, propostas e incidentes | A2 | — | FND-09 §8.2, linhas `ADR`, `RFC`, `INC` |
| **Aprovar Template** | A2 | dono do tipo | FND-09 §8.2, linha `TPL` |
| **Registrar** incidente de conformidade | A2 | quem detectou | FND-09 §8.2, linha `INC` |
| **Aprovar** registro da camada **EST** | A2 | DEP-KMS | FND-09 §8.2, linha `MEM`: *"DEP-GOV se camada EST"* |
| **Homologar** estrutura da memoria e taxonomia de registro proposta por DEP-KMS | A2 | DEP-KMS | FND-01 §7.3, linha *Estrutura da memoria* — **`IR-11`: o termo e homologacao, nunca ratificacao** |
| **Validar a forma** de uma RFC | A2 | — | FND-09 §8.2, linha `RFC` |

### 5.1 O que **nao** decido
| Materia | Quem decide | Fonte |
|---|---|---|
| **Merito** de qualquer natureza — tecnico, de produto, de qualidade, de prioridade | ENG · PRD · QAR · EXE | FND-02 §3; FND-04 §12 |
| Se a entrega **passa** em QG-3 | **DEP-QAR** | FND-01 §6.2 |
| **Emenda a Constituicao** | **SOBERANO** | FND-01 §9 |
| Aprovar Carta de Departamento, Capability, Produto ou Excecao | **SOBERANO** | FND-09 §8.2 |
| Aprovar `FIT` | **DEP-EXE** | FND-09 §8.2, linha `FIT` |
| Reverter veto proprio contestado | **SOBERANO** | LV-09 |
| **Aprovar esta Carta** | **SOBERANO** | DC-09 |

### 5.2 Portoes sob minha responsabilidade
| Portao | O que verifico | Criterio de liberacao | Fonte |
|---|---|---|---|
| **QG-2** *(com DEP-ENG)* | As alternativas foram consideradas e a decisao esta **registrada**? | ADR presente, rastreavel, com instrumento correto para a classe — **a forma**, nunca o acerto tecnico | FND-01 §6.2 |
| **QG-6** *(com DEP-QAR)* | A arquitetura ficou mais apta a evoluir? — **pela forma** | `FIT` emitido, com executor distinto do produtor e ressalvas com dono e gatilho | FND-01 §6.2; FND-09 §10.7 |

> **Coliberar um portao nao e exercer a Capability do outro.** Em QG-2, DEP-GOV libera pela
> **forma** (`CAP-governanca`) e DEP-ENG pelo **merito** (`CAP-arquitetura`); em QG-6, DEP-GOV
> pela forma e DEP-QAR pelo merito (`CAP-qualidade`). Duas competencias, um portao — resolucao
> dos achados **P3** e **P5** em [REV-ESTRUTURAL-I §3.6](../../foundation/revisao-estrutural-01-2026-07-28.md).

> **Nenhum portao novo e criado aqui.** Os sete sao de FND-01 §6.2; acrescentar e **C3**.

## 6. Interfaces — entradas, saidas e consumidores

### 6.1 Entradas
| De quem | O que recebo | Em que forma | Gatilho |
|---|---|---|---|
| **Todos os departamentos** | Consulta de conformidade e de classe de mudanca | **CONSULTA** | Antes de propor mudanca C1 a C3 |
| Todos os departamentos | Artefato submetido a verificacao de forma | HANDOFF | Producao concluida |
| **Qualquer papel** | Violacao detectada | **ALERTA** *(obrigatorio, LV-11)* | Deteccao |
| DEP-QAR | Parecer de revisao independente sobre artefato que **eu** produzi | REPORTE | Toda mudanca em que DEP-GOV e produtor (RM-06b) |
| DEP-EXE | Pedido de parecer de forma sobre decisao de portfolio | CONSULTA | Decisao C2/C3 em analise |
| DEP-KMS | Proposta de estrutura de memoria e de taxonomia de registro | HANDOFF | Mudanca na arquitetura de memoria |
| **SOBERANO** | Ato de ratificacao, excecao formal, determinacao | **DIRETIVA** | Ato do Soberano |

### 6.2 Saidas
| Entrega | Destinatario | Formato | Cadencia | Consumidor final |
|---|---|---|---|---|
| **Parecer de conformidade** | Departamento proponente | REPORTE, com a norma exata citada | Por submissao | Quem propos |
| **Numeracao oficial** de ADR, RFC e INC | `decisions/` · `rfcs/` · `governance/incidents/` | Identificador atribuido | Por registro | Toda a organizacao |
| **Veto fundamentado** | Produtor, DEP-EXE, SOBERANO | **ALERTA** *(nunca reporte de rotina, CN-06)* | Por evento | Toda a cadeia |
| **Registro de excecao formal** | SOBERANO + solicitante | Artefato `EXC` | Por excecao | Quem opera sob ela |
| **Incidente de conformidade** | DEP-QAR *(que fecha)* + SOBERANO | Artefato `INC` | Por violacao | Toda a organizacao |
| **Auditoria documental** — varredura de indices contra fontes | DEP-EXE + SOBERANO | REPORTE, com achados | A cada C2/C3 e por horizonte | Quem corrige |
| **Catalogo mestre e baseline** | Toda a organizacao | Artefato `M3`, com impressao digital | A cada marco | Quem mede o acervo |
| **Registro canonico do ato de ratificacao** | Toda a organizacao | Artefato `MSG`, canal DIRETIVA | Por ato do Soberano | Quem verifica integridade |
| Emenda proposta a Fundacao | **SOBERANO** | `RFC` C3 + `ADR` candidato | Por gatilho de revisao | Quem ratifica |
| Aprendizado sobre conformidade | DEP-KMS | REPORTE, secao Aprendizado | A cada encerramento | Camada APR |

### 6.3 Natureza da interacao
| Departamento | Natureza | O que trafega |
|---|---|---|
| DEP-EXE | **entrega** | Parecer de forma, auditoria, escalonamento |
| **DEP-QAR** | **consulta e revisao independente recebida** | Forma × merito. **DEP-QAR e quem revisa o que DEP-GOV produz** (RM-06b) |
| DEP-PRD · DEP-ENG · DEP-OPS · DEP-GRW · DEP-TLS | **veto** | Conformidade, rastreabilidade, instrumento |
| DEP-KMS | **entrega e veto** | Aprendizado gravado; aprovacao de registro em EST; veto de forma |

> A matriz completa de interacao vive em **FND-02 §4** e **nao** e reproduzida aqui: esta
> secao declara apenas as linhas de DEP-GOV (DC-08).

## 7. Artefatos e registros mantidos

| Tipo documental | Entidade | Meu papel | Onde vive |
|---|---|---|---|
| **Constituicao** | `FND` | **Autor e custodio**; nunca aprovador nem ratificador | `foundation/` |
| **Documento Fundacional · Meta Model · Framework** | `FND` | **Autor e custodio** | `foundation/` |
| **ADR** | `ADR` | **Numera e registra**; autor quando a materia for de forma; **revisor** dos demais | `decisions/` |
| **RFC** | `RFC` | **Valida a forma**; autor quando a materia for de forma | `rfcs/` |
| **Excecao Formal** | `EXC` | **Revisor e registrador**; nunca aprovador | `governance/exceptions/` |
| **Incidente** | `INC` | **Registra e numera**; **nao fecho** — quem fecha e DEP-QAR | `governance/incidents/` |
| **Template** | `TPL` | **Autor com o dono do tipo, e aprovador** | `foundation/templates/` |
| **Catalogo mestre · baseline · indices** | `M3` derivado | **Autor e proprietario** | `governance/` e cada `README.md` |
| **Diretiva** — registro canonico de ato soberano | `MSG` | **Registra**; nunca emite | `memory/operacional/` |
| Memoria **EST** | `MEM` | **Dono da camada**; aprova o registro | `memory/estrategica/` |
| Carta de Capability · Departamento · Agente · Skill | `CAP` `DEP` `AGT` `SKL` | **Revisor**, exceto quando eu for o objeto | `capabilities/` · `departments/` |
| **Fitness Check · Revisao Arquitetural** | `FIT` | **Revisor de forma**; nunca autor | `governance/fitness/` |

> **Tipo documental que nao conste de [FND-10 §4](../../foundation/10-artifact-framework.md)
> nao existe** (CS-01, MT-01). Nenhum e criado por esta Carta.

## 8. Quando escalo

| Gatilho | Escala para | Nivel | Bloqueia execucao? |
|---|---|---|---|
| Violacao de **Principio Imutavel** ou **Linha Vermelha** | SOBERANO | **E4** | **Sim** |
| Pedido de **excecao formal** | SOBERANO | **E4** | **Sim** — so ele autoriza (FND-01 §8.3) |
| **Proposta de emenda** a Fundacao | SOBERANO | **E4** | **Sim** — sem ratificacao a emenda nao existe |
| **Divergencia de `H-N`** apos ato de ratificacao | SOBERANO, via incidente | **E4** *(pula niveis, EC-02)* | **Sim** (IR-05) |
| Credencial em texto detectada em auditoria | SOBERANO, via DEP-QAR | **E4** | **Sim** |
| Veto proprio contestado | SOBERANO | **E4** | **Sim** — a area nao executa (LV-09) |
| **Impedimento proprio que deixe a verificacao de forma sem executor** | SOBERANO, via DEP-QAR | **E3 → E4** | **Sim** |
| Duvida de **qualidade ou risco** — nao de forma | DEP-QAR | **E3** | Sim |
| Conflito de prioridade sobre o que auditar primeiro | DEP-EXE | **E2** | Nao |
| Duvida rotineira de taxonomia resolvivel por premissa | ninguem — **decide e registra a premissa** | **E0** | Nao |

### 8.1 Cadencias de que participo
| Cadencia | Meu papel | O que produzo |
|---|---|---|
| **Fechamento de ciclo** *(com DEP-EXE)* | **Conduzo a parte de auditoria** | Reporte de conformidade, excecoes vencidas |
| **Revisao estrutural** *(por horizonte)* | **Conduzo a forma** *(FND-02 §9.4)* | Registro da revisao, achados, varredura de indices |
| **Revisao da Fundacao** *(semestral, com o SOBERANO)* | **Conduzo** | Emendas propostas, aderencia verificada |
| Abertura de ciclo | Participo | Validacao de classe de mudanca em QG-0 |
| Colheita de aprendizado | Contribuo | Causas de nao conformidade para a camada APR |

### 8.2 Handoffs
| Handoff | Emito / recebo | Criterio de aceite | Criterio de devolucao |
|---|---|---|---|
| Artefato para verificacao de **forma** | **Recebo** | Frontmatter completo, tipo documental declarado, vinculo a Capability presente | Campo obrigatorio ausente; tipo nao declarado em FND-10 §4; vinculo invalido (AC-06, VC-01) |
| **Parecer de conformidade** | **Emito** | Norma exata citada por identificador | — |
| **Artefato que eu produzi, para revisao independente** | **Emito** a DEP-QAR | Objeto nomeado; papel de produtor declarado | **Revisor = DEP-GOV** — devolvo por impedimento (I-1) |
| Proposta de estrutura de memoria | **Recebo** de DEP-KMS | Camada identificada, proveniencia declarada | Registro sem `origem` (FM-04); duplicacao entre camadas (MM-01) |

> **Handoff devolvido duas vezes pelo mesmo motivo escala a DEP-EXE** — ha defeito de
> fronteira (HO-03, FND-02 §9.2).

## 9. Memoria autorizada e politica de contexto

| Camada | Meu papel | Sob que condicao |
|---|---|---|
| **EST** | **Dono da camada** e **unico escritor** | Escrita **sempre** mediante ADR aprovado (FND-06 §3.1, MI-04). **Ser dono da camada nao e exercer `CAP-conhecimento`** — resolucao de **P2** |
| **PRD** | Leitor | Auditoria de proveniencia |
| **TEC** | Leitor | Auditoria de proveniencia |
| **OPR** | **Escritor** | Excecoes vigentes, estado de portoes, achados de auditoria do ciclo corrente |
| **APR** | **Contribuinte obrigatorio**; DEP-KMS e o dono | Toda causa de nao conformidade vira licao (QG-5, DR-8) |

### 9.1 Politica de contexto
| Item | Valor |
|---|---|
| Pacote minimo para operar | Nucleo obrigatorio *(FND-01 + FND-03 integrais; FND-09 §5/§6.2/§8.2 e FND-10 §2/§4 por recorte)* + o **artefato submetido** |
| Custo medido do pacote | **1.099 linhas** de nucleo, medido em 2026-07-28, mais o artefato submetido |
| Gatilho para carregar alem do minimo | **Auditoria documental ou revisao estrutural**, que tocam o acervo por definicao. O custo desse carregamento e o maior medido do sistema — **6.176 linhas**, 20% delas de indices ([FIT-2026-007 §F5.1](../../governance/fitness/FIT-2026-007-revisao-estrutural-i.md)) |
| **Nao** carrego por padrao | O acervo inteiro; as 23 Cartas de Capability; perfil `arquivo`. **Carregar tudo e a falha de curadoria mais provavel deste departamento**, e esta declarada como risco RG-4 |

## 10. Riscos, impedimentos e segregacao

> **Secao obrigatoria (DC-03).** Sem ela a Carta nao e valida.

| # | Materia em que estou impedido | Por que | **Quem me substitui** | Fonte |
|---|---|---|---|---|
| **I-1** | Verificar, revisar ou aprovar **artefato que eu produzi** | `verifica` **nao admite par reflexivo**, em nenhum estrato | **DEP-QAR** — revisor independente da mudanca | RM-06b, ADR-0005, LV-03 |
| **I-2** | **Revisar Carta de Departamento de cuja revisao estrutural eu fui autor** | FND-02 §9.4 me torna **produtor** da revisao estrutural; revisar depois a Carta que a revisao avaliou acumula produtor e revisor | **DEP-QAR** *(revisao)*; se DEP-QAR tambem estiver impedido, **SOBERANO** | **RE-03** de REV-ESTRUTURAL-I §9; FT-02, CV-08 |
| **I-3** | **Aprovar, revisar ou emendar esta Carta** | E o instrumento que define a minha propria autoridade | **DEP-QAR** *(revisa)* · **SOBERANO** *(aprova e ratifica)* | RM-06b, LV-03; FND-09 §8.2 |
| **I-4** | **Julgar merito** — tecnico, de produto, de qualidade, de risco ou de prioridade | Julgo **forma**; merito e de outros. Confundir os dois converte guarda em gargalo | DEP-ENG · DEP-PRD · DEP-QAR · DEP-EXE, conforme a materia | FND-02 §3; FND-04 §12 |
| **I-5** | **Escrever na camada EST sem ADR aprovado** | Ser dono da camada nao dispensa o instrumento | O rito: ADR aprovado antes da escrita | FND-06 §3.1, MI-04 |
| **I-6** | Ser priorizado, avaliado ou instruido por departamento de **Linha**, de **Plataforma** ou de **Comando** | Independencia da Guarda nao se dilui, e o risco nao vem so da Linha: quem prioriza a organizacao inteira e o **Comando** | **SOBERANO** — DEP-GOV responde diretamente a ele. DEP-EXE coordena Linha e Plataforma, **nunca** a Guarda | ES-02, IV-01; FND-09 §6.2, R-07; **IC-5**, por simetria com `DEP-QAR` **I-6** |
| **I-7** | **Executar `IR-09`** — o teste de reconstrucao — **sobre artefato que eu produzi ou registrei** | Quem registra o ato nao pode ser a unica prova de que o registro esta integro | **DEP-QAR** executa; DEP-GOV **confere** de forma independente | **RC-02**; IR-09 de ADR-0012 |
| **I-8** | **Emendar a Constituicao ou qualquer documento fundacional sem o instrumento da classe** | Propor e meu; emendar exige o rito, e C3 exige o **Soberano** | **SOBERANO** *(etapa 4 de FND-01 §9)* | FND-01 §9; FND-04 §2 |
| **I-9** | **Fechar incidente de conformidade** | Registro e numero sao meus; **fechar e de DEP-QAR** | **DEP-QAR** | FND-09 §8.2, linha `INC` |
| **I-10** | **Corrigir a fonte para que o indice ou a soma feche** | O defeito e sempre da vista derivada, nunca da fonte | Correcao na projecao; divergencia vira **achado** | PJ-03, RG-03, M3; **PR-2** |
| **I-11** | **Editar baseline ja emitida**, ou artefato **M1** | Baseline nunca e editada; `FIT`, `REV`, `ADR` aprovado e `MSG` nao se alteram | Nova medicao com **identidade nova**; correcao por **superacao** | BL-02; LV-04; MEM-APR-0003 |
| **I-12** | **Alterar Carta de Capability** para acomodar esta Carta ou um indice | A fonte prevalece sobre a projecao | Rito de FND-08 §6.3 | PR-2, PR-3 de ADR-0011; PJ-03 |

### 10.1 Riscos proprios do dominio
| # | Risco | Probabilidade | Impacto | Mitigacao declarada |
|---|---|---|---|---|
| RG-1 | **Guarda de forma virar gargalo de merito** — devolver por discordar do conteudo | Media | **Alto** | Todo parecer cita a **norma exata por identificador**; parecer sem norma citada e ele proprio devolvido (I-4) |
| RG-2 | **O ponto cego medido:** a auditoria confere **projecao contra fonte** e **nao confere a fonte contra si mesma** | **Observado — 4 ocorrencias** *(IC-8, RE-04, RE-05, RE-07)* | **Alto** | G-7 passa a exigir **somar as tabelas da fonte**, nao apenas compara-las com a projecao — acao de [MEM-APR-0002](../../memory/aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md), dono DEP-GOV |
| RG-3 | **Contencao tomada por solucao** — `IR-11` conter IC-2 e a emenda nunca ocorrer | **Media** | Medio | Risco **RR-3** de RFC-0009, quarto ciclo. Mitigado nesta missao: o texto da emenda existe em [RFC-0011](../../rfcs/RFC-0011-emenda-constitucional-ratifica-homologa.md) e falta **so o ato** |
| RG-4 | **Falha de curadoria de contexto no proprio departamento** — carregar o acervo por habito | **Media** | Medio | §9.1 declara o gatilho; o custo de auditoria e o **maior medido** do sistema e por isso e o que mais exige recorte (CE-01, PC-01) |
| RG-5 | **Concentracao de papeis criticos sem alternativa estrutural** — DEP-GOV produz a revisao estrutural e revisa quase tudo | **Observado — 5 ocorrencias sem Carta** | **Alto** | Esta Carta e a mitigacao possivel: declara **I-1**, **I-2** e **I-7**. O residuo so desaparece quando existirem **agentes** (IC-3) |
| RG-6 | **Assimetria de custodia** — 1 Capability custodiada, 22 verificadas | **Observado** | Medio | Achado **P7**, avaliado em §12.1. **Nao dividir**, com custo declarado |

### 10.2 Incompatibilidades de papel
| Papel A | Papel B | Por que nao se acumulam na mesma mudanca |
|---|---|---|
| Produtor do artefato | Verificador de forma do mesmo artefato | RM-06b, LV-03 — `verifica` nao tem par reflexivo |
| **Autor da revisao estrutural** | **Revisor da Carta que ela avaliou** | **RE-03** — e o impedimento **I-2**, criado por esta Carta |
| Registrador do incidente | Quem o fecha | FND-09 §8.2, linha `INC` — registro e de GOV, fechamento e de QAR |
| Registrador do ato de ratificacao | Executor de `IR-09` sobre o mesmo ato | **RC-02** — e o impedimento **I-7** |
| Guardiao *(DEP-GOV)* | Verificador *(DEP-QAR)* | Papeis distintos que **nao** se substituem: forma × conteudo (FND-04 §12) |
| Proponente de emenda | Ratificador da emenda | FND-01 §9 — propor e de GOV; ratificar e do **SOBERANO** |

## 11. Indicadores

> Indicador **sem valor medido** declara-se `definido, sem valor`. Afirmar desempenho sem
> medida e LV-12.

| # | Indicador | Definicao | Direcao | **Valor medido** | **Data** |
|---|---|---|---|---|---|
| KG-1 | Decisoes registradas | Contagem de `ADR-*.md` em `decisions/` | — | **14** | 2026-07-28 |
| KG-2 | Propostas registradas | Contagem de `RFC-*.md` em `rfcs/` | — | **11** | 2026-07-28 |
| KG-3 | Incidentes de conformidade abertos | Contagem com `situacao` ≠ `fechado` | → 0 | **0** — os 2 do sistema estao `fechado` | 2026-07-28 |
| KG-4 | Excecoes formais vigentes | Contagem em `governance/exceptions/` | → 0 | **0** | 2026-07-28 |
| KG-5 | Documentos fundacionais sob custodia | Contagem em `foundation/` | estavel | **10** | 2026-07-28 |
| KG-6 | Templates sob guarda | Contagem em `foundation/templates/` | estavel | **19** | 2026-07-28 |
| KG-7 | Cartas cadastradas no catalogo | Capability + Departamento | ↑ ate 9/9 | **23 `CAP` · 9 `DEP`** | 2026-07-28 |
| KG-8 | Baselines emitidas | Contagem em `artifact-registry §10` | ↑ | **6** — `BL-01` a `BL-06` | 2026-07-28 |
| KG-9 | **Links relativos quebrados no acervo** | Varredura de todos os links `.md` | → 0 | **0** | 2026-07-28 |
| KG-10 | **Ocorrencias de autoverificacao** | Papel de quem verifica = papel de quem produziu | → 0 | **0** | 2026-07-28 |
| KG-11 | **Credenciais em texto** | Varredura do acervo | → 0 | **0** | 2026-07-28 |
| KG-12 | Divergencias catalogo × fonte encontradas e corrigidas | Contagem por missao | ↓ | **4 na Missao 1.8** *(IC-8, RE-04, RE-05, RE-07)* | 2026-07-28 |
| KG-13 | **Defeitos da fonte contra si mesma** — o ponto cego de RG-2 | Contagem acumulada | ↓ | **4** | 2026-07-28 |
| KG-14 | Emendas a Fundacao propostas e **nao** ratificadas | Contagem de `ADR` candidato sem ato | → 0 | **1** — [ADR-0014](../../decisions/ADR-0014-candidato-emenda-fnd-01-7-3-homologa.md) | 2026-07-28 |
| KG-15 | Taxa de devolucao por forma | Devolvidos / submetidos | estavel e nao-zero | **`definido, sem valor`** — nao ha fila de submissao medida | — |
| KG-16 | Tempo entre violacao detectada e incidente registrado | Latencia | ↓ | **`definido, sem valor`** — 2 ocorrencias, ambas registradas na mesma missao da deteccao; serie insuficiente | — |
| KG-17 | Cobertura de rastreabilidade | % de artefatos com frontmatter completo e valido | → 100% | **`definido, sem valor`** — a varredura por campo ainda nao foi executada artefato a artefato | — |

**Contagem: 17 indicadores definidos · 14 com valor medido · 3 `definido, sem valor`.**

> **Os catorze medidos descrevem o acervo, nao o desempenho.** Contar ADRs prova que o registro
> existe; **nao** prova que a governanca esta funcionando. Os tres sem valor sao exatamente os
> que mediriam desempenho — e dependem de fila real, serie temporal e varredura campo a campo
> que esta fase nao produziu. Declara-los medidos seria **LV-12**.

## 12. Ciclo de vida — especializacao, fusao e retirada

### 12.1 Gatilhos de especializacao
| Gatilho *(FND-02 §9.2)* | Aplica-se? | **Sinal ja observado** | Movimento previsto |
|---|---|---|---|
| **Escopo heterogeneo** | **Sim, confirmado** | **Onze** responsabilidades exclusivas sobre **uma** Capability (§3), de naturezas distintas: custodia normativa, taxonomia, numeracao, cadastro, excecao, incidente, auditoria, catalogo, memoria EST, hash de ato e templates. Achado **P7**, gatilho **disparado e confirmado** em REV-ESTRUTURAL-I §3.1 | Dividir dominio — candidato natural: separar **auditoria e catalogo** *(medicao)* da **custodia normativa** *(norma)* |
| **Carga concentrada** | **Sim, observado** | DEP-GOV produziu a forma de **1 de 1** revisao estrutural e revisa **22 de 23** Capabilities. **5 ocorrencias** de exercicio de papel critico sem Carta (R2 de FIT-2026-006) | Promover funcao a agente — **impossivel nesta fase**: criar agente e proibido |
| **Gargalo de decisao** | **Nao** | **0** escalonamentos E3 registrados por fila de conformidade | — |
| **Contexto excessivo** | **Sim, medido** | O pacote de auditoria e o **maior do sistema**: **6.176 linhas**, **21,3%** do acervo, dos quais **1.230 sao indices** | Recortar subagente — **impossivel nesta fase** |
| **Fronteira em disputa** | **Sim, com sinal** | **3 ocorrencias** do impedimento cruzado C5, a ultima em §0.1 de REV-ESTRUTURAL-I | Redesenhar a folga da matriz de autoridade — achado **C5**, dono DEP-GOV |
| Duplicacao | Nao | Toda exibicao de conteudo alheio esta declarada como projecao | — |
| Conhecimento ilhado | **Sim** | **1** autor para 5 Cartas; **1** departamento para toda a forma | Converter pratica em Skill — **impossivel nesta fase** |

> **Decisao registrada: nao especializar — e a decisao e desconfortavel.** **Cinco** gatilhos
> tem sinal observado, e SE-02 exige **dois**. O criterio de FND-02 §9.2 esta **satisfeito com
> folga**, e mesmo assim o movimento **nao se executa**, pelo motivo declarado em
> [REV-ESTRUTURAL-I §3.5](../../foundation/revisao-estrutural-01-2026-07-28.md): os movimentos
> que os gatilhos indicam — *promover funcao a agente* e *recortar subagente* — exigem **criar
> agente ou subagente**, expressamente proibido nesta fase; e *devolver direito de decisao*
> exige alterar **FND-09 §8.2**, que e **C3**.
>
> **Custo assumido, e visivel:** DEP-GOV permanece com onze responsabilidades sobre uma
> Capability, e a concentracao continua sendo a maior do sistema. **Gatilho de reexecucao:**
> existencia do **primeiro agente**, ou resolucao de **IC-3** — o que vier antes. Este e o
> registro por escrito que PI-14 regra 2 exige; sem ele, o custo ficaria invisivel.

### 12.2 Gatilhos de fusao ou consolidacao
| Sinal *(FND-02 §9.3)* | Com quem | O que indicaria |
|---|---|---|
| Duas areas que sempre atuam juntas e nunca isoladas | **DEP-QAR** | Que a distincao **forma × conteudo** nao existe na pratica. **Contraindicado e vedado**: a fusao concentraria conformidade e verificacao no mesmo papel, contra PI-05 e ES-02 — seria **emenda C3** |
| Handoff que so transporta, sem transformar | DEP-QAR | Que a revisao dupla nao agrega. **Sinal contrario observado**: os quatro achados de RG-2 sairam de DEP-GOV e foram revisados por DEP-QAR |
| Componente sem acionamento ao longo de um horizonte | — | **Nao avaliavel** — nenhum horizonte se tornou avaliavel sob `HZ-02` ([ADR-0013](../../decisions/ADR-0013-criterio-de-horizonte-e-consolidacao.md)) |
| Custo de coordenacao maior que o ganho | — | Nenhum sinal registrado |

> Fusao com DEP-QAR **exigiria emenda C3**. Registrado para que a hipotese nao seja levantada
> sem o rito.

### 12.3 Criterio de extincao
DEP-GOV deixa de ser necessario apenas se a rastreabilidade e a conformidade deixarem de ser
exigidas — o que exigiria **emenda a PI-02, PI-03 e V4**, todas C3. Na extincao, cada
responsabilidade e cada custodia recebe destino explicito (IV-07, FND-02 §8.3):

| Responsabilidade / custodia | Destino declarado na extincao |
|---|---|
| Custodia de `CAP-governanca` *(`nucleo`, dominio `DIR`)* | **Obrigatoriamente** departamento de classe **Guarda** e **nunca** de Suporte (OW-04, OW-05). Nao ha hoje alternativa alem de DEP-QAR, e ela e vedada por PI-05 |
| Portoes QG-2 e QG-6 *(coliberacao pela forma)* | Destino explicito obrigatorio; portao sem dono e portao pulado |
| **Camada de memoria EST** | Novo dono nomeado; a camada **nao** e apagada (MM-09) e continua exigindo ADR para escrita (MI-04) |
| Poder de veto | Nao transferivel a Linha nem a Plataforma (ES-02) |
| Numeracao oficial e catalogo mestre | Transferidos com o registro; identificadores **nunca** sao reatribuidos |
| `ADR`, `RFC`, `INC`, `EXC` e baselines ja emitidos | Preservados; sao **M1** e historicos (LV-04, BL-02) |

### 12.4 Funcoes internas nomeadas
> Responsabilidades hospedadas aqui que ainda nao merecem departamento proprio (ES-04).

| Funcao | Responsabilidade | Gatilho de promocao |
|---|---|---|
| **Auditoria e catalogo** | Varredura de indices contra fontes, catalogo mestre, baseline, medicao de acervo | **Primeiro agente criado**, ou custo de auditoria acima de **25%** do acervo em duas medicoes itemizadas consecutivas |
| **Integridade de ato** | Registro canonico de ratificacao, tres hashes, diff e conferencia de `IR-09` | **Terceiro ato de ratificacao** registrado sob ADR-0012 — **ja ocorrido**; a promocao aguarda existirem agentes |
| **Taxonomia** | Nomes, identificadores, estados e localizacao | Primeiro conflito de identificador registrado |

## 13. Resumo operacional, carregamento e rastreabilidade

### 13.1 Resumo operacional
Mantem a integridade normativa do sistema e barra o que exista sem rastreabilidade, sem
responsavel ou em violacao de norma vigente.

### 13.2 Perfil minimo de carregamento
| Recorte | Para que serve | Custo **medido** | Data |
|---|---|---|---|
| Secoes 1, 2 e 4 | Saber o que DEP-GOV faz e o que nao faz | **53 linhas** | 2026-07-28 |
| + secoes 5 e 10 | Decidir se DEP-GOV pode verificar ou vetar algo | **133 linhas** | 2026-07-28 |
| Carta integral | Auditoria, revisao estrutural, extincao | **457 linhas** | 2026-07-28 |

> Carregar alem do recorte aplicavel exige **gatilho declarado** (CE-01, PC-01). O recorte de decisao custa **29% da Carta** — medido por
> `sed`+`wc -l` sobre os intervalos das secoes.

### 13.3 Rastreabilidade
| Campo | Conteudo |
|---|---|
| ADR de criacao do departamento | [ADR-0001](../../decisions/ADR-0001-adocao-da-fundacao-organizacional.md) — adota FND-02, que cria os nove departamentos |
| ADR do contrato desta Carta | [ADR-0011](../../decisions/ADR-0011-contrato-de-carta-de-departamento.md) |
| RFC de origem | [RFC-0008](../../rfcs/RFC-0008-contrato-de-carta-de-departamento.md) |
| Decisoes que moldam esta Carta | ADR-0002 *(vinculacao a Capability)* · ADR-0005 *(proibicao de autoverificacao — base de I-1)* · ADR-0008 *(uma fonte, multiplas projecoes — base de I-10)* · ADR-0009 *(o que conta como emenda)* · ADR-0012 *(integridade do ato — base de G-10 e I-7)* · ADR-0013 *(criterio de horizonte — base de §12.2)* |
| Achado que esta Carta fecha | **IC-4** — *"DEP-GOV com dois papeis criticos sem Carta"* · **RE-03** — declarado em **I-2**, conforme a condicao de [FIT-2026-007 §Rollout](../../governance/fitness/FIT-2026-007-revisao-estrutural-i.md) |
| Achados que esta Carta **abre** | **RC-04** — a contagem de responsabilidades exclusivas de P7 esta desatualizada para menos: sao **11**, nao 7 |
| Alteracoes (ADRs) | Nenhuma |
| Fonte da custodia e do exercicio | frontmatter de `capabilities/CAP-governanca.md` |
| Validacao em cenarios | [REV-ROLLOUT §3](../../foundation/revisao-arquitetural-rollout-cartas-2026-07-28.md) |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-EXE | Criacao — **quinta Carta do sistema e a primeira do rollout**, escrita sozinha conforme a Condicao 1 de FIT-2026-006 e a decisao de [REV-ESTRUTURAL-I §6.1](../../foundation/revisao-estrutural-01-2026-07-28.md). Doze blocos preenchidos. Declara em **B9** o impedimento exposto por **RE-03** *(I-2)* e o exposto por **RC-02** *(I-7)*. Permanece em `em-revisao`: aprovar Carta de Departamento e ato do **SOBERANO** (DC-09). |
