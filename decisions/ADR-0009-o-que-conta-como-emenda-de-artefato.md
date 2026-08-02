---
id: ADR-0009-o-que-conta-como-emenda-de-artefato
titulo: Definir que "emendado", no contrato de artefato, e a alteracao que incrementa MAIOR ou MENOR
tipo: adr
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0006, ADR-0008]
substitui: []
substituido_por: null
classe_mudanca: C2
tipo_decisao: 2
supera: []
superado_por: null
resumo: Fixa que a obrigacao dos cinco campos do contrato de artefato nasce da alteracao de efeito normativo, preservando a migracao de custo zero do acervo anterior.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# ADR-0009: O que conta como "emendado" no contrato de artefato

## Proposito

Registrar a decisao de ler *"criado ou emendado"*, em [FND-10 §2.2 e §2.3](../foundation/10-artifact-framework.md),
como **alteracao que incrementa MAIOR ou MENOR** — fechando o achado **C13** de
[REV-CONSOLIDACAO](../foundation/revisao-arquitetural-consolidacao-2026-07-28.md) sem anular a
promessa de migracao de custo zero sob a qual ADR-0006 foi ratificado.

## Escopo

| Item | Definicao |
|---|---|
| **Inclui** | A leitura do termo "emendado"; o tratamento de `CORRECAO`, de artefato **M1** e de artefato **M3**; a regra de deteccao de alteracao sem incremento de versao |
| **Nao inclui** | Quais sao os cinco campos, seus valores e seus padroes (ADR-0006, ratificado); migracao do acervo nao emendado; alteracao de EV-03, que mantem `revisor` nao retroativo |
| **Subordinado a** | [FND-01](../foundation/01-constituicao.md), [FND-03 §6](../foundation/03-taxonomia.md), [FND-04 §2](../foundation/04-governanca.md), [FND-10 §2](../foundation/10-artifact-framework.md) |

## Responsaveis

| Papel | Quem |
|---|---|
| Proponente | DEP-GOV |
| Revisor independente | **DEP-QAR** |
| Aprovador | **DEP-EXE**, com parecer de DEP-GOV (FND-04 §2.1, C2) |
| Ratificador | **Nao aplicavel** — C2/Tipo 2 (§11) |
| Executor | DEP-GOV |

---

## 1. Contexto

FND-10 entrou em vigor em 2026-07-28, com a ratificacao de ADR-0006 registrada em
[INC-2026-001 §11](../governance/incidents/INC-2026-001-ratificacao-inferida.md). Seu §2.2
obriga cinco campos novos em *"artefato criado ou emendado a partir da vigencia"*, e seu §2.3
promete, em texto expresso, que **os artefatos existentes nao sao tocados**.

Na mesma missao em que a promessa foi feita, tres artefatos do acervo anterior foram alterados
e **nao** passaram a declarar os campos. A revisao arquitetural registrou o fato como achado
**C13**, com dono DEP-GOV e gatilho *"proxima mudanca C2/C3"*, e **deliberadamente nao
corrigiu**: escolher uma das duas leituras naquele momento seria promover hipotese a norma —
recusado ali mesmo nos achados C2 e C5.

**Se nada mudar:** a duvida reabre a cada missao, e o gatilho declarado em C13 vira
formalidade. O gatilho dispara nesta missao, que e C2.

## 2. Problema / Pergunta de decisao

**Qual alteracao de um artefato do acervo anterior faz nascer a obrigacao de declarar os cinco
campos do contrato de FND-10 §2.2?**

## 3. Criterios de decisao

> Declarados antes do exame das alternativas (CD-01, VD-02). Reproduzidos de
> [RFC-0006 §4](../rfcs/RFC-0006-contrato-de-artefato-o-que-e-emenda.md), que e a fonte.

| # | Criterio | Peso | Como se mede |
|---|---|---|---|
| C1 | Preserva a promessa de migracao de custo zero de §2.3 | **Bloqueante** | Arquivos reescritos por obrigacao retroativa = 0 |
| C2 | Criterio binario, conferivel sem julgar merito | **Bloqueante** | DEP-GOV decide olhando o Historico de versoes |
| C3 | Proporcional ao risco (GV-02) | Alto | Correcao editorial nao dispara contrato inteiro |
| C4 | Nao deixa buraco permanente | Alto | Todo artefato **vivo** converge ao contrato |
| C5 | Reversivel | Medio | Desfazer nao exige tocar artefato |

## 4. Alternativas consideradas

Analise completa em [RFC-0006 §5](../rfcs/RFC-0006-contrato-de-artefato-o-que-e-emenda.md).
Sintese:

### Alternativa A — Incremento de MAIOR ou MENOR *(escolhida)*

| Campo | Conteudo |
|---|---|
| Descricao | A obrigacao nasce da alteracao de **efeito normativo**, que FND-03 §6 ja obriga a versionar e a registrar no Historico de versoes |
| A favor | Reusa sinal ja existente e ja obrigatorio; nao cria campo, marcador nem controle |
| Contra | Artefato que so receba `CORRECAO` permanece atendido apenas pelo catalogo (L2) |
| Custo | 4 regras em FND-10 §2.3; 0 arquivos reescritos por retroatividade |
| Risco | Alteracao sem incremento escapar da obrigacao — tratado por AC-11 |
| Avaliacao | C1 ✔ · C2 ✔ · C3 ✔ · C4 ✔ · C5 ✔ |

### Alternativa B — Qualquer edicao do arquivo

| Campo | Conteudo |
|---|---|
| Descricao | Tocar o arquivo por qualquer motivo dispara a obrigacao |
| A favor | Enunciado simples; convergencia mais rapida |
| Contra | **Falha em C1 e C3.** Anula §2.3 comecando pelos artefatos **mais mantidos** — os indices, que IX-02 e RG-03 obrigam a atualizar a cada mudanca. Cria incentivo a nao corrigir link quebrado |
| Custo | Baixo hoje, alto e permanente depois |
| Risco | Converter uma promessa em letra morta sem revoga-la — o pior dos dois mundos |
| Avaliacao | C1 **falha** · C2 ✔ · C3 **falha** · C4 ✔ · C5 ✔ |

### Alternativa C — Migrar os 68 artefatos agora

| Campo | Conteudo |
|---|---|
| Descricao | Aplicar os cinco campos a todo o acervo anterior de uma vez |
| A favor | Elimina a distincao entre migrado e nao migrado |
| Contra | **Falha em C1 e C5.** Reescreve 68 arquivos e contraria **EV-03**. Pior: `revisor` de artefato antigo so poderia ser preenchido por atribuicao inventada, o que e **LV-12** |
| Custo | 68 arquivos tocados |
| Risco | Fabricar revisor onde nao houve revisao |
| Avaliacao | C1 **falha** · C2 ✔ · C3 **falha** · C4 ✔ · C5 **falha** |

### Alternativa Z — Nao fazer nada

| Campo | Conteudo |
|---|---|
| O que acontece se mantivermos o estado atual | A ambiguidade permanece e C13 segue aberto |
| Custo real da inacao | Ja observado: uma missao inteira registrou o achado sem poder fecha-lo. O gatilho dispara agora; adiar de novo o transformaria em formalidade, que e como uma ressalva vira divida permanente |
| Por que nao venceu | O adiamento so seria defensavel se faltasse informacao. Nao falta — a escolha nao depende de nenhum fato futuro |

## 5. Decisao

**Decidimos que, para efeito do contrato de artefato de FND-10 §2.2, "emendado" e a alteracao
que incrementa a versao MAIOR ou MENOR do proprio artefato.** FND-10 §2.3 recebe quatro
regras.

| # | Regra |
|---|---|
| **AC-08** | **"Emendado" e a alteracao que incrementa MAIOR ou MENOR** do proprio artefato (FND-03 §6). A partir dela, os cinco campos de §2.2 sao obrigatorios **no artefato**, e sua ausencia e nao conformidade (AC-06). |
| **AC-09** | **`CORRECAO` (C0) nao dispara a obrigacao**, e **atualizacao derivada de artefato M3** pela mudanca que o afeta (CV-04, RG-03) tambem nao. Do contrario a promessa de §2.3 se anularia primeiro nos artefatos mais mantidos — os indices —, que sao obrigados a acompanhar toda mudanca (IX-02). |
| **AC-10** | **Artefato M1 nunca e emendado**, logo AC-08 nunca o alcanca (§6.2). Corrige-se **superando**, e o sucessor ja nasce sob o contrato por ser artefato novo. |
| **AC-11** | **Alteracao de conteudo sem incremento de versao e nao conformidade a FND-03 §6**, nao terceira natureza de mudanca. Corrige-se declarando a versao devida no ato; a obrigacao decorre da versao corrigida, **nunca de efeito retroativo** (FND-01 §9, EV-03). |

### 5.1 Aplicacao imediata — os tres artefatos de C13

Os tres sao emendados **nesta missao**, e por isso passam a declarar os cinco campos. Nenhum e
tocado por efeito retroativo de AC-08.

| Artefato | Por que a obrigacao se aplica agora | Campos que faltavam |
|---|---|---|
| [`README.md`](../README.md) | Emendado nesta missao *(indice mestre recebe a fase, a nova baseline e os artefatos novos — mudanca de conteudo, MENOR)* | os cinco |
| [`foundation/03-taxonomia.md`](../foundation/03-taxonomia.md) | Emendado nesta missao *(§8 recebe termo oficial novo, MENOR)* | quatro — ja declarava `ratificacao` |
| [`memory/README.md`](../memory/README.md) | Emendado nesta missao *(registra a primeira memoria da camada EST, MENOR)*. Aplica-se **AC-11** a alteracao nao versionada da Missao 1.4: o defeito de forma e sanado declarando a versao devida | os cinco |

### 5.2 Alcance alem dos tres — todo artefato tocado nesta missao

C13 nomeou tres artefatos porque foram os tres tocados na Missao 1.4. A regra vale para
**todo** artefato emendado, e esta missao emenda outros dois que tambem nao declaravam os
campos:

| Artefato | Emenda desta missao |
|---|---|
| [`foundation/06-arquitetura-memoria.md`](../foundation/06-arquitetura-memoria.md) | §3.1 passa a remeter ao contrato de conhecimento sobre o Soberano ([ADR-0010](ADR-0010-contrato-de-conhecimento-do-soberano.md)) |
| [`memory/estrategica/README.md`](../memory/estrategica/README.md) | Registra a primeira memoria formal da camada |

> **Nenhum outro artefato do acervo e tocado por esta decisao.** Os demais **63** artefatos sem
> os cinco campos permanecem atendidos pelo catalogo mestre (L2), como §2.3 preve.

## 6. Justificativa

A Alternativa A vence pelos dois criterios bloqueantes, que **nenhuma** das outras satisfaz.

**Por que o incremento de versao e o sinal certo.** AL-01 ja determina que a alteracao segue a
classe do **efeito**, nao do tamanho do texto. A versao e a materializacao desse efeito, e ja e
obrigatoria em todo artefato desde ADR-0001. Escolhe-se um sinal existente em vez de criar um
segundo — que seria, ele proprio, segunda fonte de verdade sobre o mesmo fato (MM-01).

**Por que a promessa de §2.3 nao e detalhe de conforto.** Ela foi condicao declarada da
adocao de FND-10: a Alternativa B a anularia sem revoga-la, deixando no acervo uma promessa
escrita que nao se cumpre. Uma norma que se contradiz na aplicacao e pior que a ausencia de
norma, porque ensina que texto normativo pode ser ignorado quando incomoda.

**Tradeoff aceito, explicito.** Um artefato que so receba correcoes editoriais pode nunca
declarar os cinco campos. Aceita-se essa lacuna porque ela e **coberta onde importa**: o
catalogo mestre cura `resumo`, `perfil_contexto` e `confidencialidade` (L2, §2.3), e o que
sobra — `revisor` — ja e declarado nao retroativo por **EV-03**. Preencher `revisor` num
artefato antigo exigiria nomear um revisor que nao revisou, que e LV-12. **A lacuna aceita e
menor que a violacao evitada.**

## 7. Impacto

| Dimensao | Impacto |
|---|---|
| Departamentos afetados | DEP-GOV (confere a obrigacao no portao); DEP-KMS (mantem a curadoria L2) |
| Componentes afetados | **Nenhum** — nao existe componente |
| Entidades novas | **Zero** — universo permanece em 21 |
| Tipos documentais novos | **Zero** — universo permanece em 33 |
| Camadas de memoria a atualizar | Nenhuma. A decisao nao produz fato duravel alem do proprio ADR (MM-07) |
| Decisoes superadas | **Nenhuma.** ADR-0006 e **interpretado**, nao alterado: os cinco campos, seus valores e seus padroes continuam exatamente como ratificados |
| Documentos a atualizar | [FND-10 §2.3](../foundation/10-artifact-framework.md) v1.2.0 *(AC-08 a AC-11)* · os cinco artefatos de §5.1 e §5.2 · catalogo mestre · indices |
| Arquivos reescritos por retroatividade | **Zero** |
| Custo e dependencia criados | Quatro regras. Nenhuma dependencia externa. Nenhum campo, marcador ou controle novo |
| Ganho PI-14 | **Organizacao** — uma pergunta binaria que a norma nao respondia passa a ter resposta conferivel sem julgar merito |

## 8. Evidencias

| # | Evidencia | Origem (ID) | Confianca | O que ela discrimina |
|---|---|---|---|---|
| E1 | A norma **nao** define "emendado", e os tres arquivos tocados apresentam **duas naturezas** distintas de alteracao | [REV-CONSOLIDACAO §10, C13](../foundation/revisao-arquitetural-consolidacao-2026-07-28.md) | **Alta — verificavel** | Estabelece que a ambiguidade e real e ja produziu efeito. Elimina a Alternativa Z |
| E2 | §2.3 promete, em texto expresso, que os artefatos existentes **nao sao tocados** | [FND-10 §2.3](../foundation/10-artifact-framework.md) | **Alta — verificavel** | Elimina as Alternativas B e C pelo criterio bloqueante C1 |
| E3 | `revisor` e declarado **nao retroativo** | FND-10 §2.3, **EV-03** (FND-09 §11.4) | **Alta — verificavel** | Elimina a Alternativa C: migrar exigiria fabricar revisor (LV-12) |
| E4 | FND-03 §6 ja obriga toda mudanca MAIOR ou MENOR a acrescentar linha ao Historico de versoes | [FND-03 §6](../foundation/03-taxonomia.md) | **Alta — verificavel** | Sustenta que o sinal de AC-08 **ja existe** e nao precisa ser criado |
| E5 | **68** dos 93 artefatos do acervo nao declaram os cinco campos | Varredura por ferramenta sobre o frontmatter de todos os `.md`, 2026-07-28 | **Alta — medida** | Dimensiona o custo da Alternativa C |

**Evidencia ausente, declarada (VD-05):** **nao ha nenhuma medicao do custo real de manter a
lacuna** de AC-09 — isto e, de quantos artefatos permanecerao indefinidamente sem os cinco
campos por so receberem `CORRECAO`. Esse numero so pode ser observado ao longo de varios
ciclos, e nao existe hoje. Apresenta-lo como pequeno seria estimativa disfarcada de fato
(LV-12, CE-04). Fica como gatilho de revisao (§12).

## 9. Riscos e mitigacao

| # | Risco | Probabilidade | Impacto | Mitigacao prevista |
|---|---|---|---|---|
| R1 | Alteracao de conteudo sem incremento de versao escapar da obrigacao | Media | Medio | **AC-11**: ja e nao conformidade a FND-03 §6, verificada na auditoria de conformidade de artefato (FND-04 §8) |
| R2 | Artefato que so recebe `CORRECAO` nunca convergir ao contrato | Media | Baixo | Aceito e declarado (§6). Coberto por L2; `revisor` ja e nao retroativo por EV-03 |
| R3 | A fronteira `CORRECAO` × `MENOR` ser disputavel caso a caso | Baixa | Baixo | Nao e fronteira nova: FND-03 §6 a define e ela ja e aplicada em toda versao emitida. Este ADR **reusa**, nao cria |
| R4 | **Esta decisao estar errada** — a leitura restritiva deixar buraco maior que o previsto | Baixa | Medio | Gatilho de revisao por evento em §12; reversao trivial (§10). Se o buraco se mostrar grande, a Alternativa B continua disponivel, agora com dado observado em vez de hipotese |
| R5 | AC-09 ser lido como dispensa geral para indices | Baixa | Medio | O texto de AC-09 limita a dispensa a **atualizacao derivada** pela mudanca que o afeta. Mudanca de estrutura ou de escopo do proprio indice incrementa MENOR e dispara AC-08 |

## 10. Plano de reversao

| Campo | Conteudo |
|---|---|
| Como desfazer | ADR de revogacao superando este; AC-08 a AC-11 saem de FND-10 §2.3 por versao MENOR |
| Custo da reversao | **Trivial** |
| Por que a reversao e trivial (Tipo 2) | Nao cria componente, entidade, tipo documental, campo, template nem dependencia. Os cinco artefatos que passam a declarar os campos **continuariam validos** apos a revogacao: declarar mais do que o exigido nunca e nao conformidade |
| Janela | Permanente |
| Quem executa | DEP-GOV, sob aprovacao de DEP-EXE |
| Backup necessario (PI-07) | Nenhum — nenhum dado vivo e tocado, nenhum arquivo e removido ou sobrescrito em conteudo normativo |

## 11. Classificacao

| Campo | Valor |
|---|---|
| Classe de mudanca | **C2 — Estrutural** |
| Tipo de reversibilidade | **Tipo 2** |
| Decisor | DEP-EXE, com parecer de DEP-GOV |
| Ratificador | **Nao aplicavel** — C2/Tipo 2 (FND-04 §2.2, FND-07 §2.3) |
| Data da decisao | 2026-07-28 |
| Data de vigencia | 2026-07-28 |

> **Por que C2 e nao C3, e por que Tipo 2 e nao Tipo 1.** C2 e a mudanca que altera **padrao**
> (FND-04 §2) — a hipotese literal: fixa-se o padrao de aplicacao de um contrato ja adotado.
> Nao ha C3 porque nenhum principio imutavel, linha vermelha, hierarquia normativa ou direito
> de decisao muda, e **nenhum documento entra ou sai da Fundacao**. Quanto ao eixo de
> reversibilidade: o indicador *"mudanca de norma"* de FND-07 §2.1 esta presente, mas a norma
> alterada e **interpretativa e sem consumidor construido sobre ela** — revoga-la nao obriga a
> migrar nenhum artefato, porque declarar campos a mais nunca e defeito. **GV-03 foi
> considerado**: nao ha duvida a resolver, e a analise fica registrada para que a
> classificacao seja auditavel, e nao apenas afirmada.

## 12. Revisao

| Campo | Conteudo |
|---|---|
| Gatilho por evento | **Terceiro artefato** que permaneca sem os cinco campos por so receber `CORRECAO` ao longo de duas missoes — sinal de que a lacuna de AC-09 e maior que o previsto |
| Gatilho por evento | **Primeira divergencia real** sobre se uma alteracao foi `CORRECAO` ou `MENOR`, sinal de que R3 se materializou |
| Gatilho temporal | 2027-01-28 — revisao semestral da Fundacao |
| Sinal de que esta decisao deu errado | (a) O acervo estabilizar com a maioria dos artefatos vivos fora do contrato, e o catalogo virar a unica fonte pratica dos tres campos curados — sinal de que a convergencia prometida por C4 nao ocorre; (b) AC-11 nunca ser acionado apesar de haver alteracoes sem incremento — sinal de que a deteccao nao opera |
| Responsavel pela revisao | DEP-QAR |

## 13. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Origem | [RFC-0006](../rfcs/RFC-0006-contrato-de-artefato-o-que-e-emenda.md); achado **C13** de [REV-CONSOLIDACAO §10](../foundation/revisao-arquitetural-consolidacao-2026-07-28.md) |
| Decisoes superadas | Nenhuma |
| Decisoes relacionadas | [ADR-0006](ADR-0006-adocao-do-enterprise-artifact-framework.md) — **interpretado**, nao alterado; [ADR-0008](ADR-0008-uma-fonte-multiplas-projecoes.md) — §3 desta decisao declara-se projecao de RFC-0006 §4 |
| Artefatos alterados | FND-10 v1.2.0 (§2.3) · `README.md` · `foundation/03-taxonomia.md` · `memory/README.md` · `foundation/06-arquitetura-memoria.md` · `memory/estrategica/README.md` · catalogo mestre · indices |
| Registros de memoria gerados | **Nenhum** — a decisao nao produz fato duravel alem de si propria; criar registro seria duplicar a fonte (MM-01, MM-07) |
| Verificacao de aptidao | [FIT-2026-004](../governance/fitness/FIT-2026-004-conhecimento-do-soberano.md) (QG-6, CV-07) |

---

## Checklist de validade (FND-07 §4.1)
- [x] VD-01 — 3 alternativas reais + "nao fazer nada"
- [x] VD-02 — criterios declarados antes das alternativas (§3 antes de §4)
- [x] VD-03 — nenhuma alternativa de palha: B e a leitura oposta, defendida por C13; C e a solucao completa
- [x] VD-04 — tradeoff aceito explicito (§6)
- [x] VD-05 — evidencia ausente declarada (§8)
- [x] VD-06 — reversao declarada trivial, com justificativa (Tipo 2)
- [x] VD-07 — impacto em cascata mapeado e executado (§7)
- [x] VD-08 — data e responsavel presentes
- [x] VD-09 — gatilhos de revisao definidos (§12)
