---
id: RFC-0016
titulo: Regime ministerial de promulgacao e ativacao — titular declarado, nao criado
tipo: rfc
versao: 1.0.0
status: aprovado
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-GOV
criado_em: 2026-07-29
atualizado_em: 2026-07-29
revisao_prevista: null
decisoes_relacionadas: [ADR-0020]
substitui: []
substituido_por: null
resumo: Propoe fechar RD-22 declarando que promulgar e ativar sao operacoes ministeriais cujos executores, verificadores e registradores ja estao nomeados em FND-04 §3 e §4, FND-07 §5 e AU-06, sem criar autoridade nem emendar fonte.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# RFC-0016: Regime ministerial de promulgacao e ativacao

## Proposito

Propor o instrumento que fecha o achado **`RD-22`** — *`promulgacao` e `ativacao` nao sao
titularidades declaradas* — sem criar entidade, agente, papel ou autoridade, e sem emendar
documento fundacional.

## Escopo

| Item | Definicao |
|---|---|
| **Inclui** | A natureza juridica de **promulgar** e **ativar**; o mapeamento de cada ato a **autoridade decisoria**, **executor**, **verificador** e **registrador**; a cascata de impedimento e de ausencia; o texto proposto de regras |
| **Nao inclui** | Qualquer alteracao de **FND-01 §7.3**, **FND-02 §4**, **FND-09 §8.2** ou de portao de **FND-01 §6.2**; qualquer titular novo; o tratamento de `RD-23`, `RD-24` e `RD-26` |
| **Subordinado a** | [FND-01](../foundation/01-constituicao.md) · [FND-04](../foundation/04-governanca.md) · [FND-07](../foundation/07-framework-decisoes.md) · [FND-09](../foundation/09-meta-model.md) · [FND-10](../foundation/10-artifact-framework.md) |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| Propoe | **DEP-GOV** | Materia de **forma e conformidade** — [DEP-GOV §5](../departments/gov/carta.md), autonomia A2 |
| Valida a forma | **DEP-GOV** | FND-09 §8.2, linha `RFC` |
| **Revisa** | **DEP-QAR** | **DEP-GOV `I-1`** — nao revisa o que produz (RM-06b, ADR-0005) |
| Decide | ver **ADR-0020** | FND-07 §2.4 |

---

## 1. Contexto

O sexto ato soberano — [MSG-2026-0006 §IX](../memory/operacional/MSG-2026-0006-ato-soberano-aplicacao-integral.md)
— exigiu que a prova de consumo por Specs identificasse, *"sem interpretacao informal"*, os
titulares de **dez** atos, entre eles **promulgacao** e **ativacao**.

A aplicacao integral do ato foi provada em
[PT-2026-005](../governance/relatorio-transicao-2026-07-29-aplicacao.md): **as 55 celulas
respondem**, mas **duas das dez titularidades ficaram sem titular declarado**, e por isso a
**condicao 6 de §X** falhou e `GO-TO-SPECS` **nao** foi autorizado.

A medicao que produziu `RD-22` esta em §5.3 daquele relatorio, e ela e **correta em tudo o que
mediu**:

| Evidencia de `RD-22` | Verificada nesta RFC |
|---|---|
| Os **cinco** verbos de autoridade de FND-09 §8.1 sao *Criar, Alterar, Aprovar, Consumir, Aposentar* — `promulgar` **nao** esta entre eles | ✅ **Confirmado** na fonte vigente |
| `FND-10 §5.2` `O4` declara operacao, transicao, criterio e rollback — **nao** o ator | ✅ **Confirmado** |
| `FND-10 §5.4` declara a **condicao** de entrada em `ativo` — **nao** o ator | ✅ **Confirmado** |
| Nenhuma celula de **FND-09 §8.2** nomeia titular de promulgacao ou ativacao | ✅ **Confirmado** |

## 2. Problema — e ele nao e o que o achado supos

**Pergunta exata:** *promulgar* e *ativar* sao **decisoes discricionarias**, que exigem
titular declarado em uma matriz de autoridade, ou **operacoes ministeriais**, que decorrem de
aprovacao ou ratificacao valida e cujo executor ja esta nomeado?

`RD-22` procurou o titular em **FND-09 §8.1/§8.2** e em **FND-10 §5.2/§5.4**, e nao o achou.
**Nao o achou porque nao esta la — e nao esta la por uma razao normativa, nao por lacuna.**

### 2.1 O que FND-09 §8.2 e, e o que ela nao e

FND-09 §8.2 e a **matriz de autoridade por entidade**, e o que ela distribui sao os **cinco
verbos de §8.1**. Ela responde *quem pode decidir sobre a coisa*. **Ela nao e o registro de
quem opera o ciclo do documento** — e `AU-09` incide sobre o que ela governa:

> **`AU-09`.** *Autoridade nao declarada em §8.2 **nao existe** (MT-09). Na duvida, escala-se
> (EC-01).*

`AU-09` diz que **autoridade** nao declarada nao existe. **Promulgar e ativar nao sao
autoridade** — §8.1 fecha a lista em cinco verbos, e nenhum dos dois consta. Aplicar `AU-09`
a eles e usar a regra fora do seu objeto.

### 2.2 A regra que responde e `AU-06`, e ela e literal

> **`AU-06`.** *Instrumento **autoriza**; nao executa. O ADR permite criar o componente; quem
> o cria e o **executor nomeado**.*

`AU-06` separa **autorizar** de **executar** e remete a execucao ao **executor nomeado**.
A pergunta de `RD-22` deixa de ser *"quem tem autoridade para promulgar?"* e passa a ser
*"quem e o executor nomeado?"* — que e pergunta de **FND-04** e de **FND-07**, nao de
FND-09 §8.2.

### 2.3 Os executores **estao** nomeados — em quatro lugares

| Fonte vigente | Texto declarado | Ato que ela nomeia |
|---|---|---|
| **FND-04 §3** | **Executor** — *"Aplica a mudanca aprovada, no escopo aprovado"*; **nao pode** *"Alterar o escopo durante a execucao"* | **Executor ministerial**, com a vedacao que o ato soberano exigia |
| **FND-04 §3** | **Guardiao** (DEP-GOV) — *"Valida classe, forma, conformidade, rastreabilidade; atribui ID"*; **nao pode** *"Julgar merito de conteudo"* | **Registrador**, sem competencia de merito |
| **FND-04 §3** | **Verificador** (DEP-QAR) · **Curador** (DEP-KMS) · **Ratificador** (SOBERANO) | **Verificador** · **registrador de memoria** · **decisor de eficacia** |
| **FND-04 §4 [7]** | ***"REGISTRO — DEP-GOV atribui ID definitivo, publica ADR, atualiza indices e contadores"*** | **PROMULGACAO — titular DEP-GOV, declarado** |
| **FND-04 §4 [8]** | *"EXECUCAO — Executor aplica exatamente o aprovado. Desvio durante execucao ⇒ volta a [2]"* | **Execucao vinculada** (CV-03) |
| **FND-04 §4 [9]** | *"VERIFICACAO — DEP-QAR confirma que o resultado corresponde ao aprovado; confirma backup e reversao"* | **Verificacao independente** |
| **FND-04 §4 [12]** | *"MEMORIA — DEP-KMS grava na camada correta (QG-5)"* | **Registro de memoria** |
| **FND-04 `CV-02`** | *"Para C2 e C3, o **registro (7) precede a execucao (8)**. Executar antes de registrar e violacao"* | **Promulgacao precede ativacao — ordem normativa** |
| **FND-07 §5 [10]** | ***"REGISTRO — DEP-GOV atribui numero e publica o ADR"*** | **PROMULGACAO — segunda fonte, mesmo titular** |
| **FND-07 §5 [13]** | ***"VIGENCIA — decisao passa a valer e vincula"*** | **ATIVACAO — etapa sem ator: e efeito, nao ato** |
| **FND-07 `CD-05`** | *"Decisao vigente vincula todos, inclusive quem discordou"* | **Nenhuma discricionariedade posterior** |
| **FND-09 §7.5** | *"Entra em vigor | `ativo` | **Publicacao + atualizacao de indice**"* | **O instrumento da ativacao e operacional** |
| **FND-09 `LC-01`** | *"Toda transicao e **ato registrado**, com responsavel e data. Transicao silenciosa e **nula**"* | **Ativacao exige registro nominal** |
| **FND-10 §5.2 `O4`** | Transicao com **criterio verificavel** e **rollback** declarados | **Criterio, nao juizo** |
| **FND-10 §5.4 `LM-02`** | Ratificacao e **condicao de validade**: sem ato, permanece `aprovado` | **A condicao satisfeita completa O4** |
| **FND-10 `LM-05`** | *"Quem registra a ratificacao e papel **distinto** de quem executou a mudanca (CV-09)"* | **Separacao executor × registrador** |
| **FND-10 §6.1** | Tabela *Ato → Quem*: Propor, Criar, Revisar, Aprovar, Ratificar, Alterar, Superar, Aposentar | **Promulgar e ativar nao constam — coerente com serem execucao** |
| **DEP-GOV §7** | *"**Diretiva** — registro canonico de ato soberano | `MSG` | **Registra; nunca emite**"*; *"Catalogo mestre · baseline · indices | **Autor e proprietario**"* | **DEP-GOV e registrador, nunca emissor** |
| **DEP-GOV `G-10`** | *"Registro canonico do ato de ratificacao — os tres hashes e o diff"* | **A prova do ato e do registrador** |
| **DEP-GOV `I-7`** | DEP-GOV **nao** executa `IR-09` sobre o que registrou → **DEP-QAR executa** | **Verificacao independente e estrutural** |

**Sao vinte declaracoes em cinco fontes vigentes distintas, todas convergentes.** A leitura
que `PT-2026-005 §5.3` chamou de *"contra-leitura defensavel, e ela mesma interpretacao"* **nao
e interpretacao: e a soma literal dessas declaracoes.** O que faltava nao era norma — era
**medi-la no lugar certo**.

### 2.4 Por que a omissao ocorreu, e por que ela e informativa

`RD-22` mediu **tres coisas**: os verbos de §8.1, as ocorrencias da palavra *"promulg"* na
camada normativa e as duas secoes de FND-10. **Nao mediu FND-04 §3 nem FND-04 §4, nem
FND-07 §5** — e e exatamente nelas que o executor esta nomeado.

A causa e a mesma de `RD-23`: **a varredura procurou o termo, nao a funcao.** O acervo nunca
usou a palavra *promulgar* para nomear a etapa `[7]`; usou **REGISTRO**. Procurar
*"promulg"* encontra **prosa de ADR**; procurar *"quem publica o que foi aprovado"* encontra
**titular declarado**. Isto e registrado como aprendizado, com dono, em ADR-0020 §12.

## 3. O mapa completo — **ato x papel**, sobre fonte viva

| Ato | **Natureza** | Autoridade decisoria | **Executor ministerial** | Verificador | Registrador | Fonte |
|---|---|---|---|---|---|---|
| **Propor** | Discricionaria | conforme entidade | — | — | DEP-GOV | FND-09 §8.2 |
| **Aprovar** | **Discricionaria — merito** | conforme classe | — | DEP-QAR | DEP-GOV | FND-04 §2; FND-07 §2.4 |
| **Vetar** | Discricionaria — vinculante | DEP-QAR · DEP-GOV | — | — | DEP-GOV | FND-02 §4.2; LV-09 |
| **Ratificar** | **Discricionaria — indelegavel** | **SOBERANO** | — | DEP-QAR | DEP-GOV | FND-10 §5.4; `AU-05` |
| **Promulgar** | **Ministerial** | *(nenhuma — decorre do ato)* | **DEP-GOV** | **DEP-QAR** | **DEP-GOV** | **FND-04 §4 [7]**; **FND-07 §5 [10]** |
| **Ativar** | **Ministerial** | *(nenhuma — decorre do ato)* | **Executor nomeado no ato** | **DEP-QAR** | **DEP-GOV** + **DEP-KMS** | **FND-09 §7.5**; **FND-04 §4 [8]–[12]**; **`LC-01`** |
| **Superar** | Discricionaria | conforme classe | autor do sucessor | DEP-QAR | DEP-GOV | FND-10 §6.1; `O6` |

> **Por que a coluna *Autoridade decisoria* de promulgar e ativar e vazia, e isso e resposta e
> nao lacuna.** Uma operacao ministerial **nao tem** autoridade propria: ela **executa** a
> autoridade de quem aprovou ou ratificou. Preencher a celula com um nome seria **criar**
> autoridade — o que `AU-03` proibe e o que `RD-22` corretamente se recusou a fazer. A
> resposta certa nao e um nome novo: e **declarar que a celula nao existe**, e nomear quem
> executa.

## 4. Texto proposto

Regras **`PA-01`** a **`PA-14`**, instituidas **no proprio ADR**, na forma em que
[ADR-0012](../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md) instituiu `IR-01` a
`IR-12` e [ADR-0015](../decisions/ADR-0015-fitness-check-e-parecer-nao-decisao.md) instituiu
`FT-10` a `FT-14`: **sem emendar nenhum documento fundacional**. Texto integral em
[ADR-0020 §5](../decisions/ADR-0020-regime-ministerial-de-promulgacao-e-ativacao.md).

**Nenhuma tabela de FND-01, FND-02, FND-04, FND-07, FND-09 ou FND-10 e alterada.** A matriz
de regime operacional de ADR-0020 §5.2 e **projecao declarada** (`PJ-02`) dessas fontes: em
divergencia, **prevalece a fonte** (`PJ-03`).

## 5. A verificacao que importa — isto amplia titular?

| Nome que a proposta usa | Ja constava de | Ampliado? |
|---|---|---|
| **DEP-GOV** promulga / registra / indexa | FND-04 §4 [7] · FND-07 §5 [10] · `G-3` · `G-8` · `G-10` · DEP-GOV §7 | **Nao** |
| **DEP-QAR** verifica | FND-04 §3 e §4 [9] · `IR-09` · DEP-GOV `I-7` | **Nao** |
| **DEP-KMS** grava memoria | FND-04 §3 e §4 [12] · QG-5 | **Nao** |
| **Executor nomeado no ato** aplica | `AU-06` · FND-04 §3 | **Nao** |
| **SOBERANO** ratifica | FND-10 §5.4 · `AU-05` · `AU-10` | **Nao** |

**Cinco nomes, cinco fontes anteriores, zero ampliacoes.** E a mesma verificacao que
`ADR-0016` §5, `ADR-0018` e `ADR-0019` fizeram, com o mesmo resultado.

### 5.1 E o Soberano vira operador tecnico?

**Nao — o contrario.** Hoje, sem o regime declarado, **cada** promulgacao e cada ativacao
retorna ao Soberano como duvida de titularidade: foi o que produziu `RD-22` e o que bloqueou
`GO-TO-SPECS`. Com o regime declarado, o Soberano aparece em **duas** posicoes, ambas
decisorias:

| Onde o Soberano aparece | Natureza | Frequencia |
|---|---|---|
| **Ratificacao** de C3 e de Tipo 1 | Decisao de merito, indelegavel (`AU-05`) | Por ato |
| **Terminus de impedimento duplo** | Decisao excepcional (`AU-10`, `EC-01`) | Por excecao |

Em nenhuma delas ele executa, publica, indexa ou mede hash. `PA-13` fecha isso por escrito.

## 6. O limite declarado — o que esta RFC **nao** resolve

| Nao resolve | Por que | Onde vive |
|---|---|---|
| **`RD-23`** — `TPL-spec` fora da cascata de ADR-0019 | Exige emenda a template; materia de `TPL`, aprovador DEP-GOV, rito proprio | Pre-correcao obrigatoria da Missao 1.13 |
| **`RD-27`** — FND-01 e FND-02 sem os campos do contrato | A correcao altera **`H-N`** e por isso exige **ato soberano** (`IR-01`, `IR-03`, `IR-05`) | PT-2026-006 §3.4 |
| **`RD-24`** — §10.2 do catalogo | `BL-02` proibe editar baseline | Permanece aberto, com dono |
| **`RD-10`** — rota de escalonamento `PRD → TLS` | Materia de Carta, nao de portao | Permanece aberto |
| Autoverificacao residual de DEP-GOV *(familia `RC-02`)* | So desaparece quando existirem agentes (`IC-3`) | Declarado, nao resolvido |

## 7. Riscos

| # | Risco | Prob. | Impacto | Mitigacao |
|---|---|---|---|---|
| RR-1 | **Ministerial virar discricionario na pratica** — o executor "interpretar" o diff | Media | **Alto** | `PA-04` e `PA-05`: promulgar publica **exatamente** o conteudo autorizado, conferido por hash; divergencia e `IR-05`, nao correcao |
| RR-2 | **A matriz virar segunda fonte de verdade** | Media | Medio | Declarada como projecao (`PJ-02`) com fonte, campos, finalidade e metodo; `PJ-03` da precedencia a fonte |
| RR-3 | **DEP-GOV concentrar promulgacao, registro e catalogo** | **Observada — familia `RC-02`** | **Alto** | `PA-08`: verificacao e de DEP-QAR, sempre; `I-7` ja impede DEP-GOV de ser a unica prova. Residuo **declarado** |
| RR-4 | A classificacao **C2** ser contestada | Media | Medio | §8 declara o teste aplicado e a alternativa; o ADR e reversivel por superacao (`PA-14`) |
| RR-5 | Ausencia de ato ser suprida por precedente | Baixa | **Alto** | `PA-11` remete a `LM-03`: precedente e silencio **nao ratificam** |

## 8. Classificacao proposta — e o teste que a sustenta

| Teste de FND-04 §2 | Resposta | Consequencia |
|---|---|---|
| Altera **principio imutavel** ou **linha vermelha**? | **Nao** | Nao e C3 |
| Altera a **hierarquia normativa** de FND-01 §10? | **Nao** | Nao e C3 |
| Altera **direitos de decisao** — FND-01 §7.3, FND-09 §8.2? | **Nao.** Declara que promulgar e ativar **nao sao** direitos de decisao | Nao e C3 |
| Altera a **propria Fundacao**? | **Nao.** Nenhum arquivo de `foundation/` e tocado | Nao e C3 |
| Cria, altera ou remove **componente**? | **Nao** | Nao e C2 por esse fundamento |
| Muda **escopo, fronteira, interface ou padrao**? | **Sim — institui padrao de execucao** | **C2** |
| E **reversivel a custo baixo e conhecido**? | **Sim** — superacao por ADR; nenhum artefato migra | **Tipo 2** |

**Proposta: `C2` · `Tipo 2` · decide DEP-EXE com parecer de DEP-GOV · ratificacao nao
exigida.** Precedente de forma: **oito** ADR desta classe — `ADR-0005`, `ADR-0007` a
`ADR-0013` —, entre eles `ADR-0012`, que instituiu o regime de integridade do **proprio ato
de ratificacao** sob a mesma classe.

> **Se o SOBERANO entender que a materia e C3**, o caminho e `RFC → ADR C3 → ratificacao`, e
> esta RFC serve de peca instrutoria sem reescrita. **A escolha permanece dele**; o que esta
> proposta remove e a **necessidade** de um ato para responder a uma pergunta que a fonte
> vigente ja responde.

## 9. As decisoes possiveis

| # | Decisao | Efeito |
|---|---|---|
| **D1** | **Acolher** — ADR-0020 C2 · Tipo 2, com `PA-01` a `PA-14` | `RD-22` **fecha**; a condicao 6 de §X passa a ser apuravel |
| D2 | Acolher o merito, reclassificar como **C3** | `RD-22` fica **pendente de ato**; a missao encerra `READY-FOR-RATIFICATION` |
| D3 | Recusar o merito e **emendar FND-09 §8.1/§8.2** para incluir os verbos | Cria **dois verbos de autoridade novos** — C3, e amplia o universo fechado de §8.1 |
| D4 | **Nao fazer nada** | `RD-22` permanece aberto; toda promulgacao futura reabre a duvida, e `GO-TO-SPECS` fica bloqueado por tempo indeterminado |

**Recomendacao: `D1`.** `D3` e o unico caminho que **cria** autoridade, e por isso o unico
que exigiria ato soberano — e ele resolveria por ampliacao um problema que a fonte ja resolve
por leitura.

## 10. Manifestacoes

| Area | Manifestacao | Registro |
|---|---|---|
| **DEP-QAR** | Revisao independente e verificacao de aptidao | [FIT-2026-014](../governance/fitness/FIT-2026-014-regime-ministerial-e-cobertura-de-contexto.md) |
| **DEP-EXE** | Decide a classe C2 · Tipo 2 | ADR-0020 §11 |
| **DEP-KMS** | Grava o aprendizado na camada APR | [MEM-APR-0005](../memory/aprendizado/MEM-APR-0005-medir-a-ausencia-na-fonte-errada.md) |
| **DEP-GOV** | Propoe, valida a forma, promulga e registra | Esta RFC · ADR-0020 |

## 11. Resultado

**Acolhida.** Convertida em [ADR-0020](../decisions/ADR-0020-regime-ministerial-de-promulgacao-e-ativacao.md).

---

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-GOV | Proposta de fechamento de **`RD-22`**: promulgar e ativar sao **operacoes ministeriais**, e seus executores, verificadores e registradores **ja estao nomeados** em **FND-04 §3 e §4**, **FND-07 §5**, **FND-09 §7.5 e `AU-06`**, **FND-10 §5.2, §5.4, `LM-05` e §6.1** e na **Carta de DEP-GOV** — **vinte declaracoes em cinco fontes vigentes**. Demonstra que `AU-09` nao alcanca os dois atos porque **§8.1 fecha os verbos de autoridade em cinco** e nenhum deles e promulgar ou ativar. Declara a **causa da omissao** de `RD-22`: a varredura procurou o **termo** *"promulg"*, e o acervo nomeia a etapa como **REGISTRO**. Propoe `PA-01` a `PA-14` **dentro do ADR**, sem emendar fonte, na forma de `ADR-0012` e `ADR-0015`. **Zero titulares ampliados**, verificado nome a nome. Classe proposta **C2 · Tipo 2**, com o teste de FND-04 §2 aplicado item a item. |
