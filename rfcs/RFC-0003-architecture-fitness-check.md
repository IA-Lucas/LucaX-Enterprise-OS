---
id: RFC-0003-architecture-fitness-check
titulo: Introduzir o Architecture Fitness Check como verificacao obrigatoria de aptidao evolutiva
tipo: rfc
versao: 1.0.0
status: aprovado
camada_memoria: nao-aplicavel
autor: DEP-QAR
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: null
decisoes_relacionadas: [ADR-0004]
substitui: []
substituido_por: null
classe_mudanca: C3
prazo_analise: 2026-07-28
---

# RFC-0003: Architecture Fitness Check

## Proposito
Propor um mecanismo obrigatorio de verificacao de **aptidao evolutiva** ao encerrar toda
mudanca estrutural: alem de perguntar se a arquitetura ficou correta, perguntar se ela ficou
**mais simples de evoluir**.

## Escopo
Abrange o mecanismo, o instrumento de registro (`FIT`), o portao correspondente e as regras
de veredito. Nao abrange o conteudo de nenhuma mudanca especifica nem substitui o
Architecture Review.

## Responsaveis
| Papel | Quem |
|---|---|
| Proponente | DEP-QAR |
| Areas que devem se manifestar | DEP-GOV (forma e classe), DEP-EXE (custo de cadencia), DEP-KMS (evidencia de contexto) |
| Aprovador | SOBERANO |
| Prazo de manifestacao | 2026-07-28 |

---

## 1. Situacao atual

O sistema verifica corretude em seis portoes (FND-01 §6.2), conformidade em cada mudanca
(FND-04 §8) e coerencia estrutural na revisao arquitetural que encerra cada trabalho de
arquitetura — como a que produziu
[a revisao do catalogo de Capabilities](../capabilities/revisao-arquitetural-2026-07-28.md).

Todas essas verificacoes medem **estado**: esta correto, esta conforme, esta rastreavel.

## 2. Problema

Nenhuma verificacao vigente mede **variacao**.

| # | Defeito | Consequencia |
|---|---|---|
| P1 | **Degradacao por acumulo de acertos.** Cada mudanca pode ser individualmente correta, conforme e rastreavel — e a soma delas tornar o sistema progressivamente mais caro de mudar. | O sistema fica correto e imovel. Nenhum portao dispara, porque nenhum portao pergunta pelo custo de evoluir. |
| P2 | **PI-14 e verificado apenas na entrada.** O Teste de Especializacao (FND-04 §6.2) exige ganho declarado **antes** de criar um componente. Nada verifica, **depois**, se a mudanca de fato reduziu contexto, aumentou reuso ou melhorou a organizacao. | O ganho declarado nunca e confrontado com o resultado. A metrica "Ganho de especializacao" de FND-01 §6.3 nao tem instrumento que a alimente. |
| P3 | **Complexidade nao tem dono.** Duplicacao e detectada; abstracao ociosa, nao. Custo de contexto e uma metrica declarada em FND-01 §6.3 e em FND-06 §9.1, sem nenhum momento obrigatorio de leitura. | As duas metricas de PI-14 existem no papel e nunca sao medidas. |
| P4 | **A revisao arquitetural nao e obrigatoria nem padronizada.** Ela ocorreu por determinacao do Soberano em cada missao, com perguntas definidas caso a caso. | O que depende de lembrar-se de pedir nao e garantia estrutural (Visao V3: qualidade produzida pela estrutura, nao pela atencao momentanea). |

**Evidencia direta:** a revisao do catalogo de Capabilities registrou 111 indicadores
definidos e 88 sem valor medido. Entre os nao medidos estao exatamente os que responderiam
a P2 e P3. Isso confirma que a organizacao **declara** saude arquitetural e nao a **verifica**.

## 3. Pergunta de decisao

O LucaX deve tornar obrigatoria, no encerramento de toda mudanca estrutural, uma verificacao
de aptidao evolutiva, com instrumento proprio e poder de bloquear o encerramento?

## 4. Criterios de avaliacao

| # | Criterio | Peso | Como se mede |
|---|---|---|---|
| C1 | Detecta degradacao que os portoes atuais nao detectam | Alto | Perguntas medem variacao, nao estado |
| C2 | Produz sinal observavel, nao opiniao | **Bloqueante** | Toda resposta exige numero ou fato verificavel (DoD-5) |
| C3 | Tem consequencia real | Alto | Veredito negativo bloqueia; nao vira observacao sem destino (FND-04 §8) |
| C4 | Nao duplica o Architecture Review nem os portoes existentes | **Bloqueante** | Pergunta distinta, momento distinto, veredito distinto |
| C5 | Custo proporcional | Medio | Nao se aplica a C0/C1; usa evidencia ja existente na memoria |
| C6 | Resiste a complacencia | Alto | Ha regra que trata a aprovacao sistematica como sinal de alerta |

## 5. Opcoes

### Opcao A — Verificacao obrigatoria com instrumento e portao proprios

| Campo | Conteudo |
|---|---|
| Descricao | Entidade `FIT`, seis perguntas com sinal observavel obrigatorio, veredito de tres valores, portao QG-6, executada por DEP-QAR |
| A favor | Satisfaz C1, C2, C3 e C6. Da instrumento as duas metricas de PI-14 que hoje nao sao medidas. Torna a verificacao estrutural, nao dependente de lembranca |
| Contra | Acrescenta um portao a Constituicao (C3) e um artefato por mudanca estrutural |
| Custo | 1 secao normativa, 1 template, 1 artefato por mudanca C2/C3 |
| Risco | Virar formalidade preenchida por habito |

### Opcao B — Ampliar o Architecture Review com as seis perguntas

| Campo | Conteudo |
|---|---|
| Descricao | Manter uma unica revisao, acrescentando as perguntas de aptidao as de corretude |
| A favor | Nenhum instrumento novo; nenhum portao novo; custo minimo |
| Contra | **Confunde dois vereditos.** A revisao de corretude produz achados com severidade; a de aptidao produz veredito que bloqueia. Fundidas, o veredito bloqueante seria diluido em lista de achados — e achado de severidade media nao bloqueia nada. Alem disso, o Architecture Review **nao e obrigatorio hoje** (P4): ampliar um mecanismo opcional nao produz garantia |
| Custo | Baixo |
| Risco | Alto — o mecanismo continua dependendo de ser lembrado |

### Opcao C — Metrica de saude acompanhada na revisao estrutural periodica

| Campo | Conteudo |
|---|---|
| Descricao | Medir contexto, reuso e complexidade apenas na revisao semestral (FND-02 §9.4) |
| A favor | Custo minimo por mudanca; cadencia ja existente |
| Contra | **Detecta tarde.** Entre duas revisoes cabem todas as mudancas de um horizonte; a degradacao seria constatada quando ja estivesse consolidada, e a correcao exigiria desfazer trabalho aprovado. Nao satisfaz C3: a revisao periodica nao bloqueia nada |
| Custo | Baixo |
| Risco | Medio — deteccao tardia e cara |

### Opcao Z — Nao fazer nada

| Campo | Conteudo |
|---|---|
| O que acontece | A arquitetura continua verificada quanto a corretude e nao quanto a aptidao. P1 a P4 permanecem |
| Custo real da inacao | Cresce de forma nao linear: cada camada acrescentada sem verificacao de aptidao aumenta o custo de detectar e desfazer a proxima |
| Por que nao venceu | A plataforma esta em fase de acumulo rapido de camadas normativas — tres em um unico dia. E exatamente a fase em que a degradacao se instala sem sinal |

## 6. Recomendacao do proponente

**Opcao A.**

A Opcao B falha em C3 e C4: fundir os vereditos dilui o unico que bloqueia, e amplia um
mecanismo que hoje nem sequer e obrigatorio. A Opcao C falha em C3 e detecta tarde demais.

Sobre **C4 (bloqueante)**: as seis perguntas nao repetem nenhuma pergunta do Architecture
Review. Duas parecem proximas e nao sao:

| Pergunta do Review | Pergunta do Fitness | Diferenca |
|---|---|---|
| "Existe entidade duplicada?" | "Algum conceito foi duplicado?" | A primeira examina o **estado** do catalogo; a segunda examina o que **a mudanca introduziu** — inclusive definicao recolada em vez de referenciada, que nao cria entidade nova e mesmo assim duplica conceito |
| "Alguma entidade deveria ser abstraida?" | "Alguma abstracao ficou desnecessaria?" | A primeira busca abstracao **faltante**; a segunda busca abstracao **ociosa** — o movimento simetrico, que hoje nao tem verificador |

Sobre **C6**: a regra FT-04 — tres vereditos `apto` consecutivos sem uma unica ressalva
escalam ao Soberano — e o mesmo dispositivo que a Constituicao ja aplica a taxa de
reprovacao zero em QG-3 (FND-01 §6.3) e que FND-02 §9.4 aplica a revisao que conclui "manter
tudo" tres vezes. Nao e invencao: e aplicacao de um padrao ja adotado.

## 7. Impacto previsto

| Dimensao | Impacto |
|---|---|
| Documentos afetados | FND-01 (§6.2 novo portao QG-6), FND-02 (§9.4 revisao estrutural), FND-03 (identificador `FIT`, diretorio, frontmatter), FND-04 (§4 ciclo de mudanca, §8 auditoria), FND-09 (§10, mecanismo) |
| Artefatos criados | `TPL-fitness-check`; `governance/fitness/` com indice e contador |
| Quem executa | DEP-QAR, independente do produtor (PI-05) |
| Cadencia | Um `FIT` por mudanca C2 ou C3; nenhum em C0; opcional em C1 |
| Ganho PI-14 pretendido | **Organizacao:** a degradacao passa a ter dono e momento de deteccao. **Reuso:** as seis perguntas servem a qualquer mudanca futura sem adaptacao. **Reducao de contexto:** a metrica "Contexto por papel" passa a ser lida periodicamente, em vez de existir apenas no papel |
| Sinal que comprovara o ganho | Primeiro veredito `inapto` ou `apto-com-ressalva` que impeca uma mudanca de encerrar como estava |

## 8. Riscos

| # | Risco | Probabilidade | Impacto | Mitigacao |
|---|---|---|---|---|
| R1 | Virar formalidade: seis "nao" preenchidos por habito | **Alta** | Alto | C2 bloqueante — resposta sem sinal observavel e devolvida; FT-04 escala complacencia ao Soberano |
| R2 | Atrasar mudancas legitimas | Media | Medio | Nao se aplica a C0; opcional em C1; usa evidencia ja existente na memoria |
| R3 | Veredito subjetivo usado para bloquear por preferencia | Media | Alto | Veredito exige fundamento em sinal; `inapto` sem sinal e ele proprio devolvivel por DEP-GOV; ressalva exige dono e gatilho |
| R4 | Sobreposicao com o Architecture Review | Media | Medio | §6 delimita as duas perguntas ambiguas; FT-01 declara complementaridade |
| R5 | Acrescentar portao a Constituicao por mecanismo ainda nao testado | Media | **Alto** | Gatilho de revisao no ADR: se apos tres mudancas o mecanismo nao tiver produzido nenhuma ressalva com dono, ele proprio e candidato a consolidacao (EV-08) |

## 9. Perguntas em aberto

| Pergunta | Dono da resposta | Bloqueia? |
|---|---|---|
| O Fitness Check deve ser portao constitucional ou etapa de FND-04? | DEP-GOV | Nao — resolvido: portao, porque precisa bloquear e ser liberado por quem nao produziu |
| Deve aplicar-se a C1 em lote? | DEP-EXE, apos o primeiro horizonte | Nao — recomendado, nao obrigatorio |
| Quem mede o custo de contexto? | DEP-KMS | Nao — evidencia vem da memoria, veredito vem de DEP-QAR |

## 10. Manifestacoes

| Area | Posicao | Fundamento | Data |
|---|---|---|---|
| DEP-QAR | Propoe | O sistema mede corretude e nao mede aptidao; 88 de 111 indicadores sem valor medido sao a evidencia | 2026-07-28 |
| DEP-GOV | Apoia com ressalva | Acrescentar portao a FND-01 §6.2 e mudanca **C3**, indelegavel. Exige ainda que o `FIT` siga o perfil de instrumento: imutavel apos eficacia, superado nunca editado | 2026-07-28 |
| DEP-EXE | Apoia com ressalva | Aceita o custo de cadencia, mas exige que o mecanismo nao se aplique a C0 e permaneca opcional em C1, sob pena de virar gargalo (FND-04 §12) | 2026-07-28 |
| DEP-KMS | Apoia | As metricas exigidas ja existem em FND-01 §6.3 e FND-06 §9.1; o Fitness Check e o consumidor que faltava a elas | 2026-07-28 |

## 11. Resultado

| Campo | Conteudo |
|---|---|
| Decisao | **aceita** |
| ADR gerado | [ADR-0004](../decisions/ADR-0004-adocao-do-architecture-fitness-check.md) |
| Ressalvas incorporadas | Classe **C3, Tipo 1**; perfil de instrumento imutavel (DEP-GOV); nao se aplica a C0 e opcional em C1 (DEP-EXE) |
| Origem | Determinacao direta do Soberano, 2026-07-28 |
| Data | 2026-07-28 |
| Responsavel | DEP-QAR |
