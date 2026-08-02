---
id: ADR-0008-uma-fonte-multiplas-projecoes
titulo: Adotar "uma fonte, multiplas projecoes" para toda tabela normativa, com teste preventivo antes da submissao
tipo: adr
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-QAR
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0003, ADR-0004, ADR-0006]
substitui: []
substituido_por: null
classe_mudanca: C2
tipo_decisao: 2
supera: []
superado_por: null
resumo: Fixa que tabela normativa vive em fonte unica, que toda exibicao dela e projecao declarada, e move a verificacao de duplicacao para antes da submissao.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-GOV
ratificacao: nao-exigida
---

# ADR-0008: Uma fonte, multiplas projecoes

## Proposito

Registrar a decisao de corrigir a **causa** da duplicacao documental por reproducao de tabela
— defeito que produziu ressalva em duas missoes consecutivas — e de fechar as duas ocorrencias
abertas.

## Escopo

| Item | Definicao |
|---|---|
| **Inclui** | Regra de fonte unica para tabela e diagrama normativos; contrato de declaracao de projecao; tratamento de campo de estado em artefato imutavel; teste preventivo antes da submissao; correcao das duas ocorrencias vigentes |
| **Nao inclui** | Automacao de verificacao (nao ha codigo nem infraestrutura); reescrita do acervo; criacao de tipo, entidade ou template |
| **Subordinado a** | [FND-04 §8](../foundation/04-governanca.md), [FND-10](../foundation/10-artifact-framework.md) |

## Responsaveis

| Papel | Quem |
|---|---|
| Proponente | **DEP-QAR** — detectou o padrao em FIT-2026-001 e FIT-2026-002 |
| Guardiao (forma e classe) | DEP-GOV |
| Revisor independente | **DEP-GOV** |
| Aprovador | **DEP-EXE** |
| Ratificador | **Nao aplicavel** — C2/Tipo 2 (§11) |
| Executor | DEP-GOV |

> **Nota de independencia.** O defeito esta em documentos produzidos por DEP-GOV (FND-09,
> FND-10). Por isso a proposta e de DEP-QAR e a aprovacao de DEP-EXE; DEP-GOV atua como
> guardiao de forma e revisor, nunca como proponente da correcao do proprio produto
> (FND-04 §3.1, ADR-0005).

---

## 1. Contexto

Duas verificacoes de aptidao consecutivas registraram a **mesma classe de defeito**:

| Ressalva | Ocorrencia | Estado ate esta decisao |
|---|---|---|
| **R2 de [FIT-2026-001](../governance/fitness/FIT-2026-001-meta-model.md)** | O grafo de transicao de estados esta reproduzido em FND-03 §5.1 **e** em FND-09 §7.1 | **Aberta** |
| **R2 de [FIT-2026-002](../governance/fitness/FIT-2026-002-artifact-framework.md)** | O diretorio de cada tipo esta em FND-03 §7 **e** repetido na coluna Local da matriz FND-10 §10.3 | **Aberta** |

A missao anterior ja havia criado o instrumento de deteccao — a auditoria de **coerencia
interna de norma** (FND-04 §8), que verifica *"tabela ou diagrama reproduzido de outro
documento em vez de referenciado"*. Ele **funcionou**: detectou o segundo caso. E nao o
**preveniu**, porque so age depois do texto pronto, na auditoria.

O aprendizado ja estava escrito em FIT-2026-002 §Aprendizado, com dono declarado (DEP-GOV) e
acao declarada — *"o checklist de `TPL-documento` passa a incluir a verificacao antes da
submissao, nao so na auditoria"* —, e nao havia sido executado.

Um terceiro caso apareceu nesta missao, de natureza diferente e mais grave: o campo
`ratificacao` foi declarado obrigatorio em artefatos de classe **M1**, cujo conteudo nunca
muda (CC-01). Um campo de **estado** que nao pode ser atualizado no proprio arquivo so pode
ser lido como *estado no ato*; lido como *estado corrente*, mente. Detalhado em
[INC-2026-001 §11.4](../governance/incidents/INC-2026-001-ratificacao-inferida.md).

**Se nada mudar:** a terceira missao produz a terceira ressalva da mesma familia, e o
mecanismo de aptidao passa a produzir divida em vez de correcao — risco ja nomeado em
FIT-2026-002 §FT-04.

## 2. Problema / Pergunta de decisao

Como impedir que informacao normativa seja reproduzida em segundo documento — em vez de
apenas detectar a reproducao depois de escrita?

## 3. Criterios de decisao

> Declarados antes do exame das alternativas (CD-01).

| # | Criterio | Peso | Como se mede |
|---|---|---|---|
| C1 | Age **antes** da submissao, nao apenas na auditoria | **Bloqueante** | Existe passo obrigatorio anterior ao portao em que o autor responde |
| C2 | Distingue **reproduzir** de **exibir legitimamente** | **Bloqueante** | Uma tabela derivada conforme continua permitida, com declaracao |
| C3 | Fecha as duas ocorrencias abertas | Alto | R2 de FIT-2026-001 e R2 de FIT-2026-002 saem de "aberta" |
| C4 | Nao cria artefato, tipo, entidade nem template | Alto | Contadores inalterados |
| C5 | Verificavel sem automacao | Alto | Conferivel por leitura, nesta fase sem codigo |

## 4. Alternativas consideradas

### Alternativa A — Regra de fonte unica + projecao declarada + teste preventivo

| Campo | Conteudo |
|---|---|
| Descricao | Tabela normativa vive em uma fonte; qualquer outra exibicao e **projecao** e declara fonte, campos, finalidade e metodo de atualizacao; o autor responde ao teste no checklist **antes** de submeter; o Fitness Check passa a exigir evidencia de que o teste foi aplicado |
| A favor | Satisfaz C1 a C5. Nao proibe exibir — proibe exibir **sem declarar**, que e a forma verificavel do defeito |
| Contra | Depende de disciplina do autor enquanto nao houver automacao |
| Custo | 1 secao em FND-10, 1 item de checklist em `TPL-documento`, 1 verificacao em `TPL-fitness-check` |
| Avaliacao | C1 ✔ · C2 ✔ · C3 ✔ · C4 ✔ · C5 ✔ |

### Alternativa B — Proibir toda repeticao de conteudo normativo

| Campo | Conteudo |
|---|---|
| Descricao | Nenhum documento pode exibir informacao que ja exista em outro; sempre link |
| A favor | Regra simples e absoluta; deteccao trivial |
| Contra | **Falha em C2.** Destroi as matrizes que cruzam dimensoes — FND-10 §10.3 cruza tipo × autoridade × ciclo × local, e uma dessas colunas vem sempre de outro documento. Tambem inviabiliza o catalogo mestre, que e projecao por definicao (RG-01). Proibir a projecao para impedir a copia elimina o instrumento junto com o defeito |
| Custo | Alto: reescrita de varias matrizes |
| Avaliacao | C1 ✔ · C2 **falha** · C3 ✔ · C4 ✔ · C5 ✔ |

### Alternativa C — Manter apenas a deteccao e automatizar depois

| Campo | Conteudo |
|---|---|
| Descricao | Conservar a auditoria de coerencia interna e esperar existir infraestrutura para verificar automaticamente |
| A favor | Custo zero agora |
| Contra | **Falha em C1 e C3.** A deteccao ja existe e ja falhou em prevenir — e a evidencia e de duas missoes, nao de uma. Alem disso, condiciona a correcao a uma dependencia que **nao existe e nao tem data**: nao ha codigo nem infraestrutura, e G3 de FND-10 §3.4 registra que automacao real e hoje impossivel |
| Custo | Zero agora; uma ressalva por missao depois |
| Avaliacao | C1 **falha** · C2 ✔ · C3 **falha** · C4 ✔ · C5 ✔ |

### Alternativa Z — Nao fazer nada

| Campo | Conteudo |
|---|---|
| O que acontece se mantivermos o estado atual | As duas ressalvas permanecem abertas ate a "1a revisao" de cada documento, e o padrao continua livre para se repetir |
| Custo real da inacao | Ja e mensuravel: **duas ocorrencias em duas missoes consecutivas**, ambas detectadas depois de escritas. A terceira dispara o alerta de complacencia de FIT-2026-002 §FT-04 — ressalva emitida sem que nenhuma anterior tenha sido fechada |
| Por que nao venceu | Aprendizado com dono e acao declarados, nao executado, deixa de ser aprendizado e vira divida (FND-06) |

## 5. Decisao

**Decidimos adotar a regra "uma fonte, multiplas projecoes"**, nos seguintes termos.

### 5.1 As seis regras

| # | Regra |
|---|---|
| **PJ-01** | **Tabela, matriz ou diagrama normativo vive em exatamente uma fonte.** Qualquer outro documento **referencia, filtra ou projeta** — nunca reproduz. Reproducao consistente hoje e defeito hoje: o defeito e a segunda fonte de verdade, nao a divergencia, que e apenas o momento em que ele se torna visivel (MM-01, FND-03 §7.1) |
| **PJ-02** | **Toda projecao se declara**, com as quatro informacoes: **fonte** (ID e secao), **campos** projetados, **finalidade** (por que a projecao existe em vez do link) e **metodo de atualizacao** (quem a atualiza, e sob que gatilho). Tabela derivada sem as quatro e **reproducao**, nao projecao |
| **PJ-03** | **Em divergencia, a fonte prevalece** e o defeito e da projecao. Corrigir a fonte para caber na projecao e proibido — e a regra M3 de FND-10 §6.2 generalizada a todo artefato |
| **PJ-04** | **Campo de estado em artefato de classe M1 registra o estado no ato**, nunca o estado corrente. Como o conteudo de M1 nunca muda (CC-01, LV-04), o estado corrente vive na fonte declarada, e o campo do artefato e leitura historica. Vale para `ratificacao`, `status` de instrumento superado e qualquer campo futuro de mesma natureza |
| **PJ-05** | **A verificacao de reproducao e feita pelo autor, antes da submissao** — item obrigatorio do checklist de [`TPL-documento`](../foundation/templates/TPL-documento.md). A auditoria de coerencia interna (FND-04 §8) permanece, como segunda barreira. **Deteccao posterior nao substitui prevencao** |
| **PJ-06** | **O Fitness Check verifica a prevencao, nao so a ocorrencia.** A pergunta F2 passa a exigir duas respostas: houve duplicacao? **e** o teste preventivo foi aplicado antes da submissao, com evidencia? Responder apenas a primeira e responder pela metade |

### 5.2 Campo `projecao_de` — opcional, com valor padrao

| Campo | Valores | Obrigatorio em | Valor padrao |
|---|---|---|---|
| `projecao_de` | `<ID> §<secao>` de cada fonte projetada, ou ausente | Artefato cujo conteudo seja **majoritariamente** projecao — indice, catalogo, matriz derivada | **Ausente** = o artefato nao e projecao |

> **Satisfaz AC-07** (campo novo exige valor padrao declarado ou janela de migracao): a
> ausencia e o padrao, e **nenhum arquivo do acervo precisa ser tocado**. O campo existe para
> tornar a projecao detectavel por varredura; a declaracao completa das quatro informacoes de
> PJ-02 vive no corpo, porque nao cabe em um campo.

### 5.3 As duas ocorrencias abertas — fechadas nesta decisao

| Ocorrencia | Correcao aplicada | Ressalva que fecha |
|---|---|---|
| Grafo de estados reproduzido em FND-09 §7.1 | O grafo e removido de FND-09; a secao passa a **referenciar** FND-03 §5.1. FND-09 conserva o que e proprio dele: os quatro perfis de ciclo (§7.2), que **restringem** o grafo | **R2 de FIT-2026-001** |
| Coluna Local reproduzida em FND-10 §10.3 | A coluna e removida da matriz; a matriz passa a declarar-se **projecao** de FND-03 §7 quanto a localizacao, cruzando as tres dimensoes que sao proprias dela: autoridade, ciclo e perfil | **R2 de FIT-2026-002** · acao **A7** de REV-ARTIFACT §10 |

> Ambas as correcoes **removem** conteudo duplicado e **nao alteram norma**: a regra removida
> continua valendo, no lugar unico onde sempre esteve. Sao, por isso, alteracoes de efeito
> nulo sobre o conteudo normativo — o que muda e onde ele e lido (AL-01).

### 5.4 O que a regra **nao** proibe

| Continua permitido | Porque |
|---|---|
| Catalogo mestre listar os 85 artefatos com tipo, perfil e custo | E projecao declarada (RG-01); a fonte de cada linha e o proprio artefato |
| Indice de diretorio listar a sequencia que conta | E o registro oficial daquela sequencia (IX-01/IX-03) |
| Matriz cruzar dimensoes de documentos diferentes | Desde que declare a fonte de cada coluna projetada (PJ-02) |
| Citar uma regra pelo codigo, com uma frase de contexto | Citacao nao e reproducao: nao substitui a leitura da fonte nem cria segunda tabela |

## 6. Justificativa

A Alternativa A vence pelos cinco criterios. B falha no bloqueante C2: eliminaria as matrizes
e o proprio catalogo, que sao instrumentos, nao defeitos. C falha em C1 e C3, e falha da pior
forma — condicionando a correcao a uma automacao que o proprio acervo registra como impossivel
nesta fase (FND-10 §3.4, gatilho G3).

**O que muda de fato.** Antes, a pergunta "isto duplica?" era feita por um verificador, depois
do texto pronto. Agora e feita pelo autor, antes da submissao, e o verificador passa a
perguntar se ela foi feita. Deslocar quem pergunta e quando pergunta e a unica correcao de
causa disponivel sem automacao.

**Sobre PJ-04.** A regra nasceu de um caso concreto desta missao: `ratificacao` foi tornado
obrigatorio em ADR — classe M1 — e, quando a ratificacao ocorreu, o campo nao pode ser
atualizado sem violar CC-01. Sem PJ-04, restariam duas saidas ruins: editar artefato imutavel,
ou conviver com campo que afirma o contrario do fato. PJ-04 abre a terceira: o campo e leitura
historica, e a fonte corrente esta declarada.

**Tradeoff aceito:** a regra depende de disciplina do autor enquanto nao houver automacao. Um
autor que ignore o item do checklist reintroduz o defeito, e a segunda barreira — a auditoria
— continuara detectando depois. Aceita-se essa dependencia porque a alternativa e esperar por
uma infraestrutura que nao existe e nao tem data.

## 7. Impacto

| Dimensao | Impacto |
|---|---|
| Departamentos afetados | DEP-GOV (auditoria e templates), DEP-QAR (F2 do Fitness Check), todo autor de artefato |
| Componentes afetados | Nenhum |
| Camadas de memoria a atualizar | APR — [MEM-APR-0002](../memory/aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md) e [MEM-APR-0003](../memory/aprendizado/MEM-APR-0003-campo-de-estado-em-artefato-imutavel.md) |
| Decisoes superadas | Nenhuma. ADR-0004 e ADR-0006 sao **complementados** |
| Documentos a atualizar | FND-09 v1.2.0 (§7.1) · FND-10 v1.1.0 (§2.6 nova, §10.3) · `TPL-documento` v1.2.0 · `TPL-fitness-check` v1.1.0 |
| Ressalvas fechadas | **2** — R2 de FIT-2026-001 e R2 de FIT-2026-002 |
| Acoes fechadas | **1** — A7 de REV-ARTIFACT §10 |
| Custo e dependencia criados | 1 item de checklist por artefato novo; 1 pergunta a mais no Fitness Check |
| Ganho PI-14 | **Reducao de contexto** — duas reproducoes removidas do acervo; e **organizacao**, por deslocar a verificacao para quem escreve |

## 8. Evidencias

| # | Evidencia | Origem (ID) | Confianca | O que ela discrimina |
|---|---|---|---|---|
| E1 | Duas ressalvas da mesma familia em duas missoes consecutivas | FIT-2026-001 R2; FIT-2026-002 R2 | **Alta — verificavel** | Sustenta que e padrao, nao ocorrencia. Elimina Z |
| E2 | A auditoria de coerencia interna detectou o segundo caso e nao preveniu | FIT-2026-002 §F2 e §Aprendizado | **Alta — verificavel** | Elimina a Alternativa C |
| E3 | Acao corretiva ja declarada com dono, e nao executada | FIT-2026-002 §Aprendizado | **Alta — verificavel** | Sustenta a urgencia relativa |
| E4 | Matrizes legitimas cruzam dimensoes de documentos distintos | FND-10 §10.3; catalogo mestre §4 | **Alta — verificavel** | **Elimina a Alternativa B** |
| E5 | `ratificacao` obrigatorio em ADR (M1) tornou-se inatualizavel apos o ato soberano | [INC-2026-001 §11.4](../governance/incidents/INC-2026-001-ratificacao-inferida.md) | **Alta — observada nesta missao** | Sustenta PJ-04 |
| E6 | Automacao de verificacao e hoje impossivel | FND-10 §3.4, gatilho G3 | Alta | Elimina o adiamento da Alternativa C |

**Evidencia ausente, declarada (VD-05):** nao ha medicao de quantas reproducoes existem no
acervo alem das duas conhecidas. A varredura desta missao (§7 da revisao arquitetural) e por
leitura, nao exaustiva por ferramenta — e portanto **nao prova ausencia**.

## 9. Riscos e mitigacao

| # | Risco | Probabilidade | Impacto | Mitigacao prevista |
|---|---|---|---|---|
| R1 | O item de checklist virar formalidade marcada sem execucao | **Media** | Medio | PJ-06: o Fitness Check pergunta pela **evidencia** da aplicacao, nao pela marca |
| R2 | A distincao projecao × reproducao ser usada para legitimar copia com rotulo | Media | Medio | PJ-02 exige as quatro informacoes; "metodo de atualizacao" e a que uma copia nao consegue responder |
| R3 | Remover o grafo de FND-09 §7.1 tornar a leitura mais dificil para quem le so o Meta Model | **Alta** | **Baixo** | Aceito e declarado: um salto de link contra uma segunda fonte de verdade. A referencia nomeia secao exata |
| R4 | **Esta decisao estar errada** — a regra ser burocratica demais para o ganho | Baixa | Baixo | Gatilho de revisao em §12: se nenhuma reproducao for barrada ate a 2a revisao estrutural, aplicar EV-08 ao item de checklist |

## 10. Plano de reversao

| Campo | Conteudo |
|---|---|
| Como desfazer | ADR de revogacao superando este; PJ-01 a PJ-06 saem de FND-10 por versao MENOR; o item volta a existir apenas na auditoria |
| Custo da reversao | **Trivial** |
| Por que a reversao e trivial (Tipo 2) | Acrescenta regra de forma e remove texto duplicado. Nenhum artefato depende dela; nenhum conteudo normativo foi alterado, apenas relocalizado por referencia |
| Sobre as duas remocoes | O texto removido continua integralmente em FND-03 §5.1 e §7 — **nada se perde**; reverter e recolar, se algum dia se quiser o defeito de volta |
| Quem executa | DEP-GOV, sob aprovacao de DEP-EXE |
| Backup necessario (PI-07) | Nenhum — nenhum conteudo unico e removido |

## 11. Classificacao

| Campo | Valor |
|---|---|
| Classe de mudanca | **C2 — Estrutural** (muda padrao de redacao normativa) |
| Tipo de reversibilidade | **Tipo 2** |
| Decisor | DEP-EXE |
| Ratificador | **Nao aplicavel** — C2/Tipo 2 (FND-04 §2.2, FND-07 §2.3) |
| Data da decisao | 2026-07-28 |
| Data de vigencia | 2026-07-28 |

> **RFC dispensada.** FND-04 §2 permite dispensar a RFC em C2 quando a alternativa unica for
> obvia **e** DEP-GOV concordar por escrito. A funcao da RFC — abrir a pergunta e coletar
> alternativas — ja foi cumprida por **dois** Fitness Checks independentes, que registraram o
> defeito, o dono e a correcao. Concordancia de DEP-GOV registrada em §13. Ainda assim, tres
> alternativas reais foram analisadas em §4, satisfazendo VD-01.

## 12. Revisao

| Campo | Conteudo |
|---|---|
| Gatilho por evento | **Terceira ocorrencia** da mesma familia de defeito — indicaria que a prevencao no autor tambem nao basta, e que o proximo degrau e automacao ou reducao de matrizes |
| Gatilho por evento | Existir consumidor programatico do acervo — reavaliar PJ-05 para verificacao automatica (G3, FND-10 §3.4) |
| Gatilho por confirmacao de ganho | 2a revisao estrutural: **nenhuma** reproducao barrada pelo checklist ⇒ aplicar EV-08 ao item |
| Gatilho temporal | 2027-01-28 |
| Sinal de que esta decisao deu errado | Projecoes declaradas proliferarem como forma de legitimar copia — muitos blocos de PJ-02 com "metodo de atualizacao: manual, quando necessario" |
| Responsavel pela revisao | DEP-QAR |

## 13. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Origem | Ressalva **R2** de [FIT-2026-001](../governance/fitness/FIT-2026-001-meta-model.md); ressalva **R2** e §Aprendizado de [FIT-2026-002](../governance/fitness/FIT-2026-002-artifact-framework.md); acao **A7** de [REV-ARTIFACT](../foundation/revisao-arquitetural-artifact-framework-2026-07-28.md) §10 |
| Decisoes superadas | Nenhuma |
| Decisoes relacionadas | [ADR-0004](ADR-0004-adocao-do-architecture-fitness-check.md) e [ADR-0006](ADR-0006-adocao-do-enterprise-artifact-framework.md) — complementados |
| Artefatos alterados | FND-09 v1.2.0; FND-10 v1.1.0; `TPL-documento` v1.2.0; `TPL-fitness-check` v1.1.0 |
| Concordancia de DEP-GOV com a dispensa de RFC | Registrada: *"a pergunta ja foi aberta por duas verificacoes independentes, e a acao corretiva ja estava declarada com dono. Abrir RFC para reproposta seria rito sem funcao. DEP-GOV concorda com a dispensa e atua apenas como guardiao de forma e revisor, por ser o produtor dos documentos onde o defeito esta."* — 2026-07-28 |
| Registros de memoria gerados | [MEM-APR-0002](../memory/aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md) · [MEM-APR-0003](../memory/aprendizado/MEM-APR-0003-campo-de-estado-em-artefato-imutavel.md) |
| Verificacao de aptidao | [FIT-2026-003](../governance/fitness/FIT-2026-003-consolidacao-baseline.md) (QG-6, CV-07) |

---

## Checklist de validade (FND-07 §4.1)
- [x] VD-01 — 3 alternativas reais + "nao fazer nada"
- [x] VD-02 — criterios declarados antes da escolha (§3 antes de §4)
- [x] VD-03 — nenhuma alternativa de palha: B e a regra absoluta, C e o estado atual mantido
- [x] VD-04 — tradeoff aceito explicito (§6)
- [x] VD-05 — ausencia de varredura exaustiva declarada (§8)
- [x] VD-06 — reversao declarada trivial, com justificativa (Tipo 2)
- [x] VD-07 — impacto em cascata mapeado e executado (§7)
- [x] VD-08 — data e responsavel presentes
- [x] VD-09 — gatilhos de revisao definidos (§12)
