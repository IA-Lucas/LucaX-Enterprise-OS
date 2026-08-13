---
id: DEP-TLS
titulo: Ferramentas e Integracoes
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
decisoes_relacionadas: [ADR-0001, ADR-0002, ADR-0003, ADR-0007, ADR-0011, ADR-0018, ADR-0025]
substitui: []
substituido_por: null
classe: plataforma
nivel: 2
nivel_autonomia: A1
responde_a: DEP-EXE
capabilities: [CAP-integracao]
resumo: Prove, avalia e mantem as capacidades externas que a organizacao usa, para que ninguem improvise acesso.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-GOV
ratificacao: ratificada
---

# Ferramentas e Integracoes (DEP-TLS)

## Proposito
Existir como o ponto em que a dependencia externa deixa de ser improviso. Prove, avalia e
mantem as capacidades externas que a organizacao usa — **sem que ninguem obtenha acesso por
conta propria** —, e responde pelo que a organizacao passa a depender de fora dela.

## Escopo
| Item | Definicao |
|---|---|
| Classe | **plataforma** |
| Nivel | 2 |
| Responde a | **DEP-EXE** |
| Nivel de autonomia | **A1** — executa o previsto na Carta; **adocao de ferramenta nova sempre precisa de aprovacao**, porque e Tipo 1 por dependencia (FND-02 §3, nota de autonomia) |
| Poder de veto | **Nao** — veto e exclusivo da classe Guarda (FND-02 §2.1) |
| **Nao** inclui | Como o produto usa a ferramenta no dominio, e se o risco e aceitavel. Delimitacao integral na secao 4 |
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

**Missao:** prover, avaliar e manter as capacidades externas que a organizacao usa, sem que
ninguem improvise acesso.

**Mandato:** decidir **qual** capacidade externa e oficial para qual finalidade e sob que
limite — e nenhuma autoridade sobre **como** o dominio a usa, nem sobre **se** o risco dela e
aceitavel.

## 2. Capabilities custodiadas e exercidas

> **Declaracao de projecao (PJ-02).** **Fonte:** frontmatter de
> `capabilities/CAP-integracao.md`, campos `custodio` e `exercentes`.
> **Campos projetados:** apenas as linhas de DEP-TLS. **Finalidade:** responder "o que custodio
> e o que exerco" sem abrir o arquivo da Capability. **Atualizacao:** pela mesma mudanca que
> altera a Carta de Capability (CV-04). Em divergencia, prevalece a Carta de Capability (PR-1).

| Capability | Dominio · Classe | **Custodia** | **Exercicio** | Por que este departamento |
|---|---|---|---|---|
| [CAP-integracao](../../capabilities/CAP-integracao.md) | SUS · `habilitadora` | **sim** | sim | Conectar a organizacao ao que existe fora dela, com criterio e limite declarados, e o mandato integral desta area |

**Capabilities que exerco sem custodiar:** nenhuma.
**Capabilities que custodio e sao exercidas por outros:** nenhuma **declarada na fonte**.

> **Exposicao declarada.** `CAP-integracao` **depende de** `CAP-arquitetura` *(custodia de
> DEP-ENG)* e `CAP-seguranca` *(custodia de DEP-QAR)*. Dependencia dura **nao** transfere
> autoridade (AU-08, MT-09): DEP-TLS **consome** as duas e nao as governa.

> **`CAP-seguranca` e de DEP-QAR, e isso nao muda por eu operar acesso e segredo.** FND-02 §3
> atribui a DEP-TLS *"gestao de acesso e segredo **(por referencia)**"*. **Operar sob politica
> nao e custodiar a politica** — a politica e de DEP-QAR, e o que exerco e
> `CAP-integracao`. Resolucao do achado **P4** em
> [REV-ESTRUTURAL-I §3.6](../../foundation/revisao-estrutural-01-2026-07-28.md); **nenhuma
> Carta de Capability foi alterada** (PJ-03).

## 3. O que possuo — escopo exclusivo

| # | Responsabilidade | Como se verifica que esta sendo cumprida | Capability |
|---|---|---|---|
| T-1 | **Catalogo de ferramentas e integracoes** — o que e oficial, para que finalidade | Toda ferramenta em uso consta do catalogo com ficha propria (`TOL`) | CAP-integracao |
| T-2 | **Criterio de adocao** | Toda adocao declara finalidade, dado que trafega, custo, dependencia e alternativa avaliada (FND-04 §6) | CAP-integracao |
| T-3 | **Criterio de descarte** | Nenhuma ferramenta e adotada **sem** criterio de descarte declarado (PD-07) | CAP-integracao |
| T-4 | **Limites de uso** — quota, escopo, ambiente | Limite declarado na ficha e conferido antes de cada uso ampliado | CAP-integracao |
| T-5 | **Gestao de acesso e segredo, por referencia** | **Zero** credenciais em texto; apenas referencia a variavel de ambiente ou cofre (PI-08, LV-02) | CAP-integracao |
| T-6 | **Avaliacao de dependencia externa** — o que quebra se a ferramenta sumir | Mapa de dependencia externa vigente, com risco por item | CAP-integracao |
| T-7 | **Contrato de integracao** — o que trafega, em que direcao, sob que autenticacao | Declarado antes do primeiro uso; alteracao e C2 | CAP-integracao |

## 4. O que NAO me compete

| Materia | Dono real | Fonte |
|---|---|---|
| Decidir **se o risco** de uma ferramenta e aceitavel | DEP-QAR | FND-02 §3; FND-09 §8.2, linha `TOL` |
| **Definir e verificar** a politica de seguranca e privacidade | DEP-QAR | FND-02 §3; **P4** |
| Decidir **como** o produto usa a ferramenta no dominio | DEP-PRD *(o que)* · DEP-ENG *(como)* | FND-02 §3 |
| Decidir **arquitetura tecnica** e modelo de dados | DEP-ENG | FND-02 §3; FND-01 §7.3 |
| **Aprovar** a adocao de uma ferramenta | **DEP-EXE** aprova · **SOBERANO** ratifica | FND-09 §8.2, linha `TOL` |
| Definir prioridade, fila e alocacao | DEP-EXE | FND-02 §3 |
| Julgar forma, conformidade e rastreabilidade | DEP-GOV | FND-04 §12 |
| Decidir onde um registro de memoria pertence | DEP-KMS | FND-06 §2.1 |
| **Operar** a rotina que usa a ferramenta, e responder por incidente operacional | DEP-OPS | FND-02 §3 |
| Expor dado vivo a servico externo | **SOBERANO** | FND-01 §7.3; LV-08 |
| Importar conteudo do **LucaX Legacy** | Portao de admissao G1–G5 | [ADR-0007 §5.3](../../decisions/ADR-0007-fronteira-greenfield-legado.md) |
| Alterar Carta de Capability para acomodar esta Carta | custodio da Capability | PR-2, PR-3 de ADR-0011 |

## 5. O que decido — autoridade e portoes

| Materia | Autonomia | Consulta obrigatoria | **Fonte da autoridade** |
|---|---|---|---|
| **Qual ferramenta e oficial** para qual finalidade | **A1** — proponho; aprova DEP-EXE, ratifica SOBERANO | DEP-QAR *(risco)*, DEP-ENG *(viabilidade)* | FND-02 §3, DEP-TLS "Decide"; FND-01 §7.3, *Adocao de ferramenta ou integracao* |
| **Quando uma ferramenta e descartada** | **A1** | DEP-ENG, DEP-OPS *(dependentes)* | FND-02 §3 |
| **Quais limites de uso** se aplicam | A1 | DEP-EXE *(custo)* | FND-02 §3 |
| Conteudo da **ficha de ferramenta** (`TOL`) | A1 | DEP-QAR + DEP-ENG *(revisores)* | FND-09 §8.2, linha `TOL`: propoe/cria |
| **Mapa de dependencia externa** | A1 | — | FND-02 §3, "avaliacao de dependencia externa" |
| Referencia de acesso e segredo — **nunca o segredo** | A1 | DEP-QAR | FND-02 §3; PI-08 |

> **Por que tudo em A1, e nao A2.** FND-02 §3 declara: *"Opera em A1: adocao de ferramenta nova
> sempre precisa de aprovacao (PI-11 exige qualidade como criterio, mas a adocao e **Tipo 1 por
> dependencia**)"*. **A1 nao e desconfianca do departamento: e a natureza do objeto.** Adotar
> ferramenta cria dependencia externa, e dependencia externa e reversao cara (PI-06).

### 5.1 O que **nao** decido
| Materia | Quem decide | Fonte |
|---|---|---|
| Se o **risco** da ferramenta e aceitavel | **DEP-QAR** | FND-09 §8.2, linha `TOL`: revisa |
| **Aprovacao** da adocao | **DEP-EXE** | FND-09 §8.2, linha `TOL`: aprova |
| **Ratificacao** da adocao *(Tipo 1)* | **SOBERANO** | FND-09 §8.2, linha `TOL`: ratifica |
| Exposicao de dado vivo ao exterior | **SOBERANO** | FND-01 §7.3 |
| Arquitetura e modelo de dados que a integracao serve | **DEP-ENG** | FND-01 §7.3 |
| **Aprovar esta Carta** | **SOBERANO** | DC-09 |

### 5.2 Portoes sob minha responsabilidade

**Nenhum.** Os sete portoes de FND-01 §6.2 sao liberados por **DEP-EXE** *(QG-0 e QG-1)*,
DEP-ENG + DEP-GOV *(QG-2)*, DEP-QAR *(QG-3, QG-4)*, DEP-KMS *(QG-5)* e
DEP-QAR + DEP-GOV *(QG-6)*. **DEP-TLS nao libera portao algum** — habilita quem os atravessa.

> **Nenhum portao novo e criado aqui.** Os sete sao de FND-01 §6.2; acrescentar e **C3**.
> **Nao liberar portao nenhum e propriedade da classe Plataforma**, nao lacuna desta Carta:
> ES-07 — *"plataforma serve, nao decide pela linha"*.

## 6. Interfaces — entradas, saidas e consumidores

### 6.1 Entradas
| De quem | O que recebo | Em que forma | Gatilho |
|---|---|---|---|
| **DEP-ENG** | Pedido de capacidade externa, com finalidade e dado que trafega | **HANDOFF** | Necessidade tecnica identificada |
| DEP-OPS | Pedido de capacidade para rotina; sinal de falha de dependencia externa | HANDOFF ou **ALERTA** | Operacao |
| DEP-PRD · DEP-GRW · DEP-KMS | Pedido de capacidade externa para o proprio dominio | HANDOFF | Necessidade identificada |
| DEP-QAR | Parecer de risco sobre ferramenta candidata; **veto** | REPORTE ou **ALERTA** | Avaliacao de adocao |
| DEP-EXE | Aprovacao ou recusa de adocao; limite de custo | DIRETIVA | Decisao de adocao |
| DEP-GOV | Parecer de conformidade e classe de mudanca validada | CONSULTA | Antes de propor adocao |
| **SOBERANO** | Ratificacao de adocao Tipo 1; autorizacao de exposicao de dado | **DIRETIVA** | Ato do Soberano |

### 6.2 Saidas
| Entrega | Destinatario | Formato | Cadencia | Consumidor final |
|---|---|---|---|---|
| **Ficha de ferramenta** | DEP-QAR + DEP-ENG *(revisores)* → DEP-EXE *(aprova)* | Artefato `TOL` | Por candidata | Quem decide a adocao |
| **Parecer de adocao** | DEP-EXE + SOBERANO | REPORTE, com alternativa avaliada e criterio de descarte | Por candidata | Quem aprova e ratifica |
| **Catalogo de ferramentas vigente** | Toda a organizacao | Artefato `M3` derivado | A cada adocao ou descarte | Quem usa |
| **Mapa de dependencia externa** | DEP-ENG, DEP-OPS, DEP-QAR, DEP-EXE | REPORTE, com risco por item | Por horizonte e a cada adocao | Quem avalia continuidade |
| **Limites de uso vigentes** | Todos os consumidores da ferramenta | REPORTE | Por alteracao de limite | Quem opera |
| **Referencia de acesso** — nunca o segredo | Departamento consumidor | Referencia a variavel de ambiente ou cofre | Por concessao | Quem executa |
| **Alerta de dependencia critica ou credencial exposta** | DEP-QAR, DEP-EXE, **SOBERANO** | **ALERTA** | Por evento | Toda a cadeia |
| Registro de dependencia externa | DEP-ENG *(dono da camada TEC)* | Registro em camada **TEC** | Por adocao | Quem constroi |
| Aprendizado sobre ferramenta | DEP-KMS | REPORTE, secao Aprendizado | A cada encerramento | Camada APR |

### 6.3 Natureza da interacao
| Departamento | Natureza | O que trafega |
|---|---|---|
| DEP-EXE | **entrega** | Parecer, catalogo, mapa de dependencia, escalonamento |
| DEP-GOV | consulta | Conformidade — DEP-GOV **veta** DEP-TLS, nunca o inverso |
| DEP-QAR | consulta | Risco e seguranca — DEP-QAR **veta** DEP-TLS, nunca o inverso |
| **DEP-ENG** | **entrega e consulta** | Ferramenta oficial e limite entregues; viabilidade consultada |
| DEP-OPS | **entrega** | Ferramenta oficial, limite, referencia de acesso |
| DEP-KMS | **entrega** | Aprendizado gravado |
| DEP-PRD | **sem interacao estrutural direta** | FND-02 §4 declara `—` na linha TLS × PRD; o pedido de capacidade de PRD chega por DEP-ENG ou DEP-EXE |
| DEP-GRW | **sem interacao estrutural direta** | idem |

> A matriz completa de interacao vive em **FND-02 §4** e **nao** e reproduzida aqui: esta
> secao declara apenas as linhas de DEP-TLS (DC-08).

## 7. Artefatos e registros mantidos

| Tipo documental | Entidade | Meu papel | Onde vive |
|---|---|---|---|
| **Ficha de Ferramenta** | `TOL` | **Autor e proprietario**; nunca aprovador nem ratificador | fase futura — `tools/` |
| **Catalogo de ferramentas** | `M3` derivado | **Autor e proprietario** | fase futura |
| **ADR** *(de adocao ou descarte)* | `ADR` | **Autor**; nunca aprovador do proprio | `decisions/` |
| **RFC** *(de adocao)* | `RFC` | **Autor** | `rfcs/` |
| Memoria **TEC** — dependencias externas | `MEM` | **Escritor**; **DEP-ENG e o dono da camada** | `memory/tecnica/` |
| **Reporte / Consulta / Alerta** | `MSG` | **Emissor** | `memory/operacional/` |
| Carta de Agente / Subagente de DEP-TLS | `AGT` `SUB` | **Autor**, quando o agente for desta area | fase futura |

> **Nenhuma ferramenta esta adotada nesta fase**, por determinacao: `tools/` **nasce quando o
> primeiro artefato do tipo for aprovado** (FND-03 §7.2). Tipo documental que nao conste de
> [FND-10 §4](../../foundation/10-artifact-framework.md) nao existe (CS-01, MT-01).

## 8. Quando escalo

| Gatilho | Escala para | Nivel | Bloqueia execucao? |
|---|---|---|---|
| **Credencial exposta** | SOBERANO, via DEP-QAR | **E4** *(pula niveis, EC-02)* | **Sim** — revogar, rotacionar, registrar incidente (PI-08) |
| Adocao com **custo recorrente** | SOBERANO, via DEP-EXE | **E4** | **Sim** |
| Adocao que envolva **dado sensivel** ou exposicao externa | SOBERANO | **E4** | **Sim** (LV-08) |
| **Dependencia critica** — o que quebra se a ferramenta sumir | SOBERANO, via DEP-EXE | **E4** | **Sim** |
| Toda **adocao de ferramenta nova** *(Tipo 1 por dependencia)* | DEP-EXE aprova · SOBERANO ratifica | **E4** | **Sim** — A1 |
| Ferramenta em uso **sem ficha** detectada | DEP-GOV *(registro)* + DEP-QAR *(risco)* | **E3** | **Sim** — improviso de acesso e o que esta area existe para impedir |
| Duvida de conformidade ou de risco | DEP-GOV / DEP-QAR | **E3** | Sim |
| Conflito sobre qual ferramenta serve a qual area | DEP-EXE | **E2** | Nao |
| Pedido de capacidade sem finalidade declarada | quem pediu, por devolucao de handoff | **E1** | Sim, para o item |
| Duvida rotineira de limite de uso resolvivel por premissa | ninguem — **decide e registra a premissa** | **E0** | Nao |

### 8.1 Cadencias de que participo
| Cadencia | Meu papel | O que produzo |
|---|---|---|
| Abertura de ciclo | Recebo prioridade | Estado do catalogo e limites vigentes |
| **Sincronizacao de linha** | Participo | Dependencias externas e bloqueios |
| Fechamento de ciclo | Reporto | Consumo, custo e limites do ciclo |
| **Revisao estrutural** *(por horizonte)* | Participo | **Mapa de dependencia externa atualizado** |
| Colheita de aprendizado | Contribuo | Licao sobre ferramenta adotada ou descartada |

### 8.2 Handoffs
| Handoff | Emito / recebo | Criterio de aceite | Criterio de devolucao |
|---|---|---|---|
| **Pedido de capacidade externa** | **Recebo** | Finalidade, dado que trafega, volume esperado e prazo declarados | Finalidade generica; dado nao declarado; pedido que ja e atendido por ferramenta do catalogo (T-1) |
| **Ficha de ferramenta para revisao** | **Emito** a DEP-QAR + DEP-ENG | Alternativa avaliada, custo, dependencia e **criterio de descarte** presentes | Criterio de descarte ausente — devolucao obrigatoria (PD-07, T-3) |
| **Ferramenta oficial e limite** | **Emito** ao consumidor | Ficha aprovada e ratificada; limite declarado | Ferramenta nao ratificada — nao se entrega |
| **Referencia de acesso** | **Emito** ao consumidor | Referencia a variavel ou cofre | **Qualquer segredo em texto — devolucao imediata e incidente** (LV-02) |

> **Handoff devolvido duas vezes pelo mesmo motivo escala a DEP-EXE** — ha defeito de
> fronteira (HO-03, FND-02 §9.2).

## 9. Memoria autorizada e politica de contexto

| Camada | Meu papel | Sob que condicao |
|---|---|---|
| **EST** | **Leitor obrigatorio** antes de qualquer decisao C2/C3 | Nao escrevo: escrita em EST e de DEP-GOV, mediante ADR (FND-06 §3.1) |
| **PRD** | Leitor | Antes de avaliar se a ferramenta serve ao dominio |
| **TEC** | **Escritor** — dependencias externas | **DEP-ENG e o dono da camada** (FND-06 §3.3). Escrevo o que a organizacao passa a depender de fora |
| **OPR** | **Escritor** | Consumo, custo, limites e estado das integracoes do ciclo corrente |
| **APR** | **Contribuinte obrigatorio**; DEP-KMS e o dono | Toda adocao frustrada, descarte e falha de dependencia vira licao (QG-5) |

### 9.1 Politica de contexto
| Item | Valor |
|---|---|
| Pacote minimo para operar | Nucleo obrigatorio + a **ficha da ferramenta** em questao + `TPL-ferramenta` |
| Custo medido do pacote | **1.099 linhas** de nucleo + **145 linhas** de `TPL-ferramenta`, medidos em 2026-07-28 = **1.244 linhas**. **Nenhuma ficha existe nesta fase** |
| Gatilho para carregar alem do minimo | **Candidata em avaliacao**, ou incidente de dependencia externa. Carrega-se **a ferramenta em questao**, nunca o catalogo inteiro |
| **Nao** carrego por padrao | O catalogo de ferramentas integral; a Carta de `CAP-arquitetura` e a de `CAP-seguranca`, das quais dependo mas que **nao governo**; perfil `arquivo` |

## 10. Riscos, impedimentos e segregacao

> **Secao obrigatoria (DC-03).** Sem ela a Carta nao e valida.

| # | Materia em que estou impedido | Por que | **Quem me substitui** | Fonte |
|---|---|---|---|---|
| **I-1** | **Aprovar ou ratificar a adocao que eu proponho** | Quem propoe nao aprova | **DEP-EXE** *(aprova)* · **SOBERANO** *(ratifica, Tipo 1)* | PI-05, GV-04, LV-03; FND-09 §8.2, linha `TOL` |
| **I-2** | **Decidir se o risco de uma ferramenta e aceitavel** | Risco e materia de `CAP-seguranca`, custodiada por DEP-QAR — nao por quem quer a ferramenta | **DEP-QAR** | FND-02 §3; **P4** |
| **I-3** | **Definir ou verificar a politica de seguranca e privacidade** | **Operar sob politica nao e custodiar a politica** | **DEP-QAR** | FND-02 §3 *("por referencia")*; **P4** |
| **I-4** | **Gravar, transmitir ou manusear credencial em texto**, ainda que a pedido | Segredo nunca em texto, **sem excecao** | Referencia a variavel de ambiente ou cofre; credencial exposta e **incidente critico** | **PI-08, LV-02** — nao admite excecao formal (FND-01 §8.3) |
| **I-5** | **Adotar, habilitar ou usar ferramenta sem ficha aprovada e ratificada** | Improviso de acesso e exatamente o que esta area existe para impedir | O rito completo: ficha → revisao → aprovacao → ratificacao | PI-12, LV-06; FND-04 §6 |
| **I-6** | **Decidir como o dominio usa a ferramenta** | Plataforma serve, nao decide pela linha | **DEP-PRD** *(o que)* · **DEP-ENG** *(como)* | **ES-07**; FND-02 §2.1 |
| **I-7** | **Priorizar, avaliar ou instruir departamento de Guarda** | Plataforma nao coordena a Guarda | **DEP-EXE** coordena Linha e Plataforma; a Guarda responde ao **SOBERANO** | ES-02, IV-01 |
| **I-8** | **Expor dado vivo a servico externo** | Exposicao e materia do Soberano, e nenhuma adocao a autoriza por tabela | **SOBERANO**, com parecer de DEP-QAR | FND-01 §7.3; **LV-08** |
| **I-9** | **Importar conteudo do LucaX Legacy** | Origem externa nao tem autoridade por existir | Portao G1–G5, com decisao formal | [ADR-0007 §5.3](../../decisions/ADR-0007-fronteira-greenfield-legado.md), FR-03 |
| **I-10** | **Aprovar, revisar ou emendar esta Carta** | E o instrumento que define a minha propria autoridade | **DEP-GOV** *(revisa)* · **SOBERANO** *(aprova e ratifica)* | RM-06b, LV-03; FND-09 §8.2 |
| **I-11** | **Alterar `CAP-arquitetura` ou `CAP-seguranca`**, das quais `CAP-integracao` depende | Consumir nao da autoridade sobre o consumido | Custodios: **DEP-ENG** e **DEP-QAR**, pelo rito de FND-08 §6.3 | AU-08, MT-09; PR-3 |

### 10.1 Riscos proprios do dominio
| # | Risco | Probabilidade | Impacto | Mitigacao declarada |
|---|---|---|---|---|
| RT-1 | **Credencial em texto** | Baixa | **Critico** | I-4; varredura do acervo a cada QG-4 por DEP-QAR — **0 ocorrencias** medidas em 2026-07-28 |
| RT-2 | **Dependencia critica sem alternativa** — a organizacao para se a ferramenta sumir | **Media** | **Alto** | T-3 e T-6: **nenhuma** adocao sem criterio de descarte e sem alternativa avaliada; PD-07 permite **veto de DEP-QAR** |
| RT-3 | **Adocao por conveniencia**, contra PI-11 | Media | Medio | O criterio primario e o **resultado para a tarefa**; custo e restricao declarada, nunca criterio dominante (PI-11) |
| RT-4 | **Ferramenta em uso sem ficha** — o improviso que a area existe para impedir | **Media** | **Alto** | I-5; gatilho de escalonamento **E3** proprio em §8; **0** ferramentas adotadas nesta fase, logo **0** ocorrencias possiveis hoje |
| RT-5 | **Departamento sem exercicio** — DEP-TLS **nao registrou nenhum ato** ate esta data | **Observado** | Medio | Registrado em [REV-ESTRUTURAL-I §3.2](../../foundation/revisao-estrutural-01-2026-07-28.md), no teste de **IC-7**. E o motivo de todos os indicadores de atividade valerem **zero** (§11) |
| RT-6 | **Fronteira ENG ↔ TLS mutuamente exposta** | Media | Baixa | Achado **P8** de `capabilities/README §10.3` — **nao e ciclo proibido**; o grafo de `depende-de` entre Capabilities permanece aciclico. Gatilho: **2a revisao estrutural** |

### 10.2 Incompatibilidades de papel
| Papel A | Papel B | Por que nao se acumulam na mesma mudanca |
|---|---|---|
| Proponente da adocao | Aprovador da adocao | PI-05, GV-04 — e o impedimento **I-1** |
| Proponente da adocao | Avaliador do risco | **P4** — quem quer a ferramenta nao julga o risco dela (I-2) |
| Operador do acesso | Definidor da politica de seguranca | **Operar sob politica ≠ custodiar a politica** (I-3) |
| Custodio de `CAP-integracao` | Autoridade que aprova a propria proposta de evolucao dela | FND-08 §6.1 — o custodio **propoe**; nao aprova |
| Plataforma | Decisor do dominio servido | **ES-07** — plataforma serve, nao decide pela linha (I-6) |

## 11. Indicadores

> Indicador **sem valor medido** declara-se `definido, sem valor`. Afirmar desempenho sem
> medida e LV-12.

| # | Indicador | Definicao | Direcao | **Valor medido** | **Data** |
|---|---|---|---|---|---|
| KT-1 | Capabilities custodiadas | Contagem na projecao de `capabilities/README §10` | estavel | **1** | 2026-07-28 |
| KT-2 | **Ferramentas adotadas** | Contagem de fichas `TOL` | — | **0** — nenhuma adotada; `tools/` **nao existe** por determinacao | 2026-07-28 |
| KT-3 | **Integracoes ativas** | Contagem de contratos de integracao vigentes | — | **0** | 2026-07-28 |
| KT-4 | **Credenciais em texto detectadas** | Varredura do acervo | → 0 | **0** | 2026-07-28 |
| KT-5 | Ferramentas em uso **sem ficha** | Contagem | → 0 | **0** — consequencia direta de KT-2 | 2026-07-28 |
| KT-6 | Dependencias externas mapeadas | Contagem no mapa | — | **0** | 2026-07-28 |
| KT-7 | Atos registrados por DEP-TLS no acervo | Contagem de artefatos com autor DEP-TLS | — | **0** — risco RT-5, observado | 2026-07-28 |
| KT-8 | Adocoes com criterio de descarte declarado | Adocoes com criterio / adocoes totais | → 100% | **`definido, sem valor`** — divisao por zero; nao ha adocao | — |
| KT-9 | Tempo entre pedido de capacidade e ferramenta disponivel | Latencia | ↓ | **`definido, sem valor`** — nenhum pedido recebido | — |
| KT-10 | Ferramentas descartadas por criterio proprio | Contagem | estavel e nao-zero | **`definido, sem valor`** — nenhum ciclo de adocao ocorreu | — |
| KT-11 | Incidentes de dependencia externa | Contagem | → 0 | **`definido, sem valor`** — nenhuma dependencia externa existe | — |
| KT-12 | Custo recorrente de ferramentas | Soma declarada na ficha | ↓ | **`definido, sem valor`** — nenhum custo contratado | — |

**Contagem: 12 indicadores definidos · 7 com valor medido · 5 `definido, sem valor`.**

> **Os sete medidos valem zero, e isso e o estado honesto — e o mais literal do acervo.**
> DEP-TLS e o **unico departamento que nao registrou nenhum ato** ate esta data (KT-7), porque
> adotar ferramenta esta fora do que esta fase permite. **Zero em KT-4 e KT-5 e resultado bom;
> zero em KT-2 e KT-7 e ausencia determinada, nao desempenho.** A distincao esta escrita para
> que a leitura nao as confunda (PI-10).

## 12. Ciclo de vida — especializacao, fusao e retirada

### 12.1 Gatilhos de especializacao
| Gatilho *(FND-02 §9.2)* | Aplica-se? | **Sinal ja observado** | Movimento previsto |
|---|---|---|---|
| Escopo heterogeneo | **Nao** | **Nenhum** — sete responsabilidades sobre **uma** Capability, todas da mesma natureza: mediar o externo | — |
| Carga concentrada | **Nao avaliavel** | **Nenhum** — zero atos registrados (KT-7) | — |
| Contexto excessivo | **Nao** | Pacote minimo **1.244 linhas**, **3,9%** do acervo | — |
| Fronteira em disputa | **Nao** | **Zero** conflitos registrados. P8 *(ENG ↔ TLS)* e exposicao mutua, **nao** conflito | — |
| Duplicacao | Nao | Nenhum procedimento refeito — nao ha procedimento |
| Gargalo de decisao | Nao | **0** escalonamentos registrados | — |
| Conhecimento ilhado | Nao | Nao ha resultado produzido | — |

> **Decisao registrada: nao especializar** (FND-04 §6.2). **Zero gatilhos com sinal**, e SE-02
> exige dois. Neste departamento a decisao e trivial e o motivo e o mesmo de RT-5: **nao ha
> exercicio de que extrair sinal**. Registrar *"avaliado, nenhum sinal"* e o que a norma exige;
> registrar *"nao aplicavel"* sem avaliar seria omissao.

### 12.2 Gatilhos de fusao ou consolidacao
| Sinal *(FND-02 §9.3)* | Com quem | O que indicaria |
|---|---|---|
| **Duas areas que sempre atuam juntas e nunca isoladas** | **DEP-KMS** | Que a distincao **conhecimento interno × capacidade externa** nao existe na pratica. **E a unica fusao do sistema que nenhuma norma proibe** — achado **IC-7** |
| Componente sem acionamento ao longo de um horizonte | **DEP-TLS**, sobre si mesmo | Que a area foi criada antes da demanda. **Nao avaliavel**: nenhum horizonte se tornou avaliavel sob `HZ-02` ([ADR-0013](../../decisions/ADR-0013-criterio-de-horizonte-e-consolidacao.md)) |
| Handoff que so transporta | DEP-ENG | Que a mediacao TLS entre ENG e o externo nao transforma o trabalho |
| Custo de coordenacao maior que o ganho | — | Nenhum sinal registrado |

> ### IC-7 — a fusao possivel, testada e **sem sinal**
> A hipotese **DEP-KMS + DEP-TLS** foi testada em
> [REV-ESTRUTURAL-I §3.2](../../foundation/revisao-estrutural-01-2026-07-28.md) e o resultado
> foi **sem sinal**, com o motivo declarado: **DEP-TLS nao tinha Carta e nao registrou nenhum
> ato**. **Esta Carta remove metade do motivo** — a ausencia de Carta —, e **nao** remove a
> outra: **KT-7 continua zero**.
>
> *"Sem vedacao"* e *"sem sinal"* permanecem distintos, e agora um deles esta **medido**. IC-7
> permanece **fechado quanto ao teste** e o gatilho de reteste e o **primeiro ato registrado por
> DEP-TLS** — a primeira ficha `TOL`.

### 12.3 Criterio de extincao
DEP-TLS deixa de ser necessario se a organizacao deixar de depender de qualquer capacidade
externa — o que hoje contradiria a propria operacao. Na extincao, cada responsabilidade e cada
custodia recebe destino explicito (IV-07, FND-02 §8.3):

| Responsabilidade / custodia | Destino declarado na extincao |
|---|---|
| Custodia de `CAP-integracao` | Destino explicito obrigatorio. Candidato natural: **DEP-ENG**, que ja custodia `CAP-arquitetura`, da qual `CAP-integracao` depende. **Nunca** departamento de Guarda — concentraria adocao e avaliacao de risco no mesmo papel |
| **Gestao de acesso e segredo, por referencia** | Destino explicito obrigatorio e **imediato**; acesso sem dono e o risco que PI-08 protege |
| Catalogo de ferramentas e limites de uso | Transferido integralmente; ferramenta sem limite declarado e ferramenta sem controle |
| Mapa de dependencia externa | Transferido; e o unico registro do que quebra se o externo falhar |
| Fichas `TOL` ja emitidas | Preservadas; nenhuma e apagada (FND-04 §7.2) |

### 12.4 Funcoes internas nomeadas
> Responsabilidades hospedadas aqui que ainda nao merecem departamento proprio (ES-04).

| Funcao | Responsabilidade | Gatilho de promocao |
|---|---|---|
| **Acesso e segredo** | Concessao, rotacao e revogacao por referencia | **Primeira credencial sob gestao** |
| **Avaliacao de dependencia** | Mapa do que quebra se o externo falhar | **Terceira ferramenta adotada** |
| **Custo de ferramenta** | Consumo e limite por integracao | Primeiro custo recorrente contratado — **coordena com a funcao Recursos (FIN) de DEP-EXE**, que ja existe (FND-02 §3) |

## 13. Resumo operacional, carregamento e rastreabilidade

### 13.1 Resumo operacional
Prove, avalia e mantem as capacidades externas que a organizacao usa, para que ninguem
improvise acesso.

### 13.2 Perfil minimo de carregamento
| Recorte | Para que serve | Custo **medido** | Data |
|---|---|---|---|
| Secoes 1, 2 e 4 | Saber o que DEP-TLS faz e o que nao faz | **52 linhas** | 2026-07-28 |
| + secoes 5 e 10 | Decidir se DEP-TLS pode adotar ou habilitar algo | **125 linhas** | 2026-07-28 |
| Carta integral | Auditoria, revisao estrutural, extincao | **425 linhas** | 2026-08-12 |

> Carregar alem do recorte aplicavel exige **gatilho declarado** (CE-01, PC-01). O recorte de decisao custa **29% da Carta** — medido por
> `sed`+`wc -l` sobre os intervalos das secoes.

### 13.3 Rastreabilidade
| Campo | Conteudo |
|---|---|
| ADR de criacao do departamento | [ADR-0001](../../decisions/ADR-0001-adocao-da-fundacao-organizacional.md) — adota FND-02, que cria os nove departamentos |
| ADR do contrato desta Carta | [ADR-0011](../../decisions/ADR-0011-contrato-de-carta-de-departamento.md) |
| RFC de origem | [RFC-0008](../../rfcs/RFC-0008-contrato-de-carta-de-departamento.md) |
| Decisoes que moldam esta Carta | ADR-0002 *(vinculacao a Capability)* · ADR-0003 *(Meta Model; entidade `DEP` e linha `TOL`)* · ADR-0007 *(fronteira greenfield/legado — base de I-9)* |
| Achado que esta Carta trata | **P4** *(operar sob politica ≠ custodiar a politica)* — declarado em §2 e em **I-3** · **IC-7** *(fusao KMS+TLS)* — reavaliado em §12.2 · **P8** — declarado em RT-6 |
| Alteracoes (ADRs) | Nenhuma |
| Fonte da custodia e do exercicio | frontmatter de `capabilities/CAP-integracao.md` |
| Validacao em cenarios | [REV-ROLLOUT §3](../../foundation/revisao-arquitetural-rollout-cartas-2026-07-28.md) |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-EXE | Criacao — **sexta Carta do sistema**, segunda do rollout. **Completa a classe Plataforma** e torna DEP-TLS o **ultimo departamento a receber Carta entre os que nunca registraram ato**. Doze blocos preenchidos. Declara **zero portoes** sob responsabilidade e **zero atos registrados** (KT-7), e reavalia **IC-7** com metade do motivo removido. Permanece em `em-revisao`: aprovar Carta de Departamento e ato do **SOBERANO** (DC-09). |
| 1.1.0 | 2026-07-30 | DEP-EXE | Emenda **C2 · Tipo 2** por **ADR-0025**, em **cascata** (`CV-04`) de [ADR-0018](../../decisions/ADR-0018-liberacao-do-portao-qg-1.md), **ratificado**: **§5.2** deixa de afirmar que **`QG-1` e liberado por `DEP-PRD`** e passa a declarar **`DEP-EXE` *(QG-0 e QG-1)***, alinhando esta Carta a fonte ratificada **FND-01 §6.2**. **Uma afirmacao falsa corrigida; duas linhas substituidas; `0` linhas acrescentadas.** Fecha **RD-37** quanto a esta Carta. **Nenhuma responsabilidade, portao, papel, direito de decisao, interface, risco, metrica ou Capability desta Carta foi criado, removido ou alterado** — este departamento continua **nao liberando portao algum**, e o que muda e **de quem se diz** que libera `QG-1`. **Nenhum titular novo:** `DEP-EXE` ja e o titular por ADR-0018 desde 2026-07-29. |
