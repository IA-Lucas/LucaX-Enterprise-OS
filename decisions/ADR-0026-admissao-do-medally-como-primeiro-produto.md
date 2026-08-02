---
id: ADR-0026-admissao-do-medally-como-primeiro-produto
titulo: Admitir o medAlly pelo portao de ADR-0007 e cria-lo como PRO-medally, primeiro Produto do acervo, sem admitir conteudo algum do seu repositorio
tipo: adr
versao: 1.0.0
status: em-revisao
camada_memoria: estrategica
autor: DEP-PRD
proprietario: DEP-PRD
aprovador: SOBERANO
criado_em: 2026-07-31
atualizado_em: 2026-07-31
revisao_prevista: 2027-01-31
decisoes_relacionadas: [ADR-0002, ADR-0007, ADR-0012, ADR-0021, ADR-0022]
substitui: []
substituido_por: null
classe_mudanca: C2
tipo_decisao: 1
supera: []
superado_por: null
resumo: Admite o medAlly pelo portao de origem externa e cria PRO-medally como primeiro Produto, admitindo identidade e proposta e nenhum byte do repositorio de origem.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: pendente
---

# ADR-0026: Admissao do medAlly como primeiro Produto

> ## ⛔ ESTE ADR NAO ESTA EM VIGOR.
>
> `status: em-revisao` · `ratificacao: pendente`. **`C2 · Tipo 1` exige ato explicito e datado
> do Soberano sobre o texto final** (`LM-02`, `CV-09`, `PI-06`). Enquanto o ato nao ocorrer,
> **nenhum Produto existe**, `products/` **nao e criado** e **`RD-33` permanece bloqueante**.
>
> **A fonte corrente do estado e o frontmatter** (`FND-10 §5.4`, `PJ-04`), nunca este bloco.

## Proposito

Registrar a decisao de **admitir o medAlly pelo portao unico de origem externa** de
[ADR-0007 §5.3](ADR-0007-fronteira-greenfield-legado.md) e de **criar `PRO-medally`** como o
primeiro Produto do LucaX Enterprise OS — admitindo **identidade e proposta**, e **nenhum byte**
do repositorio de origem.

## Escopo

| Item | Definicao |
|---|---|
| **Inclui** | A aplicacao cumulativa de `G1`–`G5` ao candidato **medAlly**; a classificacao `G3`; a criacao de `PRO-medally` com a Carta de [PS-2026-014 §3](../governance/pacote-soberano-2026-07-31-medally.md); a criacao do diretorio `products/`; e a **avaliacao de suficiencia** do portao, que `ADR-0007 §12` obriga no primeiro caso real |
| **Nao** inclui | O **merito tecnico** do medAlly · **qualquer conteudo** do seu repositorio — codigo, schema, `ADR`, documento, base clinica ou teste · a criacao de `Spec`, `Projeto`, `Skill`, `Tool`, `Command`, `Workflow`, `Agente`, codigo ou infraestrutura · o **inventario** de qualquer outro produto *(`FR-07`)* · o **fechamento de `RD-33`**, que **so ocorre apos vigencia** · a **emenda de `ADR-0007`**, submetida como questao e **nao decidida aqui** |
| **Subordinado a** | [FND-01](../foundation/01-constituicao.md) · [FND-03](../foundation/03-taxonomia.md) · [FND-04](../foundation/04-governanca.md) · [FND-07](../foundation/07-framework-decisoes.md) · [FND-08](../foundation/08-capability-framework.md) · [FND-09](../foundation/09-meta-model.md) · [FND-10](../foundation/10-artifact-framework.md) · [FND-11](../foundation/11-framework-specifications.md) |
| Origem | [RFC-0021](../rfcs/RFC-0021-admissao-do-medally-como-primeiro-produto.md), Opcao A sob a leitura `L1` |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| Proponente | **DEP-PRD** | `FND-09 §8.2`, linha `PRO` |
| Revisor independente | **DEP-QAR** | `AC-03`; **`G4`** de `ADR-0007 §5.3` |
| Guardiao *(forma, classe, rastreabilidade)* | **DEP-GOV** | `FND-04 §3`; confere o portao **sem julgar merito** (`ADR-0007 §5.3`) |
| Consulta obrigatoria | **DEP-PRD** e **DEP-EXE** | `FND-01 §7.3`, linha *Portfolio*. **DEP-EXE nao se manifestou** — ausencia **declarada** |
| **Aprovador** | **SOBERANO** | §11, `Q3` |
| **Ratificador** | **SOBERANO** | `C2 · Tipo 1` — `FND-04 §2.2`, `FND-07 §2.3`, `PI-06`. **Indelegavel** |
| Executor | **DEP-GOV** | Regime ministerial de [ADR-0020](ADR-0020-regime-ministerial-de-promulgacao-e-ativacao.md) |

---

## 1. Contexto

O acervo tem **norma completa sobre Produto e nenhum Produto**, e **norma completa sobre `Spec`
e nenhuma `Spec`**. `FND-11` entrou em vigor em 2026-07-30 com `SF-01` a `SF-32`
**determinados e nao observados** (`A2` de `FIT-2026-018`), e `RD-33` — a **unica pendencia
bloqueante do acervo** — depende de `S1`: um ato que crie o primeiro Produto real.

Ao lado disso, o portao de admissao de origem externa existe desde 2026-07-28 e **nunca foi
exercido**. `ADR-0007 §8` declara literalmente a ausencia: *"nao ha nenhum candidato real,
nenhum dado sobre o conteudo do LucaX Legacy e nenhuma tentativa de importacao observada"*.

**Se nada mudar:** as duas camadas seguem validadas apenas por construcao — e `ADR-0007 §12`
ja declarou que a ausencia prolongada de candidato **com o Legacy em uso** e sinal de que o
portao **esta sendo contornado**, nao respeitado. **O Legacy esta em uso:** **19** commits
alcancam o caminho do candidato entre 2026-07-26 e 2026-07-30, medidos nesta missao.

## 2. Problema / Pergunta de decisao

**O medAlly deve ser admitido como o primeiro Produto do acervo, e sob qual classificacao do
portao?**

## 3. Criterios de decisao

> Declarados antes do exame das alternativas (`VD-02`). Sao os **sete** criterios de
> [RFC-0021 §4](../rfcs/RFC-0021-admissao-do-medally-como-primeiro-produto.md), **nao
> reproduzidos aqui** (`PJ-01`) — a fonte prevalece.

## 4. Alternativas consideradas

> Analise integral em [RFC-0021 §5](../rfcs/RFC-0021-admissao-do-medally-como-primeiro-produto.md).

| Alternativa | Desfecho | Por que |
|---|---|---|
| **A — medAlly agora** | **escolhida** | Unico candidato com evidencia medida; satisfaz `K1`–`K5` e `K7`; **condiciona** `K6` |
| **B — nXtrack primeiro** | recusada **por ausencia de evidencia, nao por merito** | `K1`, `K2` e `K3` sao **`desconhecido`**: `FR-07` proibe inventariar candidato nao nomeado, e o nomeado nesta missao e o medAlly. **Se o Soberano souber o que esta RFC nao pode saber, B vence A** |
| **C — os dois na mesma decisao** | recusada | **Falha `K2` e `K4`.** Exigiria o inventario previo que `FR-07` proibe, e instituiria o precedente de admissao em bloco que `ADR-0007` existe para impedir |
| **Z — nao fazer nada** | recusada | Nao produz informacao nova, e o custo da inacao **ja esta escrito em `ADR-0007 §12`** |

## 5. Decisao

### 5.1 O portao — `G1` a `G5`, cumulativos

> Condicoes de **admissibilidade**, nao de merito. DEP-GOV as confere **sem julgar conteudo**
> (`ADR-0007 §5.3`, `FND-04 §12`). **Condicao ausente bloqueia; nao gera ressalva** (`FR-06`).

| # | Condicao | Como foi satisfeita | Quem | Estado |
|---|---|---|---|---|
| **`G1`** | **Proveniencia declarada** | **De onde veio:** `E:/LucasIA/Projetos/lucaX/My_WorkSpace/Meus_projetos/medally`, dentro do repositorio Git `lucaX`, ramo `main`. **O que e:** software de telemedicina em ortopedia, **550** arquivos, **282** rastreados pelo Git. **Quem o produziu:** o **CEO**, por despacho proprio, registrado no `ADR-056` do repositorio de origem, **datado 2026-07-22**. **Quando foi observado:** **2026-07-31**, com estado Git registrado em [PS-2026-014 §2](../governance/pacote-soberano-2026-07-31-medally.md) | Proponente | ✅ |
| **`G2`** | **Fit-gap contra o vigente** | **O que o acervo ja tem que responde a mesma pergunta: nada.** `0` Produtos, `0` `Spec`s, `0` componentes executaveis; `products/` **nao existe**. **Onde o candidato diverge:** ele **nao e artefato de governanca** e **nao pretende ser** — nao ha duplicacao possivel, porque nao ha membro no conjunto com que duplicar. **A unica sobreposicao e conceitual e desejada:** o candidato **consome** cinco Capabilities do catalogo e **nao governa nenhuma** (`FND-09` E-17, *"Produto consome competencia; nao a governa"*) | Proponente, **conferido por DEP-GOV** | ✅ |
| **`G3`** | **Classificacao declarada — exatamente uma** | **`REWRITE`** — §5.2 | Proponente | ✅ |
| **`G4`** | **Validacao independente** | **DEP-QAR**, contra a **norma vigente** e nunca contra a pratica do Legacy. Parecer em [PS-2026-014 §5](../governance/pacote-soberano-2026-07-31-medally.md); aptidao em [FIT-2026-019](../governance/fitness/FIT-2026-019-admissao-do-medally.md). **DEP-QAR nao produziu a Carta nem este ADR** | **DEP-QAR** | ✅ |
| **`G5`** | **Decisao formal** | **Este ADR**, `C2 · Tipo 1`, com **ratificacao do SOBERANO**. **Sem o ato, nada entra em `ativo`** | Aprovador da classe | ⏳ **PREPARADO — pendente de ato** |

### 5.2 A classificacao `G3` e **`REWRITE`**, e a escolha e por eliminacao declarada

| Classificacao | Cabe? | Por que |
|---|---|---|
| `ADOPT` | **Nao** | Nenhum artefato do repositorio *"serve como esta"* para entrar no acervo. **`0`** arquivos sao propostos para entrada |
| `ADAPT` | **Nao** | Nada entra alterado, porque **nada entra** |
| **`REWRITE`** | **Sim** | *"O problema e real, a solucao do Legacy nao serve"* — e a definicao literal de `ADR-0007 §5.4`. **Nada entra**, e produz-se artefato **`native`** que responde ao mesmo problema: a **Carta**, escrita neste sistema, do zero |
| `RETIRE` | **Nao** | O problema **se aplica** a este sistema: e o desbloqueio de `S1`. **Reconhecer que o problema e real e o que separa `REWRITE` de `RETIRE`** |

> **`FR-08` esta cumprido de propria mao:** o portao produziu um resultado em que **nada entra**,
> e isso e **sucesso do portao, nao falha**. O que o ato admite e a **existencia formal** de um
> Produto; o **conteudo** do repositorio permanece `legacy-candidate`, **nao admitido**, e cada
> peca dele que um dia queira entrar tera **portao proprio** (`FR-07`).

### 5.3 O que passa a existir

| # | Objeto | Caminho | Estado apos o ato |
|---|---|---|---|
| **`O-1`** | **`PRO-medally`** — Carta de Produto 1.0.0 | `products/medally/carta.md` | `ativo` · `ratificada` |
| **`O-2`** | **Este ADR** | `decisions/ADR-0026-admissao-do-medally-como-primeiro-produto.md` | `ativo` · `ratificada` |

> **Dois objetos. Nenhum outro.** O diretorio `products/` nasce como **consequencia do caminho
> canonico** que `FND-03 §3.1`, `FND-09 §5.6` e `FND-10 §4.4` **ja declaravam** — nao e
> diretorio novo na norma, e a primeira instancia do que a norma previa.

### 5.4 O que a decisao **nao** faz — regras `AM`

| # | Regra |
|---|---|
| **`AM-01`** | **Nenhum byte do repositorio do medAlly entra no acervo.** Nem por copia, nem por referencia normativa, nem por adaptacao informal, nem por analogia (`FR-03`). Conteudo que entrar fora do portao e **nulo** e sua presenca e incidente de conformidade |
| **`AM-02`** | **Nenhuma `Spec` nasce deste ato.** A Carta **habilita** `SF-23` item (9); **criar a primeira `Spec` e mudanca propria**, com `DoR` de nove itens e `DoD` de dez. **`RD-33` so fecha apos a vigencia desta Carta**, e **nunca por inferencia** |
| **`AM-03`** | **Nenhuma norma do medAlly vira norma do acervo.** As sete linhas vermelhas de §4 da Carta sao **restricoes do Produto**, registradas para nao serem removidas em silencio — **nao** sao regras do LucaX Enterprise OS, e nao vinculam outro Produto |
| **`AM-04`** | **Este ato nao autoriza operar o medAlly com paciente real, dado real, producao, chamada externa nova, cobranca nova, alteracao de regra clinica ou alegacao regulatoria.** Os **sete** portoes clinico-juridicos permanecem **fechados**, e **nenhum deles se abre por decisao deste acervo** — cada um pertence a um titular externo |
| **`AM-05`** | **Este ato nao inventaria, nao nomeia e nao classifica nenhum outro produto** (`FR-07`). O nXtrack e citado **exclusivamente** como alternativa recusada por ausencia de evidencia, e **nao foi examinado** |
| **`AM-06`** | **Este ato nao emenda `ADR-0007`.** As duas lacunas medidas do portao *(§7 `L1` e `L2`)* nascem **declaradas**, com dono e gatilho — emendar o portao e mudanca **`C2` propria** |
| **`AM-07`** | **Nenhum departamento passa a operar o medAlly por este ato.** A tabela de responsaveis da Carta declara **de quem sera** a responsabilidade; o trabalho corrente permanece do CEO, fora do acervo |

## 6. Justificativa

| # | Fundamento |
|---|---|
| 1 | **E a unica alternativa com evidencia medida.** `B` perde por ausencia de dado, e a ausencia e **desta missao**, nao do candidato — o que esta declarado para que o Soberano possa reverter a escolha com informacao que so ele tem |
| 2 | **A norma pediu este exercicio por escrito.** `ADR-0007 §12` fixa o *"primeiro candidato real"* como gatilho de revisao **e** a ausencia prolongada como sinal de contorno. Exercer o portao **e cumprir a norma**, nao testa-la |
| 3 | **O resultado do portao e `REWRITE`, e isso protege o acervo.** A admissao mais barata *(`ADOPT`)* nao foi escolhida: **`0`** arquivos entram, e o custo de qualquer entrada futura permanece integral |
| 4 | **O teste de existencia passa, e passa pelo motivo mais fraco.** Um usuario nomeado. `FND-03 §3.1` pergunta *"alguem"*, nao *"muitos"* — e a fragilidade esta declarada em `R1` da Carta e **testada com prazo** por `H1`, em vez de dissolvida em adjetivo |
| 5 | **Tradeoff aceito, explicito:** o acervo passa a carregar um Produto cujo criterio de sucesso **ainda nao foi medido nenhuma vez** e cujo publico tem **um** membro. Aceita-se isso em troca de exercer duas camadas normativas contra um caso real — e o **criterio de encerramento de §6 da Carta e o preco declarado**: se `H1` for refutada, o Produto encerra |

## 7. Avaliacao do portao — **`G1`–`G5` bastaram?**

> `ADR-0007 §12` obriga esta secao: *"primeiro candidato real submetido ao portao — reavaliar
> se `G1`–`G5` sao suficientes e conferiveis na pratica"*.

**Resposta medida: sim para conferir, quase para bastar.** Os cinco foram **conferiveis sem
julgar merito**, exatamente como `ADR-0007 §6` previa. **Duas lacunas apareceram**, e nenhuma
delas impediu a admissao:

| # | Lacuna | Severidade | Estado |
|---|---|---|---|
| **`L1`** | **O portao nao distingue admitir *identidade* de admitir *conteudo*.** `G1` a `G5` sao escritos para *"conteudo externo"*, e o primeiro caso real precisou de uma distincao que **nenhuma das cinco condicoes nomeia** — sem ela, admitir um produto de **550 arquivos** poderia ser lido como admitir os 550 | **Media** | ⚠️ **ABERTO.** Dono **DEP-GOV**; gatilho *"segunda admissao pelo portao, ou emenda a `ADR-0007`"*. **Contornado, nao fechado:** a distincao esta escrita em `AM-01` e em `G3`, e vale para **este** caso |
| **`L2`** | **As quatro classificacoes de `G3` descrevem destino de *conteudo*, e nenhuma descreve *"admitir a existencia sem admitir nada"*.** `REWRITE` foi escolhida **por eliminacao**, e a sua definicao — *"a solucao do Legacy nao serve"* — **nao e literalmente verdadeira aqui**: a solucao do Legacy nao foi **avaliada**, porque nao foi **submetida** | **Media** | ⚠️ **ABERTO.** Dono **DEP-GOV**; mesmo gatilho. **`REWRITE` e a mais proxima e o seu efeito e o correto — `0` entradas, proveniencia `native`** —, e a imprecisao esta **declarada em vez de dissolvida** |

> **Isto e o valor de exercer o instrumento, e nao de le-lo.** As duas lacunas **nao apareceriam
> em nenhuma leitura de `ADR-0007`** — apareceram quando um candidato real foi passado pelas
> cinco condicoes, uma a uma. E o mesmo mecanismo de
> [`MEM-APR-0006`](../memory/aprendizado/MEM-APR-0006-exercer-o-contador-revela-o-defeito.md).

## 8. Evidencias

| # | Evidencia | Origem | Confianca | O que discrimina |
|---|---|---|---|---|
| `E1` | Entrevista real com o ortopedista piloto — perfil, gargalo, contrato do prontuario, erros perigosos e os **cinco** criterios do piloto | `kb/entrevista-felipe-2026-07-23.md`, no repositorio de origem | **Media — alegada, com proveniencia declarada** | Sustenta `K1`, `K2` e `K3`. **Nao foi verificada com o entrevistado por esta missao** |
| `E2` | Decisao de nascimento datada **2026-07-22**, aprovada pelo CEO | `docs/adr/056` do repositorio de origem | **Alta — documento lido** | Sustenta `G1` |
| `E3` | **7** portoes declarados, **`0`** liberados — `liberado: false`, `liberado_por: null`, `documento: null` nos sete | `config/portoes.json`, lido | **Alta — medida** | Sustenta `AM-04` e o estagio `construcao` |
| `E4` | **37 de 37** registros de trilha com `"ambiente": "simulacao"`; **`0`** em qualquer outro ambiente | Varredura das trilhas | **Alta — medida** | Prova que **nenhum paciente real foi atendido** |
| `E5` | **9** sensores · **91** rotas · **11** telas · **76** modulos · **28.093** linhas de nucleo · **50** arquivos de teste com **1.298** funcoes | Contagem por ferramenta | **Alta — medida** | Sustenta que o candidato **existe e roda**, contra a hipotese de projeto de papel |
| `E6` | **19** commits alcancam o caminho entre **2026-07-26** e **2026-07-30**; **282** arquivos rastreados; **6** modificados na arvore | Historico Git do repositorio hospedeiro | **Alta — medida** | Sustenta *"o Legacy esta em uso"*, que e a premissa do sinal de `ADR-0007 §12` |
| `E7` | **`0`** Produtos, **`0`** `Spec`s e **`products/` ausente** no acervo | Varredura do acervo | **Alta — medida** | Sustenta `G2`: **nao ha com que duplicar** |
| `E8` | O Soberano fixou *"`S1` com Produto real — `nXtrack`, **se seguir sendo o primeiro produto comercial**"* | [PS-2026-013 §7](../governance/pacote-soberano-2026-07-30-consolidado.md) | **Alta — citacao literal** | E a **colisao**, e o motivo de `Q1` ser bloqueante |
| **`A1`** | **Evidencia ausente, declarada:** **nenhum** criterio de sucesso do Produto foi medido; as 10 teleconsultas simuladas **nao ocorreram** | Carta §15 | — | `PI-10`, `LM-01` |
| **`A2`** | **Evidencia ausente, declarada:** **nada** foi medido sobre o **nXtrack**. Publico, problema, valor, estagio e sinal de uso sao **`desconhecido`**, e produzi-los exigiria o inventario que `FR-07` proibe | `FR-07` | — | E a razao pela qual `B` foi recusada **por ausencia**, nunca por demerito |
| **`A3`** | **Evidencia ausente, declarada:** **DEP-EXE nao se manifestou**, e `FND-01 §7.3` o exige como consulta obrigatoria | `RFC-0021 §10` | — | `LM-03`: silencio **nao** aprova |
| **`A4`** | **Evidencia ausente, declarada:** a alegacao de *"1440 testes verdes"* **nao foi reexecutada** — rodar a suite exigiria executar codigo no repositorio, e a missao veda escrita nele | Carta `E6` | — | `PI-10` |

## 9. Riscos e mitigacao

| # | Risco | Prob. | Impacto | Mitigacao |
|---|---|---|---|---|
| `RA-1` | **A decisao 7 ser contrariada sem que o Soberano perceba** | Media | **Alto** | `Q1` de §12 e **bloqueante** e a minuta do ato a enuncia **antes** dos objetos |
| `RA-2` | **Admissao por atacado do repositorio, por precedente** | Media | **Alto** | `AM-01`, `AM-05`, `G3` = `REWRITE` com **`0`** entradas, e `FR-07` — **cada admissao futura tem portao proprio** |
| `RA-3` | **O ato ser lido como autorizacao de operacao clinica real** | Media | **Alto** | `AM-04` e §4 da Carta; a minuta repete as sete linhas vermelhas em item proprio |
| `RA-4` | **`RD-33` ser dado por fechado no proprio ato** | **Alta** | Medio | `AM-02` e item expresso da minuta: **`RD-33` so fecha apos vigencia**, por missao ministerial separada |
| `RA-5` | **`H1` refutada — Produto com publico de um so** | Media | Medio | Criterio de encerramento da Carta §6, com sinal observavel e prazo |
| `RA-6` | **`L1` e `L2` do portao virarem contorno permanente** | Media | Medio | Nascem com **dono e gatilho** em §7. **Contorno declarado e divida; contorno silencioso e defeito** |

## 10. Plano de reversao

| Campo | Conteudo |
|---|---|
| **Reversivel?** | **Tipo 1 — nao trivialmente.** A reversao **existe**, e o seu custo cresce com o tempo |
| **Janela barata** | **Enquanto nenhuma `Spec` for criada e nenhum artefato depender de `PRO-medally`.** Nessa janela, reverter e: `O8`/`O9` sobre os dois objetos, remocao de `products/` **se e somente se a Carta nunca esteve `ativo`**, e reconciliacao dos indices |
| **Depois da primeira `Spec`** | **A remocao fisica passa a ser proibida** (`RB-05`), e o caminho e **`O9` — retirada**, declarando o que passa a valer no lugar (`SU-04`), com **todos** os dependentes tratados (`LC-05`, `RB-04`) |
| **Quem executa** | DEP-GOV, sob ato do Soberano |
| **O que a reversao NAO desfaz** | O exercicio do portao e as duas lacunas `L1`/`L2` — elas **permanecem achados validos** ainda que o Produto seja revertido |
| **Backup necessario (`PI-07`)** | **Copia datada do acervo antes da aplicacao.** **Nenhum dado vivo do medAlly e tocado em hipotese alguma** |

## 11. Classificacao

| Campo | Valor |
|---|---|
| **Classe de mudanca** | **`C2` — Estrutural** |
| **Tipo de reversibilidade** | **`Tipo 1`** |
| **Aprovador** | **SOBERANO** |
| **Ratificador** | **SOBERANO** — indelegavel (`PI-01`, `PI-06`) |
| Instrumento | **RFC → ADR → Ratificacao** ([RFC-0021](../rfcs/RFC-0021-admissao-do-medally-como-primeiro-produto.md)) |
| Fitness Check | **Obrigatorio** (`CV-07`, `QG-6`) — [FIT-2026-019](../governance/fitness/FIT-2026-019-admissao-do-medally.md) |
| Data da decisao | *(em branco — o ato nao ocorreu)* |
| Data de vigencia | *(em branco)* |

> **Por que `C2` e nao `C3`.** `FND-04 §2` da a hipotese literal: C2 *"cria, altera ou remove
> **um componente**"*, e a linha de exemplo diz **"criar produto"**. C3 exigiria alterar
> principio imutavel, linha vermelha, hierarquia normativa, direitos de decisao ou a Fundacao —
> e **nenhum** e tocado: `0` fundacionais emendadas, `0` titulares criados, `0` niveis movidos.
> `GV-03` foi considerado e **nao se aplica**: nao ha duvida a resolver, porque a hipotese de C2
> **nomeia o caso**.
>
> **Por que `Tipo 1`.** `FND-07 §2.1` lista entre os indicadores *"qualquer coisa que outros
> passarao a assumir como dado"* — e `PRO-medally` passa a ser a **pre-condicao de existencia**
> de toda `Spec` futura. Alem disso, `FND-09` E-17 e `FND-03 §3.1` **ja fixam** criacao de
> Produto como Tipo 1 do Soberano: a classificacao **e derivada de norma, nao escolhida**.
>
> **Por que o aprovador e o SOBERANO e nao DEP-EXE — `Q3`.** Ha **colisao declarada**:
> `FND-07 §2.4` da *"C2 · Tipo 1 → DEP-EXE propoe / SOBERANO ratifica"*, enquanto
> `FND-01 §7.3` da, para **portfolio: criar produto**, *"decide **Soberano**"*, e
> `FND-09 §8.2` linha `PRO` da *"aprova **SOBERANO**"*. **Duas fontes de nivel superior
> convergem no Soberano; uma fonte de nivel 2 nomeia DEP-EXE para a classe.** Aplica-se
> `FND-01 §10` *(precedencia)* e `GV-03` *(na duvida, a mais alta)*: **aprovador e ratificador
> convergem no mesmo ato**, e DEP-EXE permanece como **consulta obrigatoria**, cuja ausencia
> esta declarada em `A3`. **A escolha esta submetida como `Q3`, nao presumida.**

## 12. Questoes submetidas ao Soberano

| # | Questao | Bloqueia? |
|---|---|---|
| **`Q1`** | **A decisao 7 de `PT-2026-009 §1` fixou o nXtrack como primeiro produto *comercial* (`L1`) ou como primeiro Produto *do acervo* (`L2`)?** Sob `L2`, **este ADR e inadmissivel** sem ato que altere aquela decisao | ✅ **SIM** |
| `Q2` | **Emendar `ADR-0007` para fechar `L1` e `L2` do portao, ou mante-los declarados?** | ❌ Nao |
| `Q3` | **Confirmar o SOBERANO como aprovador**, e nao DEP-EXE — §11 | ❌ Nao |
| `Q4` | **Confirmar o estagio `construcao`** para produto que roda com **`0`** usuarios reais | ❌ Nao |

## 13. Revisao

| Campo | Conteudo |
|---|---|
| **Gatilho por evento** | **Segunda admissao pelo portao** — reavaliar `L1` e `L2` |
| **Gatilho por evento** | **Primeira `Spec` de `PRO-medally`** — o unico evento que torna `SF-01` a `SF-32` observados |
| **Gatilho por evento** | **Primeira medicao de `M1` a `M5`** da Carta, ou **2026-10-31** |
| **Gatilho temporal** | 2027-01-31 |
| **Sinal de que esta decisao deu errado** | (a) **`H1` refutada** — nenhum segundo medico aceita usar, e o Produto e ferramenta de uma pessoa; (b) **conteudo do repositorio aparecer no acervo sem portao proprio** — sinal de que `AM-01` virou formalidade; (c) **`RD-33` declarado fechado antes da vigencia** |
| **Responsavel pela revisao** | **DEP-QAR** |

## 14. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Origem | [RFC-0021](../rfcs/RFC-0021-admissao-do-medally-como-primeiro-produto.md) |
| Portao aplicado | [ADR-0007 §5.3](ADR-0007-fronteira-greenfield-legado.md) — `G1`–`G5` |
| Classificacao `G3` | **`REWRITE`** — proveniencia resultante **`native`** |
| Decisoes superadas | **Nenhuma.** `ADR-0007` e **exercido**, nao superado; `ADR-0021` e **habilitado em parte**, nao alterado |
| Artefatos criados pelo ato | **`PRO-medally`** *(Carta 1.0.0)* · **este ADR** |
| Artefatos do acervo alterados pelo ato | **`0` fontes normativas.** Somente projecoes `M3` — catalogo e indices — pela mesma mudanca (`CV-04`, `IX-02`) |
| Bytes admitidos do repositorio de origem | **`0`** |
| Pacote soberano | [PS-2026-014](../governance/pacote-soberano-2026-07-31-medally.md) |
| Verificacao de aptidao | [FIT-2026-019](../governance/fitness/FIT-2026-019-admissao-do-medally.md) |
| Registros de memoria gerados | Camada **PRD** *(via Carta)*; camada **APR** *(a licao de §7)* |
| Achados abertos por esta decisao | **`L1`** e **`L2`** de §7 — registrados no catalogo como **`RD-54`** e **`RD-55`** |

---

## Checklist de validade (FND-07 §4.1)

- [x] `VD-01` — 3 alternativas reais + *"nao fazer nada"*
- [x] `VD-02` — criterios declarados antes das alternativas (`RFC-0021 §4`, antes de §5)
- [x] `VD-03` — nenhuma alternativa de palha: **B e a decisao ja fixada pelo Soberano**, e §4 declara em que hipotese ela vence
- [x] `VD-04` — tradeoff aceito explicito (§6, item 5)
- [x] `VD-05` — **quatro** ausencias de evidencia declaradas (`A1` a `A4`)
- [x] `VD-06` — reversao declarada, com janela barata e custo crescente (§10)
- [x] `VD-07` — impacto em cascata mapeado (`RFC-0021 §7`)
- [x] `VD-08` — data e responsavel presentes
- [x] `VD-09` — gatilhos de revisao definidos (§13)
- [x] Proponente ≠ aprovador · revisor ≠ autor · guardiao ≠ proponente

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-31 | DEP-PRD | Decisao inicial, **`em-revisao`, nao vigente**. Aplica `G1`–`G5` ao **primeiro candidato real** do portao de `ADR-0007`; classifica **`G3` = `REWRITE`** com **`0`** bytes admitidos; cria `PRO-medally` e `products/` **somente por ato**. **7** regras `AM` do que a decisao nao faz; **2** lacunas do portao (`L1`, `L2`) abertas com dono e gatilho; **4** ausencias de evidencia declaradas; **4** questoes ao Soberano, sendo **`Q1` bloqueante**. |
