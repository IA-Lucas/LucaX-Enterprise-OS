---
id: ADR-0004-adocao-do-architecture-fitness-check
titulo: Adotar o Architecture Fitness Check como verificacao obrigatoria de aptidao evolutiva, com portao QG-6
tipo: adr
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-QAR
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0001, ADR-0003]
substitui: []
substituido_por: null
classe_mudanca: C3
tipo_decisao: 1
supera: []
superado_por: null
---

# ADR-0004: Adotar o Architecture Fitness Check

## Proposito

Registrar a decisao de criar o **Architecture Fitness Check** — verificacao obrigatoria de
aptidao evolutiva ao encerrar toda mudanca estrutural —, a entidade `FIT` que a registra e
o portao **QG-6** que a torna bloqueante.

## Escopo

Aplica-se ao encerramento de toda mudanca C2 e C3. Nao altera o conteudo de nenhuma decisao
existente, nao substitui o Architecture Review e nao cria componente de execucao.

## Responsaveis

| Papel | Quem |
|---|---|
| Proponente | DEP-QAR |
| Revisor independente | DEP-GOV |
| Consulta de cadencia e custo | DEP-EXE |
| Consulta de evidencia | DEP-KMS |
| Aprovador | SOBERANO |
| Ratificador | **SOBERANO** (C3 e Tipo 1) |
| Executor | DEP-GOV |

---

## 1. Contexto

O sistema verifica corretude em seis portoes (FND-01 §6.2), conformidade a cada mudanca
(FND-04 §8) e coerencia estrutural em revisoes arquiteturais executadas ao fim de cada
trabalho de arquitetura.

Todas medem **estado**. Nenhuma mede **variacao**.

Isso produz uma classe de falha que nenhum controle atual detecta: cada mudanca e
individualmente correta, conforme e rastreavel — e a soma delas torna o sistema
progressivamente mais caro de mudar. O sistema fica correto e imovel, sem que nenhum portao
dispare.

Tres consequencias ja observaveis nesta data:

1. **PI-14 e verificado apenas na entrada.** O Teste de Especializacao (FND-04 §6.2) exige
   ganho declarado **antes** de criar um componente; nada verifica **depois** se o ganho se
   confirmou.
2. **As metricas de PI-14 nao tem consumidor.** "Contexto por papel" (FND-01 §6.3) e "Volume
   de contexto por consulta" (FND-06 §9.1) estao declaradas e nunca foram lidas.
3. **A revisao arquitetural nao e obrigatoria nem padronizada.** Ocorreu por determinacao do
   Soberano em cada trabalho, com perguntas definidas caso a caso. O que depende de lembrar
   de pedir nao e garantia estrutural — contraria a Visao V3, que exige qualidade produzida
   pela estrutura e nao pela atencao momentanea.

**Evidencia direta:** a revisao do catalogo de Capabilities registrou 111 indicadores
definidos e **88 sem valor medido**. Entre os nao medidos estao precisamente os que
responderiam se a arquitetura esta ficando melhor ou pior de evoluir.

O momento importa: a plataforma acumulou tres camadas normativas em um unico dia — Fundacao,
Capabilities e Meta Model. E exatamente a fase em que a degradacao se instala sem sinal.

## 2. Problema / Pergunta de decisao

O LucaX deve tornar obrigatoria, no encerramento de toda mudanca estrutural, uma verificacao
de aptidao evolutiva com instrumento proprio e poder de bloquear o encerramento?

## 3. Criterios de decisao

> Definidos antes do exame das alternativas (CD-01). Herdados de
> [RFC-0003 §4](../rfcs/RFC-0003-architecture-fitness-check.md).

| # | Criterio | Peso | Como se mede |
|---|---|---|---|
| C1 | Detecta degradacao que os portoes atuais nao detectam | Alto | As perguntas medem variacao, nao estado |
| C2 | Produz sinal observavel, nao opiniao | **Bloqueante** | Toda resposta exige numero ou fato verificavel (DoD-5) |
| C3 | Tem consequencia real | Alto | Veredito negativo bloqueia; nao vira observacao sem destino |
| C4 | Nao duplica o Architecture Review nem os portoes existentes | **Bloqueante** | Pergunta, momento e veredito distintos |
| C5 | Custo proporcional | Medio | Nao se aplica a C0; opcional em C1; usa evidencia ja existente |
| C6 | Resiste a complacencia | Alto | Ha regra que trata a aprovacao sistematica como alerta |

## 4. Alternativas consideradas

### Alternativa A — Verificacao obrigatoria com instrumento e portao proprios

| Campo | Conteudo |
|---|---|
| Descricao | Entidade `FIT`, seis perguntas com sinal observavel obrigatorio, veredito de tres valores, portao QG-6, executada por DEP-QAR |
| A favor | Satisfaz C1, C2, C3 e C6; da consumidor as duas metricas de PI-14 que hoje nao sao lidas; torna a verificacao estrutural em vez de dependente de lembranca |
| Contra | Acrescenta portao a Constituicao (C3) e um artefato por mudanca estrutural |
| Custo | 1 secao normativa, 1 template, 1 artefato por mudanca C2/C3 |
| Risco | Virar formalidade preenchida por habito (R1) |
| Avaliacao | C1 alto · C2 satisfeito · C3 alto · C4 satisfeito · C5 medio · C6 alto |

### Alternativa B — Ampliar o Architecture Review com as seis perguntas

| Campo | Conteudo |
|---|---|
| Descricao | Uma unica revisao, somando aptidao a corretude |
| A favor | Nenhum instrumento novo, nenhum portao novo, custo minimo |
| Contra | **Dilui o veredito bloqueante.** A revisao de corretude produz achados com severidade; a de aptidao produz veredito que bloqueia. Fundidas, o bloqueio vira achado de severidade media — que nao bloqueia nada. Pior: o Architecture Review **nao e obrigatorio hoje**, e ampliar mecanismo opcional nao produz garantia |
| Custo | Baixo |
| Risco | Alto — o mecanismo continua dependendo de ser lembrado |
| Avaliacao | C1 medio · C2 medio · C3 **baixo** · C4 **falha** · C5 alto · C6 baixo |

### Alternativa C — Metrica de saude acompanhada na revisao estrutural periodica

| Campo | Conteudo |
|---|---|
| Descricao | Medir contexto, reuso e complexidade apenas na revisao semestral (FND-02 §9.4) |
| A favor | Custo minimo por mudanca; usa cadencia existente |
| Contra | **Detecta tarde.** Entre duas revisoes cabem todas as mudancas de um horizonte; a degradacao seria constatada ja consolidada, e a correcao exigiria desfazer trabalho aprovado. Nao satisfaz C3: revisao periodica nao bloqueia |
| Custo | Baixo |
| Risco | Medio — deteccao tardia e cara |
| Avaliacao | C1 medio · C2 medio · C3 **baixo** · C4 satisfeito · C5 alto · C6 medio |

### Alternativa Z — Nao fazer nada

| Campo | Conteudo |
|---|---|
| O que acontece | A arquitetura continua verificada quanto a corretude e nao quanto a aptidao |
| Custo real da inacao | Cresce de forma nao linear: cada camada acrescentada sem verificacao aumenta o custo de detectar e desfazer a proxima. As duas metricas de PI-14 permanecem sem consumidor indefinidamente |
| Por que nao venceu | A fase corrente e de acumulo rapido de camadas normativas — a fase de maior risco de degradacao silenciosa |

## 5. Decisao

**Decidimos adotar o Architecture Fitness Check**, composto de:

1. O **mecanismo**, normatizado em [FND-09 §10](../foundation/09-meta-model.md): verificacao
   de aptidao evolutiva obrigatoria ao encerrar toda mudanca **C2** e **C3**, ao encerrar
   trabalho que produza ou altere artefato da Fundacao, do catalogo de Capabilities ou do
   Meta Model, e na revisao estrutural periodica. **Opcional em C1; nao se aplica a C0.**

2. As **seis perguntas obrigatorias** (FND-09 §10.3), cada uma com sinal observavel exigido:
   - **F1** A complexidade aumentou sem ganho proporcional?
   - **F2** Algum conceito foi duplicado?
   - **F3** Alguma abstracao ficou desnecessaria?
   - **F4** O sistema continua mais simples de evoluir do que antes?
   - **F5** A mudanca reduz ou aumenta o custo de contexto?
   - **F6** Ela favorece reutilizacao?

3. O **veredito de tres valores**: `apto`, `apto-com-ressalva`, `inapto`. **`inapto` bloqueia
   o encerramento** e devolve a mudanca a etapa [2] do ciclo de FND-04 §4.

4. A **entidade `FIT`** — Verificacao de Aptidao Arquitetural —, registrada no Meta Model
   (FND-09 §5.2, E-08), com identificador `FIT-<AAAA>-<NNN>-<slug>`, residencia em
   `governance/fitness/` e perfil de instrumento (imutavel apos eficacia; corrige-se
   superando, nunca editando).

5. O **portao QG-6 — Aptidao Arquitetural**, acrescentado a FND-01 §6.2, liberado por
   DEP-QAR com DEP-GOV, sujeito a regra geral de portao: **nao pode ser liberado por quem
   produziu o artefato**, e portao pulado exige excecao formal registrada.

6. As **nove regras de operacao** (FND-09 §10.6), das quais tres sao estruturais:
   - **FT-02** executor ≠ produtor, sob pena de veredito nulo (LV-03);
   - **FT-03** resposta sem sinal observavel e devolvida sem analise de merito;
   - **FT-04** tres vereditos `apto` consecutivos **sem uma unica ressalva** escalam ao
     Soberano como sinal de complacencia.

7. O **template `TPL-fitness-check`**, obrigatorio pela regra de FND-03 §3.9.

## 6. Justificativa

A Alternativa A vence nos dois criterios bloqueantes e nos tres de maior peso.

A Alternativa B **falha em C4**: fundir corretude e aptidao dilui o unico veredito que
bloqueia. Um mecanismo cuja unica consequencia e virar item de lista nao satisfaz C3, e a
propria Governanca ja proibe achado sem destino (FND-04 §8). Falha tambem em C6: ampliar um
mecanismo opcional nao cria garantia estrutural.

A Alternativa C **falha em C3 e detecta tarde**: entre duas revisoes semestrais cabe um
horizonte inteiro de mudancas, e degradacao consolidada custa desfazer trabalho ja aprovado
— exatamente o oposto de VL-04 (reversibilidade por padrao).

Sobre **C4 (bloqueante)**, o teste foi aplicado par a par. Duas perguntas parecem proximas
das do Architecture Review e nao sao:

| Architecture Review | Fitness Check | Diferenca material |
|---|---|---|
| "Existe entidade duplicada?" | "Algum conceito foi duplicado?" | A primeira examina o **estado do catalogo**; a segunda, o que **a mudanca introduziu** — inclusive definicao recolada em vez de referenciada, que nao cria entidade e mesmo assim duplica conceito (MM-01) |
| "Alguma entidade deveria ser abstraida?" | "Alguma abstracao ficou desnecessaria?" | A primeira busca abstracao **faltante**; a segunda, abstracao **ociosa** — movimento simetrico que hoje nao tem verificador, e que PI-14 regra 5 exige |

Sobre **C6**, FT-04 nao e dispositivo novo: e a aplicacao, a este mecanismo, do padrao que a
Constituicao ja usa em FND-01 §6.3 ("taxa de reprovacao zero em QG-3 e sinal de alerta, nao
de excelencia") e que FND-02 §9.4 usa na revisao estrutural ("manter tudo tres vezes seguidas
escala ao Soberano").

**Tradeoff aceito.** A organizacao passa a produzir um artefato adicional por mudanca
estrutural e a admitir um portao que pode bloquear trabalho tecnicamente correto. Aceita-se
esse custo em troca de que a degradacao arquitetural — a unica falha que nenhum controle
vigente detecta — passe a ter dono, momento de deteccao e consequencia.

**Ressalva de DEP-GOV incorporada:** acrescentar portao a FND-01 §6.2 e mudanca **C3**,
indelegavel; e o `FIT` segue o perfil de instrumento — imutavel apos eficacia, superado
nunca editado (FT-09).

**Ressalva de DEP-EXE incorporada:** o mecanismo **nao se aplica a C0** e permanece
**opcional em C1**, para nao converter governanca em gargalo (FND-04 §12).

## 7. Impacto

| Dimensao | Impacto |
|---|---|
| Departamentos afetados | DEP-QAR passa a executar; DEP-GOV verifica forma; DEP-KMS fornece evidencia; DEP-EXE aprova |
| Componentes afetados | Nenhum existente. Toda mudanca C2/C3 futura passa a exigir `FIT` para encerrar |
| Camadas de memoria a atualizar | **EST** (o mecanismo) e **APR** (aprendizado gerado por cada verificacao, FT-07) |
| Decisoes superadas | Nenhuma |
| Documentos a atualizar | FND-01 v1.2.0 (§6.2 portao QG-6) · FND-02 v1.2.0 (§9.4 revisao estrutural) · FND-03 v1.2.0 (identificador `FIT`, sequencia, tipo, diretorio) · FND-04 v1.2.0 (§4 ciclo de mudanca, §8 auditoria) · FND-09 §10 |
| Artefatos criados | `TPL-fitness-check`; `governance/fitness/` com indice e contador; `FIT-2026-001` |
| Custo e dependencia criados | Um artefato por mudanca C2/C3. **Nenhuma dependencia externa** |
| Ganho PI-14 | **Organizacao:** a degradacao arquitetural passa a ter dono e momento de deteccao. **Reuso:** as seis perguntas servem a qualquer mudanca futura sem adaptacao. **Reducao de contexto:** a metrica "Contexto por papel" passa a ser lida periodicamente, em vez de existir apenas no papel |

## 8. Evidencias

| # | Evidencia | Origem | Confianca | O que discrimina |
|---|---|---|---|---|
| E1 | 88 de 111 indicadores de Capability sem valor medido | [Revisao arquitetural, achado A6](../capabilities/revisao-arquitetural-2026-07-28.md) | **Alta — verificavel** | Prova que a organizacao declara saude e nao a verifica |
| E2 | Nenhum dos seis portoes de FND-01 §6.2 pergunta pelo custo de evoluir | FND-01 §6.2 | Alta | Elimina a Alternativa Z; sustenta C1 |
| E3 | As metricas "Contexto por papel" e "Ganho de especializacao" existem desde ADR-0001 e nunca foram medidas | FND-01 §6.3 | Alta | Sustenta P2 e P3 da RFC |
| E4 | O Teste de Especializacao verifica o ganho **antes**, e nenhum instrumento o verifica **depois** | FND-04 §6.2 | Alta | Sustenta a lacuna que o mecanismo fecha |
| E5 | Determinacao do Soberano de que cada trabalho encerre com verificacao de saude da arquitetura | Instrucao direta, 2026-07-28 | Alta | Origem da proposta; elimina B e C |
| E6 | O padrao "aprovacao sistematica e sinal de alerta" ja e adotado em FND-01 §6.3 e FND-02 §9.4 | Fundacao vigente | Alta | Sustenta FT-04 como aplicacao, nao invencao |

**Evidencia ausente, declarada (VD-05):** o mecanismo **nunca foi executado** antes desta
data. Nao ha evidencia de que ele detecte degradacao real, nem de que o custo por mudanca
seja proporcional. A primeira execucao —
[FIT-2026-001](../governance/fitness/FIT-2026-001-meta-model.md) — e simultanea a esta
decisao e nao pode ser tratada como comprovacao independente.

## 9. Riscos e mitigacao

| # | Risco | Probabilidade | Impacto | Mitigacao |
|---|---|---|---|---|
| R1 | Virar formalidade: seis "nao" preenchidos por habito | **Alta** | Alto | C2 bloqueante (FT-03: sem sinal, devolvido); FT-04 escala complacencia ao Soberano |
| R2 | Atrasar mudancas legitimas | Media | Medio | Nao se aplica a C0; opcional em C1; usa evidencia ja existente na memoria |
| R3 | Veredito subjetivo usado para bloquear por preferencia | Media | Alto | `inapto` exige fundamento em sinal e e devolvivel por DEP-GOV se nao o tiver; ressalva exige dono e gatilho (FT-06) |
| R4 | Sobreposicao com o Architecture Review | Media | Medio | §6 delimita as duas perguntas ambiguas; FT-01 declara complementaridade explicita |
| R5 | Portao constitucional criado para mecanismo nao testado | Media | **Alto** | Gatilho de §12: se apos tres mudancas C2/C3 o mecanismo nao tiver produzido nenhuma ressalva com dono nem um `inapto`, ele proprio vira candidato a consolidacao (EV-08) |
| R6 | **Esta decisao estar errada** — o custo do portao exceder o valor que ele protege | Media | Alto | Reversao barata (§10); gatilhos de §12; o mecanismo e submetido as proprias seis perguntas na primeira revisao estrutural |

## 10. Plano de reversao

| Campo | Conteudo |
|---|---|
| Como desfazer | ADR de revogacao superando este; QG-6 removido de FND-01 §6.2 por nova versao MAIOR; FND-09 §10 passa a `revogado`; entidade `FIT` removida do Meta Model pelo rito de EV-06, com destino declarado dos `FIT` ja emitidos (preservados como historico, MM-09) |
| Custo da reversao | **Baixo** — apenas um `FIT` existe nesta data; nenhuma mudanca foi bloqueada por veredito |
| Janela em que ainda e possivel | Permanece barata: o custo cresce com o numero de `FIT` emitidos, e cada um e artefato isolado, sem dependentes |
| Reversao parcial | **Preferivel e possivel:** manter as seis perguntas como pratica recomendada e remover apenas a obrigatoriedade e o portao — equivale a recuar da Alternativa A para a B |
| Quem executa | DEP-GOV, sob ratificacao do Soberano |
| Backup necessario (PI-07) | Copia datada de `foundation/` e `governance/` antes de qualquer revogacao |

## 11. Classificacao

| Campo | Valor |
|---|---|
| Classe de mudanca | **C3** — acrescenta portao a Constituicao (FND-01 §6.2) |
| Tipo de reversibilidade | **Tipo 1** — cria obrigacao vinculante para toda mudanca estrutural futura |
| Decisor | SOBERANO |
| Ratificador | SOBERANO |
| Data da decisao | 2026-07-28 |
| Data de vigencia | 2026-07-28 |

## 12. Revisao

| Campo | Conteudo |
|---|---|
| Gatilho temporal | 2027-01-28 — revisao semestral da Fundacao |
| Gatilho por evento | **Apos tres mudancas C2/C3 verificadas**: se nenhuma produziu ressalva com dono nem veredito `inapto`, o mecanismo e candidato a consolidacao — ou o criterio esta frouxo, ou o mecanismo nao discrimina (FT-04, EV-08) |
| Gatilho por evento | Primeiro veredito `inapto` ou `apto-com-ressalva` que impeca uma mudanca de encerrar como estava — **confirma C1 e C3** |
| Gatilho por sinal de falha | Tempo medio para produzir um `FIT` exceder o tempo de produzir a mudanca que ele verifica — sinal de desproporcao (C5) |
| Gatilho por confirmacao de ganho PI-14 | Na revisao estrutural, verificar se as metricas "Contexto por papel" e "Ganho de especializacao" passaram a ter serie historica |
| Sinal de que esta decisao deu errado | `FIT` preenchidos com respostas identicas entre mudancas diferentes; vereditos sem sinal observavel aceitos; excecao formal recorrente para pular QG-6 |
| Responsavel pela revisao | DEP-QAR com DEP-GOV; DEP-EXE arbitra o custo de cadencia |

## 13. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Origem | [RFC-0003](../rfcs/RFC-0003-architecture-fitness-check.md), aceita em 2026-07-28; determinacao direta do Soberano |
| Decisoes superadas | Nenhuma |
| Decisoes relacionadas | [ADR-0003](ADR-0003-adocao-do-enterprise-meta-model.md) — registra a entidade `FIT` no Meta Model; [ADR-0001](ADR-0001-adocao-da-fundacao-organizacional.md) — emendada em §6.2 |
| Artefatos criados | `TPL-fitness-check`; `governance/fitness/README.md`; `FIT-2026-001` |
| Emendas em cascata | FND-01 v1.2.0 · FND-02 v1.2.0 · FND-03 v1.2.0 · FND-04 v1.2.0 |
| Primeira aplicacao | [FIT-2026-001](../governance/fitness/FIT-2026-001-meta-model.md) — verificacao do proprio Meta Model |
| Registros de memoria | Camada EST (o mecanismo); camada APR (aprendizado de cada verificacao) |

---

## Checklist de validade (FND-07 §4.1)
- [x] VD-01 — 3 alternativas reais + "nao fazer nada"
- [x] VD-02 — criterios declarados antes da escolha (herdados da RFC)
- [x] VD-03 — nenhuma alternativa de palha (B e C sao praticas correntes e defensaveis)
- [x] VD-04 — tradeoff aceito explicito (§6)
- [x] VD-05 — ausencia de evidencia de eficacia declarada (§8)
- [x] VD-06 — plano de reversao presente, com reversao parcial (Tipo 1)
- [x] VD-07 — impacto em cascata mapeado e executado (§7)
- [x] VD-08 — data e responsavel presentes
- [x] VD-09 — gatilhos de revisao definidos (§12)

---

## Ratificacao do Soberano

Esta decisao e C3 e Tipo 1: exige ato explicito do Soberano (PI-01, PI-06).

| Campo | Conteudo |
|---|---|
| Ratificado por | SOBERANO (Lucas) |
| Data | 2026-07-28 |
| Forma | Determinacao direta e escrita, durante a missao do Meta Model |
| Texto invocado | *"Alem do Architecture Review, cada Mission encerraria com uma verificacao de saude da arquitetura."* — seguido das seis perguntas adotadas integralmente em FND-09 §10.3 |

### Observacao de conformidade (DEP-GOV)

A determinacao invocada e ato soberano real e datado, e dela derivam tanto o mecanismo
quanto as seis perguntas, adotadas sem alteracao de conteudo. O que esta ADR acrescenta e a
forma: instrumento, veredito, portao, papeis e regras de operacao.

Duas escolhas de forma **nao** constam da determinacao e sao atribuiveis a DEP-QAR e
DEP-GOV, devendo ser lidas como proposta e nao como ordem do Soberano:

1. tratar a verificacao como **portao constitucional (QG-6)** em vez de etapa de FND-04;
2. estabelecer o **veredito bloqueante** `inapto`.

Discordando o Soberano de qualquer uma, esta ADR deve ser **superada** pelo rito de FND-07
§7, nunca editada (LV-04). Ate la, o mecanismo vigora integralmente.

| Campo | Conteudo |
|---|---|
| Confirmado apos leitura? | |
| Data | |
| Ajustes solicitados | |
