---
id: DEP-OPS
titulo: Operacoes
tipo: carta
versao: 1.1.0
status: ativo
camada_memoria: estrategica
autor: DEP-EXE
proprietario: DEP-EXE
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-30
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0001, ADR-0002, ADR-0003, ADR-0011, ADR-0018, ADR-0025]
substitui: []
substituido_por: null
classe: linha
nivel: 2
nivel_autonomia: A2
responde_a: DEP-EXE
capabilities: [CAP-operacoes, CAP-infraestrutura]
resumo: Mantem em funcionamento o que ja existe e executa o trabalho recorrente com previsibilidade, backup verificado e continuidade.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-GOV
ratificacao: ratificada
---

# Operacoes (DEP-OPS)

## Proposito
Existir como o ponto em que o que foi construido continua funcionando. Mantem em operacao o
que ja existe, executa o trabalho recorrente com previsibilidade, e responde por **backup
verificado, incidente operacional e continuidade** — sem decidir o que muda no que opera.

## Escopo
| Item | Definicao |
|---|---|
| Classe | **linha** |
| Nivel | 2 |
| Responde a | **DEP-EXE** |
| Nivel de autonomia | **A2** — executa e decide Tipo 2 no proprio dominio; Tipo 1 exige aprovacao humana |
| Poder de veto | **Nao** — veto e exclusivo da classe Guarda (FND-02 §2.1) |
| **Nao** inclui | Mudanca estrutural do que opera, padrao de qualidade e prioridade de portfolio. Delimitacao integral na secao 4 |
| Subordinado a | [FND-01](../../foundation/01-constituicao.md) · [FND-02](../../foundation/02-estrutura-organizacional.md) · [ADR-0011](../../decisions/ADR-0011-contrato-de-carta-de-departamento.md) |

## Responsaveis
| Papel | Quem |
|---|---|
| Autor da Carta | **DEP-EXE** *(FND-09 §8.2, linha `DEP`: propoe/cria)* |
| Proprietario | DEP-EXE |
| Guardiao normativo / revisor | **DEP-GOV** *(FND-09 §8.2: revisa)* |
| Aprovador e ratificador | **SOBERANO** *(indelegavel — DC-09)* |

---

## 1. Missao e mandato

**Missao:** manter em funcionamento o que ja existe e executar o trabalho recorrente com
previsibilidade.

**Mandato:** decidir **como** a rotina e executada e **quando** se aciona incidente, com
autoridade sobre a operacao corrente — e nenhuma sobre **o que** muda no que se opera.

## 2. Capabilities custodiadas e exercidas

> **Declaracao de projecao (PJ-02).** **Fonte:** frontmatter de `capabilities/CAP-operacoes.md`
> e `CAP-infraestrutura.md`, campos `custodio` e `exercentes`.
> **Campos projetados:** apenas as linhas de DEP-OPS. **Finalidade:** responder "o que custodio
> e o que exerco" sem abrir dois arquivos. **Atualizacao:** pela mesma mudanca que altera a
> Carta de Capability (CV-04). Em divergencia, prevalece a Carta de Capability (PR-1).

| Capability | Dominio · Classe | **Custodia** | **Exercicio** | Por que este departamento |
|---|---|---|---|---|
| [CAP-operacoes](../../capabilities/CAP-operacoes.md) | SUS · `habilitadora` | **sim** | sim | Executar o recorrente com previsibilidade e o mandato integral desta area |
| [CAP-infraestrutura](../../capabilities/CAP-infraestrutura.md) | SUS · `habilitadora` | **sim** | sim | O que sustenta a execucao — disponibilidade, recuperacao e continuidade — e sustentacao, nao construcao |

**Capabilities que exerco sem custodiar:** nenhuma.
**Capabilities que custodio e sao exercidas por outros:** nenhuma **declarada na fonte**.

> **Exposicao declarada.** `CAP-operacoes` **depende de** `CAP-infraestrutura` *(que custodio)*
> e de `CAP-engenharia` *(custodia de DEP-ENG)*; `CAP-infraestrutura` **depende de**
> `CAP-arquitetura` *(DEP-ENG)*. **DEP-OPS depende integralmente de DEP-ENG** e nao o governa
> (AU-08, MT-09).

> **Verificar backup nao e custodiar `CAP-seguranca`.** FND-02 §3 atribui a DEP-OPS *"backups e
> sua verificacao"*, e `CAP-seguranca` declara `exercentes: [DEP-QAR]`. **Operar sob politica
> nao e custodiar a politica**: a politica de backup, retencao e recuperacao e definida e
> **verificada** por DEP-QAR; o que DEP-OPS exerce ao executar a rotina e `CAP-operacoes`.
> Resolucao do achado **P4** em
> [REV-ESTRUTURAL-I §3.6](../../foundation/revisao-estrutural-01-2026-07-28.md); **nenhuma
> Carta de Capability foi alterada** (PJ-03).

## 3. O que possuo — escopo exclusivo

| # | Responsabilidade | Como se verifica que esta sendo cumprida | Capability |
|---|---|---|---|
| O-1 | **Estado corrente de execucao** — o que esta em curso e o que esta bloqueado | A camada OPR reflete o estado real do ciclo, e o que expira nao e renovado sem justificativa | CAP-operacoes |
| O-2 | **Runbooks** — o procedimento escrito da rotina | Toda rotina recorrente tem runbook localizavel; rotina sem runbook e improviso | CAP-operacoes |
| O-3 | **Rotinas recorrentes** | Executadas com resultado registrado, nao com resultado presumido | CAP-operacoes |
| O-4 | **Monitoramento** | O sinal de falha chega **antes** do usuario, ou a ausencia disso esta declarada | CAP-infraestrutura |
| O-5 | **Incidentes operacionais** — acionamento, conducao e postmortem | Todo incidente encerra com postmortem que identifica **causa**, nao sintoma (FND-06 §3.5) | CAP-operacoes |
| O-6 | **Backups e sua verificacao** | **Copia datada e verificada** antes de toda acao destrutiva; sem copia, nao executa | CAP-infraestrutura |
| O-7 | **Suporte** — atendimento do que ja opera | Ordem de atendimento declarada; fila visivel | CAP-operacoes |
| O-8 | **Continuidade** — o que acontece quando algo para | Plano de continuidade declarado por componente operado, com tempo de recuperacao alvo | CAP-infraestrutura |
| O-9 | **Camada de memoria OPR** — dono do conteudo | Item que expira sem promocao e presumidamente irrelevante, e essa presuncao e desejada (FND-06 §3.4) | CAP-operacoes |

> **O-6 e a responsabilidade mais dura desta Carta.** PI-07 e LV-01 nao admitem excecao formal
> quando ha dado vivo: **sem copia datada e verificada, nao executa** — e quem verifica a copia
> e DEP-OPS, com **conferencia independente de DEP-QAR** a cada QG-4.

## 4. O que NAO me compete

| Materia | Dono real | Fonte |
|---|---|---|
| **Mudanca estrutural do que opero** — arquitetura, padrao tecnico, modelo de dados | DEP-ENG | FND-02 §3; FND-01 §7.3 |
| Decidir **o que** construir e o escopo do produto | DEP-PRD | FND-02 §3 |
| Definir **padrao de qualidade** e julgar se a entrega passa | DEP-QAR | FND-02 §3; QG-3 |
| **Definir e verificar** a politica de seguranca, privacidade e retencao | DEP-QAR | FND-02 §3; **P4** |
| Definir prioridade de **portfolio**, fila organizacional e alocacao | DEP-EXE | FND-02 §3 |
| Julgar forma, conformidade e rastreabilidade | DEP-GOV | FND-04 §12 |
| **Registrar e numerar incidente de conformidade** — distinto do operacional | DEP-GOV *(registra)* · DEP-QAR *(fecha)* | FND-09 §8.2, linha `INC` |
| Declarar qual **ferramenta externa** e oficial | DEP-TLS | FND-02 §3 |
| Decidir onde um registro de memoria pertence fora da camada OPR | DEP-KMS | FND-06 §2.1 |
| Comunicar externamente indisponibilidade ou incidente | DEP-GRW, com o **SOBERANO** | FND-01 §7.3; LV-08 |
| Alterar Carta de Capability para acomodar esta Carta | custodio da Capability | PR-2, PR-3 de ADR-0011 |
| **Aprovar a propria Carta, ou revisa-la** | **SOBERANO** *(aprova)* · **DEP-GOV** *(revisa)* | RM-06b; FND-09 §8.2 |

> **Incidente operacional × incidente de conformidade sao coisas distintas, e a distincao e
> desta secao.** O primeiro e meu: falha do que opera, com postmortem e causa. O segundo e
> **violacao de norma**, registrado por DEP-GOV e fechado por DEP-QAR (FND-04 §10). Um mesmo
> evento pode gerar os dois; **nenhum substitui o outro**.

## 5. O que decido — autoridade e portoes

| Materia | Autonomia | Consulta obrigatoria | **Fonte da autoridade** |
|---|---|---|---|
| **Como executar a rotina** | A2 | DEP-ENG *(quando tocar o que ele construiu)* | FND-01 §7.3, *Rotina operacional e runbooks*; FND-02 §3 |
| **Quando acionar incidente** operacional | A2 | — | FND-02 §3 |
| **Ordem de atendimento** operacional | A2 | DEP-EXE *(se conflitar com a fila)* | FND-02 §3 |
| Conteudo do **runbook** | A2 | DEP-ENG | FND-01 §7.3 |
| **Execucao e verificacao de backup** | A2 | DEP-QAR *(politica e conferencia)* | FND-02 §3; PI-07 |
| **Curadoria da camada OPR** — o que expira, o que e promovido | A2 | DEP-KMS *(alocacao entre camadas)* | FND-06 §2.1 e §3.4 |
| **Declarar indisponibilidade** interna | A2 | DEP-EXE | FND-02 §3 |

> **A homologacao de rotina operacional e runbooks e de DEP-EXE** (FND-01 §7.3). **`IR-11`:
> o termo e homologacao, nunca ratificacao** — ratificar e ato exclusivo do Soberano
> ([ADR-0012 §5.4](../../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md)).

### 5.1 O que **nao** decido
| Materia | Quem decide | Fonte |
|---|---|---|
| **Mudar o que opero** | **DEP-ENG** *(como)* · **DEP-PRD** *(o que)* | FND-01 §7.3 |
| Se a entrega passa em QG-3, e se o risco e aceitavel | **DEP-QAR** | FND-01 §6.2 |
| **Executar acao destrutiva sem backup verificado** | **Ninguem** — e proibido, sem excecao possivel | **PI-07, LV-01** |
| Expor dado vivo ao exterior | **SOBERANO** | FND-01 §7.3; LV-08 |
| Prioridade de portfolio | **DEP-EXE** | FND-02 §3 |
| **Aprovar esta Carta** | **SOBERANO** | DC-09 |

### 5.2 Portoes sob minha responsabilidade

**Nenhum.** Os sete portoes de FND-01 §6.2 sao liberados por **DEP-EXE** *(QG-0 e QG-1)*,
DEP-ENG + DEP-GOV *(QG-2)*, DEP-QAR *(QG-3, QG-4)*, DEP-KMS *(QG-5)* e
DEP-QAR + DEP-GOV *(QG-6)*.

> **DEP-OPS nao libera portao, e contribui evidencia para um.** A **verificacao de backup e
> reversao** que DEP-QAR exige em **QG-4** e executada por DEP-OPS e **conferida** por DEP-QAR
> (`DEP-QAR §6.2`). Executar a verificacao **nao e liberar o portao** — e a mesma distincao de
> P4, aplicada ao portao.

> **Nenhum portao novo e criado aqui.** Os sete sao de FND-01 §6.2; acrescentar e **C3**.

## 6. Interfaces — entradas, saidas e consumidores

### 6.1 Entradas
| De quem | O que recebo | Em que forma | Gatilho |
|---|---|---|---|
| **DEP-ENG** | Componente construido, desenho de arquitetura, criterio de operacao | **HANDOFF** | Liberacao de QG-3 |
| DEP-EXE | Prioridade, alocacao, briefing | DIRETIVA, com `nivel_autonomia_concedido` | Abertura de ciclo |
| DEP-QAR | Politica de seguranca e retencao; parecer de risco; **veto**; pedido de verificacao de backup | REPORTE ou **ALERTA** | QG-4 e por evento |
| DEP-GOV | Parecer de conformidade, classe de mudanca validada | CONSULTA | Antes de propor mudanca |
| DEP-TLS | Ferramenta oficial, limite de uso, referencia de acesso | REPORTE | Adocao aprovada |
| DEP-PRD | Criterio de aceite recorrente; escopo do que se opera | REPORTE | Definicao concluida |
| DEP-KMS | Pacote de contexto; licoes da camada APR sobre falhas conhecidas | REPORTE | QG-0 |
| **SOBERANO** | Determinacao sobre dado vivo ou continuidade | **DIRETIVA** | Ato do Soberano |

### 6.2 Saidas
| Entrega | Destinatario | Formato | Cadencia | Consumidor final |
|---|---|---|---|---|
| **Runbook** | Quem executa a rotina; DEP-ENG *(consulta)* | Artefato de rotina, na camada **OPR** | Por rotina | Quem opera |
| **Status operacional** | DEP-EXE | REPORTE | Por ciclo e por evento | Quem prioriza |
| **Registro e postmortem de incidente** | DEP-EXE, DEP-ENG, DEP-QAR | REPORTE + registro em **APR** | Por incidente | Quem corrige a causa |
| **Confirmacao de backup** | **DEP-QAR** *(confere)* + **SOBERANO** | REPORTE, com data e resultado da verificacao | A cada QG-4 e por rotina | Quem autoriza o risco |
| **Relatorio de continuidade** | DEP-EXE + SOBERANO | REPORTE, com tempo de recuperacao alvo | Por horizonte | Quem avalia exposicao |
| **Alerta de indisponibilidade ou perda de dado** | DEP-QAR, DEP-EXE, **SOBERANO** | **ALERTA** *(interrompe, CN-04)* | Por evento | Toda a cadeia |
| **Sinal de uso real** | **DEP-PRD** e DEP-ENG | **HANDOFF** | Continuo | Quem define e quem constroi |
| Aprendizado operacional | DEP-KMS | REPORTE, secao Aprendizado | A cada encerramento | Camada APR |

### 6.3 Natureza da interacao
| Departamento | Natureza | O que trafega |
|---|---|---|
| DEP-EXE | **entrega** | Status, continuidade, escalonamento |
| DEP-GOV | consulta | Conformidade — DEP-GOV **veta** DEP-OPS, nunca o inverso |
| DEP-QAR | consulta | Risco e politica — DEP-QAR **veta** DEP-OPS, nunca o inverso |
| **DEP-ENG** | **entrega e consulta** | Componente recebido de ENG; sinal de uso e incidente devolvidos |
| DEP-PRD | **consulta** | Sinal de uso real entregue; criterio recorrente consultado |
| DEP-TLS | consulta | Ferramenta oficial e limite |
| DEP-KMS | **entrega** | Aprendizado e postmortem gravados |
| DEP-GRW | **sem interacao estrutural direta** | FND-02 §4 declara `—`. Comunicacao externa de incidente passa por DEP-EXE e pelo **SOBERANO** |

> A matriz completa de interacao vive em **FND-02 §4** e **nao** e reproduzida aqui: esta
> secao declara apenas as linhas de DEP-OPS (DC-08).

## 7. Artefatos e registros mantidos

| Tipo documental | Entidade | Meu papel | Onde vive |
|---|---|---|---|
| Memoria **OPR** | `MEM` | **Dono da camada** | `memory/operacional/` |
| **Runbook** | `MEM` da camada OPR | **Autor e proprietario** | `memory/operacional/` |
| **Postmortem de incidente operacional** | `MEM` da camada APR | **Autor**; **DEP-KMS e o dono da camada** | `memory/aprendizado/` |
| **Reporte / Alerta** | `MSG` | **Emissor** | `memory/operacional/` |
| **ADR** *(de rotina, quando o efeito for C2)* | `ADR` | **Autor**; nunca aprovador do proprio | `decisions/` |
| **Nota de Decisao** *(C1 de rotina)* | `ADR` derivado | **Autor**, com revisor de papel distinto | `decisions/` |
| Incidente de **conformidade** | `INC` | **Detecto e reporto** — nao registro nem numero, nao fecho | `governance/incidents/` |
| Carta de Agente / Subagente de DEP-OPS | `AGT` `SUB` | **Autor**, quando o agente for desta area | fase futura |

> **Nenhum componente operado existe nesta fase**, por determinacao — nao ha codigo,
> infraestrutura nem banco. Tipo documental que nao conste de
> [FND-10 §4](../../foundation/10-artifact-framework.md) nao existe (CS-01, MT-01).

## 8. Quando escalo

| Gatilho | Escala para | Nivel | Bloqueia execucao? |
|---|---|---|---|
| **Incidente com perda ou exposicao de dado** | SOBERANO | **E4** *(pula niveis, EC-02)* | **Sim** |
| **Falha de backup** | SOBERANO, via DEP-QAR | **E4** | **Sim** — sem copia, nao executa (PI-07, LV-01) |
| **Indisponibilidade material** | SOBERANO, via DEP-EXE | **E4** | **Sim** |
| Credencial exposta detectada na operacao | SOBERANO, via DEP-QAR | **E4** | **Sim** (PI-08) |
| Acao destrutiva pedida **sem backup verificado** | **recusa e escala** ao SOBERANO | **E4** | **Sim — a recusa e obrigatoria** (LV-01) |
| Duvida de conformidade, qualidade ou risco | DEP-GOV / DEP-QAR | **E3** | Sim |
| **Runbook impossivel de escrever a partir do que foi entregue** | DEP-ENG, por devolucao de handoff | **E1** | Sim, para o item |
| Conflito entre a fila operacional e a fila organizacional | DEP-EXE | **E2** | Nao |
| Duvida rotineira de execucao resolvivel por premissa | ninguem — **decide e registra a premissa** | **E0** | Nao |

### 8.1 Cadencias de que participo
| Cadencia | Meu papel | O que produzo |
|---|---|---|
| Abertura de ciclo | Recebo prioridade e alocacao | Estado operacional de entrada |
| **Sincronizacao de linha** | Participo | Estado, bloqueios, dependencias operacionais |
| Revisao de qualidade | **Sou avaliado** — nunca avalio | Correcao dos defeitos apontados; **confirmacao de backup para QG-4** |
| Fechamento de ciclo | Reporto | Status operacional, incidentes, continuidade |
| Colheita de aprendizado | **Contribuo com postmortem** | Causa raiz de incidente para a camada APR |

### 8.2 Handoffs
| Handoff | Emito / recebo | Criterio de aceite | Criterio de devolucao |
|---|---|---|---|
| **Componente para operacao** | **Recebo** de DEP-ENG | Desenho e criterio de operacao entregues; QG-3 liberado | **Runbook impossivel de escrever** a partir do entregue (HO-02, HO-04) |
| **Sinal de uso real** | **Emito** a DEP-PRD e DEP-ENG | Ocorrencia com frequencia e contexto | Devolvido se nao for reproduzivel |
| **Confirmacao de backup** | **Emito** a DEP-QAR | Data, escopo da copia e **resultado da verificacao** | Copia sem verificacao de restauracao — **nao e backup** (PI-07) |
| **Postmortem** | **Emito** a DEP-KMS | Causa identificada, nao sintoma; acao com dono | Relato de evento **sem licao extraida** — isso e OPR, nao APR (FND-06 §3.5) |
| Pedido de capacidade externa | **Emito** a DEP-TLS | Finalidade e dado que trafega declarados | Ferramenta nao adotada, ou limite incompativel |

> **Handoff devolvido duas vezes pelo mesmo motivo escala a DEP-EXE** — ha defeito de
> fronteira (HO-03, FND-02 §9.2).

## 9. Memoria autorizada e politica de contexto

| Camada | Meu papel | Sob que condicao |
|---|---|---|
| **EST** | **Leitor obrigatorio** antes de qualquer decisao C2/C3 | Nao escrevo: escrita em EST e de DEP-GOV, mediante ADR (FND-06 §3.1) |
| **PRD** | Leitor | Criterios de aceite recorrentes do que se opera |
| **TEC** | **Leitor obrigatorio** antes de operar | Como esta construido e por que assim; **DEP-ENG e o dono** |
| **OPR** | **Dono da camada** | Estado corrente, runbooks, incidentes, backups, consumo e excecoes vigentes (FND-06 §2.1). **Expiracao e o comportamento padrao** |
| **APR** | **Contribuinte obrigatorio**; DEP-KMS e o dono | Todo postmortem e causa raiz vira licao (QG-5) |

> **Ser dono da camada OPR nao e exercer `CAP-conhecimento`.** Dono custodia **conteudo**; a
> Capability e **persistir e devolver o que se sabe**, e quem a exerce e **DEP-KMS**, o curador.
> Resolucao do achado **P2** em [REV-ESTRUTURAL-I §3.6](../../foundation/revisao-estrutural-01-2026-07-28.md).

### 9.1 Politica de contexto
| Item | Valor |
|---|---|
| Pacote minimo para operar | Nucleo obrigatorio + o **runbook** da rotina em execucao + o registro **TEC** do componente operado |
| Custo medido do pacote | **1.099 linhas** de nucleo, medido em 2026-07-28. **Nenhum runbook e nenhum registro TEC existem nesta fase** — o pacote real e hoje **so o nucleo** |
| Gatilho para carregar alem do minimo | **Incidente aberto** ou rotina em execucao. Carrega-se **o componente afetado**, nunca o acervo |
| **Nao** carrego por padrao | As duas Cartas de Capability juntas *(**319 linhas**, medidas)*; a camada PRD integral; perfil `arquivo` |

## 10. Riscos, impedimentos e segregacao

> **Secao obrigatoria (DC-03).** Sem ela a Carta nao e valida.

| # | Materia em que estou impedido | Por que | **Quem me substitui** | Fonte |
|---|---|---|---|---|
| **I-1** | **Executar acao destrutiva, irreversivel ou de exposicao sobre dado vivo sem copia datada e verificada** | **Sem copia, nao executa** — nao admite excecao formal | **Ninguem.** A acao **nao ocorre**; escala-se ao SOBERANO | **PI-07, LV-01**; FND-01 §8.3 |
| **I-2** | **Mudar estruturalmente o que opero** | Operar nao da autoridade sobre o que se opera | **DEP-ENG** *(como)* · **DEP-PRD** *(o que)* | FND-01 §7.3; AU-08 |
| **I-3** | **Definir ou verificar a politica** de seguranca, privacidade e retencao | **Operar sob politica nao e custodiar a politica** | **DEP-QAR** | FND-02 §3; **P4** |
| **I-4** | **Verificar ou aprovar a propria confirmacao de backup** como prova suficiente | Quem executa a copia nao e a unica prova de que ela presta | **DEP-QAR**, que confere a cada QG-4 | PI-05, LV-03; FND-01 §6.2 |
| **I-5** | **Fechar incidente de conformidade**, ou registra-lo e numera-lo | Incidente **operacional** e meu; o de **conformidade** e de DEP-GOV *(registra)* e DEP-QAR *(fecha)* | **DEP-GOV** e **DEP-QAR** | FND-09 §8.2, linha `INC` |
| **I-6** | **Comunicar externamente** indisponibilidade, incidente ou perda de dado | Saida externa passa por aprovacao humana | **DEP-GRW** + **SOBERANO** | FND-01 §7.3; **LV-08**, PI-01 |
| **I-7** | **Expandir a camada OPR para reter o que deveria expirar** | Sem TTL agressivo, memoria vira log e log vira ruido | **DEP-KMS** decide promocao entre camadas | FND-06 §3.4, MM-05 |
| **I-8** | **Adotar ferramenta externa por conta propria** para resolver incidente | Urgencia altera o instrumento, nunca o registro | **DEP-TLS** propoe · DEP-EXE aprova · SOBERANO ratifica | **GV-08**; FND-09 §8.2, linha `TOL` |
| **I-9** | **Alterar Carta de Capability** que custodio, para acomodar a rotina | A fonte prevalece sobre a projecao | Rito de FND-08 §6.3 | PR-2, PR-3; PJ-03 |
| **I-10** | **Aprovar, revisar ou emendar esta Carta** | E o instrumento que define a minha propria autoridade | **DEP-GOV** *(revisa)* · **SOBERANO** *(aprova e ratifica)* | RM-06b, LV-03; FND-09 §8.2 |
| **I-11** | **Priorizar, avaliar ou instruir departamento de Guarda** | Linha nao coordena a Guarda | **DEP-EXE** coordena Linha; a Guarda responde ao **SOBERANO** | ES-02, IV-01 |

### 10.1 Riscos proprios do dominio
| # | Risco | Probabilidade | Impacto | Mitigacao declarada |
|---|---|---|---|---|
| RO-1 | **Backup nao verificado tratado como backup** | **Media** | **Critico** | O-6 e I-1: copia **sem verificacao de restauracao nao e backup**. Conferencia independente de DEP-QAR a cada QG-4 |
| RO-2 | **Urgencia usada para dispensar registro** | **Media** | **Alto** | **GV-08**: urgencia altera o instrumento, nunca o registro. Excecao formal e do Soberano, e PI e LV-01 **nao a admitem** |
| RO-3 | **Postmortem que descreve sintoma e nao causa** | **Media** | Medio | O-5 e o criterio de devolucao de handoff: relato sem licao **e OPR, nao APR** (FND-06 §3.5) |
| RO-4 | **Camada OPR virar log** — reter o que deveria expirar | Media | Medio | I-7; expiracao e o **comportamento padrao** da camada, e a presuncao de irrelevancia e desejada |
| RO-5 | **Operacao decidindo o que opera** por proximidade com o problema | Media | **Alto** | I-2: a correcao estrutural volta a DEP-ENG por handoff, com o sinal de uso registrado |
| RO-6 | **Dependencia integral de DEP-ENG** — as duas Capabilities custodiadas dependem das dele | **Observado** | Medio | Declarado em §2. Mitigacao: o handoff ENG → OPS tem **criterio de devolucao proprio** *(runbook impossivel de escrever)*, que impede receber o que nao se pode operar |
| RO-7 | **Zero exercicio** — nenhum componente operado, nenhum runbook, nenhum incidente | **Observado** | Medio | Todos os indicadores de operacao valem **zero** (§11). E ausencia **determinada**, nao omissao |

### 10.2 Incompatibilidades de papel
| Papel A | Papel B | Por que nao se acumulam na mesma mudanca |
|---|---|---|
| Executor da copia de backup | Verificador de que a copia presta | PI-05, LV-03 — e o impedimento **I-4** |
| Operador do componente | Decisor da mudanca estrutural nele | FND-01 §7.3 — impedimento **I-2** |
| Executor da rotina sob politica | Definidor da politica | **P4** — impedimento **I-3** |
| Detector do incidente operacional | Registrador do incidente de **conformidade** | FND-09 §8.2, linha `INC` — impedimento **I-5** |
| Custodio de Capability | Autoridade que aprova a propria proposta de evolucao dela | FND-08 §6.1 — o custodio **propoe**; nao aprova |

## 11. Indicadores

> Indicador **sem valor medido** declara-se `definido, sem valor`. Afirmar desempenho sem
> medida e LV-12.

| # | Indicador | Definicao | Direcao | **Valor medido** | **Data** |
|---|---|---|---|---|---|
| KO-1 | Capabilities custodiadas | Contagem na projecao de `capabilities/README §10` | estavel | **2** | 2026-07-28 |
| KO-2 | Capabilities custodiadas em maturidade `experimental` | Contagem no catalogo | ↓ | **2 de 2** | 2026-07-28 |
| KO-3 | **Componentes operados** | Codigo, infraestrutura, banco sob operacao | — | **0** — proibido nesta fase, por determinacao | 2026-07-28 |
| KO-4 | **Runbooks vigentes** | Contagem na camada OPR | — | **0** | 2026-07-28 |
| KO-5 | **Incidentes operacionais abertos** | Contagem | → 0 | **0** | 2026-07-28 |
| KO-6 | **Registros na camada OPR** | Contagem em `memory/operacional/` | — | **3** — os tres registros canonicos de ato soberano (`MSG-2026-0001` a `MSG-2026-0003`) | 2026-07-28 |
| KO-7 | **Backups verificados** | Contagem de copias com verificacao registrada | ↑ | **2** — as copias datadas das Missoes 1.8 *(115 arquivos)* e 1.9 *(117 arquivos)*, ambas tomadas antes das edicoes | 2026-07-28 |
| KO-8 | **Acoes destrutivas executadas sem backup** | Contagem | → 0 | **0** | 2026-07-28 |
| KO-9 | Postmortems emitidos | Contagem | — | **0** — nenhum incidente operacional ocorreu | 2026-07-28 |
| KO-10 | Disponibilidade do que se opera | Tempo em funcionamento / tempo total | ↑ | **`definido, sem valor`** — nao ha componente operado | — |
| KO-11 | Tempo de recuperacao apos falha | Latencia media | ↓ | **`definido, sem valor`** — nenhuma falha ocorreu | — |
| KO-12 | Rotinas executadas com resultado registrado | Registradas / executadas | → 100% | **`definido, sem valor`** — nenhuma rotina recorrente existe | — |
| KO-13 | Incidentes recorrentes pela mesma causa | Contagem | → 0 | **`definido, sem valor`** — serie inexistente | — |
| KO-14 | Itens OPR expirados e nao tratados | Contagem | → 0 | **`definido, sem valor`** — nenhum ciclo se fechou com expiracao medida | — |

**Contagem: 14 indicadores definidos · 9 com valor medido · 5 `definido, sem valor`.**

> **Dois medidos nao valem zero, e sao os unicos.** **KO-6 = 3** e **KO-7 = 2**: a camada OPR
> ja hospeda os registros canonicos dos atos soberanos, e as duas copias datadas do acervo
> foram tomadas e verificadas. **Sao a unica atividade real de DEP-OPS ate esta data**, e
> ambas ocorreram a servico de missoes documentais, nao de operacao de produto. **Os demais
> valem zero por determinacao**, e os cinco sem valor dependem de um ciclo de operacao que nao
> existe. Declara-los medidos seria **LV-12**.

## 12. Ciclo de vida — especializacao, fusao e retirada

### 12.1 Gatilhos de especializacao
| Gatilho *(FND-02 §9.2)* | Aplica-se? | **Sinal ja observado** | Movimento previsto |
|---|---|---|---|
| **Escopo heterogeneo** | **Sim, potencialmente** | Duas Capabilities de naturezas proximas mas distintas: **executar o recorrente** *(operacoes)* e **sustentar o que roda** *(infraestrutura)*. Contam **2**, abaixo do limite de **tres** de VC-03 | Dividir dominio — **so com sinal medido**, que nao existe |
| Carga concentrada | **Nao avaliavel** | **Nenhum** — zero componentes operados (KO-3) | — |
| Contexto excessivo | **Nao** | Pacote minimo **1.099 linhas**, **3,4%** do acervo — o **menor** entre os nove departamentos | — |
| Fronteira em disputa | **Nao** | **Zero** conflitos registrados com ENG ou QAR | — |
| Duplicacao | Nao | Nenhum procedimento refeito — nao ha procedimento | — |
| Gargalo de decisao | Nao | **0** escalonamentos registrados | — |
| Conhecimento ilhado | **Nao avaliavel** | Nao ha resultado produzido de que extrair o sinal | — |

> **Decisao registrada: nao especializar** (FND-04 §6.2). **SE-02 exige dois sinais observados
> e ha zero.** Dividir agora criaria dois departamentos sem operacao em vez de um. **Gatilho de
> reexecucao:** primeiro componente sob operacao real.

### 12.2 Gatilhos de fusao ou consolidacao
| Sinal *(FND-02 §9.3)* | Com quem | O que indicaria |
|---|---|---|
| **Duas areas que sempre atuam juntas e nunca isoladas** | **DEP-ENG** | Que construir e operar nao sao fronteiras distintas. **Contraindicado**: FND-02 §4 e §5 separam quem constroi de quem sustenta, e a fusao colocaria a correcao estrutural nas maos de quem sente o sintoma (RO-5). Registrado tambem em `DEP-ENG §12.2` |
| Handoff que so transporta, sem transformar | DEP-ENG | Que a entrega ENG → OPS nao acrescenta etapa. **Sinal contrario declarado**: o handoff tem criterio de devolucao proprio — *runbook impossivel de escrever* |
| Componente sem acionamento ao longo de um horizonte | **DEP-OPS**, sobre si mesmo | Que a area foi estruturada antes da operacao. **Nao avaliavel**: nenhum horizonte se tornou avaliavel sob `HZ-02` ([ADR-0013](../../decisions/ADR-0013-criterio-de-horizonte-e-consolidacao.md)) |
| Custo de coordenacao maior que o ganho | — | Nenhum sinal registrado |

### 12.3 Criterio de extincao
DEP-OPS deixa de ser necessario se a organizacao deixar de manter qualquer coisa em
funcionamento — o que contradiria OB-H2.3 de FND-01 §5. Na extincao, cada responsabilidade e
cada custodia recebe destino explicito (IV-07, FND-02 §8.3):

| Responsabilidade / custodia | Destino declarado na extincao |
|---|---|
| Custodia de `CAP-operacoes` e `CAP-infraestrutura` | Destino explicito obrigatorio. Candidato natural: **DEP-ENG**, de quem as duas ja dependem. **Nunca** departamento de Guarda — concentraria execucao e verificacao no mesmo papel |
| **Backups e sua verificacao** | Destino explicito obrigatorio e **imediato**. Backup sem dono e o risco que PI-07 protege; a organizacao **nao opera** sem esse dono |
| **Continuidade** | Transferida com o componente operado; plano sem dono e plano inexistente |
| **Camada de memoria OPR** | Novo dono nomeado; a camada **nao** e apagada (MM-09) e continua expirando por padrao |
| Runbooks e postmortems ja emitidos | Preservados; nenhum e apagado (FND-04 §7.2) |

### 12.4 Funcoes internas nomeadas
> Responsabilidades hospedadas aqui que ainda nao merecem departamento proprio (ES-04).

| Funcao | Responsabilidade | Gatilho de promocao |
|---|---|---|
| **Continuidade e recuperacao** | Backup, verificacao, plano de recuperacao, tempo alvo | **Primeiro dado vivo sob operacao** |
| **Monitoramento** | Sinal de falha antes do usuario | **Primeiro componente exposto ao publico** |
| **Suporte** | Atendimento do que ja opera | **Primeiro usuario externo** |

## 13. Resumo operacional, carregamento e rastreabilidade

### 13.1 Resumo operacional
Mantem em funcionamento o que ja existe e executa o trabalho recorrente com previsibilidade,
backup verificado e continuidade.

### 13.2 Perfil minimo de carregamento
| Recorte | Para que serve | Custo **medido** | Data |
|---|---|---|---|
| Secoes 1, 2 e 4 | Saber o que DEP-OPS faz e o que nao faz | **59 linhas** | 2026-07-28 |
| + secoes 5 e 10 | Decidir se DEP-OPS pode executar ou acionar algo | **136 linhas** | 2026-07-28 |
| Carta integral | Auditoria, revisao estrutural, extincao | **437 linhas** | 2026-07-28 |

> Carregar alem do recorte aplicavel exige **gatilho declarado** (CE-01, PC-01). O recorte de decisao custa **31% da Carta** — medido por
> `sed`+`wc -l` sobre os intervalos das secoes.

### 13.3 Rastreabilidade
| Campo | Conteudo |
|---|---|
| ADR de criacao do departamento | [ADR-0001](../../decisions/ADR-0001-adocao-da-fundacao-organizacional.md) — adota FND-02, que cria os nove departamentos |
| ADR do contrato desta Carta | [ADR-0011](../../decisions/ADR-0011-contrato-de-carta-de-departamento.md) |
| RFC de origem | [RFC-0008](../../rfcs/RFC-0008-contrato-de-carta-de-departamento.md) |
| Decisoes que moldam esta Carta | ADR-0002 *(vinculacao a Capability)* · ADR-0003 *(Meta Model; entidade `DEP`)* · ADR-0012 *(integridade do ato — base da nota de homologacao em §5)* · ADR-0013 *(criterio de horizonte — base de §12.2)* |
| Achado que esta Carta trata | **P4** *(operar sob politica ≠ custodiar a politica)* — declarado em §2 e em **I-3** · **P2** *(dono de camada ≠ exercer `CAP-conhecimento`)* — declarado em §9 |
| Alteracoes (ADRs) | Nenhuma |
| Fonte da custodia e do exercicio | frontmatter de `capabilities/CAP-operacoes.md`, `CAP-infraestrutura.md` |
| Validacao em cenarios | [REV-ROLLOUT §3](../../foundation/revisao-arquitetural-rollout-cartas-2026-07-28.md) |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-EXE | Criacao — **oitava Carta do sistema**, quarta do rollout. Doze blocos preenchidos. Declara o unico impedimento do acervo **sem substituto possivel** *(I-1: sem copia, nao executa)* e a distincao entre **incidente operacional** e **incidente de conformidade**. Permanece em `em-revisao`: aprovar Carta de Departamento e ato do **SOBERANO** (DC-09). |
| 1.1.0 | 2026-07-30 | DEP-EXE | Emenda **C2 · Tipo 2** por **ADR-0025**, em **cascata** (`CV-04`) de [ADR-0018](../../decisions/ADR-0018-liberacao-do-portao-qg-1.md), **ratificado**: **§5.2** deixa de afirmar que **`QG-1` e liberado por `DEP-PRD`** e passa a declarar **`DEP-EXE` *(QG-0 e QG-1)***, alinhando esta Carta a fonte ratificada **FND-01 §6.2**. **Uma afirmacao falsa corrigida; duas linhas substituidas; `0` linhas acrescentadas.** Fecha **RD-37** quanto a esta Carta. **Nenhuma responsabilidade, portao, papel, direito de decisao, interface, risco, metrica ou Capability desta Carta foi criado, removido ou alterado** — este departamento continua **nao liberando portao algum**, e o que muda e **de quem se diz** que libera `QG-1`. **Nenhum titular novo:** `DEP-EXE` ja e o titular por ADR-0018 desde 2026-07-29. |
