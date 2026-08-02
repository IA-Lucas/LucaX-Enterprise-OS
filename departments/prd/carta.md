---
id: DEP-PRD
titulo: Produto e Estrategia
tipo: carta
versao: 1.1.0
status: ativo
camada_memoria: estrategica
autor: DEP-EXE
proprietario: DEP-EXE
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-29
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0001, ADR-0002, ADR-0003, ADR-0011, ADR-0018, ADR-0019, ADR-0023]
substitui: []
substituido_por: null
classe: linha
nivel: 2
nivel_autonomia: A2
responde_a: DEP-EXE
capabilities: [CAP-produto, CAP-pesquisa, CAP-design]
resumo: Define o que deve existir e por que, transformando intencao em problema bem formulado e resultado verificavel.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-GOV
ratificacao: ratificada
---

# Produto e Estrategia (DEP-PRD)

## Proposito
Existir como o ponto em que intencao vira problema bem formulado. Define **o que deve
existir e por que**, com criterio de aceite verificavel e escopo negativo explicito — e
responde pela pergunta que antecede toda construcao, sem responder por como ela e feita.

## Escopo
| Item | Definicao |
|---|---|
| Classe | **linha** |
| Nivel | 2 |
| Responde a | **DEP-EXE** |
| Nivel de autonomia | **A2** — executa e decide Tipo 2 no proprio dominio; Tipo 1 exige aprovacao humana |
| Poder de veto | **Nao** — veto e exclusivo da classe Guarda (FND-02 §2.1) |
| **Nao** inclui | Como implementar, se a entrega passa, e se o produto entra no portfolio. Delimitacao integral na secao 4 |
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

**Missao:** definir o que deve existir e por que, transformando intencao em problema bem
formulado e resultado verificavel.

**Mandato:** decidir **o que** se constroi e **o que fica de fora**, com autoridade sobre
escopo e criterio de aceite funcional — e nenhuma sobre **como** se constroi, **se** a entrega
passa, ou **se** o produto existe no portfolio.

## 2. Capabilities custodiadas e exercidas

> **Declaracao de projecao (PJ-02).** **Fonte:** frontmatter de `capabilities/CAP-produto.md`,
> `CAP-pesquisa.md` e `CAP-design.md`, campos `custodio` e `exercentes`.
> **Campos projetados:** apenas as linhas de DEP-PRD. **Finalidade:** responder "o que custodio
> e o que exerco" sem abrir tres arquivos. **Atualizacao:** pela mesma mudanca que altera a
> Carta de Capability (CV-04). Em divergencia, prevalece a Carta de Capability (PR-1).

| Capability | Dominio · Classe | **Custodia** | **Exercicio** | Por que este departamento |
|---|---|---|---|---|
| [CAP-produto](../../capabilities/CAP-produto.md) | VAL · **`nucleo`** | **sim** | sim | Definir o que deve existir e por que e o nucleo do mandato |
| [CAP-pesquisa](../../capabilities/CAP-pesquisa.md) | VAL · `habilitadora` | **sim** | sim | Saber antes de decidir: o problema precede a solucao |
| [CAP-design](../../capabilities/CAP-design.md) | VAL · `habilitadora` | **sim** | sim | Forma, comportamento e linguagem sao parte do que se define, nao de como se implementa |

**Capabilities que exerco sem custodiar:** nenhuma.
**Capabilities que custodio e sao exercidas por outros:** nenhuma **declarada na fonte**.

> **Custodia no limite de VC-03, e nao acima dele.** Tres vinculos **igualam** o limite de
> **tres** de VC-03; nao o ultrapassam. Diferentemente de DEP-ENG *(5)* e DEP-EXE *(4)*, DEP-PRD
> **nao dispara** o achado **P6** de [capabilities/README §10.3](../../capabilities/README.md).
> As tres pertencem ao **mesmo dominio** `VAL` — homogeneidade que DEP-GOV, com uma unica
> Capability, nao tem.

> **`CAP-produto` e um dos dois maiores fan-outs do catalogo** — defeito nela propaga para
> arquitetura, design, marketing e comercial (`capabilities/README §4.1`). E prioridade de
> indicador, e esta declarada como risco **RP-4**.

## 3. O que possuo — escopo exclusivo

| # | Responsabilidade | Como se verifica que esta sendo cumprida | Capability |
|---|---|---|---|
| P-1 | **Descoberta** — investigar antes de definir | Toda definicao cita o que se investigou e o que ficou desconhecido | CAP-pesquisa |
| P-2 | **Definicao de problema** | O problema esta escrito antes da solucao, e nao a partir dela | CAP-produto |
| P-3 | **Personas e publico** | Publico nomeado, com contexto de uso; "todo mundo" e devolvido | CAP-pesquisa |
| P-4 | **Specs e requisitos** | Toda spec declara resultado, criterio de aceite e o que fica fora (FND-04 §6) | CAP-produto |
| P-5 | **Criterios de aceite funcionais** | Verificaveis por terceiro, declarados **antes** da construcao | CAP-produto |
| P-6 | **Roadmap de produto e sua justificativa** | O que foi despriorizado consta, com o motivo (FND-06 §3.2) | CAP-produto |
| P-7 | **Priorizacao dentro do produto** | Ordem de valor declarada; nao confundir com a fila organizacional, que e de DEP-EXE | CAP-produto |
| P-8 | **Completude da spec submetida a `QG-1`** | Nenhuma spec e submetida a `QG-1` sem resultado, criterio de aceite e escopo negativo presentes e verificaveis por terceiro. **Liberar o portao e de DEP-EXE** (FND-01 §6.2, pos-ADR-0018) | CAP-produto |
| P-9 | **Escopo negativo** — o que o produto deliberadamente nao faz | Registrado na camada PRD, com o motivo (FND-06 §3.2) | CAP-produto |
| P-10 | **Forma, comportamento e linguagem do produto** | Decisao de design registrada antes da construcao; linguagem do dominio declarada | CAP-design |
| P-11 | **Hipoteses e sua validacao** | Hipotese entra **marcada como hipotese**, com o teste que a confirmaria; invalidada **nao e apagada** (MM-09) | CAP-pesquisa |
| P-12 | **Camada de memoria PRD** — dono do conteudo | Todo fato duravel sobre o produto vive em uma camada so (MM-01) | CAP-produto |

## 4. O que NAO me compete

| Materia | Dono real | Fonte |
|---|---|---|
| Decidir **como** construir; arquitetura, padrao tecnico e modelo de dados | DEP-ENG | FND-02 §3; FND-01 §7.3 |
| Decidir se a entrega **passa** ou e devolvida; medir risco | DEP-QAR | FND-02 §3; QG-3 |
| **Criar ou encerrar produto** — a decisao de portfolio | **SOBERANO** | FND-01 §7.3; FND-02 §3 |
| Definir prioridade **entre** produtos, fila e alocacao de capacidade | DEP-EXE | FND-02 §3 |
| Julgar forma, conformidade e rastreabilidade | DEP-GOV | FND-04 §12 |
| Decidir **como comunicar** ao publico, por qual canal e com qual mensagem | DEP-GRW | FND-02 §3 |
| Declarar qual **ferramenta externa** e oficial | DEP-TLS | FND-02 §3 |
| **Operar** o que foi construido; rotina e incidente operacional | DEP-OPS | FND-02 §3 |
| Decidir onde um registro de memoria pertence, e o que expira | DEP-KMS | FND-02 §3; FND-06 §2.1 |
| **Estimar** prazo ou esforco tecnico | DEP-ENG | FND-02 §3 |
| Alterar Carta de Capability para acomodar esta Carta | custodio da Capability | PR-2, PR-3 de ADR-0011 |
| **Liberar o portao `QG-1`** sobre a spec que eu escrevo | **DEP-EXE** | FND-01 §6.2, *Regra de portao* e nota pos-[ADR-0018](../../decisions/ADR-0018-liberacao-do-portao-qg-1.md) |
| **Aprovar a Spec de classe `C2` ou `C3`** que eu escrevo | **DEP-EXE** *(`C2`, com parecer de DEP-GOV)* · **SOBERANO** *(`C3`)* | FND-04 §2; FND-09 §8.2, linha `SPC`, pos-[ADR-0019](../../decisions/ADR-0019-aprovador-e-ratificador-de-spec.md) |
| **Aprovar a propria Carta, ou revisa-la** | **SOBERANO** *(aprova)* · **DEP-GOV** *(revisa)* | RM-06b; FND-09 §8.2 |

## 5. O que decido — autoridade e portoes

| Materia | Autonomia | Consulta obrigatoria | **Fonte da autoridade** |
|---|---|---|---|
| **Escopo do produto** e o que fica fora | A2 | DEP-ENG *(viabilidade)*, DEP-EXE *(prioridade)* | FND-01 §7.3, *Escopo e prioridade de produto*; FND-02 §3 |
| **Ordem de valor** dentro do produto | A2 | DEP-EXE | FND-02 §3 |
| Quando um requisito esta **suficientemente definido** | A2 | DEP-ENG | FND-02 §3 |
| **Criterio de aceite funcional** | A2 | DEP-QAR *(verificabilidade)* | FND-02 §3; QG-1 |
| **Submissao da spec a `QG-1`** — declarar que os tres itens estao presentes e verificaveis | A2 | DEP-QAR *(verificabilidade)* | FND-01 §6.2, nota *"Sobre QG-1 e a regra de portao"*. **A liberacao do portao e de DEP-EXE** |
| **Aprovar Spec** (`SPC`) **de classe `C0` ou `C1`**, como proprietario | A2 | DEP-ENG + DEP-QAR *(revisores)* | FND-09 §8.2, linha `SPC`: **aprova conforme classe (FND-04 §2)**, com **`C1` como piso** (FND-04 §6). **`C2` aprova DEP-EXE; `C3`, o SOBERANO** |
| **Propor** Carta de Produto | A2 | DEP-QAR *(revisor)* | FND-09 §8.2, linha `PRO`: propoe/cria |
| Decisao de **design** — forma, comportamento e linguagem | A2 | DEP-ENG *(viabilidade)*, DEP-GRW *(consistencia de linguagem)* | FND-02 §3, "Possui"; `CAP-design` |
| **Curadoria da camada PRD** | A2 | DEP-KMS *(alocacao entre camadas)* | FND-06 §2.1 |

> **A homologacao de escopo e prioridade de produto e de DEP-EXE** (FND-01 §7.3). **`IR-11`:
> o termo e homologacao, nunca ratificacao** — ratificar e ato exclusivo do Soberano
> ([ADR-0012 §5.4](../../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md)).

### 5.1 O que **nao** decido
| Materia | Quem decide | Fonte |
|---|---|---|
| **Criar ou encerrar produto** | **SOBERANO** | FND-01 §7.3; FND-09 §8.2, linha `PRO` |
| **Aprovar e ratificar Carta de Produto** | **SOBERANO** | FND-09 §8.2, linha `PRO` |
| **Liberar `QG-1`** | **DEP-EXE** | FND-01 §6.2, pos-ADR-0018 |
| **Aprovar Spec `C2` ou `C3`** | **DEP-EXE** *(`C2`, com parecer de DEP-GOV)* · **SOBERANO** *(`C3`)* | FND-04 §2; FND-09 §8.2, linha `SPC` |
| Se a entrega passa em QG-3 | **DEP-QAR** | FND-01 §6.2 |
| Como se constroi | **DEP-ENG** | FND-01 §7.3 |
| Prioridade **entre** produtos | **DEP-EXE** | FND-02 §3 |
| Posicionamento e comunicacao externa | **DEP-GRW**, com ratificacao do **SOBERANO** | FND-01 §7.3 |
| **Aprovar esta Carta** | **SOBERANO** | DC-09 |

### 5.2 Portoes sob minha responsabilidade

**Nenhum.** Desde [ADR-0018](../../decisions/ADR-0018-liberacao-do-portao-qg-1.md), `QG-1` — o
portao da propria Spec — e liberado por **DEP-EXE** (FND-01 §6.2). DEP-PRD **produz** o artefato
que o portao verifica, e por isso **nao pode libera-lo**: a *Regra de portao* de FND-01 §6.2
proibe que o portao seja liberado por quem produziu o artefato.

| Portao | Meu papel | O que entrego antes dele | Fonte |
|---|---|---|---|
| **QG-1** | **Submetido — nunca liberador** | A spec com **resultado**, **criterio de aceite** e **o que esta fora**, os tres verificaveis por terceiro; escopo negativo explicito; publico nomeado | FND-01 §6.2; FND-04 §6, linha *Spec* |

> **Nenhum portao novo e criado aqui, e nenhum e transferido aqui.** Os sete sao de FND-01 §6.2;
> acrescentar e **C3**, e a titularidade de `QG-1` foi determinada por **ADR-0018**, ratificado.
> **Liberar o portao nao e aprovar o artefato** (FND-01 §6.2): DEP-EXE confirma **presenca e
> verificabilidade por terceiro**; **DEP-PRD segue decidindo o escopo**; e o veto de **DEP-QAR**
> sobre criterio de aceite nao verificavel permanece integral (LV-09). **O contraditorio que
> `RP-1` declarava ausente passa a existir antes do portao, e nao depois.**

## 6. Interfaces — entradas, saidas e consumidores

### 6.1 Entradas
| De quem | O que recebo | Em que forma | Gatilho |
|---|---|---|---|
| **DEP-EXE** | Prioridade, alocacao, briefing, decisao de portfolio do Soberano | **DIRETIVA**, com `nivel_autonomia_concedido` | Abertura de ciclo |
| **SOBERANO** *(via DEP-EXE)* | Criacao ou encerramento de produto; mudanca de posicionamento | DIRETIVA | Ato do Soberano |
| DEP-ENG | Avaliacao de viabilidade, estimativa, restricao tecnica | **CONSULTA** respondida | Antes de fechar escopo |
| DEP-QAR | Parecer sobre verificabilidade do criterio de aceite; defeito de spec devolvido em QG-3 | REPORTE | QG-1 e QG-3 |
| DEP-GOV | Parecer de conformidade, classe de mudanca validada | CONSULTA | Antes de propor mudanca |
| **DEP-GRW** | Sinal de mercado, objecao, motivo de perda | **HANDOFF** | Contato com o publico |
| **DEP-OPS** | Sinal de uso real, incidente operacional recorrente | REPORTE | Operacao |
| DEP-KMS | Pacote de contexto; licoes da camada APR | REPORTE | QG-0 |

### 6.2 Saidas
| Entrega | Destinatario | Formato | Cadencia | Consumidor final |
|---|---|---|---|---|
| **Spec** | **DEP-ENG** | **HANDOFF**, artefato `SPC` | Por item priorizado | Quem constroi |
| **Criterio de aceite funcional** | DEP-ENG + DEP-QAR | Parte da spec | Por item | Quem verifica |
| **Roadmap e sua justificativa** | DEP-EXE + SOBERANO | REPORTE | Por ciclo | Quem prioriza o portfolio |
| **Escopo negativo** | DEP-ENG, DEP-QAR, DEP-GRW | Registro em camada **PRD** | Por produto | Quem poderia prometer o que nao existe |
| **Decisao de escopo registrada** | DEP-EXE | Nota de Decisao ou `ADR`, conforme a classe | Por decisao | Toda a organizacao |
| **Definicao de sucesso do produto** | DEP-EXE + SOBERANO | Parte da Carta de Produto | Por produto | Quem decide continuar ou encerrar |
| **Decisao de design** | DEP-ENG, DEP-GRW | Registro em camada **PRD** | Por decisao | Quem constroi e quem comunica |
| **Carta de Produto proposta** | DEP-QAR *(revisor)* → **SOBERANO** | Artefato `PRO` | Por produto | Quem aprova e ratifica |
| Aprendizado de produto | DEP-KMS | REPORTE, secao Aprendizado | A cada encerramento | Camada APR |

### 6.3 Natureza da interacao
| Departamento | Natureza | O que trafega |
|---|---|---|
| DEP-EXE | **entrega** | Roadmap, decisao de escopo, escalonamento |
| DEP-GOV | consulta | Conformidade — DEP-GOV **veta** DEP-PRD, nunca o inverso |
| DEP-QAR | consulta | Verificabilidade e risco — DEP-QAR **veta** DEP-PRD, nunca o inverso |
| **DEP-ENG** | **entrega** | Spec, criterio de aceite, escopo negativo. **PRD entrega a ENG, nunca o inverso** (FND-02 §4) |
| **DEP-GRW** | **entrega e consulta** | Escopo e escopo negativo entregues; sinal de mercado consultado |
| DEP-OPS | **consulta** | Sinal de uso real recebido |
| DEP-TLS | consulta | Capacidade externa necessaria ao produto |
| DEP-KMS | **entrega** | Aprendizado e definicao de produto gravados |

> A matriz completa de interacao vive em **FND-02 §4** e **nao** e reproduzida aqui: esta
> secao declara apenas as linhas de DEP-PRD (DC-08).

## 7. Artefatos e registros mantidos

| Tipo documental | Entidade | Meu papel | Onde vive |
|---|---|---|---|
| **Spec** | `SPC` | **Autor e proponente**; **aprovador apenas quando a classe do efeito for `C0` ou `C1`** (FND-04 §2); **nunca revisor do proprio** e **nunca liberador de `QG-1`** | fase futura — `products/<slug>/specs/` |
| **Carta de Produto** | `PRO` | **Autor e proponente**; nunca aprovador nem ratificador | fase futura — `products/` |
| Memoria **PRD** | `MEM` | **Dono da camada** | `memory/produto/` |
| **ADR** *(de escopo)* | `ADR` | **Autor**; nunca aprovador do proprio | `decisions/` |
| **RFC** *(de produto)* | `RFC` | **Autor** | `rfcs/` |
| **Nota de Decisao** *(C1 de escopo)* | `ADR` derivado | **Autor**, com revisor de papel distinto | `decisions/` |
| Carta de Agente / Subagente de DEP-PRD | `AGT` `SUB` | **Autor**, quando o agente for desta area | fase futura |
| **Reporte / Consulta** | `MSG` | **Emissor** | `memory/operacional/` |

> **Nenhum produto, projeto ou spec existe nesta fase**, por determinacao: `products/` e
> `projects/` **nascem quando o primeiro artefato do tipo for aprovado** (FND-03 §7.2). Tipo
> documental que nao conste de [FND-10 §4](../../foundation/10-artifact-framework.md) nao
> existe (CS-01, MT-01).

## 8. Quando escalo

| Gatilho | Escala para | Nivel | Bloqueia execucao? |
|---|---|---|---|
| **Criacao ou encerramento de produto** | SOBERANO, via DEP-EXE | **E4** | **Sim** |
| **Mudanca de posicionamento** | SOBERANO, via DEP-GRW e DEP-EXE | **E4** | **Sim** |
| **Conflito entre valor e principio** — o que da resultado viola norma | SOBERANO | **E4** | **Sim** (PI-13) |
| Uso de dado de terceiros na descoberta | SOBERANO, via DEP-QAR | **E4** | **Sim** (LV-08) |
| Duvida de conformidade, qualidade ou risco | DEP-GOV / DEP-QAR | **E3** | Sim |
| **Conflito de escopo com DEP-ENG** | DEP-EXE | **E2** | Nao |
| Conflito de prioridade entre produtos | DEP-EXE | **E2** | Nao |
| Descoberta insuficiente para definir o problema | **ninguem — a spec nao e submetida a `QG-1`** | **E1** | **Sim, para o item** |
| Duvida rotineira de escopo resolvivel por premissa | ninguem — **decide e registra a premissa** | **E0** | Nao |

### 8.1 Cadencias de que participo
| Cadencia | Meu papel | O que produzo |
|---|---|---|
| Abertura de ciclo | Recebo prioridade e alocacao | Escopo do ciclo, itens definidos |
| **Sincronizacao de linha** | Participo | Estado da definicao, bloqueios, dependencias |
| Revisao de qualidade | **Sou consultado sobre criterio de aceite** — nunca avalio a entrega | Esclarecimento de criterio; correcao de defeito **de spec** |
| Fechamento de ciclo | Reporto | Escopo entregue, despriorizado e o motivo |
| Colheita de aprendizado | Contribuo | Hipoteses validadas e invalidadas para a camada APR |

### 8.2 Handoffs
| Handoff | Emito / recebo | Criterio de aceite | Criterio de devolucao |
|---|---|---|---|
| **Spec para construcao** | **Emito** a DEP-ENG | Problema, resultado, criterio de aceite verificavel e escopo negativo presentes; **`QG-1` liberado por DEP-EXE** | Devolvida por DEP-ENG quando o escopo for insuficiente ou o criterio nao for verificavel (HO-02, HO-04) |
| **Defeito de spec** | **Recebo** de DEP-QAR, via QG-3 | Item de DoD e trecho da spec identificados | Devolucao que aponte defeito de **construcao**, nao de spec — nao e minha (FND-02 §5) |
| **Sinal de mercado** | **Recebo** de DEP-GRW | Objecao ou motivo de perda, com origem | Promessa externa apresentada como requisito — **nao vira spec sem passar por mim** (FND-02 §4) |
| **Sinal de uso real** | **Recebo** de DEP-OPS | Ocorrencia com frequencia e contexto | Relato sem contexto de uso |
| Pedido de capacidade externa | **Emito** a DEP-TLS, **via DEP-ENG ou DEP-EXE** | Finalidade e dado que trafega declarados | FND-02 §4 declara `—` entre PRD e TLS — o pedido nao vai direto |

> **Handoff devolvido duas vezes pelo mesmo motivo escala a DEP-EXE** — ha defeito de
> fronteira (HO-03, FND-02 §9.2).

## 9. Memoria autorizada e politica de contexto

| Camada | Meu papel | Sob que condicao |
|---|---|---|
| **EST** | **Leitor obrigatorio** antes de qualquer decisao C2/C3 | Nao escrevo: escrita em EST e de DEP-GOV, mediante ADR (FND-06 §3.1) |
| **PRD** | **Dono da camada** | O que se constroi, para quem e sob quais criterios (FND-06 §2.1). **DEP-GRW contribui sinal de mercado; DEP-OPS contribui sinal de uso** |
| **TEC** | Leitor | Antes de definir escopo que dependa de restricao tecnica conhecida |
| **OPR** | **Escritor** | Estado da definicao, bloqueios e handoffs do ciclo corrente |
| **APR** | **Contribuinte obrigatorio**; DEP-KMS e o dono | Toda hipotese invalidada e todo escopo revisto vira licao (QG-5) |

### 9.1 Politica de contexto
| Item | Valor |
|---|---|
| Pacote minimo para operar | Nucleo obrigatorio + a **camada PRD do produto** em questao + `TPL-spec` |
| Custo medido do pacote | **1.099 linhas** de nucleo + **272 linhas** de `TPL-spec` **1.1.0**, medidos em 2026-07-29 = **1.371 linhas**. **A camada PRD tem 0 registros nesta fase** |
| Gatilho para carregar alem do minimo | **Item priorizado por DEP-EXE**. Carrega-se a memoria **do produto** em questao, nunca a camada inteira |
| **Nao** carrego por padrao | As tres Cartas de Capability juntas *(**477 linhas**, medidas)*; a camada TEC; perfil `arquivo` |

## 10. Riscos, impedimentos e segregacao

> **Secao obrigatoria (DC-03).** Sem ela a Carta nao e valida.

| # | Materia em que estou impedido | Por que | **Quem me substitui** | Fonte |
|---|---|---|---|---|
| **I-1** | **Verificar ou aprovar se a entrega atende a spec que eu escrevi** | Quem define o criterio nao julga se ele foi atendido | **DEP-QAR** *(QG-3)* | PI-05, LV-03, GV-04 |
| **I-2** | **Revisar a propria Spec** | `SPC` tem revisores nomeados na matriz, e nenhum sou eu | **DEP-ENG + DEP-QAR** | FND-09 §8.2, linha `SPC`: revisa |
| **I-3** | **Decidir como construir**, ainda que a solucao tecnica pareca obvia | Arquitetura e de DEP-ENG; sugerir e legitimo, decidir nao | **DEP-ENG** | FND-01 §7.3; PI-09 |
| **I-4** | **Criar ou encerrar produto** | Portfolio e materia do Soberano | **SOBERANO**, via DEP-EXE | FND-01 §7.3; FND-09 §8.2, linha `PRO` |
| **I-5** | **Aprovar ou ratificar a Carta de Produto que eu proponho** | Quem propoe nao aprova | **SOBERANO** | FND-09 §8.2, linha `PRO`; PI-05 |
| **I-6** | **Priorizar entre produtos**, ou alocar capacidade | Fila organizacional e de DEP-EXE; a minha ordem e **dentro** do produto | **DEP-EXE** | FND-02 §3 |
| **I-7** | **Transformar promessa externa em requisito** sem passar pela minha propria definicao | Se a promessa entrasse direto, o escopo passaria a ser definido fora do dono dele | **DEP-PRD** — eu proprio, pelo rito; DEP-GRW **nao instrui** DEP-ENG | FND-02 §4 |
| **I-8** | **Comunicar externamente** o que o produto e ou fara | Saida externa e de DEP-GRW e passa por aprovacao humana | **DEP-GRW** + **SOBERANO** | FND-01 §7.3; LV-08 |
| **I-9** | **Alterar Carta de Capability** que custodio, para acomodar decisao de escopo | A fonte prevalece sobre a projecao | Rito de FND-08 §6.3; ratifica **SOBERANO** se `nucleo` | PR-2, PR-3; PJ-03 |
| **I-10** | **Aprovar, revisar ou emendar esta Carta** | E o instrumento que define a minha propria autoridade | **DEP-GOV** *(revisa)* · **SOBERANO** *(aprova e ratifica)* | RM-06b, LV-03; FND-09 §8.2 |
| **I-12** | **Liberar o portao `QG-1` sobre a Spec que eu escrevi** | Portao nao e liberado por quem produziu o artefato | **DEP-EXE** | FND-01 §6.2, *Regra de portao* e nota pos-[ADR-0018](../../decisions/ADR-0018-liberacao-do-portao-qg-1.md); PI-05, LV-03 |
| **I-11** | **Priorizar, avaliar ou instruir departamento de Guarda** | Linha nao coordena a Guarda | **DEP-EXE** coordena Linha; a Guarda responde ao **SOBERANO** | ES-02, IV-01 |

### 10.1 Riscos proprios do dominio
| # | Risco | Probabilidade | Impacto | Mitigacao declarada |
|---|---|---|---|---|
| RP-1 | **QG-1 sem contraditorio** — **risco EXTINTO NA FONTE** por [ADR-0018](../../decisions/ADR-0018-liberacao-do-portao-qg-1.md): `QG-1` passa a ser liberado por **DEP-EXE**, que **nao produz** a spec | **Extinto** | — | **Nao ha mais assimetria a mitigar:** o contraditorio passa a existir **antes** do portao. A linha e **registrada e nao apagada** (MM-09) — a Carta **1.0.0** declarava este risco com impacto **Alto** e mitigacao *"assimetrica e declarada como tal"*, e o que esta linha registra e que **a correcao veio da fonte, nao da mitigacao** |
| RP-2 | **Solucao disfarcada de problema** — a spec descrever o como | Media | **Alto** | P-2: o problema esta escrito **antes** da solucao. Spec que so descreva implementacao e devolvida por DEP-ENG (HO-02) |
| RP-3 | **Escopo negativo ausente** — o produto vira tudo o que pedirem | **Media** | **Alto** | P-9 e QG-1: **os tres** — resultado, criterio de aceite e o que fica fora — sao condicao de liberacao |
| RP-4 | **Fan-out de defeito** — `CAP-produto` e um dos dois maiores do catalogo | Media | **Alto** | Defeito nela propaga para arquitetura, design, marketing e comercial (`capabilities/README §4.1`). Prioridade de indicador |
| RP-5 | **Hipotese tratada como fato** | **Media** | Medio | P-11: hipotese entra **marcada**, com o teste que a confirmaria; invalidada **nao e apagada** (MM-09) |
| RP-6 | **Descoberta que vira pesquisa infinita** — nunca definir por nunca saber o bastante | Media | Medio | QG-1 exige **resultado e criterio**, nao certeza. *"Nao encontrei"* e resposta valida e obrigatoria (RC-03), e nao motivo para adiar a definicao |
| RP-7 | **Zero exercicio** — nenhuma spec, produto ou registro PRD existe | **Observado** | Medio | Todos os indicadores de producao valem **zero** (§11). E ausencia **determinada**, nao omissao |

### 10.2 Incompatibilidades de papel
| Papel A | Papel B | Por que nao se acumulam na mesma mudanca |
|---|---|---|
| **Definidor do problema** | **Construtor da solucao** | DEP-PRD × DEP-ENG (FND-02 §4) — e o impedimento **I-3** |
| Autor da spec | Verificador de que a entrega a atende | PI-05, LV-03 — impedimento **I-1** |
| Autor da spec | Revisor da mesma spec | FND-09 §8.2, linha `SPC` — impedimento **I-2** |
| **Produtor da spec** | **Liberador do portao que a verifica** | FND-01 §6.2, *Regra de portao*; PI-05, LV-03 — e a razao de **I-12** |
| Proponente da Carta de Produto | Aprovador dela | PI-05; FND-09 §8.2, linha `PRO` |
| Custodio de Capability | Autoridade que aprova a propria proposta de evolucao dela | FND-08 §6.1 — o custodio **propoe**; nao aprova |
| Definidor do escopo | Comunicador externo do escopo | FND-01 §7.3; LV-08 — impedimento **I-8** |

## 11. Indicadores

> Indicador **sem valor medido** declara-se `definido, sem valor`. Afirmar desempenho sem
> medida e LV-12.

| # | Indicador | Definicao | Direcao | **Valor medido** | **Data** |
|---|---|---|---|---|---|
| KP-1 | Capabilities custodiadas | Contagem na projecao de `capabilities/README §10` | estavel | **3** | 2026-07-28 |
| KP-2 | Capabilities custodiadas em maturidade `experimental` | Contagem no catalogo | ↓ | **3 de 3** | 2026-07-28 |
| KP-3 | **Produtos com Carta** | Contagem em `products/` | — | **0** — proibido nesta fase, por determinacao | 2026-07-28 |
| KP-4 | **Specs emitidas** | Contagem de `SPC` | — | **0** | 2026-07-28 |
| KP-5 | **Registros na camada PRD** | Contagem em `memory/produto/` | — | **0** | 2026-07-28 |
| KP-6 | **Specs submetidas a `QG-1`** | Contagem de submissoes — **a liberacao do portao e medida por DEP-EXE** (`KX-15` da Carta de DEP-EXE) | — | **0** | 2026-07-29 |
| KP-7 | Capabilities do dominio `VAL` custodiadas por DEP-PRD | Contagem — cobertura do dominio | estavel | **3 de 3** — o dominio `VAL` inteiro | 2026-07-28 |
| KP-8 | Specs com escopo negativo declarado | Specs com escopo negativo / specs emitidas | → 100% | **`definido, sem valor`** — divisao por zero; nao ha spec | — |
| KP-9 | Taxa de devolucao de spec por DEP-ENG | Devolvidas / entregues | estavel e nao-zero | **`definido, sem valor`** — nenhum handoff emitido | — |
| KP-10 | Defeitos de QG-3 atribuidos a **spec**, e nao a construcao | Contagem | ↓ | **`definido, sem valor`** — nenhuma verificacao ocorreu | — |
| KP-11 | Hipoteses validadas × invalidadas | Razao | — | **`definido, sem valor`** — nenhuma hipotese registrada | — |
| KP-12 | Retrabalho por escopo mal definido | Itens refeitos / itens entregues | ↓ | **`definido, sem valor`** — nenhuma entrega | — |
| KP-13 | Itens despriorizados com motivo registrado | Com motivo / total | → 100% | **`definido, sem valor`** — nenhum roadmap emitido | — |

**Contagem: 13 indicadores definidos · 7 com valor medido · 6 `definido, sem valor`.**

> **Os sete medidos valem zero em cinco deles, e isso e o estado honesto.** DEP-PRD custodia o
> dominio `VAL` **inteiro** e **nao produziu nada**: zero produtos, zero specs, zero registros
> na propria camada. **Os seis sem valor sao precisamente os que mediriam desempenho**, e todos
> dependem de um ciclo de produto que **nao existe por determinacao**. Declara-los medidos seria
> **LV-12**.

## 12. Ciclo de vida — especializacao, fusao e retirada

### 12.1 Gatilhos de especializacao
| Gatilho *(FND-02 §9.2)* | Aplica-se? | **Sinal ja observado** | Movimento previsto |
|---|---|---|---|
| **Escopo heterogeneo** | **Sim, potencialmente** | Tres Capabilities de naturezas distintas: **descobrir** *(pesquisa)*, **definir** *(produto)* e **dar forma** *(design)*. Contam **3**, que **iguala** o limite de VC-03 e nao o ultrapassa | Dividir dominio — candidato natural: separar `CAP-design`. **So com sinal medido**, que nao existe |
| Carga concentrada | **Nao avaliavel** | **Nenhum** — zero producao registrada (KP-3 a KP-6) | — |
| Contexto excessivo | **Nao** | Pacote minimo **1.231 linhas**, **3,8%** do acervo | — |
| Fronteira em disputa | **Nao** | **Zero** conflitos registrados com ENG, GRW ou EXE | — |
| Duplicacao | Nao | Nenhum procedimento refeito — nao ha procedimento | — |
| Gargalo de decisao | Nao | **0** escalonamentos E2 registrados | — |
| Conhecimento ilhado | **Nao avaliavel** | Nao ha resultado produzido de que extrair o sinal | — |

> **Decisao registrada: nao especializar** (FND-04 §6.2). **SE-02 exige dois sinais observados
> e ha zero** — o escopo heterogeneo e **indicado pela natureza**, nao **observado por medicao**.
> Dividir agora criaria dois departamentos sem producao em vez de um. **Custo assumido:** as tres
> naturezas convivem sem fronteira interna declarada ate haver producao. **Gatilho de
> reexecucao:** primeiro produto com Carta aprovada.

### 12.2 Gatilhos de fusao ou consolidacao
| Sinal *(FND-02 §9.3)* | Com quem | O que indicaria |
|---|---|---|
| Duas areas que sempre atuam juntas e nunca isoladas | **DEP-GRW** | Que definir o produto e leva-lo ao publico nao sao fronteiras distintas. **Contraindicado**: FND-02 §4 separa quem define de quem promete, e a fusao permitiria que a promessa definisse o escopo (I-7) |
| Handoff que so transporta, sem transformar | DEP-ENG | Que a spec nao acrescenta ao pedido. **Sinal contrario esperado**: a spec e exatamente a transformacao de intencao em criterio verificavel |
| Componente sem acionamento ao longo de um horizonte | **DEP-PRD**, sobre si mesmo | Que a definicao de produto foi estruturada antes da demanda. **Nao avaliavel**: nenhum horizonte se tornou avaliavel sob `HZ-02` ([ADR-0013](../../decisions/ADR-0013-criterio-de-horizonte-e-consolidacao.md)) |
| Custo de coordenacao maior que o ganho | — | Nenhum sinal registrado |

### 12.3 Criterio de extincao
DEP-PRD deixa de ser necessario se a organizacao deixar de decidir **o que** construir — o que
contradiria a Missao de FND-01 §1 e o fluxo de FND-02 §5. Na extincao, cada responsabilidade e
cada custodia recebe destino explicito (IV-07, FND-02 §8.3):

| Responsabilidade / custodia | Destino declarado na extincao |
|---|---|
| Custodia de `CAP-produto` *(`nucleo`)* | **Nunca** a departamento de classe Suporte (OW-04). Transferencia e C2 com ADR e **ratificacao do SOBERANO** (OW-06) |
| Custodia de `CAP-pesquisa` e `CAP-design` | Destino explicito obrigatorio; competencia orfa e tao proibida quanto responsabilidade orfa (IV-07) |
| **Submissao da spec a `QG-1`** | Destino explicito obrigatorio. **O portao `QG-1` nao e destino desta extincao:** ele e liberado por **DEP-EXE** desde [ADR-0018](../../decisions/ADR-0018-liberacao-do-portao-qg-1.md), e o que se extingue aqui **nao o detem**. O que precisa de destino e **quem submete** — vai com `P-4` e `P-8`. **Nunca** a DEP-ENG — quem constroi nao define |
| **Camada de memoria PRD** | Novo dono nomeado; a camada nao e apagada (MM-09) |
| Specs e Cartas de Produto ja emitidas | Preservadas; nenhuma e apagada (FND-04 §7.2) |
| Escopo negativo registrado | Transferido integralmente — e o registro do que a organizacao decidiu **nao** fazer, e perde-lo reabre decisoes fechadas |

### 12.4 Funcoes internas nomeadas
> Responsabilidades hospedadas aqui que ainda nao merecem departamento proprio (ES-04).

| Funcao | Responsabilidade | Gatilho de promocao |
|---|---|---|
| **Pesquisa** | Descoberta, personas, contexto de uso | **Segundo produto** em descoberta simultanea |
| **Design** | Forma, comportamento e linguagem | **Primeiro produto com interface exposta ao publico** |
| **Curadoria da camada PRD** | Requisitos duraveis, escopo negativo, hipoteses | **Vigesimo registro** na camada PRD |

## 13. Resumo operacional, carregamento e rastreabilidade

### 13.1 Resumo operacional
Define o que deve existir e por que, transformando intencao em problema bem formulado e
resultado verificavel.

### 13.2 Perfil minimo de carregamento
| Recorte | Para que serve | Custo **medido** | Data |
|---|---|---|---|
| Secoes 1, 2 e 4 | Saber o que DEP-PRD faz e o que nao faz | **55 linhas** | 2026-07-29 |
| + secoes 5 e 10 | Decidir se DEP-PRD pode definir, submeter ou aprovar algo | **145 linhas** | 2026-07-29 |
| Carta integral | Auditoria, revisao estrutural, extincao | **445 linhas** | 2026-07-29 |

> Carregar alem do recorte aplicavel exige **gatilho declarado** (CE-01, PC-01). O recorte de decisao custa **33% da Carta** — medido por
> `sed`+`wc -l` sobre os intervalos das secoes.

### 13.3 Rastreabilidade
| Campo | Conteudo |
|---|---|
| ADR de criacao do departamento | [ADR-0001](../../decisions/ADR-0001-adocao-da-fundacao-organizacional.md) — adota FND-02, que cria os nove departamentos |
| ADR do contrato desta Carta | [ADR-0011](../../decisions/ADR-0011-contrato-de-carta-de-departamento.md) |
| RFC de origem | [RFC-0008](../../rfcs/RFC-0008-contrato-de-carta-de-departamento.md) |
| Decisoes que moldam esta Carta | ADR-0002 *(vinculacao a Capability)* · ADR-0003 *(Meta Model; entidades `SPC` e `PRO`)* · ADR-0012 *(integridade do ato — base da nota de homologacao em §5)* · **ADR-0018** *(`QG-1` liberado por DEP-EXE)* · **ADR-0019** *(aprovador de Spec conforme a classe)* |
| Achados que esta Carta trata | **P6** — declarado **nao aplicavel** a DEP-PRD, com a contagem: **3**, no limite de VC-03 e nao acima · **RD-31** — as **8** afirmacoes que `ADR-0018` e `ADR-0019` tornaram falsas, corrigidas em 1.1.0 · **RD-41** — a `Spec` alojada em `projects/`, corrigida para `products/<slug>/specs/` |
| Alteracoes (ADRs) | [**ADR-0023**](../../decisions/ADR-0023-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md) — propagacao de `ADR-0018` e `ADR-0019` |
| Fonte da custodia e do exercicio | frontmatter de `capabilities/CAP-produto.md`, `CAP-pesquisa.md`, `CAP-design.md` |
| Validacao em cenarios | [REV-ROLLOUT §3](../../foundation/revisao-arquitetural-rollout-cartas-2026-07-28.md) |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.1.0 | 2026-07-29 | DEP-EXE | Emenda **C2 · Tipo 2** por **ADR-0023**, que **propaga** `ADR-0018` e `ADR-0019` — ambos **ratificados** — a esta Carta, fechando **RD-31** quanto a DEP-PRD. **Oito afirmacoes tornadas falsas foram corrigidas:** `§3 P-8`, `§5` *(liberacao de `QG-1`)*, `§5` *(aprovar Spec, com a citacao de `FND-09 §8.2` que nao existe mais)*, `§5.2` *(a tabela de portoes)*, `§5.2` *(a nota "unico portao que DEP-PRD libera sozinho")*, `§7` *(Spec — "autor e aprovador")*, `§10.1 RP-1` e `§12.3`. **Seis blocos adicionais foram revisados e ajustados** — `§4` e `§5.1` *(duas linhas cada, declarando o que nao compete)*, `§8` *(escalonamento)*, `§8.2` *(handoff)*, `§10` *(impedimento novo **I-12**)*, `§10.2` *(incompatibilidade de papel)*, `§11 KP-6` *(passa a medir submissoes)* e `§13.3`. **`RP-1` nao foi apagado: foi declarado EXTINTO NA FONTE** (MM-09) — o risco que a Carta 1.0.0 registrava com impacto **Alto** deixou de existir porque `QG-1` passou a ser liberado por quem **nao** produz a spec. **`RD-41` corrigido no mesmo ato:** `§7` alojava a `Spec` em `projects/`, contra `FND-03 §3.6`, `FND-04 §6` e `FND-10 §4.4`, que a alojam em `products/<slug>/specs/`. **Nenhum titular, portao, papel, classe ou direito decisorio foi criado:** `DEP-EXE` detem `QG-1` por `ADR-0018` e aprova `C2` por `FND-04 §2`, ambos anteriores a esta emenda; **DEP-ENG e DEP-QAR permanecem os revisores da Spec** (`I-2` intacto); **DEP-PRD segue decidindo escopo e criterio de aceite**, e **segue aprovando Spec `C0` e `C1`** como proprietario. **7 portoes antes, 7 depois.** |
| 1.0.0 | 2026-07-28 | DEP-EXE | Criacao — **setima Carta do sistema**, terceira do rollout. Doze blocos preenchidos. Declara o unico portao do sistema liberado **sem contraditorio previo** *(QG-1)* e a mitigacao assimetrica correspondente (RP-1). Permanece em `em-revisao`: aprovar Carta de Departamento e ato do **SOBERANO** (DC-09). |
