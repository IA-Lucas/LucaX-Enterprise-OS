---
id: RFC-0006-contrato-de-artefato-o-que-e-emenda
titulo: O que conta como "emendado" para efeito do contrato de artefato de FND-10 §2.3?
tipo: rfc
versao: 1.0.0
status: aprovado
camada_memoria: nao-aplicavel
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: null
decisoes_relacionadas: [ADR-0006, ADR-0009]
substitui: []
substituido_por: null
classe_mudanca: C2
prazo_analise: 2026-07-28
resumo: Submete a analise o criterio que define quando um artefato do acervo anterior passa a dever os cinco campos do contrato de artefato.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# RFC-0006: O que conta como "emendado" no contrato de artefato

## Proposito

Submeter a analise o criterio que decide **quando** um artefato criado antes da vigencia de
FND-10 passa a dever os cinco campos do contrato de artefato (§2.2), fechando o achado **C13**
de [REV-CONSOLIDACAO §10](../foundation/revisao-arquitetural-consolidacao-2026-07-28.md).

## Escopo

| Item | Definicao |
|---|---|
| **Inclui** | A leitura do termo *"criado ou emendado"* em [FND-10 §2.2 e §2.3](../foundation/10-artifact-framework.md); o efeito sobre os tres artefatos nomeados em C13; o tratamento de artefatos **M1** e **M3** |
| **Nao inclui** | Alterar quais sao os cinco campos, seus valores admitidos ou seus padroes — isso e ADR-0006, ja ratificado; migrar o acervo nao emendado |
| **Subordinado a** | [FND-01](../foundation/01-constituicao.md), [FND-03 §6](../foundation/03-taxonomia.md), [FND-04 §2](../foundation/04-governanca.md), [FND-10 §2](../foundation/10-artifact-framework.md) |

## Responsaveis

| Papel | Quem |
|---|---|
| Proponente | **DEP-GOV** — dono declarado de C13 |
| Areas que devem se manifestar | DEP-QAR (risco e conformidade), DEP-KMS (curadoria do catalogo) |
| Aprovador | **DEP-EXE**, com parecer de DEP-GOV (FND-04 §2.1, C2) |
| Prazo de manifestacao | 2026-07-28 |

---

## 1. Situacao atual

[FND-10 §2.2](../foundation/10-artifact-framework.md) declara que os cinco campos do contrato
sao obrigatorios em *"artefato criado ou emendado a partir da vigencia deste framework"*, e
§2.3 promete que **os artefatos existentes nao sao tocados**.

A vigencia ocorreu em 2026-07-28, com a ratificacao de ADR-0006 registrada em
[INC-2026-001 §11](../governance/incidents/INC-2026-001-ratificacao-inferida.md).

**A norma nao define o que e "emendado".** Nenhuma das duas leituras possiveis esta escrita.

## 2. Problema

Na Missao 1.4, tres artefatos do acervo anterior foram alterados sem passar a declarar os
campos, e a revisao arquitetural registrou o achado sem corrigi-lo, por nao ser possivel
corrigir sem **escolher uma leitura por hipotese** — exatamente o que os achados C2 e C5
daquela mesma revisao recusaram fazer.

| Artefato | O que houve na Missao 1.4 | Campos que declara |
|---|---|---|
| [`README.md`](../README.md) | Emenda versionada, ate `1.3.0` | **Nenhum** dos cinco |
| [`foundation/03-taxonomia.md`](../foundation/03-taxonomia.md) | Emenda versionada, `1.3.0` → `1.4.0` | Apenas `ratificacao` |
| [`memory/README.md`](../memory/README.md) | Alterado **sem** mudar de `1.0.0` | **Nenhum** dos cinco |

**Consequencia de manter a ambiguidade:** cada missao futura reabre a mesma duvida, e o
achado C13 permanece aberto por tempo indeterminado. A duvida ja custou uma missao inteira.

**Evidencia do problema:** o proprio C13 registra que os tres arquivos apresentam **duas
naturezas distintas** de alteracao, e que a norma nao discrimina entre elas
([REV-CONSOLIDACAO §10, C13 em detalhe](../foundation/revisao-arquitetural-consolidacao-2026-07-28.md)).

## 3. Pergunta de decisao

**Qual alteracao de um artefato do acervo anterior faz nascer a obrigacao de declarar os cinco
campos do contrato de FND-10 §2.2?**

## 4. Criterios de avaliacao

> Declarados antes do exame das opcoes (CD-01, VD-02).

| # | Criterio | Peso | Como se mede |
|---|---|---|---|
| C1 | **Preserva a promessa de migracao de custo zero** de §2.3 | **Bloqueante** | Arquivos do acervo reescritos **por obrigacao retroativa** = 0 |
| C2 | **Criterio binario, conferivel sem julgar merito** | **Bloqueante** | DEP-GOV decide olhando o Historico de versoes do artefato, sem interpretar intencao |
| C3 | Proporcional ao risco (GV-02) | Alto | Correcao de link ou de tipografia nao dispara contrato inteiro |
| C4 | Nao deixa buraco permanente | Alto | Existe caminho previsivel pelo qual todo artefato **vivo** converge ao contrato |
| C5 | Reversivel | Medio | Desfazer nao exige tocar nenhum artefato |

## 5. Opcoes

### Opcao A — "Emendado" e a alteracao que incrementa **MAIOR ou MENOR**

| Campo | Conteudo |
|---|---|
| Descricao | A obrigacao nasce da alteracao de **efeito normativo** — a que FND-03 §6 obriga a incrementar MAIOR ou MENOR e a acrescentar linha ao Historico de versoes. `CORRECAO` (C0) nao dispara. Atualizacao **derivada** de artefato M3 pela mudanca que o afeta (CV-04, RG-03) nao dispara. Artefato **M1** nunca dispara, porque nao e emendado — e superado |
| A favor | Usa um sinal que **ja existe e ja e obrigatorio** em todo artefato: a linha do Historico de versoes. Nao cria campo, marcador nem controle novo. Proporcional: a obrigacao acompanha o efeito, nao o tamanho do texto (AL-01) |
| Contra | Um artefato que so receba correcoes editoriais permanece sem os campos indefinidamente — atendido apenas pelo catalogo (L2) |
| Custo / Risco | Custo: 4 regras em FND-10 §2.3. Risco: alteracao de conteudo feita **sem** incrementar versao escapa da obrigacao — mitigado pela regra de deteccao (§9) |
| Quem e afetado | Todo artefato do acervo anterior que venha a ser emendado; DEP-GOV, que confere |
| Avaliacao | C1 ✔ · C2 ✔ · C3 ✔ · C4 ✔ *(converge por artefato, quando cada um for emendado)* · C5 ✔ |

### Opcao B — "Emendado" e **qualquer edicao** do arquivo

| Campo | Conteudo |
|---|---|
| Descricao | Tocar o arquivo por qualquer motivo — inclusive corrigir um link quebrado — obriga a declarar os cinco campos |
| A favor | Regra simples de enunciar; o acervo converge mais rapido ao contrato |
| Contra | **Falha em C1.** A promessa de §2.3 se anula na pratica, e se anula primeiro nos artefatos **mais mantidos** — os indices, que sao atualizados a cada mudanca por forca de IX-02 e RG-03. Falha em **C3**: obriga o contrato inteiro por uma virgula. E cria incentivo perverso — deixar de corrigir um link para nao disparar a obrigacao |
| Custo / Risco | Custo imediato baixo; custo estrutural alto e permanente |
| Quem e afetado | Todo indice do sistema, a cada encerramento de mudanca |
| Avaliacao | C1 **falha** · C2 ✔ · C3 **falha** · C4 ✔ · C5 ✔ |

### Opcao C — Migrar os 68 artefatos agora

| Campo | Conteudo |
|---|---|
| Descricao | Encerrar a duvida aplicando os cinco campos a todo o acervo anterior de uma vez |
| A favor | Elimina a distincao entre migrado e nao migrado; o catalogo deixa de curar o que o frontmatter passaria a declarar |
| Contra | **Falha em C1 e C5.** Reescreve 68 arquivos, revoga expressamente a promessa de §2.3 e contraria **EV-03**, que declara `revisor` nao retroativo. Alem disso, `revisor` de artefato antigo so poderia ser preenchido por atribuicao inventada — **LV-12** |
| Custo / Risco | 68 arquivos tocados; risco de fabricar `revisor` onde nao houve revisao |
| Quem e afetado | Todo o acervo anterior |
| Avaliacao | C1 **falha** · C2 ✔ · C3 **falha** · C4 ✔ · C5 **falha** |

### Opcao Z — Nao fazer nada

| Campo | Conteudo |
|---|---|
| Consequencia de manter o estado atual | A ambiguidade permanece; C13 segue aberto; a proxima missao reabre a mesma duvida com os mesmos argumentos |
| Custo da inacao | O custo ja e observado: **uma missao inteira** registrou o achado sem poder fecha-lo, e o gatilho declarado — *"proxima mudanca C2/C3"* — dispara **agora**. Adiar de novo transformaria o gatilho em formalidade |
| Por que nao vence | O adiamento so seria defensavel se faltasse informacao. Nao falta: as duas leituras estao enunciadas, e a escolha entre elas nao depende de nenhum fato futuro |

## 6. Recomendacao do proponente

**Opcao A.** E a unica que satisfaz os dois criterios bloqueantes. As opcoes B e C compram
convergencia mais rapida ao preco de anular a promessa de migracao zero — que nao e detalhe de
conforto, e a condicao sob a qual ADR-0006 foi ratificado.

A Opcao A tambem responde ao que a Opcao B tem de correto: o acervo **converge**, artefato por
artefato, no momento em que cada um recebe alteracao de efeito real. O que ela recusa e a
convergencia forcada por evento sem efeito normativo.

## 7. Impacto previsto

| Dimensao | Impacto |
|---|---|
| Departamentos | DEP-GOV (confere a obrigacao no portao); DEP-KMS (mantem a curadoria L2 dos nao emendados) |
| Componentes | **Nenhum** — nao existe componente |
| Normas afetadas | [FND-10 §2.3](../foundation/10-artifact-framework.md), versao MENOR, com 4 regras novas |
| Camadas de memoria | Nenhuma — a decisao nao produz fato duravel alem do proprio ADR |
| Entidades / tipos documentais novos | **Zero** |
| Artefatos que passam a declarar os cinco campos nesta missao | `README.md`, `foundation/03-taxonomia.md`, `memory/README.md`, `foundation/06-arquitetura-memoria.md`, `memory/estrategica/README.md` — **todos porque sao emendados agora**, nenhum por efeito retroativo |
| Ganho PI-14 pretendido e sinal que o comprova | **Organizacao.** Sinal ja observado: o achado C13 existe porque a norma nao respondeu a uma pergunta binaria feita durante a execucao. O ganho se confirma se a proxima missao nao precisar reabrir a duvida |

## 8. Riscos

| # | Risco | Impacto | Mitigacao |
|---|---|---|---|
| R1 | Alteracao de conteudo feita **sem** incrementar versao escapa da obrigacao | Medio | Regra de deteccao: alteracao de conteudo sem incremento ja e nao conformidade a FND-03 §6; corrige-se declarando a versao devida, e a obrigacao entao se aplica |
| R2 | Artefato que so recebe `CORRECAO` nunca converge ao contrato | Baixo | Aceito e declarado. O catalogo mestre cura `resumo`, `perfil_contexto` e `confidencialidade` (L2); o que falta e `revisor`, que **EV-03 ja declara nao retroativo** |
| R3 | A fronteira entre `CORRECAO` e `MENOR` ser ela propria disputavel | Baixo | Nao e fronteira nova: FND-03 §6 ja a define e ja e aplicada a cada versao emitida desde ADR-0001. Esta RFC nao cria criterio — **reusa** o que ja existe |
| R4 | A regra parecer obvia depois de escrita, e o custo da RFC parecer excessivo | Baixo | Duas leituras defensaveis atravessaram uma missao inteira sem que nenhuma prevalecesse. Obviedade retrospectiva nao e evidencia de que a duvida nao existiu |

## 9. Perguntas em aberto

| # | Pergunta | Estado |
|---|---|---|
| Q1 | Alteracao de conteudo **sem** incremento de versao deve ser tratada como emenda, ou como defeito de forma? | **Respondida na Opcao A:** e defeito de FND-03 §6. Corrige-se declarando a versao devida; a obrigacao decorre da versao corrigida, nunca de efeito retroativo |
| Q2 | Artefato **M1** pode ser "emendado"? | **Nao.** M1 e imutavel apos eficacia (FND-10 §6.2): corrige-se superando. A obrigacao nunca o alcanca — o **sucessor** ja nasce sob o contrato, por ser artefato novo |
| Q3 | Atualizar um indice ou o catalogo (M3) e emenda? | **Nao**, quando for reprocessamento derivado da mudanca que o afeta (CV-04, RG-03, M3). **Sim**, quando o proprio indice mudar de estrutura ou de escopo, o que incrementa MENOR |

## 10. Manifestacoes

| Area | Posicao | Fundamento | Data |
|---|---|---|---|
| **DEP-QAR** | **Apoia** | A Opcao A e a unica que nao exige inventar `revisor` retroativo, o que seria LV-12. R1 tem mitigacao verificavel | 2026-07-28 |
| **DEP-KMS** | **Apoia** | A curadoria L2 do catalogo ja cobre tres dos cinco campos para o acervo nao emendado; a Opcao C tornaria a curadoria redundante sem eliminar o trabalho | 2026-07-28 |
| **DEP-EXE** | **Apoia** | Proporcionalidade (GV-02) decide: obrigacao de contrato inteiro por correcao editorial e instrumento acima da classe real | 2026-07-28 |

## 11. Resultado

| Campo | Conteudo |
|---|---|
| Decisao | **Aceita** — Opcao A |
| ADR gerado | [ADR-0009](../decisions/ADR-0009-o-que-conta-como-emenda-de-artefato.md) |
| Se rejeitada, por que | Nao se aplica |
| Se adiada, ate quando e sob qual condicao | Nao se aplica — o gatilho declarado em C13 disparou nesta missao |
| Data | 2026-07-28 |
| Responsavel | DEP-EXE, com parecer de DEP-GOV |

---

## Linhagem

| Campo | Conteudo |
|---|---|
| Origem | Achado **C13** de [REV-CONSOLIDACAO §10](../foundation/revisao-arquitetural-consolidacao-2026-07-28.md), com dono DEP-GOV e gatilho *"proxima mudanca C2/C3"* |
| Deriva de | [FND-10 §2.2 e §2.3](../foundation/10-artifact-framework.md) |
| Gera | [ADR-0009](../decisions/ADR-0009-o-que-conta-como-emenda-de-artefato.md) |
| Gatilho de ativacao | Duvida sobre a obrigatoriedade dos cinco campos em artefato do acervo anterior |
| Dependencias minimas | FND-10 §2, FND-03 §6 |

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-GOV | Proposta inicial: tres opcoes reais e a opcao nula, cinco criterios declarados antes das opcoes, recomendacao pela Opcao A. |
