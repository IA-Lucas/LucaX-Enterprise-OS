---
id: IDX-capabilities
titulo: Enterprise Capability Model — Catalogo e Mapa Oficial
tipo: relatorio
versao: 1.3.0
status: ativo
camada_memoria: estrategica
autor: DEP-EXE
proprietario: DEP-EXE
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0002, ADR-0005, ADR-0011]
substitui: []
substituido_por: null
resumo: Cataloga as 23 Capabilities vigentes, o mapa de dependencias duras e a projecao de custodia e exercicio por departamento.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-GOV
ratificacao: nao-exigida
projecao_de: frontmatter das 23 Cartas em capabilities/CAP-*.md
---

# Enterprise Capability Model

## Proposito
Manter o catalogo oficial das competencias permanentes do LucaX Enterprise OS e o mapa
autoritativo de relacoes entre elas. Este documento e a fonte unica para verificar
cobertura, vinculacao e dependencia.

## Escopo
As 23 Capabilities vigentes, sua classificacao nos tres eixos, o mapa de relacoes e as
regras de consulta. O framework que as governa esta em
[FND-08](../foundation/08-capability-framework.md).

## Responsaveis
| Papel | Responsavel |
|---|---|
| Proprietario do catalogo | DEP-EXE |
| Custodia dos registros | DEP-KMS |
| Conformidade e vinculacao | DEP-GOV |
| Sobreposicao, lacuna e indicadores | DEP-QAR |
| Ratificador | SOBERANO |

---

## 1. Regra de entrada

> **Nenhum Departamento, Agente, Subagente, Skill, Workflow ou Produto pode existir sem
> estar vinculado a pelo menos uma Capability deste catalogo** (FND-08 §8).

Componente cuja competencia nao cabe em nenhuma Capability aqui **revela lacuna**: abre-se
RFC de Capability antes de criar o componente (VC-02).

## 2. Catalogo — 23 Capabilities em 7 dominios

### `DIR` — Direcao
| Capability | Classe | Maturidade | Custodio |
|---|---|---|---|
| [Estrategia](CAP-estrategia.md) | `nucleo` | `emergente` | DEP-EXE |
| [Governanca Organizacional](CAP-governanca.md) | `nucleo` | `emergente` | DEP-GOV |
| [Coordenacao Organizacional](CAP-coordenacao.md) | `habilitadora` | `experimental` | DEP-EXE |

### `VAL` — Descoberta e Valor
| Capability | Classe | Maturidade | Custodio |
|---|---|---|---|
| [Pesquisa](CAP-pesquisa.md) | `habilitadora` | `experimental` | DEP-PRD |
| [Produto](CAP-produto.md) | `nucleo` | `experimental` | DEP-PRD |
| [Design](CAP-design.md) | `habilitadora` | `experimental` | DEP-PRD |

### `REA` — Realizacao
| Capability | Classe | Maturidade | Custodio |
|---|---|---|---|
| [Arquitetura](CAP-arquitetura.md) | `habilitadora` | `experimental` | DEP-ENG |
| [Engenharia](CAP-engenharia.md) | `habilitadora` | `experimental` | DEP-ENG |
| [Dados](CAP-dados.md) | `habilitadora` | `experimental` | DEP-ENG |
| [Inteligencia Artificial](CAP-inteligencia-artificial.md) | `nucleo` | `experimental` | DEP-ENG |
| [Engenharia de Agentes](CAP-engenharia-de-agentes.md) | `nucleo` | `experimental` | DEP-ENG |

### `GAR` — Garantia *(custodia obrigatoria na Guarda, OW-05)*
| Capability | Classe | Maturidade | Custodio |
|---|---|---|---|
| [Qualidade](CAP-qualidade.md) | `nucleo` | `experimental` | DEP-QAR |
| [Seguranca](CAP-seguranca.md) | `habilitadora` | `experimental` | DEP-QAR |
| [Juridico e Regulatorio](CAP-juridico.md) | `suporte` | `experimental` | DEP-QAR |

### `SUS` — Sustentacao
| Capability | Classe | Maturidade | Custodio |
|---|---|---|---|
| [Operacoes](CAP-operacoes.md) | `habilitadora` | `experimental` | DEP-OPS |
| [Infraestrutura](CAP-infraestrutura.md) | `habilitadora` | `experimental` | DEP-OPS |
| [Integracao e Ferramental](CAP-integracao.md) | `habilitadora` | `experimental` | DEP-TLS |

### `MER` — Mercado e Recursos
| Capability | Classe | Maturidade | Custodio |
|---|---|---|---|
| [Marketing](CAP-marketing.md) | `habilitadora` | `experimental` | DEP-GRW |
| [Comercial](CAP-comercial.md) | `habilitadora` | `experimental` | DEP-GRW |
| [Financeiro](CAP-financeiro.md) | `suporte` | `experimental` | DEP-EXE |

### `COG` — Cognicao Organizacional
| Capability | Classe | Maturidade | Custodio |
|---|---|---|---|
| [Conhecimento](CAP-conhecimento.md) | `nucleo` | `experimental` | DEP-KMS |
| [Aprendizado Organizacional](CAP-aprendizado-organizacional.md) | `nucleo` | `experimental` | DEP-KMS |
| [Comunicacao Organizacional](CAP-comunicacao.md) | `habilitadora` | `experimental` | DEP-EXE |

## 3. Distribuicao

| Eixo | Distribuicao |
|---|---|
| **Dominio** | DIR 3 · VAL 3 · REA 5 · GAR 3 · SUS 3 · MER 3 · COG 3 |
| **Classe** | `nucleo` 8 · `habilitadora` 13 · `suporte` 2 |
| **Maturidade** | `emergente` 2 · `experimental` 21 |
| **Custodia** | DEP-ENG 5 · DEP-EXE 4 · DEP-QAR 3 · DEP-PRD 3 · DEP-KMS 2 · DEP-GRW 2 · DEP-OPS 2 · DEP-GOV 1 · DEP-TLS 1 |

### 3.1 As oito Capabilities `nucleo`

| Capability | Por que a proposta inteira falha sem ela |
|---|---|
| **Engenharia de Agentes** | E o que distingue o LucaX de uma empresa que apenas usa IA |
| **Inteligencia Artificial** | E o substrato sobre o qual todo o trabalho e executado |
| **Conhecimento** | Sem memoria que compoe, nao ha Visao V2 |
| **Aprendizado Organizacional** | Sem licao acumulada, cada projeto recomeca do zero |
| **Qualidade** | Sem verificacao independente, nao ha Visao V3 |
| **Governanca** | Sem rastreabilidade, nao ha Visao V4 nem soberania verificavel |
| **Produto** | Sem definicao correta, constroi-se a coisa errada com eficiencia |
| **Estrategia** | Sem direcao, a organizacao nao tem por que existir |

> Oito de 23 (35%) e proporcao alta para uma classe que deveria ser seletiva. Isso e
> analisado como achado na [revisao arquitetural §7](revisao-arquitetural-2026-07-28.md),
> com recomendacao de reavaliacao no primeiro horizonte.

## 4. Mapa oficial de dependencias duras

Somente relacoes `depende-de`. Ordem topologica verificada: **sem ciclo** (RL-01).

```
NIVEL 0  ── base, nao depende de ninguem
  CAP-conhecimento

NIVEL 1
  CAP-governanca                 <- conhecimento
  CAP-comunicacao                <- conhecimento
  CAP-aprendizado-organizacional <- conhecimento
  CAP-pesquisa                   <- conhecimento

NIVEL 2
  CAP-estrategia                 <- conhecimento, governanca
  CAP-qualidade                  <- governanca, aprendizado
  CAP-seguranca                  <- governanca
  CAP-juridico                   <- governanca

NIVEL 3
  CAP-coordenacao                <- estrategia, comunicacao
  CAP-produto                    <- pesquisa, estrategia

NIVEL 4
  CAP-arquitetura                <- produto
  CAP-design                     <- produto
  CAP-marketing                  <- produto, estrategia

NIVEL 5
  CAP-engenharia                 <- arquitetura
  CAP-dados                      <- arquitetura, seguranca
  CAP-infraestrutura             <- arquitetura
  CAP-integracao                 <- arquitetura, seguranca
  CAP-comercial                  <- marketing, produto, juridico

NIVEL 6
  CAP-inteligencia-artificial    <- dados, arquitetura, integracao
  CAP-operacoes                  <- infraestrutura, engenharia
  CAP-financeiro                 <- coordenacao, comercial

NIVEL 7
  CAP-engenharia-de-agentes      <- inteligencia-artificial, conhecimento,
                                    comunicacao, aprendizado-organizacional
```

### 4.1 Leituras do mapa

| Observacao | Significado |
|---|---|
| `CAP-conhecimento` e a unica de nivel 0 | Toda a organizacao repousa sobre a capacidade de lembrar. Falha aqui propaga para tudo. |
| `CAP-engenharia-de-agentes` e a mais profunda (nivel 7) | E a competencia mais composta: exige que sete outras funcionem antes. Coerente com ser a distintiva e a ultima a amadurecer. |
| `CAP-produto` e `CAP-arquitetura` sao os maiores fan-outs | Defeito nelas propaga para toda a realizacao. Prioridade de indicador. |
| Nenhuma Capability de Garantia e dependencia dura de quem ela verifica | Preserva PI-05 e RL-05: o verificador nunca depende do verificado. |

## 5. Relacoes de verificacao (`verifica`)

Exercidas pelo dominio `GAR` e por `CAP-governanca`. Nunca coexistem com `depende-de` na
mesma direcao (RL-05).

| Verificador | Verifica |
|---|---|
| `CAP-governanca` | **todas as demais** — forma, conformidade e rastreabilidade. **Nunca a si propria** (RM-06b, LV-03) |
| `CAP-qualidade` | `CAP-engenharia`, `CAP-arquitetura`, `CAP-produto`, `CAP-dados`, `CAP-engenharia-de-agentes` |
| `CAP-seguranca` | `CAP-engenharia`, `CAP-infraestrutura`, `CAP-dados`, `CAP-integracao` |

> **Quem verifica o que DEP-GOV produz (ADR-0005).** Nenhuma Capability o faz de forma
> permanente: `CAP-qualidade` ja **depende de** `CAP-governanca` (mapa §4, nivel 2), e
> acrescentar `verifica` na mesma direcao violaria RL-05. A verificacao cabe ao **revisor
> independente da mudanca** — na pratica DEP-QAR, por papel e nao por competencia
> (FND-04 §3) — e, em materia constitucional, ao **Soberano**, a quem a Guarda responde
> diretamente (FND-02 §2.1).

## 6. Relacoes de coordenacao (`coordena`)

| Coordenador | Coordena |
|---|---|
| `CAP-coordenacao` | todas as Capabilities de realizacao, sustentacao e mercado |

## 7. Fluxos de saida sem dependencia dura (`consome-saida-de`)

Relacoes reais, mas que nao travam a Capability consumidora. Admitem ciclo (RL-02).

| Origem → Destino | O que flui |
|---|---|
| `CAP-pesquisa` → `estrategia`, `design`, `marketing` | Achados, contexto de uso, panorama |
| `CAP-aprendizado` → `estrategia`, `produto` | Heuristicas, hipoteses invalidadas |
| `CAP-design` → `engenharia`, `marketing` | Forma, comportamento, linguagem |
| `CAP-dados` → `produto`, `estrategia`, `comercial` | Metricas confiaveis |
| `CAP-operacoes` → `produto`, `dados`, `aprendizado` | Sinal de uso real, incidentes |
| `CAP-comercial` → `produto`, `marketing` | Objecoes e motivos de perda |
| `CAP-qualidade` → `aprendizado` | Defeitos e vereditos |
| `CAP-IA`, `integracao`, `infraestrutura` → `financeiro` | Custos |

## 8. Consulta obrigatoria

| Momento | O que verificar aqui |
|---|---|
| Antes de criar qualquer componente | A qual Capability ele se vincula (VC-01) |
| Se nao houver Capability adequada | Abrir RFC de Capability **antes** do componente (VC-02) |
| Antes de propor Capability nova | Sobreposicao com o catalogo (FND-08 §7.1) |
| Em QG-0 | Vinculo declarado e valido (VC-04) |
| Na revisao estrutural | Gatilhos de especializacao, fusao e depreciacao (FND-08 §7.5) |

## 9. Estado do catalogo

| Campo | Valor |
|---|---|
| Capabilities vigentes | 23 |
| Aposentadas | 0 |
| Em depreciacao | 0 |
| Componentes vinculados | **0** — nenhum departamento, agente, skill, workflow ou produto criado |
| Indicadores definidos | 111 |
| Indicadores com valor medido | **23** — quase todos registrando ausencia de violacao, nao presenca de competencia |
| Ultima revisao arquitetural | [2026-07-28](revisao-arquitetural-2026-07-28.md) |

## 10. Matriz Departamento × Capability

> **Declaracao de projecao (PJ-02, [ADR-0008](../decisions/ADR-0008-uma-fonte-multiplas-projecoes.md)).**
> **Fonte:** o frontmatter das **23** Cartas em `capabilities/CAP-<slug>.md`, campos
> `custodio`, `exercentes` e `depende_de`.
> **Campos projetados:** custodia, exercicio e a exposicao derivada de `depende-de`, pivotados
> **por departamento**.
> **Finalidade:** responder "o que este departamento custodia e exerce" em uma leitura, sem
> percorrer 23 arquivos — pergunta que nenhuma secao anterior responde, porque §2 e §4 sao
> orientadas a Capability, nao a departamento.
> **Metodo de atualizacao:** pela mesma mudanca que altera o frontmatter de uma Carta de
> Capability (CV-04). Divergencia e defeito **desta** tabela, nunca da fonte (PJ-03).
> **Esta e a unica projecao Departamento × Capability do acervo** (ADR-0011 §5.5).

### 10.1 Projecao por departamento

| Departamento | Classe | **Custodia** | **Exerce** | Exerce sem custodiar | Custodia exercida por outro |
|---|---|---|---|---|---|
| **DEP-EXE** | Comando | estrategia · coordenacao · financeiro · **comunicacao** | estrategia · coordenacao · financeiro · comunicacao | — | **comunicacao** *(tambem por DEP-KMS)* |
| **DEP-GOV** | Guarda | governanca | governanca | — | — |
| **DEP-QAR** | Guarda | qualidade · seguranca · juridico | qualidade · seguranca · juridico | — | — |
| **DEP-PRD** | Linha | pesquisa · produto · design | pesquisa · produto · design | — | — |
| **DEP-ENG** | Linha | arquitetura · engenharia · dados · inteligencia-artificial · engenharia-de-agentes | as mesmas 5 | — | — |
| **DEP-OPS** | Linha | operacoes · infraestrutura | operacoes · infraestrutura | — | — |
| **DEP-GRW** | Linha | marketing · comercial | marketing · comercial | — | — |
| **DEP-KMS** | Plataforma | conhecimento · aprendizado-organizacional | conhecimento · aprendizado-organizacional · **comunicacao** | **comunicacao** | — |
| **DEP-TLS** | Plataforma | integracao | integracao | — | — |

**Totais medidos:** 23 custodias · **24** vinculos de exercicio · **1** exercicio sem
custodia · **1** custodia compartilhada no exercicio · **0** Capabilities sem custodio ·
**0** Capabilities sem exercente · **0** departamentos sem custodia.

### 10.2 Exposicao derivada de `depende-de`

> **Isto nao e uma relacao.** `DEP → DEP` **nao consta** dos pares permitidos de **R-04** em
> [FND-09 §6.2](../foundation/09-meta-model.md); declarar dependencia entre departamentos
> seria relacao **nula** (RM-02). A tabela abaixo e leitura derivada: mostra de que
> **custodias alheias** cada departamento depende **por via das Capabilities que custodia**.
> Custodia nao cria dependencia (RM-05, FND-09 §9.4).

| Departamento | Depende de custodia de | Por qual Capability |
|---|---|---|
| DEP-EXE | KMS · GOV · GRW | estrategia ← conhecimento, governanca · comunicacao ← conhecimento · financeiro ← comercial |
| DEP-GOV | KMS | governanca ← conhecimento |
| DEP-QAR | GOV · KMS | qualidade, seguranca, juridico ← governanca · qualidade ← aprendizado |
| DEP-PRD | KMS · EXE | pesquisa ← conhecimento · produto ← estrategia |
| DEP-ENG | PRD · QAR · TLS · KMS · EXE | arquitetura ← produto · dados ← seguranca · IA ← integracao · eng-agentes ← conhecimento, aprendizado, comunicacao |
| DEP-OPS | ENG | infraestrutura ← arquitetura · operacoes ← engenharia |
| DEP-TLS | ENG · QAR | integracao ← arquitetura, seguranca |
| DEP-GRW | PRD · EXE · QAR | marketing ← produto, estrategia · comercial ← produto, juridico |
| **DEP-KMS** | **nenhuma** | `CAP-conhecimento` e a unica de nivel 0 (§4) |

### 10.3 Achados desta projecao

Divergencia constatada vira **achado**, nunca ajuste silencioso. Nenhuma Carta de Capability
foi alterada por esta projecao (PJ-03, PR-2 de ADR-0011).

| # | Achado | Severidade | Dono | Gatilho |
|---|---|---|---|---|
| **P1** | **22 de 23 Capabilities declaram `exercentes` identico ao `custodio`.** OW-02 e RM-05 — *"custodia nao e exclusividade de exercicio"* — tem **um unico membro observado** (`CAP-comunicacao`). A regra existe e quase nao e exercida; abstracao com menos de dois membros e suspeita (AQ-03) | **Media** | DEP-EXE + DEP-QAR | 1a revisao estrutural, ou 3a Carta de Departamento |
| **P2** | **Divergencia aparente na camada de memoria.** [FND-06 §2.1](../foundation/06-arquitetura-memoria.md) atribui dono por camada a **cinco** departamentos (EST→GOV, PRD→PRD, TEC→ENG, OPR→OPS, APR→KMS), enquanto `CAP-conhecimento` declara `exercentes: [DEP-KMS]` | **Media** | DEP-KMS *(custodio)* com DEP-GOV | ✅ **FECHADO** na 1a revisao estrutural — **ser dono de camada nao e exercer `CAP-conhecimento`**. Dono custodia **conteudo**; a Capability e **persistir e devolver o que se sabe**, e quem o faz e o **curador** (DEP-KMS). O catalogo estava correto; faltava a leitura escrita — [REV-ESTRUTURAL-I §3.6](../foundation/revisao-estrutural-01-2026-07-28.md) |
| **P3** | **Divergencia aparente nos portoes.** [FND-01 §6.2](../foundation/01-constituicao.md) atribui **QG-2** a DEP-ENG **+ DEP-GOV** e **QG-6** a DEP-QAR **+ DEP-GOV**, enquanto `CAP-qualidade` declara `exercentes: [DEP-QAR]` | **Media** | DEP-QAR *(custodio)* | ✅ **FECHADO** — **coliberar portao nao e exercer a Capability.** DEP-GOV libera pela **forma** (`CAP-governanca`); DEP-QAR, pelo **merito** (`CAP-qualidade`). Duas competencias, um portao — e o desenho que ADR-0005 protege |
| **P4** | **Divergencia aparente em seguranca.** [FND-02 §3](../foundation/02-estrutura-organizacional.md) da a DEP-TLS *"gestao de acesso e segredo (por referencia)"* e a DEP-OPS *"backups e sua verificacao"*, enquanto `CAP-seguranca` declara `exercentes: [DEP-QAR]` | **Media** | DEP-QAR *(custodio)* | ✅ **FECHADO** — **operar sob politica nao e custodiar a politica.** `CAP-seguranca` e definir e verificar; executar a rotina sob ela e `CAP-infraestrutura` e `CAP-operacoes`. FND-02 §3 diz *"por referencia"*, e a referencia e a politica de DEP-QAR |
| **P5** | **Divergencia aparente em comunicacao.** [FND-05 §Responsaveis](../foundation/05-framework-comunicacao.md) da a DEP-GOV a guarda do **formato**, enquanto `CAP-comunicacao` declara `exercentes: [DEP-EXE, DEP-KMS]` | **Baixa** | DEP-EXE *(custodio)* | ✅ **FECHADO** — **guardar a forma de um artefato e `CAP-governanca`**, nao `CAP-comunicacao`. Mesma distincao de P3, sobre outro objeto |
| **P6** | **VC-03 dispara em 2 de 9 departamentos antes da primeira Carta.** DEP-ENG vincula-se a **5** Capabilities e DEP-EXE a **4**; VC-03 fixa em **tres** o sinal de componente amplo demais, e manda avaliar a especializacao **do componente**, nao criar Capability | **Media** | DEP-EXE | 1a revisao estrutural, ou Carta de DEP-EXE |
| **P7** | **Assimetria de custodia.** DEP-GOV custodia **1** Capability, e ela verifica **todas as 22 demais** (§5) e e dependencia dura de **4**. O maior alcance de verificacao do catalogo esta no departamento de menor custodia | **Baixa** | DEP-GOV | 🔁 **RECLASSIFICADO na Missao 1.9.** A [Carta de DEP-GOV](../departments/gov/carta.md) o **avalia e decide manter**, com custo declarado (§12.1). **A contagem estava para menos:** sao **11** responsabilidades exclusivas, nao sete — quatro foram atribuidas por norma posterior a FND-02 §3. Achado **RC-04**; o sinal de **escopo heterogeneo** e **confirmado e agravado** |
| **P8** | **Duas duplas mutuamente expostas.** Em §10.2, **EXE ↔ GRW** e **ENG ↔ TLS** aparecem nos dois sentidos. **Nao e ciclo proibido:** PD-01 e RL-01 vedam ciclo em `depende-de` **entre Capabilities**, e o grafo de §4 permanece aciclico. E sinal de fronteira a vigiar, nao defeito | **Baixa** | DEP-EXE | 2a revisao estrutural |

> **As quatro fecharam pelo mesmo mecanismo, e isso e o achado.** Nenhuma era divergencia de
> **dado**: as quatro eram a **ausencia de uma distincao escrita** entre *deter a competencia* e
> *operar sob ela*. **Zero Cartas de Capability foram alteradas** — a correcao foi escrever a
> leitura, nao mudar a fonte (PJ-03, PR-2 de ADR-0011). Uma divergencia que se resolve **sem
> tocar a fonte** nunca foi divergencia da fonte.

> **P1, P6, P7 e P8 permanecem abertos.** P1 continua com **um** membro *(`CAP-comunicacao`)*;
> P6 e P7 tiveram o gatilho **disparado e confirmado** pela 1a revisao estrutural, e a
> resolucao de P7 depende da **Carta de DEP-GOV**; P8 tem gatilho na **2a** revisao. Fechar
> quatro nao fecha os outros quatro — [REV-ESTRUTURAL-I §5.2](../foundation/revisao-estrutural-01-2026-07-28.md).

> **Resultado negativo, declarado (PI-10).** A projecao **nao** encontrou: Capability sem
> custodio (OW-03), custodia dupla (OW-01), Capability de dominio `GAR` fora da Guarda
> (OW-05), Capability `nucleo` custodiada por departamento de Suporte (OW-04), nem
> departamento sem nenhuma custodia. Cinco verificacoes, cinco negativos — e isso e o
> resultado bom.

## 11. Documentos relacionados

| Referencia | Relacao |
|---|---|
| [FND-08](../foundation/08-capability-framework.md) | Framework que governa esta camada |
| [ADR-0002](../decisions/ADR-0002-adocao-da-camada-de-capabilities.md) | Decisao que adotou a camada e este catalogo |
| [ADR-0011](../decisions/ADR-0011-contrato-de-carta-de-departamento.md) | Contrato de Carta de Departamento; declara esta projecao como fonte unica do pivo por departamento |
| [RFC-0001](../rfcs/RFC-0001-camada-de-capabilities.md) | Proposta de origem |
| [Revisao arquitetural](revisao-arquitetural-2026-07-28.md) | Duplicacao, sobreposicao, lacuna e cobertura |
| [TPL-capability](../foundation/templates/TPL-capability.md) | Template da Carta |

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-EXE | Catalogo inicial: 23 Capabilities em 7 dominios, mapa de dependencias duras, relacoes de verificacao e coordenacao. Ratificado por ADR-0002. |
| 1.1.0 | 2026-07-28 | DEP-EXE | Emenda **MENOR** por **ADR-0011**: §10 acrescenta a **projecao Departamento × Capability** — custodia, exercicio, exposicao derivada e **oito achados**; §10 anterior *(Documentos relacionados)* passa a §11. Frontmatter passa a declarar os cinco campos do contrato de artefato e `projecao_de` (AC-08, ADR-0009). **Nenhuma Carta de Capability foi alterada** (PJ-03). |
| 1.3.0 | 2026-07-28 | DEP-EXE | Emenda **MENOR** pelo **rollout das Cartas**, Missao 1.9: §10.3 **reclassifica P7** — a Carta de DEP-GOV o avalia e decide manter, e a contagem de responsabilidades exclusivas sobe de **7** para **11** (achado **RC-04**). **Nenhuma Carta de Capability foi alterada** (PJ-03); nenhum `custodio`, `exercente` ou `depende_de` tocado. A projecao por departamento de §10.1 **permanece exata**: as nove Cartas a reproduzem sem divergencia. |
| 1.2.0 | 2026-07-28 | DEP-EXE | Emenda **MENOR** pela **Primeira Revisao Estrutural**: §10.3 registra o **fechamento de P2, P3, P4 e P5** — as quatro divergencias aparentes resolvidas pela distincao entre **deter a competencia** e **operar sob ela** —, e declara que P1, P6, P7 e P8 **permanecem abertos**. **Nenhuma Carta de Capability foi alterada** (PJ-03); nenhum `custodio`, `exercente` ou `depende_de` tocado. |
