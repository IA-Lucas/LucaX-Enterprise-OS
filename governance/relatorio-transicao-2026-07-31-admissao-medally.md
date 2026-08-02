---
id: PT-2026-011
titulo: Relatorio de transicao da Missao 1.13.4 — S1, a admissao canonica do medAlly
tipo: relatorio
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-07-31
atualizado_em: 2026-07-31
revisao_prevista: null
decisoes_relacionadas: [ADR-0007, ADR-0012, ADR-0020, ADR-0021, ADR-0026]
substitui: []
substituido_por: null
resumo: Registra o que a Missao 1.13.4 fez e nao fez — o primeiro exercicio do portao de origem externa, dois objetos submetidos e nenhum Produto em vigor — e os sete achados que o exercicio revelou.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# PT-2026-011 — Missao 1.13.4: admissao canonica do medAlly

> **NENHUM Produto entrou em vigor.** `products/` **nao existe** na raiz do acervo, **`0`**
> artefatos de tipo `PRO` estao vigentes, **nenhuma `Spec` nasceu** e **`RD-33` permanece
> bloqueante**. O que esta missao produziu foi um **rito completo, submetido e nao aplicado**.
>
> **E a primeira missao do acervo em que o portao de origem externa de `ADR-0007` e exercido.**

## Proposito

Registrar o que a Missao 1.13.4 fez, o que **nao** fez, o que mediu e o que descobriu.

## Escopo

| Item | Definicao |
|---|---|
| Inclui | A reproducao da baseline; a evidencia de Produto; o exercicio de `G1`–`G5`; a Carta candidata; o rito `C2 · Tipo 1`; o pacote soberano; a reconciliacao; os **sete** achados novos; e a preparacao da 1.13.5 |
| **Nao** inclui | O **merito** do medAlly · **qualquer conteudo** do seu repositorio · a escolha entre medAlly e nXtrack, que e do **Soberano** · o inventario de outro produto · `RD-49`, `RD-47`, `RD-48`, `RD-43`, `RD-13`, `RD-36` e as ressalvas de `FIT-2026-018`, **expressamente fora do escopo e mantidos abertos** |
| Natureza | **Reporte.** Nenhum tipo, entidade, camada ou diretorio novo |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| **Propoe o Produto** | **DEP-PRD** | `FND-09 §8.2`, linha `PRO` |
| **Confere o portao** | **DEP-GOV** | `ADR-0007 §5.3` — sem julgar merito |
| **Revisa e verifica** | **DEP-QAR** | `G4`; `ADR-0005` |
| **Decide** | **SOBERANO** | `FND-01 §7.3`, linha *Portfolio*. **Ainda nao decidiu** |

---

## 1. O que foi produzido

| # | Artefato | Onde | Estado |
|---|---|---|---|
| 1 | **Carta candidata `PRO-medally`** | **fora do acervo**, em `_candidatos-LucaX-Enterprise-OS-2026-07-31-M1.13.4/products/medally/carta.md` | **candidato** — nao esta no acervo |
| 2 | [`RFC-0021`](../rfcs/RFC-0021-admissao-do-medally-como-primeiro-produto.md) | `rfcs/` | `aprovado` **quanto a forma** |
| 3 | [`ADR-0026`](../decisions/ADR-0026-admissao-do-medally-como-primeiro-produto.md) | `decisions/` | **`em-revisao` · `ratificacao: pendente`** — **retido por falta de ato** |
| 4 | [`PS-2026-014`](pacote-soberano-2026-07-31-medally.md) | `governance/` | submetido |
| 5 | [`FIT-2026-019`](fitness/FIT-2026-019-admissao-do-medally.md) | `governance/fitness/` | `apto-com-ressalva` |
| 6 | **este relatorio** | `governance/` | — |

## 2. A evidencia de Produto — separada por natureza

| Dimensao | Resposta | Natureza |
|---|---|---|
| **Caminho** | `E:/LucasIA/Projetos/lucaX/My_WorkSpace/Meus_projetos/medally` — **550** arquivos | **observado** |
| **Estagio** | **construcao** — nucleo executavel entregue, **`0`** usuarios reais | **inferido** de observado |
| **Licenca** | **nenhuma** — `0` arquivos `LICENSE`/`LICENCA`/`COPYING` | **observado** |
| **Documentacao** | **32** arquivos `.md`, entre eles estado vivo, checklists, API e parecer juridico pre-operacional | **observado** |
| **Publico** | **Um** ortopedista nomeado, com entrevista real; paciente como persona secundaria; clinica como terciaria **nao entrevistada** | **alegado** *(entrevista)* + **observado** *(o documento existe)* |
| **Problema** | Papelada compete com o tempo de captacao; registro precisa sustentar reembolso; erros de lateralidade, dose e negacao ferem paciente | **alegado** pelo proprio medico |
| **Valor** | Devolver tempo sem transferir o risco de um registro que o medico nao escreveu | **inferido** |
| **Sinais de uso** | **37** registros de trilha — **37 de 37** em `"ambiente": "simulacao"`; **3** sessoes de treino *(2026-07-27)*; **7** consultas semeadas *(2026-07-30)*; **19** commits em **5** dias | **observado** |
| **Estrutura** | **9** sensores · **91** rotas · **11** telas · **76** modulos · **28.093** linhas de nucleo · **50** arquivos de teste com **1.298** funcoes | **observado** |
| **"1440 testes verdes"** | **nao reexecutado** — rodar a suite seria escrever no candidato | **alegado** |
| **Mercado, preco, segundo usuario, concorrencia** | — | **desconhecido** |

### 2.1 O teste de existencia

> *"Se for descontinuado, quem perde o que?"* (`FND-03 §3.1`)

**Passa — pelo motivo mais fraco possivel: um usuario nomeado.** O ortopedista perde o unico
instrumento existente para o registro ancorado da consulta dele, e **nao tem prontuario
eletronico proprio**; o CEO perde 550 arquivos e 28.093 linhas de nucleo; o acervo perde o
**unico** caminho de desbloqueio de `RD-33` com evidencia. **Paciente real nao perde nada**,
porque nenhum e servido.

**Ausencia comprovada de publico, problema ou valor bloquearia a Carta. Nenhuma das tres se
comprovou ausente** — e a fragilidade do "um" esta **declarada e datada**, nao dissolvida.

## 3. O portao de `ADR-0007` — exercido pela primeira vez

| Condicao | Estado | Sintese |
|---|---|---|
| **`G1`** proveniencia | ✅ | Caminho, natureza, autor *(CEO)*, data de origem *(`ADR-056`, 2026-07-22)* e data de observacao *(2026-07-31)*, com `HEAD` do repositorio hospedeiro registrado |
| **`G2`** fit-gap | ✅ | **O acervo nao tem nada que responda a mesma pergunta:** `0` Produtos, `0` `Spec`s, `products/` ausente. **Nao ha duplicacao possivel** |
| **`G3`** classificacao | ✅ | **`REWRITE`** — exatamente uma, com as outras tres eliminadas por escrito |
| **`G4`** validacao independente | ✅ | **DEP-QAR**, **15** controles, **4** ressalvas — `PS-2026-014 §5` |
| **`G5`** decisao formal | ⏳ | **PREPARADA** — `ADR-0026` existe, `em-revisao`, e **so o ato lhe da eficacia** |

### 3.1 `G1`–`G5` bastam? **Sim para conferir. Quase para bastar.**

`ADR-0007 §12` obrigava esta avaliacao no primeiro caso real. **Tres lacunas apareceram, e
nenhuma delas seria visivel por leitura:**

| # | Lacuna | Achado |
|---|---|---|
| **1** | **O portao nao distingue admitir *identidade* de admitir *conteudo***. As cinco condicoes sao escritas para *"conteudo externo"*; sem uma distincao que **nenhuma delas nomeia**, admitir um produto de **550** arquivos poderia ser lido como admitir os 550 | **`RD-54`** |
| **2** | **As quatro classificacoes de `G3` descrevem destino de conteudo**, e nenhuma descreve *"admitir a existencia sem admitir nada"*. **`REWRITE` foi escolhida por eliminacao**, e a sua definicao — *"a solucao do Legacy nao serve"* — **nao e literalmente verdadeira**: a solucao **nao foi avaliada**, porque **nao foi submetida** | **`RD-55`** |
| **3** | **`G1` exige *"em que data foi observado"*, e data nao basta para repositorio vivo.** O candidato mudou **entre a abertura e o fechamento da mesma missao**. O instante so ficou fixado porque a missao produziu um **manifesto `sha256`** — **que `G1` nao pede** | **`RD-59`** |

> **O efeito de `REWRITE` e o correto — `0` entradas, proveniencia `native` — e a imprecisao do
> nome esta declarada em vez de dissolvida.** As duas nascem com dono **DEP-GOV** e gatilho
> *"segunda admissao pelo portao, ou emenda a `ADR-0007`"*, e `Q2` do pacote pergunta ao
> Soberano se devem ser emendadas agora.

## 4. A colisao com a decisao **7** — declarada, nao contornada

A decisao **7** de [§1 do relatorio anterior](relatorio-transicao-2026-07-30-convergencia.md)
registra que o Soberano fixou *"`S1` com Produto real — **`nXtrack`, se seguir sendo o primeiro
produto comercial**"*.

**Esta missao submete outro produto.** A condicao esta **escrita no proprio registro**, e admite
duas leituras:

| Leitura | Consequencia |
|---|---|
| **`L1`** — a condicao e sobre ser o primeiro produto **comercial** | A decisao 7 fica **intacta**, e nada impede que o **primeiro Produto do acervo** seja outro |
| **`L2`** — a decisao 7 fixou o nXtrack como primeiro Produto **do acervo** | **O pacote inteiro e inadmissivel** sem ato que altere aquela decisao |

**A escolha e do Soberano, e e a questao `Q1`** — a unica bloqueante, e o **item `0`** da minuta,
**antes** de qualquer objeto.

> **O nXtrack nao foi examinado, e isso e cumprimento de norma, nao omissao.** `FR-07` proibe
> levantamento amplo previo: *"o portao opera sobre um candidato por vez, nomeado"*. A alternativa
> **B** de `RFC-0021` foi recusada **por ausencia de evidencia desta missao**, jamais por
> demerito — e o texto diz, literalmente, que **se o Soberano souber do nXtrack o que esta
> missao nao pode saber, `B` vence `A`**.

## 5. O metodo — o que esta missao fez diferente

### 5.1 O instrumento foi validado antes do uso, e a calibracao **reprovou a primeira versao**

`IR-02`/`IR-03` foram reimplementados e conferidos contra **hashes ja publicados** — **10
controles**, entre eles `FND-10` em `CRLF` — **antes** de medir qualquer objeto novo.

**A primeira versao reprovou em `FND-03`**, e o motivo importa: ela removia **toda** linha cujo
texto antes do primeiro `:` fosse uma chave de `IR-03`, **inclusive linhas do corpo**. `FND-03`
e a taxonomia — ela **fala sobre** `status` e `ratificacao` no corpo, e o filtro os comia.
Resultado: `9e020eda…cf7d` contra o publicado `1004673a…4b4e`.

`RA-4` de `ADR-0012` ja dizia como era: *"o filtro e por chave de **frontmatter**"*. Corrigido
para operar **somente dentro do bloco delimitado por `---`**, o instrumento passou a reproduzir
**10 de 10**.

> **Segunda missao seguida em que exercer o instrumento revela o defeito do instrumento**
> ([`MEM-APR-0006`](../memory/aprendizado/MEM-APR-0006-exercer-o-contador-revela-o-defeito.md)).
> **Medir os objetos novos primeiro teria publicado dois `H-N` errados sem nenhum sinal de erro**
> — e o erro so apareceria no ato seguinte, quando alguem tentasse reproduzi-los.

### 5.2 A evidencia foi **medida**, e a alegacao foi **marcada como alegacao**

O repositorio do candidato declara *"1440 testes verdes"*. Esta missao **contou 1.298 funcoes
`test_` em 50 arquivos** — e **nao concluiu divergencia**: casos parametrizados contam mais de
uma vez, e a alegacao **nao foi reexecutada** porque rodar a suite seria **escrever** no
candidato. **O numero alegado esta registrado como alegado; o medido, como medido.**

### 5.3 Zero escrita no candidato — e a prova mudou de natureza no meio da missao

Manifesto `sha256` de **527** arquivos, tomado **antes** de qualquer leitura de conteudo e
**remedido** no fechamento. **Ele nao reproduziu** — e o motivo importa mais do que o susto:
**o candidato mudou sozinho, no mesmo dia, entre a abertura e o fechamento.**

| Delta | Quantidade | Onde |
|---|---|---|
| Novos | **1** | `docs/demonstracao/felipe/tudo.html` |
| Alterados | **15** | **12** sob `docs/demonstracao/` e **3** geradores em `ferramentas/` |
| Removidos | **`0`** | — |

**Nenhuma escrita e atribuivel a esta missao**, e a prova passou a ser o **recorte**, nao o
manifesto: **`0`** dos 16 caminhos foi lido, aberto ou executado; **as 5 fontes efetivamente
consumidas estao byte a byte identicas**; **todas** as contagens publicadas remedem igual
*(**9** sensores, **91** rotas, **11** telas, **76** modulos, **28.093** linhas, **50** arquivos
de teste, **1.298** funcoes, **32** `.md`, **37 de 37** trilhas em `simulacao` e **`0`** em
qualquer outro ambiente)*; e o **`HEAD` de referencia nao mudou**. **A unica contagem que se
moveu foi o total de arquivos: 550 → 551.**

> **As contagens da Carta e de `ADR-0026` sao as do INSTANTE DE ABERTURA, e os dois objetos NAO
> foram reeditados.** Reescrever objeto ja hasheado para perseguir uma arvore viva quebraria
> `H-A`, `H-N` e `H-P` **sem ganho de verdade**, e recomecaria na medicao seguinte. **A
> reconciliacao vive em [PS-2026-014 §2.2](pacote-soberano-2026-07-31-medally.md)**, que e o
> documento que **pode** mudar.
>
> **Isto e a terceira lacuna medida do portao — `RD-59`.** `G1` exige *"em que data foi
> observado"*, e **data nao basta para repositorio vivo**. O que salvou a evidencia foi o
> manifesto — **produzido por determinacao da missao, nao por `G1`**.

## 6. Reconciliacao — `CV-04`, `RG-03`

| Alvo | O que mudou |
|---|---|
| [`artifact-registry`](artifact-registry.md) | §2 *(estado)*, §4.2 *(`ADR-0026`)*, §4.5 *(`FIT-2026-019`)*, §4.7 e §4.6 *(registros e indices)*, §7 *(achados **`RD-53`** a **`RD-58`**)*, §9 *(proveniencia — o **primeiro** `legacy-candidate` do acervo)*, §10 *(baseline nova)* |
| [`rfcs/README`](../rfcs/README.md) | `RFC-0021` indexada |
| [`decisions/README`](../decisions/README.md) | `ADR-0026` indexado, **`em-revisao`** |
| [`governance/README`](README.md) · [`fitness/README`](fitness/README.md) | Contadores, `PS-2026-014`, `PT-2026-011` e `FIT-2026-019` |
| [`README`](../README.md) da raiz | Baseline, contagem e estado |

## 7. Achados abertos por esta missao

| # | Achado | Severidade | Estado |
|---|---|---|---|
| **`RD-53`** | **O comando publicado da baseline nao reproduzia `BL-2026-07-30-01` sobre a copia datada em que ela foi medida.** O comando exclui `./.obsidian/*` e `./_SAIDA-COMPANY-OS/*`, e a raiz continha tambem **`_candidatos/`** com **13** arquivos `.md`: executado como publicado, da **198**, nao **185**. **E `§10.9` declara que os tres candidatos de `FND-01` *"permanecem em `_candidatos/`"* — diretorio que NAO existe na raiz do acervo hoje.** Os tres arquivos **existem**, com **490 · 488 · 492** linhas e hashes que reproduzem os publicados, em `_backups/…_2026-07-30_pre-missao-1-13-3/_candidatos/` | **Media** | ⚠️ **ABERTO.** **A baseline vigente `BL-2026-07-30-02` reproduz** — **189 · 55.280 · `a3ca6ce3…ca5d`** —, porque `_candidatos/` ja nao esta na raiz. **`BL-2026-07-30-01` NAO e editada** (`BL-02`). **Segunda ocorrencia da familia de `RD-17`**, e **decima terceira** da familia de `MEM-APR-0002`. **Mitigado nesta missao pela escolha de caminho:** os candidatos de 1.13.4 vivem **fora** do acervo |
| **`RD-54`** | **O portao de `ADR-0007 §5.3` nao distingue admitir *identidade* de admitir *conteudo*** | **Media** | ⚠️ **ABERTO.** Dono **DEP-GOV**; gatilho *"segunda admissao, ou emenda a `ADR-0007`"*. **Contornado por `AM-01` e `G3`, nao fechado** |
| **`RD-55`** | **As quatro classificacoes de `G3` descrevem destino de conteudo; nenhuma descreve *"admitir existencia sem admitir nada"*.** `REWRITE` foi escolhida **por eliminacao** | **Media** | ⚠️ **ABERTO.** Mesmo dono e gatilho. **O efeito e correto; o nome e impreciso, e a imprecisao esta declarada** |
| **`RD-56`** | **`TPL-carta-produto` 1.0.0 nao preve `capabilities` no frontmatter nem os cinco campos de `FND-10 §2.2`**, embora `FND-09` E-17 declare `capabilities` como **atributo minimo** de `PRO` e `FND-04 §6` faca do vinculo a Capability **pre-condicao universal I**. Nao ha secao para **Capabilities consumidas** nem para **interfaces**. **A Carta candidata os declara assim mesmo**, por norma superior — e por isso **excede o template** | **Media** | ⚠️ **ABERTO.** Dono **DEP-GOV** *(forma)* + **DEP-PRD** *(conteudo)*; gatilho *"antes da segunda Carta de Produto"*. **Segunda ocorrencia da familia de `RD-23`** — template que contradiz a norma que deveria instrumentar. **Nao corrigido:** emendar template e `C2` propria, e a missao veda correcao silenciosa |
| **`RD-57`** | **Este catalogo divergia de si proprio em CINCO lugares, todos anteriores a esta missao:** `resumo` **169**, §Escopo **164**, §2 **185 · 54.190**, a conferencia de §4 somando **185** com um `10` que a **propria §4.1** contradiz desde `FND-11`, e §9 **169** `native` — contra **189 · 55.280** em §10.0 do **mesmo documento** | **Media** | ✅ **CORRIGIDO na projecao**, valor a valor, **medido por ferramenta**, **`0` fontes alteradas** (`PJ-03`, `RG-03`). **Sexta ocorrencia** de o catalogo divergir de si proprio, **decima quarta** da familia de `MEM-APR-0002`. **A emissao anterior remediu §10 e §4.1 e nao remediu os agregados que os resumem** |
| **`RD-58`** | **[`governance/README`](README.md) mantem uma DUPLICATA do contador `FIT`, tres emissoes atras.** Declarava **`016` / `017`** enquanto a **linha seguinte do mesmo arquivo** reconhece [`fitness/README`](fitness/README.md) como a **fonte**, e la o valor era **`018` / `019`** | Baixa | ✅ **Valor corrigido na projecao.** **O defeito nao e a divergencia: e a duplicata** (`PJ-01`), e **suprimir a linha e mudanca de estrutura do indice** — fica **declarada, nao executada**. **Quarta ocorrencia da familia dentro do mesmo arquivo**, apos `RD-04`, `RD-32` e `RD-52` |
| **`RD-59`** | **`G1` do portao exige *"em que data foi observado"*, e data nao basta para repositorio vivo.** O candidato mudou **entre a abertura e o fechamento da mesma missao** — **1** arquivo novo e **15** alterados, todos material de demonstracao e seus geradores. **A evidencia continua valida**, porque o instante ficou fixado por um manifesto `sha256` *(`cc6fbbcf…aadc`)* — **mas esse manifesto foi produzido por determinacao da missao, nao exigido por `G1`** | **Media** | ⚠️ **ABERTO.** Dono **DEP-GOV**; gatilho *"segunda admissao pelo portao"*. **Terceira lacuna medida do portao.** A correcao possivel e barata: `G1` passar a exigir **instante verificavel** *(commit, manifesto ou hash de arvore)*, e nao data |

## 8. O que esta missao NAO fez

| # | Nao feito | Por que |
|---|---|---|
| 1 | **Nenhum Produto entrou em vigor** · `products/` **nao existe** | Criar Produto e **`C2 · Tipo 1` do Soberano**. **`RD-33` permanece bloqueante** |
| 2 | **Nenhuma `Spec`, Projeto, Skill, Tool, Command, Workflow, Agente, codigo ou infraestrutura** | Limite expresso da missao |
| 3 | **Nenhum byte escrito no repositorio do medAlly** | Determinacao da missao — provado por manifesto de **527** arquivos |
| 4 | **Nenhum byte do repositorio admitido no acervo** | `G3` = `REWRITE`; `AM-01` |
| 5 | **`ADR-0007` nao emendado** | As duas lacunas nascem **declaradas**; emendar e `C2` propria |
| 6 | **Nenhuma fundacional emendada; nenhum artefato historico, `MSG`, `FIT` ou baseline editado** | `LV-04`, `BL-02`, `CC-01` — **`0` bytes** |
| 7 | **Nenhum outro produto inventariado** | `FR-07` |
| 8 | **`RD-49`, `RD-47`, `RD-48`, `RD-43`, `RD-13`, `RD-36` mantidos abertos** | Fora do escopo — **nao se fecham por inferencia** |
| 9 | **`RD-54`, `RD-55` e `RD-56` nao corrigidos** | Correcao silenciosa e **proibida**, e os tres exigem **rito proprio**: dois emendam `ADR-0007`, um emenda `TPL-carta-produto`. **`RD-53` nao e corrigivel** — `BL-02` proibe editar baseline. **`RD-57` e `RD-58` foram corrigidos NA PROJECAO**, com o achado registrado — que e o oposto de correcao silenciosa |

## 9. Preparacao da Missao 1.13.5 — **uma** necessidade candidata a primeira `Spec`

> **Nenhuma `Spec` e criada aqui**, e **nenhuma e criavel** enquanto o ato nao ocorrer
> (`SF-23` item **9**). O que segue e **candidata nomeada**, nao Spec.

| Campo | Conteudo |
|---|---|
| **Necessidade** | **O texto que o medico digita no caderno da sala nao sobrevive a um reinicio do processo.** O caderno vive em memoria, junto da `Sala`; reiniciar o servidor no meio de uma consulta **perde o que ele digitou e ainda nao atravessou** para o prontuario |
| **Evidencia** | `ESTADO-medally.md`, secao *"Lacunas TECNICAS — trabalho que falta, nao decisao humana"*, **primeiro item**, atribuido ao `ADR-122` do repositorio de origem. O proprio texto declara que *"a consequencia agora e maior, porque antes o que se perdia era fala simulada e agora e texto dele"* — **`observado`**: o documento existe e foi lido |
| **Por que e atual** | Consta das lacunas **abertas**, nao das fechadas. O produto esta em **RC1** e o proximo passo declarado sao **10 teleconsultas simuladas com o medico** — exatamente o cenario em que o caderno e usado |
| **Por que e real** | O que se perde **e texto do medico**, nao saida de maquina. E a unica lacuna aberta cuja perda tem **autor humano** |
| **Por que e de baixo risco** | **Nao abre portao nenhum** dos sete · **nao toca regra clinica** · **nao alcanca dado real de paciente** *(so existe `simulacao`)* · **nao cria chamada externa** · **nao cria cobranca** · **nao faz alegacao regulatoria**. Nenhuma das sete linhas vermelhas e tocada |
| **Forma de `Spec`** | Declara **o que deve ser verdadeiro** — *"o caderno de uma consulta aberta sobrevive ao reinicio do processo"* — e **como se verifica** — reiniciar durante consulta aberta e reabrir. **Nao decide o como**, que e de engenharia |
| **Restricao que a `Spec` teria de carregar** | O produto ja tem regra propria de que **dado clinico so e escrito pela fronteira de armazenamento**, com prova estrutural no repositorio. A `Spec` teria de declarar isso como **requisito NEGATIVO** — e isso a **fortalece**, porque `SF-25` exige as quatro categorias |
| **O que esta missao NAO fez** | Nao escreveu a `Spec` · nao atribuiu `SPC-id` · nao incrementou contador · nao respondeu ao `DoR` de nove itens |

> **Alternativas consideradas e nao escolhidas**, para que a escolha seja auditavel: *(a)* a
> trilha de auditoria sem `HMAC` nao detectar reescrita integral — **e capacidade que ja existe**
> e a lacuna e **operacional**, nao de definicao; *(b)* a rota `POST /tempo` sem chamador — o
> proprio repositorio declara que **removê-la e decisao a tomar com o medico**, e Spec nao decide
> por ele; *(c)* a licenca ausente — **nao e necessidade do produto**, e corrigi-la seria escrita
> no repositorio, vedada. **A escolha e (1) por ser a unica atual, real, de baixo risco e com
> forma de `Spec`.**

## 10. Decisao

**`READY-FOR-RATIFICATION`, com uma questao bloqueante que precede o ato.**

Os candidatos estao **integros**: `G1`–`G4` **comprovados** e `G5` **preparado**; Carta conforme
o template **e alem dele**, onde a norma superior exige; revisao independente com **15**
controles; **`0`** Produtos ativos; **`0`** bytes escritos no medAlly; **`0`** links quebrados;
**`0`** autoverificacoes; **`0`** credenciais; baseline e pacote **reproduziveis**.

**A integridade nao decide `Q1`.** Sob a leitura `L2` da decisao **7**, o pacote e inadmissivel
sem ato que a altere — e **so o Soberano pode ler a propria decisao**. Por isso a minuta comeca
pelo item **`0`**, que resolve `Q1` **antes** de qualquer objeto: escolhida `L2`, **o ato para
ali**, e nenhum item seguinte tem efeito.

**Apos ato soberano valido, uma missao ministerial separada aplica, verifica e libera a 1.13.5.**
**`RD-33` so fecha apos a vigencia** — nunca por este relatorio, pelo pacote ou pelo ato.

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-31 | DEP-GOV | Relatorio da **Missao 1.13.4**. **Primeiro exercicio do portao de `ADR-0007`**: `G1`–`G4` comprovados, `G5` preparado, `G3` = **`REWRITE`** com **`0`** bytes admitidos. **Dois** objetos submetidos, `H-N` invariante **2 de 2**, `IR-09` **2 de 2**, instrumento validado em **10 de 10** apos a calibracao reprovar a primeira versao. **Sete** achados novos — `RD-53` a `RD-59`. **Uma** candidata a primeira `Spec`, nomeada e nao criada. Decisao **`READY-FOR-RATIFICATION`**, com **`Q1`** bloqueante. |
