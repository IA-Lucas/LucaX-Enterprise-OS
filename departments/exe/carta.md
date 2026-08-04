---
id: DEP-EXE
titulo: Gabinete Executivo
tipo: carta
versao: 1.2.0
status: ativo
camada_memoria: estrategica
autor: DEP-EXE
proprietario: DEP-EXE
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-08-02
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0001, ADR-0002, ADR-0004, ADR-0011, ADR-0018, ADR-0019, ADR-0023, ADR-0032]
substitui: []
substituido_por: null
classe: comando
nivel: 1
nivel_autonomia: A3
responde_a: SOBERANO
capabilities: [CAP-estrategia, CAP-coordenacao, CAP-financeiro, CAP-comunicacao]
resumo: Converte a direcao do Soberano em prioridade executavel, aloca capacidade, arbitra entre areas de Linha e responde pela entrega do que foi priorizado.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-GOV
ratificacao: ratificada
---

# Gabinete Executivo (DEP-EXE)

## Proposito
Existir como o ponto em que direcao vira fila. Traduz a intencao do Soberano em prioridade
executavel, decide quem faz o que e quando, arbitra empates entre areas de Linha e responde
perante o Soberano pelo que a organizacao entregou — sem decidir o conteudo do que se entrega.

## Escopo
| Item | Definicao |
|---|---|
| Classe | **comando** — a **unica** do sistema (FND-02 §2.1) |
| Nivel | **1** — o unico nivel 1; entre o Soberano e todo o resto |
| Responde a | **SOBERANO**, diretamente |
| Nivel de autonomia | **A3** — o **mais alto concedido a qualquer papel**; nenhum papel opera acima (FND-01 §7.2) |
| Poder de veto | **Nao** — decide e arbitra; vetar e exclusivo da Guarda (FND-02 §2.1) |
| **Nao** inclui | Conteudo tecnico, escopo de produto, padrao de qualidade e norma. Delimitacao integral na secao 4 |
| Subordinado a | [FND-01](../../foundation/01-constituicao.md) · [FND-02](../../foundation/02-estrutura-organizacional.md) · [ADR-0011](../../decisions/ADR-0011-contrato-de-carta-de-departamento.md) |

## Responsaveis
| Papel | Quem |
|---|---|
| Autor da Carta | **DEP-EXE** *(FND-09 §8.2, linha `DEP`: propoe/cria)* |
| Proprietario | DEP-EXE |
| Guardiao normativo / revisor | **DEP-GOV** *(FND-09 §8.2: revisa)* |
| Verificacao adversarial dos blocos impedidos | **DEP-QAR** *(secao 10, I-1 — desvio declarado)* |
| Aprovador e ratificador | **SOBERANO** *(indelegavel — DC-09)* |

> **Esta Carta foi escrita por DEP-EXE sobre DEP-EXE, e nao havia alternativa.** A matriz de
> [FND-09 §8.2](../../foundation/09-meta-model.md), linha `DEP`, atribui **exclusivamente a
> DEP-EXE** a proposicao de Carta de Departamento; nenhum outro papel pode propor. O impedimento
> esta declarado em **I-1** e o desvio aplicado — verificacao dos blocos B4, B9 e B12 por
> **DEP-QAR**, com forma por DEP-GOV — esta registrado em
> [REV-INTERCLASSES §4](../../foundation/revisao-arquitetural-validacao-interclasses-2026-07-28.md).
> **E o impedimento que R2 de FIT-2026-005 e DR-5 de REV-DEPARTAMENTO nomearam como o mais
> dificil do contrato**, e esta e a primeira vez que ele e exercido.

---

## 1. Missao e mandato

**Missao:** converter a direcao do Soberano em prioridade executavel e garantir que a
organizacao entregue o que foi priorizado.

**Mandato:** decidir **quem faz o que, quando e em que ordem**, com autoridade para arbitrar
entre areas de Linha — e nenhuma sobre o **merito** do que se decide em cada dominio.

> **A distincao que define a classe Comando.** A Guarda responde *"isto pode passar?"*; a Linha
> responde *"como isto se faz?"*; o Comando responde *"isto vem antes ou depois, e por quem?"*.
> Nenhuma das tres responde a pergunta das outras duas.

## 2. Capabilities custodiadas e exercidas

> **Declaracao de projecao (PJ-02).** **Fonte:** frontmatter de `capabilities/CAP-estrategia.md`,
> `CAP-coordenacao.md`, `CAP-financeiro.md` e `CAP-comunicacao.md`, campos `custodio` e
> `exercentes`. **Campos projetados:** apenas as linhas de DEP-EXE. **Finalidade:** responder "o
> que custodio e o que exerco" sem abrir quatro arquivos. **Atualizacao:** pela mesma mudanca que
> altera a Carta de Capability (CV-04). Em divergencia, prevalece a Carta de Capability (PR-1).

| Capability | Dominio · Classe | **Custodia** | **Exercicio** | Por que este departamento |
|---|---|---|---|---|
| [CAP-estrategia](../../capabilities/CAP-estrategia.md) | DIR · **`nucleo`** | **sim** | sim | Traduzir direcao em algo operavel e a razao de existir da classe Comando |
| [CAP-coordenacao](../../capabilities/CAP-coordenacao.md) | DIR · `habilitadora` | **sim** | sim | Priorizar, alocar e arbitrar e o mandato literal |
| [CAP-financeiro](../../capabilities/CAP-financeiro.md) | MER · `suporte` | **sim** | sim | Custo, consumo e limite pertencem a funcao interna **Recursos (FIN)**, hospedada aqui (§12.4) |
| [CAP-comunicacao](../../capabilities/CAP-comunicacao.md) | COG · `habilitadora` | **sim** | sim | Transferir trabalho sem perder contexto e condicao do handoff, que e instrumento de coordenacao |

**Capabilities que exerco sem custodiar:** nenhuma.
**Capabilities que custodio e sao exercidas por outros:** **`CAP-comunicacao`**, tambem
exercida por **DEP-KMS**.

> **Esta e a unica linha do acervo que da membro a OW-02.** O achado **P1** de
> [capabilities/README §10.3](../../capabilities/README.md) registra que **22 de 23**
> Capabilities declaram `exercentes` identico ao `custodio` — a regra *"custodia nao e
> exclusividade de exercicio"* (OW-02, RM-05) tinha **um unico membro observado**, e ele e
> este. Declarar esta coluna vazia, como fizeram DEP-QAR e DEP-ENG por serem de fato vazias,
> teria deixado a regra sem nenhum exercicio em quatro Cartas. **P1 permanece aberto**: um
> membro continua sendo menos que os dois de AQ-03; o que muda e que agora ele esta **declarado
> na Carta do custodio**, e nao so na projecao.

> **Achado declarado, nao contornado — VC-03.** Quatro vinculos ultrapassam o limite de **tres**
> de VC-03. E o achado **P6** de capabilities/README §10.3, dono DEP-EXE, com gatilho **"1a
> revisao estrutural, ou Carta de DEP-EXE"**. **Esta Carta e o gatilho.** A avaliacao esta em
> §12.1, e a decisao registrada e **nao especializar** — com o custo declarado.

## 3. O que possuo — escopo exclusivo

| # | Responsabilidade | Como se verifica que esta sendo cumprida | Capability |
|---|---|---|---|
| X-1 | **Portfolio ativo** — o conjunto do que a organizacao esta fazendo | Todo trabalho em curso consta do portfolio; trabalho fora dele e desvio | CAP-estrategia |
| X-2 | **Fila de prioridades** — a ordem em que o trabalho ocorre | Toda entrada e saida da fila tem motivo registrado | CAP-coordenacao |
| X-3 | **Alocacao de capacidade** — quem executa o que | Nenhum departamento assume trabalho nao alocado | CAP-coordenacao |
| X-4 | **Cadencia organizacional** — quando um ciclo abre e fecha | Abertura e fechamento declarados, nunca implicitos | CAP-coordenacao |
| X-5 | **Arbitragem entre areas de Linha** | Conflito N2 resolvido com decisao registrada (FND-02 §7) | CAP-coordenacao |
| X-6 | **Portao QG-0** — o pedido esta claro, cabe no escopo e nao viola norma? | Nenhum trabalho comeca sem QG-0 liberado | CAP-coordenacao |
| X-7 | **Orcamento de recursos e custos** | Custo e consumo acompanhados por ciclo; limite declarado antes de ser atingido | CAP-financeiro |
| X-8 | **Briefing de trabalho**, com `nivel_autonomia_concedido` | Toda DIRETIVA declara a autonomia concedida, nunca presumida | CAP-comunicacao |
| X-9 | **Relatorio consolidado ao Soberano** | O Soberano decide sobre estado reportado, nao inferido | CAP-comunicacao |
| X-10 | **Aprovacao do veredito de aptidao (`FIT`)** | Nenhum `FIT` encerra mudanca sem aprovacao de papel distinto do executor | CAP-coordenacao |
| X-11 | **Proposicao de Carta de Departamento** | Toda Carta tem DEP-EXE como autor; nenhuma nasce por autodeclaracao do proprio departamento | CAP-estrategia |
| X-12 | **Decisao de rollout** — quando uma serie de artefatos deixa de ser piloto | GO/ADJUST/STOP registrado com condicoes verificaveis | CAP-estrategia |
| X-13 | **Portao `QG-1`** — a spec define resultado, criterio de aceite e o que esta fora? | Nenhuma spec passa a construcao sem `QG-1` liberado, com responsavel e data registrados. **Verifico presenca e verificabilidade, nunca merito de escopo** | CAP-coordenacao |

## 4. O que NAO me compete

| Materia | Dono real | Fonte |
|---|---|---|
| Decidir **o que** construir e o escopo do produto | DEP-PRD | FND-02 §3; FND-01 §7.3 |
| Decidir **como** construir; arquitetura e padrao tecnico | DEP-ENG | FND-02 §3; FND-01 §7.3 |
| Decidir se a entrega **passa**, e qual o padrao de qualidade | DEP-QAR | FND-02 §3; FND-01 §7.3 |
| Decidir **norma**, taxonomia, forma e conformidade | DEP-GOV | FND-01 §7.3; FND-04 §12 |
| Decidir **onde um registro de memoria pertence** e o que expira | DEP-KMS | FND-01 §7.3; FND-06 §2.1 |
| Declarar qual **ferramenta externa** e oficial | DEP-TLS | FND-02 §3 |
| Executar **rotina operacional** e responder por incidente operacional | DEP-OPS | FND-02 §3 |
| **Priorizar, avaliar ou instruir a Guarda** | **Ninguem** — a Guarda responde ao Nivel 0 | **ES-02, IV-01**; FND-02 §2.1 |
| **Reverter veto da Guarda** | **SOBERANO** | LV-09; FND-02 §6 |
| **Criar ou encerrar produto**; alterar a estrutura organizacional | **SOBERANO** | FND-01 §7.3 |
| **Exposicao de dado vivo ao exterior** | **SOBERANO**, com DEP-QAR | FND-01 §7.3; LV-08 |
| **Aprovar ou ratificar esta Carta**, ou qualquer Carta de Departamento | **SOBERANO** | FND-09 §8.2, linha `DEP`; DC-09 |
| Alterar Carta de Capability para acomodar esta Carta | custodio da Capability | PR-2, PR-3 de ADR-0011 |

## 5. O que decido — autoridade e portoes

| Materia | Autonomia | Consulta obrigatoria | **Fonte da autoridade** |
|---|---|---|---|
| **O que entra e sai da fila** | A3 | — | FND-02 §3, DEP-EXE "Decide" |
| **Quem executa o que** — alocacao | A3 | — | FND-02 §3 |
| **Quando um ciclo abre e fecha** | A3 | — | FND-02 §3 |
| **Empate entre areas de Linha** — arbitragem | A3 | DEP-GOV se envolver norma | FND-02 §3 e §7, nivel N2 |
| Liberacao de **QG-0** | A3 | — | FND-01 §6.2, linha QG-0 |
| Liberacao de **QG-1** | A3 | **DEP-PRD** *(autor da spec)* · **DEP-QAR** *(verificabilidade do criterio de aceite)* | FND-01 §6.2, linha `QG-1`, pos-[ADR-0018](../../decisions/ADR-0018-liberacao-do-portao-qg-1.md) |
| **Aprovar Spec** (`SPC`) **quando a classe do efeito for `C1` ou `C2`** | A3 | DEP-GOV *(parecer, em `C2`)*; DEP-ENG + DEP-QAR *(revisores da spec)* | FND-04 §2, `C1` e `C2`, e **§3.1**; FND-09 §8.2, linha `SPC`, pos-[ADR-0019](../../decisions/ADR-0019-aprovador-e-ratificador-de-spec.md) e **[ADR-0032](../../decisions/ADR-0032-separacao-de-proponente-e-aprovador-na-spec-c1.md)** — *aprova conforme classe*. **`C0`: o proprietario. `C3`: SOBERANO** |
| **Aprovar o veredito de aptidao (`FIT`)** | A3 | DEP-GOV *(forma)* | FND-09 §8.2, linha `FIT` |
| **Aprovar Carta de Agente, Subagente e Skill** | A3 | DEP-GOV + DEP-QAR *(revisao)* | FND-09 §8.2, linhas `AGT`, `SUB`, `SKL` |
| **Homologar** escopo e prioridade de produto decididos por DEP-PRD | A3 | DEP-PRD, DEP-ENG | FND-01 §7.3, coluna *Ratifica* |
| **Homologar** arquitetura tecnica decidida por DEP-ENG | A3 | DEP-QAR | FND-01 §7.3, coluna *Ratifica* |
| **Homologar** rotina operacional decidida por DEP-OPS | A3 | DEP-ENG | FND-01 §7.3, coluna *Ratifica* |
| **Homologar** adocao de ferramenta decidida por DEP-TLS | A3 | DEP-QAR, DEP-ENG | FND-01 §7.3, coluna *Ratifica* |
| **Atribuicao provisoria** de responsabilidade sem dono | A3 | DEP-GOV registra | FND-02 §6 |
| Abrir proposta de **consolidacao** (EV-08) | A3 | DEP-QAR *(evidencia)* | FND-10 §9; FND-02 §9.3 |

> **Termo: "homologar", nao "ratificar".** [FND-01 §7.3](../../foundation/01-constituicao.md)
> usa *Ratifica: DEP-EXE* em quatro materias, enquanto **LM-02 e DC-09** reservam
> *ratificacao* ao ato do Soberano que da vigencia a artefato. **Sao dois institutos com um
> nome so.** Esta Carta usa **homologar** para o de FND-01 §7.3, para que a leitura de uma
> linha de B4 nunca sugira que DEP-EXE possa dar vigencia a artefato. A colisao terminologica
> e do documento de origem, **nao e resolvida aqui** — e registrada como achado **IC-2** em
> [REV-INTERCLASSES §6](../../foundation/revisao-arquitetural-validacao-interclasses-2026-07-28.md),
> dono DEP-GOV. Renomear em FND-01 seria **C3** (LX-07, DC-08).

### 5.1 O que **nao** decido
| Materia | Quem decide | Fonte |
|---|---|---|
| Merito tecnico, escopo de produto, padrao de qualidade, norma | DEP-ENG · DEP-PRD · DEP-QAR · DEP-GOV | FND-01 §7.3 |
| **Aprovar Carta de Departamento** — inclusive a minha | **SOBERANO** | FND-09 §8.2, linha `DEP` |
| Aprovar Carta de Capability, Produto ou Excecao | **SOBERANO** | FND-09 §8.2 |
| Criar ou encerrar produto; alterar a estrutura organizacional | **SOBERANO** | FND-01 §7.3 |
| **Reverter veto da Guarda** | **SOBERANO** | LV-09 |
| **Priorizar ou instruir DEP-GOV e DEP-QAR** | **Ninguem** — respondem ao Nivel 0 | ES-02, IV-01 |
| Aprovar `FIT` cujo objeto **eu produzi** | **DEP-GOV**, ou o SOBERANO | §10, **I-2** |

### 5.2 Portoes sob minha responsabilidade
| Portao | O que verifico | Criterio de liberacao | Fonte |
|---|---|---|---|
| **QG-0** | O pedido esta claro, cabe no escopo e nao viola norma vigente? | Pedido formulado, vinculo a Capability declarado e valido (VC-04), e nenhuma norma vigente contrariada | FND-01 §6.2 |
| **QG-1** | A spec define **resultado**, **criterio de aceite** e **o que esta fora**? | Os tres **presentes e verificaveis por terceiro**; escopo negativo explicito; publico nomeado. **Liberar nao e aprovar** | FND-01 §6.2, pos-ADR-0018; FND-04 §6, linha *Spec* |

> **Nenhum portao novo e criado aqui, e nenhum e transferido aqui.** Os sete sao de
> FND-01 §6.2; acrescentar e **C3**, e a titularidade de `QG-1` foi determinada por
> [**ADR-0018**](../../decisions/ADR-0018-liberacao-do-portao-qg-1.md), **ratificado** —
> esta Carta **declara** o que a fonte ja decidiu, e nao decide de novo.
> **QG-0 e o unico portao que nao verifica um artefato produzido** — verifica um pedido antes
> de existir producao. Por isso a regra *"portao nao pode ser liberado por quem produziu"*
> (FND-01 §6.2) nao o alcanca da mesma forma que aos demais: nao ha produto ainda. O que o
> alcanca e I-4.
>
> **`QG-1` e o caso inverso, e e por isso que ele cabe aqui.** Ele verifica um artefato
> **produzido por outro** — a `Spec`, de **DEP-PRD** (FND-09 §8.2, linha `SPC`) —, e e essa
> alteridade que **satisfaz** a regra de portao, em vez de excepciona-la. **Liberar nao e
> aprovar** (FND-01 §6.2): confirma-se **presenca e verificabilidade por terceiro**;
> **DEP-PRD segue decidindo o escopo**; e o veto de **DEP-QAR** sobre criterio de aceite nao
> verificavel permanece integral (LV-09). **I-5 continua vedando a DEP-EXE decidir merito, e
> o portao nao e via para contorna-lo** — e o que **I-10** declara.

## 6. Interfaces — entradas, saidas e consumidores

### 6.1 Entradas
| De quem | O que recebo | Em que forma | Gatilho |
|---|---|---|---|
| **SOBERANO** | Direcao, intencao, determinacao, arbitragem de N4 | **DIRETIVA** | Ato do Soberano |
| **DEP-PRD** | **Spec submetida a `QG-1`**, com os tres itens declarados e o publico nomeado | **HANDOFF** | Antes da construcao — `QG-1` |
| DEP-PRD · DEP-ENG · DEP-OPS · DEP-GRW · DEP-KMS · DEP-TLS | Estado, estimativa, bloqueio, escalonamento **E2** | REPORTE | Ciclo corrente |
| DEP-GOV | Parecer de conformidade, classe de mudanca validada, escalonamento **E3** | CONSULTA | Etapa 2 do ciclo de FND-04 §4 |
| DEP-QAR | Laudo de risco, veredito de aptidao para aprovacao, **veto** | REPORTE ou **ALERTA** | QG-3, QG-4, QG-6 |
| DEP-KMS | Pacote de contexto, sintese de aprendizado, alerta de contradicao | REPORTE | QG-0 e QG-5 |
| Qualquer departamento | Conflito de fronteira N2 para arbitragem | CONSULTA | FND-02 §7 |

### 6.2 Saidas
| Entrega | Destinatario | Formato | Cadencia | Consumidor final |
|---|---|---|---|---|
| **Prioridade vigente** | Todos os departamentos | DIRETIVA | Por ciclo | Quem executa |
| **Briefing de trabalho** | Departamento alocado | **DIRETIVA**, com `nivel_autonomia_concedido` | Por item | Quem executa |
| **Decisao de arbitragem** | Areas em conflito + DEP-GOV | REPORTE, com motivo registrado | Por evento | As areas e o registro |
| **Relatorio consolidado** | **SOBERANO** | REPORTE | Por ciclo e ao encerrar mudanca C2/C3 | Quem decide o rumo |
| **Liberacao de `QG-1`** | **DEP-PRD** *(autor)* e **DEP-ENG** *(quem recebe a spec)* | Registro do portao, com responsavel e data | Por spec submetida | Quem constroi |
| **Aprovacao de `FIT`** | `governance/fitness/` | Campo `aprovador` do artefato | A cada C2/C3 | Toda a organizacao |
| **Carta de Departamento** *(autor)* | `departments/<dep>/` | Artefato `DEP` em `em-revisao` | Por departamento | SOBERANO, que aprova |
| **Decisao de rollout** GO/ADJUST/STOP | DEP-GOV + SOBERANO | Secao de `FIT` | Ao fim de um piloto | Quem escreve os proximos |
| Aprendizado sobre priorizacao e arbitragem | DEP-KMS | REPORTE, secao Aprendizado | A cada encerramento | Camada APR |

### 6.3 Natureza da interacao
| Departamento | Natureza | O que trafega |
|---|---|---|
| DEP-PRD · DEP-ENG · DEP-OPS · DEP-GRW · DEP-KMS · DEP-TLS | **aprovacao** | Prioridade, alocacao, briefing; estado e escalonamento no sentido inverso |
| DEP-GOV | **consulta** | Conformidade. **DEP-GOV veta DEP-EXE; DEP-EXE nunca instrui DEP-GOV** (ES-02) |
| DEP-QAR | **consulta** | Risco e aptidao. **DEP-QAR veta DEP-EXE; DEP-EXE nunca instrui DEP-QAR** (ES-02, IV-01) |
| SOBERANO | recebe e obedece | Direcao para baixo; relatorio e escalonamento **E4** para cima |

> A matriz completa de interacao vive em **FND-02 §4** e **nao** e reproduzida aqui: esta
> secao declara apenas as linhas de DEP-EXE (DC-08).

> **A leitura mais importante da minha linha na matriz.** DEP-EXE **aprova** seis
> departamentos e **consulta** dois. Os dois que consulta — GOV e QAR — sao exatamente os que
> **o vetam**. A classe Comando e a unica que coordena quase todos e nao coordena os que a
> verificam; e o desenho literal de ES-02, e ele so fica visivel quando se le a linha inteira.

## 7. Artefatos e registros mantidos

| Tipo documental | Entidade | Meu papel | Onde vive |
|---|---|---|---|
| **Carta de Departamento** | `DEP` | **Autor**; nunca aprovador | `departments/<dep>/` |
| **Fitness Check** | `FIT` | **Aprovador**; nunca autor nem executor | `governance/fitness/` |
| **Revisao Arquitetural** | `FIT` *(corretude)* | **Aprovador** | Ao lado do que revisa |
| **Spec** | `SPC` | **Liberador de `QG-1`**; **aprovador quando a classe do efeito for `C1` ou `C2`**; **nunca autor nem revisor** | fase futura — `products/<slug>/specs/` |
| Carta de Agente / Subagente / Skill | `AGT` `SUB` `SKL` | **Aprovador** | fase futura |
| ADR | `ADR` | **Autor** *(quando a materia for de coordenacao ou portfolio)*; **aprovador** conforme a classe | `decisions/` |
| RFC | `RFC` | Autor | `rfcs/` |
| Carta de Capability | `CAP` | **Proprietario do catalogo**; nunca aprovador | `capabilities/` |
| Diretiva / Reporte | `MSG` | **Emissor** | `memory/operacional/` |
| Memoria **OPR** | `MEM` | Escritor — portfolio e fila do ciclo corrente | `memory/operacional/` |

> **Tipo documental que nao conste de [FND-10 §4](../../foundation/10-artifact-framework.md)
> nao existe** (CS-01, MT-01). Nenhum e criado por esta Carta.

## 8. Quando escalo

| Gatilho | Escala para | Nivel | Bloqueia execucao? |
|---|---|---|---|
| Decisao **Tipo 1** de qualquer natureza | SOBERANO | **E4** | **Sim** |
| **Conflito com norma vigente** | SOBERANO, via DEP-GOV | **E4** | **Sim** |
| **Mudanca de portfolio** — criar ou encerrar produto | SOBERANO | **E4** | **Sim** |
| **Veto de Guarda que se pretende reverter** | SOBERANO | **E4** | **Sim** — nao se executa enquanto isso (LV-09) |
| Exposicao de dado vivo, ou credencial comprometida | SOBERANO, via DEP-QAR | **E4** *(pula niveis, EC-02)* | **Sim** |
| Conflito **N4** — norma, principio ou Tipo 1 | SOBERANO | **E4** | **Sim** |
| Impedimento proprio que deixe a aprovacao sem executor | SOBERANO, via DEP-GOV | **E3 → E4** | **Sim** |
| Duvida de conformidade documental | DEP-GOV | **E3** | Sim |
| Duvida de risco | DEP-QAR | **E3** | Sim |
| Empate entre areas de Linha | **ninguem — arbitro e registro** | **E0** | Nao |

### 8.1 Cadencias de que participo
| Cadencia | Meu papel | O que produzo |
|---|---|---|
| **Abertura de ciclo** | **Conduzo** | Prioridade, alocacao, briefing, QG-0 liberado |
| **Sincronizacao de linha** | **Conduzo** | Desbloqueio, realocacao, arbitragem |
| Revisao de qualidade | Recebo o resultado | Decisao sobre a fila diante do veredito |
| **Fechamento de ciclo** | **Conduzo** | Relatorio consolidado ao Soberano; divida e custo do ciclo |
| **Revisao estrutural** *(por horizonte)* | Participo com DEP-GOV *(forma)* e DEP-KMS *(evidencia)* | Proposta de especializacao, de consolidacao, ou "manter" fundamentado |
| Colheita de aprendizado | Contribuo | Licao sobre priorizacao e arbitragem |

### 8.2 Handoffs
| Handoff | Emito / recebo | Criterio de aceite | Criterio de devolucao |
|---|---|---|---|
| **Briefing de trabalho** | **Emito** | Item priorizado, dono nomeado, autonomia concedida declarada, vinculo a Capability valido | Recebedor devolve se o escopo nao couber no seu dominio (HO-02) |
| **Estado e bloqueio do ciclo** | **Recebo** | Estado com evidencia; bloqueio com causa nomeada | Reporte sem evidencia e devolvido (RP-01) |
| **Veredito de aptidao para aprovacao** | **Recebo** de DEP-QAR | Executor ≠ produtor declarado; seis sinais observaveis | **Produtor = DEP-EXE** — devolvo por impedimento (I-2) |
| **Conflito para arbitragem** | **Recebo** | As duas posicoes registradas, com a fronteira em disputa nomeada | Conflito de **norma** vai a DEP-GOV, nao a mim (FND-02 §7, N3) |

> **Handoff devolvido duas vezes pelo mesmo motivo indica defeito de fronteira** (HO-03,
> FND-02 §9.2) — e aqui a escalada nao sobe: **DEP-EXE ja e o destino da escalada**. Quando o
> defeito de fronteira e do proprio desenho de DEP-EXE, o destino e o **SOBERANO** (E4).

## 9. Memoria autorizada e politica de contexto

| Camada | Meu papel | Sob que condicao |
|---|---|---|
| **EST** | **Leitor obrigatorio** antes de qualquer decisao C2/C3 | Nao escrevo: escrita em EST e de DEP-GOV, mediante ADR (FND-06 §3.1) |
| **PRD** | Leitor | Antes de priorizar item de produto |
| **TEC** | Leitor | Antes de arbitrar disputa de natureza tecnica |
| **OPR** | **Escritor** | Portfolio, fila, alocacao e estado do ciclo corrente |
| **APR** | **Contribuinte obrigatorio**; DEP-KMS e o dono | Toda licao sobre priorizacao, arbitragem e ganho previsto que nao se confirmou |

### 9.1 Politica de contexto
| Item | Valor |
|---|---|
| Pacote minimo para operar | Nucleo obrigatorio *(FND-01 + FND-03 integrais; FND-09 §5/§6.2/§8.2 e FND-10 §2/§4 por recorte)* + **FND-02** + `capabilities/README §10.1` |
| Custo medido do pacote | **1.579 linhas**, medido em 2026-07-28 *(1.099 do nucleo + 479 de FND-02 + 1 linha da projecao)* |
| Gatilho para carregar alem do minimo | **Item entrando na fila.** Carrega-se o **recorte de decisao** da Carta do departamento envolvido — 111 a 115 linhas —, nunca a Carta inteira nem o acervo (PC-01, CE-01) |
| **Nao** carrego por padrao | As quatro Cartas de Capability que custodio; as Cartas integrais dos departamentos que coordeno; perfil `arquivo`; [MEM-EST-0001](../../memory/estrategica/MEM-EST-0001-contexto-do-soberano.md), que permanece `aprovado` e **nao vigente** |

> **O caso que mais tenta violar CE-01.** Coordenar sugere carregar tudo o que se coordena. As
> quatro Cartas de Capability que custodio custam **641 linhas** medidas *(161+159+161+160)*, e
> as Cartas integrais dos departamentos coordenados custam mais ainda — para responder perguntas
> que o **recorte de decisao** de cada Carta responde com **111 a 155 linhas**. Coordenar nao e
> conhecer o interior de cada dominio; e saber a quem ele pertence e se aquele dono pode decidir
> aquilo.

## 10. Riscos, impedimentos e segregacao

> **Secao obrigatoria (DC-03).** Sem ela a Carta nao e valida.

| # | Materia em que estou impedido | Por que | **Quem me substitui** | Fonte |
|---|---|---|---|---|
| **I-1** | **Revisar, verificar ou aprovar esta Carta** — que eu mesmo escrevi | E o instrumento que define a minha propria autoridade; autor nao se verifica | **DEP-GOV** *(revisa)* · **DEP-QAR** *(verifica B4, B9 e B12)* · **SOBERANO** *(aprova e ratifica)* | RM-06b, LV-03, PI-05; FND-09 §8.2 |
| **I-2** | **Aprovar `FIT` ou `REV` cujo objeto avaliado eu tenha produzido** | Quem produz nao aprova o parecer sobre o proprio produto | **DEP-GOV** aprova em meu lugar; se tambem impedido, **SOBERANO** | PI-05, GV-04, FT-02; precedente **FIT-2026-003**, aprovado por DEP-GOV |
| **I-3** | **Priorizar, avaliar, instruir ou alocar DEP-GOV e DEP-QAR** | A independencia da Guarda nao se dilui por coordenacao | **Ninguem** — a Guarda responde ao **Nivel 0** diretamente | **ES-02, IV-01**; FND-02 §2.1; FND-09 §6.2, R-07 |
| **I-4** | **Liberar QG-0 sobre pedido que eu mesmo formulei** sem registro do motivo | Portao autoliberado sem rastro e portao pulado | **DEP-GOV** confere a liberacao; motivo registrado e condicao | FND-01 §6.2, regra de portao |
| **I-5** | **Decidir merito** — tecnico, de produto, de qualidade ou de norma | Coordenar nao concede autoridade sobre o coordenado | DEP-ENG · DEP-PRD · DEP-QAR · DEP-GOV, cada um no seu dominio | **MT-09**; FND-01 §7.3 |
| **I-6** | **Reverter veto da Guarda**, ainda que a fila sofra | Veto de Guarda so cai por decisao registrada do Soberano | **SOBERANO** | LV-09; FND-02 §2.1 |
| **I-7** | **Criar ou encerrar produto; alterar a estrutura organizacional** | Sao materias do Soberano, com consulta obrigatoria a mim — nao decisao minha | **SOBERANO** | FND-01 §7.3 |
| **I-8** | **Aprovar Carta de Departamento**, inclusive as que escrevo | Autor nao aprova; e aqui o aprovador e indelegavel | **SOBERANO** | FND-09 §8.2, linha `DEP`; **DC-09** |
| **I-10** | **Definir, redigir ou alterar o conteudo da `Spec` que eu libero em `QG-1`** | Liberar o portao **nao** concede autoridade sobre o artefato verificado; escopo e criterio de aceite sao materia de DEP-PRD | **DEP-PRD** | FND-01 §6.2, nota pos-ADR-0018; **I-5**; **MT-09**; FND-01 §7.3 |
| **I-9** | **Alterar Carta de Capability** para acomodar decisao de portfolio | A fonte prevalece sobre a projecao | Rito de FND-08 §6.3; ratifica SOBERANO se `nucleo` | PR-2, PR-3; PJ-03 |

> **I-1 e o impedimento sem substituto na proposicao, e isso esta declarado.** DEP-GOV pode
> revisar, DEP-QAR pode verificar e o SOBERANO pode aprovar — mas **ninguem alem de DEP-EXE
> pode propor** uma Carta de Departamento (FND-09 §8.2). O impedimento e **parcial por
> construcao da matriz**: alcanca revisao, verificacao e aprovacao, e **nao alcanca a autoria**.
> Resolve-lo exigiria emendar FND-09 §8.2 — **C3**. Registrado como achado **IC-3**, dono
> DEP-GOV, gatilho **primeira Carta de Departamento escrita apos a existencia de agentes**.

### 10.1 Riscos proprios do dominio
| # | Risco | Probabilidade | Impacto | Mitigacao declarada |
|---|---|---|---|---|
| RX-1 | **Coordenacao virar merito** — arbitrar entre areas e, no ato, decidir o conteudo | **Media** | **Alto** | I-5. Toda arbitragem registra **a fronteira em disputa**, nao a solucao tecnica. Arbitragem que prescreva o *como* e devolvida por DEP-GOV |
| RX-2 | **Diluicao da independencia da Guarda** por via de fila e alocacao | Baixa | **Alto** | I-3 e ES-02. Guarda **nao** recebe briefing nem prioridade de DEP-EXE; o unico canal e a DIRETIVA do Soberano |
| RX-3 | **Impedimento cruzado** — DEP-EXE produz o objeto e e o aprovador previsto do `FIT` | **Observado — 1 ocorrencia** | Medio | **FIT-2026-003 foi aprovado por DEP-GOV**, e nao por DEP-EXE, exatamente por isso. E o achado **C5** de REV-CONSOLIDACAO, dono DEP-GOV, e o **RQ-2** da Carta de DEP-QAR |
| RX-4 | **Amplitude excessiva** — 4 Capabilities contra o limite de 3 de VC-03 | **Observado** | Medio | Achado **P6**; avaliacao em §12.1, com decisao de **nao** especializar e custo declarado |
| RX-5 | **A3 como autoridade generica** — tratar o nivel de autonomia como licenca de materia | Media | **Alto** | A3 e **profundidade** de decisao, nunca **extensao** de materia. §5 lista materias nominalmente; materia ausente de §5 **nao** e decidida por DEP-EXE, qualquer que seja o nivel |
| RX-6 | **Fila sem contrapartida de consolidacao** — priorizar sempre criar, nunca fundir | **Observado — 5 ciclos** | **Alto** | R3 de FIT-2026-005: cinco missoes de crescimento, **zero** consolidacoes. X-12 e a autoridade de abrir EV-08, e ela **nao foi exercida nenhuma vez** |
| RX-8 | **`QG-1` virar gargalo, ou virar via para decidir escopo** | **Media** | **Alto** | O portao verifica **presenca e verificabilidade por terceiro**, nao merito (FND-01 §6.2). **I-5** e **I-10** vedam decidir escopo, e liberacao **com motivo registrado** e condicao. Riscos herdados de `RS-1` e `RS-2` de [ADR-0018](../../decisions/ADR-0018-liberacao-do-portao-qg-1.md), **agora com titular declarado em Carta** |
| RX-7 | **Autoria concentrada** — DEP-EXE e autor das quatro Cartas existentes | **Observado — 4 de 4** | Medio | R1 de FIT-2026-005. Um contrato exercido pelo proprio autor mede a autoria, nao a regra. Mitigacao: a medicao de **devolucoes** de §11, KX-10 |

### 10.2 Incompatibilidades de papel
| Papel A | Papel B | Por que nao se acumulam na mesma mudanca |
|---|---|---|
| Autor da Carta | Revisor ou aprovador da mesma Carta | RM-06b, LV-03 — e a razao de I-1 |
| Produtor do objeto avaliado | Aprovador do `FIT` sobre ele | PI-05, GV-04 — e a razao de I-2 |
| Coordenador | Verificador do coordenado | ES-02 — Comando nao verifica; Guarda nao e coordenada |
| **Liberador de `QG-1`** | **Autor ou revisor da `Spec` liberada** | FND-01 §6.2, *Regra de portao*; PI-05 — e a razao de **I-10** |
| Arbitro do conflito | Parte no conflito | FND-04 §3.1 — se DEP-EXE for parte, arbitra o **SOBERANO** |
| Autor do contrato *(ADR-0011)* | Unico avaliador do proprio contrato | PI-05 — a validacao interclasses e desenhada e executada por DEP-QAR e DEP-GOV |

## 11. Indicadores

> Indicador **sem valor medido** declara-se `definido, sem valor`. Afirmar desempenho sem
> medida e LV-12.

| # | Indicador | Definicao | Direcao | **Valor medido** | **Data** |
|---|---|---|---|---|---|
| KX-1 | Capabilities custodiadas | Contagem na projecao de capabilities/README §10.1 | estavel | **4** | 2026-07-28 |
| KX-2 | Custodias exercidas tambem por outro departamento | Contagem — membros de OW-02 | — | **1** *(`CAP-comunicacao`, por DEP-KMS)* | 2026-07-28 |
| KX-3 | Artefatos de que sou **aprovador** | `grep "^aprovador: DEP-EXE"` no acervo | — | **24** | 2026-07-28 |
| KX-4 | Artefatos de que sou **autor** | `grep "^autor: DEP-EXE"` no acervo | — | **32** — dos quais **24** em `capabilities/` | 2026-07-28 |
| KX-5 | Cartas de Departamento de que sou autor | Contagem em `departments/*/carta.md` | — | **4 de 4** — 100% | 2026-07-28 |
| KX-6 | Vereditos de aptidao (`FIT`+`REV`) aprovados por mim | Contagem do campo `aprovador` | — | **8 de 11** | 2026-07-28 |
| KX-7 | Vereditos que **nao** aprovei por impedimento | Contagem | — | **1** — FIT-2026-003, aprovado por DEP-GOV | 2026-07-28 |
| KX-8 | Propostas de consolidacao (EV-08) abertas | Contagem | ↑ **e nao-zero** | **0** — em **5** ciclos | 2026-07-28 |
| KX-9 | Excecoes formais vigentes sob minha fila | Contagem em `governance/exceptions/` | → 0 | **0** | 2026-07-28 |
| KX-10 | **Itens de checklist devolvidos** na revisao de Carta | Devolvidos / submetidos | **nao-zero** | **`definido, sem valor`** — a medicao de devolucoes so tem sentido a partir de uma Carta escrita por **autor distinto**, que nao existe | — |
| KX-11 | Arbitragens N2 registradas | Contagem de conflitos entre Linha resolvidos por mim | — | **`definido, sem valor`** — nenhum conflito N2 ocorreu; nao ha producao concorrente | — |
| KX-12 | Ciclos abertos e fechados | Contagem de aberturas e fechamentos declarados | — | **`definido, sem valor`** — o ciclo organizacional **nao e artefato** e nao tem registro proprio no acervo | — |
| KX-13 | Custo e consumo por ciclo | Serie da funcao Recursos (FIN) | — | **`definido, sem valor`** — FIN e funcao nomeada sem carga; nenhum orcamento foi movimentado | — |
| KX-14 | Aderencia da fila a prioridade declarada | Executado / priorizado | ↑ | **`definido, sem valor`** — sem fila registrada, nao ha aderencia a medir | — |
| KX-15 | **Liberacoes de `QG-1`** | Contagem de portoes liberados, com responsavel e data | — | **0** — **nenhuma `Spec` existe** (`RD-33`) | 2026-07-29 |

**Contagem: 15 indicadores definidos · 10 com valor medido · 5 `definido, sem valor`.**

> **Os cinco sem valor dependem de operacao continua**, que nao existe nesta fase — nao de
> omissao. **KX-8 e o indicador mais desconfortavel desta Carta, e por isso esta medido e nao
> omitido:** a autoridade de abrir consolidacao existe, e foi exercida **zero** vezes em cinco
> ciclos de crescimento. E o mesmo fato que R3 de FIT-2026-005 registra, visto do lado de
> **quem tem a autoridade de agir** em vez do lado de quem mede o acervo.

## 12. Ciclo de vida — especializacao, fusao e retirada

### 12.1 Gatilhos de especializacao
| Gatilho *(FND-02 §9.2)* | Aplica-se? | **Sinal ja observado** | Movimento previsto |
|---|---|---|---|
| **Escopo heterogeneo** | **Sim, com sinal** | Custodio de quatro naturezas distintas: direcao *(estrategia)*, orquestracao *(coordenacao)*, **custo** *(financeiro)* e **transferencia de contexto** *(comunicacao)*. **Contagem: 4 > 3** (VC-03) | Promover **Recursos (FIN)** a departamento proprio — o candidato ja nomeado em FND-02 §3 |
| **Carga concentrada** | **Nao avaliavel** | **Nenhum** — nenhuma serie de carga por Capability; KX-11 a KX-14 sem valor | — |
| Gargalo de decisao | **Nao** | **Nenhum** — 0 escalonamentos E2 registrados por fila | — |
| Contexto excessivo | **Nao** | Pacote minimo medido em **1.579 linhas**, **6,0%** do acervo | — |
| Fronteira em disputa | **Nao** | **Nenhum** conflito recorrente registrado com qualquer area | — |
| Duplicacao | **Nao** | **Nenhum** procedimento refeito em lugar diferente | — |

> **Decisao registrada: nao especializar** (FND-04 §6.2, SE-06). **SE-02 exige dois sinais
> observados e ha um** — a contagem de VC-03. O candidato natural, **FIN**, e explicitamente
> uma **funcao nomeada** em FND-02 §3 e §8.4, promovivel *"quando a carga justificar"*; a carga
> e **zero** (KX-13). Promover agora inverteria ES-04: criaria area para responsabilidade que
> **nao tem volume**, exatamente o que ES-03 proibe. **Custo assumido:** DEP-EXE opera acima do
> limite de VC-03 ate a 1a revisao estrutural; o custo esta declarado, nao invisivel (PI-14
> regra 2). **Esta Carta e o gatilho de P6, e P6 permanece aberto com a avaliacao feita.**

### 12.2 Gatilhos de fusao ou consolidacao
| Sinal *(FND-02 §9.3)* | Com quem | O que indicaria |
|---|---|---|
| Duas areas que sempre atuam juntas e nunca isoladas | **Nenhuma** | DEP-EXE atua com todas e depende de nenhuma para existir |
| Componente sem acionamento ao longo de um horizonte | **funcao FIN** | Que a hipotese de custo relevante nao se confirmou — sinal de **retirar a funcao**, nao de promove-la |
| Custo de coordenacao maior que o ganho | — | Nenhum sinal registrado |

> **Fusao de DEP-EXE com qualquer departamento e estruturalmente vedada.** Fundir com a Linha
> poria o coordenador dentro do coordenado; fundir com a Guarda quebraria **PI-05** e **ES-02**;
> fundir com a Plataforma poria quem prioriza dentro de quem serve. Qualquer uma exigiria
> **emenda C3** a FND-02. Registrado para que a hipotese nao seja levantada sem o rito.

### 12.3 Criterio de extincao
DEP-EXE deixa de ser necessario apenas se a organizacao deixar de ter mais de um trabalho
possivel ao mesmo tempo — condicao em que priorizar perde objeto. Na extincao, cada
responsabilidade e cada custodia recebe destino explicito (IV-07, FND-02 §8.3):

| Responsabilidade / custodia | Destino declarado na extincao |
|---|---|
| Custodia de `CAP-estrategia` *(`nucleo`)* | **Nunca** a departamento de classe Suporte (OW-04). Transferencia e C2 com ADR e ratificacao do SOBERANO (OW-06) |
| Custodia de `CAP-coordenacao`, `CAP-financeiro`, `CAP-comunicacao` | Destino explicito obrigatorio; competencia orfa e tao proibida quanto responsabilidade orfa (IV-07) |
| **Portao QG-0** | Destino explicito obrigatorio. **Portao sem dono e portao pulado**, e QG-0 e o primeiro de todos |
| **Portao `QG-1`** | Destino explicito obrigatorio. **Nunca** a **DEP-PRD** — quem produz a spec nao libera o portao que a verifica (FND-01 §6.2, *Regra de portao*) — e **nunca** a **DEP-ENG** — quem constroi nao define (`DEP-PRD §12.3`) |
| **Aprovacao de `FIT`, `AGT`, `SUB` e `SKL`** | Reatribuida por emenda a FND-09 §8.2 — **C3**. Sem ela, quatro entidades ficam **sem aprovador** |
| **Autoria de Carta de Departamento** | Reatribuida por emenda a FND-09 §8.2 — **C3**. Sem ela, **nenhuma Carta nova pode nascer** |
| Arbitragem entre areas de Linha | Sobe ao **SOBERANO**, unico papel acima |
| Funcao **Recursos (FIN)** | Rehospedada em departamento nomeado, ou promovida no mesmo ato |

> **A extincao de DEP-EXE e a mais cara do sistema, e o motivo esta na tabela:** duas linhas
> exigem **emenda C3 a FND-09 §8.2** so para que o restante continue funcionando.

### 12.4 Funcoes internas nomeadas
| Funcao | Responsabilidade | Gatilho de promocao |
|---|---|---|
| **Recursos (FIN)** | Custo, consumo e limites; custodia operacional de `CAP-financeiro` | **Carga que justifique** (ES-04, FND-02 §3 e §8.4) — hoje **zero** (KX-13) |
| **Portfolio** | Composicao do que a organizacao faz ao mesmo tempo | Segundo produto ativo simultaneo |

## 13. Resumo operacional, carregamento e rastreabilidade

### 13.1 Resumo operacional
Converte a direcao do Soberano em prioridade executavel, aloca capacidade, arbitra entre areas
de Linha e responde pela entrega do que foi priorizado.

### 13.2 Perfil minimo de carregamento
| Recorte | Para que serve | Custo **medido** | Data |
|---|---|---|---|
| Secoes 1, 2 e 4 | Saber o que DEP-EXE faz e o que nao faz | **63 linhas** | 2026-07-28 |
| + secoes 5 e 10 | Decidir se DEP-EXE pode decidir, liberar ou aprovar algo | **172 linhas** | 2026-07-29 |
| Carta integral | Auditoria, revisao estrutural, extincao | **506 linhas** | 2026-07-29 |

> Carregar alem do recorte aplicavel exige **gatilho declarado** (CE-01, PC-01). O recorte de
> decisao custa **34% da Carta** — medido por `sed`+`wc -l` sobre os intervalos das secoes.
> **A proporcao e maior que a das duas primeiras Cartas** *(29% em ambas)*, e a causa e
> declarada: a classe Comando concentra materia em B4 e impedimento em B9, que sao justamente
> as duas secoes do recorte.

### 13.3 Rastreabilidade
| Campo | Conteudo |
|---|---|
| ADR de criacao do departamento | [ADR-0001](../../decisions/ADR-0001-adocao-da-fundacao-organizacional.md) — adota FND-02, que cria os nove departamentos |
| ADR do contrato desta Carta | [ADR-0011](../../decisions/ADR-0011-contrato-de-carta-de-departamento.md) |
| RFC de origem | [RFC-0008](../../rfcs/RFC-0008-contrato-de-carta-de-departamento.md) |
| Decisoes que moldam esta Carta | ADR-0002 *(vinculacao a Capability)* · ADR-0004 *(`FIT`, aprovado por DEP-EXE)* · ADR-0011 *(contrato)* · **ADR-0018** *(`QG-1` passa a ser liberado por DEP-EXE)* · **ADR-0019** *(aprovador de Spec conforme a classe)* |
| Alteracoes (ADRs) | [**ADR-0023**](../../decisions/ADR-0023-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md) — propagacao de `ADR-0018` e `ADR-0019` |
| Fonte da custodia e do exercicio | frontmatter de `capabilities/CAP-estrategia.md`, `CAP-coordenacao.md`, `CAP-financeiro.md`, `CAP-comunicacao.md` |
| Achados que esta Carta **dispara** | **P6** *(VC-03 em DEP-EXE)* — gatilho *"Carta de DEP-EXE"*, avaliado em §12.1 |
| Achados que esta Carta **abre** | **IC-2** *(colisao do termo "ratifica")* · **IC-3** *(impedimento sem substituto na proposicao)* |
| Achado que esta Carta **fecha** | **RD-31**, quanto a DEP-EXE — o portao `QG-1` passa a ter **titular declarado em Carta**, onde antes tinha **0 ocorrencias** |
| Validacao em cenarios | [REV-INTERCLASSES §3](../../foundation/revisao-arquitetural-validacao-interclasses-2026-07-28.md) |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.1.0 | 2026-07-29 | DEP-EXE | Emenda **C2 · Tipo 2** por **ADR-0023**, que **propaga** `ADR-0018` e `ADR-0019` — ambos **ratificados** — a esta Carta, fechando **RD-31** quanto a DEP-EXE. **O portao `QG-1` passa a ter titular declarado em Carta, onde antes tinha `0` ocorrencias medidas.** **Onze blocos alterados:** `§3` *(responsabilidade **X-13**)*, `§5` *(liberacao de `QG-1` e aprovacao de Spec `C2`)*, `§5.2` *(o portao na tabela, e a nota que explica por que `QG-1` **satisfaz** a regra de portao em vez de excepciona-la)*, `§6.1` *(entrada: spec submetida)*, `§6.2` *(saida: registro da liberacao)*, `§7` *(o tipo `SPC`)*, `§10` *(impedimento novo **I-10** — liberar o portao nao concede autoridade sobre o artefato)*, `§10.1` *(risco novo **RX-8**)*, `§10.2` *(incompatibilidade de papel)*, `§11` *(indicador **KX-15**, com valor **0** medido)*, `§12.3` *(destino do portao na extincao)* e `§13.3`. **Nenhum titular, portao, papel, classe ou direito decisorio foi criado:** `QG-1` e de DEP-EXE por **ADR-0018** e a aprovacao de `C2` e de DEP-EXE por **FND-04 §2**, ambos anteriores a esta emenda; **7 portoes antes, 7 depois**; **DEP-ENG e DEP-QAR permanecem os revisores da Spec** e **DEP-PRD segue decidindo escopo e criterio de aceite**. **I-5 e I-10 vedam expressamente que o portao vire via para decidir merito.** |
| 1.0.0 | 2026-07-28 | DEP-EXE | Criacao como piloto da classe **Comando**, sob o contrato de ADR-0011. Doze blocos preenchidos. Permanece em `em-revisao`: aprovar Carta de Departamento e ato do **SOBERANO** (DC-09), e o ato de 2026-07-28 **nao a alcanca** — ela nao existia na data (LM-03, [MSG-2026-0001 §3](../../memory/operacional/MSG-2026-0001-ato-soberano-ratificacao-cartas-piloto.md)). |
| 1.2.0 | 2026-08-02 | DEP-EXE | Emenda **C3 · Tipo 2** por [ADR-0032](../../decisions/ADR-0032-separacao-de-proponente-e-aprovador-na-spec-c1.md), **propagacao obrigatoria** (`CV-04`) da emenda de `FND-09 §8.2` **1.6.0** e `FND-11 §5` **1.1.0** que sana **`RD-91`**. **Duas afirmacoes desta Carta ficariam falsas ou incompletas, e as duas foram corrigidas:** `§5` *(aprovar Spec — passa de `C2` para **`C1` ou `C2`**, e a nota `"C0/C1: o proprietario"` passa a `"C0: o proprietario"`)* e `§7` *(linha `Spec` — aprovador em `C1` ou `C2`)*. **Recebo materia, e ela e estreita:** aprovar `Spec` de classe **`C1`**, porque `FND-09 §8.2` poe **DEP-PRD** como proponente de toda `Spec` e `FND-04 §3.1` declara **nula** (`LV-03`) a aprovacao em que `Proponente = Aprovador`. **Nenhuma autoridade nova foi criada:** ja aprovo `Spec` em `C2` desde `ADR-0019`, e `C1` e **degrau abaixo** de `C2` — sem `RFC`, sem `ADR`, sem `FIT`, sem ratificacao. **`I-10` permanece intacto:** aprovar **nao** e definir, redigir ou alterar conteudo de `Spec`, que segue sendo materia de **DEP-PRD** (`FND-01 §7.3`). **Liberar `QG-1` e aprovar continuam atos distintos** (`FND-01 §6.2`, nota pos-`ADR-0018`; `ADR-0019` `H3`), e o acumulo dos dois em `C1` e **o mesmo** que a norma ja aceita em `C2` nesta mesma linha da matriz. **`0` Capabilities, portoes, papeis, impedimentos ou niveis de autonomia alterados** — `A3` antes e depois, **7 portoes antes e 7 depois**. **`0` linhas de historico editadas.** **Nao vigora sem ato** (`LM-02`). |
