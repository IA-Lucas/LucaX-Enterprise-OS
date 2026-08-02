---
id: ADR-0031-primeira-spec-governanca-de-dado-pessoal-do-nxtrack
titulo: Criar SPC-001 — a primeira Spec do acervo — sobre a governanca de dado pessoal do nXtrack, em classe C2 Tipo 2
tipo: adr
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-PRD
proprietario: DEP-PRD
aprovador: DEP-EXE
criado_em: 2026-08-02
atualizado_em: 2026-08-02
revisao_prevista: 2027-02-02
decisoes_relacionadas: [ADR-0005, ADR-0018, ADR-0019, ADR-0021, ADR-0022, ADR-0030]
substitui: []
substituido_por: null
classe_mudanca: C2
tipo_decisao: 2
supera: []
superado_por: null
ratificacao: nao-exigida
---

# ADR-0031: Criar `SPC-001` — a primeira `Spec` do acervo — sobre governanca de dado pessoal do nXtrack

## Proposito

Registrar a decisao de **criar a primeira `Spec` real do LucaX Enterprise OS**, sobre a lacuna
`LM-6(a)` de [`PRO-nxtrack`](../products/nxtrack/carta.md), e de faze-lo em classe **`C2 · Tipo
2`** — **acima** do piso `C1` que [`FND-04 §6`](../foundation/04-governanca.md) fixa para `Spec`
—, porque o piso, exercido, produz **aprovacao nula**.

## Escopo

| Item | Definicao |
|---|---|
| **Aplica-se a** | A criacao de `SPC-001` em `products/nxtrack/specs/` · a classe e o tipo dessa criacao · o vinculo a `CAP-juridico` e a DEP-QAR como custodiante da materia |
| **Nao se aplica a** | Qualquer alteracao no nXtrack · a decisao de **expor dado vivo ao exterior**, que permanece do SOBERANO (`FND-01 §7.3`) · a `Spec` de materia **nao-produto** (`RD-88`, `S2` deferida) · `E2`, `Q3`, `Q4` · a classe das `Spec`s **futuras**, que continua sendo funcao do efeito de cada uma (`SF-10`) |
| **Subordina-se a** | `FND-01` *(nivel 1)* · `FND-03`, `FND-04`, `FND-07`, `FND-09`, `FND-10`, `FND-11` *(nivel 2)* |
| **Origem** | [RFC-0026](../rfcs/RFC-0026-primeira-spec-governanca-de-dado-pessoal-do-nxtrack.md) |

## Responsaveis

| Papel | Quem |
|---|---|
| Proponente | **DEP-PRD** — `FND-09 §8.2`, linha `SPC` |
| Revisor independente | **DEP-ENG** + **DEP-QAR** — `FND-09 §8.2`, linha `SPC`; `AC-03` |
| Aprovador | **DEP-EXE**, com parecer de **DEP-GOV** — `FND-04 §2`, `C2` |
| Ratificador | **Nao exigido** — `C2 · Tipo 2` (`FND-04 §2.1`; `SF-10`, coluna `C2 · T2`, linha *Ratificacao*) |
| Executor | **DEP-GOV** *(registro e promulgacao — `FND-04 §4 [7]`)* |

---

## 1. Contexto

O nono ato soberano criou `PRO-nxtrack` e **fixou a materia da primeira `Spec`**: a lacuna
`LM-6(a)` — *"zero ocorrencias de LGPD, ANPD, politica de privacidade e termos de uso, num
produto com nome, `senha_hash` e sal por conta"* —, **com prioridade sobre as demais de `LA-7`**
([`MSG-2026-0009 §2`](../memory/operacional/MSG-2026-0009-ato-soberano-admissao-do-nxtrack.md),
`DC-3`). Em 2026-08-01 a Missao 1.13.4.6 fechou `RD-33` e `GO-TO-SPECS` passou de *liberado e
nao exercivel* a **exercivel**.

**Nada, porem, havia sido exercido.** [`FND-11 §14`](../foundation/11-framework-specifications.md)
declara o limite `L1` na propria fonte: *"Nenhuma `Spec` real existe. Todas as **32** regras sao
**determinadas, nao observadas**"*. Esta decisao e o primeiro exercicio.

**O que o exercicio encontrou, e que a leitura nao tinha encontrado.** Ao montar o quadro de
papeis da criacao — e nao ao ler a matriz — apareceu uma colisao entre duas fontes vigentes:

| Fonte | O que diz | Nivel |
|---|---|---|
| [`FND-11 §5`](../foundation/11-framework-specifications.md), matriz de `SF-10`, coluna **`C1 · T2`** | *Proposta* = **proprietario**… e, para `SPC`, `FND-09 §8.2` poe **DEP-PRD** como quem **propoe/cria** e quem **aposenta** *(logo, proprietario)*. *Aprovacao* = **proprietario + revisor** | 2 |
| [`FND-04 §3.1`](../foundation/04-governanca.md) | *"`Proponente ≠ Aprovador` (PI-05)"* e *"Acumulo indevido de papeis torna a aprovacao **nula** (`LV-03`)"* | 2, remetendo a `LV-03` de `FND-01`, nivel **1** |

**Em `C1 · T2`, para o tipo `SPC`, Proponente e Aprovador sao o mesmo Departamento.** A
consequencia nao e estilistica: e **nulidade**.

## 2. Problema / Pergunta de decisao

> **Cria-se agora a primeira `Spec` sobre `LM-6(a)` de `PRO-nxtrack`, e em qual classe — dado
> que o piso `C1` de `FND-04 §6` produz aprovacao nula por `FND-04 §3.1`?**

## 3. Criterios de decisao

> Declarados **antes** de examinar as alternativas (`CD-01`, `VD-02`). Sao os `CR-1` a `CR-6` de
> [`RFC-0026 §4`](../rfcs/RFC-0026-primeira-spec-governanca-de-dado-pessoal-do-nxtrack.md),
> reproduzidos sem alteracao.

| # | Criterio | Peso | Como se mede |
|---|---|---|---|
| `CR-1` | A aprovacao resultante e **valida** | Alto | Confronto papel a papel com `FND-04 §3.1` |
| `CR-2` | Obedece a ordem que o ato fixou | Alto | `DC-3` de `MSG-2026-0009` |
| `CR-3` | Nao usurpa competencia alheia | Alto | `FND-01 §7.3`; `LV-08`; `SF-03` |
| `CR-4` | Exercivel hoje, sem `S2` | Alto | `RD-88` |
| `CR-5` | Produz a revisao empirica de `FND-11` | Medio | `FND-11 §15`, gatilho de revisao |
| `CR-6` | Custo de contexto medido | Medio | `CE-02`, `CE-04` |

## 4. Alternativas consideradas

### Alternativa A — `Spec` de produto, classe **`C2 · Tipo 2`**

| Campo | Conteudo |
|---|---|
| Descricao | `SPC-001` em `products/nxtrack/specs/`, `CAP-juridico`, custodiante DEP-QAR. Classe elevada ao **menor** valor da matriz em que nenhum papel se acumula |
| A favor | `CR-1` satisfeito **por construcao**: DEP-PRD propoe, DEP-ENG + DEP-QAR revisam, DEP-EXE aprova, DEP-GOV registra — **quatro** papeis, **quatro** titulares distintos. `CR-2`, `CR-3`, `CR-4` e `CR-5` satisfeitos |
| Contra | `C2` puxa `RFC → ADR` (`FND-04 §2`) e `FIT` (`SF-24`, item 9). **Cinco** artefatos |
| Custo | Medido em §7 |
| Risco | Precedente de `Spec` cara. Mitigado por §6, que **declara o piso `C1` intacto** para as demais |
| Avaliacao pelos criterios | `CR-1` ✅ · `CR-2` ✅ · `CR-3` ✅ · `CR-4` ✅ · `CR-5` ✅ · `CR-6` ⚠️ **custo alto, e declarado** |

### Alternativa B — `Spec` de produto, classe **`C1 · Tipo 2`** *(o piso literal)*

| Campo | Conteudo |
|---|---|
| Descricao | Idem, mantendo a classe que `FND-04 §6` escreve na linha *Spec* |
| A favor | Literal. **Dois** artefatos em vez de cinco. Dispensa `RFC`, `ADR` e `FIT` |
| Contra | **Reprova `CR-1`, que tem peso Alto e e binario:** a aprovacao seria **nula** (`FND-04 §3.1`, `LV-03`). Alem disso, produziria o **primeiro** artefato do acervo a reprovar no criterio `AC-03`, hoje medido em **`0`** violacoes |
| Custo | O menor de todos |
| Risco | **Maximo.** Entregar artefato nulo e pior que nao entregar: `LV-05` proibe reportar como concluido o que nao esta |
| Avaliacao pelos criterios | `CR-1` ❌ **binario** · `CR-2` ✅ · `CR-3` ✅ · `CR-4` ✅ · `CR-5` ✅ · `CR-6` ✅ |

### Alternativa C — Politica organizacional de dado pessoal *(materia nao-produto)*

| Campo | Conteudo |
|---|---|
| Descricao | Norma interdepartamental valida para todo o acervo |
| A favor | Fecharia `FG-11` de `PT-2026-014` inteiro, e nao so o nXtrack |
| Contra | **Reprova `CR-4` de forma binaria.** `RD-88` registra que a categoria **nao existe**: `FND-03 §3.6` e `FND-10 §4.4` so preveem `products/<slug>/specs/`, e `FND-04 §6` exige *"Produto existe"*. So `S2` a cria, e `S2` esta **DEFERIDA** por decisao do SOBERANO |
| Custo | `RFC C3` + `ADR C3` + ato soberano |
| Risco | Decidir no lugar do SOBERANO — o que a missao veda expressamente |
| Avaliacao pelos criterios | `CR-1` n/a · `CR-2` ⚠️ · `CR-3` ❌ · `CR-4` ❌ · `CR-5` ✅ · `CR-6` ❌ |

### Alternativa Z — Nao fazer nada

| Campo | Conteudo |
|---|---|
| O que acontece se mantivermos o estado atual | `LM-6(a)` continua em `0`. `GO-TO-SPECS` fica **exercivel e nao exercido** — o mesmo estado que `FIT-2026-015` usou para recusar `GO-TO-SKILLS`. As **32** regras seguem determinadas e nao observadas (`L1`), e o gatilho de revisao de `FND-11 §15` nunca dispara |
| Custo real da inacao | O risco `R2` da Carta de `PRO-nxtrack` — *"aprendizado coletivo entre usuarios com bibliotecas separadas"*, severidade **Alta** — segue **sem mitigacao escrita**, contido apenas pelo **loopback**, que e configuracao *(uma linha de `compose.beta.yml`)* e nao norma |
| Por que nao venceu | Descumpre `CR-2` — o ato fixou materia **e** prioridade. **Nao e alternativa de palha:** e a unica de custo zero, e venceria se a exposicao fosse impossivel; mas `POST /sessao/criar` existe e o cadastro e publico (`LM-5`) |

## 5. Decisao

**Decidimos criar `SPC-001 — Governanca de dado pessoal do nXtrack`, em
`products/nxtrack/specs/`, vinculada a `CAP-juridico` e custodiada por DEP-QAR, na classe
`C2 · Tipo 2`, com aprovacao de DEP-EXE mediante parecer de DEP-GOV e sem ratificacao.**

E decidimos que **a elevacao de `C1` para `C2` vale para esta criacao e nao se generaliza**: a
classe de cada `Spec` futura continua sendo funcao do efeito dela, com `C1` como piso, nos exatos
termos de `SF-10`.

## 6. Justificativa

`CR-1` decide sozinho, porque e **binario e de peso Alto**: entre A e B, so A produz aprovacao
valida. `FND-01 §7.1.6` — *"na duvida sobre classificacao, prevalece a classificacao mais
restritiva"* — nao foi invocada como cautela generica: a **duvida tem fundamento citado e
reproduzivel por terceiro** *(basta ler a coluna `C1 · T2` de `SF-10 §5` contra `FND-04 §3.1`)*,
e `C2` e o **menor** valor da matriz que a dissolve.

C reprova em `CR-3` e `CR-4`; Z reprova em `CR-2`.

**A colisao nao e corrigida aqui, e a razao esta na propria norma.** Sanar `SF-10` exige emendar
`FND-11`, que so vigora com **aprovacao e ratificacao do SOBERANO** (`FND-09 §8.2` linha `FND`;
`LM-02`) — competencia que este `ADR`, `C2`, **nao tem**. Fica como achado **`RD-91`**, dono
**SOBERANO**, gatilho *"proxima emenda de `FND-11` ou segunda `Spec` real"*. **Congelamento em
vigor: nao gera missao.**

**Tradeoff aceito.** Abre-se mao do custo baixo: **cinco** artefatos onde a leitura literal de
`FND-04 §6` previa **dois**, e cria-se o risco de precedente caro. Aceita-se porque a alternativa
barata entrega **nulidade**, e porque §5 declara o piso `C1` **intacto** para as demais `Spec`s.

## 7. Impacto

| Dimensao | Impacto |
|---|---|
| **Departamentos afetados** | DEP-PRD · DEP-ENG · DEP-QAR · DEP-EXE · DEP-GOV · DEP-OPS |
| **Componentes afetados** | **`PRO-nxtrack`** — primeira `Spec`. **`0` bytes** no repositorio do candidato |
| **Camadas de memoria a atualizar** | `estrategica` *(este `ADR`)* · `produto` *(a `Spec`)* · `operacional` *(o `PT`)* |
| **Decisoes superadas** | **Nenhuma.** `supera: []` |
| **Documentos a atualizar** *(cascata `CV-04`, **na mesma mudanca**)* | [catalogo mestre](../governance/artifact-registry.md) · [`README` raiz](../README.md) · [`decisions/README`](README.md) · [`rfcs/README`](../rfcs/README.md) · [`governance/README`](../governance/README.md) · [`governance/fitness/README`](../governance/fitness/README.md) · [`roadmap`](../governance/roadmap-canonico.md) |
| **Custo e dependencia criados** | **1 `RFC` + 1 `ADR` + 1 `SPC` + 1 `FIT` + 1 `PT`.** `0` dependencias externas, `0` ferramentas novas, `0` entidades, `0` tipos documentais, `0` portoes, `0` papeis |
| **Ganho `PI-14`** | **Organizacao e reducao de contexto** — requisito enderecavel por `<SPC-id> RQ-nn` (`SF-31`). Sinal observado: `PB-1`/`PB-2` de `RFC-0026 §2`. **Reavaliacao: 2027-02-02** |

## 8. Evidencias

| # | Evidencia | Origem | Confianca | O que ela discrimina |
|---|---|---|---|---|
| `E1` | **`LM-6(a)` = `0` para os seis termos**, nas duas varreduras *(183 rastreados sob `tree b9b36be9…fb4b`; 262 na arvore de trabalho)*, com **controle positivo** aplicado antes | Item 0 da Missao 1.13.5, §3 | **Alta** | Discrimina *"a lacuna existe"* de *"o instrumento nao mediu"* — o primeiro resultado desta missao foi `0` para tudo, **inclusive para `senha_hash`**, e foi **descartado** como defeito de instrumento |
| `E2` | **`feedback_recomendacao` nao tem coluna de usuario**; `carregar_feedback` le sem clausula por usuario; `alternar` apaga e insere globalmente | `prototipo/feedback.py:29-95` | **Alta** | Discrimina *"aprendizado coletivo"* de *"aprendizado agregado com titular preservado"*. E o fato que `R2` da Carta declarava sem medir |
| `E3` | **`0` caminhos de exclusao de conta** em codigo de producao; `DELETE FROM usuarios` so em teste | `prototipo/tests/test_usuarios.py:393` | **Alta** | Discrimina *"a regra existe e nao foi implementada"* de *"a regra nao existe"* |
| `E4` | **`spec-tecnica-v1.md §24` ja enuncia oito regras de privacidade**, sem criterio de aceite | `spec-tecnica-v1.md:777` | **Alta** | Discrimina *"lacuna de intencao"* de *"lacuna de obrigacao verificavel"*. **Muda o que a `Spec` precisa fazer**: partir do que existe, nao reinventar |
| `E5` | **Colisao `SF-10 C1·T2` × `FND-04 §3.1`** | Leitura confrontada das duas fontes vigentes | **Alta** | Discrimina *"cautela"* de *"nulidade"*. Reproduzivel por terceiro sem consultar o autor |
| `E6` | **Numero de titulares do nXtrack** | — | **AUSENTE, e declarado ausente** (`VD-05`, `PI-10`) | Exigiria abrir `nxtrack.db`. Proibido. **A decisao nao depende dele:** ha dado pessoal por desenho, e `1` titular ja basta |
| `E7` | **Enquadramento legal aplicavel** | — | **AUSENTE, e declarado ausente** | Materia de assessoria humana qualificada — `CAP-juridico` declara isso na propria fonte. **Nenhum requisito desta decisao afirma enquadramento** |

## 9. Riscos e mitigacao

| # | Risco | Prob. | Impacto | Mitigacao prevista |
|---|---|---|---|---|
| `R1` | **Precedente de `Spec` cara** — toda `Spec` futura custar cinco artefatos | Media | Medio | §5 declara a elevacao **restrita a esta criacao**; `SF-10` segue valendo integral. Sinal de que se realizou: **segunda `Spec` classificada `C2` sem colisao propria** |
| `R2` | **A `Spec` virar parecer juridico** | Baixa | **Alto** | `0` requisitos que afirmem enquadramento legal; `CAP-juridico` remete a assessoria humana. Verificavel por contagem |
| `R3` | **Usurpar a competencia do SOBERANO** sobre exposicao de dado vivo | Baixa | **Alto** | Requisitos de exposicao **negativos** (`SF-25`); a `Spec` declara em §4 que satisfaze-la **nao autoriza publicar** |
| `R4` | **`RD-91` nunca ser sanado**, e a colisao virar norma de fato | Media | Medio | Achado com dono **SOBERANO** e gatilho declarado. Sinal: terceira `Spec` elevada pelo mesmo motivo |
| `R5` | **Esta decisao estar errada** — a colisao ser leitura equivocada, e `C1` bastar | Baixa | Medio | A colisao e **verificavel por terceiro** lendo duas linhas de fontes vigentes. Se refutada, o remedio e barato: superar este `ADR` e reclassificar a `Spec` por emenda `CORRECAO`, **sem tocar no conteudo dos requisitos** |

## 10. Plano de reversao

| Campo | Conteudo |
|---|---|
| **Como desfazer** | Superar este `ADR` por `ADR` sucessor que o referencie (`FND-01 §7.1.5`) e **retirar** `SPC-001` por `O9` (`SF-30`), declarando o que passa a valer no lugar (`SU-04`) |
| **Custo da reversao** | **Medido: 6 arquivos** — 1 `ADR` novo, 1 `SPC` retirada, catalogo, `README` raiz, `decisions/README`, baseline nova. **`0` dependentes a migrar**, porque `SPC-001` e a primeira e nenhum artefato a cita ainda (`LC-05` sem trabalho) |
| **Janela em que ainda e possivel** | **Permanente enquanto `0` componentes implementarem os requisitos.** A partir do primeiro consumo por missao de construcao, a reversao passa a exigir plano de migracao (`SF-29`) |
| **Quem executa** | **DEP-PRD** — `FND-09 §8.2` linha `SPC`, *aposenta* |
| **Backup necessario (`PI-07`)** | `_backups/LucaX-Enterprise-OS_2026-08-01_pre-missao-1-13-5` — **597 arquivos**, datado antes da primeira escrita |

> **Por que a reversao e trivial para `Tipo 2`.** O objeto e **documental**: `0` bytes de codigo,
> `0` bytes no repositorio do candidato, `0` dado vivo tocado, `0` dependentes. Desfazer e
> apagar um arquivo e reconciliar cinco indices — o mesmo custo de qualquer artefato deste acervo.

## 11. Classificacao

| Campo | Valor |
|---|---|
| **Classe de mudanca** | **`C2`** — elevada do piso `C1` de `FND-04 §6` por `FND-01 §7.1.6`, com a duvida fundada em `E5` |
| **Tipo de reversibilidade** | **`Tipo 2`** — reversivel a custo medido de 6 arquivos, `0` dependentes |
| **Decisor** | **DEP-EXE**, com parecer de DEP-GOV |
| **Ratificador** | **Nao exigido** — `C2 · Tipo 2` (`FND-04 §2.1`) |
| **Data da decisao** | 2026-08-02 |
| **Data de vigencia** | 2026-08-02 — `C2` nao depende de ratificacao (`LM-02` alcanca `C3` e `Tipo 1`) |

## 12. Revisao

| Campo | Conteudo |
|---|---|
| **Gatilho de reavaliacao** | **evento** + **confirmacao de ganho** |
| **Detalhe do gatilho** | *(a)* a **segunda `Spec` real** do acervo — que dira se a elevacao a `C2` foi especifica ou virou regra de fato; *(b)* o **primeiro consumo** de um `RQ-nn` de `SPC-001` por missao de construcao, que confirma ou nega o ganho `PI-14`; *(c)* qualquer emenda de `FND-11` que sane `RD-91` |
| **Sinal de que esta decisao deu errado** | Uma terceira `Spec` elevada a `C2` **pelo mesmo motivo** *(colisao de papeis, e nao efeito proprio)*: seria prova de que o defeito e estrutural e de que este `ADR` o acomodou em vez de o expor |
| **Responsavel pela revisao** | **DEP-PRD**, com DEP-QAR como verificador |

## 13. Rastreabilidade

| Campo | Conteudo |
|---|---|
| **Origem** | [RFC-0026](../rfcs/RFC-0026-primeira-spec-governanca-de-dado-pessoal-do-nxtrack.md) — aceita em 2026-08-02 |
| **Decisoes superadas** | Nenhuma |
| **Decisoes relacionadas** | `ADR-0021` *(institui `SF-01`–`SF-32`)* · `ADR-0022` *(sede em `FND-11`)* · `ADR-0019` *(aprovador e ratificador de `Spec`)* · `ADR-0018` *(`QG-1`)* · `ADR-0030` *(admite o `PRO-nxtrack`)* · `ADR-0005` *(proibicao de autoverificacao)* |
| **Artefato criado** | [`SPC-001`](../products/nxtrack/specs/SPC-001-governanca-de-dado-pessoal-do-nxtrack.md) |
| **Verificacao de aptidao** | [`FIT-2026-024`](../governance/fitness/FIT-2026-024-primeira-spec.md) — exigida por `SF-24`, item 9 |
| **Registros de memoria gerados** | [`PT-2026-017`](../governance/relatorio-transicao-2026-08-02-primeira-spec.md) |
| **Achados abertos por esta decisao** | **`RD-91`** *(colisao `C1` × `FND-04 §3.1`; dono SOBERANO)* · **`RD-92`** *(DEP-QAR custodiante da materia **e** revisor do tipo na mesma mudanca; dono DEP-GOV)* |

---

## Checklist de validade (`FND-07 §4.1`)

- [x] `VD-01` — **3 alternativas reais + "nao fazer nada"** *(A, B, C, Z)*
- [x] `VD-02` — criterios `CR-1` a `CR-6` declarados em §3, **antes** de §4
- [x] `VD-03` — **nenhuma alternativa de palha**: B e o texto literal da norma; C fecharia lacuna maior; Z e a de custo zero, e §4 declara **por que cada uma nao venceu**
- [x] `VD-04` — tradeoff explicito em §6: **cinco artefatos onde a leitura literal previa dois**
- [x] `VD-05` — `E6` e `E7` declarados **ausentes**, com a razao
- [x] `VD-06` — plano de reversao em §10, com custo **medido** em 6 arquivos *(nao exigido para `Tipo 2`; feito assim mesmo)*
- [x] `VD-07` — impacto em cascata mapeado em §7, com os **7** documentos `M3`
- [x] `VD-08` — data *(2026-08-02)* e responsaveis presentes
- [x] `VD-09` — gatilho de revisao em §12, com **sinal de erro** declarado

---

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-08-02 | DEP-PRD | Criacao. Decide criar **`SPC-001`**, a **primeira `Spec` real do acervo**, sobre `LM-6(a)` de `PRO-nxtrack`, em classe **`C2 · Tipo 2`**. A elevacao acima do piso `C1` de `FND-04 §6` e fundada em colisao **medida** entre a coluna `C1 · T2` de `SF-10` e `FND-04 §3.1` — *Proponente = Aprovador* para o tipo `SPC` —, que torna a aprovacao **nula** por `LV-03`. `FND-01 §7.1.6` aplicada a duvida **com fundamento citado**, jamais como cautela generica. **`0` fontes emendadas · `0` entidades, tipos, portoes ou papeis criados · `0` bytes no repositorio do candidato · `0` celulas de `FND-09 §8.2` alteradas.** Achados **`RD-91`** e **`RD-92`** abertos, com dono e gatilho, **sem gerar missao** — congelamento em vigor. **Primeiro `ADR` do acervo cujo autor e DEP-PRD e cujo objeto e uma `Spec`.** |
