---
id: REV-ARTIFACT-2026-07-28
titulo: Revisao Arquitetural do Enterprise Artifact Framework
tipo: relatorio
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-QAR
proprietario: DEP-QAR
aprovador: DEP-EXE
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0005, ADR-0006]
substitui: []
substituido_por: null
classe_avaliacao: corretude
resumo: Examina FND-10 quanto a corretude estrutural e verifica as tres correcoes obrigatorias da Missao 1.3.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-EXE
ratificacao: nao-exigida
---

# Revisao Arquitetural do Enterprise Artifact Framework

## Proposito
Submeter o Artifact Framework (FND-10) e as tres correcoes obrigatorias da Missao 1.3 a exame
critico independente, registrando cada achado com severidade, dono e gatilho.

## Escopo
| Item | Definicao |
|---|---|
| Inclui | FND-10, ADR-0005, ADR-0006, INC-2026-001, catalogo mestre, emendas em cascata; verificacao das tres correcoes obrigatorias |
| Nao inclui | Aptidao evolutiva — objeto de [FIT-2026-002](../governance/fitness/FIT-2026-002-artifact-framework.md) |
| Metodo | Confronto com FND-01 a FND-09; classificacao exaustiva do acervo; varredura de links e de frontmatter |

## Responsaveis
| Papel | Responsavel |
|---|---|
| Executa | **DEP-QAR** — independente de DEP-GOV, que produziu FND-10 (RM-06b, ADR-0005) |
| Aprova | DEP-EXE |
| Decide sobre os achados | SOBERANO |

---

## Sumario dos achados

| # | Achado | Severidade | Acao |
|---|---|---|---|
| A1 | Seis decisoes C3/Tipo 1 com **ratificacao pendente**: todo o corpo normativo esta condicionado | **Alta** | Ato unico do Soberano; INC-2026-001 aberto |
| A2 | Ganho de contexto e **calculado, nao observado** — nenhum trabalho executado sob os perfis | **Alta** *(esperada)* | Gatilho em ADR-0006 §12 |
| A3 | Verificabilidade por varredura so alcanca artefato **novo**: 76 do acervo nao declaram os cinco campos | Media | Aceito; alternativa era migrar 76 arquivos |
| A4 | Catalogo mestre e ponto unico de falha de manutencao, sem automacao possivel nesta fase | Media | RG-03 + verificacao a cada C2/C3 |
| A5 | `IDX` composto: `governance/README.md` indexa tres entidades, e a regra previa uma | Baixa | Regra de indice composto — **corrigida nesta revisao** |
| A6 | Entidade E-08 passa a ter **dois prefixos** (`FIT`, `REV`) | Baixa | Verificado contra LX-08: nao ha violacao |
| A7 | FND-10 acrescenta 694 linhas ao acervo que se propoe a economizar | Media | Perfil por recorte; medido em FIT-2026-002 |

**Correcoes aplicadas durante esta revisao:** duas — §0.

---

## 0. Divergencia corrigida durante a revisao

| # | Divergencia | Correcao |
|---|---|---|
| D2 | FND-10 §2.2 fixava a obrigacao dos cinco campos em **"a partir de 2026-07-28"**. Como **todo** o acervo foi criado nessa data, a regra tornaria os 76 artefatos anteriores nao conformes — contradizendo a promessa de migracao zero de §2.3 e o criterio C5 da propria decisao | A data de corte passa a ser a **vigencia** de FND-10, que depende da ratificacao (§5.4). Os artefatos desta missao declaram os campos por **demonstracao**, nao por obrigacao |
| D1 | FND-10 §4.7 declarava que a entidade de um indice e "a entidade que indexa", no singular. **`governance/README.md` indexa tres** — `EXC`, `INC` e `FIT` — e `README.md` da raiz indexa o acervo inteiro. A regra nao previa o caso composto | Acrescentada regra **IX-03**: indice pode indexar mais de uma sequencia quando co-localizadas; a entidade e o **conjunto** indexado, e o contador oficial de cada sequencia permanece unico |

---

## 1. As tres correcoes obrigatorias foram executadas?

### 1.1 Autoverificacao de `CAP-governanca` — **executada**

| Verificacao | Resultado |
|---|---|
| Rito aplicavel | **C2, Tipo 2** — [ADR-0005](../decisions/ADR-0005-proibicao-de-autoverificacao.md), com RFC dispensada por alternativa unica e concordancia escrita de DEP-GOV |
| Independencia respeitada | **Sim.** Proponente DEP-QAR; DEP-GOV atuou **so como guardiao de forma**, declarando-se impedido; aprovacao de DEP-EXE |
| Causa corrigida, nao so ocorrencia | **Sim.** RM-06b em FND-09 §6.3 proibe o par reflexivo em qualquer estrato; RL-05b em FND-08 §5.2 apenas **aponta** para ela, sem reescrever (MM-01) |
| Redacao corrigida | **Sim** — `capabilities/README.md` §5 e `CAP-governanca.md` §9 |
| Lacuna fechada | **Sim.** Quem verifica o produto de DEP-GOV esta nomeado: revisor independente da mudanca e, em materia constitucional, o Soberano |
| Alternativa perigosa recusada | **Sim.** `CAP-qualidade` verificar `CAP-governanca` violaria RL-05, porque ja **depende dela** (mapa §4, nivel 2). Recusada com fundamento |

**Verificacao adicional:** varredura das 23 Cartas por relacoes `verifica` reflexivas.
`CAP-qualidade` e `CAP-seguranca` nomeiam explicitamente as verificadas e **nao se incluem**.
Nenhuma outra ocorrencia.

### 1.2 Ratificacao de ADR-0001 a ADR-0004 — **verificada e registrada**

| Verificacao | Resultado |
|---|---|
| Os quatro foram examinados | **Sim.** Os quatro invocam determinacao **anterior** ao texto ratificado; os quatro mantem "Confirmado apos leitura?" **em branco** |
| Ratificacao inferida de instrucao generica | **Confirmado nos quatro** |
| Registrado sem editar ADR historico | **Sim** — [INC-2026-001](../governance/incidents/INC-2026-001-ratificacao-inferida.md); nenhum dos quatro arquivos foi tocado (LV-04 e determinacao expressa) |
| Pendencia visivel | **Sim** — coluna `Ratificacao` no indice de decisoes; campo `ratificacao: pendente` em FND-01, FND-03, FND-04, FND-08, FND-09 e FND-10 |
| Causa corrigida | **Sim, em tres frentes:** F1 compreensao (LM-02 a LM-06); F2 instrumento (auditoria de eficacia de ratificacao, FND-04 §8); F3 norma (CV-09 separa obter de registrar) |
| Precedente rompido na pratica | **Sim.** [ADR-0006](../decisions/ADR-0006-adocao-do-enterprise-artifact-framework.md) §14 tem o campo **vazio** e permanece em `aprovado`, nao `ativo` |
| Aprendizado gravado | **Sim** — [MEM-APR-0001](../memory/aprendizado/MEM-APR-0001-ratificacao-por-precedente.md), primeiro registro da camada APR |

> **Achado A1.** A pendencia alcanca **seis** decisoes C3/Tipo 1 — as quatro originais mais
> ADR-0006 e, por derivacao, tudo que delas depende. Nenhum componente foi criado, entao o
> efeito pratico esta contido ao corpo normativo. **Somente o ato do Soberano encerra.**

### 1.3 Nenhuma ontologia separada — **cumprido**

| Verificacao | Resultado |
|---|---|
| Ontologia formal criada? | **Nao.** Nenhum modelo de conceitos, propriedades ou inferencia |
| Canon Semantico criado? | **Sim** — FND-10 §3: vocabulario controlado com mapeamento tipo → entidade |
| Distincao declarada? | **Sim** — §3.1 contrasta os dois em quatro dimensoes |
| Gatilhos de promocao definidos? | **Sim** — G1 ambiguidade, G2 consulta relacional, G3 automacao real |
| Algum gatilho observado? | **Nenhum.** G3 e impossivel: nao existe codigo nem infraestrutura |
| FND-09 fornece semantica suficiente? | **Sim** — CS-01 mapeia os 33 tipos as 21 entidades sem lacuna |

---

## 2. Existe duplicacao?

**Nao. Tres riscos examinados individualmente.**

### 2.1 FND-10 × FND-03

| Conceito | FND-03 | FND-10 | Duplica? |
|---|---|---|---|
| Frontmatter | Define os 15 campos | **Acrescenta 5**, nao repete os 15 | Nao |
| Estados | Define os 8 e o grafo | Define as **operacoes** que produzem transicoes | Nao |
| Localizacao | Arvore canonica | Coluna Local na matriz §10.3 — **referencia**, nao arvore paralela | **Tensao registrada** |
| Tipos | Definicao canonica de 16 componentes | Tipos **documentais**, granularidade menor | Nao |

> **Tensao em Localizacao:** a matriz §10.3 lista o diretorio de cada tipo, informacao que
> tambem esta em FND-03 §7. Nao e duplicacao de definicao — a matriz cruza quatro dimensoes
> e o diretorio e uma delas —, mas **e informacao repetida**. Registrado como ressalva no
> Fitness Check, com correcao proposta: substituir o valor por referencia a FND-03 §7 na
> proxima revisao de FND-10.

### 2.2 FND-10 × FND-09

| Conceito | Verificacao |
|---|---|
| Relacoes | §7.1 **mapeia** os nove verbos as dez relacoes de FND-09 §6.1; nao cria relacao |
| Autoridade | §6.1 declara explicitamente que a matriz nao e reproduzida, e que em conflito prevalece FND-09 |
| Perfis de ciclo | §5.1 declara que os quatro perfis de FND-09 §7.2 valem sem redefinicao |

**Verificacao aplicada:** FND-10 nao contem tabela de entidades, de relacoes por par, de
estados nem de autoridade por entidade. Todas remetem por link.

### 2.3 Motor de especializacao × os tres testes existentes
FND-10 §9.1 delimita explicitamente: quatro motores, quatro objetos — componente (FND-04
§6.2), competencia (FND-08 §7), tipo de entidade (FND-09 §11.1), **documento** (FND-10 §9).
Os sinais S1–S7 sao proprios de documento: cadencia de alteracao, precisao de recuperacao,
custo em linhas. **Sem sobreposicao.**

---

## 3. Existe tipo generico demais, ou que deveria ser abstraido?

**Um caso de cada. Ambos resolvidos.**

### 3.1 `Evaluation` — generico demais, foi decomposto
A missao listava `Evaluation` como tipo. Ele nao e tipo: e **nome guarda-chuva** de duas
formas com perguntas distintas — `FIT` pergunta se ficou mais apto a evoluir; `REV` pergunta
se esta correto. Adota-lo como tipo unico teria forcado um veredito unico, revertendo por via
oblqua o que ADR-0004 §6 recusou. **Decomposto em dois tipos documentais da mesma entidade.**

### 3.2 `Checklist` — abstraido para secao
Tres instancias observadas — em `TPL-documento`, nos ADRs e em `TPL-fitness-check` —, **todas
como secao de outro artefato**. Nenhuma existe isolada. Promove-lo a tipo criaria artefato sem
pergunta propria (MT-02). **Recusado com destino declarado**, e gatilho armado: reuso por 3+
tipos com versao propria.

### 3.3 Achado A6 — dois prefixos para uma entidade
E-08 passa a ter `FIT` e `REV`. Verificado contra **LX-08**: *"Prefixo de tipo e obrigatorio
no ID e nunca e reutilizado por outro tipo."* A regra proibe **um prefixo servir a dois
tipos**; aqui ocorre o inverso — dois prefixos, dois tipos documentais, uma entidade.
**Nao ha violacao.** Registrado como tensao de baixa severidade: se um terceiro tipo
documental de parecer aparecer, a entidade merece reexame pelo Teste de Entidade.

---

## 4. Existe relacionamento circular?

**Nao. Um caso aparente examinado e refutado.**

### 4.1 Caso aparente: FND-10 ↔ catalogo mestre
FND-10 §10.4 obriga a existencia do catalogo; o catalogo classifica FND-10. Parece ciclo.

**Nao e**, porque as duas arestas sao de tipos diferentes:

| Aresta | Relacao | Admite ciclo? |
|---|---|---|
| Catalogo → FND-10 | R-09 `registra` | **Sim** (RM-09, §6.1) |
| FND-10 → catalogo | **Nenhuma.** RG-02 e obrigacao normativa, nao dependencia: FND-10 continua valendo integralmente se o catalogo for apagado — o que se perde e a localizabilidade dos artefatos, nao a norma | — |

Aplicado o criterio de FND-09 §9.4: *se o destino desaparecer e a origem continuar valendo, o
vinculo nao e dependencia*. **Sem ciclo.**

### 4.2 Verbos de linhagem
`deriva-de`, `implementa`, `depende-de` e `substitui` mapeiam a R-04 e R-08, ambas aciclicas
por PD-01 e por monotonicidade temporal. `consome`, `produz`, `valida` e `evidencia` mapeiam a
R-05, R-06 e R-09, que **admitem ciclo por desenho**. `restringe` esta fora do grafo.
**Nenhum ciclo proibido possivel.**

### 4.3 `valida` reflexivo
Proibido por LN-06, que aplica RM-06b. Verificado: **REV-ARTIFACT nao valida a si proprio** —
seu revisor declarado e DEP-EXE, e seu objeto e FND-10, produzido por DEP-GOV.

---

## 5. Existe dependencia proibida?

**Nenhuma.** Verificacao das doze de FND-09 §9.2 contra os artefatos desta missao:

| # | Verificacao | Resultado |
|---|---|---|
| PD-01 | Ciclo em `depende-de` | ✓ §4 |
| PD-02 | Norma depender de componente | ✓ FND-10 depende so de FND-01/03/04/09 — mesmo estrato |
| PD-03 | Capability depender de estrutura | ✓ ADR-0005 nao criou relacao de Capability; usou papel por mudanca |
| PD-04 | Verificador depender do verificado | ✓ **E a correcao central desta missao**; RM-06b acrescenta o caso reflexivo |
| PD-05 a PD-07 | Subagente, entidade nao vigente, ferramenta externa | n/a — nenhuma instancia |
| PD-08 | Norma depender de memoria | ✓ FND-10 §5.4 **cita** MEM-APR-0001 como origem da licao, sem dela depender |
| PD-09 | Instrumento depender de instrumento futuro | ✓ FND-10 referencia ADR-0006, **simultaneo** |
| PD-10 a PD-12 | Produto, ascendente, agente cruzado | ✓ / n/a |

### 5.1 Verificacao de independencia dos papeis nesta missao

| Artefato | Autor | Revisor | Aprovador | Conflito? |
|---|---|---|---|---|
| ADR-0005 | DEP-QAR | DEP-GOV *(so forma)* | DEP-EXE | **Nao** — DEP-GOV declarou-se impedido |
| FND-10 | DEP-GOV | **DEP-QAR** | SOBERANO *(pendente)* | Nao |
| ADR-0006 | DEP-GOV | **DEP-QAR** | SOBERANO *(pendente)* | Nao |
| INC-2026-001 | DEP-GOV | — | DEP-QAR *(fecha)* | Nao |
| Esta revisao | DEP-QAR | DEP-EXE | DEP-EXE | **Tensao** — revisor e aprovador coincidem |

> **Tensao registrada:** nesta revisao, DEP-EXE acumula revisor e aprovador. FND-04 §3.1
> proibe Proponente = Aprovador e Executor = Verificador; **nao** proibe Revisor = Aprovador.
> Aceitavel pela norma vigente, e registrado porque a estrutura so tem tres papeis
> disponiveis nesta fase. Gatilho: quando existirem agentes, separar.

---

## 6. O framework classifica 100% do acervo?

**Sim — 85 de 85 artefatos**, verificado no [catalogo mestre](../governance/artifact-registry.md).

| Situacao antes | Situacao depois |
|---|---|
| 10 artefatos sem tipo declarado (8 `IDX` + 2 `REV`) — **13% do acervo** | 0 |
| Tipos documentais declarados | 33, sobre 21 entidades |
| Entidades novas criadas | **0** — universo permanece em 21 |
| Arquivos do acervo reescritos para caber no framework | **0** |

### 6.1 Como os dois casos dificeis foram resolvidos

| Caso | Resolucao | Teste aplicado |
|---|---|---|
| `IDX` | Registro oficial da entidade que indexa — o contador que FND-03 §2.3 ja atribuia a DEP-GOV | **Falha TE-2**: nao persiste alem do que indexa; conteudo e projecao. Logo, nao e entidade |
| `REV` | Segundo tipo documental de `FIT` | **Passa TE-1 a TE-7** e mesmo assim nao vira entidade: `FIT` ja responde a mesma pergunta, e criar violaria **MT-02** |

> A assimetria e deliberada e correta: um falha no teste, o outro passa e e recusado por
> duplicar pergunta. Registrar as duas razoes distintas evita que a decisao pareca arbitraria.

---

## 7. Ha reducao de duplicacao e de custo de contexto sem governanca desnecessaria?

### 7.1 Duplicacao — reducao verificavel

| Medida | Antes | Depois |
|---|---|---|
| Templates universais | 1 | **1** — `TPL-documento` estendido, nao duplicado |
| Templates especializados criados | — | **0** — 19 de 19 vigentes passam em T1–T4 |
| Arquivos auxiliares por artefato | — | **0** (RG-05) |
| Regras de verificacao reflexiva escritas | — | **1**, em FND-09; FND-08 apenas aponta |
| Definicoes reescritas de outro documento em FND-10 | — | **0** |

### 7.2 Custo de contexto — reducao **calculada**, nao observada

| Medida | Valor |
|---|---|
| Acervo total | **18.916 linhas em 85 artefatos** *(medido apos esta missao)* |
| Nucleo obrigatorio | **1.087 linhas integrais + 2 recortes** |
| Proporcao | **5,7% do acervo** |
| Trabalhos executados sob os perfis | **0** |

> **Achado A2.** A reducao e a razao entre o nucleo declarado e o acervo — **nao** a medicao
> de um trabalho real. Nenhum papel executou tarefa carregando apenas o nucleo. O numero e
> honesto como calculo e **nao e evidencia de eficacia**.

### 7.3 Governanca desnecessaria — quatro verificacoes

| Pergunta | Resposta |
|---|---|
| Quantos arquivos existentes precisam ser reescritos? | **Zero** — valor padrao + catalogo (§2.3) |
| Quantos campos novos exigem trabalho manual por artefato? | **Um** — `resumo`, e apenas para artefato **novo** |
| Quantos artefatos auxiliares por documento? | **Zero** (RG-05) |
| Quantos atributos derivaveis foram tornados obrigatorios? | **Zero** — AC-01 os proibe explicitamente |

> **Achado A3.** O preco de nao migrar e que a verificabilidade por varredura — criterio C6 —
> so alcanca artefato **novo**. Os 76 do acervo continuam exigindo leitura para checar LV-03.
> Tradeoff aceito e declarado; a alternativa era reescrever 76 arquivos.

---

## 8. Alguma regra deve virar norma constitucional?

**Uma candidata nova; a de MT-01 permanece pendente da revisao anterior.**

| Candidata | Avaliacao |
|---|---|
| **LM-02** — ratificacao ausente e impedimento, nao ressalva | **Forte candidata.** Deriva diretamente de PI-06 e GV-05, ja constitucionais. **Recomendacao: nao elevar agora** — a regra nasceu hoje, de um unico incidente, e elevar antes de ser exercida repetiria o erro de MEM-APR-0001: transformar em clausula petrea o que ainda nao foi testado. **Gatilho:** segunda ocorrencia de ratificacao inferida, ou primeira ratificacao efetiva registrada sob CV-09 |
| **CE-01** — proibicao de carregamento integral | **Nao elevar.** Deriva de PI-14, ja constitucional; elevar duplicaria norma (LX-07) |
| **MT-01** — universo fechado | Pendente desde a revisao do Meta Model, com prazo em 2027-01-28. **Sem alteracao** |

> Registrado como decisao de nao decidir (FND-07 §9), com prazo, gatilho e dono: DEP-GOV,
> 1a revisao da Fundacao.

---

## 9. Conclusao

| Criterio de conclusao da missao | Resultado |
|---|---|
| 100% dos artefatos classificados | ✓ **85 de 85**, no catalogo mestre |
| Regras sem conflito | ✓ Duas tensoes registradas (§2.1 Localizacao, §5.1 papeis), nenhuma contradicao |
| Links validos | ✓ Varredura do repositorio: **0 quebrados** |
| Rastreabilidade origem → estado → substituicao | ✓ LN-07 a LN-09; cadeia percorrivel em todos os artefatos desta missao |
| Reducao de duplicacao | ✓ Verificavel (§7.1): 0 templates novos, 0 arquivos auxiliares, 0 definicoes reescritas |
| Reducao de custo de contexto | ⚠ **Calculada, nao observada** (§7.2, achado A2) |
| Sem governanca desnecessaria | ✓ Zero migracao, um campo manual, zero atributo derivavel obrigatorio (§7.3) |
| `Artifact` permanece arquetipo | ✓ Nenhuma entidade criada; universo em 21 |
| Ontologia nao criada | ✓ Canon Semantico com tres gatilhos, **nenhum observado** |

**Parecer de DEP-QAR:** o Artifact Framework esta apto a servir de base para a fase seguinte.
Os sete achados sao registrados com dono e gatilho; **nenhum bloqueia a adocao**.

**Ressalva registrada (PI-10):** o framework **nao esta em vigor**. FND-10 e ADR-0006
permanecem em `aprovado`, aguardando ato explicito do Soberano — e essa e a primeira aplicacao
correta da regra que a propria missao mandou instituir.

---

## 10. Achados que geram acao futura

| # | Acao | Quando | Responsavel |
|---|---|---|---|
| A1 | Obter ato de ratificacao do Soberano sobre ADR-0001 a ADR-0004 e ADR-0006 | Proxima interacao com o Soberano | SOBERANO; registro por DEP-QAR |
| A2 | Medir o custo real de um trabalho executado sob os perfis | Primeiro trabalho apos a ratificacao | DEP-KMS |
| A3 | Avaliar se vale migrar o acervo para os cinco campos | 1a revisao estrutural | DEP-GOV + DEP-EXE |
| A4 | Verificar sincronia do catalogo mestre com o acervo | A cada C2/C3 | DEP-GOV |
| A5 | *(corrigido nesta revisao — IX-03)* | — | — |
| A6 | Reexaminar E-08 pelo Teste de Entidade se surgir terceiro tipo de parecer | Por evento | DEP-QAR |
| A7 | Substituir a coluna Local da matriz §10.3 por referencia a FND-03 §7 | 1a revisao de FND-10 | DEP-GOV |
| A8 | Avaliar elevacao de LM-02 a norma constitucional | 2a ocorrencia ou 1a ratificacao sob CV-09 | DEP-GOV |
