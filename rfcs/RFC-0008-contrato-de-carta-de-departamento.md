---
id: RFC-0008-contrato-de-carta-de-departamento
titulo: Onde vive o contrato de Carta de Departamento, e como validá-lo sem criar camada nova
tipo: rfc
versao: 1.0.0
status: aprovado
camada_memoria: nao-aplicavel
autor: DEP-EXE
proprietario: DEP-EXE
aprovador: DEP-GOV
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: null
decisoes_relacionadas: [ADR-0001, ADR-0002, ADR-0003, ADR-0006, ADR-0009]
substitui: []
substituido_por: null
classe_mudanca: C2
prazo_analise: 2026-07-28
resumo: Pergunta onde deve viver o contrato de Carta de Departamento e propõe instituí-lo por ADR com emenda ao template, sem criar documento fundacional novo.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-GOV
ratificacao: nao-exigida
---

# RFC-0008: Contrato de Carta de Departamento

## Proposito
Responder onde deve viver o contrato que fixa o conteudo minimo e os limites de uma Carta
de Departamento, e como valida-lo antes de qualquer rollout — sem criar documento
fundacional novo nem camada conceitual nova.

## Escopo
| Item | Definicao |
|---|---|
| **Abrange** | O contrato documental da **Carta de Departamento** (tipo documental de FND-10 §4.3), as regras de desenho que o sustentam, a projecao Departamento × Capability e a instanciacao de **dois** pilotos de validacao. |
| **Nao abrange** | Criar departamento novo; alterar FND-02; alterar a matriz de autoridade de FND-09 §8.2; criar agente, subagente, skill, workflow, produto, projeto ou ferramenta; as sete Cartas restantes. |
| **Subordinado a** | [FND-01](../foundation/01-constituicao.md), [FND-02](../foundation/02-estrutura-organizacional.md), [FND-04](../foundation/04-governanca.md), [FND-08](../foundation/08-capability-framework.md), [FND-09](../foundation/09-meta-model.md), [FND-10](../foundation/10-artifact-framework.md). |

## Responsaveis
| Papel | Quem |
|---|---|
| Proponente | DEP-EXE |
| Areas que devem se manifestar | DEP-GOV *(forma e conformidade)* · DEP-QAR *(risco e segregacao)* · DEP-KMS *(memoria e custo de contexto)* |
| Aprovador | DEP-GOV valida a forma (FND-09 §8.2) |
| Prazo de manifestacao | 2026-07-28 |

---

## 1. Situacao atual

| Fato | Fonte |
|---|---|
| Os 9 departamentos existem e sao vinculantes desde ja, em 4 classes | [FND-02 §2.1 e §3](../foundation/02-estrutura-organizacional.md) |
| **Nenhum** tem Carta. FND-02 §3 declara que cada um "tera Carta completa em fase futura" | FND-02 §3 |
| Existe `TPL-carta-departamento` v1.0.0, com 13 secoes, criado por ADR-0001 | [TPL-carta-departamento](../foundation/templates/TPL-carta-departamento.md) |
| `Carta de Departamento` ja e tipo documental declarado, mapeado a entidade `DEP` | [FND-10 §4.3](../foundation/10-artifact-framework.md) |
| `DEP` ja tem atributos minimos, relacoes validas e perfil de ciclo declarados | [FND-09 §5.4, E-10](../foundation/09-meta-model.md) |
| A autoridade sobre `DEP` ja esta fixada: propoe DEP-EXE · revisa DEP-GOV · aprova e ratifica SOBERANO | FND-09 §8.2 |
| O catalogo de Capabilities declara `custodio` e `exercentes` por Capability | [capabilities/README §2](../capabilities/README.md) |
| **Nao existe** projecao que responda, por departamento, o que ele custodia e o que exerce | Varredura do acervo, 2026-07-28 |
| O template vigente **nao** exige distinguir custodia de exercicio, nem indicador medido de indicador definido, nem memoria autorizada, nem perfil de carregamento | TPL-carta-departamento v1.0.0, §§1–13 |

## 2. Problema

O template vigente basta para **produzir** uma Carta, mas nao basta para **julgar** se ela
esta correta. Cinco lacunas verificaveis:

| # | Lacuna | Consequencia se a Carta for escrita hoje |
|---|---|---|
| L1 | O template pede `capabilities` como lista unica | A Carta nao distingue **custodiar** de **exercer**, e OW-01/OW-02 ficam inverificaveis na instancia |
| L2 | O template nao exige declarar **impedimentos** | Um departamento de Guarda poderia aparecer aprovando ou verificando materia propria sem que a Carta o proibisse (PI-05, RM-06b) |
| L3 | O template pede "Criterio de sucesso" sem distinguir indicador **definido** de **medido** | Repetiria no nivel do departamento o defeito ja registrado no catalogo de Capabilities: **88 de 111 indicadores sem valor medido** (REV-CAP A6) |
| L4 | O template nao trata **memoria autorizada** nem politica de contexto | A Carta nasceria sem dizer o que o departamento pode escrever, e em que camada (FND-06 §3) |
| L5 | O template nao tem **resumo operacional** nem **perfil minimo de carregamento** | Decidir se a Carta e relevante exigiria abri-la — contra CE-01 e FND-10 §8.3 |

**Evidencia de que a lacuna e real, nao antecipada:** as cinco lacunas foram levantadas
percorrendo o proprio template contra FND-02, FND-06, FND-08, FND-09 e FND-10. Nenhuma
depende de instancia futura para ser constatada.

## 3. Pergunta de decisao

> **Onde deve viver o contrato de Carta de Departamento — e o que basta para valida-lo antes
> de aplicar as nove Cartas?**

## 4. Criterios de avaliacao

> Declarados antes de examinar as opcoes (CD-01, FND-07).

| # | Criterio | Peso | Como se mede |
|---|---|---|---|
| K1 | **Nao amplia o universo sem gatilho** | Alto | Numero de entidades, tipos documentais, camadas e documentos fundacionais criados. Meta: **0** |
| K2 | **Vigora nesta missao** | Alto | O instrumento entra em `ativo` sem depender de ato do Soberano que a missao nao pode produzir (LM-02, CV-09) |
| K3 | **Validado antes do rollout** | Alto | Numero de instancias reais testadas em cenario, antes das sete restantes |
| K4 | **Custo de contexto** | Medio | Linhas acrescidas ao acervo e ao pacote de quem escreve uma Carta, medidas (CE-02) |
| K5 | **Reversibilidade** | Medio | O que e preciso desfazer se o contrato se mostrar errado |

## 5. Opcoes

### Opcao A — Criar FND-11 "Department Framework"

| Campo | Conteudo |
|---|---|
| Descricao | Documento fundacional novo, no nivel 2 da hierarquia normativa, com o contrato completo. |
| A favor | Lugar obvio para quem procura; simetria com FND-08, FND-09 e FND-10. |
| Contra | **Zero instancias anteriores, zero consumidores, zero regimes concorrentes.** Repete exatamente o padrao que REV-SOBERANO §6.1 ja recusou para o contrato sobre o Soberano. |
| Custo / Risco | **C3 com ratificacao do Soberano.** Como esta missao nao ratifica, FND-11 nasceria `aprovado` e **nao entraria em vigor** — e as Cartas nasceriam sob norma sem eficacia. |
| Quem e afetado | FND-01 §10 *(hierarquia normativa)*, todos os documentos que a listam. |
| **K1** | Falha — cria documento fundacional sem gatilho. |
| **K2** | **Falha** — nao vigora nesta missao. |

### Opcao B — Instituir o contrato por ADR e materializa-lo no template vigente

| Campo | Conteudo |
|---|---|
| Descricao | Um ADR institui o contrato — blocos obrigatorios, limites e **dez regras de desenho** — e emenda `TPL-carta-departamento` para materializa-lo. A projecao Departamento × Capability entra no catalogo de Capabilities. Dois pilotos validam o contrato em cenarios antes de qualquer rollout. |
| A favor | Reusa o **precedente exato** de [ADR-0010](../decisions/ADR-0010-contrato-de-conhecimento-do-soberano.md): contrato em ADR, instancia em artefato proprio, nenhum documento fundacional criado. Nao toca a hierarquia normativa. |
| Contra | O contrato fica em **M1** (imutavel): evoluir exige superar o ADR, nao versiona-lo. |
| Custo / Risco | **C2 / Tipo 2.** Reversao documental integral (§8). Risco: o contrato so tera dois exercicios reais antes do rollout. |
| Quem e afetado | `TPL-carta-departamento` *(MENOR)* · `capabilities/README` *(MENOR)* · catalogo mestre · indices. |
| **K1** | **Passa** — 0 entidades, 0 tipos documentais, 0 camadas, 0 documentos fundacionais. |
| **K2** | **Passa** — ADR C2/Tipo 2 entra em `ativo` sem ratificacao (FND-10 §10.3). |
| **K3** | **Passa** — dois pilotos de classes distintas, testados em seis cenarios. |

### Opcao C — Emendar o template sem ADR

| Campo | Conteudo |
|---|---|
| Descricao | Levar o contrato inteiro para dentro do template, sem instrumento decisorio. |
| A favor | O menor acrescimo possivel ao acervo. |
| Contra | **Template vincula a forma, nunca o conteudo** (FND-09 §5.4, E-16). Regras de desenho — custodia unica, impedimento, indicador medido — sao **conteudo normativo**, e template nao e o lugar delas. Alem disso, alterar template e C2 e **exige ADR** (FND-04 §6). |
| Custo / Risco | Cria regra normativa em artefato sem autoridade para carrega-la; a rastreabilidade da regra ficaria sem origem (LN-07). |
| **K1** | Passa. |
| **K2** | Passa. |
| **K3** | Falha — sem instrumento, nao ha registro de alternativas, reversao nem gatilho de reavaliacao. |

### Opcao Z — Nao fazer nada

| Campo | Conteudo |
|---|---|
| Consequencia de manter o estado atual | As nove Cartas seriam escritas sob um template que nao verifica L1 a L5. O primeiro defeito apareceria **depois** de nove instancias — nove correcoes, nao uma. |
| Custo da inacao | OB-H2.1 *("cada departamento com Carta aprovada e escopo nao sobreposto")* fica bloqueado sem criterio de aceite. A pergunta "esta Carta esta correta?" continua sem resposta verificavel. |

## 6. Recomendacao do proponente

**Opcao B.** E a unica que passa em K1, K2 e K3 simultaneamente. A Opcao A falha no criterio
que a missao mais protege — nao criar camada sem gatilho — e falharia tambem em vigencia. A
Opcao C produz norma em artefato sem autoridade normativa.

**Ajuste recomendado a Opcao B:** os pilotos **nao** sao promovidos a `aprovado` nesta
missao. A autoridade de aprovar Carta de Departamento e do **SOBERANO** (FND-09 §8.2,
FND-10 §10.3); declara-los `aprovado` sem ato explicito e datado seria repetir a causa de
[INC-2026-001](../governance/incidents/INC-2026-001-ratificacao-inferida.md). Os pilotos
permanecem em `em-revisao`, com revisao independente concluida e registrada.

## 7. Impacto previsto

| Dimensao | Impacto |
|---|---|
| Departamentos | DEP-EXE *(autor das Cartas)* · DEP-GOV *(revisor, guardiao do template)* · DEP-QAR *(objeto de um piloto; executor do Fitness Check)* · DEP-ENG *(objeto do outro piloto)* · DEP-KMS *(medicao de contexto e memoria)* |
| Componentes | **Duas** Cartas de Departamento, em `em-revisao`. Nenhum agente, skill, workflow, produto, projeto ou ferramenta |
| Normas afetadas | Nenhuma norma alterada. `TPL-carta-departamento` e `capabilities/README` recebem emenda MENOR |
| Camadas de memoria | APR — registro de aprendizado da missao (QG-5) |
| Ganho PI-14 pretendido e sinal que o comprova | **Organizacao:** a pergunta "esta Carta esta correta?" passa de julgamento a lista verificavel — sinal medido nos dois pilotos, em §12 do ADR. **Reducao de contexto:** o perfil minimo de carregamento da Carta e medido em linhas, nao estimado |

## 8. Riscos

| # | Risco | Impacto | Mitigacao |
|---|---|---|---|
| RS1 | Dez regras novas com pouco exercicio real — o padrao ja registrado em R1 de FIT-2026-002 e R1 de FIT-2026-004 | Alto | Medir, no Fitness Check, **quantas das dez** foram exercidas pelos dois pilotos, e declarar as que nao foram |
| RS2 | Dois pilotos podem nao cobrir o espaco das quatro classes | Medio | Amostra por **contraste declarado**: uma Guarda e uma Linha; Comando e Plataforma ficam sem cobertura, e isso e declarado como limite, nao omitido |
| RS3 | O contrato ficar em M1 e envelhecer sem via de emenda barata | Medio | Gatilho de reavaliacao declarado no ADR §12: **terceira Carta escrita** |
| RS4 | A projecao Departamento × Capability virar segunda fonte da custodia | Alto | Declarar projecao com as quatro informacoes de PJ-02; fonte permanece o frontmatter das 23 Cartas de Capability (PJ-03) |

## 9. Perguntas em aberto

| # | Pergunta | Encaminhamento |
|---|---|---|
| Q1 | `departments/<dep>/` — `<dep>` e o codigo em minusculas (`qar`) ou o ID completo (`dep-qar`)? | FND-03 §7 nao desambigua. Adota-se o codigo em minusculas, por LX-01 e pelo padrao `AGT-<DEP>-<papel>` em `departments/<dep>/agents/`. **Registrado como achado**, dono DEP-GOV |
| Q2 | Um departamento pode exercer Capability que nao custodia? | **Sim** (OW-02, RM-05). O catalogo declara isso em **1 de 23** casos; a divergencia e achado da projecao, nao ajuste |
| Q3 | O contrato deve alcancar tambem Carta de Agente? | **Nao nesta RFC.** Nenhum agente existe; alcancar dois tipos com um exercicio seria antecipacao (FND-08 §7.1) |

## 10. Manifestacoes

| Area | Posicao | Fundamento | Data |
|---|---|---|---|
| DEP-GOV | **Apoia** | Opcao B nao toca hierarquia normativa nem cria tipo; a emenda ao template e C2 com ADR, como FND-04 §6 exige | 2026-07-28 |
| DEP-QAR | **Apoia com ressalva** | Apoia o contrato; ressalva RS1 — exige que o Fitness Check meca o exercicio das dez regras, e nao apenas as declare | 2026-07-28 |
| DEP-KMS | **Apoia** | O perfil minimo de carregamento e medido em linhas, coerente com CE-02 e CE-04 | 2026-07-28 |

## 11. Resultado

| Campo | Conteudo |
|---|---|
| Decisao | **Aceita com ajuste** — os pilotos permanecem em `em-revisao` (§6) |
| ADR gerado | [ADR-0011](../decisions/ADR-0011-contrato-de-carta-de-departamento.md) |
| Se rejeitada, por que | — |
| Se adiada, ate quando | — |
| Data | 2026-07-28 |
| Responsavel | DEP-EXE *(proposta)* · DEP-GOV *(validacao de forma)* |
