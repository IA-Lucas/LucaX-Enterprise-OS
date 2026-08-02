---
id: RFC-0026-primeira-spec-governanca-de-dado-pessoal-do-nxtrack
titulo: Criar a primeira Spec do acervo sobre a lacuna LM-6(a) do nXtrack — em que recorte e sob que classe
tipo: rfc
versao: 1.0.0
status: aprovado
camada_memoria: nao-aplicavel
autor: DEP-PRD
proprietario: DEP-PRD
aprovador: DEP-EXE
criado_em: 2026-08-02
atualizado_em: 2026-08-02
revisao_prevista: null
decisoes_relacionadas: [ADR-0021, ADR-0030, ADR-0031]
substitui: []
substituido_por: null
classe_mudanca: C2
prazo_analise: 2026-08-02
---

# RFC-0026: Criar a primeira `Spec` do acervo sobre a lacuna `LM-6(a)` do nXtrack

## Proposito

Submeter a analise **duas** perguntas que a Missao 1.13.5 nao pode resolver por presuncao: qual
**recorte** a primeira `Spec` real do acervo deve ter sobre a lacuna `LM-6(a)` de
[`PRO-nxtrack`](../products/nxtrack/carta.md), e sob qual **classe de mudanca** ela e criada — ja
que o piso que [`FND-04 §6`](../foundation/04-governanca.md) fixa para `Spec` produz, medido,
**aprovacao nula** por [`FND-04 §3.1`](../foundation/04-governanca.md).

## Escopo

| Item | Definicao |
|---|---|
| **Abrange** | O recorte da primeira `Spec` · a classe e o tipo de reversibilidade dessa criacao · a `Capability` e o Departamento custodiante a que ela se vincula (`SF-07`) |
| **Nao abrange** | Qualquer alteracao no nXtrack · qualquer parecer juridico · a decisao de **expor dado vivo ao exterior**, que e do SOBERANO (`FND-01 §7.3`) · `E2`, `Q3`, `Q4` e `RD-88` · emenda de `FND-11` ou de qualquer fundacional |
| **Subordina-se a** | `FND-01` *(nivel 1)* · `FND-03`, `FND-04`, `FND-07`, `FND-09`, `FND-10` e `FND-11` *(nivel 2)* |

## Responsaveis

| Papel | Quem |
|---|---|
| Proponente | **DEP-PRD** — `FND-09 §8.2`, linha `SPC`, *propoe/cria* |
| Areas que devem se manifestar | **DEP-QAR** *(custodio de `CAP-juridico` e de `CAP-seguranca`; verificacao de risco)* · **DEP-ENG** *(revisor de `SPC`; executor previsto)* · **DEP-GOV** *(guardiao: valida classe e forma)* |
| Aprovador | **DEP-EXE**, com parecer de DEP-GOV — `FND-04 §2`, classe `C2` |
| Prazo de manifestacao | 2026-08-02 — mesma missao, por `CV-02` *(o registro precede a execucao)* |

---

## 1. Situacao atual — fatos verificaveis

| # | Fato | Fonte |
|---|---|---|
| `SA-1` | **`PRO-nxtrack` esta em vigor** — `status: ativo`, `ratificacao: ratificada`, criado pelo item **III** do nono ato soberano | [`products/nxtrack/carta.md`](../products/nxtrack/carta.md) · [`MSG-2026-0009`](../memory/operacional/MSG-2026-0009-ato-soberano-admissao-do-nxtrack.md) |
| `SA-2` | **`GO-TO-SPECS` esta LIBERADO e EXERCIVEL** desde 2026-08-01, e o `DoR` de `SF-23` item (9) **passa** | [`artifact-registry §2`](../governance/artifact-registry.md) · [`PT-2026-016 §3`](../governance/relatorio-transicao-2026-08-01-fechamento-rd-33.md) |
| `SA-3` | **`0` `Spec`s existem no acervo.** As **32** regras `SF-01`–`SF-32` sao **determinadas, nao observadas** — limite `L1` declarado pela propria sede | [`FND-11 §14`](../foundation/11-framework-specifications.md) |
| `SA-4` | **O ato fixou a materia da primeira `Spec`: `LM-6(a)`, com prioridade sobre as demais de `LA-7`** — `RD-71` *(custodia)* e `RD-74` *(`VC-03`)* ficam depois | [`MSG-2026-0009 §2`, `DC-3`](../memory/operacional/MSG-2026-0009-ato-soberano-admissao-do-nxtrack.md) |
| `SA-5` | **`LM-6(a)` reproduz: `0` ocorrencias** de `LGPD`, `GDPR`, `ANPD`, *"dados pessoais"*, *"politica de privacidade"* e *"termos de uso"* nos **183** arquivos rastreados sob o `tree` `b9b36be9…fb4b` **e** na arvore de trabalho de **262** arquivos. Padrao mais largo que o publicado *(singular e forma acentuada)*, e ainda assim `0` | Item 0 da missao, §3 |
| `SA-6` | **Ha dado pessoal por desenho:** `usuarios(nome, nome_norm, senha_hash, sal)`, com `biblioteca_faixas` e `sessoes` em `ON DELETE CASCADE` | `prototipo/usuarios.py:37-70` |
| `SA-7` | **A tabela do aprendizado coletivo nao tem coluna de usuario.** `feedback_recomendacao(origem_norm, destino_norm, tipo, criado_em)`; `carregar_feedback` le **sem clausula por usuario**; `alternar` apaga e insere **globalmente** | `prototipo/feedback.py:29-95` |
| `SA-8` | **Nao existe caminho de exclusao de conta em codigo de producao.** `DELETE FROM usuarios` tem **1** ocorrencia, **dentro de um teste** | `prototipo/tests/test_usuarios.py:393` |
| `SA-9` | **O candidato JA declarou oito regras de privacidade** em `spec-tecnica-v1.md §24`, numa unica frase, **sem criterio de aceite e sem implementacao verificada** — inclusive *"permitir exclusao de conta/dados"* e *"oferecer opt-out de treinamento"* | `spec-tecnica-v1.md:777` |
| `SA-10` | **A exposicao esta contida hoje:** porta em **loopback**, `"127.0.0.1:8501:8501"` | `compose.beta.yml:13` |

## 2. Problema

**A lacuna nao e de intencao — e de obrigacao verificavel.** O candidato escreveu o que quer
(`SA-9`) e nao escreveu **o que precisa ser verdadeiro, sob que condicao, e por qual evidencia
isso sera aceito** — que e exatamente o que `SF-01` define como `Spec`. Enquanto assim for:

| # | Consequencia, e para quem |
|---|---|
| `PB-1` | **DEP-ENG nao tem contra o que construir.** Oito regras em prosa, `0` criterios de aceite, `0` metodos de verificacao |
| `PB-2` | **DEP-QAR nao tem contra o que vetar.** Sem requisito, nao ha nao conformidade — ha opiniao |
| `PB-3` | **O SOBERANO nao tem contra o que decidir a exposicao.** `FND-01 §7.3` poe *"exposicao de dado vivo ao exterior"* na sua competencia, e hoje **nao existe o conjunto de condicoes** que essa decisao pressupoe |
| `PB-4` | **O titular nao tem como sair.** `SA-7` + `SA-8`: nao ha caminho de exclusao, e a contribuicao ao aprendizado coletivo **nao e atribuivel** a ninguem, logo nao e removivel nem quando a conta for apagada |

**Evidencia do problema:** o item 0 desta missao, medido por ferramenta com **controle
positivo** aplicado antes de se acreditar em qualquer zero.

## 3. Pergunta de decisao

> **A primeira `Spec` do acervo deve ser criada agora sobre `LM-6(a)` de `PRO-nxtrack`; em que
> recorte; e sob qual classe de mudanca — dado que o piso `C1` de `FND-04 §6` produz aprovacao
> nula por `FND-04 §3.1`?**

## 4. Criterios de avaliacao

> Preenchidos **antes** de examinar as opcoes (`CD-01`).

| # | Criterio | Peso | Como se mede |
|---|---|---|---|
| `CR-1` | **A aprovacao resultante e valida** — nenhum acumulo de papel incompativel | Alto | Confronto papel a papel com `FND-04 §3.1`. Acumulo ⇒ aprovacao **nula** (`LV-03`) |
| `CR-2` | **Obedece a ordem que o ato fixou** — `LM-6(a)` antes de `RD-71` e `RD-74` | Alto | `DC-3` de `MSG-2026-0009` |
| `CR-3` | **Nao usurpa competencia alheia** — em especial a do SOBERANO sobre exposicao de dado vivo | Alto | `0` requisitos que autorizem exposicao; `FND-01 §7.3`, `LV-08`, `SF-03` |
| `CR-4` | **Exercivel hoje, sem `S2`** | Alto | `RD-88` declara a `Spec` de materia nao-produto **inexistente e deferida** |
| `CR-5` | **Produz o entregavel que so a primeira `Spec` produz** — a revisao empirica de `FND-11` | Medio | Gatilho de revisao de `FND-11 §15`; limites `L1` e `L2` |
| `CR-6` | **Custo de contexto declarado e medido** | Medio | `CE-02`, `CE-04` — linhas por `wc -l`, com data |

## 5. Opcoes

### Opcao A — `Spec` de produto sobre `LM-6(a)`, classe **`C2 · Tipo 2`**

| Campo | Conteudo |
|---|---|
| Descricao | Criar `SPC-001` em `products/nxtrack/specs/`, vinculada a **`CAP-juridico`** *(ativa)* e custodiada por **DEP-QAR**, declarando o que precisa ser verdadeiro sobre dado pessoal no nXtrack **antes de qualquer exposicao a usuario externo**, com criterio de aceite verificavel por terceiro. Classe **`C2`** por `FND-01 §7.1.6` *(na duvida, a mais restritiva)*, com a duvida **fundada e medida** |
| A favor | Unica classe da matriz de `SF-10` em que **nenhum papel se acumula**: proponente DEP-PRD ≠ aprovador DEP-EXE ≠ revisores DEP-ENG/DEP-QAR ≠ guardiao DEP-GOV. Satisfaz `CR-1` a `CR-5` |
| Contra | **Custa mais**: `C2` exige `RFC → ADR` (`FND-04 §2`) e **`FIT`** (`SF-24`, item 9). Cinco artefatos onde a leitura ingenua previa um |
| Custo / Risco | 1 `RFC` + 1 `ADR` + 1 `SPC` + 1 `FIT` + 1 `PT`, mais catalogo, projecoes `M3` e baseline. Risco: **super-classificar** e criar precedente de que toda `Spec` custa cinco artefatos |
| Quem e afetado | DEP-PRD *(autor)* · DEP-ENG e DEP-QAR *(revisores)* · DEP-EXE *(aprova)* · DEP-GOV *(registra)* · DEP-OPS *(operacao futura)* |

### Opcao B — `Spec` de produto sobre `LM-6(a)`, classe **`C1 · Tipo 2`** *(o piso literal)*

| Campo | Conteudo |
|---|---|
| Descricao | Idem a Opcao A, mas mantendo a classe que `FND-04 §6` fixa na linha *Spec*: **`C1`** |
| A favor | E o texto literal de `FND-04 §6`. Custa **dois** artefatos *(a `Spec` e o registro)*, nao cinco. `C1` dispensa `RFC`, `ADR` e `FIT` |
| Contra | **A aprovacao e nula, e isto e medido, nao suposto.** No `C1 · T2` de `SF-10 §5`, *Proposta* = **DEP-PRD** e *Aprovacao* = **proprietario + revisor**; `FND-09 §8.2` linha `SPC` poe DEP-PRD como quem **propoe** e quem **aposenta** *(logo, proprietario)*. Resulta **Proponente = Aprovador**, que `FND-04 §3.1` proibe em termos absolutos: *"Acumulo indevido de papeis torna a aprovacao **nula** (`LV-03`)"* — e `LV-03` e **Linha Vermelha** de `FND-01`, nivel **1** |
| Custo / Risco | Custo baixo, risco **maximo**: entrega um artefato cuja aprovacao e nula desde a origem, e cria o primeiro artefato do acervo a reprovar no criterio `AC-03`, hoje em **`0` violacoes** |
| Quem e afetado | Todos os acima, **e todas as `Spec`s futuras**, por precedente |

### Opcao C — Politica organizacional de dado pessoal *(materia nao-produto)*

| Campo | Conteudo |
|---|---|
| Descricao | Escrever uma norma interdepartamental de dado pessoal, valida para todo o acervo, em vez de uma `Spec` de produto |
| A favor | Resolveria de uma vez `FG-11` de `PT-2026-014` — *"`0` artefato governa dado pessoal de usuario final"* — e nao so o nXtrack |
| Contra | **Impossivel hoje, e a impossibilidade esta registrada.** `RD-88` declara que a `Spec` de materia **nao-produto** continua **inexistente**: `FND-03 §3.6` e `FND-10 §4.4` so preveem `products/<slug>/specs/`, e `FND-04 §6` exige *"Produto existe"*. So **`S2`** cria a categoria, e `S2` esta **DEFERIDA** por decisao do proprio SOBERANO (`PT-2026-009 §1`, decisao 7) |
| Custo / Risco | 1 `RFC` `C3` + 1 `ADR` `C3` + ato soberano. **Reprova `CR-4` de forma binaria** |
| Quem e afetado | Todo o acervo — e por isso mesmo e do SOBERANO, nao desta missao |

### Opcao Z — Nao fazer nada

| Campo | Conteudo |
|---|---|
| Consequencia de manter o estado atual | `LM-6(a)` continua em **`0`**. `PB-1` a `PB-4` permanecem. **`GO-TO-SPECS` fica exercivel e nao exercido** — o mesmo estado que `FIT-2026-015` usou, com fundamento, para recusar `GO-TO-SKILLS`: *"o portao anterior foi liberado e nao pode ser exercido"*. A sequencia **para em 1.13.5** |
| Custo da inacao | As **32** regras seguem **determinadas e nao observadas** (`L1`), e `FND-11 §15` nunca dispara o gatilho de revisao. **O risco de `R2` da Carta — aprendizado coletivo entre bibliotecas separadas, severidade Alta — segue sem mitigacao escrita**, contido **so** pelo loopback (`SA-10`), que e configuracao e nao norma |
| Por que nao venceu | Descumpre `CR-2` *(o ato fixou a materia e a prioridade)* e `CR-5`. **Nao e alternativa de palha:** e a unica opcao com custo **zero** de contexto, e seria a correta se a exposicao fosse impossivel — mas `POST /sessao/criar` existe e o cadastro e publico (`LM-5`), de modo que a contencao e **operacional e reversivel por uma linha de `compose`** |

## 6. Recomendacao do proponente

**Opcao A.** Ela e a unica que satisfaz `CR-1` **sem** depender de leitura benevolente: a
colisao entre o `C1 · T2` de `SF-10` e `FND-04 §3.1` **foi medida celula a celula**, e `C2` e a
**menor** classe da matriz em que ela desaparece. A escolha **nao e preferencia por rigor**: e a
aplicacao de `FND-01 §7.1.6` a uma duvida que tem fundamento citado, e a duvida so existe porque
a primeira `Spec` real **exerceu** a matriz em vez de le-la.

**O custo maior e consequencia da Opcao A, e esta declarado:** cinco artefatos. A alternativa
barata (**B**) custa dois e entrega aprovacao nula — **o barato aqui e nulo, nao barato**.

## 7. Impacto previsto

| Dimensao | Impacto |
|---|---|
| **Departamentos** | DEP-PRD *(autor)* · DEP-ENG + DEP-QAR *(revisores)* · DEP-EXE *(aprova e libera `QG-1`)* · DEP-GOV *(guardiao e registro)* · DEP-OPS *(alcancado pelos requisitos de operacao)* |
| **Componentes** | **`PRO-nxtrack`** ganha sua primeira `Spec`. **`0`** bytes no produto: a `Spec` declara, nao implementa |
| **Normas afetadas** | **Nenhuma emendada.** `FND-01` a `FND-11` com **`0`** bytes. `FND-11` e **exercido**, e o exercicio gera **achado**, nunca emenda automatica |
| **Camadas de memoria** | `produto` *(a `Spec`)* · `estrategica` *(o `ADR`)* · `operacional` *(o `PT`)* |
| **Ganho `PI-14` pretendido, e o sinal que o comprova** | **Organizacao e reducao de contexto:** um requisito passa a ser enderecavel por `<SPC-id> RQ-nn` sem carregar o documento (`SF-31`). **Sinal ja observado:** `PB-1` e `PB-2` — DEP-ENG e DEP-QAR nao tem, hoje, contra o que construir e contra o que vetar. **O ganho sera reavaliado** quando o primeiro requisito for consumido por uma missao de construcao |

## 8. Riscos

| # | Risco | Impacto | Mitigacao |
|---|---|---|---|
| `RI-1` | **Super-classificar**: `C2` onde `C1` bastaria, criando precedente caro para toda `Spec` | Medio | A justificativa e **especifica da colisao medida**, nao generica. `ADR-0031 §6` declara que **`C1` volta a ser o piso** assim que a colisao for sanada por quem tem competencia — o SOBERANO, via `FND-11` |
| `RI-2` | **A `Spec` virar parecer juridico disfarcado** | **Alto** | `CAP-juridico` declara na propria fonte *"identificar quando o assunto exige assessoria humana qualificada"*. A `Spec` **remete** e nao qualifica: `0` requisitos que afirmem enquadramento legal |
| `RI-3` | **Usurpar a competencia do SOBERANO** sobre exposicao de dado vivo | **Alto** | Todos os requisitos de exposicao sao **negativos** (`SF-25`) — restringem, nunca autorizam. `§4` da `Spec` declara que satisfaze-la **nao** autoriza publicar |
| `RI-4` | **Especificar o "como"** e ser devolvida por `SF-02` | Medio | Revisao de DEP-ENG e DEP-GOV sobre a tabela de requisitos; `0` escolhas de tecnologia |
| `RI-5` | **Esta RFC estar errada quanto a colisao** | Medio | A colisao e **reproduzivel por leitura**: `SF-10 §5` linha *Proposta* e linha *Aprovacao*, coluna `C1 · T2`, contra `FND-04 §3.1`. Terceiro decide sem consultar o autor |

## 9. Perguntas em aberto

| # | Pergunta | Bloqueia esta RFC? |
|---|---|---|
| `PA-1` | **A colisao `C1` × `FND-04 §3.1` se corrige emendando `FND-11` ou `FND-09 §8.2`?** | **Nao.** Fica como achado `RD-91`, dono **SOBERANO** — `FND` so se emenda com ratificacao (`LM-02`), e o congelamento veda gerar missao |
| `PA-2` | **Quantos titulares existem hoje no nXtrack?** | **Nao.** Nao medido, e declarado nao medido: abrir banco e proibido. A `Spec` nao depende do numero |
| `PA-3` | **Ha enquadramento legal aplicavel, e qual?** | **Nao, e nao e desta casa.** A `Spec` declara o que precisa existir; o enquadramento e de assessoria humana qualificada |

## 10. Manifestacoes

| Area | Posicao | Fundamento | Data |
|---|---|---|---|
| **DEP-QAR** | **apoia com ressalva** | Apoia a Opcao A por `CR-1`. **Ressalva:** e custodio de `CAP-juridico` *(materia)* **e** revisor de `SPC` *(tipo)* na mesma mudanca — os dois papeis nao estao em `FND-04 §3.1` como incompativeis, e a concentracao **fica declarada**, nao dissolvida. Achado `RD-92` | 2026-08-02 |
| **DEP-ENG** | **apoia** | Executor previsto. `PB-1` e o proprio problema: sem requisito com criterio de aceite, nao ha o que construir | 2026-08-02 |
| **DEP-GOV** | **apoia** | Guardiao. Valida a classe `C2 · Tipo 2` (`FND-04 §2`) e a forma. Registra que **a classificacao mais restritiva foi aplicada com fundamento medido**, e nao por cautela | 2026-08-02 |
| **DEP-EXE** | **apoia** | Aprovador da classe `C2`. Libera `QG-1` da `Spec` em ato distinto do de aprovacao (`FND-01 §6.2`) | 2026-08-02 |

## 11. Resultado

| Campo | Conteudo |
|---|---|
| **Decisao** | **aceita** — Opcao A |
| **ADR gerado** | [`ADR-0031`](../decisions/ADR-0031-primeira-spec-governanca-de-dado-pessoal-do-nxtrack.md) |
| Se rejeitada, por que | — |
| Se adiada, ate quando | — |
| **Data** | 2026-08-02 |
| **Responsavel** | DEP-PRD *(proponente)* · DEP-EXE *(aprovador)* |
