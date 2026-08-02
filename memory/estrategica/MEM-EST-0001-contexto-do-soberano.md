---
id: MEM-EST-0001-contexto-do-soberano
titulo: Contexto do Soberano — conhecimento operacional comprovado sobre quem dirige o LucaX Enterprise OS
tipo: memoria
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-KMS
proprietario: DEP-GOV
aprovador: DEP-GOV
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0010]
substitui: []
substituido_por: null
origem: ADR-0010
evidencia: Dez fontes nomeadas em §8; nenhuma afirmacao sem fonte, data e contexto declarados
confianca: media
ocorrencias: 1
ttl: permanente
aplica_se_a: [global]
resumo: Registra o que se sabe, com prova, sobre visao, criterios, linguagem e forma de trabalho do Soberano — e o que nao se sabe.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: ratificada
---

# Contexto do Soberano

> **Este registro nao obriga.** Ele orienta escolhas **apenas onde a norma admite escolha**, e
> cede diante da Constituicao, da Governanca, de ADR vigente, de evidencia verificavel e de
> seguranca (CT-01). A subordinacao nao e uma promessa deste texto: decorre de `MEM` ter
> autoridade normativa **nenhuma** ([FND-09 §5.7](../../foundation/09-meta-model.md), E-20;
> MM-07).

> **Estado `aprovado`, nao `ativo`.** A entrada em vigor aguarda ato explicito e datado do
> Soberano sobre este texto — **CT-28** de [ADR-0010 §5.8](../../decisions/ADR-0010-contrato-de-conhecimento-do-soberano.md).
> Artefato `aprovado` **pode ser referenciado** (FND-03 §5).

## Proposito

Registrar o que se sabe **com prova** sobre visao, criterios, linguagem e forma de trabalho do
Soberano, para que estruturas futuras nao precisem inferi-los — e registrar, com o mesmo rigor,
o que **nao** se sabe.

## Escopo

| Item | Definicao |
|---|---|
| **Aplica-se a** | Qualquer papel, no momento e na medida do pacote de contexto aplicavel (§9) |
| **Nao** se aplica a | Decisao ja registrada — fonte e o ADR (CT-05); norma — fonte e a Fundacao; estado corrente de missao — vive em OPR e expira (CT-25) |
| Camada e por que esta camada | **EST.** [FND-06 §3.1](../../foundation/06-arquitetura-memoria.md) ja declara como conteudo desta camada *"restricoes permanentes impostas pelo Soberano"* e *"padroes duraveis de preferencia do Soberano sobre como o trabalho e feito"* — desde a v1.0.0, antes deste registro existir |
| **Nao contem** | Nenhum item da lista fechada de **CT-15**: credencial, dado biometrico, medico, financeiro pessoal, documento, endereco, contato, dado sobre terceiros, detalhe de vida privada, avaliacao psicologica ou juizo sobre carater |

## Responsaveis

| Papel | Quem |
|---|---|
| Dono da camada | **DEP-GOV** |
| Curador | **DEP-KMS** |
| Verificacao independente | **DEP-QAR** — classe, sensibilidade e conformidade a CT-15 |
| **Unica autoridade que confirma o conteudo** | **SOBERANO** — nenhum papel confirma no lugar dele (PI-01, CT-08) |
| Leitura obrigatoria por | Ninguem por padrao. Carregamento integral e **proibido** (CT-22, CE-01) |

---

## Conteudo

**Legenda das colunas.** `Classe`: `stated` declarado · `observed` constatado em atos
registrados · `inferred` hipotese, **nao orienta** · `unknown` sem evidencia.
`Sens.`: escala unica de `confidencialidade` (CT-14). `Fonte`: ID de §8.
Cada afirmacao declara as oito informacoes de **CT-06**.

### 1. Identidade e autoridade — pacote **P1**

| # | Afirmacao | Classe · Confianca | Sens. | Fonte · Data | Contexto | Validade · Gatilho de revisao |
|---|---|---|---|---|---|---|
| **AF-01** | O Soberano do LucaX Enterprise OS e **Lucas**, humano, autoridade final e **indelegavel** | `stated` · alta | interno | **F1** · 2026-07-28 | Constituicao, cuja adocao o proprio Soberano ratificou por ato de 2026-07-28 | permanente · Emenda C3 de FND-01 §11 |
| **AF-02** | Ele **se designa "Fundador"**; o termo oficial do sistema e `SOBERANO`, e os dois designam a mesma autoridade | `stated` · alta | interno | **F2** · 2026-07-28 | O unico ato soberano registrado abre com *"ATO SOBERANO DO FUNDADOR"*. Equivalencia ja resolvida em INC-2026-001 §7.1 e FND-10 §3.3 — aqui apenas referenciada | permanente · Emenda C3 que altere o termo oficial |
| **AF-03** | Exerce autoridade por **ato escrito, explicito e datado**, emitido diretamente ao sistema | `stated` · alta | interno | **F2** · 2026-07-28 | Forma declarada no proprio ato. **Uma** ocorrencia registrada ate hoje — forma atestada, nao serie | 2027-01-28 · **Segundo** ato soberano registrado |
| **AF-04** | Opera por **missoes numeradas**, cada uma aberta por determinacao propria | `observed` · media | interno | **F5**, **F9**, FIT-2026-003 · 2026-07-28 | Tres missoes nomeadas no acervo (1.3, 1.4, 1.5). O **texto integral** de apenas uma — a 1.5 — e diretamente observavel; as demais sao citadas por terceiros | 2027-01-28 · Missao 1.6 |
| **AF-05** | O papel que ele reservou para si na operacao e **definidor de direcao, arbitro de tradeoffs e juiz final de qualidade** — nao executor de producao | `stated` · alta | interno | **F1** *(FND-01 §2, ratificada)* · 2026-07-28 | Visao V1–V4. Texto **nao reproduzido** aqui: a fonte e FND-01 §2 (CT-05, PJ-01) | permanente · Emenda de FND-01 §2 |
| **AF-06** | Existe um sistema preexistente, `LucaX Legacy`, **externo** a este repositorio. **Se ele o construiu, quando, com quem ou por que: nao se sabe** | `unknown` | interno | **F8** · 2026-07-28 | ADR-0007 §5.1 declara a existencia e a externalidade do sistema; **nada** no acervo atribui autoria, data ou motivo. Consultar o Legacy para descobrir esta expressamente vedado nesta missao | permanente · Primeiro candidato submetido ao portao de ADR-0007 §5.3 |
| **AF-07** | **Trajetoria profissional, formacao, experiencia anterior e contexto de mercado: nao se sabe** | `unknown` | interno | — | Nenhuma fonte do acervo, e nenhuma declaracao do Soberano, trata do assunto. **Nao se preenche por inferencia** (CT-07) | permanente · Primeira declaracao do Soberano sobre o tema |

### 2. Visao, objetivos e horizontes — pacote **P2**

| # | Afirmacao | Classe · Confianca | Sens. | Fonte · Data | Contexto | Validade · Gatilho de revisao |
|---|---|---|---|---|---|---|
| **AF-08** | A visao que ele ratificou e operar uma empresa digital **completa** — da intencao a operacao — como sistema de agentes governado por **um unico humano soberano** | `stated` · alta | interno | **F1** *(FND-01 §1 e §2)* · 2026-07-28 | Missao e visao da Constituicao. Enunciados **nao reproduzidos**: fonte unica em FND-01 (CT-05) | permanente · Emenda C3 de FND-01 §1 ou §2 |
| **AF-09** | Os objetivos estao ordenados em **tres horizontes de precedencia, nao de calendario**; H2 nao comeca antes de H1 estar estruturalmente pronto | `stated` · alta | interno | **F1** *(FND-01 §5)* · 2026-07-28 | Estrutura de OB-H1 a OB-H3. **Horizonte corrente: H1** | permanente · Criterio de conclusao de H1 satisfeito |
| **AF-10** | Determinacao originaria: *"Os documentos produzidos passarao a ser a unica fonte oficial de verdade para as proximas fases da transformacao"* | `stated` · alta | interno | **F4** *(ADR-0001)* · 2026-07-28 | Citacao literal registrada em INC-2026-001 §1. **Atencao:** esta determinacao e **anterior** aos documentos e, por si, **nao ratifica** nada (LM-03) — vale como declaracao de intencao, nao como ato | permanente · Superacao de ADR-0001 |
| **AF-11** | **Objetivos pessoais, comerciais, financeiros ou de mercado alem dos ratificados: nao se sabe** | `unknown` | interno | — | O acervo registra apenas objetivos **organizacionais**. Objetivo pessoal ou financeiro so entraria com necessidade operacional, consentimento e acesso formal (CT-15 item 7) | permanente · Declaracao explicita do Soberano |

### 3. Principios, padrao de qualidade e modelo de decisao — pacote **P2**

| # | Afirmacao | Classe · Confianca | Sens. | Fonte · Data | Contexto | Validade · Gatilho de revisao |
|---|---|---|---|---|---|---|
| **AF-12** | O padrao de qualidade que ele ratificou e a **Definicao de Pronto de nove criterios** e os **sete portoes** de FND-01 §6 | `stated` · alta | interno | **F1** · 2026-07-28 | Referencia, nao reproducao (CT-05, PJ-01). Consultar FND-01 §6 | permanente · Emenda de FND-01 §6 |
| **AF-13** | A **ordem de trade-offs** que ele ratificou e a lista de valores de FND-01 §3: vence o de **numero menor**, e `VL-01` soberania humana vence todos | `stated` · alta | interno | **F1** · 2026-07-28 | E o unico criterio de desempate declarado do sistema. Referencia, nao reproducao | permanente · Emenda C3 de FND-01 §3 |
| **AF-14** | **Qualidade antes de custo**: o criterio primario e o resultado para a tarefa; custo e restricao declarada, nunca criterio dominante | `stated` · alta | interno | **F1** *(PI-11)* **e F10** · 2026-07-28 | **Duas ocorrencias independentes** — uma dentro do acervo ratificado, outra em instrucao permanente fora dele, esta ultima aplicada a habilitacao de ferramenta. Coincidencia entre fontes independentes e o sinal mais forte deste registro | 2027-01-28 · Ato do Soberano que altere a instrucao permanente |
| **AF-15** | **Ato explicito acima de inferencia**: instrucao generica anterior, precedente e silencio nao valem como autorizacao | `stated` · alta | interno | **F3**, **F2**, **F9** · 2026-07-28 | **Tres ocorrencias**: a determinacao que abriu a Missao 1.3 *("ratificacao C3/Tipo 1 nao pode ser inferida de instrucao generica")*; o ato de 2026-07-28, que determina registro em fonte canonica; e a Missao 1.5, que manda *consumir apenas ato soberano explicito e separado* | permanente · Primeira ocorrencia em que o Soberano dispense ato explicito |
| **AF-16** | **Historico nao se reescreve**: registro ja emitido e preservado, e a correcao vem por superacao, nao por edicao | `stated` · alta | interno | **F2**, **F9** · 2026-07-28 | **Duas ocorrencias**: o ato determina *"sem edicao retroativa dos ADRs historicos"*; a Missao 1.5 determina nao editar nem recalcular a baseline historica. Convergente com LV-04 e CC-01, que sao norma — aqui registra-se a **preferencia**, nao a norma | permanente · Primeira determinacao em contrario |
| **AF-17** | **Verificacao independente antes de encerrar**: encerramento depende de quem nao produziu | `stated` · alta | interno | **F2**, **F7**, **F9** · 2026-07-28 | O ato autoriza fechar INC-2026-001 *"apos verificacao independente"*; a revisao arquitetural ocorreu **por determinacao dele em cada missao**; a Missao 1.5 exige revisao independente e Fitness Check na conclusao | permanente · Primeira dispensa de verificacao independente |
| **AF-18** | **Nenhum componente sem vinculo a Capability** | `stated` · alta | interno | **F4** *(ADR-0002)* · 2026-07-28 | Citacao literal em INC-2026-001 §1. Hoje e **norma** (VC-01); registra-se aqui a **origem soberana** do criterio, nao a regra | permanente · Superacao de ADR-0002 |
| **AF-19** | **Nenhum framework introduz entidade estrutural sem obedecer ao Meta Model** | `stated` · alta | interno | **F4** *(ADR-0003)* · 2026-07-28 | Citacao literal em INC-2026-001 §1. Norma correspondente: MT-01 | permanente · Superacao de ADR-0003 |
| **AF-20** | **Toda missao encerra com verificacao de saude da arquitetura**, alem da revisao arquitetural | `stated` · alta | interno | **F4** *(ADR-0004)*, **F6** · 2026-07-28 | Citacao literal em INC-2026-001 §1; FND-09 §10 registra que o **mecanismo** foi determinado por ele. Note-se que ele pediu **as duas** verificacoes, nao uma | permanente · Primeira missao encerrada sem uma das duas |
| **AF-21** | **O significado de "premium" e de "padrao ouro" como criterio de qualidade: nao se sabe** | `unknown` | interno | **F9** *(uso atestado)* · 2026-07-28 | A Missao 1.5 nomeia os dois termos como vocabulario a registrar — o que **atesta o uso** —, mas **nenhuma fonte os define**. Varredura no acervo: **zero** ocorrencias. Definir por analogia com DoD ou com PI-11 seria inferencia disfarcada de fato (CT-07, LV-12) | permanente · **Primeira definicao declarada pelo Soberano** |

### 4. Preferencias de dominio — pacote **P3**, por subsecao

#### 4.1 Estilo de trabalho e comunicacao

| # | Afirmacao | Classe · Confianca | Sens. | Fonte · Data | Contexto | Validade · Gatilho de revisao |
|---|---|---|---|---|---|---|
| **AF-22** | **Entrega pronta.** Espera a solucao final, pronta para uso; se um passo ficar bloqueado e exigir verificacao posterior, **quem executa verifica** antes de reportar, em vez de devolver a checagem a ele | `stated` · alta | interno | **F10** · 2026-07-28 | Instrucao permanente ao ambiente de execucao. **Fonte externa ao acervo** — nivel 8 de FND-01 §10 (CT-11) | 2027-01-28 · Ato do Soberano que altere a instrucao |
| **AF-23** | **Regra propria contradita:** quando um pedido esbarra em norma vigente do proprio sistema, espera que se **aponte a regra exata** e se exponha o tradeoff. **Proibido obedecer em silencio; igualmente proibido recusar em silencio** | `stated` · alta | interno | **F10 e F1** *(PI-13)* · 2026-07-28 | **Duas ocorrencias independentes** — instrucao permanente e principio imutavel ratificado, com formulacao praticamente identica | permanente · Emenda C3 de PI-13 |
| **AF-24** | A determinacao de missao que ele emite e **estruturada**: missao, pre-correcoes, fontes, entregaveis, restricoes e criterios de conclusao | `observed` · media | interno | **F9** · 2026-07-28 | Observado **integralmente uma vez** (Missao 1.5). Missoes 1.3 e 1.4 sao citadas por terceiros, sem texto disponivel — logo a regularidade **nao esta comprovada** | 2027-01-28 · Missao 1.6 — segunda observacao direta forma serie |
| **AF-25** | Encaminhar um plano a refinamento externo **nao e rejeicao do conteudo**: espera confirmacao do encaminhamento e continuidade de outras frentes em paralelo | `stated` · media | interno | **F10** · 2026-07-28 | Fonte unica e externa ao acervo (CT-11). Confianca media por **uma** ocorrencia, sem corroboracao interna | 2027-01-28 · Segunda ocorrencia, ou ato que altere a instrucao |
| **AF-26** | **Preferencias de idioma, tom, extensao e formato de relatorio alem do que FND-05 normatiza: nao se sabe** | `unknown` | interno | — | O acervo e integralmente em portugues do Brasil por forca de **LX-05**, que e norma — nao evidencia de preferencia pessoal. Nao se deduz preferencia a partir de conformidade a norma | permanente · Declaracao explicita |

#### 4.2 Preferencias tecnicas

| # | Afirmacao | Classe · Confianca | Sens. | Fonte · Data | Contexto | Validade · Gatilho de revisao |
|---|---|---|---|---|---|---|
| **AF-27** | O **shell do Soberano e PowerShell**. Comando destinado a ele usa sintaxe PowerShell, ainda que a ferramenta interna execute outro interpretador | `stated` · alta | interno | **F10** · 2026-07-28 | Instrucao permanente, fonte externa (CT-11). Fato de ambiente, nao dado pessoal | 2027-01-28 · Ato que altere a instrucao |
| **AF-28** | **Ferramenta externa habilita-se por qualidade de resultado**, nao por limiar de volume ou economia | `stated` · alta | interno | **F10** · 2026-07-28 | Instrucao permanente sobre habilitacao de MCP. Converge com **PI-11** (AF-14), o que eleva a confianca | 2027-01-28 · Ato que altere a instrucao |
| **AF-29** | **Preferencias de linguagem, framework, nuvem, banco de dados ou modelo de IA: nao se sabe** | `unknown` | interno | — | Nenhum codigo, infraestrutura ou ferramenta existe no sistema — nao ha o que observar. Deduzir de AF-27 seria inferencia | permanente · Primeira Ficha de Ferramenta ou primeira decisao tecnica registrada |

#### 4.3 Preferencias de produto e design

| # | Afirmacao | Classe · Confianca | Sens. | Fonte · Data | Contexto | Validade · Gatilho de revisao |
|---|---|---|---|---|---|---|
| **AF-30** | **Preferencias de produto — publico, proposta de valor, escopo negativo, modelo de negocio: nao se sabe** | `unknown` | interno | — | Nenhum produto foi criado, por determinacao. A camada PRD tem **zero** registros | permanente · Primeira Carta de Produto |
| **AF-31** | **Preferencias de design — linguagem visual, interacao, acessibilidade, tom de interface: nao se sabe** | `unknown` | interno | — | `CAP-design` existe como competencia; **nenhuma** manifestacao do Soberano sobre design consta do acervo | permanente · Primeira manifestacao sobre design |

#### 4.4 Vocabulario

| # | Afirmacao | Classe · Confianca | Sens. | Fonte · Data | Contexto | Validade · Gatilho de revisao |
|---|---|---|---|---|---|---|
| **AF-32** | Usa **"Mission" / "Missao"** para designar o que a Governanca chama de **mudanca C2/C3** | `stated` · alta | interno | **F9**, **F4** *(ADR-0004)* · 2026-07-28 | Equivalencia ja resolvida em FND-09 §5.8 (X-13) e FND-10 §3.3 — aqui referenciada, nao redefinida | permanente · Emenda que altere X-13 |
| **AF-33** | Usa **"Ultraplan"** para o encaminhamento de um plano a refinamento externo | `stated` · media | interno | **F10** · 2026-07-28 | Termo de uso proprio, fonte externa e unica. **Nao** e termo oficial: nao consta de FND-03 §8 e nao designa entidade | 2027-01-28 · Segunda ocorrencia, ou uso em documento normativo |
| **AF-34** | **Vocabulario proprio alem de "Fundador" (AF-02), "Missao" (AF-32), "Ultraplan" (AF-33) e "premium"/"padrao ouro" (AF-21): nao se sabe** | `unknown` | interno | — | Varredura do acervo por termos nao oficiais atribuiveis a ele: nada alem dos quatro | permanente · Primeiro termo novo observado em determinacao |

#### 4.5 Tolerancia a risco, ritmo e autonomia

| # | Afirmacao | Classe · Confianca | Sens. | Fonte · Data | Contexto | Validade · Gatilho de revisao |
|---|---|---|---|---|---|---|
| **AF-35** | **Backup antes do risco.** Nenhuma sobrescrita, exclusao, migracao ou exposicao de dado vivo sem copia datada. *"Sem copia, nao roda."* | `stated` · alta | interno | **F10 e F1** *(PI-07, LV-01)* · 2026-07-28 | **Duas ocorrencias independentes**, com a mesma formulacao categorica dentro e fora do acervo. Tolerancia a risco irreversivel: **baixa e declarada** | permanente · Emenda C3 de PI-07 |
| **AF-36** | Mudanca **irreversivel** exige ato humano explicito, e a duvida sobre a classificacao resolve-se **pela mais restritiva** | `stated` · alta | interno | **F1** *(PI-06, FND-01 §7.1)* · 2026-07-28 | Referencia, nao reproducao. Consistente com AF-15 e AF-35 | permanente · Emenda C3 de PI-06 |
| **AF-37** | **Ritmo e cadencia de trabalho esperados: nao se sabe** — e **nao sao mensuraveis a partir do acervo** | `unknown` | interno | — | **Limite declarado (PI-10):** os 93 artefatos anteriores carregam **a mesma data**, 2026-07-28. Isso impede separar cadencia de intensidade: nao se sabe se cinco missoes ocorreram em um dia, em uma semana ou em meses. Qualquer numero aqui seria fabricado (LV-12, CE-04) | permanente · Primeira data distinta no acervo |
| **AF-38** | **Nivel de autonomia que ele atribuira a papeis executores: nao se sabe** | `unknown` | interno | — | A escala A0–A3 existe em FND-01 §7.2, mas **nenhuma Carta foi criada** e nenhum nivel foi atribuido. AF-22 informa como ele quer que o trabalho seja **entregue**, nao que autonomia formal concedera | permanente · Primeira Carta de agente ou departamento |

### 5. Lacunas declaradas

**Onze das 45 afirmacoes deste registro sao `unknown`** — AF-06, AF-07, AF-11, AF-21, AF-26,
AF-29, AF-30, AF-31, AF-34, AF-37 e AF-38. As outras 34 tem fonte, data e contexto declarados.

| # | Regra |
|---|---|
| L-1 | A lacuna vive **na secao do seu dominio**, nao em lista separada: quem carrega o pacote P3 de um dominio precisa ver o que **nao** se sabe sobre ele. Consolidar em outro lugar criaria segunda fonte (MM-01) |
| L-2 | **Nenhuma lacuna e preenchida por inferencia, plausibilidade ou analogia** (CT-07). Preencher e **LV-12** |
| L-3 | Lacuna **nao** e defeito deste registro: e o resultado correto de aplicar CT-07 a um acervo que documenta uma organizacao, nao uma pessoa |
| L-4 | Cada lacuna carrega **gatilho proprio** — o evento que a tornaria preenchivel. Lacuna sem gatilho seria observacao sem destino (FND-04 §8) |

> **Nao ha nenhuma afirmacao de classe `inferred` neste registro.** Onde faltou evidencia,
> registrou-se `unknown` — nunca hipotese. Se uma vier a ser registrada, ela **nao orienta** e
> expira sem confirmacao explicita do Soberano (CT-08).

### 6. Como este registro muda

| Movimento | Regra aplicavel |
|---|---|
| Captura, validacao, revisao, conflito, substituicao, expiracao e retirada | [ADR-0010 §5.6](../../decisions/ADR-0010-contrato-de-conhecimento-do-soberano.md) — **fonte**, nao reproduzida aqui |
| Correcao | Substituicao, nunca apagamento (CT-10, MM-09). A afirmacao anterior vai a `superado`, apontando para a que a substituiu |
| Retirada pelo Soberano | Sem necessidade de motivar (CT-19). Afirmacoes de **fonte externa** — F9 e F10 — sao as candidatas preferenciais |
| Divisao em novos artefatos | Exige **≥ 2 sinais observados** (CT-26, SE-02). Hoje ha **zero** |

### 7. Limites, recusas e consulta obrigatoria — pacote **P1**

> **Recusa duravel, nao restricao de missao.** Restricao valida para **uma** missao e estado
> temporario e vive na propria missao, nunca aqui (CT-25). O que segue atravessou mais de uma
> ocorrencia, ou foi declarado sem prazo.

| # | Afirmacao | Classe · Confianca | Sens. | Fonte · Data | Contexto | Validade · Gatilho de revisao |
|---|---|---|---|---|---|---|
| **AF-39** | **Recusa credencial em texto puro** — chave, token ou senha nao sao usados, executados ou manuseados **mesmo se ele proprio insistir**. A conduta esperada e orientar revogacao, rotacao e uso de variavel de ambiente | `stated` · alta | interno | **F10 e F1** *(PI-08, LV-02)* · 2026-07-28 | **Duas ocorrencias independentes.** A instrucao permanente e notavel por **antecipar a propria insistencia futura** — o Soberano se vincula contra si. Coerente com FND-01 §8.3, que veda excecao a LV-02 | permanente · Emenda C3 de PI-08 |
| **AF-40** | **Recusa autoridade construida por inferencia** — instrucao generica anterior, precedente ou silencio nao autorizam | `stated` · alta | interno | **F3**, **F9** · 2026-07-28 | Ver AF-15. Registrado tambem aqui como **recusa** porque e o unico caso em que o Soberano abriu incidente contra o efeito de uma pratica ja consolidada no proprio acervo | permanente · Primeira dispensa em contrario |
| **AF-41** | **Recusa abstracao sem gatilho observado** — caso concreto registrado: nao criar ontologia formal enquanto nao houver sinal | `stated` · alta | interno | **F5** · 2026-07-28 | Determinacao da Missao 1.3, registrada como evidencia E7 de ADR-0006. Convergente com SE-01 e FND-08 §7.1, que sao norma | permanente · Disparo de G1, G2 ou G3 de FND-10 §3.4 |
| **AF-42** | **Recusa criar componente de execucao antes de a fundacao estar pronta** — nenhum agente, subagente, skill, comando, workflow, produto, projeto ou ferramenta | `observed` · alta | interno | **F9**, `README.md`, REV-CONSOLIDACAO §1.1 · 2026-07-28 | Constatado ao longo de **todas** as missoes ate hoje, e verificado independentemente na Missao 1.4. Confianca alta por repeticao verificada, ainda que a formulacao literal do Soberano so conste da Missao 1.5 | 2027-01-28 · Criacao do primeiro componente — a recusa termina por evento, nao por prazo |
| **AF-43** | **Recusa clone, persona, perfil psicologico ou diagnostico** do proprio Soberano | `stated` · alta | interno | **F9** · 2026-07-28 | Determinacao expressa da Missao 1.5. Materializada como proibicao permanente em **CT-15 item 8**, que e norma — aqui registra-se a origem soberana | permanente · Ato do Soberano em contrario |
| **AF-44** | **Recusa preencher lacuna de conhecimento por inferencia** — sem evidencia, registra-se "desconhecido" | `stated` · alta | interno | **F9** · 2026-07-28 | Determinacao expressa da Missao 1.5, aplicada a este proprio registro. Convergente com **LV-12** e **PI-10** | permanente · Ato do Soberano em contrario |
| **AF-45** | **Situacoes que exigem consulta a ele** | `stated` · alta | interno | **F1**, **F10** · 2026-07-28 | Quatro, todas por **referencia** e nenhuma reproduzida: **(a)** pedido que esbarra em norma vigente — apontar a regra e perguntar o tradeoff (AF-23); **(b)** materias em que FND-01 §7.3 o nomeia como decisor ou ratificador; **(c)** mudanca **Tipo 1**, qualquer que seja a classe (PI-06); **(d)** exposicao de dado do Soberano ou de terceiros a servico externo (LV-08) | permanente · Emenda de FND-01 §7.3 |

## 8. Proveniencia das fontes

| Fonte | O que e | Interna ao acervo? | Posicao na hierarquia de FND-01 §10 |
|---|---|---|---|
| **F1** | [FND-01](../../foundation/01-constituicao.md), Constituicao — adotada por ADR-0001, **ratificada** pelo Soberano | **Sim** | Nivel 1 |
| **F2** | [INC-2026-001 §11.1](../../governance/incidents/INC-2026-001-ratificacao-inferida.md) — texto integral do **ato soberano** de 2026-07-28 | **Sim** | Registro do ato de autoridade maxima |
| **F3** | [INC-2026-001 §10](../../governance/incidents/INC-2026-001-ratificacao-inferida.md) — determinacao de abertura da **Missao 1.3**, citada literalmente | **Sim** | Registro de determinacao |
| **F4** | [INC-2026-001 §1](../../governance/incidents/INC-2026-001-ratificacao-inferida.md) — quatro determinacoes do Soberano citadas literalmente a partir de ADR-0001 a ADR-0004 | **Sim** | Registro de determinacao |
| **F5** | [ADR-0006 §8, E7](../../decisions/ADR-0006-adocao-do-enterprise-artifact-framework.md) — determinacao da Missao 1.3 sobre arquetipo e ontologia | **Sim** | Nivel 3 |
| **F6** | [FND-09 §10](../../foundation/09-meta-model.md) — mecanismo de Fitness Check **determinado pelo Soberano** | **Sim** | Nivel 2 |
| **F7** | [RFC-0003 §2, P4](../../rfcs/RFC-0003-architecture-fitness-check.md) — pratica observada: revisao arquitetural por determinacao dele **em cada missao** | **Sim** | Proposta registrada |
| **F8** | [ADR-0007 §5.1](../../decisions/ADR-0007-fronteira-greenfield-legado.md) — existencia e externalidade do `LucaX Legacy` | **Sim** | Nivel 3 |
| **F9** | **Determinacao de abertura da Missao 1.5** — texto integral disponivel a execucao | **Nao** | **Nivel 8** *(instrucao / mensagem)* |
| **F10** | **Instrucao permanente do Soberano ao ambiente de execucao** — preferencias declaradas por ele para qualquer projeto | **Nao** | **Nivel 8** *(instrucao / mensagem)* |

> **CT-11 aplicado, com residuo declarado.** **F9** e **F10** sao externas ao acervo e ocupam o
> **nivel mais baixo** da hierarquia normativa. Vinte e uma afirmacoes as invocam, em duas
> situacoes distintas:
>
> | Situacao | Quais | Leitura |
> |---|---|---|
> | **Corroborada por fonte interna** — 12 | AF-04, AF-14, AF-15, AF-16, AF-17, AF-23, AF-32, AF-35, AF-39, AF-40, AF-42, AF-45 | A fonte externa **confirma** o que o acervo ja registra. Retirar a fonte externa nao apaga a afirmacao |
> | **Apoiada apenas em fonte externa** — 9 | AF-21, AF-22, AF-24, AF-25, AF-27, AF-28, AF-33, AF-43, AF-44 | Retirar a fonte externa **derruba** a afirmacao. Sao as candidatas preferenciais a retirada (CT-19) |
>
> Nenhuma delas e norma. **Que estas fontes sejam "aprovadas" nao foi objeto de ato do
> Soberano** — o residuo esta declarado em
> [ADR-0010 §12](../../decisions/ADR-0010-contrato-de-conhecimento-do-soberano.md), e nao
> omitido (PI-10).

> **Nenhuma fonte do `LucaX Legacy` foi consultada** (FR-03, FR-04, e determinacao expressa da
> Missao 1.5). AF-06 registra apenas a **existencia** do sistema, que ja consta de ADR-0007.

## 9. Pacotes de contexto e custo medido

> **CT-22:** carregamento integral e **proibido por padrao**. **CT-23:** custo medido em
> linhas, nunca estimado. **CT-20:** carregar acima do minimo exige gatilho declarado, e o
> carregamento e registrado no artefato que o consome.

| Pacote | Gatilho | Consumidor | Fonte *(secoes)* | **Custo medido** | % deste registro |
|---|---|---|---|---|---|
| **P1 — minimo** | Sempre que o Contexto for consultado | Qualquer papel | §1 e §7 | **28** linhas | **9,9%** |
| **P2 — estrategico** | Decisao C2/C3, priorizacao, arbitragem de tradeoff | DEP-EXE, DEP-GOV | P1 + §2 e §3 | **52** linhas | **18,4%** |
| **P3 — dominio** | Trabalho no dominio da afirmacao | O papel do dominio | P1 + a subsecao aplicavel de §4 | **38** linhas *(maior subsecao)* | **13,5%** |
| **P4 — sob demanda** | Gatilho nomeado na propria afirmacao | Quem o gatilho nomear | A afirmacao, por ID | **1 linha** | **0,4%** |
| *(referencia)* | *carregamento integral* | **proibido por padrao** | o registro inteiro | **282** linhas | 100% |

**Medicao:** `sed -n '<inicio>,<fim>p' | wc -l` sobre este arquivo, em 2026-07-28.
**Prova de que uma missao futura carrega apenas o perfil necessario:** uma decisao C2 carrega
**P2 = 52 linhas**, e nao as **282** do registro — **81,6%** do registro nao e
carregado. O numero e medido, nao estimado (CE-02, CE-04).

> **Limite da medicao, declarado (PI-10).** O custo esta medido; o **beneficio** nao. Nenhum
> componente existe para consumir estes pacotes, e por isso nao se pode afirmar que o recorte
> e o certo — apenas que ele e menor. Registrado como evidencia ausente **A1** em
> [ADR-0010 §8](../../decisions/ADR-0010-contrato-de-conhecimento-do-soberano.md).

## Relacionados

| ID | Relacao |
|---|---|
| [ADR-0010](../../decisions/ADR-0010-contrato-de-conhecimento-do-soberano.md) | **Origem.** Institui o contrato e autoriza este registro |
| [RFC-0007](../../rfcs/RFC-0007-conhecimento-sobre-o-soberano.md) | Proposta de origem; §9.1 traz o Teste de Entidade que manteve `Contexto do Soberano` como conteudo, nao entidade |
| [FND-01](../../foundation/01-constituicao.md) | Fonte de F1 — e a norma que este registro **nunca** supera |
| [FND-06 §3.1](../../foundation/06-arquitetura-memoria.md) | Camada que hospeda este registro, e que ja o previa |
| [INC-2026-001](../../governance/incidents/INC-2026-001-ratificacao-inferida.md) | Fonte de F2, F3 e F4; e o incidente cuja causa AF-15 e AF-40 registram do lado do Soberano |
| [FND-03 §8](../../foundation/03-taxonomia.md) | Fonte do **termo** `Contexto do Soberano`; este registro e o **conteudo** |

## Gatilhos de promocao (FND-06 §5.2)

- [ ] Confirmado em 2+ ocorrencias independentes → candidato a **EST** — **ja e EST**; a promocao aplicavel seria a **norma**, e exige rito C3 (CT-04)
- [ ] Recuperado repetidamente para o mesmo fim → candidato a Skill (PI-14) — **nao ha componente**; nada a promover
- [x] Determinado diretamente pelo Soberano → entrada em EST autorizada por [ADR-0010](../../decisions/ADR-0010-contrato-de-conhecimento-do-soberano.md)

## Gatilhos de expiracao (FND-06 §5.3)

- [ ] `ttl` de afirmacao vencido sem renovacao → a **afirmacao** expira, nao o registro
- [ ] Afirmacao `inferred` nao confirmada → expira (CT-08). **Nao ha nenhuma hoje**
- [ ] Nunca recuperado ao longo de um horizonte (RC-05) → candidato a poda
- [ ] Refutado por evidencia nova → `superado`, **nunca apagado** (CT-10, MM-09)
- [ ] Retirada por ato do Soberano (CT-19) → `superado`, sem necessidade de motivacao

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-KMS | Registro inicial: **45 afirmacoes** — 34 com evidencia e **11 `unknown`** —, dez fontes nomeadas, **zero** afirmacoes `inferred`, quatro pacotes de contexto com custo medido. Nasce em `aprovado`, com `ratificacao: pendente` (CT-28). |
