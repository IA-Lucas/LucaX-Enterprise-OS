---
id: DEP-ENG
titulo: Engenharia
tipo: carta
versao: 1.1.0
status: ativo
camada_memoria: estrategica
autor: DEP-EXE
proprietario: DEP-EXE
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0001, ADR-0002, ADR-0003, ADR-0007, ADR-0011]
substitui: []
substituido_por: null
classe: linha
nivel: 2
nivel_autonomia: A2
responde_a: DEP-EXE
capabilities: [CAP-arquitetura, CAP-engenharia, CAP-dados, CAP-inteligencia-artificial, CAP-engenharia-de-agentes]
resumo: Constroi a solucao mais simples defensavel que satisfaz a spec e a sustenta tecnicamente ao longo do tempo.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-GOV
ratificacao: ratificada
---

# Engenharia (DEP-ENG)

## Proposito
Existir como o ponto em que definicao vira coisa que funciona. Constroi a solucao mais
simples defensavel que satisfaz a spec, decide como construir, e responde pela sustentacao
tecnica do que construiu ao longo do tempo.

## Escopo
| Item | Definicao |
|---|---|
| Classe | **linha** |
| Nivel | 2 |
| Responde a | **DEP-EXE** |
| Nivel de autonomia | **A2** — executa e decide Tipo 2 no proprio dominio; Tipo 1 exige aprovacao humana |
| Poder de veto | **Nao** — veto e exclusivo da classe Guarda (FND-02 §2.1) |
| **Nao** inclui | O que construir, se a entrega e aceita, qual ferramenta externa e oficial. Delimitacao integral na secao 4 |
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

**Missao:** construir a solucao mais simples defensavel que satisfaz a spec, e sustenta-la
tecnicamente ao longo do tempo.

**Mandato:** decidir **como** se constroi, com autoridade sobre estrutura tecnica e divida
assumida — e nenhuma sobre **o que** se constroi ou **se** a entrega e aceita.

## 2. Capabilities custodiadas e exercidas

> **Declaracao de projecao (PJ-02).** **Fonte:** frontmatter de `CAP-arquitetura.md`,
> `CAP-engenharia.md`, `CAP-dados.md`, `CAP-inteligencia-artificial.md` e
> `CAP-engenharia-de-agentes.md`, campos `custodio` e `exercentes`.
> **Campos projetados:** apenas as linhas de DEP-ENG. **Finalidade:** responder "o que custodio
> e o que exerco" sem abrir cinco arquivos. **Atualizacao:** pela mesma mudanca que altera a
> Carta de Capability (CV-04). Em divergencia, prevalece a Carta de Capability (PR-1).

| Capability | Dominio · Classe | **Custodia** | **Exercicio** | Por que este departamento |
|---|---|---|---|---|
| [CAP-arquitetura](../../capabilities/CAP-arquitetura.md) | REA · `habilitadora` | **sim** | sim | Decidir estrutura tecnica defensavel e o nucleo do mandato |
| [CAP-engenharia](../../capabilities/CAP-engenharia.md) | REA · `habilitadora` | **sim** | sim | Construir o que a arquitetura decidiu |
| [CAP-dados](../../capabilities/CAP-dados.md) | REA · `habilitadora` | **sim** | sim | Modelagem de dados e escopo exclusivo declarado em FND-02 §3 |
| [CAP-inteligencia-artificial](../../capabilities/CAP-inteligencia-artificial.md) | REA · **`nucleo`** | **sim** | sim | Escolher, instruir e avaliar modelos — substrato de todo o trabalho |
| [CAP-engenharia-de-agentes](../../capabilities/CAP-engenharia-de-agentes.md) | REA · **`nucleo`** | **sim** | sim | E a competencia que distingue o LucaX de uma empresa que apenas usa IA |

**Capabilities que exerco sem custodiar:** nenhuma.
**Capabilities que custodio e sao exercidas por outros:** nenhuma **declarada na fonte**.

> **Achado declarado, nao contornado — VC-03.** Cinco vinculos ultrapassam o limite de **tres**
> de VC-03, que manda **avaliar a especializacao do componente**, nao criar Capability. E o
> achado **P6** de [capabilities/README §10.3](../../capabilities/README.md), dono DEP-EXE,
> gatilho na 1a revisao estrutural. **Esta Carta nao divide DEP-ENG:** SE-02 exige **dois**
> sinais observados e ha **um** (a contagem). A avaliacao esta em §12.1.

> **Fronteira a vigiar.** `CAP-inteligencia-artificial` × `CAP-engenharia-de-agentes` exige
> disciplina de fronteira — achado **A4** de
> [REV-CAP](../../capabilities/revisao-arquitetural-2026-07-28.md), dono DEP-ENG, gatilho
> **apos 5 agentes criados**. Hoje ha **zero** agentes.

## 3. O que possuo — escopo exclusivo

| # | Responsabilidade | Como se verifica que esta sendo cumprida | Capability |
|---|---|---|---|
| E-1 | **Arquitetura** — a estrutura tecnica de tudo que se constroi | Toda decisao arquitetural tem ADR com alternativas e reversao | CAP-arquitetura |
| E-2 | **Padroes tecnicos** | Padrao vigente e localizavel e citado nas decisoes que o aplicam | CAP-arquitetura |
| E-3 | **Decisoes de implementacao** | Registradas no nivel proporcional ao efeito (AL-01) | CAP-engenharia |
| E-4 | **Modelagem de dados** | Modelo declarado antes do uso; mudanca de modelo e C2 | CAP-dados |
| E-5 | **Integracoes internas** | Contrato de interface declarado entre as partes | CAP-engenharia |
| E-6 | **Divida tecnica** | Toda divida assumida e **registrada** com motivo e custo (PI-14 regra 2) | CAP-engenharia |
| E-7 | **Portao QG-2** *(com DEP-GOV)* | Alternativas consideradas e decisao registrada antes de construir | CAP-arquitetura |
| E-8 | **Viabilidade e estimativa** | Estimativa acompanha a premissa que a sustenta | CAP-engenharia |
| E-9 | **Escolha, instrucao e avaliacao de modelos de IA** | Criterio de escolha declarado; avaliacao antes da adocao (PI-11) | CAP-inteligencia-artificial |
| E-10 | **Projeto de papeis executores** — escopo, limite e autonomia de agentes | Toda Carta de agente declara o que **nao** lhe compete e as Capabilities que exerce | CAP-engenharia-de-agentes |

## 4. O que NAO me compete

| Materia | Dono real | Fonte |
|---|---|---|
| Decidir **o que** construir, o escopo e o criterio de aceite funcional | DEP-PRD | FND-02 §3; FND-01 §7.3 |
| Decidir se a entrega **passa** ou e devolvida | DEP-QAR | FND-02 §3; QG-3 |
| Declarar qual **ferramenta externa** e oficial, e seus limites de uso | DEP-TLS | FND-02 §3 |
| Decidir se o **risco** e aceitavel | DEP-QAR | FND-02 §3 |
| Definir prioridade, fila e alocacao | DEP-EXE | FND-02 §3 |
| Julgar forma, conformidade e rastreabilidade | DEP-GOV | FND-04 §12 |
| Decidir onde um registro de memoria pertence | DEP-KMS | FND-06 §2.1 |
| **Operar** o que construiu, e responder por incidente operacional | DEP-OPS | FND-02 §3 |
| Prometer capacidade tecnica ao publico | DEP-GRW, apos DEP-PRD | FND-02 §4 *(GRW nao instrui ENG)* |
| Criar Capability, ou alterar escopo de Capability que custodia sem o rito | custodio + DEP-GOV + SOBERANO | FND-08 §6.3; DC-01 |
| Importar conteudo do **LucaX Legacy** | Portao de admissao G1–G5 | [ADR-0007 §5.3](../../decisions/ADR-0007-fronteira-greenfield-legado.md) |

## 5. O que decido — autoridade e portoes

| Materia | Autonomia | Consulta obrigatoria | **Fonte da autoridade** |
|---|---|---|---|
| **Como construir** — arquitetura e padrao a adotar | A2 | DEP-QAR *(risco)* | FND-01 §7.3, "Arquitetura tecnica"; FND-02 §3 |
| O que e **viavel** tecnicamente | A2 | DEP-PRD | FND-02 §3 |
| Qual **divida tecnica** assumir conscientemente | A2 | DEP-QAR | FND-02 §3 |
| Modelo de dados | A2 | DEP-QAR *(seguranca)*, DEP-TLS *(integracao)* | FND-02 §3 |
| Escolha e avaliacao de modelo de IA | A2 | DEP-TLS *(adocao da ferramenta)*, DEP-QAR *(risco)* | FND-02 §3; PI-11 |
| Liberacao de **QG-2**, com DEP-GOV | A2 | DEP-GOV | FND-01 §6.2 |
| Emitir **ADR tecnico** | A2 | DEP-QAR *(revisor independente)* | FND-09 §8.2, linha `ADR` |

### 5.1 O que **nao** decido
| Materia | Quem decide | Fonte |
|---|---|---|
| Decisao arquitetural **Tipo 1**; migracao ou reescrita | **SOBERANO** | FND-02 §3; PI-06 |
| Aceite da entrega | DEP-QAR | QG-3 |
| Adocao oficial de ferramenta externa | DEP-TLS propoe, **DEP-EXE** aprova, **SOBERANO** ratifica | FND-09 §8.2, linha `TOL` |
| Aprovacao da propria Carta de agente | **DEP-EXE** | FND-09 §8.2, linha `AGT` |

### 5.2 Portoes sob minha responsabilidade
| Portao | O que verifico | Criterio de liberacao | Fonte |
|---|---|---|---|
| **QG-2** *(com DEP-GOV)* | As alternativas foram consideradas e a decisao esta registrada? | ADR com ≥2 alternativas reais + "nao fazer nada", criterios antes da escolha e plano de reversao | FND-01 §6.2; VD-01 a VD-09 |

> **Nenhum portao novo e criado aqui.** Os sete sao de FND-01 §6.2; acrescentar e **C3**.

## 6. Interfaces — entradas, saidas e consumidores

### 6.1 Entradas
| De quem | O que recebo | Em que forma | Gatilho |
|---|---|---|---|
| **DEP-PRD** | Spec, criterio de aceite funcional, escopo negativo | **HANDOFF** | Liberacao de QG-1 |
| DEP-EXE | Prioridade, alocacao, briefing | DIRETIVA, com `nivel_autonomia_concedido` | Abertura de ciclo |
| DEP-QAR | Parecer, defeitos, laudo de risco, **veto** | REPORTE ou **ALERTA** | QG-3 e QG-4 |
| DEP-GOV | Parecer de conformidade, classe de mudanca validada | CONSULTA | Etapa 2 do ciclo de FND-04 §4 |
| DEP-TLS | Ferramenta oficial, limite de uso, mapa de dependencia externa | REPORTE | Adocao aprovada |
| DEP-OPS | Sinal de uso real, incidente operacional | REPORTE | Operacao |
| DEP-KMS | Pacote de contexto, licoes da camada APR | REPORTE | QG-0 |

### 6.2 Saidas
| Entrega | Destinatario | Formato | Cadencia | Consumidor final |
|---|---|---|---|---|
| **ADR tecnico** | `decisions/` | Artefato `ADR` | Por decisao arquitetural | Toda a organizacao |
| **Desenho de arquitetura** | DEP-QAR, DEP-OPS | Artefato tecnico | Por componente | Quem constroi e quem opera |
| **Implementacao** | DEP-QAR *(QG-3)* → DEP-OPS | Componente construido | Por entregavel | DEP-OPS |
| **Estimativa e avaliacao de viabilidade** | DEP-PRD, DEP-EXE | REPORTE | Sob CONSULTA | Quem prioriza |
| **Registro de divida tecnica** | DEP-EXE, DEP-QAR | Registro em camada **TEC** | Por divida assumida | Quem decide o proximo ciclo |
| Aprendizado tecnico | DEP-KMS | REPORTE, secao Aprendizado | A cada encerramento | Camada APR |

### 6.3 Natureza da interacao
| Departamento | Natureza | O que trafega |
|---|---|---|
| DEP-EXE | entrega | Estado, estimativa, escalonamento |
| DEP-GOV | consulta | Conformidade — DEP-GOV **veta** DEP-ENG, nunca o inverso |
| DEP-QAR | consulta | Risco — DEP-QAR **veta** DEP-ENG, nunca o inverso |
| **DEP-PRD** | **consulta** | Spec recebida. **PRD entrega a ENG, nunca o inverso** (FND-02 §4) |
| DEP-OPS | **entrega** | Componente construido, desenho, runbook de apoio |
| DEP-TLS | consulta | Ferramenta, limite, dependencia externa |
| DEP-KMS | entrega | Aprendizado e decisao tecnica gravados |
| DEP-GRW | **sem interacao estrutural direta** | Promessa externa **nao** vira requisito sem passar por DEP-PRD (FND-02 §4) |

> A matriz completa de interacao vive em **FND-02 §4** e **nao** e reproduzida aqui: esta
> secao declara apenas as linhas de DEP-ENG (DC-08).

## 7. Artefatos e registros mantidos

| Tipo documental | Entidade | Meu papel | Onde vive |
|---|---|---|---|
| **ADR** *(tecnico)* | `ADR` | **Autor**; nunca aprovador do proprio | `decisions/` |
| **RFC** *(tecnica)* | `RFC` | **Autor** | `rfcs/` |
| Memoria **TEC** | `MEM` | **Dono da camada** | `memory/tecnica/` |
| Carta de Agente / Subagente | `AGT` `SUB` | **Autor**, quando o agente for de DEP-ENG | fase futura |
| Skill | `SKL` | Autor | fase futura |
| Spec | `SPC` | **Revisor**, com DEP-QAR — nunca autor | fase futura |
| Ficha de Ferramenta | `TOL` | **Revisor**, com DEP-QAR — nunca autor | fase futura |
| Reporte / Consulta | `MSG` | **Emissor** | `memory/operacional/` |

> **Nenhum artefato de codigo, infraestrutura ou banco existe nesta fase**, por determinacao.
> Tipo documental que nao conste de [FND-10 §4](../../foundation/10-artifact-framework.md)
> nao existe (CS-01, MT-01).

## 8. Quando escalo

| Gatilho | Escala para | Nivel | Bloqueia execucao? |
|---|---|---|---|
| Decisao arquitetural **Tipo 1** | SOBERANO | **E4** | **Sim** |
| Migracao ou reescrita | SOBERANO | **E4** | **Sim** |
| **Risco de perda de dado** | SOBERANO | **E4** *(pula niveis, EC-02)* | **Sim** |
| Credencial exposta detectada na construcao | SOBERANO, via DEP-QAR | **E4** | **Sim** |
| Duvida de conformidade ou de risco | DEP-GOV / DEP-QAR | **E3** | Sim |
| Conflito de escopo com DEP-PRD | DEP-EXE | **E2** | Nao |
| Spec insuficiente para construir | DEP-PRD, por devolucao de handoff | **E1** | Sim, para o item |
| Duvida rotineira resolvivel por premissa | ninguem — **decide e registra a premissa** | **E0** | Nao |

### 8.1 Cadencias de que participo
| Cadencia | Meu papel | O que produzo |
|---|---|---|
| Abertura de ciclo | Recebo prioridade e alocacao | Estimativa e viabilidade |
| **Sincronizacao de linha** | Participo | Estado, bloqueios, dependencias |
| Revisao de qualidade | **Sou avaliado** — nunca avalio | Correcao dos defeitos apontados |
| Fechamento de ciclo | Reporto | Divida assumida no ciclo |
| Colheita de aprendizado | Contribuo | Licao tecnica para a camada APR |

### 8.2 Handoffs
| Handoff | Emito / recebo | Criterio de aceite | Criterio de devolucao |
|---|---|---|---|
| **Spec para construcao** | **Recebo** de DEP-PRD | Problema, resultado, criterio de aceite verificavel e escopo negativo presentes | Escopo insuficiente; criterio nao verificavel; QG-1 nao liberado (HO-02, HO-04) |
| **Componente para verificacao** | **Emito** a DEP-QAR | Criterio de aceite declarado; evidencia anexada por ID | Devolvido por defeito ou risco nao mitigado |
| **Componente para operacao** | **Emito** a DEP-OPS | Desenho e criterio de operacao entregues | Runbook impossivel de escrever a partir do entregue |
| Pedido de capacidade externa | **Emito** a DEP-TLS | Finalidade e dado que trafega declarados | Ferramenta nao adotada, ou limite de uso incompativel |

> **Handoff devolvido duas vezes pelo mesmo motivo escala a DEP-EXE** — ha defeito de
> fronteira (HO-03, FND-02 §9.2).

## 9. Memoria autorizada e politica de contexto

| Camada | Meu papel | Sob que condicao |
|---|---|---|
| **EST** | **Leitor obrigatorio** antes de qualquer decisao C2/C3 | Nao escrevo: escrita em EST e de DEP-GOV, mediante ADR (FND-06 §3.1) |
| **PRD** | **Leitor obrigatorio** antes de construir | Requisitos duraveis e escopo negativo do produto |
| **TEC** | **Dono da camada** | Como esta construido e por que assim (FND-06 §2.1) |
| **OPR** | **Escritor** | Estado da construcao, bloqueios, dependencias do ciclo corrente |
| **APR** | **Contribuinte obrigatorio**; DEP-KMS e o dono | Toda licao tecnica e ganho de especializacao constatado ou frustrado |

### 9.1 Politica de contexto
| Item | Valor |
|---|---|
| Pacote minimo para operar | Nucleo obrigatorio + a **spec** do item em construcao + as Cartas das Capabilities que o item exerce |
| Custo medido do pacote | **1.099 linhas** de nucleo, medido em 2026-07-28. A spec **nao existe nesta fase** — nao ha produto |
| Gatilho para carregar alem do minimo | Item priorizado por DEP-EXE. Carrega-se a Capability **do item**, nao as cinco custodiadas |
| **Nao** carrego por padrao | As cinco Cartas de Capability juntas *(**820 linhas**, medidas)*; perfil `arquivo`; [MEM-EST-0001](../../memory/estrategica/MEM-EST-0001-contexto-do-soberano.md), que permanece `aprovado` e nao vigente |

> **CE-01 aplicado ao caso mais caro do acervo.** DEP-ENG e o departamento de maior custodia;
> carregar as cinco Cartas por padrao custaria **3,5%** do acervo sem que a tarefa as use.

## 10. Riscos, impedimentos e segregacao

> **Secao obrigatoria (DC-03).** Sem ela a Carta nao e valida.

| # | Materia em que estou impedido | Por que | **Quem me substitui** | Fonte |
|---|---|---|---|---|
| **I-1** | Aprovar ou verificar a **propria entrega** | Producao, revisao e aprovacao nao se concentram | **DEP-QAR** *(QG-3)*, com DEP-GOV *(forma)* | PI-05, LV-03, GV-04 |
| **I-2** | Aprovar o proprio **ADR tecnico** | Quem propoe nao aprova | Revisor independente + DEP-QAR; aprovacao conforme a classe | FND-09 §8.2, linha `ADR`; PI-05 |
| **I-3** | Decidir **o que** construir, ainda que a spec pareca errada | Escopo e de DEP-PRD; ampliar por iniciativa propria e violacao | **DEP-PRD**, por devolucao de handoff com motivo | PI-09, HO-02 |
| **I-4** | Adotar ferramenta externa por conta propria | Improviso de acesso externo e o que DEP-TLS existe para impedir | **DEP-TLS** propoe · DEP-EXE aprova · SOBERANO ratifica | FND-02 §3; FND-09 §8.2, linha `TOL` |
| **I-5** | Alterar Carta de Capability que custodia, para acomodar decisao propria | A fonte prevalece sobre a projecao | Rito de FND-08 §6.3; ratifica SOBERANO se `nucleo` | PR-2, PR-3; PJ-03 |
| **I-6** | Importar conteudo do **LucaX Legacy** | Origem externa nao tem autoridade por existir | Portao G1–G5, decisao formal | ADR-0007 §5.3, FR-03 |
| **I-7** | Depender diretamente de agente de outro departamento | Comunicacao atravessa Handoff formal ou DEP-EXE | Handoff, ou escalonamento a DEP-EXE | PD-12, AG-04, CN-01 |
| **I-8** | Instruir ou ser instruido por DEP-GRW | Promessa externa nao vira requisito sem passar por DEP-PRD | **DEP-PRD** | FND-02 §4 |
| **I-9** | **Aprovar, revisar ou emendar esta Carta** | E o instrumento que define a minha propria autoridade | **DEP-GOV** *(revisa)* · **SOBERANO** *(aprova e ratifica)* | RM-06b, LV-03; FND-09 §8.2 |

### 10.1 Riscos proprios do dominio
| # | Risco | Probabilidade | Impacto | Mitigacao declarada |
|---|---|---|---|---|
| RE-1 | **Amplitude excessiva** — 5 Capabilities, contra o limite de 3 de VC-03 | **Observado** | **Alto** | Achado **P6**, dono DEP-EXE, gatilho na 1a revisao estrutural. Avaliacao em §12.1 |
| RE-2 | **Fronteira IA × engenharia-de-agentes** indistinta | Media | Medio | Achado **A4** de REV-CAP; limites explicitados nas duas Cartas; gatilho **apos 5 agentes** |
| RE-3 | **Divida tecnica invisivel** — assumida e nao registrada | Media | **Alto** | E-6: toda divida assumida e registrada com motivo e custo. Custo invisivel e defeito de governanca (FND-04 §6.2) |
| RE-4 | **Sofisticacao nao pedida** | Media | Medio | VL-07: a solucao mais simples que satisfaz os criterios e **que se consegue justificar** |
| RE-5 | **Fan-out de defeito** — `CAP-arquitetura` e um dos maiores fan-outs do catalogo | Media | **Alto** | Defeito nela propaga para engenharia, dados, IA, infraestrutura e integracao (capabilities/README §4.1). Prioridade de indicador |
| RE-6 | **Dependencia externa sem criterio de descarte** | Baixa | Alto | PD-07: dependencia dura em ferramenta externa sem alternativa avaliada e criterio de descarte e **vetada por DEP-QAR** |

### 10.2 Incompatibilidades de papel
| Papel A | Papel B | Por que nao se acumulam na mesma mudanca |
|---|---|---|
| Produtor do componente | Verificador em QG-3 | PI-05, LV-03 |
| Autor do ADR tecnico | Aprovador do mesmo ADR | GV-04 |
| Custodio de Capability | Autoridade que aprova a propria proposta de evolucao dela | FND-08 §6.1 — o custodio **propoe**; nao aprova |
| Definidor do problema | Construtor da solucao | DEP-PRD × DEP-ENG (FND-02 §4) |

## 11. Indicadores

> Indicador **sem valor medido** declara-se `definido, sem valor`. Afirmar desempenho sem
> medida e LV-12.

| # | Indicador | Definicao | Direcao | **Valor medido** | **Data** |
|---|---|---|---|---|---|
| KE-1 | Capabilities custodiadas | Contagem na projecao de capabilities/README §10 | estavel | **5** | 2026-07-28 |
| KE-2 | Capabilities custodiadas em maturidade `experimental` | Contagem no catalogo | ↓ | **5 de 5** | 2026-07-28 |
| KE-3 | ADRs tecnicos emitidos | Contagem em `decisions/` com autor DEP-ENG | — | **0** | 2026-07-28 |
| KE-4 | Componentes construidos | Codigo, infraestrutura, banco | — | **0** — proibido nesta fase, por determinacao | 2026-07-28 |
| KE-5 | Registros na camada **TEC** | Contagem em `memory/tecnica/` | — | **0** | 2026-07-28 |
| KE-6 | Dividas tecnicas registradas e abertas | Contagem | ↓ | **0** | 2026-07-28 |
| KE-7 | Agentes com Carta | Contagem em `departments/*/agents/` | — | **0** | 2026-07-28 |
| KE-8 | **Decisao arquitetural produzida sem retrabalho posterior** | Decisoes nao superadas por defeito / decisoes emitidas | ↑ | **`definido, sem valor`** — zero ADRs tecnicos emitidos | — |
| KE-9 | Reuso de padrao tecnico entre contextos | Padroes reaproveitados / padroes criados | ↑ | **`definido, sem valor`** — nao ha segundo contexto | — |
| KE-10 | Estimativa contra realizado | Desvio medio | → 0 | **`definido, sem valor`** — nenhuma estimativa emitida | — |
| KE-11 | Taxa de devolucao em QG-3 | Devolvidos / submetidos | estavel e nao-zero | **`definido, sem valor`** — nenhuma submissao | — |
| KE-12 | Escapes — defeitos encontrados apos QG-3 | Contagem | ↓ | **`definido, sem valor`** — nenhuma liberacao | — |

**Contagem: 12 indicadores definidos · 7 com valor medido · 5 `definido, sem valor`.**

> **Os sete medidos valem zero, e isso e o estado honesto.** DEP-ENG e o departamento de maior
> custodia e **nenhuma producao**: cinco Capabilities `experimental`, zero ADRs tecnicos, zero
> componentes. Declarar desempenho aqui seria LV-12. Os cinco sem valor dependem de um ciclo
> de construcao que **nao existe por determinacao**, nao por omissao.

## 12. Ciclo de vida — especializacao, fusao e retirada

### 12.1 Gatilhos de especializacao
| Gatilho *(FND-02 §9.2)* | Aplica-se? | **Sinal ja observado** | Movimento previsto |
|---|---|---|---|
| **Escopo heterogeneo** | **Sim, indicado** | Cinco Capabilities de naturezas distintas: estrutura, construcao, dados, modelos e papeis executores. **Contagem: 5 > 3** (VC-03) | Dividir dominio — candidato natural: separar `IA` + `engenharia-de-agentes` do nucleo de construcao |
| Carga concentrada | **Nao avaliavel** | **Nenhum** — zero producao registrada (KE-3 a KE-7) | — |
| Contexto excessivo | **Nao** | As cinco Cartas custam **820 linhas**, e a politica de §9.1 ja carrega **uma**, nao cinco | — |
| Fronteira em disputa | Nao | **Nenhum** conflito recorrente registrado com PRD, TLS ou QAR | — |
| Duplicacao | Nao | **Nenhum** procedimento refeito — nao ha procedimento | — |
| Gargalo de decisao | Nao | **Nenhum** escalonamento E2 registrado | — |

> **Decisao registrada: nao especializar** (FND-04 §6.2). **SE-02 exige dois sinais
> observados e ha um** — a contagem de VC-03. Os demais gatilhos dependem de carga real, que
> nao existe. Dividir agora seria fragmentacao: criaria dois departamentos sem producao em vez
> de um. **Custo assumido:** DEP-ENG opera acima do limite de VC-03 ate a 1a revisao
> estrutural; o custo esta declarado, nao invisivel (PI-14 regra 2).

### 12.2 Gatilhos de fusao ou consolidacao
| Sinal *(FND-02 §9.3)* | Com quem | O que indicaria |
|---|---|---|
| Componente sem acionamento ao longo de um horizonte | — | Que a custodia de cinco Capabilities nao correspondeu a demanda real |
| Duas areas que sempre atuam juntas e nunca isoladas | **DEP-OPS** | Que construir e operar nao sao fronteiras distintas. **Contraindicado hoje:** FND-02 §4 separa quem constroi de quem sustenta |
| Handoff que so transporta, sem transformar | DEP-OPS | Que a entrega ENG → OPS nao agrega etapa |

### 12.3 Criterio de extincao
DEP-ENG deixa de ser necessario se a organizacao deixar de construir — o que contradiria a
Missao de FND-01 §1. Na extincao, cada responsabilidade e cada custodia recebe destino
explicito (IV-07, FND-02 §8.3):

| Responsabilidade / custodia | Destino declarado na extincao |
|---|---|
| Custodia de `CAP-inteligencia-artificial` e `CAP-engenharia-de-agentes` *(`nucleo`)* | **Nunca** a departamento de classe Suporte (OW-04). Transferencia e C2 com ADR e ratificacao do SOBERANO (OW-06) |
| Custodia de `CAP-arquitetura`, `CAP-engenharia`, `CAP-dados` | Destino explicito obrigatorio; competencia orfa e tao proibida quanto responsabilidade orfa (IV-07) |
| Portao QG-2 | Destino explicito obrigatorio |
| Camada de memoria **TEC** | Novo dono nomeado; a camada nao e apagada (MM-09) |
| Divida tecnica registrada e aberta | Transferida com o componente, nunca extinta com o departamento |

### 12.4 Funcoes internas nomeadas
| Funcao | Responsabilidade | Gatilho de promocao |
|---|---|---|
| **Engenharia de Agentes** | Projeto de papeis executores: escopo, limite, autonomia | **5 agentes criados** — mesmo gatilho do achado A4 de REV-CAP |
| **Dados** | Modelagem, movimentacao e confiabilidade | Primeiro dado vivo sob custodia |
| **Modelos de IA** | Escolha, instrucao e avaliacao | Segundo modelo adotado em producao |

## 13. Resumo operacional, carregamento e rastreabilidade

### 13.1 Resumo operacional
Constroi a solucao mais simples defensavel que satisfaz a spec e a sustenta tecnicamente ao
longo do tempo.

### 13.2 Perfil minimo de carregamento
| Recorte | Para que serve | Custo **medido** | Data |
|---|---|---|---|
| Secoes 1, 2 e 4 | Saber o que DEP-ENG faz e o que nao faz | **55 linhas** | 2026-07-28 |
| + secoes 5 e 10 | Decidir se DEP-ENG pode decidir algo | **116 linhas** | 2026-07-28 |
| Carta integral | Auditoria, revisao estrutural, extincao | **402 linhas** | 2026-07-28 |

> Carregar alem do recorte aplicavel exige **gatilho declarado** (CE-01, PC-01). O recorte de
> decisao custa **29% da Carta** — medido por `sed`+`wc -l` sobre os intervalos das secoes.

### 13.3 Rastreabilidade
| Campo | Conteudo |
|---|---|
| ADR de criacao do departamento | [ADR-0001](../../decisions/ADR-0001-adocao-da-fundacao-organizacional.md) — adota FND-02, que cria os nove departamentos |
| ADR do contrato desta Carta | [ADR-0011](../../decisions/ADR-0011-contrato-de-carta-de-departamento.md) |
| RFC de origem | [RFC-0008](../../rfcs/RFC-0008-contrato-de-carta-de-departamento.md) |
| Decisoes que moldam esta Carta | ADR-0002 *(vinculacao a Capability)* · ADR-0003 *(Meta Model; entidade `DEP`)* · ADR-0007 *(fronteira greenfield/legado — base de I-6)* |
| Alteracoes (ADRs) | Nenhuma |
| Fonte da custodia e do exercicio | frontmatter das cinco Cartas em `capabilities/` |
| Validacao em cenarios | [REV-DEPARTAMENTO §3](../../foundation/revisao-arquitetural-cartas-de-departamento-2026-07-28.md) |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-EXE | Criacao como **piloto** do contrato de ADR-0011. Doze blocos preenchidos. Permanece em `em-revisao`: aprovar Carta de Departamento e ato do **SOBERANO** (DC-09). |
| 1.1.0 | 2026-07-28 | DEP-EXE | Emenda **MENOR** que fecha o achado **RC-07**: acrescenta o impedimento **I-9** — aprovar, revisar ou emendar a propria Carta —, que as outras oito Cartas ja declaravam e esta nao declarava (DC-03). **Nenhum outro bloco alterado**, alem da medicao autorreferente de §13.2. Nasce em `em-revisao`, `ratificacao: pendente`: emendar Carta ja ratificada exige **ato novo** do Soberano (DC-09, LM-03, IR-01). |
